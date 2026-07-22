#!/usr/bin/env python3
P=7
M=49

def mul(x,y):
    a,b=x; c,d=y
    return ((a*c+b*d)%M,(a*d+b*c+b*d)%M)

def pw(x,e):
    r=(1,0)
    while e:
        if e&1:
            r=mul(r,x)
        x=mul(x,x)
        e//=2
    return r

def norm7(x):
    a,b=x
    return (a*a+a*b-b*b)%P

U=[(a,b) for a in range(M) for b in range(M) if norm7((a,b))]
H={pw(x,7) for x in U}
unseen=set(U)
idx={}
cos=[]
while unseen:
    g=next(iter(unseen))
    C={mul(g,h) for h in H}
    i=len(cos)
    for x in C:
        idx[x]=i
    cos.append(C)
    unseen-=C

split=idx[(1,0)]
w=(0,1)
cw=(27,35)
cb=(13,14)
r=next((a,0) for a in range(1,M) if a%7 and idx[(a,0)]!=split)
coords={}
for i in range(7):
    for j in range(7):
        coords[idx[mul(pw(r,i),pw(w,j))]]=(i,j)

print('basis_r',r)
print('split',coords[split])
print('w',coords[idx[w]])
print('cw',coords[idx[cw]])
print('cbar',coords[idx[cb]])
print('rational_subgroup',sorted({coords[idx[(a,0)]] for a in range(1,M) if a%7}))

def fadd(x,y):
    return ((x[0]+y[0])%7,(x[1]+y[1])%7)

def fmul(x,y):
    a,b=x; c,d=y
    return ((a*c+b*d)%7,(a*d+b*c+b*d)%7)

roots=[(0,1),(1,6)]
raw=[coords[idx[cw]],coords[idx[cb]]]
for lam in roots:
    ev=((1,0),lam)
    vals=[]
    for s in range(7):
        q1=((raw[0][0]+s)%7,raw[0][1])
        q2=((raw[1][0]+s)%7,raw[1][1])
        z=fadd(fmul(ev[0],q1),fmul(ev[1],q2))
        vals.append(z)
    print('lambda',lam,'projected',vals,'contains_zero',(0,0) in vals,'contains_w',(0,1) in vals)