# Local conductor reduction of the three corrected quadratic survivors

## Exact ray conductors

The exact PARI/GP script

```text
scripts/identify_four_ray_chars.gp
```

returns

```text
(0,1)  conductor norm 5, infinity (1,1)
(90,0) conductor norm 45, infinity (0,0)
(90,1) conductor norm 9, infinity (1,1)
```

Over `F=Q(sqrt(5))`, these finite ideals are respectively

\[
(\sqrt5),
\qquad
(3)(\sqrt5),
\qquad
(3).
\]

Thus:

| character | at `(3)` | at `(sqrt(5))` |
|---|---|---|
| `(0,1)` | unramified | ramified quadratic |
| `(90,0)` | ramified quadratic | ramified quadratic |
| `(90,1)` | ramified quadratic | unramified |

All ramification here is tame: the characters have order two, while the residue characteristics are `3` and `5`.

## Conductor lemma for a reducible extension

Let `q` be a prime above `3` or `5`, and suppose

\[
\bar\rho^{ss}|_{G_{F_q}}
=\chi\oplus\bar\varepsilon_7\chi^{-1}.
\]

The mod-`7` cyclotomic character is unramified at `q`.

### If `chi` is unramified

The inertia action on a reducible extension is unipotent after a scalar unramified twist. Wild inertia is pro-`3` or pro-`5`, so it maps trivially to the additive order-`7` unipotent group. The Swan conductor is zero and inertia fixes a line. Hence

\[
a_q(\bar\rho)\le1.
\]

### If `chi` is ramified quadratic

After factoring out `chi`, inertia acts unipotently, but the scalar quadratic action is nontrivial. Since `chi` is tame and nontrivial, the inertia-fixed subspace is zero. Wild inertia is still trivial. Therefore

\[
a_q(\bar\rho)=2.
\]

The extension class cannot raise this to `3` because the only possible extra image is a tame unipotent `7`-group and the full two-dimensional space already has no inertia invariants.

## Elimination of `(0,1)`

The character `(0,1)` is unramified at `(3)`. Therefore any corresponding reducible representation has

\[
a_{(3)}(\bar\rho_7)\le1.
\]

The translated source Theorem 7.8 gives

\[
a_{(3)}(\bar\rho_7)=\epsilon_3\in\{2,3\}
\]

for every primitive branch. Contradiction.

Hence `(0,1)` is impossible.

## Elimination of `(90,1)`

The character `(90,1)` is unramified at `(sqrt(5))`. Therefore

\[
a_{(\sqrt5)}(\bar\rho_7)\le1,
\]

while Theorem 7.8 gives `epsilon_5 in {2,3}`. Contradiction.

Hence `(90,1)` is impossible.

## The remaining character `(90,0)`

The character `(90,0)` is ramified quadratic at both `(3)` and `(sqrt(5))`. Therefore a reducible representation with this semisimplification has exact local conductor exponents

\[
a_{(3)}(\bar\rho_7)=2,
\qquad
a_{(\sqrt5)}(\bar\rho_7)=2.
\]

Consequently it is compatible only with the source branch

\[
(\epsilon_3,\epsilon_5)=(2,2).
\]

It is incompatible with levels `(2,3)`, `(3,2)`, and `(3,3)`.

## Current irreducibility barrier

After the full auxiliary-prime sieve, corrected toric splitting condition, and local conductor comparison, Lemma D has exactly one remaining character:

\[
\boxed{\chi=(90,0),
\quad\operatorname{cond}(\chi)=(3)(\sqrt5),
\quad(\epsilon_3,\epsilon_5)=(2,2).}
\]

Closing residual irreducibility is now equivalent to eliminating this one quadratic Eisenstein-type residual representation at level `(2,2)`.