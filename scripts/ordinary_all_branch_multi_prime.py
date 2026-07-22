#!/usr/bin/env python3
from pathlib import Path
import re
import sympy as sp
import galois

PRIMES=[11,19,29,31,41,59,61,71,79,89]
COORDS={
11:((77,0),(167,0)),19:((141,1),(141,1)),29:((44,1),(134,1)),
31:((106,0),(106,0)),41:((163,0),(73,0)),59:((58,1),(148,1)),
61:((92,0),(92,0)),71:((39,0),(129,0)),79:((179,1),(179,1)),
89:((132,1),(42,1))}
x=sp.symbols('x')

def split_top(s,sep=','):
 out=[];start=0;depth=0
 for i,ch in enumerate(s):
  if ch in '[<(': depth+=1
  elif ch in ']>)': depth-=1
  elif ch==sep and depth==0: out.append(s[start:i].strip());start=i+1
 out.append(s[start:].strip());return out

def parse_data():
 s=Path('research/beal/upstream/GFE-5p3/Outputs/Data.txt').read_text()
 body=s[s.index('[')+1:s.rindex(']')]; out={}
 for ent in split_top(body):
  p=split_top(ent.strip()[1:-1]); ell=int(p[0]); sets=[]
  for q in p[1:]:
   q=q.strip()[1:-1]
   sets.append([sp.Poly(sp.sympify(z.replace('^','**')),x,domain=sp.ZZ) for z in split_top(q)] if q else [])
  out[ell]=sets
 return out

def ord_mod(a,n):
 z=1
 for k in range(1,100):
  z=z*a%n
  if z==1:return k
 raise RuntimeError

def roots(poly,GF):
 coeff=[GF(int(c)%7) for c in poly.all_coeffs()]
 return list(galois.Poly(coeff,field=GF).roots())

def keypair(a,b):
 return tuple(sorted((int(a),int(b))))

def branch_sets(ell,sets,GF):
 C1,C0,Coo=sets
 generic=set()
 for p in C1:
  rr=roots(p,GF)
  if len(rr)==1: generic.add(keypair(rr[0],rr[0]))
  elif len(rr)==2: generic.add(keypair(rr[0],rr[1]))
 d=ord_mod(ell%15,15)
 r0={int(r) for p in C0 for r in roots(p,GF)}
 roo={int(r) for p in Coo for r in roots(p,GF)}
 return generic,r0,roo,d

def main():
 data=parse_data(); GF=galois.GF(7**12); g=GF.primitive_element
 zeta=g**((GF.order-1)//180); minus=GF(6)
 alive={(u,v) for u in range(180) for v in range(2)}
 print('initial',len(alive))
 for ell in PRIMES:
  generic,r0,roo,d=branch_sets(ell,data[ell],GF); nxt=set(); counts={'generic':0,'t0':0,'too':0,'t1':0}
  for u,v in alive:
   trs=[]
   for e1,e2 in COORDS[ell]:
    chi=zeta**((u*e1)%180)*(minus**((v*e2)%2))
    trs.append(chi+GF(ell%7)/chi)
   okg=keypair(*trs) in generic
   if d==2: qtrs=[t*t-GF((2*ell)%7) for t in trs]
   else: qtrs=trs
   ok0=all(int(t) in r0 for t in qtrs)
   okoo=all(int(t) in roo for t in qtrs)
   target=GF((ell+1)%7); ok1=all(t==target or t==-target for t in trs)
   if okg or ok0 or okoo or ok1:
    nxt.add((u,v))
    counts['generic']+=int(okg);counts['t0']+=int(ok0);counts['too']+=int(okoo);counts['t1']+=int(ok1)
  alive=nxt
  print(ell,'survivors',len(alive),'branch_hits',counts,'chars',sorted(alive))
  if not alive:break
if __name__=='__main__':main()