#!/usr/bin/env python3
from pathlib import Path
import json,re

base=Path('research/beal/data/lmfdb/level_2025')
manifest=json.loads((base/'manifest.json').read_text())
for row in manifest:
    text=Path(row['file']).read_text()
    m=re.search(r'hecke_eigenvalues_array\s*=\s*\[(.*?)\]\nhecke_eigenvalues',text,re.S)
    if not m:
        raise RuntimeError(row['label'])
    vals=[x.strip() for x in m.group(1).replace('\\\n','').split(',')]
    print(row['label'], 'dim=',row['dimension'],'CM=',row['is_CM'],'a_q19=',vals[5:7])