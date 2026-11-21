---
format: long
lesson: ddd-building-blocks/value-objects
title: Value Objects: care about what it is, not which one
thumb: Change it by replacing it
---

@chapter Which marker?
@title text="Value Objects" sub="Domain-Driven Design, Chapter 5" art=thumb
Evans starts with a child drawing with markers. The child cares about a marker's colour and its tip, but not which of two identical markers he's holding.

@art markers-and-drawings
Though he cares very much which drawings are his, and which are his sister's. The markers are values. The drawings have identity.

@art identity-everywhere
It's tempting to give every object an identity, and some frameworks do. Evans counts the cost. The system must track it all, optimisations are ruled out, defining meaningful identities takes analysis, and an artificial identity makes every object look alike. Special handling belongs only where it's needed.

@chapter What a value is
@words text="We care what it is, not which one."
A value object describes something and has no conceptual identity. And whether a thing is one depends on who's asking. To a mail order firm, an address is a value. To a postal service organising rounds, it's an entity.

@art whole-value
Values needn't be simple. They can be built from other values, and can even refer to entities, like a route between two cities. And their parts should belong together as one idea. A street, a city and a postal code belong together as an address, not as three fields of a person.

@chapter Sharing safely
@art shared-name
Two people who share a name are still two people, but their name objects are interchangeable. So they could share one. Until one of them changes name, and the other's changes too.

@quote text="To protect against this, in order for an object to be shared safely, it must be immutable: it cannot be changed except by full replacement." cite="Evans, Domain-Driven Design, Chapter 5"
To protect against this, in order for an object to be shared safely, it must be immutable. It cannot be changed except by full replacement.

@list heading="Mutable values, only if" items="They change often@change often|Creation is expensive@expensive|Replacement disturbs the database@database|Little sharing anyway@little sharing"
Evans does allow mutable values, for performance: values that change often, objects expensive to create, replacement that disturbs how the database clusters data, or little sharing anyway. But the rule that goes with it is absolute. A mutable value must not be shared.

@chapter The bakery
@math heading="slot-shared-mutable" items="3 holders: orders 17, 18, 19@three orders;;change through order 18@order eighteen;;3 see it · 2 surprised · 0 new values@two are surprised"
Here's a bakery. Three orders hold the one pickup slot, Saturday nine to eleven. The customer of order eighteen moves her pickup an hour later, by changing the slot in place. Three holders see the change, two are surprised, orders seventeen and nineteen, and no new values. Two customers have been moved without asking.

@code block=1 lines=1-17 label=Java focus="2-4@final|12-14@later|17@To move one order"
Now make the slot immutable. Every field is final. To move it, later builds a brand new slot, an hour on. To move one order, you give that order the new slot.

@art replace-not-change
So order eighteen now points at a new value, and the old slot is untouched. Orders seventeen and nineteen still hold Saturday, nine to eleven, exactly as their customers chose.

@math heading="slot-shared-immutable" items="3 holders@three holders;;1 sees it · 0 surprised@nobody surprised;;1 new value@one new value"
Three holders, one sees the change, nobody surprised, and one new value. That new object is the price of the safety, and it's why Evans lists object creation among his reasons for allowing mutability.

@art own-copies
Or take his special case, done properly. The slot is mutable, but each order holds its own copy. Changing order eighteen's copy reaches one holder, surprises nobody, and makes no new value. It's safe because nothing is shared, and it gives up the sharing that made values cheap.

@words text="Which trade-off?" sub="how often slots change · how many orders hold them"
Which trade off a real bakery should take depends on how often slots change and how many orders hold them. The lab doesn't know that.

@chapter Where people slip
@list heading="Common slips" items="Give everything an identity@The first|Share a mutable value@The second|Values must be simple@And the third"
The first slip is giving every domain object an identity, just in case. The second is sharing a mutable value. And the third is thinking a value object must be simple. What makes a value is having no conceptual identity, not being small.

@chapter Try it
@words text="class-7a, 7b, 7c, 8a: autumn · 8b: spring" sub="7c's trip moves the last day"
Your turn. A school's classes each hold term dates. Four hold autumn, one holds spring. Class seven c's trip moves its last day. Count the holders, who sees the change, who's surprised, and the new values, for a mutable and an immutable value.

@end text="Who sees the change?"
Then say whether term dates are a value to this school at all, and check it on Learn. That's learn dot get er done dot I O.
