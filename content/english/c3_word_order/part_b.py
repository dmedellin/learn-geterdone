# -*- coding: utf-8 -*-
"""Lesson two of the word-order course: where the frequency adverb goes.

The lab scores the middle-place rule on 120 lines from the novel, each printed
in the table with its verdict, and counts the same adverbs in two modern public
documents printed beside them. Figures from a run over the whole novel are
quoted and labelled as quoted.
"""

LESSONS = [
    {
        "slug": "where-the-adverb-goes",
        "module": "The middle place",
        "title": "Where the Adverb Goes",
        "one_line": "Words like always and never sit in the middle of the verb, and a count shows how often.",
        "standard": (
            "Finish when you can place always, never, often and the words "
            "like them in the right place, and say which cases the rule does not cover.",
            "You should be able to state the three places a frequency word "
            "can sit in the middle of a sentence, read how often that held "
            "on the 120 lines printed with this lesson, and name the kinds of "
            "line that fell outside it.",
        ),
        "summary": (
            "Learners often put <em>always</em> and <em>never</em> where "
            "their own language would: at the end, or before the subject. "
            "English has a favourite home for them. A word that tells how "
            "often, called a frequency <dfn>adverb</dfn>, sits in the middle "
            "of the verb phrase: before the main verb, after the first "
            "helping verb, as Helping Verbs calls them &mdash; <em>have</em>, "
            "<em>be</em> and <em>will</em>, and their kind, <em>can, could, "
            "do, did, must</em> &mdash; or after <em>be</em> on its own. On "
            "120 lines from <em>Pride and Prejudice</em>, printed with this "
            "lesson, that held in 85, which is 70.8%. On the whole novel, in "
            "a run this page cannot repeat, it held for 81.8% of 577 cases, "
            "and the misses fall into five named groups, the largest of which "
            "is not a failure at all."
        ),
        "key_label": "The three middle places, and the score",
        "key": [
            "before the main verb    she always knew",
            "after a helping verb    she has always known",
            "after be                she is always late",
            "",
            "120 printed lines: 85 in the middle    70.8%",
            "whole novel, quoted: 472 of 577        81.8%",
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
                "seen, and a count can tell you how often it holds. The "
                "printed list also carries <em>still</em>, <em>already</em> "
                "and <em>soon</em>, which tell when rather than how often; "
                "they take the same middle places, and the lab scores them "
                "with the rest.",
            ),
            (
                "The score depends on what you count as a case",
                "A word such as <em>still</em> or <em>already</em> is not "
                "always a frequency word. <em>Still</em> can mean "
                "<em>quiet</em>, and <em>still better</em> is about degree, "
                "not time. <em>How soon</em> and <em>as soon as</em> are "
                "phrases of their own. Those uses land in the misses "
                "without being a mistake of place. So 70.8% on the lines, "
                "and 81.8% on the novel, are if anything a little low for the "
                "true frequency words alone. The menu above the table scores "
                "one word at a time, and <em>always</em> alone reaches 15 of "
                "16.",
            ),
            (
                "The misses are named groups, and the largest is not a failure",
                "In the whole-novel run, of the 105 cases outside the rule, 51 "
                "are verbs the tool did not know, 23 sit in a phrase such as "
                "<em>never in my life</em>, 10 are at the end of their "
                "<dfn>clause</dfn>, the group of words built around one verb, "
                "7 are at its start, and 14 are other. The first two are not "
                "mistakes in place. Only the last three are cases of a "
                "different place, and they total 31. The lab on this page "
                "sorts its 35 misses two ways: a <dfn>preposition</dfn> "
                "follows, a small word such as <em>in</em>, <em>to</em> or "
                "<em>with</em>, or something else does. It prints every line "
                "so you can sort the rest by eye.",
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
                "verb <em>be</em> is the exception to the first place, and "
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
                "The table holds 120 lines from the novel, each cut around "
                "one of eight adverbs. For each line the lab reads the word "
                "before the adverb and the word after it, against a list of "
                "the 249 verb forms the lines contain and 25 helping verbs, "
                "which the page carries. The rule holds when a helping verb or <em>be</em> "
                "comes before the adverb, or a verb comes after it. The "
                "first two boxes are the hit rate. The next two sort the "
                "misses: a preposition from the lab&rsquo;s short list of "
                "seven, <em>in, at, on, of, to, for, with</em>, follows the "
                "adverb, as in <em>never in my life</em>, or something else "
                "does, and the verdict beside each line lets you sort the "
                "something else yourself. "
                "The first menu scores one adverb at a time. "
                "The last two boxes count the same adverbs in the two modern "
                "documents printed below the table: the Supreme Court "
                "opinion <em>Stanley v. City of Sanford</em>, 606 U.S. 46 "
                "(2025), and the Census Bureau story &ldquo;U.S. Population "
                "Aging as Nation Turns 250&rdquo; (9 April 2026). The text "
                "is 1810s English, so a miss may be a habit of that time."
            ),
        }),
        "read_title": "The cases outside the middle",
        "read_intro": (
            "On the whole novel, 105 of 577 cases were not in a middle place. "
            "Here is what they were, and beside them the 35 misses on the "
            "lines printed with this lesson."
        ),
        "worked": {
            "title": "Five groups of misses, and two boxes",
            "intro": [
                "The first block is quoted from the run over the whole novel, "
                "which this page cannot repeat; the counts are of cases, out "
                "of 105. The second block is what the lab finds on the 120 "
                "printed lines, out of 35 misses.",
            ],
            "lines": [
                "the whole novel, quoted",
                "verb not in the tool's list       51",
                "  (the tool cannot tell the verb)",
                "inside a phrase: never in my life 23",
                "at the end of the clause          10",
                "at the start of the clause         7",
                "other                             14",
                "",
                "the 120 printed lines, counted on the page",
                "a preposition follows              6",
                "  never in my life, still to think",
                "something else between            29",
                "  as soon as, more than usually, still better",
            ],
            "after": [
                "The largest group in the novel is a limit of the tool. The "
                "word list does not hold some of the verbs Austen used, so the "
                "tool cannot say where the verb is, and it counts the case as a "
                "miss. This says nothing about where the adverb sat. The same "
                "thing happens five times on this page: <em>they always "
                "contrived</em>, <em>my letters sometimes convey</em>, "
                "<em>who still resides</em>, <em>I sometimes amuse myself</em> "
                "and <em>ladies sometimes condescend</em> are in the right "
                "place, and the scan does not know the verb.",
                "The second group, 23 cases in the novel and 6 on this page, "
                "is a frequency word inside a phrase, such as <em>never in "
                "my life</em>. The rule did not mean to cover these.",
                "Only 17 cases in the novel, the end and the start, are plain "
                "examples of a frequency word in a different place. The 14 "
                "&ldquo;other&rdquo; cases include the senses of <em>still</em> "
                "and <em>already</em> that are not about how often. We did not "
                "read all 14, so we do not claim to know how many are real "
                "differences in place. On this page you can read all 29 of "
                "the <em>something else</em> lines, and they sort into seven "
                "kinds: five verbs the list does not hold; three <em>as soon "
                "as</em>; five adverbs before an adjective, as in <em>more "
                "than usually insolent</em> and <em>still better</em>; four at "
                "the end of their clause, <em>what is strong already</em>; "
                "five at the start of one, <em>and still they admired "
                "her</em>; six with a word after the adverb that the "
                "lab&rsquo;s short list does not hold, <em>often without</em>, "
                "<em>so soon after</em>, <em>how soon</em>; and one "
                "<em>Sometimes.</em> on its own.",
            ],
        },
        "note": (
            "A rule that holds in seven lines of ten here, in eight of ten on "
            "the whole novel, and has a clear list of reasons for the rest is "
            "a good rule. What you cannot say is that seven sentences in ten "
            "sound natural, because the count is about where the word sits "
            "and not about how a sentence sounds."
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
                "always</em>. With every other main verb it comes before. "
                "Learn it as one short list: after <em>be</em>, after the "
                "first helping verb, before any other.",
            ),
        ],
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "Which sentence puts <em>always</em> where the rule says?",
                "a": [
                    "<em>She is late always</em>",
                    "<em>She is always late</em>",
                    "<em>Always she is late</em>",
                    "<em>She late is always</em>",
                ],
                "c": 1,
                "why": (
                    "After <em>be</em>. The other orders are possible in "
                    "special cases, but they are not the middle place the "
                    "rule describes."
                ),
            },
            {
                "q": "In the whole-novel run, the largest group of misses has 51 cases. What is it?",
                "a": [
                    "Words at the end of the clause",
                    "Words at the start of the clause",
                    "Words in the wrong place",
                    "Verbs the tool did not know",
                ],
                "c": 3,
                "why": (
                    "The verb after the word was not in the tool's list, so "
                    "the tool could not tell where the verb was. It is a "
                    "limit of the tool, and the printed lines show it five "
                    "times."
                ),
            },
            {
                "q": "Why might 70.8% be too low a figure for true frequency words?",
                "a": [
                    "<em>Still</em> and <em>already</em> have other senses that were counted as misses",
                    "The novel has too many commas",
                    "Frequency words cannot be counted",
                    "The rule has no middle place",
                ],
                "c": 0,
                "why": (
                    "Those words were counted, but in some uses they do not "
                    "tell how often: <em>still better</em>, <em>as soon as</em>. "
                    "The misses include them without being errors of place."
                ),
            },
            {
                "q": "What does the lab find when it counts these adverbs in the two modern documents?",
                "a": [
                    "More than in the novel",
                    "None at all",
                    "Two in 1,723 words, about 1.2 per thousand",
                    "Only <em>always</em>",
                ],
                "c": 2,
                "why": (
                    "<em>Stanley v. City of Sanford</em> and the Census Bureau "
                    "story together have 1,723 words and two of these adverbs, "
                    "one <em>often</em> and one <em>still</em>. There is too "
                    "little in formal writing to measure the rule on."
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
             "The lab holds 120 lines from <em>Pride and Prejudice</em>, "
             "each cut around one adverb, and prints every one. In 85 of "
             "them, 70.8%, the adverb sits in one of the three places. In "
             "the other 35 it does not. Word by word the picture differs: "
             "<em>always</em> is in the middle in 15 lines of 16 and "
             "<em>never</em> in 14, while <em>sometimes</em> manages 7 of "
             "16, because it so often opens or closes a clause."),
            ("p",
             "The same rule was once run over the whole novel, novel text "
             "only. It found 577 cases, and in 472 of them, 81.8%, the word "
             "sat in one of the three places. That figure is quoted: no page "
             "can carry the novel. The 120 lines are the part you can check."),
            ("h3", "What the 105 whole-novel misses were"),
            ("ul", [
                "<strong>51 had a verb outside the list.</strong> The tool "
                "reads a list of verb forms. When the verb was not "
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
            ("h3", "What the 35 misses on this page are"),
            ("p",
             "The lab sorts them two ways. Six have a preposition from its "
             "short list straight after the adverb: <em>never in my life</em>, "
             "<em>still to think</em>, <em>so often to Miss Watson&rsquo;s</em>. "
             "The other 29 it calls <em>something else between</em>, and they "
             "are the whole-novel groups in small. Five are a verb the list "
             "does not hold: <em>they always contrived</em>, <em>who still "
             "resides</em>. Three are <em>as soon as</em>. Five put the "
             "adverb before an adjective rather than a verb: <em>more than "
             "usually insolent</em>, <em>still more interesting</em>, "
             "<em>often absent</em>. Four are at the end of their clause, "
             "<em>and me never</em>, and five at the start of one, <em>and "
             "sometimes the refusal is repeated</em>. Six have a word after "
             "the adverb that the short list does not hold, <em>often without "
             "any attention</em>, <em>so soon after his arrival</em>, or sit "
             "in a phrase of their own, <em>how soon</em>, <em>soon "
             "afterwards</em>. One is the single word <em>Sometimes.</em> "
             "Read the verdict column and you will find very few that a "
             "speaker would call wrong."),
            ("h3", "Why a novel, and what it costs"),
            ("p",
             "The lab also counts the same adverbs, and <em>rarely</em> too, in two modern public "
             "documents, printed in full under the table: the Supreme Court "
             "opinion <em>Stanley v. City of Sanford</em>, 606 U.S. 46 "
             "(2025), and the Census Bureau story &ldquo;U.S. Population "
             "Aging as Nation Turns 250&rdquo; of 9 April 2026. In 1,723 "
             "words they contain two, one <em>often</em> and one "
             "<em>still</em>, which is 1.2 per thousand words. The novel's "
             "577 cases in about 122,400 words, both quoted, come to about "
             "4.7 per thousand. A reader who learns from formal modern "
             "writing meets very few of these words, and the middle place "
             "is a rule of speech and story more than of reports."),
            ("p",
             "The cost is age. This is 1810s English, and a few of the "
             "misses may be habits that have changed. We cannot tell which "
             "from this count alone."),
        ],
    },
]
