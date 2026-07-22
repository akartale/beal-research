#!/usr/bin/env python3
from __future__ import annotations

# Arithmetic in (Z/nZ)[w]/(w^2-w-1).
def mul(x: tuple[int,int], y: tuple[int,int], n: int) -> tuple[int,int]:
    a,b=x; c,d=y
    # (a+bw)(c+dw)=ac+bd+(ad+bc+bd)w because w^2=w+1
    return ((a*c+b*d)%n,(a*d+b*c+b*d)%n)

def powr(x: tuple[int,int], e: int, n: int) -> tuple[int,int]:
    r=(1,0)
    while e:
        if e&1:r=mul(r,x,n)
        x=mul(x,x,n);e//=2
    return r

def roots7(target: tuple[int,int], n: int) -> list[tuple[int,int]]:
    return [(a,b) for a in range(n) for b in range(n) if powr((a,b),7,n)==target]

w=(0,1)
for n in (3,5,9,25,49):
    rr=roots7(w,n)
    print(n,len(rr),rr[:12])