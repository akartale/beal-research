# The generalized Fermat equation of signature (3,5,7)

## A proof-status manuscript rebuilt from first principles

### Abstract

We study primitive nonzero integer solutions of

\[
A^3+B^5=C^7.
\]

The intended strategy is the modular method over \(F=\mathbf Q(\sqrt5)\), using the plus hypergeometric/Frey motive for the signature \((5,7,3)\). This manuscript is written from the beginning and records only deductions whose hypotheses have been checked. At present it is **not** a proof of nonexistence. The exact four-branch auxiliary-prime sieve reduces 360 ray characters to four quadratic characters. A corrected tangent-branch computation at \(7\) shows that the toric splitting character is the nontrivial unramified quadratic character, not the trivial character. Local conductor comparisons then eliminate two of the three nontrivial survivors and leave exactly one character, \((90,0)\), ramified quadratically at both \(3\) and \(5\), compatible only with conductor pair \((2,2)\). Thus Lemma D and absolute irreducibility remain open at one explicit Eisenstein-type character. All four Step-IV levels are computationally eliminated. Levels \((2,3)\), \((3,2)\), and \((3,3)\) are eliminated by exact mod-7 Brandt-module sieves at the split primes 11, 19, and 29, but the theorem-level Jacquet--Langlands/Brandt completeness bridge remains pending.

## 1. The Diophantine problem

A solution is called primitive when

\[
\gcd(A,B,C)=1.
\]

A solution is nontrivial when \(ABC\ne0\). The desired theorem is:

> **Target theorem.** There are no primitive nontrivial integer solutions of
> \[
> A^3+B^5=C^7.
> \]

No statement below should be read as claiming this theorem until every item in the final gap ledger is closed.

## 2. Translation to the source equation

The source modular framework studies

\[
x^5+y^p+z^3=0.
\]

Our equation is obtained by

\[
p=7,\qquad x=B,\qquad y=-C,\qquad z=A.
\]

Thus the source variables \((a,b,c)\) correspond to

\[
(a,b,c)=(B,-C,A).
\]

Every condition imported from the source paper must be translated through this identification. In particular, a hypothesis involving the source variable \(b\) is a hypothesis on \(-C\), and a hypothesis involving the source variable \(c\) is a hypothesis on \(A\).

The source paper's final Theorem A excludes a finite set of small primes containing 7. Therefore its final nonexistence theorem does not cover the present exponent directly. We must separately prove irreducibility and eliminate all residual newform packets at \(p=7\).

## 3. The residual representation

Let

\[
F=\mathbf Q(\sqrt5),
\]

and let \(\mathfrak p_7\) be the unique prime of \(F\) above 7. Since 7 is inert in \(F\),

\[
F_{\mathfrak p_7}/\mathbf Q_7
\]

is unramified of degree two, has absolute ramification index 1, and has residue field \(\mathbf F_{49}\).

The plus Frey motive supplies a two-dimensional residual representation over the RM coefficient field,

\[
\bar\rho_7:G_F\longrightarrow \mathrm{GL}_2(\overline{\mathbf F}_7).
\]

The source results state, for the relevant specialization and prime above 7, that the residual representation is unramified outside the expected bad primes and finite at \(\mathfrak p_7\). The modularity statement is available for the \((5,7,3)\) motive after the standard Tate normalization. These source inputs must be cited with the exact theorem numbers and with the variable translation above.

The intended proof first establishes absolute irreducibility and then applies Hilbert modular level lowering.

## 4. Lemma A: possible finite-flat inertia characters

Assume that \(\bar\rho_7\) is absolutely reducible. After semisimplification,

\[
\bar\rho_7^{\mathrm{ss}}=\chi_1\oplus\chi_2,
\qquad
\chi_1\chi_2=\bar\varepsilon_7.
\]

Because \(e(F_{\mathfrak p_7}/\mathbf Q_7)=1<7-1\), the generic-fibre functor on finite flat commutative 7-primary group schemes is fully faithful and exact. Raynaud's tame-character theorem gives, for a simple Jordan--Hölder quotient, digits in \(\{0,1\}\).

A diagonal constituent is a character of the full decomposition group. Arithmetic Frobenius acts on tame inertia by the 49th-power map, so scalar-valued characters satisfy Frobenius invariance. The Raynaud digit sequence is therefore periodic with period dividing two. Consequently every diagonal tame character descends to niveau at most two and has exponent

