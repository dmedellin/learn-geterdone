# Pedagogy review: Course 7, Software Craftsmanship (`code-complete-software-craftsmanship`)

Reviewed 2026-10-25 on branch `feat/code-complete-subject`, against the
`pedagogical-expert` brief, PLAN §0, §B, §C (Course 7), §E.4 and §F,
`docs/code-complete/AUTHORING.md`, and my pre-authoring review
(`docs/reviews/code-complete-spec-pedagogy-review.md`). All four lessons of
`content/code_complete/c7_craftsmanship/part_a.py` and the course dict were
read whole. The course was rendered with `preview_subject.py` (final line
`OK`; 4 pages executed, 4 with pinned figures, 0 failing), served locally and
driven in Playwright at 360 px and 1280 px: every preset of every lab loaded,
each lesson's exercise entered into its lab (`clamp`, `isLeapYear`, the
2-hour script with an automated time of 0 and 5 runs a week), the break-even
lab probed at its edges (automated time equal to or above the hand time, 0
runs a week, `1/4` and `0.25`, a build of 0.5 hours), the layout lab probed
with the shapes a reader's own routine will have (two-space indentation,
tabs, an unbraced `else if` chain, an unbraced `for`, braces on their own
line, a continuation line), and the size lab with a block comment. No page
error, no horizontal scroll at 360 px; the lab's listing stacks under the
textarea on a phone, and a flagged line carries a gutter glyph and the word
"mis-indented". The code read-out was run over every key line, worked line,
backtick run and the page's math spans (`speech.say_code`); every `&&`, `||`
and `/` comes out as "and", "or" and "divided by", and nothing is spelt. The
four opening quotations check `OK` with `cc_quotes.py` (15, 22, 23, 27
words). Facts the findings rest on were checked against pp. 737, 749,
781–785, 830, 848 and 852 of the text; nothing from the text is reproduced
here.

## Verdict

The course teaches. Each lesson sets out the chapter in paraphrase that says
whose claim it is, then turns to a snippet written for the lesson and does
one act on it that the chapter asks for: find the lines whose indentation
disagrees with Java's structure and say what the compiler does; count and
sort a routine's comments; price a tool; count decision points and nesting
and name the theme a change serves. The material clause holds throughout ("a
count is a reason to look"), the Commento's voices are kept apart from
McConnell's, the modern aside sits in a late paragraph and not in
`mistakes[0]`, the numbers are other people's and are said to be, and every
lesson ends by sending the reader to their own code with an observable
result. Of the pre-authoring findings that touched this course, #3 (own-code
step), #12 (density per statement), #17 (the indentation misconception), #31
(the listing's evidence stated in words; gutter marker), #32 (stacking on a
phone) and #33 (the answer in one quiz `why`) are all taken.

Three things need fixing before it ships. The layout lesson's own-code step
tells the reader to let an editor re-indent their routine before pasting it,
which removes exactly what the lab checks, and a reader who pastes two-space
code instead gets every indented line flagged with no hint why. The last
lesson's first quiz item, the one that carries the exercise, asks for figures
the page states three times, so it is a lookup rather than a retrieval. And
the comments lesson's first misconception states the exercise's answer. The
rest is should-fix and consider.

## A. Does each lesson teach a working programmer to do something?

**`layout-and-style`.** Yes. The act is real and it is the chapter's: work
out each line's depth from the structure Java reads, compare it with the
indentation, and say what runs. The three presets are well chosen, each one
a different failure (an `else` bound to the wrong `if`; a second statement
that only looks governed; the braced version, where the count is 0 and the
prose says what 0 does not mean). The body states the binding in words for a
listener, as #31 asked. The `clamp` exercise is the best thing in the course:
the mis-indented statement is a `return`, so the compiler catches it, and the
quiz `why` says that with any other statement nothing would. Lab checks:
`clamp` gives Mis-indented lines 1, Which 6, as the `why` says; an unbraced
`else if` chain, an unbraced `for`, braces on their own line and a
continuation line all give 0, so a reader's ordinary routine is not flagged
for its style.

