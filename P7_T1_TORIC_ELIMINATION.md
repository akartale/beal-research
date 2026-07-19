# Toric elimination of e, h, and l in the t=1 branch

## 1. Special fibre

At `t=1`, the reduced sextic is

    f(x)=5x^6+2x^5+3x^3+1 in F_7[x].

The exact script

    scripts/p7_t1_stable_reduction.py

computes

    gcd(f,f') = x^2+6x+6,
    f = (x^2+6x+6)^2 (5x^2+5x+1).

The quadratic node polynomial `g=x^2+6x+6` is irreducible over `F_7`.
Hence the geometric special fibre has two conjugate ordinary double points,
while its normalization is

    z^2=5x^2+5x+1,

which has genus zero.  The generalized Jacobian therefore has no abelian part
and toric rank two.

## 2. The nodes are genuinely smoothed by t-1

For

    F_t(x)=45x^6-108x^5+90t*x^3+9t^2,

one has at `t=1`

    dF_t/dt = 90x^3+18 = 6x^3+4 mod 7.

Reduction modulo the node polynomial gives

    (dF_t/dt) mod g = 3+5x,

which is nonzero in `F_49=F_7[x]/(g)`.  Therefore `t-1` is a first-order
smoothing parameter at each of the two conjugate nodes.  In particular the
stable Jacobian is genuinely totally toric of rank two, not a degeneration
with a hidden positive-dimensional abelian normalization.

For the Diophantine specialization,

    t=-B^5/A^3,
    t-1=-(A^3+B^5)/A^3=-C^7/A^3

(up to the harmless sign convention for `t`).  Thus the branch `t=1 mod 7`
is exactly the branch `7|C`, with `A,B` units.

## 3. Cyclotomic submodule on the Frey side

Let `J` be the genus-2 Frey Jacobian over the local field at 7.  For a
semistable abelian variety with toric rank two, Raynaud uniformization gives a
canonical exact sequence on p-adic Tate modules whose toric part is

    X_*(T) tensor Z_7(1)  subset  T_7(J),

where `X_*(T)` has rank two.  Reducing modulo 7 gives a nonzero
Galois-stable cyclotomic submodule

    X_*(T)/7 tensor F_7(1)  subset  J[7](Kbar).

After the unramified quadratic base change that splits the two conjugate
nodes, this contains two copies of the cyclotomic character.  Descent may
permute the two copies, but it cannot remove the multiplicative-type
submodule.  Equivalently, the generic 7-torsion contains the generic fibre of
a nonzero multiplicative finite flat group scheme of type `mu_7` after a
finite unramified extension.

No assertion that the full extension is split is needed.

## 4. Nonordinary type of e, h, and l

At the unique prime `q|7` of norm 49, the three surviving forms have

    a_q(e)=-14,
    a_q(h)=a_q(l)=0.

Their local q-Frobenius polynomials have no unit root: for `e` it is
`(T+7)^2`, while for `h,l` it is `T^2+49`.  Thus all p-Frobenius slopes are
`1/2` (equivalently all q-Frobenius slopes are `1`).  Their finite-flat
7-torsion modules have no nonzero etale or multiplicative subquotient.  In
particular none contains a subgroup of type `mu_7` after unramified base
change.

For `h,l` this is the same supersingular local type used in the
filtered-Frobenius analysis of the `t=0` branch.

## 5. Contradiction

Assume that the residual Frey representation in the `t=1` branch is
isomorphic to that of `e`, `h`, or `l`.

The target representation is finite flat at 7.  The cyclotomic submodule of
the toric Frey representation gives a generic-fibre morphism from `mu_7` into
the target finite-flat model after unramified base change.  Since the absolute
ramification index is `1<7-1`, low-ramification full faithfulness extends this
morphism to finite-flat group schemes.  Its generic injectivity and exactness
force a nonzero multiplicative subgroup in the finite-flat model of the
candidate form.

That contradicts its nonordinary slope-one q-Frobenius type.

Therefore none of `e,h,l` can occur in the `t=1` branch.

## Status

The computational inputs are exact and reproduced by
`scripts/p7_t1_stable_reduction.py`.  The only external theorem used is the
standard toric part of Raynaud uniformization together with the same
low-ramification full-faithfulness theorem already cited in the other local
branches.