---
format: long
lesson: accelerate-measuring-performance/high-medium-and-low-performers
title: How Accelerate found high, medium and low performers
thumb: The method doesn't know what's good
---

@chapter From measures to groups
@title text="High, Medium and Low Performers" sub="Accelerate, Chapter 2 and Appendix C" art=thumb
You've got four measures of delivery. How do you get from those to high, medium and low performers? The authors' answer is a method that doesn't know which answers are good.

@art cluster-points
It's called cluster analysis. It sorts responses into groups whose members resemble one another more than anyone outside. The four answers are four axes, and the method sees only how far apart responses lie. That lets the groups emerge without a prior view of what good looks like.

@chapter Choosing the method
@list heading="Appendix C: how they chose" items="Five hierarchical methods tried@five hierarchical|Ward's gave the best solution@Ward's|No theory of how many groups@no theory"
Appendix C gives the method. They tried five hierarchical methods and compared the solutions, setting aside ones with tiny clusters. Ward's method gave the best. They chose a hierarchical method because it shows how clusters join, because they had no theory about how many groups to expect, and because the dataset wasn't too large for it.

@chapter What they found
@art four-axes-groups
For each of the four years, they report significantly different categories of delivery performance. All four measures were good classifiers, and the high, medium and low groups differed significantly on every one.

@list heading="2017, in the book's words" items="High: deploy on demand@on demand|High: lead time and restore under an hour@under an hour|High: change fail rate 0–15%@zero to fifteen|Low: change fail rate 31–45%@thirty one to forty five"
In twenty seventeen, high performers deploy on demand, with lead times and times to restore under an hour, and change fail rates of zero to fifteen percent. Low performers deploy between once a week and once a month, take between a day and a week to restore, and fail thirty one to forty five percent of changes.

@quote text="Astonishingly, these results demonstrate that there is no tradeoff between improving performance and achieving higher levels of stability and quality" cite="Forsgren, Humble and Kim, Accelerate, Chapter 2"
Then the headline. Astonishingly, these results demonstrate that there is no tradeoff between improving performance and achieving higher levels of stability and quality.

@words text="A description of the groups" sub="why comes in later chapters"
Read it for what it says. In their survey, the groups that are quick are also the groups that recover quickly and fail less. It's a description of the groups. Why, the authors take up later.

@chapter Moving groups and a surprise
@art moving-groups
The groups aren't fixed. High performers in twenty seventeen held or improved on twenty sixteen. Low performers began to speed up in twenty seventeen, but lost ground on stability, which the authors suspect comes from pushing harder without fixing what's in the way. The clusters are redrawn from each year's data.

@art surprise-box
And one box, headed Surprise, is the honest part. In twenty sixteen the medium performers did worse than the low performers on change fail rate. The research doesn't explain it conclusively. The authors suggest large rearchitecture work, and the lesson claims no more for it.

@chapter Ward's method by hand
@math heading="Each merge costs" items="cost = a·b / (a + b) × (distance between centres)²@a times b;;two single teams: ½ × squared distance@two single teams"
Code each team's four answers from one, the best option, to six. Then, at each step merge the two groups whose merger raises the within group sum of squares least. For groups of sizes a and b that's a times b over a plus b, times the squared distance between their centres. For two single teams, it's half their squared distance.

@art ward-merge
So the cost grows with how far apart the two centres are, and with how big both groups are. Near neighbours join cheaply. Unlike groups cost a lot.

@math heading="The first two merges" items="T01 (1,1,2,2) to T03 (1,1,2,1): 0+0+0+1 = 1@T zero one;;T01 + T03 merge at ½@merge at one half;;centre (1,1,2,1.5); T04 (1,1,1,2): 1 + 0.25 = 1.25@one point two five;;T04 joins at (2·1/3) × 1.25 = 5/6@five sixths"
Take ten invented teams. T zero one and T zero three differ by one on one measure, a squared distance of one, so they merge at one half. Their centre is one, one, two, one and a half. T zero four is one point two five away, and joins at two times one over three, times one point two five: five sixths.

@art merge-tree
That cost is the fusion coefficient. The nine merges cost from one half up to sixty three. Three groups remain after a merge costing twenty three sixths, and the next would cost twenty five halves. The jump is where to consider stopping.

@math heading="Three groups: median codes" items="G1 (T01–T04): 1, 1, 2, 2@G one;;G2 (T05–T07): 3, 3, 3, 3@G two;;G3 (T08–T10): 5, 5, 5, 4@G three"
G one has medians one, one, two, two: on demand, under an hour, restoring within a day, and sixteen to thirty percent. G two is three on everything. G three is five, five, five, four. Whether to call a group high is for you to read from the medians. The lab doesn't know.

@chapter Where people slip
@list heading="Common slips" items="The method finds the high performers@The first|No trade-off means speed causes stability@The second|Groups are fixed bands@the third"
The first slip is thinking the clustering tells you which group is high performing. We decide that by reading the medians. The second is reading no tradeoff as proof that speed causes stability. And the third is treating the groups as fixed bands, when they're drawn afresh each year.

@chapter Try it
@words text="Quay 1,1,1,2 · Ridge 1,2,1,2 · Shoal 4,4,3,3 · Tarn 5,4,3,4"
Your turn. Four teams: Quay, Ridge, Shoal and Tarn. Find the squared distance between each pair, then the first merge and its cost, then the two groups. Then change Tarn to match Quay, and say what happens to the merges.

@end text="Cluster the teams yourself"
You can cluster ten teams and watch every merge, on Learn. That's learn dot get er done dot I O.
