# Current Proof Snapshot — Signature `(3,5,7)`

_Logical dependency and circularity audit: `LOGICAL_PROOF_AUDIT.md`._

_Frozen on 2026-07-21 for hackathon submission._  
_Base Git commit before this stabilization pass: `4c0006a434915e0e208b7f6d829ef8def02317e6`._

## Purpose

This file is the canonical frozen statement of what is proved, what is computationally certified, and what remains open at the submission cutoff. It supersedes stale progress language in older notes. Historical files remain evidence of the research process but must not be used as current status unless referenced here.

## Main theorem status

The nonexistence theorem for primitive solutions of generalized Fermat signature `(3,5,7)` is **not yet claimed**.

The project has:

- completed the main computational elimination pipeline for all Step-IV candidate levels;
- closed Lemmas A, B, and C in the current residual-irreducibility audit;
- reduced Lemma D to one explicit quadratic survivor `(90,0)`;
- identified two noncircular routes to eliminate that survivor;
- not yet completed either route at theorem level.

## Residual irreducibility package

### Lemma A — finite-flat inertia types

**Status: closed in the current audit.**

Canonical evidence:

- `LEMMAS_ABCD_REAUDIT.md`
- `LEMMA_A_B_LOCAL_PROOF_DRAFT.md`

Closed inputs include inertness of `7` in `Q(sqrt(5))`, the finite-flat source hypothesis, Raynaud-type inertia restrictions, and the resulting tame exponent possibilities.

### Lemma B — conductor bounds

**Status: closed in the current audit.**

Canonical evidence:

- `LEMMAS_ABCD_REAUDIT.md`
- `PRIMITIVE_VALUATION_CONDUCTOR_TABLE.md`
- `LEMMA_A_B_LOCAL_PROOF_DRAFT.md`

The translated branch table under `(a,b,c)=(B,-C,A)` gives the required conductor bounds for the ray-character modulus.

### Lemma C — ordinary ray characters

**Status: closed.**

Canonical evidence:

- `LEMMAS_ABCD_REAUDIT.md`
- `LEMMA_C_D_ABSOLUTE_CHARACTERS_AND_L19.md`
- `RAY_CLASS_357_RESULTS.md`
- `p7_rayclass_coords.csv`
- `p7_rayclass_coords_full.csv`

The ray class group is `Z/180 x Z/2`, giving exactly `360` characters. The paired prime-above-`19` coordinates and character enumeration are exact.

### Lemma D — ordinary branch elimination

**Status: open, sharply reduced.**

Closed computational reductions:

1. The generic paired-`19` sieve eliminates all `360` characters in the good-reduction branch.
2. The complete auxiliary-branch sieve leaves four quadratic characters:

   ```text
   (0,0), (0,1), (90,0), (90,1).
   ```

3. The corrected toric splitting condition at `7` eliminates `(0,0)`.
4. Local conductor comparisons eliminate `(0,1)` and `(90,1)`.
5. Exactly one survivor remains:

   ```text
   (90,0)
   ```

6. This survivor forces conductor pair `(2,2)`.
7. The level-`(2,2)` Brandt computation contains no matching mod-`7` eigensystem.

However, that Brandt computation cannot by itself prove irreducibility because the cited level-lowering theorem assumes irreducibility. Using it here would be circular.

Canonical evidence:

- `LEMMAS_ABCD_REAUDIT.md`
- `P7_QUADRATIC_SURVIVOR_LOCAL_CONDUCTOR.md`
- `P7_900_LEVEL22_BRANDT_CERTIFICATE.md`
- `P7_900_DIRECT_LOCAL_CERTIFICATE_AUDIT.md`
- `P7_900_EISENSTEIN_NECESSITY_BRIDGE_AUDIT.md`

## The two remaining noncircular routes for Lemma D

### Route 1 — explicit RM correspondence

The source `CurveConstruction.m` computes a quotient curve and states that its Jacobian has real multiplication, but it does not export an explicit RM correspondence or the action of a generator on the Jacobian or nodal lattice. Therefore the missing one of four RM matrices cannot currently be reconstructed honestly from the published quotient computation alone.

