from pathlib import Path

libpath = Path('/workspace/research/beal/vendor/fdom-upstream/libfdom-2-15-2.so')
out = Path('/workspace/research/beal/data/fdom_elf_symbol_probe.txt')
names = {
    'afuchmakefdom', 'afuchword', 'normbasis', 'minimalcycles_bytype',
    'presentation', 'signature', 'elliptic', 'afuchfdom_worker',
    'afuchfdom_subgroup', 'afuchmakefdom_fromelts', 'afuchminimalcycles'
}
lines = []
try:
    from elftools.elf.elffile import ELFFile
    with libpath.open('rb') as fh:
        elf = ELFFile(fh)
        found = set()
        for secname in ('.dynsym', '.symtab'):
            sec = elf.get_section_by_name(secname)
            if sec is None:
                lines.append(f'{secname}=MISSING')
                continue
            lines.append(f'{secname}=PRESENT COUNT={sec.num_symbols()}')
            for sym in sec.iter_symbols():
                if sym.name in names:
                    found.add(sym.name)
                    lines.append(f'{secname}:{sym.name}:bind={sym.entry.st_info.bind}:type={sym.entry.st_info.type}:shndx={sym.entry.st_shndx}')
        for name in sorted(names):
            lines.append(f'{name}={"FOUND" if name in found else "NOT_FOUND"}')
except Exception as exc:
    lines.append(f'ERROR={type(exc).__name__}:{exc}')
out.write_text('\n'.join(lines))
print(out)