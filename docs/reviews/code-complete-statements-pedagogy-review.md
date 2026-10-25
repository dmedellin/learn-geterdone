# Pedagogy review: Course 4, Statements (`code-complete-statements`)

Reviewed 2026-10-25 on branch `feat/code-complete-subject`, against the
`pedagogical-expert` brief, `docs/code-complete/PLAN.md` (§0, §B, the Course 4
entries of §C, §E.4, §F), `docs/code-complete/AUTHORING.md`, and my own
pre-authoring review (`docs/reviews/code-complete-spec-pedagogy-review.md`).
All seven lessons were read in full (`content/code_complete/c4_statements/`,
`__init__.py`, `part_a.py`, `part_b.py`). The course was rendered with
`scripts/preview_subject.py` (final line `OK`; 7 pages, 7 with pinned figures,
0 failing), every page was opened in Playwright at 390 px and 1280 px, and
every lab was driven with the exercise's own input: the `printQuote` rewrite,
the router frequencies, the `i -= 3` header, `factorial(21)` and
`fibonacci(5)`, the shipping table under both rules and a key past the top,
the owner condition and two wrong rewrites, `discountPercent`, and three
versions of `refundAmount`. The spoken forms (`data-say`) of every code block,
key line and worked line were read. Where a finding rests on what the book
says, the page was checked with `ccbook.py`; nothing from the text is
reproduced here.

## Verdict

