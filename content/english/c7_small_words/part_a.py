# -*- coding: utf-8 -*-
"""Lessons one and two of Small Words and Comparisons.

Every figure is read off the lab with labcheck.js --observe.

In, On or At: Time (time_preps, preset all): 109 lines, 103 right, 94.5%.
By kind, from the lab's own table: day 32 of 32; month 5 of 5; year 16 of 16;
season 7 of 7; part of the day 32 lines, 29 right; night, noon or midnight 10
lines, 7 right; festival 3 of 3; clock time 4 of 4. Novel 77 of 79 (97.5%),
play 9 of 13 (69.2%), modern documents 17 of 17 (100.0%). The six misses are
on Sunday night, on the evening (novel), on Thursday night, on Wednesday night,
at evening parties, on the morning of the day (play).

Bigger or More Big (compare, rule A shipped): novel 367 forms, 337 right
(91.8%), 30 wrong; rule B 341 (92.9%). Play 44 of 49 (89.8%) and 45 of 49.
Modern documents 32 of 32 under both. Parts by form in the novel: one part 268
and 2, two parts 54 and 15, three parts 0 and 18, four or more 0 and 10.

Spoken forms for the orchestrator are in content/spoken/english_c7_small_words.py:
the key lines with a hyphen-initial ending, and the worked lines of lesson two.
"""

