---
format: long
lesson: ddd-distillation/core-domain
title: Core Domain: put your best people where the value is
thumb: Where do your best people work?
---

@chapter Too complex, even in layers
@title text="Core Domain" sub="Domain-Driven Design, Chapter 15" art=thumb
Layers keep the domain apart from the technical code. But in a big system, the domain by itself can still be too complex to manage. Chapter fifteen's answer is distillation: separating a mixture, so its essence can be drawn off.

@list heading="What distillation gives" items="A grasp of the overall design@overall design|A core small enough to talk about@small enough|A guide for refactoring@refactoring|Decisions on buying and staffing@outsource"
Done well, it gives the whole team a grasp of the overall design, and a core small enough to enter the Ubiquitous Language. It guides refactoring, focuses work where the value is, and helps decide what to outsource, what to buy, and who works on what.

@chapter Where skill drifts
@art lost-in-corners
Losing sight of the core costs twice. First, people get lost outside their own corner, so they specialise, knowledge stops moving, and behaviour gets written twice. Second, not every part can be equally refined, so priorities get set whether or not anyone sets them.

@art drift-to-infrastructure
And Evans observes where they go. Scarce skilled developers drift toward infrastructure, and toward neatly defined problems that need no special knowledge of the business. Those look interesting, and travel well on a CV. The core is then built by less experienced hands, and the application never does anything compelling, however good its plumbing.

@art comments-not-loans
His story is a system for syndicated loans. The strong developers were busy with database mapping and messaging. The one experienced object designer built an elegant way to attach comments to objects. Useful, and peripheral. Meanwhile the loan module, the reason for the system, was tangled by a developer out of his depth.

@chapter The pattern
@quote text="The planning process must drive resources to the most crucial points in the model and design." cite="Evans, Domain-Driven Design, Chapter 15"
So decide which part is the core, make it easy to see, and keep it small. Staff it with your best developers. The planning process must drive resources to the most crucial points in the model and design.

@words text="Distinctive core · generic rest" sub="keep the core secret · refactor for the core"
And the hard decision makes several easy ones. Make the core distinctive, and the rest as generic as you practically can. If anything is kept secret, it's the core. And when there's only time for one of two good refactorings, choose the one that does more for the core.

@chapter Choosing, and staffing
@art money-core
The answer depends on where you stand. Many applications need a plain model of money, but for software that trades currencies, a richer money model is the core. And the choice should change with the iterations, because what looks central at first can turn out to be supporting.

@art stay-and-learn
Strong developers seldom know the domain, so they get supporting work, so they never learn it. Evans's remedy is strong developers who mean to stay and become holders of domain knowledge, paired with experts. And the core can rarely be bought: industry frameworks have disappointed, except as published languages.

@chapter A bike share's weeks
@art weeks-shares
Now a project written for the lesson: a city bike share, whose distinctive problem is rebalancing. Forecasting where riders will want bikes, and planning van runs to move them there. Eight parts, each with its weeks and its strongest developers.

@math heading="as-it-drifted, 100 weeks" items="core: rebalancing 16 + forecast 8 = 24@twenty four;;generic: 18 + 10 + 12 + 8 = 48@forty eight;;supporting: 14 + 14 = 28@twenty eight;;strongest on core: 0 of 3@none of the three"
As the team arranged itself, twenty four of a hundred weeks are on the core, forty eight on generic parts like payments and login, and twenty eight on supporting parts. And none of the three strongest developers is on the core.

@math heading="core-first" items="core: 46 of 100 · generic: 30 of 100@forty six;;strongest on core: 3 of 3@all three"
After a planning decision, forty six weeks go to the core, and thirty to generic parts. All three strongest developers work on rebalancing and the forecast. The lab can't tell you rebalancing is the core. That's the team's choice. It only counts what the choice does.

@chapter Where people slip
@list heading="Common slips" items="The hardest part must be the core@The first|Buying the core as a framework@The second|Fixing the core at the start@And the third"
The first slip is taking the core to be the hardest or most essential looking part. Payments can be hard and indispensable and still not be it. The second is expecting to buy the core as an industry framework. And the third is fixing the core at the start of the project.

@chapter Try it
@words text="Triage scheduling is the core" sub="triage 10 · records 14 · billing 15 · login 6 · reminders 5"
Your turn. A clinic's booking system, whose team agrees that triage scheduling is the core. Its parts, with their weeks and strongest developers, are in the lesson. Find the total weeks, the share on the core, the share on generic parts, and how many of the strongest developers are on the core.

@end text="Staff the core first"
Type the parts into the lab to check, on Learn. That's learn dot get er done dot I O.
