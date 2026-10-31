"""Strings, Geometry and Hardness, lessons 5-8 -- Chapters 34 and 35.

Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, 3rd ed. (MIT
Press, 2009): Chapter 34, NP-Completeness (pp. 1048-1105), and Chapter 35,
Approximation Algorithms (pp. 1106-1139). Every quotation is copied from the
operator's copy with its printed page in the comment beside the lesson. The
formulas, graphs, set families and number lists are written for these
lessons; none of the book's figures, tables, pseudocode or exercises is
reproduced. Every figure the prose attributes to the lab was read off the
running kit with the instance typed in.
"""

LESSONS = [
    # ---------------------------------------------------------------- 05
    # CLRS 34 intro, 34.1-34.2, pp. 1048-1067. Quote: p. 1049, 31 words,
    # quotes.py OK. Lesson total: 31 words. Lab: reduction/selfreduce, kit
    # presets; the lesson's formula -1 2 3; 1 -2; -2 -3; -1 -3 (4 calls,
    # x1=T x2=T x3=F, 3 of 8 models) and the exercise's 1 2; -1 3; -2 -3;
    # -1 -2 (x1=T x2=F x3=T, 2 of 8), read off the kit.
    {
        "slug": "polynomial-time-and-verification",
        "title": "Polynomial Time and Verification",
        "module": "Chapter 34 · NP-Completeness",
        "one_line": "P is the class of problems a polynomial-time algorithm decides; NP is the class whose yes-instances have a short certificate that a polynomial-time algorithm can check.",
        "summary": (
            "The opening of Chapter 34 and sections 34.1 and 34.2: decision and optimization "
            "problems, why the encoding of an input matters, the class P in the formal-language "
            "framework, verification algorithms and certificates, the class NP, and co-NP. Check "
            "a certificate for a formula written for the lesson clause by clause, and count the "
            "decision questions it takes to build one."
        ),
        "key": [
            "decision problem: answer yes or no",
            "P: decided in O(n^k) time",
            "input size: the length of the encoding",
            "verifier A(x, y): y is the certificate",
            "NP: a short certificate, checked fast",
            "P ⊆ NP; whether P = NP is open",
        ],
        "key_label": "Sections 34.1 and 34.2 in six lines",
        "concepts_intro": (
            "Three definitions from these sections are used in every later one. Each turns an "
            "informal word, easy, size or check, into something exact."
        ),
        "concepts": [
            ("A decision problem",
             "A problem whose answer is yes or no. An optimization problem becomes one by "
             "adding a bound: not the shortest path, but whether there is a path of at most k "
             "edges. If the optimization problem is easy, so is the decision problem, which is "
             "why hardness is studied on decision problems."),
            ("An encoding and its length",
             "An instance is given to an algorithm as a binary string, and running time is "
             "measured against that string's length. The authors assume a concise encoding: "
             "integers in binary, or any base polynomially related to it, never in unary."),
            ("A verification algorithm",
             "A two-argument algorithm A(x, y) that takes an input x and a certificate y. A "
             "language is in NP when some polynomial-time A accepts exactly its members, each "
             "with some certificate of length polynomial in |x|, and no certificate makes A "
             "accept a non-member."),
        ],
        "read_title": "The chapter's argument first, then the check",
        "read_intro": (
            "Read the opening of Chapter 34 and sections 34.1 and 34.2 in your own copy first. "
            "The lesson sets out the argument in its own words and then checks a certificate "
            "for a formula written for it."
        ),
        "body": [
            ("p", "&ldquo;If we were somehow given a “certificate” of a solution, then we could "
                  "verify that the certificate is correct in time polynomial in the size of the "
                  "input to the problem.&rdquo; That is how the opening of Chapter 34 first "
                  "describes NP, informally, before sections 34.1 and 34.2 make each word in it "
                  "exact. This lesson reads those pages and then plays both parts on a small "
                  "formula of its own: the verifier, who checks a certificate, and the "
                  "searcher, who has to find one."),
            ("p", "The chapter opens with pairs of problems that look alike and are not: shortest "
                  "and longest simple paths, Euler tours and hamiltonian cycles, 2-CNF and "
                  "3-CNF satisfiability. In each pair the first has a polynomial-time algorithm "
                  "and the second is NP-complete. It then names the three classes the chapter studies, P, "
                  "NP and NPC, and the three ideas its proofs need: decision problems in place of "
                  "optimization problems, reductions, and a first NP-complete problem to reduce "
                  "from. The authors are plain about the stakes: no one has found a "
                  "polynomial-time algorithm for an NP-complete problem, and no one has proved "
                  "that none exists."),
            ("p", "Section 34.1 builds the definition of polynomial time with care. An abstract "
                  "problem is a relation between instances and solutions; a decision problem has "
                  "solutions yes and no. An algorithm sees an instance only through an encoding "
                  "as a binary string, and the encoding matters. If an algorithm runs in time "
                  "proportional to an integer k, it is linear in the input's length when k is "
                  "written in unary and exponential when k is written in binary, since a binary k "
                  "takes only about lg k bits. So the authors rule out unary and assume any "
                  "reasonable concise encoding; encodings polynomially related to one another "
                  "agree on which problems are polynomial-time solvable (Lemma 34.1)."),
            ("p", "With encodings fixed, a decision problem is a language: the set of binary "
                  "strings whose answer is yes. An algorithm accepts a string if it outputs 1, "
                  "and decides a language if it accepts every member and rejects every other "
                  "string. P is the class of languages decided, equivalently (Theorem 34.2) "
                  "accepted, in polynomial time. The section also defends polynomial time as the "
                  "line between tractable and intractable: polynomials compose, are closed under "
                  "addition and multiplication, and coincide across the usual models of "
                  "computation."),
            ("p", "Section 34.2 starts from the hamiltonian-cycle problem. Deciding it by trying "
                  "every ordering of the vertices takes time exponential in the square root of "
                  "the input's length. But if someone hands you an ordering and claims it is a "
                  "hamiltonian cycle, checking takes polynomial time: is it a permutation of the "
                  "vertices, and is every consecutive pair, including the last and the first, an "
                  "edge? That check is a verification algorithm, and the ordering is its "
                  "certificate. NP is the class of languages with a polynomial-time verifier and "
                  "certificates of polynomial length."),
            ("p", "Every language in P is in NP, because a decider can ignore the certificate. "
                  "Whether the inclusion is strict is the open question, and the section adds two "
                  "more: whether NP is closed under complement, that is whether NP equals co-NP, "
                  "and whether P equals the intersection of NP and co-NP. The section's diagram "
                  "draws the four ways the classes might relate, and the authors say which one "
                  "most researchers expect without claiming that it has been shown."),
            ("p", "Now the lab, which works on formulas in conjunctive normal form, written as "
                  "clauses separated by semicolons, with `-2` for not x2. It plays a game the "
                  "chapter leaves to Exercise 34.4-6: given only a yes-or-no oracle for "
                  "satisfiability, build a satisfying assignment. Ask whether the formula is "
                  "satisfiable; then fix x1 true and ask again, keeping true if the answer is yes "
                  "and false otherwise; and so on for each variable. That is at most n + 1 "
                  "questions where trying assignments could take 2^n. The lab then checks the "
                  "assignment clause by clause, which is the verifier's job, and re-asks every "
                  "step of brute force."),
            ("p", "Its presets: <code>three</code> has 3 variables and 4 clauses; the oracle is "
                  "asked 4 times, a search would try 8 assignments, and the result x1=T x2=T "
                  "x3=F is one of the formula's 4 models. <code>forced</code> has exactly 1 model "
                  "of 8, found in 4 questions. <code>four</code> takes 5 questions against 16 "
                  "assignments and has 7 models. <code>free</code> has a variable the formula "
                  "allows either way; the oracle says yes to x1 true, so the lab keeps it, and "
                  "finds x1=T x2=T in 3 questions. <code>unsat</code> is unsatisfiable: the first "
                  "answer is no, after 1 question, and there is no certificate to check."),
            ("p", "Then type the lesson's formula: `-1 2 3; 1 -2; -2 -3; -1 -3`, that is "
                  "(¬x1 ∨ x2 ∨ x3) ∧ (x1 ∨ ¬x2) ∧ (¬x2 ∨ ¬x3) ∧ (¬x1 ∨ ¬x3). The lab asks 4 "
                  "questions, builds x1=T x2=T x3=F, checks it against every clause, and reports "
                  "that the formula has 3 models among its 8 assignments. The 4 questions are "
                  "a count for this formula; that n + 1 suffice for every formula is the "
                  "argument above, and that each question could itself take exponential time is "
                  "why none of this shows satisfiability is easy."),
            ("h3", "Exercise"),
            ("code", [
                "1 2; -1 3; -2 -3; -1 -2",
            ]),
            ("p", "Run the self-reduction by hand: for each question say which formula is asked "
                  "about and what the answer is, and give the assignment it builds. Then check "
                  "that assignment as a verifier would, clause by clause, and count the formula's "
                  "models. Type the formula into the lab to compare."),
            ("p", "A certificate shows a problem is in NP; it says nothing yet about how hard it "
                  "is. The next lesson, NP-Completeness and Reducibility, adds the reductions "
                  "that do."),
        ],
        "lab": ("reduction", {
            "mode": "selfreduce",
            "preset": "three",
            "panel_title": "Build a certificate from yes-or-no answers, then check it",
            "panel_intro": "Type clauses separated by semicolons, with a minus sign for "
                           "negation. The lab asks a decision oracle at most n + 1 questions, "
                           "builds an assignment one variable at a time, checks it clause by "
                           "clause, and compares every answer with brute force. Type the "
                           "lesson's formula, then the exercise's.",
        }),
        "steps_title": "Verifying and finding a certificate",
        "steps_intro": "Four steps settle one formula; the fifth is a formula of your own.",
        "steps": [
            ("Say what the certificate is",
             "For satisfiability it is an assignment of true or false to each variable: n bits "
             "for n variables, polynomial in the formula's length."),
            ("Verify it clause by clause",
             "A clause is satisfied when at least one of its literals is true. The certificate "
             "is good exactly when every clause is satisfied, and checking takes one pass over "
             "the formula."),
            ("Search with the oracle",
             "Ask whether the formula is satisfiable. If yes, fix x1 true and ask again; keep "
             "true on yes, false on no. Repeat for each variable, at most n + 1 questions."),
            ("Count what each side cost",
             "Write the n + 1 questions beside the 2^n assignments a blind search could try, "
             "and remember that the oracle is the part no polynomial-time algorithm is known "
             "to supply."),
            ("Write a formula with one model",
             "Write a formula of your own on four variables that has exactly one satisfying "
             "assignment, type it into the lab, and check that the models tile reads 1 of 16 "
             "and that the lab still needs only 5 questions."),
        ],
        "worked": {
            "title": "Four questions and one certificate",
            "intro": [
                "The lesson's formula: (¬x1 ∨ x2 ∨ x3), (x1 ∨ ¬x2), (¬x2 ∨ ¬x3), (¬x1 ∨ ¬x3).",
            ],
            "lines": [
                "ask 1: satisfiable?  yes",
                "ask 2: with x1 true?  (x2 ∨ x3)(¬x2 ∨ ¬x3)(¬x3)",
                "       yes, by x2 true, x3 false;  keep x1 true",
                "ask 3: and x2 true?  (¬x3)(¬x3): yes;  keep",
                "ask 4: and x3 true?  ¬x3 fails: no;  x3 false",
                "certificate: x1 true, x2 true, x3 false",
                "check: x2, x1, ¬x3, ¬x3 satisfy the four clauses",
            ],
            "after": [
                "Four questions built the certificate and one pass over the clauses verified it. "
                "The formula's other two models set x1 and x2 false, with x3 either way; three "
                "of eight, as the lab counts. The verifier's pass is polynomial on "
                "every formula. The questions are polynomial in number, but each asks an oracle "
                "for which no polynomial-time algorithm is known, so the search is fast only "
                "relative to that oracle.",
            ],
        },
        "quiz_title": "Encodings, certificates and the classes",
        "quiz": [
            {"q": "Running the self-reduction on the exercise's formula (x1 ∨ x2), (¬x1 ∨ x3), "
                  "(¬x2 ∨ ¬x3), (¬x1 ∨ ¬x2), which assignment does it build, and how many models "
                  "does the formula have?",
             "a": ["x1 true, x2 true, x3 false; 2 models",
                   "x1 true, x2 false, x3 true; 2 models",
                   "x1 false, x2 true, x3 false; 1 model",
                   "x1 true, x2 false, x3 true; 3 models"],
             "c": 1,
             "why": "The formula is satisfiable, and with x1 true it still is (x2 false, x3 "
                    "true), so x1 stays true. With x2 also true the last clause fails, so x2 is "
                    "false; with x3 true everything holds. The other model is x1 false, x2 true, "
                    "x3 false, so there are 2 of 8. x1 true and x2 true violates (¬x1 ∨ ¬x2). "
                    "x1 false, x2 true, x3 false does satisfy the formula, but the procedure tries "
                    "true first and so builds the other model."},
            {"q": "An algorithm takes an integer k and runs in Θ(k) time. Under the book's "
                  "conventions, is it a polynomial-time algorithm?",
             "a": ["Yes, because its running time is linear",
                   "No: with k in binary the input has about lg k bits, so Θ(k) is exponential "
                   "in the input's length",
                   "Yes, if k is written in unary, which the book allows when it is convenient",
                   "It depends on the machine model"],
             "c": 1,
             "why": "Running time is measured against the length of the encoding, and section "
                    "34.1 assumes a concise one, with integers in binary. An n-bit k can be as "
                    "large as 2^n, so Θ(k) is exponential in n. Unary would make it linear, which "
                    "is exactly why the book excludes unary encodings. The usual machine models "
                    "agree on polynomial time, so the model does not change the answer."},
            {"q": "Which statement does section 34.2 establish?",
             "a": ["P = NP",
                   "P ⊆ NP, because a decider can be used as a verifier that ignores its "
                   "certificate",
                   "NP = co-NP, because a certificate for yes gives one for no",
                   "HAM-CYCLE is not in P"],
             "c": 1,
             "why": "The inclusion is proved in one line. Whether it is strict, whether NP equals "
                    "co-NP, and whether HAM-CYCLE has a polynomial-time algorithm are all open; "
                    "the section draws the possible relations among the classes without choosing "
                    "one. A certificate that a graph is hamiltonian says nothing about how to "
                    "certify that another graph is not."},
        ],
        "mistakes": [
            ("Reading NP as not polynomial",
             "NP stands for nondeterministic polynomial time, and the book defines it by "
             "verification: a short certificate, checked in polynomial time. Every problem in P "
             "is in NP. Sorting is in NP; so is finding a shortest path. The formula in this "
             "lesson is checked in one pass over four clauses; what is not known is how to find "
             "a certificate that fast on every formula."),
            ("Measuring time against the value instead of the length",
             "An algorithm that loops k times on an input k looks linear. Against the length of "
             "k written in binary it is exponential. Section 34.1's insistence on encodings is "
             "what makes the definition of P mean something, and it returns in the next lesson, "
             "where subset sum's numbers are large exactly so that this matters."),
            ("Taking the self-reduction for a fast algorithm",
             "The lab builds a certificate in n + 1 questions, but each question is a call to an "
             "oracle that decides satisfiability, and no polynomial-time algorithm for that is "
             "known. The reduction shows that finding a certificate is no harder than deciding "
             "whether one exists; it does not make either one easy."),
        ],
        "standard": ("Finish when you can say exactly what puts a problem in NP.",
                     "For a decision problem such as satisfiability or hamiltonian cycle, name "
                     "the certificate, describe the polynomial-time check, explain why the "
                     "encoding of numbers matters, and say which of the relations among P, NP "
                     "and co-NP are proved and which are open."),
        "note": ("The lab's oracle is brute force over every assignment, so it is exponential, "
                 "and it caps the formula's size to stay usable; the n + 1 count is about "
                 "questions asked, not time spent. No count on small formulas bears on whether "
                 "P equals NP, which is a question about every input size at once."),
    },
    # ---------------------------------------------------------------- 06
    # CLRS 34.3-34.5, pp. 1067-1105. Quote: p. 1050, 34 words, quotes.py OK.
    # Lesson total: 34 words. Lab: reduction/subsetsum (the book's own
    # 3-CNF-SAT to SUBSET-SUM construction, base 10), kit presets; the
    # lesson's formula 1 -2 3; -1 2 -3 and the exercise's 1 2 3; -1 -2 -3
    # (each: 10 numbers, target 11144, 6 subsets, 6 of 8 models), read off
    # the kit.
    {
        "slug": "np-completeness-and-reductions",
        "title": "NP-Completeness and Reducibility",
        "module": "Chapter 34 · NP-Completeness",
        "one_line": "A polynomial-time reduction carries every instance of one problem to an instance of another with the same answer; one NP-complete problem and a chain of reductions give the rest.",
        "summary": (
            "Sections 34.3 to 34.5: polynomial-time reducibility, NP-hard and NP-complete, "
            "circuit satisfiability as the first NP-complete problem, the five-step method for "
            "the others, and the chain through SAT, 3-CNF-SAT, CLIQUE, VERTEX-COVER, HAM-CYCLE, "
            "TSP and SUBSET-SUM. Build the subset-sum instance for a formula written for the "
            "lesson, digit by digit, and check that its solutions and the formula's match."
        ),
        "key": [
            "L1 ≤P L2: x ∈ L1 iff f(x) ∈ L2",
            "f computable in polynomial time",
            "NP-hard: every NP language reduces to it",
            "NP-complete: NP-hard and in NP",
            "one NPC problem in P would give P = NP",
            "subset sum: n + k digits, base 10",
            "target digits: 1 per variable, 4 per clause",
        ],
        "key_label": "Sections 34.3 to 34.5 in seven lines",
        "concepts_intro": (
            "Three definitions make up section 34.3, and the rest of the chapter is their "
            "application."
        ),
        "concepts": [
            ("Polynomial-time reducibility",
             "L1 reduces to L2, written L1 ≤P L2, when a function f computable in polynomial "
             "time maps every string x to a string f(x) with x in L1 exactly when f(x) is in "
             "L2. A polynomial-time decider for L2 then gives one for L1 (Lemma 34.3)."),
            ("NP-hard and NP-complete",
             "A language is NP-hard when every language in NP reduces to it, and NP-complete "
             "when it is also in NP. If any NP-complete language is in P, then P = NP "
             "(Theorem 34.4)."),
            ("A gadget",
             "A small piece of the constructed instance that stands for one piece of the "
             "original. In the subset-sum reduction each variable gets two numbers, one per "
             "truth value, and each clause gets a column of digits and two slack numbers that "
             "can top the column up to its target."),
        ],
        "read_title": "The chapter's argument first, then the construction",
        "read_intro": (
            "Read sections 34.3, 34.4 and 34.5 in your own copy first, and section 34.5.5 most "
            "closely. The lesson sets out the argument in its own words and then builds the "
            "subset-sum instance for a formula written for it."
        ),
        "body": [
            ("p", "&ldquo;When we demonstrate that a problem is NP-complete, we are making a "
                  "statement about how hard it is (or at least how hard we think it is), rather "
                  "than about how easy it is.&rdquo; Most of the book proves that algorithms are "
                  "fast. Sections 34.3 to 34.5 prove that problems are probably not, and the "
                  "proofs are constructions: each one builds, in polynomial time, an instance of "
                  "one problem from an instance of another. This lesson reads those sections and "
                  "builds one construction in full."),
            ("p", "Section 34.3 defines the tool. A reduction from L1 to L2 is a function f, "
                  "computable in polynomial time, such that x is in L1 if and only if f(x) is in "
                  "L2. Composing f with a polynomial-time decider for L2 decides L1 in polynomial "
                  "time (Lemma 34.3), so L1 is no harder than L2, up to a polynomial. NP-hard and "
                  "NP-complete follow, and Theorem 34.4 draws the consequence: a polynomial-time "
                  "algorithm for any one NP-complete problem would give one for every problem in "
                  "NP, and if any problem in NP has none, no NP-complete problem has one."),
            ("p", "The section then needs a first NP-complete problem, and takes circuit "
                  "satisfiability: given a boolean combinational circuit, is there an input that "
                  "makes the output 1? It is in NP because a circuit can be checked on a given "
                  "input in polynomial time (Lemma 34.5). It is NP-hard (Lemma 34.6) because the "
                  "whole computation of any polynomial-time verifier, a sequence of machine "
                  "configurations, can be wired as one circuit whose only free inputs are the "
                  "certificate's bits; the circuit is satisfiable exactly when some certificate "
                  "makes the verifier accept. That is the only proof in the chapter that reduces "
                  "every problem in NP directly."),
            ("p", "Section 34.4 turns Lemma 34.8 into a five-step method, so that no later proof "
                  "has to do that again: prove the language is in NP; choose a known NP-complete "
                  "language; describe a function from its instances to the new language's; prove "
                  "that the function preserves the answer in both directions; prove it runs in "
                  "polynomial time. The section applies it to formula satisfiability, introducing "
                  "a variable for each wire of the circuit so that the formula does not blow up "
                  "(Theorem 34.9), and then to 3-CNF-SAT, by rewriting each small piece of the "
                  "formula into clauses of exactly three literals (Theorem 34.10)."),
            ("p", "Section 34.5 extends the chain. CLIQUE is reached from 3-CNF-SAT with three "
                  "vertices per clause and edges between consistent literals in different clauses "
                  "(Theorem 34.11); VERTEX-COVER from CLIQUE by taking the complement graph "
                  "(Theorem 34.12); HAM-CYCLE from VERTEX-COVER with a widget of vertices for "
                  "each edge (Theorem 34.13); TSP from HAM-CYCLE with costs 0 and 1 "
                  "(Theorem 34.14); and SUBSET-SUM from 3-CNF-SAT (Theorem 34.15). The Algorithms "
                  "lesson Numbers as Gadgets, and Weak Hardness builds the last of these with "
                  "the same lab as this lesson."),
            ("p", "The subset-sum construction deserves reading slowly, because the lab follows "
                  "it exactly. For a formula with n variables and k clauses, every number has "
                  "n + k decimal digits, one column per variable and one per clause. Each "
                  "variable has two numbers, one for true and one for false, each with a 1 in its "
                  "own variable's column and a 1 in the column of every clause its literal "
                  "satisfies. Each clause has two slack numbers, with 1 and 2 in its column. The "
                  "target has 1 in every variable column and 4 in every clause column. A subset "
                  "hitting the target must take exactly one number per variable, an assignment, "
                  "and each clause column then holds the number of true literals in that clause, "
                  "which the slack can raise to 4 only if it is at least 1. No column can exceed "
                  "6, so base 10 never carries and the columns stay independent."),
            ("p", "Now the lab. Type a formula and it builds the numbers, prints them as a "
                  "digit table with the target, finds every subset that hits the target and "
                  "every satisfying assignment, checks that the map from subsets to assignments "
                  "is sound, onto and one to one, prints the largest column total against the "
                  "base, and solves the instance a second time by dynamic programming over the "
                  "sums. That second solution runs in time proportional to the target's value, "
                  "which is exponential in the formula's length; section 34.5.5 is careful that "
                  "the numbers are encoded in binary, and the previous lesson said why that "
                  "matters."),
            ("p", "Its presets: <code>three</code> has 3 variables and 2 clauses of three "
                  "literals, giving 10 numbers of 5 digits, target 11144, 6 subsets and 6 of 8 "
                  "assignments, with a largest column of 6 against the base 10. "
                  "<code>two</code> and <code>single</code> use clauses of two literals, which "
                  "the lab allows and the book's 3-CNF does not: target 1144 with 2 subsets, and "
                  "target 114 with 3. <code>forced</code> has 1 subset and 1 model, and the map "
                  "is a bijection. <code>unsat</code> is unsatisfiable: 0 subsets, 0 models, and "
                  "the dynamic programme cannot reach the target either."),
            ("p", "Then type the lesson's formula: `1 -2 3; -1 2 -3`, that is "
                  "(x1 ∨ ¬x2 ∨ x3) ∧ (¬x1 ∨ x2 ∨ ¬x3). The lab builds 10 numbers of 5 digits, "
                  "among them 10010 for x1 true and 1001 for x2 true, with target 11144. It finds "
                  "6 subsets that hit the target and 6 satisfying assignments, matched one for "
                  "one, and the largest column total is 6. The two assignments that fail are the "
                  "two that make one clause entirely false, and for each of them some clause "
                  "column would need 4 from slack that can supply only 3."),
            ("h3", "Exercise"),
            ("code", [
                "1 2 3; -1 -2 -3",
            ]),
            ("p", "Build the subset-sum instance for this formula by hand: write the ten numbers "
                  "as five-digit strings and the target. Then take the assignment x1 true, x2 "
                  "false, x3 false, choose its three variable numbers and the slack each clause "
                  "needs, and add them. Finally, say how many subsets hit the target and why. "
                  "Check the table in the lab."),
            ("p", "A proof of NP-completeness is a reason to stop looking for an exact fast "
                  "algorithm, and Chapter 35 says what to look for instead. The next lesson is "
                  "Approximating Vertex Cover and TSP."),
        ],
        "lab": ("reduction", {
            "mode": "subsetsum",
            "preset": "three",
            "panel_title": "Build the digit table for a formula, and match the solutions",
            "panel_intro": "Type clauses separated by semicolons, with a minus sign for "
                           "negation. The lab writes one number per literal and two slack "
                           "numbers per clause, in base 10, with the target below, and then "
                           "checks every subset against every assignment. Type the lesson's "
                           "formula, then the exercise's.",
        }),
        "steps_title": "Building the subset-sum instance",
        "steps_intro": "Four steps follow the construction in section 34.5.5; the fifth is a formula of your own.",
        "steps": [
            ("Lay out the columns",
             "One digit column per variable, most significant first, then one per clause. With "
             "n variables and k clauses every number has n + k digits."),
            ("Write the literal numbers",
             "For each variable, the true number has a 1 in its own column and a 1 under every "
             "clause containing the variable; the false number has a 1 in its own column and a "
             "1 under every clause containing its negation."),
            ("Write the slack and the target",
             "Each clause has two slack numbers, 1 and 2 in its own column. The target is 1 in "
             "every variable column and 4 in every clause column."),
            ("Map an assignment to a subset",
             "Take the number for each variable's value; each clause column now holds its "
             "count of true literals, 1, 2 or 3. Add slack 1 and 2, slack 2, or slack 1 to "
             "make 4."),
            ("Break the construction on purpose",
             "Write a three-clause formula of your own and type it into the lab. Then imagine "
             "the same numbers written in base 2 instead of base 10: find a column whose total "
             "would carry, and say which subset could then hit the target without being an "
             "assignment."),
        ],
        "worked": {
            "title": "The assignment x1 true, x2 true, x3 false, as numbers",
            "intro": [
                "The lesson's formula, C1 = (x1 ∨ ¬x2 ∨ x3) and C2 = (¬x1 ∨ x2 ∨ ¬x3). Digits "
                "are x1 x2 x3 C1 C2.",
            ],
            "lines": [
                "x1 true    1 0 0 1 0    10010",
                "x2 true    0 1 0 0 1     1001",
                "x3 false   0 0 1 0 1      101",
                "so far     1 1 1 1 2    11112",
                "C1 has 1 true literal: slack 10 + 20",
                "C2 has 2 true literals: slack 2",
                "11112 + 30 + 2 = 11144, the target",
            ],
            "after": [
                "The variable columns each received exactly one 1, so the subset is an "
                "assignment, and the clause columns received the counts of true literals, which "
                "the slack topped up to 4 in exactly one way. That is the forward direction of "
                "the proof. The backward direction is the same reading in reverse: any subset "
                "that hits 11144 has one number per variable, and each clause column could reach "
                "4 only if the chosen numbers put at least 1 into it.",
            ],
        },
        "quiz_title": "Reductions and the subset-sum gadget",
        "quiz": [
            {"q": "For the exercise's formula (x1 ∨ x2 ∨ x3) ∧ (¬x1 ∨ ¬x2 ∨ ¬x3), which numbers "
                  "make up the subset for x1 true, x2 false, x3 false, and how many subsets hit "
                  "the target?",
             "a": ["10010, 1001, 101, 10, 20 and 2; 6 subsets",
                   "10010, 1010, 110, 10 and 2; 6 subsets",
                   "10010, 1001, 101, 10, 20 and 2; 8 subsets",
                   "10010, 1001, 101 and 30; 6 subsets"],
             "c": 0,
             "why": "x1 true is 10010 (it satisfies C1); x2 false is 1001 and x3 false is 101 "
                    "(each satisfies C2). C1 then holds 1 and needs slack 10 and 20; C2 holds 2 "
                    "and needs slack 2. The total is 11144. Six of the eight assignments satisfy "
                    "both clauses, all false and all true being the exceptions, and the map is "
                    "one to one, so 6 subsets. 1010 and 110 are the true numbers for x2 and x3. "
                    "There is no number 30: the slack comes as 10 and 20."},
            {"q": "To show a new language L is NP-complete by the method of section 34.4, which "
                  "direction must the reduction go?",
             "a": ["From L to a known NP-complete language",
                   "From a known NP-complete language to L, together with a proof that L is "
                   "in NP",
                   "Either direction, as long as it runs in polynomial time",
                   "From L to a language in P"],
             "c": 1,
             "why": "Reducing a known NP-complete L′ to L shows L is at least as hard as L′, and "
                    "so as hard as everything in NP; membership in NP then makes it complete "
                    "(Lemma 34.8). Reducing L to an NP-complete problem shows only that L is no "
                    "harder than it, which every language in NP satisfies. A reduction to a "
                    "language in P would put L in P."},
            {"q": "Why does the subset-sum construction write its numbers in base 10?",
             "a": ["Because the book's examples are easier to read in decimal",
                   "Because no column can total more than 6, so no column carries and each "
                   "column is an independent constraint",
                   "Because base 10 keeps the numbers polynomially small in value",
                   "Because the target must be a multiple of 10"],
             "c": 1,
             "why": "A column holds at most two variable numbers' 1s or, in a clause column, at "
                    "most three literal 1s plus slack 1 and 2, total 6; any base above 6 would "
                    "do, and 10 is the convenient one. In base 2 the columns could carry and "
                    "unrelated subsets could reach the target. The values are exponential in the "
                    "number of digits in any base, which is what makes the dynamic programme "
                    "slow."},
            {"q": "Theorem 34.4 says that if any NP-complete problem is solvable in polynomial "
                  "time, then P = NP. What does it say if some problem in NP is not?",
             "a": ["Nothing; the theorem only goes one way",
                   "Then no NP-complete problem is solvable in polynomial time",
                   "Then every NP-complete problem is outside NP",
                   "Then P and NP are both empty"],
             "c": 1,
             "why": "The theorem states both forms, and they are contrapositives of each other: "
                    "if some NP-complete problem were in P, every problem in NP would be, "
                    "contradicting the assumption. NP-complete problems are in NP by definition, "
                    "and P is not empty, since every problem the earlier chapters solve is in "
                    "it."},
        ],
        "mistakes": [
            ("Reducing in the wrong direction",
             "To show a problem is hard, reduce a known hard problem to it. Reducing the new "
             "problem to SAT shows only that it is in NP or easier. The subset-sum proof goes "
             "from 3-CNF-SAT to SUBSET-SUM: a formula becomes numbers, so a fast subset-sum "
             "solver would decide formulas."),
            ("Checking only one direction of the answer",
             "A reduction must send yes-instances to yes-instances and no-instances to "
             "no-instances. On the lesson's formula the lab checks both: every subset that "
             "hits 11144 carries back to an assignment that satisfies both clauses, and every "
             "satisfying assignment gives a subset. The unsat preset shows the other half: 0 "
             "subsets for 0 models."),
            ("Taking pseudo-polynomial for polynomial",
             "Subset sum has a dynamic programme whose time is proportional to the target. The "
             "target here is 11144, and every added variable or clause adds a digit, "
             "multiplying it by ten. The programme is polynomial in the value and exponential "
             "in the length of the input, and section 34.5.5 relies on the binary encoding to "
             "say so."),
        ],
        "standard": ("Finish when you can build and check one reduction by hand.",
                     "For a 3-CNF formula with two or three clauses, write the subset-sum "
                     "instance, map a satisfying assignment to a subset and back, explain why "
                     "base 10 matters, and say which direction a reduction must go to prove a "
                     "problem NP-complete."),
        "note": ("The lab solves both sides by exhaustive search, which is possible only on "
                 "tiny formulas and caps their size. Its check that the solutions correspond on "
                 "the formulas you type is evidence for the construction on those formulas; the "
                 "proof in section 34.5.5 covers every formula, and the reduction's polynomial "
                 "running time is part of the proof the lab does not measure."),
    },
    # ---------------------------------------------------------------- 07
    # CLRS 35 intro, 35.1-35.2, pp. 1106-1117. Quote: p. 1106, 10 words,
    # quotes.py OK. Lesson total: 10 words. Lab: coping/vertexcover, kit
    # presets; the lesson's graph 1-2, 2-3, 3-4, 4-5, 2-6, 3-6, 6-7 (matching
    # 3, cover 6, optimum 3) and the exercise's 1-2, 1-3, 1-4, 2-3, 4-5
    # (matching 2, cover 4, optimum 3), read off the kit.
    {
        "slug": "vertex-cover-and-tsp-approximation",
        "title": "Approximating Vertex Cover and TSP",
        "module": "Chapter 35 · Approximation Algorithms",
        "one_line": "An approximation ratio is proved against a lower bound the algorithm can see: a matching for vertex cover, a minimum spanning tree for a tour that obeys the triangle inequality.",
        "summary": (
            "The opening of Chapter 35 and sections 35.1 and 35.2: the approximation ratio and "
            "approximation schemes, APPROX-VERTEX-COVER and its ratio of 2 through a matching, "
            "APPROX-TSP-TOUR's ratio of 2 under the triangle inequality, and the theorem that "
            "without it no constant ratio is possible unless P = NP. Run the vertex-cover "
            "algorithm on a graph written for the lesson and set its answer against the "
            "matching and the optimum."
        ),
        "key": [
            "ratio ρ(n): max(C/C*, C*/C) ≤ ρ(n)",
            "vertex cover: take both ends of any edge",
            "the chosen edges form a matching A",
            "any cover has at least |A| vertices",
            "the algorithm's cover has exactly 2|A|",
            "TSP: preorder walk of an MST, ratio 2",
            "needs the triangle inequality",
        ],
        "key_label": "Sections 35.1 and 35.2 in seven lines",
        "concepts_intro": (
            "Three ideas carry the chapter's first two sections, and the third is the shape of "
            "every proof in it."
        ),
        "concepts": [
            ("An approximation ratio",
             "An algorithm has ratio ρ(n) if, whatever the input and its size n, the cost C of "
             "its answer and the optimal cost C* satisfy max(C/C*, C*/C) ≤ ρ(n). The ratio is never "
             "below 1, and 1 means the answer is optimal."),
            ("The triangle inequality",
             "A cost function on the edges of a complete graph obeys it when going directly "
             "from u to w never costs more than going through a third vertex v: "
             "c(u, w) ≤ c(u, v) + c(v, w). Distances in the plane obey it."),
            ("A computable lower bound",
             "The optimum is unknown, so the proofs compare the answer with something the "
             "algorithm can compute that is no larger than the optimum: the size of a matching "
             "for vertex cover, the weight of a minimum spanning tree for the tour."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read the opening of Chapter 35 and sections 35.1 and 35.2 in your own copy first. "
            "The lesson sets out the argument in its own words and then runs the vertex-cover "
            "algorithm on a graph written for it."
        ),
        "body": [
            ("p", "&ldquo;Even if a problem is NP-complete, there may be hope.&rdquo; Chapter "
                  "35 opens by listing three kinds: inputs small enough for an exponential "
                  "algorithm, special cases that are easy, and algorithms that find answers near "
                  "the optimum in polynomial time. The chapter is about the third, and it insists "
                  "that near be a proved factor. This lesson reads the chapter's opening and "
                  "sections 35.1 and 35.2, and then measures one such factor on a graph of its "
                  "own."),
            ("p", "The opening defines the approximation ratio so that it works for minimization "
                  "and maximization alike: the larger of C/C* and C*/C, never less than 1. An "
                  "algorithm with ratio ρ(n) is a ρ(n)-approximation algorithm. Some problems "
                  "have small constant ratios; for others, such as set cover, the best known "
                  "ratio grows with n. An approximation scheme takes an extra input ε > 0 and "
                  "achieves ratio 1 + ε; it is polynomial-time if it runs in polynomial time for "
                  "each fixed ε, and fully polynomial-time if its running time is polynomial in "
                  "1/ε as well, so that halving ε costs only a constant factor."),
            ("p", "Section 35.1 recalls that a vertex cover is a set of vertices touching every "
                  "edge, and that finding a smallest one is NP-hard, which the previous lesson's "
                  "chain proved. APPROX-VERTEX-COVER is short: while edges remain, take any edge "
                  "(u, v), put both u and v in the cover, and delete every edge touching either. "
                  "With adjacency lists it runs in `O(V + E)` time."),
            ("p", "Theorem 35.1's proof is the chapter's model. Let A be the set of edges the "
                  "algorithm picked. No two of them share a vertex, because picking an edge "
                  "deletes every edge touching its ends, so A is a matching. Any cover, an "
                  "optimal one included, must contain at least one end of each edge of A, and "
                  "those ends are distinct, so |C*| ≥ |A|. The algorithm's cover has exactly "
                  "2|A| vertices. Therefore |C| = 2|A| ≤ 2|C*|. The optimum appears in the "
                  "proof only through the inequality |A| ≤ |C*|; nobody had to know it."),
            ("p", "Section 35.2 turns to the travelling-salesman problem with the triangle "
                  "inequality. APPROX-TSP-TOUR picks a root, grows a minimum spanning tree with "
                  "Prim's algorithm, and visits the vertices in preorder. The lower bound is the "
                  "tree: deleting any edge from an optimal tour leaves a spanning tree, so the "
                  "tree's weight is at most the optimal tour's. A full walk around the tree "
                  "crosses every edge twice and costs twice the tree; skipping repeated vertices "
                  "can only shorten the walk under the triangle inequality. So the tour costs at "
                  "most twice the optimum (Theorem 35.2)."),
            ("p", "Then the section shows the hypothesis is doing the work. Without the triangle "
                  "inequality, Theorem 35.3 says, no polynomial-time algorithm has any constant "
                  "ratio ρ unless P = NP. The proof reduces HAM-CYCLE: give the graph's edges "
                  "cost 1 and every missing edge cost ρ·|V| + 1. A hamiltonian cycle is a tour of "
                  "cost |V|, and any tour that uses a missing edge costs more than ρ·|V|, so a "
                  "ρ-approximation would tell the two cases apart. The Algorithms lessons Twice a "
                  "Matching and The Hypothesis Doing the Work run both algorithms."),
            ("p", "Now the lab, which runs the vertex-cover algorithm, taking edges in the order "
                  "you list them. It prints the vertices and edges, the matching it found (the "
                  "lower bound), the cover it built, the optimum found by searching every subset "
                  "of vertices, the realised ratio against the promised 2, and whether the "
                  "promise held. A second panel enumerates every graph on 3, 4 or 5 vertices, "
                  "runs the algorithm and the exhaustive search on each, and reports the worst "
                  "ratio any of them produced; at 4 vertices that is 2, over 63 graphs with an "
                  "edge."),
            ("p", "Its presets: <code>matching</code> is three disjoint edges, so the matching "
                  "has 3 edges, the cover 6 vertices, the optimum 3, and the ratio is 2. "
                  "<code>star</code> is a hub with four leaves: matching 1, cover 2, optimum 1, "
                  "ratio 2. <code>cycle5</code> gives matching 2, cover 4, optimum 3, ratio 4/3; "
                  "<code>cycle6</code> gives 3, 6, 3 and ratio 2; <code>path5</code> gives a cover "
                  "of 4 against an optimum of 2. <code>triangles</code>, two disjoint triangles, "
                  "gives a cover of 4 equal to the optimum, ratio 1."),
            ("p", "Then type the lesson's graph: `1-2, 2-3, 3-4, 4-5, 2-6, 3-6, 6-7`. The "
                  "algorithm takes 1-2, which removes 2-3 and 2-6; then 3-4, which removes 3-6 "
                  "and 4-5; then 6-7. The matching has 3 edges and the cover is {1, 2, 3, 4, 6, "
                  "7}, 6 vertices. The exhaustive search finds an optimum of 3, for instance "
                  "{2, 4, 6}, so the ratio is exactly 2 on this graph: the bound is met, not "
                  "merely respected. List the edges in another order and the cover can change; "
                  "the guarantee cannot."),
            ("h3", "Exercise"),
            ("code", [
                "1-2, 1-3, 1-4, 2-3, 4-5",
            ]),
            ("p", "Run APPROX-VERTEX-COVER by hand, taking edges in the order listed. Give the "
                  "matching, the cover and its size, then find the optimum by reasoning about "
                  "the triangle 1, 2, 3 and the edge 4-5, and compute the ratio. Say why the "
                  "matching's size, 2, is below the optimum here. Check in the lab."),
            ("p", "Vertex cover and the metric tour have constant ratios. The next lesson, Set "
                  "Cover, Randomization and Subset Sum, meets a ratio that grows with the input, "
                  "one that holds only in expectation, and one you can buy down with time."),
        ],
        "lab": ("coping", {
            "mode": "vertexcover",
            "preset": "matching",
            "panel_title": "Build the cover from a matching, and compare it with the optimum",
            "panel_intro": "Type edges as u-v, separated by commas; the algorithm takes them in "
                           "the order typed. The lab prints the matching, the cover, the "
                           "optimum by exhaustive search and the realised ratio, and the slider "
                           "searches every graph on that many vertices for the worst ratio. "
                           "Type the lesson's graph, then the exercise's.",
        }),
        "steps_title": "Running APPROX-VERTEX-COVER and checking its ratio",
        "steps_intro": "Four steps run the algorithm and its proof; the fifth is a graph of your own.",
        "steps": [
            ("Take an edge and both its ends",
             "Pick any remaining edge (u, v), add u and v to the cover, and record the edge in "
             "the matching A."),
            ("Delete every edge they touch",
             "Remove all edges with u or v as an endpoint. Repeat until no edges remain."),
            ("Name the lower bound",
             "The recorded edges share no vertex, so any cover needs at least |A| vertices. "
             "Write |A| beside the cover's size, 2|A|."),
            ("Compare with the optimum when you can",
             "On a small graph, find the smallest cover by trying subsets, and compute the "
             "realised ratio C/C*. It is at most 2, and it can be less."),
            ("Find a graph where the ratio is below 2",
             "Type a graph of your own on six vertices into the lab whose realised ratio is "
             "strictly between 1 and 2. Write down the matching, the cover and the optimum, and "
             "say where the matching's lower bound is loose."),
        ],
        "worked": {
            "title": "The lesson's graph, edge by edge",
            "intro": [
                "Edges in the order listed: 1-2, 2-3, 3-4, 4-5, 2-6, 3-6, 6-7.",
            ],
            "lines": [
                "take 1-2: cover {1, 2}; remove 2-3, 2-6",
                "take 3-4: cover adds 3, 4; remove 3-6, 4-5",
                "take 6-7: cover adds 6, 7; no edges left",
                "matching A = {1-2, 3-4, 6-7}, |A| = 3",
                "cover C = {1, 2, 3, 4, 6, 7}, |C| = 6",
                "optimum: {2, 4, 6} covers all 7 edges",
                "|A| = 3 ≤ |C*| = 3,  |C| = 6 = 2·|C*|",
            ],
            "after": [
                "The three matched edges share no vertex, so no cover has fewer than 3 vertices, "
                "and {2, 4, 6} shows 3 is enough. The lower bound is exact here and the cover is "
                "twice it, so the ratio is exactly 2. On the lab's cycle5 preset the bound is "
                "loose: the matching has 2 edges, the optimum is 3, and the cover of 4 gives "
                "a ratio of 4/3.",
            ],
        },
        "quiz_title": "Ratios, lower bounds and the hypothesis",
        "quiz": [
            {"q": "Running APPROX-VERTEX-COVER on the exercise's graph 1-2, 1-3, 1-4, 2-3, 4-5 "
                  "in the order listed, what cover does it build, what is the optimum, and what "
                  "is the ratio?",
             "a": ["{1, 2, 4, 5}, optimum 2, ratio 2",
                   "{1, 2, 4, 5}, optimum 3, ratio 4/3",
                   "{1, 2, 3, 4, 5}, optimum 3, ratio 5/3",
                   "{1, 4}, optimum 2, ratio 1"],
             "c": 1,
             "why": "Taking 1-2 removes 1-3, 1-4 and 2-3; taking 4-5 removes nothing more. The "
                    "cover is {1, 2, 4, 5}. The triangle 1, 2, 3 needs two of its vertices and "
                    "the edge 4-5 one more, so the optimum is 3, for instance {1, 2, 4}, and the "
                    "ratio is 4/3. The matching has 2 edges, which is a lower bound, not the "
                    "optimum; {1, 4} leaves 2-3 uncovered."},
            {"q": "In the proof of Theorem 35.1, why is the size of the matching A a lower bound "
                  "on every vertex cover?",
             "a": ["Because the algorithm's cover is twice as large as A",
                   "Because A's edges share no vertex, so a cover needs a different vertex for "
                   "each of them",
                   "Because every graph has a perfect matching",
                   "Because the optimum always equals |A|"],
             "c": 1,
             "why": "Each edge of A must be covered, and no vertex covers two of them, since they "
                    "are disjoint. That |C| = 2|A| is the other half of the proof, the upper "
                    "half. Not every graph has a perfect matching, and the exercise's graph shows "
                    "the optimum can exceed |A|."},
            {"q": "APPROX-TSP-TOUR is run on a complete graph whose costs violate the triangle "
                  "inequality. What does section 35.2 let you conclude about its tour?",
             "a": ["It is still within twice the optimum, because the tree is still a lower "
                   "bound",
                   "Nothing from Theorem 35.2, because the shortcutting step can then make the "
                   "tour longer",
                   "It is optimal, because the minimum spanning tree is optimal",
                   "It is within ρ of the optimum for some constant ρ depending on the costs"],
             "c": 1,
             "why": "The tree is still a lower bound, but the step from the full walk to the tour "
                    "skips vertices, and only the triangle inequality guarantees that a skip does "
                    "not cost more. Theorem 35.3 goes further: for general costs no "
                    "polynomial-time algorithm has any constant ratio unless P = NP. A minimum "
                    "spanning tree is not a tour."},
        ],
        "mistakes": [
            ("Thinking the ratio needs the optimum",
             "A ratio of 2 is a statement about the optimum, which no one can compute fast. The "
             "proof never computes it: it compares the answer with the matching, which the "
             "algorithm builds anyway and which can only be smaller than the optimum. The lab "
             "computes the optimum by exhaustive search only to show you the realised ratio on "
             "small graphs."),
            ("Reading a realised ratio as the algorithm's ratio",
             "On the lab's cycle5 preset the ratio is 4/3, and on the exercise's graph also "
             "4/3; on the lesson's graph it is 2. The guarantee is the worst over every input, "
             "and a single graph shows one value under it. The lab's sweep over all graphs of a "
             "size finds 2 at every size it can search, which matches the theorem without "
             "proving it for larger graphs."),
            ("Dropping the triangle inequality",
             "The MST tour's factor of 2 rests on the triangle inequality at the shortcutting "
             "step. Section 35.2 does not leave this as a technicality: Theorem 35.3 shows that "
             "without it no constant ratio is achievable in polynomial time unless P = NP."),
        ],
        "standard": ("Finish when you can prove a ratio of 2 from a lower bound.",
                     "Run APPROX-VERTEX-COVER on a small graph, name the matching, prove from it "
                     "that the cover is at most twice the optimum, compute the realised ratio "
                     "against the optimum, and say where the triangle inequality enters the TSP "
                     "argument."),
        "note": ("The lab's optimum is an exhaustive search, so it works only on small graphs, "
                 "and its sweep covers every graph on at most five vertices; both are evidence "
                 "about those graphs. The theorem's ratio holds for every graph, and only its "
                 "proof establishes that. This lab does not run the TSP algorithm."),
    },
    # ---------------------------------------------------------------- 08
    # CLRS 35.3-35.5, pp. 1117-1139. Quote: p. 1107, 13 words, quotes.py OK.
    # Lesson total: 13 words. Lab: coping/setcover, kit presets; the lab
    # bounds by H over the universe, not the book's H(max |S|) (see the
    # report). The lesson's family 1 2 3 4; 5 6 7 8; 1 2 5 6 7 (greedy 3,
    # optimum 2) and the exercise's 1 2 3 4; 1 3 5; 2 4 6 (greedy 3, optimum
    # 2), read off the kit. The trimming example in the body is the lesson's
    # own numbers, worked by hand.
    {
        "slug": "set-cover-randomization-and-subset-sum",
        "title": "Set Cover, Randomization and Subset Sum",
        "module": "Chapter 35 · Approximation Algorithms",
        "one_line": "Greedy set cover is within a harmonic number of the optimum, a random assignment satisfies 7/8 of a 3-CNF formula's clauses in expectation, and trimming a list of sums buys accuracy with time.",
        "summary": (
            "Sections 35.3 to 35.5: GREEDY-SET-COVER and its ratio H(max |S|), the randomized "
            "8/7-approximation for MAX-3-CNF satisfiability, rounding a linear program for "
            "weighted vertex cover, and the fully polynomial-time approximation scheme for "
            "subset sum that trims its lists of sums. Run greedy set cover on a family written "
            "for the lesson, add up the charges, and trim a list of sums by hand."
        ),
        "key": [
            "greedy: take the set covering most new",
            "ratio H(max |S|) ≤ ln |X| + 1",
            "each new element pays 1/(new elements)",
            "random assignment: 7/8 of clauses expected",
            "weighted cover: round the LP at 1/2",
            "trim: drop y if some z ≤ y ≤ (1 + δ)·z",
            "δ = ε/(2n) gives ratio 1 + ε",
        ],
        "key_label": "Sections 35.3 to 35.5 in seven lines",
        "concepts_intro": (
            "Three ideas carry these sections, one for each kind of guarantee the chapter ends "
            "with."
        ),
        "concepts": [
            ("A charge",
             "When greedy takes a set that covers k new elements, each of those elements is "
             "charged 1/k. The charges add up to the number of sets taken, and bounding the "
             "charges paid by the elements of any one set bounds the whole cover."),
            ("An expected ratio",
             "A randomized algorithm has ratio ρ(n) when the expected cost of its answer is "
             "within a factor ρ(n) of the optimum. Setting each variable of a 3-CNF formula true "
             "or false with probability 1/2 leaves a clause unsatisfied with probability 1/8."),
            ("Trimming",
             "Removing from a sorted list of subset sums every value y that some kept value z "
             "represents, meaning z ≤ y ≤ (1 + δ)·z. The list stays short, and every removed "
             "sum is approximated within a factor 1 + δ."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read sections 35.3, 35.4 and 35.5 in your own copy first. The lesson sets out the "
            "argument in its own words, runs greedy set cover on a family written for it, and "
            "trims a list of sums by hand."
        ),
        "body": [
            ("p", "&ldquo;That is, we can trade computation time for the quality of the "
                  "approximation.&rdquo; The chapter's opening says this of approximation "
                  "schemes, and its last section delivers one. Before that come two other kinds "
                  "of guarantee: a ratio that grows slowly with the input, and a ratio that holds "
                  "on average over the algorithm's own coin flips. This lesson reads sections "
                  "35.3 to 35.5 and ends the read-along."),
            ("p", "Section 35.3 states the set-covering problem: given a finite X and some "
                  "subsets of it, F, whose union is X; find the smallest subfamily whose union is still X. "
                  "It generalizes vertex cover, so it is NP-hard. GREEDY-SET-COVER repeatedly "
                  "takes the set that covers the most elements not yet covered, until none "
                  "remain, and can be implemented in time polynomial in |X| and |F|."),
            ("p", "Theorem 35.4 bounds it by H(max |S|), the harmonic number of the size of the "
                  "largest set, where H(d) = 1 + 1/2 + … + 1/d. The proof charges each element "
                  "1/k when it is first covered by a set that covers k new elements, so that the "
                  "charges add up to the number of sets greedy takes. It then shows that the "
                  "elements of any one set S, an optimal set included, pay at most H(|S|) in "
                  "total, because when j of S's elements remain uncovered greedy takes a set "
                  "covering at least j new elements. Summing over an optimal cover gives the "
                  "ratio, and since |S| ≤ |X|, Corollary 35.5 adds that the ratio is at most "
                  "ln |X| + 1."),
            ("p", "Section 35.4 shows two more techniques. For MAX-3-CNF satisfiability, where "
                  "every clause has exactly three distinct literals and none holds a variable "
                  "with its negation, set each variable true with probability 1/2. A clause fails "
                  "only if all three literals are false, with probability 1/8, so by linearity of "
                  "expectation 7/8 of the clauses are satisfied on average. No assignment "
                  "satisfies more than all of them, so the expected ratio is at most 8/7 "
                  "(Theorem 35.6). The section's second technique is linear programming: relax "
                  "weighted vertex cover to fractions between 0 and 1, solve, and put a vertex in "
                  "the cover when its value is at least 1/2. Every edge's constraint forces one "
                  "end to 1/2 or more, and the rounding at most doubles the cost, a "
                  "2-approximation (Theorem 35.7)."),
            ("p", "Section 35.5 finishes with subset sum as an optimization: the largest sum of a "
                  "subset of S that does not exceed t. The exact method keeps a sorted list of "
                  "every reachable sum up to t, merging the list with a copy shifted by each new "
                  "element; the list can double each time. APPROX-SUBSET-SUM trims the list "
                  "after each merge with δ = ε/(2n), and Theorem 35.8 shows that the answer is "
                  "within 1 + ε of the optimum and that every list stays short enough for a "
                  "running time polynomial in n and 1/ε: a fully polynomial-time approximation "
                  "scheme. Here is a trim on numbers of the lesson's own, S = {12, 20, 31, 45}, "
                  "t = 70, ε = 0.4, so δ = 0.4/8 = 0.05."),
            ("math", [
                "after 12:  0, 12",
                "after 20:  0, 12, 20, 32",
                "after 31:  merged 0, 12, 20, 31, 32, 43, 51, 63",
                "           32 ≤ 1.05 · 31, so 32 is dropped",
                "after 45:  merged list, then 45 ≤ 1.05 · 43 and 65 ≤ 1.05 · 63 dropped",
                "           kept up to 70:  0, 12, 20, 31, 43, 51, 57, 63",
                "answer 63;  optimum 20 + 45 = 65;  65/63 ≤ 1.4",
            ]),
            ("p", "The trim threw away 65, the optimum itself, because 63 was within 5 per cent "
                  "of it, and the answer lost about 3 per cent where ε allowed 40. The Algorithms "
                  "lessons Charging Every Element and Accuracy by the Epsilon run greedy set cover "
                  "and an approximation scheme for knapsack, a different scheme from the book's "
                  "trimming."),
            ("p", "Now the lab, which runs greedy set cover on the family you type and prints "
                  "the universe and sets, the sets greedy took in order, the optimum by searching "
                  "every subfamily, the realised ratio, a harmonic number H over the size of the "
                  "universe, the bound H times the optimum, whether the answer is within it, and "
                  "whether the charges add up to the answer. Its bound uses H(|X|), which is "
                  "Corollary 35.5's coarser form: H(max |S|) is never larger, and the lesson "
                  "computes it beside the lab's."),
            ("p", "Its presets: <code>trap</code> has 7 elements and 3 sets; greedy takes all 3, "
                  "the optimum is 2, the ratio 3/2, against a bound of 363/70 from H₇ = 363/140. "
                  "<code>trap10</code> is the same trap on 10 elements, again 3 against 2. "
                  "<code>clean</code> is a partition into 2 sets, and greedy is optimal with "
                  "charges 2 against 2. <code>overlap</code> has five overlapping triples and "
                  "greedy finds an optimal cover of 2. <code>singletons</code> has one big set "
                  "and the singletons under it; greedy takes the big set, and the bound is "
                  "H₅ = 137/60."),
            ("p", "Then type the lesson's family: `1 2 3 4; 5 6 7 8; 1 2 5 6 7`. Greedy takes "
                  "S3 first, five new elements charged 1/5 each; then S1, which adds 3 and 4 at "
                  "1/2 each; then S2, which adds only 8, charged 1. The charges add to 3, the "
                  "optimum is 2 (S1 and S2), and the ratio is 3/2. The lab's bound is "
                  "2·H₈ = 761/140, about 5.44; the book's is 2·H(5) = 137/30, about 4.57. Both "
                  "hold with room to spare, which is what a bound over every input usually looks "
                  "like on one of them."),
            ("h3", "Exercise"),
            ("code", [
                "S1 = {1, 2, 3, 4}   S2 = {1, 3, 5}   S3 = {2, 4, 6}",
            ]),
            ("p", "Run GREEDY-SET-COVER by hand, giving the charge each element pays. Find the "
                  "optimum, the realised ratio and the book's bound 2·H(max |S|). Then type the "
                  "family as `1 2 3 4; 1 3 5; 2 4 6` and compare."),
            ("p", "That ends the read-along of Parts I to VII. Part VIII of the book, the "
                  "appendices on summations, sets, counting and probability and matrices, is the "
                  "background these lessons leaned on; and the Algorithms Subject's course "
                  "Intractability and Approximation takes the last two chapters further, with "
                  "branch and bound and parameterized algorithms."),
        ],
        "lab": ("coping", {
            "mode": "setcover",
            "preset": "trap",
            "panel_title": "Step through greedy's choices and add up the charges",
            "panel_intro": "Type sets as elements separated by spaces, and sets separated by "
                           "semicolons. The lab runs greedy, prices every element at 1/k when "
                           "it is one of k new elements, finds the optimum by searching every "
                           "subfamily, and bounds the cover by H over the universe. Type the "
                           "lesson's family, then the exercise's.",
        }),
        "steps_title": "Running greedy set cover and checking its bound",
        "steps_intro": "Four steps run the algorithm and the book's bound; the fifth is a family of your own.",
        "steps": [
            ("Take the set with the most new elements",
             "Among the sets, find the one containing the most elements not yet covered. Break "
             "a tie any way you like, and note how you broke it."),
            ("Charge its new elements",
             "If it covers k new elements, each pays 1/k. Repeat until every element is "
             "covered; the number of sets taken equals the sum of the charges."),
            ("Compute the book's bound",
             "Find the largest set's size d and the harmonic number H(d) = 1 + 1/2 + … + 1/d. "
             "The cover has at most H(d) times as many sets as an optimal one."),
            ("Compare with the optimum on small families",
             "Try subfamilies of increasing size until one covers everything. Divide greedy's "
             "count by it for the realised ratio, and check it is at most H(d)."),
            ("Build a trap of your own",
             "Write a family on ten elements where greedy takes at least one more set than the "
             "optimum, type it into the lab, and record the two counts, the charges and both "
             "bounds, H(max |S|) by hand and the lab's H over the universe."),
        ],
        "worked": {
            "title": "Greedy on the lesson's family, with the charges",
            "intro": [
                "X = {1, …, 8}; S1 = {1, 2, 3, 4}, S2 = {5, 6, 7, 8}, S3 = {1, 2, 5, 6, 7}.",
            ],
            "lines": [
                "step 1: S3 covers 5 new; 1, 2, 5, 6, 7 pay 1/5",
                "step 2: S1 covers 3, 4; each pays 1/2",
                "step 3: S2 covers 8; it pays 1",
                "charges: 5·(1/5) + 2·(1/2) + 1 = 3 sets",
                "optimum: S1 and S2, 2 sets; ratio 3/2",
                "book: H(5) = 137/60;  2·H(5) = 137/30",
                "lab: H(8) = 761/280;  2·H(8) = 761/140",
            ],
            "after": [
                "Look at the charges inside the optimal set S2: 5, 6 and 7 paid 1/5 each and 8 "
                "paid 1, a total of 8/5, well under H(4) = 25/12, the most the proof allows a "
                "set of four elements to pay. The same holds for S1: 1/5 + 1/5 + 1/2 + 1/2 = "
                "7/5. Adding the two gives 3, greedy's count, and the proof's argument is that "
                "this sum can never exceed the optimum times H of the largest set.",
            ],
        },
        "quiz_title": "Greedy charges, expectations and trimming",
        "quiz": [
            {"q": "Running GREEDY-SET-COVER on the exercise's family S1 = {1, 2, 3, 4}, "
                  "S2 = {1, 3, 5}, S3 = {2, 4, 6}, how many sets does it take, what is the "
                  "optimum, and what is the book's bound on greedy's count?",
             "a": ["3 sets, optimum 2, bound 2·H(4) = 25/6",
                   "2 sets, optimum 2, bound 2·H(4) = 25/6",
                   "3 sets, optimum 2, bound 2·H(6) = 49/10",
                   "3 sets, optimum 3, bound 3·H(4) = 25/4"],
             "c": 0,
             "why": "Greedy takes S1 first (four new elements, 1/4 each), then S2 and S3 each "
                    "cover one new element, 5 and 6, paying 1 each: 3 sets, charges "
                    "1 + 1 + 1. S2 and S3 together cover all six, so the optimum is 2. The "
                    "largest set has 4 elements, H(4) = 25/12, and the bound is 25/6. The bound "
                    "with H(6) = 49/20 is the lab's coarser one over the universe, not the "
                    "book's."},
            {"q": "A 3-CNF formula has 40 clauses, each with three distinct literals and no "
                  "variable with its negation. Each variable is set true or false by a fair "
                  "coin. What is the expected number of satisfied clauses?",
             "a": ["20",
                   "35",
                   "40 − 3 = 37",
                   "It depends on how many clauses share variables"],
             "c": 1,
             "why": "Each clause fails only if its three literals are all false, probability "
                    "(1/2)³ = 1/8, so it is satisfied with probability 7/8. Linearity of "
                    "expectation holds whether or not clauses share variables, so the expected "
                    "count is 40 · 7/8 = 35. Twenty would be the chance of one literal, not of "
                    "at least one of three."},
            {"q": "Trimming the sorted list 0, 12, 20, 31, 32, 43 with δ = 0.05, which values "
                  "are removed?",
             "a": ["None, because no two values are equal",
                   "32, because 31 ≤ 32 ≤ 1.05 · 31 = 32.55",
                   "32 and 43, because each is within 12 of the value before",
                   "20 and 32"],
             "c": 1,
             "why": "Trimming keeps a value only if it exceeds (1 + δ) times the last value kept. "
                    "12 > 0, 20 > 12.6 and 31 > 21 are kept; 32 is at most 32.55 and is "
                    "dropped; 43 > 32.55 is kept. The rule is a ratio, not a difference, so 43 "
                    "stays, and 20 is far more than 5 per cent above 12."},
        ],
        "mistakes": [
            ("Expecting greedy to be optimal because it is greedy",
             "Chapter 16's greedy algorithms were optimal because their problems had the "
             "greedy-choice property. Set cover does not. On the lesson's family greedy's first "
             "choice, the largest set, is in no optimal cover, and it ends with 3 sets where 2 "
             "suffice. What section 35.3 proves is a bound, H(max |S|), not optimality."),
            ("Reading 8/7 as a guarantee on every run",
             "The ratio for MAX-3-CNF is about the expected number of satisfied clauses over the "
             "algorithm's coin flips. A single run can do worse than 7/8 of the clauses; the "
             "theorem says that on average it does not. Repeating the algorithm, or fixing "
             "variables one at a time by conditional expectation, are ways to turn the average "
             "into a certainty."),
            ("Thinking an approximation scheme is free accuracy",
             "Each halving of ε roughly doubles the trimmed lists and the running time. The "
             "scheme is fully polynomial because the cost grows polynomially in 1/ε, not because "
             "it does not grow. In the lesson's trim, ε = 0.4 kept 8 sums where the exact "
             "method would have kept 11 of the 16 subset sums at or below 70."),
        ],
        "standard": ("Finish when you can run and bound greedy set cover, and trim a list.",
                     "For a family of three to five sets, run greedy with its charges, compute "
                     "H(max |S|) and the bound, and compare with the optimum; compute the "
                     "expected satisfied clauses of a random assignment; and trim a sorted list "
                     "of sums for a given δ."),
        "note": ("The lab's optimum is an exhaustive search over subfamilies, so it handles "
                 "only small families, and its bound uses H over the universe, which is looser "
                 "than the book's H(max |S|). It runs neither the randomized MAX-3-CNF algorithm "
                 "nor the trimming scheme. Its counts are about the family you type; the ratio "
                 "H(max |S|) is the book's proof about every family."),
    },
]
