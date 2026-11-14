# Review: wealth-wages-and-profits (Book I, Chapters 8-9)

Files: `content/wealth_of_nations/c04_wages/part_a.py`, `__init__.py`.

## Gates

- Before: `preview_subject.py --course wealth-wages-and-profits` OK (5 pages, 5 pinned, 0 failing); `quotes.py` 92 OK, 0 MISS.
- After: preview OK (5 pinned, 0 failing); `quotes.py` 0 MISS. Re-pinned tiles checked by hand and against `labcheck.js --observe`.

## Fixes (15)

### Labs

1. **funds, `declining` preset.** The fund fell 4% while the workers held, so `wwgTrend` read "the workers grow faster than the fund" when the workers were not growing at all. I changed it to the fund at -4% and the workers at +1% (the label says so). Smith's Bengal has the lowest class "overstocked with its own workmen, but with the overflowings of all the other classes" (l. 2372-2373) until want reduces the numbers. Hand check: 10 x (0.96/1.01)^10 = 6.0186, fund 664.83, workers 110.46. Re-pinned `wwgWageLast` "≈ £6.02"; the prose now gives £664.83 and £6.02.
2. **profits, `half` preset.** Two alternative rates were entered as rows, so `witFall` printed "interest 4% → 5% (+1 point)", a rise between two figures that are not a time series. I reordered the rows from ten to eight per cent, labelled that order as the lesson's, and the prose now explains the tile: interest falls 1 point while profit falls 2. Re-pinned all three tiles (5x2=10, 4x2=8; 10-5=5, 8-4=4).
3. **price/parts panel_intro and step 1** said "the same stages as in the first lesson", but course 3's chain is different. They now name the lesson *Wages, Profit and Rent* and say the linen chain is written for this lesson.

### Accuracy against the text

4. L3: Messance was cited as supporting the belief that workmen are more industrious in dear years. His registers show the opposite: more goods made in cheap years (l. 2774-2784). Corrected, and the Scotland and Yorkshire point now reads "no sensible connection either way" (l. 2789-2790).
5. L1: "Chapter 8 is the longest in Book I" is false, because Chapters 10 and 11 are far longer (contents l. 39-43). Removed.
6. L1: "the chapter's first heading" is the drop-cap first sentence (l. 2095). Now reads "first sentence".
7. L1: the closing caution ("should not be read as a comparison of regions") contradicted the presets. It now gives the real cautions: Hales wrote under Charles II, and Smith says that expenses have "increased considerably since" (l. 2521, 2534-2535); and one family's needs are used for all three places.
8. L2: the "three or four hundred thousand ... die of hunger" sentence is Smith's general sentence about "a fertile country" that follows his Bengal sentence (l. 2382-2385). It is no longer attached to Bengal as a direct report.
9. L2 mistake: Smith cites no "East India Company records" for Bengal. Reworded.
10. L3: the forward pointer "the one after the lesson on it" was confused. It now names Chapter 9's last pages and this course's fifth lesson.
11. L4: "the reason ... in the third concept" pointed to the wrong concept. It now points to the second.
12. `__init__` not_covered: rent as "an effect of price, not a cause" was credited to Chapter 7. It is Chapter 11's idea, and is now credited there.
13. `__init__` how_to: "each preset varies a single figure" was not true of the funds presets. Softened.

### Teaching

14. L1 quiz 4: the distractor "Masters are always richer than the workmen's own funds" was close to the correct answer (masters live on their stocks). Replaced with "The masters own the cottages the workmen live in".
15. L5: "with the point about interest" was ambiguous and now reads "with the merchants".

I checked the other claims about later writers and left them as they stand: Ricardo 1817 on the natural price of labour; Malthus 1798 on doubling in 25 years; Mill 1848 and his 1869 recantation after Longe (1866) and Thornton; Hume 1752; Fogel and Engerman; Pomeranz. The Capital lesson titles cited all exist. The arithmetic of every pinned tile was checked by hand (the linen chain to the penny: 416.504, 452.298, 473.337, 513.675; profit on the old advances 48.252). Correct answers: five at each of the four positions.

## Left undone

- `wwgTrend` gives one sentence for any falling wage ("the workers grow faster than the fund"), even when both fall. The kit text is outside my brief, so I configured the presets around it. A kit author may want a separate wording for a falling fund.
- The `europe` growth preset uses 200 years because the kit caps the doubling time there, short of Smith's 500. The prose and label say so.
