#!/usr/bin/env python3
"""Cartier-Manin/Hasse-Witt matrices for the normalized p=7 special disks.

For a genus-2 hyperelliptic curve y^2=f(x) in odd characteristic p, write

    f(x)^((p-1)/2) = sum c_n x^n.

With the basis dx/y, x dx/y, one standard Cartier-Manin convention is

    M = [[c_{p-1}, c_{p-2}], [c_{2p-1}, c_{2p-2}]].

The transpose convention has the same ranks and stable nilpotence properties.
This script computes the matrix symbolically modulo 7 for the normalized
reductions in the t=0 and t=infinity disks.
"""

from __future__ import annotations

from dataclasses import dataclass

P = 7


@dataclass(frozen=True)
class Poly:
    # sparse polynomial in x whose coefficients are polynomials in one unit
    # parameter, represented as dict x_degree -> dict parameter_degree -> coeff
    terms: dict[int, dict[int, int]]


def coeff_add(a: dict[int, int], b: dict[int, int]) -> dict[int, int]:
    out = dict(a)
    for degree, value in b.items():
        out[degree] = (out.get(degree, 0) + value) % P
    return {degree: value for degree, value in out.items() if value % P}


def coeff_mul(a: dict[int, int], b: dict[int, int]) -> dict[int, int]:
    out: dict[int, int] = {}
    for da, va in a.items():
        for db, vb in b.items():
            degree = da + db
            out[degree] = (out.get(degree, 0) + va * vb) % P
    return {degree: value for degree, value in out.items() if value % P}


def poly_mul(a: Poly, b: Poly) -> Poly:
    out: dict[int, dict[int, int]] = {}
    for xa, ca in a.terms.items():
        for xb, cb in b.terms.items():
            degree = xa + xb
            out[degree] = coeff_add(out.get(degree, {}), coeff_mul(ca, cb))
    return Poly({degree: coeff for degree, coeff in out.items() if coeff})


def poly_pow(poly: Poly, exponent: int) -> Poly:
    out = Poly({0: {0: 1}})
    base = poly
    while exponent:
        if exponent & 1:
            out = poly_mul(out, base)
        base = poly_mul(base, base)
        exponent >>= 1
    return out


def format_coeff(coeff: dict[int, int], variable: str) -> str:
    if not coeff:
        return "0"
    pieces: list[str] = []
    for degree in sorted(coeff):
        value = coeff[degree] % P
        monomial = "" if degree == 0 else variable if degree == 1 else f"{variable}^{degree}"
        if degree == 0:
            pieces.append(str(value))
        elif value == 1:
            pieces.append(monomial)
        else:
            pieces.append(f"{value}*{monomial}")
    return " + ".join(pieces)


def matrix_for(poly: Poly) -> list[list[dict[int, int]]]:
    power = poly_pow(poly, (P - 1) // 2)
    c = lambda n: power.terms.get(n, {})
    return [[c(P - 1), c(P - 2)], [c(2 * P - 1), c(2 * P - 2)]]


def determinant_mod7(matrix: list[list[int]]) -> int:
    return (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % P


def rank_mod7(matrix: list[list[int]]) -> int:
    if determinant_mod7(matrix):
        return 2
    if any(entry % P for row in matrix for entry in row):
        return 1
    return 0


def evaluate(coeff: dict[int, int], unit: int) -> int:
    return sum(value * pow(unit, degree, P) for degree, value in coeff.items()) % P


def multiply_matrix(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [
        [sum(a[i][k] * b[k][j] for k in range(2)) % P for j in range(2)]
        for i in range(2)
    ]


def report(name: str, variable: str, poly: Poly) -> None:
    symbolic = matrix_for(poly)
    print(name)
    print("M = [[%s, %s], [%s, %s]]" % tuple(
        format_coeff(symbolic[i][j], variable) for i in range(2) for j in range(2)
    ))
    print("unit rank(M) rank(M^2) a_number p_rank")
    for unit in range(1, P):
        matrix = [[evaluate(symbolic[i][j], unit) for j in range(2)] for i in range(2)]
        square = multiply_matrix(matrix, matrix)
        rank = rank_mod7(matrix)
        stable_rank = rank_mod7(square)
        print(unit, rank, stable_rank, 2 - rank, stable_rank)


def main() -> None:
    # t=0 reduction: -108*x^5 + 9*u^2 = 4*x^5 + 2*u^2 mod 7.
    t0 = Poly({5: {0: -108}, 0: {2: 9}})

    # t=infinity reduction: 45*v^2*x^6 + 90*v*x^3 + 9.
    infinity = Poly({6: {2: 45}, 3: {1: 90}, 0: {0: 9}})

    report("t=0", "u", t0)
    report("t=infinity", "v", infinity)


if __name__ == "__main__":
    main()