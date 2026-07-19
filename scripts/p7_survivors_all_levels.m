load "research/beal/upstream/GFE-5p3/Codes/MagmaCode.m";
load "research/beal/upstream/GFE-5p3/Outputs/Data.txt";

// Detailed reruns needed because the published TheoremA.txt used flag=false
// for (2,2), (2,3), and (3,3), so it does not identify which individual
// non-Bad forms retain p=7.

print "=== level (2,2) ===";
time TheoremA(2,2,Data : flag := true);

print "=== level (2,3) ===";
time TheoremA(2,3,Data : flag := true);

print "=== level (3,3) ===";
time TheoremA(3,3,Data : flag := true);