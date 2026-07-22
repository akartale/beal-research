#!/usr/bin/env python3
"""Exact branch-splitting test at the two t=1 nodes over F_49."""

P = 7

# F_49 = F_7[a]/(a^2-a-1); represent x+y*a as (x,y).
def add(u, v):
    return ((u[0] + v[0]) % P, (u[1] + v[1]) % P)


def mul(u, v):
    x, y = u
    z, w = v
    # a^2=a+1
    return ((x*z + y*w) % P, (x*w + y*z + y*w) % P)


def power(u, n):
    out = (1, 0)
    while n:
        if n & 1:
            out = mul(out, u)
        u = mul(u, u)
        n >>= 1
    return out


def frobenius(u):
    return power(u, P)


def q(x):
    # q(X)=1+5X+5X^2, the squarefree quotient f/g^2.
    return add((1, 0), add(mul((5, 0), x), mul((5, 0), mul(x, x))))


def main():
    alpha = (0, 1)
    beta = frobenius(alpha)
    assert mul(alpha, alpha) == add(alpha, (1, 0))
    assert beta != alpha

    qa = q(alpha)
    qb = q(beta)
    euler_a = power(qa, (P*P - 1)//2)
    euler_b = power(qb, (P*P - 1)//2)

    print("alpha", alpha)
    print("beta", beta)
    print("q(alpha)", qa)
    print("q(beta)", qb)
    print("q(alpha)^24", euler_a)
    print("q(beta)^24", euler_b)
    print("branches_split_over_F49", euler_a == (1,0) and euler_b == (1,0))
    print("branch_splitting_character_at_Frob49", -1 if euler_a == (P-1,0) else 1)

    assert euler_a == (P-1, 0)
    assert euler_b == (P-1, 0)
    print("toric_splitting_character=unramified_quadratic")


if __name__ == "__main__":
    main()