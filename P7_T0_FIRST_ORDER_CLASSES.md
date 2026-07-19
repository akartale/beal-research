# First-order deformation classes in the t=0 disk

## Normalized lift modulo 49

For the branch `7|B`, write

    t=7^(5b)u,

with `u` a 7-adic unit.  The first nontrivial case is `b=1`.  Modulo 49 the
normalized model is

    C_u: y^2 = -108 x^5 + 42u x^3 + 9u^2.

The term `45*7^2*x^6` vanishes modulo 49.  Therefore the first-order
special-fibre deformation is represented over `F_7` by the binary sextics

    F_u(X,Z) = 4X^5Z + 2u^2Z^6,
    G_u(X,Z) = 6uX^3Z^3.

## Affine classification

The script

    scripts/p7_t0_lifts_mod49.py

classifies the lifts under integral affine hyperelliptic changes

    x=aX+r,
    y=bY.

The coefficient of `X^4` forces `r=0`.  Solving the remaining coefficient
conditions gives six orbits, one for each residue `u mod 7`.  Changing the lift
of `u` modulo 49 does not change the orbit:

    orbit 1: u == 1 mod 7,
    ...
    orbit 6: u == 6 mod 7.

Thus the first-order class depends only on `u mod 7`, but it genuinely retains
all six nonzero residue classes.

## Full first-order GL2 test

The script

    scripts/p7_t0_deformation_gl2.py

checks all `|GL_2(F_7)|=2016` changes of the binary sextic.  It also quotients
by every infinitesimal coordinate correction and y-rescaling.  For a target
special fibre `F_v`, the tangent space used is

    < X F_X, Z F_X, X F_Z, Z F_Z, F >.

The result is again

    FIRST_ORDER_GL2_ORBITS 6
    [1], [2], [3], [4], [5], [6].

Hence no two classes `G_u` and `G_v` with `u != v mod 7` become isomorphic even
after arbitrary residue-field GL2 changes and arbitrary first-order lifts of
those changes.

This is substantially stronger than the affine calculation: the six classes
are intrinsic first-order binary-sextic deformation classes over `F_7`.

## Arithmetic meaning

Since

    u = - (B/7^b)^5 / A^3,

all six nonzero residues are a priori possible modulo 7: the fifth-power map on
`F_7^*` is bijective, while the remaining unit factor does not collapse the
classes.

Therefore the Frey side contributes a finite list of exactly six local lifts.
The local elimination of `h,l` can now be reduced to the following finite
comparison:

1. construct a genus-2 or principally polarized CM lift attached to `h` and
   to `l` modulo 49;
2. put each lift into the same binary-sextic deformation quotient;
3. compute its class among the six residues above;
4. eliminate the form if its class is absent, or restrict `u mod 7` if it
   matches only one class.

## Current computational boundary

The workspace contains the Hilbert modular eigenvalue records and the CM field

    K=Q[z]/(z^4+5z^2+5),

but no explicit genus-2 CM model or Igusa class-polynomial data for the two
lifts `h,l`.  Sage and Magma are not installed in the governed runtime.  PARI
verifies the CM field and its local decomposition, but does not by itself
materialize the required principally polarized genus-2 CM models here.

Accordingly, the next missing input is no longer an unbounded computation.  It
is one explicit CM model (or equivalent display/Dieudonne lift data) for each
of `h,l`.  Once supplied, the comparison is a finite modulo-49 calculation
against the six certified classes above.