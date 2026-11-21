---
format: long
lesson: decision-and-rationality/pascals-wager
title: Pascal's wager as a decision table, and the trouble with infinity
thumb: Where the wager turns
---

@chapter The wager
@title text="Pascal's Wager" sub="Decision and Rationality" art=thumb
Blaise Pascal argued that belief in God is the prudent bet. Not that God exists, but that if you aren't certain either way, wagering on God has the larger expected value. Let's set it out as a decision table.

@math heading="The wager as a table" items="wager:  God exists M − c,  no God −c@wagering pays;;abstain:  0,  0@Abstaining pays"
Let p be your probability that God exists. Let c be the cost of the wager, everything a life of belief gives up. And let M be the reward if God exists. Measured from abstaining, wagering pays M minus c if God exists, and minus c if not. Abstaining pays zero either way.

@math heading="The threshold" items="EU(wager) = p · (M − c) − (1 − p) · c = p · M − c@p times M minus c;;wager wins when M > c / p@c over p"
The expected value of wagering simplifies to p times M minus c. That beats abstaining when it's above zero, that is, when the reward M exceeds c over p. At exactly c over p, the two tie.

@art table-rows
So the whole argument lives in one row. A big reward in one state, a small cost in both. Everything turns on how big the reward is, against how likely the state is.

@chapter No standing aside
@art embarked-boat
Pascal himself denied that abstaining was available. You're already embarked, he said. Not to wager for God is to wager against. The table survives that. Read the second row as wagering against, with the same payoff of zero, and nothing in the arithmetic changes. What changes is that you can't say you stayed out of the game.

@chapter On the threshold
@math heading="p = 1/1000, c = 1" items="M = 1000:  EU = 0, a tie@a thousand;;M = 1001:  EU = 1/1000@a thousand and one;;M = 999:  abstaining wins@nine hundred and ninety nine"
Take p as one in a thousand, and c as one. The threshold is c over p, a thousand. With a reward of a thousand, the wager sits exactly on it: a tie. Raise the reward to a thousand and one, and wagering wins, by a thousandth. Lower it to nine hundred and ninety nine, and abstaining wins.

@art threshold-slide
One unit either way reverses the advice. So the number to argue about is the reward, not the shape of the argument. And each factor of ten off the probability moves the threshold by a factor of ten.

@chapter Small probabilities
@art tiny-chance
The first objection says a probability of one in a thousand is too small to count. The table doesn't allow it. A chance that small is exactly offset by a reward that large. That's what an expected value is. Whoever ignores small probabilities must say below which figure they stop counting, and why that figure.

@chapter An infinite reward
@words text="p · ∞ = ∞ for every p > 0"
The second objection is sharper. Suppose the reward is infinite, so no finite cost can outweigh it. Then p times M is infinite for every p above zero. The argument no longer needs a probability, only that it isn't exactly zero.

@art two-gods
That's also its undoing. Any other god, however improbable, who offers an infinite reward on a different condition has the same argument. Picture two gods, each with probability one in a thousand and reward a thousand and one. Wagering on the wrong one costs one and pays nothing.

@math heading="Two gods" items="wager on A:  1/1000@Wagering on either;;wager on B:  1/1000@scores a thousandth;;abstain:  0@beat abstaining"
Wagering on either scores a thousandth. Both beat abstaining, and they tie. The argument recommends both, and you can't do both. With finite rewards, changing a probability or a reward breaks the tie. With infinite rewards, there's nothing to break it with, because infinity times any positive probability is the same infinity.

@chapter Three replies
@list heading="Three replies" items="Cap the reward: the threshold returns@caps the reward|Deny that a probability can be assigned@denies|Keep the infinity, accept it recommends too much@keeps the infinity"
Three replies are on offer, and each has a cost. One caps the reward, so the threshold returns, and the argument becomes an ordinary comparison of a probability with a price. One denies that a probability can be assigned to claims like these. And one keeps the infinity, and accepts that it recommends too much.

@art capped-reward
Capping is the most modest reply. With any finite reward, there's a threshold again, and you can argue about whether your probability clears it. That's an ordinary decision, like any other bet.

@chapter Where people slip
@list heading="Common slips" items="Thinking a tiny probability can be ignored@The first|Treating infinity as a bigger finite reward@The second|Reading the verdict as an argument for belief@the third"
The first slip is thinking a tiny probability can be ignored. The second is treating the infinite reward as just a bigger finite one. They differ in kind, not size. And the third is reading the table's verdict as an argument for belief. It says nothing about whether God exists, or whether belief can be adopted for a reason like this.

@end text="Find where the wager turns"
You can change the reward and the probability and find where the wager turns, on Learn. That's learn dot get er done dot I O.
