default(parisize,"512M");
default(parisizemax,"3G");
out=fileopen("/workspace/research/beal/data/hecke_coset_reps_l2_35721.txt","w");
read("/workspace/research/beal/scripts/quaternion_7p3_eichler_lib_hilbert.gp");
runreps()={
  my(O,mt,T,S,elts,pts,P,alpha,inds,reps=vector(9),kernels=vector(9),norms=vector(9),
     inside=vector(9),beta,c,M,v,kk);
  O=alglatinter(beala,alglatinter(beala,bealo,bealthreepath[2]),bealsevenpath[2]);
  mt=bealmultable(O); T=algtableinit(mt,2); S=algsplit(T,qa);
  elts=Set(concat(vector(#S[1],i,concat(Vec(S[1][i])))));
  pts=concat(vector(#elts,i,[1,elts[i]]),[[0,1]]);
  read("/workspace/research/beal/data/fdom_level35721_tuned.txt"); P=PRESENTATION;
  alpha=[84375348026710,56753615930793,42172478281059,32573379187888,15907250900642,27509664693825,51054269144031,49197166096933,71208765229897,46624317430880,72803325709437,-85201653337709]~;
  inds=[21,24,0,3,11,6,1,5,12];
  for(k=1,9,
    beta=if(inds[k]==0,alpha,algmul(beala,alginv(beala,P[1][inds[k]]),alpha));
    reps[k]=beta; norms[k]=algnorm(beala,beta); inside[k]=alglatcontains(beala,O,beta,&c);
    M=matrix(2,2);for(i=1,12,M+=Mod(c[i],2)*S[1][i]);
    kk=0;for(j=1,#pts,v=pts[j]*M;if(v==[0,0],kk=j));kernels[k]=kk
  );
  filewrite(out,Str("GENERATOR_INDICES=",inds));
  filewrite(out,Str("NORMS=",norms));
  filewrite(out,Str("ALL_IN_ORDER=",vecprod(inside)));
  filewrite(out,Str("KERNEL_INDICES=",kernels));
  filewrite(out,Str("DISTINCT_KERNELS=",#Set(kernels)));
  filewrite(out,Str("REPRESENTATIVES=",reps));
  1
};
iferr(runreps(),err,filewrite(out,Str("ERROR=",err)));
fileclose(out);quit;