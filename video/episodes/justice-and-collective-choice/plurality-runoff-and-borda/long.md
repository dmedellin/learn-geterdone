---
format: long
lesson: justice-and-collective-choice/plurality-runoff-and-borda
title: Plurality, runoff and Borda: same ballots, different winners
thumb: Three rules, three winners
---

@chapter The question
@title text="Plurality, Runoff and Borda" sub="Justice and Collective Choice" art=thumb
Majorities can't always be assembled into a ranking. But real elections need a winner anyway, and the rules in use find one in different ways. The fair way to compare them is to hold the ballots fixed, and change only the rule.

@art ballot-stack
Take nine voters and three candidates. Four voters rank A B C. Three rank B C A. And two rank C B A. Keep those nine ballots in front of you throughout. Every rule below reads these same ballots. Only the counting changes.

@chapter Plurality and runoffs
@art first-column
Start with the simplest rule.

@math heading="Plurality: first places" items="A 4,  B 3,  C 2@A has four;;A wins, with fewer than half@fewer than half"
Plurality reads only the first column. A has four first places, B has three, and C has two. So A wins, with fewer than half the voters.

@art runoff-bracket
The two round runoff keeps A and B, the two with the most first places, and asks voters to choose between them using their whole ballots. Four rank A above B, and five rank B above A. So B wins.

@words text="Instant runoff: drop C" sub="its 2 ballots go to B: 5 of 9"
Instant runoff gets there by another road. C has the fewest first places and is removed. Its two ballots pass to their next choice, which is B. And B holds five of the nine ballots.

@chapter Borda
@art points-ladder
The Borda count doesn't eliminate anyone. Each ballot gives two, one and zero points down the ranking, and every point is added up.

@math heading="Borda: 2, 1, 0 points" items="4 voters:  A 8,  B 4,  C 0@four voters;;3 voters:  A 0,  B 6,  C 3@three voters;;2 voters:  A 0,  B 2,  C 4@two voters;;total:  A 8,  B 12,  C 7@In total"
The four voters give A eight and B four. The three voters give B six and C three. The two voters give C four and B two. In total, A has eight, B has twelve, and C has seven.

@words text="B: Borda and Condorcet winner" sub="beats A 5–4 and C 7–2"
So B wins the Borda count. B is also the Condorcet winner, beating A five to four, and C seven to two. Three of the four counts elect B. Plurality alone elects A, a candidate who loses head to head with B.

@chapter Three rules, three winners
@math heading="4: A C B,  3: B C A,  2: C B A" items="plurality:  A,  4 first places@Plurality still;;runoffs:  B,  A loses 4 to 5@The runoff;;Borda:  C,  11 against 8 and 8@The Borda count;;Condorcet:  C beats A 5–4,  B 6–3@C is also"
Change one ballot group, so the four voters rank A C B. Plurality still elects A. The runoff and instant runoff elect B. The Borda count elects C, with eleven points against eight and eight. C is also the Condorcet winner, beating A five to four, and B six to three.

@art eliminated-favourite
Three counts, three winners, from nine ballots. C is never ranked last by anyone, yet both runoff rules eliminate it first, because only two voters put it first. Nothing in the ballots changed between the rules. What changed is which part of the ballots each rule looks at.

@chapter What each rule counts
@list heading="What each rule counts" items="Plurality: enthusiasm@Plurality counts|Runoffs: strength against the strongest rival@The runoffs|Borda: average standing@Borda counts|Condorcet: victories@The Condorcet rule"
Plurality counts enthusiasm, how many voters would be delighted. The runoffs count strength against the strongest rival, but only after first places choose who the rivals are. Borda counts average standing, who most voters place high, whether or not first. The Condorcet rule counts victories, who beats every other candidate, when anyone does.

@chapter Where people slip
@list heading="Common slips" items="Treating most first choices as the people's choice@The first|Speaking of the winner without naming the rule@The second|Expecting a runoff to rescue the Condorcet winner@And the third"
The first slip is treating the most first choices as the people's choice. A lead of four in nine can be a majority's last choice. The second is speaking of the winner without naming the rule. The winner belongs to a profile and a rule together. And the third is expecting a runoff to rescue the Condorcet winner. It can knock that candidate out first. A runoff lets first places decide who reaches the contest, so a candidate everyone finds acceptable, but few adore, never gets to it.

@chapter Try it
@art same-ballots-four-rules
Work through the second profile yourself. Four A C B, three B C A, two C B A. Count first places, run the head to head, then add the Borda points. Check you get A, then B, then C. Then count every pair, and confirm C is the Condorcet winner.

@end text="Same ballots, different rule"
You can switch the rule and watch the winner move, on Learn. That's learn dot get er done dot I O.
