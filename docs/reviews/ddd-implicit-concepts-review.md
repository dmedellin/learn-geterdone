# Review (accuracy and teaching): Domain-Driven Design, Course 4 — Breakthroughs and Implicit Concepts

Course: `ddd-implicit-concepts` (`content/domain_driven_design/c4_implicit_concepts/`,
`__init__.py`, `part_a.py`), five lessons. Built to `docs/domain-driven-design/PLAN.md`
§C Course 4, §D, §E, §F and `docs/domain-driven-design/AUTHORING.md`. Reviewed
2026-11-01 against the private extraction of the operator's copy, reading Chapter 8
(PDF pp. 115–122) and Chapter 9 (pp. 123–146) section by section with `book.py` and
`page.py`, behind every sentence that says what Evans argues. I read neither the
file whole nor `site/`.

## Gates

- **Preview:** `python3 scripts/preview_subject.py domain_driven_design --course ddd-implicit-concepts --out …/scratchpad/rev/ddd-implicit-concepts`
  printed 6 pages; labcheck 5 executed, 5 with pinned figures, 0 failing; **OK**.
- **`quotes.py`: 6 quotations, all OK.** 4.1 p. 115 (12 words), 4.2 p. 124 (19),
  4.3 p. 132 (10) and p. 135 (20), 30 in the lesson, 4.4 p. 135 (16), 4.5 p. 137 (16
  counting the dashed words; the source comment says 14). Every opening quotation is
  under 40 words and every lesson under 60. The page comments are right.
- **`overlap.py … 8`: 10 runs**, all titles (How to Model Less Obvious Kinds of
  Concepts, ×4) or the six counted quotations. Nothing else.
- **Browser (Playwright, chromium, `file://`).** All five lessons at 375 px and 1280 px:
  no sideways scroll (scrollWidth equals clientWidth), no page or console errors. Quizzes
  clicked through at 375 px; feedback and Next work. Every preset's tiles match the
  prose, the worked lines and the `expect` pins, by my own count:
  - 4.1 lease 9,999 at 50/30/20: nearest 5,000/3,000/2,000, 10,000, +1, gap 1/2; allocator
    5,000/3,000/1,999, 0, gap 4/5. Gas 4,000 at 9/7/5: nearest 1,714/1,333/952, −1;
    allocator 1,715/1,333/952, 0.
  - 4.2 `library-before` 8 / alike 1 / 12 translations (2+2+3+0+1+2+2) / missing recall
    and pickup-window / reservation ambiguous; `library-after` 2 / none / none.
  - 4.3 inline 5 (1 + if 2 + && 2), caller 2, constraint 4; depth 3.
  - 4.4 lot-01 4 of 4; lot-02 3 of 4, first false moisture; lot-07 1 of 4, three false.
  - 4.5 `distributable` lot-01, lot-06 with the five first false clauses the prose
    names; `school-garden` 3; `school-garden-safe` 2, lot-05 at quarantine.
- **Exercises typed into the lab.** Each agrees with its quiz `why`: 10,000 at 3 3 1
  gives 4,286/4,286/1,429, 10,001 (nearest) and 4,286/4,286/1,428, 10,000 (allocator);
  the clinic glossary gives 6 translations, missing triage (developers, code) and
  care-episode (code); `book` gives 6, 1 + if 2 + for 1 + && 1 + || 1; lot-08 gives
  2 of 4, first false age <= 10, false age and quarantine; the exercise rule selects
  lot-01, lot-03, lot-06, with lot-04 blamed on kind = herb. No exercise answer
  appears in the rendered prose outside the quiz data.

## MUST-FIX

1. **`part_a.py:762–778` (4.2 quiz 1): "clinician" can be argued for.** Evans's
   doubly strong warning is when both the developers and the experts use *terms that
   are not in the design* (PDF p. 124). In the clinic glossary the experts say
   clinician and the developers say doctor, and neither word is in the code (it says
   user). Read as Evans writes it, clinician qualifies as well as care-episode. The
   lesson's reading (the code has *no name for the concept*) is reasonable, but the
   question has to say it is the one being used. Replace the question with: "In the
   exercise's clinic glossary (experts, developers, code), which concept does the code
   have no name for at all, although the experts and the developers both name it? That
   is the lesson's reading of Evans's doubly strong warning." Add to the `why`: "Read
   word by word, Evans's warning also touches clinician: neither clinician nor doctor
   is in the code, which says user. The lab counts that as 3 translations, not as a
   missing name."
2. **`part_a.py:330–333` (4.1): the 4/5 gap is explained wrongly.** Under the pie
   the lease parts are 5,000, 3,000 and 1,999 against exact parts of 4,999.5, 2,999.7
   and 1,999.8. The largest gap, 4/5, is the *third* caterer's shortfall. No member
   gets a whole cent more than the exact part. Replace "4/5 of a cent under the pie,
   which gives one member a whole extra cent" with "4/5 of a cent under the pie, where
   the third caterer, who gets none of the leftover cents, falls 0.8 short of the
   exact part".
