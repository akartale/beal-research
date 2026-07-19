#!/usr/bin/env python3
import json, urllib.parse, urllib.request

BASE='https://www.lmfdb.org/api/hmf_forms/'
levels=[2025,10125,18225,91125]
expected={2025:(14,45),10125:(35,225),18225:(111,405),91125:(112,2025)}

def fetch(level):
    params={'field_label':'2.2.5.1','level_norm':level,'_format':'json','_limit':1000}
    url=BASE+'?'+urllib.parse.urlencode(params)
    with urllib.request.urlopen(url,timeout=120) as r:
        return json.load(r)['data']

for level in levels:
    rows=fetch(level)
    dims=sum(int(r['dimension']) for r in rows)
    print(level, 'orbits=',len(rows),'sum_dimensions=',dims)
    print('labels=', [r['label'] for r in rows])
    eo,ed=expected[level]
    print('expected_orbits=',eo,'expected_space_dimension=',ed)