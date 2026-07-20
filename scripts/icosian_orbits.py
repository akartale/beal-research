#!/usr/bin/env python3
"""Icosian unit-group orbits on P^1 for the two Beal target levels.

The exact norm-one icosian group has order 120.  We generate it from the five
standard generators, map those generators to each local matrix ring, precompute
their permutations on the local projective lines, and combine them by CRT.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass

from icosian_mod_n import (
    HamiltonQuaternion,
    LocalHamiltonSplitting,
    icosian_group_generators,
)
from p1_sqrt5 import CRTProjectiveLine, LocalProjectiveLine


def generate_icosian_group() -> tuple[HamiltonQuaternion, ...]:
    generators = icosian_group_generators()
    identity = HamiltonQuaternion.from_coefficients((1, 0, 0, 0))
    seen = {identity}
    queue = deque([identity])
    while queue:
        current = queue.popleft()
        for generator in generators:
            nxt = current * generator
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
                if len(seen) > 120:
                    raise ArithmeticError("icosian unit closure exceeded order 120")
    if len(seen) != 120:
        raise ArithmeticError(f"expected 120 norm-one icosians, found {len(seen)}")
    return tuple(seen)


def local_generator_permutations(line: LocalProjectiveLine) -> tuple[tuple[int, ...], ...]:
    splitting = LocalHamiltonSplitting.build(line.ring)
    permutations = []
    for generator in icosian_group_generators():
        matrix = splitting.map(generator)
        image = tuple(line.index(line.act_row(point, matrix)) for point in line.points)
        if len(set(image)) != line.order:
            raise ArithmeticError("unit generator does not act bijectively on local P1")
        permutations.append(image)
    return tuple(permutations)


@dataclass(slots=True)
class DisjointSet:
    parent: list[int]
    size: list[int]

    @classmethod
    def build(cls, n: int) -> "DisjointSet":
        return cls(list(range(n)), [1] * n)

    def find(self, x: int) -> int:
        parent = self.parent
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(self, x: int, y: int) -> None:
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]


def global_orbit_sizes(exponent_at_3: int) -> tuple[int, ...]:
    space = CRTProjectiveLine(exponent_at_3)
    left_perms = local_generator_permutations(space.left)
    right_perms = local_generator_permutations(space.right)
    dsu = DisjointSet.build(space.order)
    left_order = space.left.order

    for generator_index in range(len(left_perms)):
        lp = left_perms[generator_index]
        rp = right_perms[generator_index]
        for right in range(space.right.order):
            source_base = left_order * right
            target_base = left_order * rp[right]
            for left in range(left_order):
                dsu.union(source_base + left, target_base + lp[left])

    counts: dict[int, int] = {}
    for index in range(space.order):
        root = dsu.find(index)
        counts[root] = counts.get(root, 0) + 1
    sizes = tuple(sorted(counts.values()))
    if sum(sizes) != space.order:
        raise ArithmeticError("orbit partition has wrong total size")
    if any(120 % size != 0 for size in sizes):
        raise ArithmeticError("orbit size does not divide group order 120")
    return sizes


def summarize(exponent_at_3: int) -> None:
    space = CRTProjectiveLine(exponent_at_3)
    sizes = global_orbit_sizes(exponent_at_3)
    histogram: dict[int, int] = {}
    for size in sizes:
        histogram[size] = histogram.get(size, 0) + 1
    print(f"N_{exponent_at_3}3: P1 size={space.order}, orbit count={len(sizes)}")
    print("orbit-size histogram:", " ".join(f"{size}:{count}" for size, count in sorted(histogram.items())))


def self_test() -> None:
    group = generate_icosian_group()
    assert len(group) == 120
    assert all(element.reduced_norm().num.x == element.reduced_norm().den for element in group)
    assert all(element.reduced_norm().num.y == 0 for element in group)
    print("exact icosian unit group order: 120")
    summarize(2)
    summarize(3)


if __name__ == "__main__":
    self_test()