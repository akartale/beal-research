#!/usr/bin/env python3
"""Exact mod-7 Brandt test for the final quadratic character at level (2,2).

Build the full icosian orbit module for N=(3)^2*p5^2 and the two Hecke
operators above each of 11, 19, and 29.  Test the simultaneous eigensystem
attached to chi=(90,0):

    T_11a=T_11b=2,
    T_19a=T_19b=1,
    T_29a=T_29b=2  (mod 7).

A full-column-rank stacked matrix excludes this eigensystem over every finite
extension of F_7, without any characteristic-zero lifting assumption.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from hecke_t11_mod7 import global_orbit_data, global_hecke_from_data, hecke_representatives_11, sparse_product
from hecke_t11_conjugate_mod7 import hecke_representatives_11_conjugate
from hecke_t19_pair_mod7 import representatives as representatives_19
from hecke_t29_pair_mod7 import representatives as representatives_29
from ok_sqrt5 import A

P = 7
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data/p7_900_brandt_level22_certificate.json"


def rank_mod7(rows: list[list[int]]) -> int:
    if not rows:
        return 0
    a = [[x % P for x in row] for row in rows]
    m, n = len(a), len(a[0])
    rank = 0
    for col in range(n):
        pivot = next((r for r in range(rank, m) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, P)
        a[rank] = [(x * inv) % P for x in a[rank]]
        for r in range(m):
            factor = a[r][col]
            if r != rank and factor:
                a[r] = [(x - factor * y) % P for x, y in zip(a[r], a[rank])]
        rank += 1
        if rank == n:
            return rank
    return rank


def shifted_dense(rows: list[dict[int, int]], eigenvalue: int) -> list[list[int]]:
    n = len(rows)
    out = [[0] * n for _ in range(n)]
    for i, row in enumerate(rows):
        for j, value in row.items():
            out[i][j] = value % P
        out[i][i] = (out[i][i] - eigenvalue) % P
    return out


def digest_sparse(rows: list[dict[int, int]]) -> str:
    h = hashlib.sha256()
    for i, row in enumerate(rows):
        for j, value in sorted(row.items()):
            h.update(f"{i},{j},{value % P};".encode())
    return h.hexdigest()


def main() -> None:
    exponent_at_3 = 2
    exponent_at_5 = 2
    data = global_orbit_data(exponent_at_3, exponent_at_5)

    reps11a = hecke_representatives_11()
    reps11b = hecke_representatives_11_conjugate()
    reps19a = representatives_19(4 + A)
    reps19b = representatives_19(5 - A)
    reps29a = representatives_29(5 + A)
    reps29b = representatives_29(6 - A)

    operators = []
    for name, reps, target in (
        ("T11a", reps11a, 2),
        ("T11b", reps11b, 2),
        ("T19a", reps19a, 1),
        ("T19b", reps19b, 1),
        ("T29a", reps29a, 2),
        ("T29b", reps29b, 2),
    ):
        orbit_reps, rows = global_hecke_from_data(data, reps)
        operators.append((name, target, orbit_reps, rows))
        expected_degree = {"T11a": 12, "T11b": 12, "T19a": 20, "T19b": 20, "T29a": 30, "T29b": 30}[name]
        assert all(sum(row.values()) % P == expected_degree % P for row in rows)
        print(name, "dimension", len(rows), "nnz", sum(map(len, rows)), "target", target, flush=True)

    base_reps = operators[0][2]
    assert all(op[2] == base_reps for op in operators)
    for i in range(len(operators)):
        for j in range(i + 1, len(operators)):
            assert sparse_product(operators[i][3], operators[j][3]) == sparse_product(operators[j][3], operators[i][3])

    n = len(base_reps)
    stacked: list[list[int]] = []
    chain = []
    for name, target, _, rows in operators:
        stacked.extend(shifted_dense(rows, target))
        rank = rank_mod7(stacked)
        dim = n - rank
        chain.append({"after": name, "rank": rank, "dimension": dim})
        print("after", name, "rank", rank, "dimension", dim, flush=True)

    result = {
        "level": "(3)^2*(sqrt(5))^2",
        "exponents": [2, 2],
        "dimension": n,
        "targets": {name: target for name, target, _, _ in operators},
        "rank_chain": chain,
        "survivors_dimension": chain[-1]["dimension"],
        "operator_nnz": {name: sum(map(len, rows)) for name, _, _, rows in operators},
        "operator_sha256": {name: digest_sparse(rows) for name, _, _, rows in operators},
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "all_pairwise_commute": True,
        "row_sum_checks": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("survivors_dimension", result["survivors_dimension"], flush=True)
    print("certificate", OUT, flush=True)
    if result["survivors_dimension"] != 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()