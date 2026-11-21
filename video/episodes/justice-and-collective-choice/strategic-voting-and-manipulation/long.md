---
format: long
lesson: justice-and-collective-choice/strategic-voting-and-manipulation
title: Strategic voting: when an honest ballot doesn't pay
thumb: Bury the rival
---

@chapter The question
@title text="Strategic Voting and Manipulation" sub="Justice and Collective Choice" art=thumb
A voting rule is a procedure, and any procedure invites the question of whether it can be used against its own purpose. A voter who knows the rule, and the likely ballots of others, can choose a ballot to get the best result. And the best ballot isn't always the true one.

@words text="Manipulable at a profile" sub="some voters gain by reporting a ranking they don't hold"
A rule is manipulable at a profile when some group of voters can get an outcome they prefer, by their true rankings, by reporting rankings other than their own.

@chapter Burying under Borda
@math heading="Seven voters, Borda 2, 1, 0" items="2: A B C,  2: B C A,  3: C B A@two rank;;A 4,  B 9,  C 8:  B wins@A gets four;;C is 1 point short@one point short"
Take seven voters. Two rank A B C, two rank B C A, and three rank C B A. Under the Borda count, A gets four, B gets nine, and C gets eight. So B wins. The three voters who rank C first prefer C to B, and C is one point short.

@art bury-rival
Suppose they report C A B instead of C B A. They still give C its two points, but now give B nothing, and give A a point.

@art score-bars
If two of the three do this, B falls to seven, A rises to six, and C keeps eight. So C wins. Nothing about C's support increased. B's total was lowered by ranking it where it didn't belong. That's burying. And one voter alone can't do it, because B would still tie C at eight.

@chapter The spoiler's dilemma
@math heading="Plurality" items="2: A C B,  3: B C A,  2: C B A@two voters ranking;;B wins, 3 first places@B with three;;A voters report C A B:  C 4,  C wins@reporting C A B"
Plurality offers a different route. Take two voters ranking A C B, three B C A, and two C B A. Plurality elects B with three first places. The two voters who rank A first prefer C to B. Their favourite can't win, but by reporting C A B, they give C four first places, and elect it.

@art spoiler-choice
That's the spoiler voter's dilemma. Vote for your favourite and get your worst, or vote for your second choice. Under Borda, the same profile elects C without any misreport, and a different group gains.

@chapter Not lying about facts
@art honest-ballots
Notice what's happening here. No one states a false fact about the world. A voter hands in a ranking, which only they hold, and the rule counts it as given. The question is whether the rule rewards the misreport. That's a property of the rule and the profile.

@chapter The one safe setting
@art two-candidates
With two candidates, there's nothing to bury, and no one to switch to. A voter who ranks A above B can report that, or the reverse, and the reverse can only help B. With three voters at A B and two at B A, the lab finds no group that gains under any rule.

@chapter The theorem
@words text="Gibbard–Satterthwaite" sub="3+ candidates, any can win, no dictator ⟹ manipulable somewhere"
The Gibbard Satterthwaite theorem is Arrow's companion. With at least three candidates, if a rule picks one winner, every candidate can win under some profile, and no voter is a dictator, then at some profile some voter gains by misreporting.

@art information-lens
So manipulability isn't a defect of plurality or Borda in particular. What the theorem leaves open is how often a profile is manipulable, how much the manipulators need to know, and how costly the manipulation is to find. The lab assumes they know every ballot, the most favourable case for them.

@chapter Where people slip
@list heading="Common slips" items="Treating strategic voting as lying about facts@The first|Assuming sincere voting is always safe@The second|Taking none found as proof a rule resists@And the third"
The first slip is treating strategic voting as lying about facts. The second is assuming voting sincerely is always safe. The sincere A voters elected their last choice. And the third is taking none found as proof that a rule resists manipulation. It covers one profile only.

@chapter Try it
@words text="Move one C B A voter to B C A" sub="Borda winner: still B · manipulation: none found"
Try the lesson's change. In the Borda profile, move one voter from C B A to B C A. Recount, then search for a profitable misreport. The winner's still B, but now none is found. The two voters left who rank C first can't lower B enough.

@end text="Search for a profitable misreport"
You can search for manipulations on your own profiles, on Learn. That's learn dot get er done dot I O.
