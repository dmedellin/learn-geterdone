---
format: long
lesson: games-and-the-social-contract/the-prisoners-dilemma
title: The prisoner's dilemma: why trust doesn't fix it
thumb: Both defect, both lose
---

@chapter Two prisoners
@title text="The Prisoner's Dilemma" sub="Games and the Social Contract" art=thumb
Here's the most famous game in the whole subject, and the reason it matters.

@art two-cells
Two people are held separately, and can't talk to each other. Each is asked to stay silent, or to inform on the other. Each has a reason to inform that doesn't depend on the other at all. And if both follow it, both do worse.

@list heading="The four payoffs" items="R: reward, both cooperate@reward|T: temptation, defect on a cooperator@temptation|P: punishment, both defect@punishment|S: sucker's payoff@sucker's"
Write C for cooperating with the other prisoner, staying silent, and D for defecting, informing. The four payoffs have names. R is the reward when both cooperate. T is the temptation to defect against a cooperator. P is the punishment when both defect. And S is the sucker's payoff, cooperating against a defector.

@math heading="The standard numbers" items="C, C:  3, 3@the reward is three;;C, D:  0, 5  ·  D, C:  5, 0@the sucker's payoff zero;;D, D:  1, 1@the punishment one;;T > R > P > S:  5 > 3 > 1 > 0@temptation beats reward"
Here the reward is three, the sucker's payoff zero, the temptation five, and the punishment one. And the game is a prisoner's dilemma exactly when temptation beats reward, reward beats punishment, and punishment beats being the sucker. That ordering is the whole definition.

@chapter Defect dominates
@math heading="The row player" items="column cooperates:  D 5, C 3@If the column player cooperates;;column defects:  D 1, C 0@If the column player defects"
Take the row player. If the column player cooperates, defecting pays five and cooperating pays three. If the column player defects, defecting pays one and cooperating pays zero. Defecting is better in both cases.

@art dominance-arrows
So defecting strictly dominates cooperating. It pays more against every strategy the other might choose. The table is symmetric, so the same holds for the column player. And that settles the play without asking what either player believes. Each defects, and the cell reached is defect, defect.

@chapter The cell passed over
@art pareto-gap
Now compare the cell reached with the one passed over. Mutual cooperation gives each player three. Mutual defection gives each one. One cell Pareto dominates another when every player gets at least as much, and someone gets more. So the only equilibrium of this game is Pareto dominated.

@words text="Each has a reason. Together, the reasons defeat both."
That's the dilemma. Each has a reason that doesn't depend on the other, and the reasons together defeat both.

@art gap-unclosable
The shortfall is two each, and no one can close it alone. A player who moves to cooperate while the other holds defect doesn't climb toward three. They drop to zero.

@chapter It isn't about trust
@art trust-bites
It's tempting to think the dilemma comes from distrust, and would vanish between people who trust each other. It doesn't. A player who's certain the other will cooperate should still defect, because five beats three. The more you trust, the more the temptation bites.

@chapter What changes the game
@math heading="Change the payoffs" items="T = 4:  4 > 3 > 1 > 0,  still a dilemma@Lower the temptation;;R = 4, T = 3:  ordering broken@reward at four"
The dilemma needs the ordering and nothing else. Lower the temptation from five to four, and the ordering still holds, so defect still dominates. But set the reward at four and the temptation at three, and against a cooperator, cooperating now pays four where defecting pays three. The ordering is broken. Mutual cooperation becomes an equilibrium alongside mutual defection.

@art new-table
So what can dissolve the dilemma is a different table, one where the players value the outcomes differently. Talk, promises and reassurance change no payoff in this table. And whether real prisoners care about each other would be a different table too, with its own computation.

@chapter Where people slip
@list heading="Common slips" items="Thinking it comes from distrust@The first|Reading the equilibrium as the best the pair can do@The second|Treating defect as a verdict on the players@the third"
The first slip is thinking the dilemma comes from distrust. The second is reading the equilibrium as the best the pair can do. It's just the cell where each is best responding, and the cell passed over pays both more. And the third is treating defect as a verdict on the players. They're names for columns in a table. The argument takes no view on who's wicked.

@chapter Try it
@words text="Four checks" sub="dominance for row · for column · the cell · a better cell?"
Here's one to try. Take any two by two game. Check whether one strategy dominates for the row player, then for the column player. Name the cell they reach. Then look for a cell that pays both more. If there is one, you've found a dilemma.

@end text="Test the ordering"
You can change any payoff and see whether the dilemma survives, on Learn. That's learn dot get er done dot I O.
