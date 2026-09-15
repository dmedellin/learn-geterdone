# Subjects proposed for the future

A backlog, not a plan. Nothing here is scheduled and nothing here is designed.

Recorded because the operator named them and because several of them raise the
same question, which is worth answering once rather than seven times.

## The question they all raise

Every lesson in this library carries a lab, and that is not a convention — it is
enforced. `labs.build(key, cfg)` is unconditional in `scripts/mathpath/render.py`,
so a lesson without one does not render. And the labs are built on a specific
claim, the one each path's `material` clause makes to the reader: **every figure
is computed in the browser from the definition the lesson states**, in exact
rational arithmetic.

That claim is easy to keep for Algebra, Discrete Mathematics, System Design,
Algorithms and Operations Research, because those subjects are made of numbers.
It is not obviously keepable for a subject about how to organise notes.

So each proposal below is recorded with the only question that decides whether it
can be built the way this library builds things: **what does the reader compute?**
Where the answer is "nothing", that is written down rather than glossed, because
the alternative is a path whose labs are decorative — and a decorative lab is
worse than no lab, since it teaches the reader that the widgets are ornamental.

---

## PARA

A method for organising notes and files into Projects, Areas, Resources,
Archives.

**What the reader computes:** more than it first appears. A filing system is a
classification problem with measurable properties — how many items are
ambiguous between two buckets, how retrieval cost grows with archive size, how
often a "project" is really an "area" and what that misfiling costs when the
project ends. A lab could take a reader's own inventory of items and measure the
ambiguity rate rather than asserting the method works.

**Risk:** the honest version of this subject is short. PARA is four buckets and
one rule. Padding it to a course is how a path becomes ceremony.

## Zettelkasten

Atomic notes, densely linked, with no imposed hierarchy.

**What the reader computes:** this one is genuinely mathematical, and the
library already teaches the mathematics. A Zettelkasten *is* a graph. Link
density, orphan detection, connected components, the distance between two notes,
the degree distribution and whether it is scale-free, the cost of finding a note
by traversal against by index — every one of those is a Discrete Mathematics
`graphs-and-trees` lesson wearing different clothes, and the Algorithms path's
`graphkit` could serve it almost unchanged.

**The strongest candidate of the seven**, because the claim "a link is worth more
than a folder" is exactly the kind of assertion this library is built to make
measurable rather than repeat.

## Pomodoro

Fixed work intervals separated by fixed breaks.

**What the reader computes:** real arithmetic, and some of it is already on the
System Design path. Throughput over a day as a function of interval and break
length; the cost of an interruption as a resumption penalty, which is a queueing
question; the difference between a 25/5 split and a 50/10 split once the
resumption penalty is non-zero. There is a genuine counter-intuitive result
here — the optimum depends on the penalty, and for a large penalty *longer*
intervals win, which is the opposite of the method's folklore.

**Risk:** the evidence base for the specific numbers is thin. A lesson may
compute honestly from a stated model while the model itself is not well
supported, and the path would have to say so.

## Idioms and languages

**What the reader computes:** vocabulary frequency is Zipf, which the System
Design caching course already builds exactly (`zipfHit`, harmonic sums), so the
"learn the top 1000 words and understand 80% of speech" claim becomes a number
the reader derives rather than a slogan. Spaced repetition is a scheduling
problem with a real model behind it — the SM-2 interval recurrence, the
forgetting curve, the arithmetic of how many reviews a given retention target
costs.

**Risk:** the language content itself — idioms, usage, register — is not
computable and is the part a reader actually wants. This would be a path about
*how to learn a language*, not a language course, and it must not pretend
otherwise.

## Music

**What the reader computes:** the most natural fit on this list after
Zettelkasten, and possibly ahead of it. Intervals are frequency ratios; a perfect
fifth is exactly 3/2 and the library already carries exact rationals. Twelve
fifths against seven octaves is `(3/2)¹² = 129.746…` against `2⁷ = 128` — the
Pythagorean comma, an exact fraction that is not 1, which is *why* temperament
exists. Equal temperament is the twelfth root of two, an irrational the path
would print rounded and labelled exactly as the other paths do. Rhythm is
fractions. Additive and subtractive synthesis are sums.

This subject would exercise the existing `algebra_core` rational and surd
machinery almost unmodified.

## Biographies

**What the reader computes: nothing.** This is the one proposal that does not fit
the library as built, and it should be said plainly rather than engineered
around.

A biography path would need either a different page contract — one where a
lesson may have no lab — or labs that are decorative. The first is a real
architectural change affecting `render.py` and every guard that assumes a lab;
the second is worse than not shipping it.

There is a narrower version that does fit: a path about *reading* biography —
source reliability, how a claim is traced to a primary source, the arithmetic of
overlapping accounts. That is a subject about evidence, and evidence is
countable. But it is a different subject from the one named.

## Fields: magnetics and electrics

**What the reader computes:** a great deal, and the prerequisites mostly exist.
Coulomb and Biot–Savart are inverse-square sums; superposition is vector
addition; a resistive network is a linear system, which is Algebra's
`systems-and-matrices` and solvable by the exact machinery already shipped; a
circuit with sources and constraints is a linear program, which Operations
Research now has an exact simplex for.

**The honest obstacle:** the real treatment of fields is calculus — divergence,
curl, flux integrals — and this library refuses calculus everywhere. That refusal
has been productive so far (EOQ by discriminant, extrema by vertex, every
scheduling rule by exchange), but fields are where it bites hardest. A
discrete-and-algebraic treatment is possible and would be genuinely useful; it
would also have to be explicit that it stops short of Maxwell, in the same way
the Algebra path says it stops short of convergence tests.

---

## If one of these is picked up

The process that produced System Design, Algorithms and Operations Research is
recorded and repeatable: an advisor pass produces a curriculum spine, a
reconciliation pass reads it against every existing path for duplication and
contradiction, and a final build specification names every lesson, its one hard
idea, its misconception and its lab mode before a line is authored.

Read `AGENTS.md` §0 for what is currently unfinished, and do not start a seventh
subject while two are half-built.
