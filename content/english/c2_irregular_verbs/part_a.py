# -*- coding: utf-8 -*-
"""Irregular Verbs, lesson one: what an irregular verb is, and how many there are."""

LESSONS = [
    {
        "slug": "the-verbs-that-break-the-rules",
        "module": "The exception list Tense Tables kept pointing at",
        "title": "The Verbs That Break the Rules",
        "one_line": "About 180 verbs ignore the -ed rule, and they are the verbs you use most.",
        "standard": (
            "Finish when you can test a verb against the -ed rule, give the size "
            "of the list, and explain why the list is short but the words are "
            "everywhere.",
            "You should be able to run the four-step test on any verb and say "
            "regular or irregular, name the three forms that matter, say how "
            "many irregular verbs there are and where that figure comes from, "
            "and explain why a verb you use every day is far more likely to be "
            "irregular than one you rarely meet.",
        ),
        "summary": (
            "<em>Tense Tables</em> gave four rules that build every regular verb, and "
            "on the regular verbs the rules were right more than 99 times in "
            "100. The <dfn>irregular</dfn> verbs were set aside before that "
            "score was taken, because no rule makes their past: <em>bring</em> "
            "does not become <em>bringed</em>. This course is about them. The "
            "lab holds 133, printed with their three forms; 132 of them sort "
            "into six classes by a rule a computer can check, and <em>be</em> "
            "stands outside. The list is short, but it is made of the words "
            "you say most."
        ),
        "key_label": "Three forms, regular and not",
        "key": [
            "base / past / form after have",
            "",
            "walk / walked / walked",
            "   the -ed rule builds both",
            "bring / brought / brought",
            "   no rule builds these: learn them",
            "",
            "133 verbs in the lab: 132 in 6 classes, and be",
        ],
        "concepts_intro": "Three ideas, and the last one explains the other two.",
        "concepts": [
            (
                "A verb is irregular when the -ed rule fails",
                "<em>Tense Tables</em> showed that adding <em>-ed</em> gives the past of "
                "almost every regular verb. A verb is <em>irregular</em> when "
                "that rule gives the wrong answer. <em>Bring</em> becomes "
                "<em>brought</em>, and "
                "nothing in the spelling of <em>bring</em> tells you so.",
            ),
            (
                "The list is short and it is counted",
                "The lab holds 133 verbs. 132 of them fall into six classes, "
                "the largest with 60, and <em>be</em> stands outside the "
                "classes. Pinker, who has written about this at length, "
                "puts the whole list at about 180. A list of 180 is a small "
                "thing to learn next to a language of many thousands of "
                "verbs.",
            ),
            (
                "Frequency is what keeps a verb irregular",
                "The idea, which Pinker has argued, is that a word "
                "you hear all the time is held in memory whole. It never needs "
                "the rule, so the rule never takes it over. A rare word has to "
                "be built each time, and a build soon settles on the "
                "regular rule. That is why the odd verbs are the common ones.",
            ),
        ],
        "steps_title": "Testing a verb",
        "steps_intro": "To find out whether a verb is irregular, do this.",
        "steps": [
            (
                "Write the three forms",
                "The base, the past, and the form used after <em>have</em>. "
                "These three are enough. The other two forms, the <em>-s</em> "
                "form and the <em>-ing</em> form, follow the rules from that "
                "course for every irregular verb but two: <em>have</em> makes "
                "<em>has</em>, and <em>be</em> has <em>am</em>, <em>is</em> "
                "and <em>are</em>.",
            ),
            (
                "Build the past by the -ed rule",
                "Add <em>-ed</em>, with the small changes that course listed. "
                "This is your guess.",
            ),
            (
                "Compare the guess with what people write",
                "If they match, the verb is regular. If they do not, the verb "
                "is irregular, and the difference is what you have to learn.",
            ),
            (
                "Look at the form after have",
                "Check the third form on its own. For <em>show</em> the past "
                "is regular, <em>showed</em>, but the form after "
                "<em>have</em> is <em>shown</em>. One wrong form is enough.",
            ),
        ],
        "lab": ("english", {
            "mode": "irregular",
            "panel_title": "Every irregular verb in the list, in three forms",
            "panel_intro": (
                "These are the 133 verbs the lab holds, each with its base, its "
                "past and its form after <em>have</em>, and the class the "
                "sorting rule puts it in. Search for a verb you use every day "
                "and see whether it is here. Then narrow the list to one class "
                "and read how the six classes share out the whole list. The "
                "counts in the tiles are made in your browser from the printed "
                "rows."
            ),
        }),
        "read_title": "Running the test on three verbs",
        "read_intro": (
            "The four steps above, on a regular verb, on a verb with one odd "
            "form, and on a verb with two."
        ),
        "worked": {
            "title": "Walk, show and bring",
            "intro": [
                "For each verb the guess is the base plus -ed, used for both "
                "the past and the form after have. Beside it is what people "
                "write.",
            ],
            "lines": [
                "walk:   guess walked, walked",
                "        written walked, walked      regular",
                "",
                "show:   guess showed, showed",
                "        written showed, shown       irregular",
                "",
                "bring:  guess bringed, bringed",
                "        written brought, brought    irregular",
            ],
            "after": [
                "<em>Walk</em> passes both steps. <em>Show</em> passes the "
                "past and fails the form after <em>have</em>, and one failure "
                "is enough, so it is on the list. <em>Bring</em> fails both. "
                "The test never asks how a verb sounds or how common it is; it "
                "compares two spellings, which is what lets the lab print the "
                "list without a judgement in it.",
                "The lab shows the written forms for all 133. Pick any row, "
                "build the guess yourself, and you will find the row is there "
                "because the guess is wrong.",
            ],
        },
        "note": (
            "The figure of 180 is Pinker&rsquo;s, and it is a count of "
            "judgement, not of measurement. Where you draw the edge of the "
            "list changes the number. What does not change is the shape: many "
            "common verbs, few rare ones."
        ),
        "mistakes": [
            (
                "Calling a verb irregular because it feels odd",
                "<em>Showed</em> feels fine, so <em>show</em> seems regular. "
                "But the form after <em>have</em> is <em>shown</em>, and "
                "that one breaks the rule. A verb is irregular if any of its "
                "forms break the rule, not only the past.",
            ),
            (
                "Thinking the odd forms are mistakes that stuck",
                "<em>Went</em> and <em>was</em> are not errors. They are "
                "very old forms that stayed because people used them too "
                "often to change. Treating them as errors is the wrong "
                "starting point.",
            ),
            (
                "Learning the list in the order of a book",
                "A list in the order of the letters hides the fact that the verbs fall "
                "into a few shapes. The next lesson sorts them by shape, "
                "which is much easier to hold in mind.",
            ),
        ],
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "Which pair shows a verb that is irregular?",
                "a": [
                    "<em>walk</em> and <em>walked</em>",
                    "<em>plan</em> and <em>planned</em>",
                    "<em>bring</em> and <em>brought</em>",
                    "<em>stop</em> and <em>stopped</em>",
                ],
                "c": 2,
                "why": (
                    "<em>Brought</em> is not <em>bring</em> plus <em>-ed</em>. "
                    "The others are built by the <em>-ed</em> rule, with the "
                    "doubling change from <em>Tense Tables</em> for <em>plan</em> and "
                    "<em>stop</em>."
                ),
            },
            {
                "q": "Why is a common verb more likely to be irregular than a rare one?",
                "a": [
                    "Common words are shorter",
                    "A word heard often is kept whole and escapes the rule",
                    "Rare words were never given a past",
                    "Common words are newer",
                ],
                "c": 1,
                "why": (
                    "Frequency protects the old form. A rare word is built "
                    "from the rule each time, and the rule is the regular one."
                ),
            },
            {
                "q": "Pinker puts the number of irregular verbs at about 180. What kind of figure is that?",
                "a": [
                    "An exact figure with no doubt",
                    "A figure measured on one novel",
                    "A figure for the lab list alone",
                    "A count that depends on where you draw the edge",
                ],
                "c": 3,
                "why": (
                    "The lab holds 133 and 183 were collected for the word "
                    "list check. The edge of the list moves with the "
                    "choices made, so no single number is final."
                ),
            },
            {
                "q": "<em>Show</em> has a regular past, <em>showed</em>. Is it an irregular verb?",
                "a": [
                    "Yes, because the form after <em>have</em> is <em>shown</em>",
                    "No, because the past is regular",
                    "No, because it is too common",
                    "Yes, because it ends in <em>-w</em>",
                ],
                "c": 0,
                "why": (
                    "One broken form is enough. <em>Shown</em> is not "
                    "<em>show</em> plus <em>-ed</em>."
                ),
            },
        ],
        "body": [
            ("p",
             "<em>Tense Tables</em> ended with a score. Four rules build the five forms "
             "of any regular verb, and on the 1,210 regular verbs of the word "
             "list they were right 99.92%, 99.34% and 99.26% of the time. The "
             "few they missed were regular verbs with a spelling twist, such "
             "as <em>panic</em> and <em>panicking</em>. But before that score "
             "was taken, a set of verbs was put aside, because no rule builds "
             "their past at all. This course is that set."),
            ("h3", "What irregular means here"),
            ("p",
             "Every verb has a base form, a past, and a form used after "
             "<em>have</em>. The last of these is called the "
             "<dfn>participle</dfn>. For <em>walk</em> the past and the "
             "participle are both <em>walked</em>, and the <em>-ed</em> rule "
             "builds them."),
            ("p",
             "A verb is <em>irregular</em> when that rule gives the wrong "
             "answer for the past, the participle, or both. <em>Bring</em>, "
             "<em>brought</em>, <em>brought</em>. <em>Know</em>, "
             "<em>knew</em>, <em>known</em>. No rule from <em>Tense Tables</em> makes "
             "these, and you cannot work them out from the base."),
            ("h3", "How many there are"),
            ("p",
             "The lab holds 133 verbs, printed with their three forms. 132 of "
             "them fall into six classes, and the biggest class has 60; the "
             "tile that counts the classes reads 6, because <em>be</em> stands "
             "outside them all. The next lesson shows how the classes are "
             "defined."),
            ("p",
             "The wider figure is Pinker&rsquo;s: about 180 irregular verbs "
             "in all. A list of 183 was put together for this course, and "
             "that is close to his number. It is a count that depends on "
             "where you draw the line, so read it as a size and not as an "
             "exact total."),
            ("h3", "They are the common words"),
            ("p",
             "When this course was built, the 183 verbs were checked against "
             "a list of the 2,809 most common words in English. 132 of them "
             "were in it, which is 72.1%. The 51 that were not include "
             "<em>weep</em>, <em>flee</em>, <em>creep</em>, <em>shed</em> and "
             "<em>forgive</em>. That check was made once, and it is quoted "
             "here: the page does not carry the 183, so it cannot redo it. "
             "The lab holds 133, one more than the 132, because the list was "
             "settled by hand after the check; every one of the 133 is in the "
             "common list."),
            ("p",
             "Look at the kept verbs by rank in that common list. The middle "
             "verb is at rank 697.5, so half of them sit among the 700 "
             "commonest words, and 44% are in the top 500. These two figures "
             "are quoted too: the page carries each word&rsquo;s band, not "
             "its rank. The irregular verbs gather at the frequent end."),
            ("h3", "Why the common words are the odd ones"),
            ("p",
             "This is an observation more than a proof, and it is "
             "Pinker&rsquo;s, not something measured "
             "here. A word that you meet thousands of times is stored in "
             "memory whole. It never has to be built, so the regular rule "
             "never gets the chance to replace it. Frequency keeps a "
             "verb irregular."),
            ("p",
             "A rare verb works the other way. You meet it too rarely to "
             "store its past, so you build the past each time, and what you "
             "build is the regular one. Over many years, rare irregular "
             "verbs tend to move toward <em>-ed</em>. The common ones stay "
             "as they are."),
            ("h3", "What the numbers do not say"),
            ("p",
             "The word list check shows that irregular verbs are common. It "
             "does not show why. The idea of memory is a good reason, and "
             "other reasons may also play a part. Treat it as the best "
             "account available, and do not lean on it too hard."),
            ("p",
             "The rest of this course puts numbers on the list. Next comes "
             "its shape, six classes with a rule each. After that comes the "
             "question of how much of a real page these verbs fill, and "
             "there the first number you see turns out to need a fix."),
        ],
    },
]
