---
format: long
lesson: decision-and-rationality/the-allais-paradox-and-the-sure-thing-principle
title: The Allais paradox: two natural choices no utilities can explain
thumb: A and D can't both be right
---

@chapter Two choices
@title text="The Allais Paradox and the Sure-Thing Principle" sub="Decision and Rationality" art=thumb
Here are two choices that most people make the same way. And here's a proof that no set of utilities, whatever they are, can make both of them come out of expected utility.

@list heading="The first choice" items="A: 1M for certain@A pays|B: 10% 5M, 89% 1M, 1% nothing@B pays"
Maurice Allais put these to people in nineteen fifty three. In the first, gamble A pays a million for certain. Gamble B pays five million with probability ten percent, a million with probability eighty nine percent, and nothing with probability one percent. Most people choose A.

@list heading="The second choice" items="C: 11% 1M, otherwise nothing@C pays|D: 10% 5M, otherwise nothing@D pays"
In the second, gamble C pays a million with probability eleven percent, and nothing otherwise. Gamble D pays five million with probability ten percent, and nothing otherwise. Most people choose D.

@art sure-vs-shot
Each choice looks sensible on its own. A gives up a little expected money for certainty, and B risks ending with nothing at all. In the second choice, nobody's certain of anything, so the bigger prize for nearly the same chance is the natural pick.

@chapter A table of tickets
@art hundred-tickets
Lay the gambles out as a hundred tickets. Tickets one to eighty nine are the shared part. Ticket ninety decides the one percent. Tickets ninety one to a hundred decide the ten percent.

@math heading="Tickets 1–89 · 90 · 91–100, in millions" items="A:  1 · 1 · 1@A pays one;;B:  1 · 0 · 5@B pays one;;C:  0 · 1 · 1@C pays zero;;D:  0 · 0 · 5@D pays zero"
Payoffs are in millions. A pays one, one, one. B pays one, zero, five. C pays zero, one, one. And D pays zero, zero, five.

@art shared-column
Read the first column. A and B agree on it, both paying one. C and D agree on it too, both paying zero. The last two columns are identical across the two choices. The only difference between the choices is what the shared tickets pay.

@chapter The sure-thing principle
@words text="Shared states shouldn't matter."
The sure thing principle says that if two acts pay the same in some states, your preference between them should depend only on the states where they differ. The name is Leonard Savage's, from nineteen fifty four, though the principle is older than the name.

@math heading="The two gaps" items="EU(A) − EU(B) = 11/100 · u(1M) − 10/100 · u(5M) − 1/100 · u(0)@The difference between A and B;;EU(C) − EU(D) = 11/100 · u(1M) − 10/100 · u(5M) − 1/100 · u(0)@the difference between C and D"
Expected utility obeys it automatically, because a shared term cancels. The difference between A and B comes out as eleven hundredths of the utility of a million, minus ten hundredths of the utility of five million, minus a hundredth of the utility of nothing. And the difference between C and D is exactly the same expression.

@art one-number
So for any utilities whatever, the two gaps are equal. Preferring A makes the first positive. Preferring D makes the second negative. And one number can't be both.

@chapter With numbers
@math heading="u(0) = 0, u(1M) = 10, u(5M) = 14" items="EU(A) = 10,  EU(B) = 103/10@A scores ten;;EU(C) = 11/10,  EU(D) = 7/5@C scores;;both gaps:  −3/10@both gaps"
Try some utilities: zero for nothing, ten for a million, fourteen for five million. A scores ten, and B scores a hundred and three tenths. C scores eleven tenths, and D scores seven fifths. So both gaps are minus three tenths, in favour of the gamble. These utilities pick B and D.

@art gaps-move-together
Change the utilities, and the gaps move together, always by the same amount. With nothing at zero, preferring A needs five million below eleven tenths of a million's utility, and preferring D needs it above. The rule can prefer A and C, or B and D. It can't prefer A and D.

@chapter A defence of the popular pair
@art regret-weight
What's said for the popular pair isn't foolish. Certainty is a state of mind as well as a payoff. Turn down a sure million and end with nothing, and you may feel a regret that nothing in the second choice can produce. But then regret is part of the outcome, the payoff table should list it, and the choices are no longer about the same payoffs.

@words text="Give up the principle, or revise a choice."
So there are two ways out. Keep the table as stated and give up the sure thing principle, which means giving up expected utility as the measure of these acts. Or keep the principle, and revise one of the two choices.

@chapter Where people slip
@list heading="Common slips" items="Thinking a sure thing earns a premium@The first|Judging each choice alone@The second|Concluding people are simply irrational@the third"
The first slip is thinking a sure thing always earns a premium under expected utility. Certainty carries no bonus of its own. The second is judging each choice alone. The contradiction lives in the pair. And the third is concluding that people are simply irrational. Whether to revise the choices or the rule is the open question.

@end text="Move the utilities, watch both gaps"
You can change the utilities and watch both gaps move together, on Learn. That's learn dot get er done dot I O.
