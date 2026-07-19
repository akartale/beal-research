#!/usr/bin/env python3
"""Eliminate all F_49-valued ray-class characters unramified above 7 at l=19.

Field model: F_49 = F_7[w]/(w^2-w-1), primitive generator g=2w.
Ray class group for modulus p3^3 p5^3 infinity_1 infinity_2 is [180,2].
The prime above 19 has ray-class coordinates [141,1].
"""

def add(x,y): return ((x[0]+y[0])%7,(x[1]+y[1])%7)
def mul(x,y):
    a,b=x; c,d=y
    return ((a*c+b*d)%7,(a*d+b*c+b*d)%7)
def power(x,n):
    r=(1,0)
    while n:
        if n&1: r=mul(r,x)
        x=mul(x,x); n//=2
    return r

def roots_of_pairs(pairs):
    out=set()
    for s,p in pairs:
        for a in range(7):
            for b in range(7):
                r=(a,b)
                val=add(add(mul(r,r),((-s*a)%7,(-s*b)%7)),(p,0))
                if val==(0,0): out.add(r)
    return out

# Unique RM trace polynomials X^2-sX+p over F_7 arising from all nonsingular
# local Frey specializations at l=19 with A,B,C nonzero and A^3+B^5=C^7.
pairs=[(0,1),(0,4),(1,4),(1,6),(2,3),(3,1),(3,4),(3,5),(3,6),
       (4,1),(4,6),(5,2),(5,3),(5,5),(6,3)]
actual=roots_of_pairs(pairs)

g=(0,2)  # order 48
survivors=[]
rows=[]
for y1 in range(0,48,4):       # 180*y1=0 mod 48: 12 possibilities
    for y2 in (0,24):          # 2*y2=0 mod 48: 2 possibilities
        e=(141*y1+y2)%48
        chi=power(g,e)
        tr=add(chi,mul((19%7,0),power(chi,47)))
        ok=tr in actual
        rows.append((y1,y2,e,chi,tr,ok))
        if ok: survivors.append((y1,y2))

print(f"characters={len(rows)}")
print(f"actual_trace_values={len(actual)}")
print(f"survivors={survivors}")
assert len(rows)==24
assert survivors==[]
print("ELIMINATED: all 24 characters")