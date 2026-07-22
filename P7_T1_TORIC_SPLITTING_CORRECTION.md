# Correction: toric splitting character in the t=1 branch at 7

## Exact stable fibre

At `t=1`, over `F_7`,

\[
f(x)=g(x)^2q(x),
\]

with

\[
g(x)=x^2+6x+6,
\qquad
q(x)=5x^2+5x+1.
\]

The prime `7` is inert in `F=Q(sqrt(5))`, so the actual residue field is `F_49`. The two roots `alpha,beta` of `g` are rational over `F_49`; hence the two ordinary nodes are `F_49`-rational.

Rationality of the nodes alone does not determine whether the torus is split. One must also check the two tangent branches at each node.

## Tangent-branch test

Near a root `alpha` of `g`, write `x=alpha+u`. The leading local equation is

\[
y^2=q(\alpha)u^2.
\]

The two branches are rational over `F_49` exactly when `q(alpha)` is a square in `F_49`.

The exact script

```text
scripts/p7_t1_branch_splitting.py
```

uses

\[
F_{49}=F_7[a]/(a^2-a-1)
\]

and computes

```text
q(alpha)^24 = -1
q(beta)^24  = -1
branches_split_over_F49 False
branch_splitting_character_at_Frob49 -1
toric_splitting_character=unramified_quadratic
```

Thus both tangent values are nonsquares in `F_49`. Frobenius fixes each node but exchanges the two local branches at it.

## Correct toric character

The rank-two torus is not split over `K=F_{p7}`. It becomes split over the unramified quadratic extension of `K`. Its splitting character is the nontrivial unramified quadratic character

\[
\delta:G_K\to\{\pm1\},
\qquad
\delta(\operatorname{Frob}_K)=-1.
\]

Real multiplication still makes the toric Tate submodule rank one over `O_F tensor Z_7`. Therefore the toric line on the two-dimensional RM representation has character

\[
\bar\varepsilon_7\delta,
\]

and the other line has character `delta`, because the determinant is `bar epsilon_7`.

Hence the correct local semisimplification is

\[
\boxed{\bar\rho_7^{ss}|_{G_K}
       \simeq \delta\oplus\bar\varepsilon_7\delta,}
\]

not `1 direct_sum bar epsilon_7`.

## Consequence for the four ray characters

The four auxiliary-prime survivors evaluate at `Frob_p7` as

```text
(0,0)   ->  1
(0,1)   -> -1
(90,0)  -> -1
(90,1)  -> -1
```

The corrected local toric condition therefore eliminates the trivial character `(0,0)` and retains the three nontrivial quadratic characters. The earlier argument did the reverse because it checked node rationality but not tangent-branch rationality.

The uniform conductor contradiction for a trivial character remains valid, but it is no longer the relevant final step after the corrected toric condition.

## Current Lemma D barrier

Lemma D remains open. To close it one must eliminate

```text
(0,1), (90,0), (90,1)
```

by an additional local or global condition not already encoded in the four-branch auxiliary-prime sieve. Adding more auxiliary primes with the same `t=1` degeneration condition cannot remove them, because each has the required local value `-1` at `p7` and each is quadratic at the auxiliary primes.