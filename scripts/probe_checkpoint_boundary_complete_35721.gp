default(parisize,"1G");
default(parisizemax,"4G");
read("fdom.gp");
out=fileopen("/workspace/research/beal/data/probe_checkpoint_boundary_complete_35721.log","w");
read("/workspace/research/beal/scripts/quaternion_7p3_eichler_lib.gp");
fileclose(out);
read("/workspace/research/beal/vendor/fdom-memory-reduced/load_memory_reduced.gp");
logpath="/workspace/research/beal/data/probe_checkpoint_boundary_complete_35721.log";
runprobe()={
  my(all,cp,xx,U,out,pair,elts,vc,xf);
  all=read("/workspace/research/beal/data/fdom_level35721_reconstruct_batched_v9_checkpoint.bin");
  cp=all[#all]; xx=cp[1]; U=cp[2];
  out=fileopen(logpath,"a");
  filewrite(out,Str("ROOT_TYPE=",type(U)," ROOT_LEN=",#U," LASTIDX=",cp[3]));
  for(i=1,#U,filewrite(out,Str("SLOT=",i," TYPE=",type(U[i])," LEN=",if(type(U[i])=="t_VEC"||type(U[i])=="t_COL"||type(U[i])=="t_MAT"||type(U[i])=="t_VECSMALL",#U[i],-1))));
  pair=U[8]; elts=U[1]; vc=U[6];
  filewrite(out,Str("PAIR_TYPE=",type(pair)," PAIR_LEN=",if(type(pair)=="t_VEC"||type(pair)=="t_VECSMALL",#pair,-1)," ELTS_LEN=",#elts," VC_LEN=",#vc));
  fileclose(out);
  xf=afuchfinalize_from_U(xx,U);
  writebin("/workspace/research/beal/data/fdom_level35721_direct_finalized_probe.bin",xf);
  out=fileopen(logpath,"a");
  filewrite(out,Str("FINALIZE_OK SIGNATURE=",afuchsignature(xf)," SIDES=",#afuchsides(xf)," GENERATORS=",#afuchpresentation(xf)[1]));
  fileclose(out);
  1
};
iferr(runprobe(),err,my(out=fileopen(logpath,"a"));filewrite(out,Str("ERROR=",err));fileclose(out));
quit;