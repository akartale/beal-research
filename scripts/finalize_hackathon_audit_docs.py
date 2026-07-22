from pathlib import Path
root = Path(__file__).resolve().parents[1]

p = root / "CURRENT_PROOF_SNAPSHOT.md"
s = p.read_text()
if "LOGICAL_PROOF_AUDIT.md" not in s:
    s = s.replace("# Current Proof Snapshot — Signature `(3,5,7)`\n", "# Current Proof Snapshot — Signature `(3,5,7)`\n\n_Logical dependency and circularity audit: `LOGICAL_PROOF_AUDIT.md`._\n", 1)
    p.write_text(s)

p = root / "PROOF_ELEMENT_INDEX.md"
s = p.read_text()
if "LOGICAL_PROOF_AUDIT.md" not in s:
    s = s.replace("## Canonical status documents\n", "## Canonical status documents\n\n- `LOGICAL_PROOF_AUDIT.md` — canonical dependency, sufficiency, and circularity audit.\n", 1)
    p.write_text(s)

p = root / "PROJECT_STATUS.md"
s = p.read_text()
if "## Logical audit verdict" not in s:
    s += "\n\n## Logical audit verdict\n\nA proof-structure audit was run without repeating the large matrix calculations. The A–D dependency chain is acyclic after rejecting the level-`(2,2)` circular shortcut. Lemmas A, B, and C are closed in the current audit. Lemma D remains open at exactly the quadratic survivor `(90,0)`. See `LOGICAL_PROOF_AUDIT.md`.\n"
    p.write_text(s)

print("finalized")