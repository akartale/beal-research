# Logical proof audit: signature `(3,5,7)`

_Last audited: 2026-07-21_

## Scope

This audit checks the logical structure of the written proof package without rerunning the large arithmetic computations. It checks dependency direction, sufficiency of stated hypotheses, circularity, claim boundaries, and consistency among canonical documents. It is not an independent re-computation of Brandt matrices, ray class groups, traces, or ranks.

## Canonical dependency graph

```text
Primitive solution and source Frey construction
        |
        v
Source finite-flatness and branchwise conductor table
        |
        +--------------------+
        |                    |
        v                    v
Lemma A                  Lemma B
finite-flat inertia      conductor support/bounds
        |                    |
        +---------+----------+
                  |
                  v
        Niveau-two branch elimination
        by the ray-class exact sequence
                  |
                  v
Lemma C: exhaustive ordinary ray-character enumeration
                  |
                  v
Lemma D reductions:
  four-branch auxiliary-prime sieve
        -> four quadratic characters
  corrected toric splitting at 7
        -> three characters
  branchwise conductor contradictions
        -> sole survivor (90,0)
                  |
                  v
OPEN: noncircular elimination of (90,0)
                  |
                  v
Absolute irreducibility at p=7
                  |
                  v
Source level lowering / candidate levels
                  |
                  v
JL/Brandt theorem bridge + exact computational certificates
                  |
                  v
Final nonexistence theorem
```

## Lemma A audit

### Inputs

- The source residual representation is finite-flat at the unique prime above `7`.
- `7` is inert in `Q(sqrt(5))`, so the local absolute ramification index is `e=1` and the residue cardinality is `49`.
- Raynaud Corollaire 3.4.4 applies to generic-fibre Jordan--Hoelder factors of a finite-flat prolongation.

### Output

The only possible tame inertia exponent multisets are

```text
{0,8}  and  {1,7}.
```

### Logical check

The argument does not require an absolutely reducible line to descend to `F_49`. The Jordan--Hoelder passage is supplied by the cited finite-flat result, and Frobenius conjugacy forces period two in the Raynaud digits. No later lemma is used. There is no circular dependence.

### Status

**Closed in the current written audit**, conditional only on the source finite-flat statement that has been checked and recorded in the source-integration documents.

## Lemma B audit

### Inputs

- Source ramification and conductor exponents, translated branchwise under `(a,b,c)=(B,-C,A)`.
- Additivity of the Artin conductor on semisimplification and the proved inequality
  `a(rho_bar^ss) <= a(rho_bar)`.
- Lemma A for the conductor exponent above `7`.

### Output

Every diagonal character has prime-to-`7` conductor dividing

```text
(3)^3 (sqrt(5))^3,
```

with the stated ordinary/niveau-two behavior at the prime above `7`.

### Logical check

The proof uses only the source conductor table and Lemma A. The source table is exhaustively transcribed in `PRIMITIVE_VALUATION_CONDUCTOR_TABLE.md`. No auxiliary-prime elimination or level lowering is used.

### Status

**Closed in the current written audit.** Older wording describing the branchwise source table as pending is stale and has been corrected.

## Niveau-two reducible branch audit

### Inputs

- Lemmas A and B.
- Exact ray-class sequence for `m0 -> m1=m0*p7`.
- The computed group orders `|F_49^*|=48` and ray-kernel order `24`.

### Output

Every globalized tame exponent is even, contradicting the niveau-two exponents `1` and `7`.

### Logical check

This step eliminates only the niveau-two reducible branch. It does not assume irreducibility and does not use level lowering. The local-to-global map and its unit kernel are explicitly identified.

### Status

**Closed**, subject to the exact ray-class data already certified.

## Lemma C audit

### Inputs

- Lemma B's ray modulus in the ordinary branch.
- Exact ray class group `Z/180 x Z/2`.

### Output

Exactly `360` algebraic-closure-valued ray characters are enumerated; `F_(7^12)` is merely a common realization field.

### Logical check

The enumeration does not assume characters are `F_49`-valued. It depends on B, but not on D or on level lowering.

### Status

**Closed.**

## Lemma D audit

### Valid completed reductions

1. The generic good-reduction `l=19` comparison is paired at the two primes and is exhaustive for that branch.
2. The full four-branch auxiliary-prime sieve leaves exactly
   `(0,0), (0,1), (90,0), (90,1)`.
3. The corrected tangent-branch calculation shows that the toric splitting character at `7` is the nontrivial unramified quadratic character. This removes `(0,0)`.
4. The branchwise conductor comparison removes `(0,1)` at the prime above `3` and `(90,1)` at the prime above `5`.
5. Exactly one reducible semisimplification remains: `(90,0)`, quadratically ramified at both primes and compatible with conductor pair `(2,2)`.

### Circular route explicitly rejected

The exact Brandt module at level `(2,2)` contains no matching eigensystem. However, the source level-lowering theorem used to place a representation at that level assumes irreducibility. Therefore

```text
level-(2,2) Brandt vanishing -> irreducibility
```

is circular and is not a proof of Lemma D.

### Direct-certificate limitation

The auxiliary-prime direct certificate omits the separate `t=1` degeneration. Quadratic characters automatically satisfy the corresponding Steinberg/toric trace congruence, so that certificate cannot unconditionally remove `(90,0)`.

### Remaining noncircular routes

- Construct the correct parallel-weight-two Eisenstein stabilization at square level `(3)^2(sqrt(5))^2`, compute all cusp constants integrally at `7`, transfer the away-from-level congruence to the chosen local stabilizations, and prove the all-cusp constant-term ideal is a `7`-adic unit.
- Recover an explicit RM correspondence/action sufficient to determine the missing local RM matrix.
- Supply another reducible-compatible exact-level theorem or complete Selmer obstruction.

### Status

**Open at exactly one explicit survivor `(90,0)`.** The factor `16/15` is a `7`-adic unit and is strong evidence for the Eisenstein obstruction, but it is not by itself the missing theorem.

## Post-irreducibility chain audit

The candidate-level computations cannot be promoted to the final theorem until absolute irreducibility is established. Even after Lemma D is closed, the written proof still requires the theorem-level JL/Brandt bridge:

- exact weight, level, central character and Hecke normalization;
- relevant newspace identification;
- oldspace and degeneracy-map control;
- Eisenstein constituent separation;
- generalized residual eigenspace implication;
- residue-field scalar extension and split-prime labeling.

The exact rank computations are valid computational certificates but are not substitutes for those identifications.

## Consistency verdict

After correcting stale status language, the canonical proof package has a coherent acyclic dependency structure. Lemmas A, B and C are closed in the current audit. Lemma D is not closed and is isolated to one noncircular theorem bridge for `(90,0)`. No valid route from the existing level-`(2,2)` computation to irreducibility is currently available without adding a new theorem.

## Permitted public claim

> The system has closed the first three irreducibility lemmas, reduced the fourth to one explicit quadratic survivor, identified and rejected a circular computational shortcut, and isolated a bounded all-cusp weight-two Eisenstein theorem as the preferred remaining bridge. Separately, all candidate Step-IV modules have been computationally eliminated, pending irreducibility and the JL/Brandt theorem bridge.

## Prohibited public claims

- Lemma D is proved.
- Absolute irreducibility at `p=7` is proved.
- The exact Brandt computation at level `(2,2)` proves irreducibility.
- The full `(3,5,7)` nonexistence theorem is proved.
- The Beal conjecture is proved.