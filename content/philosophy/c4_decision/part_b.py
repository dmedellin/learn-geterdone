"""Decision and Rationality, lessons 6-10: the paradoxes and puzzles of expected value."""

LESSONS = [
    # ---------------------------------------------------------------- 06
    {
        "slug": "the-allais-paradox-and-the-sure-thing-principle",
        "title": "The Allais Paradox and the Sure-Thing Principle",
        "module": "Risk",
        "one_line": "Two common choices test the same expression for opposite signs, so no set of utilities can make both.",
        "summary": (
            "Most people prefer a sure million to a gamble that might pay five, and "
            "also prefer a one-in-ten chance of five million to an eleven-in-a-hundred "
            "chance of one. Expected utility scores the gap in each pair by the same "
            "expression, so the two preferences together contradict it whatever "
            "numbers the utilities take."
        ),
        "key": [
            "A: 1M for sure",
            "B: 89% 1M, 10% 5M, 1% nothing",
            "C: 11% 1M, otherwise nothing",
            "D: 10% 5M, otherwise nothing",
            "EU(A) − EU(B) = EU(C) − EU(D)",
            "A and D together contradict EU",
        ],
        "key_label": "One number, tested twice",
        "concepts_intro": (
            "The paradox is short to state and easy to miss. It asks the same "
            "question twice, with the same answer hidden in a different place."
        ),
        "concepts": [
            ("Two choices, one common part",
             "In the first choice the two gambles share an 89% chance of a million. "
             "In the second they share an 89% chance of nothing. Take the shared "
             "part away and the same two remainders are left to compare."),
            ("The sure-thing principle",
             "If two acts give the same outcome in some states, those states "
             "should not affect which act you prefer. Expected utility obeys this "
             "automatically, because a shared term appears on both sides and cancels."),
            ("The pattern A and D",
             "Preferring the sure million and then preferring the one-in-ten shot "
             "at five million is the popular response. It lets the shared part "
             "change the verdict, and that is the violation."),
        ],
        "read_title": "Four gambles and a term that cancels",
        "read_intro": "First the choices, then the arithmetic that shows they cannot both be answered as most people answer them.",
        "body": [
            ("p", "Maurice Allais put two choices to people in 1953. In the first, "
                  "gamble A pays a million for certain, and gamble B pays five million "
                  "with probability 10%, a million with probability 89% and nothing "
                  "with probability 1%. In the second, gamble C pays a million with "
                  "probability 11% and nothing otherwise, and gamble D pays five "
                  "million with probability 10% and nothing otherwise. Most people "
                  "choose A over B, and D over C."),
            ("p", "Each choice looks sensible on its own. A gives up a little "
                  "expected money for certainty, which is just what a concave "
                  "utility was shown to allow in “Risk Aversion and the Value of "
                  "Information”, and B risks ending with nothing at all, which is a "
                  "poor price for a small improvement. In the second "
                  "choice nobody is certain of anything, so the bigger prize "
                  "for nearly the same chance is the natural pick."),
            ("p", "Lay the gambles out as a table of tickets, numbered 1 to 100. "
                  "Tickets 1 to 89 are the shared part, ticket 90 is the "
                  "single ticket that decides the 1% and tickets 91 to 100 decide "
                  "the 10%. Payoffs are in millions."),
            ("math", [
                "gamble    1 to 89    90    91 to 100",
                "A              1     1            1",
                "B              1     0            5",
                "C              0     1            1",
                "D              0     0            5",
            ]),
            ("p", "Read the first column. A and B agree on it, both paying 1, and "
                  "C and D agree on it too, both paying 0. The only difference "
                  "between the first choice and the second is what the shared "
                  "tickets pay. The last two columns are the same in both choices: "
                  "A and C pay 1 and 1, B and D pay 0 and 5."),
            ("def", ("The sure-thing principle",
                     "If two acts pay the same in some states, then which of them "
                     "you prefer should depend only on the states where they "
                     "differ. Changing what they both pay in the shared states "
                     "should leave the preference unchanged. The name is Leonard "
                     "Savage's, from 1954; the principle is older than the name.")),
            ("p", "Expected utility satisfies this by construction. Write the "
                  "utilities of nothing, a million and five million as `u(0)`, "
                  "`u(1M)` and `u(5M)`. The difference between A and B is "
                  "computed below, and so is the difference between C and D. The "
                  "89% term is common to A and B and cancels; the corresponding "
                  "term cancels between C and D."),
            ("math", [
                "EU(A) − EU(B) = 11/100·u(1M) − 10/100·u(5M) − 1/100·u(0)",
                "EU(C) − EU(D) = 11/100·u(1M) − 10/100·u(5M) − 1/100·u(0)",
            ]),
            ("thm", ("The same expression",
                     "For any utilities whatever, `EU(A) − EU(B)` and `EU(C) − EU(D)` "
                     "are equal. So preferring A to B makes the first positive, "
                     "preferring D to C makes the second negative, and one number "
                     "cannot be both.")),
            ("p", "The lab enters the utilities `u(0) = 0`, `u(1M) = 10` and "
                  "`u(5M) = 14` and scores each pair. In the first it prints "
                  "103/10 for B and 10 for A; in the second 7/5 for D and 11/10 for "
                  "C. Expected utility picks B and D here. Both gaps are 3/10 in "
                  "favour of the gamble. Change the utilities and the gaps move "
                  "together, always by the same amount."),
            ("p", "That is the whole result: the rule can prefer A and C, or it can "
                  "prefer B and D, but it cannot prefer A and D. Preferring A "
                  "to B needs `u(5M)` below `11/10·u(1M)` when `u(0)` is zero, and "
                  "preferring D to C needs it above. The popular pair asks for "
                  "both."),
            ("p", "What is said for the popular pair is not foolish. Certainty is a "
                  "state of mind as well as a payoff: a chooser who ends up with "
                  "nothing after turning down a sure million may feel a regret "
                  "that nothing in the second choice can produce. On this view "
                  "the shared 89% of tickets is not the same in the two choices, "
                  "because in the first it contributes certainty. A defender must "
                  "then say what the outcome is: if regret is part of it, the "
                  "payoff table should list it, and the choices are no longer "
                  "about the same payoffs."),
            ("p", "The reader has two ways out. One keeps the table as stated and "
                  "gives up the sure-thing principle, which means giving up "
                  "expected utility as the measure of these acts. The other keeps "
                  "the principle and revises one of the two choices. The lab "
                  "computes what each costs, not which to pay."),
        ],
        "lab": ("choicekit", {
            "mode": "decide", "rule": "eu",
            "preset": "allais-a",
            "presets": [
                {"id": "allais-a", "label": "the sure million against the gamble",
                 "acts": ["A", "B"], "states": ["tickets 1-89", "ticket 90", "tickets 91-100"],
                 "payoffs": [[10, 10, 10], [10, 0, 14]],
                 "probs": ["89/100", "1/100", "1/10"], "expect": {"deChoice": "B", "deValue": "103/10"}},
                {"id": "allais-b", "label": "eleven in a hundred against ten in a hundred",
                 "acts": ["C", "D"], "states": ["tickets 1-89", "ticket 90", "tickets 91-100"],
                 "payoffs": [[0, 10, 10], [0, 0, 14]],
                 "probs": ["89/100", "1/100", "1/10"], "expect": {"deChoice": "D", "deValue": "7/5"}},
                {"id": "all-four", "label": "all four gambles in one table",
                 "acts": ["A", "B", "C", "D"], "states": ["tickets 1-89", "ticket 90", "tickets 91-100"],
                 "payoffs": [[10, 10, 10], [10, 0, 14], [0, 10, 10], [0, 0, 14]],
                 "probs": ["89/100", "1/100", "1/10"], "expect": {"deChoice": "B", "deValue": "103/10"}},
            ],
            "panel_title": "Move the utilities and watch both gaps move together",
            "panel_intro": "The payoffs are utilities, with u(0) = 0, u(1M) = 10 and u(5M) = 14. Score the first pair, then the second, and compare each winning score with the other act's. Now change the 14 to 21/2 in both presets. Gamble A beats B in the first, and C beats D in the second: the preference flips in both places at once, which is the point. No value of the 14 produces A with D.",
        }),
        "steps_title": "Testing a pair of choices against expected utility",
        "steps_intro": "Four steps, and none needs a number for any utility.",
        "steps": [
            ("Tabulate on common tickets",
             "Give the gambles the same states, one column for what they "
             "share and one for each place they differ. Without common states "
             "the shared part is hidden."),
            ("Write each gap",
             "Write `EU` of the first act minus `EU` of the second as a sum over "
             "the states, with the probabilities and utilities left as symbols."),
            ("Cancel the shared columns",
             "In each pair, the states where the two acts pay the same give "
             "equal terms, which subtract to zero."),
            ("Compare what remains",
             "If the two remainders are the same expression, the two choices "
             "must go the same way under expected utility, and a pattern that "
             "splits them contradicts it."),
        ],
        "worked": {
            "title": "Both gaps, from one set of utilities",
            "intro": [
                "Take `u(0) = 0`, `u(1M) = 10` and `u(5M) = 14`, with the "
                "tickets split 89, 1 and 10 in a hundred."
            ],
            "lines": [
                "EU(A) = 10",
                "EU(B) = 89/100·10 + 1/100·0 + 10/100·14 = 103/10",
                "EU(A) - EU(B) = -3/10",
                "EU(C) = 89/100·0 + 1/100·10 + 10/100·10 = 11/10",
                "EU(D) = 89/100·0 + 1/100·0 + 10/100·14 = 7/5",
                "EU(C) - EU(D) = -3/10",
            ],
            "after": [
                "The two gaps print the same fraction. These utilities favour B and D; "
                "lower the five-million utility far enough and they favour A and C. "
                "Preferring A and D is choosing both signs of one number."
            ],
        },
        "quiz_title": "Same gap, opposite signs",
        "quiz": [
            {"q": "With u(0) = 0, u(1M) = 10 and u(5M) = 14, what is EU(A) − EU(B)?",
             "a": ["3/10", "1", "−3/10", "0"],
             "c": 2,
             "why": "EU(A) = 10 and EU(B) = 103/10, so the gap is −3/10. The "
                    "value 3/10 has the right size and the wrong sign: B is ahead. "
                    "A gap of 0 would mean a tie, and 1 is not the difference "
                    "of either pair of scores."},
            {"q": "Why can no choice of utilities make A over B and D over C both "
                  "come out of expected utility?",
             "a": ["Utilities must be proportional to the money",
                   "A is riskier than B",
                   "The probabilities 89% and 11% are too large for the rule to use",
                   "EU(A) − EU(B) and EU(C) − EU(D) are the same expression, so one "
                   "would have to be positive and negative at once"],
             "c": 3,
             "why": "The shared 89% term cancels in each pair and leaves the same "
                    "expression, so the signs must agree. Utilities need not be "
                    "proportional to money, and the argument holds for any. A is "
                    "the less risky of the two, but the argument does not use risk. "
                    "Expected utility handles any probabilities."},
            {"q": "What does the sure-thing principle say about the 89% of tickets "
                  "on which A and B pay the same?",
             "a": ["They should not affect which of A and B you prefer",
                   "They should make you choose the sure act",
                   "They should be paid out as a million in both choices",
                   "They show that A dominates B"],
             "c": 0,
             "why": "The principle says a state where the acts agree is irrelevant to "
                    "choosing between them. It does not favour sure acts. It does not "
                    "fix what the shared tickets pay. And A does not dominate B: B pays "
                    "5 on tickets 91 to 100 where A pays 1."},
            {"q": "Someone prefers B to A, using any utilities at all. What does expected "
                  "utility then require of the second choice?",
             "a": ["C over D", "D over C", "Indifference between C and D",
                   "Nothing, since the choices are independent"],
             "c": 1,
             "why": "B over A means EU(A) − EU(B) is negative, and EU(C) − EU(D) is the "
                    "same number, so D is ahead of C. C over D would need the "
                    "opposite sign. A tie needs a zero gap. And the choices are "
                    "not independent: the identity connects them."},
        ],
        "mistakes": [
            ("Thinking a sure thing always earns a premium under expected utility",
             "Under the rule a sure million is worth `u(1M)` and nothing more. With "
             "`u(0) = 0`, `u(1M) = 10` and `u(5M) = 14` the gamble B scores 103/10 "
             "against 10 for A, so the sure thing loses. It wins only if "
             "`u(5M)` is below 11 on this scale, and then it must also win "
             "the second choice for C over D. Certainty carries no bonus of its "
             "own; that is the thing the popular pattern adds."),
            ("Judging each choice alone",
             "Taken alone, A over B fits expected utility for some utilities, and so "
             "does D over C. The contradiction lives in the pair. Checking the "
             "choices one at a time will find nothing wrong, which is why the "
             "pattern persisted for so long."),
            ("Concluding that the people are simply irrational",
             "The argument shows the pair is inconsistent with the rule, not "
             "that anyone has made an error. A defender may say the rule leaves "
             "out something outcomes carry, such as regret. Whether to revise the "
             "choices or the rule is the open question."),
        ],
        "standard": ("Finish when you can show that a pair of choices breaks expected utility.",
                     "Given the four gambles, you should be able to tabulate them "
                     "on common tickets, write both gaps, show that they are the same "
                     "expression, and say what accepting the popular pattern costs."),
        "note": "The utilities are the same assumption as everywhere else on this course: a number somebody chose. The argument does not depend on them, which is why the paradox is stated for any utilities. The reasons people choose as they do are not computed here.",
    },
    # ---------------------------------------------------------------- 07
    {
        "slug": "ambiguity-and-the-ellsberg-urn",
        "title": "Ambiguity and the Ellsberg Urn",
        "module": "Risk",
        "one_line": "Preferring the known bet in both of two choices fits no single guess about the unknown proportion.",
        "summary": (
            "An urn holds 30 red balls and 60 that are black or yellow in an unknown "
            "mix. People prefer to bet on red rather than black, and to bet on black "
            "or yellow rather than red or yellow. Each choice needs a different "
            "estimate of the black share, so no one estimate supports both."
        ),
        "key": [
            "urn: 30 red, 60 black or yellow, mix unknown",
            "I: bet red, or bet black",
            "II: red or yellow, or black or yellow",
            "red in I needs p(black) < 1/3",
            "black or yellow in II needs p(black) > 1/3",
            "both at once fit no single p",
        ],
        "key_label": "Known odds against unknown odds",
        "concepts_intro": (
            "The puzzle does not ask whether you like risk. It asks whether you "
            "prefer to know the odds."
        ),
        "concepts": [
            ("Risk and ambiguity are different",
             "Risk is a gamble with known probabilities, like red here. Ambiguity "
             "is a gamble whose probabilities are not known, like black. The "
             "prizes are the same; what differs is how much you know."),
            ("A single guess settles every bet",
             "If you hold one credence `p` for the black share, each bet has a "
             "probability, and expected utility ranks all four bets from it. "
             "Choices that need two different values of `p` cannot come from one guess."),
            ("Worst-case rules can avoid the guess",
             "A rule that scores a bet by its worst case over the possible mixes "
             "needs no single `p`, and it reproduces the popular pattern. It "
             "pays for that by leaving expected utility."),
        ],
        "read_title": "The urn, the two bets, and the proportion that decides them",
        "read_intro": "First the setup, then the algebra that shows no proportion fits, then the one rule that does.",
        "body": [
            ("p", "Daniel Ellsberg described an urn of 90 balls in 1961. Thirty are "
                  "red. The other 60 are black or yellow, in a proportion nobody "
                  "has told you. One ball will be drawn. A bet pays 100 if its colour "
                  "comes up and nothing otherwise, so on a scale where winning is "
                  "worth 1 and losing 0, a bet is worth its probability."),
            ("p", "In the first decision you choose between a bet on red and a bet "
                  "on black. In the second you choose between a bet on red or "
                  "yellow and a bet on black or yellow. Most people choose red in "
                  "the first and black or yellow in the second. In both the pick "
                  "is the bet whose chance is known: red is exactly 30 in 90, and "
                  "black or yellow is exactly 60 in 90."),
            ("p", "Let `p` be your credence that a drawn ball is black. Yellow is "
                  "then `2/3 − p`, since red is 1/3 and the three add to 1. Score "
                  "each bet by its probability of winning."),
            ("math", [
                "bet                  chance of winning",
                "red                  1/3",
                "black                p",
                "red or yellow        1/3 + (2/3 − p) = 1 − p",
                "black or yellow      p + (2/3 − p) = 2/3",
            ]),
            ("p", "Red beats black exactly when `1/3 > p`. Black or yellow beats red "
                  "or yellow exactly when `2/3 > 1 − p`, which is `p > 1/3`. The "
                  "popular pair needs `p` below a third and above a third. No "
                  "credence satisfies both, and the lab shows it: the first preset "
                  "puts black at 2/9 and red wins; the second puts black at 4/9 and "
                  "black or yellow wins; no one table holds both."),
            ("thm", ("The pair has no credence",
                     "A strict preference for red over black needs `p < 1/3`. A strict "
                     "preference for black or yellow over red or yellow needs "
                     "`p > 1/3`. No single `p` does both, so the pattern is "
                     "inconsistent with a probability of black, and with "
                     "expected utility, whatever the utilities.")),
            ("p", "It is tempting to call this risk aversion. It is not. Both red "
                  "and black pay the same prize on the same terms, so any "
                  "utility for the prize multiplies both scores by the same "
                  "positive factor and leaves their order alone. A concave "
                  "utility cannot prefer red to black unless the probability of "
                  "red is higher, and nothing in the urn says it is. The "
                  "preference is for a known probability."),
            ("example", ("Black at a quarter",
                         "Suppose you believe `p = 1/4`. Then red at 1/3 beats black "
                         "at 1/4 in the first decision, and red or yellow at 3/4 "
                         "beats black or yellow at 2/3 in the second. A believer "
                         "in `p = 1/4` bets on red twice. The popular pattern "
                         "bets on red once and on black or yellow once.")),
            ("p", "One rule does reproduce the pattern. Let the possible mixes be "
                  "0, 30 or 60 black balls, and score each bet by its worst case "
                  "over the three. Red wins one third in every mix, so its worst "
                  "case is 1/3; black wins 0 in the first mix, so its worst case "
                  "is 0. Red or yellow can fall to 1/3, while black or yellow wins "
                  "2/3 in every mix. The worst-case rule picks red in the first "
                  "decision and black or yellow in the second."),
            ("p", "The third preset sets this up, with one state per mix and each "
                  "mix given probability 1/3. Under expected utility red and "
                  "black tie, and red or yellow ties black or yellow; averaging "
                  "over the mixes has erased the difference between known and "
                  "unknown. Switch the rule to maximin and black or yellow comes out "
                  "alone on top."),
            ("p", "Which view to hold is the question. A defender of the pattern "
                  "says ignorance is not the same as having a credence of one "
                  "third, and a chooser who has no basis for any `p` has no "
                  "reason to average. A critic answers that a credence is what "
                  "betting behaviour reveals, and that a chooser who will not "
                  "assign one to black has declined to treat the bets as bets. "
                  "The lab computes each rule and takes no side."),
        ],
        "lab": ("choicekit", {
            "mode": "decide", "rule": "eu",
            "preset": "ellsberg-1",
            "presets": [
                {"id": "ellsberg-1", "label": "red against black, black at 2/9",
                 "acts": ["red", "black"], "states": ["red", "black", "yellow"],
                 "payoffs": [[1, 0, 0], [0, 1, 0]],
                 "probs": ["1/3", "2/9", "4/9"], "expect": {"deChoice": "red", "deValue": "1/3"}},
                {"id": "ellsberg-2", "label": "red or yellow against black or yellow, black at 4/9",
                 "acts": ["red or yellow", "black or yellow"], "states": ["red", "black", "yellow"],
                 "payoffs": [[1, 0, 1], [0, 1, 1]],
                 "probs": ["1/3", "4/9", "2/9"], "expect": {"deChoice": "black or yellow", "deValue": "2/3"}},
                {"id": "maximin-view", "label": "one state per possible mix of black, each at 1/3",
                 "acts": ["red", "black", "red or yellow", "black or yellow"],
                 "states": ["0 black", "30 black", "60 black"],
                 "payoffs": [["1/3", "1/3", "1/3"], [0, "1/3", "2/3"],
                             [1, "2/3", "1/3"], ["2/3", "2/3", "2/3"]],
                 "probs": ["1/3", "1/3", "1/3"], "expect": {"deChoice": "red or yellow, black or yellow", "deValue": "2/3"}},
            ],
            "panel_title": "Try every credence for black",
            "panel_intro": "In the first preset change the probabilities to 1/3, 1/3, 1/3: red and black tie. Do the same in the second preset and its two bets tie as well; that is the credence in the middle. The third preset gives each mix of black balls the same probability and shows each bet's chance of winning in that mix. Switch the rule from expected utility to maximin and read the verdict again.",
        }),
        "steps_title": "Testing the Ellsberg pattern against any credence",
        "steps_intro": "Four steps, and the unknown stays a symbol until the last.",
        "steps": [
            ("Name the unknown",
             "Let `p` be the probability of black. Yellow is whatever is left "
             "after red at 1/3 and black, so `2/3 − p`."),
            ("Score the four bets",
             "Add the probabilities of every colour a bet wins on. A "
             "bet's expected utility is that sum, with winning scored 1."),
            ("State each choice as an inequality",
             "Red over black is `1/3 > p`. Black or yellow over red or yellow is "
             "`2/3 > 1 − p`. Solve each for `p`."),
            ("Look for a `p` that satisfies both",
             "If the solution sets do not overlap, the pair of choices "
             "fits no credence, and the pattern is not expected utility's."),
        ],
        "worked": {
            "title": "The two decisions as inequalities in p",
            "intro": [
                "Let `p` be the black share. Red is 1/3 and yellow is `2/3 − p`."
            ],
            "lines": [
                "I:  red wins 1/3, black wins p",
                "    red preferred when 1/3 > p",
                "II: red or yellow wins 1 - p",
                "    black or yellow wins 2/3",
                "    black or yellow preferred when 2/3 > 1 - p",
                "    that is p > 1/3",
                "both strict: p < 1/3 and p > 1/3",
            ],
            "after": [
                "At `p = 1/3` the bets tie in both decisions, so the credence "
                "in the middle is indifferent twice. The popular pattern is "
                "strict twice, in opposite directions, and for no credence is "
                "that possible."
            ],
        },
        "quiz_title": "A single credence against the pattern",
        "quiz": [
            {"q": "You believe the black share is 1/4. In the first decision, which "
                  "bet has the higher expected utility?",
             "a": ["Red, at 1/3 against 1/4", "Black, at 1/4 against 1/3",
                   "They tie", "Neither, since the share is unknown"],
             "c": 0,
             "why": "A credence of 1/4 gives black a probability of 1/4, and red is "
                    "1/3. They do not tie. The share is unknown, but a credence "
                    "turns it into a probability, which is all expected utility "
                    "needs."},
            {"q": "Which credences for black make a strict preference for red in the "
                  "first decision and a strict preference for black or yellow in the "
                  "second both hold?",
             "a": ["Only exactly 1/3",
                   "Every credence below 1/3",
                   "Every credence above 1/3",
                   "None"],
             "c": 3,
             "why": "The first needs a credence below 1/3 and the second above 1/3. "
                    "At exactly 1/3 both bets tie in both decisions, so neither "
                    "preference is strict there. Below 1/3 the second "
                    "choice reverses, and above 1/3 the first does."},
            {"q": "Why can concave utility not explain the pattern?",
             "a": ["Concave utility applies only to money",
                   "Red and black pay the same prize, so any utility scales both "
                   "scores equally and leaves their order alone",
                   "The Ellsberg bets are not gambles",
                   "Risk aversion always favours the unknown bet"],
             "c": 1,
             "why": "Both bets win the same prize or nothing, so a utility for the "
                    "prize multiplies each probability by the same factor. Concave "
                    "utility can apply to anything a chooser values. The bets are "
                    "gambles. And risk aversion does not favour the unknown bet; it "
                    "prefers certainty of the same expected value."},
            {"q": "Each mix of 0, 30 or 60 black balls is given probability 1/3. Under "
                  "expected utility, what does the lab say about red and black?",
             "a": ["Red is better, because it is known",
                   "Black is better, because its range is wider",
                   "They tie, both scoring 1/3",
                   "The lab refuses, because the mix is unknown"],
             "c": 2,
             "why": "Averaging over the three mixes gives red 1/3 and black "
                    "(0 + 1/3 + 2/3)/3 = 1/3. Averaging removes the distinction "
                    "between known and unknown, so neither is better. Nothing is "
                    "refused, because a probability for each mix is given."},
        ],
        "mistakes": [
            ("Treating ambiguity aversion as risk aversion",
             "Risk aversion is a fact about how prizes are valued. Red and black "
             "offer the same prize on the same terms, so a curve for the prize "
             "multiplies both scores by the same factor and cannot separate them; "
             "change the payoff 1 to 5 in the lab and the order is unchanged. "
             "What separates them is whether the probability is known."),
            ("Assuming ignorance means a credence of 1/3",
             "Giving each colour an equal share is a choice, not a consequence "
             "of ignorance. It turns the unknown into a known and then "
             "removes the preference. Someone who refuses to do so is not "
             "confused; the open question is whether they are consistent."),
            ("Reading the inconsistency as a fact about psychology",
             "The result is a statement about the pair of choices: no probability "
             "of black supports both. It does not say how many people choose "
             "this way or why, which is an empirical matter."),
        ],
        "standard": ("Finish when you can show that two choices fit no single credence.",
                     "Given the urn, you should be able to write each bet's chance in "
                     "terms of one unknown, state each choice as an inequality, find "
                     "the value at which the bets tie, and show that the popular "
                     "pair needs the unknown to be on both sides of it."),
        "note": "The urn is idealised: the red count is known and the rest is stipulated as unknown. The lab scores the table you enter and has no view on whether ignorance of a proportion should be treated as a probability. That is the question the lesson leaves open.",
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "pascals-wager",
        "title": "Pascal's Wager",
        "module": "Puzzles of expected value",
        "one_line": "A cost, a probability and a reward fix the threshold at which wagering wins, and an infinite reward removes the threshold.",
        "summary": (
            "Pascal argued that one should wager on God's existence, because the "
            "reward is large and the cost small. As a decision table the argument "
            "turns on a threshold, the reward at which the expected value of "
            "wagering reaches zero, and on what an infinite reward does to every "
            "act with a positive probability of reaching it."
        ),
        "key": [
            "wager costs c; God exists with chance p",
            "reward M if God exists",
            "EU(wager) = p·M − c",
            "EU(abstain) = 0",
            "wagering wins when M > c / p",
            "M infinite: any p above 0 wins",
            "two gods: the argument recommends both",
        ],
        "key_label": "A threshold, and what removes it",
        "concepts_intro": (
            "Pascal's argument is a decision table with an unusual payoff. Set "
            "it out like any other and the argument becomes a calculation."
        ),
        "concepts": [
            ("The wager as a table",
             "Two acts, wager or abstain, against two states, God exists or not. "
             "Wagering costs `c` in every state and pays a reward `M` if God "
             "exists. Abstaining costs nothing and earns nothing."),
            ("The threshold",
             "Wagering scores `p·M − c`, so it beats abstaining when `M` exceeds "
             "`c / p`. The smaller the probability, the larger the reward has to be, "
             "and below the threshold wagering loses."),
            ("The infinite reward",
             "If `M` is infinite, `p·M` is infinite for any `p` above zero, however "
             "small, and the argument no longer depends on a probability. That is "
             "the strongest form, and the one with the worst consequence."),
        ],
        "read_title": "The wager in a table, its tipping point and its limit",
        "read_intro": "A finite reward first, because that is where the arithmetic lives. The infinite case comes last.",
        "body": [
            ("p", "Blaise Pascal's wager is an argument that belief in God is the "
                  "prudent bet. It says nothing about whether God exists. It says "
                  "that if you are not certain either way, then wagering on God "
                  "has the larger expected value, because the reward is so great "
                  "that even a small chance of it outweighs the cost of living as "
                  "a believer."),
            ("p", "Set it out as a decision table. Let `p` be your probability "
                  "that God exists, `c` the cost of the wager, which stands for "
                  "everything a life of belief gives up, and `M` the reward if God "
                  "exists. Scores are measured from abstaining, which is "
                  "worth 0."),
            ("math", [
                "act        God exists    no God",
                "wager        M − c        −c",
                "abstain        0            0",
            ]),
            ("p", "The expected value of wagering is `p·(M − c) − (1 − p)·c`, which "
                  "simplifies to `p·M − c`. It beats abstaining when this is "
                  "above zero, that is, when `M` exceeds `c / p`."),
            ("thm", ("The wager's threshold",
                     "Wagering has higher expected value than abstaining exactly when "
                     "`M > c / p`. At `M = c / p` the two tie, and below it "
                     "abstaining wins.")),
            ("p", "Pascal himself denied that the second row was available. You are "
                  "already embarked, he said; not to wager for God is to wager "
                  "against, and there is no standing aside. The table survives the "
                  "point. Read the second act as wagering against, with the same "
                  "payoff of 0 in each state, and nothing in the arithmetic changes; "
                  "what changes is that a chooser who takes it can no longer say "
                  "she has stayed out of the game. That is the argument in its "
                  "strongest form, and the objections below are aimed at it."),
            ("p", "Take `p = 1/1000`, `c = 1` and `M = 1000`. The threshold is "
                  "`c / p = 1000`, so the wager sits exactly on it: the lab prints a "
                  "tie, with expected value 0 and the tipping point `p = 1/1000`. "
                  "Raise the reward to 1001 and wagering wins, with expected value "
                  "1/1000. Lower it to 999 and abstaining wins. One unit either way "
                  "reverses the advice, so the number to argue about is the "
                  "reward and not the shape of the argument."),
            ("p", "The first objection is aimed at the premise that the probability "
                  "is worth counting. A probability of one in a thousand is small, "
                  "and a reader may be tempted to say that nobody lives by "
                  "chances like that. The table does not allow it. A chance that "
                  "small is exactly offset by a reward that large, and "
                  "that is what an expected value is. Whoever ignores small "
                  "probabilities must say below which figure they stop counting "
                  "and why that figure."),
            ("p", "The second objection is the sharper one. Suppose the reward is "
                  "infinite, as the wager's defender wants, so no finite cost "
                  "can outweigh it. Then `p·M` is infinite for every `p` above "
                  "zero, and the argument no longer needs a probability, only "
                  "that the probability is not exactly zero. That is also its "
                  "undoing. Any other god, however improbable, who offers an infinite "
                  "reward on a different condition has the same argument."),
            ("example", ("Two gods",
                         "God A rewards those who wager on A and God B rewards "
                         "those who wager on B, each with probability 1/1000 and "
                         "reward 1001, and wagering on the wrong god costs 1 and "
                         "pays nothing. Wagering on either scores 1/1000. The "
                         "argument recommends both, and you cannot do both.")),
            ("p", "The third preset sets this up. The expected values tie between "
                  "the two wagers and both beat abstaining. With finite rewards "
                  "the tie is broken by changing a probability or a reward, and "
                  "the lab shows how much it takes. With infinite rewards "
                  "there is nothing to break it with, because infinity "
                  "times any positive probability is the same infinity. The "
                  "lab cannot take an infinity as input, and the lesson does not "
                  "pretend that it can."),
            ("p", "Three replies are on offer, and each has a cost. One caps the "
                  "reward, so that the threshold returns and the argument "
                  "becomes an ordinary comparison of a probability with a price. "
                  "One denies that a probability can be assigned to claims "
                  "like these. One keeps the infinity and accepts that it "
                  "recommends too much. The lab shows what each does to the "
                  "table and not which to take."),
        ],
        "lab": ("choicekit", {
            "mode": "decide", "rule": "eu",
            "preset": "pascal",
            "presets": [
                {"id": "pascal", "label": "chance 1/1000, cost 1, reward 1000",
                 "acts": ["wager", "abstain"], "states": ["God exists", "no God"],
                 "payoffs": [[999, -1], [0, 0]],
                 "probs": ["1/1000", "999/1000"], "expect": {"deChoice": "wager, abstain", "deValue": "0", "deFlip": "p(God exists) = 1/1000"}},
                {"id": "pascal-wins", "label": "the same, with reward 1001",
                 "acts": ["wager", "abstain"], "states": ["God exists", "no God"],
                 "payoffs": [[1000, -1], [0, 0]],
                 "probs": ["1/1000", "999/1000"], "expect": {"deChoice": "wager", "deValue": "1/1000", "deFlip": "p(God exists) = 1/1001"}},
                {"id": "many-gods", "label": "two gods at 1/1000 each, reward 1001",
                 "acts": ["wager on A", "wager on B", "abstain"],
                 "states": ["A exists", "B exists", "neither"],
                 "payoffs": [[1000, -1, -1], [-1, 1000, -1], [0, 0, 0]],
                 "probs": ["1/1000", "1/1000", "998/1000"], "expect": {"deChoice": "wager on A, wager on B", "deValue": "1/1000"}},
            ],
            "panel_title": "Find the reward at which the wager turns",
            "panel_intro": "The first preset sits exactly on the threshold. Change the 999 to 1000 and the wager wins; change it to 998 and abstaining wins. The tipping point tile prints the probability at which the two acts tie for whatever reward is in the box. In the third preset change the probabilities to 2/1000, 1/1000 and 997/1000 and watch the tie break in favour of A.",
        }),
        "steps_title": "Setting up the wager and finding its threshold",
        "steps_intro": "Five steps, with the cost counted once.",
        "steps": [
            ("Fix the baseline",
             "Measure every payoff from abstaining, so abstaining scores 0 "
             "in every state. What the believer gives up is the cost `c`."),
            ("Fill in the table",
             "Wagering pays `M − c` if God exists and `−c` if not. Write both "
             "entries before computing anything."),
            ("Score the wager",
             "Weight by the probabilities: `p·(M − c) − (1 − p)·c`, which reduces "
             "to `p·M − c`."),
            ("Solve for the threshold",
             "Set the score to zero and solve for the reward: `M = c / p`. Above "
             "it wagering wins, below it abstaining wins."),
            ("Add a rival",
             "Give a second state with its own wager. If its expected value "
             "matches the first, the argument recommends both and cannot choose."),
        ],
        "worked": {
            "title": "The threshold, then one unit above it",
            "intro": [
                "Take `p = 1/1000` and `c = 1`. The wager pays `M − 1` if God "
                "exists and `−1` otherwise; abstaining pays 0."
            ],
            "lines": [
                "EU(wager) = p·M - c",
                "M = 1000:  1/1000·1000 - 1 = 0, a tie",
                "M = 1001:  1/1000·1001 - 1 = 1/1000",
                "threshold: M = c / p = 1 / (1/1000) = 1000",
            ],
            "after": [
                "At 1000 the wager ties with abstaining, and one more unit "
                "tips it. Each factor of ten off the probability moves the "
                "threshold by a factor of ten, and a reward that grows without "
                "bound passes every threshold."
            ],
        },
        "quiz_title": "Reading the threshold",
        "quiz": [
            {"q": "With p = 1/1000 and cost 1, at what reward does wagering tie "
                  "with abstaining?",
             "a": ["1", "100", "1000", "1,000,000"],
             "c": 2,
             "why": "The threshold is c / p = 1 / (1/1000) = 1000. A reward of 1 "
                    "or 100 is far below it, and 1,000,000 is far above it, so "
                    "wagering would win by a wide margin rather than tie."},
            {"q": "The probability is halved to 1/2000, with cost 1. What happens "
                  "to the threshold?",
             "a": ["It doubles to 2000", "It halves to 500",
                   "It stays at 1000", "It becomes infinite"],
             "c": 0,
             "why": "The threshold is c / p, so halving p doubles it. It does "
                    "not halve, which would be the effect of halving the cost; "
                    "it does not stay fixed, since p is in the formula; and it is "
                    "finite for any p above zero."},
            {"q": "Why does an infinite reward remove the need for a probability?",
             "a": ["Infinite rewards make the cost zero",
                   "Infinity times any probability above zero is infinite, so the "
                   "wager always exceeds any finite cost",
                   "Infinite rewards make the probability 1",
                   "The lab refuses infinite rewards, so none are possible"],
             "c": 1,
             "why": "The product p·M is infinite whenever p is above zero, "
                    "however small. The reward does not change the cost or the "
                    "probability. The lab cannot take an infinity, but that is a "
                    "limit of the lab and not an argument about the wager."},
            {"q": "Two gods each have probability 1/1000 and reward 1001, and "
                  "wagering on the wrong one costs 1. What does the table say?",
             "a": ["Wager on A, because it is listed first",
                   "Abstain, because the two cancel",
                   "Wager on B, because it has the larger reward",
                   "The two wagers tie, and both beat abstaining"],
             "c": 3,
             "why": "Each wager scores 1/1000, so they tie and both exceed the "
                    "0 of abstaining. The order of the list does not matter, "
                    "the rewards are equal, and the wagers do not cancel: "
                    "each is evaluated against abstaining on its own."},
        ],
        "mistakes": [
            ("Thinking a tiny probability can be ignored",
             "At a chance of one in a thousand and a reward of 1001, wagering "
             "scores 1/1000 and beats abstaining. A chance that small is "
             "offset exactly by a reward that large. To ignore small probabilities "
             "one needs a rule saying how small, and the table then answers "
             "to that rule and not to the wager."),
            ("Treating the infinite reward as a bigger finite one",
             "A finite reward has a threshold `c / p`, and the lab shows the "
             "wager flipping at it. An infinite reward has none, because every "
             "positive probability reaches it, and the same argument supports every "
             "rival wager. The two cases differ in kind and not in size."),
            ("Reading the lab's verdict as an argument for belief",
             "The table scores a wager on a probability that you supply. "
             "It says nothing about whether God exists, whether belief can be "
             "adopted for a reason like this, or whether the reward and the "
             "probability are the right numbers. Those are the premises the "
             "argument turns on."),
        ],
        "standard": ("Finish when you can compute the wager's threshold and say what removes it.",
                     "Given a probability, a cost and a reward, you should be able to "
                     "set out the table, compute the expected value of wagering, find "
                     "the reward at which it ties with abstaining, and describe what an "
                     "infinite reward and a rival god each do to the argument."),
        "note": "Pascal's own text has several arguments and this lesson takes only the decision-theoretic one. The probability and the cost are inputs the reader supplies; the lab does not think any particular value is right, and no value can be derived from the table.",
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "newcombs-problem",
        "title": "Newcomb's Problem",
        "module": "Puzzles of expected value",
        "one_line": "Two valid arguments recommend opposite acts, and the predictor's accuracy fixes where the evidential one turns.",
        "summary": (
            "A predictor has already filled or emptied a box according to what it "
            "forecast you would do. Two-boxing beats one-boxing in every column of "
            "the table, while one-boxing has the higher expected value once the "
            "predictor's record is counted. The accuracy at which the evidential "
            "verdict turns is computed."
        ),
        "key": [
            "box A holds 1,000 for certain",
            "box B holds 1M if one-boxing was foreseen",
            "accuracy a: predictor right with chance a",
            "dominance: two-boxing ahead in every state",
            "one-boxing wins iff a > 1001/2000",
        ],
        "key_label": "Dominance against the record",
        "concepts_intro": (
            "Two arguments, both valid and both from reasoning the course has "
            "already taught, reach opposite conclusions about the same table."
        ),
        "concepts": [
            ("Dominance looks at the state",
             "The boxes are already filled. Whatever is in the second box, taking "
             "both leaves you 1,000 better off than taking one. An act that is "
             "better in every state dominates."),
            ("Evidential value looks at the act as news",
             "What you choose is evidence about what the predictor foresaw. If it "
             "is usually right, one-boxers usually find a full box and two-boxers "
             "an empty one, and the average over those cases favours one-boxing."),
            ("Accuracy is a dial",
             "How strongly the act is evidence depends on how reliable the "
             "predictor is. At accuracy one half the act tells you nothing, and "
             "above a threshold slightly over one half the evidential "
             "verdict flips."),
        ],
        "read_title": "The table, the two arguments and the accuracy at which they part",
        "read_intro": "The setup, then the two arguments at full strength, then the arithmetic that locates the switch.",
        "body": [
            ("p", "Robert Nozick's version of William Newcomb's problem runs like "
                  "this. Two boxes sit in front of you. Box A is open and holds "
                  "1,000 dollars. Box B is closed and holds either 1,000,000 "
                  "dollars or nothing. You may take both boxes or take box B "
                  "alone. A predictor, who has been right in the past, has "
                  "already decided what to put in B: the million if it forecast "
                  "that you would take only B, nothing if it forecast that you "
                  "would take both."),
            ("p", "Write the table with two states, box full and box empty, and "
                  "two acts. Dollars are scored at face value here, so the "
                  "threshold below is a dollar threshold; a concave utility "
                  "would move it and leave the structure alone."),
            ("math", [
                "act           box full      box empty",
                "one-box       1,000,000             0",
                "two-box       1,001,000         1,000",
            ]),
            ("p", "The first argument is dominance. The boxes are filled and what "
                  "you do now cannot change them. Whichever state you are in, the "
                  "two-box row is 1,000 higher than the one-box row, so "
                  "two-boxing is the better act in every state. This is the same "
                  "argument as in “The Decision Matrix and Dominance”, and it is "
                  "valid."),
            ("p", "The second argument uses the predictor's record. Let `a` be "
                  "the probability that the predictor is right about whoever "
                  "stands before it. Then a one-boxer finds a full box with "
                  "probability `a`, and a two-boxer finds a full box with "
                  "probability `1 − a`. Score each act with those conditional "
                  "probabilities."),
            ("math", [
                "EU(one-box) = a·1,000,000",
                "EU(two-box) = (1 − a)·1,001,000 + a·1,000",
            ]),
            ("thm", ("The evidential threshold",
                     "One-boxing has the higher evidential expected value exactly when "
                     "`a > 1001/2000`. At `a = 1001/2000` the two tie, and below it "
                     "two-boxing is ahead.")),
            ("p", "At accuracy 9/10 the lab scores one-boxing at 900,000 and "
                  "two-boxing at 101,000. The evidential rule recommends taking "
                  "one box, while the dominance rule, switched on in the same "
                  "lab, says the second row wins. At accuracy 1/2, a coin flip, "
                  "one-boxing scores 500,000 and two-boxing 501,000, so the "
                  "evidential rule also recommends both boxes. The switch lies "
                  "just above one half, because the extra 1,000 in box A is "
                  "small beside the million."),
            ("p", "The two rules agree below the threshold and part above it. A "
                  "predictor right fewer than 1001 times in 2000 gives both "
                  "rules the same answer, two boxes, and at exactly that accuracy "
                  "the evidential scores tie. For every accuracy above it the "
                  "rules part, and which is correct depends on what one thinks "
                  "an act is for."),
            ("p", "The one-boxer says: look at who ends up rich. The two-boxer "
                  "says: the money is there or not already, and a rational "
                  "chooser takes what she can. Each says a valid thing. The "
                  "dominance argument takes the states as fixed; the evidential "
                  "argument treats the act as information about the state. "
                  "Whether the act can be treated as independent of the "
                  "contents of the box is the premise the problem exists to "
                  "test."),
            ("p", "Two quick answers fail. One says the predictor's record is "
                  "irrelevant because the boxes are already filled. That "
                  "confuses what the act causes with what it is evidence "
                  "for, and the lab shows the record changing the evidential "
                  "figure from 101,000 to 900,000. The other says a high "
                  "accuracy settles the question. It settles only the "
                  "evidential rule, which is the rule in dispute."),
        ],
        "lab": ("choicekit", {
            "mode": "decide", "rule": "evidential",
            "preset": "newcomb-90",
            "presets": [
                {"id": "newcomb-90", "label": "a predictor right nine times in ten",
                 "acts": ["one-box", "two-box"], "states": ["box full", "box empty"],
                 "payoffs": [[1000000, 0], [1001000, 1000]],
                 "conditional": {"one-box": ["9/10", "1/10"], "two-box": ["1/10", "9/10"]},
                 "expect": {"deChoice": "one-box", "deValue": "900000"}},
                {"id": "newcomb-coin", "label": "a predictor right half the time",
                 "acts": ["one-box", "two-box"], "states": ["box full", "box empty"],
                 "payoffs": [[1000000, 0], [1001000, 1000]],
                 "conditional": {"one-box": ["1/2", "1/2"], "two-box": ["1/2", "1/2"]},
                 "expect": {"deChoice": "two-box", "deValue": "501000"}},
                {"id": "threshold", "label": "accuracy at the threshold, 1001/2000",
                 "acts": ["one-box", "two-box"], "states": ["box full", "box empty"],
                 "payoffs": [[1000000, 0], [1001000, 1000]],
                 "conditional": {"one-box": ["1001/2000", "999/2000"], "two-box": ["999/2000", "1001/2000"]},
                 "expect": {"deChoice": "one-box, two-box", "deValue": "500500"}},
            ],
            "panel_title": "Move the accuracy, then switch the rule",
            "panel_intro": "The rule starts as evidential, which scores each act by the conditional rows. Edit both conditional rows in the first preset so the accuracy falls from 9/10 to 1/2: the choice flips from one-box to two-box on the way, at 1001/2000. Then switch the rule to dominance, which ignores the conditional rows, and the verdict is two-box for every accuracy. The third preset sits on the threshold, where the evidential scores tie.",
        }),
        "steps_title": "Scoring both arguments and finding the switch",
        "steps_intro": "Five steps; the first four are mechanical.",
        "steps": [
            ("Write the table",
             "Two acts, two states (box full, box empty), and the dollar "
             "payoffs. Check that two-boxing is 1,000 higher in each column."),
            ("Test dominance",
             "An act dominates when it is at least as good in every state and "
             "better in one. Here two-boxing is better in both."),
            ("Write the conditional rows",
             "For each act, the probability of each state given that you "
             "choose it. With accuracy `a` the one-boxer's row is `a` and `1 − a`, "
             "the two-boxer's is `1 − a` and `a`."),
            ("Score each act with its own row",
             "Weight the payoffs by the act's conditional probabilities and "
             "add. Compare the two scores, and set them equal to find the "
             "accuracy where they tie."),
            ("Say which premise you reject",
             "Dominance needs the states to be fixed whatever you do; the "
             "evidential score treats the act as evidence. Decide which "
             "you will give up before you choose."),
        ],
        "worked": {
            "title": "Both verdicts at accuracy 9/10, and the switch",
            "intro": [
                "One-boxing pays 1,000,000 or 0; two-boxing pays 1,001,000 or "
                "1,000. The predictor is right with chance `a`."
            ],
            "lines": [
                "a = 9/10",
                "EU(one) = 9/10·1,000,000 = 900,000",
                "EU(two) = 1/10·1,001,000 + 9/10·1,000 = 101,000",
                "dominance: 1,001,000 > 1,000,000 and 1,000 > 0",
                "tie:  a·1,000,000 = 1,001,000 - a·1,000,000",
                "      a = 1001/2000",
            ],
            "after": [
                "At 9/10 the evidential rule says one box, by 900,000 to 101,000, "
                "and dominance says two, row by row. Both can be checked in the "
                "lab. They are different rules applied to the same table, and "
                "the accuracy at which the first gives way is just above a half."
            ],
        },
        "quiz_title": "Two arguments, one table",
        "quiz": [
            {"q": "At accuracy 9/10, what is the evidential expected value of "
                  "one-boxing?",
             "a": ["101,000", "1,000,000", "500,000", "900,000"],
             "c": 3,
             "why": "A one-boxer finds a full box with probability 9/10, so the "
                    "score is 9/10 times 1,000,000, which is 900,000. The figure "
                    "101,000 is the two-boxer's score. The full 1,000,000 ignores "
                    "the chance of an empty box, and 500,000 is the score at "
                    "accuracy 1/2."},
            {"q": "Why does two-boxing dominate?",
             "a": ["The predictor is probably wrong",
                   "It scores 1,000 more than one-boxing in each state, whether "
                   "the box is full or empty",
                   "Box A is certain, so box B can be ignored",
                   "Its expected value is higher at every accuracy"],
             "c": 1,
             "why": "Dominance compares rows state by state, and two-boxing is 1,000 "
                    "ahead in both. Dominance says nothing about the predictor. "
                    "Box B is not ignorable, as it holds the million. And "
                    "the evidential value of two-boxing is higher only below "
                    "1001/2000."},
            {"q": "Below what accuracy does the evidential rule recommend two-boxing?",
             "a": ["1001/2000", "1/2", "9/10", "1/1000"],
             "c": 0,
             "why": "The scores tie at a = 1001/2000, which is a little above 1/2, "
                    "and below it two-boxing is ahead. At exactly 1/2 two-boxing "
                    "already wins, so 1/2 is not the threshold. 9/10 is above "
                    "it, where one-boxing wins, and 1/1000 is not a threshold "
                    "of the problem."},
            {"q": "Which statement about the predictor's record is correct?",
             "a": ["It is irrelevant, since the boxes are already filled",
                   "It decides the problem, since a high record means one-box",
                   "It changes the evidential scores and leaves the dominance "
                   "verdict unchanged",
                   "It makes the two rules agree at every accuracy"],
             "c": 2,
             "why": "The conditional rows depend on the accuracy, so the "
                    "evidential scores move with it; the dominance comparison "
                    "uses only the payoff table. So the record is not irrelevant "
                    "to the evidential rule, and it does not decide between "
                    "rules. And the rules do not agree: two-boxing dominates at "
                    "every accuracy."},
        ],
        "mistakes": [
            ("Treating the predictor's record as irrelevant, or as decisive",
             "The record is irrelevant to dominance and fully relevant to the "
             "evidential score: at 9/10 it takes one-boxing from 101,000 for "
             "two-boxing up to 900,000. It is not decisive either, because "
             "it matters only if the act is to be treated as evidence about the "
             "box, which is what the two-boxer denies. The threshold, 1001/2000, "
             "shows where the evidential rule turns."),
            ("Thinking one of the two arguments is invalid",
             "Both are valid. Dominance takes the states as fixed whatever "
             "you do; the evidential argument takes the act as information "
             "about the state. The disagreement is over a premise, not a "
             "step, and the lab computes both without choosing."),
            ("Expecting a high accuracy to be needed",
             "The evidential switch is at 1001/2000, a hair above one half. A "
             "predictor right 51 times in 100 already favours one-boxing, "
             "because the million is so much larger than the thousand. The "
             "problem does not need a near-perfect predictor."),
        ],
        "standard": ("Finish when you can compute both verdicts and the accuracy at which they part.",
                     "Given the box payoffs and an accuracy, you should be able to show "
                     "that two-boxing dominates, compute each act's evidential "
                     "expected value from the conditional rows, find the accuracy at "
                     "which the evidential scores tie, and name the premise each "
                     "argument relies on."),
        "note": "The causal alternative to the evidential rule, which scores acts by what they bring about and not by what they indicate, is not built here: the table can show dominance and the evidential figure and no more. Dollars are scored at face value, which a concave utility would change in the figures and not in the shape.",
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "the-st-petersburg-game",
        "title": "The St Petersburg Game",
        "module": "Puzzles of expected value",
        "one_line": "A game with an infinite expected value is worth only a modest price once the bank's bankroll is capped.",
        "summary": (
            "A coin is tossed until it lands heads, and the prize doubles with each "
            "toss. Every term of the expected value is 1, so the sum grows without "
            "bound, and yet nobody would pay much to play. Capping the bankroll "
            "makes the series finite, and the lab computes the price for a bank "
            "of any size."
        ),
        "key": [
            "prize 2^k if the first head is on toss k",
            "chance of that: 1 / 2^k",
            "every term: 2^k · 1/2^k = 1",
            "n terms sum to n, with no upper bound",
            "bankroll cap: the series has a finite sum",
        ],
        "key_label": "Infinite on paper, small in practice",
        "concepts_intro": (
            "The puzzle sets expected value against common sense, and the sum "
            "that creates it can be written down in one line."
        ),
        "concepts": [
            ("Each term is the same",
             "A prize that doubles is exactly cancelled by a probability that "
             "halves, so every toss contributes 1 to the expected value. The "
             "partial sums are 1, 2, 3 and so on."),
            ("The sum has no ceiling",
             "However large a number you name, enough terms pass it. The "
             "expected value is not a large number but no number, and the "
             "rule says to pay anything for the right to play."),
            ("A cap turns the series finite",
             "A real bank can pay only what it has. Once the prize is capped at "
             "the bankroll, late terms shrink instead of staying at 1, and the "
             "series adds up to a figure you can compute."),
        ],
        "read_title": "Terms that never shrink, and a cap that makes them",
        "read_intro": "The sum first, then what stops it, then what the stopping does and does not show.",
        "body": [
            ("p", "A casino offers a game. A fair coin is tossed until it first "
                  "lands heads. If that happens on toss `k`, the player is paid "
                  "`2^k` dollars. So heads on the first toss pays 2, heads on "
                  "the second pays 4, heads on the third pays 8, and a run of "
                  "twenty tails before the first head pays over a million. The "
                  "question, posed in Nicolaus Bernoulli's letter of 1713, is "
                  "what the player should pay to enter."),
            ("p", "The expected value is the sum, over `k`, of the prize times "
                  "its probability. The first head falls on toss `k` with "
                  "probability `1 / 2^k`, so each term is the prize times that "
                  "chance."),
            ("math", [
                "k       prize     chance     term",
                "1           2        1/2        1",
                "2           4        1/4        1",
                "3           8        1/8        1",
                "4          16       1/16        1",
            ]),
            ("thm", ("Every term is 1",
                     "The term for toss `k` is `2^k · 1/2^k = 1`. After `n` tosses the "
                     "partial sum is exactly `n`, and a larger `n` passes any number "
                     "you name. The expected value is not finite.")),
            ("p", "The lab, with no cap and twenty terms, prints a sum of 20 and "
                  "no limit. Add terms and the sum rises by 1 each. If expected "
                  "value is the price to pay, the player should pay any amount "
                  "to enter, and no ticket is too dear. Nobody believes that. "
                  "Ask people what they would pay and the answer is usually "
                  "a few dollars."),
            ("p", "The first reply is that no bank has an infinite purse. Suppose "
                  "the bank has a bankroll of 1024 dollars, which is 2^10. If "
                  "the first head arrives on toss 10 or earlier the bank pays "
                  "in full. If it arrives later the bank pays only 1024. The "
                  "term for toss `k` then becomes 1024 divided by 2^k whenever `k` "
                  "is above 10."),
            ("math", [
                "k           1 to 10     11      12      13",
                "term              1    1/2     1/4     1/8",
            ]),
            ("p", "The first ten terms add to 10. The terms after them are a half, "
                  "a quarter, an eighth, and so on, which add to exactly 1. The "
                  "whole series therefore sums to 11, and 11 dollars is the "
                  "expected value of the game against a bank with 1024. The lab "
                  "prints the limit 11, and for twelve terms the partial sum "
                  "43/4, a quarter short of it."),
            ("p", "The cap grows slowly. A bank with 1,048,576 dollars, which is "
                  "2^20, gives twenty terms of 1 and then a tail of 1, so the "
                  "game is worth 21. A bank with a trillion dollars would "
                  "still be worth only a little over forty. The price rises with "
                  "the logarithm of the bank, which is why even a very rich "
                  "casino cannot make the game look expensive."),
            ("p", "So the capped game is no puzzle, but it is not a full answer "
                  "either. The puzzle was meant to show that expected value "
                  "and sensible price come apart, and the cap shows one "
                  "reason: the infinity was in the bank. Another reason is in the "
                  "utility, and it is Daniel Bernoulli's reply of 1738. If the "
                  "player values each extra dollar less, as in “Risk Aversion "
                  "and the Value of Information”, the late prizes are worth "
                  "little to her, and the sum of the utilities can be finite "
                  "without any cap. The lab computes the first reply only."),
            ("p", "Both replies leave something unsaid. A cap is a fact about the "
                  "bank. A utility curve is a fact about the player, and a "
                  "concave one closes this game without closing the puzzle: a "
                  "curve that keeps rising, however slowly, can be outrun by a "
                  "game whose prizes grow faster, and the infinite sum returns. "
                  "Only a utility with a ceiling closes every such game, and a "
                  "ceiling on how good things can get is a strong thing to "
                  "assert. A reader who finds either reply too convenient has "
                  "the harder position: that the uncapped game is a coherent "
                  "thing to evaluate, and that the rule gives the wrong answer "
                  "on it."),
        ],
        "lab": ("choicekit", {
            "mode": "series",
            "kind": "petersburg",
            "preset": "uncapped",
            "presets": [
                {"id": "uncapped", "label": "no bankroll limit, twenty terms",
                 "kind": "petersburg", "n": 20, "expect": {"srSum": "20", "srLimit": "none"}},
                {"id": "cap-1024", "label": "bankroll 1024, twelve terms",
                 "kind": "petersburg", "n": 12, "cap": 1024, "expect": {"srSum": "43/4", "srLimit": "11"}},
                {"id": "cap-million", "label": "bankroll 1,048,576, twenty terms",
                 "kind": "petersburg", "n": 20, "cap": 1048576, "expect": {"srSum": "20", "srLimit": "21"}},
            ],
            "panel_title": "Change the number of terms and the bankroll",
            "panel_intro": "Each preset sums the expected value of the game one toss at a time. Empty the bankroll box on the second preset and the limit becomes none. Put 1024 back, then raise the count to 60 and watch the sum close in on 11 without passing it. Change the bankroll to 2048 and the limit moves to 12: each doubling of the bank adds exactly 1.",
        }),
        "steps_title": "Summing the game, with and without a cap",
        "steps_intro": "Four steps, and the cap decides which sum you are asked for.",
        "steps": [
            ("Write the term for each toss",
             "Prize times probability. Without a cap this is `2^k · 1/2^k`, which "
             "is 1 for every `k`."),
            ("Add the terms",
             "The partial sum after `n` tosses is `n`, which has no upper bound. "
             "Any price is below the expected value."),
            ("Apply the bankroll",
             "Replace the prize by the smaller of `2^k` and the bankroll. "
             "Terms up to the cap stay 1; later ones are the bankroll over `2^k`."),
            ("Add the tail",
             "Beyond the cap the terms halve each time, so they sum to a "
             "number you can write down. Add it to the count of terms "
             "of 1 to get the value of the game."),
        ],
        "worked": {
            "title": "The same game with a bankroll of 1024",
            "intro": [
                "The bank can pay at most 1024, which is 2^10, so tosses 1 to 10 pay "
                "in full and later tosses pay 1024."
            ],
            "lines": [
                "tosses 1 to 10:   10 terms of 1 = 10",
                "toss 11:          1024/2048 = 1/2",
                "toss 12:          1024/4096 = 1/4",
                "tail from toss 11: 1/2 + 1/4 + 1/8 + ... = 1",
                "value of the game = 10 + 1 = 11",
            ],
            "after": [
                "Twenty terms of an uncapped game sum to 20 and the sum keeps "
                "growing; the capped game sums to 11 and stops. A price of 11 "
                "or less is then a fair one against this bank, which is a "
                "very different answer to the one the infinite sum gave."
            ],
        },
        "quiz_title": "Terms, sums and caps",
        "quiz": [
            {"q": "What is the term for toss 5 of the uncapped game?",
             "a": ["1/32", "32", "5", "1"],
             "c": 3,
             "why": "The prize is 2^5 = 32 and the probability is 1/32, so the "
                    "product is 1. The value 32 is the prize and 1/32 the "
                    "probability, each only half the term. The number 5 is the "
                    "partial sum after five terms."},
            {"q": "Why does an uncapped expected value of this kind recommend "
                  "paying any price?",
             "a": ["Because the game is certain to pay a lot",
                   "Because every term is positive, so some price is "
                   "always below the sum",
                   "Because the partial sums grow without bound, so any price is "
                   "eventually below the sum",
                   "Because the player is risk averse"],
             "c": 2,
             "why": "The sum has no ceiling, so any finite price is passed after "
                    "enough terms. The game is not certain to pay much: the "
                    "most likely prize is 2. Positive terms alone would not do it, "
                    "since a series of shrinking positive terms converges. "
                    "Risk aversion would lower the price, not raise it."},
            {"q": "The bank has 1024 dollars. What is the expected value of the game?",
             "a": ["10", "11", "1024", "no limit"],
             "c": 1,
             "why": "Ten terms of 1 give 10, and the later terms 1/2 + 1/4 + ... add "
                    "to 1, so the total is 11. The value 10 omits the tail. The "
                    "bankroll 1024 is the largest prize and not the "
                    "average. And the capped sum has a limit."},
            {"q": "The bankroll is doubled from 1024 to 2048. What happens to the "
                  "value of the game?",
             "a": ["It rises by 1, to 12", "It doubles to 22",
                   "It is unchanged", "It becomes unbounded"],
             "c": 0,
             "why": "A bankroll of 2048 is 2^11, which gives eleven terms of 1 and a "
                    "tail of 1, so the value is 12. It does not double, since the "
                    "value grows with the logarithm of the bankroll. It is not "
                    "unchanged, and a finite cap never makes it unbounded."},
        ],
        "mistakes": [
            ("Thinking an infinite expected value means you should pay any price",
             "The expected value is infinite only if the bank can pay any prize. "
             "Against a bank of 1024 dollars the value is 11 and against one of "
             "1,048,576 it is 21. The infinity belongs to an idealised bank, "
             "and a rule applied to a game the bank could never run is not "
             "a rule applied to a game you could play."),
            ("Reading the cap as a refutation of expected value",
             "The cap removes the infinity but not the gap between the "
             "expected value and what most people would pay, which for a bank "
             "of a million dollars is 21. Whether expected value is the right "
             "price or whether the utility of late prizes should be "
             "discounted is still open."),
            ("Expecting the value to grow in step with the bank",
             "Each doubling of the bankroll adds exactly 1 to the value. A bank "
             "a thousand times larger adds about ten. The sum is dominated by the "
             "early terms, because the late prizes, though large, are very "
             "unlikely."),
        ],
        "standard": ("Finish when you can sum the game and price it against a given bank.",
                     "Given a bankroll, you should be able to write the term for each "
                     "toss, show that without a cap each term is 1 and the sum "
                     "has no ceiling, and compute the value of the capped game as "
                     "the count of full terms plus the tail."),
        "note": "The lab sums the expectation exactly, one toss at a time, and the bankroll must be a whole number of dollars. It scores dollars at face value. A bounded utility, the other standard reply, is described here and not computed.",
    },
]
