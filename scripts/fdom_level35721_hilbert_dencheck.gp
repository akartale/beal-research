default(parisize,"256M");
default(parisizemax,"3G");
out=fileopen("/workspace/research/beal/data/fdom_level35721_tuned.txt","w");
filewrite(out,"START=1");
read("/workspace/research/beal/scripts/quaternion_7p3_eichler_lib_hilbert.gp");
levellattice=alglatinter(beala,alglatinter(beala,bealo,bealthreepath[2]),bealsevenpath[2]);
print("DEN=",levellattice[2]);
quit;
