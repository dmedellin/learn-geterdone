---
format: long
lesson: enterprise-patterns-web-presentation/two-step-view
title: Two Step View: change the look of a site in one place
thumb: One renderer for every page
---

@chapter The problem
@title text="Two Step View" sub="Patterns of Enterprise Application Architecture, Chapters 4 and 14" art=thumb
You change a site's look. A new header, a different style of table. And you find the change waiting in every page's template.

@quote text="Two Step View's key value comes from the separation of first and second stages, allowing you to make global changes more easily." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 14, When to Use It"
That's the problem this pattern answers. Two Step View's key value comes from the separation of first and second stages, allowing you to make global changes more easily.

@chapter One stage or two
@art every-page-template
In a single stage view, there's mostly one view component per screen, and it turns the domain's data straight into HTML. So the decision about which HTML to use is spread across every screen.

@art two-stages
A two stage view breaks that in two. First, the domain data becomes a logical screen: fields, headers, tables, choices, but no HTML at all. Then a second stage turns that logical screen into HTML. There's one first stage for each screen, and only one second stage for the application.

@art one-renderer
The second stage knows each kind of element and how to show it. So every formatting decision is made in one place, and a global change to the HTML is one object to alter. You can build it as two XSLT stylesheets, as classes for the elements, or as templates written in logical tags.

@chapter The arithmetic
@art many-looks
It works even better with several looks. Fowler's example is several airlines in front of one reservation system, each with its own second stage. And the same goes for different devices.

@math heading="10 screens, 3 appearances" items="single stage: 10 × 3 = 30 view modules@thirty;;two stages: 10 + 3 = 13@thirteen"
Here are his own figures. Ten screens and three appearances need thirty single stage view modules. With two stages, you need thirteen: ten for the screens, and three for the looks. The saving grows with both numbers.

@chapter The code
@code block=1 lines=1-20 label=Java focus="2-9@a Field|11-19@HtmlRenderer"
Here's the lesson's listing. A Field is the smallest logical screen there is: a label and a value. HtmlRenderer is a second stage. It takes any list of fields and writes them as a definition list. Want every field on the site shown as a table instead? You change render, and nothing else.

@chapter Count the reach
@math heading="one-step: change look" items="direct: concertpage, tourpage, venuepage = 3@three directly;;reached in all: the same 3@same three"
The lab is the ripple count from the first lesson. In one step, three pages each format their own HTML, so each depends on look. Change look, and it reaches three directly, and the same three in all.

@math heading="two-step: change look" items="direct: renderer = 1@renderer directly;;reached in all: renderer = 1@one in all"
In two step, the pages depend on the logical screen, and only the renderer depends on look. The same change reaches the renderer directly, and one in all. That's the global change, made in one class.

@words text="Reached ≠ edited" sub="but in one-step, every reached page holds HTML"
Being reached isn't the same as being edited. But here it matters. In one step, each page holds its own HTML, so every page reached is a page to edit. In two step, only the renderer holds any.

@chapter The cost
@art design-intensive
The gain lasts only while every screen keeps to one logical layout. A site built on visual design, where each page should look unlike the others, won't find a good logical screen. Designers using visual editors can't write a renderer, so programmers join every design change. And it's a harder model to learn, though not difficult once you're used to it.

@chapter Where people slip
@list heading="Common slips" items="Two templates per page@The first|Every change gets cheaper@The second|It suits every site@And the third"
The first slip is thinking it means two templates per page. It's one first stage per page, and one second stage for the site. The second is thinking every change gets cheaper. A change of look does. And the third is expecting it to suit every site. Design intensive sites are constrained by it.

@chapter Try it
@art screen-change-ripple
So which change becomes the expensive one? The logical screen is now something everything depends on.

@code block=2 lines=1-7 label=Records focus="1-3@three pages|4-5@a browser renderer|6-7@a print renderer"
Here's a site with three pages, a browser renderer, and a print renderer, each renderer with its own look. Change screen, the logical screen, and work out by hand what it reaches directly and in all. Then compare it with a change to look.

@end text="Trace a change of look"
You can paste these records into the lab and watch a change spread, on Learn. That's learn dot get er done dot I O.
