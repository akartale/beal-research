#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "full/scripts"))
from trace_sieve_eta35 import count_fp, count_fp2, trace_poly, smooth

P=19
for t in (0,1):
    n1=count_fp(t,P)
    n2=count_fp2(t,P)
    s,prod,_,_=trace_poly(t,P)
    roots=[r for r in range(7) if (r*r-s*r+prod)%7==0]
    print('t',t,'smooth',smooth(t,P),'n1',n1,'n2',n2,'s_mod7',s%7,'prod_mod7',prod%7,'roots_mod7',roots)