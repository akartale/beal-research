# Full proof audit for the signature (3,5,7)

## Translation to the source paper

Our equation is

    A^3 + B^5 = C^7.

It becomes the paper's equation

    x^5 + y^p + z^3 = 0

with

    p = 7,
    x = B,
    y = -C,
    z = A.

Thus the paper's variables (a,b,c) correspond to

    (a,b,c) = (B,-C,A).

## Crucial conclusion

Theorem A of Pacetti--Villagra Torcomian explicitly excludes

    p in {2,3,5,7,11,13,19,29,31,41,61,71,79,89,101,109}.

In particular, p=7 is not covered by their final theorem. Therefore proving
absolute irreducibility at 7 does not by itself prove the nonexistence of
primitive solutions to A^3+B^5=C^7.

## What absolute irreducibility would accomplish

Once Lemmas A and B in `P7_IRREDUCIBILITY_ARGUMENT.md` are proved, the
reducible branch for p=7 is removed. This completes Step III of the modular
method for the chosen residual RM representation.

It does not complete Step IV. One must still eliminate every Hilbert newform
whose residual representation can remain congruent mod 7 to the Frey
representation.

## Remaining Step-IV branches

The source paper's general elimination leaves three kinds of obstruction:

1. CM Hilbert modular forms;
2. the two ghost forms attached to t=-1/8 and t=9/8;
3. additional forms whose Mazur bounds are divisible by 7.

The elementary argument that t=-1/8 and t=9/8 are not actual primitive
specializations does not eliminate residual congruences to their mod-7
representations. A separate local-type or residual comparison is required.

Similarly, proving that the Frey characteristic-zero object has no CM does not
by itself rule out a mod-7 congruence to a CM form.

## Candidate sets currently known

### Level (2,2): 3^2 (sqrt(5))^2

The published output has exceptional-prime set

    {2,3,5,11,19,29}

for every form outside the Bad set. Since 7 is absent, the complete p=7
candidate set at this level is exactly

    {3,9,12}.

These three forms are CM forms in the source paper.

### Level (3,2): 3^3 (sqrt(5))^2

The detailed official output gives the exact p=7 candidate set

    {21,22,26,33,61,65,78,92,98}.

Here 65 and 78 are unconditionally Bad for the standard auxiliary-prime sieve;
the other seven retain 7 in their individual bounds.

### Levels (2,3) and (3,3)

The official computation repository has now been imported at
`upstream/GFE-5p3`.  Its transcript gives unconditional Bad sets

    B_23={1,7,11,12,13,16,21},
    B_33={22,39}.

The published calls use `flag=false`; their aggregate exceptional-prime lists
contain 7, so the complete individual p=7 candidate sets outside these Bad
sets still cannot be recovered from the transcript alone.  The correct level
norms are 10125 and 91125 because the inert ideal `(3)` has norm 9.  Direct
LMFDB pages exist at norm 10125, but the public search/API does not currently
return the complete orbit list, so a dedicated label/download reconstruction
is required.  See `P7_STEP_IV_CANDIDATE_INVENTORY.md`.

## Translation of the paper's auxiliary local hypotheses

Theorem B assumes that the paper's b is odd and divisible by 3 or 5. In our
variables this means

    C is odd and 3|C or 5|C.

Moreover Theorem B still excludes p=7, so it cannot be applied directly.

Theorem C uses 3 not dividing the paper's c to distinguish the ghost local
type. In our variables this is

    3 does not divide A.

This may provide a useful local elimination for a subcase, but it does not
cover all primitive solutions.

## Exact logical status

At level `(2,2)`, norm 2025, the three candidates are eliminated in the special 7-adic disks `t=0` and `t=infinity`; see `P7_LEVEL2025_FINAL_LOCAL_LEMMA.md`.  The generic unit-disk branch is still open.  The official candidate inventory for
all four levels is recorded in `P7_STEP_IV_CANDIDATE_INVENTORY.md`.

After proving Lemmas A and B:

    absolute irreducibility at p=7: complete;
    modularity and conductor framework: inherited from the source papers;
    level (2,2) newform elimination: complete only in the special 7-adic disks; generic unit disk open;
    levels (3,2), (2,3), (3,3): still open;
    full nonexistence theorem for A^3+B^5=C^7: not yet established.

## Required path to a complete private-signature theorem

1. Prove Lemma A: exact finite-flat inertia types at p7.
2. Prove Lemma B: diagonal-character conductor bounds.
3. Obtain the complete p=7 candidate newform list at all four levels.
4. Identify each candidate by coefficient field, CM status, and ghost origin.
5. Build local residual tests specifically mod 7, preserving paired primes and
   embeddings.
6. Eliminate CM congruences.
7. Eliminate ghost congruences, possibly using local type at 3 and separate
   treatment of 3|A.
8. Eliminate all additional p=7 exceptional forms.
9. Audit all primitive divisibility subcases and signs.

Only after all nine items are closed can one claim the full primitive
signature-(3,5,7) result.