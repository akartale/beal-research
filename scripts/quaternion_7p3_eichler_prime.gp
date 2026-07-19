default(parisizemax,"4G");
y='y;x='x;a='a;
K=nfinit(y^3+y^2-2*y-1);A=alginit(K,[2,[[],[]],[1/2,1/2,0]],x);
B=algbasis(A);mt=algmultable(A);
PreimageLattice(M,p)={my(n,Kmod,G);n=matsize(M)[2];Kmod=lift(matkermod(lift(M),p));G=concat(Kmod,p*matid(n));mathnf(G)}
out=fileopen("research/beal/data/eichler_prime_7p3.txt","w");

T3=algtableinit(mt,3);S3=algsplit(T3,a);
toM3=matinvmod(S3[2],3);cond3=toM3[7..9,];
filewrite(out,Str("COND3_SIZE=",matsize(cond3)));
H3=PreimageLattice(cond3,3);filewrite(out,Str("H3_DET=",abs(matdet(H3))));

T7full=algtableinit(mt,7);R7=algradical(T7full);
Q7data=algquotient(T7full,R7,1);T7=Q7data[1];proj7=Q7data[2];
S7=algsplit(T7,a);toM7=matinvmod(S7[2],7)*proj7;cond7=toM7[3..3,];
filewrite(out,Str("COND7_SIZE=",matsize(cond7)));
H7=PreimageLattice(cond7,7);filewrite(out,Str("H7_DET=",abs(matdet(H7))));

filewrite(out,Str("MOD3_KERNEL_OK=",cond3*H3%3==matrix(3,12)));
filewrite(out,Str("MOD7_KERNEL_OK=",cond7*H7%7==matrix(1,12)));
filewrite(out,Str("H3=",H3));filewrite(out,Str("H7=",H7));
fileclose(out);quit;