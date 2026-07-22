# Next steps

The broad search is done. Do not start it again unless we find a real error.

The remaining work is much smaller and more specific.

## First: remove the last survivor

Only `(90,0)` is left.

The best route right now is the Eisenstein series argument.

What still has to be done:

- write down the exact series at the level we use
- list every cusp
- compute the constant term at each cusp
- check that all needed coefficients are integral at 7
- show that the Hecke congruence reaches the stabilized forms we actually use
- prove that the constant terms generate a 7-adic unit ideal

A key number is already known. Up to harmless units, the expected constant term is `16/15`, which is `2 mod 7`. That is good for the contradiction we want.

But checking only the cusp at infinity is not enough. The proof has to cover every cusp.

The argument is finished only when it clearly says:

1. the cusp form is congruent to the Eisenstein form
2. every Eisenstein constant term is zero mod 7
3. this would force the whole constant-term ideal to be divisible by 7
4. that is impossible because the ideal is a 7-adic unit

No shortcuts here. This is the main open point.

## Backup route

There is another possible route through real multiplication.

To use it, we would need:

- an explicit correspondence on the curve or its Jacobian
- the action of the RM generator
- the missing residual matrix
- a direct contradiction for `(90,0)`

A source saying only that the Jacobian has RM is not enough. We need the actual action.

Use this route only if new source material or code appears.

## Second: finish the Brandt bridge

After irreducibility is done, the proof still has to explain why the level-lowered systems are exactly the ones checked by our Brandt calculations.

The final write-up should cover:

- the exact weight and level conventions
- the Jacquet Langlands link
- old and new parts
- the Eisenstein part
- multiplicity issues mod 7
- the quotient used in the code
- the prime labels at 11, 19 and 29
- field extensions when they are needed

The working file is `JL_BRANDT_THEOREM_BRIDGE.md`.

## Third: cleanup and final checks

- check the zero, sign and valuation edge cases
- check the variable change everywhere
- finish the local check at level `(2,2)`
- rerun the important scripts in a clean environment
- remove old status lines that no longer match
- merge the proof into one final manuscript

## Parts that should not be redone without a reason

These parts are stable for now:

- the ray class group
- all 360 characters
- the paired coordinates above 19
- the corrected toric splitting calculation at `t=1`
- the reduction to `(90,0)`
- the Brandt dimensions
- the zero-survivor results at all four levels
- the icosian and maximal-order checks

## Where to restart

Read these files first:

1. `CURRENT_PROOF_SNAPSHOT.md`
2. `P7_900_EISENSTEIN_NECESSITY_BRIDGE_AUDIT.md`
3. `LEMMAS_ABCD_REAUDIT.md`
4. `PROOF_ELEMENT_INDEX.md`
5. `JL_BRANDT_THEOREM_BRIDGE.md`

Then take the first unfinished Eisenstein item and work on that. Switch to the RM route only if the missing explicit data turns up.

That is the shortest honest path from the current state.