**`self-documenting-code`.** Yes. Counting is the lab's; sorting by kind is
the reader's, and the lesson says so three times (panel, steps, note). The
two presets with the same statement count and opposite comments make the
point the chapter makes, and `isLeapYear` extends it: the same density as
`comments-repeat` with every comment earning its place. The block-comment
probe gives 3 comment lines over 5 statements and a status line that says one
line "carries code and a comment and counts as both", so the lab explains
itself on a reader's own code.

**`personal-character`.** Yes, within what the chapter allows. The chapter
has no count, the lesson says so in the concept, the body, the panel and the
note, and the model is small enough to do by hand. The lab is honest at its
edges: an automated time equal to or above the hand time prints "A run by
hand must take longer than an automated run, or the tool never pays back";
0 runs a week is refused in a sentence; `1/4` and `0.25` both work. Step 5
("double your estimate of the build time") is a genuine act and the lab
supports it (2 h → 24 runs, 4.80 weeks; 4 h → 48 runs, 9.60 weeks, 17.67 h).
The chapter's traits are paraphrased at the book's strength, and §33.7's
three kinds of laziness are as p. 830 gives them.

**`themes-of-craftsmanship`.** Yes. The lesson does what the PLAN's capstone
promised: two of the book's counts on one routine, and the themes named for
the two improvements the counts point at. `retry-delay` is a good choice
(inside both warning signs, and still improvable), and `nested-shipping`
brings a routine the reader has met back for comparison. The `else if` and
`do … while` probe counts as the stated rule says (an `else if` is an `if`;
the `while` of a `do` counts; `?:` is not counted and the banner says so).

## B. Are the exercises applied and answerable?

