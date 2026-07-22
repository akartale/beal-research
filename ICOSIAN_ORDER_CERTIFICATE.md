# Exact certificate for the icosian order and finite ramification

## Setup

Let

\[
F=\mathbf Q(\sqrt5),\qquad \mathcal O_F=\mathbf Z[a],\qquad a^2-a-1=0,
\]

and let

\[
B=(-1,-1)_F
 =F\langle i,j\rangle/(i^2=j^2=-1,\ ij=-ji).
\]

The repository uses the four explicit elements returned by

```text
icosian_order_basis()
```

as an \(\mathcal O_F\)-basis of the implemented icosian order \(R\subset B\).

The exact verification script is

```text
scripts/icosian_order_certificate.py
```

and uses only rational arithmetic together with the repository's exact \(\mathcal O_F\) and quaternion implementations.

## Multiplicative closure

For every ordered pair of basis elements \(e_i,e_j\), the script solves

\[
e_i e_j=\sum_{k=1}^4 c_{ijk}e_k
\]

exactly over \(F\). All sixteen products have coefficients

\[
c_{ijk}\in\mathcal O_F.
\]

The script prints

```text
multiplication_closed True
```

so the displayed lattice is an \(\mathcal O_F\)-order.

## Reduced-trace Gram matrix

For the basis \(e_1,\ldots,e_4\), define

\[
G_{ij}=\operatorname{trd}(e_i e_j).
\]

The exact matrix is

\[
G=
\begin{pmatrix}
-1&-1&-1&-a\\
-1&-2&-a&-a\\
-1&-a&-2&-a\\
-a&-a&-a&-2
\end{pmatrix}.
\]

Its determinant is

\[
\det G=a-2.
\]

Since

\[
N_{F/\mathbf Q}(a-2)=1,
\]

this determinant is a unit of \(\mathcal O_F\). The script prints

```text
trace_discriminant (-2)+(1)*a
trace_discriminant_norm 1
trace_discriminant_is_unit True
```

## Consequences

For an order in a quaternion algebra over a number field, the local discriminant detects precisely the finite primes at which either the algebra is ramified or the order is nonmaximal. Because the reduced-trace discriminant of \(R\) is the unit ideal, its localization has unit discriminant at every finite prime.

Therefore:

1. \(B\) is split at every finite prime of \(F\);
2. the finite ramification set of \(B\) is empty;
3. \(R\) is maximal at every finite prime;
4. because \(B\) is ramified at both real places, its complete ramification set is exactly the two real places of \(F\).

Equivalently,

\[
\operatorname{Ram}(B)=\{v_1,v_2\},
\]

where \(v_1,v_2\) are the two real embeddings of \(F\).

## Reproduction

From `research/beal`, run

```text
python3 scripts/icosian_order_certificate.py
```

The expected final lines are

```text
multiplication_closed True
finite_ramification_empty=true
order_maximal_at_all_finite_primes=true
```

The command exits with status `0`.

## Scope

This certificate closes the finite-ramification and maximal-order obligations for the implemented Hamilton/icosian pair. It does not by itself identify the projective-line quotient with the required Hilbert newspace; the open-compact, oldspace, Eisenstein, multiplicity, and Jacquet--Langlands comparison obligations remain in `JL_BRANDT_THEOREM_BRIDGE.md`.