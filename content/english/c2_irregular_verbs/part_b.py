# -*- coding: utf-8 -*-
"""Course 2, lesson two: the six classes, as rules about strings."""

LESSONS = [
    {
        "slug": "six-patterns-not-one-hundred-and-eighty",
        "module": "Six shapes to hold in place of a long list",
        "title": "Six Patterns, Not One Hundred and Eighty",
        "one_line": "Sort the odd verbs by which of their three forms match, and six classes appear.",
        "standard": (
            "Finish when you can put an odd verb into its class by "
            "looking at its three forms, and say what the class tells you to "
            "remember.",
            "You should be able to state each of the six rules, sort a verb "
            "by them, say why <em>go</em> does not belong with <em>know</em> "
            "even though both have three different forms, and say what a "
            "class does not tell you.",
        ),
        "summary": (
            "A list of 180 <dfn>irregular</dfn> verbs is hard to hold. Six shapes are not. Each "
            "class is a rule about which of the three forms are the same "
            "string of letters, and a computer can check it. The rules are "
            "exact, and one near-miss, <em>go</em>, <em>went</em>, "
            "<em>gone</em>, shows how exact. What the rules do not do is "
            "tell you which verb goes where. That you still learn."
        ),
        "key_label": "The six classes, by which forms match",
        "key": [
            "60: past = form after have (bring)",
            "37: all differ, ends in -n (know)",
            "21: all three the same (put)",
            "9: all differ, not -n (go, sing)",
            "4: base = form after have (come)",
            "1: base = past (beat)",
            "",
            "be stands outside all six",
        ],
        "concepts_intro": "Three ideas.",
        "concepts": [
            (
                "A class is a statement about equal strings",
                "Take the three forms of a verb. Ask which of them are the "
                "same string of letters. That one question gives five of the "
                "six classes. The sixth, three different forms, is split in "
                "two by a second question: does the last form end in "
                "<em>-n</em>?",
            ),
            (
                "The rule is exact, so the near-miss is exact too",
                "<em>Know</em>, <em>knew</em>, <em>known</em> has three "
                "different forms and the last ends in <em>-n</em>. "
                "<em>Go</em>, <em>went</em>, <em>gone</em> also has three "
                "different forms, but <em>gone</em> ends in <em>-e</em>. "
                "They look the same and the rule puts them in different "
                "classes, so the rule says clearly what it cannot cover.",
            ),
            (
                "A class tells you the shape, not the membership",
                "Knowing that a verb is in the class of 21 tells you that "
                "all three forms are the same. It does not tell you that "
                "<em>put</em> is in that class. You still have to learn "
                "which verbs belong where. What you save is the work of "
                "learning three forms for each of them.",
            ),
        ],
        "steps_title": "Sorting a verb",
        "steps_intro": "Ask the questions in this order and stop at the first yes.",
        "steps": [
            (
                "Are all three forms the same?",
                "<em>Put</em>, <em>put</em>, <em>put</em>. If yes, it is in "
                "the class of 21, and there is nothing else to learn.",
            ),
            (
                "Are the past and the form after have the same?",
                "<em>Bring</em>, <em>brought</em>, <em>brought</em>. If yes, "
                "it is in the largest class, 60 verbs. You learn two forms.",
            ),
            (
                "Does the base match one of the other two?",
                "<em>Come</em>, <em>came</em>, <em>come</em> matches the "
                "last. <em>Beat</em>, <em>beat</em>, <em>beaten</em> "
                "matches the past. These are small classes, four and one.",
            ),
            (
                "Otherwise all three differ: look at the last letter",
                "If the last form ends in <em>-n</em>, as in "
                "<em>known</em>, it is in the class of 37. If not, as in "
                "<em>sung</em> or <em>gone</em>, it is in the class of 9.",
            ),
        ],
        "lab": ("english", {
            "mode": "classes",
            "panel_title": "Choose a class and read its verbs",
            "panel_intro": (
                "Each class is a rule about the three forms of a verb. Pick "
                "one and the lab lists every verb that follows it, with the "
                "size of the class beside it. Try the class of nine and read "
                "the last letter of the third form in every row."
            ),
        }),
        "read_title": "Reading the classes",
        "read_intro": (
            "Here is what each class holds, and what its members have in "
            "common beyond the rule."
        ),
        "worked": {
            "title": "Three different forms, two different classes",
            "intro": [
                "Both of these have three different forms. The only thing "
                "that separates them is the last letter.",
            ],
            "lines": [
                "know / knew / known: ends in n",
                "  also: blow, grow, throw, fly,",
                "  break, speak, steal, write",
                "",
                "go / went / gone: ends in e",
                "  also: do, undergo",
                "",
                "sing / sang / sung: ends in g",
                "  also: drink, ring, sink, swim",
            ],
            "after": [
                "The class of nine is two small groups under one label. "
                "<em>Do</em>, <em>go</em> and <em>undergo</em> end in "
                "<em>-e</em>, and the rest follow a pattern of <dfn>vowels</dfn>: "
                "<em>i</em> in the base, <em>a</em> in the past, <em>u</em> "
                "in the participle. <em>Sing</em>, <em>drink</em>, "
                "<em>ring</em>, <em>sink</em>, <em>spring</em> and "
                "<em>swim</em> all do it.",
                "The rule is not perfect, and the lab shows where. "
                "<em>Begin</em>, <em>began</em>, <em>begun</em> has the same "
                "vowels, but <em>begun</em> ends in <em>-n</em>, so the rule "
                "puts it in the class of 37. The class follows the last "
                "letter and not the sound.",
            ],
        },
        "note": (
            "The classes are defined by strings, not by sound. That is what "
            "lets a computer check them, and it is also why a word such as "
            "<em>read</em> sits in the class of 21: the letters are the same "
            "three times, though you say the past differently."
        ),
        "mistakes": [
            (
                "Taking the class to be the whole answer",
                "The class says how many forms to learn. It does not say "
                "what they are. <em>Bring</em> and <em>buy</em> are in the "
                "same class, and you still have to know <em>brought</em> "
                "and <em>bought</em>.",
            ),
            (
                "Putting go with know",
                "Both have three different forms. But a rule that says "
                "&ldquo;the last form ends in <em>-n</em>&rdquo; fails on "
                "<em>gone</em> and <em>done</em>. They need their own class, "
                "and the class of nine gives them one.",
            ),
            (
                "Treating a class of one as a rule",
                "<em>Beat</em>, <em>beat</em>, <em>beaten</em> is alone. "
                "A rule with one member says nothing, and no rule is being "
                "claimed. It is a word to learn on its own.",
            ),
        ],
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "<em>Cut</em>, <em>cut</em>, <em>cut</em> belongs to which class?",
                "a": [
                    "All three forms the same",
                    "Past matches the form after <em>have</em> only",
                    "All three differ, ends in <em>-n</em>",
                    "Base matches the past only",
                ],
                "c": 0,
                "why": (
                    "All three strings are equal, so it is in the class of "
                    "21 with <em>put</em> and <em>hit</em>."
                ),
            },
            {
                "q": "Why is <em>gone</em> not in the same class as <em>known</em>?",
                "a": [
                    "It does not end in <em>-n</em>",
                    "It has fewer letters",
                    "Its base is not the same as its past",
                    "It is an older word",
                ],
                "c": 0,
                "why": (
                    "Both have three different forms. The rule for the "
                    "class of 37 asks for a last form ending in <em>-n</em>, "
                    "and <em>gone</em> ends in <em>-e</em>."
                ),
            },
            {
                "q": "<em>Come</em>, <em>came</em>, <em>come</em> is in a class of four. What matches?",
                "a": [
                    "The base and the form after <em>have</em>",
                    "The base and the past",
                    "The past and the form after <em>have</em>",
                    "Nothing matches",
                ],
                "c": 0,
                "why": (
                    "The first and third strings are both <em>come</em>. "
                    "<em>Become</em>, <em>overcome</em> and <em>run</em> do "
                    "the same."
                ),
            },
        ],
        "body": [
            ("p",
             "The last lesson ended on a number, about 180 verbs. That is a "
             "long list, and a long list is hard to hold. This lesson shows "
             "that the list is not as long as it looks, because the verbs "
             "come in a few shapes."),
            ("h3", "One question, asked of every verb"),
            ("p",
             "Take the three forms: base, past, and the <dfn>participle</dfn>. Ask "
             "which of them are the same string of letters. There are only a "
             "few answers, and each answer is a class."),
            ("ul", [
                "<strong>Past and participle match</strong> "
                "(<em>bring</em>, <em>brought</em>, <em>brought</em>): "
                "60 verbs. The largest class by far.",
                "<strong>All three match</strong> (<em>put</em>, "
                "<em>put</em>, <em>put</em>): 21 verbs.",
                "<strong>Base and participle match</strong> "
                "(<em>come</em>, <em>came</em>, <em>come</em>): 4 verbs.",
                "<strong>Base and past match</strong> (<em>beat</em>, "
                "<em>beat</em>, <em>beaten</em>): 1 verb.",
                "<strong>All three differ</strong>: 46 verbs, split by the "
                "last letter into the 37 that end in <em>-n</em> and the "
                "9 that do not.",
            ]),
            ("p",
             "That is six classes. The verb <em>be</em> stands outside "
             "them. Its forms (<em>am</em>, <em>is</em>, <em>are</em>, "
             "<em>was</em>, <em>were</em>, <em>been</em>) are not "
             "variations on one base, so no rule about strings fits it. It "
             "is the one verb that is handled by hand."),
            ("h3", "The near-miss"),
            ("p",
             "Look at <em>know</em>, <em>knew</em>, <em>known</em> and at "
             "<em>go</em>, <em>went</em>, <em>gone</em>. Both have three "
             "different forms. You might expect both in one class. But "
             "<em>known</em> ends in <em>-n</em> and <em>gone</em> ends "
             "in <em>-e</em>, and that one letter sends them to different "
             "classes."),
            ("p",
             "This is a useful thing to see. A rule that says exactly what "
             "it covers also says exactly what it does not. <em>Gone</em> "
             "and <em>done</em> are not covered by the <em>-n</em> rule. "
             "They are the two best-known verbs in English, and they sit "
             "in the class of nine, with <em>undergo</em>."),
            ("h3", "A shape inside the class of nine"),
            ("p",
             "Six of the nine do something else. <em>Sing</em>, "
             "<em>sang</em>, <em>sung</em>. <em>Drink</em>, <em>drank</em>, "
             "<em>drunk</em>. <em>Ring</em>, <em>sink</em>, <em>spring</em> "
             "and <em>swim</em> do it too. The vowel moves from <em>i</em> "
             "to <em>a</em> to <em>u</em>. If you know that shape, you "
             "know six verbs."),
            ("p",
             "The lab shows the limit of the rule, and so should this "
             "lesson. <em>Begin</em> has the same vowels, but its last "
             "form is <em>begun</em>, which ends in <em>-n</em>. The "
             "classes follow the last letter. A shape of vowels is a "
             "second pattern, laid across the first."),
            ("h3", "What a class does not do"),
            ("p",
             "It would be easy to say that six patterns replace 180 verbs. "
             "That says too much. A class tells you how many forms to hold "
             "for a verb: one for the class of 21, two for the classes of "
             "60, 4 and 1, and three for the 46. It does not tell you which "
             "verbs belong in each class, and it does not give you the "
             "letters. <em>Bought</em> and <em>brought</em> are in one "
             "class, and each is still a form to learn."),
            ("p",
             "What the classes do give you is a place to put each new verb. "
             "You learn a form once, and you know what kind of form it is. "
             "That is a smaller job than 180 separate facts, and it is a "
             "job you can finish."),
        ],
    },
]
