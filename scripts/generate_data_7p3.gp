read("research/beal/scripts/GPcode_7p3_lib.gp");

\\ Emit exactly the four-component records consumed by MagmaCode.m and by
\\ the open Python elimination backend:
\\     <ell, C1, C0, Coo>
DataEntry_7p3(p)=
{
  strjoin([
    concat("<",p),
    Candidates_7p3(p),
    Degenerate0_7p3(p),
    concat(Degenerateoo_7p3(p),">")
  ],",")
}

MagmaInput_7p3(P,path)=
{ local(out);
  if(#P==0,error("prime list must be nonempty"));
  out=fileopen(path,"w");
  filewrite1(out,"Data7p3:=[");
  for(i=1,#P,
    if(i>1,filewrite1(out,","));
    filewrite1(out,DataEntry_7p3(P[i]));
  );
  filewrite(out,"];");
  fileclose(out);
}

\\ All primes are coprime to 3*7.  Generation is intentionally prime-local:
\\ each completed entry is written before the next expensive hgm computation.
P7p3=[11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97];
MagmaInput_7p3(P7p3,"research/beal/data_7p3.txt");
quit;