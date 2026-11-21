---
format: long
lesson: dynamic-programming/where-the-greedy-choice-fails
title: Where greedy fails: fewest coins, and the recurrence that replaces the rule
thumb: Largest coin first is wrong
---

@chapter The question
@title text="Where the Greedy Choice Fails" sub="Dynamic Programming and Optimal Substructure" art=thumb
Making change sounds easy. Take the biggest coin that fits, and repeat. With everyday coins, that works. But change the coins to one, three and four, and ask for six, and the obvious rule gets it wrong.

@art coin-piles
Here's the problem. Given some coin denominations and an amount, find the fewest coins, using each denomination as often as you like, that add up to exactly that amount. And if no combination works, the answer is that it can't be made. That's a result, not a failure.

@chapter Six from one, three and four
@math heading="Coins 1, 3, 4  ·  amount 6" items="largest first:  4 + 1 + 1  →  3 coins@Largest first;;best:  3 + 3  →  2 coins@three plus three"
Largest first takes the four, leaving two. Then a one, then another one. Four plus one plus one, three coins. But three plus three is just two coins. Both pay six. Only one is fewest, and the rule doesn't find it.

@art greedy-commit
Notice how little it took. Three coins and an amount of six. Nothing is adversarially large. The rule committed to the four before it knew what that would cost, and it never looked back.

@chapter Rule or recurrence
@words text="A rule says what to do next" sub="A recurrence says what the answer is"
Here's the key distinction. A rule says what to do next: take the largest coin that fits. A recurrence says what the answer is, in terms of smaller answers, and commits to nothing.

@math heading="Fewest coins" items="f(0) = 0@f of zero;;f(a) = 1 + min over coins c ≤ a of f(a − c)@f of a;;f(6) = 1 + min(f(5), f(3), f(2))@f of six;;f(3) = 1  →  f(6) = 2@f of three"
F of a is the fewest coins making a. F of zero is zero. F of a is one plus the smallest f of a minus c, over coins c that fit. So f of six is one plus the least of f of five, f of three and f of two. F of three is one, so f of six is two.

@art row-of-cells
Each value reads only smaller amounts, so you can work them out in order, from zero upward, and every one is ready when it's needed.

@art try-every-first
The recurrence tries every legal first coin at once, and keeps the best. That's not cleverness. It just doesn't throw away the alternatives before it knows what they cost.

@chapter Why it's correct
@words text="Optimal substructure" sub="an optimal solution contains optimal solutions to smaller instances"
What licenses the recurrence is optimal substructure. If a fewest coin way of making a starts with coin c, what's left must be a fewest coin way of making a minus c. Otherwise you could swap in something cheaper, and beat the optimum.

@words text="Greedy choice property ✗" sub="no optimal way to make 6 uses a 4"
Greedy needs more. It needs some optimal solution to agree with the rule's first step. For six, no optimal solution contains a four, so that property is simply false. Optimal substructure survives, which is exactly why the recurrence still works.

@chapter Three routes
@list heading="Same answer, three costs" items="No memory:  24 calls@no memory|Memo:  14 calls@writing each answer down|Table:  28 cells@filled bottom up"
The lab runs the recurrence three ways. As a recursion with no memory. As the same recursion, writing each answer down the first time. And as a table filled bottom up. All three answer two. The costs are twenty four calls, fourteen calls, and twenty eight cells.

@art crossing-curves
Look again. The recursion with no memory did less work than the table. On this input, the exponential method beats the polynomial one. Move the amount to eighteen, and the same two cost twenty two thousand and eighty nine calls, and seventy six cells. A count at one size can't order two growth rates.

@chapter Where people slip
@list heading="Common slips" items="Reading one greedy failure as a verdict on greedy@The first|Treating optimal substructure as obvious@The second|Trusting the smaller count at one size@The third"
The first slip is reading this as a verdict on greedy. It's one rule, on one coin system. The second is treating optimal substructure as obvious. The longest simple path doesn't have it, because two halves can share a vertex. The third is trusting the smaller count at one size.

@art longest-path
That longest path case is worth seeing. Two halves can each be longest on their own, and still meet at a repeated vertex, so their join isn't a simple path at all. Skip the substitution argument, and you can write a confident recurrence for a problem that has none.

@chapter Try it
@words text="coins 1, 2, 5" sub="does largest first ever lose?"
Your turn. Switch to coins one, two and five, and try a few amounts with largest first and with the recurrence. You'll find they agree. Then explain why that agreement is a fact about the amounts you tried, not a proof.

@end text="Run all three routes yourself"
You can try your own coins and watch the three routes count their work, on Learn. That's learn dot get er done dot I O.
