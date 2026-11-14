# Review (accuracy and teaching): Leviathan, Course 9 — The Kingdom of Darkness, and the Review and Conclusion

Course `leviathan-kingdom-of-darkness` (`content/leviathan/c9_kingdom_of_darkness/`), five
lessons, against PLAN §C/§D.1/§E/§F and AUTHORING. Reviewed 2026-11-14 on the operator's
copy (PDF pp. 513–588 read behind every claim checked; images for quotations). No Tuck
apparatus used; not the whole text file; not `site/`. I wrote only this file. Line
numbers are `part_a.py`.

## Gates

- **Preview:** `python3 scripts/preview_subject.py leviathan --course leviathan-kingdom-of-darkness --out …/scratchpad/rev/leviathan-kingdom-of-darkness`
  rendered 6 pages; labcheck 5 executed, 5 with pinned figures, 0 failing; **OK**.
- **`quotes.py`:** 116 quoted spans, all in the text; 107 OK, the rest OCR, italics or
  page breaks (pp. 537, 561, 578, 580 checked on the image: exact). Openings 68/75/90/75/79
  words.
- **Source comments.** PDF pages are right. The 1651 page for 1.3 is wrong (SF-1).
- **Browser (Playwright, chromium, `file://`).** All five lessons at 375 and 1280 px: no
  sideways scroll, no page or console errors. Every preset's tiles match the prose, the
  worked lines and my hand count (1.1 8/0/1/1 rows; 1.2 4-1-3, 3-3-2, 3-2-3; 1.3 2-1-2-3,
  2-0-3-3, 3-0-2-3; 1.4 6/9/2/0, 5/8/0/0, 1/1/2/0; 1.5 7 v 7, 8 v 7, −3 v −3/5, least 6
  and 30).
- **Typed in:** the 1.4 recodings in MF-1/SF-2 (results there).

## MUST-FIX

**MF-1. 1.4 counts one Presbyterian doctrine twice, and the `root` result depends on
it.** Lines 1266–1267 and 1300–1302 code `church-is-kingdom` to
`pope roman-clergy presbytery` and also `resurrection-kingdom` to `presbytery`.
Chapter 47 treats these as one doctrine. The doctrine "first taught by the Church of Rome"
was then "maintained also by the Presbytery". Those are Hobbes's marginal notes on PDF
p. 571. In the places where the Presbytery took the office, "this Doctrine, that the
Kingdome of Christ is already come, and that it began at the Resurrection … was still
retained" (p. 572). With the Presbytery on both rows, `root` names the Presbytery as most
served. That is an artifact of the coding, and the prose (1186–1191) and quiz item 3
(1365–1375) teach it as a finding.

*Replacement:* code `church-is-kingdom` as `pope roman-clergy` in `all` and `root`, and
leave `resurrection-kingdom` as `presbytery`. In the lab: `all` gives pope 6,
roman-clergy 9, presbytery 1 (most: roman-clergy, 9 of 14). `root` gives `pope and
roman-clergy and presbytery, 1 of 2 doctrines each (a tie)`.

- Prose 1183–1185: "Presbytery by 1". 1186–1191: "In <em>root</em> … Rome's form and the
  Presbytery's, and the three parties tie at 1 each, which is Hobbes's own verdict:
  &ldquo;the Romane, and the Presbyterian Clergy&rdquo;."
