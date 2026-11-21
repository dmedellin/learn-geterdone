---
format: long
lesson: duality-and-sensitivity-analysis/weak-duality-and-certificates-of-optimality
title: Weak duality: a proof of optimality you can check by hand
thumb: Feasible prices are proof
---

@chapter The question
@title text="Weak Duality and Certificates" sub="Duality and Sensitivity Analysis" art=thumb
How do you prove nobody can beat your plan, without searching every plan? You need a certificate. And any feasible set of dual prices is one.

@chapter The chain
@math heading="One number, read two ways" items="yᵀAx = (Aᵀy)ᵀx ≥ cᵀx@at least c;;yᵀAx = yᵀ(Ax) ≤ bᵀy@at most b;;cᵀx ≤ yᵀAx ≤ bᵀy@therefore"
Take any feasible plan x and any feasible prices y. Write down y transpose A x, and read it two ways. Grouped one way, it's at least c x, because A transpose y is at least c, and x is at least zero. Grouped the other way, it's at most b y, because A x is at most b, and y is at least zero. Therefore c x is at most the middle, which is at most b y.

@art two-links
Two links, each needing one sign restriction. Nothing about optimality, no algorithm, no basis. Just feasibility.

@math heading="Workshop:  x = (1, 1),  y = (0, 2, 1)" items="cᵀx = 3 + 5 = 8@eight;;yᵀAx = 0 + 4 + 5 = 9@nine;;bᵀy = 0 + 24 + 18 = 42@forty two"
On the workshop, take x equals one, one, and y equals zero, two, one. The plan earns eight. The middle is nine. The prices value the resources at forty two. So eight, at most nine, at most forty two.

@chapter Weak duality
@words text="cᵀx ≤ bᵀy" sub="every feasible x, every feasible y"
That's weak duality. Every feasible set of prices is an upper bound on the primal optimum. And if a pair ever has equal ends, both are optimal.

@art closed-gap
Why? Any other plan earns at most b y, which equals c x, so nothing beats x. Any other prices are worth at least c x, which equals b y, so nothing beats y. Two lines. No pivots.

@chapter A bound nobody solved for
@math heading="Bakery:  max 5x + 4y" items="6x + 4y ≤ 24,  x + 2y ≤ 6,  x + y ≥ 2@twenty four;;guess y = (1, 0, 0):  6 ≥ 5,  4 ≥ 4  ✓@six at least five;;chain:  9 ≤ 10 ≤ 24@nine;;true optimum 21@twenty one"
A bakery maximises five x plus four y, with six x plus four y at most twenty four, x plus two y at most six, and x plus y at least two. Guess the crudest prices: one, zero, zero. Check them. Six at least five, four at least four. Valid. So no plan earns more than twenty four. The plan one, one earns nine, so the chain is nine, ten, twenty four. The true optimum is twenty one.

@art crude-bound
Not sharp, but proved, by inspecting one column at a time.

@chapter What a gap says
@words text="8 ≤ 9 ≤ 42" sub="gap 1 + gap 33;  optimum 36"
A chain of eight, nine, forty two says the optimum is somewhere between eight and forty two. It's actually thirty six, but nothing in the chain could tell you that. The left gap of one is how much the prices overvalue what this plan uses. The right gap of thirty three is the resource the plan leaves unused, at those prices.

@art bracket
And a gap isn't evidence against either point. The plan could be perfect and the prices dreadful. Only a closed gap says anything about either point on its own.

@chapter Not a certificate
@math heading="y = (0, 0, 1)" items="bᵀy = 18@eighteen;;plan (2, 6) earns 36@thirty six;;2y₂ + 2y₃ = 2 < 5  ✗@only two"
Offer the workshop prices zero, zero, one. Then b y is eighteen, but the plan two, six earns thirty six. Has weak duality failed? No. The x two dual constraint asks two y two plus two y three to be at least five, and these give only two. y was never feasible, so never a certificate.

@art not-certificate
That's the check to run first, and the one most often skipped. A number is a bound because its point is feasible. And the lab enforces it. Type a plan that seems to beat the bound, and it names which point isn't feasible.

@art downward-chain
On a minimisation, the chain runs downward. The prices give a lower bound on cost. A kit that hard coded the direction would report the wrong claim, which is harder to notice than a wrong number.

@chapter Where people slip
@list heading="Common slips" items="Only solved prices count@The first|Quoting a bound without checking feasibility@The second|Reading a gap against both points@The third"
The first slip is believing prices are only worth having if you solved for them. The second is quoting a bound without checking dual feasibility. It's one substitution per column. And the third is reading a gap as evidence that neither point is any good.

@end text="Try to beat the bound"
You can type a plan and prices, read the chain, and try to beat the bound, on Learn. That's learn dot get er done dot I O.
