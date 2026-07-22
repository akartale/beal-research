#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data/lmfdb/level_2025"
TARGETS = {11: 2, 19: 1, 29: 2}
P = 7


class F49:
    __slots__ = ("a", "b")

    def __init__(self, a: int = 0, b: int = 0):
        self.a = a % P
        self.b = b % P

    @staticmethod
    def coerce(x):
        return x if isinstance(x, F49) else F49(int(x), 0)

    def __add__(self, other):
        other = self.coerce(other)
        return F49(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return F49(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        # u^2 = -1 gives F_49 because x^2+1 is irreducible over F_7.
        return F49(self.a * other.a - self.b * other.b,
                   self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def __pow__(self, n: int):
        if n < 0:
            return (self.inverse()) ** (-n)
        out = F49(1)
        base = self
        while n:
            if n & 1:
                out = out * base
            base = base * base
            n >>= 1
        return out

    def inverse(self):
        if self == F49(0):
            raise ZeroDivisionError
        return self ** (P * P - 2)

    def __truediv__(self, other):
        return self * self.coerce(other).inverse()

    def __rtruediv__(self, other):
        return self.coerce(other) / self

    def __eq__(self, other):
        other = self.coerce(other)
        return self.a == other.a and self.b == other.b

    def __repr__(self):
        return f"({self.a},{self.b})"


F49_ELEMENTS = [F49(a, b) for a in range(P) for b in range(P)]


def split_top(s: str) -> list[str]:
    out: list[str] = []
    start = 0
    depth = 0
    for i, ch in enumerate(s):
        if ch in "[<((":
            depth += 1
        elif ch in "]>))":
            depth -= 1
        elif ch == "," and depth == 0:
            out.append(s[start:i].strip())
            start = i + 1
    out.append(s[start:].strip())
    return [x for x in out if x]


def eval_expr(expr: str, value: F49, variable: str) -> F49:
    safe = expr.replace("^", "**")
    if not re.fullmatch(r"[0-9+\-*/() *xe]+", safe):
        raise ValueError(f"unsafe expression: {expr}")
    env = {variable: value, "x": value, "e": value}
    result = eval(safe, {"__builtins__": {}}, env)
    return F49.coerce(result)


def parse_record(path: Path):
    txt = path.read_text()
    pm = re.search(r"primes_array\s*=\s*\[(.*?)\]\nprimes\s*=", txt, re.S)
    vm = re.search(r"hecke_eigenvalues_array\s*=\s*\[(.*?)\]\nhecke_eigenvalues", txt, re.S)
    hm = re.search(r"^heckePol\s*=\s*(.+)$", txt, re.M)
    if not pm or not vm or not hm:
        raise ValueError(f"missing data in {path}")

    primes = [(int(a), int(b)) for a, b in re.findall(r"\[\s*(\d+)\s*,\s*(\d+)\s*,", pm.group(1))]
    vals = split_top(vm.group(1).replace("\\\n", ""))
    if len(primes) != len(vals):
        raise ValueError(f"array length mismatch in {path}: {len(primes)} != {len(vals)}")

    selected: dict[int, list[str]] = {11: [], 19: [], 29: []}
    for (norm, _rational_prime), val in zip(primes, vals):
        if norm in TARGETS:
            selected[norm].append(val)
    for norm in TARGETS:
        if len(selected[norm]) != 2:
            raise ValueError(f"expected two primes of norm {norm} in {path}, got {len(selected[norm])}")
    return hm.group(1).strip(), selected


def main() -> None:
    rows = []
    survivors = []
    for path in sorted(DATA_DIR.glob("2.2.5.1-2025.1-?.sage")):
        hecke_pol, selected = parse_record(path)
        roots = [r for r in F49_ELEMENTS if eval_expr(hecke_pol, r, "x") == F49(0)]
        surviving_roots = []
        root_checks = []
        for root in roots:
            checks = []
            ok = True
            for norm in (11, 19, 29):
                target = F49(TARGETS[norm])
                for idx, expr in enumerate(selected[norm], start=1):
                    value = eval_expr(expr, root, "e")
                    matched = value == target
                    checks.append({"norm": norm, "index": idx, "value": repr(value), "target": repr(target), "matched": matched})
                    ok = ok and matched
            root_checks.append({"root": repr(root), "checks": checks, "survives": ok})
            if ok:
                surviving_roots.append(repr(root))
        survives = bool(surviving_roots)
        row = {
            "label": path.stem,
            "hecke_polynomial": hecke_pol,
            "roots_in_F49": [repr(r) for r in roots],
            "surviving_roots": surviving_roots,
            "survives": survives,
            "root_checks": root_checks,
        }
        rows.append(row)
        if survives:
            survivors.append(path.stem)
        print(path.stem, "roots", [repr(r) for r in roots], "survivors", surviving_roots)

    out = {
        "field": "F_49 = F_7[u]/(u^2+1)",
        "targets": {str(k): v for k, v in TARGETS.items()},
        "packets_tested": len(rows),
        "survivors": survivors,
        "rows": rows,
    }
    out_path = ROOT / "data/p7_900_level2025_hecke_certificate.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n")
    print("packets_tested", len(rows))
    print("survivors", survivors)
    if survivors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()