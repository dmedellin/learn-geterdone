"""Code Improvements, lessons 1-4 -- Chapters 20-22 of Code Complete, 2nd ed.

The quality landscape, collaborative construction, and developer testing in
two halves (structured basis testing; boundaries, bad data and the rest of the
chapter). Pages are the second edition's printed pages. Every quotation is
copied from the book character for character, with its page in the comment
beside the lesson; every figure attributed to the book carries its register id
from docs/code-complete/PLAN.md section S.2. The code is written for these
lessons; none of it is the book's.
"""

# ---------------------------------------------------------------- snippets
# One constant per snippet: the lesson's code block and the lab's preset both
# use it, so the line numbers the prose names are the lab's (PLAN D.4).

# PLAN D.4 `overtime` (presets.py `basis`). Also the exercise of Debugging as
# Science (part_b).
OVERTIME = """double overtimePay(Employee[] staff, int count) {
    double pay = 0.0;
    int i = 0;
    while (i < count && staff[i] != null) {
        Employee e = staff[i];
        if (e.isExempt()) {
            // exempt staff earn no overtime
        } else if (e.hours() > 40) {
            pay = pay + (e.hours() - 40) * e.rate() * 1.5;
        }
        i = i + 1;
    }
    return pay;
}"""

# PLAN D.4 `switch-without-default` (presets.py `basis-switch`).
SHIPPING_LABEL = """String shippingLabel(int zone, boolean express) {
    String label = "";
    switch (zone) {
        case 1:
            label = "local";
            break;
        case 2:
            label = "regional";
            break;
        case 3:
            label = "national";
            break;
    }
    if (express) {
        label = label + " express";
    }
    return label;
}"""

# PLAN D.4 exercise `archiveOld` (presets.py `archive-old`): 4 basis cases.
ARCHIVE_OLD = """void archiveOld(Message[] inbox, int days) {
    for (int i = 0; i < inbox.length; i++) {
        if (inbox[i].ageInDays() > days || inbox[i].isSpam()) {
            inbox[i].archive();
        }
    }
}"""

# PLAN D.4 exercise `countPassing` (presets.py `count-passing`): three planted
# defects, lines 3, 5 and 2.
COUNT_PASSING = """// Returns how many scores are at or above the pass mark.
int countPassing(int[] scores, int passMark, int maxScore) {
    int count = 1;
    for (int i = 0; i < scores.length; i++) {
        if (scores[i] > passMark) {
            count = count + 1;
        }
    }
    return count;
}"""

# Boundaries and Bad Data, exercise (PLAN C 5.4): the check `len > 8 && len
# <= 64` against a range of 8 to 64, put in a routine for the lesson. Not a
# lab preset; its answer is the lab's `range` view on lo 8, hi 64.
VALID_LENGTH = """// A password must be 8 to 64 characters long.
boolean validLength(String password) {
    int len = password.length();
    return len > 8 && len <= 64;
}"""


def _lines(snippet):
    return snippet.split("\n")


