# Review (accuracy and teaching): Leviathan, Course 3 — Power, Manners and Religion

Course: `leviathan-power-manners-religion` (`content/leviathan/c3_power_and_religion/`,
`__init__.py`, `part_a.py`), five lessons. Built to `docs/leviathan/PLAN.md` §C Course 3,
§D, §E, §F and `docs/leviathan/AUTHORING.md`. Reviewed 2026-11-14 against the private
OCR of the operator's copy. I read PDF pp. 158–181 (Chapters 10–12 whole) with
`page.py` and checked the page images where the OCR was in doubt. I did not read
`site/` or the text file whole, and I used nothing from Tuck. I wrote only this file.

## Gates

- **Preview:** `preview_subject.py leviathan --course leviathan-power-manners-religion`
  rendered 6 pages; labcheck 5 executed, 5 with pinned figures, 0 failing; **OK**.
- **`quotes.py`:** I extracted all 120 `&ldquo;…&rdquo;` spans and checked each against
  pp. 158–182. 106 are OK. Four are LOOSE or NEAR because of OCR errors, and I checked
  each on the image: "Power ofa" (p. 158), "t¢ HONOUR" (p. 160), "Agent /nvisible"
  (p. 172) and "WorTHINESSE" (p. 165). All four are exact as printed. The dignity
  opening (51 words, pp. 159–160) MISSes only because the OCR reads "DiGnity", and it
  is exact. The other 9 spans are not Hobbes's text: see MF-1 and MF-2. Every
  quotation is under 120 words. The page comments are right: [41]/[42] on pp. 158–159,
  [47] on p. 165, [48] on p. 166, [54]/[55] on pp. 174–175, and [58] for the p. 180
  passage.
- **Browser (Playwright, chromium, `file://`):** I loaded all five lessons at 375 px and
  at 1280 px. scrollWidth equals clientWidth at both widths, and there are no page or
  console errors. Every preset's tiles match the prose and my own arithmetic, and
  when I typed "follows ×3" into lesson 4's lab it gave 81/206, as I computed.

## MUST-FIX

1. **The author's own wording inside Hobbes's quotation marks.** At part_a.py:1284–1286,
   `c`, `g` and `d` are glossed in `&ldquo;…&rdquo;`: "the founder or his priests enjoin
   belief of contradictories", "his ignorance is detected" and "he is discredited in
   all else he proposes as revelation". None of these is in the text; Hobbes's words
   are on p. 180. Step 2 at :1357 does the same with `&ldquo;if&rdquo;`. Replacement:
   "Let `c` stand for: the founder enjoins belief of contradictories; `g`: his
   ignorance is detected; `d`: he is discredited in all else he propounds as
   revelation." At :1357, write: "…become *if* links in a chain."
2. **Lesson and course titles in `&ldquo;…&rdquo;`.** This happens at :142, :443, :760,
   :878, :1027 and :1324. The brief puts only Hobbes's text inside these marks.
   Capital writes titles with literal “…”. Use that form or `<em>…</em>`.
3. **Dignity is a kind of worth (part_a.py:369–370).** The lesson says Hobbes "puts
   dignity in the list next to worth and not as one of its kinds". But Hobbes defines
   dignity as "The publique worth of a man" (p. 159), and the lesson's own concept
   says the same. Replacement: "That is why Hobbes calls dignity a man's *public*
   worth: a worth, but one set by a single buyer whose valuation binds everyone."
4. **"not alwayes" is dropped (:633, :637, :661).** Hobbes says the cause "is not
   alwayes" a hope of more delight or an inability to be content (p. 166). The
   one_line ("not out of greed"), the summary ("is not that men cannot be content")
   and the concept ("The cause is not that…") turn this into a flat denial. The
   lesson's own mistake 1 and Chapter 13's glory-seekers depend on "not always".
   Replacements: one_line "…power after power, not always out of greed, but because
   he cannot be sure of what he has without more." Summary "Its cause, he says, is
   not always that men cannot be content…". Concept "The cause is not always that…".
5. **The one-greedy table is not "as in the first table" (:722–723).** In the greedy
   preset the column player's payoffs are HH 3, HA 4, AH 0, AA 1. In one-greedy they
   are 2, 4, 1, 3, and this column player prefers (Add, Add) to (Hold, Hold). That is
   why the lab prints "every equilibrium is efficient", unlike the greedy preset.
   Either delete ", as in the first table", or set the payoffs to
   `[[[3, 3], [0, 4]], [[2, 0], [1, 1]]]`. By hand, (Add, Add) is still the only
   equilibrium, and `gaPareto` becomes "(Add, Add) is dominated by (Hold, Hold)".
