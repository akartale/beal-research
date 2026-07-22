\\ Full normalized q-Frobenius characteristic polynomial modulo 7 for the
\\ infinity-disk Frey family. PARI returns a 5-dimensional even-degree space
\\ with one extraneous line. For A=M^2/7 mod 7 that line has eigenvalue 0,
\\ so charpoly(A)=X * charpoly(A_genus2).

x='x;
p=7;
n=2;

target=Mod(1,7)*(x+1)^4;
survivors=List();

showcase(a,v)={
  Q=45*v^2*x^6-108*7^a*v^2*x^5+90*v*x^3+9;
  M=liftall(hyperellpadicfrobenius(Q,p,n));
  S=M*M;
  for(i=1,matsize(S)[1],for(j=1,matsize(S)[2],if(S[i,j]%7,error("M^2 not divisible by 7"))));
  A=matrix(matsize(S)[1],matsize(S)[2],i,j,Mod(S[i,j]/7,7));
  cp=liftpol(charpoly(A));
  if(polcoeff(cp,0)!=0,error("extraneous zero factor missing"));
  qp=cp/x;
  print(a," ",v," ",qp);
  if(qp==target,listput(survivors,[a,v]));
};

print("target_orbit_e=",target);
print("a v normalized_qcharpoly_mod7");
for(a=1,2,for(v=1,48,if(v%7,showcase(a,v))));
print("survivors=",Vec(survivors));
if(#survivors,error("unexpected orbit-e matches"));
quit;