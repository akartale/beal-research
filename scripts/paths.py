from pathlib import Path

BEAL_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = BEAL_ROOT / "data"
UPSTREAM_DIR = BEAL_ROOT / "upstream"

DATA_DIR.mkdir(parents=True, exist_ok=True)