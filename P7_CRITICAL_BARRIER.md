# Critical p=7 barrier

The author code proves residual irreducibility only above explicit bounds. The published computations are:

- `BoundIrreducibility(9,1,4) = 8969`;
- `BoundIrreducibility(9,2,4) = 41363281`;
- `BoundIrreducibility(5,1,4) = 809`;
- `BoundIrreducibility(5,2,4) = 335809`.

Therefore `p=7` is not covered by that irreducibility argument. Before level lowering and newform elimination can become a proof for

    A^3 + B^5 = C^7,

one must separately prove that the residual mod-7 RM representation of the genus-2 Frey Jacobian is absolutely irreducible, or classify and eliminate the reducible case.

The current project reduces this to three explicit local inputs:

1. Lemma A: exact finite-flat/Raynaud inertia types at the prime above 7;
2. Lemma B: conductor bounds for the diagonal characters of a reducible semisimplification;
3. the niveau-two local-to-global ray-class identification showing that odd tame exponents cannot globalize.

The ordinary reducible branch has already been eliminated over the full algebraic closure by the 360-character paired-trace computation at `l=19`; see `LEMMA_C_D_ABSOLUTE_CHARACTERS_AND_L19.md`.

The ghost specializations `t=-1/8` and `t=9/8` are impossible as characteristic-zero primitive integral solutions, but their mod-7 representations may still be congruent to the Frey representation. This is secondary to the irreducibility gap.