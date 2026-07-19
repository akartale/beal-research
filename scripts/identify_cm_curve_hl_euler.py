#!/usr/bin/env python3
"""Compare Euler factors of Jac(y^2=x^5-1) with HMF orbit h/l.

For a split rational prime p of F=Q(sqrt(5)), a Hilbert coefficient a_q in
the quadratic coefficient field E gives the degree-4 Euler polynomial

  (1-a_q T+pT^2)(1-a_q' T+pT^2).

The script parses the cached LMFDB Sage file for form h, computes the curve
Euler polynomial from point counts over F_p and F_{p^2}, and checks equality.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HFILE = ROOT / "data/lmfdb/level_2025/2.2.5.1-2025.1-h.sage"


@dataclass(frozen=True)
class PrimeEntry:
    norm: int
    p: int
    generator: str


def extract_bracket_block(text: str, marker: str) -> str:
    start = text.index(marker)
    start = text.index("[", start)
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "[":
            depth += 1
        elif text[i] == "]":
            depth -= 1
            if depth == 0:
                return text[start : i + 1]
    raise ValueError(marker)


def parse_primes(text: str) -> list[PrimeEntry]:
    block = extract_bracket_block(text, "primes_array")
    out = []
    for m in re.finditer(r"\[(\d+),\s*(\d+),\s*([^\]]+)\]", block):
        out.append(PrimeEntry(int(m.group(1)), int(m.group(2)), m.group(3).strip()))
    return out


def parse_coeffs(text: str) -> list[str]:
    block = extract_bracket_block(text, "hecke_eigenvalues_array")
    return [token.strip() for token in block[1:-1].split(",")]


def parse_linear_e(token: str) -> tuple[int, int]:
    """Return m,n for m*e+n."""
    s = token.replace(" ", "")
    if s == "0":
        return 0, 0
    # Normalize implicit coefficients of e.
    s = s.replace("-e", "-1*e").replace("+e", "+1*e")
    if s.startswith("e"):
        s = "1*" + s
    m = re.fullmatch(r"([+-]?\d+)\*e([+-]\d+)?", s)
    if m:
        return int(m.group(1)), int(m.group(2) or 0)
    if re.fullmatch(r"[+-]?\d+", s):
        return 0, int(s)
    raise ValueError(token)


def trace_norm_h(m: int, n: int) -> tuple[int, int]:
    # e^2+9e+19=0, so Tr(e)=-9 and Norm(e)=19.
    tr = -9 * m + 2 * n
    norm = 19 * m * m - 9 * m * n + n * n
    return tr, norm


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def count_curve_fp(p: int) -> int:
    # Odd degree model has one point at infinity.
    return 1 + sum(1 + legendre(pow(x, 5, p) - 1, p) for x in range(p))


def fp2_mul(x: tuple[int, int], y: tuple[int, int], p: int, d: int) -> tuple[int, int]:
    a, b = x
    c, e = y
    return ((a * c + b * e * d) % p, (a * e + b * c) % p)


def fp2_pow(x: tuple[int, int], n: int, p: int, d: int) -> tuple[int, int]:
    out = (1, 0)
    while n:
        if n & 1:
            out = fp2_mul(out, x, p, d)
        x = fp2_mul(x, x, p, d)
        n >>= 1
    return out


def fp2_quadchar(x: tuple[int, int], p: int, d: int) -> int:
    if x == (0, 0):
        return 0
    return 1 if fp2_pow(x, (p * p - 1) // 2, p, d) == (1, 0) else -1


def count_curve_fp2(p: int) -> int:
    d = next(a for a in range(2, p) if legendre(a, p) == -1)
    total = 1
    for a in range(p):
        for b in range(p):
            x = (a, b)
            rhs = fp2_mul(fp2_mul(fp2_mul(fp2_mul(x, x, p, d), x, p, d), x, p, d), x, p, d)
            rhs = ((rhs[0] - 1) % p, rhs[1])
            total += 1 + fp2_quadchar(rhs, p, d)
    return total


def curve_euler(p: int) -> tuple[int, int, int, int, int]:
    n1 = count_curve_fp(p)
    n2 = count_curve_fp2(p)
    a1 = p + 1 - n1
    # N2=p^2+1-(alpha_i^2 sum), alpha_i^2 sum=a1^2-2a2.
    a2 = (n2 - p * p - 1 + a1 * a1) // 2
    return (1, -a1, a2, -p * a1, p * p)


def hmf_euler(p: int, coeff: str) -> tuple[int, int, int, int, int]:
    m, n = parse_linear_e(coeff)
    tr, norm = trace_norm_h(m, n)
    return (1, -tr, norm + 2 * p, -p * tr, p * p)


def main() -> None:
    text = HFILE.read_text(errors="replace")
    primes = parse_primes(text)
    coeffs = parse_coeffs(text)
    checked = 0
    print("p generator coeff curve_euler hmf_euler match")
    for prime, coeff in zip(primes, coeffs):
        p = prime.p
        if prime.norm != p or p in {2, 3, 5, 7}:
            continue
        curve = curve_euler(p)
        hmf = hmf_euler(p, coeff)
        print(p, prime.generator, coeff, curve, hmf, curve == hmf)
        checked += 1
        if checked >= 4:
            break


if __name__ == "__main__":
    main()