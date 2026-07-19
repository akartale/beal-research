x='x;K=bnfinit(x^3+x^2-2*x-1);
out=fileopen("research/beal/data/narrow_7p3.txt","w");
filewrite(out,Str("NARROW_CLASSNO=",bnrclassno(K,[1,[1,1,1]])));
filewrite(out,Str("UNITS=",K.fu));
fileclose(out);
quit;