**Status: blocked on missing explicit correspondence data.**

### Route 2 — weight-two Eisenstein necessity bridge

After twisting `(90,0)`, the residual semisimplification is

```text
1 direct_sum epsilon_bar_7.
```

Away from the bad level this forces

```text
T_q = 1 + N(q)  (mod 7).
```

The candidate stabilized weight-two Hilbert Eisenstein series has expected constant-term factor

```text
zeta_F(-1)(1-N(3))(1-N(sqrt(5))) = 16/15,
```

which is a `7`-adic unit (`2 mod 7`). If a valid necessity theorem for the exact square level forces every cusp constant term to vanish modulo `7`, the survivor is impossible.

The available sources do not currently provide the exact theorem needed:

- Martin gives an existence criterion, not the required converse for this precise stabilization.
- Fretwell–Roberts gives a necessity argument under hypotheses excluding this parallel-weight-two composite square-level case.

Therefore the following five checks remain:

1. Construct the correct parallel-weight-two stabilization at level `(3)^2(sqrt(5))^2` with the required local `U_p` eigenvalues.
2. Compute constant terms at every cusp.
3. Verify integral `q`-expansions over `Z_(7)` and the relevant `q`-expansion principle.
4. Transfer away-from-level Hecke congruence to the chosen local stabilizations, or work through the full integral Hecke algebra and Eisenstein ideal.
5. Prove that the all-cusp constant-term ideal is a `7`-adic unit ideal.

**Status: preferred route; bounded but incomplete.**

## Computational Step-IV status

| Level | Exact computational status | Theorem-level status |
|---|---|---|
| `(2,2)` | No compatible mod-`7` eigensystem; local CM candidates computationally separated | Requires noncircular use and local/integral certification |
| `(2,3)` | Brandt module dimension `226`; filter chain `226 -> 8 -> 4 -> 0` | JL/Brandt completeness bridge remains |
| `(3,2)` | Dimension `406`; filter chain `406 -> 15 -> 4 -> 0` | JL/Brandt completeness bridge remains |
| `(3,3)` | Dimension `2026`; filters at `11`, `19`, `29` give zero survivors | JL/Brandt completeness bridge remains |

These are exact computational facts, not by themselves a complete proof of the main theorem.

## Current dependency chain

```text
Primitive solution
      |
      v
Frey motive and local conductor table
      |
      v
Residual representation mod 7
      |
      +--> Lemma A: finite-flat inertia types       [closed]
      +--> Lemma B: conductor bounds                [closed]
      +--> Lemma C: ray-character enumeration       [closed]
      +--> Lemma D: reducible branch elimination    [OPEN: survivor (90,0)]
                         |
                         +--> explicit RM route      [blocked]
                         +--> Eisenstein route       [5 bounded checks]

After irreducibility:
      |
      v
Level lowering / automorphic placement
      |
      v
JL / Brandt identification and old-new-Eisenstein control
      |
      v
Exact mod-7 Hecke elimination at four levels
      |
      v
Final contradiction
```

## Submission-safe claim

> An AI-assisted arithmetic-geometry research system built an exact computational pipeline for the generalized Fermat signature `(3,5,7)`, computationally eliminated every candidate Step-IV level, closed three of four residual-irreducibility lemmas, reduced the fourth to one explicit quadratic survivor, and isolated a bounded five-check Eisenstein obstruction whose expected constant-term factor is a `7`-adic unit.

## Claims forbidden at this snapshot

Do not claim any of the following:

- that the full `(3,5,7)` case is proved;
- that Lemma D is proved;
- that the level-`(2,2)` Brandt computation proves irreducibility;
- that Martin or Fretwell–Roberts directly covers the exact weight-two square-level case;
- that the missing RM matrix has been recovered.

## Preservation rule

Future work must update this file only when accompanied by:

1. a specific new proof artifact or certificate;
2. an explicit statement of which open item is closed;
3. a dependency check showing the new argument is noncircular;
4. a reproducibility command or a precise bibliographic theorem reference.