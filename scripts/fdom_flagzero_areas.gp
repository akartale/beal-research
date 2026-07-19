default(parisizemax,"8G");
out=fileopen("/workspace/research/beal/data/fdom_flagzero_areas.txt","w");
read("/workspace/research/beal/scripts/quaternion_7p3_eichler_lib.gp");
read("fdom.gp");
onearea(ethree,eseven)=
{ my(levellattice,xx,area,ratio);
  levellattice=alglatinter(beala,alglatinter(beala,bealo,bealthreepath[ethree]),bealsevenpath[eseven]);
  xx=afuchinit(beala,levellattice[1],0,0);
  area=xx[12][1];
  ratio=bestappr(area/Pi,10^8);
  filewrite(out,Str("E=",ethree,",",eseven," INDEX=",alglatindex(beala,levellattice,bealo)," AREA=",area," AREA_OVER_PI=",ratio," EULER_MINUS=",ratio/2," LEVEL=",algorderlevel(beala,levellattice[1],0)));
}
onearea(2,2);
onearea(2,3);
onearea(3,2);
onearea(3,3);
fileclose(out);quit;