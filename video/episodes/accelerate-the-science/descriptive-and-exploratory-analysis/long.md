---
format: long
lesson: accelerate-the-science/descriptive-and-exploratory-analysis
title: Correlation and the third variable: exploratory analysis in Accelerate
thumb: Coffee doesn't ship code
---

@chapter The second rung
@title text="Descriptive and Exploratory Analysis" sub="Accelerate, Chapter 12" art=thumb
Once you've described your data, the next question is whether anything in it goes with anything else. That's the second rung of the ladder in chapter twelve of Accelerate, and it comes with a warning.

@quote text="Two variables moving together can always be due to a third variable or, sometimes, just chance." cite="Forsgren, Humble and Kim, Accelerate, Chapter 12"
Here it is. Two variables moving together can always be due to a third variable or, sometimes, just chance.

@chapter What exploration is
@art outlier-check
The authors call exploratory analysis a broad category: looking for relationships, perhaps with charts, and spotting outliers. But check that an outlier really is one, and not a legitimate member of the group. They call this the enjoyable stage, where new ideas and hypotheses come from. And anyone who wants to speak of prediction or cause has to go further.

@chapter Pearson's r
@art three-scatters
The tool is correlation: how closely two variables rise and fall together, and not why. The authors report Pearson's r, the strength of a linear relationship, from minus one through zero to one. Points close to a rising line give r near one, a falling line near minus one, a shapeless cloud near zero.

@math heading="Pearson's r (standard statistics)" items="r = Σ(x − x̄)(y − ȳ) ÷ √(Σ(x − x̄)² · Σ(y − ȳ)²)@three sums"
The chapter prints no formula, so this one is standard. Read it as three sums over the pairs: how the two measures vary together on top, and how each varies alone underneath. So the result doesn't depend on the units.

@chapter Cheese and bedsheets
@art cheese-bedsheets
The authors make the point with a joke that's also serious. Tyler Vigen's site lists spurious correlations. Their Figure twelve point one shows per capita cheese consumption against deaths by tangling in bedsheets, with r of nought point nine four seven one.

@words text="Look for a pattern, find a story"
Nobody believes one drives the other. But a reader who goes looking through data for patterns will find a story for whatever turns up. So report the correlations, then go on to analyses that ask more.

@chapter Deploys and coffee
@art two-climbs
Here's one way it happens, on a sample written for this lesson. Eight years of an invented, growing company: its deploys per week, and the coffees its office cafe sells per day. Both rise with head count, and neither has anything to do with the other.

@math heading="Preset shared-growth" items="levels: r = 0.994@nought point nine nine four;;changes in deploys: 6, 6, 3, 5, 4, 6, 5@six, six, three;;changes in coffees: 5, 3, 3, 2, 6, 4, 3@five, three, three;;changes: r = 0@exactly zero"
For the levels, the lab reports r of nought point nine nine four. Nearly a perfect line. Now difference the series, each year minus the year before, so the steady climb drops out. Deploys change by six, six, three, five, four, six, five. Coffees by five, three, three, two, six, four, three. And their r is exactly zero.

@art stepped-changes
Once the shared climb is taken away, nothing is left that moves together. Differencing is a standard device for series that trend with time. The book doesn't use it, and it isn't a test of cause. It's here only to show where the nought point nine nine four came from.

@chapter When the changes agree
@math heading="Preset moving-together: deploys and merged pull requests" items="levels: r = 0.999@nought point nine nine nine;;changes: r = 0.955@nought point nine five five"
Keep the deploys, but swap in merged pull requests per week. The levels give r of nought point nine nine nine, and the changes still give nought point nine five five. These really do move together year to year.

@art third-variable
That's a stronger correlation, and it's still only one. A larger team may well produce both: the third variable of the chapter's sentence. The lab can't show whether it does.

@chapter Where people slip
@list heading="Common slips" items="A high r is a connection@connection|r is a percentage@percentage|r of zero means nothing's happening@zero to mean"
Three slips. Reading a high correlation as a connection. Treating r as a percentage, when it's a coefficient from minus one to one. And taking a zero to mean nothing's happening: r only measures a straight line.

@chapter Try it
@words text="tests: 10, 14, 17, 21, 24 · bookings: 4, 7, 11, 14, 18"
Your turn. Five years of an invented test suite, in hundreds of tests: ten, fourteen, seventeen, twenty one, twenty four. Meeting room bookings per week: four, seven, eleven, fourteen, eighteen. Find r for the levels, then for the four yearly changes.

@end text="Correlate the changes too"
Check your arithmetic in the lab, on Learn. That's learn dot get er done dot I O.
