# Review: wealth-different-employments (Book I, Chapter 10)

Files: `content/wealth_of_nations/c05_employments/part_a.py`, `__init__.py`.

## Gates

- Before: `preview_subject.py --course wealth-different-employments` OK (5 pages, 5 pinned, 0 failing); `quotes.py` 110 OK, 0 MISS.
- After: preview OK (5 pinned, 0 failing); `quotes.py` 0 MISS. No preset values changed. I checked every pinned tile by hand and against `labcheck.js --observe`: net 300/300/300/300, 60/year learning, 3 and 105 for cutler, 1.212 x 300 - 3 = 360.60; lottery 4,200, 2,400/21 = 114.29, 19/18; apothecary 4/40 = 10%, grocer 10/100, city 960/10,000 = 9.6%; parishes 312/468/390.

## Fixes (14)

### Accuracy against the text

1. L5 note: it said the first lesson quotes Smith's weekly wages of common labour, "four or five shillings, six, and nine or ten in London". The first lesson quotes only the six-against-nine-and-ten of masons (l. 3376). Replaced with Smith's Chapter 8 figures for nearby places, 18d in London and 14-15d a few miles off, a difference "not always sufficient to transport a man from one parish to another" (l. 2441-2448).
2. L1: coal-heavers were said to earn "six to ten shillings a day, about four times common labour". Smith says six shillings is about four times (l. 3407-3409), from an inquiry he cites. Corrected.
3. L1 quiz 1: "colliers earn about double". Smith gives double at Newcastle and three times in parts of Scotland (l. 3398-3400, 3405). Now reads "double or triple".
4. L2: "The sea is a better lottery than the army" is a verdict Smith does not give. He says only that its great prizes are smaller and its small ones more numerous (l. 3591-3592). Reworded.
5. L4: one mistake said Smith puts the needed teaching at "a few weeks in a common mechanic trade". He says a few weeks for clocks and watches, and "a few days" for the common mechanic trades (l. 4069-4074). Corrected, and the worked example's "after" line now reads "a few weeks ... at most".
6. `__init__` blurb: "the longest chapter of Book I" is false, because Chapter 11 runs pp. 124-224 against Chapter 10's pp. 86-124 (contents l. 41-43). Now reads "one of the longest".

### Accuracy about others

7. L1 note: Mill (1848) was said to hold that wage differences between grades are "larger than compensation explains". What he argued is that the hardest and most disagreeable work is often the worst paid, the reverse of compensation, because those who do it have no choice. Corrected. Cairnes (1874) on non-competing groups is unchanged.
8. L3 note: "Capital's course on average profit" now names the lesson by title, *The General Rate of Profit and Prices of Production*.
9. L5 note: the settlement historiography ("settlement moved less labour") was garbled. It now says historians dispute how far the laws obstructed movement in practice.

### Labs

10. L4 `capped` preset: its base tiles show the uncapped trade, so `wadSpread` reads "every employment nets the same". The prose now says that those tiles show the trade before the cap, and that the limit and ranking tiles show it after.
11. L4 panel_intro: "the same labourer and cutler as in the first lesson" was wrong, because L1 has no cutler. Reworded.

### Teaching

12. L2 quiz 3: the distractor "The tickets are paid for by the state" could be argued for from Part II's churchmen educated at public expense (l. 4298 ff.). Replaced, and the explanation rewritten. That explanation had also named "public education", which was not among the options.
13. L3 quiz 2: the distractor "Stock moves freely between trades and labour does not" is close to Smith's own Part II sentence on corporations (l. 4486-4488). Replaced with "Every trade employs about the same amount of stock", and the explanation rewritten.
14. Answer positions were 6/7/4/3 across positions 0-3. I reordered two questions (L1 q4 to position 2, L5 q4 to position 3), giving 5/6/5/4.

I checked the other claims about later writers and left them as they stand: Ogilvie and Epstein on guilds, Cairnes, the reading of the curate against the mason under the Statute of Labourers (l. 4321-4332), and the "greatest disorder ... in the police of England" (l. 4500). The Capital titles cited exist.

## Left undone

- The net view's `wadLimited` and `wadRankAfter` print "no limit given" on every preset without a limit. That is an honest empty state from the kit, so I left the presets as they are.
- The `free` parish wage of 5/4 shilling is arbitrary (labelled as written for the lesson). The prose already says the lab cannot tell where the wages would meet.
