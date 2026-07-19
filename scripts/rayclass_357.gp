K=bnfinit(x^2-x-1,1);
P3=idealprimedec(K,3)[1];
P5=idealprimedec(K,5)[1];
P7=idealprimedec(K,7)[1];
print("P3 norm=",idealnorm(K,P3)," P5 norm=",idealnorm(K,P5)," P7 norm=",idealnorm(K,P7));
scan()={
  my(a,b,c,m,B,cyc,n6);
  for(a=0,3,
    for(b=0,3,
      for(c=0,2,
        m=idealmul(K,idealmul(K,idealpow(K,P3,a),idealpow(K,P5,b)),idealpow(K,P7,c));
        B=bnrinit(K,[m,[1,1]],1);
        cyc=B.cyc;
        n6=prod(i=1,#cyc,gcd(cyc[i],6));
        print("a=",a," b=",b," c=",c," cyc=",cyc," chars_order_div_6=",n6);
      );
    );
  );
};
scan();