LESSONS = [
    {
        "slug": "in-on-at-for-time",
        "module": "Prepositions and particles",
        "title": "In, On or At: Time",
        "one_line": "Three small words, and the kind of time word after them picks which one.",
        "standard": (
            "Finish when you can choose in, on or at for a time phrase by the kind of time word.",
            "You should be able to state the rule in three parts, read its score "
            "off every printed line, name the kinds of line it gets wrong, and "
            "tell a time phrase that takes a small word from one that takes none.",
        ),
        "summary": (
            "You may have been told that <em>in</em> is for long times, "
            "<em>on</em> for days and <em>at</em> for points. The kind of time "
            "word is a better guide. A rule that looks only at that kind is right "
            "on 103 of 109 printed lines. The six lines it gets wrong come in "
            "three kinds, and one of the kinds is a step the rule already takes "
            "for mornings and does not yet take for nights."
        ),
        "key_label": "The rule, and its score on 109 lines",
        "key": [
            "at   a clock time, night, noon, a festival",
            "on   a day, or a named day's morning",
            "in   a month, a year, a season,",
            "     a morning, afternoon or evening",
            "",
            "103 of 109 lines right, 94.5%",
        ],
        "concepts_intro": "Three ideas. The second one is the one learners miss.",
        "concepts": (
            (
                "The kind of time word decides",
                "The lab sorts the time words into eight kinds and gives each "
                "kind one small word. A day takes <em>on</em>: 32 lines, 32 right. "
                "A month, a year or a season takes <em>in</em>: 5, 16 and 7 lines, "
                "all right. A festival and a clock time take <em>at</em>: 3 and 4 "
                "lines, all right. The rule never asks how long the time is.",
            ),
            (
                "A named day beats the part of the day",
                "<em>In the morning</em> is the plain case. Name the day and the "
                "word changes: <em>on Saturday morning</em>, <em>on the following "
                "morning</em>. The lab finds seven lines like this, and the rule "
                "gets all seven. The same idea reaches <em>night</em>, and that is "
                "where the rule is still short.",
            ),
            (
                "Some time words take no small word at all",
                "<em>This morning</em>, <em>last night</em>, <em>every "
                "morning</em>. Nothing comes before them, so there is nothing to "
                "score. The lab lists them under the table and does not count "
                "them as misses.",
            ),
        ),
        "steps_title": "Choosing the small word for a time phrase",
        "steps_intro": "Five questions, in this order.",
        "steps": (
            (
                "Does the phrase begin with this, last, next or every?",
                "Then it takes no small word: <em>this morning</em>, <em>last "
                "night</em>. Stop here.",
            ),
            (
                "Is the time word a clock time, night, noon, midnight or a festival?",
                "Use <em>at</em>: <em>at eight o'clock</em>, <em>at night</em>, "
                "<em>at Christmas</em>. One care: when a day is named before "
                "<em>night</em>, the day wins, as it does for a morning in the "
                "last step, and the phrase is <em>on Sunday night</em>. The "
                "lab's rule stops short of this, and the lesson shows the three "
                "lines it loses.",
            ),
            (
                "Is it the name of a day?",
                "Use <em>on</em>: <em>on Tuesday</em>.",
            ),
            (
                "Is it a month, a year or a season?",
                "Use <em>in</em>: <em>in July</em>, <em>in 2025</em>, <em>in "
                "the summer</em>.",
            ),
            (
                "Is it a morning, an afternoon or an evening?",
                "Use <em>in</em>, unless a day is named or picked out. Then use "
                "<em>on</em>: <em>on Monday morning</em>, <em>on the following "
                "morning</em>.",
            ),
        ),
        "lab": ("english", {
            "mode": "time_preps",
            "source": "all",
            "panel_title": "Score the rule on 109 printed lines",
            "panel_intro": (
                "Each line has <em>in</em>, <em>on</em> or <em>at</em> before a "
                "time word. 79 are from <em>Pride and Prejudice</em> (1813), 13 "
                "from <em>The Importance of Being Earnest</em> (1895) and 17 from "
                "two modern documents. The two older texts are 1813 and 1895 "
                "English; the modern documents are the US Supreme Court opinion "
                "<em>Stanley v. City of Sanford</em>, 606 U.S. 46 (2025), and "
                "the Census Bureau story &ldquo;U.S. Population Aging as Nation "
                "Turns 250&rdquo; (2026). Choose "
                "the lines, then read the table: it shows the kind of time word, "
                "what the rule says and what the writer wrote. The last list "
                "shows time words that have no small word before them."
            ),
        }),
        "read_title": "The six lines the rule misses",
        "read_intro": (
            "The rule is right on 103 of 109 lines. The other six are not six "
            "unrelated cases."
        ),
        "worked": {
            "title": "Seven phrases, each from a different kind of time word",
            "intro": [
                "Every phrase below is one of the printed lines, or the same kind "
                "of line. Name the kind first, then the small word.",
            ],
            "lines": [
                "on Tuesday                a day",
                "in July                   a month",
                "in 2025                   a year",
                "at eight o'clock          a clock time",
                "at night                  night",
                "in the evening            part of a day",
                "on the following morning  a day, picked out",
            ],
            "after": [
                "The last phrase is the one that needs care. <em>Morning</em> "
                "alone takes <em>in</em>. <em>The following morning</em> names "
                "one particular day, and a particular day takes <em>on</em>.",
                "Now the six misses. Three are <em>night</em> with a day name: "
                "<em>on Sunday night</em> in the novel, <em>on Thursday night</em> "
                "and <em>on Wednesday night</em> in the play. The rule says "
                "<em>at</em> for <em>night</em>, and the writers named the day. "
                "It is the step that already works for mornings, applied to "
                "nights. Two are an evening or a morning picked out by words "
                "that come after it: <em>on the evening before my going</em> and "
                "<em>on the morning of the day</em>. The rule reads only the words "
                "before the time word, so it cannot see them. The last, <em>at "
                "evening parties</em>, is not a time phrase: <em>evening</em> "
                "describes the parties.",
            ],
        },
        "note": (
            "The lab reads only the words between the small word and the time "
            "word. It is a count of spellings, not of meanings, and it leaves "
            "out <em>may</em>, which is also a helping verb. The two older texts "
            "are 1813 and 1895 English, and they give 92 of the 109 lines; "
            "the 17 modern lines are 16 years and one month, so they test the "
            "<em>in</em> and year part of the rule far more than the rest."
        ),
        "mistakes": (
            (
                "Putting in before every part of the day",
                "<em>In the morning</em> is right, so <em>in Monday morning</em> "
                "feels right. It is not: the day wins, and the phrase is "
                "<em>on Monday morning</em>. In the table, seven part-of-day lines "
                "say <em>on</em> because a day is named or picked out.",
            ),
            (
                "Choosing by how long the time is",
                "A festival lasts days and takes <em>at</em>: <em>at "
                "Christmas</em>. An afternoon lasts hours and takes <em>in</em>: "
                "<em>in the afternoon</em>. Length does not choose the word. The "
                "kind of time word does.",
            ),
            (
                "Adding a small word to every time phrase",
                "<em>This morning</em> and <em>last night</em> take none. The "
                "novel has 13 lines of <em>this morning</em> and 9 of <em>last "
                "night</em>, and every one is bare. A small word added to them "
                "(<em>in this morning</em>) is the error.",
            ),
        ),
        "quiz_title": "Check yourself",
        "quiz": (
            {
                "q": "Which small word goes before <em>Friday morning</em>?",
                "a": ["in", "on", "at", "for"],
                "c": 1,
                "why": (
                    "<em>On</em>. A named day beats the part of the day, so "
                    "<em>on Friday morning</em>. <em>In</em> is for a morning "
                    "that no day is named for, and <em>at</em> is for clock "
                    "times, <em>night</em> and festivals."
                ),
            },
            {
                "q": "Which of these kinds of time word had lines the rule got wrong?",
                "a": ["a month", "a year", "a day name", "a part of the day"],
                "c": 3,
                "why": (
                    "A part of the day: 32 lines, 29 right. The rule was right on "
                    "all 5 month lines, all 16 year lines and all 32 day lines."
                ),
            },
            {
                "q": "Which of these is wrong?",
                "a": ["in this morning", "at five o'clock",
                      "on the following morning", "in the summer"],
                "c": 0,
                "why": (
                    "<em>This morning</em> takes no small word. The other three "
                    "follow the rule: a clock time takes <em>at</em>, a named "
                    "morning takes <em>on</em>, a season takes <em>in</em>."
                ),
            },
            {
                "q": "Three of the six misses are <em>on Sunday night</em> and its "
                     "kind. What change to the rule would fix them?",
                "a": [
                    "Use <em>in</em> for every <em>night</em>",
                    "Drop <em>at</em> before <em>night</em>",
                    "Let a named day beat <em>night</em>, as it beats <em>morning</em>",
                    "Count them as the writers' errors",
                ],
                "c": 2,
                "why": (
                    "The rule already lets a day name beat a morning or an "
                    "evening. Letting it beat <em>night</em> too fixes all three. "
                    "<em>At</em> is right on the other seven lines of this kind, "
                    "six <em>at night</em> and one <em>at midnight</em>, so "
                    "dropping it would lose them, and the writers were not wrong."
                ),
            },
        ),
        "body": [
            ("p",
             "A <dfn>preposition</dfn> is a small word that stands in front of a "
             "noun and joins it to the rest of the sentence. <em>In</em>, "
             "<em>on</em> and <em>at</em> are three of the commonest, and before "
             "a time word they are the three that learners most often mix up."),
            ("p",
             "The rule you are usually given is about length: <em>in</em> for long "
             "times, <em>on</em> for days, <em>at</em> for points. Look at what "
             "it does with <em>Christmas</em>, which lasts days and takes "
             "<em>at</em>, and <em>the afternoon</em>, which lasts hours and "
             "takes <em>in</em>. Length is not what is deciding."),
            ("h3", "The kind of time word"),
            ("p",
             "Sort the time word instead. The lab does, into eight kinds. A day "
             "takes <em>on</em>. A month, a year, a season or a morning takes "
             "<em>in</em>. A clock time, <em>night</em>, <em>noon</em>, "
             "<em>midnight</em> or a festival takes <em>at</em>. That is the "
             "whole rule, and you can say it in the time it takes to read it."),
            ("p",
             "Run it on 109 printed lines and it is right on 103, which is "
             "94.5%. The novel gives 77 right of 79. The play gives 9 right "
             "of 13, and the modern documents 17 of 17. Six of the eight kinds "
             "are right on every line: day, month, year, season, festival and clock "
             "time. The two that are not are the ones worth reading."),
            ("h3", "A day beats the part of the day"),
            ("p",
             "<em>Morning</em>, <em>afternoon</em> and <em>evening</em> take "
             "<em>in</em>, and the table has 22 lines that show it: <em>in the "
             "evening</em>, <em>early in the morning</em>. But the table also "
             "has seven lines where one of them takes <em>on</em>: <em>on "
             "Saturday morning</em>, <em>on Wednesday morning</em>, <em>on the "
             "following morning</em>, <em>on the third morning</em>. In each, a "
             "day is named or picked out, and the day decides. The rule has a "
             "step for this and gets all seven."),
            ("h3", "What is left over"),
            ("p",
             "Six lines are wrong, and they belong to three kinds. Three put "
             "<em>on</em> before <em>night</em> with a day name: <em>on Sunday "
             "night</em>, <em>on Thursday night</em>, <em>on Wednesday night</em>. "
             "This is the same step again. If a named day beats a morning, it "
             "beats a night, and that fixes three lines with no cost, because "
             "<em>at</em> is still right on the other seven lines of this kind, "
             "six of them <em>at night</em> and one <em>at midnight</em>."),
            ("p",
             "Two lines pick the evening or the morning out by words that come "
             "after it: <em>on the evening before my going</em>, <em>on the "
             "morning of the day</em>. The lab reads only what comes before the "
             "time word, so it cannot see these. A person reads the whole "
             "phrase, and the whole phrase names one day. The sixth, <em>at "
             "evening parties</em>, is not a time phrase at all."),
            ("h3", "Time words with no small word"),
            ("p",
             "Below the table the lab lists time words that have nothing before "
             "them: <em>the next morning</em> 17 times in the novel, <em>this "
             "morning</em> 13, <em>last night</em> 9. They are not scored, "
             "because there is no small word to be right or wrong. If you add "
             "one, you have made the error."),
            ("p",
             "Two limits. The lab counts spellings and not meanings, so it "
             "cannot tell you the right word for a phrase that is not on its "
             "list. And 92 of the 109 lines come from texts written in 1813 and "
             "1895. The modern lines are 17 of the 109, and 16 of those are a "
             "year. They agree with the rule, but they test only a corner of it."),
        ],
    },
    {
        "slug": "bigger-or-more-big",
        "module": "Making a comparison",
        "title": "Bigger or More Big",
        "one_line": "Count the parts in the adjective, and one rule picks the form on nine lines in ten.",
        "standard": (
            "Finish when you can choose -er or more for an adjective by counting its parts.",
            "You should be able to count the parts, apply the rule to an "
            "adjective you have not seen, read the rule's score off every printed "
            "comparison, and name the adjectives of two parts that the novel gives -er "
            "that a modern writer would give more.",
        ),
        "summary": (
            "A comparison of an <dfn>adjective</dfn> is made with <em>-er</em> or with "
            "<em>more</em>, and books say that short words take <em>-er</em> and long words take "
            "<em>more</em>. Counting the parts of the word makes that exact. On "
            "the 367 comparisons in the novel, the rule is "
            "right on 337. Reading the 30 it gets wrong shows what an old text "
            "does that a modern one does not."
        ),
        "key_label": "The rule, and its score on the novel",
        "key": [
            "one part         -er, -est     bigger",
            "two parts, -y    -ier, -iest   happier",
            "all the others   more, most     more beautiful",
            "",
            "the novel: 337 of 367 forms, 91.8%",
        ],
        "concepts_intro": "Three ideas. The third is where the 30 wrong forms are.",
        "concepts": (
            (
                "Count the parts, not the letters",
                "A <dfn>part</dfn> is one beat of a word, built round a <dfn>vowel</dfn> "
                "sound: <em>big</em> has one, <em>happy</em> two, "
                "<em>beautiful</em> three. The lab takes the count from "
                "CMUdict, a <dfn>dictionary</dfn> of sounds. Word Stress goes further "
                "into parts; here you only need to count them.",
            ),
            (
                "Three parts or more: more, every time",
                "In the novel, <dfn>adjectives</dfn> of three parts give 18 forms and none "
                "takes <em>-er</em> or <em>-est</em>. Adjectives of four parts or "
                "more give 10 forms with the same result. One part "
                "goes the other way: 268 forms with <em>-er</em> or <em>-est</em> "
                "and only 2 with <em>more</em> or <em>most</em>.",
            ),
            (
                "Two parts is where the choosing is",
                "The novel gives 54 forms of two parts an ending and 15 a "
                "<em>more</em>. The rule takes adjectives of two parts ending in "
                "<em>-y</em> and sends the rest to <em>more</em>, and nearly "
                "all of its mistakes are here.",
            ),
        ),
        "steps_title": "Choosing the form for an adjective in front of you",
        "steps_intro": "Four steps, then one check.",
        "steps": (
            (
                "Say the adjective and count its parts",
                "<em>Big</em> has one. <em>Happy</em> has two. "
                "<em>Beautiful</em> has three.",
            ),
            (
                "One part: add the ending",
                "<em>Big</em> becomes <em>bigger</em> and <em>biggest</em>. The "
                "last letter doubles here as it does in <em>When the Last Letter "
                "Doubles</em>.",
            ),
            (
                "Two parts ending in -y: change the y to i and add the ending",
                "<em>Happy</em> becomes <em>happier</em> and <em>happiest</em>.",
            ),
            (
                "Every other adjective: put more or most in front",
                "<em>More beautiful</em>, <em>most important</em>. The adjective "
                "does not change.",
            ),
            (
                "Check the age of what you are copying",
                "The novel is from 1813. It writes <em>handsomer</em> and "
                "<em>pleasanter</em>. Today's writing, as the lab's modern "
                "lines show, keeps the rule above.",
            ),
        ),
        "lab": ("english", {
            "mode": "compare",
            "source": "austen",
            "rule": "A",
            "panel_title": "Score the rule on every comparison in a text",
            "panel_intro": (
                "Each row is a comparison from a printed text: "
                "the novel (1813), the play (1895) or the two modern documents. "
                "The rule A is the one in this lesson. The rule B also gives "
                "<em>-er</em> to adjectives of two parts ending <em>-ow</em>, "
                "<em>-le</em> or <em>-er</em>. Switch the text and the rule and "
                "read the table: it shows the number of parts, the form the "
                "writer used and the form the rule says."
            ),
        }),
        "read_title": "The 30 forms the rule gets wrong",
        "read_intro": (
            "30 of the novel's 367 forms break rule A. They come in three kinds."
        ),
        "worked": {
            "title": "Four adjectives, one rule, one old habit",
            "intro": [
                "Count the parts, apply the rule, then look at the last line.",
            ],
            "lines": [
                "big        1 part    bigger",
                "happy      2 parts   happier",
                "beautiful  3 parts   more beautiful",
                "handsome   2 parts   more handsome",
                "                     handsomer (1813)",
            ],
            "after": [
                "The last two lines are the largest group of misses. Of the "
                "30 wrong forms, 22 are an adjective of two parts that the novel "
                "gives an ending: <em>handsomest</em> 4, <em>pleasanter</em> 4, "
                "<em>handsomer</em> 3, <em>pleasantest</em> 2, and one each of "
                "<em>commonest</em>, <em>gentlest</em>, <em>minutest</em>, "
                "<em>narrowest</em>, <em>nobler</em>, <em>noblest</em>, "
                "<em>quieter</em>, <em>severest</em> and <em>stupider</em>. "
                "Rule B moves four of them to the right side, those of "
                "<em>gentle</em>, <em>narrow</em> and <em>noble</em>, and "
                "its score is 341 of 367, or 92.9%. The rule that is "
                "right today for <em>handsome</em> and <em>pleasant</em> is "
                "<em>more</em>.",
                "Of the other eight, three are <em>oftener</em>, an <dfn>adverb</dfn>, "
                "and the rule was not built for it. The last five go the other "
                "way: <em>more angry</em>, <em>more likely</em> and <em>most "
                "likely</em> are words of two parts ending in <em>-y</em> that the "
                "novel gives <em>more</em>, and <em>more strange</em> and "
                "<em>most sure</em> are words of one part that it gives "
                "<em>more</em>.",
            ],
        },
        "note": (
            "The lab counts spellings and takes the parts from CMUdict, so it "
            "says nothing about meaning or taste. It cannot show that a modern "
            "writer would choose <em>more handsome</em>: the two modern "
            "documents have 32 forms, all 32 with <em>-er</em> or <em>-est</em> "
            "(a Census Bureau story and a Supreme Court opinion, named in the "
            "lesson, with words such as <em>older</em> and <em>earlier</em>), "
            "so they show only that "
            "nothing in them breaks the rule. The novel is the place where the "
            "rule fails and the place the reader learns it from."
        ),
        "mistakes": (
            (
                "Thinking more is always safe",
                "<em>More</em> is safe for a word of three parts or more: the "
                "novel uses it on all 28 such forms. For a word of one part it "
                "is the error, as in <em>more big</em>: the novel puts "
                "<em>-er</em> or <em>-est</em> on 268 of its 270 forms of one "
                "part. Its two exceptions, <em>more strange</em> and "
                "<em>most sure</em>, are a writer's choice and not a rule.",
            ),
            (
                "Putting -er on a long word",
                "<em>Beautifuler</em> is not a form anyone wrote. Not one of "
                "the 28 forms of three parts or more has an ending, in a novel "
                "that writes <em>handsomer</em> without a second thought.",
            ),
            (
                "Copying every form from an old book",
                "22 of the 30 forms the rule gets wrong are an ending on a "
                "word of two parts. Some, such as <em>quieter</em>, are still "
                "good English; others, such as <em>handsomer</em> and "
                "<em>pleasanter</em>, a modern writer would give "
                "<em>more</em>. A form that is in a printed book is not for "
                "that reason a form to copy. Look at the date.",
            ),
        ),
        "quiz_title": "Check yourself",
        "quiz": (
            {
                "q": "By the rule, which is the <em>-er</em> form of <em>happy</em>?",
                "a": ["happyer", "more happy", "happier", "happiest"],
                "c": 2,
                "why": (
                    "<em>Happy</em> has two parts and ends in <em>-y</em>, so "
                    "the <em>y</em> becomes <em>i</em> and <em>-er</em> follows: "
                    "<em>happier</em>. <em>Happiest</em> is the <em>-est</em> form, "
                    "made the same way, but the question asks for <em>-er</em>. "
                    "<em>Happyer</em> skips the spelling "
                    "change, and <em>more happy</em> is the form the rule is "
                    "there to replace."
                ),
            },
            {
                "q": "In the novel, how many of the forms of adjectives with "
                     "three or more parts take <em>-er</em> or <em>-est</em>?",
                "a": ["None of them", "About one in ten", "About half",
                      "All of them"],
                "c": 0,
                "why": (
                    "None. The lab's parts table shows 0 with an ending and 18 "
                    "with <em>more</em> or <em>most</em> for three parts, and "
                    "0 and 10 for four or more."
                ),
            },
            {
                "q": "Which group is the largest among the 30 forms rule A gets "
                     "wrong in the novel?",
                "a": [
                    "Adverbs such as <em>oftener</em>",
                    "Adjectives of one part written with <em>more</em>",
                    "Adjectives of three parts written with <em>-er</em>",
                    "Adjectives of two parts given an ending, such as <em>handsomer</em>",
                ],
                "c": 3,
                "why": (
                    "22 of the 30. <em>Oftener</em> accounts for 3, adjectives of one "
                    "part with <em>more</em> for 2, and adjectives of three "
                    "parts with an ending for none."
                ),
            },
            {
                "q": "Rule B is right on 341 forms and rule A on 337. What is "
                     "the difference?",
                "a": [
                    "The five <em>more</em> and <em>most</em> misses are now right",
                    "Four forms of <em>gentle</em>, <em>narrow</em> and "
                    "<em>noble</em> are now right",
                    "The three <em>oftener</em> lines are now right",
                    "Four forms of adjectives of three parts are now right",
                ],
                "c": 1,
                "why": (
                    "Rule B gives <em>-er</em> to two parts ending in "
                    "<em>-ow</em>, <em>-le</em> or <em>-er</em>. That moves "
                    "<em>gentlest</em>, <em>narrowest</em>, <em>nobler</em> "
                    "and <em>noblest</em>, and nothing else."
                ),
            },
        ),
        "body": [
            ("p",
             "The rule most books give is about size: short words take "
             "<em>-er</em> and long words take <em>more</em>. It is a good "
             "start, and it leaves one question open. How short is short? "
             "<em>Pleasant</em> and <em>handsome</em> are both eight letters "
             "and two parts, and the novel puts <em>-er</em> on both."),
            ("p",
             "Count parts instead of letters. <em>Big</em> has one part, "
             "<em>happy</em> two, <em>beautiful</em> three. The rule then has "
             "three lines. One part takes <em>-er</em> and <em>-est</em>. Two "
             "parts ending in <em>-y</em> take them too, with the <em>y</em> "
             "changed to <em>i</em>. Everything else takes <em>more</em> and "
             "<em>most</em>."),
            ("h3", "How the rule scores on a novel"),
            ("p",
             "The lab holds 367 comparisons from "
             "<em>Pride and Prejudice</em>. Rule A is right on 337, which is "
             "91.8%. The table of parts shows why it works so well. Of the "
             "forms of one part, 268 take an ending and 2 take <em>more</em>. Of "
             "the forms of three parts and longer, none take an ending: 18 and 10 "
             "take <em>more</em>. The only place the two choices both occur in "
             "numbers is two parts, 54 with an ending and 15 with <em>more</em>."),
            ("h3", "Where the rule breaks"),
            ("p",
             "Adjectives of two parts are the whole difficulty. Rule A sends only "
             "those ending in <em>-y</em> to an ending, and the novel gives an "
             "ending to far more: 54 of its 69 forms of two parts. 22 of the 30 wrong "
             "forms are this. They belong to ten adjectives: <em>handsome</em>, "
             "<em>pleasant</em>, <em>common</em>, <em>gentle</em>, "
             "<em>minute</em>, <em>narrow</em>, <em>noble</em>, <em>quiet</em>, "
             "<em>severe</em> and <em>stupid</em>. Some of the ten are still "
             "good English with an ending: <em>quieter</em>, <em>narrower</em>, "
             "<em>gentler</em>. A modern writer would give <em>handsome</em> and "
             "<em>pleasant</em> <em>more</em> and <em>most</em>. The lab cannot "
             "sort the two groups, because the sort is a judgement about how "
             "English sounds now; the novel is not wrong, it is 1813."),
            ("p",
             "Rule B tries to catch some of them by also giving an ending to "
             "two parts that end in <em>-ow</em>, <em>-le</em> or <em>-er</em>. "
             "It moves four forms, <em>gentlest</em>, <em>narrowest</em>, "
             "<em>nobler</em> and <em>noblest</em>, and the score goes from "
             "337 to 341 of 367, or 92.9%. That is a rule built to fit the "
             "novel. The other 18 forms end in <em>-e</em>, <em>-t</em>, "
             "<em>-n</em> and <em>-d</em>, and no short ending covers them."),
            ("h3", "The other eight"),
            ("p",
             "Three are <em>oftener</em>, which is an adverb: the rule is for "
             "adjectives, and these lines are outside it. Five go the other way. "
             "<em>More angry</em>, <em>more likely</em> and <em>most likely</em> "
             "are words of two parts ending in <em>-y</em> that the novel gives "
             "<em>more</em>, and <em>more strange</em> and <em>most sure</em> "
             "are words of one part that it gives <em>more</em>. Today "
             "<em>more likely</em> is the usual form, so that pair is a hole in "
             "the rule's <em>-y</em> line and not a fault in the novel."),
            ("h3", "A second text and a modern one"),
            ("p",
             "The play has 49 forms. Rule A is right on 44, which is 89.8%, and "
             "rule B on 45, which is 91.8%. The misses are <em>remotest</em> "
             "twice, <em>noblest</em>, <em>oftener</em> and <em>pleasanter</em>, "
             "the same kinds as the novel. The two modern documents have 32 "
             "forms, and both rules are right on all 32. None of the 32 uses "
             "<em>more</em> or <em>most</em>. They are the Census Bureau story "
             "&ldquo;U.S. Population Aging as Nation Turns 250&rdquo; (2026) and "
             "the US Supreme Court opinion <em>Stanley v. City of Sanford</em>, "
             "606 U.S. 46 (2025), with words such as <em>older</em> and "
             "<em>earlier</em>, so 32 right says that nothing in them breaks the "
             "rule. It does not say that a modern writer prefers <em>more "
             "handsome</em>."),
            ("p",
             "Take the rule, use it on a word you have not met, and check an "
             "old form against its date before you copy it."),
        ],
    },
]