\[
n=a_0+7a_1,
\qquad a_0,a_1\in\{0,1\}.
\]

Thus

\[
n\in\{0,1,7,8\}.
\]

Since

\[
\det(\bar\rho_7)|_{I_{\mathfrak p_7}}
=ar\varepsilon_7|_{I_{\mathfrak p_7}}
=\\omega_2^8,
\]

up to exchange the possible inertia multisets are

\[
\{0,8\}\quad\text{and}\quad\{1,7\}.
\]

The first is the ordinary branch; the second is the niveau-two branch.

### Audit status of Lemma A

The numerical hypotheses \(e=1<6\) and residue degree two are correct. The previously missing categorical passage is supplied directly by Raynaud, Corollary 3.4.4: the statement starts with a generic finite commutative group scheme killed by a power of \(p\) which admits a finite-flat prolongation, and applies its character classification to every generic-fibre Jordan--Hölder quotient. Thus one does not need to lift a chosen \(\overline{\mathbf F}_7\)-stable line as an independently defined finite-flat subgroup. Instead, one takes a simple Jordan--Hölder factor over \(\mathbf F_7\); Raynaud equips it with a one-dimensional structure over a suitable finite endomorphism field and bounds its tame digits by \(e\).

Conrad, Lemma 4.1, independently states that for \(e<p-1\) the finite-flat category is abelian and the generic-fibre functor is fully faithful and exact. This corroborates the categorical argument but is not being used to assume descent of the stable line. Accordingly, the finite-flat/Jordan--Hölder gap in Lemma A is closed, conditional only on the source representation genuinely satisfying the quoted finite-flat hypothesis at \(\mathfrak p_7\).

## 5. Lemma B: conductor bounds for diagonal characters

Away from \(3,5,7\), the source representation is unramified, so both diagonal characters are unramified.

At primes above 3 and \(\sqrt5\), the source conductor exponents lie in \(\{2,3\}\). For a finite inertia quotient, semisimplification cannot increase the Artin conductor: for every lower ramification group, the invariant dimension of the semisimplification is at least the invariant dimension of the original representation. Therefore

\[
a_{\mathfrak q}(\bar\rho_7^{\mathrm{ss}})
\le a_{\mathfrak q}(\bar\rho_7).
\]

Since Artin conductors are additive on direct sums,

\[
a_{(3)}(\chi_i)\le3,
\qquad
a_{(\sqrt5)}(\chi_i)\le3.
\]

At \(\mathfrak p_7\), Lemma A gives either an unramified constituent in the ordinary branch or tame conductor exponent one in the niveau-two branch. Hence the diagonal characters factor through ray class groups of moduli

\[
\mathfrak m_0=(3)^3(\sqrt5)^3\infty_1\infty_2
\]

or

\[
\mathfrak m_1=\mathfrak m_0\mathfrak p_7.
\]

### Audit status of Lemma B

The internal conductor inequality is sound. The remaining dependency is external: the exact source conductor table must be checked for every primitive divisibility branch after substituting \((a,b,c)=(B,-C,A)\). A bound stated only for one valuation branch is not sufficient. Until that table is transcribed branch by branch, Lemma B remains conditional on the source conductor input.

## 6. Excluding the niveau-two reducible branch

The ray class computations give

\[
\mathrm{Cl}_{\mathfrak m_0}(F)\simeq \mathbf Z/180\mathbf Z\oplus\mathbf Z/2\mathbf Z,
\]

and

\[
\mathrm{Cl}_{\mathfrak m_1}(F)\simeq
\mathbf Z/360\mathbf Z\oplus\mathbf Z/12\mathbf Z\oplus\mathbf Z/2\mathbf Z.
\]

Hence the kernel of

\[
\mathrm{Cl}_{\mathfrak m_1}(F)	o\mathrm{Cl}_{\mathfrak m_0}(F)
\]

has order 24. The exact ray-class sequence identifies this kernel with a quotient of

\[
(\mathcal O_F/\mathfrak p_7)^*=\mathbf F_{49}^*,
\]

which has order 48. The image of the relevant global-unit subgroup therefore has order two, hence equals \(\{\pm1\}\). Every global ray character is trivial on \(-1\), so its local tame exponent is even. This excludes the odd exponents 1 and 7.

### Audit status

This step is plausible and computationally supported. The final manuscript must display the exact ray-class sequence, including the unit subgroup and the infinite-sign conditions, rather than infer the local map only from group orders. Reciprocity may invert the tame character, but inversion does not affect parity.

