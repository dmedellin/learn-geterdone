---
format: long
lesson: linear-programming-models/product-mix-and-resource-constraints
title: Product mix: what a tight resource does and doesn't tell you
thumb: Used up isn't worth more
---

@chapter The question
@title text="Product Mix and Packing Constraints" sub="Linear Programming Models" art=thumb
A workshop has limited hours in each shop, and several products competing for them. Which mix earns the most? And once you've found it, which resources did it use right up?

@words text="usage ≤ availability"
Every row in this kind of model says the same sentence. What the plan uses of one resource is at most what there is of it. That's a packing row.

@chapter Reading the table
@art rate-table
The data arrive as a table. Rates go down the columns, one column per product. Availabilities go down the right. And profit sits in the row underneath. The model is just a transcription of that table.

@math heading="The rate table" items="carpentry:  1·C + 0·T ≤ 4@carpentry;;finishing:  0·C + 2·T ≤ 12@finishing;;assembly:  3·C + 2·T ≤ 18@assembly;;profit:  3C + 5T@profit"
In carpentry, a chair takes one bench hour, a table none, and there are four. In finishing, a table takes two hours, out of twelve. On assembly, a chair takes three and a table two, out of eighteen. And profit is three per chair and five per table.

@art transposed
Notice that each row belongs to a resource, not to a product. Three shops give three rows, not nine. Read the table across instead of down and you get a different model. It builds, it solves, and it answers a question nobody asked.

@chapter Slack
@art slack-gap
Picture a resource as a bar. The plan fills part of it. Whatever's left over is the slack.

@math heading="Slack" items="slack = b − a·x@b minus;;tight  ⇔  slack = 0@zero"
The gap a row leaves at a point is its slack: the availability, b, minus the usage. It's zero or more exactly where the row holds. And when it's exactly zero, the row is tight.

@math heading="At (2, 6), profit 36" items="carpentry:  4 − 2 = 2 bench hours@two bench hours;;finishing:  12 − 12 = 0@finishing;;assembly:  18 − 18 = 0@assembly"
The best plan is two chairs and six tables, worth thirty six. At that point, carpentry has two bench hours left. Finishing has none left, and assembly has none left. Two rows used right up, which is usual. A two variable optimum sits where two boundaries cross.

@art two-boundaries
And slack isn't a score or a percentage. It's measured in the resource's own unit. The same optimum has a slack in hours for each row, each a different kind of hour.

@chapter A third product
@words text="Bench: 1 · 1 · 2 hours, earns 4" sub="optimum 75/2 at (1, 9/2, 3)"
Now let the workshop make benches too. One bench hour, one finishing hour and two assembly hours each, earning four. The optimum becomes seventy five halves, at one chair, nine halves tables and three benches, with all three rows tight.

@art no-picture
Two things changed. The answer is a fraction. And there's no picture any more, because three decisions can't be drawn on a plane. So the lab hands it to the exact simplex. Pin benches at zero and it returns thirty six again. The two methods agree.

@chapter Tight isn't a bottleneck
@math heading="Assembly up to 24" items="optimum (4, 6), profit 42@forty two;;4 ≤ 4,  12 ≤ 12,  24 ≤ 24@all three rows;;+1 assembly hour → 42@twenty fifth;;+1 bench hour → 42@a bench hour;;+2 finishing hours → 45@forty five"
Push assembly to twenty four hours. The optimum moves to four and six, earning forty two, and all three rows are tight. Add a twenty fifth assembly hour, still forty two. Add a bench hour, still forty two. Add two finishing hours, and it's forty five.

@art three-tight
Three resources exhausted, and only one of them worth paying for. What separates them is a shadow price, which comes later in the course. For now, the honest report is this: a tight row says a resource was used up. It says nothing about what relieving it would be worth.

@chapter Where people slip
@list heading="Common slips" items="Reading tight as a bottleneck@The first|One row per product@The second|Dropping a row with slack@The third"
The first slip is reading a tight row as a bottleneck worth relieving. The second is writing one row per product instead of one per resource. The usual symptom is coefficients that all look like profits. The third is deleting a row because it has slack. Move a profit or an availability, and that row can become the one that binds.

@words text="Change it by less than its slack: nothing moves"
What slack does settle is smaller, and exact. Change that row's availability by less than its slack, and neither the plan nor the profit moves at all.

@chapter Try it
@words text="Assembly 18 → 24" sub="which tight row is worth an hour?"
Your turn. Set assembly to twenty four hours. Check that all three rows are tight at four and six. Then add one hour to each resource in turn, and see which one actually raises the profit.

@end text="Grow the rate table"
You can add a product column and watch the exact simplex solve it, on Learn. That's learn dot get er done dot I O.
