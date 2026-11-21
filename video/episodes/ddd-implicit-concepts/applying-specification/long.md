---
format: long
lesson: ddd-implicit-concepts/applying-specification
title: One specification, three jobs: validate, select, build to order
thumb: One rule, three jobs
---

@chapter One rule, three places
@title text="Applying and Implementing Specification" sub="Domain-Driven Design, Chapter 9" art=thumb
A specification says whether an object satisfies a rule. Evans's claim at the end of Chapter 9 is that the same object can do three different jobs.

@list heading="Three uses" items="Validation: is this fit?@check whether|Selection: which of these?@choose objects|Building to order: what must be made?@new object"
The three uses are to check whether an object is fit for some purpose, to choose objects from a collection, and to say what a new object must be like.

@quote text="These three uses—validation, selection, and building to order—are the same on a conceptual level." cite="Evans, Domain-Driven Design, Chapter 9"
These three uses, validation, selection, and building to order, are the same on a conceptual level.

@art rule-three-forms
Without a pattern, one rule tends to appear in all three places, in different forms, which can come to contradict each other. With a specification, the model stays one, even where the three implementations have to differ.

@chapter Selection
@art repo-filter
Selection is where it gets interesting. If the objects are few and in memory, a repository can take any specification and return the ones that satisfy it. Usually they're in a relational database, and there are options.

@list heading="Against a database" items="The specification writes SQL@produce its own SQL|A framework queries in model terms@mapping frameworks|Double dispatch to a repository query@double dispatch|A generic query, filtered in memory@generic query"
The specification can produce its own SQL, which keeps the rule in one place but leaks the tables into the domain. Some mapping frameworks let a query be stated in model terms. The repository can offer a specialised query that the specification chooses by double dispatch. Or a generic query, filtered in memory, at some cost in performance. None of these changes the model.

@chapter Building to order
@art generator-spec
Building to order turns it around. The specification describes objects that aren't there yet, as a buyer's requirements describe an aircraft no one has designed. A generator written as a procedure defines its behaviour only implicitly. One that takes a specification states what's wanted, where callers can read it, and the same specification can check the result.

@code block=1 lines=1-19 label=Java focus="2@one lot|5-7@satisfying|11-13@told what|15-18@checked"
Here are all three on a seed bank. Validation asks about one lot. Selection hands the rule to the repository, through satisfying. And building to order: the assembler is told what, not how, and its result is checked against the same specification.

@art warehouse-prototype
The book's warehouse example shows the order of work: validation first, to make the rules explicit and to test the packer. Then a service interface stated in specifications. Then a deliberately naive prototype behind it, so two teams could each work against something real.

@chapter Select seed lots
@art seven-lots
Back to the seed bank, now with all seven of its lots. The lab's select view takes a specification, and reports the lots that satisfy it, and for each one refused, its first false clause.

@math heading="distributable · 7 lots" items="selects 2: lot-01, lot-06@selects two;;lot-03, lot-07: germination@germination;;lot-02: moisture · lot-04: age · lot-05: quarantine@one reason each"
The bank's rule selects two, lot one and lot six. Of the five refused, lot three and lot seven fail first on germination. Lot two on moisture, lot four on age, and lot five on quarantine. One reason each, in the rule's own terms.

@math heading="school-garden" items="germination ≥ 80 and age ≤ 6@at least eighty;;selects 3: lot-01, lot-03, lot-05@three lots;;lot-05 is in quarantine@quarantine"
A school asks for seed for its garden: germination at least eighty, and at most six years old. Written as just that, it selects three lots: one, three and five. But lot five is in quarantine.

@art lost-clause
The request was written as a new rule, and left out a clause the bank's own rule always carries. Add it, and the safe version selects two, lot one and lot three, with lot five refused at quarantine. The bank's rule turned up again in a new guise, and lost a clause on the way.

@chapter Where people slip
@list heading="Common slips" items="A separate rule for each use@The first|It must run in memory@The second|Building to order is a different pattern@And the third"
The first slip is writing a separate rule for each use, until they disagree. The second is thinking a specification must be evaluated in memory. And the third is treating building to order as a different pattern. It's the same concept, used the other way round.

@chapter Try it
@words text="moisture ≤ 7 and (kind = herb or age ≤ 3)"
Your turn. Take the seven lots, and this rule: moisture at most seven, and either the kind is herb or the age is at most three. Find the lots it selects, and which are refused on moisture.

@end text="Select the lots"
Then type the rule into the lab and read the clause it blames for each of the rest, on Learn. That's learn dot get er done dot I O.
