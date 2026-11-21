---
format: long
lesson: dynamic-programming-and-sequential-decisions/the-state-is-what-is-left
title: The state is what is left: allocation by dynamic programming
thumb: Greedy loses by six
---

@chapter Nobody hands you the stages
@title text="The State Is What Is Left" sub="Dynamic Programming and Sequential Decisions" art=thumb
Last time the network was given to you. This time all you get is a table, and before you can solve anything, you have to invent the network yourself.

@art unit-blocks
Here's the problem. You have a whole number of indivisible units to hand out across some activities. A table says what each activity returns for zero units, one unit, two, and so on. You want the split with the biggest total return.

@chapter The state
@words text="State = units still unspent" sub="when this activity decides"
The invention is the state. Before each activity decides, what does the future need to know? Only how many units are still unspent. Not who took what. Just one number.

@math heading="The value function" items="g(n+1, s) = 0@no activities left;;g(i, s) = max over x = 0..s of  rᵢ(x) + g(i+1, s − x)@take x units"
Once there are no activities left, whatever remains is worth nothing, so that value is zero. Otherwise, activity i with s units left can take x units, anywhere from zero to s. It earns r i of x, and passes s minus x on to the next activity. Take the best x.

@words text="rᵢ(0) = 0" sub="a return for nothing must be nothing"
One rule about the table: every activity must return zero for zero units. A first column that isn't zero is measuring something other than a return.

@chapter The network it forces
@words text="P: 0 2 4 15 16 · Q: 0 6 8 9 10 · R: 0 3 7 8 9" sub="returns for 0 to 4 units"
Here's the lesson's table. P returns zero, two, four, fifteen and sixteen for zero to four units. Q returns zero, six, eight, nine and ten. R returns zero, three, seven, eight and nine. You have four units.

@art state-grid
Now build the network. One stage per activity, plus a finish. In each stage, one node for each amount that could still be unspent, zero to four. An arc from s left to s minus x left carries the return of x units. Five nodes, four stages: twenty state values.

@art best-route
Fill it from the finish back, and the value at four left in P's stage is twenty one. P takes three, Q takes one, and R takes none.

@math heading="Check it" items="15 + 6 + 0 = 21@fifteen plus six;;35 splits priced, 21 is the best@thirty five"
That's fifteen plus six plus zero, twenty one. The lab also prices all thirty five ways to split four units across three activities, and finds twenty one, from exactly that split and no other.

@chapter The rule that looks at the next unit
@math heading="One unit at a time" items="1st unit → Q, gain 6@the first;;2nd → R, gain 3@the second;;3rd → R, gain 4@the third;;4th: tie at gain 2;; total 15@fifteen"
Now try the obvious shortcut. Hand out units one at a time, each to whoever gains most from the next one. The first goes to Q, gaining six. The second goes to R, gaining three. The third goes to R again, gaining four. The fourth is a tie at two. Total: fifteen.

@art jump-staircase
Every comparison was right, and the answer is six short. Why? P's first two units gain two each, but its third gains eleven. A rule that only asks about the next unit never sees that eleven. The recursion does, because it asks how much P should take, and three is one of the options.

@art greedy-steps
So it isn't an approximation. It's solving a different problem exactly: the plans you can reach one unit at a time, never revisiting. That set leaves out every plan that pays for two poor units to reach a good third.

@chapter Ties, and what the state leaves out
@art two-splits
When every activity has diminishing returns, the shortcut stops losing, and both reach nineteen in the lesson's second example. But two splits reach it. One, two, one, and two, one, one. Even the friendly case has a set of answers.

@list heading="What this model rules out" items="Activities that affect each other@affect each other|Splitting a unit@split a unit|Forbidden combinations@forbidden|Set-up costs@set up costs"
And the state makes a claim. Activities can't affect each other. You can't split a unit. No combination is forbidden, and there are no set up costs. If any of those is true, the recursion still gives an exact optimum, of the wrong problem.

@chapter Try it
@words text="P: 0 7 11 14 15 · Q: 0 5 10 13 16" sub="four units, two activities"
Your turn, with two activities. P returns zero, seven, eleven, fourteen, fifteen. Q returns zero, five, ten, thirteen, sixteen. Split four units. There are only fifteen splits, so check every one by hand. You should find two and two, for twenty one.

@end text="Build the network from a table"
You can type in your own return table and watch the state grid fill, on Learn. That's learn dot get er done dot I O.
