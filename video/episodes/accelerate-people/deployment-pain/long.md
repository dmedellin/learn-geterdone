---
format: long
lesson: accelerate-people/deployment-pain
title: Deployment pain: what the dread at deploy time tells you
thumb: Where deploys hurt most
---

@chapter The question
@title text="Deployment Pain" sub="Accelerate, Chapter 9" art=thumb
Every engineer knows the feeling: dread at deploy time. Chapter nine of Accelerate asks whether teams are reaching good delivery by brute force, at the cost of the people doing it. So it starts with that dread.

@quote text="We found that where code deployments are most painful, you’ll find the poorest software delivery performance, organizational performance, and culture." cite="Forsgren, Humble and Kim, Accelerate, Chapter 9"
Here's the claim at the centre of the section. We found that where code deployments are most painful, you'll find the poorest software delivery performance, organizational performance, and culture.

@chapter Why deployment
@art two-shores
Why start with deployment? The authors say it's where development meets IT operations, so it's where two groups differ most: in environment, in process, in mindset, even in the words they use for their work.

@art hidden-wall
There's a second warning sign that's easy to miss. Ask a developer or tester what deployments are like. If they say they've never thought about it, the authors suspect something is keeping that work out of their sight, and they count that as a sign that delivery performance may be low.

@chapter Measuring a feeling
@list heading="Asked in three surveys" items="2015, 2016, 2017@twenty fifteen|Feared?@feared|Disruptive?@disruptive|Easy and pain-free?@easy and pain free"
The measure came from the authors' experience and from talking to people who run systems. It was asked in twenty fifteen, twenty sixteen and twenty seventeen. Were deployments feared? Disruptive to your work? Or easy and pain free? Like every measure in the book, it's a person's report, gathered by survey.

@chapter What moves with it
@art calm-pipeline
The first finding is about practices. Deployment pain fell for teams that put in comprehensive test and deployment automation, continuous integration with trunk based development, shift left on security, good test data management, loosely coupled architecture, the ability to work independently, and version control of everything needed to reproduce production.

@words text="More pain, lower performance" sub="a high correlation, as the authors report it"
The second finding is a correlation. Where deployments hurt more, IT performance, organizational performance and culture are all lower. The authors call it a high correlation. The same practices that improve speed and stability also reduce the stress of pushing code.

@chapter Three causes
@list heading="Why deployments get brittle" items="Not built for deployability@deployability|Manual changes in production@manual changes|Many handoffs between silos@handoffs"
The authors give three causes. Software that wasn't written with deployability in mind, so it needs its environment set up one precise way. Manual changes made to production during the deployment, with typing slips and drifting environments. And many handoffs between teams in siloed organizations.

@art moon-clock
Their remedies follow: systems that deploy easily and tolerate failure, production state reproduced from version control, and simple deployments. And a deployment that must happen outside business hours, they say, is a sign of architectural problems.

@chapter Counting a correlation
@art scatter-line
The lab computes a correlation coefficient, r, on eight invented teams. Each has a share of deployment steps done by hand, from ten to eighty percent, and a pain score from one to seven. The means are forty five percent and four.

@math heading="The preset manual-steps" items="Σ products of distances = 260@two hundred and sixty;;Σ squares: share = 4200, pain = 18@four thousand two hundred;;r² = 260² ÷ (4200 · 18) = 67600/75600 = 0.894@sixty seven thousand six hundred;;r = 260/274.95 = 0.946@nought point nine four six"
Subtract the means, multiply each team's two distances, and add them: two hundred and sixty. The sums of squares are four thousand two hundred for the share and eighteen for pain. So r squared is sixty seven thousand six hundred over seventy five thousand six hundred, about nought point eight nine four. And r is nought point nine four six.

@chapter One team differs
@art one-dot-drops
Now change one thing. The last team, doing eighty percent of its steps by hand, scores its pain at two instead of six.

@math heading="The preset one-team-differs" items="r = 0.463@nought point four six three;;r² = 21.4%@twenty one point four"
The lab now reports r of nought point four six three, and r squared of twenty one point four percent. One team out of eight moved the figure by about half. That's what a small sample does, and it's why the authors collect thousands of responses.

@chapter Where people slip
@list heading="Common slips" items="It's only a feeling@only a feeling|A high r proves a cause@proof|Nobody thinks about it, so it's fine@nobody thinks"
Don't treat pain as only a feeling: it moves with outcomes measured in other ways. Don't read a high r as proof that manual steps cause the pain. And don't treat a deployment that nobody thinks about as a painless one.

@chapter Try it
@words text="P 10, 2 · Q 30, 3 · R 50, 4 · S 70, 4 · T 90, 7"
Your turn, with five invented teams: P, ten percent manual, pain two. Q, thirty and three. R, fifty and four. S, seventy and four. T, ninety and seven. Find the means, the sum of products and the two sums of squares, then write r squared as a fraction.

@end text="Compute r on your own teams"
Then check it in the lab, on Learn. That's learn dot get er done dot I O.
