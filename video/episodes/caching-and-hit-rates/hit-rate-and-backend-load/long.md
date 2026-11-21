---
format: long
lesson: caching-and-hit-rates/hit-rate-and-backend-load
title: Hit rate and backend load: why one more nine is a factor of ten
thumb: Read the miss rate
---

@chapter The question
@title text="Hit Rate and Backend Load" sub="Caching and Hit Rates" art=thumb
Your cache's hit rate goes from ninety to ninety nine percent. That sounds like a nine point improvement. For the database behind it, it's something much bigger, and this video is about why.

@art split-stream
A cache is described by its hit rate, but it's judged by its miss rate. The backend never sees the hits. It only sees what the cache forwards, and that's the number nobody quotes.

@chapter Two rates, one number
@math heading="Splitting the stream" items="hit rate h  →  served from the cache@the hit rate;;miss rate 1 − h  →  forwarded@the miss rate;;backend load = (1 − h)·λ@the backend load"
Requests arrive at a rate called lambda. The hit rate, h, is the fraction served from the cache. The miss rate, one minus h, is the fraction forwarded. So the backend load is one minus h, times lambda, in the same units as lambda.

@words text="h is about the cache" sub="1 − h is about everything behind it"
Those are one number written two ways. But which one you write down decides what your sentence is about. h is about the cache. One minus h is about everything behind it.

@chapter A worked example
@math heading="λ = 10 000 rps, h = 90%" items="cache absorbs (9/10)(10 000) = 9 000 rps@absorbs;;backend gets (1/10)(10 000) = 1 000 rps@receives;;μ = 2 000 rps  →  ρ = 1 000/2 000 = 1/2@two thousand"
Take ten thousand requests a second at a ninety percent hit rate. The cache absorbs nine thousand a second, and the backend receives one thousand. If the backend can serve two thousand a second, its utilisation, rho, is a half. It's busy half the time.

@chapter One more nine
@art shrinking-misses
Now improve the cache. At ninety five percent, the backend receives five hundred a second. The hit rate went up five points, and the backend's work halved. At ninety nine percent it receives a hundred, a tenth of what it got at ninety.

@math heading="The ratio of miss rates" items="backend at h₂ / backend at h₁ = (1 − h₂)/(1 − h₁)@lambda cancels;;90% → 95%:  (1/20)/(1/10) = 1/2@half the load;;90% → 99%:  (1/100)/(1/10) = 1/10@a tenth"
Divide one backend load by the other and lambda cancels. What's left is the ratio of the two miss rates. Ninety to ninety five is a twentieth over a tenth, half the load. Ninety to ninety nine is a hundredth over a tenth, a tenth of the load.

@art scale-of-points
That's why the same percentage point is worth wildly different amounts. Fifty to fifty one percent divides the backend load by fifty over forty nine, about two percent. Ninety eight to ninety nine percent divides it by two.

@chapter What you were buying
@list heading="λ = 10 000 · μ = 2 000" items="h = 90%  →  1 000 rps · ρ = 1/2@ninety percent|h = 95%  →  500 rps · ρ = 1/4@ninety five|h = 99%  →  100 rps · ρ = 1/20@ninety nine percent|h = 99.9%  →  10 rps · ρ = 1/200@ninety nine point nine"
Here's the same cache four ways. Ninety percent leaves a thousand a second, rho a half. Ninety five leaves five hundred, rho a quarter. Ninety nine percent leaves a hundred, rho a twentieth. And ninety nine point nine leaves ten, rho one two hundredth. Nearly the same hit rates, utilisations a hundred times apart.

@art wait-knee
But the backend feels its wait, not its load. Using the mean wait from the M M one queue, those four rows give one millisecond, point six seven, point five three and point five. The last two barely moved. Past the knee, more hit rate buys almost nothing, because the queue was already nearly empty.

@art cache-wall
So a cache earns the most exactly where the backend is struggling. Going from rho of point nine five to point five is the difference between a system that falls over and one that doesn't.

@chapter Where people slip
@list heading="Common slips" items="Reading a hit-rate gain as a percentage gain@The first|Quoting h in a sentence about the backend@The second|Assuming the wait falls in step with the load@The third"
The first slip is reading a hit rate gain as a percentage gain. Ninety to ninety five halves the work, but fifty to fifty five cuts it by a ninth. The second is quoting h in a sentence about the backend, where ninety nine point nine and ninety nine differ tenfold. The third is assuming the wait falls in step with the load.

@art hot-key-burst
Two cautions. One minus h times lambda is an average, and a hot key expiring sends a burst this formula can't see. And a hit rate is measured, not chosen. Writing ninety nine percent into a plan is a forecast.

@chapter Try it
@words text="λ = 40 000 rps · μ = 1 000 rps" sub="start at h = 95%"
Your turn. Forty thousand requests a second arrive at a backend that serves one thousand. First check that it's overloaded at ninety five percent. Then find the smallest hit rate, in tenths of a percent, that puts rho below a half, and say by what factor the load fell.

@end text="Move the hit rate, watch the backend"
You can slide the hit rate and watch the backend's load and wait move at different speeds, on Learn. That's learn dot get er done dot I O.
