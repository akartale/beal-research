o=fileopen("research/beal/data/gp_identifier_probe.txt","w");
bealK=5;filewrite(o,Str("bealK=",bealK,",",type(bealK)));
bealk=6;filewrite(o,Str("bealk=",bealk,",",type(bealk)));
foo_bar=7;filewrite(o,Str("foo_bar=",foo_bar,",",type(foo_bar)));
fileclose(o);quit;