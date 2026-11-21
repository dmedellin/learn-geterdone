---
format: long
lesson: accelerate-technical-practices/trunk-based-development
title: Trunk-based development: three thresholds from Accelerate
thumb: Fewer than three, under a day
---

@chapter The finding
@title text="Trunk-Based Development" sub="Accelerate, Chapter 4" art=thumb
How long should a branch live? Chapter four has a surprisingly specific answer, and it holds regardless of team size, organization size or industry.

@quote text="Teams that did well had fewer than three active branches at any time, their branches had very short lifetimes (less than a day) before being merged into trunk and never had “code freeze” or stabilization periods." cite="Forsgren, Humble and Kim, Accelerate, Chapter 4"
Teams that did well had fewer than three active branches at any time, their branches had very short lifetimes, less than a day, before being merged into trunk, and never had code freeze or stabilization periods.

@list heading="Three thresholds" items="Fewer than three active branches@fewer than three|Every branch merged within a day@within a day|No freeze days@no freeze"
So there are three thresholds: fewer than three active branches, every branch merged within a day, and no freeze days. What the authors compare it with is developing on long lived feature branches.

@art freeze-days
A freeze is a day when the team stops adding to the release while it stabilizes. The strongest teams in the survey never needed one, because trunk was kept ready to release all along.

@chapter The objection
@art github-flow
Some developers who use GitHub Flow, which relies on branches merged into trunk only now and then, stay unconvinced. The authors answer in two parts.

@list heading="The authors' answer" items="Short branches merged daily fit CI@consistent with continuous integration|Under a day did better than longer@did better"
First, short lived branches merged into trunk at least daily are consistent with continuous integration. Second, in further research, teams with branch lifetimes and integration periods under a day did better than teams with longer ones.

@art tangled-branches
They hypothesise, from experience and anecdote, that several long lived branches discourage refactoring and communication within a team. And GitHub Flow suits open source projects with part time contributors, whose branches can reasonably live longer.

@chapter Security and adoption
@art security-left
Two short sections follow. High performing teams were more likely to build security into delivery, with security people giving feedback at every stage, without slowing development.

@words text="Architecture is the critical obstacle"
And adopting continuous delivery often means rethinking how teams work, plus substantial investment in test and deployment automation. The authors name architecture as a critical obstacle, and send you to chapter five.

@chapter A month of branches
@art branch-timeline
Now the count. The lesson's lab takes an invented twenty days of a team's branches, each with the time it was created and merged. Fewer than three active means at most two. And a lifetime of exactly a day fails, as less than a day implies.

@math heading="Preset short" items="10 branches · at most 2 open at once@ten branches;;mean lifetime 9 h 48 min@nine hours forty eight;;none a day old · no freezes → meets all three@meets all three"
In the first month, the team opens ten branches and merges every one in under a day. No more than two are ever open at once, the mean lifetime is nine hours forty eight minutes, and there are no freeze days. It meets all three.

@math heading="Preset long: merged lifetimes" items="f1 195 · f2 289 · f3 222 · f5 223 h@one hundred and ninety five;;s1 5 · s2 23 · s3 2 h@five, twenty three;;959 / 7 = 137 h = 5 d 17 h@nine hundred and fifty nine"
In the second, eight branches. Four lived one hundred and ninety five, two hundred and eighty nine, two hundred and twenty two, and two hundred and twenty three hours. Three short ones lived five, twenty three, and two. That's nine hundred and fifty nine hours over seven merged branches: one hundred and thirty seven hours, five days seventeen hours.

@art open-branch
The eighth branch, f four, is still open after at least fourteen days, so it's left out of the mean. Up to five were open at once, five have lived a day or longer, and three days were frozen. It meets none of the thresholds.

@words text="A description, not a guarantee"
Each count is what the log says. The thresholds describe teams that did well in a survey. They don't say why a branch lived long, and a branch may sit open for good reason, like waiting on a decision.

@chapter Where people slip
@list heading="Common slips" items="Trunk-based means no branches@The first|Only for small or modern teams@The second|GitHub Flow is simply wrong@the third"
The first slip is thinking trunk based development means no branches at all. The second is assuming it's only for small or modern teams. And the third is treating GitHub Flow as simply wrong. The objection is to branches that live long.

@chapter Try it
@words text="10 days · branches a to e · e still open"
Your turn. Ten days, five branches, a to e, and e is still open. Work out the most branches open at once, the mean lifetime of the merged ones, and which have lived a day or longer. Which thresholds does it meet, and which branches would you have to change?

@end text="Read your branches against the book"
You can type in a month of branches and check all three thresholds, on Learn. That's learn dot get er done dot I O.
