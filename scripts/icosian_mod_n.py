#!/usr/bin/env python3
"""Hamilton quaternions and the icosian order modulo the Beal levels.

This is a dependency-free port of the algebraic core used by psage's
Q(sqrt(5)) Hilbert modular-form implementation.  It provides:

* exact Hamilton quaternion arithmetic over Q(sqrt(5));
* the five norm-one icosian group generators;
* the four O_K-basis generators of the icosian maximal order;
* explicit local splittings into M_2(O_K/(3^a)) and M_2(O_K/(pi5^3)).

The splitting uses I=[[0,-1],[1,0]] and J=[[0,s],[s,0]], where s^2=-1
in the local quotient.  Hence I^2=J^2=-1 and IJ=-JI.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd
from random import Random
from typing import Iterable

from ok_sqrt5 import A, ONE, PI5, ZERO, OK, PrincipalQuotient, beal_level


@dataclass(frozen=True, slots=True)
class QOK:
    """A fraction in Q(sqrt(5)) represented by an O_K numerator."""

    num: OK
    den: int = 1

    def __post_init__(self) -> None:
        if self.den == 0:
            raise ZeroDivisionError
        num = self.num
        den = self.den
        if den < 0:
            num = -num
            den = -den
        g = gcd(gcd(abs(num.x), abs(num.y)), den)
        if g > 1:
            num = OK(num.x // g, num.y // g)
            den //= g
        object.__setattr__(self, "num", num)
        object.__setattr__(self, "den", den)

    def __add__(self, other: object) -> "QOK":
        z = qcoerce(other)
        return QOK(self.num * z.den + z.num * self.den, self.den * z.den)

    def __radd__(self, other: object) -> "QOK":
        return self + other

    def __neg__(self) -> "QOK":
        return QOK(-self.num, self.den)

    def __sub__(self, other: object) -> "QOK":
        return self + (-qcoerce(other))

    def __rsub__(self, other: object) -> "QOK":
        return qcoerce(other) - self

    def __mul__(self, other: object) -> "QOK":
        z = qcoerce(other)
        return QOK(self.num * z.num, self.den * z.den)

    def __rmul__(self, other: object) -> "QOK":
        return self * other

    def __truediv__(self, divisor: int) -> "QOK":
        if not isinstance(divisor, int):
            return NotImplemented
        return QOK(self.num, self.den * divisor)

    def conjugate(self) -> "QOK":
        return QOK(self.num.conjugate(), self.den)


def qcoerce(value: object) -> QOK:
    if isinstance(value, QOK):
        return value
    if isinstance(value, OK):
        return QOK(value)
    if isinstance(value, int):
        return QOK(OK(value))
    return NotImplemented  # type: ignore[return-value]


QZERO = QOK(ZERO)
QONE = QOK(ONE)


@dataclass(frozen=True, slots=True)
class HamiltonQuaternion:
    """a0+a1*i+a2*j+a3*k with i^2=j^2=k^2=-1 and k=i*j."""

    a0: QOK = QZERO
    a1: QOK = QZERO
    a2: QOK = QZERO
    a3: QOK = QZERO

    @classmethod
    def from_coefficients(cls, values: Iterable[object], denominator: int = 1) -> "HamiltonQuaternion":
        vals = tuple(values)
        if len(vals) != 4:
            raise ValueError("four quaternion coefficients required")
        coeffs = tuple(qcoerce(v) / denominator for v in vals)
        return cls(*coeffs)

    def __add__(self, other: "HamiltonQuaternion") -> "HamiltonQuaternion":
        return HamiltonQuaternion(*(a + b for a, b in zip(self.coefficients, other.coefficients)))

    def __neg__(self) -> "HamiltonQuaternion":
        return HamiltonQuaternion(*(-a for a in self.coefficients))

    def __sub__(self, other: "HamiltonQuaternion") -> "HamiltonQuaternion":
        return self + (-other)

    def __mul__(self, other: "HamiltonQuaternion") -> "HamiltonQuaternion":
        a, b, c, d = self.coefficients
        e, f, g, h = other.coefficients
        return HamiltonQuaternion(
            a * e - b * f - c * g - d * h,
            a * f + b * e + c * h - d * g,
            a * g - b * h + c * e + d * f,
            a * h + b * g - c * f + d * e,
        )

    def __pow__(self, exponent: int) -> "HamiltonQuaternion":
        if exponent < 0:
            raise ValueError("negative quaternion powers are not implemented")
        result = HONE
        base = self
        n = exponent
        while n:
            if n & 1:
                result = result * base
            base = base * base
            n >>= 1
        return result

    @property
    def coefficients(self) -> tuple[QOK, QOK, QOK, QOK]:
        return self.a0, self.a1, self.a2, self.a3

    def conjugate(self) -> "HamiltonQuaternion":
        return HamiltonQuaternion(self.a0, -self.a1, -self.a2, -self.a3)

    def reduced_trace(self) -> QOK:
        return 2 * self.a0

    def reduced_norm(self) -> QOK:
        product = self * self.conjugate()
        if product.a1 != QZERO or product.a2 != QZERO or product.a3 != QZERO:
            raise ArithmeticError("quaternion norm is not central")
        return product.a0


HONE = HamiltonQuaternion(QONE)
HI = HamiltonQuaternion(QZERO, QONE)
HJ = HamiltonQuaternion(QZERO, QZERO, QONE)
HK = HI * HJ


def icosian_group_generators() -> tuple[HamiltonQuaternion, ...]:
    omega_bar = ONE - A
    return (
        HI,
        HJ,
        HK,
        HamiltonQuaternion.from_coefficients((-1, 1, 1, 1), 2),
        HamiltonQuaternion.from_coefficients((0, 1, A, omega_bar), 2),
    )


def icosian_order_basis() -> tuple[HamiltonQuaternion, ...]:
    omega_bar = ONE - A
    return tuple(
        HamiltonQuaternion.from_coefficients(v, 2)
        for v in (
            (1, -omega_bar, A, 0),
            (0, -omega_bar, 1, A),
            (0, A, -omega_bar, 1),
            (0, 1, A, -omega_bar),
        )
    )


Matrix2 = tuple[tuple[OK, OK], tuple[OK, OK]]


def matrix_add(ring: PrincipalQuotient, left: Matrix2, right: Matrix2) -> Matrix2:
    return tuple(
        tuple(ring.add(left[i][j], right[i][j]) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def matrix_neg(ring: PrincipalQuotient, matrix: Matrix2) -> Matrix2:
    return tuple(
        tuple(ring.reduce(-matrix[i][j]) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def matrix_mul(ring: PrincipalQuotient, left: Matrix2, right: Matrix2) -> Matrix2:
    return tuple(
        tuple(
            ring.add(
                ring.mul(left[i][0], right[0][j]),
                ring.mul(left[i][1], right[1][j]),
            )
            for j in range(2)
        )
        for i in range(2)
    )  # type: ignore[return-value]


def matrix_scalar(ring: PrincipalQuotient, scalar: OK, matrix: Matrix2) -> Matrix2:
    scalar = ring.reduce(scalar)
    return tuple(
        tuple(ring.mul(scalar, matrix[i][j]) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def matrix_trace(ring: PrincipalQuotient, matrix: Matrix2) -> OK:
    return ring.add(matrix[0][0], matrix[1][1])


def matrix_determinant(ring: PrincipalQuotient, matrix: Matrix2) -> OK:
    return ring.add(
        ring.mul(matrix[0][0], matrix[1][1]),
        -ring.mul(matrix[0][1], matrix[1][0]),
    )


def identity_matrix(ring: PrincipalQuotient) -> Matrix2:
    return ((ring.reduce(ONE), ring.reduce(ZERO)), (ring.reduce(ZERO), ring.reduce(ONE)))


def zero_matrix(ring: PrincipalQuotient) -> Matrix2:
    z = ring.reduce(ZERO)
    return ((z, z), (z, z))


def quotient_characteristic(ring: PrincipalQuotient) -> int:
    for n in range(1, ring.order + 1):
        if ring.reduce(n) == ZERO:
            return n
    raise ArithmeticError("failed to determine quotient characteristic")


def map_qok(ring: PrincipalQuotient, value: QOK) -> OK:
    characteristic = quotient_characteristic(ring)
    if gcd(value.den, characteristic) != 1:
        raise ZeroDivisionError(f"denominator {value.den} is not invertible")
    inv = pow(value.den, -1, characteristic)
    return ring.reduce(inv * value.num)


def square_root_minus_one(ring: PrincipalQuotient) -> OK:
    minus_one = ring.reduce(-ONE)
    for candidate in ring.elements():
        if ring.mul(candidate, candidate) == minus_one:
            return candidate
    raise ArithmeticError("-1 has no square root in quotient ring")


def sum_two_squares_minus_one(ring: PrincipalQuotient) -> tuple[OK, OK]:
    """Find u,v with u^2+v^2=-1 in the finite quotient ring."""
    minus_one = ring.reduce(-ONE)
    elements = tuple(ring.elements())
    squares: dict[OK, OK] = {}
    for value in elements:
        squares.setdefault(ring.mul(value, value), value)
    for u in elements:
        needed = ring.add(minus_one, -ring.mul(u, u))
        if needed in squares:
            return u, squares[needed]
    raise ArithmeticError("Hamilton algebra did not split over quotient ring")


@dataclass(frozen=True, slots=True)
class LocalHamiltonSplitting:
    ring: PrincipalQuotient
    I: Matrix2
    J: Matrix2
    K: Matrix2
    sqrt_minus_one: OK

    @classmethod
    def build(cls, ring: PrincipalQuotient) -> "LocalHamiltonSplitting":
        z = ring.reduce(ZERO)
        o = ring.reduce(ONE)
        m = ring.reduce(-ONE)
        I = ((z, m), (o, z))
        try:
            s = square_root_minus_one(ring)
            J = ((z, s), (s, z))
        except ArithmeticError:
            u, v = sum_two_squares_minus_one(ring)
            s = z  # sentinel: the general two-square splitting was used
            J = ((u, v), (v, ring.reduce(-u)))
        K = matrix_mul(ring, I, J)
        model = cls(ring, I, J, K, s)
        ident = identity_matrix(ring)
        assert matrix_mul(ring, I, I) == matrix_neg(ring, ident)
        assert matrix_mul(ring, J, J) == matrix_neg(ring, ident)
        assert matrix_mul(ring, I, J) == matrix_neg(ring, matrix_mul(ring, J, I))
        return model

    def map(self, quaternion: HamiltonQuaternion) -> Matrix2:
        matrices = (identity_matrix(self.ring), self.I, self.J, self.K)
        result = zero_matrix(self.ring)
        for coefficient, matrix in zip(quaternion.coefficients, matrices):
            result = matrix_add(
                self.ring,
                result,
                matrix_scalar(self.ring, map_qok(self.ring, coefficient), matrix),
            )
        return result


def self_test() -> None:
    assert HI * HI == -HONE
    assert HJ * HJ == -HONE
    assert HK == HI * HJ
    assert HI * HJ == -(HJ * HI)

    group_gens = icosian_group_generators()
    order_basis = icosian_order_basis()
    assert len(group_gens) == 5
    assert len(order_basis) == 4
    assert all(g.reduced_norm() == QONE for g in group_gens)
    assert all(b.reduced_norm() == QONE for b in order_basis)

    n23 = beal_level(2)
    n33 = beal_level(3)
    local_rings = (n23.left, n23.right, n33.left, n33.right)
    rng = Random(357)
    test_quaternions = list(group_gens) + list(order_basis)
    for _ in range(40):
        values = [OK(rng.randrange(-4, 5), rng.randrange(-4, 5)) for _ in range(4)]
        test_quaternions.append(HamiltonQuaternion.from_coefficients(values))

    for ring in local_rings:
        splitting = LocalHamiltonSplitting.build(ring)
        ident = identity_matrix(ring)
        assert splitting.map(HONE) == ident
        for q in test_quaternions:
            image = splitting.map(q)
            assert matrix_trace(ring, image) == map_qok(ring, q.reduced_trace())
            assert matrix_determinant(ring, image) == map_qok(ring, q.reduced_norm())
        for left in test_quaternions[:20]:
            for right in test_quaternions[:20]:
                assert splitting.map(left * right) == matrix_mul(
                    ring, splitting.map(left), splitting.map(right)
                )

    print("Hamilton quaternion identities: OK")
    print("icosian generators and order basis have reduced norm 1")
    for ring in local_rings:
        splitting = LocalHamiltonSplitting.build(ring)
        print(
            f"quotient order {ring.order}: sqrt(-1)={splitting.sqrt_minus_one}; "
            "multiplicativity/trace/determinant OK"
        )


if __name__ == "__main__":
    self_test()