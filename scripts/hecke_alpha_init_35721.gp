default(parisize,"256M"); default(parisizemax,"3G"); default(realprecision,100);
out=fileopen("/workspace/research/beal/data/hecke_alpha_init_35721.txt","w");
read("/workspace/research/beal/scripts/quaternion_7p3_eichler_lib_hilbert.gp");
runinit()={
 my(O,X);
 O=alglatinter(beala,alglatinter(beala,bealo,bealthreepath[2]),bealsevenpath[2]);
 X=afuchinit(beala,O[1],0,0);
 filewrite(out,Str("X12=",X[12]));
 filewrite(out,Str("X_LEN=",#X));
 1
};
iferr(runinit(),err,filewrite(out,Str("ERROR=",err)));
fileclose(out);quit;