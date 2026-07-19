# Diagnosis of the three level-2025 survivors

The open reproduction identifies the complete p=7 candidate set

    2025.1-e, 2025.1-h, 2025.1-l.

A branch-by-branch recomputation of the four Mazur bounds shows:

- form `e`: the `t=infinity`/`Coo` bound is identically zero at every
  auxiliary prime in the authors' data;
- forms `h` and `l`: the `t=0`/`C0` bound is identically zero at every
  auxiliary prime.

The ordinary `t != 0,infinity` branch is not identically zero for these forms.
Therefore these are not generic failures of the local sieve. They are precisely
special-fibre/ghost congruence obstructions.

Reproduction script:

    research/beal/scripts/diagnose_level2025_bad.py

This also explains why proving that the rational parameters t=-1/8 and t=9/8
are not genuine primitive integral specializations does not yet remove the
forms: the obstruction is residual mod 7, not equality of characteristic-zero
specializations.

The next required test is local at 7 or at the bad primes 3 and sqrt(5): compare
inertial type, finite-flat filtration, or residual conductor of the genuine
Frey representation with the corresponding residual representations of forms
`e`, `h`, and `l`.