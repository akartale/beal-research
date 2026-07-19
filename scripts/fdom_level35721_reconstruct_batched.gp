default(parisize,"512M");
default(parisizemax,"3G");
logpath="/workspace/research/beal/data/fdom_level35721_reconstruct_batched_v9.log";
checkpoint="/workspace/research/beal/data/fdom_level35721_reconstruct_batched_v9_checkpoint.bin";
finalpath="/workspace/research/beal/data/fdom_level35721_reconstructed_xx_batched_v9.bin";
out=fileopen(logpath,"w");
read("/workspace/research/beal/scripts/quaternion_7p3_eichler_lib.gp");
read("/workspace/research/beal/vendor/fdom-memory-reduced/load_memory_reduced.gp");
read("/workspace/research/beal/data/fdom_level35721_tuned.txt");
levellattice=alglatinter(beala,alglatinter(beala,bealo,bealthreepath[2]),bealsevenpath[2]);
G=PRESENTATION[1];
xx=afuchinit(beala,levellattice[1],0,0);
U=0; batch=32;
filewrite(out,Str("START GENERATORS=",#G," BATCH=",batch)); fileclose(out);
processbound(startidx)=
{
  my(lastidx,res);
  if(startidx>#G,return(1));
  lastidx=min(startidx+batch-1,#G);
  res=afuchnormbound_batch(xx,U,G[startidx..lastidx]); xx=res[1]; U=res[2];
  if(U==0,error("normbound produced no boundary"));
  writebin(checkpoint,[xx,U,lastidx]);
  write(logpath,Str("BOUND_DONE from=",startidx," to=",lastidx," U_LEN=",#U," TIME=",gettime()));
  processbound(lastidx+1)
};
mainrun()=
{
  my(res);
  processbound(1);
  write(logpath,Str("COMPLETE_START U_LEN=",#U," TIME=",gettime()));
  res=afuchcomplete_from_U(xx,U,G); xx=res[1]; U=res[2];
  write(logpath,Str("COMPLETE_DONE U_LEN=",#U," TIME=",gettime()));
  xx=afuchfinalize_from_U(xx,U);
  write(logpath,Str("FINALIZE_DONE TIME=",gettime()));
  writebin(finalpath,xx);
  write(logpath,Str("DONE SIGNATURE=",afuchsignature(xx)," SIDES=",#afuchsides(xx)," GENERATORS=",#afuchpresentation(xx)[1]));
};
mainrun();
quit;