3. **`part_a.py:280–281` (4.1): "felt sick" is not a light remark.** In the book that
   line turns the story from success to fear. The next section, A Sobering Decision,
   says their main emotion was fear under a severe deadline (PDF p. 120). Replace
   "Evans's own light remark is that when the new model worked very well, the whole
   team felt sick." with "The new model worked very well, and Evans records that the
   whole team felt sick."

## SHOULD-FIX

1. **`part_a.py:1054–1060` (4.3 quiz 1 `why`): the warning sign is asserted, not
   shown.** Evans's first sign is data that does not otherwise fit the object's
   definition (p. 134). A clinician's diary does fit a clinician. Replace the last
   sentence with: "Which warning sign the rule shows is a judgement: the Saturday
   closure and the urgent exemption are clinic policy sitting in a clinician's diary,
   and if scheduling meetings keep returning to them while the code hides them in one
   condition, that is Evans's third sign."
2. **`part_a.py:964–966` (4.3):** the preview flag belongs to a performance, so it is
   a weak case of the first sign. Suggested text: "The members' tenth on preview nights
   and a patron's membership are needed only by the limit, not by selling as such,
   which is the nearest thing here to the first sign".
3. **`part_a.py:919–923` and `:1064` (4.3): a close paraphrase of Evans's numbered
   list.** The scanner at 6 words finds "objects forcing duplication or inheritance
   between" and "that are not otherwise a family" (p. 134), and the quiz option
   repeats the shape. Reword it, for example: "Rules of the same kind turn up in
   several classes, so they are copied, or classes that share nothing else are made to
   inherit from each other."
4. **`part_a.py:1343–1344` (4.4 quiz 2 `why`)** follows p. 135 closely ("separated from
   the domain layer altogether, leaving" plus "a lifeless data object"). Suggested
   text: "The rules leave the domain layer entirely, and the object they were about
   is left holding data that expresses none of them."
5. **`part_a.py:1209` (4.4):** "It states a constraint on another object's state"
   echoes p. 136. Suggested text: "It says what another object's state must be".
6. **`part_a.py:302–305` (4.1, Epilogue):** the word was "transaction", in the
   financial sense (p. 121). It came with an awkward design: rules crammed into
   Facility and Loan. Suggested text: "weeks later the team noticed rules crammed into
   the Facility and the Loan, and a word in their conversations, transaction in the
   financial sense, that named no object; a second deeper model followed."
7. **`part_a.py:602–603` (4.2):** "is summarised in Chapter 9 itself" is wrong, because
   the book tells the itinerary example at length as a conversation (pp. 124–126).
   Suggested text: "The book's example, from its shipping domain, is a conversation in
   which a word on a printed report…".
8. **`part_a.py:1493` (4.5):** A Working Prototype of the Warehouse Packer is a second
   Example, not a sidebar (p. 145). Write "Its second example, a working prototype,
   makes the general point".
9. **`part_a.py:1510–1513` (4.5):** "That is Evans's warning about one rule in several
   guises" stretches the point. Evans warns that one rule appears in different forms
   across validation, selection and building (p. 137). The school's request is a
   different rule that should contain the bank's rule. Suggested text: "That is a
   cousin of Evans's warning: the bank's rule turned up again in a new guise and lost
   a clause on the way".
10. **`part_a.py:959–961` (4.3):** the lab's "First line at that depth" is line 11,
    the preview reduction, not "the if around the sale". Write "the class, the method
    and an if (the lab's first line at that depth, 11, is the preview reduction)".
11. **`part_a.py:1394–1395`:** the source comment gives 14 words for the 4.5 quotation.
    `quotes.py` and a plain count give 16. The lesson is still under every limit.

## NOTE

- 4.3's theatre limit (capacity less a tenth for members) mirrors Chapter 1's
  overbooking rule (capacity plus 10 per cent), which the same lesson cites. It is a
  different domain, so it is allowed. A fraction other than a tenth would put more
  distance between the two.
- 4.1's shared kitchen splits by shares, the concept §C asks for, in a domain that is
  not the book's. The `SharePie` sketch is the lesson's own code: the book's Share
  Pie listing is never reproduced.
- The labs fit their arguments. 4.3's "factoring moved, not removed, four decisions"
  is the strongest. Every lesson closes on the gap, in the body and in its note. Evans's
  costs are kept: the 4.1 decision under deadline and the 4.5 performance trade and
  stored procedures. Every other wrong quiz answer resisted my attempts to argue for it.

**Verdict:** accurate and well built, with every gate green. Fix the arguable 4.2 quiz
item and the two 4.1 misstatements before publishing.
