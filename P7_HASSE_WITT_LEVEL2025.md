# Hasse--Witt elimination at p=7 for level 2025

Consider the genus-2 hyperelliptic model

    C_t : y^2 = 5x^6 - 12x^5 + 10 t x^3 + t^2.

For p=7, the Hasse--Witt matrix is obtained from the coefficients of
`f(x)^3`. With the standard genus-2 indexing it is

    HW = [[c_6,c_5],[c_13,c_12]].

The open symbolic calculation gives modulo 7

    c_6  = 0,
    c_5  = -t^4,
    c_13 = t,
    c_12 = 0,

and therefore

    det(HW) = t^5.

Reproduction:

    research/beal/scripts/hasse_witt_p7.py

Hence for every finite nonzero parameter t modulo 7, the Jacobian is ordinary.
It is nonordinary only at t=0.

For a Frey specialization

    t = -B^5/A^3,

if 7 does not divide A then

    nonordinary at p7  <=>  7 divides B.

All three level-2025 survivors have p7-Hecke trace divisible by 7:

    a_p7(e)=-14,
    a_p7(h)=0,
    a_p7(l)=0.

Thus their residual local representations are nonordinary. Consequently:

    if 7 does not divide A*B,
    all three level-2025 survivors are eliminated.

Combined with the source local-type results, a level-2025 obstruction can now
remain only in the narrow arithmetic locus

    gcd(C,15)=1,
    3|A,
    and (7|A or 7|B).

The branch 7|B is the finite t=0 reduction. The branch 7|A corresponds to
t=infinity and requires a separate stable-model/local-type analysis because
the displayed affine model degenerates after the naive u=1/t substitution.