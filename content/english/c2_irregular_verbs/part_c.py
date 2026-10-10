# -*- coding: utf-8 -*-
"""Course 2, lesson three: how much of a real page is irregular verbs.

The lab counts on the printed passage (936 words of the novel) and its tiles
are computed in the browser. Every figure for the WHOLE novel (12.39%, 59.5%,
87.66%, 73.90%, 15,147 forms in 122,294 words and so on) was counted once,
offline, on 2026-10-10, with the matcher and tokeniser this page ships (the
irrshare form table over wordsOf, run under node) over the novel text only:
Gutenberg #1342 sliced on its first and last sentence, with the 1894
edition's 154 picture captions removed first. The recipe and the recount are
in docs/pedagogy/english-irregular-verbs.md. The earlier quoted figures
(12.29%, 4.98%, 15,192 of 123,611) came from a tokeniser that split every
typographic apostrophe into two words and kept the captions; they are gone.
The prose labels each novel figure as quoted, and the lesson teaches the
difference.
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
            "On the passage printed with the lab, 936 words of <em>Pride and "
            "Prejudice</em>, 149 words match a form of an <dfn>irregular</dfn> "
            "verb: 15.9%, about one word in six, counted in your browser. "
            "That number is true and it is also a trap. Three verbs, "
            "<em>be</em>, <em>have</em> and <em>do</em>, are 91 of the 149. "
            "Take them out and the share falls to 6.2%. Over the whole novel, "
            "counted once and quoted here, the same move takes 12.39% down to "
            "5.01%. The lab also counts how much of the irregular forms the "
            "twenty commonest verbs cover, 95.3% with the three and 93.1% "
            "without, and the lesson sets those beside the two figures quoted "
            "from the novel. A list that looks concentrated is concentrated "
            "mostly in three places, and a short page makes it look more "
            "concentrated still."
        ),
        "key_label": "Irregular verb forms, two counts",
        "key": [
            "printed passage, 936 words (counted here)",
            "with be, have, do: 149 forms, 15.9%",
            "without them: 58 forms, 6.2%",
            "top 20 cover 95.3% with, 93.1% without",
            "",
            "whole novel (quoted, counted once)",
            "with: 12.39%   without: 5.01%",
            "top 20 cover 87.66% with, 73.90% without",
        ],
        "concepts_intro": "Three ideas, and the second is the one to keep.",
        "concepts": [
            (
                "A share of words is a count of forms",
                "Every time an irregular verb appears in the text, in any "
                "form, that is one count. <em>Had</em>, <em>have</em> and "
                "<em>having</em> all count for <em>have</em>. The share is the "
                "number of those counts divided by the number of words in "
                "the text: on the passage, 149 divided by 936. It tells you "
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
                "&ldquo;The top twenty cover 87.66%&rdquo; is true of the "
                "novel. But three of those twenty are <em>be</em>, <em>have</em> "
                "and <em>do</em>. With them left out, the top twenty of the "
                "rest cover 73.90%. Both figures are quoted: the page cannot "
                "recount them, because it would need the whole book. The page "
                "does count the same thing on its own passage, and gets 95.3% "
                "and 93.1%. The first quoted figure makes the list look more "
                "concentrated than the verbs you must learn really are, and "
                "the passage figures show the same effect for a different "
                "reason: a short text uses few verbs.",
            ),
        ],
        "steps_title": "Reading a share honestly",
        "steps_intro": "When someone gives you a share, ask these four things.",
        "steps": [
            (
                "Share of what?",
                "Words, or verbs, or irregular verbs only. 15.9% is of all "
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
                "The passage is printed under the table: 936 words of the "
                "novel, written in 1813. Every word in it is checked in your "
                "browser against the printed list of irregular verbs, and the "
                "menu decides whether <em>be</em>, <em>have</em> and "
                "<em>do</em> are counted. Switch them in and out and watch the "
                "share of all words change while their own share of the "
                "irregulars stays put. The last tile gives the share of the "
                "irregular forms that the twenty commonest verbs cover. The "
                "page does not decide which is the right number. It lets you "
                "see why the choice matters."
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
                "passage, 936 words, counted here:",
                "  with be, have, do: 149 forms, 15.9% of words",
                "    the top twenty verbs cover 95.3% of the 149",
                "  without them: 58 forms, 6.2% of words",
                "    the top twenty verbs cover 93.1% of the 58",
                "  be, have, do: 91 of the 149, which is 61.1%",
                "",
                "whole novel, quoted:",
                "  with be, have, do: 12.39% of words",
                "    the top twenty cover 87.66%",
                "  without them: 5.01% of words",
                "    the top twenty cover 73.90%",
                "  be, have, do: 59.5% of the irregular forms",
            ],
            "after": [
                "On the passage, 91 of the 149 forms are <em>be</em>, "
                "<em>have</em> or <em>do</em>: about three in five. In the novel the "
                "same three are 9,017 of 15,147 forms, which is 59.5%. The "
                "passage is one page of the book, and the book agrees with it "
                "in shape: take the three out and the share of words falls "
                "by more than half, 15.9% to 6.2% here, 12.39% to 5.01% there. "
                "The page is richer in irregular forms than the book as a "
                "whole, which is what one page of a long book can be.",
                "The passage is where the checking happens. Count the words "
                "in the table yourself, or search the passage for <em>had</em>, "
                "and the tile moves when the menu does. The novel figures are "
                "the same kind of count on a text more than a hundred times "
                "longer, and they are given here as quoted. The last tile "
                "is new to this lesson. On the passage the twenty commonest "
                "verbs cover 142 of the 149 forms, and with the three left "
                "out, 54 of the 58. The novel quoted 87.66% and 73.90% for "
                "the same question, so the passage gives a higher share "
                "each time. The next paragraphs say why.",
            ],
        },
        "note": (
            "Both quoted top-twenty numbers are real, and both come from one "
            "count of the whole novel. The first answers how much of the "
            "irregular text is covered by twenty verbs including the helpers. "
            "The second answers how much is covered by twenty verbs you have "
            "to learn as ordinary main verbs. Only the second is about the "
            "list this course teaches. The page&rsquo;s own pair, 95.3% and "
            "93.1%, answers the same two questions for one page, and it is "
            "counted in your browser."
        ),
        "mistakes": [
            (
                "Quoting 87.66% as if every slot counted",
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
                "15.9% says how often you meet an irregular form on the "
                "page. It does not say that 16% of verbs are irregular. A few "
                "verbs are met over and over, which is exactly why the share "
                "is high while the list is short.",
            ),
        ],
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "On the printed passage, what share of the irregular forms are <em>be</em>, <em>have</em> or <em>do</em>?",
                "a": ["15.9%", "61.1%", "6.2%", "59.5%"],
                "c": 1,
                "why": (
                    "91 of 149, which is 61.1%. 15.9% and 6.2% are shares of "
                    "all the words in the passage, with and without the three. "
                    "59.5% is the same share of the irregulars, but counted "
                    "over the whole novel and quoted."
                ),
            },
            {
                "q": "Why is the figure 87.66% a flattering one?",
                "a": [
                    "It is counted on the wrong text",
                    "It leaves out the commonest verb",
                    "It counts every verb in English",
                    "Three of the twenty verbs carry most of it",
                ],
                "c": 3,
                "why": (
                    "With <em>be</em>, <em>have</em> and <em>do</em> left out, the "
                    "top twenty of the rest cover 73.90%. The headline gets part of its "
                    "height from three verbs that are also helping words."
                ),
            },
            {
                "q": "With the three left out, the page says its top twenty cover 93.1% of the irregular forms, and the novel&rsquo;s top twenty cover 73.90%. What explains the gap?",
                "a": [
                    "The passage is short, so it uses few different verbs",
                    "The page counts the words wrongly",
                    "The passage is from a different book",
                    "The novel has fewer irregular verbs than the passage",
                ],
                "c": 0,
                "why": (
                    "Both counts are of the same novel. A short page uses only "
                    "a few different irregular verbs, so twenty of them "
                    "cover nearly all the forms on it. Over a whole book the "
                    "list of verbs used is longer, and the twenty commonest "
                    "leave more of it uncovered."
                ),
            },
            {
                "q": "Which of these figures does the page count in your browser?",
                "a": [
                    "12.39% of the words of the novel",
                    "87.66% for the top twenty",
                    "15.9% of the printed passage",
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
             "The lab prints 936 words of <em>Pride and Prejudice</em> and "
             "checks each one against the list of irregular verbs from the "
             "first lesson. For each verb it looks for every form: the base, "
             "the past, the form after <em>have</em>, the form after "
             "<em>he</em> or <em>she</em>, and the <em>-ing</em> form. The "
             "last two are made by the spelling rules from <em>Tense "
             "Tables</em>, so <em>go</em> gives <em>goes</em> and "
             "<em>write</em> gives <em>writing</em>. <em>Be</em> and "
             "<em>have</em> are the two the rules cannot make, so the forms "
             "the rules miss are written out: <em>am</em>, <em>is</em>, "
             "<em>are</em> and <em>being</em> for <em>be</em>, and "
             "<em>has</em> for <em>have</em>. Every match counts as one "
             "irregular form. It finds 149, which is 15.9% of the words. "
             "About one word in six."),
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
             "The other irregular verbs come to 58 forms, which is 6.2% of "
             "the words. About one word in sixteen. That is still a fair "
             "share, but it is well under half the first figure. "
             "There is a reason these three stand apart. They are not only "
             "main verbs. They are also the helping words that build the "
             "tenses from <em>Tense Tables</em>, so they appear whether or not the "
             "sentence is about being, having or doing anything."),
            ("h3", "What a match does not prove"),
            ("p",
             "The lab matches spellings, not meanings, and there are words where "
             "that matters. <em>Left</em> would count for "
             "<em>leave</em> even if it meant the side, and <em>saw</em> "
             "for <em>see</em> even if it meant the tool. In this passage "
             "the one <em>left</em> and both of the <em>saw</em>s are verbs. "
             "One match is not a verb at all: <em>by no means</em> is "
             "counted as a form of <em>mean</em>, because <em>means</em> is "
             "the <em>he</em> or <em>she</em> form the <em>-s</em> rule "
             "builds. So of the 149 matches, 148 are irregular verb forms, "
             "and the share of words is 15.8% rather than 15.9%; the shape "
             "of every figure below is untouched. The table lists every "
             "verb with its count, so you can find the row for <em>mean</em> "
             "and check it against the passage by hand."),
            ("h3", "The whole novel, quoted"),
            ("p",
             "The same count was made once over the whole novel, with the "
             "program this page runs, over the text of the novel only: the "
             "picture captions that the 1894 printing added were taken out "
             "first. That gave 15,147 irregular forms in 122,294 words, "
             "which is 12.39%, about one word in eight. <em>Be</em> appears "
             "5,858 times, 4.79% of all the words by itself. <em>Have</em> "
             "appears 2,339 times and <em>do</em> 820. Together they are "
             "9,017 forms, 59.5% of every irregular form in the book, and the "
             "rest come to 6,130 forms, 5.01% of the words. "
             "None of those figures is recomputed on this page. The novel is "
             "about 120,000 words, some 130 times the passage, far too much "
             "to print here, so they are "
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
             "twenty cover 87.66% of all irregular forms. It sounds like "
             "proof that a short list does almost all the work."),
            ("p",
             "It is the number to distrust. Three of the twenty places "
             "belong to the three verbs that carry 59.5% on their own. "
             "That leaves seventeen places to share what remains. Leave "
             "the three out and rank the rest again. The top twenty of those "
             "cover 73.90%. Both figures are quoted from the one count of the "
             "novel; the lab&rsquo;s table shows the same ranking on the "
             "passage, where <em>say</em>, <em>know</em> and <em>see</em> "
             "lead once the three are gone. Both figures are correct, and they "
             "are answers to different questions. The first asks how much a "
             "list with the helpers covers. The second asks how much twenty "
             "ordinary main verbs cover. If you are deciding which verbs to "
             "learn, you want the second."),
            ("h3", "The same question on the page"),
            ("p",
             "The lab&rsquo;s last tile asks the question of the passage. "
             "Count the forms of the twenty commonest irregular verbs on it "
             "and divide by all the irregular forms. With <em>be</em>, "
             "<em>have</em> and <em>do</em> counted, the answer is 95.3%, "
             "142 of 149. With them left out it is 93.1%, 54 of 58. Both "
             "are counted in your browser, and both are higher than the "
             "novel&rsquo;s quoted 87.66% and 73.90%. "
             "Do not read that as the passage being more concentrated. Look "
             "at the table under the tiles: with the three counted it lists "
             "27 different verbs, and without them 24. Twenty of 27 is "
             "nearly everything, so twenty verbs cannot help covering most "
             "of the forms. A whole novel meets many more of the 133 verbs, "
             "and a long tail of them is met once or twice each. The "
             "same question gets a lower answer on a longer text. That is "
             "why the page prints its figure next to the quoted ones and "
             "does not replace them. It shows which way the number moves "
             "with the length of the text, and the novel&rsquo;s figure is "
             "the better guide to the list as a whole."),
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
             "printed here is 133 long, with about fifty rarer ones left "
             "out. It falls into six patterns, and fills about "
             "one word in six of this printed page and one in eight of the "
             "novel. Three verbs carry more than half of that, and the claim "
             "that twenty verbs cover almost all of it holds only if those "
             "three are in. The Helping Verbs course takes up <em>be</em>, "
             "<em>have</em> and <em>do</em> next, as the words that stand "
             "in front of other verbs."),
        ],
    },
]
