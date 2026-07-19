#!/usr/bin/env python3
"""Classify first-order t=0 Frey lifts modulo 49 under affine changes.

For b=1 the normalized equation modulo 49 is

    C_u: y^2 = -108*x^5 + 42*u*x^3 + 9*u^2  (mod 49),

where u is a unit modulo 49.  The x^6 term is divisible by 49.

We test affine hyperelliptic changes

    x = a*X + r,   y = b*Y,

with a,b units modulo 49 and r divisible by 7.  Requiring exact equality with
another member C_v gives a rigorous lower-bound classification: curves in
different reported orbits are not equivalent under this natural subgroup of
integral coordinate changes.  Equality under arbitrary PGL_2 changes is not
claimed.
"""

from __future__ import annotations

from collections import defaultdict, deque
from math import comb

M = 49
UNITS = [x for x in range(M) if x % 7]


def polynomial(u: int) -> list[int]:
    coeffs = [0] * 6
    coeffs[0] = 9 * u * u
    coeffs[3] = 42 * u
    coeffs[5] = -108
    return [c % M for c in coeffs]


def affine_transform(coeffs: list[int], a: int, r: int, b: int) -> list[int]:
    inv_b2 = pow((b * b) % M, -1, M)
    out = [0] * len(coeffs)
    for degree, coefficient in enumerate(coeffs):
        for j in range(degree + 1):
            out[j] += coefficient * comb(degree, j) * pow(a, j, M) * pow(r, degree - j, M)
    return [(value * inv_b2) % M for value in out]


def equivalences() -> dict[int, set[int]]:
    # The X^4 coefficient after x=aX+r is
    #   -108*5*a^4*r/b^2 mod 49.
    # For r=7c and unit a,b this vanishes only for c=0 mod 7, so r=0.
    # We can therefore solve the three remaining coefficient conditions
    # directly, without expanding every polynomial.
    graph: dict[int, set[int]] = defaultdict(set)
    squares = defaultdict(list)
    for b in UNITS:
        squares[(b * b) % M].append(b)

    for u in UNITS:
        for a in UNITS:
            a5 = pow(a, 5, M)
            if a5 not in squares:
                continue
            # Degree 3 equality is only modulo 7 because its coefficient is 42.
            required_v_mod7 = (u * pow(a, -2, 7)) % 7
            for v in UNITS:
                if v % 7 != required_v_mod7:
                    continue
                # Constant coefficient equality modulo 49.
                if (u * u - a5 * v * v) % M:
                    continue
                graph[u].add(v)
                graph[v].add(u)
    return graph


def connected_components(graph: dict[int, set[int]]) -> list[list[int]]:
    unseen = set(UNITS)
    components: list[list[int]] = []
    while unseen:
        start = min(unseen)
        queue = deque([start])
        component: set[int] = set()
        while queue:
            u = queue.popleft()
            if u in component:
                continue
            component.add(u)
            queue.extend(graph[u] - component)
        unseen -= component
        components.append(sorted(component))
    return components


def main() -> None:
    graph = equivalences()
    components = connected_components(graph)
    print("AFFINE_MOD49_ORBITS", len(components))
    for index, component in enumerate(components, 1):
        residues = sorted({u % 7 for u in component})
        print(index, "size", len(component), "mod7", residues, "units", component)


if __name__ == "__main__":
    main()