\\ Correct local PARI/GP certificate: enumerate Rosati-self-adjoint RM matrices.
\\ Valid constraints over the local field F_p (residue field F_49):
\\   T^2-T-I=0 and T^t=T in the node-loop basis where Q_mon is scalar.

p=7;
Fp(a)=Mod(a,p);
Kpol=z^2-z-1;
K(a,b)=Mod(Fp(a)+Fp(b)*z,Kpol);
I2=matid(2)*Fp(1);
Z2=matid(2)*Fp(0);

digits3(n)=
{
  my(a,b,c,m=n);
  a=m%p;m=(m-a)/p;
  b=m%p;m=(m-b)/p;
  c=m%p;
  return([a,b,c]);
};

digits4(n)=
{
  my(a,b,c,d,m=n);
  a=m%p;m=(m-a)/p;
  b=m%p;m=(m-b)/p;
  c=m%p;m=(m-c)/p;
  d=m%p;
  return([a,b,c,d]);
};

left_eigenvector(T,lam)=
{
  my(v,u,w,L1,L2);
  for(n=1,p^4-1,
    v=digits4(n);
    u=K(v[1],v[2]);
    w=K(v[3],v[4]);
    L1=u*T[1,1]+w*T[2,1];
    L2=u*T[1,2]+w*T[2,2];
    if(L1==lam*u&&L2==lam*w,return([u,w]));
  );
  error("no left eigenvector");
};

main()=
{
  my(q1,q2,split,roots,rosati,v,T,bad,lam,ev,proj,is_split,coeff0,is_unit_line);
  q1=K(5,4);q2=K(5,3);
  split=K(0,0);
  roots=[K(0,1),K(1,6)];

  rosati=List();
  for(n=0,p^3-1,
    v=digits3(n);
    T=[Fp(v[1]),Fp(v[2]);Fp(v[2]),Fp(v[3])];
    if(T*T-T-I2==Z2,listput(rosati,T));
  );
  print("ROSATI_COUNT=",#rosati);

  bad=List();
  for(i=1,#rosati,
    T=rosati[i];
    print("T",i,"=",lift(T));
    for(j=1,2,
      lam=roots[j];
      ev=left_eigenvector(T,lam);
      proj=ev[1]*q1+ev[2]*q2;
      is_split=(proj==split);
      coeff0=lift(polcoeff(lift(proj),0))%p;
      is_unit_line=(coeff0==0&&proj!=0);
      print("  L",j," EV=",lift(ev)," PROJ=",lift(proj)," SPLIT=",is_split," UNIT_LINE=",is_unit_line);
      if(is_split||is_unit_line,listput(bad,[lift(T),j,lift(ev),lift(proj),is_split,is_unit_line]));
    );
  );
  print("BAD_COUNT=",#bad);
  for(i=1,#bad,print("BAD",i,"=",bad[i]));
  print("CERTIFICATE_DONE=1");
};

main();
quit;