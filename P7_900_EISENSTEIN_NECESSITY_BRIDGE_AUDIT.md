# Audit of the weight-two Hilbert Eisenstein necessity bridge for `(90,0)`

## Target

After twisting the final quadratic survivor `(90,0)`, the residual semisimplification is

    1 direct_sum epsilon_bar_7.

Away from the bad level this forces Eisenstein Hecke eigenvalues

    T_q = 1 + N(q)  (mod 7).

The candidate parallel-weight-two Eisenstein series over `F=Q(sqrt(5))`, stabilized at the primes above `3` and `5`, has candidate constant-term factor

    zeta_F(-1)(1-N(3))(1-N(sqrt(5))) = 16/15,

which is `2 mod 7` and hence a 7-adic unit.

## Primary-source comparison

The corrected version of Kimball Martin, *The Jacquet--Langlands correspondence, Eisenstein congruences, and integral L-values in weight 2*, treats weight-two Hilbert Eisenstein congruences by definite quaternionic modular forms. It allows nonsquare level, but its main theorem is an existence result obtained from the Eichler mass formula. It does not by itself state the converse needed here for the exact square-level stabilization.

Fretwell--Roberts, *Hilbert modular Eisenstein congruences of local origin*, proves a necessity argument by comparing a cusp form with a stabilized Eisenstein series, applying the mod-l q-expansion principle and theta injectivity, and then forcing all constant terms to vanish modulo l. However, the stated theorem assumes parallel weight `k>2`, squarefree base level `m`, and a single auxiliary prime level raise. Their proof explicitly notes that more general level products are expected but not supplied.

Thus neither cited theorem can currently be quoted verbatim for the exact level

    (3)^2 (sqrt(5))^2

in parallel weight two.

## What would be sufficient

A direct theorem for the present case needs only the following bounded statement.

Let `f` be a parallel-weight-two Hilbert cuspidal eigenform over `Q(sqrt(5))`, integral at a prime above `7`, whose Hecke eigenvalues away from `(3)(sqrt(5))7` satisfy

    a_q(f) = 1 + N(q) (mod 7),

and whose local stabilizations at `(3)` and `(sqrt(5))` are the ones forced by the conductor-two reducible representation. Then the matching stabilized Eisenstein series must be cuspidal modulo `7`; equivalently, every constant term at every cusp must vanish modulo `7`.

For `Q(sqrt(5))`, narrow class number one reduces the cusp bookkeeping. If the all-cusp constant-term ideal is generated up to 7-adic units by

    zeta_F(-1)(1-N(3))(1-N(sqrt(5))),

then its value `16/15` is a unit and the congruence is impossible.

## Exact remaining checks

1. Construct the correct weight-two Eisenstein stabilization at square level `(3)^2(sqrt(5))^2` with the required local `U_p` eigenvalues.
2. Compute its constant term at every cusp, not only at infinity.
3. Verify integral q-expansions over `Z_(7)` and the q-expansion principle for this level.
4. Prove that equality of Hecke eigenvalues away from the level implies equality of the mod-7 forms after the chosen local stabilizations; alternatively, use the full integral Hecke algebra and Eisenstein ideal.
5. Show that all constant terms generate a 7-adic unit ideal.

If these five checks hold, `(90,0)` is eliminated without determining the RM matrix and without invoking irreducible level lowering.

## Current conclusion

The numerical value `16/15` is strong evidence and is exactly the expected obstruction, but the available cited theorems do not yet cover the precise weight-two square-level situation verbatim. Lemma D remains open until the bounded all-cusp stabilization argument above is supplied or an explicit RM correspondence is computed.