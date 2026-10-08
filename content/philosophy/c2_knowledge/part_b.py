"""Course 2, lessons 07-12 -- conditional credence, updating, testimony, reference classes, and the lottery and preface paradoxes."""

LESSONS = [
    # ---------------------------------------------------------------- 07
    {
        "slug": "conditional-credence-and-base-rates",
        "title": "Conditional Credence and Base Rates",
        "module": "Credence",
        "one_line": "Why a test that is right 99 times in 100 can leave most of its positives false.",
        "summary": (
            "A conditional credence is a credence on the supposition that something "
            "else is true, and it is a ratio of two ordinary ones. Counting a "
            "million people shows that the chance of a positive result given the "
            "condition is a different number from the chance of the condition given "
            "a positive result, and that the gap is set by how rare the condition is."
        ),
        "key": [
            "P(A | B) = P(A ∧ B) / P(B)",
            "P(+ | D) is not P(D | +)",
            "rare condition: most positives are false",
            "count a million people, then divide",
        ],
        "key_label": "Two conditionals, two questions",
        "concepts_intro": (
            "Evidence arrives as a result of a test, a report or an observation. "
            "What it does to a credence is a conditional credence, and the first "
            "job is to keep its two directions apart."
        ),
        "concepts": [
            ("A conditional credence is a ratio",
             "The credence in A on the supposition that B is true is the credence "
             "in both, divided by the credence in B. It is defined only when B has "
             "credence above 0."),
            ("The two directions answer different questions",
             "How likely a positive result is for someone who has the condition, and "
             "how likely the condition is for someone with a positive result, have "
             "different denominators. They are equal only by coincidence."),
            ("The base rate sets the gap",
             "The proportion of people who have the condition before any test is "
             "the base rate. When it is small, the false positives from the many "
             "healthy people can outnumber the true positives from the few sick ones."),
        ],
        "read_title": "A test, a condition and a million people",
        "read_intro": "The same arithmetic done twice: as counts of people, then as a formula.",
        "body": [
            ("p", "Almost every grandmother is a woman, and very few women are "
                  "grandmothers. The two statements are about different groups, and "
                  "nothing forces their proportions to match. A conditional "
                  "credence makes the difference exact."),
            ("def", ("Conditional credence",
                     "The <strong>conditional credence</strong> in A given B is "
                     "`P(A | B) = P(A ∧ B) / P(B)`, defined when `P(B)` is above 0. "
                     "Credences are written with `P`, like the probabilities whose "
                     "rules they obey. It is the credence you would hold in A if you "
                     "learned B and nothing else, and the direction of the bar "
                     "matters: `P(A | B)` and `P(B | A)` are different numbers.")),
            ("p", "Now a test for a condition. One person in 1,000 has it. The test "
                  "is positive for 99 in 100 of those who have it, and positive for "
                  "5 in 100 of those who do not. A person tests positive. The "
                  "question is how likely it is that they have the condition, and the "
                  "easiest way to answer it is to count a million people."),
            ("math", [
                "              has it    does not      total",
                "-------------------------------------------",
                "tests +          990       49950      50940",
                "tests −           10      949050     949060",
                "total           1000      999000    1000000",
            ]),
            ("p", "Of the 1,000 who have the condition, 99 in 100 test positive, "
                  "which is 990, and the other 10 test negative. Of the 999,000 who "
                  "do not, 5 in 100 test positive, which is 49,950, and the "
                  "remaining 949,050 test negative. Everyone who tests positive is "
                  "in the first row: 990 plus 49,950, which is 50,940 people."),
            ("math", [
                "P(D | +) = 990 / 50940 = 11/566, about 1.9%",
            ]),
            ("p", "Fewer than 2 in 100 of the people with a positive result have "
                  "the condition. The number 99 in 100 is `P(+ | D)`, the "
                  "proportion of the 1,000 who test positive, and the question asked "
                  "for `P(D | +)`, the proportion of the 50,940 who have it. The "
                  "two share a numerator and have different denominators."),
            ("p", "The reason is the size of the second column. There are 999 healthy "
                  "people for every sick one, so a false positive rate of 5 in 100 "
                  "produces about fifty false positives for each true one. A very "
                  "accurate test applied to a rare condition mostly produces false "
                  "alarms, and the mistake of reading `P(+ | D)` as `P(D | +)` is "
                  "called <strong>base-rate neglect</strong>."),
            ("h3", "The base rate is an input, not background"),
            ("p", "Hold the test fixed and change who is tested. If 30 in 100 of "
                  "those tested have the condition, the same test gives "
                  "`P(D | +) = 297/332`, about 89%. Nothing about the test has "
                  "changed. The people have, and a positive result is worth what "
                  "the population makes it worth."),
            ("p", "A negative result is the other half of the table. Of the 949,060 "
                  "who test negative, 10 have the condition, so `P(D | −)` is "
                  "`1/94906`. In this population a negative result is far more "
                  "conclusive than a positive one, which is not what the phrase "
                  "&ldquo;99% accurate&rdquo; suggests."),
            ("p", "The lab states its limit plainly: it divides the counts it is "
                  "given. Whether 1 in 1,000 is the right base rate for the person "
                  "in front of you, who may have been tested because of symptoms, "
                  "is a question about which group they belong to, and a later "
                  "lesson takes it up."),
        ],
        "lab": ("bayes", {
            "prev": 1000,
            "sens": 99,
            "fpr": 5,
            "panel_title": "The test, counted",
            "panel_intro": "The lab opens on this lesson’s test: 1 in 1,000 have the "
                           "condition, 99% of them test positive and 5% of the others "
                           "do too. The table is the one above and the bar shows how "
                           "small the true-positive share is. Choose &ldquo;30 in "
                           "100&rdquo; from the prevalence menu to see the same test in "
                           "a different population, then move the false positive rate "
                           "to 0 to see what it would take to remove the problem.",
        }),
        "steps_title": "From a test result to P(D | +)",
        "steps_intro": "The order that avoids the usual mistake: counts first, ratio last.",
        "steps": [
            ("Take a round population",
             "A million people, so that every cell is a whole number. The prior "
             "tells you how many have the condition."),
            ("Split it by the condition",
             "Those who have it and those who do not. Do not skip the second group; "
             "it is the larger one."),
            ("Apply the test to each group separately",
             "The sensitivity applies to the first group and the false positive "
             "rate to the second. Neither is applied to the whole population."),
            ("Collect the positives",
             "Add the true positives and the false positives. This total, not the "
             "number with the condition, is the denominator."),
            ("Divide",
             "True positives over all positives is `P(D | +)`. Check it against the "
             "formula: the same two numbers appear."),
        ],
        "worked": {
            "title": "A positive result, counted",
            "intro": ["One person in 1,000 has the condition; sensitivity 99 in 100; false positives 5 in 100."],
            "lines": [
                "have it:            1,000    positive  990",
                "do not:           999,000    positive  49,950",
                "all positives:     990 + 49,950 = 50,940",
                "P(D | +) = 990 / 50,940 = 11/566",
                "P(+ | D) = 990 / 1,000   = 99/100",
            ],
            "after": [
                "The last two lines have the same numerator and different "
                "denominators, and that is the whole difference between them. "
                "Fewer than 2 in 100 of the people with a positive result have "
                "the condition.",
            ],
        },
        "quiz_title": "Which conditional, and how many",
        "quiz": [
            {"q": "In a million people with the lesson’s test, how many test positive?",
             "a": ["`990`", "`50,940`", "`49,950`", "`1,000`"],
             "c": 1,
             "why": "`990` is only the true positives and `49,950` is only the false ones; the positives are both together, `50,940`. `1,000` is the number who have the condition, a different group."},
            {"q": "Someone tests positive and asks how likely they are to have the condition. Which quantity answers that?",
             "a": ["`P(+ | D)`", "`P(D)`", "`P(+)`", "`P(D | +)`"],
             "c": 3,
             "why": "The question conditions on the result they have, so it is `P(D | +)`. `P(+ | D)` conditions on the wrong thing, `P(D)` is the credence before the test, and `P(+)` is the chance of a positive in the whole population."},
            {"q": "The same test is used where 30 in 100 have the condition. What happens to `P(D | +)`?",
             "a": ["It stays at `11/566`, since the test has not changed",
                   "It rises to `99/100`, the sensitivity",
                   "It rises to `297/332`, because true positives are now a larger share of the positives",
                   "It rises to `3/10`, the base rate"],
             "c": 2,
             "why": "The test is unchanged but the people are not: there are far more true positives against about the same stream of false ones. The sensitivity and the base rate are inputs to the answer, not the answer."},
            {"q": "A friend says: the test is 99% accurate, so a positive means a 99% chance of having the condition. What is missing from the reasoning?",
             "a": ["The base rate, which fixes how many of the positives come from people without the condition",
                   "The negative results, since `P(D | +)` is a share of the people who tested negative",
                   "Nothing; sensitivity is the probability of the condition given a positive",
                   "A larger sample, since the claim holds only for populations above a million"],
             "c": 0,
             "why": "Sensitivity is `P(+ | D)`, which says nothing about the false positives from the healthy majority. `P(D | +)` is a share of the positives and never of the negatives, the claim is not true by definition, and the count of a million was only for convenience."},
        ],
        "mistakes": [
            ("Reading P(+ | D) as P(D | +)",
             "The two have the same numerator, 990, and different denominators: `1,000` people who have the condition for the first, `50,940` people who tested positive for the second. For this test one is `99/100` and the other is `11/566`. A statement about how often the test finds the condition is not a statement about how often a positive result is right."),
            ("Treating the base rate as background",
             "Nothing about the test changes between the two populations, yet `P(D | +)` moves from `11/566` to `297/332`. The base rate is as much an input as the sensitivity. Leaving it out is not a simplification; it replaces the question with a different one."),
            ("Applying the number to any person who tested positive",
             "The figure `11/566` is true of the population of 1,000,000 as described. A patient who was tested because of symptoms is not drawn from that population, and the lab has no way to know it. The calculation is exact about the group it is given and silent about which group a person belongs to."),
        ],
        "standard": (
            "Finish when you can fill the table before you divide.",
            "You should be able to take a base rate, a sensitivity and a false positive rate, count a population into the four cells, and compute `P(D | +)` as a ratio of two of them. Stating the answer is not enough; say which two counts it is the ratio of and why the other direction has a different denominator."),
        "note": "The condition and the test here are invented to make the arithmetic clean. Real screening programmes have numbers of exactly this shape, and the same counting is how they are evaluated.",
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "updating-on-evidence",
        "title": "Updating on Evidence",
        "module": "Credence",
        "one_line": "A prior, the likelihood of what was seen, and the Bayes factor that measures the weight of the evidence.",
        "summary": (
            "Updating takes a prior over some hypotheses, multiplies each by how "
            "probable the observation is on it, and rescales so the results sum to "
            "1. The Bayes factor compares how probable the data are on a hypothesis "
            "and on its rivals, and a second observation updates the result of the "
            "first."
        ),
        "key": [
            "P(H | E) = P(E | H)·P(H) / P(E)",
            "Bayes factor: P(E | H) / P(E | ¬H)",
            "posterior odds = prior odds · factor",
            "fit is not proof: weigh the rival too",
        ],
        "key_label": "Weighing evidence",
        "concepts_intro": (
            "The previous lesson computed one conditional credence from a table. "
            "Updating is the same computation arranged so that it can be repeated "
            "as evidence keeps arriving."
        ),
        "concepts": [
            ("The likelihood belongs to the hypothesis",
             "How probable the observation is if the hypothesis is true. A "
             "hypothesis that makes the observation probable gains on one that "
             "makes it improbable, and neither number alone is the posterior."),
            ("The Bayes factor is the weight of the evidence",
             "The likelihood of the data on a hypothesis divided by its likelihood "
             "on the alternatives. A factor of 3 means the data are three times as "
             "probable on the hypothesis, and it multiplies the odds."),
            ("Updating in sequence agrees with updating once",
             "The posterior after the first observation is the prior for the second. "
             "The factors of independent observations multiply, and the order in "
             "which they arrive does not change the result."),
        ],
        "read_title": "Two urns and a red ball",
        "read_intro": "A prior, a likelihood and an observation, worked out on paper before the lab does it.",
        "body": [
            ("p", "Two urns hold four balls each. One of them is chosen by a fair "
                  "coin, you cannot see which, and a ball is drawn from it."),
            ("math", [
                "urn 1:  red  red  red  blue",
                "urn 2:  red  blue blue blue",
            ]),
            ("p", "The prior credence in each urn is `1/2`. A red ball is drawn. It "
                  "is red with probability `3/4` if the urn is urn 1 and `1/4` if "
                  "it is urn 2. Multiply each prior by its likelihood, then divide "
                  "by the total so that the posteriors sum to 1."),
            ("math", [
                "urn     prior    P(red | urn)    product    posterior",
                "---------------------------------------------------",
                "urn 1   1/2      3/4             3/8        3/4",
                "urn 2   1/2      1/4             1/8        1/4",
                "total                            1/2        1",
            ]),
            ("def", ("Posterior",
                     "The <strong>posterior</strong> credence in a hypothesis H after "
                     "evidence E is `P(H | E) = P(E | H)·P(H) / P(E)`. The "
                     "denominator `P(E)` is the total of the products over every "
                     "hypothesis, so the step is: multiply, add, divide.")),
            ("p", "The red draw moved urn 1 from `1/2` to `3/4`. A summary of how "
                  "much it moved, independent of where it started, is the "
                  "<strong>Bayes factor</strong>: the probability of the data on "
                  "urn 1, `3/4`, over the probability of the data on the "
                  "alternatives, `1/4`, which is 3."),
            ("def", ("Bayes factor and odds",
                     "The <strong>Bayes factor</strong> of the data for H is "
                     "`P(E | H) / P(E | ¬H)`, with the likelihood on the "
                     "alternatives averaged by their priors when there are several. "
                     "The <strong>odds</strong> on H are the credence in H against "
                     "the credence in `¬H`, so a credence of `3/4` is odds of 3 to 1, "
                     "and odds of `a` to `b` are a credence of `a/(a + b)`. The "
                     "posterior odds on H equal the prior odds times the factor, "
                     "and a factor of 1 leaves the credence where it was.")),
            ("p", "Here the prior odds are 1 to 1, the factor is 3, and the "
                  "posterior odds are 3 to 1, which is the posterior `3/4`. With "
                  "two hypotheses the factor does not depend on the prior, so the "
                  "same red ball multiplies the odds by 3 whatever they were."),
            ("h3", "A second observation"),
            ("p", "Put the ball back and draw again. The second ball is also red. "
                  "The prior for this step is the previous posterior, `3/4` for urn "
                  "1, and the update gives `(3/4)·(3/4) = 9/16` against "
                  "`(1/4)·(1/4) = 1/16`, so the posterior is `9/10`. The factors "
                  "multiply, `3 · 3 = 9`, and so do the odds, 1 to 1, then 3 to 1, "
                  "then 9 to 1. Had the second ball been blue, the factor for urn 1 "
                  "would have been `1/3` and the credence would have returned to "
                  "`1/2`; the same two balls in the other order give the same "
                  "answer."),
            ("h3", "Fit is not proof"),
            ("p", "A coin is either two-headed or fair, and the prior for two-headed "
                  "is `1/100`. Three heads in a row are certain on the two-headed "
                  "coin and have probability `1/8` on the fair one. That is a "
                  "Bayes factor of 8, and the lab gives a posterior of `8/107` for "
                  "two-headed: under 8%."),
            ("p", "The evidence confirms the hypothesis, in that its credence "
                  "rose from `1/100`, and fits it perfectly, since its likelihood is "
                  "1. It does not prove it. A posterior of 1 would need the data to "
                  "be impossible on every rival, and a rival that makes three heads "
                  "merely improbable keeps its share of the credence. The reverse is "
                  "stricter: one tails makes the likelihood of the two-headed coin "
                  "0 and its posterior 0, whatever the prior."),
            ("p", "What the lab cannot supply is the hypotheses. It updates over "
                  "the ones listed, with the likelihoods typed in, and if the truth "
                  "is not among them it still prints exact fractions."),
        ],
        "lab": ("choicekit", {
            "mode": "update",
            "preset": "urns",
            "presets": [
                {"id": "urns", "label": "two urns, one red ball",
                 "hyps": ["urn 1", "urn 2"], "prior": ["1/2", "1/2"],
                 "outcomes": ["red", "blue"], "lik": [["3/4", "1/4"], ["1/4", "3/4"]],
                 "data": ["red"], "payoffs": None,
                 "expect": {"upPost": "3/4", "upBF": "3"}},
                {"id": "two-draws", "label": "two urns, two red balls",
                 "hyps": ["urn 1", "urn 2"], "prior": ["1/2", "1/2"],
                 "outcomes": ["red", "blue"], "lik": [["3/4", "1/4"], ["1/4", "3/4"]],
                 "data": ["red", "red"], "payoffs": None,
                 "expect": {"upPost": "9/10", "upBF": "9"}},
                {"id": "bias", "label": "a two-headed coin or a fair one, three heads",
                 "hyps": ["two-headed", "fair"], "prior": ["1/100", "99/100"],
                 "outcomes": ["heads", "tails"], "lik": [["1", "0"], ["1/2", "1/2"]],
                 "data": ["heads", "heads", "heads"], "payoffs": None,
                 "expect": {"upPost": "8/107", "upBF": "8"}},
            ],
            "panel_title": "Change the prior, the likelihoods or the data",
            "panel_intro": "Each row of the likelihoods is one hypothesis and must sum to 1. Type red red, or red blue, and compare; then add a third red and watch the factor for urn 1 reach 27. The menu at the foot of the controls chooses which hypothesis the tiles report.",
        }),
        "steps_title": "Updating on one observation",
        "steps_intro": "Five moves, the same whether there are two hypotheses or five.",
        "steps": [
            ("List the hypotheses and their priors",
             "The priors must sum to 1, and the list must include the truth if the "
             "answer is to be trusted."),
            ("Read off the likelihood of what was seen",
             "For each hypothesis, how probable the observation is if it is true. "
             "A likelihood is not a credence in the hypothesis."),
            ("Multiply, add and divide",
             "Multiply each prior by its likelihood, add the products, and divide "
             "each product by the total. The results are the posteriors."),
            ("Report the Bayes factor",
             "Divide the likelihood on the hypothesis by the likelihood on the "
             "rest. It says how much the observation moved the odds, without the "
             "prior in it."),
            ("Use the posterior as the next prior",
             "For another observation, repeat the steps from the posterior. Do not "
             "return to the original prior and do not count an observation twice."),
        ],
        "worked": {
            "title": "Urn 1 after two red draws",
            "intro": ["Prior 1/2 each; urn 1 has 3 red in 4, urn 2 has 1 red in 4."],
            "lines": [
                "draw 1 red:   urn 1  1/2 · 3/4 = 3/8    urn 2  1/8",
                "posterior:    urn 1  3/8 / (1/2) = 3/4   factor 3",
                "draw 2 red:   urn 1  3/4 · 3/4 = 9/16   urn 2  1/16",
                "posterior:    urn 1  9/16 / (10/16) = 9/10",
                "factor so far:  3 · 3 = 9",
            ],
            "after": [
                "The same answer comes from one step using both balls: "
                "the likelihood of two reds is `9/16` on urn 1 and `1/16` on urn "
                "2, a factor of 9 on prior odds of 1 to 1. Updating twice and "
                "updating once are the same arithmetic.",
            ],
        },
        "quiz_title": "Posteriors and factors",
        "quiz": [
            {"q": "Two urns have priors of 1/2 each. One red ball is drawn: urn 1 gives red with probability 3/4, urn 2 with 1/4. What is the posterior for urn 1?",
             "a": ["`3/4`", "`3/8`", "`1/2`", "`9/10`"],
             "c": 0,
             "why": "The products are `3/8` and `1/8`, which total `1/2`, and `(3/8)/(1/2) = 3/4`. The value `3/8` is the product before dividing, `1/2` is the prior, and `9/10` is the posterior after a second red."},
            {"q": "The data carry a Bayes factor of 9 for H, and the prior credence in H is 1/5. What is the posterior credence in H?",
             "a": ["`9/5`", "`9/10`", "`9/13`", "`4/13`"],
             "c": 2,
             "why": "Prior odds are 1 to 4, and times 9 they are 9 to 4, which is a credence of `9/13`. `9/5` is not a credence, `9/10` is what a factor of 9 gives from even odds, and `4/13` is the credence in the negation."},
            {"q": "Three heads fit the two-headed coin perfectly, and its prior was 1/100. Which statement is correct?",
             "a": ["The data prove the coin is two-headed, since its likelihood is 1",
                   "The data count in favour of the fair coin, since it can also give three heads",
                   "The posterior for the two-headed coin is the likelihood times the prior, `1/100`",
                   "The data confirm the two-headed coin, raising it to `8/107`, and the fair coin is still much more probable"],
             "c": 3,
             "why": "The factor is 8, so the credence rises from `1/100` to `8/107` without coming near 1. A likelihood of 1 is not a posterior of 1, the fair coin is disconfirmed since it makes the data less probable than its rival does, and `1/100` is the prior, not a product of the update."},
            {"q": "The credence in urn 1 is 3/4 after one red ball, and the next ball is blue. What is the credence in urn 1 now?",
             "a": ["`3/4`, since the blue ball is a single observation", "`1/2`", "`1/4`", "`3/16`"],
             "c": 1,
             "why": "A blue ball has likelihood `1/4` on urn 1 and `3/4` on urn 2, a factor of `1/3`, and odds of 3 to 1 become 1 to 1. Leaving the credence at `3/4` ignores the ball, `1/4` swaps the two urns, and `3/16` is the product before dividing by the total."},
        ],
        "mistakes": [
            ("Thinking that evidence that fits a hypothesis proves it",
             "Three heads fit the two-headed coin as well as anything could, with likelihood 1, and the lab still gives it only `8/107`. How well the hypothesis explains the data is one factor; how probable it was before, and how well the rival explains the data, are the others. Proof would need a rival that makes the data impossible."),
            ("Reading the Bayes factor as the posterior",
             "A factor of 9 does not mean a credence of `9/10`. It multiplies the odds, and the odds started somewhere. From a prior of `1/5` it gives `9/13`; from `1/100` it gives `1/12`; only from even odds is it `9/10`."),
            ("Using the same observation twice",
             "After the first red ball the credence in urn 1 is `3/4`. The second update starts from that, not from the original `1/2` and not by adding the first ball again. A single red ball counted twice would give `9/10` on the evidence of one draw."),
        ],
        "standard": (
            "Finish when you can update twice and name the factor each time.",
            "You should be able to take priors and likelihoods, produce posteriors by multiplying, adding and dividing, state the Bayes factor of the data for a hypothesis, and update again on a second observation, showing that the factors multiply."),
        "note": "The lab updates over a short list of hypotheses and a short list of outcomes, with likelihoods you type. It is the standard calculation of Bayesian updating, and everything that is philosophically contestable lies in the inputs.",
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "testimony-and-independent-witnesses",
        "title": "Testimony and Independent Witnesses",
        "module": "Credence",
        "one_line": "What a witness of stated reliability does to a prior, and why independent witnesses multiply.",
        "summary": (
            "A witness who is right 9 times in 10 does not make the claim 9 in 10 "
            "likely; the prior still counts. Each independent witness contributes "
            "its own Bayes factor and the factors multiply. Hume’s argument about "
            "miracles compares two likelihoods: that the witness is mistaken, and "
            "that the event happened."
        ),
        "key": [
            "reliability: P(yes | true), not P(true | yes)",
            "a witness: one Bayes factor, r / (1 − r)",
            "independent witnesses: factors multiply",
            "Hume: compare a false report with a miracle",
        ],
        "key_label": "A witness is a test",
        "concepts_intro": (
            "A witness who says yes is evidence in the sense of the previous "
            "lesson, and nothing more. The lesson is to read the witness’s "
            "reliability as a likelihood."
        ),
        "concepts": [
            ("A witness has two likelihoods",
             "How probable a yes is if the claim is true, and how probable it is if "
             "the claim is false. A witness of reliability 9/10 says yes with "
             "probability 9/10 if it is true and 1/10 if it is false."),
            ("Independence is relative to the truth",
             "Two witnesses are independent when, once you know whether the claim is "
             "true, what one says tells you nothing about what the other says. "
             "Witnesses who share a source are not independent."),
            ("A miracle report compares two improbable things",
             "One is that the event happened, and the other is that the witness is "
             "wrong. Which is more probable decides what the report is worth."),
        ],
        "read_title": "One witness, then two",
        "read_intro": "A claim at 1 in 100, a witness at 9 in 10, and the arithmetic on paper.",
        "body": [
            ("p", "A claim has prior credence `1/100`. A witness who is reliable in "
                  "the sense that she says yes with probability `9/10` when the "
                  "claim is true, and says no with probability `9/10` when it is "
                  "false, says yes. So the likelihood of a yes is `9/10` if the "
                  "claim is true and `1/10` if it is false."),
            ("math", [
                "claim    prior     P(yes | claim)    product    posterior",
                "------------------------------------------------------",
                "true     1/100     9/10              9/1000     1/12",
                "false    99/100    1/10              99/1000    11/12",
            ]),
            ("p", "The posterior is `1/12`, about 8%. The witness raised the claim "
                  "from 1% to 8% and nowhere near 90%. Her Bayes factor is "
                  "`(9/10)/(1/10) = 9`, the prior odds are 1 to 99, and the posterior "
                  "odds are 9 to 99, which is 1 to 11."),
            ("p", "This is the error of the previous lessons in a different "
                  "setting. Her reliability, `9/10`, is the probability of a yes "
                  "given that the claim is true, and what is wanted is the "
                  "probability that the claim is true given a yes. They differ by "
                  "the same factor as before, and a claim that was improbable to "
                  "start with stays improbable unless the witness is very good."),
            ("def", ("Independent witnesses",
                     "Two witnesses are <strong>independent</strong> when, given "
                     "whether the claim is true, the probability of what one says "
                     "does not depend on what the other says. Then the likelihood of "
                     "both answers is the product of the two likelihoods, and so is "
                     "the Bayes factor.")),
            ("p", "A second witness of the same reliability also says yes. The "
                  "likelihood of two yeses is `(9/10)·(9/10) = 81/100` if the claim "
                  "is true and `(1/10)·(1/10) = 1/100` if it is false: a factor of "
                  "81, which is 9 times 9."),
            ("math", [
                "witnesses    Bayes factor    posterior odds    posterior",
                "-------------------------------------------------------",
                "none         1               1/99              1/100",
                "one          9               1/11              1/12",
                "two          81              9/11              9/20",
            ]),
            ("p", "Two independent witnesses take the claim to `9/20`, a little under "
                  "a half. The second is worth as much as the first in the sense "
                  "that matters, a factor of 9, and worth more in credence, because "
                  "the same factor applied at higher odds moves the credence further."),
            ("p", "Independence is an assumption the lab does not check. Two "
                  "newspapers that both reprint the same agency report are one "
                  "witness heard twice, and multiplying their factors would count "
                  "that witness’s possible error as if it had been confirmed."),
            ("h3", "Hume and the miracle"),
            ("p", "Hume’s argument about miracles can be put as a comparison of "
                  "two likelihoods. Suppose the prior for an extraordinary event is "
                  "`1/1000000`, and a witness reports it who is wrong only 1 time "
                  "in 1,000. Of the ways the report could come about, one is that "
                  "the event happened and the witness is right, with weight "
                  "`(1/1000000)·(999/1000)`; the other is that it did not and the "
                  "witness is wrong, with weight `(999999/1000000)·(1/1000)`. The "
                  "second is 1,001 times the first, and the posterior is `1/1002`."),
            ("p", "The conclusion is a comparison and not a ban. A report is "
                  "worth believing when its Bayes factor outweighs the odds against "
                  "the event. One witness at 999 in 1,000 has a factor of 999 "
                  "against odds of about a million, and three independent such "
                  "witnesses have a factor near a thousand million. The lab puts "
                  "the claim after three at about 99.9%. What the argument requires "
                  "is that the witnesses really are independent and that their "
                  "reliability is as stated, and those are the premises worth "
                  "disputing."),
        ],
        "lab": ("choicekit", {
            "mode": "update",
            "preset": "witness",
            "presets": [
                {"id": "witness", "label": "one witness, 9 in 10 reliable",
                 "hyps": ["claim true", "claim false"], "prior": ["1/100", "99/100"],
                 "outcomes": ["yes", "no"], "lik": [["9/10", "1/10"], ["1/10", "9/10"]],
                 "data": ["yes"], "payoffs": None,
                 "expect": {"upPost": "1/12", "upBF": "9", "upConf": "Confirms"}},
                {"id": "two-witnesses", "label": "two independent witnesses",
                 "hyps": ["claim true", "claim false"], "prior": ["1/100", "99/100"],
                 "outcomes": ["yes", "no"], "lik": [["9/10", "1/10"], ["1/10", "9/10"]],
                 "data": ["yes", "yes"], "payoffs": None,
                 "expect": {"upPost": "9/20", "upBF": "81", "upConf": "Confirms"}},
                {"id": "miracle", "label": "a miracle, one witness at 999 in 1,000",
                 "hyps": ["it happened", "it did not"], "prior": ["1/1000000", "999999/1000000"],
                 "outcomes": ["yes", "no"], "lik": [["999/1000", "1/1000"], ["1/1000", "999/1000"]],
                 "data": ["yes"], "payoffs": None,
                 "expect": {"upPost": "1/1002", "upBF": "999", "upConf": "Confirms"}},
                {"id": "miracle-three", "label": "a miracle, three witnesses",
                 "hyps": ["it happened", "it did not"], "prior": ["1/1000000", "999999/1000000"],
                 "outcomes": ["yes", "no"], "lik": [["999/1000", "1/1000"], ["1/1000", "999/1000"]],
                 "data": ["yes", "yes", "yes"], "payoffs": None,
                 "expect": {"upPost": "998001/999002", "upBF": "997002999", "upConf": "Confirms"}},
            ],
            "panel_title": "Change the prior, the reliability or the number of witnesses",
            "panel_intro": "A reliability is a pair of likelihoods, typed row by row. Add a third yes to the first example and watch the factor become 729; type yes no to see two witnesses disagree and the factors cancel. The lab multiplies the likelihoods because it is told the witnesses are independent.",
        }),
        "steps_title": "Weighing a witness",
        "steps_intro": "Five moves, in the order that keeps the prior in view.",
        "steps": [
            ("Write the prior for the claim",
             "Before the witness spoke. A claim that was unlikely stays unlikely "
             "unless the evidence is strong."),
            ("Write the witness’s two likelihoods",
             "The chance of a yes if the claim is true and the chance of a yes if "
             "it is false. Reliability gives both when the witness is symmetric."),
            ("Form the Bayes factor",
             "The first over the second. A witness at 9 in 10 has a factor of 9; at "
             "999 in 1,000 a factor of 999."),
            ("Multiply for independent witnesses",
             "Check independence first, by asking whether they could have got the "
             "claim from one source. Then multiply the factors."),
            ("Convert to a posterior",
             "Multiply the prior odds by the total factor and turn the odds back "
             "into a credence."),
        ],
        "worked": {
            "title": "The claim at 1 in 100, two witnesses at 9 in 10",
            "intro": ["Each witness says yes."],
            "lines": [
                "prior odds:         1 : 99",
                "one witness:        factor 9    odds 9 : 99 = 1 : 11",
                "                    posterior 1/12",
                "second witness:     factor 9    odds 81 : 99 = 9 : 11",
                "                    posterior 9/20",
            ],
            "after": [
                "Each witness is right 9 times in 10, and two of them still leave "
                "the claim below even odds because it began at 1 in 100. A claim "
                "that began at 1 in 2 would stand at `81/82`.",
            ],
        },
        "quiz_title": "Witnesses and miracles",
        "quiz": [
            {"q": "A claim has prior 1/100. A witness who says yes with probability 9/10 if it is true and 1/10 if it is false says yes. What is the posterior?",
             "a": ["`9/10`", "`1/10`", "`1/12`", "`9/100`"],
             "c": 2,
             "why": "Prior odds of 1 to 99 times a factor of 9 are 9 to 99, a credence of `1/12`. The witness’s reliability `9/10` is not the posterior, `1/10` is her false-alarm rate, and `9/100` multiplies the prior by the factor without turning odds into a credence."},
            {"q": "Two independent witnesses each have a Bayes factor of 9 and both say yes. What is the factor for the pair?",
             "a": ["`81`", "`18`", "`9`", "`3`"],
             "c": 0,
             "why": "Independent likelihoods multiply: `(9/10)·(9/10)` over `(1/10)·(1/10)` is 81. Adding gives 18, which is not how likelihoods combine; `9` ignores the second witness and `3` takes a square root."},
            {"q": "Two newspapers print the same agency report. Why should their Bayes factors not be multiplied?",
             "a": ["Newspapers are never reliable enough to have a Bayes factor",
                   "Given the truth of the claim, the second report is not independent of the first, since both repeat one source",
                   "Bayes factors can be multiplied only for three or more witnesses",
                   "A printed report has no likelihood"],
             "c": 1,
             "why": "Multiplication needs independence given the truth. Two copies of one report are the same witness twice, and the second adds no new factor. A printed report has a likelihood like any other, and the number of sources does not matter beyond that."},
            {"q": "With prior 1/1,000,000 and one witness at 999 in 1,000, the lab gives `1/1002`. What does Hume’s comparison say about this?",
             "a": ["No testimony could ever establish a miracle",
                   "The miracle is now more probable than not",
                   "The witness must be unreliable",
                   "A mistaken report is about a thousand times more probable than the event, so the report leaves it improbable"],
             "c": 3,
             "why": "The two weights are in the ratio 1,001 to 1, so the event is improbable though not impossible. Nothing in the comparison forbids more or better witnesses, the posterior is far below one half, and the witness’s reliability is an input the example granted."},
        ],
        "mistakes": [
            ("Thinking a 90% reliable witness makes the claim 90% likely",
             "Her reliability is `P(yes | true)`, and what is wanted is `P(true | yes)`. For a claim at `1/100` the posterior after her yes is `1/12`: nine true yeses for every ninety-nine false alarms. The reliability only becomes the posterior when the prior is even odds."),
            ("Multiplying the factors of witnesses who share a source",
             "Two witnesses who read the same notice are one witness. The lab multiplies the factors because it is told the witnesses are independent, and a lesson that finds `9/20` for two witnesses has assumed it. If the second witness only repeats the first, the posterior stays at `1/12`."),
            ("Reading Hume as saying that no testimony could support a miracle",
             "The comparison is between the odds against the event and the factor the testimony supplies. One witness at 999 in 1,000 falls short for an event at 1 in a million, and three independent ones do not. The argument sets a bar and invites the reader to ask whether the evidence clears it."),
        ],
        "standard": (
            "Finish when you can say what a witness is worth in a number.",
            "You should be able to turn a stated reliability into two likelihoods and a Bayes factor, update a prior on one or several independent witnesses, and state Hume’s argument as a comparison of two weights, saying which premises it depends on."),
        "note": "A symmetric reliability is the simplest case. Real witnesses are more likely to say yes when the claim is true than to say no when it is false, or the reverse; the lab takes any pair of likelihoods you type.",
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "reference-classes-and-statistical-evidence",
        "title": "Reference Classes and Statistical Evidence",
        "module": "Evidence and belief",
        "one_line": "Why the probability for an individual depends on the group the individual is placed in.",
        "summary": (
            "A statistic is a rate in a group, and it reaches an individual only "
            "through the group chosen. A person belongs to many groups with "
            "different rates, and a pooled rate is the rate of one more group. The "
            "lab prints the rate in each class and in their union from the same counts."
        ),
        "key": [
            "a rate belongs to a class, not a person",
            "one person sits in many classes",
            "pooled rate: add the counts, then divide",
            "the lab divides; the class is chosen",
        ],
        "key_label": "Whose rate is it",
        "concepts_intro": (
            "Evidence about a population is used for an individual by reading "
            "the individual into a class. The step is easy to take without noticing."
        ),
        "concepts": [
            ("A reference class is the group whose rate is used",
             "To say that a person’s chance of an outcome is 1 in 5 is to say that "
             "1 in 5 in some group the person belongs to has the outcome."),
            ("An individual belongs to many classes",
             "Smokers, cyclists, people of sixty, smokers who cycle: each has its own "
             "rate, and the data do not choose among them."),
            ("A pooled rate is a rate for a class too",
             "Adding the counts of two groups gives the rate of their union. It "
             "depends on how many are in each group, and it is the answer to a "
             "question about the union."),
        ],
        "read_title": "A smoker who cycles",
        "read_intro": "One person, several rates, and counts that make each of them exact.",
        "body": [
            ("p", "A man of sixty smokes and cycles daily. Asked how likely he is "
                  "to die of heart disease before seventy-five, a doctor can "
                  "consult tables. The counts below are invented, so that every rate "
                  "is a clean fraction."),
            ("math", [
                "class                    died    total    rate",
                "---------------------------------------------",
                "smokers                   200     1000    1/5",
                "  who cycle                 5      100    1/20",
                "  who do not              195      900    13/60",
                "non-smokers                30     1000    3/100",
                "  who cycle                 6      400    3/200",
                "  who do not               24      600    1/25",
            ]),
            ("p", "He is a smoker, so `1/5` applies. He is a smoker who cycles, so "
                  "`1/20` applies. He is a person who cycles, a person of sixty, "
                  "a person who lives in his city, and each of those has a rate of "
                  "its own. All of these are statements about groups he belongs to, "
                  "and the two rates above differ by a factor of four."),
            ("def", ("Reference class",
                     "A <strong>reference class</strong> is the group whose rate of an "
                     "outcome is taken as the probability of that outcome for one "
                     "case. The <strong>reference class problem</strong> is that a "
                     "case belongs to many such groups, with different rates, and "
                     "the counts do not say which to use.")),
            ("p", "A practical rule is to use the narrowest class that has enough "
                  "data. The lab shows the cost on both sides. The class of "
                  "smokers who cycle gives `1/20`, but it rests on 100 people and "
                  "5 deaths, and the lab, which treats counts as exact rates and "
                  "estimates nothing, cannot tell how far that figure can be "
                  "trusted. The class of smokers gives `1/5` on ten times as many "
                  "people and ignores the cycling."),
            ("h3", "The pooled rate"),
            ("p", "The rate for smokers, `1/5`, is the pooled rate of the two "
                  "groups beneath it: add the deaths, `5 + 195 = 200`, add the "
                  "totals, `100 + 900 = 1000`, and divide. It is not the average of "
                  "`1/20` and `13/60`, which would ignore that nine in ten smokers "
                  "here do not cycle. The pooled rate sits close to the "
                  "larger group’s rate because the larger group supplies most of "
                  "the counts."),
            ("p", "Nothing makes the pooled rate &ldquo;the&rdquo; probability. It "
                  "is the probability for a smoker chosen at random from this "
                  "population, which is the right answer to a question about "
                  "that, and the wrong one to a question about a man who cycles."),
            ("h3", "When the pooled rate points the wrong way"),
            ("p", "The effect can be larger than a difference in size. In a "
                  "well-known set of counts, two treatments for kidney stones are "
                  "compared by stone size. The open operation has a higher success "
                  "rate than the keyhole procedure for small stones, `81/87` against "
                  "`234/270`, and for large stones, `192/263` against `55/80`. "
                  "Pooled, it is `273/350` against `289/350`, and the keyhole "
                  "procedure is ahead."),
            ("p", "A patient with a large stone asks which treatment to choose. The "
                  "pooled figures answer a question about patients whose stones "
                  "might be of either size, and he is not one of them. The reason "
                  "the pooled comparison reverses, which is that the two "
                  "treatments were given to different mixes of patients, belongs "
                  "to Science, Induction and Causation, where it is called "
                  "Simpson’s paradox; here it only shows that the choice of class "
                  "can change which treatment looks better."),
            ("p", "A rate in a class is a conditional credence given membership, "
                  "in the sense of the earlier lesson. Learning that he also has a "
                  "family history puts him in a narrower class and changes the "
                  "number again. The probability for an individual is relative to "
                  "what is known about him, and the lab only divides."),
        ],
        "lab": ("choicekit", {
            "mode": "simpson",
            "preset": "smoker-cyclist",
            "weight": "pooled",
            "presets": [
                {"id": "smoker-cyclist", "label": "smokers and non-smokers, split by cycling",
                 "names": ["smokers", "non-smokers"],
                 "groups": [
                     {"name": "cyclists", "a": [5, 100], "b": [6, 400]},
                     {"name": "non-cyclists", "a": [195, 900], "b": [24, 600]},
                 ],
                 "expect": {"siPooled": "smokers 200/1000 vs non-smokers 30/1000: smokers higher", "siGroup1": "smokers higher", "siGroup2": "smokers higher"}},
                {"id": "kidney", "label": "kidney stones, split by size",
                 "names": ["open", "keyhole"],
                 "groups": [
                     {"name": "small stones", "a": [81, 87], "b": [234, 270]},
                     {"name": "large stones", "a": [192, 263], "b": [55, 80]},
                 ],
                 "expect": {"siPooled": "open 273/350 vs keyhole 289/350: keyhole higher", "siGroup1": "open higher", "siGroup2": "open higher"}},
            ],
            "panel_title": "Change the counts and compare the classes",
            "panel_intro": "Counts read successes over trials, for each treatment in each group. The first example reads deaths over people for smokers and non-smokers, split by cycling; the pooled line adds the groups. Change one count and see which of the three comparisons moves. The Verdict tile reads Reversal when the pooled comparison disagrees with both groups, as it does for the kidney stones; the Adjusted tile and the standardised weighting are tools of Science, Induction and Causation and can be left alone here.",
        }),
        "steps_title": "From counts to a rate for one person",
        "steps_intro": "The order that makes the choice of class visible.",
        "steps": [
            ("List the classes the person belongs to",
             "Everything you know about him that you have a count for. Each is "
             "a candidate."),
            ("Write each rate as a fraction",
             "Cases with the outcome over cases in the class. Keep the counts "
             "beside the fraction so you can see how much data each rests on."),
            ("Pool by adding counts",
             "To combine two classes, add numerators and denominators. Averaging the "
             "rates gives the wrong answer unless the classes are the same size."),
            ("Compare the classes",
             "If the rates differ, the data have not chosen between them. Say what "
             "reason you have for the one you use."),
            ("State the class with the rate",
             "&ldquo;1 in 20 of smokers who cycle&rdquo;, not &ldquo;his chance is 1 "
             "in 20&rdquo;. The sentence should carry its class."),
        ],
        "worked": {
            "title": "A smoker who cycles",
            "intro": ["From the counts above, the rates that apply to him."],
            "lines": [
                "smokers who cycle:      5 / 100   = 1/20",
                "smokers who do not:   195 / 900   = 13/60",
                "all smokers (pooled): 200 / 1000  = 1/5",
                "non-smokers (pooled):  30 / 1000  = 3/100",
                "his classes give:       1/20  and  1/5",
            ],
            "after": [
                "Two of these rates are about classes he is in, and they differ "
                "by a factor of four. The pooled `1/5` is not wrong; it is the rate "
                "for smokers whether or not they cycle, and he is a smoker who "
                "does.",
            ],
        },
        "quiz_title": "Which class, and what rate",
        "quiz": [
            {"q": "A man is a smoker who cycles. The lab prints 1/5 for smokers and 1/20 for smokers who cycle. Which is his probability?",
             "a": ["`1/5`, because it rests on ten times as many people",
                   "`1/20`, because the narrowest class is always right",
                   "Neither is forced by the data; each is the rate of a class he belongs to, and the choice needs a reason",
                   "The average of the two"],
             "c": 2,
             "why": "Both classes contain him, and the counts alone do not rank them. More data and a closer match pull in different directions here. A rule such as the narrowest class with enough data can be defended but is not a theorem, and an average is the rate of no class."},
            {"q": "Smokers who cycle: 5 in 100. Smokers who do not: 195 in 900. What is the pooled rate for smokers?",
             "a": ["`2/15`, the average of `1/20` and `13/60`",
                   "`13/60`, the larger rate",
                   "`1/20`, the smaller rate",
                   "`1/5`, found by adding the counts and dividing"],
             "c": 3,
             "why": "The pooled rate adds the deaths, 200, and the people, 1,000. The average `2/15` gives the two groups equal weight although one is nine times the size. Either extreme ignores one of the groups."},
            {"q": "Why does the pooled rate for smokers, `1/5`, lie nearer `13/60` than `1/20`?",
             "a": ["Nine in ten smokers here do not cycle, so that group supplies most of the counts",
                   "Because a pooled rate always equals the larger of the two rates",
                   "Because cycling has no effect on the outcome",
                   "Because the lab weights the groups equally"],
             "c": 0,
             "why": "A pooled rate is weighted by group size. It need not equal the larger rate, and it would not here if the groups were reversed; nothing says cycling is inert, since it is what makes the rates differ, and the lab adds counts rather than weighting groups equally."},
            {"q": "The open operation is ahead of the keyhole procedure for small stones, `81/87` against `234/270`, and for large stones, `192/263` against `55/80`, but behind pooled. For a patient known to have a large stone, which comparison answers his question?",
             "a": ["The pooled one, since it uses all 350 patients of each treatment",
                   "The large-stone one, since his stone size is known and the pooled one mixes in cases unlike his",
                   "Neither, since rates cannot apply to an individual",
                   "The average of the pooled and the large-stone rates"],
             "c": 1,
             "why": "The pooled class contains patients with small stones, which he is not. The comparison for his own stone size is the better-matched class; it is not the only possible one, but it is the one the data support for him. The statement that rates cannot apply at all would rule out all evidence, and an average is the rate of no class."},
        ],
        "mistakes": [
            ("Treating the pooled rate as the probability",
             "The pooled rate for smokers is `1/5` and it is a true statement about the 1,000 of them. It is the rate for a smoker whose cycling is unknown. For this man, whose cycling is known, the class that counts it gives `1/20`, and the pooled figure would be the natural one only for someone about whom nothing else is known."),
            ("Averaging two rates instead of adding counts",
             "The two groups of smokers have 100 and 900 people. The average of their rates, `2/15`, weights them equally and describes no class. Adding the counts gives `1/5`, and changing a group’s size changes it."),
            ("Thinking the data can choose the class",
             "The counts print a rate for each class and are silent on which class is the right one. Choosing is a judgement about relevance, about how much data each class has, and about what else is known about the case. A lab or a table of statistics can compute any of them and cannot say which to use."),
        ],
        "standard": (
            "Finish when you can say which class each rate is a rate of.",
            "You should be able to compute the rate of an outcome in two classes and in their union from counts, say why the pooled rate is not the average of the rates, and state for a given individual which classes apply and why the figure for one differs from the figure for another."),
        "note": "All counts here are exact and no estimate is attempted. Deciding how far a rate from a small class can be trusted is a question for statistics, which this course does not cover.",
    },
    # ---------------------------------------------------------------- 11
    {
        "slug": "the-lottery-paradox",
        "title": "The Lottery Paradox",
        "module": "Evidence and belief",
        "one_line": "A belief threshold that accepts every ticket’s losing, and a lottery with a winner.",
        "summary": (
            "If to believe a claim is to give it a credence at or above a "
            "threshold, then in a fair lottery with enough tickets you believe of "
            "each ticket that it loses. The claims cannot all be true, because one "
            "ticket wins. Belief at a threshold is therefore not closed under "
            "conjunction, and raising the threshold does not help."
        ),
        "key": [
            "n tickets, one winner: P(loses) = 1 − 1/n",
            "accept a claim when its P is at least t",
            "all n accepted: they cannot all be true",
            "belief at a threshold is not closed under ∧",
        ],
        "key_label": "Each ticket loses; one wins",
        "concepts_intro": (
            "The credences in a lottery are perfectly coherent. The trouble is "
            "what happens when belief is read off credences by a threshold."
        ),
        "concepts": [
            ("A threshold turns credence into acceptance",
             "Accept a claim when its credence is at least some t below 1. The "
             "rule is simple and has many defenders."),
            ("Closure under conjunction is a second principle",
             "If you accept A and accept B, you accept A and B. It is what lets a "
             "reasoner put premises together."),
            ("The two cannot both hold in a lottery",
             "Accepting each claim that a ticket loses and accepting their "
             "conjunction would be accepting that no ticket wins, which is "
             "impossible."),
        ],
        "read_title": "A hundred tickets, one winner",
        "read_intro": "A threshold, a lottery, and the set of claims it accepts.",
        "body": [
            ("p", "A fair lottery sells 100 tickets and draws one winner. For each "
                  "ticket there is a claim, <em>this ticket loses</em>. Every one of "
                  "those claims has credence `99/100`: 99 of the 100 equally likely "
                  "outcomes make it true."),
            ("def", ("Threshold rule",
                     "To <strong>accept</strong> a claim at threshold `t` is for "
                     "its credence to be at least `t`, where `t` is below 1. A "
                     "reasoner who believes what she accepts has the whole set of "
                     "accepted claims as her beliefs.")),
            ("p", "Set `t = 99/100`. Each of the 100 claims has credence exactly "
                  "`99/100`, so each is accepted, and the lab reports 100 of 100. "
                  "Now put the claims together."),
            ("ol", [
                "Each claim &ldquo;ticket i loses&rdquo; has credence `99/100`, "
                "so by the threshold it is accepted.",
                "The lottery has a winner, so not every ticket loses: some "
                "claim &ldquo;ticket i loses&rdquo; is false.",
                "So the 100 accepted claims cannot all be true, and their "
                "conjunction, which says that every ticket loses, has probability 0.",
            ]),
            ("p", "The lab reports the accepted set as inconsistent and the "
                  "probability that all the accepted claims are true as 0. No "
                  "ticket survives, because it would have to be the winner and "
                  "then the claim about it would be false. This is the "
                  "<strong>lottery paradox</strong>."),
            ("p", "Two principles are in play, and one fact. The principles: "
                  "accept a claim when it is probable enough, and accept the "
                  "conjunction of what you accept. The fact: the lottery has a "
                  "winner. With 100 tickets at threshold `99/100` the three cannot "
                  "stand together, and since the fact is not negotiable, the exits "
                  "are ways of giving up a principle or restricting it."),
            ("ul", [
                "<strong>Give up the threshold rule.</strong> Belief is more than "
                "high credence, and no credence short of 1 makes it rational to "
                "believe that this ticket loses.",
                "<strong>Keep the threshold and give up closure.</strong> One may "
                "rationally accept each claim and not their conjunction, so "
                "belief is not closed under <em>and</em>; the price is holding a "
                "set of beliefs one knows are not all true.",
                "<strong>Restrict the threshold rule.</strong> Statistical "
                "evidence alone, however strong, is not the kind that supports "
                "belief, so &ldquo;ticket i loses&rdquo; is never accepted. This "
                "keeps the threshold for evidence of other kinds and owes an "
                "account of the difference.",
            ]),
            ("p", "Each exit is a position with defenders, and each has a price. The "
                  "first needs a theory of what belief is, the second gives up "
                  "an inference used whenever premises are combined, and the third "
                  "leaves open why the same worry does not arise for a claim "
                  "supported by an ordinary statistic."),
            ("h3", "A higher threshold does not help"),
            ("p", "Raise the threshold to `999/1000`. With 100 tickets each claim "
                  "has credence `99/100`, which is below it, so nothing is accepted "
                  "and the paradox is gone. But the paradox returns with 1,000 "
                  "tickets: each claim now has credence `999/1000`, all are "
                  "accepted, and the conjunction is again impossible."),
            ("p", "For any threshold below 1 there is a lottery large enough to "
                  "reach it, so no threshold avoids the problem. Setting the "
                  "threshold at 1 avoids it by accepting only what is certain, which "
                  "is a different and much narrower account of belief."),
            ("p", "The credences here are coherent in the sense of the earlier "
                  "lesson on the Dutch book: they add up correctly and no book "
                  "exists. The incoherence appears only in the acceptances, and "
                  "the lab can show that and cannot say which exit to take."),
        ],
        "lab": ("choicekit", {
            "mode": "credence",
            "preset": "hundred",
            "presets": [
                {"id": "hundred", "label": "100 tickets, threshold 99/100", "kind": "lottery",
                 "n": 100, "threshold": "99/100",
                 "expect": {"crAccepted": "100 of 100", "crConsistent": "Inconsistent", "crPAll": "0"}},
                {"id": "thousand", "label": "1,000 tickets, threshold 999/1000", "kind": "lottery",
                 "n": 1000, "threshold": "999/1000",
                 "expect": {"crAccepted": "1000 of 1000", "crConsistent": "Inconsistent", "crPAll": "0"}},
                {"id": "strict", "label": "100 tickets, threshold 999/1000", "kind": "lottery",
                 "n": 100, "threshold": "999/1000",
                 "expect": {"crAccepted": "0 of 100", "crConsistent": "Consistent", "crPAll": "1"}},
            ],
            "panel_title": "Change the number of tickets or the threshold",
            "panel_intro": "Move the number of tickets and the threshold together. Find the smallest lottery for which a threshold of 99/100 accepts everything, then do the same for 9/10.",
        }),
        "steps_title": "Running the paradox",
        "steps_intro": "From a fair lottery to the failure of closure.",
        "steps": [
            ("Compute the credence of each claim",
             "In a fair lottery of n tickets, the claim that ticket i loses has "
             "credence `1 − 1/n`."),
            ("Apply the threshold",
             "Accept the claim when its credence is at least `t`. All n claims "
             "share one credence, so all are accepted or none are."),
            ("Form the conjunction",
             "If all n are accepted, their conjunction says that no ticket wins."),
            ("Compare the conjunction with the facts",
             "The lottery has exactly one winner, so the conjunction has "
             "probability 0 and the accepted set has no model."),
            ("Name the exit",
             "Reject the threshold rule, reject closure under conjunction, or "
             "restrict the threshold so that statistical evidence alone accepts "
             "nothing, and say what each costs."),
        ],
        "worked": {
            "title": "100 tickets at threshold 99/100",
            "intro": ["One ticket wins, drawn at random."],
            "lines": [
                "credence in each ‘ticket i loses’:  99/100",
                "threshold:                          99/100",
                "claims accepted:                    100 of 100",
                "conjunction (every ticket loses):   probability 0",
                "accepted set:                       inconsistent",
            ],
            "after": [
                "Each acceptance is reasonable on its own terms, and the set of all "
                "of them cannot be true. If belief is closed under conjunction, "
                "one of the steps must go.",
            ],
        },
        "quiz_title": "Tickets, thresholds and conjunctions",
        "quiz": [
            {"q": "A fair lottery has 100 tickets and the threshold is 99/100. How many of the claims “ticket i loses” are accepted?",
             "a": ["`99`", "`100`", "`1`", "`0`"],
             "c": 1,
             "why": "Each claim has credence exactly `99/100`, which meets the threshold, so all 100 are accepted. `99` would be the number of losing tickets, which is a different count; `1` and `0` would need the threshold to be higher."},
            {"q": "What is the probability that all the accepted claims are true together?",
             "a": ["`0`", "`99/100`", "`1/100`", "The product of one hundred factors of `99/100`"],
             "c": 0,
             "why": "All true would mean every ticket loses, and one wins. The product of 100 factors of `99/100` is the preface calculation, which treats the claims as independent; here they are tied together by the winner. `99/100` and `1/100` are single-ticket figures."},
            {"q": "Raising the threshold to 999/1000 is proposed as a cure. What does the lab show?",
             "a": ["It cures the paradox for every lottery, since 999/1000 is nearly 1",
                   "It cures it for 100 tickets, so the paradox is permanently gone",
                   "It accepts nothing for 100 tickets, but accepts all 1,000 tickets of a 1,000-ticket lottery, and the contradiction returns",
                   "It leaves the accepted set consistent by making the conjunction probable"],
             "c": 2,
             "why": "Any threshold below 1 is met by a large enough lottery. A cure for 100 tickets is not a cure for 1,000, and the conjunction of all the claims is impossible however large the lottery, so it never becomes probable."},
            {"q": "Which reply keeps the threshold rule and gives up something else?",
             "a": ["Deny that the lottery is fair",
                   "Deny that credences are additive",
                   "Deny that exactly one ticket wins",
                   "Deny that belief is closed under conjunction"],
             "c": 3,
             "why": "Accepting each claim and not the conjunction keeps the threshold and gives up closure. Denying fairness or the single winner changes the example rather than answering it, and the credences are additive, as in the Dutch-book lesson."},
        ],
        "mistakes": [
            ("Assuming rational belief is closed under conjunction",
             "It seems obvious that someone who believes A and believes B should believe both together. In the lottery that principle, with the threshold rule, makes a person believe that no ticket wins while knowing that one does. Either the principle or the threshold has to give, and the lab cannot say which."),
            ("Thinking a bigger threshold fixes it",
             "At `999/1000` the 100-ticket lottery accepts nothing, and the 1,000-ticket lottery accepts everything and fails again. A threshold below 1 is always reached by a large enough lottery, so it only moves the example."),
            ("Concluding that the credences are incoherent",
             "The credences are `99/100` for each of 100 losing claims and `1/100` for each ticket winning, and they obey every rule of the earlier lesson. The failure is in moving from credence to belief, not in the credences."),
        ],
        "standard": (
            "Finish when you can show that the accepted set has no model.",
            "You should be able to apply a threshold to every claim in a fair lottery, state how many are accepted, show that their conjunction has probability 0, and say which principle a given reply gives up or restricts."),
        "note": "The paradox is about belief, not about lotteries. Any claim supported by a large enough statistical base can play the role of a ticket.",
    },
    # ---------------------------------------------------------------- 12
    {
        "slug": "the-preface-paradox",
        "title": "The Preface Paradox",
        "module": "Evidence and belief",
        "one_line": "A hundred well-supported claims that could all be true, and probably are not.",
        "summary": (
            "An author believes each sentence of a book and writes in the preface "
            "that errors remain. With claims independent and each at 99 in 100, a "
            "threshold accepts every one, the accepted set is consistent, and the "
            "probability that all are true is about 0.37. Closure under "
            "conjunction fails here by probability, not by logic."
        ),
        "key": [
            "100 claims, each at 99/100, all accepted",
            "they can all be true: the set is consistent",
            "P(all true) is the product: about 0.37",
            "believe each, doubt the whole",
        ],
        "key_label": "A careful book, an honest preface",
        "concepts_intro": (
            "The lottery paradox fails by logic: one claim is certainly false. "
            "The preface fails more quietly, and the difference is the lesson."
        ),
        "concepts": [
            ("Independent claims multiply",
             "If the claims are independent, the probability that all are true is "
             "the product of their probabilities. A hundred factors of 99/100 "
             "multiply to far less than any one of them."),
            ("Consistent is not probable",
             "A set of claims can all be true without it being likely that they "
             "are. Consistency is a matter of logic and probability of how "
             "much risk accumulates."),
            ("Risk accumulates with length",
             "Each claim added to a book, or each premise added to an argument, "
             "adds a little chance of error, and the little chances add up."),
        ],
        "read_title": "Believe each sentence, doubt the book",
        "read_intro": "A threshold, a hundred independent claims, and what the product says.",
        "body": [
            ("p", "An author has checked a hundred claims for a book. Each is "
                  "supported strongly enough to have credence `99/100`, and the "
                  "checks are independent: an error in one tells her nothing about "
                  "another. At a threshold of `95/100` she accepts every claim, and "
                  "the lab reports 100 of 100."),
            ("p", "Unlike the lottery, nothing logical ties the claims together. "
                  "They could all be true, and the lab reports the accepted set as "
                  "consistent. The question is how likely that is."),
            ("def", ("Independent claims",
                     "Claims are <strong>independent</strong> when the probability "
                     "of two of them together is the product of their separate "
                     "probabilities, and likewise for any number. For `n` claims "
                     "each at probability `p`, the probability that all are true "
                     "is `p` multiplied by itself `n` times.")),
            ("math", [
                "P(all 100 true) = (99/100)¹⁰⁰, about 0.37",
            ]),
            ("p", "The lab prints the exact fraction. The conjunction of the "
                  "hundred claims is true with probability about 0.37, well under "
                  "the threshold of `95/100`, so she does not accept it. She "
                  "accepts every claim, and she does not accept the claim that "
                  "all of them are true. That is the <strong>preface "
                  "paradox</strong>: she may write that she is confident of each "
                  "sentence and that some error remains."),
            ("p", "The two paradoxes differ in kind. In the lottery, closure under "
                  "conjunction fails because the conjunction is certainly false. "
                  "In the preface the conjunction is possible and merely improbable. "
                  "So the lottery shows that a threshold can accept an "
                  "inconsistent set, while the preface shows that it can accept a "
                  "consistent set whose conjunction it rejects."),
            ("h3", "Why it matters outside books"),
            ("p", "A valid argument preserves truth, not probability. If a "
                  "conclusion follows from a hundred premises, each at `99/100`, "
                  "and the premises are independent, the conclusion is at least as "
                  "probable as their conjunction, which is about 0.37. A long "
                  "chain of reasoning in which every step is believable can end in "
                  "a conclusion that is not. The principle that if you accept each "
                  "premise you accept the conclusion fails for exactly this reason."),
            ("p", "Shorten the book and the effect shrinks. Ten claims at `9/10` "
                  "give a conjunction of about 0.35, which the lab prints as "
                  "`3486784401/10000000000`: milder, but still far below the "
                  "claims it is made of. Only at certainty does it vanish: a "
                  "hundred claims at probability 1 have a conjunction of "
                  "probability 1. Closure under conjunction holds for what is "
                  "certain and is at risk for everything else."),
            ("p", "The lab assumes independence, and real claims in a book are "
                  "more often positively related, as when they rest on one source. "
                  "That raises the probability that all are true, but not "
                  "to 1, and the paradox remains for any set with enough independent "
                  "risk."),
        ],
        "lab": ("choicekit", {
            "mode": "credence",
            "preset": "book",
            "presets": [
                {"id": "book", "label": "100 claims at 99/100, threshold 95/100", "kind": "independent",
                 "n": 100, "p": "99/100", "threshold": "95/100",
                 "expect": {"crPAll": "36603234127322950493061602657251738618971207663892369140595737269931704475072474818719654351002695040066156910065284327471823569680179941585710535449170757427389035006098270837114978219916760849490001/100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000", "crConsistent": "Consistent", "crAccepted": "100 of 100"}},
                {"id": "short", "label": "10 claims at 9/10, threshold 4/5", "kind": "independent",
                 "n": 10, "p": "9/10", "threshold": "4/5",
                 "expect": {"crPAll": "3486784401/10000000000", "crConsistent": "Consistent", "crAccepted": "10 of 10"}},
                {"id": "certain", "label": "100 claims at 1, threshold 95/100", "kind": "independent",
                 "n": 100, "p": "1", "threshold": "95/100",
                 "expect": {"crPAll": "1", "crConsistent": "Consistent", "crAccepted": "100 of 100"}},
            ],
            "panel_title": "Change the number of claims, their probability or the threshold",
            "panel_intro": "Each claim has the probability in the second box and all are independent. Find how many claims at 99/100 it takes before the conjunction falls below one half.",
        }),
        "steps_title": "Running the preface",
        "steps_intro": "From independent claims to a rejected conjunction.",
        "steps": [
            ("State each claim’s probability",
             "All the claims are given the same probability here, and the claims "
             "are independent."),
            ("Apply the threshold",
             "Accept the claims whose probability is at least `t`. If one is accepted "
             "they all are."),
            ("Check consistency",
             "Nothing ties independent claims together, so they can all be true. "
             "The accepted set has a model."),
            ("Multiply for the conjunction",
             "The probability that all are true is the common probability multiplied by "
             "itself once for each claim. Compare it with `t`."),
            ("Say what is given up",
             "If the product is below `t`, the reasoner accepts every claim and "
             "not their conjunction, so closure fails without any inconsistency."),
        ],
        "worked": {
            "title": "A hundred claims at 99/100",
            "intro": ["Independent, with a threshold of 95/100."],
            "lines": [
                "each claim:                        99/100",
                "threshold:                         95/100",
                "claims accepted:                   100 of 100",
                "accepted set:                      consistent",
                "P(all true) = (99/100)¹⁰⁰:         about 0.37",
            ],
            "after": [
                "Nothing in the claims prevents all of them being true, and yet "
                "the conjunction is well below the threshold. Believing every "
                "sentence and doubting the book is not a contradiction.",
            ],
        },
        "quiz_title": "Products and conjunctions",
        "quiz": [
            {"q": "A hundred independent claims each have probability 99/100. What is the probability that all of them are true?",
             "a": ["`99/100`, the same as each claim",
                   "`0`, as in the lottery",
                   "`(99/100)¹⁰⁰`, about 0.37",
                   "`1/100`"],
             "c": 2,
             "why": "For independent claims the probability of all is the product, a hundred factors of `99/100`. It is not `99/100`, which would need the claims to be the same claim. It is not 0, since nothing excludes all of them being true, and `1/100` is the chance of one specific loss."},
            {"q": "How does the preface differ from the lottery?",
             "a": ["The preface has less probable claims",
                   "In the preface the accepted claims could all be true though they probably are not; in the lottery they cannot all be true",
                   "The preface has fewer claims",
                   "The lottery has no threshold"],
             "c": 1,
             "why": "The lottery set is inconsistent and the preface set is consistent with a low-probability conjunction. The preface claims are more probable, not less, the number of claims is not the difference, and both paradoxes use a threshold."},
            {"q": "The lab prints 1 for the conjunction of 100 claims each at probability 1. What does that show?",
             "a": ["Closure under conjunction cannot fail when every claim is certain; the paradox needs claims short of 1",
                   "The lab has divided incorrectly",
                   "Certain claims are always independent",
                   "The threshold rule is refuted"],
             "c": 0,
             "why": "A product of 1s is 1, so a conjunction of certainties is certain. The result is correct and says nothing about independence, and a threshold at 95/100 is satisfied at no cost to anyone."},
            {"q": "Which change lowers the probability that all the claims are true?",
             "a": ["Raising the threshold",
                   "Making each claim more probable",
                   "Removing some of the claims",
                   "Adding more claims at 99/100"],
             "c": 3,
             "why": "Each added claim multiplies the product by 99/100, which can only lower it. Raising the threshold changes what is accepted but not the product, and the other two changes raise it."},
        ],
        "mistakes": [
            ("Thinking an author who believes each sentence must believe the book has no errors",
             "Believing each claim at `99/100` is compatible with giving the conjunction credence about 0.37, because the probability of all of them is the product and not the common value. The preface states exactly that: no particular sentence is doubted, and the whole is expected to contain a mistake."),
            ("Treating the preface as the lottery again",
             "The lottery set is inconsistent, so one accepted claim is certainly false. The preface set is consistent, and every accepted claim might be true. They share a failure of closure and differ in why."),
            ("Dropping belief in each claim because the whole is doubtful",
             "The doubt about the book is a doubt about the conjunction. No sentence has become less probable, and withdrawing from every claim at `99/100` would give up a hundred well-supported beliefs to avoid an inconsistency the set does not contain."),
        ],
        "standard": (
            "Finish when you can say why the set is consistent and the conjunction is not accepted.",
            "You should be able to apply a threshold to independent claims, state that the accepted set has a model, compute the probability that all are true as a product, and contrast the failure of closure here with its failure in the lottery."),
        "note": "Whether the author should believe the book is error-free, doubt it, or suspend judgement is contested; the lab shows only that the three cannot all be derived from the threshold rule together.",
    },
]
