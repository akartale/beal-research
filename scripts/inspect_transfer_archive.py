from pathlib import Path
import tarfile

arc = Path('/workspace/research/beal/beal_fdom_transfer.tgz')
out = Path('/workspace/research/beal/data/beal_transfer_archive_contents.txt')
lines=[f'ARCHIVE_EXISTS={arc.exists()} SIZE={arc.stat().st_size if arc.exists() else 0}']
if arc.exists():
    with tarfile.open(arc, 'r:gz') as tf:
        members=tf.getmembers()
        lines.append(f'MEMBERS={len(members)}')
        keys=('gp','pari','libfdom','fdom.c','fdom.o','Makefile','bin/','lib/')
        for m in members:
            name=m.name
            low=name.lower()
            if any(k.lower() in low for k in keys):
                lines.append(f'{name}\t{m.size}\t{oct(m.mode)}\t{"file" if m.isfile() else "dir" if m.isdir() else "other"}')
out.write_text('\n'.join(lines))
print(out)