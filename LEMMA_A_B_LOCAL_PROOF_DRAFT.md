# Lemmas A and B: local finite-flat types and conductor bounds

## Setup

Let K=Q(sqrt(5)), let p7 be the unique prime above 7, and let

    rho_bar : G_K -> GL_2(F_49)

be the residual RM representation attached to the plus Frey motive for a
hypothetical primitive solution of A^3+B^5=C^7. The source paper uses

    (a,b,c)=(B,-C,A), p=7.

The determinant is the mod-7 cyclotomic character and, after the standard Tate
normalization, the p-adic representation has parallel Hodge--Tate weights
{0,1} at both embeddings K_p7 -> Qbar_7.

Theorem `thm:mot-+-prop` of Pacetti--Villagra Torcomian, citing the local
results of their reference [GP], states:

1. rho_bar is unramified outside 3,5,7;
2. rho_bar is finite at p7.

Here `finite at p7` is the finite-flat condition used in level lowering.

## Lemma A — exact tame inertia possibilities

Because 7 is inert in K, the local extension K_p7/Q_7 is unramified of residue
degree 2 and absolute ramification index e=1. Let omega_2 be a fundamental
character of niveau two.

There is no need to lift a chosen `Fbar_7`-stable line as a separate finite-flat subgroup scheme. Regard the residual representation as a finite `F_7`-module and choose a simple Jordan--Hoelder quotient of its generic finite group scheme. Absolute reducibility guarantees that, after extending coefficients, its characters are among the diagonal constituents; a simple factor over `F_7` may have dimension greater than one and acquires a one-dimensional structure over its finite endomorphism field.

Raynaud, `Schemas en groupes de type (p,...,p)`, Corollaire 3.4.4, applies directly to this situation: if a finite commutative `K`-group scheme killed by a power of `p` admits a finite-flat prolongation, then every generic-fibre Jordan--Hoelder quotient is an `F`-vector scheme for a suitable finite field `F`, and its tame character has Raynaud digits bounded by `e`. Thus the categorical generic-fibre/Jordan--Hoelder passage is part of the cited corollary itself.

Conrad, Lemma 4.1, independently confirms that when `e<p-1` the finite-flat category is abelian and the generic-fibre functor is fully faithful and exact. It is useful as a consistency check, but it is not necessary to assume that the chosen absolutely reducible line itself descends to the original coefficient field.  If its endomorphism field is `F=F_(7^r)`, its tame
character has the form

    psi_0^u0 psi_1^u1 ... psi_(r-1)^u_(r-1),
    uj in {0,1},

because the absolute ramification index is `e=1`.  The underlying residual RM
representation has F_7-dimension four, so `r<=4`.

There is one further constraint which is essential here.  Each diagonal
constituent is a one-dimensional character of the full local decomposition
group, not merely of inertia.  Arithmetic Frobenius acts on tame inertia by
raising to the residue-field cardinality `q=49`; scalar-valued characters are
unchanged by conjugation.  Therefore

    theta(tau^49)=theta(tau),

so the Raynaud digit sequence is periodic with period two.  For `r=1,2,3,4`
this forces the character to descend to niveau dividing two.  Writing
`omega_2` for a fundamental character of niveau two gives

    theta = omega_2^(a0 + 7 a1),   a0,a1 in {0,1}.

Thus the only possible exponents are

    0, 1, 7, 8.

This argument also covers absolutely reducible lines defined only over an
extension of F_49; no unjustified F_49-rationality of the stable line is used.

Since det(rho_bar)|I = epsilon_bar_7|I = omega_2^8, the two exponents are
complementary to 8 modulo 48. Up to exchange, the only possible multisets are

    {0,8} and {1,7}.

The first is the ordinary branch; the second is the niveau-two branch.

### Exact citation and hypotheses

The required inertia statement is Raynaud, *Schemas en groupes de type
(p,...,p)*, Bulletin de la Societe Mathematique de France 102 (1974),
Corollaire 3.4.4. That corollary explicitly treats a Jordan--Hoelder quotient of a generic finite group scheme which admits a finite-flat prolongation, so it supplies the previously questioned categorical passage directly. Raynaud's result applies because the local absolute ramification index is `e=1`. Conrad, *Finite group schemes over bases with low ramification*, Lemma 4.1, additionally states that for `e<p-1` the finite-flat category is abelian and generic fibre is fully faithful and exact; this corroborates, rather than replaces, the direct Raynaud application.  Frobenius conjugacy over
the residue field F_49 then forces the Raynaud tame digits to have period two.
This proves Lemma A without invoking a separate Fontaine--Laffaille
labelled-weight theorem or assuming that the stable line is F_49-rational.

