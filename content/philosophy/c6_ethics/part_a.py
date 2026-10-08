"""Course 6, lessons 01-06 -- metaethics in outline, and consequentialism.

The first two lessons ask what an argument from facts to a duty needs, and what
it takes for a definition of "good" to survive the cases. The next four put
numbers on consequentialism: a sum, a sum across populations, a weighted sum,
and a decision matrix with one act struck from it.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "is-and-ought",
        "title": "Is and Ought",
        "module": "Metaethics in outline",
        "one_line": "Why facts alone never deliver a duty, and what the missing premise costs.",
        "summary": (
            "An argument whose premises only describe and whose conclusion prescribes has a "
            "counterexample row, and the lab finds it. Adding a bridging premise makes the "
            "argument valid &mdash; and the work moves to that premise: what it says, who "
            "accepts it, and what it costs to assume it."
        ),
        "key": [
            "premises: facts   conclusion: an ought",
            "the row p = T, q = T, o = F refutes it",
            "add (p ∧ q) → o and it is valid",
            "the bridge is the premise to examine",
        ],
        "key_label": "A gap, and what closes it",
        "concepts_intro": (
            "Hume’s observation is about what an argument can deliver, not about what is "
            "true. The three ideas below keep those apart."
        ),
        "concepts": [
            ("A gap in vocabulary, not a verdict on morality",
             "If the conclusion says something the premises never say, validity needs "
             "a premise that connects them. An argument can lack that premise and still have "
             "a conclusion that is true. The gap is in the argument, not in the conclusion."),
            ("A bridge makes the argument valid and nothing more",
             "Add the premise that links the facts to the duty and the argument is valid. "
             "Validity says that if the premises are true the conclusion is. It does not say "
             "the new premise is true, and that is where the dispute moves."),
            ("The lab sees letters, not meanings",
             "To the lab `o` is a sentence letter. It does not know `o` is an ought; it knows "
             "that `o` appears in the conclusion and in no premise. That is the logical shape of "
             "Hume’s point, and it is all the lab can check."),
        ],
        "read_title": "From what is to what ought to be",
        "read_intro": "One argument, its counterexample row, and the premise that closes the gap.",
        "body": [
            ("def", ("The is–ought gap",
                     "An argument crosses the <strong>is–ought gap</strong> when every premise "
                     "describes how things are and the conclusion says how they ought to be. "
                     "Hume’s remark was that such arguments usually slip an “ought” in "
                     "between the last description and the conclusion without announcing it.")),
            ("p", "Take Jones, who promised to repay Smith. Let `p` be “Jones promised to "
                  "repay Smith”, `q` be “Smith has not been repaid” and `o` be “Jones ought to "
                  "repay Smith”. The argument is `p, q ∴ o`, and it sounds entirely natural."),
            ("p", "The lab builds all eight rows for `p`, `q` and `o` and finds exactly one on "
                  "which both premises are true and the conclusion is false: `p = T, q = T, "
                  "o = F`. Nothing is being claimed about Jones. The row only describes a case "
                  "in which the facts hold and the duty does not follow from them."),
            ("math", [
                "p  q  o  |  premises both true?  |  conclusion",
                "T  T  T  |  yes                  |  T",
                "T  T  F  |  yes                  |  F   (the counterexample row)",
                "any other row: a premise is false, so no refutation",
            ]),
            ("p", "It is easy to hear this as saying something stronger, so the limit of the "
                  "point is worth stating. The row does not show that `o` is false, or that "
                  "there are no duties, or that morality is opinion. It shows that these two "
                  "premises do not force this conclusion."),
            ("def", ("Bridging premise",
                     "A <strong>bridging premise</strong> is an added premise that connects the "
                     "descriptive premises to the normative conclusion. Here it is `(p ∧ q) → o`: "
                     "if Jones promised to repay and has not repaid, then Jones ought to repay.")),
            ("p", "With the bridge in place the lab finds no counterexample row. Every row that "
                  "makes `p`, `q` and the bridge true also makes `o` true, so the argument is "
                  "valid. The bridge is not a description of anyone’s behaviour. It says what "
                  "follows from the facts, and it is an ought-bearing claim."),
            ("p", "Three replies are available, and each can be put at full strength. The "
                  "moralist accepts the bridge as a moral principle, argued for on its own "
                  "grounds. Searle replies that promising is an institution: to say the words "
                  "under the right conditions is, by what the word means, to undertake an "
                  "obligation, so the bridge records a fact about the institution rather than a "
                  "moral commitment. The skeptic answers that this only relocates the bridge: why "
                  "should anyone act inside the institution at all?"),
            ("example", ("Searle’s derivation",
                         "Let `u` be “Jones uttered the words of a promise in the right "
                         "conditions”, `m` be “Jones made a promise” and `o` be “Jones ought to "
                         "repay”. The premises are `u`, `u → m` and `m → o`, and the conclusion is "
                         "`o`. The lab finds the argument valid. Whether `m → o` is a fact about "
                         "what promising is or a moral claim in disguise is exactly what the lab "
                         "cannot tell you, since both are sentence letters to it.")),
            ("p", "So the price of the bridge is threefold. It has to be argued for, because "
                  "validity gives it no support. It has to be defended for every case it covers, "
                  "not only for Jones. And it can be denied without inconsistency by someone who "
                  "grants every fact: the counterexample row is a situation in which the facts "
                  "hold and the bridge fails."),
        ],
        "lab": ("argkit", {
            "mode": "validity",
            "show": "all",
            "preset": "hume",
            "presets": [
                {"id": "hume", "label": "Hume: two facts, then an ought",
                 "premises": ["p", "q"], "conclusion": "o", "expect": {'vaVerdict': 'Invalid', 'vaCounter': '1'}},
                {"id": "bridged", "label": "The same argument with its bridge",
                 "premises": ["p", "q", "(p & q) -> o"], "conclusion": "o", "expect": {'vaVerdict': 'Valid', 'vaCounter': '0'}},
                {"id": "searle", "label": "Searle: the promising argument",
                 "premises": ["u", "u -> m", "m -> o"], "conclusion": "o", "expect": {'vaVerdict': 'Valid', 'vaCounter': '0'}},
            ],
        }),
        "steps_title": "Testing an argument across the gap",
        "steps_intro": "Five questions, in this order. The third one is a table, not a judgment.",
        "steps": [
            ("Sort the sentences",
             "Mark each premise and the conclusion as descriptive (says how things are) or "
             "normative (says how they ought to be). If the conclusion is normative and no premise "
             "is, the gap is in play."),
            ("Give each sentence its own letter",
             "Write the descriptive premises as `p`, `q` and the conclusion as `o`. The "
             "conclusion’s letter should appear in no premise; that is the formal shape of "
             "the gap."),
            ("Run the table",
             "A counterexample row, with every premise true and the conclusion false, confirms "
             "that the premises do not force the conclusion."),
            ("Write the bridge",
             "State the premise that would close the gap, usually a conditional from the facts "
             "to the duty, and check the argument is now valid."),
            ("Price the bridge",
             "Ask who would accept it and why, whether it holds in every case it covers, and "
             "whether it is itself a description or an ought. Only then decide whether to "
             "accept the conclusion."),
        ],
        "worked": {
            "title": "Jones and the debt",
            "intro": ["Formalise the argument, find the row, then close the gap and ask what "
                      "closing it cost."],
            "lines": [
                "p   Jones promised to repay Smith",
                "q   Smith has not been repaid",
                "o   Jones ought to repay Smith",
                "p, q therefore o:  invalid, row p=T q=T o=F",
                "add the bridge  (p and q) imply o",
                "p, q, bridge therefore o:  valid, no such row",
            ],
            "after": [
                "The second verdict is not an endorsement. The lab has shown that the conclusion "
                "follows if the bridge is true. Whether it is true is the question the argument "
                "was supposed to settle and has instead been rewritten to contain."
            ],
        },
        "quiz_title": "What the row shows",
        "quiz": [
            {"q": "In the first preset the lab reports one counterexample row. What does that row "
                  "establish?",
             "a": ["That Jones ought not to repay Smith",
                   "That the conclusion is false in the actual world",
                   "That the premises can be true while the conclusion is false, so they do not "
                   "force it",
                   "That at least one premise is false"],
             "c": 2,
             "why": "A counterexample row describes a possible assignment, not the actual world. "
                    "It shows that the premises leave the conclusion open. It says nothing about "
                    "whether Jones ought to repay, and the premises are not shown false either."},
            {"q": "Which of these is a bridging premise for “Ana promised to babysit tonight, so "
                  "Ana ought to babysit tonight”?",
             "a": ["Ana is able to babysit tonight",
                   "Ana promised to babysit tonight",
                   "Babysitting is a pleasant way to spend an evening",
                   "Whoever promises to do something ought to do it, other things equal"],
             "c": 3,
             "why": "Only the last connects the fact of promising to the duty. The second repeats "
                    "the premise and the first and third are further facts; none of them contains "
                    "an ought, so the row on which the facts hold and the duty fails survives."},
            {"q": "The bridged preset is valid. What has the lab verified?",
             "a": ["That the conclusion is true whenever all three premises are",
                   "That Jones ought to repay Smith",
                   "That the bridging premise is true",
                   "That the original argument was valid all along"],
             "c": 0,
             "why": "Validity is a conditional guarantee. The lab checked every row and found no "
                    "case with true premises and a false conclusion. Whether the premises are true, "
                    "the bridge included, is untouched, and the original two-premise argument "
                    "remains invalid."},
            {"q": "The Searle preset is valid. What does the dispute about it turn on?",
             "a": ["Whether the argument is valid",
                   "Whether `m → o` is a fact about what promising is or a moral claim in disguise",
                   "Whether `u` is a sentence letter",
                   "Whether the conclusion `o` appears in the premises"],
             "c": 1,
             "why": "The lab settles validity and finds it. The remaining question is the status of "
                    "the bridge `m → o`, which the lab cannot judge because it sees only letters. "
                    "The conclusion does not appear in the premises, but that is the formal gap "
                    "the bridge exists to close."},
        ],
        "mistakes": [
            ("Reading Hume as saying that moral claims are false",
             "The counterexample row `p = T, q = T, o = F` says only that these premises do not "
             "force this conclusion. With the bridge, `o` follows, and is as true as the premises "
             "are. A conclusion can be unsupported by some premises and supported by others; the "
             "gap is a fact about one argument."),
            ("Treating the bridge as a harmless extra",
             "The bridge does the work. Whoever accepts the argument has accepted it, and it is "
             "the premise a critic should look at first. An argument that quietly assumes its "
             "bridge has assumed the point at issue."),
            ("Taking “valid” as the end of the matter",
             "The Searle preset is valid and the dispute goes on, because validity does not touch "
             "the truth of `m → o`. The lab checks the step from premises to conclusion; it never "
             "checks the premises."),
        ],
        "standard": ("Finish when you can name the premise that carries the ought.",
                     "Given an argument from stated facts to a stated duty, you should be able to "
                     "classify its sentences, produce the counterexample row, write the bridging "
                     "premise that closes the gap and say in one sentence what accepting that "
                     "premise commits the arguer to."),
        "note": "The lab uses one letter for each sentence, so it cannot see inside “ought”. A "
                "stricter treatment needs a logic of obligation; “Moral Dilemmas and Deontic "
                "Consistency” later in this course uses one only as a consistency check.",
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "defining-good-and-the-open-question",
        "title": "Defining “Good” and the Open Question",
        "module": "Metaethics in outline",
        "one_line": "Testing “good = pleasant” and “good = desired” against cases, and classifying "
                    "how each fails.",
        "summary": (
            "A definition of “good” predicts, for every case you can describe, whether it is "
            "good. Write the cases as a table, evaluate a candidate definition on every row, and "
            "classify each disagreement as too broad or too narrow. The lab also searches for the "
            "short formulas that fit the cases you accept."
        ),
        "key": [
            "a definition: good ⟺ some condition holds",
            "says good, table says no: too broad",
            "says no, table says good: too narrow",
            "a fit to five cases is a candidate only",
        ],
        "key_label": "Testing a definition against cases",
        "concepts_intro": (
            "The method is the one used for any definition: propose, then try to break it with a "
            "case. The three ideas below say what counts as breaking it."
        ),
        "concepts": [
            ("A definition makes a claim about every case",
             "To say a thing is good exactly when it is pleasant is a biconditional. It is true "
             "or false of each case you can describe, so a single case where the two come apart "
             "is enough to refute it."),
            ("There are two ways to fail",
             "A definition is too broad when it counts a case good that the table says is not, "
             "and too narrow when it leaves out a case the table says is good. It can be both, and "
             "the two repairs pull in opposite directions."),
            ("The verdicts are premises",
             "The case table is judgment, not measurement. You may reject a verdict, but you then "
             "owe a reason, and the lab shows what the other cases cost you when you do."),
        ],
        "read_title": "Definitions against cases",
        "read_intro": "Four conditions, five cases, and two candidate definitions.",
        "body": [
            ("p", "G. E. Moore’s open question argument starts from a contrast. If “a bachelor "
                  "is an unmarried man” is a real definition, then asking of an unmarried man "
                  "whether he is a bachelor is a closed question: no competent speaker can "
                  "sensibly doubt it. But asking of a pleasant thing whether it is good is "
                  "open. Someone who asks it is not confused. So “good” does not simply mean "
                  "“pleasant”."),
            ("p", "The lab does not run that test. It runs the method the test motivates, which "
                  "is the method of cases: describe a case, settle its verdict before consulting "
                  "any definition, and see which definitions agree."),
            ("def", ("Definition tested by cases",
                     "A proposed definition is a formula in the conditions `P` (pleasant), `D` "
                     "(desired), `A` (authentic: the person’s beliefs about the life are "
                     "true) and `H` (harmless to others). It <strong>fits</strong> a case when the "
                     "formula is true exactly when the case is good.")),
            ("p", "Five cases, with each condition marked 1 if it holds and 0 if not, and the "
                  "verdict the case table records."),
            ("math", [
                "case                    P  D  A  H  |  verdict",
                "a good life             1  1  1  1  |  good",
                "a hard-won project      0  1  1  1  |  good",
                "the experience machine  1  1  0  1  |  not good",
                "the satisfied sadist    1  1  1  0  |  not good",
                "the unwanted cure       0  0  1  1  |  good",
            ]),
            ("p", "Test hedonism, “good = pleasant”, which is the formula `P`. It is true of the "
                  "good life, and of the experience machine and the satisfied sadist, which the "
                  "table says are not good: too broad. It is false of the hard-won project and the "
                  "unwanted cure, which the table says are good: too narrow. It fits only the "
                  "first case. The lab calls it too broad and too narrow."),
            ("p", "Desire fares differently. “Good = desired”, the formula `D`, fits the good "
                  "life and the project but is too broad on the machine and the sadist and too "
                  "narrow on the cure. A different shape of failure, from different cases."),
            ("p", "The pairs search then asks which conjunctions or disjunctions of two "
                  "conditions fit all five cases. It finds `A ∧ H`: good when the life is "
                  "authentic and harms no one. That is a candidate, and a modest one. It fits "
                  "these cases, and a sixth case could break it. A philosopher would also ask "
                  "whether it still passes the open question."),
            ("p", "What if you reject a verdict? The hedonist can say the machine life is good. "
                  "In the lab, click that verdict and change it. Hedonism then fits two cases "
                  "instead of one, and it still fails on the other three. Rejecting a verdict is "
                  "allowed, but it is a specific move with a specific price, which is what makes "
                  "it different from a shrug about taste."),
            ("p", "The limit is stated once. The lab checks formulas against the table you "
                  "give it. It does not decide which cases belong in the table, or whether "
                  "four conditions are the right ones to describe a life."),
        ],
        "lab": ("argkit", {
            "mode": "analysis",
            "search": "pairs",
            "preset": "hedonism",
            "presets": [
                {"id": "hedonism", "label": "Hedonism: good is pleasant",
                 "conditions": ["P", "D", "A", "H"], "target": "good", "definition": "P",
                 "cases": [
                     {"name": "a good life", "values": [1, 1, 1, 1], "verdict": 1},
                     {"name": "a hard-won project", "values": [0, 1, 1, 1], "verdict": 1},
                     {"name": "the experience machine", "values": [1, 1, 0, 1], "verdict": 0},
                     {"name": "the satisfied sadist", "values": [1, 1, 1, 0], "verdict": 0},
                     {"name": "the unwanted cure", "values": [0, 0, 1, 1], "verdict": 1},
                 ], "expect": {'anAgree': '1 / 5', 'anFail': 'a hard-won project: too narrow', 'anVerdict': 'Too broad and too narrow', 'anCands': '1: first A & H'}},
                {"id": "desire", "label": "Desire: good is desired",
                 "conditions": ["P", "D", "A", "H"], "target": "good", "definition": "D",
                 "cases": [
                     {"name": "a good life", "values": [1, 1, 1, 1], "verdict": 1},
                     {"name": "a hard-won project", "values": [0, 1, 1, 1], "verdict": 1},
                     {"name": "the experience machine", "values": [1, 1, 0, 1], "verdict": 0},
                     {"name": "the satisfied sadist", "values": [1, 1, 1, 0], "verdict": 0},
                     {"name": "the unwanted cure", "values": [0, 0, 1, 1], "verdict": 1},
                 ], "expect": {'anAgree': '2 / 5', 'anFail': 'the experience machine: too broad', 'anVerdict': 'Too broad and too narrow', 'anCands': '1: first A & H'}},
            ],
        }),
        "steps_title": "Testing a definition",
        "steps_intro": "Settle the cases first. A definition judged before the cases is a definition "
                       "judged on how it sounds.",
        "steps": [
            ("Write the cases as rows",
             "Choose the conditions the definition is built from and mark each case 1 or 0 on each "
             "condition. A case is one row."),
            ("Settle each verdict independently",
             "Decide whether the case is good before looking at any definition. The verdict "
             "column is your data, and it is allowed to be disputed later."),
            ("Evaluate the definition on every row",
             "Compute the formula’s value for each case and mark the rows where it differs "
             "from the verdict."),
            ("Classify each disagreement",
             "Definition says good, table says not: too broad. Definition says not, table says "
             "good: too narrow. Report the first row of each kind."),
            ("Ask what the failure shows",
             "Either revise the definition to fit the cases, or defend the verdict you are "
             "refusing. Both are legitimate; the second needs a reason beyond the definition."),
        ],
        "worked": {
            "title": "Hedonism on five cases",
            "intro": ["Evaluate the formula P on each row and compare it with the verdict."],
            "lines": [
                "case                      P   verdict  result",
                "a good life               1   good     fits",
                "a hard-won project        0   good     too narrow",
                "the experience machine    1   not      too broad",
                "the satisfied sadist      1   not      too broad",
                "the unwanted cure         0   good     too narrow",
            ],
            "after": [
                "One agreement in five, with failures in both directions. The machine is the "
                "classic case: pleasant, desired by the user, not authentic. The search finds "
                "`A ∧ H` as a fit to all five, which is why the lab reports a candidate "
                "rather than a definition."
            ],
        },
        "quiz_title": "Too broad or too narrow",
        "quiz": [
            {"q": "A definition is true of a case that the table says is not good. How is the "
                  "definition failing?",
             "a": ["It is too narrow",
                   "It is too broad",
                   "It is inconsistent",
                   "It is unsound"],
             "c": 1,
             "why": "It reaches further than the table allows, so it is too broad. Too narrow is "
                    "the opposite failure, where the definition leaves out a good case. "
                    "Inconsistency and soundness are properties of arguments and sets of "
                    "sentences, not of a definition’s fit."},
            {"q": "The pairs search finds `A ∧ H` fits all five cases. What does that "
                  "establish?",
             "a": ["That `A ∧ H` agrees with these five verdicts and may fail on a sixth case",
                   "That good means authentic and harmless",
                   "That hedonism is refuted by the search itself",
                   "That the case table is complete"],
             "c": 0,
             "why": "Fitting is relative to the table. A formula can match five cases and fail "
                    "on a sixth, and the search says nothing about whether the five cases are all "
                    "the cases there are. Hedonism is refuted by its own failures, not by the "
                    "search."},
            {"q": "A hedonist says the experience machine verdict is just taste, so it cannot "
                  "refute hedonism. What is the strongest reply?",
             "a": ["The verdict is a fact the lab has verified",
                   "A definition does not need cases, so the objection fails",
                   "Because the lab computes the verdict from the definition, the dispute cannot "
                   "arise",
                   "The verdict is a premise; the hedonist may reject it but then must call the "
                   "machine life good, and the other failures remain"],
             "c": 3,
             "why": "Verdicts are judgments, so they can be disputed. But dropping one has a "
                    "price: hedonism then agrees with two cases rather than one and still fails "
                    "three. The lab did not verify the verdict, and it does not compute verdicts "
                    "from the definition."},
            {"q": "Why does the openness of “this is pleasant, but is it good?” count against "
                  "defining good as pleasant?",
             "a": ["Because pleasant things are never good",
                   "Because open questions have no answer",
                   "If the two meant the same, the question would be as idle as asking whether an "
                   "unmarried man is a bachelor, and it is not idle",
                   "Because the lab has answered it"],
             "c": 2,
             "why": "Moore’s point is about what competent speakers can sensibly ask. The first "
                    "choice is false, since pleasant things often are good. The third is an "
                    "unrelated claim and the fourth is not what the lab does."},
        ],
        "mistakes": [
            ("Treating a counterexample to a definition as a disagreement about taste",
             "The verdict column is the data, and a disagreement is a specific dispute about one "
             "cell. Changing the machine’s verdict to good lifts hedonism from one agreement to two "
             "and leaves three failures. Rejecting a verdict is a move with a price, not an "
             "exit."),
            ("Reading a fit as the discovery of what good means",
             "A formula that matches the table is a candidate. `A ∧ H` fits five cases and the "
             "next case may break it. The search lists what the cases allow, not what “good” means."),
            ("Mixing up the two directions",
             "Ask which side the definition is on. If it says good where the table says not, it "
             "has reached too far, and the repair is a stricter condition. If it says not where "
             "the table says good, it has left something out, and the repair is a weaker one."),
        ],
        "standard": ("Finish when you can classify each failure and say which it is.",
                     "Given a definition and a table of cases, you should be able to evaluate the "
                     "definition on every row, name each disagreement as too broad or too narrow, "
                     "and say whether you would revise the definition or dispute the verdict."),
        "note": "“Defining art” is a legitimate instance of the same method, and so is defining "
                "knowledge, as in Knowledge and Evidence. What changes is the cases, not the "
                "method.",
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "utilitarianism-and-the-sum-of-welfare",
        "title": "Utilitarianism and the Sum of Welfare",
        "module": "Consequentialism",
        "one_line": "Ranking outcomes by total welfare, and what the total cannot see.",
        "summary": (
            "Utilitarianism is stated here as a rule of aggregation: add up each person’s "
            "welfare and prefer the larger total. Rank two distributions by that rule and see that "
            "the ranking ignores who gets what, including a case where two of three people are "
            "worse off."
        ),
        "key": [
            "an outcome: one welfare number per person",
            "total = x₁ + x₂ + … + xₙ, largest wins",
            "10, 10, 10 totals 30; 1, 30, 2 totals 33",
            "the total cannot see who has which number",
        ],
        "key_label": "Utilitarianism as a rule of aggregation",
        "concepts_intro": (
            "To make a moral theory computable you need two things: what it counts, and how it "
            "combines the counts. Utilitarianism supplies both in one sentence."
        ),
        "concepts": [
            ("A distribution is a list",
             "An outcome is described by one number per person, the welfare of that person’s "
             "life. The numbers are stipulated by the example; whether welfare can be measured so "
             "is a real question that the lab does not answer."),
            ("The rule is a sum",
             "Utilitarianism ranks distributions by total welfare. Add the list, compare the "
             "sums, and the larger total is the better outcome. Ties are ties."),
            ("A sum forgets order and owner",
             "Two lists with the same numbers in a different order have the same total. So the "
             "rule is indifferent to who has which welfare, and to how the welfare is spread."),
        ],
        "read_title": "Welfare as a column of numbers",
        "read_intro": "Two distributions, one rule, and what the rule does not ask.",
        "body": [
            ("def", ("Utilitarianism as aggregation",
                     "The theory ranks outcomes by <strong>total welfare</strong>, the sum of "
                     "every person’s welfare, and holds that the outcome with the larger total "
                     "is better. It is a rule that turns a distribution into one number.")),
            ("p", "Compare `A = 10, 10, 10` with `B = 1, 30, 2`, each list giving the "
                  "welfare of three people. Under `A` the total is 30. Under `B` it is 33. The "
                  "lab prints that `B` is ranked above `A`, because the larger total wins."),
            ("p", "Look at what that ranking does. Compared with `A`, the three people change "
                  "as follows."),
            ("math", [
                "person    under A   under B   change",
                "first        10        1        −9",
                "second       10       30       +20",
                "third        10        2        −8",
                "net                            +3",
            ]),
            ("p", "Two of the three people are much worse off under `B`, "
                  "and the rule prefers it. Bentham’s slogan, the greatest good of the greatest "
                  "number, makes that sound impossible, because it sounds like two aims. As a "
                  "rule of aggregation there is one: the sum. When “the greatest good” and “the "
                  "greatest number” pull apart, as they do here, the number of people helped "
                  "does not count, and Bentham himself came to drop the second clause."),
            ("example", ("A transfer",
                         "Compare `A = 5, 15` with `B = 15, 5`. The two people have swapped "
                         "welfare. Each list totals 20, so the rule calls them equal. The same "
                         "indifference covers any redistribution that leaves the sum alone, "
                         "whether it takes from the badly off to give to the well off or the "
                         "reverse.")),
            ("example", ("A sacrifice",
                         "Compare `A = 10, 10, 10` with `B = 0, 15, 16`. One person is left with "
                         "nothing, and the total rises from 30 to 31. The rule prefers `B`.")),
            ("p", "These are the cases critics press, and the replies should be heard at "
                  "full strength. A utilitarian can say that in practice resources have "
                  "diminishing returns in welfare, so sacrifices like this are rare. That is a "
                  "claim about how often the sum favours them, and it leaves the rule’s verdict "
                  "on the stated numbers where it was. Another reply accepts the verdict and "
                  "holds that intuition against it should be revised."),
            ("p", "Two of the lab’s tiles are for later. The population at `ε` is read in "
                  "“Total, Average and the Repugnant Conclusion” and the Gini coefficient in "
                  "“Priority, Equality and Levelling Down”; here the verdict and the two scores "
                  "are the whole of the rule."),
            ("p", "The next lessons keep the rule’s structure and change the part that "
                  "bothers: what is summed, how people are counted, and how heavily the worse "
                  "off are weighted. First comes the plain version, because the plain version is "
                  "the one the others are defined against."),
        ],
        "lab": ("choicekit", {
            "mode": "aggregate",
            "rule": "total",
            "preset": "equal-vs-skewed",
            "presets": [
                {"id": "equal-vs-skewed", "label": "Equal against skewed",
                 "A": [10, 10, 10], "B": [1, 30, 2], "expect": {'agVerdict': 'B ≻ A', 'agScores': '30 vs 33', 'agGini': '0 vs 58/99'}},
                {"id": "transfer", "label": "A transfer between two people",
                 "A": [5, 15], "B": [15, 5], "expect": {'agVerdict': 'A ~ B', 'agScores': '20 vs 20'}},
                {"id": "sacrifice", "label": "One person left at zero",
                 "A": [10, 10, 10], "B": [0, 15, 16], "expect": {'agVerdict': 'B ≻ A', 'agScores': '30 vs 31'}},
            ],
        }),
        "steps_title": "Ranking two outcomes by total",
        "steps_intro": "Five steps. The last one is the one that connects the arithmetic to "
                       "the objection.",
        "steps": [
            ("Write each outcome as a list",
             "One welfare number per person. Keep the people in the same order in both "
             "lists so changes can be read off."),
            ("Add each list",
             "The total is the score. Do not average, weight or sort."),
            ("Compare the totals",
             "The larger total ranks higher; equal totals tie. That is the whole of the rule."),
            ("Write the change for each person",
             "Subtract the first list from the second, person by person. The changes add up to "
             "the difference of the totals, and their signs show who gains and who loses."),
            ("Ask what the ranking ignored",
             "Check whether swapping two people’s numbers would change the verdict. It would "
             "not. Then ask whether the example is one where that matters."),
        ],
        "worked": {
            "title": "Ranking A and B",
            "intro": ["Add each list, compare, then look at the individuals."],
            "lines": [
                "A = 10, 10, 10           total 30",
                "B = 1, 30, 2             total 33",
                "total ranks B first       33 against 30",
                "changes from A to B:     −9   +20   −8     net +3",
                "worst-off person:        10 under A,  1 under B",
            ],
            "after": [
                "The rule did what it says. The ranking is correct, and the third line is where a "
                "critic starts: the person left with 1 is the price of the person with 30."
            ],
        },
        "quiz_title": "What the total sees",
        "quiz": [
            {"q": "Under total welfare, which pair of distributions is ranked as a tie?",
             "a": ["10, 10, 10 and 1, 30, 2",
                   "5, 15 and 15, 5",
                   "10, 10, 10 and 0, 15, 16",
                   "4, 4 and 3, 3, 3"],
             "c": 1,
             "why": "Both lists in the second pair total 20. The first pair totals 30 and 33, the "
                    "third 30 and 31, and the fourth 8 and 9."},
            {"q": "The rule ranks `1, 30, 2` above `10, 10, 10` although two of the three people "
                  "are worse off. Why is that consistent with the rule?",
             "a": ["The rule gives priority to the worst-off person",
                   "The rule counts how many people are better off, and one gains a lot",
                   "The rule weights each person by their Gini coefficient",
                   "The rule counts only the sum, and the sum is larger"],
             "c": 3,
             "why": "The rule is the sum and nothing else, so the 33 beats the 30. It does not "
                    "count heads, and it does not weight the worse off; the other rules in the "
                    "next lessons do that."},
            {"q": "Someone says utilitarianism aims at “the greatest good for the greatest "
                  "number”. In the skewed example, which aim does the rule actually follow?",
             "a": ["The greatest good alone, meaning the total",
                   "The greatest number alone, meaning most people better off",
                   "Both, since both rank `B` first",
                   "Neither"],
             "c": 0,
             "why": "The rule follows the total. Most people are better off under `A`, so the "
                    "greatest number points to `A` while the greatest good points to `B`, and the "
                    "rule goes with the sum."},
            {"q": "Which change to a distribution always leaves its total welfare unchanged?",
             "a": ["Giving every person one more unit",
                   "Swapping two people’s welfare",
                   "Adding a person at welfare 1",
                   "Taking one unit from the best off and giving two to the worst off"],
             "c": 1,
             "why": "A sum is the same in any order, so a swap cannot move it; that is the "
                    "transfer preset, and it is what the rule cannot see. Each of the other three "
                    "adds to the sum: one unit per person, one unit, and a net one unit."},
        ],
        "mistakes": [
            ("Reading the slogan as two separate aims",
             "“The greatest good for the greatest number” sounds like two aims, but the rule has "
             "one: the sum. In the skewed example two of three people lose and the rule still "
             "chooses `B`, so the number of people helped did not count."),
            ("Expecting the total to favour fairness",
             "The transfer preset swaps two people’s welfare and the total does not move. A sum "
             "is the same for every ordering, so it is the same whether welfare is shared or "
             "concentrated."),
            ("Reading the arithmetic as an argument for or against the theory",
             "The numbers are stipulated. Nothing here shows that anyone’s welfare is the "
             "number written, or that welfare can be added across people. The argument lives in "
             "those stipulations, not in the sum."),
        ],
        "standard": ("Finish when you can rank by total and say what the ranking ignored.",
                     "Given two distributions, you should be able to compute each total, state "
                     "the ranking, write the change for each person, and say whether the ranking "
                     "would survive swapping two people’s welfare."),
        "note": "Everything in this course assumes welfare can be put on one scale and added across "
                "people. That is a substantive assumption, and one the labs cannot check.",
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "total-average-and-the-repugnant-conclusion",
        "title": "Total, Average and the Repugnant Conclusion",
        "module": "Consequentialism",
        "one_line": "What happens to the sum when the number of people changes.",
        "summary": (
            "When outcomes contain different numbers of people, total and average welfare come "
            "apart. Compute the smallest population at a barely-worth-living welfare level that "
            "beats a flourishing one by total, state the mere addition premise behind it, and see "
            "what averaging costs instead."
        ),
        "key": [
            "ε: the welfare of a life barely worth living",
            "n·ε adds up: enough people beat any total",
            "mere addition: add lives, harm no one",
            "average: one person at 11 beats a crowd at 10",
        ],
        "key_label": "Population and the sum",
        "concepts_intro": (
            "Once the number of people can vary, “maximise welfare” stops being one instruction. "
            "Each way of making it precise has a consequence the others avoid."
        ),
        "concepts": [
            ("Population is part of the outcome",
             "An outcome now lists a number of people as well as their welfare. Total welfare "
             "rewards adding people whose lives are worth living; average welfare is unmoved by "
             "numbers and moved only by the level."),
            ("The repugnant conclusion",
             "For any flourishing population and any positive welfare level, however small, some "
             "larger population at that level has the bigger total. The lab computes the smallest "
             "such population."),
            ("Mere addition is a premise",
             "Adding people whose lives are worth living, at no cost to anyone else, does not "
             "make an outcome worse. The total accepts it. The average does not."),
        ],
        "read_title": "Adding people",
        "read_intro": "A flourishing population, a crowd at the margin, and two rules that part "
                      "company.",
        "body": [
            ("p", "Take a population of three people at welfare 10 each: `A = 10, 10, 10`. Its "
                  "total is 30 and its average is 10. Now consider a population whose members "
                  "all live at welfare `ε`, a small positive number standing for a life barely "
                  "worth living. Let `ε = 1/10`."),
            ("p", "A crowd of `n` people at `1/10` has a total of `n·(1/10)`. That exceeds 30 "
                  "once `n` is large enough, and the lab finds the least such `n`."),
            ("math", [
                "n = 300    total 30      ties with A",
                "n = 301    total 301/10  exceeds 30",
            ]),
            ("def", ("The repugnant conclusion",
                     "For every population at welfare 10 there is a population at a lower "
                     "positive welfare `ε` whose total is greater. The least size is the smallest "
                     "whole number `n` with `n·ε` greater than the total; the lab prints it as "
                     "`n*`. Here `n* = 301`.")),
            ("p", "The lab lists at most twelve people on a side, so `B` holds twelve of the "
                  "crowd as a sample and the last tile reports how many would be needed. Twelve "
                  "at `1/10` total 6/5 and lose to the three at ten; it is the 301 that win. "
                  "Under total welfare the 301 are better than the three, though every one of "
                  "them has a life of little value. That is the conclusion Parfit called "
                  "repugnant."),
            ("p", "It follows from a premise that sounds harmless."),
            ("def", ("Mere addition",
                     "Adding people whose lives are worth living, without making anyone else "
                     "worse off, does not make an outcome worse.")),
            ("p", "In the mere-addition preset, `B` is `A` plus two people at welfare 2. Total "
                  "welfare ranks `B` above `A`, 34 against 30, and agrees with the premise. "
                  "Average welfare ranks `A` above `B`, since 10 exceeds 34/5, so it "
                  "denies the premise: two new people with lives worth living made the "
                  "outcome worse."),
            ("p", "That is how averaging dodges the conclusion, and it is not free. In the "
                  "average-trap preset, `A` is one person at 11 and `B` is twelve people at "
                  "10. Total welfare prefers `B`, 120 to 11. Average welfare prefers `A`, 11 "
                  "to 10, and the same holds for a million people at 10, which the lab is "
                  "too small to list. One person at 11 is better than any crowd at 10."),
            ("p", "There is no free exit here. Accept the total’s conclusion, accept the "
                  "average’s, or look for a rule that avoids both. The next lessons tune the "
                  "weighting; none of them is announced as the answer."),
            ("p", "The scale carries a stipulation. “Barely worth living” means a welfare level "
                  "just above zero, and the computation depends on where zero lies. The lab "
                  "takes `ε` as given and cannot tell you whether a life at `ε` is worth "
                  "living."),
        ],
        "lab": ("choicekit", {
            "mode": "aggregate",
            "rule": "total",
            "preset": "repugnant",
            "presets": [
                {"id": "repugnant", "label": "Twelve at ε against three at ten",
                 "A": [10, 10, 10],
                 "B": ["1/10"] * 12, "eps": "1/10", "expect": {'agRepug': 'n* = 301', 'agVerdict': 'A ≻ B'}},
                {"id": "mere-addition", "label": "Two more people at 2",
                 "A": [10, 10, 10], "B": [10, 10, 10, 2, 2], "expect": {'agVerdict': 'B ≻ A', 'agScores': '30 vs 34'}},
                {"id": "average-trap", "label": "One at eleven, twelve at ten",
                 "A": [11], "B": [10] * 12, "expect": {'agVerdict': 'B ≻ A', 'agScores': '11 vs 120'}},
            ],
        }),
        "steps_title": "Comparing populations of different sizes",
        "steps_intro": "Five steps; the second shows where total and average disagree.",
        "steps": [
            ("Write both lists, with their sizes",
             "Count the people as well as listing them. A comparison between populations "
             "starts from different lengths."),
            ("Compute total and average",
             "The total is the sum; the average is the sum divided by the count. Compare the "
             "outcomes under each rule and see whether they agree."),
            ("Name the premise the disagreement turns on",
             "If total ranks the larger population higher and average the smaller, ask whether "
             "adding the extra people made things better or worse, and whether they harmed "
             "anyone."),
            ("Choose ε and compute n*",
             "Take the welfare of a barely worthwhile life and find the least number of people "
             "at that level whose total exceeds the flourishing population’s."),
            ("Count the cost",
             "Each rule rejects a premise. Say which premise you would give up and what you "
             "would then have to accept."),
        ],
        "worked": {
            "title": "The smallest crowd that beats three at ten",
            "intro": ["Fix ε at one tenth and find the least population whose total exceeds "
                      "30."],
            "lines": [
                "A = 10, 10, 10          total 30      average 10",
                "ε = 1/10                a life barely worth living",
                "n people at ε           total n times 1/10",
                "n = 300                 total 30       ties with A",
                "n = 301                 total 301/10   beats A",
                "so n* = 301",
            ],
            "after": [
                "Average welfare, meanwhile, ranks the 301 far below the three: 1/10 against 10. "
                "Which of those two verdicts to keep is the question the two rules are answers to."
            ],
        },
        "quiz_title": "Total, average and the crowd",
        "quiz": [
            {"q": "Compare `10, 10, 10` with `10, 10, 10, 2, 2`. Which statement is correct?",
             "a": ["Total prefers the first, average prefers the second",
                   "Total prefers the second, average prefers the first",
                   "Both prefer the second",
                   "Both prefer the first"],
             "c": 1,
             "why": "The totals are 30 and 34, so total prefers the second list. The averages "
                    "are 10 and 34/5, so average prefers the first. Adding the two people "
                    "raises one number and lowers the other."},
            {"q": "In the mere-addition preset, which rule violates the premise that adding "
                  "worthwhile lives, at no cost to anyone, does not make an outcome worse?",
             "a": ["Average",
                   "Total",
                   "Both",
                   "Neither"],
             "c": 0,
             "why": "Under average the extra two people lower the score from 10 to 34/5, so the "
                    "larger population is ranked worse. Total raises the score, and so respects "
                    "the premise."},
            {"q": "Someone says averaging avoids the repugnant conclusion at no cost. Which "
                  "result shows the cost?",
             "a": ["Average ranks a crowd at ε above three people at ten",
                   "Average cannot compare populations of different sizes",
                   "Average is indifferent between any two populations",
                   "Average ranks one person at 11 above twelve people at 10"],
             "c": 3,
             "why": "That is the average-trap preset: one person at 11 beats a crowd at 10. The "
                    "first claim is false, since a crowd at ε has a tiny average. Average can "
                    "compare sizes, and it is not indifferent."},
            {"q": "Keep A as three people at 10, but let ε be 1/5. What is the least population "
                  "at ε whose total beats A?",
             "a": ["31",
                   "150",
                   "151",
                   "301"],
             "c": 2,
             "why": "150 people at 1/5 total exactly 30, which ties; 151 total 151/5, which "
                    "exceeds it. The answer 301 belongs to ε = 1/10, and 31 forgets that each "
                    "person adds only 1/5 to the total, not a whole unit."},
        ],
        "mistakes": [
            ("Assuming averaging avoids the problem",
             "Average welfare avoids the crowd at ε, and then ranks one person at 11 above "
             "twelve at 10, and ranks two worthwhile added lives as a loss. It trades one "
             "repugnant verdict for others."),
            ("Reading the conclusion as requiring misery",
             "The people at ε have lives that are worth living, if barely. If ε were zero or "
             "negative no population would be large enough, and the lab prints a dash. The "
             "conclusion is about many small goods, not about suffering."),
            ("Treating n* as a prediction",
             "The 301 depends on the scale and on the choice of ε. Change either and the "
             "number moves. It measures what the rule commits you to, not how many people the "
             "world will contain."),
        ],
        "standard": ("Finish when you can compute n* and name the rule that blocks it.",
                     "Given a flourishing population and a welfare level ε, you should be able to "
                     "compute the least population at ε that beats it by total, state the mere "
                     "addition premise, and say which rule gives it up and what that rule then "
                     "ranks."),
        "note": "The repugnant conclusion has many proposed escapes, including critical-level "
                "views and rules that count a person’s welfare relative to how many exist. The "
                "lab compares total and average because they show the structure most clearly.",
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "priority-equality-and-levelling-down",
        "title": "Priority, Equality and Levelling Down",
        "module": "Consequentialism",
        "one_line": "Weighting the worse off, measuring inequality, and the case that separates "
                    "them.",
        "summary": (
            "A priority rule gives a gain more weight the lower the recipient starts. An equality "
            "rule looks at the spread. Compute a priority score and the Gini coefficient for two "
            "distributions, and use the levelling-down case to show that the two can disagree."
        ),
        "key": [
            "priority: a gain counts more the lower down",
            "g(x) = x up to the knee, then half",
            "Gini 0: all equal; larger: more spread",
            "levelling down: more equal, better for no one",
        ],
        "key_label": "Priority against equality",
        "concepts_intro": (
            "The sum treats a unit of welfare the same wherever it falls. Two families of "
            "views object, for different reasons, and the lab can tell them apart."
        ),
        "concepts": [
            ("Priority weights by level",
             "A prioritarian counts a gain more when the person gaining has less. The weight "
             "depends on how well off the person is in absolute terms, not on how others are "
             "doing."),
            ("Equality looks at the spread",
             "An egalitarian cares about inequality as such, which the Gini coefficient measures: "
             "0 for a perfectly equal distribution, larger as the welfare spreads."),
            ("Levelling down separates them",
             "Bringing the better off down to the level of the worse off lowers the Gini and "
             "benefits no one. Priority sees nothing gained; a rule that ranks by inequality "
             "alone sees an improvement."),
        ],
        "read_title": "Weights, spreads and the levelling-down case",
        "read_intro": "A concave weighting, a measure of inequality, and the distribution where "
                      "they come apart.",
        "body": [
            ("def", ("Prioritarian score",
                     "Choose a <strong>knee</strong>. A person’s welfare `x` counts as `x` up "
                     "to the knee and counts for only half of what lies above it, so "
                     "`g(x) = x` for `x ≤ knee` and `g(x) = knee + (x − knee)/2` above. The score "
                     "of a distribution is the sum of `g` over its people.")),
            ("p", "This is the simplest weighting that has the right shape: a unit of welfare "
                  "counts for less the more a person already has. A smoother curve would shift "
                  "the numbers and keep the structure, and the knee is a parameter to move, not a "
                  "fact."),
            ("p", "Take the priority preset, with the knee at 8, `A = 6, 14` and `B = 9, 9`. "
                  "Under `A`, `g(6) = 6` and `g(14) = 8 + 3 = 11`, a score of 17. Under `B`, "
                  "each `g(9) = 17/2`, a score of 17. The lab prints a tie, although the totals "
                  "are 20 and 18. The six counts in full; the fourteen is discounted."),
            ("def", ("Gini coefficient",
                     "The <strong>Gini coefficient</strong> is the sum of `|xᵢ − xⱼ|` over every "
                     "ordered pair of people, divided by `2·n²` times the mean. It is 0 when "
                     "everyone has the same, and grows as the welfare spreads.")),
            ("p", "For `1, 30, 2` the unordered gaps are 29, 1 and 28, so the ordered sum is "
                  "116, the divisor is `2·9·11 = 198`, and the Gini is 58/99. For `10, 10, 10` "
                  "it is 0."),
            ("p", "Before the levelling-down case, a simpler one shows what the Gini does not "
                  "measure. In the first preset, `A = 10, 10, 10` and `B = 5, 5, 5` both have "
                  "Gini 0, so a rule that ranks by inequality alone has no preference between "
                  "them. Priority prefers `A`, 27 to 15, because every person is better off. "
                  "The Gini reads the spread and is blind to the level."),
            ("p", "The levelling-down case is the one where the better off are brought down to "
                  "the worst off and no one gains. In the levelled preset, `A = 10, 2` has Gini "
                  "1/3 and `B = 2, 2` has Gini 0. Ranked by inequality alone, `B` wins. Priority "
                  "scores `A` at 11 and `B` at 4, and prefers `A`. The person at 2 is no better "
                  "off under `B`, and the person at 10 is worse off."),
            ("p", "That is the levelling-down objection. The egalitarian has replies: that "
                  "equality is one good among several, so a levelled outcome can be worse "
                  "all things considered while still better in the one respect. The lab "
                  "ranks by one thing at a time and cannot say how the respects should be "
                  "combined. What it shows is that priority and equality are different views, "
                  "even though both favour the worse off in the ordinary case."),
        ],
        "lab": ("choicekit", {
            "mode": "aggregate",
            "rule": "prioritarian",
            "preset": "levelling-down",
            "presets": [
                {"id": "levelling-down", "label": "Everyone brought down by half",
                 "A": [10, 10, 10], "B": [5, 5, 5], "knee": 8, "expect": {'agVerdict': 'A ≻ B', 'agScores': '27 vs 15', 'agGini': '0 vs 0'}},
                {"id": "levelled", "label": "Levelling down: the better off brought to the worse off",
                 "A": [10, 2], "B": [2, 2], "knee": 8, "expect": {'agVerdict': 'A ≻ B', 'agScores': '11 vs 4', 'agGini': '1/3 vs 0'}},
                {"id": "priority", "label": "A gain to the better off against a loss below",
                 "A": [6, 14], "B": [9, 9], "knee": 8, "expect": {'agVerdict': 'A ~ B', 'agScores': '17 vs 17', 'agGini': '1/5 vs 0'}},
                {"id": "gini", "label": "The Gini of a skewed distribution",
                 "A": [10, 10, 10], "B": [1, 30, 2], "knee": 8, "expect": {'agGini': '0 vs 58/99', 'agVerdict': 'A ≻ B', 'agScores': '27 vs 22'}},
            ],
        }),
        "steps_title": "Applying a priority weight and an inequality measure",
        "steps_intro": "Five steps. The last compares the two verdicts.",
        "steps": [
            ("Choose the knee",
             "State where the weighting turns. It is a parameter of the view and should be named "
             "before anything is computed."),
            ("Transform each welfare number",
             "Replace `x` by `g(x)`: unchanged up to the knee, half the excess above it."),
            ("Add the transformed numbers",
             "That sum is the score. Compare the two scores; equal scores tie."),
            ("Compute the Gini of each distribution",
             "Sum the gaps over every ordered pair, divide by `2·n²` times the mean. A zero means "
             "perfect equality."),
            ("Compare the verdicts",
             "Does the lower Gini go with the higher priority score? Where it does not, the "
             "two views disagree, and the case is a levelling-down case."),
        ],
        "worked": {
            "title": "Priority and Gini on two distributions",
            "intro": ["Knee at 8. Weight each welfare number, add, then compute the Gini."],
            "lines": [
                "knee 8:  g(x) = x up to 8, else 8 + (x - 8)/2",
                "A = 6, 14    g = 6, 11      score 17     total 20",
                "B = 9, 9     g = 17/2 each  score 17     total 18",
                "priority says a tie, 17 against 17",
                "Gini of A = 1/5       Gini of B = 0",
            ],
            "after": [
                "The two distributions are equal in priority terms and very different in spread. "
                "A rule that ranks by Gini alone would prefer `B`, and one that ranks by total "
                "would prefer `A`; priority is the position in between."
            ],
        },
        "quiz_title": "Priority or equality",
        "quiz": [
            {"q": "Which view can be made to prefer `2, 2` to `10, 2`, a distribution in which no "
                  "one gains and one person loses?",
             "a": ["Total welfare",
                   "The prioritarian score",
                   "Ranking by Gini alone",
                   "Maximin"],
             "c": 2,
             "why": "The Gini falls from 1/3 to 0, so ranking by inequality alone prefers the "
                    "levelled outcome. Total and the prioritarian score both prefer `10, 2`. "
                    "Maximin sees a worst-off of 2 in both and is indifferent."},
            {"q": "Why does the priority preset, `A = 6, 14` against `B = 9, 9` with the knee at "
                  "8, tie?",
             "a": ["Each distribution scores 17: the 6 counts in full while the 14 counts as 11",
                   "Their Gini coefficients are equal",
                   "Their totals are equal",
                   "The knee is at the mean"],
             "c": 0,
             "why": "Both scores are 17. The totals are 20 and 18, and the Ginis are 1/5 and 0, "
                    "so neither of those explains the tie. The mean of `A` is 10, not 8."},
            {"q": "Which statement is true of the first preset, `A = 10, 10, 10` against "
                  "`B = 5, 5, 5`?",
             "a": ["Total prefers `B`",
                   "Priority prefers `A`",
                   "The Gini of `B` is lower",
                   "Priority is indifferent because both are equal"],
             "c": 1,
             "why": "The prioritarian scores are 27 and 15, so `A` wins; every person has more "
                    "under `A`. The totals, 30 and 15, also prefer `A`. Both Ginis are 0, so the "
                    "third claim is false, and equality of shape does not make priority "
                    "indifferent."},
            {"q": "Move the knee from 8 to 9 in the priority preset, `A = 6, 14` against "
                  "`B = 9, 9`. What does the lab now report?",
             "a": ["Still a tie, since the knee does not enter the scores",
                   "`B ≻ A`, 18 against 35/2: the 9s now count in full and the 14 is still "
                   "discounted",
                   "`A ≻ B`, because `A` has the larger total",
                   "`A ≻ B`, 17 against 35/2"],
             "c": 1,
             "why": "With the knee at 9, `g(9) = 9`, so `B` scores 18; `g(6) = 6` and "
                    "`g(14) = 9 + 5/2 = 23/2`, so `A` scores 35/2. The knee is where the discount "
                    "begins, and moving it past 9 lifts both of `B`’s people out of the discounted "
                    "region while `A`’s 14 stays in it. The totals, 20 and 18, are not what the "
                    "rule reads."},
        ],
        "mistakes": [
            ("Treating prioritarianism as egalitarianism",
             "Priority gives weight to a person’s level, not to the gap between people. When "
             "everyone is brought down by half the Gini has no preference and priority prefers "
             "`A`; when only the better off are brought down the Gini prefers `B` and priority "
             "still prefers `A`. The views agree often and are not the same."),
            ("Reading a Gini of 0 as a good outcome",
             "The Gini measures the spread and says nothing about the level. Everyone at 5 has the "
             "same Gini as everyone at 10."),
            ("Taking the knee as a fact",
             "The knee and the half slope are parameters of this lab’s weighting. Move the knee "
             "and the tie in the priority preset moves with it; the structure of the view "
             "remains."),
        ],
        "standard": ("Finish when you can apply a weighting and a Gini and say where they differ.",
                     "Given two distributions, you should be able to compute the prioritarian "
                     "score and the Gini coefficient of each, rank them under both, and say "
                     "whether the case is one of levelling down."),
        "note": "Several variants of both views exist, including sufficientarianism, which "
                "counts only whether people fall below a threshold. The lab supports that rule "
                "too, and Justice and Collective Choice returns to it.",
    },
    # ---------------------------------------------------------------- 06
    {
        "slug": "the-trolley-problem-as-a-decision-matrix",
        "title": "The Trolley Problem as a Decision Matrix",
        "module": "Consequentialism",
        "one_line": "Two cases with the same numbers, and the constraint that separates them.",
        "summary": (
            "Lay the switch and footbridge cases out as acts against outcomes. Total welfare "
            "gives both the same recommendation because their numbers are the same. A side "
            "constraint that forbids an act removes it before the maximising, and that is the "
            "only thing that makes the recommendations differ."
        ),
        "key": [
            "acts × outcomes: divert −1, do nothing −5",
            "total welfare: take the largest payoff",
            "side constraint: delete the forbidden act",
            "then maximise over what is left",
        ],
        "key_label": "A decision matrix with a constraint",
        "concepts_intro": (
            "Decision and Rationality supplied the matrix. The new ingredient is a rule that "
            "acts before the maximising does."
        ),
        "concepts": [
            ("The matrix is the same",
             "The switch and the footbridge each offer one life against five. Written as acts "
             "against outcomes, the two cases are identical, and so is every rule that looks only "
             "at the payoffs."),
            ("A constraint removes an act",
             "A side constraint says some acts are not to be performed whatever the outcomes. "
             "The constrained rule strikes them from the table first, then maximises over the "
             "acts that remain."),
            ("The lab applies a list, not a theory",
             "Which acts are forbidden is typed by you. The lab does not know that pushing a man "
             "uses him, or that diverting does not, and it takes any list you give it."),
        ],
        "read_title": "Acts, outcomes and a forbidden list",
        "read_intro": "Three trolley cases as one table each, and one rule that changes the answer.",
        "body": [
            ("p", "In the switch case a runaway trolley will kill five people unless you pull "
                  "a lever that sends it onto a side track, where it will kill one. In the "
                  "footbridge case it will kill five unless you push a large man off a bridge "
                  "into its path, killing him. Most people say pulling the lever is permissible "
                  "and pushing the man is not."),
            ("p", "The first thing to see is that the numbers cannot account for that. Let the "
                  "payoff be minus the number of deaths and let the outcome be certain."),
            ("math", [
                "switch          certain",
                "divert           −1",
                "do nothing       −5",
                "",
                "footbridge      certain",
                "push             −1",
                "do nothing       −5",
            ]),
            ("p", "The two tables are the same table with the first act renamed. Total welfare, "
                  "maximising the payoff, says divert in the first and push in the second, and "
                  "no rule that reads only the table can say otherwise. If you judge the cases "
                  "differently, something that is not a cell in the table is carrying the "
                  "difference."),
            ("def", ("Side constraint",
                     "A <strong>side constraint</strong> is a restriction on acts that holds "
                     "whatever the outcomes. The constrained rule deletes every forbidden act "
                     "from the table and then picks the act with the best payoff among those "
                     "left.")),
            ("p", "With “do not push a man to his death as a means” on the forbidden list, the "
                  "footbridge table loses its first row and the only act left is to do nothing, "
                  "with payoff −5. The switch table has no forbidden act and its answer does not "
                  "change. The numbers were never the difference; the list was."),
            ("p", "A constraint is not a penalty. Subtract a large number from the pushing "
                  "payoff and the act sinks in the table; but a large enough gain elsewhere "
                  "brings it back, and the number can be outweighed. A constraint is applied "
                  "before any weighing, so no gain can reach it."),
            ("example", ("The loop",
                         "Suppose the side track loops back to the main one, and the trolley "
                         "will kill the five unless the one man’s body stops it. The numbers are "
                         "the same again. Whether diverting onto the loop belongs on the "
                         "forbidden list depends on whether the man is being used to stop the "
                         "trolley, and people disagree. The loop preset lists it as forbidden. "
                         "“Double Effect, Means and Side Effects” takes that question up with "
                         "a causal model.")),
            ("p", "The lab applies the list you give it, and "
                  "whether an act belongs on the list is the ethical question. It also cannot "
                  "say why a constraint should exist, or how it fares when the stakes grow "
                  "large. It shows what a constraint does to a recommendation, and no more."),
        ],
        "lab": ("choicekit", {
            "mode": "decide",
            "rule": "constrained",
            "preset": "switch",
            "presets": [
                {"id": "switch", "label": "The switch case",
                 "acts": ["divert", "do nothing"], "states": ["certain"],
                 "payoffs": [[-1], [-5]], "probs": [1], "expect": {'deChoice': 'divert', 'deValue': '−1'}},
                {"id": "footbridge", "label": "The footbridge case",
                 "acts": ["push", "do nothing"], "states": ["certain"],
                 "payoffs": [[-1], [-5]], "probs": [1], "forbidden": ["push"], "expect": {'deChoice': 'do nothing', 'deValue': '−5'}},
                {"id": "loop", "label": "The loop case",
                 "acts": ["divert to loop", "do nothing"], "states": ["certain"],
                 "payoffs": [[-1], [-5]], "probs": [1], "forbidden": ["divert to loop"],
                 "expect": {'deChoice': 'do nothing', 'deValue': '−5'}},
            ],
        }),
        "steps_title": "Running a case through the matrix",
        "steps_intro": "Five steps. Run the third before the fourth, so the constraint’s effect "
                       "is something you can see.",
        "steps": [
            ("List the acts and the outcomes",
             "Write each act you can perform as a row and each way things might go as a column. "
             "A certain outcome is one column."),
            ("Fill in the payoffs",
             "Put in the welfare of each act in each outcome. Here it is minus the number of "
             "deaths."),
            ("Apply total welfare",
             "Choose the act with the largest payoff. Record it, with its score."),
            ("Write the forbidden list",
             "Name the acts a side constraint rules out. This is a judgment the table cannot make "
             "for you."),
            ("Run the constrained rule",
             "Strike the forbidden acts, maximise over the rest, and compare with step three. A "
             "case where the answer differs is one where the constraint bites."),
        ],
        "worked": {
            "title": "Three cases, one table",
            "intro": ["The payoffs are the same in every case. Only the forbidden list changes the "
                      "recommendation."],
            "lines": [
                "switch       divert -1       do nothing -5    divert",
                "footbridge   push -1         do nothing -5    push (total)",
                "footbridge, push forbidden                    do nothing",
                "loop, divert to loop forbidden                do nothing",
            ],
            "after": [
                "Each recommendation is the best payoff among the acts allowed. In the second row "
                "nothing is forbidden and in the third the allowed set has shrunk to one act. "
                "Switch the lab’s rule to expected utility and the footbridge and loop cases "
                "move to the act they forbid, while the switch case stays where it was."
            ],
        },
        "quiz_title": "Numbers and constraints",
        "quiz": [
            {"q": "In the lab the switch and footbridge cases carry the same payoffs. What makes "
                  "the lab’s recommendation differ between them?",
             "a": ["The forbidden list",
                   "The number of people killed",
                   "The state probabilities",
                   "The order of the acts"],
             "c": 0,
             "why": "Only the footbridge preset forbids an act. The payoffs are identical, the "
                    "outcome is certain in both, and the order of the acts does not enter the "
                    "maximising."},
            {"q": "How does a side constraint differ from subtracting a large penalty from the "
                  "forbidden act’s payoff?",
             "a": ["A penalty cannot be typed into the lab",
                   "A constraint is a smaller number than a penalty",
                   "A penalty can be outweighed by a large enough gain; a constraint removes "
                   "the act before any weighing",
                   "A constraint changes the payoffs of the other acts"],
             "c": 2,
             "why": "A penalty is one more number in the table, so some gain can exceed it. A "
                    "constraint deletes the act first. Penalties can be typed in, a constraint "
                    "is not a number, and it leaves the other acts’ payoffs alone."},
            {"q": "Which presets change their recommendation when the rule is switched from "
                  "constrained to expected utility?",
             "a": ["Switch only",
                   "Footbridge only",
                   "All three",
                   "Footbridge and loop"],
             "c": 3,
             "why": "The footbridge and loop presets each forbid an act, so removing the constraint "
                    "restores it as the best-paying act. The switch preset forbids nothing and "
                    "does not move."},
            {"q": "Two people agree on the payoffs and both apply total welfare, but one says "
                  "the footbridge push is wrong. What must they add to explain the difference?",
             "a": ["A different payoff for the push",
                   "A side constraint that forbids the act",
                   "A lower probability of the five dying",
                   "A third act"],
             "c": 1,
             "why": "A different payoff would be a change of numbers, which the cases are stipulated "
                    "not to have. What the second person holds is a restriction on acts that the "
                    "table does not contain, which is a constraint."},
        ],
        "mistakes": [
            ("Thinking the two cases differ in their numbers",
             "The switch and footbridge tables are identical: one dies against five. Everything "
             "that differs between the lab’s two answers comes from the forbidden list. If you "
             "judge the cases differently, the difference lies in a rule about acts, not in a "
             "cell."),
            ("Thinking a side constraint is a very large penalty",
             "A penalty is a number and can be outweighed; a constraint is applied before the "
             "numbers are weighed. The distinction matters when the stakes rise, and it is the "
             "distinction deontologists draw."),
            ("Expecting the lab to know which acts are forbidden",
             "The lab applies the list you type. That pushing belongs on it and diverting does "
             "not is the thing in dispute, and the lab has no opinion about it."),
        ],
        "standard": ("Finish when you can name the case in which a constraint changes the answer.",
                     "Given a trolley case, you should be able to write it as a decision "
                     "matrix, apply total welfare, write the forbidden list and apply the "
                     "constrained rule, and say which cases change and why the numbers could not "
                     "have explained it."),
        "note": "Real versions of these cases rarely come with certain outcomes. A state "
                "column with probabilities makes the same structure a decision under risk, and "
                "the constrained rule treats it the same way: strike, then maximise.",
    },
]
