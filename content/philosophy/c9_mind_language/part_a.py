"""Course 9, lessons 01-05 -- the philosophy of mind, where it can be checked."""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "dualism-and-the-conceivability-argument",
        "title": "Dualism and the Conceivability Argument",
        "module": "Mind",
        "one_line": "Test the step from what can be conceived to what could be, in a model with and without the world that does the work.",
        "summary": (
            "The dualist argues that pain without C-fibre firing is conceivable, "
            "so possible, so pain is not the firing of C-fibres. Evaluate the "
            "identity claim as a necessity in a small possible-worlds model, with "
            "and without the one world the argument needs, and locate the step "
            "from conceivable to possible as the decision to include it."
        ),
        "key": [
            "pain is C-fibres  →  □(p ↔ c)",
            "□(p ↔ c): p ↔ c at every world seen",
            "add a world: pain, no C-fibres",
            "then □(p ↔ c) is false",
            "conceivable → possible admits the world",
        ],
        "key_label": "The argument rests on one world",
        "concepts_intro": (
            "The conceivability argument is a modal argument, and Identity, Modality "
            "and Freedom supplies its instrument. What it adds is a particular "
            "world, and a question about the right to put it in."
        ),
        "concepts": [
            ("A true identity holds at every world",
             "If pain is the firing of C-fibres, then wherever there is pain there "
             "are firing C-fibres, and the other way round, in every possible case. "
             "This is the necessity of identity, and it is what the argument's "
             "fourth step asserts. Leibniz's law, met in “Leibniz's Law and the "
             "Masked Man”, says that one thing cannot differ from itself in any "
             "property; the fourth step adds that it cannot differ from itself "
             "from one world to the next. The possible-worlds model of Identity, "
             "Modality and Freedom is the instrument that makes that claim "
             "checkable, and it is what makes the dualist's argument possible at all."),
            ("A zombie world is one more world in the model",
             "A world with pain and no C-fibre firing is not an exotic object. In a "
             "model it is a node with `p` true and `c` false. Whether such a world "
             "exists is the question; what it would do if it did is arithmetic."),
            ("Conceivable is not yet possible",
             "That a thinker can imagine a case is a fact about the thinker. That "
             "the case is a possible world is a further claim, and the argument "
             "needs it as a premise."),
        ],
        "read_title": "From conceivable pain to a false necessity",
        "read_intro": (
            "Four steps, then a model that makes the third one visible."
        ),
        "body": [
            ("def", ("Dualism",
                     "<strong>Dualism</strong> about the mind is the claim that mental "
                     "states are not identical to physical states. The version tested "
                     "here is about one pair: pain, and the firing of C-fibres in the "
                     "brain. The claim is not what pain is; it is that pain is not "
                     "that.")),
            ("p", "The conceivability argument for it has four steps, and the first "
                  "three are about what can be imagined."),
            ("ol", [
                "It is conceivable that there is pain with no C-fibre firing.",
                "Whatever is conceivable in this way is possible.",
                "So it is possible that there is pain with no C-fibre firing.",
                "If pain were identical to C-fibre firing, the two would go together "
                "in every possible case. So pain is not identical to C-fibre firing.",
            ]),
            ("p", "Let `p` say that someone is in pain and `c` that C-fibres are "
                  "firing. The identity claim, taken as a necessity, is `□(p ↔ c)`, "
                  "read &ldquo;necessarily, `p` if and only if `c`&rdquo;. In a "
                  "possible-worlds model `□A` is true at a world when `A` is true at "
                  "every world that one can see, so the necessity claim is only as "
                  "strong as the list of worlds in view."),
            ("p", "Here is the model the dualist needs. There are two worlds. The "
                  "first, `w1`, is the actual one, and it sees itself and the second."),
            ("math", [
                "world   sees     p   c",
                "-----------------------",
                "w1      w1, w2   T   T",
                "w2      none     T   F",
            ]),
            ("p", "Evaluate at `w1`. The biconditional `p ↔ c` is true at `w1`, where "
                  "both are true, and false at `w2`, where `p` is true and `c` false. "
                  "Since `w1` sees `w2`, the claim `□(p ↔ c)` is false at `w1`, and the "
                  "lab prints that value. The lab also lists the worlds where the "
                  "formula holds: only `w2`, which sees no world, so nothing there can "
                  "go wrong. Nothing in the argument turns on that."),
            ("p", "Now remove `w2`. The atoms at `w1` are what they were, the "
                  "formula is what it was, and the verdict reverses: with only `w1` "
                  "in view, `□(p ↔ c)` is true. No logic changed between the two "
                  "models. A world was added or taken away. So the work of the "
                  "argument is done by the second step, which is the licence to add "
                  "the world."),
            ("p", "The dualist can say why the licence is good. We have no access to "
                  "pain except through how it feels, and how it feels seems to leave "
                  "open whether anything is going on in the brain. The physicalist "
                  "answers with a precedent. Before the chemistry, heat without "
                  "molecular motion was just as easy to imagine, and heat is "
                  "molecular motion all the same: what was imagined was a situation "
                  "that felt like heat, not a world without heat. The dualist replies "
                  "that for pain the way it feels is the thing itself, so no such "
                  "gap between seeming and being is available. The lab cannot settle "
                  "that."),
            ("p", "The physicalist has a second place to stand, at the fourth step. "
                  "The first identity theorists held that pain is C-fibre firing as "
                  "lightning is an electrical discharge, a fact found out and not a "
                  "necessity, and a contingent identity survives the pain-only "
                  "world untouched. The argument's answer, which is Kripke's, is "
                  "that an identity between two things each named for what it is "
                  "cannot hold here and fail elsewhere, so a physicalist who grants "
                  "that must fight at the second step instead. The lab writes the "
                  "identity as a necessity because that is the form the argument "
                  "gives it, and the model with `w1` alone shows what a necessary "
                  "identity costs the physicalist: nothing, until a world is "
                  "admitted."),
            ("p", "The limit is the usual one. A model has the worlds you gave it. "
                  "Whether the pain-without-fibres world is a genuine possibility is "
                  "exactly what the second premise asserts, and the lab computes "
                  "what follows from the answer, not the answer."),
        ],
        "lab": ("argkit", {
            "mode": "kripke",
            "preset": "zombie",
            "presets": [
                {"id": "zombie", "label": "Pain and C-fibres, with a pain-only world in view",
                 "n": 2, "access": [[1, 1], [1, 2]],
                 "valuation": {"p": [1, 2], "c": [1]},
                 "formula": "[](p <-> c)", "expect": {"krValue": "False at w1", "krWorlds": "w2"}},
                {"id": "no-zombie-world", "label": "Pain and C-fibres, with no further world",
                 "n": 1, "access": [[1, 1]],
                 "valuation": {"p": [1], "c": [1]},
                 "formula": "[](p <-> c)", "expect": {"krValue": "True at w1", "krWorlds": "all"}},
            ],
            "panel_title": "The same claim, with and without one world",
            "panel_intro": (
                "The first model has a second world where `p` is true and `c` false. "
                "Read the value at the first world, then switch to the second model, "
                "which keeps only the first world, and read it again. Then try the "
                "formula on its own, without the box, in the first model."
            ),
        }),
        "steps_title": "Testing a conceivability argument",
        "steps_intro": "Five steps. The fourth is where the premise shows.",
        "steps": [
            ("Name the two sides",
             "Give the mental state one letter and the physical state another: `p` "
             "for pain, `c` for C-fibre firing."),
            ("State the identity as a necessity",
             "If the two are one thing, they go together everywhere: `□(p ↔ c)`. A "
             "mere coincidence of the two here would be `p ↔ c` and nothing more."),
            ("Write down the conceived case",
             "Add a world where `p` is true and `c` false, and decide which worlds "
             "can see it. That is the dualist's second step, drawn as a node."),
            ("Evaluate at the actual world",
             "The necessity claim holds only if the biconditional holds at every "
             "world in view. One world where it fails is enough to make it false."),
            ("Say which premise admitted the world",
             "If the verdict turns on that world, the argument turns on the claim "
             "that it is possible. Name the claim, and say what would count for or "
             "against it."),
        ],
        "worked": {
            "title": "With and without the world",
            "intro": [
                "Two models of one formula, `□(p ↔ c)`, read at the actual world "
                "`w1`.",
            ],
            "lines": [
                "model A:  w1 sees w1, w2     p: w1 w2    c: w1",
                "          p ↔ c at w1:  T     at w2:  F",
                "          □(p ↔ c) at w1:  False",
                "model B:  w1 sees w1         p: w1       c: w1",
                "          p ↔ c at w1:  T",
                "          □(p ↔ c) at w1:  True",
            ],
            "after": [
                "The only difference between the models is the second world. The "
                "dualist gets a false necessity by admitting it, and the physicalist "
                "keeps a true one by declining. What each is entitled to is the "
                "question of whether a world that can be pictured is a world that "
                "could be.",
            ],
        },
        "quiz_title": "Reading the model",
        "quiz": [
            {"q": "In the first model, why is `□(p ↔ c)` false at `w1`?",
             "a": ["Both `p` and `c` are false at `w1`",
                   "`w1` sees `w2`, where `p` is true and `c` is false",
                   "`w1` sees no world at all",
                   "The formula is false at every world of the model"],
             "c": 1,
             "why": "A box is true at a world only if the formula holds at every "
                    "world it sees, and `w1` sees `w2`, where the biconditional fails. "
                    "At `w1` itself both letters are true, so the first choice is "
                    "wrong; `w1` sees two worlds, so the third is wrong; and the "
                    "formula holds at `w2`, which sees nothing, so the fourth is wrong."},
            {"q": "The two presets differ only in whether one world is present. Which "
                  "premise of the argument does that world's presence correspond to?",
             "a": ["Identical things are necessarily identical",
                   "Someone is in pain at the actual world",
                   "C-fibres fire at the actual world",
                   "What is conceivable in this way is possible"],
             "c": 3,
             "why": "The world carries the pain-without-fibres case, and including it "
                    "is the step from conceivable to possible. The other three "
                    "choices describe things that are the same in both models: the "
                    "formula, and the letters true at `w1`."},
            {"q": "Add a third world `w3` to the first model, seen by `w1`, with `p` "
                  "and `c` both true there. What is `□(p ↔ c)` at `w1`?",
             "a": ["False, because `w2` is still in view",
                   "True, because most of the worlds in view agree",
                   "True, because `w3` outweighs `w2`",
                   "Undefined until `w3` sees a world"],
             "c": 0,
             "why": "A box needs every world in view to agree, not most of them. "
                    "`w2` is still seen from `w1` and still breaks the biconditional. "
                    "Whether `w3` sees anything has no effect on the value at `w1`."},
        ],
        "mistakes": [
            ("Treating what can be conceived as what is possible",
             "The lab shows what the step costs. With the pain-only world in the "
             "model, `□(p ↔ c)` is false; without it, the same formula over the same "
             "letters is true. The argument goes through if the world may be "
             "added, and nothing else in it does any work. "
             "Whether it may is a claim about possibility, and a claim about what "
             "someone can imagine does not decide it: heat was once imagined "
             "without molecular motion."),
            ("Reading the lab's False as a refutation of physicalism",
             "The lab computed a necessity claim in a model that already includes "
             "the world the dualist wants. It reports what follows from that model, "
             "and says nothing about whether the world exists."),
            ("Reading `□A` as `A` at the world you start from",
             "At `w1` the biconditional `p ↔ c` is true, and `□(p ↔ c)` is false. "
             "A box looks at every world in view, not only at the one you are "
             "standing on, and that is why a coincidence here is not a necessity."),
        ],
        "standard": (
            "Finish when you can say which world carries the argument.",
            "Given a pair of states and the case a dualist describes, you should be "
            "able to build the model with and without the case, evaluate the "
            "necessity claim in each, and name the premise that decides between "
            "them. An answer that stops at &ldquo;the argument is bad&rdquo; has "
            "not located anything."
        ),
        "note": (
            "Whether pain is the firing of C-fibres is not what this lesson decides. "
            "It teaches where an argument on either side has to commit itself."
        ),
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "behaviourism-and-the-turing-test",
        "title": "Behaviourism and the Turing Test",
        "module": "Mind",
        "one_line": "Treat the judge as an updater, and compute what a perfect mimic and a single tell each do to the judge's belief.",
        "summary": (
            "The Turing test replaces the question whether a machine thinks with a "
            "question about what a judge can tell. Model the judge as an updater "
            "with two hypotheses, human and machine, show that a perfect mimic "
            "gives a Bayes factor of 1 on every answer, and compute what one "
            "tell does."
        ),
        "key": [
            "judge: prior × likelihood, normalised",
            "Bayes factor = P(a | H) / P(a | ¬H)",
            "a perfect mimic: factor 1 on every answer",
            "a tell: 1/10 under human, 9/10 under machine",
            "one tell: factor 1/9",
        ],
        "key_label": "A test is evidence about who, not whether",
        "concepts_intro": (
            "Behaviourism says that being in a mental state is a matter of "
            "behaving a certain way. The Turing test turns that into a procedure, "
            "and a procedure that yields evidence can be computed."
        ),
        "concepts": [
            ("The judge updates on each answer",
             "The judge begins with some belief that the party behind the screen is "
             "human, and each answer moves it by the Bayes factor, the probability "
             "of that answer if the party is human divided by its probability if "
             "not. This is the updating of Knowledge and Evidence."),
            ("A perfect mimic gives a factor of 1",
             "If an answer is exactly as probable from the machine as from the "
             "human, it is no evidence either way. Ten such answers are ten factors "
             "of 1, and the belief ends where it began."),
            ("The hypotheses are about who, not whether",
             "The test compares &ldquo;human&rdquo; with &ldquo;machine&rdquo;. It "
             "does not compare &ldquo;thinks&rdquo; with &ldquo;does not think&rdquo;. "
             "To connect them takes a further premise, and that premise is "
             "behaviourism."),
        ],
        "read_title": "The test as a Bayes factor",
        "read_intro": (
            "Behaviourism first, then the judge as an updater, then what the "
            "numbers can and cannot be made to say."
        ),
        "body": [
            ("def", ("Behaviourism",
                     "<strong>Behaviourism</strong> about the mind is the claim that "
                     "to be in a mental state is to be disposed to behave in certain "
                     "ways. On its strongest version nothing is left over: there is "
                     "no inner fact about whether a thing thinks beyond what it would "
                     "say and do.")),
            ("p", "Turing's proposal replaces the question. A judge converses in "
                  "writing with two parties, one human and one machine, and must say "
                  "which is which. If the judge cannot do better than chance, the "
                  "machine has passed, and the question whether it thinks has been "
                  "swapped for one that can be answered. Turing himself set the "
                  "original question aside as too ill-defined to discuss. Read as a "
                  "test of thought rather than of imitation, his game is behaviourism "
                  "put to work, and that reading is the one this lesson examines."),
            ("p", "The lab models the judge as what the judge is, an updater. There "
                  "are two hypotheses about the party behind the screen, `human` and "
                  "`machine`, and each answer is data. Each hypothesis assigns a "
                  "probability to each kind of answer. Take the answers to be of two "
                  "kinds, a plain answer and a tell, an answer the machine gives "
                  "more often than a person would. A tell might be an arithmetic "
                  "result too fast, or a reply too even in tone."),
            ("math", [
                "answer   P(answer | human)   P(answer | machine)",
                "-----------------------------------------------",
                "plain    9/10                1/10",
                "tell     1/10                9/10",
            ]),
            ("p", "That is a machine with a tell. The Bayes factor of one tell for "
                  "the hypothesis `human` is `(1/10) / (9/10)`, which is `1/9`: the "
                  "answer is nine times as probable if the party is a machine. "
                  "Starting from a prior of one half, the lab reports a posterior of "
                  "`1/10` for human after the one tell."),
            ("p", "Now the perfect mimic. Give the machine the human's row: a plain "
                  "answer with probability `9/10` and a tell with probability "
                  "`1/10`, whichever party it is. Every answer, plain or tell, is "
                  "exactly as probable under one hypothesis as under the other, so "
                  "every answer has a Bayes factor of 1, and ten answers together "
                  "have a factor of 1. The posterior is the prior. The judge has "
                  "learned nothing about who is behind the screen, and that is all "
                  "that a pass is."),
            ("p", "Prior matters too. A judge who starts at `9/10` for human and "
                  "meets one tell lands at one half: the factor of `1/9` exactly "
                  "cancels the odds of nine to one. A judge who starts at one half "
                  "lands at `1/10`. The same tell is the same evidence, and it "
                  "moves different judges to different places."),
            ("p", "Two consequences for the claim that the test measures thought. A "
                  "pass is not a proof: a factor of 1 says the judge could not tell "
                  "the parties apart, which is a fact about how well the machine "
                  "imitates, and a very good imitation of a thinking person need not "
                  "think. A failure is not a disproof either: a tell shows that the "
                  "parties differ in style, and a person with an odd manner of "
                  "answering would show one too. The behaviourist closes the gap by "
                  "definition, because for the behaviourist there is nothing for "
                  "the test to miss. “The Chinese Room and the Lookup Table” shows what that costs."),
            ("p", "The limit: the probabilities in the lab are numbers someone "
                  "chose. The lab computes what a judge holding those numbers should "
                  "believe. It cannot say whether a real answer is a tell."),
        ],
        "lab": ("choicekit", {
            "mode": "update",
            "preset": "mimic",
            "presets": [
                {"id": "mimic", "label": "A machine with the human's own answers, ten answers heard",
                 "hyps": ["human", "machine"], "prior": ["1/2", "1/2"],
                 "outcomes": ["plain", "tell"],
                 "lik": [["9/10", "1/10"], ["9/10", "1/10"]],
                 "data": ["plain", "plain", "tell", "plain", "plain",
                          "plain", "tell", "plain", "plain", "plain"],
                 "payoffs": None, "expect": {"upPost": "1/2", "upBF": "1"}},
                {"id": "tell", "label": "A machine with a tell, one answer heard",
                 "hyps": ["human", "machine"], "prior": ["1/2", "1/2"],
                 "outcomes": ["plain", "tell"],
                 "lik": [["9/10", "1/10"], ["1/10", "9/10"]],
                 "data": ["tell"], "payoffs": None, "expect": {"upPost": "1/10", "upBF": "1/9"}},
                {"id": "prior-heavy", "label": "A judge nine-tenths sure of a human, one tell heard",
                 "hyps": ["human", "machine"], "prior": ["9/10", "1/10"],
                 "outcomes": ["plain", "tell"],
                 "lik": [["9/10", "1/10"], ["1/10", "9/10"]],
                 "data": ["tell"], "payoffs": None, "expect": {"upPost": "1/2", "upBF": "1/9"}},
            ],
            "panel_title": "What the judge should believe",
            "panel_intro": (
                "The tiles report the hypothesis human. In the first preset the two "
                "likelihood rows are the same, so change the answers heard and watch "
                "the posterior stay put. Then change one entry of the machine's row "
                "and see how far a single answer now moves the judge."
            ),
        }),
        "steps_title": "Computing what a test shows",
        "steps_intro": "Five steps. The fourth is the one a quick reading skips.",
        "steps": [
            ("Name the two hypotheses",
             "State them as who is behind the screen: human and machine. Do not "
             "state them as thinks and does not think. Those are different "
             "hypotheses, and the test only reaches the first pair."),
            ("Give each hypothesis a row of likelihoods",
             "For each kind of answer, say how probable it is if the party is human "
             "and how probable if a machine. Each row must sum to 1."),
            ("Enter the prior and the answers heard",
             "The prior is how likely the judge thinks a human before any answer. "
             "The data are the answers, in order."),
            ("Compare the rows before reading the posterior",
             "If every answer is equally probable under both hypotheses, the Bayes "
             "factor is 1 and the posterior is the prior whatever was heard."),
            ("State what the number measures",
             "A factor away from 1 means the parties can be told apart. It says "
             "nothing about thought until a premise about behaviour and mind is "
             "added, and you should say which."),
        ],
        "worked": {
            "title": "Ten answers, then one tell",
            "intro": [
                "A judge with a prior of one half for human, hearing a perfect "
                "mimic, and then a machine with a tell.",
            ],
            "lines": [
                "mimic:  both rows plain 9/10, tell 1/10",
                "        ten answers, Bayes factor 1",
                "        posterior human: 1/2",
                "tell:   human 1/10, machine 9/10 on a tell",
                "        one tell, Bayes factor 1/9",
                "        posterior human: 1/10",
            ],
            "after": [
                "The mimic's ten answers are not weak evidence. They are no evidence, "
                "because the rows are the same. The tell is one answer and moves the "
                "odds on human from one to one down to one to nine, and the whole "
                "difference between the cases is a row of probabilities.",
            ],
        },
        "quiz_title": "Reading the judge",
        "quiz": [
            {"q": "A machine gives each kind of answer with exactly the probability a "
                  "human does. A judge who starts at one half for human hears ten "
                  "answers. Where should the judge end?",
             "a": ["Above one half, because ten answers is a lot of evidence",
                   "Below one half, because no answer favoured the human",
                   "At one half, because every answer has a Bayes factor of 1",
                   "It cannot be computed without hearing the answers"],
             "c": 2,
             "why": "Equal rows give a factor of 1 for every answer, whichever answers "
                    "come, so the posterior is the prior. The amount of data does not "
                    "matter when each datum carries no weight, and the answers do not "
                    "matter either."},
            {"q": "The lab's hypotheses are human and machine. What must be added "
                  "before a pass bears on whether the machine thinks?",
             "a": ["The premise that a party indistinguishable in behaviour has the "
                   "same mental life",
                   "More answers, until the posterior moves",
                   "A smaller prior for human",
                   "A likelihood row that sums to more than 1"],
             "c": 0,
             "why": "Behaviourism is the bridge from who to whether. More answers "
                    "from a perfect mimic leave the factor at 1, a different prior "
                    "changes the starting point and not the bridge, and a row that "
                    "does not sum to 1 is refused by the lab."},
            {"q": "In the tell preset, one answer has probability `1/10` under human "
                  "and `9/10` under machine. What is its Bayes factor for human?",
             "a": ["9", "`1/10`", "`9/10`", "`1/9`"],
             "c": 3,
             "why": "The factor is the probability under the hypothesis divided by the "
                    "probability under its alternative: `(1/10) / (9/10) = 1/9`. "
                    "Nine is the factor for machine, and the other two are single "
                    "likelihoods, not their ratio."},
            {"q": "A judge starts at `9/10` for human and hears the one tell. What "
                  "is the posterior for human?",
             "a": ["`9/10`, unchanged", "`1/2`", "`1/10`", "`1/9`"],
             "c": 1,
             "why": "The prior odds are nine to one and the factor is `1/9`, so the "
                    "posterior odds are one to one, which is a probability of one "
                    "half. A tell moves everyone, so the first choice is wrong, and "
                    "`1/10` is the answer only for a judge who started at one half."},
        ],
        "mistakes": [
            ("Reading a pass as proof of thought and a failure as its disproof",
             "The mimic preset passes with a Bayes factor of exactly 1, and that is "
             "a statement about what the judge can tell, not about what is behind "
             "the screen. The tell preset fails the machine with a factor of `1/9`, "
             "and a person with a distinctive manner would fail it in the same way. "
             "Only a bridge premise that identifies thinking with behaving turns "
             "either result into a verdict on thought."),
            ("Counting ten answers as ten pieces of evidence",
             "Evidence is a ratio of likelihoods, not a number of observations. "
             "Ten answers from a perfect mimic are ten factors of 1, and ten times "
             "1 is 1."),
            ("Thinking that one tell settles the question",
             "The prior-heavy preset shows a tell bringing a judge from `9/10` "
             "only to `1/2`. How far one answer moves a judge depends on where "
             "the judge began, and a confident judge needs more than one tell."),
        ],
        "standard": (
            "Finish when you can say what a pass shows and what it does not.",
            "Given two likelihood rows and an answer, you should be able to compute "
            "the Bayes factor and the posterior, say whether the answer separates "
            "the parties, and state the premise that would carry the result from "
            "who is behind the screen to whether it thinks."
        ),
        "note": (
            "The updating here is the same as in Knowledge and Evidence, with two "
            "hypotheses and two kinds of answer. What is new is the use made of the "
            "result."
        ),
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "functionalism-and-multiple-realisability",
        "title": "Functionalism and Multiple Realisability",
        "module": "Mind",
        "one_line": "Build two different circuits with the same truth table, and state functionalism as the claim that the state is the function.",
        "summary": (
            "Functionalism says a mental state is whatever plays a certain role, "
            "whatever it is made of. Write two circuits that compute the same "
            "function, check in the table that they agree in every row, and see "
            "what follows for pain being C-fibre firing."
        ),
        "key": [
            "same table, different circuit",
            "(p ∧ q) ∨ (p ∧ r)  three gates",
            "p ∧ (q ∨ r)        two gates",
            "equal in all eight rows",
            "functionalism: the state is the function",
        ],
        "key_label": "One function, two circuits",
        "concepts_intro": (
            "A truth table is the smallest honest example of a function that can "
            "be built more than one way. The idea of the lesson is in that gap."
        ),
        "concepts": [
            ("A function is what the table says",
             "Two circuits that give the same output for every input compute the "
             "same function, however differently they are wired. The table "
             "compares them without opening either."),
            ("Realisability is the many wirings of one table",
             "A state defined by its role can be realised by different parts: "
             "neurons in a person, silicon in a machine, valves in an imagined "
             "plumbing. That is multiple realisability, and the argument against "
             "identifying a state with one kind of part."),
            ("Agreeing on the inputs you tried is not agreeing",
             "Two functions can agree on most rows and differ on one. A test that "
             "never reaches that row, whether a behavioural test or a table "
             "checked halfway, cannot tell them apart."),
        ],
        "read_title": "The state as the function",
        "read_intro": (
            "Functionalism, then the circuit example, then the thing the example "
            "leaves out."
        ),
        "body": [
            ("def", ("Functionalism",
                     "<strong>Functionalism</strong> says that a mental state is "
                     "defined by the role it plays: what brings it about, what it "
                     "brings about, and how it combines with other states. Anything "
                     "that has states playing those roles is in the state, "
                     "whatever it is made of.")),
            ("p", "If that is right, the identity theory that the physicalist reached for in "
                  "“Dualism and the Conceivability Argument” was aiming at the wrong level. Pain is not the "
                  "firing of C-fibres, because an octopus, which has no C-fibres, "
                  "or a machine, which has no neurons at all, might be in pain by "
                  "having something in the right role. One state, many "
                  "realisations: that is <strong>multiple realisability</strong>."),
            ("p", "A truth table shows the idea at its smallest scale. Here are two "
                  "circuits with three inputs `p`, `q` and `r`. The first uses "
                  "three gates, two of conjunction and one of disjunction: "
                  "`(p ∧ q) ∨ (p ∧ r)`. The second uses two, one of disjunction "
                  "and one of conjunction: `p ∧ (q ∨ r)`. They are wired "
                  "differently. Put them in the lab and they agree in all eight "
                  "rows, true in the same three and false in the same five."),
            ("p", "So as functions they are one. Anything that treats an input "
                  "according to this table is doing what both do, and nothing about "
                  "the output reveals which circuit produced it. A functionalist "
                  "says the same of minds: the state is the function, and the "
                  "circuit is its realisation."),
            ("p", "Other pairs in the lab show the variety. The circuit "
                  "`¬(¬p ∨ ¬q)` has a negation at each input, a disjunction and a "
                  "negation at the output, and computes exactly `p ∧ q`, which is "
                  "De Morgan's law as wiring. The circuit `(p → q) ∧ (q → p)` "
                  "computes `p ↔ q`, again by a different route."),
            ("p", "The same lab shows what a behavioural test can miss. The "
                  "functions `p ∧ q` and `p ∧ (q ∨ r)` differ in one row only, "
                  "where `p` and `r` are true and `q` false. Feed them every other "
                  "input and they behave alike. A tester who never tries that input "
                  "concludes they are the same, and is wrong."),
            ("p", "What the example leaves out matters. A truth table is a function "
                  "of the present inputs, and a mind has states that depend on "
                  "history, so real functionalism describes machines with internal "
                  "states, not tables. The lesson takes the smallest case in which "
                  "the point can be checked row by row. And it does not show that "
                  "the role is all there is to pain. That is what the next "
                  "lessons press from two sides."),
        ],
        "lab": ("truth_table", {
            "mode": "two",
            "formulas": ["(p & q) | (p & r)", "p & (q | r)", "~(~p | ~q)",
                         "p & q", "(p -> q) & (q -> p)", "p <-> q"],
            "compare_with": "p & (q | r)",
            "panel_title": "Two circuits, one table",
            "panel_intro": (
                "Formula A starts as the three-gate circuit and formula B as the "
                "two-gate one. Compare the columns row by row. Then set A to "
                "`p ∧ q` and find the one row in which it differs from B. Then set "
                "B to `p ∧ q` as well, set A to the formula with a negation at each "
                "input, and find none."
            ),
        }),
        "steps_title": "Checking that two circuits compute one function",
        "steps_intro": "Four steps, in this order. Only the last speaks to functionalism.",
        "steps": [
            ("Write each circuit as a formula",
             "One formula per circuit, over the same input letters. A letter that "
             "one circuit never reads is still an input to the table."),
            ("Fill both tables over all inputs",
             "Every assignment of true and false to every input letter, not a "
             "selection. A shortcut here is the mistake the lesson is about."),
            ("Compare the output columns row by row",
             "If one row differs, the functions differ, and you have the input "
             "that tells them apart. If none does, they are one function."),
            ("Say what is shared and what is not",
             "The shared thing is the table, and it is the candidate for the state. "
             "The unshared things, the number and kind of gates, are the "
             "realisations."),
        ],
        "worked": {
            "title": "Three gates against two",
            "intro": [
                "The two circuits compared in all eight rows of `p`, `q`, `r`.",
            ],
            "lines": [
                "A = (p ∧ q) ∨ (p ∧ r)    three gates",
                "B = p ∧ (q ∨ r)          two gates",
                "true rows of A:   TTT   TTF   TFT",
                "true rows of B:   TTT   TTF   TFT",
                "other five rows:  A false, B false",
                "differing rows:   none",
            ],
            "after": [
                "Different circuits, one function. The factoring of `p` out of the "
                "disjunction is the whole of the difference, and the table does not "
                "see it. A functionalist reads that as the point: what makes "
                "something the state is the table, not the factoring.",
            ],
        },
        "quiz_title": "Same function, different circuit",
        "quiz": [
            {"q": "How do `(p ∧ q) ∨ (p ∧ r)` and `p ∧ (q ∨ r)` compare in the lab?",
             "a": ["They differ in the row where `p` is true and `q` and `r` are false",
                   "They differ in the row where `p` is false and `q` and `r` are true",
                   "They differ in exactly two rows",
                   "They agree in all eight rows although they are wired differently"],
             "c": 3,
             "why": "The two are equivalent by distribution. In the row with `p` true "
                    "and `q` and `r` false both are false, and in the row with `p` "
                    "false both are false, so the first two choices name rows where "
                    "they agree."},
            {"q": "Which pair of formulas differs in no row?",
             "a": ["`p ∧ q` and `p ∧ (q ∨ r)`",
                   "`¬(¬p ∨ ¬q)` and `p ∧ q`",
                   "`p ∧ q` and `p ↔ q`",
                   "`p ↔ q` and `p ∧ (q ∨ r)`"],
             "c": 1,
             "why": "De Morgan: the negation of a disjunction of negations is the "
                    "conjunction. The first pair differs when `p` and `r` are true "
                    "and `q` false, the third when both letters are false (the "
                    "biconditional is true and the conjunction false), and the "
                    "fourth in several rows."},
            {"q": "A functionalist says pain can be realised in an octopus and in a "
                  "machine. Which part of the lab's example corresponds to that claim?",
             "a": ["Two circuits with one truth table",
                   "Two circuits with different tables that are both called pain",
                   "One circuit whose table changes with the material it is built from",
                   "A table that records which gates a circuit has"],
             "c": 0,
             "why": "Pain is the function, and the octopus and the machine are two "
                    "ways of computing it. The second choice gives up the role as "
                    "the definition, the third makes the function depend on the "
                    "material, which is what the functionalist denies, and a table "
                    "records outputs, not gates."},
            {"q": "The functions `p ∧ q` and `p ∧ (q ∨ r)` agree in seven of the "
                  "eight rows. What follows for a tester who tries only those seven "
                  "inputs?",
             "a": ["The two are the same function",
                   "Adding gates to either circuit would remove the difference",
                   "The tester cannot tell them apart, although they are different "
                   "functions",
                   "The tester has shown that the functions are the same in all "
                   "but one row, which is as good as equal"],
             "c": 2,
             "why": "Agreement on the inputs tried is consistent with a difference "
                    "elsewhere. One differing row is enough for the functions to be "
                    "different, and the gates do not matter: the function is the "
                    "table."},
        ],
        "mistakes": [
            ("Thinking that the same behaviour means the same mechanism",
             "The two circuits agree in all eight rows and are built from different "
             "gates, three against two. Output depends on the function, and a "
             "function can be reached by more than one route. That is why a "
             "functionalist does not identify a state with the parts that happen to "
             "realise it."),
            ("Taking agreement on the inputs tried for agreement",
             "The functions `p ∧ q` and `p ∧ (q ∨ r)` agree in seven rows and "
             "differ in the eighth. A behavioural test that skips the eighth input "
             "rates them equal. The judge of “Behaviourism and the Turing Test” "
             "is in that position: ten answers heard are ten rows of a table "
             "whose other rows were never tried."),
            ("Reading functionalism as saying that the material never matters",
             "The claim is that the material does not decide which state it is. "
             "It can still decide whether anything plays the role at all: a "
             "circuit wired as `p ∧ q` does not realise the function `p ∧ (q ∨ r)`, "
             "whatever it is made of."),
        ],
        "standard": (
            "Finish when you can show two realisations and say what they share.",
            "Given a function, you should be able to write two different circuits "
            "for it, check by table that they agree in every row, and say what "
            "the claim that a state is a function amounts to when applied to the "
            "two."
        ),
        "note": (
            "The circuits here have no memory. A mind, and a machine that "
            "functionalism is about, does, so the lesson is the idea at its "
            "smallest, not a theory of mind."
        ),
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "the-chinese-room-and-the-lookup-table",
        "title": "The Chinese Room and the Lookup Table",
        "module": "Mind",
        "one_line": "Count the entries a lookup table needs for a conversation, and use the count to state Block's argument and Searle's.",
        "summary": (
            "A machine that passes a conversation test by consulting a table keyed "
            "on the whole conversation needs one entry for each possible "
            "conversation. Count them, see why that makes a table the opposite of a "
            "program, and state what Block and Searle each use the table for."
        ),
        "key": [
            "table: one reply per whole conversation",
            "n inputs per turn, r turns: nʳ entries",
            "24 inputs, 12 turns: 24¹² entries",
            "each extra turn multiplies by 24",
            "a program compresses; a table lists",
        ],
        "key_label": "A table is as big as the conversations",
        "concepts_intro": (
            "Behaviour that passes a test can be produced in two quite different "
            "ways, by a rule that generates it or by a list that stores it. The "
            "second is countable."
        ),
        "concepts": [
            ("A table stores replies; a program generates them",
             "A lookup table holds a reply for every case it must meet and computes "
             "nothing. A program holds a rule from which the replies follow. The "
             "same replies can come from either, and the two have very different "
             "sizes."),
            ("A conversation is a sequence",
             "If each turn offers one of `n` things to say and the conversation "
             "lasts `r` turns, there are `nʳ` complete conversations, because each "
             "turn multiplies the count by `n`. This is the count of ordered "
             "choices with repetition from Combinatorics and Counting on the "
             "Discrete Mathematics path."),
            ("Two arguments, one device",
             "Block uses the table to argue that passing a behavioural test is not "
             "enough for intelligence. Searle uses a room with a rulebook to argue "
             "that running a program is not enough for understanding. The device "
             "differs, and so does the count that bears on it."),
        ],
        "read_title": "Counting the table",
        "read_intro": (
            "The count first, then the two arguments, then what the count settles "
            "and does not."
        ),
        "body": [
            ("def", ("Lookup table",
                     "A <strong>lookup table</strong> answers by finding its input "
                     "in a list and returning the reply stored beside it. It does "
                     "not compute a reply; every reply it will ever give is "
                     "already written down.")),
            ("p", "Suppose a machine is to pass the conversation test of the "
                  "previous lessons by this method. Its reply at any moment depends "
                  "on everything said so far, so the table has to be keyed on the "
                  "whole conversation, not on the last remark. If at each turn the "
                  "judge may say one of `n` things, and the conversation has `r` "
                  "turns, the table needs a reply ready for every sequence of "
                  "`r` remarks."),
            ("p", "That is a count of ordered choices with repetition: `n` choices "
                  "at the first turn, `n` at the second, and so on, which gives "
                  "`nʳ`. Shorter conversations add a little more, because the "
                  "table must also answer the ones that end early, but the largest "
                  "term is the whole-conversation count. In the lab, set `n` to 24 "
                  "and `r` to 12."),
            ("math", [
                "24¹²  =  36 520 347 436 056 576",
            ]),
            ("p", "That is over thirty-six quadrillion entries for a twelve-turn "
                  "conversation in which the judge has only twenty-four things to "
                  "say. Slide `r` down and the table shrinks fast: at three turns "
                  "it is 13 824, and each further turn multiplies it by 24. A real "
                  "conversation has a vastly larger stock of remarks and many more "
                  "turns, so the table grows at a rate no budget can meet."),
            ("p", "Compare a program. A program that holds a rule for forming "
                  "replies can be a few thousand lines and meet every one of those "
                  "conversations, because it does not store them; it works them "
                  "out. A table is the opposite of compression. Its size is the "
                  "number of cases it covers, and a program's size is the length of "
                  "the idea behind them."),
            ("p", "Block takes the table as a thought experiment. Build one anyway, "
                  "in principle, with every sensible conversation of some length "
                  "written in. It passes the test with a Bayes factor of 1 and "
                  "nothing in it is intelligent: it looks up. So behaviour that "
                  "passes the test is not sufficient for intelligence, and "
                  "behaviourism is false. The reply is that a table which cannot be "
                  "built tells us little about what a thing that could be built "
                  "must be like. Block's rejoinder is that behaviourism was a "
                  "claim about what is conceptually enough, and an in-principle "
                  "case refutes a claim of that strength."),
            ("p", "Searle's room is a different case. A person who reads no Chinese "
                  "sits in a room with a rulebook for manipulating Chinese symbols, "
                  "and passes out replies that a Chinese speaker would accept. The "
                  "room runs on rules, so its size is the size of the rulebook and "
                  "not the number of conversations, and the count does not touch "
                  "it. Searle argues that the person understands nothing, so "
                  "following the rules cannot be understanding. The standard reply "
                  "is that the whole system, room and rulebook and person together, "
                  "understands. Searle's rejoinder is to let the person memorise "
                  "the rulebook and work in the open, so that the system is the "
                  "person, who still understands nothing. The lesson does not "
                  "choose."),
            ("p", "What the count settles is narrow. A passing system of any "
                  "realistic size is not a table, so it generalises, and whether "
                  "generalising amounts to understanding is the open question. What "
                  "it does not settle is whether a table, if built, would think."),
        ],
        "lab": ("counting", {
            "rule": "pr",
            "n": 24,
            "r": 12,
            "panel_title": "How many conversations",
            "panel_intro": (
                "The first row counts ordered choices with repetition, which is "
                "the conversation count. Slide the number of turns down to three and "
                "up again, and watch the first row against the others."
            ),
        }),
        "steps_title": "Sizing a table",
        "steps_intro": "Four steps. The second is the one that makes the number large.",
        "steps": [
            ("Fix the inputs per turn",
             "Say how many things the judge can say at one turn. Call it `n`. The "
             "lab's `n` is that number."),
            ("Key the table on the whole conversation",
             "The reply may depend on everything said before, so the table needs "
             "an entry for each sequence of `r` remarks, not for each remark."),
            ("Count the sequences",
             "Ordered, with repetition: `n` at each turn, so `nʳ`. Read it off the "
             "first row of the lab."),
            ("Compare it with a rule",
             "A program that forms replies is the length of its rule, whatever the "
             "number of conversations. A table is the length of the number of "
             "conversations."),
        ],
        "worked": {
            "title": "A twelve-turn table",
            "intro": [
                "A judge with twenty-four possible remarks per turn, and a "
                "conversation of twelve turns.",
            ],
            "lines": [
                "turns   entries",
                "3       24³ = 13 824",
                "12      24¹² = 36 520 347 436 056 576",
                "each added turn multiplies the table by 24",
            ],
            "after": [
                "The table grows with the number of conversations, and the number of "
                "conversations grows by a factor of 24 for every turn. So the "
                "machine that passes a long test is not a table of this kind in "
                "practice. It is something that computes, and Block's table is "
                "then an argument about what would follow if one existed.",
            ],
        },
        "quiz_title": "Counting and arguing",
        "quiz": [
            {"q": "A table is keyed on whole conversations of three turns, with 24 "
                  "possible remarks per turn. How many entries does it need?",
             "a": ["72", "576", "13 824", "12 144"],
             "c": 2,
             "why": "Ordered choices with repetition: `24 · 24 · 24 = 13 824`. The "
                    "first choice adds the three turns instead of multiplying, the "
                    "second counts two turns, and `12 144` is `24 · 23 · 22`, which "
                    "forbids a remark being repeated."},
            {"q": "The table is extended by one more turn. What happens to the number "
                  "of entries?",
             "a": ["It is multiplied by 24",
                   "It grows by 24 entries",
                   "It is multiplied by the ratio of the new number of turns to the old",
                   "It doubles"],
             "c": 0,
             "why": "Each earlier conversation can now continue in 24 ways. Adding 24 "
                    "would be the growth of a list with one new item per turn, and "
                    "the ratio of turn counts is a different formula."},
            {"q": "What does the count say about a lookup table compared with a "
                  "program that produces the same replies?",
             "a": ["The table is about the size of the program",
                   "The table is smaller, since it stores replies only",
                   "The table is the same size but slower",
                   "The table grows with the number of conversations, where the "
                   "program's size need not"],
             "c": 3,
             "why": "A table lists every case. A program holds the rule from which the "
                    "cases follow, so it can be short and still meet all of them."},
            {"q": "Which claim does Block use the table to attack?",
             "a": ["That a machine can be built from gates",
                   "That whatever behaves as an intelligent thing does is intelligent",
                   "That a conversation has a finite number of turns",
                   "That a program can be run on more than one machine"],
             "c": 1,
             "why": "The table passes the test and looks up. If it is not "
                    "intelligent, behaviour that passes is not enough, which is "
                    "behaviourism denied. The other claims are not in dispute."},
        ],
        "mistakes": [
            ("Taking a lookup table for a small program",
             "A program is short because it generalises: it turns a rule into a "
             "reply for each case. A table has no rule, so its length is the "
             "number of cases, and that number is `nʳ`. At 24 remarks and 12 turns "
             "the lab prints a count of more than thirty-six quadrillion, and each "
             "added turn multiplies it by 24."),
            ("Treating the Chinese room and the lookup table as one argument",
             "The room has a rulebook and can be small, so the count does not "
             "touch it. The table is the large device with no rule at all. Block's "
             "argument needs the table, and Searle's needs the rulebook."),
            ("Reading the count as a refutation of Block",
             "That a table cannot be built shows that nothing could pass by "
             "looking up. It does not show that a table, if built, would think, "
             "and Block's claim was about what is possible in principle. The "
             "count tells you what a real passer must be doing, not what an "
             "imaginary one would be."),
        ],
        "standard": (
            "Finish when you can count the table and say what each argument uses it for.",
            "Given the number of remarks and turns, you should be able to compute "
            "the entries a table needs, say why a program of the same behaviour is "
            "smaller, and state in a sentence what Block and what Searle infer "
            "from their devices."
        ),
        "note": (
            "The lab's rows give the other counting rules beside the one used here. "
            "Only the first row, ordered with repetition, is the conversation "
            "count; the others answer different questions."
        ),
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "the-knowledge-argument",
        "title": "The Knowledge Argument",
        "module": "Mind",
        "one_line": "Formalise Mary's argument, find it valid, and place the physicalist's reply in a premise rather than in the logic.",
        "summary": (
            "Mary knows every physical fact about colour and has never seen red. "
            "Formalise the argument that she learns something on release, show it "
            "valid as modus tollens, and show that the physicalist's replies deny "
            "a premise or charge equivocation, and do not dispute the validity."
        ),
        "key": [
            "a: physicalism     n: Mary learns a fact",
            "a → ¬n,  n  ∴  ¬a",
            "valid: no row has true premises, false ¬a",
            "reply: deny n  (an ability, not a fact)",
            "reply: two senses of knowing, two atoms",
        ],
        "key_label": "A valid argument, a denied premise",
        "concepts_intro": (
            "The knowledge argument is short, and the temptation is to wave it "
            "away. The lab shows where a reply has to go instead."
        ),
        "concepts": [
            ("Mary's story gives two premises",
             "If physicalism is true, a person who knows all the physical facts "
             "has nothing left to learn about what red looks like. And on seeing "
             "red, Mary does learn something. The conclusion is that physicalism "
             "is false."),
            ("Validity is the first question, and the lab answers it",
             "The form is modus tollens, which has no counterexample row. So the "
             "physicalist must deny a premise, and the lesson is about which, and "
             "at what cost."),
            ("Changing an atom changes the argument",
             "If the premise about a new fact is replaced by one about a new "
             "ability, or if &ldquo;knows&rdquo; is used in two senses, the "
             "argument is no longer the same argument. The lab shows this "
             "as a counterexample row."),
        ],
        "read_title": "Mary, in three presets",
        "read_intro": (
            "The argument as stated, the reply that changes an atom, and the "
            "charge of equivocation."
        ),
        "body": [
            ("p", "Mary is a scientist who knows every physical fact there is to "
                  "know about colour and the vision of colour. She has lived "
                  "her whole life in a room where everything is black, white or "
                  "grey. One day she is let out and sees a ripe tomato. The "
                  "knowledge argument says that she learns what red looks like, "
                  "that this is something she did not already know, and that "
                  "therefore not every fact is a physical fact."),
            ("p", "Put it in standard form. Let `a` say that physicalism is true: "
                  "every fact is a physical fact. Let `n` say that on release Mary "
                  "learns a new fact."),
            ("ol", [
                "If physicalism is true, Mary, who already knew every physical "
                "fact, learns no new fact: `a → ¬n`.",
                "Mary does learn a new fact on release: `n`.",
                "So physicalism is false: `¬a`.",
            ]),
            ("p", "This is modus tollens. The lab builds a row for every assignment "
                  "of `a` and `n`, four in all, and finds none in which both "
                  "premises are true and the conclusion false. The verdict is "
                  "valid, and the form is named. That settles the logic, and "
                  "puts all the weight on the premises."),
            ("def", ("The physicalist's two ways out",
                     "A physicalist can <strong>deny a premise</strong>, most "
                     "naturally the second, or can say that the argument "
                     "<strong>equivocates</strong>, so that its two premises do not "
                     "share the sense they need. Neither is a claim that the form "
                     "is invalid.")),
            ("p", "The first is the ability reply. What Mary gains is not a fact but "
                  "an ability: to recognise red, to imagine it, to remember it. "
                  "Knowing how is not knowing that, and a new ability is not a new "
                  "fact. This denies `n`. The second preset shows what happens "
                  "when the argument is restated with the ability in the place of "
                  "the fact: let `k` say that Mary gains a new ability. Then "
                  "`a → ¬n` and `k` do not lead to `¬a`, and the lab finds a "
                  "counterexample row, with `a` and `k` true and `n` false. A new "
                  "ability does not conflict with physicalism. The reply is not "
                  "that the argument is invalid. It is that the fact premise is "
                  "false, and that the ability premise, which is true, does not "
                  "carry the conclusion."),
            ("p", "The second is the charge of equivocation. Knowing a physical "
                  "fact is knowing that something is so; knowing what red looks "
                  "like seems to be knowing it by acquaintance. If the two are "
                  "different senses, then the premise that links them for "
                  "physicalism fails. In the third preset the senses are separate "
                  "atoms: `f` for Mary's knowing all the physical facts, `l` for "
                  "her lacking what red looks like in the same sense, and `m` for "
                  "her lacking it in the sense of acquaintance. The premises "
                  "are `a → ¬(f ∧ l)`, `f` and `m`. The lab finds a counterexample "
                  "row, with `a`, `f` and `m` true and `l` false."),
            ("p", "That is the physicalist's point, and the dualist's answer is "
                  "also visible. Make `l` and `m` one atom, so that what Mary "
                  "lacks is the same in both premises, and the lab finds the "
                  "argument valid again. Whether they are one atom is what the "
                  "dispute is: the dualist holds that acquaintance with red is "
                  "knowledge of a fact, and the physicalist that it is not."),
            ("p", "Each side has a cost. To deny that Mary learns a new fact is to "
                  "say that her coming to know what red looks like adds nothing "
                  "to what is so, which many find hard to say with a straight "
                  "face. To accept the new fact is to accept that something is "
                  "left out of the physical story, which is what the physicalist "
                  "cannot. The lab checks the logic and leaves the costs for you "
                  "to weigh."),
        ],
        "lab": ("argkit", {
            "mode": "validity",
            "preset": "mary",
            "show": "all",
            "presets": [
                {"id": "mary", "label": "Physicalism, a new fact, the conclusion",
                 "premises": ["a -> ~n", "n"], "conclusion": "~a", "expect": {"vaRows": "4", "vaCounter": "0", "vaVerdict": "Valid", "vaForm": "modus tollens"}},
                {"id": "ability-reply", "label": "Physicalism, a new ability, the conclusion",
                 "premises": ["a -> ~n", "k"], "conclusion": "~a", "expect": {"vaRows": "8", "vaCounter": "1", "vaVerdict": "Invalid"}},
                {"id": "equivocation", "label": "Two senses of knowing, as two atoms",
                 "premises": ["a -> ~(f & l)", "f", "m"], "conclusion": "~a", "expect": {"vaRows": "16", "vaCounter": "1", "vaVerdict": "Invalid"}},
            ],
            "panel_title": "Which atom the premise is about",
            "panel_intro": (
                "In the first preset find the premises and the conclusion, and check "
                "that no row makes the premises true and the conclusion false. In "
                "the others the highlighted row is the case the reply describes. "
                "Then, in the last, type l in place of m and see the verdict return."
            ),
        }),
        "steps_title": "Formalising a philosophical argument",
        "steps_intro": "Five steps. The third is where replies get their grip.",
        "steps": [
            ("Pick one letter for each claim",
             "Physicalism, Mary learns a new fact, and so on. Two letters for two "
             "claims, and no letter for a claim that is used in two senses."),
            ("Write each premise and the conclusion",
             "Use the connectives of the earlier course. A conditional for what "
             "physicalism says Mary would not learn, and a plain letter for what "
             "she does learn."),
            ("Check the atoms across the premises",
             "A letter must mean the same in each premise it appears in. If "
             "&ldquo;knows&rdquo; is used in two senses, give each its own letter "
             "and see whether the argument survives."),
            ("Ask the lab for the verdict and the row",
             "A verdict of valid leaves only the premises to doubt. A verdict of "
             "invalid shows the row, and the row says which case was overlooked."),
            ("Place the reply",
             "Say which premise a reply denies, or which atom it splits. A reply "
             "that does neither has not yet met the argument."),
        ],
        "worked": {
            "title": "Mary as modus tollens",
            "intro": [
                "Premises `a → ¬n` and `n`, conclusion `¬a`.",
            ],
            "lines": [
                "a  n  |  a → ¬n   n   |  ¬a",
                "T  T  |  F         T   |  F",
                "T  F  |  T         F   |  F",
                "F  T  |  T         T   |  T",
                "F  F  |  T         F   |  T",
            ],
            "after": [
                "Only the third row makes both premises true, and in it the "
                "conclusion is true. The argument is valid. The ability reply "
                "goes after the premise `n`, and the equivocation reply after "
                "the match between the senses; neither touches the table.",
            ],
        },
        "quiz_title": "Where the reply goes",
        "quiz": [
            {"q": "In the ability-reply preset the premise `k` replaces `n`. Why does "
                  "the lab find a counterexample?",
             "a": ["Modus tollens is invalid",
                   "The conclusion mentions physicalism and the premise does not",
                   "Physicalism and a new ability are logically incompatible",
                   "Nothing in the premises relates `k` to `a`, so `a` and `k` can both "
                   "be true"],
             "c": 3,
             "why": "The first premise is about `n`, not `k`. With `a` and `k` true "
                    "and `n` false both premises hold and the conclusion fails. "
                    "Modus tollens is valid in the first preset; the form has "
                    "changed in the second."},
            {"q": "A physicalist says Mary learns no new fact, only a new ability. "
                  "Which premise of the first preset is being denied?",
             "a": ["`n`, that Mary learns a new fact",
                   "`a → ¬n`, that physicalism rules out a new fact",
                   "`¬a`, the conclusion",
                   "That modus tollens is a valid form"],
             "c": 0,
             "why": "`n` says that she learns a new fact, and the reply is that she "
                    "does not. The second choice is a different strategy, the "
                    "conclusion is what the premises are meant to establish, and the "
                    "ability reply accepts the validity of the form."},
            {"q": "Which statement about the first preset is correct?",
             "a": ["It is valid, so its conclusion is true",
                   "It is invalid, because the physicalist disagrees with it",
                   "It is valid, so a reply must deny a premise or split an atom",
                   "It is invalid, because its conclusion mentions a different "
                   "sentence letter from its premises"],
             "c": 2,
             "why": "Validity says no row has true premises and a false conclusion, "
                    "and says nothing about whether the premises are true. Someone "
                    "disagreeing does not make it invalid, and a conclusion may "
                    "reuse letters from the premises, as here."},
            {"q": "In the equivocation preset the lab marks one counterexample "
                  "row. What case does it describe?",
             "a": ["Physicalism is false, and Mary lacks both kinds of knowledge",
                   "Physicalism is true, Mary knows all the physical facts and lacks "
                   "acquaintance, but does not lack knowing-that of red",
                   "Mary knows every physical fact and learns nothing on release",
                   "Physicalism is true and Mary knows no physical facts"],
             "c": 1,
             "why": "The row has `a`, `f` and `m` true and `l` false: the premises "
                    "hold and the conclusion fails. That is the physicalist's "
                    "picture, in which what Mary lacks is not what physicalism "
                    "says she should have."},
        ],
        "mistakes": [
            ("Thinking the knowledge argument is invalid",
             "The lab checks it. With `a → ¬n` and `n` as premises and `¬a` as the "
             "conclusion there are four rows and no counterexample, and the form is "
             "modus tollens. A physicalist who wants to resist it must deny a "
             "premise or charge equivocation, and the replies are good or bad "
             "according to what they say about the premises."),
            ("Counting a change of atom as a refutation",
             "The ability preset has a counterexample row, but it has changed the "
             "argument. `k` is not `n`. The ability reply does not show that Mary's "
             "argument fails to follow; it asks the dualist to defend the claim "
             "that Mary learns a fact."),
            ("Treating the equivocation charge as settled",
             "The third preset shows what the charge would show, if the two senses "
             "are different. Make `l` and `m` one letter and the argument is valid "
             "again. Whether they are one is the question between the sides, and "
             "the lab does not decide it."),
        ],
        "standard": (
            "Finish when you can place a reply to the argument.",
            "Given the knowledge argument or a reply to it, you should be able to "
            "write the premises with one letter for each claim, check the validity "
            "in a lab, and say which premise the reply denies or which atom it "
            "splits."
        ),
        "note": (
            "The dualist and the physicalist can both read this lesson as favouring "
            "them. The lab does not choose, because choosing is a matter of which "
            "premise to give up."
        ),
    },
]
