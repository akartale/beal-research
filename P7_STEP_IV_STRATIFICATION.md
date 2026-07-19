# Step-IV stratification at p=7 from the official paper and transcript

## Source correction

The official PDF, page 37, gives the exact unconditional survivor sets that are
partly obscured in the HTML rendering.

For the four levels:

1. `(2,2)`: indices `{3,9,12}`; these are the three CM forms `e,h,l` and are
   eliminated in `P7_LEVEL2025_FINAL_LOCAL_LEMMA.md`.
2. `(2,3)`: indices `{1,7,11,12,13,16,21}`; all seven have CM by
   `Q(sqrt(-3))`.
3. `(3,2)`: indices `{64,65,69,73,77,78,79}`; all seven have CM by the
   cyclotomic CM extension denoted `Q(zeta_15)/F` in the source paper.
4. `(3,3)`: indices `{22,39}`; these are the two ghost forms attached to
   `t=-1/8` and `t=9/8`.

## Exact p=7 list at level (3,2)

The official `flag=true` transcript gives the complete p=7 exceptional set

    C_32={21,22,26,33,61,65,78,92,98}.

Intersecting with the unconditional CM set gives

    C_32^CM={65,78}.

The remaining seven are p-specific Mazur-bound exceptions:

    C_32^nonCM={21,22,26,33,61,92,98}.

This separation is important: the two subsets require different elimination
arguments.

## High-return elimination plan

### A. The two CM forms 65 and 78

Recover their local CM extension and splitting behavior at 7 from the
cyclotomic field.  Then compare their finite-flat/Honda type at 7 with the
special-disk Frey types.  This is analogous to, but not identical with, the
level-2025 CM argument.

### B. The seven non-CM p-specific exceptions

For each index, find one auxiliary prime whose individual Mazur bound has
7-adic valuation exactly one and then refine the comparison by retaining the
actual residue class of the Frey parameter rather than the full coarse
candidate polynomial set.  The official transcript already shows that these
forms are eliminated for every sufficiently large p; only the accidental
factor 7 remains.

The cheapest refinement is therefore:

1. reconstruct the candidate residue sets modulo 7 from `Outputs/Data.txt`;
2. for each of the seven forms, obtain only a few Hecke eigenvalues rather than
   the full eigenpacket;
3. test the exact mod-7 traces against the Frey family, including the equation
   constraints on the parameter.

### C. The seven CM forms at level (2,3)

All seven share one CM field.  A single local splitting/Honda computation can
potentially eliminate all seven simultaneously, up to unramified twists.

### D. The two ghost forms at level (3,3)

The source paper proves a local-type mismatch at 3 when `3` does not divide the
relevant solution coordinate.  The remaining divisibility subcase should be
isolated before any new computation.

## Current Step-IV status

- level `(2,2)`: closed;
- level `(3,2)`: exact p=7 set split into 2 CM plus 7 non-CM candidates;
- level `(2,3)`: exact unconditional CM set known, but additional individual
  p=7 exceptions are not yet enumerated;
- level `(3,3)`: two unconditional ghost forms known, but additional individual
  p=7 exceptions are not yet enumerated.