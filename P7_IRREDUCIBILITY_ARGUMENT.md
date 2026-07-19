# Candidate absolute irreducibility argument at p=7

## Status

The computational completeness issues for the ordinary branch are now resolved
over the full algebraic closure. Two mathematical inputs remain to be proved as
standalone local lemmas:

- Lemma A: exact finite-flat/Raynaud inertia types at p7;
- Lemma B: conductor bound for each diagonal character.

Lemmas C and D are now complete and reproducible; see
`LEMMA_C_D_ABSOLUTE_CHARACTERS_AND_L19.md`.

## Setup

Let K=Q(sqrt(5)) and let p7 be the unique prime above 7. Since 7 is inert,
K_p7/Q_7 is unramified of degree 2 and its residue field is F_49.

Assume absolute reducibility:

    rho_bar_7^ss = chi_1 direct_sum chi_2,
    chi_1 chi_2 = epsilon_bar_7.

## Lemma A target: finite-flat inertia

Under the required finite-flat hypotheses, the tame inertia exponents should be

    chi_1|I = omega_2^n,
    chi_2|I = omega_2^(8-n),
    n in {0,1,7,8}.

Up to exchange, the two branches are:

- ordinary type {0,8};
- niveau-two type {1,7}.

This statement still requires a precise citation/proof for this Frey
specialization.

## Niveau-two branch

For

    m0 = p3^3 p5^3 infinity_1 infinity_2,
    m1 = m0 p7,

PARI/GP gives

    Cl_m0 = [180,2],
    Cl_m1 = [360,12,2],

and hence

    |ker(Cl_m1 -> Cl_m0)| = 24.

The local tame unit quotient is `F_49^*`, of order 48, while the new global ray kernel has order 24. This order comparison strongly suggests that the global quotient kills the unique subgroup of order 2 and hence admits only even `omega_2` exponents. However, the order computation alone does not identify the kernel map.

To make the exclusion rigorous, one must explicitly identify the image of the local tame unit group in `Cl_m1/Cl_m0` and prove that every global ray character restricts with even `omega_2` exponent. Until that map is written down, the exclusion of exponents 1 and 7 remains conditional.

This conclusion is also conditional on Lemma B supplying the stated global conductor support.

## Ordinary branch — complete over Fbar_7

No assumption is made that chi is F_49-valued.

The ray class group is

    Cl_m0 = Z/180Z direct_sum Z/2Z.

Thus there are exactly 360 algebraic-closure-valued characters in
characteristic 7. All values lie in F_{7^12}, since ord_180(7)=12.

At l=19, the two primes above 19 both have ray coordinates [141,1]. For every
admissible nonsingular local Frey specialization, the unordered pair of RM
traces is computed from the genus-two characteristic polynomial. There are 15
such unordered pairs.

The paired comparison over all 360 characters gives

    actual_trace_pairs=15
    survivors_at_l19_pairwise=0
    survivors=[]

Therefore the ordinary absolutely reducible branch is eliminated completely,
including all conjugate-pair and larger coefficient-field cases.

Primary script:

    research/beal/scripts/eliminate_all_c0_l19_pairs.gp

## Conditional conclusion

Once Lemma A and Lemma B are proved with the exact hypotheses above, both
possible reducible inertia branches are impossible, and therefore

    rho_bar_7 is absolutely irreducible.

This document does not yet claim an unconditional proof: the remaining gap is
now localized entirely in Lemmas A and B, not in character enumeration or the
l=19 trace computation.