o=fileopen("/workspace/research/beal/data/gp_lowercase_nf_probe.txt","w");
qx='qx;qy='qy;
bealk=nfinit(qy^3+qy^2-2*qy-1);
filewrite(o,Str("bealk=",type(bealk)));
beala=alginit(bealk,[2,[[],[]],[1/2,1/2,0]],qx);
filewrite(o,Str("beala=",type(beala)));
fileclose(o);quit;