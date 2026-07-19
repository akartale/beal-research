qx='qx;qy='qy;qa='qa;
bealk=nfinit(qy^3+qy^2-2*qy-1);filewrite(out,Str("LIB_bealk=",type(bealk)));
beala=alginit(bealk,[2,[[],[]],[1/2,0,1/2]],qx);filewrite(out,Str("LIB_beala=",type(beala)));
bealn=12;bealo=alglathnf(beala,matid(bealn));filewrite(out,Str("LIB_bealo=",type(bealo)));

bealpreimage(m,p)=
{ my(n,kmod,g);
  n=matsize(m)[2];kmod=lift(matkermod(lift(m),p));
  g=concat(kmod,p*matid(n));mathnf(g)
}

bealmultable(o)=
{ my(ee,mt,z,c);
  ee=vector(bealn,i,alglatelement(beala,o,vector(bealn,j,j==i)~));
  mt=vector(bealn,i,matrix(bealn,bealn));
  for(i=1,bealn,for(j=1,bealn,
    z=algmul(beala,ee[i],ee[j]);
    if(!alglatcontains(beala,o,z,&c),error("order is not closed"));
    for(r=1,bealn,mt[i][r,j]=c[r])
  ));
  mt
}

bealsublattice(o,h)=
{ my(m);
  m=matrix(bealn,bealn,r,c,alglatelement(beala,o,h[,c])[r]);
  alglathnf(beala,m)
}

bealneighbors(o,p)=
{ my(mt,t,qq,s,proj,n,tom,cone,ctwo,hone,htwo,ione,itwo);
  mt=bealmultable(o);
  if(p==3,
    t=algtableinit(mt,3);proj=matid(bealn);n=3,
    t=algtableinit(mt,7);qq=algquotient(t,algradical(t),1);
    t=qq[1];proj=qq[2];n=1
  );
  s=algsplit(t,qa);
  tom=matinvmod(s[2],p)*proj;
  cone=tom[2*n+1..4*n,];
  ctwo=tom[1..2*n,];
  hone=bealpreimage(cone,p);htwo=bealpreimage(ctwo,p);
  ione=bealsublattice(o,hone);itwo=bealsublattice(o,htwo);
  [alglatlefttransporter(beala,ione,ione),alglatlefttransporter(beala,itwo,itwo)]
}

bealdistance(o)=alglatindex(beala,alglatinter(beala,bealo,o),bealo);

bealbuildpath(p,q,emax)=
{ my(path=vector(emax),cur=bealo,candidates,target,chosen);
  for(e=1,emax,
    candidates=bealneighbors(cur,p);target=q^e;chosen=0;
    for(k=1,#candidates,if(bealdistance(candidates[k])==target,chosen=candidates[k];break));
    if(type(chosen)=="t_INT",error(Str("no forward neighbor at p=",p," step=",e)));
    path[e]=chosen;cur=chosen;
  );
  path
}

bealthreepath=bealbuildpath(3,27,3);
bealsevenpath=bealbuildpath(7,7,3);