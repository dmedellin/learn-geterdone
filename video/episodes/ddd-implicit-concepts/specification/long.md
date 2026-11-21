---
format: long
lesson: ddd-implicit-concepts/specification
title: The Specification pattern: a business rule as a value object
thumb: Does this object satisfy it?
---

@chapter Little rules
@title text="Specification" sub="Domain-Driven Design, Chapter 9" art=thumb
Evans developed this pattern with Martin Fowler, and it starts from something you've written a hundred times: a method that returns true or false.

@quote text="In all kinds of applications, Boolean test methods appear that are really parts of little rules." cite="Evans, Domain-Driven Design, Chapter 9"
In all kinds of applications, Boolean test methods appear that are really parts of little rules.

@chapter A test that grows
@art past-due
A method asking whether a bill is past its due date is a one line rule, and it belongs on the bill. Fine.

@art swamped-bill
But a method asking whether a bill is delinquent starts the same way, then needs a grace period from the customer's account, the payment history, policy for different product lines, and the difference between a second notice and a collection agency. The bill's plain meaning disappears under the rules, and it picks up dependencies that have nothing to do with it.

@art rules-move-up
The usual rescue is worse. Developers move the rules out to the application layer. That leaves the domain object a bundle of data, while the rules sit in code that isn't about the model. The rules belong in the domain layer, and they don't fit in the object being tested.

@chapter Borrow the predicate
@words text="A predicate: true or false" sub="combined with and, or"
Logic programming has an answer: rules written as predicates, functions that return true or false and combine with and and or. But a full implementation in objects is a major undertaking, and says little about intent.

@art spec-object
So Evans borrows only the concept. A small, specialised value object that evaluates to true or false, and can be asked about another object. That's a specification. It says what another object's state must be, and its most basic use is testing whether a given object satisfies it.

@list heading="Three details" items="Specifications can be combined@combined|A factory can build one@factory|It can carry what it needs@carry"
Three details follow. Specifications can be combined, as predicates are, which Chapter 10 develops. Because the rule is a full object, a factory can build it from an account or a policy table, without coupling the tested object to them. And a specification can carry what it needs, like Evans's delinquency rule with its evaluation date built in.

@chapter A seed bank's rule
@code block=1 lines=1-20 label=Java focus="1@interface|4-6@thresholds|14-19@isSatisfiedBy"
Here's a seed bank sending lots of seed to growers. The interface has one method. The specification holds its thresholds, and isSatisfiedBy asks four things: at least eighty-five percent germination, moisture at most eight percent, at most ten years old, and not in quarantine. The lot knows its measurements, and nothing about the policy.

@math heading="lot-01" items="4 of 4 clauses true@all four;;may go out@go out"
The lab checks each lot clause by clause. On lot one, all four clauses are true, and the lot may go out.

@math heading="lot-02" items="germination 88 ✓ · moisture 9 ✗@eighty-eight;;age 5 ✓ · not quarantined ✓@five years;;3 true · fails on moisture ≤ 8@needs drying"
Lot two has eighty-eight percent germination, nine percent moisture, is five years old, and isn't quarantined. Three clauses are true. The one false clause is moisture. The lot needs drying, not discarding.

@math heading="lot-07" items="germination 72 ✗@seventy-two;;moisture 10 ✗ · age 11 ✗@moisture ten;;first false: germination ≥ 85@first"
Lot seven has seventy-two percent germination, moisture ten, and age eleven. Three clauses are false, and the first is germination.

@art all-reasons
The order only matters for the first false clause. The lab lists every false one, because a seed bank deciding whether to dry a lot, retest it or compost it needs all of them.

@art seed-lots
Once the rule is an object, any part of the system can ask it about any lot, and the answer comes with its reasons. Whether eighty-five percent is right, only the curators can say.

@chapter Where people slip
@list heading="Common slips" items="Put every rule on the object@The first|Specification means a rule engine@The second|Read only the first false clause@And the third"
The first slip is putting every rule about an object on the object. A one line test belongs there, but rules that grow don't. The second is thinking specification means building a rule engine. It borrows only the predicate. And the third is reading only the first false clause.

@chapter Try it
@words text="lot-08: germination 85 · moisture 8 · age 11 · quarantine yes"
Your turn. Lot eight: germination eighty-five, moisture eight, age eleven, and in quarantine. Evaluate each clause by hand. Does it satisfy the rule, which clauses are false, and which is the first?

@end text="Check the lot"
Then add it to the lab and check, on Learn. That's learn dot get er done dot I O.
