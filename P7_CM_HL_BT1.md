# CM BT_1 type of the surviving forms h and l

## CM field

The Hecke-zero reconstruction gives

    K = F(sqrt(w-3)),
    F=Q(w),  w^2-w-1=0.

Writing `z^2=w-3`, one obtains

    w=z^2+3,
    z^4+5z^2+5=0.

The reproducible PARI/GP calculation

    scripts/cm_hl_field_local7.gp

returns

    Disc(K)=2000,
    Gal(K/Q)=C4,
    Cl(K)=1.

At 7 it gives one prime with

    e=1,
    f=4.

Equivalently, the polynomial `x^4+5x^2+5` is irreducible modulo 7.  Thus 7 is
unramified and completely inert in the cyclic quartic CM field `K`.

## CM type and circular word

Let `sigma` generate `Gal(K/Q)=C4`; complex conjugation is `sigma^2`.  A CM type
chooses one embedding from each conjugate pair

    {1,sigma^2}, {sigma,sigma^3}.

Every primitive CM type is equivalent, up to Galois translation and complex
conjugation, to

    Phi={1,sigma}.

Because the decomposition group at 7 is the full cyclic group `C4`, Frobenius
runs through the embeddings in the order

    1, sigma, sigma^2, sigma^3.

Marking membership in `Phi` by `F` and non-membership by `V` gives the circular
word

    [F F V V].

This is the indecomposable self-dual genus-2 word `I_{2,1}`.  Hence the good
reduction of the CM abelian surface has

    p-rank = 0,
    a-number = 1.

This agrees with the dimension-2 classification of CM `BT_1` group schemes for
an unramified prime of decomposition type `(alpha,beta)=(1,1)`.

## Comparison with the Frey t=0 disk

For the normalized Frey reduction in the branch `7|B`, the direct
Cartier--Manin computation gives

    M_0(u) = [[0,-u^4],[0,0]],
    rank(M_0)=1,
    M_0^2=0,
    p-rank=0,
    a-number=1.

Thus both sides have the same coarse `BT_1` isomorphism type `I_{2,1}`.
Consequently neither p-rank, a-number, nor the abstract geometric `BT_1` type
eliminates forms `h,l`.

## Consequence

The remaining local invariant must retain the `O_F/7 = F_49` action and/or the
first-order lift over `O_{F_q}/7^2`.  The abstract special-fibre group scheme
forgets precisely the information now needed.

The next targets are therefore:

1. the `F_49`-linear Dieudonne module with its labelled embedding action;
2. the first deformation term in the normalized t=0 model,

       Y^2 = -108X^5 + 9u^2 + 7^b(90uX^3) + 7^(2b)(45X^6),

   especially the case `b=1` modulo 49;
3. the Serre--Tate/display extension class of the `I_{2,1}` special fibre;
4. comparison of that class with the two conjugate CM lifts corresponding to
   forms `h` and `l`.

At this point the local problem has been reduced from all Hilbert forms to a
comparison of three lifts of the same `I_{2,1}` special fibre: the Frey lift and
the two CM-conjugate lifts.