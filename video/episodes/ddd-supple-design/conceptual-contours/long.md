---
format: long
lesson: ddd-supple-design/conceptual-contours
title: Conceptual Contours: cut the design where the domain divides
thumb: Follow the grain
---

@chapter No rule of size
@title text="Conceptual Contours" sub="Domain-Driven Design, Chapter 10" art=thumb
How should you divide a design into classes and operations? Evans starts with three habits. Chop everything fine, so the pieces can be recombined. Lump it large, to hide complexity. Or keep every class and operation to one scale.

@art monolith-and-crumbs
He calls all three oversimplifications, though each answers a real problem. A monolith duplicates what it embeds, hides what a client cares about, and mixes concepts until none is clear. Tiny pieces make the client assemble them, and a concept can vanish in the cutting.

@quote text="Half of a uranium atom is not uranium." cite="Evans, Domain-Driven Design, Chapter 10"
Half of a uranium atom is not uranium. What matters isn't only the size of the grain, but the direction it runs in.

@chapter The domain's own lines
@art wood-grain
No cookbook rule works. But most domains have a deep logical consistency, or they wouldn't work as fields of knowledge. So a model that fits one part of a domain is likely to fit parts discovered later. When it doesn't, you refactor toward deeper insight.

@words text="Expedient, or a contour?" sub="high cohesion, low coupling, for concepts"
High cohesion and low coupling apply to concepts, not only to code. At each decision, Evans asks: is this an expedient that suits the present code, or does it follow a contour of the domain? Each object should be one complete concept, Cunningham's Whole Value.

@art whole-paints
Where users have no interest in detail, keep it together. In the paint example, customers mix whole paints and never single pigments. So pigments aren't offered as separate parts.

@chapter Watch where change lands
@quote text="When successive refactoring tends to be localized, not shaking multiple broad concepts of the model, it is an indicator of model fit." cite="Evans, Domain-Driven Design, Chapter 10"
So the tool is to watch. Over several rounds of refactoring, notice what keeps changing together and what stays put. When successive refactoring tends to be localized, not shaking multiple broad concepts of the model, it is an indicator of model fit.

@art one-payment-class
His example returns to the loan model from Chapter nine. When an unforeseen requirement for early and late payments arrived, it connected to the single payment class without duplication. Not because anyone foresaw it, but because the design had been aligned with the domain's concepts.

@chapter A school timetable
@art two-divisions
The lab's model is a school timetable, written for the lesson. Nine elements, rules, clash checks and printed views, divided two ways. By processing step: checks, clashes, printing and periods. Or by concept: rooms, teachers and periods.

@list heading="Four requests in one term" items="Science labs@Science labs|Part-time teachers@part time teachers|Shorter Friday periods@shorter Friday|Large-type printouts@large type"
Four change requests arrive in one term. Science labs, part time teachers, shorter Friday periods, and large type printouts.

@math heading="term-requests" items="by step:  3 + 3 + 2 + 1 = 9 touches, 1 confined@nine module touches;;by concept:  1 + 1 + 3 + 2 = 7 touches, 2 confined@seven touches"
Divided by step, the changes touch three, three, two and one modules, nine module touches, with one change confined to a single module. Divided by concept, it's one, one, three and two, seven touches, with two confined.

@chapter Neither is local for everything
@math heading="split the term" items="rooms-and-teachers:  step 6 · concept 2@rooms and teachers;;cross-cutting:  step 3 · concept 5@cross cutting"
Now split the term. On rooms and teachers, the step division takes six touches and the concept division two. On cross cutting, short Fridays and large type, the step division takes three and the concept division five.

@art time-concept
So neither division is local for every change. Which one follows the contours depends on which changes keep arriving. If short Fridays kept recurring, the concept division would be telling the team that time is a concept it hasn't modelled yet.

@chapter Where people slip
@list heading="Common slips" items="Looking for a rule of size@The first|Expecting contours up front@The second|Reading fewer touches as proof@And the third"
The first slip is looking for a rule of size. The second is expecting to find the contours before writing the design. They're usually an outcome of refactoring. And the third is reading a lower total of touches as proof that a division fits. The total depends on which requests you list.

@chapter Try it
@code block=1 lines=1-2 focus="1@exam weeks|2@teacher cover"
Your turn. Two more requests. Exam weeks touches the room clash check, the room view and the period length rule. Teacher cover touches the free day rule, the teacher clash check and the teacher view. For each division, give the modules each request touches, the total, and how many are confined to one module.

@end text="Where does the change land?"
Enter them in the lab to check, on Learn. That's learn dot get er done dot I O.
