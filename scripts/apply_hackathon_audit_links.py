from pathlib import Path

root = Path(__file__).resolve().parents[1]

insertions = {
    "README.md": (
        "- `CURRENT_PROOF_SNAPSHOT.md` for the careful math version\n",
        "- `CURRENT_PROOF_SNAPSHOT.md` for the careful math version\n- `LOGICAL_PROOF_AUDIT.md` for the dependency, circularity, and sufficiency audit\n",
    ),
    "PROJECT_STATUS.md": (
        "This is the canonical high-level status for the hackathon cutoff. For the exact frozen mathematical state, read `CURRENT_PROOF_SNAPSHOT.md`.\n",
        "This is the canonical high-level status for the hackathon cutoff. For the exact frozen mathematical state, read `CURRENT_PROOF_SNAPSHOT.md`. For the proof-dependency and circularity audit, read `LOGICAL_PROOF_AUDIT.md`.\n",
    ),
    "DEMO.md": (
        "Open `CURRENT_PROOF_SNAPSHOT.md` and `LEMMAS_ABCD_REAUDIT.md`.\n",
        "Open `CURRENT_PROOF_SNAPSHOT.md`, `LOGICAL_PROOF_AUDIT.md`, and `LEMMAS_ABCD_REAUDIT.md`. The logical audit checks the proof chain without rerunning the large matrix computations.\n",
    ),
    "CURRENT_PROOF_SNAPSHOT.md": (
        "This file is the canonical frozen statement of what is proved, what is computationally certified, and what remains open at the submission cutoff. It supersedes stale progress language in older notes. Historical files remain evidence of the research process but must not be used as current status unless referenced here.\n",
        "This file is the canonical frozen statement of what is proved, what is computationally certified, and what remains open at the submission cutoff. It supersedes stale progress language in older notes. Historical files remain evidence of the research process but must not be used as current status unless referenced here. The dependency, sufficiency, and circularity audit is `LOGICAL_PROOF_AUDIT.md`.\n",
    ),
    "PROOF_ELEMENT_INDEX.md": (
        "## Canonical status documents\n",
        "## Canonical status documents\n\n`LOGICAL_PROOF_AUDIT.md` is the canonical dependency/circularity audit for Lemmas A–D and the post-irreducibility chain.\n",
    ),
}

for name, (anchor, replacement) in insertions.items():
    p = root / name
    s = p.read_text()
    if "LOGICAL_PROOF_AUDIT.md" in s:
        continue
    if anchor not in s:
        raise SystemExit(f"anchor not found in {name}")
    p.write_text(s.replace(anchor, replacement, 1))

print("hackathon audit links synchronized")