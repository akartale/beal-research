\\ Quartic CM field for h,l: K=F(sqrt(w-3)), w^2-w-1=0.
\\ If z^2=w-3, then w=z^2+3 and z satisfies z^4+5*z^2+5=0.

x='x;
P=x^4+5*x^2+5;
print("POLY=",P);
print("DISC=",poldisc(P));
print("GALOIS=",polgalois(P));
K=bnfinit(P,1);
print("PRIME_DEC_7=",idealprimedec(K,7));
print("FACTOR_MOD_7=",factormod(P,7));
print("CLASS_GROUP=",K.clgp);
quit;