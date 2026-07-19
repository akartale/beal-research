#!/usr/bin/env python3
"""Compare the explicit CM curve y^2=x^5-1 with Frey t=0 lifts mod 49.

Open-source Bouyer--Streng data identify the cyclic quartic CM field
x^4+5*x^2+5 with the genus-2 curve

    C_CM: y^2 = x^5 - 1.

For every u in (Z/49Z)^*, this script decides whether C_CM and

    C_u: y^2 = -108*x^5 + 42*u*x^3 + 9*u^2  (mod 49)

are isomorphic through a hyperelliptic binary-sextic change induced by
GL_2(Z/49Z), together with y-scaling. Instead of enumerating all 7^5 lifts
of each residue-field transformation, it linearizes the lift equations over
F_7 and tests membership in the resulting five-dimensional tangent span.

The answer is exact for GL_2(Z/49Z) binary-sextic equivalence.
"""

from __future__ import annotations

from itertools import product
from math import comb

P = 7
M = 49
Vector = tuple[int, ...]


def cm_form(modulus: int) -> Vector:
    return tuple([-1 % modulus, 0, 0, 0, 0, 1, 0])


def frey_form(u: int, modulus: int) -> Vector:
    out = [0] * 7
    out[0] = 9 * u * u
    out[3] = 42 * u
    out[5] = -108
    return tuple(value % modulus for value in out)


def linear_power(a: int, b: int, n: int, modulus: int) -> dict[int, int]:
    return {
        i: comb(n, i) * pow(a, i, modulus) * pow(b, n - i, modulus) % modulus
        for i in range(n + 1)
    }


def transform(form: Vector, g: tuple[int, int, int, int], modulus: int) -> Vector:
    a, b, c, d = g
    out = [0] * 7
    for i, coefficient in enumerate(form):
        if coefficient % modulus == 0:
            continue
        left = linear_power(a, b, i, modulus)
        right = linear_power(c, d, 6 - i, modulus)
        for ix, lv in left.items():
            for jx, rv in right.items():
                out[ix + jx] = (out[ix + jx] + coefficient * lv * rv) % modulus
    return tuple(out)


def rank(rows: list[list[int]]) -> int:
    matrix = [[entry % P for entry in row] for row in rows]
    if not matrix:
        return 0
    r = 0
    for col in range(len(matrix[0])):
        pivot = next((i for i in range(r, len(matrix)) if matrix[i][col]), None)
        if pivot is None:
            continue
        matrix[r], matrix[pivot] = matrix[pivot], matrix[r]
        inv = pow(matrix[r][col], -1, P)
        matrix[r] = [(inv * x) % P for x in matrix[r]]
        for i in range(len(matrix)):
            if i != r and matrix[i][col]:
                factor = matrix[i][col]
                matrix[i] = [(x - factor * y) % P for x, y in zip(matrix[i], matrix[r])]
        r += 1
        if r == len(matrix):
            break
    return r


def in_span(vector: Vector, generators: list[Vector]) -> bool:
    base = rank([list(row) for row in generators])
    enlarged = rank([list(row) for row in generators] + [list(vector)])
    return base == enlarged


def gl2_f7() -> list[tuple[int, int, int, int]]:
    return [
        (a, b, c, d)
        for a, b, c, d in product(range(P), repeat=4)
        if (a * d - b * c) % P
    ]


def scalar_multiple(a: Vector, b: Vector) -> int | None:
    scalar: int | None = None
    for x, y in zip(a, b):
        x %= P
        y %= P
        if y:
            candidate = x * pow(y, -1, P) % P
            if candidate == 0:
                return None
            if scalar is None:
                scalar = candidate
            elif scalar != candidate:
                return None
        elif x:
            return None
    return scalar


def divide_by_7(vector: Vector) -> Vector:
    assert all(value % P == 0 for value in vector)
    return tuple((value // P) % P for value in vector)


def difference_mod49(a: Vector, b: Vector) -> Vector:
    return tuple((x - y) % M for x, y in zip(a, b))


def scale_mod(c: int, form: Vector, modulus: int) -> Vector:
    return tuple(c * x % modulus for x in form)


def lifted_tangent(cm: Vector, g0: tuple[int, int, int, int]) -> list[Vector]:
    base = transform(cm, g0, M)
    generators: list[Vector] = []
    for index in range(4):
        lifted = list(g0)
        lifted[index] += P
        moved = transform(cm, tuple(lifted), M)
        generators.append(divide_by_7(difference_mod49(moved, base)))
    return generators


def equivalent(u49: int) -> tuple[bool, tuple[int, int, int, int] | None, int | None]:
    cm49 = cm_form(M)
    cm7 = cm_form(P)
    target49 = frey_form(u49, M)
    target7 = frey_form(u49 % P, P)

    for g0 in gl2_f7():
        moved7 = transform(cm7, g0, P)
        c = scalar_multiple(moved7, target7)
        if c is None:
            continue
        roots = [b0 for b0 in range(1, P) if b0 * b0 % P == c]
        for b0 in roots:
            moved49 = transform(cm49, g0, M)
            scaled_target49 = scale_mod(b0 * b0, target49, M)
            delta49 = difference_mod49(moved49, scaled_target49)
            if any(value % P for value in delta49):
                continue
            residual = divide_by_7(delta49)
            generators = lifted_tangent(cm49, g0)
            generators.append(scale_mod((-2 * b0) % P, target7, P))
            if in_span(residual, generators):
                return True, g0, b0
    return False, None, None


def main() -> None:
    print("u_mod7 matching_lifts_mod49")
    for residue in range(1, P):
        matches = []
        for lift_digit in range(P):
            u49 = residue + P * lift_digit
            ok, _, _ = equivalent(u49)
            if ok:
                matches.append(u49)
        print(residue, matches)


if __name__ == "__main__":
    main()