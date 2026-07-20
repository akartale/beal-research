#!/usr/bin/env python3
from __future__ import annotations
import base64, json, urllib.parse, urllib.request
UA={"User-Agent":"beal-357-research/1.0","Accept":"application/vnd.github+json"}
REPO="lucasvillagra/GFE-5p3"

def get(url:str):
    req=urllib.request.Request(url,headers=UA)
    with urllib.request.urlopen(req,timeout=60) as r:
        return json.load(r)

print("BRANCHES")
for b in get(f"https://api.github.com/repos/{REPO}/branches?per_page=100"):
    print(b['name'],b['commit']['sha'])
print("COMMITS TheoremA")
path="Outputs/TheoremA.txt"
commits=get(f"https://api.github.com/repos/{REPO}/commits?path={urllib.parse.quote(path)}&per_page=100")
for c in commits:
    sha=c['sha']; msg=c['commit']['message'].splitlines()[0]
    print(sha,msg)
    try:
        obj=get(f"https://api.github.com/repos/{REPO}/contents/{path}?ref={sha}")
        text=base64.b64decode(obj['content']).decode('utf-8','replace')
        print('  chars',len(text),'lines',text.count('\n')+1,'flag_true',text.count('flag := true'),'B23',text.count('The bound is 7'))
        if len(text)>5000:
            out=f"/tmp/TheoremA_{sha[:8]}.txt"
            open(out,'w',encoding='utf-8').write(text)
            print('  saved',out)
    except Exception as exc:
        print('  ERR',exc)
print("TAGS")
for t in get(f"https://api.github.com/repos/{REPO}/tags?per_page=100"):
    print(t['name'],t['commit']['sha'])