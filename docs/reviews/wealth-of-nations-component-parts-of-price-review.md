# Review: The Component Parts of Price (`wealth-component-parts-of-price`)

Files: `content/wealth_of_nations/c03_price/part_a.py`. I made no change to `__init__.py` and added no spoken forms.

## Gates

- Before: `preview_subject.py --course wealth-component-parts-of-price` printed OK (3 pages, 3 pinned, 0 failing). `quotes.py` found no MISS.
- After: OK (3 pages, 3 pinned, 0 failing). `quotes.py` found no MISS.

## Fixes made

**Lesson 1, Wages, Profit and Rent**

1. **Lab: a preset whose tiles the reader was told to ignore.** The `coarse` and `fine` presets (Smith's two manufactories, PSU l. 1601-1611) entered the materials as a wage-only first stage. The body then said the wage and share tiles were "not Smith's. Read the profit tile." The reconfiguration below makes every tile mean something, and the prose now states the assumption instead of telling the reader to look away.
   - The stage is renamed `earlier-hands`.
   - Each label now says the materials are counted as earlier wages, as an assumption of the lab.
   - The body explains the tiles:
     - The wage tile (£1,000; £7,300) is the owner's £300 plus the earlier hands.
     - The profit tile is all the owner's, so the profits of £100 and £730 are Smith's comparison exactly.
     - The share tile prints profit 1/11 in both presets, which is the point: profit follows the stock.
   - The panel intro's "read the profit tile" is gone.
   - I checked `wprStages` by hand (£700 then £1,100; £7,000 then £8,030) and pinned it.
2. **Accuracy about others.** "Marx argued that adding up the parts hides where they come from" was vague. Marx's actual objection, in the Capital lesson the paragraph names, is that the resolution loses the part of price that replaces the means of production used up. The sentence now says that and ties it to Smith's horse. I also added Ricardo's other objection: rent is no part of the price of corn, because that price is set on land that pays no rent.

**Lesson 2, Natural and Market Price**

3. **Prose and lab.** The `glut` paragraph now gives the figure the tile prints: 2,600 shillings in all, that is, −2s on 1,300 yards.
4. **Teaching.** The first mistake said a natural price "may sit on starvation wages". Smith argues in I.8 that wages cannot long fall below what maintains the worker. It now says "low wages".
5. **Labels.** `match` and `glut` now say the schedule is written for the lesson, as `short` already did.

**Lesson 3, Monopoly and the Natural Price**

6. **Labels.** `free`, `m500` and `m400` now say the schedule is written for the lesson.
7. **Teaching.** The first mistake's heading, "Thinking Smith says monopoly sells at some limit price", did not say what the error is. It is now "Reading 'the highest which can be got' as the monopolist's best choice", which is what the body of the mistake corrects.

## Checked and left

- **Smith's text, checked against the lines:**
  - the beaver and the deer;
  - the "undertaker" and profit "upon the whole stock of materials and wages";
  - the two manufactories (£15 × 20 = £300; £1,000 and £7,300 at 10%);
  - landlords who "love to reap where they never sowed";
  - the horse argument;
  - sea-fish, salmon and the Scotch pebbles;
  - the planter, the manufacturer and the gardener;
  - effectual demand and the coach and six;
  - oranges and old iron;
  - "where there is perfect liberty" (l. 1819);
  - corn and linen, and the fluctuations falling on wages and profit;
  - the public mourning, black cloth and the journeymen tailors;
  - the dyer's "high wages of that labour";
  - the French vineyards;
  - corporations as "enlarged monopolies";
  - apprenticeship statutes and the castes of Indostan and Egypt.
- **Lab arithmetic, by hand:**
  - bread: 77, 90.20 and 110.22, with profits 7 + 8.20 + 10.02 = 25.22;
  - fish: 66;
  - pebbles: 20;
  - the market schedule: 14s, +3,200s; 10s, 0; 8s, −2,600s;
  - the monopolist: 3,200, 5,000 and 4,800, peaking at 500.

  All tiles agree with the prose and the worked examples.
- **Others:**
  - Ricardo, 1817, on natural price as cost of production;
  - Marshall's scissors, 1890;
  - Schumpeter, 1942;
  - Cournot, 1838;
  - the Capital lessons "Former Discussions: Quesnay and Smith" and "The General Rate of Profit and Prices of Production", both of which exist.
- **Quizzes:** answer positions are spread (0,2,1,3 / 0,1,2,3 / 3,2,1,0). I found no wrong answer that could be argued for.
- **Closing notes:** each note closes on what the lab cannot settle.

## Left undone

Nothing.
