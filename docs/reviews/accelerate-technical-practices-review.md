# Review (accuracy and teaching): Accelerate, Course 3 — Technical Practices and Architecture

Course: `accelerate-technical-practices` (`content/accelerate/c3_technical_practices/`,
`__init__.py`, `part_a.py`, `part_b.py`), seven lessons, Chapters 4–5. Built to
`docs/accelerate/PLAN.md` §C Course 3 and `docs/accelerate/AUTHORING.md`. Reviewed
2026-11-01 against the private extraction (PDF pages 76–104 read in full with
`page.py`, plus the chapter notes on p. 93 and p. 104). I did not read `site/` or the
book file whole. I wrote only this file; each finding is a recommendation.

## Gates

- **Preview:** `preview_subject.py accelerate --course accelerate-technical-practices`
  rendered 8 pages; labcheck 7 executed, 7 with pinned figures, 0 failing; **OK**.
- **`quotes.py`** (my own file of the seven quotations): L1 p. 77 OK (34 words), L2
  p. 87 OK (20), L3 p. 89 OK (23), L4 p. 91 OK (36), L5 p. 94 OK (26), **L6 p. 98
  LOOSE (19)**, **L7 p. 104 LOOSE (18)**. One quotation a lesson, so every lesson is
  under 40 and under 60. The source comments call L6 and L7 "quotes.py OK"; they are
  not (MF-3).
- **`overlap.py … 8`:** section titles (What Works and What Doesn't; Architects Should
  Focus on Engineers…) and the seven quotations, plus three uncounted runs: part_a.py:970
  (8 words, a quiz option), part_b.py:303 (9, a quiz option), part_b.py:592 (10, a
  `why`). See MF-4.
- **Browser (Playwright, chromium, `file://`).** Every preset of all seven lessons at
  375 px and 1280 px: scrollWidth equals clientWidth everywhere, no page or console
  errors. Every tile matches the prose and worked lines, and I worked every figure by
  hand: batch 26/14/28/21/8/32/20, 6.25/25/125/8; shares 44/19/13/24 and 505/1,000;
  odds 7/3 against 2/3 = 3.5, 3 against 1 = 3; branch lifetimes 195, 289, 222, 223, 5,
  23, 2 → 959/7 = 137 h, short-month mean 98/10 = 9 h 48 min; release groups;
  rates 2/5, 19/40, 5/8 etc.
- **Exercises typed in:** batch 18→8, 36→48, 27→28 (agrees with L1 quiz 1); 800 h,
  40/25/20/15 %, 80 freed, 50 %; 80 % against 40 %, 2×, +40, odds ratio 6; sprint max 2,
  mean 1 d 15 h 15 min, over a/c/e; clinic 2 groups, largest 3, 0 alone; orgs 1/2,
  2/5, 1/4 falling (agrees with L6 quiz 2); L7 one group of 5, arlCoord
  `1: shop + find + growth…`, after `1: shop + growth for {web, api, ads}`.

## MUST-FIX

