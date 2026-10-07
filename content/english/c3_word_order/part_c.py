# -*- coding: utf-8 -*-
"""Lesson three of the word-order course: the rule that could not be made to work.

This lesson ships STATED and not computed, and says so. The rule was tried on
printed text, scored 55.4%, and its largest group of misses is not a failure of
the rule. A tile that looked like a measurement would claim more than we know.
"""

LESSONS = [
    {
        "slug": "asking-a-question",
        "module": "The one rule we could not make work",
        "title": "Asking a Question",
        "one_line": "The rule for questions is real, our count of it was poor, and this lesson says so.",
        "standard": (
            "Finish when you can build a question in English, and say why "
            "the number printed for this rule is stated and not computed.",
            "You should be able to put a helping verb before the subject, "
            "add do when there is no other helping verb, name the kinds of "
            "question the rule did not catch, and explain why a poor score "
            "on an old novel is not a reason to doubt the rule.",
        ),
        "summary": (
            "Every other lesson in this course states a rule, scores it on "
            "printed text and shows what is left. This one is different. The "
            "rule for questions is old and well known: a helping verb moves "
            "in front of the subject, and <em>do</em> is added if there is "
            "none. Scored on <em>Pride and Prejudice</em> it matched 55.4% of "
            "the questions. The largest group of misses was not a failure of "
            "the rule, and we could not separate the groups by machine. So the "
            "figures here are <strong>stated</strong>, not computed, and "
            "the lesson explains why that is the honest choice."
        ),
        "key_label": "The rule, and the figure we state",
        "key": [
            "you know       ->  do you know?",
            "she went       ->  did she go?",
            "she can go     ->  can she go?",
            "she went where ->  where did she go?",
            "",
            "rule matched 55.4% of questions",
            "STATED, not computed in your browser",
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
                "the end, or by an ending on the verb. English moves "
                "words, and that is why the rule is worth stating.",
            ),
            (
                "Scoring it was a different matter",
                "On <em>Pride and Prejudice</em> the rule matched 55.4% of "
                "the questions. That is too low to call the rule good, and "
                "too high to call it wrong. Where the other lessons found a "
                "small set of named misses, this one found a spread of "
                "different kinds, and the largest of them is a result of "
                "how people write, not of how English builds questions.",
            ),
            (
                "A figure you cannot rebuild should be called what it is",
                "The other labs recompute their figures in your browser from "
                "a passage you can read. This one does not, and the page "
                "says so. The reason is that deciding what counts as a "
                "question in print, and which group each miss belongs to, "
                "came from reading the cases. A tile that looked like a "
                "measurement would claim more than we know. We state the "
                "figure, give its source, and let you judge it.",
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
                "misses, and the next section names them.",
            ),
        ],
        "lab": ("english", {
            "mode": "questions",
            "panel_title": "The figures for questions, as stated",
            "panel_intro": (
                "The boxes in this panel are quoted from the measurement on "
                "the whole novel. They are not recomputed in your browser, "
                "and the panel is marked that way. The first box is the "
                "55.4% hit rate. The second is the share of the misses that "
                "begin with a joining word such as <em>and</em> or "
                "<em>but</em>. Both come from 1810s English, and the way "
                "people ask questions has changed since."
            ),
        }),
        "read_title": "What the rule did not catch",
        "read_intro": (
            "Questions that did not follow the rule fell into four groups. "
            "The first is the largest by a long way."
        ),
        "worked": {
            "title": "Four kinds of question that skipped the rule",
            "intro": [
                "Only the first share was measured. The other three are "
                "named, in the order of their size, without a share.",
            ],
            "lines": [
                "joining word first         45% of misses",
                "  And what ...  But why ...",
                "a name or title first",
                "  Mr. Darcy, do you ...",
                "statement order",
                "  You know him?",
                "no do, in older English",
                "  What say you?",
            ],
            "after": [
                "The first group is a question that begins with <em>and</em> "
                "or <em>but</em>. A check that looks for the helping verb "
                "at the front misses these, because a joining word stands "
                "first. In the cases we read, the rest of the question "
                "did follow the rule. We did not read all of them.",
                "The second group is a name or title at the start, called "
                "a vocative. The third is a question with the order of a "
                "statement, and tone alone makes it a question. The fourth "
                "is a form older English used without <em>do</em>.",
            ],
        },
        "note": (
            "Only the 45% was counted. We do not print shares for the other "
            "three groups because we did not count them. Writing a number we "
            "had not measured would be a bigger fault than printing a low one."
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
                "55.4% on an old novel is a fact about the novel and about "
                "our count. Some of the misses are questions that follow the "
                "rule after a joining word. Do not drop the rule. Do not "
                "lean on the figure either.",
            ),
        ],
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "How do you turn <em>she went</em> into a question with the standard rule?",
                "a": [
                    "<em>Did she go?</em>",
                    "<em>Went she?</em>",
                    "<em>She did went?</em>",
                    "<em>Do she went?</em>",
                ],
                "c": 0,
                "why": (
                    "There is no helping verb, so <em>do</em> is added in the "
                    "past form, and the main verb goes back to its plain form."
                ),
            },
            {
                "q": "Why is the figure for questions stated and not computed?",
                "a": [
                    "Deciding what counts as a question and sorting the misses needed a person to read them",
                    "English questions cannot be counted",
                    "The novel has no questions",
                    "The rule is known to be false",
                ],
                "c": 0,
                "why": (
                    "A box that recomputed a number would look like a "
                    "measurement of the rule. It would claim more than we "
                    "know."
                ),
            },
            {
                "q": "What was the largest group among the misses?",
                "a": [
                    "Questions that began with a joining word, such as <em>and</em> or <em>but</em>",
                    "Questions with no verb",
                    "Questions spoken by a child",
                    "Questions in the past",
                ],
                "c": 0,
                "why": (
                    "It was 45% of the misses. The joining word stands first, "
                    "so a check at the front of the sentence misses it."
                ),
            },
            {
                "q": "What did the modern public documents show about questions?",
                "a": [
                    "None in 1,844 words, while Austen has one in about every 256",
                    "More than Austen",
                    "About the same as Austen",
                    "Only questions with <em>do</em>",
                ],
                "c": 0,
                "why": (
                    "A court opinion and a Census Bureau story, both free to "
                    "use, carry no questions. Formal writing barely holds the "
                    "form you most need in speech."
                ),
            },
        ],
        "body": [
            ("p",
             "This is the one lesson where the method did not work, and the "
             "failure is part of what it teaches."),
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
             "The rule was scored on <em>Pride and Prejudice</em>, and it "
             "matched 55.4% of the questions. For a rule that is taught "
             "first, that is a poor figure. It is worth asking why."),
            ("h3", "What the misses looked like"),
            ("ul", [
                "<strong>A joining word first, 45% of the misses.</strong> "
                "<em>And what do you mean? But why did she go?</em> A check "
                "for the helping verb at the front misses these. In the "
                "cases we read, the question follows the rule after the "
                "joining word.",
                "<strong>A name or title first.</strong> <em>Mr. Darcy, do "
                "you know her?</em> The name comes before the helping verb "
                "so a check at the front misses it.",
                "<strong>Statement order.</strong> <em>You know him?</em> "
                "Tone alone makes it a question. This is a real exception, "
                "and it is common in speech today.",
                "<strong>No do, in older English.</strong> <em>What say "
                "you?</em> Austen wrote some questions in a form that has "
                "gone out of use.",
            ]),
            ("p",
             "Only the first has a measured share. We did not count the "
             "other three. We name them because we read them, and we leave "
             "out their size because we did not measure it."),
            ("h3", "Why this section is stated, not computed"),
            ("p",
             "The other two labs in this course find a rule's hits and "
             "misses by machine, from a passage on the page. A question rule "
             "would need the same. But what counts as a question in print "
             "is hard to decide by machine, and the groups of misses came "
             "from reading them. A box that showed a number would look "
             "like the other boxes, and it would not be one."),
            ("p",
             "So the figures here are quoted from a single run on the whole "
             "novel, and the lab says so. If you wish to doubt them, doubt "
             "the 55.4% most. It is a poor figure for a rule that is "
             "sound, and the reason is the way people write, not the rule."),
            ("h3", "What the modern documents show"),
            ("p",
             "Two modern public documents, a US Supreme Court opinion and a "
             "Census Bureau story, were read for questions. In 1,844 words "
             "they have none. Austen has one in about every 256. Formal "
             "writing hardly holds a question at all."),
            ("p",
             "That gap is the lesson in small. A learner who reads only "
             "reports and textbooks will almost never see the form they "
             "most need when they talk, and no count on Austen can replace "
             "hearing real questions asked aloud."),
            ("h3", "How to use this"),
            ("p",
             "Use the rule. Expect to hear many questions that break it, "
             "and learn the four kinds. Treat the 55.4% as a warning about "
             "counting, not about the rule."),
        ],
    },
]
