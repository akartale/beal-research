#!/usr/bin/env python3
from pathlib import Path
P=[11,19,29,31,41,59,61,71,79,89]
C={11:((77,0),(167,0)),19:((141,1),(141,1)),29:((44,1),(134,1)),31:((106,0),(106,0)),41:((163,0),(73,0)),59:((58,1),(148,1)),61:((92,0),(92,0)),71:((39,0),(129,0)),79:((179,1),(179,1)),89:((132,1),(42,1))}
def split(e):
 b=e[1:-1];o=[];s=0;d=0
 for i,ch in enumerate(b):
  if ch=='[':d+=1
  elif ch==']':d-=1
  elif ch==',' and d==0:o.append(b[s:i].strip());s=i+1
 o.append(b[s:].strip());return o
def entry(data,p):
 i=data.find(f'<{p},');j=data.find('>,<',i)
 if j<0:j=data.find('>];',i)
 return split(data[i:j+1])
def main():
 data=Path('upstream/GFE-5p3/Outputs/Data.txt').read_text(); R={p:entry(data,p) for p in P}
 L=["x='x;","rootany(z,L)={my(i);for(i=1,#L,if(subst(L[i],x,z)==0,return(1)));0};","T=ffinit(7,12,'t);a=ffgen(T,'a);g=ffprimroot(a);zz=g^((7^12-1)/180);mone=a^0*6;","A=List();for(u=0,179,for(v=0,1,listput(A,[u,v])));","step(A,p,c1,c2,G,Z,I,r)={my(N=List(),j,u,v,h1,h2,t1,t2,q1,q2,okg,ok0,ok1,oki);for(j=1,#A,u=A[j][1];v=A[j][2];h1=zz^((c1[1]*u)%180)*mone^((c1[2]*v)%2);h2=zz^((c2[1]*u)%180)*mone^((c2[2]*v)%2);t1=h1+(a^0*(p%7))/h1;t2=h2+(a^0*(p%7))/h2;q1=if(r==2,t1^2-a^0*((2*p)%7),t1);q2=if(r==2,t2^2-a^0*((2*p)%7),t2);okg=rootany(t1,G)&&rootany(t2,G);ok0=rootany(q1,Z)&&rootany(q2,Z);ok1=(t1==a^0*((p+1)%7)||t1==a^0*((-(p+1))%7))&&(t2==a^0*((p+1)%7)||t2==a^0*((-(p+1))%7));oki=rootany(q1,I)&&rootany(q2,I);if(okg||ok0||ok1||oki,listput(N,[u,v])));N};"]
 for p in P:
  f=R[p];c1,c2=C[p];r=1 if p%15==1 else 2
  L += [f"A=step(A,{p},{list(c1)},{list(c2)},{f[1]},{f[2]},{f[3]},{r});",f"print(\"p={p} union=\",#A,\" \",Vec(A));"]
 L += ["quit;"]
 Path('scripts/lemmaD_union_multprime.gp').write_text('\n'.join(L)+'\n')
if __name__=='__main__':main()