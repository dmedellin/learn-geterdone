# Second review — Wages and Accumulation (Capital, course 4)

This is an independent second read of `content/capital/c04_accumulation/`
(`__init__.py`, `part_a.py` and `part_b.py`) on branch `feat/capital-subject`.
It follows `docs/capital/SECOND-REVIEW.md`. I wrote the findings below before
reading `docs/pedagogy/capital-wages-and-accumulation.md`. The last section
compares the two.

## Method

- **Reading against the text.** I read every lesson in full against Volume I,
  Chapters 19 to 25 of `/mnt/project-files/capital-texts/volume-1-kerr.txt`
  (ll. 3936–4731, plus the parts of §5 that the course cites: Gladstone,
  official pauperism, Dr Smith and Ireland). I checked every sentence that
  says what Marx argues, replies or concludes against the line that should
  support it.
- **Quotations.** I ran
  `scratchpad/tools/strict_quotes.py c04_accumulation 1` before and after the
  changes.
- **Arithmetic.** I recomputed every figure in prose, worked lines, quiz
  answers and `why`s by hand. I also wrote an exact-fraction copy of the
  kit's `acRun` loop, and it reproduced every pinned accumulate tile before I
  relied on it. I rendered with `preview_subject.py` into
  `scratchpad/c04rev/` and read every preset's tiles with
  `labcheck.js --observe`.
- **Quiz.** I argued for every distractor.

## Verdict

The arithmetic is right almost everywhere. Every pinned tile, every worked
line and every quiz answer recomputes exactly. The figures I checked include:

- the wage figures 3 3/5d, 2 2/5d, 3s 7 1/5d and 1s 9 3/5d;
- the national-wage rates 5/3 and 1/3 and the relative wages 3/4 and 3/2;
- the accumulation totals £124,416/5 and £161,051/10, and the original
  capital's share of them, 40.19% and 62.09%;
- `tight` (s of £3,600, £26,525/2) and `wage-rise` (s of £2,800 down to
  £1,181 1/4, and £81,825/8);
- the boom path (wages of £80/7, £185/16 and £23/2; capital of £34,200;
  1/19);
- the long run at 10 periods (9/10).

**One arithmetic fault was in a preset:** `slump` employed a fractional
171 3/7 workers in period 4.

**Two `why`s and one mistake misdescribed the lab:**

- the supply "the same in all three presets";
- "the slump's reading" of falling wages, in a lab that never lowers a wage;
- "600 is the variable capital".

**The fidelity defects follow Course 1's pattern.** There were four places
where the lesson gave Marx a reply or a verdict the text does not contain:

- a reply to an objection Marx never takes up;
- a "Marx's reply" to Marshall, Böhm-Bawerk and Fisher;
- a refutation of abstinence by a computation Senior would accept;
- "mocking" where the text also pays tribute.

There were also several smaller paraphrase slips. Three quotations changed
the case of their first word. All of these are fixed. The course renders OK
and every pin matches.

## Findings and changes

### Fidelity to Marx

1. **`surplus-value-into-capital`, body (Marshall paragraph): "Marx's reply"
   to writers after his death.** The paragraph presented Marshall (1890),
   Böhm-Bawerk (1889) and Fisher (1907), then said "Marx's reply works at the
   level of the class". Marx died in 1883. That is the exact construction
   AUTHORING's Course 1 lessons forbid.
   **Changed** to: "Marx died before any of them wrote. What his chapter says
   against Senior bears on their version at the level of the class: …". I
   replaced the paraphrase "consumption grows with his accumulation rather
   than being sacrificed to it" with Marx's own words, quoted: the
   capitalist's expenditure "grows with his accumulation, without the one
   necessarily restricting the other" (l. 4439).

2. **`surplus-value-into-capital`, `mistakes[0]`: abstinence was "refuted" by
   a computation the critic accepts.** The mistake made three points:
   - the half preset consumes £1,000 and adds £1,000;
   - what is added is surplus value;
   - "nearly three fifths of the capital was never anybody's to abstain
     from".

   Senior accepts the first. Indeed it *is* his abstinence: £1,000 not eaten.
   The second is Marx's definition, not a refutation. The third is the
   lesson's own verdict, in its own voice, and it contradicts the arithmetic:
   that surplus value was the capitalist's to consume, which is the whole
   point of the split in §3.
   **Changed** to name Senior's claim and grant what the preset grants. The
   new text gives Marx's point about the source (about three fifths
   capitalised surplus value, on his definitions) and the chapter's actual
   answer (expenditure grows with accumulation, quoted). It ends: "Whether
   forgone consumption earns a reward is what Senior's successors and Marx
   dispute; the arithmetic is common to both."

