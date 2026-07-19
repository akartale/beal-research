#!/usr/bin/env python3
"""Certify the divided-Frobenius rank separating CM h/l from Frey t=0.

Matrices are the precision-7^2 outputs of PARI/GP hyperellpadicfrobenius in the
basis dx/(2y), x dx/(2y), x^2 dx/(2y), x^3 dx/(2y).  The Hodge filtration
Fil^1 is spanned by the first two basis vectors.  Since Frobenius sends Fil^1
into 7D, the lower-left 2x2 block divided by 7 and reduced modulo 7 defines

    Fil^1 mod 7 -> (D/Fil^1) mod 7.

Its rank is invariant under filtration-preserving integral changes of basis.
"""

from __future__ import annotations

P = 7

MATRICES = {
    "CM_x5_minus_1": [
        [0, 0, 37, 0],
        [35, 0, 0, 0],
        [0, 0, 0, 22],
        [0, 14, 0, 0],
    ],
    "Frey_u1": [[0, 0, 41, 14], [42, 0, 0, 0], [42, 0, 0, 2], [0, 21, 21, 0]],
    "Frey_u2": [[0, 0, 38, 7], [21, 0, 0, 0], [42, 0, 0, 18], [0, 42, 42, 0]],
    "Frey_u3": [[0, 0, 33, 21], [35, 0, 0, 0], [7, 0, 0, 29], [0, 35, 14, 0]],
    "Frey_u4": [[0, 0, 40, 28], [35, 0, 0, 0], [42, 0, 0, 15], [0, 35, 35, 0]],
    "Frey_u5": [[0, 0, 10, 42], [21, 0, 0, 0], [7, 0, 0, 32], [0, 42, 7, 0]],
    "Frey_u6": [[0, 0, 27, 35], [42, 0, 0, 0], [7, 0, 0, 16], [0, 21, 28, 0]],
}


def rank2(matrix: list[list[int]]) -> int:
    det = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % P
    if det:
        return 2
    return 1 if any(entry % P for row in matrix for entry in row) else 0


def divided_block(matrix: list[list[int]]) -> list[list[int]]:
    block = [[matrix[i][j] for j in range(2)] for i in range(2, 4)]
    if any(entry % P for row in block for entry in row):
        raise ValueError("Frobenius does not map Fil^1 into 7D")
    return [[entry // P % P for entry in row] for row in block]


def main() -> None:
    print("label divided_Fil_to_quotient rank")
    for label, matrix in MATRICES.items():
        block = divided_block(matrix)
        print(label, block, rank2(block))


if __name__ == "__main__":
    main()