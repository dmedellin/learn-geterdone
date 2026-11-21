---
format: long
lesson: decision-and-rationality/maximin-maximax-and-minimax-regret
title: Maximin, maximax and minimax regret: choosing without probabilities
thumb: Same table, three verdicts
---

@chapter No idea how likely
@title text="Maximin, Maximax and Minimax Regret" sub="Decision and Rationality" art=thumb
Dominance left the umbrella undecided. And suppose you have no idea how likely rain is. You still have to choose. So you need a rule that turns each row of the table into one score.

@math heading="The umbrella" items="take:   rain 2,   dry 1@Take pays;;leave:  rain −3,  dry 3@leave pays"
Recall the table. Take pays two in rain and one when dry. Leave pays minus three and three. Here are three rules, and they won't all agree.

@chapter Maximin and maximax
@art worst-case
Maximin is the pessimist's rule. Score each act by its worst payoff, and choose the act whose worst is best. Take's worst is one. Leave's worst is minus three. So maximin takes the umbrella.

@art best-case
Maximax is the optimist's rule. Score each act by its best payoff, and choose the highest. Take's best is two. Leave's best is three. So maximax leaves the umbrella at home.

@chapter Minimax regret
@math heading="The regret table" items="take:   rain 0,  dry 2@take regrets;;leave:  rain 5,  dry 0@leave regrets"
The third rule needs a new table. In each column, subtract every payoff from the column's best. In rain, the best is two, from take. So take regrets nothing, and leave regrets two minus minus three, which is five. When it's dry, the best is three, from leave. So leave regrets nothing, and take regrets three minus one, which is two.

@art regret-gap
Now score each act by its largest regret, and choose the smallest. Take's worst regret is two. Leave's is five. So minimax regret also takes the umbrella. Two rules say take, and one says leave.

@chapter Where they part
@math heading="Safe or bold?" items="safe:  3, 3@safe act;;bold:  2, 10@bold act;;maximin:  safe (3 against 2)@Maximin takes;;worst regret:  safe 7, bold 1:  bold@regrets seven"
Here's a table where maximin and minimax regret part. A safe act pays three in a weak market and three in a strong one. A bold act pays two and ten. Maximin takes the safe act, whose worst is three against two. But the safe act regrets seven in the strong market, while the bold act regrets at most one. So minimax regret takes the bold act.

@art two-temperaments
So a decision maker who dreads having acted unwisely will take bold. One who dreads the worst outcome will take safe. Neither is confused. They're answering different questions about the same table.

@chapter Regret is relative
@math heading="Add 10 to the rain column" items="regret table:  unchanged, picks take@regret table is unchanged;;maximin:  take's worst 1, leave's worst 3:  leave@maximin switches"
Minimax regret is maximin applied to a different table, and that table is relative. Each column is measured from its own best. So anything every act shares in a state drops out. Add a bonus of ten to the rain column for both acts. The regret table is unchanged, and still picks take. But take's worst is now one, and leave's worst is three, so maximin switches to leave.

@art shared-bonus
That's the real difference between the rules. Regret is blind to a gain every act shares. Maximin reads the raw payoffs, so a shared gain can change its verdict.

@chapter Attitudes, not answers
@list heading="What each rule encodes" items="Maximin: plan for the worst state@Maximin says|Maximax: plan for the best state@maximax|Minimax regret: avoid choosing worse than the state allowed@minimax regret"
None of the three is the right rule. Each encodes an attitude. Maximin says the worst state is the one to plan for. Maximax says the best state is. And minimax regret says the thing to avoid is having chosen worse than the state allowed. Which attitude to hold is up to you.

@art three-dials
Think of them as three dials reading the same table. Each one is exact about what it measures: the worst, the best, the biggest shortfall. A choice defended by one of them is really defended by the attitude it carries, so say which attitude you're relying on.

@chapter Where people slip
@list heading="Common slips" items="Treating regret as just maximin again@The first|Reading a rule's verdict as the verdict@The second|Using these rules when the odds are known@the third"
The first slip is treating minimax regret as maximin on a different table, and stopping there. The table is relative, and that changes answers. The second is reading a rule's verdict as the verdict. And the third is using these rules when the probabilities are in fact known. If rain has a one in a thousand chance, planning only for it throws away what you know.

@chapter Try it
@words text="Min · max · regret · compare"
Here's one to try. Take any table. Write each row's minimum and maximum. Build the regret table. Score the regret rows by their largest entry. If all three rules agree, the choice doesn't depend on attitude. If not, say which state is driving each.

@end text="One table, three rules"
You can switch between the three rules on the same table, on Learn. That's learn dot get er done dot I O.
