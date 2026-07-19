from pathlib import Path
p=Path('research/beal/scripts/p7_reducible_sieve.py')
s=p.read_text()
s=s.replace("Path('research/beal/p7_rayclass_coords.csv')","Path('research/beal/p7_rayclass_coords_full.csv')")
s=s.replace("l,e1,e2,n=line.split(',');d[int(l)]=(int(e1),int(e2),int(n))","l,e1,e2,e3,n=line.split(',');d[int(l)]=(int(e1),int(e2),int(e3),int(n))")
s=s.replace("alive={(k1,k2) for k1 in range(0,48,4) for k2 in (0,24)}","alive={(k1,k2,k3) for k1 in range(0,48,2) for k2 in range(0,48,4) for k3 in (0,24)}")
s=s.replace("e1,e2,n=co[l]","e1,e2,e3,n=co[l]")
s=s.replace("for k1,k2 in alive:\n   chi=pw(G,(k1*e1+k2*e2)%48);tr=add(chi,mul((n%7,0),pw(chi,47)))\n   if tr in F:nxt.add((k1,k2))","for k1,k2,k3 in alive:\n   chi=pw(G,(k1*e1+k2*e2+k3*e3)%48);tr=add(chi,mul((n%7,0),pw(chi,47)))\n   if tr in F:nxt.add((k1,k2,k3))")
Path('research/beal/scripts/p7_reducible_sieve_full.py').write_text(s)