# Fresh logical re-audit of Lemmas A, B, C, and D

## Scope

This document records a new dependency audit of the residual irreducibility argument at `p=7`. It supersedes any wording that treated the paired good-reduction sieve at `l=19` as the complete Lemma D.

## Lemma A — finite-flat inertia types

### Closed points

- `7` is inert in `F=Q(sqrt(5))`, so the local ramification index is `e=1` and the residue field has order `49`.
- Raynaud, Corollary 3.4.4, applies directly to a Jordan--Hoelder quotient of the generic finite group scheme whenever the generic group scheme admits a finite-flat prolongation.
- Therefore no separate descent or finite-flat lifting of a chosen `Fbar_7`-stable line is required.
- Each simple factor is one-dimensional over a suitable finite endomorphism field, with Raynaud digits in `{0,1}`.
- Frobenius invariance over residue cardinality `49` forces period two, yielding tame exponents `0,1,7,8` and inertia multisets `{0,8}` or `{1,7}`.

### Source dependency now checked

The source Theorem 2.1(4) states uniformly for the plus motive that its residual representation is finite at every prime dividing `p`. For `p=7` this covers every specialization and every primitive branch. Thus the source finite-flat dependency is closed.

## Lemma B — conductor bounds

### Closed points

- Semisimplification cannot increase the Artin conductor, by the lower-ramification invariant-dimension argument.
- Hence a source exponent at most `3` gives `a_q(chi_i)<=3` for each diagonal character.
- The local `p7` contribution is correctly bounded by exponent `0` in the chosen ordinary constituent and by exponent `1` in the niveau-two branch.

### Branch table now checked

`PRIMITIVE_VALUATION_CONDUCTOR_TABLE.md` transcribes Theorem 7.8 under

```text
(a,b,c)=(B,-C,A)
```

and gives an exhaustive decision rule for `epsilon_3,epsilon_5 in {2,3}`. Hence the branchwise conductor upper bound needed for the ray-character modulus is closed.

## Lemma C — ordinary ray characters

### Closed points

- The exact ray class group is `Z/180 x Z/2`.
- Since its order `360` is prime to `7`, there are exactly `360` algebraic-closure-valued characters.
- `F_(7^12)` is only a common realization field.
- Both primes above `19` have independently verified ray coordinates `[141,1]`.

Lemma C is complete conditional on Lemma B's conductor modulus.

## Lemma D — ordinary branch elimination

### Closed computational points

- The paired `l=19` computation eliminates all `360` characters in the generic good-reduction branch `19 does not divide ABC`.
- The full four-branch auxiliary-prime sieve includes `t=0`, `t=1`, and `t=infinity` and leaves exactly

```text
(0,0), (0,1), (90,0), (90,1).
```

- These four characters are quadratic, explaining why the same auxiliary-prime congruence cannot remove them.

### Corrected theorem-level status

The exact tangent-branch computation in `scripts/p7_t1_branch_splitting.py` shows that the two nodes are rational over `F_49` but their branches are not. The toric splitting character is the nontrivial unramified quadratic character. Consequently the local condition at `7` eliminates `(0,0)` and retains `(0,1)`, `(90,0)`, and `(90,1)`.

The exact local conductor comparison in `P7_QUADRATIC_SURVIVOR_LOCAL_CONDUCTOR.md` then eliminates `(0,1)` at the prime above `3` and `(90,1)` at the prime above `5`. The sole remaining character is `(90,0)`, ramified quadratically at both primes, and it forces the conductor pair `(2,2)`.

## Exact current conclusion

- Lemma A: closed, including the uniform source finite-at-`7` input.
- Lemma B: closed by the exhaustive translated source conductor table.
- Lemma C: closed.
- Lemma D: the four-branch sieve, corrected toric condition, and local conductor reductions leave exactly one quadratic character `(90,0)`. The full mod-`7` Brandt module at level `(2,2)` has no matching eigensystem; see `P7_900_LEVEL22_BRANDT_CERTIFICATE.md`. However, Theorem 7.8 assumes irreducibility before placing the representation at that lowered level, so this computation cannot be used noncircularly to prove irreducibility. The remaining gap is a direct Eisenstein/Selmer obstruction, or another reducible-compatible level theorem.

The attempted direct certificate in `data/p7_900_direct_local_certificate.json` does not change this status: it checks only the generic, `t=0`, and `t=infinity` upstream data sets. The separate `t=1` branch is omitted, and every quadratic character automatically satisfies its Steinberg/toric trace congruence. See `P7_900_DIRECT_LOCAL_CERTIFICATE_AUDIT.md`.

Therefore theorem-level absolute irreducibility at `p=7` is not yet claimed.