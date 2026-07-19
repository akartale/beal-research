#!/usr/bin/env python3
"""Corrected local order/valuation explorer for A^x + B^y = C^z.

An auxiliary prime q is not required to divide A^x+B^y. Therefore conditional
valuation patterns are descriptive only unless an external theorem or
factorization makes q a mandatory divisor.
"""
from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, List, Optional


@dataclass(frozen=True)
class Observation:
    q: int
    tested_coprime_pairs: int
    divisible_pairs: int
    unit_divisible_pairs: int
    valuation_histogram: Dict[int, int]
    order_histogram: Dict[int, int]
    conditional_bad_fraction: float
    globally_valid_obstruction: bool
    reason: str


def primes_up_to(n: int) -> List[int]:
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b"\x00" * (((n - p*p)) // p + 1)
    return [i for i, f in enumerate(sieve) if f]


def vp(n: int, p: int, cap: int) -> int:
    if n == 0:
        return cap
    v = 0
    while v < cap and n % p == 0:
        n //= p
        v += 1
    return v


def factor_distinct(n: int) -> List[int]:
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def order_mod(a: int, q: int) -> Optional[int]:
    a %= q
    if a == 0:
        return None
    d = q - 1
    for r in factor_distinct(q - 1):
        while d % r == 0 and pow(a, d // r, q) == 1:
            d //= r
    return d


def observe(x: int, y: int, z: int, q: int, bound: int, cap: int) -> Observation:
    mod = q ** cap
    vh = Counter()
    oh = Counter()
    tested = divisible = unit_divisible = bad = 0
    for A in range(1, bound + 1):
        for B in range(1, bound + 1):
            if math.gcd(A, B) != 1:
                continue
            tested += 1
            residue = (pow(A, x, mod) + pow(B, y, mod)) % mod
            if residue % q:
                continue
            divisible += 1
            v = vp(residue, q, cap)
            vh[v] += 1
            if v % z != 0:
                bad += 1
            if A % q and B % q:
                unit_divisible += 1
                ratio = A * pow(B, -1, q) % q
                order = order_mod(ratio, q)
                if order is not None:
                    oh[order] += 1
    return Observation(
        q=q,
        tested_coprime_pairs=tested,
        divisible_pairs=divisible,
        unit_divisible_pairs=unit_divisible,
        valuation_histogram=dict(sorted(vh.items())),
        order_histogram=dict(sorted(oh.items())),
        conditional_bad_fraction=(bad / divisible if divisible else 0.0),
        globally_valid_obstruction=False,
        reason=("q is optional. This observation becomes useful only after a "
                "factorization or primitive-divisor theorem makes q mandatory."),
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--signature", nargs=3, type=int, required=True)
    ap.add_argument("--prime-bound", type=int, default=31)
    ap.add_argument("--search-bound", type=int, default=180)
    ap.add_argument("--valuation-cap", type=int, default=8)
    ap.add_argument("--output", default="-")
    ns = ap.parse_args()
    x, y, z = ns.signature
    observations = [observe(x, y, z, q, ns.search_bound, ns.valuation_cap)
                    for q in primes_up_to(ns.prime_bound) if q > 2]
    report = {
        "signature": [x, y, z],
        "status": "descriptive_only",
        "valid_global_obstructions_found": 0,
        "observations": [asdict(o) for o in observations],
        "structural_conclusion": (
            "Independent local congruence mining cannot by itself prove the "
            "signature impossible. A next-stage engine must supply mandatory "
            "prime divisors from cyclotomic factorization, Zsigmondy-type "
            "theorems, or a Frey/modular construction."
        ),
    }
    text = json.dumps(report, indent=2)
    if ns.output == "-":
        print(text)
    else:
        Path(ns.output).write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()