# Ray-class enumeration for the reducible mod-7 branch

Let K=Q(sqrt(5)), with O_K=Z[(1+sqrt(5))/2]. The rational primes 3 and 7 are inert in K, with norms 9 and 49, while 5 is ramified, with prime norm 5.

A broad modulus was scanned:

    m = p3^a * p5^b * p7^c * infinity_1 * infinity_2,
    0 <= a <= 3, 0 <= b <= 3, 0 <= c <= 2.

For each ray class group Cl_m, the number of characters with values in F_7^* was computed as

    #Hom(Cl_m, F_7^*) = product_i gcd(d_i,6),

where [d_i] is the cyclic decomposition of Cl_m.

At the maximal scanned modulus (a,b,c)=(3,3,2):

    Cl_m cyclic structure = [2520,12,2]
    number of F_7^*-valued characters = 72.

At the same 3- and 5-part but with no conductor at the prime above 7:

    (a,b,c)=(3,3,0)
    Cl_m cyclic structure = [180,2]
    number of F_7^*-valued characters = 12.

Thus the reducible branch is already finite and small: at most 72 broad ray-class characters in this conductor box, and only 12 if one diagonal character can be chosen unramified at 7 after using the local finite-flat/Serre-weight condition and exchanging chi with epsilon_7 chi^{-1}.

Important: the reduction from 72 to 12 still requires a rigorous local analysis of the Frey representation at the prime above 7. It is not yet assumed as proved.

Script: research/beal/scripts/rayclass_357.gp