1. **The arlCoord tile's leading number is read as a team count (the author's flag
   holds).** The tile's number counts *groups* that span more than one team; the teams
   are the names after it. On `lockstep` after the removal the tile is
   `2: payments + growth for {…}; data + platform for {…}`: two groups, four teams
   still coordinating in two pairs. The exercise shows the trap: after removing
   api–search it prints `1: shop + growth`, which a reader taught the lesson's reading
   will take as "one team".
   - part_b.py:391–394 (concept) defines the teams as those of "the largest release
     group"; the kit lists every multi-team group. Replace: "The teams that own the
     components of a release group spanning more than one team. The lab's tile counts
     such groups and names each group's teams; when each component has a team, a
     group owned by one team is not listed."
   - part_b.py:462–464: "The largest has 4 services and spans 2 teams. The lab shows
     the same figures after the removal" → "The larger has 4 services owned by
     payments and growth; the other, 3 services owned by data and platform. The lab's
     after tile reads 2: two groups that still need two teams each, so all four teams
     still coordinate, but in pairs."
   - part_b.py:561–563 (worked `after`): "so the lab reports 2 teams" → "and the lab's
     after tile reads 2 because two groups still span two teams each; the teams it names
     are four."
   - part_b.py:574–575 (quiz 1 `why`): "two is the figure after the signup-reports tie
     is removed" → "two is the number of teams in each group after the signup–reports
     tie is removed (and the number of groups the lab's after tile counts)."

2. **part_a.py:1313, Lesson 4 note: "by whole days"** is wrong about the lab, which
   takes and prints `day.hh:mm` times and refuses bare day numbers (kit report,
   branches/trunk; the lesson's own body at 1134–1136 says so). Replace with "from a
   log you type, to the minute."

3. **Two quotations are not character for character.** part_b.py:106: the book has
   lower-case "organizations" (p. 98); write "&ldquo;[O]rganizations which design…" or
   lower-case it. part_b.py:403–404: the book's sentence runs on ("…hate using them, or
   if they don't achieve the outcomes…", p. 104); closing the quotation with a full stop
   presents half the sentence as whole. End the quotation at "them" without the stop
   inside (". . . them&rdquo;, the authors write, or if the tools do not achieve…") and
   fix the "quotes.py OK" comments at part_b.py:54–55 and 352.

4. **Three uncounted 8+-word runs (PLAN §E).** part_a.py:970–971 quiz option → "Keeping
   configuration under version control, more than the application code"; part_b.py:
   303–304 → "Changing how the teams and the organization are structured so as to get
   the architecture wanted"; part_b.py:592–593 → "…to software delivery performance,
   and so to organizational performance."

## SHOULD-FIX

1. **part_a.py:1165–1169, Lesson 4 exercise:** "which single branch changes the
   answer" has no answer. The lifetime test fails on three branches (a, c, e), and the
   active test passes with 2 open at four separate moments, so no one branch flips
   either. Replace with "and which branches you would have to change for the lifetime
   threshold to be met."
2. **part_a.py:1222–1225, step 3:** "A branch still open is a question, not a pass"
   contradicts the lab, which already fails an open branch a day old (f4, e). Replace:
   "An open branch younger than a day is not yet decided; one already a day old fails."
3. **part_a.py:1460–1462, Lesson 5 exercise:** "the one tie whose removal would make the
   largest group smaller": two ties do (booking–reminders, reminders–notes). Write
   "a tie whose removal…", or ask for both.
4. **part_b.py:455–461, Lesson 7 model.** The library is said to force billing, signup,
   reports *and* gateway to upgrade together, yet removing one of its three ties leaves
   the other two standing. Say what the removal stands for: "Suppose signup and reports
   could take the new version at different times, say through a compatibility shim:
   remove that one tie…".
5. **part_a.py:977–980, quiz `why`:** "a result it calls a corrective". The book says
   the data shows the idea "is a misconception" (p. 89). Replace "calls a corrective to"
   with "says shows to be a misconception".
6. **Near-paraphrase of survey items (PLAN §E).** part_a.py:1359–1360 and 1406–1410
   restate the two p. 97 statements almost word for word ("deploy or release … independently
   of other applications/services it depends on"), and part_a.py:1416–1421 walks through
   the six p. 97–98 items in order, keeping "normal business hours with negligible
   downtime". Name the two properties and summarise the six as "whether a team can change
   its design, finish its work, test and deploy without asking or waiting for other teams,
   and deploy in working hours without an outage". The 2017 construct at part_a.py:520–524
   is also close to the p. 82–83 items; shorten it the same way.
7. **part_a.py:524–526:** "The capabilities of 2014 to 2016 were strongly and
   significantly associated with that construct". Note 4 (p. 93) says only a subset was
   tested for length. Add "(a subset of them, the authors note)".
8. **part_a.py:574–577:** "The chapter's answer is the practices it has just listed".
   Those practices come in the *next* section, and the book's own answer here is small
   batches with continuous in-process testing (p. 88); configuration is the lesson's
   addition. Replace with: "The chapter's answer, at the end of the section, is small
   batches and continuous testing; the next section adds the practices that go with
   performance."

## NOTE

- Accuracy otherwise holds against pp. 76–104, including 49/21 and 38/27 percent,
  the eleven system types, the 2017 "biggest contributor", Conway 1968 and Figure
  5.1's daily-deployer sample and trends. Causal wording follows the book's own
  ("contributes", "predicts"), and every note closes on the sample-not-finding gap.
- part_a.py:218–219: 8 of 26 hours is just under a third. "In under a third of the
  time" is exact.
- part_a.py:1269–1271: 959/8 h is 4 d 23 h 52 min. "Just under 5 days" reads better
  than "about 4 days 23 hours".
- part_a.py:1552–1555: quiz 2's distractor "4" has no explanation in the `why`.
- Kit, not course: `aflOverhead` prints "1 hours" on `automated`.
- PLAN §C names Little's law as Lesson 1's lab on `flow/batch`. The lesson correctly
  says the chapter does not mention it and points to System Design's "Little's Law from
  a Trace" (the title exists). No change needed; the deviation could go in the author's
  report.
- No lab uses the book's data; every sample is labelled invented.

**Verdict:** accurate and well taught. Fix the arlCoord reading in Lesson 7 and the
three small gate failures before the course goes live.
