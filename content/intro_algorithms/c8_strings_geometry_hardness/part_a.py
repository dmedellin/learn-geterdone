"""Strings, Geometry and Hardness, lessons 1-4 -- Chapters 32 and 33.

Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, 3rd ed. (MIT
Press, 2009): Chapter 32, String Matching (pp. 985-1013), and Chapter 33,
Computational Geometry (pp. 1014-1047). Every quotation is copied from the
operator's copy with its printed page in the comment beside the lesson. The
instances are written for these lessons; none of the book's figures, tables,
pseudocode or exercises is reproduced. Every figure the prose attributes to
the lab was read off the running kit with the instance typed in, and every
hand computation was done twice, once by hand and once against the lab.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # CLRS 32.1-32.2, pp. 985-995. Quote: p. 993, 23 words, quotes.py OK.
    # Lesson total: 23 words. Lab: strings/rabin (kit presets); the lesson's
    # own instance is typed into the lab: "a banana and a bandana in a cabana",
    # pattern "ana", base 256, modulus 11 (1 spurious hit, offset 10) and 13
    # (8 spurious hits), read off the kit.
    {
        "slug": "naive-and-rabin-karp-matching",
        "title": "Naive and Rabin-Karp String Matching",
        "module": "Chapter 32 · String Matching",
        "one_line": "Every shift of the pattern is a candidate; the naive matcher checks each one character by character, and Rabin-Karp first compares one number per shift.",
        "summary": (
            "Sections 32.1 and 32.2: the string-matching problem as finding every valid shift, "
            "the naive matcher and its (n − m + 1)·m worst case, and Rabin and Karp's idea of "
            "reading each window as a number modulo a prime, rolling it forward in constant "
            "time, and checking the characters only when the numbers agree. Run the rolling "
            "hash on a text written for the lesson and count the spurious hits at three moduli."
        ),
        "key": [
            "a valid shift s: T[s+1..s+m] = P",
            "shifts to try: n − m + 1",
            "naive worst case: (n − m + 1)·m",
            "equal residues are a hint, not a match",
            "every hit is checked character by character",
            "spurious hits: expected about n/q",
        ],
        "key_label": "Sections 32.1 and 32.2 in six lines",
        "concepts_intro": (
            "Three terms carry the first two sections of the chapter, and the rest of it "
            "keeps all three."
        ),
        "concepts": [
            ("A valid shift",
             "The pattern P of length m occurs with shift s in the text T of length n when the "
             "m characters of T after position s are exactly P. The shifts run from 0 to "
             "n − m, so there are n − m + 1 of them, and the problem is to report every valid "
             "one."),
            ("A rolling hash",
             "Read a window of m characters as an m-digit number in radix d, reduced modulo a "
             "prime q. Dropping the leading digit, shifting and adding the next character "
             "gives the next window's value in a constant number of arithmetic steps, whatever "
             "m is."),
            ("A spurious hit",
             "A shift whose window has the same residue modulo q as the pattern and different "
             "characters. Residues that differ prove a shift invalid; residues that agree "
             "prove nothing, so every agreement is checked character by character."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read the opening of Chapter 32 and sections 32.1 and 32.2 in your own copy first. "
            "The lesson sets out the argument in its own words and then runs the rolling hash "
            "on a text written for it."
        ),
        "body": [
            ("p", "&ldquo;If q is large enough, then we hope that spurious hits occur "
                  "infrequently enough that the cost of the extra checking is low.&rdquo; The "
                  "word to notice is <em>hope</em>. Section 32.2 of Cormen, Leiserson, Rivest "
                  "and Stein gives an algorithm whose worst case is no better than the naive "
                  "one and whose ordinary behaviour is far better, and it is careful to say "
                  "which of those claims is proved. This lesson reads the opening of Chapter 32 "
                  "and sections 32.1 and 32.2, and then counts the hope on a text of its own."),
            ("p", "The chapter states the problem precisely. A text T[1..n] and a pattern "
                  "P[1..m] are arrays of characters from a finite alphabet Σ. The pattern occurs "
                  "with shift s when T[s+1..s+m] equals P[1..m], for s between 0 and n − m, and "
                  "the task is to find every such valid shift. The chapter's opening table sets "
                  "the four algorithms side by side by preprocessing time and matching time, and "
                  "the authors fix the notation the later sections need: the prefix and suffix "
                  "relations on strings, P_k for the first k characters of the pattern, and a "
                  "cost model in which comparing two strings costs time proportional to one more "
                  "than the length of their common prefix."),
            ("p", "Section 32.1 is short because the naive matcher is. It tries every one of the "
                  "n − m + 1 shifts and, at each, compares characters until one differs or all m "
                  "agree. The worst case is `(n − m + 1)·m` comparisons, and the authors show it "
                  "is reached: a text of n copies of one letter and a pattern of m copies of it "
                  "make every shift valid and every comparison necessary. With m near n/2 that is "
                  "`Θ(n²)`. The section's diagnosis is the one the rest of the chapter answers: "
                  "the naive matcher throws away what one shift taught it about the text before "
                  "it tries the next."),
            ("p", "Section 32.2 turns the comparison of strings into the comparison of numbers. "
                  "With decimal digits for characters, a window of m characters is an m-digit "
                  "number, and the pattern's number p can be computed by Horner's rule in "
                  "`Θ(m)` steps. The next window's number follows from the current one by "
                  "removing the high-order digit, multiplying by the radix and adding the new "
                  "low-order digit. That is equation (32.1), and it makes all n − m + 1 window "
                  "values cost `Θ(n − m + 1)` together. If the numbers could be compared in "
                  "constant time, matching would be linear."),
            ("p", "They cannot, because an m-digit number does not fit in a word. So the authors "
                  "reduce everything modulo a prime q chosen so that d·q fits in one word, with "
                  "equation (32.2) as the rolling step and h, the weight of the high-order digit, "
                  "precomputed as d^(m−1) mod q. Now the residues fit, and the price is "
                  "one-sided: different residues prove the window differs from the pattern, but "
                  "equal residues do not prove it equal. Procedure RABIN-KARP-MATCHER therefore "
                  "checks the characters of every window whose residue matches, and its loop "
                  "invariant is simply that the residue in hand is the current window's."),
            ("p", "The analysis comes in two strengths, and the section keeps them apart. The "
                  "worst case is still `Θ((n − m + 1)·m)`, because a text in which every shift "
                  "is valid forces a full check at every shift. The expected case rests on a "
                  "heuristic assumption, which the authors label as one: that reduction modulo q "
                  "behaves like a random map, so that a given window collides with probability "
                  "about 1/q. Then the spurious hits number about n/q, and with few valid shifts "
                  "and q larger than m the expected matching time is `O(n + m)`. You will meet "
                  "the same rolling hash, and the sweep over moduli used below, in the Algorithms "
                  "lesson A Rolling Hash, and a Collision You Can Read."),
            ("p", "Now the count. The lab hashes every window of a text in a chosen base and "
                  "modulus and prints the windows, the hashes equal to the pattern's, the real "
                  "matches beside the matches found by comparing every shift directly, the "
                  "collisions, the characters compared while verifying (the lab charges m for "
                  "each check, as the book's cost model does for a full match), the characters "
                  "spent on collisions, and how many of the 46 primes under 200 produce at least "
                  "one collision on the same text, with the largest of them."),
            ("p", "Its presets are the lab's own. <code>english</code> searches a line of prose "
                  "for a three-letter pattern at modulus 41: 41 windows, 7 equal hashes, 4 real "
                  "matches, 3 collisions and 9 characters wasted; 18 of the 46 primes collide, "
                  "the largest 137. <code>clean</code> is the same line at modulus 1000003, with "
                  "0 collisions. <code>dna</code> finds 3 collisions at modulus 13 that waste 21 "
                  "characters; <code>binary</code> finds 4 at modulus 11, and only 6 of the 46 "
                  "primes collide on it, 17 the largest; <code>abra</code> finds 6 real matches "
                  "and 4 collisions at modulus 13."),
            ("p", "Then type the lesson's own instance: the text `a banana and a bandana in a "
                  "cabana`, the pattern `ana`, base 256. The text has 34 characters, so there "
                  "are 32 windows and the naive bound is `32 · 3 = 96` comparisons. The valid "
                  "shifts are 3, 5, 19 and 31, and two of them overlap inside `banana`. At "
                  "modulus 11 the lab finds 5 equal hashes: the 4 matches and 1 collision, the "
                  "window at shift 10, an n, a d and a space. Verifying costs 15 characters, 3 of "
                  "them wasted. At modulus 17 the collisions vanish; on this text 17 of the 46 "
                  "primes under 200 collide, the largest 181."),
            ("p", "Now set the modulus to 13 and the count jumps to 8 spurious hits, 36 "
                  "characters compared and 24 wasted. Nothing about 13 is small next to m = 3; "
                  "the cause is in the text. That is exactly the gap the book's hedge leaves: "
                  "the n/q estimate assumes the residues of this text's windows look random, and "
                  "on one text, at one modulus, they need not. The count is evidence about this "
                  "text; the expected bound is a statement under an assumption the count cannot "
                  "test."),
            ("h3", "Exercise"),
            ("code", [
                "text     a banana and a bandana in a cabana",
                "pattern  ana",
                "base     256    modulus  13",
            ]),
            ("p", "Without computing any window's hash, explain why the modulus 13 makes so many "
                  "windows collide. Find the remainders of the codes of a (97), n (110) and the "
                  "space (32) modulo 13, and of 256 modulo 13. Then list every spurious hit by "
                  "shift, and say how many characters the matcher spends verifying. Check your "
                  "list against the lab's table."),
            ("p", "The rolling hash still pays for every check. The next lesson, Finite Automata "
                  "and Knuth-Morris-Pratt, reads the two matchers that never look at a text "
                  "character twice."),
        ],
        "lab": ("strings", {
            "mode": "rabin",
            "preset": "english",
            "panel_title": "Hash every window, and read the spurious hits off the table",
            "panel_intro": "Each bar is one window and its height is that window's hash, with "
                           "the pattern's hash drawn across. The table lists every window whose "
                           "hash equals the pattern's, marked as a real match or a collision. "
                           "Type the lesson's text and pattern, choose base 256, and move the "
                           "modulus between 11, 13 and 17.",
        }),
        "steps_title": "Running Rabin-Karp by hand",
        "steps_intro": "Four steps settle one window, and the fifth is on a text of your own.",
        "steps": [
            ("Count the shifts first",
             "There are n − m + 1 of them, from 0 to n − m. The naive bound is that number "
             "times m; write it down before anything else."),
            ("Hash the pattern by Horner's rule",
             "Reduce the radix modulo q once, then take each character in turn: multiply the "
             "running residue by the radix, add the character, reduce. Keep the result: every "
             "window is compared with it."),
            ("Roll one window forward",
             "Subtract the leading character times h = d^(m−1) mod q, multiply by d, add the "
             "next character, reduce. Then hash the new window from scratch and check that the "
             "two agree."),
            ("Check every equal residue",
             "Compare the m characters of each window whose residue equals the pattern's. "
             "Count the matches and the spurious hits separately."),
            ("Do it on your own text",
             "Paste a paragraph of your own into the lab with a short pattern, and find a prime "
             "under 200 at which it collides and a larger one at which it does not. Write down "
             "both, and one sentence on why the larger prime is not guaranteed clean."),
        ],
        "worked": {
            "title": "One spurious hit at modulus 11, checked by hand",
            "intro": [
                "Base 256, modulus 11, pattern ana, in the lesson's text. Character codes: "
                "a is 97, n is 110, d is 100, the space is 32.",
            ],
            "lines": [
                "256 mod 11 = 3,   h = 256² mod 11 = 9",
                "a ≡ 9,  n ≡ 0,  d ≡ 1,  space ≡ 10",
                "pattern ana:  (9·3 + 0)·3 + 9 = 90 ≡ 2",
                "window and, shift 9:  (9·3 + 0)·3 + 1 ≡ 5",
                "roll to shift 10:  (5 − 9·9)·3 + 10",
                "  = (5 − 4)·3 + 10 = 13 ≡ 2",
                "window nd space, from scratch:  1·3 + 10 ≡ 2",
                "residues agree, characters differ",
            ],
            "after": [
                "The rolled value and the value computed from scratch agree, which is the loop "
                "invariant of the matcher holding at shift 10. The residue 2 equals the "
                "pattern's, so the matcher compares the three characters and finds n, d and a "
                "space where it wanted a, n and a: a spurious hit, the only one at this modulus. "
                "The four valid shifts cost 12 character comparisons to confirm and the one "
                "collision 3 more, the 15 the lab prints.",
            ],
        },
        "quiz_title": "Shifts, residues and the analysis",
        "quiz": [
            {"q": "In the lesson's text at base 256 and modulus 13, how many spurious hits does the "
                  "matcher meet when it searches for ana?",
             "a": ["0, because 13 is larger than the pattern's length",
                   "4, one for each valid shift",
                   "8",
                   "12, every window whose residue equals the pattern's"],
             "c": 2,
             "why": "Modulo 13, a (97), n (110) and the space (32) all leave 6, and 256 leaves 9, "
                    "so every window made only of those three characters has the residue "
                    "6·(9 + 3 + 1) = 6·13 ≡ 0, the same as ana. Those windows are at shifts 4, 6, "
                    "7, 8, 12, 20, 24 and 25 besides the four real matches: 8 spurious hits, 12 "
                    "checks and 36 characters compared. Twelve counts the matches as well; q > m "
                    "is the book's condition for a good expected time, not a promise about one "
                    "text."},
            {"q": "Which statement about RABIN-KARP-MATCHER does section 32.2 prove without any "
                  "assumption about the hash?",
             "a": ["Its expected matching time is O(n + m) when q exceeds m",
                   "Its worst-case matching time is Θ((n − m + 1)·m)",
                   "It meets about n/q spurious hits on any text",
                   "A larger prime q always gives fewer spurious hits"],
             "c": 1,
             "why": "The worst case is proved outright: a text in which every shift is valid "
                    "forces a full character check at each of the n − m + 1 shifts. The expected "
                    "time and the n/q estimate both rest on the heuristic that reduction modulo q "
                    "acts like a random map, which the authors name as an assumption. The last "
                    "choice is false on the lesson's own text: 13 gives 8 spurious hits where 11 "
                    "gives 1."},
            {"q": "Why does the matcher check the characters when the residues agree, but not when "
                  "they differ?",
             "a": ["Because checking every window would make it slower than the naive matcher",
                   "Because equal residues modulo q can come from different windows, while "
                   "different residues cannot come from equal ones",
                   "Because the residues are only approximations of the window's value",
                   "Because the rolling update can drift and must be corrected"],
             "c": 1,
             "why": "If two windows are equal their numbers are equal, so their residues are "
                    "equal; different residues therefore prove the window is not the pattern. "
                    "The converse fails: many numbers share a residue. The residues are exact, "
                    "not approximate, and the update does not drift, because it is exact "
                    "arithmetic modulo q, which is why the lab's from-scratch check always "
                    "agrees."},
            {"q": "A text has 1,000 characters and the pattern 10. How many shifts does the naive "
                  "matcher try, and what is its worst-case number of character comparisons?",
             "a": ["1,000 shifts and 10,000 comparisons",
                   "991 shifts and 9,910 comparisons",
                   "990 shifts and 9,900 comparisons",
                   "991 shifts and 1,000 comparisons"],
             "c": 1,
             "why": "The shifts run from 0 to n − m = 990, which is 991 values, and each can cost "
                    "m = 10 comparisons, so the worst case is (n − m + 1)·m = 9,910. Forgetting "
                    "the + 1 gives 990; using n instead of n − m + 1 gives 1,000. A thousand "
                    "comparisons is what the naive matcher often spends on ordinary text, which "
                    "is a count on one input and not its bound."},
        ],
        "mistakes": [
            ("Taking a matching residue for a match",
             "The residue is a fingerprint of the window, and fingerprints collide. Section 32.2 "
             "is explicit that equal residues only make a shift worth checking. On the lesson's "
             "text at modulus 11, the window at shift 10 has residue 2, the pattern's, and holds "
             "n, d and a space. A matcher that reported it would be wrong."),
            ("Reading the expected time as a guarantee",
             "The `O(n + m)` expected matching time depends on a heuristic assumption about the "
             "residues and on there being few valid shifts. The worst case is still that of the "
             "naive matcher. A text of one repeated letter, searched for a run of the same "
             "letter, makes every shift valid and every check full."),
            ("Expecting a larger modulus always to help",
             "The n/q estimate is about the average over moduli. On one text the collisions "
             "depend on the text: the lesson's text collides at 13 and not at 17, at 23 and not "
             "at 19, and at 181, while 47 is clean. A prime that works on one input is not shown "
             "to work on the next."),
        ],
        "standard": ("Finish when you can run Rabin-Karp on a short text by hand.",
                     "For a text, a pattern, a radix and a small prime, compute the pattern's "
                     "residue, roll a window forward and check it from scratch, find the valid "
                     "shifts and the spurious hits, and say which of the section's running-time "
                     "claims rests on an assumption."),
        "note": ("The lab counts collisions on the text you type at the moduli it offers; it "
                 "cannot show the expected n/q, which is an average over an assumption about "
                 "the hash, and it charges m characters for each check where a real "
                 "implementation stops at the first difference. The worst-case bound is "
                 "the book's proof, and no count on one text can stand in for it."),
    },
    # ---------------------------------------------------------------- 02
    # CLRS 32.3-32.4, pp. 995-1013. Quote: p. 989, 26 words, quotes.py OK.
    # Lesson total: 26 words. Lab: strings/kmp, opening on the kit preset
    # aabaaab; the lesson's own pattern abaabab with text abaababaabaababab
    # (pi 0 0 1 1 2 3 2, 2 inner iterations, 19 against 35 comparisons) and
    # the exercise pattern abacabab (pi 0 0 1 0 1 2 3 2), read off the kit.
    {
        "slug": "automata-and-knuth-morris-pratt",
        "title": "Finite Automata and Knuth-Morris-Pratt",
        "module": "Chapter 32 · String Matching",
        "one_line": "A matcher that remembers how much of the pattern it has seen never re-reads the text: an automaton stores every move in a table, and KMP computes each move from the prefix function.",
        "summary": (
            "Sections 32.3 and 32.4: the string-matching automaton, whose state counts how "
            "much of the pattern, from its start, ends the text read so far, and the "
            "Knuth-Morris-Pratt matcher, which replaces the automaton's table with the prefix "
            "function π. Build π for a pattern written for the lesson, count the inner-loop "
            "iterations against the aggregate bound, and see where the automaton and π agree."
        ),
        "key": [
            "state q: longest prefix of P ending here",
            "δ(q, a) = σ(P_q·a)",
            "automaton: Θ(n) matching, a table to build",
            "π[q]: longest proper border of P_q",
            "on a mismatch, fall back from q to π[q]",
            "k rises at most m − 1 times in all",
            "so the while loop runs at most m − 1 times",
        ],
        "key_label": "Sections 32.3 and 32.4 in seven lines",
        "concepts_intro": (
            "Three definitions do the work in these two sections. The second and third are the "
            "same idea at two costs."
        ),
        "concepts": [
            ("The suffix function σ",
             "For a string x, σ(x) measures the longest pattern prefix that is also a suffix "
             "of x. The string-matching automaton's state after reading part of the text "
             "is σ of what it has read, and it accepts exactly when that state is m."),
            ("The transition function δ",
             "The automaton's move from state q on character a is δ(q, a) = σ(P_q·a): append a "
             "to the q characters already matched and ask how much of the pattern is still in "
             "play. The table has one entry per state and character, (m + 1)·|Σ| in all."),
            ("The prefix function π",
             "π[q] measures the longest pattern prefix that is also a proper suffix of P_q, "
             "the first q characters. Such a string is called a border. π has only m "
             "entries and does not depend on the next character, which is the saving KMP "
             "makes over δ."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read sections 32.3 and 32.4 in your own copy first. The lesson sets out the "
            "argument in its own words and then builds the prefix function for a pattern "
            "written for it."
        ),
        "body": [
            ("p", "&ldquo;The naive string-matcher is inefficient because it entirely ignores "
                  "information gained about the text for one value of s when it considers "
                  "other values of s.&rdquo; That sentence closes section 32.1, and sections "
                  "32.3 and 32.4 are two answers to it. Both keep one number while they scan, "
                  "how much of the pattern the text has just matched, and both use it to decide "
                  "the next move without looking back. This lesson reads both sections and "
                  "then builds the second answer's table by hand and in the lab."),
            ("p", "Section 32.3 begins with finite automata in general: a set of states, a start "
                  "state, accepting states, an alphabet and a transition function. The "
                  "string-matching automaton for P has states 0 to m, starts at 0 and accepts "
                  "at m. Its transition function is defined through the suffix function σ: from "
                  "state q on character a it moves to σ(P_q·a), the longest prefix of P that "
                  "ends the string the automaton has effectively seen. Scanning the text is then "
                  "one table lookup per character, and the matching time is `Θ(n)` with no "
                  "character read twice."),
            ("p", "The correctness argument is an invariant about σ. The authors prove that the "
                  "state after reading the first i characters of the text is σ(T_i), using two "
                  "lemmas: σ(xa) is at most σ(x) + 1, and if q = σ(x) then σ(xa) = σ(P_q·a). "
                  "The second is what lets the automaton forget everything about the text except "
                  "q. The price is the table. Their straightforward construction, "
                  "COMPUTE-TRANSITION-FUNCTION, takes `O(m³·|Σ|)` time; the section notes that "
                  "it can be brought to `O(m·|Σ|)`, and that is still a factor of |Σ| per "
                  "state."),
            ("p", "Section 32.4 removes that factor. Suppose q characters of the pattern have "
                  "matched at some shift and the next one fails. The q text characters just read "
                  "are known: they are P_q. The next shift worth trying is the one that lines up "
                  "the longest proper prefix of P_q that is also a suffix of P_q, and its length "
                  "is π[q]. Because π depends only on the pattern, it can be computed once, in "
                  "an array of m entries, before the text is read. KMP-MATCHER scans the text "
                  "with a counter q, falling back from q to π[q] on each mismatch until the next "
                  "character fits or q reaches 0."),
            ("p", "The running time is an aggregate argument (section 17.1), and it is the "
                  "chapter's most instructive count. In COMPUTE-PREFIX-FUNCTION the counter k "
                  "starts at 0, rises by at most 1 per pattern character, and every iteration of "
                  "the inner while loop lowers it by at least 1 without taking it below 0. So the "
                  "total number of decreases cannot exceed the total number of increases, which "
                  "is at most m − 1. One step can fall back many times; all of them together "
                  "cannot. The same argument with the text in place of the pattern gives "
                  "KMP-MATCHER its `Θ(n)` matching time."),
            ("p", "Correctness takes the rest of the section. The prefix-function iteration "
                  "lemma says that following π from q, to π[q], to π[π[q]] and so on down to 0, "
                  "lists every k for which P_k is a proper suffix of P_q, and nothing else. "
                  "From it the authors show that the procedure computes π correctly and that the "
                  "matcher simulates the automaton. The Algorithms lesson Borders, and the "
                  "Failure Function Built runs the same construction under the name the failure "
                  "function."),
            ("p", "Now the lab. Type a pattern and a text, and it builds π one prefix at a time, "
                  "beside the longest border of each prefix found by trying every length, so "
                  "the linear construction is checked against the definition. Its tiles are m, "
                  "the inner-loop iterations, a bound of 2m (looser than the book's m − 1, and "
                  "printed so the two can be compared), the longest border of the whole pattern, "
                  "KMP's comparisons on the text beside the naive matcher's, the bound 2n, and "
                  "the matches beside the matches by definition."),
            ("p", "The presets are the lab's. <code>aabaaab</code> takes 2 inner iterations "
                  "against 14, ends on the border aab of length 3, and finds 3 matches with 19 "
                  "comparisons where naive takes 42. <code>aaaa</code> has the longest possible "
                  "border, 4, and no inner iterations at all; KMP takes 20 comparisons on its "
                  "text of 20 a's against naive's 80. <code>abcabcabd</code> builds a border of "
                  "5 and then loses it at the final d, ending at 0 after 2 iterations. "
                  "<code>abcdefg</code> has no border, and KMP's 23 comparisons beat naive's 34 "
                  "only narrowly. <code>ababaca</code> is the pattern the chapter's own figures "
                  "use, so you can follow those figures with it."),
            ("p", "Then type the lesson's pattern `abaabab` and the text `abaababaabaababab`. "
                  "The table reads π = 0, 0, 1, 1, 2, 3, 2, agreeing with the definition on all "
                  "seven prefixes, and the inner loop ran 2 times against the book's bound of "
                  "m − 1 = 6. The fallback chain from the whole pattern is 7, 2, 0. On the "
                  "17-character text KMP made 19 comparisons and found the 2 valid shifts, 0 "
                  "and 8; the naive matcher made 35. The bound 2n is 34, and 19 is under it on "
                  "this text, as the proof says it must be on every text."),
            ("h3", "Exercise"),
            ("code", [
                "pattern  abacabab",
            ]),
            ("p", "Compute π[1] to π[8] by the procedure's rule, and count the iterations of the "
                  "inner loop as you go, saying at which q each one happens. Give the longest "
                  "border of the whole pattern and the fallback chain from 8. Then type the "
                  "pattern into the lab, with any text, and compare."),
            ("p", "Strings are sequences; the next chapter's objects are points in the plane. "
                  "The next lesson, Line-Segment Properties and Intersection, shows how far one "
                  "cross product goes."),
        ],
        "lab": ("strings", {
            "mode": "kmp",
            "preset": "aabaaab",
            "panel_title": "Build the prefix function one prefix at a time",
            "panel_intro": "Each bar is one prefix of the pattern and its height is the length of "
                           "that prefix's longest proper border. The table sets the linear-time "
                           "construction beside the border found by trying every length. Type "
                           "the lesson's pattern abaabab and its text, then the exercise's "
                           "pattern.",
        }),
        "steps_title": "Computing π by hand",
        "steps_intro": "Four steps compute the table; the fifth checks the aggregate bound on a pattern of your own.",
        "steps": [
            ("Start with π[1] = 0 and k = 0",
             "A single character has no proper border. The counter k always holds the length "
             "of the border being extended."),
            ("Try to extend the border",
             "For q from 2 to m, compare P[k + 1] with P[q]. If they are equal, the border "
             "grows: k becomes k + 1 and π[q] = k."),
            ("Fall back on a mismatch",
             "If they differ and k > 0, set k to π[k] and compare again; each such step is one "
             "inner-loop iteration. Stop when the characters match or k is 0, and then set "
             "π[q] as before."),
            ("Check the count against m − 1",
             "Add up the inner-loop iterations. They can never exceed the number of times k "
             "rose, and k rises at most once per character after the first."),
            ("Find a pattern that makes the loop work",
             "Type a pattern of your own of about ten characters into the lab and change it "
             "until the inner-loop count is at least 4. Write down the pattern, the count and "
             "the bound m − 1, and say at which prefixes k fell."),
        ],
        "worked": {
            "title": "The prefix function of abaabab, step by step",
            "intro": [
                "Pattern abaabab, m = 7. Each line is one value of q, with the comparison made "
                "and the inner-loop iterations it cost.",
            ],
            "lines": [
                "q = 1   a          π = 0",
                "q = 2   b vs a, no   π = 0",
                "q = 3   a vs a, yes  k = 1, π = 1",
                "q = 4   a vs b, no: k = π[1] = 0",
                "        a vs a, yes  k = 1, π = 1   (1 fall)",
                "q = 5   b vs b, yes  k = 2, π = 2",
                "q = 6   a vs a, yes  k = 3, π = 3",
                "q = 7   b vs a, no: k = π[3] = 1",
                "        b vs b, yes  k = 2, π = 2   (1 fall)",
            ],
            "after": [
                "Two falls in all, against an increase of k on five occasions and the book's "
                "bound of m − 1 = 6. The table also says what an automaton for this pattern "
                "would do. In state 6, reading a, the automaton goes to δ(6, a) = σ(abaabaa) = "
                "4. KMP reaches the same state by falling from 6 to π[6] = 3 and then matching "
                "the a: it computes the table entry when it needs it instead of storing it.",
            ],
        },
        "quiz_title": "The prefix function and its bound",
        "quiz": [
            {"q": "For the exercise's pattern abacabab, what are π[4] and π[8], and how many "
                  "inner-loop iterations does COMPUTE-PREFIX-FUNCTION make?",
             "a": ["π[4] = 1, π[8] = 3, and 1 iteration",
                   "π[4] = 0, π[8] = 2, and 2 iterations",
                   "π[4] = 0, π[8] = 3, and 2 iterations",
                   "π[4] = 0, π[8] = 2, and 7 iterations"],
             "c": 1,
             "why": "The full table is 0, 0, 1, 0, 1, 2, 3, 2. At q = 4, k = 1 and P[2] = b differs "
                    "from c, so k falls to π[1] = 0 (one iteration) and a differs from c, so "
                    "π[4] = 0. At q = 8, k = 3 and P[4] = c differs from b, so k falls to "
                    "π[3] = 1 (the second iteration), and P[2] = b matches: π[8] = 2. Three would "
                    "be the border before the last character; seven is m − 1, the bound and not "
                    "the count."},
            {"q": "Why does the inner while loop of COMPUTE-PREFIX-FUNCTION run at most m − 1 "
                  "times in total, even though one value of q can make it run several times?",
             "a": ["Because π[q] is always less than q, so each fall shortens the pattern",
                   "Because k rises by at most 1 per value of q, every iteration lowers k, and "
                   "k never goes below 0",
                   "Because most patterns have short borders",
                   "Because the loop stops as soon as a mismatch is found"],
             "c": 1,
             "why": "It is an aggregate count: the total fall of k is bounded by its total rise, "
                    "which is at most m − 1. π[q] < q is true and is what makes each iteration "
                    "lower k, but on its own it bounds the iterations at one q, not their total. "
                    "Short borders are typical and prove nothing about every pattern."},
            {"q": "The string-matching automaton and KMP-MATCHER both run in Θ(n) on the text. "
                  "What does KMP save?",
             "a": ["Comparisons on the text: it makes fewer than the automaton's n lookups",
                   "The preprocessing: π has m entries computed in Θ(m), where δ has "
                   "(m + 1)·|Σ| entries",
                   "Correctness on patterns with repeated characters",
                   "Nothing asymptotic; it is the same algorithm"],
             "c": 1,
             "why": "The automaton makes exactly one transition per text character, and KMP may "
                    "make more than one comparison per character (each fall is another), so KMP "
                    "does not save work on the text. What it saves is the table: π does not "
                    "depend on the next character. Both are correct on every pattern."},
        ],
        "mistakes": [
            ("Thinking one mismatch costs constant time in KMP",
             "A single mismatch can make the matcher fall back several times. The linear bound "
             "is not a bound on each step; it is a bound on all of them together, from the fact "
             "that q cannot fall further in total than it has risen. On the lesson's pattern two "
             "falls happen at two different prefixes, and the pattern aaaab against the text "
             "aaaac puts four at the c: from 4 to 3, 2, 1 and 0."),
            ("Confusing π[q] with a shift",
             "π[q] is a length: the longest proper border of the first q characters. The shift "
             "KMP moves the pattern by is q − π[q]. On the lesson's pattern, after 6 characters "
             "match and the 7th fails, π[6] = 3, so the pattern slides by 3 and the first 3 "
             "characters are already known to match."),
            ("Treating the automaton as always the better choice",
             "Its matching is a single lookup per character, but its table has (m + 1)·|Σ| "
             "entries. For a long pattern over a large alphabet that is the dominant cost, and "
             "KMP pays only `Θ(m)` for π. Section 32.4 presents KMP as the way around exactly "
             "this."),
        ],
        "standard": ("Finish when you can compute π and justify its linear bound.",
                     "For a pattern of up to ten characters, compute π by the procedure's rule, "
                     "count the inner-loop iterations and say where they happen, give the "
                     "fallback chain from m, and explain in two sentences why the total "
                     "iterations never exceed m − 1."),
        "note": ("The lab builds π for the pattern you type and checks it against the "
                 "definition; it does not build the automaton's table (the Algorithms lesson "
                 "The Matcher as a Machine does). Its bound of 2m is looser than the book's "
                 "m − 1. A small count on one pattern is the common case and not the bound; "
                 "the aggregate argument is what covers every pattern."),
    },
    # ---------------------------------------------------------------- 03
    # CLRS 33.1-33.2, pp. 1014-1029. Quote: p. 1015, 21 words, quotes.py OK.
    # Lesson total: 21 words. Lab: geometry/segments, kit presets; the
    # lesson's own segments (1, 1)-(7, 5) and (2, 6)-(6, 0) (proper crossing,
    # orientations -26 26 26 -26 in the lab's convention), (4, 3)-(4, 8)
    # (touching), and the exercise (0, 0)-(6, 0) with (3, 1)-(11, -1),
    # read off the kit.
    {
        "slug": "line-segment-properties",
        "title": "Line-Segment Properties and Intersection",
        "module": "Chapter 33 · Computational Geometry",
        "one_line": "One cross product says which way three points turn; four of them, and a check for the boundary case, say whether two segments meet.",
        "summary": (
            "Sections 33.1 and 33.2: the cross product as a signed area, the turn test, "
            "SEGMENTS-INTERSECT with its straddle test and its boundary case, and the sweep "
            "that decides whether any two of n segments intersect in O(n lg n) time. Compute "
            "the four orientations for segments written for the lesson, and see the lab use the "
            "opposite sign convention to the book's."
        ),
        "key": [
            "p1 × p2 = x1·y2 − x2·y1",
            "the sign says the turn, zero: colinear",
            "straddle: endpoints on opposite sides",
            "meet: each straddles, or an end on the other",
            "no division, no angles",
            "sweep: events left to right, neighbours only",
        ],
        "key_label": "Sections 33.1 and 33.2 in six lines",
        "concepts_intro": (
            "Three ideas carry these sections. The first answers every question in 33.1, and "
            "the third is a technique the rest of the chapter reuses."
        ),
        "concepts": [
            ("The cross product",
             "For vectors p1 = (x1, y1) and p2 = (x2, y2), p1 × p2 = x1·y2 − x2·y1, the signed "
             "area of the parallelogram they span. Its sign says whether p1 is clockwise or "
             "counterclockwise from p2 about the origin; zero means the two are colinear."),
            ("Straddling",
             "A segment straddles a line when its two endpoints lie strictly on opposite sides "
             "of it. Two segments meet exactly when each straddles the line through the other, "
             "or when an endpoint of one lies on the other, the boundary case."),
            ("A sweep",
             "An imaginary vertical line moves across the plane from left to right, stopping "
             "only at event points such as segment endpoints. The algorithm keeps, in a "
             "balanced search tree, the order of the segments the line currently cuts, and "
             "tests only segments that become neighbours in that order."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read the opening of Chapter 33 and sections 33.1 and 33.2 in your own copy first. "
            "The lesson sets out the argument in its own words and then computes the four "
            "orientations for segments written for it."
        ),
        "body": [
            ("p", "&ldquo;We need neither division nor trigonometric functions, both of which "
                  "can be computationally expensive and prone to problems with round-off "
                  "error.&rdquo; That is the promise section 33.1 makes, and it keeps it: every "
                  "question the section asks is answered with additions, subtractions, "
                  "multiplications and comparisons. This lesson reads the opening of "
                  "Chapter 33 and sections 33.1 and 33.2, and then does the arithmetic on "
                  "segments of its own."),
            ("p", "The chapter opens by saying what computational geometry is, with its inputs "
                  "given as sets of points with real coordinates, and works in the plane "
                  "throughout. Section 33.1 asks three questions: given two directed segments "
                  "from a common point, is one clockwise from the other; given two consecutive "
                  "segments, do they turn left or right where they join; and do two segments "
                  "intersect. Each takes `O(1)` time. The authors contrast their method with the "
                  "obvious one, solving for the intersection of the two lines, which divides and "
                  "is fragile when the segments are nearly parallel."),
            ("p", "All three answers come from the cross product, which the section defines as "
                  "the determinant x1·y2 − x2·y1 and reads as the signed area of a "
                  "parallelogram. Positive means p1 is clockwise from p2 about the origin; "
                  "negative, counterclockwise; zero, colinear. To ask about two segments from a "
                  "common point p0, translate so that p0 is the origin and take the cross "
                  "product of the differences. To ask which way the path p0, p1, p2 turns at p1, "
                  "take (p2 − p0) × (p1 − p0): negative is a left turn, positive a right "
                  "turn, zero means the three points are colinear."),
            ("p", "The intersection test combines four of these. SEGMENTS-INTERSECT computes, "
                  "with a helper called DIRECTION, the orientation of each endpoint of one "
                  "segment relative to the other segment. If the first pair of values have "
                  "opposite signs and so do the second pair, each segment straddles the line "
                  "through the other and they cross. If some value is zero, that endpoint is "
                  "colinear with the other segment, and ON-SEGMENT finishes the case by checking "
                  "whether the point lies within the segment's bounding box. Otherwise they do "
                  "not meet."),
            ("p", "Section 33.2 asks a larger question: do any two of n segments intersect? "
                  "Testing every pair costs `Θ(n²)`. The sweep costs `O(n lg n)`. It assumes no "
                  "segment is vertical and no three meet at one point, sorts the 2n endpoints "
                  "from left to right, and keeps the segments the sweep line currently cuts in a "
                  "total preorder by height, stored in a red-black tree. At a left endpoint it "
                  "inserts the segment and tests it against the segments just above and below; "
                  "at a right endpoint it tests those two neighbours against each other and "
                  "deletes the segment. The correctness argument is that the leftmost "
                  "intersection, if there is one, is between two segments that become "
                  "neighbours at some event before the sweep passes it."),
            ("p", "That procedure, ANY-SEGMENTS-INTERSECT, answers yes or no. It does not find "
                  "every intersection, and the section says so; a report of all k crossings "
                  "needs more work. The Algorithms lesson Do Two Segments Meet covers the "
                  "pairwise test with the same lab used here, and The Sweep Line and the Work It "
                  "Does Not Save runs a sweep."),
            ("p", "Now the lab. Type four points, p1 and p2 for one segment and q1 and q2 for "
                  "the other, and it prints the four orientations, whether the segments cross "
                  "properly (in their interiors), whether they touch, whether their bounding "
                  "boxes overlap, the verdict from the four signs, and a second verdict from "
                  "solving the two parametric equations exactly, with whether the two routes "
                  "agree. One thing to know before you read its table: the lab's orientation "
                  "orient(a, b, c) is (b − a) × (c − a), positive for a left turn, which is the "
                  "negative of the book's DIRECTION(a, b, c). The verdicts do not care; the "
                  "signs are reversed."),
            ("p", "The lab's presets cover the cases the boundary rule exists for. "
                  "<code>proper</code> is an ordinary crossing: proper yes, touching no, they "
                  "meet. <code>touch</code> has one segment end on the other: proper no, "
                  "touching yes. <code>overlap</code> is two colinear segments sharing a "
                  "stretch, <code>shared</code> two segments with only an endpoint in common, "
                  "and <code>point</code> a segment that is a single point lying on the other; "
                  "all three touch and meet. <code>apart</code> is colinear with a gap and "
                  "<code>parallel</code> never meets; in both the boxes do not overlap and the "
                  "verdict is that they miss. The two routes agree on every preset."),
            ("p", "Then type the lesson's segments: p1 = (1, 1), p2 = (7, 5), q1 = (2, 6), "
                  "q2 = (6, 0). The lab prints orientations −26, 26, 26 and −26: each pair has "
                  "opposite signs, so the crossing is proper. Now move q1 to (4, 3) and q2 to "
                  "(4, 8). The third orientation becomes 0, because (4, 3) lies on the line "
                  "through p1 and p2, halfway along. The sign test alone decides nothing; the "
                  "boundary case finds the point inside the segment, and the lab reports "
                  "touching yes, proper no, they meet."),
            ("h3", "Exercise"),
            ("code", [
                "p1 = (0, 0)    p2 = (6, 0)",
                "p3 = (3, 1)    p4 = (11, −1)",
            ]),
            ("p", "Compute the book's four values d1 to d4 for SEGMENTS-INTERSECT on these "
                  "segments by hand, say which segment straddles which line, and decide whether "
                  "they meet. Then type the points into the lab and check that its "
                  "orientations are your values with the signs reversed."),
            ("p", "Orientation is also the whole of the next lesson's machinery. Convex Hull "
                  "and the Closest Pair uses the turn test to decide which points to keep."),
        ],
        "lab": ("geometry", {
            "mode": "segments",
            "preset": "proper",
            "panel_title": "Four orientations, and the boundary case when one is zero",
            "panel_intro": "Type p1, p2 for one segment and q1, q2 for the other. The table "
                           "prints each orientation the test uses, in the lab's convention: "
                           "positive is a left turn, the opposite sign to the book's DIRECTION. "
                           "A second route solves the two segments' equations exactly and must "
                           "agree.",
        }),
        "steps_title": "Deciding whether two segments meet",
        "steps_intro": "Four steps follow SEGMENTS-INTERSECT; the fifth is a pair of your own.",
        "steps": [
            ("Compute the two orientations against the second segment",
             "With the book's DIRECTION, d1 = (p1 − p3) × (p4 − p3) and d2 = (p2 − p3) × "
             "(p4 − p3). Opposite signs mean p1p2 straddles the line through p3p4."),
            ("Compute the two against the first segment",
             "d3 = (p3 − p1) × (p2 − p1) and d4 = (p4 − p1) × (p2 − p1). Opposite signs mean "
             "p3p4 straddles the line through p1p2."),
            ("Decide the general case",
             "If both pairs have opposite signs, the segments cross. If neither pair has a zero "
             "and either pair has equal signs, they do not."),
            ("Finish any zero with the bounding box",
             "For each zero, the endpoint is colinear with the other segment: it lies on that "
             "segment exactly when its coordinates fall between the segment's endpoints in both "
             "x and y."),
            ("Build a case of your own",
             "Choose two segments that share only an endpoint, compute the four values, and say "
             "which of them are zero. Type the points into the lab and check that it reports "
             "touching yes and proper no."),
        ],
        "worked": {
            "title": "The four directions for (1, 1)-(7, 5) and (2, 6)-(6, 0)",
            "intro": [
                "p1 = (1, 1), p2 = (7, 5), p3 = (2, 6), p4 = (6, 0), with the book's "
                "DIRECTION(a, b, c) = (c − a) × (b − a).",
            ],
            "lines": [
                "p4 − p3 = (4, −6),   p2 − p1 = (6, 4)",
                "d1:  (−1, −5) × (4, −6) = 6 + 20 = 26",
                "d2:  (5, −1) × (4, −6) = −30 + 4 = −26",
                "d3:  (1, 5) × (6, 4) = 4 − 30 = −26",
                "d4:  (5, −1) × (6, 4) = 20 + 6 = 26",
                "d1, d2 opposite; d3, d4 opposite",
                "each straddles the other's line: they cross",
            ],
            "after": [
                "The lab's table shows −26, 26, 26, −26 for the same four orientations, because "
                "its orient(a, b, c) is (b − a) × (c − a), the book's value with the sign "
                "reversed. Every comparison the test makes is between two signs, so reversing "
                "all four changes no verdict. No division appeared anywhere, which is the "
                "section's point.",
            ],
        },
        "quiz_title": "Cross products and the intersection test",
        "quiz": [
            {"q": "For the exercise's segments (0, 0)-(6, 0) and (3, 1)-(11, −1), what are the "
                  "book's values d1 to d4, and do the segments meet?",
             "a": ["14, 2, −6, 6; they do not meet",
                   "14, 2, −6, 6; they meet, because d3 and d4 have opposite signs",
                   "−14, −2, 6, −6; they meet",
                   "14, −2, −6, 6; they meet"],
             "c": 0,
             "why": "d1 = (−3, −1) × (8, −2) = 6 + 8 = 14 and d2 = (3, −1) × (8, −2) = −6 + 8 = 2 "
                    "have the same sign, so p1p2 does not straddle the line through p3p4, and no "
                    "value is zero. d3 = (3, 1) × (6, 0) = −6 and d4 = (11, −1) × (6, 0) = 6 have "
                    "opposite signs, so p3p4 does straddle the x-axis, at x = 7, beyond p2. One "
                    "straddle is not enough. The lab prints −14, −2, 6, −6, the same values with "
                    "its opposite convention."},
            {"q": "What does a cross product of 0 tell SEGMENTS-INTERSECT about an endpoint?",
             "a": ["That the endpoint lies on the other segment, so the segments meet",
                   "That the endpoint is colinear with the other segment, so ON-SEGMENT must "
                   "decide whether it lies between that segment's endpoints",
                   "That the two segments are parallel and cannot meet",
                   "That the computation has lost precision"],
             "c": 1,
             "why": "Zero means the three points are on one line, nothing more: the endpoint may "
                    "lie on the segment, as (4, 3) does on (1, 1)-(7, 5), or beyond it, as in the "
                    "lab's apart preset. Parallel segments give nonzero values unless they are "
                    "colinear. With integer coordinates the product is exact, so zero is a fact "
                    "about the points, not a rounding effect."},
            {"q": "What does ANY-SEGMENTS-INTERSECT report, and in what time?",
             "a": ["Every intersecting pair, in O(n lg n) time",
                   "Whether any two segments intersect, in O(n lg n) time",
                   "Whether any two segments intersect, in Θ(n²) time",
                   "The leftmost intersection point, in O(n) time after sorting"],
             "c": 1,
             "why": "The sweep answers yes or no; it may stop at the first intersection it finds. "
                    "Testing every pair is the Θ(n²) method it improves on. Its correctness proof "
                    "reasons about the leftmost intersection, but the procedure does not compute "
                    "that point, and reporting every pair needs more than this sweep."},
        ],
        "mistakes": [
            ("Testing only for straddling",
             "If the four values are all nonzero, the straddle test decides. When one is zero "
             "it decides nothing: on the lesson's second pair, (4, 3) lies on the line through "
             "(1, 1) and (7, 5) and the segments touch, while the lab's apart preset has every "
             "value zero and the segments miss. The boundary case is half of the procedure, not "
             "a footnote."),
            ("Mixing the two sign conventions",
             "The book's DIRECTION(a, b, c) is (c − a) × (b − a) and the lab's orient(a, b, c) "
             "is (b − a) × (c − a); one is the negative of the other. A rule such as "
             "&ldquo;positive is a left turn&rdquo; is true in one convention and false in the "
             "other. Fix one convention before reading any sign, and note that the intersection "
             "verdict is unchanged because it compares signs in pairs."),
            ("Solving for the intersection point",
             "Writing each segment as y = m·x + b and solving needs division and fails for "
             "vertical segments. Section 33.1 avoids it on purpose: the four cross products of "
             "integer coordinates are exact integers. The lab's second route does solve the "
             "equations, exactly and without dividing, and agrees."),
        ],
        "standard": ("Finish when you can decide by hand whether two segments meet.",
                     "For two segments with small integer endpoints, compute d1 to d4, say which "
                     "segment straddles which line, finish any zero with the bounding-box check, "
                     "and state the verdict; then say what the sweep of section 33.2 adds."),
        "note": ("The lab tests one pair of segments with exact integer arithmetic; it does not "
                 "run ANY-SEGMENTS-INTERSECT, and agreeing on the cases you type is not the "
                 "section's proof that the four-sign test is right on every pair. Its sign "
                 "convention is the opposite of the book's, which changes the signs it prints "
                 "and none of its verdicts."),
    },
    # ---------------------------------------------------------------- 04
    # CLRS 33.3-33.4, pp. 1029-1047. Quote: p. 1029, 18 words, quotes.py OK.
    # Lesson total: 18 words. Lab: geometry/hull, opening on the kit preset
    # general; the kit runs Andrew's monotone chain, not Graham's polar sort
    # (see the report). The lesson's own eight points and the exercise's six
    # were run in the kit; the Graham's scan traces are by hand.
    {
        "slug": "convex-hull-and-closest-pair",
        "title": "Convex Hull and the Closest Pair",
        "module": "Chapter 33 · Computational Geometry",
        "one_line": "Graham's scan keeps a stack of candidate corners and pops any point that makes a non-left turn; the closest pair is found by dividing the points and checking a narrow strip.",
        "summary": (
            "Sections 33.3 and 33.4: the convex hull, Graham's scan with its O(n lg n) "
            "bound and Jarvis's march with O(n·h), and the divide-and-conquer algorithm for the closest pair of "
            "points with its strip of width 2δ. Run Graham's scan by hand on eight points "
            "written for the lesson, then compare the lab's stack counts and n·h."
        ),
        "key": [
            "hull: smallest convex polygon around all",
            "Graham: sort by angle, pop unless a left turn",
            "each point pushed once, popped at most once",
            "Graham: O(n lg n), sort dominates",
            "Jarvis: O(n·h), h hull vertices",
            "closest pair: T(n) = 2T(n/2) + O(n)",
            "in the strip, check the next 7 points",
        ],
        "key_label": "Sections 33.3 and 33.4 in seven lines",
        "concepts_intro": (
            "Three ideas organise these two sections, and the turn test of the previous lesson "
            "sits inside all three."
        ),
        "concepts": [
            ("The convex hull",
             "CH(Q) is the smallest convex polygon such that every point of Q lies on its "
             "boundary or inside it. Its vertices are points of Q. The section assumes the "
             "points are distinct and that at least three of them are not colinear."),
            ("Rotational sweep",
             "Both hull algorithms in the section process points in order of the polar angle "
             "they make with a reference point. Graham's scan sorts by that angle once; "
             "Jarvis's march finds the next smallest angle each time it adds a vertex."),
            ("The strip",
             "After the closest pair on each side of a dividing line is found at distance δ, "
             "any closer pair must straddle the line within the band of width 2δ around it. "
             "Sorted by y, each point in that band needs comparing only with the next seven."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read sections 33.3 and 33.4 in your own copy first. The lesson sets out the "
            "argument in its own words and then runs Graham's scan by hand on eight points "
            "written for it."
        ),
        "body": [
            ("p", "&ldquo;Intuitively, we can think of each point in Q as being a nail sticking "
                  "out from a board.&rdquo; The rubber band stretched around the nails is the "
                  "convex hull, and section 33.3 gives two ways to find it with the cross "
                  "product of the previous lesson as the only geometric operation. Section 33.4 "
                  "then applies divide and conquer to the closest pair of points. This lesson "
                  "reads both sections and runs Graham's scan by hand on points of its own."),
            ("p", "Section 33.3 defines CH(Q) and states the two algorithms' bounds before "
                  "either is given: Graham's scan runs in `O(n lg n)`, Jarvis's march in "
                  "`O(n·h)`, where h is the number of hull vertices. It surveys other methods "
                  "too, the incremental method, divide and conquer and prune and search, the "
                  "last running in `O(n lg h)`, and it notes that the farthest pair of points "
                  "lies on the hull, so a hull is often the first step of another algorithm."),
            ("p", "GRAHAM-SCAN takes the point with the lowest y-coordinate, the leftmost in a "
                  "tie, as p0, and sorts the others by polar angle about it, keeping only the "
                  "farthest of any points at the same angle. It pushes p0 and the first two "
                  "points onto a stack. Then, for each remaining point in angle order, it pops "
                  "the stack while the top two entries and the new point fail to make a left "
                  "turn, and pushes the new point. When the loop ends the stack holds the hull's "
                  "vertices in counterclockwise order."),
            ("p", "The correctness proof is a loop invariant: at the start of each iteration, "
                  "the stack holds exactly the vertices of the convex hull of the points "
                  "processed so far, in counterclockwise order. A point popped is inside the "
                  "triangle formed by p0, the point below it on the stack and the new point, so "
                  "it cannot be a hull vertex. The running time is an aggregate count again: "
                  "each point is pushed once and popped at most once, so the whole loop is "
                  "`O(n)` and the `O(n lg n)` sort dominates."),
            ("p", "Jarvis's march wraps the set like paper. From the lowest point it repeatedly "
                  "chooses the point with the smallest polar angle relative to the last edge, "
                  "one pass over all n points per vertex found, building a right chain up to "
                  "the highest point and then a left chain back down. With h vertices that is "
                  "`O(n·h)`, asymptotically better than Graham's scan when h grows more slowly than lg n, and worse "
                  "when nearly every point is a vertex."),
            ("p", "Section 33.4 finds the closest pair among n points in `O(n lg n)`, where "
                  "testing every pair costs `Θ(n²)`. It divides the points by a vertical line "
                  "into two halves, solves each recursively to get the smaller distance δ, and "
                  "then looks for a closer pair crossing the line. Such a pair lies in the strip "
                  "of width 2δ about the line, and the authors show that at most eight points "
                  "fit in a δ by 2δ rectangle, so each strip point, taken in order of y, needs "
                  "comparing with only the next seven. Presorting by x and y and splitting the "
                  "sorted lists keeps each level linear, giving `T(n) = 2T(n/2) + O(n)`. The "
                  "Algorithms lessons The Convex Hull and Its Definition and The Closest Pair "
                  "and the Strip run both algorithms."),
            ("p", "Now the lab. It runs a hull algorithm that differs from GRAHAM-SCAN in one "
                  "respect: Andrew's monotone chain sorts the points by x instead of by angle and "
                  "builds the lower and upper chains with the same stack and the same "
                  "pop-while-not-a-left-turn rule. So each point is pushed twice, once per "
                  "chain, and the lab compares pushes and pops with 4n. It also runs gift "
                  "wrapping, Jarvis's march, and reports the vertices it returns, the points on "
                  "the boundary by definition, and the work n·h beside n·lg n. A second run with "
                  "floating-point turns shows what rounding does."),
            ("p", "Its presets: <code>general</code> has nine points and 4 hull vertices by "
                  "every route, with 18 + 12 = 30 stack operations against 36. "
                  "<code>edges</code> puts a point at the middle of each side of a square: the "
                  "chain returns 4 vertices, the boundary holds 8 points and gift wrapping "
                  "returns 6, so the answer depends on whether colinear boundary points count. "
                  "<code>segment</code> is five points on a line, a hull of 2. "
                  "<code>duplicate</code> has 6 points typed and 4 distinct. "
                  "<code>needle</code> is a thin triangle whose floating-point run returns 2 "
                  "vertices, a vertex short. <code>single</code> is one point typed twice. The "
                  "book's assumptions, distinct points and three not colinear, exclude the last "
                  "four, which is why it can state the algorithms so cleanly."),
            ("p", "Then type the lesson's points: `1, 0; 7, 1; 4, 3; 9, 5; 5, 9; 0, 6; 6, 6; "
                  "2, 3`. The lab finds 5 hull vertices, (1, 0), (7, 1), (9, 5), (5, 9) and "
                  "(0, 6), agreeing with the definition point by point; (4, 3), (6, 6) and "
                  "(2, 3) are inside. The monotone chain made 16 pushes and 9 pops, 25 against "
                  "4n = 32. Gift wrapping's work is n·h = 40 against n·lg n = 24 on these eight "
                  "points; that comparison is about this set, not about the algorithms."),
            ("h3", "Exercise"),
            ("code", [
                "0, 0; 4, 1; 2, 2; 5, 4; 1, 4; 3, 2",
            ]),
            ("p", "Run GRAHAM-SCAN on these six points by hand: choose p0, sort the rest by "
                  "polar angle about it, and record every push and pop with the turn that "
                  "caused it. Give the hull's vertices in counterclockwise order and the number "
                  "of pops. Then type the points into the lab and compare the vertex set."),
            ("p", "The next lesson leaves algorithms that are fast for questions about which "
                  "problems might never have one. Polynomial Time and Verification opens "
                  "Chapter 34."),
        ],
        "lab": ("geometry", {
            "mode": "hull",
            "preset": "general",
            "panel_title": "Find the hull, and count the stack operations",
            "panel_intro": "Type points as x, y pairs. The lab runs the monotone chain, a "
                           "Graham's scan that sorts by x and builds two chains, and gift "
                           "wrapping, and checks both against the definition point by point. "
                           "Type the lesson's eight points, then the exercise's six.",
        }),
        "steps_title": "Running Graham's scan by hand",
        "steps_intro": "Four steps follow GRAHAM-SCAN; the fifth is a set of your own.",
        "steps": [
            ("Choose p0 and sort",
             "Take the lowest point, the leftmost if two tie. Sort the others by the angle of "
             "the vector from p0, comparing two of them by the sign of a cross product rather "
             "than by computing angles."),
            ("Start the stack",
             "Push p0 and the first two points in sorted order."),
            ("Pop while the turn is not left",
             "For each next point, look at the top two entries of the stack and the new point. "
             "If they make a right turn or are colinear, pop the top and look again. Then push "
             "the new point."),
            ("Read off the hull and the count",
             "The stack, bottom to top, is the hull counterclockwise. Count the pops: never more "
             "than the pushes, which is n."),
            ("Try a set that defeats the march",
             "Type ten points of your own into the lab, all of them hull vertices (points on a "
             "circle of integer coordinates will do), and note n·h against n·lg n. Then move "
             "most of them inside and note how both figures change."),
        ],
        "worked": {
            "title": "Graham's scan on the lesson's eight points",
            "intro": [
                "p0 = (1, 0), the lowest. Sorted by angle about it: (7, 1), (9, 5), (4, 3), "
                "(6, 6), (5, 9), (2, 3), (0, 6). Each turn is orient of the top two and the new "
                "point, positive for left.",
            ],
            "lines": [
                "push (1, 0), (7, 1), (9, 5)",
                "(4, 3): turn at (9, 5) is 16, left; push",
                "(6, 6): turn at (4, 3) is −3; pop (4, 3)",
                "        turn at (9, 5) is 14, left; push",
                "(5, 9): turn at (6, 6) is −8; pop (6, 6)",
                "        turn at (9, 5) is 24, left; push",
                "(2, 3): turn at (5, 9) is 36, left; push",
                "(0, 6): turn at (2, 3) is −21; pop (2, 3)",
                "        turn at (5, 9) is 32, left; push",
                "stack: (1, 0) (7, 1) (9, 5) (5, 9) (0, 6)",
            ],
            "after": [
                "Eight pushes and three pops, and the stack holds the five vertices the lab "
                "found. The lab's monotone chain made 16 pushes and 9 pops on the same points "
                "because it sorts by x and builds two chains, pushing every point once in each; "
                "the counts differ, the hull does not, and both stay within the linear bound "
                "that the push-once, pop-at-most-once argument gives.",
            ],
        },
        "quiz_title": "Hulls and the closest pair",
        "quiz": [
            {"q": "Running GRAHAM-SCAN on the exercise's six points, which points form the hull "
                  "and how many pops are made?",
             "a": ["(0, 0), (4, 1), (5, 4), (1, 4), with 2 pops",
                   "(0, 0), (4, 1), (5, 4), (2, 2), (1, 4), with 1 pop",
                   "(0, 0), (4, 1), (3, 2), (5, 4), (1, 4), with 1 pop",
                   "(0, 0), (4, 1), (5, 4), (1, 4), with 4 pops"],
             "c": 0,
             "why": "From p0 = (0, 0) the angle order is (4, 1), (3, 2), (5, 4), (2, 2), (1, 4). "
                    "(5, 4) makes a right turn at (3, 2), orient −4, so (3, 2) is popped; "
                    "(1, 4) makes a right turn at (2, 2), orient −8, so (2, 2) is popped. Two "
                    "pops, and four vertices remain. (2, 2) is pushed and later popped, so a "
                    "trace that stops early keeps it; four pops would remove points that are on "
                    "the hull."},
            {"q": "Why is the loop of GRAHAM-SCAN linear, though one iteration may pop many "
                  "points?",
             "a": ["Because at most three points are ever on the stack",
                   "Because each point is pushed exactly once and so can be popped at most once",
                   "Because the points are sorted by angle, so pops are rare",
                   "Because a point is popped only when it is colinear with two others"],
             "c": 1,
             "why": "It is the aggregate argument of the previous chapter's KMP: total pops "
                    "cannot exceed total pushes, which is n. The stack can hold any number of "
                    "points, sorting does not make pops rare (the lesson's points pop three of "
                    "eight), and a right turn pops a point as well as a colinear one."},
            {"q": "In the closest-pair algorithm, why does each point in the strip need comparing "
                  "with only the next seven in order of y?",
             "a": ["Because the strip contains at most eight points",
                   "Because at most eight points with pairwise distance at least δ fit in a "
                   "δ by 2δ rectangle",
                   "Because the closest pair is always among the eight points nearest the line",
                   "Because seven comparisons per point make the combine step O(n lg n)"],
             "c": 1,
             "why": "Each half has no two points closer than δ, and a δ by 2δ rectangle straddling "
                    "the line can hold at most eight such points, so a closer partner for a "
                    "point must be among the seven after it. The strip itself can hold many "
                    "points. Seven comparisons per point make the combine step linear, which is "
                    "what gives O(n lg n) overall."},
            {"q": "A set of 64 points has 6 hull vertices. Which bound is smaller here, and is "
                  "that a reason to prefer Jarvis's march on every input?",
             "a": ["n·h = 384 is below n·lg n = 384; no",
                   "n·h = 384 is below n·lg n = 4,096; yes",
                   "n·h = 384 equals n·lg n = 384, so the bounds tie here; no",
                   "n·lg n = 384 is below n·h = 2,048; yes"],
             "c": 2,
             "why": "lg 64 = 6, so n·lg n = 64 · 6 = 384, and n·h = 64 · 6 = 384: they tie, and "
                    "with fewer hull vertices the march's bound would be smaller. The comparison "
                    "is of bounds on this one set: a set of the same size with all 64 points on "
                    "the hull gives n·h = 4,096, and Graham's bound does not depend on h. "
                    "Saying one bound is below the other when they are equal misreads the "
                    "arithmetic."},
        ],
        "mistakes": [
            ("Thinking the hull algorithm must find interior points to discard them",
             "Neither algorithm tests a point for being inside. Graham's scan pops a point when "
             "a later point makes a non-left turn with it, and the invariant guarantees that "
             "such a point is not a vertex of the hull so far. On the lesson's points, (4, 3) is "
             "pushed and later popped; nothing ever asked whether it was inside."),
            ("Expecting every algorithm to return the same list on every input",
             "The book assumes distinct points and no three colinear on the hull. On the lab's "
             "edges preset, a square with midpoints, the monotone chain returns 4 vertices, the "
             "boundary has 8 points and gift wrapping returns 6. Each answers a slightly "
             "different question; the assumption is what makes the answer unique."),
            ("Reading O(n·h) as always faster or always slower",
             "Jarvis's march wins asymptotically when h grows more slowly than lg n and loses when h is large. "
             "Which applies depends on the input, and on the lesson's eight points n·h = 40 "
             "against n·lg n = 24 says only that this set has many hull vertices for its "
             "size."),
        ],
        "standard": ("Finish when you can run Graham's scan by hand.",
                     "For six to eight points with small integer coordinates, choose p0, sort by "
                     "angle, trace every push and pop with its turn, give the hull, and explain "
                     "why the loop is linear and why the strip check in section 33.4 is too."),
        "note": ("The lab's hull algorithm is the monotone chain, a variant of Graham's scan "
                 "that sorts by x; its push and pop counts are not GRAHAM-SCAN's, though its "
                 "hull is the same, and this lab does not run the closest-pair algorithm. The "
                 "counts are of one point set; the linear loop and the O(n lg n) bound come "
                 "from the book's arguments."),
    },
]
