# Reference and source audit for the p=7 local elimination

## 1. Finite-flat uniqueness from the generic fibre

Let `A_0=O_{F_q}`.  Here `F_q/Q_7` is unramified, so the absolute
ramification index is

    e(A_0)=1<7-1.

Brian Conrad, *Finite group schemes over bases with low ramification*, Lemma
4.1, states that for `e<p-1` the generic-fibre functor from finite flat
commutative `p`-power order group schemes over `A_0` to finite commutative
group schemes over its fraction field is fully faithful and exact.  In
particular, two finite-flat models with isomorphic generic fibres are uniquely
isomorphic.

This is the exact reference needed in the elimination of form `e`; no vague
appeal to a uniqueness principle is necessary.

## 2. Finite Honda classification

In the same paper, Theorem 3.6 states that the contravariant functor

    LM_{A_0}: FF_{A_0} -> SH^f_{A_0}

is fully faithful and essentially surjective when `e<p-1`.  Since `p=7` and
`e=1`, finite flat 7-primary group schemes are therefore classified by their
finite Honda systems.  The unramified case recovers Fontaine's original
classification.

For the present proof this implies:

- an isomorphism of finite-flat `J[7]` group schemes induces an isomorphism of
  their finite Honda systems;
- any rank computed from a functorially defined map in the filtered Honda
  system is an isomorphism invariant.

## 3. PARI basis audit

The official PARI source tree has been imported at

    upstream/pari.

The function descriptor

    src/functions/elliptic_curves/hyperellpadicfrobenius

states that the routine returns the Frobenius matrix on crystalline/de Rham
cohomology for the model `y^2=Q(x)`, with `omega=dx/(2y)`.  The prose line in
that descriptor truncates the displayed basis at `x^(g-1) omega`; however, the
returned matrix is `2g x 2g`, and the implementation in

    src/basemath/hyperell.c

constructs columns for `i=1,...,d-1`.  For odd degree `d=2g+1`, this is the
ordered basis

    omega, x omega, ..., x^(2g-1) omega.

This agrees with Kedlaya's standard Monsky--Washnitzer/de Rham basis

    x^i dx/(2y),  i=0,...,2g-1.

For genus 2, the Hodge subspace of holomorphic differentials is the span of

    omega, x omega,

which are therefore the first two basis vectors.  The PARI matrix is stored by
columns: the source loop places the reduced Frobenius image of the `i`-th basis
vector in column `i`.  Hence the lower-left `2 x 2` block is exactly the map
from `Fil^1` to the quotient in this ordered basis.

## 4. Divided Frobenius as a Honda invariant

For all curves under consideration the computed Frobenius matrix satisfies

    phi(Fil^1) subset 7D.

Thus the map

    delta: Fil^1/7 -> (D/Fil^1)/7,
    delta(x) = phi(x)/7 mod (Fil^1,7)

is defined.  It is functorial under isomorphisms of filtered Frobenius/Honda
modules, so its rank is invariant.

The certified values are

    rank(delta_CM)=1,
    rank(delta_Frey,u)=2 for every u in F_7^*.

Therefore the finite Honda systems, and hence the finite-flat 7-torsion group
schemes, are nonisomorphic.

## 5. Citations to use in the final manuscript

1. B. Conrad, *Finite group schemes over bases with low ramification*,
   Lemma 4.1: exact and fully faithful generic-fibre functor for `e<p-1`.
2. Ibid., Theorem 3.6: full faithfulness and essential surjectivity of the
   finite Honda-system functor for `e<p-1`.
3. K. Kedlaya, description of the hyperelliptic cohomology basis
   `x^i dx/(2y)`, `0<=i<=2g-1`, in the direct cohomological method.
4. Official PARI source files listed above, fixing matrix ordering and column
   convention for `hyperellpadicfrobenius`.

## 6. Corrected global-to-local check

A direct Euler-factor comparison shows that `Jac(y^2=x^5-1)` is not literally
the global compatible system represented by `h,l`.  The correct bridge is the
finite-order twist statement in `P7_HL_UNRAMIFIED_CM_TWIST.md`: the systems have
the same CM field and infinity type, hence their Hecke characters differ by a
finite-order character, and this character is unramified at 7.  Such a unit
twist preserves the rank of divided Frobenius.  Thus literal global modular
identification is unnecessary.