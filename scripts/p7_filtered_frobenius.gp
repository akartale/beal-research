\\ Compute crystalline Frobenius matrices to precision 7^2 for the explicit
\\ CM curve and the six normalized t=0 Frey lifts.

x='x;
p=7;
n=2;

Qcm=x^5-1;
print("CM_POLY=",Qcm);
Mcm=hyperellpadicfrobenius(Qcm,p,n);
print("CM_FROB=",liftall(Mcm));
print("CM_CHARPOLY=",centerlift(simplify(liftpol(charpoly(Mcm)))));

showfrey(u)={Q=-108*x^5+42*u*x^3+9*u^2; print("FREY_U=",u); print("FREY_POLY=",Q); M=hyperellpadicfrobenius(Q,p,n); print("FREY_FROB=",liftall(M)); print("FREY_CHARPOLY=",centerlift(simplify(liftpol(charpoly(M)))));};
showfrey(1);
showfrey(2);
showfrey(3);
showfrey(4);
showfrey(5);
showfrey(6);
quit;