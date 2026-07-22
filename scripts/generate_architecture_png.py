#!/usr/bin/env python3
"""Generate a dependency-free architecture PNG with the Python standard library."""

from pathlib import Path
import struct
import zlib

W, H = 1800, 1000
WHITE = (255, 255, 255)
BLACK = (22, 22, 22)
LIGHT = (245, 247, 250)
ACCENT = (225, 235, 248)

# Minimal 5x7 bitmap font for uppercase letters, digits, and punctuation used below.
FONT = {
'A':["01110","10001","10001","11111","10001","10001","10001"],
'B':["11110","10001","10001","11110","10001","10001","11110"],
'C':["01111","10000","10000","10000","10000","10000","01111"],
'D':["11110","10001","10001","10001","10001","10001","11110"],
'E':["11111","10000","10000","11110","10000","10000","11111"],
'F':["11111","10000","10000","11110","10000","10000","10000"],
'G':["01111","10000","10000","10111","10001","10001","01111"],
'H':["10001","10001","10001","11111","10001","10001","10001"],
'I':["11111","00100","00100","00100","00100","00100","11111"],
'J':["00111","00010","00010","00010","10010","10010","01100"],
'K':["10001","10010","10100","11000","10100","10010","10001"],
'L':["10000","10000","10000","10000","10000","10000","11111"],
'M':["10001","11011","10101","10101","10001","10001","10001"],
'N':["10001","11001","10101","10011","10001","10001","10001"],
'O':["01110","10001","10001","10001","10001","10001","01110"],
'P':["11110","10001","10001","11110","10000","10000","10000"],
'Q':["01110","10001","10001","10001","10101","10010","01101"],
'R':["11110","10001","10001","11110","10100","10010","10001"],
'S':["01111","10000","10000","01110","00001","00001","11110"],
'T':["11111","00100","00100","00100","00100","00100","00100"],
'U':["10001","10001","10001","10001","10001","10001","01110"],
'V':["10001","10001","10001","10001","10001","01010","00100"],
'W':["10001","10001","10001","10101","10101","10101","01010"],
'X':["10001","10001","01010","00100","01010","10001","10001"],
'Y':["10001","10001","01010","00100","00100","00100","00100"],
'Z':["11111","00001","00010","00100","01000","10000","11111"],
'0':["01110","10001","10011","10101","11001","10001","01110"],
'1':["00100","01100","00100","00100","00100","00100","01110"],
'2':["01110","10001","00001","00010","00100","01000","11111"],
'3':["11110","00001","00001","01110","00001","00001","11110"],
'4':["00010","00110","01010","10010","11111","00010","00010"],
'5':["11111","10000","10000","11110","00001","00001","11110"],
'6':["01110","10000","10000","11110","10001","10001","01110"],
'7':["11111","00001","00010","00100","01000","01000","01000"],
'8':["01110","10001","10001","01110","10001","10001","01110"],
'9':["01110","10001","10001","01111","00001","00001","01110"],
' ':["00000"]*7, '-':["00000","00000","00000","11111","00000","00000","00000"],
'+':["00000","00100","00100","11111","00100","00100","00000"],
'(':["00010","00100","01000","01000","01000","00100","00010"],
')':["01000","00100","00010","00010","00010","00100","01000"],
',':["00000","00000","00000","00000","00110","00100","01000"],
'.':["00000","00000","00000","00000","00000","00110","00110"],
':':["00000","00110","00110","00000","00110","00110","00000"],
'/':["00001","00010","00100","01000","10000","00000","00000"],
'=':["00000","00000","11111","00000","11111","00000","00000"],
}

pixels = [[WHITE for _ in range(W)] for _ in range(H)]

def rect(x1,y1,x2,y2,color,outline=BLACK,width=3):
    for y in range(max(0,y1), min(H,y2)):
        for x in range(max(0,x1), min(W,x2)):
            pixels[y][x]=color
    for k in range(width):
        for x in range(x1,x2):
            if 0<=x<W and 0<=y1+k<H: pixels[y1+k][x]=outline
            if 0<=x<W and 0<=y2-1-k<H: pixels[y2-1-k][x]=outline
        for y in range(y1,y2):
            if 0<=y<H and 0<=x1+k<W: pixels[y][x1+k]=outline
            if 0<=y<H and 0<=x2-1-k<W: pixels[y][x2-1-k]=outline

