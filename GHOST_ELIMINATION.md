# Exact elimination of ghost specializations

For the plus Frey family use

    t = -B^5/A^3.

A primitive solution has `gcd(A,B)=1`.

## `t=-1/8`

Then

    A^3 = 8B^5.

Pairwise coprimality forces `B=1` and `A=2`. Hence

    A^3+B^5=9,

which is not a seventh power. Therefore no primitive Beal solution has `t=-1/8`.

## `t=9/8`

For positive `A,B`, the quantity `-B^5/A^3` is negative, so `t=9/8` is impossible. Even allowing signs gives

    8B^5 = -9A^3.

At the prime 3,

    5 v_3(B) = 2 + 3 v_3(A).

Coprimality forces one of `v_3(A),v_3(B)` to vanish, and either choice is impossible. Hence no primitive integral specialization has `t=9/8`.

## Consequence

Any Hilbert newform arising from these ghost specializations cannot be the characteristic-zero Frey object of a genuine solution. If it survives the `p=7` Mazur sieve, the obstruction is a residual mod-7 congruence. It must be removed using local information at 7 or a refined residual-image argument, not by more auxiliary-prime point counting.