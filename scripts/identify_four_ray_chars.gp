K=bnfinit(x^2-x-1,1);
P3=idealprimedec(K,3)[1];P5=idealprimedec(K,5)[1];
m=idealmul(K,idealpow(K,P3,3),idealpow(K,P5,3));
B=bnrinit(K,[m,[1,1]],1);
C=[[0,0],[0,1],[90,0],[90,1]];
print("cyc=",B.cyc);
for(i=1,#C,print("char=",C[i]," conductor=",bnrconductorofchar(B,C[i])));
quit;