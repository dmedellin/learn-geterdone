"""Paradoxes and Their Exits, lessons 6-9: probability and belief."""

LESSONS = [
    # ---------------------------------------------------------------- 06
    {
        "slug": "the-two-envelopes",
        "title": "The Two Envelopes",
        "module": "Probability",
        "one_line": "The argument that you should always switch needs the other envelope to be double with probability one half at every amount, and a bounded prior cannot supply that.",
        "summary": (
            "Two envelopes hold an amount and its double. You open one and find 8, reason "
            "that the other holds 4 or 16 with equal chance, and conclude that switching is "
            "worth 10. The same reasoning works whatever you find, so it says to switch "
            "without looking. The lab computes the worth of switching from a stated prior "
            "and finds the step that fails: the chance of &ldquo;double&rdquo; cannot be "
            "one half at every amount."
        ),
        "key": [
            "other envelope: x/2 or 2x",
            "switch = (1/2)·(x/2) + (1/2)·2x = 5x/4",
            "needs P(other is 2x | x) = 1/2 for every x",
            "a bounded prior breaks it at the top",
            "exit: deny a premise (the 1/2)",
        ],
        "key_label": "Where the always-switch argument turns",
        "concepts_intro": (
            "Three ideas locate the fault. The first is the argument in its strongest form, "
            "the second is the quantity it quietly assumes, and the third is what a finite "
            "prior does to that quantity."
        ),
        "concepts": [
            ("Once the amount is fixed, the argument is valid",
             "From the premise that the other envelope holds half your amount or double it, "
             "each with probability one half, the expected value of switching is "
             "five quarters of your amount, which is more than keeping it. With the "
             "amount in hand the arithmetic has no slip, and if there is a fault it is "
             "in a premise. Run without opening, the same words hide a slip, and the "
             "lesson says where."),
            ("The premise is about what you saw",
             "Before you open anything, your envelope is the smaller one with probability "
             "one half. After you see 8, the right probability is the chance that 8 is the "
             "smaller amount of a pair, given how the pairs were chosen. That is a "
             "posterior, and it depends on a prior over the pairs."),
            ("A bounded prior cannot give one half everywhere",
             "If the pairs come from a finite list, there is a largest amount. Seeing it "
             "tells you your envelope is the larger one, so the chance that the other is "
             "double is zero there. The premise cannot hold at every amount, and the "
             "argument needed it to."),
        ],
        "read_title": "Switching, given what you saw",
        "read_intro": "The argument first, then the quantity it assumes, then the lab.",
        "body": [
            ("p", "Two sealed envelopes hold money. One holds some amount and the other "
                  "holds exactly double. You are given one at random and may keep it or "
                  "swap. You open yours and find 8. The other, you reason, holds 4 if "
                  "yours is the larger and 16 if yours is the smaller, and the two cases "
                  "are equally likely because you were handed yours by chance."),
            ("math", [
                "other = 4, chance 1/2",
                "other = 16, chance 1/2",
                "worth of switching = (1/2)·4 + (1/2)·16 = 10",
            ]),
            ("p", "Ten is more than eight, so switch. Nothing in this depends on the "
                  "number 8. If you had found `x`, the other would be worth `(1/2)·(x/2) + "
                  "(1/2)·2x`, which is `5x/4`, more than `x`. Since you would switch "
                  "whatever you found, you may as well switch without opening. And "
                  "having switched, the same argument about the new envelope says to "
                  "switch back. A rule that recommends swapping forever, between "
                  "envelopes that were symmetric to begin with, is what makes this a "
                  "paradox."),
            ("def", ("The two envelopes",
                     "The <strong>two envelopes paradox</strong> is the argument that "
                     "you should switch whatever amount you find, from the premise that "
                     "the other envelope holds half or double with equal probability, "
                     "and the unacceptable conclusion that two symmetric envelopes are "
                     "each better than the other.")),
            ("p", "Which exit is best depends on how the argument is run. Run without "
                  "opening the envelope, it equivocates. The letter `x` stands for the "
                  "amount in your envelope in both cases, but if the pair is some amount "
                  "and its double, your envelope holds the smaller amount in one case "
                  "and the larger in the other, so the `x` in `x/2` and the `x` in `2x` "
                  "are not the same number, and averaging them as if they were is a step "
                  "that only looks valid. That is exit two, and it is the standard "
                  "diagnosis of the closed version: written with the pair as `y` and "
                  "`2y`, switching is worth `(1/2)·2y + (1/2)·y` whichever envelope you "
                  "hold, and so is keeping. Run after opening, with the 8 in hand, the "
                  "step is sound: 4 and 16 are two definite amounts and their average "
                  "at equal weights is 10. Accepting the conclusion would mean swapping "
                  "forever, which no one defends. So in the open version look at the "
                  "premises. One is that the envelopes hold an amount and its double, "
                  "which is the setup. Another is that you should pick the act of "
                  "greater expected value, which Decision and Rationality defended. The "
                  "third is that the chance of &ldquo;the other is double&rdquo; is one "
                  "half, and that one is not part of the setup."),
            ("p", "Why was it thought to be? Before you open anything, the chance that "
                  "yours is the smaller envelope is one half, because it was handed "
                  "over by chance. The argument carries that one half across the act of "
                  "opening. But what you learn on opening is the amount, and the amount "
                  "is evidence about which kind of envelope you hold. A small amount "
                  "suggests the smaller one, and a large one the larger. The chance "
                  "after the opening is a posterior, as in “Updating on Evidence”, and "
                  "a posterior depends on a prior over the pairs."),
            ("p", "Now suppose the prior is bounded, so that the pairs come from a "
                  "finite list. Then there is a largest amount that can appear, and "
                  "when you see it you know your envelope is the larger. The other "
                  "holds half, with probability one, and switching is worth half of "
                  "what you have. The same holds in mirror image at the smallest "
                  "amount, where you know the other is double. So the chance of "
                  "&ldquo;double&rdquo; is zero at one end of the list and one at the "
                  "other, and in between it is whatever the prior makes it. It cannot "
                  "be one half at every amount."),
            ("p", "The lab takes the chance as the prior over two hypotheses, &ldquo;mine is "
                  "the larger, so the other holds 4&rdquo; and &ldquo;mine is the smaller, so "
                  "the other holds 16&rdquo;, and takes the payoffs of keeping and "
                  "switching under each. In the first preset the prior is one half each, "
                  "which is the premise of the argument for this amount. The lab reports "
                  "that switching is worth 10 and keeping 8, as the argument said. In the "
                  "second preset the prior is 1 on the first hypothesis: 8 is the "
                  "largest amount there is. Keeping is worth 8 and switching only 4. In "
                  "the third preset the prior is 1 on the second, and switching is "
                  "worth 16."),
            ("example", ("Why the interior is not the top",
                         "At 8, with one half on each hypothesis, the lab gives switching "
                         "10 against 8. If the largest amount in the list is 8, the "
                         "prior on the second hypothesis there is 0, and the lab gives "
                         "switching 4 against 8. The same arithmetic, fed a different "
                         "prior, reverses the advice. No single act is best at every "
                         "amount, and that is why the always-switch rule cannot be "
                         "right.")),
            ("p", "The reply has a price, and it should be stated. Giving up the "
                  "premise means giving up a very natural thought, that when you "
                  "know nothing about the amounts the two cases are equally likely. "
                  "A bounded prior does not say that thought is always wrong. It says "
                  "the thought cannot be right at every amount, and it leaves the "
                  "reader free to hold it at the amounts in the middle of the list, "
                  "as the first preset does."),
            ("p", "The lab's limit is the limit of the reply. Every prior here is over "
                  "finitely many hypotheses, and the payoffs are the amounts, chosen by "
                  "you. Priors over unboundedly many amounts, some of which give the "
                  "switching argument an infinite expected value, belong to a harder "
                  "form of the puzzle that is named in the course home and not built. "
                  "What the lab computes is that a prior that can be written down, "
                  "with a largest amount, cannot make the argument work at every amount."),
        ],
        "lab": ("choicekit", {
            "mode": "update",
            "preset": "interior",
            "presets": [
                {"id": "interior",
                 "label": "Found 8 in the middle of the list, one half each",
                 "hyps": ["mine is larger (other is 4)", "mine is smaller (other is 16)"],
                 "prior": ["1/2", "1/2"],
                 "outcomes": ["seen-8"],
                 "lik": [["1"], ["1"]],
                 "data": ["seen-8"],
                 "payoffs": {"switch": ["4", "16"], "keep": ["8", "8"]},
                 "expect": {"upPost": "1/2", "upBest": "switch: 10"}},
                {"id": "top",
                 "label": "Found 8, the largest amount in the list",
                 "hyps": ["mine is larger (other is 4)", "mine is smaller (other is 16)"],
                 "prior": ["1", "0"],
                 "outcomes": ["seen-8"],
                 "lik": [["1"], ["1"]],
                 "data": ["seen-8"],
                 "payoffs": {"switch": ["4", "16"], "keep": ["8", "8"]},
                 "expect": {"upPost": "1", "upBest": "keep: 8"}},
                {"id": "bottom",
                 "label": "Found 8, the smallest amount in the list",
                 "hyps": ["mine is larger (other is 4)", "mine is smaller (other is 16)"],
                 "prior": ["0", "1"],
                 "outcomes": ["seen-8"],
                 "lik": [["1"], ["1"]],
                 "data": ["seen-8"],
                 "payoffs": {"switch": ["4", "16"], "keep": ["8", "8"]},
                 "expect": {"upPost": "0", "upBest": "switch: 16"}},
            ],
            "panel_title": "Switching, given a prior over the two cases",
            "panel_intro": "Each preset is the same sealed envelope holding 8, with the same payoffs: switching gives 4 if yours is the larger and 16 if it is the smaller, keeping gives 8 either way. Only the prior differs. Read the best act and its value in each, then move the prior in the first preset to 3/4 and 1/4 and find the prior at which keeping and switching tie.",
        }),
        "steps_title": "Testing the always-switch argument",
        "steps_intro": "Five steps, for this puzzle and for any argument that a symmetric choice is better on one side.",
        "steps": [
            ("Write the two cases and their payoffs",
             "For the amount you hold, say what the other envelope would contain in each "
             "case, and what keeping and switching pay in each."),
            ("State the probability the argument uses",
             "Write down the chance it gives to each case. The always-switch argument "
             "gives one half to each, for every amount."),
            ("Ask where it comes from",
             "Before opening, one half is right. After opening, the chance is a "
             "posterior, so ask which prior over the pairs would give it."),
            ("Try the ends of the list",
             "Take the largest and the smallest amount the prior allows. There the "
             "chance of &ldquo;double&rdquo; is 0 and 1, and the advice reverses."),
            ("Name the exit and its price",
             "The premise that the chance is one half at every amount is the one to "
             "deny. The price is a natural thought, that ignorance of the amounts gives "
             "equal chances, which holds only in the interior."),
        ],
        "worked": {
            "title": "Switching after finding 8",
            "intro": [
                "Take the envelope you hold to contain 8, and compare the two priors on "
                "what the other contains. The first is the argument's own, the second "
                "puts 8 at the top of the list."
            ],
            "lines": [
                "other is 4 if mine is the larger, 16 if the smaller",
                "prior one half each:",
                "  switch = (1/2)·4 + (1/2)·16 = 10",
                "  keep = 8, so switch wins by 2",
                "8 is the largest amount: prior 1 on the larger",
                "  switch = 1·4 + 0·16 = 4",
                "  keep = 8, so keep wins by 4",
                "the premise fails: one half is not right at every amount",
            ],
            "after": [
                "At 8 in the interior, switching is worth 10 against 8. At the largest "
                "amount, the prior on &ldquo;the other is 16&rdquo; is 0 and switching "
                "is worth 4. The argument used one half at both."
            ],
        },
        "quiz_title": "Worth and premise",
        "quiz": [
            {"q": "You hold 8, and the chance that the other holds 16 rather than 4 is "
                  "one half. What is switching worth?",
             "a": ["8, since the envelopes are symmetric",
                   "12, since 8 plus half of 8 is 12",
                   "10, since half of 4 plus half of 16 is 10",
                   "20, since 4 and 16 are the two possible amounts"],
             "c": 2,
             "why": "The worth is the probability-weighted sum, one half of 4 plus one "
                    "half of 16, which is 10. Eight is the worth of keeping, and "
                    "symmetry of the setup does not make switching equal to it once "
                    "you hold 8 and give the cases equal chance. Twelve adds half of 8 "
                    "to 8, which is not a payoff of either case. Twenty is the sum of "
                    "the two payoffs, without the weights."},
            {"q": "You have opened your envelope and found 8. Which premise of the "
                  "always-switch argument does the standard reply deny?",
             "a": ["That the envelopes hold an amount and its double",
                   "That the other is double with chance one half at every amount you might find",
                   "That you should take the act of greater expected value",
                   "That half of 4 plus half of 16 is 10"],
             "c": 1,
             "why": "A bounded prior cannot make the chance of “double” one half at the "
                    "top and bottom of the list, so that premise goes. The setup, the "
                    "decision rule and the arithmetic are not at fault: the first is "
                    "stipulated, the second is what makes the question about worth, and "
                    "the third is a sum that is right."},
            {"q": "The prior says 8 is the largest amount that can appear, and you find "
                  "8. What does the lab give as the best act?",
             "a": ["Switch, worth 16",
                   "Either, since the envelopes are symmetric",
                   "Switch, since the argument works at every amount",
                   "Keep, worth 8, because switching is worth only 4"],
             "c": 3,
             "why": "At the top you hold the larger envelope with probability one, so "
                    "the other holds 4 and switching is worth 4, less than 8. Sixteen "
                    "is switching's worth at the bottom of the list. Symmetry is a "
                    "fact about the setup before you look, and the amount you see "
                    "breaks it. That the argument works at every amount is the claim "
                    "this preset refutes."},
            {"q": "Before opening, your envelope is the smaller one with chance one half. "
                  "Why may that chance change when you see 8?",
             "a": ["Seeing the amount is evidence about whether it is the smaller one of a pair",
                   "Opening an envelope changes what is in the other one",
                   "A chance of one half cannot be carried across any act of looking",
                   "The amount 8 is too small to be the smaller one"],
             "c": 0,
             "why": "The amount is evidence, and the chance after seeing it is the "
                    "posterior given the prior over pairs. Opening does not alter the "
                    "envelopes. The third choice overstates: the chance can stay one "
                    "half if the prior makes 8 equally likely to be either, as in the "
                    "first preset. The fourth fixes a rule the setup does not give, "
                    "since 8 may be the smaller amount of the pair 8 and 16."},
        ],
        "mistakes": [
            ("Thinking that symmetry shows switching is always better",
             "The setup is symmetric before you look, so neither envelope is better "
             "in advance. After you see an amount, what matters is the chance that "
             "yours is the smaller one given that amount, and the prior sets it. "
             "At the largest amount the lab gives that chance as 0 and switching is "
             "worth 4 against 8. A rule that recommends switching at every amount "
             "must give the same chance at every amount, and a bounded prior cannot."),
            ("Carrying the pre-opening chance across the opening",
             "One half is the right chance for &ldquo;mine is the smaller&rdquo; before "
             "anything is seen. It is not the right chance after the amount is seen, "
             "unless the prior happens to make it so. Treat the amount as evidence, "
             "as in the lessons on updating, and recompute."),
            ("Reading the lab's best act as advice about real envelopes",
             "The payoffs are the amounts and the prior is a number you typed. The lab "
             "computes what follows from them. It does not say what prior a real "
             "organiser of envelopes used, and the best act changes when that does."),
        ],
        "standard": ("Finish when you can compute the worth of switching from a prior and locate the step that fails.",
                     "Given the amount in your envelope and a prior over the two cases, "
                     "you should be able to compute the expected value of keeping and of "
                     "switching, state the chance the always-switch argument assumes, "
                     "show with a bounded prior where that chance fails, and name the "
                     "exit and what it costs."),
        "note": "Priors that range over unboundedly many amounts can make the expected value of both envelopes infinite, and the puzzle then returns in a harder form; this course treats the bounded prior only. The next lesson also turns on what the evidence is, in a case where the dispute is over how to state the likelihood.",
    },
    # ---------------------------------------------------------------- 07
    {
        "slug": "sleeping-beauty",
        "title": "Sleeping Beauty",
        "module": "Probability",
        "one_line": "The halfer and the thirder compute the same Bayes' rule from two different likelihoods for “I am awake”, and the disagreement is about which likelihood is right.",
        "summary": (
            "Beauty is put to sleep on Sunday and a fair coin is tossed. On heads she is "
            "woken once, on tails twice, with memory of the first waking erased. Woken, she "
            "is asked how likely heads is. The halfer says one half, the thirder one third. "
            "Each is a correct update from a stated likelihood, and what the lab shows is "
            "that they differ in the likelihood and nowhere else."
        ),
        "key": [
            "heads: wake Monday.  tails: Monday, Tuesday",
            "posterior ∝ prior × likelihood",
            "halfer: P(awake | H) = P(awake | T) = 1",
            "thirder: P(this waking | H) = 1/2",
            "same rule, two likelihoods",
        ],
        "key_label": "Two answers, one rule",
        "concepts_intro": (
            "The puzzle is not about arithmetic. Three ideas show what it is about."
        ),
        "concepts": [
            ("The prior is not in dispute",
             "On Sunday the coin is fair, so the credence in heads is one half. Everyone "
             "agrees. The question is whether being woken is evidence that should "
             "move it."),
            ("The evidence is stated by a likelihood",
             "Bayes' rule needs the probability of the evidence under each hypothesis. "
             "&ldquo;I am awake&rdquo; can be modelled as certain on both outcomes of "
             "the coin, or as a particular waking whose probability differs between "
             "them. Those are the two models, and the rule is the same for both."),
            ("The disagreement is about what the evidence is",
             "The halfer treats being awake as something she knew in advance would "
             "happen. The thirder treats it as locating her at one of the possible "
             "wakings, which tails produces twice as often. Both are positions about a "
             "self-locating fact, and no arithmetic chooses between them."),
        ],
        "read_title": "One rule and two likelihoods",
        "read_intro": "The setup, the two answers, and the lab that shows what they share.",
        "body": [
            ("p", "On Sunday evening Beauty is told the plan, and she is put to sleep. A "
                  "fair coin is tossed. If it lands heads she is woken on Monday and the "
                  "experiment ends. If it lands tails she is woken on Monday, put back "
                  "to sleep with a drug that erases the memory of the waking, and woken "
                  "again on Tuesday. Each time she is woken she is asked: how likely "
                  "is it that the coin landed heads? She cannot tell Monday's waking "
                  "from Tuesday's, and she knows all this in advance."),
            ("p", "The <strong>halfer</strong> answers one half. She knew on Sunday that "
                  "she would be woken, and being woken tells her nothing she did not "
                  "know, so her credence in heads should be what it was. The "
                  "<strong>thirder</strong> answers one third. Over many repetitions of the "
                  "experiment a third of her wakings follow heads, and since she cannot "
                  "tell which waking this is, one third is the credence that matches "
                  "what her wakings are like."),
            ("p", "Both answers can be written as an update by Bayes' rule, as in "
                  "“Updating on Evidence”. There are two hypotheses, heads and "
                  "tails, each with prior one half. What differs is the likelihood of the "
                  "evidence. The halfer says the evidence is &ldquo;I am awake&rdquo;, "
                  "which has probability 1 if the coin is heads and probability 1 if it "
                  "is tails, since she is woken either way."),
            ("math", [
                "P(awake | H) = 1",
                "P(awake | T) = 1",
                "Bayes factor = 1/1 = 1",
                "P(H | awake) = 1/2",
            ]),
            ("p", "The thirder says the evidence is the fact that <em>this</em> waking is "
                  "occurring. Consider a day on which she might be woken. Under heads "
                  "only one of the two days, Monday, has a waking, so the chance that this "
                  "day is a waking day is one half. Under tails both days have one, so "
                  "it is 1. The likelihoods are one half and 1."),
            ("math", [
                "P(this waking | H) = 1/2",
                "P(this waking | T) = 1",
                "Bayes factor = (1/2)/1 = 1/2",
                "P(H | this waking) = 1/3",
            ]),
            ("p", "The lab shows the two computations. In the first preset, the halfer's, "
                  "the Bayes factor is 1 and the posterior for heads stays at one half. "
                  "In the second, the thirder's, the Bayes factor is one half, the "
                  "evidence disconfirms heads, and the posterior is one third. The rule "
                  "that produced both is the same, and so is the prior. Only the "
                  "likelihood of the word &ldquo;awake&rdquo; was changed."),
            ("example", ("Where the two models part",
                         "Ask what each says when Beauty learns that it is Monday. "
                         "The thirder starts from one third for heads and the likelihood "
                         "of Monday is 1 under heads and one half under tails, which "
                         "brings her to one half. The halfer starts from one half with "
                         "the same likelihoods and goes to two thirds. The third preset "
                         "is the thirder's, and editing its prior to one half and one "
                         "half gives the halfer's. A fair coin that has not yet been "
                         "tossed, in the version where it is tossed on Monday night, "
                         "moves to two thirds on the news that it is Monday, and that is "
                         "what the halfer has to defend.")),
            ("p", "Each position can be put at its strongest. The halfer has a clean "
                  "principle behind her: evidence is something you did not already "
                  "know, and Beauty knew she would be woken. Her cost is the case just "
                  "given, where a fair coin she has not seen tossed moves to two thirds "
                  "on the news of a weekday. The thirder has a clean principle too: "
                  "credences should be right on average over the occasions on which "
                  "they are held. Her cost is a credence of one third in a coin she "
                  "knows is fair, reached by evidence that is not about the coin in "
                  "the ordinary sense."),
            ("p", "So the exit is not the usual one. Set out as this course sets out a "
                  "paradox, there are two arguments, each valid, each from the Sunday "
                  "prior and a likelihood, to credences that cannot both be held; the "
                  "exit is to deny a premise of one of them, and the only premise that "
                  "differs is the likelihood. Neither side denies a premise of "
                  "Bayes' rule or faults a step of it. The choice is of a likelihood "
                  "model, and each model implies the whole of its answer. This is why "
                  "the question cannot be settled by checking the sum, and why the "
                  "lesson does not announce a winner. Whether a self-locating fact, "
                  "&ldquo;this is a waking&rdquo;, counts as evidence about the coin is "
                  "the premise the two answers divide on."),
            ("p", "The limit of the lab is that it computes from a likelihood and does not "
                  "decide which to put in. A bet does not settle it either unless it says "
                  "what is scored. If a stake is paid for each waking, tails pays twice "
                  "as often as heads and betting on tails is the better bet whichever "
                  "model is held. If one stake is paid for the experiment, the bet is "
                  "even. That the best bet depends on the scoring, and not on the "
                  "model alone, is a further fact about the puzzle and not a way "
                  "round it."),
        ],
        "lab": ("choicekit", {
            "mode": "update",
            "preset": "halfer",
            "presets": [
                {"id": "halfer",
                 "label": "Halfer: being awake is certain on either outcome",
                 "hyps": ["heads", "tails"],
                 "prior": ["1/2", "1/2"],
                 "outcomes": ["awake", "asleep"],
                 "lik": [["1", "0"], ["1", "0"]],
                 "data": ["awake"],
                 "payoffs": None,
                 "expect": {"upPost": "1/2", "upBF": "1"}},
                {"id": "thirder",
                 "label": "Thirder: this waking is half as likely under heads",
                 "hyps": ["heads", "tails"],
                 "prior": ["1/2", "1/2"],
                 "outcomes": ["awake", "asleep"],
                 "lik": [["1/2", "1/2"], ["1", "0"]],
                 "data": ["awake"],
                 "payoffs": None,
                 "expect": {"upPost": "1/3", "upBF": "1/2"}},
                {"id": "told-monday",
                 "label": "Thirder, then told that it is Monday",
                 "hyps": ["heads", "tails"],
                 "prior": ["1/3", "2/3"],
                 "outcomes": ["monday", "tuesday"],
                 "lik": [["1", "0"], ["1/2", "1/2"]],
                 "data": ["monday"],
                 "payoffs": None,
                 "expect": {"upPost": "1/2", "upBF": "2"}},
                {"id": "halfer-told-monday",
                 "label": "Halfer, then told that it is Monday",
                 "hyps": ["heads", "tails"],
                 "prior": ["1/2", "1/2"],
                 "outcomes": ["monday", "tuesday"],
                 "lik": [["1", "0"], ["1/2", "1/2"]],
                 "data": ["monday"],
                 "payoffs": None,
                 "expect": {"upPost": "2/3", "upBF": "2"}},
            ],
            "panel_title": "The same rule with two likelihoods",
            "panel_intro": "The hypotheses are heads and tails, and the tiles report heads. In the first two presets the prior is the Sunday one, one half each, and only the likelihood of the evidence changes. In the last two Beauty is also told that it is Monday, which has likelihood 1 under heads and one half under tails; the prior is the thirder's one third in the first and the halfer's one half in the second.",
        }),
        "steps_title": "Comparing two answers to a puzzle of evidence",
        "steps_intro": "Four steps, for Sleeping Beauty and for any puzzle where the answers differ and the rule is the same.",
        "steps": [
            ("Fix the prior",
             "State the hypotheses and the credence in each before the evidence. Here "
             "heads and tails at one half each, which both sides accept."),
            ("Write each side's evidence as a likelihood",
             "For each hypothesis, give the probability of the evidence as that side "
             "describes it. The two sides will differ here, if anywhere."),
            ("Compute both posteriors by the same rule",
             "Run the update for each. If both are correct computations, the "
             "disagreement is already located in the likelihoods."),
            ("State what the disagreement is about",
             "Say which likelihood each side defends and what it costs. A test case "
             "that separates them, such as being told it is Monday, helps."),
        ],
        "worked": {
            "title": "Heads, under two likelihoods",
            "intro": [
                "The prior is one half for heads. The question is what the evidence "
                "&ldquo;I am awake&rdquo; does to it under each model."
            ],
            "lines": [
                "prior: heads 1/2, tails 1/2",
                "halfer: P(awake | heads) = 1, P(awake | tails) = 1",
                "  Bayes factor = 1/1 = 1",
                "  posterior for heads = 1/2",
                "thirder: P(this waking | heads) = 1/2, | tails = 1",
                "  Bayes factor = (1/2)/1 = 1/2",
                "  posterior for heads = 1/3",
                "same rule, same prior, different likelihood",
            ],
            "after": [
                "The halfer's Bayes factor is 1 and her posterior one half. The thirder's "
                "Bayes factor is one half and her posterior one third. Neither made a "
                "mistake in the arithmetic."
            ],
        },
        "quiz_title": "Likelihoods and answers",
        "quiz": [
            {"q": "Under the halfer's model, what are the Bayes factor for heads and the "
                  "posterior?",
             "a": ["Bayes factor 1/2 and posterior 1/3",
                   "Bayes factor 1 and posterior 1/2",
                   "Bayes factor 2 and posterior 2/3",
                   "Bayes factor 1 and posterior 1/3"],
             "c": 1,
             "why": "Being awake has probability 1 under both outcomes, so the factor "
                    "is 1 and the posterior stays at the prior, one half. The first "
                    "choice is the thirder's model. Factor 2 and two thirds is neither "
                    "model's answer to this question. The last mixes a factor of 1 "
                    "with a posterior that a factor of 1 cannot produce."},
            {"q": "What do the halfer and the thirder disagree about?",
             "a": ["Whether the coin is fair",
                   "How to apply Bayes' rule when there are two hypotheses",
                   "Whether Beauty remembers the experiment from Sunday",
                   "The probability of the evidence “I am awake” under heads, relative to tails"],
             "c": 3,
             "why": "Both give the coin a prior of one half, so fairness is not in "
                    "dispute, and both apply the same rule. Both grant that she "
                    "knows the plan from Sunday, and what she lacks is a memory of "
                    "the earlier waking. What differs is the likelihood of the "
                    "evidence under each outcome."},
            {"q": "The thirder is told it is Monday and starts from one third for heads. "
                  "Monday has likelihood 1 under heads and one half under tails. What "
                  "is her posterior?",
             "a": ["1/3",
                   "2/3",
                   "1/2",
                   "1"],
             "c": 2,
             "why": "The products are one third times 1 and two thirds times one half, "
                    "both one third, so the posterior is one half. It does not stay at "
                    "one third because the evidence has a Bayes factor of 2. It does "
                    "not reach two thirds, which is the halfer's answer from a prior "
                    "of one half. It does not reach 1, since tails also has a Monday."},
            {"q": "A reader says the coin is fair, so the answer must be one half. What "
                  "does the thirder reply?",
             "a": ["The prior is one half and the evidence of this waking moves it, since tails makes wakings twice as common",
                   "The coin is not fair after the first waking",
                   "Fairness is irrelevant to credence",
                   "Bayes' rule does not apply to a coin"],
             "c": 0,
             "why": "Fairness fixes the prior and the thirder keeps it. The disagreement "
                    "is over whether the waking is evidence. She does not claim the coin "
                    "changes, so the second is wrong, nor that fairness is irrelevant, "
                    "since the prior comes from it, nor that the rule fails for coins."},
        ],
        "mistakes": [
            ("Thinking the coin is fair, so the answer must be one half",
             "Fairness fixes the prior, and nobody disputes it. The question is what "
             "being woken does to the prior, and that depends on the likelihood of the "
             "evidence under each outcome. With a likelihood of 1 for both, the "
             "posterior is one half. With one half under heads and 1 under tails, "
             "it is one third, for the same fair coin."),
            ("Taking the two answers to be an error of arithmetic on one side",
             "Each answer is a correct update from its likelihood, and the lab "
             "shows both. The dispute is over the likelihood, which is a statement "
             "of what the evidence is, and checking the sum cannot settle it."),
            ("Expecting a bet to settle it",
             "A bet is scored in some way, per waking or per experiment, and the best "
             "bet follows from the scoring. Per waking, tails wins twice as often. "
             "Per experiment, the bet is even. Which scoring matches Beauty's "
             "credence is part of the question."),
        ],
        "standard": ("Finish when you can compute both answers by one rule and say what the disagreement is about.",
                     "Given the setup, you should be able to write the likelihood each "
                     "side uses, compute the Bayes factor and posterior for heads under "
                     "each, run a test case such as being told it is Monday, and state "
                     "that the dispute is over the likelihood of the evidence."),
        "note": "This lesson makes no claim about which answer is right. Real work on the puzzle weighs the two costs named above, and some reject both models in favour of a third. The next lesson returns to a puzzle where the answer is settled once the model is stated, and the interest is in how a small change in the model moves it.",
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "monty-hall",
        "title": "Monty Hall",
        "module": "Probability",
        "one_line": "After the host opens a door the chance is not one half each, because what the host does depends on where the car is, and a different host gives a different answer.",
        "summary": (
            "A car is behind one of three doors. You choose door 1, and a host who knows "
            "where it is opens door 3 to show a goat. The lab updates on the host's act, "
            "not on the bare fact that door 3 is empty, and finds that door 2 now holds "
            "the car with probability two thirds. A host who opens a door at random gives "
            "one half, which is why the host's rule has to be part of the problem."
        ),
        "key": [
            "car at 1, 2 or 3: 1/3 each; you pick door 1",
            "host opens 3: 1/2 if car at 1, 1 if at 2",
            "P(car at 2 | host opens 3) = 2/3",
            "random host: 1/2 each",
            "exit: accept the conclusion",
        ],
        "key_label": "The host's rule is the evidence",
        "concepts_intro": (
            "Three ideas explain why the obvious answer is wrong and when it is right."
        ),
        "concepts": [
            ("The evidence is what the host did",
             "The fact that door 3 is empty is not all you learned. You learned that "
             "the host, following his rule, opened door 3. The likelihood of that "
             "act under each hypothesis is what updating needs."),
            ("A forced move is stronger evidence than a free one",
             "If the car is behind door 2, the host must open door 3. If it is behind "
             "door 1, he could have opened door 2 or door 3 and chose 3 with probability "
             "one half. So his act is twice as probable if the car is behind 2."),
            ("Change the rule and the answer changes",
             "A host who opens one of the other two doors at random, and happened to show "
             "a goat, gives no extra weight to door 2. The same sight, door 3 open and "
             "empty, is then worth one half each. The model decides, and the lesson "
             "states it."),
        ],
        "read_title": "Updating on the host's act",
        "read_intro": "The game, the common answer, the update, and the host who is not informed.",
        "body": [
            ("p", "A game show has three doors. Behind one is a car and behind the other "
                  "two are goats. You choose a door, say door 1. The host, who knows "
                  "where the car is, opens one of the other doors to show a goat, and he "
                  "always does so; if both of the others hide goats he picks at random. "
                  "He opens door 3. You may stay with door 1 or switch to door 2. "
                  "Which gives the better chance of the car?"),
            ("p", "Most people say it makes no difference. Two doors are closed, the car "
                  "is behind one of them, and so each has chance one half. The reasoning "
                  "treats the news as &ldquo;door 3 is empty&rdquo; and spreads the "
                  "chance evenly over what remains. That is the premise to look at, "
                  "because the news was not that, but that the host opened door 3."),
            ("p", "Let the hypotheses be the three places for the car, each with prior "
                  "one third. The evidence is that the host opened door 3. Its "
                  "likelihood under each hypothesis follows from his rule. If the car "
                  "is behind door 1, he may open door 2 or door 3, and opens 3 with "
                  "probability one half. If the car is behind door 2, he cannot open "
                  "door 2 and cannot open door 1, which you chose, so he must open "
                  "door 3, with probability 1. If the car is behind door 3, he cannot "
                  "open it, and the probability is 0."),
            ("math", [
                "likelihoods of opening 3: 1/2, 1, 0",
                "prior times likelihood: 1/6, 1/3, 0",
                "total: 1/2",
                "posterior: 1/3, 2/3, 0",
            ]),
            ("p", "So the car is behind door 2 with probability two thirds, and staying "
                  "wins with probability one third. The lab shows the table and, with the "
                  "payoffs of staying and switching, names switching as the better act, "
                  "worth two thirds. The reason is the one in the second concept. Door 1 "
                  "gave the host a free choice and door 2 gave him none, so seeing him "
                  "open door 3 is twice as probable if the car is behind door 2."),
            ("example", ("Counting it another way",
                         "Door 1 holds the car with chance one third, and nothing the host "
                         "does can change that, because he never opens your door and "
                         "never opens the car. The other two doors together hold two "
                         "thirds. The host has shown that one of them is empty, and the "
                         "whole of the two thirds falls on the other. That is the same "
                         "answer, reached without the table.")),
            ("p", "Set out as this course sets out a paradox, the argument is short, "
                  "and every premise of it is part of the setup."),
            ("ol", [
                "The car was placed at random, so each door holds it with probability one third.",
                "The host knows where the car is, never opens your door or the car's door, and chooses at random when he has a choice.",
                "Under that rule his opening door 3 had probability one half if the car is behind door 1, 1 if it is behind door 2, and 0 if it is behind door 3.",
                "So, by Bayes' rule, the car is behind door 2 with probability two thirds, and switching doubles your chance.",
            ]),
            ("p", "Every step is valid, the premises are the rules of the game, and "
                  "the conclusion felt wrong. The exit is the third: accept it. The "
                  "conclusion was unacceptable only because the argument for one half was "
                  "familiar, and that argument is not the paradox but a mistake, whose "
                  "false premise, that all you learned is that door 3 is empty, the "
                  "lab exposes. The price of exit three is small. One loses the habit of "
                  "treating the sight of an empty door as the whole of the evidence, and "
                  "gains the habit of asking how the sight came about."),
            ("p", "The second preset shows how much the rule matters. Suppose the host does "
                  "not know where the car is. He opens one of the two other doors at "
                  "random and, as it happens, it shows a goat. Now the likelihood of "
                  "opening door 3 and showing a goat is one half if the car is behind "
                  "door 1, one half if it is behind door 2, and 0 if it is behind door 3, "
                  "since that would have shown the car. The posterior is one half "
                  "for each of the first two doors, and switching is worth no more than "
                  "staying. The lab's best-act tile names both."),
            ("p", "The third preset has four doors. You choose door 1, and the host, who "
                  "knows, opens door 4. Door 1 gave him a choice among three doors, so "
                  "the likelihood is one third; doors 2 and 3 gave him a choice "
                  "between two, so it is one half; door 4 gave him none. The posterior is "
                  "one quarter for door 1 and three eighths for each of door 2 and "
                  "door 3. Staying still wins one time in four, and each of the two other "
                  "doors is better."),
            ("p", "The lab's limit is that it computes from the rule you type. It does "
                  "not know which rule the host followed, and nothing in the sight of "
                  "an open door reveals it. A reader who is not told the rule has to "
                  "assume one, and the standard statement of the puzzle gives it for "
                  "that reason. A problem without the rule has two correct answers, "
                  "one for each rule, and the dispute about which is meant is a dispute "
                  "about the model."),
        ],
        "lab": ("choicekit", {
            "mode": "update",
            "preset": "monty",
            "presets": [
                {"id": "monty",
                 "label": "Host knows the car and opens a goat door: he opens 3",
                 "hyps": ["car at 1", "car at 2", "car at 3"],
                 "prior": ["1/3", "1/3", "1/3"],
                 "outcomes": ["opens-2", "opens-3"],
                 "lik": [["1/2", "1/2"], ["0", "1"], ["1", "0"]],
                 "data": ["opens-3"],
                 "payoffs": {"stay": ["1", "0", "0"], "switch": ["0", "1", "0"]},
                 "expect": {"upPost": "1/3", "upBest": "switch: 2/3"}},
                {"id": "random-host",
                 "label": "Host opens a door at random and shows a goat: he opens 3",
                 "hyps": ["car at 1", "car at 2", "car at 3"],
                 "prior": ["1/3", "1/3", "1/3"],
                 "outcomes": ["opens-3-goat", "opens-2-goat", "shows-car"],
                 "lik": [["1/2", "1/2", "0"], ["1/2", "0", "1/2"], ["0", "1/2", "1/2"]],
                 "data": ["opens-3-goat"],
                 "payoffs": {"stay": ["1", "0", "0"], "switch": ["0", "1", "0"]},
                 "expect": {"upPost": "1/2", "upBest": "stay, switch: 1/2"}},
                {"id": "four-doors",
                 "label": "Four doors, host knows the car and opens 4",
                 "hyps": ["car at 1", "car at 2", "car at 3", "car at 4"],
                 "prior": ["1/4", "1/4", "1/4", "1/4"],
                 "outcomes": ["opens-2", "opens-3", "opens-4"],
                 "lik": [["1/3", "1/3", "1/3"], ["0", "1/2", "1/2"], ["1/2", "0", "1/2"], ["1/2", "1/2", "0"]],
                 "data": ["opens-4"],
                 "payoffs": {"stay": ["1", "0", "0", "0"], "switch-2": ["0", "1", "0", "0"], "switch-3": ["0", "0", "1", "0"]},
                 "expect": {"upPost": "1/4", "upBest": "switch-2, switch-3: 3/8"}},
            ],
            "panel_title": "The car's place, given what the host did",
            "panel_intro": "You chose door 1. The table lists the likelihood of the host's act under each place for the car, then the posterior. The tiles report door 1, the door you hold. The best-act tile compares staying with switching, using the payoffs 1 for the car and 0 for a goat. Then edit the likelihood rows of the first preset toward the second's and watch the best act change.",
        }),
        "steps_title": "Updating on what an informed agent did",
        "steps_intro": "Five steps, for Monty Hall and for any puzzle where someone who knows something acts in front of you.",
        "steps": [
            ("Fix the hypotheses and the prior",
             "List the places the prize could be, with equal priors if the setup says "
             "the placing was at random."),
            ("State the agent's rule",
             "Write what the host does under each hypothesis, including what he is "
             "forbidden to do. The rule is part of the problem."),
            ("Find the likelihood of the act that occurred",
             "For each hypothesis, give the probability that the host did what you "
             "saw. A forced act has probability 1 and a free one is divided among the "
             "choices he had."),
            ("Update and compare the acts",
             "Multiply prior by likelihood, normalise, and compute the chance of "
             "winning by staying and by switching."),
            ("Try a different rule, then name the exit",
             "Change the host to one who acts at random and see whether the answer "
             "moves. If it does, the rule was doing the work. With the rule fixed, the "
             "exit is the third: the two thirds is accepted, and what is given up is "
             "the habit of counting doors."),
        ],
        "worked": {
            "title": "The car's place after the host opens door 3",
            "intro": [
                "You hold door 1. The host knows the car, never opens your door or the "
                "car's door, and chooses at random when he has a choice."
            ],
            "lines": [
                "prior: 1/3 for each door",
                "car at 1: host opens 2 or 3, so P(opens 3) = 1/2",
                "car at 2: host must open 3, so P(opens 3) = 1",
                "car at 3: host cannot open 3, so P(opens 3) = 0",
                "products: 1/6, 1/3, 0 with total 1/2",
                "posterior: 1/3, 2/3, 0",
                "so P(car at 2 | host opens 3) = 2/3",
                "random host instead: 1/2, 1/2, 0 and posterior 1/2 each",
            ],
            "after": [
                "With an informed host, switching wins with probability two thirds. "
                "With a host who opened at random and showed a goat, the same sight "
                "gives one half."
            ],
        },
        "quiz_title": "The host and the doors",
        "quiz": [
            {"q": "You hold door 1. An informed host opens door 3 to show a goat. What is "
                  "the probability that the car is behind door 2?",
             "a": ["1/3",
                   "1/2",
                   "1",
                   "2/3"],
             "c": 3,
             "why": "The likelihoods of opening 3 are one half, 1 and 0, so the "
                    "posterior is one third, two thirds and 0. One third is door 1, the "
                    "door you hold. One half is the answer that treats the news as only "
                    "“door 3 is empty”. And 1 would need door 1 to be ruled out, which "
                    "nothing the host did does."},
            {"q": "The host does not know where the car is, opens a door at random, and "
                  "shows a goat at door 3. Why is the chance of the car at door 2 now "
                  "one half?",
             "a": ["Opening 3 and showing a goat is equally probable whether the car is at door 1 or door 2",
                   "Two doors remain, so each has one half whatever the rule",
                   "A random host always reveals the car",
                   "A random host is more likely to open door 3 when the car is behind door 2"],
             "c": 0,
             "why": "Each of those two hypotheses gives the act and the goat a "
                    "probability of one half, so the prior of equal weights is "
                    "unchanged. The second reasons from the count of doors, which "
                    "also gives one half here by chance and gives the wrong answer "
                    "with an informed host. A random host reveals the car sometimes, "
                    "not always. And a random host's choice of door does not depend on "
                    "where the car is at all; it is the informed host whose choice does, "
                    "which is why his act is evidence and the random host's is not."},
            {"q": "Why is the informed host's opening door 3 evidence in favour of "
                  "door 2?",
             "a": ["Because the host wants you to switch",
                   "Because the host always opens the door furthest from the car",
                   "Because the act of opening 3 was twice as probable if the car is behind door 2 as behind door 1",
                   "Because door 3 is now known to be empty, and an empty door's chance always passes to the other unopened door"],
             "c": 2,
             "why": "Behind door 2 the host's act was forced, probability 1, and "
                    "behind door 1 it had probability one half, so the Bayes factor "
                    "of door 2 against door 1 is 2. Wanting you to switch is not in "
                    "the rule. The furthest-door rule is not what the host follows. "
                    "The last gives the right number for the wrong reason: with a "
                    "random host door 3 is just as empty and its third is shared "
                    "between doors 1 and 2, so it is the host's rule, not the empty "
                    "door, that sends the whole of it to door 2."},
            {"q": "Four doors, you hold door 1, and the informed host opens door 4. What "
                  "is the chance that the car is behind door 2?",
             "a": ["1/4",
                   "1/3",
                   "1/2",
                   "3/8"],
             "c": 3,
             "why": "The likelihoods of opening 4 are one third, one half, one half and "
                    "0, so the posterior is one quarter, three eighths, three eighths "
                    "and 0. One quarter is door 1. One third would spread the chance "
                    "evenly over three doors, which ignores the host's rule. One half "
                    "would ignore door 3."},
        ],
        "mistakes": [
            ("Thinking that two doors remain, so each is one half",
             "The count of doors would give one half only if the host's act were "
             "equally probable under every place for the car. It is not: it was "
             "forced if the car is behind door 2 and free if it is behind door 1. "
             "The lab's table shows the likelihoods one half, 1 and 0, and the "
             "posterior one third and two thirds. Count the host's choices, not the "
             "doors."),
            ("Treating the sight of an empty door as the whole of the evidence",
             "What you learned is that the host, following a rule, opened it. The same "
             "sight is worth one half each with a host who opens at random and happens "
             "to show a goat. Always ask what the agent would have done under each "
             "hypothesis."),
            ("Taking the answer to hold without the host's rule",
             "The two thirds depends on a host who knows the car and never shows it. "
             "The lab computes from the rule you type. A story that omits the rule "
             "has no single answer, and saying so is correct."),
        ],
        "standard": ("Finish when you can compute the posterior from the host's rule and show it changes with the rule.",
                     "Given a host's rule, you should be able to write the likelihood of "
                     "his act under each place for the prize, compute the posterior by "
                     "Bayes' rule, name the better act, show how the answer changes "
                     "for a host who acts at random or when there are more doors, and "
                     "say which exit the two-thirds answer takes."),
        "note": "The Monty Hall answer is a case of the third exit: the conclusion is accepted, and the work is to see why it was resisted. The last lesson takes up a paradox of a different kind, in which nothing is computed from chance and a sentence can be true and still cannot be believed.",
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "moores-paradox-and-what-cannot-be-believed",
        "title": "Moore's Paradox and What Cannot Be Believed",
        "module": "Belief",
        "one_line": "A sentence of the form p and I do not know that p can be true, and the same sentence preceded by “I know that” is true at no world of a reflexive frame.",
        "summary": (
            "&ldquo;It is raining but I do not know it&rdquo; sounds absurd to say, yet it "
            "could be true. In a possible-worlds model the lab finds a world where it is "
            "true. Prefix the box, so that it says the speaker knows it, and the lab finds "
            "no world of the frame where that holds. A sentence can be true and still "
            "be one that no one in a world like that could know."
        ),
        "key": [
            "Moore: p ∧ ¬□p, read as p but I do not know p",
            "it can be true: satisfiable at a world",
            "□(p ∧ ¬□p): true at no reflexive world",
            "reflexive: every world sees itself",
            "true is not the same as knowable",
        ],
        "key_label": "A true sentence that cannot be known",
        "concepts_intro": (
            "Three ideas separate what is absurd to say from what is false."
        ),
        "concepts": [
            ("Moore's sentence is satisfiable",
             "The sentence says that `p` is true and the speaker does not know it. "
             "Nothing forbids that: many truths are not known by anyone. There is a "
             "world, in the lab a model with two worlds, where the sentence is true. "
             "So it is not a contradiction."),
            ("Adding the box changes the sentence",
             "The box says that the speaker knows what follows. `□(p ∧ ¬□p)` says "
             "that the speaker knows both that `p` and that they do not know it. The "
             "added claim is stronger, and it is the one that fails."),
            ("A reflexive frame makes knowledge factive",
             "In a reflexive frame every world sees itself, so whatever is known is "
             "true there. If the speaker knew `¬□p` it would be true, so they would not "
             "know `p`, while also knowing `p`. No world of such a frame survives."),
        ],
        "read_title": "True, and not knowable",
        "read_intro": "The sentence, the model where it is true, the model where it cannot be known, and what that costs.",
        "body": [
            ("p", "G. E. Moore noticed that some sentences are odd to assert although "
                  "nothing about their content is odd. &ldquo;It is raining, but I do not "
                  "know that it is&rdquo; is one. Each half may be true, and the whole "
                  "may be true, as when it is raining in a room where no one has "
                  "looked. Yet no one can sincerely say it. The puzzle is why a "
                  "sentence that could be true cannot be sincerely stated, and set out "
                  "as this course sets out a paradox it is three premises that cannot "
                  "all hold."),
            ("ol", [
                "Moore's sentence, “it is raining but I do not know that it is”, can be true.",
                "Whatever can be true can be known, and so sincerely asserted, by the one it is about.",
                "No one can sincerely assert Moore's sentence.",
                "So someone can sincerely assert it, and no one can.",
            ]),
            ("p", "Write `p` for &ldquo;it is raining&rdquo; and read the box `□` as "
                  "&ldquo;the speaker knows that&rdquo;, the reading the lab names and "
                  "“Leibniz's Law and the Masked Man” used before. "
                  "Moore's sentence is `p ∧ ¬□p`. Its stated form is the sentence "
                  "itself, and what would have to hold of the speaker for the assertion "
                  "to be sincere, that they know what they assert, is the sentence with "
                  "the box in front:"),
            ("math", [
                "p ∧ ¬□p",
                "□(p ∧ ¬□p)",
            ]),
            ("p", "The first is true at a world where it rains and the speaker does not "
                  "know it. The lab models that with two worlds. At the first, `w1`, "
                  "it rains. The speaker at `w1` sees `w1` and `w2`, and at `w2` it does "
                  "not rain, so the speaker does not know it is raining. The lab "
                  "evaluates `p ∧ ¬□p` at `w1` and reports True. It also lists the worlds "
                  "where the sentence holds, and the list is `w1`, since at `w2` it is not "
                  "raining. So the sentence is satisfiable, and Moore's paradox is "
                  "not that it is contradictory."),
            ("def", ("Moore's paradox",
                     "<strong>Moore's paradox</strong> is that a sentence of the form "
                     "&ldquo;<em>p</em>, but I do not know that <em>p</em>&rdquo; can be "
                     "true, and yet cannot be known by the person it is about, so "
                     "that it cannot be sincerely asserted, nor believed by a believer "
                     "who knows their own mind.")),
            ("p", "The second sentence is a different matter. Suppose a world where "
                  "`□(p ∧ ¬□p)` is true. The box distributes over the conjunction, so "
                  "at that world the speaker knows `p` and knows `¬□p`. Now use the "
                  "frame. If every world sees itself, whatever the speaker knows is "
                  "true there: that is the axiom `□p → p` of “Frames, Axioms and What "
                  "Necessity Obeys”, which a reflexive frame validates and the lab's "
                  "axioms tile lists as T. So `¬□p` is true at the world: the speaker "
                  "does not know `p`. But the speaker knows `p`. The two cannot both "
                  "hold, so there is no such world."),
            ("p", "The lab checks this. In the second preset the frame is reflexive: "
                  "`w1` sees `w1` and `w2`, and `w2` sees itself. The formula "
                  "`□(p ∧ ¬□p)` is evaluated at every world and the lab's list of worlds "
                  "where it holds is empty. The argument above shows that the same "
                  "would hold in any reflexive frame, whatever the number of worlds. The "
                  "lab shows it for this one, and the argument generalises it."),
            ("example", ("What the dead end hides",
                         "A world that sees no world satisfies every boxed sentence "
                         "vacuously, because there is nothing for the box to range over. "
                         "A reflexive frame has no dead ends, which is part of why it "
                         "gives no world for the boxed Moore sentence. The third "
                         "preset drops reflexivity, and its list of worlds includes a "
                         "dead end for exactly this reason.")),
            ("p", "So Moore's sentence is a truth that no one in a reflexive frame can "
                  "know. That is exit one, and the premise denied is the second, "
                  "that whatever can be true can be known. The premise is natural: it "
                  "treats the limits of knowledge as the limits of fact. The price of "
                  "denying it is that some truths are unknowable by their own subject, "
                  "not through ignorance of the world but through the form of the "
                  "sentence. Nothing is wrong with the logic. The sentence says "
                  "something about the speaker's knowledge that knowing it would "
                  "falsify."),
            ("p", "The third preset shows what the argument needed. It has three "
                  "worlds, `w1` sees `w2` and `w2` sees `w3`, and no world sees itself. "
                  "At `w1` the speaker knows that `p` and that they do not know it, "
                  "because at the one world `w1` sees, `w2`, it rains and the speaker "
                  "there sees a dry world. The lab reports the boxed sentence True at "
                  "`w1`. Without reflexivity, what is known need not be true, and this is "
                  "a model of mistaken belief. Belief does not have to be reflexive, "
                  "which is why the paradox is put in terms of knowledge here."),
            ("p", "A believer who can look into their own beliefs recovers the result "
                  "without reflexivity. The fourth preset is a frame in which each "
                  "world sees only worlds that see the same worlds, as an agent "
                  "does who knows their own mind, and the lab again finds no world "
                  "that satisfies the boxed sentence. What the lab shows in each case is "
                  "a property of the frame and not a finding about people. It says what "
                  "a speaker whose frame has the property cannot coherently hold."),
        ],
        "lab": ("argkit", {
            "mode": "kripke",
            "at": 1,
            "reading": "epistemic",
            "preset": "moore-true",
            "presets": [
                {"id": "moore-true",
                 "label": "Raining at w1 only; the speaker sees w1 and w2",
                 "n": 2, "access": [[1, 1], [1, 2], [2, 2]],
                 "valuation": {"p": [1]},
                 "formula": "p & ~[]p",
                 "expect": {"krValue": "True at w1", "krWorlds": "w1"}},
                {"id": "moore-known",
                 "label": "The same frame, the Moore sentence known",
                 "n": 2, "access": [[1, 1], [1, 2], [2, 2]],
                 "valuation": {"p": [1]},
                 "formula": "[](p & ~[]p)",
                 "expect": {"krValue": "False at w1", "krWorlds": "none"}},
                {"id": "not-reflexive",
                 "label": "No world sees itself: w1 sees w2, w2 sees w3",
                 "n": 3, "access": [[1, 2], [2, 3]],
                 "valuation": {"p": [1, 2]},
                 "formula": "[](p & ~[]p)",
                 "expect": {"krValue": "True at w1", "krWorlds": "w1, w3"}},
                {"id": "introspective",
                 "label": "The speaker knows their own mind: w1 sees w2, w2 sees w2",
                 "n": 2, "access": [[1, 2], [2, 2]],
                 "valuation": {"p": [1, 2]},
                 "formula": "[](p & ~[]p)",
                 "expect": {"krValue": "False at w1", "krWorlds": "none"}},
            ],
            "panel_title": "A sentence that is true, and the same sentence known",
            "panel_intro": "The box is read as it is known that, and the sentence is evaluated at w1. The first model has three arrows, each world seeing itself and w1 also seeing w2; it is raining at w1 only. Read the first preset, then the second, which prefixes the box. Then the third and the fourth, which change the frame: the third has no world that sees itself, and the fourth has one world seeing another which sees only itself.",
        }),
        "steps_title": "Testing whether a true sentence can be known",
        "steps_intro": "Five steps, for Moore's sentence and for any sentence that says something about the speaker's own knowledge.",
        "steps": [
            ("Write the sentence and its known form",
             "Give the sentence, then put the box in front of it. For Moore's sentence "
             "these are `p ∧ ¬□p` and `□(p ∧ ¬□p)`."),
            ("Find a world where the sentence is true",
             "Build a small model. If one exists the sentence is satisfiable, and the "
             "paradox is not a contradiction."),
            ("Evaluate the known form at every world",
             "Read the list of worlds where it holds. In a reflexive frame the list is "
             "empty."),
            ("Check the frame",
             "Ask what the frame property did. Without reflexivity, or the "
             "introspective condition of the fourth preset, the known form can hold."),
            ("Name the exit and its price",
             "Deny that whatever can be true can be known. The price is that some truths "
             "are unknowable by the person they are about, because of what they say."),
        ],
        "worked": {
            "title": "Moore's sentence at w1, and with the box",
            "intro": [
                "The model has two worlds. The speaker at w1 sees w1 and w2, and at w2 "
                "sees w2. It is raining at w1 only."
            ],
            "lines": [
                "at w1: p is true",
                "w1 sees w2, where p is false, so box p is false at w1",
                "so not box p is true, and p and not box p is true at w1",
                "at w2: p is false, so the Moore sentence is false",
                "box of the Moore sentence at w1 needs it true at w1 and w2",
                "it is false at w2, so box of it is false at w1",
                "any world: box Moore gives box p and box not box p",
                "reflexive: box not box p gives not box p, against box p",
            ],
            "after": [
                "At w1 the sentence is true; prefix the box and no world of the frame "
                "satisfies it. A reflexive frame cannot have one at all."
            ],
        },
        "quiz_title": "True and known",
        "quiz": [
            {"q": "Which is the correct description of Moore's sentence `p ∧ ¬□p`?",
             "a": ["It is false at every world, so it is a contradiction",
                   "It is true at a world where p holds and the speaker does not know p",
                   "It is true at every world of every frame",
                   "It is true only at a world where the speaker knows p"],
             "c": 1,
             "why": "The lab finds it true at w1, where p holds and the speaker sees a "
                    "world where it does not. So it is not a contradiction. It is not "
                    "true at every world, since at w2 the first conjunct fails. And "
                    "it cannot be true where the speaker knows p, because that "
                    "falsifies the second conjunct."},
            {"q": "In a reflexive frame, what does the lab give for the worlds where "
                  "`□(p ∧ ¬□p)` holds?",
             "a": ["All of them",
                   "Only the worlds where p is true",
                   "Only the worlds that see a world where p is false",
                   "None of them"],
             "c": 3,
             "why": "At such a world the speaker would know p and know they do not, and "
                    "reflexivity makes the second true, against the first. So no world "
                    "satisfies it. The worlds where p is true are not enough, since "
                    "the boxed sentence needs the Moore sentence at every world seen, "
                    "and a world that sees a world where p is false fails at once, "
                    "because the first conjunct fails there: in the lab's second preset "
                    "w1 is such a world and the value at w1 is False."},
            {"q": "The third preset has no reflexive world and the lab finds the boxed "
                  "sentence True at w1. What does this show?",
             "a": ["That the boxed sentence is satisfiable in every frame",
                   "That knowledge can be false in that model, so reflexivity is what the argument used",
                   "That the boxed sentence is satisfiable in a reflexive frame after all",
                   "That the lab is in error"],
             "c": 1,
             "why": "At w1 what is “known” is not true at w1 itself, so the "
                    "model is not one of knowledge, and the argument that used "
                    "reflexivity does not apply. The boxed sentence is not satisfiable "
                    "in every frame, since the second preset is a frame where it holds "
                    "at no world. A third preset says nothing about the reflexive case, "
                    "which the argument settles for every reflexive frame. And the lab "
                    "evaluates the formula correctly, which is what the argument "
                    "predicts for a frame without reflexivity."},
            {"q": "Which premise does the usual reply to Moore's paradox deny?",
             "a": ["That Moore's sentence can be true",
                   "That the box distributes over a conjunction",
                   "That whatever can be true can be known by the one it is about",
                   "That a reflexive frame is a frame in which every world sees itself"],
             "c": 2,
             "why": "The sentence is true at w1, so the first is not denied. Distribution "
                    "is a validity of the logic, and the last choice is only the "
                    "definition. What is denied is that truth guarantees knowability "
                    "for the subject: Moore's sentence is true and cannot be known by "
                    "the speaker it is about."},
        ],
        "mistakes": [
            ("Treating Moore's sentence as a contradiction",
             "A contradiction is false at every world. This sentence is true at w1, "
             "where it rains and the speaker does not know it. What fails is "
             "the sentence with the box in front, which a reflexive frame does not "
             "allow anywhere. The two are different sentences, and mixing them "
             "makes the paradox look like a contradiction."),
            ("Reading the failure of the boxed form as a failure of the sentence",
             "The sentence is true at w1 and the world is a possible one. What "
             "cannot happen is that the speaker there knows it. The odd thing is "
             "an assertion's claim to know, not the content."),
            ("Taking the result to depend on how many worlds are drawn",
             "The lab shows one frame, and the argument shows all reflexive "
             "frames: the distribution of the box and the truth of what is "
             "known. Adding worlds does not change that, and the third preset "
             "shows that taking away reflexivity does."),
        ],
        "standard": ("Finish when you can show a sentence is true at a world and its known form is true at none.",
                     "Given a sentence about the speaker's own knowledge, you should be "
                     "able to build a model where it holds, evaluate its boxed form at "
                     "every world, say what the frame property did, and name the "
                     "premise the best reply denies and what it costs."),
        "note": "This is the last paradox of the course, and it is a fit ending: nothing in the lab chose the exit. Each lesson set out an argument, a computation and the exits with their prices, and the choice among them, which the computation cannot make, is the philosophy that remains.",
    },
]