3. **`surplus-value-into-capital`, body and `read_intro`: "Moses and the
   prophets" read as mockery only.** The lesson said Marx "is mocking the
   economists" and that the passage is "a joke at the expense of the
   economists who preached it". The passage itself goes on to say that
   classical economy "did not for a single instant deceive itself over the
   birth-throes of wealth". The next lines say that "Political economy takes
   the historical function of the capitalist in bitter earnest" (l.
   4445). It is a parody and a tribute at once, and it marks the
   contrast with the vulgar economy (Senior) that follows.
   **Changed** both places to say so, quoting "in bitter earnest".

4. **`simple-reproduction`, body (the accountant objection): "Marx's reply"
   to an objection he does not raise.** The lesson stated the objection well:
   money has no label, so one could equally say the capitalist spent his
   profits and kept his capital. But it then gave "Marx's reply". Chapter 23
   never takes up that objection.
   **Changed** to: "Marx does not take up this objection in so many words.
   What the chapter sets against it is that the question concerns 'not the
   material elements, but the value' of the capital …". The quotation is from
   l. 4256. The rest of the paragraph, including the closing "not making an
   arithmetic mistake", is unchanged.

5. **`simple-reproduction`, body (cotton famine): the emigration was
   "prevented", not "not paid for".** Kerr l. 4297: "Their emigration was
   prevented". The old text also left the reader unsure whose phrase "moral
   workhouse" was. It was the *Times*, mocking Potter.
   **Changed** to: "The *Times* mocked Potter for wanting half a million
   workers kept in a great 'moral workhouse', but public opinion, Marx says,
   was Potter's: the emigration was prevented …".

6. **`simple-reproduction`, body: "like oiling a machine".** The oil-and-coal
   image (l. 4268) belongs to the case Marx calls an abuse: individual
   consumption made a mere incident of production. The class-level point
   uses a different comparison, "just as cleaning machinery does" (l. 4272).
   **Changed** to "like the cleaning of machinery".

7. **`value-of-labour-power-into-wages`, body: what the economists
   borrowed.** The lesson said the economists borrowed the phrase "value of
   labour" from everyday life "without asking what it could mean". Kerr l.
   3962 says they borrowed the category "price of labour" without criticism,
   and "then simply asked the question, how is this price determined?". The
   old line also said "Marx does not say the payslip lies". That undersells a
   form that "shows the direct opposite" of the relation (l. 3976).
   **Changed** to: Marx does not call the payslip a fraud; it is a surface
   that arises from the relations of production and yet shows the opposite of
   what lies under it. The economists took "price of labour" from everyday
   life without criticism and asked only how the price is determined.

8. **`time-wages`, body: the overtime computation was detached from its
   target, and "enjoys it" was the lesson's verdict.**
   - The 3d/4d overtime arithmetic is Marx's answer to the full-priced
     baker, who "insists upon extra pay" for overtime and does not see that
     it includes unpaid labour (l. 4047). The lesson placed it under "Marx
     takes the employer at his word" and then, separately, said Marx "calls
     their complaint a jeremiad and enjoys it".
   - Marx says the jeremiad is "interesting because it shows how the
     appearance only … mirrors itself in the brain of the capitalist".

   **Changed:** the overtime paragraph now gives Marx's "ridiculously small"
   extra pay and says he computes what it leaves unpaid. The bakers'
   paragraph calls the complaint a jeremiad "interesting for what it shows",
   and ties the 4d hour to the baker who insists on extra pay.

9. **`surplus-value-into-capital`, body (Aikin): "by 1758".** Kerr l. 4443:
   "It was not till 1758, and this marks an epoch, that a person actually
   engaged in business was seen with an equipage of his own." "By 1758"
   reverses the point.
   **Changed** to "not until 1758, an epoch, Marx notes".

10. **`the-general-law-of-accumulation`, `read_intro`: "the sentence most
    quoted from the whole of Volume I".** That is an unverifiable
    superlative in the lesson's own voice.
    **Changed** to "among the most quoted sentences of Volume I, and among
    the most argued over".

### Quotations

The strict checker went from 5 misses to 2.

**Fixed: three first-word case changes, which AUTHORING forbids.**

- `accumulation-with-constant-composition`, quiz 3: "&ldquo;to put it
  mathematically&rdquo;" (text: "To"). Reworded to "Putting the relation
  'mathematically', Marx says …".
- `the-general-law-of-accumulation`, body: "&ldquo;the lowest sediment of
  the relative surplus-population&rdquo;" (text: "The"). The full sentence
  is now quoted: "The lowest sediment of the relative surplus-population
  finally dwells in the sphere of pauperism."
- `the-general-law-of-accumulation`, body: "&ldquo;Be his payment high or
  low&rdquo;" at the head of a sentence (text: "be"). Reworded so that the
  quotation sits mid-sentence.

**Convention only: two drop capitals, left as they are.**

