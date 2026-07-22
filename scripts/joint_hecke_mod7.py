#!/usr/bin/env python3
"""Joint Wiedemann probes for T2 and the two norm-11 Hecke operators mod 7."""
from __future__ import annotations

import argparse
import pickle
from pathlib import Path

from paths import DATA_DIR

from wiedemann_hecke_mod7 import (
    build_or_load,
    sparse_linear_combination,
    trial,
)

CONJ_CACHE = DATA_DIR / "hecke_t11_conjugate_mod7.pkl"


def add_three(t2, t11a, t11b, a: int, b: int):
    return sparse_linear_combination(
        sparse_linear_combination(t2, t11a, a), t11b, b
    )


def main(exponent: int) -> None:
    data = build_or_load()
    with CONJ_CACHE.open("rb") as handle:
        conjugate = pickle.load(handle)
    if exponent not in conjugate:
        raise RuntimeError(f"missing conjugate cache for exponent {exponent}")
    t2, t11a = data[exponent]
    _, t11b = conjugate[exponent]
    print(f"N_{exponent}3 dimension={len(t2)}", flush=True)
    for a, b in ((0, 0), (1, 0), (0, 1), (1, 1), (1, 2), (2, 1), (3, 5)):
        rows = add_three(t2, t11a, t11b, a, b)
        best = None
        for k in range(3):
            result = trial(rows, 3570000 + 10000 * exponent + 100 * a + 10 * b + k)
            if best is None or len(result[0]) > len(best[0]):
                best = result
        poly, roots, residual = best
        hist = {r: roots.count(r) for r in sorted(set(roots))}
        print(
            f"A=T2+{a}*T11a+{b}*T11b: BM degree={len(poly)-1}, "
            f"linear roots={hist}, residual degree={len(residual)-1}",
            flush=True,
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("exponent", type=int, choices=(2, 3))
    args = parser.parse_args()
    main(args.exponent)