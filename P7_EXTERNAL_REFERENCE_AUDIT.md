# External-reference audit for the two missing level-2025 cross-branches

## Purpose

This note records which parts of the current local argument are actually
supported by published or preprint literature, and which parts still require a
new calculation.

The remaining missing comparison is

    forms h,l in the t=infinity disk.

The initially questioned comparison of form `e` with the `t=0` disk is in fact
reproduced by `scripts/p7_form_e_exact_branches.py`: using the branch
polynomials from the Pacetti--Villagra data, it finds no compatible `t=0`
polynomial at auxiliary prime `ell=11`.

## 1. Pacetti--Villagra Torcomian

Primary source:

A. Pacetti and L. Villagra Torcomian,
"On the generalized Fermat equation of signature (5,p,3)",
arXiv:2512.17845 (2025).

The relevant source sections are 7.3 and 7.4.  Section 7.4 implements Mazur's
method by comparing Frobenius traces at auxiliary primes.  It separates three
reduction cases modulo an auxiliary rational prime and produces Theorem A by a
finite computation.  The supporting repository is

    https://github.com/lucasvillagra/GFE-5p3

The paper's own output for level (2,2) leaves three newforms, indexed there by
[3,9,12].  The theorem then states that a residual representation is either
reducible, congruent to a CM form, or congruent to one of two ghost forms.
Thus Section 7.4 is the source of the global auxiliary-prime sieve, but it does
not prove the two missing p=7 local cross-comparisons above.  In particular,
"exact branch sieve" must not be cited as if it identified the finite flat
7-torsion on the t=0 or t=infinity residue disks.

The paper explicitly presents the surviving ghost specializations as an
obstruction to the standard modular method and suggests further procedures,
such as a symplectic argument.  This is evidence that an additional local
invariant is genuinely required.

## 2. Conrad finite Honda systems

Primary source:

B. Conrad, "Finite Group Schemes over Bases with Low Ramification",
Compositio Math. 119 (1999), 239--320.

For a mixed-characteristic DVR of absolute ramification index e<p-1,
Conrad's Theorem 3.6 gives a fully faithful and essentially surjective
contravariant functor from finite flat commutative p-power group schemes to
finite Honda systems.  In the present application e=1 and p=7, so the strict
inequality is satisfied.

Lemma 4.1 is the appropriate source for extending an action on the generic
fibre to the finite flat model.  Consequently an isomorphism of residual
Galois representations coming from finite flat 7-torsion can be transported
to an isomorphism of the associated Honda systems, including the coefficient
order action.

What Conrad does not supply is the explicit Honda system for any of the four
objects in our comparison.  Those matrices still have to be computed from the
Frey models and the Hilbert forms.

## 3. Semistable toric branch

Useful modern source:

C. Gunton, "Semistable abelian varieties and maximal torsion
1-crystalline submodules", arXiv:1812.07936.

This source constructs the maximal 1-crystalline finite flat submodule inside
p-power torsion of a semistable abelian variety and relates it to the toric and
abelian parts of the reduction.  It supports the general mechanism behind the
t=1 argument, but it does not compute our specific rank-two toric character.
The latter still comes from the explicit stable model and Raynaud
uniformization.

## 4. Consequence for the proof status

The literature supports the following implications:

1. the auxiliary-prime elimination leaves precisely the exceptional forms;
2. finite flat residual isomorphisms can be tested on Honda systems at p=7;
3. the toric degeneration gives a distinguished 1-crystalline/cyclotomic
   submodule.

It does not provide a theorem saying that

    e differs from the t=0 Frey Honda system,
    h,l differ from the t=infinity Frey Honda system.

These are new explicit local comparisons.  The most economical next step is
to compute one common intrinsic invariant on all four finite Honda systems.
Candidates, in increasing order of strength, are:

- ranks of F and V on the special fibre;
- a-number and Ekedahl--Oort type;
- the coefficient-linear conjugacy class of divided Frobenius;
- the normalized q-Frobenius trace tau=Tr(Phi_q^2/7) mod 7.

The last invariant already eliminates e at infinity.  The immediate
computational objective is therefore to calculate tau for h,l and for the t=0
Frey model, or prove that tau is undefined there and replace it by the full
coefficient-linear Honda conjugacy class.