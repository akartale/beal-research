# Intrinsicness of the normalized q-Frobenius trace

## Purpose

This note closes the two formal checks left in
`P7_FORM_E_NORMALIZED_QFROBENIUS.md`:

1. why `Tr(Phi_7^2/7) mod 7` is determined by the finite-flat 7-torsion
   Fontaine--Laffaille module when the Hasse--Witt matrix is zero;
2. why the form `e` contributes `2*a_q(e)/7` on the four-dimensional
   restriction-of-scalars representation.

Throughout, `W=W(F_49)`, `p=7`, and `sigma` is Witt Frobenius.

## 1. The block formula

Let `(M,Fil^1 M,Phi)` be a weight-{0,1} strongly divisible module over `W`,
with `M` free of rank 4 and `Fil^1 M` a direct summand of rank 2.  Choose a
splitting

    M = N direct_sum L,       L = Fil^1 M.

Because `Phi(L) subset pM`, the sigma-semilinear p-Frobenius has block matrix

               [ A   pB ]
    Phi      = [        ]
               [ C   pD ]

relative to `N direct_sum L`.  The torsion Fontaine--Laffaille module `M/pM`
records exactly

- `A mod p` and `C mod p`, from `Phi_0` on `N`;
- `B mod p` and `D mod p`, from the divided map `Phi_1=Phi/p` on `L`.

Since the residue degree is two, linear q-Frobenius is

    Psi = Phi^(sigma) Phi.

Its diagonal blocks are

    Psi_NN = A^(sigma) A + p B^(sigma) C,
    Psi_LL = p C^(sigma) B + p^2 D^(sigma) D.

Therefore

    Tr(Psi)/p
      = Tr(A^(sigma)A/p)
        + Tr(B^(sigma)C)
        + Tr(C^(sigma)B)
        + p Tr(D^(sigma)D).

## 2. Vanishing Hasse--Witt block

The Hasse--Witt operator on `M/Fil^1 M` is represented by `A mod p`.
For the normalized infinity special fibre its Cartier--Manin matrix is zero,
so

    A = p A_1.

Consequently

    Tr(A^(sigma)A/p) is divisible by p,

and the last term in the block formula is also divisible by p.  Hence

    tau(M)
      := Tr(Psi/p) mod p
       = Tr(B^(sigma)C + C^(sigma)B) mod p.

The right-hand side uses only the torsion Fontaine--Laffaille maps
`Phi_0 mod p` and `Phi_1 mod p`.  It is therefore intrinsic to the finite-flat
7-torsion group scheme.  A change of splitting changes the four blocks but not
the left-hand side, so the displayed expression is merely a coordinate formula
for an intrinsic trace.

Thus an isomorphism of finite-flat 7-torsion models forces equality of `tau`.
No level-49 group scheme and no lift of the residual representation is needed.

## 3. Computing tau from the genus-2 Weil polynomial

Let the degree-four p-Frobenius polynomial be

    P(T)=T^4+c1*T^3+c2*T^2+p*c1*T+p^2.

Then

    Tr(Phi^2)=c1^2-2*c2.

In the infinity family `c1=0`, so

    tau = -2*c2/p mod p.

The exact PARI computations give

    c2 = 7       => tau = -2 = 5 mod 7,
    c2 = -14     => tau =  4 mod 7.

This recovers the set `{4,5}` without referring to a basis of crystalline
cohomology.  The extra `-7` eigenline returned by PARI for an even-degree
sextic contributes `49` to `Tr(Phi^2)`, hence zero after division by 7 modulo
7; equivalently one may divide the degree-five polynomial by `T+7` first.

## 4. Restriction of scalars for form e

Let `K=F_q`, the unramified quadratic extension of `Q_7`.  The Hilbert modular
representation attached to `e` is two-dimensional over `K`, and q-Frobenius
has polynomial

    T^2-a_q(e)T+49.

Viewed as a four-dimensional `Q_7`-representation by restriction of scalars,
the trace of a `K`-linear operator is the field trace of its `K`-linear trace:

    Tr_Q7(Res_{K/Q7}(Frob_q)) = Tr_{K/Q7}(a_q(e)).

Here `a_q(e)=-14` is rational, hence fixed by the nontrivial automorphism of
`K/Q_7`.  Therefore

    Tr_Q7 = 2*(-14) = -28,
    tau(e) = -28/7 = -4 = 3 mod 7.

Equivalently, the four-dimensional characteristic polynomial is

    Norm_{K/Q7}(T^2+14T+49) = (T^2+14T+49)^2.

## 5. Local contradiction

For every infinity parameter,

    tau(Frey) is in {4,5},

whereas

    tau(e)=3.

If the residual representations were isomorphic, low-ramification full
faithfulness would identify their finite-flat 7-torsion models, hence their
torsion Fontaine--Laffaille modules, and therefore their intrinsic `tau`
invariants.  The unequal values give a contradiction.

Thus form `e` is eliminated in the infinity branch, subject only to the same
standard finite-flat/full-faithfulness input already used elsewhere in the
local argument.