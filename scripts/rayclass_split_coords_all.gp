K=bnfinit(x^2-x-1,1);
P3=idealprimedec(K,3)[1]; P5=idealprimedec(K,5)[1];
m=idealmul(K,idealpow(K,P3,3),idealpow(K,P5,3));
B=bnrinit(K,[m,[1,1]],1);
V=[11,19,29,31,41,59,61,71,79,89];
scan()={my(i,l,D,j,e);print("prime,j,norm,e1,e2");for(i=1,#V,l=V[i];D=idealprimedec(K,l);if(#D==2,for(j=1,2,e=Vec(bnrisprincipal(B,D[j],0));print(l,",",j,",",idealnorm(K,D[j]),",",e[1],",",e[2]))));};
scan();
quit;