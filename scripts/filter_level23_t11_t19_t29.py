#!/usr/bin/env python3
"""Exact mod-7 intersection at split primes 11, 19, and 29 for level (2,3)."""
from __future__ import annotations

import pickle
from pathlib import Path

from paths import DATA_DIR

from filter_level23_t11_t19 import attainable_pairs, common_eigenspace_dim
from wiedemann_hecke_mod7 import build_or_load

D = DATA_DIR


def main():
    base = build_or_load()
    with (D / "hecke_t11_conjugate_mod7.pkl").open("rb") as f:
        c11 = pickle.load(f)
    with (D / "hecke_t19_pair_mod7.pkl").open("rb") as f:
        c19 = pickle.load(f)
    with (D / "hecke_t29_pair_mod7.pkl").open("rb") as f:
        c29 = pickle.load(f)

    _, t11a = base[2]
    _, t11b = c11[2]
    _, t19a, _, t19b = c19[2]
    _, t29a, _, t29b = c29[2]

    base_ops = ((t11a, 2), (t11b, 2), (t19a, 5), (t19b, 5))
    base_dim = common_eigenspace_dim(base_ops)
    print(f"base after 11 and 19 dimension={base_dim}")

    details, pairs = attainable_pairs(29)
    print(f"attainable t/traces at 29={details}")
    print(f"attainable ordered trace pairs mod 7={sorted(pairs)}")
    survivors = []
    for a, b in sorted(pairs):
        dim = common_eigenspace_dim(base_ops + ((t29a, a), (t29b, b)))
        print(f"29-pair=({a},{b}) joint dim={dim}")
        if dim:
            survivors.append((a, b, dim))
    print(f"surviving={survivors}")
    print(f"total surviving dimensions={sum(d for _, _, d in survivors)}")


if __name__ == "__main__":
    main()