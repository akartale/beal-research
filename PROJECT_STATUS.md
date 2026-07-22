# Project status

This is the short version for the hackathon.

The main computer work is done for all four levels we expected. Every search ended with no matching candidate.

Three of the four irreducibility checks are done. One small case is still open. In the notes it is called `(90,0)`.

So the project is close, but it is not a finished proof yet.

## What is done

- the main curve setup is in place
- the local case table is written down
- the ray class group was computed exactly
- all 360 characters were checked
- the reducible branch was reduced to one survivor
- the Brandt calculations were run at all four levels
- no matching Hecke packet survived
- the scripts save exact outputs and can be run again

The biggest module had size 2026, so this was not a tiny test.

## The last open case

Only `(90,0)` remains.

A computer calculation at level `(2,2)` finds no match for it. It would be nice to stop there, but we cannot. The theorem needed to use that calculation already assumes irreducibility. Using it here would be circular.

There are two possible ways to finish the job.

The first is an Eisenstein series argument. Most of the needed numbers are already known. The remaining work is to check the constant term at every cusp and make sure the setup at this level is correct.

The second is to recover the missing real multiplication action on the curve. The source builds the quotient curve, but it does not give the actual matrix we need.

The Eisenstein route looks more realistic right now.

## The four computer checks

- level `(2,3)`: 226 starting cases, then 8, then 4, then 0
- level `(3,2)`: 406 starting cases, then 15, then 4, then 0
- level `(3,3)`: 2026 starting cases, and the filters leave 0
- level `(2,2)`: no matching candidate

These are exact computer results. They matter, but they do not finish the theorem by themselves.

## What is still missing

- remove the last survivor without circular reasoning
- finish the written link between the modular theorem and the Brandt calculations
- check the last edge cases with signs and valuations
- rerun the important scripts from a clean setup
- put the whole argument into one final draft

## What we can safely say

We built a working research pipeline for the Beal case with powers 3, 5 and 7. It finishes the main exact computer search, cuts 360 possible characters down to one, and leaves a small and clearly described proof gap.

We are not claiming the full theorem is proved.

## Rough progress

These are just project estimates, not probabilities that the theorem is true.

- code and calculations: about 90 percent
- irreducibility work: about 85 percent
- full theorem path: about 80 percent
- paper ready write-up: about 70 percent

The hard part now is not another huge search. It is writing the last math step correctly.