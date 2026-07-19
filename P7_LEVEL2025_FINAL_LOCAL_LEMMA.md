# Final local elimination lemma for the three level-2025 survivors

## Statement

Let `q` be the unique prime of `F=Q(sqrt(5))` above 7.  For every 7-adic
residue branch arising from a primitive solution, the residual Frey
representation is not isomorphic to any of

    2.2.5.1-2025.1-e,
    2.2.5.1-2025.1-h,
    2.2.5.1-2025.1-l.

The branches are exhaustive: `t=0`, `t=infinity`, `t=1`, and the smooth unit
classes `t mod 7 in {2,3,4,5,6}`.  Form `e` in the `t=0` branch is eliminated
by the reproducible auxiliary-prime calculation in
`scripts/p7_form_e_exact_branches.py`; all remaining comparisons are local at
7 and are recorded below.  Consequently level `(2,2)`, norm 2025, is locally
eliminated.

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

The earlier split-CM ordinarity argument is invalid and is not used.  The
correct invariant is

    tau = Tr(Phi_7^2/7) mod 7.

The infinity special fibre has zero Hasse--Witt matrix.  In a Hodge-adapted
block matrix this makes

    tau = Tr(B^(sigma)C + C^(sigma)B) mod 7,

so `tau` is intrinsic to the torsion Fontaine--Laffaille module.  The exact
modulo-49 computation gives

    tau(Frey) in {4,5}

for every unit `v mod 49` and every `a>=1`.  For form `e`,

    a_q(e)=-14,

and restriction of scalars gives

    tau(e)=Tr_{F_q/Q_7}(-14)/7=-28/7=3 mod 7.

Thus the finite-flat modules cannot be isomorphic.  See
`P7_FORM_E_NORMALIZED_QFROBENIUS.md` and
`P7_FORM_E_QFROBENIUS_INTRINSICNESS.md`.

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

## 5. Smooth unit classes

For `t mod 7 in {2,3,4,5,6}`, the reduced genus-2 curve is smooth and its
Hasse--Witt matrix is invertible.  Hence the Frey Jacobian is ordinary.  The
three candidate forms are nonordinary at `q`: `e` has polynomial `(T+7)^2`
and `h,l` have polynomial `T^2+49`.  Therefore none can occur in a smooth unit
class.

## 6. The t=1 branch

At `t=1`, the reduced sextic factors as

    (x^2+6x+6)^2 (5x^2+5x+1).

The normalization has genus zero and the two conjugate nodes are smoothed to
first order by `t-1`; hence the stable Jacobian is totally toric of rank two.
Raynaud uniformization supplies a nonzero cyclotomic submodule in the residual
Tate module.  None of `e,h,l` has a multiplicative subquotient, since all three
are nonordinary.  Low-ramification full faithfulness gives the contradiction.
See `P7_T1_TORIC_ELIMINATION.md`.

## 7. Elimination of h and l in the infinity disk

For the normalized infinity sextic, PARI returns the five-dimensional
even-degree Monsky--Washnitzer space with ordered basis

    e_i=X^(i-1)dX/(2Y), 1<=i<=5.

At the two points at infinity, only `e_3` has nonzero residue.  Hence the proper
genus-2 crystalline lattice is the Frobenius-stable kernel

    D=<e_1,e_2,e_4,e_5>.

Its Hodge filtration is `<e_1,e_2>`.  Dividing the lower-left Frobenius block
by 7 and reducing modulo 7 gives rank 2 for all six infinity unit classes.  The
explicit CM model for `h,l` has rank 1, and the local unramified-twist lemma
preserves this rank.  Low-ramification finite-Honda full faithfulness therefore
rules out both forms.  The complete residue calculation and matrices are in
`P7_INFINITY_HL_DIVIDED_FROBENIUS.md` and
`scripts/p7_infinity_quotient_divided_rank.py`.

## 8. Conclusion and verified dependencies

The exact auxiliary-prime sieve eliminates `e` at `t=0`, and Sections 2--7
eliminate all remaining candidate/branch pairs.  Thus level `(2,2)`, norm
2025, is locally closed.

The proof depends on:

The verified eliminations depend on:

1. the normalized branch models and their Hasse--Witt/stable-reduction data;
2. Conrad Lemma 4.1 and Theorem 3.6 in the range `e=1<6`;
3. the local unramified-twist lemma for `h,l` in the `t=0` comparison;
4. the audited PARI/Kedlaya Frobenius matrices modulo 49;
5. the standard toric part of Raynaud uniformization.

They do not depend on Sage, Magma, AFUCH, a literal global identification of
`Jac(y^2=x^5-1)` with `h/l`, or the invalid split-CM ordinarity claim for `e`.
This lemma closes only level 2025; the other Step-IV levels remain open.