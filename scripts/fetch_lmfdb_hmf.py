#!/usr/bin/env python3
"""Fetch Hilbert modular-form data from LMFDB without Sage or Magma.

Uses only Python's standard library.  For each label it downloads the official
LMFDB ``download/sage`` text endpoint, then extracts the Hecke polynomial,
prime-ideal list and Hecke eigenvalue list as raw algebraic expressions.

Examples:
  python3 fetch_lmfdb_hmf.py --label 2.2.5.1-10125.1-a
  python3 fetch_lmfdb_hmf.py --prefix 2.2.5.1-10125.1 --max-orbits 40 -o c23_lmfdb.json
"""

from __future__ import annotations

import argparse
import json
import re
import string
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

BASE = "https://www.lmfdb.org/ModularForm/GL2/TotallyReal"
USER_AGENT = "beal-357-research/1.0 (stdlib-only LMFDB data client)"


def orbit_suffix(index: int) -> str:
    """LMFDB-style lowercase suffixes: a,...,z,aa,ab,..."""
    if index < 0:
        raise ValueError("index must be nonnegative")
    out = ""
    n = index
    while True:
        n, r = divmod(n, 26)
        out = string.ascii_lowercase[r] + out
        if n == 0:
            return out
        n -= 1


def fetch_text(url: str, timeout: float) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read()
        charset = resp.headers.get_content_charset() or "utf-8"
    text = data.decode(charset, errors="replace")
    lowered = text.lower()
    if "recaptcha" in lowered or "checking your browser" in lowered:
        raise RuntimeError("LMFDB returned an anti-bot page instead of data")
    return text


def balanced_list(text: str, assignment: str) -> str:
    marker = assignment + " = ["
    start = text.find(marker)
    if start < 0:
        raise ValueError(f"missing assignment {assignment}")
    left = text.find("[", start)
    depth = 0
    for pos in range(left, len(text)):
        ch = text[pos]
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
            if depth == 0:
                return text[left : pos + 1]
    raise ValueError(f"unterminated list for {assignment}")


def parse_download(label: str, text: str) -> dict[str, Any]:
    if text.strip() == "No such form":
        raise LookupError(label)
    hecke_match = re.search(r"^heckePol\s*=\s*(.+)$", text, re.MULTILINE)
    level_match = re.search(r"^NN\s*=\s*ZF\.ideal\((.+)\)$", text, re.MULTILINE)
    if not hecke_match:
        raise ValueError("missing heckePol")
    return {
        "label": label,
        "source_url": f"{BASE}/2.2.5.1/holomorphic/{label}/download/sage",
        "hecke_polynomial": hecke_match.group(1).strip(),
        "level_ideal_expression": level_match.group(1).strip() if level_match else None,
        "primes_array_raw": balanced_list(text, "primes_array"),
        "hecke_eigenvalues_raw": balanced_list(text, "hecke_eigenvalues_array"),
    }


def fetch_label(label: str, timeout: float) -> dict[str, Any]:
    field = label.split("-", 1)[0]
    url = f"{BASE}/{field}/holomorphic/{label}/download/sage"
    return parse_download(label, fetch_text(url, timeout))


def search_level_labels(field: str, level_norm: int, timeout: float) -> list[str]:
    query = urllib.parse.urlencode({
        "field_label": field,
        "level_norm": str(level_norm),
        "count": "500",
    })
    text = fetch_text(f"{BASE}/?{query}", timeout)
    pattern = re.compile(
        rf"{re.escape(field)}-{level_norm}\.\d+-[a-z]+"
    )
    return sorted(set(pattern.findall(text)))


def labels_from_args(args: argparse.Namespace) -> list[str]:
    labels = list(args.label)
    if args.prefix:
        labels.extend(f"{args.prefix}-{orbit_suffix(i)}" for i in range(args.max_orbits))
    if not labels:
        raise SystemExit("provide --label or --prefix")
    return labels


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--label", action="append", default=[], help="full LMFDB HMF label; repeatable")
    parser.add_argument("--prefix", help="label prefix without orbit suffix, e.g. 2.2.5.1-10125.1")
    parser.add_argument("--search-level", type=int, help="discover labels by level norm before downloading")
    parser.add_argument("--field", default="2.2.5.1", help="base-field label for --search-level")
    parser.add_argument("--max-orbits", type=int, default=50, help="number of suffixes to probe with --prefix")
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--delay", type=float, default=0.25, help="polite delay between requests")
    parser.add_argument("-o", "--output", type=Path, default=Path("lmfdb_hmf.json"))
    args = parser.parse_args()

    discovered: list[str] = []
    if args.search_level is not None:
        discovered = search_level_labels(args.field, args.search_level, args.timeout)
        args.label.extend(discovered)
        print(f"discovered {len(discovered)} labels at level norm {args.search_level}", file=sys.stderr)

    records: list[dict[str, Any]] = []
    misses: list[str] = []
    errors: list[dict[str, str]] = []
    for label in labels_from_args(args):
        try:
            records.append(fetch_label(label, args.timeout))
            print(f"ok {label}", file=sys.stderr)
        except (urllib.error.HTTPError, LookupError) as exc:
            misses.append(label)
            print(f"missing {label}: {exc}", file=sys.stderr)
        except Exception as exc:  # retain diagnostics in output
            errors.append({"label": label, "error": str(exc)})
            print(f"error {label}: {exc}", file=sys.stderr)
        time.sleep(args.delay)

    payload = {
        "discovered_labels": discovered,
        "records": records,
        "missing_labels": misses,
        "errors": errors,
        "record_count": len(records),
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {args.output} with {len(records)} records", file=sys.stderr)
    return 0 if records and not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())