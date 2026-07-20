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

All seven share the CM field `F(sqrt(-3))`, but the prime `q|7` splits in this
extension because the residue field is `F_49` and `-3` is a square there.
Therefore their local type is split ordinary.  The inert-CM Honda-rank argument
used at level `2025` does not apply.  Nonordinary and toric Frey branches can be
removed uniformly; ordinary branches require the exact unramified twist or
Frobenius data for the seven forms.  See `full/LEVEL_23_CM_LOCAL_AUDIT.md`.

### D. The two ghost forms at level (3,3)

Both ghost forms are now uniformly excluded at the fixed prime `3`: their Swan
conductor is `6`, while the GA branches have Swan conductor `0` or `2`.

## Current Step-IV status

- level `(2,2)`: closed;
- level `(3,2)`: the zero-bound set is exactly `{65,78}`; the five additional
  PDF-classified CM forms have nonzero finite bounds and are eliminated at `p=7`;
  seven further non-CM forms remain as `p=7`-specific exceptions;
- level `(2,3)`: the seven zero-bound CM forms are split ordinary at `q|7`;
  individual `flag=true` output and exact local twist data are still required;
- level `(3,3)`: the two zero-bound ghost forms are uniformly closed at `3`;
  additional `p=7`-specific exceptions have not yet been enumerated.