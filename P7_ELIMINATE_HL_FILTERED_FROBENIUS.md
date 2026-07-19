# Filtered-Frobenius separation of the CM forms h,l

## Open-source CM model

The Bouyer--Streng open-source data repository

    upstream/mstreng-reduce

contains in table `data/1a` the entry

    [5,5,5], ..., [[-1],[0],[0],[0],[0],[1]].

By the table format, this is the curve

    C_CM: y^2 = x^5 - 1

with CM by the cyclic quartic field

    K = Q[z]/(z^4+5z^2+5).

This is the CM field reconstructed from the Hecke-zero patterns of the forms
`2025.1-h` and `2025.1-l`.  The two forms correspond to the two coefficient/RM
embeddings of the same CM isogeny datum; the underlying principally polarized
CM genus-2 curve is represented by `C_CM`.

## Direct modulo-49 curve comparison

The script

    scripts/p7_compare_cm_x5_minus1.py

performs exact binary-sextic equivalence over `Z/49Z`.  It tests every residue
class in `GL_2(F_7)` and solves the five first-order lift parameters linearly.
For every unit `u mod 49`, it compares `C_CM` with

    C_u: y^2 = -108x^5 + 42u x^3 + 9u^2.

The result is

    u mod 7 = 1,2,3,4,5,6: no matching lift modulo 49.

This proves that the CM curve and all Frey lifts are distinct as polarized
curves modulo 49.  By itself this is not yet the finite-flat Galois statement,
because distinct abelian-scheme lifts can in principle have isomorphic
p-torsion.

## PARI crystalline Frobenius

PARI/GP provides the open-source Kedlaya implementation

    hyperellpadicfrobenius(Q,7,2).

The script

    scripts/p7_filtered_frobenius.gp

computes Frobenius to precision `7^2` in the standard odd-degree basis

    omega, x omega, x^2 omega, x^3 omega,
    omega=dx/(2y).

For genus 2 the Hodge filtration `Fil^1` is spanned by the first two basis
vectors.

All seven curves have characteristic polynomial

    X^4 + 49,

so the ordinary local zeta polynomial does not distinguish them.

## Divided-Frobenius invariant

Because Frobenius maps `Fil^1` into `7D`, define

    delta: Fil^1/7 -> (D/Fil^1)/7

by taking the lower-left `2x2` block of the Frobenius matrix, dividing by 7,
and reducing modulo 7.

The script

    scripts/p7_divided_frobenius_rank.py

certifies:

    C_CM: rank(delta)=1,

whereas

    C_u: rank(delta)=2

for every `u=1,...,6`.

The explicit blocks are

    CM      [[0,0],[0,2]],
    Frey 1  [[6,0],[0,3]],
    Frey 2  [[6,0],[0,6]],
    Frey 3  [[1,0],[0,5]],
    Frey 4  [[6,0],[0,5]],
    Frey 5  [[1,0],[0,6]],
    Frey 6  [[1,0],[0,3]].

Rank is unchanged under integral basis changes preserving the Hodge
filtration.  Hence the filtered Frobenius modules of the CM lift and every
Frey lift are nonisomorphic.

## Fontaine--Laffaille consequence

The local field `F_q/Q_7` is unramified and the Hodge--Tate weights are
`{0,1}`, contained in the Fontaine--Laffaille range `[0,p-2]` for `p=7`.
Fontaine--Laffaille/finite-Honda theory classifies the corresponding finite
flat 7-torsion using filtered Frobenius modules and is fully faithful in this
range.

Therefore an isomorphism of the finite-flat residual representations would
force an isomorphism of the filtered modules and preserve `rank(delta)`.  The
computed ranks `1` and `2` contradict this.

The required classification and basis checks are now explicit.  Conrad,
*Finite group schemes over bases with low ramification*, Theorem 3.6 gives the
fully faithful and essentially surjective finite-Honda functor for `e<p-1`.
The official PARI descriptor and implementation imported in `upstream/pari`
fix the cohomology basis and column convention; the source loop uses the full
ordered basis `x^i dx/(2y)`, `0<=i<=2g-1`.  See
`P7_REFERENCE_AND_SOURCE_AUDIT.md` for the exact audit.

The explicit Euler-factor check shows that `Jac(y^2=x^5-1)` is not literally
the global compatible system `h/l`.  The correct statement is that all three
systems have the same CM field and weight-2 infinity type, so the h/l Hecke
characters differ from the explicit curve's character by finite-order twists.
These twists are unramified at 7 because both systems have good reduction and
prime-to-7 conductor there.  Unramified unit twists preserve the rank of the
divided-Frobenius map.  See `P7_HL_UNRAMIFIED_CM_TWIST.md`.

With that correction, the rank contradiction eliminates both surviving CM
forms

    2025.1-h,
    2025.1-l.

No Sage, Magma, or AFUCH computation is required.

## Correct global-to-local bridge

The Euler-factor comparison in `scripts/identify_cm_curve_hl_euler.py` rules
out literal equality of the global compatible systems.  What is needed, and
what suffices locally, is the finite-order unramified-twist relation proved in
`P7_HL_UNRAMIFIED_CM_TWIST.md`.  The remaining manuscript task is only to add a
standard citation for the fact that equal infinity type implies finite-order
quotient of algebraic Hecke characters; no further CM model computation is
required.