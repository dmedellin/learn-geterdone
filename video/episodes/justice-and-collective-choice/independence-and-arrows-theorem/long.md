---
format: long
lesson: justice-and-collective-choice/independence-and-arrows-theorem
title: Arrow's theorem: strike a loser, and the winner changes
thumb: The loser decides
---

@chapter The question
@title text="Independence and Arrow's Theorem" sub="Justice and Collective Choice" art=thumb
The Condorcet paradox showed that one rule, majority rule, can fail to produce a ranking. Arrow asked a bigger question. Is there any rule that turns every profile of rankings into a group ranking, and behaves sensibly?

@art three-conditions
He made sensibly precise with three conditions. Unanimity: if every voter ranks A above B, so does the group. Independence of irrelevant alternatives: the group's ranking of A and B depends only on how each voter ranks A and B. Non dictatorship: no one voter's ranking always becomes the group's.

@chapter Strike a loser
@math heading="Nine voters, plurality" items="4: A B C,  3: B C A,  2: C B A@four rank;;A 4,  B 3,  C 2:  A wins@Under plurality;;strike C:  A 4,  B 5@strike C;;B wins@B wins"
Back to the nine voters. Four rank A B C, three rank B C A, and two rank C B A. Under plurality, A wins with four first places. Now strike C from every ballot. The two C B A voters become B A. Plurality now counts four for A, and five for B, and B wins.

@art struck-ballot
No voter changed a view about A and B. Before, four ranked A above B, and five ranked B above A. After, the same four and the same five. Yet the group's ranking reversed, because the voters who put C first had their first places handed to B.

@words text="C was never going to win" sub="but C decided A against B"
So the presence of C decided the contest between A and B, and C was never going to win. That's a failure of independence.

@art removal-test
The lab's test is a close, visible cousin of Arrow's condition. Strike a losing candidate from every ballot, keep everyone's order of the rest, and recount under the same rule. If the winner changes, independence has failed on that profile.

@chapter Borda fails too
@math heading="2: A C B,  2: B A C,  2: B C A,  3: C B A" items="plurality:  B, 4 first places@Plurality elects;;Borda:  B 11,  C 10,  A 6@Borda also;;Condorcet:  C beats B 5–4,  A 5–4@C beats B"
It's tempting to blame plurality for reading only first places. So take another nine voters. Plurality elects B, with four first places. Borda also elects B, with eleven points against ten for C and six for A. But C beats B five to four, and beats A five to four. C is the Condorcet winner.

@art borda-flip
Now strike A, who loses under every rule. With two candidates left, both plurality and Borda reduce to majority rule between B and C, and C wins five to four. Both rules fail the removal test on this profile.

@chapter The theorem
@words text="3+ candidates: unanimity + IIA ⟹ dictatorship" sub="for rules giving a full group ranking on every profile"
Here's Arrow's theorem. Suppose there are at least three candidates, and a rule turns every profile of complete, transitive rankings into a complete, transitive group ranking. If it satisfies unanimity and independence, it's a dictatorship. Some one voter's ranking is the group's, on every profile.

@list heading="What it doesn't say" items="Elections can't be held@It doesn't say|It applies to two candidates@two candidates|Every rule fails the same way@every rule"
Three things it doesn't say. It doesn't say elections can't be held. It doesn't apply to two candidates, where majority rule satisfies all three. And it doesn't say every rule fails the same way. Borda gives up independence. Majority rule gives up always producing a ranking. And restricting the profiles, say to voters who place candidates on one left to right line, lets majority rule work.

@art single-line
That last one is worth a picture. If every voter places the candidates along one shared line, the cycles can't form, and majority rule works.

@chapter Where people slip
@list heading="Common slips" items="Believing Arrow proved democracy impossible@The first|Reading a failure as a voter changing their mind@The second|Hearing dictator as a tyrant@And the third"
The first slip is believing Arrow proved democracy impossible. What it forbids is getting everything at once. The second is reading an independence failure as a voter changing their mind. Nobody's view of A or B moved. And the third is hearing dictator as a tyrant. A rule that copies the first voter's ballot is a dictatorship by the definition.

@chapter Try it
@art copy-first-ballot
Try the lesson's check. Set the rule to Borda on the first nine voters, and strike each candidate in turn. The Borda winner is B, and the removal test passes on that profile. So independence fails on a profile, not for a rule in general.

@end text="Strike a loser, recount"
You can strike candidates and recount yourself, on Learn. That's learn dot get er done dot I O.
