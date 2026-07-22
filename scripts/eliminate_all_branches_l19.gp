keypair(r1,r2)={Str(r1+r2,"|",r1*r2)};
run()={
 my(T,a,g,zz,mone,P,actualL,r,actual,surv,u,v,chi1,chi2,tr1,tr2,qtr1,qtr2,i,
    c0roots,cooroots,ok_generic,ok0,okoo,ok1,branch);
 T=ffinit(7,12,'t); a=ffgen(T,'a); g=ffprimroot(a);
 zz=g^((7^12-1)/180); mone=a^0*6;
 /* Exact generic paired RM trace data at l=19. */
 P=[[0,1],[0,4],[1,4],[1,6],[2,3],[3,1],[3,4],[3,5],[3,6],[4,1],[4,6],[5,2],[5,3],[5,5],[6,3]];
 actualL=List();
 for(i=1,#P,
  r=polrootsmod(x^2-(a^0*P[i][1])*x+(a^0*P[i][2]),a);
  if(#r==1,listput(actualL,keypair(r[1],r[1])));
  if(#r==2,listput(actualL,keypair(r[1],r[2])));
 );
 actual=Set(Vec(actualL));
 /* Exact degenerate trace-power data from Data.txt at l=19. */
 c0roots=Set(polrootsmod(x+(a^0*38),a));
 cooroots=Set(concat(polrootsmod(x+(a^0*22),a),polrootsmod(x^2-(a^0*22)*x-(a^0*599),a)));
 surv=List();
 for(u=0,179,
  for(v=0,1,
   chi1=zz^((141*u)%180)*mone^v; chi2=chi1;
   tr1=chi1+(a^0*(19%7))/chi1;
   tr2=chi2+(a^0*(19%7))/chi2;
   qtr1=tr1^2-a^0*(2*(19%7));
   qtr2=tr2^2-a^0*(2*(19%7));
   ok_generic=setsearch(actual,keypair(tr1,tr2));
   ok0=setsearch(c0roots,qtr1)&&setsearch(c0roots,qtr2);
   okoo=setsearch(cooroots,qtr1)&&setsearch(cooroots,qtr2);
   /* Case t=1: Steinberg congruence a_l = +/-(l+1). */
   ok1=((tr1==a^0*((19+1)%7))||(tr1==-a^0*((19+1)%7)))&&
       ((tr2==a^0*((19+1)%7))||(tr2==-a^0*((19+1)%7)));
   if(ok_generic||ok0||okoo||ok1,
      branch=[];
      if(ok_generic,branch=concat(branch,["generic"]));
      if(ok0,branch=concat(branch,["t0"]));
      if(okoo,branch=concat(branch,["too"]));
      if(ok1,branch=concat(branch,["t1"]));
      listput(surv,[u,v,tr1,qtr1,branch]));
  );
 );
 print("generic_pairs=",#actual);
 print("C0_roots=",c0roots);
 print("Coo_roots=",cooroots);
 print("all_branch_survivors=",#surv);
 print(Vec(surv));
};
run();