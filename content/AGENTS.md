# content/ — the data the generated paths are rendered from

Root `AGENTS.md` applies. This adds what is specific to this directory.

`content/discrete_math/` and `content/algebra/` are the SOURCE. The pages under
those course slugs in `site/` are output — **editing a published page there is
reverted by the next build**, so the change appears to work and then vanishes.

Model: **balanced tier** (`gpt-5.6-terra`, or `codex -p build`). Volume work with
real gates behind it — `mathcheck.js` and `labcheck.js` will catch an arithmetic
or lab-mode mistake, which is why this does not need the frontier tier.

## Shape a lesson to what the renderer draws

Three concepts, four method steps, three mistakes, with a little room where a
lesson earns it. `TestLessonDataMatchesTheRenderer` enforces the range. A lesson
supplying two concepts still renders — lopsidedly, on one page out of hundreds.

## The two failures that keep recurring

**A distractor that is also true.** `3/√3` and `√3` are the same number;
`aₙ = 2n−1 for n ≥ 1` and the same rule with an explicit `a₁` describe the same
sequence. Before committing a question, try to argue for each wrong answer. If
you can, rewrite it.

**A lab mode that does not exist.** A lesson naming an unknown mode silently
renders the lab kit's default — the page looks finished and teaches the wrong
thing. `labcheck.js` catches this.

## Adding a lesson

Add the dict, run `python3 scripts/build_paths.py`, then add the URL to the five
declarations named in root `AGENTS.md` §1. The suite tells you which are missing.

## Write math a voice can read

Lessons can be read aloud. `scripts/mathpath/speech.py` turns every math run into
words at build time, and a few shapes of notation are ambiguous to it as they
would be to a listener. Write new math so the reading is not a guess:

- **Write a product as a product.** `λ·(r + 1)`, `p·(1 − p)`, `n·(n + 1)` — a
  letter touching a bracket is read as a function: `x(t)` is "x of t". Leave
  `f(x)`, `P(A)`, `T(n)`, `Θ(n)` and the like as they are.
- **Write the multiplication between a group and a function.** `(n/2)·log₂ n`,
  not `(n/2) log₂ n`.
- **Bracket a fraction's denominator** when anything follows it: `3/(2x)` or
  `(3/2)·x`, never `3/2x`.
- **A table is a display block, not a line of prose.** `(1,1)=5 (1,2)=10 …`
  written along one line is read as a run of numbers; put it in a `math` block
  with one cell per column and it is announced as a table instead.

When the notation must stay as it is, give the run a spoken form in
`content/<subject>/spoken.py`, keyed by the exact run text:

    SPOKEN = {
        "λ(1 − π₅)": "lambda times the quantity 1 minus pi sub 5",
    }

It lives beside the course modules rather than in them, so it never moves the
content-preservation hashes. `python3 scripts/speechcheck.py` lists the runs
still guessed at; `tests/test_speech.py` fails while any are, and when a spoken
form outlives the math it was written for.
