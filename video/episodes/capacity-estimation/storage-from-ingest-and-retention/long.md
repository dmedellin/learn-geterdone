---
format: long
lesson: capacity-estimation/storage-from-ingest-and-retention
title: Storage is a sum, not rate times time
thumb: Two missing factors
---

@chapter The question
@title text="Storage from Ingest and Retention" sub="Capacity Estimation" art=thumb
Half a terabyte arrives every day, and you keep it for ninety days. How much storage do you need? Most people say forty five terabytes. The answer here is a hundred and forty one point eight six, and the gap is two factors that got left out.

@art retention-window
Start with the retention window, how long data is kept before it's deleted. Once the system is older than the window, each day's arrivals are matched by one day's deletions. So what you size is everything that arrived across the window.

@chapter A sum over the window
@art flat-staircase
Storage is a sum of the daily ingest over the window. If the ingest never changes, every term is the same, and the sum collapses to rate times days. That's the only case where storage is a product, and it's the case everyone pictures when they multiply.

@chapter Growth makes it geometric
@math heading="Growth g a month" items="daily ingest in month m = i₀ · (1 + g)ᵐ@in month m;;S = 30 · i₀ · Σ (1 + g)ᵐ@the total;;m = 0 … blocks − 1@counting from"
Now let the ingest grow by g a month. In month m, the daily ingest is i nought times one plus g to the m. The window becomes a run of thirty day blocks, each at its own constant rate, and the total is a geometric sum, counting from month zero.

@art growing-staircase
Growth here steps once a month and stays flat inside the month. That's a modelling choice, and it shows up as a staircase rather than a curve. It keeps every term an exact fraction.

@chapter A worked example
@math heading="500 GB/day · 90 days · +5%/month" items="block 1:  500.00 GB/day × 30 = 15.00 TB@five hundred gigabytes;;block 2:  525.00 GB/day × 30 = 15.75 TB@five hundred and twenty five;;block 3:  551.25 GB/day × 30 = 16.54 TB@five hundred and fifty one;;one copy = 47.29 TB@forty seven point two nine"
Five hundred gigabytes a day, growing five percent a month, kept ninety days. Block one runs at five hundred gigabytes a day and adds fifteen terabytes. Block two runs at five hundred and twenty five and adds fifteen point seven five. Block three runs at five hundred and fifty one point two five and adds sixteen point five four. One copy is forty seven point two nine terabytes.

@math heading="Then the copies" items="47.29 TB × 3 = 141.86 TB@three copies;;flat: 500 GB · 90 · 3 = 135 TB@never grew;;growth costs 141.86/135 = 1.0508×@growth costs"
Then three copies make a hundred and forty one point eight six terabytes. If the ingest never grew, it would be a hundred and thirty five. So growth costs one point zero five zero eight times, and the copies cost exactly three times.

@art copies-last
Do replication last. The copies multiply the accumulated total, not the ingest rate. That also keeps the unique data figure visible, and that's the number a retention policy is really about.

@chapter Growth is not a rounding
@art long-window
Five percent over ninety days feels like a rounding. That feeling is about the window. Take a hundred gigabytes a day, kept two years, growing fifteen percent a month. That's five hundred and eighty one point one three terabytes of unique data, against seventy three if it stayed flat. Growth is worth seven point nine six zero seven times.

@words text="3 terms vs 25 terms"
Why? A geometric sum is dominated by its last terms. Ninety days is three terms, and two years is twenty five. So don't ask how big the growth rate is. Ask how many growth steps the window contains.

@chapter Where people slip
@list heading="Common slips" items="Rate × window, then stop@The first|Using the last month's rate for every day@The second|Filing growth as a rounding@The third|Mixing 1024 and 1000@and finally"
The first slip is multiplying rate by window and stopping, which misses both the growth and the copies. The second is using the final month's rate for the whole window, which treats the fastest rate as if it held from the start. The third is filing growth as a rounding. And finally, mixing ten twenty four based units with decimal ones partway through.

@art disk-stack
Stay decimal throughout. A kilobyte is a thousand bytes and a terabyte is ten to the twelve, which is what a disk is sold in. Mix in ten twenty four based units halfway through a chain and the error looks like nothing at all, because both numbers are plausible.

@chapter Try it
@words text="2 TB/day · 1 year · no growth · 2 copies" sub="g = 0, so the sum is rate × days"
Your turn. Two terabytes a day, kept a year, with no growth and two copies. With no growth every term is equal, so the sum really is rate times days. Predict the unique data and the total. Then turn the growth up to five percent and guess what the twelve blocks cost you.

@end text="Watch the staircase pull away"
You can grow the ingest and watch the staircase pull away from the straight line, on Learn. That's learn dot get er done dot I O.
