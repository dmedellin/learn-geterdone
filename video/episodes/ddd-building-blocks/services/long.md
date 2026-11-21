---
format: long
lesson: ddd-building-blocks/services
title: Domain Services: when an operation isn't a thing
thumb: Sometimes it isn't a thing
---

@chapter Not a thing
@title text="Services" sub="Domain-Driven Design, Chapter 5" art=thumb
Entities and value objects are things. But some of the most important operations in a domain aren't things at all. They're activities.

@quote text="Sometimes, it just isn't a thing." cite="Evans, Domain-Driven Design, Chapter 5"
That's how Evans opens the pattern. Sometimes, it just isn't a thing.

@art forced-operation
He names two mistakes. The more common is giving up too soon on finding the right object, and drifting into procedural code. The other is forcing the operation onto an object it doesn't fit. The object loses its clarity, and because the operation brings several objects together, the host picks up dependencies on all of them.

@chapter What a service is
@art stateless-service
A service is defined purely by what it does for a client, and it's usually named for an activity, a verb rather than a noun. It's still part of the model, with an operation name from the ubiquitous language, and parameters and results that are domain objects.

@list heading="A good service" items="Stands for a domain concept no object owns@stands for a concept|Its interface uses the model's elements@its interface|Stateless@stateless"
A good one has three characteristics. The operation stands for a concept of the domain that doesn't belong naturally to an entity or a value. Its interface is expressed through other elements of the model. And it's stateless: any client can use any instance, whatever its history.

@chapter Three layers
@art three-service-layers
Most services are technical and live in the infrastructure, like the interface to an email system. Application and domain services are harder to tell apart, and the test is business meaning. Exporting transactions to a spreadsheet is an application service. File formats mean nothing to banking.

@words text="Funds transfer: a domain service" sub="Balance below a threshold: not a service at all"
A funds transfer is a domain service. It's a term of the business, embeds its rules, and involves two accounts, so it's awkward on either one. The service still asks the accounts to do most of the work. And deciding a balance is below a threshold isn't a service at all. It fits the account.

@chapter Granularity
@art medium-grain
There's a second reason for the pattern. A medium grained, stateless service puts significant behaviour behind a simple interface, easier to reuse and cheaper to call across a network than many fine grained objects. Without it, domain knowledge leaks up into the application layer.

@chapter A ticket exchange
@art exchange-swap
At a theatre box office, a customer exchanges a ticket for another performance. Exchange is a word the box office uses, and it involves the ticket held, the performance wanted, its seat plan, the price list and the refunds.

@code block=1 lines=1-17 label=Java focus="6-7@price list|9-16@exchangeFor"
In this first design, exchange is forced onto the ticket. So the ticket holds a price list and a refunds account, here only for one operation, exchangeFor.

@math heading="exchange-on-the-ticket" items="6 classes · 6 uses@six classes;;connected pairs 6/15 = 40%@forty percent;;fan-out: Ticket 4@fan out"
The lab counts dependencies. Six classes, six uses, and forty percent of the possible pairs connected. The largest fan out is Ticket, which uses four others. The largest fan in is SeatPlan, at two.

@code block=2 lines=1-17 label=Java focus="2-4@an interface|7-8@prices and refunds|10-16@exchange"
Now make exchange a domain service. It's an interface named for the activity, in the model's terms. The implementation holds the prices and refunds, and exchange reserves the new seat, settles the difference, surrenders the old ticket, and issues a new one.

@math heading="exchange-as-a-service" items="7 classes · 8 uses@seven classes;;connected pairs 8/21 ≈ 38.1%@thirty-eight;;fan-out: TicketExchange 5 · Ticket 4 → 1@from four to one"
Now there are seven classes and eight uses, about thirty-eight point one percent connected. The largest fan out is the exchange, at five. And Ticket's own fan out falls from four to one.

@art moved-dependencies
Read that honestly. The service design has more classes and more uses, not fewer. The connections have moved, from an entity that should be about who holds which seat, to an operation about exchanging. Whether the box office thinks of exchange as an activity is a question for the experts, not the lab.

@chapter Where people slip
@list heading="Common slips" items="Make every operation a service@The first|Anything called Service is a domain service@The second|Stateless means it changes nothing@And the third"
The first slip is making every operation a service, which strips entities of their behaviour. The second is calling any class with service in its name a domain service. And the third is thinking stateless means it can't change anything. It can. It just holds no state of its own.

@chapter Try it
@list heading="A bike-share" items="End a ride@when a ride ends|Choose the dock to empty@choose which dock|Send a push notification@push notification|Work out a fare@a ride's fare"
Your turn. Four bike-share operations: when a ride ends, close it, charge the member and send a receipt. Choose which dock the rebalancing van empties next. Send a push notification. And work out a ride's fare. Sort each into application, domain, infrastructure, or no service.

@end text="Sort the services"
Then write the domain service's interface in the model's terms, on Learn. That's learn dot get er done dot I O.