6. **Phormio and Scipio belong to the wrong seed (:975–997).** In Hobbes, "from the
   like things past, they expect the like things to come… As the Athenians… another
   Phormio" belongs to the *second* seed. It is about "the way by which they think
   these Invisible Agents wrought their effects", that is, ignorance of second causes
   (p. 174, above "Thirdly"). The lesson attaches it to the fourth seed, prognostics,
   and quotes it as illustrating that seed. Also, "The last is the one the lab takes
   up" (:980–981) refers back to worship, which is the third seed. Replacement: move
   the Phormio/Scipio sentence and the "expect the like things" quotation into the
   second-seed clause at :977–978. At :980–981 write: "The fourth is the one the lab
   takes up." Then start :990 with "That is an observation about evidence…" and go
   straight to "Men use the past to guess the future…".
7. **"Which premise does the work" has no answer in the lab, and the lesson
   contradicts itself (:1291–1305, :1361–1363, :1378–1382, :1451–1453).** Dropping
   *either* premise opens a counterexample. I typed `g -> d` alone and got Invalid, 1
   (c=T, g=F, d=F). So step 4's test ("the one whose removal opens a counterexample")
   and the `standard` ("name the premise whose removal makes it invalid") pick out
   both premises, not one. The body also says the second premise is what "its
   opponents deny". Yet its example defender "could grant the chain and deny that it
   applies", which means denying that `c` holds, as quiz 4's `why` also says.
   Replacement for :1299–1305: "Both links are needed: drop either and a
   counterexample opens. The defender of a mystery attacks neither. A Catholic or
   Anglican defender of the Trinity grants the chain and denies `c`, because the
   doctrine is above reason, not against it. Hobbes's own sentence grants that
   line…". Step 4: "Delete each in
   turn: each deletion opens a counterexample, so the argument needs both. Then ask
   which an opponent denies, a premise or the claim that `c` is true of his
   doctrine." Standard: "…say whether it is valid, show that it needs both premises,
   and say where a defender of a mystery resists it." Worked `after`: "…is what rules
   it out; the defender of a mystery need not deny it, only that his doctrine is a
   contradiction."
8. **"he spends most of the chapter on it" (:282–284).** Most of Chapter 10 (pp.
   160–164) is on honour and titles, not on instrumental power. Popularity, good
   success and affability are listed as powers but are not labelled instrumental.
   Replacement: "Hobbes's list of what counts as power runs well past strength and
   skill: riches (with liberality), reputation, friends, popularity, good success,
   affability."

## SHOULD-FIX

1. **:94–95.** The greatest human power is a commonwealth "Or… the Power of a Faction,
   or of divers factions leagued" (p. 158). Add ", or a faction", which also fits the
   lab's third buyer.
2. **:393.** The text has piracy as "a lawfull Trade, not onely amongst the Greeks, but
   also amongst all other Nations" before great commonwealths (p. 163). Replace "the
   piracy of the early Greeks" with "piracy, a lawful trade among the Greeks and other
   nations before great commonwealths".
3. **:414–415.** "so is the judge's [above every buyer's price], though it equals…"
   contradicts itself. Replace with "the judge's is above two and equal to the third,
   the peace buyer's 34".
4. **:136–138, :436–442 (critic at strength, PLAN §F).** Lesson 1 promises that the
   next lesson "meets its best form" of Kant's objection. Lesson 2 instead calls it a
   clash of words. Kant objects to *worth* as price: pricing a person treats as
   replaceable what has no equivalent. State that, then give Hobbes's real reply,
   that he describes how men value one another, not how they ought to.
5. **Quiz 1.4 `why` (:270–273).** It implies the merchant may be lowest for the faction.
   He is lowest for no buyer (24 against 16 and 17). Replace with "The merchant is never
   lowest (the orator is for war, the general for peace and the faction)".
6. **:58–60 against the docstring at :5–6.** The docstring says small capitals are
   printed as capitals, and WORTH, DIGNITY, HONOUR and WORTHINESSE are. But the opening
   gives "Power", and p. 158 prints "POWER" in small capitals. Write "POWER".
7. **`__init__.py`:79–80.** "Chapter 10 ends with a long digression on coats of arms and
   titles" is wrong: the chapter ends with worthiness (p. 165). Write "Chapter 10 closes,
   just before worthiness, with a long digression…".
8. **:736.** "Military men" should read "Needy and hardy men, and all who are ambitious
   of military command" (p. 167).

## NOTE

1. **:95–97.** Hobbes left England in late 1640 and saw the war from Paris.
   **:68–69.** "before any commonwealth exists" reads more into "Universally" than
   the text does.
2. **:406–409.** "That is dignity" follows a sentence about *civil honour*, and Hobbes
   keeps the two apart (p. 161: civil honours are magistracy, offices and titles). This
   is defensible but could be one clause more careful.
3. **:1258.** "and the lesson should say so" is the lesson talking about itself. Cut it.
4. Every figure in the body, worked lines, quizzes and mistakes checks by hand. The
   right quiz answers are in varied positions. Part III material (Numa, Mahomet,
   Bramhall) is fair, and each note closes on what the lab cannot settle.

**Verdict:** the labs are sound and every figure checks, but the course should not
ship until the eight MUST-FIXes are made. The most serious are the author's glosses
inside Hobbes's quotation marks, the misplaced Phormio example, the dropped "not
alwayes", and the premise test in lesson 5 that singles out no premise.
