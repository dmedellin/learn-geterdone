---
format: long
lesson: games-and-the-social-contract/nash-equilibrium-in-pure-and-mixed-strategies
title: Nash equilibrium, and how to solve for a mixed strategy
thumb: Nine times in ten, swerve
---

@chapter What an equilibrium is
@title text="Nash Equilibrium in Pure and Mixed Strategies" sub="Games and the Social Contract" art=thumb
When is a pair of choices stable? When neither player would change their mind, given what the other is doing. That's a Nash equilibrium, and some games have several, while some seem to have none.

@words text="Nash equilibrium" sub="no player gains by changing alone"
A combination of strategies is a Nash equilibrium when no player can get a larger payoff by changing their own strategy while the others keep theirs. A pure equilibrium is a cell of the table. A mixed equilibrium gives each player a probability for each strategy.

@chapter Chicken
@art narrow-road
Chicken has two pure equilibria. Two drivers head for each other on a narrow road, and each can swerve or go straight. If both swerve, nothing's lost. If one swerves and the other doesn't, the swerver gets minus one and the other gets one. If neither swerves, they crash, and each gets minus ten.

@math heading="Chicken" items="Swerve, Swerve:  0, 0@In the table;;Swerve, Straight:  −1, 1@exactly one driver swerves;;Straight, Straight:  −10, −10@minus ten by going straight"
In the table, the cells where exactly one driver swerves are equilibria. The driver going straight gets one, and would get zero by swerving. The one who swerved gets minus one, and would get minus ten by going straight.

@art pure-cells
So chicken has two pure equilibria, one for each driver getting to go straight. Check any cell the same way: ask of each player, in turn, whether switching alone would pay. If neither would, the cell is an equilibrium.

@art nobody-hurt
And swerve, swerve isn't an equilibrium, because either driver gains by going straight. It's the one cell where nobody's hurt, and equilibrium doesn't choose it. Equilibrium describes stability, not merit.

@chapter When no cell qualifies
@art matching-pennies
Matching pennies is the opposite case. No cell is an equilibrium, because in every cell the player who loses the match would rather have chosen the other side. Nash's theorem says every game with finitely many strategies has an equilibrium, if mixed strategies are allowed. That's stated here, not proved.

@chapter Solving for the mix
@math heading="Column swerves with probability q" items="row swerves:  0 · q − 1 · (1 − q) = q − 1@swerving;;row straight:  1 · q − 10 · (1 − q) = 11q − 10@going straight;;q − 1 = 11q − 10@equal;;q = 9/10@nine tenths"
Let the column player swerve with probability q. The row player's expected payoff from swerving is q minus one. From going straight, it's eleven q minus ten. A row player who mixes must be indifferent between the two, so set them equal. Ten q is nine, and q is nine tenths.

@art crash-chance
So the column player swerves nine times in ten, and by symmetry the row player does too. At that pair of mixes, each driver expects minus a tenth, below the zero they'd get if both simply swerved. And they crash one time in a hundred. It's a true equilibrium, and it's worse for both than the cell it doesn't use.

@chapter Whose numbers fix whose mix
@art indifference-balance
Here's the surprise. Each player's probability is chosen so that the other is indifferent. The column driver's nine tenths comes from the row driver's payoffs. A player doesn't randomise to keep the opponent guessing. They randomise because, at that mix, the opponent has no better strategy to move to.

@words text="Crash at −100?" sub="the drivers swerve more often"
And the mix depends on the numbers. This is the textbook version, with a crash costing ten. Make a crash cost a hundred, and the drivers swerve more often.

@chapter Where people slip
@list heading="Common slips" items="Taking an equilibrium to be the best outcome@The first|Reading a mix as keeping the opponent guessing@The second|Expecting one equilibrium per game@the third"
The first slip is taking an equilibrium to be the best outcome for the group. The second is reading a player's mix as a way of keeping the opponent guessing. The weights are fixed by the opponent's payoffs, not your own. And the third is expecting one equilibrium per game. Chicken has two pure equilibria and a mixed one, and the table alone doesn't say which will be played.

@chapter Try it
@list heading="The method" items="List the doubly marked cells@doubly marked|Let the column play its first strategy with probability q@probability q|Set the row's two payoffs equal and solve@set them equal|Swap roles for the row's probability@swap the roles"
Here's the method to practise. List the doubly marked cells. Let the column player play its first strategy with probability q. Write the row player's two payoffs, set them equal, and solve for q. Then swap the roles to find the row player's probability.

@end text="Find the pure cells and the mix"
You can change the payoffs and watch the mix move, on Learn. That's learn dot get er done dot I O.
