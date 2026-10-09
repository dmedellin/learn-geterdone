# -*- coding: utf-8 -*-
"""Course 2, lesson three: how much of a real page is irregular verbs.

The lab counts on the printed passage (949 words of the novel) and its tiles
are computed in the browser. Every figure for the WHOLE novel (12.29%, 59.5%,
87.65%, 73.89%, 15,192 forms and so on) was counted once, offline, over the
novel text, which is far too large to inline; the prose labels each of those
as quoted, and the lesson teaches the difference.
"""

LESSONS = [
    {
        "slug": "how-much-of-english-is-irregular",
        "module": "A flattering number, and what it hides",
        "title": "How Much of English Is Irregular",
        "one_line": "On a printed page about one word in six is an irregular verb form, and three verbs are more than half of those.",
        "standard": (
            "Finish when you can give the share of a printed passage that is "
            "irregular verb forms, with and without the three biggest, say "
            "which figures in this lesson the page computes and which it "
            "quotes, and say why the first number misleads.",
            "You should be able to read both shares off the lab, say how much "
            "of the total <em>be</em>, <em>have</em> and <em>do</em> carry, "
            "explain why a top-twenty figure that includes them flatters the "
            "list, tell a figure counted in your browser from one quoted from "
            "the whole novel, and name what one old novel cannot tell you.",
        ),
        "summary": (
            "On the passage printed with the lab, 949 words of <em>Pride and "
            "Prejudice</em>, 149 words are forms of an <dfn>irregular</dfn> "
            "verb: 15.7%, about one word in six, counted in your browser. "
            "That number is true and it is also a trap. Three verbs, "
            "<em>be</em>, <em>have</em> and <em>do</em>, are 91 of the 149. "
            "Take them out and the share falls to 6.1%. Over the whole novel, "
            "counted once and quoted here, the same move takes 12.29% down to "
            "4.98%. The lesson counts both ways, and shows why a list that "
            "looks concentrated is concentrated mostly in three places."
        ),
        "key_label": "Irregular verb forms, two counts",
        "key": [
            "printed passage, 949 words (counted here)",
            "with be, have, do: 149 forms, 15.7%",
            "without them: 58 forms, 6.1%",
            "be, have, do: 91 of 149, 61.1%",
            "",
            "whole novel (quoted, counted once)",
            "with: 12.29%   without: 4.98%",
            "top 20 cover 87.65% with, 73.89% without",
        ],
        "concepts_intro": "Three ideas, and the second is the one to keep.",
        "concepts": [
            (
                "A share of words is a count of forms",
                "Every time an irregular verb appears in the text, in any "
                "form, that is one count. <em>Had</em>, <em>have</em> and "
                "<em>having</em> all count for <em>have</em>. The share is the "
                "number of those counts divided by the number of words in "
                "the text: on the passage, 149 divided by 949. It tells you "
                "how often you will meet one as you read, which is not the "
                "same as how many there are.",
            ),
            (
                "Three verbs are doing most of the work",
                "On the passage, <em>be</em>, <em>have</em> and <em>do</em> "
                "are 91 of the 149 forms, which is 61.1%. Over the whole "
                "novel the same three are 59.5% of every irregular form. So "
                "when you hear that irregular verbs fill a large part of "
                "English, most of that part is three verbs that are also the "
                "helping words of the language.",
            ),
            (
                "A number counted one way can flatter",
                "&ldquo;The top twenty cover 87.65%&rdquo; is true of the "
                "novel. But three of those twenty are <em>be</em>, <em>have</em> "
                "and <em>do</em>. With them left out, the top twenty of the "
                "rest cover 73.89%. Both figures are quoted: the page cannot "
                "recount them, because it would need the whole book. The first "
                "makes the list look more concentrated than the verbs you must "
                "learn really are.",
            ),
        ],
        "steps_title": "Reading a share honestly",
        "steps_intro": "When someone gives you a share, ask these four things.",
        "steps": [
            (
                "Share of what?",
                "Words, or verbs, or irregular verbs only. 15.7% is of all "
                "the words in the passage. 61.1% is of the irregular forms "
                "in it. They answer different questions.",
            ),
            (
                "Which items are in the count?",
                "Here the question is whether <em>be</em>, <em>have</em> and "
                "<em>do</em> are in. They change the answer a great deal, "
                "so a figure should say.",
            ),
            (
                "Count it again without the biggest items",
                "If the largest three are most of the total, take them out "
                "and count again. The new figure shows how much the rest of "
                "the list is doing.",
            ),
            (
                "Was it counted here, or somewhere else?",
                "A figure counted in front of you on printed words can be "
                "checked by hand. A figure quoted from a count you cannot "
                "see has to be trusted, and the page should say which it is.",
            ),
        ],
        "lab": ("english", {
            "mode": "irrshare",
            "panel_title": "The same passage, counted with and without three verbs",
            "panel_intro": (
                "The passage is printed under the table: 949 words of the "
                "novel. Every word in it is checked in your browser against "
                "the printed list of irregular verbs, and the menu decides "
                "whether <em>be</em>, <em>have</em> and <em>do</em> are "
                "counted. Switch them in and out and watch the share of all "
                "words change while their own share of the irregulars stays "
                "put. The page does not decide which is the right number. It "
                "lets you see why the choice matters."
            ),
        }),
        "read_title": "One passage, counted two ways",
        "read_intro": (
            "The lab&rsquo;s own count on the printed passage, and beside it "
            "the count made once over the whole novel."
        ),
        "worked": {
            "title": "The passage, then the novel",
            "intro": [
                "The first block is what the lab prints, and you can check it "
                "against the passage under the table. The second block is "
                "quoted: it was counted once over the whole novel, and the "
                "page does not carry the novel.",
            ],
            "lines": [
                "passage, 949 words, counted here:",
                "  all irregular forms: 149, which is 15.7% of words",
                "  be, have, do: 91, which is 61.1% of those",
                "  all the others: 58, which is 6.1% of words",
                "",
                "whole novel, quoted:",
                "  all irregular forms: 12.29% of words",
                "  be, have, do: 59.5% of those",
                "  all the others: 4.98% of words",
            ],
            "after": [
                "On the passage, 91 of the 149 forms are <em>be</em>, "
                "<em>have</em> or <em>do</em>: about three in five. In the novel the "
                "same three are 9,037 of 15,192 forms, which is 59.5%. The "
                "passage is one page of the book, and the book agrees with it "
                "in shape: take the three out and the share of words falls "
                "by more than half, 15.7% to 6.1% here, 12.29% to 4.98% there. "
                "The page is richer in irregular forms than the book as a "
                "whole, which is what one page of a long book can be.",
                "The passage is where the checking happens. Count the words "
                "in the table yourself, or search the passage for <em>had</em>, "
                "and the tile moves when the menu does. The novel figures are "
                "the same kind of count on a text a thousand times longer, and "
                "they are given here as quoted.",
            ],
        },
        "note": (
            "Both top-twenty numbers are real, and both are quoted from one "
            "count of the whole novel. The first answers how much of the "
            "irregular text is covered by twenty verbs including the helpers. "
            "The second answers how much is covered by twenty verbs you have "
            "to learn as ordinary main verbs. Only the second is about the "
            "list this course teaches."
        ),
        "mistakes": [
            (
                "Quoting 87.65% as if every slot counted",
                "Three of the twenty carry 59.5% on their own. The other "
                "seventeen share what is left. A reader who hears "
                "&ldquo;twenty verbs cover nearly nine tenths&rdquo; will "
                "picture twenty equal workers. There are three large ones and "
                "seventeen small ones.",
            ),
            (
                "Treating one old novel as English",
                "The text is from the 1810s. Some verbs were more common "
                "then and some are less common now. The shares are right "
                "for this book. They are a guide to the language, not a "
                "measure of it.",
            ),
            (
                "Reading a share of words as a count of verbs",
                "15.7% says how often you meet an irregular form on the "
                "page. It does not say that 16% of verbs are irregular. A few "
                "verbs are met over and over, which is exactly why the share "
                "is high while the list is short.",
            ),
        ],
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "On the printed passage, what share of the irregular forms are <em>be</em>, <em>have</em> or <em>do</em>?",
                "a": ["15.7%", "61.1%", "6.1%", "59.5%"],
                "c": 1,
                "why": (
                    "91 of 149, which is 61.1%. 15.7% and 6.1% are shares of "
                    "all the words in the passage, with and without the three. "
                    "59.5% is the same share of the irregulars, but counted "
                    "over the whole novel and quoted."
                ),
            },
            {
                "q": "Why is the figure 87.65% a flattering one?",
                "a": [
                    "It is counted on the wrong text",
                    "It leaves out the commonest verb",
                    "It counts every verb in English",
                    "Three of the twenty verbs carry most of it",
                ],
                "c": 3,
                "why": (
                    "With <em>be</em>, <em>have</em> and <em>do</em> left out, the "
                    "top twenty of the rest cover 73.89%. The headline gets part of its "
                    "height from three verbs that are also helping words."
                ),
            },
            {
                "q": "Which claim does an 1810s novel support?",
                "a": [
                    "A pattern in the text of that book",
                    "The exact share in speech today",
                    "The share in every book ever written",
                    "The number of irregular verbs in English",
                ],
                "c": 0,
                "why": (
                    "One book from one time shows how that book is built. "
                    "Whether the same holds now is a question for other texts."
                ),
            },
            {
                "q": "Which of these figures does the page count in your browser?",
                "a": [
                    "12.29% of the words of the novel",
                    "87.65% for the top twenty",
                    "15.7% of the printed passage",
                    "59.5% for <em>be</em>, <em>have</em> and <em>do</em> in the novel",
                ],
                "c": 2,
                "why": (
                    "The passage is printed under the lab and the tiles are "
                    "counted from it. The other three need the whole novel, "
                    "which the page does not carry, so they are quoted."
                ),
            },
        ],
        "body": [
            ("p",
             "How much of English is irregular? There is a quick answer, and "
             "it is the wrong place to stop. This lesson gives the quick "
             "answer, counted in front of you, then takes it apart."),
            ("h3", "The count on the page"),
            ("p",
             "The lab prints 949 words of <em>Pride and Prejudice</em> and "
             "checks each one against the list of irregular verbs from the "
             "first lesson. For each verb it looks for every form: the base, "
             "the past, the form after <em>have</em>, the form after "
             "<em>he</em> or <em>she</em>, and the <em>-ing</em> form. The "
             "last two are made by the spelling rules from <em>Tense "
             "Tables</em>, so <em>go</em> gives <em>goes</em> and "
             "<em>write</em> gives <em>writing</em>. <em>Be</em> and "
             "<em>have</em> are the two the rules cannot make, so their "
             "present forms are written out: <em>am</em>, <em>is</em>, "
             "<em>are</em>, and <em>has</em>. Every match is one irregular "
             "form. It finds 149, which is 15.7% of the words. About one "
             "word in six."),
            ("p",
             "That is a large share. It is the sort of number that gets "
             "quoted when someone wants to say that irregular verbs matter, "
             "and they do. But look at what it is made of. The table under "
             "the tiles sorts the verbs by how often they appear, and the "
             "top three rows are <em>be</em>, <em>have</em> and <em>do</em>."),
            ("h3", "Three verbs"),
            ("p",
             "<em>Be</em>, <em>have</em> and <em>do</em> are 91 of the 149 "
             "forms, which is 61.1%: about three in five of every irregular "
             "form on the page. <em>Be</em> alone is 49 of them, and twenty "
             "of those are <em>was</em>. Take the three out with the menu. "
             "The other irregular verbs come to 58 forms, which is 6.1% of "
             "the words. About one word in sixteen. That is still a fair "
             "share, but it is well under half the first figure."),
            ("p",
             "There is a reason these three stand apart. They are not only "
             "main verbs. They are also the helping words that build the "
             "tenses from <em>Tense Tables</em>, so they appear whether or not the "
             "sentence is about being, having or doing anything."),
            ("h3", "What a match does not prove"),
            ("p",
             "The lab matches spellings, not meanings, and there are words where "
             "that would matter. <em>Left</em> would count for "
             "<em>leave</em> even if it meant the side, and <em>saw</em> "
             "for <em>see</em> even if it meant the tool. In this passage "
             "the one <em>left</em> and both of the <em>saw</em>s are verbs, "
             "and the table lists every verb with its count, so you can "
             "check any of them against the passage by hand."),
            ("h3", "The whole novel, quoted"),
            ("p",
             "The same count was made once over the whole novel, using the "
             "text of the novel only and a program that knew every form of "
             "<em>be</em>. That gave 15,192 irregular forms in 123,611 words, "
             "which is 12.29%, about one word in eight. <em>Be</em> appears "
             "5,873 times, 4.75% of all the words by itself. <em>Have</em> "
             "appears 2,343 times and <em>do</em> 821. Together they are "
             "9,037 forms, 59.5% of every irregular form in the book, and the "
             "rest come to 6,155 forms, 4.98% of the words."),
            ("p",
             "None of those figures is recomputed on this page. The novel is "
             "about 700,000 letters, far too much to print here, so they are "
             "quoted, and they are marked as quoted wherever they appear in "
             "this lesson. What you can check is that the passage, counted in "
             "front of you, has the same shape: more than half of the irregular "
             "forms are three verbs, and the share of words falls by more "
             "than half when they leave."),
            ("h3", "The top twenty"),
            ("p",
             "Now count the other way, over the novel. Rank the irregular "
             "verbs by how often they appear and add up the top twenty. With "
             "<em>be</em>, <em>have</em> and <em>do</em> in the list, the "
             "twenty cover 87.65% of all irregular forms. It sounds like "
             "proof that a short list does almost all the work."),
            ("p",
             "It is the number to distrust. Three of the twenty places "
             "belong to the three verbs that carry 59.5% on their own. "
             "That leaves seventeen places to share what remains. Leave "
             "the three out and rank the rest again. The top twenty of those "
             "cover 73.89%. Both figures are quoted from the one count of the "
             "novel; the lab&rsquo;s table shows the same ranking on the "
             "passage, where <em>say</em>, <em>know</em> and <em>see</em> "
             "lead once the three are gone. Both figures are correct, and they "
             "are answers to different questions. The first asks how much a "
             "list with the helpers covers. The second asks how much twenty "
             "ordinary main verbs cover. If you are deciding which verbs to "
             "learn, you want the second."),
            ("h3", "What one old book cannot tell you"),
            ("p",
             "Everything above comes from one novel from the 1810s. It is "
             "one writer, writing a story, with a lot of talk in it. Verbs "
             "that were common in that book may be rarer today, and the "
             "reverse. The ranks, and so the top twenty, would change in "
             "other texts. What should hold up is the shape, not the exact "
             "figures. A few verbs carry a great deal, and a long tail carries "
             "a little. The shares tell you how that shape looks in this "
             "book, and the lab lets you check it on one page of it."),
            ("p",
             "That is the end of this course. The list of irregular verbs "
             "is about 180 long, falls into six patterns, and fills about "
             "one word in six of this printed page and one in eight of the "
             "novel. Three verbs carry more than half of that, and the claim "
             "that twenty verbs cover almost all of it holds only if those "
             "three are in."),
        ],
    },
]
