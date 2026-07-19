#!/usr/bin/env python3
"""Normalized mod-7 reductions in the two special disks.

For t=7^(5b)u (7|B), x=7^(2b)X and y=7^(5b)Y give
  Y^2 = 45*7^(2b)X^6 -108X^5 +90*7^b*u*X^3 +9u^2,
so for b>=1 the reduction is Y^2=-108X^5+9u^2.

For s=1/t=7^(3a)v (7|A), Y=y/t and x=7^(-a)X give
  Y^2 = 45v^2X^6 -108*7^a*v^2X^5 +90vX^3 +9,
so for a>=1 the reduction is Y^2=45v^2X^6+90vX^3+9.

This script counts F_7-points of these smooth genus-2 reductions for every
unit residue u,v.  It reports the rational trace q+1-#C(F_q).
"""

from __future__ import annotations

P = 7
D = 3  # nonsquare in F_7; F_49 = F_7[w]/(w^2-D)


def legendre(a: int) -> int:
    a %= P
    if a == 0:
        return 0
    return 1 if pow(a, (P - 1) // 2, P) == 1 else -1


def f49_add(z: tuple[int, int], w: tuple[int, int]) -> tuple[int, int]:
    return ((z[0] + w[0]) % P, (z[1] + w[1]) % P)


def f49_mul(z: tuple[int, int], w: tuple[int, int]) -> tuple[int, int]:
    return ((z[0] * w[0] + D * z[1] * w[1]) % P, (z[0] * w[1] + z[1] * w[0]) % P)


def f49_pow(z: tuple[int, int], n: int) -> tuple[int, int]:
    out = (1, 0)
    while n:
        if n & 1:
            out = f49_mul(out, z)
        z = f49_mul(z, z)
        n >>= 1
    return out


def f49_character(z: tuple[int, int]) -> int:
    if z == (0, 0):
        return 0
    return 1 if f49_pow(z, 24) == (1, 0) else -1


def count_curve(coeffs: list[int]) -> int:
    """Count smooth projective y^2=f(x) over F_7, coeffs low to high."""
    degree = max(i for i, c in enumerate(coeffs) if c % P)
    affine = 0
    for x in range(P):
        fx = sum(c * pow(x, i, P) for i, c in enumerate(coeffs)) % P
        affine += 1 + legendre(fx)
    if degree % 2:
        infinity = 1
    else:
        infinity = 2 if legendre(coeffs[degree]) == 1 else 0
    return affine + infinity


def count_curve_f49(coeffs: list[int]) -> int:
    degree = max(i for i, c in enumerate(coeffs) if c % P)
    affine = 0
    for a in range(P):
        for b in range(P):
            x = (a, b)
            fx = (0, 0)
            xp = (1, 0)
            for c in coeffs:
                fx = f49_add(fx, f49_mul((c % P, 0), xp))
                xp = f49_mul(xp, x)
            affine += 1 + f49_character(fx)
    if degree % 2:
        infinity = 1
    else:
        infinity = 2 if f49_character((coeffs[degree] % P, 0)) == 1 else 0
    return affine + infinity


def derivative(coeffs: list[int]) -> list[int]:
    return [(i * coeffs[i]) % P for i in range(1, len(coeffs))]


def eval_poly(coeffs: list[int], x: int) -> int:
    return sum(c * pow(x, i, P) for i, c in enumerate(coeffs)) % P


def is_squarefree(coeffs: list[int]) -> bool:
    deriv = derivative(coeffs)
    return all(not (eval_poly(coeffs, x) == 0 and eval_poly(deriv, x) == 0) for x in range(P))


def main() -> None:
    print("branch unit squarefree N1 a1 N2 a2")
    for u in range(1, P):
        # -108 X^5 + 9u^2
        coeffs = [9 * u * u, 0, 0, 0, 0, -108]
        n1 = count_curve(coeffs)
        a1 = P + 1 - n1
        n2 = count_curve_f49(coeffs)
        a2 = (n2 - P * P - 1 + a1 * a1) // 2
        print("t=0", u, is_squarefree(coeffs), n1, a1, n2, a2)

    for v in range(1, P):
        # 45v^2 X^6 + 90v X^3 + 9
        coeffs = [9, 0, 0, 90 * v, 0, 0, 45 * v * v]
        n1 = count_curve(coeffs)
        a1 = P + 1 - n1
        n2 = count_curve_f49(coeffs)
        a2 = (n2 - P * P - 1 + a1 * a1) // 2
        print("t=infinity", v, is_squarefree(coeffs), n1, a1, n2, a2)


if __name__ == "__main__":
    main()