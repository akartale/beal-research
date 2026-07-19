run()={
 my(T,a,g,zz,mone,P,actualL,r,actual,surv,in49,u,v,chi,tr,i,j);
 T=ffinit(7,12,'t); a=ffgen(T,'a); g=ffprimroot(a);
 zz=g^((7^12-1)/180); mone=a^0*6;
 P=[[0,1],[0,4],[1,4],[1,6],[2,3],[3,1],[3,4],[3,5],[3,6],[4,1],[4,6],[5,2],[5,3],[5,5],[6,3]];
 actualL=List();
 for(i=1,#P,
  r=polrootsmod(x^2-(a^0*P[i][1])*x+(a^0*P[i][2]),a);
  for(j=1,#r,listput(actualL,r[j]));
 );
 actual=Set(Vec(actualL)); surv=List(); in49=0;
 for(u=0,179,
  for(v=0,1,
   chi=zz^((141*u)%180)*mone^v;
   tr=chi+(a^0*(19%7))/chi;
   if(tr^49==tr,in49++);
   if(setsearch(actual,tr),listput(surv,[u,v,chi,tr,tr^49==tr]));
  );
 );
 print("all_characters=360");
 print("actual_trace_values=",#actual);
 print("characters_with_l19_trace_in_F49=",in49);
 print("survivors_at_l19=",#surv);
 print("survivors=",Vec(surv));
};
run();