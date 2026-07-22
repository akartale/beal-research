#!/usr/bin/env python3
"""Construct the two split norm-19 Hecke operators modulo 7."""
from __future__ import annotations

import argparse
import pickle
from pathlib import Path

from paths import DATA_DIR

from ok_sqrt5 import A
from icosian_mod_n import HamiltonQuaternion, QOK
from enumerate_icosians import enumerate_norm, left_unit_orbits
from hecke_t2_mod7 import global_orbit_and_t2
from hecke_t11_mod7 import global_orbit_data, global_hecke_from_data, sparse_product

CACHE = DATA_DIR / "hecke_t19_pair_mod7.pkl"


def field_conjugate(q: HamiltonQuaternion) -> HamiltonQuaternion:
    return HamiltonQuaternion(*(QOK(c.num.conjugate(), c.den) for c in q.coefficients))


def representatives(target):
    elements = enumerate_norm(target, 4)
    expected = 120 * 20
    if len(elements) != expected:
        raise ArithmeticError(
            f"full bound-4 enumeration found {len(elements)} norm-{target} elements, "
            f"expected {expected}"
        )
    orbits = left_unit_orbits(elements)
    if len(orbits) != 20 or any(len(o) != 120 for o in orbits):
        raise ArithmeticError(f"wrong norm-{target} unit-orbit decomposition")
    print(f"norm-{target}: full bound-4 enumeration recovered {len(elements)}", flush=True)
    return tuple(orbit[0].conjugate() for orbit in orbits)


def main(exponent: int):
    cache = {}
    if CACHE.exists():
        with CACHE.open("rb") as handle:
            cache = pickle.load(handle)
    reps2, t2 = global_orbit_and_t2(exponent)
    orbit_data = global_orbit_data(exponent)
    if exponent in cache:
        reps19a, t19a, _, _ = cache[exponent]
        print("loaded cached norm-(4+a) operator", flush=True)
    else:
        reps_a = representatives(4 + A)
        reps19a, t19a = global_hecke_from_data(orbit_data, reps_a)
    reps_b = representatives(5 - A)
    reps19b, t19b = global_hecke_from_data(orbit_data, reps_b)
    cache[exponent] = (reps19a, t19a, reps19b, t19b)
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    with CACHE.open("wb") as handle:
        pickle.dump(cache, handle, protocol=pickle.HIGHEST_PROTOCOL)
    print("both norm-19 operators constructed by direct unit-closed enumeration", flush=True)
    assert reps2 == reps19a == reps19b
    assert all(sum(row.values()) % 7 == 20 % 7 for row in t19a)
    assert all(sum(row.values()) % 7 == 20 % 7 for row in t19b)
    assert sparse_product(t2, t19a) == sparse_product(t19a, t2)
    assert sparse_product(t2, t19b) == sparse_product(t19b, t2)
    assert sparse_product(t19a, t19b) == sparse_product(t19b, t19a)
    print(f"N_23 dimension={len(t2)}, nnz=({sum(map(len,t19a))},{sum(map(len,t19b))}), commute OK", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("exponent", type=int, choices=(2, 3), nargs="?", default=2)
    args = parser.parse_args()
    main(args.exponent)