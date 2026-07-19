default(parisizemax,"8G");
y='y;x='x;a='a;
K=nfinit(y^3+y^2-2*y-1);
A=alginit(K,[2,[[],[]],[1/2,1/2,0]],x);
N=12;O0=alglathnf(A,matid(N));

PreimageLattice(M,p)=
{ my(n,Kmod,G);
  n=matsize(M)[2];Kmod=lift(matkermod(lift(M),p));
  G=concat(Kmod,p*matid(n));mathnf(G)
}

OrderMultable(O)=
{ my(E,MT,z,c);
  E=vector(N,i,alglatelement(A,O,vector(N,j,j==i)~));
  MT=vector(N,i,matrix(N,N));
  for(i=1,N,for(j=1,N,
    z=algmul(A,E[i],E[j]);
    if(!alglatcontains(A,O,z,&c),error("order is not closed"));
    for(r=1,N,MT[i][r,j]=c[r])
  ));
  MT
}

SublatticeIn(O,H)=
{ my(M);
  M=matrix(N,N,r,c,alglatelement(A,O,H[,c])[r]);
  alglathnf(A,M)
}

TwoNeighbors(O,p)=
{ my(MT,T,Q,S,proj,n,toM,C1,C2,H1,H2,I1,I2);
  MT=OrderMultable(O);
  if(p==3,
    T=algtableinit(MT,3);proj=matid(N);n=3,
    T=algtableinit(MT,7);Q=algquotient(T,algradical(T),1);
    T=Q[1];proj=Q[2];n=1
  );
  S=algsplit(T,a);
  toM=matinvmod(S[2],p)*proj;
  C1=toM[2*n+1..4*n,];
  C2=toM[1..2*n,];
  H1=PreimageLattice(C1,p);H2=PreimageLattice(C2,p);
  I1=SublatticeIn(O,H1);I2=SublatticeIn(O,H2);
  [alglatlefttransporter(A,I1,I1),alglatlefttransporter(A,I2,I2)]
}

DistanceIndex(O)=alglatindex(A,alglatinter(A,O0,O),O0);

BuildPath(p,q,eMax)=
{ my(path=vector(eMax),cur=O0,C,target,chosen);
  for(e=1,eMax,
    C=TwoNeighbors(cur,p);target=q^e;chosen=0;
    for(k=1,#C,if(DistanceIndex(C[k])==target,chosen=C[k];break));
    if(type(chosen)=="t_INT",error(Str("no forward neighbor at p=",p," step=",e)));
    path[e]=chosen;cur=chosen;
  );
  path
}

P3path=BuildPath(3,27,3);
P7path=BuildPath(7,7,3);

EmitLevel(u,v,out)=
{ my(ord,idx,expected,closed);
  ord=alglatinter(A,alglatinter(A,O0,P3path[u]),P7path[v]);
  idx=alglatindex(A,ord,O0);
  expected=27^u*7^v;
  closed=alglatsubset(A,alglatmul(A,ord,ord),ord);
  filewrite(out,Str("LEVEL_",u,"_",v,"_INDEX=",idx));
  filewrite(out,Str("LEVEL_",u,"_",v,"_EXPECTED=",expected));
  filewrite(out,Str("LEVEL_",u,"_",v,"_CLOSED=",closed));
  filewrite(out,Str("LEVEL_",u,"_",v,"_LATTICE=",ord));
}

out=fileopen("research/beal/data/eichler_paths_7p3.txt","w");
for(u=1,3,filewrite(out,Str("P3_STEP_",u,"_INDEX=",DistanceIndex(P3path[u]))));
for(v=1,3,filewrite(out,Str("P7_STEP_",v,"_INDEX=",DistanceIndex(P7path[v]))));
EmitLevel(2,2,out);
EmitLevel(2,3,out);
EmitLevel(3,2,out);
EmitLevel(3,3,out);
fileclose(out);quit;