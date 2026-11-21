---
format: long
lesson: accelerate-surveys-and-data/tests-for-relationships-and-classification
title: Correlation, regression and clusters: Accelerate's second-stage tests
thumb: r is not the share explained
---

@chapter The second stage
@title text="Tests for Relationships and Classification" sub="Accelerate, Appendix C" art=thumb
Once the constructs pass their tests, the authors of Accelerate move to the second stage: testing the relationships they predicted, and sorting teams into groups. It starts with one measure.

@quote text="Pearson correlation measures the strength of a linear relationship between two variables" cite="Forsgren, Humble and Kim, Accelerate, Appendix C"
In the appendix's words. Pearson correlation measures the strength of a linear relationship between two variables. Hold on to the word linear.

@art theory-gate
A rule governs everything after it. Every hypothesis tested is supported by theory and literature. Where no theory suggests that one construct predicts another, the authors report correlations only. So a regression in the book tests a predicted relationship. It's neither a discovery of cause nor a fishing trip.

@chapter Correlation and the line
@math heading="One predictor (standard formulas)" items="r = Sxy ÷ √(Sxx · Syy)@S x y over;;slope = Sxy ÷ Sxx@slope;;intercept = ȳ − slope · x̄@intercept;;r² = r · r@r times r"
Pearson's r runs from minus one through zero to one. It's S x y over the square root of S x x times S y y: the summed products of the two deviations from their means, over the root of their summed squares. A regression adds a line. The slope is S x y over S x x, the intercept is the mean of y less the slope times the mean of x, and r squared is r times r.

@list heading="The regressions the authors ran" items="2014: linear regression@twenty fourteen|2015–2017: partial least squares@partial least squares"
The authors used linear regression for twenty fourteen, and partial least squares from twenty fifteen to twenty seventeen. They chose it because it optimizes for predicting the outcome, doesn't require normally distributed data, and suits exploratory research. A regression with several predictors is more than the lab's one line.

@chapter Clusters
@art cluster-groups
The classification tests built the high, medium and low performers. They ran five clustering methods and compared them on the change in fusion coefficients, the size of each cluster, and univariate F statistics. Ward's method did best. They preferred a hierarchical method: it shows parent and child clusters, they had no reason to fix the number in advance, and the data set wasn't too big.

@art group-means
To interpret the clusters, they ran an analysis of variance and compared group means with Tukey's test, adding Duncan's test, which agreed. Differences counted as significant at p below nought point one oh. In every year but twenty sixteen, high performers were best on all four measures, low performers worst, and medium in the middle.

@chapter Five teams
@art five-points
Now five invented teams, each with a practice score from one to five, and a delivery score. In the preset five teams, the delivery scores are two, four, three, six and five.

@math heading="Preset five-teams" items="means: x̄ = 3, ȳ = 4@three and four;;Sxx = 10, Syy = 10, Sxy = 8@eight;;r = 8 ÷ √(10 · 10) = 0.8@nought point eight;;y = 1.6 + 0.8x · r² = 0.64@sixty four percent"
The means are three and four. S x x is ten, S y y is ten, and S x y is eight. So r is eight over ten, nought point eight. The line is y equals one point six plus nought point eight x, and r squared is nought point six four: the line accounts for sixty four percent of the spread of y in this sample.

@art pairing-swap
Now keep the same values, and change only which team gets which score.

@math heading="Same values, new pairs" items="reshuffled: 6, 4, 3, 2, 5 → Sxy = −4@minus four;;r = −0.4 · r² = 0.16@minus nought point four;;a-curve: 5, 2, 1, 2, 5 → r = 0@a curve"
Now pair the same delivery scores in another order: six, four, three, two, five. S x y becomes minus four, so r is minus nought point four, and r squared is sixteen percent. Correlation depends on which values are paired. And in the preset a curve, five, two, one, two, five, every y follows from its x, yet r is zero.

@art curve-flat
Pearson's r sees straight line association and nothing else. So read r of zero as no linear association, not no relationship. And a high r doesn't say which way influence runs, or whether a third thing drives both.

@chapter Where people slip
@list heading="Common slips" items="r as the share explained@share explained|r of zero as no relationship@no relationship|A predictive test as a cause@cause"
Three slips. Reading r as the share explained: nought point eight isn't eighty percent; r squared is. Reading r of zero as no relationship. And treating a predictive test as a finding of cause.

@chapter Try it
@words text="n1 (2, 3) · n2 (4, 1) · n3 (6, 4) · n4 (8, 2) · n5 (10, 5)"
Your turn. Five teams: two and three, four and one, six and four, eight and two, ten and five. Find the means, the three sums, r, r squared and the line. Then predict y at x of eight, and compare it with that team's own y.

@end text="Compute r and its line"
Check it in the lab, on Learn. That's learn dot get er done dot I O.
