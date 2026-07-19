\\ Enumerate the first Fontaine--Laffaille q-Frobenius trace invariant for
\\ every unit v modulo 49 in the normalized infinity family.
\\
\\ PARI returns a 5-dimensional even-degree Monsky--Washnitzer matrix with
\\ one extraneous eigenvalue -7.  After squaring, that line contributes 49,
\\ hence zero modulo 49.  Therefore trace(M^2)/7 mod 7 is already the trace
\\ of (Frob_7^2/7) on the 4-dimensional genus-2 quotient modulo 7.

x='x;
p=7;
n=2;

showcase(a,v)={
  Q=45*v^2*x^6-108*7^a*v^2*x^5+90*v*x^3+9;
  M=hyperellpadicfrobenius(Q,p,n);
  tr=centerlift(lift(Mod(lift(trace(M*M)),49)));
  if(tr%7, error("trace not divisible by 7: a=",a," v=",v," tr=",tr));
  print(a," ",v," ",Mod(tr/7,7));
};

print("a v normalized_qtrace_mod7");
for(a=1,2,for(v=1,48,if(v%7,showcase(a,v))));
quit;