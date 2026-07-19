#!/usr/bin/env python3
"""Analyze exact area scaling for the (7,5,3) exponent-switch levels."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "fdom_area_grid.txt"
OUTPUT = ROOT / "data" / "fdom_area_grid_analysis.json"


def load_grid(path: Path) -> dict[tuple[int, int], dict[str, Fraction | int]]:
    grid: dict[tuple[int, int], dict[str, Fraction | int]] = {}
    for line in path.read_text().splitlines():
        fields = line.split()
        if len(fields) != 5 or not fields[0].isdigit():
            continue
        e3, e7 = map(int, fields[:2])
        grid[e3, e7] = {
            "area_over_pi": Fraction(fields[2]),
            "minus_orbifold_euler": Fraction(fields[3]),
            "index": int(fields[4]),
        }
    if set(grid) != {(a, b) for a in range(4) for b in range(4)}:
        raise ValueError("area grid is incomplete")
    return grid


def second_difference(values: list[Fraction], exponent: int) -> Fraction:
    if exponent < 2:
        raise ValueError("newspace second difference requires exponent >= 2")
    return values[exponent] - 2 * values[exponent - 1] + values[exponent - 2]


def main() -> None:
    grid = load_grid(INPUT)
    base = grid[0, 0]["area_over_pi"]
    assert isinstance(base, Fraction)
    u3 = [grid[e, 0]["area_over_pi"] / base for e in range(4)]
    u7 = [grid[0, e]["area_over_pi"] / base for e in range(4)]
    for e3 in range(4):
        for e7 in range(4):
            assert grid[e3, e7]["area_over_pi"] == base * u3[e3] * u7[e7]

    result: dict[str, object] = {
        "base_area_over_pi": str(base),
        "u3": [str(x) for x in u3],
        "u7": [str(x) for x in u7],
        "new_area_over_pi_scale": {},
    }
    scales: dict[str, str] = {}
    for e3 in (2, 3):
        for e7 in (2, 3):
            scale = base * second_difference(u3, e3) * second_difference(u7, e7)
            scales[f"{e3},{e7}"] = str(scale)
    result["new_area_over_pi_scale"] = scales
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n")

    print(f"base area/pi = {base}")
    print("u3 =", u3)
    print("u7 =", u7)
    for key, value in scales.items():
        print(f"formal new area/pi ({key}) = {value}")


if __name__ == "__main__":
    main()