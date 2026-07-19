K=bnfinit(x^2-x-1,1);
P3=idealprimedec(K,3)[1]; P5=idealprimedec(K,5)[1];
m=idealmul(K,idealpow(K,P3,3),idealpow(K,P5,3));
B=bnrinit(K,[m,[1,1]],1);
print("cyc=",B.cyc);
scan()={
 my(l,D,j);
 forprime(l=2,31,
   if(l!=3 && l!=5 && l!=7,
     D=idealprimedec(K,l);
     for(j=1,#D,
       print("l=",l," j=",j," norm=",idealnorm(K,D[j])," log=",bnrisprincipal(B,D[j],0));
     );
   );
 );
};
scan();