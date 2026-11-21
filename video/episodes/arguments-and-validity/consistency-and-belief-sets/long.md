---
format: long
lesson: arguments-and-validity/consistency-and-belief-sets
title: When your beliefs can't all be true, and why logic won't say which to drop
thumb: Something must go. Not which.
---

@chapter Can they all be true?
@title text="Consistency and Belief Sets" sub="Arguments and Validity" art=thumb
Here's a different question to ask of a set of beliefs. Not whether they're true, but whether they could all be true together.

@art model-row
A set of sentences is consistent when at least one row of its table makes every member true. That row is called a model of the set. A set with no model at all is inconsistent.

@chapter The smallest case
@math heading="p → q,  p,  ¬q" items="T T:  ¬q is F@In the first;;T F:  p → q is F@second;;F T:  p is F@third;;F F:  p is F@fourth"
Take three sentences. If p then q. P. And not q. If the first two hold, q must hold, and the third denies it. Check the rows. In the first, not q is false. In the second, the conditional is false. In the third and fourth, p is false. Zero rows of four survive. Inconsistent.

@art no-bad-pair
Notice what kind of fact that is. No pair of these sentences clashes. The conditional with p is fine. P with not q is fine. The conditional with not q is fine. The trouble appears only when all three are held at once.

@words text="A valid argument in disguise"
And that set is just modus ponens with its conclusion denied and turned into a premise. That's the general link. If the premises plus the denied conclusion have no model, the argument is valid. Same table, read two ways.

@chapter The smallest failing subset
@art minimal-subset
When a set fails, look for its smallest failing part. A minimal inconsistent subset is one that can't all be true, but becomes possible when any one member is removed. Sentences outside it are innocent of that failure. And adding sentences can never repair an inconsistency, because every failing row already fails.

@chapter The alarm that didn't wake her
@list heading="Four beliefs" items="1. p → q: if it was set, it rang@if it was set|2. q → r: if it rang, she woke@if it rang|3. p: it was set@It was set. And|4. ¬r: she did not wake@she did not wake"
Here's the lesson's example. P is the alarm was set, q is the alarm rang, and r is she woke. The beliefs: if it was set, it rang. If it rang, she woke. It was set. And she did not wake. Zero models of eight.

@art alarm-clock
Chain the first three. It was set, so it rang, so she woke. The fourth belief denies the last link. Something in that story has to be false, but which part? Maybe the alarm was never set. Maybe it rang and she slept through it. Maybe she did wake.

@math heading="Give up one, and a model appears" items="give up 1:  p T, q F, r F@the first;;give up 2:  p T, q T, r F@the second;;give up 3:  p F, q F, r F@the third;;give up 4:  p T, q T, r T@the fourth"
Now give up each sentence in turn. Give up the first, and a model appears: set, didn't ring, didn't wake. Give up the second: set, rang, didn't wake. Give up the third: nothing set, nothing rang, no waking. Give up the fourth: she did wake after all.

@art four-repairs
All four repairs work, and they describe four different worlds. So the smallest failing subset is all four sentences. The table has shown they can't stand together. It hasn't said which one is false.

@chapter The table is neutral
@words text="At least one is false." sub="The table never says which."
That's the part that matters for philosophy. Which to give up is a question about the sentences themselves. How much you trust each, what each costs to lose, what else depends on it. And that neutrality is why a skeptic's valid argument forces you to choose, and can't make the choice for you.

@art consistent-not-true
Consistency is also weaker than truth. The set p or q, not p, if q then r, has exactly one model: p false, q and r true. So they could all be true. Whether they are is a question about the world.

@chapter Where people slip
@list heading="Common slips" items="Looking for the false sentence@The first|Expecting a pair that contradict@The second|Reading consistent as true@the third"
The first slip is looking for the false sentence in an inconsistent set. The table marks no culprit. The second is expecting to find a pair that contradict. The conflict can need all three, or more, which is how a belief system can fail while every belief looks fine beside its neighbours. And the third is reading consistent as true.

@chapter Try it
@words text="p → q, q → r, p ∴ r is valid." sub="Which set is inconsistent?"
Here's one to try. The argument if p then q, if q then r, p, so r, is valid. Write down the belief set that must therefore be inconsistent. Hint: deny the conclusion and add it to the premises.

@end text="Give up one belief at a time"
You can give up each belief in turn and watch a model appear, on Learn. That's learn dot get er done dot I O.
