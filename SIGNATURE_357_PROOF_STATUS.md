# Signature (3,5,7): proof-status manuscript

## 1. Statement under investigation

We study primitive nonzero integer solutions of

\[
A^3+B^5=C^7,
\qquad \gcd(A,B,C)=1.
\]

The goal is to prove that no such solution exists.

This document records the exact theorem-level status of the modular-method argument. It deliberately separates established deductions from remaining work. At the present stage the full nonexistence theorem is **not yet proved**. All four Step-IV levels are now computationally eliminated, but the local-integral and Jacquet--Langlands/Brandt completeness bridges are not yet fully written and verified.

## 2. Translation to the source modular framework

The source equation

\[
x^5+y^p+z^3=0
\]

is obtained by

\[
p=7,\qquad x=B,\qquad y=-C,\qquad z=A.
\]

Thus the source variables \((a,b,c)\) correspond to \((B,-C,A)\). Every imported conductor, modularity, and level-lowering statement must be read through this translation.

The source theorem excludes \(p=7\) from its final global statement. Consequently the case \((3,5,7)\) requires a separate Step-IV elimination of all residual Hilbert newform packets.

## 3. Modular representation and irreducibility

Let \(F=\mathbf Q(\sqrt5)\), and let \(\mathfrak p_7\) be the unique prime above 7. Since 7 is inert in \(F\),

\[
F_{\mathfrak p_7}/\mathbf Q_7
\]

is unramified of degree two and has residue field \(\mathbf F_{49}\).

The Frey construction supplies a two-dimensional residual RM representation

\[
\bar\rho_7:G_F\longrightarrow \mathrm{GL}_2(\overline{\mathbf F}_7).
\]

The irreducibility argument has two branches.

### 3.1 Niveau-two branch

Raynaud's tame-weight bound and low-ramification finite-flat full faithfulness restrict the inertia exponents to

\[
\{0,8\}\quad\text{or}\quad\{1,7\}.
\]

The exact ray-class sequence for the modulus enlarged by \(\mathfrak p_7\) shows that every global ray character allowed by the conductor bound is trivial on the local element \(-1\). Hence its tame exponent is even. This excludes the niveau-two exponents 1 and 7.

### 3.2 Ordinary branch

The relevant ray class group has order 360. All algebraic-closure-valued characters are enumerated, without assuming that the character values lie in \(\mathbf F_{49}\). At the two primes above 19, the exact paired sieve leaves no survivor in the generic good-reduction branch. The full four-branch sieve leaves four quadratic characters. The corrected tangent-branch calculation at \(7\) eliminates the trivial character, and local conductor comparisons eliminate two more. One character remains:

\[
\chi=(90,0),
\qquad
\operatorname{cond}(\chi)=(3)(\sqrt5),
\qquad
(\epsilon_3,\epsilon_5)=(2,2).
\]

The sole remaining character is computationally absent from the full mod-`7` Brandt module at level `(2,2)`: an exact rank computation on the dimension-`46` module gives zero simultaneous eigenspace. However, the source level theorem assumes irreducibility before applying level lowering. Hence this Brandt contradiction cannot be used to prove irreducibility without circularity. A direct Eisenstein/Selmer obstruction, or a reducible-compatible level theorem, is still required. Therefore theorem-level absolute irreducibility is not yet proved.

The detailed argument and reproducible computations are in `P7_IRREDUCIBILITY_ARGUMENT.md`, `LEMMA_A_B_LOCAL_PROOF_DRAFT.md`, and `LEMMA_C_D_ABSOLUTE_CHARACTERS_AND_L19.md`.

## 4. Candidate levels after level lowering

The Step-IV levels are indexed by

\[
(r,s)\in\{2,3\}\times\{2,3\},
\]

corresponding to levels

\[
3^r(\sqrt5)^s.
\]

Their norms are:

\[
(2,2):2025,\qquad (3,2):18225,\qquad (2,3):10125,\qquad (3,3):91125.
\]

Here \(\mathrm N((3))=9\), because 3 is inert in \(F\), and \(\mathrm N((\sqrt5))=5\).

The proof must eliminate every mod-7 newform packet at all four levels.

## 5. Level \((2,2)\): computational/local elimination complete, theorem integration pending

The open reconstruction of the source auxiliary-prime sieve identifies exactly three mod-7 candidates:

\[
2025.1\text{-}e,
\qquad 2025.1\text{-}h,
\qquad 2025.1\text{-}l.
\]

All three are CM forms.

The 7-adic parameter space is divided into the smooth unit disks and the special disks \(t=0,1,\infty\). The eliminations are:

1. smooth unit disks: the Frey Jacobian is ordinary, whereas all three candidates are nonordinary;
2. \(t=1\): stable reduction is totally toric of rank two, incompatible with the candidate local systems;
3. \(h,l\) at \(t=0\) and \(t=\infty\): the rank of the divided-Frobenius map on the proper four-dimensional crystalline lattice is 2 for the Frey family and 1 for the CM local systems;
4. \(e\) at \(t=0\): exact auxiliary-prime branch polynomials give no compatible residual branch;
5. \(e\) at \(t=\infty\): the intrinsic normalized \(q\)-Frobenius invariant separates the finite-flat torsion modules.

For the last comparison, form \(e\) has

\[
a_{\mathfrak p_7}(e)=-14,
\]

so on the four-dimensional restriction-of-scalars module

\[
\tau(e)=\frac{2(-14)}7\equiv3\pmod7.
\]

The infinity Frey family has

\[
\tau\in\{4,5\}.
\]

Equivalently, the full normalized \(q\)-Frobenius characteristic polynomial of form \(e\) is

\[
(X+1)^4,
\]

whereas every Frey lift gives one of

\[
X^4+2X^3+3X^2+2X+1,
\]