LESSONS = [
    # ---------------------------------------------------------------- 01
    # McConnell Chapter 20, pp. 463-477. Quote: p. 477 (Key Points), 19 words.
    # External and internal characteristics, pp. 463-465; Figure 20-1, p. 466;
    # techniques, pp. 466-468; Weinberg and Schulman 1974, pp. 468-469;
    # Table 20-2, p. 470 (F16); modal rates, the 85 and 95 percent figures,
    # Myers 1978b, Jones's under-60-percent, Table 20-3, pp. 470-472 (F17);
    # cost of finding, p. 472; when, p. 473; the General Principle, p. 474.
    {
        "slug": "the-software-quality-landscape",
        "title": "The Software-Quality Landscape",
        "module": "Chapter 20 · The Software-Quality Landscape",
        "one_line": "No single way of finding defects finds most of them, so the share a project removes depends on which unlike techniques it combines.",
        "summary": (
            "Chapter 20 surveys what software quality is, the techniques that improve it, and "
            "how effective each is at finding defects. Its table of detection rates, after "
            "Capers Jones, puts no single technique's typical rate above 75 percent. Compute "
            "what a sequence of stages leaves behind from each stage's rate, and say what the "
            "product assumes."
        ),
        "key": [
            "no single technique is enough",
            "a stage finds its rate of what reaches it",
            "left: start × every miss rate",
            "unit test 30, code inspection 60",
            "the product assumes independent misses",
            "improving quality reduces cost",
        ],
        "key_label": "The chapter in six lines",
        "concepts_intro": (
            "The chapter is a survey, and the lesson takes three things from it: a rate for "
            "each technique, the arithmetic of combining them, and the principle the chapter "
            "ends on."
        ),
        "concepts": [
            ("Defect-detection rate",
             "The share of the defects present at a stage that the stage finds. The book's "
             "Table 20-2, after Jones and others, gives each technique a lowest, a modal and "
             "a highest rate; the modal rate is the one seen most often."),
            ("Combined removal",
             "The share of the original defects that a sequence of stages finds between them. "
             "If each stage finds its rate of whatever reaches it, the defects left are the "
             "starting number times each stage's miss rate."),
            ("The General Principle of Software Quality",
             "McConnell's name for the claim that improving quality reduces development cost, "
             "because the largest single activity on most projects is finding and reworking "
             "what went wrong."),
        ],
        "read_title": "The chapter's survey, section by section, then the arithmetic",
        "read_intro": (
            "The lesson follows the chapter's five sections in order and then does the one "
            "calculation the chapter itself does with its table: multiplying the misses."
        ),
        "body": [
            ("p", "<strong>Code Complete, Chapter 20, p. 477.</strong> &ldquo;No single "
                  "defect-detection technique is completely effective by itself. Testing by "
                  "itself is not optimally effective at removing errors.&rdquo; That is the "
                  "chapter's own summary, from its Key Points. Read Chapter 20, pages 463 to "
                  "477, in your own copy first; it is short, and this lesson goes back through "
                  "it a section at a time."),
            ("p", "The chapter asks what quality is before it asks how to get it. Section 20.1 "
                  "(p. 463) separates the characteristics a user meets, such as correctness, "
                  "usability, efficiency, reliability and robustness, from the ones only a "
                  "programmer meets: maintainability, readability, testability and the rest. "
                  "Users care only about the first kind, McConnell says, but the second kind "
                  "reaches them in the end, because code you cannot understand is code whose "
                  "defects you cannot fix. And the characteristics pull against each other: his "
                  "Figure 20-1 shows, for instance, that working on correctness, doing exactly "
                  "what the specification says, works against robustness, carrying on when "
                  "the input is not what was specified."),
            ("p", "Section 20.2 (p. 466) lists the techniques: explicit quality objectives, an "
                  "explicit assurance activity, a testing strategy, guidelines, informal and "
                  "formal reviews, external audits, and in the development process change "
                  "control, measurement and prototyping. The case for setting objectives is a "
                  "story. In 1974 Gerald Weinberg and Edward Schulman gave several teams the same "
                  "program and told each to optimise something different: memory, readable "
                  "output, readable code, the least code, the least programming time. Nearly "
                  "every team came first on the objective it had been given, and none did well "
                  "on all of them. Programmers do what they are asked, the chapter concludes, "
                  "and the objectives conflict, so someone has to choose."),
            # F16, p. 470; F17, pp. 470-471.
            ("p", "Section 20.3 (p. 469) is the heart of the chapter. Its Table 20-2, which the "
                  "book adapts from Capers Jones (1986 and 1996) and from Shull and others "
                  "(2002), gives each defect-detection technique a lowest, a modal and a highest "
                  "rate. A few of the modal rates: unit testing 30 percent, integration testing "
                  "35, system testing 40, formal design inspections 55, formal code inspections "
                  "60. McConnell's reading of the table is that no technique's modal rate is "
                  "above 75 percent and that they average about 40; that the typical "
                  "test-heavy organisation removes about 85 percent of its defects; and that "
                  "leading organisations, using a wider variety of techniques, reach 95 percent "
                  "or more (Jones 2000). These are averages over many organisations' projects, "
                  "mostly before 2004, gathered by other people. Your own defect records are "
                  "what would test them, and nothing in this lesson can."),
            # F17, p. 471 (Jones's under-60-percent); Myers 1978b, pp. 470-471.
            ("p", "So the chapter argues for combining techniques, and for combining unlike "
                  "ones. It cites a study by Glenford Myers (1978) in which experienced "
                  "programmers looked for the known errors in one program by different methods: "
                  "no method had a significant advantage on its own, but any two together, even "
                  "two independent groups using the same method, found far more than one, "
                  "because different people find different defects. Jones reports that unit, "
                  "functional and system testing together often remove less than 60 percent, "
                  "which the book calls usually inadequate for production software. The "
                  "section then turns to what finding and fixing a defect costs, which the next "
                  "lesson takes up."),
            ("p", "Section 20.4 (p. 473) says when: early, and throughout, because a defect "
                  "made in requirements or architecture spreads into design, code and tests "
                  "before anyone finds it. Section 20.5 (p. 474) closes with what McConnell "
                  "calls the General Principle of Software Quality: improving quality reduces "
                  "development costs. His reason is that the largest single activity on most "
                  "projects is debugging and reworking code that does not work, so preventing "
                  "a defect is cheaper than finding it later. Quality, the Key Points put it, is "
                  "free in the end, but only after resources are moved upstream."),
            ("def", ("A sequence of removal stages",
                     "Defects pass through stages in order: an inspection, then unit test, "
                     "then system test. Each stage finds its rate of the defects that reach "
                     "it, and the rest go on. After the last stage, the defects left are the "
                     "starting number times each stage's miss rate, one minus its rate.")),
            # F16, p. 470 (modal rates); presets are the lesson's illustration.
            ("p", "That is the lab's arithmetic, and it is the arithmetic the book itself does "
                  "in Table 20-3 (p. 472), where it multiplies the rates of Extreme "
                  "Programming's practices to estimate what they remove. The "
                  "<code>testing-only</code> preset sends 1,000 defects through unit, "
                  "integration and system testing at the table's modal rates, 30, 35 and 40 "
                  "percent. Unit testing finds 300 and passes on 700; integration testing finds "
                  "35 percent of those and passes on 455; system testing finds 40 percent of "
                  "those and passes on 273. The lab prints Found 727, Remaining 273 and Combined "
                  "removal 727/1000 = 72.7%: the share of the original defects found by some "
                  "stage. The <code>one-stage</code> preset, unit testing alone, finds 300, "
                  "leaves 700 and removes 30%."),
            ("p", "The <code>inspections-too</code> preset puts a formal design inspection at 55 "
                  "percent and a formal code inspection at 60 percent in front of the same three "
                  "tests. Remaining falls to 2457/50 = 49.14 and Combined removal rises to "
                  "47543/50000, about 95.1%, the level the chapter reports for leading "
                  "organisations. A fraction of a defect is the model's expected value, not a "
                  "defect anyone could point to. On the lesson's illustration, three test stages "
                  "at their modal rates still leave more than a quarter of the defects behind, "
                  "and only stages of another kind bring the remainder below fifty."),
            ("p", "Read the product for what it assumes. It treats each stage's misses as "
                  "independent of the stages before it, as if every defect that survived unit "
                  "testing were as easy for integration testing to find as any other. Two "
                  "stages that miss the same kinds of defect break that assumption, and the "
                  "product cannot tell them from two that miss different kinds: three test "
                  "stages multiply exactly as three unlike stages would. That unlike "
                  "techniques find different defects is the chapter's claim from Jones's and "
                  "Myers's data, not something the multiplication shows. And since Jones "
                  "reports that testing combinations like this one often remove less than 60 "
                  "percent, the 72.7 is an upper bound on the illustration, not a forecast."),
            ("h3", "Exercise"),
            ("math", [
                "defects at the start:  1000",
                "pipeline A:  two stages, 40 percent then 50 percent",
                "pipeline B:  three stages, 30 percent each",
            ]),
            ("p", "For each pipeline, compute by hand the defects left and the combined removal, "
                  "and say which of the two removes more. Then type each pipeline into the lab's "
                  "stages box, with any stage names, to check your figures."),
            ("p", "The rates in Table 20-2 are what a technique finds. What it costs to find "
                  "them, and why reviews find different defects from tests, is the subject of "
                  "the next lesson, “Collaborative Construction”."),
        ],
        "lab": ("cckit", {
            "mode": "defects",
            "view": "removal",
            "injected": 1000,
            "preset": "testing-only",
            "presets": [
                {"id": "testing-only",
                 "label": "Testing only: unit 30, integration 35, system 40 percent",
                 "stages": "unit test, 3/10; integration test, 35/100; system test, 40/100",
                 "expect": {"dfFound": "727", "dfRemaining": "273",
                            "dfCombined": "727/1000 = 72.7%"}},
                {"id": "inspections-too",
                 "label": "Design and code inspections, then the three tests",
                 "stages": ("design inspection, 55/100; code inspection, 60/100; unit test, 3/10; "
                            "integration test, 35/100; system test, 40/100"),
                 "expect": {"dfRemaining": "2457/50 = 49.14",
                            "dfCombined": "47543/50000 ≈ 95.1%"}},
                {"id": "one-stage",
                 "label": "Unit testing alone",
                 "stages": "unit test, 3/10",
                 "expect": {"dfFound": "300", "dfRemaining": "700", "dfCombined": "3/10 = 30%"}},
            ],
            "panel_title": "What a sequence of stages leaves behind",
            "panel_intro": (
                "Each stage finds its rate of the defects that reach it, and the rest go on to "
                "the next. Rates are typed as fractions or decimals. The product assumes each "
                "stage's misses are independent of the stages before it. Figures: modal rates "
                "from the book's Table 20-2, after Jones and Shull et al."
            ),
        }),
        "steps_title": "Combining removal stages",
        "steps_intro": "Four steps of arithmetic and one of your own.",
        "steps": [
            ("Write each stage's miss rate",
             "A stage that finds 30 percent of what reaches it misses 70 percent. Write the "
             "miss rate, one minus the rate, for every stage in order."),
            ("Multiply the misses",
             "The defects left after the last stage are the starting number times every miss "
             "rate. The order of the stages does not change the product."),
            ("Subtract for what was found",
             "Found is the starting number minus what is left, and the combined removal is "
             "found over the starting number."),
            ("Say what the product assumes",
             "Write one sentence saying the stages are taken to miss independently, so the "
             "figure is an upper bound when two stages find the same kinds of defect."),
            ("Put your own team's stages in",
             "List the stages your team actually runs, give each the book's modal rate from "
             "Table 20-2, type them into the lab and note the combined removal. Then write one "
             "sentence saying the rates are averages from other people's projects, and name "
             "the record of your own that would test them."),
        ],
        "worked": {
            "title": "Three test stages on 1,000 defects",
            "intro": [
                "Take the <code>testing-only</code> preset: 1,000 defects, then unit testing "
                "at 30 percent, integration testing at 35 and system testing at 40, the modal "
                "rates of the book's Table 20-2.",
            ],
            "lines": [
                "after unit test:  1000 × 0.70 gives 700",
                "after integration test:  700 × 0.65 gives 455",
                "after system test:  455 × 0.60 gives 273",
                "found:  1000 - 273 gives 727",
                "combined removal:  727 of 1000, 72.7 percent",
            ],
            "after": [
                "More than a quarter of the defects are still there after three rounds of "
                "testing, and that is on the assumption that each stage misses independently. "
                "Adding a design and a code inspection in front, the <code>inspections-too</code> "
                "preset, leaves about 49.",
            ],
        },
        "quiz_title": "Rates and their product",
        "quiz": [
            {"q": "Pipeline A has two stages at 40 percent and 50 percent; pipeline B has three "
                  "stages at 30 percent each. What combined removal does the product give for "
                  "each?",
             "a": ["A 70%, B 65.7%", "A 90%, B 90%", "A 20%, B 2.7%", "A 70%, B 90%"],
             "c": 0,
             "why": "Multiply the misses. A leaves 0.6 × 0.5 = 0.30 of the defects, so it "
                    "removes 70%: 300 of 1,000 are left. B leaves 0.7 × 0.7 × 0.7 = 0.343, so "
                    "it removes 65.7%: 343 are left. A, with fewer stages, removes more. Adding "
                    "the rates gives 90% for both, counting twice every defect two stages "
                    "would both find; multiplying the rates instead of the misses gives the "
                    "share every stage would find, 20% and 2.7%."},
            # F17, p. 470.
            {"q": "What does McConnell read from the modal rates of Table 20-2 (after Jones and "
                  "others)?",
             "a": ["No technique's modal rate is above 75%, and they average about 40%",
                   "Unit testing has the highest modal rate, at 75%",
                   "Formal code inspections reach 95% on their own",
                   "Every technique's modal rate is above 60%"],
             "c": 0,
             "why": "Section 20.3, p. 470: the modal rates do not rise above 75 percent for "
                    "any single technique and average about 40 (the book's reading of Jones "
                    "and others). Unit testing's modal rate is 30 percent and formal code "
                    "inspection's 60; 95 percent is what Jones reports for leading "
                    "organisations combining several techniques."},
            {"q": "Add a design inspection at 55% and a code inspection at 60% in front of "
                  "unit, integration and system testing at 30%, 35% and 40%. How many of 1,000 "
                  "defects does the product leave?",
             "a": ["About 49", "180", "273", "450"],
             "c": 0,
             "why": "1,000 × 0.45 × 0.40 = 180 reach the tests, and 180 × 0.70 × 0.65 × 0.60 "
                    "= 49.14 are left: the <code>inspections-too</code> preset. 180 stops "
                    "after the inspections, 273 is the three tests without them, and 450 is "
                    "the design inspection alone."},
            {"q": "The lab leaves 273 of 1,000 defects after the three test stages. Which "
                  "assumption does that figure rest on?",
             "a": ["Each stage finds its rate of whatever reaches it, independently of what "
                   "earlier stages missed",
                   "The three stages find different kinds of defect from one another",
                   "The rates were measured on your own project",
                   "Every defect is found by at least one stage"],
             "c": 0,
             "why": "The product treats each stage's misses as independent. That the stages "
                    "find different kinds of defect is the chapter's claim, which the product "
                    "cannot show: like stages multiply exactly as unlike ones do. The rates "
                    "are the book's averages, not yours, and 273 defects are found by no stage "
                    "at all."},
        ],
        "mistakes": [
            ("Thinking testing is how you get quality",
             "Many teams rely on testing as both the measure and the source of quality, and "
             "the chapter argues it cannot carry that weight. No single technique's modal rate "
             "in the book's table is above 75 percent, they average about 40, and Jones "
             "reports that unit, functional and system testing together often remove less "
             "than 60 percent. On the lesson's illustration, even three test stages at their "
             "modal rates leave 273 of 1,000 defects, more than a quarter; the level the "
             "chapter reports for leading organisations comes only from combining unlike "
             "techniques, such as inspections, with the tests."),
            ("Adding the rates",
             "Unit testing at 30 percent, integration at 35 and system at 40 do not remove 105 "
             "percent of the defects, nor 100. Each stage works on what the stages before it "
             "left, so the misses multiply: 0.70 × 0.65 × 0.60 leaves 273 of 1,000."),
            ("Reading the book's rates as your project's",
             "The rates in Table 20-2 are averages over many organisations' projects, gathered "
             "by Jones and others mostly before 2004, with wide ranges either side of the "
             "modal figure. They say where to look, not what your stages remove. Your own "
             "records of defects found at each stage, and found later, are what would test "
             "them."),
        ],
        "standard": (
            "Finish when you can compute what a sequence of stages leaves and say what the "
            "product assumes.",
            "For three stages with stated rates and 1,000 defects, compute the defects found, "
            "the defects remaining and the combined removal by hand, and state in one sentence "
            "the independence assumption the product makes."
        ),
        "note": (
            "The lab multiplies the misses, so it assumes each stage misses independently of "
            "the stages before it. It therefore gives the same answer for two like stages as "
            "for two unlike ones; that unlike techniques find different defects is the "
            "chapter's claim from Jones's and Myers's data, which a product cannot test. The "
            "book also reports, after Jones, that real combinations of testing alone often "
            "remove less than 60 percent, so the lab's 72.7 percent for three tests is an "
            "upper bound on the illustration, not a forecast."
        ),
    },
    # ---------------------------------------------------------------- 02
    # McConnell Chapter 21, pp. 479-497. Quote: p. 497 (Key Points), 30 words.
    # Overview, blind spots, different kinds of errors, pp. 480-481; pair
    # programming, pp. 483-484; Fagan and the inspection's features, p. 485;
    # roles, pp. 486-487; stages, pp. 487-489; egos and the second edition's
    # inspections, pp. 490-491; walk-throughs, code reading, dog-and-pony shows,
    # pp. 492-495; summary of pairs against inspections, pp. 496-497.
    # Hours per defect: F18, pp. 472-473 (Kaplan 1995; Moore 1992).
    {
        "slug": "collaborative-construction",
        "title": "Collaborative Construction",
        "module": "Chapter 21 · Collaborative Construction",
        "one_line": "Other people find defects you are blind to, and the book reports that an inspection finds a defect in a fraction of the hours a test takes.",
        "summary": (
            "Chapter 21 covers pair programming, formal inspections, walk-throughs and code "
            "reading, and argues that reviews find different kinds of errors from testing. "
            "Read a short routine as an inspector would and list what to raise, then compute "
            "the defects found, the defects left and the hours spent by a pipeline that puts "
            "an inspection in front of the tests."
        ),
        "key": [
            "you are blind to some of your own defects",
            "inspect for defects, not for fixes",
            "IBM: 3.5 hours by inspection, 15–25 testing",
            "hours per defect: hours over defects found",
            "reviews and tests find different errors",
        ],
        "key_label": "The chapter in five lines",
        "concepts_intro": (
            "The chapter rests on one observation about programmers and builds three "
            "practices on it; the lesson keeps the observation, the inspection, and a way to "
            "compare costs."
        ),
        "concepts": [
            ("Blind spots",
             "Every collaborative technique, the chapter says, rests on the same idea: "
             "developers are blind to some of the trouble spots in their own work, other "
             "people do not share those blind spots, and so it pays to have someone else "
             "look."),
            ("Formal inspection",
             "A review with checklists, distinct roles, preparation before the meeting and "
             "data collected afterwards, aimed only at finding defects. Michael Fagan "
             "developed it at IBM and published it in 1976."),
            ("Hours per defect found",
             "What a stage costs divided by what it finds. The book reports figures from IBM "
             "and Microsoft that put inspection's hours per defect at a fraction of "
             "testing's, and the lab compares pipelines on that measure."),
        ],
        "read_title": "The chapter's practices in order, then the cost of finding a defect",
        "read_intro": (
            "The lesson goes through the four sections in the book's order and then takes up "
            "the figures on cost that Chapter 20 left for this one."
        ),
        "body": [
            ("p", "<strong>Code Complete, Chapter 21, p. 497.</strong> &ldquo;Collaborative "
                  "development practices tend to find different kinds of errors than testing "
                  "does, implying that you need to use both reviews and testing to ensure the "
                  "quality of your software.&rdquo; Read Chapter 21, pages 479 to 497, in your "
                  "own copy first; the lesson goes through it section by section."),
            # F16, p. 470 (the same modal rates, which p. 480 gives after Jones 1996).
            ("p", "Why should anyone else read your code? Section 21.1 (p. 480) answers that "
                  "every collaborative technique rests on one idea: you are blind to some of "
                  "the trouble spots in your own work, and other people are blind to different "
                  "ones. It sets the average rates of testing against those of inspection, "
                  "after Jones: about 30 percent for unit testing and 35 for integration "
                  "testing, against 55 and 60 for design and code inspections. It cites studies "
                  "(Myers 1978; Basili, Selby and Hutchens 1986) finding that reviews and tests "
                  "find different kinds of error, and adds two benefits besides: reviews pass "
                  "on a team's knowledge from its experienced programmers to its new ones, and "
                  "people who know their work will be read scrutinise it more carefully."),
            ("p", "Section 21.2 (p. 483) is pair programming: one programmer types, the other "
                  "watches for mistakes and thinks about whether the right code is being "
                  "written. The chapter's advice includes supporting pairs with a coding "
                  "standard, so that they do not spend the time arguing about style, not "
                  "letting the second programmer become a spectator, and rotating the pairs. "
                  "Its summary is that pairing costs about the same as inspection and produces "
                  "code of similar quality, and that the choice between them can come down to "
                  "how a team prefers to work."),
            ("p", "Section 21.3 (p. 485) is the formal inspection, developed by Michael Fagan "
                  "at IBM and used there for several years before his 1976 paper made it "
                  "public. What makes it formal is a list: checklists that point reviewers at "
                  "past trouble, a focus on finding defects rather than fixing them, "
                  "preparation before the meeting, distinct roles, a moderator who is not the "
                  "author, and data kept from each inspection to improve the next. The roles "
                  "are moderator, author, reviewers and scribe; management stays away, and the "
                  "results are never used to appraise anyone. The stages run from planning and "
                  "an optional overview through preparation, which each reviewer does alone, "
                  "to a meeting where someone other than the author "
                  "reads or paraphrases the code, at a pace kept neither too fast nor too slow. Then come the report, the rework and the "
                  "follow-up, with an informal third-hour meeting afterwards for anyone who "
                  "wants to talk about fixes."),
            ("p", "McConnell tells how inspections changed his own book. The first edition had "
                  "been reread by him, reviewed by peers, edited, proofread, and corrected "
                  "from readers' reports through its years in print. For the second edition "
                  "he had small teams of reviewers inspect it formally, as the chapter "
                  "describes, and to his surprise they found errors that every one of those "
                  "earlier reviews had missed. Section 21.4 (p. 492) "
                  "then covers the looser kinds. A walk-through is loosely defined, usually "
                  "led by the author, and in Jones's data finds fewer defects than an "
                  "inspection; McConnell's view is that a review worth a meeting is worth "
                  "running as an inspection. Code reading puts the effort into each reviewer's "
                  "own reading rather than a meeting. A dog-and-pony show is a demonstration "
                  "to a customer, a management review rather than a technical one."),
            # F18, pp. 472-473.
            ("p", "Chapter 20 left the cost of finding defects for this lesson. The book reports "
                  "two companies' figures from the 1990s. At IBM, it took 3.5 staff-hours to "
                  "find each error by code inspection against 15 to 25 by testing (Kaplan "
                  "1995, as the book cites him). At Microsoft's applications division, it took "
                  "about 3 hours to find and fix a defect by inspection against 12 by testing "
                  "(Moore 1992). The book's explanation is that an inspection is a one-step "
                  "technique, finding a defect and its cause together, while a test finds a "
                  "symptom and leaves the cause to be debugged. These are two organisations' "
                  "averages, measured on their projects and not yours."),
            ("def", ("Hours per defect found",
                     "The hours a stage costs divided by the defects it finds. In the lab each "
                     "stage is given its rate and its hours per defect found, so a stage's "
                     "hours are the defects it finds times that figure.")),
            ("p", "The lab's pipeline adds hours to the previous lesson's product. The "
                  "<code>test-only</code> preset sends 100 defects through unit testing at "
                  "30 percent and system testing at 40, each at 20 hours per defect found, a "
                  "figure the lesson chose inside the IBM range of 15 to 25. Unit testing finds "
                  "30 and system testing 28 of the 70 left: the lab prints Found 58, Remaining "
                  "42, Hours spent 1,160 and Hours per defect found 20."),
            ("p", "The <code>inspect-first</code> preset puts a code inspection at 60 percent and "
                  "3.5 hours in front of the same tests. It finds 60 defects in 210 hours; unit "
                  "testing finds 12 of the 40 left in 240; system testing finds 11.2 of the 28 "
                  "in 224. The lab prints Found 416/5 = 83.20, Remaining 84/5 = 16.80, Combined "
                  "removal 104/125 = 83.2%, Hours spent 674 and Hours per defect found 1685/208 "
                  "≈ 8.10. The <code>three-and-twelve</code> preset uses Microsoft's pair, 3 "
                  "hours by inspection and 12 by testing: the same 83.20 found and 16.80 left, "
                  "since the rates have not changed, for 2292/5 = 458.40 hours and 573/104 ≈ "
                  "5.51 per defect. On the lesson's illustration, the pipeline with the "
                  "inspection finds more and spends fewer hours; the note says what the model "
                  "assumes to get there."),
            ("h3", "Exercise"),
            ("code", _lines(COUNT_PASSING)),
            ("p", "Read <code>countPassing</code> as a reviewer preparing for an inspection would: "
                  "alone, line by line, against what its comment promises. List every defect "
                  "you would raise, with its line number, and for each name the kind of "
                  "checklist question that would have pointed you at it. The lab cannot do "
                  "this one for you; reading is the technique."),
            ("p", "Inspection reads code; testing runs it. The next lesson, “Structured Basis "
                  "Testing”, counts how many tests a routine needs before every decision in it "
                  "has gone both ways."),
        ],
        "lab": ("cckit", {
            "mode": "defects",
            "view": "pipeline",
            "injected": 100,
            "preset": "test-only",
            "presets": [
                {"id": "test-only",
                 "label": "Testing only: unit 30 percent, system 40, at 20 hours each",
                 "stages": "unit test, 3/10, 20; system test, 4/10, 20",
                 "expect": {"dfFound": "58", "dfRemaining": "42", "dfHours": "1,160",
                            "dfPerDefect": "20"}},
                {"id": "inspect-first",
                 "label": "A code inspection at 60 percent and 3.5 hours, then the same tests",
                 "stages": "code inspection, 6/10, 7/2; unit test, 3/10, 20; system test, 4/10, 20",
                 "expect": {"dfRemaining": "84/5 = 16.80", "dfHours": "674",
                            "dfPerDefect": "1685/208 ≈ 8.10"}},
                {"id": "three-and-twelve",
                 "label": "Microsoft's figures as the book reports them: 3 hours and 12",
                 "stages": "code inspection, 6/10, 3; unit test, 3/10, 12; system test, 4/10, 12",
                 "expect": {"dfRemaining": "84/5 = 16.80", "dfHours": "2292/5 = 458.40",
                            "dfPerDefect": "573/104 ≈ 5.51"}},
            ],
            "panel_title": "Defects found, and the hours it took",
            "panel_intro": (
                "Each stage is a name, its rate, and the hours it spends per defect it finds. "
                "A stage's hours are the defects it finds times that figure, which assumes a "
                "stage costs nothing when it finds nothing. Figures: rates from the book's "
                "Table 20-2, after Jones; hours as the book reports them, Kaplan for IBM and "
                "Moore for Microsoft; 20 hours for testing is illustrative."
            ),
        }),
        "steps_title": "Reading as an inspector, and costing a pipeline",
        "steps_intro": "Two steps of reading, two of arithmetic, and one with your own reviews.",
        "steps": [
            ("Prepare alone, against the promise",
             "Read the routine's comment or specification first, then each line against it. "
             "Note each suspected defect with its line number, and do not stop to fix it."),
            ("Ask the checklist's questions",
             "For each variable, ask where it is set first and whether that value is right; "
             "for each comparison, whether it should include its boundary; for each parameter, "
             "whether it is used."),
            ("Run the defects through the stages",
             "Multiply the defects reaching each stage by its rate to get what it finds, and "
             "pass the rest on to the next stage."),
            ("Cost each stage",
             "Multiply what each stage finds by its hours per defect found, add the hours, and "
             "divide the total by the defects found."),
            ("Compare a review of your own with its tests",
             "Take the last change you reviewed or had reviewed, list what each reviewer "
             "found, and mark each finding that the existing tests had not caught. Write the "
             "two counts side by side."),
        ],
        "worked": {
            "title": "An inspection in front of two tests",
            "intro": [
                "Take the <code>inspect-first</code> preset: 100 defects, a code inspection at "
                "60 percent and 3.5 hours per defect found, then unit testing at 30 percent and "
                "system testing at 40, each at 20 hours.",
            ],
            "lines": [
                "inspection:  60 found × 3.5 h gives 210 h",
                "unit test:  12 of 40 found × 20 h gives 240 h",
                "system test:  11.2 of 28 found × 20 h gives 224 h",
                "total:  83.2 found in 674 h",
                "per defect:  674 / 83.2, about 8.10 h",
            ],
            "after": [
                "Testing alone, the <code>test-only</code> preset, found 58 defects in 1,160 "
                "hours, 20 hours each. The pipeline with the inspection finds 25 more in fewer "
                "hours, on the assumption the note names.",
            ],
        },
        "quiz_title": "Inspection and its cost",
        "quiz": [
            {"q": "Read <code>countPassing</code> as an inspector. Which list names the defects "
                  "in it?",
             "a": ["Line 3 starts `count` at 1; line 5 uses `>` where the comment promises at "
                   "or above; the parameter `maxScore` on line 2 is never used",
                   "Line 4 should loop while `i <= scores.length`; line 3 starts `count` at 1",
                   "Line 5 should use `>=`, and nothing else is wrong",
                   "Line 6 should be `count++`; line 5 uses `>` where the comment promises at "
                   "or above"],
             "c": 0,
             "why": "Line 3 starts <code>count</code> at 1 instead of 0, so every result is one "
                    "too many. Line 5 tests <code>scores[i] &gt; passMark</code>, but the "
                    "comment promises at or above the mark, so a score equal to it is not "
                    "counted. The parameter <code>maxScore</code>, line 2, is never used. Two of "
                    "the three are on the chapter's checklist kinds, initialisation and "
                    "off-by-one comparisons, and the third is a parameter nobody reads. The loop "
                    "on line 4 is right as written (<code>&lt;=</code> would read past the end), "
                    "and <code>count = count + 1</code> and <code>count++</code> do the same."},
            # F18, p. 472.
            {"q": "In the figures the book reports from IBM (Kaplan 1995), how many staff-hours "
                  "did it take to find each error by code inspection, and by testing?",
             "a": ["3.5 against 15 to 25", "3 against 12", "15 to 25 against 3.5",
                   "35 against 150 to 250"],
             "c": 0,
             "why": "Section 20.3, p. 472: 3.5 staff-hours per error found by code inspection "
                    "against 15 to 25 by testing, at IBM, as the book cites Kaplan 1995. The "
                    "pair 3 against 12 is Microsoft's, from Moore 1992, and measures finding "
                    "and fixing together. Both are those organisations' averages."},
            {"q": "100 defects pass a code inspection that finds 60 percent, then unit testing "
                  "at 30 percent. How many does unit testing find?",
             "a": ["12", "30", "28", "18"],
             "c": 0,
             "why": "Unit testing sees only the 40 the inspection missed, and 30 percent of 40 "
                    "is 12. Thirty would be 30 percent of all 100, 28 is what unit testing "
                    "passes on, and 18 is 30 percent of the 60 the inspection already found."},
            {"q": "In the formal inspection the chapter describes, who reads or paraphrases the "
                  "code at the meeting?",
             "a": ["Someone other than the author, chosen by the moderator", "The author",
                   "The scribe", "A manager, so that the results are recorded"],
             "c": 0,
             "why": "Section 21.3, p. 488: the moderator chooses someone other than the author "
                    "to paraphrase the design or read the code, so that the code has to speak "
                    "for itself. The scribe records the defects, and management does not "
                    "attend."},
        ],
        "mistakes": [
            ("Thinking reviews cost time that testing would not",
             "The objection is that an hour spent reading code is an hour not spent writing "
             "it, while tests run by themselves. The book reports the opposite from two "
             "organisations: at IBM, 3.5 hours to find a defect by inspection against 15 to "
             "25 by testing (Kaplan, as the book cites him); at Microsoft, about 3 hours to "
             "find and fix one against 12 (Moore). Testing still has to find the defects the "
             "review misses, and debugging still has to find their causes. On the lesson's "
             "illustration, putting an inspection first takes the hours from 1,160 to 674 "
             "while finding more, under the assumption the note names."),
            ("Fixing the code in the inspection meeting",
             "The chapter's inspection finds defects and stops: discussion of a defect ends as "
             "soon as it is recognised, and the fixes are the author's afterwards. Solutions "
             "debated in the meeting slow it down and turn it into an argument about style. "
             "Anyone who wants to talk about fixes can stay for the informal third-hour "
             "meeting."),
            ("Treating a walk-through as an inspection with less paperwork",
             "A walk-through has no defined roles, is usually led by the author and has no "
             "follow-up, and the book reports, after Jones, that walk-throughs find "
             "significantly fewer defects than inspections. McConnell's view is that a "
             "review worth holding a meeting for is worth running as an inspection."),
        ],
        "standard": (
            "Finish when you can list a routine's defects as an inspector would and cost a "
            "pipeline with an inspection in it.",
            "For a ten-line routine with planted defects, list each defect with its line; for "
            "an inspection followed by two tests, compute the defects found, the defects left "
            "and the hours per defect found, and compare them with testing alone."
        ),
        "note": (
            "The pipeline assumes each stage's hours are the defects it finds times its hours "
            "per defect found, so a stage that finds nothing costs nothing. A real test suite "
            "costs its running time and upkeep whether it finds anything or not, so the hours "
            "for testing after an inspection are understated, and the totals hold only under "
            "the model's assumption. The hours per defect are the book's reports of IBM's and "
            "Microsoft's averages, and 20 hours for testing is the lesson's choice inside "
            "IBM's range."
        ),
    },
    # ---------------------------------------------------------------- 03
    # McConnell Chapter 22, pp. 499-509 (to the end of structured basis
    # testing). Quote: p. 533 (Key Points), 27 words. Testing's role and
    # limits, pp. 500-501 (the scale, p. 501); testing during construction,
    # p. 502; recommended approach and test first, pp. 503-504 (one of the most
    # beneficial practices, p. 504); limitations, statement and branch
    # coverage, p. 504; exhaustive testing, p. 505; structured basis testing and
    # the counting rule, pp. 505-508. This is the course's modern aside (PLAN
    # F.4): test-first and test-driven development, in a late p.
    {
        "slug": "structured-basis-testing",
        "title": "Structured Basis Testing",
        "module": "Chapter 22 · Developer Testing",
        "one_line": "A routine needs at least one test for each way through its decisions, and running every line once is not the same thing.",
        "summary": (
            "The first half of Chapter 22: developer testing's place in quality, the "
            "approach the book recommends, writing tests first, and structured basis "
            "testing. Count the minimum number of test cases a routine needs from its "
            "decision points, and write one input for each, so that every decision is made "
            "true once and false once."
        ),
        "key": [
            "start with 1 for the straight path",
            "add 1: if, while, for, &&, ||",
            "add 1 per case, and 1 for no default",
            "the count is the fewest tests, not enough",
            "make each decision true once, false once",
        ],
        "key_label": "Counting basis tests",
        "concepts_intro": (
            "Three ideas from the first half of the chapter: what developer testing is, how "
            "much of a routine one test touches, and the count that says how many tests are "
            "the least you can write."
        ),
        "concepts": [
            ("White-box testing",
             "Testing with the code in view. The chapter is about the testing a developer "
             "does on their own routines, where you know what is inside the box and can "
             "choose tests to exercise it."),
            ("Statement and branch coverage",
             "Statement coverage asks that every line run at least once; branch coverage asks "
             "that every condition come out true at least once and false at least once. The "
             "chapter calls the first a good start and the second a better standard."),
            ("Structured basis testing",
             "A way to reach branch coverage with the fewest tests: count one for the straight "
             "path and one for each decision, then write a test for each, so that every "
             "decision goes each way."),
        ],
        "read_title": "Developer testing, then the counting rule",
        "read_intro": (
            "The lesson reads the chapter from its start to the end of structured basis "
            "testing; the rest of the chapter is the next lesson."
        ),
        "body": [
            ("p", "<strong>Code Complete, Chapter 22, p. 533.</strong> &ldquo;Writing test "
                  "cases before the code takes the same amount of time and effort as writing "
                  "the test cases after the code, but it shortens "
                  "defect-detection-debug-correction cycles.&rdquo; Read Chapter 22 from page "
                  "499 to the end of structured basis testing on page 509 in your own copy "
                  "first; the rest of the chapter is the next lesson."),
            ("p", "You have a routine whose tests all pass, and a coverage tool reports that "
                  "they ran every line. Is it tested? Chapter 22 is about the testing you do "
                  "on your own code, and its first section (p. 500) begins by putting it in "
                  "its place. Testing is often a project's only quality technique, which the "
                  "chapter calls unfortunate; it tries to break what every other activity "
                  "tries to build; it can never prove that no errors "
                  "remain; and by itself it does not improve anything. McConnell's comparison "
                  "is that trying to improve software by testing more is like trying to lose "
                  "weight by weighing yourself more often."),
            ("p", "Section 22.2 (p. 503) sets out the approach the book recommends: test each "
                  "relevant requirement and each design concern, add basis tests and then "
                  "data-flow tests to exercise the code, and keep a checklist of the errors "
                  "you have made before. It argues for writing test cases first. Doing so, it "
                  "says, takes no more effort than writing them after, finds defects sooner, "
                  "makes you think about the requirements before you code, and exposes a poor "
                  "requirement early, because a test for one is hard to write. McConnell calls "
                  "test-first programming one of the most beneficial practices to emerge in "
                  "the decade before the book, and adds that it is no panacea, because it has "
                  "developer testing's limits."),
            ("p", "Those limits come next (p. 504). Developers tend to write clean tests, "
                  "checking that the code works, rather than dirty ones, looking for the ways "
                  "it breaks. They believe their tests cover more of the code than they do. "
                  "And most of them, the book says, regard running every statement once as "
                  "adequate. It is a good start, McConnell writes, but a better standard is "
                  "branch coverage, with every condition tested at least once true and once "
                  "false."),
            ("p", "Section 22.3 (p. 505) begins from the fact that testing everything is "
                  "impossible: even a program that stores a name, an address and a telephone "
                  "number has so many possible inputs, the book calculates, that trying them "
                  "all is out of the question. So the art is choosing the few tests that tell you different "
                  "things. The first technique, structured basis testing, despite what the "
                  "book calls its hairy name, comes with a counting rule (p. 506). Start with "
                  "1 for the straight path through the routine. Add 1 for each "
                  "<code>if</code>, <code>while</code>, <code>repeat</code> and "
                  "<code>for</code>, and for each <code>and</code> and <code>or</code>, in "
                  "Java `&&` and `||`. Add 1 for each case of a <code>case</code> statement, "
                  "and 1 more if it has no default. It is the same count as the decision "
                  "points of “Nesting and Complexity”, used here for a different purpose."),
            ("def", ("Basis test cases",
                     "The number the rule gives is the fewest test cases that can make every "
                     "decision in the routine come out true once and false once. It is a "
                     "minimum: the book warns that any set of that many tests will not do, "
                     "only one chosen so that each decision goes each way.")),
            ("code", _lines(OVERTIME)),
            ("p", "The <code>overtime</code> preset reads <code>overtimePay</code> and prints "
                  "Basis test cases 5, and its Decision points, in line order, are the while "
                  "and the `&&` on line 4, the if on line 6 and the if on line 8: the "
                  "<code>else if</code> on line 8 counts as an <code>if</code>, and the <code>else</code> alone counts "
                  "nothing. The tile switch with no default reads 0. Five tests make each "
                  "decision go both ways: <code>count</code> 0, so the loop never starts; "
                  "<code>count</code> 1 with a null first entry, so the loop stops at the "
                  "second half of its condition; one exempt employee; one non-exempt employee "
                  "with 45 hours; and one with exactly 40, where the overtime test is false."),
            ("p", "Now the coverage tool's verdict. A single call with two employees, one "
                  "exempt and one with 45 hours, and <code>count</code> 2, runs every line of "
                  "the routine. It never tries a null entry, and never an employee at 40 "
                  "hours or under, so two of the five outcomes the count asks for are "
                  "untested by a suite with full statement coverage."),
            ("code", _lines(SHIPPING_LABEL)),
            ("p", "The <code>switch-without-default</code> preset reads "
                  "<code>shippingLabel</code>: case line 4, case line 7, case line 10 and "
                  "if line 14, with switch with no default 1, so Basis test cases is 1 + 3 + 1 "
                  "+ 1 = 6. The sixth case is the one the missing default adds: a zone the "
                  "switch does not name, such as 4, where <code>label</code> stays the empty "
                  "string. Whether that is right is a question for the specification, and only "
                  "a test of zone 4 asks it. In Java a case without <code>break</code> falls "
                  "through to the next, which the count does not see; it counts case labels."),
            ("p", "Test-first has had a long life since 2004. Kent Beck, whom the chapter cites "
                  "for it (Beck 2003), described test-driven development: write one failing "
                  "test, write just enough code to pass it, tidy the code, and repeat, so that "
                  "the tests lead the design in small steps. Many teams now work that way, and "
                  "it carries the book's recommendation further rather than arguing against "
                  "it. Others write tests alongside or just after the code and argue that the "
                  "order matters less than the tests' quality. The book's own claim is the "
                  "narrower one at the head of this page: first costs no more than after, and "
                  "shortens the cycle from defect to fix. Either way, the basis count says "
                  "how many tests the decisions need."),
            ("h3", "Exercise"),
            ("code", _lines(ARCHIVE_OLD)),
            ("p", "Count the basis test cases <code>archiveOld</code> needs by the rule above, "
                  "and write one input for each case so that every decision goes both ways. "
                  "Then paste the routine into the lab's code box to check your count."),
            ("p", "Basis tests check that each decision goes both ways, but not what values "
                  "reach it. The next lesson, “Boundaries and Bad Data”, reads the rest of the "
                  "chapter and tests the edges of a range."),
        ],
        "lab": ("cckit", {
            "mode": "code",
            "view": "basis",
            "preset": "overtime",
            "presets": [
                {"id": "overtime",
                 "label": "overtimePay: a while with two conditions, an if and an else if",
                 "code": OVERTIME,
                 "expect": {"coBasis": "5", "coNoDefault": "0",
                            "coPoints": "while line 4, && line 4, if line 6, if line 8"}},
                {"id": "switch-without-default",
                 "label": "shippingLabel: a switch of three cases with no default, and an if",
                 "code": SHIPPING_LABEL,
                 "expect": {"coBasis": "6", "coNoDefault": "1",
                            "coPoints": "case line 4, case line 7, case line 10, if line 14"}},
            ],
            "panel_title": "Basis test cases",
            "panel_intro": (
                "The count is 1, plus 1 for each if, while, for, do, and, or and case, plus 1 "
                "for each switch with no default: the fewest tests that can make every "
                "decision go both ways. Paste a routine of your own to count its decisions."
            ),
        }),
        "steps_title": "Counting and choosing basis tests",
        "steps_intro": "Four steps on the routine in front of you, and one on your own.",
        "steps": [
            ("Start at one",
             "One test runs the straight path through the routine, so the count starts at 1."),
            ("Add one for each decision",
             "Add 1 for each if (an else if included), while, for and do, for each && and ||, "
             "and for each case label; add 1 more for a switch with no default. An else adds "
             "nothing."),
            ("Write a test for each",
             "For each decision, choose an input that makes it true and another that makes it "
             "false; for && and ||, one where each half alone decides the result."),
            ("Check against statement coverage",
             "Ask which of your tests could be dropped while every line still runs. Each one "
             "you could drop is a decision outcome statement coverage would leave untested."),
            ("Count a routine of your own",
             "Paste one routine of yours into the lab, note its basis count, and count the "
             "tests that exist for it. Write down each decision outcome no existing test "
             "makes happen."),
        ],
        "worked": {
            "title": "Five cases for overtimePay",
            "intro": [
                "Take the <code>overtime</code> preset. The rule counts the straight path and "
                "each decision point in <code>overtimePay</code>.",
            ],
            "lines": [
                "straight path:  1",
                "while, line 4:  1",
                "&& in the while, line 4:  1",
                "if, line 6:  1",
                "else if, line 8:  1",
                "basis test cases:  5",
            ],
            "after": [
                "Five tests: <code>count</code> 0; a null first entry; an exempt employee; a "
                "non-exempt employee at 45 hours; one at 40. A single call with an exempt "
                "employee and one at 45 hours runs every line and leaves two of those outcomes "
                "untried.",
            ],
        },
        "quiz_title": "The basis count",
        "quiz": [
            {"q": "By the chapter's rule (1, plus 1 for each if, while and for, each && and ||, "
                  "each case, and a missing default), how many basis test cases does "
                  "<code>archiveOld</code> need?",
             "a": ["4", "3", "2", "5"],
             "c": 0,
             "why": "1 for the straight path, 1 for the <code>for</code>, 1 for the "
                    "<code>if</code> and 1 for the <code>||</code>: 4. One input each: an "
                    "empty inbox, so the loop never runs; an old message, where the first half "
                    "of the condition decides it; a spam message that is not old, where the "
                    "second half does; and a new message that is not spam, where the "
                    "<code>if</code> is false. Three forgets the <code>||</code>, and two "
                    "counts only the straight path and the <code>if</code>."},
            {"q": "A single call to <code>overtimePay</code> with two employees, one exempt and "
                  "one with 45 hours, and <code>count</code> 2, runs every line. Which of these "
                  "outcomes has it not tested?",
             "a": ["`staff[i]` being null", "An exempt employee",
                   "An employee with more than 40 hours",
                   "The loop ending because `i` reaches `count`"],
             "c": 0,
             "why": "The call makes the exempt test true, the overtime test true, and ends the "
                    "loop when <code>i</code> reaches 2. It never meets a null entry, the second "
                    "half of the <code>while</code> condition coming out false, and it never "
                    "tests an employee at 40 hours or under either. Full statement coverage, two "
                    "of five outcomes untried."},
            {"q": "<code>shippingLabel</code> has a switch of three cases with no default, "
                  "followed by one if. How many basis test cases does the rule give?",
             "a": ["6", "5", "4", "7"],
             "c": 0,
             "why": "1 + 3 cases + 1 for the missing default + 1 for the <code>if</code> = 6. "
                    "Five forgets the missing default, which is the case of a zone the switch "
                    "does not name; four counts the switch once; seven counts the "
                    "<code>switch</code> keyword as well as its cases."},
            {"q": "What does Section 22.2 claim about writing test cases before the code?",
             "a": ["It takes no more effort than writing them after, and defects are found "
                   "sooner",
                   "It takes about twice the effort, and halves the defects",
                   "It makes basis testing unnecessary",
                   "It guarantees branch coverage"],
             "c": 0,
             "why": "Pages 503 to 504: writing the tests first takes no more effort than "
                    "writing them after, since it only changes the order, and it detects "
                    "defects earlier. The book gives no doubling or halving, and it calls "
                    "test-first a good general approach but no panacea; the basis count still "
                    "says how many tests the decisions need."},
        ],
        "mistakes": [
            ("Thinking full statement coverage means the routine is tested",
             "Most developers, the chapter says, take running every statement once as "
             "adequate, and it calls that a good start but hardly sufficient. Basis testing "
             "asks for each decision's outcomes, both ways. On the lesson's illustration one "
             "call with an exempt employee and one at 45 hours runs every line of "
             "<code>overtimePay</code>, and never makes <code>staff[i]</code> null or tests "
             "an employee at 40 hours: two of the five outcomes the count asks for."),
            ("Taking the count as enough tests",
             "The count is a minimum. Five tests chosen carelessly, all with a non-exempt "
             "employee, can leave the exempt branch unrun; the five must be chosen so each "
             "decision goes each way. And basis tests say nothing about which values reach a "
             "decision, which is why the chapter goes on to data flow and boundaries."),
            ("Counting else as a decision",
             "An else is the other outcome of an if that has already been counted, so it adds "
             "nothing; an else if is a new if and adds one. A switch adds one per case label, "
             "and one more only when there is no default."),
        ],
        "standard": (
            "Finish when you can count a routine's basis test cases and give one input for "
            "each.",
            "For a routine with a while, an && and two ifs, state the basis count by the "
            "chapter's rule and give one input per case, so that every decision comes out "
            "true once and false once."
        ),
        "note": (
            "The lab counts decision points by the rule stated under its listing and prints "
            "the minimum number of tests; it reads the code and never runs it. It cannot tell "
            "whether your tests make each decision go both ways, or whether the expected "
            "results are right, and it counts a case label whether or not the case falls "
            "through. The routines are the lesson's illustrations."
        ),
    },
    # ---------------------------------------------------------------- 04
    # McConnell Chapter 22, pp. 509-533: the rest of section 22.3 and sections
    # 22.4-22.7. Quote: p. 533 (Key Points), 24 words. Data-flow testing, p. 509;
    # equivalence partitioning, p. 512; error guessing and boundary analysis,
    # p. 513; compound boundaries, p. 514; bad and good data, pp. 514-515;
    # hand-checks, p. 516; typical errors, pp. 517-522 (F19, p. 517 and p. 521;
    # F2, pp. 520-521); tools, p. 523; improving testing, pp. 528-529; records,
    # p. 529.
    {
        "slug": "boundaries-and-bad-data",
        "title": "Boundaries and Bad Data",
        "module": "Chapter 22 · Developer Testing",
        "one_line": "A check against a range is most often wrong at its ends, so the tests that find the error are the values on and either side of each boundary.",
        "summary": (
            "The second half of Chapter 22: data-flow testing, equivalence classes, error "
            "guessing, boundary analysis, classes of bad and good data, where errors cluster, "
            "and how testing itself improves. List the boundary tests for a range, and find "
            "which of them exposes a wrong check."
        ),
        "key": [
            "a boundary: below, on, and above it",
            "range 1 to 99: test 0 1 2 98 99 100",
            "qty < 99 is wrong at 99 only",
            "a typical value passes a wrong check",
            "errors cluster in a few routines",
        ],
        "key_label": "Boundaries in five lines",
        "concepts_intro": (
            "The second half of the chapter adds ways of choosing tests to the basis count; "
            "the lesson keeps the two that are about values, and the chapter's evidence on "
            "where errors are."
        ),
        "concepts": [
            ("Equivalence class",
             "A set of inputs that a routine treats alike, so that one test from the set finds "
             "whatever the others would. Two tests that flush out the same errors, the chapter "
             "says, need not both be run."),
            ("Boundary analysis",
             "Testing at the edges of each class, where off-by-one errors live: for a boundary "
             "at a value, the value just below it, the value itself and the value just above."),
            ("Bad data",
             "Inputs a routine should refuse or survive: too little data, too much, the wrong "
             "kind, the wrong size, data never initialised. The chapter treats them as a "
             "class of tests of their own."),
        ],
        "read_title": "The rest of the chapter, then the edges of a range",
        "read_intro": (
            "The lesson reads from data-flow testing to the end of the chapter and then tests "
            "one validation check at its boundaries."
        ),
        "body": [
            ("p", "<strong>Code Complete, Chapter 22, p. 533.</strong> &ldquo;You can generate "
                  "many test cases deterministically by using basis testing, data-flow "
                  "analysis, boundary analysis, classes of bad data, and classes of good "
                  "data.&rdquo; Read Chapter 22 from data-flow testing on page 509 to the end "
                  "on page 533 in your own copy first."),
            ("p", "Once basis tests have made every decision go both ways, what is left to "
                  "test? The chapter's answer is the data. Data-flow testing (p. 509) starts "
                  "from the claim, which it credits to Boris Beizer, that data use is at least "
                  "as error-prone as control flow. A variable is defined, used, and sometimes "
                  "killed, and some sequences are suspicious, such as one defined twice before "
                  "its value is used; the tests add a case for each place a value is defined "
                  "and then first used. Equivalence partitioning (p. 512) is the idea that two "
                  "tests flushing out the same errors need not both be run, so each class of "
                  "inputs a routine treats alike needs one."),
            ("p", "Error guessing (p. 513) is a lowbrow name, the book says, for a sensible "
                  "idea: test where your experience says errors are. The most fruitful place "
                  "is the boundary. Off-by-one errors, writing <code>&gt;=</code> where "
                  "<code>&gt;</code> was meant, sit there, and boundary analysis tests each "
                  "boundary three times: just below it, on it, and just above it. Compound "
                  "boundaries (p. 514) involve several variables at once, two large numbers "
                  "multiplied, every string at its longest. Then come classes of bad data, "
                  "such as too little data, too much, or the wrong kind, and of good data, from "
                  "the nominal case to the smallest and largest normal configurations. "
                  "McConnell adds a practical aside: choose test values you can check by hand, "
                  "because an ugly number is no more likely to find an error than a round one "
                  "in the same class, and much more likely to spoil your arithmetic."),
            # F19, pp. 517 and 521; F2, pp. 520-521.
            ("p", "Section 22.4 (p. 517) is about the errors themselves. They are not spread "
                  "evenly. The book reports that about 80 percent of errors are found in 20 "
                  "percent of a project's classes or routines (after Endres 1975, Boehm 1987 "
                  "and others) and about half in 5 percent (Jones 2000). Construction causes "
                  "at least 35 percent of all defects whatever the project's size, and about "
                  "three-quarters on small projects. The industry average it gives is about 1 "
                  "to 25 errors per thousand lines of delivered code. It also warns that error "
                  "taxonomies disagree wildly from study to study, and that test data is often "
                  "as likely to contain errors as the code it tests, so your own records are "
                  "worth more than anyone's averages."),
            ("p", "The last three sections are shorter. Section 22.5 (p. 523) surveys test "
                  "support: scaffolding, stub objects that stand in for a class not yet "
                  "written, drivers that call the code under test, file comparators, coverage "
                  "monitors and the rest. Section 22.6 (p. 528) argues that regression testing, "
                  "running the same tests after every change, is only practical when it is "
                  "automated. Section 22.7 (p. 529) lists what to record about each defect, so "
                  "that you can tell whether the project is getting healthier."),
            ("def", ("The six boundary tests of a range",
                     "For a range from a low value to a high one, boundary analysis gives three "
                     "tests at each end: one below the low value, the low value itself and one "
                     "above it; one below the high value, the high value itself and one above "
                     "it. On integers that is six tests.")),
            ("p", "The lab takes a specification and a check: an order of 1 to 99 items is "
                  "valid, and the check says <em>valid</em> when it is true. The "
                  "<code>correct</code> preset is `qty >= 1 && qty <= 99`. The lab tries it on "
                  "every integer and prints Where check and range disagree: none. Boundary "
                  "tests lists the six values 0, 1, 2, 98, 99, 100, and Tests that expose a "
                  "difference reads none, because there is none to expose."),
            ("p", "The <code>strict-top</code> preset is `qty > 0 && qty < 99`. Its lower half "
                  "is the same check as `qty >= 1` on integers, but its upper half refuses 99, "
                  "the largest valid order: Where check and range disagree reads 99, and of "
                  "the six boundary tests only 99 exposes it. The <code>no-lower-check</code> "
                  "preset is `qty <= 99`, which accepts 0 and every negative quantity: the "
                  "disagreement is 0 and below, and the test 0 is the one that exposes it. A "
                  "typical order of 50 passes all three checks. On the lesson's illustration, "
                  "only the boundary tests tell the right check from the two wrong ones."),
            ("h3", "Exercise"),
            ("code", _lines(VALID_LENGTH)),
            ("p", "A password must be 8 to 64 characters long, and <code>validLength</code> "
                  "returns true for a valid one. Write the six boundary tests for that range, "
                  "say what the check returns for each, and name each test it gets wrong. To "
                  "check, type the check into the lab with the range's ends."),
            ("p", "That ends Chapter 22 and the first half of this course. Tests find that "
                  "something is wrong; the next lesson, “Debugging as Science”, is about "
                  "finding out what."),
        ],
        "lab": ("cckit", {
            "mode": "cond",
            "view": "range",
            "means": "valid",
            "lo": 1,
            "hi": 99,
            "preset": "correct",
            "presets": [
                {"id": "correct",
                 "label": "qty from 1 to 99, checked on both ends",
                 "cond": "qty >= 1 && qty <= 99",
                 "expect": {"cdDisagree": "none", "cdTests": "0, 1, 2, 98, 99, 100",
                            "cdExposed": "none"}},
                {"id": "strict-top",
                 "label": "A strict comparison at the top",
                 "cond": "qty > 0 && qty < 99",
                 "expect": {"cdDisagree": "99", "cdExposed": "99"}},
                {"id": "no-lower-check",
                 "label": "No check on the lower end",
                 "cond": "qty <= 99",
                 "expect": {"cdDisagree": "0 and below", "cdExposed": "0"}},
            ],
            "panel_title": "A validation check at its boundaries",
            "panel_intro": (
                "The specification is a range of whole numbers and what a true check means. The "
                "lab compares the check with the range on every integer, and lists the six "
                "boundary tests and which of them would expose a difference."
            ),
        }),
        "steps_title": "Testing a range at its edges",
        "steps_intro": "Four steps for any range check, and one for a check of your own.",
        "steps": [
            ("Write the range down",
             "State the lowest and highest valid values from the specification, not from the "
             "code, and whether the ends are included."),
            ("List the six boundary values",
             "One below the low end, the low end, one above it; one below the high end, the "
             "high end, one above it."),
            ("Evaluate the check at each",
             "Work out what the check returns for each of the six values and what the "
             "specification says it should."),
            ("Name the tests that disagree",
             "Every value where the two differ is a test that exposes the error. A test that "
             "agrees with both is still worth keeping, against later changes."),
            ("Test a validation of your own",
             "Find one validation in your own code, write down its documented range, list its "
             "six boundary tests, and mark which of them your test suite already has."),
        ],
        "worked": {
            "title": "A strict comparison at the top",
            "intro": [
                "Take the <code>strict-top</code> preset: orders of 1 to 99 items are valid, "
                "and the check is `qty > 0 && qty < 99`.",
            ],
            "lines": [
                "boundary tests:  0, 1, 2, 98, 99, 100",
                "valid by the range:  1, 2, 98, 99",
                "true by the check:  1, 2, 98",
                "they differ at:  99",
                "a typical order, 50:  both say valid",
            ],
            "after": [
                "The check refuses the largest valid order, and the test 99 is the only one of "
                "the six that shows it; a test at 50 cannot.",
            ],
        },
        "quiz_title": "Boundaries and errors",
        "quiz": [
            {"q": "Passwords of 8 to 64 characters are valid, and the check is "
                  "`len > 8 && len <= 64`. Which of the six boundary tests does the check get "
                  "wrong?",
             "a": ["8 only", "8 and 64", "64 only", "7 and 65"],
             "c": 0,
             "why": "The boundary tests are 7, 8, 9, 63, 64 and 65. The range says 8 to 64 are "
                    "valid; the check is true for 9 to 64. They differ at 8 only, the shortest "
                    "valid password, and only the test 8 exposes it. At 64 both say valid, and "
                    "at 7 and 65 both say invalid."},
            {"q": "Boundary analysis, as Section 22.3 describes it, tests a boundary at a "
                  "maximum with how many cases?",
             "a": ["Three: just below it, on it and just above it", "Two: on it and above it",
                   "One: the maximum itself", "Four: two either side of it"],
             "c": 0,
             "why": "Page 513: there are three boundary cases, just less than the maximum, the "
                    "maximum itself and just greater, and it takes all three to rule out the "
                    "common mistakes. A range has two boundaries, so six tests."},
            {"q": "Which check is the same as `qty >= 1 && qty <= 99` on every integer?",
             "a": ["`qty > 0 && qty < 100`", "`qty > 0 && qty < 99`",
                   "`qty >= 1 || qty <= 99`", "`qty > 1 && qty <= 99`"],
             "c": 0,
             "why": "On integers, <code>qty &gt; 0</code> is <code>qty &gt;= 1</code> and "
                    "<code>qty &lt; 100</code> is <code>qty &lt;= 99</code>, so the first is the "
                    "same check. <code>qty &lt; 99</code> refuses 99; <code>||</code> accepts "
                    "every integer; <code>qty &gt; 1</code> refuses 1."},
            # F19, p. 517.
            {"q": "How does the book report errors are distributed among a project's classes "
                  "and routines (after Endres, Boehm and others)?",
             "a": ["About 80% of the errors are in 20% of them",
                   "About 20% of the errors are in 80% of them",
                   "Evenly, at about 10 per 1,000 lines in each",
                   "About 50% of the errors are in 50% of them"],
             "c": 0,
             "why": "Section 22.4, p. 517: eighty percent of the errors are found in 20 percent "
                    "of a project's classes or routines, after Endres 1975, Gremillion 1984, "
                    "Boehm 1987 and Shull et al. 2002, and fifty percent in 5 percent after "
                    "Jones 2000. The chapter calls the assumption of an even spread natural and "
                    "wrong."},
        ],
        "mistakes": [
            ("Thinking one typical value per case is enough",
             "A typical value per equivalence class is the efficient part of the chapter's "
             "advice, and a reader can stop there. But a class's errors are at its edges. On "
             "the lesson's illustration an order of 50 passes the right check, the check that "
             "refuses 99 and the check that accepts 0; only the boundary tests, 99 and 0, tell "
             "the three apart."),
            ("Testing only with good data",
             "Developers tend to test that the code works rather than the ways it breaks. The "
             "chapter's classes of bad data, such as no data, too much data, the wrong kind and "
             "uninitialised data, are tests of their own, and a check that accepts 0 and every "
             "negative quantity is found by them."),
            ("Expecting errors to be spread evenly",
             "With ten defects per thousand lines it is natural to expect one in a 100-line "
             "class. The book reports instead, after Endres, Boehm and others, that about 80 "
             "percent of errors are in 20 percent of the classes and routines. Your own defect "
             "records will show where yours cluster."),
        ],
        "standard": (
            "Finish when you can list a range's boundary tests and name the ones a check gets "
            "wrong.",
            "For a valid range and a check, write the six boundary values and name each that "
            "the check gets wrong."
        ),
        "note": (
            "The lab compares the check with the range on every integer and lists the six "
            "boundary tests; it reads the condition and never runs code. It handles one "
            "variable compared with whole numbers, so compound boundaries, bad data of the "
            "wrong type and data-flow tests are the chapter's and the reader's to work out. "
            "The figures on where errors cluster are the book's reports of other people's "
            "projects."
        ),
    },
]
