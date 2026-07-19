read("research/beal/scripts/GPcode_7p3_lib.gp");

\\ Override p before reading this file when a different prime is wanted.
if(type(p)!="t_INT",p=11);
entry=DataEntry_7p3(p);
print(entry);
out=fileopen("research/beal/data_7p3_one.txt","w");
filewrite(out,entry);
fileclose(out);
quit;