#!/usr/bin/env python3
"""Exact sparse mod-7 joint eigenspace filter for level (3,3).

Uses the unique attainable Frey trace pairs (2,2) at 11 and (5,5) at 19.
All caches are loaded from the canonical research/beal/data directory.
"""
from __future__ import annotations

import pickle
from typing import Dict, Iterable

from paths import DATA_DIR

P = 7
EXPONENT = 3

SparseRow = Dict[int, int]


def shifted_rows(rows: list[dict[int, int]], eigenvalue: int) -> Iterable[SparseRow]:
    for i, source in enumerate(rows):
        row = {j: value % P for j, value in source.items() if value % P}
        row[i] = (row.get(i, 0) - eigenvalue) % P
        if row[i] == 0:
            row.pop(i, None)
        yield row


def sparse_rank(row_groups: Iterable[Iterable[SparseRow]], ncols: int) -> int:
    """Row rank over F_7 using normalized sparse pivot rows."""
    pivots: dict[int, SparseRow] = {}
    inverses = {a: pow(a, -1, P) for a in range(1, P)}

    for rows in row_groups:
        for raw in rows:
            row = dict(raw)
            while row:
                pivot_col = min(row)
                coeff = row[pivot_col]
                pivot = pivots.get(pivot_col)
                if pivot is None:
                    inv = inverses[coeff]
                    normalized = {
                        col: (value * inv) % P
                        for col, value in row.items()
                        if (value * inv) % P
                    }
                    pivots[pivot_col] = normalized
                    break

                for col, value in pivot.items():
                    new_value = (row.get(col, 0) - coeff * value) % P
                    if new_value:
                        row[col] = new_value
                    else:
                        row.pop(col, None)

            if len(pivots) == ncols:
                return ncols

    return len(pivots)


def main() -> None:
    with (DATA_DIR / "hecke_mod7_cache.pkl").open("rb") as handle:
        primary11 = pickle.load(handle)
    with (DATA_DIR / "hecke_t11_conjugate_mod7.pkl").open("rb") as handle:
        conjugate11 = pickle.load(handle)
    with (DATA_DIR / "hecke_t19_pair_mod7.pkl").open("rb") as handle:
        pair19 = pickle.load(handle)

    _, t11a = primary11[EXPONENT]
    reps11b, t11b = conjugate11[EXPONENT]
    reps19a, t19a, reps19b, t19b = pair19[EXPONENT]

    if not (reps11b == reps19a == reps19b):
        raise ArithmeticError("incompatible orbit orderings in saved Hecke caches")

    n = len(t11a)
    if not all(len(rows) == n for rows in (t11b, t19a, t19b)):
        raise ArithmeticError("incompatible Hecke matrix dimensions")
    print("all Hecke caches use the common certified orbit ordering")
    rank11 = sparse_rank(
        (shifted_rows(t11a, 2), shifted_rows(t11b, 2)), n
    )
    dim11 = n - rank11
    print(f"ambient dimension={n}")
    print(f"after T11 pair (2,2): rank={rank11}, dimension={dim11}")

    rank1119 = sparse_rank(
        (
            shifted_rows(t11a, 2),
            shifted_rows(t11b, 2),
            shifted_rows(t19a, 5),
            shifted_rows(t19b, 5),
        ),
        n,
    )
    dim1119 = n - rank1119
    print(f"after T11=(2,2), T19=(5,5): rank={rank1119}, dimension={dim1119}")
    print(f"level-(3,3) eliminated={dim1119 == 0}")

    if dim1119 != 0:
        raise SystemExit(2)


if __name__ == "__main__":
    main()