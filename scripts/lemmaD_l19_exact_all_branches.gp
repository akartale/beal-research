\\ Exact Lemma-D ray-character sieve at l=19.
\\ Branches follow the upstream GFE-5p3 elimination code:
\\ generic: compare a_l directly with Candidates(19);
\\ t=0,infinity: compare a_l^2-2*l with Degenerate0/oo(19);
\\ t=1: compare a_l with +/-(l+1).

x='x;

root_of_any(z, polys)={
  my(i);
  for(i=1,#polys,if(subst(polys[i],x,z)==0,return(1)));
  return(0);
};

run()={
  my(T,a,g,zz,mone,generic,tzero,tinf,sgen,s0,s1,sinf,sall,u,v,chi,tr,qtr);
  T=ffinit(7,12,'t); a=ffgen(T,'a); g=ffprimroot(a);
  zz=g^((7^12-1)/180); mone=a^0*6;

  generic=[
    x^2+7*x+1,x^2+4*x-16,x^2+11*x+29,x^2+6*x+4,
    x^2-6*x-11,x^2+7*x+11,x^2+9*x+9,x^2-4*x-1,
    x^2-2*x-4,x^2-x-1,x^2+2*x-19,x^2+9*x+19,
    x^2-5*x-25,x^2+4*x-1,x^2+3*x+1,x-5,x^2+2*x-19
  ];
  tzero=[x+38];
  tinf=[x+22,x^2-22*x-599];

  sgen=List(); s0=List(); s1=List(); sinf=List(); sall=List();
  for(u=0,179,
    for(v=0,1,
      \\ Both primes above 19 have ray coordinates [141,1].
      chi=zz^((141*u)%180)*mone^v;
      tr=chi+(a^0*(19%7))/chi;
      qtr=tr^2-a^0*((2*19)%7);

      if(root_of_any(tr,generic),listput(sgen,[u,v,tr]));
      if(root_of_any(qtr,tzero),listput(s0,[u,v,tr,qtr]));
      if(tr==a^0*((19+1)%7)||tr==a^0*((-(19+1))%7),listput(s1,[u,v,tr]));
      if(root_of_any(qtr,tinf),listput(sinf,[u,v,tr,qtr]));
      if(root_of_any(tr,generic)||root_of_any(qtr,tzero)||
         tr==a^0*((19+1)%7)||tr==a^0*((-(19+1))%7)||
         root_of_any(qtr,tinf),listput(sall,[u,v,tr]));
    );
  );

  print("generic_survivors=",#sgen); print(Vec(sgen));
  print("t0_survivors=",#s0); print(Vec(s0));
  print("t1_survivors=",#s1); print(Vec(s1));
  print("tinf_survivors=",#sinf); print(Vec(sinf));
  print("union_survivors=",#sall); print(Vec(sall));
};

run();