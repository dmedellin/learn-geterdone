---
format: long
lesson: arguments-and-validity/validity-and-soundness
title: Valid but false? Validity and soundness, kept apart
thumb: Valid is not the same as true
---

@chapter Two questions
@title text="Validity and Soundness" sub="Arguments and Validity" art=thumb
There are two questions you can ask about any argument, and the whole subject depends on keeping them apart.

@words text="Could the premises be true and the conclusion false?" sub="Are the premises in fact true?"
The first: could the premises be true while the conclusion is false? The second: are the premises in fact true? You can settle the first by looking at cases. The second needs the world.

@chapter Validity
@art banned-combination
An argument is valid when there's no case in which every premise is true and the conclusion is false. Otherwise it's invalid, and any one such case shows it. So validity is a ban on exactly one combination: true premises with a false conclusion.

@art four-combinations
Every other combination can turn up in a valid argument. A valid argument can have false premises and a false conclusion. It can have false premises and a true conclusion. Only that one pairing is ruled out.

@chapter Soundness
@art valid-plus-world
An argument is sound when it's valid and every premise is true. Otherwise it's unsound, which means one of two things. Either it's invalid, or it's valid with at least one false premise.

@chapter Two examples
@list heading="Valid and unsound" items="All whales are fish.@All whales are fish|All fish fly.@All fish fly|So all whales fly.@So all whales fly"
All whales are fish. All fish fly. So all whales fly. Suppose the premises were true. Then whales would be among the fish, and the fish among the fliers, so whales would fly. No case has the premises true and the conclusion false. It's valid.

@art whales-and-fish
But check the premises against the world, and the first one fails at once. Whales are mammals, not fish. So the argument is valid and unsound. The form was fine. What went wrong was a premise, and that's a different question, answered somewhere else.

@list heading="Invalid, every sentence true" items="Paris is in France.@Paris is in France|So Rome is in Italy.@So Rome is in Italy"
Now the opposite. Paris is in France. So Rome is in Italy. Every sentence is true, and the argument is invalid. It's easy to describe a case with the premise true and the conclusion false, because nothing ties one sentence to the other.

@chapter What the lab can see
@math heading="Three presets" items="same:  p ⊢ p  →  2 cases, valid@p, so p;;other:  q ⊢ p  →  4 cases, one with q T, p F@q, so p;;both:  p, q ⊢ q  →  4 cases, valid@p and q, so q"
The lesson's lab only looks at cases. Take p, so p. Two cases, and in neither is the premise true and the conclusion false. Valid, whatever p says. Take q, so p. Four cases, and in one, q is true and p false. That single case is all the invalidity there is. And p and q, so q, has four cases and no such row, because q is one of the premises.

@art lab-blind-spot
If p is whales fly, then p, so p is valid and unsound. The lab has no way to know that, because no claim about whales ever enters the check. It can settle validity. It can't settle soundness.

@chapter Using a valid argument
@art fork-in-the-road
Here's why validity matters. If an argument is valid, accepting all its premises commits you to its conclusion. And rejecting its conclusion commits you to rejecting at least one premise. Which of the two to do is a question about the premises, and the table can't answer it.

@words text="Validity guarantees you have to choose."
That's where the lessons ahead begin. A skeptic offers a valid argument whose conclusion is that you know nothing. You can accept the conclusion, or reject a premise. Validity guarantees you have to choose.

@chapter Where people slip
@list heading="Common slips" items="Thinking a valid argument has a true conclusion@The first|Using valid to mean reasonable@The second|Calling an argument invalid because you dislike its conclusion@the third"
The first slip is thinking a valid argument has a true conclusion. Validity is conditional: if the premises are true, so is the conclusion. The second is using valid to mean reasonable. In logic, sentences are true or false, and arguments are valid or invalid. And the third is calling an argument invalid because you dislike its conclusion. If it's valid, a premise has to go, and finding which one is the work.

@chapter Try it
@words text="Valid argument + false conclusion → ?"
Here's one to try. You're sure an argument is valid, and sure its conclusion is false. What follows? Think about the one combination validity bans, and you'll see that at least one premise has to be false.

@end text="Watch the verdict move"
You can retype premises and conclusions and watch the verdict move, on Learn. That's learn dot get er done dot I O.
