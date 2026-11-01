# Review (accuracy and teaching): Domain-Driven Design, Course 5 — Supple Design

Course: `ddd-supple-design` (`content/domain_driven_design/c5_supple_design/`,
`__init__.py`, `part_a.py`, `part_b.py`), seven lessons, Chapter 10. Built to
`docs/domain-driven-design/PLAN.md` §C Course 5 and `AUTHORING.md`. Reviewed
2026-11-01 against the private extraction (PDF page = the tools' page), reading
the pages behind every claim about what Evans argues (PDF pp. 147–180) with
`book.py`/`page.py`. I did not read the book whole and did not read `site/`.
I wrote only this file.

## Gates

- **Preview:** `preview_subject.py domain_driven_design --course ddd-supple-design --out …/scratchpad/rev/ddd-supple-design`
  rendered 8 pages; labcheck 7 executed, 7 with pinned figures, 0 failing; **OK**.
- **`quotes.py`: 9 quotations, all OK.** 5.1 p. 150 (22 words), 5.2 p. 153 (22), 5.3 p. 156 (18),
  5.4 p. 160 (22) + p. 159 (8; lesson 30), 5.5 p. 164 (13), 5.6 p. 168 (18) + p. 170 (13; lesson 31),
  5.7 p. 174 (26). Every opening ≤ 40, every lesson ≤ 60; each dict comment gives the page.
- **`overlap.py … 8`:** 11 runs, every one a counted quotation or the three pattern names
  run together (`__init__.py:21`, `:82`). Clean. At 6 words, see SHOULD-FIX 3.
- **Browser (Playwright, chromium, `file://`).** All seven at 375 px and 1280 px: no
  sideways scroll (scrollWidth = clientWidth), no page or console errors. Every preset's
  tiles match the prose, worked lines and quiz by my own count (holders 3/3/2/0 and 3/1/0/1;
  clauses 4 of 4, 3 of 4 at clause 4, 3 of 4 at clause 1; touches 9/1 and 7/2, 6 and 2, 3 and 5;
  ripple 2/3, 1/2, 2/3; subsume 1/4/0/yes, 4/1/3/no, 2/0/undecidable; bakery 8/6, 4/7,
  cycle; 9/5, 9/14, no cycle, tie at 2).
- **Exercises typed in** (records separated by `;`). All agree with the quiz `why`s:
  `amt` 3 counted, `d, base, tmp` short; windows 3/3/2/0 then 3/1/0/1 (`morning′`);
  vault A yes, B first false `left >= 30`, C first false `left = 20`; timetable 6/0 and 3/1;
  library DueDate 1 direct, 3 in all; concession (A `age >= 60`, B the senior rule) logical yes;
  `lotF` added to `with-or` gives 1 counter-example; clinic 4/3/cycle and 3/4/no cycle.
- **The subsume view as it now renders.** Field labels are "Specification A" and
  "Specification B"; the tiles say "every one B accepts, A accepts too" and never "subsumes";
  the rules state both senses (logicians': looser A subsumes B; Evans's: stricter B subsumes A).
  Evans p. 172: the more stringent spec subsumes the less stringent. The lesson's concept,
  key line, worked example, quiz 2 and its exercise all use Evans's sense correctly; the
  lab-warning paragraph does not match the lab (MUST-FIX 1).

## MUST-FIX

1. **`part_b.py:226–232` (and `:346`)** — the lab warning describes the old lab. It says
   the lab "uses subsumes the way logicians use it", "calls A the more general rule, and says
   A subsumes B". The lab no longer does either: the label "(the more general)" is gone,
   the tiles avoid the word, and the rules give both senses. The direction advice (old rule
   as A, new as B) is still right. Replace the paragraph's middle with:
   "One warning before you run it. The lab never says subsumes, because the word runs both
   ways: its rules note that logicians say the looser rule subsumes the stricter, while Evans
   says the stricter subsumes the looser. Its tiles ask one plain question: does A accept
   every candidate B accepts? A yes means, in Evans's words, that B subsumes A. So to ask
   Evans's question, whether the new rule subsumes the old, enter the old rule as A and the
   new one as B." At `:346` replace "enter overSixty as A, the more general," with "enter
   overSixty, the looser rule, as A".
2. **`part_b.py:126`** — "Evans has seen it fail as often as succeed" is not in the book.
   He names two pitfalls he has met "more than once", calls dumbing-down the unintended
   consequence of "many attempts", and names the narrow framework as the greatest value
   he has seen (pp. 166–167). Replace with "and Evans has seen many attempts at it trap the
   model in the limits of a framework."
3. **`part_b.py:209`** — "Usually only one operator is needed" overstates p. 170, which says
   full generality is not needed in many cases and that AND is used far more than the others.
   Replace with "Often the full set is not needed, and and is used far more than the others:".
4. **`part_a.py:1138–1141`** — the Whole Value concept credits Cunningham's pattern with
   "an operation with a coherent meaning … should be one operation". On p. 159 that is
   Evans's own point; the footnote to Whole Value covers only "each object should be a
   single complete concept". The body (`:1180`) has it right. Replace with:
   "Ward Cunningham's pattern, which Evans cites: each object should be one complete concept.
   Evans puts it beside his own rule that an operation with a coherent meaning in the domain
   should be one operation, not split into steps."
5. **`part_b.py:585`** — the worked example's title, "Four dependencies that cross,
   carved", is wrong. The carved packaging has 5 across (lab `dmoAcross2` = 5, body `:528`),
   and the example lists five, three into `quantities` and two into `orders`. Replace with
   "Five dependencies that cross, carved".

## SHOULD-FIX

1. **`part_a.py:1503–1505`** — "the lab refuses an edge from a class to itself, and closure
   is that refusal put to work" gets closure wrong. Closure is about types (p. 165): `plus`
   takes and returns a `Fare`, and `Fare` still "depends on" `Fare`. The lab refuses the
   self-edge ("names Fare on both sides") because it adds no other concept, and that is a
   convention of the input format. Replace with "`plus` is closed under `Fare`, so it adds no
   concept beyond the class itself, which is why the model lists no edge for it."
2. **`part_b.py:245`** — "the logical answer names a moisture the old rule allows": the tile
   reads "B allows a value of moisture that fails A’s clause moisture <= 6". It names the
   attribute and the clause, not a value. Write "the logical answer says the old rule allows
   a moisture that fails the new rule's clause `moisture <= 6`".
3. **Near-runs on boxed pattern statements** (`overlap.py … 6`). These are 6-word runs
   that track the "Therefore" paragraphs closely:
   - `part_a.py:899` "write automated unit tests for them, and put them in documents or
     diagrams where that suits the project's process" (p. 156 statement, clause for clause);
     also `:1068`. Suggest "where the language cannot express them, check them with
     automated tests, and record them wherever the team's process keeps such things".
   - `part_a.py:1183–1186` follows p. 160's statement in order: "operations, interfaces,
     classes and aggregates into" and "successive refactorings, and look for the". Suggest
     "divide the design into cohesive units where you sense the domain divides; over several
     rounds of refactoring, notice what keeps changing together and what stays put, and look
     for the domain lines that explain it."
   - `part_a.py:347–348` "the event and not how it is carried out" echoes p. 150's statement
     (5-word run). Suggest "Say what rule holds and what event happens; leave how to the code."
4. **`part_b.py:50`, exercise data** — two age thresholds compared for subsumption sit very
   close to the book's own subsumption example (minimum-age specifications, driving and
   voting, p. 173). Age is not on PLAN's list of banned domains, but the exercise's shape is
   the book's. Suggest another attribute, such as `visits >= 10 and member = yes` against
   `visits >= 6`, with the quiz updated to match (a member with 8 visits separates them).

