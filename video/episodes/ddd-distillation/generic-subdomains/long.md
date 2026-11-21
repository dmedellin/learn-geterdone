---
format: long
lesson: ddd-distillation/generic-subdomains
title: Generic Subdomains: the parts you'd rather not build
thumb: Buy it, borrow it, or build less
---

@chapter Clutter around the core
@title text="Generic Subdomains" sub="Domain-Driven Design, Chapter 15" art=thumb
Some parts of a model add complexity without carrying any special knowledge. Principles everybody knows, or details from specialties that support the project without being its focus. They're needed for the system to work, but mixed in with the core, they make it harder to see.

@quote text="There is a part of your model that you would like to take for granted." cite="Evans, Domain-Driven Design, Chapter 15"
There is a part of your model that you would like to take for granted. Evans's examples are an organisation chart, which shipping, banking and manufacturing all need, and accounting ledgers. And he's watched two projects put their best developers on dates and time zones for weeks.

@art separate-module
So find the subdomains that support the project without being its point. Give each a generic model in a Module of its own, holding nothing peculiar to your business. Rank their work below the core's, keep the core's developers elsewhere, and check whether a package or a published model would serve.

@chapter Four options
@list heading="How to get a generic part" items="Off the shelf@off the shelf|A published design or model@published|Outsourced@outsourced|Built in house@in house"
Then there are four options: buy one off the shelf, adopt a published model, have it outsourced, or build it in house. Each has costs. Off the shelf means less code, maintained by someone else, but it still has to be evaluated, may be overbuilt, and can bring platform dependencies. Evans finds such solutions worth investigating, and usually not worth the trouble.

@art published-model
A published design or model comes mature and documented, though it may fit badly or be more than you need. Where a field has a rigorous formal model, as accounting and physics do, use it, and implement only the consistent subset you need.

@art outsource-tests
Outsourcing keeps the core team on the core, and forces an interface oriented design. But explaining the interface takes the core team's time, and bringing the code back in has an overhead. Evans recommends specifying the acceptance tests yourself. And in house is easy to integrate, but costs maintenance, and its estimate is easy to get wrong.

@chapter Two time zones
@art two-timezones
Two projects spent weeks on time zones. On a shipping scheduler, the need was proven, the core was mature, and a strong programmer on a short contract adapted a public domain implementation. On an insurance system, long term developers built a fully general time zone model before any requirement was known, and the core went undeveloped. Both kept it out of the core.

@chapter Generic, not reusable
@words text="Generic ≠ reusable" sub="only what you need, strictly generic"
Evans said generic, not reusable, on purpose. If you build it yourself, don't design that code for reuse. Put only what's needed into it, and the effort into the core. But stay strictly inside the generic concept. Anything specific to your industry belongs in the core, or in a specialised subdomain.

@art first-cut-core
And what should an early end to end system be made of? A generic part is tempting, because it's easy to analyse. But unless the team's skills are proven and the domain well known, build the first cut on part of the core, even a small one. That's where the risk is.

@chapter Buying weeks back
@math heading="all-built" items="100 weeks · core 24 · generic 48@a hundred weeks;;48 weeks a decision could free@could free"
Back to the bike share. With every generic part built in house: a hundred weeks, twenty four on the core, forty eight on generic parts, and forty eight weeks a decision to buy or outsource could free.

@math heading="buy-and-outsource" items="buy payments, maps · outsource login@buys payments;;+ 3 + 1 weeks to fit the packages@isn't free;;team: 64 weeks · core 24 of 64 = 3/8@sixty four;;strongest on core: 0 of 3@still none"
Now the team buys payments and map tiles, outsources login, and keeps messaging. Buying isn't free: three weeks and one week to evaluate and integrate the packages. The team's own weeks fall to sixty four, twenty four on the core, three eighths. But there are still none of the strongest developers on the core.

@art freed-weeks
No decision about people was made. So the last preset makes one. The thirty six weeks the purchases saved go to rebalancing and the forecast, and so do the three strongest developers. The core now holds sixty of the team's hundred weeks, and all three of the strongest.

@chapter Where people slip
@list heading="Common slips" items="Generic means designed for reuse@The first|Strongest developers on the generic part@The second|Starting with generic parts@And the third"
The first slip is taking generic to mean designed for reuse. The second is giving the generic part to the strongest developers because it's hard and well defined. And the third is starting a project with the generic parts to reduce risk.

@chapter Try it
@words text="Buy billing · outsource login · build reminders" sub="billing-fit: 1 week"
Your turn. The clinic from the last lesson buys billing, adding one week to fit it, outsources login, and builds reminders. Find the team's own weeks, the core's share of them, the generic parts still built in house, and the weeks a further decision could free.

@end text="Spend the freed weeks on the core"
Type the parts into the lab, on Learn. That's learn dot get er done dot I O.
