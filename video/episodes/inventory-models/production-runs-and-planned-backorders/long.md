---
format: long
lesson: inventory-models/production-runs-and-planned-backorders
title: Production runs and planned backorders: one formula, two switches
thumb: Two fixes, one formula
---

@chapter Two assumptions to remove
@title text="Production Runs and Planned Backorders" sub="Inventory Models" art=thumb
The plain order quantity model assumes a batch appears instantly, and that you're never short. Remove either assumption, and it turns out you're changing the same thing.

@art instant-sawtooth
Here's the plain picture. A batch of Q appears all at once, a vertical rise, and the level falls in a straight line to zero.

@chapter A machine that takes time
@art production-ramp
Now say stock is produced at a rate P, faster than demand D, while demand carries on. Stock builds only at P minus D. The machine runs for Q over P of the cycle, and the peak is one minus D over P, times Q. Not Q.

@math heading="Economic production quantity" items="peak = (1 − D/P)·Q@the peak;;holding = h·(1 − D/P)·Q/2@average stock"
Average stock is half the peak, so the holding cost becomes h times one minus D over P, times Q over two. Everything else is unchanged. So the answer is the plain formula with a smaller holding rate.

@chapter A shortage you chose
@art backorder-dip
Now let shortages happen, at a cost pi per unit short per unit time. Each cycle spends part of its time in stock, and part of it short by up to b, the planned backorder level.

@math heading="Best backorder level at a fixed Q" items="b = (1 − D/P)·Q·h / (h + π)@b equals;;holding rate ÷ (h + π)/π@divided"
At a fixed Q, the cost is a quadratic in b, and its minimum is at b equals one minus D over P, times Q, times h over h plus pi. Optimise over Q as well, and the holding rate is divided again, by h plus pi over pi.

@chapter One formula
@math heading="Both switches" items="Q* = √( 2KD / (h(1 − D/P)) · (h + π)/π )@one expression"
So here's one expression with two switches. Set P to infinity and the first factor is one. Set pi to infinity and the second is one. Do both, and you're back to the plain economic order quantity.

@words text="K = 100 · D = 1200 · h = 6 · P = 2400 · π = 6" sub="1 − D/P = ½ · (h + π)/π = 2"
The lesson's instance: K a hundred, D twelve hundred, h six, a production rate of twenty four hundred, and a penalty of six. So one minus D over P is a half, and h plus pi over pi is two.

@math heading="Four readings" items="plain:  Q* 200,  C* 1200@plain;;finite P:  200√2,  600√2@finite production;;backorders:  200√2,  600√2@backorders alone;;both:  400,  600@both at once"
Plain, it's two hundred at a cost of twelve hundred. With finite production, two hundred root two and six hundred root two. With backorders alone, exactly the same pair. And both at once, four hundred and six hundred.

@art both-switches
The middle rows match, and that's no typo. Each switch alone halves the effective holding rate here, which multiplies Q by root two. Both together quarter it, so Q doubles and the cost halves. Here, a finite machine and a tolerated shortage are interchangeable.

@chapter Owing a hundred
@art cost-in-b
At a run of four hundred, the best backorder level is a half times four hundred times six, over twelve: a hundred. The cost there is six hundred. At ninety nine or a hundred and one, it's three hundredths more. And refusing any shortage at all costs nine hundred.

@chapter Where the model refuses
@art slow-machine
Set P equal to D, twelve hundred each. One minus D over P is zero, and stock never rises. There's no cycle to optimise. That's a capacity problem, and the fix is a faster machine, not a better Q.

@words text="π = 0: no finite answer"
And set the penalty to zero. Every backorder is free, so the cheapest plan is to owe everybody forever. Pi is the price of a promise, and a model with no price on breaking it will always say break it.

@chapter Where people slip
@list heading="Common slips" items="Using the raw holding rate with finite P@The first|Treating a planned shortage as failure@The second|Reading a refusal as a bug@And the third"
The first slip is using the raw holding rate with a finite production rate, which gives two hundred instead of two eighty three. The second is treating a planned shortage as a failure. Here it saves a third of the cost. And the third is reading a refusal as a bug.

@chapter Try it
@words text="P = 12000 · π = 3" sub="K = 100 · D = 1200 · h = 6"
Your turn. Change the production rate to twelve thousand and the penalty to three. Work out both factors, and you should get a hundred and twenty root thirty for the cost.

@end text="Flip the two switches"
You can switch production and backorders on and off and watch one formula cover all four, on Learn. That's learn dot get er done dot I O.
