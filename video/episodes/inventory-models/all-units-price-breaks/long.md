---
format: long
lesson: inventory-models/all-units-price-breaks
title: All-units price breaks: when a bigger order costs less
thumb: Check every band's floor
---

@chapter The offer
@title text="All-Units Price Breaks" sub="Inventory Models" art=thumb
A supplier says: order a thousand or more, and every unit is cheaper. Is it worth it? The economic order quantity alone can't tell you, because now the price depends on how much you buy.

@art price-steps
Under all units pricing, crossing a break reprices every unit in the order, not just the ones above it. Buy nine ninety nine at ten each and the bill is nine thousand nine hundred ninety. Buy a thousand at eight each and it's eight thousand. One more unit made the whole order cheaper.

@math heading="Cost per unit time" items="total(Q) = D·price(Q) + K·D/Q + h(Q)·Q/2@D times"
So the cost now has a purchase term, D times the price, and it depends on Q. And the holding rate h usually depends on the price too, because holding is often charged as a fraction of the value on the shelf.

@chapter A broken curve
@art broken-curve
The total cost curve drops by D times the price difference at every break. It's a jump, not a slope. Drawing it as one smooth line would claim costs no order quantity actually has.

@words text="Within a band: an ordinary EOQ curve"
But inside a single band, the price is constant, so the curve is the ordinary one again. One minimum, falling to the left of it, and rising to the right.

@art candidate-dots
So each band offers one candidate. If the band's own economic order quantity lands inside it, that's the candidate. If it lands below the band, the curve is rising throughout, so the candidate is the band's floor: the smallest order that still gets the price.

@chapter The worked schedule
@words text="K = 40 · D = 1200" sub="from 0: 10, h 2 · from 500: 9, h 9/5 · from 1000: 8, h 8/5"
Here's the lesson's schedule. K is forty and D is twelve hundred. From zero units the price is ten, with holding two. From five hundred, nine, holding nine fifths. From a thousand, eight, holding eight fifths. Holding is twenty percent of price throughout.

@math heading="Each band's own √(2KD/h)" items="band 1:  40√30 ≈ 219.09  inside@band one's;;band 2:  (400/3)√3 ≈ 230.94  below → 500@band two's;;band 3:  100√6 ≈ 244.95  below → 1000@band three's"
Band one's own quantity is forty root thirty, about two nineteen, and it's inside. Band two's is about two thirty one, below its floor, so the candidate is five hundred. Band three's is about two forty five, also below, so the candidate is a thousand.

@math heading="Price the candidates" items="219.09:  12000 + 80√30 ≈ 12438.18@two nineteen;;500:  10800 + 96 + 450 = 11346@five hundred;;1000:  9600 + 48 + 800 = 10448@a thousand"
At two nineteen, the purchase bill is twelve thousand, plus eighty root thirty, about twelve thousand four hundred thirty eight. At five hundred, eleven thousand three hundred forty six. At a thousand, ten thousand four hundred forty eight. A thousand wins.

@art whole-scan
As a check, the lab prices every whole quantity from one to eighteen hundred under the all units rule, with no idea of a candidate. The cheapest is a thousand, at ten thousand four hundred forty eight.

@chapter The purchase bill does the work
@art purchase-bill
Notice what decided it. Moving to the third band saves twenty four hundred on purchases, and costs a few hundred in a bigger cycle. Compare only the cycle costs, four thirty eight, five forty six and eight forty eight, and you'd pick exactly the wrong plan, on figures that are all correct.

@art discount-not-worth
Not every discount is worth taking. In the lesson's two band schedule, the price drops from ten to thirty nine quarters at nine hundred. The floor plan costs about twelve thousand six hundred thirty one, more than the two nineteen plan. Saving a quarter a unit costs more in holding than it saves.

@chapter Compare without rounding
@words text="12000 + 80√30  vs  10448"
And the comparison is done exactly. One candidate cost is a whole number plus an irrational multiple of root thirty. Two real candidates can be within a fraction of a percent, so comparing four place decimals could let the rounding decide. The lab brackets them with fractions until they separate.

@chapter Where people slip
@list heading="Common slips" items="Pricing only the units above the break@The first|One holding rate for every band@The second|Forgetting the purchase bill@And the third"
The first slip is pricing only the units above the break. That's incremental pricing, a different contract. The second is using one holding rate for every band. And the third is forgetting the purchase bill, which reliably picks the smallest order, and reliably the wrong one.

@chapter Try it
@words text="Two bands: 10 below 900, 39/4 from 900" sub="K = 40 · D = 1200 · h = 20% of price"
Your turn. Price both candidates in the two band schedule. You should find the first band's two nineteen at about twelve thousand four hundred thirty eight, beating the floor of nine hundred at seventy five thousand seven hundred eighty five sixths.

@end text="Price every band, compare exactly"
You can build your own price schedule and see each band's candidate, on Learn. That's learn dot get er done dot I O.
