---
format: long
lesson: inventory-models/the-economic-order-quantity
title: The economic order quantity, and just how flat the bottom is
thumb: Where the two costs meet
---

@chapter The trade-off
@title text="The Economic Order Quantity" sub="Inventory Models" art=thumb
Order often, and you pay for lots of orders. Order big, and you pay to store it all. Somewhere in between is the cheapest batch size. Let's find it, and then measure how much it matters if you miss.

@art big-batch-small-batch
Here's the model. One item, drawn from stock at a steady rate D. Every order costs a fixed K, whatever its size, and it arrives all at once the moment stock hits zero. Holding stock costs h per unit per unit time. You choose the batch size Q.

@art sawtooth
So the stock level is a sawtooth. A batch of Q arrives, demand drains it in a straight line to zero, and the next one arrives. Because the line is straight, the average stock is Q over two.

@math heading="Cost per unit time" items="C(Q) = K·D/Q + h·Q/2@C of Q"
So C of Q is K D over Q, plus h Q over two. The first term is the ordering bill: D over Q orders, at K each. The second is the holding bill: the holding rate times the average stock.

@chapter Where the halves meet
@art two-costs
The ordering bill falls as the batch grows. The holding bill rises. Neither can be made small without making the other one large, and that's why there's an answer at all.

@words text="K = 100 · D = 1200 · h = 6"
Take the lesson's workshop: K of a hundred per order, twelve hundred units a year, and holding at six per unit per year.

@math heading="Ordering + holding" items="Q = 100:  1200 + 300 = 1500@a hundred;;Q = 150:  800 + 450 = 1250@one fifty;;Q = 200:  600 + 600 = 1200@two hundred;;Q = 300:  400 + 900 = 1300@three hundred;;Q = 400:  300 + 1200 = 1500@four hundred"
At a hundred, it's twelve hundred plus three hundred, fifteen hundred. At one fifty, twelve fifty. At two hundred, six hundred plus six hundred, twelve hundred. At three hundred, thirteen hundred. And at four hundred, fifteen hundred again.

@art total-bowl
The total is least exactly where the two columns are equal. That's the whole trick.

@chapter The formula
@math heading="Set the halves equal" items="K·D/Q = h·Q/2@set the two;;Q² = 2KD/h@Q squared;;Q* = √(2KD/h),  C* = √(2KDh)@the square root"
Set the two halves equal, and you get Q squared equals two K D over h. So the best quantity is the square root of two K D over h, and the best cost is the square root of two K D h. No calculus needed. The next lesson proves it's the minimum.

@words text="Q* = 20√30 ≈ 109.5445" sub="K = 50 · D = 600 · h = 5"
Here the workshop came out whole: two hundred, and twelve hundred. That's a coincidence. With K of fifty, D of six hundred and h of five, the answer is twenty root thirty, about one oh nine point five. The cheapest whole quantity is one ten, found by pricing every whole number, not by rounding.

@chapter How flat is flat
@math heading="Order t times the best" items="C(t·Q*) / C* = (t + 1/t) / 2@t plus one over t;;t = ½ or 2:  5/4@a half;;t = 6/5:  61/60@six fifths"
Everyone says the cost curve is flat near the bottom. You can measure it. Order t times the best quantity, and the cost is t plus one over t, over two, times the minimum. K, D and h all cancel. Order a half or double, and you pay five quarters. At six fifths, only sixty one sixtieths.

@art half-and-double
So half the batch and twice the batch cost the same twenty five percent extra. In the workshop, that's fifteen hundred at a hundred, and fifteen hundred at four hundred. The curve is symmetric in t, not in Q.

@art flat-band
And within one percent of the minimum, you can order thirteen point two percent too little, or fifteen point two percent too much. Those percentages are the same in every warehouse, because t has no K, D or h in it.

@chapter Where people slip
@list heading="Common slips" items="Charging holding on the whole batch@The first|Hearing flat as anything will do@The second|Quoting the decimal as the answer@And the third"
The first slip is charging holding on the whole batch instead of the average, Q over two. The second is hearing flat as anything will do. At five times the best, you pay a hundred and sixty percent more. And the third is quoting the decimal as the answer, when twenty root thirty is the answer.

@chapter Try it
@words text="Within 5% of the minimum?" sub="K = 100 · D = 1200 · h = 6"
Your turn. In the workshop, find the range of batch sizes that cost within five percent of the minimum. You should get about one forty six to two seventy four.

@end text="Watch the two halves meet"
You can drag the batch size and watch the two costs cross, on Learn. That's learn dot get er done dot I O.
