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
character of niveau two. Raynaud/Fontaine--Laffaille gives the following for
every one-dimensional Jordan--Hoelder constituent of the restriction to tame
inertia of a finite-flat representation with weights in [0,1]:

    theta = omega_2^(a0 + 7 a1),   a0,a1 in {0,1}.

Thus the only possible exponents are

    0, 1, 7, 8.

Since det(rho_bar)|I = epsilon_bar_7|I = omega_2^8, the two exponents are
complementary to 8 modulo 48. Up to exchange, the only possible multisets are

    {0,8} and {1,7}.

The first is the ordinary branch; the second is the niveau-two branch.

### Citation requirement

For the final paper, cite either Raynaud's Corollaire 3.4.4 in the semistable
finite-flat formulation or a Fontaine--Laffaille/Caruso--Savitt theorem for an
absolutely unramified local field and Hodge--Tate interval of length <=p-2.
The hypotheses here are especially small: e=1, f=2, weights {0,1}, p=7.

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

To use the published conductor bound for `rho_bar`, one also needs the standard inequality

    a_q(rho_bar^ss) <= a_q(rho_bar),

or an equivalent local argument at the primes above 3 and 5. This step must be cited or proved in the final version, especially in the presence of wild inertia. Once this inequality is supplied, each nonnegative summand satisfies

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

Lemma A becomes complete after inserting an exact finite-flat/Raynaud or Fontaine--Laffaille theorem and checking its hypotheses for this Frey representation.

Lemma B additionally requires a cited proof of

    a_q(rho_bar^ss) <= a_q(rho_bar)

at the primes above 3 and 5, or a direct local conductor calculation there.

The niveau-two branch also requires a written local-to-global identification of the order-24 ray kernel with the relevant quotient of the local tame unit group, sufficient to prove that only even `omega_2` exponents globalize.

After these three obligations are discharged, the argument combines with `LEMMA_C_D_ABSOLUTE_CHARACTERS_AND_L19.md` to prove absolute irreducibility of `rho_bar` at `p=7`. This draft does not yet claim that unconditional conclusion.