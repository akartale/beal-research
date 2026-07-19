# Beal computational research lab

Target equation:

    A^x + B^y = C^z

Current focus: open generalized-Fermat core, especially signature (3,5,7).

## Scripts

- `scripts/beal_conjecture_miner_v2.py` — exact local search modulo prime powers p^k, valuation patterns, lift ratios.
- `scripts/beal_order_valuation_miner_v3_1.py` — corrected descriptive order/valuation explorer. It explicitly forbids treating optional auxiliary primes as global obstructions.
- `scripts/beal_invariant_miner_v4.py` — finite-field low-degree invariant search, subtracting obvious multiples of A^x+B^y-C^z.

## Established computational conclusions

1. For (3,5,7), ordinary one-prime congruence searches and p-adic lifting show no hidden local obstruction in tested ranges.
2. Conditional q-adic valuation patterns are not global contradictions unless q is made mandatory by a separate factorization/primitive-divisor theorem.
3. For degree <= 7, primes 13, 17, and 19 show no extra polynomial invariant beyond the defining equation itself.
4. Next serious direction: mandatory-prime/cyclotomic machinery or a multi-Frey trace sieve.

## Reproducible runs

```sh
python3 scripts/beal_conjecture_miner_v2.py --signature 3 5 7 --prime-bound 31 --max-k 3 --modulus-cap 5000 --output reports/beal_357_pk_report.json
python3 scripts/beal_order_valuation_miner_v3_1.py --signature 3 5 7 --prime-bound 31 --search-bound 180 --valuation-cap 8 --output reports/beal_357_order_valuation_report.json
python3 scripts/beal_invariant_miner_v4.py --signature 3 5 7 --degree 7 --prime-bound 19 --max-relations 6 --output reports/beal_357_invariant_report_degree7.json
```

The project is exploratory. Finite computations generate or reject candidate lemmas; they are not proofs unless accompanied by a separate symbolic argument.