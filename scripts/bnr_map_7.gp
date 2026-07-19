K=bnfinit(x^2-x-1,1);
P3=idealprimedec(K,3)[1]; P5=idealprimedec(K,5)[1]; P7=idealprimedec(K,7)[1];
m0=idealmul(K,idealpow(K,P3,3),idealpow(K,P5,3));
m1=idealmul(K,m0,P7);
B0=bnrinit(K,[m0,[1,1]],1);
B1=bnrinit(K,[m1,[1,1]],1);
print("B1 cyc=",B1.cyc," B0 cyc=",B0.cyc);
M=bnrmap(B1,B0);
print(M);