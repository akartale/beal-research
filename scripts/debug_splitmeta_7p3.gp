TracePowerPoly(d,N)=
{my(S0=2,S1='x,S2);
 if(d==0,return(S0));
 if(d==1,return(S1));
 for(k=2,d,S2='x*S1-N*S0;S0=S1;S1=S2);
 S1}
SplitMeta_7p3(p)=
{my(K,F,PK,PF,fK,fF,d,N);
 K=nfinit(y^3+y^2-2*y-1);
 F=nfinit(polcyclo(21,'z));
 PK=idealprimedec(K,p)[1]; PF=idealprimedec(F,p)[1];
 fK=PK[4]; fF=PF[4]; d=fF/fK; N=p^fK;
 [fK,fF,d,N,TracePowerPoly(d,N)]}
forprime(p=11,43,if(p!=3&&p!=7,print(p," ",SplitMeta_7p3(p))));
quit;