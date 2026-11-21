---
format: long
lesson: dynamic-programming-and-sequential-decisions/the-secretary-problem-exactly
title: The secretary problem, solved exactly with fractions
thumb: Reject some, then leap
---

@chapter The problem
@title text="The Secretary Problem, Exactly" sub="Dynamic Programming and Sequential Decisions" art=thumb
You're hiring, and candidates arrive one at a time in a random order. Decide on each one on the spot, and you can't call anyone back. You only win if you pick the very best. How good can your chances be?

@art arrival-line
There are n candidates, all of distinct quality, in a uniformly random order. When each arrives you learn just one thing: its rank among the ones you've seen. Accept or reject, right away, and a rejection is final.

@art rank-only
So you never see a value. You can't ask whether this one is good enough, only whether it's the best so far. That's a weak signal, but it means the answer doesn't depend on how the qualities are distributed.

@chapter Look, then leap
@art look-then-leap
The rule is called look then leap. With parameter r, reject the first r minus one candidates, whatever they are. Then accept the first one better than all of them. If you reach the last candidate, take it.

@art trade-off-curve
It's a trade. A record early on is weak evidence: the best of three often isn't the best of twenty. Reject too few and you stop on a weak record.

@art missed-best
Reject too many, and the best candidate goes past unclaimed while you're still learning the standard. The best r sits at the peak, between those two failures.

@chapter The exact probability
@math heading="Success with parameter r" items="P(1) = 1/n@one over n;;P(r) = ((r − 1)/n) · Σᵢ₌ᵣⁿ 1/(i − 1)@r minus one over n"
For r of one, you take the first arrival, so it's one over n. Otherwise, it's r minus one over n, times the sum, for i from r up to n, of one over i minus one. Every term is a fraction, so the whole table is exact.

@words text="best at i, and best of first i − 1 in the prefix" sub="1/n × (r − 1)/(i − 1)"
Here's why. You win when the best candidate is at some position i, at least r, and the best of the earlier ones sits in the part you rejected. Those are independent, with chances one over n and r minus one over i minus one.

@chapter Four candidates
@math heading="n = 4" items="r = 1:  1/4@one quarter;;r = 2:  ¼ · (1 + ½ + ⅓) = 11/24@eleven twenty fourths;;r = 3:  ½ · (½ + ⅓) = 5/12@five twelfths;;r = 4:  ¾ · ⅓ = 1/4@back to"
With four candidates, r of one gives one quarter. r of two gives a quarter of one plus a half plus a third, eleven twenty fourths. r of three gives five twelfths. And r of four is back to a quarter.

@art all-orderings
So reject one candidate unseen, then take the next record, and you win eleven times in twenty four, a little over forty five percent. Play the rule out on all twenty four orderings and count: six, eleven, ten and six wins. Exactly the same.

@chapter Why fractions
@words text="n = 7:  2088 vs 2052 of 5040" sub="29/70 vs 57/140 · both 0.41"
At seven candidates, the best is reject two, winning twenty nine seventieths. Rejecting three is close: two thousand and eighty eight wins against two thousand and fifty two, out of five thousand and forty orderings. Rounded to two decimals, both are point four one. Only exact fractions can say which is better.

@chapter The famous constant
@math heading="n = 100" items="reject 37:  0.371043@thirty seven;;n/e = 36.7879@n over e;;reject 36: 0.371015 · reject 38: 0.370801@either side"
At a hundred candidates, reject thirty seven, and you win with probability point three seven one oh four three. Meanwhile n over e is about thirty six point seven nine, which rounds to thirty seven. Either side, the rows differ only from the fifth decimal place.

@words text="n/e is a limit, not the answer"
So n over e said look near thirty seven. Only the table says thirty seven beats thirty six and thirty eight. And the rounding isn't dependable. Across the lab's ninety eight settings, rounding n over e gives one too many eighteen times.

@chapter Where people slip
@list heading="Common slips" items="Thinking the rule needs the quality distribution@The first|Reading n/e as the rule@The second|Forgetting how harsh the objective is@And the third"
The first slip is thinking the rule needs to know how quality is distributed. It only uses ranks, but it does need every ordering equally likely. The second is reading n over e as the rule. And the third is forgetting the objective: second best counts the same as nobody at all.

@chapter Try it
@words text="n = 5" sub="find P(r) for r = 1 to 5"
Your turn. With five candidates, compute P of r for every r from one to five as exact fractions, and find the best. Then, if you like, check one of them by counting orderings.

@end text="Reject some, then take the next record"
You can slide the number of candidates and compare the exact table against a full count, on Learn. That's learn dot get er done dot I O.
