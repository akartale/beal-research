bnf=bnfinit(x^2-x-1);
P3=idealfactor(bnf,3)[1,1]; P5=idealfactor(bnf,5)[1,1]; P7=idealfactor(bnf,7)[1,1];
m=idealmul(bnf,idealmul(bnf,idealpow(bnf,P3,3),idealpow(bnf,P5,3)),P7);
bnr=bnrinit(bnf,[m,[1,1]],1);
V=[11,19,29,31,41,59,61,71,79,89];
file="research/beal/p7_rayclass_coords_full.csv";
write(file,"prime,e1,e2,e3,norm");
for(i=1,#V,l=V[i];P=idealfactor(bnf,l)[1,1];e=bnrisprincipal(bnr,P,0);write(file,l,",",e[1],",",e[2],",",e[3],",",idealnorm(bnf,P)));
quit;