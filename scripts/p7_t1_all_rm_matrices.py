#!/usr/bin/env python3
from __future__ import annotations

P=7; MOD=49

def uadd(x,y): return ((x[0]+y[0])%MOD,(x[1]+y[1])%MOD)
def umul(x,y):
    a,b=x;c,d=y
    return ((a*c+b*d)%MOD,(a*d+b*c+b*d)%MOD)
def upow(x,e):
    r=(1,0)
    while e:
        if e&1:r=umul(r,x)
        x=umul(x,x); e//=2
    return r
def unorm7(x):
    a,b=x; return (a*a+a*b-b*b)%P
def unit(x): return unorm7(x)!=0
U=[(a,b) for a in range(MOD) for b in range(MOD) if unit((a,b))]
H={upow(x,7) for x in U}
# Build quotient group and additive coordinates with generators.
unseen=set(U); cosets=[]; idx={}
while unseen:
    g=next(iter(unseen)); C={umul(g,h) for h in H}; i=len(cosets)
    for x in C: idx[x]=i
    cosets.append(C); unseen-=C
one=idx[(1,0)]
# quotient operation
qmul=lambda i,j: idx[umul(next(iter(cosets[i])),next(iter(cosets[j])))]
# choose two independent order-7 generators
nonzero=[i for i in range(len(cosets)) if i!=one]
g1=nonzero[0]
span1={one}; cur=one
for _ in range(1,7): cur=qmul(cur,g1); span1.add(cur)
g2=next(i for i in nonzero if i not in span1)
coord={}
for a in range(7):
    x=one
    for _ in range(a): x=qmul(x,g1)
    for b in range(7):
        y=x
        for _ in range(b): y=qmul(y,g2)
        coord[y]=(a,b)
assert len(coord)==49

def v(x): return coord[idx[x]]
# F49 arithmetic z=a+b*r with r^2=r+1
fadd=lambda x,y:((x[0]+y[0])%P,(x[1]+y[1])%P)
def fmul(x,y):
    a,b=x;c,d=y
    return ((a*c+b*d)%P,(a*d+b*c+b*d)%P)
def fneg(x): return ((-x[0])%P,(-x[1])%P)
def finv(x):
    for a in range(P):
      for b in range(P):
        if fmul(x,(a,b))==(1,0): return (a,b)
    raise ZeroDivisionError(x)
def fdiv(x,y): return fmul(x,finv(y))
def fscalar(a): return (a%P,0)

def tensor_comb(a,va,b,vb):
    # a,b in F49; va,vb in F7^2; output F49^2
    return (fadd(fmul(a,fscalar(va[0])),fmul(b,fscalar(vb[0]))),
            fadd(fmul(a,fscalar(va[1])),fmul(b,fscalar(vb[1]))))
def det(x,y): return fadd(fmul(x[0],y[1]),fneg(fmul(x[1],y[0])))

cw=(27,35); cb=(13,14); w=(0,1)
vr=v((2,0)) # generator of rational-unit line if nonzero; otherwise find one
if vr==(0,0):
    vr=next(v((a,0)) for a in range(1,MOD) if a%P and v((a,0))!=(0,0))
vcw=v(cw); vcb=v(cb); vw=v(w)
print('quotient_basis_cosets',g1,g2)
print('vectors rational,cw,c1-w,w',vr,vcw,vcb,vw)

# symmetric matrices M=[[a,b],[b,d]] with trace 1, det -1, hence M^2-M-I=0.
matrices=[]
for a in range(P):
 for b in range(P):
  for d in range(P):
   if (a+d)%P==1 and (a*d-b*b)%P==P-1:
    matrices.append((a,b,d))
print('symmetric_rm_matrices',len(matrices),matrices)
roots=[(0,1),(1,P-1)] # r and 1-r
hits=[]; total=0
for M in matrices:
 a,b,d=M
 for lam in roots:
  # left eigenvector l=(x,y), choose a nonzero solution to l M=lam l
  eig=[]
  for x0 in range(P):
   for x1 in range(P):
    for y0 in range(P):
     for y1 in range(P):
      x=(x0,x1); y=(y0,y1)
      if x==(0,0) and y==(0,0): continue
      e1=fadd(fadd(fmul(x,fscalar(a)),fmul(y,fscalar(b))),fneg(fmul(lam,x)))
      e2=fadd(fadd(fmul(x,fscalar(b)),fmul(y,fscalar(d))),fneg(fmul(lam,y)))
      if e1==(0,0) and e2==(0,0): eig=[x,y]; break
     if eig: break
    if eig: break
   if eig: break
  x,y=eig
  for s in range(P):
   va=((vcw[0]+s*vr[0])%P,(vcw[1]+s*vr[1])%P)
   vb=((vcb[0]+s*vr[0])%P,(vcb[1]+s*vr[1])%P)
   z=tensor_comb(x,va,y,vb)
   total+=1
   split=(z[0]==(0,0) and z[1]==(0,0))
   global_w=(det(z,(fscalar(vw[0]),fscalar(vw[1])))==(0,0))
   if split or global_w:
    hits.append({'M':M,'lambda':lam,'eig':(x,y),'s':s,'z':z,'split':split,'global_w_line':global_w})
print('tested',total,'hits',len(hits))
for h in hits: print(h)