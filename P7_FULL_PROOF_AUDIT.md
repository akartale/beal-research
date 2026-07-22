# Full proof audit for the signature `(3,5,7)`

_Last synchronized: 2026-07-21_

## Scope

This file records the current theorem-level structure of the modular-method argument. It must be read together with:

- `CURRENT_PROOF_SNAPSHOT.md` — frozen mathematical status;
- `LOGICAL_PROOF_AUDIT.md` — dependency and circularity audit;
- `LEMMAS_ABCD_REAUDIT.md` — detailed status of the irreducibility lemmas;
- `PROOF_ELEMENT_INDEX.md` — map of proof artifacts and certificates.

The large arithmetic computations were not rerun for this audit. Their outputs are treated as previously certified computational inputs. The present audit checks logical use of those inputs.

## Source-variable translation

The equation

```text
A^3 + B^5 = C^7
```

matches the source convention

```text
x^5 + y^p + z^3 = 0
```

under

```text
p = 7,
x = B,
y = -C,
z = A,
(a,b,c) = (B,-C,A).
```

The source paper's final theorem excludes `p=7`. Therefore the repository must independently close residual irreducibility and every Step-IV candidate level.

## Residual irreducibility chain

### Lemma A — finite-flat inertia types

**Status: closed in the current audit.**

Raynaud's finite-flat Jordan--Hoelder statement applies at the unique prime above `7`, where the absolute ramification index is `1`. Frobenius conjugacy over residue cardinality `49` forces period-two Raynaud digits. The only inertia exponent multisets are

```text
{0,8} and {1,7}.
```

The proof does not assume that a stable line is defined over `F_49`.

### Lemma B — conductor bounds

**Status: closed in the current audit.**

The Artin-conductor comparison with semisimplification is proved directly. The branchwise source conductor exponents have been checked under the exact variable translation in `PRIMITIVE_VALUATION_CONDUCTOR_TABLE.md`. The selected ordinary character factors through the prime-to-`7` ray modulus, while the niveau-two branch allows one power of the prime above `7`.

### Niveau-two branch

**Status: eliminated.**

The ray-class exact sequence shows that every globalized tame exponent is even. This contradicts the niveau-two exponents `1` and `7`. This argument does not use irreducibility or level lowering.

### Lemma C — ordinary ray characters

**Status: closed.**

The ray class group is `Z/180 x Z/2`, giving exactly `360` algebraic-closure-valued characters. The use of `F_(7^12)` is only a common realization field.

### Lemma D — ordinary branch elimination

**Status: open at one explicit character.**

The valid chain is:

```text
360 ordinary characters
  -> full four-branch auxiliary-prime sieve
4 quadratic characters: (0,0), (0,1), (90,0), (90,1)
  -> corrected toric splitting at 7
3 characters: (0,1), (90,0), (90,1)
  -> local conductor contradictions at 3 and sqrt(5)
1 character: (90,0)
```

The survivor `(90,0)` is quadratically ramified at both bad primes and is compatible only with conductor pair `(2,2)`.

The exact level-`(2,2)` Brandt module has no matching eigensystem. However, the source theorem placing the representation at that lowered level assumes irreducibility. Using that computation to prove irreducibility would therefore be circular.

The attempted direct auxiliary-prime certificate also does not close the gap because it omits the separate `t=1` degeneration, which quadratic characters satisfy automatically.

The preferred remaining route is the bounded all-cusp parallel-weight-two Eisenstein argument recorded in `P7_900_EISENSTEIN_NECESSITY_BRIDGE_AUDIT.md`. The candidate constant-term factor is `16/15`, a `7`-adic unit, but five exact stabilization, integrality, congruence-transfer, and all-cusp checks remain.

Therefore absolute irreducibility at `p=7` is not yet proved.

## Step-IV computational status

All four candidate levels are computationally eliminated in the implemented exact modules:

| Level | Computational status | Theorem-level status |
|---|---|---|
| `(2,2)` | no matching candidate survives local/Brandt computations | local-integral completeness and use after irreducibility still require certification |
| `(2,3)` | exact paired Brandt sieve gives dimension zero | JL/Brandt bridge pending |
| `(3,2)` | exact paired Brandt sieve gives dimension zero | JL/Brandt bridge pending |
| `(3,3)` | exact paired Brandt sieve gives dimension zero | JL/Brandt bridge pending |

These computations do not by themselves prove the final theorem. After irreducibility, the proof still requires exact identification of the relevant Hilbert spaces with the computed Brandt modules, including newspace completeness, oldform control, Eisenstein separation, multiplicities, residue fields, and Hecke normalization.

## Acyclicity verdict

The current canonical proof structure is acyclic:

```text
source local inputs
 -> Lemmas A and B
 -> niveau-two elimination and Lemma C
 -> Lemma D reductions
 -> OPEN elimination of (90,0)
 -> absolute irreducibility
 -> level lowering
 -> JL/Brandt identification
 -> computational zero eigenspaces
 -> final theorem
```

The only detected circular shortcut is the rejected use of level-`(2,2)` Brandt vanishing to prove the irreducibility required to reach that level.

## Exact remaining theorem obligations

1. Eliminate `(90,0)` by a noncircular theorem-level argument.
2. Complete primitive/sign/valuation exhaustiveness and source theorem citation integration.
3. Certify the level-`(2,2)` integral local invariants and branch exhaustiveness.
4. Prove the JL/Brandt identification and full relevant-space completeness at levels `(2,3)`, `(3,2)`, and `(3,3)`.
5. Independently reproduce hashes and deterministic certificates from a clean environment.
6. Produce a final manuscript with no conditional labels and obtain independent mathematical review.

## Final verdict

The proof package is logically coherent after synchronization, but incomplete. Lemmas A, B, and C are closed in the current audit. Lemma D is reduced to one explicit survivor `(90,0)` and remains open. The full signature-`(3,5,7)` theorem must not yet be claimed.