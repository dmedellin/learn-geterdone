"""Decision and Rationality, lessons 1-5: preference, ignorance, and the first of risk."""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "preference-transitivity-and-the-money-pump",
        "title": "Preference, Transitivity and the Money Pump",
        "module": "Preference",
        "one_line": "A cycle of preferences can be priced, and the price is paid every lap.",
        "summary": (
            "Preference is a relation on options, and rational choice needs it to be "
            "complete and transitive. Build a cyclic preference on the relation grid, "
            "read the pair that breaks transitivity, and compute what a trader earns "
            "by walking an agent round the cycle."
        ),
        "key": [
            "A ≻ B     A is preferred to B",
            "complete: of any two, one is preferred",
            "transitive: A ≻ B, B ≻ C give A ≻ C",
            "cycle: A ≻ B, B ≻ C, C ≻ A",
            "pay ε a swap: lose 3ε every lap",
        ],
        "key_label": "Transitive, or a trader eats you",
        "concepts_intro": (
            "A theory of choice has to start from what the chooser prefers. Before any "
            "number appears, there is a structure the preferences must have."
        ),
        "concepts": [
            ("Preference is a relation on options",
             "`A ≻ B` says the chooser ranks `A` strictly above `B`. The options may be "
             "cakes, careers or lotteries; the relation does not care, and that is why "
             "one condition on it can apply to all of them."),
            ("Two conditions make a ranking",
             "Complete: for any two options one is preferred or they are tied. "
             "Transitive: if `A ≻ B` and `B ≻ C`, then `A ≻ C`. Together they let the "
             "options be lined up, with ties sharing a rung."),
            ("A cycle has no best option",
             "If `A ≻ B`, `B ≻ C` and `C ≻ A`, every option is beaten by another, so "
             "choosing &ldquo;the best&rdquo; has no answer. The money pump shows the "
             "same defect from the outside, as a loss."),
        ],
        "read_title": "Preference, and the loop that cannot be ranked",
        "read_intro": "Two conditions, then the argument that the second one is not optional.",
        "body": [
            ("p", "Choice theory begins by asking what the chooser would pick from a "
                  "pair. Write `A ≻ B` when `A` is strictly preferred to `B`, and "
                  "`A ≽ B` when `A` is at least as good: preferred or tied. Everything "
                  "the course computes later, expected values and rules for ignorance "
                  "included, assumes that this relation can be turned into a ranking."),
            ("def", ("Completeness",
                     "A preference is <strong>complete</strong> when, for any two "
                     "options `A` and `B`, at least one of `A ≽ B` and `B ≽ A` holds. "
                     "The chooser is never left without a view on a pair.")),
            ("def", ("Transitivity",
                     "A preference is <strong>transitive</strong> when `A ≽ B` and "
                     "`B ≽ C` together give `A ≽ C`. A comparison that passes through a "
                     "third option does not change the answer.")),
            ("p", "The relation grid below makes both conditions things you can see. "
                  "Read a 1 in row `a`, column `b` as &ldquo;option `a` is preferred "
                  "to option `b`&rdquo;. A complete strict preference has a 1 on one "
                  "side of the diagonal or the other for every pair, with no gap. A "
                  "transitive one has no two-step path `a` to `b` to `c` without the "
                  "direct step `a` to `c`; the property table names the first "
                  "offending pair when there is one."),
            ("p", "The preset is the relation `a &lt; b` on five options, and as a "
                  "strict preference it is both complete and transitive: option 1 "
                  "beats all, option 5 beats none. Now click the cell in row 5, column "
                  "1. That adds the pair `5 ≻ 1` and closes a loop, because the "
                  "preset already ranks `1 ≻ 5` through the cell in row 1, column 5. "
                  "The table reports transitivity failing at the pair `(1, 5)` and "
                  "`(5, 1)` without `(1, 1)`: a cycle forces each option to be "
                  "preferred to itself, which no one means by preference."),
            ("math", [
                "A ≻ B",
                "B ≻ C",
                "C ≻ A",
            ]),
            ("p", "Nothing in those three lines is false as a report of taste. The "
                  "trouble is what a cyclic chooser will do. Suppose you hold `A`, and "
                  "you prefer `C` to `A`, `B` to `C` and `A` to `B`. A trader offers "
                  "`C` for `A` plus a small fee `ε`, and you accept because you prefer "
                  "`C`. The trader then offers `B` for `C` plus `ε`, and you accept. "
                  "Then `A` for `B` plus `ε`, and you accept again."),
            ("example", ("One lap",
                         "You began with `A` and you end with `A`. You are `3ε` poorer, "
                         "and each trade was one you wanted at the moment you made it. "
                         "Another lap costs another `3ε`, and the trader can run as "
                         "many laps as you will go round.")),
            ("p", "That is the money pump. It is an argument that transitivity is a "
                  "condition on what you prefer, not a feature of what you like. The "
                  "options can be anything and the fee as small as you please; the "
                  "loss is `3ε` a lap in every case, so a cycle among three kinds of "
                  "tea is exposed in the same way as a cycle among three jobs."),
            ("p", "The argument has a strongest objection, and it deserves a hearing. "
                  "A person may rank three flats by different standards, price against "
                  "size, size against light, light against price, and each pairwise "
                  "verdict can be reasonable. The reply is that this is a cycle in "
                  "the pairwise verdicts and not in the ranking of the flats as "
                  "wholes, so one of the standards has to give way or a weighting has "
                  "to be chosen before the person can act without being walked in "
                  "circles. Accepting the cycle costs the chooser the loss above; "
                  "rejecting a pairwise verdict costs a reason that looked sound."),
            ("p", "The limit of the argument is worth stating. It assumes the chooser "
                  "really will pay for each swap and has no memory of the lap. An "
                  "agent who sees the trader coming and refuses the third offer has "
                  "changed her preferences, which is exactly the repair that "
                  "transitivity asks for. The pump does not prove cycles "
                  "unthinkable; it prices them."),
        ],
        "lab": ("relation", {
            "size": 5, "preset": "lt",
            "panel_title": "A preference on five options, and the loop you add",
            "panel_intro": "Read the pair `(a, b)` as &ldquo;option `a` is preferred to option `b`&rdquo;. As shipped, the grid is the strict ranking in which a lower number is better: complete, because every pair of distinct options has a 1 on one side, and transitive, because the property table finds no offending pair. Click row 5, column 1 to add `5 ≻ 1`. Watch the transitive row turn to <strong>no</strong> and name a pair. Then click the same cell again to remove the pair, and click row 2, column 4 to delete that one. The property table has no row for completeness, so read it off the grid: options 2 and 4 now have a 1 on neither side, and a preference with such a gap is incomplete.",
        }),
        "steps_title": "Testing a preference, and pricing it",
        "steps_intro": "Four moves, in this order. The first three decide whether the ranking exists and the fourth puts a price on its failing.",
        "steps": [
            ("List the strict preferences as pairs",
             "Write each `X ≻ Y` the chooser holds, one per pair of options. If some "
             "pair has no entry and no tie, the preference is not complete, and a "
             "different question is being asked."),
            ("Follow every two-step chain",
             "For each `A ≻ B` and `B ≻ C`, look for `A ≻ C`. A missing pair is the "
             "witness that transitivity fails, and it is the only thing the check has "
             "to find."),
            ("Look for a way round",
             "If a chain of strict preferences returns to where it began, the "
             "preference has a cycle, and no option in the cycle is best."),
            ("Price one lap",
             "Start at any option in the cycle and take each preferred swap in turn, "
             "paying the fee each time. A lap of `k` swaps costs `k·ε`, and the "
             "agent holds exactly what it started with."),
        ],
        "worked": {
            "title": "A cycle of three, walked once",
            "intro": [
                "The chooser prefers C to A, B to C and A to B, and pays 1 cent for "
                "each swap to something preferred. She starts holding A."
            ],
            "lines": [
                "holds A      cash 0",
                "A -> C  pays 1 cent, prefers C to A        cash -1",
                "C -> B  pays 1 cent, prefers B to C        cash -2",
                "B -> A  pays 1 cent, prefers A to B        cash -3",
                "holds A      cash -3 cents after one lap",
                "after 100 laps    cash -300 cents, still holds A",
            ],
            "after": [
                "Each line, taken alone, is a choice the chooser endorses. It is the "
                "sequence that has no defence: she ends with what she began with and "
                "three cents fewer, and the pump may run for as long as she keeps "
                "saying yes."
            ],
        },
        "quiz_title": "Cycles and what they cost",
        "quiz": [
            {"q": "An agent strictly prefers X to Y, Y to Z and Z to X, and will pay 2 "
                  "cents to swap to anything it prefers. It holds X. A trader offers Z "
                  "for X, then Y for Z, then X for Y. What has the trader collected "
                  "when the agent is back to X?",
             "a": ["Nothing, because the agent ends where it started",
                   "2 cents, the fee for one swap",
                   "6 cents, a fee for each of three swaps",
                   "An amount that depends on how much the agent values X"],
             "c": 2,
             "why": "Each swap is to something the agent prefers, so each is paid for: "
                    "three swaps at 2 cents. The agent does end with X, but not with "
                    "its cash. One swap would be 2 cents, but there are three, and the "
                    "fee per swap was stated, so how much the agent values X does not "
                    "enter."},
            {"q": "Which situation does the transitivity condition rule out?",
             "a": ["Preferring A to B, B to C, and not A to C",
                   "Preferring A to B and also B to A",
                   "Having no preference between two options",
                   "Preferring a cheaper option to a dearer one"],
             "c": 0,
             "why": "That is the definition: A ≻ B and B ≻ C should give A ≻ C. "
                    "Preferring A to B and B to A is a different failure, of "
                    "asymmetry, and a transitive relation can still contain it. A tie "
                    "is allowed by the conditions, and so is a preference for the "
                    "dearer option, since the conditions say nothing about what is "
                    "preferred."},
            {"q": "Someone says: &ldquo;I prefer tea to coffee, coffee to juice and "
                  "juice to tea, and tastes are not open to criticism.&rdquo; What does "
                  "the money-pump argument say in reply?",
             "a": ["Tastes are never criticisable, so nothing can be said",
                   "No one can really have a cyclic preference, so the speaker is mistaken",
                   "A cycle among drinks is harmless because drinks are cheap",
                   "The content of the taste is left alone, but a cyclic preference can be traded against at a fixed loss per lap, whatever the options"],
             "c": 3,
             "why": "The argument is about the shape of the preferences, not what they "
                    "are for. It does not claim cycles cannot be reported, so the "
                    "second choice overreaches. Cheapness does not help, because the "
                    "loss is a multiple of the fee however small the fee is. The first "
                    "choice ignores the loss the cycle exposes the chooser to."},
        ],
        "mistakes": [
            ("Treating transitivity as a matter of taste",
             "Taste decides whether you prefer tea to coffee. Transitivity constrains how "
             "your preferences fit together, and it is violated by a cycle among any "
             "three options whatever they are. The cycle costs `3ε` a lap whether "
             "the options are drinks, jobs or flats, which is a fact about the "
             "structure and not about the contents."),
            ("Reading a cycle as indifference",
             "If `A`, `B` and `C` are tied, nothing is wrong: ties are transitive, and "
             "no one pays to swap between things they value equally. A cycle is the "
             "opposite case, a strict preference all the way round. Each swap in the "
             "pump is paid for because the agent <em>prefers</em> what it gets."),
            ("Expecting a single choice to show the defect",
             "Pick from the pair `A` and `B` and nothing looks wrong, and the same "
             "holds for the other two pairs. The cost appears only in a sequence, "
             "and it is the sequence the argument concerns."),
        ],
        "standard": ("Finish when you can build a cycle and put a price on it.",
                     "Given a set of options and the pairs a chooser prefers, you should "
                     "be able to say whether the preference is complete, name the pair "
                     "that breaks transitivity if there is one, and compute what a "
                     "trader collects over a given number of laps at a given fee."),
        "note": 'The lab here is the relation grid from the Discrete Mathematics path, used for a different job. Nothing from that path is assumed: a preference is a relation on the options, transitivity is the property defined above, and what this lesson adds is the reason to want it. “The Decision Matrix and Dominance” starts from preferences that are in order and asks how to choose among acts.',
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "the-decision-matrix-and-dominance",
        "title": "The Decision Matrix and Dominance",
        "module": "Ignorance",
        "one_line": "Lay acts against states, and drop any act that another beats everywhere.",
        "summary": (
            "A decision problem is a table of acts against states with a payoff in "
            "every cell. Dominance is the one rule that needs nothing but the table: "
            "it removes an act that some other act matches or beats in every state. "
            "When no act dominates, the table is silent, and the rest of the course "
            "is about what to add."
        ),
        "key": [
            "rows: acts    columns: states",
            "cell: the payoff of an act in a state",
            "a dominates b: at least as good in every",
            "  state, and better in at least one",
            "dominated acts are dropped, no odds needed",
        ],
        "key_label": "A table, and one rule that needs nothing else",
        "concepts_intro": (
            "Every rule in the next lessons reads the same object, so it is worth "
            "being exact about what the object holds."
        ),
        "concepts": [
            ("Acts, states, payoffs",
             "An act is something you can choose. A state is a way the world might be "
             "that you do not control. A payoff is how things go for you if you choose "
             "that act and the world is in that state. The table has one cell for "
             "each pair."),
            ("Dominance compares acts column by column",
             "Act `a` dominates act `b` when `a` is at least as good in every state and "
             "better in at least one. The comparison is state by state, never one "
             "act's best cell against another's."),
            ("No odds are needed",
             "Dominance uses no probabilities and no attitude to risk, which is why it "
             "is so hard to resist when it applies and so seldom decides anything."),
        ],
        "read_title": "Reading a decision table",
        "read_intro": "The table first, then the rule, then the way it falls silent.",
        "body": [
            ("p", "Whether to take an umbrella is a decision with two acts and two "
                  "states. If it rains, you are glad to have taken it; if it stays dry, "
                  "you carried it for nothing. Put numbers on how each of the four "
                  "cases goes for you and you have a decision table."),
            ("math", [
                "act      rain    dry",
                "take      2       1",
                "leave    -3       3",
            ]),
            ("p", "The first row reads: if you take the umbrella, you score 2 in rain "
                  "and 1 when it is dry. The numbers are yours to choose, and they "
                  "stand for how good each case is; the lab will not tell you whether "
                  "a soaking is worth minus 3, only what follows if it is."),
            ("def", ("Dominance",
                     "Act `a` <strong>dominates</strong> act `b` when `a` pays at least "
                     "as much as `b` in every state, and strictly more in at least "
                     "one. A dominated act can be removed from the table without "
                     "loss. If one act dominates all the others, it is the choice.")),
            ("p", "The umbrella table has no dominance. Take beats leave in rain, "
                  "2 to minus 3, and leave beats take when it is dry, 3 to 1. "
                  "Neither act is at least as good in both columns, so the lab reports "
                  "that no act dominates and picks none."),
            ("example", ("Adding a worse act",
                         "Add a third act, take a coat, paying 1 in rain and 0 when "
                         "dry. Take-the-umbrella pays 2 and 1 in the same states, "
                         "more in each, so it dominates the coat and the coat can be "
                         "struck out. The table is unchanged in what it recommends, "
                         "and the dominated act drops out. In the `dominated` preset "
                         "the status line under the table names the acts that survive, "
                         "take and leave, and the coat is not among them; the choice "
                         "tile still reads none, because neither survivor dominates "
                         "the other.")),
            ("p", "The lab's definition is the weak one, and the `weak` preset shows "
                  "why that matters. Take pays 2 and 1; leave pays 2 and 0. They tie in "
                  "rain, take wins when it is dry, so take dominates leave even "
                  "though it is not better everywhere. A strict version, better in "
                  "every state, would leave this table undecided."),
            ("p", "The best possible outcome is not the test. Leaving the umbrella "
                  "has the highest cell in the table, a 3, but that cell sits in only "
                  "one column and the same act has the lowest cell, minus 3, in the "
                  "other. Dominance asks about each column in turn."),
            ("p", "There is one condition on using dominance, and it is easy to "
                  "break. The states must not depend on the act. If you reason that "
                  "you will pass the exam whether or not you study and then skip the "
                  "revision, you have treated passing as a state when it is partly an "
                  "outcome of the act. “Newcomb's Problem” returns to exactly this "
                  "worry with a table that does seem to dominate."),
        ],
        "lab": ("choicekit", {
            "mode": "decide", "rule": "dominance",
            "preset": "umbrella",
            "presets": [
                {"id": "umbrella", "label": "umbrella, no dominance",
                 "acts": ["take", "leave"], "states": ["rain", "dry"],
                 "payoffs": [[2, 1], [-3, 3]], "expect": {"deChoice": "none"}},
                {"id": "dominated", "label": "a coat that the umbrella dominates",
                 "acts": ["take", "leave", "coat"], "states": ["rain", "dry"],
                 "payoffs": [[2, 1], [-3, 3], [1, 0]], "expect": {"deChoice": "none"}},
                {"id": "weak", "label": "a tie in one state",
                 "acts": ["take", "leave"], "states": ["rain", "dry"],
                 "payoffs": [[2, 1], [2, 0]], "expect": {"deChoice": "take"}},
            ],
        }),
        "steps_title": "Applying dominance to a table",
        "steps_intro": "Work pair by pair, and write down which state decided each comparison.",
        "steps": [
            ("Fix the states first",
             "Check that no state depends on what you choose. If one does, the "
             "table is mis-built and dominance may mislead."),
            ("Compare two acts column by column",
             "Write the two rows one over the other and compare each state. `a` "
             "dominates `b` only if no column favours `b` and at least one favours "
             "`a`."),
            ("Strike dominated acts and repeat",
             "Remove any act that another dominates, then compare what is left. "
             "Dominance is transitive, so the order of striking does not matter."),
            ("Ask whether one act is left",
             "If one remains, it is the choice. If several remain, dominance has done "
             "all it can and another principle has to choose."),
        ],
        "worked": {
            "title": "The umbrella, then a coat",
            "intro": [
                "Take, leave and coat in the states rain and dry, payoffs as in the "
                "lab. Compare the acts in pairs."
            ],
            "lines": [
                "take  vs leave   rain: 2 > -3    dry: 1 < 3     no dominance",
                "take  vs coat    rain: 2 > 1     dry: 1 > 0     take dominates",
                "leave vs coat    rain: -3 < 1    dry: 3 > 0     no dominance",
                "left after striking the coat: take, leave",
                "no single act dominates all the others, so no choice",
            ],
            "after": [
                "The coat went, and the decision did not get any easier. That is the "
                "usual shape of dominance reasoning: it removes the plainly bad "
                "acts and leaves the real question where it was."
            ],
        },
        "quiz_title": "Dominated or not",
        "quiz": [
            {"q": "Three acts, two states. X pays 5 and 5, Y pays 4 and 6, Z pays 5 and "
                  "4. Which statement is correct?",
             "a": ["X dominates Y", "X dominates Z", "Y dominates Z", "Z dominates X"],
             "c": 1,
             "why": "X ties Z in the first state and beats it, 5 to 4, in the second, "
                    "which is dominance. X does not dominate Y, since Y pays more in the "
                    "second state. Y does not dominate Z, because 4 is less than 5 in "
                    "the first state. Z is worse than X in the second, so it cannot "
                    "dominate X."},
            {"q": "No act dominates in the umbrella table. What follows?",
             "a": ["Take is the better choice, being safer",
                   "Leave is the better choice, because it holds the highest payoff, 3",
                   "The table was built wrongly",
                   "Dominance gives no answer, and a further principle is needed to choose"],
             "c": 3,
             "why": "Dominance can only remove acts that are beaten everywhere, and "
                    "none is. Safer and highest-payoff are both appeals to other "
                    "principles, which the next lessons examine. A table without "
                    "dominance is perfectly well formed; most real decisions are like it."},
            {"q": "When is reasoning by dominance unsafe?",
             "a": ["When there are more than two states",
                   "When some payoffs are negative",
                   "When a state is made more or less likely by the act you choose",
                   "When the probabilities of the states are unknown"],
             "c": 2,
             "why": "Dominance assumes the state is fixed independently of the act. If "
                    "skipping revision makes failing more likely, comparing columns "
                    "ignores the very connection that matters. More states and negative "
                    "payoffs change nothing in the comparison, and dominance never "
                    "uses probabilities at all."},
        ],
        "mistakes": [
            ("Choosing the act with the best possible outcome",
             "Leaving the umbrella has the highest cell in the table, a 3, and it is "
             "not the best act: it has the lowest cell too, minus 3. One cell does "
             "not rank an act. Dominance compares two acts state by state, and the "
             "umbrella table shows the best cell and the best act coming apart."),
            ("Dropping an act that merely does well in the likely state",
             "An act that is worse in some state is not dominated by an act that is "
             "better in the likely one. Dominance does not weigh states, so it "
             "cannot say that one column matters more; that is a job for the "
             "probabilities introduced later in the course."),
            ("Treating a tie as a reason to keep both acts",
             "If one act ties the other in every state but one and wins that one, "
             "it dominates. The `weak` preset has take and leave tied in rain, "
             "and take wins in the dry state, so take is the choice. Equal "
             "payoffs in a column are no reason to retain the weaker act."),
        ],
        "standard": ("Finish when you can lay out a table and say what dominance does to it.",
                     "Given a decision described in words, you should be able to "
                     "write it as acts against states, name any dominated act with "
                     "the state-by-state comparison that shows it, and say when "
                     "dominance leaves the choice undecided."),
        "note": "The lab ships with the dominance rule and with no probabilities, which is the situation of this lesson. The rule menu has the others, which the next two lessons use; a rule that needs odds will say so rather than invent them.",
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "maximin-maximax-and-minimax-regret",
        "title": "Maximin, Maximax and Minimax Regret",
        "module": "Ignorance",
        "one_line": "Three ways to choose when you cannot say how likely any state is.",
        "summary": (
            "When dominance is silent and no probabilities are available, a rule must "
            "turn each row of the table into one score. Maximin scores the worst "
            "case, maximax the best, and minimax regret the largest shortfall from "
            "what the state allowed. They can disagree on one table, and the "
            "disagreement is the lesson."
        ),
        "key": [
            "maximin: best of the row minimums",
            "maximax: best of the row maximums",
            "regret = column best − your payoff",
            "minimax regret: smallest worst regret",
            "regret ignores a gain every act shares",
        ],
        "key_label": "Three rules, three scores per row",
        "concepts_intro": (
            "A rule for ignorance reduces each act to a single number computed from its "
            "row of the table, and then picks the best number. What differs is which "
            "number."
        ),
        "concepts": [
            ("Maximin is the pessimist's rule",
             "Score each act by its worst payoff and take the act whose worst is best. "
             "It guards against the worst state and cares about nothing else."),
            ("Maximax is the optimist's rule",
             "Score each act by its best payoff and take the act whose best is "
             "highest. It chases the best state and ignores the risk."),
            ("Regret is measured against the state",
             "In each state the best act pays something. The regret of an act in that "
             "state is the best payoff minus what it paid. Minimax regret takes the "
             "act whose largest regret is smallest."),
        ],
        "read_title": "Three scores from one table",
        "read_intro": "The umbrella table again, scored three ways, and then a table where two rules part.",
        "body": [
            ("p", "“The Decision Matrix and Dominance” left the umbrella undecided. "
                  "Take pays 2 in rain and 1 when dry; leave pays minus 3 and 3. "
                  "Suppose you have no idea how likely rain is. The three rules here "
                  "each give an answer, and they do not all give the same one."),
            ("def", ("Maximin",
                     "Score each act by its minimum payoff across the states. Choose "
                     "the act with the largest such minimum. On the umbrella table "
                     "take scores 1 and leave scores minus 3, so maximin takes the "
                     "umbrella.")),
            ("def", ("Maximax",
                     "Score each act by its maximum payoff. Choose the act with the "
                     "largest maximum. Take scores 2 and leave scores 3, so maximax "
                     "leaves it at home.")),
            ("def", ("Minimax regret",
                     "Build the regret table first: in each column, subtract every "
                     "payoff from the column's best. Score each act by its largest "
                     "regret and choose the smallest score.")),
            ("math", [
                "regret    rain    dry",
                "take        0      2",
                "leave       5      0",
            ]),
            ("p", "In rain the best payoff is 2, from take, so take regrets nothing and "
                  "leave regrets 2 − (−3) = 5. When it is dry the best is 3, from "
                  "leave, so leave regrets nothing and take regrets 3 − 1 = 2. The "
                  "largest regrets are 2 for take and 5 for leave, so minimax regret "
                  "also takes the umbrella."),
            ("p", "On this table, then, two rules say take and one says leave. The "
                  "`disagree` preset is a table where maximin and minimax regret part. "
                  "A safe act pays 3 in a weak market and 3 in a strong one; a bold "
                  "act pays 2 and 10. Maximin takes the safe act, whose worst is 3 "
                  "against 2. But the safe act regrets 7 in the strong market, "
                  "where the bold one would have paid 10, while the bold act regrets "
                  "at most 1. Minimax regret takes the bold act."),
            ("p", "Minimax regret is maximin applied to a different table, the regret "
                  "table, and that table is relative: each column is measured from "
                  "its own best. So anything every act shares in a state drops "
                  "out of the regret table and cannot move the answer. It does move "
                  "maximin. The `shifted` preset adds a bonus of 10 to the rain "
                  "column for both acts, as if rain brought an allowance whatever you "
                  "carried. The regret table is unchanged and still picks take, but "
                  "take's worst is now 1 and leave's worst is 3, so maximin switches "
                  "to leave."),
            ("p", "None of the three is the right rule. Each encodes an attitude: "
                  "maximin says the worst state is the one to plan for, maximax that "
                  "the best state is, and minimax regret that the thing to avoid is "
                  "having chosen worse than the state allowed. The lab computes what "
                  "each says exactly; which attitude to hold is left to you."),
        ],
        "lab": ("choicekit", {
            "mode": "decide", "rule": "maximin",
            "preset": "umbrella",
            "presets": [
                {"id": "umbrella", "label": "umbrella, maximin and regret agree",
                 "acts": ["take", "leave"], "states": ["rain", "dry"],
                 "payoffs": [[2, 1], [-3, 3]], "expect": {"deChoice": "take", "deValue": "1"}},
                {"id": "disagree", "label": "a table where maximin and regret part",
                 "acts": ["safe", "bold"], "states": ["weak market", "strong market"],
                 "payoffs": [[3, 3], [2, 10]], "expect": {"deChoice": "safe", "deValue": "3"}},
                {"id": "shifted", "label": "umbrella with 10 added to the rain column",
                 "acts": ["take", "leave"], "states": ["rain", "dry"],
                 "payoffs": [[12, 1], [7, 3]], "expect": {"deChoice": "leave", "deValue": "3"}},
            ],
            "panel_title": "One table, three rules",
            "panel_intro": "Each preset opens under maximin. Change the rule menu to maximax or to minimax regret and the same payoffs are scored again; the score column shows what each act earned under the rule. On `disagree`, switch from maximin to minimax regret and watch the choice change.",
        }),
        "steps_title": "Applying the three rules",
        "steps_intro": "Do the three scores in the order below and compare the verdicts.",
        "steps": [
            ("Write each row's minimum and maximum",
             "Take the smallest and largest entry of each row. These two columns "
             "give maximin and maximax at once."),
            ("Build the regret table",
             "For each state, find the best payoff in its column, then subtract "
             "each act's payoff from it. Every entry is zero or more, and each column "
             "has a zero."),
            ("Score the regret rows by their largest entry",
             "Each act's score is its worst regret. The smallest worst regret "
             "wins."),
            ("Compare and look for a disagreement",
             "If the three rules pick the same act, the choice does not depend on "
             "attitude. If not, say which state's worst case is driving each."),
        ],
        "worked": {
            "title": "Where maximin and minimax regret part",
            "intro": [
                "Two acts in two markets. Safe pays 3 and 3; bold pays 2 and 10."
            ],
            "lines": [
                "maximin     safe min 3     bold min 2     picks safe",
                "maximax     safe max 3     bold max 10    picks bold",
                "regret      safe 0, 7      bold 1, 0",
                "worst regret   safe 7      bold 1         picks bold",
                "maximin and minimax regret pick different acts",
            ],
            "after": [
                "Safe guards against the poor market and pays for it with a regret of "
                "7 in the good one. Bold risks a loss of 1 against safe in the weak "
                "market and wins 7 in the strong. A decision maker who dreads "
                "having acted unwisely will take bold; one who dreads the worst "
                "outcome will take safe."
            ],
        },
        "quiz_title": "Three rules, one table",
        "quiz": [
            {"q": "On the umbrella table, take pays 2 and 1, leave pays −3 and 3. "
                  "Which rule picks leave?",
             "a": ["Maximax", "Maximin", "Minimax regret", "All three of them"],
             "c": 0,
             "why": "Leave has the highest single payoff, 3, so maximax picks it. "
                    "Maximin compares the minimums, 1 for take against −3 for leave, "
                    "so it takes the umbrella. Minimax regret compares worst regrets, "
                    "2 against 5, and also takes the umbrella."},
            {"q": "What is the regret of an act in a given state?",
             "a": ["Its payoff minus the smallest payoff in that column",
                   "Its best payoff minus its worst payoff",
                   "The best payoff in that column minus its own payoff in that column",
                   "Its payoff with the sign reversed"],
             "c": 2,
             "why": "Regret is measured against what the state allowed: the column "
                    "best minus the act's payoff. The first choice measures from the "
                    "worst, which would reward bad acts. The second is a property of "
                    "one row, not a comparison with other acts. A sign reversal "
                    "would turn payoffs into costs, not shortfalls."},
            {"q": "Both acts get the same extra bonus in one state, so that column's "
                  "entries all rise by 10. Which of the three rules can change its choice?",
             "a": ["None of the three rules",
                   "All three rules",
                   "Minimax regret only",
                   "Maximin and maximax, but not minimax regret"],
             "c": 3,
             "why": "A bonus shared by every act in a state does not change any "
                    "difference within that column, so each regret entry stays "
                    "the same and so does the minimax regret choice. Maximin and "
                    "maximax read raw payoffs, so either can change: the shifted "
                    "cell may stop or start being a row's minimum or its maximum. "
                    "Adding 10 to the rain column of the umbrella takes maximin "
                    "from take to leave and maximax from leave to take."},
            {"q": "Safe pays 3 and 3, bold pays 2 and 10. Which statement is correct?",
             "a": ["Maximin and minimax regret both pick safe",
                   "Maximin picks safe and minimax regret picks bold",
                   "Maximin picks bold and minimax regret picks safe",
                   "Both pick bold"],
             "c": 1,
             "why": "The minimums are 3 and 2, so maximin picks safe. The worst "
                    "regrets are 7 for safe, in the strong market, and 1 for bold, in "
                    "the weak one, so minimax regret picks bold."},
        ],
        "mistakes": [
            ("Treating minimax regret as maximin on a different table, and stopping there",
             "It is maximin applied to the regret table, and the correction is in "
             "the word different. Regret is measured from each state's own best, "
             "so it is blind to a gain every act shares in a state, while maximin "
             "reads the raw payoffs. Add 10 to the rain column of the umbrella "
             "and minimax regret still takes the umbrella; maximin switches to leave."),
            ("Reading a rule's verdict as the verdict",
             "Each rule answers a question about the table: what is the worst, what "
             "is the best, what is the biggest shortfall. The same table can answer "
             "differently, as `disagree` does. A choice defended by a rule is "
             "defended by the attitude the rule carries."),
            ("Using these rules when the probabilities are in fact known",
             "Maximin ignores a state however unlikely it is. If you know rain has a "
             "one-in-a-thousand chance, planning only for it throws away what you "
             "know, and the next lesson's rule uses it."),
        ],
        "standard": ("Finish when you can score one table three ways and name the disagreement.",
                     "Given a decision table, you should be able to compute the maximin "
                     "and maximax scores, build the regret table, apply minimax regret, "
                     "and say which rules agree and which part, with the state that "
                     "drives the difference."),
        "note": "The rule menu carries one rule for ignorance this lesson does not teach. Laplace weights every state equally and takes the best average, which makes it expected utility with the probabilities left at one over the number of states; it has its own place in Justice and Collective Choice, where the same menu is used for a different question. The rules after it need probabilities, and the next lesson is where they begin.",
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "expected-value-and-expected-utility",
        "title": "Expected Value and Expected Utility",
        "module": "Risk",
        "one_line": "Weight each payoff by the probability of its state, add, and take the largest.",
        "summary": (
            "When the states have probabilities, an act can be scored by the average "
            "of its payoffs weighted by those probabilities. That score is its "
            "expected utility, and the act with the largest score is the one the "
            "rule recommends. The probability at which two acts tie says how much "
            "the recommendation depends on your estimate."
        ),
        "key": [
            "EU(a) = Σ P(s)·u(a, s)   take the largest",
            "P(s): probability of state s",
            "u(a, s): payoff of act a in state s",
            "tie at p: solve EU(a) = EU(b) for p",
            "EU is a score, not a prediction",
        ],
        "key_label": "Weight, add, compare",
        "concepts_intro": (
            "The rules for ignorance used the table alone. Once the states have "
            "probabilities, the table can be summarised more finely."
        ),
        "concepts": [
            ("Expected utility is a weighted average",
             "Multiply each payoff in an act's row by the probability of its state "
             "and add the products. An act that pays 2 with probability 1/3 and 1 "
             "with probability 2/3 scores 4/3."),
            ("The score need not be a possible payoff",
             "4/3 is not a number the act can pay. It is a number for comparing acts, "
             "and it has a meaning only as a comparison."),
            ("The recommendation has a tipping point",
             "With two states, the probability at which two acts score equally "
             "divides the cases where one is recommended from those where the other "
             "is. Your estimate matters only if it is on the other side of that "
             "point."),
        ],
        "read_title": "Scoring acts by expected utility",
        "read_intro": "The umbrella with a probability of rain, then the tipping point.",
        "body": [
            ("p", "Knowledge and Evidence introduced credences: degrees of belief "
                  "that obey the laws of probability. Suppose your credence in rain "
                  "is 1/3, and so 2/3 in no rain. Those two numbers are the new "
                  "ingredient, and with them the umbrella table can be scored in "
                  "a way the rules for ignorance could not."),
            ("def", ("Expected utility",
                     "The <strong>expected utility</strong> of act `a` is the sum, over "
                     "states `s`, of the probability of the state times the payoff of "
                     "`a` in it: `EU(a) = Σ P(s)·u(a, s)`. The rule recommends an act "
                     "with the largest expected utility.")),
            ("p", "For take, the weighted sum is 2·(1/3) + 1·(2/3) = 4/3. For leave "
                  "it is (−3)·(1/3) + 3·(2/3) = 1. Take scores higher, so at a "
                  "credence of 1/3 in rain the rule recommends the umbrella, which is "
                  "the verdict maximin and minimax regret also gave."),
            ("p", "The number 4/3 deserves a closer look, because the word "
                  "&ldquo;expected&rdquo; misleads. No single outing with the umbrella "
                  "pays 4/3; it pays 2 or 1. The figure is what the average would be "
                  "if the same decision were faced many times with the same odds. For "
                  "one decision it is a score, a number that ranks acts by weighing "
                  "every state in proportion to how likely you think it is. That is "
                  "the whole claim of the rule, and it is a substantial one."),
            ("thm", ("The tipping point",
                     "With two states, let `p` be the probability of the first. Each act's "
                     "score is a straight line in `p`, so the two lines cross at one "
                     "value, and the recommendation changes only there.")),
            ("p", "For the umbrella, let `p` be the probability of rain. Take scores "
                  "2·p + 1·(1 − p) = 1 + p and leave scores (−3)·p + 3·(1 − p) = "
                  "3 − 6·p. They tie when 1 + p = 3 − 6·p, that is when 7·p = 2, so "
                  "`p = 2/7`. Above 2/7 the umbrella is recommended and below it the "
                  "act of leaving is. The lab prints that figure as the point where "
                  "the expected utilities tie."),
            ("p", "The tipping point is the most useful number in the lab, because it "
                  "separates two questions. How likely is rain is a question about "
                  "the world; whether the answer matters is a question about the "
                  "table. If you are sure rain is more likely than 2/7, your exact "
                  "estimate is irrelevant to what to do."),
            ("example", ("A fair bet",
                         "Win 1 or lose 1 with probability 1/2 each, against not "
                         "betting at all. Betting scores 1·(1/2) + (−1)·(1/2) = 0 and "
                         "not betting scores 0. The two tie, and the tipping point "
                         "is p = 1/2. A bet is worth taking when your probability of "
                         "winning is above that.")),
            ("p", "The `lottery-ticket` preset is the same comparison with the odds "
                  "moved. A ticket costing 1 pays 500 if it wins, so buying scores "
                  "499 with probability 1/1000 and minus 1 otherwise, which comes to "
                  "499/1000 − 999/1000 = −1/2, against 0 for skipping. The lab "
                  "recommends skipping and prints the tie at a probability of "
                  "winning of 1/500, which is where the prize is exactly the odds "
                  "against it. Only above that is buying recommended, and a lottery "
                  "that sold tickets there would be paying out more than it took in."),
            ("p", "One caution. The payoffs in the table are utilities, numbers "
                  "that stand for how much you value each outcome, and for money "
                  "amounts the two can come apart. The next lesson takes the "
                  "difference up. Here the payoffs are taken as utilities from the "
                  "start, so there is nothing to convert."),
        ],
        "lab": ("choicekit", {
            "mode": "decide", "rule": "eu",
            "preset": "umbrella-p",
            "presets": [
                {"id": "umbrella-p", "label": "umbrella, rain at 1/3",
                 "acts": ["take", "leave"], "states": ["rain", "dry"],
                 "payoffs": [[2, 1], [-3, 3]], "probs": ["1/3", "2/3"], "expect": {"deChoice": "take", "deValue": "4/3", "deFlip": "p(rain) = 2/7"}},
                {"id": "bet", "label": "a fair bet against not betting",
                 "acts": ["bet", "decline"], "states": ["win", "lose"],
                 "payoffs": [[1, -1], [0, 0]], "probs": ["1/2", "1/2"], "expect": {"deChoice": "bet, decline", "deValue": "0", "deFlip": "p(win) = 1/2"}},
                {"id": "lottery-ticket", "label": "a ticket costing 1 that pays 500",
                 "acts": ["buy", "skip"], "states": ["win", "lose"],
                 "payoffs": [[499, -1], [0, 0]], "probs": ["1/1000", "999/1000"], "expect": {"deChoice": "skip", "deValue": "0", "deFlip": "p(win) = 1/500"}},
            ],
            "panel_title": "Change a probability and find where the choice flips",
            "panel_intro": "Each preset ships with its probabilities filled in. On the umbrella, change the probabilities from 1/3 and 2/3 to 1/5 and 4/5: the act recommended switches to leave. The last tile prints the probability at which the two best acts tie, so you can check that 1/5 is below it and 1/3 above. A text box that does not parse, or probabilities that do not add to 1, are refused with a message and not repaired.",
        }),
        "steps_title": "Scoring an act and finding the tipping point",
        "steps_intro": "Four steps. The last two apply only when there are two states.",
        "steps": [
            ("Check the probabilities",
             "One per state, none negative, summing to 1. A table whose "
             "probabilities do not sum to 1 describes some other problem."),
            ("Multiply across each row",
             "Pair every payoff with the probability of its column and multiply. "
             "Keep the fractions; rounding early moves a tie."),
            ("Add and compare",
             "The sum is the act's expected utility. The act with the largest "
             "sum is recommended, and a tie means the rule does not choose."),
            ("Solve for the tie",
             "With two states write each score as a function of `p`, set them "
             "equal and solve. The answer tells you how wrong your estimate can be "
             "before the choice changes."),
        ],
        "worked": {
            "title": "The umbrella at one chance in three, and its tipping point",
            "intro": [
                "Take pays 2 in rain and 1 when dry; leave pays −3 and 3. The "
                "probability of rain is p."
            ],
            "lines": [
                "p = 1/3",
                "EU(take)  = 2·(1/3) + 1·(2/3) = 4/3",
                "EU(leave) = -3·(1/3) + 3·(2/3) = 1",
                "take is recommended at p = 1/3",
                "general p:   1 + p = 3 - 6·p",
                "7·p = 2,   p = 2/7",
            ],
            "after": [
                "The credence 1/3 is above 2/7, so the umbrella wins, but not by "
                "much: only 1/21 of probability separates them. A forecaster who "
                "revised rain from 1/3 to 1/5 would reverse the advice."
            ],
        },
        "quiz_title": "Scoring by probability",
        "quiz": [
            {"q": "Take pays 2 in rain and 1 when dry; leave pays −3 and 3. Rain has "
                  "probability 1/3. What is the expected utility of leaving?",
             "a": ["0", "1", "4/3", "−1"],
             "c": 1,
             "why": "(−3)·(1/3) + 3·(2/3) = −1 + 2 = 1. The value 4/3 is the "
                    "score of taking, not leaving. Zero and −1 come from adding "
                    "only one of the two terms."},
            {"q": "At what probability of rain do take and leave have equal expected "
                  "utility?",
             "a": ["1/3", "1/2", "1/7", "2/7"],
             "c": 3,
             "why": "Setting 1 + p = 3 − 6·p gives 7·p = 2, so p = 2/7. At 1/3 take is "
                    "ahead, 4/3 against 1; at 1/2 it is further ahead, 3/2 against 0; "
                    "at 1/7 leave is ahead."},
            {"q": "What does it mean that the expected utility of taking is 4/3?",
             "a": ["It is a weighted average of the payoffs, used as a score to compare acts",
                   "It is the payoff you will receive if you take the umbrella",
                   "It is the payoff you will receive if the more likely state occurs",
                   "It is the payoff of the second-best act"],
             "c": 0,
             "why": "The score is a probability-weighted average, and no single "
                    "outcome need equal it. Taking pays 2 or 1, never 4/3. The "
                    "more likely state, dry, pays 1 for take. The second-best act is "
                    "leave, which scores 1."},
        ],
        "mistakes": [
            ("Reading expected value as the value you expect",
             "The expected utility of taking the umbrella is 4/3, and no outcome of "
             "taking it is worth 4/3: it pays 2 or 1. The figure is an average, "
             "weighted by probability, that ranks the acts. It is not a forecast of "
             "what will happen on this occasion, and acting on it does not promise "
             "a result near it."),
            ("Treating the probability as a fact rather than an estimate",
             "The 1/3 is your credence, and the tipping point of 2/7 shows how much "
             "room it has: a credence of 1/5 reverses the advice. Report the "
             "recommendation together with the tipping point."),
            ("Expecting a tie to mean the choice does not matter",
             "At the tipping point the two scores are equal, so the rule is silent, "
             "but the payoffs still differ state by state. Which one you take "
             "decides what you get in rain and in sun, and indifference between "
             "the averages is not indifference between the outcomes."),
        ],
        "standard": ("Finish when you can score two acts and say where the choice flips.",
                     "Given a table and a probability for each state, you should be "
                     "able to compute each act's expected utility, name the act the rule "
                     "recommends, and for two states solve for the probability at "
                     "which the recommendation changes."),
        "note": "The payoff numbers are inputs: the lab scores the table you give it and cannot tell you that a soaking is worth minus 3. “Risk Aversion and the Value of Information” is where the difference between a sum of money and its worth to you is made explicit.",
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "risk-aversion-and-the-value-of-information",
        "title": "Risk Aversion and the Value of Information",
        "module": "Risk",
        "one_line": "A concave utility makes a sure thing beat a fair gamble, and prices what a forecast is worth.",
        "summary": (
            "Expected utility scores utilities, not sums of money, and when utility "
            "rises more slowly than wealth a sure amount can beat a fair gamble on "
            "the same average. The same machinery prices a perfect forecast as the "
            "expected best payoff minus the best expected payoff, which is the most "
            "any forecast can be worth."
        ),
        "key": [
            "u(wealth) rises, but ever more slowly",
            "fair bet: average money the same, EU lower",
            "refusing a fair bet can be consistent",
            "VPI = expected best − best expected",
            "no forecast is worth more than the VPI",
        ],
        "key_label": "Utility is not money",
        "concepts_intro": (
            "Two ideas share one mechanism: what a payoff is worth is a separate fact "
            "from how large it is, and what knowing the state is worth comes out of "
            "the same table."
        ),
        "concepts": [
            ("Utility can be concave in money",
             "The first thousand is worth more to you than the ten-thousandth. "
             "When each extra unit adds less, the utility curve bends, and averaging "
             "over outcomes then gives less than the utility of the average."),
            ("A fair bet is fair in money only",
             "A coin flip for plus or minus 96 around 100 has the same average "
             "wealth as keeping 100. In utility, with a concave curve, it has a "
             "lower average, so the sure thing wins."),
            ("Information is worth the gain from acting on the state",
             "Learning the state before you choose lets you take the best act in "
             "each state. The value of perfect information is the expected best "
             "payoff minus the best expected payoff."),
        ],
        "read_title": "A curve that bends, and a forecast with a price",
        "read_intro": "First why a fair gamble can be refused, then how much a forecast is worth.",
        "body": [
            ("p", "A fair bet is one whose average gain is zero. A person who has "
                  "expected utility as their rule, and scores money at face value, "
                  "would be indifferent to a fair bet, so refusing it would be a mistake. "
                  "That is a consequence of scoring money at face value and not of "
                  "expected utility itself, which scores utilities."),
            ("def", ("Risk aversion",
                     "A chooser is <strong>risk averse</strong> when she prefers a "
                     "sure amount to a gamble with the same average amount. With "
                     "expected utility, this holds exactly when the utility of wealth "
                     "is concave: it rises, but each extra unit adds less.")),
            ("p", "Take utility equal to the square root of wealth. Wealth 100 has "
                  "utility 10, wealth 196 has utility 14 and wealth 4 has utility 2. "
                  "A coin flip between 196 and 4 averages 100, the same as keeping 100 "
                  "for sure. Its expected utility is 14·(1/2) + 2·(1/2) = 8, which "
                  "is below the 10 of keeping. The `fair-gamble` preset enters "
                  "exactly these utilities, and the rule prefers to keep. The flip tile shows "
                  "how far the coin would have to be bent: gambling wins only when heads "
                  "has probability above 2/3."),
            ("p", "There is nothing irrational in that preference unless the utility "
                  "of money is a straight line, and nothing in expected utility "
                  "requires that. What expected utility does require is that one set "
                  "of utilities explains all the choices, a demand “The Allais "
                  "Paradox and the Sure-Thing Principle” puts to the test."),
            ("example", ("Insurance",
                         "Wealth is 100 and a fire, with probability 1/4, would cost "
                         "75. Cover costs 19. Insured, you hold 81 whatever happens, "
                         "utility 9. Uninsured you hold 100, utility 10, or 25, "
                         "utility 5. Insuring scores 9 and risking scores 10·(3/4) + "
                         "5·(1/4) = 35/4 = 8.75, so insuring wins.")),
            ("p", "That example is worth a second look: the cover costs 19 and the "
                  "expected loss is 18.75, so in money the policy is slightly "
                  "unfavourable. It is still worth buying, because the lost 75 comes "
                  "out of a smaller pot, where each unit is worth more to you. A "
                  "risk-neutral chooser, scoring money at face value, would decline. "
                  "The `insurance` preset enters the utilities and the lab recommends "
                  "insuring, and its last tile says the cover is worth buying "
                  "whenever the chance of fire is above 1/5."),
            ("def", ("Value of perfect information",
                     "Let the <em>best expected</em> payoff be the highest expected "
                     "utility of any act now. Let the <em>expected best</em> be the "
                     "average, over states, of the best payoff available in each state. "
                     "Their difference is the <strong>value of perfect "
                     "information</strong>.")),
            ("p", "On the umbrella with rain at 1/3, take is best in rain at 2 and "
                  "leave is best when dry at 3. The expected best is 2·(1/3) + "
                  "3·(2/3) = 8/3. The best expected is 4/3, from take. So a "
                  "forecast that never misses is worth 4/3 in the same units as "
                  "the payoffs."),
            ("p", "The figure is a ceiling. A forecast that is sometimes wrong gives "
                  "less than a perfect one, so no forecast is worth more than 4/3 "
                  "here, and paying more for one is a mistake whatever it promises. "
                  "If one act is best in every state, nothing can be gained by "
                  "knowing the state and the value is zero."),
        ],
        "lab": ("choicekit", {
            "mode": "decide", "rule": "eu",
            "preset": "insurance",
            "presets": [
                {"id": "insurance", "label": "insure at 19, fire at 1/4, in utilities",
                 "acts": ["insure", "risk"], "states": ["fire", "no fire"],
                 "payoffs": [[9, 9], [5, 10]], "probs": ["1/4", "3/4"], "expect": {"deChoice": "insure", "deVpi": "3/4", "deFlip": "p(fire) = 1/5"}},
                {"id": "fair-gamble", "label": "a fair coin flip, 196 or 4, against keeping 100",
                 "acts": ["keep", "gamble"], "states": ["heads", "tails"],
                 "payoffs": [[10, 10], [14, 2]], "probs": ["1/2", "1/2"], "expect": {"deChoice": "keep", "deVpi": "2", "deFlip": "p(heads) = 2/3"}},
                {"id": "vpi", "label": "the umbrella with rain at 1/3",
                 "acts": ["take", "leave"], "states": ["rain", "dry"],
                 "payoffs": [[2, 1], [-3, 3]], "probs": ["1/3", "2/3"], "expect": {"deChoice": "take", "deVpi": "4/3"}},
            ],
            "panel_title": "Utilities in, values out",
            "panel_intro": "The payoff columns in the first two presets are utilities, the square roots of the wealth in the example, so the lab never sees the money. Change both 9s in the insurance table to 8, as if cover cost more, and watch the recommendation turn to risk. The third tile is the value of perfect information, computed from whatever table and probabilities are in the boxes.",
        }),
        "steps_title": "Pricing a risk and a forecast",
        "steps_intro": "Convert to utilities first. Everything after that is the arithmetic of the last lesson.",
        "steps": [
            ("Turn outcomes into utilities",
             "Apply the utility curve to each wealth level before averaging. "
             "Averaging the money and converting afterwards gives a different, and "
             "wrong, answer."),
            ("Score each act by expected utility",
             "Weight utilities by the state probabilities and add. Compare the sure "
             "act with the gamble."),
            ("Find the best payoff in each state",
             "Look down each column for its highest entry and average these "
             "by the state probabilities. That is the expected best."),
            ("Subtract the best expected",
             "Take the larger expected utility from the previous step away from "
             "the expected best. The remainder is the most any forecast could "
             "be worth."),
        ],
        "worked": {
            "title": "What a perfect forecast of rain is worth",
            "intro": [
                "Take pays 2 in rain and 1 when dry; leave pays −3 and 3. Rain has "
                "probability 1/3."
            ],
            "lines": [
                "best in rain: take, 2        best when dry: leave, 3",
                "expected best    = 2·(1/3) + 3·(2/3) = 8/3",
                "EU(take)  = 4/3        EU(leave) = 1",
                "best expected    = 4/3",
                "value of perfect information = 8/3 - 4/3 = 4/3",
            ],
            "after": [
                "Without the forecast you take the umbrella and score 4/3. With it, "
                "you take the umbrella in rain and leave it when dry and score 8/3. "
                "The forecast is worth the difference, in the units of the payoffs, "
                "and an honest seller cannot charge more for a perfect one."
            ],
        },
        "quiz_title": "Concave utility and the price of knowing",
        "quiz": [
            {"q": "How can an expected-utility maximiser refuse a fair bet without "
                  "contradicting the rule?",
             "a": ["Expected utility does not apply to bets",
                   "She has miscalculated the average money",
                   "The utility of the average wealth exceeds the average of the "
                   "utilities when utility is concave",
                   "The probabilities are not really one half"],
             "c": 2,
             "why": "With a concave utility, the sure 100 scores more than the "
                    "even chance of 196 or 4. Expected utility applies to bets like any "
                    "other act, the average money is the same by construction, and "
                    "the bet is stipulated fair."},
            {"q": "The value of perfect information on the umbrella is 4/3. What does "
                  "that tell you?",
             "a": ["No forecast, perfect or not, is worth more than 4/3 in these units",
                   "Every forecast is worth exactly 4/3",
                   "The forecast raises the probability of rain by 4/3",
                   "Taking the umbrella is worth 4/3, so information is worthless"],
             "c": 0,
             "why": "A perfect forecast is the best possible, so 4/3 is the ceiling. "
                    "An imperfect forecast is worth less than the perfect one, which "
                    "rules out the second choice. Information changes what you "
                    "know, not the probability of rain. That take scores 4/3 "
                    "without a forecast is a coincidence of the numbers, and does not "
                    "make information worthless."},
            {"q": "In the insurance example the cover costs 19 and the expected loss is "
                  "18.75, yet insuring wins. What explains it?",
             "a": ["The table must contain an error",
                   "The insurer must be mispricing the cover",
                   "Expected utility is the wrong rule for insurance",
                   "A loss of 75 comes out of a smaller pot where each unit is worth "
                   "more, so the sure payment is worth its small excess"],
             "c": 3,
             "why": "With utility equal to the square root of wealth, insuring "
                    "scores 9 against 8.75. The numbers are correct as stated, and "
                    "the price being above the expected loss in money is exactly what "
                    "risk aversion allows. Expected utility is the rule that "
                    "produces the result."},
            {"q": "The value of perfect information is expected best minus best "
                  "expected. Which statement is true of it?",
             "a": ["It can be negative if the forecast is wrong",
                   "It is zero when one act is best in every state",
                   "It is always strictly positive",
                   "It is the probability that the forecast turns out right"],
             "c": 1,
             "why": "If one act is best in every state, the expected best equals the "
                    "best expected and the difference is zero. It is never negative, "
                    "because an average of column maxima is at least any one act's "
                    "average, and so it is not always strictly positive either. And "
                    "it is a difference of two scores, in the units of the payoffs; "
                    "a perfect forecast is right every time, and its value is still "
                    "4/3 on the umbrella and 0 when one act wins everywhere."},
        ],
        "mistakes": [
            ("Calling the refusal of a fair bet irrational",
             "Fair means the average money is zero, and expected utility averages "
             "utility, not money. With the square root of wealth the coin flip "
             "between 196 and 4 scores 8 and keeping 100 scores 10, so refusing is "
             "what the rule recommends. It would be a mistake only if the utility of "
             "money were a straight line, and nothing requires that."),
            ("Averaging the money and then converting to utility",
             "The utility of the average is not the average of the utilities. Convert "
             "each outcome first. Doing it the other way round erases the curvature "
             "that the whole example turns on."),
            ("Paying for a forecast because it is accurate",
             "A forecast is worth what acting on it gains, and no more than the "
             "perfect-information figure. If one act wins in every state, an accurate "
             "forecast is worth nothing, since you would choose the same act "
             "whatever it said."),
        ],
        "standard": ("Finish when you can show a sure thing beating a fair gamble and price a forecast.",
                     "Given a utility curve and a gamble, you should be able to compute "
                     "both expected utilities and say which wins. Given a table "
                     "with probabilities, you should be able to compute the expected "
                     "best, the best expected, and the value of perfect information."),
        "note": "The curve used here, the square root, is one choice among many concave curves, and the lab does not choose it for you. A different curve gives different numbers and the same shape of result. Every utility in this lesson is a number somebody chose.",
    },
]
