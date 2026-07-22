#!/usr/bin/env python3
from pathlib import Path
PRIMES=[11,19,29,31,41,59,61,71,79,89]
COORDS={11:((77,0),(167,0)),19:((141,1),(141,1)),29:((44,1),(134,1)),31:((106,0),(106,0)),41:((163,0),(73,0)),59:((58,1),(148,1)),61:((92,0),(92,0)),71:((39,0),(129,0)),79:((179,1),(179,1)),89:((132,1),(42,1))}
def split_entry(entry):
    body=entry[1:-1]; out=[]; start=0; depth=0
    for i,ch in enumerate(body):
        if ch=='[': depth+=1
        elif ch==']': depth-=1
        elif ch==',' and depth==0: out.append(body[start:i].strip()); start=i+1
    out.append(body[start:].strip()); return out
def get_entry(data,p):
    i=data.find(f'<{p},'); j=data.find('>,<',i)
    if j<0: j=data.find('>];',i)
    return data[i:j+1]
def main():
    data=Path('upstream/GFE-5p3/Outputs/Data.txt').read_text()
    rows={p:(lambda f:(f[2],f[3]))(split_entry(get_entry(data,p))) for p in PRIMES}
    L=["x='x;","rootany(z,L)={my(i);for(i=1,#L,if(subst(L[i],x,z)==0,return(1)));0};","T=ffinit(7,12,'t);a=ffgen(T,'a);g=ffprimroot(a);zz=g^((7^12-1)/180);mone=a^0*6;","A0=List();A1=List();AI=List();for(u=0,179,for(v=0,1,listput(A0,[u,v]);listput(A1,[u,v]);listput(AI,[u,v])));","keepbranch(L,p,c1,c2,polys,kind,ratio)={my(N=List(),j,u,v,ch1,ch2,tr1,tr2,z1,z2);for(j=1,#L,u=L[j][1];v=L[j][2];ch1=zz^((c1[1]*u)%180)*mone^((c1[2]*v)%2);ch2=zz^((c2[1]*u)%180)*mone^((c2[2]*v)%2);tr1=ch1+(a^0*(p%7))/ch1;tr2=ch2+(a^0*(p%7))/ch2;if(kind==1,if((tr1==a^0*((p+1)%7)||tr1==a^0*((-(p+1))%7))&&(tr2==a^0*((p+1)%7)||tr2==a^0*((-(p+1))%7)),listput(N,[u,v])),z1=if(ratio==2,tr1^2-a^0*((2*p)%7),tr1);z2=if(ratio==2,tr2^2-a^0*((2*p)%7),tr2);if(rootany(z1,polys)&&rootany(z2,polys),listput(N,[u,v]))));N};"]
    for p in PRIMES:
        c1,c2=COORDS[p]; z0,zi=rows[p]; ratio=1 if p%15==1 else 2
        L += [f"A0=keepbranch(A0,{p},{list(c1)},{list(c2)},{z0},0,{ratio});",f"A1=keepbranch(A1,{p},{list(c1)},{list(c2)},[],1,{ratio});",f"AI=keepbranch(AI,{p},{list(c1)},{list(c2)},{zi},0,{ratio});",f"print(\"p={p} t0=\",#A0,\" t1=\",#A1,\" tinf=\",#AI);"]
    L += ["print(\"T0=\",Vec(A0));","print(\"T1=\",Vec(A1));","print(\"TINF=\",Vec(AI));","quit;"]
    Path('scripts/lemmaD_special_branches_multprime.gp').write_text('\n'.join(L)+'\n')
if __name__=='__main__': main()