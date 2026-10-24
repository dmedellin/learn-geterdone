# Second review: Ground Rent (`capital-ground-rent`, `c13_rent`)

Volume III, Part VI, Chapters 37–47; eleven lessons. Reviewed 2026-10-24 against
the Kerr text (`volume-3-kerr.txt`) and the table images in
`capital-texts/tables/volume-3/` (pp. 764–858), read with the scan's habit of
printing 3 as 8 in mind. Written before reading `docs/pedagogy/capital-ground-rent.md`.

## Summary

- **Arithmetic: no errors.** Every figure in prose, worked lines, keys, quiz
  answers and `why`s was recomputed by hand, and every preset's tiles were read
  with `labcheck.js --observe`; all 35 preset tile sets match both the lesson's
  prose and Marx's printed tables.
- **Quotations: 151 segments, 0 misses.** Convention-only matches are listed below.
- **The six slips the course says are in the Kerr text are all real** (eight
  places, counting the Table II label and the second "3½"), each confirmed
  from Marx's or Engels' own figures and tables. One attribution softened.
- **Sixteen text changes in nine lessons**, mostly places where a sentence said a little more
  or a little other than the chapter does. None changes a preset or a pinned
  figure. Final preview: `OK`.

## The slips the course names in the Kerr text

| # | lesson | the course's claim | check | verdict |
|---|---|---|---|---|
| 1 | Differential Rent I | Table III's rental "from 18 pounds sterling to 22, a growth of 22 1/9%" (l. 5651) is a slip | Table III (p. 768 image) prints rents 2, 5, 8 qrs = 60, 150, 240s, total 15 qrs = 450s = £22½, +25%. £22 would be +22 2/9%, so the text's percentage follows from neither total | **confirmed** |
| 2 | Differential Rent I | "doubled upon C" (l. 5651) is not given by the yields | C's rent goes 120s → 150s (×1¼) in money and 2 → 5 qrs (×2½) in grain. (The same sentence's "more than doubled upon D" also fails in money, 180s → 240s; it holds in grain. Not flagged by the lesson; harmless.) | **confirmed** |
| 2a | Differential Rent I | the table calls the 1⅓-quarter soil A, the sentence before it A′ | Table II image and l. 5627/5629 | **confirmed** |
| 3 | Differential Rent II | "10-2 = 8 quarters … or 12 pounds sterling" (l. 5833) sets four doses against one | At B's £1½ the four doses (4, 1, 3, 2 qrs; £3 cost and profit each) give 6 − 1½ + 1½ + 0 = £3; the 1-quarter dose loses £1½. Marx's own rule two paragraphs earlier (l. 5825–5827) prices each £2½ dose against its own £3 | **confirmed** |
| 4 | Constant Price | Ch. 40 gives D "6 quarters" (l. 5884) but needs 7 | Same sentence: D's second dose pays "two quarters instead of three"; l. 5886 "from three quarters to five (from 9 … to 15)"; table p. 800 prints D's second-investment rent £6 (= 2 qrs). Six would give 4 qrs, 240s. Ch. 41's Table III (p. 803) prints D 4 + 3½ = 7½, rent 5½ qrs, £16½ | **confirmed** |
| 5 | Falling Price | "D and its price of production of 30 shillings would become regulating" (l. 5956) | Table IV (p. 811): B rent 0, selling price £1½ = 30s; D's own price is £6/8 = 15s | **confirmed** |
| 6 | Falling Price | p. 817 table prints C's grain rent 3 and total 25 | Money rent column prints C "8" (= £3, scan) and D "83" (= £33); £3 at £1½ is 2 qrs; 0 + 2 + 22 = 24; the text after the table says the grain rent "would have been doubled" from Table II's 12 | **confirmed**; attribution softened (see L6) |
| 7 | Worst Soil | Engels' average printed "3½ pounds sterling", twice (l. 6422–6424) | 14 / 4½ = 3 1/9; only 3 1/9 gives Engels' own 1/9 on A, and his "4½ quarters at [3 1/9] … make 14 pounds" (at 3½ they make 15¾) | **confirmed** |

