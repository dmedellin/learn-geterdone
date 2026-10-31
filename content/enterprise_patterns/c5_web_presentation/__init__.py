"""Course 5 -- Web Presentation: Chapters 4 and 14 of Patterns of Enterprise
Application Architecture.

Six lessons in one module: part_a reads Chapter 4, Web Presentation, with the
seven patterns of Chapter 14, Web Presentation Patterns. Pages are PDF pages of
the operator's copy, in source comments only. Fowler et al., Patterns of
Enterprise Application Architecture (Addison-Wesley, 2002). The design is
docs/enterprise-patterns/PLAN.md, section C, Course 5.
"""

from . import part_a

COURSE = {
    "slug": "enterprise-patterns-web-presentation",
    "title": "Web Presentation",
    "level": "Intermediate",
    "summary": (
        "Chapter 4, Web Presentation, read with the seven patterns of Chapter 14, Web "
        "Presentation Patterns: Model View Controller as the separation underneath; Page "
        "Controller and Front Controller, the two ways to write the input controller; "
        "Template View and Transform View, the two ways to write the view; Two Step View, "
        "the variation that puts the look in one place; and Application Controller, for "
        "the order of screens. Each lesson sets out Fowler's argument and then counts, on "
        "Java written for the lesson, what the pattern changes in the code: what a change "
        "reaches, how many decisions a page holds, and which lines several controllers "
        "repeat."
    ),
    "blurb": (
        "Put a web front on a layered system, the way Fowler's Chapter 4 does. Trace what "
        "an HTML change reaches when the model knows about HTML, count the decisions in a "
        "page controller and a template and move them to a helper, find what page "
        "controllers repeat and remove it with a superclass or one handler, count what a "
        "change of look reaches with one stage and two, and move a flow written twice "
        "into one method."
    ),
    "key": [
        "the presentation depends on the model",
        "one controller per action, or one for all",
        "a helper decides; the page only asks",
        "a template: the page, with markers",
        "a second stage: the look in one place",
        "machine leads the flow: one controller",
    ],
    "assumes_short": "Layers and Performance",
    "assumes_long": (
        "Layers and Performance, for the three layers and why the presentation sits on "
        "top of the domain and never the other way round; the code is short Java, and a "
        "reader of any C-family language can follow it"
    ),
    "outcomes_intro": (
        "By the end you can do, on a small design or a short controller or view, the "
        "counts these chapters make in words, and say in Fowler's terms what each count "
        "shows and what it leaves to you."
    ),
    "outcomes": [
        ("Trace what a presentation change reaches",
         "List what a change to an HTML library reaches directly and in all, with the "
         "model dependent on the library and independent of it, and say why the direction "
         "of the dependency decides the count."),
        ("Count and place a controller's decisions",
         "Count the decision points in a page controller or a page fragment by a stated "
         "rule, sort them into request, domain and view, and write the helper methods "
         "that take the view's decisions out of the page."),
        ("Find what controllers repeat",
         "Mark the lines two page controllers share, remove them with a superclass and "
         "with a front handler, and name the reasons Fowler gives for one handler that a "
         "count of lines cannot see."),
        ("Count the reach of a change of look",
         "List what a site-wide change of look reaches with one stage and with a logical "
         "screen and a renderer, and what a change to the logical screen itself reaches."),
        ("Put a flow in one place",
         "Apply Fowler's test of who controls the flow, mark the flow rules two "
         "controllers repeat, and write the one method that returns the next screen."),
    ],
    "syllabus_intro": (
        "Six lessons follow Chapter 14's patterns in the book's order, each read with the "
        "part of Chapter 4 that introduces it: the separation underneath, the two input "
        "controllers, the two views, the two-stage variation, and the controller of flow."
    ),
    "how_to": [
        "Read the chapter before the lesson. This is a read-along of Martin Fowler, with "
        "David Rice, Matthew Foemmel, Edward Hieatt, Robert Mee and Randy Stafford, "
        "<em>Patterns of Enterprise Application Architecture</em> (Addison-Wesley, 2002), "
        "Chapter 4 and Chapter 14, with code written for these lessons. Each lesson names "
        "its sections and patterns, opens with at most one short quotation, and sets out "
        "the argument in its own words; the book's own examples are better read in the "
        "book.",
        "Read the narrative as an argument and the pattern as a tool. Chapter 4 is a "
        "short argument about how a web request should be handled and a page produced; "
        "each Chapter 14 pattern is a description to look up, with its own When to Use "
        "It. Every lesson pairs the two, and Fowler's hedges are kept: several of these "
        "patterns, by his own account, earn their cost only on some sites.",
        "Every lab in this course reuses the Code Complete kit, because what each of "
        "these patterns changes is code: which classes a change reaches, how many "
        "decisions a page or controller holds, and which lines several controllers "
        "repeat. The rules each lab counts by are stated beside it, and the bands beside "
        "a decision count are McConnell's, not Fowler's. A count is a reason to look, not "
        "a verdict.",
        "Paste your own code. Every lesson ends by sending you to a controller, template "
        "or design of your own, and the labs take whatever you paste or type. Nothing you "
        "paste leaves your browser.",
    ],
    "not_covered": [
        "The book's listings, sketches and worked examples. Chapter 14's examples, in "
        "Java servlets and JSP, XSLT and ASP.NET, are named in the lessons and not "
        "reproduced, and its example domain is left to the book.",
        "Servlet, JSP and ASP.NET specifics. The book's advice on configuring a web "
        "server, custom tags and code-behind is tied to the platforms of 2002, and is "
        "named, not taught; the snippets use a small stand-in for a request and a "
        "response.",
        "Rich clients and JavaScript frameworks. Fowler mentions rich-client interfaces "
        "where they bear on Model View Controller, such as the observer that keeps "
        "several views of one model in step; presentation built in the browser comes "
        "after the book and is named once, in Template View and Transform View, and not "
        "taught.",
        "Running code. The labs read code and dependency records and never run them, so "
        "they cannot tell you whether a page renders or a flow is right; the exercises "
        "ask you to check a few by hand.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson "
        "states: what a change reaches by following its dependency records backwards, "
        "decision points by the rule beside each listing, and repeated lines by matching "
        "them as text. The code and the designs are written for these lessons; the one "
        "figure quoted from the book is marked as its illustration. A count says where to "
        "look, not what you will find."
    ),
    "lessons": part_a.LESSONS,
}
