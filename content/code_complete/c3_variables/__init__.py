"""Course 3 -- Variables: Part III of Code Complete, Chapters 10-13 (pp. 237-344).

Six lessons, one part file: two on Chapter 10 (initialisation; scope, span
and live time), one on Chapter 11 (names), two on Chapter 12 (numbers; named
constants and the other fundamental types) and one on Chapter 13 (structures,
pointers and global data). The design is docs/code-complete/PLAN.md, Course 3.
"""

from . import part_a

COURSE = {
    "slug": "code-complete-variables",
    "title": "Variables",
    "level": "Intermediate",
    "summary": (
        "Part III of the book, Chapters 10 to 13: General Issues in Using Variables; The "
        "Power of Variable Names; Fundamental Data Types; and Unusual Data Types. McConnell "
        "goes down from routines to the single variable: how it is declared and initialised, "
        "how far apart its references lie and how long it stays live, what it is called, what "
        "Java's integers and floating-point numbers do with it, why its literals should have "
        "names, and why global data is best reached through access routines. Each lesson "
        "measures the chapter's point on a short Java routine written for it."
    ),
    "blurb": (
        "Read Part III a chapter at a time. Find the variables a routine reads before it sets "
        "them, measure how long each one stays live, average the length of its names, see "
        "what Java prints when an int overflows or a tenth is added ten times, list its magic "
        "numbers, and count the routines a global variable couples together."
    ),
    "key": [
        "initialise each variable close to its use",
        "live time: last line - first line + 1",
        "names: describe the problem, not the code",
        "an int wraps silently past 2147483647",
        "only 0 and 1 belong in the body as literals",
        "reach global data through access routines",
    ],
    "assumes_short": "Creating High-Quality Code",
    "assumes_long": (
        "the two courses before it, Laying the Foundation and Creating High-Quality Code, above "
        "all the argument that managing complexity is software's primary technical imperative, "
        "and enough Java to read a short routine"
    ),
    "outcomes_intro": (
        "By the end you can read a routine variable by variable and say, in the book's terms, "
        "what each of Part III's chapters would have you look at, and do the count each "
        "lesson's lab does without the lab."
    ),
    "outcomes": [
        ("Find a routine's data-flow anomalies",
         "Read a routine top to bottom and list every variable read before it is set, set "
         "twice with no use between, or set and never used, and say which of them Java's "
         "compiler rejects."),
        ("Measure span and live time",
         "Given the lines on which variables are referenced, compute each span, the average "
         "span and each live time, and move declarations to shrink them."),
        ("Name for the problem",
         "List a routine's declared names with their lengths, average them without loop "
         "indexes, and rename the short ones for what they stand for."),
        ("Predict Java's arithmetic",
         "Say whether an int sum or product overflows, which way it wraps and how to fix it, "
         "and why a decimal fraction added as a double is not the exact result."),
        ("Root out literals and contain global data",
         "List a routine's magic numbers and declare the constants that replace them; count "
         "the routines a global couples and the places that touch it, with and without access "
         "routines."),
    ],
    "syllabus_intro": (
        "Six lessons follow Part III's order. Chapter 10 is split at Section 10.4, between "
        "initialisation and scope, and Chapter 12 at Section 12.4, between numbers and the "
        "other types."
    ),
    "how_to": [
        "Read the chapter before the lesson. Each lesson names the sections and pages it "
        "covers in the second edition (Microsoft Press, 2004), and the section numbers are "
        "that edition's. This course is a read-along of Steve McConnell's <em>Code "
        "Complete</em>: it sets out each chapter's argument in its own words and quotes at most "
        "a sentence or two, so the book's own examples and checklists are better read in the "
        "book. The code in every lesson is written for these lessons.",
        "Four of the six labs read code: you paste a Java routine into the box and the lab "
        "counts what the chapter says to count, by the rules printed under the listing. The "
        "lab for Integers and Floating Point does Java's arithmetic on a number you give it, "
        "and the lab for Structures, Pointers and Global Data reads a list of which routine "
        "reads or writes which global. Paste a routine of your own into each code lab before "
        "you leave the lesson; the last step of every lesson asks you to.",
        "Treat every count as a reason to look. A live time of sixteen lines or a name of "
        "three letters does not make a routine wrong, and McConnell says himself that no one "
        "has found the number that separates a good live time from a bad one. The lessons say "
        "what each count measured and what to look at next.",
        "Keep Java's own checks in view. Java's compiler already rejects some of what these "
        "chapters warn about, a local variable read before it is set among them, and does "
        "nothing about others, such as integer overflow. Each lesson says which is which, and "
        "where C or Python behaves differently.",
    ],
    "not_covered": [
        "Pointers in C and C++. Section 13.2 gives many pages to pointer arithmetic, memory "
        "allocation and C++ references; Java has no pointer type, so the lesson names what the "
        "section covers and teaches only its general advice, which is the same as for global "
        "data: put the risky operations behind a few routines.",
        "The book's tables and checklists. The Data Literacy Test, the tables of good and bad "
        "names and of naming conventions for several languages, the integer ranges and the "
        "end-of-chapter checklists are named where they matter and not reproduced; read them "
        "in the book.",
        "Naming conventions for C, C++ and Visual Basic in detail. Section 11.4's sample "
        "conventions per language are summarised, not taught, and the Hungarian convention is "
        "described only as far as Section 11.5 describes its idea.",
        "Floating-point arithmetic in depth. The lessons show what Java prints and why; they "
        "do not teach the binary format, error analysis or the algorithms Section 12.3 points "
        "to.",
        "Strings in C, Unicode and localisation. Section 12.4's advice on character sets and "
        "C string routines is named in one sentence.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the code or the numbers "
        "a lesson states: anomalies by reading the lines in order, spans and live times as "
        "differences of line numbers, a mean of name lengths, Java's int, long and double "
        "arithmetic simulated exactly, and the pairs of routines a global couples. The one "
        "study figure quoted, on name length, is the book's report of Gorla, Benander and "
        "Benander (1990). None of the counts says whether a routine is good; each says where "
        "to look."
    ),
    "lessons": part_a.LESSONS,
}
