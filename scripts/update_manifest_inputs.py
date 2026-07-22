from pathlib import Path
p = Path(__file__).resolve().parent / "generate_stabilization_manifest.py"
s = p.read_text()
for anchor, item in [
    ('    "CURRENT_PROOF_SNAPSHOT.md",\n', '    "CURRENT_PROOF_SNAPSHOT.md",\n    "LOGICAL_PROOF_AUDIT.md",\n'),
    ('    "MANUSCRIPT_357_FROM_SCRATCH.md",\n', '    "MANUSCRIPT_357_FROM_SCRATCH.md",\n    "P7_FULL_PROOF_AUDIT.md",\n    "SIGNATURE_357_PROOF_STATUS.md",\n'),
]:
    if item.splitlines()[-1].strip().strip(',').strip('"') not in s:
        s = s.replace(anchor, item, 1)
p.write_text(s)
print("manifest inputs updated")