"""Course 3, lessons 1 to 5: induction and confirmation up to the ravens."""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "enumerative-induction-and-humes-problem",
        "title": "Enumerative Induction and Hume's Problem",
        "module": "Induction",
        "one_line": "A run of sunrises is not a deduction of the next one, and what must be added is a prior.",
        "summary": (
            "&ldquo;The sun has risen ten times, so it will rise again&rdquo; has a counterexample row, however "
            "large the number. It gains force only under a prior over hypotheses about how reliable the sun "
            "is, and the same ten sunrises give a different prediction under a different prior."
        ),
        "key": [
            "10 sunrises, so an 11th: has a bad row",
            "no row ⟹ valid; one row ⟹ invalid",
            "P(next) = Σ P(chance | data)·chance",
            "the prior supplies what the data cannot",
        ],
        "key_label": "What the past licenses",
        "concepts_intro": (
            "Induction is reasoning from observed cases to unobserved ones. The question is not whether we do "
            "it, but what we are assuming when we do."
        ),
        "concepts": [
            ("Enumerative induction is not deduction",
             "From &ldquo;every observed case was F&rdquo; to &ldquo;the next case will be F&rdquo; there is "
             "always a row of the truth table on which the premises hold and the conclusion fails. Adding "
             "more premises of the same kind adds more cases to the premises and leaves that row in place."),
            ("A prior is the missing premise written down",
             "To let the past bear on the future you must say, before looking, how likely the various "
             "regularities are. That is a prior over hypotheses, and the data then reweight it."),
            ("Hume's problem is about justification, not reliability",
             "The question is not whether induction has worked. It is whether anything non-circular shows that "
             "it will go on working, and the answer Hume gave is that nothing does."),
        ],
        "read_title": "From the past to the next case",
        "read_intro": (
            "First the argument, then the row that defeats it, then the extra premise that would repair it."
        ),
        "body": [
            ("p", "Take the plainest inductive argument there is: the sun has risen on each of the last ten "
                  "days, so it will rise on the eleventh. Write `R₁` for &ldquo;the sun rises on day 1&rdquo;, "
                  "and so on. The argument has ten premises and one conclusion, and “Validity by Truth "
                  "Table” gives the test: look for a row on which every premise is true and the conclusion "
                  "false."),
            ("math", [
                "day 1   day 2   ...   day 10   |   day 11",
                "-----------------------------------------",
                "  T       T     ...     T      |     F      <- every premise true, conclusion false",
            ]),
            ("p", "The row exists. Nothing in the ten premises mentions day 11, so the sentence about day 11 "
                  "is free to be false, and the argument is invalid. Replace ten by ten thousand and the row "
                  "is still there: the premises grow, the conclusion does not move into them."),
            ("def", ("Enumerative induction",
                     "<strong>Enumerative induction</strong> is the inference from &ldquo;all observed cases "
                     "of F have been G&rdquo; to &ldquo;the next case of F will be G&rdquo;. As a form it "
                     "is invalid, so whatever force it has comes from a premise it does not state.")),
            ("p", "The missing premise can be written as a probability. Suppose the sun rises each day with "
                  "some fixed chance, and consider five hypotheses about that chance: `1`, `3/4`, `1/2`, "
                  "`1/4` and `0`. Put an equal prior of `1/5` on each. This is the rule of succession "
                  "reduced to five points, which keeps every number an exact fraction; it is a discretisation "
                  "and it says nothing about hypotheses in between."),
            ("p", "Ten sunrises in a row have probability `chance¹⁰` under each hypothesis, so they favour "
                  "the high chances heavily. After the data, the hypothesis that the sun always rises "
                  "carries the posterior the lab prints in its first tile, and the probability of an eleventh "
                  "sunrise is each hypothesis's chance weighted by its posterior."),
            ("math", [
                "chance   prior   weight after ten sunrises (units of 1/1048576)",
                "---------------------------------------------------------------",
                "  1       1/5        1048576",
                "  3/4     1/5          59049",
                "  1/2     1/5           1024",
                "  1/4     1/5              1",
                "  0       1/5              0",
            ]),
            ("thm", ("The predictive probability",
                     "The probability that the next case is a success is the sum, over the hypotheses, of "
                     "the posterior of each times its chance of a success: `P(next | data) = Σ P(h | data)·chance(h)`. "
                     "It is below 1 whenever some hypothesis with a chance under 1 keeps any posterior.")),
            ("example", ("Same data, other prior",
                         "Give a skeptic a prior of `1/1000` on a chance of 1, `1/10` on each of `3/4`, "
                         "`1/2` and `1/4`, and `699/1000` on a chance of 0. The ten sunrises are the same, "
                         "the likelihoods are the same, and the predictive probability falls from just "
                         "under 1 to about `0.78`. The data did not change; the prior did.")),
            ("p", "That is the force of Hume's point. His argument can be set out as a valid argument, and "
                  "its premises are worth stating at full strength:"),
            ("ol", [
                "An argument from observed cases to an unobserved one is either deductive or rests on the "
                "assumption that the unobserved resembles the observed.",
                "It is not deductive: the row above shows that.",
                "The assumption of resemblance is not a necessary truth, since a world in which the sun "
                "stops is describable without contradiction. So if anything supports it, experience does; "
                "Hume allowed no third source.",
                "Any argument from experience for it is itself an argument from observed cases to "
                "unobserved ones, and so already assumes it.",
                "So nothing non-circular supports the assumption, and nothing non-circular supports "
                "enumerative induction.",
            ]),
            ("p", "The lab does not answer this. It shows exactly where the answer would have to go. Reject "
                  "the third premise and you owe an account of a third source of support, or of why "
                  "resemblance is necessary after all; reject the fourth and you owe an account of why a "
                  "circular defence is not vicious; accept the conclusion and you owe an account of why "
                  "anyone should expect the sun at all. Either way the reader decides, and the arithmetic "
                  "is the same."),
        ],
        "lab": ("choicekit", {
            "mode": "update",
            "preset": "succession",
            "presets": [
                {"id": "succession",
                 "label": "Uniform prior over five chances, ten sunrises",
                 "hyps": ["chance 1", "chance 3/4", "chance 1/2", "chance 1/4", "chance 0"],
                 "prior": ["1/5", "1/5", "1/5", "1/5", "1/5"],
                 "outcomes": ["rise", "fail"],
                 "lik": [["1", "0"], ["3/4", "1/4"], ["1/2", "1/2"], ["1/4", "3/4"], ["0", "1"]],
                 "data": ["rise"] * 10,
                 "payoffs": None,
                 "expect": {"upPost": "524288/554325", "upPred": "43735/44346"}},
                {"id": "skeptic",
                 "label": "Skeptic's prior, ten sunrises",
                 "hyps": ["chance 1", "chance 3/4", "chance 1/2", "chance 1/4", "chance 0"],
                 "prior": ["1/1000", "1/10", "1/10", "1/10", "699/1000"],
                 "outcomes": ["rise", "fail"],
                 "lik": [["1", "0"], ["3/4", "1/4"], ["1/2", "1/2"], ["1/4", "3/4"], ["0", "1"]],
                 "data": ["rise"] * 10,
                 "payoffs": None,
                 "expect": {"upPost": "131072/881997", "upPred": "1382119/1763994"}},
            ],
        }),
        "steps_title": "Reading an inductive argument",
        "steps_intro": "Four moves, in this order, for any argument from past cases to a new one.",
        "steps": [
            ("Find the row",
             "Write the observed cases as premises and the new case as the conclusion, and set every "
             "premise true and the conclusion false. If nothing forbids that, the argument is invalid."),
            ("Name the missing premise",
             "Say what would have to be true of the unobserved for the past to bear on it. For the sun it "
             "is that the chance of rising is stable from one day to the next."),
            ("Write it as a prior",
             "List the hypotheses about that stability, with a probability on each before any data. The "
             "choice is yours, and it is the part the data cannot check."),
            ("Compute, then vary the prior",
             "Read the posterior and the predictive probability from the lab, then change the prior and "
             "read them again. The gap between the two answers is how much the conclusion owes to the "
             "premise rather than to the data."),
        ],
        "worked": {
            "title": "Ten sunrises under two priors",
            "intro": [
                "Take the five chances and the uniform prior. Weight each by the probability of the data "
                "under it, then normalise."
            ],
            "lines": [
                "chances: 1, 3/4, 1/2, 1/4, 0; prior 1/5 on each",
                "data: ten sunrises in a row",
                "weights, in units of 1/1048576: 1048576, 59049, 1024, 1, 0",
                "total weight: 1108650",
                "P(chance 1 | data) = 1048576/1108650 = 524288/554325",
                "P(next sunrise | data) = 43735/44346, just under 1",
                "skeptic's prior: P(next sunrise | data) = 1382119/1763994",
            ],
            "after": [
                "The first predictive probability is `1 − 611/44346`, so the uniform prior is certain "
                "enough to bet on and never certain. The second is about `0.78`. The ten sunrises were "
                "identical; the skeptic's prior started with almost nothing on the hypotheses that "
                "ten sunrises favour, and ten sunrises were not enough to undo that."
            ],
        },
        "quiz_title": "What the sunrises license",
        "quiz": [
            {"q": "&ldquo;The sun has risen on each of ten days, so it will rise on the eleventh.&rdquo; "
                  "Which statement about this argument is correct?",
             "a": ["It is valid, because ten is a large enough sample",
                   "It is invalid: there is a row with every premise true and the conclusion false",
                   "It is valid only if the sun has in fact risen on every day so far",
                   "It is invalid only for small samples and valid for large ones"],
             "c": 1,
             "why": "Validity is the absence of a counterexample row, and the row with day 11 false "
                    "survives any number of premises about earlier days. The first and fourth treat "
                    "sample size as if it changed the form; the third confuses validity with the truth "
                    "of the premises."},
            {"q": "The skeptic's lab run and the uniform run use the same ten sunrises but give "
                  "different predictive probabilities. What explains the difference?",
             "a": ["The skeptic's run uses different data",
                   "The skeptic's run uses different likelihoods for the sun rising",
                   "The lab rounds the two answers differently",
                   "The two priors weight the hypotheses differently, and the data do not remove the gap"],
             "c": 3,
             "why": "Only the prior row differs between the two runs. The data and the likelihood table are "
                    "identical, and every figure is an exact fraction, so nothing is rounded."},
            {"q": "In Hume's terms, what does the prior in the lab supply?",
             "a": ["The observed sunrises themselves",
                   "A deduction of the eleventh sunrise from the first ten",
                   "A premise about how the unobserved relates to the observed, which the data cannot supply",
                   "A proof that the sun will rise tomorrow"],
             "c": 2,
             "why": "The data are the ten sunrises and are entered separately. The prior is the premise "
                    "that closes the gap the row opens, and the lab computes what follows from it without "
                    "saying whether it is justified."},
            {"q": "Under the uniform prior over the five chances, can the probability of another sunrise "
                  "reach exactly 1 after some finite run of sunrises?",
             "a": ["No: the chance 3/4 keeps a positive posterior after any finite run, because 3/4 to "
                   "the power n is never 0",
                   "Yes, after about a hundred sunrises",
                   "Yes, as soon as the posterior of chance 1 passes 1/2",
                   "No, because the chance 1 hypothesis gives the sunrises probability 0"],
             "c": 0,
             "why": "Each run of n sunrises has probability (3/4)ⁿ under chance 3/4, which is positive for "
                    "every n, so that hypothesis keeps some posterior and the prediction stays below 1. "
                    "The chance 1 hypothesis gives sunrises probability 1, not 0, and passing 1/2 only "
                    "makes the prediction large."},
        ],
        "mistakes": [
            ("Thinking a large sample makes induction valid",
             "Ten sunrises and ten million have the same defect: a row on which the premises are true "
             "and the next case is not. A large sample raises the probability of the conclusion under a "
             "prior; it never turns the argument into a deduction."),
            ("Reading the posterior as if the data had produced it alone",
             "The posterior is the prior reweighted. The skeptic and the optimist start from different "
             "priors, see the same ten sunrises, and end with predictions that are about `0.78` and "
             "`0.99`. Where the prior came from is exactly Hume's question."),
            ("Thinking the problem is that induction fails",
             "Induction has worked in every case we have checked. Hume's point is about justification: "
             "using that record to defend induction is itself an inductive argument, and the lab shows "
             "what any version of it has to assume."),
        ],
        "standard": (
            "Finish when you can construct the row and compute the prediction.",
            "Given an inductive argument, you should be able to write the row that makes it invalid, "
            "state the premise a prior would supply, and compute the predictive probability under two "
            "priors from the lab, saying which part of the difference is the prior's."
        ),
        "note": (
            "The five chances are a discretisation chosen so every figure is an exact fraction. A finer "
            "set of hypotheses changes the numbers and not the lesson. “Grue and the New Riddle” asks "
            "why the hypotheses were these five and not some others."
        ),
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "grue-and-the-new-riddle",
        "title": "Grue and the New Riddle",
        "module": "Induction",
        "one_line": "Two hypotheses can fit every observation and differ in the future, and the data cannot choose.",
        "summary": (
            "Define &ldquo;grue&rdquo; so that every emerald examined so far is both green and grue. The "
            "two hypotheses assign the same probability to every observation before the critical time, so "
            "their Bayes factor is exactly 1 and the posterior ratio equals the prior ratio. Which "
            "predicate is projectible is a fact about the prior."
        ),
        "key": [
            "grue: green if seen before t, else blue",
            "same rows before t: BF = 1 exactly",
            "posterior ratio = prior ratio",
            "100 green emeralds do not separate them",
        ],
        "key_label": "Two hypotheses, one record",
        "concepts_intro": (
            "Hume asked what justifies projecting the past into the future. Goodman's new riddle asks which "
            "pattern in the past to project."
        ),
        "concepts": [
            ("Grue agrees with green until t",
             "An object is grue if it is examined before time `t` and green, or not so examined and blue. "
             "Every emerald examined before `t` that was green was therefore grue as well."),
            ("A Bayes factor of 1 means the data did not discriminate",
             "If two hypotheses give the observed data the same probability, the data move neither "
             "relative to the other, however many observations there are."),
            ("Projectibility lives in the prior",
             "Treating green as projectible and grue as not is a judgement made before the data, since "
             "the data are the same for both."),
        ],
        "read_title": "Defining the rival",
        "read_intro": "The definition first, then the table of what each hypothesis says, then the arithmetic.",
        "body": [
            ("p", "Every emerald ever examined has been green. That supports &ldquo;all emeralds are "
                  "green&rdquo;, and by the reasoning of the last lesson it supports &ldquo;the next "
                  "emerald will be green&rdquo;. Now introduce a word."),
            ("def", ("Grue",
                     "Fix a time `t` in the future. An object is <strong>grue</strong> if it is examined "
                     "before `t` and is green, or is not examined before `t` and is blue.")),
            ("p", "Every emerald examined so far was examined before `t` and was green, so it was grue. "
                  "&ldquo;All emeralds are grue&rdquo; has exactly as much observed support as &ldquo;all "
                  "emeralds are green&rdquo;, and the two predict opposite colours for the first emerald "
                  "examined after `t`."),
            ("math", [
                "an emerald examined   H-green says   H-grue says",
                "-----------------------------------------------",
                "before t              green           green",
                "after t               green           blue",
            ]),
            ("p", "The lab takes two outcomes, green and blue, for an emerald as examined. Before `t` both "
                  "hypotheses give green probability 1, so their likelihood rows are identical. Put "
                  "the prior `3/4` on green and `1/4` on grue and enter 100 green emeralds."),
            ("thm", ("Identical rows give a Bayes factor of 1",
                     "If `P(data | H) = P(data | H′)` then the Bayes factor of `H` against `H′` is `1`, and "
                     "the posterior odds equal the prior odds. With only these two hypotheses it follows "
                     "that the posterior of `H` equals its prior.")),
            ("p", "The lab prints exactly that: the Bayes factor is 1, the posterior of green is still "
                  "`3/4`, and the tile that classifies the data says they are neutral. One hundred "
                  "emeralds and one thousand do the same, because each multiplies both likelihoods by 1."),
            ("p", "The second preset adds the one difference that matters. Suppose the next emerald is "
                  "examined after `t` and is green. Under grue it should have been blue, so grue gives "
                  "it probability 0 and green gives it 1. The Bayes factor is infinite, the posterior of "
                  "green is 1, and the lab says the data prove green against this one rival. Until such "
                  "an observation arrives, nothing in the evidence tells the hypotheses apart."),
            ("p", "Goodman's riddle is that no formal feature of the data prefers green to grue. The standard "
                  "replies place the difference elsewhere. One says grue is gerrymandered, because it "
                  "mentions a time; but a speaker of a language with grue and bleen as primitives would "
                  "call green the gerrymandered word. Another says natural kinds are the projectible ones, "
                  "which relocates the question to what makes a kind natural. Each is a claim about the "
                  "prior, and the lab can show that it must be."),
            ("p", "The lab's limit is the same as in the last lesson: it computes from the prior it is "
                  "given. It does not say that `3/4` on green is the right number, and a reader who sets "
                  "the prior on grue at `3/4` gets the mirror result."),
        ],
        "lab": ("choicekit", {
            "mode": "update",
            "preset": "grue",
            "presets": [
                {"id": "grue",
                 "label": "Green and grue, 100 green emeralds before t",
                 "hyps": ["green", "grue"],
                 "prior": ["3/4", "1/4"],
                 "outcomes": ["green", "blue"],
                 "lik": [["1", "0"], ["1", "0"]],
                 "data": ["green"] * 100,
                 "payoffs": None,
                 "expect": {"upBF": "1", "upConf": "Neutral", "upPost": "3/4"}},
                {"id": "tell",
                 "label": "One emerald examined after t, found green",
                 "hyps": ["green", "grue"],
                 "prior": ["3/4", "1/4"],
                 "outcomes": ["green", "blue"],
                 "lik": [["1", "0"], ["0", "1"]],
                 "data": "green",
                 "payoffs": None,
                 "expect": {"upBF": "infinite", "upConf": "Proves", "upPost": "1"}},
            ],
        }),
        "steps_title": "Testing whether data favour one hypothesis",
        "steps_intro": "Four steps, applied to any pair of rival hypotheses.",
        "steps": [
            ("Write what each predicts",
             "For each observation you have, record the probability each hypothesis gave it. Do this "
             "before computing anything."),
            ("Compare the rows",
             "If the two rows agree on every outcome that occurred, the Bayes factor is exactly 1 and "
             "the data are idle between them."),
            ("Find the outcome where they differ",
             "Look for an observation, possible in principle, on which the rows disagree. That is the "
             "only kind of evidence that can separate them."),
            ("Ask where the preference came from",
             "If you favoured one hypothesis while the Bayes factor was 1, the preference came from the "
             "prior. Say what justified it."),
        ],
        "worked": {
            "title": "A hundred green emeralds",
            "intro": ["Prior `3/4` on green and `1/4` on grue; both give a green emerald probability 1 before `t`."],
            "lines": [
                "likelihood of the data under green: 1 to the 100th = 1",
                "likelihood of the data under grue:  1 to the 100th = 1",
                "Bayes factor of green against grue: 1/1 = 1",
                "posterior of green: (3/4 · 1) / (3/4 · 1 + 1/4 · 1) = 3/4",
                "prior ratio 3 to 1; posterior ratio 3 to 1",
            ],
            "after": [
                "The posterior ratio equals the prior ratio to the digit. One hundred emeralds were "
                "examined, and the evidence for green is exactly the evidence for grue."
            ],
        },
        "quiz_title": "Green, grue and the data",
        "quiz": [
            {"q": "A hundred green emeralds examined before `t`. What is the Bayes factor of green "
                  "against grue?",
             "a": ["100", "Greater than 1 but less than 100", "0", "1"],
             "c": 3,
             "why": "Both hypotheses give each green emerald probability 1, so the likelihood of the "
                    "data is 1 under each and the ratio is 1. A hundred supporting instances each "
                    "multiply both sides by 1."},
            {"q": "Which of these would be evidence that separates green from grue?",
             "a": ["A thousand more green emeralds examined before `t`",
                   "The fact that grue mentions a time",
                   "A green emerald examined after `t`",
                   "A hundred green sapphires examined before `t`"],
             "c": 2,
             "why": "Only an observation on which the likelihood rows differ can change the ratio, and "
                    "that is a green emerald after `t`, where grue predicts blue. More of the same "
                    "observations and observations of other gems leave the rows equal."},
            {"q": "If the prior on green is 3/4 and on grue 1/4, what is the posterior of green after the "
                  "hundred green emeralds?",
             "a": ["Close to 1, but not exactly", "3/4", "1/2", "100/101"],
             "c": 1,
             "why": "With a Bayes factor of 1 the posterior odds equal the prior odds, so the posterior "
                    "of green is its prior, 3/4. The other values would require the data to favour "
                    "green, which they do not."},
        ],
        "mistakes": [
            ("Thinking more green emeralds favour green over grue",
             "Each green emerald examined before `t` has probability 1 under both hypotheses. The Bayes "
             "factor stays at exactly 1 after one emerald and after a hundred, and the posterior ratio "
             "is the prior ratio, so the count of green emeralds is no argument at all."),
            ("Treating &ldquo;grue&rdquo; as a trick of language that the data can sweep aside",
             "The hypothesis is as well defined as green and fits as well. It is excluded by a judgement "
             "that colours are projectible and time-indexed colours are not, and that judgement is "
             "prior to the data."),
            ("Concluding that induction is hopeless",
             "The lab shows only that induction needs a prior that treats some predicates as "
             "projectible. A reader can hold such a prior, defend it, and compute with it; what cannot be "
             "done is to derive it from the observations it is applied to."),
        ],
        "standard": (
            "Finish when you can show a Bayes factor of 1 and say what follows.",
            "Given two hypotheses and a record of observations, you should be able to write their "
            "likelihood rows, show that the Bayes factor is 1, compute the posterior from the prior, "
            "and name the kind of observation that would separate them."
        ),
        "note": (
            "The time `t` is stipulated and never reached by the data in the first preset; the second "
            "preset is the one where it is reached. Some authors prefer to make the riddle about "
            "properties rather than times, and the arithmetic of identical rows is the same."
        ),
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "confirmation-and-the-weight-of-evidence",
        "title": "Confirmation and the Weight of Evidence",
        "module": "Confirmation",
        "one_line": "Evidence confirms a hypothesis when it raises its probability, and the Bayes factor measures how much.",
        "summary": (
            "Evidence confirms a hypothesis when the posterior exceeds the prior, and its weight is the "
            "Bayes factor, the ratio of the probability of the evidence under the hypothesis to its "
            "probability under the alternative. Evidence that is merely consistent with a hypothesis "
            "need not confirm it, and surprising evidence confirms more than expected evidence."
        ),
        "key": [
            "E confirms H  ⟺  P(H | E) > P(H)",
            "weight: BF = P(E | H) / P(E | ¬H)",
            "BF > 1 confirms; BF = 1 neutral; BF < 1 not",
            "surprising E weighs more than expected E",
        ],
        "key_label": "Confirmation and its weight",
        "concepts_intro": (
            "Confirmation is a relation between evidence and a hypothesis. This lesson defines it by "
            "probability and measures it by a ratio."
        ),
        "concepts": [
            ("Confirmation is raising probability",
             "`E` confirms `H` when `P(H | E) > P(H)`, disconfirms it when the inequality reverses, "
             "and is neutral when the two are equal. It is a comparison of two numbers, not a property of "
             "`E` alone."),
            ("Weight is the Bayes factor",
             "`P(E | H) / P(E | ¬H)` says how much more probable the evidence is if the hypothesis is "
             "true than if it is false. It is the same whatever the prior."),
            ("Surprise carries weight",
             "Evidence that was improbable on the alternative and probable on the hypothesis has a large "
             "factor. Evidence expected either way has one near 1."),
        ],
        "read_title": "Probability up, and by how much",
        "read_intro": "A definition, a measure, and three cases that differ only in one likelihood.",
        "body": [
            ("p", "“Updating on Evidence” gave the procedure for revising a probability on new "
                  "evidence. This lesson asks what to call the result. A reasonable rule is that the "
                  "evidence supports the hypothesis if, and only if, the hypothesis is more probable "
                  "afterwards than before."),
            ("def", ("Confirmation",
                     "<strong>`E` confirms `H`</strong> when `P(H | E) > P(H)`. It <strong>disconfirms</strong> "
                     "`H` when `P(H | E) < P(H)` and is <strong>neutral</strong> when they are equal.")),
            ("p", "That is a qualitative verdict. To compare how strongly two pieces of evidence confirm, "
                  "the usual measure is the factor by which they multiply the odds in favour of the "
                  "hypothesis."),
            ("thm", ("Odds form of Bayes' rule",
                     "`posterior odds = BF · prior odds`, where `BF = P(E | H) / P(E | ¬H)`. So `E` confirms "
                     "`H` exactly when `BF > 1`, and the factor does not depend on the prior.")),
            ("p", "Three cases share a prior of `1/2` on `H` and the same likelihood for the evidence "
                  "under `H`, namely `P(E | H) = 1`. They differ only in how probable `E` is if `H` is false."),
            ("math", [
                "case         P(E | H)   P(E | not H)   Bayes factor   P(H | E)",
                "-------------------------------------------------------------",
                "surprising      1          1/10            10          10/11",
                "expected        1          9/10           10/9         10/19",
                "neutral         1            1              1           1/2",
            ]),
            ("p", "In every row `E` is perfectly consistent with `H`, because `H` makes it certain. Yet the "
                  "verdicts are different. In the first row the evidence would rarely occur unless `H` "
                  "were true, so seeing it is strong support. In the second it would very probably have "
                  "occurred anyway, so it supports `H` only slightly. In the third it would have occurred "
                  "whatever, and it supports nothing."),
            ("p", "The third row is the one that corrects an easy mistake. That a hypothesis predicts the "
                  "evidence is not the same as the evidence confirming the hypothesis. &ldquo;The sun "
                  "rose this morning&rdquo; is predicted by every theory of the heavens anyone takes "
                  "seriously, and so confirms none of them against the others."),
            ("p", "The limit of the lab is in the second likelihood. `P(E | ¬H)` is an average over every "
                  "way `H` could be false, weighted by their priors, and it is a number you chose. Change "
                  "it and the same evidence changes weight, which is why two scientists can agree on the "
                  "observation and disagree on what it shows."),
        ],
        "lab": ("choicekit", {
            "mode": "update",
            "preset": "surprising",
            "presets": [
                {"id": "surprising",
                 "label": "Surprising: the evidence is rare if H is false",
                 "hyps": ["H", "not-H"],
                 "prior": ["1/2", "1/2"],
                 "outcomes": ["E", "no-E"],
                 "lik": [["1", "0"], ["1/10", "9/10"]],
                 "data": "E",
                 "payoffs": None,
                 "expect": {"upBF": "10", "upConf": "Confirms", "upPost": "10/11"}},
                {"id": "expected",
                 "label": "Expected: the evidence is common if H is false",
                 "hyps": ["H", "not-H"],
                 "prior": ["1/2", "1/2"],
                 "outcomes": ["E", "no-E"],
                 "lik": [["1", "0"], ["9/10", "1/10"]],
                 "data": "E",
                 "payoffs": None,
                 "expect": {"upBF": "10/9", "upConf": "Confirms", "upPost": "10/19"}},
                {"id": "neutral",
                 "label": "Neutral: the evidence is certain either way",
                 "hyps": ["H", "not-H"],
                 "prior": ["1/2", "1/2"],
                 "outcomes": ["E", "no-E"],
                 "lik": [["1", "0"], ["1", "0"]],
                 "data": "E",
                 "payoffs": None,
                 "expect": {"upBF": "1", "upConf": "Neutral", "upPost": "1/2"}},
            ],
        }),
        "steps_title": "Weighing a piece of evidence",
        "steps_intro": "Four steps, in this order.",
        "steps": [
            ("State the hypothesis and its negation",
             "Name `H` and everything that is not `H`. The alternative is part of the question; evidence "
             "has weight only against it."),
            ("Find both likelihoods",
             "Write `P(E | H)` and `P(E | ¬H)`. The second is a mixture over the ways `H` could fail, "
             "weighted by their priors."),
            ("Take the ratio",
             "Divide the first by the second. A result above 1 confirms, 1 is neutral and below 1 "
             "disconfirms."),
            ("Apply it to the prior odds",
             "Multiply the prior odds by the factor to get the posterior odds, and convert back to a "
             "probability if you need one."),
        ],
        "worked": {
            "title": "The same prior, two kinds of evidence",
            "intro": ["Prior `1/2` on `H`, and `P(E | H) = 1`. The only difference is `P(E | ¬H)`."],
            "lines": [
                "surprising: BF = 1 / (1/10) = 10",
                "  prior odds 1 to 1, posterior 10 to 1, P(H | E) = 10/11",
                "expected:   BF = 1 / (9/10) = 10/9",
                "  prior odds 1 to 1, posterior 10 to 9, P(H | E) = 10/19",
                "neutral:    BF = 1 / 1 = 1",
                "  posterior = prior = 1/2",
            ],
            "after": [
                "The evidence is the same sentence in all three, and `H` predicts it with certainty in "
                "all three. A factor of 10 and a factor of `10/9` differ in weight by the ratio "
                "`9` to `1`, and that difference comes from the alternative alone."
            ],
        },
        "quiz_title": "Does it confirm, and how much",
        "quiz": [
            {"q": "`H` predicts `E` with certainty, and `E` is observed. What follows?",
             "a": ["`E` confirms `H`",
                   "`E` confirms `H` if and only if `P(E | ¬H) < 1`",
                   "`E` confirms `H` by exactly the prior of `H`",
                   "`E` disconfirms `H` unless `P(E | ¬H) = 1`"],
             "c": 1,
             "why": "With `P(E | H) = 1` the factor is `1 / P(E | ¬H)`, which exceeds 1 exactly when the "
                    "alternative gives `E` probability below 1. If it gives `E` probability 1 the "
                    "factor is 1 and `E` is neutral, which rules out the first choice, and a factor "
                    "of at least 1 can never disconfirm, which rules out the last."},
            {"q": "In the surprising and expected cases the prior and `P(E | H)` are the same. What "
                  "makes the first stronger?",
             "a": ["`E` is less probable if `H` is false",
                   "`E` is more probable if `H` is false",
                   "The posterior is computed differently",
                   "The prior is higher"],
             "c": 0,
             "why": "The factor is `1 / P(E | ¬H)`, so a smaller alternative likelihood (1/10 against "
                    "9/10) gives a larger factor (10 against 10/9). The prior and the rule are the same "
                    "in both."},
            {"q": "`P(E | H) = P(E | ¬H) = 1/2`. What is the Bayes factor, and what is the verdict?",
             "a": ["1/2; disconfirms", "2; confirms", "1; neutral", "0; refutes"],
             "c": 2,
             "why": "A ratio of equal likelihoods is 1, and a factor of 1 leaves the odds where they "
                    "were: neutral. A factor of 1/2 or 2 would need unequal likelihoods, and 0 would "
                    "need `P(E | H) = 0`."},
            {"q": "A hypothesis with prior 1/2 meets evidence with Bayes factor 3. What are its "
                  "posterior odds?",
             "a": ["1 to 3", "3 to 2", "1 to 1", "3 to 1"],
             "c": 3,
             "why": "Posterior odds are the factor times the prior odds: 3 · (1 to 1) = 3 to 1. The "
                    "other options mistake the factor for a probability or invert it."},
        ],
        "mistakes": [
            ("Thinking evidence consistent with a hypothesis confirms it",
             "In the neutral case `H` predicts `E` with certainty and `E` is observed, and the posterior "
             "stays exactly at the prior `1/2`, because the alternative predicted `E` with certainty "
             "too. Consistency says only that the likelihood is not 0; confirmation compares it with "
             "the alternative's."),
            ("Measuring confirmation without an alternative",
             "`P(E | H)` alone settles nothing. The same value of 1 gives a factor of 10, `10/9` or 1 "
             "as `P(E | ¬H)` moves from `1/10` to `9/10` to 1."),
            ("Treating the Bayes factor as the probability of the hypothesis",
             "A factor of 10 means the odds are multiplied by 10. From a prior of `1/2` that gives "
             "`10/11`; from a prior of `1/100` it gives `10/109`, nowhere near certainty."),
        ],
        "standard": (
            "Finish when you can classify a piece of evidence and give its weight.",
            "Given a prior and two likelihoods you should be able to compute the Bayes factor, say "
            "whether the evidence confirms, disconfirms or is neutral, and compute the posterior from "
            "the prior odds."
        ),
        "note": (
            "Probability-raising is one of several measures of confirmation, and the Bayes factor is "
            "one of several ways to weigh it. They agree on the verdict and can disagree on the "
            "comparison between two cases with different priors; the cases here share a prior."
        ),
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "falsification-and-what-a-theory-forbids",
        "title": "Falsification and What a Theory Forbids",
        "module": "Confirmation",
        "one_line": "An outcome a hypothesis forbids refutes it for good; no run of allowed outcomes proves it; and a hypothesis that predicts exactly what its rival predicts is never moved.",
        "summary": (
            "A hypothesis forbids the outcomes it gives probability 0. One such observation drives its "
            "posterior to 0 whatever the prior, while any number of allowed observations leaves it short "
            "of 1. A hypothesis with no zero in its row cannot be refuted, and one whose row matches its "
            "rival's cannot be moved at all; the more a theory forbids, the more it gains when it survives."
        ),
        "key": [
            "forbids o  ⟺  P(o | H) = 0",
            "o observed ⟹ P(H | data) = 0, any prior",
            "no zero in the row ⟹ never refuted",
            "same row as the rival ⟹ never moved",
            "survival is worth more when more is forbidden",
        ],
        "key_label": "What a theory forbids",
        "concepts_intro": (
            "Popper's thought was that a theory is scientific to the degree that it says what cannot "
            "happen. In probability terms that is a likelihood of zero."
        ),
        "concepts": [
            ("A forbidden outcome is a likelihood of zero",
             "If `P(o | H) = 0` then observing `o` makes `P(H | o) = 0`, whatever `P(H)` was. No prior "
             "survives it except a prior of exactly 1 that was never really in doubt."),
            ("Confirmation never reaches proof",
             "Evidence that raises `P(H)` leaves it below 1 as long as some rival gave the data positive "
             "probability. A refutation is final; a confirmation is not."),
            ("A theory that forbids nothing risks nothing",
             "A hypothesis with no zero in its row cannot be refuted by any single observation. If its "
             "row also matches its rival's, nothing can move it at all, and survival is worth nothing. "
             "Between the two lies every hypothesis whose row differs from its rival's without a zero: "
             "those are moved, by the Bayes factor of the last lesson, and never to 0."),
        ],
        "read_title": "The asymmetry in the numbers",
        "read_intro": "One forbidden outcome, one theory that forbids nothing, and one that forbids a great deal.",
        "body": [
            ("p", "Take a hypothesis `H` and three possible outcomes, `o1`, `o2` and `o3`. Suppose `H` "
                  "gives probability `1/2` to each of the first two and `0` to the third: it forbids "
                  "`o3`. A rival, which is just not-`H`, gives each outcome `1/3`. Give `H` a prior of "
                  "`99/100`."),
            ("def", ("Forbidden outcome",
                     "An outcome is <strong>forbidden</strong> by `H` when `P(o | H) = 0`. A hypothesis "
                     "is <strong>falsifiable</strong> to the extent that it forbids some outcome that "
                     "can be observed.")),
            ("p", "Now observe `o3`. The likelihood of the data under `H` is 0, so the joint probability "
                  "of `H` and the data is 0 and the posterior is 0. The lab calls that refuted, and the "
                  "Bayes factor is 0. Nothing about the prior of `99/100` mattered; multiplying anything by 0 "
                  "gives 0."),
            ("thm", ("The asymmetry of refutation",
                     "If `P(o | H) = 0` and `o` is observed, then `P(H | o) = 0` for every prior. But "
                     "if `P(o | H) > 0` for every observed `o`, and a rival gives some of them positive "
                     "probability, then `P(H | data) < 1` however many there are.")),
            ("p", "The second half is the one the misconception ignores. Feed the same hypothesis ten "
                  "observations of `o1`, which it allows, and its posterior rises from `99/100` to "
                  "`5845851/5846875`, about `0.9998`, and does not reach 1, because the rival never gave `o1` probability 0. The lab "
                  "reports the verdict as &ldquo;confirms&rdquo;, not &ldquo;proves&rdquo;. One refuting "
                  "observation does what no number of confirming ones can."),
            ("p", "The preset for a hypothesis that forbids nothing takes the opposite case: no zero in its "
                  "row, and the same row as its rival, `1/3` on each outcome. Whatever is observed, the two "
                  "likelihoods are equal at every step, so the posterior is the prior and the lab calls the "
                  "data neutral. Two things are true of this hypothesis, and they should be kept apart. "
                  "Because it has no zero, no single observation can refute it. Because its row matches "
                  "its rival's, nothing can confirm it either. Edit its row to `1/2`, `1/4`, `1/4` and the "
                  "first stays true while the second fails: the hypothesis still forbids nothing, and the "
                  "same four observations now confirm it, by a factor of `81/64`. The slogan that a theory "
                  "which forbids nothing risks nothing is exact about refutation and a limiting case about "
                  "the rest. The general measure of what a theory risks is how far its row departs from "
                  "its rival's, and a zero is the furthest it can go."),
            ("p", "Between the two lies the last preset. `H` now forbids two of the three outcomes and "
                  "gives all its probability to `o1`. Observing `o1` is what `H` said would happen, "
                  "and the rival, which spread its probability, gave it only `1/3`. The factor is 3, "
                  "and `H` goes from `1/2` to `3/4`. The more a hypothesis forbids, the more its "
                  "survival counts."),
            ("p", "Popper himself refused the reading given here. On his account a theory that survives a "
                  "severe test is corroborated, not made more probable; he held that every universal law "
                  "has probability 0 on any evidence, and that the search for probable theories is the "
                  "wrong aim, since the most probable hypothesis is the one that says least. The lesson "
                  "borrows his asymmetry and puts it into the frame he rejected. A reader who follows him "
                  "keeps the first tile of the first preset, the 0, and declines to read the posteriors "
                  "of the others as anything but bookkeeping; what that reader then owes is an account of "
                  "why a corroborated theory should be relied on, which Popper agreed he could not give."),
            ("p", "None of this makes falsification a procedure. A theory is rarely tested alone, and "
                  "“The Duhem–Quine Problem” asks what a forbidden outcome refutes when the prediction "
                  "depends on more than the theory. What the lab shows is only the arithmetic: a "
                  "likelihood of zero is the strongest thing a hypothesis can stake."),
        ],
        "lab": ("choicekit", {
            "mode": "update",
            "preset": "popper",
            "presets": [
                {"id": "popper",
                 "label": "H forbids o3, and o3 is observed",
                 "hyps": ["H", "not-H"],
                 "prior": ["99/100", "1/100"],
                 "outcomes": ["o1", "o2", "o3"],
                 "lik": [["1/2", "1/2", "0"], ["1/3", "1/3", "1/3"]],
                 "data": "o3",
                 "payoffs": None,
                 "expect": {"upBF": "0", "upConf": "Refutes", "upPost": "0"}},
                {"id": "confirmed",
                 "label": "The same H, o1 observed ten times",
                 "hyps": ["H", "not-H"],
                 "prior": ["99/100", "1/100"],
                 "outcomes": ["o1", "o2", "o3"],
                 "lik": [["1/2", "1/2", "0"], ["1/3", "1/3", "1/3"]],
                 "data": ["o1"] * 10,
                 "payoffs": None,
                 "expect": {"upConf": "Confirms", "upPost": "5845851/5846875"}},
                {"id": "unfalsifiable",
                 "label": "A hypothesis that forbids nothing",
                 "hyps": ["H", "not-H"],
                 "prior": ["99/100", "1/100"],
                 "outcomes": ["o1", "o2", "o3"],
                 "lik": [["1/3", "1/3", "1/3"], ["1/3", "1/3", "1/3"]],
                 "data": "o1 o2 o3 o1",
                 "payoffs": None,
                 "expect": {"upBF": "1", "upConf": "Neutral", "upPost": "99/100"}},
                {"id": "risky",
                 "label": "H forbids two of three outcomes, o1 observed",
                 "hyps": ["H", "not-H"],
                 "prior": ["1/2", "1/2"],
                 "outcomes": ["o1", "o2", "o3"],
                 "lik": [["1", "0", "0"], ["1/3", "1/3", "1/3"]],
                 "data": "o1",
                 "payoffs": None,
                 "expect": {"upBF": "3", "upConf": "Confirms", "upPost": "3/4"}},
            ],
        }),
        "steps_title": "Reading what a hypothesis forbids",
        "steps_intro": "Four steps, applied to any hypothesis with a row of likelihoods.",
        "steps": [
            ("List the outcomes with likelihood 0",
             "Scan the hypothesis's row for zeros. Those are the outcomes it forbids, and they are what "
             "makes it falsifiable."),
            ("Check the data against the zeros",
             "If any observed outcome sits under a zero, the posterior is 0 and the work is over; no "
             "prior or further data can restore it."),
            ("Otherwise compare with the rivals",
             "If nothing forbidden occurred, the Bayes factor against the rivals gives the confirmation. "
             "A row identical to a rival's gives a factor of 1."),
            ("Note how much was staked",
             "The more outcomes forbidden, the larger the factor when the data fall in the allowed "
             "region. Compare the surviving factor with the share of outcomes that were allowed."),
        ],
        "worked": {
            "title": "A prior of 99/100 and one forbidden outcome",
            "intro": ["The hypothesis `H` forbids `o3`; its rival gives every outcome `1/3`."],
            "lines": [
                "P(o3 | H) = 0, P(o3 | not-H) = 1/3",
                "joint probability of H and o3: 99/100 · 0 = 0",
                "joint probability of not-H and o3: 1/100 · 1/3 = 1/300",
                "P(H | o3) = 0 / (0 + 1/300) = 0",
                "Bayes factor = 0",
            ],
            "after": [
                "One observation took `99/100` to 0. Had the prior been `999999/1000000` the result would "
                "have been the same, because the joint probability would still be 0."
            ],
        },
        "quiz_title": "Forbidding and surviving",
        "quiz": [
            {"q": "`H` gives outcome `o` probability 0, and `o` is observed. What is `P(H | o)`?",
             "a": ["0 whatever the prior of `H`, provided the prior of `o` is positive",
                   "The prior of `H` divided by two",
                   "It depends on how large the prior of `H` was",
                   "1, because `H` survived"],
             "c": 0,
             "why": "The joint probability of `H` and `o` is the prior times 0, so the posterior is 0 "
                    "for every prior. The prior of the observation overall must be positive for the "
                    "posterior to be defined, which it is when some rival allows it."},
            {"q": "A hypothesis that allows every outcome and shares its rival's likelihoods is "
                  "observed to succeed in twenty tests. What happens to its probability?",
             "a": ["It rises towards 1 with each test",
                   "It falls with each test",
                   "It reaches exactly 1 after enough tests",
                   "It stays at its prior"],
             "c": 3,
             "why": "Equal likelihoods give a Bayes factor of 1 at every test, so nothing changes. "
                    "Rising and falling would need unequal likelihoods, and reaching 1 would need the "
                    "rival to forbid something observed."},
            {"q": "`H` has been confirmed by one hundred observations it allowed. Which statement is "
                  "correct?",
             "a": ["Its probability is exactly 1",
                   "Its probability may be very high, but is below 1 as long as a rival allowed those "
                   "observations",
                   "It can no longer be refuted",
                   "Its probability is 99/100"],
             "c": 1,
             "why": "A rival that gave the data positive probability keeps a positive posterior, so "
                    "`H` stays short of 1, and a later forbidden outcome would still send it to 0. "
                    "The 99/100 is just the prior in the lesson's example."},
        ],
        "mistakes": [
            ("Thinking a theory confirmed many times is proven",
             "Ten observations of `o1` take `H` from `99/100` to a figure close to 1 and not equal to it, "
             "because the rival gave `o1` probability `1/3`. The lab labels this &ldquo;confirms&rdquo;, "
             "and a single `o3` afterwards would still bring it to 0."),
            ("Thinking an unfalsifiable theory is the best-supported one",
             "A theory that forbids nothing is never contradicted, but with likelihoods equal to its "
             "rival's it is never confirmed either. The posterior equals the prior at every step."),
            ("Reading a likelihood of zero as a prior of zero",
             "A prior is what you believed before the data. A likelihood of zero is what the "
             "hypothesis says about an outcome. The first can be moved by evidence and the second is "
             "the reason one observation moves it all the way."),
        ],
        "standard": (
            "Finish when you can identify what a hypothesis forbids and compute the effect.",
            "Given a row of likelihoods you should be able to list the forbidden outcomes, say what "
            "happens to the posterior if one occurs, and say what happens if only allowed outcomes occur."
        ),
        "note": (
            "In the lab the rival is simply not-H, and its row is a stated average of the other ways "
            "H could fail. A real theory has a particular rival or several, and the Bayes factor "
            "changes with which."
        ),
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "the-raven-paradox",
        "title": "The Raven Paradox",
        "module": "Confirmation",
        "one_line": "A white shoe confirms that all ravens are black, by a factor so close to 1 that it barely counts.",
        "summary": (
            "Nicod's condition and the equivalence condition together entail that a white shoe confirms "
            "&ldquo;all ravens are black&rdquo;. Sampling from the non-black objects shows how little: "
            "the Bayes factor is 901/900, against 10/9 for a black raven sampled from the ravens. Both "
            "confirm; the asymmetry is in the sampling."
        ),
        "key": [
            "Nicod: a black raven confirms the law",
            "equivalent hypotheses are confirmed together",
            "white shoe: BF 901/900. black raven: 10/9",
            "confirmation comes in degrees, not all-or-none",
        ],
        "key_label": "Two conditions, one paradox",
        "concepts_intro": (
            "Hempel's paradox is a valid argument from two plausible conditions to an implausible "
            "conclusion. The way out is to ask how much."
        ),
        "concepts": [
            ("Nicod's condition",
             "An instance of &ldquo;all F are G&rdquo;, an F that is G, confirms it. A black raven "
             "confirms &ldquo;all ravens are black&rdquo;."),
            ("The equivalence condition",
             "Whatever confirms a hypothesis confirms every hypothesis logically equivalent to it. "
             "&ldquo;All ravens are black&rdquo; and &ldquo;every non-black thing is a non-raven&rdquo; "
             "say the same thing."),
            ("Degree, not kind",
             "Both conditions can stand if confirmation is a matter of degree and the degrees differ "
             "enormously with how the evidence was gathered."),
        ],
        "read_title": "A white shoe, and the sampling behind it",
        "read_intro": "First the argument, then the question it leaves, then the arithmetic that answers it.",
        "body": [
            ("p", "Write `R(x)` for &ldquo;`x` is a raven&rdquo; and `B(x)` for &ldquo;`x` is black&rdquo;. "
                  "The hypothesis is `R(x) → B(x)` for every `x`. Its contrapositive, which "
                  "“Equivalence, De Morgan and Contraposition” shows to be equivalent, is `¬B(x) → ¬R(x)` "
                  "for every `x`."),
            ("math", [
                "R   B  |  R → B   ¬B → ¬R",
                "--------------------------",
                "T   T  |    T        T",
                "T   F  |    F        F",
                "F   T  |    T        T",
                "F   F  |    T        T",
            ]),
            ("p", "The columns agree on every row, so the two hypotheses are equivalent. Now run the "
                  "argument. By Nicod, a non-black non-raven, a white shoe, is an instance of the "
                  "second hypothesis, so it confirms it. By equivalence it confirms the first. So a "
                  "white shoe confirms that all ravens are black, and one need not leave the room."),
            ("def", ("The two conditions",
                     "<strong>Nicod's condition:</strong> an object that is F and G confirms &ldquo;all F "
                     "are G&rdquo;. <strong>Equivalence condition:</strong> evidence that confirms one "
                     "hypothesis confirms every hypothesis logically equivalent to it.")),
            ("p", "Each condition is hard to reject. What can be rejected is the assumption that the "
                  "conclusion is absurd, once confirmation is measured. Confirmation depends on a "
                  "likelihood, and the likelihood depends on how the object was found."),
            ("p", "Take a world with ten ravens. If the hypothesis `H` is true, all ten are black and "
                  "the non-black things number 900, none of them a raven. If `H` is false, exactly one "
                  "raven is not black, so there are 901 non-black things and one of them is a raven. "
                  "Give `H` a prior of `1/2`."),
            ("p", "First case: pick a non-black thing at random and find it is not a raven. Under `H` that "
                  "had probability 1. Under not-`H` it had probability `900/901`, since one of the 901 "
                  "would have been a raven. The Bayes factor is `1 / (900/901) = 901/900`."),
            ("p", "Second case: pick a raven at random and find it is black. Under `H` that had probability "
                  "1. Under not-`H` it had probability `9/10`. The factor is `10/9`."),
            ("thm", ("Both confirm, unequally",
                     "A white shoe sampled from the non-black things has Bayes factor `901/900`; a black "
                     "raven sampled from the ravens has `10/9`. The first is above 1, so the shoe "
                     "confirms, and it is barely above 1, so it hardly matters.")),
            ("p", "The asymmetry is therefore not a property of shoes. It comes from the size of the "
                  "sampled class: there are very many non-black things for a counterexample to hide "
                  "among, and few ravens. Choose a different class to sample from, such as a thousand "
                  "ravens, and the numbers move. The lab's limit is the world it describes. The result "
                  "does not say that colour of shoes is evidence about birds in general, and a reader who "
                  "samples shoes without a reason to link them to ravens has changed the likelihoods. "
                  "Good pressed this further: the background can change the sign. If the hypothesis being "
                  "true would mean there are few ravens and its being false would mean there are a great "
                  "many, then a black raven drawn from all the birds is more probable when the hypothesis "
                  "is false, and its factor falls below 1. Rewrite both rows of the lab for a draw from all "
                  "the birds, with a black raven rarer under the hypothesis than under its rival, and the "
                  "tile that said confirms will say disconfirms."),
        ],
        "lab": ("choicekit", {
            "mode": "update",
            "preset": "nonblack",
            "presets": [
                {"id": "nonblack",
                 "label": "Sample a non-black thing: a non-raven",
                 "hyps": ["all ravens are black", "one raven is not"],
                 "prior": ["1/2", "1/2"],
                 "outcomes": ["raven", "non-raven"],
                 "lik": [["0", "1"], ["1/901", "900/901"]],
                 "data": "non-raven",
                 "payoffs": None,
                 "expect": {"upBF": "901/900", "upPost": "901/1801"}},
                {"id": "ravens",
                 "label": "Sample a raven: a black one",
                 "hyps": ["all ravens are black", "one raven is not"],
                 "prior": ["1/2", "1/2"],
                 "outcomes": ["black", "non-black"],
                 "lik": [["1", "0"], ["9/10", "1/10"]],
                 "data": "black",
                 "payoffs": None,
                 "expect": {"upBF": "10/9", "upPost": "10/19"}},
            ],
        }),
        "steps_title": "Answering a confirmation paradox",
        "steps_intro": "Four steps that apply to any case where evidence looks irrelevant yet follows from two plain principles.",
        "steps": [
            ("Write the argument as conditions",
             "State each principle used and check each on its own. Here that is Nicod's condition and "
             "the equivalence condition."),
            ("Check the equivalence by table",
             "Build the truth table for the two forms and confirm that they agree on every row."),
            ("Fix how the evidence was gathered",
             "Say what was sampled from what. The likelihoods depend on it, and they are not "
             "defined without it."),
            ("Compute the factor for each",
             "Take the ratio of the two likelihoods for each case. Compare them as numbers, and do not "
             "ask only whether they exceed 1."),
        ],
        "worked": {
            "title": "A white shoe and a black raven",
            "intro": ["Ten ravens; under the hypothesis all black, under its negation one is not. Prior `1/2`."],
            "lines": [
                "white shoe (sampled from non-black things):",
                "  P(non-raven | H) = 900/900 = 1",
                "  P(non-raven | not-H) = 900/901",
                "  Bayes factor = 901/900",
                "black raven (sampled from ravens):",
                "  P(black | H) = 1; P(black | not-H) = 9/10",
                "  Bayes factor = 10/9",
            ],
            "after": [
                "Both factors exceed 1, so both confirm. The shoe's exceeds 1 by `1/900` and the "
                "raven's by `1/9`, a hundred times as much. The paradox dissolves because "
                "&ldquo;confirms&rdquo; was being heard as &ldquo;confirms appreciably&rdquo;."
            ],
        },
        "quiz_title": "Shoes, ravens and degrees",
        "quiz": [
            {"q": "What does the equivalence condition contribute to the paradox?",
             "a": ["It says a white shoe is a raven",
                   "It carries confirmation from the contrapositive to the original hypothesis",
                   "It says that non-black things are never ravens",
                   "It makes every observation confirm every hypothesis"],
             "c": 1,
             "why": "A non-black non-raven instances the contrapositive; the condition then transfers "
                    "that confirmation to the original. The others claim more than the condition says."},
            {"q": "In the lab a white shoe has Bayes factor 901/900 and a black raven 10/9. What follows?",
             "a": ["Both confirm it, the raven far more strongly",
                   "The shoe disconfirms the hypothesis",
                   "Neither confirms it",
                   "The shoe confirms it more strongly than the raven"],
             "c": 0,
             "why": "Both factors exceed 1, so both confirm; 10/9 is much further above 1 than 901/900. "
                    "The factor for the shoe is smaller, not larger."},
            {"q": "The paradox is resolved here by changing which assumption?",
             "a": ["That Nicod's condition holds",
                   "That the equivalence condition holds",
                   "That confirmation is all-or-nothing",
                   "That ravens are black"],
             "c": 2,
             "why": "Both conditions are kept. What goes is the assumption that a confirming instance must "
                    "confirm substantially, which measuring by the Bayes factor replaces."},
        ],
        "mistakes": [
            ("Treating confirmation as all-or-nothing",
             "A white shoe confirms with factor `901/900` and a black raven with `10/9`. Both exceed 1, "
             "and the first exceeds it by a hundredth as much. Asking only whether evidence confirms "
             "loses the one number that tells the cases apart."),
            ("Thinking the paradox shows that indoor ornithology works",
             "The `901/900` is the result of sampling from the non-black things at random. A shoe "
             "picked for its colour, with no route to a raven, is not that sample, and the lab does "
             "not describe it."),
            ("Rejecting the equivalence condition to escape",
             "The truth table shows the two forms agree on every row. A condition that gives different "
             "verdicts to hypotheses that agree on every row is not a theory of evidence for the "
             "hypothesis, but of its wording."),
        ],
        "standard": (
            "Finish when you can compute the factor for each way of sampling.",
            "Given a hypothesis and a description of how an object was drawn, you should be able to "
            "compute the Bayes factor for the object found, compare it with the factor for a different "
            "draw, and say why the two differ."
        ),
        "note": (
            "The numbers 10, 900 and 901 are the world the lesson stipulates. A world with more ravens "
            "or fewer non-black things changes both factors, and the lab will show it when you edit "
            "the likelihoods."
        ),
    },
]
