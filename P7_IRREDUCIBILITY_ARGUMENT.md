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

Lemma C is complete and reproducible. `LEMMA_C_D_ABSOLUTE_CHARACTERS_AND_L19.md` supplies only the generic good-reduction part of Lemma D at `19`. The complete four-branch auxiliary-prime sieve leaves four quadratic characters, so Lemma D additionally depends on the split-toric local argument at `7` and the branchwise conductor contradiction at `3` or `sqrt(5)`.

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

for the generic good-reduction branch `19 does not divide ABC`. This does not eliminate the degeneration branches `t=0`, `t=1`, and `t=infinity`. The full four-branch sieve leaves the four quadratic characters `(0,0)`, `(0,1)`, `(90,0)`, and `(90,1)`.

Primary script:

    research/beal/scripts/eliminate_all_c0_l19_pairs.gp

## Conclusion and exact status

The niveau-two branch is eliminated by the exact ray-class sequence, conditional on Lemmas A and B. The categorical finite-flat passage in Lemma A is supplied directly by Raynaud Corollaire 3.4.4; Conrad Lemma 4.1 gives a compatible abelian/exactness statement.

The ordinary ray-character enumeration of Lemma C is complete. The full four-branch sieve leaves four quadratic characters. The source finite-flat and conductor inputs are now checked branchwise in `PRIMITIVE_VALUATION_CONDUCTOR_TABLE.md`, so Lemmas A and B are closed.

The exact tangent-branch computation at `7` corrects the earlier toric claim: the nodes are rational over `F_49`, but the two branches at each node are exchanged by Frobenius. The toric splitting character is the nontrivial unramified quadratic character. Hence the local condition eliminates the trivial character `(0,0)` and retains `(0,1)`, `(90,0)`, and `(90,1)`.

The local conductor calculation then eliminates `(0,1)` because it is unramified at `(3)`, and eliminates `(90,1)` because it is unramified at `(sqrt(5))`. The unique remaining reducible semisimplification is the character `(90,0)`, ramified quadratically at both primes, and it can occur only at lowered level `(2,2)`.

The final character is computationally absent from the full mod-`7` Brandt module at level `(2,2)`: the exact rank certificate has ambient dimension `46` and reaches dimension `0` after the conditions `T11a=T11b=2` and `T19a=1`. Nevertheless Theorem 7.8 assumes irreducibility before applying level lowering to this exact level. Using the level-`(2,2)` vanishing to establish irreducibility would therefore be circular.

An attempted direct local certificate at the auxiliary primes `19,79,89,131` excludes the character from the generic, `t=0`, and `t=infinity` data sets, but it omits the separate `t=1` branch. Since every quadratic character automatically satisfies the `t=1` congruence `a_q=±(q+1)`, that computation is conditional on the auxiliary prime not dividing the relevant Diophantine coordinate and is not an unconditional elimination. See `P7_900_DIRECT_LOCAL_CERTIFICATE_AUDIT.md`.

Thus theorem-level absolute irreducibility remains open precisely at a noncircular elimination of this one quadratic character. The remaining viable routes are an exact Selmer calculation plus exclusion of the split case, a matching integral Hilbert Eisenstein theorem, or a reducible-compatible exact-level modularity theorem.