## 7. Lemma C: all ordinary ray characters

In the ordinary branch, choose \(\chi\) to be the constituent unramified at \(\mathfrak p_7\). Then

\[
\bar\rho_7^{\mathrm{ss}}
=\chi\oplus\bar\varepsilon_7\chi^{-1},
\]

and \(\chi\) factors through \(\mathrm{Cl}_{\mathfrak m_0}(F)\).

Because the ray class group has order \(360\), prime to 7, it has exactly 360 characters with values in \(\overline{\mathbf F}_7^*\). The computation does not assume that the values lie in \(\mathbf F_{49}\). A common field of definition is \(\mathbf F_{7^{12}}\).

At the two primes above 19, the chosen ray-class coordinates are independently computed as

\[
[141,1],\qquad[141,1].
\]

### Audit status of Lemma C

The character count and field-of-definition treatment are complete. The coordinate computation is reproducible. The use of both primes above 19 is correct and must remain paired.

## 8. Lemma D: the auxiliary-prime sieve at 19

The existing script enumerates

\[
(A,B)\in(\mathbf F_{19}^*)^2,
\qquad A^3+B^5\ne0,
\]

retains nonsingular reductions of the genus-two Frey curve, computes the degree-four Frobenius polynomial, and extracts the unordered pair of RM traces modulo 7. It obtains 15 trace-pair polynomials. Comparing these against all 360 ray characters gives

```text
actual_trace_pairs=15
survivors_at_l19_pairwise=0
survivors=[]
```

This computation is correct for the good-reduction branch

\[
19\nmid ABC.
\]

### Exact all-branch repair of Lemma D

The upstream computation does not model the exceptional cases by an unrestricted pair of values \(\pm(\ell+1)\). Instead, at each auxiliary prime it supplies four exact branches:

1. the generic good-reduction branch;
2. the degeneration \(t=0\);
3. the degeneration \(t=1\);
4. the degeneration \(t=\infty\).

For the generic branch the ray-character trace is compared directly with the upstream trace polynomial. For \(t=0\) and \(t=\infty\), the comparison uses the upstream invariant

\[
a_{\mathfrak l}^2-2\ell
\]

when the relevant residue-degree ratio is two, and uses \(a_{\mathfrak l}\) when that ratio is one. For \(t=1\), the exact congruence is

\[
a_{\mathfrak l}\equiv\pm(\ell+1)\pmod7.
\]

The paired calculation was run at both primes above every split rational prime in the upstream data set:

\[
11,19,29,31,41,59,61,71,79,89,101,109,131,139,149,151,
\]

\[
179,181,191,199,211,229,239,241,251,269,271,281,311,331,349,359,379,389.
\]

At each rational prime the four exact branch sets were first united, and the resulting character sets were then intersected across primes. The survivor counts begin

\[
20\longrightarrow8\longrightarrow8\longrightarrow4
\]

at \(11,19,29,31\), and remain equal to four through \(389\). The exact survivor set is

\[
\boxed{(0,0),\ (0,1),\ (90,0),\ (90,1)}.
\]

Their exact ray conductors are:

\[
\begin{array}{c|c|c}
\text{character}&\text{finite conductor}&\text{infinite part}\\
\hline
(0,0)&1&(0,0)\\
(0,1)&\begin{pmatrix}5&2\\0&1\end{pmatrix}&(1,1)\\
(90,0)&\begin{pmatrix}15&6\\0&3\end{pmatrix}&(0,0)\\
(90,1)&\begin{pmatrix}3&0\\0&3\end{pmatrix}&(1,1)
\end{array}
\]

All four are quadratic, including the trivial character. This explains why the auxiliary-prime sieve stabilizes. At every unramified prime, a quadratic character satisfies

\[
\chi(\mathrm{Frob}_{\mathfrak l})\in\{\pm1\},
\]

and therefore

\[
\chi(\mathrm{Frob}_{\mathfrak l})
+\ell\chi(\mathrm{Frob}_{\mathfrak l})^{-1}
=\pm(\ell+1).
\]

Thus every quadratic character automatically satisfies the \(t=1\) trace congruence. Adding more auxiliary primes of the same type cannot eliminate these four characters.

### Corrected local refinement at 7

The two roots of the node polynomial are indeed rational over the actual residue field \(\mathbf F_{49}\), but this does not imply that the torus is split. One must also test the two tangent branches at each node.

Writing the special fibre as

