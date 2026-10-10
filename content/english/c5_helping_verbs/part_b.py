# -*- coding: utf-8 -*-
"""Course three, lessons four to six: be, not and do, and the twelve boxes.

Every figure here is read off the auxchain lab's tiles with `labcheck.js
--observe`: be 6 of 137 followed by an -ing form (4.4%), 13 by a participle,
19 an adjective, 37 a noun phrase, 26 a preposition, 3 a pronoun, 33 something
else; not 29 of 39 after a helping verb (74.4%), 5 after a main verb, 3 after
a joining word, 2 something else, 0 n't; boxes 55 of 216 simple (27 past, 25
present, 3 past with do), 3 progressive, 4 perfect, 57 with a modal (28 modal
simple, 27 modal other, 1 modal perfect, 1 modal progressive), 4 be and a
participle, 38 be as the main verb, 8 have as the main verb, 42 no verb found.
The modern documents give 2 of 36, 8 of 10 and 14, 0 and 3 of 34. Where a
lesson reads the printed rows by hand it says so and names the rows: one
progressive sits in the be lab's something-else group (was now fast
approaching: fast is on no list the skipping step reads), so 7 of 137 by
hand; it has a noun subject, so the boxes lab's 3 of 216 is also the count
by hand. Whole-novel figures are the designer's
(docs/english-v2/measure/out/corpus.txt) and are marked quoted wherever they
appear; the progressive boxes there sum to 63 + 47 + 13 + 10 + 10 = 143 of
8,864, 1.6% (the plan's 1.5% is the sum of the rounded shares).

Spoken forms for the key and worked lines are in
content/spoken/english_c5_helping_verbs.py.
"""

