# Open compact subgroup represented by the projective-line quotient

## Setup

Let

\[
F=\mathbf Q(\sqrt5),\qquad R=\mathcal O_F,
\]

and let \(\mathfrak N\) be one of

\[
(3)^2\mathfrak p_5^3,
\qquad
(3)^3\mathfrak p_5^2,
\qquad
(3)^3\mathfrak p_5^3.
\]

The Hamilton quaternion algebra used by the repository is split at every finite prime, and the implemented icosian order is maximal at every finite prime. Hence, after choosing the explicit local splittings used in the scripts,

\[
\widehat B^{\times}\simeq GL_2(\widehat F),
\qquad
\widehat R^{\times}\simeq GL_2(\widehat{\mathcal O}_F).
\]

## The local projective line

For a finite local quotient \(A=\mathcal O_F/\mathfrak p^e\), the code represents

\[
\mathbf P^1(A)
\]

by the disjoint charts

\[
\{[x:1]:x\in A\}
\sqcup
\{[1:y]:y\in\mathfrak m_A\}.
\]

The exact normalization routine accepts precisely primitive row pairs and identifies two primitive pairs when they differ by multiplication by a unit of \(A\).

Let \(G=GL_2(A)\), acting on primitive projective row vectors from the right. Take the base point

\[
x_0=[0:1].
\]

For

\[
g=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\]

we have

\[
x_0g=[c:d].
\]

This is projectively equal to \([0:1]\) exactly when

\[
c=0
\]

in \(A\). Since \(g\) is invertible, \(d\) is then a unit. Therefore the stabilizer is

\[
B_0(A)=
\left\{
\begin{pmatrix}a&b\\c&d\end{pmatrix}\in GL_2(A):c=0
\right\}.
\]

The action of \(GL_2(A)\) on primitive projective row vectors is transitive, so

\[
\mathbf P^1(A)\simeq B_0(A)\backslash GL_2(A)
\]

as right \(GL_2(A)\)-sets.

## The global finite quotient

By the Chinese remainder theorem,

\[
\mathbf P^1(\mathcal O_F/\mathfrak N)
\simeq
\prod_{\mathfrak p^e\parallel\mathfrak N}
\mathbf P^1(\mathcal O_F/\mathfrak p^e).
\]

Define

\[
K_0(\mathfrak N)=
\left\{
(g_v)_v\in GL_2(\widehat{\mathcal O}_F):
(g_v)_{21}\in\mathfrak N\widehat{\mathcal O}_F
\right\}.
\]

Equivalently, at every \(\mathfrak p^e\parallel\mathfrak N\), the lower-left matrix entry is zero modulo \(\mathfrak p^e\), while away from \(\mathfrak N\) the local subgroup is maximal compact.

The local stabilizer calculation gives the exact finite-set identification

\[
\mathbf P^1(\mathcal O_F/\mathfrak N)
\simeq
K_0(\mathfrak N)\backslash GL_2(\widehat{\mathcal O}_F).
\]

Under the explicit finite splittings of the Hamilton algebra and maximal icosian order, this is the finite-level quotient attached to the standard Eichler open compact \(K_0(\mathfrak N)\).

## Relation with the computed orbit module

The scripts quotient this projective line by the norm-one units of the icosian order:

\[
R^1\backslash\mathbf P^1(\mathcal O_F/\mathfrak N).
\]

Consequently, the computed permutation module is exactly the norm-one-unit orbit module for the standard \(K_0(\mathfrak N)\) level structure. It is not an unspecified congruence subgroup and it is not a \(K_1\)-level quotient.

The right-row convention is important: because the base point is \([0:1]\), the stabilizer condition is on the lower-left entry. Thus the implemented subgroup is the conventional \(K_0(\mathfrak N)\), up to replacing all matrices by transposes if a source uses column-vector conventions.

## Remaining global step

The stabilizer calculation identifies the local/open-compact level exactly, but it does not alone prove that the single norm-one-unit orbit quotient exhausts the global quaternionic double-coset space

\[
B^{\times}\backslash\widehat B^{\times}/K_0(\mathfrak N).
\]

For that conclusion one still needs a global class-number statement for the maximal icosian order, together with the passage between \(R^1\) and the relevant central-character quotient. After that global identification, the standard definite Jacquet--Langlands theorem must still be matched to the parallel-weight-two Hilbert cuspidal space and its new/old decomposition.

## Certified conclusion

The following point is closed:

> The projective-line action used by the repository realizes the standard open compact subgroup \(K_0(\mathfrak N)\) at each of the three computational levels.

The global double-coset exhaustiveness, central quotient, Jacquet--Langlands comparison, and newspace projection remain separate theorem-level obligations.