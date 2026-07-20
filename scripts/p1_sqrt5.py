#!/usr/bin/env python3
"""Projective lines over the local factors of the Beal levels.

This module depends only on :mod:`ok_sqrt5` and the Python standard library.
For a finite local ring R with maximal ideal m, it uses the disjoint charts

    P^1(R) = {[x:1] : x in R} union {[1:y] : y in m}.

For the target composite levels, CRT gives

    P^1(O/N_23) = P^1(O/(3^2)) x P^1(O/(pi5^3)),
    P^1(O/N_33) = P^1(O/(3^3)) x P^1(O/(pi5^3)).
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd
from typing import Iterator

from ok_sqrt5 import A, ONE, PI5, ZERO, OK, PrincipalQuotient, beal_level


@dataclass(frozen=True, slots=True)
class P1Point:
    """Canonical projective point; chart 0 means [x:1], chart 1 means [1:y]."""

    chart: int
    value: OK


class LocalProjectiveLine:
    """P^1 over O_K/(uniformizer^exponent)."""

    def __init__(
        self,
        ring: PrincipalQuotient,
        rational_prime: int,
        residue_size: int,
    ) -> None:
        self.ring = ring
        self.rational_prime = rational_prime
        self.residue_size = residue_size
        self.characteristic = self._compute_characteristic()
        self._elements = tuple(ring.elements())
        self._nonunits = tuple(
            z for z in self._elements if z.norm() % rational_prime == 0
        )
        self._inverse = {
            z: self._inverse_by_conjugation(z)
            for z in self._elements
            if z.norm() % rational_prime != 0
        }
        expected_nonunits = ring.order // residue_size
        if len(self._nonunits) != expected_nonunits:
            raise ArithmeticError(
                f"expected {expected_nonunits} nonunits, found {len(self._nonunits)}"
            )
        self._points = tuple(
            [P1Point(0, z) for z in self._elements]
            + [P1Point(1, z) for z in self._nonunits]
        )
        self._index = {point: i for i, point in enumerate(self._points)}

    def _compute_characteristic(self) -> int:
        for n in range(1, self.ring.order + 1):
            if self.ring.reduce(n) == ZERO:
                return n
        raise ArithmeticError("failed to determine quotient characteristic")

    def _inverse_by_conjugation(self, z: OK) -> OK:
        norm = z.norm()
        if gcd(norm, self.characteristic) != 1:
            raise ZeroDivisionError(z)
        scalar_inverse = pow(norm, -1, self.characteristic)
        candidate = self.ring.reduce(scalar_inverse * z.conjugate())
        if self.ring.mul(z, candidate) != self.ring.reduce(ONE):
            raise ArithmeticError(f"bad inverse for {z}")
        return candidate

    @property
    def order(self) -> int:
        return len(self._points)

    @property
    def expected_order(self) -> int:
        return self.ring.order + self.ring.order // self.residue_size

    @property
    def points(self) -> tuple[P1Point, ...]:
        return self._points

    @property
    def nonunits(self) -> tuple[OK, ...]:
        return self._nonunits

    def is_unit(self, z: OK) -> bool:
        return self.ring.reduce(z) in self._inverse

    def inverse(self, z: OK) -> OK:
        return self._inverse[self.ring.reduce(z)]

    def coordinates(self, point: P1Point) -> tuple[OK, OK]:
        if point.chart == 0:
            return point.value, self.ring.reduce(ONE)
        if point.chart == 1:
            return self.ring.reduce(ONE), point.value
        raise ValueError(point.chart)

    def normalize(self, c: OK, d: OK) -> P1Point:
        c = self.ring.reduce(c)
        d = self.ring.reduce(d)
        if self.is_unit(d):
            return P1Point(0, self.ring.mul(c, self.inverse(d)))
        if self.is_unit(c):
            y = self.ring.mul(d, self.inverse(c))
            if self.is_unit(y):
                raise ArithmeticError("second chart value must be a nonunit")
            return P1Point(1, y)
        raise ValueError("pair is not primitive")

    def index(self, point: P1Point) -> int:
        return self._index[point]

    def from_index(self, index: int) -> P1Point:
        return self._points[index]

    def act_row(
        self,
        point: P1Point,
        matrix: tuple[tuple[OK, OK], tuple[OK, OK]],
    ) -> P1Point:
        """Right action of a 2x2 matrix on row coordinates [c,d]."""
        c, d = self.coordinates(point)
        a11, a12 = matrix[0]
        a21, a22 = matrix[1]
        return self.normalize(
            self.ring.add(self.ring.mul(c, a11), self.ring.mul(d, a21)),
            self.ring.add(self.ring.mul(c, a12), self.ring.mul(d, a22)),
        )


@dataclass(frozen=True, slots=True)
class CRTP1Point:
    left_index: int
    right_index: int


class CRTProjectiveLine:
    def __init__(self, exponent_at_3: int) -> None:
        crt = beal_level(exponent_at_3)
        self.exponent_at_3 = exponent_at_3
        self.left = LocalProjectiveLine(crt.left, rational_prime=3, residue_size=9)
        self.right = LocalProjectiveLine(crt.right, rational_prime=5, residue_size=5)

    @property
    def order(self) -> int:
        return self.left.order * self.right.order

    def index(self, point: CRTP1Point) -> int:
        return point.left_index + self.left.order * point.right_index

    def from_index(self, index: int) -> CRTP1Point:
        if not 0 <= index < self.order:
            raise IndexError(index)
        right, left = divmod(index, self.left.order)
        return CRTP1Point(left, right)

    def points(self) -> Iterator[CRTP1Point]:
        for right in range(self.right.order):
            for left in range(self.left.order):
                yield CRTP1Point(left, right)


def self_test() -> None:
    p1_23 = CRTProjectiveLine(2)
    p1_33 = CRTProjectiveLine(3)

    assert p1_23.left.characteristic == 9
    assert p1_33.left.characteristic == 27
    assert p1_23.right.characteristic == p1_33.right.characteristic == 25

    assert p1_23.left.order == 90
    assert p1_33.left.order == 810
    assert p1_23.right.order == p1_33.right.order == 150
    assert p1_23.order == 13_500
    assert p1_33.order == 121_500

    identity = ((ONE, ZERO), (ZERO, ONE))
    swap = ((ZERO, ONE), (ONE, ZERO))
    shear = ((ONE, ONE), (ZERO, ONE))

    for line in (p1_23.left, p1_23.right, p1_33.left, p1_33.right):
        assert line.order == line.expected_order
        assert len(set(line.points)) == line.order
        for i, point in enumerate(line.points):
            assert line.index(point) == i
            c, d = line.coordinates(point)
            assert line.normalize(c, d) == point
            assert line.act_row(point, identity) == point
            assert line.act_row(line.act_row(point, swap), swap) == point
            # The shear has determinant one, so it must preserve primitivity.
            assert line.act_row(point, shear) in line.points

        # Exhaustively verify that every primitive pair normalizes to one of the
        # chart representatives.  The largest local ring has 729^2 pairs.
        for c in line.ring.elements():
            for d in line.ring.elements():
                primitive = line.is_unit(c) or line.is_unit(d)
                if primitive:
                    assert line.normalize(c, d) in line.points
                else:
                    try:
                        line.normalize(c, d)
                    except ValueError:
                        pass
                    else:
                        raise AssertionError("nonprimitive pair was accepted")

    for space in (p1_23, p1_33):
        seen = set()
        for point in space.points():
            idx = space.index(point)
            assert space.from_index(idx) == point
            seen.add(idx)
        assert len(seen) == space.order

    print("local P1 sizes: 90, 810, 150")
    print(f"P1(N_23) size: {p1_23.order}")
    print(f"P1(N_33) size: {p1_33.order}")
    print("normalization and matrix-action tests: OK")


if __name__ == "__main__":
    self_test()