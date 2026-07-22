K=bnfinit(x^2-x-1,1);
P3=idealprimedec(K,3)[1]; P5=idealprimedec(K,5)[1];
m=idealmul(K,idealpow(K,P3,3),idealpow(K,P5,3));
B=bnrinit(K,[m,[1,1]],1);
P=[11,19,29,31,41,59,61,71,79,89];
print("cyc=",B.cyc);
for(j=1,#P,D=idealprimedec(K,P[j]);if(#D==2,print(P[j],"|",Vec(bnrisprincipal(B,D[1],0)),"|",Vec(bnrisprincipal(B,D[2],0)))));
quit;