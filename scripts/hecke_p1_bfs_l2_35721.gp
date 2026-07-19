default(parisize,"512M");
default(parisizemax,"3G");
out=fileopen("/workspace/research/beal/data/hecke_p1_bfs_l2_35721.txt","w");
read("/workspace/research/beal/scripts/quaternion_7p3_eichler_lib_hilbert.gp");
runbfs()={
  my(O,mt,T,S,elts,pts,P,ng,perms,invs,c,M,v,w,j,alpha,ca,Ma,ker=0,
     seen,parent,edge,queue,head=1,tail=1,u,nxt,words,cur,ww,maxlen=0);
  O=alglatinter(beala,alglatinter(beala,bealo,bealthreepath[2]),bealsevenpath[2]);
  mt=bealmultable(O); T=algtableinit(mt,2); S=algsplit(T,qa);
  elts=Set(concat(vector(#S[1],i,concat(Vec(S[1][i])))));
  pts=concat(vector(#elts,i,[1,elts[i]]),[[0,1]]);
  read("/workspace/research/beal/data/fdom_level35721_tuned.txt");
  P=PRESENTATION; ng=#P[1]; perms=vector(ng); invs=vector(ng);
  for(g=1,ng,
    alglatcontains(beala,O,P[1][g],&c);
    M=matrix(2,2); for(i=1,12,M+=Mod(c[i],2)*S[1][i]);
    v=vector(#pts);
    for(k=1,#pts,
      w=pts[k]*M; if(w[1]!=0,w=w/w[1],w=w/w[2]);
      j=0; for(h=1,#pts,if(w==pts[h],j=h;break)); v[k]=j
    );
    perms[g]=v; invs[g]=vector(#pts); for(k=1,#pts,invs[g][v[k]]=k)
  );
  alpha=[84375348026710,56753615930793,42172478281059,32573379187888,15907250900642,27509664693825,51054269144031,49197166096933,71208765229897,46624317430880,72803325709437,-85201653337709]~;
  alglatcontains(beala,O,alpha,&ca); Ma=matrix(2,2); for(i=1,12,Ma+=Mod(ca[i],2)*S[1][i]);
  for(k=1,#pts,if(pts[k]*Ma==[0,0],ker=k));
  seen=vector(#pts); parent=vector(#pts); edge=vector(#pts); queue=vector(#pts);
  seen[ker]=1; queue[1]=ker;
  while(head<=tail,
    u=queue[head]; head++;
    for(g=1,ng,
      nxt=perms[g][u];
      if(!seen[nxt],tail++;queue[tail]=nxt;seen[nxt]=1;parent[nxt]=u;edge[nxt]=g)
    )
  );
  words=vector(#pts);
  for(k=1,#pts,
    ww=List();cur=k;
    while(cur!=ker,listput(ww,-edge[cur]);cur=parent[cur]);
    words[k]=Vec(ww); maxlen=max(maxlen,#words[k])
  );
  filewrite(out,Str("KERNEL_INDEX=",ker));
  filewrite(out,Str("ORBIT_SIZE=",vecsum(seen)));
  filewrite(out,Str("MAX_INVERSE_WORD_LENGTH=",maxlen));
  filewrite(out,Str("WORDS_POINT_TO_KERNEL=",words));
  filewrite(out,Str("POINTS=",pts));
  1
};
iferr(runbfs(),err,filewrite(out,Str("ERROR=",err)));
fileclose(out);quit;