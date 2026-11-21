---
format: long
lesson: ddd-large-scale-structure/knowledge-level
title: Knowledge Level: objects that describe other objects
thumb: Rules a superuser can change
---

@chapter A pattern about models
@title text="Knowledge Level" sub="Domain-Driven Design, Chapter 16" art=thumb
Evans takes this pattern from Martin Fowler's Analysis Patterns. It never has a chapter there, because unlike Fowler's other patterns it doesn't model a domain. It structures a model.

@quote text="a group of objects that describes how another group of objects should behave." cite="Evans, Domain-Driven Design, Chapter 16"
A knowledge level is a group of objects that describes how another group of objects should behave. It's for software whose behaviour must be configurable, where roles and relationships change when the system is installed, or even while it runs.

@chapter When one arrangement fails the rest
@art bent-fields
Organisations arrange their people in different ways. Departments under directors, units under managers, two reporting lines at once. An application that assumes one arrangement fails the rest. Users bend data entry fields to meanings they weren't built for, features get switched off, and years later the fields mean different things to different users.

@art static-or-loose
A static model forces workarounds. A fully flexible one is hard to use, and can't enforce the organisation's own rules. And options bolted onto the operational objects make them unwieldy. Inside such a model, Evans says, is another model about the model.

@chapter Two levels
@art two-levels
A knowledge level separates it out, and makes its constraints explicit. One set of objects records what is actually happening. Another says what kinds of thing are allowed, and what each may do. In the book's pay example, an employee type that only a superuser may edit turns out to be a knowledge level already.

@list heading="Not Reflection, not a layer" items="Built from ordinary domain objects@ordinary objects|Narrow, not fully general@full generality|Dependencies run both ways@both ways"
It's like the Reflection pattern's base and meta levels, with two differences. It's about the business, so it's built from ordinary objects, never the language's reflection tools. And it doesn't aim at full generality. It isn't called a layer, because dependencies run both ways between the levels.

@words text="Use it sparingly" sub="intoxicating, Evans says"
The warnings are as strong as the pattern. Evans calls it intoxicating, and says use it sparingly. The indirection brings back some obscurity. Configuring a complex knowledge level takes a programmer's skills. Data migration doesn't vanish. And the design must hold up for every configuration a user might later choose.

@chapter A library's borrowers
@code block=1 lines=1-19 focus="3-10@Borrower Category|13-18@Every real borrower|17@loan days"
Now a library that lends to students, staff and the public. With a knowledge level, each category is a borrower category object, a row in a table a superuser edits. Every real borrower points to one, and its due date comes from its category's loan days.

@math heading="four requirements, modules touched" items="add-visitor:  subclasses 3 · knowledge 1@visitor category;;add-alumni:  2 · 1@alumni;;longer-staff-loans:  1 · 1@longer loans;;exam-amnesty:  2 · 2@amnesty"
Four requirements arrive. A visitor category with its own fines, an alumni category with the public's fines, longer loans for staff, and an amnesty on students' fines during exams. With a subclass per category, they touch three, two, one and two modules, eight in all. With the knowledge level, the first three each touch only the category table.

@art superuser-table
That's one module apiece, with no code written. A visitor category, an alumni category and longer staff loans are all just rows that a superuser edits.

@art amnesty-new-rule
The fourth is the instructive one. An exam time amnesty is a kind of rule the fine policy was never built to express. So it reaches the knowledge level itself, where the fine policy must learn about dates, and the configuration. Two modules. Five touches in all, with three changes confined.

@words text="A new kind of rule is still new code"
The knowledge level doesn't make the amnesty harder than the subclasses did. It just doesn't make it easier. And the count leaves out the superuser who must configure amnesties correctly, and the loans already out when the rule changes.

@chapter Where people slip
@list heading="Common slips" items="Building it with reflection tools@The first|Making it as general as possible@The second|Expecting every change to be configuration@And the third"
The first slip is implementing a knowledge level with the language's reflection facilities. The second is making it as general as possible. A narrow set of constraints says more about intent. And the third is believing it turns every future change into configuration.

@chapter Try it
@art gym-types
Your turn. A gym, written first with a subclass per kind of session, then with a knowledge level of session types. Four changes, from adding pilates to automatic follow up booking. Find the modules each change touches in each design, the totals, and the changes confined to one module. Then say which change the knowledge level makes harder.

@end text="Describe, then constrain"
Type both designs into the lab to check, on Learn. That's learn dot get er done dot I O.
