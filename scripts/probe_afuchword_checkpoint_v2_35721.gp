default(parisize,"1G");
default(parisizemax,"4G");
install(afuchword,GG,afuchword,"/workspace/research/beal/vendor/fdom-upstream/libfdom-2-15-2.so");
out=fileopen("/workspace/research/beal/data/probe_afuchword_checkpoint_v2_35721.txt","w");
runprobe()={
  my(chk,xx,U,last,P,wg);
  read("/workspace/research/beal/data/fdom_level35721_tuned.txt");
  P=PRESENTATION;
  chk=readbin("/workspace/research/beal/data/fdom_level35721_reconstruct_batched_v9_checkpoint.bin");
  xx=chk[1]; U=chk[2]; last=chk[3];
  filewrite(out,Str("CHECKPOINT_LAST=",last," U_LEN=",#U," XX_LEN=",#xx));
  wg=afuchword(xx,P[1][1]);
  filewrite(out,Str("GENERATOR_WORD=",wg));
  filewrite(out,Str("GENERATOR_TYPE=",type(wg)));
  1
};
iferr(runprobe(),err,filewrite(out,Str("ERROR=",err)));
fileclose(out);quit;