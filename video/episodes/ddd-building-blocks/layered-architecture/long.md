---
format: long
lesson: ddd-building-blocks/layered-architecture
title: Layered Architecture: give the domain a layer of its own
thumb: No arrow points up
---

@chapter The problem
@title text="Layered Architecture" sub="Domain-Driven Design, Chapter 4" art=thumb
The code that actually solves the business's problem is usually a small part of a program. Evans's point is that it matters far more than its size.

@art one-action-many-steps
A single user action needs code to draw the screen, query the database, check the input, record the choice and commit it. Only one of those steps is about the business.

@art tangled-layers
When screen and storage code are written straight into business objects, and business rules into widgets and database scripts, the domain becomes very hard to see. A cosmetic change to the screen can alter a rule. And it happens because it's the quickest way to make something work today.

@chapter Four layers
@list heading="Four layers" items="User interface@user interface|Application: thin, directs the work@application layer|Domain: the heart of the software@domain layer|Infrastructure: generic technical help@infrastructure"
Evans uses the layering most of the industry already uses. The user interface shows information and interprets commands. The application layer defines the jobs and directs domain objects to do them, and stays thin, with no business rules. The domain layer holds the concepts and rules, the heart of business software. And the infrastructure layer supplies generic technical help.

@quote text="The essential principle is that any element of a layer depends only on other elements in the same layer or on elements of the layers “beneath” it." cite="Evans, Domain-Driven Design, Chapter 4"
And there's one rule. The essential principle is that any element of a layer depends only on other elements in the same layer, or on elements of the layers beneath it.

@chapter Speaking upward
@art callback-up
So how does a lower layer tell a higher one something? Not by calling it. It goes through an indirect mechanism: a callback, or the Observer pattern. Infrastructure, meanwhile, should know nothing in particular about the domain it serves.

@art framework-cage
Evans adds a caution about frameworks that make every domain object extend their base class. Use a framework selectively, for the hard technical problems, and keep the model free. In the end, domain driven design needs only one layer to exist: the domain layer, where the model lives.

@chapter Count the arrows
@math heading="tangled" items="8 dependencies@there are eight;;5 down · 1 within · 2 up@five downward;;Loan → LoanScreen · LoanStore → LendCopy@Loan to LoanScreen"
The lab takes a library's lending feature, puts each class in a layer, and counts the dependencies. On the tangled preset there are eight: five downward, one within a layer, and two upward, Loan to LoanScreen and LoanStore to LendCopy. One more, LendCopy to Mailer, skips the domain layer, which is allowed.

@code block=1 lines=1-10 label=Java focus="3@holds a screen|6-9@markOverdue"
Here's the first upward dependency in code. Loan holds a screen. When markOverdue runs, it tells the screen directly. Now the domain can't be compiled, tested or read without the screen, and every new screen that cares means another field in Loan.

@code block=2 lines=1-16 label=Java focus="2-4@declares a listener|7@list of listeners|12-14@tells each listener"
The fix turns the arrow round. The domain declares a listener interface, which the screen implements. Loan keeps a list of listeners, and tells each listener when it falls overdue. It knows nothing about screens.

@math heading="callbacks" items="10 dependencies@ten dependencies;;7 down · 3 within · 0 up@seven downward;;3 skip a layer@skipping"
Do the same for storage, and the lab counts ten dependencies: seven downward, three within a layer, and none upward, with three skipping a layer. There are more arrows than before, and none of them points up.

@art arrows-down
So read the count as a reason to look. The remedy adds an interface rather than removing a connection. And the lab can't tell whether Loan belongs in the domain. It takes your word for each layer, and that assignment is the design.

@chapter A later view
@art hexagon-centre
Alistair Cockburn's hexagonal architecture, published the year after the book, puts the domain at the centre, with storage implementing interfaces the domain declares. On that view, storage pointing inward is the design. The two agree on what matters most to Evans: the domain must not depend on the screens or the storage.

@chapter Where people slip
@list heading="Common slips" items="Layers exist to swap the UI@The first|Business rules in the application layer@The second|Using every framework feature@And the third"
The first slip is thinking the layers exist so the user interface can be swapped. Projects rarely do that. The second is putting business rules in the application layer. And the third is using every feature of an architectural framework.

@chapter Try it
@words text="SmsGateway → BookVisit · Clinician → BookingPage" sub="a clinic's seven dependencies"
Your turn. A clinic has seven dependencies across the same four layers. Sort each into downward, within a layer, or upward. Two candidates to look at closely: SmsGateway to BookVisit, and Clinician to BookingPage. Say which layer would declare the interface that turns each one round.

@end text="Find the arrows that point up"
Then type the records into the lab and check, on Learn. That's learn dot get er done dot I O.
