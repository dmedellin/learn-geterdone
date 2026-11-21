---
format: long
lesson: gof-behavioral-objects/observer
title: Observer: one change, how many updates?
thumb: Twenty one updates, or thirteen?
---

@chapter Keeping in step
@title text="Observer" sub="Design Patterns, chapter 5" art=thumb
Observer is probably the pattern you've used most without naming it: listeners, subscribers, events. It's simple to write. What's hard is seeing what one change actually costs, and the book warns about exactly that.

@quote text="A seemingly innocuous operation on the subject may cause a cascade of updates to observers and their dependent objects." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Chapter 5"
That warning is from the consequences. A seemingly innocuous operation on the subject may cause a cascade of updates to observers and their dependent objects. The book also calls the pattern Dependents, and Publish Subscribe.

@art table-and-chart
The motivation is a toolkit that keeps application data apart from its views. A table and a chart of the same data can each be reused alone, yet a change typed into one shows up at once in the other. Neither view knows the other exists. Both depend on the data.

@chapter The pattern
@list heading="Participants" items="Subject@the subject|Observer@the observer|Concrete subject@concrete subject|Concrete observer@concrete observer"
There are four participants. The subject knows its observers, and lets them attach and detach. The observer declares the updating interface. A concrete subject holds the state they care about, and notifies them when it changes. And a concrete observer keeps its own state in step.

@code block=1 lines=1-20 label=Java focus="2@pull model|8-9@attach and detach|11-14@a sale|17-19@tells every observer"
Here's the lesson's seat plan, for a theatre box office. The update uses the pull model: the plan passes itself, and each observer asks what it needs. Observers attach and detach. And a sale changes the state first, then notifies. The notify loop tells every observer, every time.

@words text="Make the state consistent, then notify"
That order matters. Observers query the subject as they update, so a subclass that notifies through an inherited operation and then changes more state has notified too early. The book's remedy is a template method that notifies last.

@chapter What it buys, and costs
@art broadcast
The benefits: subjects and observers vary independently, and observers can be added without touching anything else. The coupling is abstract and minimal. And communication is broadcast. The notification names no receiver, and each observer handles it or ignores it.

@art cascade
The liability is the opening quote. Observers can't see each other, so none can see what a change will cost in all. Loosely kept dependencies give spurious updates that are hard to trace. And the simple protocol doesn't say what changed.

@art push-pull
Two choices shape it. Who calls notify? If the subject does, clients can't forget, but a run of changes sends a run of updates. And push or pull? Push makes observers less reusable, because the subject assumes what they need. Pull may be inefficient.

@chapter Count it
@art box-office
In the lab, the subjects are seats, prices and the schedule. The seat map watches seats and prices, the kiosk all three, the mailer the schedule, and the nightly report the seats. So seats have three observers, prices two, and the schedule two.

@math heading="Each change notifies at once" items="sale: 3@a sale;;reprice: 2 + 3 = 5@a re pricing;;matinee: 2 + 2 + 3 = 7@a new matinee;;exchange: 3 + 3 = 6@an exchange;;3 + 5 + 7 + 6 = 21@twenty one"
A sale changes seats: three updates. A re pricing changes prices, then seats: two plus three, five. A new matinee changes all three: seven. An exchange changes seats twice: six. That's twenty one updates, for four operations.

@art change-manager
Now route them through a change manager, an instance of Mediator, that waits for the end of each operation, and sends one update to each observer of anything it changed. That's three, three, four and three: thirteen. Eight fewer.

@words text="21 − 13 = 8 redundant" sub="redundant is the book's word, not a fault"
Redundant is the book's word, and it isn't a fault. The simple manager, it says, is fine when several updates do no harm. The count doesn't weigh them: a kiosk redraw and a log line count the same.

@chapter Where people slip
@list heading="Common slips" items="Thinking a change is cheap@The first|Notifying too early@The second|Reading redundant as a defect@And the third"
The first slip is treating a change as cheap because the subject does so little. Every observer does its own work, and may be a subject in turn. The second is notifying before the subject is consistent. And the third is reading redundant updates as a defect.

@chapter Try it
@words text="A garden irrigation controller" sub="dawn: soil, rain · shower: rain, rain, soil"
Your turn. Soil and rain are the subjects. The valve and the panel watch both, the phone watches rain. Count the changes, the updates sent directly, and the updates through a change manager.

@end text="Count the updates"
Then type the design into the lab and check, on Learn. That's learn dot get er done dot I O.