- **7.1 `clamp`:** applied, determinate, answered once (quiz 3's `why`), and
  checked in the lab. Nothing else on the page gives the lines. Good.
- **7.2 `isLeapYear`:** applied and determinate for the counts. One problem
  with the classification (finding 5) and one leak (finding 3).
- **7.3 the 2-hour script:** arithmetic, as §C says, and the chapter has
  nothing else; answered once (quiz 1's `why`); the lab confirms 24, 4.80,
  59/3. Acceptable.
- **7.4 the reader's own routine:** the right capstone. The fixed answer is
  carried by quiz 1 on `retry-delay`, and that is where it fails (finding 2).

## C. Findings

### Must-fix

**1. `layout-and-style`, step 5: the own-code step destroys its own
evidence, and the lab gives no hint when the indent width is the cause.**
*Where:* `steps[4]`: "Paste a routine of yours into the lab, re-indented at
four spaces a level if your team uses another width (an editor will do
it)." *What is wrong:* an editor re-indents to the structure it parses, which
is the structure Java reads. Run on the dangling-else preset it would move
the `else` to eight spaces and `sendLetter` to twelve, and the lab would then
report 0. So a reader who follows the step as written pastes a routine the
editor has already corrected, and the count is 0 by construction; the step
measures nothing. A reader who ignores the advice and pastes two-space code
gets, as the probe shows, "4 lines are indented other than the structure
Java gives them … lines 2, 3, 4, 5", every indented line, and nothing on the
page tells them why. (Tabs are accepted silently: a tab-indented routine
reports 0 with no note, which is the opposite surprise.) *Change:* replace
`steps[4]` with:

> **Check a routine of your own.** Paste a routine of yours into the lab. If
> your team indents by two spaces, widen it first with a search-and-replace
> that turns each pair of leading spaces into four, and not with your
> editor's re-indent command, which would move every line to the depth Java
> reads and hide exactly what you are checking. If every indented line is
> flagged, the width is the cause. Note the Mis-indented lines count, and
> for each flagged line write one sentence on what Java does with it and
> whether that is what you meant.

Add one sentence to the `note`, after "at four spaces a level, and nothing
else": "Code indented by two spaces or by tabs must be widened to four
spaces first, by replacement and not by re-indenting." *Kit gap to report:*
the `layout` view could say in its status line, when every indented line
disagrees, that the width may be the cause; and it should say what it does
with a tab.

**2. `themes-of-craftsmanship`, quiz 1 is a lookup, and it is the item that
carries the exercise.** *Where:* quiz 1 asks for `retry-delay`'s decision
points and depth. The body paragraph after the listing gives "7 decision
points … The deepest nesting is 2, first reached on line 9"; the worked
example gives "1 + 3 + 1 + 2 makes 7 … deepest nesting 2, first on line 9";
the lab's default preset shows 7 and 2 on load. §C chose this item so that
the lesson "has one" fixed answer, and §E.4 item 3 rightly requires the
preset's figures in the body, so the two rules collide and the item tests
whether the reader scrolled. The distractors' diagnoses ("six forgets the
starting 1; depth 3 counts the routine's own braces; five leaves out `&&` and
`||`") are good and should be kept; what is missing is a count the page does
not print. *Change:* make the item a transformation of the preset, which the
reader can only answer by applying the rule:

> **q:** The retry-delay preset's loop caps the delay with an if on lines 8
> to 10. Suppose line 7 became `delay = Math.min(delay * 2, 10000);` and
> lines 8 to 10 were deleted, nothing else changing. By the lab's rule (1
> plus each if, while, for, case, && and ||; depth is brace depth below the
> routine's own braces), what would the lab count?
> **a:** "6 decision points, deepest nesting 1" (correct); "7 decision
> points, deepest nesting 1"; "6 decision points, deepest nesting 2"; "5
> decision points, deepest nesting 1".
> **why:** The if on line 8 is gone, so 1 + if 2 + for 1 + && 1 + || 1 = 6,
> still in the band 6–10; `Math.min` is a call, not a branch, and adds
> nothing. The deepest line is now the loop body at depth 1, since the if
> that reached depth 2 is gone. Seven keeps the deleted if; depth 2 keeps
> its braces; five drops the `||` as well. On the preset as it stands the
> lab shows 7 and 2, and the method is the same on a routine of your own.

The `standard` can stay on the 16-line routine as the PLAN asks, but add
"without looking at the lab or the worked example" so that it is a standard
and not a transcription.

**3. `self-documenting-code`, `mistakes[0]` states the exercise's answer.**
*Where:* "The exercise has the same density as comments-repeat with every
comment useful." *What is wrong:* §B and §E.4 item 4 put the exercise's
answer in one quiz `why` "and nowhere else on the page, so the reader commits
to an answer before seeing it". This sentence gives both halves of the answer
(100%, no repeats) two screens below the exercise. §C's Misconception line
prescribed it, so the author followed the plan; the plan's own rule is the
one to keep. *Change:* replace the sentence with: "A routine can match that
density with every comment earning its place, and the count would not tell
you; the exercise asks you to find out which kind `isLeapYear` is." Correct
the §C line the same way.

### Should-fix

**4. `layout-and-style`, steps 2 and 3 do not say what depth an `else`
sits at, and a reader following step 3 literally reaches depth 4 for line
6.** *Where:* step 3: "Count the braces open above the line, add one for
each unbraced control line that governs it." *What is wrong:* for line 6 of
the dangling-else preset a reader counts the routine's brace (1), the `if`
on line 2 which governs lines 3 to 6 (2), the `if` on line 3 whose statement
includes the `else` (3), and the `else` on line 5 (4): sixteen spaces, where
the worked example says twelve. The worked example resolves it ("line 3:
unbraced if, governs line 4; its else is line 5") but the step should not
need it. *Change:* step 2 ("Pair each else with its if") gains a last
sentence: "An else sits at the same depth as its if, and governs one
statement one level deeper, exactly as the if does." Step 3's first sentence
becomes: "Count the braces open above the line, add one for each unbraced
if, else, for or while whose one statement the line is, and multiply by the
indent, four spaces here."

**5. `self-documenting-code`, quiz 1's `why` asserts a classification the
exercise leaves open, and does not answer the reader who chose the other.**
*Where:* the exercise asks the reader to "mark each comment as a repeat of
the code, an explanation, a summary or a statement of intent"; the `why`
says "Both are intent comments". *What is wrong:* line 3 ("divisible by 4,
except centuries, except every fourth century") sits over a one-line
expression that is exactly the kind of dense code the chapter's second kind,
"an explanation of the code", is written for, and a reader who marks it
explanation (or summary) has a defensible answer the feedback never meets.
The options are safe, because they differ only on the counts and on "repeats
the code"; the `why` is what needs a sentence. *Change:* replace "Both are
intent comments, of a kind the chapter keeps." with: "Line 1 is intent. Line
3 you may have marked explanation, since it sits over a dense expression, or
summary, since it says the rule in one line; either way it is in the
calendar's words and not Java's, which is what keeps it out of the first
kind. The chapter's advice on an explanation is to ask whether the code could
be made to need it less, and here a reader might split the test into two
named booleans; the comment is still not a repeat."

**6. `themes-of-craftsmanship`, quiz 4 is trivia with no defensible
distractor.** *Where:* "How does Chapter 35 organise its reading plan?" with
"by programming language", "by the chapters of Code Complete", "by year of
publication". *What is wrong:* nobody holds any of the three, and the lesson
itself says the list is named and not taught. With finding 2 taken this
leaves the lesson one item on the counts and two on §34.7 and §34.9; the
theme the course elsewhere leans on, programming *into* a language (§34.4,
and Course 1's Key Construction Decisions), is untested anywhere in Course 7
and has a real misconception behind it. *Change:*

> **q:** Section 34.4 says to program into your language, not in it. What
> does the distinction mean there?
> **a:** "Decide what you want to express, then find how your language can
> express it, writing your own named constants or assertions where it has
> none" (correct); "Use every feature your language offers, since each was
> put there for a reason"; "Write in the lowest-level constructs the
> language has, because they are the ones the compiler understands best";
> "Choose the language with the most features for each project".
> **why:** Page 843: the programmer who programs *in* a language limits their
> thoughts to the constructs the language supports; the one who programs
> *into* it decides what to express and then finds the way the language can
> express it, supplying what it lacks by convention or a routine of their
> own. Using every feature is programming in the language more thoroughly;
> writing at the lowest level is the opposite of the section's advice; and
> the section is about how you think in a language, not which one you pick.

(Check the page before pinning the wording; the lesson's own paragraph on
§34.4 says the same thing in its own words.)

**7. `personal-character`, quiz 1 and quiz 3 test the same skill, and the
chapter's content gets one item.** *Where:* quiz 1 is the exercise's
arithmetic; quiz 3 is the same arithmetic on `rare-task` with 13 runs and 28
minutes handed over in the stem, so it is 13 × 28 − 480. Of the chapter's
nine sections, only §33.1's 10-to-1 and §33.7's laziness are asked.
*Change:* replace quiz 3 with an item on §33.4, which the body already
teaches through Bert and which has holders:

> **q:** In Section 33.4's story, Bert's manager asks whether the project
> could be done in less time with fewer people, and Bert agrees. What does
> the chapter say Bert got wrong?
> **a:** "An estimate can be revised to be more accurate but cannot be
> negotiated down" (correct); "He should have padded the first estimate so
> that the negotiation landed on the true figure"; "He should have refused
> to give an estimate until the design was finished"; "Nothing: agreeing to
> a shorter schedule is what intellectual honesty asks of a team player".
> **why:** Page 827: the mistake was not realising that estimates are not
> negotiable; Bert can revise an estimate when he learns more, but a smaller
> number agreed to under pressure is a promise the project cannot keep, and
> he loses credibility when it takes as long as it was always going to take.
> Padding is a different dishonesty; refusing to estimate is not the
> chapter's advice; and agreeing is the opposite of the honesty §33.4 means.

If the author prefers to keep an arithmetic item, keep quiz 3 and drop quiz
4 instead; but one of the two arithmetic items should go.

**8. `layout-and-style`, quiz 3's fourth option has no path.** *Where:* "It
compiles, and clamp(15, 0, 10) logs and returns 15". *What is wrong:* no
reading of the routine, right or wrong, returns 15 for a high of 10; the
`why` says as much ("nothing in the routine returns 15"), which is a
distractor confessing. The two real wrong models are already options 2 and 3
(the indentation's story; the code without line 7). The one wrong model
missing is "unreachable code is a warning, not an error", which readers of C
and Python bring to Java. *Change:* fourth option: "It compiles with a
warning about line 7, and clamp(5, 0, 10) returns 10"; in the `why`, replace
the last clause with: "and Java treats an unreachable statement as a compile
error, not a warning, which is where a reader coming from C or Python may be
caught."

**9. `themes-of-craftsmanship`, step 1 should say what an `else if` and a
`do … while` count for.** *Where:* "Start at 1 and add one for each if,
while, for, case, && and ||. An else, a default and a do add nothing." *What
is wrong:* the two shapes a reader's own routine is most likely to have are
not named; the lab counts an `else if` as an `if` and the `while` of a `do`
as a `while` (probed), and a reader who counts neither, or counts the `else`
as well, gets a defensible different number and no feedback. *Change:* add:
"An else if is an if and counts; the while of a do … while counts, the do
does not; the ?: operator is not counted, which is the lab's choice and not
the book's."

### Consider

**10. `layout-and-style` is at the body ceiling and front-loaded.** Eighteen
blocks, seven paragraphs of paraphrase (about 900 words) before the first
listing. The paragraph on §§31.4–31.8 could lose its first two sentences
(the list of per-section advice) and keep only the single-statement-block
passage of pp. 748–749, which is the one the lesson uses. Fifteen minutes is
right for the whole; the wait before the code is the cost.

**11. `self-documenting-code`, "printed 1 = 100%".** The density tile prints
`1 = 100%` for `comments-repeat` and the prose explains it once. A reader
will still wonder what the "1 =" is; "the ratio as a fraction, then as a
percentage" in the "Now the code" paragraph would settle it.

**12. `personal-character`'s lab on a desktop.** At 1280 px the left column
holds only the status sentence, and the inputs and tiles sit on the right;
it looks like a page that failed to load its listing. A kit matter, not the
lesson's; recorded so that nobody reads it as a lesson defect.

**13. The course's `assumes_short` is "Nothing in this course".** Course 1's
is "Nothing", and the long form already says what the short form is trying
to. Use "Nothing".

**14. `personal-character`, the worked example's "pays for itself in the
fourth week".** 3.50 weeks is during the fourth week, so the sentence is
right; "midway through the fourth week" would stop a reader rechecking it.

## D. The quiz distractors, item by item

Every item was argued for each wrong option. Where an option could not be
argued for, it is in the findings above (8, 6); where an item is a lookup,
finding 2.

- 7.1 Q1 (which `if` the `else` binds to): line 2 is the indentation's
  story; "javac rejects it as ambiguous" is a belief real readers hold about
  the dangling else; "both" is the wrong model of `else` as "when either
  fails". All three arguable. Good.
- 7.1 Q2 (balance 50): "neither" is the indentation's story and the
  misconception; "lines 3 and 4" is the balance-0 case; "line 3 only" is the
  off-by-one, which the `why` names. Good.
- 7.1 Q3: see finding 8.
- 7.1 Q4 (Miara): a book figure as §S.2 settles it, source in the `why`;
  the inverted options are the reader's likely misrememberings. Acceptable
  as the lesson's one recall item.
- 7.2 Q1 (`isLeapYear` counts): each option differs on an integer, and the
  `why` names which line each wrong count adds or forgets. Good, with
  finding 5.
- 7.2 Q2 (one in ten): the five-line standard is the one p. 792 warns
  against; one per statement is the preset; "no peak" is the misconception.
  Good.
- 7.2 Q3 (Callicles): checked against pp. 782–784; Callicles says both
  things the stem names, Thrasymachus is the one who says good comments
  state intent, Ismene answers, Socrates closes. Good, and the lesson has
  made "whose voice" a taught skill rather than trivia.
- 7.2 Q4 (4/20): all-lines, inverted and 4/16 are the three wrong sums a
  reader makes. Good.
- 7.3 Q1 (24 runs): forgets the build; rounds a whole division; build
  minutes as runs. Good.
- 7.3 Q2 (long-term laziness): the other two kinds and hustle, as p. 830
  has them. Good.
- 7.3 Q3: see finding 7.
- 7.3 Q4 (10 to 1): F29 as settled. Acceptable.
- 7.4 Q1: see finding 2.
- 7.4 Q2 (what p. 848 says): "must be split" is the rule-reader, "proof" is
  the verdict, "does not mention" is checkable; p. 848 says exactly what
  the correct option says. Good.
- 7.4 Q3 (eclecticism): one method, the newest, no method. Good.
- 7.4 Q4: see finding 6.

## E. Voice, load and the read-out

**Voice.** §F is met. Two lessons open with the reader's own code (7.1 "You
have probably met this", 7.4 "Take a routine you wrote last month") and two
with the chapter's question, which is the half §F.1 allows. Each lesson has
at most one story with people in it (Hank and Tony; the Commento; Dijkstra's
lecture; Simple Simon) and the light remarks are McConnell's own. "McConnell
argues", "the chapter calls", "the book reports" are used throughout and the
Commento's speakers are attributed by name. The modern aside (Martin against
Ousterhout, "both read like the dialogue continued") states both sides and
settles nothing, and is not a misconception. The §F.5 rule is kept for
Miara, Fjelstad and Hamlen, Jones and Sackman. The one sentence that leans is
7.3's "Hustle, visible effort for its own sake, comes off worse than any of
them": p. 830 says hustle is extra, unnecessary effort, which is close
enough, but "worse than any of them" is the lesson's ranking. "Comes off
badly" would be the page's strength.

**Load.** Reading sections run 1588, 1568, 1191 and 1368 words, inside the
12–15 minute estimates. One new hard idea per lesson: the binding rule; the
kinds against the count; the proviso as a sum; counts as warning signs. 7.1
is the heaviest (finding 10).

**Read-out.** `preview_subject.py` reports no unspoken or ambiguous run;
every key line and worked line was run through `say_code` and reads as
words ("density is comment lines divided by statement lines", "points 1 plus
each if, for, while, case, and, or", "480 divided by 14 is approximately
34.3, so 35 runs"). No `=` or `%` in a key or worked line; the `1 = 100%`
and `1/5 = 20%` strings sit in plain prose and in the quiz, which the
read-out leaves alone or skips. 7.1's `note` says the evidence is visual and
the body states each routine's structure in words, as #31 asked; a listener
gets the lesson. The gutter mark is a glyph plus the word "mis-indented",
not colour alone.

## F. Against the pre-authoring review

| # | asked for | state |
| --- | --- | --- |
| 3 | an own-code step with an observable result in every lesson | done in all four; 7.1's is self-defeating (finding 1) |
| 12 | density per statement line | done; `coStatements` shown and explained |
| 17 | "indentation is cosmetic" as 7.1's misconception | done, refuted by both presets and the exercise |
| 31 | structure stated in words; gutter marker | done |
| 32 | listings stack on a phone; depth convention stated | done; the `complexity` banner states its convention |
| 33 | answer in one quiz `why` only | done for 7.1 and 7.3; 7.2 leaks in `mistakes[0]` (finding 3); 7.4's answer is on the page three times by design (finding 2) |
| 5 | `themes-of-craftsmanship` carried by `retry-delay` | done, and it is where finding 2 arises |

## Summary of must-fix findings

1. **`layout-and-style` step 5** tells the reader to re-indent with an
   editor before pasting, which removes what the lab checks, and gives no
   hint when a two-space routine has every line flagged. Replace the step
   with the search-and-replace instruction and the "if every indented line
   is flagged, the width is the cause" sentence; report the status-line hint
   and the tab behaviour as kit gaps.
2. **`themes-of-craftsmanship` quiz 1** asks for figures the body, the worked
   example and the lab all show. Make it a transformation of `retry-delay`
   (the cap folded into `Math.min`: 6 points, depth 1).
3. **`self-documenting-code` `mistakes[0]`** gives the exercise's answer.
   Reword it so that it says the count cannot tell the two cases apart
   without saying which case `isLeapYear` is; correct §C's line to match.
