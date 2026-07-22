#!/usr/bin/env python3
from __future__ import annotations

P=7; M=49

def add(x,y): return ((x[0]+y[0])%M,(x[1]+y[1])%M)
def neg(x): return ((-x[0])%M,(-x[1])%M)
def mul(x,y):
    a,b=x;c,d=y
    return ((a*c+b*d)%M,(a*d+b*c+b*d)%M)
def powr(x,e):
    r=(1,0)
    while e:
        if e&1:r=mul(r,x)
        x=mul(x,x);e//=2
    return r
def inv(x): return powr(x, M*M-2) if False else next(y for y in U if mul(x,y)==(1,0))
def scalar(a): return (a%M,0)
def norm7(x):
    a,b=x; return (a*a+a*b-b*b)%P
def isunit(x): return norm7(x)!=0
U=[(a,b) for a in range(M) for b in range(M) if isunit((a,b))]
H={powr(x,7) for x in U}
unseen=set(U); idx={}; cosets=[]
while unseen:
    g=next(iter(unseen)); C={mul(g,h) for h in H}; i=len(cosets)
    for x in C: idx[x]=i
    cosets.append(C); unseen-=C

def poly_q(x): return add(add(mul(scalar(5),mul(x,x)),mul(scalar(-2),x)),scalar(1))
def D(x): return add(mul(scalar(90),mul(mul(x,x),x)),scalar(18))
def gp(x): return add(mul(scalar(2),x),scalar(-1))
def coeff(x):
    den=mul(scalar(9),mul(mul(gp(x),gp(x)),poly_q(x)))
    return mul(D(x),inv(den))

w=(0,1); wb=add((1,0),neg(w))
for name,x in [('w',w),('1-w',wb)]:
    c=coeff(x)
    line=sorted({idx[mul(c,(a,0))] for a in range(M) if a%P})
    print(name,'x',x,'D',D(x),'q',poly_q(x),'gprime',gp(x),'coeff',c,'coeff_coset',idx[c])
    print(name,'affine_rational_line',line,'contains_w',idx[w] in line,'contains_split',idx[(1,0)] in line)
print('w_coset',idx[w],'split_coset',idx[(1,0)])