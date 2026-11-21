---
format: long
lesson: enterprise-patterns-web-presentation/page-controller
title: Page Controller: one handler for each action
thumb: Move the choice of view
---

@chapter The mess
@title text="Page Controller" sub="Patterns of Enterprise Application Architecture, Chapters 4 and 14" art=thumb
You may have written a controller like this. It began by finding one record and showing it. Then it grew a branch for every case the page had to handle.

@quote text="Things get a lot more messy when you have to make decisions based on the input, such as different display formats for classical and jazz albums." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 4"
Fowler writes this about server pages. Things get a lot more messy when you have to make decisions based on the input, such as different display formats for classical and jazz albums.

@chapter One per action
@art one-path-one-file
The most common design, he says, gives every page on the site its own input controller. Page Controller starts from the simplest model of the web: one path leads to one file. Each logical page gets its own controller, a script or a server page.

@art one-link-many-pages
But the match isn't quite one to one. The more precise thought is a controller for each action, a button or a link. That's because one link can lead to different pages, depending on some condition.

@chapter Three jobs
@list heading="A page controller" items="Decode the URL and form data@decodes the URL|Create and call the model@creates and calls|Choose the view, forward the data@decides which view"
The pattern gives the controller three jobs. It decodes the URL and any form data. It creates and calls the model objects, passing them everything they need from the request, so the model never touches the request. And it decides which view shows the result, and forwards the data to it.

@art helper-object
A server page that's also the controller makes a good view, but a poor controller. Once there's logic, it fills with awkward scriptlets. Fowler's way out is a helper object the page calls first, or a script that does the controlling and forwards to a server page.

@chapter Count the decisions
@code block=1 lines=1-13 label=Java focus="3@finds a concert|4-5@if there's no concert|6-7@sold out|8-9@seated|10-11@otherwise"
Here's the lesson's controller. It finds a concert, then spends the rest choosing one of four views. If there's no concert, a missing page. If it's sold out, a waitlist. If it's seated and has a seat map, the seats page. Otherwise, tickets.

@math heading="concert-page" items="1 + if 3 + && 1 = 5@one, plus three;;deepest nesting 1, first at line 5@deepest nesting"
The lab counts decision points: one, plus one for each if, while, for and case, and one for each and and or. An else adds nothing. That's one, plus three ifs, plus one and, which makes five. The deepest nesting is one, first at line five.

@chapter Sort them
@art branching-controller
Leave aside the one every routine starts with. Of the four decisions, the null test is about the request: was there such a concert? Sold out, seated, and has a seat map are questions the concert answers. And using those answers to pick a page is presentation.

@code block=2 lines=1-6 label=Java focus="4@finds the concert|5@forwards"
So move that choice to a helper on the presentation side. Now the controller finds the concert, asks the helper for a view, and forwards. That's all.

@math heading="concert-page-split" items="decision points: 1@prints one;;deepest nesting 0, first at line 4@nesting of zero"
On the split preset, the lab prints one, with a nesting of zero, first reached on line four.

@art helper-split
The four branches haven't disappeared. They've moved to a helper method, viewFor, which holds the same tests and returns the page's name. The model keeps only its own predicates, and never names a page. What you gain is a place to test the decisions: hand it a sold out concert, and check the name, with no web server.

@chapter Where people slip
@list heading="Common slips" items="A page controller is a page@The first|Moving a decision removes it@The second|Handling every URL the same way@And the third"
The first slip is thinking a page controller is a page. It's one for each action. The second is thinking that moving a decision removes it. It moves where you can test it. And the third is handling every URL the same way.

@art mixed-urls
Teams that insist on one style end up with pages full of scriptlets, or many trivial scripts that only pass the request through. Fowler's advice is a server page where there's little controller logic, and a script where there's more. The two patterns mix, too: a site moving to a Front Controller often has both.

@chapter Try it
@code block=3 lines=1-17 label=Java focus="4@no booking or no seats|9@between one and eight|11@paid and not refundable"
Your turn. This controller changes the seats on a booking. It checks for no booking or no seats, for a number between one and eight, and for a booking that's paid and not refundable. Count its decision points by the lab's rule. Then sort them: the request, the booking's own rules, and the choice of page.

@end text="Count a controller yourself"
You can paste a controller into the lab and count its decisions, on Learn. That's learn dot get er done dot I O.
