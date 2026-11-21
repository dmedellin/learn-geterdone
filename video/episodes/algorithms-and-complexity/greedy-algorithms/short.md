---
format: short
lesson: algorithms-and-complexity/greedy-algorithms
title: When grabbing the biggest coin goes wrong
---

@art coin-piles
Always grab the biggest coin? With the wrong coins, that gives you a worse answer.

@math items="coins {1, 3, 4}, make 6@make six;;greedy:  4 + 1 + 1  →  3 coins@Greedy takes;;best:  3 + 3  →  2 coins@three plus three"
With coins of one, three and four, make six. Greedy takes four, then one, then one: three coins. But three plus three uses only two.

@words text="It depends on the coins, not the strategy"
With one, five, ten and twenty five, greedy always works. Whether greedy works is a property of the coin system.

@end text="Full lesson on Learn"
The full lesson on greedy algorithms is on Learn.
