# Level (3,2) paired-Hecke export protocol

## Objective

The exact candidate set is

\[
C_{32}=\{21,22,26,33,61,65,78,92,98\}.
\]

The historical `flag=true` transcript proves that these and only these packets retain the prime `7` under the original coarse Mazur-bound sieve. It does not store their Hecke eigenvalues. Exact elimination therefore needs a minimal export from the original Hilbert-newform decomposition.

## Exporter

Run in the upstream `Codes` directory with Magma:

```text
magma ExportLevel32Hecke.m
```

The script is

```text
upstream/GFE-5p3/Codes/ExportLevel32Hecke.m
```

It reconstructs

\[
S_2^{\mathrm{new}}(3^3\mathfrak p_5^2)
\]

using the same `NewformDecomposition(NewSubspace(M))` ordering as the historical transcript and exports only the nine candidate indices.

## Required data per packet

For each candidate packet the export records:

1. coefficient-field degree;
2. coefficient-field defining polynomial;
3. both prime ideals above every split rational auxiliary prime;
4. the Hecke eigenvalue at each labelled prime ideal;
5. coordinates of that eigenvalue in the coefficient-field power basis;
6. its minimal polynomial as an independent check.

The paired coordinates are essential. Independent characteristic or minimal polynomials do not determine whether two eigenvalues at conjugate primes belong to the same packet.

## Auxiliary primes

The initial export set is

```text
11, 19, 29, 31, 41, 59, 61, 71, 79, 89, 101, 109
```

This contains the smallest primes from the original elimination list and enough redundancy to continue the sieve if `11,19,29` leave survivors.

## Exact downstream sieve

For each coefficient field \(E\) and each prime \(\lambda\mid7\):

1. reduce the paired Hecke eigenvalues modulo \(\lambda\);
2. compute the exact attainable ordered Frey trace pairs at the same labelled prime ideals;
3. discard the packet/\(\lambda\) branch at the first auxiliary prime where the pair is unattainable;
4. retain the full coefficient-field prime information, because different primes above `7` may give different reductions;
5. apply the local `7`-adic test to any branches surviving all auxiliary primes.

A packet is eliminated only when every prime \(\lambda\mid7\) is removed.

## Validation requirements

The export is accepted only if:

- `DECOMP_COUNT` equals `111`;
- the candidate ordering is exactly `[21,22,26,33,61,65,78,92,98]`;
- each split rational prime has two exported prime ideals;
- the eigenvalue coordinates reconstruct the printed eigenvalue in its coefficient field;
- recomputing the original `TheoremABound` from the export reproduces retention of `7` for all nine candidates;
- at least one noncandidate control packet reproduces exclusion of `7`.

## Current blocker

The active environment contains PARI/GP but not Magma or Sage. The exporter is ready, but the paired eigenvalue data cannot be generated locally from the upstream Hilbert-newform decomposition. No claim of level-`(3,2)` elimination is made until the export is produced and the exact sieve is run.