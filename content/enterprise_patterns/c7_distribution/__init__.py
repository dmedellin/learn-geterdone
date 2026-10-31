"""Course 7 -- Distribution and Putting It Together: Chapters 7, 8 and 15, with
Plugin and Service Stub from Chapter 18.

Five lessons in one part file: Distribution Strategies (Chapter 7), Remote
Facade and Data Transfer Object (Chapter 15), Putting It All Together and Other
Layering Schemes (Chapter 8), and Plugin and Service Stub (Chapter 18, by David
Rice and Matt Foemmel, and by Rice). The source is Fowler et al., Patterns of
Enterprise Application Architecture (Addison-Wesley, 2002); PDF pages of the
operator's copy are in comments beside each lesson. The design is
docs/enterprise-patterns/PLAN.md, section C, Course 7.
"""

from . import part_a

COURSE = {
    "slug": "enterprise-patterns-distribution",
    "title": "Distribution and Putting It Together",
    "level": "Intermediate",
    "summary": (
        "Chapter 7, Distribution Strategies; Chapter 15, Distribution Patterns (Remote "
        "Facade and Data Transfer Object); Chapter 8, Putting It All Together, with its "
        "section Other Layering Schemes; and two of Chapter 18's Base Patterns, Plugin and "
        "Service Stub. When to cross a process boundary, how to cross it when you must, and "
        "Fowler's own summary of the book. Each lesson sets out the chapter's argument and "
        "counts its trade-off on a stated situation: the calls that cross a node and what "
        "they cost, the round trips a facade removes, the bytes a transfer object carries, "
        "the price of three deployments of one stack, and what a change to a network "
        "library reaches with and without a stub."
    ),
    "blurb": (
        "Decide what, if anything, runs on another machine. Price a design's calls across "
        "nodes, count the round trips a Remote Facade saves and the bytes a Data Transfer "
        "Object sends, compare three deployments of the same layers, and see what a Plugin "
        "and a Service Stub keep a test from reaching."
    ),
    "key": [
        "first law: do not distribute your objects",
        "remote interfaces are coarse-grained",
        "a facade translates; it holds no logic",
        "send too much rather than call twice",
        "advice prods thinking; it is no recipe",
        "a stub lets the tests run without it",
    ],
    "assumes_short": "Layers and Performance",
    "assumes_long": (
        "Layers and Performance, for the three layers, latency and Separated Interface, and "
        "enough of the domain and database courses to know what a Domain Model, a mapper and "
        "a Unit of Work are; the code is short Java"
    ),
    "outcomes_intro": (
        "By the end you can price the calls of a design whose parts run on different "
        "machines, and say in the chapters' terms what each figure shows and what only "
        "measuring your own system can show."
    ),
    "outcomes": [
        ("Price a distribution by class",
         "Given the calls between classes and the node each runs on, count the remote calls "
         "and compute the time, its remote share and its ratio to one node."),
        ("Count what a Remote Facade saves",
         "Compute the time of fine-grained calls across a network against the facade's "
         "coarse calls, for a latency and a work time, and the share of it spent waiting."),
        ("Weigh a Data Transfer Object",
         "Compute one getter a field against one object carrying every field, the bytes it "
         "sends that the screen never shows, and what the saved round trips could have carried."),
        ("Compare deployments of one stack",
         "Count the calls that cross a node for one request under several deployments of "
         "the same layers, and say which boundaries Chapter 7 says you will usually have to keep."),
        ("Keep a test off the network",
         "List what a change to a network library reaches with a direct dependency and "
         "with a Separated Interface, a Service Stub and a Plugin."),
    ],
    "syllabus_intro": (
        "Five lessons in the book's order: Chapter 7's case against distributed objects; "
        "Chapter 15's two patterns for the boundaries you cannot remove; Chapter 8's summary "
        "of the whole book and its comparison with other layering schemes; and Chapter 18's "
        "Plugin and Service Stub, which read back to Separated Interface in the first course."
    ),
    "how_to": [
        "Read the chapter before the lesson. This is a read-along of Fowler et al., "
        "<em>Patterns of Enterprise Application Architecture</em> (Addison-Wesley, 2002), "
        "with code written for these lessons. Each lesson names its chapter, sections and "
        "patterns, opens with at most one short quotation, and sets out the argument in its "
        "own words; the book's examples, worked in full in Part 2, are better read in the "
        "book. Plugin is by David Rice and Matt Foemmel and Service Stub by Rice, as the "
        "book names them.",
        "Hold the First Law throughout. Chapter 7 says not to distribute your objects, and "
        "the rest of the course is about the places where you must. Four of the five labs "
        "count calls across a boundary and price them from a latency the lesson states; the "
        "last counts what a change to a network library reaches.",
        "Treat every time as the lesson's. The labs multiply the calls you give them by the "
        "costs you give them. A remote call at a thousand times a local one is the "
        "lesson's ratio, not your network's; Fowler's rule is to measure your own "
        "configuration.",
        "Price your own system. Every lesson ends by sending you to a boundary, a screen, "
        "an API response, a deployment or a test of your own, with a count to make. Nothing "
        "you type leaves your browser.",
    ],
    "not_covered": [
        "The web-services and messaging technologies of 2002. SOAP, XML over HTTP, session "
        "and entity beans, and .NET's data sets are named as the book names them, not "
        "taught.",
        "Asynchronous, message-based distribution. Fowler says he prefers it and leaves its "
        "patterns out of the book; the lessons say so and follow the book's synchronous, "
        "call-based model.",
        "The book's examples and listings: the album service behind Remote Facade, the "
        "transfer objects and assemblers of Data Transfer Object, the identity generator of "
        "Plugin and the tax service of Service Stub. Every snippet here is new, with its "
        "own domain.",
        "What has happened to distribution since 2002. One lesson, Putting It All Together, "
        "sets services and microservices beside Chapter 7 in its note; the rest read the "
        "book as written.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson states: "
        "a time is the calls you list multiplied by the costs you give, a share and a ratio "
        "are divisions of those times, the bytes a transfer object sends are the fields you "
        "list, and what a change reaches is a walk along the dependencies you type. The code "
        "and the designs are written for these lessons; figures quoted from the book are "
        "marked as the book's. A count models the situation, not your system."
    ),
    "lessons": part_a.LESSONS,
}
