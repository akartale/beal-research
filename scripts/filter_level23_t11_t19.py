#!/usr/bin/env python3
"""Intersect the level-(2,3) norm-11 survivor with attainable norm-19 traces."""
from __future__ import annotations

import pickle
from pathlib import Path

from paths import DATA_DIR

from filter_level23_t11_pairs import (
    P,
    count_fp,
    count_fp2,
    dense,
    rank_mod7,
    smooth,
)
from wiedemann_hecke_mod7 import build_or_load

CONJ11_CACHE = DATA_DIR / "hecke_t11_conjugate_mod7.pkl"
T19_CACHE = DATA_DIR / "hecke_t19_pair_mod7.pkl"


def common_eigenspace_dim(operators):
    n = len(operators[0][0])
    stacked = []
    for rows, eigenvalue in operators:
        matrix = dense(rows)
        for i, row in enumerate(matrix):
            row[i] = (row[i] - eigenvalue) % P
            stacked.append(row)
    return n - rank_mod7(stacked)


def attainable_pairs(ell: int):
    seventh = {pow(c, 7, ell) for c in range(1, ell)}
    fifth = {pow(b, 5, ell) for b in range(1, ell)}
    ts = set()
    for A in range(1, ell):
        A3 = pow(A, 3, ell)
        for B5 in fifth:
            if (A3 + B5) % ell in seventh:
                t = (-B5 * pow(A3, -1, ell)) % ell
                if smooth(t, ell):
                    ts.add(t)
    pairs = set()
    details = []
    for t in sorted(ts):
        n1, n2 = count_fp(t, ell), count_fp2(t, ell)
        trace_sum = 1 + ell - n1
        trace_product = (n2 - 1 - ell * ell + trace_sum * trace_sum) // 2 - 2 * ell
        roots = [
            r for r in range(P)
            if (r * r - trace_sum * r + trace_product) % P == 0
        ]
        for first in roots:
            pairs.add((first, (trace_sum - first) % P))
        details.append((t, trace_sum % P, trace_product % P, tuple(roots)))
    return details, pairs


def main():
    data = build_or_load()
    with CONJ11_CACHE.open("rb") as handle:
        conjugate11 = pickle.load(handle)
    with T19_CACHE.open("rb") as handle:
        pair19 = pickle.load(handle)
    _, t11a = data[2]
    _, t11b = conjugate11[2]
    _, t19a, _, t19b = pair19[2]
    details, pairs = attainable_pairs(19)
    print(f"attainable t/traces at 19={details}")
    print(f"attainable ordered trace pairs mod 7={sorted(pairs)}")
    surviving = []
    base_dim = common_eigenspace_dim(((t11a, 2), (t11b, 2)))
    print(f"norm-11 base eigenspace dim={base_dim}")
    for first, second in sorted(pairs):
        dim = common_eigenspace_dim(
            ((t11a, 2), (t11b, 2), (t19a, first), (t19b, second))
        )
        print(f"19-pair=({first},{second}) joint dim={dim}")
        if dim:
            surviving.append((first, second, dim))
    print(f"surviving={surviving}")


if __name__ == "__main__":
    main()