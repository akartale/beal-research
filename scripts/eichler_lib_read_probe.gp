out=fileopen("/workspace/research/beal/data/eichler_lib_read_probe.txt","w");
filewrite(out,"BEFORE");
read("/workspace/research/beal/scripts/quaternion_7p3_eichler_lib.gp");
filewrite(out,Str("AFTER=",type(bealk),",",type(beala),",",type(bealo),",",type(bealthreepath)));
fileclose(out);quit;