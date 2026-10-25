"""System Considerations, lessons 1-4 -- Code Complete, Part VI, Chapters 27-30.

One lesson per chapter. Every quotation is copied from McConnell, Code
Complete, 2nd edition (Microsoft Press, 2004); the comment beside each lesson
gives its pages. Every figure attributed to the book carries its id in the
register of figures (docs/code-complete/PLAN.md, section S.2) and its page.
The labs are cckit's family 2 and 3 views: the instances are the lessons'
own, and the book's figures arrive in the cfg, never from the kit.
"""

# Lesson 3's exercise: a call graph written as Java, for the reader to read
# the calls off before listing stubs and drivers. Its records are
# app, ui; app, core; core, store; ui, core.
INTEGRATION_EXERCISE = """\
class App {
    void start() {
        Ui.show();
        Core.load();
    }
}

class Ui {
    static void show() { Core.load(); }
}

class Core {
    static void load() { Store.read(); }
}

class Store {
    static void read() { }
}"""

# Lesson 4's exercise: the build the lab's records describe, as the
# dependency lines of a makefile (the recipe lines, which make indents with a
# tab, are left out). Its records are app, main.o; app, util.o; main.o,
# main.c; main.o, util.h; util.o, util.c; util.o, util.h.
MAKEFILE_EXERCISE = """\
app: main.o util.o
main.o: main.c util.h
util.o: util.c util.h"""

# The build the ripple lab reads, in the kit's records (target, prerequisite).
BUILD_EDGES = ("app, main.o; app, util.o; main.o, main.c; main.o, util.h; "
               "util.o, util.c; util.o, util.h")

# The call graph the integrate lab reads, in the kit's records (caller, callee).
CALL_EDGES = "main, ui; main, orders; ui, widgets; orders, pricing; orders, db; pricing, db"