\[
f(x)=g(x)^2q(x),
\qquad
g(x)=x^2+6x+6,
\qquad q(x)=5x^2+5x+1,
\]

the local equation at a root \(\alpha\) of \(g\) has leading term

\[
y^2=q(\alpha)u^2.
\]

The exact computation in `scripts/p7_t1_branch_splitting.py` gives

\[
q(\alpha)^{24}=q(\beta)^{24}=-1
\]

in \(\mathbf F_{49}\). Hence both tangent values are nonsquares. Frobenius fixes each node but exchanges its two local branches, so the toric splitting character is the nontrivial unramified quadratic character \(\delta\), with

\[
\delta(\operatorname{Frob}_{\mathfrak p_7})=-1.
\]

On the rank-one RM toric line the character is \(\bar\varepsilon_7\delta\), and the quotient line has character \(\delta\). Thus

\[
\bar\rho_7^{\mathrm{ss}}|_{G_{F_{\mathfrak p_7}}}
\simeq
\delta\oplus\bar\varepsilon_7\delta,
\]

not \(1\oplus\bar\varepsilon_7\).

The ray-class values at \(\mathfrak p_7\) are

\[
(0,0)\mapsto1,
\qquad
(0,1),(90,0),(90,1)\mapsto-1.
\]

Therefore the corrected local condition eliminates the trivial character and retains the three nontrivial quadratic characters. Lemma D remains open; see `P7_T1_TORIC_SPLITTING_CORRECTION.md`.

### Final elimination of the trivial character at 3 and 5

It remains to exclude

\[
\bar\rho_7^{\mathrm{ss}}=1\oplus\bar\varepsilon_7.
\]

Let \(\mathfrak q\) be a prime of \(F\) above \(3\) or \(5\). Since \(\mathfrak q\nmid7\), both \(1\) and \(\bar\varepsilon_7\) are unramified at \(\mathfrak q\). If \(\bar\rho_7\) is reducible with this semisimplification, then after choosing the invariant line its restriction to inertia has the form

\[
\bar\rho_7(\sigma)=
\begin{pmatrix}
1&c(\sigma)\\
0&1
\end{pmatrix},
\qquad \sigma\in I_{\mathfrak q}.
\]

The image is therefore an additive \(7\)-group. The wild inertia subgroup is pro-\(3\), respectively pro-\(5\), and hence maps trivially to this \(7\)-group. Thus the Swan conductor is zero. Moreover the inertia-fixed subspace has dimension at least one, so the tame conductor is at most one. Consequently

\[
a_{\mathfrak q}(\bar\rho_7)\le1.
\tag{D.1}
\]

On the other hand, the exact source conductor calculation applies directly to the branch \(30\mid C\). Under the translation

\[
(a,b,c)=(B,-C,A)
\]

from \(A^3+B^5=C^7\) to \(a^5+b^7+c^3=0\), one has \(3\mid b\) and \(5\mid b\). Lemma 7.3 of Pacetti--Villagra Torcomian proves that the congruence between the hypergeometric representation and the relevant Jacobian factor holds over \(F\) without a quadratic twist. At the prime above \(3\), Corollary 3.6 together with Remark 3.7 applies because \(3\mid ab\); at the prime above \(5\), Proposition 3.14 together with the transported form of Remark 3.12 applies because \(5\mid bc\). In both cases the local type is special with a ramified quadratic character and trivial Nebentypus. Since the residual characteristic is \(7\), reduction preserves that quadratic character. Hence

\[
a_{(3)}(\bar\rho_7)=2,
\qquad
a_{(\sqrt5)}(\bar\rho_7)=2.
\tag{D.2}
\]

Either equality in (D.2) contradicts (D.1). Therefore the trivial character is impossible.

Combining this with the exact ray-character sieve and the split-toric test at \(7\) proves:

\[
\boxed{\text{Lemma D. The ordinary reducible branch is empty.}}
\]

The exact conductor factorizations of the four intermediate survivors remain useful as a consistency check:

\[
\begin{array}{c|c}
\chi&\text{finite conductor support}\\
\hline
(0,0)&1\\
(0,1)&\mathfrak p_5\\
(90,0)&\mathfrak p_3\mathfrak p_5\\
(90,1)&\mathfrak p_3.
\end{array}
\]

The scripts `scripts/identify_four_ray_chars.gp`, `scripts/generate_lemmaD_union_all_split_gp.py`, `scripts/lemmaD_union_all_split.gp`, `scripts/factor_four_conductors.gp`, and `scripts/eta35_at_7.gp` reproduce the finite computations used above.

