---
format: long
lesson: duality-and-sensitivity-analysis/complementary-slackness
title: Complementary slackness: check a claimed optimum without pivoting
thumb: Certify it, no pivots
---

@chapter The question
@title text="Complementary Slackness" sub="Duality and Sensitivity Analysis" art=thumb
Someone hands you a plan and says it's optimal. Can you check that claim without running the simplex method? Yes. The claim itself tells you what the prices must be.

@chapter The conditions
@list heading="At an optimum" items="A row with slack is priced at zero@slack must be priced|A used activity is worth exactly its ingredients@used must be exactly"
At an optimal pair, two things hold. A row with slack must be priced at zero. And an activity that's used must be exactly worth its ingredients. Its dual constraint holds with equality.

@art paired-switches
Think of each row paired with its price, and each activity paired with its dual constraint. In every pair, at most one side can have room to spare.

@math heading="Where they come from" items="bᵀy − yᵀAx = yᵀ(b − Ax)@The right gap;;yᵀAx − cᵀx = (Aᵀy − c)ᵀx@The left gap"
Here's why. Weak duality's two gaps are sums. The right gap adds up each price times its row's slack. The left gap adds up each dual gap times its activity. Every term is non negative.

@art zero-products
So the ends are equal exactly when every single product is zero. A price and its slack are never both positive. An activity and its dual gap are never both positive. That's the theorem.

@chapter Certifying a claim
@math heading="Claim: x = (2, 6)" items="cutting: 2 ≤ 4, slack 2  ⟹  y₁ = 0@two spare;;x₁ > 0  ⟹  y₁ + 3y₃ = 3@x one is positive;;x₂ > 0  ⟹  2y₂ + 2y₃ = 5@x two is positive"
Claim: two, six is optimal for the workshop. The cutting row has two spare, so y one is zero. Glazing and assembly are tight, so they give no condition. x one is positive, so y one plus three y three equals three. x two is positive, so two y two plus two y three equals five.

@math heading="Solve and test" items="y₃ = 1,  y₂ = 3/2@y three is one;;y = (0, 3/2, 1) ≥ 0  ✓@all non negative;;bᵀy = 36 = cᵀx  ✓@thirty six"
Solve. y three is one, and y two is three halves. The prices are all non negative, and b y is thirty six, which matches the plan. Certified. The same prices the final tableau holds, with no pivot at all.

@art linear-system
So the conditions turn a claim into a small linear system. Slack rows give zero prices. Positive activities give equations. Solve it, then test the prices.

@chapter A refutation
@math heading="Claim: x = (4, 3)" items="feasible: 4 ≤ 4,  6 ≤ 12,  18 ≤ 18@feasible;;glazing slack 6  ⟹  y₂ = 0@six spare;;y₃ = 5/2,  y₁ = −9/2  ✗@minus nine halves"
Now claim four, three. It's feasible. Glazing has six spare, so y two is zero. Both activities are positive, so two y three equals five, giving five halves. Then y one is three minus fifteen halves, minus nine halves. But a cutting price can't be negative. The claim is refuted, with a reason.

@art refuted-claim
That's a specific reason you can state. No set of prices consistent with this plan is dual feasible, so this plan cannot be optimal.

@words text="cᵀx = 27,  bᵀy = 27" sub="and still not optimal"
Here's the trap. At that claim, c x is twenty seven, and b y is twenty seven too. They agree! But equal values only prove optimality for a feasible pair, and these prices aren't feasible. The agreement means nothing.

@chapter The converse fails
@math heading="max x + y" items="x ≤ 2,  y ≤ 2,  x + y ≤ 4@kiln;;optimum (2, 2),  z* = 4,  all three tight@all three rows;;y₁ + y₃ = 1,  y₂ + y₃ = 1@two equations"
Is a tight row always positively priced? No. Maximise x plus y, with a kiln limit, x at most two, a wheel limit, y at most two, and firing, x plus y at most four. The optimum is two, two, worth four, and all three rows are tight. No slack, so the conditions give two equations for three unknowns.

@art degenerate-corner
The lab reports one, one, zero, and says the third price was never pinned down. So here's a tight row priced at exactly nothing. And zero, zero, one is equally optimal. Degeneracy in the primal is multiple optima in the dual.

@art contradiction
The system can also be contradictory. Claim one, one. Every row has slack, so every price is zero. But both activities are positive, so y one plus y three equals one. That says zero equals one. There are no prices to test, and the lab says so rather than inventing a verdict.

@chapter Where people slip
@list heading="Common slips" items="A tight row must have a positive price@The first|Equal values as the feasibility test@The second|Writing conditions for tight rows@The third"
The first slip is the converse: a tight row must have a positive price. The second is letting equal values stand in for the feasibility test. And the third is writing a condition for a tight row, or an unused activity. Count first: slack rows plus positive activities, nothing else.

@end text="Certify or refute a claim"
You can type a claimed plan, see the system it forces, and get the verdict, on Learn. That's learn dot get er done dot I O.
