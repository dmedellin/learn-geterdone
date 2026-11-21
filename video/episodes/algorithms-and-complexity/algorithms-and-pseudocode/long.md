---
format: long
lesson: algorithms-and-complexity/algorithms-and-pseudocode
title: What counts as an algorithm? The five requirements
thumb: Precise steps, every time
---

@chapter The question
@title text="Algorithms and Pseudocode" sub="Algorithms and Complexity" art=thumb
You follow algorithms all the time, recipes, directions, the long division you learned at school. But what actually makes a set of instructions an algorithm, and not just good advice?

@art input-output-machine
Here's the short answer. An algorithm is a finite sequence of precise instructions that turns an input into an output. Every word in that sentence is doing work, and if you drop one, something real slips through.

@chapter Five requirements
@list heading="An algorithm has" items="Input from a specified set@input from a specified set|Definiteness@definiteness|Finiteness@finiteness|Output related to the input@an output|Effectiveness@effectiveness"
There are five requirements. It takes input from a specified set. It has definiteness, so every step is unambiguous. It has finiteness, so it stops after finitely many steps. It produces an output with a specified relation to the input. And it has effectiveness, so every step can be performed exactly.

@art ambiguous-fork
Each one rules something out. Definiteness rules out a step like pick a suitable value. Here's a good test: if two people following the description could do different things, it isn't an algorithm yet.

@art endless-loop
Finiteness rules out a loop that might never exit. It has to stop on every valid input. A procedure that might run forever isn't an algorithm, however useful it is.

@words text="Decide whether this program halts" sub="not a step anyone can perform"
And effectiveness rules out a step like decide whether this program halts. That sounds like an instruction, but the last lesson of this course shows nobody can actually perform it, ever.

@chapter Writing it down
@math heading="MAXIMUM(a₁, …, aₙ)" items="max = a₁@start with;;for i = 2 to n:@for i from two;;if aᵢ > max:  max = aᵢ@if a i is bigger;;return max@return max"
To write an algorithm down, the course uses pseudocode. Here's one that finds the largest of n numbers. Start with max equal to a one. Then for i from two to n, if a i is bigger than max, make it the new max. At the end, return max.

@words text="Precise about the method" sub="silent about the language"
Notice what it leaves out. Indentation marks the blocks, equals means assignment, and counting starts at one. There's no semicolon and no type in sight. It's precise enough to analyse, and it doesn't care what language you'd use.

@chapter One problem, three algorithms
@art two-staircases
The same problem can have many algorithms. Take x to the power n, for a positive whole number n. Method A multiplies by x again and again. Method B uses repeated squaring. Method C uses an addition chain, and sometimes does slightly better than B.

@math heading="xⁿ at n = 1000" items="A: repeated multiplication → n − 1 = 999 multiplications@method A;;B: repeated squaring → about 15 multiplications@method B"
All three give the right answer, but look at the cost. At n equal to one thousand, method A does nine hundred and ninety nine multiplications. Method B does about fifteen.

@words text="999 vs about 15" sub="a property of the algorithm, not the machine"
That gap is what this whole course is about. And it's a property of the algorithm, not of the computer you run it on. A faster machine speeds both up, and the gap is still there.

@chapter Correctness first
@art fast-wrong
There's a fixed order to the work. First, show the algorithm is correct. Then measure what it costs. Only then look for a better method. The temptation runs the other way, but optimising something before you know it's right just gives you a faster wrong answer, and the speed makes the error harder to find.

@list heading="The order of work" items="Establish correctness@proves algorithms are correct|Measure the cost@measure the cost|Look for a better method@look for a better method"
That's the shape of the course too. The next lesson proves algorithms are correct. Then the middle lessons measure the cost, with growth rates, bounds, and recursion. And the last few look for a better method, with greedy algorithms and dynamic programming.

@chapter Where people slip
@list heading="Common slips" items="Leaving a step to judgement@The first|Optimising before proving correct@The second|Specifying the output loosely@The third"
The first slip is leaving a step to judgement. Choose a good pivot hides a whole algorithm inside one line. The second is optimising before proving correct. And the third is specifying the output loosely. Find the element doesn't say whether you want the first one, any one, or all of them, and different algorithms answer different questions.

@chapter Try it
@art five-pillars
Here's something to try. Write a recipe you know as pseudocode, then hold it up against the five requirements. Is every step definite? Does it always stop? Does it say exactly what the output is? Wherever it says something like season to taste, you've found a step that isn't one yet.

@end text="Five requirements, one precise method"
The full lesson, with the five requirements and the three ways to compute a power, is on Learn. That's learn dot get er done dot I O.
