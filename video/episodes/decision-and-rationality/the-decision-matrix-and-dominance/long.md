---
format: long
lesson: decision-and-rationality/the-decision-matrix-and-dominance
title: The decision matrix: acts, states, and when one act dominates
thumb: Beaten everywhere, struck out
---

@chapter Acts and states
@title text="The Decision Matrix and Dominance" sub="Decision and Rationality" art=thumb
Should you take an umbrella? That's a decision with two acts and two states, and laying it out as a table is the first step in thinking about any choice.

@art acts-states-grid
An act is something you can choose. A state is a way the world might be that you don't control. And a payoff is how things go for you, if you choose that act and the world is in that state. The table has one cell for each pair.

@math heading="The umbrella" items="take:   rain 2,   dry 1@take the umbrella;;leave:  rain −3,  dry 3@leave it"
If you take the umbrella, you score two in rain, and one when it's dry. If you leave it, minus three in rain, and three when it's dry. The numbers are yours to choose. They stand for how good each case is. Whether a soaking is worth minus three is up to you. The table only says what follows if it is.

@chapter Dominance
@words text="a dominates b" sub="at least as good in every state, better in at least one"
Here's the one rule that needs nothing but the table. Act a dominates act b when a pays at least as much as b in every state, and strictly more in at least one. A dominated act can be removed without loss. And if one act dominates all the others, it's the choice.

@art column-compare
The umbrella table has no dominance. Take beats leave in rain, two to minus three. Leave beats take when it's dry, three to one. Neither act is at least as good in both columns, so dominance picks nothing.

@chapter Adding a worse act
@math heading="Add a coat" items="take vs coat:  rain 2 > 1,  dry 1 > 0@Compare take against coat;;take dominates coat@take dominates;;left: take, leave@take and leave"
Now add a third act, take a coat, paying one in rain and zero when dry. Compare take against coat, column by column. Two beats one in rain, and one beats zero when dry. So take dominates the coat, and the coat is struck out. What's left is take and leave, and neither dominates the other.

@art strike-out
The coat went, and the decision didn't get any easier. That's the usual shape of dominance reasoning. It removes the plainly bad acts, and leaves the real question where it was. And since dominance is transitive, the order you strike acts in doesn't matter.

@chapter Ties count
@math heading="The weak version" items="take:   rain 2,  dry 1@Take pays;;leave:  rain 2,  dry 0@leave pays"
This is the weak definition, and it matters. Suppose take pays two and one, and leave pays two and zero. They tie in rain, and take wins when it's dry. So take dominates leave, even though it isn't better everywhere. A strict version would leave this table undecided.

@art tie-column
So equal payoffs in a column are no reason to keep the weaker act. A tie in rain, and a win in the dry, is enough. Take is the choice, and leave is dropped.

@chapter The best cell isn't the test
@art best-cell
Leaving the umbrella has the highest cell in the table, a three. But that cell sits in only one column, and the same act has the lowest cell, minus three, in the other. One cell doesn't rank an act. Dominance asks about each column in turn.

@chapter A condition on using it
@art exam-state
There's one condition on using dominance, and it's easy to break. The states mustn't depend on the act. If you reason that you'll pass the exam whether or not you study, and then skip the revision, you've treated passing as a state, when it's partly an outcome of the act.

@chapter Where people slip
@list heading="Common slips" items="Choosing the act with the best possible outcome@The first|Dropping an act that does well in the likely state@The second|Keeping both acts because of a tie@the third"
The first slip is choosing the act with the best possible outcome. The second is dropping an act just because another does well in the likely state. Dominance doesn't weigh states, so it can't say one column matters more. And the third is treating a tie as a reason to keep both acts. A tie in one state and a win in another is dominance.

@chapter Try it
@math heading="Which dominates?" items="X:  5, 5@X pays;;Y:  4, 6@Y pays;;Z:  5, 4@Z pays"
Here's one to try. Three acts, two states. X pays five and five. Y pays four and six. Z pays five and four. Compare each pair column by column, and find the one dominance that holds.

@end text="Strike the dominated acts"
You can build your own tables and watch dominated acts drop out, on Learn. That's learn dot get er done dot I O.
