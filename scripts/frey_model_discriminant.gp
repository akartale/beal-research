\\ Exact discriminant of the explicit genus-2 Frey model.
\\ Model from upstream/GFE-5p3/Outputs/CurveConstruction.txt:
\\   y^2 = 45*x^6 - 108*x^5 + 90*t*x^3 + 9*t^2.

x='x; t='t;
f = 45*x^6 - 108*x^5 + 90*t*x^3 + 9*t^2;
Draw = poldisc(f, x);
D = factor(Draw);
print("FREY_POLY=", f);
print("DISC_RAW=", Draw);
print("DISC_CONSTANT_FACTORED=", factor(32535882602611200000));
print("DISC_FACTORED=", D);

\\ Infinity chart: s=1/t and Y=y/t.
s='s;
finf = 9 + 90*s*x^3 + s^2*(45*x^6 - 108*x^5);
Dinfraw = poldisc(finf, x);
print("INFINITY_POLY=", finf);
print("INFINITY_DISC_RAW=", Dinfraw);
print("INFINITY_DISC_FACTORED=", factor(Dinfraw));
quit;