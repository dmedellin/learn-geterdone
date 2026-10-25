"""Laying the Foundation, lessons 1-3 -- Part I of Code Complete, Chapters 1-4.

Every quotation is copied from McConnell, Code Complete, 2nd edition
(Microsoft Press, 2004), character for character, with its printed page in
the comment beside the lesson and checked against the text; each lesson's
quotations total at most 60 words (docs/code-complete/PLAN.md section E.3).
A figure attributed to the book carries its id in the register of figures
(PLAN section S.2) and its page. The hours in the first lab are the lesson's
own; the cost table and the statement ratios are the book's, after the
sources it names. The one Java snippet is written for this course.
"""

from fractions import Fraction

# Key Construction Decisions: Java has no default parameter values, and this
# convention supplies them. Written for the lesson; nothing in it is the
# book's. Line numbers in the prose count every line from 1.
SEND_WITH_DEFAULT = """\
// Java has no default argument values. The team's convention: the
// full version holds the logic, and each shorter one forwards to it.
static final int DEFAULT_RETRIES = 3;

boolean send(Message message) {
    return send(message, DEFAULT_RETRIES);
}

boolean send(Message message, int retries) {
    for (int attempt = 1; attempt <= retries; attempt++) {
        if (transmit(message)) {
            return true;
        }
    }
    return false;
}"""

# Table 3-1 as the lesson gives it (F3, p. 29): (introduced, detected) to the
# relative cost of the fix. The stages are requirements, architecture,
# construction, system test and post-release.
COST_TABLE = {
    ("req", "req"): 1, ("req", "arch"): 3, ("req", "cons"): (5, 10),
    ("req", "test"): 10, ("req", "post"): (10, 100),
    ("arch", "arch"): 1, ("arch", "cons"): 10, ("arch", "test"): 15,
    ("arch", "post"): (25, 100),
    ("cons", "cons"): 1, ("cons", "test"): 10, ("cons", "post"): (10, 25),
}

