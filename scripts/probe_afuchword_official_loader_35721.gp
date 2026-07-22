default(parisize,"1G");
default(parisizemax,"4G");
out=fileopen("/workspace/research/beal/data/probe_afuchword_official_loader_35721.txt","w");
read("fdom.gp");
read("/workspace/research/beal/scripts/quaternion_7p3_eichler_lib_hilbert.gp");
runprobe()={
  my(all,cp,xx,P,w1,w2);
  read("/workspace/research/beal/data/fdom_level35721_tuned.txt");
  P=PRESENTATION;
  all=read("/workspace/research/beal/data/fdom_level35721_reconstruct_batched_v9_checkpoint.bin");
  cp=all[#all]; xx=cp[1];
  filewrite(out,Str("CHECKPOINTS=",#all," LASTIDX=",cp[3]," XX_LEN=",#xx," U_LEN=",#cp[2]));
  w1=afuchword(xx,P[1][1]);
  w2=afuchword(xx,P[1][2]);
  filewrite(out,Str("WORD1=",w1));
  filewrite(out,Str("WORD2=",w2));
  filewrite(out,Str("TYPE1=",type(w1)," LEN1=",#w1," TYPE2=",type(w2)," LEN2=",#w2));
  1
};
iferr(runprobe(),err,filewrite(out,Str("ERROR=",err)));
fileclose(out);quit;