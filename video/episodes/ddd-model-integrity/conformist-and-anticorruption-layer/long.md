---
format: long
lesson: ddd-model-integrity/conformist-and-anticorruption-layer
title: Conformist or Anticorruption Layer: when upstream won't help you
thumb: Follow it, or wall it off
---

@chapter On your own
@title text="Conformist and Anticorruption Layer" sub="Domain-Driven Design, Chapter 14" art=thumb
Customer Supplier needs an upstream team with a reason to serve you. Sometimes there isn't one. The teams are far apart in a large company, or the supplier has many small customers, or it's changing direction, or it's gone out of business. Then promises from upstream won't be kept.

@list heading="Three paths" items="Abandon the upstream@Abandon|Build your own model and translate@translation layer|Give up your model and conform@conform"
Evans gives three paths. Abandon the upstream, which is Separate Ways, two lessons on. If you must keep the dependency and its design is hard to work with, build your own model and a translation layer. And if its quality is tolerable and its style compatible, give up an independent model, and conform.

@chapter Conformist
@art follow-upstream
Conforming means following the upstream model closely, and dropping translation altogether. It cramps the downstream design. But integration becomes far simpler, and the two teams share a language. The cost is a deeper dependence, and an application limited to what the upstream model can do.

@quote text="It is very unappealing emotionally, which is why we choose it less often than we probably should." cite="Evans, Domain-Driven Design, Chapter 14"
It is very unappealing emotionally, which is why we choose it less often than we probably should.

@art pulled-upward
A sidebar makes the positive case for an off the shelf component with a large interface. If it's worth having, its design holds crunched knowledge, perhaps more than yours. Conforming can pull your design upward.

@chapter Anticorruption Layer
@art bent-model
At the defensive end, a new system with a large interface to another can find its model bent to match, piece by piece. The trap is believing that only plain values cross, and that a plain value means the same on both sides. Meaning lives in how the data is associated.

@art layer-parts
So build an isolating layer. It offers your context the other system's functions in your own model's terms, reaches the other system by the interface it already has, and translates both ways. It's not a messaging mechanism. It translates concepts and actions.

@list heading="Inside the layer" items="Facade: in the other system's model@facade|Adapter: makes a service's requests@adapter|Translator: converts, holds no state@translator"
Evans builds it from three parts. The facade simplifies the other system's interface, and stays in that system's model. The adapter makes the requests a service needs. And the translator converts objects and data, and holds no state.

@code block=1 lines=1-20 focus="2-4@its own question|16-19@asks the old membership|17@card number"
Here's a sketch of one service, from a theatre's box office. The box office asks its own question: does this patron have a discount? The adapter asks the old membership system's facade for a row by card number, and the translator turns the row into a Discount. Nothing outside this class names the legacy row.

@art great-wall
Evans closes with a cautionary tale. The Great Wall kept a civilisation distinct, and helped bankrupt a dynasty. Isolation has costs as well as benefits, and integration of any kind is always expensive.

@chapter Count the reach
@code block=2 lines=1-3 focus="1@old membership|2@marketing|3@finance"
Now the count. The box office is downstream of the old membership system. Marketing conforms to the box office, and finance is its customer. The membership team changes its model.

@math heading="one upstream change" items="conform: 3 models · 0 translators@conforms;;acl: 0 models · 1 translator · 2 untouched@layer"
If the box office conforms, three models must change, box office, marketing and finance, and there are no translators. Behind a layer, no models change, one translator updates, the box office's, and marketing and finance are untouched.

@art translator-cost
But three to nothing isn't a verdict. The layer is code the box office team writes and keeps, for every change on the other side. One translator may be a day's work or a month's. Which is cheaper depends on the size of the interface, how often upstream changes, and how good it is.

@chapter Where people slip
@list heading="Common slips" items="Treating Conformist as surrender@The first|Mistaking the layer for transport@The second|Passing primitive data straight through@And the third"
The first slip is treating Conformist as surrender, always to be avoided. The second is mistaking an anticorruption layer for the transport between systems. And the third is passing the other system's primitive data straight through.

@chapter Try it
@code block=3 lines=1-3 focus="1@till software|2@baking plan|3@accounts"
Your turn. A bakery's order system conforms to the till software it bought. The baking plan conforms to the orders, and accounts translates orders through its own layer. The till vendor changes its model. Find the models that must change and the translators, then do it again with the first relationship made a layer.

@end text="Conform, or translate"
Check both in the lab, on Learn. That's learn dot get er done dot I O.
