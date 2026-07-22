from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]

p = root / "LEMMA_A_B_LOCAL_PROOF_DRAFT.md"
s = p.read_text()
pattern = re.compile(
    r"Lemma A's finite-flat Jordan--Hoelder passage is now closed.*?Accordingly, absolute irreducibility is not claimed here as theorem-level complete\.\n?",
    re.S,
)
new = """Lemma A's finite-flat Jordan--Hoelder passage is closed by the exact statement of Raynaud Corollaire 3.4.4. The branchwise source conductor table has now been verified under `(a,b,c)=(B,-C,A)` in `PRIMITIVE_VALUATION_CONDUCTOR_TABLE.md`; therefore Lemma B is also closed in the current audit.\n\n`LEMMA_C_D_ABSOLUTE_CHARACTERS_AND_L19.md` proves only the good-reduction part of Lemma D at `19`; it must not be cited as a complete proof of the ordinary branch. The full four-branch sieve and the separately audited toric and conductor arguments reduce Lemma D to the single quadratic survivor `(90,0)`. Its noncircular elimination remains open. Accordingly, absolute irreducibility is not claimed here as theorem-level complete.\n"""
s2, n = pattern.subn(new, s, count=1)
if n != 1:
    raise SystemExit(f"A/B status replacement count={n}")
p.write_text(s2)

for name in ["README.md", "PROJECT_STATUS.md", "DEMO.md", "CURRENT_PROOF_SNAPSHOT.md", "PROOF_ELEMENT_INDEX.md"]:
    p = root / name
    s = p.read_text()
    if "LOGICAL_PROOF_AUDIT.md" in s:
        continue
    candidates = {
        "README.md": (
            "- `CURRENT_PROOF_SNAPSHOT.md` — frozen cutoff statement and canonical claim boundary.\n",
            "- `CURRENT_PROOF_SNAPSHOT.md` — frozen cutoff statement and canonical claim boundary.\n- `LOGICAL_PROOF_AUDIT.md` — dependency, circularity, and sufficiency audit of Lemmas A–D.\n",
        ),
        "PROJECT_STATUS.md": (
            "## Canonical documents\n",
            "## Canonical documents\n\nThe logical dependency and circularity audit is `LOGICAL_PROOF_AUDIT.md`. It confirms an acyclic A–D chain, closes A–C in the current audit, and isolates D at `(90,0)`.\n",
        ),
        "DEMO.md": (
            "## 3:05–3:55 — Self-correction and scientific honesty\n",
            "## 3:05–3:55 — Self-correction and scientific honesty\n\nOpen `LOGICAL_PROOF_AUDIT.md` and show the dependency graph. Emphasize that the audit reran the proof logic without rerunning the large matrix computations.\n",
        ),
        "CURRENT_PROOF_SNAPSHOT.md": (
            "## Canonical status hierarchy\n",
            "## Canonical status hierarchy\n\n`LOGICAL_PROOF_AUDIT.md` is the canonical audit of dependency direction, sufficiency, and circularity.\n",
        ),
        "PROOF_ELEMENT_INDEX.md": (
            "# Proof element index\n",
            "# Proof element index\n\n- `LOGICAL_PROOF_AUDIT.md` — canonical dependency/circularity audit for Lemmas A–D and the post-irreducibility chain.\n",
        ),
    }
    anchor, replacement = candidates[name]
    if anchor not in s:
        raise SystemExit(f"anchor not found in {name}")
    p.write_text(s.replace(anchor, replacement, 1))

print("logical audit synchronization applied")