- Quiz 3: "What does the root preset report?" a: ["A three-way tie: pope, Roman clergy and
  Presbytery, 1 each", "The Presbytery, 2", "The Roman clergy, 2", "No party"], c 0. Why:
  "Rome's form of the doctrine serves the pope and the Roman clergy, and the form kept by
  the Presbytery serves the Presbytery. That makes one each, which is Hobbes's pairing of
  the two clergies."
- Quiz 2's why (1362–1363) and mistake 2 (1394–1395): change "2" to "1" in both.
- Re-pin `expect`.

**MF-2. 1.4 lines 1203–1204: "Hobbes also spares the sovereigns".** He blames them: they
"may neverthelesse bee esteemed accessaries", "I say they might have hindred the same",
"I blame those … [who] have holden the Stirrop to all the succeeding Popes" (p. 574).

*Replacement:* "Hobbes does not spare the sovereigns who let it happen either. They
suffered it &ldquo;for want of foresight&rdquo;, but &ldquo;may neverthelesse bee
esteemed accessaries to their own, and the Publique dammage&rdquo;, and once the people
were possessed there was &ldquo;no humane remedy&rdquo;." Check the new short quotation
with `quotes.py` (p. 574).

**MF-3. 1.2 lines 511–515 give scandal where Hobbes denies it.** Worship a king compels
to himself by terror is "no Worship; and therefore no Idolatry", and no scandal, "how
wise, or learned soever he be … it is not his act, but the act of his Soveraign"
(pp. 545–546). Scandal (p. 548) is a different case: a pastor or man of repute honouring
an *idol* for fear without making his fear evident.

*Replacement:* "…if a king compels a man by the terror of death to worship him, it is
&ldquo;no Worship; and therefore no Idolatry&rdquo;. The act is a sign of fear for
oneself and not of inward honour, and it gives no scandal, since it is the sovereign's act
and not his. Honour done to an idol for fear is not idolatry either. But a pastor, or a
man whose knowledge others follow, who does it without making his fear as plain as the
worship gives scandal, a sin of its own."

**MF-4. 1.1 quiz 2's why, lines 314–315: "The other three premises still stand".** With
c → s removed, two premises remain (k → c and ¬s). *Replacement:* "The two premises that
remain say nothing about when the kingdom comes."

## SHOULD-FIX

**SF-1. 1.3 source comment, line 716: "1651 p. 373".** On the image of PDF p. 561 the
marginal [373] stands beside "that by this doctrine of Separated Essences", below the
quotation. The opening is on 1651 p. 372. Write "1651 p. 372".

**SF-2. 1.4 canonization (lines 1275, 1291) breaks the lesson's own rule** (1179–1182:
serves both, goes to both). Hobbes: "they assure their Power" when men are declared
enemies "by the Popes excommunication … that is, (as they interpret it,) to the Pope"
(p. 573). Code `pope roman-clergy`. Typed in: `held` pope 6, roman-clergy 8; `all` pope 7,
roman-clergy 9. Update worked lines 1336–1345 ("…: 6"; "fourteen entries") and re-pin,
or justify clergy-only in the coding paragraph.

**SF-3. 1.4 lines 1244–1246: "both have no existence but in the fancies of the
ignorant".** Hobbes says that of the fairies only. Of the pope he says that his spiritual
power outside his own dominion "consisteth onely in the Fear that Seduced people stand
in, of their Excommunication" (p. 578). *Replacement:* "He means it as an argument: as
the fairies have no existence but in the fancies of ignorant people, so the pope's
spiritual power outside his own dominion &ldquo;consisteth onely…&rdquo;" Keep the
existing quotation.

**SF-4. 1.5 line 1564: "the conqueror's heirs".** p. 582 speaks of sovereigns who rest
their right on the war "and not on the Possession", and of conquerors requiring "an
Approbation of all their actions past". *Replacement:* "Sovereignties weaken, he says,
when their holders rest their right on the justice of the war that won it rather than on
possession, or require approval of all they did."

**SF-5. 1.1 lines 216–218: "and he leaves his own readings to the better scholars".**
This is attached to eternal torment (p. 527). The deference, "I may propound such things
to the consideration of more learned Divines", is about the sin against the Holy Ghost
(p. 531). Move the clause to the end of the Holy Ghost sentence, or cut it.

**SF-6. 1.5 `failed` preset prints a state the prose does not mention.** With protection
gone, the tiles still read `lcvCondition` "a common power" and `lcvFirst` "−4, since
subject breaks". That is a sovereign who pays 4 to protect and protects nothing. Add one
sentence after line 1530: "The sovereign's tiles still show him paying 4 for protection
that is worth nothing to the subject: that is the lab's way of saying the first
performance has failed, and why the subject's obligation is in question."

## NOTE

- **1.4 coding, otherwise sound.** All twelve doctrines (pp. 572–573) checked; apart from
  SF-2 each party follows Hobbes's sentence (pope: 1, 2, 4, 6; both: 3; clergy: 5, 7, 9–12).
  The knots (p. 575) are right. "Doctrines, that serve them" (p. 572) grammatically covers
  both clergies; mistake 2's reading is fair.
- **1.2 lab.** A phantasm is defined without `dimension`, so on the `hobbes` preset "a
  demon is a body" is false. For Hobbes a phantasm is motion in the organs (p. 536), so
  the simplification is the lesson's. The panel says the definitions are its rendering,
  which is enough. A clause in the prose would help.
- **1.3 line 845:** "The soul is body" should read "A soul is a body". Mistake 1 (1047),
  "three claims in each", means three insignificant claims; say so.
- **Teaching and voice.** Every lab computes the chapter's argument; no other wrong quiz
  answer is arguable; each lesson closes on the gap; critics at strength (Bellarmine,
  Beza, the Aristotelians, cui bono turned on Hobbes). Voice meets §F; Parts III–IV are
  neither mocked nor preached.

**Verdict:** Accurate and well taught overall. Fix the double-counted Presbytery in 1.4
(MF-1), the two misstatements of Hobbes (MF-2, MF-3) and quiz 1.1's why (MF-4) before
release.
