---
format: long
lesson: accelerate-measuring-performance/the-flaws-in-previous-measures
title: Lines of code, velocity, utilization: why they mislead
thumb: Busier is not faster
---

@chapter Why it's hard
@title text="The Flaws in Previous Measures" sub="Accelerate, Chapter 2" art=thumb
How do you measure a software team's performance? Chapter two of Accelerate starts by saying it's hard. The inventory is invisible, the way work is broken down is fairly arbitrary, and design and delivery happen at the same time.

@list heading="Two flaws" items="Outputs, not outcomes@outputs|Local, not global@one person"
The authors name two flaws in the usual measures. They focus on outputs rather than outcomes. And they focus on what one person or one function does, rather than on what a team, or the whole, delivers. Then they test three examples.

@art outputs-outcomes
A stream of things produced is an output. What the stream achieves for the organization is the outcome. Keep that difference in mind for each example.

@chapter Lines of code
@art bloated-code
Lines of code come first. Reward developers for lines written, and you get more lines, and the authors say bloated software, with higher maintenance and change costs. They'd rather have ten lines than a thousand for the same problem. And a business change that removes the need for code is better still.

@words text="Neither more nor fewer" sub="one unreadable line is worse than a few clear ones"
But they don't say fewer is always better. A task done in one line nobody else can read is worse than a few lines everybody can. A count of lines is a count of output, and no direction of it is the goal.

@chapter Velocity
@art velocity-points
Velocity is the Agile version. Teams estimate stories in points, and the points signed off in an iteration are the velocity. It was designed to plan capacity, to work out how long the planned work will take.

@list heading="When velocity is misused" items="It is relative and team-dependent@relative|Used as a target, it gets gamed@gaming"
The authors object when managers use it to compare teams or measure productivity. It's relative and team dependent, so one team's points can't be set against another's. And as a target, it invites gaming: inflated estimates, stories pushed through, collaboration suffering, and teams discouraged from helping one another.

@chapter Utilization
@quote text="high utilization is only good up to a point" cite="Forsgren, Humble and Kim, Accelerate, Chapter 2"
The third is utilization, how busy people are. The authors say that high utilization is only good up to a point. Past it, nothing is left for the unplanned, for a change of plan or for improving the work, and lead times lengthen.

@art queue-curve
They cite queue theory: lead times approach infinity as utilization approaches a hundred percent. So utilization has to be managed against lead time, the measure that avoids the faults of the other two.

@chapter The arithmetic
@art waiting-queue
The lesson puts that into the simplest queueing model. Picture one worker taking tasks one at a time, with tasks arriving at random. When a task arrives while another is being done, it joins the queue.

@math heading="One worker, random arrivals" items="wait = u / (1 − u) service times@waits on average;;lead time = service ÷ (1 − u)@Its lead time"
In that model, a task waits on average u over one minus u service times, where u is the utilization. Its lead time, the wait plus the work, is the service time divided by one minus u.

@math heading="A two-hour review at 80%" items="u = 4/5,  1 − u = 1/5@four fifths;;wait = (4/5) ÷ (1/5) = 4 service times@four service times;;lead time = 2 h × (1 + 4) = 10 h@ten hours"
Take a review with two hours of hands on work, at eighty percent busy. U is four fifths, so one minus u is one fifth. The wait is four fifths over one fifth, four service times. The lead time is two hours times one plus four, which is ten hours.

@math heading="Same review, busier team" items="50% → 4 h@fifty percent;;80% → 10 h@eighty;;90% → 20 h@ninety;;95% → 40 h@ninety five;;99% → 200 h@ninety nine"
Now run the ladder. At fifty percent the lead time is four hours. At eighty, ten. At ninety, twenty. At ninety five, forty. And at ninety nine, two hundred. Going from ninety to ninety nine multiplies it by ten.

@art slack-time
The same person does the same review at the same speed in every row. Only the queue changes. Take a three hour task at ninety percent: thirty hours. Drop to eighty percent and it's fifteen, half, and nothing was sped up.

@chapter Read it carefully
@list heading="Two cautions" items="A real team is not one queue@simplification|A hyperbola, not strictly exponential@hyperbola"
Two cautions. The model is a simplification: a real team has several people, mixed task sizes and arrivals that aren't random. And the growth is a hyperbola, not strictly the exponential of the book's wording. The book's point, that the wait has no limit, still holds.

@list heading="Common slips" items="Busier means more productive@The first|Velocity compares teams@The second|Less code is always better@the third"
The first slip is thinking a busier team is a more productive one. The second is using velocity to compare teams. And the third is concluding that less code is always better.

@chapter Try it
@words text="6 hours of work · 75% utilization"
Your turn. A task takes six hours of hands on work, and the team is seventy five percent busy. Find the wait in service times, then the lead time in hours. Then find the utilization at which the lead time is ten times the service time.

@end text="Watch the wait grow"
You can slide the utilization and watch the lead time climb, on Learn. That's learn dot get er done dot I O.
