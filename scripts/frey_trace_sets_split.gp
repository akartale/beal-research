roots7(s,pd)={my(v=List(),r);for(r=0,6,if((r*r-s*r+pd)%7==0,listput(v,r)));Vec(v)};
seventh_residue_exists(n,l)={my(c);for(c=1,l-1,if((c^7-n)%l==0,return(1)));return(0)};
scanprime(l)={
 my(S=List(),A,B,n,P,cp,c1,c2,rr,r,disc);
 for(A=1,l-1,
  for(B=1,l-1,
   n=(A^3+B^5)%l;
   if(n!=0 && seventh_residue_exists(n,l),
    P=Mod(5,l)*x^6-Mod(12*A,l)*x^5-Mod(10*B^5,l)*x^3+Mod(B^10,l);
    disc=lift(poldisc(P));
    if(disc%l!=0,
      cp=hyperellcharpoly(P);
      c1=polcoef(cp,3); c2=polcoef(cp,2);
      rr=roots7((-c1)%7,(c2-2*l)%7);
      for(k=1,#rr,listput(S,rr[k]));
    );
   );
  );
 );
 print("l=",l," traces=",Set(Vec(S)));
};
scan()={forprime(l=11,83,if(kronecker(5,l)==1 && l!=5 && l!=7,scanprime(l)));};
scan();