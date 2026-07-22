# Audit of the attempted direct local certificate for the character `(90,0)`

## Summary

The file

```text
data/p7_900_direct_local_certificate.json
```

correctly compares the reducible target attached to `(90,0)` against three upstream local data sets:

1. `Candidates(q)`, corresponding to generic parameters `t=2,...,q-1`;
2. `Degenerate0(q)`;
3. `Degenerateoo(q)`.

It finds no match at `q=19,79,89,131` in those three sets.

This is a valid partial local computation, but it is **not an exhaustive all-branch irreducibility certificate**.

## Missing branch

The upstream function `Candidates(q)` explicitly loops over

```text
for(i=2,q-1,...)
```

and therefore excludes `t=1`. The tuple written to `Data.txt` contains only

```text
<Candidates(q), Degenerate0(q), Degenerateoo(q)>
```

and has no fourth `t=1` entry.

The separate exact all-branch scripts correctly impose at `t=1` the Steinberg/toric congruence

\[
a_{\mathfrak q}\equiv \pm(q+1)\pmod 7.
\]

For a quadratic ray character,

\[
\chi(\operatorname{Frob}_{\mathfrak q})\in\{\pm1\},
\]

so the reducible trace

\[
\chi(\operatorname{Frob}_{\mathfrak q})
+q\chi(\operatorname{Frob}_{\mathfrak q})^{-1}
\]

is automatically `+(q+1)` or `-(q+1)`. Hence every quadratic survivor, including `(90,0)`, automatically passes the `t=1` branch at every unramified auxiliary prime.

## Consequence

The primes `19,79,89,131` eliminate `(90,0)` only under the additional hypothesis that the corresponding specialization is not in the `t=1` disk, equivalently that the auxiliary prime does not divide the relevant Diophantine coordinate `C`.

A finite collection of such primes does not give an unconditional contradiction: a hypothetical integer `C` may be divisible by all of them.

Therefore the attempted certificate does **not** close Lemma D and must not be cited as proving absolute irreducibility.

## Exact remaining obstruction

After twisting by `(90,0)`, the final reducible semisimplification is

\[
1\oplus\bar\varepsilon_7.
\]

A noncircular closure must exclude:

1. the split representation `1 direct_sum bar epsilon_7`;
2. extensions of `1` by `bar epsilon_7`;
3. extensions of `bar epsilon_7` by `1`;

with the actual finite-flat condition at `7` and the prescribed quadratic tame local conditions at the primes above `3` and `5` before undoing the twist.

The presently viable theorem-level routes are:

- an explicit Selmer calculation together with a separate exclusion of the split case;
- an integral Hilbert Eisenstein theorem whose hypotheses and all-cusp constant-term ideal match this exact stabilization;
- a reducible-compatible exact-level modularity theorem, which would allow use of the already completed level-`(2,2)` Brandt certificate without circularity.