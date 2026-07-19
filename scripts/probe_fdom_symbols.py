import ctypes
from pathlib import Path

libpath = Path('/workspace/research/beal/vendor/fdom-upstream/libfdom-2-15-2.so')
out = Path('/workspace/research/beal/data/fdom_symbol_probe.txt')
lib = ctypes.CDLL(str(libpath))
names = [
    'afuchmakefdom', 'afuchword', 'normbasis', 'minimalcycles_bytype',
    'presentation', 'signature', 'elliptic', 'afuchfdom_worker',
    'afuchfdom_subgroup', 'afuchmakefdom_fromelts', 'afuchminimalcycles'
]
lines=[]
for name in names:
    try:
        getattr(lib, name)
        lines.append(f'{name}=EXPORTED')
    except AttributeError:
        lines.append(f'{name}=NOT_EXPORTED')
out.write_text('\n'.join(lines))
print(out)