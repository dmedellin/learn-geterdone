---
format: long
lesson: accelerate-the-science/inferential-predictive-analysis
title: What Accelerate means by drive: inferential predictive analysis
thumb: Drive means predict
---

@chapter Theory first
@title text="Inferential Predictive Analysis" sub="Accelerate, Chapter 12" art=thumb
When a later chapter of Accelerate says a practice drives performance, what kind of finding is that? This section of chapter twelve tells you, and it starts with how science is done.

@quote text="Science is done by stating hypotheses, designing research to test those hypotheses, collecting data, and then testing the stated hypotheses." cite="Forsgren, Humble and Kim, Accelerate, Chapter 12"
In the authors' words. Science is done by stating hypotheses, designing research to test those hypotheses, collecting data, and then testing the stated hypotheses.

@chapter Where it's used
@art no-lab
Inferential design is one of the most common in business and technology research. It's used where a purely experimental design isn't possible. A company won't sacrifice earnings so a researcher can have a tidy control group, and the data comes from working organisations, not a laboratory.

@art theory-first
The safeguard against fishing for patterns is the order. Theory comes first and drives the hypotheses, and the theory has to be mature and well supported before the data is touched. Each further piece of supporting evidence earns the hypothesis a little more trust.

@list heading="The book's main hypotheses" items="Continuous delivery and architecture drive delivery performance@continuous delivery|Delivery performance affects organisational performance@organisational performance|Culture affects both@culture"
The examples are the book's main claims. Continuous delivery and architecture practices drive software delivery performance. Delivery performance positively affects organisational performance. And culture positively affects both. They were tested with multiple linear regression or partial least squares. Where no theory suggests prediction, the authors report only the correlation.

@chapter What drive means
@words text="drive = a theory-based hypothesis tested on survey data"
So read drive with that in mind. Whenever the book speaks of impacting or driving results, the design was this third type: a hypothesis from theory, tested on survey data, to see whether one measure predicts another.

@list heading="The rungs they did not climb" items="Predictive: forecasting the future@forecasts|Causal: the gold standard, randomised studies@gold standard|Mechanistic: the exact change for the exact effect@exact change"
The last three rungs weren't part of the research, because the authors didn't have the data. Predictive analysis forecasts future events from past ones. Causal analysis they call the gold standard, and it generally needs randomised studies, like A B tests on websites. Mechanistic analysis works out the exact change to cause an exact behaviour.

@art randomised-split
In a randomised study, chance decides which group gets the change. That's the step a survey of working organisations can't take.

@art two-sides
Be fair to both sides. The authors didn't run randomised studies, so the book isn't best read as proof of cause. They argue that a hypothesis from theory, tested on years of data, earns confidence. Martin Fowler's foreword adds cautions: the data are perceptions, the sample may not reflect IT at large, and confirmation bias is a strong force.

@chapter A third variable at work
@art size-groups
The lab shows one thing to guard against. Twelve invented changes to a codebase each have review comments, days to merge, and a size: small, medium or large.

@math heading="Preset size-explains" items="all twelve rows: r = 0.964@nought point nine six four;;within small 0.5 · medium 0.5 · large −0.5@within small;;pooled within size: r = 1 ÷ √(6 · 6) = 0.167@nought point one six seven"
Over all twelve rows, r is nought point nine six four, a very strong correlation. Now look inside each size. Within small changes, r is nought point five; within medium, nought point five; within large, minus nought point five. Pool the groups' sums and the within group r is one over six, nought point one six seven.

@art group-gaps
So most of the correlation comes from the differences between sizes. Large changes have more comments and also take longer. That's a third variable doing the work. It isn't a finding that size causes either; it's a reason to ask what else isn't held fixed.

@math heading="Preset size-explains-nothing" items="all rows: r = 0.967@all the rows;;pooled within repository: r = 0.967@also nought point nine six seven"
The contrast: twelve changes from three repositories. All the rows give r of nought point nine six seven, and the pooled within repository r is also nought point nine six seven. So the repository isn't the explanation. That doesn't make the link causal either.

@chapter Where people slip
@list heading="Common slips" items="Reading drives as proof of cause@proof of cause|Fishing first, theory after@fishing|One variable held fixed settles it@settles"
Three slips. Reading drives as proof of cause. Fishing in the data, then writing the theory. And thinking that holding one variable fixed settles it. A variable nobody measured can't be held fixed.

@chapter Try it
@words text="north: (1, 3) (2, 2) (3, 1) · south: (7, 9) (8, 8) (9, 7)" sub="comments, days"
Your turn. Six invented changes in two repositories. North: one comment and three days, two and two, three and one. South: seven and nine, eight and eight, nine and seven. Find r over all six, in each repository, and pooled. Watch the sign.

@end text="State it first, then test it"
Then check it in the lab, on Learn. That's learn dot get er done dot I O.
