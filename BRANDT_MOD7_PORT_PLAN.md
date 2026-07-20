# Lightweight mod-7 Brandt-module port for Q(sqrt(5))

## Goal

Recover the individual p=7 candidate sets C_23 and C_33 without Magma or a
full Sage installation.  The target levels are

    N_23 = (3)^2 * p5^3,
    N_33 = (3)^3 * p5^3,

where O_K = Z[a], a^2-a-1=0, and p5=(2*a-1) is the unique prime over 5.

Only the Hecke module modulo 7 is required.  We do not need integral Hecke
fields, complex embeddings, or full newform q-expansions.

## Audited open-source implementations

### PARI/GP script libraries

The public PARI script collection includes quaternion and Brandt routines over
Q, but not the totally real number-field ideal arithmetic needed here.  It is
useful for low-level number-field and lattice operations, not as a complete HMF
backend.

### psage sqrt5 implementation

The repository `williamstein/psage` contains a direct implementation of
Dembele's algorithm specialized to Q(sqrt(5)):

    psage/modform/hilbert/sqrt5/sqrt5.py
    psage/modform/hilbert/sqrt5/sqrt5_fast.pyx

The mathematical specialization is exactly relevant: Hamilton's quaternion
algebra over Q(sqrt(5)), the icosian maximal order, reduction modulo the level,
P^1(O_K/N), and Hecke operators obtained from norm-p icosians.

It is not a lightweight installable solution.  The Python layer imports Sage
number fields, quaternion algebras, ideals, residue fields, and matrices.  The
Cython layer also imports Sage integer, ideal, matrix, allocation, and PARI
wrappers.  Its reusable contribution is therefore the algorithm and explicit
icosian formulas, not a standalone binary.

## Minimal replacement architecture

### 1. Quadratic-field arithmetic

Represent x+y*a by integer pairs `(x,y)`, with

    a^2 = a+1,
    conjugate(x+y*a) = (x+y)-y*a,
    norm(x+y*a) = x^2+x*y-y^2.

Implement exact addition, multiplication, conjugation, norm, and reduction by
an ideal lattice.  PARI/GP remains the oracle for ideal HNF/SNF and
factorization during validation, but the hot loops use fixed-width integer
pairs.

### 2. Quotient ring O_K/N

Represent an integral ideal by a 2x2 HNF lattice in the basis `(1,a)`.  Reduce
pairs modulo that lattice.  Build multiplication tables once for each target
level.  The quotient sizes are

    |O_K/N_23| = 10125,
    |O_K/N_33| = 91125.

The larger quotient is still small enough for indexed tables, especially when
Chinese-remainder decomposition is used:

    O_K/N_ab ~= O_K/(3^a) x O_K/(p5^b).

### 3. Projective line P^1(O_K/N)

Port the normalization/orbit logic from `sqrt5_fast.pyx`.  Enumerate primitive
pairs `(c,d)` modulo N and quotient by units.  Store one canonical integer index
per projective point.  Avoid Python objects in the final hot loop.

### 4. Icosian action

Use the explicit generators of the icosian order recorded in `sqrt5.py`:

    i, j, k,
    (-1+i+j+k)/2,
    (i+a*j+(1-a)*k)/2.

At primes away from 2, denominators are invertible modulo both target levels.
Port the explicit local splitting map of the Hamilton quaternion algebra into
M_2(O_K/N).  Generate the finite unit action and orbit representatives on
P^1(O_K/N).

### 5. Hecke matrices modulo 7

For each small auxiliary prime q not dividing 3*5*7, enumerate the required
icosians of reduced norm q and accumulate their permutation action directly in
F_7.  Construct sparse Hecke matrices only modulo 7.

The stopping criterion is not full diagonalization over characteristic zero.
For each Hecke-stable residual constituent, compare its possible eigenvalues
with the admissible Frey trace sets used by `NewformBound`.  Intersect kernels
or generalized eigenspaces over finite extensions of F_7 as necessary.

### 6. Validation ladder

Before running the target levels, reproduce published psage examples at prime
levels 31 and 41:

    charpoly(T_5), charpoly(T_3), charpoly(T_11a), charpoly(T_11b).

Then reproduce the known dimensions/orbit counts from the upstream Magma run.
Only after these checks should the mod-7 candidate sieve be trusted.

## Implementation order

1. `ok_sqrt5.py`: pair arithmetic, ideal-HNF reduction, CRT, unit tests. **Completed.**
2. `p1_sqrt5.py`: P^1 over prime-power quotients and CRT products. **Completed.**
3. `icosian_mod_n.py`: quaternion multiplication and matrix reduction. **Completed.**
4. `icosian_orbits.py`: generate the 120 norm-one units and compute orbit bases. **Completed:** dimensions 226 and 2026.
5. `hecke_t2_mod7.py`: first sparse Hecke operator modulo 7. **Completed and validated** against the published level-31 matrix up to orbit permutation; target matrices have 1122 and 10122 nonzero entries.
6. `enumerate_icosians.py`: prescribed reduced-norm enumeration in the rank-8 integral icosian basis. **Completed for pi=3+a, Norm(pi)=11:** exactly 1440 elements, decomposing into 12 free unit orbits of size 120.
7. `hecke_t11_mod7.py`: sparse T_q for q=(3+a), Norm(q)=11. **Completed:** nnz 2630 at N_23 and 24230 at N_33; both operators commute with T_2 modulo 7.
8. `brandt_mod7.py`: consolidate generic sparse Hecke construction and add further auxiliary primes.
9. `recover_c23_c33.py`: reproduce the exact `NewformBound` predicate modulo 7.

## Important scope decision

Do not port generic quaternion ideal-class machinery.  The class number of
Q(sqrt(5)) is one and the psage specialization already reduces the problem to
icosians acting on P^1(O_K/N).  A specialized port is substantially smaller
than a general Brandt-module package and directly matches the two required
levels.