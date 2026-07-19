#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import math,re
from functools import reduce
import sympy as sp
from newform_bound_over_f import expression_minpoly, trace_power_expr, cyclotomic_inertia_degree, quadratic_inertia_degree, A as nf_a
x,e,y=sp.symbols('x e y')
DATA=Path('research/beal/upstream/GFE-5p3/Outputs/Data.txt').read_text()
def split_top(s,sep=','):
 out=[];start=0;depth=0
 for i,ch in enumerate(s):
  if ch in '[<(':depth+=1
  elif ch in ']>)':depth-=1
  elif ch==sep and depth==0:out.append(s[start:i].strip());start=i+1
 out.append(s[start:].strip());return out
def poly(s,var=x):return sp.Poly(sp.sympify(s.replace('^','**')),var,domain=sp.ZZ)
body=DATA[DATA.index('[')+1:DATA.rindex(']')];local={}
for ent in split_top(body):
 p=split_top(ent.strip()[1:-1]);ell=int(p[0]);sets=[]
 for q in p[1:]:
  q=q.strip()[1:-1];sets.append([poly(z) for z in split_top(q)] if q else [])
 local[ell]=sets
def parse_record(label):
 txt=Path(f'research/beal/data/lmfdb/level_2025/{label}.sage').read_text()
 pm=re.search(r'primes_array\s*=\s*\[(.*?)\]\nprimes\s*=',txt,re.S)
 primes=[(int(a),int(b)) for a,b in re.findall(r'\[\s*(\d+)\s*,\s*(\d+)\s*,',pm.group(1))]
 hm=re.search(r'heckePol\s*=\s*(.*?)\nK\.<e>',txt)
 P=sp.Poly((sp.sympify(hm.group(1).replace('^','**')).subs(x,e)) if hm else e,e,domain=sp.QQ)
 vm=re.search(r'hecke_eigenvalues_array\s*=\s*\[(.*?)\]\nhecke_eigenvalues',txt,re.S)
 vals=[sp.sympify(v.strip().replace('^','**')) for v in split_top(vm.group(1).replace('\\\n','')) if v.strip()]
 ans={}
 for (_,ell),v in zip(primes,vals):
  if ell not in ans:ans[ell]=v
 return P,ans
def minpoly_expr(P,expr):
 field_poly=sp.Poly(P.as_expr().subs(e,nf_a),nf_a,domain=sp.QQ)
 field_expr=sp.sympify(expr).subs(e,nf_a)
 return expression_minpoly(field_poly,field_expr,generator=nf_a,output=x)
def resabs(a,b):return abs(int(sp.resultant(a.as_expr(),b.as_expr(),x)))
def lcm(v):return reduce(math.lcm,(abs(int(z)) for z in v),1)
def gcd(v):return reduce(math.gcd,(abs(int(z)) for z in v),0)
def norm_shift(mp,c):return abs(int(mp.eval(c)))
def bound(label):
 P,E=parse_record(label);per=[]
 for ell,(C1,C0,Coo) in local.items():
  a=E[ell];m1=minpoly_expr(P,a);b1=lcm(resabs(m1,q) for q in C1)
  fK=quadratic_inertia_degree(ell,5);fF=cyclotomic_inertia_degree(ell,15)
  if fF%fK: raise ArithmeticError(f'incompatible inertia degrees at {ell}')
  ae=trace_power_expr(a,fF//fK,ell**fK)
  m2=minpoly_expr(P,ae);b2=lcm([resabs(m2,q) for q in C0]+[ell]);b3=lcm([resabs(m2,q) for q in Coo]+[ell])
  b4=lcm([norm_shift(m1,ell+1),norm_shift(m1,-ell-1)])
  per.append(lcm([b1,b2,b3,b4]))
 G=gcd(per);return G,list(sp.factorint(G).keys()) if G else []
import sys
rows=[]
for suffix in (sys.argv[1] if len(sys.argv)>1 else 'abcdefghijklmn'):
 label=f'2.2.5.1-2025.1-{suffix}';G,ps=bound(label)
 row=f'{suffix} {G} {ps}';rows.append(row);print(row,flush=True)
Path('research/beal/data/open_theoremA_level2025_all.out').write_text('\\n'.join(rows)+'\\n')