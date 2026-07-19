default(parisizemax,"4G");
y='y;x='x;a='a;
K=nfinit(y^3+y^2-2*y-1);
A=alginit(K,[2,[[],[]],[1/2,1/2,0]],x);
mt=algmultable(A);

T3=algtableinit(mt,3);
C3=algcenter(T3);
S3=algsplit(T3,a);

T7full=algtableinit(mt,7);
R7=algradical(T7full);
Q7data=algquotient(T7full,R7,1);
T7=Q7data[1];
proj7=Q7data[2];
S7=algsplit(T7,a);

out=fileopen("research/beal/data/local_split_7p3.txt","w");
filewrite(out,Str("ABS_DIM_MOD3=",algdim(T3)));
filewrite(out,Str("CENTER_DIM_MOD3=",matsize(C3)[2]));
filewrite(out,Str("SPLIT3_MAP_LEN=",#S3[1]));
filewrite(out,Str("SPLIT3_MATRIX_SIZE=",matsize(S3[1][1])));
filewrite(out,Str("FULL_DIM_MOD7=",algdim(T7full)));
filewrite(out,Str("RADICAL_DIM_MOD7=",matsize(R7)[2]));
filewrite(out,Str("RESIDUE_DIM_MOD7=",algdim(T7)));
filewrite(out,Str("SPLIT7_MAP_LEN=",#S7[1]));
filewrite(out,Str("SPLIT7_MATRIX_SIZE=",matsize(S7[1][1])));
filewrite(out,Str("PROJ7_SIZE=",matsize(proj7)));
fileclose(out);
print("local split maps: OK");
quit;