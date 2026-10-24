# Second review: Reproduction of the Social Capital (Course 8)

Course `capital-social-reproduction`, package `content/capital/c08_reproduction`,
Volume II, Part III, Chapters 18–21. Reviewed against the Kerr text
(`volume-2-kerr.txt`, ll. 3590–5470 read in full for every passage a lesson
paraphrases), following `docs/capital/SECOND-REVIEW.md`. The findings below were
written before the pedagogy assessment was opened.

## Summary

- **Arithmetic:** no errors. Every figure in prose, worked lines, quiz answers
  and `why`s recomputes exactly, and every preset's tiles were read with
  `labcheck.js --observe` and agree with an independent exact-fraction run of
  the expanded-scheme rule (both of Marx's illustrations and `ii-short`).
  One claim about agreement with Marx's rounded figures was overstated (F7).
- **Quotations:** strict checker 75 segments, 0 misses after the changes (69
  before, 0 misses). No convention-only misses. Two one-word quotations
  (`convincing`, `latent`/`potential`) are matched by the checker at unrelated
  lines; I checked them by hand at l. 4796 and l. 5496.
- **Misrepresentation of Marx:** five places, one of them a lesson's first
  misconception (F1). All fixed.
- **Final preview:** `OK` (6 pages swept, 6 with pinned figures, 0 failing).

## Findings and changes

### F1. The Object of the Inquiry: Proudhon's error stated the wrong way round (fixed; §C corrected)

The body and `mistakes[0]` said Marx faults Proudhon for treating society "as a
single firm", and the misconception was titled "Thinking of the economy as one
big firm". The text says the opposite of the conclusion this suggests. At
l. 4419 Marx rejects the manner "copied by Proudhon from bourgeois economy" of
treating society *as though* it lost its capitalist character by being taken as
a unit, and goes on: "Not at all. We have, in that case, to deal with the
aggregate capitalist." He treats society as one unit himself, the stock company.
What Proudhon took from bourgeois economy is Say's "discovery" (l. 3941–3943):
for society the gross product is all revenue, the difference between capital
and revenue is "purely subjective". The lesson's own refutation (only 3,000 of
the 9,000 can go into any household) answers exactly that error, so the
refutation was right and the attribution wrong.

Changed: the body paragraph now gives Say's conclusion, Proudhon's adoption of
it, the l. 4419 sentence and Marx's reply ("We have, in that case, to deal with
the aggregate capitalist."); `mistakes[0]` is retitled "Thinking that, for
society as a whole, the whole product is income" with the same preset as its
refutation. The §C entry in `docs/capital/PLAN.md` (Course 8, lesson 1) is
corrected to match and says why.

### F2. The Object of the Inquiry: a remark of Marx's attributed to Engels (fixed)

"The chapter's second section, which Engels' note says belongs later but is
placed here". The parenthesis at l. 3633 ("Although the following belongs in a
later part of this section, we shall analyze it immediately") is in the text in
the first person, not one of Engels' signed notes. Now: "which the text says
belongs later in the Part but takes up at once".

### F3. Former Discussions: Marx's actual reply to Smith's regress was skipped (fixed)

The lesson gives Smith's horse-and-breeder regress, Sraffa's dated-labour
reduction at strength, and then says that what in the chapter bears on the
regress is the one-year period. But the chapter answers the regress directly
(l. 3820–3822): it "would not be a specious subterfuge" only if Smith could show
that it ends in products made by labour alone, with no means of production; his
example, the collectors of Scotch pebbles, was no proof, and they use baskets
and sacks. That is Marx's reply, and it is also what bears on Sraffa, whose
residue never reaches zero. Leaving it out made Marx's position look weaker
than the text makes it. Added before the Sraffa sentence; the one-year point is
kept as the second consideration.

### F4. Simple Reproduction: Fixed Capital and Money: Marx's claim weakened, and one not his (fixed)

1. "Marx's claim is narrower: that the balance is not guaranteed even under the
   strictest assumptions, and that an industry equipped all at once will renew
   all at once." Marx says the disproportion "can and must arise" (l. 4796), so
   "not guaranteed" understates him. The second half is not in this section; the
   argument here is that expiring fixed capital varies from year to year
   "the same as among men" (l. 4794). The equipped-at-once idea belongs to the
   turnover cycle of Volume II, Chapter 9. Replaced with what §11 says, and a
   sentence that he does not say how large the swings are.
2. Mr. X. The lesson said Mr. X's hoarding of wear is "ordinary prudence" for
   one capitalist. In the text (l. 4655–4657) Mr. X is the case of Department II
   advancing the money for its own wear, which for one capitalist "looks...
   absurd" (he would lose 200 by wear and put up another 200 out of his own
   pocket) and only "seemingly" so because Department II's capitals are of
   different ages. Removed the "prudence" line and added that step before
   "Marx's solution is that Department II is not one capitalist", which is how
   the text gets there.
