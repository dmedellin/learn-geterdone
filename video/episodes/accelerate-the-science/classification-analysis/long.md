---
format: long
lesson: accelerate-the-science/classification-analysis
title: How Accelerate found high, medium and low performers
thumb: Where the merges jump
---

@chapter Where the groups came from
@title text="Classification Analysis" sub="Accelerate, Chapter 12" art=thumb
The most quoted result in Accelerate is that there are high, medium and low performers. Where did those groups come from? Chapter twelve describes the method in one line.

@quote text="classification variables are entered into the clustering algorithm and significant groups are identified." cite="Forsgren, Humble and Kim, Accelerate, Chapter 12"
Classification variables are entered into the clustering algorithm and significant groups are identified. Chapter two reports the groups. This lesson reads the method.

@chapter Off the ladder
@art four-measures
Classification isn't one of Leek's six rungs, and the authors say so. Depending on the design, it may count as exploratory, predictive or even causal. They used it to see whether teams differed in how they built and delivered software, feeding in their four delivery measures and looking at the groups that emerged.

@list heading="The groups, as the authors report them" items="High: better on all four measures@better|Low: worse on all four@worse|Medium: in between@between"
The groups differ distinctly and with statistical significance. The high group is better than the others on every one of the four measures, the low group worse on every one, and the medium group in between.

@chapter Points in space
@art point-cloud
Each measure is a dimension, so each team is a point in four dimensional space. The algorithm looks for points near each other and far from the rest. And as chapter two adds, it has no idea what a good or bad answer is. The names high, medium and low are the researchers' reading afterwards.

@list heading="Why hierarchical, not k-means" items="No prior idea how many groups@no theory|Parent and child groups@parent and child|A dataset small enough@not so large"
Why hierarchical clustering over k means? K means needs the number of groups chosen first, and they had no theory of how many there should be. Hierarchical clustering shows parent and child groups, which helps interpretation. And their dataset was not so large that the computing cost mattered.

@chapter Ward's method
@art merge-tree
Appendix C says they ran five methods and Ward's performed best. Start with every team alone. Merge the two groups whose joining raises the total within group spread the least. That rise is the fusion coefficient. Repeat until one group is left.

@math heading="Ward's merge cost (stated by the lab)" items="cost(A, B) = nA·nB ÷ (nA + nB) · Σ(a − b)²@n A times n B;;T1 = (6,6,6,6), T5 = (6,6,5,6): distance² = 1@squared distance of one;;cost = 1·1 ÷ 2 · 1 = 1/2@one half"
The cost is n A times n B over their sum, times the squared distance between the two groups' averages. The book doesn't print it, so the lab states it. Nine invented teams are coded one to six on the four measures. T one and T five differ by one on a single measure: a squared distance of one, so the cost is one half.

@chapter Where to stop
@art cost-steps
Read the merge costs in order. Cheap merges join teams that are already alike. A sudden expensive one joins groups that aren't.

@math heading="Preset three-groups: the eight merge costs" items="1/2, 1, 3/2, 2, 3, 10/3@ten thirds;;then 67/3 ≈ 22.33@sixty seven thirds;;then 81@eighty one"
The costs never decrease. The first six merges, which leave three groups, cost ten thirds at most, about three point three three. The seventh would cost sixty seven thirds, about twenty two point three three. Then eighty one. A jump from about three to about twenty two says going to two groups forces together teams that aren't alike.

@art three-clusters
So the data gives three groups. The first has medians that read as on demand deploys and under an hour of lead time. The second reads far worse on every measure, and the third sits in between. A researcher would call them high, low and medium, and the researcher is doing the naming, not the algorithm.

@art lonely-one
Ask for four groups instead, and team T seven splits off alone, leaving a group of one. The authors excluded solutions with very small clusters, and this is why.

@words text="Equal steps are assumed · no cut is the true one" sub="the lesson's reservations"
Two reservations are the lesson's own. The distance treats the codes as equal steps, which six answer options only suggest. And a tree of merges always ends in one group. The costs help you choose where to cut, and no cut is the true one.

@chapter Where people slip
@list heading="Common slips" items="The algorithm knows good from bad@good from bad|Choose the number of groups first@first|The lab's groups are the book's finding@book's finding"
Three slips. Thinking the algorithm knows good from bad. Choosing the number of groups first, which is just what the authors avoided. And treating the lab's three invented groups as the book's finding.

@chapter Try it
@words text="A 1,1,1,1 · B 2,1,1,1 · C 5,5,5,4 · D 6,6,5,6"
Your turn. Four invented teams. A is one, one, one, one. B is two, one, one, one. C is five, five, five, four. D is six, six, five, six. Work out the three merges and their costs, and say what the last cost tells you.

@end text="Let the merges tell you where to stop"
Then ask the lab for two groups, on Learn. That's learn dot get er done dot I O.
