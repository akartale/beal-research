from pathlib import Path

paths = [
    '/usr/bin/gcc','/usr/bin/cc','/usr/bin/clang','/usr/bin/ld','/usr/bin/as',
    '/usr/local/bin/gcc','/usr/local/bin/clang','/usr/local/swift/usr/bin/clang',
    '/opt/llvm/bin/clang','/usr/bin/zig','/usr/local/bin/zig',
    '/usr/include/aarch64-linux-gnu/pari/pari.h','/usr/include/pari/pari.h',
    '/usr/lib/aarch64-linux-gnu/libpari.so','/usr/lib/aarch64-linux-gnu/libpari-gmp-tls.so.8',
    '/usr/lib/libpari.so','/usr/local/lib/libpari.so'
]
out = Path('/workspace/research/beal/data/toolchain_path_probe.txt')
lines=[]
for p in paths:
    x=Path(p)
    lines.append(f'{p}: exists={x.exists()} file={x.is_file()} executable={bool(x.exists() and (x.stat().st_mode & 0o111))}')
out.write_text('\n'.join(lines))
print(out)