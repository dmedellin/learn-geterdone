# Review: wealth-mercantile-system (Book IV, Chapters 1–6)

Files: `content/wealth_of_nations/c10_mercantile/part_a.py`, `part_b.py`. No spoken forms were needed.

## Gates

- Before: `preview_subject.py --course wealth-mercantile-system` printed OK (6 pages, 6 pinned, 0 failing). `quotes.py` had no MISS.
- After: OK (6 pages, 6 pinned, 0 failing). `quotes.py` has no MISS.

## Fixes

**Lab defect (lesson 6, `treaties-of-commerce`).** The home cost was set to £900 a tun so the lab would always buy abroad, and the panel told the reader to ignore the "make at home" tiles (£880,000, £878,000, £871,000). I set it to £600, thirty times the French £20. That is Smith's ratio for Scottish hot-wall wine (IV.2, l. 14558–14560). Every tile now has a meaning, and a new body paragraph names each one. The prohibition tile reads £580,000 / £578,000 / £571,000, and the paragraph sets it beside the £9,000 cost of the preference, using Smith's line that a preference "can scarce amount to any positive loss, but only to a lessening of the gain" (l. 17484–17486). Buyers-pay-more equals the duty. The £0 loss tile in `portuguese-dearer` is explained: the favoured merchants' extra £7 sits inside the foreign price, where the tile cannot see it. I checked all 18 tiles by hand, re-pinned them from `--observe`, and updated the panel intro, the worked example and the note to match.

**Accuracy about others.**
- Lesson 2 (invisible hand):
  - Arrow and Debreu now read "among others" (the 1950s welfare theorems were not theirs alone).
  - Greenwald and Stiglitz (1986): changed "the hand is generally not there" to what the paper shows, that the competitive outcome can generally be improved on.
  - Viner (1927): now cites the essay on Smith and laissez-faire, with his contrast between a beneficent natural order and the Wealth of Nations' many exceptions.
  - Rothschild: now cites *Economic Sentiments* (2001), "lightly, perhaps ironically". I cut the claim that eighteenth-century readers rarely mentioned the phrase, because I am not sure of it.
  - The astronomy essay: now says only "published after his death". It is no longer a quotation, since the phrase is not in the PSU text.
- Lesson 4, Hamilton's 1791 Report: it was called "the opposite direction" to Smith on drawbacks, which was wrong (both approve drawbacks). It now says Hamilton listed drawbacks on materials and bounties, and argued that bounties had advantages over protecting duties.
- Lesson 5, Sen (1981): "famines occur in years when the food supply is not unusually short" is now "can occur". Thompson (1971), Ricardo and Malthus (1815), Hamilton on bounties, and Olson are correct as written.
- Lesson 6: List (1841) on the Methuen treaty, Viner (1950) on trade creation and diversion, and Ricardo's 1817 figures are correct. No change.

**Accuracy against the text.**
- L2, Navigation Act: "Smith says its purpose was to weaken the Dutch" overstated him. He says some rules "may have proceeded from national animosity", and that the animosity aimed at what wisdom would recommend (l. 14736–14744). It now says that, and gives his defence reason (l. 14703).
- L2: "a hard climate" changed to "a bad climate" (l. 14820).
- L2, tax presets: the lab takes the taxed £12 as the home cost. So the prohibition tile (£1,000) is the cost to buyers, not to the country, and the £1,000 "loss" in `tax-equal-duty` is home tax the treasury does collect. The garbled sentence is rewritten to say so (l. 14769–14779).
- L3: "Smith's longest description of a single bank" was unsupported, and is softened.
- L3: "countries that pay in bank money show an exchange in their favour" is corrected to Smith's claim that the *computed* exchange may favour them while the real one does not (l. 15234–15238).
- L3: "He doubts how much treasure the bank held" becomes "a matter of conjecture" (l. 15557).
- L3: "Smith doubts whether it kept its word" becomes "allows that this may seem uncertain, then gives the burgomasters' oaths" (l. 15531–15542).
- L5: "rather than the country gentlemen… most anxious" was a gloss. It is now his "greatest zeal" (l. 16458).
- L5: the herring bounty is now described by its tonnage basis (l. 16614–16617).
- L5: the Tracts' ratios are restated: one in thirty-one of the produce, and 570 to one and thirty to one (l. 17169–17177).
- L5: the "author he places little faith in" mistake is fixed. Smith calls him "very well informed" (l. 16242). It is his computations Smith does not warrant (l. 17178).
- L5: the statute of 13 George III phrasing is fixed.
- L6, fairness: added Smith's concession that easing the round-about trades is "the principal advantage of the Portugal trade… a considerable one" (l. 17631–17633).

## Checked and left

I checked every other figure in all six lessons against the text and found them right. That includes £90M, two-thirds, £18M and £30M, £6M against £19M, a third of the plate, 1692/1696 and 75 per cent, the 600-guilder bills, the 4–5 per cent agio, 2,000 accounts × £1,500 at 11 guilders, 96,000 and 14,000 hogsheads, 5s and 4s and 31 giving £6 4s, Barretti's £50,000 a week, and the seignorage cases. Quiz answers are spread across positions. Every lesson closes on what its arithmetic cannot settle.

## Left undone

Nothing.
