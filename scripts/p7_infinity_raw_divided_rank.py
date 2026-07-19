#!/usr/bin/env python3
"""Inspect the raw divided lower-left block in PARI's even-degree basis.

This is an exploratory computation only.  hyperellpadicfrobenius returns a
5-dimensional even-degree Monsky--Washnitzer space for a genus-2 sextic, with
one extraneous line.  The script records the rank of rows 3..5, columns 1..2
after division by 7.  Turning this into a finite-Honda invariant requires an
explicit identification of the genus-2 quotient and its Hodge filtration.
"""

from __future__ import annotations

P = 7

MATRICES = {
    1: [[35,35,0,25,14],[0,42,7,0,20],[0,0,42,0,0],[28,0,0,14,21],[0,21,0,0,7]],
    2: [[21,21,0,32,28],[0,21,28,0,33],[0,0,42,0,0],[14,0,0,28,35],[0,21,0,0,28]],
    3: [[42,42,0,3,42],[0,35,14,0,4],[0,0,42,0,0],[42,0,0,7,42],[0,28,0,0,14]],
    4: [[42,42,0,39,7],[0,35,14,0,3],[0,0,42,0,0],[7,0,0,7,42],[0,21,0,0,14]],
    5: [[21,21,0,3,21],[0,21,28,0,23],[0,0,42,0,0],[35,0,0,28,35],[0,28,0,0,28]],
    6: [[35,35,0,45,35],[0,42,7,0,36],[0,0,42,0,0],[21,0,0,14,21],[0,28,0,0,7]],
}


def rank_mod_p(a: list[list[int]]) -> int:
    m = [[x % P for x in row] for row in a]
    rows, cols = len(m), len(m[0])
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if m[i][c]), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        inv = pow(m[r][c], -1, P)
        m[r] = [(x * inv) % P for x in m[r]]
        for i in range(rows):
            if i != r and m[i][c]:
                q = m[i][c]
                m[i] = [(x - q*y) % P for x, y in zip(m[i], m[r])]
        r += 1
    return r


def main() -> None:
    print("v raw_divided_block rank")
    for v, matrix in MATRICES.items():
        block = [[matrix[i][j] for j in range(2)] for i in range(2, 5)]
        if any(x % P for row in block for x in row):
            raise ValueError(f"v={v}: lower-left block not divisible by 7")
        divided = [[x // P % P for x in row] for row in block]
        print(v, divided, rank_mod_p(divided))


if __name__ == "__main__":
    main()