## 9. Present irreducibility status

The niveau-two reducible branch is excluded by the ray-class exponent argument, and Lemma D now excludes the ordinary reducible branch. Subject to the finite-flat inertia classification and the categorical generic-fibre/Jordan--Hölder passage recorded in Lemma A, the residual representation is absolutely irreducible:

\[
\boxed{\bar\rho_7\text{ is absolutely irreducible}.}
\]

This completes the previously open ordinary part of Step III. It does not by itself close the later newform-elimination levels in Step IV.

## 10. Modularity and level lowering

If absolute irreducibility is established, the source modularity theorem and Hilbert modular level lowering produce a parallel-weight-two Hilbert newform over \(F\), with trivial Nebentypus and level supported at the primes above 3 and 5.

The possible exponent pairs are

\[
(r,s)\in\{2,3\}\times\{2,3\},
\]

corresponding to levels

\[
3^r(\sqrt5)^s.
\]

Since 3 is inert in \(F\),

\[
\mathrm N((3))=9,
\qquad
\mathrm N((\sqrt5))=5.
\]

The level norms are therefore

\[
(2,2):2025,
\quad(3,2):18225,
\quad(2,3):10125,
\quad(3,3):91125.
\]

### Audit obligations before invoking level lowering

The final proof must explicitly verify:

1. modularity of the chosen plus motive for \((q,p,r)=(5,7,3)\);
2. absolute irreducibility in the precise sense required by the level-lowering theorem;
3. finite flatness at the prime above 7;
4. determinant and Nebentypus normalization after the Tate twist;
5. minimality/conductor exponents for every valuation branch;
6. that no oldform or lower-level contribution is omitted from the candidate spaces.

## 11. Level \((2,2)\), norm 2025

The source auxiliary-prime computation leaves exactly three candidates,

\[
2025.1\text{-}e,
\qquad2025.1\text{-}h,
\qquad2025.1\text{-}l.
\]

The repository contains local calculations intended to eliminate all three over all 7-adic residue disks. These include Hasse--Witt ordinarity, stable toric reduction, divided-Frobenius ranks, and a normalized \(q\)-Frobenius invariant.

### Audit status

The computations are substantial and reproducible, but three theorem-level bridges still require a polished proof:

1. every primitive solution must lie in exactly one of the listed normalized disks, with no omitted valuation/sign branch;
2. the explicit CM model used for \(h,l\) must be related to the actual local systems by a rigorously identified unramified twist, not merely by a matching zero pattern;
3. the matrices returned by `hyperellpadicfrobenius` must be proved to represent the correct integral finite-Honda lattice, not only rational crystalline cohomology, before divided-Frobenius rank is used as a torsion invariant.

Accordingly, level \((2,2)\) is computationally very close to closed, but the manuscript should describe it as **conditionally closed pending these local-integrality and exhaustiveness bridges**.

## 12. Level \((2,3)\), norm 10125

An exact mod-7 Brandt-module computation has dimension 226 and yields the reductions

\[
226\xrightarrow{\ell=11}8
\xrightarrow{\ell=19}4
\xrightarrow{\ell=29}0.
\]

No simultaneous eigenspace survives the attainable paired Frey traces used by the script.

### Audit status

Before this becomes a theorem-level elimination, the following must be certified:

1. the Brandt module is canonically the full relevant parallel-weight-two cuspidal space at the exact level and character;
2. the chosen quaternion algebra and Eichler order have the correct ramification and level;
3. oldspaces, degeneracy maps, and multiplicities are handled correctly;
4. the two Hecke operators above each split rational prime are correctly labelled and normalized;
5. the Frey trace-pair sets include every good, multiplicative, and zero-coordinate reduction branch compatible with a primitive solution;
6. the mod-7 linear-algebra calculation is independently checkable from stored matrices/hashes.

The computation is compelling, but these bridges are not yet written as a complete certification. Thus the safest current label is **computationally eliminated, theorem-level certification pending**.

## 13. Level \((3,2)\), norm 18225

The historical characteristic-zero candidate set is

\[
C_{32}=\{21,22,26,33,61,65,78,92,98\}.
\]

The repository now bypasses packet-by-packet reconstruction by computing the full exact mod-7 Brandt module at this level. Its orbit dimension is

\[
406.
\]

