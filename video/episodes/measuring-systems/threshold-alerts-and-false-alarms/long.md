---
format: long
lesson: measuring-systems/threshold-alerts-and-false-alarms
title: A healthy service, a 2% alert, and 104 pages a week
thumb: 104 false pages a week
---

@chapter A threshold on a sample
@title text="Threshold Alerts and False Alarms" sub="Measuring Systems" art=thumb
Your service runs at one percent errors and never changes. You alert at two percent. How often does it page you? About a hundred and four times a week.

@art binomial-bars
A threshold alert fires when a ratio measured over a window crosses a fixed value. But that ratio comes from a sample, and a sample varies even when the true rate doesn't. The error count in a window is a binomial random variable.

@math heading="p = 1%,  n = 200,  τ = 2%" items="τ · n = 4,  so it fires at k = 5@five errors;;E[X] = 2 errors a window@The mean is two;;P(X ≥ 5) = 0.051746…  ≈ 5.175%@five point one seven five"
Two hundred requests a window at a true one percent. Two percent of two hundred is four, so the alert needs strictly more, five errors. The mean is two. And the exact binomial tail, the chance of five or more, is five point one seven five percent.

@words text="Nothing has changed about the service"
About one window in nineteen crosses the threshold anyway. Five errors out of two hundred is an ordinary thing for a process with a mean of two. This isn't a tuning problem with a better threshold hiding behind it. It's what a threshold on a small sample does.

@chapter The boundary
@art off-by-one
And watch the boundary. Firing at four instead of five would be fourteen point two percent. At six, one point six percent. One error either way is a factor of about three.

@chapter From windows to pages
@art many-windows
Now multiply. Five minute windows give seven times twenty four times sixty over five, two thousand and sixteen windows a week.

@math heading="Pages" items="0.051746 × 2 016 = 104.32 a week@a hundred and four;;≈ 14.9 a day@fourteen point nine;;P(≥ 1 in the next hour) = 1 − (1 − 0.0517)¹² = 47.14%@forty seven"
Times point oh five one seven, that's a hundred and four point three two false pages a week, about fourteen point nine a day. And the chance of at least one page in the next hour, across twelve windows, is forty seven point one four percent.

@art pager-buzz
That's the number that matters. A forty seven percent chance of being paged in any hour by a service with nothing wrong. After a week of it, the page carries no information, and the response to a real outage looks just like the response to the hundred and fifth false one.

@words text="1 − (1 − p)ᵏ, the third time"
And that's one minus one minus p to the k, for the third time on this course. The sampling capture probability, the load test meeting its tail, and now this.

@chapter Two levers
@art wider-window
Widen the window to fifteen minutes, six hundred requests, and keep two percent. It now fires at thirteen errors. That's point eight four nine percent of six hundred and seventy two windows, five point seven one pages a week. A bigger sample's ratio varies less.

@art higher-threshold
Or raise the threshold to four percent on two hundred requests. It fires at nine, point oh two one percent, point four three pages a week. Quieter still. But at a true two percent, double the healthy rate, the mean is four and the alert wants nine. It no longer catches the thing it was built for.

@words text="Window costs latency. Threshold costs sensitivity."
So the wider window buys quiet with detection latency. The same regression is caught, ten minutes later. The higher threshold buys quiet with sensitivity, and some regressions are never caught. Pull the window lever first.

@chapter Where people slip
@list heading="Common slips" items="Treating one crossing as a fact about the system@The first|Judging an alert by its per-window rate@The second|Raising the threshold when the window is the problem@the third"
The first slip is treating one crossing as a fact about the system. The second is judging an alert by its per window probability, instead of its weekly count. And the third is reaching for the threshold when the window is the problem.

@chapter Try it
@words text="p = 0.5%,  100 requests a minute,  τ = 2%" sub="first move: mean 0.5, fires at 3"
Your turn. A true rate of half a percent, one minute windows of a hundred requests, and a two percent threshold. The mean is point five, and it fires at three. Work out the tail, the windows a week, and the pages. Then say which lever you'd pull, and whether a ratio threshold suits a service this small.

@end text="Count the pages before you ship"
You can move the rate, the window and the threshold and watch the weekly pages, on Learn. That's learn dot get er done dot I O.