3. "Marx is pleased with this." Replaced with his own word: he calls the
   illustration "convincing" (l. 4796).

### F5. Accumulation in Department I: the difficulty stated more strongly than Marx states it (fixed); what bears on Say (added)

1. The concept card said that if every capitalist hoarded at once "it would be
   inexplicable where the buyers were to come from". The text says it "seems
   inexplicable" and calls it "this seeming difficulty" (l. 5010) before
   resolving it with the B's who buy out of old hoards. The body quoted it
   correctly; the card now says "would seem inexplicable ... a difficulty he
   calls only seeming and then resolves".
2. §C asks the lesson to say what in the section bears on Say's law. The
   section has a direct sentence (l. 5032): the disposal of the annual product
   is not a "bare exchange of commodity for commodity, as the political
   economists assume". Added to the paragraph that says the section does not
   name Say.

### F6. Reproduction on an Enlarged Scale: the opening rule is not what the figures show, and the lesson implied it was (fixed)

The passage is "accumulation in II must take place more rapidly than in I"
(l. 5286). In Marx's own figures Department II's capital grows from 2,250 to
2,400 (a fifteenth) while Department I's grows from 5,000 to 5,500 (a tenth),
and then both grow by a tenth a year (2,640 and 6,050; 2,904 and 6,655).
Department II's share of its surplus value accumulated (20%, then 30%) is also
below Department I's 50%. The lesson printed these growth rates without saying
they do not bear out the rule it opened with, and in the Tugan-Baranovsky
paragraph said "his figures show that it can". Now the growth paragraph says
plainly that, read literally, the rule is not what the figures show, what they
do show (Department II's accumulation is set by Department I's growing
I(v + s)), and that the chapter does not comment on the difference; the later
sentence says the figures show a balanced path, not that Department II grows
faster.

Also: `read_intro` said the passage is the rule Marx draws "after the first
year ... before he runs the second". In the text (l. 5257–5290) the order is:
the first year's product, 9,800; the second year's rearrangement, ending in
capitals of 4,840c + 1,210v and 1,760c + 880v (8,690); then the rule; then the
second year's product, 10,780. Now: "the rule he draws partway through, once the
first year is done and the capitals for the second are arranged". (My first
correction, "two years into it", overshot; see the disagreements below.)

### F7. Reproduction on an Enlarged Scale: "agrees ... throughout" (fixed)

For the second illustration the lesson said the lab's table agrees with Marx's
rounded figures "throughout" apart from the misprinted 6,385. Exactly,
Department I's variable capital after the second year is 1,173 11/18 (Marx
1,173; rounding gives 1,174) and its constant capital after the third is
6,357.06 (Marx's corrected 6,358). These are Marx's rounding carried forward,
within a unit. Now "to within a unit, the rounding he carries forward". The
misprint finding itself (6,385 for 6,358, confirmed by 6,358 + 1,271 = 7,629)
and the first illustration's slip (Kerr's II total 4,249 for 2,129 + 1,065 +
1,065 = 4,259; exact product 65,219/5) are both right.

## Arithmetic checked (all correct)

- L1: 300 + 100 = 400, 150 + 50 = 200, 600; misclassified 450 / 150.
- L2: 6,000 + 1,500 + 1,500 = 9,000, v + s = 3,000; spinner 372 + 50 + 78 = 500
  (Vol. II l. 480); tableau 500 / 300 / 200; a third of the value created in the
  year.
- L3: three exchanges 1,000 + 2·2,000 + 4,000 = 9,000; the gaps ±100; the money
  paragraph (1,000 + 500 circulating 5,000) matches l. 4228; diagram b 5,750 +
  2,502 = 8,252 with 1,750 = 1,750 (l. 5154–5158, which Marx gives as a
  simple-reproduction arrangement); Ic = 4,000 is "more than two fifths".
- L4: gaps 0, −100, +100, −20; Marx's 40 (l. 4753).
- L5: 500 accumulated; gaps 0, +500, −500; 250/250.
- L6: year one 400c + 100v, demand 1,600, II adds 100c + 50v, 9,800;
  then 10,780, 11,858 and exactly 65,219/5 = 13,043⅘, growth 20,219/45,000 =
  44.93%; second illustration 16,250/3, 3,250/3, 4,750/3, 947/3 and four-period
  growth 746,893/1,944,000 = 38.42%; `ii-short` needs 150 against 100.

## Quiz

Each question has exactly one defensible answer; I argued for every
distractor and could not make one stand. Two near-misses, left as they are
because the stem closes them: L3 q2 ("absorbed in the exchange within
Department I") is excluded only by "Under simple reproduction", which the stem
says; L6 q2 distractor 8,252 is diagram a's total and labelled as such in the
`why`.

## Critics and historians

Quesnay (court physician, Tableau 1758, economics in his sixties), Smith (1776),
Say (Traité 1803), Ricardo and James Mill on Say's law, Storch, Sraffa (1960,
dated labour), Leontief (input–output from the 1930s, tracing it to Quesnay),
Keynes (1936, saving and investment brought into line by income), the
loanable-funds view, Tugan-Baranovsky (1894), Luxemburg (1913), Bauer (1913),
Bukharin (1924): names, dates and positions are accurate and stated at
strength, and the lessons say that each later writer wrote after 1883.

