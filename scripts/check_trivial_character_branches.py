#!/usr/bin/env python3
from pathlib import Path
from generate_lemmaD_union_all_split_gp import entries

def ev(expr,x,p=7):
    return eval(expr.replace('^','**'),{'__builtins__':{}},{'x':x})%p

data=Path('upstream/GFE-5p3/Outputs/Data.txt').read_text()
for ell,f in entries(data):
    if ell in (3,5,7) or ell%5 not in (1,4):
        continue
    target=(ell+1)%7
    hits=[]
    for name,idx in [('generic',1),('t0',2),('tinf',3)]:
        polys=f[idx].strip()[1:-1]
        arr=[] if not polys.strip() else [z.strip() for z in polys.split(',')]
        if any(ev(q,target)==0 for q in arr): hits.append(name)
    hits.append('t1')
    print(ell,target,hits)