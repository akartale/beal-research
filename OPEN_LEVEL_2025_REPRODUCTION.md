# Open reproduction of Theorem A at level norm 2025

## Inputs

- public LMFDB Sage records for all 14 Hilbert newform orbits at
  `2.2.5.1-2025.1-a` through `-n`;
- upstream `Outputs/Data.txt`, containing the four local polynomial sets used
  by the authors at every auxiliary prime;
- an independent Python/SymPy implementation of `NewformBound`,
  `NewformBoundOverF`, `Eliminate_FormLL`, `MazurBound`, and `TheoremABound`.

No Magma or Sage executable is used.

## Script

    research/beal/scripts/open_theoremA_level2025_all.py

The runtime executes the quadratic orbits one at a time to avoid unnecessary
symbolic-memory peaks.

## Results

LMFDB label | gcd bound | prime divisors

    a   376200   [2,3,5,11,19]
    b    15840   [2,3,5,11]
    c     3960   [2,3,5,11]
    d      360   [2,3,5]
    e        0   []
    f     1800   [2,3,5]
    g       36   [2,3]
    h        0   []
    i       36   [2,3]
    j      720   [2,3,5]
    k       36   [2,3]
    l        0   []
    m      720   [2,3,5]
    n       36   [2,3]

Therefore the complete set of forms not eliminated by the authors' standard
auxiliary-prime sieve is

    {2025.1-e, 2025.1-h, 2025.1-l}.

This agrees in cardinality and mathematical content with the published Magma
`Bad=[3,9,12]`. The numerical indices differ because LMFDB and Magma order the
newform decomposition differently.

For p=7, every other orbit is eliminated because 7 divides none of its gcd
bounds. Hence the complete p=7 candidate set at this level is exactly

    {2025.1-e, 2025.1-h, 2025.1-l}.

All three are marked CM in LMFDB.