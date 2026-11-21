---
format: long
lesson: accelerate-measuring-performance/capabilities-not-maturity
title: Capabilities, not maturity: what a single level hides
thumb: A level hides what you can do
---

@chapter The argument
@title text="Capabilities, Not Maturity" sub="Accelerate, Preface and Chapter 1" art=thumb
Chapter one of Accelerate makes its first argument in one sentence, and it's about how you measure change. Not which practices to adopt, but what kind of yardstick to hold up against a team.

@quote text="we cannot stress enough that maturity models are not the appropriate tool to use or mindset to have" cite="Forsgren, Humble and Kim, Accelerate, Chapter 1"
Of maturity models, the authors write that we cannot stress enough that maturity models are not the appropriate tool to use or mindset to have. To see why, start with where their evidence comes from.

@chapter Where the evidence comes from
@art survey-responses
Forsgren, Humble and Kim began working together in late twenty thirteen, on the twenty fourteen State of DevOps Report. The book covers four years of findings, twenty fourteen through twenty seventeen: more than twenty three thousand survey responses from more than two thousand organizations, from startups to enterprises.

@list heading="How the surveys worked" items="Snowball sampling@snowball sampling|Likert-type answers@Likert type|Cross-sectional@cross sectional"
The surveys went out to mailing lists and social media, and readers were asked to pass them on, which the authors call snowball sampling. Answers were Likert type, from strongly disagree to strongly agree. And the study is cross sectional: it asks many people about the present and looks for relationships among their answers.

@list heading="Fowler's cautions" items="Answers are perceptions@perceptions|The sample may not be representative@representative|Other methods should confirm it@confirm|Commit to production only@commit to production"
Martin Fowler's foreword gives plain cautions. The answers are people's perceptions. He's unsure how representative the respondents are. He wants independent work by other methods to confirm the results. And the book covers the journey from commit to production, not all of software development.

@chapter Four reasons against levels
@art ladder-levels
A maturity model sets out levels and assesses a team against them. The authors give four reasons against it.

@list heading="Against maturity models" items="They aim at arriving@aim at arriving|They are lock-step@lock step|They measure tooling, not outcomes@vanity metrics|They fix a static level@static level"
They aim at arriving, and a transformation has no arrival. They're lock step, as if level one looked the same in every team. They often measure the tooling installed without tying it to an outcome, which the authors call vanity metrics. And they fix a static level, while the industry moves.

@art moving-target
What counted as high performing one year, the authors found, wasn't enough the next.

@chapter What predicted performance
@list heading="Did not predict performance" items="Age and technology of the application@age and technology|Who performed deployments@who performed|A change approval board@change approval board"
So which things matter? Of the factors people often cite, three did not predict performance: the age and technology of the application, mainframe against greenfield; who performed deployments, operations or development; and whether a change approval board was in place.

@art capability-profile
What did predict it, they report, were twenty four capabilities, in five categories: continuous delivery, architecture, product and process, lean management and monitoring, and culture. They're listed in no particular order.

@chapter The value of DevOps
@math heading="2017: high vs low performers" items="46× more frequent deployments@forty six;;440× faster commit to production@four hundred and forty;;170× faster recovery@one hundred and seventy;;⅕ the change failure rate@a fifth"
In twenty seventeen, the authors report, high performers deployed code forty six times as often as low performers, got a commit to production four hundred and forty times as fast, recovered from downtime one hundred and seventy times as fast, and had a fifth of the failure rate.

@words text="Two groups, one year" sub="a comparison of survey respondents"
Keep that in proportion. These are comparisons of two groups of survey respondents in one year. They say what went together, not what will happen to your team.

@chapter Atlas against a ladder
@math heading="Atlas on the lesson's ladder" items="level 1: version control ✓ · deployment automation ✓@level one;;level 2: CI ✓ · test automation ✓ · trunk-based ✗@level two;;level = 1@So the level;;profile: 4 + 1 + 2 + 3 + 4 = 14 of 24@fourteen of twenty four"
The lesson invents a three level ladder, the kind the authors argue against. Team Atlas meets level one: version control and deployment automation. Level two asks for continuous integration, test automation and trunk based development, and Atlas lacks trunk based development. So the level is one. But its profile is fourteen of twenty four, with something in every category.

@art hidden-capabilities
The level hides three capabilities that higher levels ask for: continuous integration, test automation and monitoring. Another nine, among them everything cultural, are on no level at all.

@art two-teams
Now add Brook, with eight capabilities, all in continuous delivery. Brook meets level two, so the ladder puts it above Atlas. The ladder answers which team is higher, not what each should do next. For Atlas that's one capability. For Brook it's the other four categories.

@chapter Where people slip
@list heading="Common slips" items="Thinking a level says where a team is@The first|Ticking the 24 off in order@The second|Reading a finding as a promise@And the third"
The first slip is thinking a level says where a team is. It only says where the first unmet requirement is. The second is reading the twenty four as a checklist to tick in order. And the third is reading a survey finding as a promise about your team.

@chapter Try it
@words text="Cove: VC · deploy automation · CI · tests · trunk-based · monitoring"
Your turn. Cove has version control, deployment automation, continuous integration, test automation, trunk based development and monitoring. Count its capabilities, find its level on the ladder, and name what would lift it to the next. Then say what the level can't tell you.

@end text="Profile a team, not a level"
You can type a team into the profile and read what its level hides, on Learn. That's learn dot get er done dot I O.
