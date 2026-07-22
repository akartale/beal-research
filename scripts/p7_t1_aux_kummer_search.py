#!/usr/bin/env python3
from __future__ import annotations

from math import isqrt

P=7
# F49 coefficient arithmetic r^2=r+1
def fadd(x,y): return ((x[0]+y[0])%P,(x[1]+y[1])%P)
def fmul(x,y):
 a,b=x;c,d=y
 return ((a*c+b*d)%P,(a*d+b*c+b*d)%P)
def fneg(x): return ((-x[0])%P,(-x[1])%P)
def fscalar(a): return (a%P,0)
roots49=[(0,1),(1,6)]
matrices=[]
for a in range(P):
 for b in range(P):
  for d in range(P):
   if (a+d)%P==1 and (a*d-b*b)%P==6:
    matrices.append((a,b,d))
def eigvec(M,lam):
 a,b,d=M
 for x0 in range(P):
  for x1 in range(P):
   for y0 in range(P):
    for y1 in range(P):
     x=(x0,x1);y=(y0,y1)
     if x==(0,0) and y==(0,0): continue
     e1=fadd(fadd(fmul(x,fscalar(a)),fmul(y,fscalar(b))),fneg(fmul(lam,x)))
     e2=fadd(fadd(fmul(x,fscalar(b)),fmul(y,fscalar(d))),fneg(fmul(lam,y)))
     if e1==(0,0) and e2==(0,0): return x,y
 raise RuntimeError
EIG=[(M,lam,eigvec(M,lam)) for M in matrices for lam in roots49]

def primes(n):
 out=[]
 for x in range(2,n+1):
  if all(x%d for d in range(2,isqrt(x)+1)):out.append(x)
 return out

def invmod(a,q): return pow(a,q-2,q)

def factorint(n):
 fs=[];d=2
 while d*d<=n:
  if n%d==0:
   fs.append(d)
   while n%d==0:n//=d
  d+=1
 if n>1:fs.append(n)
 return fs

def primitive_fp(q):
 for g in range(2,q):
  if all(pow(g,(q-1)//r,q)!=1 for r in factorint(q-1)):return g
 raise RuntimeError

def kclass_fp(z,q,g):
 z%=q
 if z==0: raise ValueError
 mu=pow(z,(q-1)//7,q); zeta=pow(g,(q-1)//7,q)
 cur=1
 for k in range(7):
  if cur==mu:return k
  cur=cur*zeta%q
 raise RuntimeError

# Fq2 represented a+b*w, w^2=w+1
def add2(x,y,q):return ((x[0]+y[0])%q,(x[1]+y[1])%q)
def mul2(x,y,q):
 a,b=x;c,d=y
 return ((a*c+b*d)%q,(a*d+b*c+b*d)%q)
def pow2(x,e,q):
 r=(1,0)
 while e:
  if e&1:r=mul2(r,x,q)
  x=mul2(x,x,q);e//=2
 return r
def inv2(x,q):return pow2(x,q*q-2,q)
def primitive_fq2(q):
 N=q*q-1
 for a in range(q):
  for b in range(q):
   g=(a,b)
   if g==(0,0):continue
   if all(pow2(g,N//r,q)!=(1,0) for r in factorint(N)):return g
 raise RuntimeError
def kclass_fq2(z,q,g):
 N=q*q-1; mu=pow2(z,N//7,q); zeta=pow2(g,N//7,q);cur=(1,0)
 for k in range(7):
  if cur==mu:return k
  cur=mul2(cur,zeta,q)
 raise RuntimeError

def projection_zero_possible(k1,k2,rset):
 # common rational class s shifts both node classes by s
 for M,lam,(x,y) in EIG:
  for s in rset:
   a=(k1+s)%7;b=(k2+s)%7
   z=fadd(fmul(x,fscalar(a)),fmul(y,fscalar(b)))
   if z==(0,0): return True,(M,lam,x,y,s)
 return False,None

hits=[]
for q in primes(2000):
 if q in (2,3,5,7) or (q*q-1)%7: continue
 disc=5%q
 split=pow(disc,(q-1)//2,q)==1
 if split:
  if (q-1)%7:
   continue
  sq=next(x for x in range(q) if x*x%q==disc)
  ws=[((1+sq)*invmod(2,q))%q,((1-sq)*invmod(2,q))%q]
  g=primitive_fp(q)
  for j,w in enumerate(ws):
   den=75%q
   if den==0:continue
   c1=(16+28*w)*invmod(den,q)%q
   wb=(1-w)%q
   c2=(16+28*wb)*invmod(den,q)%q
   kw=kclass_fp(w,q,g); k1=kclass_fp(c1,q,g); k2=kclass_fp(c2,q,g)
   rset={kclass_fp(a,q,g) for a in range(1,q)}
   zero,wit=projection_zero_possible(k1,k2,rset)
   if kw==0 and not zero:
    hits.append((q,'split',j,kw,k1,k2,sorted(rset)))
    print('ELIM',hits[-1])
 else:
  g=primitive_fq2(q);w=(0,1);wb=(1,q-1)
  den=invmod(75%q,q)
  c1=((16*den)%q,(28*den)%q)
  c2=((44*den)%q,(-28*den)%q)
  kw=kclass_fq2(w,q,g);k1=kclass_fq2(c1,q,g);k2=kclass_fq2(c2,q,g)
  rset={kclass_fq2((a,0),q,g) for a in range(1,q)}
  zero,wit=projection_zero_possible(k1,k2,rset)
  if kw==0 and not zero:
   hits.append((q,'inert',kw,k1,k2,sorted(rset)))
   print('ELIM',hits[-1])
print('total_hits',len(hits))