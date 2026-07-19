#!/usr/bin/env python3
from pathlib import Path
import re
for s in 'ehl':
    t=Path(f'research/beal/data/lmfdb/level_2025/2.2.5.1-2025.1-{s}.sage').read_text()
    pm=re.search(r'primes_array\s*=\s*\[(.*?)\]\nprimes\s*=',t,re.S)
    vm=re.search(r'hecke_eigenvalues_array\s*=\s*\[(.*?)\]\nhecke_eigenvalues',t,re.S)
    primes=[(int(a),int(b)) for a,b in re.findall(r'\[\s*(\d+)\s*,\s*(\d+)\s*,',pm.group(1))]
    vals=[v.strip() for v in vm.group(1).replace('\\\n','').split(',')]
    print(s,[(p,v) for p,v in zip(primes,vals) if p[0]==49])