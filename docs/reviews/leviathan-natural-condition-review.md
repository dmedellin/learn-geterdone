# Review (accuracy and teaching): Leviathan, Course 4 — The Natural Condition and the Laws of Nature

Course `leviathan-natural-condition` (`content/leviathan/c4_natural_condition/`), seven lessons, against
`docs/leviathan/PLAN.md` §C Course 4, §D, §E, §F and `docs/leviathan/AUTHORING.md`. I read Chapters 13–15
in full (PDF pp. 182–207) with `page.py`, checked quotations with `quotes.py` and the page images, and
compared lesson 2 with Philosophy's "Hobbes and the State of Nature" (`content/philosophy/c5_games/part_b.py`).
I did not read `site/` or Tuck's apparatus. I wrote only this file.

## Gates

- **Preview:** 8 pages rendered. Labcheck: 7 executed, 7 with pinned figures, 0 failing. **OK**.
- **Quotations:** 227 `&ldquo;…&rdquo;` spans. 179 are OK in `quotes.py`. 9 are LOOSE, all from small
  capitals ("CONTRACT", "MERIT", "INJUSTICE", "PARDON"), and they are fine. The rest were checked
  by fuzzy match and on the image: 8 are lesson or course titles, and the others are OCR noise or page
  breaks. Four are real misquotes (MF-1). Every opening quotation is under 120 words (the longest
  is 78). Every PDF page in the comments is right.
- **Browser:** I loaded all 8 pages in Playwright chromium at 375 and 1280 px. No page scrolls sideways
  and none logs a page or console error.
- **Tiles:** I worked every figure out by hand and all of them match the prose:
  - Equality presets: 2/1/1…, 6 of 6; machination 12 > 10; giant 4, 26; beyond 29 < 30.
  - The three games: competition dominance; diffidence mixed equilibrium at 2/3 (5q = 2 + 2q); pair
    with Attack dominant for column.
  - Validity: 16/0, 16/1, 16/1.
  - Covenants: 1/9/−5/8; hire −6; loan −10; tie 1/1; sword 0, +3; misses 9/2 with a least sanction of 16; oath −1.
  - Fool: 10, 5, 0, −10, −40; perish 1/100; kingdom 98, 90, 80.
  - Iterated: 30, 25, 27/32, 0/50, 0/5. I recomputed the round robin: ten rounds give TF2T 185, TFT 184,
    ALLC 177, PAVLOV 173, GRIM 172, ALLD 146, STFT 145. One round gives ALLD and STFT 27 and every other strategy 15. The lab's table prints all of these.
- **Quiz arithmetic:** I checked it by hand. 2.3 gives 5/2 against 3 and 5/3 against 8/3; 5.2 gives 16; 6.1 gives 1/10.

## MUST-FIX

1. **Four quotations are not as printed.** I checked each against the page image.
   - `part_a.py:846`: the text has "leave the other to **perform** his part" (p. 190). Change `performe` to `perform`.
   - `part_b.py:86`: the text has "is to **per-form** first" (p. 192). Change it to `perform first`.
   - `part_b.py:98`: the text has "other **signe** of the Will" (p. 192). Change `sign` to `signe`.
   - `part_b.py:259`: the text has "It appears also, that **the** Oath addes nothing" (p. 196). Use
     `&ldquo;the Oath addes nothing to the Obligation.&rdquo;`
   - `part_a.py:323` has the same fault at smaller scale: the text reads "**And from** this diffidence"
     (p. 183). Use `&ldquo;from this diffidence of one another, …&rdquo;`.

2. **`part_a.py:1047` (note, lesson 4) gets Hobbes's two helps wrong.** The note says Hobbes allows two
   things that hold a man to his word "besides fear": glory, and "the fear of what unseen powers will
   do". The text says the two helps *are* fear and glory. The power of spirits invisible is one of
   the two objects of fear (p. 195). Replace with: "Hobbes names two helps to strengthen a covenant,
   fear of the consequence of breaking it and glory in not needing to break it, and calls the second
   too rare to presume on. The figures here include neither: the lab's second party has no fear and no pride."

3. **`part_a.py:297–298` and `:465` (lesson 2) say Hobbes calls diffidence reasonable.** He does
   not. What he calls reasonable is anticipation, the response to diffidence: "no way for any man
   to secure himselfe, so reasonable, as Anticipation" (p. 183).
   - Concept: "Diffidence is the cause behind the move Hobbes calls reasonable: from it, the best
     way to secure oneself is anticipation, …"
   - Worked `after`: "This is Hobbes's diffidence, and attacking first is what he calls the reasonable
     answer to it."

4. **Lesson 2 repeats the Philosophy lesson and says it does not (`part_a.py:314`, `:398–410`, `:511`).**
   "Hobbes and the State of Nature" already writes competition as the dilemma (3/0/5/1) and diffidence
   as the stag hunt with a mixed threshold (3/4). It also has the mistake "Thinking Hobbes took people
   to be wicked" and the note that glory has no payoff. Lesson 2 has the same two tables with new
   numbers (4/0/6/1, 2/3), the mistake "Thinking Hobbes calls men wicked", and the same note on glory.
   PLAN §C asks for the two games, but "does not repeat that lesson" is false as written. The new
   material is the pair preset, from the paragraph on those who take pleasure in conquest, which
   Philosophy does not have. Fix:
   - (a) Cut the competition and diffidence paragraph to two sentences that point to the Philosophy
     lesson for the general shape and give only this lesson's figures.
   - (b) Make `pair` the default preset and the subject of the worked example.
   - (c) Replace mistake 1 with "Thinking the war needs a majority of aggressors", answered by the pair table.
   - (d) Change read_intro to: "… writes competition and diffidence as tables and adds a sovereign's
     fine. This lesson takes those tables briefly and adds the third case, the immoderate few."

