---
format: long
lesson: ddd-supple-design/declarative-design
title: Declarative Design: when a specification controls the software
thumb: Does the new rule subsume the old?
---

@chapter The Holy Grail
@title text="Declarative Design" sub="Domain-Driven Design, Chapter 10" art=thumb
Assertions help, but handwritten code can always have a side effect nobody excluded. And much code is boilerplate that adds no meaning and buries the model. Declarative design answers with a precise description that actually controls the software, so another developer can take it at face value.

@art trapped-model
Evans calls generating a running program from the model's properties a kind of Holy Grail. He's met two problems more than once. A declaration language that can't say everything, inside a framework that's hard to go beyond. And generated code mixed with handwritten code, so regenerating destroys work. The common result is a model dumbed down to fit the tool.

@art narrow-framework
Rule engines bring side effects back through control predicates added for performance. Domain specific languages link tightly to the Ubiquitous Language, but then refining the model means changing a language. The greatest value he's seen comes from a narrowly scoped framework that automates one tedious part, like object relational mapping, and leaves the rest free.

@chapter A declarative style
@quote text="A supple design can make it possible for the client code to use a declarative style of design." cite="Evans, Domain-Driven Design, Chapter 10"
Then the turn. A design with intention revealing interfaces, functions and assertions is already edging into declarative territory. A supple design can make it possible for the client code to use a declarative style of design.

@code block=1 lines=1-14 focus="5-7@and|8-10@or|11-13@not"
The book shows it on Specification, an adaptation of the predicate. Predicates combine with and, or and not, and each returns a new Spec and changes nothing.

@art combinators
Combine two specifications and you get a specification. So and, or and not are closed under specifications. That's Closure of Operations again, giving you a declarative style without a framework.

@quote text="Don't be afraid to implement only AND, if that is all you need." cite="Evans, Domain-Driven Design, Chapter 10"
Evans is careful about cost. On one project a more elaborate version made millions of small objects and slowed the database. And often the full set isn't needed. Don't be afraid to implement only AND, if that is all you need.

@chapter Subsumption
@art stricter-inside-looser
Subsumption compares two specifications. His case is a regulation that tightens. A stricter specification subsumes a looser one if everything satisfying it satisfies the other. Proving it in general is hard, but with and alone it's easy: one conjunction subsumes another when its clauses include all of the other's.

@words text="Does A accept every candidate B accepts?" sub="yes: B subsumes A"
One warning about the lab. Logicians say the looser rule subsumes the stricter, and Evans says the reverse. So the lab asks a plain question instead. Does A accept every candidate B accepts? A yes means, in Evans's words, that B subsumes A.

@chapter A seed bank
@art seed-lots
The lab's model is a seed bank whose storage rule has been tightened, with five stored lots, A to E.

@code block=2 lines=1-2 focus="1@old rule|2@new rule"
The old rule asks for moisture at most eight and temperature at most minus ten. The new rule asks for moisture at most six, temperature at most minus eighteen, and sealed.

@math heading="A = old, B = new" items="B accepts lotA · A accepts lotA–lotD@Only lot A;;0 counter-examples · logically, yes@no counter examples"
On the preset tightened, the old rule is A and the new is B. Only lot A satisfies the new rule, while lots A to D satisfy the old. Lot A satisfies both, so there are no counter examples. And since both are conjunctions, the lab gives a logical yes. The new rule subsumes the old.

@math heading="swapped: A = new, B = old" items="3 counter-examples: lotB, lotC, lotD@three counter examples;;lotE satisfies neither@satisfies neither"
Swap them, and ask whether the old rule subsumes the new. No. Three counter examples, lots B, C and D, satisfy the old rule and fail the new, each for a different clause. Lot E satisfies neither. Those three are the lots the tightening affects.

@chapter When or arrives
@math heading="B with an or" items="(moisture ≤ 6 and sealed = yes) or temp ≤ −25@give B an or;;lotA, lotC: 0 counter-examples · not decidable@not decidable;;lotF: sealed, moisture 4, 0 degrees → fails A@lot F"
Now give B an or: moisture at most six and sealed, or temperature at most minus twenty five. Lots A and C satisfy it, and both satisfy the old rule. No counter examples, but the lab says the logical answer is not decidable. And it's in fact no. Add lot F, sealed, moisture four, kept at zero degrees, and it fails the old rule.

@chapter Where people slip
@list heading="Common slips" items="Generating the whole program@The first|Building every operator@The second|No counter-example as proof@And the third"
The first slip is taking declarative design to mean generating the whole program. The second is building every operator because the pattern describes it. And the third is reading no counter example as proof of subsumption. Only for pure conjunctions does the lab give a logical answer.

@chapter Try it
@code block=3 lines=1-2 focus="1@loyal member|2@regular visitor"
Your turn. Two rules for a theatre's loyalty discount. Loyal member: at least ten visits and a member. Regular visitor: at least six visits. Say which subsumes the other in Evans's sense, and give a candidate that satisfies one and not the other.

@end text="Mind which rule is A"
Then enter the rules and candidates in the lab, on Learn. That's learn dot get er done dot I O.
