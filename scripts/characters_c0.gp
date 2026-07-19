K=bnfinit(x^2-x-1,1);
P3=idealprimedec(K,3)[1]; P5=idealprimedec(K,5)[1];
m=idealmul(K,idealpow(K,P3,3),idealpow(K,P5,3));
B=bnrinit(K,[m,[1,1]],1);
g=3; /* generator of F_7^* */
scan()={
 my(chars=List(),u,v,l,D,j,lg,e,val,N,tr);
 for(u=0,5, for(v=0,1, listput(chars,[u,3*v])));
 print("character_count=",#chars);
 print("id,y1,y2,l,prime_index,norm,class1,class2,chi,trace");
 for(l=2,47,
   if(isprime(l) && l!=3 && l!=5 && l!=7,
     D=idealprimedec(K,l);
     for(j=1,#D,
       lg=Vec(bnrisprincipal(B,D[j],0)); N=idealnorm(K,D[j]);
       for(k=1,#chars,
         e=(chars[k][1]*lg[1]+chars[k][2]*lg[2])%6;
         val=lift(Mod(g,7)^e);
         tr=lift(Mod(val + (N%7)/val,7));
         print(k,",",chars[k][1],",",chars[k][2],",",l,",",j,",",N,",",lg[1],",",lg[2],",",val,",",tr);
       );
     );
   );
 );
};
scan();