## Findings by lesson

Each: what was wrong, what changed (or what is recommended).

**L1 Introductory Remarks on Ground Rent**
1. "In the seventeenth century … Dudley North and Locke … and Turgot" put Turgot
   (1766) in the seventeenth century. Marx says only "in the beginning of
   capitalist production" (l. 5375). *Changed:* North and Locke in the
   seventeenth century, Turgot in the eighteenth.
2. *Recommendation:* "a purchase only transfers a title" is Chapter 46's argument
   (l. 6667), not Chapter 37's; Chapter 37's reply is the slave comparison and
   that rent exists without land-capital. Harmless, since Building Rent repeats it
   with the right chapter.

**L2 Differential Rent: General Remarks**
3. "Why two measures? Marx gives both." Marx writes only the 10 ("surplus-profit
   of 10%", l. 5505); the 11½ is implied by his definition (the difference between
   individual and general price of production) and his own 103½ (l. 5511), never
   written. The two are a known inconsistency in the text, not two measures Marx
   offers. *Changed:* "Marx's text holds both, though it writes out only the
   first", and `mistakes[2]` now says ten is Marx's figure and 11½ follows from his
   definition and his 103½.
4. Quiz 2, option d, "The sale of its goods above their price of production", is
   defensible: the goods do sell above their *individual* price of production
   (103½). *Changed:* "above the general price of production".
5. Confirmed: steam-cheapens (100 → 90) is Marx's own figure (l. 5553), so its
   label "Marx's case" is right.
6. *Kit gap (not edited):* the steam-cheapens price tile prints `£207/2` while the
   prose says 103½ and the surplus tile on the same view prints `£11½`. A
   mixed-number price in the waterfall view would match.

**L3 Differential Rent I**
7. "Or suppose A was farmed first … then the price never rose above 60s." The
   text says the opposite: "the price of wheat at first rose above 60 shillings
   … But when the necessary supply was raised by B … fell once more to 60
   shillings" (l. 5614). *Changed:* the price rose above 60s only until B's supply
   came in, fell back and stayed.
8. Key line "price = worst soil's capital + profit / output" reads with the
   wrong precedence. *Changed:* "price = (capital + profit) / worst output" (the
   box holds 46 characters).
9. *Recommendation (voice):* Ricardo "wrote the most rigorous economics of his
   age" is the lesson's own verdict; "the most systematic" or simply what he
   wrote would present rather than praise.

**L4 Differential Rent II**
10. "The point Marx wanted … is sound" gave a verdict in the lesson's voice.
    *Changed:* the point "does not depend on the slip", and the next two lessons
    compute it dose by dose.

**L5 DR II at a Constant Price**
11. "Producing twice the product with the same capital … releases capital." In
    Marx's yards example (l. 5925–5927) capital is *released* when the same product
    takes half the capital, and *saved* when the same capital doubles the product.
    *Changed:* "the first saves the capital a doubled output would otherwise need".
12. `mistakes[2]` said the text states £15 for D "twice"; it states it once
    (l. 5886) and the p. 800 table implies it. *Changed* accordingly.

**L6 DR II at a Falling Price**
13. "Marx's table on page 817 prints …" The grain-rent slip is in the table as the
    Kerr edition prints it; whose slip it is cannot be told from this edition, and
    the sentence after the table ("the grain rent would have been doubled") has
    the right figure. *Changed:* "The table on page 817 of the Kerr edition", and
    the sentence now cites Marx's doubling of Table II's 12 quarters as the check.
14. "Engels … added a note to the next chapter": the prairie passage is the end of
    Engels' own bracketed section of Chapter 43 (l. 6267–6273, signed F. E.), not a
    note. *Changed:* "closed the section he wrote for the next chapter with a
    passage". ("In the 1890s" dropped: he edited 1885–94.)

