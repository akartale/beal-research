#!/usr/bin/env python3
"""Exact discriminant/maximality certificate for the implemented icosian order.

The computation uses rational arithmetic only.  It verifies that the displayed
four-element O_F-basis is closed under multiplication and that the determinant
of the reduced-trace Gram matrix is a unit of O_F.  Consequently the order is
maximal at every finite prime and B=(-1,-1)_F has no finite ramification.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations

from icosian_mod_n import HamiltonQuaternion, icosian_order_basis


@dataclass(frozen=True)
class F:
    """Element x+y*a of Q(sqrt(5)), with a^2=a+1."""

    x: Fraction
    y: Fraction = Fraction(0)

    def __add__(self, other: object) -> "F":
        z = coerce(other)
        return F(self.x + z.x, self.y + z.y)

    __radd__ = __add__

    def __neg__(self) -> "F":
        return F(-self.x, -self.y)

    def __sub__(self, other: object) -> "F":
        return self + (-coerce(other))

    def __rsub__(self, other: object) -> "F":
        return coerce(other) - self

    def __mul__(self, other: object) -> "F":
        z = coerce(other)
        return F(self.x*z.x + self.y*z.y, self.x*z.y + self.y*z.x + self.y*z.y)

    __rmul__ = __mul__

    def conjugate(self) -> "F":
        return F(self.x + self.y, -self.y)

    def norm(self) -> Fraction:
        return (self * self.conjugate()).x

    def inverse(self) -> "F":
        n = self.norm()
        if n == 0:
            raise ZeroDivisionError
        c = self.conjugate()
        return F(c.x/n, c.y/n)

    def __truediv__(self, other: object) -> "F":
        return self * coerce(other).inverse()

    def integral(self) -> bool:
        return self.x.denominator == 1 and self.y.denominator == 1

    def unit(self) -> bool:
        return self.integral() and abs(self.norm()) == 1

    def __str__(self) -> str:
        return f"({self.x})+({self.y})*a"


def coerce(value: object) -> F:
    if isinstance(value, F):
        return value
    if isinstance(value, int):
        return F(Fraction(value))
    if isinstance(value, Fraction):
        return F(value)
    raise TypeError(value)


def fq(q) -> F:
    return F(Fraction(q.num.x, q.den), Fraction(q.num.y, q.den))


def det(matrix: list[list[F]]) -> F:
    n = len(matrix)
    total = F(Fraction(0))
    for p in permutations(range(n)):
        inv = sum(p[i] > p[j] for i in range(n) for j in range(i+1, n))
        term = F(Fraction(-1 if inv % 2 else 1))
        for i in range(n):
            term *= matrix[i][p[i]]
        total += term
    return total


def solve(matrix: list[list[F]], rhs: list[F]) -> list[F]:
    n = len(rhs)
    aug = [row[:] + [rhs[i]] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next(r for r in range(col, n) if aug[r][col] != F(Fraction(0)))
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x / scale for x in aug[col]]
        for r in range(n):
            if r == col:
                continue
            factor = aug[r][col]
            if factor != F(Fraction(0)):
                aug[r] = [aug[r][c] - factor*aug[col][c] for c in range(n+1)]
    return [aug[i][n] for i in range(n)]


def main() -> None:
    basis = icosian_order_basis()
    coeff = [[fq(basis[j].coefficients[i]) for j in range(4)] for i in range(4)]
    print("basis_coefficient_det", det(coeff))

    gram: list[list[F]] = []
    for bi in basis:
        row = []
        for bj in basis:
            row.append(fq((bi * bj).reduced_trace()))
        gram.append(row)

    print("trace_gram")
    for row in gram:
        print(" ".join(str(x) for x in row))
    disc = det(gram)
    print("trace_discriminant", disc)
    print("trace_discriminant_norm", disc.norm())
    print("trace_discriminant_is_unit", disc.unit())

    multiplication_integral = True
    print("multiplication_table_coordinates")
    for i, bi in enumerate(basis):
        for j, bj in enumerate(basis):
            rhs = [fq(c) for c in (bi*bj).coefficients]
            coords = solve(coeff, rhs)
            ok = all(c.integral() for c in coords)
            multiplication_integral &= ok
            print(i, j, " ".join(str(c) for c in coords), "integral", ok)
    print("multiplication_closed", multiplication_integral)

    if not multiplication_integral:
        raise SystemExit("basis is not closed under multiplication")
    if not disc.unit():
        raise SystemExit("trace discriminant is not a unit")
    print("finite_ramification_empty=true")
    print("order_maximal_at_all_finite_primes=true")


if __name__ == "__main__":
    main()