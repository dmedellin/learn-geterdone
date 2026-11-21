---
format: long
lesson: games-and-the-social-contract/repeated-games-and-reciprocity
title: Tit for tat never wins a match. So how does it win the tournament?
thumb: Never wins a match, nearly wins it all
---

@chapter Playing again
@title text="Repeated Games and Reciprocity" sub="Games and the Social Contract" art=thumb
Play the prisoner's dilemma once, and defecting wins. But play it again and again, and something changes. Strategies that answer in kind start to score.

@words text="R = 3 · S = 0 · T = 5 · P = 1"
Here are the same four payoffs as before: the reward three, the sucker's payoff zero, the temptation five, and the punishment one. Now they're played over many rounds, and each player's score is the sum of what the rounds paid.

@art history-rule
In a repeated game, a strategy isn't a single move. It's a rule that gives a move for every possible history of play. It can depend on what the other player has done, on what you've done, and on how many rounds have passed.

@chapter Seven rules
@list heading="Seven strategies" items="ALLC and ALLD: always cooperate, always defect@always cooperates|TFT: cooperate, then copy their last move@Tit for tat|GRIM: cooperate until defected on once@Grim|PAVLOV: repeat if last round paid well@Pavlov|TF2T: defect only after two defections@Tit for two tats|STFT: tit for tat, opening with defect@Suspicious tit for tat"
Here are seven. One always cooperates, and one always defects. Tit for tat cooperates first, then copies the other's last move. Grim cooperates until defected on once, then defects forever. Pavlov cooperates first, then repeats its move if the last round paid the reward or the temptation, and switches otherwise. Tit for two tats defects only after two defections in a row. Suspicious tit for tat is tit for tat with a defection in round one.

@chapter Tit for tat against always defect
@math heading="Ten rounds" items="round 1:  TFT C, ALLD D  →  0 and 5@In the first round;;rounds 2 to 10:  both D  →  9 and 9@From then on;;TFT 9,  ALLD 14@nine for tit for tat"
Take tit for tat against always defect, for ten rounds. In the first round, tit for tat cooperates and always defect defects, so the scores are zero and five. From then on, tit for tat copies the defection, and both defect for nine rounds, one point each. Nine for tit for tat, fourteen for always defect.

@art never-ahead
Tit for tat lost. And it can never do better than tie any match. It defects only after being defected against, so it can't outscore its partner. Always defect is the reverse. It scores at least as much as its partner in every match. So it looks like the strategy to beat.

@chapter The round robin
@art seven-players
Picture the whole field at once. Seven rules, and each one plays every other rule for ten rounds, and itself too. A rule's score is its total over all seven partners.

@math heading="Round robin, ten rounds" items="TF2T:  185@one hundred and eighty five;;TFT:  184@a hundred and eighty four;;ALLD:  146@a hundred and forty six"
The round robin refutes that. Every strategy meets every strategy, itself included. Always defect takes fifty from always cooperate, but only fourteen from tit for tat and from grim, and ten from itself. Over the whole field, tit for two tats scores one hundred and eighty five, tit for tat a hundred and eighty four, and always defect a hundred and forty six.

@art cooperators-pile
Here's why. Tit for tat, grim, Pavlov, always cooperate and tit for two tats cooperate all ten rounds with one another, and take thirty each time. Mutual defection earns only ten a match. A tournament adds points across partners. It doesn't count victories.

@art silent-reciprocity
And notice tit for tat against itself. It cooperates throughout, and each side scores thirty. So do grim and Pavlov against each other, because neither is ever defected against, so neither ever has cause to respond. Reciprocity is a rule that's silent when met by cooperation. That's why it costs nothing against a cooperator.

@chapter Two limits
@art shifting-ranks
Two limits belong here. The field is seven rules chosen for the lab, and a different field would rank them differently. And at ten rounds the winner is only one point ahead. At one round, always defect and suspicious tit for tat win. At five, tit for two tats. At eight, tit for tat and tit for two tats tie.

@chapter Where people slip
@list heading="Common slips" items="Thinking the strategy that beats everyone wins@The first|Reading the winner as the best strategy@The second|Treating reciprocity as a feeling@the third"
The first slip is thinking the strategy that beats every opponent wins the tournament. Always defect does that, and finishes sixth of seven. The second is reading the winner as the best strategy in general. It's the best of these seven, against these seven, at this number of rounds. And the third is treating reciprocity as a feeling. Tit for tat is a rule with no attitude in it: copy the last move.

@end text="Pick two strategies, run the field"
You can pick any two strategies, change the rounds, and run the round robin, on Learn. That's learn dot get er done dot I O.
