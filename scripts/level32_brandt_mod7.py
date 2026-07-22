#!/usr/bin/env python3
"""Exact paired-Hecke Brandt sieve modulo 7 for level (3,2).

This is a dependency-free replacement for the unavailable Magma/Sage HMF
packet computation.  It constructs the full icosian Brandt module at
N = (3)^3 * (sqrt(5))^2, builds both split-prime Hecke operators at
11, 19, and 29 on one common orbit ordering, and computes exact simultaneous
kernel dimensions over F_7 for every attainable ordered Frey trace tuple.
"""
from __future__ import annotations

import pickle
from itertools import product

from paths import DATA_DIR
from filter_level23_t11_t19 import attainable_pairs, common_eigenspace_dim
from hecke_t2_mod7 import global_orbit_and_t2
from hecke_t11_mod7 import (
    global_orbit_data,
    global_hecke_from_data,
    hecke_representatives_11,
    sparse_product,
)
from hecke_t11_conjugate_mod7 import hecke_representatives_11_conjugate
from hecke_t19_pair_mod7 import field_conjugate, representatives as representatives19
from hecke_t29_pair_mod7 import representatives as representatives29
from ok_sqrt5 import A

P = 7
A3 = 3
B5 = 2
CACHE = DATA_DIR / "level32_paired_hecke_mod7.pkl"


def nnz(rows: list[dict[int, int]]) -> int:
    return sum(map(len, rows))


def validate_operator(rows: list[dict[int, int]], degree: int) -> None:
    assert all(sum(row.values()) % P == degree % P for row in rows)


def build_or_load():
    if CACHE.exists():
        with CACHE.open("rb") as handle:
            data = pickle.load(handle)
        print(f"loaded {CACHE}", flush=True)
        return data

    orbit_data = global_orbit_data(A3, B5)
    reps2, t2 = global_orbit_and_t2(A3, B5)

    reps11a, t11a = global_hecke_from_data(orbit_data, hecke_representatives_11())
    reps11b, t11b = global_hecke_from_data(
        orbit_data, hecke_representatives_11_conjugate()
    )

    reps19a_q = representatives19(4 + A)
    reps19b_q = representatives19(5 - A)
    reps19a, t19a = global_hecke_from_data(orbit_data, reps19a_q)
    reps19b, t19b = global_hecke_from_data(orbit_data, reps19b_q)

    reps29a_q = representatives29(5 + A)
    reps29b_q = representatives29(6 - A)
    reps29a, t29a = global_hecke_from_data(orbit_data, reps29a_q)
    reps29b, t29b = global_hecke_from_data(orbit_data, reps29b_q)

    assert reps2 == reps11a == reps11b == reps19a == reps19b == reps29a == reps29b
    for rows, degree in (
        (t2, 5),
        (t11a, 12), (t11b, 12),
        (t19a, 20), (t19b, 20),
        (t29a, 30), (t29b, 30),
    ):
        validate_operator(rows, degree)

    operators = (t11a, t11b, t19a, t19b, t29a, t29b)
    for rows in operators:
        assert sparse_product(t2, rows) == sparse_product(rows, t2)
    for i, left in enumerate(operators):
        for right in operators[i + 1:]:
            assert sparse_product(left, right) == sparse_product(right, left)

    data = {
        "reps": reps2,
        "t2": t2,
        "t11a": t11a,
        "t11b": t11b,
        "t19a": t19a,
        "t19b": t19b,
        "t29a": t29a,
        "t29b": t29b,
    }
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    with CACHE.open("wb") as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"wrote {CACHE}", flush=True)
    return data


def main() -> None:
    data = build_or_load()
    n = len(data["reps"])
    print(f"level=(3,2) dimension={n}", flush=True)
    print(
        "nnz=" + ",".join(
            f"{name}:{nnz(data[name])}"
            for name in ("t2", "t11a", "t11b", "t19a", "t19b", "t29a", "t29b")
        ),
        flush=True,
    )

    pairs11 = sorted(attainable_pairs(11)[1])
    pairs19 = sorted(attainable_pairs(19)[1])
    pairs29 = sorted(attainable_pairs(29)[1])
    print(f"pairs11={pairs11}", flush=True)
    print(f"pairs19={pairs19}", flush=True)
    print(f"pairs29={pairs29}", flush=True)

    survivors11 = []
    for pair11 in pairs11:
        ops11 = ((data["t11a"], pair11[0]), (data["t11b"], pair11[1]))
        dim11 = common_eigenspace_dim(ops11)
        print(f"11={pair11} dim11={dim11}", flush=True)
        if dim11:
            survivors11.append((pair11, ops11, dim11))

    survivors19 = []
    for pair11, ops11, _ in survivors11:
        for pair19 in pairs19:
            ops19 = ops11 + (
                (data["t19a"], pair19[0]),
                (data["t19b"], pair19[1]),
            )
            dim = common_eigenspace_dim(ops19)
            print(f"11={pair11} 19={pair19} dim1119={dim}", flush=True)
            if dim:
                survivors19.append((pair11, pair19, ops19, dim))

    survivors29 = []
    for pair11, pair19, ops19, _ in survivors19:
        for pair29 in pairs29:
            ops29 = ops19 + (
                (data["t29a"], pair29[0]),
                (data["t29b"], pair29[1]),
            )
            dim = common_eigenspace_dim(ops29)
            print(
                f"11={pair11} 19={pair19} 29={pair29} dim111929={dim}",
                flush=True,
            )
            if dim:
                survivors29.append((pair11, pair19, pair29, dim))

    print(f"survivors_after_11={[(p,d) for p,_,d in survivors11]}", flush=True)
    print(
        f"survivors_after_19={[(p11,p19,d) for p11,p19,_,d in survivors19]}",
        flush=True,
    )
    print(f"survivors_after_29={survivors29}", flush=True)
    print(f"eliminated={not survivors29}", flush=True)
    if survivors29:
        raise SystemExit(3)


if __name__ == "__main__":
    main()