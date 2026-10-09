# -*- coding: utf-8 -*-
"""Lesson three of the word-order course: the rule that covers only half.

The lab scores the question rule on 90 lines from the novel, each printed with
its verdict, and searches two modern public documents, printed beside them,
for a question mark. An earlier draft shipped this lesson "stated, not
computed"; the boxes are now counted in the browser, and the whole-novel
figures that cannot be rebuilt on a page (55.4%, 45%) are kept only as quoted
figures, labelled as such wherever they appear.
"""

LESSONS = [
    {
        "slug": "asking-a-question",
        "module": "The one rule that covers only half",
        "title": "Asking a Question",
        "one_line": "The rule for questions is real, it covers about half of the questions people ask, and the other half is printed here.",
        "standard": (
            "Finish when you can build a question in English, and say what "
            "the other half of real questions look like.",
            "You should be able to put a helping verb before the subject, "
            "add do when there is no other helping verb, read the rule's "
            "score off the 90 questions printed with this lesson, name the "
            "kinds of question the rule did not catch, and say which figures "
            "on the page are counted and which are quoted.",
        ),
        "summary": (
            "Every lesson in this course states a rule, scores it on printed "
            "text and shows what is left. The rule for questions is old and "
            "well known: a helping verb moves in front of the subject, and "
            "<em>do</em> is added if there is none. It is a real rule, and you "
            "should use it. Scored on 90 questions from <em>Pride and "
            "Prejudice</em>, printed with this lesson, it covers 48, which is "
            "53.3%. A run over the whole novel, quoted here because no page "
            "can carry it, gave 55.4%. That is too low to call the rule good "
            "and too high to call it wrong, and the lesson is about the other "
            "half: what real questions look like when they do not open with a "
            "helping verb."
        ),
        "key_label": "The rule, and its score",
        "key": [
            "you know       ->  do you know?",
            "she went       ->  did she go?",
            "she can go     ->  can she go?",
            "she went where ->  where did she go?",
            "",
            "90 printed questions: 48 follow it    53.3%",
            "whole novel, quoted                   55.4%",
        ],
        "concepts_intro": "Three ideas carry this lesson.",
        "concepts": [
            (
                "The rule is real",
                "To ask a question with a helping verb, put that verb "
                "before the subject: <em>can she go?</em> If there is no "
                "helping verb, add <em>do</em> in the right form: <em>did "
                "she go?</em> With a question word, the question word comes "
                "first and the rest follows: <em>where did she go?</em> "
                "Many languages ask a question by tone, by a small word at "
                "the end, or by an ending on the verb. English moves a "
                "word, and that is why the rule is worth stating. The lab's "
                "menu calls the helping verb an auxiliary and the question "
                "word a wh-word; they are the same things.",
            ),
            (
                "Half of real questions do not open that way",
                "On the 90 printed questions the rule covers 48, which is "
                "53.3%; on the whole novel, quoted, 55.4%. Where the other "
                "lessons found a small set of named misses, this one finds a "
                "spread. Of the 42 misses here, 13 begin with a joining word "
                "such as <em>and</em> or <em>but</em>, 6 begin with a "
                "question word that has no helping verb after it, 2 begin "
                "with a small word of address such as <em>oh</em>, and 21 "
                "the lab can only call something else. The largest kind is a "
                "result of how people write, not of how English builds "
                "questions.",
            ),
            (
                "A counted figure and a quoted one are different things",
                "The boxes are counted in your browser on the 90 lines you "
                "can read. The figures 55.4% and 45% come from a single run "
                "over the whole novel, which no page can carry, so they are "
                "quoted, and the page says so each time. The two sets differ "
                "a little, 53.3% against 55.4%, and 31.0% against 45%, because "
                "90 lines are a sample. The <em>something else</em> box has "
                "a limit of its own: 16 of its 21 lines begin in the middle "
                "of a sentence, or of a word, because the line was cut a fixed "
                "distance before the question mark, or at the full stop in "
                "<em>Mr.</em> or <em>Mrs.</em> The table shows them, so you "
                "can see what the count could not.",
            ),
        ],
        "steps_title": "Building a question",
        "steps_intro": "To turn a statement into a question, do this.",
        "steps": [
            (
                "Look for a helping verb",
                "<em>Can, will, have, is, must</em> and their kind. If the "
                "sentence has one, move it in front of the subject: "
                "<em>she has gone</em> becomes <em>has she gone?</em>",
            ),
            (
                "If there is none, add do",
                "<em>She went</em> becomes <em>did she go?</em> The main "
                "verb goes back to its plain form, and <em>do</em> takes "
                "the tense.",
            ),
            (
                "If you need a question word, put it first",
                "<em>Where, what, why, who, how.</em> Then the helping verb, "
                "then the subject: <em>why did she go?</em> When the question "
                "word is itself the subject, nothing moves: "
                "<em>who went?</em>",
            ),
            (
                "Leave the speech habits for later",
                "People in books and in life also ask questions by tone "
                "alone, or open with a name, or begin with <em>and</em> or "
                "<em>but</em>. Learn the rule first. Those forms are the "
                "misses, and the table below prints every one.",
            ),
        ],
        "lab": ("english", {
            "mode": "questions",
            "panel_title": "Score the rule on ninety real questions",
            "panel_intro": (
                "The table holds 90 lines from the novel, each cut around a "
                "question mark, and prints every one with its verdict. The "
                "rule holds when the first word is a helping verb, or a "
                "question word followed by one; the menu calls these an "
                "auxiliary and a wh-word. The first two boxes are the hit "
                "rate. The next two count the misses that begin with a "
                "joining word such as <em>and</em> or <em>but</em>, and give "
                "that count as a share of all the misses. The box called "
                "<em>something else</em> holds the misses that fit no named "
                "kind; read them, because 16 of the 21 begin in the middle "
                "of a sentence or a word, where the line was cut short. The "
                "eight misses in no box are the two kinds the verdict column "
                "names: a question word with no helping verb after it, and a "
                "small word of address first. The last two boxes search the "
                "two modern documents printed below the table for a question "
                "mark: the Supreme Court opinion <em>Stanley v. City of "
                "Sanford</em>, 606 U.S. 46 (2025), and the Census Bureau "
                "story &ldquo;U.S. Population Aging as Nation Turns "
                "250&rdquo; (9 April 2026). The questions are 1810s English, "
                "and the way people ask questions has changed since."
            ),
        }),
        "read_title": "What the rule did not catch",
        "read_intro": (
            "On the 90 printed questions, 42 did not open with a helping "
            "verb. Here is what they were, in order of size, with the one "
            "share the whole-novel run measured beside them."
        ),
        "worked": {
            "title": "Four kinds of question that skipped the rule",
            "intro": [
                "The first block is counted on the page. The lab prints a box "
                "for the joining words and for the something else; the two "
                "counts between them are read off the verdict column. The "
                "second block is quoted from the run over the whole novel, "
                "which this page cannot repeat, and only one share was "
                "measured there.",
            ],
            "lines": [
                "the 90 printed questions, counted on the page: 42 misses",
                "joining word first: 13 of 42 misses    31.0%",
                "  And what is your success?  But are you pleased, Jane?",
                "question word, no helping verb after it   6",
                "  What say you, Mary?  What made you so shy of me?",
                "a small word of address first              2",
                "  Oh, why is not everybody as happy?",
                "something else                            21",
                "  Miss Bennet, do you know who I am?",
                "  If she does not object to it, why should we?",
                "",
                "the whole novel, quoted",
                "joining word first         45% of misses",
            ],
            "after": [
                "The first kind is a question that begins with <em>and</em>, "
                "<em>but</em> or <em>or</em>. A check that looks for the "
                "helping verb at the front misses these, because a joining "
                "word stands first. In most of the thirteen the rest of the "
                "question follows the rule: <em>And do you really know all "
                "this?</em> In a few it does not: <em>But why all this "
                "secrecy?</em> has no verb at all.",
                "The second kind is a question word with no helping verb "
                "after it. Three are a form older English used without "
                "<em>do</em>: <em>What say you, Mary?</em> One has the "
                "question word as its own subject, where nothing moves: "
                "<em>What made you so shy of me?</em> One is a longer "
                "question phrase, <em>what sort of girl is Miss King?</em>, "
                "where the helping verb comes after the phrase and the scan "
                "reads only the second word. One has no verb: <em>What, none "
                "of you?</em>",
                "The third kind opens with a small word of address or feeling, "
                "<em>Oh</em> or <em>Well</em>, and then follows the rule. The "
                "fourth is the mixed bag. Sixteen of its 21 lines begin "
                "mid-sentence, so their first word is not the question's "
                "first word. The five whole ones are two with a name first, "
                "<em>Girls, can I do anything for you?</em>, two with a "
                "clause first, <em>If she does not object to it, why should "
                "we?</em>, and one statement with a question mark on it, "
                "<em>I must ask whether you were surprised?</em>",
            ],
        },
        "note": (
            "The boxes are counted on the 90 lines in your browser. The "
            "55.4% and the 45% are quoted from a single run over the whole "
            "novel and cannot be rebuilt here, and the lesson says so wherever "
            "they appear. The two sets of figures differ because 90 lines are "
            "a sample; the picture they give is the same."
        ),
        "mistakes": [
            (
                "Asking by tone alone",
                "<em>You know him?</em> is common in speech and fine "
                "between friends. If you use it for every question, you may "
                "sound as if you are always surprised. Learn <em>do you "
                "know him?</em> as the plain form.",
            ),
            (
                "Adding do with a helping verb",
                "<em>Do you can go?</em> is a mistake. If the sentence has "
                "a helping verb, that verb moves. <em>Do</em> is added only "
                "when there is none: <em>can you go?</em> and <em>do you "
                "go?</em>",
            ),
            (
                "Believing the low number means the rule is wrong",
                "53.3% on 90 old questions is a fact about how people write "
                "questions and about how the lines were cut, not about how "
                "English builds a question. Most of the misses that begin "
                "with <em>and</em> or <em>but</em> follow the rule after it. "
                "Do not drop the rule. Do not lean on the figure either.",
            ),
        ],
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "How do you turn <em>she went</em> into a question with the standard rule?",
                "a": [
                    "<em>Went she?</em>",
                    "<em>She did went?</em>",
                    "<em>Do she went?</em>",
                    "<em>Did she go?</em>",
                ],
                "c": 3,
                "why": (
                    "There is no helping verb, so <em>do</em> is added in the "
                    "past form, and the main verb goes back to its plain form."
                ),
            },
            {
                "q": "On the 90 printed questions, how many open the way the rule says?",
                "a": [
                    "All 90",
                    "48, which is 53.3%",
                    "None",
                    "13, which is 31.0%",
                ],
                "c": 1,
                "why": (
                    "The lab counts 48 of 90 in your browser. The 13 is the "
                    "number of misses that begin with a joining word, and "
                    "31.0% is their share of the 42 misses."
                ),
            },
            {
                "q": "What share of the 42 misses begin with a joining word such as <em>and</em> or <em>but</em>?",
                "a": [
                    "All 42",
                    "About 90%",
                    "13 of 42, which is 31.0%",
                    "None",
                ],
                "c": 2,
                "why": (
                    "The joining word stands first, so a check at the front "
                    "of the sentence misses it. The whole-novel run, quoted, "
                    "put this kind at 45% of its misses; the 90 lines are a "
                    "sample and give 31.0%."
                ),
            },
            {
                "q": "What does the lab find when it searches the two modern documents for a question mark?",
                "a": [
                    "None in 1,723 words",
                    "More questions than the novel",
                    "About one in every ten sentences",
                    "Only questions with <em>do</em>",
                ],
                "c": 0,
                "why": (
                    "<em>Stanley v. City of Sanford</em> and the Census Bureau "
                    "story, both free to use, carry no question at all in "
                    "1,723 words. Formal writing barely holds the form you "
                    "most need in speech."
                ),
            },
        ],
        "body": [
            ("p",
             "This is the lesson where the rule covers only half of what "
             "people actually say, and that is part of what it teaches."),
            ("h3", "The rule"),
            ("p",
             "Every learner is taught how to ask a question. A helping verb "
             "goes before the subject. If there is no helping verb, add "
             "<em>do</em>. If there is a question word, it goes first. "
             "<em>Can you go? Did you go? Where did you go?</em> It is a "
             "short rule. It matters most to a speaker of a language that "
             "asks by tone, such as Mandarin or Japanese, or by a small "
             "ending, and to a speaker of Spanish or Russian, where the "
             "subject and verb may swap with no help word at all."),
            ("h3", "The score"),
            ("p",
             "The lab holds 90 questions from <em>Pride and Prejudice</em>, "
             "each a line cut from the novel around a question mark, and "
             "prints every one. The rule covers 48 of them, which is 53.3%. "
             "A run over the whole novel, quoted here because no page can "
             "carry it, gave 55.4%. For a rule that is taught first, that is "
             "a poor figure. It is worth asking why."),
            ("h3", "What the misses looked like"),
            ("ul", [
                "<strong>A joining word first, 13 of the 42 misses, "
                "31.0%.</strong> <em>And what is your success? But why "
                "should you wish to persuade me?</em> A check for the helping "
                "verb at the front misses these. In most of them the question "
                "follows the rule after the joining word.",
                "<strong>A question word with no helping verb after it, "
                "6.</strong> <em>What say you, Mary?</em> is a form older "
                "English used without <em>do</em>, and three of the six are "
                "that. <em>What made you so shy of me?</em> has the question "
                "word as its subject, so nothing moves, and the rule itself "
                "says so. <em>What sort of girl is Miss King?</em> puts a "
                "longer question phrase first.",
                "<strong>A small word of address first, 2.</strong> <em>Oh, "
                "why is not everybody as happy?</em> The <em>oh</em> stands "
                "in front, and the rule follows.",
                "<strong>Something else, 21.</strong> Sixteen of these lines "
                "begin in the middle of a sentence, or of a word, because the "
                "line was cut a fixed distance before the question mark or at "
                "the full stop in <em>Mr.</em> or <em>Mrs.</em>; their first "
                "word is not the question's first word, and the count cannot "
                "tell. The five whole ones are a name first, <em>Miss "
                "Bennet, do you know who I am?</em>, a clause first, <em>If "
                "she does not object to it, why should we?</em>, and a "
                "statement with a question mark on it, <em>I must ask "
                "whether you were surprised?</em>",
            ]),
            ("p",
             "The whole-novel run, quoted, found the joining word in 45% of "
             "its misses, and that is the only share it measured; the other "
             "kinds were named there without a number. On the 90 lines the "
             "share is 31.0%. The difference is what a sample of 90 looks "
             "like against a novel, and the lesson gives both so you can see "
             "that."),
            ("h3", "Which figures are counted, and which are quoted"),
            ("p",
             "Every box in the lab is counted in your browser from the 90 "
             "lines printed under it, and you can read any line and disagree "
             "with its verdict. The 55.4% and the 45% are quoted: they come "
             "from one run over the whole novel, and a page cannot hold a "
             "novel. Wherever this lesson gives a quoted figure it says so, "
             "because a number that looks counted and is not would claim "
             "more than we know."),
            ("h3", "What the modern documents show"),
            ("p",
             "The lab searches two modern public documents, printed in full "
             "under the table, for a question mark: the Supreme Court "
             "opinion <em>Stanley v. City of Sanford</em>, 606 U.S. 46 "
             "(2025), and the Census Bureau story &ldquo;U.S. Population "
             "Aging as Nation Turns 250&rdquo; of 9 April 2026. In 1,723 "
             "words they have none. Formal writing hardly holds a question "
             "at all."),
            ("p",
             "That gap is the lesson in small. A learner who reads only "
             "reports and textbooks will almost never see the form they "
             "most need when they talk, and no count on Austen can replace "
             "hearing real questions asked aloud."),
            ("h3", "How to use this"),
            ("p",
             "Use the rule. Expect to hear many questions that break it, "
             "and learn the four kinds. Treat the 53.3% as a warning about "
             "counting, not about the rule."),
        ],
    },
]
