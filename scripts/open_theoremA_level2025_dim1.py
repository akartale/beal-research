#!/usr/bin/env python3
"""Open reproduction of TheoremA for six rational-coefficient level-2025 orbits."""
from __future__ import annotations
from pathlib import Path
import math,re
from functools import reduce
import sympy as sp
x=sp.symbols('x')
DATA=Path('research/beal/upstream/GFE-5p3/Outputs/Data.txt').read_text()

def split_top(s,sep=','):
 out=[];start=0;depth=0
 for i,ch in enumerate(s):
  if ch in '[<(':depth+=1
  elif ch in ']>)':depth-=1
  elif ch==sep and depth==0:out.append(s[start:i].strip());start=i+1
 out.append(s[start:].strip());return out

def parse_poly(s):return sp.Poly(sp.sympify(s.replace('^','**')),x,domain=sp.ZZ)
body=DATA[DATA.index('[')+1:DATA.rindex(']')];local={}
for ent in split_top(body):
 parts=split_top(ent.strip()[1:-1]);ell=int(parts[0]);sets=[]
 for q in parts[1:]:
  q=q.strip()[1:-1];sets.append([parse_poly(z) for z in split_top(q)] if q else [])
 local[ell]=sets

def sage_arrays(label):
 txt=Path(f'research/beal/data/lmfdb/level_2025/{label}.sage').read_text()
 pm=re.search(r'primes_array\s*=\s*\[(.*?)\]\nprimes\s*=',txt,re.S)
 vm=re.search(r'hecke_eigenvalues_array\s*=\s*\[(.*?)\]\nhecke_eigenvalues',txt,re.S)
 primes=[]
 for a,b in re.findall(r'\[\s*(\d+)\s*,\s*(\d+)\s*,',pm.group(1)):
  primes.append((int(a),int(b)))
 vals=[int(v.strip()) for v in vm.group(1).replace('\\\n','').split(',') if v.strip()]
 return primes,vals

def first_prime_eigs(label):
 primes,vals=sage_arrays(label);ans={}
 for (_,ell),v in zip(primes,vals):
  if ell not in ans:ans[ell]=v
 return ans

def resultant_abs(p,q):return abs(int(sp.resultant(p.as_expr(),q.as_expr(),x)))
def lcm(vals):return reduce(math.lcm,(abs(int(v)) for v in vals),1)
def gcd(vals):return reduce(math.gcd,(abs(int(v)) for v in vals),0)
def ordmod(a,n):
 z=1
 for k in range(1,100):
  z=z*a%n
  if z==1:return k
 raise ValueError
def f2_K(l):return 1 if pow(5,(l-1)//2,l)==1 else 2

def bound_form(label):
 eigs=first_prime_eigs(label);per=[]
 for ell,(C1,C0,Coo) in local.items():
  a=eigs[ell];mp=sp.Poly(x-a,x)
  b1=lcm(resultant_abs(mp,p) for p in C1)
  ratio=ordmod(ell%15,15)//f2_K(ell)
  ae=a*a-2*(ell**f2_K(ell)) if ratio==2 else a
  mp2=sp.Poly(x-ae,x)
  b2=lcm([resultant_abs(mp2,p) for p in C0]+[ell])
  b3=lcm([resultant_abs(mp2,p) for p in Coo]+[ell])
  b4=lcm([abs(a-(ell+1)),abs(a+(ell+1))])
  per.append(lcm([b1,b2,b3,b4]))
 G=gcd(per);return G,list(sp.factorint(G).keys()) if G else []
for suffix in 'abcdef':
 label=f'2.2.5.1-2025.1-{suffix}';G,ps=bound_form(label)
 print(label,'gcd=',G,'primes=',ps)