LESSONS = [
    # ---------------------------------------------------------------- 01
    # McConnell Chapter 27, pp. 649-659: §27.1 p. 650, §27.2 p. 651, §27.3
    # p. 651 (Table 27-1, p. 652), §27.4 p. 653 (Table 27-2), §27.5 p. 654.
    # Opening quotation: Key Points, p. 659 (21 words). "right-weight":
    # p. 658 (1 word). Quotations in all: 22 words.
    # F1, p. 654 (construction's share: as much as 65% small, about 50% medium).
    # F2, p. 652 (construction errors about 75% small, about 50% larger;
    #   up to 75% on some 500,000-line projects, Grady 1987).
    # F24, p. 652 (Table 27-1, after Jones 1977 and 1998).
    # F25, p. 653 (Table 27-2, after Putnam and Meyers 1992 and 1997,
    #   Boehm et al. 2000, Cusumano et al. 2003).
    {
        "slug": "how-program-size-affects-construction",
        "title": "How Program Size Affects Construction",
        "module": "Chapter 27 · Program Size",
        "one_line": "A larger project is not a small one made bigger: communication grows with the square of the team, errors per line rise and output per person falls.",
        "summary": (
            "Chapter 27 argues that scaling a project up changes its kind as well as its size. "
            "Count the communication paths in a team, work the book's tables of defect density "
            "and productivity into ranges for three sizes, and see how wide the ranges the book "
            "itself gives are."
        ),
        "key": [
            "paths = n·(n − 1)/2",
            "defects = KLOC × errors per KLOC",
            "staff-years = lines / lines per year",
            "spread = high rate / low rate",
            "larger: more errors per line, less per head",
            "construction: a smaller share as size grows",
        ],
        "key_label": "Chapter 27 in six lines",
        "concepts_intro": (
            "The chapter has one claim and three measures of it. Each measure is a ratio, and "
            "each grows or shrinks faster than the size it is taken against."
        ),
        "concepts": [
            ("Communication paths",
             "A path is a pair of people who may need to talk. Among n people there are "
             "n·(n − 1)/2 of them, so the count grows with the square of the team, not in "
             "proportion to it. Two people have one path; ten have forty-five."),
            ("Error density",
             "Errors found per thousand lines of code, written KLOC. Table 27-1, which the "
             "book takes from Jones, gives a range of densities for each band of project size, "
             "and both ends of the range rise as the size does."),
            ("Productivity",
             "Lines of code per staff-year, a staff-year being one person's work for a year. "
             "Table 27-2 gives a range for each size, from Putnam and Meyers, Cocomo II and "
             "Cusumano's survey, and the ranges fall as the size grows."),
        ],
        "read_title": "The chapter's argument, then the book's tables at three sizes",
        "read_intro": (
            "The first half follows Chapter 27 section by section. The second puts the book's "
            "rows for three project sizes into the lab and reads what the ranges say."
        ),
        "body": [
            ("p", "<strong>Chapter 27, Key Points, p. 659.</strong> &ldquo;All other things "
                  "being equal, a large project will have more errors per thousand lines of "
                  "code than a small one.&rdquo; The chapter is short, pages 649 to 659; read "
                  "it in your own copy before going on, Tables 27-1 and 27-2 especially, since "
                  "the lesson uses a few of their figures and does not reproduce them."),
            ("p", "What happens when a project grows? The obvious answer is that everything "
                  "grows with it, and Chapter 27 argues that the obvious answer is wrong. "
                  "McConnell opens with a hypothetical product whose next version is to be ten "
                  "times the size, and says the effort, the errors and the mix of work will "
                  "each grow by a different and larger factor. A large project, in his account, "
                  "is a different kind of thing, and a team used to small ones can find its "
                  "first large one getting out of hand."),
            ("p", "Section 27.1 (p. 650) gives the first reason. One programmer has one path "
                  "of communication, with the customer. Add people and the paths are not "
                  "added; they multiply, because each new person may need to talk to every "
                  "person already there. The book's figure draws them for teams of two, three, "
                  "four, five and ten people: one path, then three, six, ten and forty-five. Every path is time spent "
                  "talking and a chance of being misunderstood, which is why large projects "
                  "formalise communication in documents: fifty people read and write documents "
                  "rather than talk in every combination."),
            ("def", ("Communication paths in a team of n",
                     "Each pair of people is one path. There are n choices for the first "
                     "person and n − 1 for the second, and each pair is counted twice that "
                     "way, so the team has n·(n − 1)/2 paths.")),
            ("p", "Section 27.2 (p. 651) asks whether your project is a typical size, and "
                  "answers that no size is. Most projects are done by small teams, but because "
                  "large projects use many more people each, a large share of all programmers "
                  "work on large ones. Section 27.3 (p. 651) turns to errors. As size grows, "
                  "more of them come from requirements and design: the book puts construction "
                  "at about 75 percent of the errors on small projects and about 50 percent on "
                  "larger ones, while noting that on some very large projects construction "
                  "still accounts for up to three quarters. And the density rises. Table 27-1, "
                  "after Jones, gives 0 to 25 errors per thousand lines for projects under 2K "
                  "lines and 4 to 100 for projects of 512K lines or more."),
            ("p", "Section 27.4 (p. 653) does the same for productivity. On small projects the "
                  "single biggest influence is the individual programmer's skill; as size grows, "
                  "the team and its organisation matter more. Table 27-2 gives the lines of code "
                  "per staff-year the book's sources report: 2,000 to 25,000 at 10K lines, "
                  "1,000 to 20,000 at 100K, 700 to 10,000 at a million. McConnell says plainly "
                  "that the specific figures vary dramatically with the kind of software, the "
                  "people, the language and how lines are counted, and that the trend is what "
                  "matters. These are other people's projects, averaged; your own records are "
                  "the test of them."),
            ("p", "Section 27.5 (p. 654) follows the shift into the work itself. Construction "
                  "takes as much as 65 percent of the time on a small project and about 50 "
                  "percent on a medium one, and less again on a large one, because detailed "
                  "design, coding, debugging and unit testing grow roughly in proportion to "
                  "size while communication, planning, integration and system testing grow "
                  "faster. McConnell's chart of the shares stops at 512K lines, he says, to "
                  "protect his job. The section ends on methodology: every team has one, chosen "
                  "or not, and the book reports Boehm and Turner's advice that a light method "
                  "scaled up tends to serve better than a heavy one pared down, the aim being a "
                  "&ldquo;right-weight&rdquo; method for the project in front of you."),
            ("h3", "The book's rows, at three sizes"),
            ("p", "The lab takes a team size, a size in thousands of lines and one row from "
                  "each table, and does four pieces of arithmetic. Communication paths is "
                  "n·(n − 1)/2. Defects multiplies the size by each end of the density range. "
                  "Staff-years divides the lines by each end of the productivity range, the "
                  "fast end first. Spread of the productivity range divides the high by the low: how many "
                  "times the slowest estimate exceeds the fastest. The <code>small-team</code> "
                  "preset is three people on 10K lines, with the 2K&ndash;16K density row "
                  "(0 to 40) and the 10K productivity row: 3 paths, 0&ndash;400 defects, "
                  "2/5 = 0.40 to 5 staff-years, and a spread of 25/2 = 12.50."),
            ("p", "The <code>medium</code> preset is ten people on 100K lines, with the "
                  "64K&ndash;512K density row (2 to 70) and the 100K productivity row: 45 "
                  "paths, 200&ndash;7,000 defects, 5&ndash;100 staff-years, a spread of 20. "
                  "The <code>large-team</code> preset is fifty people on a million lines, with "
                  "the top density row and the 1,000K productivity row: 1,225 paths, "
                  "4,000&ndash;100,000 defects, 100 to 10000/7 &asymp; 1,428.57 staff-years, "
                  "and a spread of 100/7 &asymp; 14.29. On the lesson's illustration the team "
                  "grew about seventeenfold and the paths about four hundredfold."),
            ("p", "Read the spread before anything else. At every size the book's own "
                  "productivity range is at least ten times wide, so the staff-years are an "
                  "order of magnitude wide too, and that is the honest result: the table is a "
                  "snapshot of an industry, not a forecast for your project. What the figures "
                  "do show is the direction McConnell argues for. Every figure here is the lab's "
                  "arithmetic on the book's rows; none is a measurement of a project, and a "
                  "large range is a reason to find your own organisation's numbers."),
            ("h3", "Exercise"),
            ("ul", [
                "A team of 6 people grows to 12.",
                "Everyone may need to talk to everyone else, as in the chapter's figure.",
            ]),
            ("p", "Compute the communication paths before and after the team grows, and how "
                  "many times larger the second count is than the first. Do it by hand; then "
                  "type each team size into the lab's People box to check."),
            ("p", "The paths among people are one cost of size; the next chapter asks how "
                  "construction on such a team is managed and estimated. The next lesson is "
                  "&ldquo;Managing Construction&rdquo;."),
        ],
        "lab": ("cckit", {
            "mode": "project",
            "view": "scale",
            "preset": "small-team",
            "presets": [
                {"id": "small-team",
                 "label": "3 people, 10K lines (rows 2K–16K and 10K)",
                 "people": 3, "kloc": 10, "densityLow": 0, "densityHigh": 40,
                 "prodLow": 2000, "prodHigh": 25000,
                 "expect": {"pjPaths": "3", "pjDefects": "0–400", "pjStaffYears": "2/5 = 0.40 to 5", "pjSpread": "25/2 = 12.50"}},
                {"id": "medium",
                 "label": "10 people, 100K lines (rows 64K–512K and 100K)",
                 "people": 10, "kloc": 100, "densityLow": 2, "densityHigh": 70,
                 "prodLow": 1000, "prodHigh": 20000,
                 "expect": {"pjPaths": "45", "pjDefects": "200–7,000", "pjStaffYears": "5–100", "pjSpread": "20"}},
                {"id": "large-team",
                 "label": "50 people, 1,000K lines (rows 512K or more and 1,000K)",
                 "people": 50, "kloc": 1000, "densityLow": 4, "densityHigh": 100,
                 "prodLow": 700, "prodHigh": 10000,
                 "expect": {"pjPaths": "1,225", "pjDefects": "4,000–100,000", "pjStaffYears": "100 to 10000/7 ≈ 1,428.57", "pjSpread": "100/7 ≈ 14.29"}},
            ],
            "panel_title": "Paths, defects and staff-years by size",
            "panel_intro": (
                "Each preset takes one row from each of the book's tables for its size. The "
                "densities and productivities are the book's quotations of other people's "
                "averages; the lab multiplies and divides them, and cannot say what your "
                "project will see. Figures: the book's Table 27-1 (p. 652), after Jones 1977 "
                "and 1998, and Table 27-2 (p. 653), after Putnam and Meyers, Boehm et al. 2000 "
                "and Cusumano et al. 2003."
            ),
        }),
        "steps_title": "Working a size through the book's tables",
        "steps_intro": "Five steps, the last of which is your own project's.",
        "steps": [
            ("Count the paths",
             "Multiply the team size by one less than itself and halve it. Three people have "
             "3 paths; fifty have 1,225."),
            ("Find the rows",
             "Put the size in thousands of lines into the band of Table 27-1 that contains "
             "it, and into the nearest row of Table 27-2. A 100K-line project falls in the "
             "64K–512K density band."),
            ("Multiply and divide",
             "Multiply the size in KLOC by each end of the density range for defects. Divide "
             "the size in lines by each end of the productivity range for staff-years; the "
             "high productivity gives the low figure."),
            ("Take the spread",
             "Divide the high productivity by the low. That ratio is how wide the staff-year "
             "range is, and it is the first thing to report alongside it."),
            ("Place your own project",
             "Type your team's size and your project's size in thousands of lines into the "
             "lab with the book's rows for that size. Note the paths, the defect range and the "
             "staff-year range, and write one sentence comparing the staff-years with what "
             "your project actually took."),
        ],
        "worked": {
            "title": "Fifty people on a million lines",
            "intro": [
                "Take the large-team preset: fifty people, a million lines, the book's 4 to 100 "
                "errors per KLOC and 700 to 10,000 lines per staff-year for that size.",
            ],
            "lines": [
                "paths: 50 × 49 / 2 = 1,225",
                "defects: 1,000 × 4 = 4,000 up to 1,000 × 100 = 100,000",
                "fast end: 1,000,000 / 10,000 = 100 staff-years",
                "slow end: 1,000,000 / 700 ≈ 1,428.57 staff-years",
                "spread: 10,000 / 700 ≈ 14.29",
            ],
            "after": [
                "Each figure is arithmetic on the book's rows. The spread says the slow end of "
                "the staff-year range is more than fourteen times the fast end, which is why the "
                "chapter leans on the trend and not on any one figure.",
            ],
        },
        "quiz_title": "Size, paths and the book's tables",
        "quiz": [
            {"q": "A team grows from 6 people to 12, and everyone may need to talk to everyone "
                  "else. How many communication paths are there before and after?",
             "a": ["12 before, 24 after", "15 before, 66 after", "30 before, 132 after",
                   "36 before, 144 after"],
             "c": 1,
             "why": "Each pair is one path, n·(n − 1)/2: 6 × 5 / 2 = 15 and 12 × 11 / 2 = 66, "
                    "so doubling the team multiplies the paths by 4.4. Twelve and 24 count "
                    "people, not pairs; 30 and 132 count every pair twice; 36 and 144 are n "
                    "squared, which also pairs each person with themselves."},
            {"q": "Table 27-1, after Jones, gives 2 to 70 errors per KLOC for projects of "
                  "64K to 512K lines. What range of errors does that give a 200K-line project?",
             "a": ["2 to 70", "400 to 14,000", "100 to 10,000", "800 to 20,000"],
             "c": 1,
             "why": "200 KLOC lies in the 64K–512K band, so 200 × 2 = 400 and 200 × 70 = 14,000 "
                    "(F24, Table 27-1, p. 652, after Jones 1977 and 1998). 2 to 70 is the "
                    "density, not the count; 100 to 10,000 uses the 16K–64K row (0.5 to 50), and "
                    "800 to 20,000 the row for 512K or more (4 to 100)."},
            {"q": "Table 27-2 gives 1,000 to 20,000 lines per staff-year at 100K lines. What "
                  "staff-year range does it give a 100,000-line project, and how many times the "
                  "fast end is the slow end?",
             "a": ["5 to 100 staff-years; 20 times", "5 to 100 staff-years; 95 times",
                   "0.05 to 1 staff-year; 20 times", "100 to 2,000 staff-years; 20 times"],
             "c": 0,
             "why": "100,000 / 20,000 = 5 and 100,000 / 1,000 = 100, and 20,000 / 1,000 = 20 "
                    "(F25, p. 653). 95 is the difference of the ends, not their ratio; 0.05 to "
                    "1 divides the size in thousands, not in lines; 100 to 2,000 multiplies by "
                    "the spread instead of dividing by the rates."},
            {"q": "What does Section 27.5 say happens to construction's share of a project's "
                  "time as the project grows?",
             "a": ["It stays about the same, since coding grows with the lines",
                   "It falls: as much as 65 percent on a small project, about 50 on a medium one",
                   "It rises, since a larger project has more code to write",
                   "It falls to nothing past 512K lines"],
             "c": 1,
             "why": "The book gives as much as 65 percent on small projects and about 50 on "
                    "medium ones, falling further on large ones (F1, p. 654), because other "
                    "activities grow faster than construction. Construction does grow with the "
                    "lines, but its share falls. Cutting the chart off at 512K is McConnell's "
                    "joke about protecting his job, not a claim that construction vanishes."},
        ],
        "mistakes": [
            ("Thinking a ten-times-larger program is ten times the work",
             "It is the natural model: twice the lines, twice the effort. Chapter 27 argues "
             "against it on three counts. Error density rises with size (Table 27-1, after "
             "Jones), productivity falls (Table 27-2), and communication grows with the square "
             "of the team, so the work that is not construction grows faster than the work that "
             "is. On the lesson's illustration the team grows from 3 people to 50 and the paths "
             "from 3 to 1,225. The tables' ranges are wide, but at every size they move the same "
             "way."),
            ("Thinking construction's errors stop mattering on a large project",
             "Requirements and design errors do take a larger share as size grows, and a reader "
             "can conclude that construction is a minor source of trouble on big systems. The "
             "book's figures do not support that: construction is about half the errors on "
             "larger projects, about three quarters on small ones, and on some very large "
             "projects still up to three quarters (F2, p. 652). Half of a larger number of "
             "errors is still the largest single share."),
            ("Starting from a heavy method and paring it down",
             "A team that expects to grow may adopt the full apparatus of a large-project "
             "methodology at once and plan to drop what a small project does not need. The book "
             "reports Boehm and Turner's finding that the reverse tends to work better: start "
             "light and add formality as size demands it, aiming for a method of the right "
             "weight for the project actually in hand."),
        ],
        "standard": (
            "Finish when you can work a team and a size through the book's tables by hand.",
            "Given a team size, a size in thousands of lines and the book's rows for that size, "
            "compute the communication paths, the defect range, the staff-year range and the "
            "ratio of the productivity range's ends, each exactly, and say which of the four is "
            "a count and which are the book's averages."
        ),
        "note": (
            "The lab multiplies and divides; the figures it works on are the book's quotations "
            "of Jones, Putnam, Boehm and Cusumano, averages over projects mostly finished before "
            "2004, and McConnell says the specific figures vary dramatically. The path count "
            "assumes everyone may need to talk to everyone, as the chapter's figure does; a "
            "team that is organised into smaller groups has fewer paths, which is the point of "
            "organising it. Nothing here can say how many errors your project will have."
        ),
    },
    # ---------------------------------------------------------------- 02
    # McConnell Chapter 28, pp. 661-688: §28.1 p. 662, §28.2 p. 664, §28.3
    # p. 671 (Table 28-1, p. 674; what to do if you're behind, pp. 675-676;
    # Brooks's law and its qualification, p. 676), §28.4 p. 677, §28.5 p. 680
    # (individual variation, p. 682), §28.6 p. 686. Brooks and OS/360: pp. 658
    # and 687. Opening quotation: Key Points, p. 688 (35 words); the lesson
    # quotes nothing else.
    # F26, p. 674 (Table 28-1, after Boehm et al. 2000; percentages and the
    #   multipliers they give).
    # F29, p. 682 (order-of-magnitude differences among programmers, Sackman,
    #   Erikson and Grant 1968 and later studies).
    {
        "slug": "managing-construction",
        "title": "Managing Construction",
        "module": "Chapter 28 · Managing Construction",
        "one_line": "Managing construction means encouraging good code, controlling change, estimating and measuring, and remembering that programmers are people; an estimate is a range that tightens as the project goes.",
        "summary": (
            "Chapter 28 covers the parts of management that touch construction: standards, "
            "configuration management, estimation, measurement and people. Turn the book's "
            "effort factors from Cocomo II into multipliers, apply them to a nominal estimate, "
            "and see how far two or three factors move it."
        ),
        "key": [
            "effort = nominal × each multiplier",
            "−24 percent is a multiplier of 0.76",
            "+34 percent is a multiplier of 1.34",
            "estimate several ways and compare",
            "estimate again as the project goes",
            "more people means more paths",
        ],
        "key_label": "Chapter 28 in six lines",
        "concepts_intro": (
            "Three terms carry the chapter's estimating sections, and one of them carries the "
            "lab."
        ),
        "concepts": [
            ("Configuration management",
             "Identifying a project's artifacts and handling changes to them systematically, so "
             "that the system keeps its integrity over time; the book's other name for it is "
             "change control. It covers requirements and design changes, version control of the "
             "code, the tools' own versions and backups."),
            ("A nominal estimate",
             "The effort a model gives a project of a given size before any of its particular "
             "circumstances are taken into account. Cocomo II, Boehm's estimation model, then "
             "multiplies it by one factor for each circumstance: the team's capability, the "
             "product's complexity, the memory the program may use."),
            ("An effort multiplier",
             "A factor's influence written as a number to multiply by. Table 28-1 prints each "
             "factor's influence as a percentage, helpful or harmful; −24 percent becomes 0.76 "
             "and +34 percent becomes 1.34. A multiplier of 1 changes nothing."),
        ],
        "read_title": "The chapter's argument, then three estimates adjusted",
        "read_intro": (
            "The first half follows Chapter 28's six sections in order. The second applies a few "
            "of Table 28-1's factors to one nominal estimate and reads how far they move it."
        ),
        "body": [
            ("p", "<strong>Chapter 28, Key Points, p. 688.</strong> &ldquo;Good software "
                  "estimation is a significant challenge. Keys to success are using multiple "
                  "approaches, tightening down your estimates as you work your way into the "
                  "project, and making use of data to create the estimates.&rdquo; Read the "
                  "chapter, pages 661 to 688, in your own copy first; Section 28.3 is the one "
                  "the lab works on."),
            ("p", "Someone has asked you how long the next feature will take, and you gave a "
                  "number. Chapter 28 is written for that moment and the ones around it, from "
                  "both sides: it tells a developer what a manager has to worry about, and a "
                  "manager how construction looks from the developer's chair. It covers only the "
                  "parts of management that touch construction, and points to other books for "
                  "the rest."),
            ("p", "Section 28.1 (p. 662) asks how to encourage good code, and advises against "
                  "standards handed down from management. Programmers, McConnell says, tend to "
                  "rank managers somewhere between single-celled organisms and the woolly "
                  "mammoth, so if there are to be standards, a respected architect should set "
                  "them and the team should accept them. Lighter means work too: two people on "
                  "every part of the code, a review of every line, good code circulated as an "
                  "example, and code treated as the project's property rather than its "
                  "author's."),
            ("p", "Section 28.2 (p. 664) is configuration management. Without control, changes "
                  "to requirements leave code written for features that are later dropped, and "
                  "changes to code leave a version that seems tested when only its predecessor "
                  "was. The book's advice for requirements and design changes is to handle them "
                  "in groups rather than as each occurs to you, to estimate the cost of each "
                  "including its ripple through design, code, tests and documents, and to treat a "
                  "high volume of change as a sign that the upstream work was not finished. For "
                  "code it is version control, and backups whose restore has actually been "
                  "tried. Its warning runs both ways: the systemic risk is overcontrol, but "
                  "McConnell reports seeing far more projects suffer from no change control "
                  "than from too much."),
            ("p", "Section 28.3 (p. 671) is estimation. The book lists several approaches, from "
                  "estimating software and algorithmic models such as Cocomo II to estimating the "
                  "pieces and adding them up, and a procedure it adapts from Boehm's 1981 book: "
                  "establish why you need the estimate, give the estimate time of its own, spell "
                  "out the requirements, estimate at a low level of detail so that the pieces' "
                  "errors tend to cancel, use several techniques and compare them, and estimate "
                  "again as the project goes. Then come the influences on the schedule. Table "
                  "28-1, from Boehm and his colleagues' Cocomo II, gives each factor a helpful "
                  "and a harmful percentage: programmer capability −24 and +34 percent, "
                  "requirements analyst capability −29 and +42, product complexity −27 and +74."),
            ("p", "What if you are behind? Hoping to catch up rarely works: the survey the "
                  "book cites found delays growing toward a project's end, not shrinking. Adding people is the move the book weighs most "
                  "carefully, by way of Fred Brooks, who managed IBM's OS/360 and wrote "
                  "<em>The Mythical Man-Month</em> about it. His law, as the book cites it from "
                  "the 1995 edition, is that adding people to a late project makes it later: new "
                  "people must learn the project, their teaching takes the time of those who "
                  "know it, and more people means more communication. One woman can have a baby "
                  "in nine months; nine women cannot have one in a month. McConnell heeds the "
                  "warning and then qualifies it (p. 676): where the tasks can be divided and "
                  "done independently, people added late can help. The other remedy is to cut "
                  "the scope."),
            ("p", "Section 28.4 (p. 677) argues that any measurement of a project is better than "
                  "none, that people work on what is measured, and that most measures are best "
                  "used to find outliers, routines worth a second look. Section 28.5 (p. 680) "
                  "treats programmers as people. The book reports differences of an order of "
                  "magnitude among programmers of similar experience, from Sackman, Erikson and "
                  "Grant in 1968 and many studies since, and lists the &ldquo;religious&rdquo; "
                  "issues, such as braces, naming and the choice of IDE, on which a manager "
                  "should suggest rather than rule. Section 28.6 (p. 686), on managing your manager, recommends educating "
                  "the manager over the alternatives it lists, which include finding another "
                  "job."),
            ("h3", "One estimate, three sets of factors"),
            ("p", "The lab takes a nominal estimate and a list of factors, each with its "
                  "multiplier, and prints two figures. Product of the multipliers is the factors "
                  "multiplied together; Adjusted effort is the nominal estimate times that "
                  "product. Multiplying the factors is how Cocomo II combines them; the book "
                  "prints the percentages and leaves the arithmetic to the model it cites. Every "
                  "preset starts from 100 staff-months. The <code>strong-team</code> preset "
                  "applies a capable programming team, 0.76, and capable requirements analysts, "
                  "0.71: the product is 1349/2500 &asymp; 0.54, and the adjusted effort "
                  "1349/25 = 53.96 staff-months."),
            ("p", "The <code>weak-team</code> preset applies the same two factors at their "
                  "harmful ends, 1.34 and 1.42: 4757/2500 &asymp; 1.90, and 4757/25 = 190.28 "
                  "staff-months. The <code>hard-product</code> preset leaves the people alone "
                  "and applies the product's complexity, 1.74, a tight time constraint, 1.63, "
                  "and a tight storage constraint, 1.46, the last two being how much of the "
                  "machine's run time and memory the program itself will use, not the "
                  "schedule: 1035213/250000 &asymp; 4.14, and "
                  "1035213/2500 &asymp; 414.09 staff-months. Two factors about the people, "
                  "nothing about the product, move the same nominal estimate from about half to "
                  "nearly twice; three about the product, more than fourfold."),
            ("p", "That spread is the lab's arithmetic on Boehm's figures, and it is the "
                  "chapter's argument in numbers: an estimate made before you know the team "
                  "and the product is a range, and the way to narrow it is the one the "
                  "quotation names, several approaches, data, and a new estimate as each "
                  "factor becomes known. The multipliers are averages Boehm's team fitted to "
                  "other people's projects; your own records are the test of them, and the lab "
                  "cannot say which factors apply to you."),
            ("h3", "Exercise"),
            ("ul", [
                "A nominal estimate of 50 staff-months.",
                "Programmer capability at the harmful end of Table 28-1: +34 percent.",
                "Use of software tools at the helpful end: −22 percent.",
            ]),
            ("p", "Turn the two percentages into multipliers, multiply them, and give the "
                  "adjusted effort in staff-months. Work it by hand first; then put 50 in the "
                  "Nominal effort box and the two factors in the Factors box, each as a name, "
                  "a comma and its multiplier, to check."),
            ("p", "An estimate assumes the pieces will fit together; the next chapter is about "
                  "the order in which they are made to. The next lesson is "
                  "&ldquo;Integration Order&rdquo;."),
        ],
        "lab": ("cckit", {
            "mode": "project",
            "view": "effort",
            "preset": "strong-team",
            "nominal": 100,
            "presets": [
                {"id": "strong-team",
                 "label": "Capable programmers and analysts (0.76, 0.71)",
                 "factors": "programmer capability, 0.76; requirements analyst capability, 0.71",
                 "expect": {"pjProduct": "1349/2500 ≈ 0.54", "pjEffort": "1349/25 = 53.96"}},
                {"id": "weak-team",
                 "label": "Weak programmers and analysts (1.34, 1.42)",
                 "factors": "programmer capability, 1.34; requirements analyst capability, 1.42",
                 "expect": {"pjProduct": "4757/2500 ≈ 1.90", "pjEffort": "4757/25 = 190.28"}},
                {"id": "hard-product",
                 "label": "A complex product, short of run time and memory (1.74, 1.63, 1.46)",
                 "factors": ("product complexity, 1.74; time constraint, 1.63; "
                             "storage constraint, 1.46"),
                 "expect": {"pjProduct": "1035213/250000 ≈ 4.14", "pjEffort": "1035213/2500 ≈ 414.09"}},
            ],
            "panel_title": "A nominal estimate adjusted by effort factors",
            "panel_intro": (
                "Each multiplier is one of Table 28-1's percentages written as a factor: "
                "−24 percent is 0.76, +34 percent is 1.34. The lab multiplies them, as Cocomo II "
                "does, and applies the product to the nominal estimate in staff-months. Figures: the "
                "book's Table 28-1 (p. 674), after Boehm et al. 2000, Cocomo II."
            ),
        }),
        "steps_title": "Adjusting an estimate by its factors",
        "steps_intro": "Five steps, the last of which is your own estimate's.",
        "steps": [
            ("Start from a nominal estimate",
             "Take the effort before any circumstance is counted, in staff-months. The lab's "
             "presets use 100."),
            ("Turn each percentage into a multiplier",
             "Add the percentage to 100 percent: −29 percent gives 0.71, +42 percent gives 1.42. "
             "A factor at its neutral setting is 1 and can be left out."),
            ("Multiply the multipliers",
             "Multiply them together rather than adding the percentages. Two helpful factors of "
             "−24 and −29 percent give 0.76 × 0.71 ≈ 0.54, not 1 − 0.53 = 0.47."),
            ("Apply the product, and state the range",
             "Multiply the nominal estimate by the product. Then work the same factors at their "
             "other ends, so that you report the range the factors span and not one figure."),
            ("Revisit your own last estimate",
             "Take an estimate you gave recently, choose the two factors from Table 28-1 you "
             "would apply to it now, type them into the lab with your figure as the nominal, and "
             "write down the adjusted effort beside what the work actually took."),
        ],
        "worked": {
            "title": "A capable team",
            "intro": [
                "Take the strong-team preset: a nominal 100 staff-months, programmer capability "
                "at −24 percent and requirements analyst capability at −29 percent.",
            ],
            "lines": [
                "programmers: 1 − 0.24 = 0.76",
                "analysts: 1 − 0.29 = 0.71",
                "product: 0.76 × 0.71 = 0.5396",
                "effort: 100 × 0.5396 = 53.96 staff-months",
            ],
            "after": [
                "The lab prints the product as 1349/2500 ≈ 0.54, the fraction exact and the "
                "decimal to two places. Turn the same two factors to their harmful ends and the "
                "estimate is 190.28: the factors alone span more than a factor of three.",
            ],
        },
        "quiz_title": "Factors, estimates and Brooks's law",
        "quiz": [
            {"q": "A nominal estimate is 50 staff-months. Programmer capability is at +34 "
                  "percent and use of software tools at −22 percent. Multiplying the factors, "
                  "as Cocomo II does, what is the adjusted effort?",
             "a": ["56 staff-months", "52.26 staff-months", "67 staff-months",
                   "106 staff-months"],
             "c": 1,
             "why": "The multipliers are 1.34 and 0.78, and 1.34 × 0.78 = 1.0452, so the effort "
                    "is 50 × 1.0452 = 52.26 staff-months (F26, Table 28-1, p. 674, after Boehm "
                    "et al. 2000). Adding the percentages, 1 + 0.34 − 0.22 = 1.12, gives 56; "
                    "ignoring the tools gives 50 × 1.34 = 67; adding the multipliers, "
                    "1.34 + 0.78 = 2.12, gives 106."},
            {"q": "Table 28-1 gives requirements analyst capability a helpful influence of −29 "
                  "percent. What multiplier does that put on the effort?",
             "a": ["0.29", "0.71", "1.29", "0.971"],
             "c": 1,
             "why": "A change of −29 percent leaves 100 − 29 = 71 percent of the effort, a "
                    "multiplier of 0.71 (F26, p. 674). 0.29 is the reduction, not what is left; "
                    "1.29 treats the helpful influence as harmful; 0.971 takes 2.9 percent off "
                    "rather than 29."},
            {"q": "The book states Brooks's law and then qualifies it (p. 676). When, it says, "
                  "can people added to a late project help?",
             "a": ["Never; the law has no exceptions",
                   "When the project's tasks can be divided and done independently",
                   "When the people added are more capable than those already there",
                   "When the project is less than half finished"],
             "c": 1,
             "why": "Following Brooks's own analysis, the book says adding people does not help "
                    "where the tasks cannot be divided, but if they are partitionable they can be "
                    "split further and given to people added late. It names no exception for "
                    "capability or for how far the project has gone, and it explicitly allows "
                    "exceptions."},
            {"q": "Which of these is part of the approach to estimation Section 28.3 recommends?",
             "a": ["Use several estimation techniques and compare the results",
                   "Estimate the project as one large piece, so the errors cannot add up",
                   "Give the estimate at once, before the requirements are spelled out",
                   "Fix the first estimate and hold the project to it"],
             "c": 0,
             "why": "The section recommends several techniques, compared. It recommends the "
                    "opposite of the others: estimating at a low level of detail so that the "
                    "pieces' errors tend to cancel, spelling out the requirements first, and "
                    "re-estimating periodically as the project goes."},
        ],
        "mistakes": [
            ("Thinking an estimate is a number",
             "A single figure is what people ask for, and it is easy to give one. Section 28.3 "
             "asks for several approaches compared and an estimate tightened as the project "
             "goes, because the circumstances that set the effort are not known at the start. "
             "On the lesson's illustration two factors about the team alone move the same "
             "nominal 100 staff-months to 53.96 or to 190.28, from about half to nearly twice, "
             "before anything about the product is counted."),
            ("Thinking more people will bring a late project in earlier",
             "It looks like arithmetic: twice the people, half the time. Brooks's law, which the "
             "book cites from Brooks 1995, says the opposite: new people need time to learn the "
             "project, their teaching takes the time of those who know it, and every person "
             "added adds communication paths. The book qualifies it: where tasks can be "
             "divided and done independently, people added late can help. It is a question "
             "about the work, not a rule about headcount."),
            ("Thinking a rough measurement is worse than none",
             "Some figures are so imprecise that collecting them seems pointless. Section 28.4 "
             "argues that a measurement improves on not measuring, even when it is cloudy, and "
             "that the cloud clears as the measure is refined; its caution is that people "
             "attend to what is measured, so the choice of what to measure matters."),
        ],
        "standard": (
            "Finish when you can adjust a nominal estimate by stated factors.",
            "Given a nominal estimate and three of Table 28-1's percentages, turn each into a "
            "multiplier, multiply them, and give the adjusted effort exactly; then state the "
            "range the same factors span at their other ends."
        ),
        "note": (
            "The multipliers are Cocomo II's, as the book prints them, fitted by Boehm's team to "
            "other people's projects; the lab multiplies them as the model does, which assumes "
            "the factors act independently. It has no input for team size, so Brooks's law is "
            "argued in prose and not computed, and it cannot tell you which factors describe "
            "your project or by how much."
        ),
    },
    # ---------------------------------------------------------------- 03
    # McConnell Chapter 29, pp. 689-708: §29.1 p. 689 (the stadium, pp.
    # 689-690), §29.2 p. 691 (phased, pp. 691-692; incremental and its
    # benefits, pp. 692-694), §29.3 p. 694 (top-down pp. 694-696, bottom-up
    # p. 697, sandwich p. 698 after Myers 1976, risk-oriented p. 699,
    # feature-oriented p. 700, T-shaped p. 701, summary p. 702), §29.4 p. 702
    # (daily build and smoke test, pp. 702-706). Opening quotation: Key Points,
    # p. 708 (21 words); "big bang integration", p. 691 (3 words); "dump truck
    # full of stubs", p. 696 (5 words). Quotations in all: 29 words. No figure
    # from the book is used.
    {
        "slug": "integration-order",
        "title": "Integration Order",
        "module": "Chapter 29 · Integration",
        "one_line": "Integrating a system one piece at a time beats putting it all together at the end, and every incremental order pays for itself in stubs, drivers or both.",
        "summary": (
            "Chapter 29 argues for incremental integration over the phased kind, and surveys the "
            "orders it can take: top-down, bottom-up, sandwich, risk-oriented, feature-oriented "
            "and T-shaped. Walk three orders through one call graph and count the stubs and "
            "drivers each needs."
        ),
        "key": [
            "stub: called before it is integrated",
            "driver: no caller integrated yet",
            "phased: every piece at once",
            "incremental: one piece at a time",
            "build daily, smoke test daily",
        ],
        "key_label": "Chapter 29 in five lines",
        "concepts_intro": (
            "The chapter's one distinction, and the two kinds of scaffolding that the "
            "incremental side of it costs."
        ),
        "concepts": [
            ("Phased and incremental integration",
             "Phased integration develops every class on its own and then combines them all at "
             "once. Incremental integration starts from a small working skeleton and adds one "
             "tested piece at a time, testing the combination before the next."),
            ("A stub",
             "A stand-in for a routine that is not yet integrated, written so that a routine "
             "which calls it can be integrated and run. Top-down integration needs many of them."),
            ("A driver",
             "Test code that calls a routine in place of the real callers, which are not yet "
             "integrated. Bottom-up integration needs many of them."),
        ],
        "read_title": "The chapter's argument, then three orders through one call graph",
        "read_intro": (
            "The first half follows Chapter 29 through its four sections. The second walks three "
            "orders through one six-component call graph and counts the scaffolding each needs."
        ),
        "body": [
            ("p", "<strong>Chapter 29, Key Points, p. 708.</strong> &ldquo;Incremental "
                  "integration comes in several varieties, and, unless the project is trivial, "
                  "any one of them is better than phased integration.&rdquo; Read the chapter, "
                  "pages 689 to 708, in your own copy first; Section 29.3's figures show each "
                  "order better than words can."),
            ("p", "In what order should the pieces of a system be put together? Integration, "
                  "in the chapter's sense, is combining separately written components into one "
                  "system, and it cannot be separated from the order in which they are built, "
                  "since nothing can be integrated before it exists. McConnell's illustration is "
                  "from his own region: a stadium extension at the University of Washington "
                  "that collapsed partway through construction. It would probably have stood "
                  "when finished; it was built in an order in which it could not stand at each "
                  "step. Software built in the wrong order, he argues in Section 29.1 (p. 689), "
                  "is harder to code, test and debug in the same way, and can seem as if it will "
                  "never work because none of it works until all of it does."),
            ("p", "Section 29.2 (p. 691) sets out the choice. Phased integration develops and "
                  "tests every class alone, combines them all at once, and then tests the whole. "
                  "Its trouble is that every problem appears together and any class is a suspect, "
                  "which is why the book also calls it &ldquo;big bang integration&rdquo;. For a "
                  "program of two or three classes it may save time; for anything larger the book "
                  "prefers the incremental way: a small working skeleton, then one tested class "
                  "at a time, each combination tested before the next is added. When something "
                  "breaks, the new class or its connection to the rest is where to look; the "
                  "system works early; progress is visible as features rather than reported "
                  "percentages."),
            ("p", "Section 29.3 (p. 694) surveys the orders. Top-down integration starts with "
                  "the class at the top, the one that holds <code>main</code>, and replaces stubs "
                  "with real classes going down. It exercises the control logic and the design's "
                  "big decisions early and gives a visible system soon, but it leaves the tricky "
                  "low-level system interfaces until last and needs, in McConnell's phrase, a "
                  "&ldquo;dump truck full of stubs&rdquo;, which as test code are more likely "
                  "than production code to hold errors. Pure top-down, level by level, is in his view nearly "
                  "impossible; integrating in vertical slices is the workable form."),
            ("p", "Bottom-up integration reverses it: low-level classes first, exercised by test "
                  "drivers until their callers arrive. It reaches the system interfaces early and "
                  "the high-level design late, and it needs the whole design settled first. The "
                  "book then describes four blends: sandwich integration, top and bottom first "
                  "and the middle last, which it credits to Myers in 1976; risk-oriented, the "
                  "hardest parts first wherever they sit; feature-oriented, one feature's classes "
                  "at a time on a skeleton; and T-shaped, one deep slice end to end and then the "
                  "breadth. McConnell is frank that the names are being coined as people go: "
                  "the orders are heuristics rather than procedures, and the best one is an order "
                  "you make for your own project."),
            ("p", "Section 29.4 (p. 702) adds the practice that goes with any order: the daily "
                  "build and smoke test. Every file is compiled, linked and combined into a "
                  "program every day, and the program is put through a simple test of the whole "
                  "system to see whether it &ldquo;smokes&rdquo;. A broken build is fixed first; "
                  "the smoke test grows with the system; both are automated. If the product "
                  "worked yesterday and is broken today, something since yesterday broke it. The "
                  "section closes on continuous integration, which Programming Tools takes up."),
            ("h3", "Three orders through one call graph"),
            ("p", "The lab's call graph has six components: <code>main</code> calls "
                  "<code>ui</code> and <code>orders</code>; <code>ui</code> calls "
                  "<code>widgets</code>; <code>orders</code> calls <code>pricing</code> and "
                  "<code>db</code>; <code>pricing</code> calls <code>db</code>. Given an order, "
                  "it walks the components one at a time. Stubs needed lists every component "
                  "that some integrated component calls before it is itself integrated; Drivers "
                  "needed lists every component that has callers, none of them integrated when "
                  "it is. The <code>top-down</code> preset integrates <code>main</code>, "
                  "<code>ui</code>, <code>orders</code>, <code>widgets</code>, "
                  "<code>pricing</code>, <code>db</code>: everything below the top is called "
                  "before it arrives, so the stubs are 5: db, orders, pricing, ui, widgets, and "
                  "the drivers 0: none."),
            ("p", "The <code>bottom-up</code> preset runs the other way, <code>db</code> first "
                  "and <code>main</code> last: no stubs, and 5 drivers, the same five names, "
                  "because each arrives before any of its callers. The <code>risk-first</code> "
                  "preset starts with <code>pricing</code>, taken here to be the hard part, then "
                  "<code>db</code>, <code>orders</code>, <code>main</code>, <code>ui</code>, "
                  "<code>widgets</code>: 3 stubs (db, ui, widgets) and 2 drivers (orders, "
                  "pricing). On the lesson's illustration, putting the hardest part first costs "
                  "scaffolding of both kinds, which is the trade the chapter accepts. The lab "
                  "counts which components need scaffolding; it does not know how large each "
                  "stub is, or how risky each component, which is for you to judge."),
            ("h3", "Exercise"),
            ("code", INTEGRATION_EXERCISE.split("\n")),
            ("p", "Read the calls off the four classes, so that each call from one class to "
                  "another is a pair of caller and callee. Then integrate them in the order "
                  "<code>app</code>, <code>ui</code>, <code>core</code>, <code>store</code>, and "
                  "list the components that need a stub and those that need a driver. Work it by "
                  "hand; then type the pairs into the lab's Calls box and the order into its "
                  "Integration order box, in lower case, to check."),
            ("p", "The daily build is the first tool of integration; the next chapter surveys "
                  "the rest. The next lesson is &ldquo;Programming Tools&rdquo;."),
        ],
        "lab": ("cckit", {
            "mode": "deps",
            "view": "integrate",
            "preset": "top-down",
            "edges": CALL_EDGES,
            "presets": [
                {"id": "top-down",
                 "label": "Top down: main ui orders widgets pricing db",
                 "order": "main ui orders widgets pricing db",
                 "expect": {"dgStubs": "5: db, orders, pricing, ui, widgets", "dgDrivers": "0: none"}},
                {"id": "bottom-up",
                 "label": "Bottom up: db widgets pricing orders ui main",
                 "order": "db widgets pricing orders ui main",
                 "expect": {"dgStubs": "0: none", "dgDrivers": "5: db, orders, pricing, ui, widgets"}},
                {"id": "risk-first",
                 "label": "Hardest part first: pricing db orders main ui widgets",
                 "order": "pricing db orders main ui widgets",
                 "expect": {"dgStubs": "3: db, ui, widgets", "dgDrivers": "2: orders, pricing"}},
            ],
            "panel_title": "Stubs and drivers for an integration order",
            "panel_intro": (
                "Each record is a caller and the component it calls. The lab walks the order one "
                "component at a time: a component called before it is integrated needs a stub, "
                "and one integrated before any of its callers needs a driver."
            ),
        }),
        "steps_title": "Counting an order's scaffolding",
        "steps_intro": "Four steps, the last of which is your own feature's.",
        "steps": [
            ("Write the calls as pairs",
             "For every call from one component to another, write the caller and the callee. "
             "Two calls between the same pair are one pair."),
            ("Walk the order and mark stubs",
             "Take the components in order. When one is integrated, every component it calls "
             "that is not yet integrated needs a stub until it arrives."),
            ("Mark drivers",
             "When a component is integrated, check its callers. If it has callers and none of "
             "them is integrated yet, it needs a driver to exercise it."),
            ("Order one feature of your own",
             "Take one feature of a system you work on, write its components' calls as pairs, "
             "choose the order you would integrate them in, type both into the lab, and note "
             "the stubs and drivers it lists against the scaffolding you actually wrote."),
        ],
        "worked": {
            "title": "Top-down, step by step",
            "intro": [
                "Take the top-down preset: main, ui, orders, widgets, pricing, db.",
            ],
            "lines": [
                "main: calls ui and orders, not yet in, so 2 stubs",
                "ui: called by main, already in; calls widgets, a stub",
                "orders: calls pricing and db, both stubs",
                "widgets, pricing, db: each replaces its stub",
                "stubs: db, orders, pricing, ui, widgets; drivers: none",
            ],
            "after": [
                "Every component below the top is called before it arrives, so every one of them "
                "is a stub for a while, and no driver is ever needed: each component's caller is "
                "always there first.",
            ],
        },
        "quiz_title": "Orders, stubs and drivers",
        "quiz": [
            {"q": "In the exercise, app calls ui and core, ui calls core, and core calls store. "
                  "Integrated in the order app, ui, core, store, which components need a stub "
                  "and which a driver?",
             "a": ["Stubs: core, store, ui; no drivers",
                   "Stubs: core, store; no drivers",
                   "No stubs; drivers: core, store, ui",
                   "Stubs: store; drivers: core"],
             "c": 0,
             "why": "When app is integrated it calls ui and core, neither yet in: two stubs. When "
                    "core arrives it calls store, not yet in: a third. Each component's caller is "
                    "integrated before it, so no driver is needed: stubs core, store and ui, 3. "
                    "Leaving out ui forgets that app calls it before it arrives, even though it "
                    "arrives next; the drivers-only answer is the bottom-up order's pattern, not "
                    "this one's."},
            {"q": "In the lesson's call graph, orders and pricing both call db. Suppose db is "
                  "integrated first, before either of them. What does db need?",
             "a": ["A driver, since none of its callers is integrated yet",
                   "A stub, since it is called before it is integrated",
                   "Nothing, since db calls no other component",
                   "Both a stub and a driver"],
             "c": 0,
             "why": "A driver stands in for callers that are not there yet, and db has two "
                    "callers, neither integrated. A stub stands in for a callee: nothing "
                    "integrated calls db before it arrives, so it needs none. Calling nothing "
                    "spares db stubs of its own, not a driver."},
            {"q": "Which disadvantage does the book give for pure top-down integration?",
             "a": ["It tests the system's control logic late",
                   "It needs a test driver for every low-level class",
                   "It leaves the tricky low-level system interfaces until last",
                   "It cannot produce a visible, partly working system early"],
             "c": 2,
             "why": "Section 29.3 says pure top-down leaves exercising the tricky system "
                    "interfaces until last (p. 695). It names the control logic tested early and "
                    "a visible system early as top-down's advantages, and test drivers belong to "
                    "bottom-up integration."},
            {"q": "For what kind of program does Section 29.2 say phased integration might be "
                  "the best approach?",
             "a": ["A tiny program of two or three classes",
                   "A project of fifty or more people",
                   "A system whose interfaces are well documented",
                   "Any program built daily"],
             "c": 0,
             "why": "The book allows phased integration for tiny programs, two or three classes, "
                    "and then only if you are lucky (p. 692). It prefers incremental integration "
                    "for everything larger, and a daily build is itself a form of frequent, "
                    "incremental integration."},
        ],
        "mistakes": [
            ("Thinking integration is a phase at the end of construction",
             "If every class is written and tested first, putting them together looks like a "
             "last step. That is phased integration, and Section 29.2 argues against it: every "
             "problem surfaces at once, any class may be the culprit, and nothing works until "
             "everything does. The stubs and drivers the lab counts are the price of integrating "
             "incrementally, which is the trade the chapter accepts; on the lesson's "
             "illustration, the risk-first order pays 3 stubs and 2 drivers to do the hardest "
             "part first."),
            ("Thinking pure top-down is the safe, textbook order",
             "Starting from <code>main</code> and working down sounds orderly. The book calls "
             "pure top-down nearly impossible to carry out: it needs a great many stubs, which "
             "as test code are more error-prone than the code they stand in for, and it leaves "
             "the system interfaces at the bottom, often the riskiest part, until last. Vertical "
             "slices are the form of it the book recommends."),
            ("Thinking the best order is the one with the least scaffolding",
             "A count of stubs and drivers is easy to minimise and easy to mistake for the goal. "
             "The book's orders trade scaffolding against other things: risk-oriented "
             "integration accepts scaffolding to meet the hardest problems early, and the "
             "chapter says none of the orders is best in every case. A count is a reason to "
             "look at an order, not a ranking of it."),
        ],
        "standard": (
            "Finish when you can list an order's stubs and drivers from its calls.",
            "Given the calls among six components and an integration order, list without the "
            "lab every component that needs a stub and every one that needs a driver, and say "
            "for each why."
        ),
        "note": (
            "The lab knows only who calls whom and in what order the components arrive. It "
            "cannot weigh a stub's size, a component's risk or the cost of finding the design "
            "wrong late, which are what the chapter's orders trade against one another, and it "
            "treats each component as one unit where a real one may be integrated in pieces."
        ),
    },
    # ---------------------------------------------------------------- 04
    # McConnell Chapter 30, pp. 709-725: §30.1 p. 710, §30.2 p. 710 (editing,
    # pp. 710-713; code quality, pp. 713-714; refactoring, version control and
    # data dictionaries, pp. 714-715), §30.3 p. 716 (build tools, pp. 716-717,
    # the Word group's full rebuild, p. 717; libraries, generators,
    # preprocessors, debugging, testing and tuning, pp. 717-720), §30.4 p. 720,
    # §30.5 p. 721 (scripts, p. 722), §30.6 p. 722 (Fortran, p. 722; why
    # programming stays hard, p. 723). The modern aside cites §29.4's
    # continuous-integration passage, p. 706. Opening quotation: Key Points,
    # p. 725 (14 words); "too much of a good thing", p. 706 (6 words).
    # Quotations in all: 20 words. No figure from the book is used.
    {
        "slug": "programming-tools",
        "title": "Programming Tools",
        "module": "Chapter 30 · Programming Tools",
        "one_line": "Good tools take tedium out of construction, a build tool among them, which rebuilds whatever depends on a change; no tool removes the need to program.",
        "summary": (
            "Chapter 30 surveys the kinds of tool a programmer works with, from editors and "
            "analysers to build tools, debuggers and the tools you write yourself, and ends in "
            "tool fantasyland. Trace a change through a small build the way make does, and find "
            "every target it reaches."
        ),
        "key": [
            "a build redoes what depends on a change",
            "direct: one edge from the changed file",
            "affected: reached by any chain of edges",
            "a header reaches every file including it",
            "tools cut tedium; programming stays hard",
        ],
        "key_label": "Chapter 30 in five lines",
        "concepts_intro": (
            "The chapter is a survey; the lab takes one tool from it, the build tool, and the "
            "three terms below are what that tool works with."
        ),
        "concepts": [
            ("A target and its prerequisites",
             "A target is a file the build produces, an object file or a program. Its "
             "prerequisites are the files it is made from; when any of them changes, the target "
             "is out of date and must be made again."),
            ("Direct and transitive dependence",
             "A target depends directly on the files it lists. It depends transitively on "
             "everything those depend on, through any chain: a program depends on an object "
             "file, which depends on a header, so the program depends on the header."),
            ("A build tool",
             "A program such as make or ant that reads the targets and their prerequisites, "
             "finds which targets a change has put out of date, and rebuilds those and no others, "
             "so the sources end in a consistent state."),
        ],
        "read_title": "The chapter's survey, then one change traced through a build",
        "read_intro": (
            "The first half follows Chapter 30's survey in its order. The second traces two "
            "changes through a small build, as a build tool does."
        ),
        "body": [
            ("p", "<strong>Chapter 30, Key Points, p. 725.</strong> &ldquo;Programmers "
                  "sometimes overlook some of the most powerful tools for years before "
                  "discovering them.&rdquo; Read the chapter, pages 709 to 725, in your own copy "
                  "first; it is a survey, and its value is in noticing a kind of tool you have "
                  "been doing without."),
            ("p", "You edit one header, start the build, and watch it recompile files you never "
                  "touched. That is a build tool doing exactly what it was asked, and Chapter 30 "
                  "is about such tools: what kinds exist, what each takes off your hands, and "
                  "where the promise of tools runs out. McConnell writes about kinds of tool "
                  "rather than brands, because, as he says, products change faster than a book "
                  "can be printed, and he names a few, such as grep, make and lint, only because "
                  "they are so common."),
            ("p", "Sections 30.1 and 30.2 (p. 710) cover design tools and source-code tools. "
                  "The source-code tools are the richer set: an IDE with its compiler, search, "
                  "outlining, formatting and refactoring built in; search and replace across "
                  "many files, with regular expressions; diff and merge tools for comparing and "
                  "combining versions; beautifiers that standardise layout; tools that extract "
                  "interface documentation, of which Javadoc is the book's example; picky syntax "
                  "and semantics checkers, lint among them, that warn about code which compiles "
                  "and is probably not what you meant; metrics reporters; refactoring browsers; "
                  "version control; and, on large projects, a data dictionary of every "
                  "significant name."),
            ("p", "Section 30.3 (p. 716) turns to tools for executable code: compilers and "
                  "linkers, then build tools. A build tool's purpose, the book says, is to "
                  "rebuild a program in the least time from the current sources, and to bring "
                  "every file to a consistent state. For each target you state what it depends "
                  "on and how to make it; when a file changes, the tool rebuilds the targets "
                  "that depend on it and leaves the rest. The book names make and ant, and adds "
                  "a counterexample: one large team found that rebuilding everything, with the "
                  "sources tuned for it, beat checking dependencies at all. Then come libraries "
                  "and code generators, preprocessors, debuggers, testing tools and execution "
                  "profilers."),
            ("p", "Section 30.4 (p. 720) praises the Unix environment's small tools that work "
                  "together. Section 30.5 (p. 721) is about building your own. Given five hours "
                  "for a job, McConnell says, most good programmers would rather spend four hours "
                  "and forty-five minutes building a tool and let it do the job in fifteen. He "
                  "recommends planning time for project-specific tools, and a script for anything "
                  "longer than about five characters that you type more than a few times a day."),
            ("p", "Section 30.6 (p. 722), &ldquo;Tool Fantasyland&rdquo;, is the chapter's "
                  "history. Fortran, the formula translator, was conceived so that scientists and "
                  "engineers could type in their formulas and do without programmers. They did "
                  "write programs with it, and programmers were still needed. Third- and "
                  "fourth-generation languages, automatic programming, CASE tools and visual "
                  "programming each carried the same promise, and each, McConnell says, made "
                  "programming better without eliminating it, because what is left once the "
                  "accidental difficulties are gone is hard in itself: the messy world, the "
                  "dependencies and exceptions, the users who cannot make up their minds."),
            ("h3", "One change, traced through a build"),
            ("p", "The lab's build is a small C program's, because make is the book's example "
                  "and C has the header files that show the point; Java has no headers, and a "
                  "class that many others use plays their part. The program <code>app</code> is "
                  "linked from <code>main.o</code> and <code>util.o</code>; <code>main.o</code> "
                  "is compiled from <code>main.c</code> and <code>util.h</code>; "
                  "<code>util.o</code> from <code>util.c</code> and <code>util.h</code>. Depend on "
                  "it directly lists the targets with the changed file among their "
                  "prerequisites; Reached in all lists every target that some chain of "
                  "dependencies connects to it. The <code>header</code> preset changes <code>util.h</code>: "
                  "2: main.o, util.o directly, and 3: app, main.o, util.o in all, because the "
                  "program is linked from both."),
            ("p", "The <code>source</code> preset changes <code>main.c</code>: 1: main.o "
                  "directly, and 2: app, main.o in all; <code>util.o</code> is left alone. On the "
                  "lesson's illustration the header reaches every object file that includes it, "
                  "which is why changing one is expensive. The lab reads the dependencies you "
                  "type, not your files: a dependency missing from a makefile is missing from "
                  "the count, and that is how a build ends in the out-of-step state the book "
                  "warns about."),
            ("p", "The book's own position on how often to integrate is in Chapter 29 (p. 706). "
                  "It accepts continuous integration in the sense most writers then gave it, at "
                  "least daily, and calls the literal sense, integrating each change within hours, "
                  "&ldquo;too much of a good thing&rdquo; for most projects, because there is "
                  "value in letting code be out of step briefly during a larger change. Much "
                  "practice since has gone the other way: many teams merge small changes to a shared "
                  "mainline several times a day, and a server builds and tests every one; build "
                  "systems record exact dependencies and reuse every target a change does not "
                  "reach, the lab's computation done on every commit. Its advocates point to "
                  "problems found within minutes; the book's point about larger changes is "
                  "still the one they answer with short-lived branches and switches that hide "
                  "unfinished work. The book ties the choice to a project's size and kind, "
                  "and this lesson leaves it there."),
            ("h3", "Exercise"),
            ("code", MAKEFILE_EXERCISE.split("\n")),
            ("p", "These are the dependency lines of the lab's build, as a makefile states "
                  "them: each target, a colon, and its prerequisites. Suppose "
                  "<code>util.c</code> changes. List the targets that depend on it directly and "
                  "every target the build will remake. Work it from the three lines; then type "
                  "<code>util.c</code> into the lab's What changes box to check."),
            ("p", "This is the last chapter of the book's Part VI. The next course, Software "
                  "Craftsmanship, turns from the project to the programmer, and begins with "
                  "&ldquo;Layout and Style&rdquo;."),
        ],
        "lab": ("cckit", {
            "mode": "deps",
            "view": "ripple",
            "preset": "header",
            "edges": BUILD_EDGES,
            "presets": [
                {"id": "header",
                 "label": "util.h changes",
                 "changed": "util.h",
                 "expect": {"dgDirect": "2: main.o, util.o", "dgAffected": "3: app, main.o, util.o"}},
                {"id": "source",
                 "label": "main.c changes",
                 "changed": "main.c",
                 "expect": {"dgDirect": "1: main.o", "dgAffected": "2: app, main.o"}},
            ],
            "panel_title": "What a change rebuilds",
            "panel_intro": (
                "Each record is a target and one of its prerequisites, as a makefile lists them. "
                "The lab follows the records back from the changed file, as a build tool does, "
                "and lists the targets it reaches directly and in all."
            ),
        }),
        "steps_title": "Tracing a change through a build",
        "steps_intro": "Four steps, the last of which is your own build's.",
        "steps": [
            ("List targets and prerequisites",
             "For each target, write each file it is made from as a pair: the target, then the "
             "prerequisite."),
            ("Find the direct dependents",
             "Every target with the changed file among its prerequisites is out of date. Those "
             "are the direct ones."),
            ("Follow the chain upward",
             "Every target with an out-of-date target among its prerequisites is out of date "
             "too. Repeat until nothing new is added; the result is everything the build "
             "remakes."),
            ("Trace your own most-included file",
             "Take one build target of your own, write its prerequisites as records, type them "
             "into the lab with the file most others include as the change, and note how many "
             "targets it reaches against how many your build has."),
        ],
        "worked": {
            "title": "A change to util.h",
            "intro": [
                "Take the header preset: util.h changes in the lab's six-record build.",
            ],
            "lines": [
                "main.o lists util.h: out of date",
                "util.o lists util.h: out of date",
                "app lists main.o and util.o: out of date",
                "direct: main.o, util.o; in all: app, main.o, util.o",
            ],
            "after": [
                "Three targets are remade for one edited file, and the edit touched no source "
                "file of either object. That is not the build tool being wasteful: both object "
                "files were compiled with the header in them, and both may now be wrong.",
            ],
        },
        "quiz_title": "Builds and the tools around them",
        "quiz": [
            {"q": "In the exercise's makefile, util.c changes. Which targets does the build "
                  "remake?",
             "a": ["util.o only", "util.o and app", "app, main.o and util.o",
                   "util.c and util.o"],
             "c": 1,
             "why": "util.o lists util.c, so it is out of date; app lists util.o, so it is too: "
                    "2 targets, util.o directly and app through it. util.o alone stops at the "
                    "direct dependent; main.o does not list util.c, so it is not remade; and "
                    "util.c is the source you edited, not a target."},
            {"q": "Add a fourth line to the lesson's build, a test program linked from util.o "
                  "and test.o. Which targets does a change to util.h now reach in all?",
             "a": ["main.o and util.o", "app, main.o and util.o",
                   "app, main.o, test and util.o", "app, main.o, test, test.o and util.o"],
             "c": 2,
             "why": "util.h is a prerequisite of main.o and util.o directly; app is linked from "
                    "both, and test from util.o, so 4 targets in all. test.o is not reached: "
                    "nothing says it is made from util.h, so a change to the header leaves it "
                    "alone unless the makefile says otherwise."},
            {"q": "In Section 30.6's history, which tool was the first said to make "
                  "programmers unnecessary?",
             "a": ["Fortran", "CASE tools", "Fourth-generation languages",
                   "Visual programming"],
             "c": 0,
             "why": "The book names Fortran first, conceived so that scientists and engineers "
                    "could type in formulas without programmers (p. 722). CASE tools, "
                    "fourth-generation languages and visual programming come later in its list "
                    "of tools that carried the same promise."},
            {"q": "By Section 30.5's rule of thumb, which of these is a candidate for a script?",
             "a": ["A five-hour job done once",
                   "A command longer than about five characters typed several times a day",
                   "Any command typed more than once a week",
                   "Only a job that takes longer than writing the script"],
             "c": 1,
             "why": "The book suggests scripting anything longer than about five characters that "
                    "you type more than a few times a day, such as compile and link sequences "
                    "and backup commands (p. 722). Its five-hour example is about building a "
                    "tool for a job, not a script, and it states no weekly rule or "
                    "break-even condition."},
        ],
        "mistakes": [
            ("Thinking a build tool rebuilds what you edited",
             "You edited one file, so it seems one thing should be rebuilt. A build tool "
             "rebuilds what depends on the change, transitively: every target that lists the "
             "file, and every target that lists one of those. On the lesson's illustration a "
             "change to util.h, which no one compiles on its own, remakes main.o, util.o and "
             "app, because the header reaches every object file that includes it."),
            ("Expecting a tool to eliminate the need for programming",
             "Every generation of tools has been sold this way, from Fortran onwards. Section "
             "30.6 argues that each removed some accidental difficulty and none removed the "
             "essential one: someone still has to think rigorously about sequences, "
             "dependencies and exceptions and connect the computer to a messy world. McConnell's "
             "advice when a vendor promises otherwise is to run, or at least to smile."),
            ("Thinking that writing your own tools is time taken from the real work",
             "A tool you write is not the product, so it can look like a detour. Section 30.5 "
             "treats it as part of the work: most large organisations have tool groups, most "
             "medium and large projects need tools of their own for test data, data checking or "
             "missing hardware, and a short script removes a repeated chance of typing a long "
             "command wrong."),
        ],
        "standard": (
            "Finish when you can say what a change to one file rebuilds.",
            "Given a make-style list of targets and their prerequisites and one changed file, "
            "list without the lab the targets that depend on it directly and every target the "
            "build remakes, and explain each by the chain that reaches it."
        ),
        "note": (
            "The lab follows the dependencies you type; it does not read files, so it cannot "
            "find a dependency the list leaves out, which is the commonest way a real build goes "
            "wrong. It treats every listed change as making its dependents out of date, where "
            "real tools compare timestamps or contents and may skip a target whose inputs did "
            "not really change. Of the chapter's survey it computes one tool; the rest is the "
            "chapter's to show."
        ),
    },
]
