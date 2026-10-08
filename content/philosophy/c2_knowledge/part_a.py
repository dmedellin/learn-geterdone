"""Course 2, lessons 01-06 -- analysing knowledge, justification, and the opening of credence."""


def _case(name, values, verdict):
    return {"name": name, "values": values, "verdict": verdict}


LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "belief-truth-and-justification",
        "title": "Belief, Truth and Justification",
        "module": "Analysing knowledge",
        "one_line": "Knowledge as three conditions, and a definition tested against cases until one row disagrees.",
        "summary": (
            "The traditional analysis says that to know is to believe something true "
            "with justification. Each of the three conditions is claimed to be "
            "necessary and the three together sufficient, and a table of cases can "
            "test both claims. The skill taught here is finding the row where a "
            "definition and a verdict disagree."
        ),
        "key": [
            "knows ⟺ justified, true, believed",
            "necessary: no case lacks it and knows",
            "sufficient: every case with all three knows",
            "test: a case where definition ≠ verdict",
        ],
        "key_label": "An analysis is a claim about every case",
        "concepts_intro": (
            "An analysis of knowledge is a definition, and a definition can be wrong "
            "in exactly two ways. Cases are how you find out which."
        ),
        "concepts": [
            ("Necessary means no exceptions below",
             "A condition is necessary when every case that lacks it is a case of not "
             "knowing. One lucky guess, a belief held without any justification that "
             "happens to be true, is enough to show why justification is on the list."),
            ("Sufficient means no exceptions above",
             "The conditions are jointly sufficient when every case that has all of "
             "them is a case of knowing. This is the claim that later lessons break."),
            ("The verdict column is yours",
             "A case table records what you judge about each case before the "
             "definition is applied. The lab compares the definition with those "
             "judgements; it cannot say whether the judgements are right."),
        ],
        "read_title": "The tripartite analysis and the method of cases",
        "read_intro": "A definition, four cases, and the one question the table asks of each row.",
        "body": [
            ("p", "To believe something is not yet to know it, and to be right is not "
                  "yet to know it either. A person who believes it will rain "
                  "tomorrow, and is right, but only because they flipped a coin to "
                  "decide what to believe, does not know it will rain. The oldest "
                  "serious answer to what is missing is that the belief must also be "
                  "justified."),
            ("def", ("The tripartite analysis",
                     "A person <strong>knows</strong> that `p` exactly when three "
                     "conditions hold: `p` is true (`T`), the person believes `p` "
                     "(`B`), and the belief is justified (`J`). In symbols, "
                     "`knows ⟺ J ∧ T ∧ B`.")),
            ("p", "Two claims are packed into that biconditional, and they fail "
                  "differently. Each condition is <em>necessary</em>: nobody who "
                  "lacks one of the three knows. And the three are <em>jointly "
                  "sufficient</em>: anybody who has all three knows. A definition "
                  "that fails in the first way, because some case lacks one of its "
                  "conditions and is knowledge all the same, shuts out a case of "
                  "knowledge and is called <strong>too narrow</strong>. One that "
                  "fails in the second way, because some case has every condition "
                  "and is not knowledge, lets in a case that is not knowledge and "
                  "is called <strong>too broad</strong>. This lesson tests the "
                  "first claim; the next lesson breaks the second."),
            ("h3", "Four cases, one condition missing each"),
            ("math", [
                "case                   J   T   B   knows?",
                "----------------------------------------",
                "ordinary perception    1   1   1   yes",
                "lucky guess            0   1   1   no",
                "confident error        1   0   1   no",
                "unbelieved truth       1   1   0   no",
            ]),
            ("p", "Read the table row by row. Ordinary perception is a plain case: "
                  "you see the cup, you believe it is there, it is there. The lucky "
                  "guess lacks justification, the confident error lacks truth, and "
                  "the unbelieved truth lacks belief, as when a student has good "
                  "evidence that she passed and cannot bring herself to accept it. "
                  "Each of the three failing rows is a reason one condition is on "
                  "the list."),
            ("p", "Written as a formula, the definition is `J ∧ T ∧ B`, and the lab "
                  "writes the and-sign as an ampersand. It agrees with all four verdicts. Now remove "
                  "a condition and test again. The definition `T ∧ B` says the lucky "
                  "guess is knowledge, and the verdict says no. The definition "
                  "`J ∧ B` says the confident error is knowledge, and the verdict "
                  "says no. The definition `J ∧ T` says the unbelieved truth is "
                  "knowledge, and the verdict says no. Each shortened definition is "
                  "too broad, and the lab names the row."),
            ("example", ("The method of cases in one move",
                         "State a definition. Collect cases whose verdict you are "
                         "confident of. Apply the definition to every case. If the "
                         "definition and a verdict disagree on some row, one of "
                         "them has to give, and the rest of the lesson is about "
                         "which. Here nothing disagrees, so the definition "
                         "survives these four cases and no more than these four.")),
            ("p", "That last clause is the lab’s limit. Agreement on four rows "
                  "is agreement on four rows. The next lesson is a case the table "
                  "above does not contain."),
        ],
        "lab": ("argkit", {
            "mode": "analysis",
            "search": "off",
            "preset": "jtb",
            "presets": [
                {"id": "jtb", "label": "J, T and B all required",
                 "conditions": ["J", "T", "B"], "target": "knows", "definition": "J & T & B",
                 "cases": [
                     _case("ordinary perception", [1, 1, 1], 1),
                     _case("lucky guess", [0, 1, 1], 0),
                     _case("confident error", [1, 0, 1], 0),
                     _case("unbelieved truth", [1, 1, 0], 0),
                 ],
                 "expect": {"anAgree": "4 / 4", "anVerdict": "Adequate"}},
                {"id": "no-justification", "label": "justification dropped",
                 "conditions": ["J", "T", "B"], "target": "knows", "definition": "T & B",
                 "cases": [
                     _case("ordinary perception", [1, 1, 1], 1),
                     _case("lucky guess", [0, 1, 1], 0),
                     _case("confident error", [1, 0, 1], 0),
                     _case("unbelieved truth", [1, 1, 0], 0),
                 ],
                 "expect": {"anAgree": "3 / 4", "anFail": "lucky guess: too broad", "anVerdict": "Too broad"}},
            ],
            "panel_title": "Edit the definition and read the verdict",
            "panel_intro": "The table has four cases and three conditions. Type a formula over `J`, `T` and `B` and the lab reports how many verdicts it matches and the first row it gets wrong. Click a value or a verdict in the table to change a case.",
        }),
        "steps_title": "Testing a definition against a case table",
        "steps_intro": "Five moves, in this order. The order matters: the verdict comes before the definition.",
        "steps": [
            ("List the conditions",
             "Name each condition the analysis uses and give it a letter. A case is "
             "then a row of ones and zeros: has the condition, or lacks it."),
            ("Record the verdict first",
             "Write what you judge about each case before looking at the "
             "definition. Otherwise the definition decides your verdict and the test "
             "tests nothing."),
            ("Evaluate the definition on every row",
             "Apply the formula to each row. The definition is true on a row when "
             "it says the person knows."),
            ("Find the first disagreement",
             "A row where the definition is true and the verdict is no is too "
             "broad. A row where the definition is false and the verdict is yes is "
             "too narrow."),
            ("Report the direction, not just the failure",
             "“It fails” is not a finding. “It is too broad on the lucky guess” "
             "tells the next author which way to repair it."),
        ],
        "worked": {
            "title": "Dropping each condition in turn",
            "intro": ["Take the four cases of the table and try the full definition, then each pair."],
            "lines": [
                "J ∧ T ∧ B   agrees on 4 of 4",
                "T ∧ B       lucky guess: definition yes, verdict no",
                "J ∧ B       confident error: yes, verdict no",
                "J ∧ T       unbelieved truth: yes, verdict no",
            ],
            "after": [
                "Every pair is too broad on exactly the row that the dropped "
                "condition was there to exclude. That is what it means for the "
                "three to be individually necessary on this table, and it is the "
                "whole of the argument for each: a case in which the condition is "
                "missing and knowledge plainly is too.",
            ],
        },
        "quiz_title": "Conditions and cases",
        "quiz": [
            {"q": "The lab tries the definition `J ∧ B`, with truth dropped. Which case does it get wrong?",
             "a": ["Ordinary perception", "Lucky guess", "Unbelieved truth", "Confident error"],
             "c": 3,
             "why": "The confident error has `J = 1` and `B = 1`, so `J ∧ B` says the person knows, and the verdict is no. Ordinary perception is a case of knowing and `J ∧ B` agrees. The lucky guess has `J = 0` and the unbelieved truth has `B = 0`, so `J ∧ B` already says no on both, which matches their verdicts."},
            {"q": "To say the three conditions are individually necessary is to say that",
             "a": ["any case with one of the three is a case of knowing",
                   "any case lacking one of the three is a case of not knowing",
                   "any case with all three is a case of knowing",
                   "the three are listed in order of importance"],
             "c": 1,
             "why": "Necessary means no exceptions below: lack the condition and you do not know. The first choice mixes it up with sufficiency in its weakest form, the third is sufficiency, and nothing in the analysis ranks the conditions."},
            {"q": "A definition agrees with all four verdicts in a table. What follows?",
             "a": ["The definition is correct",
                   "The verdicts were correct",
                   "The definition survives those four cases; a fifth might disagree",
                   "Each of its conditions is sufficient on its own"],
             "c": 2,
             "why": "Agreement is evidence about the cases listed and nothing beyond them. The verdicts are the reader’s input, so agreement cannot make them right, and a single condition being sufficient would be a stronger claim than the table can show."},
        ],
        "mistakes": [
            ("Treating a definition as a list of typical features",
             "On a feature list, a case with most of the features is mostly knowledge. A definition says something stronger: every one of the conditions must hold. The confident error has justification and belief, two of three, and the verdict is not that it is two-thirds knowledge but that it is not knowledge at all. A definition of knowledge is tested by one failing row, not by a majority."),
            ("Expecting the lab to say which verdict is right",
             "The lab compares a formula with a column you typed. If you record the wrong verdict for a case, a wrong definition will agree with it and the lab will say the definition is adequate. The method of cases moves the argument to the verdicts, where it belongs; it does not remove it."),
            ("Thinking the truth condition is something the knower can check",
             "Justification and belief are conditions on the person. Truth is a condition on the world, and from the inside the confident error feels exactly like ordinary perception. That is why the truth condition is the one that is easy to forget and the hardest to use."),
        ],
        "standard": (
            "Finish when you can find the row, and name the direction.",
            "Given a proposed definition and a table of cases you should be able to evaluate the definition on every row, name the first row where it disagrees with the verdict, and say whether it is too broad or too narrow there. “It does not work” without the row and the direction does not carry over to the cases in “Gettier Cases and the Fourth Condition”."),
        "note": "The case table is deliberately small. Philosophers argue for decades about single rows of tables like this one, and the lab can hold only the rows you give it. Its job is to make a disagreement visible, not to settle it.",
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "gettier-cases-and-the-fourth-condition",
        "title": "Gettier Cases and the Fourth Condition",
        "module": "Analysing knowledge",
        "one_line": "A case with justification, truth and belief that is not knowledge, and a repair that the next case breaks.",
        "summary": (
            "Gettier cases are rows where all three conditions hold and the verdict "
            "is still that the person does not know, so the definition is too broad. "
            "A fourth condition can be added to remove the failing row, and a new "
            "case can then be found that the fourth condition cannot separate."
        ),
        "key": [
            "J, T and B all hold, and no knowledge",
            "the definition is too broad on that row",
            "a fourth condition removes the row",
            "a new case breaks the fourth condition",
        ],
        "key_label": "Too broad, then repaired, then too broad again",
        "concepts_intro": (
            "The previous lesson tested a definition against four cases, and it "
            "survived. These cases are the ones it was not tested against."
        ),
        "concepts": [
            ("A Gettier case has all three conditions",
             "The belief is justified, true and held, and the person does not know. "
             "The definition says the person knows, so it admits a case that should "
             "be excluded. That is the direction called too broad."),
            ("A fourth condition is a new column",
             "To exclude the failing row the table needs a way to tell it apart from "
             "ordinary perception. A new condition is a new column that is 1 on the "
             "failing row and 0 on perception."),
            ("A repair is itself a definition",
             "A repaired analysis is tested the way the original was. The cases that "
             "broke the first version are not the only cases, and the repair must "
             "meet the ones that follow."),
        ],
        "read_title": "Smith’s coins, the stopped clock and the fake barns",
        "read_intro": "Two cases that the three conditions cannot tell apart from perception, and a third that the repair cannot.",
        "body": [
            ("p", "In Gettier’s own case Smith has strong evidence that Jones "
                  "will get the job, and that Jones has ten coins in his pocket. "
                  "Smith therefore believes that the man who will get the job has "
                  "ten coins in his pocket. In fact Smith himself gets the job, and "
                  "Smith himself has ten coins. The belief is justified, true and "
                  "held. Almost nobody thinks Smith knew it."),
            ("p", "Russell’s stopped clock is the same shape with a simpler "
                  "mechanism. You look at a clock that stopped twelve hours ago, "
                  "read the time off it, and believe it is a quarter past two. By "
                  "chance it is. You had good reason to trust the clock, the belief "
                  "is true, and you hold it."),
            ("math", [
                "case                   J   T   B   knows?",
                "----------------------------------------",
                "ordinary perception    1   1   1   yes",
                "Smith's coins          1   1   1   no",
                "stopped clock          1   1   1   no",
                "lucky guess            0   1   1   no",
            ]),
            ("p", "Two rows of this table are identical in all three columns and "
                  "different in the verdict. Whatever the definition says about "
                  "perception it must say about Smith’s coins, and the "
                  "verdicts disagree. The lab’s search over one and two conditions "
                  "finds no formula that fits, and none of any length could, because "
                  "the inputs of two rows are the same and the outputs are not."),
            ("h3", "A fourth condition"),
            ("p", "The usual repair adds a condition that is true of the failing "
                  "rows and false of perception. In both cases the belief depends "
                  "on something false along the way: that Jones will get the job, "
                  "that the clock is running. Call the condition `L`, for “relies "
                  "on a false lemma”, and require it to be absent: `J ∧ T ∧ B ∧ ¬L`. "
                  "The lab writes not as a tilde."),
            ("math", [
                "case                   J   T   B   L   knows?",
                "---------------------------------------------",
                "ordinary perception    1   1   1   0   yes",
                "Smith's coins          1   1   1   1   no",
                "stopped clock          1   1   1   1   no",
                "lucky guess            0   1   1   0   no",
                "fake barns             1   1   1   0   no",
            ]),
            ("p", "The fourth condition now separates Smith’s coins and the "
                  "stopped clock from perception, and the lab now reports "
                  "agreement on four of five rows. The last row is why it does not end there. "
                  "Henry drives through country dotted with barn facades and looks "
                  "at the one real barn. He sees a barn, believes it is a barn, and "
                  "is right. He relies on no false lemma at all, so `L = 0`, and "
                  "most people think he does not know, because he could easily have "
                  "been looking at a facade."),
            ("p", "Perception and fake barns now agree on every column, `J = 1`, "
                  "`T = 1`, `B = 1`, `L = 0`, and differ in the verdict. This is "
                  "the same trouble as before at a new place, and the lab names the "
                  "row. Fixing it takes a fifth condition, and the literature has "
                  "tried several."),
            ("thm", ("What the cases show and what they do not",
                     "They show that the three conditions are not jointly "
                     "sufficient. They do not show that knowledge is impossible, "
                     "and they do not show that justification is irrelevant: the "
                     "lucky guess row still needs `J`, because without it the "
                     "repaired definition calls the guess knowledge.")),
        ],
        "lab": ("argkit", {
            "mode": "analysis",
            "search": "pairs",
            "preset": "lemma",
            "presets": [
                {"id": "gettier", "label": "J, T and B only",
                 "conditions": ["J", "T", "B"], "target": "knows", "definition": "J & T & B",
                 "cases": [
                     _case("ordinary perception", [1, 1, 1], 1),
                     _case("Smith's coins", [1, 1, 1], 0),
                     _case("stopped clock", [1, 1, 1], 0),
                     _case("lucky guess", [0, 1, 1], 0),
                 ],
                 "expect": {"anAgree": "2 / 4", "anFail": "Smith's coins: too broad", "anVerdict": "Too broad", "anCands": "none"}},
                {"id": "lemma", "label": "with a false-lemma condition",
                 "conditions": ["J", "T", "B", "L"], "target": "knows", "definition": "J & T & B & ~L",
                 "cases": [
                     _case("ordinary perception", [1, 1, 1, 0], 1),
                     _case("Smith's coins", [1, 1, 1, 1], 0),
                     _case("stopped clock", [1, 1, 1, 1], 0),
                     _case("lucky guess", [0, 1, 1, 0], 0),
                     _case("fake barns", [1, 1, 1, 0], 0),
                 ],
                 "expect": {"anAgree": "4 / 5", "anFail": "fake barns: too broad", "anVerdict": "Too broad", "anCands": "none"}},
            ],
            "panel_title": "Add a condition and test the repair",
            "panel_intro": "The first preset has three conditions and the second has a fourth, `L`. The candidate search tries formulas of one or two conditions and reports how many fit every row.",
        }),
        "steps_title": "Working a Gettier case",
        "steps_intro": "Constructing a case and then testing a repair, in the order the lab expects.",
        "steps": [
            ("Start from an ordinary case of knowing",
             "Take a case you are sure about, such as seeing a cup on the table, "
             "and write its row. Everything else is a variation on it."),
            ("Break the connection but keep the three conditions",
             "Add luck that sits between the justification and the truth. The "
             "evidence points the right way for the wrong reason, so `J`, `T` and "
             "`B` stay at one."),
            ("Record the verdict and classify the failure",
             "If you judge that the person does not know, the definition is too "
             "broad on this row. Say so: it is the direction that tells you the "
             "repair must add a condition."),
            ("Propose a fourth condition",
             "Choose a condition that is present on the failing row and absent on "
             "ordinary perception, and add its negation or itself to the "
             "definition."),
            ("Look for a case the new condition cannot separate",
             "Build a case with the same four values as perception and a different "
             "verdict. If you can, the repair is too broad on that row, and you "
             "are back at the second step."),
        ],
        "worked": {
            "title": "Smith’s coins through the lab",
            "intro": ["Row by row, with `L` standing for a false lemma."],
            "lines": [
                "Smith's coins:  J=1 T=1 B=1  verdict no",
                "J ∧ T ∧ B:      says knows -> too broad",
                "add ¬L:         L=1 on the coins -> now says no",
                "fake barns:     J=1 T=1 B=1 L=0, verdict no",
                "J ∧ T ∧ B ∧ ¬L: says knows -> too broad again",
            ],
            "after": [
                "The repair did what it was built to do and removed one row. It "
                "did not stop the failure; it moved it. That is the usual history "
                "of a proposed fourth condition.",
            ],
        },
        "quiz_title": "Gettier rows",
        "quiz": [
            {"q": "On Smith’s coins the definition `J ∧ T ∧ B` says the person knows and the verdict is no. The definition is",
             "a": ["too narrow", "too broad", "adequate on this row", "inconsistent"],
             "c": 1,
             "why": "It admits a case that should be excluded, and that is the meaning of too broad. Too narrow is the opposite failure, where the definition shuts out a case of knowing. A row cannot make a definition inconsistent; it only agrees or disagrees with the verdict."},
            {"q": "In the table with `L`, which row stops you from dropping `J` from the repaired definition?",
             "a": ["Ordinary perception", "The stopped clock", "The lucky guess", "The fake barns"],
             "c": 2,
             "why": "The lucky guess is the only row with `J = 0`. Without `J` the definition `T ∧ B ∧ ¬L` says the guess is knowledge, and the verdict is no. Every other row has `J = 1`, so `J` makes no difference to them."},
            {"q": "Why does the fake barns case break the false-lemma repair?",
             "a": ["It has a false lemma, so the repair excludes it wrongly",
                   "It has no false lemma, yet the verdict is that Henry does not know",
                   "It lacks justification",
                   "It lacks belief"],
             "c": 1,
             "why": "Henry relies on nothing false, so `L = 0` and the repaired definition says he knows; the verdict says he does not. He has justification and belief, so the third and fourth choices are wrong, and since `L = 0` the repair does not exclude him, so the first is wrong."},
            {"q": "What do Gettier cases show about the three conditions?",
             "a": ["Knowledge is impossible",
                   "Justification plays no part in knowing",
                   "The three are not jointly sufficient",
                   "Truth is not necessary"],
             "c": 2,
             "why": "The cases are rows with all three conditions and no knowledge, which is exactly a failure of sufficiency. Nothing in them makes knowing impossible or removes a necessary condition, and the lucky guess row still shows why justification is needed."},
        ],
        "mistakes": [
            ("Taking Gettier to show that knowledge is impossible, or that justification is irrelevant",
             "The ordinary perception row still has all conditions and the verdict yes, so cases of knowing survive. The lucky guess row still needs justification excluded, and the lab shows the repaired definition calling the guess knowledge as soon as `J` is dropped. What the cases refute is the claim that the three conditions are enough. A definition that is too broad on some rows is not a definition of nothing."),
            ("Believing a fourth condition ends the matter",
             "A repair is a new definition and meets the same test. The false-lemma condition removes the coins and the clock and then fails on the fake barns, where there is no false lemma. The failure moves to a case the repair did not anticipate, and the lab’s search finds no formula of one or two of the listed conditions that fits the table; the two rows that agree in every column and differ in the verdict show that none of any size could."),
            ("Reading “justified” as “certain”",
             "Smith is not careless. His evidence is strong, and it is only the luck between evidence and truth that fails him. Raising the standard of justification does not help, because any standard short of the truth itself can be met by a case with this structure."),
        ],
        "standard": (
            "Finish when you can build the row and classify it.",
            "You should be able to write down a case with all three conditions present and the verdict no, say that the definition is too broad on it, propose a fourth condition, and construct a case with the same values as perception that the new condition cannot separate. A case described in prose without its row of values has not yet been tested."),
        "note": "The labs search only the conditions that you list. If the table has no column that separates two rows, no search can succeed, and finding what the missing column would be is the philosophical work the lab leaves to you.",
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "reliabilism-and-the-clairvoyant",
        "title": "Reliabilism and the Clairvoyant",
        "module": "Analysing knowledge",
        "one_line": "Justification as a reliable process, tested against Norman the clairvoyant and the brain in a vat.",
        "summary": (
            "Reliabilism replaces the believer’s evidence with the "
            "reliability of the process that produced the belief. Norman, who has a "
            "reliable and undetected power of clairvoyance, makes the definition too "
            "broad, and the envatted twin makes it too narrow as a theory of "
            "justification. The lab names the direction of each failure."
        ),
        "key": [
            "reliable process: right in most uses",
            "Norman: reliable, no evidence, believes",
            "vat twin: evidence, unreliable, believes",
            "failures run in opposite directions",
        ],
        "key_label": "Two theories, two kinds of counterexample",
        "concepts_intro": (
            "Reliabilism and evidentialism are two answers to what makes a belief "
            "justified. Each is a definition, and each is tested the same way."
        ),
        "concepts": [
            ("Reliability belongs to a process",
             "A process type, such as vision in good light, is reliable when it "
             "produces mostly true beliefs over many uses. It is a property of the "
             "kind of process, not of the one belief it produced this time."),
            ("Evidence is what the believer can access",
             "The rival view says a belief is justified by what the believer has to "
             "go on: experiences, memories, reasons they could cite. Two people with "
             "the same evidence are alike in justification."),
            ("The two views fail on different cases",
             "A case with reliability and no accessible evidence tests one. A case "
             "with accessible evidence and no reliability tests the other."),
        ],
        "read_title": "Reliable process against accessible evidence",
        "read_intro": "Two definitions, four cases, and the direction each failure runs.",
        "body": [
            ("p", "The reliabilist keeps the shape of the earlier definitions and "
                  "changes the justification condition. A belief is justified when "
                  "it was produced by a reliable process. A person knows when the "
                  "belief is also true and held, so in the lab’s symbols the "
                  "definition is `R ∧ T ∧ B`, with `R` for a reliable process. "
                  "The evidentialist keeps accessible evidence in its place: "
                  "`E ∧ T ∧ B`."),
            ("p", "Reliability is easily misread. It does not mean the process "
                  "gave the right answer this time. A coin toss can deliver a true "
                  "belief once, and the process of guessing by coin is not reliable "
                  "for that. A good barometer can give a false reading on a rare "
                  "day and remain reliable. The measure is the proportion of true "
                  "beliefs the process delivers across its uses."),
            ("h3", "Norman"),
            ("p", "Norman has a faculty of clairvoyance that is, as it happens, "
                  "reliable. One day he finds himself believing that the President "
                  "is in New York. He has no evidence for it and no evidence that "
                  "he has the faculty. The President is in New York. The belief is "
                  "true, held, and produced by a reliable process."),
            ("math", [
                "case              R   E   T   B   knows?",
                "-----------------------------------------",
                "perception        1   1   1   1   yes",
                "Norman            1   0   1   1   no",
                "envatted twin     0   1   0   1   no",
                "stranger's guess  0   0   1   1   no",
            ]),
            ("p", "Reliabilism says Norman knows, because `R`, `T` and `B` all hold. "
                  "The verdict, as recorded, is that he does not. The definition is "
                  "too broad on that row. Evidentialism says Norman does not know, "
                  "because `E = 0`, and agrees with the verdict. When the lab "
                  "searches for formulas that fit every row, it finds two, `R ∧ E` "
                  "and `E ∧ T`, and the first it lists is `R ∧ E`: reliable and "
                  "with evidence."),
            ("h3", "The brain in a vat"),
            ("p", "The envatted twin is a person whose experiences are exactly like "
                  "yours but who is a brain in a vat, fed those experiences by a "
                  "computer. Nearly all of the twin’s beliefs about the "
                  "external world are false, so as a case of <em>knowing</em> the "
                  "twin is simply a no, and both definitions agree. The case matters "
                  "for the justification condition, which is where the two theories "
                  "differ. If the twin’s beliefs are as well justified as "
                  "yours, then justification cannot be the same as reliability, "
                  "because the twin’s process is not reliable."),
            ("math", [
                "case              R   E   justified?",
                "-------------------------------------",
                "perception        1   1   yes",
                "Norman            1   0   no",
                "envatted twin     0   1   yes",
                "stranger's guess  0   0   no",
            ]),
            ("p", "Run on this second table, “justified iff reliable” fails twice. "
                  "It is too broad on Norman, who is reliable and not justified by "
                  "this verdict, and too narrow on the twin, who is justified and "
                  "not reliable. “Justified iff has evidence” fits all four rows. "
                  "That does not make evidentialism correct. The reliabilist "
                  "replies with the chicken sexer, who sorts chicks reliably, "
                  "cannot say how, and seems to know; his row would be "
                  "`R = 1`, `E = 0`, the same values as Norman, with the opposite "
                  "verdict, and no formula can fit two rows like that."),
        ],
        "lab": ("argkit", {
            "mode": "analysis",
            "search": "pairs",
            "preset": "reliabilist",
            "presets": [
                {"id": "reliabilist", "label": "reliability replaces justification",
                 "conditions": ["R", "E", "T", "B"], "target": "knows", "definition": "R & T & B",
                 "cases": [
                     _case("perception", [1, 1, 1, 1], 1),
                     _case("Norman", [1, 0, 1, 1], 0),
                     _case("envatted twin", [0, 1, 0, 1], 0),
                     _case("stranger's guess", [0, 0, 1, 1], 0),
                 ],
                 "expect": {"anAgree": "3 / 4", "anFail": "Norman: too broad", "anCands": "2: first R & E"}},
                {"id": "evidentialist", "label": "accessible evidence replaces justification",
                 "conditions": ["R", "E", "T", "B"], "target": "knows", "definition": "E & T & B",
                 "cases": [
                     _case("perception", [1, 1, 1, 1], 1),
                     _case("Norman", [1, 0, 1, 1], 0),
                     _case("envatted twin", [0, 1, 0, 1], 0),
                     _case("stranger's guess", [0, 0, 1, 1], 0),
                 ],
                 "expect": {"anAgree": "4 / 4", "anVerdict": "Adequate", "anCands": "2: first R & E"}},
                {"id": "justified", "label": "the same four cases, asking only about justification",
                 "conditions": ["R", "E"], "target": "justified", "definition": "R",
                 "cases": [
                     _case("perception", [1, 1], 1),
                     _case("Norman", [1, 0], 0),
                     _case("envatted twin", [0, 1], 1),
                     _case("stranger's guess", [0, 0], 0),
                 ],
                 "expect": {"anAgree": "2 / 4", "anFail": "Norman: too broad", "anVerdict": "Too broad and too narrow", "anCands": "1: first E"}},
            ],
            "panel_title": "Swap the definition and watch the direction",
            "panel_intro": "Two presets ask whether a person knows, and the third asks only whether the belief is justified. Edit the definition in each and compare which row it fails on.",
        }),
        "steps_title": "Testing a theory of justification",
        "steps_intro": "The same procedure as before, with the added care of asking which question the table is about.",
        "steps": [
            ("Fix the target",
             "Decide whether the table is about knowing or about justification. A "
             "case such as the vat twin can be no on one and yes on the other."),
            ("Write each case as values of the conditions",
             "Give the reliability of the process and the accessibility of the "
             "evidence separately. The cases only separate the theories when "
             "those two come apart."),
            ("Record the verdicts before applying either theory",
             "Norman and the twin are the cases whose verdicts are contested. "
             "Write yours down, and note which readers might disagree."),
            ("Apply each theory and read the direction",
             "Where a theory says yes and the verdict says no it is too broad. "
             "Where it says no and the verdict says yes it is too narrow."),
            ("Check what the search finds",
             "The lab lists the formulas that fit every row. A theory that fits "
             "is not thereby right, but one that has no fitting formula at all "
             "needs a new condition."),
        ],
        "worked": {
            "title": "Norman and the twin, in the lab’s terms",
            "intro": ["Use the justification table with the definition `R`."],
            "lines": [
                "perception:   R=1  verdict yes   agrees",
                "Norman:       R=1  verdict no    too broad",
                "vat twin:     R=0  verdict yes   too narrow",
                "guess:        R=0  verdict no    agrees",
                "R alone:      too broad and too narrow",
            ],
            "after": [
                "A single definition can fail in both directions at once, on "
                "different rows. The lab reports the first row that disagrees and "
                "the verdict for the whole definition, and the second is the one "
                "that records both.",
            ],
        },
        "quiz_title": "Reliability and evidence",
        "quiz": [
            {"q": "Norman believes truly through a reliable faculty and has no evidence. Reliabilism about justification is",
             "a": ["too narrow on Norman", "adequate on Norman", "too broad on Norman", "unaffected, because Norman does not believe"],
             "c": 2,
             "why": "Reliabilism says Norman is justified and the verdict records that he is not, so it admits a case that should be excluded. Norman does believe, with `B = 1`, which rules out the last choice."},
            {"q": "Which statement about the word “reliable” is correct?",
             "a": ["A reliable process is one that is right this time",
                   "A reliable process is one that produces mostly true beliefs across its uses",
                   "A reliable process is one the believer can describe",
                   "A reliable process is one that has never given a false belief"],
             "c": 1,
             "why": "Reliability is a rate over many uses of a kind of process. A lucky guess is right this time without being reliable, a reliable process can occasionally err, and the believer need not be able to say how it works."},
            {"q": "The envatted twin has experiences like yours and mostly false beliefs. Why does the twin count against “justified iff reliable”?",
             "a": ["Because the twin is justified and not reliable, so the definition is too narrow",
                   "Because the twin is reliable and not justified, so the definition is too broad",
                   "Because the twin has no beliefs",
                   "Because the twin knows the external world"],
             "c": 0,
             "why": "If the twin is as justified as you are, a definition that requires reliability shuts out a case of justified belief, which is too narrow. The twin has beliefs and does not know the external world, which rules out the last two choices."},
            {"q": "The chicken sexer is reliable, has no accessible evidence, and seems to know. What does his row do to the table?",
             "a": ["It confirms evidentialism",
                   "It shows the table has no solution because there are too many rows",
                   "It is the same case as the twin",
                   "It has the same values as Norman and the opposite verdict, so no formula over these conditions fits both"],
             "c": 3,
             "why": "Two rows with identical inputs and different outputs cannot be fitted by any formula of those inputs, and that is a fact about the table. It would refute the evidentialist reading, not confirm it, the number of rows is not the issue, and the twin has `R = 0`."},
        ],
        "mistakes": [
            ("Reading “reliable” as “right this time”",
             "Reliability is a rate for a kind of process. The stranger’s guess in the table gives a true belief, so it was right this time, and the process is not reliable: `R = 0`. A reliable faculty can also give a false belief on a rare occasion without ceasing to be reliable. Norman’s case is unsettling because the faculty is reliable and nothing in his experience says so."),
            ("Concluding that a theory which fits the table is true",
             "The evidentialist definition fits all four rows, and the lab’s search finds several fitting formulas. The rows are a few chosen cases. The chicken sexer, left out of the table, is a case no formula can fit alongside Norman, so the choice of rows has already decided what fits."),
            ("Confusing the failure of a definition with its refutation",
             "A definition that is too broad on one row has a counterexample, and a counterexample is a reason for revising it, not necessarily for dropping the idea. Reliabilists answer Norman by adding that the believer must have no reason to doubt the faculty, which is a new condition tested the same way."),
        ],
        "standard": (
            "Finish when you can say which direction each case pushes.",
            "Given a theory of justification and three cases you should be able to compute which rows it fits, name the cases on which it is too broad and the cases on which it is too narrow, and say what a case that no formula fits shows about the table."),
        "note": "The twin is only a counterexample to reliabilism if you record its justification as yes. Some reliabilists record no and explain the intuition away. The lab accepts either verdict and reports what follows from it.",
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "skepticism-and-the-closure-argument",
        "title": "Skepticism and the Closure Argument",
        "module": "Justification",
        "one_line": "The brain-in-a-vat argument as modus tollens, Moore’s reply as modus ponens, and what validity cannot choose.",
        "summary": (
            "The skeptic and Moore share one premise, that knowing you have hands "
            "brings with it knowing you are not a brain in a vat, and disagree about "
            "which of two other claims is more certain. The lab shows that both "
            "arguments are valid. Choosing between them takes a judgement that no "
            "truth table supplies."
        ),
        "key": [
            "skeptic: h → b, ¬b, so ¬h",
            "Moore: h, h → b, so b",
            "both arguments are valid",
            "the shared premise is closure",
        ],
        "key_label": "One conditional, two directions",
        "concepts_intro": (
            "A skeptical argument is an argument, and what the earlier course "
            "taught about validity applies to it without change."
        ),
        "concepts": [
            ("Closure",
             "If you know something and you know that it brings another claim with "
             "it, you know the other claim. Here: if you know you have hands, you "
             "know you are not a handless brain in a vat."),
            ("Modus tollens and modus ponens run one conditional both ways",
             "From `h → b` and `¬b` you may conclude `¬h`. From `h → b` and `h` you "
             "may conclude `b`. Both are valid forms, so the quarrel is over the "
             "premises that are not shared."),
            ("Denying closure is a third option",
             "Drop the conditional and neither argument goes through. The cost is "
             "that you must say a person can know one thing without knowing "
             "something it plainly implies."),
        ],
        "read_title": "Two valid arguments with opposite conclusions",
        "read_intro": "The argument written out, then its mirror image, then the choice neither of them makes.",
        "body": [
            ("p", "Let `h` stand for “I know I have hands” and `b` for “I know I am "
                  "not a brain in a vat being fed experiences”. The skeptic argues "
                  "in three lines."),
            ("math", [
                "h → b      if I know I have hands, I know I am not envatted",
                "¬b         I do not know I am not envatted",
                "∴ ¬h       so I do not know I have hands",
            ]),
            ("p", "The first premise is the closure principle applied to a case. "
                  "The second is the skeptic’s claim that nothing in your "
                  "experience could rule the vat out, since the vat is built to "
                  "make your experience exactly what it is. The lab reads this "
                  "argument as valid, with the form modus tollens, and that "
                  "verdict is the whole of what the lab contributes."),
            ("p", "Moore answered by reading the argument backwards. He was more "
                  "certain that he had hands than he could be of any philosophical "
                  "premise, so he took the same conditional and went the other way."),
            ("math", [
                "h          I know I have hands",
                "h → b      if I know that, I know I am not envatted",
                "∴ b        so I know I am not envatted",
            ]),
            ("p", "This is modus ponens, also valid. Put the two side by side and "
                  "what stands out is that they share a conditional and a "
                  "disagreement. The skeptic is more sure of `¬b` than of `h`, and "
                  "Moore is more sure of `h` than of `¬b`. The three sentences "
                  "`h → b`, `¬b` and `h` cannot all be true together, which is the "
                  "sort of fact the consistency lab reports, and it means one has "
                  "to go."),
            ("h3", "The third option"),
            ("p", "Dretske and others keep both `¬b` and `h` and give up the "
                  "conditional: you can know there is a zebra in the pen without "
                  "knowing it is not a cleverly painted mule. The preset for this "
                  "has only `¬b` as a premise and `¬h` as the conclusion, and the "
                  "lab finds it invalid, with the counterexample row `h = T`, "
                  "`b = F`. That row is the denier’s position written as an "
                  "assignment: knows hands, does not know about the vat."),
            ("p", "What each choice costs deserves to be said plainly. The skeptic "
                  "accepts that nobody knows much of anything about the external "
                  "world. Moore accepts that a philosopher can claim to know the "
                  "vat is not there without any evidence that settles it. The "
                  "denier accepts that “I know I have hands but I do not know I "
                  "am not a handless brain in a vat” is true, which sounds "
                  "absurd when said aloud. The lab can tell you none of this is "
                  "inconsistent with the logic and nothing more."),
        ],
        "lab": ("argkit", {
            "mode": "validity",
            "show": "all",
            "preset": "closure",
            "presets": [
                {"id": "closure", "label": "the skeptic’s argument",
                 "premises": ["h -> b", "~b"], "conclusion": "~h", "expect": {"vaVerdict": "Valid", "vaForm": "modus tollens", "vaCounter": "0"}},
                {"id": "moore", "label": "Moore’s reply",
                 "premises": ["h", "h -> b"], "conclusion": "b", "expect": {"vaVerdict": "Valid", "vaForm": "modus ponens", "vaCounter": "0"}},
                {"id": "deny-closure", "label": "closure denied",
                 "premises": ["~b"], "conclusion": "~h", "expect": {"vaVerdict": "Invalid", "vaForm": "no catalogued form", "vaCounter": "1"}},
            ],
            "panel_title": "Check each argument for a counterexample row",
            "panel_intro": "The lab builds every row of the truth table for `h` and `b`. A counterexample row makes every premise true and the conclusion false. Type the arrow as a hyphen followed by a greater-than sign, and not as a tilde.",
        }),
        "steps_title": "Formalising a skeptical argument",
        "steps_intro": "How to turn a paragraph of epistemology into something the lab can check.",
        "steps": [
            ("Pick one letter for each knowledge claim",
             "Let the letter stand for the whole claim, including “I know”. The "
             "lab does not see inside it, and the argument is about how the claims "
             "relate."),
            ("State the closure premise as a conditional",
             "Write it as `h → b`. This is the step on which the skeptic and Moore "
             "agree, and the step that the denier rejects."),
            ("Write the argument in each direction",
             "One has the negated consequent as a premise, the other has the "
             "antecedent. Run both and note the form the lab names."),
            ("Read the counterexample rows",
             "A valid argument has none. An invalid one has at least one, and the "
             "row tells you which combination of truth values the argument fails to "
             "exclude."),
            ("Say what is left to decide",
             "Name the premise that each side holds more firmly than the other. "
             "That judgement is not a truth-table fact, and the lesson is not "
             "finished until you have said it in words."),
        ],
        "worked": {
            "title": "One conditional, three arguments",
            "intro": ["With `h` for “I know I have hands” and `b` for “I know I am not envatted”."],
            "lines": [
                "h → b, ¬b  ∴ ¬h    valid, modus tollens",
                "h, h → b   ∴ b     valid, modus ponens",
                "¬b         ∴ ¬h    invalid: h=T, b=F",
                "{h → b, ¬b, h}     cannot all be true",
            ],
            "after": [
                "The first two arguments are both valid and their conclusions "
                "cannot both be accepted along with all their premises. The "
                "disagreement is therefore a disagreement about whether `¬b` or "
                "`h` is the one to keep, and about nothing in the logic.",
            ],
        },
        "quiz_title": "Which move, and what it needs",
        "quiz": [
            {"q": "The skeptic’s argument has the premises `h → b` and `¬b` and the conclusion `¬h`. Which form is it?",
             "a": ["Modus ponens", "Affirming the consequent", "Modus tollens", "Denying the antecedent"],
             "c": 2,
             "why": "It denies the consequent of the conditional and concludes the denial of the antecedent. Modus ponens would assert `h`, and the other two forms are the fallacies that look similar and have counterexample rows."},
            {"q": "The lab calls both the skeptic’s and Moore’s arguments valid. What decides between them?",
             "a": ["A judgement about whether `¬b` or `h` is the more certain claim",
                   "The number of counterexample rows in each table",
                   "Which of the two uses fewer symbols",
                   "A third truth table that scores plausibility"],
             "c": 0,
             "why": "Both tables have no counterexample row, so the count cannot separate them, and symbol count is irrelevant to truth. No truth table scores plausibility. What is left is a decision about which premise to hold more firmly."},
            {"q": "The argument with premise `¬b` and conclusion `¬h` is invalid. Which row is the counterexample?",
             "a": ["`h = F`, `b = F`", "`h = F`, `b = T`", "`h = T`, `b = T`", "`h = T`, `b = F`"],
             "c": 3,
             "why": "A counterexample makes the premise `¬b` true, so `b = F`, and the conclusion `¬h` false, so `h = T`. In the other rows either the premise fails or the conclusion holds."},
        ],
        "mistakes": [
            ("Thinking a valid argument compels you to accept its conclusion",
             "Validity says only that if the premises are true the conclusion is. Here the skeptic’s argument and Moore’s are both valid, yet `h → b`, `¬b` and `h` cannot all be true, so no one can accept every premise of both. A person who is more sure that they have hands than that `¬b` is true should reject `¬b`, and that is not a mistake of logic."),
            ("Hearing Moore’s reply as a refutation",
             "Moore’s argument is valid, but the skeptic can accuse it of begging the question: whoever doubts `b` will doubt `h` for the same reason. Whether that charge is fair depends on how premises earn their credibility, which the lab does not model. Moore’s reply tells you what rejecting the skeptic costs; it does not make the cost zero."),
            ("Treating closure as obviously true",
             "The conditional `h → b` looks like plain common sense, and that is why both sides use it. It is also the premise whose denial gives the third position, and the invalid argument in the lab is the shape of that position. Closure is a principle about knowledge, not a theorem of logic."),
        ],
        "standard": (
            "Finish when you can say what the lab has not decided.",
            "You should be able to formalise the skeptic’s argument and Moore’s reply over one conditional, name their forms, find the counterexample row that closure denial exposes, and state in a sentence which premise each position holds more firmly. The validity verdict is the easy half."),
        "note": "The same structure reappears whenever an argument has a premise that its opponent finds less credible than the denial of the conclusion. Learning to see the shared conditional is worth more than any one version of the vat.",
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "the-regress-of-justification",
        "title": "The Regress of Justification",
        "module": "Justification",
        "one_line": "Agrippa’s trilemma as six claims that cannot all be true, and the position each deletion yields.",
        "summary": (
            "If every justified belief needs a justified supporter, the chain of "
            "support must end in a foundation, loop back on itself, or run on "
            "forever. The set of claims that rules out all three is inconsistent, "
            "its smallest inconsistent subset is the whole set, and each single "
            "deletion gives one named position."
        ),
        "key": [
            "some belief is justified: j",
            "j needs a justified supporter: j → n",
            "n → circle, foundation or infinite chain",
            "deny each of the three: inconsistent",
        ],
        "key_label": "Six claims, no model",
        "concepts_intro": (
            "The regress is an old problem, and the earlier course gave us a "
            "tool for it: a set of claims is consistent when some assignment "
            "makes them all true."
        ),
        "concepts": [
            ("The set is inconsistent",
             "The six sentences have no model. Every assignment makes at least one "
             "false, so something has to give, and the question becomes which."),
            ("A minimal inconsistent subset is what is really at issue",
             "It is a set that cannot all be true and in which removing any one "
             "sentence restores consistency. Here it is the whole set, so every "
             "sentence is load-bearing for the trouble."),
            ("Each deletion is a position",
             "Delete one of the three denials and a way of ending the regress is "
             "permitted. Delete the first sentence and you have the skeptic."),
        ],
        "read_title": "Agrippa’s trilemma as a set of claims",
        "read_intro": "Six sentences, one inconsistency, and four ways out.",
        "body": [
            ("p", "Suppose you believe the tap is dripping because you heard it. "
                  "What justifies hearing as a source? That it has been reliable. "
                  "What justifies that? A track record of checks, each of which "
                  "was itself a belief. Asked for the support of each supporter, "
                  "you can answer in only a few ways, and the old skeptical "
                  "argument says none of them is satisfactory."),
            ("p", "Write it as six claims over five letters. `j` says some "
                  "belief is justified. `n` says every justified belief needs a "
                  "justified supporter. And `c`, `f` and `i` say that, "
                  "respectively, a circle of supporters, a foundation that needs "
                  "no further support, and an infinite chain of supporters are "
                  "acceptable ways for the chain to end."),
            ("math", [
                "1.  j                 some belief is justified",
                "2.  j → n             so it needs a justified supporter",
                "3.  n → (c ∨ f ∨ i)   the chain is a circle, a foundation",
                "                      or infinite",
                "4.  ¬c                circles are not acceptable",
                "5.  ¬f                unsupported foundations are not",
                "6.  ¬i                infinite chains are not",
            ]),
            ("p", "The lab finds no assignment that makes all six true, and "
                  "reports the smallest inconsistent subset as all six sentences. "
                  "That matters. A minimal inconsistent subset is the part of the "
                  "set that is doing the damage, and here no part of it can be "
                  "spared: remove any one sentence and a model appears."),
            ("h3", "Four positions, four deletions"),
            ("ul", [
                "<strong>Foundationalism</strong> deletes `¬f`. Some beliefs "
                "justify others without needing a justifier of their own, and the "
                "lab’s model has `f` true and the chain stopping there.",
                "<strong>Coherentism</strong> deletes `¬c`. Beliefs support one "
                "another in a web, and the objection that this is a circle is "
                "denied as an objection.",
                "<strong>Infinitism</strong> deletes `¬i`. Justification is never "
                "completed, only deepened as far as questions are asked.",
                "<strong>Skepticism</strong> deletes `j`. If nothing is justified "
                "there is nothing for the regress to apply to, and the lab’s "
                "skeptic preset replaces `j` with `¬j`.",
            ]),
            ("p", "The foundationalist version is one line of a truth table. Take "
                  "the foundationalist set, with `¬f` removed, and the lab finds a model "
                  "in which `j`, `n` and `f` are true and `c` and `i` are false: "
                  "a justified belief that needs a supporter, the supporter being "
                  "a foundation. That the set is satisfiable shows only that the "
                  "position is coherent as a set of sentences. Whether any "
                  "belief is a foundation is the substantive question."),
            ("p", "One limit should be stated. The lab sees the five letters as "
                  "unanalysed claims. It does not look inside “every justified "
                  "belief needs a supporter” to see a chain, so the structure of "
                  "the regress is carried by the sentences, not computed from them. "
                  "Everything the lab reports follows from the six sentences as "
                  "written."),
        ],
        "lab": ("argkit", {
            "mode": "consistency",
            "preset": "agrippa",
            "presets": [
                {"id": "agrippa", "label": "all three endings denied",
                 "sentences": ["j", "j -> n", "n -> (c | f | i)", "~c", "~f", "~i"],
                 "expect": {"coVerdict": "Inconsistent", "coMis": "{1, 2, 3, 4, 5, 6}", "coWitness": "none"}},
                {"id": "foundationalist", "label": "foundations permitted",
                 "sentences": ["j", "j -> n", "n -> (c | f | i)", "~c", "~i"],
                 "expect": {"coVerdict": "Consistent", "coMis": "none", "coWitness": "c=F f=T i=F j=T n=T"}},
                {"id": "skeptic", "label": "nothing is justified",
                 "sentences": ["~j", "j -> n", "n -> (c | f | i)", "~c", "~f", "~i"],
                 "expect": {"coVerdict": "Consistent", "coMis": "none", "coWitness": "c=F f=F i=F j=F n=F"}},
            ],
            "panel_title": "Delete a sentence and look for a model",
            "panel_intro": "The set is the one in the text. Use the drop menu to delete one sentence at a time and read whether a model appears, and which letters it makes true.",
        }),
        "steps_title": "Reading the regress as a consistency problem",
        "steps_intro": "From a puzzle in words to a set the lab can search.",
        "steps": [
            ("Write every commitment as a sentence",
             "Include the denials. The trilemma is only a problem because the "
             "skeptic denies each ending, and a denial left unwritten is a premise "
             "hidden."),
            ("Check the whole set",
             "Ask for a model. If the lab finds none, the set is inconsistent and "
             "something has to be deleted."),
            ("Read the minimal inconsistent subset",
             "It names the sentences the trouble actually needs. If it is smaller "
             "than the set, the rest is innocent."),
            ("Delete one sentence at a time",
             "For each deletion read the model the lab finds. Each model is a "
             "picture of one position: which of the endings it allows."),
            ("Name the cost of each position",
             "Each position keeps the set consistent by permitting an ending the "
             "skeptic found unacceptable. Say what the objection was and how the "
             "position answers it."),
        ],
        "worked": {
            "title": "Dropping the denial of foundations",
            "intro": ["Compare the whole set with the foundationalist set."],
            "lines": [
                "all six:       0 models, Inconsistent",
                "smallest MIS:  the whole set",
                "drop ¬f (5):   consistent, j n f true; c i false",
                "drop ¬c (4):   consistent, c true",
                "drop j (1):    consistent, nothing justified",
            ],
            "after": [
                "Dropping a different sentence gives a different position, and the "
                "lab’s model for each says which ending the position "
                "leans on. The positions are not refuted by this. Each one is "
                "what the set looks like when one of its denials is given up.",
            ],
        },
        "quiz_title": "Positions as deletions",
        "quiz": [
            {"q": "What is the smallest inconsistent subset of the six-sentence Agrippa set?",
             "a": ["The three denials `¬c`, `¬f`, `¬i`", "`j` and `j → n`", "The whole set of six", "`n → (c ∨ f ∨ i)` and the three denials"],
             "c": 2,
             "why": "Drop any one sentence and a model appears, so no proper subset is inconsistent. The three denials alone are consistent, and so are the other two subsets, since each omits `j` or `j → n` and leaves the conditional satisfiable."},
            {"q": "Deleting `¬f` from the set gives which position?",
             "a": ["Coherentism", "Infinitism", "Skepticism", "Foundationalism"],
             "c": 3,
             "why": "`¬f` is the denial that an unsupported foundation is acceptable, so deleting it permits foundations. Deleting `¬c` would give coherentism, deleting `¬i` infinitism, and deleting `j` skepticism."},
            {"q": "A reader says that a circle and an infinite chain are the same complaint. How does the set show otherwise?",
             "a": ["`c` and `i` are separate sentences, and deleting `¬c` and deleting `¬i` give different models",
                   "The set has no sentence about circles",
                   "Deleting either one makes the set inconsistent",
                   "The lab reports the same witness for both"],
             "c": 0,
             "why": "The two denials are independent sentences, and the two models make different letters true. The set does have a sentence about circles, `¬c`, and deleting either denial restores consistency, so the other choices are false."},
        ],
        "mistakes": [
            ("Treating “circular” and “infinite” as the same complaint",
             "The set gives them different letters. A circle complains that a claim ends up supporting itself; an infinite chain complains that no one can ever finish giving the support. Deleting `¬c` yields a model in which `c` is true and `i` false, deleting `¬i` the other way round, and the positions that result, coherentism and infinitism, answer different objections."),
            ("Thinking the inconsistency refutes epistemology",
             "An inconsistent set says that something in it has to be given up, not which thing. The skeptic gives up `j`, the others give up a denial. The argument has no force until a reason is given for treating the six sentences as fixed, and each of the denials can be argued against."),
            ("Expecting the lab to find which position is right",
             "The lab finds models, and every deletion has one. Choosing among them depends on how costly each ending is to accept, and that is the judgement the lesson leaves open on purpose."),
        ],
        "standard": (
            "Finish when you can name the position for each deletion.",
            "You should be able to write the trilemma as a set of sentences, state its smallest inconsistent subset, and for each single deletion say which position results and which letter the lab’s model makes true."),
        "note": "The same procedure works for any philosophical puzzle that comes as a list of individually appealing claims. Write them down, ask whether they can all be true, and see which deletion you can live with.",
    },
    # ---------------------------------------------------------------- 06
    {
        "slug": "credence-and-the-dutch-book",
        "title": "Credence and the Dutch Book",
        "module": "Credence",
        "one_line": "Degrees of belief as prices of bets, and the sure loss that incoherent prices allow.",
        "summary": (
            "A credence is a degree of belief, measured by the price at which a "
            "person would buy or sell a bet that pays 1 if the event happens. "
            "Credences that break the rules of probability allow a set of bets that "
            "loses whatever happens. The lab finds the book and prints the loss."
        ),
        "key": [
            "credence: the price of a bet paying 1",
            "every credence lies between 0 and 1",
            "exclusive events: their credences add",
            "break a rule: a set of bets loses for sure",
        ],
        "key_label": "Prices, not feelings",
        "concepts_intro": (
            "The rest of the course measures belief, and the first thing to settle "
            "is what a number for a belief is and when a set of them is allowed."
        ),
        "concepts": [
            ("A credence is a price",
             "If you would pay 1/2 for a ticket that pays 1 when the coin lands "
             "heads, and would equally sell one for 1/2, then your credence in "
             "heads is 1/2."),
            ("Coherence is the absence of a sure loss",
             "A set of credences is coherent when no combination of bets at those "
             "prices loses in every outcome. The rules of probability are the "
             "conditions for that."),
            ("Coherent is not the same as reasonable",
             "A coherent set can still be absurd, such as 99/100 for heads on a "
             "fair coin and 1/100 for tails. The test catches contradictions "
             "among credences, not mistakes about the world."),
        ],
        "read_title": "A Dutch book, built by hand",
        "read_intro": "Two credences for a coin, a pair of bets, and a table that shows the loss.",
        "body": [
            ("p", "Take a coin that lands heads or tails and nothing else. "
                  "Someone gives credence `3/5` to heads and `3/5` to tails. At "
                  "their own prices they should be willing to buy a bet on heads "
                  "that pays 1 if the coin lands heads, for `3/5`, and a bet on "
                  "tails on the same terms. Together the two bets cost `6/5`."),
            ("math", [
                "outcome   bet on heads   bet on tails   net",
                "-------------------------------------------",
                "heads     +2/5           -3/5           -1/5",
                "tails     -3/5           +2/5           -1/5",
            ]),
            ("p", "Each bet pays 1 when it wins, so a winning bet leaves `1 − 3/5 = "
                  "2/5` ahead and a losing bet leaves `3/5` behind. Exactly one "
                  "bet wins in either outcome, so the net is `2/5 − 3/5 = −1/5` "
                  "whichever way the coin falls. A set of bets with a sure loss "
                  "is called a <strong>Dutch book</strong>. The lab reports "
                  "this as a loss of `1/5` per unit staked."),
            ("def", ("Coherent credences",
                     "A set of credences is <strong>coherent</strong> when it "
                     "obeys three rules: each credence lies between 0 and 1; a "
                     "certain event gets 1; and for two events that cannot both "
                     "happen, the credence in “A or B” is the sum of the credences "
                     "in A and in B.")),
            ("p", "The coin example breaks the third rule in its simplest form: "
                  "heads and tails exclude each other and exhaust the outcomes, so "
                  "their credences should sum to 1. If the "
                  "sum is below 1, as with `1/3` and `1/3`, the book runs the "
                  "other way: the person sells both bets for `2/3` in total and "
                  "pays out 1 whichever wins, losing `1/3`. The lab computes the "
                  "size of the loss as the distance of the sum from 1."),
            ("p", "The die preset breaks additivity for three events. “Even” has "
                  "credence `1/2`, “one” has `1/6`, and “even or one” also has "
                  "credence `1/2`. The first two are exclusive, so the third "
                  "should be `2/3`, and the lab finds the book that the gap of "
                  "`1/6` allows."),
            ("h3", "What credence 1/2 means"),
            ("p", "Credence `1/2` in heads is a statement of price. It is the "
                  "credence of a person who knows the coin is fair, and the same "
                  "price can come from a person who knows nothing about it. It "
                  "does not mean “no idea”, and no one could say no idea about "
                  "each face of a die by writing `1/2` for each, since six "
                  "credences of `1/2` sum to 3 and the rules require the six to "
                  "sum to 1."),
            ("p", "The Dutch book result runs one way only. If your credences "
                  "break a rule you can be exploited. If they obey the rules, the "
                  "lab finds no book, whether the credences are sensible or not. "
                  "Coherence is a necessary condition of rational credence, and "
                  "the lessons that follow add what coherence leaves out."),
        ],
        "lab": ("choicekit", {
            "mode": "credence",
            "preset": "coin",
            "presets": [
                {"id": "coin", "label": "a coin, 3/5 on each face", "kind": "space",
                 "outcomes": ["H", "T"], "probs": ["1/2", "1/2"],
                 "events": [{"name": "heads", "set": ["H"]}, {"name": "tails", "set": ["T"]}],
                 "typed": {"heads": "3/5", "tails": "3/5"}, "threshold": 1,
                 "expect": {"crBook": "loss 1/5 per unit"}},
                {"id": "die", "label": "a die, additivity broken", "kind": "space",
                 "outcomes": ["1", "2", "3", "4", "5", "6"],
                 "probs": ["1/6", "1/6", "1/6", "1/6", "1/6", "1/6"],
                 "events": [{"name": "even", "set": ["2", "4", "6"]},
                            {"name": "one", "set": ["1"]},
                            {"name": "even or one", "set": ["1", "2", "4", "6"]}],
                 "typed": {"even": "1/2", "one": "1/6", "even or one": "1/2"}, "threshold": 1,
                 "expect": {"crBook": "loss 1/6 per unit"}},
                {"id": "coherent", "label": "a coin, 1/2 on each face", "kind": "space",
                 "outcomes": ["H", "T"], "probs": ["1/2", "1/2"],
                 "events": [{"name": "heads", "set": ["H"]}, {"name": "tails", "set": ["T"]}],
                 "typed": {"heads": "1/2", "tails": "1/2"}, "threshold": 1,
                 "expect": {"crBook": "none found"}},
            ],
            "panel_title": "Type your own credences and look for a book",
            "panel_intro": "Type a credence for each event as a fraction, such as `heads=3/5 tails=3/5`. The lab checks every complementary pair and every pair of exclusive events whose union is also listed. The tile to read here is the Dutch book. The other three belong to the threshold rule of “The Lottery Paradox” and “The Preface Paradox”, and with the threshold at 1 they report that nothing is accepted.",
        }),
        "steps_title": "Checking credences for a Dutch book",
        "steps_intro": "What the lab does, in the order you can do it by hand.",
        "steps": [
            ("Write each credence as a fraction",
             "Use exact fractions. A credence of 0.6 is 3/5, and exact arithmetic "
             "keeps the loss exact too."),
            ("Check the range",
             "A credence below 0 or above 1 is already a book: someone could "
             "sell you a bet they must lose."),
            ("Pair every event with its negation",
             "Add the two credences. The distance of the sum from 1 is the loss "
             "per unit that a book on the pair can extract."),
            ("Check exclusive events against their union",
             "If A and B cannot both occur, the credence in “A or B” should equal the credence in A plus the credence in B. "
             "The gap is again the loss."),
            ("State the bets",
             "A Dutch book is a recipe: if the sum is too high, sell the bets; if "
             "too low, buy them. Write the net payoff in each outcome and check "
             "that it is the same negative number everywhere."),
        ],
        "worked": {
            "title": "Heads and tails at 3/5 each",
            "intro": ["The person buys both bets at their own prices."],
            "lines": [
                "price paid:        3/5 + 3/5 = 6/5",
                "payout, heads:     1",
                "payout, tails:     1",
                "net in each case:  1 − 6/5 = −1/5",
                "lab: loss 1/5 per unit",
            ],
            "after": [
                "Whatever the coin does the person is `1/5` poorer, and no "
                "information about the coin could change that. The fault is in "
                "the prices, not in any belief about the world.",
            ],
        },
        "quiz_title": "Prices and books",
        "quiz": [
            {"q": "Someone gives credence 3/5 to heads and 3/5 to tails and buys both bets. What is the guaranteed loss per unit?",
             "a": ["`3/5`", "`6/5`", "`1/5`", "None, because one bet always wins"],
             "c": 2,
             "why": "The two bets cost `6/5` and exactly one pays 1, so the net is `−1/5` in each outcome. The loss is not `3/5` or `6/5`, which are prices rather than losses, and the fact that one bet wins does not prevent the loss."},
            {"q": "A person gives 9/10 to heads and 1/10 to tails on a fair coin. The lab finds no Dutch book. What follows?",
             "a": ["Their credences are reasonable",
                   "Nothing about whether the credences are reasonable; the test checks only coherence",
                   "The lab is wrong, because 9/10 is too high",
                   "They must be certain of heads"],
             "c": 1,
             "why": "The two credences sum to 1 and obey the rules, so no book exists. But a credence of 9/10 in heads on a fair coin is coherent and unreasonable, and the lab cannot tell the difference."},
            {"q": "Which pair of credences for “rain” and “no rain” allows a Dutch book?",
             "a": ["`1/4` and `3/4`", "`1/3` and `1/3`", "`0` and `1`", "`1/2` and `1/2`"],
             "c": 1,
             "why": "Only `1/3` and `1/3` fails the rule that a claim and its negation sum to 1; the sum is `2/3` and the loss is `1/3` per unit. Each of the other pairs sums to exactly 1."},
        ],
        "mistakes": [
            ("Reading credence 1/2 as “I have no idea”",
             "A credence is a price, and `1/2` is a specific price: pay up to `1/2` for a bet paying 1 on heads, and equally for tails. Ignorance among the six faces of a die cannot be written as `1/2` for each, since the six sum to 3 and the lab’s rules need them to sum to 1. The same number, `1/2`, can come from knowing the coin is fair or from knowing nothing, and so the number alone does not say which."),
            ("Thinking a Dutch book shows that the credences are false",
             "It shows only that they cannot all be acted on at their own prices. The person with `3/5` on both faces has not made a mistake about the coin; they have made a mistake about each other. And a coherent person can be wrong about the coin, which the coherent preset does not rule out."),
            ("Assuming coherence is enough",
             "The rules never mention the world. A person who gives `99/100` to heads on a fair coin and `1/100` to tails passes the test. The next lessons are about how evidence is supposed to move credences, which is what coherence leaves open."),
        ],
        "standard": (
            "Finish when you can write the bets, not just say “incoherent”.",
            "You should be able to take credences over a small outcome space, check each against the rules, and for a violation write the bets that lose in every outcome and the amount lost. “Their credences do not add up” without the bets and the size of the loss is not yet the result."),
        "note": "The Dutch book argument is controversial as a foundation for probability: it supposes that credences are prices a person must honour, which real people are not forced to do. It is used here because it is exact and gives the rules a reason you can check.",
    },
]
