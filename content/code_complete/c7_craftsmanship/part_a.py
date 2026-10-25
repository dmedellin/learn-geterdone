"""Software Craftsmanship, lessons 1-4 -- Code Complete, Part VII (Chapters 31-35).

Every quotation is copied from the second edition (Microsoft Press, 2004),
with its printed page in the comment beside the lesson. Every figure
attributed to the book carries its PLAN §S.2 id and page. The snippets are
written for these lessons (PLAN §D.4); each is one constant, used by the
lesson's code block and by the lab preset that counts it, so the line numbers
the prose names are the lab's.
"""

from fractions import Fraction

# ---------------------------------------------------------------- snippets

# Layout and Style (PLAN §D.4: dangling-else, two-statements, braced, clamp)
DANGLING_ELSE = """void notifyUser(User user) {
    if (user.isActive())
        if (user.wantsEmail())
            sendEmail(user);
    else
        sendLetter(user);
    log(user);
}"""

TWO_STATEMENTS = """void close(Account account) {
    if (account.balance() == 0)
        account.markClosed();
        archive(account);
    log(account);
}"""

BRACED = """void notifyUser(User user) {
    if (user.isActive()) {
        if (user.wantsEmail()) {
            sendEmail(user);
        } else {
            sendLetter(user);
        }
    }
    log(user);
}"""

# The exercise: line 6 is mis-indented, and line 7 is unreachable.
CLAMP = """int clamp(int value, int low, int high) {
    if (value < low)
        return low;
    if (value > high)
        log("clamped");
        return high;
    return value;
}"""

# Self-Documenting Code (PLAN §D.4: comments-repeat, comments-intent, isLeapYear)
COMMENTS_REPEAT = """// Computes the average.
double average(double[] values) {
    // set sum to zero
    double sum = 0.0;
    // loop over the values
    for (int i = 0; i < values.length; i++) {
        // add the value to the sum
        sum = sum + values[i];
    }
    // divide the sum by the length
    return sum / values.length;
}"""

COMMENTS_INTENT = """// Mean of the values; the caller guarantees at least one value.
double mean(double[] values) {
    double sum = 0.0;
    for (double value : values) {
        sum = sum + value;
    }
    return sum / values.length;
}"""

IS_LEAP_YEAR = """// True if the year has 366 days in the Gregorian calendar.
boolean isLeapYear(int year) {
    // divisible by 4, except centuries, except every fourth century
    return (year % 4 == 0 && year % 100 != 0) || year % 400 == 0;
}"""

# Themes of Craftsmanship (PLAN §D.4: retry-delay is presets.py's capstone;
# nested-shipping is the Nesting and Complexity lesson's listing, verbatim).
RETRY_DELAY = """int retryDelayMillis(Request request, int attempt) {
    if (request == null || attempt < 1) {
        return 0;
    }
    int delay = 100;
    for (int i = 1; i < attempt; i++) {
        delay = delay * 2;
        if (delay > 10000) {
            delay = 10000;
        }
    }
    if (request.isIdempotent() && request.hasDeadline()) {
        delay = Math.min(delay, request.millisToDeadline());
    }
    return delay;
}"""

NESTED_SHIPPING = """double shippingCost(Order order) {
    double cost = 0.0;
    if (order != null) {
        if (order.weight() > 0) {
            if (order.isDomestic()) {
                if (order.weight() < 2 && !order.isExpress()) {
                    cost = 5.0;
                } else {
                    cost = 9.0 + order.weight();
                }
            } else {
                for (Item item : order.items()) {
                    if (item.isRestricted() || item.weight() > 30) {
                        return -1.0;
                    }
                }
                cost = 25.0 + 2 * order.weight();
            }
        }
    }
    return cost;
}"""


def _lines(snippet):
    return snippet.split("\n")


