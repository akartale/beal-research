default(parisize,"1G");
default(parisizemax,"4G");
read("/workspace/research/beal/scripts/quaternion_7p3_eichler_lib_hilbert.gp");
out=fileopen("/workspace/research/beal/data/probe_checkpoint_structure_35721.txt","w");
runprobe()={
  my(chk,e,n,t1,t2,t3,v3);
  chk=read("/workspace/research/beal/data/fdom_level35721_reconstruct_batched_v9_checkpoint.bin");
  filewrite(out,Str("ROOT_TYPE=",type(chk)," ROOT_LEN=",#chk));
  for(i=1,#chk,
    e=chk[i]; n=if(type(e)=="t_VEC"||type(e)=="t_COL"||type(e)=="t_MAT",#e,-1);
    if(n==3,
      t1=type(e[1]);t2=type(e[2]);t3=type(e[3]);v3=if(t3=="t_INT",e[3],"NA");
      filewrite(out,Str("I=",i," TYPE=",type(e)," LEN=",n," C1=",t1," C2=",t2," C3=",t3," LAST=",v3)),
      filewrite(out,Str("I=",i," TYPE=",type(e)," LEN=",n))
    )
  );
  1
};
iferr(runprobe(),err,filewrite(out,Str("ERROR=",err)));
fileclose(out);quit;