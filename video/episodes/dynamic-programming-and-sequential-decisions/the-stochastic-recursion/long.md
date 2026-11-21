---
format: long
lesson: dynamic-programming-and-sequential-decisions/the-stochastic-recursion
title: The stochastic recursion: maximise the expected future
thumb: Choose, then chance
---

@chapter Chance enters
@title text="The Stochastic Recursion" sub="Dynamic Programming and Sequential Decisions" art=thumb
So far, an action decided exactly where you'd end up. Now it only decides the odds. The recursion handles that with one change, and the rest of filling the table backwards stays the same.

@art action-split
An action now chooses a distribution over where you land. So its value is the reward you get right now, plus the expected value of where it sends you.

@math heading="Finite-horizon recursion" items="V_T(i) = 0@zero;;Vₜ(i) = max over a of [ r(a,i) + Σⱼ P(a,i,j) · Vₜ₊₁(j) ]@the best"
With no periods left, every state is worth zero. Otherwise, the value of state i is the best action's immediate reward, plus the sum, over next states j, of the chance of landing at j times its value one period later.

@words text="max outside, expectation inside" sub="choose, then chance resolves"
Notice the order. The maximum is outside and the expectation is inside. You choose, then chance resolves. Swap them and you're assuming you know the outcome before choosing, which is a different, easier problem.

@chapter The instance
@art two-states
Here's the lesson's example. Two states, small and large, and four periods. Growing pays nothing when small, and moves you to large three times in four. In large it pays one and keeps you there. Harvesting pays three when small and keeps you small. In large it pays nine, and knocks you back to small three times in four.

@chapter Filled from the end
@art backward-columns
Fill the table from the end. With zero periods left, both states are worth zero.

@math heading="One and two left" items="1 left:  small harvest 3 · large harvest 9@one period;;2 left, small:  grow 0 + ¼·3 + ¾·9 = 15/2@grow gives;;2 left, small:  harvest 3 + 3 = 6@harvest gives;;2 left, large:  harvest 9 + ¾·3 + ¼·9 = 27/2@twenty seven halves"
With one period left, harvest everywhere: three in small, nine in large. With two left, in small, grow gives a quarter of three plus three quarters of nine, fifteen halves. Harvest gives three plus three, six. So grow. In large, harvest gives twenty seven halves.

@math heading="Three and four left" items="3 left:  small 12 (grow) · large 18 (harvest)@twelve;;4 left:  small 33/2 (grow) · large 45/2 (harvest)@thirty three halves"
Keep going. Three left: small is twelve, growing, and large is eighteen, harvesting. Four left: small is thirty three halves, and large is forty five halves.

@chapter The policy has a clock
@art policy-flip
Now read the small state down the table: harvest, grow, grow, grow. With one period left there's nothing to grow into, so harvesting's immediate three wins. With more time, growing puts three quarters of the chance into the large state. So the best action depends on how many periods remain.

@art absorbing-sold
The lesson's second example makes that stark. Keep a machine and earn three, and it stays owned four times in five. Sell it once for seven, and the sold state pays nothing ever again. With one period left you sell. With two you keep, worth forty three fifths. With three, still keep, at two forty seven over twenty five.

@chapter Checking without a value function
@art distribution-push
Now, the table's number isn't the same claim as the policy being worth that number. So the lab checks it. It fixes the policy and pushes the probability forward, period by period. 
@words text="256 policies, none beats the table" sub="33/2 from small · 45/2 from large"
Then it does that for all two hundred fifty six deterministic policies. None beats thirty three halves from small, or forty five halves from large. Three routes to the same pair of numbers, and only two of them involve a value function at all.

@chapter Where people slip
@list heading="Common slips" items="Averaging the max instead of maximising the average@The first|Assuming the policy is stationary@The second|Rounding exact fractions@And the third"
The first slip is averaging the maximum instead of maximising the average. That's the perfect information problem, and it's never smaller. The second is assuming the policy is stationary. And the third is rounding the fractions. Once rounded, you can't tell a real tie from a near miss.

@words text="Markov: only state and action matter" sub="and expected total reward is a choice"
And remember the assumptions. Transitions depend only on the state and action, and nothing else. And maximising expected reward treats a certain ten the same as a fifty fifty gamble between zero and twenty.

@chapter Try it
@words text="Machine: keep 3 (owned 4/5) or sell 7" sub="find V with 1, 2 and 3 left"
Your turn. Using the machine example, fill the table for one, two and three periods left, as exact fractions. Then say in one sentence why selling is right only at the very end, even though it pays the most of any single action.

@end text="Fill the table on exact fractions"
You can build your own two state process and check every policy against the table, on Learn. That's learn dot get er done dot I O.
