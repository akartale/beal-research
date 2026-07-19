from pathlib import Path
import os, platform, shutil, sys, urllib.request

out = Path('/workspace/research/beal/data/bootstrap_environment_probe.txt')
lines = [
    f'ARCH={platform.machine()}',
    f'PLATFORM={platform.platform()}',
    f'PYTHON={sys.version}',
]
for cmd in ['curl','wget','dpkg-deb','ar','tar','xz','zstd','make','gcc','cc','clang','gp']:
    lines.append(f'{cmd}={shutil.which(cmd)}')
for url in [
    'https://deb.debian.org/debian/dists/stable/Release',
    'https://pari.math.u-bordeaux.fr/pub/pari/unix/',
]:
    try:
        req = urllib.request.Request(url, headers={'User-Agent':'qOrchestra-bootstrap/1.0'})
        with urllib.request.urlopen(req, timeout=20) as r:
            data = r.read(256)
            lines.append(f'URL_OK={url} STATUS={getattr(r,"status",None)} PREFIX={data[:80]!r}')
    except Exception as exc:
        lines.append(f'URL_ERROR={url} {type(exc).__name__}:{exc}')
out.write_text('\n'.join(lines))
print(out)