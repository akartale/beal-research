# Local Kummer-line audit for the final survivor `(90,0)`

## Setup

After twisting by the quadratic character `(90,0)`, the remaining reducible semisimplification is

\[
1\oplus\bar\varepsilon_7.
\]

The `t=0` and `t=infinity` normalized fibres at the inert prime above `7` have p-rank zero. Hence an ordinary reducible survivor must be sought in the totally toric `t=1` branch.

At `t=1`,

\[
F_1(x)=9(x^2-x-1)^2(5x^2-2x+1).
\]

The two nodes are at

\[
\alpha=w,\qquad \beta=1-w,
\qquad w^2-w-1=0.
\]

The Diophantine smoothing parameter is

\[
t-1=-C^7/A^3.
\]

## Local Kummer quotient

The script

```text
scripts/p7_local_kummer_cosets.py
```

computes the unit quotient

\[
(\mathcal O_{F_{\mathfrak p}}/49)^\times /
((\mathcal O_{F_{\mathfrak p}}/49)^\times)^7.
\]

It has order `49`. The image of rational 7-adic units is a subgroup of order `7`. The class of the fundamental unit `w` is not in that subgroup.

Thus a toric extension class represented by a rational unit cannot equal the global Selmer class represented by `w`.

## Node-smoothing coefficients

Let

\[
D(x)=\left.\frac{\partial F_t(x)}{\partial t}\right|_{t=1}=90x^3+18,
\]

\[
g(x)=x^2-x-1,
\qquad q(x)=5x^2-2x+1.
\]

For a node `x=alpha`, the first-order local smoothing coefficient is

\[
c_\alpha=\frac{D(\alpha)}{9g'(\alpha)^2q(\alpha)}.
\]

The exact script

```text
scripts/p7_t1_smoothing_kummer_line.py
```

computes modulo `49`:

```text
c_w     = 27+35w,
c_{1-w} = 13+14w.
```

Because `t-1=-C^7/A^3`, the seventh-power factor `C^7` disappears in local Kummer theory. Varying the rational unit `A` therefore produces the affine Kummer lines

\[
c_w\cdot \operatorname{im}(\mathbf Z_7^\times),
\qquad
c_{1-w}\cdot \operatorname{im}(\mathbf Z_7^\times).
\]

The exhaustive modulo-49 computation shows that neither line contains:

1. the split class;
2. the class of the fundamental unit `w`.

## What this proves

This is an exact separation for the two raw node-smoothing periods.

## Missing theorem bridge

The Frey Jacobian has toric rank two, while the residual RM representation is rank two over `F_7`. To turn the raw node-period calculation into a statement about the RM constituent, one must determine the action of real multiplication on the toric character lattice, or equivalently the monomial combination of the two node periods defining the RM extension class.

No explicit RM matrix on this character lattice is presently available in the repository. Therefore one must not yet identify either raw node class with the extension class of the RM constituent.

A theorem-level closure now requires one of:

- computing the RM correspondence on the dual graph/toric character lattice at `t=1`;
- deriving the induced RM projection on the Raynaud 1-motive and its Kummer parameter;
- an alternative Eisenstein or reducible-compatible level theorem.

## Status

The local obstruction has been narrowed from an arbitrary finite-flat extension class to an explicit RM projection problem on two certified Kummer lines. Lemma D is not yet closed by this calculation alone.