#!/usr/bin/env python3
from math import gcd
mods=[8,9,13,16,19,25,27,31,37,49,64,73,81,97,121,125,169,343]
for m in mods:
    seventh={pow(c,7,m) for c in range(m) if gcd(c,15)==1}
    counts={'A7':0,'B7':0}
    ex={}
    for A in range(m):
        if A%3: continue
        for B in range(m):
            if gcd(gcd(A,B),m)!=1: continue
            branch='A7' if A%7==0 and B%7 else ('B7' if B%7==0 and A%7 else None)
            if not branch: continue
            rhs=(pow(A,3,m)+pow(B,5,m))%m
            if rhs in seventh:
                counts[branch]+=1; ex.setdefault(branch,(A,B,rhs))
    print(m,counts,ex)