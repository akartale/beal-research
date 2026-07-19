# Special p=7 disks after abandoning unbounded AFUCH completion

## Decision

The unbounded AFUCH `normbasis` retry loop is no longer the primary route.
The three level-2025 survivors already have extensive Hecke data in
`data/lmfdb/level_2025`, and the standard auxiliary-prime sieve fails for a
structural reason rather than from missing coefficients.

The exact surviving forms are

    2025.1-e, 2025.1-h, 2025.1-l.

The branch diagnosis is:

- `e` is the `t=infinity` special-fibre obstruction;
- `h` and `l` are the `t=0` special-fibre obstruction.

Thus computing additional ordinary Hecke coefficients cannot by itself remove
these congruences.  The next proof step must distinguish a genuine integral
Frey specialization from the corresponding special fibre inside the relevant
7-adic residue disk.

## Arithmetic translation

For

    A^3 + B^5 = C^7,
    t = -B^5/A^3,

there are two special branches:

1. `7 | B`, `7 \nmid AC`: finite disk `t=0`;
2. `7 | A`, `7 \nmid BC`: disk `t=infinity`.

The Hasse--Witt computation already eliminates every finite nonzero residue of
`t` modulo 7.  Therefore only these two disks remain at level 2025.

## Exact power-residue diagnostic

The script

    scripts/p7_special_disks_power_residues.py

computes exact intersections modulo `7^k` between:

- seventh powers and fifth powers in the `7 | A` branch;
- seventh powers and cubes in the `7 | B` branch.

For `k=1,2,3,4` the intersection sizes are respectively

    7 | A: 6, 6, 42, 294;
    7 | B: 2, 2, 14, 98.

Hence neither branch has a pure unit power-residue contradiction through
`7^4`.  The persistent scaling shows that merely increasing an elementary
modulus is not a promising proof strategy.

## Explicit Frey model and discriminant

The upstream quotient computation gives the genus-2 model

    y^2 = 45x^6 - 108x^5 + 90tx^3 + 9t^2.

The exact polynomial discriminant is

    2^12 * 3^26 * 5^5 * t^8 * (t-1)^2.

This is reproduced by `scripts/frey_model_discriminant.gp`.

### Disk `t=0`

Write

    t = 7^(5b) u,

with `b>=1` and `u` a 7-adic unit.  The Newton polygon has five roots of
valuation `2b` and one unit root.  With

    x = 7^(2b) X,
    y = 7^(5b) Y,

one obtains the integral model

    Y^2 = 45*7^(2b)X^6 - 108X^5 + 90*7^b*u*X^3 + 9u^2.

Its reduction is

    Y^2 = -108X^5 + 9u^2,

which is smooth over `F_7` for every unit residue `u`.

### Disk `t=infinity`

Put `s=1/t` and `Y=y/t`, so

    Y^2 = 45s^2x^6 - 108s^2x^5 + 90sx^3 + 9.

Write

    s = 7^(3a) v,

with `a>=1` and `v` a 7-adic unit.  The Newton polygon gives six roots of
valuation `-a`.  With `x=7^(-a)X` one obtains

    Y^2 = 45v^2X^6 - 108*7^a*v^2X^5 + 90vX^3 + 9.

Its reduction is

    Y^2 = 45v^2X^6 + 90vX^3 + 9,

again smooth for every unit residue `v`.

The corresponding discriminant orders before normalization are

    v_7(Disc_t0) = 40b,
    v_7(Disc_infinity_chart) = 30a.

## Local zeta data of the normalized reductions

The script `scripts/p7_special_disks_reductions.py` computes `N_1`, `N_2`,
and the first two Weil coefficients.

For the `t=0` disk, every unit class has

    N_1 = 8,
    a_1 = 0,
    N_2 = 50,
    a_2 = 0,

so the local Weil polynomial is

    1 + 49 T^4.

