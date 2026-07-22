default(parisize,"1G");
default(parisizemax,"4G");
read("/workspace/research/beal/scripts/quaternion_7p3_eichler_lib_hilbert.gp");
install("afuchword","GG","afuchword","/workspace/research/beal/vendor/fdom-upstream/libfdom-2-15-2.so");
out=fileopen("/workspace/research/beal/data/probe_afuchword_checkpoint_v4_35721.txt","w");
runprobe()={
  my(chk,xx,U,last,P,wg);
  read("/workspace/research/beal/data/fdom_level35721_tuned.txt");
  P=PRESENTATION;
  chk=read("/workspace/research/beal/data/fdom_level35721_reconstruct_batched_v9_checkpoint.bin");
  filewrite(out,Str("CHK_TYPE=",type(chk)," CHK_LEN=",#chk));
  xx=chk[1]; U=chk[2]; last=chk[3];
  filewrite(out,Str("LAST_TYPE=",type(last)," LAST=",last," U_LEN=",#U," XX_LEN=",#xx));
  wg=afuchword(xx,P[1][1]);
  filewrite(out,Str("GENERATOR_WORD=",wg));
  filewrite(out,Str("GENERATOR_TYPE=",type(wg)));
  1
};
iferr(runprobe(),err,filewrite(out,Str("ERROR=",err)));
fileclose(out);quit;