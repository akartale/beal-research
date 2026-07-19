#!/usr/bin/env python3
exec(open('research/beal/scripts/open_theoremA_level2025_all.py').read().split('import sys')[0])
for s in 'ehl':
    P,E=parse_record(f'2.2.5.1-2025.1-{s}')
    print('FORM',s,'heckePol',P.as_expr())
    txt=Path(f'research/beal/data/lmfdb/level_2025/2.2.5.1-2025.1-{s}.sage').read_text()
    pm=re.search(r'primes_array\s*=\s*\[(.*?)\]\nprimes\s*=',txt,re.S)
    vm=re.search(r'hecke_eigenvalues_array\s*=\s*\[(.*?)\]\nhecke_eigenvalues',txt,re.S)
    ps=[(int(a),int(b)) for a,b in re.findall(r'\[\s*(\d+)\s*,\s*(\d+)\s*,',pm.group(1))]
    vs=[sp.sympify(v.strip().replace('^','**')) for v in split_top(vm.group(1).replace('\\\n','')) if v.strip()]
    by={}
    for (_,ell),v in zip(ps,vs): by.setdefault(ell,[]).append(v)
    for ell in [11,19,29,31,41,59,61,71,79]:
        if len(by.get(ell,[]))==2:
            a,b=by[ell]; print(ell,'vals',a,b,'sum',sp.rem(a+b,P.as_expr(),e),'prod',sp.rem(a*b,P.as_expr(),e))