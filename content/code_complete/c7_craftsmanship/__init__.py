"""Course 7 -- Software Craftsmanship: Part VII of Code Complete (Chapters 31-35).

Four lessons, one part file: layout (Chapter 31), self-documenting code
(Chapter 32), personal character (Chapter 33), and the book's themes with its
reading list (Chapters 34-35). The design is docs/code-complete/PLAN.md, §C,
Course 7. Pages are the printed pages of the second edition (Microsoft Press,
2004).
"""

from . import part_a

COURSE = {
    "slug": "code-complete-software-craftsmanship",
    "title": "Software Craftsmanship",
    "level": "Intermediate",
    "summary": (
        "Part VII of the book, Chapters 31 to 35: Layout and Style; Self-Documenting Code; "
        "Personal Character; Themes in Software Craftsmanship; and Where to Find More "
        "Information. The earlier Parts are about what the code does. This one is about the "
        "code as something people read, and about the programmer who writes it: how layout "
        "shows a routine's structure or misstates it, what a comment can say that the code "
        "cannot, which traits McConnell finds matter and which matter less than you might "
        "think, and the themes the whole book has been arguing."
    ),
    "blurb": (
        "Find the lines whose indentation tells a different story from the one Java reads, "
        "count a routine's comments against its statements and sort them by kind, work out "
        "when a tool you write repays the hours it took, and put one routine through the "
        "book's counts to see which of its themes each count serves."
    ),
    "key": [
        "layout shows the structure Java reads",
        "an else binds to the nearest open if",
        "density is comment lines / statement lines",
        "comments say what the code cannot",
        "runs to repay is build time / saving per run",
        "warning signs are reasons to look",
    ],
    "assumes_short": "Nothing in this course",
    "assumes_long": (
        "nothing from the earlier courses, though Statements and Code Improvements make the "
        "last lesson's counts familiar; you can read a short Java routine"
    ),
    "outcomes_intro": (
        "By the end you can do, on a routine of your own, each of the acts the four chapters "
        "ask for, and say what the count does not settle."
    ),
    "outcomes": [
        ("Mark the lines whose layout misstates the code",
         "For a listing with unbraced ifs, find every line whose indentation disagrees with "
         "the structure Java gives it, and say in words what the compiler does."),
        ("Classify comments and compute their density",
         "Count a routine's comment lines and statement lines, compute comment lines per "
         "statement line, and mark each comment as repeating the code, explaining it, "
         "summarising it or stating its intent."),
        ("Compute when a tool repays its cost",
         "From the hours to build a tool, the minutes a task takes by hand and automated, and "
         "how often it runs, compute the runs and weeks to pay back and the net hours in the "
         "first year."),
        ("Measure a routine and name the theme each count serves",
         "Count a routine's decision points and nesting depth, name two improvements, and say "
         "which of Chapter 34's themes each one serves."),
        ("State Part VII's claims at their strength",
         "Say whose voice each position in the commenting dialogue is, what the chapter on "
         "character means by laziness, and why the book closes by arguing against treating "
         "any method as a religion."),
    ],
    "syllabus_intro": (
        "Four lessons in the book's order: layout, comments, character, and the themes with "
        "the book's closing pointers to further reading."
    ),
    "how_to": [
        "This course is a read-along of Steve McConnell's <em>Code Complete</em>, second "
        "edition (Microsoft Press, 2004). Section numbers and pages are that edition's; the "
        "code is written for these lessons, and none of the book's listings, tables or "
        "checklists is reproduced. Read each chapter's sections in your own copy first, then "
        "the lesson.",
        "The course can be read alone. Part VII leans on the rest of the book, and a lesson "
        "names the earlier lesson where an idea was taught, but nothing here needs it: the "
        "counts are explained where they are used.",
        "Use the labs on your own code. Every code lab takes a routine you paste in. A count "
        "is a reason to look at the code, not a verdict on it, and each lesson says what its "
        "count leaves out.",
        "Watch whose voice a sentence is in. Chapter 32 argues by a dialogue, and some of its "
        "speakers hold views McConnell does not; Chapter 34 states views in order to reject "
        "them. Each lesson says whose view it is reporting.",
    ],
    "not_covered": [
        "The book's checklists, listings and tables. Chapters 31 and 32 each end with a "
        "checklist and are built round dozens of listings; the lessons name them and point "
        "to them, because a checklist reproduced is a checklist not read.",
        "The C++ and Visual Basic layout details: pointer declarations, Visual Basic's line "
        "continuations and the like. They are named where the chapter meets them and not "
        "taught, because every snippet here is Java.",
        "Chapter 35's reading list. The lesson names how the chapter organises it and points "
        "to it; a reading list from 2004 needs your own judgement about what has been "
        "superseded, and it is the book's.",
        "The IEEE documentation standards of Section 32.6, which concern documents outside "
        "the code; the lesson names them in a sentence.",
        "Formatting tools, linters and documentation generators. Much of Chapter 31 is now "
        "done by an editor on save; the lessons say so in a sentence where it matters and "
        "teach what the tool cannot decide for you.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson states: "
        "a line is mis-indented when its leading spaces differ from the depth Java's "
        "structure gives it times the indent, a comment density is comment lines over "
        "statement lines, a payback is build time over the minutes each run saves, and a "
        "decision-point count is one plus the branches a stated rule finds. The labs read "
        "code and never run it. Figures quoted from the book are marked with their source; "
        "the payback figures are illustrative. A count says where to look."
    ),
    "lessons": part_a.LESSONS,
}
