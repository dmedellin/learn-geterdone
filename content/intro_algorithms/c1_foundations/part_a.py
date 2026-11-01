"""Foundations, lessons 1-5 -- Chapters 1, 2 and 3.

Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, 3rd ed.
(MIT Press, 2009): Chapter 1, The Role of Algorithms in Computing
(pp. 5-14); Chapter 2, Getting Started (pp. 16-42); Chapter 3, Growth of
Functions, sections 3.1-3.2 (pp. 43-64). Every quotation is copied from the
operator's copy with its printed page in the comment beside the lesson. The
arrays, machines and functions are written for these lessons: none of the
book's figures, examples or exercises is reproduced, and its procedures are
described in prose and named.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # CLRS Chapter 1, sections 1.1-1.2, pp. 5-14.
    # Quote: p. 13, 15 words, quotes.py OK. Lesson total: 15 words.
    # Algorithm, computational problem, instance, correctness (pp. 5-6);
    # the kinds of problems, data structures, hard problems, parallelism
    # (pp. 6-10); infinitely fast computers, efficiency, the two-computers
    # comparison and its crossover (pp. 11-13); algorithms and other
    # technologies (pp. 13-14).
    {
        "slug": "algorithms-as-a-technology",
        "title": "Algorithms as a Technology",
        "module": "Chapter 1 · The Role of Algorithms in Computing",
        "one_line": "An algorithm is a well-defined procedure that turns every instance of a problem into the right output, and the choice of algorithm can matter more than a machine a thousand times faster.",
        "summary": (
            "Chapter 1 says what an algorithm is, what it means for one to be correct, and why "
            "efficiency is worth studying even on fast hardware. Its central argument is "
            "arithmetic: a quadratic sort on a fast machine against an n lg n sort on a slow one, "
            "and the size beyond which the slow machine always wins. Work that arithmetic by "
            "hand, then race two programs of your own in the lab and find their crossover."
        ),
        "key": [
            "an instance is one input to a problem",
            "correct: right output on every instance",
            "time = constant · cost(n) / speed",
            "a lower order of growth wins for good",
            "the crossover can come at a modest n",
        ],
        "key_label": "Chapter 1 in five lines",
        "concepts_intro": (
            "Three ideas from the chapter. Everything later in the book is built from the first "
            "two and justified by the third."
        ),
        "concepts": [
            ("Problem, algorithm and instance",
             "A computational problem states, in general terms, which outputs are acceptable for "
             "which inputs. An algorithm is a well-defined procedure that produces such an output. "
             "An instance is one particular input: one array to sort, one map to route across."),
            ("Correctness",
             "An algorithm is correct if, on every instance, it halts with a correct output. A "
             "procedure that works on the inputs you tried has not yet been shown correct; the "
             "book's way of showing it, the loop invariant, is the next lesson."),
            ("Efficiency as a technology",
             "Two correct algorithms for one problem can differ in running time by far more than "
             "two machines do. The book asks you to treat the choice of algorithm the way you "
             "treat the choice of hardware: as a technology that decides how fast a system is."),
        ],
        "read_title": "The chapter's argument first, then the race",
        "read_intro": (
            "Read Chapter 1 in your own copy first; it is short. The lesson sets out its two "
            "sections in its own words, works the two-machines arithmetic on an instance written "
            "for the lesson, and then lets you race programs of your own."
        ),
        "body": [
            ("p", "&ldquo;Total system performance depends on choosing efficient algorithms as "
                  "much as on choosing fast hardware.&rdquo; The authors reach that sentence in "
                  "the last part of Section 1.2, just after a calculation that most readers remember long "
                  "after the rest of the chapter. This lesson reads Chapter 1, The Role of "
                  "Algorithms in Computing: Section 1.1 on what an algorithm is, and Section 1.2 "
                  "on why its efficiency is a technology in its own right."),
            ("p", "Section 1.1 begins informally. An algorithm accepts an input, one value or many, "
                  "carries out a sequence of well-defined computational steps, and delivers an "
                  "output, again one value or many. The problem it solves is stated "
                  "separately, as a relation between inputs and acceptable outputs, and the "
                  "authors take sorting as their running example: given a sequence of n numbers, "
                  "produce a permutation of it in nondecreasing order. One particular input "
                  "sequence is an instance of the problem."),
            ("def", ("Correct algorithm",
                     "An algorithm is <strong>correct</strong> if on each instance of its problem "
                     "it halts, and halts with a right answer; a correct algorithm "
                     "<strong>solves</strong> the problem. An incorrect one may fail to halt on "
                     "some instance or halt with a wrong answer. The authors note that an "
                     "incorrect algorithm is sometimes useful when its error rate can be "
                     "controlled, and point to the primality tests of Chapter 31.")),
            ("p", "The rest of Section 1.1 is a tour. Sequencing a genome, routing data across "
                  "the Internet, keeping electronic commerce private, and allocating scarce "
                  "resources in a business are all problems whose solutions rest on algorithms "
                  "the book later teaches: shortest paths, longest common subsequences, "
                  "topological sorting, convex hulls, linear programming. Two features recur. "
                  "Each problem has a great many candidate solutions, most of them not what is "
                  "wanted, and each has practical use. The section closes with four threads "
                  "the book returns to: data structures, techniques of design and analysis for "
                  "problems no published algorithm covers, problems for which no efficient "
                  "algorithm is known (the NP-complete problems of Chapter 34), and parallelism "
                  "on multicore machines (Chapter 27)."),
            ("p", "Section 1.2 asks a question to clear the ground. If computers were infinitely "
                  "fast and memory free, would algorithms still be worth studying? Yes, the "
                  "authors answer, because you would still need to show that your method halts "
                  "and gives the right answer; but you would then use whichever correct method "
                  "was easiest to write. Real computers are fast but finite, so time and space "
                  "are bounded resources, and efficiency decides how much of them a method uses."),
            ("p", "The argument is a comparison of two sorts the next chapter analyses. Insertion "
                  "sort takes time roughly `c₁·n²` and merge sort roughly `c₂·n·lg n`, with "
                  "constants that do not depend on n, and insertion sort usually has the smaller "
                  "constant. Write the two as `c₁·n·n` and `c₂·n·lg n` and the difference is a "
                  "factor of n against a factor of `lg n`. However much smaller `c₁` is, once n "
                  "is large enough the factor `lg n` makes up for it, so there is always a "
                  "crossover beyond which merge sort is faster. The authors then make this "
                  "concrete with two computers, one a thousand times faster than the other."),
            ("math", [
                "the lesson's own two machines, sorting 5 million keys",
                "",
                "A: 3n² instructions at 5 billion a second",
                "   3 · (5·10⁶)² / (5·10⁹) = 15,000 s, over four hours",
                "B: 60n lg n instructions at 20 million a second",
                "   60 · 5·10⁶ · lg(5·10⁶) / (2·10⁷) ≈ 333.8 s, under six minutes",
            ]),
            ("p", "Machine A is 250 times faster than machine B and runs code twenty times "
                  "leaner, and it still loses by a factor of about 45. The book's own figures, in "
                  "Section 1.2, make the same point with a still wider gap in machine speed. The "
                  "point is not the particular numbers. It is that the ratio of the two times "
                  "grows without bound as n grows, so for big enough inputs no lead in hardware "
                  "or coding survives a worse order of growth."),
            ("p", "The section ends by placing algorithms beside the other technologies a system "
                  "depends on, such as fast hardware, graphical interfaces, object-oriented "
                  "systems and networking. Even an application with no algorithmic content of "
                  "its own leans on algorithms everywhere below it: the hardware was designed "
                  "with them, the interface is drawn with them, the network routes with them, "
                  "and the compiler that translated the program is full of them. And because "
                  "computers keep getting larger, people keep solving larger problems, which is "
                  "exactly where differences in efficiency show."),
            ("p", "Now the lab. Choose a cost function and a constant for each program and a "
                  "speed for each machine; each time is the constant times the cost at n, divided "
                  "by the speed. The tiles are the crossover, the least n from which the program "
                  "with the slower-growing cost is faster at every larger size; each program's "
                  "time at your n; and which is faster there, by what factor. Every comparison "
                  "involving `lg n` is decided exactly, and times containing it print rounded."),
            ("p", "The worked example <code>five-million</code> is the table above: 15,000 "
                  "seconds for A, about 333.80 for B, and B about 44.9 times faster. Its crossover "
                  "is n = 81,580. Choose <code>one-thousand</code>: the same two machines sorting "
                  "a thousand keys, where A finishes in six ten-thousandths of a second and is "
                  "about 49.8 times faster than B. The crossover has not moved, because it "
                  "depends on the programs and machines, not on the n you ask about."),
            ("p", "Two more examples show the edges of the argument. In "
                  "<code>same-order</code> both programs cost `n·lg n`, and the lab reports that "
                  "there is no crossover: the ratio of the two times is a constant, here 5,000, "
                  "at every n, so the faster machine and the leaner code win for good. In "
                  "<code>exponential</code> program A costs `2ⁿ` on the fast machine and program "
                  "B costs `100·n³` on the slow one; the crossover is n = 30, and at n = 60 A "
                  "would need about 230 million seconds, over seven years, against B's 1.08 "
                  "seconds."),
            ("h3", "Exercise"),
            ("p", "Program A costs `4n²` instructions on a machine that runs 2 billion a "
                  "second; program B costs `100n lg n` on a machine that runs 50 million a "
                  "second. By hand, trying n = 2¹⁰, 2¹¹, 2¹², and so on, find the least power "
                  "of 2 at which B is faster than A. Then set the lab to these programs and read "
                  "the exact crossover."),
            ("p", "The chapter argued that insertion sort loses to merge sort for large n without "
                  "yet saying what either does. The next lesson, Insertion Sort and Loop "
                  "Invariants, opens Chapter 2 with the first of them and with the tool the book "
                  "uses to prove every loop it writes correct."),
        ],
        "lab": ("itakit", {
            "mode": "growth",
            "view": "race",
            "preset": "five-million",
            "presets": [
                {"id": "five-million",
                 "label": "3n² at 5 billion a second against 60n lg n at 20 million, 5 million keys",
                 "fnA": "n^2", "costA": "3", "speedA": "5000000000",
                 "fnB": "n lg n", "costB": "60", "speedB": "20000000", "n": "5000000",
                 "expect": {"griCross": "n = 81,580: from there on B (n lg n) is always faster",
                            "griTimeA": "15,000 s", "griTimeB": "≈ 333.80 s",
                            "griFaster": "B, ≈ 44.9× faster"}},
                {"id": "one-thousand",
                 "label": "The same two machines, 1,000 keys",
                 "fnA": "n^2", "costA": "3", "speedA": "5000000000",
                 "fnB": "n lg n", "costB": "60", "speedB": "20000000", "n": "1000",
                 "expect": {"griCross": "n = 81,580: from there on B (n lg n) is always faster",
                            "griFaster": "A, ≈ 49.8× faster"}},
                {"id": "same-order",
                 "label": "Both programs n lg n, the slow machine running the costly code",
                 "fnA": "n lg n", "costA": "60", "speedA": "20000000",
                 "fnB": "n lg n", "costB": "3", "speedB": "5000000000", "n": "5000000",
                 "expect": {"griCross": "never: the same order of growth, so A always takes 5,000× B's time",
                            "griFaster": "B, ≈ 5,000.0× faster"}},
                {"id": "exponential",
                 "label": "2ⁿ on the fast machine against 100n³ on the slow one, n = 60",
                 "fnA": "2^n", "costA": "1", "speedA": "5000000000",
                 "fnB": "n^3", "costB": "100", "speedB": "20000000", "n": "60",
                 "expect": {"griCross": "n = 30: from there on B (n^3) is always faster",
                            "griTimeB": "27/25 = 1.08 s"}},
            ],
            "panel_title": "Race two programs on two machines",
            "panel_intro": (
                "Each program has a cost function, a constant and a machine speed; its time at n "
                "is the constant times the cost, divided by the speed. The lab finds the size "
                "from which the program with the slower-growing cost is always faster, and "
                "compares the two at the n you choose."
            ),
        }),
        "steps_title": "Finding a crossover by hand",
        "steps_intro": "Four steps with a calculator, then one race of your own.",
        "steps": [
            ("Write each time as a formula",
             "Time is constant times cost at n, divided by machine speed. Write both, for "
             "example `3n²/(5·10⁹)` and `60n lg n/(2·10⁷)`, in seconds."),
            ("Divide one by the other",
             "Cancel what you can. For the lesson's machines the ratio of A's time to B's is "
             "`n/(5000·lg n)`, so B is faster exactly when `n > 5000·lg n`."),
            ("Bracket the crossover with powers of 2",
             "At `n = 2ᵏ`, `lg n` is just k, so the test is arithmetic. Find the last power of 2 "
             "where the slower-growing program still loses and the first where it wins."),
            ("Narrow the bracket",
             "Halve the interval and test the midpoint, keeping the half where the winner "
             "changes, until it is as narrow as you need. This is what the lab does past n = 64."),
            ("Race two of your own",
             "Pick two programs and machines you find plausible, find the bracketing powers of 2 "
             "by hand, then enter them in the lab and check that its crossover lies in your "
             "bracket."),
        ],
        "worked": {
            "title": "Five million keys on two machines",
            "intro": [
                "Machine A runs 5 billion instructions a second and program A costs `3n²`; "
                "machine B runs 20 million a second and program B costs `60n lg n`. Sort "
                "n = 5,000,000 keys, then find the crossover.",
            ],
            "lines": [
                "A: 3 · 2.5·10¹³ = 7.5·10¹³ instructions",
                "   7.5·10¹³ / 5·10⁹ = 15,000 s",
                "B: lg(5·10⁶) ≈ 22.25",
                "   60 · 5·10⁶ · 22.25 ≈ 6.68·10⁹",
                "   6.68·10⁹ / 2·10⁷ ≈ 334 s",
                "B wins when n > 5000·lg n",
                "2¹⁶: 65,536 < 80,000, A still wins",
                "2¹⁷: 131,072 > 85,000, B wins",
            ],
            "after": [
                "So the crossover lies between 65,536 and 131,072, and the lab's exact answer, "
                "81,580, is inside the bracket. At five million keys B is about 45 times faster; "
                "at a thousand keys, below the crossover, A is about 50 times faster.",
            ],
        },
        "quiz_title": "Correctness, crossovers and orders of growth",
        "quiz": [
            {"q": "In the exercise, program A costs `4n²` at 2 billion instructions a second and "
                  "program B costs `100n lg n` at 50 million a second. What is the least power "
                  "of 2 at which B is faster?",
             "a": ["8,192", "16,384", "32,768", "1,024"],
             "c": 1,
             "why": "The ratio of A's time to B's is `n/(1000·lg n)`, so B is faster when "
                    "`n > 1000·lg n`. At 2¹³ = 8,192 the right side is 13,000, so A still wins; "
                    "at 2¹⁴ = 16,384 it is 14,000, and B wins. The lab's exact crossover is "
                    "13,747, between the two. At 32,768 B is faster too, but it is not the least "
                    "such power; at 1,024 A is faster by a wide margin."},
            {"q": "Keep the lesson's programs and make machine B ten times faster, 200 million "
                  "instructions a second. Where is the crossover now?",
             "a": ["8,158, a tenth of 81,580", "81,580, unchanged",
                   "6,312", "815,800, ten times 81,580"],
             "c": 2,
             "why": "B now wins when `n > 500·lg n`, and the least such n is 6,312 (the lab "
                    "confirms it). The crossover does move, because it is where the two times "
                    "meet, and it falls by a factor of about 13, not exactly 10, because `lg n` "
                    "shrinks too as n shrinks. Ten times 81,580 would mean B got "
                    "slower."},
            {"q": "Which of these is what Section 1.1 means by a correct algorithm?",
             "a": ["It halts with the correct output on every input it has been tested on",
                   "It halts with the correct output on every instance of the problem",
                   "It halts on every instance of the problem",
                   "It produces the correct output on most instances, with a controllable error "
                   "rate"],
             "c": 1,
             "why": "Correctness is a claim about every instance: halting and being right. "
                    "Passing tests says nothing about the instances not tested. Halting alone "
                    "allows a wrong answer. A controllable error rate describes the useful "
                    "incorrect algorithms the authors mention, such as Chapter 31's primality "
                    "tests, which they set apart from correct ones."},
            {"q": "In the example <code>same-order</code>, both programs cost `n lg n`, with "
                  "constants 60 and 3, on machines of 20 million and 5 billion instructions a "
                  "second. What does the lab report for the crossover, and why?",
             "a": ["None: the ratio of the two times is the same at every n",
                   "n = 2, because the fast machine wins from the first comparison",
                   "A crossover beyond 10¹⁵, too large for the lab to find",
                   "n = 81,580, as for the lesson's first pair of programs"],
             "c": 0,
             "why": "With the same cost function the ratio of the times is `(60/(2·10⁷))` over "
                    "`(3/(5·10⁹))`, which is 5,000 whatever n is, so neither program ever "
                    "overtakes the other and there is no crossover to find. A crossover at n = 2 "
                    "would mean the other program was ahead at n = 1. Nothing grows here, so "
                    "there is nothing beyond 10¹⁵ either. 81,580 belongs to the quadratic "
                    "program against the n lg n one."},
        ],
        "mistakes": [
            ("Believing faster hardware can make up for a worse algorithm",
             "A faster machine divides every running time by the same constant, and a leaner "
             "program multiplies it by a smaller one. A better order of growth changes the "
             "ratio itself, which grows without bound, so beyond the crossover no constant "
             "lead survives. On the lesson's illustration, a machine 250 times faster running "
             "code 20 times leaner loses by a factor of about 45 at five million keys."),
            ("Expecting the better order of growth to win at every size",
             "Below the crossover the program with the smaller constant wins, and the authors "
             "say that insertion sort usually beats merge sort on small inputs. On the lesson's "
             "machines the quadratic program is about 50 times faster at a thousand keys. The "
             "chapter's claim is about large enough n, and the crossover tells you where that "
             "begins for one pair of programs and machines."),
            ("Calling a procedure correct because it passed its tests",
             "The definition in Section 1.1 quantifies over every instance, and a finite set of "
             "tests covers almost none of them. A test can show a procedure is wrong; showing it "
             "right needs an argument about all inputs, which is what the loop invariant of the "
             "next lesson supplies."),
        ],
        "standard": (
            "Finish when you can compute where a better algorithm overtakes a faster machine.",
            "Given two cost formulas, two constants and two machine speeds, bracket the crossover "
            "between powers of 2 by hand, compute both times at a stated n, and say why no "
            "crossover exists when the orders of growth are equal."
        ),
        "note": (
            "The lab's times are formulas evaluated at n, not measurements of programs; a real "
            "program's constant depends on its compiler, its machine and its memory, which the "
            "RAM model of the next lessons sets aside. The crossover it finds is exact for the "
            "formulas you give. That some crossover exists for every such pair is the chapter's "
            "argument, and it holds whatever the constants."
        ),
    },
    # ---------------------------------------------------------------- 02
    # CLRS section 2.1, pp. 16-22.
    # Quote: p. 18, 13 words, quotes.py OK. Lesson total: 13 words.
    # The sorting problem and keys, pseudocode (pp. 16-17); INSERTION-SORT
    # and the hand of cards (pp. 17-18); the loop invariant and its three
    # properties, the analogy with induction (pp. 18-19); the invariant for
    # insertion sort (pp. 19-20); pseudocode conventions (pp. 20-22).
    {
        "slug": "insertion-sort-and-loop-invariants",
        "title": "Insertion Sort and Loop Invariants",
        "module": "Chapter 2 · Getting Started",
        "one_line": "Insertion sort grows a sorted prefix one key at a time, and a loop invariant with three parts, initialisation, maintenance and termination, proves that it sorts every array.",
        "summary": (
            "Section 2.1 gives the book's first algorithm and its first proof. Insertion sort "
            "takes each key in turn and slides it left past the larger keys already sorted. The "
            "proof states what is true at the start of every pass, shows it is true before the "
            "first, kept by each, and enough at the end. Sort a short array by hand writing the "
            "invariant at each pass, then watch the lab check it pass by pass on arrays of your "
            "own."
        ),
        "key": [
            "pass j inserts A[j] into A[1..j − 1]",
            "A[1..j − 1]: the first j − 1 keys, sorted",
            "initialisation: true before the first pass",
            "maintenance: each pass keeps it true",
            "termination: at j = n + 1, all sorted",
        ],
        "key_label": "Section 2.1 in five lines",
        "concepts_intro": (
            "Three ideas: one algorithm, one tool for proving loops correct, and the property "
            "of the algorithm that the tool is used to show."
        ),
        "concepts": [
            ("Insertion sort",
             "For j from 2 to n, take `key = A[j]`, move each element of the sorted prefix "
             "`A[1..j − 1]` that is larger than key one place right, and drop key into the gap. "
             "It sorts in place: only key is held outside the array."),
            ("Loop invariant",
             "A statement about the variables that is true at the start of every iteration of a "
             "loop. You show it is true before the first iteration (initialisation), that an "
             "iteration that starts with it true ends with it true (maintenance), and that when "
             "the loop stops it gives what you wanted (termination)."),
            ("The sorted prefix",
             "Insertion sort's invariant: at the start of the pass for j, `A[1..j − 1]` holds "
             "exactly the elements that were first in `A[1..j − 1]`, now in sorted order. The "
             "rest of the array, `A[j..n]`, is untouched."),
        ],
        "read_title": "The section's argument first, then the check",
        "read_intro": (
            "Read the opening of Chapter 2 and Section 2.1 in your own copy first. The lesson "
            "sets out the algorithm and its proof in its own words, sorts one array by hand, and "
            "then lets the lab check the invariant at every pass on arrays you choose."
        ),
        "body": [
            ("p", "&ldquo;We use loop invariants to help us understand why an algorithm is "
                  "correct.&rdquo; The authors write it in Section 2.1, a page after giving "
                  "their first algorithm, and the rest of the section shows what that means. "
                  "This lesson reads the opening of Chapter 2 and Section 2.1: the sorting "
                  "problem, insertion sort, the three properties a loop invariant must have, and "
                  "the conventions of the book's pseudocode."),
            ("p", "Chapter 2 opens by promising a framework for the whole book: specify an "
                  "algorithm, argue that it is correct, analyse its running time. Insertion sort "
                  "is the first instance. The numbers being sorted are the <em>keys</em>, they "
                  "arrive in an array `A[1..n]`, and the procedure INSERTION-SORT rearranges "
                  "them within that array, holding at most a constant number outside it at any "
                  "time. The book calls this sorting <em>in place</em>."),
            ("p", "The authors' picture is a hand of playing cards. You pick up cards one at a "
                  "time from a pile on the table and slide each into its place among the cards "
                  "already in your left hand, comparing from right to left. The cards in your "
                  "hand are always sorted, and they are always the cards that were on top of the "
                  "pile. INSERTION-SORT does exactly this: the index j marks the card being "
                  "inserted, `A[1..j − 1]` is the hand, and `A[j + 1..n]` is the pile."),
            ("def", ("Loop invariant",
                     "A property that holds at the start of each iteration of a loop. To use "
                     "one you show three things. <strong>Initialisation</strong>: it holds "
                     "before the first iteration. <strong>Maintenance</strong>: if it holds "
                     "before an iteration, it holds before the next. "
                     "<strong>Termination</strong>: when the loop ends, the invariant, together "
                     "with the reason the loop ended, gives a property that shows the algorithm "
                     "correct.")),
            ("p", "The authors compare the first two parts to mathematical induction: "
                  "initialisation is the base case and maintenance the inductive step. The "
                  "third part is where the analogy stops. An induction runs forever; a loop "
                  "stops, and termination uses the stopping condition. They call it perhaps the "
                  "most important of the three, because it is the part that delivers "
                  "correctness."),
            ("p", "For insertion sort the invariant is that at the start of the pass for j, the "
                  "subarray `A[1..j − 1]` holds the elements that started in positions 1 to "
                  "j − 1, now sorted. Initialisation: at j = 2 the subarray is the single "
                  "element `A[1]`, which is trivially sorted and is the original. Maintenance: "
                  "the pass moves `A[j − 1]`, `A[j − 2]` and so on one place right until it finds "
                  "the place for key, and puts key there, so `A[1..j]` now holds the original "
                  "first j elements in order; increasing j restores the invariant's wording. "
                  "Termination: the loop stops when j exceeds n, that is at j = n + 1, and the "
                  "invariant then says `A[1..n]`, the whole array, holds its original elements in "
                  "sorted order."),
            ("p", "The authors note that a fully formal maintenance step would state a second "
                  "invariant for the inner while loop, and they choose not to. Exercise 2.1-3's "
                  "linear search is the place to try one yourself. The section closes with the "
                  "conventions of the pseudocode: indentation shows block structure, arrays are "
                  "indexed from 1, a loop counter keeps its value after the loop, object "
                  "attributes are written with a dot, parameters are passed by value, and the "
                  "words <em>and</em> and <em>or</em> short-circuit, which is what lets the "
                  "inner test check `i > 0` before it looks at `A[i]`."),
            ("p", "Now the lab, which runs INSERTION-SORT on the array you type and checks the "
                  "invariant at the start of each pass and once more at j = n + 1. The tiles "
                  "count the key comparisons, each a test of `A[i] > key`, and the shifts, each "
                  "an element moved one place right; say whether the invariant held at every "
                  "check; and print the sorted array. The table below them shows each pass: j, "
                  "the key, the prefix before the pass, its comparisons and shifts, and the "
                  "array after."),
            ("p", "The worked example <code>shuffled</code> is the array `[8, 3, 5, 1, 9, 2, 7]`. "
                  "The invariant holds at all 7 checks, from j = 2 to j = 8; the sort makes 15 "
                  "comparisons and 11 shifts. Choose <code>sorted</code>, eight keys already in "
                  "order: 7 comparisons, one a pass, and no shifts at all. Choose "
                  "<code>reversed</code>, the same keys in decreasing order: every key travels to "
                  "the front, 28 comparisons and 28 shifts. Same n, three different amounts of "
                  "work, and the same invariant held throughout each."),
            ("p", "The example <code>repeats</code>, `[4, 2, 4, 1, 2]`, makes 8 comparisons and "
                  "6 shifts and shows one more property. The test is strict, `A[i] > key`, so a "
                  "key stops as soon as it meets an equal one and never passes it; equal keys "
                  "leave in the order they arrived. That is stability, which Chapter 8's radix "
                  "sort depends on, and which the Algorithms Subject's lesson What a Sort Must "
                  "Promise practises further."),
            ("h3", "Exercise"),
            ("p", "Sort `[6, 2, 9, 4, 1, 7]` by hand with INSERTION-SORT. At the start of each "
                  "pass, write j, the key and the array, and check the invariant against the "
                  "original first j − 1 elements. Count the key comparisons and the shifts, then "
                  "type the array into the lab and compare."),
            ("p", "The invariant shows insertion sort is right; it says nothing about how long "
                  "it takes, and the three examples above already disagree about that. The next "
                  "lesson, Analyzing Insertion Sort, turns to the cost."),
        ],
        "lab": ("itakit", {
            "mode": "sorting",
            "view": "insertion",
            "preset": "shuffled",
            "presets": [
                {"id": "shuffled", "label": "Seven keys in a shuffled order",
                 "list": "8 3 5 1 9 2 7",
                 "expect": {"stiComparisons": "15", "stiShifts": "11",
                            "stiInvariant": "holds at all 7 checks, j = 2 to 8",
                            "stiSorted": "1, 2, 3, 5, 7, 8, 9"}},
                {"id": "sorted", "label": "Eight keys already in increasing order",
                 "list": "1 2 3 4 5 6 7 8",
                 "expect": {"stiComparisons": "7", "stiShifts": "0"}},
                {"id": "reversed", "label": "The same eight keys in decreasing order",
                 "list": "8 7 6 5 4 3 2 1",
                 "expect": {"stiComparisons": "28", "stiShifts": "28",
                            "stiInvariant": "holds at all 8 checks, j = 2 to 9"}},
                {"id": "repeats", "label": "Five keys with two pairs of equal keys",
                 "list": "4 2 4 1 2",
                 "expect": {"stiComparisons": "8", "stiShifts": "6",
                            "stiSorted": "1, 2, 2, 4, 4"}},
            ],
            "panel_title": "Insertion sort, pass by pass, with its invariant checked",
            "panel_intro": (
                "Type an array of whole numbers. The lab runs INSERTION-SORT, counts each key "
                "comparison and each shift, and checks at the start of every pass that the prefix "
                "holds the original first j − 1 elements in sorted order."
            ),
        }),
        "steps_title": "Running insertion sort by hand",
        "steps_intro": "Four steps per array, then one array of your own.",
        "steps": [
            ("Mark the hand and the pile",
             "Draw a bar after `A[1]`. Left of the bar is the sorted hand, right of it the pile. "
             "Set j = 2."),
            ("Take the key and slide",
             "Copy `A[j]` aside as key. Moving left from `j − 1`, shift each element larger than "
             "key one place right, counting a comparison for each test and a shift for each move. "
             "Stop at an element not larger than key, or at the front."),
            ("Drop the key and move the bar",
             "Write key in the gap, move the bar one place right, and add 1 to j."),
            ("Check the invariant",
             "Before the next pass, compare the hand with the original first j − 1 elements, "
             "sorted. They must be the same list. At j = n + 1 the hand is the whole array."),
            ("Sort an array of your own",
             "Write eight whole numbers with at least one repeat, sort them by hand counting "
             "comparisons and shifts, then type them into the lab and check both counts and that "
             "the equal keys kept their order."),
        ],
        "worked": {
            "title": "Seven keys, six passes",
            "intro": [
                "Sort `[8, 3, 5, 1, 9, 2, 7]`, the lab's example <code>shuffled</code>. Each line "
                "is one pass: the key, what it passes, and the comparisons and shifts.",
            ],
            "lines": [
                "j = 2, key 3: passes 8; 1 comp, 1 shift",
                "j = 3, key 5: passes 8, stops at 3; 2, 1",
                "j = 4, key 1: passes 8, 5, 3; 3, 3",
                "j = 5, key 9: stops at 8; 1, 0",
                "j = 6, key 2: passes 9, 8, 5, 3; 5, 4",
                "j = 7, key 7: passes 9, 8; 3, 2",
                "15 comparisons, 11 shifts",
            ],
            "after": [
                "At j = 2 and j = 4 the key reached the front, so its pass made no comparison "
                "with a 0th element: the loop stopped on `i > 0` instead. At j = 8 the invariant "
                "says the prefix `A[1..7]` is the original seven keys sorted, `[1, 2, 3, 5, 7, 8, "
                "9]`, which is the whole array.",
            ],
        },
        "quiz_title": "Insertion sort and its invariant",
        "quiz": [
            {"q": "Sort the exercise array `[6, 2, 9, 4, 1, 7]` with INSERTION-SORT. How many "
                  "key comparisons (tests of `A[i] > key`) and shifts does it make?",
             "a": ["11 comparisons, 8 shifts", "13 comparisons, 8 shifts",
                   "8 comparisons, 8 shifts", "15 comparisons, 11 shifts"],
             "c": 0,
             "why": "The passes make 1, 1, 3, 4 and 2 comparisons and 1, 0, 2, 4 and 1 shifts: "
                    "11 and 8. Thirteen counts every run of the while test, including the two "
                    "times it stops on `i > 0` without comparing (keys 2 and 1 reach the front); "
                    "that is the next lesson's Σt_j, not the key comparisons. Eight comparisons "
                    "would mean no pass ever stopped at a smaller key, but keys 9, 4 and 7 each "
                    "do. Fifteen is n(n − 1)/2, the worst case for six keys, and 15 and 11 are "
                    "the lesson's shuffled example."},
            {"q": "In the example <code>repeats</code>, `[4, 2, 4, 1, 2]`, call the two 4s "
                  "4a (first) and 4b. Where do they end, and why?",
             "a": ["4a before 4b, because a key never moves past an element equal to it",
                   "4b before 4a, because the later key is inserted to the left of equal keys",
                   "Either order, depending on the 1 and 2s between them",
                   "4a before 4b, because insertion sort never moves a key that is already in "
                   "its final position"],
             "c": 0,
             "why": "The inner test is `A[i] > key`; when 4b is the key it meets 4a, the test "
                    "fails, and 4b stays to its right. Every later shift moves both 4s together, "
                    "so the order never changes. Inserting to the left of equal keys would need "
                    "the test `A[i] ≥ key`. The smaller keys do not affect it. The last answer has "
                    "the right order for a wrong reason: neither 4 starts in its final place (4a is "
                    "shifted right three times, 4b twice), so the rule it cites never applies."},
            {"q": "Suppose the invariant were weakened to: at the start of each pass, "
                  "`A[1..j − 1]` is in sorted order. Which part of the proof is no longer enough?",
             "a": ["Initialisation, because one element might not count as sorted",
                   "Termination, because a sorted array of the wrong elements would satisfy it",
                   "Maintenance, because a pass might unsort the prefix",
                   "None: sorted order is all that the problem asks for"],
             "c": 1,
             "why": "At j = n + 1 the weak invariant says only that the array is sorted. A "
                    "procedure that overwrote every element with 0 would satisfy it, so it no "
                    "longer shows the output is a permutation of the input, which the sorting "
                    "problem requires. A single element is sorted, so initialisation is fine; "
                    "each pass keeps the prefix sorted, so maintenance still holds. The problem "
                    "asks for a sorted permutation of the input, not any sorted array."},
            {"q": "Which part of the invariant argument uses the condition that ends the loop?",
             "a": ["Initialisation", "Maintenance", "Termination",
                   "None of them; the exit condition is used only in the running-time analysis"],
             "c": 2,
             "why": "Termination combines the invariant with the reason the loop stopped: j "
                    "exceeds n, so j = n + 1, and substituting it gives the whole array sorted. "
                    "Initialisation looks only at the state before the first test, and "
                    "maintenance at one iteration in the middle. The exit condition is what turns "
                    "the invariant into the correctness claim, so it belongs to the proof."},
        ],
        "mistakes": [
            ("Expecting the invariant to hold at every moment inside the loop",
             "The invariant is a claim about the start of each iteration. Halfway through a pass "
             "the prefix holds a duplicate, the element just shifted, and key is in no array "
             "slot at all, so the claim is false there and true again once key is dropped into "
             "its place. The lab checks it only at the start of each pass and at j = n + 1, "
             "which is exactly where the book states it."),
            ("Dropping the clause about the original elements",
             "An invariant that says only that `A[1..j − 1]` is sorted is maintained by insertion "
             "sort, but it is also maintained by a procedure that writes zeros. Termination then "
             "proves nothing useful. The clause about the elements that started in "
             "those positions is what makes the final array a sorted "
             "permutation of the input."),
            ("Taking a check on examples for a proof",
             "The lab checks the invariant on the arrays you type, and on the lesson's four it "
             "holds at every check. That is evidence about those four arrays. The maintenance "
             "argument is about any array at any pass, and it is that argument, not the checks, "
             "that makes insertion sort correct."),
        ],
        "standard": (
            "Finish when you can prove a simple loop correct with an invariant.",
            "Given a short loop, state its invariant, show initialisation, maintenance and "
            "termination, and run insertion sort by hand on six to eight keys with the invariant "
            "written at every pass."
        ),
        "note": (
            "The lab checks the invariant by comparing the prefix with the sorted original "
            "prefix at each pass; it is a check on the array you typed, not a proof. Its counts "
            "are key comparisons and shifts, which differ from the number of times the while "
            "test runs whenever a key reaches the front; the next lesson counts those too."
        ),
    },
    # ---------------------------------------------------------------- 03
    # CLRS section 2.2, pp. 23-29.
    # Quote: p. 23, 14 words, quotes.py OK. Lesson total: 14 words.
    # The RAM model, its instructions, word size and gray areas (pp. 23-24);
    # input size and running time, line costs c_i (pp. 24-25); the cost and
    # times table, t_j, best and worst case (pp. 25-27); worst-case and
    # average-case analysis, three reasons (pp. 27-28); order of growth
    # (pp. 28-29).
    {
        "slug": "analyzing-insertion-sort",
        "title": "Analyzing Insertion Sort",
        "module": "Chapter 2 · Getting Started",
        "one_line": "Charge each line of insertion sort a constant per execution, count how often each line runs, and the running time is linear on a sorted array, quadratic on a reversed one, and Θ(n²) in the worst case.",
        "summary": (
            "Section 2.2 fixes a model of computation, the RAM, and analyses insertion sort in "
            "it line by line. The count turns on t_j, the number of times the inner loop's test "
            "runs in pass j: one in the best case, j in the worst. Keeping only the leading term "
            "gives the order of growth. Count t_j by hand for a short array, then let the lab add "
            "up every line on arrays of your own and set the best and worst cases beside them."
        ),
        "key": [
            "RAM: one processor, constant-time steps",
            "line i costs c_i each time it runs",
            "t_j: runs of the inner test in pass j",
            "best: t_j = 1, time a·n + b",
            "worst: t_j = j, time a·n² + b·n + c",
            "keep the leading term: Θ(n²)",
        ],
        "key_label": "Section 2.2 in six lines",
        "concepts_intro": (
            "Three ideas that every later analysis in the book reuses: a machine to count on, a "
            "quantity to count, and a way to forget what does not matter."
        ),
        "concepts": [
            ("The RAM model",
             "A generic one-processor machine that executes one instruction after another. "
             "Arithmetic, data movement and control instructions each take constant time, words "
             "hold about `c·lg n` bits for a constant c, and caches and virtual memory are not "
             "modelled."),
            ("Running time on an input",
             "The number of primitive steps executed on that input, as a function of the input's "
             "size. Charging line i a constant `c_i` each time it runs makes the running time a "
             "sum of cost times count over the lines."),
            ("Order of growth",
             "The leading term of the running time with its coefficient dropped. Insertion "
             "sort's worst case `a·n² + b·n + c` has order of growth `n²`, written `Θ(n²)`, a "
             "notation the next chapter makes precise."),
        ],
        "read_title": "The section's argument first, then the count",
        "read_intro": (
            "Read Section 2.2 in your own copy first, with its table of costs and times open. "
            "The lesson sets out the model and the count in its own words, counts one array by "
            "hand, and then lets the lab add up the lines on arrays you choose."
        ),
        "body": [
            ("p", "&ldquo;Analyzing an algorithm has come to mean predicting the resources that "
                  "the algorithm requires.&rdquo; Section 2.2 opens with that sentence and spends "
                  "the rest of its pages making the prediction precise for insertion sort. Memory, "
                  "bandwidth or hardware sometimes matter most, the authors say, but most often "
                  "the resource is time. This lesson reads the section: the model of computation, "
                  "the line-by-line count, the best and worst cases, and the order of growth."),
            ("p", "To count steps you need a machine to count them on. The book's is the "
                  "random-access machine, the RAM: one processor, instructions executed one after "
                  "another, and the instructions real computers have, arithmetic, loading and "
                  "storing, branching and calling, each taking constant time. A RAM with a sort "
                  "instruction would sort in one step, which is why the authors take real "
                  "computers as their guide. Words hold about `c·lg n` bits for a constant `c ≥ 1`, "
                  "enough to index the input but not so many that one word could carry it all."),
            ("p", "The authors admit gray areas. Raising a number to a power is not one "
                  "instruction in general, but computing `2ᵏ` is, by shifting 1 left k places, as "
                  "long as k fits in a word. The model leaves out caches and virtual memory; "
                  "models that include them are much harder to work with, and the authors judge "
                  "RAM analyses to be usually excellent predictors of real performance. Input "
                  "size depends on the problem: the number of items for sorting, the number of "
                  "bits for multiplying integers, two numbers, vertices and edges, for a graph."),
            ("def", ("t_j",
                     "For each j from 2 to n, `t_j` is the number of times the inner while "
                     "loop's test runs in the pass that inserts `A[j]`. A loop's test runs once "
                     "more than its body, so `t_j` is the number of shifts in that pass plus "
                     "one, whether the loop stopped at a smaller key or at the front of the "
                     "array.")),
            ("p", "With each line i charged `c_i` per execution, the running time is the sum of "
                  "cost times count over the lines of INSERTION-SORT. The loop header runs n "
                  "times, counting the final failing test; the three lines that set up and finish "
                  "each pass run n − 1 times; the while test runs `Σ t_j` times; and the two lines "
                  "of its body run `Σ (t_j − 1)` times each, with every sum over j from 2 to n. The "
                  "comment line costs nothing. The book writes this sum out with all seven "
                  "constants; the lab uses the same sum with every `c_i` equal to 1."),
            ("math", [
                "the line-cost sum with every c_i = 1",
                "",
                "lines executed = n + 3·(n − 1) + Σt_j + 2·Σ(t_j − 1)",
                "best,  t_j = 1:  5n − 4",
                "worst, t_j = j:  (3n² + 7n − 8)/2",
            ]),
            ("p", "The best case is an array already sorted: every test fails at once, "
                  "`t_j = 1`, and the time is `a·n + b` for constants depending on the `c_i`, a "
                  "linear function. The worst case is an array in decreasing order: each key "
                  "is compared with every element of the prefix, `t_j = j`, and with the sums "
                  "of Appendix A the time is `a·n² + b·n + c`, a quadratic. Same algorithm, same "
                  "n, two different functions."),
            ("p", "Which one should an analysis report? The book usually reports the worst case, "
                  "for three reasons. It is an upper bound on the time for every input of that "
                  "size, a guarantee. For some algorithms it happens often, as when a search looks "
                  "for something absent. And the average case is often about as bad: on random "
                  "input a key passes about half the prefix, `t_j` is about j/2, and the time is "
                  "still quadratic. Average-case and randomized analyses return in Chapter 5."),
            ("p", "The last step is one more abstraction. Constants and lower-order terms matter "
                  "less than the rate of growth for large inputs, so the analysis keeps only the "
                  "leading term, `a·n²`, drops its coefficient, and describes insertion sort's "
                  "worst case as `Θ(n²)`. One algorithm is then counted more "
                  "efficient than another if its worst case has a lower order of growth, with the "
                  "warning from Chapter 1 that this is a statement about large enough inputs."),
            ("p", "Now the lab, which runs INSERTION-SORT on your array and counts. The tiles are "
                  "the list of `t_j`, their sum, the key comparisons, the shifts, the best-case "
                  "and worst-case comparisons for your n, and the lines executed with every "
                  "`c_i = 1`, beside the best and worst values of that sum. The shifts equal the "
                  "inversions of the array, the pairs of positions whose keys are out of order, "
                  "which is the subject of the book's Problem 2-4."),
            ("p", "The worked example <code>eight</code> is `[6, 1, 8, 3, 7, 2, 5, 4]`. Its "
                  "`t_j` are 2, 1, 3, 2, 5, 4 and 5, summing to 22; there are 21 key comparisons "
                  "and 15 shifts; and 81 lines run, between the best case of 36 and the worst of "
                  "120. Choose <code>sorted</code> and the lines are 36, exactly `5n − 4`; choose "
                  "<code>reversed</code> and they are 120, exactly `(3n² + 7n − 8)/2`. The "
                  "formulas are not estimates; they are the counts on those two arrays."),
            ("p", "Choose <code>nearly-sorted</code>, `[1, 2, 3, 5, 4, 6, 8, 7]`, two adjacent "
                  "pairs swapped: `Σ t_j` is 9, the shifts are 2, and 42 lines run, close to the "
                  "best case. Insertion sort's cost tracks how unsorted its input is, which is "
                  "why it is used on small or nearly sorted arrays. Then choose "
                  "<code>reversed-thirty</code>, thirty keys in decreasing order: 435 comparisons "
                  "and 1,451 lines, against 146 lines had they arrived sorted. Thirty keys is "
                  "small, and the quadratic term already does most of the work."),
            ("h3", "Exercise"),
            ("p", "For the array `[5, 9, 2, 6, 3]`, write down `t_j` for j = 2 to 5 by hand. "
                  "Then evaluate the line-cost sum with every `c_i = 1`, and compare with the "
                  "lab's lines tile."),
            ("p", "Insertion sort is quadratic in the worst case because it is incremental: it "
                  "grows the sorted part one key at a time. The next lesson, Merge Sort and "
                  "Divide-and-Conquer, tries a different design and gets a different order of "
                  "growth."),
        ],
        "lab": ("itakit", {
            "mode": "sorting",
            "view": "cost",
            "preset": "eight",
            "presets": [
                {"id": "eight", "label": "Eight keys in a shuffled order",
                 "list": "6 1 8 3 7 2 5 4",
                 "expect": {"stiTj": "2, 1, 3, 2, 5, 4, 5", "stiSumTj": "22",
                            "stiComparisons": "21", "stiShifts": "15",
                            "stiLines": "81 (best 5n − 4 = 36, worst (3n² + 7n − 8)/2 = 120)"}},
                {"id": "sorted", "label": "Eight keys already sorted",
                 "list": "1 2 3 4 5 6 7 8",
                 "expect": {"stiTj": "1, 1, 1, 1, 1, 1, 1", "stiShifts": "0",
                            "stiLines": "36 (best 5n − 4 = 36, worst (3n² + 7n − 8)/2 = 120)"}},
                {"id": "reversed", "label": "Eight keys in decreasing order",
                 "list": "8 7 6 5 4 3 2 1",
                 "expect": {"stiTj": "2, 3, 4, 5, 6, 7, 8", "stiSumTj": "35",
                            "stiComparisons": "28", "stiShifts": "28",
                            "stiLines": "120 (best 5n − 4 = 36, worst (3n² + 7n − 8)/2 = 120)"}},
                {"id": "nearly-sorted", "label": "Eight keys with two adjacent pairs swapped",
                 "list": "1 2 3 5 4 6 8 7",
                 "expect": {"stiSumTj": "9", "stiShifts": "2",
                            "stiLines": "42 (best 5n − 4 = 36, worst (3n² + 7n − 8)/2 = 120)"}},
                {"id": "reversed-thirty", "label": "Thirty keys in decreasing order",
                 "list": "30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1",
                 "expect": {"stiComparisons": "435",
                            "stiLines": "1,451 (best 5n − 4 = 146, worst (3n² + 7n − 8)/2 = 1,451)"}},
            ],
            "panel_title": "Add up insertion sort's lines",
            "panel_intro": (
                "Type an array of whole numbers. The lab runs INSERTION-SORT, records t_j for "
                "each pass, and evaluates the book's line-cost sum with every line costing 1, "
                "beside the best and worst cases for the same n."
            ),
        }),
        "steps_title": "Counting insertion sort's lines by hand",
        "steps_intro": "Four steps for one array, then one array of your own.",
        "steps": [
            ("Run the sort and record t_j",
             "For each pass, count the shifts and add 1. That is `t_j`, the runs of the inner "
             "test, including the one that fails or finds i = 0."),
            ("Add the sums",
             "Compute `Σ t_j` and `Σ (t_j − 1)`. The second is the number of shifts."),
            ("Evaluate the line-cost sum",
             "With every `c_i = 1`, the lines executed are `n + 3·(n − 1) + Σ t_j + "
             "2·Σ (t_j − 1)`."),
            ("Place it between the cases",
             "Compute `5n − 4` and `(3n² + 7n − 8)/2` for your n. Your total must lie between "
             "them, at the bottom only for a sorted array and at the top only for a reversed one."),
            ("Count an array of your own",
             "Write ten distinct keys with exactly three inversions, predict `Σ t_j` (it is "
             "n − 1 plus the inversions) and the lines, then check both in the lab."),
        ],
        "worked": {
            "title": "Eight keys, line by line",
            "intro": [
                "Count insertion sort on `[6, 1, 8, 3, 7, 2, 5, 4]`, the lab's example "
                "<code>eight</code>. Each line gives a pass, its key, its shifts and its `t_j`.",
            ],
            "lines": [
                "j = 2, key 1: 1 shift, t = 2",
                "j = 3, key 8: 0 shifts, t = 1",
                "j = 4, key 3: 2 shifts, t = 3",
                "j = 5, key 7: 1 shift, t = 2",
                "j = 6, key 2: 4 shifts, t = 5",
                "j = 7, key 5: 3 shifts, t = 4",
                "j = 8, key 4: 4 shifts, t = 5",
                "Σt = 22, shifts 15: 8 + 21 + 22 + 30 = 81",
            ],
            "after": [
                "The four terms are n = 8, `3·(n − 1) = 21`, `Σ t_j = 22` and `2·Σ (t_j − 1) = "
                "30`. Only key 1 reached the front, so the key comparisons are 22 − 1 = 21. The "
                "15 shifts are the array's 15 inversions.",
            ],
        },
        "quiz_title": "The RAM model and the line-cost sum",
        "quiz": [
            {"q": "For the exercise array `[5, 9, 2, 6, 3]`, what are the `t_j` for j = 2 to 5, "
                  "and how many lines run with every `c_i = 1`?",
             "a": ["t = 1, 3, 2, 4; 39 lines", "t = 0, 2, 1, 3; 27 lines",
                   "t = 1, 2, 2, 4; 36 lines", "t = 1, 3, 2, 4; 51 lines"],
             "c": 0,
             "why": "The passes make 0, 2, 1 and 3 shifts, so `t_j` is one more: 1, 3, 2 and 4, "
                    "summing to 10. The lines are `5 + 12 + 10 + 2·6 = 39`. The list 0, 2, 1, 3 "
                    "is the shifts, not the test runs. The list 1, 2, 2, 4 counts key "
                    "comparisons, which miss the test that stops at i = 0 when key 2 reaches the "
                    "front. Fifty-one is the worst case for n = 5, which this array is not."},
            {"q": "INSERTION-SORT makes exactly n − 1 = 7 key comparisons on an array of 8 "
                  "distinct keys. What follows?",
             "a": ["The array was already sorted",
                   "Every pass made exactly one key comparison, so at most the first two keys "
                   "were out of order",
                   "No shift was made",
                   "Σ t_j = 7"],
             "c": 1,
             "why": "Each pass makes at least one comparison, so 7 means one in each. A pass "
                    "with one comparison either stops at once or, at j = 2 only, shifts `A[1]` "
                    "and reaches the front. So `[2, 1, 3, 4, 5, 6, 7, 8]` also makes 7 comparisons, "
                    "with 1 shift and `Σ t_j = 8`; the array need not have been sorted, and the "
                    "other two answers fail on the same array."},
            {"q": "Why does the book usually concentrate on the worst-case running time?",
             "a": ["Because the worst case is the input an algorithm meets most often",
                   "Because it bounds the running time on every input of that size",
                   "Because the average case always equals the worst case",
                   "Because the best case is linear for every sorting algorithm"],
             "c": 1,
             "why": "The first of Section 2.2's three reasons is that the worst case is an upper "
                    "bound for any input of the size, a guarantee. The authors say the worst case "
                    "occurs fairly often for some algorithms, not that it is the most common "
                    "input; and that the average is often roughly as bad, not equal (for "
                    "insertion sort it is about half). No claim about every sort's best case is "
                    "made, and merge sort's best case is not linear."},
            {"q": "Which of these does the RAM model of Section 2.2 treat as one constant-time "
                  "instruction?",
             "a": ["Computing 2ᵏ by shifting 1 left k places, for k no more than the word size",
                   "Raising a real number x to a real power y",
                   "Sorting an array held in memory",
                   "Loading a word, at a cost that depends on whether it is in the cache"],
             "c": 0,
             "why": "The authors treat `2ᵏ` as constant time when k fits in a word, because real "
                    "machines shift in one instruction. General exponentiation takes several "
                    "instructions. A sort instruction is their example of what would make the "
                    "model unrealistic. And the model has no cache: every load costs the same "
                    "constant."},
        ],
        "mistakes": [
            ("Reading insertion sort's Θ(n²) as its time on every input",
             "The `Θ(n²)` is the order of growth of the worst case. On a sorted array every "
             "test fails at once and the time is linear, `a·n + b`. On the lesson's eight keys the "
             "line count runs from 36 for the sorted array to 120 for the reversed one, and a "
             "nearly sorted array costs 42. The next chapter gives the precise words: the running "
             "time is `O(n²)` and `Ω(n)`, and over all inputs it is neither `Θ(n²)` nor `Θ(n)`."),
            ("Taking t_j for the number of comparisons or shifts",
             "`t_j` counts the runs of the inner test, which is one more than the shifts in that "
             "pass. It equals the key comparisons except when the key reaches the front, where "
             "the test stops on `i > 0` without comparing. The difference is small, but every "
             "line count in the analysis depends on getting it right."),
            ("Treating the line costs as known",
             "The constants `c_i` stand for costs the analysis does not know and does not need. "
             "Setting them all to 1, as the lab does, counts executed lines, not seconds; and the "
             "order of growth comes out the same whatever positive values they take, which is "
             "why the book drops them."),
        ],
        "standard": (
            "Finish when you can carry out the line-cost analysis of a short procedure.",
            "Given an array, record insertion sort's t_j and evaluate the line-cost sum; given a "
            "procedure with nested loops, write its best and worst cases and their orders of "
            "growth."
        ),
        "note": (
            "The lab counts executed lines with every cost equal to 1, which is the book's sum "
            "under one choice of constants, not a running time in seconds. Its best and worst "
            "figures are exact for your n; the order of growth they share with every choice of "
            "constants is the analysis, which the lab cannot carry out for you."
        ),
    },
    # ---------------------------------------------------------------- 04
    # CLRS section 2.3, pp. 29-42.
    # Quote: p. 30, 19 words, quotes.py OK. Lesson total: 19 words.
    # Incremental vs divide-and-conquer (p. 29); the three steps and merge
    # sort's (p. 30); MERGE, sentinels, its loop invariant (pp. 30-34);
    # MERGE-SORT and q (p. 34); recurrences for divide-and-conquer
    # (pp. 34-35); merge sort's recurrence and the recursion tree
    # (pp. 35-37); Problem 2-1 named.
    {
        "slug": "merge-sort-and-divide-and-conquer",
        "title": "Merge Sort and Divide-and-Conquer",
        "module": "Chapter 2 · Getting Started",
        "one_line": "Merge sort splits the array in half, sorts each half recursively and merges them in linear time, and its recurrence T(n) = 2T(n/2) + Θ(n) has a recursion tree of lg n + 1 levels each costing a constant times n.",
        "summary": (
            "Section 2.3 introduces divide-and-conquer through merge sort. MERGE combines two "
            "sorted runs in linear time and is proved correct by its own loop invariant; "
            "MERGE-SORT halves, recurses and merges. Its running time obeys a recurrence, and "
            "the recursion tree shows why the answer is Θ(n lg n). Merge eight keys by hand "
            "level by level, then count merge sort's comparisons per level in the lab."
        ),
        "key": [
            "divide, conquer, combine",
            "MERGE of n elements takes Θ(n)",
            "split at q = ⌊(p + r)/2⌋",
            "T(n) = 2T(n/2) + Θ(n)",
            "lg n + 1 levels, each costing c·n",
            "so merge sort is Θ(n lg n)",
        ],
        "key_label": "Section 2.3 in six lines",
        "concepts_intro": (
            "Three ideas: a design method, the procedure that does merge sort's real work, and "
            "the equation that describes the cost of any algorithm built by the method."
        ),
        "concepts": [
            ("Divide-and-conquer",
             "Divide the problem into smaller instances of the same problem, conquer them by "
             "solving them recursively (or directly when they are small enough), and combine "
             "their solutions into a solution of the original."),
            ("Merging",
             "MERGE takes two adjacent sorted subarrays `A[p..q]` and `A[q + 1..r]` and makes "
             "`A[p..r]` sorted by repeatedly moving the smaller front element into place. Each "
             "move is constant work, so merging n elements costs `Θ(n)`."),
            ("Recurrence",
             "An equation that expresses the cost at size n through the costs at smaller "
             "sizes. A divide-and-conquer algorithm making a "
             "subproblems of size n/b has `T(n) = a·T(n/b) + D(n) + C(n)`, with D and C the costs "
             "of dividing and combining."),
        ],
        "read_title": "The section's argument first, then the count",
        "read_intro": (
            "Read Section 2.3 in your own copy first. The lesson sets out the method, the merge "
            "and its invariant, and the recursion tree in its own words, merges one array by "
            "hand, and then counts merge sort's comparisons level by level in the lab."
        ),
        "body": [
            ("p", "&ldquo;The key operation of the merge sort algorithm is the merging of two "
                  "sorted sequences in the &lsquo;combine&rsquo; step.&rdquo; Section 2.3 builds "
                  "merge sort around that operation and uses it to introduce the design method "
                  "the book returns to in Chapter 4. This lesson reads the section: "
                  "divide-and-conquer, MERGE and its invariant, MERGE-SORT, and the recurrence "
                  "that prices it."),
            ("p", "Insertion sort was incremental: having sorted `A[1..j − 1]`, it inserted one "
                  "more element. Divide-and-conquer works differently. Many useful algorithms "
                  "are recursive, calling themselves on closely related smaller problems, and "
                  "they follow three steps at each level: divide the problem into subproblems, "
                  "conquer the subproblems recursively, and combine their solutions. For merge "
                  "sort, divide the n elements into two halves, sort each half by merge sort, and "
                  "merge the two sorted halves. The recursion bottoms out at one element, which is "
                  "already sorted."),
            ("p", "MERGE is described with two face-up piles of cards, each sorted with its "
                  "smallest card on top. The basic step takes the smaller of the two top cards and "
                  "puts it face down on an output pile; when one pile is empty, the other is moved "
                  "over whole. The book's procedure adds a twist: a sentinel card holding ∞ at the "
                  "bottom of each pile, so that no step ever needs to ask whether a pile is empty, "
                  "and the loop simply runs `r − p + 1` times. Copying the halves out and running "
                  "the loop both take time linear in n, so MERGE is `Θ(n)`."),
            ("p", "MERGE is proved correct by an invariant, in the same three steps as insertion "
                  "sort. At the start of each iteration of its main loop, `A[p..k − 1]` holds the "
                  "`k − p` smallest elements of the two copied halves, in sorted order, and the "
                  "current front elements of the two halves are the smallest not yet copied back. "
                  "It holds at the start because the output is empty; each iteration copies the "
                  "smaller front, which is the smallest element left, so it is maintained; and at "
                  "termination `k = r + 1`, so `A[p..r]` holds all but the two largest elements of "
                  "the copies, and those two are the sentinels."),
            ("p", "MERGE-SORT on `A[p..r]` does nothing if the subarray has at most one element. "
                  "Otherwise it computes `q = ⌊(p + r)/2⌋`, sorts `A[p..q]`, which has `⌈n/2⌉` "
                  "elements, and `A[q + 1..r]`, which has `⌊n/2⌋`, and merges them. Seen from "
                  "the bottom, it merges pairs of single elements into runs of two, pairs of runs "
                  "of two into runs of four, and so on, until two runs of about n/2 become the "
                  "sorted array."),
            ("thm", ("Merge sort's recurrence",
                     "Dividing costs `Θ(1)`, conquering costs `2T(n/2)` and merging costs "
                     "`Θ(n)`, so `T(n) = 2T(n/2) + Θ(n)` for n > 1 and `T(1) = Θ(1)`. Written "
                     "with one constant c, each level of the recursion tree costs `c·n`: level i has "
                     "`2ⁱ` nodes of cost `c·(n/2ⁱ)`. For n a power of 2 there are `lg n + 1` "
                     "levels, so `T(n) = c·n·lg n + c·n = Θ(n lg n)`.")),
            ("p", "The recursion tree is the section's real tool. Expand `T(n)` into a root of "
                  "cost `c·n` with two children `T(n/2)`, expand each of those, and continue until "
                  "the subproblems have size 1. Adding across a level gives `c·n` every time, because "
                  "the number of nodes doubles as their size halves. The authors justify the "
                  "count of `lg n + 1` levels by a short induction on the powers of 2, and they "
                  "assume n a power of 2 only for convenience; Chapter 4 shows the order of growth "
                  "is the same for every n."),
            ("math", [
                "counting merge comparisons instead of time, n = 8",
                "",
                "a merge of m elements: at most m − 1 comparisons",
                "level 3: four merges of 2   at most 4 · 1 = 4",
                "level 2: two merges of 4    at most 2 · 3 = 6",
                "level 1: one merge of 8     at most 1 · 7 = 7",
                "                            worst case 17 = n·⌈lg n⌉ − 2^⌈lg n⌉ + 1",
            ]),
            ("p", "Now the lab, which runs MERGE-SORT with the book's split and counts comparisons "
                  "by level, level 1 being the final merge. Its merge stops comparing as soon as one "
                  "half runs out, so a merge of m elements makes at most `m − 1` comparisons; the "
                  "book's MERGE with sentinels makes exactly m, and the lab prints that count too. "
                  "The tiles are the number of levels beside `⌈lg n⌉`, the comparisons at each "
                  "level, their total, the worst case for your n, the sentinel count, and the "
                  "sorted array."),
            ("p", "The worked example <code>eight</code> is `[6, 1, 8, 3, 7, 2, 5, 4]`, the "
                  "array of the last lesson. Merge sort makes 4, 6 and 7 comparisons on levels 3, "
                  "2 and 1, which is 17, exactly the worst case for n = 8; the sentinel version "
                  "makes 24, which is `n·lg n`. Insertion sort made 21 key comparisons on this "
                  "array. Choose <code>sorted</code> and the count falls to 12, four a level, "
                  "because in every merge one half runs out without interleaving; "
                  "<code>reversed</code> gives 12 too. Merge sort's count moves only between 12 "
                  "and 17 at n = 8, where insertion sort's moved between 7 and 28."),
            ("p", "Two more examples have n not a power of 2. In <code>shuffled</code>, the seven "
                  "keys of the insertion-sort lesson, the levels make 6, 5 and 3 comparisons, 14 "
                  "in all, again the worst case for its n. In <code>twelve</code> there are 4 "
                  "levels, `⌈lg 12⌉`, making 11, 9, 7 and 4 comparisons, 31 against a worst case "
                  "of 33, and the sentinels make 44. The algorithm never needed n to be a power of "
                  "2; only the tidy analysis did."),
            ("p", "Merge sort's `Θ(n lg n)` beats insertion sort's `Θ(n²)` for large n, and "
                  "insertion sort wins on small arrays, as the first lesson computed. The book's "
                  "Problem 2-1 combines them, sorting short runs by insertion sort inside merge "
                  "sort, and the Algorithms Subject's lesson k-Way Merging and Sorting in Practice "
                  "chooses such a cutoff from a measured crossover."),
            ("h3", "Exercise"),
            ("p", "Run MERGE-SORT by hand on `[2, 4, 9, 7, 1, 3, 8, 6]`. Write the runs after "
                  "each level of merging and the comparisons each merge makes, stopping each merge "
                  "when one run is used up. Total them, compare with the worst case for n = 8, and "
                  "check in the lab."),
            ("p", "The recurrence was solved here by drawing its tree. The next lesson, "
                  "Asymptotic Notation, makes precise the Θ that both sorts have been described "
                  "with, and Chapter 4 returns to recurrences with three general methods."),
        ],
        "lab": ("itakit", {
            "mode": "sorting",
            "view": "merge",
            "preset": "eight",
            "presets": [
                {"id": "eight", "label": "Eight keys in a shuffled order",
                 "list": "6 1 8 3 7 2 5 4",
                 "expect": {"stiLevels": "3 (⌈lg n⌉ = 3)",
                            "stiPerLevel": "level 1: 7; level 2: 6; level 3: 4",
                            "stiMergeTotal": "17",
                            "stiMergeBound": "n⌈lg n⌉ − 2^⌈lg n⌉ + 1 = 17",
                            "stiSentinel": "24"}},
                {"id": "sorted", "label": "Eight keys already sorted",
                 "list": "1 2 3 4 5 6 7 8",
                 "expect": {"stiPerLevel": "level 1: 4; level 2: 4; level 3: 4",
                            "stiMergeTotal": "12"}},
                {"id": "reversed", "label": "Eight keys in decreasing order",
                 "list": "8 7 6 5 4 3 2 1",
                 "expect": {"stiMergeTotal": "12", "stiSentinel": "24"}},
                {"id": "shuffled", "label": "Seven keys in a shuffled order",
                 "list": "8 3 5 1 9 2 7",
                 "expect": {"stiPerLevel": "level 1: 6; level 2: 5; level 3: 3",
                            "stiMergeTotal": "14",
                            "stiMergeBound": "n⌈lg n⌉ − 2^⌈lg n⌉ + 1 = 14"}},
                {"id": "twelve", "label": "Twelve keys in a shuffled order",
                 "list": "12 4 9 1 7 3 11 6 2 10 5 8",
                 "expect": {"stiLevels": "4 (⌈lg n⌉ = 4)",
                            "stiPerLevel": "level 1: 11; level 2: 9; level 3: 7; level 4: 4",
                            "stiMergeTotal": "31",
                            "stiMergeBound": "n⌈lg n⌉ − 2^⌈lg n⌉ + 1 = 33",
                            "stiSentinel": "44"}},
            ],
            "panel_title": "Merge sort's comparisons, level by level",
            "panel_intro": (
                "Type an array of whole numbers. The lab runs MERGE-SORT with the book's split, "
                "counts the comparisons each level of merging makes, and sets the total beside the "
                "worst case for your n and beside the count the sentinel version of MERGE makes."
            ),
        }),
        "steps_title": "Running merge sort by hand",
        "steps_intro": "Four steps for one array, then one of your own.",
        "steps": [
            ("Draw the splits",
             "Split the array at `q = ⌊(p + r)/2⌋`, then split each half the same way, until "
             "every piece has one element. The left piece gets the extra element when the length "
             "is odd."),
            ("Merge from the bottom",
             "Merge sibling pieces in pairs, from the lowest level up. In each merge, compare the "
             "two front elements, move the smaller (the left one on a tie), and repeat."),
            ("Count each merge's comparisons",
             "Stop counting when one run is used up and copy the rest across free. A merge of m "
             "elements makes between `min` of the two run lengths and `m − 1` comparisons."),
            ("Total by level",
             "Add the comparisons on each level and over all levels, and compare the total with "
             "`n·⌈lg n⌉ − 2^⌈lg n⌉ + 1`."),
            ("Find a worst case of your own",
             "Write eight keys arranged so that every merge interleaves its two runs to the end, "
             "predict 17 comparisons, and check in the lab."),
        ],
        "worked": {
            "title": "An array that interleaves at every merge",
            "intro": [
                "Sort `[1, 5, 3, 7, 2, 6, 4, 8]`. Every merge alternates between its runs until "
                "the last element, so it shows the worst case being reached.",
            ],
            "lines": [
                "level 3: 1|5 3|7 2|6 4|8: 4 merges, 4",
                "level 2: 1 5 + 3 7 → 1 3 5 7: 3",
                "         2 6 + 4 8 → 2 4 6 8: 3",
                "level 1: 1 3 5 7 + 2 4 6 8: 7",
                "total 4 + 6 + 7 = 17, the worst case",
                "with sentinels: 8 + 8 + 8 = 24",
            ],
            "after": [
                "Each merge of m elements made `m − 1` comparisons because neither run ran out "
                "before the other's last element. Type the array into the lab to see the same "
                "4, 6 and 7. Its sentinel count, one comparison an element at each of three "
                "levels, is `c·n` per level with c = 1, the recursion tree in miniature.",
            ],
        },
        "quiz_title": "Merging, splitting and the recursion tree",
        "quiz": [
            {"q": "Run MERGE-SORT on the exercise array `[2, 4, 9, 7, 1, 3, 8, 6]`, with each "
                  "merge stopping when one run is used up. How many comparisons does it make?",
             "a": ["17", "15", "24", "12"],
             "c": 1,
             "why": "Level 3 makes 4 (one per pair). On level 2, `[2, 4]` with `[7, 9]` takes "
                    "2 comparisons before the left run is used up, and `[1, 3]` with `[6, 8]` "
                    "takes 2. Level 1 interleaves to the end, 7. Total 15. Seventeen is the worst "
                    "case for n = 8, which this array does not reach; 24 is the sentinel version; "
                    "12 is a sorted array's count."},
            {"q": "Draw the recursion tree for `T(n) = 2T(n/2) + c·n` with `T(1) = c` at n = 16. "
                  "How many levels does it have, and what is the total?",
             "a": ["4 levels, 64c", "5 levels, 80c", "16 levels, 256c", "5 levels, 31c"],
             "c": 1,
             "why": "There are `lg 16 + 1 = 5` levels, sizes 16, 8, 4, 2 and 1, each costing "
                    "16c, so the total is 80c, which is `c·n·lg n + c·n`. Four levels forgets the "
                    "level of leaves, which costs `c·n` too. Sixteen levels would be a tree that "
                    "removes one element at a time. Thirty-one is the number of nodes, not the "
                    "cost."},
            {"q": "When the main loop of MERGE ends, which elements of the copied arrays L and R "
                  "have not been copied back into A?",
             "a": ["None: every element of L and R has been copied",
                   "The largest element of each half",
                   "The two sentinels",
                   "The rest of whichever half was longer"],
             "c": 2,
             "why": "The loop runs exactly `r − p + 1` times and copies that many elements, and "
                    "by the invariant they are the smallest of the `r − p + 3` in L and R. The two "
                    "left over are the largest, the sentinels ∞. The largest real elements of "
                    "the halves were copied. No leftover run is copied separately; that is the "
                    "version without sentinels, Exercise 2.3-2."},
            {"q": "At n = 8 the lab counts 17 comparisons for <code>eight</code> but only 12 for "
                  "<code>sorted</code>. Why fewer?",
             "a": ["MERGE-SORT skips the merge when the two halves are already in order",
                   "The sentinels save one comparison in every merge of a sorted array",
                   "In each merge of a sorted array, the left run is used up before any element "
                   "of the right run moves, so the merge stops after comparing the left run once",
                   "A sorted array has fewer levels, ⌈lg n⌉ − 1 instead of ⌈lg n⌉"],
             "c": 2,
             "why": "Every merge of a sorted array compares each left element with the right "
                    "run's first element and then the left run is empty, so a merge of two runs "
                    "of length m/2 costs m/2: 4 per level, 12 in all. MERGE-SORT never checks "
                    "whether halves are already in order. Sentinels add comparisons, never save "
                    "them (the sentinel count is 24 for both). The levels depend only on n."},
        ],
        "mistakes": [
            ("Crediting the speed to the splitting rather than to the cheap merge",
             "Dividing in half costs nothing much; what makes merge sort `Θ(n lg n)` is that each "
             "level of the recursion tree costs only `Θ(n)` and there are about `lg n` levels. "
             "Halve the problem but combine in quadratic time and the recurrence becomes "
             "`T(n) = 2T(n/2) + Θ(n²)`, which is `Θ(n²)`, no better than insertion sort. The "
             "combine step is where a divide-and-conquer algorithm is won or lost."),
            ("Counting lg n levels instead of lg n + 1",
             "A recursion tree for n a power of 2 has levels of size n, n/2, and so on down to 1: "
             "`lg n + 1` of them. The leaves' level is real work, n subproblems of constant cost, "
             "and here it costs `c·n` like every other level. Dropping it does not change `Θ(n lg n)`, "
             "but it gives wrong exact totals, and in other recurrences the leaves dominate."),
            ("Thinking merge sort needs n to be a power of 2",
             "MERGE-SORT splits any subarray into `⌈n/2⌉` and `⌊n/2⌋` elements and works for every "
             "n. The book assumes a power of 2 only to make each level of the analysis exactly `c·n`, "
             "and Chapter 4 shows the floors and ceilings do not change the order of growth. The "
             "lab's seven-key and twelve-key examples sort with no special treatment."),
        ],
        "standard": (
            "Finish when you can run merge sort and price it by its recursion tree.",
            "Given eight to twelve keys, run MERGE-SORT by hand counting comparisons per level, "
            "and for a recurrence of the form `2T(n/2) + c·n` draw the recursion tree and give its "
            "levels, level costs and total."
        ),
        "note": (
            "The lab counts comparisons, one ingredient of merge sort's time; copying, which "
            "MERGE also does, is n per level and is not printed. Its worst-case figure is exact "
            "for your n. That the time is Θ(n lg n) for every array of every size is the "
            "recurrence's solution, which Chapter 4 proves in general."
        ),
    },
    # ---------------------------------------------------------------- 05
    # CLRS sections 3.1-3.2, pp. 43-64.
    # Quote: p. 44, 23 words, quotes.py OK. Lesson total: 23 words.
    # Asymptotic efficiency (p. 43); Theta, O, Omega and Theorem 3.1
    # (pp. 44-49); notation in equations (pp. 49-50); o and omega
    # (pp. 50-51); comparing functions, trichotomy fails (pp. 51-52);
    # standard notations: floors, polynomials, exponentials, logarithms,
    # factorials, iterated logarithm, Fibonacci numbers (pp. 53-60).
    {
        "slug": "asymptotic-notation",
        "title": "Asymptotic Notation",
        "module": "Chapter 3 · Growth of Functions",
        "one_line": "Θ, O and Ω say that a function is eventually sandwiched, capped or floored by a constant multiple of another, each claim is witnessed by constants c and n₀, and o and ω are the strict versions.",
        "summary": (
            "Chapter 3 makes precise the notation the first two chapters used informally. Each "
            "of Θ, O, Ω, o and ω is a set of functions defined by constants: a claim f(n) = O(g(n)) "
            "is true when some c and n₀ make f(n) ≤ c·g(n) at every n from n₀ on. Section 3.2 then "
            "surveys the functions analyses meet. Check a witness by hand, then let the lab test "
            "claimed witnesses at ten thousand sizes and see where a false one breaks."
        ),
        "key": [
            "Θ(g): c₁·g(n) ≤ f(n) ≤ c₂·g(n) from n₀ on",
            "O(g): f(n) ≤ c·g(n) from n₀ on",
            "Ω(g): f(n) ≥ c·g(n) from n₀ on",
            "Θ exactly when both O and Ω hold",
            "o and ω: for every c, not just one",
            "slowest first: lg* n, lg n, n, n², 2ⁿ, n!",
        ],
        "key_label": "Sections 3.1 and 3.2 in six lines",
        "concepts_intro": (
            "Three ideas carry the chapter. The notation is used on every page that follows, "
            "and these are what it means."
        ),
        "concepts": [
            ("A bound with a witness",
             "`f(n) = O(g(n))` means there exist positive constants c and `n₀` with "
             "`0 ≤ f(n) ≤ c·g(n)` for all `n ≥ n₀`. The pair (c, `n₀`) is a witness. One witness "
             "proves the claim; a claim is false only when no witness exists."),
            ("Tight, upper and lower",
             "Θ sandwiches f between two multiples of g, O caps it from above and Ω floors it "
             "from below. O makes no claim of tightness: `n = O(n²)` is true. f is `Θ(g)` exactly "
             "when it is both `O(g)` and `Ω(g)`."),
            ("Strict bounds",
             "`f(n) = o(g(n))` means that for every positive c, however small, some `n₀` makes "
             "`f(n) < c·g(n)` from then on: f becomes insignificant beside g. ω is the reverse. "
             "`2n = o(n²)`, but `2n²` is not `o(n²)`."),
        ],
        "read_title": "The chapter's definitions first, then the witnesses",
        "read_intro": (
            "Read Sections 3.1 and 3.2 in your own copy first. The lesson sets out the "
            "definitions and the standard functions in its own words, proves one Θ bound by "
            "hand, and then tests claimed witnesses in the lab."
        ),
        "body": [
            ("p", "&ldquo;We should make sure, however, to understand the precise meaning of the "
                  "notation so that when we abuse, we do not misuse it.&rdquo; The authors write "
                  "this in the opening of Chapter 3, Growth of Functions, before defining the "
                  "notations they have been using since Chapter 2. This lesson reads Sections 3.1 "
                  "and 3.2: the five asymptotic notations, how they behave in equations, and the "
                  "standard functions that analyses keep meeting."),
            ("p", "The chapter begins from asymptotic efficiency: how running time grows as the "
                  "input grows without bound, when constants and lower-order terms no longer "
                  "matter. The notations apply to functions on the natural numbers, and the "
                  "authors stress that they apply to functions, not only to running times: "
                  "writing that insertion sort's worst case is `Θ(n²)` was a claim about the "
                  "function `a·n² + b·n + c`, and the same notation can describe space or anything "
                  "else."),
            ("def", ("Θ, O and Ω",
                     "`Θ(g(n))` is the set of functions f for which positive constants `c₁`, "
                     "`c₂` and `n₀` exist with `0 ≤ c₁·g(n) ≤ f(n) ≤ c₂·g(n)` for all `n ≥ n₀`. "
                     "`O(g(n))` keeps only the upper inequality, `0 ≤ f(n) ≤ c·g(n)`, and "
                     "`Ω(g(n))` only the lower, `0 ≤ c·g(n) ≤ f(n)`. Writing `f(n) = Θ(g(n))` "
                     "means f is a member of the set.")),
            ("p", "Θ is the asymptotically tight bound: from `n₀` on, f lies between two "
                  "constant multiples of g. Every member must be nonnegative for large n. The "
                  "definition justifies the habit of dropping lower-order terms: a quadratic "
                  "`a·n² + b·n + c` with `a > 0` is `Θ(n²)`, because a constant a little below a and "
                  "one a little above a sandwich it once n is large. O is only an upper bound, "
                  "and the book insists on the difference: `n = O(n²)` is true, and some writers' "
                  "use of O for a tight bound is not the book's."),
            ("thm", ("Theorem 3.1",
                     "For any two functions f(n) and g(n), `f(n) = Θ(g(n))` if and only if "
                     "`f(n) = O(g(n))` and `f(n) = Ω(g(n))`. In practice the theorem is used to "
                     "prove a tight bound from separate upper and lower bounds.")),
            ("p", "Applied to running times, O on the worst case bounds every input: insertion "
                  "sort's running time is `O(n²)` on every input. A Θ bound on the worst case does "
                  "not carry over that way, since insertion sort runs in linear time on sorted "
                  "input. Ω on the running time is a lower bound on the best case, so insertion "
                  "sort's running time is `Ω(n)` and `O(n²)`, and both are as tight as possible. "
                  "In an equation, a notation stands for some anonymous function in the set: "
                  "`2n² + Θ(n)` is 2n² plus some function that is `Θ(n)`; on the left of an "
                  "equation it means that whatever function is chosen there, one can be chosen on "
                  "the right to make it true."),
            ("p", "The strict notations replace one constant by all of them. `o(g(n))` is the set "
                  "of f such that for every positive c some `n₀` makes `0 ≤ f(n) < c·g(n)` from "
                  "then on, which amounts to `f(n)/g(n)` tending to 0; ω reverses it. The five "
                  "notations behave like comparisons of numbers: O like ≤, Ω like ≥, Θ like =, o "
                  "like <, ω like >, with transitivity, reflexivity for the first three, symmetry "
                  "for Θ and transpose symmetry between O and Ω, and o and ω. One property of "
                  "numbers fails: trichotomy. Two functions need not be comparable at all; n and "
                  "`n^(1 + sin n)` are the authors' example, the exponent swinging between 0 and 2."),
            ("p", "Section 3.2 reviews the standard functions. Floors and ceilings, modular "
                  "arithmetic and polynomials come first; a polynomial of degree d is `Θ(nᵈ)`. Any "
                  "exponential with base above 1 grows faster than any polynomial, and any "
                  "positive power of n grows faster than any power of `lg n`. For factorials, "
                  "`n! = o(nⁿ)`, `n! = ω(2ⁿ)` and `lg(n!) = Θ(n lg n)`, the last from Stirling's "
                  "approximation and needed again for the sorting lower bound of Chapter 8."),
            ("p", "Two less familiar functions close the section. The iterated logarithm `lg* n` "
                  "is the number of times lg must be applied to n to bring it to at most 1: it is "
                  "1 at 2, 3 at 16, 4 at 65,536 and only 5 at `2^65536`, a number far beyond any "
                  "input size. The Fibonacci numbers, `F₀ = 0`, `F₁ = 1`, each the sum of the two "
                  "before, are close to `φⁱ/√5` with φ the golden ratio, about 1.618, so they grow "
                  "exponentially. The lab's menu orders all of these."),
            ("math", [
                "the lab's menu, slowest-growing first; each grows strictly slower than the next",
                "",
                "1   lg* n   lg n   n   n lg n   n²   n³   F(n)   2ⁿ   n!",
            ]),
            ("p", "Now the lab. Write f and g as sums of up to four terms from the menu, choose the "
                  "relation and the constants, and the lab tests the inequalities at every n from "
                  "`n₀` to `n₀ + 10,000`, exactly. The tiles say whether the witness held at all "
                  "those n, the first n where it failed and which inequality broke, the values at "
                  "`n₀`, the order of growth of f against g by their leading terms, and whether "
                  "the claim itself is true for some witness."),
            ("p", "The worked example <code>quadratic-theta</code> claims `3n² + 10n = Θ(n²)` with "
                  "`c₁ = 3`, `c₂ = 4` and `n₀ = 10`. It holds at all 10,001 values, and at `n₀` "
                  "the upper inequality is an equality, 400 against 400. Choose "
                  "<code>quadratic-too-early</code>, the same claim with `n₀ = 5`: it fails at "
                  "once, `f(5) = 125` above `c₂·g(5) = 100`. The claim is still true; only this "
                  "witness is not. Choose <code>negative</code>, which claims `n² − 50n = Ω(n²)` "
                  "with `c₁ = 1/2` from `n₀ = 50`: it fails at 50, where f is 0."),
            ("p", "The example <code>nlgn-big-o-n</code> is the one to remember. It claims "
                  "`n lg n = O(n)` with `c = 100` and `n₀ = 1`, and the witness holds at every n "
                  "the lab tries, up to 10,001, while the last tile says the claim is false. Both "
                  "are right: `n lg n ≤ 100n` holds until `lg n` passes 100, near `2¹⁰⁰`. In "
                  "<code>nlgn-theta-n2</code> a false Θ claim, `n lg n = Θ(n²)` with `c₁ = 0.01`, "
                  "survives from 2 to 996 and breaks at 997. A finite check can refute a witness; "
                  "it can never establish a bound."),
            ("p", "The last examples use Section 3.2's functions. <code>fib-omega-cube</code> "
                  "claims `F(n) = Ω(n³)` from `n₀ = 21`, where `F(21) = 10,946` first passes "
                  "`21³ = 9,261`, and it holds; <code>fib-early</code> starts at 12 and fails at "
                  "once, 144 against 1,728. <code>factorial</code> confirms `n! ≥ 2ⁿ` from 4, "
                  "24 against 16. And <code>lgstar</code> claims `lg* n ≤ lg n` from 2 and fails at "
                  "3, where `lg* 3 = 2` exceeds `lg 3 ≈ 1.58`."),
            ("h3", "Exercise"),
            ("p", "Show by hand that `n² − 50n = Ω(n²)` with `c₁ = 1/2`: find the least `n₀` "
                  "from which `n² − 50n ≥ n²/2` holds at every n. Then set the lab's "
                  "<code>negative</code> example to your `n₀`, and to one less."),
            ("p", "With the notation in hand, the book returns to divide-and-conquer. The next "
                  "lesson, The Maximum-Subarray Problem and Strassen's Method, opens Chapter 4 "
                  "with two algorithms whose recurrences the notation will describe."),
        ],
        "lab": ("itakit", {
            "mode": "growth",
            "view": "bounds",
            "preset": "quadratic-theta",
            "presets": [
                {"id": "quadratic-theta", "label": "3n² + 10n = Θ(n²), c₁ = 3, c₂ = 4, n₀ = 10",
                 "f": "3, n^2; 10, n", "g": "1, n^2", "relation": "Theta",
                 "c1": "3", "c2": "4", "n0": "10",
                 "expect": {"griHolds": "yes, at all 10,001 values of n from 10 to 10,010",
                            "griAtN0": "f(10) = 400, c₁g(10) = 300, c₂g(10) = 400",
                            "griClaim": "true: some c and n₀ work"}},
                {"id": "quadratic-too-early", "label": "The same claim from n₀ = 5",
                 "f": "3, n^2; 10, n", "g": "1, n^2", "relation": "Theta",
                 "c1": "3", "c2": "4", "n0": "5",
                 "expect": {"griHolds": "no", "griFirstFail": "n = 5: f(n) > c₂·g(n)",
                            "griClaim": "true: some c and n₀ work"}},
                {"id": "negative", "label": "n² − 50n = Ω(n²), c₁ = 1/2, from n₀ = 50",
                 "f": "1, n^2; -50, n", "g": "1, n^2", "relation": "Omega",
                 "c1": "0.5", "n0": "50",
                 "expect": {"griFirstFail": "n = 50: f(n) < c₁·g(n)",
                            "griAtN0": "f(50) = 0, c₁g(50) = 1,250"}},
                {"id": "nlgn-big-o-n", "label": "n lg n = O(n), c = 100, n₀ = 1",
                 "f": "1, n lg n", "g": "1, n", "relation": "O", "c2": "100", "n0": "1",
                 "expect": {"griHolds": "yes, at all 10,001 values of n from 1 to 10,001",
                            "griOrder": "f = ω(g): n lg n grows faster than n",
                            "griClaim": "false: no c and n₀ work"}},
                {"id": "nlgn-theta-n2", "label": "n lg n = Θ(n²), c₁ = 0.01, c₂ = 1, n₀ = 2",
                 "f": "1, n lg n", "g": "1, n^2", "relation": "Theta",
                 "c1": "0.01", "c2": "1", "n0": "2",
                 "expect": {"griFirstFail": "n = 997: f(n) < c₁·g(n)",
                            "griClaim": "false: no c and n₀ work"}},
                {"id": "fib-omega-cube", "label": "F(n) = Ω(n³), c = 1, n₀ = 21",
                 "f": "1, F(n)", "g": "1, n^3", "relation": "Omega", "c1": "1", "n0": "21",
                 "expect": {"griHolds": "yes, at all 10,001 values of n from 21 to 10,021",
                            "griAtN0": "f(21) = 10,946, c₁g(21) = 9,261"}},
                {"id": "fib-early", "label": "The same claim from n₀ = 12",
                 "f": "1, F(n)", "g": "1, n^3", "relation": "Omega", "c1": "1", "n0": "12",
                 "expect": {"griFirstFail": "n = 12: f(n) < c₁·g(n)",
                            "griAtN0": "f(12) = 144, c₁g(12) = 1,728"}},
                {"id": "factorial", "label": "n! = Ω(2ⁿ), c = 1, n₀ = 4",
                 "f": "1, n!", "g": "1, 2^n", "relation": "Omega", "c1": "1", "n0": "4",
                 "expect": {"griHolds": "yes, at all 10,001 values of n from 4 to 10,004",
                            "griOrder": "f = ω(g): n! grows faster than 2^n"}},
                {"id": "lgstar", "label": "lg* n = O(lg n), c = 1, n₀ = 2",
                 "f": "1, lg* n", "g": "1, lg n", "relation": "O", "c2": "1", "n0": "2",
                 "expect": {"griFirstFail": "n = 3: f(n) > c₂·g(n)",
                            "griOrder": "f = o(g): lg* n grows slower than lg n"}},
            ],
            "panel_title": "Check a claimed witness c and n₀",
            "panel_intro": (
                "Write f and g as up to four terms each, choose O, Ω or Θ and the constants. The "
                "lab tests the inequalities at every n from n₀ to n₀ + 10,000, exactly, reports the "
                "first failure, and says separately whether any witness could prove the claim."
            ),
        }),
        "steps_title": "Proving a bound by finding a witness",
        "steps_intro": "Four steps for one claim, then one claim of your own.",
        "steps": [
            ("Write the inequalities",
             "For O write `f(n) ≤ c·g(n)`, for Ω `f(n) ≥ c·g(n)`, for Θ both, with f nonnegative "
             "from `n₀` on."),
            ("Divide by g",
             "Divide through by g(n) so the constants stand alone: `3n² + 10n ≤ c·n²` becomes "
             "`3 + 10/n ≤ c`."),
            ("Choose c, then solve for n₀",
             "Pick c a little above (for O) or below (for Ω) the leading coefficient, then solve "
             "the inequality for n. The least integer solution, if the inequality keeps holding "
             "after it, is a valid `n₀`."),
            ("Check at n₀ and argue beyond it",
             "Evaluate both sides at `n₀`, then say why the inequality cannot fail later, usually "
             "because the side you dropped only shrinks as n grows."),
            ("Witness a claim of your own",
             "Prove `n³ − 4n² = Θ(n³)` with constants of your choice, then enter f, g and your "
             "witness in the lab, confirm it holds, and if your `n₀` is the least for your "
             "constants, see it fail one step earlier."),
        ],
        "worked": {
            "title": "A Θ bound with its witness",
            "intro": [
                "Show `3n² + 10n = Θ(n²)`, the lab's example <code>quadratic-theta</code>.",
            ],
            "lines": [
                "lower: 3n² ≤ 3n² + 10n for all n ≥ 1",
                "       so c₁ = 3 works from n = 1",
                "upper: 3n² + 10n ≤ 4n² exactly when 10n ≤ n²",
                "       that is, n ≥ 10: so c₂ = 4, n₀ = 10",
                "at n₀: 300 ≤ 400 ≤ 400",
                "beyond: 10/n only shrinks",
            ],
            "after": [
                "The witness is `c₁ = 3`, `c₂ = 4`, `n₀ = 10`, and the lab confirms it at 10,001 "
                "values. A larger `c₂` would allow a smaller `n₀`: with `c₂ = 13`, `n₀ = 1` works. "
                "Witnesses are not unique; the claim needs only one.",
            ],
        },
        "quiz_title": "Witnesses and orders of growth",
        "quiz": [
            {"q": "For the exercise, what is the least `n₀` from which `n² − 50n ≥ (1/2)·n²` holds "
                  "at every n?",
             "a": ["50", "51", "100", "25"],
             "c": 2,
             "why": "The inequality is `n²/2 ≥ 50n`, that is `n ≥ 100`, and once true it stays "
                    "true. At 50, f is 0, where the lab's example fails; 51 is where f becomes "
                    "positive, still far below `n²/2`; and 25 is where `n²` first passes 50n "
                    "halved, a slip in the algebra. The lab holds from 100 and fails at 99."},
            {"q": "With `c = 1`, what is the least `n₀` from which `lg* n ≤ lg n` holds at every n?",
             "a": ["2", "4", "8", "16"],
             "c": 2,
             "why": "At 3, `lg* 3 = 2 > lg 3 ≈ 1.58`. At 4 it holds, 2 against 2, but from 5 to "
                    "7 `lg* n = 3` exceeds `lg n`, below 3. From 8 on it holds: `lg n ≥ 3` there, "
                    "and `lg* n` reaches 4 only at 17, where `lg n` is above 4. So 2 and 4 fail "
                    "later, and 16 works but is not the least."},
            {"q": "Which statement is true?",
             "a": ["n lg n = Θ(n²), because c₁ = 0.01 works from n = 2 to 996",
                   "n lg n = Ω(n²)",
                   "n lg n = O(n²), but n lg n is not Θ(n²)",
                   "n lg n = o(n)"],
             "c": 2,
             "why": "`n lg n ≤ n²` for all n ≥ 1, so O holds; but `n lg n/n²` tends to 0, so no "
                    "positive `c₁` keeps `c₁·n² ≤ n lg n` forever, and the lab shows 0.01 failing "
                    "at 997. Without that lower bound neither Θ nor Ω holds. And `n lg n` grows "
                    "faster than n, so it is ω(n), not o(n)."},
            {"q": "The lab reports that the witness `c = 100`, `n₀ = 1` for `n lg n = O(n)` "
                  "holds at every n from 1 to 10,001. What has that established?",
             "a": ["That n lg n = O(n)",
                   "That n lg n ≤ 100n at every n from 1 to 10,001, and nothing about larger n",
                   "That n lg n = Θ(n) with c₁ = c₂ = 100",
                   "That the witness fails nowhere"],
             "c": 1,
             "why": "The check covers the n it tried. The inequality fails once `lg n` exceeds "
                    "100, around `2¹⁰⁰`, so the witness does fail somewhere, the claim is false, "
                    "and no Θ statement follows. A check on a finite range can refute a witness "
                    "but never prove a bound, which needs an argument for every n from `n₀` on."},
        ],
        "mistakes": [
            ("Reading O as a tight bound",
             "In the book, `f(n) = O(g(n))` claims only that some multiple of g eventually caps f. "
             "`n = O(n²)` and `n lg n = O(n²)` are true. Saying insertion sort is `O(n²)` says "
             "nothing about whether it ever takes quadratic time; the tight statement is Θ, and "
             "the authors note that writers who use O for tight bounds are using it differently."),
            ("Taking a witness that held on a range as a proof",
             "A witness must hold at every n from `n₀` on, infinitely many. The lab checks ten "
             "thousand of them, and on <code>nlgn-big-o-n</code> a witness for a false claim "
             "passes every one. A finite check refutes a bad witness; only an argument, such as "
             "dividing by g and showing the remainder can only shrink, proves a bound."),
            ("Assuming any two functions are asymptotically comparable",
             "Real numbers obey trichotomy: one of a < b, a = b, a > b holds. Functions need "
             "not: n and `n^(1 + sin n)` are neither O nor Ω of each other, because the exponent "
             "keeps swinging between 0 and 2. The lab's menu is ordered, so every pair on it is "
             "comparable; functions in the wild may not be."),
        ],
        "standard": (
            "Finish when you can prove or refute an asymptotic claim with constants.",
            "Given f and g built from the standard functions and a relation, give a witness c and "
            "n₀ for a true claim, find the least n₀ for a given c, and explain why a false claim has "
            "no witness."
        ),
        "note": (
            "The lab tests a witness at ten thousand and one consecutive sizes, exactly. Its "
            "claim tile compares leading terms on an ordered menu; it does not prove anything "
            "about functions off the menu. A witness that passes is evidence about the range "
            "checked, and the bound itself needs the argument the steps describe."
        ),
    },
]
