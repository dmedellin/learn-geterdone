---
format: long
lesson: accelerate-surveys-and-data/tests-for-bias
title: Tests for bias: early against late respondents, by chi-square
thumb: Did the late answers differ?
---

@chapter Screen first
@title text="Tests for Bias" sub="Accelerate, Appendix C" art=thumb
Before the authors of Accelerate analyse anything, they test their data for bias. Appendix C is a brief reference to their methods, and its first tests end in one sentence.

@quote text="We did not see bias between early and late responders." cite="Forsgren, Humble and Kim, Accelerate, Appendix C"
We did not see bias between early and late responders. Let's see what that test is, and what it can and can't say.

@chapter Before the data
@art survey-prep
Each year the authors fix the constructs and hypotheses they'll test, from the literature, their own findings and debate. Where they can, they reuse items other researchers have validated, like those for organizational performance. Their own items follow accepted procedures from Dillman's work of nineteen seventy eight. And data collection is snowball sampling.

@chapter Three families of test
@list heading="Tests for bias in Appendix C" items="Chi-square: answers in categories@Chi square|T-tests: answers on a scale@T tests|Common method bias: Harman's test, marker variable@Common method bias"
Then come three families of test. Chi square tests compare answers in categories, like gender. T tests compare answers on a scale, like Likert values, and the authors used them for early against late responders. And common method bias, checked two ways: Harman's single factor test, and the marker variable test.

@art method-shadow
Common method bias is a pattern that comes from how the data were collected, say everything asked in one survey, and not from the things asked about. The result: no bias between early and late responders, and no sign that common method bias is a problem in these samples.

@chapter Why early and late
@art late-arrivals
The reasoning is the usual one in survey methods; the appendix doesn't spell it out. People who answer late are, a little, more like people who never answered. If early and late give the same picture, the missing are less likely to change it. But the check can't see people never reached, and a snowball sample isn't random to begin with.

@chapter The chi-square statistic
@math heading="Chi-square" items="E = row total · column total ÷ N@row total times its column total;;χ² = Σ (O − E)² ÷ E@observed minus expected;;df = (rows − 1)(columns − 1)@degrees of freedom"
The arithmetic is doable. Each cell's expected count is its row total times its column total, over the grand total N. The statistic adds, over every cell, observed minus expected, squared, over expected. And the degrees of freedom are rows minus one, times columns minus one.

@art yardstick
You read the statistic against a critical value. The lesson chooses a level of nought point oh five, not the book: three point eight four one for one degree of freedom, five point nine nine one for two. Above it, a gap that large would arise by chance in fewer than five samples in a hundred. It's a yardstick for a gap, not a cause.

@chapter Organization size
@art size-table
Now invented respondents: sixty early, forty late, by the size of their organization. Thirty small, fifty medium, twenty large. So the expected counts are eighteen and twelve for small, thirty and twenty for medium, twelve and eight for large.

@math heading="Preset difference" items="small: 12 early, 18 late → 36/18 + 36/12 = 2 + 3@two plus three;;medium: 30, 20 → 0 + 0@zero;;large: 18 early, 2 late → 36/12 + 36/8 = 3 + 4.5@four point five;;χ² = 12.5 > 5.991@twelve point five"
In the preset difference, small has twelve early and eighteen late: gaps of six, giving two plus three. Medium matches exactly, zero. Large has eighteen early and only two late: three plus four point five. The statistic is twelve point five, above five point nine nine one. With the counts matching expectation more closely, the preset no difference gives just two ninths.

@art one-cell
The biggest term is large, late: two observed against eight expected. That's a reason to ask whether late respondents come from smaller organizations. It doesn't say why, and it doesn't say either group is wrong.

@words text="Expected count 2.5 < 5: flagged"
One more case. In a small two by two table, the statistic is one point six, below three point eight four one. But one expected count is two point five, under five. A statistics rule of thumb, not the book's, says the test is unreliable then, so the lab flags it.

@chapter Where people slip
@list heading="Common slips" items="Below the critical value means no bias@no bias|It's a test of honesty@honesty|Chi-square and t-test are interchangeable@interchangeable"
Three slips. Reading a statistic below the critical value as proof of no bias: it's the absence of a detected difference. Treating the comparison as a test of honesty. And thinking chi square and t tests are interchangeable, when the kind of answer decides.

@chapter Try it
@words text="yes: 30 early, 10 late · no: 20 early, 20 late" sub="deploys from a pipeline? critical value 3.841"
Your turn. Eighty respondents: does the team deploy from a pipeline? Yes: thirty early and ten late. No: twenty early and twenty late. Find the four expected counts, the statistic and the degrees of freedom. Is it above three point eight four one?

@end text="Screen before you analyse"
Check it in the lab, on Learn. That's learn dot get er done dot I O.
