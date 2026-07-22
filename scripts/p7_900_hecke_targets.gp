K=bnfinit(y^2-y-1,1);
P3=idealprimedec(K,3)[1]; P5=idealprimedec(K,5)[1];
m=idealmul(K,idealpow(K,P3,3),idealpow(K,P5,3));
B=bnrinit(K,[m,[1,1]],1);
plist=[11,19,29];
for(j=1,#plist,p=plist[j];D=idealprimedec(K,p);for(i=1,#D,if(D[i].f==1,c=bnrisprincipal(B,D[i],0);s=if(c[1]%2,-1,1);t=lift(Mod(s*(1+p),7));print(p," ",i," ",c," ",s," ",t))));
quit;