- `value-of-labour-power-into-wages`, opening passage ("ON the surface").
- `piece-wages`, opening passage ("WAGES by the piece").

All the other 74 segments are found verbatim. Every quoted span in the
critics' paragraphs is in the Kerr text:

- Bellers, Mandeville and Eden;
- Merivale, Cowell and Carey;
- Gladstone and the *Times*;
- Senior.

### Arithmetic and the lab

11. **`the-general-law-of-accumulation`, preset `slump`: fractional
    workers.** At £6,000, c/v 1 rising by ½, period 4 has v = £6,000/3.5 and
    employs 171 3/7 workers. The table printed that fraction. This is the
    issue the orchestrator flagged.
    **Changed** `capital` to 4200, keeping everything else. Employment is now
    210, 168, 140, 120 and 105 against supplies of 300 to 420. The reserves
    are 90, 162, 220, 270 and 315, and the ratio runs from 3/7 to 3.
    Re-observed with `labcheck --observe`, the tiles are `3 = 300%`, `315`
    and `105`, and I re-pinned `expect` to them. The label now names the
    £4,200.

    The lab paragraph now says the boom and the long run start from £6,000
    and the slump from £4,200. It gives the slump's employment path and the
    ratio from `3/7` to 3. `docs/capital/PLAN.md` §C, Course 4, lesson 9 is
    updated, with a "Changed in second review" note.

12. **`the-general-law-of-accumulation`, preset `boom`: the point shows only
    in period 5.** I agree with the orchestrator, and I tried to fix it.

    **What I searched.** I ran an exact replica of `acRun` over a range of
    instances:
    - capitals from £600 to £30,000;
    - s/v of 100%, 200% and 300%;
    - c/v rising by ½ or 1;
    - starting wages of £5 to £20 and wage steps from 1s to £10;
    - starting supplies of 100 to 500 and supply growth of 0 to 300;
    - all of s capitalised, or half.

    **What I found.** No instance has a rising composition, a wage on its set
    path rising every period, whole-number employment in every period, and a
    reserve ratio rising over three or more periods. The obstruction is
    structural. When the supply does not bind, employment is v over a wage
    that moves by a fixed step, and v moves by a factor that depends on that
    wage. The only near-misses had employment *falling*, which is not a boom.
    I left the preset as it is.

    The prose already says plainly that the reserve forms only in period 5,
    and that "between the first period and the last, the wage and the
    reserve both rose". I added the table's own wage strings (£80/7,
    £185/16, £23/2) beside the "about £11 9s" conversions, so that the reader
    can find them. §C records the search.
    **Recommendation:** if a boom that shows the ratio rising period by
    period is wanted, it needs a kit change, such as a wage path given as a
    list or employment allowed in fractions of a worker. That is outside
    this review's remit.

13. **`accumulation-with-constant-composition`, `mistakes[1]`: "the supply is
    the same in all three presets".** It is not. It grows by 100, 40 and 0.
    **Changed** to: the supply is an input that grows by a fixed number each
    period whatever the wage does, and the wage rises only when accumulation
    outruns it, as in the tight and wage-rise presets.

14. **`the-general-law-of-accumulation`, quiz 3 `why`: "Falling wages are the
    slump's reading of the law".** No preset lowers a wage; the kit never
    does, and `slump` has a wage growth of 0.
    **Changed** to say so, and to argue the other two distractors from the
    tiles.

15. **`the-reserve-army`, quiz 1 `why`: "600 is the variable capital at
    1:1".** At 1:1 the variable capital is £6,000; 600 is the number of
    workers it employs.
    **Changed** to "600 is the employment at 1:1".

16. **`surplus-value-into-capital`, body: pound figures the tiles do not
    print.** The prose gave £24,883 4s and £16,105 2s, while the tiles print
    £124,416/5 and £161,051/10.
    **Changed:** both tile strings are now given beside the conversions.

### Quiz

I argued for every distractor in all 36 questions. Apart from the two
`why`s above (14 and 15), each question has exactly one defensible answer.
Two came closest to a second answer, and both hold:

- In `value-of-labour-power-into-wages`, quiz 2, "a share of the product" is
  close to the economists' formula that Chapter 23 mentions. The words "paid
  in advance" make it wrong.
- In `national-differences-of-wages`, quiz 3, "that its labour is more
  productive" is the cause of the higher nominal wage in Marx's chain, not
  something it fails to prove.

### Voice and smaller matters, left as recommendations

- **`time-wages`, the Robbins paragraph.** "The worker takes it or leaves
  the job" is the lesson's gloss, not a line of Chapter 20. It would be safer
  as "and that the worker does not choose it".
- **`the-general-law-of-accumulation`, `mistakes[2]`.** "It is a tendency
  stated from the definitions, not a prediction for every year" is a
  reading. Marx calls it "the absolute general law" and says it is "modified
  in its working by many circumstances". Say that, and leave "tendency" to
  the key line or to a named interpretation.