or

\[
X^4+3X^3+6X^2+3X+1.
\]

Thus

\[
\boxed{C_{22}=\varnothing.}
\]

## 6. Level \((2,3)\): computationally eliminated by exact Brandt-module filtering

The mod-7 Brandt module has dimension 226. Split-prime Hecke operators were constructed at both primes above 11, 19, and 29.

At the primes above 11, the only attainable ordered trace pair compatible with a nonzero simultaneous eigenspace is

\[
(2,2),
\]

and the space drops from dimension 226 to dimension 8.

At the primes above 19, the only attainable pair is

\[
(5,5),
\]

and the space drops from dimension 8 to dimension 4.

At the primes above 29, the attainable pairs are

\[
(1,1),\ (2,2),\ (5,5),\ (6,6).
\]

Every corresponding simultaneous eigenspace has dimension zero. Therefore

\[
226\longrightarrow8\longrightarrow4\longrightarrow0,
\]

and

\[
\boxed{C_{23}=\varnothing.}
\]

The final exact filter is implemented by `scripts/filter_level23_t11_t19_t29.py`.

## 7. Level \((3,2)\): computationally eliminated, theorem-level certification pending

The historical transcript gives the exact characteristic-zero candidate set

\[
C_{32}=\{21,22,26,33,61,65,78,92,98\}.
\]

Rather than reconstructing these packets individually, the repository now computes the full mod-7 icosian Brandt module at

\[
(3)^3(\sqrt5)^2.
\]

Its exact orbit dimension is

\[
406.
\]

At the two primes above `11`, the attainable pair `(2,2)` cuts the simultaneous eigenspace to dimension `15`. Adding the pair `(5,5)` at the two primes above `19` cuts it to dimension `4`.

At the two primes above `29`, the attainable ordered pairs are

\[
(1,1),\ (2,2),\ (5,5),\ (6,6).
\]

Each of the four corresponding simultaneous eigenspaces has dimension zero. Hence

\[
406\longrightarrow15\longrightarrow4\longrightarrow0.
\]

No local 7-adic survivor test is required. The exact computation and hashes are recorded in `LEVEL_32_CERTIFICATE.md`.

This is a computational elimination. The theorem-level Jacquet--Langlands/Brandt completeness, newspace, oldform, Eisenstein, multiplicity, and split-prime-normalization bridges remain pending.

## 8. Level \((3,3)\): computationally eliminated, theorem-level certification pending

An exact mod-7 Brandt-module computation has now been completed on a common orbit module of dimension

\[
2026.
\]

At the two primes above `11`, the attainable pair is `(2,2)` and the simultaneous eigenspace has dimension `31`. After imposing the pair `(5,5)` at the two primes above `19`, the dimension is

\[
8.
\]

The four attainable ordered pairs at the two primes above `29` are

\[
(1,1),\ (2,2),\ (5,5),\ (6,6).
\]

For each of these four pairs, the exact stacked matrix over `F_7` has rank `2026`, so every corresponding simultaneous eigenspace has dimension zero.

Therefore no level-`(3,3)` Hecke packet survives the recorded computational sieve.

This is not yet a theorem-level elimination. The remaining certification must identify the computed Brandt module with the full relevant Hilbert newspace and verify the exact weight, level, central character, oldform, multiplicity, Eisenstein, and split-prime labelling conventions.

## 9. Current theorem-level conclusion

The established computational result is:

> Conditional on absolute irreducibility and the required theorem bridges, no residual Hecke packet survives the recorded computational sieves at any of the four Step-IV levels \((2,2)\), \((2,3)\), \((3,2)\), or \((3,3)\).

Absolute irreducibility is not yet theorem-level proved. The attempted direct auxiliary-prime certificate omits the separate `t=1` degeneration, which every quadratic survivor automatically satisfies; see `P7_900_DIRECT_LOCAL_CERTIFICATE_AUDIT.md`.

The desired theorem

\[
A^3+B^5=C^7,
\quad \gcd(A,B,C)=1
\quad\Longrightarrow\quad ABC=0
\]

cannot yet be claimed because the theorem-level local-integral and Jacquet--Langlands/Brandt completeness bridges are not yet fully written and verified.

## 10. Reproducibility checklist

The proof record should be accepted only after the following commands complete with the stated outputs:

```text
python3 scripts/open_theoremA_level2025_all.py
python3 scripts/p7_reducible_sieve_full.py
python3 scripts/p7_form_e_exact_branches.py
gp -q scripts/p7_infinity_normalized_qcharpoly.gp
python3 scripts/filter_level23_t11_t19_t29.py
python3 scripts/export_level33_dense.py
go build -o scripts/level33_rank scripts/level33_rank.go
scripts/level33_rank data/level33_t11_t19_dense.bin
python3 scripts/hecke_t29_pair_mod7.py 3
python3 scripts/export_level33_t29_dense.py
go build -o scripts/level33_rank_t29 scripts/level33_rank_t29.go
scripts/level33_rank_t29 data/level33_t11_t19_t29_dense.bin
```

Expected terminal facts:

```text
level (2,2) candidates: e,h,l only
reducible ray characters surviving: 0
form-e infinity q-charpoly survivors: []
level (2,3) total surviving dimensions: 0
level (3,3) rank1119=2018 dim1119=8
level (3,3) all_trace29_eliminated=true
```

## 11. Next proof task

The shortest remaining computational task is to eliminate the nine known level-\((3,2)\) packets. In parallel, the existing computational eliminations at levels \((2,3)\) and \((3,3)\) must be promoted to theorem-level statements by writing and verifying the Jacquet--Langlands/Brandt completeness bridge, and the level-\((2,2)\) local-integral arguments must be completed. A final proof audit over all primitive divisibility branches and signs is still required before any theorem claim.