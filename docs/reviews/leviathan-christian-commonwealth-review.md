# Review (accuracy and teaching): Leviathan, Course 8 — Of a Christian Commonwealth

Course `leviathan-christian-commonwealth` (`content/leviathan/c8_christian_commonwealth/`), eight lessons, reviewed 2026-11-14 against the private OCR and page images of the operator's copy, following `docs/leviathan/REVIEW.md`. I read the pages behind each claim with `book.py`/`page.py`, did not read the text file whole, did not read `site/` or Tuck's apparatus, and wrote only this file.

## Gates

- **Preview:** `preview_subject.py leviathan --course leviathan-christian-commonwealth` → 9 pages; labcheck 8 executed, 8 with pinned figures, 0 failing; **OK** (run twice, before and after a container restart).
- **Quotations:** 118 `&ldquo;…&rdquo;` spans: 9 are lesson titles, one is not a quotation (MF-9), and the other 108 pass `quotes.py` or were checked on the image. All are under 120 words; the longest is ch. 40's at 94 words.
  - **Opening quotations of lessons 3 and 8 (not checked by the author):** checked on the image. L3 (PDF p. 366, 1651 p. [208]) is exact, with italics dropped. L8 (PDF p. 499, 1651 p. [322]) is exact; "NECESSARY" is small capitals in print, and all capitals is an acceptable rendering. Neither lesson's dict comment gives the 1651 page (SF-2).
  - Other openings on the image: L2 (p. 357), L5 (p. 399, "Creation,)" with its comma, as printed) and L4 (p. 378) are exact. **L7 (p. 420) is not exact** (MF-1).
- **Browser (Playwright, chromium, `file://`).** I loaded all 8 lessons at 375 px and 1280 px. scrollWidth equals clientWidth on every page, and there are no page or console errors. Every preset's tiles match the prose and worked lines, recomputed by hand (e.g. L4 1/41, 1/5, 1/361, 0; L5 9/500, 729/36500, 81/5531; L6 5/5, 2/5, 4/5 with C & W the one pair that fits), and the counterexample rows printed are the ones the prose describes.
- **Dates and people** (Bramhall 1658, Clarendon 1676, *Lex, Rex* 1644, Melville, Hume, Paris 1640): right.

## MUST-FIX

1. **part_b.py:701 — misquotation in L7's opening.** The page (PDF p. 420) prints "by the mediation of Moses **himself**: And our Saviour". The lesson has "himselfe". Replace with `himself:`.
2. **part_a.py:573–576 (L2 worked, `after`) misstates Hobbes.** It says the burial "tells nothing, which is why Hobbes needs the Canaanite". On p. 357 Hobbes says the opposite: from the sepulchre verse "It is therefore manifest, that those words were written after his interrement", and he brings Genesis 12.6 (p. 358) only against the reply that the last chapter alone is later. With the burial dated at year 0, the lab contradicts the lesson's own opening quotation. Replace with: "The burial, dated at year 0, does not trip the lab's test, because the lab only compares years. Hobbes's point is sharper: no writer reports his own burial and adds 'to this day', so that verse alone shows a later hand. He brings the Canaanite only to answer the reply that the last chapter alone is later."
3. **part_a.py:126 — "in the same book".** The Egyptian sorcerers are in Exodus, not Deuteronomy. Hobbes adduces them while commenting on Deut. 13 (p. 354). Replace "is in the same book" with "comes in the same place".
4. **part_a.py:319–321 (L1 mistake 1) names the wrong presets.** The first two presets are `both` (valid) and `miracle-alone` (doctrine unexamined, invalid). Replace with: "In the both and sorcerers presets the same rule and the same miracle give opposite conclusions, depending only on the doctrine."
5. **L4 calls 1 in 401 "Hobbes's count"** (part_a.py:971, 976, 982, 1096–1097, 1159, 1170–1171, 1268–1271, 1280–1281). Ch. 32 (p. 353) says "Of 400 Prophets … only Micaiah was a true one", which is 1 in 400, and lesson 1 follows it (line 57). Ch. 36 (p. 394) says "four hundred … all false Imposters, but onely one Michaiah", which leaves the total open. 401 is the lesson's reading of 1 Kings 22. Keep the figures; at 1096 write "Reading 1 Kings 22 as four hundred prophets and Micaiah besides, 401 in all, one is true (Chapter 32 counts Micaiah among the four hundred, 1 in 400; the result barely moves)", and elsewhere say "the lesson's count from the story", not "Hobbes's count".
6. **part_a.py:669 — miscount.** The preset holds nine claims, as the body says at line 799. Replace "Reckon eight claims … which are true, false or absurd" with "Reckon nine claims … which are true, false, absurd or insignificant".
7. **part_b.py:416–418 — "dispute of the sword" misstated.** On p. 407 Hobbes says he only propounds the doctrine of a kingdom of God on earth, "attending the end of that dispute of the sword, concerning the Authority … by which all sorts of doctrine are to bee approved". Replace with: "He says he only propounds this, maintaining nothing, while he waits for &ldquo;that dispute of the sword&rdquo; to decide which authority approves doctrine; and he submits it &ldquo;to the interpretation …&rdquo;".
8. **part_b.py:1067–1068 — Bellarmine's books.** On pp. 474–477 the first book contains three questions, the third being whether Peter was monarch of the church. "The second Book hath two Conclusions": that Peter was bishop of Rome and died there, and that the popes are his successors. Replace with: "answering the first, on the best form of government and Peter as monarch of the church, the second, on Peter as bishop of Rome and the popes as his successors, and the others in turn."
9. **part_a.py:804–805 — a quotation that is not in the text.** `&ldquo;inspiration is infusion&rdquo;` is the lab's claim, not Hobbes's words. Use `'inspiration-is-infusion'` (the claim id) or &lsquo;…&rsquo;.
10. **L6 case 2 contradicts the chapter** (part_b.py:491, 501, 511; body 473–480; worked 552; quiz 1; mistake 1). Hobbes's definition is normative ("at whose command they *ought* to assemble"). On p. 417 he goes straight on: "that Church also, which is assembled in any Common-wealth, that hath forbidden them to assemble, is an unlawful Assembly". So the verdict "not a church" for a forbidden congregation is not the text's, and the lesson's lead example of "too broad" rests on it. Replace the case with the one p. 417 does exclude: `_case("a crowd of Christians acting with no authority from a lawful congregation", [1, 1, 0], 0)`, with W read as "acts by the sovereign's authority". Update the body, worked line 552, quiz 1 and mistake 1 to match, and add: "A congregation that meets against the sovereign's prohibition Hobbes still calls a church, but an unlawful assembly."

