"""Data Structures, the first seven lessons - sequences, heaps, hash tables.

Every count in these seven dicts was read off the lab rather than reasoned
about. Where a figure here disagrees with a class, the figure is what the kit
prints for the preset the lesson opens on, and the prose says which of the two
numbers on the page was counted and which was proved.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "arrays-linked-lists-and-the-cost-model",
        "title": "Arrays, Linked Lists, and the Cost Model",
        "module": "The cost model",
        "one_line": "Cost one operation sequence on a dynamic array and on a doubly-linked list, and name the operation that decided it.",
        "summary": (
            "An abstract data type says what the operations are; it does not say what "
            "they cost. The cost is a property of the representation, and the two "
            "oldest representations of a sequence disagree about every operation except "
            "one. Both are run here on the same sequence in the word-RAM model, with a "
            "counter on each, and the totals are `122` against `92`."
        ),
        "key": [
            "word RAM      an array index costs 1;  reaching the i-th list node costs i + 1",
            "              index   search   insert front   insert end   delete at i",
            "array             1        n          n + 1            1         n − i",
            "list          i + 1        n              1            1         i + 2",
            "",
            "16 operations from n = 16:   array 122,   list 92,   ratio 61/46",
        ],
        "key_label": "One cost model, two representations, two counts",
        "concepts_intro": (
            "One idea, stated three ways, because it is the idea the rest of the course "
            "is quoted in: the cost of an operation is a fact about how the data is "
            "stored, not about what the operation is called."
        ),
        "concepts": [
            ("The cost belongs to the representation, not to the operation",
             "&ldquo;Insert at position `i`&rdquo; is one operation with two different "
             "prices. On an array the position is free and making room is not: every "
             "element after the gap moves. On a linked list making room is free and "
             "the position is not: you walk to it. An abstract data type deliberately "
             "hides which of those you are paying for, which is exactly why a cost "
             "cannot be read off it."),
            ("Reaching a position and acting there are separate costs",
             "This is the whole of the linked-list misunderstanding. Splicing a node "
             "into a doubly-linked list is a fixed number of pointer writes &mdash; "
             "genuinely `O(1)`. Getting to the node you splice beside costs `i + 1` "
             "hops, and nothing about the list makes that cheaper. The two costs add, "
             "and only one of them is constant."),
            ("A total is about one sequence; a bound is about all of them",
             "The lab prints `122` and `92` for the sixteen operations on screen. That "
             "is evidence about those sixteen operations on a table of that size. The "
             "cost model above is the claim about every sequence, and the two are "
             "different kinds of statement &mdash; which is the habit this whole course "
             "is built to install."),
        ],
        "read_title": "The word-RAM model, and two representations priced in it",
        "read_intro": "What one step costs, what each representation charges for each operation, and the one entry in the table that is an average rather than a worst case.",
        "body": [
            ("def", ("The word-RAM cost model",
                     "Memory is an array of words. Reading or writing a word at a known "
                     "address costs <strong>1</strong>, arithmetic on a word costs "
                     "<strong>1</strong>, and nothing else is charged for. Under this "
                     "model an array index `A[i]` is one operation, because the address "
                     "is computed from `i`; reaching the i-th node of a linked list is "
                     "`i + 1` operations, because the only way to the i-th node is "
                     "through the ones before it.",
                     "This is the model every cost on this course is stated in. It has "
                     "no cache, no page, and no notion of one access being nearer than "
                     "another &mdash; System Design&rsquo;s storage course is where that "
                     "assumption is dropped and the answers change.")),
            ("p", "A <strong>dynamic array</strong> stores the elements contiguously, "
                  "with spare capacity at the end. A <strong>doubly-linked list</strong> "
                  "stores each element in its own node with pointers to its neighbours, "
                  "and keeps a pointer to the head and to the tail. Both implement the "
                  "same abstract sequence. Here is what each charges:"),
            ("math", [
                "                    index i    search     insert front    insert end    delete at i",
                "",
                "dynamic array             1         n             n + 1            1          n − i",
                "doubly-linked list    i + 1         n                 1            1          i + 2",
                "",
                "  the array pays to MAKE ROOM      the list pays to ARRIVE",
            ]),
            ("p", "Read the two rows against each other rather than down. `insert front` "
                  "is `n + 1` on the array because every one of the `n` elements shifts "
                  "up one place and then the new element is written; it is `1` on the "
                  "list because two pointers change. `index i` is `1` on the array "
                  "because the address is arithmetic; it is `i + 1` on the list because "
                  "the walk is the only route. `delete at i` costs the array the "
                  "`n − i` elements it must shift down, and costs the list `i + 2`: "
                  "`i + 1` to arrive and one splice."),
            ("example", ("One insertion at the front, both ways",
                         "With `n = 8` elements, inserting at the front costs the array "
                         "`9` and the list `1`. The lab reports exactly that pair, and it "
                         "is the single most quoted comparison in this subject. It is "
                         "also the comparison that produces the mistake, because the "
                         "next operation in almost every real sequence is a lookup, and "
                         "the lookup reverses it.")),
            ("h3", "The sequence, executed"),
            ("p", "The lab&rsquo;s opening sequence is the four operations the model is "
                  "stated on &mdash; index, insert at the front, insert at the end, "
                  "delete from the middle &mdash; repeated four times from `n = 16`, "
                  "reaching halfway along for the two that take a position. Sixteen "
                  "operations. Grouped by kind, the counters read:"),
            ("math", [
                "operation              how many    array    list",
                "",
                "index                         4        4      38",
                "insert at the front           4       74       4",
                "insert at the end             4        4       4",
                "delete from the middle        4       40      46",
                "",
                "total                        16      122      92",
            ]),
            ("p", "The list wins this sequence, `92` against `122`, and the operation "
                  "that decided it is the insertion at the front: four of them cost `74` "
                  "on the array and `4` on the list, a gap of `70` in a contest settled "
                  "by `30`. Every other row is either close or the wrong way round. That "
                  "is the useful way to read a cost comparison &mdash; find the row with "
                  "the largest gap, because that row is the answer and the rest is noise."),
            ("example", ("Two sequences that reverse the verdict",
                         "Change nothing but the mix. Three insertions at the front and "
                         "one index, four times over from `n = 24`: array `370`, list "
                         "`78`. Three indexes and one insertion at the end, same size: "
                         "array `16`, list `250`. Same two representations, same "
                         "counters, same model &mdash; a factor of nearly five one way "
                         "and a factor of fifteen the other. The representation does not "
                         "win or lose; a workload decides."),
             ),
            ("h3", "Where the counted number and the proved bound part company"),
            ("p", "One entry in that table is not a worst case. `insert end` on a "
                  "dynamic array is written `1`, and sometimes it is not `1`: when the "
                  "spare capacity runs out the array is reallocated and every element is "
                  "copied. The `1` is the <em>amortised</em> cost &mdash; the average "
                  "over a run of insertions, which is `O(1)` because doubling makes the "
                  "copies rare. The lab charges `1` every time and never shows the copy, "
                  "so the array column is a little optimistic about any single "
                  "insertion at the end, and honest about a run of them."),
            ("p", "That gap is worth naming on the first page of the course, because it "
                  "is the shape of every disagreement to come. Three different promises "
                  "hide behind a single small number: a <strong>worst case</strong> that "
                  "no input beats, an <strong>amortised</strong> cost that holds on "
                  "average over a sequence, and an <strong>expected</strong> cost that "
                  "holds on average over some randomness. A measurement cannot tell them "
                  "apart. `122` and `92` are two integers produced by running sixteen "
                  "operations; they are not a bound, and the next lesson is about a "
                  "structure whose whole interest is that the distinction matters."),
        ],
        "lab": ("seqkit", {
            "mode": "arraylist",
            "preset": "four-operations",
            "panel_title": "Compose a sequence and watch both representations pay",
            "panel_intro": "Every figure is a count in the word RAM: an array index is `1`, "
                           "reaching the i-th list node is `i + 1`, and a shift moves every "
                           "element after the gap. Change the mix and the winner changes. "
                           "Nothing here is a complexity class &mdash; the table is the "
                           "sequence executed, operation by operation.",
        }),
        "steps_title": "Pricing a sequence you have been handed",
        "steps_intro": "The order matters: the operation list comes before either representation, and the label on the cost comes last.",
        "steps": [
            ("Write the operation sequence out, with positions",
             "&ldquo;Mostly lookups with some insertions&rdquo; cannot be costed. "
             "`index at 8, insert front, insert end, delete at 9` can. A position is "
             "part of an operation here, because two of the four costs depend on it."),
            ("Price each operation on each representation",
             "One row per operation, one column per representation, from the table "
             "above. Keep the running size in its own column: an insertion changes `n`, "
             "and the operation after it is priced at the new size."),
            ("Add the columns and find the row with the largest gap",
             "The totals answer the question; the widest row explains it. If the widest "
             "gap is small relative to the totals, the honest report is that the "
             "representation barely matters for this mix &mdash; which happens, and is "
             "worth saying."),
            ("Label each cost worst-case, amortised or expected",
             "Everything in the table above is worst-case except the array&rsquo;s "
             "insertion at the end, which is amortised. Writing the label beside the "
             "number is the habit that keeps a fast measurement from being read as a "
             "guarantee."),
        ],
        "worked": {
            "title": "Four operations at n = 16, priced twice",
            "intro": [
                "One round of the lab&rsquo;s opening sequence, by hand, with the running "
                "size carried down. The lab does four rounds; the first is where the "
                "arithmetic is visible."
            ],
            "lines": [
                "n = 16,  positions halfway along",
                "",
                "step  operation            at    size    array           list",
                "  1   index                 8      16    1               8 + 1  =  9",
                "  2   insert at the front   —      17    16 + 1 =  17    1",
                "  3   insert at the end     —      18    1               1",
                "  4   delete from the       9      17    18 − 9 =   9    9 + 2  = 11",
                "      middle",
                "",
                "round total                            28              22",
                "",
                "four rounds, as the lab counts them    122             92",
                "",
                "ratio  122 : 92  =  61 : 46            the list, by 30",
            ],
            "after": [
                "The array&rsquo;s `17` at step 2 is the whole of its loss, and it grows "
                "as the sequence runs: by the fourth round that one operation costs `20`, "
                "because three insertions have made the array longer. The list&rsquo;s "
                "`9` and `11` at steps 1 and 4 are its loss, and they grow the same way "
                "and more slowly.",
                "Notice what the round total does not tell you. `28` against `22` is a "
                "true statement about four operations at one size. It does not establish "
                "that the list is cheaper for this pattern at every size, and it does not "
                "settle where you might guess: the lab reports `61 : 46` at `n = 16`, "
                "`109 : 78` at `n = 32` and `205 : 142` at `n = 64`, creeping toward "
                "`3 : 2` as the array&rsquo;s front insertion grows like `n` against the "
                "list&rsquo;s walk of `n/2`. Reading a bound off two integers is the "
                "thing to distrust.",
                "For a faded rehearsal, price `search, insert end, search, delete at the "
                "middle` at `n = 20`, one round. The supplied first move is that `search` "
                "costs `n` on both, so the two columns are equal for steps 1 and 3 and "
                "the contest is decided by steps 2 and 4 alone. Predict the winner before "
                "you total it; then run that preset in the lab, which reports `212` "
                "against `216` over four rounds, and say why it is nearly a tie.",
            ],
        },
        "quiz_title": "Pricing operations",
        "quiz": [
            {"q": "A doubly-linked list holds `20` elements. What does it cost to delete the element at position `10`, in the model above?",
             "a": ["`1`", "`10`", "`12`", "`20`"],
             "c": 2,
             "why": "`i + 2` = `12`: eleven steps to arrive at position `10` counting from "
                    "the head, then one splice. `1` is the splice with the walk forgotten "
                    "&mdash; the most common wrong answer and the whole misconception of "
                    "this lesson. `10` is the walk with the splice forgotten. `20` is the "
                    "array&rsquo;s worst case for a deletion, not the list&rsquo;s."},
            {"q": "On the lab&rsquo;s opening sequence the array totals `122` and the list totals `92`. Which operation decided it?",
             "a": ["index", "insert at the front", "insert at the end", "delete from the middle"],
             "c": 1,
             "why": "The four insertions at the front cost `74` on the array and `4` on "
                    "the list &mdash; a gap of `70` in a contest settled by `30`. `index` "
                    "has a gap of `34` the other way, `delete from the middle` a gap of "
                    "`6`, and `insert at the end` costs `4` on both, so it cannot decide "
                    "anything."},
            {"q": "Which cost in the table above is an average over a run of operations rather than a worst case?",
             "a": ["the array&rsquo;s index, which is `1`",
                   "the array&rsquo;s insertion at the end, which is `1`",
                   "the list&rsquo;s insertion at the front, which is `1`",
                   "the list&rsquo;s search, which is `n`"],
             "c": 1,
             "why": "Appending to a dynamic array is `1` until the spare capacity runs "
                    "out, and then it is `n` while everything is copied to a bigger "
                    "block. The `1` is amortised. The array&rsquo;s index really is one "
                    "operation every time, the list&rsquo;s splice really is a fixed "
                    "number of pointer writes every time, and a list search really does "
                    "scan in the worst case."},
        ],
        "mistakes": [
            ("Reading a linked list’s insertion as constant time",
             "The splice is constant; arriving is not. Inserting at position `i` costs "
             "`i + 2`, and inserting at the front costs `1` only because the front is "
             "the one position you already hold a pointer to. Any claim that a list "
             "inserts in `O(1)` is really a claim about a cursor you already have, and "
             "the moment the position is described by an index rather than by a pointer, "
             "the walk is back."),
            ("Comparing representations on a sequence chosen to suit one of them",
             "Three insertions at the front and one index gives the list a factor of "
             "nearly five. Three indexes and one insertion at the end gives the array a "
             "factor of fifteen. Both are real measurements of the same two structures, "
             "and either one quoted alone is an advertisement rather than an analysis."),
            ("Treating a measured total as a bound",
             "`122` against `92` is a fact about sixteen operations at one size. It "
             "licenses no statement about other sizes, other mixes, or other positions, "
             "and the cost table above &mdash; which is a claim about all of them "
             "&mdash; is a different kind of object that no amount of running can "
             "produce."),
        ],
        "standard": ("Finish when you can price an operation before you are told which structure it is on, by asking where the position comes from.",
                     "You should be able to fill in both rows of the cost table from "
                     "memory, price a stated sequence on both representations with the "
                     "running size carried correctly, name the operation whose gap "
                     "decided the total, and say which single entry in the table is "
                     "amortised rather than worst-case."),
        "note": (
            "Two of the four operations above were expensive on both representations, "
            "and a structure that restricts which positions you may touch can be cheap "
            "on all of its operations for that reason. &ldquo;Stacks, Queues, and the "
            "Two-Stack Queue&rdquo; takes the smallest interesting case: a queue built "
            "from two stacks, where one dequeue costs `n` and the guarantee is still "
            "constant &mdash; the first place on this course where a single measurement "
            "and the promise behind it are plainly not the same statement."
        ),
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "stacks-queues-and-the-two-stack-queue",
        "title": "Stacks, Queues, and the Two-Stack Queue",
        "module": "The cost model",
        "one_line": "Count the stack moves in an enqueue/dequeue sequence and give the credit argument that bounds the total by `3m`.",
        "summary": (
            "A queue can be built from two stacks: push arrivals onto one, and when the "
            "other is empty, pour everything across. One dequeue then costs `n`, and the "
            "whole sequence still costs at most three per arrival, because each element "
            "is pushed once, moved once and popped once. The expensive dequeue does not "
            "go away; it is paid for in advance."
        ),
        "key": [
            "stack   push, pop at one end          queue   enqueue at one end, dequeue at the other",
            "",
            "two-stack queue:  enqueue → push on IN",
            "                  dequeue → if OUT empty, pop all of IN onto OUT; then pop OUT",
            "",
            "each element is pushed once, moved once, popped once   ⟹   total ≤ 3m",
            "EEEDDD:  costs 1 1 1 4 1 1 = 9        3m = 3 × 3 = 9",
            "credit   2 4 6 2 1 0                  never negative, which is the argument",
        ],
        "key_label": "The construction, and the three charges that pay for it",
        "concepts_intro": (
            "The structure is four lines long and the analysis is the point. What is new "
            "is not the queue; it is that a bound over a sequence can be proved by "
            "charging each element in advance."
        ),
        "concepts": [
            ("Restricting the positions is what makes the operations cheap",
             "A stack touches one end and a queue touches two, and that is the entire "
             "reason both are constant-time on every operation while a general sequence "
             "is not. Neither can answer &ldquo;what is at position `7`&rdquo; at all. "
             "Cheapness here is bought by refusing questions, which is the trade this "
             "whole course is about."),
            ("Amortised means over the sequence, and the expensive step is still there",
             "In `EEEDDD` the fourth operation costs `4` while the other five cost `1`. "
             "The amortised bound does not say that dequeue was fast. It says the six "
             "operations together cost `9`, which is `3` per arrival, and it is silent "
             "about which of them paid. A reader who cannot point at the expensive "
             "operation has read the bound as &ldquo;always fast&rdquo;."),
            ("Credit is an accounting device, not a mechanism",
             "Nothing in the code stores credit. The argument charges `3` for each "
             "enqueue, spends `1` on the push and banks `2`; a dequeue spends from the "
             "bank. If the balance is never negative then the charges covered the real "
             "costs, so the real total is at most the charged total. The structure is "
             "unchanged; only the bookkeeping is new."),
        ],
        "read_title": "Two stacks, one queue, and an argument that pays in advance",
        "read_intro": "The construction, the sequence where one dequeue costs four, and why the total is nevertheless bounded by three per arrival.",
        "body": [
            ("def", ("Stack and queue",
                     "A <strong>stack</strong> supports `push` and `pop` at one end: the "
                     "element removed is the one most recently added. A "
                     "<strong>queue</strong> supports `enqueue` at one end and `dequeue` "
                     "at the other: the element removed is the one least recently added. "
                     "Neither supports access by position, and that restriction is what "
                     "makes every operation on both of them cost `1` on an array or on a "
                     "list.")),
            ("def", ("The two-stack queue",
                     "Keep two stacks, IN and OUT. To <strong>enqueue</strong>, push onto "
                     "IN. To <strong>dequeue</strong>: if OUT is empty, pop every element "
                     "of IN and push it onto OUT, which reverses the order; then pop OUT. "
                     "Because a stack reverses and two reversals restore, the element "
                     "that comes off OUT is the oldest one still in the queue.")),
            ("p", "Charge one for each push, each pop and each move. Then an enqueue "
                  "costs `1` always. A dequeue costs `1` when OUT is not empty, and "
                  "`k + 1` when OUT is empty and IN holds `k` elements &mdash; `k` moves "
                  "and then the pop. So the worst single dequeue costs as much as the "
                  "number of elements in the queue, and that is a genuine `Θ(n)` "
                  "operation that a reader is entitled to be unhappy about."),
            ("example", ("Three in, three out",
                         "The sequence `E E E D D D` costs `1, 1, 1, 4, 1, 1`, adding to "
                         "`9`. The `4` is the first dequeue: three moves to pour IN into "
                         "OUT, then one pop. The two dequeues after it cost `1` each, "
                         "because OUT already holds their elements. One operation out of "
                         "six cost four times what the others did, and the sequence total "
                         "is `9` for three arrivals &mdash; exactly `3` each.")),
            ("h3", "The accounting argument"),
            ("p", "The technique is the accounting method of Discrete Mathematics&rsquo; "
                  "&ldquo;Recursion Trees and Amortised Analysis&rdquo;, applied to a "
                  "structure rather than to a loop. Give every enqueue a budget of `3`: "
                  "one for the push that happens now, one to pay for the move this "
                  "element will make later, and one to pay for the pop that will finally "
                  "remove it. Nothing else in the structure ever touches an element."),
            ("thm", ("The two-stack queue costs at most 3 per enqueue",
                     "Over any sequence of operations containing `m` enqueues, the total "
                     "cost of the two-stack queue is at most `3m`.",
                     "Every element enters exactly once, is moved from IN to OUT at most "
                     "once, and is popped from OUT at most once &mdash; once it has been "
                     "moved it is never pushed back, because elements only ever travel "
                     "from IN to OUT. So the three units charged at its enqueue cover "
                     "every operation performed on it, for ever. Summing over the `m` "
                     "elements gives `3m`, and the real total cannot exceed the charged "
                     "total.")),
            ("proof", [
                "Formally, let the credit after an operation be the charged total so far "
                "minus the real total so far. An enqueue is charged `3` and costs `1`, so "
                "the credit rises by `2`. A dequeue is charged `0` and costs `k + 1` or "
                "`1`, so the credit falls by that much.",
                "The credit is never negative. Each element of IN carries `2` unspent "
                "units and each element of OUT carries `1`, so before a dequeue that must "
                "pour `k` elements across, the bank holds at least `2k` &mdash; and the "
                "dequeue costs `k + 1 ≤ 2k` for `k ≥ 1`. A dequeue on a non-empty OUT "
                "costs `1` and that element&rsquo;s own unspent unit pays for it.",
                "Since the credit is the charged total minus the real total and it is "
                "never negative, the real total is at most the charged total, which is "
                "`3m`. The lab prints the credit balance after every step for exactly "
                "this reason: if it ever went negative the argument would be wrong, and "
                "watching it stay non-negative is watching the proof run.",
            ]),
            ("h3", "What the measurement does and does not show"),
            ("p", "On `E E E D D D` the lab reports a total of `9` and a bound of `9`: "
                  "the two agree, because every element that arrived was also served, so "
                  "each one really did pay all three of its charges. On `E D E D E D E D` "
                  "the total is `12` and the bound is `12`, for the same reason. On the "
                  "twelve-operation sequence `E E D E E D E E D D D D` the total is `18` "
                  "with one dequeue costing `5`, and the bound is again `18`."),
            ("p", "That the two keep coinciding is informative and it is not the "
                  "theorem. A sequence that enqueues and never dequeues costs `m` against "
                  "a bound of `3m`, so the bound is loose there; the coincidence above "
                  "happens when the queue is drained. What no sequence can do is "
                  "establish the bound, because the bound quantifies over sequences and "
                  "a run is one sequence. Type in a pattern that makes the expensive "
                  "dequeue as expensive as you can &mdash; the cumulative line will "
                  "approach the `3m` line and, by the argument above, never cross it."),
        ],
        "lab": ("seqkit", {
            "mode": "twostack",
            "preset": "fill-then-drain",
            "panel_title": "Type a sequence and watch the credit balance",
            "panel_intro": "`E` enqueues and `D` dequeues. Both stacks are drawn, the "
                           "per-operation cost and the running total are counted, and the "
                           "cumulative cost is plotted against the `3m` line the argument "
                           "promises. The credit balance is the proof made visible: it must "
                           "never go negative, and the expensive dequeue is the step where "
                           "it drops.",
        }),
        "steps_title": "Running and bounding a queue sequence",
        "steps_intro": "Cost it first, then account for it. Doing the accounting first is how a bound gets asserted rather than proved.",
        "steps": [
            ("Track both stacks, not just the queue",
             "Write IN and OUT side by side and update them. The state of the queue "
             "alone cannot tell you what the next dequeue costs, because the cost "
             "depends entirely on whether OUT happens to be empty."),
            ("Cost each operation as it happens",
             "Enqueue `1`. Dequeue `1` if OUT is non-empty, `k + 1` if it is empty and "
             "IN holds `k`. Keep a running total in its own column, and mark the "
             "operations that poured &mdash; those are the only interesting ones."),
            ("Find the expensive operation and say how expensive",
             "There is one in almost every sequence, and the point of the exercise is "
             "that you can name it and quote its cost. An amortised bound you cannot "
             "point at the expensive step of has been read as a worst case."),
            ("Charge 3 per enqueue and check the balance",
             "Add a credit column: `+2` on each enqueue, minus the real cost on each "
             "dequeue. If it is ever negative the charge was too small. If it never is, "
             "the total is at most `3m`, and you have proved something about the whole "
             "sequence rather than measured one."),
        ],
        "worked": {
            "title": "E E E D D D, counted and then accounted for",
            "intro": [
                "Six operations, three arrivals. The first column is what the structure "
                "did; the last is the argument that bounds it."
            ],
            "lines": [
                "step  op        IN        OUT       cost   total   credit   3m",
                "",
                "  1   E 1       [1]       []           1       1        2    3",
                "  2   E 2       [1 2]     []           1       2        4    6",
                "  3   E 3       [1 2 3]   []           1       3        6    9",
                "  4   D  →1     []        [3 2]        4       7        2    9",
                "        pour 3 across, then pop 1",
                "  5   D  →2     []        [3]          1       8        1    9",
                "  6   D  →3     []        []           1       9        0    9",
                "",
                "served in order   1, 2, 3          the queue order, from two stacks",
                "total 9   =   3m   =   3 × 3       credit ended at 0, never negative",
            ],
            "after": [
                "Step 4 is the lesson. It cost `4` where every other step cost `1`, and "
                "it did so because OUT was empty and IN held three elements: three moves "
                "and a pop. Nothing about the amortised bound makes that step cheap. "
                "What the bound says is that the six steps together cost `9`, and they "
                "did.",
                "The credit column is where the `3` comes from. Each enqueue banked `2` "
                "after paying for its own push, so `6` was in the bank when the "
                "expensive dequeue arrived; it spent `4` and left `2`, and the two cheap "
                "dequeues spent the rest. The balance reached `0` and never went below, "
                "which is precisely the condition the theorem needs.",
                "For a faded rehearsal, take `E E D E E D E E D D D D`. The supplied "
                "first move is that the dequeue at step 3 pours two elements and costs "
                "`3`, and the dequeue at step 6 finds OUT non-empty and costs `1`. Carry "
                "the table to the end, find the one dequeue that costs `5`, and check "
                "that the total is `18` against a bound of `3 × 6`. Then say, in one "
                "sentence, why running a second sequence would not make the bound any "
                "more established than running the first.",
            ],
        },
        "quiz_title": "Cost and guarantee",
        "quiz": [
            {"q": "A two-stack queue holds `6` elements, all of them in IN. What does the next dequeue cost?",
             "a": ["`1`", "`6`", "`7`", "`18`"],
             "c": 2,
             "why": "Six moves to pour IN into OUT, then one pop: `k + 1` = `7`. `1` is "
                    "what it costs when OUT is already non-empty, which is not this case. "
                    "`6` is the pour with the pop forgotten. `18` is `3m`, the bound on "
                    "the whole sequence, which is not a cost of any single operation."},
            {"q": "&ldquo;Dequeue is amortised `O(1)`.&rdquo; Which of these does that claim rule out?",
             "a": ["A single dequeue costing `Θ(n)`",
                   "A sequence of `m` enqueues and `m` dequeues costing `Θ(m log m)`",
                   "Two consecutive dequeues both costing more than `1`",
                   "The queue ever holding more than a constant number of elements"],
             "c": 1,
             "why": "An amortised bound is a statement about the total: `m` enqueues and "
                    "the dequeues that drain them cost `Θ(m)`, so `Θ(m log m)` is "
                    "excluded. A single `Θ(n)` dequeue is not excluded &mdash; the "
                    "sequence in this lesson contains one. Two expensive dequeues in a "
                    "row are not excluded either; they are just both paid for. And the "
                    "bound says nothing at all about how many elements the queue holds."},
            {"q": "In the credit argument, why is `3` the charge per enqueue rather than `2`?",
             "a": ["Because there are three operations in the structure",
                   "Because each element is pushed once, moved once and popped once",
                   "Because the queue has two stacks and one pointer",
                   "Because a dequeue can cost up to three times what an enqueue costs"],
             "c": 1,
             "why": "The charge counts the operations an element will ever be involved "
                    "in: the push onto IN, the move to OUT, and the pop off OUT. Three "
                    "units cover all of them for ever, because an element never travels "
                    "back. The number is not about the interface, the number of stacks, "
                    "or a ratio between operation costs &mdash; a dequeue can cost `n + 1`, "
                    "which is unbounded relative to an enqueue."},
        ],
        "mistakes": [
            ("Reading amortised as a promise about every operation",
             "It is a promise about the total. The expensive dequeue in `E E E D D D` "
             "costs four times its neighbours and is not an exception to the bound; it "
             "is what the bound was designed to absorb. Anyone who needs a guarantee on "
             "each individual operation &mdash; an interactive system, a real-time "
             "deadline &mdash; is asking a question the amortised bound does not answer, "
             "and needs a worst-case structure instead."),
            ("Concluding the bound is proved because the run stayed under it",
             "The cumulative line sits under the `3m` line for every sequence you can "
             "type, and typing sequences is not what establishes that. The argument "
             "does, by charging every element in advance and observing that the charges "
             "cover everything that will ever happen to it. The lab shows the credit "
             "balance so that you can watch the argument hold, not so that you can "
             "confirm it by sampling."),
            ("Thinking the credit is stored somewhere",
             "There is no credit field, no counter and no cost in the structure for "
             "maintaining one. The bank is a device in the proof. A reader who looks for "
             "where the credit lives has mistaken an accounting argument for an "
             "implementation, and will then wonder why the structure does not slow down "
             "as the balance grows."),
        ],
        "standard": ("Finish when you can point at the expensive operation in a sequence and still state the constant bound without flinching.",
                     "You should be able to run an enqueue/dequeue sequence keeping both "
                     "stacks, quote the cost of the dequeue that pours, carry a credit "
                     "column that never goes negative, and explain why `3` is the right "
                     "charge per arrival in terms of what happens to one element over its "
                     "whole life in the structure."),
        "note": (
            "Stacks and queues serve in arrival order and refuse every other question. "
            "The next structure answers exactly one more: which element is smallest, at "
            "any moment. &ldquo;Priority Queues and Binary Heaps&rdquo; gets it in "
            "`O(log n)` with no pointers at all, by storing a tree in an array and "
            "keeping one inequality true at every node."
        ),
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "priority-queues-and-binary-heaps",
        "title": "Priority Queues and Binary Heaps",
        "module": "Heaps",
        "one_line": "Insert and extract by sifting, read the array back as a tree, and check each operation’s comparisons against `⌊log₂ n⌋`.",
        "summary": (
            "A binary heap keeps one inequality true &mdash; every parent is at most its "
            "children &mdash; on a complete tree stored in a plain array. That is enough "
            "for insert and extract-min in `O(log n)`, with no pointers anywhere, "
            "because the tree&rsquo;s shape is arithmetic on indices. What it is not is "
            "sorted: siblings are in no particular order, and the array almost never "
            "reads as an ordered list."
        ),
        "key": [
            "heap property        parent ≤ both children,  at every node",
            "complete tree        every level full except the last, which fills left to right",
            "layout, from 1       children of i at 2i and 2i + 1;  parent of i at ⌊i/2⌋",
            "layout, from 0       children of i at 2i + 1 and 2i + 2   (what the lab draws)",
            "",
            "insert       sift UP     ≤ ⌊log₂ n⌋ comparisons",
            "extract-min  sift DOWN   ≤ 2⌊log₂ n⌋ comparisons",
        ],
        "key_label": "One inequality, one shape, and the arithmetic that replaces pointers",
        "concepts_intro": (
            "Three things, and the third is the one that gets misread on every first "
            "reading: the inequality, the layout, and what the inequality does not say."
        ),
        "concepts": [
            ("The heap property is local and it is only about ancestry",
             "`parent ≤ child` at every node. Nothing relates a node to its sibling, to "
             "its cousin, or to anything that is not on the path between it and the root. "
             "The consequence that matters is that the minimum is at the root, because "
             "the root is an ancestor of everything &mdash; and the consequence that gets "
             "assumed and is false is that the array is in order."),
            ("The shape is arithmetic, so there are no pointers",
             "A complete tree can be laid out level by level in an array, and then the "
             "children of position `i` are at `2i` and `2i + 1` when positions start at "
             "`1`. No node stores a link; the tree is a way of reading the array. This is "
             "why a heap is the cheapest structure in this course to implement and the "
             "one a sorting algorithm can build in place."),
            ("A sift walks one root-to-leaf path, and that is where the log comes from",
             "Insert puts the new key at the end and swaps it up while it is smaller than "
             "its parent: at most one comparison per level. Extract-min moves the last "
             "key to the root and swaps it down while it is larger than a child: two "
             "comparisons per level, because the smaller child has to be found first. A "
             "complete tree on `n` nodes has height `⌊log₂ n⌋`, and that is the whole "
             "bound."),
        ],
        "read_title": "The property, the layout, and the two sifts",
        "read_intro": "What a heap promises, how an array becomes a tree, and the measured comparison counts against the height.",
        "body": [
            ("def", ("Min-heap",
                     "A <strong>min-heap</strong> is a complete binary tree whose every "
                     "node satisfies the <strong>heap property</strong>: the key at a "
                     "node is less than or equal to the keys at both of its children. "
                     "<strong>Complete</strong> means every level is full except "
                     "possibly the last, which is filled from the left.",
                     "The root therefore holds a minimum, since it is an ancestor of "
                     "every node and the property is transitive along a path. A max-heap "
                     "reverses the inequality and nothing else about it changes.")),
            ("p", "Completeness is what allows the array layout, and the array layout is "
                  "what removes the pointers. Write the levels out in order, left to "
                  "right. Then for a position `i` counted from `1`, the children sit at "
                  "`2i` and `2i + 1` and the parent at `⌊i/2⌋`. The lab draws its array "
                  "with positions counted from `0`, where the same tree has its children "
                  "at `2i + 1` and `2i + 2` &mdash; the arithmetic differs by where you "
                  "start counting and the tree is identical, which is worth confirming "
                  "once on the picture rather than believing."),
            ("math", [
                "array      1    3    2    6    8    7    4    9        positions from 1",
                "",
                "                      1                    level 0",
                "                 3         2               level 1",
                "               6   8     7   4             level 2",
                "              9                            level 3",
                "",
                "  every path down increases:  1 3 6 9,  1 3 8,  1 2 7,  1 2 4",
                "  siblings are unrelated:     3 sits left of 2,  8 left of 7",
            ]),
            ("p", "That array is what the lab holds after inserting `1, 9, 2, 8, 3, 7, "
                  "4, 6` in that order, and it is a perfectly valid heap. It is also not "
                  "sorted, not nearly sorted, and not sorted after any prefix: the second "
                  "element is `3` and the third is `2`. If a heap were sorted then "
                  "building one would sort, and sorting costs more than building a heap "
                  "does &mdash; which is the argument that ought to make the "
                  "misconception uncomfortable before the picture does."),
            ("h3", "Insert, by sifting up"),
            ("p", "Put the new key in the first free array position, which keeps the "
                  "tree complete. Then while it is smaller than its parent, swap the two. "
                  "The property can only be violated between the new key and its "
                  "ancestors, and each swap repairs one level, so the walk stops at the "
                  "root at the latest: at most `⌊log₂ n⌋` comparisons and as many swaps."),
            ("example", ("The insertion that swaps, and the one that does not",
                         "Inserting `8` into the three-element heap the lab has after "
                         "`1, 9, 2` compares `8` against its parent `9`, swaps, compares "
                         "against `1`, and stops: `2` comparisons, `1` swap, against a "
                         "bound of `⌊log₂ 4⌋ = 2`. Inserting `7` a step later costs `1` "
                         "comparison and no swap at all, because it lands under `2` and "
                         "is bigger. Both are `O(log n)`; one of them did nothing.")),
            ("h3", "Extract-min, by sifting down"),
            ("p", "The root is the answer. Removing it leaves a hole, so move the last "
                  "element into the root &mdash; which keeps the tree complete &mdash; "
                  "and then push it down: compare its two children with each other, then "
                  "compare it with the smaller one, and swap if it is larger. Two "
                  "comparisons per level, `⌊log₂ n⌋` levels, so at most `2⌊log₂ n⌋`."),
            ("math", [
                "heap    1  3  2  6  8  7  4  9          extract the minimum, 1",
                "",
                "move 9 to the root:     9  3  2  6  8  7  4",
                "children of 9 are 3, 2  →  smaller is 2  →  9 > 2, swap",
                "                        2  3  9  6  8  7  4",
                "children of 9 are 7, 4  →  smaller is 4  →  9 > 4, swap",
                "                        2  3  4  6  8  7  9",
                "",
                "comparisons 4,  swaps 2,  bound 2⌊log₂ 7⌋ = 4      tight here",
            ]),
            ("p", "Four comparisons against a bound of four: the sift reached a leaf, "
                  "which is the worst case at that size, and the counter and the bound "
                  "agree. That agreement is a coincidence of this input, and the very "
                  "next extraction in the lab also costs `4` while the inserts before it "
                  "cost between `0` and `2` against bounds of `0` to `3`. Over the whole "
                  "ten-operation sequence the lab counts `18` comparisons and `7` swaps, "
                  "and reports that every single step came in at or under its bound."),
            ("p", "That last report is the one to be careful with. &ldquo;Every step "
                  "came in under its bound&rdquo; is a statement about ten operations on "
                  "eight keys. The bound itself is a statement about a path in a complete "
                  "tree, and the proof is one line: a complete tree on `n` nodes has "
                  "height `⌊log₂ n⌋`, a sift visits each level at most once, and each "
                  "level costs at most two comparisons. The lab can show you the walk; it "
                  "cannot show you that there is no taller tree."),
        ],
        "lab": ("heap", {
            "mode": "ops",
            "preset": "siblings-unordered",
            "panel_title": "Insert, extract, and read the array as a tree",
            "panel_intro": "Type the keys to insert and how many minima to extract. The "
                           "tree and the array are drawn together, the swapped positions are "
                           "highlighted on both, and each operation reports its comparisons "
                           "beside `⌊log₂ n⌋`. The opening keys are chosen so that the "
                           "siblings come out unordered &mdash; the array is a valid heap "
                           "and is nothing like sorted.",
        }),
        "steps_title": "Operating a heap by hand",
        "steps_intro": "Four steps, and the first is the one that prevents an hour of confusion: decide where you are counting positions from.",
        "steps": [
            ("Fix your indexing before you touch anything",
             "From `1`, children of `i` are at `2i` and `2i + 1`. From `0`, they are at "
             "`2i + 1` and `2i + 2`. Both are in use, the lab draws the second, and an "
             "index formula from one convention applied under the other silently walks "
             "to the wrong node."),
            ("Insert at the end, then sift up",
             "The new key goes in the first free position so the tree stays complete. "
             "Compare it with its parent and swap while it is smaller. Stop at the root "
             "or at the first parent that is already smaller &mdash; there is nothing "
             "further up to fix."),
            ("Extract by promoting the last element, then sift down",
             "Take the root as the answer, move the last element into the root, and push "
             "it down. At each level find the smaller child first, then compare. Skipping "
             "the child-versus-child comparison is the error that produces a tree that "
             "still looks plausible."),
            ("Check the property, then check the count",
             "Walk every node and confirm `parent ≤ children`. Then compare the "
             "comparisons you made with `⌊log₂ n⌋` for an insert and `2⌊log₂ n⌋` for an "
             "extract. A count above the bound means a step went wrong; a count well "
             "below it means the sift stopped early, which is ordinary."),
        ],
        "worked": {
            "title": "Eight keys in, two minima out",
            "intro": [
                "The lab&rsquo;s opening sequence, by hand. The comparison count and the "
                "bound sit in the last two columns; the array after each step is what the "
                "picture is drawing."
            ],
            "lines": [
                "insert   array after                  cmp   bound ⌊log₂ n⌋",
                "",
                "   1     1                              0       0",
                "   9     1 9                            1       1",
                "   2     1 9 2                          1       1",
                "   8     1 8 2 9      (8 swapped past 9)  2       2",
                "   3     1 3 2 9 8    (3 swapped past 8)  2       2",
                "   7     1 3 2 9 8 7                    1       2",
                "   4     1 3 2 9 8 7 4                  1       2",
                "   6     1 3 2 6 8 7 4 9                2       3",
                "",
                "extract  array after                  cmp   bound 2⌊log₂ n⌋",
                "",
                "   1     2 3 4 6 8 7 9                   4       4",
                "   2     3 6 4 9 8 7                     4       4",
                "",
                "totals   comparisons 18,  swaps 7,  every step at or under its bound",
            ],
            "after": [
                "Look at the array after the eighth insert: `1 3 2 6 8 7 4 9`. Every "
                "root-to-leaf path increases &mdash; `1 3 6 9`, `1 3 8`, `1 2 7`, "
                "`1 2 4` &mdash; and the array itself is in no order whatever. `3` "
                "precedes `2`, and `8` precedes `7` and `4`. This is the picture that "
                "settles the misconception, and it is worth staring at until it stops "
                "looking like a mistake.",
                "The two extractions both cost `4`, which equals `2⌊log₂ 7⌋` and "
                "`2⌊log₂ 6⌋`. Both sifts went all the way to a leaf, which is the worst "
                "case at those sizes. The inserts, by contrast, came in at `0` to `2` "
                "against bounds of `0` to `3`, because a sift up stops as soon as the "
                "parent is smaller and most keys arrive somewhere they can stay.",
                "For a faded rehearsal, insert `8, 7, 6, 5, 4, 3, 2, 1` in that order "
                "and extract three times. The supplied observation is that every one of "
                "these keys is smaller than everything already in the heap, so every "
                "insert sifts all the way to the root: the swap count and the comparison "
                "count coincide. Predict the total before running it &mdash; the lab "
                "reports `22` comparisons and `17` swaps &mdash; and then say why "
                "reversing the input made no difference at all to the bound.",
            ],
        },
        "quiz_title": "The property and the counts",
        "quiz": [
            {"q": "Is `1 3 2 6 8 7 4 9` a valid min-heap, reading positions from `1`?",
             "a": ["No, because `3` comes before `2`",
                   "Yes: every parent is at most both of its children",
                   "No, because the array is not sorted",
                   "Only if the tree is not complete"],
             "c": 1,
             "why": "Children of position `1` are `3` and `2`, and `1 ≤ 3` and `1 ≤ 2`. "
                    "Children of `2` are `6` and `8`, and `3` is at most both. Children of "
                    "`3` are `7` and `4`, and `2` is at most both. Child of `4` is `9`. "
                    "Every check passes. `3` before `2` is a statement about siblings, "
                    "which the heap property says nothing about, and a heap is not "
                    "required to be sorted &mdash; if it were, building one would sort."},
            {"q": "An extract-min on a heap of `7` elements is bounded by `2⌊log₂ 7⌋` comparisons. Why the factor of `2`?",
             "a": ["Because the sift may have to run twice",
                   "Because the root is compared with both of its children at each level",
                   "Because the tree has two subtrees",
                   "Because the last element is moved and then the root is removed"],
             "c": 1,
             "why": "At each level the sift first compares the two children with each "
                    "other to find the smaller, then compares the descending key with "
                    "that child: two comparisons per level. The sift itself runs once. "
                    "&ldquo;Two subtrees&rdquo; is true of every node and is not what the "
                    "factor counts; the move-then-remove is a constant amount of work, "
                    "not a doubling."},
            {"q": "Inserting a key into a heap of `6` elements, you make `1` comparison and no swaps. What happened?",
             "a": ["The key was smaller than everything and went to the root",
                   "The key was at least its parent, so the sift stopped immediately",
                   "The heap property was violated and the insert failed",
                   "The heap was already sorted, so no work was needed"],
             "c": 1,
             "why": "One comparison and no swap means the new key was compared with its "
                    "parent and found to be at least as large, so it stays where it "
                    "landed and the property already holds everywhere. A key smaller than "
                    "everything sifts all the way up, costing `⌊log₂ 7⌋ = 2` comparisons "
                    "and `2` swaps here. Nothing failed, and a heap being sorted is "
                    "neither necessary nor usual."},
        ],
        "mistakes": [
            ("Expecting the array, or any prefix of it, to be in order",
             "`1 3 2 6 8 7 4 9` is a valid heap in which `3` precedes `2`. Only "
             "root-to-leaf paths are ordered. The habit to build is to check the property "
             "node by node rather than to scan the array and feel uneasy, and the "
             "argument to remember is that a sorted array is a much stronger object than "
             "a heap and costs more to produce."),
            ("Sifting down without first comparing the two children",
             "Swapping with the left child because it happens to be smaller than the "
             "descending key gives a tree that satisfies the property on that one edge "
             "and violates it on the other. Find the smaller child, then compare. This is "
             "also where the factor of two in the bound comes from, so an implementation "
             "missing it is both wrong and suspiciously fast."),
            ("Mixing the two index conventions",
             "`2i` and `2i + 1` is correct when positions start at `1`; `2i + 1` and "
             "`2i + 2` is correct when they start at `0`. Applying the first formula to a "
             "zero-based array sends you to a cousin instead of a child, and the resulting "
             "tree usually still satisfies the property somewhere, so the bug survives a "
             "casual check. Decide once, write it down, and read the lab&rsquo;s array "
             "labels before trusting a position."),
        ],
        "standard": ("Finish when a heap that is obviously not sorted stops looking broken.",
                     "You should be able to insert and extract by hand on a drawn heap "
                     "without losing completeness, find the smaller child before comparing, "
                     "convert between the array and the tree in both index conventions, and "
                     "quote the comparison bound for each operation with the reason the "
                     "extraction&rsquo;s bound carries a factor of two."),
        "note": (
            "Inserting `n` keys one at a time costs `O(n log n)`, and a heap can be built "
            "from an arbitrary array much faster than that. &ldquo;Building a Heap in "
            "Linear Time&rdquo; sifts down from the last internal node to the root "
            "instead, and the sum `Σ ⌈n/2ʰ⁺¹⌉·h` that prices it is under `2n` &mdash; "
            "evaluated exactly, beside both methods running with counters on the same "
            "input."
        ),
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "building-a-heap-in-linear-time",
        "title": "Building a Heap in Linear Time",
        "module": "Heaps",
        "one_line": "Evaluate `Σ ⌈n/2ʰ⁺¹⌉·h` exactly for a given `n` and say why `n` inserts cost more than one bottom-up pass.",
        "summary": (
            "Sifting down from the last internal node to the root turns any array into a "
            "heap, and it costs `Σ ⌈n/2ʰ⁺¹⌉·h`, which is under `2n` &mdash; not "
            "`n log n`. The reason is that height is not shared out equally: half the "
            "nodes are leaves and sift no distance at all. At `n = 31` the sum is `26` "
            "against `2n = 62`, and inserting the same keys one at a time swaps `98` "
            "times."
        ),
        "key": [
            "Floyd's build     for i = ⌊n/2⌋ down to 1:  sift-down(i)",
            "",
            "Σ ⌈n/2ʰ⁺¹⌉·h  <  n · Σ h/2ʰ  =  2n            the sum converges",
            "",
            "n = 31:   16·0 + 8·1 + 4·2 + 2·3 + 1·4  =  26        2n = 62",
            "measured   Floyd 26 swaps        n inserts 98 swaps",
            "           on keys arriving in decreasing order",
        ],
        "key_label": "The bottom-up pass, its exact sum, and both methods measured",
        "concepts_intro": (
            "One counting idea, and it is the reason a whole family of bounds is smaller "
            "than it looks: when a cost varies across the things you are summing over, "
            "multiplying the worst cost by the count throws the answer away."
        ),
        "concepts": [
            ("Most nodes are near the bottom, so most sifts are short",
             "In a complete tree on `n` nodes, about `n/2` are leaves with height `0`, "
             "about `n/4` have height `1`, about `n/8` have height `2`. The number of "
             "nodes at height `h` is at most `⌈n/2ʰ⁺¹⌉`, and it halves as the cost "
             "doubles. That is the entire reason the total is linear, and it is a fact "
             "about the shape of the tree rather than about heaps."),
            ("A sum of costs is not the count times the worst cost",
             "`n` nodes and `log n` levels invites `n log n`, and the step that is wrong "
             "is charging every node the height of the tree. Only one node has that "
             "height. Multiplying the maximum by the count is an upper bound and it is "
             "off by a factor of `log n` here, which is the difference between an "
             "algorithm that is worth having and one that is not."),
            ("The direction of the pass is what makes it work",
             "Sifting DOWN from the bottom up is correct because when node `i` is "
             "processed, both of its subtrees are already heaps, so one sift fixes it. "
             "Sifting UP from the top down would be the insertion method in disguise and "
             "would cost the same as it. The saving is not a trick of implementation; it "
             "is a different order of operations."),
        ],
        "read_title": "Floyd's pass, the sum that prices it, and both methods counted",
        "read_intro": "Why sifting down from the middle is correct, the exact evaluation of the sum at n = 31, and what the two methods actually measure.",
        "body": [
            ("p", "Every position past `⌊n/2⌋` is a leaf, and a leaf is a one-element "
                  "heap already. So a heap can be built by sifting down at every position "
                  "from `⌊n/2⌋` back to `1`, in that order. The order is what makes it "
                  "correct: when the pass reaches node `i`, everything below `i` has "
                  "already been processed, so both subtrees of `i` are heaps and a single "
                  "sift-down from `i` puts `i` where it belongs."),
            ("def", ("Floyd's build-heap",
                     "Given an array of `n` keys in any order, for `i` from `⌊n/2⌋` down "
                     "to `1`, sift down at position `i`. The result is a heap, and the "
                     "cost is the total distance sifted.",
                     "The loop touches only the internal nodes, since leaves have nothing "
                     "to sift past. The bound is about the total distance, so it needs "
                     "the number of nodes at each height and not merely the height of the "
                     "tree.")),
            ("thm", ("Floyd's build-heap costs at most 2n",
                     "A node at height `h` sifts at most `h` levels, and a complete tree "
                     "on `n` nodes has at most `⌈n/2ʰ⁺¹⌉` nodes at height `h`. So the "
                     "total distance sifted is at most `Σ ⌈n/2ʰ⁺¹⌉·h`, summed over "
                     "`h = 0` to `⌊log₂ n⌋`.",
                     "Dropping the ceilings, that is at most `n · Σ h/2ʰ⁺¹`, and "
                     "`Σ h/2ʰ` over all `h ≥ 0` converges to `2`. So the sum is under "
                     "`2n`, and the build is `Θ(n)`: linear in the number of keys, with "
                     "no logarithm anywhere in it.")),
            ("p", "The `Σ h/2ʰ = 2` step is the only piece of analysis being imported, "
                  "and it is the standard arithmetico-geometric sum &mdash; "
                  "differentiate the geometric series, or notice that the sum `S` "
                  "satisfies `S = S/2 + 1`. Discrete Mathematics&rsquo; &ldquo;Recursion "
                  "Trees and Amortised Analysis&rdquo; is where sums of this shape are "
                  "collected; nothing else here needs it."),
            ("h3", "The sum, evaluated exactly"),
            ("p", "The lab evaluates the sum term by term rather than quoting the `2n` "
                  "bound, because the terms are where the insight is. At `n = 31` the "
                  "complete tree has five levels and the nodes are distributed like this:"),
            ("math", [
                "height h    nodes ⌈31/2ʰ⁺¹⌉    h · nodes",
                "",
                "   0              16                  0        the leaves sift nowhere",
                "   1               8                  8",
                "   2               4                  8",
                "   3               2                  6",
                "   4               1                  4        the root, alone",
                "",
                "  total                               26       and 2n = 62",
                "  per element                      26/31       under one swap each",
            ]),
            ("p", "Sixteen of the thirty-one nodes contribute nothing at all, and the "
                  "two heights that contribute most are `1` and `2` &mdash; not the "
                  "height of the tree. The total is `26`, which is `26/31` of a swap per "
                  "element. Compare that with what `n log₂ n` would have suggested: "
                  "`31 × 4` is `124`, nearly five times as much, and the error is entirely "
                  "in charging every node the root&rsquo;s height."),
            ("h3", "Both methods, on the same input"),
            ("p", "Now the measurement. Feed both methods the keys `31, 30, …, 1` "
                  "&mdash; decreasing order, which is the worst case for insertion "
                  "because every arriving key is smaller than everything present and "
                  "sifts to the root:"),
            ("math", [
                "n = 31, keys arriving in decreasing order",
                "",
                "                          swaps    comparisons",
                "Floyd's build                26             52",
                "n inserts one at a time      98             98",
                "",
                "exact sum Σ ⌈n/2ʰ⁺¹⌉·h       26        the bound Floyd's swaps hit",
                "",
                "same keys, arriving in increasing order",
                "Floyd's build                 0             30",
                "n inserts one at a time       0             30        identical",
            ]),
            ("p", "Floyd&rsquo;s swap count is `26`, which is the sum exactly: this "
                  "input makes every internal node sift its full height, so the bound is "
                  "attained rather than merely respected. Insertion swaps `98` times on "
                  "the same keys, a factor of `3.8`. And on keys already in increasing "
                  "order both methods swap zero times and make the same thirty "
                  "comparisons, producing the same heap &mdash; a measurement taken there "
                  "would show no difference between a linear algorithm and a "
                  "linearithmic one."),
            ("p", "Two things in that table are worth being careful about. First, the "
                  "exact sum bounds the <em>swaps</em>, not the comparisons: "
                  "Floyd&rsquo;s comparisons are `52`, about twice its swaps, because "
                  "each level of a sift-down compares the two children before comparing "
                  "with the parent. The `2n` bound is a bound on distance sifted. "
                  "Second, on a shuffled input Floyd swaps `21` &mdash; below the sum, "
                  "because a random arrangement does not make every node sift its full "
                  "height. The sum is the worst case; the counter shows one case."),
        ],
        "lab": ("heap", {
            "mode": "build",
            "preset": "worst-for-inserts",
            "panel_title": "Both methods, and the sum evaluated term by term",
            "panel_intro": "Set the size and the arrival order. Floyd&rsquo;s bottom-up pass "
                           "and `n` separate insertions both run on the same array with "
                           "counters, and `Σ ⌈n/2ʰ⁺¹⌉·h` is evaluated term by term beside "
                           "them &mdash; exactly, as a sum of integers, with the per-element "
                           "figure as an exact fraction. Switch the order to increasing and "
                           "watch the difference between the two methods vanish.",
        }),
        "steps_title": "Pricing a build",
        "steps_intro": "The sum before the code. Evaluating it once at a small n is what makes the linear bound believable rather than memorised.",
        "steps": [
            ("Count the nodes at each height, not the levels",
             "`⌈n/2ʰ⁺¹⌉` for `h = 0, 1, 2, …` up to `⌊log₂ n⌋`. Write the column out. "
             "The fact that it halves while the cost doubles is the whole argument, and "
             "it is invisible if you only write down the height of the tree."),
            ("Multiply and add, exactly",
             "`h` times the node count, summed. Keep it as an integer; there is no "
             "rounding anywhere in this sum. Then compare it with `2n`, and with "
             "`n⌊log₂ n⌋` to see what the loose bound would have cost you."),
            ("Run the pass from ⌊n/2⌋ down to 1",
             "Sifting down, not up, and starting at the last internal node. Going the "
             "other way is the insertion method: it still produces a heap and it costs "
             "the insertion method&rsquo;s price, which is the point of the comparison."),
            ("Choose the input order deliberately",
             "Decreasing order is the worst case for insertion and makes Floyd&rsquo;s "
             "swap count hit the sum. Increasing order makes both methods do nothing. A "
             "measurement on already-sorted input cannot distinguish the two algorithms "
             "at all, and that is the trap this lab is arranged to expose."),
        ],
        "worked": {
            "title": "n = 15, by hand and then measured",
            "intro": [
                "A smaller tree, where the whole sum fits on four lines and the two "
                "measured counts can be checked against it."
            ],
            "lines": [
                "n = 15,  a perfect tree of height 3",
                "",
                "h    nodes ⌈15/2ʰ⁺¹⌉    h · nodes",
                "0           8                  0",
                "1           4                  4",
                "2           2                  4",
                "3           1                  3",
                "                              ---",
                "sum                            11          2n = 30",
                "",
                "measured, keys 15 14 … 1 (decreasing):",
                "  Floyd            11 swaps,  22 comparisons",
                "  15 inserts       34 swaps,  34 comparisons",
                "",
                "measured, keys 1 2 … 15 (increasing):",
                "  Floyd             0 swaps,  14 comparisons",
                "  15 inserts        0 swaps,  14 comparisons",
                "",
                "per element   11/15   <   1 swap each",
            ],
            "after": [
                "Floyd&rsquo;s `11` swaps equal the sum `11` exactly on the decreasing "
                "input, and its `22` comparisons are twice that, one pair per level "
                "sifted. The insertion method pays `34` on the same keys: three times as "
                "much, at a size where `n⌊log₂ n⌋` is `45` and `2n` is `30`.",
                "The increasing-order rows are the honest half of the exercise. Both "
                "methods swap nothing and compare fourteen times, and they produce the "
                "same heap, because the array was already one. Anyone who measured there "
                "and concluded the two builds are equivalent would have a perfectly "
                "reproducible result and a false belief, which is what this course means "
                "by a count not being a bound.",
                "For a faded rehearsal, do `n = 7`. The supplied first line is that the "
                "node counts are `4, 2, 1` at heights `0, 1, 2`. Finish the sum, predict "
                "Floyd&rsquo;s swap count on decreasing input, and then check it in the "
                "lab &mdash; it is `4`, against `10` for seven insertions and `2n = 14`. "
                "Then state what the sum is a bound on, in the lab&rsquo;s own columns, "
                "and what it is not.",
            ],
        },
        "quiz_title": "The sum and the two methods",
        "quiz": [
            {"q": "At `n = 31`, what is `Σ ⌈n/2ʰ⁺¹⌉·h`?",
             "a": ["`26`", "`31`", "`62`", "`124`"],
             "c": 0,
             "why": "`16·0 + 8·1 + 4·2 + 2·3 + 1·4` = `0 + 8 + 8 + 6 + 4` = `26`. `62` is "
                    "`2n`, the bound the sum falls under. `124` is `n⌊log₂ n⌋`, what you "
                    "get by charging every node the height of the tree &mdash; the very "
                    "step the lesson exists to refute. `31` is `n`."},
            {"q": "Why is Floyd&rsquo;s build linear when it performs about `n/2` sift-downs each costing up to `log n`?",
             "a": ["Because the sifts can be done in parallel",
                   "Because the number of nodes at height `h` falls as fast as the cost at height `h` rises",
                   "Because sifting down is cheaper per level than sifting up",
                   "Because the array is already nearly a heap"],
             "c": 1,
             "why": "There are about `n/2ʰ⁺¹` nodes at height `h` and each costs at most "
                    "`h`, so the terms are `h/2ʰ⁺¹` times `n` and that series converges "
                    "to `1`. Nothing is parallel. A level of sifting down actually costs "
                    "two comparisons where sifting up costs one. And the input array is "
                    "arbitrary &mdash; the lab&rsquo;s opening order is the worst one for "
                    "insertion."},
            {"q": "On keys arriving in increasing order at `n = 31`, both methods swap `0` times and make `30` comparisons. What does that measurement establish?",
             "a": ["That the two methods have the same cost",
                   "That Floyd&rsquo;s build is linear",
                   "Nothing about their costs in general: the input was already a heap",
                   "That insertion is linear on sorted input, which is its worst case"],
             "c": 2,
             "why": "An increasing array already satisfies the heap property, so neither "
                    "method has anything to do and the two counts coincide. It is the "
                    "clearest example on the course of a reproducible measurement that "
                    "supports no claim at all. Increasing order is also insertion&rsquo;s "
                    "<em>best</em> case, not its worst &mdash; the worst is decreasing, "
                    "where it swaps `98` times."},
        ],
        "mistakes": [
            ("Charging every node the height of the tree",
             "`n` nodes times `log n` levels is `n log n`, and it is wrong because only "
             "one node is at the top. Sixteen of the thirty-one nodes at `n = 31` "
             "contribute zero, and the two biggest contributions come from heights `1` "
             "and `2`. Any time a cost varies over the things being summed, write the "
             "distribution down before multiplying."),
            ("Reading the exact sum as a bound on comparisons",
             "`26` at `n = 31` bounds the distance sifted, and therefore the swaps. "
             "Floyd&rsquo;s comparisons on the same input are `52`, because finding the "
             "smaller child costs a comparison at every level too. Both are linear, the "
             "constants differ by about two, and quoting the sum as a comparison count is "
             "off by that factor."),
            ("Concluding from one input that the two builds are equivalent",
             "On already-increasing keys both methods swap zero times and make the same "
             "comparisons. On decreasing keys it is `26` against `98`. The first "
             "measurement is real, repeatable, and says nothing; the difference between "
             "`Θ(n)` and `Θ(n log n)` is a statement about all inputs and the lab can "
             "only ever run one."),
        ],
        "standard": ("Finish when `n` operations of `O(log n)` each stops automatically suggesting `n log n`.",
                     "You should be able to write the node-count column for a stated `n`, "
                     "evaluate the sum exactly as an integer, say which measured column it "
                     "bounds and which it does not, and name an input order on which the "
                     "two build methods are indistinguishable and explain why that is not "
                     "evidence about either."),
        "note": (
            "A heap answers &ldquo;which is smallest&rdquo; and refuses &ldquo;is `k` "
            "present&rdquo;. The next three lessons take a structure that answers "
            "membership in about one step and refuses order: &ldquo;Hashing with "
            "Chaining&rdquo; computes the expected cost of a lookup exactly, as a "
            "fraction, and then produces the key set on which the same table degenerates "
            "to a linked list."
        ),
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "hashing-with-chaining",
        "title": "Hashing with Chaining",
        "module": "Hash tables",
        "one_line": "Compute `α` and the expected search cost as exact fractions, then build the key set that degenerates `h(k) = k mod m`.",
        "summary": (
            "Under simple uniform hashing the expected length of a chain is the load "
            "factor `α = n/m`, so a search costs `Θ(1 + α)` expected. That is an "
            "average over an assumption about the keys, and the worst case is `Θ(n)`: no "
            "hash function removes it. At `m = 8` and `n = 20` the lab measures `2.3` "
            "probes on random keys and `10.5` on a key set with the same `α`."
        ),
        "key": [
            "α = n/m                    the load factor: keys per slot",
            "chaining      h(k) = k mod m,  collisions live in a list at the slot",
            "",
            "expected, unsuccessful      α                            = 5/2 at m=8, n=20",
            "expected, successful        1 + α/2 − α/2m               = 67/32",
            "so a search is             Θ(1 + α) expected,  Θ(n) worst case",
            "",
            "measured at α = 5/2:   random keys 23/10       every key ≡ 0 (mod m)  21/2",
        ],
        "key_label": "The load factor, the two expectations, and the same load twice",
        "concepts_intro": (
            "Three statements, and the third is the one that turns a slogan into an "
            "engineering fact. The first two are arithmetic; the third is what the "
            "arithmetic assumed."
        ),
        "concepts": [
            ("The load factor is the answer, and it can exceed 1",
             "`α = n/m` is the average chain length by definition: `n` keys shared over "
             "`m` slots. With chaining there is no upper limit on `α` &mdash; twenty keys "
             "in eight slots is `α = 5/2` and the table works fine, just more slowly. "
             "A search costs one probe to find the slot plus a walk along the chain, "
             "which is `Θ(1 + α)`, and the `1` matters precisely when `α` is small."),
            ("The expectation is over an assumption about the keys, not over the table",
             "Simple uniform hashing says each key is equally likely to hash to each "
             "slot, independently of the others. That is an assumption about the input, "
             "and the hash function does not enforce it: `h(k) = k mod m` sends every "
             "multiple of `m` to slot `0` no matter how clever the rest of the table is. "
             "When the assumption fails the expectation says nothing."),
            ("The worst case is a linked list, and it cannot be engineered away",
             "For any fixed hash function into `m` slots there is a set of `n` keys that "
             "all collide, because there are far more keys than slots. So the worst-case "
             "search is `Θ(n)`, permanently. The honest statement is two-part &mdash; "
             "`Θ(1 + α)` expected, `Θ(n)` worst &mdash; and dropping the second half is "
             "how &ldquo;hash tables are `O(1)`&rdquo; gets said."),
        ],
        "read_title": "The load factor, the expected chain, and the key set that defeats the table",
        "read_intro": "Where the two expectations come from, the exact fractions at m = 8, and two key sets with the same load and very different costs.",
        "body": [
            ("def", ("Hashing with chaining",
                     "A table of `m` slots and a hash function `h` from keys to "
                     "`{0, …, m−1}`. Each slot holds a linked list &mdash; a "
                     "<strong>chain</strong> &mdash; of every key that hashed to it. "
                     "Insert prepends to the chain; search computes `h(k)` and walks the "
                     "chain; delete unlinks. The <strong>load factor</strong> is "
                     "`α = n/m`, the number of keys divided by the number of slots.",
                     "The division hash function is `h(k) = k mod m`. It is the one this "
                     "lesson uses, because its failure mode is arithmetic rather than "
                     "mysterious.")),
            ("thm", ("Expected search cost under simple uniform hashing",
                     "Assume each key is equally likely to hash to any of the `m` slots, "
                     "independently. Then an unsuccessful search examines `α` keys in "
                     "expectation, and a successful search examines "
                     "`1 + α/2 − α/2m`. Both are `Θ(1 + α)` once the constant probe for "
                     "the slot itself is counted.",
                     "The unsuccessful case is immediate: the search walks the whole "
                     "chain at `h(k)`, whose expected length is `n/m = α` by linearity "
                     "of expectation over the `n` keys. The successful case is smaller "
                     "than `α` because the search stops at the key it wants and, on "
                     "average, that key is halfway along &mdash; and the correction "
                     "`−α/2m` is because the key being searched for is itself one of the "
                     "`n`, so it does not collide with itself.")),
            ("p", "Linearity of expectation is doing all the work in the first half, and "
                  "it is imported from Discrete Mathematics&rsquo; &ldquo;Linearity of "
                  "Expectation&rdquo;: the expected number of keys in a given slot is the "
                  "sum over keys of the probability that key lands there, which is "
                  "`n × 1/m`. No independence is needed for that step, only for the "
                  "assumption to be stated the way it usually is."),
            ("h3", "The fractions, at a table small enough to draw"),
            ("p", "Twenty keys into eight slots. The lab computes every quantity as an "
                  "exact fraction over big integers, never as a decimal that is nearly "
                  "one, and then counts the probes an actual search makes:"),
            ("math", [
                "m = 8,  n = 20        α = 20/8 = 5/2 = 2.5",
                "",
                "expected unsuccessful       α          =  5/2      =  2.5",
                "expected successful    1 + α/2 − α/2m",
                "                     = 1 + 5/4 − 5/32 = 67/32     =  2.09375",
                "",
                "measured, twenty keys drawn from the stream:",
                "  chains        4  5  1  2  0  1  4  3        longest 5, one empty",
                "  mean probes over the twenty searches        23/10 = 2.3",
            ]),
            ("p", "`23/10` against an expected `67/32`: the measurement came in above "
                  "the expectation, which is ordinary at twenty keys, and the two numbers "
                  "are close. The chain lengths `4, 5, 1, 2, 0, 1, 4, 3` add to twenty "
                  "and average `2.5`, as they must &mdash; the average chain length is "
                  "`α` by arithmetic, not by luck. What varies is how unevenly the keys "
                  "landed, and the longest chain here is `5`, twice the average."),
            ("h3", "The same load factor, and a table that has become a list"),
            ("p", "Now keep `m = 8` and `n = 20` and choose the keys to be "
                  "`8, 16, 24, …, 160` &mdash; every one a multiple of `8`. Each of them "
                  "hashes to slot `0`:"),
            ("math", [
                "m = 8,  n = 20,  keys 8 16 24 … 160         α = 5/2, unchanged",
                "",
                "chains       20  0  0  0  0  0  0  0        longest 20, seven empty",
                "mean probes over the twenty searches        21/2 = 10.5",
                "",
                "same α,  expected 67/32 ≈ 2.09,  measured 10.5      a factor of 5",
            ]),
            ("p", "The load factor did not move. The expectation did not move. The "
                  "measured cost went up by a factor of five, and it is not a fluke or a "
                  "bad seed &mdash; it is the worst case, reached deliberately, by keys "
                  "that a real application produces all the time: record identifiers "
                  "spaced by a round number, addresses aligned to a power of two, prices "
                  "in whole units. The table is now a linked list with an index on the "
                  "front of it."),
            ("p", "So the quotable statement about a hash lookup has two halves and "
                  "needs both: <strong>`Θ(1 + α)` expected under simple uniform hashing, "
                  "`Θ(n)` in the worst case, for any fixed hash function</strong>. "
                  "System Design&rsquo;s &ldquo;Hash vs Tree for Ranges&rdquo; is where "
                  "those same two facts decide a disk index rather than an in-memory one, "
                  "and there the second half is joined by a third problem: a hash index "
                  "cannot answer a range query at all, at any load factor."),
        ],
        "lab": ("hash", {
            "mode": "chaining",
            "preset": "eight-slots",
            "panel_title": "Chains drawn, searches run, and the same load factor twice",
            "panel_intro": "Set the number of slots, the hash rule and the key set &mdash; "
                           "drawn from the stream, spaced by `m`, or typed in yourself. Every "
                           "chain is drawn, every key is then searched for with a probe "
                           "counter, and `α` and both expectations are printed as exact "
                           "fractions. Switch the key set to the stride and watch the load "
                           "factor stay still while the measured cost multiplies.",
        }),
        "steps_title": "Costing a hash table",
        "steps_intro": "Compute the expectation first, measure second, and then try to break it &mdash; in that order, because the third step is meaningless without the first two.",
        "steps": [
            ("Compute α, and keep it a fraction",
             "`n/m`, exactly. `20/8` is `5/2`, not `2.5` and certainly not `2`. Every "
             "other quantity on the page is built from `α`, and a rounded load factor "
             "puts a rounding error into all of them."),
            ("Write both expectations down before looking at the table",
             "`α` for an unsuccessful search, `1 + α/2 − α/2m` for a successful one. "
             "They differ, they are both `Θ(1 + α)`, and knowing which one a measurement "
             "should be compared with is half of reading the lab correctly."),
            ("Measure, and look at the longest chain as well as the mean",
             "The mean is pinned to `α` by arithmetic and tells you nothing about "
             "spread. The longest chain is the cost of the unluckiest key, and at "
             "`m = 8, n = 20` it is `5` &mdash; twice the mean, on keys that were drawn "
             "at random."),
            ("Now choose keys to defeat the hash function",
             "For `h(k) = k mod m`, use multiples of `m`. The load factor will not move "
             "and the measured cost will. This step is the lesson: a structure whose "
             "guarantee is an expectation over the input has to be tested against the "
             "input that expectation assumes away."),
        ],
        "worked": {
            "title": "m = 16, n = 8, both ways",
            "intro": [
                "A half-loaded table, where the fractions are small enough to check by "
                "hand and the degenerate set is only eight keys long."
            ],
            "lines": [
                "m = 16,  n = 8        α = 8/16 = 1/2",
                "",
                "expected unsuccessful      α  =  1/2  =  0.5",
                "expected successful   1 + α/2 − α/2m",
                "                    = 1 + 1/4 − 1/64",
                "                    = 79/64  =  1.234375",
                "",
                "measured, keys from the stream:",
                "  chains    0 1 0 1 0 0 1 0 0 1 1 0 2 1 0 0",
                "  longest 2,  nine slots empty",
                "  mean probes   9/8  =  1.125",
                "",
                "same m, same n, keys 16 32 48 64 80 96 112 128:",
                "  chains    8 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
                "  longest 8,  fifteen slots empty",
                "  mean probes   9/2  =  4.5",
            ],
            "after": [
                "`9/8` against an expected `79/64`: `1.125` measured, `1.234` expected, "
                "and the measurement came in slightly under. At eight keys that is "
                "nothing but variance, and it is worth noticing that the measurement can "
                "land on either side &mdash; a lab that always confirmed the expectation "
                "would be reporting the expectation.",
                "The stride set quadruples the measured cost at the same `α = 1/2`. On a "
                "half-loaded table. The expected cost of a successful search on eight "
                "keys in one chain is `(1 + 2 + … + 8)/8 = 9/2`, which is exactly what "
                "was measured, because there is no randomness left: every search walks a "
                "known list.",
                "For a faded rehearsal, set `m = 8` and `n = 8` so that `α = 1`. The "
                "supplied first step is the expectation: `1 + 1/2 − 1/16 = 23/16 = "
                "1.4375`. Predict the mean probe count for random keys, then measure it; "
                "then switch to the stride set and predict `(1 + 2 + … + 8)/8` before "
                "measuring that. Say which of your four numbers were computed from a "
                "definition and which were counted.",
            ],
        },
        "quiz_title": "Load factor and expectation",
        "quiz": [
            {"q": "A chaining table has `m = 8` slots and `n = 20` keys. What is the expected number of keys examined by an unsuccessful search?",
             "a": ["`5/2`", "`67/32`", "`20`", "`8/20`"],
             "c": 0,
             "why": "An unsuccessful search walks the whole chain, whose expected length "
                    "is `α = n/m = 5/2`. `67/32` is the successful case, which is smaller "
                    "because the search stops at the key it finds. `20` is the worst case, "
                    "not the expectation. `8/20` is `m/n`, the load factor upside down."},
            {"q": "Two key sets are inserted into the same `m = 8` table, twenty keys each. One measures `2.3` probes per search and the other `10.5`. What must be true of their load factors?",
             "a": ["The second has a load factor four times the first",
                   "They are equal: `α = 5/2` for both",
                   "The second exceeds `1` and the first does not",
                   "Nothing: the load factor is not determined by `m` and `n`"],
             "c": 1,
             "why": "`α` is `n/m` and both have twenty keys in eight slots, so both are "
                    "`5/2`. That is the point of the pair: the load factor is identical "
                    "and the measured cost differs by a factor of five, because one key "
                    "set satisfies the uniformity assumption and the other is every "
                    "multiple of `8`. The load factor is completely determined by `n` and "
                    "`m`."},
            {"q": "Why can no choice of hash function make the worst-case search better than `Θ(n)`?",
             "a": ["Because chains are linked lists and lists are slow",
                   "Because there are more possible keys than slots, so some set of `n` keys all collide",
                   "Because `α` can exceed `1` with chaining",
                   "Because `h(k) = k mod m` is a bad hash function"],
             "c": 1,
             "why": "For any fixed function into `m` slots, the pigeonhole principle "
                    "gives a slot with many preimages, and an adversary who knows the "
                    "function can pick `n` keys from it. The linked list is an "
                    "implementation detail &mdash; the collisions are the problem. `α > 1` "
                    "is normal for chaining and not the issue. And the argument applies to "
                    "every fixed hash function, good or bad, which is why the fix is a "
                    "randomly chosen one."},
        ],
        "mistakes": [
            ("Saying a hash table is `O(1)` without the two qualifications",
             "It is `Θ(1 + α)` <em>expected</em>, <em>under an assumption about the "
             "keys</em>, and `Θ(n)` in the worst case. The short version is true of the "
             "cases most people meet and is not a bound. The habit worth building is to "
             "say the expectation and the worst case in the same breath, because a system "
             "whose input an adversary chooses will meet the second one."),
            ("Reading the load factor as a measurement",
             "`α = n/m` is arithmetic, and so is the mean chain length, which equals `α` "
             "on every key set whatsoever. Twenty keys in eight slots average `2.5` per "
             "chain whether they are spread evenly or all in one place. The quantity that "
             "distinguishes those two tables is the longest chain, and it is `5` in one "
             "and `20` in the other."),
            ("Testing a hash table only on keys that suit it",
             "Random keys, sequential keys and keys drawn from a real trace all behave "
             "roughly like the expectation for `h(k) = k mod m`. Multiples of `m` do not, "
             "and they are not exotic: they arise from aligned addresses, round-numbered "
             "identifiers and strides in a loop. A table that has never been run on a "
             "degenerate set has not been tested, and the lab supplies one."),
        ],
        "standard": ("Finish when you can state the cost of a hash lookup in two halves without being prompted for the second.",
                     "You should be able to compute `α` and both expectations as exact "
                     "fractions, say which expectation a given measurement should be "
                     "compared with, produce a key set that sends every key to one slot "
                     "for `h(k) = k mod m`, and quote `Θ(1 + α)` expected and `Θ(n)` worst "
                     "case as a single two-part statement."),
        "note": (
            "Chaining pays for its collisions in pointers and never runs out of room. "
            "The alternative keeps everything inside the table and has a subtler problem: "
            "&ldquo;Open Addressing and Linear Probing&rdquo; shows why a deletion must "
            "leave a mark rather than a hole &mdash; the lab names the keys that go "
            "missing when it does not &mdash; and why clustering makes an unsuccessful "
            "search cost far more than `1 + α`."
        ),
    },
    # ---------------------------------------------------------------- 06
    {
        "slug": "open-addressing-and-linear-probing",
        "title": "Open Addressing and Linear Probing",
        "module": "Hash tables",
        "one_line": "Insert, search and delete in a probing table leaving tombstones correctly, and read the counted probes against Knuth’s curve.",
        "summary": (
            "With every key inside the table, a search stops at the first empty slot "
            "&mdash; so a deletion that empties a slot cuts every probe chain running "
            "through it, and keys already in the table become unreachable. The lab names "
            "them. Linear probing also clusters, which makes an unsuccessful search cost "
            "about `½(1 + 1/(1−α)²)` rather than `1 + α`: an approximation, printed "
            "beside probes that were counted."
        ),
        "key": [
            "open addressing    every key in a slot;  on collision, probe the next one",
            "linear probing     h(k, i) = (h(k) + i) mod m",
            "",
            "delete             mark the slot DEAD, do not empty it",
            "search stops at a TRUE empty, walks past a dead one",
            "",
            "Knuth, unsuccessful   ½(1 + 1/(1−α)²)     an approximation, not a count",
            "α = 11/16:  counted 5 probes,  curve 5.62      α must stay below 1",
        ],
        "key_label": "The probe rule, the tombstone rule, and the one figure here that rounds",
        "concepts_intro": (
            "Three ideas, and the second is the one that costs people a data-loss bug: "
            "in a probing table a deletion is not the opposite of an insertion."
        ),
        "concepts": [
            ("The probe sequence is the structure",
             "A key does not live at `h(k)`; it lives at the first slot in its probe "
             "sequence `h(k), h(k)+1, h(k)+2, …` that was free when it arrived. A search "
             "re-walks that sequence and stops at the first empty slot, because an empty "
             "slot means the key would have been put there. Everything about probing "
             "follows from that stopping rule, including the deletion problem."),
            ("A deletion must leave a mark, not a hole",
             "Emptying a slot creates a stopping point in the middle of other keys&rsquo; "
             "probe sequences, and every key beyond it becomes unreachable &mdash; still "
             "in the table, never found again. The fix is a <strong>tombstone</strong>: a "
             "slot marked dead, which a search walks past and an insertion may reuse. The "
             "lab deletes eight keys from a table of twenty-two and reports which three "
             "of the survivors go missing when the mark is omitted."),
            ("Clustering is why linear probing costs more than the load factor suggests",
             "Occupied slots gather into runs, and a long run is more likely to catch the "
             "next key, which makes it longer. Chaining has no such effect: its chains are "
             "independent. So the expected unsuccessful search is not `1 + α`; the "
             "standard analysis gives about `½(1 + 1/(1−α)²)`, which blows up as `α` "
             "approaches `1` &mdash; and with everything inside the table, `α` cannot "
             "exceed `1` at all."),
        ],
        "read_title": "Probing, deleting, and the one curve on this course that is a model",
        "read_intro": "The probe rule, the tombstone rule with the keys that go missing without it, and the approximation printed beside the counts.",
        "body": [
            ("def", ("Open addressing",
                     "Every key is stored in a slot of the table itself; there are no "
                     "chains. A key `k` has a <strong>probe sequence</strong> "
                     "`h(k, 0), h(k, 1), …` covering all `m` slots. Insert walks it to "
                     "the first free slot. Search walks it and stops when it finds `k` or "
                     "reaches an empty slot. Since every key occupies a slot, `n ≤ m` and "
                     "so `α ≤ 1`.",
                     "<strong>Linear probing</strong> is `h(k, i) = (h(k) + i) mod m`: "
                     "try the next slot, and the next. <strong>Double hashing</strong> "
                     "uses a second hash function for the step, which breaks up the runs.")),
            ("p", "The lab offers only power-of-two table sizes, and the reason is worth "
                  "knowing: the double-hashing step it computes is always odd, and an odd "
                  "step is coprime with `m` &mdash; so the probe sequence reaches every "
                  "slot &mdash; exactly when `m` is a power of two. At `m = 13` a step "
                  "could share a factor with the table size and the sequence would miss "
                  "slots, which is a silently broken table rather than a slow one."),
            ("h3", "Deletion, and the keys that disappear"),
            ("p", "Search stops at the first empty slot. So consider a key `k` whose "
                  "probe sequence is `5, 6, 7` and which ended up in slot `7` because "
                  "`5` and `6` were taken. Delete the key in slot `6` by emptying it, and "
                  "now a search for `k` probes slot `5`, probes slot `6`, finds it empty, "
                  "and reports that `k` is not in the table. `k` is in slot `7`. It will "
                  "never be found again."),
            ("def", ("Tombstone",
                     "A slot may be <strong>empty</strong>, <strong>occupied</strong>, or "
                     "<strong>dead</strong> &mdash; a tombstone left by a deletion. A "
                     "search treats a dead slot as occupied by something else and keeps "
                     "going; an insertion treats it as free and may reuse it. Only an "
                     "empty slot stops a search.",
                     "The cost is that tombstones accumulate: they lengthen searches "
                     "without holding keys, so a table with many deletions eventually "
                     "needs rebuilding even though its load factor looks healthy.")),
            ("example", ("Three keys, lost and recovered",
                         "The lab fills a table of `32` slots with `22` keys, deletes "
                         "eight of them and then searches for the fourteen that remain. "
                         "With tombstones, all fourteen are found. Deleting by emptying "
                         "the slot instead loses <strong>three</strong> of them, and the "
                         "panel prints their keys. Nothing about the table looks wrong: "
                         "the load factor is right, the slots are consistent, and three "
                         "records are gone.")),
            ("h3", "Clustering, and a number that is a model rather than a count"),
            ("p", "Now the cost. A table of `32` slots aimed at seven tenths full ends "
                  "up with `22` keys, so `α = 11/16 = 0.6875`. The lab then searches for "
                  "twelve keys that are not present and for all `22` that are, counting "
                  "probes, and prints the standard curves beside the counts:"),
            ("math", [
                "m = 32,  linear probing,  n = 22        α = 11/16 = 0.6875",
                "",
                "                          counted     Knuth's curve (approximate)",
                "unsuccessful search         5.000                       5.62",
                "successful search           2.318                       2.10",
                "",
                "longest run of non-empty slots     12 of 32",
                "clusters                           1  2  12  1  1  5",
            ]),
            ("p", "Those two right-hand numbers are the one approximation this lesson "
                  "prints, and what is approximate is the <em>model</em>, not the "
                  "arithmetic. Knuth&rsquo;s curves assume a uniform hash function and "
                  "the idealised distribution of cluster lengths the analysis derives, "
                  "and this library proves neither. The numbers beside them were produced "
                  "by walking `32` slots and incrementing a counter. The lab labels the "
                  "column, and the reason to keep the two apart is visible one row down "
                  "the load curve."),
            ("math", [
                "m = 32,  linear probing,  same keys, aimed at nine tenths       n = 28",
                "",
                "α = 7/8 = 0.875           counted 8.417 probes unsuccessful",
                "                          Knuth's curve            32.50",
                "",
                "  the curve is above the table's own ceiling:  a 32-slot table",
                "  cannot cost more than 32 probes, because there are only 32 slots",
            ]),
            ("p", "At `α = 7/8` the curve says `32.5` and the table counted `8.4`. "
                  "Neither number is wrong. The curve describes a table large enough for "
                  "the idealised cluster distribution to hold; a `32`-slot table at "
                  "`α = 7/8` has four empty slots, and an unsuccessful search stops at "
                  "one of them after about eight probes. The curve is asymptotic in `m` "
                  "as well as in the load, and the lab prints the difference in its own "
                  "column so the parting of the two is on the page rather than in a "
                  "footnote."),
            ("p", "Above `α = 0.98` the lab refuses to print the curve at all, and says "
                  "so where the number would have been. The reason is that the curve is "
                  "effectively vertical there: `1/(1−α)²` is `2500` at `α = 0.98` and "
                  "`10 000` at `0.99`, so a figure read off it is a statement about the "
                  "formula rather than about any table. That refusal is the honest "
                  "behaviour for a model outside its range, and it is why `α` in a "
                  "probing table is kept well below `1` &mdash; at `α = 1` there is no "
                  "empty slot left to stop any search at all."),
        ],
        "lab": ("hash", {
            "mode": "probing",
            "preset": "linear-seventy",
            "panel_title": "Slots, clusters, tombstones, and the curve beside the counts",
            "panel_intro": "Choose the probe rule, the table size and the load to aim at. "
                           "The slot strip shows what is occupied, what is dead and where the "
                           "clusters are; probes are counted for present and absent keys and "
                           "plotted against Knuth&rsquo;s curve, which is labelled an "
                           "approximation and is not quoted at all above `α = 0.98`. The "
                           "panel also reports how many live keys a delete-by-emptying loses.",
        }),
        "steps_title": "Working a probing table",
        "steps_intro": "Insert, search, delete, in that order, and keep the three slot states straight throughout &mdash; the whole lesson lives in the difference between empty and dead.",
        "steps": [
            ("Write the probe sequence, not just the home slot",
             "`h(k)`, then `h(k)+1`, then `h(k)+2`, modulo `m`. A key is at the first "
             "free slot along that walk, which is often not its home slot, and a search "
             "that only checks the home slot finds almost nothing."),
            ("Search by walking until you find the key or a TRUE empty",
             "Occupied and not the key: keep going. Dead: keep going. Empty: stop and "
             "report absent. Those three rules are the structure&rsquo;s entire "
             "correctness argument, and confusing the last two is the bug."),
            ("Delete by marking, and count your tombstones",
             "Set the slot dead. Then look at what a search for the keys after it now "
             "does &mdash; it walks past, as it must. Keep a count of the dead slots: "
             "they cost search time and hold nothing, so past a few they are a reason to "
             "rebuild the table."),
            ("Read the counted probes and the curve as two different quantities",
             "The counts come from the table on screen. The curve comes from a model of "
             "an idealised large table, and the lab says so. When they disagree by a "
             "lot, ask which assumption of the model this table violates before "
             "suspecting either number."),
        ],
        "worked": {
            "title": "Eight slots, five keys, one careless delete",
            "intro": [
                "Small enough to hold in your head. Linear probing, `h(k) = k mod 8`, and "
                "the keys arriving in the order shown."
            ],
            "lines": [
                "insert  h(k)   probes           table   0  1  2  3  4  5  6  7",
                "",
                "  10      2      2 free            .  .  10  .  .  .  .  .",
                "  18      2      2 taken, 3 free   .  .  10  18 .  .  .  .",
                "  26      2      2, 3 taken, 4     .  .  10  18 26 .  .  .",
                "   3      3      3 taken, 4 taken, 5",
                "                                  .  .  10  18 26 3  .  .",
                "  11      3      3, 4, 5 taken, 6  .  .  10  18 26 3  11 .",
                "",
                "search 11   probes 3, 4, 5, 6      found after 4 probes",
                "",
                "now delete 18 by EMPTYING slot 3:",
                "            .  .  10  .  26 3  11 .",
                "search 26   probes 2, 3 → slot 3 is empty → NOT FOUND",
                "search 3    probes 3    → slot 3 is empty → NOT FOUND",
                "search 11   probes 3    → slot 3 is empty → NOT FOUND",
                "",
                "delete 18 by MARKING slot 3 dead:",
                "            .  .  10  X  26 3  11 .",
                "search 26   probes 2, 3 (dead, walk on), 4      found",
                "search 11   probes 3, 4, 5, 6                   found",
            ],
            "after": [
                "Three keys lost from a five-key table by one deletion, and every one of "
                "them is still sitting in the slot it was put in. This is the failure the "
                "tombstone exists to prevent, and it is worth doing by hand once because "
                "the bug it produces in a real system is a record that cannot be found "
                "rather than a crash.",
                "The marked version walks past slot `3` and finds everything. It also "
                "shows the cost: searching for `26` now costs three probes forever, one "
                "of them spent on a slot that holds nothing. Tombstones trade a "
                "correctness bug for a slow leak, and the leak is fixed by rebuilding, "
                "which is the next lesson&rsquo;s subject.",
                "For a faded rehearsal, use the lab at `m = 32` with double hashing at "
                "the same load. The supplied observation is that the load factor is "
                "identical to linear probing&rsquo;s &mdash; `11/16` &mdash; and "
                "Knuth&rsquo;s linear-probing curve is therefore unchanged at `5.62`. "
                "Count the probes: the lab reports `3.000` unsuccessful against linear "
                "probing&rsquo;s `5.000`, and the longest cluster drops from `12` to `8`. "
                "Then say which of those four numbers are counts and which is a model.",
            ],
        },
        "quiz_title": "Probes, tombstones and curves",
        "quiz": [
            {"q": "A key `k` with `h(k) = 5` sits in slot `7` because `5` and `6` were taken. The key in slot `6` is deleted by emptying it. What happens to a search for `k`?",
             "a": ["It finds `k` in slot `7` as before",
                   "It probes `5`, then `6`, finds it empty, and reports `k` absent",
                   "It probes every slot and then reports `k` absent",
                   "It moves `k` into slot `6` automatically"],
             "c": 1,
             "why": "An empty slot means the key would have been placed there, so the "
                    "search stops. `k` is still in slot `7` and is now unreachable. The "
                    "search does not continue to the end of the table &mdash; that would "
                    "make every unsuccessful search cost `m` &mdash; and nothing moves "
                    "keys on deletion. A tombstone in slot `6` is what keeps the search "
                    "walking."},
            {"q": "At `α = 7/8` on a `32`-slot table, the lab counts `8.4` probes for an unsuccessful search and prints `32.50` for Knuth&rsquo;s curve. What should you conclude?",
             "a": ["The measurement is wrong; `32.50` is the correct expected cost",
                   "The curve is wrong; linear probing costs `8.4` probes at `α = 7/8`",
                   "The curve models a large table and this one has only `32` slots, so the model is outside its range",
                   "The table must contain tombstones, which the curve does not account for"],
             "c": 2,
             "why": "The count is a fact about the table drawn on screen. The curve is an "
                    "asymptotic model that assumes an idealised cluster distribution, "
                    "which needs a table much larger than `32` &mdash; and `32.50` exceeds "
                    "the `32` probes the whole table could possibly cost, which is the "
                    "giveaway. Neither number is a mistake and neither is the general "
                    "answer. There are no tombstones in this run; the panel reports zero."},
            {"q": "Why does the lab print nothing where Knuth&rsquo;s figure would go once `α` exceeds `0.98`?",
             "a": ["Because the formula divides by zero at `α = 1`",
                   "Because the curve is effectively vertical there, so a figure read off it describes no real table",
                   "Because the table is full and no search is possible",
                   "Because tombstones make the load factor meaningless above `0.98`"],
             "c": 1,
             "why": "`1/(1−α)²` is `2500` at `0.98` and `10 000` at `0.99`: the value "
                    "changes by a factor of four over a change of one hundredth in the "
                    "load, so quoting it would be reporting the formula&rsquo;s "
                    "sensitivity rather than a table&rsquo;s cost. The division by zero "
                    "only happens exactly at `α = 1`; the refusal starts well before "
                    "that. A table at `α = 0.99` is not full, and tombstones are a "
                    "separate problem."},
        ],
        "mistakes": [
            ("Deleting by emptying the slot",
             "It is the natural thing to write and it breaks every probe chain that ran "
             "through that slot. The lab loses three of fourteen live keys to one round "
             "of deletions on a table of thirty-two, and the keys are still there. The "
             "rule is that in an open-addressed table a deletion marks and never empties, "
             "and the cost of that rule is a table that must eventually be rebuilt."),
            ("Expecting `1 + α` to price a probing search",
             "That is chaining&rsquo;s bound, and it holds because chains are "
             "independent. Probing clusters: a long run of occupied slots catches more "
             "keys and grows. The standard figure for an unsuccessful search is about "
             "`½(1 + 1/(1−α)²)`, which at `α = 0.9` is `50.5` against chaining&rsquo;s "
             "`1.9`, and the difference is the clustering."),
            ("Treating the curve as the measurement or the measurement as the bound",
             "They are two different kinds of number printed side by side on purpose. The "
             "curve is a model whose assumptions this library does not prove; the probe "
             "count is an execution on the table in front of you. Reading the curve as "
             "the answer ignores that a `32`-slot table cannot cost `32.5` probes; "
             "reading the count as the answer ignores that one table at one load is not "
             "a bound."),
        ],
        "standard": ("Finish when a deletion in a probing table feels like an operation that needs an argument.",
                     "You should be able to insert and search along a probe sequence by "
                     "hand, name the keys a delete-by-emptying loses on a small table, "
                     "state the three slot states and what each does to a search, and say "
                     "of any figure on the page whether it was counted or read off a model "
                     "whose assumptions are not proved here."),
        "note": (
            "Tombstones accumulate and a table fills up, so both kinds of hash table need "
            "to change size while running. &ldquo;Resizing and the Load Factor&rdquo; is "
            "about the two thresholds that make that cheap: growing and shrinking at the "
            "same load thrashes, and the lab produces the sequence that rehashes on "
            "thirty-nine of forty operations."
        ),
    },
    # ---------------------------------------------------------------- 07
    {
        "slug": "resizing-and-the-load-factor",
        "title": "Resizing and the Load Factor",
        "module": "Hash tables",
        "one_line": "Count the rehash cost of an insert/delete sequence under two threshold policies and identify the one that thrashes.",
        "summary": (
            "A hash table keeps its load factor in range by doubling when it fills and "
            "halving when it empties, and the two thresholds must be different. Doubling "
            "at `α = 1` and halving at `α = ¼` costs `52` over forty operations at the "
            "boundary; doubling and halving both at `α = ½` costs `495` for the same "
            "forty, rehashing on thirty-nine of them. The gap between the thresholds is "
            "the whole mechanism."
        ),
        "key": [
            "grow    α ≥ 1      double m,  rehash every key",
            "shrink  α ≤ 1/4    halve m,   rehash every key",
            "",
            "the two thresholds must differ, and by a factor of more than 2",
            "",
            "40 operations alternating at the boundary, from m = 4:",
            "  grow at 1, shrink at 1/4     2 rehashes,  12 keys moved,  total 52",
            "  grow at 1/2, shrink at 1/2  39 rehashes, 455 keys moved,  total 495",
        ],
        "key_label": "Two thresholds, and what happens when they are the same one",
        "concepts_intro": (
            "One idea with a name worth learning &mdash; hysteresis &mdash; and two "
            "consequences: why the amortised bound holds when the thresholds differ, and "
            "why it fails completely when they do not."
        ),
        "concepts": [
            ("Rehashing is unavoidable and that is fine",
             "Every key&rsquo;s slot is computed from `m`, so changing `m` means "
             "recomputing every slot: a resize is `Θ(n)` and there is no cleverer way. "
             "The bound is amortised, exactly as for the two-stack queue: an operation "
             "that triggers a resize is expensive, and the sequence containing it is not, "
             "because doubling makes resizes exponentially rare."),
            ("The two thresholds must leave a gap",
             "If the table grows at `α = ½` and shrinks at `α = ½`, then one insertion "
             "past the boundary doubles the table, which halves `α`, which triggers a "
             "shrink, which doubles `α`, and the next operation resizes again. The gap "
             "&mdash; grow at `1`, shrink at `¼` &mdash; means that after any resize the "
             "load is far from both thresholds, so many operations must happen before "
             "another one is due. That gap is called hysteresis."),
            ("The amortised bound is a claim about every sequence, and the lab can break it",
             "`3` per operation is the promise: forty operations should cost at most "
             "`120`. The hysteresis policy costs `52`, comfortably inside. The equal "
             "thresholds cost `495`, four times the bound, on the same forty operations "
             "&mdash; which is what it looks like when a policy has no amortised bound at "
             "all rather than a loose one."),
        ],
        "read_title": "Two thresholds, the potential argument, and the policy that thrashes",
        "read_intro": "Why doubling gives an amortised constant, why the shrink threshold must be lower, and the two policies counted on the same sequence.",
        "body": [
            ("p", "A table&rsquo;s cost depends on its load factor, so the load factor "
                  "has to be kept in a band. Too high and chains grow or probes cluster; "
                  "too low and most of the memory is empty. The mechanism is to pick "
                  "thresholds and resize when one is crossed, rehashing every key into "
                  "the new table."),
            ("def", ("Growth and shrink thresholds",
                     "A table grows &mdash; usually doubling `m` &mdash; when `α` reaches "
                     "the <strong>growth threshold</strong>, and shrinks &mdash; usually "
                     "halving `m` &mdash; when `α` falls to the <strong>shrink "
                     "threshold</strong>. Both resizes rehash all `n` keys and cost "
                     "`Θ(n)`.",
                     "The standard pair is grow at `α = 1` and shrink at `α = ¼`. The "
                     "shrink threshold is deliberately far below half the growth "
                     "threshold, and the next paragraph is why.")),
            ("thm", ("Doubling gives an amortised constant cost",
                     "Under a policy that doubles at `α = 1` and halves at `α = ¼`, a "
                     "sequence of `k` insertions and deletions on a table starting empty "
                     "costs `O(k)` in total, so `O(1)` amortised per operation.",
                     "The potential method: give the table a potential that measures how "
                     "close it is to its next resize &mdash; roughly `2n − m` above half "
                     "full and `m/2 − n` below. An ordinary operation changes `n` by one "
                     "and so changes the potential by a constant. A resize costs `n` and "
                     "releases potential that the operations since the last resize have "
                     "paid in, because the gap between the thresholds guarantees there "
                     "were at least about `n/2` of them. The released potential covers "
                     "the rehash, and the amortised cost of every operation is constant.")),
            ("p", "That proof needs the gap. If growth and shrink happen at the same "
                  "load, then immediately after a resize the table is sitting on the "
                  "other threshold, no operations have accumulated any potential, and the "
                  "next operation resizes again. There is nothing to release and the "
                  "argument has no step to make. The failure is not a worse constant; it "
                  "is the absence of a bound."),
            ("h3", "Both policies, on the same forty operations"),
            ("p", "The lab&rsquo;s boundary pattern fills a table and then alternates "
                  "inserting and deleting, which is the mix designed to sit on a "
                  "threshold. Forty operations from `m = 4`:"),
            ("math", [
                "grow at α = 1,  shrink at α = 1/4",
                "",
                "  rehashes                 2      at ops 4 (4→8) and 8 (8→16)",
                "  keys moved              12",
                "  total cost              52      against the 3m line at 120",
                "  amortised per op      13/10 = 1.3",
                "  final table m = 16 holding 14 keys       no thrash detected",
                "",
                "grow at α = 1/2,  shrink at α = 1/2",
                "",
                "  rehashes                39      of 40 operations",
                "  keys moved             455",
                "  total cost             495      against the 3m line at 120",
                "  amortised per op       99/8 = 12.375",
                "  thrashing detected from operation 2",
            ]),
            ("p", "Read the two rehash counts first. Two resizes in forty operations "
                  "against thirty-nine. The hysteresis policy resizes twice, early, while "
                  "the table is growing into its final size, and then never again "
                  "&mdash; the alternating insertions and deletions move `α` around "
                  "inside the band and never reach an edge of it. The equal-threshold "
                  "policy resizes on almost every operation, oscillating between `m = 16` "
                  "and `m = 32` from operation `8` onward and moving thirteen or "
                  "fourteen keys on every resize from operation `13`."),
            ("p", "The total cost is `52` against `495`, and the second one has broken "
                  "the bound: `3` per operation would be `120`. The measured amortised "
                  "figures are `1.3` and `12.375`, and the second is not a constant "
                  "&mdash; it grows with the table, because each thrashing resize costs "
                  "`n` and `n` is proportional to `m`. Doubling the sequence length on "
                  "the thrashing policy roughly quadruples its cost."),
            ("example", ("Growth alone, for the shape of the amortised line",
                         "Forty insertions and no deletions, same thresholds: four "
                         "rehashes at `m = 4, 8, 16, 32`, moving `4 + 8 + 16 + 32 = 60` "
                         "keys in total, for a cost of `100` against the `120` line. The "
                         "rehash cost of a table that reaches size `n` is about `2n` "
                         "whatever the sequence, because the doubling costs form a "
                         "geometric series &mdash; which is the cleanest case of the "
                         "amortised argument and the one to look at before the boundary "
                         "pattern.")),
            ("p", "One caution about the measured amortised figure. `13/10` is the total "
                  "divided by the number of operations for this sequence, and it is "
                  "below `3`, and that is not the bound holding &mdash; it is one "
                  "sequence coming in under it. A different pattern at the same "
                  "thresholds could come closer to `3` and none can exceed it, and the "
                  "reason none can is the potential argument above rather than anything "
                  "the lab did. The lab is what shows you the thrashing policy, which no "
                  "amount of reasoning about the good policy would have revealed."),
        ],
        "lab": ("hash", {
            "mode": "resize",
            "preset": "hysteresis",
            "panel_title": "Two thresholds, an operation pattern, and the rehash cost",
            "panel_intro": "Set the growth and shrink thresholds and the operation pattern "
                           "&mdash; monotone growth, alternating at the boundary, or drawn "
                           "from the stream. Every rehash is reported with the keys it moved, "
                           "the cumulative cost is plotted against the `3m` line the "
                           "amortised bound promises, and the panel names the operation at "
                           "which the policy starts thrashing. Set both thresholds to a half "
                           "and watch the bound break.",
        }),
        "steps_title": "Choosing and testing a resize policy",
        "steps_intro": "Pick the thresholds, then attack them with the pattern designed to sit between them. A policy tested only on growth has not been tested.",
        "steps": [
            ("State both thresholds, and check the gap",
             "Grow at `α_g`, shrink at `α_s`, and require `α_s` to be well below "
             "`α_g/2`. `1` and `¼` is the standard pair. Equal thresholds, or `½` and "
             "`¼`, are the ones to be suspicious of, and the reason is arithmetic: after "
             "a resize the new load must be far from both edges."),
            ("Run the monotone pattern first",
             "Insertions only. The rehash costs form a geometric series, the total is "
             "about `2n`, and the cumulative line should sit comfortably under the `3m` "
             "line. If it does not, the policy is wrong in the easy case and there is no "
             "point going further."),
            ("Now alternate at the boundary",
             "Fill the table to just under the growth threshold, then insert and delete "
             "alternately. This is the pattern a bad policy dies on, and it is not "
             "exotic &mdash; a cache or a work queue whose size hovers around a "
             "threshold produces it naturally."),
            ("Count rehashes, not just total cost",
             "The rehash count is the diagnostic; the cost is the symptom. Two rehashes "
             "in forty operations is a healthy policy. Thirty-nine in forty is a policy "
             "with no amortised bound, and the count says so immediately while the total "
             "needs comparing with something."),
        ],
        "worked": {
            "title": "Both policies on the boundary pattern, operation by operation",
            "intro": [
                "The first thirteen operations of the lab&rsquo;s forty, under each policy, "
                "starting from `m = 4`. The pattern fills to thirteen keys and then "
                "alternates."
            ],
            "lines": [
                "grow at 1, shrink at 1/4                grow at 1/2, shrink at 1/2",
                "",
                "α is the load the operation produced, BEFORE any resize it triggered",
                "",
                "op  n    m   α      rehash             n    m   α      rehash",
                " 1  1    4  1/4     —                  1    4  1/4     —",
                " 2  2    4  1/2     —                  2    8  1/2     4 → 8,  2 keys",
                " 3  3    4  3/4     —                  3    4  3/8     8 → 4,  3 keys",
                " 4  4    8  1       4 → 8,  4 keys     4    8  1       4 → 8,  4 keys",
                " 5  5    8  5/8     —                  5   16  5/8    8 → 16,  5 keys",
                " 6  6    8  3/4     —                  6    8  3/8    16 → 8,  6 keys",
                " 7  7    8  7/8     —                  7   16  7/8    8 → 16,  7 keys",
                " 8  8   16  1       8 → 16, 8 keys     8   32  1/2   16 → 32,  8 keys",
                " 9  9   16  9/16    —                  9   16  9/32  32 → 16,  9 keys",
                "10 10   16  5/8     —                 10   32  5/8   16 → 32, 10 keys",
                "11 11   16 11/16    —                 11   16 11/32  32 → 16, 11 keys",
                "12 12   16  3/4     —                 12   32  3/4   16 → 32, 12 keys",
                "13 13   16 13/16    —                 13   16 13/32  32 → 16, 13 keys",
                "",
                "after 40 operations:",
                "  2 rehashes, 12 moved, total 52       39 rehashes, 455 moved, total 495",
                "  amortised 13/10                      amortised 99/8",
                "  3m line 120:  inside                 3m line 120:  broken, 4× over",
            ],
            "after": [
                "The left column stops resizing after operation `8` and never starts "
                "again: `α` wanders between `9/16` and `7/8` for the remaining "
                "thirty-two operations, and neither edge of the band is anywhere near. "
                "That is hysteresis working, and it is the whole of the mechanism &mdash; "
                "there is no cleverness in it beyond choosing two numbers far apart.",
                "The right column resizes on twelve of the first thirteen operations, and "
                "keeps going for the rest. Look at operation `8`: the insertion pushes "
                "`α` to `1/2`, which is the growth threshold, so the table doubles to "
                "`32` and `α` becomes `1/4` &mdash; which is below the shrink threshold "
                "of `1/2`, so the next operation halves it back. The policy has trapped "
                "itself between its own two rules.",
                "For a faded rehearsal, try grow at `1` and shrink at `1/2` &mdash; a gap, "
                "but only a factor of two. The supplied observation is that doubling at "
                "`α = 1` leaves `α = 1/2`, which is exactly the shrink threshold. Predict "
                "what the operation after a growth does, then run it, and say how far "
                "apart the thresholds have to be for the potential argument to have "
                "anything to release.",
            ],
        },
        "quiz_title": "Thresholds and amortised cost",
        "quiz": [
            {"q": "A table doubles at `α = ½` and halves at `α = ½`. It has just doubled from `16` slots to `32` with `8` keys. What does the next operation do?",
             "a": ["Nothing unusual: `α = 1/4` is inside the band",
                   "It resizes again, because `α = 1/4` is at or below the shrink threshold",
                   "It grows again, because the table is now too large",
                   "It depends on whether the operation is an insert or a delete"],
             "c": 1,
             "why": "After doubling, `α = 8/32 = 1/4`, which is already below the shrink "
                    "threshold of `1/2`, so the very next operation halves the table back "
                    "&mdash; and then `α` returns to about `1/2` and it grows again. With "
                    "equal thresholds there is no band for `α` to be inside. It resizes "
                    "whichever operation comes next, which is why the lab counts "
                    "thirty-nine rehashes in forty operations."},
            {"q": "Forty operations under the hysteresis policy cost `52`, an average of `1.3` each. What has been established?",
             "a": ["That the policy is `O(1)` amortised",
                   "That this sequence came in under the `3m` line; the bound itself comes from the potential argument",
                   "That the amortised cost of this policy is `1.3`",
                   "That the policy never rehashes more than twice"],
             "c": 1,
             "why": "A total of `52` for forty operations is one sequence measured. The "
                    "amortised bound is a claim about every sequence and is proved by the "
                    "potential argument, which needs the gap between the thresholds. "
                    "`1.3` is this sequence&rsquo;s average, not the policy&rsquo;s "
                    "constant, and a longer or different sequence rehashes more than "
                    "twice &mdash; forty straight insertions rehash four times."},
            {"q": "Why is a rehash unavoidably `Θ(n)`?",
             "a": ["Because the old table has to be deallocated",
                   "Because every key&rsquo;s slot is computed from `m`, so changing `m` invalidates all of them",
                   "Because the new table has to be zeroed before use",
                   "Because the load factor has to be recomputed for each key"],
             "c": 1,
             "why": "A slot is `h(k) mod m` or a probe sequence built from `m`, so a new "
                    "`m` means every key is in the wrong place and all `n` must be "
                    "reinserted. Deallocation and zeroing are `Θ(m)` costs of the same "
                    "order but they are not why the keys must move, and the load factor "
                    "is one division for the whole table."},
        ],
        "mistakes": [
            ("Shrinking at half the growth threshold, or at the same one",
             "&ldquo;Grow when full, shrink when half empty&rdquo; sounds symmetric and "
             "thrashes: doubling at `α = 1` leaves `α = 1/2`, which is the shrink "
             "threshold, so the next deletion halves the table back. The standard `1` and "
             "`¼` is not arbitrary &mdash; the gap is what the potential argument spends, "
             "and without it there is no bound to state."),
            ("Reading the measured average as the amortised constant",
             "`52` over forty operations is `1.3`, and `495` over the same forty is "
             "`12.375`. The first is a sequence that came in under a bound proved "
             "elsewhere; the second is a policy with no bound, measured on one sequence "
             "that happened to expose it. An average over a run is a number about that "
             "run, and the only thing that makes it a guarantee is an argument."),
            ("Testing a resize policy on growth only",
             "Monotone insertion is the easy case: the geometric series of doubling costs "
             "keeps the total near `2n` under almost any threshold. Every policy looks "
             "fine there. The pattern that distinguishes them is alternation at the "
             "boundary, and a cache or queue whose size hovers near a threshold produces "
             "it without anyone constructing it."),
        ],
        "standard": ("Finish when “shrink when half empty” sounds like a bug report.",
                     "You should be able to state a growth and a shrink threshold and say "
                     "what the load factor becomes immediately after each kind of resize, "
                     "count rehashes and keys moved over a stated sequence, recognise "
                     "thrashing from the rehash count rather than the total, and separate a "
                     "measured average from the amortised bound the potential argument "
                     "proves."),
        "note": (
            "Hash tables answer membership and refuse order: no predecessor, no range, no "
            "sorted walk, at any load factor. The next five lessons are about the "
            "structure that keeps order and pays for it in constants. &ldquo;Binary "
            "Search Trees&rdquo; starts with the invariant &mdash; and with the fact that "
            "it is not a check on a node and its children, which the lab settles with a "
            "tree that passes the local check and is not a search tree."
        ),
    },
]
