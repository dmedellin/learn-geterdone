---
format: long
lesson: accelerate-technical-practices/the-impact-of-continuous-delivery
title: What continuous delivery predicts, from speed to burnout
thumb: Rework is a proxy for quality
---

@chapter What does it do?
@title text="The Impact of Continuous Delivery" sub="Accelerate, Chapter 4" art=thumb
What does continuous delivery actually do for a team? And how would you measure that without a number for quality itself? Chapter four's two impact sections take those in turn.

@list heading="Modelled, 2014 to 2016" items="Version control@Version control|Test automation@test automation|Deployment automation@deployment automation|Continuous integration@continuous integration|Shifting security left@security left|Trunk-based development@trunk based|Test data management@test data"
The first survey years modelled a list of capabilities: version control, reliable test automation, deployment automation, continuous integration, shifting security left, trunk based development, and test data management. Most were measured as constructs, from several agree or disagree statements.

@chapter What it predicted
@art routine-deploy
Taken together, they predicted delivery performance strongly. And also how work felt: less deployment pain and less team burnout. When delivery is routine, deploying isn't a big bang event. It's something done in office hours, as part of the day.

@art cd-arrows
Teams that did well also identified more strongly with their organization, and continuous delivery predicted the more generative culture of chapter three. In twenty seventeen, continuous delivery was measured as a construct of its own, and two new drivers joined: a loosely coupled architecture, and teams choosing their own tools.

@words text="Findings of a survey" sub="answers that move together as the theory says"
The book draws all of these as arrows, but they're findings of a survey, from analysis that tests whether answers move together as the theory says.

@chapter Measuring quality
@words text="Quality is value to some person" sub="Jerry Weinberg"
Then the chapter asks whether continuous delivery improves quality. The authors concede that quality is contextual and subjective, and quote Jerry Weinberg: quality is value to some person.

@art proxy-gauge
So you can't measure quality directly. You measure something that stands in for it. They already had one stand in, the change fail rate from chapter two.

@list heading="Three more proxies" items="The application's quality, as its team sees it@how good|Time on rework or unplanned work@rework or unplanned|Time on defects found by users@defects"
Besides change fail rate, they tried three more proxies: how good the application is, as its own team sees it; the share of the week on rework or unplanned work; and the share on defects found by end users. All three correlated with delivery performance.

@quote text="Unplanned work and rework are useful proxies for quality because they represent a failure to build quality into our products." cite="Forsgren, Humble and Kim, Accelerate, Chapter 4"
The strongest was rework and unplanned work, and continuous delivery predicted less of it. Unplanned work and rework are useful proxies for quality because they represent a failure to build quality into our products.

@chapter High and low performers
@math heading="Figure 4.4" items="high performers: 49% new · 21% unplanned or rework@high performers;;low performers: 38% new · 27% unplanned or rework@low performers"
In the survey, high performers reported forty nine percent of their time on new work, and twenty one percent on unplanned work or rework. Low performers reported thirty eight and twenty seven percent.

@art fuel-light
The authors explain it with an image from The Visible Ops Handbook. Unplanned work is the difference between heeding a low fuel warning light, and running dry on the highway, with six engineers dropping everything to carry fuel to a truck.

@art rework-loop
They add John Seddon's idea of failure demand: the work created by failing to do the right thing the first time.

@chapter A team's month
@math heading="One invented month" items="440 + 190 + 130 + 240 = 1,000 h@one thousand;;new 44% · unplanned 19% · rework 13% · other 24%@forty four;;unplanned + rework = 32%@thirty two"
Now the count. An invented team spent four hundred and forty hours on new work, one hundred and ninety on unplanned, one hundred and thirty on rework, and two hundred and forty on other things: one thousand in all. That's forty four percent new, nineteen unplanned, thirteen rework, and twenty four other. Unplanned and rework together take thirty two percent.

@math heading="Halve the rework" items="130 / 2 = 65 h freed@sixty five;;440 + 65 = 505 → 50.5% new@fifty point five"
Halve the rework. That frees sixty five hours. If all of them went to new work, it would rise to five hundred and five hours, fifty point five percent.

@art hours-split
But that assumes the team spends everything it saves on new work, which a real team might not. And halving rework doesn't say how to halve it. The chapter's answer is small batches with continuous testing.

@chapter Where people slip
@list heading="Common slips" items="The benefit is only speed@The first|Treating a proxy as quality itself@The second|Aiming for zero unplanned work@And the third"
The first slip is thinking the benefit is only speed. The second is treating a proxy as the quantity itself. A team with little rework might still be building the wrong thing. And the third is aiming for zero unplanned work. Even the high performers spent about a fifth of their time on it.

@chapter Try it
@words text="new 320 · unplanned 200 · rework 160 · other 120"
Your turn. A team's month: three hundred and twenty hours new, two hundred unplanned, one hundred and sixty rework, one hundred and twenty other. Find each share, the hours freed by halving rework, and the new share of new work. Then say why neither tells you whether it's a high performer.

@end text="Where did the month go?"
You can split your own team's month in the lab, on Learn. That's learn dot get er done dot I O.
