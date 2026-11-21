---
format: long
lesson: logic-and-proof/direct-proof
title: Direct proof: assume the hypothesis, reach the conclusion
thumb: Assume p, arrive at q
---

@chapter The question
@title text="Direct Proof" sub="Logic and Proof" art=thumb
How do you actually prove that if p, then q? The default method is simple to state. Assume p, and reason forward until you reach q. Most of the difficulty isn't logic at all. It's writing, because a proof's job is to convince a careful reader.

@chapter The shape
@art forward-path
Almost every theorem is a for all statement about a conditional. For all x, if P of x, then Q of x. A direct proof takes an arbitrary x that satisfies P, and derives Q of x through a chain of steps. Each step is justified by a definition, a result already proved, or a rule of inference.

@list heading="The template" items="Let x be arbitrary with P(x).@Let x be arbitrary|Reason, justifying each step.@justify each step|Therefore Q(x), for all x.@Therefore"
So the template is three lines. Let x be arbitrary, with P of x. Reason forward, and justify each step. Therefore Q of x, and since x was arbitrary, the claim holds for all x.

@chapter Odd plus odd
@math heading="If m and n are odd, then m + n is even" items="m = 2j + 1,  n = 2k + 1@By definition of odd;;m + n = (2j + 1) + (2k + 1)@Then m plus n;;= 2j + 2k + 2 = 2(j + k + 1)@two times;;j + k + 1 is an integer, so m + n is even@twice an integer"
Let m and n be arbitrary odd integers. By definition of odd, m is two j plus one, and n is two k plus one. Then m plus n is two j plus one, plus two k plus one. That's two times, j plus k plus one. That's twice an integer, so m plus n is even.

@art unfold-box
Notice how much of that is managing definitions. Odd was replaced by two j plus one straight away. The algebra was routine. And the last step recognised the result as matching the definition of even. Symbols can be manipulated. Adjectives can't.

@art two-tokens
And there are two letters, j and k, for a reason. m and n are different numbers. Use one letter for both, and you've only proved the case where m equals n.

@chapter Divides, twice
@math heading="If a | b and b | c, then a | c" items="a | b  ⟹  b = a·j@a divides b;;b | c  ⟹  c = b·k@b divides c;;c = b·k = (a·j)·k = a·(j·k)@Substitute;;j·k is an integer, so a | c  ∎@is an integer"
A divides b means b equals a times some integer. So, a divides b gives b equals a j. And b divides c gives c equals b k. Substitute: c equals a j times k, which is a times j k. And j k is an integer, so a divides c. Again, two letters, because the two factors have no reason to be equal.

@chapter What a proof owes its reader
@list heading="A written proof" items="States the claim in full@First|Introduces every variable@introduce every variable|Justifies each step by name@by name|Says when it's done@Say when"
A proof is prose with symbols in it, written in full sentences. First, state what's being proved, in full. Introduce every variable as it appears. Justify each step by name: by definition, by hypothesis. And say when you're done, and what you've established.

@art open-book
A step whose justification you can't state is a step you haven't made. If it's obvious, the justification is one clause long. If you can't write that clause, it wasn't obvious. It was unexamined.

@chapter Assuming what you prove
@words text="“n is even, so n = 2k, so n² = 4k² is even”" sub="claimed: if n² is even then n is even"
Here's the most common flawed proof in this course. The claim is: if n squared is even, then n is even. The proof says n is even, so n is two k, so n squared is four k squared, which is even. But that started from the conclusion. It proves the converse instead.

@art circle-arrow
So keep the assumption you made apart from the conclusion you reached. Confusing them is how a proof quietly becomes circular.

@art detour-road
And if a direct proof stalls, that's information. Being unable to get from p to q going forwards often means the natural route runs backwards, through the contrapositive. That's the next lesson.

@chapter Where people slip
@list heading="Common slips" items="Assuming the conclusion@The first|Proving one case and claiming all@The second|Skipping a step because it's obvious@the third"
The first slip is assuming the conclusion. Start from p. The second is proving one case and claiming all. Let n equal four proves a fact about four. And the third is skipping a step because it's obvious.

@chapter Try it
@words text="If n is an odd integer, then n² is odd." sub="then hand it to someone"
Your turn. Prove that if n is an odd integer, then n squared is odd. Then hand it to someone, and watch where they hesitate. That's where a justification is missing.

@end text="Check a claim before you prove it"
You can test a claim on many values before you try to prove it, on Learn. That's learn dot get er done dot I O.
