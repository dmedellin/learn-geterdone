# Review (accuracy and teaching): Leviathan, Course 5 — Persons and the Generation of a Commonwealth

Course `leviathan-generation-of-commonwealth` (`content/leviathan/c5_commonwealth/`), six
lessons, Chapters 16–19, built to `docs/leviathan/PLAN.md` §C Course 5. Reviewed
2026-11-14 against the private OCR and page images (PDF pp. 207–234), with `page.py`,
`quotes.py` and Playwright. I wrote only this file.

## Gates

- **Preview:** `preview_subject.py leviathan --course leviathan-generation-of-commonwealth`
  rendered 7 pages; labcheck 6 executed, 6 with pinned figures, 0 failing; **OK**.
- **Quotations:** 125 `&ldquo;…&rdquo;` spans. Every Hobbes quotation is on the page cited
  (pp. 208–234), and the longest is 92 words (6, opening). I checked every LOOSE/NEAR result
  on the image: OCR errors only (`ot`, `isa`, `[niquity`, `Natural]`, `Anistocragy`,
  `Artificial` for `Artificiall`, italics), **except two misquotes** (MUST 4, 5). About
  15 spans are not Hobbes's words (lesson titles, the lab's letter glosses, "the crowd",
  "no wrong"): see SHOULD 2. The source comments' PDF and 1651 pages are right.
- **Browser** (chromium, `file://`). No sideways scroll at 375 px on any lesson, and no
  console or page errors. Every preset loaded, and the tiles match the prose:
  `full` Valid/0; `no-authority` Invalid/1 (p=F q=T r=F); `beyond-commission` Invalid/1
  (p=T q=F r=F); `six-even` mute 3–3; `seven` 4–3 +1; `one-abstains` 3–2, and with rule
  `absolute` "fails: 3 of 6 members say yes"; `men` Defect dominates, k* = 0, total 100,
  alone +4 / everyone −5; `penalty-3/4/5` as stated; `hobbes` Valid; `trust` row b=c=f=T;
  `other-release` b=F c=F f=T; `cycle` army > wall > fleet > army; `settled` fleet;
  succession lines as stated. Exercises typed in: lesson 1 quiz 2 (`p & q -> r; p` ⊢ `r`)
  gives one row, p=T q=F r=F; lesson 2 quiz 1 (5 yes, 4 no, 2 abstain) passes 5 to 4, +1;
  lesson 3's smallest penalty is 5. I worked every worked line by hand, and all are correct.

## MUST-FIX

1. **`part_a.py:119-121`, the wrong party is obliged.** The lesson says "the author was
   already obliged to obey him". Text (PDF p. 209): "When the Actor doth any thing against the
   Law of Nature by command of the Author, if he be obliged by former Covenant to obey him":
   the *actor* is obliged to obey the *author*. Replace with: "If the actor does something
   against the law of nature on the author's command, and the actor was already obliged by
   covenant to obey him, &ldquo;not he, but the Author breaketh the Law of Nature&rdquo;".

