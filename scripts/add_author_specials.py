from pathlib import Path
p=Path('research/beal/scripts/p7_reducible_sieve_full.py')
s=p.read_text()
start=s.index('SPECIAL=')
end=s.index('def main():',start)
new=r'''def split_top(text):
 out=[];start=0;depth=0
 for i,ch in enumerate(text):
  if ch in '[<(':depth+=1
  elif ch in ']> )'.replace(' ',''):depth-=1
  elif ch==',' and depth==0:
   out.append(text[start:i].strip());start=i+1
 out.append(text[start:].strip());return out

def parse_poly(poly):
 z=poly.replace(' ','').replace('*','')
 if z=='x':return (1,0,0)
 if z.startswith('x^2'):
  tail=z[3:]
  b=0;c=0
  import re
  m=re.match(r'([+-]\d*)x(.*)$',tail)
  if m:
   t=m.group(1);b=-1 if t=='-' else (1 if t=='+' else int(t));tail=m.group(2)
  if tail:c=int(tail)
  return (2,b,c)
 if z.startswith('x'):
  return (1,int(z[1:] or '0'),0)
 raise ValueError(poly)

def author_specials():
 text=Path('research/beal/upstream/GFE-5p3/Outputs/Data.txt').read_text().strip()
 body=text[text.index('[')+1:text.rfind(']')]
 entries=split_top(body);ans={}
 for ent in entries:
  e=ent.strip()
  if not (e.startswith('<') and e.endswith('>')):continue
  parts=split_top(e[1:-1])
  if len(parts)!=4:continue
  l=int(parts[0]);polys=[]
  for block in parts[2:4]:
   inner=block.strip()[1:-1].strip()
   if inner:polys.extend(parse_poly(q) for q in split_top(inner))
  ans[l]=polys
 return ans
SPECIAL=author_specials()
def special_roots(l):
 out=set()
 for deg,b,c in SPECIAL.get(l,[]):
  if deg==1:out.add((-b%7,0))
  else:out|=roots((-b)%7,c)
 return out
'''
s=s[:start]+new+s[end:]
p.write_text(s)