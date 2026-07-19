# Exponent-switched (7,5,3) Frey computation

Status: 2026-07-17

## Quaternion algebra and initialization

The base field is (K=\mathbf Q(\zeta_7)^+), represented by the cubic variable `y`.

An explicit quaternion algebra split at exactly one real place and unramified at all finite places is

[
A=(a,b/K),qquad
a=385y^2-110y-935,quad
b=275y^2-385y-1484.
]

Correct PARI initialization:

```gp
beala=alginit(bealk,[385*qy^2-110*qy-935,
                     275*qy^2-385*qy-1484]);
bealn=12;
bealo=[matid(bealn),1];
```

Do not pass `qx` as the third argument to this explicit Hilbert-symbol `alginit`.
The resulting norm form has signature `[12,0]`.

## Completed level 35721

The Eichler level with local exponents `(2,2)` has

[
\operatorname{area}/\pi=2016,qquad -\chi=1008.
]

The full fdom computation at 100 decimal digits completed with:

- signature `[505, [], 0]`;
- genus (g=505);
- no elliptic cycles;
- no cusps;
- 6054 sides.

The independent check

[
2g-2=1008=-\chi
]

holds exactly.

Primary output: `data/fdom_level35721_tuned.txt`.

## Presentation and integral homology

The stored presentation was converted to its exponent-sum matrix by
`scripts/fdom_presentation_h1_35721.gp`.

Exact output:

```
GENERATORS=1010
RELATIONS=1
MIN_RELATION_LENGTH=2020
MAX_RELATION_LENGTH=2020
ABELIANIZATION_RELATION_RANK=0
H1_RANK=1010
NONZERO_EXPONENT_ENTRIES=0
```

Thus the presentation is the expected torsion-free compact surface presentation:
one length-(4g) relation whose abelianization vanishes, and

[
\operatorname{rank}H_1=1010=2g.
]

Output: `data/fdom_presentation_h1_35721.txt`.

## Hecke backend boundary

The upstream fdom package provides the required low-level primitives

- `afuchelts(X)`;
- `afuchpresentation(X)`;
- `afuchword(X,g)`;

but no Hecke, Brandt, homology, or cohomology operator.

The next implementation layer is therefore a sparse double-coset action.
For an auxiliary prime ideal (mathfrak l\nmid 3\cdot7):

1. enumerate the (N\mathfrak l+1) right cosets in the norm-(mathfrak l) correspondence;
2. for every presentation generator (gamma), solve
   (alpha_igamma=delta_{i,gamma}alpha_j);
3. reduce each (delta_{i,gamma}) with `afuchword`;
4. abelianize those words directly into sparse vectors of length 1010;
5. assemble (T_{mathfrak l}) on (H_1), avoiding dense Fox matrices.

The resulting characteristic polynomials/traces feed the already ported
`NewformBoundOverF`, including the inertia-degree recurrence and
(a\mapsto a^2-2N) for degree two.