- **`accumulation-with-constant-composition`, the Solow paragraph.** "The
  view he opposed is not foolish" is mild and fair. It is still the lesson's
  verdict, and "is stated at strength in a modern form" would avoid it.
- **`time-wages`, Marx's "6 or 8 hours … 2s. or 1s. 6d."** Marx's order is
  crossed (6 hours give 1s 6d). The quotation is faithful, but a reader may
  stumble on it. One clause, "in the reverse order", would help.
- **Spelling.** `piece-wages` had "dryly" and `the-reserve-army` "drily". I
  made both "drily".
- **The voice works.** It is warm and plain throughout, and §F's openings
  from the reader's own world (the payslip, piece-rates per delivery, wage
  comparisons in the news) are earned, not forced.

## Preview

```
python3 scripts/preview_subject.py capital --course capital-wages-and-accumulation --out scratchpad/c04rev
10 page(s) rendered …
labcheck, pinned figures match: 9 page(s) executed and swept, 9 with pinned figures, 0 failing
OK
```

## Where I disagree with the pedagogy assessment

I read `docs/pedagogy/capital-wages-and-accumulation.md` only after the
findings above were written. Its arithmetic repairs are right: "nearly three
fifths", the boom's wage path, and the wage-rise preset's first period. I
agree with its account of the voice, the modern critics' dates and the
structure of the course. I disagree in nine places.

1. **"Fidelity to Chapters 19–25 is high."** It is high in the reading of
   Chapter 25, but four fidelity defects were in passages the assessment
   praised or passed:
   - **Lesson 6, Marshall, Böhm-Bawerk and Fisher.** The assessment says
     their account is "given its strongest form … before Marx's class-level
     reply". A reply by Marx to writers of 1889–1907 is the anachronism the
     Course 1 review named (finding 1).
   - **Lesson 6, `mistakes[0]`.** The assessment cites "The half preset
     consumes £1,000 of the first year's surplus value and still adds £1,000
     to capital" as a misconception "refuted with the specific figure". It
     corrected only "five ninths". But the figure is one Senior accepts: it
     is his abstinence. The line "never anybody's to abstain from" was the
     lesson's own verdict (finding 2).
   - **Lesson 5, "Marx's reply" to the accountant objection.** The
     assessment praised the paragraph's closing sentence, but Chapter 23
     never makes that reply (finding 4).
   - **Lesson 6, "Moses and the prophets" as mockery.** The assessment
     accepted it. The text pays tribute in the same sentence (finding 3).
2. **"One light remark … None is the lesson's own invention."** "Marx calls
   their complaint a jeremiad *and enjoys it*" is the lesson's invention. Marx
   calls the jeremiad "interesting" for what it shows (finding 8). The
   overtime arithmetic it follows was also detached from the baker it
   answers.
3. **The quotation misses.** The assessment counts all five as "a difference
   of initial or drop capital only". The two drop capitals are convention.
   The three first-word case changes are not: AUTHORING's Course 1 lessons
   say to reword around a quotation rather than change its case. All three
   are now reworded.
4. **"No phrase was invented" is true, but three paraphrases misstated the
   text:**
   - "borrowed 'value of labour' … without asking what it could mean"
     (lesson 1);
   - the emigration "not paid for" where Marx says it was "prevented"
     (lesson 5);
   - "by 1758" where Marx says "not till 1758" (lesson 6).

   These are findings 5, 7 and 9.
5. **"Every other distractor … could not be defended".** That holds for the
   distractors, but three explanations misdescribed the lab:
   - quiz 3 of lesson 9 assigned falling wages to the slump, which never
     lowers a wage;
   - quiz 1 of lesson 8 called 600 "the variable capital";
   - `mistakes[1]` of lesson 7 said the supply is "the same in all three
     presets".

   These are findings 13–15.
6. **The boom preset.** The assessment proposes "an instance in which the
   supply stays ahead of demand throughout … with integer workers it needs
   new figures". I searched for one with an exact replica of the engine
   (finding 12) and found none in a broad range. When the supply does not
   bind, a wage rising by a fixed step makes whole-number employment
   impossible with a rising composition, except in instances where
   employment falls. So the fix is a kit change, not new figures.
7. **The slump preset.** I agree, and I made the change the assessment
   recorded: £4,200, re-observed and re-pinned, with §C updated (finding
   11).
8. **`simple-reproduction`, quiz 1.** The assessment replaced two
   untestable distractors, but kept 3, which its own `why` still describes
   as coming "from no division of these two figures". It still tests
   nothing.
   **Changed** to 1/5, the division upside down, which the `why` now names.
9. **Lesson 8 as the course's heaviest lesson, and lesson 9's worked example
   starting from a given capital.** I agree with both, and have nothing to
   add.
