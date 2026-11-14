# Review (accuracy and teaching): Leviathan, Course 7, Wealth, Counsel, Law and the Office of the Sovereign

Course `leviathan-office-of-sovereign` (`content/leviathan/c7_office_of_sovereign/`), eight lessons on Chapters 24 to 31. Reviewed 2026-11-14 to `docs/leviathan/REVIEW.md` against the OCR and page images (PDF pp. 266–350). I did not read the whole text file, `site/` or Tuck's apparatus. I changed nothing except this file.

## Gates

- **Preview:** `preview_subject.py leviathan --course leviathan-office-of-sovereign`
  rendered 9 pages. Labcheck: 8 executed, 8 with pinned figures, 0 failing. **OK**.
- **Opening quotations, each checked on the page image:** all eight are exact and at most 120 words: 36, 83, 96, 48, 47, 38, 37 and 41 words. The author left Lessons 4, 5 and 8 unchecked: Lesson 4 (p. 299, LOOSE) is right to drop Tuck's `*if it be*¹` mark; Lessons 5 (p. 310) and 8 (p. 342, "rresistible") came back NEAR because of OCR errors. Lesson 2 (p. 277, NEAR) is also exact. The 1651 pages are correct: 127, 135, 137–138, 153, 171, 181 and 187, with one exception: Lesson 5 is p. 161 only (NOTE 1).
- **Inline quotations:** I checked all 107 `&ldquo;…&rdquo;` spans across the chapters' pages. Every one is in the text. Each NEAR, LOOSE or MISS result is an OCR error, which I confirmed on the image or in context (pp. 270, 297, 301, 311–312, 321, 333). The two phrases from p. 320 are correctly attributed to Chapter 29.
- **Browser (Playwright, chromium, `file://`):** I loaded all 8 lessons at 375 px and 1280 px: no sideways scroll and no errors. I ran all 25 presets. Every tile matches its pin, and every worked line matches my own arithmetic.
- **Typed:** sword with only the Church's payoff lowered (`0,-2`): both chicken equilibria and no dominance (MUST 1). Pair with labourer 180, 20 and idler 20, 30: consumption taxes 8 and 12 (MUST 5).

## MUST-FIX

1. **`part_b.py:397–401` and `:428`, the sword preset is misdescribed.** The prose
   changes only the Church's both-insist payoff ("costs it 2 and not 0") and draws the
   conclusion that the Crown's insisting then dominates. But the preset also raises the
   Crown's both-insist payoff from 0 to 4 (`[[4, -2]]`), and that change is what makes
   insisting dominate. With only the Church's change, the lab shows (Yield, Insist) and
   (Insist, Yield) with no dominance. Replacement: "In the sword preset, when both insist the
   Crown, with a sword behind its claim, gets 4 instead of 0 and the Church gets −2.
   Now the Crown's insisting dominates: against a yielding Church 5 beats 3, against an
   insisting one 4 beats 1. The Church's best answer to an insisting Crown is to yield,
   1 against −2." Label: "A sword behind the Crown: if both insist, the Crown gets 4 and
   the Church −2".
