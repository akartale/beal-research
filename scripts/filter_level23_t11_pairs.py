#!/usr/bin/env python3
"""Filter level-(2,3) mod-7 packets by the two split norm-11 traces."""
from __future__ import annotations

import pickle
from pathlib import Path

from paths import DATA_DIR

from wiedemann_hecke_mod7 import build_or_load

P = 7
CONJ_CACHE = DATA_DIR / "hecke_t11_conjugate_mod7.pkl"


def dense(rows):
    n = len(rows)
    out = [[0] * n for _ in range(n)]
    for i, row in enumerate(rows):
        for j, value in row.items():
            out[i][j] = value % P
    return out


def rank_mod7(matrix):
    a = [row[:] for row in matrix]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    rank = 0
    for col in range(n):
        pivot = next((r for r in range(rank, m) if a[r][col] % P), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col] % P, -1, P)
        a[rank] = [(x * inv) % P for x in a[rank]]
        for r in range(m):
            if r != rank and a[r][col] % P:
                factor = a[r][col] % P
                a[r] = [(x - factor * y) % P for x, y in zip(a[r], a[rank])]
        rank += 1
        if rank == m:
            break
    return rank


def common_eigenspace_dim(a_rows, b_rows, av, bv):
    A = dense(a_rows)
    B = dense(b_rows)
    n = len(A)
    stacked = []
    for i in range(n):
        row = A[i]
        row[i] = (row[i] - av) % P
        stacked.append(row)
    for i in range(n):
        row = B[i]
        row[i] = (row[i] - bv) % P
        stacked.append(row)
    return n - rank_mod7(stacked)


def legendre(x, p):
    x %= p
    if x == 0:
        return 0
    return 1 if pow(x, (p - 1) // 2, p) == 1 else -1


def fval(x, t, p):
    return (5 * pow(x, 6, p) - 12 * pow(x, 5, p) + 10 * t * pow(x, 3, p) + t * t) % p


def smooth(t, p):
    for x in range(p):
        f = fval(x, t, p)
        fp = (30 * pow(x, 5, p) - 60 * pow(x, 4, p) + 30 * t * pow(x, 2, p)) % p
        if f == 0 and fp == 0:
            return False
    return True


def count_fp(t, p):
    return sum(1 + legendre(fval(x, t, p), p) for x in range(p)) + (2 if legendre(5, p) == 1 else 0)


def nonsquare(p):
    return next(d for d in range(2, p) if legendre(d, p) == -1)


def mul(x, y, p, d):
    a, b = x
    c, e = y
    return ((a*c + b*e*d) % p, (a*e + b*c) % p)


def power(x, n, p, d):
    out, base = (1, 0), x
    while n:
        if n & 1:
            out = mul(out, base, p, d)
        base = mul(base, base, p, d)
        n //= 2
    return out


def f2val(x, t, p, d):
    x3 = power(x, 3, p, d)
    x5 = power(x, 5, p, d)
    x6 = mul(x5, x, p, d)
    return ((5*x6[0]-12*x5[0]+10*t*x3[0]+t*t) % p,
            (5*x6[1]-12*x5[1]+10*t*x3[1]) % p)


def qchar2(a, p, d):
    if a == (0, 0):
        return 0
    return 1 if power(a, (p*p-1)//2, p, d) == (1, 0) else -1


def count_fp2(t, p):
    d = nonsquare(p)
    affine = sum(1 + qchar2(f2val((a,b),t,p,d),p,d)
                 for a in range(p) for b in range(p))
    return affine + 2


def attainable_pairs_at_11():
    ell = 11
    pth = {pow(c, 7, ell) for c in range(1, ell)}
    fifth = {pow(b, 5, ell) for b in range(1, ell)}
    ts = set()
    for A in range(1, ell):
        A3 = pow(A, 3, ell)
        for B5 in fifth:
            if (A3 + B5) % ell in pth:
                t = (-B5 * pow(A3, -1, ell)) % ell
                if smooth(t, ell):
                    ts.add(t)
    pairs = set()
    details = []
    for t in sorted(ts):
        n1, n2 = count_fp(t,ell), count_fp2(t,ell)
        s = 1 + ell - n1
        prod = (n2 - 1 - ell*ell + s*s)//2 - 2*ell
        roots = [r for r in range(P) if (r*r - s*r + prod) % P == 0]
        for a in roots:
            b = (s-a) % P
            pairs.add((a,b))
        details.append((t, s % P, prod % P, roots))
    return details, pairs


def main():
    data = build_or_load()
    with CONJ_CACHE.open("rb") as handle:
        conj = pickle.load(handle)
    _, t11a = data[2]
    _, t11b = conj[2]
    details, attainable = attainable_pairs_at_11()
    print(f"attainable details={details}")
    print(f"attainable ordered pairs={sorted(attainable)}")
    surviving = []
    for a, b in sorted(attainable):
        dim = common_eigenspace_dim(t11a, t11b, a, b)
        print(f"pair=({a},{b}) common eigenspace dim={dim}")
        if dim:
            surviving.append((a,b,dim))
    print(f"surviving={surviving}")


if __name__ == "__main__":
    main()