from pathlib import Path

BASE = Path('/workspace/research/beal/data')
FILES = [
    'fdom_level35721_init.txt',
    'fdom_level35721_tuned.txt',
    'fdom_level35721_full.txt',
    'fdom_presentation_h1_35721.txt',
]
OUT = BASE / 'fdom_dump_inspection.txt'
markers = [
    'X=', 'XX=', 'FDOM=', 'ELTS=', 'SIDES=', 'VERTICES=', 'ACTIONS=',
    'PRESENTATION=', 'SIGNATURE=', 'GENUS=', 'H1_', 'SPAIR=', 'ELLIPTIC='
]
lines = []
for name in FILES:
    p = BASE / name
    data = p.read_text(errors='replace')
    lines.append(f'FILE={name} BYTES={len(data.encode())} CHARS={len(data)} LINES={data.count(chr(10))+1}')
    lines.append('PREFIX=' + repr(data[:500]))
    for marker in markers:
        positions = []
        start = 0
        while len(positions) < 10:
            i = data.find(marker, start)
            if i < 0:
                break
            positions.append(i)
            start = i + 1
        if positions:
            lines.append(f'{marker} POSITIONS={positions}')
            for i in positions[:3]:
                lines.append(f'  SNIP[{i}]={repr(data[max(0,i-80):i+240])}')
    lines.append('')
OUT.write_text('\n'.join(lines))
print(OUT)