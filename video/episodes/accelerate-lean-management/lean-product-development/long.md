---
format: long
lesson: accelerate-lean-management/lean-product-development
title: Lean product development: small batches, early feedback
thumb: First feedback, sooner
---

@chapter Faux Agile
@title text="Lean Product Development Practices" sub="Accelerate, Chapter 8" art=thumb
Chapter eight turns from how software is delivered to what's delivered. And it begins with a complaint: Agile has largely won the argument over methods, but much of what organizations adopted is faux Agile. Some of the practices, without the culture and processes around them.

@list heading="Signs of faux Agile" items="Months of budgets and requirements first@budgets|Large projects that ship rarely@large projects|Customer feedback as an afterthought@afterthought"
In larger companies, three signs are common. Months spent on budgets, analysis and requirements before work begins. Work gathered into large projects that ship rarely. And customer feedback treated as an afterthought.

@art lean-startup
Against that, the authors set the Lean approach to product development, and Eric Ries's Lean startup movement. They test a product's design and business model from the start, with frequent user research.

@chapter Four capabilities
@list heading="Lean product development" items="Small batches, MVPs among the means@Small batches|Visibility of the flow of work@flow of work|Customer feedback built into design@Customer feedback|Team authority over specifications@authority"
The hypothesis is that practices like prototyping early, working in small batches, and pivoting early and often might affect organizational performance. The authors examined four capabilities. Small batches, with MVPs among the means. Visibility of the flow of work to customers. Customer feedback built into design. And team authority over specifications.

@art flow-visible
Visibility means the team can see how work flows all the way to the customer. And customer feedback, as the authors use the term, covers several practices, from gathering satisfaction metrics to feeding what customers say into design. The fourth capability gets a lesson of its own.

@art virtuous-cycle
What they found: these factors were statistically significant predictors of higher delivery performance and organizational performance, and of a better culture and less burnout. And over several years, the prediction also ran the other way, from delivery performance to Lean product practices. They call that a virtuous cycle.

@chapter Why small batches
@quote text="Working in small batches enables short lead times and faster feedback loops" cite="Forsgren, Humble and Kim, Accelerate, Chapter 8"
The box on small batches gives the reason. Working in small batches enables short lead times and faster feedback loops.

@art mvp-slice
The key is to break work into features that can be built quickly, instead of elaborate ones grown on branches and shipped seldom. At the product level, that's the MVP: a prototype with only the features needed to learn whether the product and its business model are sound.

@words text="Small batches go with continuous delivery"
Software makes small batches especially valuable, because users can answer quickly, through techniques like A B testing. And an experimental style of product work goes closely with the technical practices behind continuous delivery.

@chapter When feedback arrives
@math heading="12 one-day items · 2-day release" items="one batch: 12 + 2 = day 14@one batch;;four batches of 3: first at 3 + 2 = day 5@four batches;;last: 4 × 5 = day 20@day twenty"
Now the count, with an invented team: twelve items of a day each, and a release that costs two days, by hand. One batch of twelve means feedback on day fourteen. Four batches of three bring the first feedback on day five: three days of work plus two of release. But the last arrives on day twenty.

@math heading="Comparing the plans" items="release time: 2 days vs 8 days@eight days;;average wait: 14 vs 12.5 days@twelve and a half;;first feedback 14/5 ≈ 2.8× sooner@two point eight"
Four releases cost eight days, against two. The average wait per item is fourteen days for one batch, and twelve and a half for four. And the first feedback comes about two point eight times sooner.

@art late-finish
So small batches carry a cost the chapter doesn't discuss. When each release is costly, they finish later in total.

@math heading="Half-day release" items="one batch of 12: day 12.5@twelve point five;;four batches of 3: first day 3.5 · last day 14@three point five;;release time: 2 days@two days of release"
Now cut the release to half a day, as a deployment pipeline would. One batch arrives on day twelve point five. Four batches bring the first feedback on day three point five, and the last on day fourteen, with two days of release time in all.

@art cheap-release
The authors report that product experimentation is highly correlated with continuous delivery's technical practices. The arithmetic shows one way the two could fit: a cheaper release makes small batches affordable.

@chapter Where people slip
@list heading="Common slips" items="Ceremonies make you Lean@The first|Smaller batches finish the job sooner@The second|A lab figure is the authors' finding@And the third"
The first slip is thinking Agile ceremonies make a team Lean in its product work. The second is expecting smaller batches to finish the whole job sooner. The gain is in feedback. And the third is reading a lab figure as the authors' finding about batch size.

@chapter Try it
@words text="10 one-day items · 3-day release" sub="1 batch of 10 vs 5 batches of 2"
Your turn. Ten items of a day each, and a release costing three days. Compare one batch of ten with five batches of two. Find the first feedback, the last, and the days spent releasing. Which plan would a cheaper release help more?

@end text="Feedback first"
You can try batch sizes and release costs in the lab, on Learn. That's learn dot get er done dot I O.
