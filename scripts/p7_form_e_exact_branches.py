#!/usr/bin/env python3
"""Exact mod-7 branch compatibility for level-2025 form e without SymPy.

For form e the Hecke field is Q, so resultants against x-a reduce to
polynomial evaluation at the integer Hecke eigenvalue.
"""

from __future__ import annotations

import math
import re
from pathlib import Path

P = 7
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "upstream/GFE-5p3/Outputs/Data.txt"
EFILE = ROOT / "data/lmfdb/level_2025/2.2.5.1-2025.1-e.sage"


def split_top(s: str, sep: str = ",") -> list[str]:
    out: list[str] = []
    start = 0
    depth = 0
    for i, ch in enumerate(s):
        if ch in "[<((":
            depth += 1
        elif ch in "]>))":
            depth -= 1
        elif ch == sep and depth == 0:
            out.append(s[start:i].strip())
            start = i + 1
    out.append(s[start:].strip())
    return out


def parse_data() -> dict[int, tuple[list[str], list[str], list[str]]]:
    text = DATA.read_text(errors="ignore")
    body = text[text.index("[") + 1 : text.rindex("]")]
    ans: dict[int, tuple[list[str], list[str], list[str]]] = {}
    for entry in split_top(body):
        e = entry.strip()
        if not (e.startswith("<") and e.endswith(">")):
            continue
        parts = split_top(e[1:-1])
        ell = int(parts[0])
        sets: list[list[str]] = []
        for raw in parts[1:4]:
            raw = raw.strip()
            inner = raw[1:-1].strip()
            sets.append(split_top(inner) if inner else [])
        ans[ell] = (sets[0], sets[1], sets[2])
    return ans


def parse_eigenvalues() -> dict[int, int]:
    text = EFILE.read_text(errors="ignore")
    pm = re.search(r"primes_array\s*=\s*\[(.*?)\]\nprimes\s*=", text, re.S)
    vm = re.search(r"hecke_eigenvalues_array\s*=\s*\[(.*?)\]\nhecke_eigenvalues", text, re.S)
    if not pm or not vm:
        raise RuntimeError("LMFDB arrays not found")
    primes = [(int(a), int(b)) for a, b in re.findall(r"\[\s*(\d+)\s*,\s*(\d+)\s*,", pm.group(1))]
    vals = [int(v.strip()) for v in vm.group(1).replace("\\\n", "").split(",") if v.strip()]
    out: dict[int, int] = {}
    for (_, ell), value in zip(primes, vals):
        out.setdefault(ell, value)
    return out


def eval_poly(expr: str, x: int) -> int:
    safe = expr.replace("^", "**")
    return int(eval(safe, {"__builtins__": {}}, {"x": x}))


def inertia_degree_quadratic(ell: int, d: int = 5) -> int:
    # For F=Q(sqrt5), split iff 5 is a square mod ell.
    return 1 if pow(d % ell, (ell - 1) // 2, ell) == 1 else 2


def order_mod(a: int, n: int) -> int:
    a %= n
    if math.gcd(a, n) != 1:
        raise ValueError((a, n))
    y = 1
    for k in range(1, 100):
        y = y * a % n
        if y == 1:
            return k
    raise RuntimeError


def compatible(polys: list[str], value: int) -> list[str]:
    return [q for q in polys if eval_poly(q, value) % P == 0]


def main() -> None:
    local = parse_data()
    eig = parse_eigenvalues()
    print("ell a generic_hits t0_hits tinf_hits multiplicative_hits")
    survivors = {"generic": [], "t0": [], "tinf": [], "mult": []}
    for ell, (c1, c0, coo) in local.items():
        if ell not in eig or ell in {3, 5, 7}:
            continue
        a = eig[ell]
        f2 = inertia_degree_quadratic(ell)
        f1 = order_mod(ell, 15)
        if f1 % f2:
            raise ArithmeticError((ell, f1, f2))
        ratio = f1 // f2
        ae = a if ratio == 1 else a * a - 2 * (ell ** f2)
        g = compatible(c1, a)
        z = compatible(c0, ae)
        oo = compatible(coo, ae)
        mult = [sign for sign, target in (("+", ell + 1), ("-", -ell - 1)) if (a - target) % P == 0]
        print(ell, a, len(g), len(z), len(oo), mult)
        if g:
            survivors["generic"].append(ell)
        if z:
            survivors["t0"].append(ell)
        if oo:
            survivors["tinf"].append(ell)
        if mult:
            survivors["mult"].append(ell)
    print("SURVIVING_PRIMES", survivors)
    for branch, primes in survivors.items():
        print(branch, "globally_possible" if all(primes) and len(primes) == len([l for l in local if l not in {3,5,7} and l in eig]) else "has_obstruction")


if __name__ == "__main__":
    main()