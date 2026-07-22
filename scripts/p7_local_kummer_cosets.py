#!/usr/bin/env python3
from __future__ import annotations

P=7
M=49

def mul(x,y):
    a,b=x;c,d=y
    return ((a*c+b*d)%M,(a*d+b*c+b*d)%M)

def inv(x):
    one=(1,0)
    for a in range(M):
        for b in range(M):
            if mul(x,(a,b))==one:return (a,b)
    raise ValueError(x)

def powr(x,e):
    r=(1,0)
    while e:
        if e&1:r=mul(r,x)
        x=mul(x,x);e//=2
    return r

def norm_res(x):
    a,b=x
    return (a*a+a*b-b*b)%P

def unit(x):
    return norm_res(x)!=0

U=[(a,b) for a in range(M) for b in range(M) if unit((a,b))]
H={powr(x,7) for x in U}
print('units',len(U),'seventh_powers',len(H),'quotient',len(U)//len(H))

unseen=set(U); cosets=[]; index={}
while unseen:
    g=next(iter(unseen))
    C={mul(g,h) for h in H}
    i=len(cosets)
    for x in C:index[x]=i
    cosets.append(C);unseen-=C

w=(0,1)
print('w_coset',index[w])
rat=sorted({index[(a,0)] for a in range(M) if a%P})
print('rational_unit_cosets',rat,'count',len(rat),'contains_w',index[w] in rat)
for a in range(1,M):
    if a%P:
        print('rat',a,'coset',index[(a,0)])
print('w_representatives',sorted(cosets[index[w]])[:20])