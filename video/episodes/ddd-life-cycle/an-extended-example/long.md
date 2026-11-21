---
format: long
lesson: ddd-life-cycle/an-extended-example
title: Domain-Driven Design's building blocks, combined on one model
thumb: Every decision, in order
---

@chapter Combining the patterns
@title text="Using the Language: An Extended Example" sub="Domain-Driven Design, Chapter 7" art=thumb
So far the building blocks have come one at a time. Chapter 7 puts them all on one model.

@quote text="In the earlier examples, the patterns were mostly applied one at a time, but on a real project you have to combine them." cite="Evans, Domain-Driven Design, Chapter 7"
In the earlier examples, the patterns were mostly applied one at a time, but on a real project you have to combine them.

@art cargo-ship
Evans follows an imagined team through a cargo shipper's model, with three requirements: track each customer's cargo, book cargo in advance, and invoice automatically when it reaches a certain point. He starts from a fairly mature model. Discovery is left for later.

@chapter The order of decisions
@list heading="The order" items="Isolate the domain@isolated|Sort entities from values@sorted|Give associations a direction@directions|Draw the boundaries@boundaries|Choose repositories@repositories|Walk scenarios@scenarios"
The decisions come in a fixed order, and the order is the lesson. First the domain is isolated, with three application classes as coordinators. Then each object is sorted into entity or value. Associations get directions. Then boundaries. Repositories are chosen from the requirements. And scenarios check the result.

@art entity-value-sort
Customers, cargoes, handling events, carrier movements and locations are entities. Two of their identity schemes were settled by asking a domain expert. The delivery history borrows its identity from its cargo. The delivery specification and the customer's role are values.

@art one-way-events
Handling events point to carrier movements and not back, because the business tracks cargo, not ships' inventories. One cycle, cargo to history to events and back, is kept, with its cost noted. And the handling event becomes a root of its own, because finding the events for a carrier movement gives it meaning apart from the cargo.

@art prototype-copy
Then scenarios. Repeat business copies a new cargo from an old one, using Prototype, deciding part by part: a fresh empty history, a copy of the customer roles that still points at the same customers, and a new tracking number. Nothing outside the boundary is touched.

@chapter A theatre box office
@words text="Sell · Change or cancel · Admit at the door"
Now the same order on the lesson's own model, a theatre box office. Three requirements: sell seats for a performance, change or cancel a booking, and admit ticket holders at the door.

@list heading="Sorted" items="Entities: customer, booking, performance, venue@entities|Local: seat in its venue, ticket in its booking@within its venue|Values: price, seat reference@values"
Customers, bookings, performances and venues are entities. A seat is an entity known by row and number only within its venue, and a ticket only within its booking. A price, and a reference to a seat by row and number, are values.

@code block=1 lines=1-20 label=Java focus="3@another aggregate's root|12-19@repeatFor|15-16@new tickets"
A booking knows its customer, another aggregate's root. And here's the Prototype scenario on this model. repeatFor makes a new booking with a new number and the same customer root, and new tickets for the next performance, at the same seats, priced afresh.

@chapter Check the boundaries
@math heading="first-draft" items="4 aggregates · 6 objects@four aggregates;;5 references cross a boundary@five references;;2 reach a non-root@two"
The lab checks the boundaries. In the first draft, the ticket holds the seat object in the venue, and the door scanner keeps the tickets it's scanned. Four aggregates, six objects, five references cross a boundary, and two reach a non-root: ticket to seat, and scanner to ticket.

@math heading="boundaries-drawn" items="ticket holds the seat as a value@as a value;;4 cross a boundary · 0 violations@every one onto a root"
Fix both. The ticket holds the seat as a value, row and number. The scanner holds the booking and asks it for its tickets. Now four references cross a boundary, every one onto a root.

@art boundaries-drawn
And repositories follow from the requirements: customers, performances and bookings, so three. The venue needs none.

@art cancelled-booking
Cancel a booking, and two objects go, the booking and its ticket. One reference is left dangling, the scanner's. So the scanner must drop a cancelled booking, a rule across aggregates the model has to state.

@chapter Where people slip
@list heading="Common slips" items="It shows how the model was found@The first|Every root gets a repository@The second|Copy everything it refers to@And the third"
The first slip is expecting this chapter to show how the model was discovered. It doesn't. The second is giving every root a repository because it's a root. And the third is copying an aggregate by copying everything it refers to.

@chapter Try it
@words text="Customer · Order · Product · Oven" sub="and the dispatch board"
Your turn. A bakery's orders, with four aggregates and the dispatch board as an outside holder. Count the references that cross a boundary and those that reach a non-root. Say what deleting an order removes and leaves dangling, and name the one change that would leave no violation.

@end text="Draw the boundaries"
Check it in the lab, on Learn. That's learn dot get er done dot I O.
