# Divided-Frobenius elimination of h,l in the infinity disk

## 1. Normalized infinity family

Let `p=7`.  After the infinity-disk normalization, the genus-2 curve is

    C_{a,v}: Y^2 = 45v^2X^6 - 108*7^a*v^2X^5 + 90vX^3 + 9,

where `a>=1` and `v` is a 7-adic unit.  Modulo `49`, the first-order case is
`a=1`; for `a>=2` the `X^5` term vanishes.  The computation below is made for
all residue classes `v mod 7`; the same lower-left divided block is unchanged
by the second 7-adic digit of `v`, and the companion q-trace enumeration checks
both `a=1` and `a>=2`.

## 2. The even-degree PARI space and the proper curve

For an even sextic, `hyperellpadicfrobenius` returns the Frobenius matrix in the
ordered differential basis

    e_1=dX/(2Y), e_2=X dX/(2Y), ..., e_5=X^4 dX/(2Y).

This is the five-dimensional minus part of the affine
Monsky--Washnitzer cohomology.  The proper genus-2 cohomology has dimension
four.  The missing condition is the residue at the two points at infinity.

Write `t=1/X`.  Since `Y ~ +/- sqrt(45)v t^{-3}`, one has

    X^i dX/Y ~ const * t^{1-i} dt.

Only `i=2` has a residue.  Therefore the residue map is, up to a unit, the
coefficient of `e_3`, and the proper cohomology lattice is

    D = ker(res) = <e_1,e_2,e_4,e_5>.

This is also visible directly in every computed matrix: row 3 has zero entries
in columns 1,2,4,5, so `D` is Frobenius-stable.  The entry in position `(3,3)`
is `42=-7 mod 49`, the redundant boundary eigenvalue.  Thus no noncanonical
quotient by a guessed eigenline is being used: the four-dimensional proper
submodule is the integral kernel of the residue map.

The general even-degree cohomological explanation is given by Michael C.
Harrison, "An extension of Kedlaya's algorithm for hyperelliptic curves",
arXiv:1006.4206, especially the introduction, Lemma 3.1, and the even-degree
analysis.  Harrison explains that the affine odd part contains one redundant
boundary eigenvalue which must be removed to recover the numerator of the
proper curve's zeta function.

## 3. Hodge filtration

For a smooth genus-2 sextic, the regular differentials are

    Fil^1 D = H^0(C,Omega^1) = <e_1,e_2>.

Choose the integral complement `<e_4,e_5>`.  Since the Cartier--Manin matrix of
the infinity special fibre is zero, crystalline Frobenius maps `Fil^1 D` into
`7D`.  Hence the intrinsic divided-Frobenius map is

    delta: Fil^1 D/7 -> (D/Fil^1 D)/7,
    delta(x) = Phi(x)/7 mod (7,Fil^1).

In the ordered proper basis `(e_1,e_2,e_4,e_5)`, its matrix is obtained from
rows 4,5 and columns 1,2 of the PARI matrix, divided by 7 and reduced modulo 7.
Its rank is invariant under integral filtered basis changes.

## 4. Exact computation

The matrix computation is produced by

    scripts/p7_infinity_filtered_frobenius.gp

and audited by

    scripts/p7_infinity_quotient_divided_rank.py.

For `v=1,...,6` the proper divided blocks are

    v=1: [[4,0],[0,3]],
    v=2: [[2,0],[0,3]],
    v=3: [[6,0],[0,4]],
    v=4: [[1,0],[0,3]],
    v=5: [[5,0],[0,4]],
    v=6: [[3,0],[0,4]].

Every block is invertible modulo 7.  Therefore

    rank(delta_infinity)=2

for every infinity residue class.

## 5. Comparison with the CM forms h,l

The explicit CM model

    C_CM: y^2=x^5-1

has, by `scripts/p7_filtered_frobenius.gp` and
`scripts/p7_divided_frobenius_rank.py`,

    delta_CM = [[0,0],[0,2]],
    rank(delta_CM)=1.

The forms `2025.1-h` and `2025.1-l` have the same quartic CM field and weight-2
CM infinity type as this model.  Their quotient Hecke characters are finite
order and unramified at the prime above 7.  An unramified unit twist preserves
the Hodge filtration and multiplies/conjugates the Frobenius-labelled blocks by
units, so it preserves `rank(delta)`.  This is recorded in
`P7_HL_UNRAMIFIED_CM_TWIST.md`.

Consequently

    rank(delta_h)=rank(delta_l)=1,

whereas every normalized infinity Frey lift has rank 2.

## 6. Finite-flat conclusion

The local field is unramified over `Q_7`, and the Hodge--Tate weights are
`{0,1}`, inside the Fontaine--Laffaille range.  Conrad's low-ramification
finite-Honda full-faithfulness theorem applies because `e=1<p-1=6`.
An isomorphism of finite-flat residual representations would induce an
isomorphism of the filtered Honda modules and preserve the rank of `delta`.
The equality is impossible because

    2 != 1.

Therefore the forms `h,l` are eliminated in the infinity disk.

## 7. Reproducibility and scope

The computational assertion is completely local and reproducible from the
PARI matrices modulo 49.  The only external structural inputs are:

1. the residue exact sequence/even-degree boundary line for hyperelliptic
   Monsky--Washnitzer cohomology;
2. finite-Honda full faithfulness in low ramification;
3. the standard finite-order unramified-twist lemma for CM Hecke characters.

This supplies the previously missing final candidate/branch comparison at
level `(2,2)`, norm 2025.