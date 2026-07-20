#!/usr/bin/env python3
from __future__ import annotations
import re, urllib.request

UA={"User-Agent":"beal-357-research/1.0"}
page="https://jvoight.github.io/hmf.html"
html=urllib.request.urlopen(urllib.request.Request(page,headers=UA),timeout=30).read().decode()
for href,text in re.findall(r"<a[^>]+href=['\"]([^'\"]+)['\"][^>]*>(.*?)</a>",html,re.S|re.I):
    clean=re.sub('<[^>]+>','',text).strip()
    if clean in {'0005','fields'} or '0005' in href or 'level' in href.lower():
        print(clean, href)