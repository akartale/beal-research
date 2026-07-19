#!/usr/bin/env python3
from pathlib import Path
PRIMES=[11,19,29,31,41,59,61,71,79,89]
def add(x,y):return((x[0]+y[0])%7,(x[1]+y[1])%7)
def mul(x,y):return((x[0]*y[0]+5*x[1]*y[1])%7,(x[0]*y[1]+x[1]*y[0])%7)
def pw(x,n):
 r=(1,0)
 while n:
  if n&1:r=mul(r,x)
  x=mul(x,x);n//=2
 return r
def primitive():
 for a in range(7):
  for b in range(7):
   x=(a,b)
   if x!=(0,0) and pw(x,48)==(1,0) and pw(x,24)!=(1,0) and pw(x,16)!=(1,0):return x
 raise RuntimeError
G=primitive()
def leg(a,p):
 a%=p
 return 0 if a==0 else (1 if pow(a,(p-1)//2,p)==1 else -1)
def nsq(p):return next(d for d in range(2,p) if leg(d,p)==-1)
def m2(x,y,d,p):return((x[0]*y[0]+d*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
def a2(x,y,p):return((x[0]+y[0])%p,(x[1]+y[1])%p)
def s2(k,x,p):return(k*x[0]%p,k*x[1]%p)
def f1(x,t,p):return(5*pow(x,6,p)-12*pow(x,5,p)+10*t*pow(x,3,p)+t*t)%p
def f2(x,t,d,p):
 x2=m2(x,x,d,p);x3=m2(x2,x,d,p);x5=m2(m2(x3,x,d,p),x,d,p);x6=m2(x3,x3,d,p)
 return a2(a2(s2(5,x6,p),s2(-12,x5,p),p),a2(s2(10*t,x3,p),(t*t%p,0),p),p)
def c2(z,d,p):return 0 if z==(0,0) else leg((z[0]*z[0]-d*z[1]*z[1])%p,p)
def tracepoly(t,p):
 n1=p+sum(leg(f1(x,t,p),p) for x in range(p))+(2 if leg(5,p)==1 else 0);d=nsq(p)
 n2=p*p+sum(c2(f2((a,b),t,d,p),d,p) for a in range(p) for b in range(p))+2
 s=p+1-n1;return s,(n2-p*p-1+s*s)//2-2*p
def roots(s,q):
 out=set()
 for a in range(7):
  for b in range(7):
   x=(a,b)
   if add(add(mul(x,x),((-s*a)%7,(-s*b)%7)),(q%7,0))==(0,0):out.add(x)
 return out
def tvals(p):
 sev={pow(c,7,p) for c in range(1,p)};v=set()
 for A in range(1,p):
  a3=pow(A,3,p);iv=pow(a3,-1,p)
  for B in range(1,p):
   if (a3+pow(B,5,p))%p in sev:v.add((-pow(B,5,p)*iv)%p)
 return sorted(v-{0,1})
def coords():
 d={}
 for line in Path('research/beal/p7_rayclass_coords_full.csv').read_text().splitlines()[1:]:
  l,e1,e2,e3,n=line.split(',');d[int(l)]=(int(e1),int(e2),int(e3),int(n))
 return d
def main():
 alive={(k1,k2,k3) for k1 in range(0,48,2) for k2 in range(0,48,4) for k3 in (0,24)};co=coords();print('G',G,'initial',len(alive))
 for l in PRIMES:
  e1,e2,e3,n=co[l];F=set()
  tv=tvals(l)
  for t in tv:
   s,q=tracepoly(t,l);F|=roots(s,q)
  nxt=set()
  for k1,k2,k3 in alive:
   chi=pw(G,(k1*e1+k2*e2+k3*e3)%48);tr=add(chi,mul((n%7,0),pw(chi,47)))
   if tr in F:nxt.add((k1,k2,k3))
  alive=nxt;print(l,'t',len(tv),'traces',len(F),'survivors',len(alive),sorted(alive))
  if not alive:break
if __name__=='__main__':main()