## SHOULD-FIX

1. **Opening capitals differ from print:** part_b.py:77 "If" (printed "if"), part_b.py:107 "All" ("all"), part_a.py:740 "The" ("the"), part_b.py:714 "the" ("The").
2. **Missing 1651 pages:** part_a.py:658 should read `1651 p. 208`; part_b.py:952 should read `1651 p. 322`.
3. **part_a.py:246:** write "Drop the third premise and ask for A instead of not-A".
4. **part_a.py:338–341:** if the marks are necessary only, only `both` loses its valid result; `sorcerers` and `ceased` stay valid. Say so.
5. **part_a.py:828, 836:** rename `an-angel-of-flesh-thin-body-is-a-spirit` to `an-angel-of-subtle-body-is-a-spirit`, which is what line 802 says.
6. **part_a.py:944–946:** for Hobbes, absurd speech *is* insignificant (ch. 5). Write: "the lab's three verdicts are the kit's; for Hobbes absurd and insignificant speech are one failure, and both differ from a false one."
7. **part_a.py:1266–1267:** the common sort give reputation for "one casuall event" (p. 387), which is overweighting a hit, not taking a likelihood for a probability. Write "to weigh one hit above many misses".
8. **part_b.py:129:** in `confederates` the miracle loses ground to the trick (from 1:49 to 0.729:49), so "gains nothing at all" understates it. Write "loses ground".
9. **part_b.py:494/504/514:** "Christians under an infidel sovereign" [1,1,0] repeats case 2 and tests nothing. Separate it with its own letter, or drop it.
10. **part_b.py:550–555:** the worked lines omit case 5, so "2 of 5" is not shown.
11. **part_b.py:469–472:** the next-course sentence is garbled. Keep only the next-lesson sentence.
12. **part_b.py:805:** in `signs`, M replaces H; it is not "added to the list".
13. **part_b.py:1181–1186:** `covenanter` has no F premise, so its row is equally a man who never had the faith. "Lost the faith by it" is a gloss the lab cannot show.

## NOTE

- part_b.py:1060: on p. 440 a martyr properly is one who saw Christ risen; one sent to preach without having seen is a "second" martyr. "Or was sent to preach it" blurs that distinction.
- part_a.py:1046: "too much light" (p. 380) explains why the interpretation is little noticed. The mistranslations follow as a separate observation.
- part_a.py:1090: Hobbes says "a little before the time of the Captivity" (p. 394).
- part_b.py:143–146: for fairness, add that Hobbes goes on, "If he say 'tis done, then he is not to contradict it" (p. 401). In a Catholic commonwealth the lieutenant's answer settles it.
- **Teaching and voice.** Every lab computes something the chapter argues, and every note closes on what it cannot settle. Critics are given at strength (More, Rome, Presbyterians, Rutherford, Covenanters, Hume), and Part III is fair, neither mocked nor preached. I could not argue for any wrong quiz answer. The voice is right.

**Verdict:** ships after the ten MUST-FIXes. One is a misquotation (MF-1); the others are claims the text does not make, most importantly the burial argument (MF-2), Hobbes's "count" of 401 (MF-5) and the forbidden congregation (MF-10). The labs, arithmetic and layout are sound.
