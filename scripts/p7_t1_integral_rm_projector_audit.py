#!/usr/bin/env python3
"""Canonical projector audit restricted to integral Rosati RM matrices.

If Q_mon=ell I in the oriented node-loop basis and the Rosati-fixed generator
omega satisfies omega^2-omega-1=0, then its integral matrix T is symmetric,
tr(T)=1, det(T)=-1.  Hence T=[[a,b],[b,1-a]] with
b^2=1-a^2+a, giving exactly four integral matrices.
"""
from p7_t1_rm_projector_audit import *

Tint=[]
for a in range(-10,11):
    for b in range(-10,11):
        d=1-a
        if a*d-b*b==-1:
            Tint.append([[tf(a),tf(b)],[tf(b),tf(d)]])
print('INTEGRAL_RM_COUNT',len(Tint))
for T in Tint: print('TINT',T)

roots=[(0,1),(1,6)]
base=[(5,4),(5,3)]
wdiag=[(0,1),(0,1)]
bad=[]
for ti,T in enumerate(Tint,1):
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
print('INTEGRAL_BAD_COUNT',len(bad))
for row in bad: print('BAD',row)
print('INTEGRAL_PROJECTOR_AUDIT_DONE',1)