**L7 DR II at a Rising Price** — no changes. All three presets check against l. 6352
and l. 6396 (B's £5 dose at £4; A−1 at £4, A−2 at £6, B £15, A £3). Engels'
twenty-one tables (VII, VIIa, VIII, VIIIa, IX, X, Xa; XI–XXIV) counted against the
images and l. 6129–6169. *Recommendation:* "Most of them price each soil's whole
product at its average" is true of the rising-price tables (e.g. Table IX prices
A's 1½ qrs at £4, its average) but the constant-price ones (e.g. Table XV) do
not need averaging; "many" would be safer.

**L8 Differential Rent Also on the Worst Soil**
15. The on-a paragraph skipped the step Marx takes first: with A's second dose at
    3¾, A's two quarters average 3⅜ (l. 6458–6460), and if that average regulates A pays
    no rent; only if the second quarter sells at its own 3¾ does A pay ¾
    (l. 6462). Leaving it out made the per-dose rule look like Marx's only answer
    in a passage where he prefers the average. *Changed:* one sentence added.
16. The both preset's "a market just large enough for the first doses and one
    extra dose" miscounted (the market includes B's, C's and D's second doses).
    *Changed:* "the doses already in use and one extra dose".
17. Checked: p. 858 tables (scan 8 = 3) give A 1, B 3½, C 5½, D 7½ at £3 (rents
    4½, 10½, 16½ = 31½) and at £3½ rents ½, 6¼, 13¼, 20¼ = £40¼ = 805s, as the
    marx preset prints.

**L9 Absolute Ground Rent**
18. `mistakes[0]`: "A price set at will is what Marx calls an actual monopoly
    price." Marx's actual monopoly price is fixed by "the needs and the solvency of
    the buyers" (l. 6586), not by the seller's will. *Changed* to that.
19. *Note, no change:* `mistakes[1]` ("each better soil's rent still exceeds A's by
    the same d, 2d, 3d") is Marx's per-unit statement at l. 6501; at l. 6580 he
    says per-acre differential rents "rise by the corresponding multiples of r".
    Both are in the chapter and do not conflict (per quarter vs per acre), but a
    reader who checks l. 6580 may be puzzled; "per quarter" in the sentence would
    settle it.
20. *Recommendation (voice):* "This is the most disputed chapter of the Part" is
    the lesson's verdict; "Economists have disputed this chapter more than
    the others" or cutting the sentence would do.

**L10 Building Rent, Mining Rent, the Price of Land**
21. Capps "makes the ground worth '400 or 500 pounds sterling'": Capps says he
    may "make 400 or 500 pounds sterling out of it", an annual ground rent
    (it is set against the £300 a year and "the increased ground-rent of 100 or 150
    pounds sterling annually"). "Worth" reads as a capital value, which would
    contradict the preset's capitalising £400 into £8,000. *Changed:* "may make
    '400 or 500 pounds sterling' a year out of it". (The witness's own figures do
    not quite agree, 500 against an increase of 150; the preset uses 400, which does.)
22. "Building rent can be both, Marx says": the chapter says building rent is marked
    by location and "the preponderance of the monopoly price in many cases"
    (l. 6651); it does not say it can be both monopoly-creates-rent and
    rent-creates-monopoly. *Changed:* "Building rent, Marx says, often rests on
    monopoly price".

**L11 Genesis of Capitalist Ground Rent** — no changes. §2 heading, two days a
week (l. 6779), Petty and Cantillon (l. 6725), the physiocrats, rent in kind and
money rent, all as the chapter has them. Clark (1899) is stated in his own
terms.

## Critics and historians

Ricardo (stockbroker, 1815 essay with West, Malthus, Torrens; the Corn Laws),
Anderson (1770s; Marx's "actual discoverer"), Carey (harmonies), North, Locke,
Turgot (corrected century), Palmerston, Engels on 1846 and the prairies, Henry
George (1879), J. B. Clark (1899), Bortkiewicz: names, dates and positions are
accurate and stated at strength. Ricardo's "corn is not high because a rent is
paid" is given at full strength in L7 before Marx's qualification.

## Quiz

Every distractor argued; one changed (L2 Q2 d, above). The others each have a
clear defect stated in the `why`.

## Quotations

`strict_quotes.py c13_rent 3`: 151 segments, 0 misses. Convention-only: "over and
above profit" (L1) is split by the page-break marker at l. 5465/5467 (reported as
l. ?); several one- and two-word spans ("irrational", "differential",
"absolutely", "identical", "offhand", "D") match earlier lines in the volume as
well as their own chapter, and were checked in-chapter; the inner quotation in
L3's Ricardo passage is printed with single curly quotes per the file's stated
convention. "Up to" in L9 quotes the lab tile, not Marx; it reads as a quotation
of Marx and could be set in plain text.

## Arithmetic and tiles

Final preview:
`python3 scripts/preview_subject.py capital --course capital-ground-rent` → 12 pages,
11 executed, 11 with pinned figures, 0 failing, **OK**. Every preset observed with
`labcheck.js --observe`; every tile string recomputed (e.g. on-a: 75s, 15s,
142s 6d, 292s 6d, 442s 6d, 892s 6d; both: market 257/14 = 18 5/14 quarters takes
B's 70s dose and leaves A's 75s dose; rent-rises: 44 × 30 − 550 × 6/5 = 660s).

## Where this review disagrees with the pedagogy assessment

Read after the findings above were written. The assessment's arithmetic and its
verification of the six text slips agree with this review in every figure; the
disagreements are all about what the lessons say Marx argues, which is where the
Course 1 second review also found its errors.

1. **"Fidelity is high … compute a natural advantage's surplus profit by both of
   Marx's measures."** The assessment takes the waterfall lesson's "Marx gives
   both" at face value. Marx writes only the 10; the 11½ is implied by his
   definition and his 103½ and never written (finding 3). The lesson now says so.
2. **The ascending succession in Differential Rent I** passed the assessment;
   it said "the price never rose above 60s", which l. 5614 contradicts in so many
   words (finding 7).
3. **"Opponents at strength … the lesson's own voice"**: the assessment found no
   verdicts in the lesson's voice. This review found "the point Marx wanted … is
   sound" (Differential Rent II, changed), and recommends against "the most
   rigorous economics of his age" (Ricardo) and "the most disputed chapter of
   the Part" (Absolute Ground Rent).
4. **Rent on the worst soil.** The assessment calls the lesson's account of
   Marx's rule and Engels' "one rule met from four sides". In the on-a case Marx
   himself first applies the averaging rule (3⅜, no rent on A) and only then the
   per-dose rule; the lesson gave only the second, which made the lab's rule look
   like Marx's only answer in exactly the passage where he prefers the other
   (finding 15).
5. **Absolute rent's "monopoly price at will"** and **Building rent "can be
   both"** were not flagged; each gave Marx a definition or a claim the chapter
   does not contain (findings 18, 22).
6. **Capps** "makes the ground worth 400 or 500": not flagged; it turns an annual
   ground rent into what reads as a capital value, against the preset's own
   capitalisation (finding 21).
7. **"The slips … are all stated in the right register ('the Kerr text
   prints…')."** One was not: the p. 817 grain rent was "Marx's table". Now "the
   table on page 817 of the Kerr edition", with Marx's own "doubled" as the check
   (finding 13). The assessment softened "misprint" to "slip" at l. 5956 on the
   same reasoning; this is the same repair one paragraph later.
8. **"Engels … the 1846 note"**: it is the end of Engels' bracketed section of
   Chapter 43, not a note; the falling-price lesson said "added a note to the
   next chapter" (finding 14).
9. **Smaller points the assessment's "every distractor was derived" missed:**
   the waterfall quiz's option "above their price of production" is true of the
   individual price (finding 4); Turgot was put in the seventeenth century
   (finding 1); "releases capital" for the case Marx says *saves* it (finding 11);
   "the £15 the text states twice" (finding 12).

Agreed with the assessment: the six slips, the "more than doubled upon D" left
alone, the kit's missing per-acre average as the course's one structural gap, the
load on Differential Rent I, and the voice overall, which is warm, plain and reads
the passage before the arithmetic.
