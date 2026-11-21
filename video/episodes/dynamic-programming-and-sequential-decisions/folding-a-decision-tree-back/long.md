---
format: long
lesson: dynamic-programming-and-sequential-decisions/folding-a-decision-tree-back
title: Decision trees, EVPI and EVSI: what is information worth?
thumb: Price it before you buy
---

@chapter The question
@title text="Folding a Decision Tree Back" sub="Dynamic Programming and Sequential Decisions" art=thumb
You have a decision to make and you don't know how things will turn out. Someone offers to sell you a survey first. How much should you pay for it? A decision tree can tell you, before you buy.

@art two-node-kinds
A tree has two kinds of node. A chance node is an average of its branches, weighted by their probabilities. A decision node is the largest of its branches, and it remembers which one.

@art fold-back
Folding the tree back is the same recursion as before. Work from the leaves to the root, and write each value only once everything below it is settled. The branch each decision node remembers is the plan.

@chapter Two values
@math heading="Prior and perfect information" items="prior value = max over a of Σₛ p(s) π(a,s)@decide now;;perfect = Σₛ p(s) max over a of π(a,s)@know the state;;EVPI = perfect − prior@the difference"
Decide now, and you take the act with the best expected payoff on the prior. If you could know the state first, you'd pick the best act in each state, then average. The difference is the expected value of perfect information, EVPI.

@art perfect-info
That second value has the maximum inside the average. Last lesson that swap was a mistake. Here it's the point. It describes a better informed decision maker, and it's a ceiling: no signal can be worth more.

@chapter A signal worth nothing
@math heading="go / stop · prior ½ up, ½ down" items="go:  ½·60 + ½·(−40) = 10@go is worth;;perfect:  ½·60 + ½·0 = 30@thirty;;EVPI = 30 − 10 = 20@twenty"
Here's the lesson's first example. Go pays sixty if things go up and loses forty if they go down. Stop pays nothing. With even odds, go is worth ten. Knowing the state first is worth thirty. So EVPI is twenty.

@art useless-signal
Now a signal. Each reading is equally likely, one half, whether things are up or down. Work out the posteriors and they come out equal to the prior. After either reading you still go, still worth ten. So the value of this sample information, EVSI, is ten minus ten: zero.

@words text="EVPI 20 · EVSI 0"
Twenty and nothing. The signal looks respectable, but its two rows are identical, so it can't tell the states apart. A signal has to discriminate to be worth anything.

@chapter A survey worth buying
@math heading="Build or wait · prior 3/10 good" items="build:  0.3·100 − 0.7·20 = 16@sixteen;;perfect: 30,  EVPI = 14@fourteen"
Second example. Building returns a hundred if things turn out good, and loses twenty if not. Waiting returns nothing. The prior is three tenths good, so building is worth sixteen. Perfect information is worth thirty, so EVPI is fourteen.

@math heading="The survey" items="P(favourable) = 83/200,  P(good | fav) = 48/83 → build@favourable;;P(unfavourable) = 117/200,  P(good | unfav) = 4/39 → wait@unfavourable;;with survey 41/2,  EVSI = 9/2@nine halves"
The survey is right four times in five when things are good, and three in four when not. A favourable reading has probability eighty three over two hundred, and leaves forty eight over eighty three good: build. An unfavourable one leaves four over thirty nine: wait. With it, the decision is worth forty one halves, so EVSI is nine halves.

@art signal-branches
That's what the survey buys: it changes what you do. Without it you always build. With it you build after good news and wait after bad. If both readings had left building best, EVSI would be zero, however much the posteriors moved.

@chapter Where people slip
@list heading="Common slips" items="Quoting EVPI as the survey's value@The first|Judging a signal by how far it moves the posterior@The second|Quoting EVSI exactly from a guessed prior@And the third"
The first slip is quoting EVPI as the survey's value. It's a ceiling, nobody's selling perfect information. The second is judging a signal by how far it moves the posterior. It's worth something only when it changes the act. And the third is quoting EVSI to the last fraction when the prior was a guess.

@art ceiling-bar
Every time, EVSI sits between zero and EVPI. Here nine halves is nine twenty eighths of fourteen. That ceiling is cheap: two weighted averages can rule out a purchase without any Bayes at all.

@chapter Try it
@words text="Move the prior from 3/10" sub="and watch EVSI move"
Your turn. Take the build or wait example and change the prior away from three tenths. Recompute EVSI, and find the prior where the survey stops changing what you do. Then quote a range, not a point, because the prior is usually somebody's judgement rather than a measurement.

@end text="Price information before you buy it"
You can build your own payoff table and watch EVPI and EVSI move, on Learn. That's learn dot get er done dot I O.
