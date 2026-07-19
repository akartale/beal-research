#!/usr/bin/env python3
"""Download validated LMFDB Sage records for HMF newforms at level norm 2025."""
from pathlib import Path
import json, time, urllib.request

FIELD='2.2.5.1'; OUT=Path('research/beal/data/lmfdb/level_2025'); OUT.mkdir(parents=True,exist_ok=True)
API=f'https://www.lmfdb.org/api/hmf_forms/?field_label={FIELD}&level_norm=2025&_format=json&_limit=100'
with urllib.request.urlopen(API,timeout=120) as r: rows=json.load(r)['data']
manifest=[]; failed=[]
for row in rows:
    label=row['label']; path=OUT/f'{label}.sage'
    url=f'https://www.lmfdb.org/ModularForm/GL2/TotallyReal/{FIELD}/holomorphic/{label}/download/sage'
    valid=False
    if path.exists():
        text=path.read_text(errors='ignore')
        valid='hecke_eigenvalues_array' in text and not text.lstrip().startswith('<!doctype html>')
    if not valid:
        for attempt in range(3):
            try:
                req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 qOrchestra-research/1.0'})
                with urllib.request.urlopen(req,timeout=120) as r: text=r.read().decode('utf-8')
                if 'hecke_eigenvalues_array' in text and not text.lstrip().startswith('<!doctype html>'):
                    path.write_text(text); valid=True; break
            except Exception:
                pass
            time.sleep(5*(attempt+1))
    if not valid:
        failed.append(label)
        if path.exists() and path.read_text(errors='ignore').lstrip().startswith('<!doctype html>'): path.unlink()
    manifest.append({'label':label,'dimension':row['dimension'],'is_CM':row['is_CM'],'is_base_change':row['is_base_change'],'source':url,'file':str(path),'valid':valid})
    time.sleep(2)
(OUT/'manifest.json').write_text(json.dumps(manifest,indent=2))
print(f'valid={sum(x["valid"] for x in manifest)} total={len(manifest)}')
print('failed=',failed)