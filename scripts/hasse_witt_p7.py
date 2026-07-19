#!/usr/bin/env python3
import sympy as sp
x,t=sp.symbols('x t')
f=5*x**6-12*x**5+10*t*x**3+t**2
g=sp.Poly(sp.expand(f**3),x,t,modulus=7)
def cx(k):
    return sp.Poly(sum(c*t**j for (i,j),c in g.terms() if i==k),t,modulus=7)
c5,c6,c12,c13=(cx(k) for k in (5,6,12,13))
det=sp.Poly(c6.as_expr()*c12.as_expr()-c5.as_expr()*c13.as_expr(),t,modulus=7)
print('c6 =',c6.as_expr())
print('c5 =',c5.as_expr())
print('c13=',c13.as_expr())
print('c12=',c12.as_expr())
print('det=',sp.factor(det.as_expr(),modulus=7))
for a in range(7):
    M=[[int(c6.eval(a))%7,int(c5.eval(a))%7],[int(c13.eval(a))%7,int(c12.eval(a))%7]]
    d=int(det.eval(a))%7
    print(a,M,'det',d,'ordinary',d!=0)