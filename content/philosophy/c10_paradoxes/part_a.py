"""Paradoxes and Their Exits, lessons 1-5: the anatomy of a paradox, the liar, and the infinite."""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "the-barber-and-the-anatomy-of-a-paradox",
        "title": "The Barber and the Anatomy of a Paradox",
        "module": "Method",
        "one_line": "A paradox is a valid-looking argument from plausible premises to a conclusion no one can accept, and it has three exits.",
        "summary": (
            "A paradox is an argument that looks valid, starts from premises that each look "
            "plausible, and ends where no one can stay. That definition says where the work "
            "lies: deny a premise, fault a step, or accept the conclusion. The barber's "
            "defining sentence is the cleanest case, and in every model the lab builds for it "
            "the sentence fails at the barber himself."
        ),
        "key": [
            "a paradox: valid, plausible, unacceptable",
            "exit 1: deny a premise",
            "exit 2: fault a step that only looks valid",
            "exit 3: accept the conclusion",
            "barber: b shaves x iff x does not",
            "  shave x  -- fails at x = b",
        ],
        "key_label": "Three parts to a paradox, three exits from it",
        "concepts_intro": (
            "Three ideas fix what the word means in this course. The barber is the first "
            "argument to be tested against them."
        ),
        "concepts": [
            ("A paradox is an argument",
             "It has premises, steps and a conclusion. A sentence cannot be a paradox by "
             "itself, only the argument that leads to it, and that is why a paradox can be "
             "worked on: each premise and each step can be examined."),
            ("Three features, all at once",
             "The argument looks valid, so that no case makes the premises true and the "
             "conclusion false. Each premise looks plausible when taken alone. The "
             "conclusion cannot be accepted. Remove any one feature and what is left is an "
             "ordinary refutation or an ordinary surprise."),
            ("A contradiction is the usual bad conclusion, not the only one",
             "A contradiction is a sentence false in every row of its truth table. Many "
             "paradoxes end in one, which is the clearest way for a conclusion to be "
             "unacceptable. Some end only in something absurd, and the later lessons meet "
             "those too."),
        ],
        "read_title": "Anatomy of a paradox, and the village barber",
        "read_intro": "The definition first, then the exits it implies, then the barber as the case that tests them.",
        "body": [
            ("p", "The word paradox is used for anything surprising. Here it has a narrower "
                  "meaning, and the narrowness is what makes it useful. A paradox is an "
                  "argument with three features. It looks valid: from “Validity and "
                  "Soundness”, no case makes every premise true and the conclusion false. "
                  "Each premise looks plausible when taken by itself. And the conclusion is "
                  "one that cannot be accepted. An argument that is plainly invalid has "
                  "nothing more to say for itself, and one whose conclusion is merely "
                  "unfamiliar has nothing to explain."),
            ("def", ("Paradox",
                     "A <strong>paradox</strong> is an argument that appears valid, from "
                     "premises that each appear plausible, to a conclusion that cannot be "
                     "accepted. It is the combination that creates the problem: the "
                     "argument cannot be waved away, and its conclusion cannot be kept.")),
            ("p", "Because the argument appears valid and the conclusion has to go, there "
                  "are three things to do. The <strong>first exit</strong> is to deny a "
                  "premise: one of them was not as plausible as it looked, and the reader "
                  "must say which, and why it deceived. The <strong>second exit</strong> is "
                  "to fault a step: the argument looked valid and is not, because a step "
                  "trades on an ambiguity or on a rule that fails in this setting. The "
                  "<strong>third exit</strong> is to accept the conclusion, on the ground "
                  "that it was unacceptable only because it was unfamiliar. Each lesson of "
                  "this course ends by asking which exit the best answer takes and what it "
                  "costs."),
            ("p", "The oldest tidy example is a village with a barber, and a rule about "
                  "him: the barber shaves all and only those who do not shave themselves. "
                  "Write `b` for the barber. The rule is one sentence:"),
            ("math", ["∀x (Shaves(b, x) ↔ ¬Shaves(x, x))"]),
            ("p", "Read it as saying that for every individual `x`, the barber shaves "
                  "`x` exactly when `x` does not shave `x`. It is a sentence of the kind "
                  "that “Quantifiers and Their Order” taught you to read and "
                  "“Compositional Truth Conditions” taught you to evaluate in a finite "
                  "model, and the lab below does that."),
            ("p", "Now apply the rule to the barber himself, which is allowed because "
                  "the rule is about every individual. Put `x = b`. The sentence says "
                  "that `b` shaves `b` exactly when `b` does not shave `b`. Write `s` for "
                  "&ldquo;`b` shaves `b`&rdquo;. The instance has the form `s ↔ ¬s`, and "
                  "that form is false whichever truth value `s` has. If `s` is true, the "
                  "left side is true and the right side is false. If `s` is false, the "
                  "left side is false and the right side is true. Either way the "
                  "biconditional fails."),
            ("example", ("The whole argument",
                         "Premise one: there is a barber `b` of whom the village rule is "
                         "true. Premise two: what a rule says of every individual it says "
                         "of `b`. Conclusion: `s ↔ ¬s`. The steps are valid, the second "
                         "premise is the logic of &ldquo;every&rdquo;, and the conclusion "
                         "is a contradiction. So the first premise goes.")),
            ("p", "That is exit one, and it is the cheapest exit this course will "
                  "offer. Nothing about shaving or logic is overturned. The village rule "
                  "can be written down, and it can be understood, and there is no "
                  "barber who meets it. The rule is like &ldquo;the largest whole number"
                  "&rdquo;: a description that no one satisfies, however clearly it "
                  "reads."),
            ("p", "The lab builds a model: three individuals `a`, `b` and `c`, with the "
                  "name `barber` given to `b`, and a list of who shaves whom. It "
                  "evaluates the sentence and names the first individual in the domain at "
                  "which it fails. In the first preset `a` shaves himself, `b` shaves "
                  "`c`, and `c` shaves no one, which satisfies the rule for `a` and for "
                  "`c` and leaves `b` as the failure. Edit the list and try to repair "
                  "it. Adding the pair for `b` shaving `b` never helps, "
                  "because the instance at `b` has the form `s ↔ ¬s` either way. Removing "
                  "the pair for `a` shaving `a` makes the lab name `a` first, since the "
                  "tile reports the earliest failure; `b` is still among the failures."),
            ("p", "The lab's limit should be stated plainly. It evaluates the sentence "
                  "in the models you build, and it says False in each of them. It does "
                  "not search all models. That the sentence is false in every model, of "
                  "any size, is the paragraph above: the instance at `b` has the form "
                  "`s ↔ ¬s` and no truth value for `s` makes that true. The lab shows the "
                  "instance; the argument generalises it."),
            ("p", "A change of wording changes the verdict, and the third preset shows "
                  "it. If the rule only ranges over the villagers, and the barber is not "
                  "a villager, the sentence becomes `∀x (Villager(x) → (Shaves(b, x) ↔ "
                  "¬Shaves(x, x)))`. Nothing now demands anything of `b`, there is no "
                  "instance at `b`, and the lab reports True. So the barber can exist if "
                  "he lives outside the rule. The paradoxes that follow are harder because "
                  "the premise that has to go is not so easily spared: it will be a "
                  "sentence that we can plainly write down and can plainly understand."),
        ],
        "lab": ("argkit", {
            "mode": "semantics",
            "preset": "barber",
            "presets": [
                {"id": "barber", "label": "three villagers, the barber among them",
                 "domain": ["a", "b", "c"], "names": {"barber": "b"},
                 "predicates": {"Shaves": [["a", "a"], ["b", "c"]]},
                 "sentence": "Ax (Shaves(barber, x) <-> ~Shaves(x, x))",
                 "expect": {"seValue": "False", "seWitness": "fails at x = b"}},
                {"id": "barber-two", "label": "two villagers, the barber among them",
                 "domain": ["b", "c"], "names": {"barber": "b"},
                 "predicates": {"Shaves": [["b", "c"]]},
                 "sentence": "Ax (Shaves(barber, x) <-> ~Shaves(x, x))",
                 "expect": {"seValue": "False", "seWitness": "fails at x = b"}},
                {"id": "honest-barber", "label": "the rule covers villagers only, and the barber is not one",
                 "domain": ["a", "b", "c"], "names": {"barber": "b"},
                 "predicates": {"Villager": ["a", "c"], "Shaves": [["a", "a"], ["b", "c"]]},
                 "sentence": "Ax (Villager(x) -> (Shaves(barber, x) <-> ~Shaves(x, x)))",
                 "expect": {"seValue": "True", "seWitness": "—"}},
            ],
            "panel_title": "The village rule, tested in a model you can edit",
            "panel_intro": "Each preset is a small village. The domain lists the individuals, the extension of Shaves lists who shaves whom as pairs (ab means a shaves b), and the name barber points at b. Read the value and the witness. Then try to repair the first village: add the pair bb, remove the pair bc, add the pair ba. The sentence stays False. Last, choose the third preset and see the only change that helps: a rule that does not range over the barber.",
        }),
        "steps_title": "Taking a paradox apart",
        "steps_intro": "Four moves, in this order, for any argument that seems to prove what cannot be true.",
        "steps": [
            ("Write it in standard form",
             "List the premises and the conclusion, as in “Premises, Conclusions and "
             "Standard Form”. A paradox hides in prose, and the premises are rarely all "
             "stated."),
            ("Check the steps",
             "Ask whether the conclusion follows from the premises, by a table or by an "
             "instance. If the argument is valid, the work is in the premises. If a step "
             "fails, that is exit two and the paradox was only an appearance."),
            ("Test each premise alone",
             "Ask of each premise whether it is as plausible as it looked. Mark the one "
             "that would be cheapest to give up, and write what it costs."),
            ("Name the exit and its price",
             "Say which of the three exits the best reply takes. For the barber, exit one, "
             "and the price is nothing: no one satisfied the rule."),
        ],
        "worked": {
            "title": "The village rule, instantiated at the barber",
            "intro": [
                "The rule is true of the barber, and the barber is one of the individuals "
                "it is about. Set the individual to the barber and read."
            ],
            "lines": [
                "rule: for every x, b shaves x iff x does not shave x",
                "take x to be b itself",
                "instance: b shaves b iff b does not shave b",
                "let s stand for: b shaves b",
                "the instance has the form: s iff not s",
                "s true: true iff false, so the instance is false",
                "s false: false iff true, so the instance is false",
                "no truth value for s makes the rule true of b",
                "so no b meets the rule: exit one, deny the premise",
            ],
            "after": [
                "The argument is valid at every step, and its second premise is only the "
                "logic of &ldquo;every&rdquo;. The only premise left to deny is the one "
                "that said there was such a barber, and denying it costs nothing."
            ],
        },
        "quiz_title": "Parts and exits",
        "quiz": [
            {"q": "Which of these is a paradox in the sense used in this course?",
             "a": ["A sentence that is false in every row of its truth table",
                   "An argument whose conclusion is surprising but plainly true",
                   "An argument that looks valid, from premises that each look plausible, to a conclusion that cannot be accepted",
                   "Any set of sentences that cannot all be true"],
             "c": 2,
             "why": "The third is the definition. The first is a contradiction, a "
                    "sentence and not an argument, and many a contradiction is just a "
                    "mistake with nothing plausible behind it. A surprising but true "
                    "conclusion is exit three at most, and only if the premises were "
                    "plausible. The last is an inconsistent set, which has no "
                    "plausibility requirement: {p, ¬p} is such a set and no one finds it "
                    "puzzling."},
            {"q": "The village rule says the barber shaves all and only those who do not "
                  "shave themselves. Which exit does the barber argument take?",
             "a": ["Accept the conclusion, that the barber both shaves and does not shave himself",
                   "Fault the step from the rule to its instance at the barber",
                   "Deny that the village rule can be stated at all",
                   "Deny the premise that some barber meets the rule"],
             "c": 3,
             "why": "No one meets the rule, so the premise that someone does is the one "
                    "to deny. The conclusion is a contradiction, which cannot be "
                    "accepted without giving up the logic that made it one. The step to "
                    "the instance is the logic of “every” and is valid. The rule can be "
                    "stated and understood perfectly well; it is only unsatisfiable."},
            {"q": "The lab reports False for the barber sentence in a model you built with "
                  "three villagers. What does that show on its own?",
             "a": ["The sentence is false in that model; that it is false in every model needs the instance at the barber",
                   "The village has no barber",
                   "The sentence is false in every model, because the lab searched them all",
                   "Nothing, since one model cannot make a sentence false"],
             "c": 0,
             "why": "A single model makes the sentence false in that model. The lab "
                    "does not search all models, so the third choice claims something it "
                    "did not do. A false sentence in one model does not say a barber is "
                    "missing from the village; the village in the model is the one "
                    "described. And one model is enough to show falsity there, so the "
                    "last choice is wrong; what it cannot show is falsity everywhere."},
            {"q": "The rule is changed to cover villagers only, and the barber lives "
                  "outside the village. Why does the paradox disappear?",
             "a": ["The barber now shaves himself",
                   "The rule no longer says anything about the barber, so there is no instance of the form s ↔ ¬s",
                   "The form s ↔ ¬s now has a row that makes it true",
                   "The lab cannot evaluate a rule with a restriction"],
             "c": 1,
             "why": "The restriction removes the barber from the individuals the rule "
                    "is about, so the instance at the barber is not demanded. The barber "
                    "need not shave himself, and nothing in the new rule says he does. "
                    "The form s ↔ ¬s is still false in every row, which is why the "
                    "instance had to be removed rather than repaired. The lab does "
                    "evaluate restricted rules: the third preset is one, and it reports "
                    "True."},
        ],
        "mistakes": [
            ("Treating a paradox as a contradiction",
             "A contradiction is a sentence false in every row. A paradox is an argument "
             "that ends in one, or in something equally unacceptable, from premises that "
             "looked fine. The barber sentence is not itself the paradox. The argument "
             "from &ldquo;there is a barber who meets the rule&rdquo; to `s ↔ ¬s` is, and "
             "it is worth studying because it shows that one of the premises has to go."),
            ("Hunting for a flaw in the logic of the barber",
             "The steps are valid. Instantiating a rule that is about everyone at the "
             "barber is the logic of &ldquo;every&rdquo;, and `s ↔ ¬s` is false in both "
             "rows. People who look for the trick in the word &ldquo;shaves&rdquo; are "
             "looking at the wrong place. The exit is in the premise that such a barber "
             "exists."),
            ("Reading the lab's False as a proof for all models",
             "The lab says False in the models you have built, and a model has the "
             "individuals you gave it. The general claim comes from the argument about "
             "the instance at `b`, not from running the lab more often. Say which of the "
             "two you are relying on."),
        ],
        "standard": ("Finish when you can classify an argument by its exit and refute the barber in a model.",
                     "Given a short argument, you should be able to set it out as premises "
                     "and a conclusion, say whether each of the three features of a paradox "
                     "is present, name the exit the best reply takes and what it costs. "
                     "For the barber you should be able to build a model, read the "
                     "individual at which the sentence fails, and say why no model "
                     "removes the failure."),
        "note": "The barber is a popular form of Russell's paradox, which is about the collection of all collections that are not members of themselves; the same instance with the form `s ↔ ¬s` is the heart of it. The next lesson takes the same form, `p ↔ ¬p`, and finds that its exits are much dearer, because the sentence in question is not a barber that can be quietly left out of the village.",
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "the-liar",
        "title": "The Liar",
        "module": "Method",
        "one_line": "The liar sentence yields p ↔ ¬p, which has no satisfying row, and the exit that survives is to forbid the sentence.",
        "summary": (
            "The liar sentence says of itself that it is not true. With the truth schema "
            "and the rule that every sentence is true or not true, it follows that it is "
            "true exactly when it is not. The truth table for `p ↔ ¬p` has no satisfying "
            "row, which shows that the premises cannot all hold and says nothing about "
            "which to give up. Tarski's answer is to forbid the sentence."
        ),
        "key": [
            "L: “L is not true”",
            "p stands for: L is true",
            "the schema gives  p ↔ ¬p",
            "no row makes p ↔ ¬p true",
            "Tarski's exit: no sentence says of itself",
            "  that it is not true",
        ],
        "key_label": "A sentence, three premises, no row",
        "concepts_intro": (
            "The barber could be left out of the village. The liar is a sentence "
            "we can write down, and that is what makes it harder."
        ),
        "concepts": [
            ("The liar says it is not true",
             "Let `L` be the sentence &ldquo;`L` is not true&rdquo;. It is built by "
             "ordinary grammar, with a subject that names the sentence and a predicate "
             "that denies truth of it. &ldquo;Not true&rdquo; is used, rather than "
             "&ldquo;false&rdquo;, for a reason that the lesson explains."),
            ("Three premises, one contradiction",
             "That `L` says it is not true; that a sentence is true exactly when things "
             "are as it says; and that every sentence is either true or not true. With "
             "`p` for &ldquo;`L` is true&rdquo; they yield `p ↔ ¬p`, which no row of a "
             "truth table makes true."),
            ("The table closes the easy escape",
             "&ldquo;The liar is simply false&rdquo; is a row of the table, and the table "
             "rejects it. What the table cannot do is choose among the premises, which is "
             "the work the exits are for."),
        ],
        "read_title": "The sentence that says it is not true",
        "read_intro": "The argument, the table that shows it closes, and the exit that most of the literature starts from.",
        "body": [
            ("p", "Take a sentence that talks about itself. Print the following in a box "
                  "and let `L` be the sentence in the box: &ldquo;the sentence in this "
                  "box is not true&rdquo;. Nothing in the grammar is odd, and a sentence "
                  "can refer to itself by being the sentence in a named place, as a "
                  "label on a jar can refer to the jar. Ask whether `L` is true."),
            ("ol", [
                "`L` says that `L` is not true.",
                "A sentence is true exactly when things are as it says.",
                "Every sentence is either true or not true.",
                "So `L` is true exactly when `L` is not true.",
            ]),
            ("p", "The first premise is a matter of how `L` was built. The second is the "
                  "truth schema: &ldquo;snow is white&rdquo; is true exactly when snow is "
                  "white, and the same for every sentence. The third is that there is no "
                  "third status. Let `p` stand for &ldquo;`L` is true&rdquo;. Premises one "
                  "and two give that `p` holds exactly when `L` is not true, that is, "
                  "when `¬p`. So the conclusion is the biconditional below."),
            ("math", ["p ↔ ¬p"]),
            ("p", "The lab builds its table. There are two rows, `p` true and `p` "
                  "false, and in each the biconditional is false. A sentence false in "
                  "every row is a contradiction, and this one is the form from the "
                  "barber, so the premises of the liar argument cannot all be true."),
            ("p", "The two halves can be read separately. The formula `p → ¬p` says "
                  "that if `L` is true then it is not, and it is true in exactly one row, "
                  "the row where `p` is false. The formula `¬p → p` says that if `L` is "
                  "not true then it is, and it is true in exactly one row, the one where "
                  "`p` is true. Each half is satisfiable alone, and they are satisfiable "
                  "in different rows, which is why the pair is not. The formula `p ∨ ¬p` is "
                  "true in both rows, and it is the form of the third premise: the "
                  "table gives it no trouble, and the trouble is that it cannot be kept "
                  "with the other two."),
            ("p", "This is why the common first reply fails. Someone says the liar "
                  "is simply false. That is the row where `p` is false. In that row "
                  "`L` is not true, which is exactly what `L` says, so things are as "
                  "`L` says and by the schema `L` is true. The reply starts in a row and "
                  "ends in the other. Saying it is simply true fails the same way in "
                  "reverse. The table has no row left to put the liar in."),
            ("p", "Saying the sentence is neither true nor false does not escape "
                  "either, and the wording of `L` shows why. It says it is <em>not "
                  "true</em>. If it is neither, then it is not true, which is what it "
                  "says, so things are as it says and it is true after all. A gap "
                  "between true and false is stepped around by &ldquo;not true&rdquo;, "
                  "unless the third premise is the one given up and the schema is "
                  "restricted to match."),
            ("p", "The exit that defines the field is Tarski's. A language cannot "
                  "contain its own truth predicate. The word &ldquo;true&rdquo; as "
                  "applied to sentences of one language belongs to a richer language, "
                  "which can talk about the first; to speak of the truth of sentences of "
                  "that richer language one needs a richer one still. The first premise "
                  "is where this bites: no sentence of the lower language can say of "
                  "itself that it is not true, because the lower language has no such "
                  "word. The liar is not false or gappy. It is not a sentence of any "
                  "language in the hierarchy, and the table is silent about sentences "
                  "that are never formed."),
            ("p", "The price is real and should be stated at its strongest. English has "
                  "one word &ldquo;true&rdquo;, and it is used without a subscript "
                  "about sentences that contain it. The hierarchy is a rule that "
                  "English does not follow, and its defenders say that the rule is a "
                  "repair and not a description. Two other exits are on offer. One gives "
                  "up the third premise and makes room for sentences that are neither, "
                  "at the cost of the strengthened version above. The other accepts the "
                  "conclusion, so that `L` is both true and not true; it needs a "
                  "consequence relation in which a contradiction does not entail "
                  "everything, and the lab does not implement one. Which of the three "
                  "is the least costly is the question the lesson leaves open."),
        ],
        "lab": ("truth_table", {
            "formulas": ["p <-> ~p", "p -> ~p", "~p -> p", "p | ~p"],
            "mode": "one",
            "panel_title": "The liar's biconditional, and its two halves",
            "panel_intro": "Pick the first formula, p if and only if not p, and read its column: it is false in both rows. Pick the second, p implies not p, and note the one row where it holds. Pick the third, not p implies p, and note that it holds in the other row. Last, pick the fourth, p or not p, which holds in both. That is the third premise by itself: easy to keep, impossible to keep together with the other two.",
        }),
        "steps_title": "Running the liar argument",
        "steps_intro": "Four moves. The first three are mechanical, and the fourth is where the philosophy is.",
        "steps": [
            ("Fix the sentence and name its truth",
             "Write down the sentence `L` and let `p` stand for &ldquo;`L` is true&rdquo;. "
             "The sentence says that it is not true, which is `¬p`."),
            ("Apply the truth schema",
             "A sentence is true exactly when things are as it says. For `L` that gives "
             "`p ↔ ¬p`."),
            ("Test the result by table",
             "Build the two rows. If the biconditional is false in both, the three "
             "premises cannot all hold."),
            ("Choose the premise and state the price",
             "Forbid the self-referring sentence, allow a status other than true or not "
             "true, or accept the contradiction. Whichever you pick, write what it costs "
             "and what the strengthened liar says to it."),
        ],
        "worked": {
            "title": "The liar by table",
            "intro": [
                "Let p stand for &ldquo;L is true&rdquo;. Read the two rows of the "
                "biconditional the argument ends with."
            ],
            "lines": [
                "L says: L is not true",
                "schema: L is true iff things are as L says",
                "so: p iff not p",
                "row p = T:  T iff F  is  F",
                "row p = F:  F iff T  is  F",
                "no row makes it true: the premises cannot all hold",
                "which premise to give up is the open question",
            ],
            "after": [
                "The table settles that the three premises are jointly impossible. It does "
                "not settle which is false, and each reply to the liar is an answer to "
                "that second question."
            ],
        },
        "quiz_title": "Rows and exits",
        "quiz": [
            {"q": "Someone says the liar sentence is simply false. What does the table for "
                  "p ↔ ¬p say against that?",
             "a": ["Nothing, because the table only handles true sentences",
                   "The row where p is false makes the biconditional false, so a false liar contradicts the schema",
                   "The row where p is false makes the biconditional true, so the reply is correct",
                   "A false liar is allowed, but a true liar is not"],
             "c": 1,
             "why": "In the row where p is false the biconditional is false: F ↔ T is F. "
                    "That means the liar's being not true clashes with the schema, since "
                    "its being not true is just what it says. The table handles any "
                    "sentence once its truth value is a letter. The two rows are "
                    "symmetrical, so a true liar fails in exactly the same way."},
            {"q": "In which row is p → ¬p true?",
             "a": ["Only the row where p is false",
                   "Only the row where p is true",
                   "Both rows",
                   "Neither row"],
             "c": 0,
             "why": "If p is true, the antecedent holds and the consequent ¬p fails, so "
                    "the conditional is false. If p is false, the antecedent fails and "
                    "the conditional is true. So it is true in one row only, the row "
                    "where p is false. That is why each half of the liar can be satisfied "
                    "alone and the biconditional cannot."},
            {"q": "Which premise does Tarski's exit reject?",
             "a": ["That a sentence is true exactly when things are as it says",
                   "That every sentence is true or not true",
                   "That a sentence of the language can say of itself that it is not true",
                   "That a contradiction is false in every row"],
             "c": 2,
             "why": "The hierarchy keeps the schema, for sentences at the right level, "
                    "and keeps the rule that every sentence has a status. What it "
                    "removes is the possibility of a sentence that uses the truth "
                    "predicate on itself. The last choice is the exit of accepting the "
                    "contradiction, which is a different reply."},
            {"q": "A reply says the liar is neither true nor false, and so avoids the "
                  "contradiction. Why is the liar worded with &ldquo;not true&rdquo; "
                  "rather than &ldquo;false&rdquo;?",
             "a": ["So that the sentence can be printed in a box",
                   "Because &ldquo;false&rdquo; is not a word of any language",
                   "Because &ldquo;not true&rdquo; makes the first premise false",
                   "Because a sentence that is neither is then not true, which is what it says, so it is true"],
             "c": 3,
             "why": "If the liar says it is not true and it is in the gap, it is not "
                    "true, so it says something correct, and the schema makes it true. "
                    "The wording is chosen to close that gap. Printing is irrelevant. "
                    "&ldquo;False&rdquo; is a perfectly good word. And the wording does "
                    "not touch the first premise, which is only about what the sentence "
                    "says."},
        ],
        "mistakes": [
            ("Calling the liar simply false",
             "&ldquo;Simply false&rdquo; is the row where `p` is false, and in that row "
             "`p ↔ ¬p` is false, so the liar's being not true is exactly what it "
             "says. The reply stays in one row and the argument crosses to the other. "
             "&ldquo;Simply true&rdquo; fails the same way, and the table has no "
             "row left."),
            ("Taking the table as the solution",
             "The table shows that three premises cannot all hold. A paradox is that "
             "result, and the work of the exits begins from it. Reading a contradiction "
             "as a solution is like reading the barber's `s ↔ ¬s` as an explanation of "
             "why there is no barber; it explains nothing about which premise failed."),
            ("Dismissing the sentence as meaningless",
             "It is built by ordinary grammar, and a rule that declares it meaningless "
             "needs a place to draw the line that does not also remove sentences we "
             "use. Tarski's hierarchy is such a rule, and its price is that English has "
             "one &ldquo;true&rdquo; and not a ladder of them."),
        ],
        "standard": ("Finish when you can derive the liar's biconditional, test it, and name an exit with its price.",
                     "Given the liar or a variant, you should be able to let a letter "
                     "stand for its truth, write the biconditional the schema yields, "
                     "say from a table whether any row satisfies it, and state which "
                     "premise a given reply rejects and the sentence that tests that reply."),
        "note": "The liar's form is the barber's with one difference. The barber could be refused a place in the village. The liar is a sentence on the page, and every exit has to say what is wrong with something we can read. The sorites in “Vagueness and the Sorites” is the other paradox in this Subject that cannot be quietly left out.",
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "zenos-dichotomy",
        "title": "Zeno's Dichotomy",
        "module": "The infinite",
        "one_line": "The halves of a unit distance form a geometric series whose partial sums are 1 − 1/2ⁿ and whose remainder shrinks below any bound.",
        "summary": (
            "To cross a room you must first cover half of it, then half of what is left, "
            "and so on without end. Zeno concludes that you never arrive. The steps form a "
            "geometric series, and the lab computes its partial sums exactly: after ten "
            "halves the sum is 1023/1024, 1/1024 remains, and the limit is 1. The "
            "premise to deny is that infinitely many positive times must add to infinity."
        ),
        "key": [
            "halves: 1/2 + 1/4 + 1/8 + ...",
            "after n steps the sum is 1 − 1/2^n",
            "what remains is 1/2^n",
            "the limit is 1",
            "exit: not every infinite sum is infinite",
        ],
        "key_label": "Infinitely many steps, a finite distance",
        "concepts_intro": (
            "The paradox is an argument about adding up, so the lesson computes the "
            "sums it is about."
        ),
        "concepts": [
            ("The steps form a geometric series",
             "Each step is half the one before. The first covers `1/2` of the room, the "
             "second `1/4`, the third `1/8`. A list in which each term is a fixed "
             "multiple of the last, added up, is a geometric series, with first term "
             "`a = 1/2` and ratio `r = 1/2`."),
            ("A partial sum is exact",
             "The sum of the first `n` steps is a fraction, computed exactly. The lab "
             "prints it, and prints what remains of the distance. The pattern in those "
             "fractions is what the limit is."),
            ("The limit is the number the sums settle on",
             "The limit is 1 because the remainder, `1/2^n`, falls below any fraction "
             "you name once `n` is large enough. The sums never reach 1 at a finite "
             "step, and they do not need to."),
        ],
        "read_title": "Halves that add up",
        "read_intro": "The argument, the sums that answer it, and what the answer leaves alone.",
        "body": [
            ("p", "Cross a room of length one. Before you can get all the way across "
                  "you must get halfway. Before the rest, you must cover half of what "
                  "remains, a quarter. Then an eighth, and the halving never stops, so "
                  "the crossing has infinitely many parts. Zeno's argument is that a "
                  "task with infinitely many parts cannot be finished."),
            ("ol", [
                "To cross you must complete every one of the steps: a half, a quarter, an eighth, and so on.",
                "At constant speed each step takes a positive time, a half, a quarter and an eighth of the whole crossing time.",
                "A sum of infinitely many positive times is infinite.",
                "So the crossing takes infinite time, and you never arrive.",
            ]),
            ("p", "The argument is valid, and the first two premises are as plausible as "
                  "a description of walking can be. The third is the one with a hidden "
                  "claim in it: it says that adding enough positive amounts always "
                  "passes any size. That is true of equal steps, as the next lesson "
                  "shows. Whether it is true of steps that shrink is a matter of "
                  "arithmetic."),
            ("math", [
                "1/2 + 1/4 + 1/8 + …",
                "S(n) = 1 − 1/2^n",
            ]),
            ("p", "The sum of the first `n` halves is `1 − 1/2^n`. After one step it is "
                  "`1/2`; after two, `3/4`; after three, `7/8`. The lab prints these as "
                  "exact fractions. With the first preset, ten halves, it reports the sum "
                  "`1023/1024` and the remainder `1/1024`, which is the distance still "
                  "to go. The limit tile shows `1`."),
            ("p", "What does it mean to say the infinite sum equals one, when no step "
                  "of the lab adds infinitely many numbers? It means this: whatever "
                  "small fraction you name, the remainder falls below it from some step "
                  "on. Name one thousandth. After nine steps the remainder is `1/512`, "
                  "too large; after ten it is `1/1024`, smaller than one thousandth, and "
                  "it stays smaller for every step after. Name one millionth and the "
                  "twentieth step does it. The third preset shows twenty steps: the "
                  "remainder is `1/1048576`. There is no number but 1 that the sums "
                  "approach in this way, and that is all that &ldquo;the limit "
                  "is 1&rdquo; says."),
            ("example", ("A different cut",
                         "A walker who covers two thirds of what is left at each step "
                         "has `a = 2/3` and `r = 1/3`. After five steps the sum is "
                         "`242/243` and the remainder is `1/243`. The limit is again 1. "
                         "The second preset is this walk, and a ratio of `1/3` shrinks "
                         "the remainder faster than a ratio of `1/2`.")),
            ("p", "So the third premise is false for these steps. A sum of infinitely "
                  "many positive times is not always infinite: when the times shrink in "
                  "a fixed proportion the total is finite, and here it is the whole "
                  "crossing time. The argument went wrong in saying that infinitely many "
                  "steps take infinitely long. They take exactly as long as the "
                  "crossing, because the steps are the crossing."),
            ("p", "The answer has limits and they should be stated. The arithmetic "
                  "settles the sum, and the sum was the premise at fault. It does not "
                  "settle whether space is made of points or can be divided without "
                  "end, or whether a physical body can perform a task for every one of "
                  "an unending list. Those are questions about the world and not about "
                  "the series. The next lesson takes the paradox in which the same "
                  "series appears with the speeds stated, and the lesson after that "
                  "asks what the series cannot give."),
        ],
        "lab": ("choicekit", {
            "mode": "series",
            "kind": "geometric",
            "preset": "halves",
            "presets": [
                {"id": "halves", "label": "halves, ten steps", "a": "1/2", "r": "1/2", "n": 10,
                 "expect": {"srSum": "1023/1024", "srRemain": "1/1024", "srLimit": "1"}},
                {"id": "thirds", "label": "two thirds of what is left, five steps", "a": "2/3", "r": "1/3", "n": 5,
                 "expect": {"srSum": "242/243", "srRemain": "1/243", "srLimit": "1"}},
                {"id": "twenty", "label": "halves, twenty steps", "a": "1/2", "r": "1/2", "n": 20,
                 "expect": {"srSum": "1048575/1048576", "srRemain": "1/1048576", "srLimit": "1"}},
            ],
            "panel_title": "Partial sums, exactly",
            "panel_intro": "Each preset gives the first term, the ratio and the number of steps. Read the sum of the steps taken, the limit, and the remainder, which is the limit less the sum. Slide the number of terms and watch the remainder halve each time in the first preset. Then type 2 for the ratio, so that each step is twice the last: the limit tile says none.",
        }),
        "steps_title": "Summing a geometric series",
        "steps_intro": "Four moves, in this order, for any list in which each term is a fixed multiple of the last.",
        "steps": [
            ("Find the first term and the ratio",
             "Write the first two steps. The first is `a`; the second divided by the first is "
             "`r`. For the halves, `a = 1/2` and `r = 1/2`."),
            ("Compute a partial sum",
             "The sum of the first `n` terms is `a·(1 − r^n) / (1 − r)`. For the halves "
             "it simplifies to `1 − 1/2^n`."),
            ("Read the remainder",
             "The limit less the partial sum is what is left. For the halves it is "
             "`1/2^n`, which halves with each new step."),
            ("Ask whether the remainder shrinks below every bound",
             "If the ratio is between −1 and 1, it does, and the limit is "
             "`a / (1 − r)`. If not, the sums do not settle and there is no limit."),
            ("Name the exit and its price",
             "For the dichotomy, exit one: the premise that infinitely many positive "
             "times must add to infinity is denied, and the series is the refutation. "
             "The price is a habit about adding up, and nothing about walking."),
        ],
        "worked": {
            "title": "Ten halves of a room",
            "intro": [
                "The room has length 1. The walker covers half, then half of what is "
                "left, ten times."
            ],
            "lines": [
                "a = 1/2    r = 1/2",
                "after 1 step:   1/2",
                "after 2 steps:  3/4",
                "after 3 steps:  7/8",
                "after 10 steps: 1 − 1/1024 = 1023/1024",
                "remainder after 10 steps: 1/1024",
                "limit: a / (1 − r) = (1/2) / (1/2) = 1",
            ],
            "after": [
                "Every step leaves half the previous remainder, so the remainder after "
                "`n` steps is `1/2^n`. It is under one thousandth from the tenth step on "
                "and under one millionth from the twentieth. The sums approach 1 and "
                "no other number."
            ],
        },
        "quiz_title": "Sums and remainders",
        "quiz": [
            {"q": "A walker covers half of what is left at each step, starting with half "
                  "of a unit distance. How far has she gone after five steps?",
             "a": ["5/6",
                   "5/32",
                   "1",
                   "31/32"],
             "c": 3,
             "why": "The sum of the first n halves is 1 − 1/2^n, which for n = 5 is "
                    "1 − 1/32 = 31/32. It is not 1, since no finite number of steps "
                    "reaches the limit. The fraction 5/32 comes from nothing in the "
                    "series, and 5/6 would be the sum of five terms of a different "
                    "series."},
            {"q": "Which premise of Zeno's argument does the arithmetic of the halves "
                  "show to be false?",
             "a": ["That the crossing has infinitely many parts",
                   "That a sum of infinitely many positive times is infinite",
                   "That each step takes a positive time",
                   "That the walker moves at a constant speed"],
             "c": 1,
             "why": "The halves sum to a finite total, 1, so an infinite list of "
                    "positive times need not add up to infinity. The crossing does "
                    "have infinitely many parts, by the way the halves are defined; "
                    "and each step does take positive time at a constant speed. Those "
                    "are the other premises, and the arithmetic does not touch them."},
            {"q": "After twenty halves the lab reports a remainder of 1/1048576. What "
                  "does that show about the limit?",
             "a": ["The walker has arrived",
                   "The limit is 1/1048576",
                   "The limit is not yet known",
                   "The remainder, and so the distance to the limit, is below one millionth, and it keeps shrinking"],
             "c": 3,
             "why": "The remainder is the limit less the partial sum, and it is under "
                    "one millionth because 1048576 is larger than a million; it halves "
                    "again with each further step. The walker has not arrived at any "
                    "finite step. The limit is 1, not the remainder. And the limit is "
                    "known: it is the number the remainders shrink around."},
        ],
        "mistakes": [
            ("Thinking infinitely many steps take infinitely long",
             "That holds only if the steps do not shrink. These do: each takes half the "
             "time of the one before, so the times add to the crossing time and no more. "
             "The lab shows it as a remainder, `1/2^n`, that falls below any fraction "
             "you name. The number of steps is infinite and the total is 1."),
            ("Treating a partial sum as the limit",
             "No finite number of halves reaches 1: after ten steps the sum is "
             "`1023/1024`, after twenty `1048575/1048576`. The limit is the number the "
             "sums approach, and a limit does not have to be a sum anyone completes. "
             "Confusing the two is what makes it seem that the walker must finish the "
             "list."),
            ("Reading the series as a proof about space",
             "The arithmetic removes a false premise about adding up. It does not "
             "show that space can be divided forever, or that a body can do something at "
             "each of infinitely many places. Say which of these you mean before "
             "claiming that Zeno is answered."),
        ],
        "standard": ("Finish when you can sum the halves exactly and bound the remainder.",
                     "Given the first term and ratio of a geometric series, you should "
                     "be able to compute the partial sum after a stated number of terms "
                     "as an exact fraction, state the remainder, find the number of "
                     "steps after which it is below a given fraction, and state the limit "
                     "or say that there is none."),
        "note": "The same series, with a different story around it, is the next paradox. “Achilles and the Tortoise” states the speeds and asks where the sum ends. “The St Petersburg Game” in Decision and Rationality uses a series with equal-sized terms, and shows the other side of the third premise.",
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "achilles-and-the-tortoise",
        "title": "Achilles and the Tortoise",
        "module": "The infinite",
        "one_line": "The gaps in the race form a geometric series whose ratio is the speed ratio, and the meeting point is its limit.",
        "summary": (
            "Achilles runs ten times as fast as a tortoise that has a head start. Each time "
            "he reaches where the tortoise was, it has moved on, so the gaps shrink and "
            "never reach zero. The gaps are a geometric series with ratio the speed ratio. "
            "The lab sums them and finds the limit, 1000/9, which is where Achilles passes "
            "the tortoise, and it finds no limit when the speeds are equal."
        ),
        "key": [
            "gaps: 100, 10, 1, 1/10, ...",
            "ratio r = tortoise speed / Achilles speed",
            "total run = 100 / (1 − r)",
            "r = 1/10 gives 1000/9; r = 1 gives none",
            "gaps never reach 0; their sum is finite",
        ],
        "key_label": "A race with endless gaps and a finite finish",
        "concepts_intro": (
            "The previous lesson's series returns with speeds attached. What is new is "
            "the ratio, and what it decides."
        ),
        "concepts": [
            ("Each gap is the last gap times the speed ratio",
             "While Achilles covers a gap, the tortoise covers that gap times the ratio "
             "of its speed to his. So the next gap is the last times `r`, and the gaps "
             "form a geometric series with that ratio."),
            ("The sum of the gaps is how far Achilles runs",
             "He runs each gap in turn, and the total of the gaps is the distance he "
             "has run when he draws level. If the series has a limit, that limit is "
             "the meeting point."),
            ("The ratio decides whether there is a meeting",
             "For a ratio below 1 the sum is finite, and Achilles passes the tortoise. "
             "For a ratio of 1 or more the gaps do not shrink, the series has no limit, "
             "and he never does. The paradox's form is the same in both."),
        ],
        "read_title": "The race that never seems to end",
        "read_intro": "The argument, the series of gaps, and the case in which Zeno is right.",
        "body": [
            ("p", "Achilles runs ten times as fast as a tortoise, and gives it a head "
                  "start of 100 metres. Zeno argues that Achilles can never catch it. To "
                  "pass the tortoise he must first reach the place it started, and by "
                  "then it has moved on. He must reach that place, and by then it has "
                  "moved on again. Each stage leaves a gap, and a gap that is still "
                  "positive means the tortoise is still ahead."),
            ("ol", [
                "Before Achilles passes the tortoise he must reach the place the tortoise has just left.",
                "Each time he does, the tortoise has moved on, so there is a gap that is still positive.",
                "There are infinitely many such stages, and the gap never reaches zero.",
                "So Achilles never passes the tortoise.",
            ]),
            ("p", "Premise three is true, and it is worth saying so: no stage ends with "
                  "a gap of zero. The conclusion does not follow from it, and the series "
                  "shows why. Achilles runs 100 metres while the tortoise runs 10; then he "
                  "runs 10 while it runs 1; then 1 while it runs a tenth. The gaps are "
                  "100, 10, 1 and so on, each one tenth of the last."),
            ("math", [
                "100 + 10 + 1 + 1/10 + …",
                "limit = a / (1 − r) = 100 / (1 − 1/10) = 1000/9",
            ]),
            ("p", "The ratio `r` is the tortoise's speed divided by Achilles' speed, `1/10` "
                  "here, and it is the same each stage because the speeds do not change. "
                  "The first term is the head start. The lab sums the gaps exactly. After six stages Achilles has run "
                  "`111111/1000` metres, with `1/9000` still to cover, and it reports the "
                  "limit as `1000/9` metres, a little over 111. That is the "
                  "total distance Achilles has run when he draws level, and each stage of "
                  "Zeno's argument takes place before that distance. After the last gap "
                  "of the list, which there is not, he would be past. After all of the "
                  "gaps together, which is the limit, he is level, and from there he is "
                  "past."),
            ("p", "The same figure comes from ordinary algebra. Achilles runs at 10 and "
                  "the tortoise at 1 from a start 100 ahead, so he draws level when `10·t "
                  "= 100 + t`, at `t = 100/9` seconds, having run `10·t = 1000/9` "
                  "metres. The series and the equation agree because they describe one "
                  "race. What the series adds is the diagnosis: premises one to three "
                  "describe stages that all occur before the meeting, and say nothing "
                  "about whether the meeting comes."),
            ("p", "The second preset shows how the ratio controls the limit. Achilles "
                  "runs at 10 and the tortoise at 9, so `r = 9/10`. The gaps are 100, "
                  "90, 81, which sum to 271 after three stages, and the limit is `1000`. A race that closes more slowly "
                  "takes more stages and a longer run, and still ends."),
            ("p", "The third preset is the case in which Zeno is right. If the speeds "
                  "are equal the ratio is 1, every gap is 100, and the sum of any number "
                  "of them is 100 times the number. The lab reports no limit. The "
                  "tortoise stays 100 metres ahead, and Achilles does not catch it. "
                  "The structure of the argument is unchanged. What differs is the ratio, "
                  "and so the series, and so the third premise's conclusion."),
            ("p", "Which exit is this? As the argument was set out, its three premises "
                  "are true and the conclusion does not follow from them: the move from "
                  "the third premise to the conclusion is a step that only looked valid, "
                  "which is exit two. It looked valid because it borrowed a premise that "
                  "was never written down, that a list of stages with no last member "
                  "must go on for ever, in distance as in time. Write that premise in "
                  "and the argument becomes valid, and the exit becomes the previous "
                  "lesson's: deny the added premise, and the series is the refutation. "
                  "The two descriptions are one repair. A step that fails only because "
                  "it leans on an unstated premise is faulted by stating the premise and "
                  "denying it, and which name the repair gets depends on how much of the "
                  "argument was put into standard form, which is why that is the first "
                  "move of the method. The equal-speed case is the reminder that the "
                  "denial is conditional on the ratio: at `r = 1` the unstated premise "
                  "is true of this race, and the tortoise stays ahead."),
        ],
        "lab": ("choicekit", {
            "mode": "series",
            "kind": "geometric",
            "preset": "ten-to-one",
            "presets": [
                {"id": "ten-to-one", "label": "ten to one, head start 100", "a": "100", "r": "1/10", "n": 6,
                 "expect": {"srSum": "111111/1000", "srLimit": "1000/9"}},
                {"id": "close-race", "label": "ten to nine, head start 100", "a": "100", "r": "9/10", "n": 3,
                 "expect": {"srSum": "271", "srLimit": "1000"}},
                {"id": "equal-speeds", "label": "equal speeds, head start 100", "a": "100", "r": "1", "n": 10,
                 "expect": {"srSum": "1000", "srLimit": "none"}},
            ],
            "panel_title": "The gaps of a race, summed exactly",
            "panel_intro": "The first term is the head start and the ratio is the tortoise's speed over Achilles'. Read the limit: it is the distance Achilles runs when he draws level. Move the number of terms to see how much of that distance the first few stages cover. Then change the ratio to 1/2, so that the tortoise is half as fast, and see the limit become 200. In the third preset the ratio is 1 and the limit tile reads none.",
        }),
        "steps_title": "Setting up the race as a series",
        "steps_intro": "Four moves. The setting-up is the philosophy, and the arithmetic is only the check.",
        "steps": [
            ("Write the first gap",
             "It is the head start. If Achilles runs 100 metres to reach the starting "
             "place, then `a = 100`."),
            ("Find the ratio from the speeds",
             "While Achilles runs a gap, the tortoise runs that gap times its speed over "
             "his. That fraction is `r`, and it does not change from stage to stage."),
            ("Sum the series, or find that it has no sum",
             "If `r` is below 1, the limit is `a / (1 − r)`. If `r` is 1 or more, the "
             "gaps do not shrink, and the series has no limit."),
            ("Interpret the limit",
             "A limit is the distance Achilles has run when he draws level. A series "
             "with no limit means the gap never closes."),
            ("Name the exit and its price",
             "The stated premises are true, and the step to the conclusion borrows one "
             "that is not: that a list with no last stage goes on for ever. Fault the "
             "step, or state that premise and deny it; the repair is the same, and its "
             "price is small."),
        ],
        "worked": {
            "title": "Head start 100, speeds 10 and 1",
            "intro": [
                "Achilles runs at 10 metres a second, the tortoise at 1, and the tortoise "
                "starts 100 metres ahead."
            ],
            "lines": [
                "stage 1: A runs 100, T runs 10, gap 10",
                "stage 2: A runs 10, T runs 1, gap 1",
                "stage 3: A runs 1, T runs 1/10, gap 1/10",
                "gaps: 100, 10, 1, 1/10, ...   a = 100, r = 1/10",
                "limit = 100 / (1 − 1/10) = 1000/9",
                "check: 10t = 100 + t gives t = 100/9, run = 1000/9",
            ],
            "after": [
                "The series and the equation give the same answer, as they must. Achilles "
                "passes the tortoise at `1000/9` metres from where he began, about "
                "111.1, at `100/9` seconds. Every stage of Zeno's list falls before that "
                "point."
            ],
        },
        "quiz_title": "Gaps and limits",
        "quiz": [
            {"q": "Achilles runs at 10 and the tortoise at 5, with a head start of 60. What is "
                  "the common ratio of the gaps?",
             "a": ["2",
                   "1/5",
                   "1/2",
                   "5"],
             "c": 2,
             "why": "While Achilles runs a gap, the tortoise runs that gap times 5/10, "
                    "which is 1/2. The ratio of Achilles' speed to the tortoise's is 2, "
                    "the reciprocal, and would give gaps that grow. A ratio of 1/5 or 5 "
                    "mixes the speeds with the head start or with the wrong pair."},
            {"q": "With the speeds 10 and 1 and a head start of 100, how far has Achilles "
                  "run when he draws level?",
             "a": ["100 metres, the head start",
                   "1000/9 metres",
                   "No distance, because he never draws level",
                   "1000 metres"],
             "c": 1,
             "why": "The gaps are a geometric series with first term 100 and ratio 1/10, "
                    "whose limit is 100 / (1 − 1/10) = 1000/9. The head start alone is "
                    "only the first stage. He does draw level, since the ratio is below "
                    "1. And 1000 is the answer for speeds 10 and 9, a different race."},
            {"q": "Both runners go at the same speed, and the tortoise starts 100 metres "
                  "ahead. What do the gaps and their sum show?",
             "a": ["The gaps shrink, so Achilles catches it eventually",
                   "The gaps are all 100 but sum to 100",
                   "The gaps are all zero",
                   "The gaps are all 100 and there is no limit, so Achilles never catches it"],
             "c": 3,
             "why": "At a ratio of 1 each gap is the previous one, 100, and n of them "
                    "sum to 100·n, which grows without bound; the series has no limit. "
                    "That agrees with the race: at equal speeds the gap stays 100. "
                    "Gaps that shrink need a ratio below 1. The sum cannot be 100, "
                    "since that would be a single gap."},
            {"q": "Premise three of the argument says the gap never reaches zero. What "
                  "should a reply say about it?",
             "a": ["It is true, and the conclusion does not follow from it, since the sum of the gaps is finite",
                   "It is false, since the gaps do reach zero at some stage",
                   "It is true, and so Achilles never catches the tortoise",
                   "It is meaningless, since infinitely many stages cannot be listed"],
             "c": 0,
             "why": "No stage ends with a gap of zero, so the premise is true. The "
                    "conclusion would follow only if infinitely many positive gaps "
                    "had an infinite sum, and for ratio 1/10 they do not. The "
                    "premise cannot be false by the gaps reaching zero, since each is a "
                    "tenth of a positive gap. And an infinite list is perfectly "
                    "meaningful: the series is one."},
        ],
        "mistakes": [
            ("Concluding that Achilles never catches the tortoise because the gaps never reach zero",
             "The gaps never reach zero, and that is true. What it does not give is "
             "that he never draws level. The gaps sum to `1000/9` metres, and Achilles "
             "reaches that point and goes on. The meeting is the limit of the stages, "
             "and it is not any stage. It is like the end of a road that has infinitely "
             "many milestones."),
            ("Trusting the paradox's form to decide the race",
             "The same form, the same infinite list of positive gaps, describes the "
             "equal-speed race in which the tortoise does stay ahead. The form cannot "
             "tell the two apart and the ratio can. Look at `r`, not at the number of "
             "stages."),
            ("Mixing up the two speed ratios",
             "The ratio of the series is the tortoise's speed over Achilles', which "
             "is below 1 when he is faster. Dividing the other way gives 10, a series "
             "of growing gaps, and a limit that does not exist for a race that clearly "
             "ends."),
        ],
        "standard": ("Finish when you can set up a race as a series and compute where it ends.",
                     "Given a head start and two speeds, you should be able to write the "
                     "first gap and the ratio, state the limit of the gaps as an exact "
                     "fraction or say that there is none, check it against the equation "
                     "for the meeting time, and say which exit the result takes, naming "
                     "the unstated premise it denies."),
        "note": "The race is a paradox whose exit is settled by a computation, which is unusual. The lesson that follows keeps the series and removes the speeds, and finds a case in which the sum is finite and the question being asked still has no answer.",
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "thomsons-lamp-and-supertasks",
        "title": "Thomson's Lamp and Supertasks",
        "module": "The infinite",
        "one_line": "The switching times of the lamp sum to a minute while its state alternates for ever, so the series fixes the time and not the state.",
        "summary": (
            "A lamp is switched on and off at the end of each half of the remaining minute. "
            "The times add to a finite limit, so every switch happens before the minute is "
            "up. The state after each switch alternates, so it has no limit. The series "
            "settles when the switching ends and leaves the lamp's state at that moment "
            "unfixed, because there is no last switch to fix it."
        ),
        "key": [
            "switch at 1/2, 3/4, 7/8, ... of a minute",
            "time of switch n is 1 − 1/2^n",
            "state after n: on if n odd, off if even",
            "times converge; states alternate",
            "no last switch, so no state at 1",
        ],
        "key_label": "A minute settled, a state not",
        "concepts_intro": (
            "The two earlier lessons showed that infinitely many tasks can fit in a finite "
            "time. This one asks what the world looks like when they are done."
        ),
        "concepts": [
            ("A supertask is infinitely many tasks in a finite time",
             "Each switch of the lamp is a task. They come faster and faster, so that all "
             "of them, infinitely many, are over by the end of the minute. A series of "
             "times that has a finite limit is what makes the story describable."),
            ("The time converges and the state does not",
             "The time of the `n`th switch is `1 − 1/2^n`, which approaches 1. The state "
             "after the `n`th switch is on if `n` is odd and off if `n` is even, and the "
             "sequence on, off, on, off, ... approaches no value."),
            ("There is no last switch",
             "Every switch has a successor. A rule that says what the lamp does after "
             "each switch says nothing about the lamp at the end of the minute, since "
             "that is after all the switches and not after any one of them."),
        ],
        "read_title": "A lamp that is switched infinitely often in a minute",
        "read_intro": "The story, the two sequences, and the question the story does not answer.",
        "body": [
            ("p", "A lamp starts off. After half a minute it is switched on. After a "
                  "further quarter of a minute, three quarters in all, it is switched "
                  "off. After a further eighth it is switched on, and so on, each switch "
                  "coming after half the time that remains. The minute has infinitely "
                  "many switches in it. Thomson's question is: at the end of the minute "
                  "is the lamp on or off?"),
            ("ol", [
                "At each switch the lamp changes state, from off to on or on to off.",
                "There are infinitely many switches, all over before the minute is up.",
                "At the end of the minute the lamp is on or off.",
                "It cannot be on, since every time it was switched on it was later switched off; and it cannot be off, by the same argument with the switches reversed.",
                "So at the end of the minute the lamp is neither on nor off, against the third premise.",
            ]),
            ("p", "The argument ends where no one can stay: a lamp that is neither on nor "
                  "off. Thomson drew the conclusion that the setup is impossible, which "
                  "is to deny the second premise. It is worth seeing what the setup "
                  "does and does not fix before deciding that."),
            ("p", "The lab's lamp setting shows both sequences. The switches happen at "
                  "the partial sums of the halves, so the `n`th switch is at time "
                  "`1 − 1/2^n` of the minute. After ten switches the lab reports the "
                  "time `1023/1024`, the same figure as in “Zeno's Dichotomy”. Those "
                  "times converge to 1."),
            ("math", [
                "time of switch n:  1 − 1/2^n",
                "state after switch n:  on, off, on, off, …",
            ]),
            ("p", "The second sequence is not a number that approaches anything. The "
                  "term tile shows the state after `n` switches: with ten switches it "
                  "reads off, and with eleven on. Odd gives on and even gives off, "
                  "because the lamp began off and each switch reverses it. The terms "
                  "never settle toward either, so there is no limit state in the "
                  "sense that there was a limit time. The second preset is eleven switches: "
                  "the state flips while the time moves only from `1023/1024` to "
                  "`2047/2048`."),
            ("p", "Now look at premise four. The setup supplies a state for every "
                  "moment before the end of the minute: at each time `1 − 1/2^n` there "
                  "is a definite state. It supplies none for the end of the minute, "
                  "because that moment is not the time of any switch, and the rule says "
                  "only what the lamp does at each switch. A rule about how the state "
                  "changes at each step, applied to every step, says nothing about what "
                  "follows all of them. &ldquo;Every time it was switched on it was "
                  "later switched off&rdquo; is true of every moment before the minute "
                  "and silent about the minute itself, and the fourth premise reads the "
                  "rule as if it fixed a state there."),
            ("p", "That is one way to reject Thomson's conclusion, and it is the "
                  "standard one: exit one, against the fourth premise. The story is "
                  "consistent, because its description of the lamp before the minute is "
                  "complete and consistent and does not mention the state at the minute. "
                  "Whatever the lamp is doing then, it does not violate the description. "
                  "A rule that did say, such as &ldquo;the lamp is on at the end of the "
                  "minute&rdquo;, would be a further stipulation by the one who tells the "
                  "story, and either choice is consistent with the rest. The price is "
                  "that a story can describe a lamp at every moment of a minute but one "
                  "and owe nothing about that one."),
            ("p", "The case against this reply has force too. A physical lamp has a state "
                  "at every moment, and if the setup describes a possible lamp then the "
                  "end of the minute has a state that the setup does not say. A reader "
                  "who finds that unacceptable has concluded, with Thomson, that the "
                  "story describes nothing possible. That is exit one as well, against "
                  "the second premise, and its price is saying which law forbids a body "
                  "to be switched in this way. The two replies deny different premises "
                  "and pay different prices, and the lesson's claim is the narrower one "
                  "the lab can check: the series fixes the time and not the state."),
        ],
        "lab": ("choicekit", {
            "mode": "series",
            "kind": "lamp",
            "preset": "lamp",
            "presets": [
                {"id": "lamp", "label": "ten switches", "n": 10, "expect": {"srTerm": "−1 (off)", "srSum": "1023/1024"}},
                {"id": "odd", "label": "eleven switches", "n": 11, "expect": {"srTerm": "+1 (on)", "srSum": "2047/2048"}},
                {"id": "long", "label": "thirty switches", "n": 30, "expect": {"srTerm": "−1 (off)", "srSum": "1073741823/1073741824"}},
            ],
            "panel_title": "The lamp, switch by switch",
            "panel_intro": "The term tile shows the lamp after the number of switches you set; the sum tile shows how much of the minute has passed when the last of them happens; the limit tile shows the end of the minute. Move the slider one step at a time and watch the state alternate while the sum creeps toward 1. Try thirty: the sum is within a billionth of the minute, and the state is still one of two.",
        }),
        "steps_title": "Asking what a supertask settles",
        "steps_intro": "Four moves, in this order, for any story with infinitely many steps in a finite time.",
        "steps": [
            ("Sum the times",
             "Find when the `n`th step happens, as a fraction, and its limit. If the "
             "limit is finite, every step falls before it."),
            ("Write the sequence of states",
             "Record the state after each step. Decide whether it approaches a value. "
             "An alternating sequence approaches none."),
            ("Ask whether any step is last",
             "A last step would fix the state after it. If every step has a successor, "
             "the rule that moves from step to step does not reach the limit time."),
            ("Say what is settled and what is not",
             "The time is settled by the series. The state is settled only if the "
             "story adds a rule for it, and a lab cannot add one."),
            ("Name the exit and its price",
             "Both replies are exit one. The standard reply denies that the rule fixes "
             "a state at the end of the minute, at the price of a story that is silent "
             "about one moment. Thomson denies that the switching is possible, at the "
             "price of saying what forbids it."),
        ],
        "worked": {
            "title": "Ten switches, then eleven",
            "intro": [
                "The lamp starts off. Switch `n` comes at `1 − 1/2^n` of the minute, and "
                "each switch reverses the lamp."
            ],
            "lines": [
                "switch 1 at 1/2:    on",
                "switch 2 at 3/4:    off",
                "switch 3 at 7/8:    on",
                "switch 10 at 1023/1024:  off",
                "switch 11 at 2047/2048:  on",
                "times: 1/2, 3/4, 7/8, ...  limit 1",
                "states: on, off, on, ...   no limit",
            ],
            "after": [
                "After ten switches the lamp is off and `1023/1024` of the minute has "
                "passed; after eleven it is on. The series fixes the minute and leaves "
                "the state at the end undefined, since no switch is the last one."
            ],
        },
        "quiz_title": "Times and states",
        "quiz": [
            {"q": "The lamp starts off and is switched at the end of each half of what "
                  "remains of the minute. What is its state after nine switches?",
             "a": ["Off, because the number of switches is nearly ten",
                   "Neither, because the series has not finished",
                   "Off, because the lamp began off",
                   "On, because nine is odd and each switch reverses it"],
             "c": 3,
             "why": "Each switch reverses the lamp, so odd counts leave it on and even "
                    "counts off. After any finite number of switches the state is "
                    "definite. “Nearly ten” is not a count, and beginning off only "
                    "fixes the state before the first switch. The series being "
                    "unfinished does not leave the state open at a finite step."},
            {"q": "What does the series of switching times fix?",
             "a": ["That the lamp is on at the end of the minute",
                   "When the switching ends, namely at the end of the minute, and not the state of the lamp then",
                   "That the lamp is off at the end of the minute",
                   "That the lamp must be switched an even number of times"],
             "c": 1,
             "why": "The times are 1 − 1/2^n, with limit 1, so all the switches fall "
                    "before the minute is up. Their sum says nothing about whether "
                    "the lamp is on or off then, and ‘an even number of switches’ has "
                    "no meaning for a list that has no last member."},
            {"q": "Which sequence approaches no value as the number of switches grows?",
             "a": ["The time of the nth switch",
                   "The remainder of the minute after the nth switch",
                   "The sequence on, off, on, off, ...",
                   "The sum of the first n halves"],
             "c": 2,
             "why": "The times, the remainders and the partial sums all converge, to 1, "
                    "to 0 and to 1 respectively. The states keep returning to both "
                    "values, so they do not settle toward either."},
            {"q": "A critic says the lamp must be on or off at the end of the minute, so "
                  "the story is impossible. Which premise does the standard reply deny?",
             "a": ["That the story's description of the lamp fixes its state at the end of the minute",
                   "That the switches happen at the times given",
                   "That the lamp changes state at each switch",
                   "That the minute has an end"],
             "c": 0,
             "why": "The description gives a state at every time before the end of the "
                    "minute and none at the end, so the story is silent there, and "
                    "silence is not contradiction. The reply keeps the times and the "
                    "reversals, which are what the story says, and it keeps that the "
                    "minute ends. A rival reply that holds the story to be impossible "
                    "is a different exit, with its own cost."},
        ],
        "mistakes": [
            ("Thinking a convergent series of actions has a last action",
             "The times converge to 1 and each switch has a successor, so there is no "
             "last switch. The end of the minute comes after all the switches and is "
             "the time of none of them. The lab's term tile gives the state after any "
             "chosen `n` and has no entry for the end, because there is no `n` for it."),
            ("Reading the state as the limit of the states",
             "The sum of the times has a limit and the sequence of states does not: "
             "on, off, on, off approaches nothing. Importing the limit from one "
             "sequence to the other is what makes the question look as if it had an "
             "answer."),
            ("Counting silence as a contradiction",
             "The story does not say what the lamp does at the end of the minute, and "
             "that is not the same as saying it does something impossible. Whether the "
             "silence is acceptable for a lamp that has a state at every moment is the "
             "disagreement, and it is a disagreement about what a possible lamp is."),
        ],
        "standard": ("Finish when you can separate what a supertask settles from what it leaves open.",
                     "Given a supertask, you should be able to compute the time of the "
                     "`n`th step and its limit, write the state after the `n`th step, "
                     "say whether the states converge, state which question the "
                     "story answers and which it leaves undefined, and name the premise "
                     "each reply denies."),
        "note": "The setup here is deliberately the plainest supertask. Others, which need a set-theoretic limit or an unbounded sum of utilities, are named in the course home and not built. The next three lessons leave the infinite and take up paradoxes in which every number is finite and the disagreement is still about which premise to deny.",
    },
]
