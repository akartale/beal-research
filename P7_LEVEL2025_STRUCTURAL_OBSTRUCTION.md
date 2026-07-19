# Structural obstruction at level 2025 for p=7

## What the remaining branches mean

For the plus family

    t=-B^5/A^3.

If 7 divides B and 7 does not divide A, then t reduces to 0 modulo 7.
If 7 divides A and 7 does not divide B, then t reduces to infinity.

The three surviving CM forms are not accidental failures of the auxiliary
prime sieve. Their zero Mazur bounds identify them with these special fibres:

- forms h and l are the t=0 obstruction;
- form e is the t=infinity obstruction.

Thus, in these two arithmetic branches, the residual plus representation is
expected to coincide with the residual representation of a special fibre.
More auxiliary-prime traces cannot separate them.

## Elementary local arithmetic

An exhaustive check modulo 49 and 343 shows that both primitive branches
7|A and 7|B are locally soluble. Simultaneous divisibility is absent, as forced
by primitivity. Hence there is no elementary contradiction modulo 7^2 or 7^3.

Reproduction:

    research/beal/scripts/local_mod7_branches.py

## Why a second Frey motive does not immediately solve this

The source paper constructs both plus and minus hypergeometric motives. The
minus motive has analogous ramification and finite-at-p properties. However,
for r=3 the paper proves modularity of every specialization of the minus motive
only when q>=11.

For q=5, which is our signature, the paper explicitly states that the method
does not prove modularity for all specializations: the auxiliary residual
representation modulo sqrt(5) can be reducible.

Therefore a plus/minus modular switch is not presently unconditional for
(5,7,3). This is a mathematical modularity gap, not a Magma/Sage dependency.

## Consequence

The plus-method proof is complete away from the special p-adic branches

    7|A or 7|B.

Closing those branches requires at least one genuinely new ingredient:

1. prove modularity of the relevant minus specializations at q=5;
2. construct a different modular Frey object whose special fibres at 0 and
   infinity are non-CM or have incompatible local type;
3. prove a refined integral/p-adic result excluding primitive solutions in
   the t=0 and t=infinity residue disks;
4. use a multi-Frey argument with a classical elliptic curve or another
   hypergeometric family.

This is currently the sharpest identified obstruction at level 2025.