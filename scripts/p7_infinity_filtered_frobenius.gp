\\ Compute crystalline Frobenius matrices modulo 7^2 for the normalized
\\ infinity-disk Frey family at the first nontrivial deformation a=1.
\\
\\   Y^2 = 45 v^2 X^6 - 108*7*v^2 X^5 + 90 v X^3 + 9,
\\
\\ for residue representatives v=1,...,6.  Precision n=2 is enough to
\\ inspect the lower-left Hodge block divided by 7.

x='x;
p=7;
n=2;

showinf(v)={
  Q=45*v^2*x^6-108*7*v^2*x^5+90*v*x^3+9;
  print("INF_V=",v);
  print("INF_POLY=",Q);
  M=hyperellpadicfrobenius(Q,p,n);
  print("INF_FROB=",liftall(M));
  print("INF_CHARPOLY=",centerlift(simplify(liftpol(charpoly(M)))));
};

showinf(1);
showinf(2);
showinf(3);
showinf(4);
showinf(5);
showinf(6);
quit;