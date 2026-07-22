# Exact level-(2,2) Brandt certificate for the final quadratic character

## Target eigensystem

For the final quadratic character

\[
\chi=(90,0),
\]

the predicted Hecke eigenvalues modulo `7` are

\[
(T_{11^+},T_{11^-})=(2,2),
\qquad
(T_{19^+},T_{19^-})=(1,1),
\qquad
(T_{29^+},T_{29^-})=(2,2).
\]

## Full integral Brandt module

The exact script

```text
scripts/p7_900_brandt_level22.py
```

constructs the full icosian orbit module for

\[
(3)^2(\sqrt5)^2
\]

with ambient dimension `46`, constructs all six Hecke operators, verifies their row sums and pairwise commutativity, and computes the stacked rank over `F_7`.

Its SHA-256 is

```text
ace7ab37dd5c995cd24ee3af37857d8d808b18e9bb4144afc282bbfea7d2eed0
```

which agrees exactly with the `script_sha256` stored in

```text
data/p7_900_brandt_level22_certificate.json
```

The certificate records

```text
ambient dimension 46
T11a=2: rank 40, dimension 6
T11b=2: rank 42, dimension 4
T19a=1: rank 46, dimension 0
T19b=1: rank 46, dimension 0
T29a=2: rank 46, dimension 0
T29b=2: rank 46, dimension 0
```

Thus

\[
\boxed{
\ker(T_{11^+}-2)\cap
\ker(T_{11^-}-2)\cap
\ker(T_{19^+}-1)=0
}
\]

already on the full mod-`7` Brandt module. In particular, adding the remaining three conditions cannot create a survivor.

This is stronger than checking only characteristic-zero eigenform packets and has no torsion or non-liftable-eigenclass ambiguity inside the Brandt module itself.

## Important noncircularity issue

This finite computation does **not by itself** prove residual irreducibility.

To use the level-`(2,2)` Brandt vanishing against a hypothetical reducible Frey representation, one needs a noncircular theorem placing that reducible residual representation in this exact Brandt/Hilbert module. If the only route to level `(2,2)` is a level-lowering theorem whose hypotheses already include absolute irreducibility, then using this certificate to prove absolute irreducibility would be circular.

Therefore one of the following must be supplied:

1. a reducible-compatible modularity/level theorem placing the representation at exact residual conductor level `(2,2)` without assuming irreducibility; or
2. an Eisenstein/Selmer theorem excluding the character directly from its local conditions, without passing through irreducible level lowering.

## Exact status

Mechanically closed:

- no Eisenstein target eigensystem `(2,2),(1,1),(2,2)` exists in the full mod-`7` Brandt module of level `(2,2)`;
- the result is recorded with matrix hashes, row-sum checks, commutativity checks, rank chain, and matching script hash.

Still theorem-level open:

- the noncircular bridge from a hypothetical reducible Frey representation to this exact level-`(2,2)` Brandt module.

Accordingly, the character `(90,0)` is computationally eliminated at level `(2,2)`, but Lemma D is not yet declared closed solely from this certificate.