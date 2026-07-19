#!/usr/bin/env python3
from math import gcd
for m in (49,343):
    counts={'A7':0,'B7':0,'both':0}
    examples={}
    for A in range(m):
        for B in range(m):
            if gcd(gcd(A,B),m)!=1:
                continue
            rhs=(A**3+B**5)%m
            for C in range(m):
                if (C**7-rhs)%m:
                    continue
                key='both' if A%7==0 and B%7==0 else ('A7' if A%7==0 else ('B7' if B%7==0 else None))
                if key:
                    counts[key]+=1
                    examples.setdefault(key,(A,B,C))
    print('modulus',m,'counts',counts,'examples',examples)