LESSONS = [
    # ---------------------------------------------------------------- 01
    # McConnell Chapter 31, pp. 729-775. Opening quotation: Key Points, p. 775
    # (15 words). Fundamental Theorem of Formatting p. 732; human and computer
    # readings pp. 732-733; Chase and Simon, Shneiderman, Hank and Tony p. 734;
    # layout as religion and the objectives pp. 735-736; white space and
    # indentation p. 737 (F27); parentheses p. 738; the four styles pp. 738-745;
    # single-statement blocks pp. 748-749.
    # F27, p. 737 (Miara et al. 1983: indentation and comprehension).
    {
        "slug": "layout-and-style",
        "title": "Layout and Style",
        "module": "Chapter 31 · Layout and Style",
        "one_line": "Good layout shows the structure the compiler reads, and a layout that shows a different structure leads the next reader into a defect.",
        "summary": (
            "Chapter 31 argues that the first job of layout is to show a program's logical "
            "structure, and that looking good comes a distant second. Find the lines of a short "
            "Java routine whose indentation tells a different story from the one Java reads, and "
            "say in words what the compiler does with them."
        ),
        "key": [
            "layout shows the logical structure",
            "an unbraced if governs one statement",
            "an else binds to the nearest open if",
            "expected spaces is depth × indent",
            "consistency matters more than style",
        ],
        "key_label": "Chapter 31 in five lines",
        "concepts_intro": (
            "The chapter rests on one principle and one fact about readers. The lesson adds the "
            "Java rule that makes the principle bite."
        ),
        "concepts": [
            ("The Fundamental Theorem of Formatting",
             "McConnell's name for the chapter's principle: good visual layout shows the logical "
             "structure of a program. Where showing the structure and looking good pull apart, "
             "showing the structure wins."),
            ("Two readers",
             "The compiler reads braces, keywords and precedence, and ignores white space. A "
             "person reads the indentation first. A layout that agrees with the code tells both "
             "the same story; one that disagrees tells the person the wrong one."),
            ("The dangling else",
             "In Java an if without braces governs exactly one statement, and an else belongs to "
             "the nearest if that does not yet have one, wherever the else is indented. A layout "
             "can put an else under one if while Java gives it to another."),
        ],
        "read_title": "The chapter's argument, then a routine whose layout misleads",
        "read_intro": (
            "Read Sections 31.1 to 31.3 in your own copy first. The lesson sets out the argument "
            "section by section, then runs the chapter's test on three short routines."
        ),
        "body": [
            ("p", "<strong>Chapter 31, Key Points, p. 775.</strong> &ldquo;The first priority "
                  "of visual layout is to illuminate the logical organization of the code.&rdquo; "
                  "Chapter 31, Layout and Style, runs from page 729 to page 775. Read Sections "
                  "31.1 to 31.3 in your own copy before going on, and skim 31.4 to 31.8, which "
                  "apply the same idea to control structures, statements, comments, routines and "
                  "classes."),
            ("p", "You have probably met this: an `if` with one statement and no braces, and "
                  "later a second line added under it at the same indentation, because the "
                  "indentation said that was where it belonged. It did not. Java gives an "
                  "unbraced `if` exactly one statement, and the second line runs every time. "
                  "Section 31.1 opens with cases of this kind (pp. 732&ndash;733). Layout is the "
                  "one part of a program that the compiler ignores and a reader cannot, so a "
                  "listing can tell the reader one story and the compiler another. McConnell's "
                  "name for the rule that follows is the Fundamental Theorem of Formatting: good "
                  "visual layout shows the logical structure of a program. Making code look good "
                  "is worth something, he says, but less than showing its structure, and where "
                  "the two pull apart, the structure wins."),
            ("p", "Why should the structure matter so much to a reader? The section answers with "
                  "a line of research (pp. 733&ndash;734). In 1973 Chase and Simon found that "
                  "chess experts remember the positions of pieces far better than novices when "
                  "the pieces stand as they might in a game, and hardly better when they are "
                  "placed at random. Ben Shneiderman found the same of programmers in 1976, with "
                  "program statements in a sensible order against the same statements shuffled. "
                  "The book's reading is that experts carry a structure in their heads, and new "
                  "material is easy to hold when it fits. So the details of a layout convention "
                  "matter much less than following one consistently. McConnell tells a story to "
                  "the point: two reviewers of his first edition, Hank and Tony, had argued over "
                  "brace placement for a whole project and ended it each preferring the style "
                  "the other had started with."),
            ("p", "Debates about layout, the chapter goes on, sound more like religious wars than "
                  "discussions (p. 735), because layout is partly taste and partly logic. Its "
                  "way through is to name the criteria. A good layout scheme represents the "
                  "code's logical structure accurately, represents it consistently, makes the "
                  "code easier to read, and survives modification, so that changing one line "
                  "does not mean changing several others (pp. 735&ndash;736). Weigh the criteria "
                  "differently and you may reach a different style; the point of naming them is "
                  "that the reasons for a preference come out into the open."),
            ("p", "Section 31.2 (p. 736) lists the tools, and white space is the main one: blank "
                  "lines that divide a routine into paragraphs of related statements, and "
                  "indentation that puts each statement under the one it is subordinate to. The "
                  "book reports one study of indentation in some detail (p. 737). Miara and "
                  "colleagues, in 1983, found that subjects scored 20 to 30 percent higher on a "
                  "comprehension test with an indentation of two to four spaces than with none, "
                  "and that six-space indentation scored second lowest, although many subjects "
                  "felt it was the easier to use. That is one study's result, from its own "
                  "subjects and programs, which the book offers as evidence that indentation is "
                  "not cosmetic; it is not a measurement of your team. The section ends on "
                  "parentheses: use more than you think you need, so that no reader has to work "
                  "out the precedence."),
            ("p", "Section 31.3 (p. 738) is about blocks, the statements under a control "
                  "statement, and describes four styles. In a language with pure blocks, such as "
                  "Visual Basic, every If has its End If and the layout follows naturally. In "
                  "Java and C++ the braces are separate from the control statement, and that is "
                  "where the trouble starts. You can emulate pure blocks, treating the opening "
                  "brace as the end of the `if` line and the closing brace as the block's last "
                  "line, which the book calls standard in Java; you can treat the braces as the "
                  "block's boundaries, indented with it; or you can use endline layout, which "
                  "indents a block to wherever its control statement's line happens to end, and "
                  "which McConnell rejects as inaccurate, hard to apply consistently and hard to "
                  "maintain (p. 745)."),
            ("p", "Sections 31.4 to 31.8 (pp. 745&ndash;772) apply the principle to control "
                  "structures, single statements, comments, routines and classes: one statement "
                  "to a line, continuation lines indented by the standard amount, a comment "
                  "indented with the code it describes, blank lines between the parts of a "
                  "routine. One passage matters most here (pp. 748&ndash;749). An `if` followed "
                  "by a single statement needs no braces, and the book sets out the ways to lay "
                  "it out. Leaving the braces out, it warns, invites someone to add a second "
                  "statement under the `if` and forget to add them, a subtle error because the "
                  "indentation says all is well while the compiler reads it otherwise. On a "
                  "group project McConnell favours braces even round a single statement, and "
                  "whichever style you choose, he asks that it be used consistently."),
            ("p", "Now the code. The lab's layout view reads a Java listing, works out the depth "
                  "that Java's structure gives each line, and compares the line's leading spaces "
                  "with that depth times four, the indent this lesson uses. Its rules are under "
                  "the listing: an unbraced `if`, `else`, `for` or `while` governs one "
                  "statement, one level deeper, and an `else` belongs to the nearest `if` that "
                  "does not yet have one. The Mis-indented lines tile counts the lines that "
                  "disagree, the Which tile lists them, and each one is marked in the listing's "
                  "gutter with a glyph and the word mis-indented. Here is the "
                  "<code>dangling-else</code> preset, a routine that writes to a user by email or "
                  "by letter:"),
            ("code", _lines(DANGLING_ELSE)),
            ("p", "Read it as the indentation invites. Line 2 tests whether the user is active; "
                  "line 3, one level in, tests whether they want email; line 4 sends the email; "
                  "and the `else` on line 5 sits at the depth of line 2, so it looks as if an "
                  "inactive user gets the letter on line 6. Java reads it differently. Neither "
                  "`if` has braces, so line 2's `if` governs the whole `if` statement that "
                  "begins on line 3, and the `else` on line 5 belongs to the nearest `if` "
                  "without one, the one on line 3. So an active user who wants email gets an "
                  "email, an active user who does not gets a letter, an inactive user gets "
                  "nothing, and line 7 logs every user. The lab agrees with Java: Mis-indented "
                  "lines 2, Which 5, 6. The `else` belongs at the depth of line 3, eight spaces, "
                  "and `sendLetter` at twelve. This is the dangling-else problem, and it is what "
                  "the chapter means by a layout that tells the human one story and the computer "
                  "another."),
            ("code", _lines(TWO_STATEMENTS)),
            ("p", "The <code>two-statements</code> preset is the case of page 749 in a routine "
                  "of its own. Line 2's `if` has no braces, so it governs line 3 alone: an "
                  "account with a zero balance is marked closed. Line 4, indented as if it "
                  "belonged under the `if`, is simply the routine's next statement, and every "
                  "account is archived, whatever its balance. The lab gives Mis-indented lines "
                  "1, Which 4. Nothing here is a syntax error, and nothing will tell you except "
                  "a reader, a test, or a check of the layout against the structure."),
            ("code", _lines(BRACED)),
            ("p", "The <code>braced</code> preset is the first routine with the braces the book "
                  "favours on group projects, in the style it calls standard for Java. The "
                  "structure is now in the code, where the compiler reads it, and the "
                  "indentation shows you the same structure: the lab gives 0 and none. Whether "
                  "the opening brace goes at the end of a line or on a line of its own is one of "
                  "the questions the chapter treats as a matter of consistency rather than "
                  "correctness, and this lesson leaves it there. A count of zero says only that "
                  "indentation and structure agree. It says nothing about names, blank lines, or "
                  "whether the routine does what it should."),
            ("h3", "Exercise"),
            ("code", _lines(CLAMP)),
            ("p", "`clamp` is meant to return `value` held between `low` and `high`, and to log "
                  "when it clamps from above. Without the lab, mark every line whose indentation "
                  "disagrees with the structure Java gives it, say in words which statement each "
                  "`if` governs, and say what happens when you compile it. Then paste it into the "
                  "lab to check the lines you marked; one of the quiz questions gives the answer."),
            ("p", "Layout is the part of a program's documentation that the compiler ignores. The "
                  "next lesson, “Self-Documenting Code”, reads Chapter 32 on the other part it "
                  "ignores, the comments, and on the code that needs fewer of them."),
        ],
        "lab": ("cckit", {
            "mode": "code",
            "view": "layout",
            "indent": 4,
            "preset": "dangling-else",
            "presets": [
                {"id": "dangling-else",
                 "label": "notifyUser: an else indented under the outer if",
                 "code": DANGLING_ELSE,
                 "expect": {"coMisIndented": "2", "coLines": "5, 6"}},
                {"id": "two-statements",
                 "label": "close: two indented statements under an unbraced if",
                 "code": TWO_STATEMENTS,
                 "expect": {"coMisIndented": "1", "coLines": "4"}},
                {"id": "braced",
                 "label": "notifyUser with braces",
                 "code": BRACED,
                 "expect": {"coMisIndented": "0", "coLines": "none"}},
            ],
            "panel_title": "Indentation against the structure Java reads",
            "panel_intro": (
                "Each line's leading spaces are compared with the depth Java's structure gives "
                "it, at four spaces a level. Load a preset, or paste a routine of your own."
            ),
        }),
        "steps_title": "Checking a listing's layout against its structure",
        "steps_intro": "Five steps, the last on a routine of your own.",
        "steps": [
            ("Find the control lines without braces",
             "Mark every if, else, for and while whose line does not end in an opening brace. "
             "Each one governs exactly one statement: the next one."),
            ("Pair each else with its if",
             "An else belongs to the nearest if above it that has no else yet and is not shut "
             "off by a closing brace. Write the pairs down by line number."),
            ("Work out each line's depth",
             "Count the braces open above the line, add one for each unbraced control line that "
             "governs it, and multiply by the indent, four spaces here."),
            ("Compare, and say what runs",
             "Mark each line whose leading spaces differ from its depth, and write one sentence "
             "on what Java does with it."),
            ("Check a routine of your own",
             "Paste a routine of yours into the lab, re-indented at four spaces a level if your "
             "team uses another width (an editor will do it). Note the Mis-indented lines count, "
             "and for each flagged line write one sentence on what Java does with it and whether "
             "that is what you meant."),
        ],
        "worked": {
            "title": "Where the else on line 5 belongs",
            "intro": [
                "Take the dangling-else preset and work out the depth Java gives each line, at "
                "four spaces a level.",
            ],
            "lines": [
                "line 2: unbraced if, governs the if on lines 3 to 6",
                "line 3: unbraced if, governs line 4; its else is line 5",
                "line 5: depth 2, so 8 spaces; it has 4",
                "line 6: depth 3, so 12 spaces; it has 8",
                "the lab flags lines 5 and 6",
            ],
            "after": [
                "An inactive user gets nothing, and only an active user who does not want email "
                "gets a letter. The indentation says otherwise, which is why the lab flags the "
                "two lines that say it.",
            ],
        },
        "quiz_title": "Layout and structure",
        "quiz": [
            {"q": "In the dangling-else preset, Java binds the else on line 5 to which if? (An "
                  "else belongs to the nearest if that does not yet have one.)",
             "a": ["The if on line 3, which tests wantsEmail",
                   "The if on line 2, which tests isActive",
                   "Neither: javac rejects the else as ambiguous",
                   "Both: it runs when either test fails"],
             "c": 0,
             "why": "The nearest if without an else is line 3's, so line 6 runs for an active "
                    "user who does not want email, and an inactive user gets nothing. Line 2 is "
                    "where the indentation puts it, which is the layout's story and not Java's. "
                    "Java's rule leaves nothing ambiguous, so there is no compile error, and an "
                    "else belongs to exactly one if."},
            {"q": "In the two-statements preset, close is called with an account whose balance "
                  "is 50. Which of lines 3 and 4 run?",
             "a": ["Line 4 only", "Lines 3 and 4", "Neither line", "Line 3 only"],
             "c": 0,
             "why": "Line 2's if has no braces, so it governs line 3 alone; with a balance of 50 "
                    "the test fails and line 3 is skipped. Line 4 is the routine's next "
                    "statement and runs for every account. Both lines run only when the balance "
                    "is 0, and line 3 never runs without line 4."},
            {"q": "What happens when you compile the exercise's clamp exactly as written?",
             "a": ["javac rejects it: line 7 can never be reached",
                   "It compiles, and clamp(5, 0, 10) returns 5",
                   "It compiles, and clamp(5, 0, 10) returns 10",
                   "It compiles, and clamp(15, 0, 10) logs and returns 15"],
             "c": 0,
             "why": "The lab flags one line, line 6 (Mis-indented lines 1, Which 6). Line 4's if "
                    "has no braces, so it governs line 5 alone, and the return on line 6 is "
                    "unconditional: every value that is not below low would return high. That "
                    "makes line 7 unreachable, and javac rejects an unreachable statement. Here "
                    "the compiler catches what the layout hid; with any statement other than a "
                    "return on line 6, a second call to log say, the routine would compile and "
                    "nothing would catch it. Returning 5 is what the indentation promises, and "
                    "returning 10 is what the code would do if line 7 were deleted; nothing in "
                    "the routine returns 15 for a high of 10."},
            {"q": "The book reports a 1983 study of indentation by Miara and colleagues. What "
                  "did it find?",
             "a": ["Scores 20 to 30 percent higher with two to four spaces than with none",
                   "The highest scores with six spaces, which subjects also preferred",
                   "No difference in comprehension between any of the schemes",
                   "Scores 20 to 30 percent higher with none than with two to four spaces"],
             "c": 0,
             "why": "Section 31.2, p. 737: subjects scored 20 to 30 percent higher on a "
                    "comprehension test with two-to-four-space indentation than with none. Six "
                    "spaces scored second lowest, though many subjects felt it was easier to "
                    "use, and no indentation scored lowest of all. It is one study's figure, as "
                    "the book reports it."},
        ],
        "mistakes": [
            ("Thinking indentation is cosmetic",
             "The thought is that the compiler ignores white space, so indentation cannot cause "
             "a defect. The first half is true, and it is the problem: the reader does not ignore "
             "it. In the dangling-else preset the layout says an inactive user gets a letter and "
             "Java sends nothing; in two-statements the layout says only closed accounts are "
             "archived and Java archives every one. Neither is a syntax error. The chapter's "
             "argument (pp. 732&ndash;733) is that a person reads structure from layout, so a "
             "layout that misstates the structure leads the next reader, and the next person "
             "to edit the routine, into the defect; the exercise is a defect the layout hid. The "
             "chapter grants that much of layout is taste, brace placement above all, and this "
             "lesson does not argue with that."),
            ("Choosing the layout that looks best",
             "Six-space indentation looked pleasing to the subjects of the study the book "
             "reports, and scored second lowest on comprehension (p. 737, after Miara and "
             "colleagues). Endline layout can look tidy on a short example and misstate the "
             "structure as soon as the conditions grow (pp. 743&ndash;745). The Fundamental "
             "Theorem puts showing the structure first and looking good a distant second."),
            ("Treating one brace style as the right one",
             "McConnell argues for some styles over others, by stated criteria, but his larger "
             "point is that the details of a convention matter less than following one "
             "consistently, and that a convention followed inconsistently can hurt readability "
             "(pp. 734, 775). Brace placement is the chapter's example of a religious issue, and "
             "its remedy is explicit criteria, not a winner."),
        ],
        "standard": (
            "Mark the mis-indented lines and say what Java does",
            "Given a listing with unbraced ifs, such as the exercise's clamp, mark every line "
            "whose indentation disagrees with the structure Java gives it, and say in a sentence "
            "per line what the compiler does with it. You meet the standard when your marks match "
            "the lab's and each sentence names the statement the governing if controls."
        ),
        "note": (
            "The evidence in this lesson is visual: a listing whose indentation disagrees with "
            "its structure. Read aloud, the indentation disappears, so the body states each "
            "routine's structure in words, and the listing marks a flagged line with a glyph and "
            "the word mis-indented, never by colour alone. The lab checks indentation against "
            "the structure Java gives each line, at four spaces a level, and nothing else: not "
            "blank lines, brace placement, line length or names, not comment-only lines or the "
            "lines that continue a statement, and not what the routine was meant to do. Most "
            "editors now re-indent code to its structure on request, which makes a dangling else "
            "visible to anyone who looks, and fixes nothing by itself."
        ),
    },

    # ---------------------------------------------------------------- 02
    # McConnell Chapter 32, pp. 777-817. Opening quotation: Key Points, p. 817
    # (22 words). External documentation p. 777; style as documentation
    # pp. 778-779; the Commento pp. 781-785 (its voices are not all
    # McConnell's); the three mystery routines pp. 785-786; the six kinds of
    # comment pp. 786-788, Fjelstad and Hamlen p. 788; commenting efficiently
    # pp. 788-791; optimum number p. 792 (F28); techniques pp. 792-812; tricky
    # code p. 801; IEEE standards p. 813. This lesson is the course's home for
    # the modern aside (PLAN §F.4: the comment debate).
    # F28, p. 792 (IBM studies via Jones 2000: one comment per ten statements).
    {
        "slug": "self-documenting-code",
        "title": "Self-Documenting Code",
        "module": "Chapter 32 · Self-Documenting Code",
        "one_line": "Most of a program's documentation is its style, and a comment earns its place by saying what the code cannot, at the level of summary or intent.",
        "summary": (
            "Chapter 32 argues that good code is its own best documentation and that a comment "
            "should say what the code cannot. Count a routine's comment lines against its "
            "statement lines, sort each comment by the chapter's kinds, and see two routines "
            "with the same density and comments of opposite worth."
        ),
        "key": [
            "style documents more than comments",
            "density is comment lines / statement lines",
            "repeating the code adds nothing",
            "keep summary, intent, what code cannot say",
            "the kind of comment matters, not the count",
        ],
        "key_label": "Chapter 32 in five lines",
        "concepts_intro": (
            "The chapter turns on three ideas: what documents code, which comments help, and "
            "why a count of them settles nothing."
        ),
        "concepts": [
            ("Self-documenting code",
             "Code whose structure, names, named constants and layout carry most of its "
             "explanation. McConnell calls it the main contributor to documentation at the level "
             "of the code, and treats comments as the finishing touch on it."),
            ("Kinds of comment",
             "The chapter's six: a repeat of the code, an explanation of it, a marker of "
             "unfinished work, a summary, a description of intent, and information the code "
             "cannot express. Only the last three belong in finished code."),
            ("Comment density",
             "Comment lines over statement lines. The lab computes it because the study the book "
             "reports counted comments per statement; it measures how many comments there are, "
             "not what any of them says."),
        ],
        "read_title": "The chapter's argument, then two routines with comments",
        "read_intro": (
            "Read Sections 32.1 to 32.4 in your own copy first, and the dialogue in 32.3 with "
            "an eye on who is speaking. The lesson then counts and sorts the comments in three "
            "short routines."
        ),
        "body": [
            ("p", "<strong>Chapter 32, Key Points, p. 817.</strong> &ldquo;Comments should say "
                  "things about the code that the code can’t say about itself—at the summary "
                  "level or the intent level.&rdquo; Chapter 32, Self-Documenting Code, runs from "
                  "page 777 to page 817. Read Sections 32.1 to 32.4 in your own copy before going "
                  "on; Section 32.5 is a catalogue of techniques to keep beside you."),
            ("p", "What, in the end, documents a program? The chapter's first answer is not "
                  "comments. Section 32.1 (p. 777) sets aside the documentation kept outside the "
                  "code, unit development folders and detailed-design documents, which on large, "
                  "formal projects hold most of it. Section 32.2 (p. 778) then argues that the "
                  "main contributor to documentation at the level of the code is programming "
                  "style: good structure, straightforward approaches, good names for variables "
                  "and routines, named constants in place of literals, clear layout, and as little "
                  "complexity in control flow and data as the problem allows. Code that carries "
                  "most of its own explanation in these ways is what McConnell calls "
                  "self-documenting, and in such code the comments come last, as a finishing "
                  "touch."),
            ("p", "Section 32.3 (p. 781), To Comment or Not to Comment, is written as a dialogue, "
                  "the Commento, set at the end of a team's daily stand-up with a cast named from "
                  "Plato. Its voices are not all McConnell's, and the section is easy to misquote "
                  "if you forget it. Thrasymachus, a green purist, wants a standard that requires "
                  "comments. Callicles, the veteran, holds that comments make code harder to read, "
                  "are less precise than code, and go out of date. Glaucon, the young hot-shot, "
                  "says that refactoring removes most of his comments. Ismene, a senior programmer "
                  "who maintains other people's code, grants that comments which repeat the code "
                  "are useless, and holds that comments which state intent let her find the part "
                  "she needs, as headings do in a technical book, and that a comment that is hard "
                  "to write is a sign the code is not understood. Socrates closes by siding with "
                  "her: encourage comments without being naive about them, and use reviews to "
                  "learn which ones help. Ismene's is the position the rest of the chapter "
                  "develops; Callicles' objections are the ones it answers."),
            ("p", "Section 32.4 (p. 785) opens with three short routines, each with a comment. "
                  "One comment is wrong, one repeats its code a statement at a time, and one, "
                  "which names the method its routine uses, is the only one that earns its place. "
                  "McConnell's conclusion is blunt: a poor comment is worse than none. He then "
                  "sorts comments into six kinds (pp. 786&ndash;788):"),
            ("ul", [
                "A repeat of the code says what the code says, in other words, and gives the "
                "reader more to read and nothing more to know.",
                "An explanation of the code explains something complicated or tricky; the "
                "chapter's advice is usually to make the code clearer instead.",
                "A marker is a note that the work is unfinished, to be removed before release; "
                "the book asks for one agreed marker, so that a search finds them all.",
                "A summary distils a few lines into a sentence a reader can scan faster than the "
                "code.",
                "A description of intent says what the code is for, in the problem's terms "
                "rather than the solution's.",
                "Information the code cannot express: copyright and version notes, references to "
                "requirements, the source of an algorithm, notes for documentation tools.",
            ]),
            ("p", "The three the chapter accepts in finished code are the last three: summary, "
                  "intent, and what the code cannot express (p. 788). Why intent above all? The "
                  "book cites a six-month study at IBM, published by Fjelstad and Hamlen in 1979, "
                  "in which maintenance programmers said the hardest problem was understanding "
                  "what the original programmer meant. The section then turns to cost. Comments "
                  "need not be slow to write: choose a style that is easy to keep up to date, "
                  "write the comments first as pseudocode, the method of the lesson “The "
                  "Pseudocode Programming Process”, and do not skip them for speed, since a build "
                  "step can strip them. On how many, the book reports (p. 792) that studies at "
                  "IBM, as Capers Jones described them in 2000, found clarity peaked at about one "
                  "comment for every ten statements, with fewer and with more both reducing it. "
                  "That is an average from other people's programs, reported at second hand, and "
                  "McConnell warns against turning it into a quota: attend to whether each "
                  "comment earns its place, and the number will look after itself."),
            ("p", "Section 32.5 (p. 792) works through the techniques level by level: single "
                  "lines (avoid comments at the end of a line, which are hard to maintain and "
                  "tend to be cryptic), paragraphs of code (say why rather than how, and document "
                  "surprises), data declarations (give units and allowed ranges), control "
                  "structures, routines (keep the comment near the code, and document parameters "
                  "where they are declared), and classes, files and whole programs. One piece of "
                  "advice runs against a common habit (p. 801): do not comment tricky code, "
                  "rewrite it, which the book takes from Kernighan and Plauger. Section 32.6 "
                  "(p. 813) points to the IEEE standards for documentation beyond the source."),
            ("p", "Now the code. The lab's size view counts a listing's lines by the rules printed "
                  "under it. Lines is every line. Code lines are those with code outside "
                  "comments, braces included. Statement lines are code lines that hold more than "
                  "braces and semicolons, so a routine's header is one. Comment lines carry a "
                  "comment, alone or after code; Blank lines are empty; Parameters are the "
                  "routine's. Comment lines per statement line is the density, comment lines "
                  "over statement lines, because the study the book reports counted comments per "
                  "statement. Here is the <code>comments-repeat</code> preset:"),
            ("code", _lines(COMMENTS_REPEAT)),
            ("p", "The lab counts 12 lines, 7 code lines and 5 statement lines (the header on "
                  "line 2, and lines 4, 6, 8 and 11), 5 comment lines and no blank ones, and 1 "
                  "parameter. The density is 5 over 5, printed 1 = 100%. Now read the comments by "
                  "kind. Lines 3, 5, 7 and 10 each restate the line under them, and line 1 "
                  "restates the routine's name: all five repeat the code. None of them says what "
                  "the code does not, such as what happens to an empty array, where line 11 "
                  "divides zero by zero and Java gives NaN."),
            ("code", _lines(COMMENTS_INTENT)),
            ("p", "The <code>comments-intent</code> preset does the same calculation as "
                  "`mean`, with one comment. The lab counts 8 lines, 7 code lines, 5 statement "
                  "lines and 1 comment line: a density of 1/5 = 20%, a fifth of the other's. "
                  "That one comment says something the code cannot, that the caller guarantees "
                  "at least one value, which is why line 7 may divide by the length: the "
                  "routine's purpose and its precondition, intent and information the code "
                  "cannot express. Neither density should be set beside the one-in-ten figure "
                  "the book reports. A five-statement routine is not a program, and on the "
                  "lesson's illustration the density tells you nothing until you read the "
                  "comments."),
            ("p", "Since 2004 the question the Commento stages has stayed open. Robert C. "
                  "Martin's <em>Clean Code</em> (2008) treats most comments as a sign that the "
                  "code has failed to say something itself, and asks for better names and "
                  "smaller functions in their place. John Ousterhout's <em>A Philosophy of "
                  "Software Design</em> (2018) argues that comments are needed to record what the "
                  "code cannot, an interface's meaning and the reasons for a design above all. "
                  "Both read like the dialogue continued. The chapter's position is McConnell's: "
                  "make the code as clear as you can, then comment what it cannot say, at the "
                  "level of summary and intent. This lesson does not settle between them, and the "
                  "lab's counts come out the same whichever side you take."),
            ("h3", "Exercise"),
            ("code", _lines(IS_LEAP_YEAR)),
            ("p", "Without the lab, count `isLeapYear`'s statement lines and comment lines by the "
                  "rules above, compute the density, and mark each comment as a repeat of the "
                  "code, an explanation, a summary or a statement of intent. Then set its density "
                  "beside the comments-repeat preset's and say what the comparison does not tell "
                  "you. The lab will check your counts afterwards; one of the quiz questions "
                  "gives the answer."),
            ("p", "Whether a comment gets written, and kept true, is a habit. The next lesson, "
                  "“Personal Character”, reads Chapter 33 on the habits and traits McConnell "
                  "thinks matter most."),
        ],
        "lab": ("cckit", {
            "mode": "code",
            "view": "size",
            "preset": "comments-repeat",
            "presets": [
                {"id": "comments-repeat",
                 "label": "average: a comment over every statement",
                 "code": COMMENTS_REPEAT,
                 "expect": {"coStatements": "5", "coComment": "5", "coDensity": "1 = 100%"}},
                {"id": "comments-intent",
                 "label": "mean: one comment stating its precondition",
                 "code": COMMENTS_INTENT,
                 "expect": {"coStatements": "5", "coComment": "1", "coDensity": "1/5 = 20%"}},
            ],
            "panel_title": "Lines, statements and comments",
            "panel_intro": (
                "The density is comment lines over statement lines. The lab cannot read a "
                "comment: sorting them by kind is yours to do. Load a preset, or paste a routine "
                "of your own."
            ),
        }),
        "steps_title": "Measuring and sorting a routine's comments",
        "steps_intro": "Five steps, the last on a routine of your own.",
        "steps": [
            ("Count the statement lines",
             "Count the lines with code outside comments that hold more than braces and "
             "semicolons. The routine's header is one."),
            ("Count the comment lines",
             "Count every line that carries a comment, alone or after code."),
            ("Compute the density",
             "Divide comment lines by statement lines. It says how many comments there are per "
             "statement and nothing about what they say."),
            ("Sort each comment by kind",
             "Mark each one as a repeat of the code, an explanation, a marker, a summary, a "
             "statement of intent, or information the code cannot express. The last three are "
             "the ones the chapter keeps in finished code."),
            ("Measure a routine of your own",
             "Paste a routine of yours into the lab and note the Comment lines count and the "
             "density. Mark each comment by kind, and write down how many repeat the code and "
             "what one comment the routine is missing would say."),
        ],
        "worked": {
            "title": "Two densities, and what the comments say",
            "intro": [
                "Take the two presets. Count by the lab's rules, then read the comments.",
            ],
            "lines": [
                "average: 5 comment lines, 5 statement lines",
                "density: 5/5, which is 100 percent",
                "mean: 1 comment line, 5 statement lines",
                "density: 1/5, which is 20 percent",
                "repeats of the code: 5 of 5, and 0 of 1",
            ],
            "after": [
                "The routine with five times the density says less: every one of its comments "
                "repeats the code, and the one comment in the other states a precondition the "
                "code cannot.",
            ],
        },
        "quiz_title": "Comments by count and by kind",
        "quiz": [
            {"q": "Count the exercise's isLeapYear by the lab's rules (a statement line holds "
                  "more than braces; the header is one). Which is right?",
             "a": ["2 statement lines, 2 comment lines, 100%; no comment repeats the code",
                   "1 statement line, 2 comment lines, 200%; one comment repeats the code",
                   "2 statement lines, 1 comment line, 50%; no comment repeats the code",
                   "3 statement lines, 2 comment lines, 2/3 ≈ 66.7%; both repeat the code"],
             "c": 0,
             "why": "The statement lines are the header on line 2 and the return on line 4; line "
                    "5 is only a brace. The comment lines are 1 and 3, so the density is 2 over "
                    "2, which the lab prints 1 = 100%, the same as comments-repeat. Neither "
                    "comment repeats the code: line 1 states what the routine is for, a year of "
                    "366 days in the Gregorian calendar, and line 3 states the calendar's rule "
                    "that line 4's expression implements, in the problem's words rather than the "
                    "code's. Both are intent comments, of a kind the chapter keeps. The densities "
                    "are equal and the comments are not, and the count cannot tell them apart. "
                    "One statement line forgets the header, three counts the closing brace, and "
                    "one comment line misses the header comment."},
            {"q": "What density did the IBM studies the book reports, after Capers Jones, find "
                  "clarity peaked at?",
             "a": ["About one comment for every ten statements",
                   "About one comment for every five statements",
                   "About one comment for every statement",
                   "No peak: the more comments, the clearer the code"],
             "c": 0,
             "why": "Section 32.4, p. 792: about one comment per ten statements, with fewer and "
                    "more comments both reducing understandability (IBM studies, as Jones 2000 "
                    "reports them). One in five is the kind of standard McConnell says such "
                    "research gets abused into; one per statement is the comments-repeat "
                    "preset; and the studies found more comments hurt as well."},
            {"q": "In the dialogue of Section 32.3, who argues that comments are useless because "
                  "they repeat the code and go out of date?",
             "a": ["Callicles, the veteran", "Ismene, the senior maintainer",
                   "Socrates, who closes the meeting", "Thrasymachus, the purist"],
             "c": 0,
             "why": "Callicles holds that comments are less precise than code and go stale. "
                    "Ismene answers him and is the voice the chapter develops; Socrates sides "
                    "with her at the end; Thrasymachus wants a standard that requires comments. "
                    "Callicles' view is a view the chapter states in order to answer it, not "
                    "McConnell's conclusion."},
            {"q": "A routine has 20 statement lines and 4 comment lines among its 30 lines. What "
                  "is its density by the lab's rule?",
             "a": ["1/5 = 20%", "2/15 ≈ 13.3%", "5", "1/4 = 25%"],
             "c": 0,
             "why": "Comment lines over statement lines: 4 over 20 is 1/5, 20%. Dividing by all "
                    "30 lines gives 2/15, which is not the measure the study used; 5 is the "
                    "ratio upside down; and 1/4 divides 4 by 16, as if the comment lines were "
                    "taken out of the statement lines, which they are not."},
        ],
        "mistakes": [
            ("Thinking more comments mean better documentation",
             "On the lesson's illustration the density of comments-repeat is five times that of "
             "comments-intent, 100% against 20%, and every one of its comments repeats the "
             "code; the one comment in comments-intent states a precondition the code cannot. "
             "The exercise has the same density as comments-repeat with every comment useful. "
             "The chapter's argument (pp. 785&ndash;788) is that a comment is judged by its kind: "
             "a repeat of the code adds reading and no knowledge, a wrong comment does harm, and "
             "only summary, intent and what the code cannot express earn a place. The count is "
             "not the test."),
            ("Commenting tricky code to make it safe",
             "A warning comment over a delicate passage feels responsible. The chapter calls it "
             "exactly the wrong approach (p. 801): a comment cannot rescue difficult code, and "
             "the advice it takes from Kernighan and Plauger is to rewrite the code. It makes "
             "one exception, for code you are maintaining and have no latitude to rewrite."),
            ("Treating one comment in ten as a quota",
             "The figure is IBM's, from whole programs, as Jones reports it. McConnell warns that "
             "such research gets turned into standards like a comment every five lines, which "
             "treat the symptom and not the cause (p. 792). His advice is to ask of each comment "
             "whether it earns its place and let the number follow."),
        ],
        "standard": (
            "Count, compute and sort a routine's comments",
            "For a routine such as the exercise's isLeapYear, count its statement lines and "
            "comment lines, compute the density, and mark each comment by the chapter's kinds. "
            "You meet the standard when your counts match the lab's and you can say, for each "
            "comment, what it tells a reader that the code does not."
        ),
        "note": (
            "The lab counts lines; it cannot read a comment. It cannot tell a comment that "
            "repeats the code from one that states intent, or a true comment from a stale one, "
            "and both presets would print the same densities if every comment in them were "
            "wrong. The kinds are your judgement, made with the chapter's categories. The "
            "one-in-ten figure is IBM's, from whole programs, reported by Jones; your own code "
            "reviews are the better test of whether your comments help."
        ),
    },

    # ---------------------------------------------------------------- 03
    # McConnell Chapter 33, pp. 819-835. Opening quotation: Key Points, p. 835
    # (23 words). Is character off the topic? p. 820 (F29); intelligence and
    # humility, Dijkstra's Turing lecture p. 821; curiosity pp. 822-826;
    # intellectual honesty pp. 826-828; communication p. 828; creativity and
    # discipline p. 829; laziness p. 830 (three kinds: "true", "enlightened"
    # and "long-term"; the tool is the third); characteristics that matter less
    # pp. 830-833; habits pp. 833-834. The chapter gives no formula for a
    # tool's payback: the lab's model is the lesson's, and its figures are
    # illustrative.
    # F29, p. 820 (Sackman, Erikson and Grant 1968 and later: about 10 to 1).
    {
        "slug": "personal-character",
        "title": "Personal Character",
        "module": "Chapter 33 · Personal Character",
        "one_line": "McConnell argues that what makes a superior programmer is character and habit more than talent, and that even laziness is a virtue when it is judged.",
        "summary": (
            "Chapter 33 argues that a programmer's character, more than intelligence or "
            "experience, decides how good they become: humility, curiosity, honesty, discipline "
            "and the right kind of laziness. Compute when a tool written to do a repeated job "
            "pays back the hours it took, and when it does not."
        ),
        "key": [
            "humility: compensate for small skulls",
            "honesty: understand before compiling",
            "laziness: write the tool, if it pays",
            "runs to repay is build time / saving",
            "weeks is runs / runs per week",
        ],
        "key_label": "Chapter 33 in five lines",
        "concepts_intro": (
            "The chapter is about traits, not techniques. Three of its ideas carry the lesson."
        ),
        "concepts": [
            ("Humility",
             "After Dijkstra: nobody's brain is large enough to hold a program whole, and many "
             "good practices exist to reduce the load on it. The programmers who accept that "
             "improve fastest."),
            ("Long-term laziness",
             "The chapter's third kind of laziness: writing a tool to do an unpleasant task so "
             "that you never do it by hand again. The most productive kind, McConnell says, "
             "provided the tool ends up saving time."),
            ("Break-even",
             "The lesson's model, not the book's: the number of runs after which the minutes a "
             "tool saves add up to the hours it took to build, and the weeks those runs take at "
             "the task's rate."),
        ],
        "read_title": "The chapter's argument, then the arithmetic of a tool",
        "read_intro": (
            "Read Sections 33.1 to 33.9 in your own copy first; the chapter is short. The lesson "
            "sets out its argument, then computes the proviso the chapter attaches to laziness."
        ),
        "body": [
            ("p", "<strong>Chapter 33, Key Points, p. 835.</strong> &ldquo;The characteristics "
                  "of a superior programmer have almost nothing to do with talent and everything "
                  "to do with a commitment to personal development.&rdquo; Chapter 33, Personal "
                  "Character, runs from page 819 to page 835. Read it in your own copy before "
                  "going on."),
            ("p", "The chapter begins by asking whether character is off the topic (§33.1, "
                  "p. 820). McConnell's answer is that in software the building material is the "
                  "programmer's intellect and the main tool is the programmer, so studying the "
                  "tool means studying people. Programming is close to unsupervisable, since "
                  "nobody else really knows what you are working on, and an employer often "
                  "cannot judge whether you are good: if you want to be great, it is up to you. "
                  "The potential is large. The book reports differences of the order of 10 to 1 "
                  "among programmers in the time to write a program, and in the time to debug it "
                  "and the size, speed and error rate of the result, from Sackman, Erikson and "
                  "Grant in 1968 and a line of later studies. Those are other people's "
                  "measurements of other programmers, and McConnell's point in citing them is "
                  "that character, not intelligence, is the more decisive factor."),
            ("p", "Section 33.2 (p. 821) takes intelligence first, and puts it in its place. In "
                  "his Turing Award lecture of 1972, The Humble Programmer, Edsger Dijkstra "
                  "argued that most of programming is an attempt to make up for the strictly "
                  "limited size of our skulls, and that the best programmers are the ones who "
                  "know how small their brains are. McConnell builds the section on it. "
                  "Decomposing a system, reviewing and testing, keeping routines short, writing "
                  "in the problem's terms and following conventions all exist to lighten the "
                  "load on the brain, and the humble programmer who leans on them writes code "
                  "with fewer errors than the clever one who refuses them."),
            ("p", "Curiosity (§33.3, p. 822) is the next trait: learn how you develop software, "
                  "experiment with a short program when you are unsure how a feature works, read "
                  "about problem solving, analyse before you act, and study the work of good "
                  "programmers. Intellectual honesty (§33.4, p. 826) means refusing to pretend "
                  "to expertise, admitting mistakes, understanding a compiler warning rather "
                  "than suppressing it, understanding a program rather than compiling it to see "
                  "whether it works, and giving realistic status reports and estimates. "
                  "McConnell's example is Bert, who lets his manager talk his estimate down and "
                  "will lose credibility when the project takes as long as it takes; an estimate, the chapter says, can be revised to be more "
                  "accurate but not negotiated."),
            ("p", "Communication and cooperation (§33.5, p. 828) come down to writing code for "
                  "the person who must change it. Creativity and discipline (§33.6, p. 829) are "
                  "not opposed: conventions in the areas that do not matter free your creativity "
                  "for the ones that do. Section 33.8 (pp. 830&ndash;833) names traits that "
                  "matter less than you might think. Persistence is mostly stubbornness when you "
                  "are stuck; experience counts for less in a field whose basic knowledge "
                  "changes fast, since ten years can be one year's experience ten times; and "
                  "all-night heroics install defects that take weeks to remove. Section 33.9 "
                  "(p. 833) closes on habits, after Aristotle: you become a good programmer by "
                  "programming well, and you change a bad habit by putting a good one in its "
                  "place."),
            ("p", "Section 33.7 (p. 830) is the one with arithmetic in it, though the chapter "
                  "does none. It names three kinds of laziness. Putting off an unpleasant task "
                  "is the chapter's &ldquo;true laziness&rdquo; and hardly ever helps; doing the "
                  "task at once to get it over with is the enlightened kind; writing a tool so "
                  "that you never do the task again is long-term laziness, which McConnell calls "
                  "the most productive kind, provided that the tool ends up saving time. Hustle, "
                  "visible effort for its own sake, comes off worse than any of them."),
            ("p", "That proviso is something you can compute. The chapter gives no formula, so "
                  "the lab's model is this lesson's. A tool takes some hours to build; the task "
                  "takes some minutes by hand and fewer when automated, so each run saves the "
                  "difference. Runs to pay back is the build time in minutes divided by the "
                  "saving per run, rounded up to a whole run. Weeks to pay back is those runs "
                  "divided by the runs per week. Hours saved in the first year is 52 weeks of "
                  "runs times the saving, less the build time, and it is negative when the tool "
                  "has not paid for itself in a year. Every figure in the presets is "
                  "illustrative."),
            ("p", "The <code>weekly-report</code> preset is a report you assemble by hand in 15 "
                  "minutes, ten times a week, and a script that takes 8 hours to write and 1 "
                  "minute to run. Each run saves 14 minutes, and 480 minutes of building need "
                  "35 runs to pay back: Runs to pay back 35, Weeks to pay back 7/2 = 3.50. "
                  "Over the first year it saves 520 runs of 14 minutes, about 121 hours, less "
                  "the 8 it cost: Hours saved in the first year 340/3 ≈ 113.33. That is the "
                  "long-term laziness the chapter praises."),
            ("p", "The <code>rare-task</code> preset takes the same 8 hours to automate a "
                  "30-minute job that drops to 2 minutes, but the job comes round once every four "
                  "weeks, so the runs per week are 1/4. It needs 18 runs, and at that rate 18 "
                  "runs take 72 weeks; in the first year the tool runs 13 times and saves about 6 "
                  "hours, so the net is −29/15, about −1.93, a loss. The <code>big-tool</code> preset "
                  "spends 40 hours to save 9 minutes on a 10-minute task done five times a week: "
                  "267 runs, 267/5 = 53.40 weeks, and a first year that ends 1 hour down."),
            ("p", "None of this counts everything. The model leaves out the hours a tool takes to "
                  "keep working, the errors a hand-done task makes and the tool does not, and "
                  "what you learn by writing it; it counts only the minutes. But it is the "
                  "arithmetic behind the chapter's proviso, and it is the habit of intellectual "
                  "honesty applied to your own enthusiasm for a tool."),
            ("h3", "Exercise"),
            ("p", "A script takes 2 hours to write and saves a task of 5 minutes once every "
                  "working day, five times a week; run by the script, the task takes no time of "
                  "yours. Without the lab, compute the runs to pay back, the weeks to pay back, "
                  "and the hours saved in the first year of 52 weeks. Then enter the four figures "
                  "in the lab to check; one of the quiz questions gives the answer."),
            ("p", "The chapter's traits recur in the book's last chapter, which gathers its "
                  "themes. The next lesson, “Themes of Craftsmanship”, reads Chapters 34 and 35 "
                  "and puts one routine through the counts of the whole book."),
        ],
        "lab": ("cckit", {
            "mode": "project",
            "view": "breakeven",
            "preset": "weekly-report",
            "presets": [
                {"id": "weekly-report",
                 "label": "A weekly report: 8 hours to script, 15 minutes by hand, ten a week",
                 "build": 8, "manual": 15, "auto": 1, "perWeek": 10,
                 "expect": {"pjRuns": "35", "pjWeeks": "7/2 = 3.50", "pjYear": "340/3 ≈ 113.33"}},
                {"id": "rare-task",
                 "label": "A rare task: 8 hours to automate a job done once in four weeks",
                 "build": 8, "manual": 30, "auto": 2, "perWeek": Fraction(1, 4),
                 "expect": {"pjRuns": "18", "pjWeeks": "72", "pjYear": "−29/15 ≈ −1.93"}},
                {"id": "big-tool",
                 "label": "A big tool: 40 hours to save 9 minutes, five times a week",
                 "build": 40, "manual": 10, "auto": 1, "perWeek": 5,
                 "expect": {"pjRuns": "267", "pjWeeks": "267/5 = 53.40", "pjYear": "−1"}},
            ],
            "panel_title": "When a tool repays the time it took",
            "panel_intro": (
                "Hours to build, minutes per run by hand and automated, and runs per week give "
                "the runs and weeks to pay back and the net hours over a year of 52 weeks. "
                "Figures: illustrative; the chapter gives no formula, so the model is the "
                "lesson's."
            ),
        }),
        "steps_title": "Working out whether a tool pays",
        "steps_intro": "Five steps, the last on a task of your own.",
        "steps": [
            ("Time the task honestly",
             "Write down the minutes the task takes by hand, and the minutes of your time it "
             "would take with the tool, which may be zero."),
            ("Estimate the build",
             "Write down the hours the tool will take to build and get working. This is the "
             "figure most often too low."),
            ("Compute the runs to pay back",
             "Convert the build time to minutes, divide by the minutes saved per run, and round "
             "up to a whole run."),
            ("Turn runs into weeks and a year",
             "Divide the runs by the runs per week. For the first year, multiply the saving by "
             "52 weeks of runs, convert to hours and subtract the build time."),
            ("Price a tool of your own",
             "Choose one task you repeat every week, enter your figures in the lab, and write "
             "down the weeks to pay back and the first year's net. Then double your estimate of "
             "the build time and note whether the tool still pays within a year."),
        ],
        "worked": {
            "title": "The weekly report",
            "intro": [
                "Take the weekly-report preset: 8 hours to build, 15 minutes by hand, 1 minute "
                "automated, ten runs a week.",
            ],
            "lines": [
                "saving per run: 15 minus 1, so 14 minutes",
                "build: 8 hours, or 480 minutes",
                "480 / 14 ≈ 34.3, so 35 runs",
                "35 runs at 10 per week: 7/2 or 3.50 weeks",
                "first year: 520 runs × 14 minutes, less 8 hours",
                "net: 340/3 hours, about 113.33",
            ],
            "after": [
                "The script pays for itself in the fourth week and saves about 113 hours in its "
                "first year. The rare-task preset shows the same build time failing to pay back "
                "inside a year.",
            ],
        },
        "quiz_title": "Character, and a tool's payback",
        "quiz": [
            {"q": "The exercise: a 2-hour script saves a 5-minute task five times a week, and "
                  "the automated run takes none of your time. What are the runs to pay back, "
                  "the weeks, and the first year's net?",
             "a": ["24 runs, 24/5 = 4.80 weeks, 59/3 ≈ 19.67 hours",
                   "24 runs, 24/5 = 4.80 weeks, 65/3 ≈ 21.67 hours",
                   "25 runs, 5 weeks, 59/3 ≈ 19.67 hours",
                   "120 runs, 24 weeks, 59/3 ≈ 19.67 hours"],
             "c": 0,
             "why": "Each run saves 5 minutes and the build is 120 minutes, so 120 / 5 = 24 runs "
                    "exactly, and at five a week 24/5 = 4.80 weeks. In 52 weeks there are 260 "
                    "runs saving 1,300 minutes, 65/3 hours, less the 2 hours of building: 59/3, "
                    "about 19.67 hours. 65/3 forgets to subtract the build; 25 rounds up a "
                    "division that comes out whole; 120 is the build time in minutes, not runs."},
            {"q": "Section 33.7 names three kinds of laziness. Which does it call long-term "
                  "laziness?",
             "a": ["Writing a tool so that you never do the unpleasant task again",
                   "Putting the unpleasant task off for as long as possible",
                   "Doing the unpleasant task at once to get it out of the way",
                   "Hustle: visible extra effort on every task"],
             "c": 0,
             "why": "Page 830: deferring the task is the chapter's true laziness, which hardly "
                    "ever helps; doing it at once is enlightened laziness; writing a tool is "
                    "long-term laziness, the most productive kind provided it ends up saving "
                    "time. Hustle is not a kind of laziness at all, and the chapter counts it "
                    "against a programmer."},
            {"q": "The rare-task preset's tool takes 8 hours to build and saves 28 minutes a run. "
                  "It runs 13 times in the first 52 weeks. What is its net over that year?",
             "a": ["−29/15 ≈ −1.93 hours", "91/15 ≈ 6.07 hours", "−8 hours",
                   "29/15 ≈ 1.93 hours"],
             "c": 0,
             "why": "13 runs × 28 minutes = 364 minutes, 91/15 hours, about 6.07; less the 8 hours "
                    "of building that is −29/15, about −1.93, a loss. 6.07 forgets the build "
                    "time, −8 forgets the runs, and 1.93 has the sign the wrong way round."},
            {"q": "The book reports differences among programmers of roughly what order in the "
                  "time to create a program?",
             "a": ["About 10 to 1", "About 2 to 1", "About 100 to 1", "No measurable difference"],
             "c": 0,
             "why": "Section 33.1, p. 820 (and Section 28.5): differences on the order of 10 to 1 "
                    "in the time to create and to debug a program, and in the size, speed and "
                    "error rate of the result, after Sackman, Erikson and Grant 1968 and later "
                    "studies as the book cites them. They are other people's measurements, not "
                    "a ranking of you."},
        ],
        "mistakes": [
            ("Thinking automating a task always saves time",
             "Writing a tool feels like progress, and the chapter does praise long-term "
             "laziness. But it praises it with a proviso, that the tool ends up saving time "
             "(p. 830), and the proviso is a sum. On the lesson's illustration the rare-task "
             "tool needs 72 weeks to pay back and ends its first year about two hours down, and "
             "the big-tool preset needs more than a year. The chapter's virtue is laziness with "
             "judgement, and the judgement is the arithmetic, done before the tool is written."),
            ("Thinking intelligence is what makes a programmer good",
             "Section 33.2 calls great intelligence only loosely connected to being a good "
             "programmer. Nobody is smart enough to hold a program whole, and the practices "
             "that lighten the load, short routines, reviews, conventions, matter more than the "
             "size of the brain using them. The humble programmer who uses them makes fewer "
             "errors (p. 821)."),
            ("Counting years of experience as skill",
             "Section 33.8 says experience counts for less in software than in most fields, "
             "because basic knowledge changes fast and habits from an old language can be worse "
             "than none. Ten years can be one year's experience ten times; what makes it ten is "
             "reflecting on the work and learning continuously (pp. 831&ndash;832)."),
        ],
        "standard": (
            "Compute a tool's payback",
            "Given the hours to build a tool, the minutes a task takes by hand and with the "
            "tool, and how often it runs, compute the runs and weeks to pay back and the net "
            "hours over a first year of 52 weeks. You meet the standard when all three figures "
            "match the lab's for the exercise's script."
        ),
        "note": (
            "The chapter gives no formula, and the lab's model is the lesson's: it counts the "
            "minutes a tool saves against the hours it took and nothing else. It leaves out "
            "maintenance, the errors a hand-done task makes, and what writing the tool teaches "
            "you, and every preset's figures are illustrative. The 10-to-1 differences are "
            "averages from other people's studies, reported by the book; no lab here measures a "
            "programmer."
        ),
    },

    # ---------------------------------------------------------------- 04
    # McConnell Chapter 34, pp. 837-853, and Chapter 35, pp. 855-862.
    # Opening quotation: Key Points, p. 853 (27 words). Conquer complexity
    # pp. 837-839; pick your process pp. 839-841; people first pp. 841-843;
    # into your language p. 843; conventions pp. 844-845; problem domain
    # pp. 845-847; falling rocks pp. 848-850 (design metrics as warning signs,
    # p. 848, restating F14 and F15; Peirce p. 849); iterate pp. 850-851;
    # software and religion pp. 851-853 (the toolbox, p. 852). Chapter 35:
    # three kinds of information p. 855; the reading plan's three levels,
    # pp. 860-862, named and not reproduced (PLAN §G).
    # F14, p. 458 (decision points and their bands, after McCabe 1976) and
    # F15, p. 445 (nesting past three levels), both restated on p. 848.
    {
        "slug": "themes-of-craftsmanship",
        "title": "Themes of Craftsmanship",
        "module": "Chapters 34–35 · Themes and Further Reading",
        "one_line": "The book's last chapter names the themes its details serve, conquering complexity first, and ends by arguing that no method should be followed as a religion.",
        "summary": (
            "Chapter 34 gathers the book's themes: conquer complexity, pick your process, write "
            "for people first, program into your language, use conventions, work in the "
            "problem's terms, watch for warning signs, iterate, and keep religion out of "
            "software. Chapter 35 points to further reading. Put one routine through the "
            "decision-point and nesting counts and say which theme each count serves."
        ),
        "key": [
            "managing complexity comes first",
            "points: 1 + each if, for, while, case, &&, ||",
            "depth counts braces below the routine",
            "warning signs are reasons to look",
            "eclecticism, not religion",
        ],
        "key_label": "Chapters 34 and 35 in five lines",
        "concepts_intro": (
            "Chapter 34 names many themes. Three of them carry the lesson and the lab."
        ),
        "concepts": [
            ("Conquer complexity",
             "The book's first theme, argued in Chapter 5 as software's primary technical "
             "imperative: most good practices exist to reduce how much of a program a person "
             "must hold in mind at once."),
            ("Warning signs",
             "Section 34.7's falling rocks: tricky code, a class with more errors than average, "
             "a routine with many decision points or deep nesting. Each is a reason to look "
             "skeptically, not proof of a fault."),
            ("Eclecticism",
             "Section 34.9's alternative to treating a method as a religion: keep a toolbox of "
             "techniques, try new ones, rely on the dependable ones, and choose for each problem."),
        ],
        "read_title": "The book's themes, then one routine measured",
        "read_intro": (
            "Read Chapter 34 in your own copy first, and look through Chapter 35's reading plan. "
            "The lesson sets out the themes, then puts one routine through two of the book's "
            "counts."
        ),
        "body": [
            ("p", "<strong>Chapter 34, Key Points, p. 853.</strong> &ldquo;Dogmatic "
                  "methodologies and high-quality software development don’t mix. Fill your "
                  "intellectual toolbox with programming alternatives, and improve your skill at "
                  "choosing the right tool for the job.&rdquo; Chapter 34, Themes in Software "
                  "Craftsmanship, runs from page 837 to page 853, and Chapter 35, Where to Find "
                  "More Information, from page 855 to page 862. Read Chapter 34 in your own copy "
                  "before going on."),
            ("p", "Take a routine you wrote last month, one you would rather nobody reviewed. "
                  "Chapter 34 is the book's account of why it feels that way. The book has been "
                  "about details, classes, names, loops, layout, and this chapter picks the "
                  "details up again to show what they serve. The first theme is the one Chapter "
                  "5 argued (§34.1, p. 837): managing complexity is the heart of software "
                  "development. Nobody's brain spans the range of detail a program has, so the "
                  "book's practices are tools for holding less of it at once: subsystems, class "
                  "interfaces that let you ignore what is behind them, avoiding global data, "
                  "deep inheritance and deep nesting, short routines, clear names, few "
                  "parameters, conventions. Abstraction is the most powerful of them; Fred "
                  "Brooks, as the book cites him, counted the move from machine language to "
                  "higher-level languages the biggest single gain the field has made."),
            ("p", "Pick your process (§34.2, p. 839): on a team, how people work together "
                  "decides whether their abilities add up or cancel out, and quality has to be "
                  "built in from the first step, because testing only tells you how the software "
                  "is defective. Write programs for people first, computers second (§34.3, "
                  "p. 841): readability improves comprehension, review, debugging and change, "
                  "and the gains accumulate from many small choices. Program into your language, "
                  "not in it (§34.4, p. 843): decide what you want to do, then find the way your "
                  "language can do it, writing your own assertions or named constants where it "
                  "lacks them."),
            ("p", "Focus your attention with conventions (§34.5, p. 844): a convention answers "
                  "an arbitrary question once, conveys information concisely, guards against a "
                  "known hazard, and can make up for a weakness in the language, though large "
                  "projects can go overboard with them and small ones underboard. Program in "
                  "terms of the problem domain (§34.6, p. 845): top-level code should read as the "
                  "problem being solved, with the files, arrays and loop indexes kept at a lower "
                  "level of abstraction."),
            ("p", "Watch for falling rocks (§34.7, p. 848) is about warning signs. Tricky code, a "
                  "class with more errors than average, a project with a great deal of debugging: "
                  "each suggests something to look at. Design metrics are warning signs of the "
                  "same kind. The section names more than about 10 decision points in a routine "
                  "and more than three levels of logical nesting, the figures of Table 19-2 after "
                  "McCabe and of Section 19.4, and says plainly that none of them necessarily "
                  "means a routine is badly designed, only that it should be looked at "
                  "skeptically. McConnell borrows a phrase from the philosopher Charles Sanders "
                  "Peirce for the feeling to heed: the irritation of doubt, the unease you "
                  "struggle to pass out of into belief."),
            ("p", "Iterate, repeatedly, again and again (§34.8, p. 850): requirements, design, "
                  "estimates and tuning all improve with repeated attempts, and the trick is to "
                  "iterate early, when it is cheap. The last theme (§34.9, p. 851) is that "
                  "software and religion should be kept apart. Dogmatic adherence to one design "
                  "method, one formatting style or one rule is always out of place, because "
                  "software development is heuristic rather than deterministic. Mix methods: "
                  "experiment with the new ones, rely on the dependable ones, and be ready to "
                  "change your beliefs when an experiment says so. McConnell's image is a "
                  "toolbox, and a contractor friend, Simple Simon, who uses vise-grip pliers for "
                  "every job."),
            ("p", "Chapter 35 is a guide to further reading. It sorts what a developer needs into "
                  "core programming books, the larger technical and management contexts, and "
                  "references that last about one project (p. 855), describes books on "
                  "construction and on the topics beyond it, and sets out the reading plan "
                  "McConnell's company, Construx, used, in three levels: introductory, "
                  "practitioner and professional (pp. 860&ndash;862). The list is the book's, "
                  "from 2004, and is not reproduced here; read it in your copy with your own "
                  "judgement about what has been superseded since."),
            ("p", "Now the code. The lab's complexity view counts decision points by the rule "
                  "printed under the listing, McCabe's as Section 19.6 gives it: 1, plus one for "
                  "each `if`, `while`, `for`, `case`, `&&` and `||`. The Decision points tile is "
                  "that count, Breakdown shows its parts, and Band places it in the book's "
                  "ranges: 0&ndash;5, 6&ndash;10 and 10+. Deepest nesting is the greatest brace "
                  "depth below the routine's own braces, and First line at that depth says "
                  "where it is reached. Here is the <code>retry-delay</code> preset, which "
                  "decides how long to wait before retrying a failed request:"),
            ("code", _lines(RETRY_DELAY)),
            ("p", "The lab counts 7 decision points: the 1, three `if`s (lines 2, 8 and 12), one "
                  "`for` (line 6), the `||` on line 2 and the `&&` on line 12, printed as 1 + if "
                  "3 + for 1 + && 1 + || 1. That is in the band 6&ndash;10, where Table 19-2 "
                  "says to start thinking about simplifying. The deepest nesting is 2, first "
                  "reached on line 9, inside the `if` inside the loop. Neither figure is a "
                  "verdict. What they point to is the loop of lines 6 to 11, which doubles a "
                  "delay and caps it, and could be a routine of its own with a name, which would "
                  "serve the complexity theme, and the bare 100 and 10000, which would read "
                  "better as named constants, which would serve the theme of writing for people "
                  "first."),
            ("code", _lines(NESTED_SHIPPING)),
            ("p", "The <code>nested-shipping</code> preset is the shipping routine from the "
                  "lesson “Nesting and Complexity”. The lab counts 9 decision points, 1 + if 5 + "
                  "for 1 + && 1 + || 1, in the band 6&ndash;10, and a deepest nesting of 5, "
                  "first reached on line 14. Five levels is past the three that Section 34.7 "
                  "names as a warning sign. That lesson rewrote the routine with guard clauses; "
                  "here the point is only that the two counts, set beside the chapter's warning "
                  "signs, tell you which of the two routines to look at first."),
            ("h3", "Exercise"),
            ("p", "The exercise is your own code. Take a routine of about fifteen lines that you "
                  "wrote, and without the lab count its decision points by the rule above and "
                  "its deepest nesting. Then name two changes you would make and the theme of "
                  "Chapter 34 each one serves. Paste the routine into the lab to check your "
                  "counts. One quiz question asks for the same counts on retry-delay, so that "
                  "you can check the method on a routine whose answer is fixed."),
            ("p", "This is the last lesson of the read-along. The book's own last word is its "
                  "reading plan; this course's is to go back to the first, “Laying the "
                  "Foundation”, with a routine of your own and see how much of what it argued you "
                  "can now measure."),
        ],
        "lab": ("cckit", {
            "mode": "code",
            "view": "complexity",
            "preset": "retry-delay",
            "presets": [
                {"id": "retry-delay",
                 "label": "retryDelayMillis: a retry with a doubling, capped delay",
                 "code": RETRY_DELAY,
                 "expect": {"coDecisions": "7", "coBreakdown": "1 + if 3 + for 1 + && 1 + || 1", "coDepth": "2"}},
                {"id": "nested-shipping",
                 "label": "shippingCost, nested (from Nesting and Complexity)",
                 "code": NESTED_SHIPPING,
                 "expect": {"coDecisions": "9", "coDepth": "5"}},
            ],
            "panel_title": "Decision points and nesting",
            "panel_intro": (
                "Decision points are 1 plus each branch keyword and boolean operator, by the rules "
                "under the listing; depth is brace depth below the routine's own braces. The bands are the book's guidance, after "
                "McCabe. Load a preset, or paste a routine of your own."
            ),
        }),
        "steps_title": "Measuring a routine against the book's themes",
        "steps_intro": "Five steps, the last on a routine of your own.",
        "steps": [
            ("Count the decision points",
             "Start at 1 and add one for each if, while, for, case, && and ||. An else, a default "
             "and a do add nothing."),
            ("Find the deepest nesting",
             "Count the braces open below the routine's own at each line, and note the greatest "
             "depth and where it is first reached."),
            ("Read the counts as warning signs",
             "Set the count beside the bands, 0 to 5, 6 to 10 and 10+, and the depth beside the "
             "three levels Section 34.7 names. A figure past them is a reason to look, not a "
             "fault."),
            ("Name the theme each change serves",
             "For each change the counts point you to, say which of Chapter 34's themes it "
             "serves: complexity, people first, conventions, the problem's terms."),
            ("Measure a routine of your own",
             "Paste a routine of yours into the lab and note its decision points, band and "
             "deepest nesting. Write one sentence for each theme of Chapter 34 the routine "
             "touches, naming the line that touches it."),
        ],
        "worked": {
            "title": "Counting retry-delay",
            "intro": [
                "Take the retry-delay preset and count by the rule printed under the lab's listing.",
            ],
            "lines": [
                "start at 1",
                "three ifs, on lines 2, 8 and 12",
                "one for, on line 6",
                "one || on line 2, one && on line 12",
                "1 + 3 + 1 + 2 makes 7, in band 6–10",
                "deepest nesting 2, first on line 9",
            ],
            "after": [
                "Seven points and a depth of two put the routine inside the book's warning "
                "signs, and still point at the loop of lines 6 to 11 as the part to look at.",
            ],
        },
        "quiz_title": "Themes and counts",
        "quiz": [
            {"q": "Count retry-delay: decision points are 1 plus each if, while, for, case, && "
                  "and ||, and depth is brace depth below the routine's own braces. Which is "
                  "right?",
             "a": ["7 decision points, deepest nesting 2",
                   "6 decision points, deepest nesting 2",
                   "7 decision points, deepest nesting 3",
                   "5 decision points, deepest nesting 2"],
             "c": 0,
             "why": "1 + three ifs (lines 2, 8, 12) + one for (line 6) + the || on line 2 + the "
                    "&& on line 12 = 7, in the band 6–10. The deepest line is 9, inside the if "
                    "inside the for: depth 2. Six forgets the starting 1; depth 3 counts the "
                    "routine's own braces; five leaves out && and ||. On a routine of your own "
                    "the method is the same, and the figures are yours to check in the lab."},
            {"q": "What does Section 34.7 say a routine with more than about 10 decision points "
                  "means?",
             "a": ["A warning sign that should make you look at it skeptically",
                   "A routine that must be split before it is merged",
                   "Proof that the routine is poorly designed",
                   "Nothing: the chapter does not mention decision points"],
             "c": 0,
             "why": "Page 848 lists more than about 10 decision points and more than three levels "
                    "of nesting among the design metrics that should raise a warning flag, and "
                    "says none of them necessarily means poor design. It names no rule that "
                    "forces a split, and it calls the figure a warning, not proof."},
            {"q": "Section 34.9 argues against treating methods as a religion. What does it "
                  "recommend instead?",
             "a": ["A mixture of methods: try new ones, rely on the dependable ones",
                   "One method, chosen carefully and applied everywhere",
                   "The newest method, adopted in full",
                   "No method: judgement case by case without any technique"],
             "c": 0,
             "why": "Pages 851–852: rather than latch on to the latest fad, use a mixture of "
                    "methods, experimenting with new ones and banking on old and dependable "
                    "ones, as tools in a toolbox. One method everywhere is the dogmatism it "
                    "rejects, so is the newest fad, and the toolbox is full of techniques."},
            {"q": "How does Chapter 35 organise its reading plan?",
             "a": ["In three levels: introductory, practitioner and professional",
                   "By programming language",
                   "By the chapters of Code Complete",
                   "By year of publication, newest first"],
             "c": 0,
             "why": "Section 35.4, pp. 860–862: the plan Construx used, in introductory, "
                    "practitioner and professional levels. It is not arranged by language, by "
                    "chapter or by date, and the lesson names it without reproducing it."},
        ],
        "mistakes": [
            ("Thinking craftsmanship is a set of rules to follow",
             "After thirty-three chapters of advice it is natural to read the book as a rulebook. "
             "Its last theme argues against that reading (§34.9): dogmatic adherence to any "
             "method, style or rule is always out of place, because software development is "
             "heuristic, and the book's techniques are tools to choose among. Even its "
             "thresholds are offered as warning signs that call for a look, not as rules that "
             "settle a case (p. 848). The counts in this course are tools for judgement, which "
             "is the point of saying that a count is a reason to look."),
            ("Reading a count under the threshold as a pass",
             "Retry-delay's 7 decision points and depth of 2 sit inside the book's warning "
             "signs, and the counts still point at a loop that could be its own routine and two "
             "bare numbers that could be named. A count says where to look in both directions: "
             "a low one does not certify a routine, any more than a high one condemns it."),
            ("Thinking process is overhead that gets in the way of code",
             "Section 34.2 states the view that code is what matters and process an abstraction, "
             "and calls it shortsighted (p. 841). Quality has to be built in from the first "
             "step, and how a team works decides whether its members' abilities add up."),
        ],
        "standard": (
            "Measure a routine and name the themes",
            "For the 16-line retry-delay routine, state its decision points and its deepest "
            "nesting by the stated rules, name two improvements and the theme of Chapter 34 "
            "each serves. You meet the standard when your counts match the lab's and each "
            "improvement names the lines it changes."
        ),
        "note": (
            "The lab counts decision points and nesting by a stated rule and nothing else. It "
            "cannot see a theme: whether a routine is written in the problem's terms, whether "
            "its conventions help, whether its process was sound. The bands are the book's "
            "guidance after McCabe, and Section 34.7 itself calls such figures warning signs. "
            "Chapter 35's reading list is named and not reproduced, and dates from 2004."
        ),
    },
]
