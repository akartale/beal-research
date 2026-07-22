#!/usr/bin/env python3
"""Fast exact cached Brandt certificate for the final character (90,0)."""
from __future__ import annotations

import hashlib
import json
import pickle
from pathlib import Path

from paths import DATA_DIR
from filter_level33_t11_t19_sparse import shifted_rows, sparse_rank
from hecke_t11_mod7 import sparse_product

P = 7
EXPONENT = 2
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data/p7_900_brandt_level22_cached_certificate.json"


def digest_sparse(rows: list[dict[int, int]]) -> str:
    h = hashlib.sha256()
    for i, row in enumerate(rows):
        for j, value in sorted(row.items()):
            h.update(f"{i},{j},{value % P};".encode())
    return h.hexdigest()


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

    operators = [
        ("T11a", t11a, 2, 12),
        ("T11b", t11b, 2, 12),
        ("T19a", t19a, 1, 20),
        ("T19b", t19b, 1, 20),
        ("T29a", t29a, 2, 30),
        ("T29b", t29b, 2, 30),
    ]
    n = len(t11a)
    if not all(len(rows) == n for _, rows, _, _ in operators):
        raise ArithmeticError("incompatible matrix dimensions")
    for name, rows, _, degree in operators:
        if not all(sum(row.values()) % P == degree % P for row in rows):
            raise ArithmeticError(f"row-sum check failed for {name}")

    for i in range(len(operators)):
        for j in range(i + 1, len(operators)):
            left = sparse_product(operators[i][1], operators[j][1])
            right = sparse_product(operators[j][1], operators[i][1])
            if left != right:
                raise ArithmeticError(f"noncommuting operators {operators[i][0]}, {operators[j][0]}")

    row_groups = []
    chain = []
    for name, rows, target, _ in operators:
        row_groups.append(tuple(shifted_rows(rows, target)))
        rank = sparse_rank(tuple(row_groups), n)
        dim = n - rank
        chain.append({"after": name, "rank": rank, "dimension": dim})
        print(f"after {name}: rank={rank}, dimension={dim}", flush=True)

    result = {
        "level": "(3)^2*(sqrt(5))^2",
        "exponent": EXPONENT,
        "dimension": n,
        "targets": {name: target for name, _, target, _ in operators},
        "rank_chain": chain,
        "survivors_dimension": chain[-1]["dimension"],
        "operator_nnz": {name: sum(map(len, rows)) for name, rows, _, _ in operators},
        "operator_sha256": {name: digest_sparse(rows) for name, rows, _, _ in operators},
        "all_pairwise_commute": True,
        "row_sum_checks": True,
        "source_caches": [
            "hecke_mod7_cache.pkl",
            "hecke_t11_conjugate_mod7.pkl",
            "hecke_t19_pair_mod7.pkl",
            "hecke_t29_pair_mod7.pkl",
        ],
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("certificate", OUT, flush=True)
    print("survivors_dimension", result["survivors_dimension"], flush=True)
    if result["survivors_dimension"] != 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()