def line(x1,y1,x2,y2,color=BLACK,width=3):
    dx=abs(x2-x1); sx=1 if x1<x2 else -1
    dy=-abs(y2-y1); sy=1 if y1<y2 else -1
    err=dx+dy
    while True:
        for oy in range(-width//2,width//2+1):
            for ox in range(-width//2,width//2+1):
                xx,yy=x1+ox,y1+oy
                if 0<=xx<W and 0<=yy<H: pixels[yy][xx]=color
        if x1==x2 and y1==y2: break
        e2=2*err
        if e2>=dy: err+=dy; x1+=sx
        if e2<=dx: err+=dx; y1+=sy

def arrow(x1,y1,x2,y2):
    line(x1,y1,x2,y2)
    if abs(x2-x1)>=abs(y2-y1):
        s=1 if x2>x1 else -1
        line(x2,y2,x2-18*s,y2-10)
        line(x2,y2,x2-18*s,y2+10)
    else:
        s=1 if y2>y1 else -1
        line(x2,y2,x2-10,y2-18*s)
        line(x2,y2,x2+10,y2-18*s)

def text_width(text,scale): return sum((6*scale) for _ in text)-scale

def draw_text(x,y,text,scale=3,color=BLACK,center=False):
    text=text.upper()
    if center: x-=text_width(text,scale)//2
    cx=x
    for ch in text:
        glyph=FONT.get(ch,FONT[' '])
        for gy,row in enumerate(glyph):
            for gx,val in enumerate(row):
                if val=='1':
                    for yy in range(scale):
                        for xx in range(scale):
                            px,py=cx+gx*scale+xx,y+gy*scale+yy
                            if 0<=px<W and 0<=py<H: pixels[py][px]=color
        cx+=6*scale

def multiline(cx,y,lines,scale=3,gap=12):
    for i,t in enumerate(lines): draw_text(cx,y+i*(7*scale+gap),t,scale,center=True)

# Header
draw_text(W//2,35,"AI-ASSISTED PROOF ENGINEERING",6,center=True)
draw_text(W//2,95,"SIGNATURE (3,5,7)",5,center=True)
draw_text(W//2,150,"EXACT COMPUTATION SEPARATED FROM THEOREM CERTIFICATION",3,center=True)

boxes=[(40,260,320,470),(390,260,670,470),(740,260,1020,470),(1090,260,1370,470),(1440,260,1740,470)]
labels=[
(["DIOPHANTINE INPUT"],["A3 + B5 = C7"]),
(["FREY LAYER"],["MOTIVE + RESIDUAL","REPRESENTATION"]),
(["LOCAL / GLOBAL AUDIT"],["IRREDUCIBILITY","CONDUCTORS","LEVEL LOWERING"]),
(["QUATERNIONIC LAYER"],["ICOSIAN ORDER","BRANDT MODULES"]),
(["EXACT HECKE SIEVE"],["PAIRED OPERATORS","11, 19, 29 OVER F7"]),
]
for i,(b,(head,body)) in enumerate(zip(boxes,labels)):
    rect(*b,ACCENT if i in (1,3,4) else LIGHT)
    multiline((b[0]+b[2])//2,b[1]+35,head,3,8)
    multiline((b[0]+b[2])//2,b[1]+105,body,2,8)
for a,b in zip(boxes,boxes[1:]): arrow(a[2]+5,(a[1]+a[3])//2,b[0]-5,(b[1]+b[3])//2)

cert=(520,650,900,840); audit=(1120,650,1500,840)
rect(*cert,LIGHT); rect(*audit,ACCENT)
multiline((cert[0]+cert[2])//2,cert[1]+35,["CERTIFICATES"],4)
multiline((cert[0]+cert[2])//2,cert[1]+105,["RANK-ZERO RESULTS","HASHES + ARTIFACTS"],2)
multiline((audit[0]+audit[2])//2,audit[1]+35,["PROOF AUDIT"],4)
multiline((audit[0]+audit[2])//2,audit[1]+105,["THEOREM BRIDGES","EXPLICIT GAP LEDGER"],2)
arrow((boxes[-1][0]+boxes[-1][2])//2,boxes[-1][3]+5,(cert[0]+cert[2])//2,cert[1]-5)
arrow(cert[2]+5,(cert[1]+cert[3])//2,audit[0]-5,(audit[1]+audit[3])//2)
line((audit[0]+audit[2])//2,audit[3]+5,(audit[0]+audit[2])//2,925)
line((audit[0]+audit[2])//2,925,530,925)
arrow(530,925,530,480)
draw_text(W//2,950,"SELF-CORRECTION LOOP: DETECT GAP - REVISE - REGENERATE CERTIFICATE",3,center=True)

raw=bytearray()
for row in pixels:
    raw.append(0)
    for r,g,b in row: raw.extend((r,g,b))

def chunk(kind,data):
    return struct.pack('>I',len(data))+kind+data+struct.pack('>I',zlib.crc32(kind+data)&0xffffffff)
png=b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',W,H,8,2,0,0,0))+chunk(b'IDAT',zlib.compress(bytes(raw),9))+chunk(b'IEND',b'')
out=Path(__file__).resolve().parents[1]/'ARCHITECTURE.png'
out.write_bytes(png)
print(out)