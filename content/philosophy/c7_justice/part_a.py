"""Justice and Collective Choice, lessons 1-5: distributive justice, and the first lesson on collective choice.

Every figure the prose states is one the lab prints; the presets pin the tiles
that say why each preset exists (scripts/mathpath/AGENTS.md, "a preset's two
claims").
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "the-original-position-and-maximin",
        "title": "The Original Position and Maximin",
        "module": "Distributive justice",
        "one_line": "Choose a society without knowing which place in it will be yours, and the rule you choose with decides the society.",
        "summary": (
            "Rawls asks which society people would pick if they did not know who they would be in it. Laid out as a decision "
            "matrix, with the chooser's position as the unknown state, the question becomes a choice of rule: maximin picks one "
            "society and equal-probability expected utility picks another from the very same table. "
            "The wrong model is that maximin is a taste for safety with money."
        ),
        "key": [
            "unknown state: which place will be yours",
            "maximin: take the best worst case",
            "Laplace: weigh every place equally",
            "same table, two rules, two societies",
        ],
        "key_label": "One table, two rules",
        "concepts_intro": (
            "The original position is a thought experiment, and a decision matrix is the form in which its argument can be checked. "
            "Three ideas carry the lesson."
        ),
        "concepts": [
            ("The position is the state",
             "Each society is an act. What the chooser does not know is which place in it will fall to them, so each place is a "
             "state, and the cell holds how well that place does in that society. The table is the one from Decision and Rationality "
             "with the unknown moved from the weather to oneself."),
            ("Maximin looks only at the worst place",
             "Maximin scores a society by the lowest entry in its row and takes the society whose lowest entry is highest. "
             "It never adds, averages or weighs, so the probabilities of the places play no part in it."),
            ("Equal chances is a different rule",
             "Laplace's rule treats every place as equally likely and scores a society by its average. Harsanyi argued that this, "
             "and not maximin, is what a rational chooser behind the veil would do. The two rules are the two sides of the dispute."),
        ],
        "read_title": "Choosing a society from behind the veil",
        "read_intro": "A table with societies down the side and places across the top, and two rules applied to it.",
        "body": [
            ("p", "Suppose you must pick the arrangement of a society, and you must do it before learning which place in it "
                  "you will occupy. You might be among the worst off, in the middle, or among the best off. "
                  "Rawls called the situation of such a chooser the <strong>original position</strong>, and the "
                  "ignorance of one's own place the <strong>veil</strong>. What he claimed is that principles chosen under "
                  "the veil are fair, because no one can tailor them to their own advantage."),
            ("p", "The argument is only worth testing if it can be written down, and it can. Take two societies, one in which "
                  "everyone has `5` units of welfare and one in which the worst place has `2`, the middle `8` and the best `20`. "
                  "The unknown is your place, so the table has three states."),
            ("math", [
                "                 bottom    middle    top",
                "     equal          5         5        5",
                "     unequal        2         8       20",
            ]),
            ("p", "Maximin reads off each society's worst entry: `5` for the equal society and `2` for the unequal one. "
                  "The larger worst case is `5`, so maximin chooses the equal society. Nothing about the `8` or the `20` entered "
                  "the calculation."),
            ("p", "Now give each place the same chance, as Laplace's rule does. The equal society averages `5`, and the unequal one "
                  "averages `(2 + 8 + 20) / 3`, which is `10`. The larger average is `10`, so this rule chooses the unequal "
                  "society. Same table, same chooser, opposite verdicts, and the difference lies wholly in what the rule "
                  "is willing to ignore."),
            ("def", ("Maximin",
                     "<strong>Maximin</strong> scores each act by its worst payoff across the states and chooses the act "
                     "whose worst payoff is largest.")),
            ("h3", "What the rule choice is about"),
            ("p", "Rawls's case for maximin is not that people dislike risk. It is that the choice has three features: the chooser "
                  "has no trustworthy basis for assigning probabilities to the places, the chooser cares little for what is gained "
                  "above the guaranteed minimum, and the worst outcome of a rejected society would be one hardly bearable. "
                  "Where those hold, looking only at the floor is a reasonable policy. Where they do not, for instance when the "
                  "stakes are small and the odds are known, it is a poor one."),
            ("p", "Harsanyi's reply denies the first feature. A chooser who knows nothing about their place has, he argued, "
                  "no reason to favour any place over another, and equal weights are what that ignorance amounts to. "
                  "Each side states a valid argument from its premises; the lab computes both and cannot say whether the "
                  "veil should leave you with no probabilities or with equal ones. That is the question the lesson leaves with you."),
            ("p", "The lab's second table carries one more figure. With each place at probability `1/3` the value-of-information "
                  "tile prints `1`, and here that quantity has a name: it is the value of lifting the veil. A chooser who learned "
                  "their place before choosing would take the equal society in the bottom place, where it pays `5` against `2`, "
                  "and the unequal society anywhere else, for an expectation of `(5 + 8 + 20) / 3`, which is `11`; the best "
                  "a chooser can do without that knowledge is `10`. The difference, `1`, is what knowing one's own place "
                  "would be worth to the chooser. The veil withholds exactly that, and withholds it from everyone, which is "
                  "what makes a choice made behind it fair on Rawls's account."),
            ("example", ("A close call",
                         "In the lab's third table the unequal society pays `5`, `6` and `7` against `5`, `5` and `5`. "
                         "Maximin finds the same worst case, `5`, in both rows and cannot separate them, while the average "
                         "separates them at once, `6` against `5`. A tie under maximin is a signal that the rule has run out "
                         "of information, which is where the next lesson begins.")),
            ("p", "One limit belongs here. The numbers are welfare levels the table's author chose, and the societies are two among "
                  "the many that could have been offered. The lab computes what each rule picks from the table as stated; "
                  "it does not tell you that the table describes any real society."),
        ],
        "lab": ("choicekit", {
            "mode": "decide", "rule": "maximin",
            "preset": "rawls",
            "presets": [
                {"id": "rawls", "label": "Equal 5, 5, 5 against unequal 2, 8, 20",
                 "acts": ["equal", "unequal"], "states": ["bottom", "middle", "top"],
                 "payoffs": [[5, 5, 5], [2, 8, 20]], "expect": {"deChoice": "equal", "deValue": "5"}},
                {"id": "harsanyi", "label": "The same table, each place at probability 1/3",
                 "acts": ["equal", "unequal"], "states": ["bottom", "middle", "top"],
                 "payoffs": [[5, 5, 5], [2, 8, 20]], "probs": ["1/3", "1/3", "1/3"], "expect": {"deVpi": "1"}},
                {"id": "close-call", "label": "Equal 5, 5, 5 against unequal 5, 6, 7",
                 "acts": ["equal", "unequal"], "states": ["bottom", "middle", "top"],
                 "payoffs": [[5, 5, 5], [5, 6, 7]], "expect": {"deChoice": "equal, unequal", "deValue": "5"}},
            ],
            "panel_title": "Choose a society, then change the rule",
            "panel_intro": "The rule is shipped as maximin. Switch it to Laplace and the same table gives the other verdict; "
                           "with the probabilities box filled in, expected utility and the value of information also work.",
        }),
        "steps_title": "Running the original position as a table",
        "steps_intro": "Five moves, and the second one is where the philosophy sits.",
        "steps": [
            ("List the societies as acts",
             "Each society on offer is a row. Keep the list short and make sure each row really is a complete arrangement."),
            ("Let the places be the states",
             "A place is something you might turn out to occupy. Whether the places should carry probabilities, equal or "
             "otherwise, is the contested premise, so leave it open for now."),
            ("Fill each cell with the welfare of that place in that society",
             "Use one scale throughout. The verdicts are verdicts about these numbers, and a different scale is a different table."),
            ("Apply maximin",
             "Underline the lowest entry in each row and choose the row whose underlined entry is highest. A tie means the rule "
             "has no verdict between those rows."),
            ("Apply the average and compare",
             "Average each row. If the two rules choose differently, the dispute between them is the dispute about the veil, "
             "and neither the table nor the lab settles it."),
        ],
        "worked": {
            "title": "Two rules on the same two societies",
            "intro": ["The table has equal at 5, 5, 5 and unequal at 2, 8, 20. Score each row twice."],
            "lines": [
                "equal      5   5    5    worst 5    average 5",
                "unequal    2   8   20    worst 2    average 10",
                "maximin:   best of 5 and 2    -> equal",
                "Laplace:   best of 5 and 10   -> unequal",
            ],
            "after": [
                "The rules differ about one thing: whether a gain of `15` at the top can make up for a loss of `3` at the "
                "bottom. Maximin says it never can. Laplace says it can, here by a wide margin. Nothing in the arithmetic "
                "says which of them is describing fairness.",
            ],
        },
        "quiz_title": "Two rules, one table",
        "quiz": [
            {"q": "In the lab's first table the equal society pays 5, 5, 5 and the unequal pays 2, 8, 20. What does maximin choose, and why?",
             "a": ["The unequal society, because its best place pays 20",
                   "The unequal society, because its average is 10",
                   "The equal society, because its worst place pays 5 against 2",
                   "Neither, because the places have no probabilities"],
             "c": 2,
             "why": "Maximin compares worst entries, 5 against 2, and takes the larger. The first two describe the best case and the "
                    "average, which are other rules' scores. The last confuses maximin with expected utility: maximin is the rule "
                    "that works when there are no probabilities."},
            {"q": "What does maximin do with the probabilities of the places?",
             "a": ["Nothing: its score is each society's lowest entry, whatever the probabilities are",
                   "It multiplies each entry by its probability and sums",
                   "It uses them only to choose between societies with equal worst entries",
                   "It requires them to be equal"],
             "c": 0,
             "why": "The score is the row minimum. Multiplying and summing is expected utility. Using probabilities to settle ties "
                    "is a different rule, and requiring equal ones is Laplace's assumption, not maximin's."},
            {"q": "The close-call table pays 5, 5, 5 against 5, 6, 7 and maximin lists both societies. What does the tie show?",
             "a": ["That the societies are equally good in every place",
                   "That the lab failed to compute the average",
                   "That the average rule also ties them",
                   "That the rule sees only the worst entry, and the worst entries are equal"],
             "c": 3,
             "why": "Both rows have minimum 5, so maximin cannot separate them, though the second pays more in two places. "
                    "The averages are 5 and 6, so the average rule does not tie them."},
            {"q": "Which grounds does Rawls give for choosing by maximin in the original position?",
             "a": ["People are risk-averse about money, so they dislike gambles",
                   "The chooser has no trustworthy probabilities and the worst case would be hardly bearable",
                   "The chooser expects to be the worst off",
                   "Maximin always maximises the average welfare"],
             "c": 1,
             "why": "Rawls's grounds are about the chooser's information and the stakes of the worst case. Risk aversion about "
                    "money is not among them. Expecting to be worst off contradicts the veil, and in the first table maximin "
                    "gives up an average of 10 for 5."},
        ],
        "mistakes": [
            ("Thinking Rawls assumes people are risk-averse about money",
             "Maximin is a rule for choosing when the probabilities are not available, and it never uses the size of the "
             "other entries. A chooser who valued each unit of welfare equally would still be told by maximin to prefer 5, 5, 5 "
             "to 2, 8, 20, because the rule does not add. Risk aversion would be a feature of the numbers in the table, "
             "if a utility curve had shaped them. The argument for maximin is about the chooser's ignorance and the "
             "cost of the worst case."),
            ("Reading the veil as ignorance of everything",
             "The chooser knows the table: what each society pays in each place. What they lack is their own place. "
             "Take the table away and neither rule has anything to compute, and take the veil away and the choice "
             "becomes self-interest. The argument needs exactly this much ignorance."),
            ("Taking a tie under maximin for equality",
             "Equal worst entries mean only that the rule finds no difference at the bottom. The close-call table has "
             "different societies with the same floor, and a rule that looks past the floor can tell them apart."),
        ],
        "standard": ("Finish when you can lay a choice of society out as a table and say what each rule picks from it.",
                     "Given two societies and three places, build the matrix, compute the worst entry and the average of each row, "
                     "name the society each rule chooses, and say which premise about the veil the disagreement turns on."),
        "note": "The lab's Laplace and expected-utility rules need no extra work once the probabilities box is filled in. "
                "Try making the bottom place much more likely than the other two, say `4/5`, `1/10` and `1/10`, and watch the "
                "verdict of the expected-utility rule move to the equal society, `5` against `22/5`, while maximin stays where "
                "it was. That is the whole difference between the two kinds of rule.",
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "the-difference-principle-and-leximin",
        "title": "The Difference Principle and Leximin",
        "module": "Distributive justice",
        "one_line": "An inequality is allowed only if it raises the position of the worst off, and ties at the bottom are settled one place up.",
        "summary": (
            "The difference principle ranks distributions by their worst-off member, then by the next worst when the first "
            "are tied, and so on. An unequal distribution that lifts the bottom beats an equal one that does not. "
            "The wrong model is that the principle demands equality."
        ),
        "key": [
            "compare the worst-off first",
            "tied there? compare the next worst",
            "raising the floor beats equal shares",
            "the principle allows inequality that pays",
        ],
        "key_label": "Leximin, step by step",
        "concepts_intro": (
            "The previous lesson ended on a tie at the bottom. Three ideas turn the maximin rule into a ranking."
        ),
        "concepts": [
            ("Sort, then compare from the bottom",
             "List each distribution from the worst-off up. Compare the first entries, and only if they are equal compare the "
             "second, and so on. The first difference decides. This is leximin, short for lexical maximin."),
            ("Inequality is permitted, on a condition",
             "The principle does not prefer unequal distributions. It permits an inequality if the worst-off are better off "
             "with it than with any alternative, and forbids it otherwise."),
            ("The justification is an argument about incentives",
             "The usual defence of an unequal distribution is that the prospect of higher rewards draws out effort and talent, "
             "and that the extra product reaches the bottom. That is a premise about how people behave, not an output of the rule."),
        ],
        "read_title": "Leximin on two distributions",
        "read_intro": "A rule that compares sorted lists, a case where it favours inequality, and a case where it does not.",
        "body": [
            ("p", "The second part of Rawls's second principle of justice, the <strong>difference principle</strong>, says that social and "
                  "economic inequalities are to be arranged so that they are to the greatest benefit of the least advantaged. "
                  "As a rule for comparing two distributions of welfare it comes to this: prefer the one in which the "
                  "worst-off person is better off. If their positions are the same, the person next up decides, and so on."),
            ("def", ("Leximin",
                     "<strong>Leximin</strong> ranks two distributions by sorting each from lowest to highest and comparing "
                     "them entry by entry from the bottom. The first position at which they differ decides, and the "
                     "distribution with the larger entry there is ranked higher.")),
            ("p", "Take the distributions `(5, 5, 5)` and `(6, 9, 20)`. Sorted, they are as they stand. The first entries are "
                  "`5` and `6`, and `6` is larger, so the second distribution is ranked higher. The `9` and the `20` are never "
                  "looked at. The same verdict would stand if the top entry were `20 000`, or if it were `7`."),
            ("p", "That is where the principle parts company with equality. A pure egalitarian prefers `(5, 5, 5)` to "
                  "`(6, 9, 20)` because it is level, and levelling is what they are after. The difference principle prefers the "
                  "second, because everyone is no worse off in it, and the worst-off are better. Preferring the first would "
                  "mean denying the worst-off a unit of welfare so that others would not have more than they do. "
                  "“Priority, Equality and Levelling Down” takes that cost as its subject."),
            ("p", "When the bottoms tie, leximin looks upward. Compare `(5, 8, 8)` with `(5, 6, 20)`. The first entries are "
                  "both `5`. The second entries are `8` and `6`, so the first distribution wins, even though the total of the "
                  "second is far larger. Maximin alone would have called the pair a tie; leximin finishes the job."),
            ("h3", "The incentive argument"),
            ("p", "Why would anyone choose the unequal distribution? The standard answer runs: if talented people are paid "
                  "more, they will do work that produces more for everyone, and some of that increase reaches the worst-off. "
                  "In the numbers, it is the step from `5` to `6` at the bottom that is bought by the `9` and the `20` above."),
            ("p", "This is an argument, and it has a premise the lab cannot check. If the high rewards do not in fact raise the "
                  "floor, the unequal distribution has nothing to recommend it, and leximin ranks it below an equal one "
                  "with the same bottom. The lab ranks the two vectors you type; whether the first caused the second is "
                  "what the philosophy is about."),
            ("example", ("When equality is the better answer",
                         "Suppose the unequal distribution is `(5, 8, 20)` and the equal one is `(5, 5, 5)`. The floors tie at `5`, "
                         "and the next entries are `8` and `5`, so leximin ranks the unequal one higher. Now suppose the "
                         "unequal distribution is `(4, 8, 20)`. The floor is lower, and leximin ranks the level one higher, "
                         "however large the top entry.")),
            ("p", "Three limits. Rawls applied the principle to the holdings of primary goods, such as income, rights and "
                  "opportunities, and not to a single scale of welfare; he took the worst-off to be a representative "
                  "group and not a named person; and he described the lexical form used here, which looks upward when the "
                  "floors tie, as a refinement his argument did not need, since he expected the position of the worst-off "
                  "to settle the cases that matter. The lab compares vectors of numbers, which is the cleanest form of the "
                  "rule and not the whole of his view."),
        ],
        "lab": ("choicekit", {
            "mode": "aggregate", "rule": "leximin",
            "preset": "incentive",
            "presets": [
                {"id": "incentive", "label": "Equal 5, 5, 5 against 6, 9, 20",
                 "A": [5, 5, 5], "B": [6, 9, 20], "expect": {"agVerdict": "B ≻ A", "agScores": "worst 5 vs 6"}},
                {"id": "tie-at-the-bottom", "label": "5, 8, 8 against 5, 6, 20",
                 "A": [5, 8, 8], "B": [5, 6, 20], "expect": {"agVerdict": "A ≻ B", "agScores": "2nd worst 8 vs 6"}},
                {"id": "pure-equality", "label": "6, 9, 20 against a level 4, 4, 4",
                 "A": [6, 9, 20], "B": [4, 4, 4], "expect": {"agVerdict": "A ≻ B", "agScores": "worst 6 vs 4"}},
            ],
            "panel_title": "Rank two distributions",
            "panel_intro": "A and B are lists of welfare levels, one entry per person. The rule is shipped as leximin; "
                           "switch it to total or maximin to see where the verdict moves.",
        }),
        "steps_title": "Ranking two distributions by leximin",
        "steps_intro": "Four moves. The only way to go wrong is to stop looking after the first entry when it ties.",
        "steps": [
            ("Sort each distribution from the lowest entry up",
             "Order matters in the comparison and the identity of the person does not. The lab sorts for you and shows the order."),
            ("Compare the first entries",
             "If one is larger, that distribution is ranked higher and the rest is irrelevant, however much larger the later "
             "entries are in the other."),
            ("If they tie, compare the second entries, then the third",
             "Move up one position at a time and stop at the first difference. If every entry matches, the distributions "
             "are ranked equal."),
            ("Ask what produced the numbers",
             "If an inequality is to be defended, say what it does for the bottom entry. The justification is a claim about "
             "incentives or output, and it is a premise of the argument and not a result of the ranking."),
        ],
        "worked": {
            "title": "Leximin on two pairs",
            "intro": ["First the case where the floor is raised, then the case where the floors tie."],
            "lines": [
                "A = 5, 5, 5      B = 6, 9, 20       first entries 5 < 6",
                "   B ranks above A, whatever the 9 and 20 are",
                "A = 5, 8, 8      B = 5, 6, 20       first entries 5 = 5",
                "   second entries 8 > 6, so A ranks above B",
            ],
            "after": [
                "In the second pair B has the larger total, `31` against `21`, and a total rule would choose it. "
                "Leximin does not add, so the larger total cannot buy a lower second entry.",
            ],
        },
        "quiz_title": "Reading a leximin verdict",
        "quiz": [
            {"q": "Why does leximin rank (6, 9, 20) above (5, 5, 5)?",
             "a": ["Its total is larger",
                   "It is more equal",
                   "The two are tied, since each has a person at 5 or above",
                   "Its worst-off entry, 6, is larger than 5"],
             "c": 3,
             "why": "Leximin compares the lowest entries first, 6 against 5, and that settles it. A larger total is the total "
                    "rule's reason, and the first distribution is the level one, not the second."},
            {"q": "Leximin compares (5, 8, 8) with (5, 6, 20). Where is the verdict decided?",
             "a": ["At the first entries, which are equal, so the distributions are tied",
                   "At the second entries, 8 against 6",
                   "At the last entries, 8 against 20",
                   "By the totals, 21 against 31"],
             "c": 1,
             "why": "The first entries tie, so the comparison moves up one place and stops at the first difference, 8 against 6. "
                    "Stopping at the tie would give the maximin verdict, and the last entries and the totals are never consulted."},
            {"q": "A defender of pure equality and a defender of the difference principle are offered a level (4, 4, 4) and (6, 9, 20). What does each prefer?",
             "a": ["The egalitarian prefers (4, 4, 4); the difference principle prefers (6, 9, 20)",
                   "Both prefer (6, 9, 20), because everyone is at least as well off",
                   "Both prefer (4, 4, 4), because it is the more equal",
                   "The difference principle prefers (4, 4, 4), because it has no one worse off than 4"],
             "c": 0,
             "why": "Pure equality ranks by level shape and chooses (4, 4, 4). The difference principle compares floors, 4 and 6, "
                    "and chooses (6, 9, 20). The last choice reads the floor backwards."},
            {"q": "What must the incentive argument establish if it is to justify (6, 9, 20) over (5, 5, 5)?",
             "a": ["That the people at the top deserve 20",
                   "That the higher rewards are what make the worst-off person's 6 possible",
                   "That the people at the top would produce just as much if paid 5",
                   "That the second distribution is more equal than the first"],
             "c": 1,
             "why": "The justification is that the inequality raises the floor. A claim about desert is a different argument, "
                    "and the second distribution is less equal, not more. The third is the claim the argument must deny: if "
                    "the same product came without the higher rewards, the inequality would be doing nothing for the floor."},
        ],
        "mistakes": [
            ("Thinking the difference principle demands equality",
             "It permits any inequality that leaves the worst-off better off than they would otherwise be. (6, 9, 20) "
             "beats (5, 5, 5) because 6 is more than 5, and the 9 and 20 count neither for nor against. Equality is the "
             "answer only when no inequality raises the floor."),
            ("Stopping at a tie in the first entry",
             "Equal floors do not make equal distributions. Compare (5, 8, 8) and (5, 6, 20): maximin finds a tie, "
             "and leximin goes on to the second entries and finds that 8 beats 6."),
            ("Reading the ranking as a defence of inequality",
             "The rule ranks the vectors it is given. That the unequal one has the higher floor is a premise somebody "
             "has to establish. If the high rewards did nothing for the bottom, the same rule would rank them below a level "
             "distribution with the same floor."),
        ],
        "standard": ("Finish when you can rank two distributions by leximin and say what an inequality has to do to be allowed.",
                     "Given two lists of welfare levels, sort them, find the first position at which they differ and name the "
                     "winner; then state, for an unequal winner, the claim about incentives that the verdict depends on."),
        "note": "Try a distribution whose lowest entry is zero and the others enormous: leximin ranks it below any "
                "distribution whose lowest entry is positive. That is the rule at its most uncompromising, and it is why "
                "critics ask whether a lexical priority is too strong.",
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "entitlement-patterns-and-the-gini-coefficient",
        "title": "Entitlement, Patterns and the Gini Coefficient",
        "module": "Distributive justice",
        "one_line": "A distribution can be judged by its shape or by how it arose, and a free exchange can change the first while respecting the second.",
        "summary": (
            "Nozick argued that justice in holdings depends on history, not pattern, and that any pattern is upset by free "
            "transfers. The Gini coefficient measures the shape, and a small exchange can be followed to the number it produces. "
            "The wrong model is that a just distribution is one with a just shape."
        ),
        "key": [
            "pattern: justice is a shape of holdings",
            "entitlement: justice is how they arose",
            "Gini: 0 for equal shares, higher for more gap",
            "a free transfer moves the Gini, wrongs no one",
        ],
        "key_label": "Shape against history",
        "concepts_intro": (
            "Two views of what makes a distribution just, and a number that lets the difference between them be seen."
        ),
        "concepts": [
            ("A pattern is a shape",
             "A patterned principle says holdings should be distributed according to some measure, such as equally or "
             "by need. Whether a distribution satisfies it can be read off the final list of holdings alone."),
            ("An entitlement is a history",
             "An historical principle says holdings are just if they were acquired justly and passed on by just transfers. "
             "Two identical lists of holdings can differ in justice if they arose differently."),
            ("Gini measures shape",
             "The Gini coefficient of “Priority, Equality and Levelling Down” is `0` when everyone holds the same and rises as the gaps between people grow. "
             "It is a measure of a pattern, and so it cannot by itself say whether a pattern is just."),
        ],
        "read_title": "Wilt Chamberlain and the number",
        "read_intro": "An exchange small enough to follow, a measure that tracks it, and the argument that grows out of both.",
        "body": [
            ("p", "Nozick's challenge to the theories of the previous two lessons is that they judge only the final list of "
                  "holdings. Suppose the list is the one you think just. Then people begin to spend what they have, freely, "
                  "on what they want, and the list changes. If the new list is not just, something wrong must have "
                  "happened in the exchanges. If nothing wrong happened, the new list is just, and a principle that "
                  "forbids it is forbidding the outcome of choices that nobody had a right to prevent."),
            ("p", "His example is a basketball player. Four people hold `10` units each. Three of them each pay `1` to "
                  "watch Wilt Chamberlain play, and he keeps what they pay. Afterwards three hold `9` and one holds `13`. "
                  "The total is still `40`, and the shares are no longer level."),
            ("def", ("Gini coefficient",
                     "For holdings `x` of `n` people with mean `m`, the <strong>Gini coefficient</strong> adds up the gap "
                     "between every ordered pair of people and divides by `2·n²·m`. It is `0` when all holdings are equal.")),
            ("p", "For the starting list, every gap is `0`, so the Gini is `0`. For the list after the game, each of the three "
                  "at `9` is `4` away from the person at `13`. There are three such pairs, counted in both orders, so the "
                  "gaps add up to `24`. The divisor is `2·16·10`, which is `320`. The Gini is `24 / 320`, which is `3/40`."),
            ("p", "That is Nozick's point as a number. A single round of voluntary payments moved the Gini from `0` to `3/40`, "
                  "and no one was wronged. To keep the Gini at `0` the state would have had to stop the payments, or "
                  "to take the money back, and either one is an interference with people who did nothing wrong. "
                  "Nozick concluded that liberty upsets patterns, and that a theory which wants a pattern must keep interfering."),
            ("example", ("Two rounds",
                         "If the same three pay again, they hold `8` each and Wilt holds `16`. The gaps are `8`, three pairs in "
                         "both orders gives `48`, and the Gini is `48 / 320`, which is `3/20`: twice the single-round figure. "
                         "A pattern is not stable under free exchange, and the lab shows the drift as a number.")),
            ("h3", "What the number does not show"),
            ("p", "Three replies deserve their strength. The first is about the premises: the argument assumes the starting "
                  "list was just and that every payment was free, and a critic asks what made the first list just and whether "
                  "a choice made under need is as free as the story imagines. The second is Rawls's own: the difference "
                  "principle is a standard for the rules of the basic structure, the law of property and taxation under which "
                  "people trade, and not a pattern to be restored after each exchange, so a tax on Chamberlain's receipts is "
                  "one of the rules the fans paid under and not an interference after the fact. The third is that the Gini "
                  "is not what every patterned theory is about: a theory that cares only about a floor is untouched by "
                  "payments made above it. Nozick's rejoinder to the second, that a tax on earnings is on a par with forced "
                  "labour, is where the dispute stands."),
            ("p", "Redistribution moves the number back. The lab's second table starts with holdings `(2, 4, 6, 28)`, whose "
                  "Gini is `1/2`, and ends with `(6, 8, 10, 16)`, whose Gini is `1/5`, with the total unchanged. The total rule "
                  "calls the two equal, since it only adds. Whether the move was just is the dispute between the two views, and "
                  "the number is the same under both of them."),
            ("p", "The lab measures shape. It does not know who paid whom, and a history is what the entitlement view is made of, "
                  "so no tile here can pass a verdict on it."),
        ],
        "lab": ("choicekit", {
            "mode": "aggregate", "rule": "total",
            "preset": "chamberlain",
            "presets": [
                {"id": "chamberlain", "label": "Level 10, 10, 10, 10 and after one round, 9, 9, 9, 13",
                 "A": [10, 10, 10, 10], "B": [9, 9, 9, 13], "expect": {"agGini": "0 vs 3/40", "agVerdict": "A ~ B"}},
                {"id": "redistribute", "label": "2, 4, 6, 28 and after a tax, 6, 8, 10, 16",
                 "A": [2, 4, 6, 28], "B": [6, 8, 10, 16], "expect": {"agGini": "1/2 vs 1/5", "agVerdict": "A ~ B"}},
                {"id": "two-rounds", "label": "Level 10, 10, 10, 10 and after two rounds, 8, 8, 8, 16",
                 "A": [10, 10, 10, 10], "B": [8, 8, 8, 16], "expect": {"agGini": "0 vs 3/20", "agVerdict": "A ~ B"}},
            ],
            "panel_title": "Compare holdings before and after",
            "panel_intro": "A is the list before, B the list after. The Gini tile prints A's coefficient first, then B's; "
                           "the verdict is shipped under the total rule, which sees only the sums.",
        }),
        "steps_title": "Measuring a transfer",
        "steps_intro": "Five moves, working from two lists of holdings to one number each.",
        "steps": [
            ("Write the holdings before and after",
             "Use one list per moment and the same people in the same order. The total should not change in an exchange."),
            ("Find the mean",
             "Add the holdings and divide by the number of people. Here it is `10` in every list."),
            ("Add the gap between every ordered pair",
             "Each pair of people counts twice, once in each order. Pairs with equal holdings contribute nothing."),
            ("Divide by twice the square of the count, times the mean",
             "For four people with mean `10` the divisor is `320`. The result runs from `0` for equal shares upward."),
            ("State what the number does and does not say",
             "It says the shape changed and by how much. Whether the change was unjust depends on how it came about, "
             "which is a fact about the history and not about the list."),
        ],
        "worked": {
            "title": "The Gini after one round",
            "intro": ["Four people at 10, then three of them pay 1 each to the fourth."],
            "lines": [
                "before   10  10  10  10     every gap 0       Gini 0",
                "after     9   9   9  13     3 pairs, gap 4",
                "ordered pairs counted twice: 3 x 4 x 2 = 24",
                "divisor 2 x 4 x 4 x 10 = 320",
                "Gini after = 24 / 320 = 3/40",
            ],
            "after": [
                "The total is `40` before and after, so a rule that adds holdings sees no change. The Gini sees the whole of it.",
            ],
        },
        "quiz_title": "Pattern and history",
        "quiz": [
            {"q": "Four people at 10 each; three pay 1 each to the fourth. What is the Gini coefficient afterwards?",
             "a": ["0",
                   "1/10",
                   "3/40",
                   "3/10"],
             "c": 2,
             "why": "Holdings are 9, 9, 9, 13. The gaps are 4 for three pairs in both orders, 24 in all, over 2·16·10 = 320, "
                    "which is 3/40. Zero is the Gini before the payments. The other two are not what the formula gives."},
            {"q": "What does Nozick use the change from 0 to 3/40 to argue?",
             "a": ["That the fans acted unjustly",
                   "That a pattern is disturbed by free transfers, so keeping it needs continued interference",
                   "That the total welfare of the group fell",
                   "That the Gini coefficient measures injustice"],
             "c": 1,
             "why": "His claim is that nobody was wronged and yet the shape changed, so a principle that insists on the "
                    "shape must undo free choices. The total did not change, and a measure of shape is not a measure of wrong."},
            {"q": "In the redistribute table the total rule calls (2, 4, 6, 28) and (6, 8, 10, 16) equal. What does that show?",
             "a": ["The redistribution changed nothing",
                   "The two lists are the same list in a different order",
                   "The Gini of both lists is the same",
                   "The total rule sees only the sum, and so cannot see the change in shape"],
             "c": 3,
             "why": "Both sum to 40, so the total rule ties them. The Gini does change, from 1/2 to 1/5, so the redistribution "
                    "did something, and the lists are different lists."},
            {"q": "Which fact would a defender of the entitlement view treat as making (9, 9, 9, 13) unjust?",
             "a": ["That the Gini is greater than 0",
                   "That one person holds more than the others",
                   "That the starting holdings were taken by force or a payment was coerced",
                   "That the holdings are not equal"],
             "c": 2,
             "why": "On the entitlement view a list is unjust because of how it arose. The other three describe the shape, "
                    "which is what the patterned view looks at and the entitlement view says is beside the point."},
        ],
        "mistakes": [
            ("Thinking a just distribution is one with a just shape",
             "On the historical view the same list of holdings can be just or unjust, depending on how it came about. "
             "The Gini of (9, 9, 9, 13) is 3/40 whether the fans paid freely or were robbed, so the number cannot tell "
             "the two apart. A defender of patterns must say why shape matters in itself."),
            ("Treating the Gini as a measure of injustice",
             "It measures the spread of holdings and nothing else. Both a fair market and a theft can leave the same spread. "
             "An egalitarian may care about the spread and a sufficientarian may not, and the coefficient is neutral between them."),
            ("Reading the argument as showing that no redistribution is justified",
             "Nozick's argument tells against patterned principles that ignore history. It leaves open a rectification of "
             "past injustice, and it assumes the starting holdings were just. If they were not, the exchanges inherit that."),
        ],
        "standard": ("Finish when you can compute a Gini coefficient for a short list and say what it does and does not show.",
                     "Given holdings before and after a set of payments, compute the coefficient of each, report the change, and state "
                     "which view of justice treats the change as significant and which treats it as irrelevant."),
        "note": "The rule shipped here is the total, which is deliberately blind to shape; switch it to leximin and "
                "the verdicts on the first table change, because the worst-off person lost a unit. The Gini and the leximin "
                "ranking are measuring different things, and a distribution can improve on one and worsen on the other.",
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "fairness-statistics-and-disparate-rates",
        "title": "Fairness, Statistics and Disparate Rates",
        "module": "Distributive justice",
        "one_line": "Equal treatment within every department can coexist with unequal overall rates, and the two ideas of fairness then give different answers.",
        "summary": (
            "A pooled acceptance rate can differ between two groups although each department accepts both at the same rate, "
            "because the groups apply to different departments. Standardising the rates removes the effect of the mix. "
            "The wrong model is that a gap in the pooled rate is a gap in treatment."
        ),
        "key": [
            "within each department: same rate for both",
            "pooled rate: weighted by who applied where",
            "a gap in the pooled rate can come from the mix",
            "equal treatment is not equal outcome",
        ],
        "key_label": "Two comparisons, two answers",
        "concepts_intro": (
            "The lesson reuses the arithmetic of “Correlation, Confounding and Simpson's Paradox” for a question about fairness. "
            "Three ideas carry it."
        ),
        "concepts": [
            ("A rate is a fraction of applicants",
             "An acceptance rate is the number admitted over the number who applied. Compared within a department, it "
             "asks whether like applicants were treated alike. Compared across departments pooled together, it asks "
             "something else."),
            ("The pooled rate depends on the mix",
             "The pooled rate for a group is an average of its department rates weighted by where its members applied. "
             "Two groups with the same rate in every department can have different pooled rates if they applied in different proportions."),
            ("Two notions of fairness",
             "Equal treatment says applicants with the same qualification in the same department should have the same chance. "
             "Equal outcomes says the overall rates for the groups should match. The two can disagree about the same data."),
        ],
        "read_title": "Two departments, one gap",
        "read_intro": "A table in which both departments treat the two groups alike and the overall rates do not match.",
        "body": [
            ("p", "A university has an open department and a selective one. In the open department three applicants in five "
                  "are admitted, and in the selective department one in five. Men and women are admitted at exactly "
                  "those rates in both. The only difference between the groups is where they applied: of every hundred men, "
                  "eighty applied to the open department and twenty to the selective; of every hundred women, twenty "
                  "applied to the open department and eighty to the selective."),
            ("math", [
                "                     men            women",
                "     open        48 of 80        12 of 20",
                "     selective    4 of 20        16 of 80",
                "     pooled      52 of 100       28 of 100",
            ]),
            ("p", "Within the open department both groups are admitted at `3/5`, and within the selective department both "
                  "at `1/5`. Pooled, the men's rate is `52/100`, which is `13/25`, and the women's is `28/100`, which is `7/25`. "
                  "A glance at the pooled rates suggests the men are admitted at nearly twice the rate. "
                  "A glance at the departments shows no group treated differently anywhere."),
            ("p", "The pattern is the one Bickel, Hammel and O'Connell found in the graduate admissions at Berkeley in "
                  "1973, where the pooled rates suggested a bias against women that the departments, taken one at a time, did "
                  "not show. The counts here are made small enough to follow by hand."),
            ("p", "Both statements are true of the same counts. What differs is the question each answers. "
                  "The within-department comparison asks whether, for the choice the applicant has already made, the "
                  "outcome depends on their group. The pooled comparison asks whether the two groups end up in the same "
                  "overall position."),
            ("def", ("Standardised rate",
                     "A <strong>standardised rate</strong> weights each department's rate by the same shares for both groups, "
                     "here each department's share of all applicants, so that the mix of applications cannot move the comparison.")),
            ("p", "Half of all applicants, `100` of `200`, applied to each department. The standardised rate for either group is "
                  "`(1/2)·(3/5) + (1/2)·(1/5)`, which is `2/5`. The two groups are equal at `2/5`, and the gap in "
                  "the pooled rates has vanished, which shows that the gap came from the mix."),
            ("h3", "Where the two notions come apart"),
            ("p", "Equal treatment holds in this table and equal outcomes fails. Each is a respectable notion of fairness, and "
                  "a policy that secures one need not secure the other. A rule that equalised the pooled rates would have "
                  "to admit applicants to the selective department at different rates for men and women, which breaks "
                  "equal treatment in the department."),
            ("p", "What the lab cannot decide is whether the mix is itself the unfairness. If women apply to the selective "
                  "department because the open one is closed to them in practice, or because of what they were taught was "
                  "possible, the equal rates within departments conceal a disadvantage upstream. If they apply there from "
                  "preference, they do not. The same counts fit both stories, and which is true is not in the table."),
            ("example", ("A reversal",
                         "Make women's rates higher in each department, `3/4` against `7/10` in the open one and `1/8` against "
                         "`1/10` in the selective one, with the same application mix. The pooled rates are then `58/100` "
                         "for men and `25/100` for women: the women do better in each department and worse overall. "
                         "The lab marks this as a reversal, and the standardised rates put the women ahead.")),
        ],
        "lab": ("choicekit", {
            "mode": "simpson", "weight": "standardised",
            "preset": "berkeley",
            "presets": [
                {"id": "berkeley", "label": "Equal rates in both departments, different application mixes",
                 "names": ["men", "women"],
                 "groups": [{"name": "open", "a": [48, 80], "b": [12, 20]},
                            {"name": "selective", "a": [4, 20], "b": [16, 80]}],
                 "expect": {"siPooled": "men 52/100 vs women 28/100: men higher", "siAdjusted": "men 2/5 vs women 2/5: equal", "siVerdict": "No reversal"}},
                {"id": "reversal", "label": "Women higher in each department, men higher pooled",
                 "names": ["men", "women"],
                 "groups": [{"name": "open", "a": [56, 80], "b": [15, 20]},
                            {"name": "selective", "a": [2, 20], "b": [10, 80]}],
                 "expect": {"siPooled": "men 58/100 vs women 25/100: men higher", "siAdjusted": "men 2/5 vs women 7/16: women higher", "siVerdict": "Reversal"}},
                {"id": "equal-everywhere", "label": "Equal rates and equal application mixes",
                 "names": ["men", "women"],
                 "groups": [{"name": "open", "a": [30, 50], "b": [30, 50]},
                            {"name": "selective", "a": [10, 50], "b": [10, 50]}],
                 "expect": {"siPooled": "men 40/100 vs women 40/100: equal", "siVerdict": "No reversal"}},
            ],
            "panel_title": "Compare the groups within and across departments",
            "panel_intro": "Each cell reads admitted/applied. The adjusted tile uses the standardised weights, "
                           "each department's share of all applicants; switch the weighting to pooled to see the raw comparison.",
        }),
        "steps_title": "Comparing two groups fairly",
        "steps_intro": "Five moves, and the third is the one that separates the two notions of fairness.",
        "steps": [
            ("Write each cell as admitted over applied",
             "Keep the fractions as they are. A rate rounded early hides the equalities this lesson depends on."),
            ("Compute the rate for each group in each department",
             "Compare the two groups within a department only. This is the equal-treatment comparison."),
            ("Compute the pooled rates and compare",
             "Add admitted over added applied for each group. This is the equal-outcomes comparison, and it may disagree with the last step."),
            ("Standardise",
             "Weight each department by its share of all applicants, the same for both groups, and compare again. "
             "If the gap vanishes, it came from the application mix."),
            ("Ask why the mix is what it is",
             "Whether the mix is itself unfair is a question about the world that lies outside the counts. State which "
             "answer your conclusion depends on."),
        ],
        "worked": {
            "title": "Equal treatment, unequal outcome",
            "intro": ["Men and women admitted at 3/5 in the open department and 1/5 in the selective one."],
            "lines": [
                "open        men 48/80 = 3/5     women 12/20 = 3/5    equal",
                "selective   men 4/20  = 1/5     women 16/80 = 1/5    equal",
                "pooled      men 52/100          women 28/100",
                "standardised (half and half): both (3/5 + 1/5) / 2 = 2/5",
            ],
            "after": [
                "Within each department the groups are treated alike, and standardised to the same mix they are equal at `2/5`. "
                "The pooled gap, `13/25` against `7/25`, is explained by who applied where.",
            ],
        },
        "quiz_title": "Two comparisons",
        "quiz": [
            {"q": "In the lesson's table, what are the two groups' admission rates within the selective department?",
             "a": ["4/20 for men and 16/80 for women, both 1/5",
                   "4/100 for men and 16/100 for women",
                   "1/5 for men and 4/5 for women",
                   "52/100 for men and 28/100 for women"],
             "c": 0,
             "why": "A rate is admitted over applied within the department: 4 of 20 and 16 of 80 are each 1/5. The second divides by "
                    "all applicants, the third mistakes applicants for admissions, and the last is the pooled pair."},
            {"q": "The pooled rates are 52/100 and 28/100 but each department admits both groups alike. What explains the gap?",
             "a": ["Men are treated better in one of the departments",
                   "The lab has rounded the fractions",
                   "The groups applied to the two departments in different proportions",
                   "Fewer women than men applied in all"],
             "c": 2,
             "why": "A pooled rate is an average of department rates weighted by where the group applied, and the weights differ: "
                    "80 of 100 men applied to the open department against 20 of 100 women. The rates within each department are equal, "
                    "a hundred of each group applied, and the lab does not round."},
            {"q": "Which pair names the two notions of fairness that come apart in this lesson?",
             "a": ["Equal treatment within each department, and equal overall outcomes",
                   "Equal effort, and equal talent",
                   "Total welfare, and average welfare",
                   "Equal opportunity before the veil, and after it"],
             "c": 0,
             "why": "The first holds in the table and the second fails. The other pairs are real distinctions, but they are not "
                    "the ones in play: no effort or talent figures appear, and the table has no welfare."},
            {"q": "In the reversal table women are admitted at a higher rate than men in both departments, yet the pooled rate is higher for men. What does the lab call this, and what causes it?",
             "a": ["Equal treatment; the departments are equally hard",
                   "A reversal; the groups' application mixes differ",
                   "A tie; the standardised rates are equal",
                   "A reversal; women are treated worse overall"],
             "c": 1,
             "why": "The pooled comparison disagrees with both within-department comparisons, which the lab calls a reversal, and "
                    "the disagreement is produced by the different mixes. The standardised rates are not equal, women lead, and "
                    "no one is treated worse in any department."},
        ],
        "mistakes": [
            ("Reading a gap in the pooled rate as a gap in treatment",
             "In the lesson's table the pooled rates are 13/25 and 7/25, yet both groups are admitted at 3/5 in the open "
             "department and 1/5 in the selective one. The pooled gap comes from where each group applied. A pooled "
             "disparity is a reason to ask why, and it does not by itself show unequal treatment."),
            ("Concluding that equal rates within departments settle the matter",
             "They settle equal treatment inside the department, and nothing else. If the application mix reflects barriers "
             "to entering the open department, the equal rates sit on top of an unfairness the table cannot show. "
             "The lab will compute the rates for any counts, and a fair-looking table does not certify its own inputs."),
            ("Expecting one fair policy to satisfy both notions",
             "To equalise the pooled rates here the selective department would have to admit the two groups at different rates, "
             "which breaks equal treatment there. When the mixes differ, the two notions give different instructions, "
             "and the choice between them is a choice of values."),
        ],
        "standard": ("Finish when you can compute within-group and pooled rates and say which notion of fairness each tests.",
                     "Given admitted and applied counts for two groups in two departments, compute the four rates and the two pooled "
                     "rates, standardise them, report whether the pooled comparison reverses, and name the claim about the mix on "
                     "which the fairness verdict depends."),
        "note": "Move ten of the women's applications in the first table from the selective department to the open one, keeping "
                "the rates, so that the women's cells read 18 of 30 and 14 of 70, and watch the pooled gap narrow, to `32/100` "
                "against `52/100`, while the rates within each department stay put. "
                "This is the arithmetic of “Correlation, Confounding and Simpson's Paradox” put to a question of justice.",
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "majority-rule-and-the-condorcet-paradox",
        "title": "Majority Rule and the Condorcet Paradox",
        "module": "Collective choice",
        "one_line": "Every voter can rank the candidates consistently and the majority still go in a circle.",
        "summary": (
            "Count, for each pair of candidates, how many voters prefer one to the other, and a Condorcet winner is a candidate who "
            "beats every rival by majority. With three voters and three candidates the majorities can form a cycle, "
            "though each voter's own ranking is in order. The wrong model is that majority rule always produces a ranking."
        ),
        "key": [
            "A beats B if more voters rank A above B",
            "a Condorcet winner beats every rival",
            "A beats B, B beats C, C beats A   a cycle",
            "transitive voters, intransitive majority",
        ],
        "key_label": "Pairwise majorities",
        "concepts_intro": (
            "Collective choice begins with the simplest rule there is, and with the case in which it fails to say anything."
        ),
        "concepts": [
            ("A profile is a list of rankings",
             "Each voter ranks all candidates from best to worst. The list of rankings, with how many voters hold each, "
             "is the profile, and it is the only input every voting rule here uses."),
            ("A Condorcet winner beats everyone",
             "Compare two candidates by counting the voters who rank one above the other. A candidate who wins every such "
             "contest is the Condorcet winner. There is at most one, and there may be none."),
            ("A cycle is not a tie",
             "In a cycle every contest has a decisive winner, and the winners go round: the first beats the second, the second the "
             "third, the third the first. No candidate is undefeated, and nothing in the votes breaks the circle."),
        ],
        "read_title": "Counting pairs",
        "read_intro": "A table of pairwise counts, a profile in which it has a winner, and one in which it does not.",
        "body": [
            ("p", "When two candidates are on the ballot, majority rule has a plain meaning: the one more voters prefer wins. "
                  "With three or more candidates there are several contests, and the question is whether majority rule can "
                  "be extended to rank them all. The first thing to do is to count, for each pair, the voters on either side."),
            ("def", ("Condorcet winner",
                     "A <strong>Condorcet winner</strong> is a candidate who is preferred to each other candidate by "
                     "a majority of voters. It is named for Condorcet, who observed in the eighteenth century that there may be none.")),
            ("p", "Take a profile with seven voters: three rank the candidates `A B C`, two rank them `B C A`, and two rank "
                  "them `C B A`. Candidate `A` meets `B`: three voters put `A` first and four put `B` above `A`, so "
                  "`B` wins `4` to `3`. Candidate `B` meets `C`: the three `A B C` voters and the two `B C A` voters rank "
                  "`B` higher, five against two, and `B` wins. Since `B` beats `A` and `B` beats `C`, `B` is the Condorcet "
                  "winner. Notice that it is not the candidate with the most first places, which is `A`."),
            ("p", "Now change the voters. Let there be three of them, one with each ranking `A B C`, `B C A` and `C A B`. "
                  "Each ranking is a perfectly ordinary order of the three candidates."),
            ("math", [
                "     voter 1      A   B   C",
                "     voter 2      B   C   A",
                "     voter 3      C   A   B",
            ]),
            ("p", "Count the contests. `A` against `B`: voters one and three rank `A` higher, so `A` wins `2` to `1`. "
                  "`B` against `C`: voters one and two rank `B` higher, so `B` wins `2` to `1`. `C` against `A`: voters two "
                  "and three rank `C` higher, so `C` wins `2` to `1`. The majority preference is that `A` beats `B`, `B` beats "
                  "`C` and `C` beats `A`."),
            ("p", "That is the <strong>Condorcet paradox</strong>. No voter prefers `A` to `B`, `B` to `C` and `C` to `A`, "
                  "so no voter is irrational in the sense of the money pump from “Preference, Transitivity and the Money Pump”. "
                  "The group, taken as a chooser, has exactly the cyclic preference that lesson showed can be exploited: "
                  "offer it `B` in exchange for `A` and a majority accepts, then `C` for `B`, then `A` for `C`."),
            ("h3", "How close a profile is to a cycle"),
            ("p", "Add two voters who both rank `A B C` to the cycle's three, so that five voters rank `A B C` three times, `B C A` "
                  "once and `C A B` once, and `A` wins every contest: it beats `B` four to one and `C` three to two. "
                  "Now move one of the three `A B C` voters to `C A B`. The contest between `A` and `C` flips to three "
                  "against two for `C`, and the circle closes. A cycle can be one voter away."),
            ("p", "The lab prints the table of counts and, when there is no Condorcet winner, the cycle it found. "
                  "Two limits apply. It reports the cycle for the profile typed; how likely such profiles are in real "
                  "elections is a different question. And it is not an argument against majority rule in the two-candidate "
                  "case, where no cycle can occur."),
        ],
        "lab": ("choicekit", {
            "mode": "vote", "rule": "condorcet",
            "preset": "cycle",
            "presets": [
                {"id": "cycle", "label": "Three voters, one ranking each",
                 "kind": "ranking",
                 "profile": [{"count": 1, "rank": "A B C"}, {"count": 1, "rank": "B C A"}, {"count": 1, "rank": "C A B"}],
                 "expect": {"voCondorcet": "cycle: A > B > C > A", "voWinner": "none"}},
                {"id": "winner", "label": "Seven voters with a Condorcet winner",
                 "kind": "ranking",
                 "profile": [{"count": 3, "rank": "A B C"}, {"count": 2, "rank": "B C A"}, {"count": 2, "rank": "C B A"}],
                 "expect": {"voCondorcet": "B", "voWinner": "B"}},
                {"id": "near-cycle", "label": "Five voters, one move from a cycle",
                 "kind": "ranking",
                 "profile": [{"count": 3, "rank": "A B C"}, {"count": 1, "rank": "B C A"}, {"count": 1, "rank": "C A B"}],
                 "expect": {"voCondorcet": "A", "voWinner": "A"}},
            ],
            "panel_title": "Count the pairwise contests",
            "panel_intro": "A profile reads count: best to worst, groups separated by semicolons. In the table each cell counts "
                           "the voters who prefer the row candidate to the column candidate; a green cell is a won contest.",
        }),
        "steps_title": "Finding a Condorcet winner or a cycle",
        "steps_intro": "Five moves for any profile with three candidates, and the last one checks the work.",
        "steps": [
            ("Write the profile as a list of rankings with counts",
             "Each ranking runs from best to worst and appears with the number of voters who hold it."),
            ("Pick a pair and count the voters on each side",
             "For `A` against `B`, count the voters whose ranking puts `A` above `B`. The rest put `B` above `A`, since each ranking is complete."),
            ("Do this for every pair",
             "Three candidates give three contests, and each contest has a winner unless the electorate is even and splits evenly."),
            ("Look for a candidate who won every contest it was in",
             "If there is one, it is the Condorcet winner. If not, follow the winners round: if the chain returns to the start, "
             "there is a cycle."),
            ("Check that each voter's own ranking is consistent",
             "Each ranking is a straight order. If the group's preference is a circle, the circle is a property of the "
             "group and not of any voter."),
        ],
        "worked": {
            "title": "Three voters, three contests",
            "intro": ["Voter one ranks A B C, voter two B C A, voter three C A B."],
            "lines": [
                "A against B:   voters 1 and 3 prefer A   -> A wins 2-1",
                "B against C:   voters 1 and 2 prefer B   -> B wins 2-1",
                "C against A:   voters 2 and 3 prefer C   -> C wins 2-1",
                "cycle: A beats B, B beats C, C beats A",
            ],
            "after": [
                "Every contest is decisive, and each voter's list is in order. The circle belongs to the majority, "
                "which is why no change of mind by one voter and no tie-break can be said to have repaired a fault in them.",
            ],
        },
        "quiz_title": "Counting contests",
        "quiz": [
            {"q": "In the cycle profile, one voter ranks A B C, one B C A and one C A B. How many voters prefer A to B?",
             "a": ["1",
                   "3",
                   "0",
                   "2"],
             "c": 3,
             "why": "The voters ranking A B C and C A B put A above B. The B C A voter puts B above A. So 2 prefer A to B and 1 prefers B to A."},
            {"q": "Every voter in the cycle profile has a consistent ranking. What does the cycle show?",
             "a": ["Consistent individual rankings do not guarantee a consistent majority preference",
                   "At least one voter must have misreported",
                   "Majority rule gives a tie between the three candidates",
                   "Two of the voters have the same ranking"],
             "c": 0,
             "why": "The three rankings are different and each is a complete order; the majority relation still cycles. "
                    "No misreport is needed, and the contests are won 2 to 1, so they are not ties."},
            {"q": "In the winner profile, three voters rank A B C, two B C A and two C B A. Why is B the Condorcet winner and not A?",
             "a": ["B has the most first places",
                   "A is ranked first by fewer voters than B",
                   "B beats each rival by a majority, while A loses to B four to three",
                   "B is ranked second by the most voters"],
             "c": 2,
             "why": "B wins against A, 4 to 3, and against C, 5 to 2. A has the most first places, three against B's two, so the "
                    "first two choices are wrong, and the count of second places is not what defines a Condorcet winner either."},
            {"q": "The near-cycle profile has three voters at A B C, one at B C A and one at C A B, and A is the Condorcet winner. One A B C voter changes to C A B. What does the lab report?",
             "a": ["A is still the Condorcet winner",
                   "C is the Condorcet winner",
                   "A cycle: A beats B, B beats C, C beats A",
                   "B is the Condorcet winner"],
             "c": 2,
             "why": "The counts become: A over B 4 to 1, B over C 3 to 2, and C over A 3 to 2, since the B C A voter and both "
                    "C A B voters prefer C. Every candidate loses a contest, so there is no winner and the majorities go round."},
        ],
        "mistakes": [
            ("Believing majority rule always produces a ranking",
             "With three voters ranking A B C, B C A and C A B, A beats B, B beats C and C beats A, each by 2 to 1. "
             "Majority preference between pairs need not be transitive, so there may be no best candidate and no order. "
             "Where there is no cycle the rule works, and a rule that always produced a ranking would need something more than majorities."),
            ("Taking a cycle for a tie",
             "Every contest in the cycle has a clear winner. The three candidates are not equal; each is beaten by one rival "
             "and beats another. A tie would mean the counts were equal, and none of them is."),
            ("Blaming the voters",
             "Each of the three voters ranks the candidates in a consistent order. The inconsistency is created by combining "
             "three consistent orders, and no voter has to be fickle for it to appear."),
        ],
        "standard": ("Finish when you can tabulate pairwise majorities and say whether a profile has a Condorcet winner or a cycle.",
                     "Given a profile of rankings with counts, compute the count for each pair of candidates, name the Condorcet "
                     "winner if there is one, and otherwise write the cycle; then build a three-voter profile that cycles."),
        "note": "The lab's rule is shipped as the Condorcet rule; the same profile can be read under the other rules by "
                "changing it, and the next lesson does exactly that. Try changing the C A B voter in the cycle profile to C B A "
                "and watch the cycle disappear: B now beats A and beats C, each 2 to 1, and is the Condorcet winner. One "
                "ranking moved, and the circle is gone.",
    },
]
