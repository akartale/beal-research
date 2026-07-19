#!/usr/bin/env python3
import sympy as sp
x=sp.symbols('x')

def hw(f):
    g=sp.Poly(sp.expand(f**3),x,modulus=7)
    c=lambda k:int(g.coeff_monomial(x**k))%7
    M=[[c(6),c(5)],[c(13),c(12)]]
    d=(M[0][0]*M[1][1]-M[0][1]*M[1][0])%7
    return M,d,sp.factor(f,modulus=7),sp.gcd(sp.Poly(f,x,modulus=7),sp.Poly(sp.diff(f,x),x,modulus=7))

# t=s^5, x=s^2 X, y=s^5 Y; s -> 0
f0=1-12*x**5
# u=1/t=s^3, x=X/s, y=tY; s -> 0
finf=1+10*x**3+5*x**6
for name,f in [('stable_t0',f0),('stable_tinf',finf)]:
    M,d,fac,g=hw(f)
    print(name,'f=',sp.Poly(f,x,modulus=7).as_expr())
    print('factor=',fac,'gcd(f,fprime)=',g.as_expr())
    print('HW=',M,'det=',d,'ordinary=',d!=0)