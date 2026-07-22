#!/usr/bin/env python3
from pathlib import Path
import re

def split_entry(entry):
    body=entry[1:-1]; out=[]; start=0; depth=0
    for i,ch in enumerate(body):
        if ch=='[': depth+=1
        elif ch==']': depth-=1
        elif ch==',' and depth==0:
            out.append(body[start:i].strip()); start=i+1
    out.append(body[start:].strip()); return out

def entries(data):
    out=[]; i=0
    while True:
        i=data.find('<',i)
        if i<0: break
        depth=0; j=i
        while j<len(data):
            if data[j]=='[': depth+=1
            elif data[j]==']': depth-=1
            elif data[j]=='>' and depth==0: break
            j+=1
        e=data[i:j+1]; f=split_entry(e)
        if f and f[0].isdigit(): out.append((int(f[0]),f))
        i=j+1
    return out

def main():
    data=Path('upstream/GFE-5p3/Outputs/Data.txt').read_text()
    E=[(p,f) for p,f in entries(data) if p not in (3,5,7) and p%5 in (1,4)]
    L=["x='x;",
       "K=bnfinit(x^2-x-1,1);P3=idealprimedec(K,3)[1];P5=idealprimedec(K,5)[1];m=idealmul(K,idealpow(K,P3,3),idealpow(K,P5,3));B=bnrinit(K,[m,[1,1]],1);",
       "rootany(z,L)={my(i);for(i=1,#L,if(subst(L[i],x,z)==0,return(1)));0};",
       "T=ffinit(7,12,'t);a=ffgen(T,'a);g=ffprimroot(a);zz=g^((7^12-1)/180);mone=a^0*6;",
       "A=List();for(u=0,179,for(v=0,1,listput(A,[u,v])));",
       "step(A,p,G,Z,I,r)={my(N=List(),D,c1,c2,j,u,v,h1,h2,t1,t2,q1,q2,okg,ok0,ok1,oki);D=idealprimedec(K,p);c1=Vec(bnrisprincipal(B,D[1],0));c2=Vec(bnrisprincipal(B,D[2],0));for(j=1,#A,u=A[j][1];v=A[j][2];h1=zz^((c1[1]*u)%180)*mone^((c1[2]*v)%2);h2=zz^((c2[1]*u)%180)*mone^((c2[2]*v)%2);t1=h1+(a^0*(p%7))/h1;t2=h2+(a^0*(p%7))/h2;q1=if(r==2,t1^2-a^0*((2*p)%7),t1);q2=if(r==2,t2^2-a^0*((2*p)%7),t2);okg=rootany(t1,G)&&rootany(t2,G);ok0=rootany(q1,Z)&&rootany(q2,Z);ok1=(t1==a^0*((p+1)%7)||t1==a^0*((-(p+1))%7))&&(t2==a^0*((p+1)%7)||t2==a^0*((-(p+1))%7));oki=rootany(q1,I)&&rootany(q2,I);if(okg||ok0||ok1||oki,listput(N,[u,v])));N};"]
    for p,f in E:
        ratio=1 if p%15==1 else 2
        L.append(f"A=step(A,{p},{f[1]},{f[2]},{f[3]},{ratio});")
        L.append(f"print(\"p={p} union=\",#A,\" \",Vec(A));")
    L.append("quit;")
    Path('scripts/lemmaD_union_all_split.gp').write_text('\n'.join(L)+'\n')
    print('split_primes=',[p for p,_ in E])
if __name__=='__main__':main()