For the `t=infinity` disk, always `a_1=0`, but `a_2` depends on the unit class:

    a_2 = 7   for v mod 7 in {1,3,4,6},
    a_2 = -14 for v mod 7 in {2,5}.

Thus the second Weil coefficient distinguishes two infinity subbranches even
though the rational trace does not.  The `t=0` branch is completely rigid at
this level.

## Cartier--Manin and Ekedahl--Oort separation

The symbolic computation is reproduced by

    scripts/p7_special_disks_hasse_witt.py.

Using the basis `dx/y, x dx/y` and the convention

    M = [[c_6,c_5],[c_13,c_12]]

for the coefficients of `f(x)^3`, the two disks give:

### Disk `t=0`

    M_0(u) = [[0,-u^4],[0,0]]

(up to the harmless transpose convention).  Hence for every unit `u`:

    rank(M_0)=1,
    M_0^2=0,
    p-rank=0,
    a-number=1.

### Disk `t=infinity`

    M_infinity(v)=0

for every unit `v`.  Hence

    p-rank=0,
    a-number=2.

Thus the two special disks have the same `p`-rank but different
Cartier--Manin/Ekedahl--Oort type.  This is strictly finer than all ordinary
mod-7 trace tests and gives a genuine local invariant separating the `t=0`
obstruction (`h,l`) from the `t=infinity` obstruction (`e`).

The cached LMFDB records also show that at the unique prime of norm 49,

    a_q(e)=-14,
    a_q(h)=a_q(l)=0.

All three values vanish modulo 7, so the semisimplified residual trace at the
prime above 7 cannot see the distinction.

## Recovered CM quadratic characters

The script

    scripts/identify_cm_quadratic_character.py

reconstructs the CM quadratic character from the vanishing pattern of Hecke
eigenvalues at split rational primes.  On the first 250 usable primes it finds
zero disagreements for the following square classes:

    e   : d = -3,
    h,l : d = w-3,

where `w^2-w-1=0` in `F=Q(sqrt(5))`.

Thus the candidate CM extensions are

    K_e   = F(sqrt(-3)),
    K_h=K_l = F(sqrt(w-3)).

At the unique prime `q|7` of `F`:

- `-3` is a square in `F_49`, so `q` splits in `K_e/F`;
- `Norm_F/Q(w-3)=5`, a nonsquare modulo 7, so `q` is inert in
  `K_h/F=K_l/F`.

This gives a sharper local prediction:

- the CM representation attached to `e` is ordinary/split at `q`;
- the CM representations attached to `h,l` are supersingular/nonsplit at `q`.

## Important correction

The `a`-number of the full genus-2 Jacobian is not automatically an invariant
of a single two-dimensional GL(2)-constituent.  Therefore one must not identify
`a=2` directly with form `e` or `a=1` directly with forms `h,l` without passing
through the relevant `O_F/7`-linear finite-flat group scheme.

What is safe is the coarser ordinary-versus-supersingular comparison.  The
`t=infinity` normalized Frey Jacobian has `p`-rank zero, whereas the CM field of
`e` splits at `q`, predicting an ordinary local CM representation.  This is a
strong candidate for a direct local elimination of `e`, once the precise
finite-flat comparison theorem is written down.

The `t=0` branch and `h,l` are both supersingular at `q`, so they require the
finer `BT_1`/Dieudonne or extension-class calculation.

## Updated next step

1. formalize the local CM theorem: splitting of `q` in the CM extension gives
   an ordinary finite-flat mod-7 representation, while inertness gives the
   supersingular/niveau-two type;
2. compare that theorem with the `p`-rank-zero `t=infinity` Frey reduction and
   eliminate `e` if the `O_F/7`-linear constituent comparison is valid;
3. for `h,l`, compute the finer `BT_1` type or the first nontrivial deformation
   class inside the `t=0` disk;
4. keep the full genus-2 `a`-number only as supporting geometric evidence, not
   as a standalone constituent-level proof.