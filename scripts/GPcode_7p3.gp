read("research/beal/upstream/GFE-5p3/Codes/GPcode.gp");

\\ Override fixed-(5,3) routines for the exponent-switched signature (7,p,3).
Degenerate0_7p3(p)=
{local(K,f,t,ans,A);
 t=lift(znprimroot(p));
 K=nfinit(polcyclo(21));
 f=idealprimedec(K,p)[1][4];
 A=algdep(Jacobi2(1/3,-1/3,1/7,-1/7,t,p,f),3);
 ans=[A/content(A)];
 for(i=2,7,
  A=algdep(Jacobi2(1/3,-1/3,1/7,-1/7,t^i,p,f),3);
  ans=concat(ans,A/content(A)));
 Set(ans)}

Degenerateoo_7p3(p)=
{local(K,f,t,ans,A);
 t=lift(znprimroot(p));
 K=nfinit(polcyclo(21));
 f=idealprimedec(K,p)[1][4];
 A=algdep(Jacobi3(1/3,-1/3,1/7,-1/7,t,p,f),3);
 ans=[A/content(A)];
 for(i=2,3,
  A=algdep(Jacobi3(1/3,-1/3,1/7,-1/7,t^i,p,f),3);
  ans=concat(ans,A/content(A)));
 Set(ans)}

Candidates_7p3(p)=
{my(ans,K,f);
 K=nfinit(x^3+x^2-2*x-1);
 f=idealprimedec(K,p)[1][4];
 ans=List();
 parfor(i=2,p-1,algdep(p^f*hgm(i,[1/7,-1/7],[1/3,-1/3],p,f),3),R,listput(~ans,R));
 for(i=1,#ans,ans[i]=ans[i]/content(ans[i]));
 Vec(ans)}

print("C11=",Candidates_7p3(11));
print("D0_11=",Degenerate0_7p3(11));
print("Doo_11=",Degenerateoo_7p3(11));