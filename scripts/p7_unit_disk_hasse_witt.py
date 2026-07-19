#!/usr/bin/env python3
"""Hasse--Witt matrices for y^2=5x^6-12x^5+10tx^3+t^2 over F_7."""

from __future__ import annotations

P = 7


def mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % P
    return out


def rank2(m: tuple[tuple[int, int], tuple[int, int]]) -> int:
    (a, b), (c, d) = m
    det = (a * d - b * c) % P
    if det:
        return 2
    return 1 if any(x % P for row in m for x in row) else 0


def mmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2)) % P for j in range(2)) for i in range(2))


def matrix_at(t: int):
    # coefficient list in ascending powers of x
    f = [t * t % P, 0, 0, 10 * t % P, 0, -12 % P, 5 % P]
    f3 = mul(mul(f, f), f)
    c = lambda n: f3[n] if n < len(f3) else 0
    # Standard genus-2 Cartier--Manin/Hasse--Witt convention.
    return ((c(6), c(5)), (c(13), c(12)))


def main() -> None:
    print("t M rank(M) rank(M^2) det")
    for t in range(P):
        m = matrix_at(t)
        m2 = mmul(m, m)  # Frobenius twist is trivial over F_7.
        det = (m[0][0] * m[1][1] - m[0][1] * m[1][0]) % P
        print(t, m, rank2(m), rank2(m2), det)


if __name__ == "__main__":
    main()