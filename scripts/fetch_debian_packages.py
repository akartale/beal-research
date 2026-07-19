from pathlib import Path
import hashlib, lzma, re, sys, urllib.request

BASE = Path('/workspace/research/beal/toolchain')
DEBS = BASE / 'debs'
META = BASE / 'metadata'
for p in (DEBS, META):
    p.mkdir(parents=True, exist_ok=True)
MIRROR = 'https://deb.debian.org/debian'
suite = 'bookworm'
args = list(sys.argv[1:])
if args and args[0].startswith('--suite='):
    suite = args.pop(0).split('=', 1)[1]
INDEX = META / f'Packages-{suite}.xz'
if not INDEX.exists():
    urllib.request.urlretrieve(MIRROR + f'/dists/{suite}/main/binary-arm64/Packages.xz', INDEX)
text = lzma.decompress(INDEX.read_bytes()).decode('utf-8', 'replace')
entries = {}
for block in text.split('\n\n'):
    fields = {}
    key = None
    for line in block.splitlines():
        if not line:
            continue
        if line[0].isspace() and key:
            fields[key] += '\n' + line[1:]
        elif ': ' in line:
            key, val = line.split(': ', 1)
            fields[key] = val
    if 'Package' in fields:
        entries[fields['Package']] = fields

def dep_names(dep):
    out = []
    for group in dep.split(','):
        first = group.strip().split('|')[0].strip()
        name = re.split(r'\s|:', first, 1)[0]
        if name and not name.startswith('${'):
            out.append(name)
    return out

requested = args or ['pari-gp', 'libpari-gmp-tls8']
resolved, seen = [], set()
def add(pkg):
    if pkg in seen:
        return
    seen.add(pkg)
    f = entries.get(pkg)
    if not f:
        return
    for k in ('Pre-Depends', 'Depends'):
        if k in f:
            for dep in dep_names(f[k]):
                if dep not in {'libc6','libgcc-s1','libstdc++6','zlib1g'}:
                    add(dep)
    resolved.append(pkg)
for pkg in requested:
    add(pkg)
lines = []
for pkg in resolved:
    f = entries[pkg]
    deb = DEBS / Path(f['Filename']).name
    if not deb.exists():
        urllib.request.urlretrieve(MIRROR + '/' + f['Filename'], deb)
    got = hashlib.sha256(deb.read_bytes()).hexdigest()
    if got != f['SHA256']:
        raise RuntimeError(f'SHA256 mismatch for {pkg}')
    lines.append(f"{pkg}\t{f.get('Version')}\t{deb}\t{f.get('Depends','')}")
(META / f'fetched-{suite}.txt').write_text('\n'.join(lines))
print('\n'.join(lines))