2. **`part_b.py:486–488`, the `why` for quiz item 1 gives the wrong figures.** At
   (Insist, Yield), an insister who switches gets 3 instead of 5, and a yielder who
   switches gets 0 instead of 1. The `why` reverses these ("the insister would get 0
   and the yielder 3 for 1"), Replacement: "At either cell where one insists and the
   other yields, neither wants to switch: the insister would get 3 instead of 5, and
   the yielder 0 instead of 1."
3. **`part_b.py:406–408` and `:518–519`, a claim the chapter does not make.** The
   cheap-war prisoner's dilemma is called "the dilemma of the factions of mixed
   government", and the quiz says it is "what Hobbes says of factions that can each
   hope to win". Hobbes says that mixed government is "three independent Factions" and
   endangers the commonwealth "somtimes for want of consent to good Lawes; but most
   often for want of such Nourishment", meaning money (PDF p. 324). He says nothing
   about each faction's hope to win, or about war being cheap. Body replacement: "That
   is a prisoner's dilemma, and it is the lesson's picture, not Hobbes's. Of mixed
   government he says only that its three independent factions endanger the
   commonwealth for want of consent to good laws and, most often, for want of money."
   Quiz replacement: "… So both insist, and the 2 each is below the 3 each of both
   yielding. That is a dilemma, a picture the lesson draws and Hobbes does not."
4. **`part_b.py:890–895` and `:981–983`, the mixed preset is given to the wrong
   reader.** The counterexample (`c` false, `p` true, `q` false) needs God not to have
   created men, and the creation reader denies exactly that. The objection of "a reader
   who grounds the right in creation" is power without right, the row with `p` true and
   `q` false that falsifies `p → q`. That row is the strip preset's counterexample, not
   the mixed one. Body replacement from "The mixed preset is that reader": "That
   reader's case, God with the power and without the right, is the strip preset's row,
   `p` true and `q` false. The mixed preset shows the other half of the reader's view:
   power joined only to the creation link, `p` and `c → q`, does not yield `q`. Its one
   counterexample has `c` false, so on that view the power does no work and the right
   rests on creation." `after` replacement: "One row breaks it: `p` true, `c` false, `q`
   false. With only the creation link, power proves nothing unless creation is granted
   too. The creation reader's objection to Hobbes, power without right, is the strip
   preset's row."
5. **`part_b.py:652–655` and `:692`, "That is Hobbes's pair" is not Hobbes's pair.**
   Hobbes asks why "he which laboureth much, and sparing the fruits of his labour,
   consumeth little" should be charged more than one who "spendeth all he gets"
   (PDF pp. 334–335). In the preset the labourer consumes 30 and the idler 20, so the
   labourer still pays more under Hobbes's own rule (12 against 8). The lab then shows
   the opposite of the passage. Replacement: persons `[["labourer", 180, 20],
   ["idler", 20, 30]]`, revenue 20. I typed this in: on riches 18 and 2, on
   consumption 8 and 12, `ltxMore` "1: idler". The prose becomes "the labourer, with
   riches 180 and consumption 20, and the idler, with 20 and 30, … on consumption 8 and
   12: the man who spares pays less." Re-pin `ltxOnConsumption` to "labourer 8; idler
   12". In quiz item 3 (`:747–754`) the right answer becomes 8. The options become
   `["18", "2", "12", "8"]` with `c: 3`, and the `why` becomes "The consumption total
   is 50, so the rate is `2/5`, and `20 · 2/5 = 8`. Eighteen is his tax on riches; 2
   and 12 are the idler's."

## SHOULD-FIX

1. **`part_a.py:938`.** The prose says "only 37.5". The tile prints `75/2 = 37.50`.
   Write "only `75/2`, 37.50".
2. **`part_a.py:920–922`.** "A penalty heavier than the law named is not the
   offender's responsibility" loosens Hobbes's claim. He says the delinquent "is
   Excused from a greater penalty" (p. 299). Write "and a man is excused any penalty
   heavier than the law named, because …".
3. **`part_b.py:261–265`, mistake 3.** It says hostility "is not done as the
   commonwealth's act" and that "the word does not say the act is forbidden". The
   eighth inference's excess *is* inflicted by public authority, and "all infliction of
   evill is lawfull" holds only "in declared Hostility" against an enemy. Harm to an
   innocent subject is "against the Law of Nature" (p. 315). Write: "Hobbes means a
   harm that is not punishment. Against a declared enemy all infliction of evil is
   lawful. Inflicted on a subject beyond the law, it falls outside the definition, and
   the delinquent is excused from it."
4. **`part_b.py:143–144`.** "From the close of the book of Job" is inaccurate. Hobbes
   says "the two last verses of the one and fortieth of Job" (p. 317). Write "from the
   last two verses of Job 41".
5. **`part_b.py:98`.** "I count eleven" is first person (PLAN §F). Write "There are
   eleven".
6. **`part_b.py:916–918`.** Hobbes limits what the sovereign ordains as signs of honour
   to actions "of an indifferent nature". Naturally contumelious acts "cannot be made by
   humane power a part of Divine worship" (p. 349). Add "among actions indifferent by
   nature".

## NOTE

1. `part_b.py:13`: "pp. 161-162" could be "p. 161". The definition ends before `[162]`.
2. Kit (for the `levkit` owner): in the price preset (certainty 1), `llwStatus` says
   "the hope of impunity makes the crime pay", but at certainty 1 there is no hope of
   impunity. The status should say "the penalty is below the gain". choicekit's
   `voStatus` reads "1 independent jurors" for n = 1.
3. Checked against the pages and found right: Chapters 24 to 27 (Canaan, Cicero, Coke and 1634, the marks of good counsel, the numbered consequences, the sources and degrees of crime), Chapter 28's eleven inferences, Chapter 29's six doctrines and historical examples, Chapter 30's tax passage and Chapter 31's Job and Plato. Condorcet, Kant and Locke are each given their position at full strength.

**Verdict:** the gates pass and the quotations are exact. Fix the five MUST items, all
in Lessons 6 to 8, before the course ships.
