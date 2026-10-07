# -*- coding: utf-8 -*-
"""Lesson one of the word-order course: who does what to whom.

The rule is scored on raw printed text with nothing marked up by hand, because
English shows the subject of an action in the pronoun itself (I/me, he/him).
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
            "the rule that a subject pronoun is followed by its verb, say how "
            "often that held on a whole novel, and name each kind of sentence "
            "that looked like an exception.",
        ),
        "summary": (
            "In many languages an ending on a word says who does the action, so "
            "the words can move. Many languages work "
            "this way to some degree, such as Spanish, Russian, Japanese and Korean. English has lost most of those endings, "
            "and keeps position instead. The one place it still marks the subject "
            "is the <dfn>pronoun</dfn>, and the pairs <dfn>pronouns</dfn> come in: <em>I</em> and <em>me</em>, <em>he</em> "
            "and <em>him</em>. That makes one rule easy to test on printed text: "
            "a <dfn>subject</dfn> pronoun is followed by its <dfn>verb</dfn>. "
            "Over a whole novel it held 88.7% of the time, and the rest is "
            "four named groups."
        ),
        "key_label": "The rule, and its score on one novel",
        "key": [
            "subject    I    he   she   we   they",
            "object     me   him  her   us   them",
            "",
            "rule: subject pronoun, then its verb",
            "",
            "5,990 subject pronouns       100.0%",
            "followed by a verb            88.7%",
            "real order mistakes found        0",
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
                "does carry the role. <em>He saw her</em> cannot mean the "
                "reverse, because <em>he</em> is only ever the subject and "
                "<em>her</em> is only ever the one it happens to. The pronoun "
                "is what lets a printed text be scored with nothing marked by hand.",
            ),
            (
                "A strict rule with an honest score",
                "The rule is: a subject pronoun &mdash; <em>I, he, she, we, "
                "they</em> &mdash; is followed directly by its verb. The "
                "word <em>you</em> and the word <em>it</em> look the same in "
                "both roles, so they cannot be scored this way and are left "
                "out. On <em>Pride and Prejudice</em> the rule found 5,990 "
                "subject pronouns, and 88.7% were followed by a verb. That "
                "number is not the end of the story. The other 11.3% is where "
                "the lesson is.",
            ),
            (
                "The misses are four named groups, not one failure",
                "A <dfn>modifier</dfn> stood between pronoun and verb in 63% of the "
                "remaining cases. The next word was not in the printed word "
                "list in 16%. A <dfn>speech tag</dfn>, as in <em>said he</em>, "
                "accounted for 15%. The last 6% we have not sorted. Each of "
                "the first three has a reason that does not break the rule, "
                "and the next section shows them.",
            ),
        ],
        "steps_title": "Finding the subject in a sentence",
        "steps_intro": "To read who does what, do this.",
        "steps": [
            (
                "Look for a pronoun first",
                "<em>I, he, she, we, they</em> are always the subject. "
                "<em>Me, him, her, us, them</em> are never the subject. This "
                "needs no grammar words and no guessing.",
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
            "panel_title": "Score the rule on the novel yourself",
            "panel_intro": (
                "The lab scans a shorter stretch of the same novel: 949 "
                "words with 126 subject pronouns, printed beside the 141 verb "
                "forms that occur in it. Each pronoun is found and the word "
                "after it is checked against that printed list. The first "
                "box is the hit rate. The next boxes are the four groups the "
                "misses fall into, and the last counts real order mistakes. "
                "The figure will not match the 88.7% for the whole novel, "
                "because this is a smaller passage full of speech. The text "
                "is 1810s English, so the groups describe that period, not "
                "speech today."
            ),
        }),
        "read_title": "Where the rule seemed to fail",
        "read_intro": (
            "677 or so of the 5,990 pronouns were not followed by a verb. "
            "Here is what they were, in order of size."
        ),
        "worked": {
            "title": "Four groups, and no real mistake",
            "intro": [
                "The shares below are shares of the misses, not of all "
                "pronouns.",
            ],
            "lines": [
                "modifier between      63%",
                "  they both knew, we all, he who",
                "next word not in list 16%",
                "  beg, inquired",
                "speech tag         15%",
                "  said he, cried she",
                "other                  6%",
                "real order mistakes    0 found",
            ],
            "after": [
                "The first group is a normal word between two words that "
                "belong together. The second is a gap in the word list, not "
                "in the text: Austen used <em>beg</em> and <em>inquired</em> "
                "where a list of common words has none. The third is one "
                "device. Every case we read was a speech tag, and a "
                "second check found 88% of the cases beside quoted speech.",
                "We cannot speak for the last 6%. We read a "
                "sample of it and of the other groups and found no case of a "
                "pronoun in the wrong place. We did not read every case, "
                "so the honest claim is that we found none, not that none "
                "exist.",
            ],
        },
        "note": (
            "Sorting the misses into groups is the whole method. A number "
            "like 88.7% says the rule is good. The groups say why it is not "
            "100%, and that is what you can use."
        ),
        "mistakes": [
            (
                "Treating <em>said he</em> as a new word order",
                "It looks like a pattern you could copy. It is a habit of "
                "older stories, and only after quoted speech. In speech today "
                "you say <em>he said</em>. Do not use it to be correct.",
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
                    "English pronouns show their own role, as in <em>he</em> and <em>him</em>",
                    "Every English noun carries an ending for its role",
                    "A person has read each page and marked the verbs",
                    "English sentences are always four words long",
                ],
                "c": 0,
                "why": (
                    "<em>He</em> is only ever the subject and <em>him</em> only "
                    "the one it happens to, so the pronoun itself says which role it "
                    "plays. Nouns have no such ending."
                ),
            },
            {
                "q": "A subject pronoun is followed by its verb 88.7% of the time. What is the largest group among the rest?",
                "a": [
                    "A modifier between pronoun and verb",
                    "A speech tag such as <em>said he</em>",
                    "A word missing from the word list",
                    "A real mistake by the writer",
                ],
                "c": 0,
                "why": (
                    "A word such as <em>both</em> or <em>all</em> sat between "
                    "them in 63% of the misses. The tag was 15% and the word "
                    "list gap 16%."
                ),
            },
            {
                "q": "Why does the course measure on a novel from the 1810s?",
                "a": [
                    "Modern formal writing has far fewer of these pronouns",
                    "Old English is the easiest to learn",
                    "Modern writing has no pronouns",
                    "Novels are the only text that can be scored",
                ],
                "c": 0,
                "why": (
                    "Two modern public documents carry about 4.5 times fewer "
                    "of these pronouns per thousand words. They are not a "
                    "useful place to measure the rule."
                ),
            },
            {
                "q": "What may you claim about real order mistakes in the novel?",
                "a": [
                    "None were found in the cases we read",
                    "There are exactly none, proved over every case",
                    "There are a few hundred",
                    "The rule cannot be tested",
                ],
                "c": 0,
                "why": (
                    "The claim is limited by what was read. A sample of each "
                    "group showed none, but not every case was read."
                ),
            },
        ],
        "body": [
            ("p",
             "Say <em>the dog bit the man</em> in Spanish, and you can move the "
             "words almost anywhere. The ending on the noun or the small word "
             "before it says who did the biting. Russian, Japanese and Korean "
             "do something like this too, each in its own way. English, for "
             "the most part, does not. This lesson is about what it does "
             "instead."),
            ("h3", "What English kept"),
            ("p",
             "Old English had endings on nouns. Almost all of them are gone. "
             "What is left is a small set of pairs of pronouns. <em>I</em> "
             "and <em>me</em>. <em>He</em> and <em>him</em>. <em>She</em> and "
             "<em>her</em>. <em>We</em> and <em>us</em>. <em>They</em> and "
             "<em>them</em>. The first of each pair is the subject. The second "
             "is who or what it happens to."),
            ("p",
             "Because the pronoun carries the role, there is a rule that needs "
             "no reading of meaning. A subject pronoun is followed by its "
             "verb. A machine can look for <em>he</em> and read the next "
             "word. Nobody has to mark up the page first."),
            ("h3", "The score"),
            ("p",
             "The rule was run over <em>Pride and Prejudice</em>, novel text "
             "only, 122,396 words. It found 5,990 instances of <em>I, he, "
             "she, we</em> and <em>they</em>. In 88.7% the next word was a "
             "verb."),
            ("p",
             "A number like that is easy to read wrongly in two ways. The first is "
             "to call 11.3% a failure rate. The second is to call it noise. "
             "It is neither. It is four things, and each can be named."),
            ("h3", "The four groups"),
            ("ul", [
                "<strong>A modifier in between, 63% of the misses.</strong> "
                "<em>They both knew. We all agreed. He who</em> &mdash; a "
                "small word sits between the pronoun and the verb, and the "
                "verb is still the next main word.",
                "<strong>A word outside the list, 16%.</strong> The tool "
                "only knows the words in a printed list. Austen wrote "
                "<em>beg</em> and <em>inquired</em> where the list has "
                "neither. This is a limit of the tool, not of the sentence.",
                "<strong>A speech tag, 15%.</strong> <em>&ldquo;But it is,&rdquo; "
                "returned she.</em> This is a fixed device of telling a story, "
                "and it only happens beside quoted speech. A check found 88% "
                "of these cases sitting next to quoted speech.",
                "<strong>Other, 6%.</strong> We have not sorted these.",
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
             "no mistake, which is a weaker claim than that there is none."),
            ("h3", "Why a novel from the 1810s"),
            ("p",
             "Two modern public documents were measured as well: an opinion "
             "of the US Supreme Court and a Census Bureau story. Both are "
             "free to use. They carry about 4.5 times fewer of these "
             "pronouns for every thousand words than Austen does. Formal "
             "modern writing is mostly nouns, and the structures a speaker "
             "needs are thin on the page."),
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
