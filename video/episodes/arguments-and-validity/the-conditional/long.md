---
format: long
lesson: arguments-and-validity/the-conditional
title: If-then in logic: the one row that makes it false
thumb: False in one row only
---

@chapter A promise
@title text="The Conditional" sub="Arguments and Validity" art=thumb
If it rains, the match is off. That's a promise. So here's the question that decides the whole table: when exactly is that promise broken?

@art broken-promise
It's broken in one way only. It rains, and the match goes ahead anyway. If it doesn't rain, nothing has been violated, whether the match goes ahead or not. The promise was about what follows rain.

@chapter The table
@math heading="p → q" items="T T  →  T@both true;;T F  →  F@p true and q false;;F T  →  T@p false and q true;;F F  →  T@both false"
In logic, if p then q is written with an arrow. P is the antecedent, the condition. Q is the consequent. Both true: true. P true and q false: false. P false and q true: true. Both false: true. It's false in exactly one row.

@math heading="The same column" items="p → q  ≡  ¬p ∨ q@not p, or q"
In fact, if p then q has the same column as not p, or q. That's false only when p is true and q is false. A sentence that rules out one case, and is silent about the rest, is true in the rest.

@chapter Why false antecedents give true
@art rain-and-match
The row that looks odd is the third. It didn't rain, and the match was called off anyway, perhaps because a ground was flooded. The promise didn't say the match would be on whenever it was dry. It was kept, so the sentence is true there.

@math heading="If n is divisible by four, n is even" items="n = 6:  antecedent F, consequent T@For six;;n = 3:  antecedent F, consequent F@for three"
Here's an independent check. Every number divisible by four is even. As a conditional about a number n: if n is divisible by four, then n is even. For six, the antecedent is false and the consequent true. For three, both are false. The claim is plainly true of every number, so it can't be false at six or at three.

@chapter Translating
@list heading="All of these say p → q" items="if p, then q@if p, then q|q if p@q if p|p only if q@p only if q|p is sufficient for q@sufficient|q is necessary for p@necessary"
Most of translation is deciding which part is which. All of these say if p then q. If p, then q. Q if p. P only if q. P is sufficient for q. And q is necessary for p.

@art only-if-gate
If, and only if, run opposite ways. You may vote only if you're registered says voting requires registration. So voting, then registered. You may vote if you're registered says registration is enough. So registered, then voting. And p unless q says that if q fails, then p.

@list heading="Translate in four moves" items="Name the two parts@Name the two parts|Find the part that is required@find the part|Choose the form from the word@choose the form|Check the one false row@check the one false row"
So when you translate, decide which part is the condition before you decide on the word. Name the two parts. Then find the part that's required, the one that can't fail while the other holds. That's the consequent. Then choose the form from the word. And finally, check the one false row.

@art falsifying-row
That last move is the safety net. Describe the false row in plain English, antecedent true and consequent false, and ask whether it's exactly the case the sentence forbids. If it is, your arrow points the right way.

@chapter The converse
@art converse-swap
Swap the parts, and you get the converse, a different sentence. If a shape is a square, it has four sides. True. If it has four sides, it's a square. False. A conditional and its converse disagree in two rows, not one: p true with q false, and p false with q true.

@chapter Where people slip
@list heading="Common slips" items="Thinking a false antecedent makes it false@The first|Reversing only if@The second|Taking the converse to say the same thing@the third"
The first slip is thinking a conditional with a false antecedent is false, or has no value. The table says true in both those rows. The second is reversing only if. P only if q is if p then q. Only if names the requirement. And the third is taking the converse to say the same thing.

@art four-sides
Keep the shapes in mind for that last one. Every square has four sides, but plenty of four sided shapes aren't squares. Being a square is sufficient for four sides. Four sides is necessary for being a square, and not enough.

@chapter Try it
@words text="“You may enter only if you have a ticket.”" sub="e: enter · t: ticket"
Here's one to try. You may enter only if you have a ticket. Let e be entering, and t be having a ticket. Which way does the arrow go? Find the row where someone breaks the rule, and check it's the one false row of your conditional.

@end text="Compare a conditional with its converse"
You can compare a conditional with its converse, row by row, on Learn. That's learn dot get er done dot I O.
