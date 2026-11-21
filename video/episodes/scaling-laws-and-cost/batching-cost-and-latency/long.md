---
format: long
lesson: scaling-laws-and-cost/batching-cost-and-latency
title: Batching: the cost keeps falling, so it can't choose for you
thumb: Cheaper, then slower
---

@chapter The bargain
@title text="Batching: Cost and Latency" sub="Scaling Laws and Cost" art=thumb
Batching makes things cheaper. Put more items in a batch and the cost per item keeps falling. So should you make batches as big as possible? No, and the reason is a second curve.

@art fixed-spread
Some costs are paid once per batch, whatever's in it. A request, a round trip, an fsync, a commit. Call that F. Batching buys that back, and only that. Other costs are paid per item. Call that v. Spread F across B items, and each pays F over B, plus v.

@math heading="Per-item cost" items="F/B + v@F over B plus v;;F = 2 000 µ$,  v = 100 µ$@two thousand micro dollars"
So the per item cost is F over B plus v. Take a fixed charge of two thousand micro dollars and a per item cost of a hundred.

@math heading="F/B + v" items="B = 1:  2 100 µ$@one item;;B = 2:  1 100 µ$@two items;;B = 10:  300 µ$@ten;;B = 100:  120 µ$@a hundred;;B = 800:  102.5 µ$@eight hundred"
One item a batch costs two thousand one hundred micro dollars each. Two items, eleven hundred. Ten, three hundred. A hundred, a hundred and twenty. Eight hundred, a hundred and two point five.

@art hyperbola-floor
It's a hyperbola sitting on a floor at v. It always falls, and it never reaches the floor. So there's no batch size at which the cost stops improving, and no batch size a cost argument alone will ever choose.

@chapter The wait
@art arrivals-queue
Something else has to stop you, and that's the wait. Items arrive at lambda, five hundred a second here. The first item into a batch waits for the other B minus one to arrive.

@math heading="λ = 500 /s,  B = 100" items="first item:  (B − 1)/λ = 99/500 s = 198 ms@a hundred and ninety eight;;mean:  (B − 1)/(2λ) = 99 ms@ninety nine;;rule of thumb:  B/λ = 200 ms@two hundred"
So the first item waits B minus one over lambda, a hundred and ninety eight milliseconds. On average, half that, ninety nine. The usual rule of thumb, B over lambda, says two hundred. It's over by one inter arrival time, two milliseconds, at every batch size. The one a percentile sees is the first item's wait.

@art fill-wait-line
And the wait rises in a straight line with B. It has no ceiling at all.

@art two-curves
So you have two curves going opposite ways. Cost falls like a hyperbola onto its floor. No B is best at both.

@chapter Choosing B
@words text="F/v = 20" sub="the whole prize: from 21v down to v"
Start with F over v, the size of the prize. Here it's twenty, so an item can fall from twenty one times v to v. If F over v were a half, you'd close the question and look for a different cost.

@math heading="Threshold: F/B ≤ v/5" items="2 000/B ≤ 20  ⟹  B ≥ 100@B at least a hundred;;per item 120 µ$,  17.5× cheaper than B = 1@seventeen and a half;;still on the table:  20 µ$, ever@twenty micro dollars"
Then state a threshold, so someone else can check it. Say, stop when the fixed share falls to a fifth of v. That's B at least a hundred. Each item costs a hundred and twenty, seventeen and a half times cheaper. And whatever B you pick above that, only twenty micro dollars an item is left to win.

@words text="B = 800:  −17.5 µ$,  first item waits 1.6 s"
Go to eight hundred and you save seventeen and a half more, a further fourteen point six percent. And the first item waits one point six seconds, eight times as long. Same curve, but the two ends aren't the same trade.

@chapter A timer too
@art timer-or-size
A batch that only closes when full stalls if traffic stops. So real systems close on whichever comes first, B items or a timer. At five hundred a second, a hundred items and a two hundred millisecond timer, the size wins. But under light traffic, every batch closes short on the timer, and costs more than the table promised.

@chapter Where people slip
@list heading="Common slips" items="Reading “cost keeps falling” as “bigger is better”@The first|Quoting B/λ as the added latency@The second|Forgetting the timer changes both curves@the third"
The first slip is reading the cost keeps falling as bigger is better. The second is quoting B over lambda as the added latency. And the third is forgetting that a timer changes both curves.

@chapter Try it
@words text="F = 500 µ$,  v = 250 µ$,  λ = 200 /s" sub="first move: F/v"
Your turn. Set F to five hundred micro dollars, v to two hundred and fifty, and lambda to two hundred a second. Compute F over v and predict whether batching is worth much. Then apply the same threshold, and work out the cost and both waits.

@end text="Price the wait too"
You can move the batch size and watch cost fall and wait rise, on Learn. That's learn dot get er done dot I O.
