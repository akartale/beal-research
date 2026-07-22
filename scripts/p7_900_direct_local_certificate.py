#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

P = 7
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "upstream/GFE-5p3/Outputs/Data.txt"
CHARS = ROOT / "data/p7_900_character_aux.txt"
OUT = ROOT / "data/p7_900_direct_local_certificate.json"


def split_polys(s: str) -> list[str]:
    return [x.strip() for x in s.split(',') if x.strip()]


def coeffs(poly: str) -> tuple[int,int,int]:
    s = poly.replace(' ', '')
    a2=a1=a0=0
    s = s.replace('-', '+-')
    if s.startswith('+-'):
        s=s[1:]
    for term in s.split('+'):
        if not term:
            continue
        if 'x^2' in term:
            c=term.replace('*x^2','').replace('x^2','')
            a2 += -1 if c=='-' else (1 if c in ('','+') else int(c))
        elif 'x' in term:
            c=term.replace('*x','').replace('x','')
            a1 += -1 if c=='-' else (1 if c in ('','+') else int(c))
        else:
            a0 += int(term)
    if a2==0:
        if a1==0:
            raise ValueError(poly)
        inv=pow(a1 % P,-1,P)
        return (0,1,(a0*inv)%P)
    inv=pow(a2 % P,-1,P)
    return (1,(a1*inv)%P,(a0*inv)%P)


def compatible(poly: str, t1: int, t2: int) -> bool:
    d,b,c=coeffs(poly)
    if d==0:
        root=(-c)%P
        return t1==t2==root
    return b%P == (-(t1+t2))%P and c%P == (t1*t2)%P


def main() -> None:
    chars={}
    for line in CHARS.read_text().splitlines():
        q,s1,s2=map(int,line.split())
        chars[q]=(s1,s2)
    text=DATA.read_text()
    pat=re.compile(r'<(\d+),\[(.*?)\],\[(.*?)\],\[(.*?)\]>',re.S)
    rows=[]
    eliminators=[]
    for m in pat.finditer(text):
        q=int(m.group(1))
        if q not in chars:
            continue
        signs=chars[q]
        targets=tuple((s*(1+q))%P for s in signs)
        groups={
            'generic':split_polys(m.group(2)),
            'degenerate0':split_polys(m.group(3)),
            'degenerateoo':split_polys(m.group(4)),
        }
        matches={name:[f for f in polys if compatible(f,*targets)] for name,polys in groups.items()}
        eliminated=not any(matches.values())
        row={'q':q,'signs':list(signs),'targets':list(targets),'matches':matches,'eliminated':eliminated,
             'candidate_counts':{k:len(v) for k,v in groups.items()}}
        rows.append(row)
        if eliminated:
            eliminators.append(q)
        print(q,targets,{k:len(v) for k,v in matches.items()},'ELIM' if eliminated else '')
    result={'residual_prime':7,'character':'(90,0)','tested_primes':len(rows),'eliminating_primes':eliminators,'rows':rows}
    OUT.write_text(json.dumps(result,indent=2)+'\n')
    print('eliminating_primes',eliminators)
    print('certificate',OUT)
    if not eliminators:
        raise SystemExit(1)

if __name__=='__main__':
    main()