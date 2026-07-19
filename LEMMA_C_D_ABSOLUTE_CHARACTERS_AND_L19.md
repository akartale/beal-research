# Lemmas C and D: absolute characters and the paired l=19 sieve

## Lemma C — completeness over the algebraic closure

Let

    m0 = p3^3 p5^3 infinity_1 infinity_2

and suppose the semisimplification of the residual RM representation is
absolutely reducible in the ordinary branch:

    rho_bar_7^ss = chi direct_sum epsilon_bar_7 chi^(-1),

with chi unramified above 7.

PARI/GP gives

    Cl_m0(K) = Z/180Z direct_sum Z/2Z.

In characteristic 7, every algebraic-closure-valued character of this ray
class group has image of order dividing 180 on the first factor and dividing 2
on the second factor. Hence there are exactly

    180 * 2 = 360

characters over Fbar_7.

No field-of-definition assumption is required. Since ord_180(7)=12, all values
of all 360 characters lie in F_{7^12}; this is only a convenient common field
for the computation, not an extra hypothesis.

The prime ideals above 19 both have ray-class coordinates

    [141,1]

with respect to the chosen generators.

## Lemma D — completeness of the paired trace set at l=19

For every pair (A,B) in (F_19^*)^2:

1. compute n=A^3+B^5;
2. require n != 0 and require that n is a seventh power in F_19^*;
3. form the reduction of the plus Frey curve

       y^2 = 5x^6 - 12 A x^5 - 10 B^5 x^3 + B^10;

4. discard exactly the singular reductions, detected by vanishing of the
   polynomial discriminant;
5. compute the genus-two characteristic polynomial

       X^4 + c1 X^3 + c2 X^2 + 19 c1 X + 19^2;

6. extract the unordered pair of RM traces as the roots, over Fbar_7, of

       T^2 + c1 T + (c2 - 2*19) mod 7.

The resulting set contains 15 unordered trace pairs.

For a reducible ray character chi, and for the two primes q1,q2 above 19, the
predicted unordered pair is

    { chi(q1)+19 chi(q1)^(-1),
      chi(q2)+19 chi(q2)^(-1) }.

The comparison must be paired. Comparing either predicted trace with the union
of all individual RM roots is weaker and is not sufficient.

The exhaustive computation over all 360 algebraic-closure-valued characters
returns

    actual_trace_pairs=15
    survivors_at_l19_pairwise=0
    survivors=[]

Therefore no absolutely reducible ordinary character survives.

## Reproducibility

Primary script:

    research/beal/scripts/eliminate_all_c0_l19_pairs.gp

Supporting computations:

    research/beal/scripts/frey_pairs_l19.gp
    research/beal/scripts/bnr_map_7.gp
    research/beal/scripts/rayclass_357_full.gp

## Remaining hypotheses outside Lemmas C and D

This calculation proves the complete character enumeration and complete paired
l=19 elimination, conditional only on the inputs supplied by the other local
lemmas:

- Lemma A: exact finite-flat inertia types at p7;
- Lemma B: conductor bound for the diagonal characters.

It does not assume that the diagonal characters are F_49-valued.