---
format: long
lesson: inventory-models/reorder-points-and-two-service-levels
title: Reorder points, and the two numbers called service level
thumb: 68.75% or 99.625%?
---

@chapter Where the risk lives
@title text="Reorder Points, and Two Numbers Called Service" sub="Inventory Models" art=thumb
Demand is random now. You watch the stock all the time, and when it falls to a reorder point, you place an order. How low should that point be?

@art lead-time-window
Here's the key. The order arrives after a lead time of L periods. Before you order, nothing can go wrong. After it arrives, you're restocked. So the only window where you can run out is the lead time.

@words text="Q is a cost question · r is a risk question"
That splits the decision in two. The order quantity Q is a cost question, which the earlier lessons answer. The reorder point r is a risk question, and it's about demand during the lead time and nothing else.

@chapter Lead-time demand
@art convolution
One period's demand is zero with probability a quarter, one with a half, and two with a quarter. Over a lead time of two periods, you add two independent draws. That's a convolution, every way each total can happen.

@math heading="Two periods" items="0:  1/16@zero;;1:  1/4@one;;2:  3/8@two;;3:  1/4@three;;4:  1/16@four"
Total zero has probability one sixteenth. One, a quarter. Two, three eighths. Three, a quarter. And four, one sixteenth. The mean doubled, and the mass piled up in the middle.

@words text="safety stock = r − μ"
Safety stock is r minus the mean demand over the lead time. It's what you hold against variation, and it can be zero or even negative.

@chapter Cycle service
@art quantile-cut
Set r to two, exactly the mean, so zero safety stock. A cycle survives whenever lead time demand is zero, one or two. That's a sixteenth plus a quarter plus three eighths: eleven sixteenths, or sixty eight point seven five percent. Not fifty percent.

@chapter Fill rate
@math heading="Fill rate" items="E[shortage] = ¼·1 + 1/16·2 = 3/8@three eighths;;fill = 1 − (3/8)/100 = 797/800 = 99.625%@ninety nine"
Now measure the same policy another way. The expected shortage per cycle is a quarter of being one short, plus a sixteenth of being two short: three eighths of a unit. Spread over an order of a hundred, the fill rate is ninety nine point six two five percent.

@art cycles-vs-units
Same policy, same instant. Sixty eight point seven five percent of cycles avoid a stockout. Ninety nine point six two five percent of units are met from stock. Cycle service counts cycles, and fill rate counts units.

@math heading="r = 0, Q = 100" items="cycle service: 1/16 = 6.25%@six point two five;;fill rate: 49/50 = 98%@ninety eight"
Push it further. A reorder point of zero means fifteen cycles in sixteen run short: six point two five percent cycle service. But the fill rate is ninety eight percent. Neither number is wrong. They answer different questions.

@words text="Q = 1:  fill rate 5/8 = 62.5%" sub="now below the cycle service of 68.75%"
The gap is the order quantity, which appears in fill rate but not cycle service. Shrink Q to one at r of two, and the fill rate drops to sixty two point five percent, now below the cycle service. One isn't the other rescaled.

@chapter Hitting a target
@art discrete-overshoot
Say you want ninety five percent cycle service. r of three gives fifteen sixteenths, ninety three point seven five. r of four gives a hundred percent. Nothing in between, so you overshoot, with two units of safety stock. A ninety five percent fill rate, meanwhile, is already met at r of zero.

@art longer-lead
And a longer lead time costs more than its extra mean. At three periods, the mean is three, and r of two gives only eleven thirty seconds, about thirty four percent. Worse than a coin. The distribution spread as well as shifted.

@chapter Where people slip
@list heading="Common slips" items="Quoting one service level, meaning the other@The first|Scaling one period instead of convolving@The second|Expecting half at zero safety stock@And the third"
The first slip is quoting one service level and meaning the other. That's the costly one. The second is scaling one period's distribution instead of convolving it, which gets the mean right and the shape wrong. And the third is expecting fifty percent at zero safety stock.

@chapter Try it
@words text="L = 3 · Q = 100" sub="find cycle service and fill rate for r = 3 and 4"
Your turn. With a lead time of three, convolve the one period demand three times. Then find cycle service and fill rate at r of three and r of four, and say which target each one meets.

@end text="Say which service level you mean"
You can change the lead time and order quantity and watch both service levels move, on Learn. That's learn dot get er done dot I O.