The attainable pair `(2,2)` at the two primes above `11` cuts the module to dimension `15`. Adding the pair `(5,5)` at the two primes above `19` cuts it to dimension `4`.

At the two primes above `29`, the attainable ordered pairs are

\[
(1,1),\ (2,2),\ (5,5),\ (6,6).
\]

Each of the four corresponding simultaneous eigenspaces has dimension zero. Therefore

\[
406\xrightarrow{\ell=11}15
\xrightarrow{\ell=19}4
\xrightarrow{\ell=29}0.
\]

The computation is implemented in `scripts/level32_brandt_mod7.py` and certified in `LEVEL_32_CERTIFICATE.md`.

### Audit status

This is a computational elimination, not yet a theorem-level elimination. The same Jacquet--Langlands/Brandt completeness, newspace, oldform, multiplicity, Eisenstein, residue-field, and split-prime-labelling obligations described for the other Brandt levels must be proved here.

## 14. Level \((3,3)\), norm 91125

The repository now contains an exact mod-7 Brandt-module computation on a common orbit module of dimension

\[
2026.
\]

The two operators above `11`, with Frey trace pair `(2,2)`, cut the module to dimension `31`. Adding the two operators above `19`, with Frey trace pair `(5,5)`, cuts it further to dimension

\[
8.
\]

At `29`, the attainable ordered trace pairs are

\[
(1,1),\ (2,2),\ (5,5),\ (6,6).
\]

For each of these four pairs, the exact stacked operator matrix over `F_7` has full rank `2026`. Therefore every simultaneous eigenspace compatible with the recorded Frey trace conditions at `11`, `19`, and `29` is zero.

The computational conclusion is:

> The simultaneous mod-7 eigenspace satisfying the Frey trace conditions at the primes above `11`, `19`, and `29` is zero for every attainable ordered trace tuple. Hence no level-`(3,3)` Hecke packet survives this computational sieve.

### Audit status

This is a computational elimination, not yet a theorem-level elimination. To promote it into Step IV, the manuscript must still prove the exact Jacquet--Langlands/Brandt correspondence for the relevant parallel weight, level and central character, establish completeness of the computed newspace, and account for oldforms, multiplicities, Eisenstein classes, and the labelling of the two primes above each split rational prime.

## 15. Primitive and sign branches

A final proof must also audit the elementary reduction before attaching the Frey motive:

1. treatment of \(A=0\), \(B=0\), or \(C=0\);
2. passage from arbitrary integer signs to the source parameter \(t\);
3. pairwise coprimality consequences of \(\gcd(A,B,C)=1\);
4. all possibilities for divisibility by 2, 3, 5, 7, and each auxiliary prime;
5. compatibility of scaling/normalization with integrality and primitivity;
6. whether the plus or minus motive is required in each sign branch.

These reductions are not yet assembled in one proof.

## 16. Current rigorous conclusion

The repository establishes a large body of exact computations and several strong local lemmas. It does **not** yet establish the target theorem. The ordinary reducible branch has been computationally closed by the exact all-branch sieve and local conditions recorded above, subject to the cited source conductor and no-twist inputs.

All four Step-IV levels are computationally eliminated. Level \((2,2)\) still requires theorem-level certification of the local-integral arguments, while levels \((2,3)\), \((3,2)\), and \((3,3)\) require theorem-level certification of the Brandt/Jacquet--Langlands bridge.

## 17. Reproducibility record

The original good-reduction Lemma-D calculation is reproduced by

```text
gp -q scripts/eliminate_all_c0_l19_pairs.gp
```

with output

```text
actual_trace_pairs=15
survivors_at_l19_pairwise=0
survivors=[]
```

The conservative all-branch audit is reproduced by

```text
gp -q scripts/audit_l19_all_branches.gp
```

with output beginning

```text
actual_pairs_with_conservative_special=18
survivors=24
```

The latter script is an audit bound, not a final exact local calculation.

## 18. Next exact tasks

The proof should proceed in this order:

1. write and verify the complete primitive/sign/valuation reduction;
2. certify the level-\((2,2)\) local integral-Honda arguments;
3. certify the level-\((2,3)\), level-\((3,2)\), and level-\((3,3)\) Brandt/Jacquet--Langlands identifications, newspace completeness, and all-branch trace sets;
4. verify oldforms, multiplicities, Eisenstein classes, residue-field extension, and split-prime labelling conventions;
5. rerun the proof audit from Section 1 with no conditional labels remaining.