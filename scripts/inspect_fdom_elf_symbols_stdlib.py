from pathlib import Path
import struct

libpath = Path('/workspace/research/beal/vendor/fdom-upstream/libfdom-2-15-2.so')
out = Path('/workspace/research/beal/data/fdom_elf_symbol_probe_stdlib.txt')
targets = {
    'afuchmakefdom', 'afuchword', 'normbasis', 'minimalcycles_bytype',
    'presentation', 'signature', 'elliptic', 'afuchfdom_worker',
    'afuchfdom_subgroup', 'afuchmakefdom_fromelts', 'afuchminimalcycles'
}

data = libpath.read_bytes()
if data[:4] != b'\x7fELF':
    raise SystemExit('not ELF')
klass, endian = data[4], data[5]
if klass != 2:
    raise SystemExit(f'unsupported ELF class {klass}')
prefix = '<' if endian == 1 else '>'
# ELF64 header after e_ident.
hdr = struct.unpack_from(prefix + 'HHIQQQIHHHHHH', data, 16)
(_, _, _, _, _, e_shoff, _, _, _, _, e_shentsize, e_shnum, e_shstrndx) = hdr
sections = []
for i in range(e_shnum):
    off = e_shoff + i * e_shentsize
    sh = struct.unpack_from(prefix + 'IIQQQQIIQQ', data, off)
    sections.append({
        'name_off': sh[0], 'type': sh[1], 'flags': sh[2], 'addr': sh[3],
        'offset': sh[4], 'size': sh[5], 'link': sh[6], 'info': sh[7],
        'align': sh[8], 'entsize': sh[9],
    })
shstr = sections[e_shstrndx]
shstr_data = data[shstr['offset']:shstr['offset']+shstr['size']]

def cstr(buf, pos):
    end = buf.find(b'\0', pos)
    if end < 0:
        end = len(buf)
    return buf[pos:end].decode('utf-8', 'replace')

for s in sections:
    s['name'] = cstr(shstr_data, s['name_off'])

found = set()
lines = [f'ELF64_ENDIAN={"LE" if endian == 1 else "BE"}', f'SECTIONS={len(sections)}']
for sec in sections:
    if sec['name'] not in ('.dynsym', '.symtab'):
        continue
    strsec = sections[sec['link']]
    strtab = data[strsec['offset']:strsec['offset']+strsec['size']]
    entsize = sec['entsize'] or 24
    count = sec['size'] // entsize
    lines.append(f'{sec["name"]}=PRESENT COUNT={count}')
    for i in range(count):
        off = sec['offset'] + i * entsize
        st_name, st_info, st_other, st_shndx, st_value, st_size = struct.unpack_from(prefix + 'IBBHQQ', data, off)
        name = cstr(strtab, st_name) if st_name else ''
        if name in targets:
            found.add(name)
            bind = st_info >> 4
            typ = st_info & 0x0F
            lines.append(f'{sec["name"]}:{name}:bind={bind}:type={typ}:shndx={st_shndx}:size={st_size}')
for name in sorted(targets):
    lines.append(f'{name}={"FOUND" if name in found else "NOT_FOUND"}')
out.write_text('\n'.join(lines))
print(out)