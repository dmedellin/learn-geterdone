---
format: long
lesson: mind-language-and-meaning/vagueness-and-the-sorites
title: The sorites paradox: four treatments of the heap
thumb: When does sand become a heap?
---

@chapter The heap
@title text="Vagueness and the Sorites" sub="Mind, Language and Meaning" art=thumb
Ten thousand grains of sand are a heap. Take one grain away, and it's still a heap. Keep going, and eventually you're told that no grains at all make a heap. Something has gone wrong. But where?

@words text="Vague" sub="clear cases, clear non-cases, and no sharp line between"
A predicate is vague when it has clear cases, clear non cases, and cases in between, where there seems to be no fact of the matter, and no sharp line. Heap, bald and tall are examples.

@math heading="F(k): k grains are a heap" items="F(10000)@F of ten thousand;;F(k) → F(k − 1)@if k grains;;∴ F(0)@no grains"
Write F of k for, k grains are a heap. The premises are F of ten thousand, and ten thousand conditionals: if k grains are a heap, so are k minus one. By ten thousand steps of modus ponens, the conclusion is F of zero. No grains are a heap.

@art sand-heap
The conclusion is absurd, and the form is valid. So a premise has to go, or the logic. And the conditionals aren't individually doubtful. Taking away one grain can't make the difference between a heap and a non heap. Or if it could, the word wouldn't be the one we use.

@chapter Classical and cutoff
@art grain-staircase
Under classical logic, every conditional is true, and ten thousand steps deliver F of zero. A heap of no grains. That's not a solution, just the problem stated. The other three treatments deny something.

@art sharp-line
A cutoff says there's a number where a heap stops being one, and the conditional there is false. The conclusion is false. The cost is that nobody can say where it is. A defender says our grasp of the word isn't fine enough to tell neighbouring counts apart, so any number we named would be a guess.

@chapter A borderline range
@math heading="Range: 50 to 200 grains" items="150 conditionals indeterminate@a hundred and fifty;;all of them hold:  super-false@super false"
A range says there's a borderline region, say between fifty and two hundred grains, where it's neither true nor false that a count is a heap. The lab reports a hundred and fifty indeterminate conditionals, and the claim that all of them hold is super false. On every sharp line in the region, some conditional fails.

@art borderline-band
The cost is that a disjunction can be true while neither disjunct is, and bivalence fails for the borderline cases.

@chapter Degrees of truth
@math heading="Degrees" items="v(F(k)) = k / 10000@F of k has;;v(F(k) → F(k − 1)) = 9999/10000@each conditional;;after 10000 steps:  1 − 10000 · (1/10000) = 0@after ten thousand"
Under degrees, truth comes in amounts between zero and one. F of k has the value k over ten thousand. And each conditional has nine thousand nine hundred and ninety nine ten thousandths. Each premise is almost perfectly true. But each step can lose one ten thousandth, and after ten thousand, the guaranteed value of F of zero is zero.

@art fading-grains
The cost is that validity no longer carries near truth from premises to conclusion. Ten thousand almost true premises, an argument of an unquestioned form, and a wholly false end.

@chapter Higher-order vagueness
@art blurred-edges
Here's what remains. The range puts sharp edges at fifty and two hundred. But is forty nine definitely not a heap? If the edges are vague, you need a borderline around each, and then around those. The cutoff has a line it concedes can't be found. And the degrees need an exact number for each count, which is a sharp choice too.

@chapter Where people slip
@list heading="Common slips" items="Taking vagueness to be ignorance of a sharp boundary@The first|Thinking precision removes vagueness@The second|Thinking degrees make the paradox disappear@And the third"
The first slip is assuming vagueness must be ignorance of a sharp boundary. That's one treatment, defensible, but not the default. The second is thinking precision removes vagueness. Replacing heap with at least a thousand grains changes the word. And the third is thinking degrees make the paradox disappear. It moves to a loss at each step.

@chapter Try it
@words text="cutoff 5000 · cutoff 1000 · range 50 to 200" sub="then shorten the chain"
Run the heap under all four treatments. Put the cutoff at five thousand, then a thousand, and watch the false conditional move. Then shorten the chain, and watch the degrees treatment's conclusion change. Finally, say which cost you'd least mind paying.

@end text="The same chain, four treatments"
You can run the heap under each treatment yourself, on Learn. That's learn dot get er done dot I O.
