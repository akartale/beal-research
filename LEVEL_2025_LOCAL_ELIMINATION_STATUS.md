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

## Final status

The special-disk calculations and finite-Honda comparison are now assembled in

    P7_LEVEL2025_FINAL_LOCAL_LEMMA.md.

They eliminate `e` in the infinity disk by ordinary versus p-rank-zero
incompatibility, and eliminate `h,l` in the t=0 disk by the rank of divided
Frobenius.  The h/l argument is local: two crystalline CM inductions from the
same unramified quadratic extension with the same labelled Hodge--Tate weights
differ by an unramified unit twist, which preserves the rank invariant.

Therefore the three candidates are eliminated in the special disks `t=0` and `t=infinity`.  The generic unit-disk branch remains open unless an independent argument forces a primitive solution into one of the special disks.