#!/usr/bin/env python3
"""Exact lightweight arithmetic in O_Q(sqrt(5)) and its finite quotients.

No Sage, Magma, PARI bindings, NumPy, or SymPy are required.

We use O_K = Z[a], a^2 = a + 1.  Elements are integer pairs (x,y)
representing x + y*a.  Every modulus used by the Beal (3,5,7) computation is
principal:

    N_(a,b) = (3^a * pi^b),  pi = 2*a - 1,  pi^2 = 5.

A principal ideal (g) is represented by the column lattice of multiplication
by g in the basis (1,a).  A two-dimensional column-HNF gives canonical
representatives and a compact integer index.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd
from random import Random
from typing import Iterable, Iterator


@dataclass(frozen=True, slots=True)
class OK:
    """An algebraic integer x + y*a, where a^2 = a + 1."""

    x: int
    y: int = 0

    def __add__(self, other: object) -> "OK":
        z = coerce(other)
        return OK(self.x + z.x, self.y + z.y)

    def __radd__(self, other: object) -> "OK":
        return self + other

    def __neg__(self) -> "OK":
        return OK(-self.x, -self.y)

    def __sub__(self, other: object) -> "OK":
        return self + (-coerce(other))

    def __rsub__(self, other: object) -> "OK":
        return coerce(other) - self

    def __mul__(self, other: object) -> "OK":
        z = coerce(other)
        # (x+y*a)(u+v*a) = xu+yv + (xv+yu+yv)*a.
        return OK(
            self.x * z.x + self.y * z.y,
            self.x * z.y + self.y * z.x + self.y * z.y,
        )

    def __rmul__(self, other: object) -> "OK":
        return self * other

    def __pow__(self, exponent: int) -> "OK":
        if exponent < 0:
            raise ValueError("negative powers are not integral in general")
        result = ONE
        base = self
        n = exponent
        while n:
            if n & 1:
                result *= base
            base *= base
            n >>= 1
        return result

    def conjugate(self) -> "OK":
        # a' = 1-a.
        return OK(self.x + self.y, -self.y)

    def norm(self) -> int:
        return self.x * self.x + self.x * self.y - self.y * self.y

    def multiplication_matrix(self) -> tuple[tuple[int, int], tuple[int, int]]:
        """Columns are the coordinates of self*1 and self*a."""
        return ((self.x, self.y), (self.y, self.x + self.y))


def coerce(value: object) -> OK:
    if isinstance(value, OK):
        return value
    if isinstance(value, int):
        return OK(value)
    return NotImplemented  # type: ignore[return-value]


ZERO = OK(0)
ONE = OK(1)
A = OK(0, 1)
PI5 = 2 * A - 1


def xgcd(a: int, b: int) -> tuple[int, int, int]:
    """Return positive gcd g and coefficients u,v with u*a+v*b=g."""
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    if old_r < 0:
        return -old_r, -old_s, -old_t
    return old_r, old_s, old_t


@dataclass(frozen=True, slots=True)
class ColumnHNF2:
    """Column lattice basis ((h11, t), (0, h22)).

    In matrix notation the basis columns are

        [h11   0]
        [ t   h22]

    with h11,h22 > 0 and 0 <= t < h22.
    """

    h11: int
    t: int
    h22: int

    @property
    def determinant(self) -> int:
        return self.h11 * self.h22

    def reduce(self, z: OK) -> OK:
        q, rx = divmod(z.x, self.h11)
        y_after_first = z.y - q * self.t
        _, ry = divmod(y_after_first, self.h22)
        return OK(rx, ry)

    def contains(self, z: OK) -> bool:
        return self.reduce(z) == ZERO


def column_hnf_2x2(
    c1: tuple[int, int], c2: tuple[int, int]
) -> ColumnHNF2:
    """Compute a canonical column-HNF for a full-rank 2x2 lattice."""
    a, c = c1
    b, d = c2
    det = a * d - b * c
    if det == 0:
        raise ValueError("lattice matrix must have full rank")

    g, u, v = xgcd(a, b)
    # First new column has top coordinate g.
    lower_first = u * c + v * d
    # Second new column has top coordinate zero and lower coordinate det/g.
    lower_second = det // g
    if lower_second < 0:
        lower_second = -lower_second
    lower_first %= lower_second
    return ColumnHNF2(g, lower_first, lower_second)


@dataclass(frozen=True, slots=True)
class PrincipalQuotient:
    """The finite ring O_K/(generator), represented by canonical pairs."""

    generator: OK
    hnf: ColumnHNF2

    @classmethod
    def from_generator(cls, generator: OK) -> "PrincipalQuotient":
        matrix = generator.multiplication_matrix()
        hnf = column_hnf_2x2(matrix[0], matrix[1])
        expected = abs(generator.norm())
        if hnf.determinant != expected:
            raise ArithmeticError(
                f"HNF determinant {hnf.determinant} != |Norm(g)| {expected}"
            )
        return cls(generator, hnf)

    @property
    def order(self) -> int:
        return self.hnf.determinant

    def reduce(self, z: OK | int) -> OK:
        return self.hnf.reduce(coerce(z))

    def add(self, left: OK, right: OK) -> OK:
        return self.reduce(left + right)

    def mul(self, left: OK, right: OK) -> OK:
        return self.reduce(left * right)

    def elements(self) -> Iterator[OK]:
        for y in range(self.hnf.h22):
            for x in range(self.hnf.h11):
                yield OK(x, y)

    def index(self, z: OK) -> int:
        r = self.reduce(z)
        return r.x + self.hnf.h11 * r.y

    def from_index(self, index: int) -> OK:
        if not 0 <= index < self.order:
            raise IndexError(index)
        y, x = divmod(index, self.hnf.h11)
        return OK(x, y)

    def inverse(self, z: OK) -> OK:
        target = self.reduce(z)
        if target == ZERO:
            raise ZeroDivisionError("zero is not invertible")
        # The relevant local factors have at most 729 elements.  A linear scan
        # is deterministic and sufficient for setup/validation; hot-loop unit
        # inversion will later use precomputed tables.
        for candidate in self.elements():
            if self.mul(target, candidate) == self.reduce(ONE):
                return candidate
        raise ZeroDivisionError(f"nonunit modulo {self.generator}: {target}")

    def is_unit(self, z: OK) -> bool:
        try:
            self.inverse(z)
        except ZeroDivisionError:
            return False
        return True


@dataclass(frozen=True, slots=True)
class CRTQuotient:
    """CRT model O_K/(m1*m2), with coprime principal moduli."""

    left: PrincipalQuotient
    right: PrincipalQuotient
    product: PrincipalQuotient
    left_generator_inverse_right: OK

    @classmethod
    def build(cls, left_generator: OK, right_generator: OK) -> "CRTQuotient":
        left = PrincipalQuotient.from_generator(left_generator)
        right = PrincipalQuotient.from_generator(right_generator)
        product = PrincipalQuotient.from_generator(left_generator * right_generator)
        inv = right.inverse(right.reduce(left_generator))
        model = cls(left, right, product, inv)
        if product.order != left.order * right.order:
            raise ArithmeticError("CRT factors are not coprime")
        return model

    @property
    def order(self) -> int:
        return self.product.order

    def split(self, z: OK) -> tuple[OK, OK]:
        return self.left.reduce(z), self.right.reduce(z)

    def combine(self, left_residue: OK, right_residue: OK) -> OK:
        l = self.left.reduce(left_residue)
        r = self.right.reduce(right_residue)
        correction = self.right.mul(
            self.right.reduce(r - l), self.left_generator_inverse_right
        )
        return self.product.reduce(l + self.left.generator * correction)


def beal_level(a3: int, b5: int = 3) -> CRTQuotient:
    if a3 < 1 or b5 < 1:
        raise ValueError("exponents must be positive")
    return CRTQuotient.build(OK(3**a3), PI5**b5)


def _assert_ring_axioms(ring: PrincipalQuotient, samples: Iterable[OK]) -> None:
    values = list(samples)
    zero = ring.reduce(ZERO)
    one = ring.reduce(ONE)
    for x in values:
        xr = ring.reduce(x)
        assert ring.add(xr, zero) == xr
        assert ring.mul(xr, one) == xr
        for y in values:
            yr = ring.reduce(y)
            assert ring.add(xr, yr) == ring.add(yr, xr)
            assert ring.mul(xr, yr) == ring.mul(yr, xr)
            for z in values[:8]:
                zr = ring.reduce(z)
                assert ring.mul(xr, ring.add(yr, zr)) == ring.add(
                    ring.mul(xr, yr), ring.mul(xr, zr)
                )


def self_test() -> None:
    assert A * A == A + 1
    assert PI5 == OK(-1, 2)
    assert PI5 * PI5 == OK(5)
    assert PI5.norm() == -5

    p5_cubed = PrincipalQuotient.from_generator(PI5**3)
    assert p5_cubed.order == 125
    assert p5_cubed.hnf == ColumnHNF2(5, 15, 25)

    n23 = beal_level(2)
    n33 = beal_level(3)
    assert n23.left.order == 81
    assert n33.left.order == 729
    assert n23.right.order == n33.right.order == 125
    assert n23.order == 10125
    assert n33.order == 91125

    rng = Random(357)
    samples = [OK(rng.randrange(-100, 101), rng.randrange(-100, 101)) for _ in range(20)]
    _assert_ring_axioms(n23.product, samples[:12])
    _assert_ring_axioms(n33.product, samples[:12])

    for model in (n23, n33):
        for z in samples:
            split = model.split(z)
            rebuilt = model.combine(*split)
            assert model.product.reduce(rebuilt) == model.product.reduce(z)
            assert model.split(rebuilt) == split
        # Exhaustive CRT bijection.  This is only 10,125 + 91,125 pairs.
        seen: set[int] = set()
        for left in model.left.elements():
            for right in model.right.elements():
                combined = model.combine(left, right)
                idx = model.product.index(combined)
                assert idx not in seen
                seen.add(idx)
        assert len(seen) == model.order

    print("O_K arithmetic: OK")
    print(f"pi5^3 HNF: {p5_cubed.hnf}")
    print(f"N_23 quotient order: {n23.order}")
    print(f"N_33 quotient order: {n33.order}")
    print("CRT exhaustive bijections: OK")


if __name__ == "__main__":
    self_test()