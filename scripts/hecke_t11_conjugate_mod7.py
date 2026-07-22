#!/usr/bin/env python3
"""Construct the conjugate norm-11 Hecke operator T_(4-a) modulo 7.

The 12 representatives are obtained from the 1440 icosians of reduced norm
4-a, modulo left multiplication by the 120 norm-one units.  The resulting
operator is checked against both T_2 and T_(3+a).
"""
from __future__ import annotations

import argparse
import pickle
from pathlib import Path

from paths import DATA_DIR

from ok_sqrt5 import A
from enumerate_icosians import enumerate_norm, left_unit_orbits
from hecke_t2_mod7 import global_orbit_and_t2
from hecke_t11_mod7 import (
    global_orbit_and_hecke,
    hecke_representatives_11,
    sparse_product,
)


def hecke_representatives_11_conjugate():
    target = 4 - A
    elements = enumerate_norm(target, 3)
    if len(elements) != 1440:
        raise ArithmeticError(
            f"expected 1440 norm-(4-a) elements, found {len(elements)}"
        )
    orbits = left_unit_orbits(elements)
    if len(orbits) != 12 or any(len(orbit) != 120 for orbit in orbits):
        raise ArithmeticError("wrong norm-(4-a) unit-orbit decomposition")
    return tuple(orbit[0].conjugate() for orbit in orbits)


def self_test(exponents: tuple[int, ...]) -> None:
    cache_path = DATA_DIR / "hecke_t11_conjugate_mod7.pkl"
    cache = {}
    if cache_path.exists():
        with cache_path.open("rb") as handle:
            cache = pickle.load(handle)

    conjugate_elements = hecke_representatives_11_conjugate()
    ordinary_elements = hecke_representatives_11()
    assert len(conjugate_elements) == 12
    print("norm-(4-a) enumeration: 1440 = 120*12, OK", flush=True)

    for exponent in exponents:
        reps2, t2 = global_orbit_and_t2(exponent)
        reps11, t11 = global_orbit_and_hecke(exponent, ordinary_elements)
        if exponent in cache:
            reps11c, t11c = cache[exponent]
            print(f"N_{exponent}3: loaded conjugate operator cache", flush=True)
        else:
            reps11c, t11c = global_orbit_and_hecke(exponent, conjugate_elements)
            cache[exponent] = (reps11c, t11c)
            cache_path.parent.mkdir(parents=True, exist_ok=True)
            with cache_path.open("wb") as handle:
                pickle.dump(cache, handle, protocol=pickle.HIGHEST_PROTOCOL)
            print(f"N_{exponent}3: cached conjugate operator", flush=True)
        assert reps2 == reps11 == reps11c
        assert all(sum(row.values()) % 7 == 12 % 7 for row in t11c)
        assert sparse_product(t2, t11c) == sparse_product(t11c, t2)
        assert sparse_product(t11, t11c) == sparse_product(t11c, t11)
        print(
            f"N_{exponent}3: dimension={len(t11c)}, "
            f"T11_conj mod 7 nnz={sum(len(row) for row in t11c)}, "
            "commutes with T2 and T11",
            flush=True,
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("exponent", nargs="?", type=int, choices=(2, 3))
    args = parser.parse_args()
    self_test((args.exponent,) if args.exponent else (2, 3))