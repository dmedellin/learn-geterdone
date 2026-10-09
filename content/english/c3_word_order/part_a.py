# -*- coding: utf-8 -*-
"""Lesson one of the word-order course: who does what to whom.

The rule is scored on raw printed text with nothing marked up by hand, because
English shows the subject of an action in the pronoun itself (I/me, he/him).
The lab counts the rule on a 949-word passage printed on the page, and counts
the same pronouns per thousand words in two modern public documents printed
beside it. Figures from a run over the whole novel, which no page can carry,
are quoted and labelled as quoted wherever they appear.
"""

LESSONS = [
    {
        "slug": "who-does-what-to-whom",
        "module": "Why English can afford to be strict about order",
        "title": "Who Does What to Whom",
        "one_line": "English shows the subject in the pronoun, and a count shows how exactly the order holds.",
        "standard": (
            "Finish when you can say which word is the subject in an English "
            "sentence, and what usually stands next to it.",
            "You should be able to name the two forms of five pronouns, state "
            "the rule that a subject pronoun is followed by its verb, read its "
            "score off the passage printed with this lesson, and name each kind "
            "of sentence that looked like an exception, including the one the "
            "lab counts as broken.",
        ),
        "summary": (
            "In many languages an ending on a word says who does the action, so "
            "the words can move. Spanish, Russian, Japanese and Korean each do "
            "this to some degree, in their own way. English has lost most of "
            "those endings and keeps position instead. The one place it still "
            "marks the subject is the <dfn>pronoun</dfn>, and the pairs "
            "<dfn>pronouns</dfn> come in: <em>I</em> and <em>me</em>, <em>he</em> "
            "and <em>him</em>. That makes one rule easy to test on printed text: "
            "a <dfn>subject</dfn> pronoun is followed by its <dfn>verb</dfn>. "
            "On the passage printed with this lesson it held for 72 of 80 "
            "subject pronouns, 90.0%. On the whole novel, in a run this page "
            "cannot repeat, it held 88.7% of the time, and the rest is four "
            "named groups."
        ),
        "key_label": "The rule, and its score",
        "key": [
            "subject    I    he   she   we   they",
            "object     me   him  her   us   them",
            "",
            "rule: subject pronoun, then its verb",
            "",
            "printed passage: 72 of 80 hold    90.0%",
            "whole novel, quoted               88.7%",
            "order broken in the passage: 1, a speech tag",
        ],
        "concepts_intro": "Three ideas carry this lesson.",
        "concepts": [
            (
                "Some languages mark the role on the word. English marks it on the pronoun",
                "If the subject of an action is shown by an ending, the subject can "
                "stand almost anywhere and the listener still knows who it is. "
                "English cannot do this with a noun: <em>the dog bit the "
                "man</em> and <em>the man bit the dog</em> use the same words, "
                "and only the order tells you which is which. But a pronoun "
                "does carry the role. <em>He saw them</em> cannot mean the "
                "reverse, because <em>he</em> is only ever the subject and "
                "<em>them</em> is only ever the one it happens to. The pronoun "
                "is what lets a printed text be scored with nothing marked by hand.",
            ),
            (
                "A strict rule with an honest score",
                "The rule is: a subject pronoun &mdash; <em>I, he, she, we, "
                "they</em> &mdash; is followed directly by its verb. The "
                "word <em>you</em> and the word <em>it</em> look the same in "
                "both roles, so they cannot be scored this way and are left "
                "out. On the passage printed below the lab, the rule found 80 "
                "subject pronouns and 72 were followed by a verb, which is "
                "90.0%. A run over the whole of <em>Pride and Prejudice</em>, "
                "quoted here because no page can carry the novel, found 5,990 "
                "and scored 88.7%. Neither number is the end of the story. The "
                "other tenth is where the lesson is.",
            ),
            (
                "The misses are named groups, not one failure",
                "In the whole-novel run, a <dfn>modifier</dfn> stood between "
                "pronoun and verb in 63% of the misses, the next word was not in "
                "the tool's word list in 16%, a <dfn>speech tag</dfn>, as in "
                "<em>said he</em>, accounted for 15%, and 6% were not sorted. "
                "The passage on this page shows the same three kinds in small: "
                "of its eight misses, five have a modifier between, two have a "
                "next word the printed scan does not know, and one is a speech "
                "tag. Each of the three has a reason that does not break the "
                "rule, and the next section shows them.",
            ),
        ],
        "steps_title": "Finding the subject in a sentence",
        "steps_intro": "To read who does what, do this.",
        "steps": [
            (
                "Look for a pronoun first",
                "In careful English, <em>I, he, she, we, they</em> are always "
                "the subject, and <em>me, him, us, them</em> are never the "
                "subject. This needs no grammar words and no guessing. "
                "<em>Her</em> is the one to watch: it is the object form of "
                "<em>she</em> and also the word for belonging, as in <em>her "
                "book</em>.",
            ),
            (
                "If there is no pronoun, use the order",
                "With nouns, the one before the verb is the subject and the one "
                "after is what it happens to. This is the rule your own "
                "language may not use, so say it to yourself slowly at first.",
            ),
            (
                "Allow a small word in between",
                "<em>They both knew</em> and <em>we all agreed</em> put a "
                "word between pronoun and verb. The subject is still the "
                "pronoun, and the verb is still the next main word.",
            ),
            (
                "Check for quoted speech",
                "If the sentence sits beside quoted speech, the subject may "
                "come after the verb: <em>said he</em>. This is a fixed "
                "habit of stories, not a new order.",
            ),
        ],
        "lab": ("english", {
            "mode": "svo",
            "panel_title": "Score the rule on the passage yourself",
            "panel_intro": (
                "The lab scans a 949-word stretch of the novel, printed under "
                "the table. It finds each of the 80 subject pronouns and "
                "checks the word after it against a list of the 141 verb forms "
                "the passage contains, plus 25 small verbs such as <em>had</em>, "
                "<em>was</em> and <em>could</em>; the table shows every pronoun, the word "
                "beside it, and the verdict. The first two boxes are the hit "
                "rate. The box called <em>word order broken</em> counts the "
                "one pronoun whose verb came before it: a speech tag, "
                "<em>said he</em>, which the rule as stated does not cover. The "
                "next box counts a modifier between. The two remaining misses "
                "are a next word the list does not hold, and the table names "
                "them. The last three boxes count the same pronouns per "
                "thousand words in this passage and in the two modern "
                "documents printed below it: an opinion of the US Supreme "
                "Court, <em>Stanley v. City of Sanford</em>, 606 U.S. 46 "
                "(2025), and the Census Bureau story &ldquo;U.S. Population "
                "Aging as Nation Turns 250&rdquo; (9 April 2026). The second "
                "menu switches to the object pronouns <em>me, him, us, "
                "them</em>; <em>her</em> is left out there because it is also "
                "the word for belonging. The text is 1810s English, so the "
                "groups describe that period, not speech today."
            ),
        }),
        "read_title": "Where the rule seemed to fail",
        "read_intro": (
            "On the whole novel, 677 or so of the 5,990 pronouns were not "
            "followed by a verb. Here is what they were, in order of size, "
            "and beside them the eight misses the passage on this page shows."
        ),
        "worked": {
            "title": "Four groups, and no real mistake",
            "intro": [
                "The shares in the first block are quoted from the run over "
                "the whole novel, which this page cannot repeat. They are "
                "shares of the misses, not of all pronouns. The counts in the "
                "second block are what the lab finds on the printed passage.",
            ],
            "lines": [
                "the whole novel, quoted",
                "modifier between      63%",
                "  they both knew, we all, he who",
                "next word not in list 16%",
                "  beg, inquired",
                "speech tag            15%",
                "  said he, cried she",
                "other                  6%",
                "",
                "the printed passage, counted on the page",
                "modifier between       5",
                "  I almost envy, he soon afterwards said",
                "next word not in list  2",
                "  I interrupt, I don't know",
                "speech tag             1",
                "  said he, as he joined them",
            ],
            "after": [
                "The first group is a normal word between two words that "
                "belong together. The second is a gap in the word list, not "
                "in the text: Austen used <em>beg</em> and <em>inquired</em> "
                "where a list of common words has none, and on this page the "
                "scan does not know <em>interrupt</em>, and reads <em>I "
                "don&rsquo;t know</em> as <em>I don</em>, because its idea of "
                "a word stops at the apostrophe Austen's printer used. The "
                "third is one "
                "device. Every case we read was a speech tag, and a second "
                "check, also quoted from the whole-novel run, found 88% of "
                "the cases beside quoted speech.",
                "We cannot speak for the last 6%. We read a sample of it and "
                "of the other groups and found no case of a pronoun in the "
                "wrong place. We did not read every case, so the honest claim "
                "is that we found none, not that none exist. On the printed "
                "passage you can read every one of the eight.",
            ],
        },
        "note": (
            "Sorting the misses into groups is the whole method. A number "
            "like 90.0% says the rule is good. The groups say why it is not "
            "100%, and that is what you can use."
        ),
        "mistakes": [
            (
                "Treating the speech tag as a new word order",
                "<em>Said he</em> looks like a pattern you could copy. It is a "
                "habit of older stories, and only after quoted speech. In "
                "speech today you say <em>he said</em>. Do not use it to be "
                "correct.",
            ),
            (
                "Taking a modifier as a break in the rule",
                "<em>They both knew</em> and <em>we all went</em> are not "
                "exceptions. A word like <em>both</em> or <em>all</em> may "
                "sit between the pronoun and its verb. Nothing else usually "
                "does.",
            ),
            (
                "Moving the words the way your own language would",
                "In a language with endings, <em>him saw he</em> can still "
                "be understood, so the habit is to move words for emphasis. "
                "In English the pronoun form saves you only if you also "
                "keep the order.",
            ),
        ],
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "Why can this rule be scored on printed text with nothing marked by hand?",
                "a": [
                    "Every English noun carries an ending for its role",
                    "A person has read each page and marked the verbs",
                    "English pronouns show their own role, as in <em>he</em> and <em>him</em>",
                    "English sentences are always four words long",
                ],
                "c": 2,
                "why": (
                    "<em>He</em> is only ever the subject and <em>him</em> only "
                    "the one it happens to, so the pronoun itself says which role it "
                    "plays. Nouns have no such ending."
                ),
            },
            {
                "q": "On the printed passage, 72 of 80 subject pronouns are followed by their verb. What is the largest group among the other eight?",
                "a": [
                    "A modifier between pronoun and verb",
                    "A speech tag such as <em>said he</em>",
                    "A word missing from the word list",
                    "A real mistake by the writer",
                ],
                "c": 0,
                "why": (
                    "Five of the eight have a word such as <em>almost</em> or "
                    "<em>soon</em> between them. Two have a next word the list "
                    "does not hold, and one is the speech tag. The whole-novel "
                    "run, quoted, has the same order: 63%, 16%, 15%."
                ),
            },
            {
                "q": "Why does the course measure on a novel from the 1810s?",
                "a": [
                    "Old English is the easiest to learn",
                    "Modern writing has no pronouns",
                    "Novels are the only text that can be scored",
                    "Modern formal writing has far fewer of these pronouns",
                ],
                "c": 3,
                "why": (
                    "The lab counts them. The passage has 84.3 subject pronouns "
                    "per thousand words; the two modern documents, "
                    "<em>Stanley v. City of Sanford</em> and the Census Bureau "
                    "story, have 13.9, about 6.1 times fewer. They are not a "
                    "useful place to measure the rule."
                ),
            },
            {
                "q": "What may you claim about real order mistakes in the novel?",
                "a": [
                    "There are exactly none, proved over every case",
                    "None were found in the cases we read",
                    "There are a few hundred",
                    "The rule cannot be tested",
                ],
                "c": 1,
                "why": (
                    "The claim is limited by what was read. A sample of each "
                    "group showed none, but not every case was read. The one "
                    "case the lab counts as broken is a speech tag."
                ),
            },
        ],
        "body": [
            ("p",
             "Say <em>the dog bit the man</em> in Spanish, and the words can "
             "move: a small word, <em>a</em>, marks the man as the one bitten, "
             "and the verb agrees with the dog. Russian puts the job in an "
             "ending on the noun itself. Japanese and Korean use a small word "
             "after the noun. English, for the most part, does none of this. "
             "This lesson is about what it does instead."),
            ("h3", "What English kept"),
            ("p",
             "Old English had endings on nouns. Almost all of them are gone. "
             "What is left is a small set of pairs of pronouns. <em>I</em> "
             "and <em>me</em>. <em>He</em> and <em>him</em>. <em>She</em> and "
             "<em>her</em>. <em>We</em> and <em>us</em>. <em>They</em> and "
             "<em>them</em>. The first of each pair is the subject. The second "
             "is who or what it happens to. <em>Her</em> also does a second "
             "job, belonging, as in <em>her book</em>, which is why the lab "
             "leaves it out when it counts the object forms."),
            ("p",
             "Because the pronoun carries the role, there is a rule that needs "
             "no reading of meaning. A subject pronoun is followed by its "
             "verb. A machine can look for <em>he</em> and read the next "
             "word. Nobody has to mark up the page first."),
            ("h3", "The score"),
            ("p",
             "The lab runs the rule over a 949-word passage from <em>Pride "
             "and Prejudice</em>, printed on this page. It finds 80 of <em>I, "
             "he, she, we</em> and <em>they</em>, and in 72 of them, 90.0%, "
             "the next word is a verb. The passage also holds 46 of "
             "<em>you</em> and <em>it</em>, and the scan leaves every one "
             "out, because those two words do not change with the job."),
            ("p",
             "The same rule was once run over the whole novel, novel text "
             "only, 122,396 words. It found 5,990 of the five pronouns, and "
             "in 88.7% the next word was a verb. No page can carry the novel, "
             "so that figure is quoted here, not counted in your browser; the "
             "passage is the part you can check."),
            ("p",
             "A number like that is easy to read wrongly in two ways. The first is "
             "to call the other tenth a failure rate. The second is to call it noise. "
             "It is neither. It is a few things, and each can be named."),
            ("h3", "The four groups"),
            ("ul", [
                "<strong>A modifier in between, 63% of the misses in the "
                "whole-novel run, 5 of the 8 on this page.</strong> "
                "<em>They both knew. We all agreed. I almost envy you.</em> A "
                "small word sits between the pronoun and the verb, and the "
                "verb is still the next main word.",
                "<strong>A word outside the list, 16%, and 2 of the 8 "
                "here.</strong> The tool only knows the words in its list. "
                "Austen wrote <em>beg</em> and <em>inquired</em> where the "
                "list has neither, and on this page <em>I interrupt</em> is "
                "scored a miss because the scan does not know "
                "<em>interrupt</em>. This is a limit of the tool, not of the "
                "sentence.",
                "<strong>A speech tag, 15%, and 1 of the 8 here.</strong> "
                "<em>&ldquo;But it is,&rdquo; returned she. &ldquo;My dear "
                "sister,&rdquo; said he.</em> This is a fixed device of "
                "telling a story, and it only happens beside quoted speech. "
                "A check in the whole-novel run, quoted, found 88% of these "
                "cases sitting next to quoted speech. The lab counts it in "
                "the box called <em>word order broken</em>, because the "
                "verb does come before its pronoun; the lesson's claim is "
                "that it is a habit, not an error.",
                "<strong>Other, 6%.</strong> We have not sorted these. The "
                "printed passage has none.",
            ]),
            ("h3", "What was not found"),
            ("p",
             "The result worth knowing is the one that is missing. Among the "
             "cases we read, there was no sentence where a subject pronoun "
             "stood in a place English does not allow. Every apparent "
             "exception was one of the groups above. English order is "
             "strict, and the one device that bends it is a named habit of "
             "telling a story."),
            ("p",
             "We say <em>among the cases we read</em> on purpose. A sample of "
             "each group was read and the speech tags were checked in "
             "full by a second method. The 16% word list gap and the 6% "
             "other were not read case by case. So the claim is that we found "
             "no mistake, which is a weaker claim than that there is none. "
             "On this page the claim is stronger, because the eight misses "
             "are all in the table and you can read each one."),
            ("h3", "Why a novel from the 1810s"),
            ("p",
             "The lab also counts the same pronouns in two modern public "
             "documents, printed in full under the passage: the opinion of "
             "the US Supreme Court in <em>Stanley v. City of Sanford</em>, "
             "606 U.S. 46 (2025), and the Census Bureau story &ldquo;U.S. "
             "Population Aging as Nation Turns 250&rdquo; of 9 April 2026. "
             "Both are free to use. The passage has 84.3 subject pronouns "
             "for every thousand words, 80 in 949; the two documents have "
             "13.9, 24 in 1,723. That is about 6.1 times fewer. For the "
             "object forms the gap is wider still: 19.0 against 1.7 per "
             "thousand, about 10.9 times fewer. Formal modern writing is "
             "mostly nouns, and the structures a speaker needs are thin on "
             "the page."),
            ("p",
             "So the measurements use a novel, and that has a cost. It is "
             "1810s English, and some of what looks like a rule may be the "
             "habit of that time. The speech tag is the clearest case. "
             "This lesson tells you where the age of the text limits a "
             "figure, and the figure that depends on it most is the "
             "15%."),
            ("p",
             "There is a lesson in the gap itself. If you learn English from "
             "formal reading only, you meet far fewer of the forms you need "
             "when you talk. Read stories and speech too."),
        ],
    },
]
