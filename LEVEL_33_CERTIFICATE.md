# Level (3,3) exact mod-7 Brandt certificate

## Scope

This file records the exact computational certificate for the Step IV level

\[
(3,3),\qquad N=3^3(\sqrt5)^3.
\]

The conclusion below is computational only. It does not by itself prove the full signature-\((3,5,7)\) theorem, and it does not replace the required Jacquet--Langlands/Brandt completeness argument.

## Canonical paths and ambient module

All cache and binary paths are resolved through

```python
from paths import DATA_DIR
```

with canonical data directory

```text
research/beal/data
```

At exponent `3` at the prime above `3`, the projective CRT space has `121500` points. The quotient by the norm-one icosian unit action has `2026` orbits. Therefore the computed Brandt permutation module has dimension

\[
\dim_{\mathbf F_7} V=2026.
\]

All Hecke operators used below were constructed on this same orbit ordering.

## Certified Hecke data

The exact cache files are:

```text
data/hecke_mod7_cache.pkl
data/hecke_t11_conjugate_mod7.pkl
data/hecke_t19_pair_mod7.pkl
data/hecke_t29_pair_mod7.pkl
```

Their exponent-`3` entries have the following formats:

```text
primary11[3]   = (t2, t11a)
conjugate11[3] = (reps11b, t11b)
pair19[3]      = (reps19a, t19a, reps19b, t19b)
pair29[3]      = (reps29a, t29a, reps29b, t29b)
```

The primary `T11` cache does not store orbit representatives in its first position. The common-order checks use

```text
reps11b == reps19a == reps19b == reps29a == reps29b
```

The verified matrix data are:

- conjugate `T11`: dimension `2026`, `nnz = 24230`, commuting with `T2` and primary `T11`;
- each `T19` operator: dimension `2026`, `nnz = 40232`, common orbit order, and `[T_q19,T_q19bar]=0`;
- each `T29` operator: dimension `2026`, `nnz = 60332`, common orbit order, commuting with `T2`, with each other, and with the previously certified construction framework.

## Frey trace pairs

The exact attainable ordered trace pairs modulo `7` are:

\[
11:\ (2,2),
\qquad
19:\ (5,5),
\]

and at `29`

\[
(1,1),\ (2,2),\ (5,5),\ (6,6).
\]

The pair computation is performed by `attainable_pairs` in

```text
scripts/filter_level23_t11_t19.py
```

## Dense artifacts and exact rank kernels

For the primes `11` and `19`, the exporter

```text
scripts/export_level33_dense.py
```

writes

```text
data/level33_t11_t19_dense.bin
```

with four dense `2026 x 2026` blocks over `F_7`, in the order

```text
T11a - 2I
T11b - 2I
T19a - 5I
T19b - 5I
```

The exact Go kernel

```text
scripts/level33_rank.go
```

computes the ranks of the two-block and four-block vertical stacks.

For the surviving eight-dimensional `11,19` space, the exporter

```text
scripts/export_level33_t29_dense.py
```

writes

```text
data/level33_t11_t19_t29_dense.bin
```

with `12` blocks: the four base blocks above, followed by the two `T29` blocks for each of the four attainable trace pairs. The exact Go kernel is

```text
scripts/level33_rank_t29.go
```

## Exact rank results

The first computation gives

\[
\operatorname{rank}(T_{11,a}-2,
T_{11,b}-2)=1995,
\qquad
\dim V_{11}=31,
\]

and

\[
\operatorname{rank}(T_{11,a}-2,
T_{11,b}-2,
T_{19,a}-5,
T_{19,b}-5)=2018,
\qquad
\dim V_{11,19}=8.
\]

Thus primes `11` and `19` alone do not eliminate level `(3,3)`.

After adjoining the two operators above `29`, each attainable trace pair gives full rank:

```text
trace29=(1,1) rank111929=2026 dim111929=0
trace29=(2,2) rank111929=2026 dim111929=0
trace29=(5,5) rank111929=2026 dim111929=0
trace29=(6,6) rank111929=2026 dim111929=0
```

Hence every admissible simultaneous eigenspace is zero.

## Reproducible commands

Run from `research/beal`:

```text
python3 -m py_compile scripts/export_level33_dense.py
python3 scripts/export_level33_dense.py
go build -o scripts/level33_rank scripts/level33_rank.go
scripts/level33_rank data/level33_t11_t19_dense.bin
python3 scripts/hecke_t29_pair_mod7.py 3
python3 -m py_compile scripts/export_level33_t29_dense.py
python3 scripts/export_level33_t29_dense.py
go build -o scripts/level33_rank_t29 scripts/level33_rank_t29.go
scripts/level33_rank_t29 data/level33_t11_t19_t29_dense.bin
```

The first Go program exits with code `3` because the `11,19` space has dimension `8`; this is a mathematical survivor result, not a runtime failure. The second Go program exits with code `0` because all four `29` trace pairs are eliminated.

## SHA-256 record

```text
7e11d0576021ce26b03d3a75025c987eca73f78f989f30e4771e56e7f05830a5  data/level33_t11_t19_dense.bin
a64a95d8ba0ed939c1f095365b03d6c191b8820789de7db97bb607da2f58716f  data/level33_t11_t19_t29_dense.bin
b0dbac2d58a7c2ed46b495a85df350380192d168a207b995ddc2012977ff23c5  scripts/level33_rank.go
d7c5f358b191980c7b22b7e732ebae61a70c4640847aa812f9e16bd447ed17ec  scripts/level33_rank_t29.go
20512eeca12885f254b87ed66ca25f7a5b71a80248f7630f86ee728a22bd80bf  scripts/export_level33_dense.py
bdc0d9b121191a73927a4bb98d482bd7b91293a47f2a894e53cc6c3f4799024c  scripts/export_level33_t29_dense.py
bee521a9e9a7f2837bab804ea69c9fb6b5a84716e424a2fd1702087c0a936f8a  data/hecke_mod7_cache.pkl
b17d0a92561f035c9abb6cf060765291320e046dfbe91a825ebd61ab9ade8ea9  data/hecke_t11_conjugate_mod7.pkl
54fd12648b9ae8830721bd93ba369efd0a01e510e43c57f47156723aa754268d  data/hecke_t19_pair_mod7.pkl
112cbd1d2e99584656562a5a668c9cc880f1b1a42907423e4dbd5dbcf5d861b1  data/hecke_t29_pair_mod7.pkl
```

## Computational conclusion

The simultaneous mod-7 eigenspace satisfying the Frey trace conditions at the primes above `11`, `19`, and `29` is zero for every attainable ordered trace tuple. Hence no level-`(3,3)` Hecke packet survives this computational sieve.

## Theorem-level caveat

This certificate does not yet establish a theorem-level elimination of level `(3,3)` until the manuscript supplies and verifies:

1. the exact Jacquet--Langlands/Brandt identification for the relevant parallel weight, level, central character, and new subspace;
2. completeness of the computed newspace;
3. treatment of oldforms, multiplicities, and Eisenstein classes;
4. correctness of the labelling and normalization of the two prime ideals above each split rational prime.

No claim of a complete proof of the Beal conjecture or of the full signature-`(3,5,7)` case is made here.