# Local analysis of the level-2025 form e

## Goal

Analyze the residual congruence with the Hilbert newform

    2.2.5.1-2025.1-e

in the special branch `7 | A` (`t=infinity`).  The earlier split-CM ordinarity
argument is invalid here: although `q` splits in the quadratic CM extension,
the rational prime 7 is inert in `F`, and the recorded local polynomial has
slope pair `(1,1)`.  A higher-order finite-Honda comparison is still required.

## 1. Local field and finite-flat uniqueness range

The rational prime 7 is inert in `F`, hence

    F_q / Q_7

is unramified of residue degree 2 and absolute ramification index

    e(F_q)=1 < 7-1.

The Frey representation is finite at `q` by the local theorem already used in
level lowering.  The representation attached to the weight-2 form `e` is also
Barsotti--Tate/finite flat at `q`, since `q` does not divide its prime-to-7
level 2025.

In the range `e<p-1`, Raynaud's full-faithfulness theorem for finite flat
commutative group schemes killed by `p` says that morphisms are determined by
their generic fibres.  Consequently, an isomorphism of the two generic-fibre
mod-7 representations extends uniquely to an isomorphism of their finite-flat
models.

### Exact reference

Use B. Conrad, *Finite group schemes over bases with low ramification*, Lemma
4.1.  For `e<p-1` it states that the generic-fibre functor on finite flat
commutative `p`-power order group schemes is exact and fully faithful.  Since
`e(F_q)=1<6`, an isomorphism of generic fibres therefore extends uniquely to
an isomorphism of finite-flat models.

## 2. Frey side in the infinity disk

The normalized integral model is

    Y^2 = 45v^2X^6 - 108*7^a*v^2X^5 + 90vX^3 + 9,

where `a>=1` and `v` is a 7-adic unit.  Its special fibre is

    Y^2 = 45v^2X^6 + 90vX^3 + 9.

The Cartier--Manin matrix is identically zero:

    M_infinity(v)=0.

Thus the special-fibre Jacobian has

    p-rank = 0,
    a-number = 2.

In particular its 7-torsion finite flat group scheme has no nonzero etale
quotient after base change to an algebraic closure of the residue field.  Any
`O_F/7`-linear direct constituent is therefore nonordinary: an ordinary
rank-two constituent would contain an etale factor of rank 7 (equivalently,
an unramified one-dimensional quotient on the generic fibre), forcing positive
p-rank.

The point requiring explicit wording in the final proof is that the RM
`O_F/7`-action decomposes the relevant Dieudonne module compatibly with the
GL(2)-type residual constituent.  Since `O_F/7 = F_49` is a field, a nonzero
ordinary constituent would contribute a nonzero etale `F_49`-subquotient and
hence positive p-rank to the full Jacobian.  This contradicts `p-rank=0`.

## 3. CM side for form e

The Hecke-zero pattern identifies the CM quadratic extension as

    K_e = F(sqrt(-3)).

At `q|7`, `-3` is a square in `F_49`, so `q` splits in `K_e/F`.  This splitting
alone does not imply ordinarity for the two-dimensional representation over
`F_q`, because 7 is inert in `F/Q`.  The cached coefficient is

    a_q(e) = -14,

and the local polynomial is

    X^2 + 14X + 49 = (X+7)^2.

Thus both Newton slopes are 1.  The form is nonordinary at `q`, so p-rank alone
does not separate it from the infinity-disk Frey model.

### Citation obligation

Quote the standard local CM induction statement: at a prime split in the CM
quadratic extension, the associated weight-2 CM representation is ordinary;
at an inert prime it is supersingular/niveau two.  An explicit proof can also
be given directly by restricting the induced representation to the local
decomposition group.

## 4. Remaining comparison

The exact mod-7 branch sieve eliminates `e` in the generic, `t=0`, and
multiplicative branches, but the infinity branch survives at every tested
auxiliary prime.  The remaining task is therefore a first-order/mod-49
comparison between the normalized infinity family

    Y^2 = 45v^2X^6 - 108*7^a*v^2X^5 + 90vX^3 + 9

and the explicit CM elliptic system attached to `e`.

The special fibre has Cartier--Manin matrix zero, but this BT1 datum is too
coarse.  One must compute a higher-order finite-Honda invariant, analogous to
the divided-Frobenius calculation used for `h,l`, and show that the coefficient
of the first nontrivial deformation term cannot match the CM model.

## Status

Form `e` is not yet eliminated in the infinity disk.  The old ordinary versus
nonordinary argument must not be used.  The remaining gap is precise and local:
a mod-49 filtered-Frobenius or equivalent Honda comparison.