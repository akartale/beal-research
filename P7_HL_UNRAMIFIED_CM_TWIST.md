# The h/l system as an unramified-at-7 twist of the explicit CM curve

## Euler-factor check and correction

The script

    scripts/identify_cm_curve_hl_euler.py

compares the local Euler polynomial of

    C_0: y^2=x^5-1

with the degree-4 polynomial obtained from the HMF coefficient field of form
`h`.  At the split prime p=11 the two polynomials are

    C_0: 1 + 4T + 6T^2 + 44T^3 + 121T^4,
    h/l: 1 + 9T + 41T^2 + 99T^3 + 121T^4.

Thus `Jac(C_0)` is not literally the compatible system labelled `h/l`.
At p=19 both have `1+38T^2+361T^4`, which is consistent with common CM but
does not identify the systems.

The earlier manuscript sentence asserting literal identification must therefore
be replaced by a twist statement.

## Common CM field and infinity type

Both systems have CM by

    K=Q(zeta_5)=Q[z]/(z^4+5z^2+5),

with maximal real subfield `F=Q(sqrt(5))`.  The curve `C_0` has primitive CM by
this field.  The Hecke-zero pattern of `h,l` reconstructs the same quadratic
CM extension `K/F`.

Let `Psi_0` be the algebraic Hecke character producing `Jac(C_0)` and let
`Psi_h`, `Psi_l` be the Hecke characters producing the HMF systems.  They have
the same weight-2 CM infinity type.  Consequently

    Xi_h=Psi_h/Psi_0,
    Xi_l=Psi_l/Psi_0

have trivial infinity type.  Algebraic Hecke characters of type zero are
finite order.  Hence `h,l` are finite-order CM twists of the explicit curve's
compatible system.

## Local behavior at 7

The quartic CM field is unramified at 7, and the HMF level 2025 is prime to 7.
The explicit curve has good reduction at 7.  Therefore `Psi_0`, `Psi_h`, and
`Psi_l` are all unramified at the prime above 7, and so are the quotient
characters `Xi_h`, `Xi_l`.

On the local crystalline/Honda module, an unramified finite-order twist changes
Frobenius by multiplication by p-adic units on the Frobenius-labelled CM
components.  It does not change the Hodge filtration.  In particular the map

    delta(x)=phi(x)/7 mod (7,Fil^1)

is conjugated and multiplied on source/target components by invertible residue
field scalars.  Therefore

    rank(delta(M tensor Xi)) = rank(delta(M))

for every unramified finite-order character `Xi`.

Thus the PARI computation on `Jac(C_0)` gives the same divided-Frobenius rank
for the local systems attached to `h` and `l`, even though their global Euler
factors differ from those of `C_0`.

## Local conclusion

The explicit CM model gives

    rank(delta_CM)=1.

Every normalized Frey lift in the t=0 disk gives

    rank(delta_Frey)=2.

Since the h/l twists are unramified at 7, they retain rank 1.  Full faithfulness
of the finite Honda functor in the range `e=1<p-1` then rules out an isomorphism
of finite-flat 7-torsion group schemes.

Therefore the local elimination of `h,l` does not require literal global
identification of `Jac(y^2=x^5-1)` with the HMF orbit.  The weaker and correct
common-CM plus unramified-twist statement is sufficient.

## Citation obligation

The final manuscript should cite the standard fact that two algebraic Hecke
characters with the same infinity type have finite-order quotient, and state
the elementary local lemma that unramified unit twists preserve the rank of
divided Frobenius.  The latter can be proved directly in one paragraph from
the definition of the twisted filtered Frobenius module.