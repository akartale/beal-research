# Normalized q-Frobenius test for the infinity branch and form e

## Setup

Let `p=7` and let `q=p^2=49`, since 7 is inert in
`F=Q(sqrt(5))`.  In the infinity branch the normalized genus-2 family is

    C_{a,v}: Y^2 = 45v^2X^6 - 108*7^a*v^2X^5 + 90vX^3 + 9,

with `a>=1` and `v` a 7-adic unit.  Its special fibre has Cartier--Manin
matrix zero, so the first useful crystalline datum occurs after two p-Frobenius
steps and division by p.

For a crystalline Frobenius matrix `Phi`, define the normalized q-Frobenius
trace

    tau(C) = Tr(Phi^2 / 7) mod 7.

On the slope-one q-Frobenius module, `Phi^2(D)` is contained in `7D`, so this
is the trace of the induced mod-7 endomorphism.  It is therefore a candidate
finite-Honda invariant.

## Exact PARI computation

The script

    scripts/p7_infinity_normalized_qtrace.gp

uses `hyperellpadicfrobenius(Q,7,2)` and enumerates every unit `v mod 49` for
both first-order cases:

- `a=1`, where the `X^5` deformation is visible modulo 49;
- `a>=2`, represented by `a=2`, where that term vanishes modulo 49.

For an even-degree sextic PARI returns a five-dimensional
Monsky--Washnitzer matrix with one extraneous eigenvalue `-7`.  After squaring,
that line contributes `49`, hence zero modulo 49.  Consequently

    Tr(Phi^2)/7 mod 7

computed from the full matrix equals the corresponding trace on the
four-dimensional genus-2 quotient.

The result is independent of the lift digit of `v` and of whether `a=1` or
`a>=2`:

    v mod 7 in {1,3,4,6}: tau(C_{a,v}) = 5,
    v mod 7 in {2,5}:     tau(C_{a,v}) = 4.

Thus the infinity family realizes only the values `{4,5}`.

The companion full-matrix script

    scripts/p7_infinity_filtered_frobenius.gp

shows that the genus-2 characteristic polynomial of p-Frobenius is

    X^4 + 7X^2 + 49       for v mod 7 in {1,3,4,6},
    X^4 - 14X^2 + 49      for v mod 7 in {2,5}.

Squaring p-Frobenius and dividing its trace by 7 gives the same values above.

## Form e

The cached LMFDB record, rechecked by

    scripts/show_p7_eigenvalues.py,

has

    a_q(e) = -14

at the unique prime of norm 49.  The two-dimensional local polynomial is

    X^2 + 14X + 49 = (X+7)^2.

For the four-dimensional restriction-of-scalars module, the normalized
q-Frobenius trace is therefore

    tau(e) = 2*(-14)/7 = -4 = 3 mod 7.

This differs from both infinity values `4` and `5`.

## Consequence

The computation gives the separation

    tau(infinity Frey) in {4,5},
    tau(e) = 3.

The two formal checks are supplied in

    P7_FORM_E_QFROBENIUS_INTRINSICNESS.md.

In a Hodge-adapted block matrix, vanishing Hasse--Witt forces the upper-left
Frobenius block to be divisible by 7, and one obtains

    tau = Tr(B^(sigma)C + C^(sigma)B) mod 7.

This expression is determined by the torsion Fontaine--Laffaille module.
The restriction-of-scalars trace is the field trace of `a_q(e)`; because
`a_q(e)=-14` is rational, it equals `2*a_q(e)=-28`.

Therefore an isomorphism of finite-flat residual models would force equal
`tau`, contradicting `{4,5} != {3}`.  Form `e` is eliminated in the infinity
branch, subject only to the standard low-ramification full-faithfulness input
already used in the local argument.