2. **`part_a.py:113-116` and `268-273`: an invalid argument is read as Hobbes's conclusion.**
   In `no-authority` and `beyond-commission` the lab shows only that `r` does not follow. The
   prose turns that into "the author is not bound" (and the mistake turns it into "the author
   is still not bound"). Getting `~r` from `p & q -> r` and `~p` is denying the antecedent
   (typed in: Invalid, 2 rows). Hobbes's ground is the converse (PDF pp. 208–209): "no man is
   obliged by a Covenant, whereof he is not Author; nor consequently by a Covenant made
   against, or beside the Authority he gave". Fix: add a preset
   `{"id": "not-author", "premises": ["r -> p & q", "~p"], "conclusion": "~r"}` (typed in:
   Valid, 0), pin it, and in 113-118 say: "These two presets show only that the rule cannot
   make him bound. That he is *not* bound needs Hobbes's other sentence, `r -> p & q`, and the
   preset *not-author* shows it does." In 270-271, replace "and the author is still not
   bound" with "so the rule alone does not bind the author".

3. **`part_a.py:392-412` and `475-482`: the ties figures are not on the page.** The prose says
   "The lab has two views" and gives 3/8, 5/16, 63/256 and 46189/262144 ≈ 17.62%. The worked
   example says its last two lines "belong to the ties view". The page has only the voices view
   (no `lasInSizes`), and a lesson takes one lab. The figures are correct (C(4,2)=6/16;
   C(6,3)=20/64; C(10,5)=252/1024; C(20,10)=184756/1048576). Either make the lab the ties view
   (sizes `2 4 6 10 20`) and move the voices cases into prose, or keep the voices lab and
   rewrite: line 392 "The lab works the voices."; line 403 "How often? The lab on this page
   does not compute it, but the count is short: if each member…"; the worked `after` "The last
   two lines are worked by hand…". Report the gap (PLAN asks for `voices` and `ties`).

4. **`part_a.py:651-652`, a misquote.** "the common Good differeth not from the Private". The
   image (PDF p. 215) reads "the Common good differeth not from the Private". Use that.

5. **`part_b.py:395-396`, a misquote.** "out of envy or interest". The image (PDF p. 228) reads
   "out of envy, or interest". Restore the comma.

6. **`part_b.py:122-124`, a wrong date.** "John Locke, writing the Two Treatises of Government
   after the revolution of 1688". The Treatises were mostly written around 1679–83, in the
   Exclusion Crisis, and published in 1689. Replace with: "John Locke, in the Two Treatises of
   Government, written in the Exclusion Crisis and published after the revolution of 1688,
   held…".

7. **`part_b.py:415-417` and label at `444`: a miscount.** The preset is called "Two voters
   change their order", and the prose says it "changes two of the nine rankings". The preset
   changes the group of 3 (`fleet army wall`→`fleet wall army`) and the group of 2
   (`army wall fleet`→`army fleet wall`), which is five voters. Two voters are enough: keep the
   group of 3 as `fleet army wall` and change only the group of 2 to `army fleet wall`. Fleet
   then beats wall 5–4 and army 7–2. Re-pin `voWinner`/`voCondorcet` "fleet". Alternatively,
   relabel the preset "Two groups, five voters, change their order".

8. **`part_b.py:355-357`, Aristotle's list garbled.** "Aristotle had made six kinds, three good
   and three bad; Hobbes keeps the three and dismisses the other three". Hobbes keeps monarchy,
   aristocracy *and democracy* (democracy is one of Aristotle's corrupt forms) and dismisses
   tyranny, oligarchy and *anarchy* (PDF p. 226). Replace with: "Aristotle had made six kinds,
   three right and three corrupt; Hobbes keeps three names, monarchy, aristocracy and democracy,
   and treats tyranny, oligarchy and anarchy as the same three misliked:".

## SHOULD-FIX

1. **`part_b.py:134-137`: Locke is not at strength, and one phrase is reversed.** "a trust that
   can be declared broken by those who hold it": the governors hold the trust, so this should
   be "by those who gave it". Give Locke's answer too: "Locke's reply was that the people shall
   be judge, and that where there is no judge on earth the appeal is to heaven: he accepted the
   risk Hobbes would not."
2. **Spans in quotation marks that are not Hobbes's words** (AUTHORING: every phrase inside
   `&ldquo;…&rdquo;` must be in the text). These are the letter glosses at `part_a.py:106-108`
   and `part_b.py:113-116`, "the crowd" at `part_a.py:352`, and "no wrong" at
   `part_b.py:277`. Use `<em>` for them. Lesson titles in quotation marks follow the subject's
   convention and can stay.
3. **Quotations closed with a period where the text runs on.** At `part_a.py:680` ("…every
   man with every man.") the text continues ", in such manner". At `part_b.py:156` ("…Civill
   Warre.") the text continues ";". Put the period outside the closing mark.
4. **`part_b.py:161-162`.** The comparison of miseries is "the premise on which the whole
   list rests". The list rests on the covenant of institution, and the comparison answers an
   objection to it (PDF p. 224). Write "the premise on which his answer to the objection rests".
5. **`part_a.py:640-642`.** "A multitude that all kept the laws of nature… would be all mankind
   doing the same" flattens a reductio. Write: "If a great multitude could keep the laws of
   nature without a common power, he says, we might as well suppose all mankind could, and then
   there would be no need of government at all, &ldquo;because there would be Peace without
   subjection&rdquo;".
6. **`part_b.py:310-312` (summary).** "the lab shows both on a stated profile of nine voters".
   The lab shows the cycle, and the attendance case (5–4 becoming 3–4) appears only in prose.
   Add a two-proposal preset (`monday` 5 v 4, `tuesday` 3 v 4) or reword to "the lab shows the
   second".
7. **`part_a.py:127-129`.** Children and the mad "become authors again when they recover the
   use of reason". The text (PDF p. 209) says something narrower: they are authors of the
   guardian's acts only when, recovering reason, "they shall judge the same reasonable". Say
   that.

## NOTE

- `part_b.py:419` says Milton was "of Hobbes's own generation". Milton was twenty years
  younger, so "of Hobbes's own time" is safer.
- Lesson 5's panel invites plurality and Borda. On `cycle` they give wall, and a fleet–wall tie;
  `voIIA` prints "violated (remove army)". One sentence on this would use what the page shows.
- Lesson 6's sixth worked line ("no children at all: his brother, then the nephew") is not a
  preset. It is easy to reach by setting the children dead, and the after-text could say so.
- `part_a.py:363-365` calls "the second half of the chapter" the next topic while this lesson
  is that half. Reword to "the rest of this half".
- Lesson 1's panel tells the reader to type `->`. The box displays `∧ →` and accepts both.
- Teaching is otherwise sound. Each lab is tied to the chapter's argument. Every lesson closes
  on what the computation cannot settle. Hobbes is given at strength, and his reasons on women
  are reported, not endorsed. The voice reads the passage, then goes through it, uses "you",
  and has no slang. I could not argue for any wrong quiz answer. Nothing is drawn from Tuck.

**Verdict:** a careful, well-taught course whose labs all compute what they say, held back by
one reversed obligation, one invalid inference read as Hobbes's conclusion, ties figures the
page does not print, two misquotes, a miscounted preset and two historical slips. Fix the eight
MUSTs, then ship.
