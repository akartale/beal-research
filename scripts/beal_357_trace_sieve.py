#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from typing import Dict, List, Tuple

def primes_up_to(n:int)->List[int]:
    s=[True]*(n+1)
    if n>=0:s[0]=False
    if n>=1:s[1]=False
    for p in range(2,int(n**0.5)+1):
        if s[p]:
            for k in range(p*p,n+1,p):s[k]=False
    return [i for i,v in enumerate(s) if v]

def legendre(a:int,p:int)->int:
    a%=p
    if a==0:return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

def nonsquare(p:int)->int:
    return next(d for d in range(2,p) if legendre(d,p)==-1)

def eval_f_fp(x:int,t:int,p:int)->int:
    return (5*pow(x,6,p)-12*pow(x,5,p)+10*t*pow(x,3,p)+t*t)%p

def count_fp(t:int,p:int)->int:
    affine=p+sum(legendre(eval_f_fp(x,t,p),p) for x in range(p))
    infinity=2 if legendre(5,p)==1 else 0
    return affine+infinity

def mul(u:Tuple[int,int],v:Tuple[int,int],d:int,p:int)->Tuple[int,int]:
    a,b=u;c,e=v
    return ((a*c+b*e*d)%p,(a*e+b*c)%p)

def add(u,v,p):return ((u[0]+v[0])%p,(u[1]+v[1])%p)
def scale(k,u,p):return (k*u[0]%p,k*u[1]%p)

def eval_f_fp2(x:Tuple[int,int],t:int,d:int,p:int)->Tuple[int,int]:
    x2=mul(x,x,d,p);x3=mul(x2,x,d,p)
    x5=mul(mul(x3,x,d,p),x,d,p);x6=mul(x3,x3,d,p)
    r=add(scale(5,x6,p),scale(-12,x5,p),p)
    r=add(r,scale(10*t,x3,p),p)
    return add(r,(t*t%p,0),p)

def chi_fp2(z:Tuple[int,int],d:int,p:int)->int:
    if z==(0,0):return 0
    norm=(z[0]*z[0]-d*z[1]*z[1])%p
    return legendre(norm,p)

def count_fp2(t:int,p:int)->int:
    d=nonsquare(p);q=p*p;total=q
    for a in range(p):
        for b in range(p):
            total+=chi_fp2(eval_f_fp2((a,b),t,d,p),d,p)
    return total+2

def trace_polynomial(t:int,p:int)->Dict[str,int]:
    n1=count_fp(t,p);n2=count_fp2(t,p)
    s1=p+1-n1
    e2=(n2-p*p-1+s1*s1)//2
    product=e2-2*p
    return {"t":t,"N1":n1,"N2":n2,"trace_sum":s1,"trace_product":product,
            "poly":[1,-s1,product]}

def local_t_values(p:int)->List[int]:
    vals=set()
    seventh={pow(c,7,p) for c in range(1,p)}
    for A in range(1,p):
        a3=pow(A,3,p);inv=pow(a3,-1,p)
        for B in range(1,p):
            if (a3+pow(B,5,p))%p in seventh:
                vals.add((-pow(B,5,p)*inv)%p)
    return sorted(vals)

def analyze_prime(p:int)->Dict[str,object]:
    ts=local_t_values(p)
    unique={}
    for t in ts:
        if t in (0,1):continue
        row=trace_polynomial(t,p)
        key=tuple(row["poly"])
        unique.setdefault(key,[]).append(t)
    return {"prime":p,"local_t_count":len(ts),"t_values":ts,
            "trace_polynomials":[{"poly":list(k),"t_values":v} for k,v in sorted(unique.items())]}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--prime",type=int)
    ap.add_argument("--prime-bound",type=int,default=43)
    ap.add_argument("--output",default="-")
    ns=ap.parse_args()
    ps=[ns.prime] if ns.prime else [p for p in primes_up_to(ns.prime_bound) if p not in (2,3,5,7)]
    report={"signature":[3,5,7],"residual_prime":7,
            "model":"y^2=5x^6-12x^5+10t*x^3+t^2, t=-B^5/A^3",
            "primes":[analyze_prime(p) for p in ps]}
    text=json.dumps(report,indent=2)
    if ns.output=="-":print(text)
    else:Path(ns.output).write_text(text+"\n",encoding="utf-8")

if __name__=="__main__":main()