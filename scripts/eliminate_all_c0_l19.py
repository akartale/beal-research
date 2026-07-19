#!/usr/bin/env python3
"""Enumerate every algebraic-closure-valued ray character for Cl_m=[180,2].

This removes the unjustified assumption that the two diagonal characters are
already F_49-valued. All 180th roots of unity lie in F_{7^12}, since
ord_180(7)=12. The prime above 19 has ray-class coordinates [141,1].
"""
import galois

F = galois.GF(7**12)
alpha = F.primitive_element
zeta180 = alpha ** ((F.order - 1) // 180)
minus1 = F(6)
assert zeta180.multiplicative_order() == 180
assert minus1.multiplicative_order() == 2

# RM trace polynomials X^2-sX+p from all admissible nonsingular l=19
# specializations, reduced mod 7.
pairs = [
    (0,1),(0,4),(1,4),(1,6),(2,3),(3,1),(3,4),(3,5),(3,6),
    (4,1),(4,6),(5,2),(5,3),(5,5),(6,3),
]
X = galois.Poly.Identity(F)
actual = set()
for s, p in pairs:
    roots = (X**2 - F(s)*X + F(p)).roots()
    actual.update(int(r) for r in roots)

survivors = []
trace_in_F49 = []
for u in range(180):
    for v in range(2):
        chi = zeta180 ** ((141*u) % 180) * (minus1 ** v)
        tr = chi + F(19 % 7) / chi
        in_F49 = tr**49 == tr
        if in_F49:
            trace_in_F49.append((u,v,int(tr)))
        if int(tr) in actual:
            survivors.append((u,v,int(chi),int(tr),in_F49))

print(f"all_characters={180*2}")
print(f"actual_trace_values={len(actual)}")
print(f"characters_with_l19_trace_in_F49={len(trace_in_F49)}")
print(f"survivors_at_l19={len(survivors)}")
print("survivors=", survivors)