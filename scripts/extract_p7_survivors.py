#!/usr/bin/env python3
import re
from pathlib import Path

text = Path('research/beal/upstream/GFE-5p3/Outputs/TheoremA.txt').read_text()
start = text.index('> time TheoremA(3,2,Data:flag := true);')
end = text.index('> time TheoremA(3,3,Data);')
block = text[start:end]

survivors = []
failed = []
for m in re.finditer(r'i = (\d+) of 111, small exponents after elimination = \[([^\]]*)\]', block, re.S):
    idx = int(m.group(1))
    exps = [int(x) for x in re.findall(r'\d+', m.group(2))]
    if 7 in exps:
        survivors.append(idx)
for m in re.finditer(r'i = (\d+) of 111 failed using', block):
    failed.append(int(m.group(1)))

all_survivors = sorted(set(survivors + failed))
print('p7_conditional_survivors=', survivors)
print('unconditionally_bad=', failed)
print('all_p7_survivors=', all_survivors)
assert survivors == [21,22,26,33,61,92,98]
assert failed == [65,78]
assert all_survivors == [21,22,26,33,61,65,78,92,98]