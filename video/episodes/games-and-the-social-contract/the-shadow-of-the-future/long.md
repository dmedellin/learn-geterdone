---
format: long
lesson: games-and-the-social-contract/the-shadow-of-the-future
title: How much must the future count before cooperation pays?
thumb: How much must tomorrow count?
---

@chapter Another round, maybe
@title text="The Shadow of the Future" sub="Games and the Social Contract" art=thumb
Cooperation is stable when the future counts for enough. And how much is enough can be computed from the four payoffs alone.

@words text="R = 3 · S = 0 · T = 5 · P = 1"
Take the standard payoffs: the reward three, the sucker's payoff zero, the temptation five, and the punishment one. After each round, the game goes on with probability delta.

@art fading-rounds
A payoff n rounds away is then worth delta to the power n times as much now. So the future still counts, but each later round counts a little less than the one before.

@chapter Summing the future
@math heading="Getting x every round" items="x · (1 + δ + δ² + …)@x times one plus delta;;1 + δ + δ² + … = 1 / (1 − δ)@one over one minus delta;;value = x / (1 − δ)@x over one minus delta"
Getting x every round is worth x times one plus delta plus delta squared, and so on. Multiply that sum by delta and subtract, and every term but the first cancels, so it equals one over one minus delta. The value of x every round is x over one minus delta.

@words text="Expected rounds = 1 / (1 − δ)"
Put x equal to one and the same sum gives the expected number of rounds: one over one minus delta.

@chapter Against a player who never forgives
@art grim-door
Grim cooperates until it's defected against once, and then defects forever. Meet Grim, and you can cooperate throughout, or defect and be punished for good.

@math heading="Cooperate against GRIM?" items="R / (1 − δ)  ≥  T + δ·P / (1 − δ)@cooperating throughout;;R  ≥  T·(1 − δ) + δ·P@clear the denominator;;δ·(T − P)  ≥  T − R@collect the terms;;δ  ≥  (T − R) / (T − P) = 2/4 = 1/2@one half"
Cooperating throughout earns R over one minus delta. Defecting at once earns T now, then P every later round. Clear the denominator and collect the terms in delta, and cooperation is at least as good when delta is at least T minus R over T minus P. With the standard payoffs, that's two over four, or one half.

@chapter Against a player who forgives
@art forgiving-echo
Tit for tat punishes only as long as you keep defecting. Defecting forever against it needs the same delta as against Grim. The other deviation is to defect once and go back to cooperating: T now, then S while tit for tat retaliates, then R afterwards.

@math heading="Defect once against TFT?" items="R + δ·R  ≥  T + δ·S@first two rounds;;δ·(R − S)  ≥  T − R@collect the terms;;δ  ≥  (T − R) / (R − S) = 2/3@two thirds"
Compare the first two rounds, since everything later is equal. Cooperating pays R plus delta R, and the deviation pays T plus delta S. Collect the terms, and cooperation holds when delta is at least T minus R over R minus S, which is two thirds.

@art two-thresholds
So the milder punishment needs the more patient player. A deviator who returns to cooperation loses only one round to the retaliation, so the shadow of the future has to be heavier.

@chapter Thirty against fourteen
@math heading="δ = 9/10" items="Cooperate vs GRIM:  3 / (1/10) = 30@thirty;;Defect at once:  5 + 9 = 14@fourteen;;9/10 clears 1/2 and 2/3@cooperation is stable"
Now set delta at nine tenths. Cooperating for good against Grim is worth three over one tenth, which is thirty. Defecting at once is worth five plus nine, which is fourteen. Nine tenths clears both thresholds, so cooperation is stable.

@math heading="δ = 1/4" items="Cooperate:  4@four;;Defect at once:  about 5.33@about five point three three"
At a quarter, it reverses. Cooperating for good is worth four, and defecting at once is worth about five point three three. The future doesn't count enough.

@chapter The end that must not be known
@art unravel
Now suppose the game lasts exactly one hundred rounds, and both players know it. In round one hundred there's no later round to punish in, so defecting dominates. So in round ninety-nine, nothing changes round one hundred, and the same argument runs back to round one.

@words text="Half chance of another round: 2 rounds on average"
Compare a game that ends after each round with probability one half. It lasts two rounds on average, and with these payoffs it just sustains cooperation against Grim. What counts is an uncertain end, not a long game.

@chapter Where people slip
@list heading="Three slips" items="Cooperation needs a long game@a long game|Mild punishment works as easily as harsh@harsh one|The threshold predicts cooperation@a prediction"
First, thinking cooperation needs a long game, when it needs an uncertain end. Second, assuming a mild punishment sustains cooperation as easily as a harsh one. Third, reading the threshold as a prediction that players will cooperate.

@art scales
The threshold says cooperation is stable: nobody gains by deviating. But both players always defecting is also stable in the repeated game. So the threshold says what's possible, not what will happen.

@end text="Practice on Learn"
Change the payoffs and the continuation probability in the lab, and watch both thresholds move. It's on Learn. That's learn dot get er done dot I O.
