# Candidate absolute irreducibility argument at p=7

## Status

The computational completeness issues for the ordinary branch are resolved
over the full algebraic closure.  The conductor comparison required in Lemma B
is now proved directly in `LEMMA_A_B_LOCAL_PROOF_DRAFT.md`; subject to the
source conductor exponents and finite-flatness at `p7`, Lemma B is complete.

Lemma A is supplied by Raynaud, Corollaire 3.4.4, together with Conrad,
Lemma 4.1.  Raynaud bounds every tame digit by the local ramification index
`e=1`.  A diagonal constituent is a character of the full local decomposition
group, so Frobenius conjugacy over the residue field F_49 forces those digits
to be periodic with period two.  Hence its tame exponent is `a0+7*a1` with
`a0,a1 in {0,1}`.  This remains valid when the stable line is defined only
over an extension of F_49.

Lemmas C and D are complete and reproducible; see
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

The precise proof and citations are recorded in
`LEMMA_A_B_LOCAL_PROOF_DRAFT.md`; no additional labelled-weight hypothesis is
used.

## Niveau-two branch

For

    m0 = p3^3 p5^3 infinity_1 infinity_2,
    m1 = m0 p7,

PARI/GP gives

    Cl_m0 = [180,2],
    Cl_m1 = [360,12,2],

and hence

    |ker(Cl_m1 -> Cl_m0)| = 24.

The exact ray-class sequence for increasing the modulus from `m0` to
`m1=m0*p7` gives a surjection from the local tame unit group

    F_49^* = (O_K/p7)^*

to the kernel of `Cl_m1 -> Cl_m0`, with kernel equal to the image of the global
units satisfying the `m0` ray conditions.  Since the source has order 48 and
the ray kernel has order 24, that unit image has order 2.  The cyclic group
`F_49^*` has a unique subgroup of order 2, namely `{+1,-1}`.  Therefore every
global ray character of modulus dividing `m1` is trivial on `-1` locally and
its restriction to tame inertia is `omega_2^n` with `n` even.

The niveau-two exponents supplied by Lemma A are `n=1` and `n=7`, both odd.
Hence the niveau-two reducible branch is impossible.  This deduction is
conditional only on the conductor support in Lemma B and the exact inertia
classification in Lemma A; the previously missing local-to-global ray-map
identification is now supplied by the exact sequence.

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

## Conclusion

The ordinary branch is eliminated by Lemmas C and D, and the niveau-two branch
is eliminated by the exact ray-class sequence above.  Lemma B's semisimplified
conductor comparison is proved in `LEMMA_A_B_LOCAL_PROOF_DRAFT.md`.  Lemma A
follows from Raynaud Corollaire 3.4.4 and Conrad Lemma 4.1, using the source
paper's finite-flatness statement and the residual F_49 coefficient action.
Therefore

    rho_bar_7 is absolutely irreducible.

This conclusion is conditional only in the ordinary mathematical sense that
the quoted source theorem `thm:mot-+-prop` and its conductor table must apply to
the Frey representation under the recorded variable translation; there is no
remaining local group-scheme or ray-character gap in the irreducibility
argument.