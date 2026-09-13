"""Course 6, lessons 08-13 - electing a leader, ordering events, and consistency as a count."""

LESSONS = [
    # ---------------------------------------------------------------- 08
    {
        "slug": "randomised-election-timeouts",
        "title": "Randomised Election Timeouts",
        "module": "Majorities and leaders",
        "one_line": "Compute the probability that an election round is clean, and the number of rounds it takes.",
        "summary": (
            "`n` candidates each pick one of `T` timeout slots at random, and the round is "
            "clean when exactly one of them holds the earliest occupied slot. Summing over "
            "which slot that is gives `P(clean) = Σ n(1/T)((T − j)/T)^(n−1)`, and the "
            "expected number of rounds is its reciprocal. At five candidates and ten slots "
            "that is `15333/20000` and `1.3044` rounds; at `T = 1` — a fixed timeout — it "
            "is exactly zero, for ever."
        ),
        "key": [
            "P(clean) = Σ over slots j of  n · (1/T) · ((T − j)/T)^(n − 1)",
            "one candidate alone in the earliest occupied slot",
            "n = 5, T = 10:   P = 15333/20000 = 76.665%",
            "expected rounds = 1/P = 20000/15333 = 1.3044",
            "T = 1, a fixed timeout:   P = 0 exactly, and no leader is ever elected",
        ],
        "key_label": "The clean-round probability, and the rounds it implies",
        "concepts_intro": (
            "A definition of what has to happen, a sum over the one free choice, and the "
            "geometric argument that turns a probability into a wait."
        ),
        "concepts": [
            ("A clean round is one candidate strictly first",
             "Every follower that times out becomes a candidate and asks for votes. If two "
             "candidates start at the same instant they each collect part of the cluster "
             "and neither reaches a majority, so the term ends with no leader and everyone "
             "tries again. What makes a round clean is not that one candidate wins by "
             "argument, it is that one candidate <em>started</em> before all the others."),
            ("The sum is over which slot the winner takes",
             "Condition on the winner's slot `j`: there are `n` choices of who the winner "
             "is, probability `1/T` that this candidate picked slot `j`, and "
             "`((T − j)/T)^(n−1)` that every other candidate picked a strictly later slot. "
             "The events for different `j` are disjoint, so the probabilities add, and the "
             "sum telescopes into nothing simpler — which is why the lab lists the terms "
             "rather than a closed form."),
            ("Rounds are independent, so the expectation is `1/P`",
             "Each round redraws every candidate's slot, so the number of rounds until the "
             "first clean one is geometric with success probability `P` and has expectation "
             "`1/P`. At `P = 15333/20000` that is `1.3044` rounds — the randomisation costs "
             "about a third of an extra election, which is a small price for the "
             "certainty it buys."),
        ],
        "read_title": "Splitting the vote, and the randomisation that stops it",
        "read_intro": (
            "What a split vote is, the sum that prices a clean round, and what happens to "
            "the same arithmetic when the timeout is not random at all."
        ),
        "body": [
            ("def", ("Election round, split vote, clean round",
                     "In an <strong>election round</strong>, each of `n` candidates waits "
                     "a randomly chosen timeout and then stands. The round is "
                     "<strong>clean</strong> if exactly one candidate holds the earliest "
                     "chosen timeout, and a <strong>split vote</strong> otherwise: two or "
                     "more candidates stand together, divide the votes, and no one reaches "
                     "a majority.")),
            ("p", "Modelling the timeout as one of `T` equally likely discrete slots is a "
                  "simplification of a continuous random delay, and it is the "
                  "simplification that makes the probability exactly computable. `T` is "
                  "roughly the width of the randomisation window divided by the "
                  "round-trip time — the resolution at which two candidates can still tell "
                  "each other apart."),
            ("math", [
                "n = 5 candidates, T = 10 slots, each candidate picks uniformly",
                "",
                "P(clean) = Σ over j = 1..10 of  5 · (1/10) · ((10 − j)/10)⁴",
                "",
                "  j = 1    5/10 · (9/10)⁴ = 5/10 · 6561/10 000  =  32 805/100 000",
                "  j = 2    5/10 · (8/10)⁴ = 5/10 · 4096/10 000  =  20 480/100 000",
                "  j = 3    5/10 · (7/10)⁴ = 5/10 · 2401/10 000  =  12 005/100 000",
                "  j = 4    5/10 · (6/10)⁴ = 5/10 · 1296/10 000  =   6 480/100 000",
                "  j = 5    5/10 · (5/10)⁴ = 5/10 ·  625/10 000  =   3 125/100 000",
                "  j = 6    5/10 · (4/10)⁴ = 5/10 ·  256/10 000  =   1 280/100 000",
                "  j = 7    5/10 · (3/10)⁴ = 5/10 ·   81/10 000  =     405/100 000",
                "  j = 8    5/10 · (2/10)⁴ = 5/10 ·   16/10 000  =      80/100 000",
                "  j = 9    5/10 · (1/10)⁴ = 5/10 ·    1/10 000  =       5/100 000",
                "  j = 10   5/10 · (0/10)⁴ = 0                   =       0",
                "",
                "  total  =  76 665/100 000  =  15 333/20 000  =  76.665%",
            ]),
            ("p", "Nearly half the mass sits in the first two terms, which is the shape to "
                  "carry away: a clean round is usually won early, because winning late "
                  "requires every other candidate to have chosen later still, and that "
                  "gets rapidly less likely. The last term is zero because a candidate in "
                  "the final slot cannot have everyone else strictly after it."),
            ("h3", "A fixed timeout is the T = 1 case"),
            ("math", [
                "T = 1: every candidate has the same slot",
                "",
                "  P(clean) = 5 · (1/1) · ((1 − 1)/1)⁴ = 5 · 0 = 0",
                "",
                "every round is a split vote, and the next round is identical",
                "",
                "expected rounds = 1/P",
                "  T = 10, n = 5     20 000/15 333 = 1.3044 rounds",
                "  T = 20, n = 5     P = 87.9166%,  1.1374 rounds",
                "  T = 1             1/0, which is what “it never elects” looks like",
            ]),
            ("p", "That is the whole argument for randomising the timeout, and it is not a "
                  "matter of degree. A deterministic timeout does not make split votes "
                  "likely, it makes them certain, and no amount of retrying helps because "
                  "every retry reproduces the tie. The randomisation is what makes the "
                  "expectation finite at all."),
            ("example", ("What a wider window costs",
                         "Doubling the window from `T = 10` to `T = 20` raises the clean "
                         "probability from `76.665%` to `87.9166%` and lowers the expected "
                         "rounds from `1.3044` to `1.1374`. But each round now waits up to "
                         "twenty slots instead of ten, so the expected <em>time</em> to "
                         "elect can go up even as the expected number of rounds goes down. "
                         "The quantity to minimise is rounds multiplied by the length of a "
                         "round, and it has an interior optimum — which is why real "
                         "implementations pick a window of a few multiples of the "
                         "round-trip time and not the largest one they can get away with.")),
            ("p", "Three assumptions are doing work here and each is worth naming. All `n` "
                  "candidates are assumed to start their timers at the same moment, which "
                  "is the worst case and roughly what a leader crash produces; slots are "
                  "assumed discrete and uniform, where a real implementation draws from a "
                  "continuous range; and every follower is assumed to become a candidate, "
                  "where in practice one that has already granted a vote or heard from a "
                  "new leader stands down. All three make the computed `P(clean)` "
                  "pessimistic, which is the safe direction for a number you are sizing a "
                  "timeout with."),
        ],
        "lab": ("replica", {
            "mode": "election",
            "panel_title": "Set the candidates and the window",
            "panel_intro": "Every term is computed as an exact fraction and listed before "
                           "it is summed, so the probability can be checked slot by slot. "
                           "Drag `T` down to `1` and watch the whole sum collapse to zero.",
        }),
        "steps_title": "Sizing an election timeout",
        "steps_intro": (
            "The window is the only free parameter and it is traded against the length of "
            "a round, not against correctness."
        ),
        "steps": [
            ("Count the candidates, which is the cluster size in the worst case",
             "After a leader crash every remaining node may time out, so `n` is `cluster "
             "size − 1` at worst. Using a smaller `n` because “they will not all stand” is "
             "how a window gets sized for a case that is not the one it exists for."),
            ("Express the window as a number of distinguishable slots",
             "`T` is the randomisation range divided by the resolution at which two "
             "candidates' starts can be told apart — in practice, the round-trip time. A "
             "window of `150` to `300` milliseconds with a `15 ms` round trip is about ten "
             "slots."),
            ("Sum the terms and take the reciprocal",
             "`P(clean) = Σ n(1/T)((T − j)/T)^(n−1)` over `j`, then `1/P` rounds. Both are "
             "exact and both are small sums; there is no reason to simulate this."),
            ("Multiply the rounds by the length of a round before choosing",
             "Expected rounds falls as `T` rises and the duration of a round rises with "
             "it. The product is what a user waits, and the window that minimises it is "
             "usually a few round trips wide rather than as wide as possible."),
        ],
        "worked": {
            "title": "Five candidates, ten slots, and a fixed timeout",
            "intro": [
                "A five-node cluster loses its leader. Every remaining node times out and "
                "stands. The implementation randomises the timeout across ten "
                "distinguishable slots, and the question is how long a leaderless period "
                "to expect — and what would happen if the randomisation were removed.",
            ],
            "lines": [
                "n = 5, T = 10",
                "",
                "P(clean) = Σ  5 · (1/10) · ((10 − j)/10)⁴",
                "",
                "  contributions, in units of 1/100 000",
                "    32 805   20 480   12 005   6 480   3 125",
                "     1 280      405       80       5       0",
                "",
                "  total = 76 665/100 000 = 15 333/20 000 = 76.665%",
                "",
                "P(split) = 1 − 15 333/20 000 = 4 667/20 000 = 23.335%",
                "",
                "expected rounds = 20 000/15 333 = 1.3044",
                "  so about one round in four is wasted, and the wasted rounds",
                "  are what the randomisation is buying",
                "",
                "now remove the randomisation:  T = 1",
                "  every candidate picks the only slot",
                "  P(clean) = 5 · 1 · 0⁴ = 0",
                "  expected rounds = 1/0 — the cluster never elects a leader",
            ],
            "after": [
                "Three quarters of first rounds succeed, and the expectation of `1.3044` "
                "says the cost of the remainder is about a third of one extra election. "
                "For a window of a few hundred milliseconds that is a leaderless period "
                "measured in fractions of a second, which is what makes randomised "
                "timeouts a solved problem rather than a tuning exercise.",
                "The `T = 1` line is the one to remember, because a fixed timeout is not a "
                "worse choice on a spectrum — it is a broken one. Its clean probability is "
                "exactly zero and every retry is identical to the last, so the cluster "
                "sits in a loop of split votes until something perturbs the timing by "
                "accident. Systems have shipped like this and the symptom is a cluster "
                "that elects instantly in testing, where clocks and loads differ, and "
                "never elects on identical hardware under identical load.",
                "For a faded rehearsal, take the same window to a nine-node cluster, so "
                "`n = 8` candidates and `T = 10`. The supplied first move is that the "
                "exponent becomes `7`, so the `j = 1` term is `8/10 · (9/10)⁷`. Predict "
                "whether `P(clean)` rises or falls against the five-candidate case before "
                "computing it, then compute it, then say what `T` would restore the "
                "original expected rounds.",
            ],
        },
        "quiz_title": "Clean rounds and split votes",
        "quiz": [
            {"q": "What has to happen for an election round to be clean?",
             "a": ["Every candidate must choose a different slot",
                   "Exactly one candidate must hold the earliest chosen slot",
                   "The candidate with the most recent log must choose the earliest slot",
                   "A majority of candidates must choose the same slot"],
             "c": 1,
             "why": "The earliest candidate asks first and collects a majority before "
                    "anyone else stands, so only the earliest slot matters and ties "
                    "anywhere else are harmless. Requiring all slots distinct is far "
                    "stronger than necessary; the log condition decides who is "
                    "<em>eligible</em> to win rather than who starts first; and candidates "
                    "sharing a slot is precisely the split this is trying to avoid."},
            {"q": "Five candidates, and the timeout is a fixed constant rather than a random draw — so `T = 1`. What is the probability of a clean round?",
             "a": ["`0`", "`1/5`", "`1`", "`1/10`"],
             "c": 0,
             "why": "With one slot every candidate picks it, so `((T − j)/T)^(n−1) = 0⁴ = "
                    "0` and the whole sum vanishes. Each candidate has probability `1/5` "
                    "of being the one the cluster would have preferred, which is not the "
                    "same question; and a clean round is impossible rather than certain, "
                    "because all five stand at once."},
            {"q": "`P(clean) = 15333/20000`. What is the expected number of rounds before a leader is elected?",
             "a": ["`1.3044`", "`0.76665`", "`5`", "`10`"],
             "c": 0,
             "why": "Rounds are independent redraws, so the count is geometric with "
                    "expectation `1/P = 20000/15333 ≈ 1.3044`. `0.76665` is `P` itself — "
                    "a probability, not a count — and `5` and `10` are the candidates and "
                    "the slots, neither of which is a number of rounds."},
        ],
        "mistakes": [
            ("Expecting a fixed timeout to work most of the time",
             "It works none of the time. `P(clean) = 0` at `T = 1` is exact, not an "
             "approximation, and the failure is stable: the same candidates redraw the "
             "same slot every round. A cluster that elects fine in a test lab and never "
             "elects on uniform hardware is showing you this, and no amount of raising or "
             "lowering the constant fixes it."),
            ("Reading `76.665%` as the probability of ever electing a leader",
             "It is the probability of electing one in the <em>first</em> round. The "
             "probability of electing one eventually is `1`, and the quantity that matters "
             "operationally is the expected number of rounds, `1.3044`, multiplied by how "
             "long a round takes. Quoting the first-round figure as a success rate "
             "under-reports the system by a factor that depends on `T`."),
            ("Widening the window because it raises the clean probability",
             "It does raise it — `76.665%` to `87.9166%` from ten slots to twenty — while "
             "making every round twice as long. The user-visible quantity is expected "
             "rounds times round length, and past a few round trips the second factor "
             "dominates. Optimise the product, and say which of the two you traded."),
        ],
        "standard": ("Finish when “we set the election timeout to 200 ms” makes you ask what the randomisation range is.",
                     "You should be able to write the clean-round sum from the definition, "
                     "evaluate it term by term as exact fractions, take the reciprocal for "
                     "expected rounds, state what happens at `T = 1` and why, and name the "
                     "three modelling assumptions and which direction each biases the "
                     "answer."),
        "note": "A leader settles who decides, and a majority settles what is committed. "
                "Neither settles the question every replicated system eventually asks: "
                "given two events on two machines, which came first? “Lamport Clocks” gives "
                "the first and cheapest answer, together with the precise sense in which "
                "that answer is only half of one.",
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "lamport-clocks",
        "title": "Lamport Clocks",
        "module": "Clocks and order",
        "one_line": "Stamp a message diagram by the Lamport rule and exhibit a pair the stamps order wrongly.",
        "summary": (
            "A Lamport clock is one counter per process and one rule: "
            "`L(e) = max(L_local, L_msg) + 1`. It produces a total order that never "
            "contradicts causality — if `a` happened before `b` then `L(a) &lt; L(b)` — and "
            "the converse is false. On an eleven-event diagram there are `32` ordered "
            "pairs and `17` further pairs whose stamps are ordered while the events are "
            "not, which is exactly the gap the next lesson closes."
        ),
        "key": [
            "L(e) = max(L_local, L_msg) + 1        a send carries the sender's L",
            "a → b   ⟹   L(a) < L(b)               sound, and useful",
            "L(a) < L(b)   ⟹   a → b               FALSE",
            "11 events, 3 messages:  32 pairs are ordered by happens-before",
            "and 17 further pairs have L(a) < L(b) with a not before b",
        ],
        "key_label": "One rule, and the implication that does not hold",
        "concepts_intro": (
            "The rule has three cases, the guarantee has one direction, and the "
            "counterexample is on the same diagram you stamped."
        ),
        "concepts": [
            ("The rule is three cases and a counter",
             "Each process keeps one integer. On a local event it increments it. On a send "
             "it increments and attaches the new value to the message. On a receive it "
             "takes the maximum of its own counter and the one on the message, then "
             "increments. The `max` is what carries information across processes, and the "
             "`+ 1` is what keeps the stamp of the receive strictly after the send."),
            ("The stamps are sound, not complete",
             "If `a` happened before `b` — by process order, by a message, or by a chain "
             "of those — then `L(a) &lt; L(b)`, because every step of the chain strictly "
             "increases the stamp. That is the guarantee and it is genuinely useful: "
             "sorting by `L`, with process identifiers breaking ties, gives a total order "
             "that never puts an effect before its cause."),
            ("A smaller stamp is not evidence of anything",
             "The converse fails and it fails often. On this diagram `L(B1) = 1` and "
             "`L(A2) = 2`, yet no chain of process order and messages runs from `B1` to "
             "`A2` — they are concurrent. There are `17` such pairs here. What `L(a) &lt; "
             "L(b)` does rule out is `b → a`, by the contrapositive of soundness, and that "
             "is all it rules out."),
        ],
        "read_title": "The rule, the guarantee, and the direction that fails",
        "read_intro": (
            "How the counters propagate along a diagram, what the resulting order "
            "promises, and a pair of events it gets the wrong way round."
        ),
        "body": [
            ("def", ("Happens-before, and the Lamport timestamp",
                     "Event `a` <strong>happens before</strong> `b`, written `a → b`, if "
                     "they are on the same process and `a` is earlier, or `a` is the send "
                     "of a message whose receive is `b`, or there is a chain of such steps "
                     "from `a` to `b`. The <strong>Lamport timestamp</strong> `L` assigns "
                     "each event `max(L_local, L_msg) + 1`, where `L_msg` is the stamp "
                     "carried by a received message and is absent otherwise.")),
            ("p", "Happens-before is a partial order, not a total one: it is the "
                  "transitive closure of “same process, earlier” and “sent, then "
                  "received”, and any two events not connected by such a chain are "
                  "unrelated by it. A Lamport clock takes that partial order and produces "
                  "integers consistent with it."),
            ("math", [
                "processes A (4 events), B (4 events), C (3 events)",
                "messages   A2 → B2      B3 → C2      C1 → A4",
                "",
                "  A    A1 = 1    A2 = 2    A3 = 3    A4 = 4",
                "  B    B1 = 1    B2 = 3    B3 = 4    B4 = 5",
                "  C    C1 = 1    C2 = 5    C3 = 6",
                "",
                "the three receives, worked",
                "  B2 = max(L(B1), L(A2)) + 1 = max(1, 2) + 1 = 3",
                "  C2 = max(L(C1), L(B3)) + 1 = max(1, 4) + 1 = 5",
                "  A4 = max(L(A3), L(C1)) + 1 = max(3, 1) + 1 = 4",
            ]),
            ("p", "The third receive is the instructive one. The message from `C1` carries "
                  "the stamp `1`, which is smaller than `A`'s own counter at that point, "
                  "so the local clock wins the maximum and `A4` becomes `4` rather than "
                  "`2`. A reader who adds one to the message stamp instead of to the "
                  "maximum gets a stamp that violates `A`'s own process order, which is "
                  "the first thing to check when a diagram comes out wrong."),
            ("h3", "The direction that fails"),
            ("math", [
                "L(B1) = 1 and L(A2) = 2, so L(B1) < L(A2)",
                "",
                "but is there a chain B1 → … → A2 ?",
                "  B1 → B2 → B3 → C2 → C3        and C3 sends nothing",
                "  the only message into A is from C1, which B cannot reach",
                "  so no: B1 and A2 are concurrent",
                "",
                "on this diagram",
                "  ordered pairs, a → b                             32",
                "  pairs with L(a) < L(b) and a NOT before b        17",
            ]),
            ("p", "Seventeen against thirty-two is not a rare corner case, it is a third of "
                  "the ordered-looking pairs on a small diagram. A Lamport stamp is a "
                  "one-dimensional summary of a partial order, and the information it "
                  "cannot carry is exactly the information about which pairs are "
                  "unrelated."),
            ("example", ("Why a total order is useful anyway",
                         "Break ties by process identifier and the stamps give a total "
                         "order on all events, consistent with causality. That is enough "
                         "for a distributed mutual-exclusion queue, for a deterministic "
                         "replay of a log, and for any rule of the form “process requests "
                         "in a fixed order that everyone agrees on”. What it is not enough "
                         "for is detecting that two updates were concurrent, because the "
                         "total order cheerfully orders pairs that nothing ordered — and "
                         "a merge that trusts it will silently pick a winner between two "
                         "updates that should both have been kept.")),
            ("p", "So the honest summary is: Lamport stamps are a cheap way to get an "
                  "order everyone agrees on, and a wrong way to decide whether one event "
                  "caused another. One integer per process is all they cost and it is also "
                  "all they can carry. “Vector Clocks and Concurrency” spends `n` integers "
                  "instead and gets the missing direction back."),
        ],
        "lab": ("replica", {
            "mode": "lamport",
            "panel_title": "Edit the message diagram",
            "panel_intro": "The stamps propagate along the diagram you type, in a "
                           "topological order of the events, by the rule and nothing else. "
                           "Draw the diagram on paper and stamp it yourself before "
                           "reading the panel — it is mechanical once the edges are "
                           "visible and confusing before.",
        }),
        "steps_title": "Stamping a diagram",
        "steps_intro": (
            "Draw first, stamp second. Most errors in this arithmetic are errors about "
            "which edges exist, not about the maximum."
        ),
        "steps": [
            ("Draw the processes as lines and the messages as arrows between them",
             "One horizontal line per process, events as dots along it in order, an arrow "
             "from each send to its receive. Everything that follows reads off this "
             "picture, and a missing arrow is invisible in a list of stamps."),
            ("Work through the events in a topological order",
             "An event can be stamped once every event with an edge into it has been. "
             "Going left to right on each process, deferring a receive until its send is "
             "stamped, is enough."),
            ("Apply the rule case by case",
             "Local event: `L + 1`. Send: `L + 1`, and put that value on the message. "
             "Receive: `max(own L, message L) + 1`. The commonest slip is adding one to "
             "the message's stamp rather than to the maximum, which breaks process order "
             "whenever the local clock was ahead."),
            ("Look for a pair the stamps order that the diagram does not",
             "Pick two events on different processes with different stamps and try to "
             "trace a chain from the smaller to the larger. If you cannot, you have found "
             "one of the pairs where the total order is inventing an order — and knowing "
             "that such pairs exist is the point of the exercise."),
        ],
        "worked": {
            "title": "Stamping eleven events, then finding the false pair",
            "intro": [
                "Three processes, eleven events, three messages. The stamps are mechanical; "
                "the interesting part is the last third of the page, where a pair of "
                "stamps says something the diagram does not support.",
            ],
            "lines": [
                "A: 4 events    B: 4 events    C: 3 events",
                "messages   A2 → B2      B3 → C2      C1 → A4",
                "",
                "process A",
                "  A1 = 0 + 1 = 1",
                "  A2 = 1 + 1 = 2          (send, message carries 2)",
                "  A3 = 2 + 1 = 3",
                "  A4 = max(3, 1) + 1 = 4  (receive from C1, which carried 1)",
                "",
                "process B",
                "  B1 = 0 + 1 = 1",
                "  B2 = max(1, 2) + 1 = 3  (receive from A2)",
                "  B3 = 3 + 1 = 4          (send, message carries 4)",
                "  B4 = 4 + 1 = 5",
                "",
                "process C",
                "  C1 = 0 + 1 = 1          (send, message carries 1)",
                "  C2 = max(1, 4) + 1 = 5  (receive from B3)",
                "  C3 = 5 + 1 = 6",
                "",
                "check soundness on the three messages",
                "  A2 = 2 < 3 = B2     B3 = 4 < 5 = C2     C1 = 1 < 4 = A4     all hold",
                "",
                "now the counterexample",
                "  L(B1) = 1 < 2 = L(A2),  but no chain runs B1 → A2",
                "  such pairs on this diagram: 17",
            ],
            "after": [
                "The stamps are correct and the guarantee holds in the direction it "
                "claims: every message is stamped so that the receive is strictly after "
                "the send, and every process's own events increase. Sorting all eleven by "
                "stamp, with ties broken by process name, gives an order no observer could "
                "prove wrong.",
                "And `B1` before `A2` is a fiction that order contains. Both are first "
                "or second events on their own processes, neither has heard of the other, "
                "and the stamps nonetheless place one before the other because integers "
                "are totally ordered and the events are not. Seventeen of the pairs here "
                "are like that.",
                "For a faded rehearsal, add a fourth message `A3 → C3` to the diagram. The "
                "supplied first move is that `C3` is now a receive rather than a local "
                "event, so its stamp becomes `max(L(C2), L(A3)) + 1`. Restamp every event "
                "that changes, say whether the number of false pairs should rise or fall "
                "and why, then check both against the lab.",
            ],
        },
        "quiz_title": "Stamps, and what they prove",
        "quiz": [
            {"q": "`B1` has stamp `1` and receives nothing. `B2` is the receive of a message sent by `A2`, which has stamp `2`. What is `L(B2)`?",
             "a": ["`2`", "`3`", "`4`", "`5`"],
             "c": 1,
             "why": "`max(L(B1), L(A2)) + 1 = max(1, 2) + 1 = 3`. `2` is the message's own "
                    "stamp, copied without the increment — which would make the receive "
                    "simultaneous with the send. `4` is `B3` and `5` is `B4`, one and two "
                    "steps further along."},
            {"q": "`A3` has stamp `3`, and `A4` is the receive of a message from `C1`, which carried stamp `1`. What is `L(A4)`?",
             "a": ["`2`", "`4`", "`5`", "`6`"],
             "c": 1,
             "why": "`max(3, 1) + 1 = 4`: the local clock is ahead of the message, so it "
                    "wins the maximum. `2` is what you get by incrementing the message's "
                    "stamp instead of the maximum, and it would place `A4` before `A3` on "
                    "`A`'s own line — which is the signal that the rule was misapplied."},
            {"q": "Two events have `L(a) = 3` and `L(b) = 5`. What follows?",
             "a": ["`a` happened before `b`",
                   "`b` did not happen before `a`",
                   "`a` and `b` are concurrent",
                   "`a` and `b` are on different processes"],
             "c": 1,
             "why": "Soundness says `b → a` would force `L(b) &lt; L(a)`, so `L(a) &lt; L(b)` "
                    "rules `b → a` out — and nothing else. `a` may have happened before "
                    "`b` or may be concurrent with it; on the diagram in this lesson there "
                    "are `17` pairs where the stamps are ordered and the events are not. "
                    "The processes may also be the same one, where consecutive events "
                    "always have increasing stamps."},
        ],
        "mistakes": [
            ("Reading a smaller stamp as “earlier”",
             "The implication runs one way only. `L(a) &lt; L(b)` means `b` did not happen "
             "before `a`, which is weaker than `a` happened before `b` and very much "
             "weaker than “`a` is earlier in time”. Any code that decides which of two "
             "updates to keep by comparing Lamport stamps is silently resolving "
             "concurrency by an arbitrary rule."),
            ("Incrementing the message's stamp rather than the maximum",
             "On a receive the rule is `max(own, message) + 1`, and the `max` matters "
             "precisely when the receiving process is ahead. Getting it wrong produces "
             "stamps that decrease along a process line, which is both obviously wrong on "
             "the diagram and easy to miss in a table of numbers — checking that each "
             "process's own stamps increase catches it immediately."),
            ("Expecting Lamport stamps to detect a conflict",
             "They cannot, by construction: a total order has no way to say “these two are "
             "unrelated”. Two concurrent updates always get different stamps and the "
             "larger always looks later. If the question is whether two writes conflict, "
             "the answer needs one counter per process rather than one in total, which is "
             "the next lesson."),
        ],
        "standard": ("Finish when you can stamp a diagram in one pass and name a pair the stamps order wrongly.",
                     "You should be able to apply the three cases of the rule without "
                     "hesitation, check soundness along every message, produce a total "
                     "order by breaking ties on process identity, and exhibit two "
                     "concurrent events whose stamps are nevertheless ordered."),
        "note": "One integer per process cannot record which processes have heard of an "
                "event, only how many steps have happened somewhere. “Vector Clocks and "
                "Concurrency” spends one integer per process instead, which is enough to "
                "answer the question Lamport stamps cannot — and turns “are these two "
                "updates in conflict” into a count.",
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "vector-clocks-and-concurrency",
        "title": "Vector Clocks and Concurrency",
        "module": "Clocks and order",
        "one_line": "Stamp a diagram with vectors and count the pairs of events that are concurrent.",
        "summary": (
            "A vector clock carries one counter per process, merged by elementwise "
            "maximum, and it makes happens-before decidable in both directions: `e → f` "
            "exactly when `V(e) ≤ V(f)` componentwise and the vectors differ. When neither "
            "vector dominates the other the events are <em>concurrent</em> — unordered by "
            "any chain of messages. On the same eleven-event diagram, `23` of the `55` "
            "pairs are concurrent, and those are precisely the pairs a merge will have to "
            "decide."
        ),
        "key": [
            "V(e) ≤ V(f) componentwise and V(e) ≠ V(f)    ⟺    e → f",
            "neither vector dominates the other           ⟺    concurrent",
            "on a receive: elementwise max, then increment your own component",
            "same 11 events:  55 pairs,  32 ordered,  23 concurrent",
            "concurrent means unordered by information, not simultaneous in time",
        ],
        "key_label": "A partial order, and the pairs it leaves unordered",
        "concepts_intro": (
            "One counter per process, a comparison that can fail in both directions, and a "
            "word that does not mean what it sounds like."
        ),
        "concepts": [
            ("One counter per process, merged by elementwise maximum",
             "Process `i` keeps a vector `V` and increments `V[i]` at each of its own "
             "events. A message carries the sender's whole vector; on receipt the "
             "receiver takes the elementwise maximum with its own and then increments its "
             "own component. The vector is therefore a record of how much of each "
             "process's history this event knows about."),
            ("Comparison is componentwise, and it can fail both ways",
             "`V(e) ≤ V(f)` means every component of `V(e)` is at most the matching "
             "component of `V(f)`. If that holds and the vectors differ, `e → f`. If "
             "neither `V(e) ≤ V(f)` nor `V(f) ≤ V(e)`, there is no chain either way and "
             "the events are <strong>concurrent</strong>. Unlike a single integer, a "
             "vector can simply refuse to compare, and that refusal is the answer."),
            ("Concurrent is a statement about information, not about time",
             "`A3` and `C3` on this diagram are concurrent, and they may have occurred a "
             "minute apart on any wall clock. What makes them concurrent is that neither "
             "process had heard anything of the other's event when its own occurred. "
             "Concurrency here means “unordered by any chain of messages”, and it is "
             "exactly the condition under which two updates conflict."),
        ],
        "read_title": "Vectors, comparison, and the pairs that refuse to order",
        "read_intro": (
            "How the vectors propagate, what the componentwise comparison decides, and why "
            "the count of concurrent pairs is the useful output."
        ),
        "body": [
            ("def", ("Vector clock, and concurrency",
                     "A <strong>vector clock</strong> on `n` processes assigns each event "
                     "a vector `V` of `n` counters. Process `i` increments `V[i]` at each "
                     "of its events; a receive first takes the elementwise maximum with "
                     "the vector carried by the message. Then `e → f` if and only if "
                     "`V(e) ≤ V(f)` componentwise with `V(e) ≠ V(f)`, and `e` and `f` are "
                     "<strong>concurrent</strong> if neither comparison holds.")),
            ("p", "The “if and only if” is what a Lamport stamp could not offer. A single "
                  "integer can be compared with any other integer, so it always produces "
                  "an answer even when there is no answer to produce; a vector produces "
                  "three possible outcomes — before, after, or neither — and the third is "
                  "as informative as the others."),
            ("math", [
                "components in the order (A, B, C)",
                "messages   A2 → B2      B3 → C2      C1 → A4",
                "",
                "  A    A1 (1,0,0)   A2 (2,0,0)   A3 (3,0,0)   A4 (4,0,1)",
                "  B    B1 (0,1,0)   B2 (2,2,0)   B3 (2,3,0)   B4 (2,4,0)",
                "  C    C1 (0,0,1)   C2 (2,3,2)   C3 (2,3,3)",
                "",
                "the three receives, worked",
                "  B2 = max((0,1,0), (2,0,0)) then +1 in B = (2,2,0)",
                "  C2 = max((0,0,1), (2,3,0)) then +1 in C = (2,3,2)",
                "  A4 = max((3,0,0), (0,0,1)) then +1 in A = (4,0,1)",
            ]),
            ("p", "Read `C3 = (2,3,3)` as a sentence: this event knows about the first two "
                  "events of `A`, the first three of `B`, and is `C`'s own third. That is "
                  "the whole content of a vector clock, and every ordering question is "
                  "answered by comparing two such sentences."),
            ("h3", "Counting the concurrent pairs"),
            ("math", [
                "pairs in total              C(11,2) = 55",
                "ordered, one dominates the other       32",
                "concurrent, neither dominates          23     = 41.8% of all pairs",
                "",
                "a worked comparison",
                "  A2 (2,0,0)   vs   B1 (0,1,0)",
                "    A2 ≤ B1 ?   2 ≤ 0 is false",
                "    B1 ≤ A2 ?   1 ≤ 0 is false",
                "    neither: concurrent",
                "",
                "and one that does order",
                "  A1 (1,0,0)   vs   C3 (2,3,3)",
                "    1 ≤ 2,  0 ≤ 3,  0 ≤ 3,  and the vectors differ",
                "    so A1 → C3, along A1 → A2 → B2 → B3 → C2 → C3",
            ]),
            ("p", "Twenty-three of fifty-five is not an anomaly of this diagram, it is what "
                  "a system with few messages looks like. Concurrency is the default and "
                  "ordering is what communication buys, so a system that gossips rarely "
                  "has a great many concurrent pairs and a system that synchronises "
                  "constantly has few — and pays for the difference in messages."),
            ("example", ("Concurrent is not simultaneous",
                         "`A3 = (3,0,0)` and `C3 = (2,3,3)`. Compare: `3 ≤ 2` fails, so "
                         "`A3` does not precede `C3`; and `3 ≤ 0` fails in the middle "
                         "component, so `C3` does not precede `A3`. They are concurrent — "
                         "and `C3` is the last event on its process while `A3` is in the "
                         "middle of another, so on a wall clock they could be seconds or "
                         "minutes apart. The vectors are not claiming they happened at the "
                         "same moment. They are claiming that neither process could "
                         "possibly have known about the other's event, which is the "
                         "condition under which two updates to the same key are a conflict "
                         "rather than an overwrite.")),
            ("p", "That is what the count is for. Every concurrent pair touching the same "
                  "data is a decision somebody has to make — keep one, keep both, merge "
                  "them — and “Conflict Resolution, Counted” is where those decisions get "
                  "priced. The vector clock's job ends at identifying them, and it does "
                  "that exactly, which is more than any single number can do."),
        ],
        "lab": ("replica", {
            "mode": "vector",
            "panel_title": "Edit the same message diagram",
            "panel_intro": "The vectors propagate along the diagram you type and every "
                           "pair is compared elementwise, with each incomparable pair "
                           "listed by name. Compare the listing against the stamps the "
                           "previous lesson produced on this same diagram.",
        }),
        "steps_title": "Stamping with vectors and reading off the conflicts",
        "steps_intro": (
            "The propagation is mechanical. The part worth slowing down for is the "
            "comparison, which has three outcomes and not two."
        ),
        "steps": [
            ("Fix the component order and keep it",
             "Decide once that the vector is `(A, B, C)` and write every vector that way. "
             "Most arithmetic errors here are a component written in the wrong slot, and "
             "they are invisible until a comparison comes out strangely."),
            ("Increment your own component at every event, including sends and receives",
             "A send is an event on the sender and a receive is an event on the receiver, "
             "so both increment. Forgetting the increment on a send makes the send and the "
             "message's previous event compare as equal."),
            ("On a receive, take the elementwise maximum first, then increment",
             "Maximum with the message's vector, then `+1` in your own slot. The order "
             "matters: incrementing first and then taking the maximum can lose your own "
             "increment if the message was ahead in your component, which it should never "
             "be but will be if an earlier step was wrong."),
            ("Compare in both directions before concluding anything",
             "Ask whether `V(e) ≤ V(f)`, then whether `V(f) ≤ V(e)`. Two failures mean "
             "concurrent; one success means ordered; two successes mean the vectors are "
             "equal and you have compared an event with itself."),
        ],
        "worked": {
            "title": "The same diagram, stamped with vectors",
            "intro": [
                "The same three processes and three messages as before. The stamps this "
                "time are vectors, and the output is not an order but a census: how many "
                "of the fifty-five pairs are ordered and how many are conflicts waiting to "
                "happen.",
            ],
            "lines": [
                "components (A, B, C);  messages A2 → B2, B3 → C2, C1 → A4",
                "",
                "  A1 (1,0,0)    A2 (2,0,0)    A3 (3,0,0)    A4 (4,0,1)",
                "  B1 (0,1,0)    B2 (2,2,0)    B3 (2,3,0)    B4 (2,4,0)",
                "  C1 (0,0,1)    C2 (2,3,2)    C3 (2,3,3)",
                "",
                "three comparisons",
                "",
                "  A2 (2,0,0) vs B1 (0,1,0)     2 ≤ 0 no,  1 ≤ 0 no    concurrent",
                "  A1 (1,0,0) vs C3 (2,3,3)     1 ≤ 2, 0 ≤ 3, 0 ≤ 3    A1 → C3",
                "  A3 (3,0,0) vs C3 (2,3,3)     3 ≤ 2 no,  3 ≤ 0 no    concurrent",
                "",
                "the census",
                "  pairs in total        C(11,2) = 55",
                "  ordered                            32",
                "  concurrent                         23",
                "",
                "and the comparison with the previous lesson's stamps",
                "  Lamport ordered 49 of these pairs by stamp, of which 17 were",
                "  pairs the vectors call concurrent",
            ],
            "after": [
                "The second and third comparisons are the ones to sit with. `A1` and `A3` "
                "are two events on the same process, one before the other, and the "
                "vectors say that the earlier one precedes `C3` while the later one does "
                "not. That is not a contradiction: `A1`'s information reached `C` through "
                "the chain of messages and `A3`'s did not, because `A3` happened after "
                "`A` had already sent everything it was going to send.",
                "Twenty-three concurrent pairs on eleven events is the real output. If "
                "those events were updates to one key, twenty-three of the pairs would "
                "need a merge rule and thirty-two would not — and no amount of clock "
                "accuracy changes that split, because it is a fact about which messages "
                "were sent.",
                "For a faded rehearsal, delete the message `C1 → A4` from the diagram. The "
                "supplied first move is that `A4` becomes a local event, so its vector is "
                "`(4,0,0)` rather than `(4,0,1)`. Restamp what changes, predict whether "
                "the concurrent count rises or falls, then compute it and check against "
                "the lab.",
            ],
        },
        "quiz_title": "Vectors, comparison and conflict",
        "quiz": [
            {"q": "`B1` is `(0,1,0)` and receives a message from `A2`, which carries `(2,0,0)`. What vector does the receiving event `B2` get?",
             "a": ["`(2,2,0)`", "`(2,1,0)`", "`(1,2,0)`", "`(2,0,0)`"],
             "c": 0,
             "why": "Elementwise maximum of `(0,1,0)` and `(2,0,0)` is `(2,1,0)`, then "
                    "increment `B`'s own component: `(2,2,0)`. `(2,1,0)` is the maximum "
                    "without the increment, `(2,0,0)` is the message copied over the "
                    "receiver's own history, and `(1,2,0)` has the components swapped."},
            {"q": "`A3` is `(3,0,0)` and `C3` is `(2,3,3)`. What is their relation?",
             "a": ["`A3 → C3`", "`C3 → A3`", "They are concurrent", "They are the same event"],
             "c": 2,
             "why": "`A3 ≤ C3` fails in the first component (`3 ≤ 2` is false) and "
                    "`C3 ≤ A3` fails in the second (`3 ≤ 0` is false). Neither dominates, "
                    "so no chain of messages connects them in either direction. Note that "
                    "a single component disagreeing each way is all it takes."},
            {"q": "Two updates to the same key are stamped with concurrent vectors. What does that tell you?",
             "a": ["They happened at the same instant on the wall clock",
                   "Neither update's process had heard of the other's when it made it, so the two conflict and a merge rule must decide",
                   "One of them is stale and should be discarded",
                   "The vectors were computed incorrectly, since every event has a time"],
             "c": 1,
             "why": "Concurrency is about information, not about time: the two may be far "
                    "apart on any clock and are concurrent because no chain of messages "
                    "connects them. Neither is stale — that word requires an order, and "
                    "there is not one — which is precisely why a merge rule is needed. "
                    "Incomparable vectors are the expected output on any system that "
                    "accepts writes in more than one place."},
        ],
        "mistakes": [
            ("Reading concurrent as simultaneous",
             "The word is borrowed and it misleads. Two concurrent events can be minutes "
             "apart in real time; what they cannot be is causally connected. Conversely "
             "two events at the same instant on synchronised clocks may be perfectly "
             "ordered if a message ran between them. The vectors know nothing about clocks "
             "and everything about messages."),
            ("Comparing vectors by their sum, or by one component",
             "`A3 = (3,0,0)` sums to `3` and `C3 = (2,3,3)` sums to `8`, which would order "
             "them — and they are concurrent. Any collapse of the vector to a single "
             "number reintroduces exactly the defect of a Lamport stamp, because a single "
             "number is always comparable. The comparison must be componentwise and it "
             "must be tried in both directions."),
            ("Expecting the vector to say which concurrent update is right",
             "It says they conflict and nothing more, which is its job done correctly. "
             "Choosing between them, or merging them, is a decision about the data rather "
             "than about the ordering — and a merge that always picks the larger vector, "
             "or the later arrival, is making that decision by accident rather than by "
             "design."),
        ],
        "standard": ("Finish when an incomparable pair of vectors reads as “a merge decision”, not as an error.",
                     "You should be able to propagate vectors along a diagram including "
                     "sends and receives, compare two vectors in both directions and "
                     "report one of three outcomes, count the concurrent pairs, and say "
                     "what a concurrent pair implies about two updates to one key."),
        "note": "Both clocks so far count events rather than seconds, which is what makes "
                "them exact. The temptation is always to use the machine's own wall clock "
                "instead, since it needs no messages at all. “Physical Clocks and Drift” "
                "computes how wrong that is: a drift rate and a sync interval give an "
                "uncertainty window, and any two events closer together than the window "
                "cannot be ordered by a timestamp at all.",
    },
    # ---------------------------------------------------------------- 11
    {
        "slug": "physical-clocks-and-drift",
        "title": "Physical Clocks and Drift",
        "module": "Clocks and order",
        "one_line": "Compute the clock uncertainty window from a drift rate and a sync interval, and the commit-wait it forces.",
        "summary": (
            "A clock drifting at `200` parts per million and corrected every `30` seconds "
            "can be `ε = 6 ms` out of true at the worst moment, and two such clocks can "
            "differ by `2ε = 12 ms`. Any two events whose true separation is smaller than "
            "that window — say `5 ms` — cannot be ordered by their timestamps at all, in "
            "either direction. Waiting `2ε` before making a commit visible converts the "
            "bound into an order, and costs `12 ms` per dependent commit to do it."
        ),
        "key": [
            "ppm is microseconds per second, exactly",
            "ε = drift × interval        200 ppm × 30 s = 6000 µs = 6 ms",
            "two clocks differ by up to 2ε = 12 ms",
            "true gap 5 ms  <  12 ms   ⟹   a wall clock cannot order the two events",
            "commit-wait of 2ε turns the bound into an order, at 12 ms a commit",
        ],
        "key_label": "One clock's error, and the window two of them make",
        "concepts_intro": (
            "An exact unit conversion, a factor of two, and the price of turning an error "
            "bound into an ordering."
        ),
        "concepts": [
            ("Parts per million is microseconds per second",
             "A drift of `200` ppm means the clock gains or loses `200` microseconds every "
             "second, so over a `30`-second correction interval it can be `6000` "
             "microseconds — `6 ms` — away from true at the moment just before the next "
             "correction. The conversion is exact and it is the only arithmetic in the "
             "lesson; everything else is a consequence of it."),
            ("Two clocks make a window twice as wide",
             "One clock may be up to `ε` fast and another up to `ε` slow, so the "
             "difference between two readings of the same instant can be as much as `2ε`. "
             "That `2ε` is the <strong>uncertainty window</strong>, and it is the quantity "
             "that matters, because ordering two events always means comparing two clocks."),
            ("Inside the window there is no order to read",
             "If two events are truly `5 ms` apart and the window is `12 ms`, the "
             "timestamps can say the first came first, the second came first, or that they "
             "were simultaneous, and all three readings are consistent with the same true "
             "order. A commit-wait of `2ε` — hold the result until the window has passed — "
             "restores an ordering, and its cost is `2ε` per commit that something else "
             "must see."),
        ],
        "read_title": "Drift, the window, and the wait that buys an order",
        "read_intro": (
            "The exact conversion from a drift rate, why the window is twice one clock's "
            "error, and what it costs to get an ordering back."
        ),
        "body": [
            ("def", ("Drift, skew, and the uncertainty window",
                     "<strong>Drift</strong> is the rate at which a clock departs from "
                     "true time, quoted in parts per million. Between corrections at "
                     "interval `I`, a clock accumulates an error of up to "
                     "`ε = drift × I`. Two clocks may be out in opposite directions, so "
                     "the <strong>uncertainty window</strong> within which their readings "
                     "cannot be compared is `2ε`.")),
            ("p", "Time synchronisation does not make clocks equal. It corrects them "
                  "periodically, which bounds the error and restarts the accumulation; "
                  "between corrections the drift resumes at the same rate. A cluster "
                  "running a time daemon has clocks within a window, not clocks that "
                  "agree, and the size of that window is a design input rather than a "
                  "detail."),
            ("math", [
                "drift 200 ppm, corrected every 30 s",
                "",
                "  200 ppm = 200 µs per second",
                "  ε  = 200 µs/s × 30 s = 6000 µs = 6 ms      one clock, worst case",
                "  2ε = 12 000 µs = 12 ms                     two clocks, against each other",
                "",
                "the same clock, corrected more often",
                "  every 1 s      ε =  200 µs      2ε =  400 µs",
                "  every 10 s     ε = 2000 µs      2ε = 4000 µs",
                "  every 600 s    ε = 120 ms       2ε = 240 ms",
            ]),
            ("p", "The window is linear in both inputs, which makes the two levers obvious "
                  "and their prices very different. Halving the drift means better "
                  "oscillators in every machine; halving the interval means twice the "
                  "synchronisation traffic and is nearly free. That asymmetry is why "
                  "tight-clock systems synchronise aggressively rather than buying exotic "
                  "hardware, up to the point where the network round trip becomes the "
                  "floor on the error."),
            ("h3", "The order the window cannot decide"),
            ("math", [
                "event X on node 1, event Y on node 2, truly 5 ms apart",
                "",
                "  true separation        5 000 µs",
                "  comparison window     12 000 µs",
                "  window ÷ separation   12/5 = 2.4×",
                "",
                "the timestamps can report X first, Y first, or the same instant,",
                "and every one of those readings is consistent with the true order",
            ]),
            ("p", "This is why a timestamp comparison is not an ordering primitive. It "
                  "answers instantly and it answers wrongly whenever the answer was close, "
                  "which is exactly the case anyone bothers to ask about — two events far "
                  "apart in time are rarely in dispute. The failure is silent, it is "
                  "data-dependent, and it disappears on a single machine, which is where "
                  "the code was tested."),
            ("example", ("What the commit-wait costs",
                         "Hold each commit for `2ε = 12 ms` before making it visible and "
                         "the window is guaranteed to have closed, so any commit a reader "
                         "can see really did happen before anything it observes "
                         "afterwards. The price is `12 ms` added to every dependent "
                         "commit: a chain of commits that must each be visible before the "
                         "next begins is capped near `1000/12 ≈ 83` a second, however fast "
                         "the hardware is. Halve the sync interval and that cap doubles, "
                         "which is the direct reason such systems care about how often "
                         "their clocks are corrected.")),
            ("p", "Two honest positions follow and they are both defensible. Either carry "
                  "the uncertainty explicitly — a timestamp is an interval, not a point, "
                  "and you wait when the intervals overlap — or do not use physical clocks "
                  "for ordering at all and use the counters of the previous two lessons, "
                  "which cost messages instead of milliseconds. What is not defensible is "
                  "comparing two raw timestamps from two machines and treating the result "
                  "as an order."),
        ],
        "lab": ("replica", {
            "mode": "drift",
            "panel_title": "Set the clock and the two events",
            "panel_intro": "Parts per million are microseconds per second, so every figure "
                           "here is an exact product. Drag the true separation below the "
                           "window and watch the verdict flip from an order to a refusal "
                           "to give one.",
        }),
        "steps_title": "Computing a clock uncertainty window",
        "steps_intro": (
            "Two multiplications and a comparison. The discipline is remembering the factor "
            "of two and never dropping the units."
        ),
        "steps": [
            ("Convert the drift to microseconds per second",
             "Parts per million already is microseconds per second, so there is nothing to "
             "convert — `200` ppm is `200 µs/s`. Writing the units down is what keeps the "
             "next step honest."),
            ("Multiply by the correction interval to get `ε`",
             "`ε = drift × interval`, the worst-case error of one clock just before its "
             "next correction. At `200` ppm and `30` seconds, `6000 µs = 6 ms`. This is a "
             "bound, not a typical value; typical is better and the bound is what you can "
             "rely on."),
            ("Double it, because ordering compares two clocks",
             "`2ε` is the window. Forgetting the factor of two is the commonest error here "
             "and it halves a safety margin, which is the direction that produces incidents "
             "rather than slowdowns."),
            ("Compare the window with the separation you need to resolve",
             "If the true gap between the events you must order is smaller than `2ε`, "
             "timestamps cannot order them and you need either a commit-wait of `2ε`, a "
             "tighter window, or a logical clock. Say which of the three you chose."),
        ],
        "worked": {
            "title": "200 ppm, thirty seconds, and a five-millisecond gap",
            "intro": [
                "Two nodes, each with a clock specified at `200` parts per million and "
                "corrected every `30` seconds. Two events happen on them, truly `5 ms` "
                "apart, and a piece of code is about to order them by comparing "
                "timestamps.",
            ],
            "lines": [
                "drift 200 ppm = 200 µs per second",
                "correction interval 30 s",
                "",
                "  ε  = 200 × 30 = 6000 µs = 6 ms",
                "  2ε = 12 000 µs = 12 ms",
                "",
                "the two events",
                "  true separation 5000 µs = 5 ms",
                "  5 ms is INSIDE the 12 ms window",
                "  window ÷ separation = 2.4×",
                "",
                "so the timestamp comparison is not an ordering:",
                "  node 1 up to 6 ms fast, node 2 up to 6 ms slow  → X reads first",
                "  node 1 up to 6 ms slow, node 2 up to 6 ms fast  → Y reads first",
                "  both correct                                    → X reads first",
                "",
                "the repairs",
                "  commit-wait 2ε         12 ms per dependent commit, ≈ 83/s serially",
                "  sync every 1 s         ε = 200 µs, 2ε = 400 µs, 5 ms now resolvable",
                "  logical clocks         no window at all, at the cost of messages",
            ],
            "after": [
                "The third line of the repairs is the one most systems take, and it is "
                "worth seeing why: shrinking the interval from `30` seconds to `1` second "
                "shrinks the window by a factor of thirty, from `12 ms` to `400 µs`, and "
                "the `5 ms` gap is then comfortably outside it. Synchronisation traffic is "
                "cheap and oscillators are not.",
                "The commit-wait line is the one that shows up as a throughput number in a "
                "design review. `83` dependent commits a second is a real ceiling, and it "
                "is set entirely by `2ε` — which means a team that wants more of them is "
                "really asking for a tighter clock, whether or not anybody has said so.",
                "For a faded rehearsal, the hardware is replaced with clocks specified at "
                "`50` ppm and the sync interval is left at `30` seconds. The supplied "
                "first move is `ε = 50 × 30 = 1500 µs`. Compute `2ε`, say whether the "
                "`5 ms` gap is now resolvable, work out the commit-wait ceiling at that "
                "window, and check all three in the lab.",
            ],
        },
        "quiz_title": "Drift, windows and what they forbid",
        "quiz": [
            {"q": "A clock drifts at `200` parts per million and is corrected every `30` seconds. What is its worst-case error just before a correction?",
             "a": ["`6 ms`", "`6 µs`", "`60 ms`", "`0.2 ms`"],
             "c": 0,
             "why": "`200` ppm is `200 µs` per second, and `200 × 30 = 6000 µs = 6 ms`. "
                    "`6 µs` is the error after a thousandth of the interval; `60 ms` is "
                    "ten times too large; `0.2 ms` is the error after one second, which is "
                    "the drift rate itself rather than the accumulated error."},
            {"q": "Two nodes have that clock. Two events occur on them, truly `5 ms` apart. Can their timestamps be used to order the events?",
             "a": ["Yes — `5 ms` is close to one clock's `6 ms` error, so the comparison is only marginal",
                   "No — the window is `2ε = 12 ms`, and `5 ms` falls inside it, so either order is consistent with the timestamps",
                   "Yes, provided both nodes were recently synchronised",
                   "Yes, because the error cancels when both clocks drift the same way"],
             "c": 1,
             "why": "Comparing two clocks means the window is `2ε`, not `ε`, and `5 ms` is "
                    "well inside `12 ms`. Recent synchronisation lowers the typical error "
                    "but the specification is a bound, and drift resumes immediately. The "
                    "errors cancel only if the two clocks happen to be wrong in the same "
                    "direction by the same amount, which is one case out of the range the "
                    "bound covers."},
            {"q": "Which change actually shrinks the window, and by how much?",
             "a": ["Running a time daemon, which makes the clocks equal",
                   "Correcting every `1` second instead of every `30`, which cuts `2ε` from `12 ms` to `400 µs`",
                   "Adding more nodes, which averages the errors out",
                   "Using a longer correction interval, so fewer corrections disturb the clock"],
             "c": 1,
             "why": "The window is `2 × drift × interval`, linear in the interval, so "
                    "correcting thirty times as often makes it thirty times smaller. A "
                    "time daemon is what performs the corrections — it bounds the error "
                    "rather than eliminating it. More nodes add more clocks and more "
                    "pairwise windows, and a longer interval makes the window larger, not "
                    "smaller."},
        ],
        "mistakes": [
            ("Believing that a time sync makes clocks equal",
             "It bounds their error and restarts the accumulation. Immediately after a "
             "correction the window is small and it grows linearly until the next one, so "
             "the number to design with is the error just before a correction, not just "
             "after it. “Our clocks are synchronised” is a statement about a bound whose "
             "value nobody has quoted."),
            ("Using `ε` where the window is `2ε`",
             "Ordering always compares two clocks and they can be wrong in opposite "
             "directions. Using one clock's error as the window halves the margin, which "
             "means a class of event pairs is declared orderable when it is not — and the "
             "wrong orderings are silent, data-dependent and absent on a single machine."),
            ("Comparing two machines' raw timestamps at all",
             "A timestamp from another machine is an interval of width `2ε` wearing the "
             "costume of a point. If you must use physical time for ordering, carry the "
             "uncertainty explicitly and wait when the intervals overlap; if you cannot "
             "afford the wait, use the event counters of “Lamport Clocks” and “Vector "
             "Clocks and Concurrency”, which have no window at all."),
        ],
        "standard": ("Finish when “the clocks are synchronised” prompts you to ask for the drift and the interval.",
                     "You should be able to convert parts per million into microseconds per "
                     "second, compute `ε` and `2ε` for any drift and interval, decide "
                     "whether a given separation is resolvable, price a commit-wait in "
                     "throughput, and name the three repairs with their costs."),
        "note": "Clocks were a way of ordering two events. The question underneath was "
                "always whether a whole history could be told as though every operation "
                "happened at one instant, and that has a definition and a decision "
                "procedure. “Linearizability by Enumeration” makes it a count — of total "
                "orders that real time allows and a register would accept — and zero of "
                "them is a violation.",
    },
    # ---------------------------------------------------------------- 12
    {
        "slug": "linearizability-by-enumeration",
        "title": "Linearizability by Enumeration",
        "module": "Consistency, counted",
        "one_line": "Count the total orders of a short history that real time allows and a register would accept.",
        "summary": (
            "A history of operations, each occupying an interval, is linearizable exactly "
            "when some total order of them respects real time — an operation that finished "
            "before another started must come first — and replays legally against the "
            "object. So enumerate the orders and count the survivors. Three operations give "
            "`6` orders, of which `3` respect real time and `0` are legal: a violation. "
            "Seven operations give `5040`, and the lab refuses, because the refusal is the "
            "lesson."
        ),
        "key": [
            "linearizable  ⟺  some total order is real-time respecting and legal",
            "real time: if a ends before b starts, a must come before b",
            "legal: replay against the object and every read returns what was written",
            "3 operations:  6 orders,  3 allowed by real time,  0 legal → a violation",
            "6 operations: 720 orders.  7: 5040, and the lab refuses to enumerate them",
        ],
        "key_label": "Two filters, and the count that survives both",
        "concepts_intro": (
            "An operation is an interval rather than an instant, two filters cut the "
            "orders down, and the number that survives is the verdict."
        ),
        "concepts": [
            ("An operation occupies an interval, not an instant",
             "A call starts when the client issues it and ends when the response arrives, "
             "and the operation may be considered to take effect at any single moment "
             "inside that interval. Two operations whose intervals overlap may therefore "
             "be placed in either order; two whose intervals do not overlap may not. This "
             "is the only role real time plays."),
            ("Real time filters the orders, the object decides which survive",
             "The first filter is mechanical: for every pair where one operation ended "
             "before the other started, keep only the orders putting them that way round. "
             "The second is a replay: run the surviving orders against the object — for a "
             "register, each read must return the value last written — and keep the ones "
             "that never contradict themselves."),
            ("Zero legal orders is the verdict, not an accusation",
             "If nothing survives both filters, the history is not linearizable, and that "
             "is a property of the history as a whole. It does not mean one particular "
             "replica returned a value it never held; every read in the violating history "
             "here returns a value that genuinely existed. The defect is that no single "
             "sequence of instants can explain all of them at once."),
        ],
        "read_title": "Two filters, a count, and the cap that is a lesson",
        "read_intro": (
            "What linearizability asks, how the enumeration answers it, and why no real "
            "checker works this way."
        ),
        "body": [
            ("def", ("History, real-time order, and a linearization",
                     "A <strong>history</strong> is a set of operations, each with a start "
                     "time, an end time and a return value. A <strong>linearization</strong> "
                     "is a total order of those operations such that `a` precedes `b` "
                     "whenever `a` ended before `b` started, and such that replaying them "
                     "in that order against the object is <strong>legal</strong> — every "
                     "read returns the most recently written value. A history is "
                     "<strong>linearizable</strong> if at least one linearization exists.")),
            ("p", "The definition is an existence claim, and that is what makes the "
                  "enumeration a decision procedure: generate every total order, apply the "
                  "two filters, and count. A count of zero settles the question in the "
                  "negative, and any count above zero settles it in the positive."),
            ("math", [
                "the register starts at 0",
                "",
                "  A   write 1    [0, 4]",
                "  B   read → 1   [2, 6]",
                "  C   read → 0   [5, 9]",
                "",
                "real time:  A ends at 4 and C starts at 5, so A must precede C",
                "            A and B overlap; B and C overlap; no other constraint",
            ]),
            ("p", "Nothing about this history looks wrong operation by operation. `B` read "
                  "`1`, which was written. `C` read `0`, which was the initial value. Both "
                  "are values the register genuinely held, and a system that checked each "
                  "response individually would report no problem at all."),
            ("math", [
                "order     real time      replay against a register starting at 0",
                "",
                "  A B C   A before C     w1,  r→1 ✓,  r→0 ✗   C reads 0 after the write",
                "  A C B   A before C     w1,  r→0 ✗",
                "  B A C   A before C     r→1 ✗   nothing written yet",
                "  B C A   C before A     rejected by real time",
                "  C A B   C before A     rejected by real time",
                "  C B A   C before A     rejected by real time",
                "",
                "  total orders                6",
                "  allowed by real time        3",
                "  legal                       0      the history is NOT linearizable",
            ]),
            ("p", "The verdict comes from the combination. `C` reading `0` would be fine if "
                  "it could be placed before the write, and real time forbids that because "
                  "`A` had already returned when `C` was issued. `B` reading `1` would be "
                  "fine anywhere after the write. It is the pair of constraints together "
                  "that leaves nothing, which is why linearizability is a property of "
                  "histories and not of responses."),
            ("h3", "Why the lab stops at six operations"),
            ("math", [
                "k       k!            what the enumeration costs",
                "3         6",
                "4        24",
                "5       120",
                "6       720           the cap the lab enforces",
                "7      5040           refused, with the number printed",
                "10  3 628 800",
                "20   2.4 × 10¹⁸",
            ]),
            ("p", "The growth is factorial, so the cap is not a limitation of the page, it "
                  "is the shape of the problem. Real checkers do not enumerate: they search "
                  "with pruning, commit operations greedily and backtrack, or check a "
                  "weaker property that is cheaper to decide. The lab refuses a seventh "
                  "operation and prints `5040` rather than quietly truncating, because a "
                  "silent truncation would teach the opposite of the thing worth learning."),
            ("example", ("One return value makes it legal",
                         "Change `C` to read `1` instead of `0` and nothing else about the "
                         "history moves — same intervals, same real-time constraint. Now "
                         "`A B C` replays as `w1, r→1, r→1`, which is legal, and `A C B` "
                         "does too. Two of the three real-time-respecting orders survive, "
                         "the count is `2`, and the history is linearizable. A single "
                         "returned value flipped the verdict, which is the sense in which "
                         "linearizability is a property of the whole history and a very "
                         "sharp one.")),
            ("p", "It is worth being precise about what this buys. Linearizability is the "
                  "guarantee that the system behaves as though there were one copy of the "
                  "data and every operation took effect at a single instant between its "
                  "call and its return. “Quorums Overlap” gave a much weaker property — no "
                  "acknowledged write is missed entirely — and the gap between the two is "
                  "the whole reason this lesson exists."),
        ],
        "lab": ("replica", {
            "mode": "linearize",
            "panel_title": "Edit the history",
            "panel_intro": "Every total order is generated, filtered by the real-time "
                           "order and replayed against a register; the count is exact and "
                           "zero is a violation. Try the seven-operation history and read "
                           "the refusal — the cap and its reason are part of the lesson.",
        }),
        "steps_title": "Deciding a short history",
        "steps_intro": (
            "Two filters in a fixed sequence, and a verdict that is a count rather than an "
            "opinion."
        ),
        "steps": [
            ("Write each operation as an interval with its return value",
             "Start, end, what it did, what it returned. A history without return values "
             "cannot be checked, and a history without intervals has no real-time "
             "constraints to apply."),
            ("Derive the real-time constraints pairwise",
             "For every pair, if one ended before the other started, that order is forced. "
             "If the intervals overlap, both orders remain open. Write the forced pairs "
             "down; they are usually far fewer than the pairs."),
            ("Enumerate the total orders and keep those respecting the constraints",
             "`k!` orders, filtered by the forced pairs. For small `k` this is a short "
             "list and worth writing out, because seeing which orders survive is what "
             "makes the next step meaningful."),
            ("Replay each survivor against the object and count the legal ones",
             "For a register: track the current value, and reject at the first read that "
             "disagrees with it. Zero survivors means the history is not linearizable. "
             "More than zero means it is, and the count itself has no further meaning."),
        ],
        "worked": {
            "title": "Three operations, six orders, no explanation",
            "intro": [
                "A register starting at zero. One client writes `1`; two others read it, "
                "one returning `1` and one returning `0`. Every response is a value the "
                "register really held, and the system is nonetheless wrong. The question "
                "is how to demonstrate that rather than assert it.",
            ],
            "lines": [
                "initial value 0",
                "",
                "  A   write 1     [0, 4]",
                "  B   read → 1    [2, 6]",
                "  C   read → 0    [5, 9]",
                "",
                "real-time constraints",
                "  A ends 4, C starts 5     A must precede C",
                "  A [0,4] and B [2,6] overlap      no constraint",
                "  B [2,6] and C [5,9] overlap      no constraint",
                "",
                "the six total orders",
                "  A B C    real time ok     w1 → r1 ✓ → r0 ✗",
                "  A C B    real time ok     w1 → r0 ✗",
                "  B A C    real time ok     r1 ✗  (register still 0)",
                "  B C A    C before A — rejected",
                "  C A B    C before A — rejected",
                "  C B A    C before A — rejected",
                "",
                "  6 orders,  3 survive real time,  0 survive the replay",
                "",
                "verdict: NOT linearizable",
                "",
                "change C's return value from 0 to 1 and re-run",
                "  A B C    w1 → r1 ✓ → r1 ✓    legal",
                "  A C B    w1 → r1 ✓ → r1 ✓    legal",
                "  B A C    r1 ✗",
                "  2 legal orders — linearizable",
            ],
            "after": [
                "The violation is `C`, and it is worth saying exactly why rather than "
                "pointing at it. `C` was issued after `A` had already returned, so "
                "whatever instant `C` took effect at, it was after the write took effect; "
                "and it returned the value from before the write. No amount of reordering "
                "the two overlapping reads changes that, which is what the three surviving "
                "orders demonstrate by all failing.",
                "The second run is the faded half of the example and it is a single "
                "character's difference. Two legal orders exist, so the history is "
                "linearizable, and nothing about the timings changed. The lesson is that "
                "linearizability is decided by the combination of intervals and returned "
                "values, and that neither alone is enough to look at.",
                "For a faded rehearsal, take the four-operation history with two concurrent "
                "writes: `A w1[0,3]`, `B w2[1,5]`, `C r1[4,8]`, `D r2[6,10]`. The supplied "
                "first move is that there are `24` total orders and the forced pairs are "
                "`A` before `C` and `A` before `D`. Work out how many survive real time, "
                "predict whether any are legal, then check both in the lab and explain the "
                "result in one sentence about where `B` had to be placed.",
            ],
        },
        "quiz_title": "Histories, orders and verdicts",
        "quiz": [
            {"q": "Every read in a history returned a value the register genuinely held at some point. Is the history linearizable?",
             "a": ["Yes — a read that returns a real value is a correct read",
                   "Not necessarily: linearizability asks whether one total order explains all the operations at once, and the example on this page has no such order",
                   "Yes, provided no two operations overlap",
                   "Only if the reads happened after the write"],
             "c": 1,
             "why": "This is the misconception the lesson exists for. In the worked "
                    "history, `B` returning `1` and `C` returning `0` are individually "
                    "fine and jointly impossible, because real time forces the write "
                    "before `C`. Checking responses one at a time cannot see that, which "
                    "is why the check is over orders rather than over operations."},
            {"q": "`A` occupies `[0,4]`, `B` occupies `[2,6]` and `C` occupies `[5,9]`. How many of the `6` total orders respect real time?",
             "a": ["`1`", "`2`", "`3`", "`6`"],
             "c": 2,
             "why": "Only one pair is forced: `A` ends at `4` before `C` starts at `5`, so "
                    "`A` must precede `C`. Of the six permutations, three put `A` before "
                    "`C` — `A B C`, `A C B` and `B A C`. The other two pairs overlap and "
                    "constrain nothing, so the count is `3` rather than `1`."},
            {"q": "Why does the lab refuse a seventh operation rather than sampling the orders?",
             "a": ["Because seven-operation histories are always linearizable",
                   "Because the enumeration is factorial — `7! = 5040` against `6! = 720` — and hiding that behind a silent truncation would teach the opposite of why real checkers do not enumerate",
                   "Because the browser cannot hold five thousand permutations",
                   "Because sampling would give the wrong answer only rarely"],
             "c": 1,
             "why": "The refusal is deliberate and the number is printed with it. Five "
                    "thousand permutations is trivial for any machine, so the limit is "
                    "pedagogical rather than computational: the factorial is the reason "
                    "production checkers search with pruning or check weaker properties, "
                    "and a silent truncation would conceal exactly that."},
        ],
        "mistakes": [
            ("Checking operations one at a time",
             "Every response in the violating history is a value the register held, so "
             "per-operation checking passes it. Linearizability is a property of the "
             "history taken together, and the only way to refute it is to show that no "
             "total order explains all of it. That is why the output is a count over "
             "orders rather than a verdict on a response."),
            ("Reading overlapping intervals as permission to do anything",
             "An overlap removes a constraint, it does not add a freedom. The two "
             "overlapping reads in the worked history could be placed either way round and "
             "it made no difference, because the constraint that killed the history came "
             "from the non-overlapping pair. Look for the forced pairs first; they are "
             "where the verdict comes from."),
            ("Expecting enumeration to be how this is checked in practice",
             "`k!` reaches five thousand at seven operations and `2.4 × 10¹⁸` at twenty. "
             "Real checkers search with pruning and backtracking, commit operations as "
             "soon as the object's state permits, or check something weaker and cheaper. "
             "The enumeration here exists because it makes the definition concrete, and "
             "the cap exists to make sure you notice it could not scale."),
        ],
        "standard": ("Finish when “every replica returned a value it held” sounds like an answer to a different question.",
                     "You should be able to write a history as intervals with return "
                     "values, derive the forced pairs, enumerate and filter the total "
                     "orders, replay the survivors against a register, report the count "
                     "with zero as a violation, and say why the procedure does not scale."),
        "note": "Linearizability rules out disagreement by insisting there was only ever "
                "one story. Systems that accept writes in more than one place give that up "
                "on purpose, and then have to decide what to do with two updates that "
                "genuinely conflict. “Conflict Resolution, Counted” closes the course by "
                "counting what each answer throws away.",
    },
    # ---------------------------------------------------------------- 13
    {
        "slug": "conflict-resolution-counted",
        "title": "Conflict Resolution, Counted",
        "module": "Consistency, counted",
        "one_line": "Count the updates each merge rule discards on a trace of concurrent updates.",
        "summary": (
            "Given concurrent updates to one value, last-writer-wins keeps the register of "
            "whichever replica holds the largest timestamp and discards the rest: on a "
            "four-update trace worth `10` it returns `7`, throwing away `2` updates worth "
            "`3`. A counter CRDT keeps one component per replica, merges by elementwise "
            "maximum and sums, returning `10` and discarding none. Accurate clocks change "
            "which update survives, never how many do."
        ),
        "key": [
            "trace   A:3:+2   B:5:+3   C:4:+1   B:9:+4     all four concurrent",
            "true total, every update applied                          10",
            "last-writer-wins: B holds t = 9, so B's register wins       7",
            "                  2 updates discarded, worth 3",
            "counter CRDT: {A = 2, B = 7, C = 1}, summed                10, discarding 0",
            "merge is elementwise max: commutative, associative, idempotent",
        ],
        "key_label": "Two merges on one trace, and what each throws away",
        "concepts_intro": (
            "One rule keeps a replica, the other keeps a component per replica, and the "
            "difference is not a matter of clock quality."
        ),
        "concepts": [
            ("Last-writer-wins keeps one replica's register and drops the rest",
             "The rule picks the update with the largest timestamp and takes the state of "
             "the replica that made it. That replica's register contains its own updates "
             "and nothing else, so every update made anywhere else during the partition is "
             "gone. On the trace here `B` holds `t = 9`, `B`'s register is `3 + 4 = 7`, and "
             "`A`'s `+2` and `C`'s `+1` are discarded — two updates worth three."),
            ("Accurate clocks change which update survives, not how many",
             "Make every timestamp perfectly correct and last-writer-wins still keeps one "
             "replica's register and still discards the others. All that changes is which "
             "replica is chosen. The count of discarded updates is a function of how many "
             "replicas were updated concurrently, and clock quality does not appear in it "
             "anywhere. This is the misconception the lesson exists to break."),
            ("The counter keeps one component per replica and merges by maximum",
             "State a counter as a vector of per-replica totals. A replica increments only "
             "its own component; merging two states takes the elementwise maximum; the "
             "value is the sum. Elementwise maximum is commutative, associative and "
             "idempotent, so every replica converges on the same value whatever order "
             "gossip arrives in, however often, and however many times a message is "
             "redelivered."),
        ],
        "read_title": "Two merges, one trace, and the count each one loses",
        "read_intro": (
            "What last-writer-wins does with concurrent updates, what a counter CRDT does "
            "instead, and the three properties that make the second one safe."
        ),
        "body": [
            ("def", ("Concurrent updates, last-writer-wins, and a counter CRDT",
                     "Updates are <strong>concurrent</strong> when no chain of messages "
                     "orders them — the condition “Vector Clocks and Concurrency” makes "
                     "decidable. <strong>Last-writer-wins</strong> resolves them by "
                     "keeping the state of the replica holding the largest timestamp. A "
                     "<strong>counter CRDT</strong> holds one count per replica, merges "
                     "two states by elementwise maximum and reports the sum.")),
            ("p", "Both rules produce a single answer from conflicting states, which is "
                  "what a merge has to do. The difference is what each one is willing to "
                  "throw away to get there, and that is a number rather than a matter of "
                  "taste."),
            ("math", [
                "four concurrent updates; no replica has seen any other's",
                "",
                "  replica   timestamp   delta    under LWW     CRDT component",
                "     A          3        +2      discarded     A = 2",
                "     B          5        +3      kept          B = 3 + 4 = 7",
                "     C          4        +1      discarded     C = 1",
                "     B          9        +4      kept",
                "",
                "  true total                     2 + 3 + 1 + 4  =  10",
                "  last-writer-wins    B holds the largest timestamp, so B's",
                "                      register wins            =   7",
                "                      2 updates discarded, worth 3",
                "  counter CRDT        {A = 2, B = 7, C = 1}, summed  =  10",
                "                      0 updates discarded",
            ]),
            ("p", "Every one of those four updates was acknowledged to a client. Under "
                  "last-writer-wins two of them stop existing at merge time, with no error "
                  "raised anywhere, and the value a reader sees afterwards is `7` for a "
                  "sequence of increments totalling `10`. That is not a bug in the "
                  "implementation; it is what the rule says to do."),
            ("h3", "The clocks are not the problem"),
            ("p", "The standard response to this is that the timestamps must be made "
                  "accurate. Suppose they are exact to the nanosecond. The rule still "
                  "keeps one replica's register and still discards every update made "
                  "elsewhere; the only thing that changes is which replica gets to be the "
                  "winner. What is being lost is not precision in the ordering, it is the "
                  "fact that there was no ordering to be precise about — the updates were "
                  "concurrent, and last-writer-wins is a rule for picking one arbitrarily."),
            ("p", "The deeper problem is that last-writer-wins treats an increment as a "
                  "state to be overwritten rather than an operation to be applied. Once "
                  "`+2` has become “`A`'s register reads `2`”, there is no way to combine "
                  "it with “`B`'s register reads `7`” except by choosing. The counter "
                  "avoids the choice by never merging the two into one slot in the first "
                  "place."),
            ("math", [
                "the merge is elementwise maximum on the component vectors",
                "",
                "  commutative    A ∨ B = B ∨ A",
                "  associative    (A ∨ B) ∨ C = A ∨ (B ∨ C)",
                "  idempotent     (A ∨ B) ∨ (A ∨ B) = A ∨ B",
                "",
                "so every replica converges on the same value regardless of",
                "  the order gossip arrives in            — commutativity",
                "  how the exchanges are grouped          — associativity",
                "  how often a message is redelivered     — idempotence",
            ]),
            ("example", ("Why each of the three laws is doing work",
                         "Drop commutativity and the value depends on which replica "
                         "gossiped first, so two replicas that exchanged the same "
                         "information in opposite orders disagree for ever. Drop "
                         "associativity and it depends on how the exchanges were grouped, "
                         "which is a topology detail nobody controls. Drop idempotence and "
                         "a redelivered message — the thing every network does under "
                         "retry — double counts. Elementwise maximum has all three, which "
                         "is why the convergence needs no coordination at all: no "
                         "ordering, no exactly-once delivery, no leader.")),
            ("p", "A grow-only counter is the easy case and it should be read as an "
                  "existence proof rather than a general solution. Sets with removals, "
                  "registers holding documents, and ordered sequences all need more "
                  "machinery, and some conflicts are genuinely business decisions that no "
                  "merge rule should be making. What transfers is the question: for this "
                  "data type, what does my merge rule discard, and can I count it?"),
        ],
        "lab": ("replica", {
            "mode": "merge",
            "panel_title": "Edit the concurrent update trace",
            "panel_intro": "Both merges run on the same trace, both counts are exact, and "
                           "the three laws are checked on your updates rather than "
                           "asserted. Move the timestamps around and watch which update "
                           "survives change while the number discarded does not.",
        }),
        "steps_title": "Counting what a merge rule discards",
        "steps_intro": (
            "The trace first, the concurrency second, and only then the merge — because a "
            "rule applied to updates that were not concurrent discards nothing and proves "
            "nothing."
        ),
        "steps": [
            ("Write the trace as replica, timestamp and operation",
             "One line per acknowledged update. If the updates are increments, keep them "
             "as increments rather than as the resulting values — the distinction between "
             "an operation and a state is where the whole difference lives."),
            ("Establish that the updates really are concurrent",
             "Use the vector-clock comparison: if one update's vector dominates another's, "
             "they are ordered and there is no conflict to resolve. A merge rule is only "
             "tested by the pairs that are genuinely incomparable."),
            ("Apply last-writer-wins and count both quantities",
             "Find the largest timestamp, take that replica's state, and count the updates "
             "that are not in it and the value they carried. Report both: “two updates, "
             "worth three” says more than either half alone."),
            ("Apply the type's own merge and check it against the true total",
             "For a counter, elementwise maximum then sum, compared with the sum of all "
             "the increments. If they agree, the rule discards nothing; if they do not, "
             "the difference is what it discards and you now know its size."),
        ],
        "worked": {
            "title": "One trace, two merges",
            "intro": [
                "Three replicas are partitioned from one another and each accepts writes. "
                "Four increments are acknowledged during the partition. The partition "
                "heals, the replicas gossip, and the question is what the counter reads "
                "afterwards — under each of the two rules on offer.",
            ],
            "lines": [
                "the trace, replica:timestamp:delta",
                "  A:3:+2    B:5:+3    C:4:+1    B:9:+4",
                "",
                "no replica has seen any other's update, so all four are concurrent",
                "",
                "true total      2 + 3 + 1 + 4 = 10",
                "",
                "last-writer-wins",
                "  largest timestamp is 9, held by B",
                "  B's register contains B's own updates only:  3 + 4 = 7",
                "  value after merge                            7",
                "  discarded:  A's +2 and C's +1",
                "              2 updates, worth 3",
                "",
                "counter CRDT",
                "  components   A = 2    B = 3 + 4 = 7    C = 1",
                "  merge        elementwise maximum, in any order",
                "  value        2 + 7 + 1 = 10",
                "  discarded    0",
                "",
                "now make every clock exact and re-run last-writer-wins",
                "  the winner may change from B to whoever truly wrote last",
                "  the count discarded does not:  still 2 updates",
            ],
            "after": [
                "Seven against ten, for a rule that raises no error and is the default in a "
                "great deal of software. The thirty per cent is not an edge case either — "
                "it is what happens whenever three replicas take writes and two of them "
                "are not the one holding the largest timestamp.",
                "The last block is the one to argue with somebody about. Improving the "
                "clocks is the reflex fix and it changes the identity of the survivor "
                "without changing the arithmetic: two updates are still discarded, because "
                "two replicas other than the winner accepted writes. Clock accuracy is the "
                "answer to a question about ordering, and these updates were not ordered.",
                "For a faded rehearsal, add a fifth update `A:11:+5` to the trace. The "
                "supplied first move is that the largest timestamp is now `11` and it is "
                "held by `A`, so `A`'s register wins. Work out the new "
                "last-writer-wins value, the number and worth of the updates it discards, "
                "and the CRDT's value — then say, before checking in the lab, whether the "
                "number discarded went up or down and why.",
            ],
        },
        "quiz_title": "What each rule throws away",
        "quiz": [
            {"q": "On the trace `A:3:+2, B:5:+3, C:4:+1, B:9:+4`, what value does last-writer-wins return?",
             "a": ["`10`", "`7`", "`4`", "`6`"],
             "c": 1,
             "why": "`B` holds the largest timestamp, `9`, so `B`'s register wins — and it "
                    "contains `B`'s own increments only, `3 + 4 = 7`. `10` is the true "
                    "total and what the CRDT returns; `4` is the last increment alone, "
                    "which is what you get by keeping the winning <em>update</em> rather "
                    "than the winning replica's state; `6` is not produced by either rule."},
            {"q": "The team proposes fitting every node with a high-accuracy clock so that last-writer-wins becomes safe. What happens to the number of discarded updates?",
             "a": ["It falls to zero, since the true order is now known",
                   "It is unchanged — accurate clocks change which replica wins, not how many others are discarded",
                   "It falls by half, since ties are eliminated",
                   "It rises, because more updates become comparable"],
             "c": 1,
             "why": "The updates were concurrent: there is no true order for a better "
                    "clock to reveal. The rule keeps one replica's state whatever the "
                    "timestamps say, so every other replica that accepted a write during "
                    "the partition still loses it. Clock accuracy answers an ordering "
                    "question, and this is not one."},
            {"q": "The counter CRDT returns `10` on the same trace. Why does it not have to choose a winner?",
             "a": ["Because it keeps one count per replica and merges by elementwise maximum, so no two updates ever compete for the same slot",
                   "Because it uses the timestamps more carefully",
                   "Because it applies the updates in timestamp order",
                   "Because it discards the smallest updates instead of the latest"],
             "c": 0,
             "why": "Each replica's increments live in its own component, so merging is a "
                    "maximum per component rather than a choice between states, and the "
                    "value is the sum of all of them. Timestamps play no part in the merge "
                    "at all — which is exactly why no clock quality is required for it to "
                    "converge, and why redelivering a gossip message cannot double count."},
        ],
        "mistakes": [
            ("Believing better clocks make last-writer-wins safe",
             "They make it arbitrary in a more defensible way and nothing else. The number "
             "of discarded updates is set by how many replicas accepted concurrent writes, "
             "not by the precision of the timestamps. If losing acknowledged updates is "
             "unacceptable, the fix is a merge that does not choose, not a clock that "
             "chooses better."),
            ("Reporting only one of the two counts",
             "“Two updates discarded” and “worth three” answer different questions and both "
             "are needed. A rule that drops many tiny updates and one that drops a single "
             "large one look identical in one number and completely different in the "
             "other, and which of them matters depends on the data rather than on the "
             "merge."),
            ("Generalising the counter to every data type",
             "A grow-only counter merges cleanly because increments commute and the "
             "elementwise maximum is a least upper bound. Removals, ordered lists and "
             "documents are harder, and some conflicts — two people editing the same "
             "sentence, two withdrawals from one balance — are business decisions that no "
             "automatic merge should quietly make. The transferable move is to count what "
             "your rule discards, not to reach for this particular rule."),
        ],
        "standard": ("Finish when “we use last-writer-wins” prompts you to ask how many acknowledged updates that discards.",
                     "You should be able to establish that a set of updates is concurrent, "
                     "compute the last-writer-wins value together with the number and "
                     "worth of what it drops, compute a counter CRDT's value from its "
                     "components, state the three merge laws and what each one buys, and "
                     "say why clock accuracy does not change the count."),
        "note": "That closes the course. Replication costs read capacity you get, write "
                "capacity you do not, a latency that is an order statistic rather than a "
                "sum, and a staleness that is a tail; quorums buy overlap by counting and "
                "nothing more than overlap; and “consistent” turns out to be three "
                "different countable questions with three different answers. The next "
                "course, “Partitioning and Load Balancing”, stops asking whether the copies "
                "agree and starts asking how the data was split between them in the first "
                "place — which is balls into bins, and skewed.",
    },
]
