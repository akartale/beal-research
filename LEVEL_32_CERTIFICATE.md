# Exact mod-7 Brandt certificate for level (3,2)

## Scope

This certificate records the exact computational elimination performed at

\[
\mathfrak N_{32}=(3)^3(\sqrt5)^2,
\qquad \mathrm N(\mathfrak N_{32})=18225,
\]

over \(F=\mathbf Q(\sqrt5)\).

It is a computational certificate only. It does not by itself prove that the computed Brandt module is the full relevant Hilbert newspace; that theorem-level identification is tracked in `JL_BRANDT_THEOREM_BRIDGE.md`.

## Implementation

The computation is implemented by

```text
scripts/level32_brandt_mod7.py
```

using the repository's exact Python icosian/quaternion arithmetic and finite-ring code. No Magma or Sage dependency is used.

The script constructs the full orbit module for

```text
exponent_at_3 = 3
exponent_at_5 = 2
```

and builds both split-prime Hecke operators at rational primes `11`, `19`, and `29` on one common orbit ordering.

## Module and operators

The exact orbit-module dimension is

\[
\dim V_{32}=406.
\]

The sparse operator sizes are:

```text
T2    nnz=2022
T11a  nnz=4810
T11b  nnz=4810
T19a  nnz=7800
T19b  nnz=7800
T29a  nnz=11782
T29b  nnz=11782
```

The implementation verifies:

1. identical orbit representatives for every operator;
2. the expected row sums modulo `7`;
3. commutativity with `T2`;
4. pairwise commutativity of the six split-prime operators.

## Exact paired trace sieve

At the two primes above `11`, the only attainable ordered Frey trace pair is

\[
(2,2),
\]

and the simultaneous eigenspace has dimension

\[
15.
\]

At the two primes above `19`, the only attainable ordered pair is

\[
(5,5),
\]

and the simultaneous eigenspace has dimension

\[
4.
\]

At the two primes above `29`, the attainable ordered pairs are

\[
(1,1),\ (2,2),\ (5,5),\ (6,6).
\]

For every one of these four pairs, the simultaneous eigenspace has dimension zero:

```text
29=(1,1) dim111929=0
29=(2,2) dim111929=0
29=(5,5) dim111929=0
29=(6,6) dim111929=0
```

Thus the exact dimension chain is

\[
406\longrightarrow15\longrightarrow4\longrightarrow0.
\]

The script exits with status `0` and prints

```text
survivors_after_29=[]
eliminated=True
```

No local `7`-adic survivor test is required because the auxiliary-prime sieve leaves no nonzero simultaneous eigenspace.

## Reproduction

From the repository directory `research/beal`, run:

```text
python3 scripts/level32_brandt_mod7.py
```

The first run constructs and stores

```text
data/level32_paired_hecke_mod7.pkl
```

A second run loads this cache and reproduces the same dimensions and zero-survivor result.

## SHA-256

```text
58a33e1d90aa237877f40a1dbb51b4b0db13eaeb1e2c48c5a26fe56b811248ff  scripts/level32_brandt_mod7.py
dc8eb1338b151b6c94d103d0111355403e32062a69e977354045a33a53a6e9b8  data/level32_paired_hecke_mod7.pkl
```

## Computational conclusion

The exact mod-7 Brandt-module sieve at level `(3,2)` has no survivor compatible with the recorded ordered Frey trace pairs at the primes above `11`, `19`, and `29`.

Equivalently, within the computed Brandt module,

\[
C_{32}=\varnothing.
\]

The correct proof-status label is therefore:

> **Level `(3,2)` is computationally eliminated; theorem-level Jacquet--Langlands/Brandt completeness certification remains pending.**