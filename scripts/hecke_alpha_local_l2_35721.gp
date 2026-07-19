default(parisize,"512M");
default(parisizemax,"3G");
default(realprecision,100);
install(afuchfindoneelt_raw,"GD1,G,DG",,"/workspace/research/beal/vendor/fdom-upstream/libfdom-2-15-2.so");
out=fileopen("/workspace/research/beal/data/hecke_alpha_local_l2_35721.txt","w");
read("/workspace/research/beal/scripts/quaternion_7p3_eichler_lib_hilbert.gp");
runlocal()={
  my(O,X,alpha,c,mt,T,S,M,elts,pts,ker=List(),v);
  O=alglatinter(beala,alglatinter(beala,bealo,bealthreepath[2]),bealsevenpath[2]);
  X=afuchinit(beala,O[1],0,0);
  alpha=afuchfindoneelt_raw(X,2);
  if(!alglatcontains(beala,O,alpha,&c),error("alpha outside order"));
  mt=bealmultable(O); T=algtableinit(mt,2); S=algsplit(T,qa);
  M=matrix(2,2); for(i=1,12,M+=Mod(c[i],2)*S[1][i]);
  elts=Set(concat(vector(#S[1],i,concat(Vec(S[1][i])))));
  pts=concat(vector(#elts,i,[1,elts[i]]),[[0,1]]);
  for(k=1,#pts,v=pts[k]*M;if(v==[0,0],listput(ker,k)));
  filewrite(out,Str("ALPHA=",alpha));
  filewrite(out,Str("NORM=",algnorm(beala,alpha)));
  filewrite(out,Str("LOCAL_MATRIX=",M));
  filewrite(out,Str("LOCAL_DET=",matdet(M)));
  filewrite(out,Str("KERNEL_POINTS=",Vec(ker)));
  filewrite(out,Str("KERNEL_COORDS=",vector(#ker,i,pts[ker[i]])));
  1
};
iferr(runlocal(),err,filewrite(out,Str("ERROR=",err)));
fileclose(out); quit;