LESSONS = [
    # ---------------------------------------------------------------- 01
    # McConnell Chapters 1-2, pp. 3-21: section 1.1 (p. 3; the list of
    # activities pp. 3-4, construction's tasks pp. 5-6, "coding" p. 5), 1.2
    # (p. 6; the four reasons p. 7), 1.3 (p. 8); 2.1 (pp. 9-11), 2.2
    # (pp. 11-12), 2.3 (pp. 13-20; writing p. 13, Brooks p. 14 and p. 16,
    # farming pp. 14-15, accretion pp. 15-16, building pp. 16-19, toolbox and
    # combining p. 20).
    # Quotations: p. 8, 21 words (the opening); p. 14, Brooks's line as the
    # book quotes it, 8 words; p. 12, 6 words. Total 35, cc_quotes.py OK.
    # F1, p. 7: construction takes 30 to 80 percent of a project's time.
    # F30, p. 55: named in the fourth quiz item's why, as Chapter 3's figure.
    {
        "slug": "construction-and-its-metaphors",
        "title": "Construction and Its Metaphors",
        "module": "Chapters 1–2 · Construction and Metaphors",
        "one_line": "Construction is the middle of software development, the one activity every project does, and the metaphor you think about it with decides what you notice.",
        "summary": (
            "Chapter 1 says what the book means by construction and why it is the activity "
            "to concentrate on; Chapter 2 asks which picture of software development to "
            "think with, and prefers building and accretion to writing and farming. Mark a "
            "project's activities as construction or not by the chapter's list, and compute "
            "construction's share of the hours."
        ),
        "key": [
            "construction: the activity sure to happen",
            "construction: 30 to 80 per cent of time",
            "metaphors: heuristics, not algorithms",
            "writing: adequate only for small work",
            "building: planning grows with the size",
            "share: construction hours / all hours",
        ],
        "key_label": "Chapters 1 and 2 in six lines",
        "concepts_intro": (
            "Two short chapters, one about what is done and one about how to think about "
            "it. Three ideas carry both."
        ),
        "concepts": [
            ("Construction",
             "The book's word for the middle of software development: detailed design, "
             "coding and debugging, construction planning, unit testing, integration and "
             "integration testing. It excludes problem definition, requirements, "
             "architecture, system testing and maintenance, which matter as much but are "
             "not the book's subject."),
            ("A metaphor as a heuristic",
             "A heuristic is a technique that helps you look for an answer without "
             "promising to find it; an algorithm is a set of instructions that leads to the "
             "answer every time. Chapter 2 says software metaphors are heuristics: they "
             "suggest what to look at, and you cannot check a line of code against one."),
            ("Accretion and building",
             "The two metaphors the chapter prefers. Accretion, growth by small additions, "
             "pictures incremental development, a running skeleton filled in a piece at a "
             "time. Building adds that the planning a structure needs grows with its size, "
             "and that changing a foundation late costs more than changing a fitting."),
        ],
        "read_title": "The key point first, then the two chapters section by section",
        "read_intro": (
            "The quotation is Chapter 1's first key point. The lesson goes through Chapter 1's "
            "three sections and Chapter 2's three, then marks a project's activities by "
            "Chapter 1's list."
        ),
        "body": [
            ("p", "<strong>Chapter 1, p. 8.</strong> &ldquo;Software construction is the "
                  "central activity in software development; construction is the only "
                  "activity that’s guaranteed to happen on every project.&rdquo; It is the "
                  "first of the chapter's key points, and Chapter 1 is the argument for it. "
                  "Read Chapters 1 and 2 in your own copy first, pages 3 to 21; they are the "
                  "two shortest chapters in the book, and the lesson goes back through them a "
                  "section at a time."),
            ("p", "Chapter 1 asks a question that sounds too easy to need asking: what is "
                  "software construction? Section 1.1 (p. 3) answers by placing it among the "
                  "activities researchers had separated out of software development over the "
                  "previous twenty-five years: problem definition, requirements development, "
                  "construction planning, architecture, detailed design, coding and "
                  "debugging, unit testing, integration testing, integration, system testing "
                  "and corrective maintenance. Construction, in the book's sense, is the "
                  "middle of that list: mostly coding and debugging, and also detailed design "
                  "(the design of classes and routines, where architecture is the design of "
                  "the system as a whole), construction planning, unit testing, integration "
                  "and integration testing. If you taught yourself to program, McConnell "
                  "says, you probably filed all of it under programming, and the intuition is "
                  "fairly accurate. What it lacks is perspective: the sight of construction "
                  "among the activities around it."),
            ("p", "The section then goes down a level, to the tasks construction involves: "
                  "checking that the groundwork has been laid, deciding how your code will be "
                  "tested, designing and writing classes and routines, naming variables and "
                  "constants, choosing control structures, testing and debugging your own "
                  "code, reviewing teammates' low-level designs and code and having them "
                  "review yours, formatting and commenting, integrating components built "
                  "separately, and tuning. Outside it are management, requirements "
                  "development, architecture, user-interface design, system testing and "
                  "maintenance, and McConnell adds that each of those affects a project's "
                  "success as much as construction does. He also says why he will not simply "
                  "call it coding: the word suggests the mechanical translation of a finished "
                  "design, and construction, he says, is not mechanical at all but calls for "
                  "creativity and judgement. The rest of the book is his evidence for that "
                  "sentence."),
            # F1, p. 7
            ("p", "Section 1.2 (p. 6) gives four reasons to concentrate on construction. It "
                  "is a large part of the work: depending on the size of the project, the "
                  "book says, construction takes 30 to 80 percent of the total time, a range "
                  "that is its own synthesis and that Section 27.5 breaks down by project "
                  "size. It is central: requirements and architecture are done so that "
                  "construction can be done well, and system testing checks that it was. Its "
                  "product, the source code, is often the only accurate description of the "
                  "software, because specifications go out of date and the code cannot. And "
                  "it is the one activity sure to happen. Real projects skip requirements and "
                  "design to start coding, and drop testing when they run out of time; no "
                  "project, however rushed, drops construction, so improving it improves "
                  "every project. Section 1.3 (p. 8) is a page on how to read the book, "
                  "cover to cover or by topic."),
            ("p", "Chapter 2 moves from what construction is to how to think about it. "
                  "Section 2.1 (p. 9) argues that important ideas often come from analogies, "
                  "and that the analogy decides what you look at. Kekulé dreamed of a snake "
                  "biting its tail and saw the benzene ring. The wave theory of light grew "
                  "from comparing light with sound, and the same comparison sent physicists "
                  "looking for an ether that was never found: a model stretched past the "
                  "point where it held. An Aristotelian watching a swinging stone saw an "
                  "object falling with difficulty, Galileo saw a pendulum, and they measured "
                  "different things. The history of science, McConnell concludes, is a "
                  "series of changes from worse metaphors to better ones rather than from "
                  "wrong to right, and software development, a young field, has many of "
                  "both."),
            ("p", "Section 2.2 (p. 11) says how to use them. A software metaphor is more like "
                  "a searchlight than a road map: it tells you how to look for an answer, not "
                  "where the answer is. That makes it a heuristic rather than an algorithm. "
                  "An algorithm is a set of well-defined instructions that takes you from one "
                  "point to another with no detours; a heuristic helps you look, and its "
                  "results depend partly on chance. In McConnell's own phrase, a heuristic is "
                  "&ldquo;an algorithm in a clown suit&rdquo;. The practical consequence is "
                  "stated plainly: you will not be able to look at a line of code and say "
                  "that it violates a metaphor. A metaphor shapes what you notice about your "
                  "work over time, and that is all it does."),
            ("p", "Section 2.3 (p. 13) goes through the metaphors on offer, from science, art "
                  "and process to a game, a bazaar and a tar pit, and takes the commonest "
                  "first. The writing metaphor, from the phrase writing code, pictures a "
                  "program as a casual letter: you sit down, write it from start to finish "
                  "and work out what you mean as you go. For one person's work or a small "
                  "project, McConnell says, it works adequately; beyond that it fails. "
                  "Writing is usually done alone, and a software project involves many "
                  "people. A letter is finished when it is posted, and software is changed "
                  "for years after its first release and is hardly ever complete. Writing "
                  "prizes originality, where construction often does better to reuse "
                  "designs, code and tests. The metaphor, he concludes, implies a process too "
                  "simple and too rigid to be healthy."),
            ("p", "The chapter tells a story here with a turn in it. Fred Brooks's <em>The "
                  "Mythical Man-Month</em> had advised, in 1975, &ldquo;Plan to throw one "
                  "away; you will, anyhow.&rdquo; McConnell reads the line as the writing "
                  "metaphor's, a wastebasket of drafts, and calls it poor advice where a "
                  "major system costs as much as a ten-story office building: better, he says, "
                  "to succeed at the first attempt, or to make your several attempts while "
                  "they are still cheap. Two pages later he reports what Brooks wrote in the anniversary "
                  "edition of 1995: that nothing in the decade after the book had so "
                  "radically changed his own practice, or its effectiveness, as incremental "
                  "development. The man who said to throw one away had come to build one a "
                  "little at a time."),
            ("p", "That is where the chapter goes next. The farming metaphor, plant a "
                  "little and grow a little, describes a good technique with a poor image, "
                  "McConnell says: doing a little at a time is valuable, but the image is "
                  "hard to extend past that one idea, and it suggests that you have no direct "
                  "control over how the software develops. He prefers <em>accretion</em>, "
                  "growth by gradual addition, the way an oyster makes a pearl. In "
                  "incremental development you first build the simplest version of the "
                  "system that will run, a skeleton calling dummy classes, and then replace "
                  "the dummies with real code a piece at a time until the system works. Its "
                  "strength as a metaphor, he says, is that it does not overpromise."),
            ("p", "The metaphor he finds most useful is building, because it fits accretion "
                  "and says more. Planning, preparation and execution vary in kind and degree "
                  "with what is built. A doghouse takes an afternoon, and if you forget the "
                  "door you fix it or start again; the same loose approach suits a thousand "
                  "lines of code. A house needs a problem definition, an architect, "
                  "blueprints and inspections, and moving one of its walls six inches is "
                  "expensive because of the labour, not the nails. You buy the dishwasher "
                  "rather than build it, as you use a library; moving a load-bearing wall "
                  "costs more than moving a partition, as a structural change to a program "
                  "costs more than a peripheral one. The section ends with the toolbox, "
                  "techniques held as tools rather than rules, and with the advice to combine "
                  "metaphors, which, being heuristics, do not exclude one another."),
            ("p", "Chapter 1's list makes a count possible, and the lab does it. It takes a "
                  "project's activities as records, a name, the hours and a <code>c</code> "
                  "where you mark the activity as construction, and adds. On the "
                  "<code>small-project</code> preset, illustrative hours for a project of "
                  "1,000 hours, the four construction activities are detailed design (120), "
                  "coding and debugging (320), unit testing (130) and integration (90), so "
                  "the total tile reads 1,000 and the share tile 33/50 = 66%. The largest "
                  "entry tile names coding and debugging at 8/25 = 32%: on this illustration "
                  "construction is mostly coding and debugging, as the chapter says, and "
                  "still more than half other work. The last tile counts the fewest "
                  "entries, taken largest first, whose hours reach four-fifths of the total: "
                  "six of the eight, so here the hours are spread across the activities, "
                  "not gathered in one or two."),
            ("p", "The <code>large-project</code> preset has the same activities on a project "
                  "of 12,000 hours, with more of them spent on requirements, architecture and "
                  "system testing. Construction comes to 6,200 hours, a share of "
                  "31/60 ≈ 51.7%, and coding and debugging, still the largest entry, to "
                  "9/40 = 22.5%; six of the eight entries again reach four-fifths. Both "
                  "shares sit inside the book's 30 to 80 percent only because the lesson "
                  "chose the hours so: they are illustrations, not measurements. What the "
                  "lab settles is the arithmetic. What it cannot settle is the marking. The "
                  "<code>c</code> is yours, and a share computed from a wrong classification "
                  "is printed exactly as precisely as one computed from a right one."),
            ("h3", "Exercise"),
            ("ul", [
                "requirements, 40 hours",
                "detailed design, 30 hours",
                "coding, 90 hours",
                "code review, 20 hours",
                "unit testing, 40 hours",
                "system testing, 50 hours",
                "user documentation, 30 hours",
            ]),
            ("p", "A small project logged these seven activities. Mark each one construction "
                  "or not by Section 1.1's lists, then state construction's share of the "
                  "hours as a fraction and as a percentage. Two of the seven deserve a second "
                  "look before you decide. When you have an answer, type the records into the "
                  "lab with a <code>c</code> on the ones you marked; it will check your sum, "
                  "not your marking."),
            ("p", "Construction is what every project does. The next lesson, “Upstream "
                  "Prerequisites”, reads Chapter 3 on what should be settled before it "
                  "starts, and on what a defect made upstream costs when it is found "
                  "downstream."),
        ],
        "lab": ("cckit", {
            "mode": "profile",
            "view": "shares",
            "tag_label": "construction",
            "unit": "hours",
            "preset": "small-project",
            "presets": [
                {"id": "small-project",
                 "label": "A small project, 1,000 hours (illustrative)",
                 "entries": "requirements, 80; architecture, 50; detailed design, 120, c; "
                            "coding and debugging, 320, c; unit testing, 130, c; "
                            "integration, 90, c; system testing, 110; "
                            "planning and management, 100",
                 "expect": {"pfTotal": "1,000", "pfTagged": "33/50 = 66%",
                            "pfTop": "coding and debugging, 8/25 = 32%"}},
                {"id": "large-project",
                 "label": "A larger project, 12,000 hours (illustrative)",
                 "entries": "requirements, 1400; architecture, 1100; detailed design, 1300, c; "
                            "coding and debugging, 2700, c; unit testing, 1000, c; "
                            "integration, 1200, c; system testing, 2100; "
                            "planning and management, 1200",
                 "expect": {"pfTotal": "12,000", "pfTagged": "31/60 ≈ 51.7%",
                            "pfTop": "coding and debugging, 9/40 = 22.5%"}},
            ],
            "panel_title": "Construction's share of a project's hours",
            "panel_intro": (
                "Each record is an activity, its hours and, for the activities you mark as "
                "construction by Section 1.1's list, a c. The lab adds and divides; the "
                "marking is yours. Figures: the presets' hours are illustrative, chosen by the "
                "lesson."
            ),
        }),
        "steps_title": "Computing construction's share",
        "steps_intro": "Five steps, the last of them on a week of your own.",
        "steps": [
            ("List the activities",
             "Write down each activity the project spent time on, with its hours, under the "
             "project's own names. The marking comes next."),
            ("Mark the construction ones",
             "By Section 1.1, construction is detailed design, coding and debugging, "
             "construction planning, unit testing, integration and integration testing, and "
             "its tasks include reviewing teammates' code. Requirements, architecture, system "
             "testing, management and maintenance are not construction."),
            ("Add and divide",
             "Add the construction hours, add all the hours, and divide the first by the "
             "second. Write the share as a reduced fraction and as a percentage."),
            ("Read the share as one project's",
             "Set it beside the book's 30 to 80 percent, a synthesis over other people's "
             "projects of many sizes. A share outside the range is a reason to look again at "
             "the marking and the hours, not a verdict on the project."),
            ("Do it for your own week",
             "Take last week's calendar, mark each block construction or not by Section 1.1's "
             "list, and paste the blocks into the lab as `name, hours, c` records, with the "
             "`c` only on construction. Note the share the lab prints, and write one sentence "
             "on the block you found hardest to mark and why."),
        ],
        "worked": {
            "title": "Construction's share of the small project",
            "intro": [
                "The <code>small-project</code> preset has eight activities and 1,000 hours. "
                "Four of them are construction by Section 1.1's list: detailed design, coding "
                "and debugging, unit testing and integration.",
            ],
            "lines": [
                "construction: 120 + 320 + 130 + 90 is 660 hours",
                "all hours: 80 + 50 + 660 + 110 + 100 is 1000",
                "share: 660 / 1000 is 33/50, or 66 per cent",
                "largest: coding and debugging, 320 / 1000 is 8/25",
            ],
            "after": [
                "Two-thirds of the hours are construction, and coding and debugging, the "
                "largest single entry, is less than half of that. Requirements, architecture, "
                "system testing and planning make up the other third, and none of it is "
                "counted, because none of it is on Section 1.1's list.",
            ],
        },
        "quiz_title": "Construction and its metaphors",
        "quiz": [
            {"q": "In the lesson's exercise, a small project logged 300 hours over seven "
                  "activities. Marking by Section 1.1's lists, what share of the hours is "
                  "construction?",
             "a": ["90/300, or 30 percent", "160/300, about 53.3 percent",
                   "180/300, that is 3/5, or 60 percent", "230/300, about 76.7 percent"],
             "c": 2,
             "why": "Construction is detailed design (30), coding (90), code review (20) and "
                    "unit testing (40): 180 of 300 hours, 3/5 or 60 percent. Code review is "
                    "construction because Section 1.1 lists reviewing teammates' code among "
                    "its tasks; requirements, system testing and user documentation are not. "
                    "Counting coding alone gives 90, 30 percent, the view that construction is "
                    "only typing; leaving out code review gives 160; adding system testing "
                    "gives 230."},
            {"q": "Which of these activities does Section 1.1 place outside construction?",
             "a": ["Integration testing", "Detailed design", "System testing",
                   "Unit testing"],
             "c": 2,
             "why": "System testing, independent testing of the whole system, is done after "
                    "construction to check it, and Section 1.1 lists it with requirements, "
                    "architecture, management and maintenance as outside. Detailed design, "
                    "unit testing and integration testing are all inside construction as the "
                    "book uses the word."},
            {"q": "What does Section 2.3 say about the farming metaphor, plant a little and "
                  "grow a little?",
             "a": ["It describes a good technique, doing a little at a time, with a poor "
                   "image that suggests you have no direct control over the software",
                   "It is the book's preferred picture of incremental development",
                   "It is adequate for one person's work and small projects only",
                   "It shows that incremental development is a mistake"],
             "c": 0,
             "why": "McConnell keeps the technique and rejects the image: the farming "
                    "metaphor is hard to extend past doing a little at a time, and it implies "
                    "a lack of control. His preferred image for incremental development is "
                    "accretion, the oyster's pearl. Adequate only for small work is what he "
                    "says of the writing metaphor, and he calls incremental development one "
                    "of the most powerful concepts available."},
            {"q": "What is the book's figure, in Section 1.2, for construction's share of a "
                  "project's time?",
             "a": ["About 10 to 20 percent", "30 to 80 percent, depending on the size of "
                   "the project", "Two-thirds on every project", "At least 90 percent"],
             "c": 1,
             "why": "Section 1.2 gives 30 to 80 percent of the total time, depending on size, "
                    "as the book's synthesis of other projects' data; Section 27.5 breaks it "
                    "down by size. Two-thirds is the share on this lesson's illustration, "
                    "chosen to fall in the range. About 10 to 20 percent is the effort "
                    "Chapter 3 says a well-run project spends upstream, not on construction."},
        ],
        "mistakes": [
            ("Writing software as writing a letter",
             "The view that a program is written like a letter, sat down to and written "
             "start to finish, and thrown away and begun again if it comes out wrong. Section "
             "2.3 is aimed at exactly this picture, and finds it adequate only for one "
             "person's work or a small project: software is written by many people, changed "
             "for years after release and rarely finished, and on a large system throwing "
             "one away is the most expensive way to learn. The chapter's answer is the "
             "building and accretion metaphors: plan in proportion to what is being built, "
             "and grow a running system a piece at a time. Brooks, whose line about throwing "
             "one away McConnell quotes against it, had moved to incremental development "
             "himself by 1995."),
            ("Thinking construction is typing in a finished design",
             "Coding in the sense of transcription is the picture Section 1.1 refuses: "
             "construction includes detailed design, debugging, unit and integration "
             "testing, integration and reviewing others' code, and McConnell drops the word "
             "coding because it suggests something mechanical. On the lesson's "
             "illustration, the construction activities come to two-thirds of the hours, and "
             "coding and debugging alone to less than half of those."),
            ("Choosing the one right metaphor",
             "Section 2.1 argues that metaphors improve from worse to better rather than "
             "being right or wrong, and Section 2.3 ends by saying that metaphors, being "
             "heuristics, are not mutually exclusive: you can think with building and "
             "accretion at once, and with writing when it helps. Section 2.2 adds that no "
             "line of code can violate a metaphor. A metaphor is a way of looking, so you "
             "keep several."),
        ],
        "standard": (
            "Finish when you can mark a project's activities by Section 1.1's lists and "
            "compute construction's share.",
            "Given seven activities with their hours, mark the construction ones by Section "
            "1.1's lists and state their share of the hours as a fraction and as a "
            "percentage, without the lab."
        ),
        "note": (
            "The lab adds hours and divides; the hours in its presets are the lesson's, and "
            "the 30 to 80 percent is the book's synthesis of other people's projects, which "
            "your own calendar can test. Nothing in the lab decides whether an activity is "
            "construction: that is a reading of Section 1.1, and on a real calendar some "
            "blocks are honestly both. Nor can it say which metaphor is better; Chapter 2's "
            "case for building and accretion is an argument from what each picture leads "
            "you to expect, and the book's later chapters are where it is tested."
        ),
    },
    # ---------------------------------------------------------------- 02
    # McConnell Chapter 3, pp. 23-60: section 3.1 (p. 24; modern projects
    # p. 25; causes of incomplete preparation pp. 25-27, the WISCA or WIMP
    # syndrome p. 26; the three appeals pp. 27-30; Table 3-1 p. 29), 3.2
    # (p. 31; Table 3-2 pp. 31-32; iterative approaches pp. 33-34, Tables
    # 3-3 and 3-4 illustrative; choosing pp. 35-36), 3.3 (p. 36), 3.4 (p. 38;
    # the post-release multiplier on smaller projects p. 39; the myth of
    # stable requirements pp. 39-40; handling changes pp. 40-41), 3.5
    # (p. 43; architecture errors p. 44), 3.6 (p. 55).
    # Quotations: p. 59, 21 words (the opening); p. 26, 5 words. Total 26,
    # cc_quotes.py OK.
    # F3, p. 29 (and p. 39): Table 3-1's cells. F30, p. 55: 10 to 20 percent
    # of effort, 20 to 30 percent of schedule upstream.
    {
        "slug": "upstream-prerequisites",
        "title": "Upstream Prerequisites",
        "module": "Chapter 3 · Upstream Prerequisites",
        "one_line": "Find a defect near the phase it was made in: by the book's table a requirements defect found after release costs ten to a hundred times one found in requirements, and iteration lowers that cost without removing it.",
        "summary": (
            "Chapter 3 argues that some of a project's success is decided before construction "
            "begins, and that the goal of preparing is to reduce risk. It backs the argument "
            "with a table of what a defect costs to fix by the phase it was made in and the "
            "phase it was found in, and qualifies it by the kind of software and by iterative "
            "and sequential approaches. Price a set of defects by the table, against the cost "
            "had each been found where it was made."
        ),
        "key": [
            "upstream, the goal is risk reduction",
            "fix a defect near where it was made",
            "late cost: count times the table cell",
            "ratio: late cost / early cost",
            "upstream: 10 to 20 per cent of effort",
            "iteration lowers the cost, not to zero",
        ],
        "key_label": "Chapter 3 in six lines",
        "concepts_intro": (
            "Chapter 3 is the longest chapter in Part I, and most of it is a way of telling "
            "whether the work before construction has been done. Three ideas hold it together."
        ),
        "concepts": [
            ("Prerequisites",
             "The work construction depends on: a problem definition, requirements and an "
             "architecture. The chapter does not teach how to produce them; it says how to "
             "tell whether they are good enough to build on, and what to do when they are "
             "not."),
            ("The cost of a late fix",
             "The book's Table 3-1 gives the relative cost of fixing a defect by the phase it "
             "was introduced in and the phase it was found in. Found in the phase it was "
             "made, a defect costs 1; a requirements defect found after release costs 10 to "
             "100. The figures are averages from other people's projects."),
            ("Iterative and sequential",
             "A sequential project finishes each activity before the next; an iterative one "
             "interleaves requirements, architecture, construction and testing. The chapter "
             "says iteration lowers the cost of thin upstream work and spreads it out, but "
             "does not remove it, and that the right balance depends on the kind of software."),
        ],
        "read_title": "The key point first, then the chapter section by section",
        "read_intro": (
            "The quotation is the chapter's first key point. The lesson follows the six "
            "sections in order and then prices a set of defects by the chapter's table."
        ),
        "body": [
            ("p", "<strong>Chapter 3, p. 59.</strong> &ldquo;The overarching goal of preparing "
                  "for construction is risk reduction. Be sure your preparation activities "
                  "are reducing risks, not increasing them.&rdquo; It is the first of the "
                  "chapter's key points, and the sentence to hold on to through nearly forty "
                  "pages of argument for doing work before construction. Read Chapter 3, "
                  "pages 23 to 60, in your own copy first; the lesson goes back through it "
                  "section by section."),
            ("p", "You have probably fixed a defect that was not a coding mistake at all. The "
                  "routine did exactly what the specification said, the tests passed, and the "
                  "specification was wrong; by the time a customer noticed, the wrong rule "
                  "was in the schema, three screens and a report. Chapter 3 is about that "
                  "kind of defect, and its carpenter's title, measure twice and cut once, is "
                  "its argument in four words: some of a project's success or failure is "
                  "settled before construction begins, and on a poor foundation the best "
                  "construction can do is limit the damage. Section 3.1 (p. 24) puts it as a "
                  "question of where a project puts its attention to quality. At the end, "
                  "that means system testing; in the middle, construction practice; at the "
                  "beginning, planning, requirements and design. Testing cannot find that you "
                  "built the wrong product, McConnell says: start from the design of a Pontiac "
                  "Aztek, test it as much as you like, and it will not turn into a "
                  "Rolls-Royce."),
            ("p", "The section takes on the claim that upstream work, architecture, design and "
                  "project planning, is not useful on modern projects. McConnell's reply is "
                  "that the claim is not well supported by data, that its holders tend to "
                  "show prerequisites done badly, and that the purpose of preparation is to "
                  "reduce risk: clear the major risks early, and the commonest risks in "
                  "software are poor requirements and poor planning. He gives three reasons "
                  "projects skip preparation anyway. The people assigned to it may lack the "
                  "skills; programmers want to start coding; and managers want to see code, "
                  "a condition the book names the WISCA syndrome, &ldquo;Why Isn’t Sam Coding "
                  "Anything?&rdquo;"),
            # F3, p. 29; the smaller-projects remark is p. 39 (Boehm and Turner 2004)
            ("p", "Then comes what the chapter calls its utterly compelling and foolproof "
                  "argument, in three appeals. The appeal to logic is to know what you are "
                  "building before you build it. The appeal to analogy is a food chain: the "
                  "architect consumes the requirements, the designer the architecture and the "
                  "coder the design, so contaminated requirements contaminate everything "
                  "downstream. The appeal to data is the one the lab computes. Find a defect "
                  "as close as possible to the time it was introduced, the principle runs, "
                  "because it does more damage the longer it stays, and a defect made "
                  "upstream tends to have broader effects. Table 3-1 (p. 29) gives the "
                  "relative cost of a fix by the phase a defect was introduced in and the "
                  "phase it was found in. Its figures are the book's synthesis of other "
                  "people's data, after Fagan 1976, Humphrey, Snyder and Willis 1991, Boehm "
                  "and Turner 2004 and others: averages over projects you did not work on. A "
                  "requirements defect costs 1 to fix in requirements, 3 in architecture, 5 "
                  "to 10 in construction, 10 in system test and 10 to 100 after release, and "
                  "the book's own example is an architecture defect that costs $1,000 to fix "
                  "while the architecture is being written and $15,000 in system test. On "
                  "page 39 it adds that on smaller projects, with lower administrative costs, "
                  "the post-release multiplier is closer to 5 to 10 than to 100."),
            ("p", "Section 3.2 (p. 31) is the chapter's qualification of itself, and the part "
                  "most easily skipped. Projects differ, and so does the balance between "
                  "preparation and construction. The book sorts software into business "
                  "systems, mission-critical systems and embedded life-critical systems, and "
                  "its table of typical good practices runs from informal, highly iterative "
                  "work for the first to formal, more sequential work for the last, where "
                  "stable requirements are part of what makes very high reliability possible. "
                  "An <em>iterative</em> approach interleaves planning, requirements and "
                  "architecture with construction and testing; a <em>sequential</em> one "
                  "finishes each before starting the next. Some writers, McConnell says, hold "
                  "that iterative projects hardly need prerequisites, and he calls that view "
                  "misinformed. Iteration lowers the cost of thin upstream work, because "
                  "defects are found nearer the time they were made, and it spreads the cost "
                  "over the project in small instalments instead of one bill at the end; it "
                  "does not remove it. In his illustrative tables the iterative project that "
                  "attends to prerequisites is the cheapest of the four."),
            ("p", "The section ends on a choice, not a rule. A more sequential approach suits "
                  "stable requirements, a well-understood design, a team that knows the "
                  "application area, low risk and a high cost of later change; a more "
                  "iterative one suits the opposite of each. Most projects are neither wholly "
                  "one nor the other, the book says, and most find value in settling at least "
                  "the most critical requirements and architecture early. Given what "
                  "software is like, McConnell judges iterative approaches the more useful far "
                  "more often. A project can go wrong in either direction: by doing too little "
                  "upstream and absorbing a stream of destabilising changes, or by doing too "
                  "much and holding to plans that later discoveries have overturned."),
            ("p", "Sections 3.3 to 3.5 (pp. 36&ndash;55) take the prerequisites one at a "
                  "time, and each says how to recognise whether one has been done, not how to "
                  "do it. A <em>problem definition</em> states the problem without reference "
                  "to a solution and in the user's language: a company that cannot keep up "
                  "with its orders has a problem, while a company that needs its data-entry "
                  "system optimised has already chosen a solution. <em>Requirements</em> say in "
                  "detail what the system is to do; written down, they let the user rather "
                  "than the programmer decide what it does, and they settle arguments. But "
                  "stable requirements, McConnell says, are a myth: customers understand what "
                  "they need better as the work goes on, and holding to the requirements as "
                  "first written amounts to refusing to respond to them. His advice for "
                  "changes during construction is a list: check the requirements and back up "
                  "if they are not good enough, make sure everyone knows what a change costs, "
                  "set up a change-control procedure, use approaches that accommodate change, "
                  "keep the business case in view, and, if nothing else works, consider "
                  "cancelling the project."),
            # F30, p. 55
            ("p", "<em>Architecture</em>, the high-level design that holds the detailed design "
                  "together, decides the system's conceptual integrity, and Section 3.5's "
                  "long account of what a good one covers, from program organisation, major "
                  "classes and data design to error processing and buy-or-build decisions, "
                  "ends in a checklist. Architectural errors, the book says, cost about as "
                  "much to fix as requirements errors, which is more than coding errors cost. "
                  "Section 3.6 (p. 55) then puts a figure on the whole: a well-run project "
                  "spends about 10 to 20 percent of its effort and about 20 to 30 percent of "
                  "its schedule on requirements, architecture and up-front planning, after "
                  "McConnell 1998 and Kruchten 2000, figures that leave out detailed design "
                  "because that is part of construction. Where requirements are unstable, the "
                  "section advises treating requirements work as a project of its own and "
                  "estimating the rest when it is done."),
            ("p", "Table 3-1 is arithmetic waiting to be done, and the lab does it. You give "
                  "it defects as records: the phase each was introduced in, the phase it was "
                  "found in, and how many, with the phases written <code>req</code>, "
                  "<code>arch</code>, <code>cons</code>, <code>test</code> and "
                  "<code>post</code> for requirements, architecture, construction, system "
                  "test and after release. It multiplies each count by the table's cell, adds "
                  "the low ends and the high ends, and sets the total beside what the same "
                  "defects would have cost had each been found in the phase it was made, "
                  "where every cell is 1. On the <code>found-late</code> preset, 10 "
                  "requirements defects found in system test cost 10 × 10 = 100, 5 "
                  "architecture defects found after release cost 5 × 25 to 5 × 100, that is "
                  "125 to 500, and 20 construction defects found in system test cost "
                  "20 × 10 = 200. The cost tile reads 425–800, in units of the cost of a fix "
                  "in the phase of origin; the early-cost tile reads 35, one unit for each "
                  "defect; and the ratio tile divides the two, 85/7 ≈ 12.1× to "
                  "160/7 ≈ 22.9×."),
            ("p", "<code>found-early</code> is the same 35 defects, each caught where it was "
                  "made: 35, 35 and a ratio of 1×. <code>requirements-late</code> is ten "
                  "requirements defects found after release: 100–1,000 against 10, a ratio "
                  "of 10× to 100×, the widest cell in the table. Every figure here is the "
                  "lab's arithmetic on the table's averages, and the range is the table's own "
                  "spread carried through. Your project's multipliers may be smaller or "
                  "larger; page 39's remark about small projects says they are often smaller "
                  "after release. What the lab cannot do is tell you which phase a defect was "
                  "introduced in. That is a judgement made by reading the defect, and it is "
                  "the hard part of using the table at all."),
            ("h3", "Exercise"),
            ("ul", [
                "Introduced in: requirements (<code>req</code>)",
                "Found in: after release (<code>post</code>)",
                "How many: 8",
            ]),
            ("p", "Eight defects in a released system turn out, on reading, to trace back to "
                  "the requirements. Using Table 3-1's cells as this lesson gives them, find "
                  "the total cost range in the table's units, the cost had each been caught "
                  "in requirements, and the ratio between the two. Then enter the record "
                  "<code>req, post, 8</code> in the lab to check your arithmetic."),
            ("p", "The chapter is about what should be in place before construction. The next "
                  "lesson, “Key Construction Decisions”, reads Chapter 4 on what the "
                  "programmers themselves decide at its start: the language, the conventions "
                  "and the practices."),
        ],
        "lab": ("cckit", {
            "mode": "defects",
            "view": "cost",
            "table": COST_TABLE,
            "preset": "found-late",
            "presets": [
                {"id": "found-late",
                 "label": "35 defects, most found late (illustrative counts)",
                 "defects": "req, test, 10; arch, post, 5; cons, test, 20",
                 "expect": {"dfCost": "425–800", "dfEarly": "35",
                            "dfRatio": "85/7 ≈ 12.1× to 160/7 ≈ 22.9×"}},
                {"id": "found-early",
                 "label": "The same 35 defects, each found where it was made",
                 "defects": "req, req, 10; arch, arch, 5; cons, cons, 20",
                 "expect": {"dfCost": "35", "dfEarly": "35", "dfRatio": "1×"}},
                {"id": "requirements-late",
                 "label": "10 requirements defects found after release",
                 "defects": "req, post, 10",
                 "expect": {"dfCost": "100–1,000", "dfEarly": "10", "dfRatio": "10× to 100×"}},
            ],
            "panel_title": "What a late fix costs, by the book's table",
            "panel_intro": (
                "Each record is a phase a defect was introduced in, the phase it was found "
                "in, and a count. The lab multiplies each count by the table's relative cost "
                "and compares the total with the cost had each defect been found where it "
                "was made. Figures: Table 3-1 as the lesson gives it, the book's synthesis after "
                "Fagan 1976 and others, an average over other people's projects."
            ),
        }),
        "steps_title": "Pricing a set of defects by the table",
        "steps_intro": "Five steps, the last of them on defects of your own.",
        "steps": [
            ("Place each defect",
             "For each defect, write the phase it was introduced in and the phase it was "
             "found in: requirements, architecture, construction, system test or after "
             "release. Group defects with the same pair and count them."),
            ("Look up each cell",
             "Find each pair's cell in Table 3-1. Some cells are a single figure and some a "
             "range; keep the range."),
            ("Multiply and add",
             "Multiply each count by its cell and add, the low ends together and the high "
             "ends together. The result is in units of the cost of a fix in the phase of "
             "origin."),
            ("Divide by the early cost",
             "The early cost is the number of defects, since each would have cost 1. Divide "
             "the low and high totals by it for the ratio, and remember that the ratio is "
             "arithmetic on other people's averages."),
            ("Price your own last five",
             "Take the last five defects in your own tracker. For each, write the phase it "
             "was introduced in and the phase it was found in, enter them in the lab as "
             "`introduced, detected, count` records, note the cost range and the ratio, and "
             "write one sentence on the defect whose phase of origin you were least sure of."),
        ],
        "worked": {
            "title": "Thirty-five defects, most found late",
            "intro": [
                "The <code>found-late</code> preset: 10 requirements defects found in system "
                "test, 5 architecture defects found after release, and 20 construction defects "
                "found in system test. The cells are 10, 25 to 100, and 10.",
            ],
            "lines": [
                "requirements, found in test: 10 × 10 is 100",
                "architecture, found after release: 5 × 25 to 5 × 100",
                "that is 125 to 500",
                "construction, found in test: 20 × 10 is 200",
                "late cost: 425 to 800 units",
                "early cost: 10 + 5 + 20 is 35 units",
                "ratio: 425/35 to 800/35, about 12.1× to 22.9×",
            ],
            "after": [
                "Five architecture defects account for most of the spread, because their cell "
                "after release is the widest. Found where each was made, the same defects "
                "would have cost 35 units: the table's averages put the late bill at twelve to "
                "twenty-three times that.",
            ],
        },
        "quiz_title": "Prerequisites and the cost of a late fix",
        "quiz": [
            {"q": "In the lesson's exercise, eight requirements defects are found after "
                  "release. By Table 3-1 as the lesson gives it, what do they cost, against "
                  "the 8 units they would have cost if caught in requirements?",
             "a": ["40 to 80 units, a ratio of 5× to 10×",
                   "80 units, a ratio of 10×",
                   "80 to 800 units, a ratio of 10× to 100×",
                   "8 to 80 units, a ratio of 1× to 10×"],
             "c": 2,
             "why": "The cell for a requirements defect found after release is 10 to 100, so "
                    "8 × 10 = 80 to 8 × 100 = 800 units, against 8 × 1 = 8 had each been "
                    "caught in requirements: a ratio of 10× to 100×. 40 to 80 uses the "
                    "construction cell (5 to 10) and 80 the system-test cell (10). The "
                    "figures are the book's synthesis after Fagan 1976 and others (p. 29), "
                    "and it notes on p. 39 that on smaller projects the post-release multiplier "
                    "is closer to 5 to 10."},
            {"q": "By Table 3-1, a defect introduced in the architecture and found in system "
                  "test costs how many times as much to fix as one found while the "
                  "architecture is being written?",
             "a": ["3", "10", "15", "25 to 100"],
             "c": 2,
             "why": "The cell is 15: the book's own example is an architecture defect that "
                    "costs $1,000 to fix during architecture and $15,000 in system test. 10 is "
                    "the cell for one found in construction, 25 to 100 for one found after "
                    "release, and 3 is a requirements defect found in architecture."},
            {"q": "What does Section 3.2 say about an iterative project that does little "
                  "upstream work?",
             "a": ["It needs no prerequisites, because each iteration finds its own defects",
                   "It pays less for late defects, and pays in smaller instalments, but the "
                   "cost is not removed",
                   "It should specify all its requirements first, as a sequential project does",
                   "It pays the after-release multiplier on every defect"],
             "c": 1,
             "why": "Iteration finds defects nearer the time they were made and spreads the "
                    "rework over the project, so it lowers and smooths the cost; the defects "
                    "are still found late in each iteration, so the cost is not removed. "
                    "McConnell calls the view that iterative projects need no prerequisites "
                    "misinformed, and he does not ask them to specify everything first: most "
                    "projects, he says, should settle at least the most critical requirements "
                    "and architecture early."},
            {"q": "What share of its effort and schedule does Section 3.6 say a well-run "
                  "project spends on requirements, architecture and up-front planning?",
             "a": ["About 10 to 20 percent of effort and 20 to 30 percent of schedule",
                   "About 20 to 30 percent of effort and 10 to 20 percent of schedule",
                   "30 to 80 percent of the total time",
                   "About half of both"],
             "c": 0,
             "why": "Section 3.6 (p. 55) gives about 10 to 20 percent of effort and about 20 "
                    "to 30 percent of schedule, after McConnell 1998 and Kruchten 2000, not "
                    "counting detailed design, which is part of construction. The second "
                    "option swaps the two. 30 to 80 percent is Chapter 1's figure for "
                    "construction's share."},
        ],
        "mistakes": [
            ("Reading the cost table as a rule to finish requirements first",
             "The table is easily read as saying every project should finish its "
             "requirements before any coding starts. Section 3.2 argues the opposite for most "
             "kinds of project. The table is an argument for finding defects close to where "
             "they were made, and an iterative project does that by doing a little of each "
             "activity at a time; McConnell says iterative approaches are the more useful far "
             "more often, and asks only that the most critical requirements and "
             "architecture be settled early. On the lesson's illustration, catching the same "
             "35 defects where each was made costs 35 units against 425 to 800, and that can "
             "happen in any order of work that finds defects early."),
            ("Leaving quality to testing at the end",
             "Section 3.1's point is that testing is one part of quality assurance and not "
             "the most influential: testing cannot find that the product is the wrong one, "
             "or the right one built the wrong way. Those flaws have to be worked out before "
             "construction. By Table 3-1, a requirements defect left for system test costs "
             "10 times what it would have in requirements."),
            ("Writing a problem definition as a solution",
             "A problem definition, Section 3.3 says, states the problem in the user's "
             "language and without reference to a solution. A statement that the company "
             "needs its data-entry system optimised has already chosen the answer, and may "
             "have chosen the wrong one: the book's example is an annual profit report that "
             "needed a calculator and four quarterly figures, not a program."),
        ],
        "standard": (
            "Finish when you can price a set of defects by the table and state the ratio.",
            "Given defects by the phase each was introduced in and the phase it was found "
            "in, and Table 3-1's cells, compute the total cost range and its ratio to the "
            "cost of finding each defect where it was made, without the lab."
        ),
        "note": (
            "The lab multiplies the table's cells; it cannot tell you whether your project's "
            "costs rise the way the table's do, and the table is an average over other "
            "people's projects, many of them large, from 1976 to 2004. This lesson is the "
            "course's one place for the later view. The agile movement, which was growing as "
            "the book was written and which Kent Beck's <em>Extreme Programming "
            "Explained</em> (2000), listed in the chapter's further reading, helped to start, "
            "holds that much of what Chapter 3 settles upstream is better discovered by "
            "building and showing working software, and that practices which make change "
            "cheap, such as small releases, automated tests and continual refactoring, "
            "flatten the rise the table records. The book's position, at its strength, is "
            "Section 3.2's: iterate, usually, and still settle the most critical requirements "
            "and architecture early, because iteration lowers the cost of a late defect "
            "without removing it. Which describes your project is a question about your own "
            "defects, and neither the book nor this lab settles it."
        ),
    },
    # ---------------------------------------------------------------- 03
    # McConnell Chapter 4, pp. 61-70: section 4.1 (p. 61; productivity and
    # Table 4-1 p. 62; Sapir-Whorf and the Fortran story p. 63; language
    # descriptions pp. 63-66), 4.2 (p. 66), 4.3 (pp. 66-69; Gries and the
    # Visual Basic convention p. 68), 4.4 (pp. 69-70).
    # Quotations: p. 70, 32 words (the opening); p. 63, 2 words. Total 34,
    # cc_quotes.py OK.
    # F4, p. 62: Table 4-1's ratios. F5, p. 62: about 30 percent more
    # productive with three or more years in the language (Cocomo II).
    {
        "slug": "key-construction-decisions",
        "title": "Key Construction Decisions",
        "module": "Chapter 4 · Key Construction Decisions",
        "one_line": "Before construction starts, choose the language, the conventions and the practices, and where the language lacks something you need, supply it by convention: program into the language, not in it.",
        "summary": (
            "Chapter 4 is about the decisions programmers and technical leads take themselves "
            "before construction: the language, the conventions, where the project stands on "
            "the technology wave, and which construction practices to use. Convert a size in "
            "statements of C by the book's ratio and say what the ratio does not measure, and "
            "supply in Java, by convention, a facility the language lacks."
        ),
        "key": [
            "program into a language, not in it",
            "ratio: C statements per statement",
            "statements: C size / ratio",
            "a ratio counts statements, not hours",
            "set conventions before the code",
            "know where you are on the wave",
        ],
        "key_label": "Chapter 4 in six lines",
        "concepts_intro": (
            "Chapter 4 is ten pages long and makes four decisions explicit. Three ideas "
            "carry it."
        ),
        "concepts": [
            ("A statement ratio",
             "The book's Table 4-1 gives, for each of several languages, how many statements "
             "of C one statement of that language is worth on average: 2.5 for Java, 6 for "
             "Python. A size in C divided by the ratio is the size of the same work in that "
             "language. It counts statements and nothing else."),
            ("A convention",
             "An agreement among programmers about how code is written, which the compiler "
             "does not enforce: names, layout, comments, or a shape every routine of a kind "
             "takes. Section 4.2 says conventions belong before construction, because they "
             "are nearly impossible to retrofit."),
            ("Programming into a language",
             "David Gries's distinction, which the book adopts: programming in a language "
             "limits your thinking to what it directly supports, while programming into it "
             "means deciding what you want to express first and then supplying, by "
             "convention if need be, what the language lacks."),
        ],
        "read_title": "The key point first, then the chapter's four decisions",
        "read_intro": (
            "The quotation is the last of the chapter's key points. The lesson takes the four "
            "sections in order, writes one convention in Java, and converts a size by the "
            "chapter's table."
        ),
        "body": [
            ("p", "<strong>Chapter 4, p. 70.</strong> &ldquo;Ask yourself whether the "
                  "programming practices you’re using are a response to the programming "
                  "language you’re using or controlled by it. Remember to program into the "
                  "language, rather than programming in it.&rdquo; It is the last of the "
                  "chapter's key points, and the idea the chapter calls critical to "
                  "understanding the whole book. Chapter 4 is short, pages 61 to 70; read it "
                  "in your own copy first."),
            ("p", "Chapter 3 was about preparations a programmer may have had no say in. "
                  "Chapter 4 asks which preparations are yours: the decisions individual "
                  "programmers and technical leads take, directly or indirectly, before "
                  "construction starts, or in the book's image, which tools go on your belt "
                  "and how you load the truck before you drive to the site. It names four: "
                  "the language, the programming conventions, where you stand on the "
                  "technology wave, and which of the many good construction practices you "
                  "will use."),
            # F5, p. 62; F4, p. 62
            ("p", "Section 4.1 (p. 61) begins with the language, since you will be immersed in "
                  "it from the start of construction to the end, and reports two findings "
                  "about productivity. Programmers are more productive in a language they "
                  "know: the Cocomo II estimation model's data, as the book gives it after "
                  "Boehm and others (2000), puts programmers with three or more years in a "
                  "language about 30 percent ahead of equally experienced programmers new to "
                  "it. And higher-level languages say more per line. Table 4-1 (p. 62), after "
                  "Jones 1998, Boehm 2000 and Prechelt 2000, gives the number of statements "
                  "of C that one statement of a language does the work of: 2.5 for C++ and "
                  "Java, 2 for Fortran 95, 4.5 for Visual Basic, and 6 for Perl, Python and "
                  "Smalltalk. The ratios are averages over the programs those authors "
                  "studied, not constants of the languages."),
            ("p", "The section's second argument is about thought rather than output. It "
                  "borrows the Sapir-Whorf hypothesis, that the words a language offers shape "
                  "the thoughts its speakers can form, and suggests that programmers may be "
                  "shaped the same way by theirs. Its evidence is a story the industry has "
                  "told for years: a team of Fortran programmers moves to C++ and writes code "
                  "that compiles as C++ but is really &ldquo;disguised Fortran&rdquo;, with "
                  "Fortran's gotos and global data and none of C++'s classes. The section "
                  "ends with a paragraph or two on each of the languages in wide use in 2004, from "
                  "Ada to Visual Basic, which this lesson leaves to your copy."),
            ("p", "Section 4.2 (p. 66) is about programming conventions: for names, layout, "
                  "comments and the like. A program's low-level detail should bear out its "
                  "architecture, McConnell argues, as the parts of a painting bear out its "
                  "design; a painting that is partly classical, partly impressionist and "
                  "partly cubist is a collage, however faithfully it follows the plan. "
                  "Arbitrary variations of style make the reader work for nothing, and "
                  "conventions remove them, leaving attention for the variations that matter. "
                  "The decision belongs before construction because conventions work at a "
                  "level of detail that is nearly impossible to retrofit into code already "
                  "written."),
            ("p", "Section 4.3 (p. 66) asks where you stand on the technology wave. Late in a "
                  "wave, as Web programming was in the mid-2000s, the languages are mature, "
                  "the tools integrated and documented and the compilers nearly free of bugs, "
                  "so a programmer's day goes on new function. Early in a wave, as Web "
                  "programming was in the mid-1990s, the languages are buggy and poorly "
                  "documented, debuggers may not exist, and much of the day goes on finding "
                  "out how the tools behave. McConnell does not advise avoiding the early "
                  "part of a wave, where some of the most innovative programs were written; "
                  "he says the book's practices help even more there."),
            ("p", "Here the chapter turns to David Gries, and to a distinction from his "
                  "<em>The Science of Programming</em> (1981), as the book cites it, on "
                  "which the key point rests. "
                  "Programmers who program <em>in</em> a language limit their thoughts to the "
                  "constructs it directly supports. Programmers who program <em>into</em> a "
                  "language first decide what they want to express, and then work out how to "
                  "express it with the tools they have. McConnell's example is his own. In "
                  "early Visual Basic he wanted business logic, user interface and database "
                  "code kept apart, and the language offered no way to do it, so he adopted a "
                  "convention: a form could only read its data from the database and write it "
                  "back, it exposed one public routine, which said whether the form had saved "
                  "its data, and everything else, validity checks included, lived in an "
                  "associated module. The language encouraged the opposite. The convention, "
                  "he says, kept the project intellectually manageable."),
            ("p", "Section 4.4 (p. 69) closes the chapter with the practices themselves. "
                  "There are more good ones than any project can use, and the book's point is "
                  "to choose them consciously: some projects pair-program and write tests "
                  "first, others work alone and hold formal inspections, and either "
                  "combination can work. Its checklist of major construction practices asks, "
                  "among other things, how much design will be done up front and how much at "
                  "the keyboard, whether programmers will write test cases before the code, "
                  "and whether they will review each other's code."),
            ("p", "Programming into a language is easiest to see in a small case. Java has no "
                  "default values for parameters: in C++ or Python a declaration can say "
                  "that a missing argument means 3, and in Java it cannot. The convention "
                  "below supplies the facility. The full version of `send` holds the logic, "
                  "the shorter version does nothing but forward to it, and the default is "
                  "written once, as a named constant. `transmit` stands for some routine "
                  "that sends the message once and reports whether it arrived."),
            ("code", SEND_WITH_DEFAULT.split("\n")),
            ("p", "Line 6 is the whole convention: `send(message)` passes `DEFAULT_RETRIES` "
                  "from line 3 to the two-argument version on lines 9 to 16, which tries up "
                  "to `retries` times and returns `true` on the first attempt that arrives. "
                  "Nothing in Java requires this shape. A teammate could give the "
                  "one-argument version a loop of its own, or write a bare 3 into it, and the "
                  "compiler would accept either; the convention holds because the team keeps "
                  "it and reviews for it, which is what it has in common with McConnell's "
                  "Visual Basic forms."),
            # F4, p. 62
            ("p", "The lab does Table 4-1's one sum. Give it a size in statements of C and a "
                  "ratio from the table, and it divides, giving the statements of the other "
                  "language that would do the same work. On the <code>java</code> preset, "
                  "10,000 statements of C at Java's 2.5 come to 4,000 statements of Java. On "
                  "<code>python</code>, at 6, they come to 5000/3 ≈ 1,666.67, and on "
                  "<code>visual-basic</code>, at 4.5, to 20000/9 ≈ 2,222.22; a fraction of a "
                  "statement is the average showing through, not a statement anyone writes. "
                  "The book never turns the ratio into a schedule, and neither does the lab: "
                  "it measures statements, not the time the work takes, not the defects in "
                  "it, and not the gain the book reports from years of experience in a "
                  "language."),
            ("h3", "Exercise"),
            ("ul", [
                "A language with no assertion statement, as Java was before version 1.4.",
                "A language with no enumerated types, as Java was before version 5.",
                "A language with no access control, in which every member of a class is "
                "public.",
            ]),
            ("p", "For each language, write the convention that supplies the missing "
                  "facility: a few lines of Java and a sentence on how they are used for the "
                  "first two, and a sentence for the third. Each answer should be something a "
                  "team can agree on and a reviewer can check. The lab has nothing to say "
                  "about this exercise; the first question of the quiz does."),
            ("p", "That ends the book's first Part. The next course, Creating High-Quality "
                  "Code, opens Part II with “Design Challenges and Complexity”, and with the "
                  "idea the rest of the book is organised around: that managing complexity is "
                  "software's primary technical imperative."),
        ],
        "lab": ("cckit", {
            "mode": "project",
            "view": "language",
            "size": 10000,
            "preset": "java",
            "presets": [
                {"id": "java",
                 "label": "10,000 statements of C, in Java (ratio 2.5)",
                 "ratio": Fraction(5, 2),
                 "expect": {"pjEquivalent": "4,000"}},
                {"id": "python",
                 "label": "10,000 statements of C, in Python (ratio 6)",
                 "ratio": 6,
                 "expect": {"pjEquivalent": "5000/3 ≈ 1,666.67"}},
                {"id": "visual-basic",
                 "label": "10,000 statements of C, in Visual Basic (ratio 4.5)",
                 "ratio": Fraction(9, 2),
                 "expect": {"pjEquivalent": "20000/9 ≈ 2,222.22"}},
            ],
            "panel_title": "The same work in another language, by the book's ratio",
            "panel_intro": (
                "Give a size in statements of C and a ratio from Table 4-1: the lab divides, "
                "giving the statements of the other language that do the same work. Figures: "
                "Table 4-1, the book's, after Jones 1998, Boehm 2000 and Prechelt 2000, an "
                "average over the programs they measured; the size is the lesson's."
            ),
        }),
        "steps_title": "Converting a size, and supplying what a language lacks",
        "steps_intro": "Five steps: three for the table, two for the convention.",
        "steps": [
            ("Find the ratio",
             "Look up the language in Table 4-1: the number of statements of C one of its "
             "statements does the work of."),
            ("Divide",
             "Divide the size in statements of C by the ratio. A fraction in the result is "
             "the average showing through; keep it, and do not round it into a promise."),
            ("Say what the figure leaves out",
             "State that the result counts statements: not hours, not defects, and not the "
             "team's experience in the language, which Section 4.1 treats as a separate "
             "effect."),
            ("Name the facility and its convention",
             "When the language lacks something you want, say what you want to express, then "
             "write the smallest convention that expresses it with what the language has, "
             "and say how a reviewer would see it kept or broken."),
            ("Do it for your own language",
             "Name one facility your own language or framework lacks, write in two or three "
             "sentences, or a few lines of code, the convention your team uses or should use "
             "to supply it, and name one place in your own code where the convention is "
             "kept, broken or missing."),
        ],
        "worked": {
            "title": "10,000 statements of C in three languages",
            "intro": [
                "The three presets take the same size, 10,000 statements of C, and divide by "
                "Table 4-1's ratios for Java, Python and Visual Basic.",
            ],
            "lines": [
                "Java: 10000 / 2.5 is 4000 statements",
                "Python: 10000 / 6 is 5000/3, about 1666.67",
                "Visual Basic: 10000 / 4.5 is 20000/9, about 2222.22",
            ],
            "after": [
                "The same work takes fewer statements the higher the ratio, and that is all "
                "the figures say. None of them is a number of hours, and a team that has used "
                "Python for a month is not, by this table, a team that will finish in a sixth "
                "of the time.",
            ],
        },
        "quiz_title": "Key construction decisions",
        "quiz": [
            {"q": "The lesson's exercise names a language with no assertion statement. "
                  "Programming into that language, which convention supplies one?",
             "a": ["A comment above each line, stating the condition the line assumes",
                   "A routine check(condition, message) that throws when the condition is "
                   "false, called wherever an assertion would go",
                   "Leaving assertions out until a later version of the language adds them",
                   "A try block around the main routine that catches every exception"],
             "c": 1,
             "why": "A routine `check(boolean condition, String message)` that throws when "
                    "the condition is false, called where an assertion would be, does what "
                    "an assertion does. A comment states the condition but checks nothing; "
                    "waiting for the language is programming in it; and catching every "
                    "exception hides failures rather than detecting them. The exercise's other "
                    "two answers: for enumerated types, a class with a private constructor and "
                    "a fixed set of `public static final` instances; for access control, a "
                    "naming convention, such as a leading underscore on any member nobody "
                    "outside the class may use, enforced by review."},
            {"q": "A function takes 9,000 statements of C. By Table 4-1's ratio for Python, "
                  "6, how many statements of Python does the same work?",
             "a": ["1,500", "2,000", "3,600", "54,000"],
             "c": 0,
             "why": "9,000 / 6 = 1,500. Dividing by Visual Basic's 4.5 gives 2,000 and by "
                    "Java's 2.5 gives 3,600; multiplying by 6 instead of dividing gives 54,000. "
                    "The ratio is the book's, after Jones 1998, Boehm 2000 and Prechelt 2000 "
                    "(p. 62)."},
            {"q": "What does a ratio in Table 4-1 measure?",
             "a": ["How many times faster a team finishes in that language than in C",
                   "How many statements of C one statement of the language does the work of",
                   "How many defects a thousand statements of the language contain",
                   "How much more productive a programmer is after three years in the "
                   "language"],
             "c": 1,
             "why": "The table gives statements of C equivalent to one statement of the "
                    "language: Java 2.5, Python 6. It is not a schedule, and the book does not "
                    "turn it into one. Defects per thousand lines are a different table, in "
                    "Chapter 27, and the gain from three years' experience, about 30 percent "
                    "by the Cocomo II data the book cites, is a separate finding on the same "
                    "page."},
            {"q": "In Gries's distinction as Section 4.3 gives it, what do programmers who "
                  "program into a language do?",
             "a": ["Limit their thoughts to the constructs the language directly supports",
                   "Choose the language with the most features for each project",
                   "Avoid any practice the compiler does not enforce",
                   "Decide what they want to express first, then how to express it with "
                   "the language's tools"],
             "c": 3,
             "why": "Programming into a language starts from the thought and supplies what "
                    "the language lacks, by convention if need be, as McConnell did with his "
                    "Visual Basic forms. Limiting your thoughts to what the language supports "
                    "is programming in it, and the chapter's conventions are exactly the "
                    "practices a compiler does not enforce."},
        ],
        "mistakes": [
            ("Thinking a missing keyword means a missing practice",
             "The view that a practice your language has no keyword for is unavailable to "
             "you. Section 4.3 is the refutation: programmers who program into a language "
             "decide what they want to express and supply what the language lacks by "
             "convention, as McConnell kept Visual Basic forms free of business logic when "
             "the language offered no way to separate it. The lesson's `send` does the same "
             "for default arguments, which Java does not have."),
            ("Reading the ratio as a schedule",
             "Table 4-1 says one statement of Python does the work of about six of C, and it "
             "is tempting to read that as six times faster. The table counts statements. It "
             "says nothing about the hours a statement takes, the defects in it or the "
             "team's experience, and the book never turns it into a schedule. On the lesson's "
             "illustration, 10,000 statements of C become 5000/3 ≈ 1,666.67 statements of "
             "Python, and no number of days."),
            ("Leaving conventions for later",
             "Agreeing conventions once the code shows what is needed sounds pragmatic. "
             "Section 4.2 says they work at a level of detail that is nearly impossible to "
             "retrofit into code already written, and so belong among the decisions taken "
             "before construction; the chapter's checklist of construction practices asks "
             "about them among its first questions."),
        ],
        "standard": (
            "Finish when you can convert a size by the table's ratio and supply a missing "
            "facility by convention.",
            "Given a size in statements of C and a ratio from Table 4-1, state the equivalent "
            "statements and what the ratio does not measure; given a facility a language "
            "lacks, write the convention that supplies it, without the lab."
        ),
        "note": (
            "The lab divides one number by another. The ratios are the book's averages over "
            "the programs Jones, Boehm and Prechelt measured, and the size in the presets is "
            "the lesson's. Nothing in the lab can tell whether a convention is kept; that is "
            "done by people reading code, which is why the chapter puts conventions among "
            "the decisions taken before construction rather than among the things a tool "
            "enforces."
        ),
    },
]
