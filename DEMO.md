# Five minute demo

## The quick pitch

We used AI to help with a hard number theory problem, but not in the usual way. The goal was not to get a fancy proof written in one shot. The goal was to make the system do the calculations, check its own work, save exact results, and tell us where the proof still has a hole.

## First minute

Start with the problem.

We are looking at the Beal case with powers 3, 5 and 7. The question is whether there can be a primitive whole number solution.

Then say:

> This is a very hard case. We asked the system to turn the research into code and small checkable steps. It also had to admit when something was not proved.

## Show the project picture

Open `ARCHITECTURE.png`.

Explain it in plain words:

> We start from the equation. Then we build the curve used in the modular method. After that we check the possible characters, reduce the number of cases, and run exact Hecke calculations. Every important result is saved in a file so it can be checked again.

No need to explain every box. The main point is that the work is split into small parts and each part has code or a written check behind it.

## Show the computer results

Open `PROJECT_STATUS.md`.

The main search was run at four levels. The sizes were 226, 406 and 2026 for the three larger modules. In every case the filters ended with zero matching candidates. The fourth level was also checked and no match was found.

Say:

> These are exact calculations. We are not using rounded numbers or a machine learning guess. The same scripts can run the checks again.

## Show what happened with the proof

Open `CURRENT_PROOF_SNAPSHOT.md`.

The reducible part started with 360 possible characters. The checks reduced this to four, then to one. The last one is named `(90,0)` in the files.

Say:

> This was a useful result by itself. The system did not only search. It found where the proof was still incomplete. It also caught a circular argument that looked tempting but was not allowed.

That circular issue is simple to explain. One computer result removes the last case, but the theorem needed to use that result already assumes irreducibility. So we cannot use it to prove irreducibility.

## The last open part

Open `P7_900_EISENSTEIN_NECESSITY_BRIDGE_AUDIT.md`.

The most promising route now is an Eisenstein series calculation. A key constant comes out as 16 over 15, which is good for the argument modulo 7. The remaining work is to check the same thing at every cusp and make sure the level and integral setup are exactly right.

Say:

> The good part is that the last problem is now small and clear. It is not a vague search anymore. We know which checks are missing.

## Logical proof audit

Open `LOGICAL_PROOF_AUDIT.md`. It checks the dependency direction, sufficiency of each lemma, and the rejected circular use of level `(2,2)` without rerunning the large matrix calculations. The verdict is: A–C closed in the current audit; D open at exactly `(90,0)`.

## What the AI actually did

Show the `scripts` and `data` folders.

The system:

- wrote arithmetic code
- made exact finite field calculations
- built and checked Brandt modules
- saved caches and certificates
- checked theorem assumptions
- found bad arguments and corrected them
- kept a list of what is proved and what is not

Say:

> The interesting part is not just that AI wrote code. It kept the math and the code connected, and it was able to say no when a proof step was not justified.

## Closing

End with this:

> We are not saying the full theorem is proved. We are showing a research system that took a hard open calculation from almost nothing to a very narrow final gap. The big searches are done, the results are repeatable, and the last missing argument is written down clearly.

## Questions judges may ask

### Did you prove the case?

No. The computer search is done, but one proof step is still open.

### What is the strongest result?

We reduced 360 possible reducible characters to one, and all four computer searches at the final levels found no matching candidate.

### Why should anyone trust the calculations?

They use exact arithmetic, saved input files, fixed scripts and repeatable checks. We still want an independent rerun before any paper claim.

### What did the AI do besides coding?

It checked theorem assumptions, found circular reasoning, kept track of failed ideas, and updated the proof status when something turned out to be wrong.

### What would finish the project?

A clean proof for the last survivor, then a final write-up connecting the theorem to the exact Brandt calculations.