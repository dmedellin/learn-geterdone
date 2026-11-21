---
format: long
lesson: enterprise-patterns-domain-logic/service-layer
title: Service Layer: when a second client shows up
thumb: Write the response once
---

@chapter Two answers
@title text="Service Layer" sub="Patterns of Enterprise Application Architecture, Chapters 2 and 9" art=thumb
Should your application have a layer of services over its domain? The book gives two answers, and says so. Fowler wrote one. Randy Stafford, who wrote the pattern itself, gives the other.

@chapter The layer
@art boundary-layer
Chapter two describes a common approach. Put a Service Layer over a Domain Model or a Table Module, so the presentation talks to the domain only through it, like an API for the application. It's also a good place for transaction control and security.

@art thin-thick
The key decision is how much behaviour it holds. At one extreme, it's a facade that forwards every call to the objects below. At the other, most of the business logic lives in scripts inside it, over simple domain objects.

@words text="As thin as possible, if any" sub="Fowler · Stafford: a rich layer serves well"
Fowler's own preference is as thin a Service Layer as possible, and none at all if he can manage without one. Then he concedes at once that many good designers always use one with a good deal of logic. Stafford has done well with a rich layer, which is why Fowler asked him to write the pattern.

@chapter Two kinds of logic
@art three-clients
Stafford defines the layer as an application's boundary, a set of operations seen from the clients' side. His motivation: an enterprise application has several kinds of interface, like data loaders, user interfaces and integration gateways. They need the same interactions, and coding them again in each one duplicates them.

@art app-vs-domain
He then splits business logic in two. Domain logic is about the problem itself, like how an order is priced. Application logic is about the application's responsibilities, like notifying administrators and integrated systems, and running the work as one transaction.

@chapter Counting the repeat
@code block=1 lines=1-18 label=Java focus="4-8@lines four to eight|13-17@thirteen to seventeen|3@builds the order|12@imported row"
Here, a web page and a nightly import both place orders, and each does the whole response itself. The lab finds one repeated block: lines four to eight, and thirteen to seventeen, ten lines in all. Only the line that builds the order differs, from the form in one, and from the imported row in the other.

@words text="Transaction + mail = application logic" sub="reserve + confirm = domain calls"
Read it with Stafford's distinction. The transaction and the mail are application logic. Inside them are two domain calls, reserving the stock and confirming the order, each already in one place. What each client had to write for itself is the response that coordinates them. A third client would write it a third time.

@chapter One operation
@code block=2 lines=1-17 label=Java focus="2-8@each client builds|11-17@placeOrder"
So make the response one operation, placeOrder in an OrderService. Each client builds its order and calls it. The lab finds zero repeated blocks. The five lines didn't disappear. They exist once, and the transaction and the mail have a home.

@art one-operation
That's Stafford's operation script in small: thicker service classes that carry out the application logic, and hand the domain logic to domain objects. His other option is a domain facade, thin classes over a Domain Model that does all the work.

@chapter When to add it
@quote text="But as soon as you envision a second kind of client, or a second transactional resource in use case responses, it pays to design in a Service Layer from the beginning." cite="Randy Stafford, in Fowler, Patterns of Enterprise Application Architecture, Chapter 9"
With one kind of client, and no response that spans several transactional resources, you probably don't need it. But as soon as you envision a second kind of client, or a second transactional resource, it pays to design in a Service Layer from the beginning.

@chapter Where people slip
@list heading="Common slips" items="Domain and application logic are the same@The first|Every application needs one@The second|It's a remote interface@And the third"
The first slip is treating domain and application logic as the same. The second is thinking every application needs a Service Layer. And the third is taking it for a remote interface.

@art remote-facade
Its interface is coarse grained, so it could be called remotely. But Stafford's advice is to start with a local layer, and add a Remote Facade only if you need one.

@chapter Try it
@code block=3 lines=1-18 label=Java focus="1-8@web page|10-18@phone client|11@stays"
Your turn. A web page and a phone client both cancel orders. Mark the lines they repeat, and write the service operation both would call. Then say which line stays in its own client, and why.

@end text="Find the repeated response"
You can paste two clients into the lab and see what they share, on Learn. That's learn dot get er done dot I O.
