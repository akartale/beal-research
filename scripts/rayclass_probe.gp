bnf=bnfinit(x^2-x-1);
P3=idealfactor(bnf,3)[1,1]; P5=idealfactor(bnf,5)[1,1]; P7=idealfactor(bnf,7)[1,1];
m=idealmul(bnf,idealmul(bnf,idealpow(bnf,P3,3),idealpow(bnf,P5,3)),P7);
bnr=bnrinit(bnf,[m,[1,1]],1);
print(bnr.cyc);
print(bnr.no);
quit;