LESSONS = [
    {
        "slug": "be-is-mostly-a-main-verb",
        "module": "Two words each",
        "title": "Be Is Mostly a Main Verb",
        "one_line": "Classrooms teach be as the helping verb of the -ing form. On the page it is rarely that.",
        "standard": (
            "Finish when you can say what follows a form of be on a real "
            "page, and how often it is an -ing form.",
            "You should be able to sort the word after be into an -ing form, "
            "a participle, an adjective, a noun phrase or a place, say why "
            "the scan cannot tell a passive from an adjective, and read the "
            "share of -ing forms off a printed chapter.",
        ),
        "summary": (
            "Teachers start with <em>be</em> as the helping verb in <em>she is "
            "walking</em>. On a real page that is the rare use. In one "
            "chapter of a novel the scan finds an <em>-ing</em> word after 6 "
            "of 137 forms of <em>be</em>, 4.4%, and a reader finds one more "
            "in the rows. Most of the time <em>be</em> is the verb, with a "
            "noun phrase, an adjective or a place after it."
        ),
        "key_label": "One chapter, 137 forms of be",
        "key": [
            "be + -ing form      she is walking",
            "be + participle     it was sent",
            "be + adjective      she is glad",
            "be + noun phrase    he is a clerk",
            "be + place          he is in town",
            "",
            "-ing form after be: 6 of 137   4.4%",
            "read by hand: 7 of 137   5.1%",
        ],
        "concepts_intro": "Three ideas. The first is the order of the evidence.",
        "concepts": (
            (
                "Be has five jobs, and only one is the progressive",
                "After a form of <em>be</em> you can find an <em>-ing</em> "
                "form (<em>was going</em>), a <dfn>participle</dfn> (<em>was "
                "humbled</em>), an <dfn>adjective</dfn> (<em>was glad</em>), a noun "
                "phrase (<em>is a truth</em>) or a place (<em>is in "
                "town</em>). In the first <em>be</em> is a helping verb, and "
                "<em>be</em> with an <em>-ing</em> form is the "
                "<dfn>progressive</dfn>. In the second it is a helping verb "
                "when the participle says what was done. In the last three it "
                "is the verb.",
            ),
            (
                "The scan cannot tell a passive from an adjective",
                "A <dfn>passive</dfn> says what was done to the subject. <em>She was pleased</em> can be about what happened to her "
                "or about how she felt. The two read the same on the page. "
                "The lab puts every participle in one class, and says so. "
                "The class holds 13 forms in the chapter, and adjective words the "
                "scan knows hold 19 more.",
            ),
            (
                "The order in class is not the order on the page",
                "Counted on the page, the largest group after <em>be</em> "
                "is a noun phrase, 37 of 137. The <em>-ing</em> form is "
                "the smallest named group. A reader who expects <em>be</em> to open a "
                "progressive will get most of the <em>be</em> they meet wrong.",
            ),
        ),
        "steps_title": "Sorting a form of be",
        "steps_intro": "Look at the word after it, past any not or adverb.",
        "steps": (
            (
                "Is it an -ing word?",
                "Then it may be a progressive: <em>were going out</em>, "
                "<em>has been acting</em>. Check that the -ing word is a "
                "verb and not a noun.",
            ),
            (
                "Is it a participle?",
                "Then <em>be</em> is a helping verb for the passive: <em>was "
                "paid</em>, <em>were received</em>. Or it is an adjective "
                "that looks like one, and the page cannot tell.",
            ),
            (
                "Is it an adjective?",
                "Then <em>be</em> is the verb, and the adjective says what "
                "the subject is like: <em>am not afraid</em>.",
            ),
            (
                "Is it a noun phrase, or a place?",
                "Then <em>be</em> is the verb again: <em>is the cause</em>, "
                "<em>am in love</em>, <em>will be in a</em>.",
            ),
        ),
        "lab": ("english", {
            "mode": "auxchain",
            "rule": "be",
            "panel_title": "Sort every form of be in the chapter",
            "panel_intro": (
                "The table prints a few words around every form of "
                "<em>be</em> in Chapter XXVI of <em>Pride and "
                "Prejudice</em>, <em>am</em>, <em>is</em>, <em>are</em>, "
                "<em>was</em>, <em>were</em>, <em>be</em>, <em>been</em> and "
                "<em>being</em>, and the sort each was given. The first "
                "boxes count the forms, those followed by an <em>-ing</em> "
                "form with its share, and those followed by a participle. "
                "The next boxes count adjective words, noun phrases and "
                "prepositions or place words. A pronoun next is a question. "
                "A participle and an adjective that the word lists lack go "
                "in <em>something else</em>. The chapter is 1813 prose, and "
                "the modern documents are in the menu."
            ),
        }),
        "read_title": "The six rows with an -ing word, and the rows the scan lost",
        "read_intro": (
            "Six rows are followed by an <em>-ing</em> word. Thirty-three "
            "are filed as something else, and most of them belong in "
            "another group."
        ),
        "worked": {
            "title": "Five forms of be, five jobs",
            "intro": [
                "Five rows from the chapter, one for each job.",
            ],
            "lines": [
                "noun phrase   her brother is the cause",
                "participle    you are warned against it",
                "adjective     I am not afraid of",
                "place         I am not in love",
                "-ing form     Caroline and Mrs Hurst were going out",
            ],
            "after": [
                "Only the last line is a progressive. It is one line in "
                "five because the five were chosen to show each job; in the "
                "chapter's 137 forms it is 6 times. The six rows with an "
                "<em>-ing</em> word after <em>be</em> are not all alike: "
                "one of them, <em>this is being serious</em>, has "
                "<em>being</em>, a form of <em>be</em> itself, with an "
                "adjective after it. The second row is "
                "the one the scan cannot settle: <em>warned</em> may be what "
                "was done to you or a state you are in.",
            ],
        },
        "note": (
            "Of the 33 rows filed as something else, many are an adjective "
            "such as <em>sure</em> or <em>certain</em>, or a participle "
            "such as <em>tempted</em> or <em>deceived</em>, that the "
            "scan's word lists lack, or <em>as</em> and an adjective: "
            "<em>was as regular</em>. One holds an <em>-ing</em> form: "
            "<em>his marriage was now fast approaching</em>, because the "
            "scan stops at <em>fast</em>. Read by hand, 7 of 137 forms of "
            "<em>be</em>, 5.1%, are followed by an <em>-ing</em> verb: near "
            "the novel's 4.7% and the scan's 4.4%, and still rare."
        ),
        "mistakes": (
            (
                "Be is the helping verb of the -ing form first and a verb second",
                "In the chapter the scan finds an <em>-ing</em> form after 6 "
                "of 137 forms of <em>be</em>, 4.4%, and a reader finds 7, "
                "5.1%. Counted once over the "
                "whole novel and quoted here, 5,858 forms of <em>be</em> "
                "have an <em>-ing</em> form after them 4.7% of the time. "
                "The same count for the play is 5.6%.",
            ),
            (
                "Every participle after be is a passive",
                "<em>She was pleased</em> and <em>he was paid</em> look the "
                "same to a scan. One says how she felt, the other says "
                "what was done. The lab keeps them in one class, and "
                "the lesson does too.",
            ),
            (
                "Reading a low share as a form not worth learning",
                "A count says how often a form turns up. It does not say how "
                "much the form matters when it does. The progressive is 4.4% "
                "of the uses of <em>be</em> in the chapter, and a sentence "
                "that needs it cannot do without it.",
            ),
        ),
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "In which sentence is <em>was</em> the main verb?",
                "a": [
                    "<em>She was going home.</em>",
                    "<em>The letter was sent.</em>",
                    "<em>He was waiting for you.</em>",
                    "<em>My visit was not long.</em>",
                ],
                "c": 3,
                "why": (
                    "<em>Long</em> is an adjective, so <em>was</em> is the "
                    "verb. In the other three it helps an <em>-ing</em> form "
                    "or a participle."
                ),
            },
            {
                "q": "What is the most common group after <em>be</em> in the "
                     "chapter?",
                "a": [
                    "A noun phrase",
                    "An <em>-ing</em> form",
                    "A participle",
                    "A pronoun",
                ],
                "c": 0,
                "why": (
                    "37 of 137 are a noun phrase. The <em>-ing</em> form is "
                    "6."
                ),
            },
            {
                "q": "Why does the lab put <em>was pleased</em> in one class "
                     "with <em>was paid</em>?",
                "a": [
                    "They mean the same.",
                    "The scan reads only the form of the word, and both are "
                    "participles.",
                    "Both are progressives.",
                    "The word list is wrong.",
                ],
                "c": 1,
                "why": (
                    "A form can be a passive or an adjective, and only the "
                    "meaning tells which. The scan cannot read meaning, and "
                    "the lab says so."
                ),
            },
            {
                "q": "In the chapter, how often does the scan find a form of "
                     "<em>be</em> followed by an <em>-ing</em> word?",
                "a": [
                    "About half the time",
                    "About one time in three",
                    "6 times in 137",
                    "Never",
                ],
                "c": 2,
                "why": (
                    "6 of 137 is 4.4%. One more, <em>was now fast "
                    "approaching</em>, is filed as something else; by hand "
                    "it is 7."
                ),
            },
        ],
        "body": [
            ("p",
             "Most courses meet <em>be</em> in the progressive. <em>She is "
             "walking.</em> <em>They were singing.</em> The rule is simple: "
             "<em>be</em> and an <em>-ing</em> form make a continuing "
             "action, and the <em>-ing</em> form is the main verb."),
            ("p",
             "Now count. Chapter XXVI has 137 forms of <em>be</em>. The "
             "lab reads the word after each one, past <em>not</em> and "
             "short <dfn>adverb</dfn> words, and sorts it. It finds six "
             "followed by an <em>-ing</em> word. That is 4.4%."),
            ("h3", "What the other 131 are"),
            ("p",
             "37 are followed by a noun phrase: <em>his arrival was no "
             "great</em>, <em>her brother is the cause</em>. 26 are "
             "followed by a <dfn>preposition</dfn> or a place: <em>I am not in "
             "love</em>, <em>she was at length</em>. 19 have an adjective "
             "the scan knows: <em>I am not afraid of</em>. 13 have a "
             "participle. Three put a <dfn>pronoun</dfn> next. One is a "
             "question turned round, <em>how am I even to know</em>; the "
             "other two are <em>as it is, you must</em>, where the scan ran "
             "past a dash, and <em>were I distractedly in love</em>, the old "
             "form for a case that is not real, which &ldquo;The -s Belongs "
             "to He, She and It&rdquo; set aside. Thirty-three are filed as "
             "something else."),
            ("p",
             "After a noun phrase, an adjective or a place, <em>be</em> is "
             "the verb. Its job is to link the subject to what comes "
             "after: <em>her brother is the cause</em>. There is no other "
             "verb for it to help. And not one of the 137 is followed by a "
             "bare verb. <em>I am agree</em> and <em>she is work here</em> "
             "put <em>be</em> in front of a verb with no ending, and the "
             "chapter never does: after <em>be</em> comes an <em>-ing</em> "
             "form, a participle, or no verb at all."),
            ("h3", "The participle you cannot sort"),
            ("p",
             "The 13 participle forms are a mix. <em>You are warned against "
             "it</em> says what is done to you, and <em>she was satisfied "
             "with</em> says how she felt. A passive and an adjective use "
             "the same word in the same place, and a scan that reads only "
             "the word cannot tell them apart. The lab puts them in one "
             "class and says so under the table."),
            ("h3", "The thirty-three the scan lost"),
            ("p",
             "Read the rows filed as something else. You will find "
             "<em>I am sure</em> and <em>I am certain</em> more than once, "
             "where <em>sure</em> and <em>certain</em> are adjective words the "
             "scan does not know. You will find <em>tempted</em>, "
             "<em>deceived</em> and <em>resented</em>, participle forms it "
             "does not know. You will find <em>as</em> before an adjective: "
             "<em>was as regular</em>, <em>be as welcome</em>. A few rows "
             "are broken: <em>what was Charlotte's first</em>."),
            ("h3", "One the scan lost"),
            ("p",
             "One of those rows is the progressive. In <em>his marriage was "
             "now fast approaching</em> the scan steps over <em>now</em>, "
             "meets <em>fast</em>, which is on none of its lists, and stops. "
             "By hand, then, 7 of the 137 forms of <em>be</em> are followed "
             "by an <em>-ing</em> verb, 5.1%, close to the novel's 4.7% and "
             "the scan's 4.4%. The page keeps the scan's number and prints "
             "the rows, and the rows are where you check it."),
            ("h3", "Over the whole novel"),
            ("p",
             "Counted once over the whole novel, which no page can carry, "
             "and quoted here: 5,858 forms of <em>be</em>. A noun phrase "
             "follows 23.5%, a participle 20.8%, a noun or name 14.3%, a "
             "preposition 12.6%, an adjective 10.4%, an <em>-ing</em> form "
             "4.7%, and a pronoun 2.4%. For the play the <em>-ing</em> share "
             "is 5.6%. In the two modern documents the lab counts 2 of 36 "
             "forms followed by an <em>-ing</em> word, which is 5.6%, and 5 "
             "followed by a participle. The picture is the same in 1813 "
             "and in 2026."),
        ],
    },
    {
        "slug": "where-not-goes",
        "module": "Not, do and the boxes",
        "title": "Where Not Goes, and When Do Arrives",
        "one_line": "Not goes after the first helping verb. If there is none, do arrives to be the helping verb.",
        "standard": (
            "Finish when you can place not in a sentence, and say when do "
            "has to be added.",
            "You should be able to put not after the first helping verb, "
            "add do, does or did when there is none, give the verb after "
            "do its bare form, and read off a printed chapter how often not "
            "sits where the rule says and what the other rows are.",
        ),
        "summary": (
            "In modern English <em>not</em> goes after the first helping "
            "verb: <em>could not</em>, <em>has not</em>. If the sentence "
            "has no helping verb, <em>do</em> arrives to be one: <em>I do "
            "not know</em>. In one chapter of a novel, 29 of 39 uses of "
            "<em>not</em> sit exactly there. The other ten are not mistakes, "
            "and sorting them is the lesson."
        ),
        "key_label": "One chapter, 39 uses of not",
        "key": [
            "could not   has not   will not   am not",
            "",
            "no helping verb?  add do:",
            "  I do not know",
            "  she did not like",
            "",
            "29 of 39 after a helping verb   74.4%",
        ],
        "concepts_intro": "Three ideas, in the order a sentence uses them.",
        "concepts": (
            (
                "Not follows the first helping verb",
                "Take the sentence and find its first helping verb: "
                "<em>is</em>, <em>has</em>, a <dfn>modal</dfn> verb, <em>do</em>. Put "
                "<em>not</em> right after it. <em>She is not</em>, <em>she "
                "has not seen</em>, <em>she could not have seen</em>. The "
                "rest of the verb phrase stays where it was.",
            ),
            (
                "No helping verb? Do arrives",
                "A sentence in the plain present or past has no helping "
                "verb, and <em>not</em> cannot follow a main verb in "
                "modern English. So <em>do</em>, <em>does</em> or "
                "<em>did</em> comes in to carry the <dfn>tense</dfn>, and the main "
                "verb goes back to its <dfn>bare</dfn> form: <em>she regretted</em> "
                "becomes <em>she did not regret</em>. It is the rule from "
                "the last lessons, a helping verb takes the tense and the verb "
                "after it takes nothing.",
            ),
            (
                "Be is the exception to do",
                "<em>Be</em> as a main verb needs no <em>do</em>: <em>my "
                "visit was not long</em>, not <em>did not be long</em>. "
                "It is its own first helping verb, and <em>not</em> goes "
                "after it.",
            ),
        ),
        "steps_title": "Making a sentence negative",
        "steps_intro": "Four questions.",
        "steps": (
            (
                "Is there a helping verb in the sentence?",
                "Look for a form of <em>be</em>, <em>have</em> or "
                "<em>do</em> or a modal. If there is, put <em>not</em> "
                "after the first one.",
            ),
            (
                "Is the main verb be?",
                "Then it works as its own helping verb. <em>I am not</em>, "
                "<em>you are not</em>. Do not add <em>do</em>.",
            ),
            (
                "Otherwise, add do",
                "<em>Do</em> for I, you, we, they; <em>does</em> for "
                "he, she, it; <em>did</em> for the past. Then <em>not</em>, "
                "then the bare verb.",
            ),
            (
                "Check the verb after not",
                "It takes no ending: <em>she did not regret</em>, not "
                "<em>she did not regretted</em>.",
            ),
        ),
        "lab": ("english", {
            "mode": "auxchain",
            "rule": "not",
            "panel_title": "Score the rule on every not in the chapter",
            "panel_intro": (
                "The table prints a few words around every <em>not</em> in "
                "Chapter XXVI of <em>Pride and Prejudice</em>, and where it "
                "sits. The first boxes count the <em>not</em> words and the "
                "ones that come after a helping verb. The next box counts "
                "those after a main verb, which is the order English used "
                "before <em>do</em> became required. Then come those after "
                "a joining word, those that are the contraction "
                "<em>n't</em>, and the rest. The text was written in 1813, "
                "and the modern documents are in the menu. Read every row "
                "that is not a hit; the scan sorts by the word before "
                "<em>not</em> and nothing more."
            ),
        }),
        "read_title": "The ten that are not after a helping verb",
        "read_intro": (
            "Five rows come after a main verb. Read them before you call "
            "them the old order."
        ),
        "worked": {
            "title": "The old order against the rule, in the chapter's own rows",
            "intro": [
                "These are the rows the lab files after a main verb, with "
                "the sentence they came from.",
            ],
            "lines": [
                "old order      she said not a word of wishing",
                "need not       you need not be under any alarm",
                "               I need not explain myself",
                "not to         determined not to",
                "not a          and not a note, not a line",
            ],
            "after": [
                "Only the first row is the old order. <em>Said not a "
                "word</em> is what <em>did not say a word</em> would be "
                "now. The next two use <em>need</em> as a modal, which "
                "English still does: <em>need not</em> is current. "
                "<em>Determined not to</em> puts <em>not</em> in front of "
                "<em>to</em>, which is still how it is done. And "
                "<em>not a note, not a line</em> says that there was no "
                "note, with <em>not</em> in front of a noun phrase. The lab "
                "files all five after a main verb, because it reads one "
                "word. In the chapter 1813 shows in one row out of five, "
                "and in that row only.",
            ],
        },
        "note": (
            "The scan counts the old order by position, not by meaning. "
            "That is why the box reads five and the old order reads one. "
            "Of the other five of the ten, three come after a joining word "
            "(<em>and not yet</em>, <em>but not with</em>), where <em>not</em> "
            "contrasts one thing with another, and two are in the "
            "last box: <em>for not calling</em> and <em>had better "
            "not</em>."
        ),
        "mistakes": (
            (
                "I know not and she likes not are English",
                "They were, in 1813, and the chapter shows how often: the "
                "scan flags 5 of 39, and only one of them, <em>said not a "
                "word</em>, is the old order. Counted once over the whole "
                "novel and quoted here, <em>not</em> sits after a helping "
                "verb 78.8% of the time and after a main verb 6.3%. Today "
                "<em>do</em> is required.",
            ),
            (
                "Adding do to be",
                "<em>I do not be ready</em>, <em>she did not be there</em>. "
                "<em>Be</em> as the main verb is its own helping verb. The chapter "
                "has <em>my visit was not long</em>, <em>you are not "
                "serious</em>, <em>I am not afraid</em>.",
            ),
            (
                "Keeping the tense on the main verb as well",
                "<em>She did not regretted</em>, <em>he does not knows</em>. "
                "<em>Did</em> and <em>does</em> have taken the tense; the "
                "main verb is bare. The rows <em>she did not regret</em> "
                "and <em>Caroline did not return</em> show it.",
            ),
        ),
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "Make this negative: <em>She liked the house.</em>",
                "a": [
                    "<em>She liked not the house.</em>",
                    "<em>She did not liked the house.</em>",
                    "<em>She not liked the house.</em>",
                    "<em>She did not like the house.</em>",
                ],
                "c": 3,
                "why": (
                    "No helping verb, so <em>did</em> arrives and takes the "
                    "tense. <em>Like</em> goes back to its bare form."
                ),
            },
            {
                "q": "Where does <em>not</em> go in <em>She could have seen "
                     "him</em>?",
                "a": [
                    "After <em>could</em>",
                    "After <em>have</em>",
                    "After <em>seen</em>",
                    "Before <em>she</em>",
                ],
                "c": 0,
                "why": (
                    "<em>Not</em> follows the first helping verb: <em>could "
                    "not have seen</em>."
                ),
            },
            {
                "q": "The lab flags 5 of 39 as after a main verb. How many "
                     "of the five are the old order?",
                "a": [
                    "All five",
                    "One",
                    "Three",
                    "None",
                ],
                "c": 1,
                "why": (
                    "<em>Said not a word</em> is the old order. "
                    "<em>Need not</em> twice and <em>determined not to</em> "
                    "are still used, and <em>not a note</em> has <em>not</em> "
                    "before a noun phrase."
                ),
            },
            {
                "q": "Why does <em>My visit was not long</em> have no "
                     "<em>do</em>?",
                "a": [
                    "<em>Do</em> was left out in 1813.",
                    "<em>Not</em> goes before <em>was</em>.",
                    "<em>Was</em> is a main verb and works as its own helping verb.",
                    "<em>Long</em> is a verb.",
                ],
                "c": 2,
                "why": (
                    "<em>Be</em> is the exception: it needs no <em>do</em> "
                    "even as a main verb. <em>Not</em> follows it."
                ),
            },
        ],
        "body": [
            ("p",
             "Here is a rule so small you may never have thought of it as a "
             "rule. <em>Not</em> follows the first helping verb. <em>She "
             "is not</em>. <em>She has not seen</em>. <em>She could not "
             "have seen</em>."),
            ("p",
             "Now take a sentence with no helping verb. <em>She liked "
             "it.</em> There is nowhere to put <em>not</em>. English does "
             "not put it after <em>liked</em> any more. It adds a helping verb: "
             "<em>she did not like it</em>."),
            ("h3", "Do arrives to carry the tense"),
            ("p",
             "<em>Did</em> takes the past tense, and <em>like</em> goes "
             "back to its bare form. This is the same pattern as the "
             "modal: one word shows the tense, and the verb after it takes "
             "nothing. <em>Do</em> is a helping verb that does nothing else. It "
             "has no meaning of its own here, only the job of being there."),
            ("h3", "Counting it"),
            ("p",
             "Chapter XXVI has 39 uses of <em>not</em> as a word of its "
             "own. The lab reads the word before each. In 29, which is "
             "74.4%, it is a helping verb: <em>I am not afraid</em>, <em>you "
             "could not do better</em>, <em>she did not regret</em>, <em>do "
             "not think me obstinate</em>. Several of those are <em>did "
             "not</em> or <em>do not</em>, the new helping verb at work."),
            ("p",
             "Ten are not. Five are filed after a main verb, three after "
             "a joining word, two as something else. The chapter has no "
             "<em>n't</em>: the text writes <em>do not</em> and <em>could "
             "not</em> in full. It also writes <em>cannot</em> as one word, "
             "five times, and the scan does not count those among the 39."),
            ("h3", "The five that look old"),
            ("p",
             "The lab files five rows after a main verb. <em>She made a "
             "slight, formal apology for not calling before, said not a "
             "word of wishing to see me again.</em> <em>Said not a "
             "word</em> is the old order. Today it is <em>did not say a "
             "word</em>. The other four are not. <em>You need not be</em> "
             "and <em>I need not explain</em> use <em>need</em> as a modal "
             "and are current. <em>Determined not to</em> and "
             "<em>and not a note, not a line</em> put <em>not</em> before "
             "a word that is not the verb. So in this chapter one row in "
             "39 is the old order."),
            ("h3", "The other five"),
            ("p",
             "Three follow a joining word: <em>and not yet</em>, <em>but "
             "not with</em>, <em>and not a note</em>. There "
             "<em>not</em> contrasts one thing with another. Two are in "
             "the last box: <em>an apology for not calling</em>, where "
             "<em>not</em> comes before an <em>-ing</em> word, and "
             "<em>we had better not mention it</em>, where <em>had "
             "better</em> works as one helping verb."),
            ("h3", "Over the whole novel and the play"),
            ("p",
             "Counted once over the whole novel, which no page can carry, "
             "and quoted here: 1,440 uses of <em>not</em>, 78.8% after a "
             "helping verb and 6.3% after a main verb. In the play the "
             "same count is 86% after a helping verb, and more than half "
             "of all the play's <em>not</em>s, 53.5%, are the "
             "<dfn>contraction</dfn> <em>n't</em> on a helping verb. In the two modern "
             "documents the lab counts 8 of 10 after a helping verb, "
             "80.0%. The one it files after a main verb there, "
             "<em>acknowledged not every</em>, is <em>not</em> before a "
             "word that means all, and is not the old order either."),
        ],
    },
    {
        "slug": "which-of-the-twelve-boxes-get-used",
        "module": "Not, do and the boxes",
        "title": "Which of the Twelve Boxes Get Used",
        "one_line": "The tense table has twelve boxes. A writer lives in a few of them.",
        "standard": (
            "Finish when you can sort a verb phrase into its box, and say "
            "which boxes carry most of a real page.",
            "You should be able to sort every pronoun-subject verb phrase "
            "in a printed chapter into the tense table's boxes or into the "
            "extra groups the lab adds, read off the shares, and say which "
            "boxes carry most of the writing and which carry almost none.",
        ),
        "summary": (
            "The tense table has twelve boxes, and a course gives them equal "
            "time. A page does not. In one chapter, 216 pronoun subjects are "
            "followed by a verb phrase. The simple boxes, present and past, "
            "hold 55, and the phrases with a modal in front hold 57. The lab "
            "files 3 as progressive."
        ),
        "key_label": "One chapter, 216 verb phrases after a pronoun",
        "key": [
            "simple, present and past    55 of 216",
            "with a modal               57 of 216",
            "perfect, any time           4 of 216",
            "progressive, any time       3 of 216",
            "be + participle             4 of 216",
            "no verb found             42 of 216",
        ],
        "concepts_intro": "Three ideas, and the last one is about the lab.",
        "concepts": (
            (
                "Twelve boxes are not twelve equal tools",
                "The <dfn>tense</dfn> table has twelve boxes: present, past and "
                "future, each simple, <dfn>progressive</dfn>, perfect and "
                "perfect progressive. The lab sorts the phrase after each "
                "<dfn>pronoun</dfn> into those boxes, and adds groups the "
                "table does not draw: <em>be</em> or <em>have</em> as the "
                "main verb, <em>be</em> and a participle, which may be the "
                "<dfn>passive</dfn> or an adjective, and <em>do</em> as a "
                "helping verb.",
            ),
            (
                "Most of a page is in three places",
                "In the chapter the largest groups are <em>be</em> as the "
                "main verb (39), a <dfn>modal</dfn> in front (57) and the "
                "plain present and past (55). Together they hold 151 of "
                "the 216. The other groups share the rest.",
            ),
            (
                "A scan has a group for what it cannot sort",
                "The lab calls it <em>no verb found</em>, and it holds 42 "
                "of 216. The rows are printed, and they are the lab "
                "being honest: a verb the word list lacks, a pronoun that "
                "is an object, <em>he ought to</em>. A count that hides "
                "its group for the rest is not a count.",
            ),
        ),
        "steps_title": "Sorting a verb phrase into a box",
        "steps_intro": "Collect the helping verbs, then look at the word after them.",
        "steps": (
            (
                "List the helping verbs in a row",
                "<em>Will not be</em>, <em>has been</em>, <em>did</em>. "
                "Skip <em>not</em> and short adverb words.",
            ),
            (
                "Find the main word",
                "The word after the last helping verb: <em>wishing</em>, "
                "<em>acting</em>, <em>written</em>, <em>afraid</em>.",
            ),
            (
                "Match the chain to a box",
                "<em>Have</em> and a <dfn>participle</dfn> is a perfect. <em>Be</em> "
                "and an <em>-ing</em> word is a progressive. A modal alone "
                "is the modal box. <em>Be</em> and a participle is the "
                "passive.",
            ),
            (
                "Say what the box is called by its parts, not its name",
                "<em>Has been acting</em> is present, perfect, progressive: "
                "three parts in one phrase. The names are a way to say the "
                "parts, not a thing to learn by heart.",
            ),
        ),
        "lab": ("english", {
            "mode": "auxchain",
            "rule": "boxes",
            "panel_title": "Sort every verb phrase after a pronoun",
            "panel_intro": (
                "The table at the top lists the boxes with how many "
                "pronoun subjects fall into each, and their shares. Under "
                "it, every row is printed with the box it was given. Every "
                "pronoun counts as a subject, so a pronoun used as an "
                "object, such as <em>it</em> in <em>to use it</em>, lands "
                "in <em>no verb found</em>. The first boxes give the "
                "count of pronoun subjects, then the simple boxes, "
                "progressive boxes, perfect boxes, the modal box, the "
                "passive and the leftovers, each as a count and a share. "
                "Switch the text to the two modern documents to compare. "
                "The chapter is 1813 prose."
            ),
        }),
        "read_title": "The boxes the chapter hardly uses",
        "read_intro": (
            "The lab files two phrases in 216 as progressive and four as "
            "perfect. Read them, because they are the ones taught in class "
            "for the most time."
        ),
        "worked": {
            "title": "Six phrases from the chapter, six boxes",
            "intro": [
                "Each line is a verb phrase after a pronoun, and the box "
                "the lab gave it.",
            ],
            "lines": [
                "she thought              past simple",
                "I hope                   present simple",
                "I am not afraid          be as the main verb",
                "I will try               modal, simple",
                "you are warned           passive, or an adjective",
                "she has been acting      present perfect progressive",
            ],
            "after": [
                "The first two are the simple boxes. The third, <em>be</em> "
                "as the main verb, is a group of its own, and it is the "
                "largest named group in the chapter: 39 phrases. The "
                "fourth is the modal box, and the future of the "
                "table lives there as <em>will</em> and a bare verb. The "
                "last two are the rare ones. A phrase with three parts, "
                "present, perfect and progressive at once, appears once in "
                "216.",
            ],
        },
        "note": (
            "The twelve boxes are a way to build a phrase. They are not a "
            "ranking of what to say. A writer who wants to say that "
            "something began before and goes on needs the perfect "
            "progressive, however rare it is. This lesson shows what the "
            "boxes cost to learn against how often they turn up; it never "
            "says which to choose."
        ),
        "mistakes": (
            (
                "The progressive is the ordinary present",
                "It is taught first and practised hardest. In the chapter "
                "the lab files 3 of 216 phrases as progressive, 1.4%, and "
                "the two modern documents give 0 of 34. Counted once over the whole novel "
                "and quoted here, with 8,864 pronoun subjects, all the "
                "progressive phrases together are 143, which is 1.6%. The "
                "plain present and past are far more common.",
            ),
            (
                "Reading the table as twelve equal tools",
                "The chapter puts 55 phrases in the simple boxes and 4 in "
                "all the perfect boxes together. The perfect is real and "
                "needed, and it is rare. A page that spread its phrases "
                "equally over twelve boxes would look nothing like this one.",
            ),
            (
                "Treating no verb found as a failure of the lab",
                "It is 42 of 216 because the lab reads every pronoun as a "
                "subject, and many are objects. Quoted for the whole novel, "
                "the same group is 17.7%. Read the rows and you can "
                "sort them by hand.",
            ),
        ),
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "In the chapter, how many of the 216 phrases does the "
                     "lab file as progressive, in any tense?",
                "a": ["3", "55", "38", "42"],
                "c": 0,
                "why": (
                    "Three: <em>she has been acting</em>, <em>I will not be "
                    "wishing</em> and <em>he was now rendering himself</em>. "
                    "The simple boxes hold 55."
                ),
            },
            {
                "q": "Which pair of groups carries the most between them in "
                     "the chapter?",
                "a": [
                    "The perfect and the passive",
                    "The progressive and the perfect",
                    "The simple boxes and the modal box",
                    "The passive and the progressive",
                ],
                "c": 2,
                "why": (
                    "55 and 57, which is 112 of 216, just over half. The "
                    "perfect, the progressive and the passive hold 4, 3 and "
                    "4."
                ),
            },
            {
                "q": "<em>She has been acting</em> is a phrase with three parts. "
                     "Which three?",
                "a": [
                    "Past, simple, passive",
                    "Present, perfect, progressive",
                    "Future, perfect, simple",
                    "Present, passive, progressive",
                ],
                "c": 1,
                "why": (
                    "<em>Has</em> is present. <em>Been</em> after it is "
                    "perfect. <em>Acting</em> after <em>been</em> is "
                    "progressive."
                ),
            },
            {
                "q": "The lab files 1.4% of the chapter's phrases as "
                     "progressive. What does that tell you about the "
                     "progressive?",
                "a": [
                    "It is rare and can be skipped.",
                    "It is wrong in formal writing.",
                    "It is the ordinary present.",
                    "It is rare on the page, but still sometimes needed.",
                ],
                "c": 3,
                "why": (
                    "A count shows how often a form turns up. It does not "
                    "show whether the form is the right one to say a "
                    "particular thing."
                ),
            },
        ],
        "body": [
            ("p",
             "You have been given a table of twelve boxes: present, past "
             "and future, each simple, progressive, perfect and perfect "
             "progressive. It is a good table. It is also usually taught "
             "as if each box mattered the same."),
            ("p",
             "Count and it does not. The lab takes every pronoun in "
             "Chapter XXVI, 216 of them, and sorts the verb phrase after "
             "each into a box."),
            ("h3", "Where the 216 land"),
            ("p",
             "<em>Be</em> as the main verb holds 38, the largest named "
             "group. A modal in front holds 57, and the table under the "
             "boxes splits it: 28 with a <dfn>bare</dfn> verb straight "
             "after, <em>I will try</em>; 27 filed as <em>modal, other</em>, "
             "most of them <em>be</em> as the main verb with a modal in "
             "front, <em>I should be miserable</em>, <em>it will be as "
             "well</em>, and the rest gaps of the kinds &ldquo;After a Modal, "
             "the Verb Is Bare&rdquo; sorted; one modal perfect, <em>we must "
             "have met</em>; and one modal progressive, <em>I will not be "
             "wishing</em>. The plain present and past hold 55: past simple "
             "27, present simple 25 and past simple with <em>do</em> 3."),
            ("p",
             "The small groups: <em>be</em> and a participle hold 4, and "
             "only one of the four, <em>you are warned</em>, plainly says "
             "what was done to the subject; <em>satisfied</em>, "
             "<em>resolved</em> and <em>convinced</em> read as states. The "
             "perfect holds 4. The progressive holds 3. Forty-two are filed "
             "as no verb found."),
            ("p",
             "So the simple boxes and the phrases with a modal in front hold "
             "112 of the 216, just over half. The progressive holds 1.4%."),
            ("h3", "The rare boxes, read by hand"),
            ("p",
             "The three progressives are <em>she has been acting</em>, "
             "<em>I will not be wishing</em> and <em>he was now rendering "
             "himself agreeable</em>, 3 of 216, 1.4%, and reading the rows "
             "by hand finds no more. &ldquo;Be Is Mostly a Main "
             "Verb&rdquo; finds six <em>-ing</em> forms after <em>be</em> in "
             "this same chapter by scan and seven by hand. The difference is "
             "that this lab reads only the phrase after a pronoun, and "
             "<em>this is being serious</em>, <em>my aunt is going</em>, "
             "<em>Mrs. Hurst were going out</em> and <em>his marriage was "
             "fast approaching</em> have no pronoun in front."),
            ("h3", "Why the group for the rest matters"),
            ("p",
             "The 42 in no verb found are the lab being honest. Read the "
             "rows. Some are an object, as in <em>to use it your "
             "father</em>. Some have a word between the pronoun and its "
             "verb, as in <em>we all expect</em>, and some a verb the word "
             "list lacks, as in <em>she endeavoured to</em>. Five are <em>I "
             "cannot</em>, which the lab does not read as <em>can</em> and "
             "<em>not</em>. Some are <em>he ought to</em>, where "
             "<em>ought</em> is not one of the helping verbs the lab tracks. "
             "They are printed so you can sort them yourself."),
            ("h3", "The whole novel"),
            ("p",
             "Counted once over the whole novel, which no page can carry, "
             "and quoted here: 8,864 pronoun subjects. Past simple is "
             "18.2%, <em>be</em> as the main verb 15.5%, present simple "
             "12.5%, and a modal or future simple 8.4%. The passive is "
             "3.3%, the past perfect 2.8%, the present perfect 1.8%, and "
             "all the progressive phrases together 143 of the 8,864, 1.6%. "
             "No verb found is 17.7%."),
            ("h3", "Today's pages"),
            ("p",
             "Switch the lab to the two modern documents. They have 34 "
             "pronoun subjects. The simple boxes hold 14, 41.2%. The "
             "perfect holds 3, 8.8%. The progressive holds 0. The boxes "
             "that a page uses are about the same in 1813 and 2026."),
            ("h3", "What this does not say"),
            ("p",
             "None of this tells you which box to choose. A writer picks a "
             "box because of what they mean, and a count of printed words "
             "cannot see that. It tells you which boxes to practise "
             "first if you have little time, and which to know well enough "
             "to read."),
        ],
    },
]
