---
format: long
lesson: enterprise-patterns-web-presentation/model-view-controller
title: Model View Controller: which way the dependencies run
thumb: The model never sees the page
---

@chapter The verdict
@title text="Model View Controller" sub="Patterns of Enterprise Application Architecture, Chapters 4 and 14" art=thumb
Model View Controller is usually taught as three folders. Fowler reads it as two separations, and he ranks one of them far above the other.

@quote text="the separation of presentation and model is one of the most important design principles in software" cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 14, When to Use It"
Here's his verdict. The separation of presentation and model is one of the most important design principles in software. The only exception he allows is a very simple system, whose model has no real behaviour in it.

@chapter Scripts and pages
@words text="Script · Server page" sub="one reads the request, one formats the response"
Chapter four starts at the web server, which hands each URL to a program. You can write that program as a script, like a servlet, which reads the request and writes text. Or as a server page, like PHP or JSP, which is the HTML with small pieces of code inserted.

@words text="Use one for each" sub="an old idea: Model View Controller"
Scripts are best at interpreting a request. Server pages are best at formatting a response. So the obvious move is to use one for each. That move, Fowler says, is an old idea, and its name is Model View Controller.

@chapter The round trip
@art round-trip
He calls the controller here the input controller, because the word controller means several things. A request makes a round trip. The input controller pulls information off the request and hands the business logic to a model. The model talks to the data source. Then the controller gets control back, picks a view, and hands it the data.

@list heading="Three roles" items="Model: nonvisual, holds the rest@a model|View: only displays@a view|Controller: takes input, works the model@and a controller"
The pattern, which Trygve Reenskaug built for Smalltalk in the late nineteen seventies, has three roles. There's a model, which is nonvisual and holds everything but the user interface. There's a view, which only displays. And a controller, which takes input, works on the model, and has the view updated.

@chapter Separation one
@art many-presentations
The first separation is presentation from model, and Fowler gives three reasons. They're different concerns, written with different libraries, often by different people. Users want the same model shown many ways: a desktop program, a web page, a service, a terminal. And nonvisual objects are easier to test.

@art dependency-arrow
But the key point is which way the dependencies run. The presentation uses the model. The model never uses the presentation. So whoever writes the model needn't know which presentation is in use, and the presentation can change freely.

@code block=1 lines=1-18 label=Java focus="2-11@a Concert|13-18@a ConcertView"
Here's the lesson's own listing. A Concert, with an act and a venue. And a ConcertView, which renders it as a heading, using an escape routine from the HTML library. ConcertView needs the HTML library and Concert. Concert needs neither.

@chapter Count the reach
@art ripple-reached
The lab makes this a count. Suppose the concert model learns to format itself with the HTML library. Now concert uses html, and both the concert page and a concert report use concert. Change the HTML library, and see what it reaches.

@math heading="model-knows-html: change html" items="direct: concert = 1@one class directly;;reached: concert, concertpage, concertreport = 3@three in all"
The change reaches one class directly, concert. Following the records backwards, it reaches three in all: concert, the page, and the report. And the report has nothing to do with HTML. It's reached only because the model knew about HTML.

@math heading="separated: change html" items="direct: concertpage = 1@directly;;reached: concertpage = 1@and one in all"
Now separate them, as in the listing. The page uses concert and html, and the report uses concert. The same change reaches the page directly, and one in all. A change below the presentation stops at the presentation.

@art ripple-stopped
Being reached doesn't mean being edited. It means the class has to be looked at, rebuilt and tested again. The count tells you where to look, not whether a dependency is needed. That's still a design rule.

@chapter Separation two
@art three-roles
The second separation, view from controller, Fowler calls less important. The irony is that almost every version of Smalltalk didn't make it. It came back on the web, where the input controller is its own object, and most of chapter fourteen is built on it.

@chapter Where people slip
@list heading="Common slips" items="Three folders is the pattern@The first|Business logic in the controller@The second|The view-controller split is the point@And the third"
The first slip is taking the pattern to be three folders. A model that calls an HTML routine breaks it, however it's filed. The second is putting the business logic in the controller. It belongs in the model, where every presentation can share it. And the third is thinking the view controller split is the point. Fowler ranks it second.

@chapter Try it
@code block=2 lines=1-4 label=Records focus="1@basket uses widgets|2-4@the checkout page"
Your turn. A small shop. Basket uses widgets, a library that draws form controls. The checkout page uses basket and widgets, and a basket API uses basket. Which classes does a change to widgets reach directly, and in all? Then remove the first record, and count again.

@end text="Trace a change yourself"
You can paste dependency records into the lab and watch how far a change reaches, on Learn. That's learn dot get er done dot I O.
