# Beal case 3, 5, 7

This repo is about one hard number theory problem. We are studying whether the equation with powers 3, 5 and 7 can have a primitive whole number solution.

The main idea was simple: do not ask AI to write a nice sounding proof. Make it build the calculations, check every case, save the results, and point out where the argument is still weak.

![Project overview](ARCHITECTURE.png)

## Where to start

For a quick look, open these files:

- `DEMO.md` for the short presentation
- `PROJECT_STATUS.md` for the current state
- `NEXT_STEPS.md` for what is left
- `CURRENT_PROOF_SNAPSHOT.md` for the careful math version
- `LOGICAL_PROOF_AUDIT.md` for the dependency, circularity, and sufficiency audit

## What we built

The project now has working code for the main arithmetic checks. It can build the needed finite objects, run the Hecke tests, save exact results, and repeat the same calculation later.

It also keeps failed ideas and corrections. That turned out to be useful. A few arguments looked right at first, but the audit found gaps or circular reasoning. We kept those notes instead of hiding them.

The large computer checks are done for all four levels we expected. In every case the search ends with no matching candidate.

We also reduced the last reducible case from hundreds of characters to one specific survivor called `(90,0)`.

## What is still open

The project is not a full proof yet.

The last survivor still needs a clean argument that does not reuse a theorem which already assumes the thing we are trying to prove. There are two possible ways forward:

- finish a direct Eisenstein series argument
- recover the missing real multiplication action on the curve

The first route looks shorter. Most of the numbers are already known, but a few checks at every cusp still have to be written down carefully.

After that, the link between the math theorem and the Brandt module calculations also needs a final clean write-up.

## What can be claimed

The repo contains an exact and repeatable research pipeline for the 3, 5, 7 case. It finishes the main computer search, closes three of the four irreducibility checks, and leaves one very small final obstruction.

It does not prove the full Beal conjecture, and it does not yet prove the full 3, 5, 7 case.

That line matters. We would rather show the real state of the work than claim too much.

## Main folders

- `scripts` has the programs
- `data` has saved results and caches
- the certificate files explain what each calculation proves
- `MANUSCRIPT_357_FROM_SCRATCH.md` is the longer proof draft
- `full` is a separate research direction and is not part of this submission

## Current rough progress

The code and calculations are mostly done. The final theorem write-up is less complete because the last few links need proper proofs and source checks.

So the project is close, but not finished. Thats the honest version.