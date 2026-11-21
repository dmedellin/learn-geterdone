---
format: long
lesson: intractability-and-approximation/charging-every-element
title: Greedy set cover and the charging argument behind its log n bound
thumb: Price every element
---

@chapter Greedy set cover
@title text="Charging Every Element" sub="Intractability and Approximation" art=thumb
Greedy set cover isn't within a constant factor of the best. Its guarantee is a harmonic number, and the proof is a lovely trick: put a price on every element.

@art sets-universe
Set cover gives a family of sets whose union is a universe, and asks for as few of them as possible that still cover everything. The greedy rule keeps taking the set that covers the most elements not yet covered, until everything's covered.

@chapter Hand out the cost
@art charges
Each set costs one. When greedy takes a set that covers k new elements, it charges each of them one over k. So every set hands out exactly its own cost, and every element is charged once, by the set that first covers it.

@words text="Σ charges = number of sets taken" sub="exactly, every time"
So the charges add up to the number of sets greedy took. Exactly. Now bounding the answer means bounding a sum of small prices, and each one can be bounded separately.

@chapter Bound each price
@math heading="When r elements remain" items="some optimal set holds ≥ r / OPT of them@at least r over;;so this element pays ≤ OPT / r@at most OPT over r;;total ≤ OPT · (1/n + … + 1/1) = OPT · Hₙ@the harmonic number"
Say r elements are still uncovered. An optimal cover of size OPT covers all of them, so one of its sets holds at least r over OPT. Greedy takes a set at least that good, so the element covered now pays at most OPT over r. Add that up from n down to one, and you get OPT times the harmonic number H n.

@art rising-prices
The prices rise as the cover fills up. The first element pays at most OPT over n. The last can pay as much as OPT on its own. So the guarantee is greedy's cover is at most H n times the optimum.

@chapter Seven elements
@math heading="Universe 1 … 7" items="{3,4,5,6},  {1,2,3},  {4,5,6,7}@the family;;greedy: 3 sets@greedy takes;;optimum: 2 sets@the optimum;;ratio 3/2@three halves"
The family is three four five six, one two three, and four five six seven. Greedy takes the four element set first, then needs two more. The optimum, from an exhaustive search over eight subfamilies, is two: the second and third sets. So the ratio is three halves.

@math heading="The charges" items="4 × 1/4 + 2 × 1/2 + 1 × 1 = 3@a quarter each"
The first set charges a quarter each to four elements. The second charges a half each to two. The third charges one to the last element. That's three, the number of sets. 

@math heading="Allowances OPT / r, with OPT = 2" items="2/7, 1/3, 2/5, 1/2, 2/3, 1, 2@two sevenths;;sum = 2 · H₇ = 363/70@add up to"
With an optimum of two, the allowances for r from seven down to one are two sevenths, a third, two fifths, a half, two thirds, one and two. They add up to two times H seven.

@art allowance-bars
The realised charges are a quarter, four times, then a half, twice, then one. Each is at or below its own allowance. The tightest is the first, a quarter against two sevenths. The bar chart draws each charge against the most the analysis allows it.

@words text="H₇ = 363/140 ≈ 2.59" sub="bound H₇ × OPT = 363/70 ≈ 5.19"
H seven is three six three over one forty, about two point five nine, so the bound is about five point one nine. Three halves was counted. Five point one nine was derived. That gap is the usual state of a guarantee: comfortable, and not evidence the bound could be improved.

@chapter Why greedy lost
@art greedy-trap
The family's built to trip the rule. The biggest set goes first, and afterwards neither of the two sets that together cover everything is whole any more. Looking ahead would have taken those two and stopped. Most families aren't like this. Three of the panel's five give a ratio of one.

@chapter Not a constant
@art log-growth
H n grows without bound. Over seven elements it's about two point five nine. Over a thousand, about seven point four nine. And it's essentially the best possible: no polynomial algorithm does asymptotically better unless P equals N P. That's quoted here, not proved.

@chapter Where people slip
@list heading="Common slips" items="Charging one over the set's size@The first|Quoting a log factor without the universe@The second|Reading 3/2 as typical@And the third"
The first slip is charging one over the set's size, instead of the number of new elements. The charges then fall short of the answer, and every number still looks plausible. The second is quoting a logarithmic factor without saying of what. And the third is reading three halves as what greedy usually does.

@end text="Price every element"
See every charge against its allowance on Learn. That's learn dot get er done dot I O.
