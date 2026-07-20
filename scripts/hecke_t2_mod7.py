#!/usr/bin/env python3
"""Construct the norm-4 Hecke operator T_2 on icosian orbit spaces.

The prime 2 is inert in Q(sqrt(5)), so its norm is 4 and T_2 has 5 coset
representatives.  psage records these five norm-2 icosians explicitly.  Since
projective action is unchanged by central scalars, we use their quaternion
conjugates instead of the literal inverses returned by psage.

This module validates the construction against psage's published level-31
matrix [[0,5],[3,2]], then computes sparse T_2 modulo 7 for N_23 and N_33.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass

from ok_sqrt5 import A, ONE, ZERO, OK, PrincipalQuotient
from p1_sqrt5 import LocalProjectiveLine, CRTProjectiveLine
from icosian_mod_n import (
    HamiltonQuaternion,
    LocalHamiltonSplitting,
    Matrix2,
    icosian_group_generators,
)


def hecke_elements_at_2() -> tuple[HamiltonQuaternion, ...]:
    """Five projectively normalized representatives for the inert prime 2."""
    raw = (
        (-A - 1, 0, A - 2, 1),
        (-A - 1, A - 1, -A + 1, A - 1),
        (-A - 1, -A + 1, -A + 1, A - 1),
        (-A - 1, -A + 2, -1, 0),
        (-A - 1, A - 2, -1, 0),
    )
    # psage uses inverses of these elements divided by 2.  In projective
    # action q^{-1}=conj(q)/Norm(q), and the central scalar Norm(q)^{-1}
    # is irrelevant, so conjugate(q) gives exactly the same P^1 action.
    return tuple(
        HamiltonQuaternion.from_coefficients(v, 2).conjugate() for v in raw
    )


@dataclass(slots=True)
class DSU:
    parent: list[int]
    size: list[int]

    @classmethod
    def build(cls, n: int) -> "DSU":
        return cls(list(range(n)), [1] * n)

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> None:
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]


def local_orbit_data(line: LocalProjectiveLine) -> tuple[tuple[int, ...], tuple[int, ...]]:
    split = LocalHamiltonSplitting.build(line.ring)
    dsu = DSU.build(line.order)
    for generator in icosian_group_generators():
        matrix = split.map(generator)
        for i, point in enumerate(line.points):
            j = line.index(line.act_row(point, matrix))
            dsu.union(i, j)
    roots = sorted({dsu.find(i) for i in range(line.order)})
    root_to_orbit = {root: i for i, root in enumerate(roots)}
    point_to_orbit = tuple(root_to_orbit[dsu.find(i)] for i in range(line.order))
    reps = tuple(next(i for i in range(line.order) if point_to_orbit[i] == orbit) for orbit in range(len(roots)))
    return reps, point_to_orbit


def local_hecke_matrix_t2(line: LocalProjectiveLine) -> list[dict[int, int]]:
    reps, point_to_orbit = local_orbit_data(line)
    split = LocalHamiltonSplitting.build(line.ring)
    matrices = tuple(split.map(q) for q in hecke_elements_at_2())
    rows: list[dict[int, int]] = []
    for rep in reps:
        point = line.from_index(rep)
        row: dict[int, int] = {}
        for matrix in matrices:
            image = line.index(line.act_row(point, matrix))
            target = point_to_orbit[image]
            row[target] = row.get(target, 0) + 1
        rows.append(row)
    return rows


def global_orbit_and_t2(exponent_at_3: int) -> tuple[list[int], list[dict[int, int]]]:
    space = CRTProjectiveLine(exponent_at_3)
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

    hecke_left = tuple(left_split.map(q) for q in hecke_elements_at_2())
    hecke_right = tuple(right_split.map(q) for q in hecke_elements_at_2())
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


def dense(rows: list[dict[int, int]]) -> list[list[int]]:
    n = len(rows)
    return [[row.get(j, 0) for j in range(n)] for row in rows]


def self_test() -> None:
    qs = hecke_elements_at_2()
    assert len(qs) == 5
    # Level (5*a-2), norm 31, has residue field F_31 and two icosian orbits.
    ring31 = PrincipalQuotient.from_generator(5 * A - 2)
    assert ring31.order == 31
    line31 = LocalProjectiveLine(ring31, rational_prime=31, residue_size=31)
    assert line31.order == 32
    matrix31 = dense(local_hecke_matrix_t2(line31))
    published = [[0, 5], [3, 2]]
    swapped = [[published[1][1], published[1][0]], [published[0][1], published[0][0]]]
    assert matrix31 in (published, swapped), matrix31
    print(f"level-31 validation up to orbit permutation: {matrix31} OK")

    for exponent in (2, 3):
        reps, rows = global_orbit_and_t2(exponent)
        assert all(sum(row.values()) % 7 == 5 for row in rows)
        nnz = sum(len(row) for row in rows)
        print(f"N_{exponent}3: dimension={len(reps)}, T2 mod 7 nnz={nnz}, row-sum=5")


if __name__ == "__main__":
    self_test()