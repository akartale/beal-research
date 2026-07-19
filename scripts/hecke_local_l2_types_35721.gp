default(parisize,"256M");
default(parisizemax,"3G");
out=fileopen("/workspace/research/beal/data/hecke_local_l2_types_35721.txt","w");
read("/workspace/research/beal/scripts/quaternion_7p3_eichler_lib_hilbert.gp");
runlocal()={
  my(O,mt,T,S);
  O=alglatinter(beala,alglatinter(beala,bealo,bealthreepath[2]),bealsevenpath[2]);
  mt=bealmultable(O); T=algtableinit(mt,2); S=algsplit(T,qa);
  filewrite(out,Str("IMAGE_COUNT=",#S[1]));
  filewrite(out,Str("IMAGE1=",S[1][1]));
  filewrite(out,Str("ENTRY_TYPE=",type(S[1][1][1,1])));
  filewrite(out,Str("ENTRY=",S[1][1][1,1]));
  filewrite(out,Str("INVERSE_MAP=",S[2]));
  1
};
iferr(runlocal(),err,filewrite(out,Str("ERROR=",err)));
fileclose(out); quit;