This is a sound course, and the best-shaped of the three families of lab in
the Subject so far: every lesson teaches an act a working programmer can do
tomorrow on their own code, every exercise is applied and has one answer that
the lab reproduces, every answer sits only in a quiz `why`, every `worked`
works a preset and never the exercise, and the opening scenes are rationed to
three of seven (Straight-Line Code, Loops, Nesting). The pre-authoring
findings that touched this course are all taken: the chain with no final
`else` (#8), the guard-clause rewrite of `refundAmount` (#8, #22), `lpAfter`
as `mistakes[1]` (#19), "a count of 11" as `mistakes[1]` (#19), the
decision-point rule stated in every stem that needs it (#26), no quiz that
offers an equivalent rewrite as a distractor (#26), one Python constant per
snippet (#27), the `-1.0` sentinel named in a clause (#29), the depth
convention stated in the banner and the two listings stacked on a phone (#32),
and the `goto` history in a late `p` as the course's one modern aside (§F.4).

Three things need fixing before it ships. The guard-clause transformation,
which Unusual Control Structures sets as its exercise, is described in that
lesson and never once shown; the reader meets the before/after only in the
next-but-two lesson's presets. The Straight-Line exercise tells the reader to
keep the rewrite "to five lines", which is impossible as written (header, four
statements and a brace are six), and the quiz's answer depends on the line
numbering the instruction confuses. And the course promises, in three places,
that its last lesson "gathers the counts of the others into one", and the
lesson's body never does the gathering. The rest is should-fix wording and one
weak quiz item.

## Lesson by lesson: does it teach an act?

| lesson | the act | shown | practised | answerable | own-code step |
| --- | --- | --- | --- | --- | --- |
| organizing-straight-line-code | list i → j dependencies; make a hidden order visible in parameters | `in-order` worked; three presets in prose | `printQuote` rewrite | yes, lab reproduces `1→2, 1→3, 1→4, 1→5, 2→3, 3→4, 4→5` | paste a routine; name the dependency the arrows miss |
| using-conditionals | price a chain by frequency; find what falls through | `as-written` worked; three presets | router (a) and `route` (b) | yes, lab gives `11/4 = 2.75`, `5/4 = 1.25` | type own chain with frequencies, say where they came from |
| controlling-loops | read iterations, last value, value after from a header | `fencepost` worked; four presets | `i -= 3` header | yes, lab gives 4, 1, −2 | four own headers |
| unusual-control-structures | rewrite nested `if`s as guards; count a recursion against its loop | recursion worked; **guard rewrite never shown** (finding 1) | `refundAmount` | yes, the Nesting lab gives 3/3 and depth 2 → 1 | one own routine, rewritten |
| table-driven-methods | look up under an endpoint rule; count both searches | `days-20` worked; four presets | shipping table, 5 kg | yes, lab gives 15 (3, 2) and 9 (2, 3) | one own `if` chain as a table, with its rule |
| boolean-expressions | truth-table equivalence; DeMorgan | three conditions on four rows worked | `!(isAdmin || !isOwner)` | yes, lab says equivalent on 4 rows | one own negated condition, checked |
| nesting-and-complexity | count decision points and depth; see what moves | `nested-shipping` worked; two presets | `discountPercent` | yes, lab gives 7, `1 + if 3 + for 1 + && 1 + || 1`, depth 2, line 11 | most-nested own routine |

Every "Do" names an act, every `standard` measures it without the lab, and
the misconceptions are the chapter's refutations with the lab's figures said
to be "on the lesson's illustration" where they appear. Prerequisite order
holds: lesson 4's exercise asks for decision points and depth, and states the
rule inside the exercise paragraph before lesson 7 formalises it; lesson 7's
`guard-clauses` preset is the transformation lesson 4 practised.

## Findings

### Must-fix

**1. `unusual-control-structures`: the guard-clause rewrite is the exercise and
is never demonstrated.** *Where:* body paragraphs 2 and 7, `steps` 1–3, the
`refundAmount` exercise. *What is wrong:* §17.1 is paraphrased ("early returns
that check the error cases first… otherwise the nominal path ends up indented
inside every check"), the steps say "write its negation as an if at the top",
and then the reader is asked to perform the transformation on `refundAmount`
with no before/after in front of them. The worked example is the recursion
count; the two code blocks are both Fibonacci. The only demonstration of a
guard rewrite in the course is lesson 7's `nested-shipping` → `guard-clauses`
pair, three lessons on. A lesson that explains and never demonstrates is
incomplete by the brief's own rule, and this is the one lesson in the course
where that happens. *Change:* add one short snippet constant and one `p`
before "Now the counting" (body goes from 14 to 16 blocks, inside the 7–18
range), a different instance from the exercise so the exercise stays the
reader's:

```python
FIRST_LINE_GUARDED = """String firstLine(File file) {
    if (file == null) {
        return "";
    }
    if (!file.canRead()) {
        return "";
    }
    return readFirstLine(file);
}"""
```

and the `p`: "Here is the transformation on a small routine written for the
lesson. The nested version wrapped `return readFirstLine(file);` in
`if (file != null)` and, inside that, `if (file.canRead())`, with
`return "";` after both. Each enclosing condition becomes its own negation at
the top, returning what the routine returns when it fails, and the nominal
case ends the routine unindented:" followed by the `code` block. Then one
sentence after it: "Count it as the exercise will ask you to: two `if`s
before and two after, 1 + 2 = 3 decision points either way; the deepest
statement was inside two `if`s and is now inside one." That sentence is the
faded step between the demonstration and `refundAmount`, and it makes
`steps` 1–3 a summary of something the reader has seen. (If the author
prefers the inline route, the nested form can be a second constant and a
second `code` block, at 17 blocks; the single-block version above is enough.)

**2. `organizing-straight-line-code`: "Keep the routine to five lines" cannot
be done, and the quiz answer depends on the line numbering it muddles.**
*Where:* the exercise `p`; quiz item 2. *What is wrong:* `printQuote` as
listed is six lines (header, four calls, closing brace; the lab's listing
numbers the brace 6). A rewrite with a header, four statements and a brace is
also six. A reader who obeys "five lines" either drops the brace or puts two
statements on one line, and a reader who wraps the long `addInsurance` call
over two lines (`Rates withInsurance =` on line 4, the call on line 5) gets
`1→2, 1→3, 1→5, 1→6, 2→3, 3→5, 4→6` from the lab and is marked wrong by a
quiz whose `why` gives `4→5`. I drove the lab with the
six-line version (header, four statements each on one line, brace) and it
prints exactly the pinned answer, so the answer is right under one layout and
the instruction does not name it. *Change:* replace "Keep the routine to five
lines." with "Keep each of the four statements on its own line, so that they
are still lines 2 to 5 and the line numbers in your list match the
listing's." And in quiz item 2's stem, after "`print` takes the last", add
"with the four statements still on lines 2 to 5".

**3. The course promises a synthesis its last lesson does not perform.**
*Where:* `how_to[3]` ("the routine it counts has dependencies, a chain, a loop,
guard clauses and compound conditions, and its decision points add up what
the earlier lessons counted one structure at a time"), `summary`'s last
clause, and `nesting-and-complexity`'s `concepts_intro` ("gathers the course's
counts into one"). *What is wrong:* the lesson body counts `nested-shipping`
and `guard-clauses` and never once names an earlier lesson's count in the
routine. `nested-shipping` has no `if-else-if` chain either (it is nested
`if`/`else`, which is the opposite shape), so "a chain" is not in the routine.
A reader who was told the course builds to this lesson arrives and finds a
count like the others. *Change:* (a) in `how_to[3]` replace "has dependencies,
a chain, a loop, guard clauses and compound conditions" with "has a loop, two
compound conditions and, in its second version, guard clauses"; (b) add one
sentence to the body after "looking shows the domestic rules buried four
levels down.": "The structures the earlier lessons read one at a time are all
here: the `for` on line 12 is a header Controlling Loops would read, one pass
per item; the `&&` on line 6 and the `||` on line 13 are the compound
conditions Boolean Expressions compared row by row, and each counts one; and
the `guard-clauses` version below is the transformation Unusual Control
Structures made on `refundAmount`, now on a routine where it moves a loop as
well." That is the gathering the `how_to` promises, in one sentence, and the
block count does not change.

### Should-fix

**4. `unusual-control-structures`, quiz item 1 `why`: "Both versions have two
`if`s" is false for the better rewrite.** The lesson's own model of a guard
clause, lesson 7's `guard-clauses` preset, combines two error cases into one
`if` with `||` (`order == null || order.weight() <= 0`). A reader who does the
same for `refundAmount` (`if (!order.isPaid() || order.daysSinceDelivery() >
30)`) has one `if` and one `||`; I pasted that version into the Nesting lab
and it prints `1 + if 1 + || 1` = 3, depth 1. The correct option ("stay at 3;
nesting falls from 2 to 1") still holds, but the `why` tells that reader their
count is wrong. *Change:* "Both versions have two `if`s, so 1 + 2 = 3 decision
points before and after" → "The nested version has two `if`s; the guard
version has two `if`s, or one `if` and one `||` if you joined the two guards,
and either way the count is 1 + 2 = 3 before and after".

**5. `controlling-loops`, quiz item 2 is the worked example's own number.**
"How many times does `for (int i = 0; i <= 10; i++)` run?" is answered in
the body, the worked example, the `fencepost` preset and `mistakes[0]`. It
tests nothing. *Change:* a header not on the page, with the same shape of
distractors: "How many times does `for (int i = 1; i < 10; i += 3)` run, and
what would an `i` declared before it hold afterwards?" Options: "3 times; 10
after" (correct: 1, 4, 7; the next value, 10, fails `< 10`), "3 times; 7
after" (last value for value after), "4 times; 10 after" (counts 10 as a
pass), "3 times; 9 after" (assumes the index stops at the bound). The `why`
names the three values and the step past.

**6. `using-conditionals`: the worked example's intro contradicts the
listing.** The `worked.intro` says the as-written preset has "no final else",
and `mistakes[0]` and the body treat the chain as the `classify` listing,
which ends with `return "unexpected";`, the error trap the quotation asks for.
A careful reader asks why the trap costs nothing. *Change:* `worked.intro` →
"Take the as-written preset: server error 5, client error 10, redirect 15,
success 70, in that order. The listing's `return "unexpected"` after the
chain is the error trap; in the illustration no status reaches it, so it
costs no tests."

**7. `boolean-expressions`: two wordings.** (a) "Two more presets show
DeMorgan used to simplify" introduces `redundant`, which is not DeMorgan
(`(found && valid) || (found && !valid)` collapses by distribution, not by
negation). *Change:* "Two more presets show the truth table used to
simplify." (b) Quiz item 4's stem, "How does Section 19.1 tell you to apply
DeMorgan's theorems to an and or an or and a pair of operands?", does not
parse aloud. *Change:* "Section 19.1 gives a three-step recipe for applying
DeMorgan's theorems to a compound condition. What are the steps?"

**8. `table-driven-methods`: the exercise's words are not the lab's tokens.**
The exercise asks for "the first step whose top it is at or below" and then
"check both in the lab"; the rule field accepts only `below` and `atmost`,
and typing "at or below" produces the kit's refusal ("A step holds keys below
or atmost its bound should be one of below, atmost, not "at or below""). The
body names `<code>atmost</code>` once, five paragraphs earlier. *Change:* in
the exercise `p`, "then check both in the lab" → "then check both in the lab,
with the rule typed as `below` and then `atmost`". Also `steps[2]`: "the
answer is that step or below, otherwise above" uses "below" in the sense the
rule name uses it the other way; → "the answer is that step or an earlier
one, otherwise a later one".

### Consider

**9. `organizing-straight-line-code`'s `standard` says "for six statements"**
and no six-statement instance exists on the page; the exercise has four. Say
"for a routine of about six statements of your own" so the reader knows where
the instance comes from.

**10. `unusual-control-structures`'s key line "recursive Fibonacci: 2·F(n + 1)
- 1 calls"** is read "2 times F of n plus 1 minus 1 calls", which a listener
hears as 2F(n) + 1 − 1. "calls: twice F(n + 1), less one" is unambiguous.

**11. The §F.4 aside in `unusual-control-structures`** adds a claim of the
lesson's own ("large C programs still use a forward `goto` to a single
cleanup label"). It is true of well-known code bases, and it is allowed in
the aside, but it is the one unsourced present-tense claim in the course;
"some large C programs" costs nothing.

**12. Load.** `using-conditionals`' second paragraph is a 130-word list of
§15.1's guidelines; it reads as a checklist, which `not_covered` says the
lessons do not reproduce. Cutting "Consider whether an `if` needs an `else`,
test the `else` too, and check that the two clauses have not been reversed"
to "and the section's remaining guidelines on the `else` clause are three
checks worth reading in your copy" lightens it without losing the argument.
The course's heaviest page, `nesting-and-complexity`, is 2,682 words
including chrome, and reads in about fifteen minutes; none of the seven would
pass twenty.

**13. `controlling-loops`'s `lpInCmp` wants `gt`, not `>`.** The exercise
says so, and the refusal ("should be one of lt, le, ne, gt, ge, not ">"") is
clear. Nothing to change; recorded so nobody reports it as a defect.

## The quiz distractors, argued

Every item was checked for the §E.4 rule: options differ on an integer, a
row, a line or a section's claim, and the `why` names the difference.

- **Straight-Line 1** (line 5 depends on): "1, 2, 3, 4" is the reader who
  thinks every line reads the parameter; "4 only" is the reader who counts
  only the line just before; "1 only" confuses the parameter with the
  dependency. All refuted by the `why`. Sound.
- **Straight-Line 2** (the rewrite): "1→2, 1→3, 1→4, 1→5" is the routine
  before the rewrite; "2→3, 3→4, 4→5" forgets that every call still reads
  `quote`; "1→2, 2→3, 3→4, 4→5" is the reader who thinks only `loadRates`
  reads the parameter. Sound, given finding 2.
- **Straight-Line 3** (which fails to compile): each option names one
  listing with a reason; "all three are legal" is the holder of
  `mistakes[0]`. Sound.
- **Straight-Line 4** (§14.2): frequency ordering is Chapter 15's advice,
  alphabetical order is §15.2's for equal cases, declaring at the top is
  Chapter 10's target; the `why` says which chapter each belongs to. Sound.
- **Conditionals 1** (router): "2; 2" is the unweighted average; "2.75;
  2.75" thinks reordering changes nothing; "3; 1" is `GET`'s own cost in each
  order. Each is a distinct wrong method. Sound.
- **Conditionals 2** (`PATCH`): "Java throws" and "`javac` rejects" are what
  a reader coming from a stricter language expects; "handled by the last
  branch" is the reader who thinks the last `else if` is an `else`. Sound.
- **Conditionals 3** (why 0.20): "the lab charges the else no tests" is
  wrong by the lab's stated rule; "not mutually exclusive" is `mistakes[2]`
  misapplied; "never more than one test" is refuted by `as-written`'s 2.
  Sound.
- **Conditionals 4** (default clause): "most common case" and "last real
  case" are the two uses §15.2 argues against; "clearer without one"
  contradicts the quotation. Sound.
- **Loops 1** (`i -= 3`): each wrong option is a named error (stops a pass
  early; last value for value after; value after for last value). Sound.
- **Loops 2**: see finding 5.
- **Loops 3** (never ends): the other three headers are traced in the `why`
  to 5, 5 and 5 passes. Sound; the `!= 10` option is a good near-miss.
- **Loops 4** (index after the loop): "rely on it" is the misconception;
  "declare it before" and "reset it" are plausible habits the section does
  not recommend. Sound.
- **Unusual 1** (guard rewrite): "3 to 1; 2 to 0" is the reader who thinks
  guards do not count; "rise to 4 for the extra return" is the reader who
  counts `return`; "stay at 2" is the reader who did not flatten. Sound,
  with finding 4.
- **Unusual 2** (calls): 30 is the depth, 832,040 the value, 1,346,269 is
  F(31) before doubling; the `why` says so. Sound.
- **Unusual 3** (§17.2 on Fibonacci): "use it because the definitions are
  recursive" is `mistakes[0]`; "with a safety counter" misapplies a tip;
  "only without loops" is a straw option but a checkable claim. Acceptable.
- **Unusual 4** (argument for `goto`): "always faster" is contradicted on
  p. 398; "Dijkstra recommended it" and "Java includes it" are false facts
  the `why` names. Sound.
- **Tables 1** (5 kg): the three distractors swap the values, the binary
  counts, or deny the rule matters; each differs on an integer. Sound.
- **Tables 2** (14 days, below): 2 is the `atmost` answer, 0 and 10 are
  neighbours. Sound.
- **Tables 3** (16 steps): 5 is ⌈log₂ 16⌉ + 1, the off-by-one of the
  halving; 8 and 16 are halves. Sound.
- **Tables 4** (three accesses): the distractors are plausible triples from
  other vocabularies. Sound.
- **Boolean 1** (`!(isAdmin || !isOwner)`): each wrong option differs on a
  named row, and the equivalent rewrite `isOwner && !isAdmin` is correctly
  absent. Sound.
- **Boolean 2** (where they disagree): "only F, F" and "only T, T" are the
  single rows a hasty table gives; "equivalent" is `mistakes[0]`. Sound.
- **Boolean 3** (division by zero): the option with the test second divides
  first; the `&` and `|` options evaluate both sides. Sound.
- **Boolean 4**: see finding 7(b) for the stem; the options are the three
  partial applications. Sound once reworded.
- **Nesting 1** (`discountPercent`): 6 drops the starting 1, 5 drops the
  operators, depth 3 counts the routine's braces; the `why` names each.
  Sound.
- **Nesting 2** (why 9 → 6): "guard clauses count less" and "a condition
  that returns is not counted" are the two wrong models of the rule;
  "removed three conditions" is `mistakes[0]`. Sound.
- **Nesting 3** (8 points): bands as the book prints them; "rewrite before
  it is used" is a verdict no band gives, and the stem names the table.
  Sound, and F14 is settled.
- **Nesting 4** (Böhm and Jacopini): the distractors each include a
  construct structured programming set out to remove or restrict. Sound.

## Voice, load and the read-out

- **Voice** is the §F contract throughout: the chapter first in paraphrase
  that says whose claim it is, "you" warmly, McConnell presented and not
  endorsed (his "small margin" verdict on guard clauses on p. 393 is given at
  that strength; the Aztek remark is his own light remark, within the
  quotation budget at 21 + 17 words). The one story with people in it is the
  `goto` history, once, in the lesson §F.4 names. The "numbers are other
  people's" sentence appears where it should (loop length and nesting,
  p. 385; the three-levels finding, p. 445; the bands, p. 458). No slang, no
  "let's", no verdicts on code.
- **Load** is one hard idea per lesson except Unusual Control Structures,
  which the plan itself gives two acts and the history; finding 1 is what
  makes the first of those acts teachable at that load.
- **The read-out** works. Every code block is spoken with its line numbers
  ("line 2, flagged, double total is set to base plus surcharge plus
  insurance"), `&&`, `||` and prefix `!` are "and", "or" and "not", brackets
  that group are spoken ("not, open bracket, done or error, close bracket"),
  `i -= 3` is "i is decreased by 3", `hourly[i]` is "hourly at index i",
  `int[]` is "array of int", `-1.0` is "minus 1.0", and the dependency tiles
  read "1 goes to 3". The nesting lesson's visual point (depth) is carried
  in words in the body ("first reached on line 14, the `return -1.0;` inside
  the restricted-item check") and the flagged line is announced. The only
  spoken ambiguity found is finding 10.
- **In the browser.** At 390 px no page scrolls horizontally; code blocks,
  the lab listing and the lab tables scroll inside their own boxes, the
  textarea and the numbered listing stack, and the marked line carries a
  gutter arrow, not colour alone. No console errors on any page at either
  width. Every lab accepted the exercise's input and printed the pinned
  answer; the kit's refusals (`factorial(21)`, a `>` where `gt` is wanted, a
  rule in words) are clear sentences.

## What is right and should not be changed

- `controlling-loops`: the clearest lesson in the course. One character
  changes three figures, `skips-the-bound` is the quotation's own case, and
  the two misconceptions are exactly the two the pre-authoring review asked
  for.
- `using-conditionals`' `mistakes[2]` (reordering a chain of range tests),
  which is the real hazard of the chapter's advice and which the lab's
  `panel_intro` admits it cannot check.
- `table-driven-methods`' two `days-60` presets and the exercise's "say what
  the two arrays leave unstated": the endpoint rule as a business decision is
  the chapter's point made concrete.
- `boolean-expressions`' `half-demorgan` and the `drain` listing, where the
  same question is asked twice in two forms on lines 4 and 7.
- `nesting-and-complexity`'s `mistakes[0]` with p. 458, and the sentence
  "Whether 6 is worth simplifying further is your judgement".
- The honesty of every `note`: what each lab cannot see, said plainly.

## Summary of must-fix findings

1. **`unusual-control-structures`**: the guard-clause rewrite is the
   exercise and is never demonstrated; add the `firstLine` before/after block
   and its one-sentence count before the recursion lab (finding 1).
2. **`organizing-straight-line-code`**: "Keep the routine to five lines" is
   impossible as written and the quiz answer depends on the layout; say
   "each of the four statements on its own line, lines 2 to 5" (finding 2).
3. **The course's promised synthesis**: `how_to`, `summary` and the last
   lesson's `concepts_intro` say Nesting and Complexity gathers the earlier
   counts, and the body does not; add the one gathering sentence and drop
   "a chain" from `how_to` (finding 3).

Should-fix findings 4–8 are wording and one quiz item; none changes a
snippet, a preset or a pinned figure except finding 1, which adds one new
snippet whose figures (3 decision points, depth 1) I checked in the lab.
