"""Dynamic Programming and Sequential Decisions -- the second half.

What information is worth before it is bought, two stopping problems whose
rules are measured rather than assumed, and the horizon with no last period,
where the fixed point is a linear system and value iteration is the slow way
round.

Every figure below is read off scripts/mathpath/labs/dpseq.py by executing its
shipped JavaScript blocks under node. Where a design note and the kit
disagreed, the kit won.
"""

LESSONS = [
    # ---------------------------------------------------------------- 06
    {
        "slug": "folding-a-decision-tree-back",
        "title": "Folding a Decision Tree Back",
        "module": "When the next step is uncertain",
        "one_line": "A chance node is an average and a decision node is a maximum; fold both back and the difference between them prices information before you buy it.",
        "summary": (
            "Put a payoff table beside a prior and the whole of a one-shot decision under "
            "uncertainty is a tree two levels deep. Folding it back is the recursion again, with "
            "two kinds of node instead of one. What the fold makes possible is a question the "
            "table alone cannot answer: what would it be worth to know the state before "
            "deciding, and what is this particular noisy signal worth? The first is a ceiling "
            "that no signal can exceed. The second can be exactly nothing, for a signal that "
            "looks perfectly respectable."
        ),
        "key": [
            "chance node   = the average of its branches, weighted by their probabilities",
            "decision node = the largest of its branches, and it records which one",
            "EVPI = E[ best act once the state is known ] - [ best act on the prior ]",
            "EVSI = E[ best act after seeing the signal ] - [ best act on the prior ]",
            "0 <= EVSI <= EVPI always, and both ends of that are reached in the lab",
            "go/stop, up/down, payoff 60 and -40, prior 1/2:  EVPI 20  and  EVSI 0",
        ],
        "key_label": "Two kinds of node, and the two prices that come out of them",
        "concepts_intro": (
            "Three ideas. The first is the fold, the second is the ceiling, and the third is the "
            "one that makes the ceiling worth having."
        ),
        "concepts": [
            ("The fold is the same recursion with two rules instead of one",
             "Work from the leaves back. A chance node takes the probability-weighted average of "
             "what its branches fold to; a decision node takes the largest, and remembers which "
             "branch that was. Nothing else changes: values are written only once everything "
             "below them is settled, and the tree is filled from the ends. The branch a decision "
             "node remembers is the plan, and the number it holds is not."),
            ("Perfect information is a ceiling, and it is computed differently",
             "Knowing the state before choosing lets you pick the best act in each state "
             "separately, so its value is `Σ P(state) × max over acts`. That has the maximum "
             "inside the average, which is the swap &ldquo;The Stochastic Recursion&rdquo; warned "
             "about &mdash; and "
             "here the swap is the point rather than a mistake, because it is describing a "
             "different and better-informed decision-maker. The difference between the two "
             "orders is `EVPI`, and no signal can be worth more."),
            ("A signal's value comes from the joint distribution, not from the shape of the tree",
             "`EVSI` is computed by finding, for each signal, how likely that signal is and what "
             "the posterior over states becomes; then taking the best act under each posterior; "
             "then averaging those over the signals. A tree with no likelihood in it has no "
             "`EVSI` at all, and the lab reports it as absent rather than producing a number "
             "from the branches &mdash; a shape can always be given a number, and that is "
             "precisely the danger."),
        ],
        "read_title": "Folding back, and then pricing what you did not know",
        "read_intro": "The two node rules, the two prices, and the signal that costs nothing to ignore.",
        "body": [
            ("def", ("A decision tree, and the two values around it",
                     "Given <strong>acts</strong> `a`, <strong>states</strong> `s`, a "
                     "<strong>payoff</strong> `π(a, s)` and a <strong>prior</strong> `p(s)`, the "
                     "<strong>prior value</strong> is `max over a of Σₛ p(s) π(a, s)` and the "
                     "<strong>perfect-information value</strong> is `Σₛ p(s) max over a of "
                     "π(a, s)`. Their difference is <strong>EVPI</strong>.",
                     "A <strong>signal</strong> is a likelihood `P(g | s)`. For each signal `g`, "
                     "`P(g) = Σₛ p(s) P(g | s)` and the posterior is `p(s) P(g | s) / P(g)`. The "
                     "<strong>value with the signal</strong> is `Σ_g P(g) max over a of Σₛ "
                     "posterior × π(a, s)`, and <strong>EVSI</strong> is that minus the prior "
                     "value.")),
            ("p", "The lab builds the tree from the payoff table rather than asking you to type "
                  "one, because typing a tree is harder than typing the thing a tree is drawn "
                  "from and the tree is not the model. With no signal it is one decision node "
                  "over a chance node per act. With a signal it is a chance node over the "
                  "signals, and inside each branch of it the same decision again, now over the "
                  "posterior."),
            ("h3", "A signal that tells you nothing"),
            ("math", [
                "acts   go  stop          states  up  down          prior  1/2  1/2",
                "",
                "   payoff        up    down              on the prior",
                "      go          60     -40             (1/2)(60) + (1/2)(-40)  =  10",
                "      stop         0       0                                        0",
                "",
                "   decide now                  best act go, worth  10",
                "   know the state first        (1/2)(60) + (1/2)(0)  =  30",
                "   EVPI                        30 - 10  =  20",
                "",
                "the signal:   P(g1 | up) = 1/2    P(g1 | down) = 1/2",
                "              P(g2 | up) = 1/2    P(g2 | down) = 1/2",
                "",
                "   P(g1) = (1/2)(1/2) + (1/2)(1/2) = 1/2      posterior  up 1/2  down 1/2",
                "   P(g2) = 1/2                                posterior  up 1/2  down 1/2",
                "",
                "   after g1 the best act is go, worth 10;  after g2, go, worth 10",
                "   with the signal  (1/2)(10) + (1/2)(10)  =  10",
                "   EVSI  =  10 - 10  =  0",
            ]),
            ("p", "Twenty and nothing. Perfect information here is worth 20, which is a great "
                  "deal against a decision currently worth 10, and this signal captures none of "
                  "it. The reason is visible in the likelihood: the two rows are identical, so "
                  "the signal is as likely in one state as in the other, the posterior comes out "
                  "equal to the prior, and no decision changes. A signal has to "
                  "<em>discriminate</em> to be worth anything, and looking informative is not "
                  "the same thing."),
            ("p", "The lab also enumerates strategies. A strategy here is a choice of act for each "
                  "signal, and the best it finds is worth 10, which is what the fold says. That "
                  "enumeration prices each "
                  "strategy straight from the joint distribution with no tree, no posterior and "
                  "no fold anywhere in it, so it is an independent witness rather than a "
                  "restatement."),
            ("h3", "A signal that is worth something, and how much"),
            ("example", ("Build or wait, with a survey you could buy",
                         "Payoffs: building returns 100 if things turn out good and loses 20 if "
                         "they do not; waiting returns nothing either way. The prior is 3/10 "
                         "good. So building is worth 16 on the prior, waiting 0, and the best "
                         "act is to build. Knowing the state first is worth 30, so EVPI is 14.",
                         "The survey is right four times in five when things are good and three "
                         "times in four when they are not. A favourable survey then has "
                         "probability 83/200 and leaves a posterior of 48/83 good, under which "
                         "building is worth 4100/83; an unfavourable one has probability 117/200 "
                         "and a posterior of 4/39 good, under which waiting at 0 beats building. "
                         "The whole thing is worth 41/2, so EVSI is 9/2 &mdash; which is 9/28 of "
                         "EVPI, and no more than EVPI, as it must be.")),
            ("p", "Notice what the survey buys. Without it you build whatever happens; with it "
                  "you build after a favourable reading and wait after an unfavourable one. A "
                  "signal is worth something exactly when it changes what you do, and 9/2 is the "
                  "price of that change. If both readings had left building as the best act, "
                  "`EVSI` would have been zero however sharply the posteriors moved &mdash; "
                  "which is a strange and useful fact, and it is why information has to be "
                  "priced against a decision and never in the abstract."),
            ("example", ("Three acts, three states, and the middling one",
                         "A payoff table with a cautious act paying 20 whatever happens, a "
                         "middle act paying 0, 40 and 45, and a bold one paying -30, 20 and 80, "
                         "against a prior of 1/4, 1/2, 1/4. On the prior the three are worth 20, "
                         "125/4 and 45/2, so the middle act wins. Perfect information is worth "
                         "45 and EVPI is 55/4.",
                         "With the signal the whole thing is worth 257/8, so EVSI is 7/8 "
                         "&mdash; a genuine but small fraction of a large EVPI. The signal is "
                         "informative and mostly fails to change the act: only the weaker of the "
                         "two readings moves the decision, and it moves it to the cautious act "
                         "rather than the bold one.")),
            ("h3", "What the tree left out"),
            ("p", "The payoffs are known exactly and are in one currency. The prior is known "
                  "exactly, which is the assumption a reader should be least comfortable with: "
                  "`EVSI` depends on it, and a prior that was really a guess produces a price "
                  "for information that is also a guess, stated to the last fraction. The "
                  "likelihood is known exactly too, which is to say somebody has measured how "
                  "often this signal is right in each state &mdash; and if they have not, the "
                  "number on the page is the value of an imagined instrument."),
            ("p", "And the objective is still the expectation. A payoff of `-40` with "
                  "probability one half sits in the average as comfortably as anything else, "
                  "which is fine if the decision is one of many and ruinous if it is not. "
                  "Nothing in the fold can raise that question; the fold will happily return a "
                  "precise expected value for a gamble nobody should take."),
        ],
        "lab": ("dpseq", {
            "mode": "tree",
            "preset": "useless",
            "panel_title": "Fold the tree, then price every strategy it could have chosen",
            "panel_intro": "The tree is built from the payoff table rather than typed, folded "
                           "back node by node, and then checked against every mapping from what "
                           "you see to what you do &mdash; each priced straight from the joint "
                           "distribution with no tree involved. The selector switches between "
                           "deciding on the prior and seeing the signal first. This example is "
                           "the one where perfect information is worth 20 and the signal is "
                           "worth exactly 0; the examples above it in the list are the ones "
                           "where a signal is worth something.",
        }),
        "steps_title": "Pricing information before buying it",
        "steps_intro": "Five steps, and the order matters: two of them are cheap and rule out the third entirely.",
        "steps": [
            ("Compute what each act is worth on the prior, and take the best",
             "One weighted average per act. This is what you would do knowing nothing more, and "
             "every price below is measured against it &mdash; so getting it wrong shifts both "
             "EVPI and EVSI by the same amount and neither looks odd."),
            ("Compute the perfect-information value, with the maximum inside",
             "For each state take the best act in that state, then average over the prior. It is "
             "the same numbers in the other order and it is never smaller. The difference is "
             "EVPI, and it is the ceiling."),
            ("Stop here if the signal costs more than EVPI",
             "No signal can be worth more than knowing the state outright. If the asking price "
             "is above EVPI the answer is no, and it took two weighted averages to find out. "
             "This is the cheapest useful thing on the page."),
            ("Otherwise work out each signal's probability and posterior",
             "`P(g) = Σₛ p(s) P(g|s)`, then the posterior by Bayes. Check that the posteriors "
             "are distributions before going on; the lab checks that each state's column of the "
             "likelihood sums to 1, because a column is a distribution over what you might see."),
            ("Take the best act under each posterior, average over the signals, subtract",
             "That is EVSI. Then ask the question the arithmetic cannot: does the best act "
             "actually differ between signals? If it does not, EVSI is zero no matter how "
             "sharply the posteriors moved, and the signal is not worth buying at any price."),
        ],
        "worked": {
            "title": "Three trees, three prices for information",
            "intro": [
                "The same procedure on three payoff tables. Only the last column differs in "
                "kind: one signal is worth a reasonable share of the ceiling, one a small share, "
                "and one nothing at all."
            ],
            "lines": [
                "                      build/wait        three acts        go/stop",
                "",
                "   best act on prior     build              medium            go",
                "   worth                    16               125/4            10",
                "   know the state first     30                  45            30",
                "   EVPI                     14                55/4            20",
                "   with the signal        41/2               257/8            10",
                "   EVSI                    9/2                 7/8             0",
                "   EVSI as a share        9/28                7/110            0",
                "",
                "THE ZERO, in full",
                "",
                "   likelihood     P(g | up)   P(g | down)",
                "      g1              1/2         1/2",
                "      g2              1/2         1/2",
                "",
                "   P(g1) = (1/2)(1/2) + (1/2)(1/2) = 1/2",
                "   posterior after g1:  up = (1/2)(1/2) / (1/2) = 1/2      the prior exactly",
                "   posterior after g2:  up = 1/2                          the prior exactly",
                "",
                "   both readings leave go as the best act, worth 10",
                "   with the signal 10,  without it 10,  EVSI 0",
                "   and EVPI is 20, so the ceiling is high and this signal reaches none of it",
                "",
                "   strategies priced from the joint distribution:  best 10, agrees",
            ],
            "after": [
                "The middle column is the one that repays a second look. EVPI is 55/4, which is "
                "large next to a decision worth 125/4, and the signal captures 7/8 of it "
                "&mdash; under a tenth. It is a perfectly informative signal in the ordinary "
                "sense: the posteriors move a long way. It is nearly worthless because the act "
                "it recommends is almost always the one you would have chosen anyway.",
                "For a rehearsal, take the build-or-wait instance and make the survey perfect "
                "&mdash; a likelihood of `1 0` in the first row and `0 1` in the second. EVSI "
                "should rise to exactly EVPI, 14, and not a fraction more. Then make it "
                "perfectly wrong, `0 1` and `1 0`, and predict the answer before running it: a "
                "signal that is always backwards is just as informative as one that is always "
                "right.",
                "The harder rehearsal: hold the likelihood fixed and move the prior. There is a "
                "prior at which building and waiting are equally good, and EVSI is largest "
                "somewhere near it. Find it, and then say in words why information is worth most "
                "when the decision is closest &mdash; and worth nothing when the decision is not "
                "in doubt, however uncertain the state is.",
            ],
        },
        "quiz_title": "Folding, ceilings and what a signal is worth",
        "quiz": [
            {"q": "How do the perfect-information value and the prior value differ as computations?",
             "a": ["They use different payoffs",
                   "One takes the maximum inside the average over states and the other takes it outside",
                   "One uses the prior and the other uses the posterior",
                   "They differ only by the cost of the information"],
             "c": 1,
             "why": "`Σₛ p(s) max_a π(a,s)` against `max_a Σₛ p(s) π(a,s)`. Same numbers, "
                    "different order, and the first is never smaller. That gap is EVPI, and it "
                    "is the same swap the stochastic recursion warns about &mdash; here it is "
                    "deliberate, because it describes someone who decides knowing the state."},
            {"q": "A signal's likelihood is the same in every state. What is EVSI?",
             "a": ["Equal to EVPI, since the signal is perfectly consistent",
                   "Exactly zero: the posterior equals the prior, so no decision changes",
                   "Half of EVPI",
                   "Undefined, because the posterior cannot be computed"],
             "c": 1,
             "why": "The posterior is computable and comes out exactly equal to the prior, so "
                    "every branch of the signal tree recommends the act you would have chosen "
                    "anyway. In the instance in the lab EVPI is 20 and EVSI is 0 &mdash; the "
                    "ceiling is high and this signal reaches none of it."},
            {"q": "A signal shifts the posterior a long way, and EVSI comes out as a tiny fraction of EVPI. Is that a contradiction?",
             "a": ["Yes: a large shift in the posterior must be worth something close to EVPI",
                   "Yes, unless the payoffs are negative somewhere",
                   "No: a signal is worth something only when it changes the act, and a posterior can move a great deal without crossing the point where the best act changes",
                   "No, because EVSI is measured in different units from EVPI"],
             "c": 2,
             "why": "The three-act instance is exactly this: EVPI is 55/4 and EVSI is 7/8, "
                    "because only one of the two readings moves the decision at all. "
                    "Information is priced against a decision, never in the abstract, which is "
                    "why the same signal can be valuable under one payoff table and worthless "
                    "under another."},
            {"q": "The lab is given a payoff table and a prior but no likelihood. What does it report for EVSI?",
             "a": ["Zero, since there is no signal",
                   "The same as EVPI",
                   "That it is not computed, because the shape of a tree cannot produce one",
                   "An estimate based on the spread of the payoffs"],
             "c": 2,
             "why": "EVSI needs the joint distribution of signals and states, and a tree drawn "
                    "without a likelihood contains no such thing. Reporting zero would be a "
                    "claim about a signal that does not exist, and inventing a number from the "
                    "branches would be worse &mdash; a shape can always be given a number."},
        ],
        "mistakes": [
            ("Treating EVPI as the value of the information you are being offered",
             "It is the value of being told the state outright, which nobody is offering. It is "
             "useful precisely because it is a ceiling: it costs two weighted averages and it "
             "can rule out a purchase without any Bayes at all. Quoting it as the worth of a "
             "survey overstates the case by whatever the survey's noise costs, which in the "
             "instance in the lab is all of it."),
            ("Judging a signal by how much it moves the posterior",
             "A signal is worth something when it changes the act. Those are different "
             "properties and the three-act instance separates them: the posteriors move "
             "substantially and EVSI is 7/8 against an EVPI of 55/4. Conversely, a signal that "
             "barely moves the posterior can be worth a great deal if the decision was finely "
             "balanced."),
            ("Quoting EVSI to the last fraction from a prior that was a guess",
             "Every number here is exact arithmetic on the inputs, and one of the inputs is "
             "usually somebody's judgement about how likely the states are. `9/2` is the value "
             "of the survey given that the prior is exactly 3/10; it is not the value of the "
             "survey. Move the prior in the lab and watch EVSI move with it, and quote the range "
             "rather than the point."),
        ],
        "standard": ("Finish when you can fold a two-level tree by hand, compute EVPI in two weighted averages, and say without computing anything whether a given signal can possibly be worth buying.",
                     "You should be able to apply the two node rules from the leaves back, "
                     "compute the prior value and the perfect-information value and know which "
                     "has the maximum on the inside, use EVPI as a ceiling before touching "
                     "Bayes, compute posteriors and EVSI when the ceiling does not settle it, "
                     "and explain why a signal that never changes the act is worth nothing "
                     "however sharp it looks."),
        "note": 'Both halves of the course so far have decided everything at once and then watched it play out. The next lesson, &ldquo;Thresholds and When to Stop Looking&rdquo;, is the first where the decision is repeated and the only question is when to stop: offers arrive one at a time, refusing one costs something, and the rule turns out to be a threshold that falls as the deadline nears. That the rule has that shape is usually asserted. On that page it is measured against every other rule there is.',
    },
    # ---------------------------------------------------------------- 07
    {
        "slug": "thresholds-and-when-to-stop-looking",
        "title": "Thresholds and When to Stop Looking",
        "module": "When to stop",
        "one_line": "The value of carrying on is a threshold, it falls as the deadline nears, and its shape is measured against all 512 accept-sets rather than assumed.",
        "summary": (
            "Offers arrive one per period, you may take one or wait, and waiting costs something "
            "and eventually runs out. The recursion is two lines and its answer has a shape: "
            "accept an offer exactly when it beats what carrying on is worth. That shape is "
            "almost always stated as though it were obvious. Here it is a measurement &mdash; "
            "every way of choosing which offers to accept in which period is enumerated and "
            "evaluated, and the winner is then tested for whether it is a threshold at all."
        ),
        "key": [
            "V(0) = 0,      V(t) = E[ max(x, V(t-1)) ] - c",
            "accept an offer exactly when it beats V(t-1), the value of carrying on",
            "offers 10, 20, 30 each with probability 1/3;  three periods;  a look costs 1",
            "thresholds  22 with three left,  19 with two,  0 with one",
            "the whole search is worth 71/3, and in the last period anything is taken",
            "512 accept-sets enumerated; the best of them IS a threshold rule, measured",
        ],
        "key_label": "One recursion, and the shape of its answer checked rather than assumed",
        "concepts_intro": (
            "Three ideas: what the state is, why the threshold falls, and what it takes to prove "
            "the rule has the shape the recursion assumed."
        ),
        "concepts": [
            ("The state is how many periods are left, and nothing else",
             "Not which offers have been seen, not their average, not how long you have been "
             "looking. Offers are independent draws from a known distribution, so the past is "
             "uninformative about the future and the only thing that matters is how many chances "
             "remain. That is the whole modelling content of the problem, and it is the "
             "assumption to interrogate first: it fails the moment offers are correlated or the "
             "distribution has to be learned."),
            ("The threshold is the value of carrying on, and it falls",
             "`V(t)` is what the whole remaining search is worth with `t` periods to go, and an "
             "offer should be taken exactly when it beats `V(t−1)` &mdash; what you would get by "
             "refusing. With fewer periods left there is less to wait for, so `V` is smaller and "
             "the bar is lower. In the final period the bar is zero: there is nothing to carry "
             "on to, so any offer at all is taken."),
            ("The claim that the best rule is a threshold is a claim about SHAPE",
             "The recursion assumes it by construction: it compares each offer against one "
             "number. But a rule could in principle accept an offer of 20 and refuse one of 30, "
             "and nothing in the recursion rules that out &mdash; it simply never considers it. "
             "So the lab enumerates every accept-set in every period, evaluates each resulting "
             "rule exactly, and then asks whether the winner has the property that accepting an "
             "offer implies accepting every larger one."),
        ],
        "read_title": "Two lines of recursion, and a shape that is measured",
        "read_intro": "The definition, the table it produces, and the enumeration that turns an assumption into a result.",
        "body": [
            ("def", ("The sell-or-wait problem",
                     "In each of `T` periods one offer arrives, drawn independently from a known "
                     "distribution over values. You may accept it and stop, or refuse it and "
                     "pay a <strong>search cost</strong> `c` to go on; a refused offer cannot be "
                     "recalled. If you refuse the last one you get nothing.",
                     "Let `V(t)` be the expected value of the whole remaining search with `t` "
                     "periods left, before the offer is seen. Then `V(0) = 0` and `V(t) = "
                     "E[max(x, V(t−1))] − c`. The optimal rule with `t` periods left is: accept "
                     "`x` if and only if `x > V(t−1)`.")),
            ("p", "The lab refuses a distribution whose probabilities do not sum to exactly 1, "
                  "rather than renormalising it &mdash; the same discipline as the transition "
                  "rows earlier on this course, and for the same reason. It also charges the "
                  "search cost at every period including the last, so `V(1)` is the mean of the "
                  "offers minus `c` rather than the mean."),
            ("math", [
                "offers  10, 20, 30  each with probability 1/3      c = 1      T = 3",
                "",
                "V(0) = 0",
                "",
                "V(1) = E[max(x, 0)] - 1                                threshold 0",
                "     = (10 + 20 + 30)/3 - 1  =  20 - 1  =  19          take anything",
                "",
                "V(2) = E[max(x, 19)] - 1                               threshold 19",
                "     = (19 + 20 + 30)/3 - 1  =  23 - 1  =  22          take 20 or 30",
                "",
                "V(3) = E[max(x, 22)] - 1                               threshold 22",
                "     = (22 + 22 + 30)/3 - 1  =  74/3 - 1  =  71/3      take 30 only",
                "",
                "so with three periods left the search is worth  71/3,  about 23.67",
            ]),
            ("p", "Read the accept-sets down the table. With three periods left only 30 is "
                  "taken; with two, 20 and 30; with one, everything. The rule tightens as you "
                  "look further ahead and relaxes as the deadline approaches, which is the "
                  "opposite of the way impatience usually feels and is exactly what the "
                  "arithmetic says: what you are comparing an offer against is the value of the "
                  "chances that remain, and there are fewer of them each period."),
            ("h3", "Proving the shape rather than assuming it"),
            ("p", "A rule, in full generality, is a choice of which offers to accept in each "
                  "period. With three distinct offer values and three periods that is nine "
                  "independent yes-or-no decisions, so 512 rules. The lab constructs all 512, "
                  "evaluates each of them exactly by working backwards over the distribution "
                  "&mdash; a computation that asks what <em>this</em> rule is worth rather than "
                  "what carrying on is worth &mdash; and reports the best."),
            ("p", "The best is worth 71/3, which is what the recursion said; its accept-sets are "
                  "exactly the ones the thresholds describe; and it passes the shape test, which "
                  "is that in every period, accepting an offer implies accepting every larger "
                  "one. So on this instance the threshold form is not an assumption that "
                  "happened to be convenient. It is a measured property of the winner of an "
                  "exhaustive search."),
            ("example", ("A rare high offer",
                         "Offers of 8, 14 and 40 with probabilities 3/5, 3/10 and 1/10, four "
                         "periods, a search cost of 1. The thresholds come out 399/25, 72/5, 12 "
                         "and 0, so with three or four periods left only the 40 is accepted "
                         "&mdash; even though it arrives one time in ten.",
                         "The whole search is worth 4341/250, about 17.36, against a mean offer "
                         "of 13. Almost all of that is the tenth that pays 40: with the same "
                         "shape of problem but the 40 removed the search is worth a little over "
                         "10. Waiting is worth doing here because of a tail, which is a real "
                         "feature of real searches and the reason an average is a poor summary "
                         "of one.")),
            ("example", ("Searching expensively",
                         "Two offers, 10 and 30, equally likely, four periods, and a look now "
                         "costs 5. The thresholds are 75/4, 35/2, 15 and 0, and the accept-set "
                         "is the same in every period but the last: take the 30, refuse the 10.",
                         "Compare that with the same offers at a cost of 1, where the thresholds "
                         "are 103/4, 47/2, 19 and 0. The expensive search is worth 155/8 and the "
                         "cheap one 215/8. At the high cost a second look adds 5/2, a third 5/4 and "
                         "a fourth only 5/8: the cost eats the option value, and the rule stops "
                         "changing long before the deadline does.")),
            ("h3", "What the model left out"),
            ("p", "Offers are independent draws from a distribution you already know, which "
                  "rules out the most interesting thing about real search: that the offers you "
                  "have seen tell you something about the ones to come. It also rules out "
                  "recall, since a refused offer is gone; rules out the offer arriving late or "
                  "not at all; and treats the search cost as the same in every period. The "
                  "recursion will produce a threshold for any of those situations if you hand it "
                  "this model, and the threshold will be exactly right for the wrong problem."),
            ("p", "One more, less obvious. The objective maximises the expected value of what "
                  "you end up with, so a rule that occasionally ends with nothing is penalised "
                  "only by the size of that nothing. In the instance here the optimal rule "
                  "refuses everything but 30 in the first period; if the deadline matters more "
                  "than the money, the rule you want is not this one, and no amount of exact "
                  "arithmetic on the expectation will say so."),
        ],
        "lab": ("dpseq", {
            "mode": "stopping",
            "preset": "three",
            "panel_title": "Set the offers and the search cost, and watch the rule change",
            "panel_intro": "The recursion gives one threshold per period and the plot draws them "
                           "against how many periods remain. Beside it, the shape is measured "
                           "rather than assumed: every possible accept-set in every period is "
                           "enumerated and each resulting rule evaluated exactly, and the winner "
                           "is tested for whether accepting an offer implies accepting every "
                           "larger one. Raise the search cost with the slider and watch the "
                           "thresholds flatten.",
        }),
        "steps_title": "Computing a stopping rule",
        "steps_intro": "Four steps, and the last of them is the one that separates a rule you can defend from a rule you have assumed.",
        "steps": [
            ("Start from the end: with nothing left, the search is worth nothing",
             "`V(0) = 0`. Everything else is built on that, and it is where the recursion bottoms "
             "out &mdash; the same role the last stage played on a network."),
            ("For each further period, average the better of the offer and carrying on",
             "`E[max(x, V(t−1))]`, which means replacing every offer below `V(t−1)` by `V(t−1)` "
             "itself and then averaging. Doing it that way rather than by cases makes the "
             "threshold visible in the arithmetic instead of implied by it."),
            ("Subtract the search cost, and record the threshold",
             "`V(t) = E[max(x, V(t−1))] − c`. The threshold with `t` periods left is `V(t−1)`, "
             "not `V(t)`: it is what you are giving up by accepting, not what the search is "
             "worth."),
            ("Read the accept-set in each period and check the direction",
             "Offers strictly above the threshold are accepted. The thresholds should fall as "
             "the deadline nears; if they do not, either the search cost is large enough that "
             "the rule barely moves, or something in the setup is wrong."),
            ("Enumerate every accept-set if the instance is small enough to allow it",
             "With `S` offer values and `T` periods there are `2^(S×T)` rules, which is 512 at "
             "three and three. Evaluating all of them and checking that the winner is a "
             "threshold rule turns the shape from an assumption into a measurement, and it is "
             "affordable exactly at the size a page can show."),
        ],
        "worked": {
            "title": "The recursion, and all 512 rules it never considered",
            "intro": [
                "Three offers, three periods, a search cost of 1. The recursion first, then the "
                "exhaustive search over every way of deciding which offers to accept when."
            ],
            "lines": [
                "offers 10, 20, 30 each 1/3        c = 1        T = 3",
                "",
                "THE RECURSION",
                "",
                "   periods left   threshold   accept        worth carrying on",
                "        1              0      10, 20, 30           19",
                "        2             19      20, 30               22",
                "        3             22      30                   71/3",
                "",
                "   V(1) = (10 + 20 + 30)/3 - 1 = 19",
                "   V(2) = (19 + 20 + 30)/3 - 1 = 22",
                "   V(3) = (22 + 22 + 30)/3 - 1 = 71/3",
                "",
                "EVERY RULE",
                "",
                "   3 offer values x 3 periods = 9 yes-or-no choices,  2^9 = 512 rules",
                "   each evaluated backwards over the distribution, asking what THAT rule",
                "   is worth rather than what carrying on is worth",
                "",
                "   best of the 512                             71/3",
                "   its accept-sets    3 left: 30    2 left: 20 30    1 left: 10 20 30",
                "   the threshold rule 3 left: 30    2 left: 20 30    1 left: 10 20 30",
                "   identical, set by set",
                "",
                "   is the winner a threshold rule?   yes",
                "      in every period, accepting an offer implies accepting every larger one",
            ],
            "after": [
                "The two accept-set rows being identical is a stronger statement than the two "
                "values being equal. A rule worth the same as the optimum would be enough to "
                "confirm the number; matching set by set says the recursion found the same rule "
                "and not merely an equally good one, which is what makes the shape test "
                "meaningful.",
                "For a rehearsal, set the search cost to 0 and recompute by hand. The thresholds "
                "become 0, 20 and 70/3, the whole search is worth 230/9, and with two periods "
                "left only the 30 is now accepted &mdash; a free look makes the rule fussier, "
                "not less. Then put the cost up to 6: the thresholds drop to 0, 14 and 46/3, "
                "and the 20 becomes acceptable again with two and with three left. So the "
                "accept-set with two periods left changes between a cost of 0 and a cost of 1, "
                "and confirming that is the exercise.",
                "The harder rehearsal: construct offers on which the best of all accept-sets is "
                "<em>not</em> a threshold rule. You will not manage it with independent draws "
                "and a constant cost &mdash; there is a proof that it cannot happen &mdash; and "
                "the useful part is working out which of those two conditions your attempted "
                "counterexample keeps breaking.",
            ],
        },
        "quiz_title": "Thresholds, deadlines and the shape of a rule",
        "quiz": [
            {"q": "Why is the threshold with `t` periods left equal to `V(t−1)` rather than `V(t)`?",
             "a": ["Because the search cost is charged in advance",
                   "Because the threshold is what you give up by accepting &mdash; the value of the search that remains after refusing",
                   "Because `V(t)` has not been computed yet",
                   "Because the offer in period `t` is already known"],
             "c": 1,
             "why": "Accepting ends the search; refusing leaves you with `t−1` periods, worth "
                    "`V(t−1)`. So the comparison is against `V(t−1)`, and `V(t)` is the value of "
                    "the whole situation including the offer you are about to see. Mixing them "
                    "up shifts every threshold by one period."},
            {"q": "The thresholds on the three-offer instance are 22, 19 and 0 as the deadline approaches. Why do they fall?",
             "a": ["Because the search cost accumulates",
                   "Because the offers get worse over time",
                   "Because there is less remaining search to give up, so the bar an offer must clear is lower",
                   "Because the distribution is uniform"],
             "c": 2,
             "why": "The threshold is the value of carrying on, and carrying on is worth less "
                    "when fewer chances remain. In the final period it is worth nothing at all, "
                    "so the threshold is 0 and any offer is taken &mdash; there is nothing left "
                    "to refuse in favour of."},
            {"q": "The lab enumerates 512 accept-sets. What does that establish that the recursion cannot?",
             "a": ["That the arithmetic in the recursion is right",
                   "That the optimal rule has the threshold shape the recursion assumed, rather than that shape being taken for granted",
                   "That the search cost is correctly charged",
                   "That the offers are independent"],
             "c": 1,
             "why": "The recursion compares each offer against a single number, so it can only "
                    "ever produce a threshold rule; it never considers accepting 20 and refusing "
                    "30. Enumerating every accept-set considers exactly those rules and finds "
                    "none of them better, and then checks that the winner has the implication "
                    "property."},
            {"q": "Offers of 8, 14 and 40 with probabilities 3/5, 3/10 and 1/10 over four periods make the search worth about 17.36, against a mean offer of 13. What is carrying that?",
             "a": ["The search cost being low",
                   "The tail: with three or four periods left only the 40 is accepted, and the option to keep waiting for it is most of the value",
                   "The fact that 14 is above the mean",
                   "The number of periods, since more periods always help by the same amount"],
             "c": 1,
             "why": "The thresholds are 399/25 and 72/5 with four and three periods left, both "
                    "above 14, so the rule holds out for the 40 that arrives one time in ten. "
                    "Remove the 40 and the same shape of search is worth a little over 10. An "
                    "average is a poor summary of a search precisely because of this."},
        ],
        "mistakes": [
            ("Comparing the offer against the wrong period's value",
             "Accepting ends the search and refusing leaves `t−1` periods, so the comparison is "
             "with `V(t−1)`. Using `V(t)` makes every threshold one period too high and produces "
             "a rule that refuses offers it should take, including in the final period &mdash; "
             "where the correct threshold is zero and the mistaken one is the mean minus the "
             "cost."),
            ("Expecting the threshold to rise as the deadline approaches",
             "Impatience suggests it should: you are running out of time, so surely you should "
             "get pickier. The arithmetic says the reverse, and the reason is that the threshold "
             "is not a measure of urgency but of what you are giving up. With one period left "
             "you are giving up nothing, so the bar is on the floor."),
            ("Treating the threshold form as something the recursion proved",
             "The recursion assumed it: it is built out of one comparison per period and cannot "
             "express any other kind of rule. What proves it on this page is the enumeration of "
             "all 512 accept-sets, which contains the non-threshold rules and finds them worse. "
             "That distinction is the lesson, and it disappears the moment the instance is too "
             "large to enumerate &mdash; at which point the shape is again an assumption, and "
             "should be named as one."),
        ],
        "standard": ("Finish when you can compute the thresholds for a three-period search by hand, say which offers are accepted in each period, and explain what an enumeration of accept-sets adds.",
                     "You should be able to write `V(t) = E[max(x, V(t−1))] − c`, compute it "
                     "period by period in exact fractions, identify the threshold as `V(t−1)` "
                     "rather than `V(t)`, explain why the thresholds fall as the deadline nears, "
                     "and say precisely what the recursion assumes about the shape of a rule and "
                     "how the page establishes it instead."),
        "note": 'Here the offers had values, and comparing one with a threshold was straightforward. The next lesson, &ldquo;The Secretary Problem, Exactly&rdquo;, removes the values: candidates arrive one at a time and all you ever learn is whether this one is the best so far. The rule that survives is a different shape &mdash; look at a fixed number and then take the next record &mdash; and its probability of success comes out of a harmonic sum rather than a recursion over values. It is also the one place on this course where a textbook reaches for an irrational number, and the page prints the exact table beside it.',
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "the-secretary-problem-exactly",
        "title": "The Secretary Problem, Exactly",
        "module": "When to stop",
        "one_line": "All you learn is whether this candidate is the best so far; the rule is to reject a fixed number and then take the next record, and its success probability is an exact fraction.",
        "summary": (
            "Candidates arrive one at a time in a random order and you can only ever compare "
            "them with the ones you have already seen. No values, no distribution, no second "
            "chances &mdash; and yet the chance of ending with the very best is nowhere near "
            "hopeless. The optimal rule rejects the first few whatever they are and then takes "
            "the first candidate better than all of them, and the probability it succeeds is a "
            "harmonic sum: an exact fraction, checked here by playing the rule out on every "
            "ordering there is."
        ),
        "key": [
            "you observe RANKS relative to what you have seen, never values",
            "reject the first r-1 whatever they are, then take the first record after them",
            "P(r) = ((r-1)/n) x sum of 1/(i-1) for i from r to n,    and P(1) = 1/n",
            "n = 4:  P = 1/4, 11/24, 5/12, 1/4     so reject 1, and win 11 times in 24",
            "checked by playing the rule out on all 24 orderings:  6, 11, 10, 6 wins",
            "n/e = 1.4715 here, and it is the LIMIT of the best r, rounded, not the answer",
        ],
        "key_label": "The rule, its exact probability, and the limit kept in its place",
        "concepts_intro": (
            "Three ideas: what you are allowed to observe, why the rule has the shape it has, and "
            "why the exact table matters more than the famous constant."
        ),
        "concepts": [
            ("The observation is a rank, not a value",
             "When candidate `k` arrives you learn only whether it is the best of the first `k`. "
             "That is a much weaker signal than a number, and it is what makes the problem "
             "interesting: you cannot ask whether this one is good enough, only whether it is "
             "the best so far. It also makes the answer independent of whatever distribution the "
             "qualities came from, which is the unusual and attractive part."),
            ("Rejecting a fixed prefix is the shape, and it comes from the same trade",
             "A candidate is worth taking only if it is a record, and a record early on is weak "
             "evidence &mdash; the best of three is often not the best of twenty. So the rule "
             "spends a prefix learning the standard and then takes the first candidate that "
             "beats it. Rejecting too few means stopping on a weak record; rejecting too many "
             "means the best one goes past unclaimed. `P(r)` is that trade written out."),
            ("An exact table, and a limit that is not the answer",
             "`P(r)` is a rational number for every `r`, so the whole table can be written in "
             "fractions and the best `r` read off it. The familiar `n/e` is the limiting "
             "position of that best `r` as `n` grows; at small `n` it is not even an integer, "
             "and this course has not built the asymptotics that make it a limit. So it appears "
             "on the page rounded and labelled, beside a table that never needed it."),
        ],
        "read_title": "One rule, one harmonic sum, and every ordering counted",
        "read_intro": "What the rule is, where its probability comes from, and the brute-force count that checks every entry.",
        "body": [
            ("def", ("The secretary problem and the look-then-leap rule",
                     "`n` candidates of distinct quality arrive one at a time in a uniformly "
                     "random order. On each arrival you learn only its rank among those seen so "
                     "far, and must accept or reject immediately; a rejection is final. You "
                     "succeed only by accepting the best of all `n`.",
                     "The <strong>look-then-leap rule with parameter `r`</strong> rejects "
                     "candidates 1 through `r−1` whatever they are, then accepts the first "
                     "candidate that is better than all of those &mdash; and accepts the last "
                     "candidate if it reaches it. `r = 1` means taking the first arrival.")),
            ("thm", ("The exact success probability",
                     "For `r ≥ 2`, the rule with parameter `r` succeeds with probability "
                     "`P(r) = ((r−1)/n) × Σ 1/(i−1)` summed over `i` from `r` to `n`. For "
                     "`r = 1` it is `1/n`.",
                     "The argument: the rule succeeds when the best candidate is in position "
                     "`i ≥ r` and the best of the first `i−1` lies in the rejected prefix. Those "
                     "are independent, with probabilities `1/n` and `(r−1)/(i−1)`. Summing over "
                     "`i` gives the formula, and every term is rational.")),
            ("p", "The lab computes that sum as a difference of two harmonic numbers, exactly, "
                  "in whole-number numerators and denominators. So the table it prints is a "
                  "table of fractions rather than decimals, and the best `r` is whichever row "
                  "holds the largest of them &mdash; a comparison between rationals, with no "
                  "rounding anywhere in it."),
            ("math", [
                "n = 4,   sum over i from r to 4 of 1/(i-1)",
                "",
                "   r = 1     P = 1/4                                       = 0.250000",
                "   r = 2     P = (1/4)(1/1 + 1/2 + 1/3) = (1/4)(11/6)      = 11/24",
                "                                                           = 0.458333",
                "   r = 3     P = (2/4)(1/2 + 1/3)       = (1/2)(5/6)       = 5/12",
                "                                                           = 0.416667",
                "   r = 4     P = (3/4)(1/3)                                = 1/4",
                "                                                           = 0.250000",
                "",
                "   the best r is 2:  reject 1 candidate, then take the next record",
                "",
                "checked by playing the rule out on all 4! = 24 orderings:",
                "",
                "   r = 1    wins  6 of 24   = 1/4        the same",
                "   r = 2    wins 11 of 24   = 11/24      the same",
                "   r = 3    wins 10 of 24   = 5/12       the same",
                "   r = 4    wins  6 of 24   = 1/4        the same",
                "",
                "   n/e = 1.4715, rounded -- the LIMIT of the best r, not the best r",
            ]),
            ("p", "Four candidates and a success rate of 11 in 24, which is a little over 45 per "
                  "cent, from a rule that throws the first candidate away unseen. That is the "
                  "surprise the problem is famous for, and at `n = 4` you can verify it by hand: "
                  "there are 24 orderings, the rule is unambiguous on each of them, and counting "
                  "the wins takes a few minutes."),
            ("h3", "The count, and why it is a real check"),
            ("p", "The closed form sums a harmonic series; the brute-force count plays the rule "
                  "out on every permutation of the ranks and counts how often it ends with the "
                  "best. The two computations share no line of arithmetic: one is a sum of "
                  "reciprocals, the other is a loop over orderings comparing integers. The lab "
                  "runs both for any `n` up to seven and compares them entry by entry, and shows "
                  "the table as checked only when every entry agrees."),
            ("example", ("Seven candidates, 5040 orderings",
                         "At `n = 7` the best `r` is 3 &mdash; reject two, then take the next "
                         "record &mdash; and it succeeds with probability 29/70, about 0.414286. "
                         "The counts over all 5040 orderings are 720, 1764, 2088, 2052, 1776, "
                         "1320 and 720, and every one of the seven fractions matches the closed "
                         "form exactly.",
                         "Notice `r = 3` and `r = 4` are close: 2088 wins against 2052, which is "
                         "29/70 against 57/140. Rounded to two decimals they are both 0.41, and "
                         "a page that printed decimals would be unable to say which rule was "
                         "better. That is what the exact table is for.")),
            ("h3", "The limit, and where it belongs"),
            ("p", "Push the candidate slider to its highest setting, sixty, and the table is too "
                  "long to print in full so the lab shows every few rows and the best one. The "
                  "best `r` is 23 &mdash; reject 22 &mdash; and it succeeds with probability "
                  "about 0.373210. Meanwhile `n/e` is 22.0728, printed rounded because `1/e` is "
                  "irrational. The two are close and they are not the same, and at `n = 4` they "
                  "are 2 against 1.4715, which is not close at all."),
            ("p", "This is the only rounded number anywhere on the course and the page labels it. "
                  "The reason to keep it is that `n/e` is what a reader will meet everywhere "
                  "else, and meeting it here as a limit sitting beside an exact table is the "
                  "right way round: the table is the answer, the constant is a description of "
                  "how the answer behaves for large `n`, and the asymptotic argument that makes "
                  "it a limit is not one this path has built."),
            ("h3", "What the model left out"),
            ("p", "Every ordering is equally likely, which is the assumption doing nearly all of "
                  "the work: it is what makes a record at position `i` mean the same thing "
                  "whatever the underlying qualities were. The objective is also unusually harsh "
                  "&mdash; you succeed only by getting the very best, and ending with the second "
                  "best scores the same as ending with the worst. Change that to maximising "
                  "expected rank and the optimal rule changes shape entirely."),
            ("p", "And nobody can be recalled, nobody refuses, `n` is known in advance, and "
                  "there is no cost to looking. Each of those is a modelling decision. The "
                  "arithmetic here is exact and exhaustively checked, and it is exact about a "
                  "situation with all four of them true."),
        ],
        "lab": ("dpseq", {
            "mode": "secretary",
            "preset": "small",
            "panel_title": "Choose how many to reject, and see what it costs you",
            "panel_intro": "Every probability here is an exact fraction from the harmonic sum, "
                           "and for seven candidates or fewer each one is checked by playing the "
                           "rule out on all `n!` orderings and counting the wins &mdash; two "
                           "computations with no arithmetic in common. The `n/e` a textbook "
                           "quotes is printed beside them, rounded and labelled as the limit it "
                           "is. At four candidates the whole thing can be verified by hand.",
        }),
        "steps_title": "Computing the table, and reading it",
        "steps_intro": "Four steps. The third is where the exactness earns its keep, and the fourth is the one people skip.",
        "steps": [
            ("Write down what success requires, in one sentence",
             "The best candidate is at position `i`, and the best of the first `i−1` is inside "
             "the rejected prefix. Those two events are independent, which is the only "
             "probabilistic content of the whole derivation."),
            ("Sum over the positions the best candidate could occupy",
             "`1/n` for its position times `(r−1)/(i−1)` for the prefix condition, summed over "
             "`i` from `r` to `n`. The `1/n` comes out of the sum and the rest is a difference "
             "of harmonic numbers."),
            ("Keep the entries as fractions and compare them as fractions",
             "At `n = 7` the two best rules score 29/70 and 57/140, which round to the same two "
             "decimals. Deciding between them requires the exact values, and this is the "
             "ordinary case rather than a contrived one &mdash; the table is flat near its "
             "maximum by construction."),
            ("Check against the count whenever the count is affordable",
             "Up to seven candidates, play the rule out on every ordering and count. `7!` is "
             "5040 and a page can do it; `8!` is 40320 and it cannot, so the honest thing at "
             "larger `n` is to say the table is the closed form alone, which is what the lab "
             "does."),
        ],
        "worked": {
            "title": "Four candidates by hand, and seven by counting",
            "intro": [
                "At four candidates the whole problem fits on a page: 24 orderings, four rules, "
                "and every entry of the closed form checkable against a count."
            ],
            "lines": [
                "n = 4      P(r) = ((r-1)/4) x sum of 1/(i-1) for i from r to 4",
                "",
                "   r     the harmonic sum         P(r) exactly    as a decimal    wins",
                "",
                "   1     -                            1/4           0.250000       6",
                "   2     1/1 + 1/2 + 1/3 = 11/6      11/24          0.458333      11",
                "   3     1/2 + 1/3 = 5/6              5/12          0.416667      10",
                "   4     1/3                          1/4           0.250000       6",
                "",
                "   24 orderings walked, the rule played out on each, the wins counted:",
                "   6, 11, 10, 6  out of 24  -- every entry matches the closed form",
                "",
                "   best r = 2:  reject 1, then take the first candidate better than it",
                "   n/e = 1.4715  (rounded)   -- the limit, and here it is not even near 2",
                "",
                "n = 7",
                "",
                "   r         1      2      3      4      5      6      7",
                "   wins    720   1764   2088   2052   1776   1320    720      of 5040",
                "   P(r)    1/7   7/20  29/70 57/140 37/105  11/42    1/7",
                "   dec.  0.1429 0.3500 0.4143 0.4071 0.3524 0.2619 0.1429",
                "",
                "   best r = 3, winning 29/70;  r = 4 is 57/140, and to two places both are 0.41",
                "   n/e = 2.5752 (rounded)",
            ],
            "after": [
                "The `n = 7` row of decimals is the argument for exact arithmetic in one line. "
                "The best two rules differ by 36 orderings out of 5040, which is 1/140, and "
                "every rounding anyone would reach for erases it. The table is flat near its "
                "maximum because that is the shape of the trade, so this is the normal situation "
                "rather than an awkward instance.",
                "For a rehearsal, work out the `n = 3` table by hand: six orderings, three "
                "rules, and the answer is that `r = 2` wins three times in six while `r = 1` and "
                "`r = 3` each win two. Then check it against the closed form. It is the smallest "
                "case with a genuine decision in it, and doing it by hand is the fastest way to "
                "understand what the rule actually does on a permutation.",
                "The harder rehearsal: move the slider from three candidates upwards one at a "
                "time and record where the best `r` increases. It does not increase every time, "
                "and the positions at which it does are not evenly spaced. Compare that sequence "
                "with `n/e` rounded, and you will see both how good the approximation is and "
                "exactly where it is wrong.",
            ],
        },
        "quiz_title": "Ranks, prefixes and an exact table",
        "quiz": [
            {"q": "What do you observe when candidate `k` arrives?",
             "a": ["Its quality, on a known scale",
                   "Only whether it is the best of the first `k`",
                   "Its rank among all `n` candidates",
                   "Its quality, but only relative to a threshold you set in advance"],
             "c": 1,
             "why": "Relative rank among those seen, and nothing else. That is why the answer "
                    "does not depend on the distribution the qualities came from &mdash; the "
                    "rule never touches a value &mdash; and why the rule cannot ask whether a "
                    "candidate is good enough, only whether it is a record."},
            {"q": "At `n = 7` the two best rules score 29/70 and 57/140. Why does the lab keep these as fractions?",
             "a": ["Because the numbers are too large for a decimal",
                   "Because they round to the same two places, and deciding between the rules needs the exact values",
                   "Because the harmonic sum has no decimal expansion",
                   "As a stylistic convention shared with the rest of the path"],
             "c": 1,
             "why": "0.4143 against 0.4071 &mdash; both 0.41 at two places, and 36 orderings out "
                    "of 5040 apart. The table is flat near its maximum by construction, so this "
                    "is the ordinary case. An exact comparison is the only kind that decides it."},
            {"q": "The lab prints `n/e` beside the table, labelled as rounded. What is it?",
             "a": ["The success probability of the best rule",
                   "The limiting position of the best `r` as `n` grows, which at small `n` is not even an integer",
                   "The number of candidates you should interview before deciding, exactly",
                   "An approximation to the harmonic sum"],
             "c": 1,
             "why": "At `n = 4` it is 1.4715 while the best `r` is 2; at `n = 7` it is 2.5752 "
                    "while the best `r` is 3. It describes how the answer behaves for large `n`, "
                    "the asymptotic argument for it is not built on this path, and the exact "
                    "table never needs it."},
            {"q": "The closed form and the brute-force count are run side by side up to seven candidates. Why is that a real check rather than a restatement?",
             "a": ["Because the count is faster",
                   "Because one sums reciprocals and the other loops over orderings comparing integers &mdash; no arithmetic in common",
                   "Because the count covers rules the closed form does not",
                   "Because the closed form is only an approximation"],
             "c": 1,
             "why": "A check has to be independent of the thing it checks. The count never forms "
                    "a harmonic number and the formula never looks at a permutation, so an error "
                    "in one cannot hide in the other. Past seven candidates the count becomes "
                    "unaffordable and the page says the table is unchecked rather than implying "
                    "otherwise."},
        ],
        "mistakes": [
            ("Thinking the rule needs to know the distribution of quality",
             "It never touches a value. All it uses is the relative rank of each arrival, which "
             "is why the success probability is the same whatever the qualities are drawn from "
             "&mdash; provided every ordering is equally likely. That last condition is the one "
             "doing the work, and it is the one to check against a real situation, where "
             "arrivals are often anything but exchangeable."),
            ("Reading `n/e` as the rule",
             "It is the limit of the optimal `r`, and the exact table is the answer. At four "
             "candidates the limit says 1.4715 and the best `r` is 2; at sixty it says 22.0728 "
             "and the best is 23. Quoting the constant as though it were the recipe also quietly "
             "imports an asymptotic argument that has not been made anywhere on this path."),
            ("Forgetting how harsh the objective is",
             "Success means ending with the very best candidate. Ending with the second best "
             "counts exactly the same as ending with the worst or with nobody at all, which is "
             "almost never what anyone actually wants. Under a gentler objective &mdash; "
             "minimising the expected rank of whoever you hire &mdash; the optimal rule is a "
             "different shape, and the famous answer does not transfer."),
        ],
        "standard": ("Finish when you can derive `P(r)` from the two independent events, build the table for four candidates in fractions, and say exactly what `n/e` is and is not.",
                     "You should be able to state what is observed on each arrival, explain why "
                     "the optimal rule rejects a prefix and then takes a record, derive the "
                     "success probability as a sum over the best candidate's position, read the "
                     "best `r` off an exact table rather than off a limit, and check a small "
                     "case by playing the rule out on every ordering."),
        "note": 'Every recursion so far has bottomed out somewhere: a last stage, a last activity, a last period, a last candidate. The closing lesson removes that. When the process never ends there is no final column to start from, and the value satisfies an equation instead of a recursion &mdash; which turns out to be a linear system with an exact solution, while the obvious method of repeated substitution is still climbing towards it. Watching the two side by side is the point, and the denominators tell the story better than the decimals do.',
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "value-iteration-and-the-fixed-point",
        "title": "Value Iteration and the Fixed Point",
        "module": "No last period",
        "one_line": "With no final period there is nothing to fill in from; the value satisfies a linear system, row reduction lands on it exactly, and value iteration never arrives.",
        "summary": (
            "Every table on this course has been filled from the end. Take the end away and the "
            "recursion has no base case &mdash; but the value still satisfies an equation: what "
            "a state is worth is its reward plus a discounted average of what the states it "
            "leads to are worth. That is `v = r + γPv`, and it is a linear system. Row reduction "
            "solves it exactly. Value iteration, which is the same map applied over and over "
            "from zero, approaches it and never gets there, and the denominators make the "
            "difference visible in a way that decimals cannot."
        ),
        "key": [
            "no last period, so no base case:  v = r + gamma P v  is an EQUATION, not a recursion",
            "rearranged:  (I - gamma P) v = r,  a linear system solved by row reduction",
            "P = [1/2 1/2 ; 1/4 3/4],  r = (1, 3),  gamma = 1/2:   v = 22/7 and 38/7",
            "check:  r + gamma P v - v  =  0 exactly, in every row",
            "value iteration from zero reaches 3.14171782 after 12 steps, against 22/7",
            "its denominator grows from 1 digit to 10 over those 12 steps, and never stops",
        ],
        "key_label": "One equation, two ways at it, and the check that separates them",
        "concepts_intro": (
            "Three ideas: why the recursion stops working, what replaces it, and what the "
            "iteration is actually doing while it fails to arrive."
        ),
        "concepts": [
            ("Without a last period there is no base case, so there is no recursion",
             "`Vₜ` was always defined from `Vₜ₊₁`, and the chain terminated at `V_T = 0`. Remove "
             "the horizon and that chain has no end to hang from. What survives is the "
             "self-consistency the values must satisfy: `v(i) = r(i) + γ Σⱼ P(i,j) v(j)` for "
             "every state at once. That is not a rule for computing `v`; it is a condition `v` "
             "obeys, and finding `v` means solving it."),
            ("The discount is what makes the equation have one answer",
             "With `γ = 1` the totals would generally be infinite and the equation would have "
             "many solutions or none. With `0 ≤ γ < 1` the matrix `I − γP` is invertible for "
             "every stochastic `P`, so there is exactly one `v`. The discount is doing "
             "mathematical work as well as modelling work, and a reader who treats it purely as "
             "a preference about the future is missing why it is there."),
            ("Value iteration is the same map applied repeatedly, and it converges without arriving",
             "Start at `v₀ = 0` and apply `v ← r + γPv`. Each step replaces the error vector "
             "by `γP` times itself, so the error shrinks by a factor tending to `γ` a step and "
             "the values reach the fixed point at no finite step. In exact arithmetic this is not a rounding story: every iterate is "
             "a rational with a denominator one power of `γ`'s denominator larger than the last, "
             "and the fixed point `22/7` is not among them."),
        ],
        "read_title": "An equation instead of a recursion, and two ways to meet it",
        "read_intro": "Where the base case went, what the equation is, and what the iteration is accumulating while it approaches the answer.",
        "body": [
            ("def", ("The discounted value of a policy",
                     "Fix a transition matrix `P` with rows summing to 1, a reward `r(i)` earned "
                     "on each visit to state `i`, and a <strong>discount factor</strong> `γ` "
                     "with `0 ≤ γ < 1`. The <strong>value</strong> `v(i)` is the expected total "
                     "of `r` earned from state `i` onward, with a reward `k` steps away counted "
                     "at `γᵏ` of its face value.",
                     "It satisfies `v = r + γPv`, equivalently `(I − γP)v = r`. Since `I − γP` "
                     "is invertible for every stochastic `P` when `γ < 1`, that system has "
                     "exactly one solution.")),
            ("p", "Two states will do. Let `P` send the first state to each of the two with "
                  "probability one half, and the second to the first with probability one "
                  "quarter and to itself with three quarters; let the rewards be 1 and 3, and "
                  "let the discount be one half. Writing `(I − γP)v = r` out gives two equations "
                  "in two unknowns, and row reduction solves them in four operations."),
            ("math", [
                "P = [ 1/2  1/2 ;  1/4  3/4 ]      r = ( 1 , 3 )      gamma = 1/2",
                "",
                "(I - gamma P) v = r:",
                "",
                "     3/4 v1  -  1/4 v2  =  1",
                "    -1/8 v1  +  5/8 v2  =  3",
                "",
                "row reduction gives     v1 = 22/7        v2 = 38/7",
                "",
                "put them back in:",
                "",
                "    3/4 (22/7) - 1/4 (38/7)  =  66/28 - 38/28  =  28/28  =  1     exactly",
                "   -1/8 (22/7) + 5/8 (38/7)  = -22/56 + 190/56 = 168/56  =  3     exactly",
                "",
                "   so  r + gamma P v - v  =  0  in both rows, with nothing rounded",
            ]),
            ("p", "That last line is the whole reason for exact arithmetic on this page. A "
                  "decimal solution would give a residual of something like `1e−16`, which is "
                  "indistinguishable from a small error in the solve, and the claim "
                  "&ldquo;this is the fixed point&rdquo; would be unverifiable on the page. As "
                  "fractions the residual is zero, and the reader can check the two lines above "
                  "by hand."),
            ("h3", "What value iteration does instead"),
            ("p", "Start at zero and apply the map. `v₁` is just `r`, which is `(1, 3)`. `v₂` is "
                  "`(2, 17/4)`. Then `(41/16, 155/32)`, then `(365/128, 1315/256)`, and so on. "
                  "Each step replaces the gap by `γP` times itself, so the ratio settles to `γ` a "
                  "step &mdash; a half here, so the gap heads towards quartering every two "
                  "steps: 1.14285714, then 0.29129464, then 0.07291085, then 0.01822908, then "
                  "0.00455729, then 0.00113932."),
            ("math", [
                "value iteration from zero, gamma = 1/2",
                "",
                "   step         state 1                      digits in     gap at",
                "                                             denominator   state 1",
                "",
                "   v0           0                                 1        3.14285714",
                "   v2           2                                 1        1.14285714",
                "   v4           365/128                           3        0.29129464",
                "   v6           25149/8192                        4        0.07291085",
                "   v8           1638205/524288                    6        0.01822908",
                "   v10          105303869/33554432                8        0.00455729",
                "   v12          6746787645/2147483648            10        0.00113932",
                "",
                "   the exact fixed point                v1 = 22/7 = 3.142857...",
                "   after twelve steps                        3.14171782",
                "",
                "   the denominator grew by 9 digits and the answer was available at step zero",
            ]),
            ("p", "The denominator column is the part a decimal cannot show. Every iterate is a "
                  "rational whose denominator carries one more power of two than the last, so "
                  "the iteration is not slowly approaching `22/7` through numbers that are "
                  "nearly it &mdash; it is walking through an infinite sequence of rationals "
                  "none of which is `22/7`, and getting more expensive to write down at every "
                  "step. Ten digits after twelve steps, and nothing stops it."),
            ("example", ("A discount closer to one",
                         "Keep the same chain and the same rewards and set the discount to nine "
                         "tenths. The fixed point becomes 670/31 and 750/31, about 21.6 and "
                         "24.2, which is far larger &mdash; a patient decision-maker values the "
                         "same stream much more highly. Row reduction still takes four "
                         "operations.",
                         "Value iteration, on the other hand, is now multiplying the gap by 9/10 "
                         "rather than 1/2 at each step, so after twelve steps it is nowhere near. "
                         "The two methods have not changed. What has changed is that one of them "
                         "is sensitive to a parameter the other is indifferent to, and that is "
                         "the argument for solving rather than iterating.")),
            ("example", ("Three states, and the same four lines of work",
                         "A three-state chain with rewards 2, 0 and 5 and a discount of three "
                         "quarters gives 1508/163, 1096/163 and 2192/163. The system is 3 by 3, "
                         "row reduction handles it in one pass, and the residual is again "
                         "exactly zero in every row.",
                         "The denominators of the iterates are worse here, not better: at twelve "
                         "steps they run to eighteen digits. Nothing about the exact solve has "
                         "got harder, and everything about the iteration has &mdash; which is "
                         "the pattern rather than a feature of this instance.")),
            ("h3", "Why value iteration exists at all"),
            ("p", "None of this makes the iteration useless, and the page is careful not to say "
                  "so. It needs no matrix inverse and no elimination, it works when the state "
                  "space is far too large to write `I − γP` down, and it extends directly to the "
                  "case where an action has to be chosen in each state, where the map has a "
                  "maximum in it and the system stops being linear. On a chain this small, with "
                  "no action to choose, it is the slow way round &mdash; and seeing it be the "
                  "slow way round on a small instance is how you learn what it is buying you on "
                  "a large one."),
            ("h3", "What this course has not built"),
            ("p", "There is no decision here. Fix a policy and its value is a linear system; ask "
                  "for the best policy and you need the maximum back inside the map, at which "
                  "point the equation is no longer linear and the method that solves it "
                  "alternates between evaluating a policy and improving it. That method needs a "
                  "chain with a class structure and a steady state already in hand, which is "
                  "Markov Chains, Decisions and Queues, and it is deliberately not attempted "
                  "here."),
            ("p", "And the discount itself is a modelling choice standing in for several "
                  "different things &mdash; an interest rate, a probability of the process "
                  "ending, an impatience &mdash; which happen to have the same arithmetic and "
                  "quite different justifications. The value `22/7` is exactly right for `γ = "
                  "1/2`, and the question of whether `1/2` is the right number is not one the "
                  "residual can answer."),
        ],
        "lab": ("dpseq", {
            "mode": "discount",
            "preset": "two",
            "panel_title": "Iterate, and solve, and watch the gap between them",
            "panel_intro": "The fixed point is found by row reduction on `(I - gP)v = r` and "
                           "then put straight back into the equation it solves, so the residual "
                           "is shown rather than assumed. Value iteration is drawn beside it "
                           "from zero, with the denominator it is accumulating printed for each "
                           "step &mdash; which is the part of &ldquo;it converges but never "
                           "arrives&rdquo; that a decimal cannot display. Move the discount "
                           "towards one and watch only one of the two methods notice.",
        }),
        "steps_title": "Solving for a value rather than iterating towards it",
        "steps_intro": "Four steps. The third is the one that makes the answer checkable, and it costs almost nothing.",
        "steps": [
            ("Write the self-consistency condition, one equation per state",
             "`v(i) = r(i) + γ Σⱼ P(i,j) v(j)`. Resist the urge to read it as an assignment: it "
             "is a condition on the whole vector at once, and every state's equation mentions "
             "every other state's value."),
            ("Rearrange into `(I − γP)v = r` and check the discount is below one",
             "Move the `γPv` across. If `γ = 1` the matrix is singular for any stochastic `P` "
             "&mdash; the all-ones vector is in its kernel &mdash; and there is no unique "
             "solution to find. No such discount appears in the selector, and the solver behind "
             "it refuses a singular system by name rather than returning a number."),
            ("Solve by row reduction, in exact fractions",
             "The same elimination used everywhere else on this path. For two or three states it "
             "is a handful of operations and the entries stay rational throughout, because the "
             "data are rational."),
            ("Substitute the answer back and confirm the residual is zero",
             "Compute `r + γPv − v` row by row. In exact arithmetic it is `0`, not nearly zero, "
             "and that is a check a floating-point solve cannot offer. It takes one pass and it "
             "converts a claim into something the reader can verify."),
            ("Only then compare with value iteration, and look at the denominators",
             "Run the map from zero and watch two things: the gap shrinking towards a factor "
             "of `γ` a step, and the denominator growing by one power of `γ`'s denominator each "
             "step. The second is the honest picture of what &ldquo;never arrives&rdquo; means."),
        ],
        "worked": {
            "title": "One system, solved and approached",
            "intro": [
                "The same two-state chain twice: once as a linear system with the answer checked "
                "by substitution, and once as a sequence of iterates with their denominators."
            ],
            "lines": [
                "P = [ 1/2 1/2 ; 1/4 3/4 ]     r = (1, 3)     gamma = 1/2",
                "",
                "SOLVED",
                "",
                "    3/4 v1 - 1/4 v2 = 1",
                "   -1/8 v1 + 5/8 v2 = 3          row reduction, four operations",
                "",
                "   v1 = 22/7 = 3.142857        v2 = 38/7 = 5.428571",
                "",
                "   residual  r + gamma P v - v   =   0 ,  0        exactly, both rows",
                "",
                "APPROACHED",
                "",
                "   step    state 1                    state 2                 denom digits",
                "   v0      0                          0                            1",
                "   v2      2                          17/4                         1",
                "   v4      365/128                    1315/256                     3",
                "   v6      25149/8192                 87747/16384                  4",
                "   v8      1638205/524288             5673155/1048576              6",
                "   v10     105303869/33554432         363999427/67108864           8",
                "   v12     6746787645/2147483648      23310643395/4294967296      10",
                "",
                "   after twelve steps    3.14171782      gap 0.0011393229",
                "   the answer, available at step zero    3.142857...  =  22/7",
                "",
                "   gap at state 1, every second step:",
                "      3.14285714  1.14285714  0.29129464  0.07291085  0.01822908",
                "      0.00455729  0.00113932        settling to a quarter of the last",
            ],
            "after": [
                "The gap column is geometric in the limit, with ratio `γ` per step, which is a "
                "quarter per two steps at `γ = 1/2`; the early ratios sit a little above it "
                "because each step multiplies the gap by `γP` and `P` mixes the two states. "
                "Extrapolating it says the iteration needs "
                "about ten more steps per three decimal places and never terminates, and the "
                "denominator column says what those steps cost: one more digit each, forever.",
                "For a rehearsal, set the discount to 99/100 in the selector and read the fixed "
                "point. Row reduction still does four operations and the residual is still "
                "exactly zero. Then look at the plot: after twenty-four steps, the most the "
                "slider allows, the iteration has barely left the axis. One method noticed the "
                "parameter and the other did not.",
                "The harder rehearsal: set `γ` to 1/2 and change the rewards to `(1, 1)`. Predict "
                "the fixed point before solving &mdash; every state pays 1 forever, discounted "
                "at a half, so the value should be `1/(1 − 1/2) = 2` in both states regardless "
                "of `P`. Check it, then perturb one entry of `P` and confirm that the value does "
                "not move at all. That invariance is a property of the equation, and it is a "
                "good test of whether the equation is understood rather than merely solved.",
            ],
        },
        "quiz_title": "Equations, fixed points and what iteration costs",
        "quiz": [
            {"q": "Why can the backward recursion not be used when the horizon is infinite?",
             "a": ["Because the values would be infinite",
                   "Because there is no final period to start from, so the chain of definitions has no base case",
                   "Because the transition matrix is no longer stochastic",
                   "Because the rewards would have to be discounted"],
             "c": 1,
             "why": "`Vₜ` was always defined from `Vₜ₊₁` and the chain ended at `V_T = 0`. Remove "
                    "the horizon and nothing anchors it. What survives is the self-consistency "
                    "condition `v = r + γPv`, which is a condition on `v` rather than a way of "
                    "computing it, and solving it is a different kind of task."},
            {"q": "The lab reports the residual `r + γPv − v` as exactly zero. Why is that worth printing?",
             "a": ["Because it confirms the discount is below one",
                   "Because a floating-point solve would give something near zero, which is indistinguishable from a small error in the solve",
                   "Because the residual is the gap between the two methods",
                   "Because it is needed for the next iteration"],
             "c": 1,
             "why": "In fractions the residual is `0` and the claim that this is the fixed point "
                    "is verifiable by hand from two lines of arithmetic. A residual of `1e−16` "
                    "verifies nothing: it is what you would see whether the solve were right or "
                    "slightly wrong."},
            {"q": "After twelve steps of value iteration the first state reads 3.14171782 against a fixed point of 22/7, and the denominator has grown from one digit to ten. What does the denominator column show?",
             "a": ["That rounding error is accumulating",
                   "That the iterates are rationals whose denominators gain a power of `γ`'s denominator each step, so `22/7` is not among them at any finite step",
                   "That the iteration is diverging",
                   "That the chain has a long mixing time"],
             "c": 1,
             "why": "There is no rounding anywhere: every iterate is exact. The point is that "
                    "the exact iterates form a sequence of rationals approaching `22/7` and "
                    "never equalling it, each more expensive to write than the last. That is "
                    "what &ldquo;converges but never arrives&rdquo; looks like when nothing is "
                    "rounded."},
            {"q": "If row reduction is exact and fast here, why does value iteration exist?",
             "a": ["It does not; it is only shown for contrast",
                   "Because it needs no elimination, works when the state space is too large to write the matrix down, and extends directly to the case with a maximum in the map",
                   "Because it is more accurate for discounts close to one",
                   "Because it does not require the rows of `P` to sum to one"],
             "c": 1,
             "why": "On this chain it is the slow way round, and seeing that on a small instance "
                    "is the point. Its virtues appear where the linear system cannot be formed, "
                    "and where an action has to be chosen in each state &mdash; at which point "
                    "the map has a maximum in it and stops being linear at all."},
        ],
        "mistakes": [
            ("Reading `v = r + γPv` as an assignment",
             "It is a condition satisfied by the whole vector at once, not a rule that computes "
             "`v` from an earlier `v`. Reading it as an assignment is exactly what turns it into "
             "value iteration, which is a legitimate method and is not what the equation says. "
             "The equation says `v` is a fixed point; the iteration is one way of hunting for "
             "one."),
            ("Treating the discount as purely a taste about the future",
             "It is also what makes `I − γP` invertible. At `γ = 1` the all-ones vector is in "
             "the kernel of `I − P` for every stochastic `P`, so the system is singular and "
             "there is no unique value to find &mdash; the undiscounted infinite-horizon problem "
             "needs a different criterion altogether. The selector offers no such discount, and "
             "the solver refuses a singular system by name rather than returning something."),
            ("Concluding that value iteration is a mistake",
             "It is the slow way round <em>here</em>, on two states with no action to choose, "
             "and that is precisely why the comparison is worth making on a page. Where the "
             "matrix cannot be formed, or where a maximum sits inside the map and the system is "
             "no longer linear, the iteration is what there is. The lesson is about knowing "
             "which situation you are in, not about a winner."),
        ],
        "standard": ("Finish when you can turn `v = r + γPv` into a linear system, solve it in fractions, verify the residual is exactly zero, and explain what the iterates' denominators are telling you.",
                     "You should be able to say why an infinite horizon has no base case, "
                     "rearrange the self-consistency condition into `(I − γP)v = r`, justify "
                     "invertibility from `γ < 1`, solve a two-state or three-state system by row "
                     "reduction, substitute back to get a zero residual, and describe value "
                     "iteration as a sequence of exact rationals that approaches the answer "
                     "without reaching it."),
        "note": 'That closes the course, and the last table was the one that could not be filled from the end. Looking back over the nine, the arithmetic was never the difficulty: every recursion here is three or four lines and every answer was checked against an exhaustive enumeration of the thing the recursion stands for. What varied was the state, and choosing it &mdash; units left rather than units spent, the period of the last order rather than the stock on hand, periods remaining rather than offers seen, a relative rank rather than a value. A recursion is exact about the state you gave it. Deciding what that state should be is the part no check on this page can do for you, and it is where this whole path says the error lives.',
    },
]
