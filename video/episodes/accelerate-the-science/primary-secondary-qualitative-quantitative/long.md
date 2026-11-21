---
format: long
lesson: accelerate-the-science/primary-secondary-qualitative-quantitative
title: Primary or secondary, qualitative or quantitative, and what a summary hides
thumb: Same mean, different team
---

@chapter How do they know?
@title text="Primary and Secondary, Qualitative and Quantitative" sub="Accelerate, Chapter 12" art=thumb
Any claim about what makes teams perform raises a question. How do you tell the actions that merely coincide with a change from the ones that bring it about? Part two of Accelerate is the authors' answer, and it starts by sorting research two ways.

@quote text="Research falls into two broad classes: primary and secondary research. The key difference between these two types is who collects the data." cite="Forsgren, Humble and Kim, Accelerate, Chapter 12"
The first sorting, in their words. Research falls into two broad classes: primary and secondary research. The key difference between these two types is who collects the data.

@chapter Who collected it
@art two-sources
Secondary research summarises what someone else collected, like a school report or a market study. It's faster and cheaper, but you're bound by whatever data exists. Primary research collects new data, like the national census taken every ten years. You choose your questions, at greater cost. The authors put their own work here.

@chapter What form it takes
@art words-to-numbers
The second sorting is by the form of the data. Qualitative data isn't in numbers: interviews, blog posts, long form logs, an ethnographer's notes. It's rich, and can reveal what you didn't expect, but it's harder to analyse. Quantitative data has numbers in it, from system logs or from a survey that asks for answers on a scale.

@words text="A survey isn't qualitative by default"
So a survey isn't qualitative just because it doesn't come from a machine. What matters is what the questions ask. The authors' research is quantitative, collected with a Likert type instrument.

@chapter Six rungs
@art ladder-six
Numbers open the door to statistics, and the chapter sets out a ladder for it.

@list heading="Leek's six types of analysis" items="Descriptive@descriptive|Exploratory@exploratory|Inferential predictive@inferential predictive|Predictive@predictive,|Causal@causal|Mechanistic@mechanistic"
The ladder comes from Jeffrey Leek, a biostatistician at Johns Hopkins. Six types, in rising complexity: descriptive, exploratory, inferential predictive, predictive, causal and mechanistic. The authors say their analyses fall into the first three, plus one that doesn't fit the ladder cleanly: classification.

@chapter The first rung
@art sample-population
Descriptive analysis summarises and reports the data, like a census. It's often the first step of a longer analysis. Two words matter here. The population is the whole group you want to learn about, and the sample is the defined portion whose data you have. A description is worth no more than how that sample was drawn.

@math heading="Preset team-a: 1, 3, 4, 5, 5, 6, 6, 6, 7, 7" items="mean = 50 ÷ 10 = 5@fifty over ten;;median = (5 + 6) ÷ 2 = 5.5@five point five;;mode = 6@mode is six;;range = 7 − 1 = 6@seven minus one"
Ten invented people answer one statement on the seven point scale. The answers sum to fifty, so the mean is fifty over ten, five. The middle two are five and six, so the median is five point five. Six appears three times, so the mode is six. And the range is seven minus one, six.

@art spread-bars
A centre isn't the whole story. How far do the answers spread around it?

@math heading="Spread around the mean" items="squared distances sum to 32@thirty two;;population: √(32 ÷ 10) ≈ 1.789@divide by n;;sample: √(32 ÷ 9) ≈ 1.886@n minus one"
Square each answer's distance from five, and the squares sum to thirty two. Divide by n and take the root, and you get one point seven eight nine: the ten people as they are. Divide by n minus one, and you estimate the spread of a larger group they came from: one point eight eight six.

@chapter A second team
@art two-teams-dots
Now team b: three, four, four, four, five, six, six, six, six, six.

@math heading="Team-b against team-a" items="mean 5 · median 5.5 · mode 6: the same@the same;;range 3 instead of 6@range is three;;SD 1.095 and 1.155@one point oh nine five"
The mean is again five, the median again five point five, the mode again six: the same. But the range is three instead of six, and the standard deviations fall to one point oh nine five and one point one five five. One mean can't tell you which team you're looking at, and no number here says why the first team is more spread out.

@words text="A mean assumes equal steps" sub="the lesson's own caution"
One caution is the lesson's own. A mean treats the step from one to two as the same size as six to seven, which a Likert type scale only assumes. Showing median and mode as well is harder to over-read.

@chapter Where people slip
@list heading="Common slips" items="Calling a survey qualitative@qualitative|Reading a mean as what the group thinks@what the group thinks|Expecting a description to explain@explain"
Three slips: calling a survey qualitative because it isn't machine data; reading a mean as what the group thinks; and expecting a description to explain. A summary says what, never why.

@chapter Try it
@words text="1, 5, 5, 5, 6, 6, 6, 6 → change the 1 to a 5"
Your turn. Eight answers: one, five, five, five, six, six, six, six. Find the mean, median, mode, range and both standard deviations. Then change the one to a five and see which summaries move.

@end text="Describe first, then climb"
Check it in the lab, on Learn. That's learn dot get er done dot I O.
