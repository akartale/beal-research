#!/usr/bin/env python3
"""Beal / generalized Fermat local conjecture miner.

Searches for reusable local statements for
    A^x + B^y = C^z
modulo prime powers p^k.

The tool does NOT prove Beal's conjecture. Its purpose is to discover exact,
finite, machine-checkable candidate lemmas such as:
  * no primitive solution exists modulo p^k;
  * every primitive solution forces a divisibility pattern;
  * a mod-p solution fails to lift to mod-p^k;
  * only specific p-adic valuation triples survive.

The output is JSON so candidate lemmas can be independently verified.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from itertools import product
from typing import Dict, List, Sequence, Set, Tuple


@dataclass(frozen=True)
class ModulusResult:
    p: int
    k: int
    modulus: int
    primitive_solution_count: int
    total_solution_count: int
    valuation_patterns: Tuple[Tuple[int, int, int], ...]
    forced_divisibility: Tuple[str, ...]
    lift_survival_ratio: float | None


def primes_up_to(n: int) -> List[int]:
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for q in range(2, int(n ** 0.5) + 1):
        if sieve[q]:
            sieve[q*q:n+1:q] = b"\x00" * (((n - q*q) // q) + 1)
    return [i for i, flag in enumerate(sieve) if flag]


def vp_mod(a: int, p: int, k: int) -> int:
    if a == 0:
        return k
    v = 0
    while v < k and a % p == 0:
        a //= p
        v += 1
    return v


def power_image(exp: int, modulus: int) -> Dict[int, Tuple[int, ...]]:
    out: Dict[int, List[int]] = {}
    for a in range(modulus):
        out.setdefault(pow(a, exp, modulus), []).append(a)
    return {r: tuple(vals) for r, vals in out.items()}


def primitive_triplet(a: int, b: int, c: int, p: int) -> bool:
    return not (a % p == 0 and b % p == 0 and c % p == 0)


def analyze_modulus(x: int, y: int, z: int, p: int, k: int,
                    previous_primitive_count: int | None = None) -> ModulusResult:
    modulus = p ** k
    ax = power_image(x, modulus)
    by = power_image(y, modulus)
    cz = power_image(z, modulus)
    primitive_count = 0
    total_count = 0
    patterns: Set[Tuple[int, int, int]] = set()
    possible_nondivisible = {"A": False, "B": False, "C": False}

    for aval, a_bases in ax.items():
        for bval, b_bases in by.items():
            cval = (aval + bval) % modulus
            c_bases = cz.get(cval)
            if not c_bases:
                continue
            total_count += len(a_bases) * len(b_bases) * len(c_bases)
            for a, b, c in product(a_bases, b_bases, c_bases):
                if not primitive_triplet(a, b, c, p):
                    continue
                primitive_count += 1
                va, vb, vc = vp_mod(a, p, k), vp_mod(b, p, k), vp_mod(c, p, k)
                patterns.add((va, vb, vc))
                if va == 0: possible_nondivisible["A"] = True
                if vb == 0: possible_nondivisible["B"] = True
                if vc == 0: possible_nondivisible["C"] = True

    forced = tuple(name for name, can_be_unit in possible_nondivisible.items()
                   if primitive_count > 0 and not can_be_unit)
    lift_ratio = None
    if previous_primitive_count is not None and previous_primitive_count > 0:
        lift_ratio = primitive_count / (previous_primitive_count * (p ** 3))

    return ModulusResult(p, k, modulus, primitive_count, total_count,
                         tuple(sorted(patterns)), forced, lift_ratio)


def analyze_prime_tower(x: int, y: int, z: int, p: int, max_k: int) -> List[ModulusResult]:
    results = []
    previous = None
    for k in range(1, max_k + 1):
        current = analyze_modulus(x, y, z, p, k, previous)
        results.append(current)
        previous = current.primitive_solution_count
        if current.primitive_solution_count == 0:
            break
    return results


def candidate_lemmas(results: Sequence[ModulusResult]) -> List[Dict[str, object]]:
    lemmas = []
    for r in results:
        if r.primitive_solution_count == 0:
            lemmas.append({"type": "primitive_obstruction", "statement": f"No primitive residue solution exists modulo {r.modulus}.", "p": r.p, "k": r.k})
        if r.forced_divisibility:
            lemmas.append({"type": "forced_divisibility", "statement": f"Every primitive residue solution modulo {r.modulus} forces " + ", ".join(f"{r.p}|{v}" for v in r.forced_divisibility) + ".", "p": r.p, "k": r.k, "variables": list(r.forced_divisibility)})
        if r.lift_survival_ratio is not None and r.lift_survival_ratio < 0.05:
            lemmas.append({"type": "strong_lift_collapse", "statement": f"Only {r.lift_survival_ratio:.6%} of naive lifts survive from p^{r.k-1} to p^{r.k}.", "p": r.p, "k": r.k, "ratio": r.lift_survival_ratio})
    return lemmas


def analyze_signature(x: int, y: int, z: int, prime_bound: int, max_k: int, modulus_cap: int) -> Dict[str, object]:
    towers = {}
    all_results = []
    for p in primes_up_to(prime_bound):
        permitted_k = 0
        while p ** (permitted_k + 1) <= modulus_cap and permitted_k < max_k:
            permitted_k += 1
        if permitted_k == 0:
            continue
        tower = analyze_prime_tower(x, y, z, p, permitted_k)
        all_results.extend(tower)
        towers[str(p)] = [asdict(r) for r in tower]
    ranked = sorted(all_results, key=lambda r: (r.primitive_solution_count != 0, r.lift_survival_ratio if r.lift_survival_ratio is not None else 1.0, r.primitive_solution_count, r.modulus))[:30]
    return {"signature": [x, y, z], "prime_bound": prime_bound, "max_k": max_k, "modulus_cap": modulus_cap, "candidate_lemmas": candidate_lemmas(all_results), "ranked_filters": [asdict(r) for r in ranked], "prime_towers": towers}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--signature", nargs=3, type=int, required=True, metavar=("X", "Y", "Z"))
    parser.add_argument("--prime-bound", type=int, default=31)
    parser.add_argument("--max-k", type=int, default=3)
    parser.add_argument("--modulus-cap", type=int, default=5000)
    parser.add_argument("--output", default="-")
    args = parser.parse_args()
    report = analyze_signature(*args.signature, args.prime_bound, args.max_k, args.modulus_cap)
    text = json.dumps(report, indent=2)
    if args.output == "-": print(text)
    else:
        with open(args.output, "w", encoding="utf-8") as fh: fh.write(text + "\n")


if __name__ == "__main__":
    main()