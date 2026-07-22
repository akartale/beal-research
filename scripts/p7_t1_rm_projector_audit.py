#!/usr/bin/env python3
"""Canonical-projector audit for the t=1 RM/Kummer argument.

This replaces the invalid eigenvector-normalization test.  For every symmetric
T in M_2(F_7) with T^2-T-I=0 and each root lambda in F_49, use the canonical
idempotent P_lambda=(T-lambda' I)/(lambda-lambda').  Compare P_lambda q(s)
against the projected global admissible classes: zero and the F_7-line
spanned by the diagonal fundamental-unit class (w,w).
"""
P=7

def add(x,y): return ((x[0]+y[0])%P,(x[1]+y[1])%P)
def neg(x): return ((-x[0])%P,(-x[1])%P)
def sub(x,y): return add(x,neg(y))
def mul(x,y):
    a,b=x;c,d=y
    return ((a*c+b*d)%P,(a*d+b*c+b*d)%P)
def pw(x,n):
    r=(1,0)
    while n:
        if n&1:r=mul(r,x)
        x=mul(x,x);n//=2
    return r
def inv(x):
    if x==(0,0): raise ZeroDivisionError
    return pw(x,P*P-2)
def smul(c,x): return mul((c%P,0),x)
ZERO=(0,0); ONE=(1,0)

def madd(A,B): return [[add(A[i][j],B[i][j]) for j in range(2)] for i in range(2)]
def msub(A,B): return [[sub(A[i][j],B[i][j]) for j in range(2)] for i in range(2)]
def mmul(A,B):
    return [[add(mul(A[i][0],B[0][j]),mul(A[i][1],B[1][j])) for j in range(2)] for i in range(2)]
def mscale(c,A): return [[mul(c,A[i][j]) for j in range(2)] for i in range(2)]
def mvec(A,v): return [add(mul(A[i][0],v[0]),mul(A[i][1],v[1])) for i in range(2)]
I=[[ONE,ZERO],[ZERO,ONE]]

def tf(a): return (a%P,0)
Ts=[]
for a in range(P):
  for b in range(P):
    for d in range(P):
      T=[[tf(a),tf(b)],[tf(b),tf(d)]]
      if msub(msub(mmul(T,T),T),I)==[[ZERO,ZERO],[ZERO,ZERO]]: Ts.append(T)

roots=[(0,1),(1,6)]
base=[(5,4),(5,3)]
wdiag=[(0,1),(0,1)]
print('ROSATI_COUNT',len(Ts))
bad=[]
for ti,T in enumerate(Ts,1):
  for li,lam in enumerate(roots):
    lamp=roots[1-li]
    Plam=mscale(inv(sub(lam,lamp)),msub(T,mscale(lamp,I)))
    assert mmul(Plam,Plam)==Plam
    gw=mvec(Plam,wdiag)
    for s in range(P):
      q=[add(base[0],tf(s)),add(base[1],tf(s))]
      pq=mvec(Plam,q)
      split=(pq==[ZERO,ZERO])
      unit=any(pq==[smul(c,gw[0]),smul(c,gw[1])] for c in range(1,P))
      if split or unit: bad.append((ti,T,li,lam,s,pq,gw,split,unit))
print('BAD_COUNT',len(bad))
for row in bad: print('BAD',row)
print('PROJECTOR_AUDIT_DONE',1)