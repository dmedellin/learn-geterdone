---
format: long
lesson: accelerate-lean-management/team-experimentation-and-product-management
title: Team experimentation and the virtuous cycle
thumb: Which drives which?
---

@chapter Building to someone else's spec
@title text="Team Experimentation and Effective Product Management" sub="Accelerate, Chapter 8" art=thumb
Many teams in organizations that call themselves Agile still have to build to requirements written by other teams. The authors say that can yield products customers don't love.

@art outside-spec
Agile means seeking customers' views from the start. A team that can't alter what it builds as it learns, without a nod from outside, is hobbled in innovating.

@chapter The finding
@quote text="the ability of teams to try out new ideas and create and update specifications during the development process, without requiring the approval of people outside the team" cite="Forsgren, Humble and Kim, Accelerate, Chapter 8"
Their finding is about the ability of teams to try out new ideas and create and update specifications during the development process, without requiring the approval of people outside the team.

@art team-free
So picture the opposite: a team that can redraw the specification as it learns, fed by what customers say, without waiting for sign off from outside.

@words text="Predicts profitability · productivity · market share"
That ability predicts organizational performance, measured by profitability, productivity and market share.

@list heading="Not free to try anything" items="Small batches@small batches|Flow of work visible to everyone@visible|Customer feedback in the design@customer feedback"
But the authors say at once what they don't propose: letting developers chase any idea they fancy. Experimentation has to go with the other capabilities: small batches, the flow of work visible to everyone, and customer feedback built into the design. Then choices are informed, and decisions are shared.

@chapter The virtuous cycle
@art two-models
The second section is about the order of cause. The authors analysed Lean product management over two years, twenty sixteen and twenty seventeen. In the first model, Lean product practices predicted better delivery performance, a more generative culture, and less burnout.

@art virtuous-cycle
The next year they turned the model round, and confirmed that delivery performance in its turn predicts those practices. Combined, it's a reciprocal model: a virtuous cycle.

@words text="Predict: a relationship tested in a model" sub="once in each direction, a year apart"
Read that with care. Predict means a statistical relationship tested in a model, once in each direction, with a year between, on perceptions. What carries the claim is two years of analysis, which a single correlation can't.

@chapter A correlation by hand
@art scatter-eight
Now the count. Pearson's r measures how closely two scores move together, from minus one to one. Eight invented teams are each scored from one to seven on lean product practice, and on delivery. Both means are four, so each team's deviations are just its scores minus four.

@math heading="Eight teams, lean as x" items="Σ products of deviations = 7@sum to seven;;Σ lean² = 12 · Σ delivery² = 8@twelve;;r = 7 / √96 ≈ 0.714@square root of ninety six;;r² = 49/96 ≈ 51.0%@fifty one"
The products of the deviations sum to seven. The lean scores' squared deviations sum to twelve, and the delivery scores' to eight. So r is seven over the square root of ninety six, about zero point seven one four. And r squared is forty nine over ninety six, about fifty one percent.

@chapter Swap the columns
@math heading="Swap x and y" items="r is still 0.714@still;;lean as x: slope 7/12 ≈ 0.583 · intercept 5/3@seven twelfths;;delivery as x: slope 7/8 = 0.875 · intercept 0.5@seven eighths"
Now swap the columns, delivery as x and lean as y. R is still zero point seven one four. It's symmetric, so it can't tell which drives which. What changes is the least squares line: with lean as x the slope is seven twelfths, and with delivery as x it's seven eighths.

@art swap-arrows
Each line predicts one score from the other. Neither says one score moves the other. To split the directions, the authors needed other designs: theory, and two years of data.

@words text="Strong: r above 0.7" sub="the lab's convention, not the book's"
The lab calls this positive and strong, using cut offs of zero point three and zero point seven that it states and the book doesn't. They're a convention, and zero point seven one four is just over the second.

@chapter Where people slip
@list heading="Common slips" items="The reciprocal model proves cause@The first|Teams should be free to try anything@The second|A high r tells you the direction@the third"
The first slip is reading the reciprocal model as proof that each causes the other. The second is believing teams should be free to try anything. And the third is treating a high r as a statement about direction. A third thing driving both would give the same number.

@chapter Try it
@words text="u1 1,2 · u2 2,1 · u3 3,3 · u4 4,5 · u5 5,4"
Your turn. Five invented teams, lean score then delivery score. Find both means, the three sums Pearson's r needs, then r and r squared. Then swap the two columns, and say what changes.

@end text="r names no direction"
You can compute r both ways and watch the lines change, on Learn. That's learn dot get er done dot I O.
