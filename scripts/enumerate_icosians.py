#!/usr/bin/env python3
"""Enumerate prescribed-norm icosians in the rank-8 integral basis.

For a totally positive prime generator pi, all elements of reduced norm pi form
120*(Norm(pi)+1) elements; quotienting by left multiplication by the 120
norm-one units gives the required Norm(pi)+1 Hecke representatives.
"""
from __future__ import annotations

from itertools import product

from ok_sqrt5 import A, OK
from icosian_mod_n import HamiltonQuaternion, QOK, icosian_order_basis
from icosian_orbits import generate_icosian_group


def zz_basis() -> tuple[HamiltonQuaternion, ...]:
    basis4 = icosian_order_basis()
    return basis4 + tuple(
        HamiltonQuaternion(*(QOK(A) * c for c in b.coefficients)) for b in basis4
    )


def linear_combination(coefficients: tuple[int, ...], basis: tuple[HamiltonQuaternion, ...]) -> HamiltonQuaternion:
    result = HamiltonQuaternion()
    for coefficient, vector in zip(coefficients, basis):
        if coefficient:
            term = HamiltonQuaternion(*(coefficient * c for c in vector.coefficients))
            result = result + term
    return result


def _raw_basis_vectors() -> tuple[tuple[tuple[int, int], ...], ...]:
    """Return the rank-8 basis as four numerator pairs over denominator 2."""
    basis = zz_basis()
    result = []
    for q in basis:
        row = []
        for c in q.coefficients:
            if c.den not in (1, 2):
                raise ArithmeticError("unexpected basis denominator")
            scale = 2 // c.den
            row.append((scale * c.num.x, scale * c.num.y))
        result.append(tuple(row))
    return tuple(result)


def _square_pair(x: int, y: int) -> tuple[int, int]:
    """Square x+y*a using a^2=a+1."""
    return x * x + y * y, 2 * x * y + y * y


def enumerate_norm(target: OK, bound: int) -> set[HamiltonQuaternion]:
    """Fast integer enumeration; only matching vectors are materialized."""
    basis = zz_basis()
    raw = _raw_basis_vectors()
    wanted_x, wanted_y = 4 * target.x, 4 * target.y
    found: set[HamiltonQuaternion] = set()
    values = range(-bound, bound + 1)
    for coefficients in product(values, repeat=8):
        components = [[0, 0] for _ in range(4)]
        for coefficient, vector in zip(coefficients, raw):
            if coefficient:
                for j in range(4):
                    components[j][0] += coefficient * vector[j][0]
                    components[j][1] += coefficient * vector[j][1]
        nx = ny = 0
        for x, y in components:
            sx, sy = _square_pair(x, y)
            nx += sx
            ny += sy
        if nx == wanted_x and ny == wanted_y:
            found.add(linear_combination(coefficients, basis))
    return found


def left_unit_orbits(elements: set[HamiltonQuaternion]) -> tuple[tuple[HamiltonQuaternion, ...], ...]:
    units = generate_icosian_group()
    remaining = set(elements)
    orbits = []
    while remaining:
        seed = next(iter(remaining))
        orbit = {u * seed for u in units}
        missing = orbit - elements
        if missing:
            raise ArithmeticError(f"enumeration bound incomplete: {len(missing)} unit translates missing")
        remaining -= orbit
        orbits.append(tuple(orbit))
    return tuple(orbits)


def representatives(target: OK, bound: int) -> tuple[HamiltonQuaternion, ...]:
    elements = enumerate_norm(target, bound)
    orbits = left_unit_orbits(elements)
    expected = abs(target.norm()) + 1
    if len(orbits) != expected:
        raise ArithmeticError(f"expected {expected} Hecke classes, found {len(orbits)}")
    if any(len(orbit) != 120 for orbit in orbits):
        raise ArithmeticError("nonfree unit action on prescribed-norm elements")
    return tuple(orbit[0].conjugate() for orbit in orbits)


def self_test() -> None:
    target = 3 + A
    assert target.norm() == 11
    for bound in (1, 2, 3):
        elements = enumerate_norm(target, bound)
        print(f"bound={bound}: norm-(3+a) elements={len(elements)}", flush=True)
        if len(elements) == 120 * 12:
            reps = representatives(target, bound)
            print(f"Hecke representatives: {len(reps)}")
            assert len(reps) == 12
            return
    raise AssertionError("bound 3 did not capture all norm-(3+a) icosians")


if __name__ == "__main__":
    self_test()