## Lemma B — conductor of diagonal characters

Assume absolute reducibility over Fbar_7:

    rho_bar^ss = chi_1 direct_sum chi_2.

### Away from 3,5,7

The source theorem states that rho_bar is unramified at every finite prime not
dividing 3*5*7. Therefore both chi_i are unramified there.

### At 3 and sqrt(5)

The conductor of rho_bar is supported on (3) and (sqrt(5)) after removing p7,
and the source conductor calculation gives exponents

    epsilon_3 in {2,3},
    epsilon_5 in {2,3}.

Artin conductors are additive on direct sums:

    a_q(rho_bar^ss)=a_q(chi_1)+a_q(chi_2).

The required comparison with the possibly non-semisimple representation is

    a_q(rho_bar^ss) <= a_q(rho_bar).

Here is a direct proof.  Let `G_i` be the lower ramification groups of the
finite inertia quotient through which `rho_bar` factors.  For every `i`, the
invariant functor is left exact.  Applying it along a Jordan--Hoelder
filtration of `rho_bar` gives

    dim((rho_bar^ss)^(G_i)) >= dim(rho_bar^(G_i)).

Hence

    codim((rho_bar^ss)^(G_i)) <= codim(rho_bar^(G_i)).

The Artin conductor is a positive weighted sum of these codimensions, so the
inequality follows term by term, including the wild terms.  Consequently each
nonnegative diagonal summand satisfies

    a_(3)(chi_i) <= 3,
    a_(sqrt(5))(chi_i) <= 3.

Therefore the prime-to-7 conductor of each diagonal character divides

    (3)^3 (sqrt(5))^3.

### At p7

Lemma A gives tame characters only. In the ordinary branch {0,8}, one diagonal
character is unramified at p7 and the other is cyclotomic; after choosing chi
to be the unramified constituent, its global ray conductor omits p7.

In the niveau-two branch {1,7}, both diagonal characters are tamely ramified.
A nontrivial tame one-dimensional character has conductor exponent exactly 1.
Thus each diagonal conductor divides one power of p7.

Consequently every diagonal character factors through the ray class group of

    m1=(3)^3 (sqrt(5))^3 p7 infinity_1 infinity_2,

and in the ordinary branch the selected unramified character factors through

    m0=(3)^3 (sqrt(5))^3 infinity_1 infinity_2.

The infinite primes allow both possible signs. They do not impose an
unjustified parity restriction.

## Conditional result and remaining proof obligations

The conductor comparison needed in Lemma B is proved above directly from the
ramification filtration.  Subject to the source conductor exponents and the
finite-flat statement at `p7`, Lemma B is therefore complete.

Lemma A is proved by Raynaud Corollaire 3.4.4 plus Conrad Lemma 4.1, as written
above.  Lemma B is proved subject only to the source paper's stated
finite-flatness and conductor exponents.

The niveau-two local-to-global step is supplied in
`P7_IRREDUCIBILITY_ARGUMENT.md` by the exact ray-class sequence.  The local
group F_49^* of order 48 maps onto the ray kernel of order 24 with kernel
`{+1,-1}`, so every globalized tame exponent is even; this excludes exponents
1 and 7.

Lemma A's finite-flat Jordan--Hoelder passage is closed by the exact statement of Raynaud Corollaire 3.4.4. The branchwise source conductor table has now been verified under `(a,b,c)=(B,-C,A)` in `PRIMITIVE_VALUATION_CONDUCTOR_TABLE.md`; therefore Lemma B is also closed in the current audit.

`LEMMA_C_D_ABSOLUTE_CHARACTERS_AND_L19.md` proves only the good-reduction part of Lemma D at `19`; it must not be cited as a complete proof of the ordinary branch. The full four-branch sieve and the separately audited toric and conductor arguments reduce Lemma D to the single quadratic survivor `(90,0)`. Its noncircular elimination remains open. Accordingly, absolute irreducibility is not claimed here as theorem-level complete.
