#!/usr/bin/env python3
"""Black-box finite-field analysis of sparse commuting Hecke operators.

Uses scalar Wiedemann sequences and Berlekamp--Massey over F_7.  This avoids
materializing dense 2026 x 2026 matrices and requires only sparse row-vector
multiplication.  Random linear combinations T2+c*T11 expose joint Hecke
constituents; repeated trials provide a lower bound, and typically the exact
minimal-polynomial degree.
"""
from __future__ import annotations

import pickle
from pathlib import Path

from paths import DATA_DIR
from random import Random

from hecke_t2_mod7 import global_orbit_and_t2
from hecke_t11_mod7 import global_orbit_and_hecke, hecke_representatives_11

P = 7
CACHE = DATA_DIR / "hecke_mod7_cache.pkl"


def sparse_linear_combination(a, b, scalar):
    rows = []
    for ra, rb in zip(a, b):
        row = dict(ra)
        for j, value in rb.items():
            row[j] = (row.get(j, 0) + scalar * value) % P
            if row[j] == 0:
                del row[j]
        rows.append(row)
    return rows


def row_matvec(vector: list[int], rows: list[dict[int, int]]) -> list[int]:
    out = [0] * len(vector)
    for i, value in enumerate(vector):
        if value:
            for j, coefficient in rows[i].items():
                out[j] = (out[j] + value * coefficient) % P
    return out


def dot(left: list[int], right: list[int]) -> int:
    return sum(a * b for a, b in zip(left, right)) % P


def berlekamp_massey(sequence: list[int]) -> list[int]:
    """Return monic recurrence polynomial C, low degree first."""
    c = [1]
    b = [1]
    length = 0
    shift = 1
    discrepancy_scale = 1
    for n in range(len(sequence)):
        discrepancy = sequence[n]
        for i in range(1, length + 1):
            discrepancy = (discrepancy + c[i] * sequence[n - i]) % P
        if discrepancy == 0:
            shift += 1
            continue
        old = c[:]
        factor = discrepancy * pow(discrepancy_scale, -1, P) % P
        needed = len(b) + shift
        if len(c) < needed:
            c.extend([0] * (needed - len(c)))
        for j, value in enumerate(b):
            c[j + shift] = (c[j + shift] - factor * value) % P
        if 2 * length <= n:
            length = n + 1 - length
            b = old
            discrepancy_scale = discrepancy
            shift = 1
        else:
            shift += 1
    c = c[: length + 1]
    # BM gives 1+c1*x+...+cL*x^L. Reverse to conventional low-first monic.
    return list(reversed(c))


def polynomial_eval(poly: list[int], x: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % P
    return value


def strip_linear_factors(poly: list[int]):
    work = poly[:]
    factors = []
    for root in range(P):
        while len(work) > 1 and polynomial_eval(work, root) == 0:
            quotient = [0] * (len(work) - 1)
            carry = work[-1]
            quotient[-1] = carry
            for index in range(len(work) - 2, 0, -1):
                carry = (work[index] + root * carry) % P
                quotient[index - 1] = carry
            remainder = (work[0] + root * carry) % P
            assert remainder == 0
            factors.append(root)
            work = quotient
    return factors, work


def build_or_load():
    if CACHE.exists():
        with CACHE.open("rb") as handle:
            return pickle.load(handle)
    hecke11 = hecke_representatives_11()
    data = {}
    for exponent in (2, 3):
        reps2, t2 = global_orbit_and_t2(exponent)
        reps11, t11 = global_orbit_and_hecke(exponent, hecke11)
        assert reps2 == reps11
        data[exponent] = (t2, t11)
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    with CACHE.open("wb") as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
    return data


def trial(rows, seed: int):
    rng = Random(seed)
    n = len(rows)
    left = [rng.randrange(P) for _ in range(n)]
    state = [rng.randrange(P) for _ in range(n)]
    sequence = []
    for _ in range(2 * n + 32):
        sequence.append(dot(left, state))
        state = row_matvec(state, rows)
    poly = berlekamp_massey(sequence)
    roots, residual = strip_linear_factors(poly)
    return poly, roots, residual


def self_test():
    # Fibonacci recurrence s_n=s_(n-1)+s_(n-2): x^2-x-1.
    seq = [0, 1]
    for _ in range(30):
        seq.append((seq[-1] + seq[-2]) % P)
    assert berlekamp_massey(seq) == [P - 1, P - 1, 1]

    data = build_or_load()
    for exponent in (2, 3):
        t2, t11 = data[exponent]
        print(f"N_{exponent}3 dimension={len(t2)}", flush=True)
        for scalar in (0, 1, 2):
            rows = sparse_linear_combination(t2, t11, scalar)
            best = None
            for trial_index in range(2):
                poly, roots, residual = trial(rows, 357000 + 100 * exponent + 10 * scalar + trial_index)
                if best is None or len(poly) > len(best[0]):
                    best = (poly, roots, residual)
            poly, roots, residual = best
            histogram = {r: roots.count(r) for r in sorted(set(roots))}
            print(
                f"  A=T2+{scalar}*T11: BM degree={len(poly)-1}, "
                f"linear roots={histogram}, residual degree={len(residual)-1}",
                flush=True,
            )


if __name__ == "__main__":
    self_test()