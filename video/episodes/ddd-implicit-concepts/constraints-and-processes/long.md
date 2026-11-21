---
format: long
lesson: ddd-implicit-concepts/constraints-and-processes
title: Explicit constraints: give the business rule a name of its own
thumb: Name the rule
---

@chapter Beyond things and actions
@title text="Explicit Constraints and Processes as Domain Objects" sub="Domain-Driven Design, Chapter 9" art=thumb
Object design leads you to look for things, and the actions they take: the nouns and verbs. Evans names three more kinds of concept that weren't obvious to him at first: constraints, processes, and specifications.

@quote text="Constraints make up a particularly important category of model concepts." cite="Evans, Domain-Driven Design, Chapter 9"
He opens with the first. Constraints make up a particularly important category of model concepts.

@chapter A named method
@art capacity-check
Sometimes a constraint has a natural home. An object whose contents may not exceed a capacity can check that in each operation that changes them. Evans's move is to factor the rule into a method of its own, with a name that says what it means. Same behaviour. But now the rule is a named thing the team can discuss, with room to grow.

@chapter When it outgrows its host
@list heading="Three warning signs" items="It needs data the host doesn't otherwise need@needs data|Similar rules recur across classes@turn up in several|Talked about, but hidden in code@keep returning"
Sometimes a method isn't enough. Three signs say a rule is distorting the object that holds it. Checking it needs data that doesn't otherwise belong there. Rules of the same kind turn up in several classes. Or the conversations keep returning to the rule, while in the code it's hidden in procedural logic.

@art constraint-object
Then the constraint can become an explicit object of its own, or even a small set of objects. His example is the overbooking policy from Chapter 1, which became a class.

@chapter Processes
@art process-object
Processes come with a caution. Procedures shouldn't become a prominent part of the model, since objects exist to encapsulate them. What Evans means are processes that exist in the domain itself. A service can make one explicit. And where it can be done several ways, each way can be its own object, a strategy.

@quote text="Is this something the domain experts talk about, or is it just part of the mechanism of the computer program?" cite="Evans, Domain-Driven Design, Chapter 9"
His test is short. Is this something the domain experts talk about, or is it just part of the mechanism of the computer program?

@chapter A theatre's sales limit
@code block=1 lines=1-19 label=Java focus="9@capacity less|10-12@preview|13-16@sold plus seats"
Here's a theatre. A performance can't sell more than its capacity less the seats held back for wheelchair users and companions. On preview nights, a tenth of the house is kept for members. The first design writes all that inline, in sell, ending with a check that sold plus seats stays within the limit.

@math heading="inline-limit" items="1 + 2 if + 2 && = 5@five decision points"
The lab counts five decision points: the starting one, two ifs, and two conditional ands. All of them in sell.

@art hidden-rule
It works. But nothing in the design says a sales limit is there. It's arithmetic and conditions, tucked inside a method about selling.

@code block=2 lines=1-13 label=Java focus="7-9@asks"
The second design names the rule SalesLimit, and sell just asks it whether a sale is allowed.

@code block=3 lines=1-14 label=Java focus="7@allows|9-11@preview|12@seats"
And here's the constraint as an object. allows does the work: the capacity less the held seats, the preview reduction for non-members, and the final check on seats.

@math heading="factored" items="caller: 1 + 1 if = 2@caller;;constraint: 1 + 1 if + 2 && = 4@constraint;;decisions: 4 inline · 1 + 3 = 4 factored@no decision"
Now the caller counts two: one question, and its two outcomes. The constraint counts four. Look at them together. The decisions themselves number four inline, and one plus three across the two classes. Factoring removed no decision. It moved three of them to an object whose name says what they are.

@art moved-decisions
Six against five is only the starting one, counted once for each routine. And that's the point: factoring doesn't make a rule simpler than it is. It gives it a name and a home.

@chapter Reading the signs
@art preview-seats
Read the inline version against the warning signs. The members' tenth and a patron's membership are needed only by the limit. A matinee discount would put related rules beside it. And if the manager talks about the preview allocation every week, the third sign applies. None of that is in the count.

@chapter Where people slip
@list heading="Common slips" items="Leave it inline because it works@The first|Factoring reduces the decisions@The second|Model every procedure@And the third"
The first slip is leaving a rule inline because it works. Both versions work. The second is expecting factoring to reduce the decisions. It moves them. And the third is modelling every procedure as a domain object.

@chapter Try it
@code block=4 lines=1-20 label=Java focus="7-11@counts|13-15@the rule"
Your turn. A clinician's diary, with a booking rule inside book. It counts the day's visits, then applies the rule. Count the decision points, say which warning signs the rule shows, and sketch the named constraint you'd move it to.

@end text="Give the rule a name"
Paste the listing into the lab to check your count, on Learn. That's learn dot get er done dot I O.
