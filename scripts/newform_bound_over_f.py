#!/usr/bin/env python3
"""Open reproduction of Magma's NewformBoundOverF trace correction.

For a two-dimensional representation with Frobenius trace a and determinant N,
the trace after a residue-field extension of degree d is

    S_0 = 2, S_1 = a, S_d = a*S_{d-1} - N*S_{d-2}.

MagmaCode.m uses only d=2, where S_2=a^2-2N.  This module implements every
positive d and computes the minimal polynomial of S_d from the coefficient
field relation by an exact resultant.
"""
from __future__ import annotations

from functools import reduce
from math import gcd, lcm
from typing import Iterable

import sympy as sp

A = sp.Symbol("a")
X = sp.Symbol("x")


def trace_power_expr(a: sp.Expr, degree: int, norm: int | sp.Expr) -> sp.Expr:
    """Return alpha^d+beta^d from alpha+beta=a and alpha*beta=norm."""
    if degree < 0:
        raise ValueError("residue-degree ratio must be nonnegative")
    if degree == 0:
        return sp.Integer(2)
    if degree == 1:
        return sp.expand(a)
    s0, s1 = sp.Integer(2), sp.expand(a)
    for _ in range(2, degree + 1):
        s0, s1 = s1, sp.expand(a * s1 - norm * s0)
    return s1


def _monic_squarefree(poly: sp.Poly) -> sp.Poly:
    p = sp.Poly(poly, poly.gens[0], domain=sp.QQ)
    if p.is_zero:
        raise ValueError("zero polynomial has no minimal polynomial")
    return sp.Poly(p.sqf_part().monic(), p.gens[0], domain=sp.QQ)


def expression_minpoly(
    field_minpoly: sp.Poly,
    expression: sp.Expr,
    *,
    generator: sp.Symbol = A,
    output: sp.Symbol = X,
) -> sp.Poly:
    """Compute the exact minimal polynomial of expression(generator).

    The input field_minpoly is assumed irreducible over Q.  The resultant may
    be a proper power when different conjugates have the same image; taking
    its squarefree part recovers the transformed element's minimal polynomial.
    """
    m = sp.Poly(field_minpoly, generator, domain=sp.QQ)
    relation = output - sp.sympify(expression)
    resultant = sp.resultant(m.as_expr(), relation, generator)
    return _monic_squarefree(sp.Poly(resultant, output, domain=sp.QQ))


def trace_power_minpoly(
    field_minpoly: sp.Poly,
    eigenvalue: sp.Expr,
    degree: int,
    norm: int,
    *,
    generator: sp.Symbol = A,
    output: sp.Symbol = X,
) -> sp.Poly:
    corrected = trace_power_expr(sp.sympify(eigenvalue), degree, norm)
    return expression_minpoly(
        field_minpoly, corrected, generator=generator, output=output
    )


def resultant_numerator_abs(left: sp.Poly, right: sp.Poly) -> int:
    variable = left.gens[0]
    right = sp.Poly(right.as_expr(), variable, domain=sp.QQ)
    value = sp.Rational(sp.resultant(left.as_expr(), right.as_expr(), variable))
    return abs(int(value.p))


def newform_bound_over_f(
    corrected_eigen_minpoly: sp.Poly,
    candidates: Iterable[sp.Poly],
    ell: int,
) -> int:
    """Exact open analogue of the final line of NewformBoundOverF()."""
    values = [ell]
    values.extend(
        resultant_numerator_abs(corrected_eigen_minpoly, candidate)
        for candidate in candidates
    )
    return reduce(lcm, values, 1)


def multiplicative_order_mod(value: int, modulus: int) -> int:
    if modulus <= 1 or gcd(value, modulus) != 1:
        raise ValueError(f"{value} is not a unit modulo {modulus}")
    value %= modulus
    current = 1
    for degree in range(1, sp.totient(modulus) + 1):
        current = current * value % modulus
        if current == 1:
            return degree
    raise ArithmeticError("multiplicative order not found")


def cyclotomic_inertia_degree(ell: int, conductor: int) -> int:
    """Inertia degree in Q(zeta_conductor), for ell not dividing conductor."""
    return multiplicative_order_mod(ell, conductor)


def real_prime_cyclotomic_inertia_degree(ell: int, q: int) -> int:
    """Inertia degree in Q(zeta_q)^+ for odd prime q and ell != q."""
    if q < 3 or not sp.isprime(q) or ell == q:
        raise ValueError("q must be an odd prime distinct from ell")
    order = multiplicative_order_mod(ell, q)
    return order // 2 if order % 2 == 0 else order


def quadratic_inertia_degree(ell: int, discriminant: int) -> int:
    """Inertia degree at an unramified prime in Q(sqrt(discriminant))."""
    if discriminant % ell == 0:
        raise ValueError("ramified prime")
    return 1 if sp.legendre_symbol(discriminant, ell) == 1 else 2


def split_meta_7p3(ell: int) -> tuple[int, int, int, int]:
    """Return (f_K,f_F,d,N) for K=Q(zeta_7)^+, F=Q(zeta_21)."""
    if gcd(ell, 21) != 1:
        raise ValueError("ell must be coprime to 21")
    f_k = real_prime_cyclotomic_inertia_degree(ell, 7)
    f_f = cyclotomic_inertia_degree(ell, 21)
    if f_f % f_k:
        raise ArithmeticError("incompatible inertia degrees")
    degree = f_f // f_k
    return f_k, f_f, degree, ell**f_k


def _self_test() -> None:
    assert sp.expand(trace_power_expr(A, 2, 11)) == A**2 - 22
    assert sp.expand(trace_power_expr(A, 3, 11)) == A**3 - 33 * A
    assert sp.expand(trace_power_expr(A, 4, 11)) == A**4 - 44 * A**2 + 242

    # The two conjugates +/-sqrt(5) have the same corrected trace at d=2.
    collapsed = trace_power_minpoly(
        sp.Poly(A**2 - 5, A), A, 2, 11, generator=A, output=X
    )
    assert collapsed == sp.Poly(X + 17, X, domain=sp.QQ)

    assert split_meta_7p3(11) == (3, 6, 2, 1331)
    assert split_meta_7p3(13) == (1, 2, 2, 13)
    assert split_meta_7p3(43) == (1, 1, 1, 43)

    # Original (5,3) code at ell=11 takes the same d=2 branch.
    assert quadratic_inertia_degree(11, 5) == 1
    assert cyclotomic_inertia_degree(11, 15) == 2


if __name__ == "__main__":
    _self_test()
    print("NewformBoundOverF open self-test: OK")