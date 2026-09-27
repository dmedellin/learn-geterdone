"""Strings and Pattern Matching, lessons 07-12 - skipping, hashing, many patterns, and the suffix array."""

LESSONS = [
    # ---------------------------------------------------------------- 07
    {
        "slug": "shifting-by-more-than-one",
        "title": "Shifting by More Than One",
        "module": "Skipping, and its worst case",
        "one_line": "Compare the window from the right, then jump by the last occurrence of the character under its final position, and read 19 of 66 characters.",
        "summary": (
            "Horspool builds one table from the pattern's first `m − 1` characters and uses it "
            "to shift past positions rather than sliding one at a time. On the lab's prose it "
            "examines 14 of the 61 alignments, compares 19 characters at 18 distinct positions of the 66, and makes 19 "
            "comparisons against naive matching's 66. Every one of those numbers is a fact "
            "about which characters this text happens to contain, and the algorithm's proved "
            "worst case is the same `m(n − m + 1)` naive matching has."
        ),
        "key": [
            "compare the window right to left; stop at the first disagreement",
            "shift by the table entry for the text character under the last position",
            "the table is built from p[0..m−2], so p's own last character shifts the full m",
            "measured: 14 alignments of 61, 19 comparisons, 52 alignments skipped outright",
            "19 comparisons at only 18 distinct positions: 48 characters are never read",
            "naive 66 and KMP 66 on the same text; Horspool's worst case is still m(n − m + 1)",
        ],
        "key_label": "One table, a shift that can be the whole pattern, and no guarantee behind it",
        "concepts_intro": (
            "The hard idea is that the saving comes from the text as much as from the pattern. "
            "The other two are the table and the direction of comparison that makes it usable."
        ),
        "concepts": [
            ("Comparing from the right is what makes a jump computable",
             "The window sits over `t[s..s+m−1]` and the first comparison is `t[s+m−1]` against "
             "`p[m−1]`. If that fails, the character `t[s+m−1]` still has to line up with some "
             "occurrence of itself in the pattern at any future alignment that can match, so the "
             "next plausible offset is found by asking where that character last occurs in the "
             "pattern. Comparing left to right gives no such handle: the character that failed is "
             "at an unknown distance from the window's end."),
            ("The table is one entry per character, and it is built from m − 1 of them",
             "For each character `c`, the shift is `m − 1 − j` where `j` is the largest index "
               "below `m − 1` with `p[j] = c`, and `m` if there is none. On `mainly` that gives "
               "`m → 5`, `a → 4`, `i → 3`, `n → 2`, `l → 1`, and `m` for everything else "
               "&mdash; including `y`, the pattern's own last character, because the table "
               "deliberately excludes position `m − 1`. Excluding it is what lets the algorithm "
               "shift the full `m` when the window's last character is the pattern's last "
               "character and everything else failed."),
            ("The saving is a property of the text, and nothing is proved by it",
             "The panel reports 52 alignments skipped outright at an average shift of 4.71 out "
             "of a maximum of 6, and 19 comparisons where the naive matcher makes 66. All of "
             "that is because this text is English and most of its characters do not appear in "
             "`mainly`. The proved worst case is unchanged from the naive matcher's: `m(n − m + "
             "1)` comparisons, attained on a text this page's sibling &ldquo;The Text Where "
             "Nothing Is Skipped&rdquo; loads with one click."),
        ],
        "read_title": "One table, one direction of comparison, and a shift that is usually large",
        "read_intro": "The algorithm, the correctness argument for the shift, the measured saving, and the fact that no bound improved.",
        "body": [
            ("def", ("The Horspool shift table",
                     "For a pattern `p` of length `m` over an alphabet `A`, the "
                     "<strong>shift table</strong> is defined for every `c` in `A` by: "
                     "`shift[c] = m − 1 − j`, where `j` is the largest index with "
                     "`0 &le; j &le; m − 2` and `p[j] = c`; and `shift[c] = m` if `c` does not "
                     "occur among `p[0..m−2]`. Every entry lies between 1 and `m`.")),
            ("def", ("Horspool matching",
                     "Start with the window at offset `s = 0`. Compare `t[s+k]` with `p[k]` for "
                     "`k = m − 1` downwards, stopping at the first disagreement or reporting a "
                     "match when `k` falls below 0. Then set `s` to `s + shift[t[s+m−1]]` and "
                     "repeat while `s + m &le; n`. The shift is read from the text character "
                     "under the window's LAST position, whatever position the comparison "
                     "actually failed at.")),
            ("thm", ("The shift skips no match",
                     "If the window is at offset `s` and `c = t[s+m−1]`, then no offset `s'` "
                     "with `s &lt; s' &lt; s + shift[c]` can begin an occurrence of `p`.")),
            ("proof", ("Suppose an occurrence begins at such an `s'`. The character `c` sits at "
                       "text position `s + m − 1`, which lies inside the occurrence's window "
                       "because `s' &le; s + m − 1 &le; s' + m − 1`, at pattern index "
                       "`i = s + m − 1 − s'`, and `0 &le; i &le; m − 2` because `s' &gt; s`.",
                       "So `p[i] = c` for some `i &le; m − 2`, and therefore `shift[c]` is "
                       "`m − 1 − j` for the largest such index `j`, giving `i &le; j` and "
                       "`s + m − 1 − s' &le; m − 1 − shift[c] + ... `. Rearranged: "
                       "`s' &ge; s + m − 1 − j = s + shift[c]`, contradicting "
                       "`s' &lt; s + shift[c]`.",
                       "If `c` does not occur in `p[0..m−2]` at all then no such `i` exists, so "
                       "no occurrence can begin strictly after `s` and before `s + m`, which is "
                       "the case `shift[c] = m`.")),
            ("p", "The lab checks that argument empirically on every keystroke rather than "
                  "resting on it, because the failure mode of a skipping algorithm is to jump "
                  "over an answer and return a shorter list of positions, and a shorter list of "
                  "correct positions looks exactly like a correct answer. The match positions "
                  "are compared with a scan that tests every offset."),
            ("example", ("Fourteen alignments out of sixty-one",
                         "The lab opens on `the rain in spain stays mainly in the plain and "
                         "never in the hills`, 66 characters, searched for `mainly`. Naive "
                         "matching would try 61 alignments; Horspool examines 14, at offsets 0, "
                         "4, 7, 13, 19, 24, 30, 36, 39, 43, 45, 51, 57 and 60. The shifts it "
                         "takes are 4, 3, 6, 6, 5, 6, 6, 3, 4, 2, 6, 6, 3, 6 &mdash; seven of "
                         "the fourteen are the full `m`. The single match is at offset 24, and "
                         "it is examined.")),
            ("p", "Those fourteen alignments cost 19 comparisons in total, and the breakdown is lopsided: thirteen of them fail on their very first comparison and cost 1 each, and the fourteenth is the match at offset 24, which compares all 6. Thirteen plus six is 19."),
            ("p", "Those 19 comparisons landed on only 18 distinct positions of the text, because position 24 is compared twice &mdash; once as the last position of the window at offset 19, and again inside the matching window. So 48 of the 66 characters of this text were never compared to anything at all. That is the property the algorithm is famous for, and it is why `characters skipped entirely` is the counter the panel leads with."),
            ("h3", "Why the average shift is 4.71 and what it is an average of"),
            ("p", "The panel's average shift is the sum of the shifts divided by the number of "
                  "alignments examined, which is `66/14`, printed as the exact fraction `33/7`. "
                  "The sum of the shifts is the text length because the window walks from 0 "
                  "past the end exactly once, so that average is `n` over the number of "
                  "alignments &mdash; a different quantity from the average over the alphabet, "
                  "which would be a fact about the pattern alone."),
            ("h3", "The letters that shift the full six, including one of the pattern's own"),
            ("p", "The shift table has `m → 5`, `a → 4`, `i → 3`, `n → 2`, `l → 1`, and 6 for "
                  "the space and for `d, e, h, p, r, s, t, v` and `y`. The `y` is worth a second "
                  "look, because `y` is in the pattern &mdash; it is `p[5]`, the last character. "
                  "The table is built from `p[0..4]` only, so `y` is absent from it and gets the "
                  "default `m`. That is deliberate: if the window's last character is `y` and "
                  "the comparison still failed, the failure was further left, and no alignment "
                  "before `s + m` can succeed either."),
            ("p", "The `l → 1` entry is the other end of the same table. `l` occurs at `p[4]`, "
                  "one place before the end, so a window ending in `l` can only be advanced by "
                  "one. A pattern whose penultimate character is common in the text therefore "
                  "loses most of the benefit, which is the mechanism the next page pushes to its "
                  "limit."),
            ("h3", "What did not improve"),
            ("p", "Naive matching takes 66 comparisons on this text and KMP takes 66 as well. "
                  "Horspool takes 19, which is better by a factor of three and a half &mdash; "
                  "and its worst case is `m(n − m + 1)`, exactly the naive matcher's, while "
                  "KMP's remains `2n`. So on the page's own numbers the fastest algorithm here "
                  "has the weakest guarantee of the three, and the slowest has the strongest."),
            ("p", "There is no contradiction and there is also no ranking. Three measurements "
                  "and three bounds are six statements about different things, and the only ones "
                  "that hold for texts nobody has typed yet are the bounds."),
        ],
        "lab": ("strings", {
            "mode": "horspool",
            "preset": "english",
            "panel_title": "Type a text and a pattern, and watch which characters are never read",
            "panel_intro": "The bar chart is one bar per alignment EXAMINED, which on this text "
                           "is fourteen of sixty-one. The shift table below is built from the "
                           "pattern's first `m − 1` characters, and the step table shows where "
                           "each window sat, how far the comparison got from the right, and how "
                           "far it then jumped.",
        }),
        "steps_title": "Building the table, then reading the shift off the right character",
        "steps_intro": "The commonest mistake here is reading the shift from the character that failed. It is read from the window's last position, always.",
        "steps": [
            ("Build the table from p[0..m−2], and check the last character's entry",
             "Write the pattern out, number the positions, and for each character record "
             "`m − 1 − j` for its largest index below `m − 1`. Then confirm that the pattern's "
             "own final character got the default `m`, because that entry is the one that looks "
             "like a bug and is not."),
            ("Compare from the right and record how far you got",
             "The count for one alignment is the number of characters matched from the right plus "
             "one for the disagreement, or `m` for a match. The panel's step table prints that "
             "middle number, and it is usually 0."),
            ("Read the shift from the window's last position, not the mismatch",
             "On this text the two coincide, because every failing alignment fails at the last position. Switch to the four-letter preset to see them part: at offset 2 the window is `TTACAGA`, the comparison fails at position 5 on a `G` whose table entry is 6, and the window's last character is an `A` whose entry is 2. The shift taken is 2, and the wrong rule would have jumped to offset 8."),
            ("Count the characters never touched, not just the comparisons",
             "19 comparisons landed on 18 distinct positions here, because one position was compared twice. The second figure is the one that explains why the algorithm is fast on large alphabets &mdash; 48 characters unread &mdash; and it is not what the comparison counter measures."),
        ],
        "worked": {
            "title": "The first five alignments, and the shift each one takes",
            "intro": [
                "The text is `the rain in spain stays mainly in the plain and never in the "
                "hills` and the pattern is `mainly`, so `m = 6` and the shift table is built "
                "from `mainl`.",
            ],
            "lines": [
                "shift table   m 5   a 4   i 3   n 2   l 1   everything else 6   (y is 6)",
                "",
                "step  at  window     last char   comparisons   shift",
                "  1    0  'the ra'       a            1           4",
                "  2    4  'rain i'       i            1           3",
                "  3    7  'n in s'       s            1           6",
                "  4   13  'pain s'       s            1           6",
                "  5   19  'tays m'       m            1           5",
                "  6   24  'mainly'       y            6           6     a match",
                "  7   30  ' in th'       h            1           6",
                "  8   36  'e plai'       i            1           3",
                "  9   39  'lain a'       a            1           4",
                " 10   43  ' and n'       n            1           2",
                " 11   45  'nd nev'       v            1           6",
                " 12   51  'er in '     space          1           6",
                " 13   57  'the hi'       i            1           3",
                " 14   60  ' hills'       s            1           6",
                "",
                "alignments examined                             14   (of 61)",
                "shifts taken       4 3 6 6 5 6 6 3 4 2 6 6 3 6      sum = 66",
                "comparisons        13 x 1 + 1 x 6                  = 19",
                "distinct positions compared   position 24 twice    = 18   (of 66)",
                "characters never compared to anything  66 - 18     = 48",
                "alignments skipped outright  66 - 14               = 52",
                "average shift  66/14 = 33/7                        = 4.71",
                "naive 66      KMP 66      Horspool 19",
            ],
            "after": [
                "Thirteen of the fourteen rows have a 1 in the comparisons column, and every "
                "one of those thirteen failed at the window's last position &mdash; which is "
                "why the shift and the mismatch agree on this text and why it is a bad text for "
                "learning the difference between them. The four-letter preset is the one to use "
                "for that: at its offset 2 the window is `TTACAGA`, the failure is at position 5 "
                "on a `G` whose table entry is 6, and the shift taken is 2 because the window's "
                "last character is an `A`.",
                "The other row worth a second look is the sixth. The match at offset 24 costs 6 "
                "comparisons, not 1, so the 19 total is 13 plus 6 rather than 14 plus something "
                "&mdash; and those 19 comparisons land on 18 distinct positions, because "
                "position 24 is the last position of the window at offset 19 and is compared "
                "again inside the matching window.",
                "For a faded rehearsal, keep the text and change the pattern to `plain`. The "
                "supplied first move is the table: it is built from `plai`, so `p → 4`, "
                "`l → 3`, `a → 2`, `i → 1`, and 5 for everything else including `n`. Predict "
                "whether the number of alignments examined goes up or down, and say which entry "
                "of the table is responsible.",
                "Then try `hills`. It occurs at the very end of the text, and its table entry "
                "for `l` is 1 because `l` is `p[3]`. Predict what happens to the comparison "
                "count relative to `mainly` before running it, and then say whether the change "
                "is about the pattern, the text, or both.",
            ],
        },
        "quiz_title": "Where the shift comes from, and what it is worth",
        "quiz": [
            {"q": "On the four-letter preset the window at offset 2 is `TTACAGA`, and the comparison fails at position 5 on a `G` whose table entry is 6. The shift taken is 2. Why?",
             "a": ["Because the table entry for G is wrong",
                   "Because the shift is read from the window's last character, an A, whose entry is 2",
                   "Because the shift is capped at the number of characters matched",
                   "Because G occurs later in the pattern than A does"],
             "c": 1,
             "why": "Horspool always reads the shift from the text character aligned with the "
                    "window's final position, whatever position the comparison failed at. Here "
                    "that is `A`, with entry 2, so the window moves to offset 4; the wrong rule "
                    "would have used `G`'s entry of 6 and jumped to offset 8. The correctness "
                    "proof only rules out the offsets that the LAST character rules out, so the "
                    "other rule has nothing behind it."},
            {"q": "Why does the pattern's own last character get the default shift of m?",
             "a": ["Because it is a mistake in the table that happens not to matter",
                   "Because the table is built from p[0..m−2], and if the window's last character already matches the failure was further left",
                   "Because the last character is compared first and cannot fail",
                   "Because a match shifts by m anyway"],
             "c": 1,
             "why": "Excluding position `m − 1` is deliberate. If the window's last character "
                    "equals `p[m−1]` and the alignment still failed, the disagreement was at some "
                    "earlier position, and the theorem's argument then rules out every offset "
                    "before `s + m`. Including that position would give a shift of 0 and the "
                    "algorithm would not advance."},
            {"q": "Horspool makes 19 comparisons here where naive matching makes 66. What has been established about Horspool?",
             "a": ["That it is about three and a half times faster than naive matching",
                   "That on this text it made 19 comparisons; its proved worst case is m(n − m + 1), the same as naive matching's",
                   "That its bound is better than naive matching's",
                   "That skipping always pays on English text"],
             "c": 1,
             "why": "The saving is a measurement and the bound did not move: Horspool has no "
                    "better worst case than the naive matcher, and the sibling lesson "
                    "&ldquo;The Text Where Nothing Is Skipped&rdquo; is a 30-character input on "
                    "which it makes 130 comparisons where naive makes 26."},
            {"q": "The average shift is reported as 33/7 on a maximum of 6. What is that the average of?",
             "a": ["The table entries, averaged over the alphabet",
                   "The shifts actually taken, which sum to the text length divided by the alignments examined",
                   "The characters skipped per comparison",
                   "The distance between consecutive matches"],
             "c": 1,
             "why": "The window walks from 0 past the end exactly once, so the shifts sum to `n`, "
                    "and dividing by the 14 alignments examined gives `66/14 = 33/7`. Averaging "
                    "the table over the alphabet would be a fact about the pattern alone and "
                    "would not depend on the text at all."},
        ],
        "mistakes": [
            ("Reading the shift from the mismatching character",
             "This is the error that makes the algorithm wrong rather than slow. Boyer&ndash;Moore "
             "has a rule of that shape and it needs a second table to stay correct; Horspool's "
             "one-table version works only because the shift is read from a fixed position, the "
             "window's last. The lab's scan over every offset is there to catch the difference."),
            ("Concluding that a large alphabet guarantees large shifts",
             "It makes them likely and promises nothing. The DNA preset has four letters, all of "
             "which occur in the pattern, and no shift there is ever the full `m`; the average "
             "drops to 2.71 from this page's 4.71. Whether a character is in the pattern is not "
             "a function of how many characters there are."),
            ("Quoting the comparison count as the characters examined",
             "They are not the same figure even here: 19 comparisons landed on 18 distinct "
             "positions, because position 24 is compared once as a window's last character and "
             "again inside the match. On the four-letter preset the gap is wider &mdash; 43 "
             "comparisons at 35 positions &mdash; and the figure that explains the algorithm's "
             "reputation is the second one, which the panel does not print."),
        ],
        "standard": ("Finish when you can build the table for a pattern you have not seen and take four shifts by hand without consulting the mismatch.",
                     "You should be able to define `shift[c]` including the exclusion of "
                     "`p[m−1]`, prove that no offset before `s + shift[c]` can begin a match, "
                     "read a shift from the window's last position rather than the failure, "
                     "distinguish 19 comparisons from 18 positions touched, and state Horspool's "
                     "worst case without hedging it."),
        "note": ("The whole of this page's saving rests on the window's last character usually "
                 "shifting far. &ldquo;The Text Where Nothing Is Skipped&rdquo; takes the same "
                 "algorithm to a 30-character text where that character always shifts by 1, and "
                 "the comparison count goes to five times the naive matcher's on the same input "
                 "&mdash; the largest reversal on this course."),
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "the-text-where-nothing-is-skipped",
        "title": "The Text Where Nothing Is Skipped",
        "module": "Skipping, and its worst case",
        "one_line": "Thirty a's searched for `baaaa`: every shift is 1, nothing is skipped, and the skipping algorithm makes five times the comparisons the naive one does.",
        "summary": (
            "Put the pattern's odd character at the front instead of the end and Horspool's "
            "table becomes useless: the window's last character always matches, the shift is "
            "always 1, and each alignment compares `m` characters before failing. The lab "
            "reports 130 comparisons against the naive matcher's 26 on the same input &mdash; "
            "exactly five times &mdash; and reversing the pattern reverses the two numbers. "
            "The algorithm did not change; the position of one character did."
        ),
        "key": [
            "text a^30, pattern baaaa:  26 alignments, 0 skipped, every shift 1",
            "each alignment matches m − 1 from the right, then fails on the b",
            "measured: Horspool 130, naive 26, KMP 30,  on one 30-character text",
            "130 = 26 × 5 = the alignments times m:  the bound m(n − m + 1), attained",
            "reverse the pattern to aaaab: Horspool 26 and naive 130, exactly swapped",
            "Horspool has no better worst case than naive matching, only a better average",
        ],
        "key_label": "The same table, the same text, and one character in a different place",
        "concepts_intro": (
            "The hard idea is that both worst cases are the same bound reached by opposite "
            "inputs. The other two are why this text defeats the table and what survives it."
        ),
        "concepts": [
            ("The table is useless when the window's last character is always in the pattern",
             "The pattern is `baaaa` and the table is built from `baaa`, so `a → 1` and "
             "`b → 4`. Every window of a run of a's ends in `a`, so every shift is 1 and the "
             "window advances as slowly as the naive matcher's. The panel reports 26 alignments "
             "out of 26 examined and 0 alignments skipped, which is the only preset in this kit "
             "that prints a zero there."),
            ("Comparing from the right is what turns a slow shift into expensive alignments",
             "At each alignment the comparison runs `p[4], p[3], p[2], p[1]` &mdash; four a's "
             "against four a's, all matching &mdash; and then `p[0] = b` against `a`, which "
             "fails. So one alignment costs the full `m = 5`, and 26 alignments cost 130. The "
             "naive matcher on the same input compares `p[0] = b` first at every alignment and "
             "leaves after one comparison, for 26 in total. The direction of comparison is the "
             "whole difference."),
            ("The two worst cases are the same bound, reached by mirror-image inputs",
             "Reverse the pattern to `aaaab` on the same text and the numbers swap exactly: "
             "Horspool 26, naive 130. Both algorithms have worst case `m(n − m + 1)`, which is "
             "`5 × 26 = 130` here, and both attain it &mdash; on different inputs. Neither "
             "algorithm dominates the other and neither has a guarantee the other lacks; "
             "Horspool's advantage is an average over texts, and an average over texts is not a "
             "statement any single measurement can make."),
        ],
        "read_title": "One character moved, and a factor of five in the other direction",
        "read_intro": "Why the shift collapses, why the alignments become expensive, the mirror input, and what remains true of both algorithms.",
        "body": [
            ("p", "Keep the text as a run of thirty a's and set the pattern to `baaaa`. The "
                  "shift table is built from `baaa`, giving `a → 1` and `b → 4`; every character "
                  "of the text is `a`; so every shift is 1 and the window visits all 26 "
                  "alignments in turn. Nothing is skipped."),
            ("thm", ("Horspool attains m(n − m + 1) on this family",
                     "On the text `a^N` with the pattern `b a^(m−1)`, Horspool examines all "
                     "`N − m + 1` alignments, makes exactly `m` comparisons at each, and "
                     "reports no match. Its total is `m(N − m + 1)`, which is the maximum "
                     "possible.")),
            ("proof", ("The shift table built from `p[0..m−2] = b a^(m−2)` gives `shift[a] = 1`, "
                       "because `a` occurs at index `m − 2`, the largest index below `m − 1`. "
                       "Every character of the text is `a`, so every shift is 1 and every offset "
                       "from 0 to `N − m` is examined.",
                       "At one alignment the comparison runs from `k = m − 1` downwards. For "
                       "`k &ge; 1` the pattern character is `a` and the text character is `a`, "
                       "so those `m − 1` comparisons succeed. At `k = 0` the pattern character "
                       "is `b` and the text character is `a`, so the comparison fails. That is "
                       "`m` comparisons and no match.",
                       "Multiplying gives `m(N − m + 1)`, and the same bound proved for the "
                       "naive matcher applies here for the same reason: `N − m + 1` alignments "
                       "at `m` comparisons each is the ceiling for any algorithm that compares "
                       "within a window and shifts by at least 1.")),
            ("p", "At `N = 30` and `m = 5` that is `5 × 26 = 130`, and the panel says so: 130 "
                  "comparisons over 26 alignments, 0 skipped, average shift exactly 1. The naive "
                  "matcher on the same input makes 26 and KMP makes 30."),
            ("example", ("The mirror image, one keystroke away",
                         "Change the pattern to `aaaab` and keep the thirty a's. Now the table "
                         "is built from `aaaa`, still giving `a → 1`, so Horspool still examines "
                         "all 26 alignments and still skips nothing &mdash; but the comparison "
                         "from the right meets `p[4] = b` against `a` immediately and fails "
                         "after one comparison. Horspool makes 26 and the naive matcher, which "
                         "matches four a's before reaching the `b`, makes 130. The two counts "
                         "have swapped and neither algorithm was touched.")),
            ("math", [
                "text a^30, m = 5, 26 alignments                Horspool   naive   KMP",
                "pattern  baaaa   odd character at the front         130      26     30",
                "pattern  aaaab   odd character at the end            26     130     56",
                "pattern  aaaaa   no odd character, 26 matches       130     130     30",
                "",
                "the bound m(n - m + 1) = 5 x 26 for both             130     130",
            ]),
            ("p", "The third row is the one that spoils any story about one algorithm being for "
                  "one kind of input. A pattern of five a's matches at every one of the 26 "
                  "alignments, so both algorithms compare all five characters at all 26 offsets "
                  "and both make 130. The bound is attained by both, simultaneously, and KMP "
                  "makes 30."),
            ("h3", "What Horspool's guarantee actually is"),
            ("p", "It is `m(n − m + 1)`, and that is the same as the naive matcher's. There is "
                  "no theorem of the form &ldquo;Horspool is never worse than naive "
                  "matching&rdquo; &mdash; this page is a counterexample to it &mdash; and no "
                  "theorem bounding Horspool below the naive matcher's worst case. What is true "
                  "is a statement about an average: over texts whose characters are drawn "
                  "independently and uniformly from a large alphabet, the expected number of "
                  "comparisons is close to `n/m`."),
            ("p", "That expectation is where the reputation comes from, and it is worth being "
                  "clear about what kind of claim it is. It quantifies over a distribution of "
                  "inputs, not over inputs, so a single text can be arbitrarily far from it in "
                  "either direction and nothing is refuted. This page's text is one such, and "
                  "the previous page's prose is another in the opposite direction."),
            ("h3", "Which of the four matchers is safe on a text like this"),
            ("p", "KMP makes 30 comparisons on the run of thirty a's with `baaaa`, and 56 with "
                  "`aaaab`, both under `2n = 60`. The automaton takes exactly 30 steps on either. "
                  "Those two are the ones whose counts cannot be made to blow up by choosing the "
                  "text, because their bounds are linear in `n` with no `m` in them at all."),
            ("p", "So the ranking across this course's four matchers changes three times "
                  "depending on the input, and the two bounds do not change at all: "
                  "`m(n − m + 1)` for naive matching and Horspool, `2n` for KMP, exactly `n` for "
                  "the automaton. When the question is which to use on text you have not seen, "
                  "the bounds are the only evidence available."),
        ],
        "lab": ("strings", {
            "mode": "horspool",
            "preset": "stuck",
            "panel_title": "The input where every shift is one, and the counter that says so",
            "panel_intro": "The bar chart is a solid block at the dashed line because every "
                           "alignment costs the full `m`, and the counter for characters skipped "
                           "reads 0 &mdash; the only preset here that does. Reverse the "
                           "pattern in the box to `aaaab` and watch the Horspool and naive "
                           "columns exchange values.",
        }),
        "steps_title": "Finding an algorithm's worst case by asking what its rule needs",
        "steps_intro": "Read the shift rule and the comparison order as two separate requirements, then defeat each one.",
        "steps": [
            ("Defeat the shift first: make the window's last character common in the pattern",
             "`shift[c]` is small when `c` occurs late in `p[0..m−2]`. A pattern whose "
             "penultimate character is the text's only character forces `shift = 1` at every "
             "alignment, which is the most any input can do to the table."),
            ("Then make each alignment expensive, using the comparison order",
             "Horspool compares from the right, so the disagreement must be as far left as "
             "possible: put the one character the text lacks at `p[0]`. Both requirements "
             "together give `b a^(m−1)` against `a^N`."),
            ("Reverse the pattern and check the numbers swap",
             "If the construction is right, moving the odd character from the front to the end "
             "should transfer the 130 to the naive matcher. That the swap is exact is the "
             "evidence that the worst case is about the comparison order and nothing else."),
            ("Read both bounds before choosing an algorithm",
             "`m(n − m + 1)` is 130 here and `2n` is 60. On a text nobody has typed yet those "
             "two numbers are the whole of what is known, and the measured columns from the "
             "previous page are not evidence about this one."),
        ],
        "worked": {
            "title": "One hundred and thirty comparisons, and the same input the other way round",
            "intro": [
                "The text is thirty a's. The pattern is `baaaa`, so `m = 5`, the shift table is "
                "built from `baaa`, and there are 26 alignments.",
            ],
            "lines": [
                "shift table         a -> 1   (a occurs at index 3)      b -> 4",
                "",
                "one alignment, compared from the right:",
                "  k = 4   p[4] = a  vs  a   match",
                "  k = 3   p[3] = a  vs  a   match",
                "  k = 2   p[2] = a  vs  a   match",
                "  k = 1   p[1] = a  vs  a   match",
                "  k = 0   p[0] = b  vs  a   FAIL      5 comparisons",
                "  window's last character is a, so shift = 1",
                "",
                "alignments examined     n - m + 1 = 30 - 5 + 1        = 26",
                "comparisons             26 x 5                        = 130",
                "alignments skipped                                    = 0",
                "average shift                                         = 1",
                "the bound m(n - m + 1)  5 x 26                        = 130",
                "",
                "naive on the same input   fails on p[0] at once, 26 x 1 = 26",
                "KMP on the same input                                  = 30",
                "reverse the pattern to aaaab:  Horspool 26, naive 130",
            ],
            "after": [
                "The line to read twice is the last. Reversing the pattern changes neither "
                "algorithm, neither bound, nor the text, and it exchanges the two measured "
                "counts exactly. Any sentence of the form &ldquo;this algorithm is faster&rdquo; "
                "that survives that keystroke was not about the measurement.",
                "For a faded rehearsal, keep the text and set the pattern to `abaaa`. The "
                "supplied first move: the table is built from `abaa`, so `a → 1` and `b → 3`, "
                "and the shift is still 1 at every alignment because the text is all a's. Work "
                "out the cost of one alignment by comparing from the right, give the total, and "
                "say whether it is nearer 26 or nearer 130.",
                "Then do the harder one. Find a pattern of length 5 over `{a, b}` on which "
                "Horspool and the naive matcher make the SAME number of comparisons on thirty "
                "a's. The supplied hint: there is one where both make 130, and it has no `b` in "
                "it at all. Say why, and say what that says about the claim that skipping helps.",
            ],
        },
        "quiz_title": "Worst cases, mirror images, and what a bound covers",
        "quiz": [
            {"q": "Horspool makes 130 comparisons and naive matching makes 26 on this input. What does that show?",
             "a": ["That Horspool is implemented wrongly here",
                   "That Horspool's worst case is the same m(n − m + 1) as naive matching's, and this input attains it",
                   "That skipping algorithms are slower than sliding ones",
                   "That the shift table should have included p[m−1]"],
             "c": 1,
             "why": "The counts are correct and both algorithms have the same worst-case bound, "
                    "`5 × 26 = 130`; this text attains it for one of them and the reversed "
                    "pattern attains it for the other. Including `p[m−1]` in the table would "
                    "give a shift of 0 and the algorithm would not terminate."},
            {"q": "Why does each alignment here cost the full 5 comparisons?",
             "a": ["Because the shift is 1, so more alignments are examined",
                   "Because the comparison runs from the right and meets the four matching a's before reaching the b at p[0]",
                   "Because the text has only one distinct character",
                   "Because the match is reported at every offset"],
             "c": 1,
             "why": "The shift and the per-alignment cost are two separate effects of the same "
                    "construction: `shift[a] = 1` makes all 26 alignments get examined, and the "
                    "right-to-left order makes each of them cost `m`. There is no match at any "
                    "offset, since the text contains no `b`."},
            {"q": "The pattern is changed to `aaaaa` on the same thirty a's. What happens?",
             "a": ["Horspool makes 26 and naive makes 130",
                   "Both make 130, both attain the bound, and every offset is a match",
                   "Horspool makes 130 and naive makes 26",
                   "Neither finds a match, so both make 26"],
             "c": 1,
             "why": "A match costs all `m` comparisons for either algorithm, and every one of "
                    "the 26 offsets is a match, so both make `5 × 26 = 130` and both are at "
                    "their proved ceiling at the same time. This is the row that rules out any "
                    "story in which one algorithm is for one kind of input."},
            {"q": "Horspool's expected comparison count is often quoted as about n/m. What kind of claim is that?",
             "a": ["A worst-case bound, like m(n − m + 1)",
                   "A statement about a distribution of texts, which no single measurement can confirm or refute",
                   "A measurement on English prose",
                   "An amortised bound, proved by a potential argument"],
             "c": 1,
             "why": "It quantifies over randomly drawn texts rather than over all texts, so any "
                    "particular input can be far from it in either direction with nothing "
                    "refuted &mdash; this page's 130 and the previous page's 19 are both "
                    "consistent with it. The worst-case bound is the separate, unconditional "
                    "`m(n − m + 1)`."},
        ],
        "mistakes": [
            ("Calling this input unrealistic and moving on",
             "A run of one symbol is what padded fixed-width records, silence in an audio "
             "stream, and a zeroed disk block look like, and a short repeated cycle is what DNA "
             "and instruction streams look like. But the more important point is that "
             "realistic is a claim about a distribution and the bound is not: the bound covers "
             "this input because it covers every input, which is the only reason it is worth "
             "having."),
            ("Concluding that Horspool should compare left to right",
             "It cannot. The shift rule needs a known character at a known offset to look up, "
             "and comparing from the right is what makes the window's last character the one "
             "whose identity is always established. A left-to-right variant has no table to "
             "consult and is the naive matcher."),
            ("Reading 130 against 26 as a five-fold slowdown of the algorithm",
             "It is a five-fold slowdown on one input, and the reversed pattern is a five-fold "
             "speed-up on the same text. The factor is a property of the pair, and averaging the "
             "two would produce a number describing neither."),
        ],
        "standard": ("Finish when you can construct Horspool's worst case from its two rules and predict the reversal without running it.",
                     "You should be able to say which rule forces `shift = 1` and which forces "
                     "`m` comparisons per alignment, prove the total is `m(n − m + 1)`, predict "
                     "that reversing the pattern swaps the two counts, explain why `aaaaa` makes "
                     "both algorithms attain the bound at once, and state what kind of claim "
                     "`n/m` is."),
        "note": ("Every matcher so far compares characters, and three of the four can be made "
                 "expensive by choosing them. The next module stops comparing: &ldquo;A Rolling "
                 "Hash, and a Collision You Can Read&rdquo; reduces a window to one number and "
                 "compares numbers instead &mdash; which introduces a new failure that none of "
                 "these pages has, because two different windows can share a number."),
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "a-rolling-hash-and-its-collisions",
        "title": "A Rolling Hash, and a Collision You Can Read",
        "module": "Hashing, and the verification",
        "one_line": "Reduce each window to one number computed from the last, then read off the three windows whose number matches the pattern's and whose characters do not.",
        "summary": (
            "Rabin&ndash;Karp hashes the pattern once and each window in constant time from the "
            "window before, so the scan is `n` arithmetic steps. Equal hashes are not a match: "
            "on the lab's opening text 7 windows hash to 36 and only 4 of them are "
            "occurrences. The other three are printed with their characters so they can be "
            "checked by eye, and the verification that separates them is not an optimisation "
            "that can be skipped &mdash; it is the only reason the answer is right."
        ),
        "key": [
            "hash of a window: its characters as digits in base b, taken modulo m",
            "roll forward: drop the leading digit, shift, add the trailing one",
            "base 256, modulus 41:  the pattern ain hashes to 36",
            "41 windows, 7 hash equal to 36, 4 are matches, 3 are collisions",
            "the collisions are at offsets 33, 36 and 38:  ' th', 'e p', 'pla'",
            "21 characters compared verifying, 9 of them spent on the collisions",
        ],
        "key_label": "One number per window, and the three windows that share the pattern's",
        "concepts_intro": (
            "The hard idea is that the hash decides nothing on its own. The other two are how "
            "the roll works and why the arithmetic is exact rather than machine-dependent."
        ),
        "concepts": [
            ("A hash equal is a candidate, and a candidate must be verified",
             "The scan compares numbers, and equal numbers mean the characters might be equal. "
             "On the opening text 7 of the 41 windows hash to 36, the pattern's value, and 3 of "
             "those are not `ain` at all: the panel lists them with their characters, at offsets "
             "33, 36 and 38. Every one of the 7 costs `m = 3` character comparisons to settle, "
             "so 21 comparisons are spent on verification of which 9 establish nothing but a "
             "false alarm. Removing the verification does not make the algorithm faster, it "
             "makes it wrong."),
            ("The roll is the one value on the page derived from another value",
             "Every other number in this kit is computed from the input. The next window's hash "
             "is computed from the current one: subtract the leading character's contribution, "
             "multiply by the base, add the trailing character, and reduce. That makes it the "
             "only place where an error can accumulate silently rather than being recomputed "
             "away, so the panel recomputes every window's hash from scratch and requires the "
             "two to agree &mdash; on this text the disagreement count is 0."),
            ("The arithmetic is exact, so the collisions are the same everywhere",
             "The hashes are computed in arbitrary-precision integers, not in machine doubles. "
             "That matters more than it looks on a page whose subject is that two particular "
             "windows collide: if the modulus arithmetic overflowed or rounded, the collision "
               "would be a property of the reader's browser rather than of the text, and the "
               "three offsets printed above would not be checkable by hand. They are, and the "
               "worked example below does check one."),
        ],
        "read_title": "One number per window, rolled forward, and what equality does not prove",
        "read_intro": "The hash, the roll and its correctness, the collisions on this text listed exactly, and the cost of settling them.",
        "body": [
            ("def", ("The window hash",
                     "Fix a base `b` and a modulus `q`. For a string `w` of length `m` the "
                     "<strong>hash</strong> is the value of `w` read as an `m`-digit number in "
                     "base `b`, taken modulo `q`: `H(w) = (w[0] b^(m−1) + w[1] b^(m−2) + ... + "
                     "w[m−1]) mod q`, where each character contributes its code point.")),
            ("thm", ("The roll is correct",
                     "Let `w = t[s..s+m−1]` and `w' = t[s+1..s+m]`. Then "
                     "`H(w') = (b (H(w) − t[s] b^(m−1)) + t[s+m]) mod q`, so each successive "
                     "hash costs a constant number of arithmetic operations once "
                     "`b^(m−1) mod q` is known.")),
            ("proof", ("Write `H(w)` without the reduction as `S = sum over i of "
                       "t[s+i] b^(m−1−i)`. Subtracting `t[s] b^(m−1)` removes the leading "
                       "term, leaving `sum over i &ge; 1 of t[s+i] b^(m−1−i)`.",
                       "Multiplying by `b` raises every remaining exponent by one, giving "
                       "`sum over i &ge; 1 of t[s+i] b^(m−i)`, which is the first `m − 1` terms "
                       "of `w'`'s expansion. Adding `t[s+m] b^0` completes it.",
                       "Reduction modulo `q` commutes with addition and multiplication, so "
                       "performing it at each step gives the same residue as performing it at "
                       "the end. The cost is one multiplication, one subtraction, one addition "
                       "and one reduction, independent of `m`.")),
            ("p", "So the scan is `n` steps of constant arithmetic plus `m` character "
                  "comparisons for each candidate. The panel counts the second part and prints "
                  "it as characters compared verifying, because that is the part whose size "
                  "depends on the text."),
            ("example", ("Seven candidates, four matches, three collisions",
                         "The lab opens on `the rain in spain stays mainly in the plain` and the "
                         "pattern `ain`, at base 256 and modulus 41. The pattern hashes to 36. "
                         "Of the 41 windows, 7 hash to 36. Four are the real occurrences, at "
                         "offsets 5, 14, 25 and 40. The other three are at offsets 33, 36 and "
                         "38, and their characters are the space followed by `th`, then `e` "
                         "space `p`, then `pla`. None of those is `ain` and all of them hash to "
                         "36.")),
            ("p", "The panel prints those three in a table with their hashes beside the "
                  "pattern's, so that a reader can copy one out and check it. The worked example "
                  "below does exactly that for the first of them, in five lines of arithmetic."),
            ("h3", "What the collisions cost, and what the cost does not depend on"),
            ("p", "Each of the 7 candidates costs `m = 3` character comparisons to settle, "
                  "whether it turns out to be a match or not, so the verification bill is 21 "
                  "comparisons. Nine of those &mdash; three collisions at three characters each "
                  "&mdash; produce nothing. The panel reports both numbers, as characters "
                  "compared verifying and wasted on collisions."),
            ("p", "Nothing in the algorithm notices the waste. A collision is indistinguishable "
                  "from a match until the characters are compared, which is why the comparison "
                  "is unconditional and why an implementation that trusted the hash would be "
                  "wrong on this very text, at three offsets, silently."),
            ("h3", "Exact arithmetic, and why it is not a detail here"),
            ("p", "At base 256 a three-character window is a number up to `256^3`, about 16.7 "
                  "million, which fits a double comfortably. At twelve characters it does not, "
                  "and a rounded intermediate would change which windows collide. The kit "
                  "computes every hash in arbitrary-precision integers, so the three offsets "
                  "above are the same three on every machine, and a reader who checks one by "
                  "hand and disagrees has found a bug rather than a rounding difference."),
            ("p", "The same choice is what makes the panel's independent recomputation "
                  "meaningful. Each window's rolled hash is compared with the same window hashed "
                  "from its characters, and the count of disagreements is printed; on this text "
                  "it is 0. If the arithmetic were approximate that check would be comparing two "
                  "approximations and could pass while both were wrong."),
            ("h3", "Where the cost actually goes"),
            ("p", "Rabin&ndash;Karp's attraction is that the scan is arithmetic rather than "
                  "comparison, so the work per window does not depend on `m`. Its exposure is "
                  "that the number of candidates does depend on the modulus, and the modulus is "
                  "a choice. Three collisions on 41 windows is a 7 per cent false-alarm rate on "
                  "this text at this modulus, and the sibling lesson &ldquo;Choosing a Modulus, "
                  "and What the Sweep Says&rdquo; runs the same text at every prime under 200 "
                  "to show what that rate does as the choice moves."),
        ],
        "lab": ("strings", {
            "mode": "rabin",
            "preset": "english",
            "panel_title": "Pick a base and a modulus, and read the collisions off the table",
            "panel_intro": "Every bar is one window and its height is that window's hash, with "
                           "the pattern's value drawn across. The upper table lists every window "
                           "whose hash matched, marked as a real match or a collision, and every "
                           "hash is an arbitrary-precision integer so the collisions are the "
                           "same on every machine.",
        }),
        "steps_title": "Hashing a window, rolling it, and never believing it",
        "steps_intro": "Compute one hash by hand, roll it once, and check a collision. Three short calculations settle what the page is about.",
        "steps": [
            ("Compute the pattern's hash first, and keep it",
             "`ain` is 97, 105, 110 in code points, so at base 256 it is "
             "`97 × 65536 + 105 × 256 + 110 = 6383982`, and `6383982 mod 41 = 36`. Every "
             "comparison on the page is against that one number."),
            ("Roll one window by hand",
             "From the window at offset 0 to the window at offset 1: subtract the leading "
               "character's contribution, multiply by the base, add the new trailing character, "
               "reduce. Doing it once makes it obvious that the cost does not grow with `m`."),
            ("Verify a candidate before recording it",
             "Compare the `m` characters. This is not a defensive extra; the panel's table has "
               "three rows where the hash agreed and the characters did not, and skipping the "
               "comparison would report all three as matches."),
            ("Check a collision by hand, at least once",
             "Take offset 33, the window consisting of a space and `th`, and compute its hash "
               "from its three code points. Getting 36 is the moment the page stops being an "
               "assertion about hashing and becomes a fact about this text."),
        ],
        "worked": {
            "title": "One collision, checked from its characters",
            "intro": [
                "The text is `the rain in spain stays mainly in the plain`, the pattern is "
                "`ain`, the base is 256 and the modulus is 41. Code points: space is 32, `a` is "
                "97, `e` is 101, `h` is 104, `i` is 105, `l` is 108, `n` is 110, `p` is 112, "
                "`t` is 116.",
            ],
            "lines": [
                "the pattern   a i n     97, 105, 110",
                "  97 x 65536 + 105 x 256 + 110            = 6383982",
                "  6383982 mod 41                          = 36",
                "",
                "offset 33     ' t h'    32, 116, 104",
                "  32 x 65536 + 116 x 256 + 104            = 2126952",
                "  2126952 mod 41                          = 36        SAME",
                "  compare characters:  ' ' vs 'a'         FAIL         a collision",
                "",
                "windows                                   = 41",
                "hashes equal to 36                        = 7",
                "real matches   offsets 5, 14, 25, 40      = 4",
                "collisions     offsets 33, 36, 38         = 3",
                "characters compared verifying  7 x 3      = 21",
                "wasted on the collisions       3 x 3      =  9",
                "rolled hashes disagreeing with a fresh one =  0",
            ],
            "after": [
                "Two three-character strings with nothing in common produced the same residue, "
                "and the only reason the algorithm did not report the space and `th` as an "
                "occurrence of `ain` is the comparison on the line below. That line is not an "
                "optimisation guard; it is where the correctness lives.",
                "For a faded rehearsal, check offset 38, whose characters are `pla` &mdash; 112, "
                "108, 97. The supplied first move is the base expansion: "
                "`112 × 65536 + 108 × 256 + 97`. Reduce it modulo 41 and confirm 36, then say "
                "how many of the three collisions you would have caught by comparing only the "
                "first character.",
                "Then change the modulus to 1000003 and count again. The candidates fall from 7 "
                "to 4 and the verification bill from 21 to 12; the matches do not move. Say why "
                "the match count cannot move however the modulus changes, and what that tells "
                "you about which of the two counters is measuring the algorithm and which is "
                "measuring the choice.",
            ],
        },
        "quiz_title": "Hashes, rolls, and what equality establishes",
        "quiz": [
            {"q": "Seven windows hash to 36 and four are matches. What may the algorithm conclude from a hash of 36?",
             "a": ["That the window is an occurrence",
                   "That the window might be an occurrence, and the m characters must be compared to find out",
                   "That the window shares its first character with the pattern",
                   "That the modulus is too small for this text"],
             "c": 1,
             "why": "A hash maps many strings to one residue, so equality is a candidate and "
                    "nothing more. The three collisions here share no character at all with "
                    "`ain` in the same position &mdash; offset 33 begins with a space &mdash; so "
                    "nothing weaker than the full comparison will separate them."},
            {"q": "Why does the lab recompute every window's hash from its characters as well as rolling it?",
             "a": ["To make the page slower and more convincing",
                   "Because the roll is the only value derived from a previous value, so an error there would accumulate silently",
                   "Because rolling is only valid for short patterns",
                   "Because the modulus can change between windows"],
             "c": 1,
             "why": "Everything else on the page is computed from the input and so cannot drift. "
                    "The roll carries a number forward, which is exactly the shape of error that "
                    "no later step would notice, so the page pays for an independent "
                    "recomputation and prints the disagreement count &mdash; 0 on this text."},
            {"q": "What does the roll cost per window, and why?",
             "a": ["m operations, one per character of the window",
                   "A constant number of operations, because the leading term is removed and the trailing one added",
                   "log m operations, by repeated squaring",
                   "One operation, since the modulus makes the arithmetic trivial"],
             "c": 1,
             "why": "Subtract the leading character's contribution, multiply by the base, add the "
                    "trailing character, reduce: four operations regardless of `m`, once "
                    "`b^(m−1) mod q` is precomputed. That independence from `m` is the whole "
                    "point of a rolling hash."},
            {"q": "An implementation drops the character comparison and reports every window whose hash equals the pattern's. What happens on this text?",
             "a": ["Nothing: the hashes are exact, so equality is reliable",
                   "It reports 7 occurrences instead of 4, and nothing in the run signals the error",
                   "It misses matches, because hashing can fail in both directions",
                   "It reports 4, because collisions are rare at base 256"],
             "c": 1,
             "why": "Three of the seven candidates are not occurrences, and the algorithm has no "
                    "other way to tell. It cannot miss a match &mdash; equal strings always hash "
                    "equal &mdash; so the error is one-sided and shows up as extra positions "
                    "that no counter or status line would flag."},
        ],
        "mistakes": [
            ("Calling the verification an optimisation that can be skipped",
             "It is the correctness argument. Without it the algorithm reports 7 positions on "
             "this text, of which 3 are wrong, and the failure is silent because a hash gives no "
             "signal of its own reliability. Every claim the page makes about the method's speed "
             "is a claim about the method with the comparison in it."),
            ("Reading a low collision count as a property of the hash function",
             "Three on 41 windows is a property of this text, this base and this modulus "
             "together. The sibling lesson runs the same text and base at 46 different moduli "
             "and gets collision counts from 0 to 18, which is what it looks like when a number "
             "depends on a choice rather than on the algorithm."),
            ("Assuming a collision must share characters with the pattern",
             "A residue is a residue. Offset 33 is a space followed by `th` and hashes to the "
             "same 36 as `ain`; they agree in no position. Checking only the first character "
             "would separate all three here and would not in general, which is why the "
             "comparison is over all `m`."),
        ],
        "standard": ("Finish when you can hash a window by hand, roll it once, and verify one collision from its code points.",
                     "You should be able to state the hash as a base expansion modulo `q`, prove "
                     "the roll correct, say why its cost is independent of `m`, explain why "
                     "equal hashes are one-sided evidence, compute a collision's residue from "
                     "its characters, and say what the independent recomputation is protecting."),
        "note": ("Three collisions on 41 windows is one modulus's worth of evidence. "
                 "&ldquo;Choosing a Modulus, and What the Sweep Says&rdquo; keeps this text and "
                 "this base and runs every prime under 200, which turns &ldquo;collisions are "
                 "rare&rdquo; into a count &mdash; and shows that the count does not fall as the "
                 "modulus rises."),
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "choosing-a-modulus",
        "title": "Choosing a Modulus, and What the Sweep Says",
        "module": "Hashing, and the verification",
        "one_line": "Zero collisions at one modulus, and 18 of the 46 primes under 200 collide on the very same text — including one larger than several that do not.",
        "summary": (
            "At modulus 1000003 the lab's prose produces no collision at all. That is a "
            "measurement of one choice, and the sweep beside it runs the same text and base at "
            "every prime under 200: 18 of the 46 collide, the largest of them 137, while 11 is "
            "clean. Collisions do not switch off above a threshold. What the analysis actually "
            "gives is an expectation over a randomly chosen modulus, which is a different "
            "statement from a promise about the one you picked."
        ),
        "key": [
            "same text, same base 256, pattern ain:  modulus 1000003 gives 0 collisions",
            "the sweep over the 46 primes under 200:  18 of them collide on this text",
            "the largest that collides is 137;  11 is clean, and so are 19, 31, 43",
            "the worst is modulus 2, with 18 collisions on 41 windows",
            "verification bill falls from 21 characters to 12 when the modulus rises",
            "the bound is an expectation over a random modulus, not a property of one",
        ],
        "key_label": "One clean modulus, and the sweep that refuses to call it a threshold",
        "concepts_intro": (
            "The hard idea is which quantifier the analysis is over. The other two are the "
            "sweep and what a clean run does and does not license."
        ),
        "concepts": [
            ("A clean run is a measurement of one choice",
             "At modulus 1000003 the panel reports 41 windows, 4 candidates, 4 matches, 0 "
             "collisions and a verification bill of 12 characters &mdash; the smallest possible, "
             "since the four real occurrences must be checked. Nothing about that run is "
             "evidence that the modulus was large enough, because the same run at modulus 11, "
             "which is nearly five orders of magnitude smaller, is also clean on this text."),
            ("The sweep turns rare into a number, and the number is not monotone",
             "The lower table runs the identical text and base at every prime modulus from 2 to "
             "199 and reports how many windows collide at each. Eighteen of the forty-six "
             "collide. The collide list is 2, 3, 5, 7, 13, 17, 23, 29, 37, 41, 47, 53, 67, 103, "
             "109, 113, 131 and 137; the clean list begins 11, 19, 31, 43, 59. So 137 collides "
             "and 11 does not, on the same text, which is what it means for the answer to be a "
             "property of the text rather than of the size of the modulus."),
            ("The analysis quantifies over the modulus, not over the text",
             "What can be proved is that for a modulus drawn at random from a suitable range, "
             "the expected number of spurious hits is small &mdash; roughly `n/q` for a "
               "sufficiently large prime `q`. That is a statement about the average over "
               "choices. Fixing the modulus in the source code and then measuring one text "
               "converts it into no statement at all, and an adversary who knows the fixed "
               "modulus can build a text on which every window collides. Randomising the "
               "modulus is what makes the expectation available."),
        ],
        "read_title": "One choice, forty-six choices, and the claim that covers them",
        "read_intro": "The clean run, the sweep, why the collision set is not an interval, and what the expectation is an expectation over.",
        "body": [
            ("p", "Keep the text `the rain in spain stays mainly in the plain`, the pattern "
                  "`ain` and the base 256, and set the modulus to 1000003. The pattern now "
                  "hashes to 383964, four windows hash to that value, all four are occurrences, "
                  "and the panel's collision counter reads 0. The verification bill is 12 "
                  "characters, which is `4 × 3` and cannot be lower."),
            ("p", "That is the good case, and the page does not stop there. The lower table "
                  "keeps this text and this base and replaces the modulus by every prime below "
                  "200 in turn."),
            ("math", [
                "the 46 primes under 200, on this text at base 256",
                "",
                "collide (18)   2   3   5   7  13  17  23  29  37  41  47  53  67",
                "             103 109 113 131 137",
                "clean   (28)  11  19  31  43  59  61  71  73  79  83  89  97 101",
                "             107 127 139 149 151 157 163 167 173 179 181 191 193",
                "             197 199",
                "",
                "worst  modulus   2   with 18 collisions on 41 windows",
                "largest that collides   137",
                "smallest that is clean   11",
            ]),
            ("thm", ("The collision set is not an interval",
                     "There exist a text, a pattern and a base together with two primes "
                     "`q1 &lt; q2` such that the hash collides at `q2` and not at `q1`. So no "
                     "threshold `Q` exists with the property that every modulus above `Q` is "
                     "collision-free for a given input.")),
            ("proof", ("The table above exhibits one: with the text "
                       "`the rain in spain stays mainly in the plain`, the pattern `ain` and "
                       "base 256, the modulus 11 produces no spurious hit and the modulus 137 "
                       "produces three.",
                       "A single instance settles the statement because the claim is existential. "
                       "The reason is that a collision at modulus `q` means `q` divides the "
                       "difference between two particular integers, and divisibility of a fixed "
                       "number is not a monotone property of the divisor: 137 divides one of "
                       "these differences and 11 divides none of them.")),
            ("p", "That proof shape is worth noticing because it is the opposite of the one this "
                  "course usually needs. Here the measurement is the proof: the claim is that "
                  "something exists, and a single exhibited pair establishes it. The claims that "
                  "measurement cannot establish are the universal ones, and the next paragraph "
                  "is about one of those."),
            ("h3", "What is actually proved about Rabin–Karp"),
            ("p", "Fix the text, the pattern and the base. A window collides at modulus `q` "
                  "exactly when `q` divides the difference between that window's value and the "
                  "pattern's. Each of those differences is a fixed integer below `b^m`, so it "
                  "has at most `m log b / log q` prime divisors above `q`, and choosing `q` at "
                  "random from a range of size `R` makes the chance that it divides any of the "
                  "`n` differences at most a bound of the form `n m log b / (R log R)`. That is "
                  "the theorem, and its subject is the random choice."),
            ("p", "Read what it does not say. It does not say that a particular large prime is "
                  "safe on a particular text &mdash; 137 is not, here. It does not say the "
                  "collision count falls as the modulus rises &mdash; the table shows 41 and 47 "
                  "colliding while 43 does not. And it says nothing at all if the modulus is a "
                  "constant in the source, because then there is no random choice to average "
                  "over and an adversary can construct a text against it."),
            ("h3", "The cost of a collision, and why a small modulus is not merely inelegant"),
            ("p", "Each candidate costs `m` character comparisons to settle. At modulus 41 this "
                  "text produces 7 candidates and a bill of 21 characters, of which 9 are "
                  "wasted; at 1000003 it produces 4 and a bill of 12, with nothing wasted; at "
                  "modulus 2 it produces 22 candidates, of which 18 are collisions. In the worst "
                  "direction the verification dominates and the algorithm degenerates towards "
                  "comparing every window in full, which is the naive matcher with extra "
                  "arithmetic."),
            ("p", "So the modulus is not a tuning detail. It decides how much of the algorithm's "
                  "advertised advantage &mdash; constant work per window &mdash; survives "
                  "contact with the input, and the only defensible way to choose it is at random "
                  "from a large range, because that is the one choice the theorem covers."),
            ("h3", "The same sweep on a different text"),
            ("p", "Switch the preset to the binary one, where the alphabet is two characters and "
                  "the base is 2, and the sweep reports 6 of the 46 primes colliding rather than "
                  "18. Switch to the repetitive `abracadabra` text at base 256 and it reports "
                  "15. The number is a property of the input triple and moves by a factor of "
                  "three between presets, which is a third way of making the same point: it is "
                  "not a constant of the method."),
        ],
        "lab": ("strings", {
            "mode": "rabin",
            "preset": "clean",
            "panel_title": "A modulus with no collisions, and the sweep that follows it",
            "panel_intro": "The upper table is empty here because no window hashes to the "
                           "pattern's value except the four real occurrences. The lower table is "
                           "the same text and base at every prime modulus under 200, so the "
                           "clean run above can be read against the 46 alternatives rather than "
                           "on its own.",
        }),
        "steps_title": "Choosing a modulus, and reading the sweep instead of one row",
        "steps_intro": "A clean run is one row of the table. Read the column it sits in before drawing anything from it.",
        "steps": [
            ("Read the collision counter and then the sweep, in that order",
             "0 collisions is the row. 18 of 46 is the column. A page that prints only the row "
             "has shown a measurement; the column is what says whether the row was luck."),
            ("Look for a counterexample to monotonicity before assuming a threshold",
             "Scan the clean list for a value smaller than something in the collide list. Here 11 "
             "is clean and 137 collides, which settles it: there is no size above which this "
             "input stops colliding."),
            ("Price the collisions in character comparisons, not in embarrassment",
             "Each candidate costs `m`. Going from 4 candidates to 22 takes the verification "
             "bill from 12 characters to 66 on a 43-character text, at which point the "
             "arithmetic saving has been spent."),
            ("Randomise the choice if you want the theorem to apply",
             "The bound is an expectation over the modulus. A constant in the source code has no "
             "expectation attached and can be attacked; a modulus drawn at random from a large "
             "range is the object the proof is about."),
        ],
        "worked": {
            "title": "The clean row, and the column it sits in",
            "intro": [
                "The text is `the rain in spain stays mainly in the plain`, the pattern is "
                "`ain`, the base is 256. The pattern's unreduced value is 6383982 and every "
                "row below is that number and the window values reduced by a different modulus.",
            ],
            "lines": [
                "modulus 1000003    6383982 mod 1000003            = 383964",
                "  windows 41   candidates 4   matches 4   collisions 0",
                "  characters compared verifying  4 x 3            = 12",
                "",
                "modulus 41         6383982 mod 41                 = 36",
                "  windows 41   candidates 7   matches 4   collisions 3",
                "  characters compared verifying  7 x 3            = 21   (9 wasted)",
                "",
                "modulus 11         clean                          collisions 0",
                "modulus 137        collides                       collisions 3",
                "  11 < 137, and the smaller one is the clean one",
                "",
                "the sweep, 46 primes under 200:",
                "  collide   18      clean   28",
                "  worst     modulus 2, 18 collisions",
                "  largest colliding    137",
                "  smallest clean        11",
            ],
            "after": [
                "The middle block is the whole lesson in four numbers. Eleven is clean and a "
                "hundred and thirty-seven is not, so any sentence beginning &ldquo;a modulus "
                "large enough to&rdquo; has to be finished with something other than a size.",
                "For a faded rehearsal, work out why modulus 2 is the worst. The supplied first "
                "move: at base 256 every character's contribution is even except when its code "
                "point is odd, so the hash modulo 2 is the parity of the last character's code "
                "point alone. Say how many of the 41 windows that puts in the candidate set, and "
                "then say what the verification bill becomes.",
                "Then switch the preset to the binary text and read the sweep again. It reports "
                "6 of 46 rather than 18. Before deciding that a small alphabet is safer, say "
                "what the base is in that preset and how many windows there are, and then say "
                "which of the three changes you would need to hold fixed to make the comparison "
                "mean anything.",
            ],
        },
        "quiz_title": "One modulus, forty-six moduli, and the quantifier",
        "quiz": [
            {"q": "At modulus 1000003 this text produces no collisions. What follows?",
             "a": ["That a modulus of that size is collision-free",
                   "That on this text, base and pattern that modulus produced none, which the sweep shows is also true of 11",
                   "That collisions become impossible above about a million",
                   "That the algorithm no longer needs to verify candidates"],
             "c": 1,
             "why": "It is one row. The sweep in the same panel shows 11 clean and 137 "
                    "colliding on the identical input, so size is not what decided it. "
                    "Verification is still required: the algorithm cannot know in advance that "
                    "this run will be clean."},
            {"q": "The sweep shows 137 colliding while 11 does not. Why is that not a measurement error?",
             "a": ["It is one; the sweep should be monotone",
                   "Because a collision means the modulus divides a fixed difference, and divisibility is not monotone in the divisor",
                   "Because 137 is not prime",
                   "Because the two runs use different bases"],
             "c": 1,
             "why": "Fix the text, pattern and base and each window gives a fixed integer "
                    "difference from the pattern. A modulus collides exactly when it divides one "
                    "of those, and whether a given number divides a fixed integer has nothing to "
                    "do with how large it is. The whole sweep is run at the same base."},
            {"q": "What does the analysis of Rabin–Karp actually bound?",
             "a": ["The number of collisions on any text at a sufficiently large modulus",
                   "The expected number of spurious hits when the modulus is chosen at random from a large range",
                   "The number of character comparisons, at m per window",
                   "The number of windows, which is n − m + 1"],
             "c": 1,
             "why": "The quantifier is over the random choice of modulus, not over texts. That "
                    "is why a fixed modulus in source code has no guarantee attached and can be "
                    "attacked by a constructed text, and why the honest implementation draws the "
                    "modulus at random."},
            {"q": "Going from 4 candidates to 22 on this 43-character text does what to the verification cost?",
             "a": ["Nothing, since verification is constant per window",
                   "Takes it from 12 character comparisons to 66, at m = 3 per candidate",
                   "Takes it from 12 to 22, one per candidate",
                   "Takes it from 4 to 22 windows"],
             "c": 1,
             "why": "Each candidate costs the full `m` characters to settle, so the bill is "
                    "`3 × 22 = 66` against a text of 43 characters. At that point the algorithm "
                    "is doing more character comparisons than the naive matcher would on "
                    "ordinary prose, plus all the arithmetic."},
        ],
        "mistakes": [
            ("Treating the modulus as a threshold to exceed",
             "The clean and colliding sets interleave: 41 and 47 collide, 43 does not; 137 "
             "collides, 11 does not. Choosing a modulus by size is choosing by a quantity that "
             "the outcome does not depend on, and the sweep is printed on the page precisely so "
             "that the interleaving is visible rather than argued about."),
            ("Reading the expectation as a bound on the input you have",
             "`n/q` is an average over moduli drawn at random. With the modulus fixed there is "
             "nothing left to average over, and the actual collision count on a given text is "
             "whatever the divisibility happens to be &mdash; three at modulus 41 here, and "
             "eighteen at modulus 2."),
            ("Comparing collision counts across presets without holding the base fixed",
             "The binary preset collides at 6 of 46 rather than 18, and it also has base 2 "
             "rather than 256, a different pattern length and a different number of windows. "
             "Four things changed; attributing the difference to the alphabet is picking one of "
             "them for no reason the page supplies."),
        ],
        "standard": ("Finish when you can read a clean run as one row of a sweep and name the quantifier the bound is over.",
                     "You should be able to state what a collision at modulus `q` means "
                     "arithmetically, exhibit a smaller clean modulus beside a larger colliding "
                     "one, explain why that rules out a threshold, price candidates in character "
                     "comparisons, and say why the modulus must be drawn at random for the "
                     "expectation to apply."),
        "note": ("That closes the single-pattern matchers. The last module changes the question: "
                 "&ldquo;One Pass for Every Word&rdquo; searches for a whole dictionary in one "
                 "scan rather than one pattern at a time, and &ldquo;The Suffix Array, and What "
                 "a Sorted Order Answers&rdquo; preprocesses the TEXT instead of the pattern, "
                 "which is the only way to answer questions about a text nobody has asked yet."),
    },
    # ---------------------------------------------------------------- 11
    {
        "slug": "one-pass-for-every-word",
        "title": "One Pass for Every Word",
        "module": "Many patterns, and the text itself",
        "one_line": "Store a dictionary as a trie, add a failure link to every node, and find every occurrence of every word in one scan of the text.",
        "summary": (
            "Four words sharing three character positions become a ten-node trie holding each "
            "shared prefix once. Adding failure links turns it into an Aho&ndash;Corasick "
            "automaton, and one pass over a 22-character text reports all 9 occurrences of all "
            "four words for 31 comparisons, where four separate KMP passes cost 98. The output "
            "links chain SUFFIXES, not prefixes, which decides which words get reported "
            "together and which never do."
        ),
        "key": [
            "a trie node is a distinct prefix; he, she, his, hers is 10 nodes for 12 characters",
            "held as an array per node it is 10 × sigma = 50 cells; as maps, 10 entries",
            "prefix query h: he, hers, his — the same three as filtering the list",
            "one Aho-Corasick pass: 9 occurrences, 31 comparisons over 22 characters",
            "four separate KMP passes on the same text: 98 comparisons",
            "output links chain suffixes: position 3 reports she AND he, and nothing else does",
        ],
        "key_label": "One structure for a dictionary, and one scan for all of it",
        "concepts_intro": (
            "The hard idea is the output link, and it chains suffixes rather than prefixes. The "
            "other two are what a trie costs and what one pass buys."
        ),
        "concepts": [
            ("A trie node is a distinct prefix, so sharing is stored once",
             "The words `he, she, his, hers` have 12 characters between them and the trie has 10 "
             "nodes: a root, then `h`, `he`, `her`, `hers`, `hi`, `his`, `s`, `sh`, `she`. The "
             "count is one per distinct prefix plus the root, so `he` being a prefix of `hers` "
             "costs nothing extra. The panel prints the saving as a number &mdash; 3 shared "
             "character positions &mdash; rather than as an adjective, and on a dictionary with "
             "no shared prefixes at all it prints 0 and says the trie is separate chains."),
            ("Space is two numbers, not one",
             "Holding each node's children in an array indexed by character costs sigma cells "
             "per node, whether or not they are used: 10 nodes at sigma 5 is 50 cells. Holding "
             "them in a map costs one entry per edge that exists, which is 9. The panel prints "
             "both, because the choice between them is the whole space question for a trie and "
             "the answer depends on how dense the alphabet is."),
            ("An output link follows suffixes, and that is why some words report together",
             "The failure link of a node points to the longest proper suffix of its string that "
             "is also a node, and the outputs at a node are its own word plus the words reachable "
             "by following failure links. So two words are reported at the same position exactly "
             "when one is a suffix of the other: `he` is a suffix of `she`, so position 3 of "
             "`ushers` reports both. Prefix nesting does nothing of the kind &mdash; with the "
               "dictionary `a, ab, abc, abcd` no position ever reports more than one word, "
               "because none of them is a suffix of another."),
        ],
        "read_title": "A trie, its failure links, and one scan for a whole dictionary",
        "read_intro": "The structure and its cost, the prefix query, the automaton, and the suffix relation that decides what is reported together.",
        "body": [
            ("def", ("Trie",
                     "A <strong>trie</strong> over a set of words is a rooted tree whose edges "
                     "carry characters, such that the path from the root to a node spells a "
                     "distinct prefix of at least one word, and every distinct prefix appears as "
                     "exactly one node. A node is marked as a word end if the prefix it spells "
                     "is one of the words. The number of nodes is one plus the number of "
                     "distinct non-empty prefixes.")),
            ("example", ("Ten nodes for twelve characters",
                         "The dictionary is `he, she, his, hers`. Its distinct non-empty "
                         "prefixes are `h`, `he`, `her`, `hers`, `hi`, `his`, `s`, `sh` and "
                         "`she` &mdash; nine of them &mdash; so the trie has 10 nodes. The four "
                         "words total 12 characters, and a list of separate strings would store "
                         "all 12; the trie stores 9 edges, saving the 3 positions where `he` and "
                         "`hers` overlap and where `h` leads to both `he` and `his`.")),
            ("p", "Held with one array of sigma slots per node that is `10 × 5 = 50` cells, since "
                  "the dictionary uses the five characters `e, h, i, r, s`. Held with a map per "
                  "node it is 9 entries. The panel prints 50 and 10 side by side so the trade is "
                  "a pair of numbers rather than a preference."),
            ("p", "A prefix query walks down from the root and then collects every word-end "
                  "below. Asking for `h` returns `he`, `hers` and `his`, and the panel checks "
                  "that against filtering the word list with a string comparison &mdash; the "
                  "definition of the query, computed a second way."),
            ("def", ("Failure and output links",
                     "In a trie over a dictionary, the <strong>failure link</strong> of a node "
                     "`v` points to the node spelling the longest proper suffix of `v`'s string "
                     "that is itself a node of the trie, or to the root if there is none. The "
                     "<strong>outputs</strong> of `v` are `v`'s own word, if it ends one, "
                     "together with the outputs of `v`'s failure link. The links are computed by "
                     "a breadth-first traversal, so a node's link is set after every shorter "
                     "node's.")),
            ("thm", ("One pass reports every occurrence of every word",
                     "Feed the text one character at a time, following the child edge when it "
                     "exists and otherwise following failure links until a child exists or the "
                     "root is reached. After reading `t[0..i]` the current node spells the "
                     "longest suffix of `t[0..i]` that is a node of the trie, and its outputs "
                     "are exactly the dictionary words ending at position `i`.")),
            ("proof", ("By induction on `i`, exactly as for the single-pattern automaton. "
                       "Before anything is read the current node is the root, spelling the "
                       "empty string, which is the longest suffix of the empty text that is a "
                       "node.",
                       "Suppose the current node spells `u`, the longest suffix of `t[0..i−1]` "
                       "that is a node. A node spelling a suffix of `t[0..i]` of length at least "
                       "1 consists of a suffix of `t[0..i−1]` followed by `t[i]`, and that "
                       "suffix must itself be a node because every prefix of a node is a node. "
                       "So the candidates are the nodes `w` followed by `t[i]` for `w` a suffix "
                       "of `u` that is a node &mdash; which is precisely the failure-link chain "
                       "from `u` &mdash; and the walk takes the longest.",
                       "A word ends at `i` exactly when it is a suffix of `t[0..i]`, hence a "
                       "suffix of the current node's string, hence on the failure chain from it. "
                       "The outputs are defined as that chain's word ends, so they are exactly "
                       "the words ending at `i`.")),
            ("p", "The final sentence of that proof is the operative one and it is easy to read "
                  "past: the words reported together at a position are the ones related by "
                  "SUFFIX. Not prefix. That distinction is what the lab's last table is for."),
            ("h3", "One pass against four passes, in comparisons"),
            ("p", "On the text `ushers hers his she he`, 22 characters, one pass reports 9 "
                  "occurrences for 31 comparisons. The four separate KMP passes cost 23, 25, 26 "
                  "and 24, which is 98 in total &mdash; a factor of more than three. The "
                  "occurrences are `he` at 2, 7, 17 and 20; `she` at 1 and 16; `his` at 12; and "
                  "`hers` at 2 and 7."),
            ("p", "The saving is not that the automaton is cleverer per character; it is that "
                  "there is one scan rather than four. Each separate pass reads all 22 "
                  "characters, so four of them read 88 characters where one reads 22, and that "
                  "ratio is where the factor of three comes from. With ten words it would be a "
                  "factor of nearer ten, which is the reason the structure exists."),
            ("h3", "Which words are reported at the same position"),
            ("p", "At the end of `ushe` &mdash; text position 3 &mdash; the automaton reports "
                  "both `she` and `he`, because `he` is a suffix of `she` and so sits on its "
                  "failure chain. Position 18 does the same. No other position on this text "
                  "reports two words, and the panel's per-word table is checked against scanning "
                  "the text separately for each one."),
            ("p", "Now take the dictionary `a, ab, abc, abcd`, where every word is a prefix of "
                  "the next, and scan `abcdabcab`. The words end at positions 0, 1, 2 and 3 "
                  "respectively for the first occurrence, and at no position does the automaton "
                  "report more than one &mdash; because none of `bcd`, `cd`, `d` is a word, so "
                  "no failure chain from `abcd` reaches another word end. Prefix nesting is "
                  "invisible to the output links; only suffix nesting is not."),
            ("p", "That is the one property of this structure most likely to be misremembered, "
                  "and it is checkable in two clicks: the classic dictionary reports two words "
                  "at one position and the nested one never reports two at all, although the "
                  "nested one is the one that looks as though it should."),
        ],
        "lab": ("strings", {
            "mode": "trie",
            "preset": "classic",
            "panel_title": "Type a dictionary, a prefix, and a text to scan for all of it at once",
            "panel_intro": "The trie is drawn from the words you type, with each word-ending node "
                           "marked. The prefix query is checked against filtering the list, and "
                           "the single pass is checked word by word against scanning the text "
                           "separately for each one &mdash; the check that catches a failure "
                           "link pointing at the wrong node.",
        }),
        "steps_title": "Building the trie, then the links, then reading the outputs",
        "steps_intro": "Count the nodes before drawing them, and work the failure links out in order of length.",
        "steps": [
            ("Count nodes as distinct prefixes, not as characters",
             "List every distinct non-empty prefix of every word and add one for the root. For "
             "`he, she, his, hers` that is nine plus one. If the count equals the character "
             "total plus one, the words share nothing."),
            ("Set the failure links shortest first",
             "A node's link points to the longest proper suffix of its string that is also a "
             "node, and finding it uses the links of shorter nodes, so a breadth-first order is "
             "not a convenience but a requirement."),
            ("Read the outputs as a chain, and ask which words are suffixes",
             "The outputs at a node are its own word plus everything on its failure chain. Two "
             "words appear together exactly when one is a suffix of the other, so scan the "
             "dictionary for suffix relations before predicting what the scan will report."),
            ("Price one pass against k passes in the same unit",
             "One scan reads the text once; `k` scans read it `k` times. The panel prints the "
             "comparison totals for both &mdash; 31 against 98 here &mdash; so the claim is a "
             "ratio rather than an argument about asymptotics."),
        ],
        "worked": {
            "title": "Ten nodes, four failure links that matter, and nine occurrences",
            "intro": [
                "The dictionary is `he, she, his, hers` and the text is `ushers hers his she "
                "he`, 22 characters. Positions are counted from 0.",
            ],
            "lines": [
                "distinct prefixes   h  he  her  hers  hi  his  s  sh  she     = 9",
                "nodes  9 + root                                               = 10",
                "characters in the words  2 + 3 + 3 + 4                        = 12",
                "shared positions  12 + 1 - 10                                 = 3",
                "array slots  10 nodes x sigma 5                               = 50",
                "map entries  one per edge                                     = 9",
                "",
                "failure links that are not the root:",
                "  she -> he      'he' is the longest suffix of 'she' that is a node",
                "  sh  -> h       'h' is a node",
                "  outputs at 'she' = { she, he }",
                "",
                "prefix h      he, hers, his        by filtering the list: the same 3",
                "",
                "occurrences, one pass:",
                "  he    at 2, 7, 17, 20        she  at 1, 16",
                "  his   at 12                  hers at 2, 7",
                "  total                                                       = 9",
                "  comparisons, one pass                                       = 31",
                "  comparisons, four separate KMP passes  23+25+26+24          = 98",
                "",
                "positions reporting two words   3 and 18   ( she and he )",
            ],
            "after": [
                "The failure link from `she` to `he` is the whole mechanism. Without it the "
                "automaton would report `she` at position 3 and miss the `he` that ends there, "
                "because the scan is at the node for `she` and never visits the node for `he`. "
                "With it, the outputs at `she` include everything on its chain, and the 9 "
                "occurrences come out right.",
                "For a faded rehearsal, switch the dictionary to `a, ab, abc, abcd` and the text "
                "to `abcdabcab`. The supplied first move: the trie is a single chain of five "
                "nodes, and every failure link points to the root, because no proper suffix of "
                "`abcd` other than the empty string is a node. Predict how many positions report "
                "two words &mdash; and then check it, because the answer is not what the shape "
                "of the dictionary suggests.",
                "Then try `he, she, his, hers` again with the text `sher`. Two words ought to be "
                "reported and one of them is not the one a left-to-right reading suggests. Give "
                "the positions and the words before running it, and say which failure link you "
                "used.",
            ],
        },
        "quiz_title": "Nodes, links, and what reports together",
        "quiz": [
            {"q": "The dictionary is `a, ab, abc, abcd` and the text is `abcdabcab`. How many positions report more than one word?",
             "a": ["Every position that ends abcd, since abc, ab and a end there too",
                   "None: the words are prefixes of each other, and output links chain suffixes",
                   "One, at the end of abcd",
                   "Three, one for each shorter word"],
             "c": 1,
             "why": "Output links follow the failure chain, which walks SUFFIXES. The proper "
                    "suffixes of `abcd` are `bcd`, `cd` and `d`, none of which is a word, so "
                    "nothing joins `abcd`'s output. `a` ends at position 0, `ab` at 1, `abc` at "
                    "2 and `abcd` at 3 &mdash; four different positions, one word each."},
            {"q": "Why does position 3 of `ushers` report both `she` and `he`?",
             "a": ["Because he is a prefix of she",
                   "Because he is a suffix of she, so it lies on she's failure chain",
                   "Because the automaton backtracks after reporting she",
                   "Because both words are in the dictionary"],
             "c": 1,
             "why": "`he` is the longest proper suffix of `she` that is a node, so the failure "
                    "link from `she` points at it and `she`'s outputs include it. Prefix "
                    "relations do nothing here, and the automaton never backtracks: it is at one "
                    "node and reads that node's precomputed output list."},
            {"q": "The trie for `he, she, his, hers` has 10 nodes and the words have 12 characters. What does 10 count?",
             "a": ["The characters, minus the ones that repeat anywhere in the dictionary",
                   "The distinct non-empty prefixes of the words, plus the root",
                   "The words, plus their shared prefixes",
                   "The edges of the tree"],
             "c": 1,
             "why": "One node per distinct prefix: `h, he, her, hers, hi, his, s, sh, she` is "
                    "nine, and the root makes ten. The edges number nine, one fewer, which is "
                    "the map-entry count the panel prints beside the 50 array slots."},
            {"q": "One pass costs 31 comparisons and four separate KMP passes cost 98. Where does the factor of three come from?",
             "a": ["The automaton compares fewer characters per position",
                   "One scan reads the 22-character text once where four scans read it four times",
                   "The trie stores the shared prefixes once",
                   "KMP is slower than Aho–Corasick per character"],
             "c": 1,
             "why": "The saving is the number of passes over the text, not the work per "
                    "character: four scans of 22 characters is 88 character positions visited "
                    "against 22. The prefix sharing saves space in the structure and is a "
                    "separate benefit; with ten words the ratio would be nearer ten."},
        ],
        "mistakes": [
            ("Expecting nested prefixes to report together",
             "With `a, ab, abc, abcd` no position ever reports two words, although every "
             "occurrence of `abcd` contains occurrences of the other three &mdash; they simply "
             "end at earlier positions. The output chain follows suffixes, so the dictionary "
             "that reports together is one like `he, she`, where the shorter word is the tail of "
             "the longer."),
            ("Setting failure links in any convenient order",
             "A node's link is found using the links of strictly shorter nodes, so computing "
               "them depth-first or in insertion order reads links that have not been set. The "
               "breadth-first order is part of the construction, and the symptom of getting it "
               "wrong is lost occurrences of one word while every other word still reports "
               "correctly &mdash; which is what the lab's per-word table is checking."),
            ("Quoting one space figure for a trie",
             "10 nodes and 50 array slots are both true and they describe different "
             "implementations. Which one to quote depends on whether the children are held in a "
             "map or an array indexed by character, and on a large alphabet the two differ by "
             "orders of magnitude &mdash; the panel prints both for that reason."),
        ],
        "standard": ("Finish when you can build the trie and its links for a dictionary you have not seen and predict which positions report two words.",
                     "You should be able to count nodes as distinct prefixes, give both space "
                     "figures, compute a failure link as a longest-suffix node, explain why the "
                     "links must be set shortest first, prove that the outputs at a position are "
                     "the words ending there, and say why suffix nesting and prefix nesting "
                     "behave completely differently."),
        "note": ("Everything up to here preprocesses the PATTERN, or the patterns, and then reads "
                 "the text once. &ldquo;The Suffix Array, and What a Sorted Order Answers&rdquo; "
                 "turns that round: it preprocesses the text, which is the only way to answer a "
                 "question about the text that nobody has asked yet &mdash; what its longest "
                 "repeated substring is, or how many distinct substrings it has."),
    },
    # ---------------------------------------------------------------- 12
    {
        "slug": "the-suffix-array-and-what-it-answers",
        "title": "The Suffix Array, and What a Sorted Order Answers",
        "module": "Many patterns, and the text itself",
        "one_line": "Sort every suffix of the text, record how much each shares with the one above it, and read the longest repeat and the exact number of distinct substrings off the result.",
        "summary": (
            "The suffix array of `banana` is 5, 3, 1, 0, 4, 2 and prefix doubling reaches it in "
            "two rounds. Beside it the LCP array &mdash; 0, 1, 3, 0, 0, 2 &mdash; turns the "
            "order into answers: its largest entry is the longest repeated substring, `ana`, "
            "and subtracting its sum from 21 gives the exact number of distinct substrings, 15. "
            "Both arrays are checked against the definitions, which are quadratic and obvious."
        ),
        "key": [
            "banana:  sa = 5, 3, 1, 0, 4, 2     a, ana, anana, banana, na, nana",
            "prefix doubling: sort by 1 character, then use those ranks to sort by 2, 4, 8",
            "two rounds on six characters, 21 comparisons, checked against sorting the strings",
            "lcp = 0, 1, 3, 0, 0, 2   overlap with the suffix one rank above",
            "longest repeated substring = the largest LCP entry = ana, of length 3",
            "distinct substrings = n(n + 1)/2 − sum of lcp = 21 − 6 = 15",
        ],
        "key_label": "One sorted order, and the two questions it answers exactly",
        "concepts_intro": (
            "The hard idea is that sorted order puts every repeat next to itself. The other two "
            "are prefix doubling and the counting identity."
        ),
        "concepts": [
            ("Sorting the suffixes puts every repeated substring beside itself",
             "A substring that occurs twice is a common prefix of two suffixes, and in sorted "
               "order those two suffixes are adjacent or separated only by suffixes that also "
               "share that prefix. So the longest repeated substring is the largest overlap "
               "between two NEIGHBOURS in the sorted order, and nothing further apart needs "
               "checking. On `banana` the neighbours `ana` and `anana` share `ana`, which is the "
               "answer, and it sits in the LCP array as its largest entry."),
            ("Prefix doubling sorts by ranks rather than by strings",
             "Round one sorts the starting positions by their first character. Round `r` then "
               "sorts by the pair of ranks from round `r − 1` at distance `2^(r−1)`, which "
               "orders the suffixes correctly to `2^r` characters while comparing two small "
               "integers rather than two strings. The order is correct once every rank is "
               "distinct, so `log2 n` rounds suffice: `banana` needs 2, `mississippi` needs 3. "
               "The panel prints each round's order and checks the final answer against sorting "
               "the suffixes as whole strings, which is the definition and is quadratic."),
            ("The LCP array makes the order answer questions, exactly",
             "There are `n(n + 1)/2` substrings counted with repeats &mdash; 21 for a text of 6. "
               "Each LCP entry counts the prefixes this suffix shares with the one above, and "
               "those contribute no new substring, so the distinct count is `n(n + 1)/2` minus "
               "the sum of the LCP array: `21 − 6 = 15` on `banana`. The two extremes are worth "
               "holding: `abcdefgh` has every LCP zero and all 36 of its substrings distinct, "
               "and `aaaaaaaa` has LCP sum 28 and only 8."),
        ],
        "read_title": "Every suffix in order, and the two arrays that follow",
        "read_intro": "The definitions, the doubling construction, the theorem that makes neighbours enough, and the counting identity.",
        "body": [
            ("def", ("Suffix array and LCP array",
                     "For a text `s` of length `n`, the <strong>suffix array</strong> `sa` is "
                     "the permutation of `0, 1, ..., n − 1` that lists the starting positions of "
                     "the suffixes of `s` in increasing lexicographic order of the suffixes. The "
                     "<strong>LCP array</strong> has `lcp[0] = 0` and, for `r &ge; 1`, "
                     "`lcp[r]` equal to the length of the longest common prefix of the suffixes "
                     "at ranks `r − 1` and `r`.")),
            ("example", ("The six suffixes of banana",
                         "In lexicographic order they are `a`, `ana`, `anana`, `banana`, `na` "
                         "and `nana`, starting at 5, 3, 1, 0, 4 and 2. So `sa` is 5, 3, 1, 0, 4, "
                         "2. The overlaps between consecutive pairs are 0, then `a` between `a` "
                         "and `ana`, then `ana` between `ana` and `anana`, then 0 between "
                         "`anana` and `banana`, then 0 between `banana` and `na`, then `na` "
                         "between `na` and `nana`. So `lcp` is 0, 1, 3, 0, 0, 2.")),
            ("thm", ("The longest repeated substring is the largest LCP entry",
                     "A string `w` occurs at two or more distinct positions of `s` if and only if "
                     "some entry of the LCP array is at least the length of `w`. Consequently "
                     "the longest repeated substring of `s` has length equal to the maximum "
                     "entry of the LCP array.")),
            ("proof", ("Suppose `w` occurs at positions `i` and `j` with `i` not equal to `j`. "
                       "Then `w` is a prefix of both the suffix at `i` and the suffix at `j`. "
                       "Every suffix lying between them in sorted order also has `w` as a "
                       "prefix, because lexicographic order places all strings beginning with "
                       "`w` contiguously. So two ADJACENT suffixes in that block share `w`, and "
                       "their LCP entry is at least the length of `w`.",
                       "Conversely if `lcp[r]` is at least the length of `w` and `w` is the "
                       "prefix of that length, then `w` prefixes the suffixes at ranks `r − 1` "
                       "and `r`, which start at two distinct positions, so `w` occurs twice.",
                       "Taking `w` as long as possible in each direction gives the equality of "
                       "lengths. On `banana` the maximum entry is 3, at rank 2, and the "
                       "substring is `ana`.")),
            ("p", "The force of that theorem is the word ADJACENT. Without it, finding the "
                  "longest repeat would mean comparing every pair of suffixes; with it, `n − 1` "
                  "neighbour comparisons suffice, and the LCP array has already done them."),
            ("thm", ("The number of distinct substrings",
                     "The number of distinct non-empty substrings of `s` is "
                     "`n(n + 1)/2` minus the sum of the LCP array.")),
            ("proof", ("Count by the rank of the suffix each substring is first attributed to. "
                       "The suffix at rank `r`, starting at `sa[r]`, has `n − sa[r]` non-empty "
                       "prefixes, and each substring of `s` is a prefix of at least one suffix.",
                       "Attribute a substring to the LOWEST rank whose suffix has it as a "
                       "prefix. The prefixes of the rank-`r` suffix already attributed to an "
                       "earlier rank are exactly its prefixes shared with the rank-`r − 1` "
                       "suffix, of which there are `lcp[r]`, because sorted order makes the "
                       "previous suffix the one sharing most with it.",
                       "So rank `r` contributes `n − sa[r] − lcp[r]` new substrings. Summing "
                       "over `r` gives `sum(n − sa[r]) − sum(lcp[r])`, and the first sum is "
                       "`n^2 − (0 + 1 + ... + n − 1) = n(n + 1)/2`.")),
            ("p", "On `banana` that is `1 + 2 + 2 + 6 + 2 + 2 = 15`, and `21 − 6 = 15` as well. "
                  "The panel prints both routes and they are the same integer, which is the "
                  "check that the identity was used rather than believed."),
            ("h3", "Two doubling rounds, watched"),
            ("p", "Round one sorts the six positions by their first character, giving 5, 1, 3, "
                  "0, 2, 4 &mdash; the three positions starting `a` first, then `b`, then the "
                  "two starting `n`, each group in whatever order the ranks left them. Round two "
                  "sorts by pairs of round-one ranks at distance 1, which is enough to separate "
                  "every suffix, and produces 5, 3, 1, 0, 4, 2. Two rounds, 21 comparisons, and "
                  "the result agrees with sorting the six suffixes as whole strings."),
            ("math", [
                "text           n     rounds   comparisons   longest repeat   distinct / all",
                "banana         6        2          21        ana      (3)       15 / 21",
                "mississippi   11        3          66        issi     (4)       53 / 66",
                "abracadabra   11        3          70        abra     (4)       54 / 66",
                "abcdefgh       8        1           7        none     (0)       36 / 36",
                "aaaaaaaa       8        3          37        aaaaaaa  (7)        8 / 36",
            ]),
            ("p", "The last two rows are the extremes of the counting identity. With every "
                  "character distinct the LCP array is all zeros and every one of the 36 "
                  "substrings is distinct; with one character repeated the LCP array is the "
                  "staircase 0, 1, 2, ..., 7 summing to 28, and `36 − 28 = 8`, which is `n` "
                  "&mdash; the only distinct substrings are the runs of length 1 to 8."),
            ("p", "The round column is the one to read against a bound. `log2 n` is about 2.6 "
                  "for `banana` and about 3.5 for `mississippi`, and the measured rounds are 2 "
                  "and 3: the construction stops as soon as every rank is distinct, which can be "
                  "sooner than the ceiling. `abcdefgh` needs one round, because a single "
                  "character already separates all eight suffixes."),
            ("h3", "What is checked against what"),
            ("p", "The suffix array is checked against sorting the suffixes as whole strings with "
                  "string comparison, which is the definition and costs `O(n^2 log n)`. The LCP "
                  "array is checked against comparing each adjacent pair character by character, "
                  "which is the definition and costs `O(n^2)`. The fast constructions &mdash; "
                  "prefix doubling and Kasai's one pass &mdash; are the ones whose correctness is "
                  "not obvious, and they are the ones being checked."),
            ("p", "Kasai's pass deserves the scrutiny in particular, because its whole idea is "
                  "that the LCP of a suffix can be computed from the LCP of the suffix one "
                  "position earlier in the TEXT, which loses at most one character. That is an "
                  "argument about a quantity carried between iterations, and a carried quantity "
                  "is the shape of error that no later step corrects &mdash; the same reason the "
                  "rolling hash on an earlier page is recomputed from scratch."),
        ],
        "lab": ("strings", {
            "mode": "suffix",
            "preset": "banana",
            "panel_title": "Type a text and sort every suffix of it",
            "panel_intro": "The upper table is one row per doubling round, showing the order and "
                           "the rank of each starting position; the lower one is the finished "
                           "suffix array with the same array produced by sorting the suffixes as "
                           "whole strings beside it. The bar chart is the LCP array, and its "
                           "tallest bar is the longest repeated substring.",
        }),
        "steps_title": "Sorting the suffixes, then reading the answers off",
        "steps_intro": "Write the suffixes out and sort them by hand once. Everything after that is arithmetic on two arrays.",
        "steps": [
            ("List the suffixes and sort them as strings",
             "For a six-character text that is six strings and takes a minute. Doing it once is "
             "what makes the doubling construction recognisable as a faster route to the same "
             "array rather than a different object."),
            ("Fill the LCP array by comparing neighbours only",
             "Compare each suffix with the one above it, character by character, and stop at the "
             "first difference. The theorem is what licenses looking at neighbours and nothing "
             "else."),
            ("Read the longest repeat off the largest entry",
             "The value is the length and the position is the rank, so the substring is the first "
             "few characters of the suffix at that rank. On `banana` that is rank 2, length 3, "
             "and the suffix `anana` &mdash; giving `ana`."),
            ("Count distinct substrings two ways and require the same integer",
             "`n(n + 1)/2` minus the LCP sum, and the per-rank sum of `n − sa[r] − lcp[r]`. They "
             "must agree; if they do not, the LCP array is wrong somewhere and the first route "
             "would not have revealed it."),
        ],
        "worked": {
            "title": "Banana, sorted by hand and then counted",
            "intro": [
                "The text is `banana`, six characters, positions 0 to 5. The six suffixes are "
                "written out, sorted as strings, and then the LCP array is filled by comparing "
                "each with the one above it.",
            ],
            "lines": [
                "rank  starts at  suffix     lcp with the one above   shared",
                "  1        5     a                  0               -",
                "  2        3     ana                1               a",
                "  3        1     anana              3               ana",
                "  4        0     banana             0               -",
                "  5        4     na                 0               -",
                "  6        2     nana               2               na",
                "",
                "sa                            5  3  1  0  4  2",
                "by sorting the strings        5  3  1  0  4  2      agree",
                "lcp                           0  1  3  0  0  2      sum = 6",
                "",
                "doubling round 1  (k = 1)     5  1  3  0  2  4",
                "doubling round 2  (k = 2)     5  3  1  0  4  2      done",
                "comparisons                                  21",
                "",
                "longest repeat    largest lcp entry, 3, at rank 3   = ana",
                "all substrings    n(n + 1)/2 = 6 x 7 / 2            = 21",
                "distinct          21 - 6                            = 15",
                "check, per rank   1 + 2 + 2 + 6 + 2 + 2             = 15",
            ],
            "after": [
                "Look at ranks 2 and 3. They are the two suffixes beginning `ana`, they are "
                "adjacent, and their overlap is 3 &mdash; so `ana` occurs twice, at positions 3 "
                "and 1. That adjacency is not luck: sorted order puts every string beginning "
                "with `ana` together, so any repeat has to show up between neighbours, which is "
                "exactly what the theorem says and why `n − 1` comparisons are enough.",
                "For a faded rehearsal, do `abab` the same way. The supplied first move: the "
                "four suffixes are `ab`, `abab`, `b`, `bab`, so `sa` is 2, 0, 3, 1. Fill the LCP "
                "array, give the longest repeat, and give the distinct count both ways &mdash; "
                "`n(n + 1)/2` is 10 here.",
                "Then predict, without writing anything out, the LCP array and the distinct "
                "count for a text of eight identical characters. The supplied hint is that the "
                "sorted order is the suffixes in decreasing length. Say what the LCP sum is and "
                "why the distinct count comes out at exactly `n`.",
            ],
        },
        "quiz_title": "Order, overlap, and what they answer",
        "quiz": [
            {"q": "Why is it enough to compare adjacent suffixes when looking for the longest repeated substring?",
             "a": ["Because adjacent suffixes are the most similar pair by construction",
                   "Because lexicographic order puts all suffixes beginning with a given string contiguously, so any repeat shows up between two neighbours",
                   "Because the LCP array only stores adjacent overlaps",
                   "Because a repeated substring must occur at consecutive positions in the text"],
             "c": 1,
             "why": "Contiguity is the reason. If `w` prefixes two suffixes, every suffix between "
                    "them in sorted order is also prefixed by `w`, so some adjacent pair in that "
                    "block overlaps by at least the length of `w`. A repeat need not occur at "
                    "consecutive text positions at all &mdash; `ana` occurs at 1 and 3."},
            {"q": "`banana` has 21 substrings counted with repeats and 15 distinct ones. Where does the 6 go?",
             "a": ["Six substrings occur twice and are counted once",
                   "It is the sum of the LCP array: each entry counts prefixes already attributed to an earlier rank",
                   "It is the number of characters in the text",
                   "It is the length of the longest repeat, doubled"],
             "c": 1,
             "why": "The identity is `n(n + 1)/2` minus the LCP sum, and `0 + 1 + 3 + 0 + 0 + 2` "
                    "is 6. Each entry counts the prefixes that the suffix above already "
                    "contributed, so they are subtracted once each rather than counted as "
                    "duplicated substrings &mdash; a substring occurring three times would be "
                    "subtracted twice."},
            {"q": "Prefix doubling needs 2 rounds on `banana` and 3 on `mississippi`. What decides the number?",
             "a": ["The alphabet size",
                   "The construction stops as soon as every rank is distinct, which is at most log2 n rounds and can be sooner",
                   "Exactly the ceiling of log2 n, always",
                   "The length of the longest repeated substring"],
             "c": 1,
             "why": "Each round doubles the number of characters the order is correct to, so "
                    "`log2 n` rounds always suffice, and the loop exits early when all ranks are "
                    "already distinct. `abcdefgh` needs 1 round because a single character "
                    "separates all eight suffixes, although `log2 8` is 3."},
            {"q": "The panel checks the suffix array against sorting the suffixes as whole strings. What does that check catch?",
             "a": ["Nothing; both methods compute the same thing by definition",
                   "A prefix-doubling implementation that has not converged or compares the wrong rank pair, which would otherwise produce a plausible wrong order",
                   "A text that is too long for the mode",
                   "An LCP array that disagrees with the definition"],
             "c": 1,
             "why": "Both methods should compute the same array, which is exactly why "
                    "disagreement is informative: prefix doubling is the one whose correctness "
                    "is not obvious, and a wrong rank pair gives an order that looks sorted "
                    "locally and is not. The LCP array is checked separately, against comparing "
                    "each adjacent pair character by character."},
        ],
        "mistakes": [
            ("Looking for a repeat between non-adjacent suffixes",
             "It cannot help and it costs `n^2` comparisons. If two suffixes far apart in the "
             "order share a prefix `w`, every suffix between them shares it too, so an adjacent "
             "pair inside that block shares at least as much. The LCP array over neighbours is "
             "complete evidence, and that is what the theorem establishes."),
            ("Subtracting the LCP sum from n^2 rather than from n(n + 1)/2",
             "The number of substrings counted with repeats is `n(n + 1)/2`, which is 21 for a "
             "text of 6 and not 36. The error gives a distinct count larger than the total, "
             "which is the kind of answer the second counting route catches immediately &mdash; "
             "and which is why the panel computes both."),
            ("Taking the round count as a measurement of log2 n",
             "The loop exits when the ranks are all distinct, so the rounds are at most the "
             "ceiling of `log2 n` and often fewer: 1 for `abcdefgh`, where `log2 8` is 3. The "
             "bound is the ceiling and the count is what this text needed, which is the same "
             "distinction every page of this course draws."),
        ],
        "standard": ("Finish when you can build both arrays by hand for a short text and read the two answers off them with their proofs.",
                     "You should be able to sort the suffixes and give `sa`, fill the LCP array "
                     "over neighbours only and justify why neighbours suffice, read the longest "
                     "repeat off the largest entry, compute the distinct count both by the "
                     "identity and rank by rank, and say why the number of doubling rounds can "
                     "be below the ceiling."),
        "note": ("That is the whole course: four matchers that read the text once, a hash that "
                 "replaces comparison with arithmetic and has to verify, one structure that "
                 "searches for a dictionary in a single scan, and one that preprocesses the text "
                 "so that questions can be asked afterwards. Every count on every one of those "
                 "pages was produced by running the algorithm on the input shown, and every page "
                 "put a proved bound beside it &mdash; because the ranking of these methods "
                 "changed three times across this course while not one of the bounds moved."),
    },
]
