#!/usr/bin/env python3
from __future__ import annotations

import pickle
import struct

from paths import DATA_DIR

P = 7
EXPONENT = 3
TRACE_PAIRS = ((1, 1), (2, 2), (5, 5), (6, 6))
OUT = DATA_DIR / "level33_t11_t19_t29_dense.bin"


def dense_rows(rows: list[dict[int, int]], eigenvalue: int) -> bytes:
    n = len(rows)
    out = bytearray(n * n)
    for i, row in enumerate(rows):
        base = i * n
        for j, value in row.items():
            out[base + j] = value % P
        out[base + i] = (out[base + i] - eigenvalue) % P
    return bytes(out)


def main() -> None:
    with (DATA_DIR / "hecke_mod7_cache.pkl").open("rb") as handle:
        primary11 = pickle.load(handle)
    with (DATA_DIR / "hecke_t11_conjugate_mod7.pkl").open("rb") as handle:
        conjugate11 = pickle.load(handle)
    with (DATA_DIR / "hecke_t19_pair_mod7.pkl").open("rb") as handle:
        pair19 = pickle.load(handle)
    with (DATA_DIR / "hecke_t29_pair_mod7.pkl").open("rb") as handle:
        pair29 = pickle.load(handle)

    _, t11a = primary11[EXPONENT]
    reps11b, t11b = conjugate11[EXPONENT]
    reps19a, t19a, reps19b, t19b = pair19[EXPONENT]
    reps29a, t29a, reps29b, t29b = pair29[EXPONENT]
    if not (reps11b == reps19a == reps19b == reps29a == reps29b):
        raise ArithmeticError("incompatible certified orbit orderings")

    n = len(t11a)
    if not all(len(rows) == n for rows in (t11b, t19a, t19b, t29a, t29b)):
        raise ArithmeticError("incompatible matrix dimensions")

    blocks = [
        dense_rows(t11a, 2),
        dense_rows(t11b, 2),
        dense_rows(t19a, 5),
        dense_rows(t19b, 5),
    ]
    for a, b in TRACE_PAIRS:
        blocks.append(dense_rows(t29a, a))
        blocks.append(dense_rows(t29b, b))

    with OUT.open("wb") as handle:
        handle.write(struct.pack("<II", n, len(blocks)))
        for block in blocks:
            handle.write(block)
    print(
        f"wrote {OUT} n={n} blocks={len(blocks)} "
        f"trace_pairs={TRACE_PAIRS} bytes={OUT.stat().st_size}"
    )


if __name__ == "__main__":
    main()