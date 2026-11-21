---
format: long
lesson: arguments-and-validity/fallacies-and-the-counterexample-method
title: How to refute a bad argument without a truth table
thumb: Same shape, obviously wrong
---

@chapter The butler or the maid
@title text="Fallacies and the Counterexample Method" sub="Arguments and Validity" art=thumb
Either the butler or the maid did it. The butler did it. So the maid didn't. Sounds like good detective work. It isn't, and here's a method for showing why that needs no table at all.

@art same-shape
The method is simple. To refute a form, write another argument of exactly the same form, with premises that are plainly true and a conclusion that's plainly false. If the shape can lead from truth to falsehood, the shape can't be valid.

@chapter Three valid forms
@list heading="Valid" items="Hypothetical syllogism: p → q, q → r, so p → r@Hypothetical syllogism|Disjunctive syllogism: p ∨ q, ¬p, so q@Disjunctive syllogism|Constructive dilemma: p → q, r → s, p ∨ r, so q ∨ s@Constructive dilemma"
First, three forms worth knowing by name, because they're valid. Hypothetical syllogism chains two conditionals. Disjunctive syllogism rules out one alternative: p or q, not p, so q. Constructive dilemma combines two conditionals with a disjunction. None has a row where the premises hold and the conclusion fails.

@art lookalikes
Two forms look similar and aren't valid. Affirming a disjunct treats an inclusive or as exclusive: p or q, p, so not q. And denying the antecedent: if p then q, not p, so not q.

@chapter Find the row, then fill it
@math heading="p ∨ q, p ∴ ¬q" items="p T, q T:  premises T, T  ·  conclusion F@p true and q true"
Here's the method in full. Find a row of the form's table with every premise true and the conclusion false. For affirming a disjunct, that's p true and q true. Both premises hold, and not q fails.

@art fill-the-letters
Then replace each letter with a real sentence that has the value the row gives it. Arithmetic and geography are good sources, because nobody disputes them. That's the craft of the method.

@words text="“Paris is in France or Rome is in Italy. Paris is in France. So Rome is not in Italy.”"
Here it is. Either Paris is in France or Rome is in Italy. Paris is in France. So Rome is not in Italy. Both premises are true, and the conclusion is false. The shape can't be valid, and no detective story was needed to show it.

@art rainy-tuesday
You can hear the same pattern on a rainy Tuesday. It's raining or it's Tuesday. It's raining. So it's not Tuesday. The argument moves from one alternative to the denial of the other. And back with the butler, the row is simply that they did it together.

@math heading="Denying the antecedent" items="If 6 is divisible by 4, then 6 is even.@If six is divisible by four;;6 is not divisible by 4.@six is not divisible by four;;So 6 is not even.@So six is not even"
It works in conversation too. For denying the antecedent, the row is p false and q true. If six is divisible by four, then six is even. Six is not divisible by four. So six is not even. True, true, false.

@chapter What it shows, and doesn't
@art maid-unsure
But be careful what you've shown. The counterexample is to the form. It doesn't show the maid is guilty. It shows this reason doesn't clear her. The original conclusion may still be true, and established by another route. If nine is divisible by four, nine is even. It isn't. So nine is not even. Same shape, true premises, true conclusion, and invalid still.

@art moon-cheese
And valid forms can have false conclusions. The moon is cheese or Paris is in Germany. The moon is not cheese. So Paris is in Germany. That's disjunctive syllogism, valid, and false at the end. A false conclusion forces a false premise, and here it's the first.

@list heading="What a false conclusion tells you" items="Valid, false conclusion: a premise is false@If a valid argument|True premises, false conclusion: invalid@true premises and a false conclusion|False conclusion alone: nothing about validity@alone settles nothing"
So keep these three apart. If a valid argument has a false conclusion, at least one premise is false. If an argument has true premises and a false conclusion, it's invalid. And a false conclusion alone settles nothing about validity.

@chapter Where people slip
@list heading="Common slips" items="Judging invalid because the conclusion is false@The first|Treating the counterexample as disproving the conclusion@The second|Using an instance with a false premise@the third"
The first slip is judging an argument invalid because its conclusion is false. The table decides, not the conclusion. The second is treating the counterexample as proof that the original conclusion is false. And the third is building a counterexample with a false premise. Check each premise is true, one at a time.

@chapter Try it
@words text="p ∨ q, p ∴ ¬q" sub="p: Paris is in France · q: Rome is in ?"
Here's one to try. For affirming a disjunct, which choice of sentences gives a real counterexample? Try different countries for Rome, and check that both premises come out true and the conclusion false.

@end text="Five forms, one row each"
You can run all five forms and find each counterexample row, on Learn. That's learn dot get er done dot I O.
