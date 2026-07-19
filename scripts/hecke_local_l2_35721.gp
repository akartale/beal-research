default(parisize,"256M");
default(parisizemax,"3G");
out=fileopen("/workspace/research/beal/data/hecke_local_l2_35721.txt","w");
read("/workspace/research/beal/scripts/quaternion_7p3_eichler_lib_hilbert.gp");
runlocal()={
  my(O,P2,mt,T,S);
  O=alglatinter(beala,alglatinter(beala,bealo,bealthreepath[2]),bealsevenpath[2]);
  P2=idealprimedec(bealk,2);
  filewrite(out,Str("PRIMES_ABOVE_2=",#P2));
  filewrite(out,Str("E=",P2[1].e));
  filewrite(out,Str("F=",P2[1].f));
  filewrite(out,Str("NORM=",idealnorm(bealk,P2[1])));
  filewrite(out,Str("HECKE_COSET_COUNT=",idealnorm(bealk,P2[1])+1));
  filewrite(out,Str("ORDER_INDEX_AT_2=",valuation(alglatindex(beala,O,bealo),2)));
  mt=bealmultable(O); filewrite(out,"MULTABLE_OK=1");
  T=algtableinit(mt,2); filewrite(out,Str("ALG_DIM=",algdim(T)));
  filewrite(out,Str("CENTER_DIM=",matsize(algcenter(T))[2]));
  S=algsplit(T,qa); filewrite(out,"ALGSPLIT_OK=1");
  filewrite(out,Str("SPLIT_MAP_SIZE=",matsize(S[2])));
  filewrite(out,Str("MATRIX_DEGREE=",matsize(S[1][1])[1]));
  1
};
iferr(runlocal(),err,filewrite(out,Str("ERROR=",err)));
fileclose(out);
quit;