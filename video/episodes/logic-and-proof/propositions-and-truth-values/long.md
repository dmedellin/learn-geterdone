---
format: long
lesson: logic-and-proof/propositions-and-truth-values
title: What counts as a proposition? The first rule of logic
thumb: True or false, never both
---

@chapter The question
@title text="Propositions and Truth Values" sub="Logic and Proof" art=thumb
Before logic can do anything, it has to decide what it's allowed to work on. Not every sentence makes the cut. And the reason some sentences are thrown out turns out to be the thing that makes everything later possible.

@chapter The definition
@art two-lamps
A proposition is a declarative sentence that's either true or false, but not both. Its truth value is T or F. Think of a lamp that's either on or off. Never both, never neither, and never it depends.

@words text="p : “17 is prime”" sub="proposition, true"
So seventeen is prime is a proposition, and it's true. We name propositions with lower case letters, p, q, r and s. Those letters are placeholders for whole sentences, not for numbers.

@chapter Four ways to fail
@list heading="Not propositions" items="Not declarative@not declarative|Open@open sentence|Self-referential paradox@paradox|Vague@vague"
Four kinds of sentence fail the definition, each for its own reason. A sentence can be not declarative. It can be an open sentence. It can be a paradox about itself. Or it can be vague.

@art door-and-bubble
What time is it? Close the door. A question and a command assert nothing, so there's nothing to be true or false. A handy test: if you can't sensibly put it is true that in front, stop there.

@art empty-slot
Now take x plus one equals five. It's true when x is four, and false otherwise. It only gets a truth value once x is fixed. That's an open sentence, a predicate, and quantifiers will deal with it later in the course.

@chapter The paradox
@art paradox-loop
Then there's this sentence is false. If it's true, then it's false. If it's false, then it's true. No truth value can be given to it consistently.

@words text="“This sentence is false”" sub="excluded: no consistent value"
And this isn't a technicality. The moment sentences may talk about their own truth, the two valued system breaks. That's why logic is built on a restricted class of sentences, and not on English.

@art fuzzy-boundary
Last, vagueness. He is tall has no boundary to be true or false against. That's a different failure from simply not knowing the answer.

@chapter Unknown is not a third value
@words text="p ∨ ¬p" sub="bivalence: exactly one of T, F"
Classical logic assumes bivalence. Every proposition has exactly one of the two truth values. That's an assumption, not a theorem, and it's what licenses p or not p, the law of the excluded middle.

@art sealed-box
So take there are infinitely many twin primes. Nobody knows its value. But the sentence is still true or false, and our ignorance is a fact about us. The same goes for P equals N P: a sharp claim we can't yet evaluate. Compare that with he is tall, which has no sharp meaning at all.

@words text="Truth ≠ provability" sub="“Every even number greater than 2 is a sum of two primes”"
So truth isn't the same as provability. Every even number greater than two is a sum of two primes is a proposition. Nobody knows its value. It still has one, and no rule in this course needs to know which.

@chapter Sorting six sentences
@math heading="Classify, and give the reason" items="“7 is a prime number.”  →  proposition, T@seven is a prime number;;“Is 7 prime?”  →  no, a question@is seven prime;;“x is a prime number.”  →  no, open in x@x is a prime number;;“7 is prime and 8 is prime.”  →  proposition, F@seven is prime and eight is prime;;“There is a largest prime.”  →  proposition, F@there is a largest prime;;“P = NP.”  →  proposition, value unknown@P equals N P"
Let's sort six. Seven is a prime number: a proposition, true. Is seven prime: no, it's a question. X is a prime number: no, it's open in x. Seven is prime and eight is prime: a proposition, false. There is a largest prime: a proposition, false, thanks to Euclid. And P equals N P: a proposition, with a value nobody knows yet.

@chapter Where people slip
@list heading="Common slips" items="Treating unknown as a truth value@The first|Calling an open sentence false@The second|Confusing vague with unknown@the third"
The first slip is treating unknown as a truth value. A conjecture's value exists whether or not anyone has found it. The second is calling an open sentence false because it's sometimes false. X greater than three isn't false, it has no value at all. And the third is confusing vagueness with ignorance.

@chapter Try it
@words text="Not declarative · open · self-referential · vague" sub="name the reason, not just the verdict"
Your turn. Write down ten sentences and sort them. For every one that fails, name the specific reason: not declarative, open, self referential, or vague. It's not a proposition, without the reason, is the answer that doesn't carry forward.

@end text="Sort sentences, watch the rows double"
You can sort sentences and watch the truth table rows double, on Learn. That's learn dot get er done dot I O.
