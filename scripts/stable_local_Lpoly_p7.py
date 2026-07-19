#!/usr/bin/env python3
import galois

def count_curve(field, coeffs, degree):
    q=field.order
    xs=field.elements
    vals=field.Zeros(xs.shape)
    for c in coeffs:
        vals=vals*xs+field(c % 7)
    chi=vals**((q-1)//2)
    affine=sum(1 if int(z)==0 else (2 if int(z)==1 else 0) for z in chi)
    if degree%2:
        inf=1
    else:
        lead=field(coeffs[0] % 7); z=lead**((q-1)//2)
        inf=1+(1 if int(z)==1 else -1)
    return affine+inf

def lpoly(coeffs,degree):
    F49=galois.GF(7**2); F2401=galois.GF(7**4)
    N1=count_curve(F49,coeffs,degree); N2=count_curve(F2401,coeffs,degree)
    q=49; a1=q+1-N1; S2=q*q+1-N2; a2=(a1*a1-S2)//2
    return N1,N2,a1,a2
# descending coefficient lists
curves={'t0':([2,0,0,0,0,1],5),'tinf':([-2,0,0,3,0,0,1],6)}
for name,(c,d) in curves.items():
    N1,N2,a1,a2=lpoly(c,d)
    print(name,'N49=',N1,'N2401=',N2,'L=1-',a1,'T+',a2,'T2-',49*a1,'T3+',49**2,'T4')