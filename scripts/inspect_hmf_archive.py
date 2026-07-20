#!/usr/bin/env python3
from __future__ import annotations
import gzip, io, re, urllib.request

UA={"User-Agent":"beal-357-research/1.0"}
BASE="https://jvoight.github.io/hmf"

def get(url: str) -> bytes:
    req=urllib.request.Request(url,headers=UA)
    with urllib.request.urlopen(req,timeout=60) as r:
        return r.read()

levels=get(f"{BASE}/ModFrmHilDatav1.1gz/levels.dat").decode("utf-8","replace")
print("LEVELS_MATCHES")
for line in levels.splitlines():
    if re.search(r"(^|\D)5(\D|$)|0005",line):
        print(line)

raw=get(f"{BASE}/ModFrmHilDatav1gz/2/data_2_0005.gz")
text=gzip.GzipFile(fileobj=io.BytesIO(raw)).read().decode("utf-8","replace")
print("ARCHIVE_BYTES",len(raw),"TEXT_CHARS",len(text))
print("HAS_10125", "10125" in text)
for pat in (r"10125", r"\[10125,", r"NEWFORMS", r"PRIMES"):
    print("PATTERN",pat,"COUNT",len(re.findall(pat,text)))
if "10125" in text:
    pos=text.find("10125")
    print("CONTEXT")
    print(text[max(0,pos-500):pos+3000])
else:
    print("TAIL")
    print(text[-3000:])