## NOTE

- Everything else checked against pp. 147–180 is accurate: the opening, Beck, Meyer and
  Fowler credited where Evans cites them, both paint examples, accruals, the dependency
  snowball, closure's refinements, the declarative pitfalls and DSLs, subsumption's
  chemical case (summarised without data), and Shares Math. One trivial point: "the extreme
  of low coupling" (`part_a.py:1414`); Evans says "an extreme".
- No book code, diagram or data is reproduced. The `Spec` combinators are Java 8 default
  methods, not the book's Composite classes. Every lab domain is the lesson's own.
- Every wrong quiz answer is wrong once the question's stated sense or rule is applied
  (the subsume quiz pins "in Evans's sense", so option 2 of item 1 fails even though it is
  true in the logicians' sense). Every lesson's `note` names the gap between count and judgement.
- Kit (not this course): the record fields take `;` between records. Typing one record per
  line, as the exercise listings are laid out, gets a misleading error ("…should be
  name=value" with the newline inside the cell). The kit owner may want to accept newlines,
  or the lessons may want to say "separate records with `;`".
- `part_b.py:355–356` the subsume quiz `why` has a 7-word run with p. 172 ("any candidate
  that would satisfy the new"). It is not a boxed statement and is under 8 words.

**Verdict:** accurate and well taught. Fix the subsume lab warning so it matches the
relabelled lab, plus four small accuracy and figure fixes, and the course is ready.
