# Proof Element Index — Signature `(3,5,7)`

This index maps mathematical claims to their canonical proof or certificate files. It is intended to prevent accidental reliance on stale exploratory notes.

## Canonical status documents

- `LOGICAL_PROOF_AUDIT.md` — canonical dependency, sufficiency, and circularity audit.

| Purpose | Canonical file |
|---|---|
| Frozen mathematical state | `CURRENT_PROOF_SNAPSHOT.md` |
| High-level project state | `PROJECT_STATUS.md` |
| Restart/handoff instructions | `NEXT_STEPS.md` |
| Main proof draft | `MANUSCRIPT_357_FROM_SCRATCH.md` |
| Residual irreducibility audit | `LEMMAS_ABCD_REAUDIT.md` |
| JL/Brandt theorem bridge | `JL_BRANDT_THEOREM_BRIDGE.md` |

## Problem reduction and local branches

| Element | Files | Status |
|---|---|---|
| Primitive/sign/valuation translation | `PRIMITIVE_VALUATION_CONDUCTOR_TABLE.md`, `MANUSCRIPT_357_FROM_SCRATCH.md` | Substantially complete; final edge-case audit remains |
| Source conductor transcription | `PRIMITIVE_VALUATION_CONDUCTOR_TABLE.md` | Closed for Lemma B usage |
| Frey setup and branch stratification | `P7_STEP_IV_STRATIFICATION.md`, `P7_STEP_IV_CANDIDATE_INVENTORY.md` | Computational framework established |

## Lemmas A–D

| Lemma | Core claim | Canonical files | Current status |
|---|---|---|---|
| A | Finite-flat inertia types at `7` | `LEMMAS_ABCD_REAUDIT.md`, `LEMMA_A_B_LOCAL_PROOF_DRAFT.md` | Closed in current audit |
| B | Conductor bounds for reducible characters | `LEMMAS_ABCD_REAUDIT.md`, `PRIMITIVE_VALUATION_CONDUCTOR_TABLE.md` | Closed in current audit |
| C | Exact ordinary ray-character enumeration | `LEMMAS_ABCD_REAUDIT.md`, `LEMMA_C_D_ABSOLUTE_CHARACTERS_AND_L19.md`, `RAY_CLASS_357_RESULTS.md` | Closed |
| D | Eliminate every reducible ordinary character | `LEMMAS_ABCD_REAUDIT.md`, `P7_QUADRATIC_SURVIVOR_LOCAL_CONDUCTOR.md`, `P7_900_EISENSTEIN_NECESSITY_BRIDGE_AUDIT.md` | Open; unique survivor `(90,0)` |

## Lemma D branch evidence

| Element | Canonical evidence | Meaning |
|---|---|---|
| Generic paired-19 sieve | `LEMMA_C_D_ABSOLUTE_CHARACTERS_AND_L19.md` | Eliminates generic good-reduction characters |
| Full auxiliary-branch sieve | `LEMMAS_ABCD_REAUDIT.md` and associated scripts/data | Leaves four quadratic characters |
| Corrected toric splitting | `P7_T1_TORIC_SPLITTING_CORRECTION.md`, `scripts/p7_t1_branch_splitting.py` | Eliminates `(0,0)`, not all quadratic survivors |
| Local conductor elimination | `P7_QUADRATIC_SURVIVOR_LOCAL_CONDUCTOR.md` | Eliminates `(0,1)` and `(90,1)` |
| Unique survivor | `LEMMAS_ABCD_REAUDIT.md` | `(90,0)`, conductor pair `(2,2)` |
| Direct local-certificate limitation | `P7_900_DIRECT_LOCAL_CERTIFICATE_AUDIT.md` | Explains omitted `t=1` and why quadratic characters survive |
| Eisenstein route audit | `P7_900_EISENSTEIN_NECESSITY_BRIDGE_AUDIT.md` | Defines exact five-check remaining bridge |
| Alternative RM route | source audit described in `CURRENT_PROOF_SNAPSHOT.md` | Blocked by missing explicit correspondence |

## Quaternionic and Brandt infrastructure

| Element | Canonical files | Status |
|---|---|---|
| Icosian maximal order | `ICOSIAN_ORDER_CERTIFICATE.md` | Certified computationally |
| Class number one | `ICOSIAN_CLASS_NUMBER_ONE_CERTIFICATE.md` | Certified computationally |
| Open compact / `K_0` data | `OPEN_COMPACT_K0_CERTIFICATE.md` | Certified computationally |
| Port plan and implementation | `BRANDT_MOD7_PORT_PLAN.md`, scripts under `scripts/` | Implemented |
| JL/Brandt theorem bridge | `JL_BRANDT_THEOREM_BRIDGE.md` | Incomplete theorem-level bridge |

## Step-IV level certificates

| Level | Certificate | Exact computational result |
|---|---|---|
| `(2,2)` | `P7_900_LEVEL22_BRANDT_CERTIFICATE.md` | No matching mod-`7` eigensystem |
| `(2,3)` | relevant Brandt output and status in `PROJECT_STATUS.md` | `226 -> 8 -> 4 -> 0` |
| `(3,2)` | `LEVEL_32_CERTIFICATE.md` | `406 -> 15 -> 4 -> 0` |
| `(3,3)` | `LEVEL_33_CERTIFICATE.md` | dimension `2026`; zero after paired filters |

## Level `(2,2)` local-analysis archive

These files contain the successive local analyses and corrections. They are supporting evidence, not all equally current.

- `P7_CM_HL_BT1.md`
- `P7_HASSE_WITT_LEVEL2025.md`
- `P7_HL_UNRAMIFIED_CM_TWIST.md`
- `P7_INFINITY_HL_DIVIDED_FROBENIUS.md`
- `P7_FORM_E_NORMALIZED_QFROBENIUS.md`
- `P7_FORM_E_QFROBENIUS_INTRINSICNESS.md`
- `P7_ELIMINATE_FORM_E_LOCAL.md`
- `P7_ELIMINATE_HL_FILTERED_FROBENIUS.md`
- `P7_LEVEL2025_FINAL_LOCAL_LEMMA.md`
- `LEVEL_2025_LOCAL_ELIMINATION_STATUS.md`
- `LEVEL_2025_BAD_BRANCH_DIAGNOSIS.md`

Current claims from this archive must be checked against `CURRENT_PROOF_SNAPSHOT.md` before use.

## External-source and theorem audits

| Topic | File |
|---|---|
| General source audit | `P7_EXTERNAL_REFERENCE_AUDIT.md` |
| Reference/source audit | `P7_REFERENCE_AND_SOURCE_AUDIT.md` |
| Full proof audit | `P7_FULL_PROOF_AUDIT.md` |
| Eisenstein necessity comparison | `P7_900_EISENSTEIN_NECESSITY_BRIDGE_AUDIT.md` |
| JL/Brandt requirements | `JL_BRANDT_THEOREM_BRIDGE.md` |

## Historical-note policy

Files not listed as canonical are retained because they document discoveries, failed paths, corrections, or computational provenance. A historical file may not override the status in `CURRENT_PROOF_SNAPSHOT.md`.

When a theorem step is closed, update all three:

1. `CURRENT_PROOF_SNAPSHOT.md`
2. `PROJECT_STATUS.md`
3. this index