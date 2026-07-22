#!/usr/bin/env python3
"""Construct T_q modulo 7 for q=(3+a), Norm(q)=11.

The 12 Hecke representatives are obtained by enumerating the 1440 icosians of
reduced norm 3+a and quotienting by left multiplication by the 120 norm-one
units.  The resulting sparse operator is checked against T_2 by commutation.
"""
from __future__ import annotations

from ok_sqrt5 import A
from p1_sqrt5 import CRTProjectiveLine
from icosian_mod_n import LocalHamiltonSplitting, icosian_group_generators
from enumerate_icosians import enumerate_norm, left_unit_orbits
from hecke_t2_mod7 import DSU, global_orbit_and_t2


def hecke_representatives_11():
    target = 3 + A
    elements = enumerate_norm(target, 3)
    if len(elements) != 1440:
        raise ArithmeticError(f"expected 1440 norm-(3+a) elements, found {len(elements)}")
    orbits = left_unit_orbits(elements)
    if len(orbits) != 12 or any(len(o) != 120 for o in orbits):
        raise ArithmeticError("wrong norm-(3+a) unit-orbit decomposition")
    # psage acts by inverses.  Projectively inverse(q) equals conjugate(q), up
    # to the central norm scalar.
    return tuple(orbit[0].conjugate() for orbit in orbits)


def global_orbit_data(exponent_at_3: int, exponent_at_5: int = 3):
    space = CRTProjectiveLine(exponent_at_3, exponent_at_5)
    left_split = LocalHamiltonSplitting.build(space.left.ring)
    right_split = LocalHamiltonSplitting.build(space.right.ring)
    unit_left = tuple(left_split.map(g) for g in icosian_group_generators())
    unit_right = tuple(right_split.map(g) for g in icosian_group_generators())
    left_order = space.left.order
    dsu = DSU.build(space.order)

    for ml, mr in zip(unit_left, unit_right):
        lp = tuple(space.left.index(space.left.act_row(p, ml)) for p in space.left.points)
        rp = tuple(space.right.index(space.right.act_row(p, mr)) for p in space.right.points)
        for r in range(space.right.order):
            sb = left_order * r
            tb = left_order * rp[r]
            for l in range(left_order):
                dsu.union(sb + l, tb + lp[l])

    roots = sorted({dsu.find(i) for i in range(space.order)})
    root_to_orbit = {root: i for i, root in enumerate(roots)}
    point_to_orbit = [root_to_orbit[dsu.find(i)] for i in range(space.order)]
    reps = [next(i for i in range(space.order) if point_to_orbit[i] == orbit) for orbit in range(len(roots))]

    return space, left_split, right_split, left_order, reps, point_to_orbit


def global_hecke_from_data(data, hecke_elements) -> tuple[list[int], list[dict[int, int]]]:
    space, left_split, right_split, left_order, reps, point_to_orbit = data
    hecke_left = tuple(left_split.map(q) for q in hecke_elements)
    hecke_right = tuple(right_split.map(q) for q in hecke_elements)
    rows: list[dict[int, int]] = []
    for rep in reps:
        r, l = divmod(rep, left_order)
        lp0 = space.left.from_index(l)
        rp0 = space.right.from_index(r)
        row: dict[int, int] = {}
        for ml, mr in zip(hecke_left, hecke_right):
            li = space.left.index(space.left.act_row(lp0, ml))
            ri = space.right.index(space.right.act_row(rp0, mr))
            target = point_to_orbit[li + left_order * ri]
            row[target] = (row.get(target, 0) + 1) % 7
        rows.append({j: c for j, c in row.items() if c})
    return reps, rows


def global_orbit_and_hecke(
    exponent_at_3: int, hecke_elements, exponent_at_5: int = 3
) -> tuple[list[int], list[dict[int, int]]]:
    return global_hecke_from_data(
        global_orbit_data(exponent_at_3, exponent_at_5), hecke_elements
    )


def sparse_product(left: list[dict[int, int]], right: list[dict[int, int]]) -> list[dict[int, int]]:
    result: list[dict[int, int]] = []
    for row in left:
        out: dict[int, int] = {}
        for middle, a in row.items():
            for column, b in right[middle].items():
                out[column] = (out.get(column, 0) + a * b) % 7
        result.append({j: c for j, c in out.items() if c})
    return result


def self_test() -> None:
    elements = hecke_representatives_11()
    assert len(elements) == 12
    print("norm-(3+a) enumeration: 1440 = 120*12, OK")
    for exponent in (2, 3):
        reps11, t11 = global_orbit_and_hecke(exponent, elements)
        reps2, t2 = global_orbit_and_t2(exponent)
        assert reps11 == reps2
        assert all(sum(row.values()) % 7 == 12 % 7 for row in t11)
        assert sparse_product(t2, t11) == sparse_product(t11, t2)
        print(
            f"N_{exponent}3: dimension={len(t11)}, "
            f"T11 mod 7 nnz={sum(len(r) for r in t11)}, commutes with T2"
        )


if __name__ == "__main__":
    self_test()