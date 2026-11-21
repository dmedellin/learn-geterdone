---
format: long
lesson: science-induction-and-causation/the-raven-paradox
title: The raven paradox: does a white shoe confirm that all ravens are black?
thumb: Yes, by one nine-hundredth
---

@chapter A white shoe
@title text="The Raven Paradox" sub="Science, Induction and Causation" art=thumb
Can you study birds without leaving your room? Here's a famous argument that says a white shoe confirms that all ravens are black.

@math heading="Two equivalent hypotheses" items="every x:  R(x) → B(x)@if x is a raven;;every x:  ¬B(x) → ¬R(x)@if x is not black"
Write R for is a raven, and B for is black. The hypothesis says, for every x, if x is a raven, x is black. Its contrapositive says, for every x, if x is not black, x is not a raven. Their truth table columns agree on every row, so they're equivalent.

@art contrapositive-flip
So the same claim can be pictured two ways. Every raven sits inside the black things. Or, flipping the view, everything outside the black things sits outside the ravens.

@chapter The argument
@list heading="Two conditions" items="Nicod: an F that is G confirms all F are G@Nicod's condition|Equivalence: what confirms one confirms its equivalents@equivalence condition"
Now two principles. Nicod's condition: an object that is F and G confirms all F are G. So a black raven confirms the hypothesis. And the equivalence condition: evidence that confirms one hypothesis confirms every hypothesis logically equivalent to it.

@art shoe-instance
Run the argument. A white shoe is a non black non raven. By Nicod, it's an instance of the contrapositive, so it confirms it. By equivalence, it confirms the original. So a white shoe confirms that all ravens are black, and you need never leave the room.

@chapter Measure it
@words text="Confirmation depends on how the object was found."
Each condition is hard to reject. What you can reject is the assumption that the conclusion is absurd, once confirmation is measured. Confirmation depends on a likelihood, and the likelihood depends on how the object was found.

@art ten-ravens
So build a world. There are ten ravens. If the hypothesis is true, all ten are black, and the non black things number nine hundred, none of them a raven. If it's false, exactly one raven isn't black, so there are nine hundred and one non black things, and one of them is a raven. Give the hypothesis a prior of a half.

@math heading="Sample a non-black thing: it's not a raven" items="under H:  900/900 = 1@Under the hypothesis;;under not H:  900/901@nine hundred over nine hundred and one;;Bayes factor:  901/900@nine hundred and one over nine hundred"
First, pick a non black thing at random, and find it's not a raven, a white shoe. Under the hypothesis, that had probability one. Under its negation, nine hundred over nine hundred and one, since one of those things would have been a raven. So the Bayes factor is nine hundred and one over nine hundred.

@math heading="Sample a raven: it's black" items="under H:  1@Under the hypothesis, one;;under not H:  9/10@nine tenths;;Bayes factor:  10/9@ten ninths"
Second, pick a raven at random, and find it's black. Under the hypothesis, one. Under its negation, nine tenths. The factor is ten ninths.

@chapter Both confirm, unequally
@art two-factors
Both factors are above one, so both confirm. But the shoe's exceeds one by a nine hundredth, and the raven's by a ninth, a hundred times as much. The paradox dissolves, because confirms was being heard as confirms appreciably.

@art sampled-class
And the asymmetry isn't a property of shoes. It comes from the size of the sampled class. There are very many non black things for a counterexample to hide among, and few ravens. Choose a different class to sample from, and the numbers move.

@chapter Good's twist
@art bird-crowd
Good pressed this further. If the hypothesis being true would mean there are few ravens, and its being false would mean a great many, then a black raven drawn from all the birds is more probable when the hypothesis is false. Its factor falls below one, and it disconfirms.

@chapter Where people slip
@list heading="Common slips" items="Treating confirmation as all or nothing@The first|Thinking indoor ornithology works@The second|Rejecting the equivalence condition@the third"
The first slip is treating confirmation as all or nothing. Asking only whether evidence confirms loses the one number that tells the cases apart. The second is thinking the paradox shows indoor ornithology works. A shoe picked for its colour, with no route to a raven, isn't a random sample of non black things. And the third is rejecting the equivalence condition to escape. That would make a theory of evidence about the wording, not the hypothesis.

@chapter Try it
@words text="Fix the sample, then compute the factor"
Here's one to try. Imagine a world with a thousand ravens instead of ten. Decide what you'd sample from, write the two likelihoods, and compare the factors for a shoe and a raven again.

@end text="Edit the world, compare the factors"
You can edit the likelihoods and compare the shoe and the raven yourself, on Learn. That's learn dot get er done dot I O.
