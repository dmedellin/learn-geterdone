---
format: long
lesson: accelerate-lean-management/shifting-left-on-security
title: Shifting left on security: build it in, don't bolt it on
thumb: Catch it early, fix it cheap
---

@chapter Does security slow you down?
@title text="Integrating Infosec into the Delivery Lifecycle" sub="Accelerate, Chapter 6" art=thumb
Does bringing security into the work speed delivery up or hold it back? That was a research question for the twenty sixteen survey, and chapter six gives the answer.

@quote text="Our research shows that building security into software development not only improves delivery performance but also improves security quality." cite="Forsgren, Humble and Kim, Accelerate, Chapter 6"
Our research shows that building security into software development not only improves delivery performance but also improves security quality.

@chapter The problem
@art security-wall
DevOps set out to stop developers and operations throwing work over a wall. The same habit appears with security. Infosec teams are thinly staffed, and usually brought in at the end of the lifecycle, when a change is painful and expensive.

@words text="1 : 10 : 100" sub="infosec · infrastructure · developers (Wickett, 2014)"
The authors quote James Wickett's ratio, from twenty fourteen: in large companies, about one infosec person to ten infrastructure people to a hundred developers. And many developers don't know the common risks, like those on the OWASP Top Ten.

@chapter Shifting left
@list heading="Shifting left" items="A security review for every major feature@security review|Infosec across the whole lifecycle@whole lifecycle|Make the secure route the easy one@easy one"
Their answer is to shift left, in three parts. Every major feature gets a security review, arranged so development doesn't slow down. Security takes part across the whole lifecycle: design, demonstrations, and the automated tests. And the secure route is made the easy one, with approved libraries and toolchains simple to adopt.

@art paved-tools
The authors report that teams that do this are better at continuous delivery, which in turn helps delivery performance. And the two teams communicate better as a side benefit.

@art shift-left-timeline
Why move the work? It's easier to equip the builders to get it right than to inspect nearly finished systems for large architectural defects. And infosec can't review every deployment once deployments are frequent. In many organizations, security and compliance is a major bottleneck.

@art platform-controls
A box on the United States federal government makes the same point at scale. A platform built by a small team of civil servants, cloud dot gov, takes care of most required controls at the platform level, so systems reach production in weeks, not months.

@chapter The finding
@words text="High performers: 50% less time fixing security issues"
The authors report that high performers spent fifty percent less time than low performers on fixing security problems. That's a comparison of groups of teams in the survey, from what respondents reported. It doesn't promise every team will halve its time, and the chapter gives no cost for fixing a finding at any stage.

@art rugged
The chapter ends with the Rugged movement. DevSecOps and Rugged DevOps are two more names for DevOps with security in it. The authors take one point from it: being rugged is everybody's responsibility.

@chapter Pricing the findings
@words text="design 2 h · build 4 h · test 12 h · after release 40 h" sub="the lesson's own costs, not the book's"
Now the count. An invented team has eight hundred hours of new work, a hundred unplanned and one hundred and forty rework, and it found twelve security issues. The lesson states its own cost per fix: two hours at design, four at build, twelve at test, and forty after release.

@math heading="Found late" items="build 1 × 4 = 4 · test 3 × 12 = 36@one at build;;after release 8 × 40 = 320@eight after release;;security 360 of 1,400 h ≈ 25.7%@three hundred and sixty"
Found late: one at build is four hours, three at test is thirty six, and eight after release is three hundred and twenty. That's three hundred and sixty hours of security work, in a total of one thousand four hundred, about twenty five point seven percent.

@math heading="Found early" items="design 5 × 2 = 10 · build 4 × 4 = 16@five at design;;test 2 × 12 = 24 · after release 1 × 40 = 40@two at test;;security 90 of 1,130 h ≈ 8%@ninety in all"
Found early, the same twelve: five at design is ten, four at build is sixteen, two at test is twenty four, and one after release is forty. Ninety in all. The total falls to one thousand one hundred and thirty, and security is about eight percent.

@art hours-by-stage
New work's share rises from about fifty seven point one percent to about seventy point eight. But those two hundred and seventy freed hours are the arithmetic of the costs the lesson chose. The lab can't say what finding issues earlier takes.

@chapter Where people slip
@list heading="Common slips" items="Security becomes the developers' job alone@The first|The 50% is your team's saving@The second|The end is the safe place to review@the third"
The first slip is thinking shifting left means security is the developers' job alone. Infosec still joins design and demos. The second is reading the fifty percent as your team's saving. And the third is treating the review at the end as the safe place for it.

@chapter Try it
@words text="10 issues · costs 3, 6, 15, 45 h" sub="late vs early"
Your turn. A team has ten security issues, with costs of three, six, fifteen and forty five hours by stage. Work out the hours for the late team and the early team, and the hours freed.

@end text="Catch it early"
You can price your own findings by stage in the lab, on Learn. That's learn dot get er done dot I O.