## Voice (recommendations only, not changed)

- L2 "On most things Marx builds on Smith" is the lesson's verdict and broader
  than this chapter supports; "Marx credits Smith with real progress over
  Quesnay elsewhere in the chapter (the general concept of capital), and here
  says he went backwards" would stay with the text (l. 3698–3704).
- L6 "No part of Volume II has been argued over more" is a verdict in the
  lesson's voice; probably true, but "These schemes started a long argument"
  would claim less.
- L5 "it deserves its full strength" is slightly performed; the paragraph
  already gives Say at strength.
- L4's paragraph after the crisis quotation places "Such a surplus is not an
  evil in itself" after the post-capitalist remedy; in the text it comes before
  it and refers to the capitalist case. The juxtaposition does not misstate
  Marx, but quoting "in capitalist society it is an element of anarchy"
  (l. 4794) there instead would follow the order of the text.
- Otherwise the voice is natural and warm, opens on the passages' own figures as
  §F asks for the schemes, and every lesson's last paragraph points forward by
  title.

## Where I disagree with the pedagogy assessment

Read after the findings above were written.

1. **Proudhon.** The assessment lists Proudhon among the economists "stated at
   strength and in their own terms" and approves `mistakes[0]`'s refutation.
   The refutation figure is right, but the attribution says Marx faulted
   Proudhon for treating society as one firm, when at l. 4419 Marx himself
   treats it as one unit, "the aggregate capitalist", and faults Proudhon for
   thinking the unit loses its capitalist character (F1). This was the
   lesson's first misconception, and the §C entry carried the same error.
2. **The horse paragraph** is called "the best in the course", with "the one
   thing in the chapter that bears on" Sraffa being the one-year period. The
   chapter's direct answer to the regress, the condition that it would have to
   end in products of labour alone, and the Scotch pebbles, was missing (F3).
3. **The second illustration** "agrees with his rounded capitals throughout
   except for one misprint". It agrees to within a unit; two figures differ by
   one from what rounding the exact path gives (F7). The misprint finding
   itself is right.
4. **Lesson 6's Luxemburg paragraph** is praised as telling the reader which
   step is disputed, which it does, but neither the lesson nor the assessment
   noticed that the passage the lesson opens with ("accumulation in II must
   take place more rapidly than in I") is not borne out by the growth rates
   the lesson itself prints a paragraph later, and the lesson's "his figures
   show that it can" implied it was (F6).
5. **The `read_intro` position of the l. 5286 passage.** The assessment changed
   "after the second year" to "after the first year ... before he runs the
   second", saying Marx draws the rule "immediately after the first year's
   product of 9,800". He does not: between 9,800 and the rule comes the whole
   rearrangement for the second year (4,840c + 1,210v; 1,760c + 880v; 8,690).
   Both versions were loose; the lesson now says where it is.
6. **Lesson 4.** The assessment judges the fixed-capital lesson faithful and
   accepts "Marx is pleased with this" because the text says "convincing". I
   replaced the remark with Marx's word, which is a matter of taste; but the
   assessment did not catch that the lesson's "Marx's claim is narrower" both
   weakened "can and must arise" and gave Marx a claim (an industry equipped at
   once renews at once) that is not in the section, or that Mr. X illustrates
   the case Marx calls "seemingly absurd", not "ordinary prudence" (F4).
7. **Engels' note** in lesson 1 (F2) and the "seeming" difficulty in lesson 5
   (F5) are small, and the assessment did not mention either.

Where we agree: the arithmetic and every pinned tile are right; the 13,033 and
4,249 slip and the 6,385 misprint are correctly diagnosed; the later critics are
dated, stated at strength and kept apart from Marx's replies; the quizzes have
one defensible answer each; the voice matches §F. I have not re-checked the
speech overrides the assessment added, beyond the preview's report that no run
is unspoken.

## Files changed

- `content/capital/c08_reproduction/part_a.py`: lessons 1, 2, 4, 5 and 6 as in
  F1–F7 (prose, `mistakes[0]` of lesson 1, one concept card in lesson 5, one
  `read_intro`, line-number comments). No preset, `expect`, slug, lab, quiz
  item or spoken form changed.
- `docs/capital/PLAN.md`: Course 8, lesson 1, the Misconception line (F1).

Final preview, `python3 scripts/preview_subject.py capital --course
capital-social-reproduction`: 7 pages rendered; every lab executes (6 swept);
pinned figures match (6 pages with pins, 0 failing); `OK`. Strict quotation
checker: 75 segments, 0 misses.
