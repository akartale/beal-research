K=bnfinit(y^2-y-1,1);
P3=idealprimedec(K,3)[1]; P5=idealprimedec(K,5)[1];
m=idealmul(K,idealpow(K,P3,3),idealpow(K,P5,3));
B=bnrinit(K,[m,[1,1]],1);
print("cyc=",B.cyc);
H=matdiagonal([2,1]);
print("subgroup=",H);
print("classfield_polynomials=",bnrclassfield(B,H,2));
quit;