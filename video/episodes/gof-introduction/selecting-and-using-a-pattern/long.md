---
format: long
lesson: gof-introduction/selecting-and-using-a-pattern
title: How to choose a design pattern, and when not to
thumb: Only where it's needed
---

@chapter Where to start
@title text="Selecting and Using a Design Pattern" sub="Design Patterns, Sections 1.7 and 1.8" art=thumb
You have a design problem in front of you, more than twenty patterns, and a catalog you don't know yet. Where do you start? The last two sections of Chapter one answer that, and end on a warning.

@list heading="Six ways in" items="How patterns solve problems@go back to Section|Scan the intents@read through the intents|Follow the cross-references@follow the cross|Read the right chapter@read the catalog chapter|Find the cause of redesign@causes of redesign|Ask what should vary@ought to vary"
Section one point seven gives six ways in. Go back to Section one point six, and how patterns solve problems. Read through the intents, narrowing by purpose and scope. Follow the cross references from a pattern you know. Read the catalog chapter for the right purpose. Look for your problem among the causes of redesign. Or ask what in your design ought to vary.

@art opposites
The authors call the last two opposites. A cause of redesign asks what might force a change on you. The last approach asks what you want to be free to change, without redesigning, and puts that concept behind an interface of its own.

@words text="What each pattern lets vary" sub="Strategy: an algorithm · State: an object's states · Observer: its dependents"
Table one point two supports it. For each pattern, it gives the aspect it lets vary. Strategy lets an algorithm vary. State, the states of an object. Observer, how many objects depend on another. And Bridge, an object's implementation.

@chapter Seven steps
@list heading="Applying a pattern" items="Read it, for Applicability and Consequences@read it through|Study Structure, Participants, Collaborations@study|Look at the Sample Code@sample code|Name the participants@choose names|Define the classes@define the classes|Name the operations@name the operations|Implement them@implement"
Once you've chosen, Section one point eight gives seven steps. Read it through, paying most attention to applicability and consequences. Study its structure, participants and collaborations. Look at the sample code. Choose names for the participants. Define the classes. Name the operations, consistently. Then implement them.

@code block=1 lines=2-14 focus="2-4@DiscountStrategy|10-14@the dozen discount"
That fourth step has a nice detail. Choose names that mean something in your application, but keep the participant's name inside them. Here, the bakery's DiscountStrategy, and the dozen discount, both keep the word Strategy, so the pattern stays visible.

@art named-participant
The book's own participant names are usually too abstract to use as they are. Your names should say what the class does in your application, and still say which role it plays.

@chapter The warning
@quote text="A design pattern should only be applied when the flexibility it affords is actually needed." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Section 1.8"
And then the warning, which the chapter ends on. A design pattern should only be applied when the flexibility it affords is actually needed.

@art indirection-layers
That's because the flexibility is often bought with extra levels of indirection. Indirection can complicate a design and cost some performance. The consequences sections are where you weigh the benefits against those liabilities.

@chapter A bakery's rule
@art bakery-changes
The lab puts that to work on a bakery's order system. Its team lists seven changes it can foresee, each with the aspect that would vary, whether they think it's likely, and how many months away it is.

@art rule-filter
The team writes its rule first, before looking at what it selects. Then each change either passes, or is turned away by one clause, and that clause is the reason not to add a pattern yet.

@math heading="likely = yes and months ≤ 12" items="discount-rules · payment-provider · loyalty-alerts@three of the seven;;oven-schedule, receipt-layout, new-branch: fail likely = yes@fail on likely;;order-states: fails months ≤ 12 at 18@eighteen months"
The team's rule is likely, and within a year. It selects three of the seven: discount rules, payment provider, and loyalty alerts. Oven schedule, receipt layout and new branch fail on likely. And order states fails on time, at eighteen months.

@list heading="A pattern for each" items="Discount rules → Strategy@discount rules|Payment provider → Abstract Factory, Bridge@payment provider|Loyalty alerts → Observer@loyalty alerts"
Each selected change points to a pattern. The discount rules are an algorithm, so Strategy. The payment provider is a platform dependence, so Abstract Factory or Bridge. And the loyalty alerts are objects that depend on an order, so Observer.

@art everything-selected
Now loosen the rule to anything within four years. It selects all seven, and fails none. A pattern for every change the team can imagine, each with its indirection. That's exactly the indiscriminate use the authors warn against.

@words text="The rule is the team's" sub="the lab can't say what will come"
The lab shows what a rule selects, and which clause turns each change away. It can't say whether an unlikely change will come anyway, or whether eighteen months is near enough. Those are judgements.

@chapter Where people slip
@list heading="Common slips" items="Applying every pattern that could fit@The first|Treating the six ways as one method@The second|Copying participant names as they are@And the third"
The first slip is applying every pattern that could fit. The second is treating the six ways of selecting as one method, when two of them are opposites. And the third is copying the book's participant names straight into the code, instead of keeping them inside your own.

@chapter Try it
@words text="A library catalogue" sub="likely = yes and months ≤ 12"
Your turn. A library catalogue lists four changes: search ranking, ebook loans, a hold queue, and fine rules. Apply the same rule, say which clause rejects each change it turns away, and name a pattern for each one selected.

@end text="Apply the rule"
Then type the changes into the lab and check, on Learn. That's learn dot get er done dot I O.
