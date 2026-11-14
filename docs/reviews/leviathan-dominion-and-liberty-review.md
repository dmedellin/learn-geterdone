# Review: Leviathan, Course 6 — Dominion, Liberty and the Parts of a Commonwealth

`content/leviathan/c6_dominion_and_liberty/`, four lessons, reviewed 2026-11-14 to
`docs/leviathan/REVIEW.md`. Read: PDF pp. 233–266 (chs. 20–23) and pp. 210–211 (ch. 16).
Line numbers are `part_a.py`. I wrote only this file.

## Gates

- **Preview:** `preview_subject.py leviathan --course leviathan-dominion-and-liberty` printed
  5 pages; labcheck 4 executed, 4 with pinned figures, 0 failing; **OK**.
- **Quotations:** 91 `&ldquo;…&rdquo;` spans across the four lessons, all through `quotes.py`.
  83 OK; 3 MISS, 4 NEAR and 1 LOOSE are line breaks or OCR faults (`Common-|wealth`, a page
  break, `4 FREE-MAN`, `/iberty`, marginal run-ins), each checked on the page: exact.
  Openings: L1 p. 237 (48 words), L2 p. 241 (31), L3 p. 247 (50), L4 p. 253 (63); source
  comments right.
- **Browser:** four lessons and course page at 375 and 1280 px: no sideways scroll, no
  errors. Every preset's tiles match prose, worked lines and quizzes, recomputed by hand: covenant 80/100/−5/20, 80/50/55/40,
  80/90/−5/200; law 6 of 8 = 75%, 5/8 = 62.5%, 6 of 8 (many-wives free); 4 commanded,
  2 refusable, 1/5 = 20%; 2 commanded, 0 refusable, 3/5 = 60%; assembly 4–2 passes (4 liable,
  2 excused), 3–3 mute, 3–2 passes (3 liable, 4 excused), absolute 3 of 7 fails.

## MUST-FIX

1. **The Chapter 22 debt rule is made conditional on "beyond the letters"; Hobbes's is not.**
   Lines 936, 983, 1127, 1139, 1157, 1177, 1185, 1225. Hobbes has two rules. (a) An *unwarranted*
   decree is the act only of those who voted for it (p. 253). (b) A *debt to a stranger* is
   owed by the one-man representative, or the assembly's yes-voters, for any borrowing, because "no Letters need limit borrowing, seeing it is left
   to mens own inclinations to limit lending", and letters that let him make the members pay
   would make him sovereign; the lender, "a stranger to the Letters", takes as debtors only
   those who engaged themselves (p. 253). The lesson ties (b) to (a) throughout, and the
   L4 quiz 3 `why` (line 1185) gives rule (a)'s reason ("representeth no mans person, but his
   own", p. 252) for rule (b). Replacements:
   - 936: "…beyond them is the act of those who voted for it. A debt to a stranger is owed only by those who voted for the borrowing, whatever the letters say, since no letters could make the members pay without making the representative sovereign."
   - 983: "If he borrows from a stranger, he alone owes the debt (no letters need limit borrowing, Hobbes says, and letters that let him make the members pay would make him their sovereign), out of the common stock…"
   - 1127: "If the motion passes, those who voted for it are answerable: for a debt to a stranger always, and for any other decree when it is beyond the letters."
   - 1139: replace the last sentence with "The lender is a stranger to the body."
   - 1157, 1177: delete "beyond its/his letters".
   - 1185: replace the second sentence with "The lender, &ldquo;being a stranger to the Letters&rdquo;, takes for his debtor only the man who engaged himself."
   - 1225: "It cannot tell you whether a decree other than a debt is beyond the body's letters…"
2. **The merchants' exception is stated but not marked as an exception, and it makes L4 quiz 1's
   option A defensible.** Lines 1033–1034, 1156–1158. For a body politic of merchants Hobbes
   says "every Member is lyable by himself for the whole" of a debt to a stranger (p. 257),
   not only the yes-voters. Line 1033 states this but reads as the general rule, and the quiz
   stem "A subordinate assembly…" fits a merchant company. Replace 1033's last clause with
   "…every member should sit in the assembly; and here Hobbes departs from the general rule:
   a debt to a stranger falls on every member for the whole, because a stranger takes no
   notice of their private laws." Change the quiz stem to "A town's governing assembly
   votes four to two, with none absent, to borrow from a stranger."
