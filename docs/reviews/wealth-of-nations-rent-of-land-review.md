# Review: wealth-rent-of-land (Course 6, The Rent of Land)

Files: `content/wealth_of_nations/c06_rent/{__init__,part_a,part_b}.py`. No spoken
forms were needed.

## Gates

- Before: `preview_subject.py --course wealth-rent-of-land` printed OK (6 pages, 6
  pinned). `quotes.py`: no MISS (2 SHORT one-word terms, `seldom`, `save-all`).
- After: OK (6 pages, 6 pinned, 0 failing). `quotes.py`: no MISS, same 2 SHORT.

## Fixes

**Labs (both silver lessons).**
1. Lesson 4: the `wreCorn` tile printed about 0.00 quarters for 1d, and the panel told
   the reader to ignore it. Changed `money_unit` from `d` to `£`, so both presets give
   prices as fractions of a pound (13s 4d = 2/3, Fleetwood's £2 19s 1¼d = 2837/960). The
   tile now reads 1, 1.50 and 2 quarters for £1 in money-and-silver, and 0.34 to 1.99 in
   fleetwood-divisions. I checked every average, ratio and inverse by hand, then pinned
   `wreAverage`, `wreRatio` and `wreCorn` from `--observe`. I rewrote the panel apology,
   the body paragraphs, quiz 3's explanation and the module docstring to the figures the
   lab prints.
2. Lesson 5 had the same defect and apology. All three presets are now in `£`, including
   the 42 Windsor prices, each checked against l. 8637–8686. Re-pinned with `wreCorn`;
   body, panel, quiz 3 and the course `how_to` on units rewritten.

**Accuracy against the text.**
3. Lesson 5: the 1741–50 average is £1 13s 9 4/5d (l. 6631), not 9¾d. The aside
   about the "half-century" now says "sixty-four years", and the slip is about 6s 9d.
4. Lesson 5: the Digression's closing warning was misstated as "Poland and Spain have
   plenty of silver and are poor". It now says what l. 8036–8062 says: a high value of
   silver is no proof of poverty and a low value no proof of wealth, and Poland, Spain
   and Portugal are the beggarly cases.
5. Lesson 5: the 1701–64 average £2 0s 6¾d is the table's figure (l. 8827), while the
   text gives 6 10/32d (l. 6518). The lesson now says "in Smith's table".
6. Lesson 4: the passage "It would be more proper, perhaps…" (l. 6600) is about the fall
   after 1700. The lesson used it as a statement about the first period, and now says
   which years it concerns.
7. Lesson 2: Smith's ancient writers are Democritus, Columella, Varro and Palladius
   (l. 5059–5073), not Cato, and he spends about a page on them, not several. Rice's
   yields "are said to be" (l. 5272), so "he says" became "he reports".
8. Lesson 3: "two mines are worked at a loss" now ties the case to Smith's "Some works
   are abandoned altogether" (l. 5549).
9. Lesson 6: fish are "both limited and uncertain" and the metals "not limited but
   altogether uncertain" (l. 7903–7940). The lesson had fish as limited only. The watch
   movement "may now perhaps" be had for 20s (l. 8214–8217).
10. Lesson 1: rent falling from £140 to £50 is a 64% fall. The lesson said "more than
    two-thirds"; it now says "nearly two-thirds".
11. Source comments: lessons 1 and 4 were right. Lesson 2's later ranges and all of
    lesson 3's were off by about 80–100 lines. Replaced with true ranges, and missing
    passages added in lessons 1, 2, 4, 5 and 6.

**Accuracy about others.**
12. Lesson 3: the body said a reader of Ricardo "will recognise" Smith's
    best-mine-regulates rule. In fact Ricardo reversed it, making the least productive
    mine in use regulate the price, and the lesson's own note says so. The body now says
    he turned it round.
13. Lesson 1: Ricardo is no longer made to say that "no combination of landlords could
    raise the price" (I could not confirm it). The lesson now gives his surplus-over-the-
    margin account and says rent is no part of what regulates the price.
14. Lesson 4 note: Malthus is no longer named as doubting that corn is a steady measure.
    His later writing on value leans the other way. Ricardo stays.

**Prose.** Lesson 6, mistake 3, now says dealers "know their own interest better than
the public's", which follows l. 8461–8463.

## Checked and left

All other lab arithmetic (farms, roads, potatoes, mines, Smith's shares, the Highland
pasture and the sheep country), Fleetwood's averages (l. 8509–8632), the 13:12 ratio, the
wool tod and the 1487 cloth, and the claims about Rogers, Phelps Brown and Hopkins,
Hamilton, Fisher, Friedman and Marx. Quiz positions are spread, and every lesson closes on
what the lab cannot settle.

## Left undone

- Lesson 5's Windsor averages now print to two places of a pound (≈ £2.08), so the
  farthing agreement between 25,933/52d, Smith's text and his table is shown by hand in
  the prose, not by the lab. That is the cost of a legible `wreCorn`; I judged it the
  better trade.
