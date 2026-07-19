#!/usr/bin/env python3
"""Exact power-residue diagnostics for the two special p=7 disks.

For A^3+B^5=C^7, the special branches are:
  * 7 | A, with B,C units: compare fifth and seventh powers;
  * 7 | B, with A,C units: compare third and seventh powers.

The script does not claim a contradiction.  It measures the exact residue
intersections modulo 7^k and records whether a pure power-residue obstruction
can exist at the tested precision.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class Row:
    k: int
    modulus: int
    unit_count: int
    seventh_power_count: int
    cube_count: int
    fifth_power_count: int
    branch_7_divides_A_intersection: int
    branch_7_divides_B_intersection: int


def unit_power_set(modulus: int, exponent: int) -> set[int]:
    return {pow(x, exponent, modulus) for x in range(1, modulus) if x % 7}


def compute(max_k: int) -> list[Row]:
    rows: list[Row] = []
    for k in range(1, max_k + 1):
        modulus = 7**k
        seventh = unit_power_set(modulus, 7)
        cubes = unit_power_set(modulus, 3)
        fifths = unit_power_set(modulus, 5)
        rows.append(
            Row(
                k=k,
                modulus=modulus,
                unit_count=6 * 7 ** (k - 1),
                seventh_power_count=len(seventh),
                cube_count=len(cubes),
                fifth_power_count=len(fifths),
                branch_7_divides_A_intersection=len(seventh & fifths),
                branch_7_divides_B_intersection=len(seventh & cubes),
            )
        )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-k", type=int, default=4)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.max_k < 1:
        raise SystemExit("--max-k must be positive")

    rows = compute(args.max_k)
    if args.json:
        print(json.dumps([asdict(row) for row in rows], indent=2))
        return

    print("k modulus units seventh cubes fifths A7_intersection B7_intersection")
    for row in rows:
        print(
            row.k,
            row.modulus,
            row.unit_count,
            row.seventh_power_count,
            row.cube_count,
            row.fifth_power_count,
            row.branch_7_divides_A_intersection,
            row.branch_7_divides_B_intersection,
        )

    if all(row.branch_7_divides_A_intersection for row in rows):
        print("NO_PURE_POWER_RESIDUE_OBSTRUCTION_IN_7_DIVIDES_A_BRANCH")
    if all(row.branch_7_divides_B_intersection for row in rows):
        print("NO_PURE_POWER_RESIDUE_OBSTRUCTION_IN_7_DIVIDES_B_BRANCH")


if __name__ == "__main__":
    main()