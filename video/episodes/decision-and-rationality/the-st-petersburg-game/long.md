---
format: long
lesson: decision-and-rationality/the-st-petersburg-game
title: The St Petersburg game: infinite expected value, worth a few dollars
thumb: Infinite on paper, 11 in practice
---

@chapter The game
@title text="The St Petersburg Game" sub="Decision and Rationality" art=thumb
Here's a game with an infinite expected value. And yet almost nobody would pay more than a few dollars to play it.

@art coin-run
A fair coin is tossed until it first lands heads. If that happens on toss k, you're paid two to the k dollars. Heads on the first toss pays two. On the second, four. On the third, eight. And a run of twenty tails before the first head pays over a million.

@words text="What should you pay to enter?"
The question, posed in Nicolaus Bernoulli's letter of seventeen thirteen, is what you should pay to enter.

@chapter Every term is one
@math heading="Prize × chance" items="k = 1:  2 · 1/2 = 1@first toss;;k = 2:  4 · 1/4 = 1@second;;k = 3:  8 · 1/8 = 1@third;;k = 4:  16 · 1/16 = 1@fourth"
The expected value is the sum, over k, of the prize times its probability. The first head falls on toss k with probability one over two to the k. So the first toss gives two times a half, one. The second, four times a quarter, one. The third, eight times an eighth, one. The fourth, one again.

@art staircase
Every term is one. A prize that doubles is exactly cancelled by a probability that halves. After n tosses, the partial sum is exactly n, and a larger n passes any number you name. The expected value isn't a large number. It's no number at all.

@words text="Pay any price?"
So if expected value is the price to pay, you should pay any amount to enter, and no ticket is too dear. Nobody believes that. Ask people what they'd pay, and the answer is usually a few dollars.

@chapter A bank with a bankroll
@art bank-cap
The first reply is that no bank has an infinite purse. Suppose the bank has a bankroll of a thousand and twenty four dollars, which is two to the ten. If the first head arrives on toss ten or earlier, the bank pays in full. Any later, and it pays only a thousand and twenty four.

@math heading="Bankroll 1024" items="tosses 1 to 10:  10 terms of 1 = 10@ten terms;;toss 11:  1024/2048 = 1/2@toss eleven;;toss 12:  1024/4096 = 1/4@toss twelve;;tail:  1/2 + 1/4 + 1/8 + … = 1@add to exactly one;;value of the game:  11@eleven"
The first ten terms add to ten. Toss eleven gives a thousand and twenty four over two thousand and forty eight, a half. Toss twelve, a quarter. The later terms are a half, a quarter, an eighth, and so on, and they add to exactly one. So the whole series sums to eleven.

@art halving-tail
Eleven dollars is the expected value of the game against a bank with a thousand and twenty four. That's a very different answer from the one the infinite sum gave.

@chapter The cap grows slowly
@math heading="Each doubling adds 1" items="bankroll 1024:  value 11@the cap grows slowly;;bankroll 2048:  value 12@two thousand and forty eight;;bankroll 1,048,576:  value 21@twenty one"
And the cap grows slowly. Double the bankroll to two thousand and forty eight, and the value rises by one, to twelve. A bank with a million and forty eight thousand, five hundred and seventy six dollars, two to the twenty, gives a game worth twenty one. A bank with a trillion would still be worth only a little over forty.

@art doubling-bank
That's because the value grows with the logarithm of the bank. Each doubling adds exactly one. The sum is dominated by the early terms, because the late prizes, though large, are very unlikely. Even a very rich casino can't make this game look expensive.

@chapter Two replies
@art bent-utility
So the infinity was in the bank. Another reply is in the utility, and it's Daniel Bernoulli's, from seventeen thirty eight. If you value each extra dollar less, the late prizes are worth little to you, and the sum of the utilities can be finite without any cap.

@words text="Only a ceiling closes every such game."
Both replies leave something unsaid. A curve that keeps rising, however slowly, can be outrun by a game whose prizes grow faster, and the infinite sum returns. Only a utility with a ceiling closes every such game, and a ceiling on how good things can get is a strong thing to assert.

@chapter Where people slip
@list heading="Common slips" items="Thinking infinite expected value means pay anything@The first|Reading the cap as refuting expected value@The second|Expecting the value to grow with the bank@the third"
The first slip is thinking an infinite expected value means you should pay any price. The infinity belongs to an idealised bank. The second is reading the cap as a refutation of expected value. A gap still remains between twenty one and what most people would pay. And the third is expecting the value to grow in step with the bank.

@end text="Change the bankroll, watch the sum"
You can change the bankroll and the number of terms, and watch the sum settle, on Learn. That's learn dot get er done dot I O.
