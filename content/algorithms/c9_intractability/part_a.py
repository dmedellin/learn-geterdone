"""Intractability and Approximation, lessons 01-07 - the line, the reductions, and the first exact method.

Every figure in these seven dicts was read off the lab by executing the
shipped JavaScript, never reasoned about. Where a preset's own `note` or
`label` disagreed with what the code computes, the code won and the lesson
says the computed thing; four of those disagreements are recorded in the
report that accompanied this course rather than repeated here.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "decision-search-and-the-certificate",
        "title": "Decision, Search and the Certificate",
        "module": "Deciding, verifying, searching",
        "one_line": "Ask a yes-or-no oracle four questions about a three-variable formula and watch an assignment it never returns come out.",
        "summary": (
            "The classes this course is about are classes of <em>decision</em> problems, which "
            "looks like a restriction and is not one. The lab hands a satisfiability oracle "
            "&mdash; a routine that answers yes or no and returns nothing else &mdash; four "
            "questions about a formula in three variables, and builds a satisfying assignment "
            "out of the four answers. That is the whole price of the restriction: `n + 1` calls."
        ),
        "key": [
            "a DECISION problem answers yes or no; a SEARCH problem hands back the object",
            "a certificate is an object a verifier accepts in polynomial time",
            "",
            "fix x1 = T and ask again:  still yes, keep it;  no, and every model has x1 = F",
            "",
            "4 oracle calls against 8 assignments, and one more variable doubles only the 8",
            "the reduction is polynomial in CALLS; the oracle is not polynomial in anything",
        ],
        "key_label": "Four questions, three variables, and the assignment the oracle never returned",
        "concepts_intro": (
            "The hard idea is the asymmetry between finding an object and checking one. The "
            "other two say what the restriction to yes-or-no questions costs, which is a number "
            "the lab counts, and what the oracle costs, which is a separate question the "
            "reduction does not touch and must not be read as answering."
        ),
        "concepts": [
            ("Checking is a different question from finding",
             "Hand someone an assignment and they can evaluate every clause and tell you whether "
             "it satisfies the formula; the work is one pass over the clauses. Ask them to "
             "produce one and nobody knows a method that is not, in the worst case, a search. "
             "A <strong>certificate</strong> is an object that makes the yes answer checkable in "
             "polynomial time, and `NP` is the class of decision problems that have one. The "
             "definition says nothing at all about how the certificate is found, and that "
             "silence is the whole open question."),
            ("Restricting to yes-or-no questions costs n + 1 calls",
             "It would be reasonable to think the decision version is a weaker, easier question "
             "than the search version, so that results about it say less. Here it is not. The "
             "lab fixes `x1` to true and asks the oracle whether what is left is still "
             "satisfiable: if yes, some model has `x1` true and committing is safe; if no, every "
             "model has `x1` false and committing to false is safe. Either way one question "
             "settles one variable, and after `n` more the assignment is written out. On the "
             "formula loaded, four calls against eight assignments."),
            ("An exponential oracle is still an oracle",
             "The oracle in the lab is brute force &mdash; it decides satisfiability by trying "
             "all eight assignments. That is deliberate and it is not a cheat, because the claim "
             "being demonstrated is about the number of CALLS, not about their cost. The "
             "reduction is polynomial in calls; the oracle is not polynomial in anything; and "
             "neither fact affects the other. A reader who concludes from this page that "
             "satisfiability has been solved efficiently has read a statement about one quantity "
             "as a statement about another."),
        ],
        "read_title": "Three forms of one question, and the reduction between two of them",
        "read_intro": "What a decision problem is, what a certificate is, the theorem that search reduces to decision, and the four calls the lab makes.",
        "body": [
            ("def", ("A decision problem",
                     "A <strong>decision problem</strong> is a set of inputs together with a "
                     "yes-or-no question about each one. `SAT` is the decision problem whose "
                     "input is a formula in conjunctive normal form and whose question is "
                     "&ldquo;is there an assignment satisfying every clause?&rdquo;. An "
                     "algorithm solves it by answering the question; it is not required to "
                     "produce anything else, and the oracle in the lab does not.")),
            ("def", ("A certificate, and the class NP",
                     "A decision problem is in `NP` when every yes instance has a "
                     "<strong>certificate</strong> of size polynomial in the input, and a "
                     "verifier that reads the instance and the certificate and accepts in "
                     "polynomial time, accepting no certificate whatever for a no instance. For "
                     "`SAT` the certificate is an assignment and the verifier evaluates the "
                     "clauses. `P` is the class of decision problems solvable in polynomial "
                     "time, and `P` is contained in `NP` because an algorithm that answers the "
                     "question is a verifier that ignores its certificate.")),
            ("p", "Whether the containment is strict is not known, and nothing on this course "
                  "settles it. What the rest of the course does is build the structure that "
                  "makes the question sharp: a relation between problems that carries hardness "
                  "from one to another, a family of problems at the top of that relation, and "
                  "six things worth doing about a problem that reaches it."),
            ("h3", "The same question in three forms"),
            ("p", "Every problem here can be asked three ways, and it is worth separating them "
                  "before the machinery starts. The <strong>decision</strong> form asks whether "
                  "a solution exists; the <strong>search</strong> form asks for one; the "
                  "<strong>optimisation</strong> form asks for the best one. They are different "
                  "questions and the theory is stated for the first. The reason that costs "
                  "nothing is this lesson."),
            ("thm", ("Search reduces to decision for satisfiability",
                     "Suppose a routine decides `SAT` in one unit of time. Then a satisfying "
                     "assignment for a formula on `n` variables can be produced with `n + 1` "
                     "calls to it.")),
            ("proof", ("Call the oracle on the formula itself. If it says no there is no "
                       "assignment to produce and the work is over, which is the first call. "
                       "Otherwise fix `x1` to true, simplify &mdash; delete every clause "
                       "containing `x1` and delete `&not;x1` from the clauses containing it "
                       "&mdash; and call the oracle on what is left.",
                       "If that call says yes, some satisfying assignment of the original has "
                       "`x1` true, so committing to true loses nothing. If it says no, no "
                       "satisfying assignment has `x1` true; since the original is satisfiable, "
                       "every satisfying assignment has `x1` false, so committing to false loses "
                       "nothing. Either way one call settles one variable and the remaining "
                       "formula is still satisfiable.",
                       "Repeat for `x2` up to `xn`. After `n` more calls every variable is "
                       "fixed and no clause remains unsatisfied, so reading the commitments off "
                       "gives an assignment. The total is `n + 1` calls, each on a formula no "
                       "larger than the original.")),
            ("h3", "What the lab counts, and what it refuses to count"),
            ("p", "The loaded formula is `(x1 or x2 or not x3) and (not x1 or x2 or x3) and "
                  "(x1 or not x2 or x3) and (not x1 or not x2 or not x3)`: three variables, four "
                  "clauses. The panel reports 4 oracle calls against 8 assignments a search "
                  "would try, the assignment `x1=T x2=T x3=F`, and the formula's 4 models out of "
                  "those 8. Both branches are allowed at `x1` and at `x2`, so the reduction "
                  "takes true and moves on; at `x3` the oracle refuses true and the reduction "
                  "takes false, which is the only place on this instance where a question does "
                  "any work."),
            ("p", "Two checks run beside the trace and neither is decoration. Every restricted "
                  "formula is re-decided by brute force independently of the reduction, and all "
                  "three steps are required to agree; and the assignment at the end is evaluated "
                  "clause by clause rather than assumed. A reduction that produced a confident "
                  "wrong witness would look identical on the page without them."),
            ("example", ("The step that refuses a branch",
                         "After `x1` and `x2` are both fixed true, the formula that is left is "
                         "`(not x3)`. The oracle is asked whether fixing `x3` to true leaves "
                         "something satisfiable and answers no, so `x3` is false. That single "
                         "refusal is the difference between an assignment and a guess, and it "
                         "cost one question.")),
            ("p", "Now read the two numbers side by side and resist the conclusion. Four calls "
                  "against eight assignments is a saving of one half on this formula. Move to "
                  "the four-variable example in the panel and it is five calls against sixteen. "
                  "The calls grow by one per variable and the assignments double, so the gap "
                  "widens without limit &mdash; but that sentence is a claim about the two "
                  "expressions, not about the two numbers on screen, and the numbers on screen "
                  "cannot establish it."),
        ],
        "lab": ("reduction", {"mode": "selfreduce", "preset": "three"}),
        "steps_title": "Turning a yes-or-no routine into one that hands back the object",
        "steps_intro": "The procedure is four lines and the discipline is in what you check afterwards.",
        "steps": [
            ("Decide the whole instance first",
             "One call, before anything is fixed. If the answer is no there is nothing to build "
             "and every later call would be answering a question about an instance you have "
             "already been told has no solution. The lab stops there, and the trace shows no "
             "variable being fixed."),
            ("Fix one variable and re-ask",
             "Set the variable, simplify the instance, and call the oracle on the smaller "
             "instance. Keep the value if the answer is still yes; take the other value if it is "
             "no. Do not reason about which value looks more promising &mdash; the oracle's "
             "answer is the whole justification and a heuristic here would break the argument."),
            ("Check that the remaining instance is still a yes",
             "The invariant that makes the induction work is that the formula in hand is "
             "satisfiable at every step. The lab re-decides each restricted formula with brute "
             "force and prints whether every step agreed; if one did not, the commitment before "
             "it was wrong and everything after it is about a different problem."),
            ("Verify the object against the original instance",
             "Evaluate the finished assignment clause by clause on the formula as it was typed, "
             "not on the simplified one you ended with. The lab prints that verdict separately "
             "from the oracle's, because a witness checked only against the instance it was "
             "derived from is checked against itself."),
            ("Report the calls and their cost as two numbers",
             "Say how many times the oracle was asked and say what one call costs. Collapsing "
             "them into a single claim about efficiency is the error this construction invites, "
             "and it is the one the panel refuses to make."),
        ],
        "worked": {
            "title": "Four calls on a four-clause formula",
            "intro": [
                "The formula is `(x1 or x2 or not x3) and (not x1 or x2 or x3) and (x1 or not x2 "
                "or x3) and (not x1 or not x2 or not x3)`. One row per question, with the "
                "formula the question was asked about and what the oracle allowed.",
            ],
            "lines": [
                "question   formula asked about                    T?    F?    taken   clauses left",
                "",
                "   0       the whole formula                      satisfiable          4",
                "   1       (x2 ∨ x3) ∧ (¬x2 ∨ ¬x3)                yes   yes   x1 = T        2",
                "   2       (¬x3)                                  yes   yes   x2 = T        1",
                "   3       nothing left                           no    yes   x3 = F        0",
                "",
                "assignment produced        x1=T  x2=T  x3=F",
                "satisfies every clause     yes, checked clause by clause",
                "every branch re-asked of brute force    all 3 agree",
                "",
                "oracle calls used          4        n + 1 is 4",
                "assignments a search would try         8",
                "models the formula has     4 of 8   (000, 110, 101, 011)",
            ],
            "after": [
                "Rows 1 and 2 have yes in both columns, and that is the ordinary case: both "
                "values of the variable extend to some model, so the reduction takes true and "
                "nothing is lost. Row 3 is where a question earns its keep. The formula in hand "
                "is `(not x3)`, fixing `x3` true empties a clause, the oracle says no, and false "
                "is forced.",
                "Notice that the assignment produced, `110`, is one of the four models and the "
                "reduction had no way of preferring it. Any of the four would have been a "
                "correct answer to the search question; the oracle's answers happen to walk to "
                "this one, and which one they walk to depends on the order the variables are "
                "fixed in, not on anything about the formula.",
                "For a faded rehearsal, switch the panel to the formula with exactly one model "
                "and predict the two columns before running it. The supplied first move: with "
                "only one model, no variable can go both ways, so every row must read yes in "
                "exactly one column. Say which one, for each of the three variables, and then "
                "check &mdash; and notice that being right about this formula tells you nothing "
                "about the next.",
            ],
        },
        "quiz_title": "Deciding, verifying, and the difference",
        "quiz": [
            {"q": "What does it mean for a decision problem to be in `NP`?",
             "a": ["Its yes instances have short certificates that a polynomial-time verifier accepts",
                   "It can be solved in polynomial time on a non-deterministic computer that guesses correctly on purpose",
                   "It cannot be solved in polynomial time",
                   "Both its yes and its no instances have short certificates"],
             "c": 0,
             "why": "Verification is the definition: a certificate of polynomial size and a "
                    "verifier that accepts it in polynomial time, and accepts nothing for a no "
                    "instance. The second answer describes the same class but sneaks in "
                    "&ldquo;guesses correctly on purpose&rdquo;, which is not a machine. The "
                    "third is wrong because `P` is inside `NP`. The fourth describes the "
                    "intersection with the complementary class, which is a different and "
                    "stronger condition."},
            {"q": "The panel reports 4 oracle calls against 8 assignments. What has been established about the cost of finding a satisfying assignment?",
             "a": ["That it is half the cost of searching",
                   "That search is no harder than decision, up to `n + 1` calls &mdash; nothing about the cost of a call",
                   "That satisfiability can be solved in four steps",
                   "That the oracle is polynomial-time"],
             "c": 1,
             "why": "The construction converts one kind of question into another and counts "
                    "calls. What a call costs is untouched: the oracle here is a brute-force "
                    "search over all eight assignments, so the total work is larger than a "
                    "single search, not smaller. The saving of one half is arithmetic about two "
                    "numbers on one formula, and it is not what the theorem says."},
            {"q": "The oracle answers no when asked whether the formula with `x3` fixed true is satisfiable. What follows?",
             "a": ["The formula is unsatisfiable",
                   "`x3` is false in every satisfying assignment of the formula in hand",
                   "`x3` is false in some satisfying assignment",
                   "The reduction should try a different variable next"],
             "c": 1,
             "why": "The formula in hand is known to be satisfiable, because the previous call "
                    "said so. If no satisfying assignment has `x3` true, every one of them has "
                    "it false, which is what makes the commitment safe. &ldquo;Some&rdquo; would "
                    "not be enough to commit on, and the whole formula's satisfiability was "
                    "settled by the very first call."},
            {"q": "A reader concludes from this page that the decision form is the easy form of the question and the search form is the hard one. What is wrong with that?",
             "a": ["Nothing: the decision form asks for less",
                   "The search form is the easy one, since it produces more information",
                   "They are equally hard here: a decision routine yields a search routine at a cost of `n + 1` calls",
                   "The comparison is meaningless because neither has a known polynomial algorithm"],
             "c": 2,
             "why": "That is exactly what the reduction shows, and it is the reason the theory "
                    "is stated for yes-or-no questions without losing generality. The last "
                    "answer is tempting and wrong: two problems can be compared by reduction "
                    "whether or not either is known to be tractable, and comparing them is what "
                    "this course does."},
        ],
        "mistakes": [
            ("Reading the certificate definition as a claim about finding",
             "`NP` says a yes answer can be justified quickly once the justification is in hand. "
             "It says nothing about producing it, and the definition would be trivially "
             "uninteresting if it did. Every misunderstanding of what `P` versus `NP` asks comes "
             "from collapsing the two."),
            ("Taking the call count for a running time",
             "Four calls is four calls. On this page one call is a search over eight assignments, "
             "so the page's own total work is larger than the search it is compared against. The "
             "panel prints both numbers and refuses to divide them, and so should you."),
            ("Believing the decision form is a weaker result",
             "It is common to hear that hardness results are &ldquo;only&rdquo; about decision "
             "problems. For every problem on this course the search and optimisation forms are "
             "no harder than the decision form by an argument of exactly this shape, so a "
             "hardness result about the yes-or-no question is a hardness result about all three."),
        ],
        "standard": (
            "Finish when you can turn a yes-or-no routine into one that returns the object, and say what that costs.",
            "You should be able to define a certificate and the class it defines, state the "
            "containment that is known and the one that is open, run the fixing argument on a "
            "formula of your own, and separate the number of calls a reduction makes from what a "
            "call costs.",
        ),
        "note": (
            "This is the only construction on this course that does not transform an instance: "
            "it transforms a question. Every reduction after it takes an instance of one problem "
            "and builds an instance of another, and &ldquo;A Reduction Is a Construction&rdquo; "
            "builds the first of them in front of you."
        ),
    },

    # ---------------------------------------------------------------- 02
    {
        "slug": "a-reduction-is-a-construction",
        "title": "A Reduction Is a Construction",
        "module": "Deciding, verifying, searching",
        "one_line": "Turn two clauses into six vertices and eight edges, then carry seven independent sets back and check every one against the formula.",
        "summary": (
            "&ldquo;Satisfiability reduces to independent set&rdquo; is a sentence that can be "
            "repeated and cannot be used. The reduction is a construction: a triangle per "
            "clause, an edge between contradictory literals, and a target equal to the number of "
            "clauses. The lab builds it, solves both sides exhaustively, and then asks the "
            "question a diagram with an arrow on it cannot &mdash; what the map does to the "
            "solutions, which is three questions and not one."
        ),
        "key": [
            "f is a polynomial-time map on INSTANCES with  x ∈ A  ⟺  f(x) ∈ B",
            "",
            "one vertex per literal OCCURRENCE, a triangle per clause,",
            "an edge between every contradictory pair, and k = the clause count",
            "",
            "2 clauses  →  6 vertices, 8 edges, k = 2",
            "7 independent sets of size 2 against 6 satisfying assignments",
            "sound: yes.   injective: no, one assignment has three preimages.   onto: no, 111 is unhit",
        ],
        "key_label": "The gadget, and the three separate verdicts on the map it induces",
        "concepts_intro": (
            "The first idea is what a reduction has to preserve, which is less than readers "
            "expect. The second is the gadget: two constraints expressed as edges. The third is "
            "the distinction the page computes three times rather than asserting once."
        ),
        "concepts": [
            ("A reduction preserves the ANSWER, not the solutions",
             "Writing `A` reduces to `B` means there is a polynomial-time map `f` on instances "
             "with the property that `x` is a yes instance of `A` exactly when `f(x)` is a yes "
             "instance of `B`. That is a statement about two bits. It does not say the solution "
             "sets correspond, and a reader who assumes they do will believe things about this "
             "reduction that the lab shows to be false. Preserving the solutions one for one is "
             "a stronger property that some reductions have and this one does not."),
            ("The gadget turns two requirements into two kinds of edge",
             "A satisfying assignment picks one true literal from each clause, and never picks a "
             "literal and its negation. Those are exactly the two things an independent set "
             "cannot do if you build the graph correctly: put the three literal occurrences of a "
             "clause in a triangle, so at most one of them can be chosen, and join every "
             "occurrence of `x` to every occurrence of `&not;x`, so a contradictory pair can "
             "never both be chosen. An independent set of size `m` then picks exactly one "
             "literal from each of the `m` clauses, consistently &mdash; which is an assignment."),
            ("Sound, injective and onto are three questions",
             "The panel answers them separately because their answers differ. Every independent "
             "set of size `k` maps back to an assignment that satisfies the formula: sound. Two "
             "different sets can map to one assignment, and here three do: not injective. And an "
             "assignment can fail to be the image of anything, because the map back leaves every "
             "variable no chosen literal mentions at false: not onto. One word could not have "
             "carried any of that."),
        ],
        "read_title": "The map on instances, the gadget, and the map it induces on solutions",
        "read_intro": "What a reduction is, the two edge types, the correctness proof in both directions, and the three verdicts the lab computes on the induced map.",
        "body": [
            ("def", ("Polynomial-time many-one reduction",
                     "`A` reduces to `B`, written `A ≤p B`, when there is a function `f` "
                     "computable in polynomial time taking instances of `A` to instances of `B` "
                     "such that `x` is a yes instance of `A` if and only if `f(x)` is a yes "
                     "instance of `B`. The direction of the consequence is the part to hold on "
                     "to: an algorithm for `B` gives one for `A`, so hardness travels from `A` "
                     "to `B` and tractability travels the other way.")),
            ("def", ("Independent set",
                     "An <strong>independent set</strong> in a graph is a set of vertices no two "
                     "of which are joined by an edge. The decision problem takes a graph and an "
                     "integer `k` and asks whether one of size `k` exists. The lab's target `k` "
                     "is always the number of clauses, which is what makes the construction a "
                     "reduction rather than a drawing.")),
            ("h3", "The construction"),
            ("ol", [
                "One vertex for each literal <em>occurrence</em>, not one per literal. A clause "
                "with three literals contributes three vertices even if two of them name the "
                "same variable.",
                "An edge between every two vertices of the same clause, making a triangle. At "
                "most one vertex per clause can be in an independent set.",
                "An edge between every occurrence of `x` and every occurrence of `&not;x`. No "
                "independent set can hold two occurrences that contradict.",
                "Ask for an independent set of size `k = m`, the number of clauses.",
            ]),
            ("thm", ("The construction is a reduction",
                     "The formula is satisfiable if and only if the constructed graph has an "
                     "independent set of size `m`.")),
            ("proof", ("Suppose the formula is satisfiable. Fix a satisfying assignment and, in "
                       "each clause, choose one occurrence of a literal the assignment makes "
                       "true. The chosen vertices lie in distinct clauses so no triangle edge "
                       "joins two of them, and they are all true under one assignment so no "
                       "contradiction edge joins two of them either. That is an independent set "
                       "of size `m`.",
                       "Conversely, suppose there is an independent set `S` of size `m`. The "
                       "triangles force its members into distinct clauses, one each. Set every "
                       "variable so that each literal named by a member of `S` is true; this is "
                       "consistent, because a variable asked to be both true and false would "
                       "mean `S` contains a contradictory pair, and those are joined. Variables "
                       "no member mentions may be set arbitrarily. Each clause now contains a "
                       "true literal, so the formula is satisfied.")),
            ("p", "Both halves are needed and the second is the one that gets skipped. A "
                  "construction with only the first half proves that a yes instance maps to a "
                  "yes instance, which permits a map that turns every no instance into a yes "
                  "instance as well &mdash; and is therefore useless. The lab checks both "
                  "directions on every solution, not once on the optimum."),
            ("h3", "What the lab built, and what it then measured"),
            ("p", "The loaded formula is `(x1 or x2 or not x3) and (not x1 or x2 or x3)`: two "
                  "clauses, three variables. The construction gives 6 vertices and 8 edges "
                  "&mdash; two triangles for six of them, plus `x1` to `&not;x1` and `&not;x3` "
                  "to `x3` &mdash; and `k = 2`. There are 15 pairs of vertices and 8 are joined, "
                  "so exactly 7 pairs are independent, and the panel reports 7 independent sets "
                  "of size 2 against 6 satisfying assignments."),
            ("p", "Those two counts are not equal, and nothing requires them to be. What the "
                  "reduction promises is that one list is empty exactly when the other is. What "
                  "the panel computes is the whole map between them: sound in both directions, "
                  "three sets landing on one assignment, and one assignment that is the image of "
                  "nothing."),
            ("p", "Two rows of that table look as though they disagree and do not, and it is "
                  "worth reading them together. The reverse construction succeeds on every "
                  "model &mdash; take the first true literal of each clause and all 6 give an "
                  "independent set of size 2 &mdash; while the map back is <em>not</em> onto. "
                  "Both are true because the round trip is not the identity: starting from the "
                  "all-true assignment, the first true literals are `x1` in the first clause "
                  "and `x2` in the second, so the set built is the pair of vertices 1 and 5, "
                  "and that set reads back as `x1=T x2=T x3=F`. Every model builds a set; not "
                  "every model is what the set it builds maps back to."),
            ("example", ("Why 111 is unreachable",
                         "The assignment making all three variables true satisfies both clauses, "
                         "so it is a model. But an independent set here has 2 members, so at most "
                         "2 variables can be named by a chosen literal, and the map back leaves "
                         "every unmentioned variable false. Three true variables therefore cannot "
                         "be the image of a 2-element set. The gap is a property of the map, not "
                         "an error in it: the reduction was never required to be onto.")),
            ("p", "This is the first place on this course where a measured fact and a proved "
                  "claim point in different directions, and the lesson is to read each for what "
                  "it is. The proof establishes that the two yes-or-no answers agree, for every "
                  "formula. The panel establishes that on this formula the map on solutions is "
                  "three-to-one somewhere and misses one assignment. Neither statement is "
                  "evidence about the other."),
        ],
        "lab": ("reduction", {"mode": "independentset", "preset": "two"}),
        "steps_title": "Building a reduction, and checking the thing you built",
        "steps_intro": "Four of these five steps are things a diagram with an arrow on it silently skips.",
        "steps": [
            ("Write the map on instances, with its running time",
             "Say exactly what is built from what: how many vertices, which edges, what target. "
             "If the construction cannot be described without the phrase &ldquo;and so "
             "on&rdquo;, it has not been written down yet. The time bound matters as much as the "
             "output, because an exponential map proves nothing about hardness."),
            ("Prove the forward direction by construction",
             "Take a solution of the original and build a solution of the transformed instance "
             "from it. This is the half that says the construction can represent what it claims "
             "to represent, and it is the one a page that only maps solutions back never tests."),
            ("Prove the backward direction by reading off",
             "Take a solution of the transformed instance and read a solution of the original "
             "out of it, then check that solution by the original problem's own rules. The lab "
             "carries each independent set back and evaluates the formula clause by clause on "
             "the result."),
            ("Ask the three questions about the induced map separately",
             "Is every image a genuine solution? Do two solutions share an image? Is every "
             "solution an image? The answers are independent of one another and only the first "
             "is required for the reduction to be valid. Writing &ldquo;bijection&rdquo; without "
             "computing the other two is how a false claim gets into a correct proof."),
            ("Check the no case as well as the yes case",
             "Load the unsatisfiable example in the panel: the largest independent set in the "
             "constructed graph is 3 against a target of 4, so the answer is no on both sides. A "
             "reduction tested only on yes instances has been tested on half the definition."),
        ],
        "worked": {
            "title": "Two clauses, six vertices, and the seven sets carried back",
            "intro": [
                "Vertices 1, 2, 3 are the occurrences of `x1`, `x2`, `not x3` in the first "
                "clause; vertices 4, 5, 6 are `not x1`, `x2`, `x3` in the second. The map back "
                "sets every variable named by a chosen literal and leaves the rest false.",
            ],
            "lines": [
                "edges      1-2  1-3  2-3      the first clause's triangle",
                "           4-5  4-6  5-6      the second clause's triangle",
                "           1-4                x1 against ¬x1",
                "           3-6                ¬x3 against x3",
                "",
                "15 pairs of vertices, 8 of them joined, so 7 independent pairs:",
                "",
                "   set        literals chosen        assignment read back",
                "  {2, 4}      x2 , ¬x1              010",
                "  {3, 4}      ¬x3 , ¬x1             000",
                "  {1, 5}      x1 , x2               110",
                "  {2, 5}      x2 , x2               010",
                "  {3, 5}      ¬x3 , x2              010",
                "  {1, 6}      x1 , x3               101",
                "  {2, 6}      x2 , x3               011",
                "",
                "every one of the 7 satisfies the formula          sound",
                "three sets land on 010                            not injective",
                "the 6 models are 000 010 110 101 011 111; 111 is the image of nothing   not onto",
            ],
            "after": [
                "The three sets landing on `010` are the clause-with-two-true-literals case. "
                "Under `010` the first clause is satisfied by `x2` and by `not x3`, and the "
                "second by `x2`, so there is more than one way to choose a witness and each "
                "choice is a different independent set. Nothing distinguishes them and the map "
                "back cannot see the difference.",
                "The unhit model is the other failure of symmetry, and it has a different cause. "
                "Two chosen literals can make at most two variables true, so a model with three "
                "true variables has no preimage. Adding a third clause changes this: the panel's "
                "three-clause example has 9 vertices, 12 independent sets of size 3, 5 models, "
                "and every model is hit.",
                "For a faded rehearsal, switch to the formula with a repeated literal and "
                "predict the vertex count before running it. The supplied first move: vertices "
                "count occurrences, so a clause writing `x1` twice still contributes three. Say "
                "how many edges that clause's triangle contributes and whether the two copies "
                "can both be chosen, then check.",
            ],
        },
        "quiz_title": "What a reduction promises, and what it does not",
        "quiz": [
            {"q": "`A ≤p B` holds. Which conclusion follows?",
             "a": ["A polynomial-time algorithm for `B` gives one for `A`",
                   "A polynomial-time algorithm for `A` gives one for `B`",
                   "`A` and `B` have the same solutions",
                   "`B` is in `NP`"],
             "c": 0,
             "why": "Map the instance and run the algorithm for `B`: that solves `A`. So "
                    "tractability flows backwards along the arrow and hardness flows forwards. "
                    "The solution sets need not correspond at all, as this lesson's own map "
                    "shows, and nothing about membership of `NP` follows from a reduction "
                    "alone."},
            {"q": "The lab reports 7 independent sets of size 2 and 6 satisfying assignments. Is the reduction broken?",
             "a": ["Yes: a correct reduction must make the two counts equal",
                   "Yes: it means some independent set maps to a non-model",
                   "No: the reduction preserves whether the answer is yes, and the counts are free to differ",
                   "No, but only because 7 is larger than 6"],
             "c": 2,
             "why": "The requirement is that one list is non-empty exactly when the other is. "
                    "Here both are non-empty and the answers agree. The second answer names a "
                    "real defect &mdash; it would be unsoundness &mdash; but the panel checks "
                    "every one of the seven against the formula and all seven satisfy it. Which "
                    "count is larger is not the point either: an unsatisfiable formula makes both "
                    "zero."},
            {"q": "Why does the map back leave `111` with no preimage?",
             "a": ["Because `111` does not satisfy the formula",
                   "Because the two chosen literals can make at most two variables true, and unmentioned variables are set false",
                   "Because the triangle edges forbid it",
                   "Because the graph has only six vertices"],
             "c": 1,
             "why": "`111` does satisfy both clauses, so it is a genuine model that the map "
                    "misses. The size of the independent set is the number of clauses, so at "
                    "most that many variables get named, and the convention for the rest is "
                    "false. The triangles constrain which sets are independent, not which "
                    "assignments are images, and the vertex count is a consequence of the clause "
                    "count rather than a cause."},
            {"q": "You verify on this formula that the induced map is not onto. What have you learned about the reduction in general?",
             "a": ["That it is never onto",
                   "That it is onto only for unsatisfiable formulas",
                   "That being onto is not a property of the reduction, since the three-clause example in the same panel is onto",
                   "That the reduction is unsound"],
             "c": 2,
             "why": "One instance is one instance, and here the panel makes that unusually easy "
                    "to check: the same construction on a three-clause formula hits every model. "
                    "So &ldquo;onto&rdquo; is a property of the instance, not of the "
                    "construction, and a page that measured it once and reported it as a "
                    "property of the reduction would be wrong for exactly this reason."},
        ],
        "mistakes": [
            ("Writing bijection over an arrow",
             "It is the single most common false claim about reductions, and no markup check "
             "anywhere would catch it. Of the reductions built on this course some do induce a "
             "bijection on solutions and some do not, and the only way to know which is to "
             "enumerate both sides and compare them as sets."),
            ("Proving only that a solution maps back",
             "Soundness alone permits a construction that turns a no instance into a yes "
             "instance, which destroys the reduction while leaving every mapped-back solution "
             "genuine. The forward half &mdash; building a solution of the transformed instance "
             "from each solution of the original &mdash; is the half that rules that out."),
            ("Counting literals instead of occurrences",
             "The gadget needs one vertex per occurrence. Merging the two copies of a repeated "
             "literal into one vertex changes the triangle, changes the target, and breaks the "
             "argument that an independent set of size `m` touches every clause. The panel's "
             "repeated-literal example is there to be tried for this reason."),
        ],
        "standard": (
            "Finish when you can build the graph from a formula on paper and say what the induced map does.",
            "You should be able to state the definition of a polynomial-time reduction and the "
            "direction hardness travels, construct the triangles and contradiction edges for a "
            "formula of your own, prove both directions, and give the three verdicts on the "
            "induced map separately with a reason for each.",
        ),
        "note": (
            "The three verdicts here were computed on one formula. &ldquo;What the Solution Map "
            "Preserves&rdquo; adds a single clause to it and watches one of the three change, "
            "which is this Subject's hazard arriving at the level of a proof rather than a count."
        ),
    },

    # ---------------------------------------------------------------- 03
    {
        "slug": "what-the-solution-map-preserves",
        "title": "What the Solution Map Preserves",
        "module": "Hardness that travels",
        "one_line": "Add one clause to the same formula and watch a property of the reduction stop being a property of the reduction.",
        "summary": (
            "The same construction, one clause larger: 9 vertices, 15 edges, 12 independent sets "
            "of size 3 and 5 satisfying assignments. Two of the three verdicts are unchanged and "
            "one has flipped &mdash; every model is now the image of at least one set. A "
            "property measured on one instance and reported as a property of the construction is "
            "the Subject's hazard, and here it can be watched happening."
        ),
        "key": [
            "3 clauses  →  9 vertices, 15 edges, k = 3",
            "12 independent sets of size 3 against 5 satisfying assignments",
            "",
            "sound      yes, on both formulas",
            "injective  no, on both:  110, 101 and 011 have three preimages each",
            "onto       NO on the two-clause formula, YES on this one",
            "",
            "the reduction did not change; the instance did",
        ],
        "key_label": "The same construction on a larger formula, and the verdict that moved",
        "concepts_intro": (
            "One idea about reductions, one about what makes a property belong to a construction "
            "rather than to an instance, and one about the only invariant that the definition of "
            "a reduction actually guarantees."
        ),
        "concepts": [
            ("A property of the map can depend on the instance",
             "Soundness is a theorem: it is proved for every formula, and the panel's check is a "
             "confirmation rather than the evidence. Surjectivity is not. On two clauses one "
             "model has no preimage; on three clauses every model has one. The construction is "
             "identical in both cases, so whatever caused the difference lives in the formula, "
             "and any sentence beginning &ldquo;this reduction is onto&rdquo; is missing a "
             "quantifier."),
            ("Why the extra clause closes the gap",
             "An independent set here has one vertex per clause, so `k = m` literals are chosen "
             "and at most `m` variables are named; every unnamed variable is left false. With "
             "two clauses at most two of three variables can be made true, so the all-true model "
             "is unreachable. With three clauses three literals are chosen, and there is a way "
             "to choose them naming all three variables positively, so the all-true model "
             "becomes an image. Nothing was fixed; the budget grew."),
            ("Only the yes-or-no answer is guaranteed",
             "It is worth being blunt about what survives every instance: the formula is "
             "satisfiable exactly when the graph has an independent set of size `m`. Every other "
             "correspondence between the two solution sets is a fact about the pair of instances "
             "in front of you. The panel computes all of them and labels each separately, which "
             "is the only honest way to present a property that is sometimes true."),
        ],
        "read_title": "One more clause, and which of the three verdicts survives it",
        "read_intro": "The larger construction, the counts on both sides, the three verdicts compared with the smaller formula, and what quantifier each of them needs.",
        "body": [
            ("p", "The formula is `(x1 or x2 or not x3) and (not x1 or x2 or x3) and (x1 or not "
                  "x2 or x3)`: the formula from the previous construction with a third clause "
                  "added. The graph has 9 vertices &mdash; three literal occurrences per clause "
                  "&mdash; and 15 edges: 9 triangle edges and 6 contradiction edges. The target "
                  "is `k = 3`."),
            ("h3", "Counting the edges, so the picture is not taken on trust"),
            ("math", [
                "triangles          3 clauses × 3 edges                      9",
                "contradictions     x1 at v1 against ¬x1 at v4               1",
                "                   x2 at v2, v5 against ¬x2 at v8           2",
                "                   ¬x3 at v3 against x3 at v6, v9           2",
                "                   x1 at v7 against ¬x1 at v4               1",
                "                                                      total 15",
            ]),
            ("p", "The panel reports 12 independent sets of size 3 and 5 satisfying assignments, "
                  "and then the three verdicts. Sound: yes, as before and as proved. Injective: "
                  "no, as before &mdash; three of the twelve sets land on `110`, three on `101`, "
                  "three on `011`, two on `111` and one on `000`. Onto: yes, which is the "
                  "verdict that has moved."),
            ("def", ("Sound, injective, onto",
                     "For the map carrying each solution of the transformed instance back to a "
                     "solution of the original: <strong>sound</strong> means every image really "
                     "is a solution of the original; <strong>injective</strong> means no two "
                     "solutions share an image; <strong>onto</strong> means every solution of "
                     "the original is an image. A map with all three is a bijection on "
                     "solutions, and the definition of a reduction requires none of them &mdash; "
                     "only that one solution set is empty exactly when the other is.")),
            ("h3", "What changed, and what a careful sentence about it looks like"),
            ("p", "On the two-clause formula the all-true assignment satisfies both clauses and "
                  "has no preimage, because two chosen literals cannot make three variables "
                  "true. On the three-clause formula the set consisting of `x2` in the first "
                  "clause, `x3` in the second and `x1` in the third is independent &mdash; the "
                  "three lie in different clauses and no two contradict &mdash; and it names all "
                  "three variables positively. So the all-true assignment is now an image, and "
                  "so is every other model."),
            ("p", "The correct sentence is therefore: <em>on this formula</em> the induced map is "
                  "onto. The incorrect sentence, which is shorter and reads better, is that the "
                  "reduction is onto. Both describe the same measurement; only one of them "
                  "survives the reader trying it on a different instance, which the panel makes "
                  "a one-click experiment."),
            ("example", ("A verdict that holds on every instance, for contrast",
                         "Soundness is checked here too, on all twelve sets, and it passes. But "
                         "the reason to believe it is the proof in &ldquo;A Reduction Is a Construction&rdquo;, which "
                         "quantifies over every formula; the twelve checks are a test of the "
                         "implementation. Knowing which of the panel's verdicts are theorems "
                         "under test and which are measurements is the skill this page is "
                         "training.")),
            ("p", "There is one more asymmetry worth naming. The failure of injectivity has a "
                  "structural cause that does hold for every formula: a clause with two or more "
                  "true literals always admits more than one choice of witness, and every "
                  "satisfying assignment of a formula with such a clause therefore has several "
                  "preimages. So &ldquo;not injective in general&rdquo; is defensible in a way "
                  "that &ldquo;not onto in general&rdquo; is not &mdash; and the difference is "
                  "not visible in the two panels, which report both as a verdict on an instance."),
            ("p", "That last point is the reason this lesson exists rather than being a footnote "
                  "to the previous one. Two verdicts printed in the same style, in the same "
                  "panel, computed by the same routine, can have completely different logical "
                  "status. The lab cannot tell you which is which. The proof can."),
        ],
        "lab": ("reduction", {"mode": "independentset", "preset": "three"}),
        "steps_title": "Deciding whether a measured property belongs to the construction",
        "steps_intro": "Four questions to ask before writing a property of a reduction down as a fact about it.",
        "steps": [
            ("State the property with its quantifier in front",
             "&ldquo;For every formula&rdquo; or &ldquo;for this formula&rdquo;. If the sentence "
             "reads naturally without one, it is ambiguous, and the ambiguous reading is the "
             "stronger claim. This is the whole discipline and the rest of these steps are ways "
             "of testing it."),
            ("Try to derive the property from the construction alone",
             "Soundness follows from the triangles and the contradiction edges, with no reference "
             "to any particular formula, so it is general. Try the same for surjectivity and the "
             "argument stalls at exactly the place where the clause count and the variable count "
             "have to be compared, which is instance data."),
            ("Find a second instance where the property could fail",
             "Fewer clauses than variables is the shape that breaks surjectivity here, and the "
               "two-clause formula is the smallest case of it. A property you cannot attack is "
               "one you have not tested; look for the instance that stresses the quantity the "
               "argument depended on."),
            ("Separate a failure that is structural from one that is incidental",
             "Injectivity fails whenever some clause has two true literals, which is a condition "
             "on the assignment rather than on the reduction, and is met by almost every "
             "interesting formula. Surjectivity fails only when the budget of chosen literals is "
             "too small to name the variables a model needs true. One of those generalises and "
             "the other does not."),
        ],
        "worked": {
            "title": "Twelve independent sets, five models, and who lands where",
            "intro": [
                "Vertices 1, 2, 3 hold `x1`, `x2`, `not x3`; vertices 4, 5, 6 hold `not x1`, "
                "`x2`, `x3`; vertices 7, 8, 9 hold `x1`, `not x2`, `x3`. The right column is the "
                "assignment the set reads back to.",
            ],
            "lines": [
                "  {1, 5, 7} → 110      {2, 5, 7} → 110      {3, 5, 7} → 110",
                "  {1, 6, 7} → 101      {1, 6, 8} → 101      {1, 6, 9} → 101",
                "  {2, 4, 9} → 011      {2, 5, 9} → 011      {2, 6, 9} → 011",
                "  {2, 6, 7} → 111      {1, 5, 9} → 111",
                "  {3, 4, 8} → 000",
                "",
                "  12 sets, 5 models, every model hit at least once",
                "",
                "the two-clause formula, for comparison:",
                "   7 sets, 6 models, and 111 the image of nothing",
                "",
                "  sound      yes        yes",
                "  injective  no         no",
                "  onto       YES        no",
            ],
            "after": [
                "The set `{2, 6, 7}` is the one worth reading twice. It takes `x2` from the first "
                "clause, `x3` from the second and `x1` from the third; no two of the three lie in "
                "one clause and no two contradict, so it is independent; and it names all three "
                "variables positively, so it reads back to the all-true assignment. On the "
                "two-clause formula there is no set of this kind because there are only two "
                "literals to choose.",
                "The single set landing on `000` is the mirror image and is worth the same look. "
                "It chooses `not x3`, `not x1` and `not x2`, one per clause, and every variable "
                "it names is made false. It is the only way to reach the all-false model, so that "
                "model has exactly one preimage while three others have three each.",
                "For a faded rehearsal, delete the third clause in the box, note the verdict "
                "change, then add a fourth clause instead and predict what happens before "
                "running it. The supplied first move: more clauses means a larger `k`, so more "
                "variables can be named &mdash; but more clauses also means fewer models. Say "
                "which of the two effects decides surjectivity, and then check.",
            ],
        },
        "quiz_title": "Which verdicts need a quantifier",
        "quiz": [
            {"q": "The panel says the induced map is onto for this formula and not onto for the two-clause one. What does that establish?",
             "a": ["That the implementation is inconsistent",
                   "That surjectivity is a property of the instance, not of the construction",
                   "That the reduction is only valid for formulas with at least three clauses",
                   "That the two-clause construction is unsound"],
             "c": 1,
             "why": "The construction is the same routine in both cases and both reductions are "
                    "valid: in each, the formula is satisfiable exactly when the graph has an "
                    "independent set of the target size. What differs is a property of the map "
                    "between the solution sets, and it differs because the instances differ."},
            {"q": "Which of the three verdicts is a theorem rather than a measurement?",
             "a": ["Soundness, which follows from the triangles and the contradiction edges for every formula",
                   "Injectivity, which fails only on small formulas",
                   "Surjectivity, which the larger example confirms",
                   "All three, since the lab checks all three"],
             "c": 0,
             "why": "Soundness is proved from the construction with no reference to a particular "
                    "formula, and the lab's check of it is a test of the implementation. The "
                    "other two are computed on the instance in the box. That the lab reports all "
                    "three in the same style is exactly why knowing their status matters."},
            {"q": "On this formula, three independent sets map to `110`. What causes the collision?",
             "a": ["Two clauses contain the same literal",
                   "The assignment makes more than one literal true in some clause, so there is more than one witness to choose",
                   "The graph has a vertex of degree three",
                   "The target `k` is smaller than the number of variables"],
             "c": 1,
             "why": "Under `110` the first clause has `x1` and `x2` both true and the third has "
                    "`x1` and `not x2` &mdash; wherever a clause has several true literals the "
                    "witness can be chosen several ways, and each choice is a different "
                    "independent set reading back to the same assignment. The degree of a vertex "
                    "and the relation between `k` and the variable count are not what the map "
                    "collapses over."},
            {"q": "A colleague writes: &ldquo;the 3-SAT to independent set reduction induces a surjection on solutions&rdquo;. What is the minimum correction?",
             "a": ["Delete the sentence: it is false on every formula",
                   "Replace `surjection` with `bijection`",
                   "Add the instance: it is true of this formula and false of the two-clause one in the same panel",
                   "Nothing: the larger example verifies it"],
             "c": 2,
             "why": "The sentence is not always false and not always true, which is the worst "
                    "kind of claim to leave unquantified. It is also not a bijection here, since "
                    "three sets share an image. And a single verifying example is what produced "
                    "the wrong sentence in the first place."},
        ],
        "mistakes": [
            ("Generalising from the instance the panel happened to load",
             "Both of these formulas are defaults in the same control. Whichever one is on screen "
             "when the verdict is read becomes, if you are not careful, the verdict for the "
             "reduction. The correction is mechanical: write the instance into the sentence, and "
             "then see whether the sentence still says anything interesting."),
            ("Treating all three verdicts as the same kind of fact",
             "They are printed identically and they are not alike. One is a theorem being "
             "regression-tested, one fails for a structural reason that generalises, and one is a "
               "measurement that goes either way. A page cannot mark that difference in the "
               "numbers, so the reader has to."),
            ("Concluding that a non-bijective reduction is defective",
             "Nothing is wrong. The definition asks for the answers to agree and they do. A "
             "reduction that also happened to be a bijection on solutions would be a stronger "
             "object with a stronger use &mdash; counting solutions, for instance &mdash; and "
             "this one simply is not that object."),
        ],
        "standard": (
            "Finish when you can say, of any property a reduction lab prints, whether it needs the instance named.",
            "You should be able to derive soundness from the construction without naming a "
            "formula, explain why the number of chosen literals bounds the number of true "
            "variables, produce an instance on which the induced map is not onto, and separate a "
            "structural failure from an incidental one.",
        ),
        "note": (
            "This has been one reduction looked at twice. &ldquo;One Structure, Three "
            "Problems&rdquo; goes the other way: a map so tight that it holds on every subset of "
            "the vertices rather than only on the solutions, checked on all 32 of them."
        ),
    },

    # ---------------------------------------------------------------- 04
    {
        "slug": "one-structure-three-problems",
        "title": "One Structure, Three Problems",
        "module": "Hardness that travels",
        "one_line": "Check on all 32 subsets of a five-cycle that a set is independent exactly when its complement covers and exactly when it is a clique in the complement.",
        "summary": (
            "Independent set, vertex cover and clique are the same question in three notations, "
            "and the translation is not an approximation or a correspondence between optima "
            "&mdash; it is an identity holding on every subset of the vertices. The lab checks "
            "it on all 32 subsets of a five-cycle rather than on the largest one, because an "
            "identity tested only at the optimum is tested at its easiest case."
        ),
        "key": [
            "S is independent in G   ⟺   V − S is a vertex cover of G",
            "S is independent in G   ⟺   S is a clique in the complement of G",
            "",
            "on the five-cycle: 11 independent sets = 11 covers = 11 cliques, over 32 subsets",
            "α = 2,  τ = 3,  α + τ = 5 = n",
            "",
            "three problems, one structure — so a hardness result about one is about all three",
        ],
        "key_label": "Two equivalences, checked on every subset rather than on the optimum",
        "concepts_intro": (
            "The first idea is the identity itself, which is one line and is the tightest "
            "relationship on this course. The second is why checking it at the optimum would be "
            "checking almost nothing. The third is what the identity does and does not transfer."
        ),
        "concepts": [
            ("Complementing the set, and complementing the graph",
             "Two different complements are at work and confusing them is the usual error. "
             "Taking `V - S` complements the SET and turns an independent set into a vertex "
             "cover of the same graph. Taking the complement GRAPH, where `u` and `v` are joined "
             "exactly when they were not, turns an independent set into a clique on the same "
             "vertices. Each equivalence is an immediate consequence of the definitions, and "
             "together they say that three problem names describe one piece of structure."),
            ("An identity checked at the optimum is barely checked",
             "The relation `α + τ = n` between the largest independent set and the smallest cover "
             "is a corollary, and it is the form most often quoted. It is also the weakest test "
             "of the underlying claim: it compares two numbers on one pair of sets. The panel "
             "instead walks all 32 subsets and asks, for each, whether the three verdicts agree "
             "&mdash; 32 tests of the equivalence rather than one test of its consequence."),
            ("What transfers, and in which direction",
             "Because the map is a bijection on instances and on solutions, a hardness result "
             "about any one of the three transfers to the other two, and so does a polynomial "
             "algorithm. That symmetry is unusual: most reductions on this course run one way "
             "only. It also means that a special case where one of them is easy is a special "
             "case where all three are, which is the shape the vertex cover lesson later depends "
             "on."),
        ],
        "read_title": "Two equivalences, the identity they imply, and the enumeration that tests them",
        "read_intro": "The three problems, the two one-line proofs, the corollary about the optima, and what the lab checks on every subset.",
        "body": [
            ("def", ("Three problems on one graph",
                     "An <strong>independent set</strong> is a set of vertices no two of which "
                     "are joined. A <strong>vertex cover</strong> is a set of vertices touching "
                     "every edge. A <strong>clique</strong> is a set of vertices every two of "
                     "which are joined. Write `α` for the size of the largest independent set "
                     "and `τ` for the size of the smallest vertex cover.")),
            ("thm", ("The two equivalences",
                     "For every subset `S` of the vertices of a graph `G`: `S` is independent in "
                     "`G` if and only if `V - S` is a vertex cover of `G`; and `S` is "
                     "independent in `G` if and only if `S` is a clique in the complement of "
                     "`G`.")),
            ("proof", ("Take an edge `uv`. If `S` is independent it does not contain both ends, "
                       "so at least one end is in `V - S`, so `V - S` touches every edge and is "
                       "a cover. Conversely if `V - S` is a cover then no edge has both ends "
                       "outside it, that is, no edge has both ends in `S`, so `S` is "
                       "independent.",
                       "For the second: `S` is independent in `G` exactly when no pair inside "
                       "`S` is joined in `G`, which is exactly when every pair inside `S` is "
                       "joined in the complement, which is exactly when `S` is a clique there. "
                       "Both arguments are the definition read twice, and that is why the "
                       "equivalence holds subset by subset rather than only at the extremes.")),
            ("thm", ("Gallai's identity",
                     "`α + τ = n` for every graph on `n` vertices.")),
            ("proof", ("If `S` is a largest independent set then `V - S` is a cover of size "
                       "`n - α`, so `τ ≤ n - α`. If `C` is a smallest cover then `V - C` is "
                       "independent of size `n - τ`, so `α ≥ n - τ`, that is `τ ≥ n - α`. The "
                       "two inequalities give `τ = n - α`.")),
            ("h3", "What the lab measured on the five-cycle"),
            ("p", "The loaded graph is the cycle on five vertices. The panel reports 32 subsets "
                  "checked, 11 independent sets, 11 vertex covers and 11 cliques in the "
                  "complement; `α = 2`, `τ = 3`, and `α + τ = 5`, which is `n`. The two "
                  "equivalences are reported as holding on every one of the 32, not as holding "
                  "at the optimum &mdash; the panel says how many subsets it checked precisely so "
                  "that the difference is visible."),
            ("p", "That the three counts are equal is a consequence of the equivalences and a "
                  "useful check on them, since a mismatch anywhere would separate them. It is "
                  "worth noticing that 11 is not a round number and is not `2^5` divided by "
                  "anything obvious: it is whatever the graph gives, and both sides give it."),
            ("example", ("The complement of a five-cycle is a five-cycle",
                         "Joining the pairs the cycle leaves out gives the edges 1-3, 1-4, 2-4, "
                         "2-5 and 3-5, which form the cycle 1, 3, 5, 2, 4. So this graph is "
                         "isomorphic to its own complement, and the clique problem on the "
                         "complement is the independent set problem on another five-cycle. The "
                         "largest clique there has 2 vertices, matching `α`.")),
            ("h3", "Why this matters for the rest of the course"),
            ("p", "Everything proved hard for one of these three is hard for the other two, with "
                  "no new gadget. That is why the approximation lessons later on can talk about "
                  "vertex cover while the reduction lessons talked about independent set, and "
                  "why the two are not two subjects. It also sets up a warning: the "
                  "approximability of the three is <em>not</em> shared, because an "
                  "approximation ratio is a statement about sizes and the map `S ↦ V - S` does "
                  "not preserve ratios. A cover within a factor 2 of the smallest says nothing "
                  "useful about the largest independent set."),
            ("p", "So the identity transfers exact answers perfectly and approximate answers not "
                  "at all. Both halves of that sentence are worth holding, because the first "
                  "makes the three problems interchangeable in the hardness chapters and the "
                  "second makes them completely different problems in the approximation ones."),
        ],
        "lab": ("reduction", {"mode": "complement", "preset": "cycle5"}),
        "steps_title": "Translating between the three, without losing what does not translate",
        "steps_intro": "The translation is mechanical; the discipline is in knowing which quantities survive it.",
        "steps": [
            ("Name which complement you are taking",
             "Complementing the set gives a cover of the same graph. Complementing the graph "
             "gives a clique on the same vertices. Writing &ldquo;the complement&rdquo; without "
             "saying which is the fastest way to produce a sentence that is half right."),
            ("Check the equivalence on a subset that is not optimal",
             "Take any set at all &mdash; a single vertex, the empty set, everything &mdash; and "
             "run the three tests. The claim is subset by subset, so a non-optimal subset is a "
             "legitimate test and a much more informative one than the extreme case."),
            ("Use the identity to convert exact answers only",
             "`α + τ = n` converts an exact largest independent set into an exact smallest cover "
             "and back. Do not push an approximation through it: a cover that is twice the "
             "smallest gives an independent set with no ratio guarantee whatever, and the "
             "arithmetic that looks like it should work does not."),
            ("Carry hardness in the direction you need it",
             "A reduction into independent set plus this equivalence is a reduction into vertex "
             "cover and into clique, at no cost. When you need a problem to be hard, reduce to "
             "whichever of the three is most convenient and translate."),
        ],
        "worked": {
            "title": "All 32 subsets of the five-cycle, and the three columns that agree",
            "intro": [
                "The graph is the cycle `1-2, 2-3, 3-4, 4-5, 5-1`. Its complement has the edges "
                "`1-3, 1-4, 2-4, 2-5, 3-5`. A few subsets of each size, with the three verdicts.",
            ],
            "lines": [
                "   S            independent in G   V − S covers G   S a clique in the complement",
                "",
                "   {}                 yes                yes                  yes",
                "   {1}                yes                yes                  yes",
                "   {1, 3}             yes                yes                  yes",
                "   {1, 2}             no                 no                   no",
                "   {1, 3, 5}          no                 no                   no",
                "   {2, 4, 5}          no                 no                   no",
                "   {1, 2, 3, 4}       no                 no                   no",
                "",
                "   over all 32 subsets:   11 independent   11 covers   11 cliques",
                "   no subset on which the three verdicts disagree",
                "",
                "   α = 2   attained by {1, 3}",
                "   τ = 3   attained by {1, 2, 4}",
                "   α + τ = 5 = n",
            ],
            "after": [
                "The subset `{1, 3, 5}` is the one to look at hardest. It is three vertices of a "
                "five-cycle and it is not independent, because 5 and 1 are adjacent. Its "
                "complement `{2, 4}` misses the edge 5-1, so it is not a cover. And in the "
                "complement graph 1 and 3 are joined but 3 and 5 are joined while 5 and 1 are "
                "not, so it is not a clique. Three different-looking checks, one answer, and none "
                "of them involved an optimum.",
                "The empty set and the full set are the degenerate rows and they are included on "
                "purpose. The empty set is independent, its complement is everything and covers, "
                "and it is vacuously a clique. A routine that special-cased the extremes would "
                "pass a check that skipped them.",
                "For a faded rehearsal, switch to the two disjoint triangles and predict the "
                "three counts before running it. The supplied first move: an independent set can "
                "take at most one vertex from each triangle, so count the sets of size 0, 1 and 2 "
                "by hand. Then say what the complement graph looks like, and check `α + τ` "
                "against 6.",
            ],
        },
        "quiz_title": "Three names, one structure",
        "quiz": [
            {"q": "`S` is an independent set of a graph on 9 vertices, and `|S| = 4`. What follows about vertex covers?",
             "a": ["There is a vertex cover of size 5",
                   "The smallest vertex cover has size 5",
                   "There is a vertex cover of size 4",
                   "Nothing, unless `S` is the largest independent set"],
             "c": 0,
             "why": "`V - S` has 5 vertices and covers every edge, so a cover of that size "
                    "exists. It need not be the smallest &mdash; that would need `S` to be "
                    "largest, and `α + τ = n` is about the extremes. The equivalence itself "
                    "holds for every subset, which is why something does follow here."},
            {"q": "Why does the lab check the equivalence on all 32 subsets rather than at the optimum?",
             "a": ["Because the optimum is expensive to compute",
                   "Because the claim is about every subset, and the optimum is the case most likely to pass anyway",
                   "Because `α + τ = n` can fail on small graphs",
                   "Because independent sets and cliques differ on non-optimal subsets"],
             "c": 1,
             "why": "The theorem quantifies over subsets, so testing it only where both sides are "
                    "extreme tests the weakest instance of it. `α + τ = n` never fails, and the "
                    "three verdicts never disagree on any subset &mdash; which is precisely what "
                    "32 checks establish and one check does not."},
            {"q": "You have an algorithm returning a vertex cover at most twice the smallest. Using `α + τ = n`, what can you say about independent sets?",
             "a": ["It gives an independent set at least half the largest",
                   "It gives an independent set at least `n/2`",
                   "Essentially nothing: subtracting from `n` destroys the ratio",
                   "It gives the largest independent set exactly"],
             "c": 2,
             "why": "If `τ = 10` and `n = 100`, then `α = 90`; a cover of size 20 leaves an "
                    "independent set of 80, which is comfortably within a factor. But if "
                    "`τ = 49` and `n = 100`, then `α = 51`, and a cover of 98 leaves an "
                    "independent set of 2. The identity converts exact answers and not "
                    "approximate ones, and this is the standard trap it sets."},
            {"q": "The complement of the loaded five-cycle turns out to be another five-cycle. What does that tell you?",
             "a": ["That every cycle is self-complementary",
                   "That the largest clique in the complement has the same size as the largest independent set here, which the panel confirms as 2",
                   "That `α = τ` for this graph",
                   "That the graph has no vertex cover"],
             "c": 1,
             "why": "The equivalence already guarantees the clique and independent set numbers "
                    "match; the self-complementary shape is a pleasant fact about this particular "
                    "graph, not a general one &mdash; the six-cycle's complement is not a cycle. "
                    "And `α = 2` while `τ = 3`, so they are not equal here."},
        ],
        "mistakes": [
            ("Confusing the two complements",
             "&ldquo;Take the complement&rdquo; means the set in one equivalence and the graph in "
             "the other. Taking the complement graph and then looking for a cover in it, or "
             "taking `V - S` and then looking for a clique, produces statements that are false "
             "and look like the theorem."),
            ("Pushing an approximation through the identity",
             "The identity is exact and the arithmetic with it is subtraction, which does not "
             "preserve ratios. This is not a technicality: vertex cover has a 2-approximation and "
             "the maximum independent set has no constant-factor approximation at all unless "
             "`P = NP`, and these two facts sit on either side of a subtraction."),
            ("Reading 11 = 11 = 11 as the theorem",
             "Equal counts are a consequence and a good check. The theorem is that the three "
             "verdicts agree subset by subset, and three equal totals could in principle arise "
             "from disagreements that cancel. The panel reports both the counts and the "
             "subset-by-subset verdict for that reason."),
        ],
        "standard": (
            "Finish when you can move a problem between the three forms and say which quantities survive the move.",
            "You should be able to prove both equivalences in a line each, derive `α + τ = n` "
            "from them, check the equivalence on a non-optimal subset of a graph you drew "
            "yourself, and explain why an approximation ratio does not transfer across the "
            "identity.",
        ),
        "note": (
            "Every reduction so far has been graph to graph or formula to graph. &ldquo;Numbers "
            "as Gadgets&rdquo; changes the material: the transformed instance is a list of "
            "integers, and the reason the construction works is that no column of a base-ten "
            "addition can carry."
        ),
    },

    # ---------------------------------------------------------------- 05
    {
        "slug": "numbers-as-gadgets",
        "title": "Numbers as Gadgets, and Weak Hardness",
        "module": "Hardness that travels",
        "one_line": "Turn two clauses into eight base-ten numbers, add up every digit in every column, and watch the largest total come out at 5 against a base of 10.",
        "summary": (
            "The transformed instance here is not a graph, it is a list of integers, and the "
            "construction is a table of digits. The reason it works is arithmetical: the largest "
            "column total is 5 and the base is 10, so no column can carry into the next and the "
            "columns are independent. The lab adds every digit of every row to check that, and "
            "the same page explains why a problem with a table-filling algorithm is NP-hard "
            "anyway."
        ),
        "key": [
            "one column per variable and one per clause; two numbers per variable, two slack per clause",
            "target: 1 in every variable column, 4 in every clause column",
            "",
            "2 variables, 2 clauses  →  8 numbers of 4 digits, target 1144",
            "largest column total 5, against the base 10, so no column can carry",
            "2 subsets reach the target, 2 satisfying assignments, and the map is a bijection",
            "",
            "the table is O(n · target); the target has n + m digits, so it is exponential in the input",
        ],
        "key_label": "A digit table, the carry that cannot happen, and the target 1144",
        "concepts_intro": (
            "The first idea is that a number can be a data structure. The second is the "
            "arithmetical fact the whole construction rests on and that readers skip. The third "
            "is the distinction between a problem that is hard in the size of its input and one "
            "that is hard in the magnitude of its numbers."
        ),
        "concepts": [
            ("A number is a row of independent columns",
             "Each variable gets a number for `x` true and a number for `x` false, each carrying "
             "a 1 in its own variable column and a 1 in every clause column the literal "
             "satisfies. The target has 1 in each variable column, which forces exactly one of "
             "each pair into the subset, and 4 in each clause column. So choosing a subset that "
             "hits the target <em>is</em> choosing an assignment, and the arithmetic does the "
             "work the triangles did in the graph construction."),
            ("No column can carry, and that is a computed fact",
             "The construction is nonsense if a column can carry, because then a shortfall in one "
             "column could be made up by an excess in another and the columns would stop "
             "encoding independent constraints. The panel adds every digit of every row, whether "
             "the row is in the subset or not: a variable column totals 2 and a clause column "
             "totals at most 6 &mdash; three literal occurrences plus the slack numbers 1 and 2. "
             "Six is less than ten. On the loaded formula the largest total is 5 and the panel "
             "prints it against the base."),
            ("Weakly NP-hard: hard in the magnitude, not in the digits",
             "Subset sum has a dynamic programme filling a table of size proportional to the "
             "number of items times the target, which Dynamic Programming and Optimal Substructure built. That is "
             "polynomial in the target's <em>value</em> and exponential in its number of digits, "
             "and the input is the digits. Here the target has one digit per variable plus one "
             "per clause, so the numbers this reduction produces are astronomically large in the "
             "formula's size and the table is no help. A problem hard only when its numbers are "
             "large is <strong>weakly</strong> NP-hard, and subset sum is the standard example."),
        ],
        "read_title": "The digit table, the no-carry argument, and what the pseudo-polynomial table does not buy",
        "read_intro": "The construction, the target, the column totals the lab adds, the bijection on solutions, and the two senses in which a problem can be hard.",
        "body": [
            ("def", ("Subset sum",
                     "Given a list of positive integers and a target, is there a sublist adding "
                     "to the target exactly? The input is the digits of the numbers, which "
                     "matters for every complexity claim on this page: a list of ten numbers with "
                     "a thousand digits each is a large input, and a list of ten numbers under "
                     "100 is a small one.")),
            ("h3", "The construction"),
            ("ol", [
                "One column per variable and one per clause, so `n + m` columns, read in base ten.",
                "For each variable, a number `x true` with a 1 in that variable's column and a 1 "
                "in every clause column the positive literal satisfies; and a number `x false` "
                "with a 1 in the variable's column and a 1 in every clause column the negative "
                "literal satisfies.",
                "For each clause, two <em>slack</em> numbers with a 1 and a 2 in that clause's "
                "column and zeros everywhere else.",
                "The target has a 1 in every variable column and a 4 in every clause column.",
            ]),
            ("thm", ("The construction is a reduction",
                     "The formula is satisfiable if and only if some subset of the constructed "
                     "numbers adds to the target.")),
            ("proof", ("No column can carry, because every column's digits add to at most 6 "
                       "across all the rows, and 6 is less than 10. So a subset hits the target "
                       "exactly when it hits each column's digit separately.",
                       "A variable column can only be reached by that variable's two numbers, "
                       "each contributing 1, and the target is 1, so exactly one of the two is "
                       "chosen: the subset picks an assignment. A clause column receives 1 from "
                       "each chosen literal number that satisfies the clause, so between 0 and 3, "
                       "plus whatever the two slack numbers contribute, which is 0, 1, 2 or 3.",
                       "The target is 4. If the assignment satisfies the clause, the literal "
                       "contribution is 1, 2 or 3 and exactly one of the four slack combinations "
                       "makes up the remaining 3, 2 or 1. If the assignment does not satisfy it, "
                       "the literal contribution is 0 and the slack numbers can supply at most 3, "
                       "so the column cannot reach 4. Hence the subsets that hit the target are "
                       "exactly the satisfying assignments, each with its forced slack choice "
                       "&mdash; which is why the map is not merely sound but a bijection.")),
            ("h3", "What the lab built"),
            ("p", "The loaded formula is `(x1 or x2) and (not x1 or x2)`: two variables, two "
                  "clauses, so four columns. The panel reports 8 numbers of 4 digits, the target "
                  "1144, 2 subsets reaching it, 2 satisfying assignments out of 4, a largest "
                  "column total of 5 against the base 10, and the verdict that the map is a "
                  "bijection &mdash; sound, surjective and injective, all three computed."),
            ("p", "The column totals are 2, 2, 5 and 5. The two variable columns get a 1 from "
                  "each of the variable's two numbers and nothing else. Each clause column gets a "
                  "1 from every literal number satisfying that clause &mdash; two of them here "
                  "&mdash; plus 1 and 2 from the slack, which is 5. Five is comfortably under ten "
                  "and the bar chart draws it against the line."),
            ("p", "Beside the enumeration the panel runs the dynamic programme from Dynamic "
                  "Programming and Optimal Substructure on the same numbers and the same target, and requires the two to agree "
                  "about whether the target is reachable. Two exhaustive routes that agree is "
                  "evidence; one clever route is not, and the two routes here share no code."),
            ("example", ("Both subsets, added in columns",
                         "`x1 false + x2 true + slack 1.1 + slack 1.2 + slack 2.2` is "
                         "`1001 + 0111 + 0010 + 0020 + 0002 = 1144`, and carries back to "
                         "`x1 = F, x2 = T`. The clause-1 column reads 1 from `x2 true` plus 1 and "
                         "2 from the slacks; the clause-2 column reads 1 from `x1 false`, 1 from "
                         "`x2 true` and 2 from a slack. Both reach 4 without help from anywhere "
                         "else in the number.")),
            ("h3", "Two senses of hard, and why the table does not rescue this"),
            ("p", "It is tempting to think a problem with a dynamic programme cannot be NP-hard. "
                  "The table for subset sum has one row per item and one column per value from 0 "
                  "to the target, so its size is proportional to `n` times the target. That is "
                  "polynomial in the target as a NUMBER and exponential in the target as an "
                  "INPUT, because a target with `d` digits has magnitude about `10^d`. Here `d` "
                  "is the number of variables plus the number of clauses, so the table has about "
                  "`10^(n+m)` columns and is not an algorithm anyone can run."),
            ("p", "The distinction has a name and a consequence. A problem that is NP-hard but "
                  "has an algorithm polynomial in the numeric values is <strong>weakly</strong> "
                  "NP-hard; one that stays hard even when the numbers are bounded by a polynomial "
                  "in the input length is <strong>strongly</strong> NP-hard. Only weakly NP-hard "
                  "problems can have the kind of approximation scheme built later on this course, "
                  "and that is not a coincidence: the scheme works by making the numbers small "
                  "enough for the table to fit."),
        ],
        "lab": ("reduction", {"mode": "subsetsum", "preset": "two"}),
        "steps_title": "Reading a digit-table reduction, and checking it cannot carry",
        "steps_intro": "The construction is four lines. The check that makes it valid is one addition per column, and it is the step to do first.",
        "steps": [
            ("Count the columns before writing any number",
             "One per variable, one per clause. The number of columns fixes the width of every "
             "row and the magnitude of every number, and it is the quantity that makes this "
             "reduction produce astronomically large integers from a small formula."),
            ("Add every digit in each column, over every row",
             "Not over the rows in a solution &mdash; over all of them. The question is whether a "
             "carry is possible at all, which is a property of the table rather than of any "
             "subset. The panel prints the totals and colours the bar red if any total reaches "
             "the base."),
            ("Check the forcing in the variable columns",
             "The target digit is 1 and exactly two rows contribute to that column, so exactly "
             "one is chosen. If a construction lets both or neither be chosen it is not encoding "
             "an assignment, and no amount of correct clause arithmetic will repair it."),
            ("Check the slack arithmetic in both directions",
             "A satisfied clause receives 1, 2 or 3 from its literals and the slack numbers can "
             "supply 3, 2 or 1 in exactly one way each. An unsatisfied clause receives 0 and the "
             "slack tops out at 3. Both halves are needed: the first makes the map onto the "
             "models, the second makes it sound."),
            ("Say which quantity the running time is polynomial in",
             "For any algorithm you quote on a numeric problem, name whether the bound is "
             "polynomial in the input length or in the magnitude of the numbers. The two coincide "
             "for graph problems and diverge here, and every confused claim about subset sum "
             "lives in that gap."),
        ],
        "worked": {
            "title": "Eight numbers, four columns, and a target of 1144",
            "intro": [
                "The formula is `(x1 or x2) and (not x1 or x2)`. Columns left to right: `x1`, "
                "`x2`, clause 1, clause 2. A digit of 1 in a clause column means this literal "
                "satisfies that clause.",
            ],
            "lines": [
                "  number        x1   x2   c1   c2      value",
                "",
                "  x1 true        1    0    1    0       1010",
                "  x1 false       1    0    0    1       1001",
                "  x2 true        0    1    1    1        111",
                "  x2 false       0    1    0    0        100",
                "  slack 1.1      0    0    1    0         10",
                "  slack 1.2      0    0    2    0         20",
                "  slack 2.1      0    0    0    1          1",
                "  slack 2.2      0    0    0    2          2",
                "",
                "  target         1    1    4    4       1144",
                "  column total   2    2    5    5      all under 10, so no carry",
                "",
                "  the two subsets that reach it:",
                "    x1 false + x2 true + slack 1.1 + slack 1.2 + slack 2.2 = 1144   →  x1=F x2=T",
                "    x1 true  + x2 true + slack 1.2 + slack 2.1 + slack 2.2 = 1144   →  x1=T x2=T",
                "",
                "  satisfying assignments: 2 of 4      subsets reaching the target: 2",
                "  the map is a bijection: sound, surjective and injective",
            ],
            "after": [
                "Both models have `x2` true, and they must: if `x2` were false the two clauses "
                "would read `x1` and `not x1`. So the `x2 true` row is in both subsets and the "
                "`x2 false` row is in neither, which is the assignment being forced showing up as "
                "a row that is never chosen.",
                "The slack choices are the part worth checking by hand. In the first subset "
                "clause 1 gets 1 from `x2 true` and needs 3 more, so both slacks are taken; "
                "clause 2 gets 1 from `x1 false` and 1 from `x2 true` and needs 2 more, so only "
                "the 2 is taken. Each shortfall has exactly one repair, which is the injectivity "
                "of the map made concrete.",
                "For a faded rehearsal, switch to the single-clause example and predict the "
                "target before running it. The supplied first move: two variables and one clause "
                "means three columns, and the target is 1 in each variable column and 4 in the "
                "clause column. Say what the target is as a number and how many rows there are, "
                "then check &mdash; and note that being right about this table says nothing about "
                "the three-variable one, where the largest column total moves to 6.",
            ],
        },
        "quiz_title": "Digits, carries, and two senses of hard",
        "quiz": [
            {"q": "Why does the construction use base ten rather than base two?",
             "a": ["Because the reader can read decimal",
                   "Because a column must not carry, and the digits in a column can add to 6",
                   "Because binary would make the numbers larger",
                   "Because the target must end in 4"],
             "c": 1,
             "why": "A clause column can receive 1 from each of three literal occurrences plus 1 "
                    "and 2 from the slack numbers, which is 6. Any base above 6 makes carrying "
                    "impossible and keeps the columns independent; base two would carry "
                    "immediately and the construction would collapse. Readability is a side "
                    "benefit, and binary numbers would be the same magnitudes written "
                    "differently."},
            {"q": "The panel reports the largest column total as 5 against the base 10. What claim does that addition support?",
             "a": ["That the subset shown adds to the target",
                   "That no subset can reach the target by borrowing across columns, so each column is an independent constraint",
                   "That there are exactly two solutions",
                   "That the numbers fit in a double"],
             "c": 1,
             "why": "The total is taken over every row whether or not it is in a solution, so it "
                    "is a statement about the table: no carry is possible, therefore hitting the "
                    "target means hitting every column's digit separately. The number of "
                    "solutions and the sum of any particular subset are separate computations on "
                    "the same page."},
            {"q": "Subset sum has a dynamic programme of size `n` times the target. Why is it still NP-hard?",
             "a": ["Because the programme is incorrect for large targets",
                   "Because the target's magnitude is exponential in the number of digits, which is what the input length counts",
                   "Because the table cannot be filled in the right order",
                   "Because the reduction here produces negative numbers"],
             "c": 1,
             "why": "A target written with `d` digits has magnitude around `10^d`, so a table "
                    "with one column per value has exponentially many columns in the input "
                    "length. The programme is correct and its fill order is fine; the numbers "
                    "here are all positive. This is exactly what &ldquo;weakly NP-hard&rdquo; "
                    "names."},
            {"q": "You bound every number in a subset sum instance by `n^2`. What happens?",
             "a": ["The problem stays NP-hard, since it was NP-hard before",
                   "The table becomes polynomial in the input length, so this restricted family is solvable in polynomial time",
                   "The reduction from satisfiability still applies",
                   "The map on solutions stops being a bijection"],
             "c": 1,
             "why": "With the target polynomially bounded the table has polynomially many "
                    "columns and the dynamic programme is a polynomial algorithm for that family. "
                    "The reduction does not apply because it produces numbers with `n + m` "
                    "digits, far above any polynomial bound. Restricting an NP-hard problem can "
                    "certainly produce a tractable family, and that observation is the whole of "
                    "the special-case strategy."},
        ],
        "mistakes": [
            ("Assuming no carry instead of computing it",
             "The independence of the columns is the entire reduction and it is one addition per "
             "column to check. A construction with a base that is too small is wrong in a way "
             "that produces plausible-looking numbers and correct-looking totals on small "
             "instances, which is the worst failure mode available here."),
            ("Reading the dynamic programme as a contradiction",
             "&ldquo;It has a polynomial algorithm, so it cannot be NP-hard&rdquo; is the "
             "commonest error about this problem. The algorithm is polynomial in a quantity that "
             "is not the input length. Say which quantity, every time, and the apparent paradox "
             "disappears."),
            ("Counting numbers instead of digits",
             "Eight numbers sounds small. Each is four digits here and would be `n + m` digits in "
             "general, and it is the digits that the input length counts and that the table's "
               "column count is exponential in. The panel labels this field &ldquo;numbers built, "
               "and their width&rdquo; for that reason."),
        ],
        "standard": (
            "Finish when you can build the digit table for a formula of your own and justify the base you chose.",
            "You should be able to lay out the columns, write both numbers for each variable and "
            "both slack numbers for each clause, state the target, add each column over every row "
            "to show no carry is possible, and say whether a numeric algorithm you quote is "
            "polynomial in the input length or in the magnitude of the numbers.",
        ),
        "note": (
            "Weak hardness is the hinge of this course: it is what makes an approximation scheme "
            "possible later, and &ldquo;Accuracy by the Epsilon&rdquo; uses exactly this table "
            "with the values scaled down until it fits."
        ),
    },

    # ---------------------------------------------------------------- 06
    {
        "slug": "circuits-tours-and-the-chain",
        "title": "Circuits, Tours and the Chain",
        "module": "Hardness that travels",
        "one_line": "Give every pair of cities distance 1 or 2, set the budget to the number of cities, and watch the tours within budget be the Hamilton circuits, listed identically.",
        "summary": (
            "The cleanest reduction in the kit: distance 1 where the graph has an edge, 2 where it "
            "does not, budget `n`. A tour costs `n` exactly when every step is an edge, so the "
            "tours within budget and the Hamilton circuits are literally the same list &mdash; "
            "the map on solutions is the identity on the vertex sequence. The lab enumerates both "
            "lists and compares them, and the page then says what the same trick does to "
            "approximability."
        ),
        "key": [
            "distance 1 on an edge, 2 off it, budget n",
            "a tour has n steps, so it costs at least n, and exactly n only if every step is an edge",
            "",
            "the five-cycle: 12 tours considered, 1 within budget, 1 Hamilton circuit, same list",
            "shortest tour 5, budget 5, and the two yes-or-no answers agree",
            "",
            "replace 2 by something huge and a constant-factor approximation would decide Hamilton",
        ],
        "key_label": "One distance matrix, two solution lists, and the identity between them",
        "concepts_intro": (
            "One idea about why this reduction is so tight, one about what a chain of reductions "
            "buys, and one about turning a reduction into a statement that no approximation is "
            "possible &mdash; which is the bridge to the second half of the course."
        ),
        "concepts": [
            ("The tightest kind of map: the identity",
             "Most reductions rename the objects. This one does not: a tour of the constructed "
             "instance is a cyclic order of the cities, a Hamilton circuit is a cyclic order of "
             "the vertices, and they are the same sequences. So the map on solutions is the "
             "identity, restricted to the tours that come in under budget. The lab still checks "
             "it, by enumerating both lists and comparing them as sets, because a construction "
             "whose correctness is obvious is exactly the kind that ships with an off-by-one in "
             "the budget."),
            ("A chain of reductions needs only its links",
             "Reductions compose: if `A ≤p B` and `B ≤p C` then `A ≤p C`, because the composition "
             "of two polynomial maps is polynomial. That is what makes a library of hardness "
               "results cheap &mdash; nobody reduces satisfiability to the travelling salesman "
               "directly. The route runs through several problems, and each link is a construction "
               "of the kind built on these pages."),
            ("The same gadget with a bigger number forbids approximation",
             "Put `1` on the edges and something enormous off them &mdash; `2n` rather than `2` "
             "&mdash; and a Hamilton circuit still costs `n` while any tour missing an edge costs "
             "more than `2n`. An algorithm promising to come within a factor 2 of the optimum "
             "would therefore have to return a tour of cost at most `2n` when a circuit exists, "
               "and could not when none does, so it would decide the Hamilton circuit problem. "
               "That is why the approximation half of this course restricts to distances obeying "
               "the triangle inequality: without some hypothesis there is nothing to prove."),
        ],
        "read_title": "The distance matrix, the two lists, and the argument that kills approximation",
        "read_intro": "The construction, why the budget is exactly `n`, what the lab enumerates, how reductions compose, and the variant that rules out a constant factor.",
        "body": [
            ("def", ("Hamilton circuit, and the travelling salesman",
                     "A <strong>Hamilton circuit</strong> is a cycle visiting every vertex of a "
                     "graph exactly once. The <strong>travelling salesman</strong> decision "
                     "problem takes a distance for every pair of cities and a budget, and asks "
                     "whether some tour visiting every city once and returning costs at most the "
                     "budget.")),
            ("h3", "The construction"),
            ("math", [
                "for every pair u, v:     D[u][v] = 1   if uv is an edge of G",
                "                         D[u][v] = 2   if it is not",
                "budget                   B = n, the number of vertices",
            ]),
            ("thm", ("The construction is a reduction",
                     "The graph has a Hamilton circuit if and only if the constructed instance "
                     "has a tour of cost at most `n`.")),
            ("proof", ("A tour visits `n` cities and returns, so it takes exactly `n` steps, and "
                       "every step costs 1 or 2. Its cost is therefore at least `n`, with "
                       "equality exactly when every step costs 1, that is, when every step is an "
                       "edge of `G` &mdash; which makes the tour a Hamilton circuit.",
                       "So if a Hamilton circuit exists it is a tour of cost exactly `n`, which "
                       "is within budget; and if a tour of cost at most `n` exists then its cost "
                       "is exactly `n`, every step is an edge, and it is a Hamilton circuit. The "
                       "two lists of solutions are therefore equal as sets of cyclic sequences, "
                       "which is stronger than the reduction needs.")),
            ("h3", "What the lab enumerated"),
            ("p", "The loaded graph is the five-cycle. The panel reports 5 vertices and 5 edges, "
                  "a budget of 5, 12 tours considered, 1 tour within budget, 1 Hamilton circuit, "
                  "the verdict that the two lists are the same list, a shortest tour of 5, and "
                  "the two answers agreeing. The single tour within budget is the cycle itself."),
            ("p", "Twelve is `(n − 1)!` divided by 2: a tour is counted once rather than twice "
                  "for itself and its reverse, and it is counted starting from city 1. Getting "
                  "that convention wrong is a real hazard here, because counting a cycle and its "
                  "reverse separately would make a bijection look like a two-to-one map, and the "
                  "panel's verdict on the map would then be wrong for a reason having nothing to "
                  "do with the construction."),
            ("example", ("Why the other eleven tours cost more",
                         "The five-cycle has 5 edges out of 10 pairs, so half the distances are "
                         "2. Any ordering other than the cycle itself must use at least one "
                         "non-edge, so it costs at least 6 &mdash; and the panel's table shows no tour of "
                         "6 at all. The lengths across the twelve are 5, 7, 8 and 10, because "
                         "dropping one edge of the cycle leaves a path whose ends are joined "
                         "only by that same edge: using one non-edge forces a second. The "
                         "budget separates the one from the eleven, and it is the only thing "
                         "doing the separating.")),
            ("h3", "Composing reductions, and where this one sits"),
            ("p", "Satisfiability is not reduced to the travelling salesman in one step by "
                  "anyone. The route runs through a sequence of problems, each link a "
                  "construction with its own gadget, and composition does the rest: two "
                  "polynomial maps compose to a polynomial map, and the yes-or-no equivalences "
                  "compose to a yes-or-no equivalence. This page builds the last link, and the "
                  "link from independent set to Hamilton circuit is stated here and built "
                  "nowhere in this library &mdash; its gadget needs more vertices than the lab "
                  "can enumerate over."),
            ("p", "That gap is worth being explicit about rather than papering over with an "
                  "arrow. What has been built in front of you on this course is: search from "
                  "decision, satisfiability to independent set, the identity carrying independent "
                  "set to vertex cover and clique, satisfiability to subset sum, and Hamilton "
                  "circuit to the travelling salesman. What is quoted and not built is "
                  "Cook&ndash;Levin &mdash; that satisfiability is NP-complete at all &mdash; and "
                  "the middle of the chain into Hamilton circuits."),
            ("thm", ("No constant-factor approximation for the general travelling salesman",
                     "If for some constant `ρ ≥ 1` there is a polynomial-time algorithm always "
                     "returning a tour of cost at most `ρ` times the optimum, then the Hamilton "
                     "circuit problem is solvable in polynomial time, and hence `P = NP`.")),
            ("proof", ("Build the distance matrix with 1 on the edges and `ρ · n + 1` off them, "
                       "which is still polynomial to write down. If `G` has a Hamilton circuit "
                       "the optimum is exactly `n`, so the algorithm must return a tour of cost "
                       "at most `ρ · n`. If `G` has none, every tour uses a non-edge and costs "
                       "more than `ρ · n`. So the returned cost decides whether a Hamilton "
                       "circuit exists, and the whole procedure is polynomial.")),
            ("p", "The lab uses 2 rather than `ρ · n + 1`, because 2 is what the decision "
                  "reduction needs and small numbers are what a five-city enumeration can show. "
                  "The inapproximability variant is the same gadget with the off-edge distance "
                  "raised, and this panel cannot do that &mdash; its distances are derived from the "
                  "graph rather than typed, so the variant is an argument here and a slider in "
                  "&ldquo;The Hypothesis Doing the Work&rdquo;. What "
                  "it means for the rest of the course is stark: approximation is not available "
                  "for this problem as stated, so the next approximation of a tour will come with "
                  "a hypothesis attached."),
        ],
        "lab": ("reduction", {"mode": "tsp", "preset": "cycle5"}),
        "steps_title": "Checking a reduction whose correctness looks obvious",
        "steps_intro": "The argument is three lines, so the risk moves entirely into the details around it.",
        "steps": [
            ("Count the steps in a tour before setting the budget",
             "A tour of `n` cities has `n` steps, not `n - 1`: it returns. The budget is `n` "
             "because the cheapest possible step costs 1. An off-by-one here makes the reduction "
             "either trivially true or trivially false, and the enumeration will still look "
             "healthy."),
            ("Fix a canonical form for a solution",
             "A cycle, its rotations and its reverse are one circuit. Decide that a tour starts "
             "at city 1 and that its second city is smaller than its last, and apply the same "
             "rule to both lists. The comparison of the two solution sets is meaningless unless "
             "both are canonicalised the same way."),
            ("Enumerate both sides and compare them as sets",
             "Not the counts &mdash; the sets. Two lists of the same length can differ, and this "
             "is the one reduction on the course where the comparison is available in full "
             "because the map is the identity."),
            ("Check a no instance too",
             "The panel's path and bowtie examples have no Hamilton circuit; the shortest tour "
             "comes to 5 against a budget of 4 in one and 6 against 5 in the other. A reduction "
             "verified only where the answer is yes has been verified on half of the "
             "equivalence."),
            ("Ask what the off-edge distance is doing before claiming anything about approximation",
             "With 2 off the edges the construction proves the decision problem hard. With "
             "`ρ · n + 1` it proves no `ρ`-approximation exists. Same gadget, different constant, "
             "completely different theorem &mdash; and the second is the one that explains the "
             "shape of everything after this page."),
        ],
        "worked": {
            "title": "Twelve tours on the five-cycle, and the one within budget",
            "intro": [
                "The graph is `1-2, 2-3, 3-4, 4-5, 5-1`, so the distance is 1 on those five "
                "pairs and 2 on the other five. Each tour is written starting at city 1, with its "
                "reverse counted once.",
            ],
            "lines": [
                "  tour            length     within budget 5?   a Hamilton circuit?",
                "",
                "  1-2-3-4-5          5              yes                yes",
                "  1-2-3-5-4          7              no                 no",
                "  1-2-4-3-5          7              no                 no",
                "  1-2-4-5-3          8              no                 no",
                "  1-2-5-3-4          8              no                 no",
                "  1-2-5-4-3          7              no                 no",
                "  1-3-2-4-5          7              no                 no",
                "  1-3-2-5-4          8              no                 no",
                "  1-3-4-2-5          8              no                 no",
                "  1-3-5-2-4         10              no                 no",
                "  1-4-2-3-5          8              no                 no",
                "  1-4-3-2-5          7              no                 no",
                "",
                "  tours considered 12       within budget 1       Hamilton circuits 1",
                "  the two lists are the same list          shortest tour 5 = the budget",
            ],
            "after": [
                "The last row is the worst tour and it is worth reading: `1-3-5-2-4` uses five "
                "non-edges and costs 10, which is twice the budget. In the five-city instance "
                "every step is either 1 or 2, so every tour costs between 5 and 10, and the whole "
                "question is whether any of them lands on the lower end.",
                "Switch to the five-cycle with a chord added and the tour list does not move: "
                "still 12 tours, still one within budget, still one circuit. The extra edge "
                "changes one distance from 2 to 1 and lowers several tour lengths &mdash; "
                "`1-2-5-4-3` drops from 7 to 6 &mdash; without creating a new Hamilton circuit. "
                "The answer is a property of the graph and not of the distances it happens to "
                "produce.",
                "For a faded rehearsal, load the bowtie &mdash; two triangles sharing a vertex "
                "&mdash; and predict the shortest tour before running it. The supplied first "
                "move: the shared vertex is a cut vertex, so any circuit would have to pass "
                "through it twice, which no tour may do. Say what that forces about the number of "
                "non-edges in every tour, and then check the shortest length against the budget.",
            ],
        },
        "quiz_title": "Budgets, compositions and constants",
        "quiz": [
            {"q": "Why is the budget exactly `n` rather than `n - 1` or `2n`?",
             "a": ["Because a tour has `n` steps and the cheapest step costs 1, so `n` is the least a tour can cost",
                   "Because the graph has `n` edges",
                   "Because the optimum is always `n`",
                   "Because `n` is half of `2n`, the worst possible tour"],
             "c": 0,
             "why": "The tour returns to its start, so it takes `n` steps for `n` cities. Every "
                    "step costs 1 or 2, so `n` is a floor, and hitting the floor means every step "
                    "is an edge. The graph's edge count is unrelated, and the optimum is `n` only "
                    "when a circuit exists."},
            {"q": "The lab reports 12 tours considered on five cities. Where does 12 come from?",
             "a": ["`5!` divided by 10",
                   "`(5 − 1)!` divided by 2, since rotations are fixed by starting at city 1 and a tour and its reverse are one circuit",
                   "The number of edges plus the number of non-edges plus two",
                   "`2^5` minus the empty and full sets minus 18"],
             "c": 1,
             "why": "Fixing the starting city removes the rotations and leaves `(n − 1)!` "
                    "orderings; identifying each with its reverse halves that, giving 12. The "
                    "convention matters: counting a cycle and its reverse separately would report "
                    "24 and would make the map on solutions look two-to-one."},
            {"q": "`A ≤p B` and `B ≤p C`. What justifies `A ≤p C`?",
             "a": ["Nothing: reductions do not compose",
                   "The composition of two polynomial maps is polynomial, and the two equivalences compose",
                   "Only if `B` is NP-complete",
                   "Only if all three are decision problems in `NP`"],
             "c": 1,
             "why": "Composition is what makes a library of hardness results worth having: "
                    "applying one polynomial map after another takes polynomial time, and `x` is "
                    "a yes instance of `A` exactly when its image is a yes instance of `B` "
                    "exactly when that image is a yes instance of `C`. Nothing about membership "
                    "of `NP` is needed for the composition itself."},
            {"q": "Why does the approximation argument need the off-edge distance to grow with `n`, rather than staying at 2?",
             "a": ["Because 2 makes the arithmetic harder",
                   "Because with 2 the worst tour costs only `2n`, so a factor-2 approximation is allowed to return it and learns nothing",
                   "Because the triangle inequality fails at 2",
                   "Because a tour of cost `2n` is not a tour"],
             "c": 1,
             "why": "With distances 1 and 2 every tour costs between `n` and `2n`, so returning "
                    "any tour at all already satisfies a factor of 2 and the approximation "
                    "algorithm need not distinguish anything. Raising the off-edge distance above "
                    "`ρ · n` is what forces the algorithm to find a circuit when one exists. "
                    "Incidentally the 1-and-2 instance does satisfy the triangle inequality, "
                    "which is why the metric case is still interesting."},
        ],
        "mistakes": [
            ("Counting a tour and its reverse as two solutions",
             "On an undirected instance they are one circuit. Counting both doubles one list "
             "without doubling the other and turns a verified identity into a spurious "
             "two-to-one map. Canonicalise before comparing, and apply the same rule to both "
             "sides."),
            ("Reading this reduction as a statement about approximation",
             "It says the decision problem is hard. The inapproximability result is a different "
             "construction with the same shape and a much larger constant, and it is proved on "
             "this page rather than implied by the lab. A page showing distances of 1 and 2 has "
             "shown an instance where a factor of 2 is free."),
            ("Treating the chain as though every link were built here",
             "Two links in the standard chain are quoted rather than constructed in this library: "
             "that satisfiability is NP-complete at all, and the route from independent set into "
             "Hamilton circuits. Knowing which of your beliefs rest on a construction you have "
             "seen is the point of building the others."),
        ],
        "standard": (
            "Finish when you can write the distance matrix, justify the budget, and state the two different theorems the same gadget gives.",
            "You should be able to construct the instance from a graph, prove both directions of "
            "the equivalence from the step count, canonicalise a tour so the two solution lists "
            "can be compared, explain why reductions compose, and derive the inapproximability "
            "statement by raising the off-edge distance.",
        ),
        "note": (
            "That is the last reduction on this course. From here the question changes from "
            "&ldquo;is this problem hard&rdquo; to &ldquo;what can honestly be done about "
            "it&rdquo;, and &ldquo;A Bound the Search Can See&rdquo; starts with the answer that "
            "gives up nothing: an exact algorithm that is still exponential and prunes anyway."
        ),
    },

    # ---------------------------------------------------------------- 07
    {
        "slug": "a-bound-the-search-can-see",
        "title": "A Bound the Search Can See",
        "module": "Exact answers, still exponential",
        "one_line": "Run the same knapsack search twice, with the fractional bound and without it, and read 14 nodes against 44 for one identical answer.",
        "summary": (
            "The first honest response to a hard problem is to solve it exactly and try to visit "
            "less of the search tree. The fractional relaxation from Greedy Algorithms and Matroids is an "
            "upper bound on anything a branch can still reach, so a branch whose bound is no "
            "better than the best answer so far can be cut. On the loaded instance that is 14 "
            "nodes against 44, with both searches returning 16 and an exhaustive check over 32 "
            "subsets agreeing."
        ),
        "key": [
            "at a node: value so far + fractional optimum of what remains  =  an upper bound",
            "bound ≤ best found so far   ⟹   cut the branch; it cannot hold anything better",
            "",
            "5 items, capacity 10:   value 16 = the optimum, from 32 subsets",
            "14 nodes with the bound, 44 without, 4 branches cut",
            "",
            "pruning changes the node count and never the answer",
        ],
        "key_label": "One search, two node counts, and one answer",
        "concepts_intro": (
            "The first idea is what makes a bound usable at all. The second is that pruning is "
            "not a heuristic, which the lab checks rather than asserts. The third is the reading "
            "of the three numbers in the panel, one of which is not measured in the same units as "
            "the other two."
        ),
        "concepts": [
            ("An upper bound on any completion licenses a cut",
             "At a node the search has decided some prefix of the items and has a remaining "
             "capacity. Allow the remaining items to be taken fractionally and greed solves that "
             "relaxation exactly &mdash; it is the algorithm Greedy Algorithms and Matroids proved correct. "
             "Since allowing fractions can only help, the value so far plus the fractional "
             "optimum of the rest is at least as large as anything the branch can actually reach. "
             "If that number is no better than an answer already in hand, nothing in the branch "
             "can be, and the branch is cut without being explored."),
            ("Pruning is not a heuristic",
             "This is the property to insist on, because the words sound like a trade. The "
             "bounded search and the unbounded search must return the same value, and both must "
             "agree with an exhaustive enumeration. The panel runs all three and prints the "
             "verdict: 16, 16, and 16 from 32 subsets. A bound that cut a branch containing the "
             "optimum would be a wrong algorithm rather than a fast one, and the check is what "
             "distinguishes the two."),
            ("Two of the three numbers are nodes and one is subsets",
             "The panel reports 14 nodes with the bound, 44 without, and 32 for the whole tree. "
             "The third is `2^n`, the number of subsets an exhaustive search examines &mdash; the "
             "leaves. The first two count nodes of a recursion, which includes every internal "
             "node on the way down. That is why the unbounded search can visit more nodes than "
             "there are subsets, and it is not a contradiction: 44 nodes produce fewer than 32 "
             "complete subsets between them, because most of them are partial."),
        ],
        "read_title": "The bound, the cut, and the three counts",
        "read_intro": "What the relaxation gives, why the cut is safe, what the lab measured on this instance, and what the same code does on two others.",
        "body": [
            ("def", ("Branch and bound",
                     "A search over partial solutions that, at each node, computes an "
                     "<strong>upper bound</strong> on the best value any completion of that "
                     "partial solution could have, and abandons the node when the bound does not "
                     "beat the best complete solution found so far. The bound must never "
                     "underestimate a completion, or the search may discard the optimum.")),
            ("thm", ("The fractional relaxation is a valid bound",
                     "Let a node have decided items `1` through `i - 1`, with value `v` taken and "
                     "capacity `c` remaining. Then every completion of that node has value at "
                     "most `v` plus the fractional knapsack optimum of items `i` through `n` with "
                     "capacity `c`.")),
            ("proof", ("Any completion chooses a subset of the remaining items fitting in `c`. "
                       "That subset is also a feasible fractional solution &mdash; take each "
                       "chosen item in full &mdash; so its value is at most the fractional "
                       "optimum of the same sub-instance. Adding `v` to both sides gives the "
                       "claim. The fractional optimum is computed exactly by taking items in "
                       "decreasing value per unit weight and splitting the one that does not "
                       "fit, which is the greedy rule proved correct in Greedy Algorithms and Matroids.")),
            ("h3", "What the lab measured"),
            ("p", "The instance is the five items `3:5, 4:6, 5:8, 2:3, 6:9` with a capacity of "
                  "10. The panel reports a value of 16, the same 16 from an exhaustive search "
                  "over 32 subsets, both searches correct, 14 nodes with the bound, 44 without, "
                  "32 for the whole tree, and 4 branches cut with the bound against 0 without. "
                  "The optimum takes items `3:5`, `5:8` and `2:3`, filling the sack exactly at "
                  "weight 10 for value 16."),
            ("p", "At the root the fractional bound is 16, which is exactly the integer optimum "
                  "on this instance. That is a coincidence of the numbers rather than a general "
                  "fact, and it is worth noticing because it is the best case for a bound: it "
                  "knows the answer before the search starts, and still has to prove it by "
                  "exploring until every alternative is cut."),
            ("example", ("The same code, a different instance",
                         "Switch to the example with one heavy prize and a lot of filler &mdash; "
                         "`9:30` and six copies of `1:2`, capacity 9 &mdash; and the counts become "
                         "3 nodes with the bound against 135 without. The single item fills the "
                         "sack, the fractional bound at the root is 30, taking it immediately "
                         "gives 30, and everything else is cut at once. Switch to the example "
                         "where every item has the same density and it is 30 against 86, with "
                         "only 2 branches cut, even though the root bound of 26 is again exactly "
                         "the optimum.")),
            ("p", "Those three instances are one algorithm and node counts of 14, 3 and 30. The "
                  "ratio between bounded and unbounded search moves from about 3 to 45 to under "
                  "3, and the number of branches cut moves from 4 to 2 to 2 without tracking "
                  "either. A tight bound at the root does not imply heavy pruning, because "
                  "pruning compares the bound against the best answer found <em>so far</em>, and "
                  "early in the search that is a poor answer."),
            ("h3", "What is therefore not established"),
            ("p", "Nothing about the worst case. Branch and bound on the knapsack is exponential "
                  "in the worst case and the bound is not a complexity improvement &mdash; there "
                  "are instances on which nothing is cut. What the node counts establish is what "
                  "the bound bought on the instance in front of you, which is a real and useful "
                  "fact about that instance and is the only kind of fact a counter can produce."),
            ("p", "This is the first of the strategies and the one that gives up least: the "
                  "answer is exact, the certificate is the search itself, and the cost is a "
                  "number you can watch. Every later strategy trades some of that away &mdash; "
                  "the guarantee of optimality, the range of instances, or the accuracy &mdash; "
                  "and each trade is worth making only against a measurement like this one."),
        ],
        "lab": ("coping", {"mode": "branchbound", "preset": "five"}),
        "steps_title": "Adding a bound to a search, and proving you have not broken it",
        "steps_intro": "The bound is the easy part. Establishing that it cannot cut the optimum is the work.",
        "steps": [
            ("Find a relaxation you can solve exactly",
             "Drop a constraint until what is left is easy, and make sure dropping it can only "
             "improve the objective. Fractional items instead of whole ones is the standard move "
             "for the knapsack, and the relaxed problem has a greedy algorithm that was proved "
             "correct before this course started."),
            ("Prove the bound never underestimates a completion",
             "Every completion must be a feasible solution of the relaxation, so that its value "
             "is at most the relaxed optimum. If some completion is not feasible in the relaxed "
             "problem, the bound is not a bound and the search will quietly discard optima."),
            ("Compare the bound against the best found so far, not against the final answer",
             "The search prunes with the information it has at the time. This matters when "
             "reading a trace: a node whose bound is below the final answer was not necessarily "
             "cut, because the running best may have been worse when the node was reached. The "
             "lab's trace says only what the two numbers on the row settle, and the count of "
             "branches actually cut is a separate counter."),
            ("Run the search with the bound switched off and require the same answer",
             "Two searches and an exhaustive enumeration, three answers, one number. This is the "
             "check that separates a correct pruning rule from a heuristic that happens to work "
             "on the instance loaded, and it costs one control on the panel."),
            ("Report the node counts as a measurement of this instance",
             "Say what the bound bought here. Do not convert it into a factor and do not attach "
               "it to the algorithm: the same code on the panel's other examples gives 3 nodes "
               "and 30 nodes, and neither is the algorithm's number."),
        ],
        "worked": {
            "title": "Twelve bounded nodes on five items, and the four cuts",
            "intro": [
                "Items `3:5, 4:6, 5:8, 2:3, 6:9`, capacity 10. Each row is a node where the "
                "bound was computed: the value decided so far, and the bound on any completion. "
                "The search ends with 16.",
            ],
            "lines": [
                "  node   depth   value so far   bound on any completion",
                "",
                "    1      0          0                16",
                "    2      1          5                16",
                "    3      2         11               79/5",
                "    4      3         11               31/2",
                "    5      4         14               31/2",
                "    6      4         11               31/2",
                "    7      2          5                16",
                "    8      3         13                16",
                "    9      4         16                16",
                "   10      4         13                16",
                "   11      3          5               31/2",
                "   12      1          0               31/2",
                "",
                "  best value 16      items 3:5 + 5:8 + 2:3      weight 10 of 10",
                "",
                "  nodes with the bound     14        branches cut    4",
                "  nodes without it         44        branches cut    0",
                "  the whole tree, 2 to the n          32 subsets",
                "  exhaustive optimum over those 32 subsets          16",
            ],
            "after": [
                "The node count is 14 and the table has 12 rows, and the difference is not an "
                "error. A node that has decided every item has nothing left to bound, so it is "
                "visited and counted without a bound being computed; there are two of those. "
                "Reading the table as the node count is the kind of small mismatch worth checking "
                "rather than assuming.",
                "The bound of `31/2` at nodes 4, 5, 6, 11 and 12 is the fractional optimum doing "
                "its work: 15.5 is above 14 but below 16, so once 16 is in hand every one of "
                "those branches is refused, and before 16 is in hand they are not. Node 9 is "
                "where 16 first appears, and every cut in this run happens after it.",
                "For a faded rehearsal, keep the items and raise the capacity to 14 before "
                "running it. The supplied first move: at capacity 14 the three heaviest items "
                "weigh 15, so the sack still cannot hold everything, and the fractional bound at "
                "the root will land between the best three-item value and the best four-item one. "
                "Predict whether the node count goes up or down, then check &mdash; and notice "
                "that whichever way it goes, it says nothing about capacity 15.",
            ],
        },
        "quiz_title": "What a bound may and may not do",
        "quiz": [
            {"q": "Why may the search cut a branch whose bound is 15.5 when the best answer so far is 16?",
             "a": ["Because 15.5 rounds to 16",
                   "Because no completion of that branch can exceed 15.5, and 16 is already in hand",
                   "Because the fractional solution is infeasible",
                   "Because the branch has no items left"],
             "c": 1,
             "why": "The bound is an upper bound on every completion, so the whole branch is "
                    "worth at most 15.5, which is worse than an answer already found. Nothing is "
                    "rounded anywhere &mdash; the bound is an exact fraction and the comparison "
                    "is exact. Feasibility of the fractional solution is what makes it a bound in "
                    "the first place."},
            {"q": "The panel reports 44 nodes without the bound and 32 for the whole tree. How can the first exceed the second?",
             "a": ["A counter is wrong",
                   "`2^n` counts complete subsets, the leaves; the node count includes every partial solution on the way down",
                   "The unbounded search revisits nodes",
                   "The whole tree is only the part the bound reached"],
             "c": 1,
             "why": "The two numbers are in different units, which is exactly the trap. `2^n` is "
                    "what an exhaustive enumeration of subsets examines; a recursion over items "
                    "also visits every prefix. Nothing is revisited and no counter is wrong, and "
                    "the useful comparison is the first two numbers against each other."},
            {"q": "On one panel instance the root bound equals the optimum and only 2 branches are cut; on another the root bound also equals the optimum and the search visits 3 nodes. What does that show?",
             "a": ["That the bound is unreliable",
                   "That how much pruning a bound buys depends on the instance, because branches are cut against the best answer found so far",
                   "That the root bound is irrelevant",
                   "That one of the two searches is wrong"],
             "c": 1,
             "why": "Both searches are correct and both bounds are valid. Pruning compares the "
                    "bound at a node against the running best, so an instance where a good answer "
                    "is found immediately prunes heavily and one where good answers arrive late "
                    "does not. The root bound is informative but it is not the quantity that "
                    "decides the node count."},
            {"q": "You measure 14 nodes against 44 on this instance. What have you established about branch and bound on the knapsack?",
             "a": ["That it is polynomial",
                   "That the bound gives a threefold saving",
                   "That on this instance the bound saved 30 node expansions; the worst case is untouched",
                   "That the whole tree is never explored"],
             "c": 2,
             "why": "A count on one input is not a bound. The same algorithm on the panel's other "
                    "instances gives 3 against 135 and 30 against 86, so no factor is the "
                    "algorithm's factor, and there are instances on which nothing is cut at all. "
                    "The measurement is about this instance and it is worth having for that."},
        ],
        "mistakes": [
            ("Trusting a bound that has not been proved to be one",
             "A quantity that usually exceeds the completions is not a bound. If any completion "
             "can beat it, the search will cut the branch holding the optimum and return a "
             "confident wrong answer with no symptom. The check on the panel &mdash; the same "
             "answer with the bound off, and again by exhaustive search &mdash; exists for this."),
            ("Reading a row of the trace as a branch that was pruned",
             "The trace records the bound at each node and not the best value known at that "
             "moment, and the search prunes against the running best. So a row whose bound is "
             "below the final answer may or may not have been cut. The number of branches "
             "actually cut is the algorithm's own counter and it is in the panel above the "
             "table."),
            ("Turning the node counts into a claim about the algorithm",
             "14 against 44 is this instance. The bound is not an asymptotic improvement and no "
             "arrangement of these three numbers becomes one. Say what the bound bought here, and "
             "if you need a claim about all instances, prove one."),
        ],
        "standard": (
            "Finish when you can add a bound to a search and demonstrate that it cannot cut the optimum.",
            "You should be able to choose a relaxation and say why relaxing can only improve the "
            "objective, prove the resulting quantity bounds every completion, explain why the "
            "comparison is against the running best rather than the final answer, and report node "
            "counts as measurements of the instance they were taken on.",
        ),
        "note": (
            "An exact search can also be made to depend on something other than the size of the "
            "input. &ldquo;Parameterising the Budget&rdquo; puts the exponential in a number the "
            "reader chooses, and prints `2^k · n` beside `2^n` with both computed."
        ),
    },
]
