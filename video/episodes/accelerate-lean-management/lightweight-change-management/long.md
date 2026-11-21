---
format: long
lesson: accelerate-lean-management/lightweight-change-management
title: Change advisory boards: slower, and not safer
thumb: Slower, and not safer
---

@chapter Who approves a change?
@title text="A Lightweight Change Management Process" sub="Accelerate, Chapter 7" art=thumb
Every organization has some process for changing production. In a startup, you call another developer over to look at your code. In a large organization, a change might go to a change advisory board, a CAB outside the team, and take days or weeks.

@list heading="Four scenarios" items="An outside body signs off every change@every production change|Sign-off only for risky changes@risky changes|The team relies on peer review@peer review|Nothing needs approval@nothing needs"
The authors put four scenarios to respondents. An outside body like a manager or CAB signs off every production change. Sign off only for risky changes, like database ones. The team relies on peer review. Or nothing needs approval.

@art cab-wait
The question the section asks is what that outside approval actually does to delivery performance. Does all the waiting buy anything?

@chapter What they found
@art four-routes
The results were surprising. Approval of risky changes alone showed no correlation with delivery performance. Teams with peer review, or no approval step, did better. And teams sending every change to an outside body did worse.

@quote text="approval by an external body (such as a manager or CAB) simply doesn't work to increase the stability of production systems" cite="Forsgren, Humble and Kim, Accelerate, Chapter 7"
Does outside approval at least buy stability? Their conclusion: approval by an external body, such as a manager or CAB, simply doesn't work to increase the stability of production systems.

@list heading="External approval" items="No help to time to restore@time to restore|No correlation with change fail rate@change fail rate|Slower delivery@slowed delivery"
It didn't help time to restore service, it showed no correlation with change fail rate, and it slowed delivery down. In their view it's worse than having no approval at all. And note the strength: these are survey correlations.

@chapter The recommendation
@art peer-pipeline
Their recommendation is a light process built on review by peers, like pair programming or a code review inside the team, with a deployment pipeline that catches and turns away faulty changes. For every kind of change: code, infrastructure and database.

@chapter Segregation of duties
@list heading="Without a CAB" items="Someone else reviews, recorded in a tool@did not write|Production only through an automated pipeline@only through"
What about regulated industries? Segregation of duties doesn't require a CAB. Two mechanisms satisfy it. Somebody who did not write the change reviews it, and the sign off is logged, in a pull request for instance. And changes reach production only through a fully automated pipeline.

@art audit-trail
The pipeline leaves auditors a complete record of what was applied where, from where, with which tests, and approved by whom.

@words text="Risk management theater"
The authors close with reasoning, offered as logic, not a result. An outside body can't judge tens of thousands of changed lines from hundreds of engineers. They call it risk management theater.

@art governance
They do see a place for people outside teams, in a governance role: watching how delivery is going, and helping teams take up the practices the book describes. Not inspecting changes.

@chapter Counting changes
@math heading="Six peer-reviewed changes" items="waits: 1, 2, 1, 3, 2, 1 = 10 h@one, two, one;;mean 10/6 = 1.67 h · median 1.5 h@one point six seven;;1 of 6 failed = 16.7%@one of six"
Now the count, with twelve invented changes. Six went through peer review, waiting one, two, one, three, two and one hours: ten hours, a mean of one point six seven, and a median of one point five. One of six failed, sixteen point seven percent.

@math heading="Six CAB changes" items="waits: 48, 72, 96, 24, 72, 120 = 432 h@forty eight;;mean 72 h · median 72 h@seventy two;;1 of 6 failed = 16.7% · difference 0@is zero"
Six went to the CAB, waiting forty eight, seventy two, ninety six, twenty four, seventy two and one hundred and twenty hours. Four hundred and thirty two in all, a mean and median of seventy two. One of six failed, so the difference in fail rate is zero.

@art one-more-failure
That matches the authors' finding, on a sample built to match it. Now make one more CAB change fail. Its rate jumps to two in six, thirty three point three percent. One change moved the rate by a sixth. Six changes are far too few to separate the routes.

@chapter Where people slip
@list heading="Common slips" items="The book says have no review at all@The first|Regulated industries must keep a CAB@The second|The lab's sample is evidence about CABs@the third"
The first slip is concluding the book says to have no review at all. It recommends peer review plus a pipeline. The second is believing a regulated industry has to keep its CAB. And the third is reading the lab's sample as evidence about CABs.

@chapter Try it
@words text="4 none · 4 peer · 4 CAB" sub="CAB waits 24, 48, 72, 96 h"
Your turn. Twelve changes, four by each route: none, peer and CAB. Find each route's change fail rate, the mean wait of the CAB and peer routes, and how many extra hours a CAB change waits on average. Then say what the sample doesn't show.

@end text="Review by peers, deploy by pipeline"
You can compare approval routes on your own changes in the lab, on Learn. That's learn dot get er done dot I O.
