bnf=bnfinit(x^2-x-1);
P3=idealfactor(bnf,3)[1,1]; P5=idealfactor(bnf,5)[1,1]; P7=idealfactor(bnf,7)[1,1];
row(a,b,c,arch)={my(m,bnr,h);m=matid(2);if(a>0,m=idealmul(bnf,m,idealpow(bnf,P3,a)));if(b>0,m=idealmul(bnf,m,idealpow(bnf,P5,b)));if(c>0,m=idealmul(bnf,m,idealpow(bnf,P7,c)));if(arch,bnr=bnrinit(bnf,[m,[1,1]],1),bnr=bnrinit(bnf,m,1));h=1;for(i=1,#bnr.cyc,h*=gcd(bnr.cyc[i],6));print(a,",",b,",",c,",",arch,",",bnr.cyc,",",bnr.no,",",h)};
print("a3,a5,a7,arch,cyc,order,hom_to_C6");
for(a=0,3,for(b=0,3,for(c=0,1,for(s=0,1,row(a,b,c,s)))));
quit;