K=bnfinit(x^2-x-1,1);
P3=idealprimedec(K,3)[1]; P5=idealprimedec(K,5)[1];
m=idealmul(K,idealpow(K,P3,3),idealpow(K,P5,3));
B=bnrinit(K,[m,[1,1]],1);
D=idealprimedec(K,19);
print("cyc=",B.cyc);
print("number_of_primes=",#D);
for(i=1,#D,print("i=",i," norm=",idealnorm(K,D[i])," coords=",Vec(bnrisprincipal(B,D[i],0))));
quit;