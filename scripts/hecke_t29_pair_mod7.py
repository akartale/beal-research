#!/usr/bin/env python3
"""Construct the two split norm-29 Hecke operators modulo 7 at level (2,3)."""
from __future__ import annotations

import argparse
import pickle
from pathlib import Path

from paths import DATA_DIR

from ok_sqrt5 import A
from enumerate_icosians import enumerate_norm, left_unit_orbits
from icosian_orbits import generate_icosian_group
from hecke_t2_mod7 import global_orbit_and_t2
from hecke_t11_mod7 import global_orbit_data, global_hecke_from_data, sparse_product

CACHE = DATA_DIR / "hecke_t29_pair_mod7.pkl"


def representatives(target):
    partial = enumerate_norm(target, 3)
    expected = 120 * 30
    units = generate_icosian_group()
    elements = {u * q for q in partial for u in units}
    if len(elements) != expected:
        raise ArithmeticError(
            f"unit closure of {len(partial)} norm-{target} elements has "
            f"size {len(elements)}, expected {expected}"
        )
    if any(q.reduced_norm().num != target for q in elements):
        raise ArithmeticError("unit closure changed the prescribed reduced norm")
    orbits = left_unit_orbits(elements)
    if len(orbits) != 30 or any(len(o) != 120 for o in orbits):
        raise ArithmeticError(f"wrong norm-{target} unit-orbit decomposition")
    print(
        f"norm-{target}: bound-3 found {len(partial)}, unit closure recovered {len(elements)}",
        flush=True,
    )
    return tuple(orbit[0].conjugate() for orbit in orbits)


def main(exponent: int):
    cache = {}
    if CACHE.exists():
        with CACHE.open("rb") as handle:
            cache = pickle.load(handle)
    reps2, t2 = global_orbit_and_t2(exponent)
    orbit_data = global_orbit_data(exponent)
    if exponent in cache:
        reps29a, t29a, reps29b, t29b = cache[exponent]
        print("loaded cached norm-29 operators", flush=True)
    else:
        reps_a = representatives(5 + A)
        reps_b = representatives(6 - A)
        reps29a, t29a = global_hecke_from_data(orbit_data, reps_a)
        reps29b, t29b = global_hecke_from_data(orbit_data, reps_b)
        cache[exponent] = (reps29a, t29a, reps29b, t29b)
        CACHE.parent.mkdir(parents=True, exist_ok=True)
        with CACHE.open("wb") as handle:
            pickle.dump(cache, handle, protocol=pickle.HIGHEST_PROTOCOL)
    assert reps2 == reps29a == reps29b
    assert all(sum(row.values()) % 7 == 30 % 7 for row in t29a)
    assert all(sum(row.values()) % 7 == 30 % 7 for row in t29b)
    assert sparse_product(t2, t29a) == sparse_product(t29a, t2)
    assert sparse_product(t2, t29b) == sparse_product(t29b, t2)
    assert sparse_product(t29a, t29b) == sparse_product(t29b, t29a)
    print(f"N_23 dimension={len(t2)}, nnz=({sum(map(len,t29a))},{sum(map(len,t29b))}), commute OK", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("exponent", type=int, choices=(2, 3), nargs="?", default=2)
    args = parser.parse_args()
    main(args.exponent)