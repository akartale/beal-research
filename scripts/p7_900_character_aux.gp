K=bnfinit(y^2-y-1,1);
P3=idealprimedec(K,3)[1]; P5=idealprimedec(K,5)[1];
m=idealmul(K,idealpow(K,P3,3),idealpow(K,P5,3));
B=bnrinit(K,[m,[1,1]],1);
plist=[11,19,29,31,41,59,61,71,79,89,101,109,131,139,149,151,179,181,191,199,211,229,239,241,251,269,271,281,311,331,349,359,379,389];
out=fileopen("data/p7_900_character_aux.txt","w");
for(j=1,#plist,p=plist[j];D=idealprimedec(K,p);vals=[];for(i=1,#D,if(D[i].f==1,c=bnrisprincipal(B,D[i],0);s=if(c[1]%2,-1,1);vals=concat(vals,s)));if(#vals==2,filewrite(out,Str(p," ",vals[1]," ",vals[2]))));
fileclose(out);
quit;