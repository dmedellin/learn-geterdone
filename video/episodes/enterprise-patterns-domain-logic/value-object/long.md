---
format: long
lesson: enterprise-patterns-domain-logic/value-object
title: Value Object: why small objects should never change
thumb: Equal by value, never changed
---

@chapter Two kinds of object
@title text="Value Object" sub="Patterns of Enterprise Application Architecture, Chapter 18" art=thumb
Some objects are things you keep track of, like a customer. Others are just values, like a date. Fowler's short pattern explains the difference, and why one small rule about values prevents a nasty kind of bug.

@art two-customers
Fowler says one handy test is size. Values are small, like an amount of money or a date. References are large, like an order or a customer. But the real difference is equality. A reference object is equal by identity: the same object, or the same key in the database. Two customers with the same name are still two customers.

@art two-dates-equal
A Value Object is equal by its field values. Two dates are equal when they name the same day of the same month and year. So values get passed around freely, and you don't care how many objects for the same date exist, or whether two owners share one.

@chapter The advice
@quote text="it's a very good idea to make them immutable—that is, once created none of their fields change." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 18"
That freedom is where the central advice comes in. It's a very good idea to make them immutable. That is, once created, none of their fields change.

@chapter The aliasing bug
@code block=1 lines=1-12 label=Java focus="2-3@start and end|5-7@setEnd|9-11@checks a day"
Here's a date range that ignores the advice. Both start and end are public, open to every caller. And setEnd changes the range in place, while the last method checks a day against both ends. The lab counts two fields, both public and not final.

@art shared-range
Now give two bookings the same DateRange object, because they cover the same week. One booking is extended, and its code calls setEnd. The other booking is now extended too, though nothing touched it. And includes answers yes for days it never covered.

@art replace-not-change
Fowler's point is less that this is wrong than that nobody expects it. People expect to change a date by replacing the object with a new one. An immutable value meets that expectation, and can be shared without anyone asking who else holds it.

@chapter The value version
@art locked-value
So follow the advice. Make the date range a value: fixed when it's made, compared by its dates, and safe for any number of bookings to share.

@code block=2 lines=1-19 label=Java focus="1@class is final|2-3@private and final|5-8@set once|10-14@equals"
Here's the value version. The class is final, so no subclass can add a field that changes. The fields are private and final, set once by the constructor. And equals compares the two dates.

@math heading="The lab's count" items="mutable: 2 fields, 2 public and not final@mutable range;;value: 2 fields, 0 public and not final@value range;;routines: 2 → 3@routine count"
On the mutable range, two fields, two public and not final. On the value range, two fields, zero public and not final. The routine count rose from two to three, because of equals, but that isn't what makes it a value. The public fields are.

@words text="What the count can't see"
The count has limits. A private field with a public setter counts zero, though it can still change. And it can't see whether equals really compares values. You check that by reading it.

@chapter Storing values
@art embedded-row
A Value Object shouldn't be stored as a record of its own. Embedded Value keeps its fields in the owner's row, which also lets SQL query them. Serialized LOB is the other option. When should you use the pattern? For anything whose equality rests on something other than identity, and consider it for any small object that's easy to create.

@chapter Where people slip
@list heading="Common slips" items="Any object without an ID is a value@The first|Immutability is a performance trick@The second|Private fields make it immutable@And the third"
The first slip is thinking any object without an ID field is a value. It's how it's compared that counts. The second is thinking immutability is a performance trick. The reason is aliasing bugs. And the third is taking private fields for an immutable class. A setter still changes it.

@chapter Try it
@code block=3 lines=1-17 label=Java focus="2-4@fields|6-8@add|10-16@routines"
Your turn. Here's a Quantity class. Count its fields, its public fields that aren't final, its routines, and its public routines. Then write the fields, the constructor and the add method of its value version, and say what equals should compare.

@end text="Count the open fields yourself"
You can paste a class into the lab and see what it leaves open, on Learn. That's learn dot get er done dot I O.
