---
format: long
lesson: justice-and-collective-choice/majority-rule-and-the-condorcet-paradox
title: The Condorcet paradox: when the majority goes in a circle
thumb: A beats B beats C beats A
---

@chapter The question
@title text="Majority Rule and the Condorcet Paradox" sub="Justice and Collective Choice" art=thumb
With two candidates, majority rule is simple. The one more voters prefer wins. But with three or more, there are several contests at once. Can majority rule rank them all? Sometimes it can't, even when every voter is perfectly consistent.

@art pairwise-contests
The first thing to do is count. For each pair of candidates, count the voters on either side. A Condorcet winner is a candidate preferred to each other candidate by a majority. It's named for Condorcet, who observed in the eighteenth century that there may be none.

@chapter A Condorcet winner
@math heading="Seven voters" items="3:  A B C,   2:  B C A,   2:  C B A@three rank;;A vs B:  B wins 4 to 3@A meets B;;B vs C:  B wins 5 to 2@B meets C;;B is the Condorcet winner@So B is"
Take seven voters. Three rank A B C, two rank B C A, and two rank C B A. A meets B: three put A higher, four put B higher, so B wins four to three. B meets C: five voters rank B higher, against two. So B is the Condorcet winner.

@words text="Most first places: A" sub="Condorcet winner: B"
Notice that it isn't the candidate with the most first places. That's A. Being first on the most ballots and beating everyone head to head are different things.

@chapter Three voters
@art three-rankings
Now change the voters. Let there be three, with rankings A B C, B C A, and C A B. Each is a perfectly ordinary order of the three candidates. Nobody here is confused.

@math heading="Count the contests" items="A vs B:  voters 1 and 3,  A wins 2–1@A against B;;B vs C:  voters 1 and 2,  B wins 2–1@B against C;;C vs A:  voters 2 and 3,  C wins 2–1@C against A"
A against B: voters one and three rank A higher, so A wins two to one. B against C: voters one and two rank B higher, so B wins two to one. C against A: voters two and three rank C higher, so C wins two to one.

@art cycle-arrows
A beats B, B beats C, and C beats A. That's the Condorcet paradox. The majority goes in a circle, and there's no best candidate, and no order at all.

@chapter Not a tie
@art not-a-tie
A cycle isn't a tie. Every contest has a clear winner, two to one. The three candidates aren't equal. Each is beaten by one rival and beats another, and nothing in the votes breaks the circle.

@chapter A group money pump
@art money-pump
No voter prefers A to B, B to C, and C to A. So no voter is irrational. But the group, taken as a chooser, has exactly the cyclic preference the money pump exploits. Offer it B in exchange for A, and a majority accepts. Then C for B. Then A for C.

@chapter One voter away
@math heading="Five voters" items="3:  A B C,   1:  B C A,   1:  C A B@five voters;;A beats B 4–1,  C 3–2@A wins every;;move one A B C voter to C A B@move one;;C beats A 3–2:  the circle closes@circle closes"
Add two A B C voters to the cycle, so five voters rank A B C three times, B C A once, and C A B once. A wins every contest, beating B four to one and C three to two. Now move one A B C voter to C A B. The contest between A and C flips to three against two for C, and the circle closes. A cycle can be one voter away.

@words text="Two limits" sub="the profile typed · two candidates never cycle"
Two limits apply. The lab reports the cycle for the profile you type. How likely such profiles are in real elections is a different question. And this isn't an argument against majority rule with two candidates, where no cycle can occur.

@chapter Where people slip
@list heading="Common slips" items="Believing majority rule always gives a ranking@The first|Taking a cycle for a tie@The second|Blaming the voters@And the third"
The first slip is believing majority rule always produces a ranking. There may be no best candidate, and no order. The second is taking a cycle for a tie. None of the counts are equal. And the third is blaming the voters. Each ranks consistently. The inconsistency comes from combining three consistent orders.

@chapter Try it
@art one-ranking-changed
Try the lesson's last move. In the three voter cycle, change the C A B voter to C B A, and count the contests again. You should find that B now beats A and beats C, each two to one. One ranking moved, and the circle is gone.

@end text="Count every contest"
You can type your own profiles and hunt for cycles, on Learn. That's learn dot get er done dot I O.
