---
format: long
lesson: enterprise-patterns-web-presentation/template-and-transform-view
title: Template View and Transform View: keep the logic out of the page
thumb: The helper decides, the page asks
---

@chapter The problem
@title text="Template View and Transform View" sub="Patterns of Enterprise Application Architecture, Chapters 4 and 14" art=thumb
You may know this template. It began as HTML with a few markers. Now it has a condition for every special case.

@quote text="This clearly provides a lot of power and flexibility; sadly, it also leads to very messy code that's difficult to maintain." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 4"
Fowler is writing about server pages, which let a page hold a whole programming language. This clearly provides a lot of power and flexibility; sadly, it also leads to very messy code that's difficult to maintain.

@chapter Two decisions
@list heading="Three view patterns" items="Template View or Transform View@Template View or|One stage or Two Step View@one stage"
There are three view patterns, and they give you two decisions. Template View or Transform View. And either one in one stage, or as a Two Step View, which is the next lesson.

@chapter Template View
@art template-markers
Writing a program that produces HTML is hard. Writing a static page in an editor is easy. So Template View writes the page as a static page, with markers that are replaced by computed results when it's served. People who aren't programmers can lay it out.

@art scriptlet-mess
Server pages go further and allow scriptlets, and Fowler calls that a big problem. Designers can't edit the page. A page is a poor module for a program. And domain logic creeps in and gets duplicated. The worst code he'd seen in recent years, he says, was server page code.

@art helper-beside-page
His answer is a helper object for each page, a regular class holding the real logic, so the page holds only calls to it. For conditional display, he calls purely conditional tags a bad smell. A condition should ask the helper one true or false question.

@chapter Transform View
@art transform-walk
Transform View is organised the other way round. A template follows the output. A transform follows the input: a program walks the domain data, and as it recognises each element, it writes out the HTML for it. It can be any language. XSLT was the dominant choice when the book was written.

@art two-pages-compared
The choice, Fowler says, comes down mostly to what the team prefers and the tools it has. A template lets a designer lay out the page, but makes it easy to let logic in, and it's hard to test outside a web server. A transform stays focused on rendering, and is easy to test.

@chapter Count the decisions
@code block=1 lines=1-13 label=Java focus="4@seats left is under ten|9@resale"
Here's the lesson's ticket row, standing in for a server page. It decides inline whether to mark the seats as few, if seats left is under ten or it's the last release. And whether to label them resale.

@math heading="ticket-row" items="1 + if 2 + && 1 + || 1 = 5@five decision points;;deepest nesting 1, first at line 5@deepest nesting"
The lab prints five decision points: one, plus two ifs, plus one and, plus one or. The deepest nesting is one, first at line five. Nobody can change this row's markup without reading both conditions.

@code block=2 lines=1-11 label=Java focus="5-7@isFew|8-10@showResale"
Now give the conditions to a helper. TicketHelper has two methods, isFew and showResale. Each returns its condition, instead of branching on it. The template would hold two markers, each asking one Boolean.

@math heading="ticket-helper" items="1 + && 1 + || 1 = 3@prints three;;the ifs are gone; the connectives stay@the ifs are gone"
The lab prints three: one, plus one and, plus one or. The ifs are gone, but the two connectives are still there. And three isn't a figure for either method. It's the whole listing, counted from one.

@words text="5 → 3 is not the point"
So the count fell from five to three, and that's not the point. The decisions moved to a class you can test by building a ticket and asking it, with no web server. And the markup moved to a page a designer can edit.

@chapter Where people slip
@list heading="Common slips" items="No code means nothing conditional@The first|Transform View needs XSLT@The second|The two differ only in syntax@And the third"
The first slip is thinking a template with no code can't show anything conditional. A helper decides, and a marker asks. The second is thinking Transform View needs XSLT. Any language will do. And the third is thinking the two differ only in syntax. They differ in organisation: the output's structure, or the input's.

@chapter Try it
@code block=3 lines=1-13 label=Java focus="3@on sale|9@out of stock"
Your turn. A price cell, built inline. It checks whether the item is on sale, and whether it's out of stock, withdrawn or recalled. Count its decision points, with the breakdown. Then name the helper methods a template would call instead, and say what each returns.

@art site-wide-change
And notice one thing left over. A site wide change of look can still mean editing every template. The next lesson puts the look in one place.

@end text="Count a view yourself"
You can paste HTML building code into the lab and count its decisions, on Learn. That's learn dot get er done dot I O.
