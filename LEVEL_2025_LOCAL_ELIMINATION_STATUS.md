# Local elimination status for the three level-2025 survivors

## Surviving forms

The complete open sieve leaves exactly

    2025.1-e, 2025.1-h, 2025.1-l.

All are CM forms.

## Local data at p7

The unique prime of K=Q(sqrt(5)) above 7 has norm 49. LMFDB gives

    a_p7(2025.1-e) = -14,
    a_p7(2025.1-h) = 0,
    a_p7(2025.1-l) = 0.

Hence all three are nonordinary at p7. Any congruence with one of these forms
forces the Frey representation into the nonordinary/niveau-two finite-flat
branch. Ordinary Frey specializations are therefore already excluded from
this level.

Reproduction:

    research/beal/scripts/show_p7_eigenvalues.py

## Existing local eliminations from the source paper

Use the source variables

    (a,b,c)=(B,-C,A).

### Ghost forms

Theorem `thm:local-type-3` applies for every p>3, hence also p=7. It states
that if 3 does not divide the source variable c, then the Frey motive is not
congruent modulo p to either ghost motive.

Translated to our variables:

    if 3 does not divide A,
    both ghost congruences are eliminated modulo 7.

This is unconditional and does not require the large-image conjecture.

### Divisibility of the exponent-p variable

The discussion following Theorem B states that if 3 divides the source
variable b or 5 divides b, the Frey representation has a special local type
at 3 or sqrt(5). This rules out both CM forms and the two ghost-form spaces.

Translated to our variables:

    if 3 divides C or 5 divides C,
    the level-2025 CM/ghost obstruction is eliminated.

The local-type argument itself is independent of the asymptotic
irreducibility bound used elsewhere in Theorem B; once p=7 absolute
irreducibility is supplied by our separate argument, this local elimination
is available at p=7.

## Current status

The verified local calculations now cover every candidate/branch pair:

- `t=0`: `h,l` are eliminated by divided-Frobenius rank, while `e` is
  eliminated by the exact auxiliary-prime branch sieve;
- `t=infinity`: `e` is eliminated by the intrinsic normalized q-Frobenius
  trace, while `h,l` are eliminated by divided-Frobenius rank on the proper
  genus-2 crystalline submodule;
- `t=1`: all three forms are eliminated by the totally toric rank-two
  degeneration and its cyclotomic submodule;
- `t mod 7 in {2,3,4,5,6}`: the smooth Frey reductions are ordinary, whereas
  all three candidate forms are nonordinary.

For the infinity comparison, the even-degree PARI space has basis
`e_i=X^(i-1)dX/(2Y)`, `1<=i<=5`.  The residue map at the two points at infinity
is the `e_3` coefficient, so the proper crystalline lattice is the
Frobenius-stable kernel `<e_1,e_2,e_4,e_5>`.  On this lattice the divided
lower-left block has rank 2 for every infinity residue class, while the CM
model for `h,l` has rank 1; unramified unit twists preserve this rank.  See
`P7_INFINITY_HL_DIVIDED_FROBENIUS.md`.

Thus the three level-2025 candidates are eliminated in every local branch at
7, subject to the stated standard finite-Honda, residue-sequence, CM-twist, and
Raynaud inputs.  This closes level `(2,2)` only.  The other Step-IV levels and
the full signature-(3,5,7) theorem remain open.