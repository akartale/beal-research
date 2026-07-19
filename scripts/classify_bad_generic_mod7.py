#!/usr/bin/env python3
exec(open('research/beal/scripts/open_theoremA_level2025_all.py').read().split('import sys')[0])
for s in 'ehl':
 label=f'2.2.5.1-2025.1-{s}';P,E=parse_record(label)
 good=[];bad=[]
 for ell,(C1,C0,Coo) in local.items():
  a=E[ell];m1=minpoly_expr(P,a);b1=lcm(resabs(m1,q) for q in C1)
  (good if b1%7==0 or b1==0 else bad).append(ell)
 print(s,'generic-compatible',good)
 print(s,'generic-impossible',bad)
 print(s,'impossible residues mod105',sorted(set(q%105 for q in bad)))