default(parisize,"512M");
default(parisizemax,"3G");
out=fileopen("/workspace/research/beal/data/hecke_p1_action_l2_35721.txt","w");
read("/workspace/research/beal/scripts/quaternion_7p3_eichler_lib_hilbert.gp");
runlocal()={
  my(O,mt,T,S,elts,pts,P,ng,perms,invs,c,M,v,w,j,ok=1,rel,rperm,state,a);
  O=alglatinter(beala,alglatinter(beala,bealo,bealthreepath[2]),bealsevenpath[2]);
  mt=bealmultable(O); T=algtableinit(mt,2); S=algsplit(T,qa);
  elts=Set(concat(vector(#S[1],i,concat(Vec(S[1][i])))));
  filewrite(out,Str("FIELD_ELEMENTS=",elts));
  filewrite(out,Str("FIELD_SIZE=",#elts));
  pts=concat(vector(#elts,i,[1,elts[i]]),[[0,1]]);
  filewrite(out,Str("P1_SIZE=",#pts));
  read("/workspace/research/beal/data/fdom_level35721_tuned.txt");
  P=PRESENTATION; ng=#P[1]; perms=vector(ng); invs=vector(ng);
  for(g=1,ng,
    if(!alglatcontains(beala,O,P[1][g],&c),error(Str("generator outside order: ",g)));
    M=matrix(2,2);
    for(i=1,12,M+=Mod(c[i],2)*S[1][i]);
    v=vector(#pts);
    for(k=1,#pts,
      w=pts[k]*M;
      if(w[1]!=0,w=w/w[1],w=w/w[2]);
      j=0; for(h=1,#pts,if(w==pts[h],j=h;break));
      if(j==0,error(Str("P1 image not found g=",g," k=",k)));
      v[k]=j
    );
    if(#Set(v)!=#pts,ok=0);
    perms[g]=v;
    invs[g]=vector(#pts); for(k=1,#pts,invs[g][v[k]]=k)
  );
  rel=P[2][1]; rperm=vector(#pts,k,k);
  for(k=1,#pts,
    state=k;
    for(z=1,#rel,
      a=rel[z];
      state=if(a>0,perms[a][state],invs[-a][state])
    );
    rperm[k]=state
  );
  filewrite(out,Str("GENERATORS_TESTED=",ng));
  filewrite(out,Str("ALL_ACTIONS_PERMUTATIONS=",ok));
  filewrite(out,Str("RELATION_LENGTH=",#rel));
  filewrite(out,Str("RELATION_ACTION=",rperm));
  filewrite(out,Str("RELATION_ACTION_IDENTITY=",rperm==vector(#pts,k,k)));
  filewrite(out,Str("FIRST_PERMUTATIONS=",perms[1..min(10,ng)]));
  1
};
iferr(runlocal(),err,filewrite(out,Str("ERROR=",err)));
fileclose(out); quit;