3. **The "Soule of the Common-wealth" sentence does not end Chapter 21 and does not link
   back to Chapter 17.** Line 754. It sits mid-paragraph on p. 249, between "can by no Covenant be
   relinquished" and "The end of Obedience is Protection". The chapter ends on the captive monarch whose subjects obey "the Magistrates formerly placed"
   (p. 250). The soul image comes from the Introduction ("an Artificiall Soul", p. 105).
   Replace with "The section rests on an image from the Introduction, where sovereignty was the
   artificial soul:" and move the paragraph into the obligation paragraph (line 731 on).
4. **Bramhall was not a bishop of the Church of England.** Line 406. He was Bishop of Derry,
   in the Church of Ireland, in exile at the time. Replace "a bishop of the Church of England"
   with "the exiled Bishop of Derry".
5. **L4 quiz 2 ("mute"): option C can be argued from Chapter 16, and the body says more than
   ch. 16 does.** Lines 1005, 1171–1176. Hobbes says an even assembly is "oftentimes mute"
   (p. 210), and that in some questions equal voices *do* decide: "not to condemne, is to
   absolve", and "the not decreeing Execution, is a decree of Dilation" (p. 211). On that rule a
   tie on a motion to borrow now leaves the money unborrowed, so "Fails" can be defended. The
   kit's own status line for `even-split` says "The motion is lost: the assembly is mute".
   Replace option C with "Fails, because the three no voters outnumber the yes voters", and the
   `why` with "Neither side has the greater number, and the lab calls such an assembly mute, as
   Chapter 16 does; Hobbes adds that in some questions an even vote still decides (not to
   condemn is to absolve). Either way nothing is decreed and no one is liable." At 1005 replace "as in Chapter 16" with "as Chapter 16 says an even assembly
   oftentimes is".

## SHOULD-FIX

1. **The worked example's last sentence misstates the soldier.** Lines 820–821 read as if Hobbes were
   silent on volunteers; the enrolled man is obliged "not to run from it, without his Captaines
   leave" (p. 248). Replace: "The lab does not mark the muster law, because on Hobbes's
   account a pressed man may sometimes refuse (with a sufficient substitute) and an enrolled
   man may not, and which case holds is a judgement the lab does not make."
2. **The two grounds of the true liberties are run together.** Lines 652–653 put confession
   under the body's defence and attach "justly condemned" to it; Hobbes gives it its own ground
   (no one "can be obliged by Covenant to accuse himselfe", p. 247), and the concept drops "not
   to resist those that assault him". Replace: "Covenants not to
   defend one's own body are void, so a subject, even justly condemned, may refuse an order to
   kill or wound himself, not to resist those who assault him, or to go without food, air or
   medicine; and since no one can be obliged to accuse himself, he need not confess his own
   crime without assurance of pardon."
3. **Two mistake titles contradict each other.** Line 870 ("Thinking Hobbes's sovereign has
   no limits at all on him") and 875 ("Thinking a subject's liberties are limits on the
   sovereign's right"). Retitle 870 "Thinking a subject must obey every command".
4. **"Eight actions, taken from Hobbes's examples"** (428, 614): paying tax is not among
   Chapter 21's examples (paying a debt for fear of prison is). Say "seven from Hobbes's
   examples and paying tax".
5. **Ch. 23's bodily comparisons are overstated** (1062): only general administration (nerves
   and tendons), teaching and judging (organs of voice) and execution (hands) are compared;
   treasure and militia are not. Replace "each compared to a part of the body" with "most of
   them compared to a part of the body".
6. **Filmer** (99–101): "You can hear who he has in mind" names a target the chapter does not,
   and *Patriarcha* was unpublished in 1651. Replace with "The view he rejects was held by
   patriarchal royalists, Sir Robert Filmer the best known."

## NOTE

1. Line 1009–1011 calls the abstention rule "its extension". The text supports more of it than
   that: "they that gave not their Vote, are therefore Innocent" (p. 253) and "onely they …
   that gave their votes to the borrowing" cover abstainers. Only the counting of a pass among
   abstentions is the lab's own.
2. `ordinary-laws` shows kill-self and confess-own-crime as free (3/5 = 60%); the body
   should say so in a sentence.
3. Line 1073–1075 says "the next course" twice running.
4. Thirteen of sixteen quiz answers sit at index 2 or 3.
5. Voice is good: passage first, history with people (Locke, Bramhall, Harrington, 1651),
   Hobbes and critics at strength. Each lesson closes on the material
   clause's gap, and every lab carries the chapter's argument.

**Verdict:** accurate on Chapters 20 and 21 apart from two slips, and the labs are exact; fix the
Chapter 22 debt rule (MUST 1–2) before release.
