from pathlib import Path
import io, lzma, gzip, tarfile

DEBS = Path('/workspace/research/beal/toolchain/debs')
ROOT = Path('/workspace/research/beal/toolchain/root')
ROOT.mkdir(parents=True, exist_ok=True)
LOG = Path('/workspace/research/beal/toolchain/metadata/extracted-bookworm.txt')

def ar_members(blob: bytes):
    if not blob.startswith(b'!<arch>\n'):
        raise ValueError('not an ar archive')
    pos = 8
    while pos + 60 <= len(blob):
        hdr = blob[pos:pos+60]
        pos += 60
        name = hdr[:16].decode('ascii', 'replace').strip().rstrip('/')
        size = int(hdr[48:58].decode('ascii').strip())
        data = blob[pos:pos+size]
        pos += size + (size & 1)
        yield name, data

def extract_deb(path: Path):
    members = dict(ar_members(path.read_bytes()))
    data_name = next((n for n in members if n.startswith('data.tar')), None)
    if data_name is None:
        raise ValueError(f'no data.tar member in {path.name}')
    payload = members[data_name]
    if data_name.endswith('.xz'):
        payload = lzma.decompress(payload)
        mode = 'r:'
    elif data_name.endswith('.gz'):
        payload = gzip.decompress(payload)
        mode = 'r:'
    elif data_name.endswith('.tar'):
        mode = 'r:'
    else:
        raise ValueError(f'unsupported compression {data_name}')
    with tarfile.open(fileobj=io.BytesIO(payload), mode=mode) as tf:
        for member in tf.getmembers():
            target = (ROOT / member.name).resolve()
            if not str(target).startswith(str(ROOT.resolve()) + '/') and target != ROOT.resolve():
                raise ValueError(f'unsafe path {member.name}')
        tf.extractall(ROOT)
    return data_name

lines = []
for deb in sorted(DEBS.glob('*.deb')):
    # Extract only Bookworm packages selected by fetched-bookworm metadata.
    metadata = Path('/workspace/research/beal/toolchain/metadata/fetched-bookworm.txt').read_text()
    if deb.name not in metadata:
        continue
    member = extract_deb(deb)
    lines.append(f'{deb.name}\t{member}\t{deb.stat().st_size}')
LOG.write_text('\n'.join(lines))
print(f'extracted={len(lines)} root={ROOT}')