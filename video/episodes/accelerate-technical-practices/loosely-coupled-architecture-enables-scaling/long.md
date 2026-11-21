---
format: long
lesson: accelerate-technical-practices/loosely-coupled-architecture-enables-scaling
title: Must a bigger team be a slower one? Conway's law and scaling
thumb: Bigger doesn't have to mean slower
---

@chapter Conway's law
@title text="A Loosely Coupled Architecture Enables Scaling" sub="Accelerate, Chapter 5" art=thumb
Add more developers, and each one gets less done. That's the orthodox view of growing a software team. Chapter five tests it, and the bridge in its argument is a sentence from nineteen sixty eight.

@quote text="organizations which design systems . . . are constrained to produce designs which are copies of the communication structures of these organizations" cite="Melvin Conway, as quoted in Accelerate, Chapter 5"
Melvin Conway wrote that organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations.

@art conway-mirror
In the twenty seventeen survey, teams that scored highly on architecture needed little communication between delivery teams to get work done, and could test, deploy and change their parts without depending on others. Architecture and teams are loosely coupled.

@chapter The inverse maneuver
@words text="Inverse Conway maneuver" sub="evolve the teams to get the architecture you want"
The authors say their research supports the inverse Conway maneuver: evolve the team and organization structure to achieve the architecture you want. Then teams can go from design to deployment without high bandwidth communication with other teams.

@art cross-functional
Those delivery teams must be cross functional, with the skills to design, build, test, deploy and run the system. 
@art bounded-contexts
How do you get there? Bounded contexts and APIs split a large domain into smaller, loosely coupled units. Test doubles and virtualization let you test a service on its own. And service oriented or microservice designs have to be strict about independence to deliver it.

@words text="Collaboration on shared goals" sub="not on fine-grained implementation decisions"
And this isn't a ban on talking. DevOps is about better collaboration. The aim is that communication isn't swamped by fine grained implementation decisions, so it can go to higher level shared goals.

@chapter What it buys
@list heading="Two gains the authors expect" items="Better delivery performance@better delivery|Productivity that grows with headcount@linearly or better"
With a loosely coupled architecture and a matching organization, the authors expect two gains. Better delivery performance, with tempo and stability up and burnout down. And productivity that grows linearly or better as the organization grows.

@art scaling-trends
To test the second, they plot deploys per developer per day against the number of developers, for respondents who deploy at least once a day. As developers grow, low performers deploy less often per developer, medium performers just as often, and high performers significantly more often.

@words text="Generative culture · modular architecture · CD · good leadership"
They credit what predicts high performance: a generative culture, a modular architecture, the practices of continuous delivery, and good leadership. Those let a business move faster as it adds people.

@chapter A limit to carry
@art deploy-count
Remember chapter two's objection to output measures? A deploy is a count of something done, not of value delivered. The chapter treats it as the productivity metric and doesn't take that up. And only respondents who deploy at least daily appear in the figure.

@chapter The rate by hand
@math heading="Rising, over 20 days" items="small: 40 / (5 × 20) = 2/5 = 0.400@forty over;;medium: 190 / (20 × 20) = 19/40 = 0.475@one hundred and ninety;;large: 1,000 / (80 × 20) = 5/8 = 0.625@one thousand"
Now the count, with invented organizations over twenty days. The small one, five developers, makes forty deploys: forty over five times twenty, two fifths. The medium one, twenty developers, makes one hundred and ninety: nineteen fortieths. The large one, eighty developers, makes one thousand: five eighths. The rate rises with size.

@math heading="Holding and falling" items="holding: 50, 200, 800 → ½ · ½ · ½@fifty, two hundred;;falling: 60, 200, 640 → 3/5 · ½ · 2/5@sixty, two hundred"
In a second preset, the same sizes make fifty, two hundred and eight hundred deploys: one half each time. In a third they make sixty, two hundred and six hundred and forty: three fifths, one half, two fifths.

@art same-total-up
Total deploys rise in all three presets. What's at stake is the share each developer carries, not whether the organization ships more. And the lab can't say why any shape appears.

@chapter Where people slip
@list heading="Common slips" items="More people must mean less each@The first|Loose coupling means no talking@The second|Growth alone raises the rate@And the third"
The first slip is believing more people must mean less output per person. The second is reading loose coupling as a ban on talking. And the third is expecting growth alone to raise the rate. The authors tie it to culture, architecture, practices and leadership.

@chapter Try it
@words text="10 days · a: 4, 20 · b: 16, 64 · c: 64, 160"
Your turn. Ten days, three organizations, developers then deploys. Work out each one's deploys per developer per day, and say whether the rate rises, holds or falls. Then say what would have to be true of the largest for the rate to hold.

@end text="Does bigger mean slower?"
You can compare organizations of different sizes in the lab, on Learn. That's learn dot get er done dot I O.
