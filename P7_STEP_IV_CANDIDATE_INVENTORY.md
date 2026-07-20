# Exact p=7 Step-IV candidate inventory from the official computation repository

The official source repository for Pacetti--Villagra Torcomian,

    upstream/GFE-5p3,

contains the Magma transcript `Outputs/TheoremA.txt`.  Reading the transcript
at p=7 gives the following exact or partially exact candidate information.

## Level (2,2)

Level:

    3^2 * (sqrt(5))^2,

with 14 newform orbits.  The standard sieve has unconditional Bad set

    {3,9,12}.

The exceptional-prime set for every other form is

    {2,3,5,11,19,29},

which does not contain 7.  Hence the exact p=7 candidate set is

    C_22={3,9,12}.

Our open LMFDB reconstruction identifies these three forms with the labels

    2025.1-e,
    2025.1-h,
    2025.1-l.

They are eliminated by `P7_LEVEL2025_FINAL_LOCAL_LEMMA.md`.  Therefore

    C_22 is empty after local elimination.

## Level (3,2)

Level:

    3^3 * (sqrt(5))^2,

with 111 newform orbits.  The detailed transcript is preserved in Git commit

    77951edd8576e450c7cf3cec78404b5521edb193

of `lucasvillagra/GFE-5p3`.  That version ran `(3,2)` with `flag=true`, so the
individual p=7 survivors are visible.  They are exactly

    C_32={21,22,26,33,61,65,78,92,98}.

Among these, 65 and 78 are unconditional Bad forms for the standard sieve;
the other seven have individual Mazur bounds divisible by 7.  The current
shorter transcript suppresses these per-orbit lines, so the historical commit
is the primary reproducible provenance for this exact set.

## Level (2,3)

Level:

    3^2 * (sqrt(5))^3,

with 35 newform orbits.  The official unconditional Bad set is

    B_23={1,7,11,12,13,16,21}.

The aggregate exceptional-prime set for the remaining forms contains 7.
Because the official call used `flag=false`, the transcript does not identify
which of the other 28 forms retain 7 individually.  Thus the currently
certified candidate containment is

    B_23 subset C_23 subset {1,...,35}.

An individual rerun or an open reconstruction of the Hecke eigenvalues is
required to determine C_23 exactly.  A complete audit of every historical
version of `Outputs/TheoremA.txt`, the deleted `TheoremA.m`/
`Elimination-Step.m`, and `Codes/GPcode.gp` found no preserved per-orbit output
or hard-coded Hecke eigenvalues for this level.

## Level (3,3)

Level:

    3^3 * (sqrt(5))^3,

with 112 newform orbits.  The official unconditional Bad set is

    B_33={22,39}.

The aggregate exceptional-prime set for the remaining forms contains 7.
Again `flag=false`, so the transcript does not reveal the complete individual
p=7 set.  The certified containment is

    B_33 subset C_33 subset {1,...,112}.

The full Git history contains no deleted detailed `(3,3)` transcript and no
stored Hecke eigenvalue table from which the individual bounds can be
recovered directly.

## Highest-return next computation

The cheapest useful next step is not another geometric local calculation.  It
is to reconstruct the individual p=7 Mazur bounds for levels (2,3) and (3,3):

1. obtain Hecke eigenvalues for the 35+112 newform orbits from an open Hilbert
   modular form source or compute the relevant Brandt modules;
2. reuse the already open PARI-generated candidate polynomials in
   `upstream/GFE-5p3/Outputs/Data.txt`;
3. implement `NewformBound`, `NewformBoundOverF`, `Eliminate_FormLL`, and
   `MazurBound` in PARI/Python;
4. retain only the forms whose individual gcd is zero or divisible by 7.

This turns two broad unknown sets into finite exact lists before any expensive
local analysis.