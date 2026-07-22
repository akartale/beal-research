#!/usr/bin/env python3
from __future__ import annotations

import pickle
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "data/hecke_mod7_cache.pkl"
with path.open("rb") as fh:
    obj = pickle.load(fh)

print("type", type(obj).__name__)
if hasattr(obj, "keys"):
    keys = list(obj.keys())
    print("key_count", len(keys))
    for key in keys[:200]:
        value = obj[key]
        size = len(value) if hasattr(value, "__len__") else ""
        print(repr(key), type(value).__name__, size)
else:
    print("length", len(obj) if hasattr(obj, "__len__") else "")