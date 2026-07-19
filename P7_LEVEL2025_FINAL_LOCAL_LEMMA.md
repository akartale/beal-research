# Final local elimination lemma for the three level-2025 survivors

## Statement

Let `q` be the unique prime of `F=Q(sqrt(5))` above 7.  In either special
7-adic disk arising from a primitive solution, the residual Frey
representation is not isomorphic to any of

    2.2.5.1-2025.1-e,
    2.2.5.1-2025.1-h,
    2.2.5.1-2025.1-l.

Consequently these three forms are eliminated in the two special disks.  This statement does not by itself treat the generic unit disk `t in Z_7^*`.

## 1. Finite-flat comparison

The extension `F_q/Q_7` is unramified, hence its absolute ramification index is
`e=1<7-1`.  Both the Frey representation and the representations attached to
parallel-weight-2 forms of prime-to-7 level are finite flat at `q`.

By Conrad, *Finite group schemes over bases with low ramification*, Lemma 4.1,
the generic-fibre functor on finite flat commutative 7-primary group schemes is
fully faithful.  Therefore an isomorphism of residual generic-fibre
representations would extend uniquely to an isomorphism of finite-flat models.
Equivalently, by Conrad Theorem 3.6, their finite Honda systems would be
isomorphic.

## 2. Elimination of e in the infinity disk

In the infinity disk the normalized Frey curve has Cartier--Manin matrix zero.
Its special-fibre Jacobian therefore has p-rank zero and a-number two.  Its
finite-flat 7-torsion has no nonzero etale quotient.

The form `e` has CM by

    K_e=F(sqrt(-3)),

and `q` splits in `K_e/F`.  Locally,

    K_e tensor_F F_q = F_q x F_q,

so the CM representation is a sum of two crystalline characters.  Their
labelled Hodge--Tate weights are 0 and 1.  A crystalline character of weight
zero over an unramified p-adic field is unramified.  Hence one summand is an
unramified unit-root line and the other is its cyclotomic partner.  The
finite-flat model is ordinary and has a nonzero etale quotient.

Thus the finite-flat models of the Frey representation and `e` cannot be
isomorphic.  This eliminates `e`.

## 3. A local unramified-twist lemma

Let `L/F_q` be the unramified quadratic extension.  Let

    V_i = Ind_{G_L}^{G_{F_q}} chi_i,  i=1,2,

where `chi_i` are crystalline characters with the same labelled Hodge--Tate
weights.  Then `eta=chi_2/chi_1` is crystalline with all labelled
Hodge--Tate weights zero.  A rank-one crystalline representation of weight zero
is unramified.  Therefore `V_2` is obtained from `V_1` by an unramified unit
twist on the Frobenius-labelled components.

On a filtered Frobenius module an unramified unit twist leaves the filtration
unchanged and multiplies Frobenius by invertible scalars.  Consequently the
rank of

    delta: Fil^1/7 -> (D/Fil^1)/7,
    delta(x)=phi(x)/7 mod (7,Fil^1),

is invariant under such a twist.

This is a local statement; no literal global identification of compatible
systems and no global finite-order Hecke-character quotient are required.

## 4. Elimination of h and l in the t=0 disk

The forms `h,l` have CM by the same cyclic quartic field

    K=Q[z]/(z^4+5z^2+5)=Q(zeta_5),

viewed as a quadratic CM extension of `F`.  The prime `q` is inert in `K/F`, so
`K_q/F_q` is the unramified quadratic extension.  Their local representations
are crystalline CM inductions with Hodge--Tate weights `{0,1}`.

The explicit CM curve

    C_CM: y^2=x^5-1

has CM by the same field and supplies one such local crystalline induction.
By the local lemma, the local systems of `h` and `l` differ from this model only
by unramified unit twists as far as their filtered Frobenius modules are
concerned.  Hence they have the same divided-Frobenius rank.

PARI/GP `hyperellpadicfrobenius(Q,7,2)`, audited against the official PARI
source, gives

    rank(delta_CM)=1.

For the six normalized first-order Frey classes in the t=0 disk, indexed by
`u in F_7^*`, the same computation gives

    rank(delta_Frey,u)=2.

The scripts

    scripts/p7_filtered_frobenius.gp
    scripts/p7_divided_frobenius_rank.py

record the matrices and certify these ranks.  Since rank(delta) is an
isomorphism invariant of the finite Honda system, no Frey finite-flat model is
isomorphic to the model attached to `h` or `l`.

Thus `h` and `l` are eliminated.

## 5. Conclusion and dependencies

The complete standard sieve at level 2025 leaves exactly `e,h,l`; the arguments above eliminate them whenever the solution parameter lies in the special disks `t=0` or `t=infinity`.  A separate residual test is still required for the generic unit disk.  The result depends only on:

1. the normalized special-disk models and their Cartier--Manin matrices;
2. Conrad Lemma 4.1 and Theorem 3.6 in the range `e=1<6`;
3. the elementary rank-one crystalline fact: weight zero implies unramified;
4. the audited PARI/Kedlaya Frobenius matrices modulo 49.

It does not depend on Sage, Magma, AFUCH, a literal global identification of
`Jac(y^2=x^5-1)` with `h/l`, or a global finite-order twist assertion.