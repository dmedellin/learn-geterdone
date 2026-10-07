# -*- coding: utf-8 -*-
"""Lesson two of the word-order course: where the frequency adverb goes."""

LESSONS = [
    {
        "slug": "where-the-adverb-goes",
        "module": "The small word that has a home of its own",
        "title": "Where the Adverb Goes",
        "one_line": "Words like always and never sit in the middle of the verb, and a count shows how often.",
        "standard": (
            "Finish when you can place always, never, often and the words "
            "like them in the right place, and say which cases the rule does not cover.",
            "You should be able to state the three places a frequency word "
            "can sit in the middle of a sentence, say how often that held "
            "on a whole novel, and name each group of sentences that fell "
            "outside it.",
        ),
        "summary": (
            "Learners often put <em>always</em> and <em>never</em> where "
            "their own language would: at the end, or before the subject. "
            "English has a favourite home for them. A word that tells how "
            "often, called a frequency <dfn>adverb</dfn>, sits in the middle "
            "of the verb phrase: before the main verb, after the first "
            "helping verb, or after <em>be</em>. On <em>Pride and "
            "Prejudice</em> this held for 81.8% of 577 cases. The other "
            "105 fall into five named groups, and one of them is not a "
            "failure at all."
        ),
        "key_label": "The three middle places, and the score",
        "key": [
            "before the main verb    she always knew",
            "after a helping verb    she has always known",
            "after be                she is always late",
            "",
            "577 cases in the novel",
            "in a middle place     472   81.8%",
            "elsewhere             105   18.2%",
        ],
        "concepts_intro": "Three ideas carry this lesson.",
        "concepts": [
            (
                "The middle is the favourite, not the only place",
                "English lets a frequency word sit at the start of a "
                "sentence or at the end, and some of them do so often. But "
                "the middle is the place most of them choose. The rule here "
                "is only about the middle, and it names exactly three spots. "
                "That is a rule you can apply to a sentence you have never "
                "seen, and a count can tell you how often it holds.",
            ),
            (
                "The score depends on what you count as a case",
                "A word such as <em>still</em> or <em>already</em> is not "
                "always a frequency word. <em>Still</em> can mean "
                "<em>quiet</em>, and <em>already</em> can tell you about "
                "time, not about how often. Those uses land in the misses "
                "without being a mistake of place. So 81.8% is, if anything, "
                "a little low for the true frequency words alone. We cannot "
                "say by how much.",
            ),
            (
                "The misses are five groups, and the largest is not a failure",
                "Of the 105 cases outside the rule, 51 are words the "
                "tool did not know, 23 sit in a phrase such as "
                "<em>never in my life</em>, 10 are at the end, 7 are at the "
                "start, and 14 are other. The first two are not mistakes in "
                "place. Only the last three are cases of a different "
                "place, and they total 31.",
            ),
        ],
        "steps_title": "Putting a frequency word",
        "steps_intro": "To put the word in the right place, do this.",
        "steps": [
            (
                "Find the verb phrase",
                "That is the main verb and any helping verbs before it: "
                "<em>knew</em>, or <em>has known</em>, or <em>is</em>.",
            ),
            (
                "With be, put the word after it",
                "<em>She is always late. They were never ready.</em> The "
                "word <em>be</em> is the exception to the first place, and "
                "it is the one most learners miss.",
            ),
            (
                "With a helping verb, put the word after the first one",
                "<em>She has always known. They would never agree.</em> Not "
                "before the helping verb, and not after the main verb.",
            ),
            (
                "With no helping verb, put the word before the main verb",
                "<em>She always knew. He often asked.</em> If you want to "
                "stress the word, English can move it, and then the sentence "
                "sounds like a choice.",
            ),
        ],
        "lab": ("english", {
            "mode": "adverbs",
            "panel_title": "Score the middle places yourself",
            "panel_intro": (
                "The lab scans a shorter stretch of the same novel and "
                "finds each frequency word in it. It checks whether the "
                "word sits before the main verb, after the first helping "
                "verb, or after <em>be</em>, using the verb forms printed "
                "beside the passage. The first box is the hit rate. The "
                "other boxes count each group of misses. The figure will "
                "not match the 81.8% for the whole novel, because this is a "
                "smaller passage. The text is 1810s English, so a miss may "
                "be a habit of that time."
            ),
        }),
        "read_title": "The 105 cases outside the middle",
        "read_intro": (
            "Out of 577 cases, 105 were not in a middle place. Here is "
            "what they were."
        ),
        "worked": {
            "title": "Five groups of misses",
            "intro": [
                "The counts below are counts of cases, out of 105.",
            ],
            "lines": [
                "word not in the printed list      51",
                "  (the tool cannot tell the verb)",
                "inside a phrase: never in my life 23",
                "at the end of the clause          10",
                "at the start of the clause         7",
                "other                             14",
            ],
            "after": [
                "The largest group is a limit of the tool. The word list "
                "does not hold some of the verbs Austen used, so the tool "
                "cannot say where the verb is, and it counts the case as a "
                "miss. This says nothing about where the adverb sat.",
                "The second group, 23 cases, is a frequency word inside a "
                "phrase, such as <em>never in my life</em>. The rule did "
                "not mean to cover these.",
                "Only 17 cases, the end and the start, are plain examples "
                "of a frequency word in a different place. The 14 &ldquo;other&rdquo; "
                "cases include the senses of <em>still</em> and "
                "<em>already</em> that are not about how often. We did not "
                "read all 14, so we do not claim to know how many are real "
                "differences in place.",
            ],
        },
        "note": (
            "A rule that holds 81.8% of the time and has a clear list of "
            "reasons for the rest is a good rule. What you cannot say is that "
            "82 sentences in 100 sound natural, because the count is about "
            "where the word sits and not about how a sentence sounds."
        ),
        "mistakes": [
            (
                "Putting the word at the end",
                "<em>She knew always</em> is a common mistake. In English "
                "the end is open to some words, such as <em>often</em> or "
                "<em>sometimes</em>, but for <em>always</em> and "
                "<em>never</em> the middle is the normal place.",
            ),
            (
                "Putting the word between the verb and its object",
                "<em>She knew always the answer</em> breaks two rules. The "
                "verb and what it acts on stay next to each other in "
                "English, and the frequency word goes before them.",
            ),
            (
                "Forgetting that be works differently",
                "With <em>be</em> the word comes after: <em>she is "
                "always</em>. With every other verb it comes before. Learn "
                "it as one short list: after <em>be</em>, after the first "
                "helping verb, before any other.",
            ),
        ],
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "Which sentence puts <em>always</em> where the rule says?",
                "a": [
                    "<em>She is always late</em>",
                    "<em>She is late always</em>",
                    "<em>Always she is late</em>",
                    "<em>She late is always</em>",
                ],
                "c": 0,
                "why": (
                    "After <em>be</em>. The other orders are possible in "
                    "special cases, but they are not the middle place the "
                    "rule describes."
                ),
            },
            {
                "q": "The largest group of misses has 51 cases. What is it?",
                "a": [
                    "Words the tool did not know",
                    "Words at the end of the clause",
                    "Words at the start of the clause",
                    "Words in the wrong place",
                ],
                "c": 0,
                "why": (
                    "The verb after the word was not in the printed list, so "
                    "the tool could not tell where the verb was. It is a "
                    "limit of the tool."
                ),
            },
            {
                "q": "Why might 81.8% be too low a figure for true frequency words?",
                "a": [
                    "<em>Still</em> and <em>already</em> have other senses that were counted as misses",
                    "The novel has too many commas",
                    "Frequency words cannot be counted",
                    "The rule has no middle place",
                ],
                "c": 0,
                "why": (
                    "Those words were counted, but in some uses they do not "
                    "tell how often. The misses include them without being "
                    "errors of place."
                ),
            },
            {
                "q": "Why does the course measure on a novel and not on a modern court opinion?",
                "a": [
                    "The modern texts have about 4.4 times fewer frequency words",
                    "Court opinions have no verbs",
                    "Novels never use <em>be</em>",
                    "Modern texts are not free to use",
                ],
                "c": 0,
                "why": (
                    "Formal modern writing has about 4.4 times fewer of these "
                    "words per thousand than Austen. There is too little to "
                    "measure. The documents are free to use."
                ),
            },
        ],
        "body": [
            ("p",
             "Ask a learner to say <em>I always drink tea</em> and you may "
             "hear <em>I drink always tea</em>, or <em>Always I drink "
             "tea</em>. Both are understood. Neither is what a speaker would "
             "choose. English has a favourite place for words that tell "
             "how often, and this lesson counts how favourite it is."),
            ("h3", "The rule"),
            ("p",
             "Take the words <em>always, usually, often, sometimes, never, "
             "ever</em> and their kind. In the middle of a sentence they have "
             "three places:"),
            ("ol", [
                "Before the main verb: <em>she always knew</em>.",
                "After the first helping verb: <em>she has always known</em>.",
                "After <em>be</em>: <em>she is always late</em>.",
            ]),
            ("p",
             "A speaker of Spanish may find the first one close to home. "
             "A speaker of Japanese or Korean, where the verb comes last, "
             "may expect the word near the front of the whole clause. A "
             "speaker of Arabic or Mandarin has other habits again. The "
             "rule is the same for everyone, and so is the count."),
            ("h3", "The score"),
            ("p",
             "On <em>Pride and Prejudice</em>, novel text only, the rule "
             "found 577 cases. In 472 of them, which is 81.8%, the word "
             "sat in one of the three places. In the other 105 it did not."),
            ("h3", "What the 105 were"),
            ("ul", [
                "<strong>51 had a word outside the list.</strong> The tool "
                "reads a printed list of verb forms. When the verb was not "
                "in it, the tool could not find the middle. These are not "
                "cases of place at all.",
                "<strong>23 were inside a phrase.</strong> <em>Never in my "
                "life</em> is a fixed unit. The rule is about single words.",
                "<strong>10 were at the end and 7 at the start.</strong> "
                "These are real cases of the word elsewhere. English allows "
                "this, and it often adds weight to the word.",
                "<strong>14 were other.</strong> This group includes uses of "
                "<em>still</em> and <em>already</em> that have nothing to do "
                "with how often. They were counted because the tool matches "
                "the spelling, and not the meaning.",
            ]),
            ("p",
             "So the count of true places other than the middle may be "
             "close to 17. We say that carefully: the 14 were not all read, "
             "and the 51 are unknown, because the tool could not see the "
             "verb. A fair statement is that the rule held in 81.8% of "
             "cases and that most of the rest are not failures of place."),
            ("h3", "Why a novel, and what it costs"),
            ("p",
             "Two modern public documents, a US Supreme Court opinion and a "
             "Census Bureau story, were also measured. They carry about 4.4 "
             "times fewer frequency words per thousand than Austen does. A "
             "reader who learns from formal modern writing meets very few "
             "of these words, and the middle place is a rule of speech and "
             "story more than of reports."),
            ("p",
             "The cost is age. This is 1810s English, and a few of the "
             "misses may be habits that have changed. We cannot tell which "
             "from this count alone."),
        ],
    },
]
