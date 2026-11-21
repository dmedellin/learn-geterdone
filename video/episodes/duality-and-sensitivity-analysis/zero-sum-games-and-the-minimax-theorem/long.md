---
format: long
lesson: duality-and-sensitivity-analysis/zero-sum-games-and-the-minimax-theorem
title: The minimax theorem is just strong duality
thumb: Mixing buys a guarantee
---

@chapter The question
@title text="Zero-Sum Games and the Minimax Theorem" sub="Duality and Sensitivity Analysis" art=thumb
Two players. One picks a row, the other picks a column, and whatever one wins, the other loses. Is there a best way to play? Yes, and finding it is a linear programme.

@art payoff-grid
A zero sum game is a payoff matrix. The row player chooses a row, the column player a column, and the row player receives that entry. A mixed strategy is a probability distribution over your own choices.

@chapter The row player's LP
@words text="Maximise the worst case"
The row player wants the mixture with the best worst case. A worst case is a minimum, which isn't linear. So add one variable, v, for the guaranteed payoff, and require it to be at most the expected payoff against every single column. Then maximise v.

@math heading="A = (3 −1 / −2 1)" items="max v@maximise v;;3p₁ − 2p₂ ≥ v@against column one;;−p₁ + p₂ ≥ v@against column two;;p₁ + p₂ = 1,  p ≥ 0,  v free@the mixture"
Take the matrix with rows three, minus one, and minus two, one. Maximise v. Against column one, three p one minus two p two is at least v. Against column two, minus p one plus p two is at least v. And the mixture adds to one, with p non negative and v free.

@chapter Its dual
@art dual-mirror
Now take the dual of that programme. Out comes: minimise a value w, subject to the expected payoff against every row being at most w, with the weights summing to one. That's exactly the column player's problem. The dual variables are the column player's mixture.

@words text="Minimax theorem = strong duality"
So the minimax theorem is strong duality with different nouns. Both programmes are feasible and bounded, so their optima are equal. The best guarantee the row player can secure equals the least the column player can hold them to. That number is the value of the game.

@math heading="Solved" items="v = 1/7@one seventh;;p = (3/7, 4/7)@three sevenths;;q = (2/7, 5/7)@two sevenths"
Here the value is one seventh. The row player mixes three sevenths and four sevenths. The column player mixes two sevenths and five sevenths.

@art two-pies
Two mixtures, and one number they agree on. The row player can't be held below it, and the column player can't be pushed above it.

@chapter What mixing buys
@math heading="Against q" items="row 1:  3(2/7) − 1(5/7) = 1/7@row one earns;;row 2:  −2(2/7) + 1(5/7) = 1/7@row two earns"
Against the column mixture, row one earns three times two sevenths, minus five sevenths, which is one seventh. Row two earns minus four sevenths plus five sevenths, also one seventh. Both exactly the value. That's complementary slackness, and it's forced.

@math heading="Guarantees" items="best pure guarantee:  −1@minus one;;mixture guarantees:  1/7@one seventh;;mixing bought 8/7@eight sevenths"
But a pure row can't promise that. Row one alone has a worst case of minus one, and row two of minus two. So the best pure promise is minus one. The mixture promises one seventh. The difference, eight sevenths, is what mixing bought.

@art exploit-pure
Mixing isn't a confession of ignorance. Against an opponent who sees your choice, a pure strategy is exploitable. The mixture can't be pushed below one seventh, even by someone who knows it.

@chapter The cycle
@words text="(0 −1 1 / 1 0 −1 / −1 1 0)" sub="v = 0,  p = q = (1/3, 1/3, 1/3)"
The three by three cycle, where each choice beats one and loses to one, has value zero. Both players mix a third, a third, a third. Against that, every row earns exactly zero. But each row on its own has a worst case of minus one.

@art cycle-triangle
So no single choice is punished by playing it once. What a single choice can't do is promise anything.

@chapter A saddle point
@math heading="A = (4 2 / 3 1)" items="best pure guarantee:  2@max of the row minimums;;least pure enforcement:  2@min of the column maximums;;v = 2,  p = (1, 0),  q = (0, 1)@both optimal"
Now take rows four, two and three, one. The max of the row minimums is two. The min of the column maximums is also two. They agree, so it's a saddle point. The value is two, and both optimal strategies are pure.

@art saddle
When that happens, mixing buys nothing at all. Don't over generalise the other way.

@chapter Where people slip
@list heading="Common slips" items="There's always a best single row@The first|Forcing v ≥ 0@The second|Reading a mixture as a plan for one play@The third"
The first slip is believing there's always a best single row. The second is restricting v to be non negative. Rows minus two, minus five and minus six, minus one are worth minus seven halves. And the third is reading a mixture as a plan for one play. It's a probability distribution, and the value is an expectation.

@end text="Solve both players' programmes"
You can edit a payoff table, solve both players' programmes, and check the value, on Learn. That's learn dot get er done dot I O.
