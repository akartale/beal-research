#!/usr/bin/env python3
"""Remove ignored transient artifacts without touching research/full."""

from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
PROTECTED = ROOT / "full"
ROOT_PATTERNS = [
    ".probe",
    ".write_probe",
    ".replaceblocks-*",
    "*.lock",
    "beal_fdom_transfer.*",
    "transfer_part_*",
]


def protected(path: Path) -> bool:
    try:
        path.resolve().relative_to(PROTECTED.resolve())
        return True
    except ValueError:
        return False


def remove(path: Path) -> None:
    if protected(path):
        raise RuntimeError(f"refusing to touch protected path: {path}")
    if path.is_dir() and not path.is_symlink():
        shutil.rmtree(path)
    else:
        path.unlink(missing_ok=True)
    print(f"removed {path.relative_to(ROOT)}")


def main() -> None:
    candidates: set[Path] = set()
    for pattern in ROOT_PATTERNS:
        candidates.update(ROOT.glob(pattern))

    for directory in ROOT.rglob("__pycache__"):
        if not protected(directory):
            candidates.add(directory)
    for suffix in ("*.pyc", "*.pyo"):
        for file in ROOT.rglob(suffix):
            if not protected(file):
                candidates.add(file)

    for path in sorted(candidates, key=lambda p: (len(p.parts), str(p)), reverse=True):
        if path.exists():
            remove(path)


if __name__ == "__main__":
    main()