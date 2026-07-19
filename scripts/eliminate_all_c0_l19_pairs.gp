keypair(r1,r2)={Str(r1+r2,"|",r1*r2)};
run()={
 my(T,a,g,zz,mone,P,actualL,r,actual,surv,u,v,chi1,chi2,tr1,tr2,i);
 T=ffinit(7,12,'t); a=ffgen(T,'a); g=ffprimroot(a);
 zz=g^((7^12-1)/180); mone=a^0*6;
 P=[[0,1],[0,4],[1,4],[1,6],[2,3],[3,1],[3,4],[3,5],[3,6],[4,1],[4,6],[5,2],[5,3],[5,5],[6,3]];
 actualL=List();
 for(i=1,#P,
  r=polrootsmod(x^2-(a^0*P[i][1])*x+(a^0*P[i][2]),a);
  if(#r==1,listput(actualL,keypair(r[1],r[1])));
  if(#r==2,listput(actualL,keypair(r[1],r[2])));
 );
 actual=Set(Vec(actualL)); surv=List();
 for(u=0,179,
  for(v=0,1,
   chi1=zz^((141*u)%180)*mone^v; chi2=chi1;
   tr1=chi1+(a^0*(19%7))/chi1;
   tr2=chi2+(a^0*(19%7))/chi2;
   if(setsearch(actual,keypair(tr1,tr2)),listput(surv,[u,v,tr1]));
  );
 );
 print("actual_trace_pairs=",#actual);
 print("survivors_at_l19_pairwise=",#surv);
 print("survivors=",Vec(surv));
};
run();