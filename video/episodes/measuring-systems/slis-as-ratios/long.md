---
format: long
lesson: measuring-systems/slis-as-ratios
title: 99.95% plus or minus what? The error bar on an SLI
thumb: Every ratio has an error bar
---

@chapter A ratio is a measurement
@title text="SLIs as Ratios" sub="Measuring Systems" art=thumb
Your availability dashboard says ninety nine point nine five percent, and the objective is ninety nine point nine. Did you meet it? With a thousand requests in the window, the honest answer is that you can't tell.

@art good-over-valid
A service level indicator is a ratio: good events over valid events, counted across a stated window. The objective is the target you compare it against. And the indicator isn't complete without its window and its denominator.

@art denominator-line
The denominator is a decision. A health check, a request the client abandoned, a malformed body. Each is either valid or not, and moving one across the line moves the ratio without anything happening to the service.

@chapter The error bar
@math heading="Each valid event is good with probability p" items="variance of good/n = p(1 − p)/n@p times one minus p;;SE = √(p(1 − p)/n)@the square root"
Treat each valid event as an independent trial that's good with probability p. Then the measured ratio has variance p times one minus p, over n. Its standard error is the square root. Nothing about the system is in that, except p.

@math heading="n = 1 000,  p = 0.9995" items="p(1 − p) = 1999/4000000@nineteen ninety nine;;variance = 1999/4000000000@exact;;SE ≈ 0.0707%  (rounded)@point oh seven oh seven"
A thousand requests at ninety nine point nine five percent. P times one minus p is nineteen ninety nine over four million. Divide by a thousand, and the variance is exact. The standard error, its square root, is about point oh seven oh seven percent. That root is the only rounded figure.

@art error-bar
Now compare. The gap to the objective is point oh five percent. In units of the error bar, that's point seven one. Less than one standard error. A service sitting exactly on the objective would produce a reading like this routinely.

@words text="99.95% ± 0.07%" sub="does not separate us from the objective"
So the honest report is ninety nine point nine five, plus or minus point oh seven, which doesn't separate us from the objective. It's a shorter meeting.

@chapter How many requests?
@math heading="Want SE ≤ w" items="n ≥ p(1 − p) / w²@has to be at least;;gap 0.05% at 2 SE:  w = 0.00025@half the gap;;n ≥ 1999 × 4 = 7 996 requests@seven thousand nine hundred and ninety six"
Turn it round. For an error bar of w, n has to be at least p times one minus p, over w squared. To resolve a gap at two standard errors, use half the gap as w. That's nineteen ninety nine times four, seven thousand nine hundred and ninety six requests. An exact scan over n agrees.

@art narrowing-bars
At a hundred requests a second, that's eighty seconds. And precision costs the square. Halving the error bar takes four times the traffic. A thousand requests can't tell ninety nine point nine from ninety nine point eight.

@chapter What the bar doesn't cover
@words text="A floor on the uncertainty" sub="independence fails during incidents"
Independence is the assumption, and it's the one that fails. Requests that fail because one dependency is down aren't independent, so during an incident the real error bar is wider. This formula is a floor. It's exactly right for the quiet week, which is when the arguments happen.

@art biased-not-noisy
And it covers only sampling noise. A denominator that silently drops requests that never reached the load balancer is biased, not noisy. Doubling the window just makes it more precisely wrong.

@chapter Where people slip
@list heading="Common slips" items="Reading a ratio over requests as one over users@The first|Quoting more digits than the window supports@The second|Changing the denominator between windows@the third"
The first slip is reading a ratio over requests as a ratio over users. A user making ten requests meets the slow tail nine point five six percent of the time, not one. The second is quoting more digits than the window supports. And the third is changing the denominator between two windows you compare.

@art too-many-digits
Ninety nine point nine four seven three, from a five minute window, is division carried to six figures on a measurement good to two. Round the report to the error bar, and state the bar.

@chapter Try it
@words text="5 000 requests,  99.92%" sub="first move: p(1 − p) = (2498/2500)(2/2500)"
Your turn. Same objective, five thousand requests reporting ninety nine point nine two. The first move is p times one minus p. Work out the standard error, express the gap of point oh two percent in units of it, and say in one sentence what the window has established.

@end text="Ask for the window first"
You can move the window and the ratio, and watch the error bar against the objective, on Learn. That's learn dot get er done dot I O.
