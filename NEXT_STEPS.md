# Next steps for signature `(3,5,7)`

Start from `CURRENT_PROOF_SNAPSHOT.md`. The broad search is over, so do not restart it unless a real error shows up. The remaining path is narrow.

## Priority 1: finish Lemma D without circular reasoning

The best route right now is the weight-two Hilbert Eisenstein argument for the last survivor `(90,0)`.

### What has to be produced

1. **The exact stabilized Eisenstein series**
   - Base field: `Q(sqrt(5))`.
   - Parallel weight: `2`.
   - Level: `(3)^2(sqrt(5))^2`.
   - Write down the local stabilization operators and the needed `U_p` eigenvalues.

2. **A table for every cusp**
   - List all cusps for the exact congruence subgroup.
   - Give each constant term symbolically and record its `7`-adic valuation.
   - Checking only the cusp at infinity is not enough.

3. **The integral setup**
   - Prove that the relevant `q`-expansions are integral over `Z_(7)`.
   - State the exact `q`-expansion principle and check its assumptions.

4. **Transfer of the Hecke congruence**
   - Show that matching Hecke eigenvalues away from the level gives a congruence between the correctly stabilized forms.
   - Another option is to work directly in the integral Hecke algebra with the Eisenstein ideal.

5. **The unit-ideal contradiction**
   - Prove that all cusp constant terms generate a `7`-adic unit ideal.
   - Up to units, the expected generator is `16/15`, which is `2 mod 7`.

### When Lemma D can be called finished

The written proof must give this chain:

```text
cuspidal congruence
  => every stabilized Eisenstein constant term is 0 mod 7
  => the all-cusp constant-term ideal is divisible by 7
  => contradiction, because that ideal is a 7-adic unit.
```

It must cover weight `2`, the square level, every cusp and the actual stabilizations being used. No hand waving here, this is the main gap.

## Backup route: explicit RM correspondence

Use this only if the missing correspondence data become available.

Needed:

- an explicit correspondence on the quotient curve or its Jacobian;
- the action of an RM generator on the relevant integral or torsion lattice;
- the missing residual matrix;
- a direct local contradiction for `(90,0)`.

A source saying that the Jacobian “has RM” is not enough. We need the action itself.

## Priority 2: finish the JL/Brandt bridge

Once Lemma D and irreducibility are done, connect the level-lowered residual systems to the exact Brandt modules used in the computation.

The write-up must cover:

- the exact weight, central character and level conventions;
- the Hecke-equivariant Jacquet–Langlands identification;
- oldspace and newspace;
- how the Eisenstein part is removed or controlled;
- multiplicity and generalized eigenspaces in characteristic `7`;
- the norm-one quotient versus the central-character quotient;
- prime labels and Hecke normalization at `11`, `19`, `29`;
- extension of the residue field when needed.

Working file: `JL_BRANDT_THEOREM_BRIDGE.md`.

## Priority 3: final local checks and cleanup

- Finish the primitive zero, sign and valuation edge cases.
- Check the variable translation `(a,b,c)=(B,-C,A)` everywhere.
- Finish the integral local check at level `(2,2)`.
- Re-run the deterministic certificates in a clean environment.
- Merge the argument into one manuscript.
- Remove old status lines that no longer match the current state.

## Do not redo these parts without a concrete reason

Treat the following as stable unless a specific defect is found:

- the ray class group and all 360 characters;
- the paired coordinates above `19`;
- the corrected `t=1` toric splitting computation;
- the reduction to the single survivor `(90,0)`;
- the Brandt dimensions and zero-survivor results at all four levels;
- the icosian, maximal-order and open-compact certificates.

## Restart checklist

At the next session, read:

1. `CURRENT_PROOF_SNAPSHOT.md`
2. `P7_900_EISENSTEIN_NECESSITY_BRIDGE_AUDIT.md`
3. `LEMMAS_ABCD_REAUDIT.md`
4. `PROOF_ELEMENT_INDEX.md`
5. `JL_BRANDT_THEOREM_BRIDGE.md`

Then take the first unchecked Eisenstein item and work on that. Switch to the RM route only if new explicit data appear.