#!/usr/bin/env python3
from __future__ import annotations
import json, urllib.request
UA={"User-Agent":"beal-357-research/1.0","Accept":"application/vnd.github+json"}

def get_json(url:str):
    req=urllib.request.Request(url,headers=UA)
    with urllib.request.urlopen(req,timeout=60) as r:
        return json.load(r)

repos=[]
page=1
while True:
    batch=get_json(f"https://api.github.com/users/jvoight/repos?per_page=100&page={page}")
    if not batch: break
    repos.extend(batch); page+=1
for repo in repos:
    name=repo['name']
    if 'github' in name.lower() or 'hmf' in name.lower() or 'hilbert' in name.lower():
        print('REPO',name,repo['html_url'],repo.get('default_branch'))
        try:
            tree=get_json(f"https://api.github.com/repos/jvoight/{name}/git/trees/{repo.get('default_branch','master')}?recursive=1")
            for item in tree.get('tree',[]):
                p=item.get('path','')
                if 'data_2_0005' in p or p.endswith('hmf.html') or 'levels.dat' in p:
                    print('FILE',p,item.get('url'))
        except Exception as exc:
            print('ERR',name,exc)