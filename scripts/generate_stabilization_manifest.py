#!/usr/bin/env python3
"""Generate a SHA-256 manifest for the canonical proof snapshot.

The ignored full/ directory is deliberately excluded.
"""
from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "STABILIZATION_MANIFEST.md"

FILES = [
    "README.md",
    "CURRENT_PROOF_SNAPSHOT.md",
    "LOGICAL_PROOF_AUDIT.md",
    "PROJECT_STATUS.md",
    "PROOF_ELEMENT_INDEX.md",
    "NEXT_STEPS.md",
    "DEMO.md",
    "ARCHITECTURE.png",
    "MANUSCRIPT_357_FROM_SCRATCH.md",
    "P7_FULL_PROOF_AUDIT.md",
    "SIGNATURE_357_PROOF_STATUS.md",
    "LEMMAS_ABCD_REAUDIT.md",
    "LEMMA_A_B_LOCAL_PROOF_DRAFT.md",
    "LEMMA_C_D_ABSOLUTE_CHARACTERS_AND_L19.md",
    "PRIMITIVE_VALUATION_CONDUCTOR_TABLE.md",
    "RAY_CLASS_357_RESULTS.md",
    "P7_QUADRATIC_SURVIVOR_LOCAL_CONDUCTOR.md",
    "P7_900_DIRECT_LOCAL_CERTIFICATE_AUDIT.md",
    "P7_900_EISENSTEIN_NECESSITY_BRIDGE_AUDIT.md",
    "P7_900_LEVEL22_BRANDT_CERTIFICATE.md",
    "JL_BRANDT_THEOREM_BRIDGE.md",
    "LEVEL_32_CERTIFICATE.md",
    "LEVEL_33_CERTIFICATE.md",
    "ICOSIAN_ORDER_CERTIFICATE.md",
    "ICOSIAN_CLASS_NUMBER_ONE_CERTIFICATE.md",
    "OPEN_COMPACT_K0_CERTIFICATE.md",
    "data/p7_900_brandt_level22_certificate.json",
    "data/p7_900_brandt_level22_cached_certificate.json",
    "data/p7_900_direct_local_certificate.json",
    "data/level32_paired_hecke_mod7.pkl",
    "data/hecke_t11_conjugate_mod7.pkl",
    "data/hecke_t19_pair_mod7.pkl",
    "data/hecke_t29_pair_mod7.pkl",
]


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    rows: list[str] = []
    missing: list[str] = []
    for relative in FILES:
        path = ROOT / relative
        if not path.is_file():
            missing.append(relative)
            continue
        rows.append(f"| `{relative}` | `{path.stat().st_size}` | `{digest(path)}` |")

    text = """# Stabilization Manifest\n\nGenerated for the 2026-07-21 proof snapshot. SHA-256 hashes preserve the exact canonical documents, certificates, and selected deterministic artifacts. The ignored `full/` directory is deliberately excluded.\n\n| File | Bytes | SHA-256 |\n|---|---:|---|\n"""
    text += "\n".join(rows) + "\n"
    if missing:
        text += "\n## Missing at generation time\n\n"
        text += "\n".join(f"- `{item}`" for item in missing) + "\n"
    OUTPUT.write_text(text, encoding="utf-8")
    print(f"wrote {OUTPUT.relative_to(ROOT)} with {len(rows)} hashes; missing={len(missing)}")


if __name__ == "__main__":
    main()