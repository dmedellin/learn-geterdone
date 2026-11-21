---
format: long
lesson: availability-and-failure/nines-and-downtime
title: Nines and downtime: what 99.9 percent actually allows
thumb: One nine, ten times less downtime
---

@chapter The question
@title text="Nines and Downtime" sub="Availability and Failure" art=thumb
Ninety nine point nine percent, or ninety nine point nine nine? The percentages differ by less than a tenth of a point. The outages they allow differ by a factor of ten. That gap is what this video is about.

@art period-bar
Availability is a fraction of a period: the share of time the service is actually serving. One minus A is the unavailability. And the downtime A permits is one minus A, times the length of the period.

@chapter One equation, two directions
@math heading="Both directions" items="downtime = (1 − A) × T@given A;;A = 1 − downtime/T@given a downtime"
Given A, the downtime is one minus A times T. Given a downtime, A is one minus downtime over T. Same equation, rearranged. A target hands you A and you want minutes. A budget hands you minutes and you want A.

@math heading="A = 999/1000, a month" items="T = 2 628 000 s@a month;;downtime = (1/1000) × 2 628 000 = 2628 s@a thousandth;;= 43 min 48 s@forty three minutes"
Take three nines over a month of two million six hundred and twenty eight thousand seconds. A thousandth of that is two thousand six hundred and twenty eight seconds, which is forty three minutes and forty eight seconds.

@words text="Keep A as a fraction" sub="999/1000, not 0.999"
Keep A as a fraction throughout. Nine nine nine over a thousand is exactly three nines. The differences that matter live in the fourth decimal place and beyond, and a rounded percentage hides them.

@chapter One nine apart
@math heading="Month · year" items="99.9%:  43 min 48 s · 8 h 45 min 36 s@ninety nine point nine;;99.99%:  4 min 22.8 s · 52 min 33.6 s@ninety nine point nine nine"
At ninety nine point nine, you may be down forty three minutes forty eight a month, and eight hours forty five minutes thirty six a year. At ninety nine point nine nine, that's four minutes twenty two point eight seconds a month, and fifty two minutes thirty three point six a year.

@art ladder
The percentages differ by point oh nine. The minutes differ by a factor of ten. The percentage is a bad scale for this quantity, and the downtime is a good one.

@art pager-night
And it's the minutes you pay for. In redundancy, in deployment discipline, and in how fast someone has to be woken up.

@chapter Counting nines
@math heading="k nines" items="1 − A ≤ 10⁻ᵏ, largest such k@one minus A;;99.95%:  1 − A = 0.0005@ninety nine point nine five;;10⁻⁴ < 0.0005 ≤ 10⁻³  →  three nines@three nines"
An availability has k nines when one minus A is at most ten to the minus k, for the largest such k. So ninety nine point nine five percent has one minus A of point oh oh oh five. That fits under ten to the minus three, not ten to the minus four. Three nines.

@art half-budget
It shows two nines in its digits, but it has three. And it permits twenty one minutes fifty four seconds a month, half of what ninety nine point nine allows. Nines are a logarithmic scale. Three and a half nines isn't a category.

@chapter The period is part of the number
@art two-months
A downtime only means something against a period. This course fixes a month as a twelfth of a three hundred sixty five day year. Use a thirty day month instead, and three nines is forty three point two minutes. Neither is wrong. Mixing them is.

@chapter A budget is an availability
@math heading="“44 minutes a month”" items="A = 1 − 2640/2 628 000@one minus;;= 10939/10950 = 99.89954%@ninety nine point eight nine;;1 − A > 10⁻³  →  two nines@two nines"
Someone rounds forty three point eight minutes up to forty four. That budget is one minus two thousand six hundred and forty over the month. That's ninety nine point eight nine nine five four percent. By the definition, it has two nines, not three. The rounding went the wrong way across a boundary.

@art boundary-step
That's why starting from a budget is often the more honest order. A team can say how long an outage may last long before it can name a nine, and the arithmetic converts one into the other without negotiation.

@chapter Where people slip
@list heading="Common slips" items="Subtracting the percentages@The first|Quoting a downtime with no period@The second|Counting the printed nines@The third"
The first slip is comparing targets by subtracting their percentages. The second is quoting a downtime with no period. Fifty two minutes is four nines over a year and barely three over a month. The third is counting the nines that are printed rather than the ones that are bought.

@chapter Try it
@words text="A = 99.5%" sub="1 − A = 1/200"
Your turn. Take ninety nine point five percent. One minus A is one two hundredth. Work out the downtime per week and per quarter, count the nines by the definition, and find the monthly budget that buys exactly one more nine.

@end text="Slide between 43 and 44 minutes"
You can convert targets to minutes and back, and watch the nines change at the boundary, on Learn. That's learn dot get er done dot I O.
