#!/usr/bin/env python3
"""Analyze the t=1 special fibre of the genus-2 Frey model over F_7."""

from __future__ import annotations

P = 7


def trim(a: list[int]) -> list[int]:
    a = [x % P for x in a]
    while a and a[-1] == 0:
        a.pop()
    return a


def divmod_poly(a: list[int], b: list[int]) -> tuple[list[int], list[int]]:
    a = trim(a[:])
    b = trim(b[:])
    if not b:
        raise ZeroDivisionError
    q = [0] * max(1, len(a) - len(b) + 1)
    inv = pow(b[-1], -1, P)
    while len(a) >= len(b) and a:
        k = len(a) - len(b)
        c = a[-1] * inv % P
        q[k] = c
        for i in range(len(b)):
            a[i + k] = (a[i + k] - c * b[i]) % P
        a = trim(a)
    return trim(q), a


def gcd_poly(a: list[int], b: list[int]) -> list[int]:
    a, b = trim(a), trim(b)
    while b:
        _, r = divmod_poly(a, b)
        a, b = b, r
    if not a:
        return []
    inv = pow(a[-1], -1, P)
    return [(x * inv) % P for x in a]


def mul_poly(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % P
    return trim(out)


def derivative(a: list[int]) -> list[int]:
    return trim([(i * a[i]) % P for i in range(1, len(a))])


def eval_poly(a: list[int], x: int) -> int:
    return sum(c * pow(x, i, P) for i, c in enumerate(a)) % P


def count_hyperelliptic_odd(q: list[int]) -> int:
    # y^2=q(x), deg(q)=3 or 4 after normalization; include infinity points directly.
    affine = 0
    for x in range(P):
        rhs = eval_poly(q, x)
        if rhs == 0:
            affine += 1
        elif pow(rhs, (P - 1) // 2, P) == 1:
            affine += 2
    deg = len(trim(q)) - 1
    if deg % 2 == 1:
        return affine + 1
    lead = trim(q)[-1]
    return affine + (2 if pow(lead, (P - 1) // 2, P) == 1 else 0)


def main() -> None:
    # f(x)=5x^6+2x^5+3x^3+1 at t=1 mod 7, ascending coefficients.
    f = [1, 0, 0, 3, 0, 2, 5]
    g = gcd_poly(f, derivative(f))
    q, r = divmod_poly(f, mul_poly(g, g))
    print("f", f)
    print("gcd(f,f')", g, "degree", len(g) - 1)
    print("squarefree quotient f/g^2", q, "remainder", r, "degree", len(q) - 1)
    print("g roots over F7", [a for a in range(P) if eval_poly(g, a) == 0])
    print("normalization point count", count_hyperelliptic_odd(q))
    # For an elliptic normalization, a_7=8-#E(F_7); ordinary iff a_7 not divisible by 7.
    n = count_hyperelliptic_odd(q)
    print("normalization trace", P + 1 - n)


if __name__ == "__main__":
    main()