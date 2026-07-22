default(parisize,"2G");
default(parisizemax,"8G");
read("fdom.gp");
out=fileopen("/workspace/research/beal/data/fdom_level35721_loader_v16.log","w");
read("/workspace/research/beal/scripts/quaternion_7p3_eichler_lib.gp");
fileclose(out);
read("/workspace/research/beal/vendor/fdom-memory-reduced/load_memory_reduced.gp");
logpath="/workspace/research/beal/data/fdom_level35721_complete_v16.log";
runcomplete()={
  my(all,cp,xx,U,res,out,G=[]);
  all=read("/workspace/research/beal/data/fdom_level35721_reconstruct_batched_v9_checkpoint.bin");
  cp=all[#all]; xx=cp[1]; U=cp[2];
  out=fileopen(logpath,"w");filewrite(out,Str("START LASTIDX=",cp[3]," U_LEN=",#U," G_LEN=",#G," TIME=",gettime()));fileclose(out);
  res=afuchcomplete_from_U(xx,U,G);
  writebin("/workspace/research/beal/data/fdom_level35721_complete_checkpoint_v16.bin",res);
  out=fileopen(logpath,"a");filewrite(out,Str("COMPLETE_DONE U_LEN=",#res[2]," TIME=",gettime()));fileclose(out);1
};
iferr(runcomplete(),err,my(out=fileopen(logpath,"a"));filewrite(out,Str("ERROR=",err));fileclose(out));quit;