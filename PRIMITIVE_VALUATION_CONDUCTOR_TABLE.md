# Primitive valuation and conductor table for signature (3,5,7)

## Source translation

The source equation is

\[
a^5+b^p+c^3=0,
\]

with `p=7`. Our equation

\[
A^3+B^5=C^7
\]

is obtained by

\[
(a,b,c)=(B,-C,A).
\]

Thus

\[
t_0=-\frac{a^5}{c^3}=-\frac{B^5}{A^3}.
\]

All congruences below use the signed integers `A,B,C`; no extra positivity hypothesis is inserted.

## Uniform source inputs

For the plus motive used in the repository, the source gives the following branch-independent inputs.

1. Theorem 2.1(4): the residual representation is finite at every prime above `p`. For `p=7`, this supplies the finite-flat input at the unique prime `p7` for every specialization, without assuming a particular divisibility branch.
2. Theorem 2.4(1): when `r=3` and `q>=5`, the plus motive is modular for every specialization of `t`. Here `q=5`, so modularity is available for every primitive branch.
3. Theorem 7.8: after absolute irreducibility and level lowering, the residual representation occurs in parallel weight two, trivial Nebentypus, at level

\[
(3)^{\epsilon_3}(\sqrt5)^{\epsilon_5},
\qquad \epsilon_3,\epsilon_5\in\{2,3\}.
\]

Theorem 7.8 already gives an exhaustive disjoint decision rule for `epsilon_3` and `epsilon_5`; no additional sign reduction is required for the conductor assignment.

## Primitive divisibility rule

For each rational prime `ell`, primitiveness implies that not all of `A,B,C` are divisible by `ell`. The source conductor theorem separates the cases according to which of the three source variables is divisible. Under the translation, these are exactly the cases listed below.

## Prime 3

Define

\[
A_0=A\,3^{-v_3(A)}.
\]

The exact translated rule is

\[
\epsilon_3=
\begin{cases}
2,&3\mid BC,\\
2,&3\mid A\text{ and }\pm2A_0^3\equiv B^5\pmod9,\\
2,&3\nmid ABC\text{ and }4A^3\equiv B^5\pmod9,\\
3,&\text{otherwise}.
\end{cases}
\]

Because the solution is primitive, the first line means `3|B` or `3|C` (not both together with `3|A`). The branch table is therefore:

| Primitive 3-branch | Extra congruence | `epsilon_3` | Source input |
|---|---:|---:|---|
| `3|B` | none | 2 | Theorem 7.8(i), case `3|ab` |
| `3|C` | none | 2 | Theorem 7.8(i), case `3|ab` |
| `3|A` | `+2A_0^3=B^5 mod 9` or `-2A_0^3=B^5 mod 9` | 2 | Theorem 7.8(i), case `3|c` |
| `3|A` | neither signed congruence | 3 | `otherwise` |
| `3∤ABC` | `4A^3=B^5 mod 9` | 2 | Theorem 7.8(i), unit case |
| `3∤ABC` | congruence fails | 3 | `otherwise` |

The no-twist input used to sharpen the special conductor exponent to `2` is Lemma 7.3 together with Corollary 3.6 and Remark 3.7.

## Prime 5

Define

\[
B_0=B\,5^{-v_5(B)}.
\]

All quotients modulo `25` below are taken in `(Z/25Z)^x`. The exact translated rule is

\[
\epsilon_5=
\begin{cases}
2,&5\mid CA,\\
2,&5\mid B\text{ and }A^3/B_0^5\in\{6,12,28\}\pmod{25},\\
2,&5\nmid ABC\text{ and }A^3/B^5\in\{6,8,17,19\}\pmod{25},\\
3,&\text{otherwise}.
\end{cases}
\]

Here `28 mod 25` means `3 mod 25`; it is retained as `28` to match the source statement. The branch table is:

| Primitive 5-branch | Extra congruence | `epsilon_5` | Source input |
|---|---:|---:|---|
| `5|A` | none | 2 | Theorem 7.8(ii), case `5|bc` |
| `5|C` | none | 2 | Theorem 7.8(ii), case `5|bc` |
| `5|B` | `A^3/B_0^5 in {6,12,28} mod 25` | 2 | Theorem 7.8(ii), case `5|a` |
| `5|B` | congruence fails | 3 | `otherwise` |
| `5∤ABC` | `A^3/B^5 in {6,8,17,19} mod 25` | 2 | Theorem 7.8(ii), unit case |
| `5∤ABC` | congruence fails | 3 | `otherwise` |

The exact exponent statements use Corollary 3.11, Remark 3.12, Proposition 7.4, and the finite residue computation referenced in the proof of Theorem 7.8.

## Assignment to the four lowered levels

The two independent decision rules give exactly one ordered pair

\[
(\epsilon_3,\epsilon_5)\in\{2,3\}^2.
\]

| Pair | Lowered level | Repository label |
|---:|---|---|
| `(2,2)` | `(3)^2 (sqrt(5))^2` | level `(2,2)` |
| `(2,3)` | `(3)^2 (sqrt(5))^3` | level `(2,3)` |
| `(3,2)` | `(3)^3 (sqrt(5))^2` | level `(3,2)` |
| `(3,3)` | `(3)^3 (sqrt(5))^3` | level `(3,3)` |

Thus no fifth conductor level and no omitted primitive divisibility branch occur in Theorem 7.8.

## Consequences for Lemmas A, B, and D

### Lemma A

The finite-at-`p` statement is uniform over all specializations by Theorem 2.1(4). Therefore the remaining source finite-flat dependency recorded in the earlier audit is closed for the plus motive used here.

### Lemma B

For every branch,

\[
a_{(3)}(\bar\rho_7)=\epsilon_3\le3,
\qquad
a_{(\sqrt5)}(\bar\rho_7)=\epsilon_5\le3.
\]

The internal inequality under semisimplification then yields the ray-character modulus used in Lemmas B and C. The branchwise source-conductor dependency is closed by the exhaustive translated Theorem 7.8 table above.

### Lemma D

For the final trivial ray character, the semisimplification at every prime away from `7` is

\[
1\oplus1,
\]

because the mod-`7` cyclotomic character is unramified at primes above `3` and `5`. Any two-dimensional extension of two unramified characters over characteristic `7` has Artin conductor at most `1` at such a prime: wild inertia is pro-`3` or pro-`5` and cannot map nontrivially to the order-`7` unipotent subgroup, while a nontrivial tame unipotent action fixes a line and contributes conductor exactly `1`.

The source table gives

\[
a_{(3)}(\bar\rho_7)=\epsilon_3\in\{2,3\},
\qquad
a_{(\sqrt5)}(\bar\rho_7)=\epsilon_5\in\{2,3\}
\]

in every primitive branch. Hence the trivial-character reducible representation contradicts the source conductor at both primes, including the level `(3,3)` branch. No additional assertion that one exponent must equal exactly `2` is needed.

Thus the branchwise conductor step in Lemma D is closed.

## Exact status

Closed by this table:

- exhaustive source-variable translation;
- all primitive divisibility branches at `3` and `5`;
- uniform modularity of the plus motive;
- uniform finite-at-`7` input;
- exact assignment to the four lowered levels;
- branchwise conductor upper bounds needed in Lemma B.

Still open:

- the split-toric RM-factor bridge in Lemma D, needed to reduce the four quadratic survivors to the trivial character.

The subsequent trivial-character conductor contradiction is now uniform over all four conductor pairs.