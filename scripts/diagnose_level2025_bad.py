#!/usr/bin/env python3
exec(open('research/beal/scripts/open_theoremA_level2025_all.py').read().split('import sys')[0])
for s in 'ehl':
 label=f'2.2.5.1-2025.1-{s}';P,E=parse_record(label)
 print('\nFORM',s)
 for ell,(C1,C0,Coo) in local.items():
  a=E[ell];m1=minpoly_expr(P,a);b1=lcm(resabs(m1,q) for q in C1)
  ratio=ordmod(ell%15,15)//f2(ell);ae=a*a-2*(ell**f2(ell)) if ratio==2 else a
  m2=minpoly_expr(P,ae);b2=lcm([resabs(m2,q) for q in C0]+[ell]);b3=lcm([resabs(m2,q) for q in Coo]+[ell])
  b4=lcm([norm_shift(m1,ell+1),norm_shift(m1,-ell-1)])
  vals=[b1,b2,b3,b4]
  print(ell, ['ZERO' if z==0 else ('7' if z%7==0 else '-') for z in vals], vals)