\\ SUPERSEDED DIAGNOSTIC ONLY.
\\ The condition S*T*S=I-T below incorrectly treats F_7-conjugation as local
\\ Galois, although the local base residue field is F_49.  Do not use this
\\ six-matrix search in a proof.  The correct certificate is
\\ p7_t1_rm_rosati_certificate.gp, using T^2-T-I=0 and Rosati symmetry T^t=T.

p=7;
Fp(a)=Mod(a,p);
Kpol=z^2-z-1;
K(a,b)=Mod(Fp(a)+Fp(b)*z,Kpol);
I2=matid(2)*Fp(1);
Z2=matid(2)*Fp(0);
S=[Fp(0),Fp(1);Fp(1),Fp(0)];

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
  my(f,fm,nodeg,h,q1,q2,split,unitw,roots,admissible,v,T,bad,lam,ev,proj,is_split,coeff0,is_unit_line);

  f=5*x^6-12*x^5+10*x^3+1;
  fm=Mod(1,p)*f;
  nodeg=gcd(fm,deriv(fm));
  nodeg=nodeg/pollead(nodeg);
  h=Mod(1,p)*(x^2+6*x+6);
  print("SPECIAL_FACTOR=",factor(fm));
  if(nodeg!=h,error("wrong quadratic node factor: ",nodeg));
  print("NODE_POLY_OK=1");

  q1=K(5,4);q2=K(5,3);
  split=K(0,0);unitw=K(0,1);
  roots=[K(0,1),K(1,6)];

  admissible=List();
  for(n=0,p^4-1,
    v=digits4(n);
    T=[Fp(v[1]),Fp(v[2]);Fp(v[3]),Fp(v[4])];
    if(T*T-T-I2==Z2&&S*T*S==I2-T,listput(admissible,T));
  );
  print("ADMISSIBLE_COUNT=",#admissible);
  if(#admissible!=6,error("expected six admissible matrices"));

  bad=List();
  symmetric=List();
  for(i=1,#admissible,
    T=admissible[i];
    if(T==mattranspose(T),listput(symmetric,T));
    print("T",i,"=",lift(T)," SYMMETRIC=",T==mattranspose(T));
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
  if(#bad!=2,error("expected exactly two exceptional projections"));
  print("SYMMETRIC_COUNT=",#symmetric);
  if(#symmetric!=4,error("expected exactly four Rosati-compatible matrices"));
  for(i=1,#bad,if(bad[i][1]==mattranspose(bad[i][1]),error("exceptional matrix survived Rosati symmetry")));
  print("ROSATI_FILTER_OK=1");
  print("CERTIFICATE_DONE=1");
};

main();
quit;