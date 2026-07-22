default(parisize,"2G");
default(parisizemax,"8G");
read("fdom.gp");
out=fileopen("/workspace/research/beal/data/fdom_level35721_finalize_loader_v11.log","w");
read("/workspace/research/beal/scripts/quaternion_7p3_eichler_lib.gp");
fileclose(out);
read("/workspace/research/beal/vendor/fdom-memory-reduced/load_memory_reduced.gp");
logpath="/workspace/research/beal/data/fdom_level35721_finalize_v11.log";
runfinalize()={
  my(res,xx,U,out);
  res=read("/workspace/research/beal/data/fdom_level35721_complete_checkpoint_v11.bin");
  xx=res[1]; U=res[2];
  out=fileopen(logpath,"w");
  filewrite(out,Str("START U_LEN=",#U," TIME=",gettime()));
  fileclose(out);
  xx=afuchfinalize_from_U(xx,U);
  writebin("/workspace/research/beal/data/fdom_level35721_reconstructed_xx_v11.bin",xx);
  out=fileopen(logpath,"a");
  filewrite(out,Str("FINALIZE_DONE SIGNATURE=",afuchsignature(xx)," SIDES=",#afuchsides(xx)," GENERATORS=",#afuchpresentation(xx)[1]," TIME=",gettime()));
  fileclose(out);
  1
};
iferr(runfinalize(),err,my(out=fileopen(logpath,"a"));filewrite(out,Str("ERROR=",err));fileclose(out));
quit;