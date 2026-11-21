---
format: long
lesson: logic-and-proof/rules-of-inference
title: Rules of inference: modus ponens, modus tollens and two fallacies
thumb: Valid, or just convincing?
---

@chapter The question
@title text="Rules of Inference" sub="Logic and Proof" art=thumb
If the program has a bug, the test fails. The test failed. So the program has a bug. Sounds right, doesn't it? It isn't. Here's how to tell a valid argument from one that only feels valid.

@chapter Valid and sound
@art domino-row
An argument is valid when its premises can't all be true while its conclusion is false. Put another way, the premises joined by and, implying the conclusion, is a tautology. Validity is a property of form. What the propositions mean never enters.

@art two-foundations
An argument is sound when it's valid and its premises are actually true. Validity is logic. Soundness adds a claim about the world. A valid argument from a false premise proves nothing about the world.

@chapter The standard rules
@math heading="Valid forms" items="modus ponens:  p → q,  p  ⊢  q@modus ponens;;modus tollens:  p → q,  ¬q  ⊢  ¬p@modus tollens;;hypothetical syllogism:  p → q,  q → r  ⊢  p → r@hypothetical syllogism;;disjunctive syllogism:  p ∨ q,  ¬p  ⊢  q@disjunctive syllogism"
Here are the workhorses. Modus ponens: p implies q, and p, so q. Modus tollens: p implies q, and not q, so not p. Hypothetical syllogism chains two conditionals. And disjunctive syllogism: p or q, and not p, so q.

@words text="addition · simplification · conjunction" sub="p ⊢ p ∨ q  ·  p ∧ q ⊢ p  ·  p, q ⊢ p ∧ q"
Three more are almost too simple to mention. Addition, simplification and conjunction. Each rule is a tautology when written as a conditional, and each can be checked by truth table in under a minute. They're worth knowing by name, because a proof that cites them is one someone else can follow.

@art resolution-merge
One deserves a note. Resolution: from p or q, and not p or r, conclude q or r. It's the single rule that automated theorem provers and SAT solvers are built on.

@chapter The two fallacies
@math heading="Affirming the consequent" items="p → q,  q  ⊬  p@from p implies q;;p = F, q = T:  premises T, conclusion F@take p false"
Now the impostors. From p implies q, and q, nothing follows about p. Take p false and q true. Both premises hold, and the conclusion p is false. That's affirming the consequent, and it's invalid.

@math heading="Denying the antecedent" items="p → q,  ¬p  ⊬  ¬q@from p implies q and not p;;p = F, q = T:  premises T, conclusion F@same row"
And from p implies q and not p, nothing follows about q. The same row breaks it: p false, q true. Both premises hold, and the conclusion not q is false. That's denying the antecedent.

@art two-sources
If it rains, the ground is wet. The ground is wet, so it rained? No, a sprinkler wets the ground. It didn't rain, so the ground is dry? No, same sprinkler. Both errors treat the conditional as an if and only if. One uses the converse, the other the inverse.

@chapter Back to the bug
@math heading="p = bug,  q = test fails" items="premises:  p → q,  q@premises;;try p = F, q = T@Try;;p → q = T,  q = T,  p = F@premise one holds;;INVALID: affirming the consequent@affirming the consequent"
So, back to the bug. The premises are p implies q, and q. Try p false, q true. Premise one holds, premise two holds, and the conclusion fails. It's affirming the consequent. And the counterexample isn't artificial: a test can fail because the test itself is wrong.

@words text="Test passed  ⟹  no bug of that kind" sub="modus tollens"
The valid inference here runs the other way. It's modus tollens. The test passed, so there's no bug of the kind that test detects.

@chapter Rules for quantifiers
@list heading="With conditions attached" items="∃x P(x) ⊢ P(c), for a new name c@existential instantiation|P(c) for arbitrary c ⊢ ∀x P(x)@universal generalisation"
Quantifiers have rules too. Two come with conditions. Existential instantiation may only introduce a fresh name. You know something exists, not which thing. The other is universal generalisation.

@art fresh-tag
That fresh name matters. It mustn't be confused with anything already named, because you don't know which thing it is, only that it exists.

@art arbitrary-pick
It needs c to be genuinely arbitrary, with nothing assumed about it. If the argument used some special property of c, the conclusion doesn't extend to every x.

@chapter Where people slip
@list heading="Common slips" items="Confusing validity with truth@The first|Reusing a name for two witnesses@The second|Generalising from a chosen element@the third"
The first slip is confusing validity with truth. A valid argument can carry a false premise to a false conclusion. The second is reusing a name. From some x has P and some x has Q, you can't conclude some x has both. And the third is generalising from an element that wasn't arbitrary.

@chapter Try it
@words text="“If she studied, she passed. She did not study. So she did not pass.”" sub="name it, and give the row that breaks it"
Your turn. If she studied, she passed. She did not study. Therefore she did not pass. Name the form, valid rule or fallacy, and give the assignment that breaks it.

@end text="Check a rule with its table"
You can check each argument form as a truth table and find the row that breaks a fallacy, on Learn. That's learn dot get er done dot I O.
