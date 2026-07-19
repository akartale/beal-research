default(parisizemax,"2G");
out=fileopen("/workspace/research/beal/data/fdom_area_grid.txt","w");
read("/workspace/research/beal/scripts/quaternion_7p3_eichler_lib.gp");
read("fdom.gp");
gridarea(ethree,eseven)=
{ my(levellattice=bealo,xx,ratio);
  if(ethree>0,levellattice=alglatinter(beala,levellattice,bealthreepath[ethree]));
  if(eseven>0,levellattice=alglatinter(beala,levellattice,bealsevenpath[eseven]));
  xx=afuchinit(beala,levellattice[1],0,0);
  ratio=bestappr(xx[12][1]/Pi,10^8);
  filewrite(out,Str(ethree," ",eseven," ",ratio," ",ratio/2," ",alglatindex(beala,levellattice,bealo)));
}
for(e=0,3,gridarea(e,0);gridarea(e,1);gridarea(e,2);gridarea(e,3));
fileclose(out);quit;