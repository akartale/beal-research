#!/usr/bin/env python3
"""Identify candidate quadratic CM characters from Hecke-zero patterns.

The base field is F=Q(w), w^2-w-1=0.  For split rational primes the cached
LMFDB prime entry gives an element a*w+b generating the corresponding prime,
so w=-b/a mod p.  For a candidate d=A+B*w, its quadratic character at that
prime is the Legendre symbol of A+B*w_mod_p.

For a CM Hilbert form, away from the conductor, a_q=0 exactly at primes inert
in the CM quadratic extension.  We search small d=A+B*w up to multiplication
by obvious squares and rank candidates by agreement with the cached zero
pattern.  This is a diagnostic, not yet a proof of the conductor.
"""

from __future__ import annotations

import ast
import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "e": ROOT / "data/lmfdb/level_2025/2.2.5.1-2025.1-e.sage",
    "h": ROOT / "data/lmfdb/level_2025/2.2.5.1-2025.1-h.sage",
    "l": ROOT / "data/lmfdb/level_2025/2.2.5.1-2025.1-l.sage",
}


@dataclass(frozen=True)
class Observation:
    p: int
    a: int
    b: int
    zero: bool


def extract_block(text: str, name: str, closing: str = "]") -> str:
    start = text.index(name)
    start = text.index("[", start)
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "[":
            depth += 1
        elif text[i] == "]":
            depth -= 1
            if depth == 0:
                return text[start : i + 1]
    raise ValueError(f"unterminated block {name}")


def parse_primes(text: str) -> list[tuple[int, int, str]]:
    block = extract_block(text, "primes_array")
    rows: list[tuple[int, int, str]] = []
    for match in re.finditer(r"\[(\d+),\s*(\d+),\s*([^\]]+)\]", block):
        rows.append((int(match.group(1)), int(match.group(2)), match.group(3).strip()))
    return rows


def parse_coeff_tokens(text: str) -> list[str]:
    block = extract_block(text, "hecke_eigenvalues_array")
    return [token.strip() for token in block[1:-1].split(",")]


def observations(path: Path, limit: int = 250) -> list[Observation]:
    text = path.read_text(errors="replace")
    primes = parse_primes(text)
    coeffs = parse_coeff_tokens(text)
    out: list[Observation] = []
    for (norm, p, generator), coeff in zip(primes, coeffs):
        if len(out) >= limit:
            break
        if p in {3, 5, 7} or norm != p:
            continue
        compact = generator.replace(" ", "")
        match = re.fullmatch(r"([+-]?\d+)\*w([+-]\d+)", compact)
        if not match:
            continue
        a = int(match.group(1))
        b = int(match.group(2))
        out.append(Observation(p=p, a=a, b=b, zero=coeff == "0"))
    return out


def legendre(value: int, p: int) -> int:
    value %= p
    if value == 0:
        return 0
    return 1 if pow(value, (p - 1) // 2, p) == 1 else -1


def score(obs: list[Observation], A: int, B: int) -> tuple[int, int, int]:
    agree = disagree = ramified = 0
    for row in obs:
        w = (-row.b * pow(row.a, -1, row.p)) % row.p
        chi = legendre(A + B * w, row.p)
        if chi == 0:
            ramified += 1
        elif row.zero == (chi == -1):
            agree += 1
        else:
            disagree += 1
    return agree, disagree, ramified


def norm_from_F(A: int, B: int) -> int:
    """Norm of A+B*w for w^2-w-1=0."""
    return A * A + A * B - B * B


def local_at_7(A: int, B: int) -> str:
    """7 is inert in F/Q, so test squareness in F_49 by the F_49/F_7 norm."""
    norm = norm_from_F(A, B) % 7
    if norm == 0:
        return "ramified"
    return "split" if legendre(norm, 7) == 1 else "inert"


def main() -> None:
    canonical = {"e": (-3, 0), "h": (-3, 1), "l": (-3, 1)}
    for label, path in FILES.items():
        obs = observations(path)
        candidates = []
        for A in range(-30, 31):
            for B in range(-30, 31):
                if A == B == 0:
                    continue
                agree, disagree, ramified = score(obs, A, B)
                candidates.append((disagree, ramified, -agree, A, B))
        candidates.sort()
        print(label, "observations", len(obs), "zero", sum(row.zero for row in obs))
        A0, B0 = canonical[label]
        print("canonical", A0, "+", B0, "*w", "norm=", norm_from_F(A0, B0), "at_7=", local_at_7(A0, B0))
        for disagree, ramified, neg_agree, A, B in candidates[:20]:
            print("d=", A, "+", B, "*w", "agree=", -neg_agree, "disagree=", disagree, "ramified=", ramified)


if __name__ == "__main__":
    main()