5. **The reply to the Fool is softened into "the chance cannot be set low" (`part_b.py:418–422`, `:485`, `:500–502`, mistake at `:549`).**
   Hobbes does not argue about how sure the Fool may be. He makes two points. Reason judges an act
   by what "can be foreseen, and reckoned on", and a lucky outcome "do[es] not make it reasonably or
   wisely done". And the breaker "declareth that he thinks he may with reason do so", so he can be
   kept in society only by others' errors, "which errours a man cannot reasonably reckon upon"
   (pp. 198–199). Put into the lab's terms, the reckoning may not count on being undetected at all.
   The breach is itself the declaration. So the chance Hobbes allows is in effect `1`, and breaking
   is worth `gain − loss`.
   - Worked `after` (`:500`): "On Hobbes's reply the Fool may not count on escaping at all: his
     breach declares him, and only others' errors could keep him in. At chance `1` breaking is worth
     `10 − 100 = −90`."
   - Step 4 (`:485`): "Hobbes's reply is that a man may reckon only on what can be foreseen, and
     others' errors cannot be, so the reasonable chance is certainty."
   - Add `"1"` to the `ruin` chances, so the lab prints `1 = 100%: −90`.
   - Keep the kingdom paragraph. There the reply is about the gain ("cannot reasonably be expected,
     but rather the contrary"), which the lesson already states correctly.

6. **`part_b.py:428–431`: Hume did not "give the Fool a new name".** The sensible knave of the
   *Enquiry* (1751, §IX pt. II) never mentions Hobbes. The comparison is one readers make. Replace with:
   "David Hume's sensible knave, in the *Enquiry concerning the Principles of Morals* of 1751, is
   often read beside the Fool: a man who thinks he may profit by a breach that goes unseen. Hume
   answered that …"

## SHOULD-FIX

1. **`part_b.py:363`: "He comes from the Psalms".** Hobbes does not cite the Psalms. The echo is
   well known, but it is the kind of thing an editor's footnote supplies. Write "The opening words
   echo Psalm 14, 'The fool hath said in his heart, There is no God', and Hobbes makes the link
   himself: …", or drop the clause.
2. **`part_b.py:114–116`: "Hobbes's page is about promises of exactly that kind."** Chapter 14 does
   not mention the Engagement. Write: "and could read this page as about promises of exactly that kind."
3. **`part_b.py:514–523`, quiz 6.2.** Option D ("there is no God") can be argued for, because the
   text says "the same Foole hath said in his heart there is no God". Change the question to "What
   does the Fool say about covenants?"
4. **`part_b.py:679`: "a man who always helps is not preyed upon".** In the field, ALLC scores 0
   against ALLD and is exploited once by STFT. Write: "… a man who always helps is preyed upon only
   by the two strategies that refuse, and still finishes third."
5. **`part_b.py:695`: "He pauses on justice of actions …"** The commutative/distributive passage
   comes before the fourth law (p. 201), not after the nineteenth. Write: "Before the fourth law he
   had paused …"
6. **`part_a.py:380–383` is ungrammatical.** "It is not a faculty … but are 'Qualities…'". Write:
   "Justice and injustice are not faculties of body or mind, for if they were they 'might be in a man
   that were alone …'; they are 'Qualities, that relate to men in Society, not in Solitude'."
   Also, at `:384`, "nothing is any man's but 'that to be every mans…'" garbles the text. Write:
   "no mine and thine distinct, 'but onely that to be every mans, that he can get; …'".

## NOTE

1. `part_a.py:335`: "Glory has a second form" counts the pleasure in conquest as glory. Chapter 6's
   definition of glory supports this, but Hobbes does not name it in Chapter 13. One clause citing
   Chapter 6 would help.
2. `part_b.py:693`: "no man a judge in his own cause or where he profits by one side's victory" puts
   the seventeenth and eighteenth laws in one clause. The count of nineteen is right: the text numbers
   the laws to the ninth, and the margins go on to the nineteenth (pp. 201–205).
3. Lesson 5's refusal to fit the two statements of the rule together (`part_b.py:100–104`) could give
   Hobbes's own fit at strength: suspicion is reasonable when it rests on a sign arising after the covenant.
4. Machination as a multiplier on strength (lesson 1) is the lesson's model, and the lesson says so.
   It is fine as written.
5. Small capitals are printed in ordinary case throughout ("Contract" for CONTRACT). The other courses
   do the same, and this course is consistent with them.
6. I found nothing drawn from Tuck's notes. The "Syn." and scribal-manuscript notes on pp. 182, 188,
   191 and 200 are not used.

## Verdict

Accurate on the laws of nature, their count and the covenant rules, and the labs are honest. Fix the
four misquotations and the fear/glory slip, give the Fool Hobbes's own reply rather than a softened
one, and stop lesson 2 from re-teaching the Philosophy tables while saying it does not.
