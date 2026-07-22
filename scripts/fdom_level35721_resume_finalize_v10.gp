default(parisize,"2G");
default(parisizemax,"8G");
out=fileopen("/workspace/research/beal/data/fdom_level35721_resume_finalize_v10.log","w");
read("fdom.gp");
read("/workspace/research/beal/scripts/quaternion_7p3_eichler_lib.gp");
read("/workspace/research/beal/vendor/fdom-memory-reduced/load_memory_reduced.gp");
read("/workspace/research/beal/data/fdom_level35721_tuned.txt");
runresume()={
  my(all,cp,xx,U,G,res);
  all=read("/workspace/research/beal/data/fdom_level35721_reconstruct_batched_v9_checkpoint.bin");
  cp=all[#all]; xx=cp[1]; U=cp[2]; G=PRESENTATION[1];
  filewrite(out,Str("RESUME CHECKPOINTS=",#all," LASTIDX=",cp[3]," U_LEN=",#U," G_LEN=",#G," TIME=",gettime()));
  res=afuchcomplete_from_U(xx,U,G); xx=res[1]; U=res[2];
  filewrite(out,Str("COMPLETE_DONE U_LEN=",#U," TIME=",gettime()));
  xx=afuchfinalize_from_U(xx,U);
  filewrite(out,Str("FINALIZE_DONE SIGNATURE=",afuchsignature(xx)," SIDES=",#afuchsides(xx)," GENERATORS=",#afuchpresentation(xx)[1]," TIME=",gettime()));
  writebin("/workspace/research/beal/data/fdom_level35721_reconstructed_xx_v10.bin",xx);
  1
};
iferr(runresume(),err,filewrite(out,Str("ERROR=",err)));
fileclose(out);quit;