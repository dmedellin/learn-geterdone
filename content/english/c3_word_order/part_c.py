# -*- coding: utf-8 -*-
"""Lessons three and four of the word-order course: the rule that covers
about half, and the same rule on a play.

Lesson three scores the question rule on 90 lines from the novel, each one
cut at the start of its sentence, and searches two modern public documents,
printed beside them, for a question mark. Lesson four scores the same rule on
256 questions of two words or more from a play of 1895. Every figure in a box
is read off the built page with labcheck --observe. The whole-novel figures
that no page can rebuild (55.4%, 45%, and the question marks per thousand
words of the novel and the play) are quoted, and labelled as quoted wherever
they appear.

Spoken forms: the four key lines of "asking-a-question" that carry an arrow
keep the forms already in content/spoken/english.py. The worked block of
"how-people-really-ask" is six lines from the play, one for each box the lab
fills, each with a plain-words gloss under it; only "A hand-bag?" needs a form
(the hyphen), and it is in content/spoken/english_c3_word_order.py.

Row-level claims (which lines sit in which box, and the hand sort of the
"something else" and "wh-word" boxes) were read off the built tables with a
node harness over labcheck's DOM shim on 2026-10-10; see
docs/pedagogy/english-word-order.md.
"""

LESSONS = [
    {
        "slug": "asking-a-question",
        "module": "Questions",
        "title": "Asking a Question",
        "one_line": "The rule for questions is real, it covers a little over half of the questions in a novel, and the rest are printed here.",
        "standard": (
            "Finish when you can build a question in English, and say what "
            "the other four in ten of a novel's questions look like.",
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
            "Prejudice</em>, printed with this lesson, it covers 52, which is "
            "57.8%. A run over the whole novel, quoted here because no page "
            "can carry it, gave 55.4%. That is too low to call the rule good "
            "and too high to call it wrong, and the lesson is about the other "
            "four in ten: what questions look like when they do not open with "
            "a helping verb."
        ),
        "key_label": "The rule, and its score",
        "key": [
            "you know       ->  do you know?",
            "she went       ->  did she go?",
            "she can go     ->  can she go?",
            "she went where ->  where did she go?",
            "",
            "90 printed questions: 52 follow it    57.8%",
            "whole novel, quoted                   55.4%",
        ],
        "concepts_intro": "Three ideas carry this lesson.",
        "concepts": [
            (
                "The rule is real",
                "To ask a question with a helping verb, put that verb "
                "before the subject: <em>can she go?</em> If there is no "
                "helping verb, add <em>do</em> in the right form: <em>did "
                "she go?</em> It is the same <em>do</em> that arrives to "
                "carry <em>not</em> in Helping Verbs. With a question word, "
                "the question word comes "
                "first and the rest follows: <em>where did she go?</em> "
                "Many languages ask a question by tone, by a small word at "
                "the end, or by an ending on the verb. English moves a "
                "word, and that is why the rule is worth stating. The "
                "helping verbs are the ones that Helping Verbs lists, and "
                "the question word is also called a wh-word, after the "
                "letters most of them start with.",
            ),
            (
                "A little over half of real questions open that way",
                "On the 90 printed questions the rule covers 52, which is "
                "57.8%; on the whole novel, quoted, 55.4%. Where the other "
                "lessons found a small set of named misses, this one finds "
                "a spread. Of the 38 misses here, 16 begin with a joining "
                "word such as <em>and</em> or <em>but</em>, 7 begin with a "
                "question word that has no helping verb after it, 4 begin "
                "with a pronoun and are statements with a question mark on "
                "them, 2 begin with a small word of address such as "
                "<em>oh</em>, and 9 the lab can only call something else. "
                "The largest kind is a result of how people write, not of "
                "how English builds questions.",
            ),
            (
                "A counted figure and a quoted one are different things",
                "The boxes are counted in your browser on the 90 lines you "
                "can read. The figures 55.4% and 45% come from a single run "
                "over the whole novel, which no page can carry, so they are "
                "quoted, and the page says so each time. The two sets are "
                "close, 57.8% against 55.4%, and 42.1% against 45%, and "
                "they differ a little because 90 lines are a sample. Each "
                "line on this page starts where its own sentence starts, or "
                "where quoted speech starts again after words such as "
                "<em>said she</em>, so its first word is the question's "
                "first word in all but one line: <em>But what, said she, can "
                "have been his motive?</em> is cut after <em>said she</em> "
                "and counted from <em>can</em>. The table lets you check any "
                "line.",
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
                "verb goes back to its bare form, as Helping Verbs calls it, "
                "and <em>do</em> takes the tense.",
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
            "source": "austen",
            "panel_title": "Score the rule on ninety real questions",
            "panel_intro": (
                "The table holds 90 questions from the novel, each starting "
                "where its sentence starts and ending at its question mark, "
                "and prints every one with its verdict. The rule holds when "
                "the first word is a helping verb, or a question word "
                "followed by one. The first two boxes are the hit rate. The "
                "next two count the misses that begin with a joining word "
                "such as <em>and</em> or <em>but</em>, and give that count as "
                "a share of all the misses. The next four boxes sort the "
                "rest by their first words: a question word with no helping "
                "verb after it, a small word of address first, a pronoun "
                "first, which makes a statement with a question mark on it, "
                "and no verb at all. The boxes are tried in that order, so a "
                "line is counted once, under the first that fits: <em>But why "
                "all this secrecy?</em> has no verb, and sits under the "
                "joining word. The box called <em>something else</em> "
                "holds what fits none of these; read those lines, because "
                "they are the part the count cannot name. The last two boxes "
                "search the two modern documents printed below the table for "
                "a question mark: the Supreme Court opinion <em>Stanley v. "
                "City of Sanford</em>, 606 U.S. 46 (2025), and the Census "
                "Bureau story &ldquo;U.S. Population Aging as Nation Turns "
                "250&rdquo; (9 April 2026). The questions are 1810s English, "
                "and the way people ask questions has changed since."
            ),
        }),
        "read_title": "What the rule did not catch",
        "read_intro": (
            "On the 90 printed questions, 38 did not open with a helping "
            "verb. Here is what they were, in order of size, with the one "
            "share the whole-novel run measured beside them."
        ),
        "worked": {
            "title": "Five kinds of question that skipped the rule",
            "intro": [
                "The first block is counted on the page, one box for each "
                "kind. The second block is quoted from the run over the "
                "whole novel, which this page cannot repeat, and only one "
                "share was measured there.",
            ],
            "lines": [
                "the 90 printed questions, counted on the page: 38 misses",
                "joining word first: 16 of 38 misses    42.1%",
                "  And what is your success?  But are you pleased, Jane?",
                "question word, no helping verb after it   7",
                "  What say you, Mary?  What made you so shy of me?",
                "a pronoun first, a statement              4",
                "  I must ask whether you were surprised?",
                "a small word of address first             2",
                "  Oh, why is not everybody as happy?",
                "something else                            9",
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
                "word stands first. In most of the sixteen the rest of the "
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
                "reads only the second word. One has a long phrase after "
                "<em>why</em> and then the subject and verb in statement "
                "order. One has no verb: <em>What, none of you?</em>",
                "The third kind starts with a pronoun, so it is a "
                "statement with a question mark on it. <em>I must ask "
                "whether you were surprised?</em> is one. Three of the four "
                "end a longer sentence with a question inside it. The "
                "fourth kind opens with a small word of address or feeling, "
                "<em>Oh</em> or <em>Well</em>, and then follows the rule.",
                "The mixed bag has nine. Two start with a name, "
                "<em>Girls, can I do anything for you in Meryton?</em> and "
                "<em>Miss Bennet, do you know who I am?</em> One starts with "
                "a clause, <em>If she does not object to it, why should "
                "we?</em> Five are long sentences that end in a question. "
                "The last, <em>Your father&rsquo;s estate is entailed on "
                "Mr. Collins, I think?</em>, is a statement with a question "
                "mark that starts with a noun, not a pronoun, so the pronoun "
                "box could not catch it. The count had no name ready for any "
                "of these, and the table shows them.",
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
                "Believing the number means the rule is wrong",
                "57.8% on 90 old questions is a fact about how people write "
                "questions, not about how English builds a question. Most of "
                "the misses that begin with <em>and</em> or <em>but</em> "
                "follow the rule after it. Do not drop the rule. Do not lean "
                "on the figure either.",
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
                    "past form, and the main verb goes back to its bare form."
                ),
            },
            {
                "q": "On the 90 printed questions, how many open the way the rule says?",
                "a": [
                    "All 90",
                    "52, which is 57.8%",
                    "None",
                    "16, which is 42.1%",
                ],
                "c": 1,
                "why": (
                    "The lab counts 52 of 90 in your browser. The 16 is the "
                    "number of misses that begin with a joining word, and "
                    "42.1% is their share of the 38 misses."
                ),
            },
            {
                "q": "What share of the 38 misses begin with a joining word such as <em>and</em> or <em>but</em>?",
                "a": [
                    "All 38",
                    "About 90%",
                    "16 of 38, which is 42.1%",
                    "None",
                ],
                "c": 2,
                "why": (
                    "The joining word stands first, so a check at the front "
                    "of the sentence misses it. The whole-novel run, quoted, "
                    "put this kind at 45% of its misses; the 90 lines are a "
                    "sample and give 42.1%."
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
             "This is the lesson where the rule covers only a little over "
             "half of what is printed, and that is part of what it teaches."),
            ("h3", "The rule"),
            ("p",
             "Every learner is taught how to ask a question. A helping verb "
             "goes before the subject. If there is no helping verb, add "
             "<em>do</em>. If there is a question word, it goes first. "
             "<em>Can you go? Did you go? Where did you go?</em> It is a "
             "short rule. It matters most to a speaker of a language that "
             "asks with a small word at the end of the sentence, such as "
             "Mandarin or Japanese, or by the voice alone, and to a speaker "
             "of Spanish or Russian, where the subject and verb may swap "
             "with no help word at all."),
            ("h3", "The score"),
            ("p",
             "The lab holds 90 questions from <em>Pride and Prejudice</em>, "
             "each one starting where its sentence starts and ending at its "
             "question mark, and prints every one. The rule covers 52 of "
             "them, which is 57.8%. A run over the whole novel, quoted here "
             "because no page can carry it, gave 55.4%. For a rule that is "
             "taught first, that is a modest figure. It is worth asking "
             "why."),
            ("h3", "What the misses looked like"),
            ("ul", [
                "<strong>A joining word first, 16 of the 38 misses, "
                "42.1%.</strong> <em>And what is your success? But why "
                "should you wish to persuade me?</em> A check for the helping "
                "verb at the front misses these. In most of them the question "
                "follows the rule after the joining word.",
                "<strong>A question word with no helping verb after it, "
                "7.</strong> <em>What say you, Mary?</em> is a form older "
                "English used without <em>do</em>, and three of the seven are "
                "that. <em>What made you so shy of me?</em> has the question "
                "word as its subject, so nothing moves, and the rule itself "
                "says so. <em>What sort of girl is Miss King?</em> puts a "
                "longer question phrase first. The other two are a long "
                "phrase after <em>why</em> with the subject and verb in "
                "statement order, and <em>What, none of you?</em>, which has "
                "no verb.",
                "<strong>A pronoun first, 4.</strong> <em>I must ask whether "
                "you were surprised?</em> This is a statement with a "
                "question mark on it. Three of the four are a longer "
                "sentence that ends with the question.",
                "<strong>A small word of address first, 2.</strong> <em>Oh, "
                "why is not everybody as happy?</em> The <em>oh</em> stands "
                "in front, and the rule follows.",
                "<strong>Something else, 9.</strong> Two begin with a "
                "name, <em>Miss Bennet, do you know who I am?</em> One begins "
                "with a clause, <em>If she does not object to it, why should "
                "we?</em> Five are long sentences that end in a question. One "
                "is a statement with a question mark that starts with a noun: "
                "<em>Your father&rsquo;s estate is entailed on Mr. Collins, I "
                "think?</em>",
            ]),
            ("p",
             "The box called <em>no verb at all</em> reads 0 here, though two "
             "of the 38 have no verb: <em>But why all this secrecy?</em> and "
             "<em>What, none of you?</em> The lab sorts by the first word "
             "first, so each sits under its joining word or its question "
             "word. On the play, in the next lesson, that box fills."),
            ("p",
             "The whole-novel run, quoted, found the joining word in 45% of "
             "its misses, and that is the only share it measured; the other "
             "kinds were named there without a number. On the 90 lines the "
             "share is 42.1%. The difference is what a sample of 90 looks "
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
             "most need when they talk. The next lesson, How People Really "
             "Ask, scores the same rule on a play, which is the nearest "
             "thing to talk that can be printed."),
            ("h3", "How to use this"),
            ("p",
             "Use the rule. Expect to meet many questions that break it, "
             "and learn the kinds. Treat the 57.8% as a fact about this "
             "novel, not as a verdict on the rule."),
        ],
    },
    {
        "slug": "how-people-really-ask",
        "module": "Questions",
        "title": "How People Really Ask",
        "one_line": "On the lines of a play, the same rule covers about a third, and the rest are short, fronted, or statements with a question mark.",
        "standard": (
            "Finish when you can say what share of a play's questions follow "
            "the helping-verb rule, and name the kinds that make up the rest.",
            "You should be able to read the rule's score off the 256 "
            "questions printed with this lesson, name the five kinds of "
            "question the count names and the one it cannot, sort a new line "
            "into one of them by its first words, and say why a low score "
            "is not a reason to drop the rule.",
        ),
        "summary": (
            "The last lesson scored the question rule on a novel and found "
            "that it covers 52 of 90 questions, 57.8%. A novel is written to "
            "be read. A play is written to be said, so it is the nearest "
            "thing to talk that can be printed. This lesson scores the same "
            "rule on <em>The Importance of Being Earnest</em> (1895). On the "
            "256 questions of two words or more printed with the lesson, the "
            "rule holds for 89, which is 34.8%. The rest are not mistakes. "
            "They are questions that start with a name, with <em>and</em>, "
            "with a <dfn>pronoun</dfn> such as <em>you</em> or <em>I</em>, "
            "or with a few words and no verb."
        ),
        "key_label": "The same rule, on a play",
        "key": [
            "helping verb first, or question word then one",
            "",
            "the play, 256 questions: 89 follow it  34.8%",
            "the novel, 90 questions: 52 follow it  57.8%",
            "",
            "joining word 35, name or oh 20, pronoun 27",
            "question word alone 24, no verb 14, other 47",
        ],
        "concepts_intro": "Three ideas carry this lesson.",
        "concepts": [
            (
                "The same rule, on text that is written to be said",
                "A play is not recorded speech. Wilde wrote every line, in "
                "1895. But the lines are written to be said aloud by "
                "people who are talking to each other, and they ask far "
                "more questions than a novel does. Counted once over each "
                "whole text and quoted here, the play has 13.1 question "
                "marks for every thousand words and the novel 3.9. On the 256 questions printed under "
                "the lab, the rule holds for 89, which is 34.8%, against "
                "57.8% on the novel in the last lesson.",
            ),
            (
                "A low score is not a verdict on the rule",
                "It would be easy to read 34.8% and say that the rule is "
                "wrong. Read the table instead. The rule describes a "
                "question that is a full sentence, and a large part of what "
                "people ask is not that: a name and then a question, a "
                "statement with a question mark on it, a few words with no "
                "verb. The rule is still how you build a question that has "
                "to stand alone. The score says how much of talk is not "
                "built that way.",
            ),
            (
                "The misses sort into kinds by their first words",
                "Of the 256 questions, 167 do not follow the rule. 35 of "
                "them, 21.0%, begin with a joining word. 27 begin with a "
                "pronoun, which makes a statement with a question mark on "
                "it. 24 begin with a question word that has no helping verb "
                "straight after it. 20 begin with a word of address, such "
                "as a name. 14 have no verb at all. Those five kinds name "
                "120 of the 167. The other 47 are in the box called "
                "<em>something else</em>, and the table shows them.",
            ),
        ],
        "steps_title": "Sorting a question by its first words",
        "steps_intro": "To sort a question you hear or read, do this.",
        "steps": [
            (
                "Read the first word",
                "If it is a helping verb, or a question word and then a "
                "helping verb, the question follows the rule: <em>Do you "
                "smoke?</em> Nothing more to sort.",
            ),
            (
                "Set aside a name, oh or a joining word, and read again",
                "<em>Gwendolen, will you marry me?</em> starts with a name. "
                "<em>And when was the engagement settled?</em> starts with "
                "a joining word. After the first word the rule follows in "
                "both. Say which kind opened the line.",
            ),
            (
                "If a pronoun comes first, it is a statement",
                "<em>You don&rsquo;t mean to say Gwendolen refused you?</em> "
                "has the order of a statement. Only the question mark, or "
                "the voice going up, makes it a question.",
            ),
            (
                "If there is no verb, it is a short piece",
                "<em>Your guardian?</em> and <em>His luggage?</em> repeat "
                "or ask about something just said. Alone, they ask nothing, "
                "and the talk around them is what gives them a meaning.",
            ),
            (
                "Do not count a question word and a phrase as a mistake",
                "<em>How old are you?</em> follows the rule. The count reads "
                "only the word after <em>how</em>, so it puts the line "
                "among the misses. When you sort by eye, look past the "
                "phrase to the helping verb.",
            ),
        ],
        "lab": ("english", {
            "mode": "questions",
            "source": "wilde",
            "panel_title": "Score the rule on a play",
            "panel_intro": (
                "The table holds 256 questions from <em>The Importance of "
                "Being Earnest</em> (1895), a play. A question here is a sentence that ends in a "
                "question mark and has two words or more; each one starts "
                "where its sentence starts, and a stage direction starts a "
                "new sentence. The rule holds when the first word is a "
                "helping verb, or a question word followed by one. The "
                "first two boxes are the hit rate. The next two count the "
                "misses that begin with a joining word, as a share of all "
                "the misses. The next four boxes sort the rest by their "
                "first words: a question word with no helping verb after "
                "it, a word of address first, a pronoun first, and no verb "
                "at all. A word of address is <em>oh</em>, <em>well</em> or "
                "<em>pray</em>, or a name of the play&rsquo;s cast with a "
                "comma after it. The boxes are tried in that order, so each "
                "line is counted once, under the first that fits. The box "
                "called <em>something else</em> "
                "holds what fits none of these. The last two boxes search "
                "the two modern documents printed below the table for a "
                "question mark: the Supreme Court opinion <em>Stanley v. "
                "City of Sanford</em>, 606 U.S. 46 (2025), and the Census "
                "Bureau story &ldquo;U.S. Population Aging as Nation Turns "
                "250&rdquo; (9 April 2026). The play is 1895 English, and "
                "the lines were written by one man, not recorded."
            ),
        }),
        "read_title": "What people ask when they do not use the rule",
        "read_intro": (
            "On the 256 printed questions, 167 did not open with a helping "
            "verb. Here is what they were, with a line from the play for "
            "each kind."
        ),
        "worked": {
            "title": "Six lines, six kinds",
            "intro": [
                "Each line is in the table, one for each box the lab fills, "
                "in the order the lab tries them. The words under each line "
                "say what it is, in plain terms.",
            ],
            "lines": [
                "And when was the engagement actually settled?",
                "  a joining word first; the rule follows",
                "How old are you?",
                "  a question word, no helper straight after it",
                "Gwendolen, will you marry me?",
                "  a word of address first; the rule follows",
                "You don't mean to say Gwendolen refused you?",
                "  a pronoun first: a statement with a question mark",
                "Your guardian?",
                "  no verb at all: a thing repeated back",
                "A hand-bag?",
                "  something else: hand and bag are on the verb lists",
            ],
            "after": [
                "The first line follows the rule once <em>and</em> is set "
                "aside; the count stops at the joining word. The second "
                "follows it too: <em>are</em> stands before <em>you</em>, but "
                "the count reads only the word straight after <em>how</em>, "
                "and <em>old</em> is not a helping verb. The third is a full "
                "question after the name, so the rule is not broken; it only "
                "starts with a word the rule does not mention.",
                "The fourth has the order of a statement. In print the "
                "question mark is the only sign that it asks; on the stage "
                "the voice would do it. The fifth is two words with no verb, "
                "a thing repeated back to the speaker. The sixth is the same "
                "kind of thing, but the lab does not call it &ldquo;no verb "
                "at all&rdquo;, because <em>hand</em> and <em>bag</em> are "
                "both on the printed verb lists. Read it as what it is: a "
                "thing repeated, which the talk around it gives a meaning.",
            ],
        },
        "note": (
            "The 89 of 256 is counted on the page. The 13.1 and 3.9 question "
            "marks per thousand words are quoted: each was counted once over "
            "a whole text, and no page carries a whole text. The play is a "
            "play, so its lines are made-up talk of 1895, and it shows what "
            "question forms writers put in people&rsquo;s mouths."
        ),
        "mistakes": [
            (
                "Reading the low score as proof the rule is wrong",
                "34.8% does not say that the rule fails. It says that most "
                "of the questions printed in a play are not full sentences "
                "of the kind the rule builds. They are short, or they start "
                "with a name, or they are statements with a question mark. "
                "The rule is still how you build the question that must "
                "stand alone.",
            ),
            (
                "Copying a short piece without the talk around it",
                "<em>A hand-bag?</em> works on the stage because someone has "
                "just said <em>hand-bag</em>. Said alone, it asks "
                "nothing. A short piece repeats or follows what was just "
                "said; use the full form when nothing came before.",
            ),
            (
                "Counting a question word and a phrase as a break in the rule",
                "The count looks at the word after the question word, and "
                "<em>old</em> is not a helping verb, so it files the line "
                "with the misses. The sentence follows the rule. Twelve of "
                "the 24 are like this, and twelve are not, so the table is "
                "worth reading line by line.",
            ),
        ],
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "On the 256 printed questions from the play, how many open the way the rule says?",
                "a": [
                    "All 256",
                    "About half, 128",
                    "89, which is 34.8%",
                    "35, which is 21.0%",
                ],
                "c": 2,
                "why": (
                    "The lab counts 89 of 256 in your browser. The 35 is the "
                    "number of misses that begin with a joining word, and "
                    "21.0% is their share of the 167 misses."
                ),
            },
            {
                "q": "Which line is a statement with a question mark on it?",
                "a": [
                    "<em>You don&rsquo;t mean to say Gwendolen refused you?</em>",
                    "<em>Gwendolen, will you marry me?</em>",
                    "<em>Do you smoke?</em>",
                    "<em>How dare you?</em>",
                ],
                "c": 0,
                "why": (
                    "It has the order of a statement: the pronoun comes "
                    "first and the verb after it. The second line starts "
                    "with a name and then follows the rule. The third "
                    "follows the rule, and the fourth puts <em>dare</em> "
                    "straight after the question word, a verb the count does "
                    "not list as a helping verb."
                ),
            },
            {
                "q": "The lab counts <em>How old are you?</em> among the misses. What is the fair reading?",
                "a": [
                    "The sentence breaks the rule",
                    "The speaker made a mistake",
                    "The line has no verb at all",
                    "The count read only the word after <em>how</em>, so this is a limit of the count",
                ],
                "c": 3,
                "why": (
                    "<em>Are</em> is a helping verb and comes before "
                    "<em>you</em>, as the rule says. The count looks only "
                    "at the word straight after the question word, and "
                    "that word is <em>old</em>."
                ),
            },
            {
                "q": "What is the best reading of 34.8% on the play?",
                "a": [
                    "The rule is wrong for English",
                    "Many printed questions are short, start with a name, or are statements with a question mark",
                    "The lab cannot read plays",
                    "People in the play ask few questions",
                ],
                "c": 1,
                "why": (
                    "The table shows the kinds. Names, joining words, "
                    "pronouns and short pieces make up most of the misses. "
                    "The play also asks many questions: 13.1 question marks "
                    "per thousand words against 3.9 in the novel, both "
                    "quoted."
                ),
            },
        ],
        "body": [
            ("p",
             "The last lesson found that the question rule covers a little "
             "over half of a novel&rsquo;s questions. A novel is written to be "
             "read, and its questions are often long and careful. What happens "
             "to the rule on a text that is written to be said?"),
            ("h3", "The text"),
            ("p",
             "The lab holds the questions of <em>The Importance of Being "
             "Earnest</em>, a play by Oscar Wilde, first staged in 1895. It "
             "is not recorded speech: every line is made up, and the "
             "people in it talk in the way that Wilde wished them to. But "
             "it is the nearest thing to talk that a page can carry for "
             "free, and it asks a great many questions. Counted once over "
             "each whole text, and quoted here, it has 13.1 question marks "
             "for every thousand words. The novel has 3.9. The two modern "
             "documents printed under the lab have none."),
            ("h3", "The score"),
            ("p",
             "The lab keeps every question of two words or more, and there "
             "are 256. The rule holds for 89 of them, which is 34.8%. "
             "On the novel in the last lesson it held for 52 of 90, which "
             "is 57.8%. The rule did not change. The questions did."),
            ("h3", "What the 167 misses are"),
            ("ul", [
                "<strong>A joining word first, 35, which is 21.0% of the "
                "misses.</strong> <em>And when was the engagement actually "
                "settled?</em> In many, take the first word away and the "
                "rule follows. Others are statements with a <dfn>tag</dfn> "
                "on the end, a short question hung on a statement: <em>And "
                "you will shake hands with him, won&rsquo;t you, Uncle "
                "Jack?</em> The count also lists <em>then</em> and "
                "<em>for</em> here, and two lines, <em>For the last three "
                "months?</em> and <em>For my sake you are prepared to do "
                "this terrible thing?</em>, begin with <em>for</em> as a "
                "small word of time or reason, not as a joining word.",
                "<strong>A pronoun first, 27.</strong> <em>I beg your "
                "pardon?</em> is in the play three times. <em>I suppose that "
                "is all right?</em> The order is that of a statement, and "
                "the question mark does the asking; in nine of them a short "
                "tag at the end asks as well, <em>You will marry me, "
                "won&rsquo;t you?</em>",
                "<strong>A question word with no helping verb after it, "
                "24.</strong> Twelve follow the rule after a short phrase: "
                "<em>What on earth do you mean?</em> <em>How old are "
                "you?</em> Three have the question word as their subject, so "
                "nothing moves: <em>What brings you up to town?</em> Eight "
                "have no verb at all but begin with a question word, so they "
                "are counted here first: <em>Why cucumber sandwiches?</em> "
                "<em>How many bedrooms?</em> One is <em>How dare you?</em>, "
                "where <em>dare</em> stands straight after the question "
                "word; Helping Verbs says <em>dare</em> works much like "
                "<em>can</em> and <em>must</em>, and the count does not list "
                "it with them.",
                "<strong>A word of address first, 20.</strong> "
                "<em>Gwendolen, will you marry me?</em> <em>Miss Prism, you "
                "are, I trust, well?</em> The name comes first, and what "
                "follows may be a full question or a statement. <em>Oh</em>, "
                "<em>well</em> and <em>my dear fellow</em> are counted here "
                "too: <em>Well, what shall we do?</em>",
                "<strong>No verb at all, 14.</strong> <em>Your "
                "guardian?</em> <em>His luggage?</em> <em>More shameful "
                "debts and extravagance?</em> These repeat or follow what "
                "was just said. One of the 14, <em>Never forgive me?</em>, "
                "has a verb that the printed lists do not hold, so the lab "
                "cannot see it.",
            ]),
            ("p",
             "Those five kinds name 120 of the 167. The other 47 are "
             "something else, and a reader can sort them by eye. Nine are "
             "statements with a tag on the end: <em>It&rsquo;s very pretty, "
             "isn&rsquo;t it?</em> Twelve are statements with a question "
             "mark that begin with a noun or a phrase rather than a pronoun, "
             "so the pronoun box could not catch them: <em>My brother is in "
             "the dining-room?</em> Nine open with a small word or two the "
             "count does not list: <em>yes</em>, <em>now</em>, "
             "<em>really</em>, <em>of course</em>, <em>by the way</em>. Five "
             "put a phrase first and then follow the rule: <em>At what hour "
             "would you wish the ceremony performed?</em> Eleven are short, "
             "most of them one thing repeated back to the speaker: <em>A "
             "hand-bag?</em> <em>The fools?</em> <em>Finished what, may I "
             "ask?</em> The lab does not call them &ldquo;no verb&rdquo; "
             "because a word in each, <em>hand</em>, <em>fools</em>, "
             "<em>finished</em>, is on the printed verb lists. One, "
             "<em>Algy, could you wait for me till I was "
             "thirty-five?</em>, starts with a name the cast list spells "
             "<em>Algernon</em>."),
            ("h3", "What the count cannot tell"),
            ("p",
             "The count reads a line by its first one or two words and no "
             "more. It cannot tell a question that follows the rule after a "
             "short phrase from one that does not, and 24 lines are "
             "filed under a question word with no helping verb after it "
             "for that reason, twelve of which follow the rule. It cannot "
             "see a pronoun with a short word stuck to it: <em>It&rsquo;s "
             "very pretty, isn&rsquo;t it?</em> and <em>You&rsquo;ll never "
             "break off our engagement again, Cecily?</em> are statements "
             "with a question mark, and the pronoun box did not catch them "
             "because their first words are <em>it&rsquo;s</em> and "
             "<em>you&rsquo;ll</em>. Its list of joining words holds "
             "<em>for</em> and <em>then</em>, so <em>For the last three "
             "months?</em> and <em>Then you think we should forgive "
             "them?</em> are counted as joining words, though neither joins "
             "two sentences there. It also cannot hear. A statement with a question mark may be said "
             "with a rising voice, and a page has only the mark. The play "
             "is a play: these are the forms a writer chose to give to "
             "people who are talking, in 1895."),
            ("h3", "What to do with this"),
            ("p",
             "Keep the rule. It is how you ask a question that has to stand "
             "alone, and it is right for a third of what is printed in a "
             "play and for a little over half in a novel. Then learn to "
             "hear the other kinds. A name before a question, a joining "
             "word, a pronoun with a rising voice, and a few words repeated "
             "back are not mistakes. They are most of what you will be "
             "asked."),
            ("p",
             "This is the same finding as the rest of the course. Each rule "
             "is real, each score is below one hundred, and the part that is "
             "left over is made of kinds you can name."),
        ],
    },
]
