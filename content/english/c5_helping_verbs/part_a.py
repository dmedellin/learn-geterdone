# -*- coding: utf-8 -*-
"""Course three, lessons one to three: agreement, the bare form, and have.

Every figure here is read off the auxchain lab's tiles with `labcheck.js
--observe`: agree 74 of 75 (98.7%, one against); modal 65 of 76 (85.5%, 20
with not or an adverb between, 4 with a pronoun next, 7 something else, none
formed); have 17 of 37 helping verbs (45.9%), 10 of 37 main verbs, 3 with a
pronoun next, 7 something else. The modern documents give 14 of 14, 16 of 17 and 16 of 23. Where a lesson
reads the printed rows by hand it says so and names the rows: two of the four
pronoun rows after a modal are the scan running past a full stop or a comma,
not questions; seven of the chapter's 37 forms of have are helping verbs the
scan filed elsewhere (three participles the list lacks, four with a subject or
a phrase between), so 24 of 37 by hand. Whole-novel figures are the designer's
(docs/english-v2/measure/out/corpus.txt) and are marked quoted wherever they
appear; after he, she and it that output gives 1,081 is/has/does/was plus 133
-s forms, 1,214 third-person forms against 37 others, and the three "formed"
rows after a modal are all a modal at a clause end with the next clause's verb
after the comma.

Spoken forms for the key and worked lines are in
content/spoken/english_c5_helping_verbs.py.
"""

LESSONS = [
    {
        "slug": "the-s-belongs-to-he-she-and-it",
        "module": "One verb, one helping verb",
        "title": "The -s Belongs to He, She and It",
        "one_line": "On a noun the -s means more than one; on a verb it means exactly one.",
        "standard": (
            "Finish when you can say which subject takes the verb form with "
            "-s, which take the other form, and which takes am.",
            "You should be able to choose between is and are, has and have, "
            "does and do, was and were for any subject, read the rule's score "
            "off the pairs in a printed chapter, and name the one kind of row "
            "that breaks it on purpose.",
        ),
        "summary": (
            "On a noun, an <em>-s</em> means more than one: <em>book</em>, "
            "<em>books</em>. On a verb it means the opposite. <em>She "
            "walks</em> has one walker. This lesson states the rule that goes "
            "with it, scores it on every pronoun and the verb after it in one "
            "chapter of a novel, and finds that it holds in 74 pairs of 75."
        ),
        "key_label": "One chapter, every pronoun and the word after it",
        "key": [
            "he, she, it       is   has   does   was",
            "you, we, they     are  have  do     were",
            "I                 am   was   or the bare form",
            "",
            "the rule holds in 74 pairs of 75",
            "the one against it: if I were",
        ],
        "concepts_intro": "Three ideas. The first one corrects a habit from nouns.",
        "concepts": (
            (
                "The -s on a verb does not mean more than one",
                "On a noun the ending marks more than one. On a verb it "
                "marks a subject that is exactly one thing and is not you "
                "or me: <em>he</em>, <em>she</em>, <em>it</em>, or a name or "
                "a noun that stands for one thing. A word such as "
                "<em>he</em> that stands in for a noun is a "
                "<dfn>pronoun</dfn>. <em>The boy walks</em> "
                "and <em>the boys walk</em> have the ending in opposite "
                "places.",
            ),
            (
                "Three verbs change the word, not the ending",
                "<em>Be</em>, <em>have</em> and <em>do</em> do not add an "
                "-s. They change word: <em>is</em>, <em>has</em>, "
                "<em>does</em>, and <em>was</em> for the past of <em>be</em>. "
                "The same subjects take them. Everyone else takes "
                "<em>are</em>, <em>have</em>, <em>do</em> and <em>were</em>, "
                "and <em>I</em> takes <em>am</em>.",
            ),
            (
                "Only the present tense cares",
                "Look at the rows the lab does not score. They are "
                "<em>she thought</em>, <em>they went</em>, <em>I would</em>. "
                "A past form such as <em>thought</em> and a <dfn>modal</dfn> "
                "verb such as <em>would</em> do not change with the subject, so the "
                "agreement rule has nothing to check. It checks the present "
                "tense, and <em>was</em> against <em>were</em>.",
            ),
        ),
        "steps_title": "Choosing the form for a subject",
        "steps_intro": "Three questions, in this order.",
        "steps": (
            (
                "Is the subject I?",
                "Then use <em>am</em> for <em>be</em>, <em>was</em> in the "
                "past, and the bare form of every other verb: <em>I walk</em>, "
                "<em>I have</em>, <em>I do</em>.",
            ),
            (
                "Is it he, she, it, or one thing that could be called "
                "that?",
                "Then use the third person form: <em>is</em>, <em>has</em>, "
                "<em>does</em>, <em>was</em>, or the bare verb with an "
                "<em>-s</em> on it. <em>The letter says</em>, <em>Jane "
                "has</em>.",
            ),
            (
                "Is it you, we, they, or more than one thing?",
                "Then use <em>are</em>, <em>have</em>, <em>do</em>, "
                "<em>were</em>, or the bare verb. <em>You</em> takes these "
                "even when it means one person.",
            ),
            (
                "Is the verb a modal or a past form?",
                "Then stop. Nothing changes with the subject, and the rule "
                "has nothing to say. <em>She could</em>, <em>they could</em>; "
                "<em>he walked</em>, <em>we walked</em>.",
            ),
        ),
        "lab": ("english", {
            "mode": "auxchain",
            "rule": "agree",
            "panel_title": "Score the rule on every pronoun in the chapter",
            "panel_intro": (
                "The table prints a few words around every pronoun in Chapter "
                "XXVI of <em>Pride and Prejudice</em>, and the verdict "
                "beside it. The first box counts the pronoun subjects the scan looked "
                "at. The next three count the pairs where the word after the "
                "pronoun is a present form, <em>was</em>, <em>were</em> or a "
                "bare verb &mdash; the pairs the rule can score &mdash; and "
                "how many of them hold. The last counts the pairs that go "
                "against the rule. The chapter was written in 1813. Switch "
                "the text to the two modern documents to see the same rule on "
                "writing from 2025 and 2026. Every row not shown is a pair "
                "the rule does not cover, and <em>Show</em> brings it back."
            ),
        }),
        "read_title": "The row that goes against it",
        "read_intro": (
            "One pair in 75 breaks the rule. It breaks it on purpose, and "
            "the rows around it show why."
        ),
        "worked": {
            "title": "Three subjects, three forms, and one that breaks the rule",
            "intro": [
                "Take the same verbs and change the subject. The first three "
                "rows follow the rule. The last is the single row in the "
                "chapter that does not.",
            ],
            "lines": [
                "she was    he has     it does",
                "they were  you have   we do",
                "I am       I was      I know",
                "",
                "against the rule:   if I were not afraid",
            ],
            "after": [
                "<em>I were</em> is not a mistake here. The chapter reads "
                "<em>if I were not afraid of judging</em>, and the "
                "<em>if</em> is the reason: the sentence is about a case that "
                "is not real, and English keeps an old form, <em>were</em>, "
                "for every subject, to say so. The lab prints it as <em>it "
                "if i were not</em> and marks it against the rule. "
                "Counted once over the whole novel, which no page can carry, "
                "and quoted here: after <em>he</em>, <em>she</em> and "
                "<em>it</em> the novel has 1,214 third person forms against "
                "37 others; after <em>you</em>, <em>we</em> and "
                "<em>they</em> it has 487 forms for more than one against 5 "
                "third person ones. Of the 37, 22 are this same form: "
                "<em>if it were</em>, <em>she were</em>, <em>he were</em>. "
                "The other 15, and all 5, are rows the one-word scan "
                "misread: <em>could she have seen</em>, where the helping "
                "verb stands in front of its subject, and <em>believing it "
                "are</em> or <em>required of you is</em>, where the pronoun "
                "is an object and the verb belongs to another subject.",
            ],
        },
        "note": (
            "A hit rate of 98.7% on 75 pairs is a small count. The quoted "
            "whole-novel figures are the check: the rule holds in 1,214 "
            "of 1,251 pairs after <em>he</em>, <em>she</em> and <em>it</em> "
            "and in 487 of 492 after the others. The two modern "
            "documents give 14 pairs of 14. The chapter is no accident, and "
            "it is also not the whole language: the lab reads one word after "
            "the pronoun and cannot tell <em>it</em> as an object from "
            "<em>it</em> as a subject."
        ),
        "mistakes": (
            (
                "Putting the -s on a verb for more than one",
                "The ending that marks <em>books</em> marks <em>he "
                "walks</em>, and students carry it over: <em>they walks</em>, "
                "<em>the children plays</em>. A verb with an <em>-s</em> has "
                "one thing doing it. In the chapter no pair with "
                "<em>you</em>, <em>we</em> or <em>they</em> takes a "
                "third person form.",
            ),
            (
                "Using have, do and was with he, she and it",
                "<em>He have</em>, <em>she do not</em>, <em>it were</em>. "
                "The helping verbs change word, not ending, so the "
                "<em>-s</em> habit does not reach them. The chapter has "
                "<em>she was</em>, <em>he has</em>, <em>it does</em>; the "
                "lab marks <em>if I were</em> as the only row that goes the "
                "other way.",
            ),
            (
                "Reading the one broken row as a hole in the rule",
                "<em>If I were</em> is a form kept for a case that is not "
                "real. Counting it against the rule is honest; calling the "
                "rule weak because of it is not. One pair in 75, and a "
                "reason you can state, is the shape of a good rule with a "
                "named exception.",
            ),
        ),
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "Which sentence follows the agreement rule?",
                "a": [
                    "<em>She have finished.</em>",
                    "<em>They was late.</em>",
                    "<em>It does not matter.</em>",
                    "<em>He do not know.</em>",
                ],
                "c": 2,
                "why": (
                    "<em>It</em> takes <em>does</em>. <em>Have</em>, "
                    "<em>was</em> and <em>do</em> belong with the subjects for more than one "
                    "subjects, and <em>was</em> goes with <em>I</em>, "
                    "<em>he</em>, <em>she</em> and <em>it</em>, not with "
                    "<em>they</em>."
                ),
            },
            {
                "q": "What does an -s on a verb tell you about its subject?",
                "a": [
                    "It is more than one thing.",
                    "It is exactly one thing, and not you or me.",
                    "It is in the past.",
                    "It is a question.",
                ],
                "c": 1,
                "why": (
                    "On a verb the <em>-s</em> goes with <em>he</em>, "
                    "<em>she</em> and <em>it</em>. It is the reverse of the "
                    "<em>-s</em> on a noun."
                ),
            },
            {
                "q": "Which row is the one pair in the chapter that goes "
                     "against the rule?",
                "a": [
                    "<em>she was</em>",
                    "<em>you are</em>",
                    "<em>I am</em>",
                    "<em>if I were not afraid</em>",
                ],
                "c": 3,
                "why": (
                    "<em>I</em> takes <em>am</em> or <em>was</em>. "
                    "<em>If I were</em> is the old form for a case that is "
                    "not real, and the lab counts it against the rule."
                ),
            },
            {
                "q": "The lab scores 75 pairs out of 216 pronoun subjects. Why are "
                     "the rest left out?",
                "a": [
                    "The word after them is a past form, a modal or not a "
                    "verb at all, so there is nothing to check.",
                    "They are in the second half of the chapter.",
                    "The scan stopped after 75 pairs.",
                    "They are all questions.",
                ],
                "c": 0,
                "why": (
                    "Rows such as <em>she thought</em>, <em>they went</em> and "
                    "<em>I would</em> carry no sign of the subject, and in "
                    "<em>to use it your father</em> the <em>it</em> is not a "
                    "subject at all."
                ),
            },
        ],
        "body": [
            ("p",
             "Here is a habit from nouns that does damage on verbs. An "
             "<em>-s</em> on a noun means more than one: <em>book</em>, "
             "<em>books</em>. So when students see an <em>-s</em> on a verb "
             "they read it as more than one too, and write <em>they walks</em>."),
            ("p",
             "It means the reverse. In <em>she walks</em> one person walks. "
             "The rule for the present <dfn>tense</dfn> is short enough to "
             "say in one breath: the third person, which is <em>he</em>, "
             "<em>she</em>, <em>it</em> and any one thing named in their "
             "place, takes the form with <em>-s</em>. Everyone else takes "
             "the <dfn>bare</dfn> form, the verb with nothing added."),
            ("h3", "Three verbs that do it with a different word"),
            ("p",
             "<em>Be</em>, <em>have</em> and <em>do</em> are the three "
             "most used helping verbs, and they follow the same rule with "
             "different words. <em>Be</em> gives <em>is</em> for "
             "<em>he</em>, <em>she</em> and <em>it</em>, <em>are</em> for "
             "<em>you</em>, <em>we</em> and <em>they</em>, and <em>am</em> "
             "for <em>I</em>. <em>Have</em> gives <em>has</em> and "
             "<em>have</em>. <em>Do</em> gives <em>does</em> and "
             "<em>do</em>. In the past, <em>be</em> splits again: "
             "<em>was</em> for <em>I</em>, <em>he</em>, <em>she</em> and "
             "<em>it</em>, <em>were</em> for the rest."),
            ("h3", "Counting it"),
            ("p",
             "The lab runs the rule on one chapter of <em>Pride and "
             "Prejudice</em>, Chapter XXVI, which has 216 pronoun subjects. "
             "It reads the word after each one. If that word is a present "
             "form, <em>was</em>, <em>were</em> or a bare verb, the pair "
             "can be scored, and there are 75 of those. The rule holds in "
             "74, which is 98.7%."),
            ("p",
             "The other 141 pronoun subjects are followed by a word the rule cannot "
             "use: <em>she thought</em>, <em>they went</em>, <em>I "
             "would</em>, <em>he ought</em>. A past form and a modal look "
             "the same whatever the subject. So most of what an English "
             "sentence does with its verb is outside this rule, and the "
             "rule is only about the present tense and the two forms of "
             "<em>was</em>."),
            ("h3", "The row that breaks it"),
            ("p",
             "One pair goes against the rule, and it is not a mistake. In the "
             "chapter, Elizabeth writes <em>if I were not afraid of "
             "judging</em>. The <em>if</em> marks a case that is "
             "not real, and English keeps <em>were</em> for that, for every "
             "subject, including <em>I</em>. It is old, it is rare, and the "
             "lab names it and sets it aside."),
            ("p",
             "Because 75 pairs is a small count, the lesson also quotes the "
             "whole novel. These figures were counted once, away from the page, over "
             "all of it, and no page can carry them. After <em>he</em>, "
             "<em>she</em> and <em>it</em> there are 1,214 third person "
             "forms and 37 others. After <em>you</em>, <em>we</em> and "
             "<em>they</em> there are 487 forms for more than one and 5 third person "
             "ones. The chapter is a sample of a pattern, not an accident."),
            ("h3", "On a modern page"),
            ("p",
             "Choose the two modern documents in the lab. The Supreme Court "
             "opinion and the Census Bureau story give 14 pairs and the rule "
             "holds in all 14, as it does in a chapter two hundred years older."),
        ],
    },
    {
        "slug": "after-a-modal-the-verb-is-bare",
        "module": "One verb, one helping verb",
        "title": "After a Modal, the Verb Is Bare",
        "one_line": "Nine words take the tense, and the verb after them takes nothing.",
        "standard": (
            "Finish when you can name the nine modals and say what form of "
            "the verb comes after one.",
            "You should be able to list the nine, say why a modal never takes "
            "-s or -ed, allow not or an adverb between a modal and its verb, "
            "and read off a printed chapter what actually follows a modal, "
            "row by row.",
        ),
        "summary": (
            "There are nine modals. Each one is followed by a verb with no "
            "ending: <em>she can go</em>, never <em>she can goes</em>. On "
            "the 76 modals in one chapter of a novel, a bare verb follows "
            "65 times, and nothing with an ending follows at all. The other "
            "eleven rows are worth reading, because none of them breaks the "
            "rule."
        ),
        "key_label": "One chapter, 76 modals",
        "key": [
            "can  could  may  might  must",
            "shall  should  will  would",
            "",
            "modal + bare verb       can go",
            "modal + not + bare verb  could not go",
            "",
            "65 of 76, with 0 verbs with an ending",
        ],
        "concepts_intro": "Three ideas, and the second one is the whole lesson.",
        "concepts": (
            (
                "A modal is a helping verb with no forms of its own",
                "Nine words are <dfn>modals</dfn>. Each is a <dfn>modal</dfn>: <em>can</em>, "
                "<em>could</em>, <em>may</em>, <em>might</em>, "
                "<em>must</em>, <em>shall</em>, <em>should</em>, "
                "<em>will</em> and <em>would</em>. They add a meaning &mdash; "
                "ability, chance, need, a plan &mdash; to the verb that "
                "follows. They never take <em>-s</em>, <em>-ed</em> or "
                "<em>-ing</em>, and they have no <em>to</em> after them.",
            ),
            (
                "The modal takes the tense, the verb takes nothing",
                "A sentence needs one word that shows the <dfn>tense</dfn>, "
                "the time. In <em>she could go</em> that word is "
                "<em>could</em>, so <em>go</em> is left <dfn>bare</dfn>, "
                "with no ending. An <em>-s</em> or an "
                "<em>-ed</em> on <em>go</em> would show the tense a second "
                "time. <em>She can goes</em> and <em>he must went</em> do "
                "just that.",
            ),
            (
                "Small words can come between",
                "<em>Not</em> and short <dfn>adverb</dfn> words sit between a modal and its "
                "verb: <em>could not do</em>, <em>will certainly come</em>. "
                "The lab steps over them, and counts those rows apart. The "
                "verb after them is still bare.",
            ),
        ),
        "steps_title": "Checking a sentence with a modal",
        "steps_intro": "Four questions.",
        "steps": (
            (
                "Find the modal",
                "It is one of the nine. <em>Ought</em>, <em>need</em> and "
                "<em>dare</em> work much the same way, and the lab does not "
                "count them as modals.",
            ),
            (
                "Skip not and any short adverb",
                "<em>Should not</em>, <em>will certainly</em>: look past "
                "them for the next word.",
            ),
            (
                "Is the next word a bare verb?",
                "A bare verb is the base form, with no ending and no "
                "<em>to</em>: <em>go</em>, <em>be</em>, <em>have</em>, "
                "<em>see</em>. If it is, the rule holds.",
            ),
            (
                "Check the order if the next word is a pronoun",
                "<em>Can I promise</em>, <em>will you come</em>: a question "
                "turns the modal and the subject round. The bare verb comes "
                "after the subject.",
            ),
        ),
        "lab": ("english", {
            "mode": "auxchain",
            "rule": "modal",
            "panel_title": "Score the rule on every modal in the chapter",
            "panel_intro": (
                "The table prints a few words around every one of the nine "
                "modals in Chapter XXVI of <em>Pride and Prejudice</em>, and "
                "what comes next. The first boxes count the modals and the "
                "ones the rule holds for. A modal followed by <em>not</em> or "
                "an adverb and then a bare verb counts as holding, and is "
                "also counted apart. The box for a verb with an ending counts "
                "the rows that would break the rule. The box for a pronoun "
                "next counts the rows where the modal and its subject are "
                "turned round, as in a question, and the rows where the scan "
                "has run past a full stop. Everything else goes in "
                "<em>something else</em>; read it. The chapter was written in "
                "1813, and the modern documents are in the menu."
            ),
        }),
        "read_title": "The eleven rows that are not a bare verb",
        "read_intro": (
            "65 of 76 is 85.5%. The other eleven are sorted by the lab, and "
            "no one of them has a verb with an ending."
        ),
        "worked": {
            "title": "Reading the eleven",
            "intro": [
                "The lab sorts the eleven into two kinds: four rows with a "
                "pronoun right after the modal, and seven filed as something "
                "else. Reading them finds more kinds than two.",
            ],
            "lines": [
                "a question:   will you come        how can I promise",
                "past a stop:  he should not. I see    will, I am sure, be",
                "",
                "something else, seven rows:",
                "  I will endeavour       you will consent",
                "  you certainly shall    could not but be",
            ],
            "after": [
                "Two of the four rows with a pronoun next are the modal and "
                "its subject turned round, <em>will you come</em> and "
                "<em>how can I promise</em>. The bare verb follows the "
                "subject, so the rule still holds, but the scan reads one "
                "word and cannot see that. The other two are not questions. "
                "In <em>better that he should not. I see the imprudence</em> "
                "the modal ends its sentence, and the scan has read on past "
                "the full stop; in <em>Lizzy will, I am sure, be "
                "incapable</em> a remark sits between the modal and its "
                "bare verb, <em>be</em>. The seven rows in "
                "<em>something else</em> are four kinds of gap. For "
                "<em>endeavour</em> and <em>consent</em> the verb is bare, "
                "but the word list the scan uses does not hold it. In "
                "<em>could not but be</em> the bare verb is there, behind "
                "<em>but</em>. In <em>you certainly shall</em> the verb "
                "has been left out, because the sentence before it says "
                "it. And three rows put <em>no longer</em> or <em>at "
                "present</em> before the verb, words the scan does not "
                "step over. In none of the eleven does a verb with an "
                "ending follow a modal.",
            ],
        },
        "note": (
            "The score here, 85.5%, is a measure of the scan as much as of "
            "the rule. The rule held in every row that was not a gap in the "
            "word list or a gap in the sentence. The number that tests the "
            "rule is the box that counts a verb with an ending after a "
            "modal: none in the chapter. Counted once over the whole novel "
            "and quoted here, there are 2,738 modals, and a verb with an "
            "ending follows 3 of them, which is 0.1%."
        ),
        "mistakes": (
            (
                "Putting the tense on both words",
                "<em>She can goes</em>, <em>he must went</em>, <em>they "
                "will came</em>. A modal takes the tense, and the verb after "
                "it takes nothing. In the chapter, a verb with an ending "
                "follows a modal 0 times in 76.",
            ),
            (
                "Adding to after a modal",
                "<em>She must to go</em>. The nine modals take the bare "
                "verb straight away. The words that look like them and do "
                "take <em>to</em> &mdash; <em>ought to</em>, <em>have to</em> "
                "&mdash; are a separate group, and the lab does not score "
                "them here.",
            ),
            (
                "Reading the lab's 85.5% as a failure rate",
                "The eleven rows that are not a direct bare verb are two "
                "questions, two rows read past a full stop or a comma, gaps "
                "in the word list, and a verb left out. "
                "Read them. A low hit rate with no row that breaks the rule "
                "is a limit of the scan, and the lab says so in its note.",
            ),
        ),
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "Which sentence has the verb in the right form?",
                "a": [
                    "<em>She can goes home.</em>",
                    "<em>He could not do better.</em>",
                    "<em>They will came on Monday.</em>",
                    "<em>You must to see it.</em>",
                ],
                "c": 1,
                "why": (
                    "<em>Could</em> takes the tense, <em>not</em> sits between, "
                    "and <em>do</em> has no ending. The others add a second "
                    "tense or a <em>to</em>."
                ),
            },
            {
                "q": "Which word is NOT one of the nine modals?",
                "a": [
                    "<em>might</em>",
                    "<em>shall</em>",
                    "<em>do</em>",
                    "<em>should</em>",
                ],
                "c": 2,
                "why": (
                    "<em>Do</em> is a helping verb and has its own forms, "
                    "<em>does</em> and <em>did</em>. A modal has none."
                ),
            },
            {
                "q": "In the chapter, how many of the 76 modals are followed by "
                     "a verb with an ending?",
                "a": ["11", "4", "20", "0"],
                "c": 3,
                "why": (
                    "None. 65 are followed by a bare verb, and the other 11 "
                    "are two questions, two rows the scan read past a full "
                    "stop or a comma, and seven gaps, none of them a verb "
                    "with an ending."
                ),
            },
            {
                "q": "<em>Will you come?</em> puts a pronoun right after the "
                     "modal. What does that do to the rule?",
                "a": [
                    "Nothing: the bare verb follows the subject.",
                    "It breaks it, because the verb is not next.",
                    "It turns the modal into a main verb.",
                    "It makes the verb take -s.",
                ],
                "c": 0,
                "why": (
                    "A question turns the modal and the subject round. "
                    "<em>Come</em> is still bare. The scan files the row "
                    "apart because it reads one word."
                ),
            },
        ],
        "body": [
            ("p",
             "Take a verb, put <em>can</em> in front, and the verb loses "
             "its endings. <em>She walks</em>, but <em>she can walk</em>. "
             "<em>He went</em>, but <em>he could go</em>. The helping verb "
             "has taken the work, and the main verb is left bare."),
            ("p",
             "There are nine words that do this, and they are called "
             "modals: <em>can</em>, <em>could</em>, <em>may</em>, "
             "<em>might</em>, <em>must</em>, <em>shall</em>, <em>should</em>, "
             "<em>will</em> and <em>would</em>. They add a meaning to the "
             "verb after them &mdash; whether it can, may or must happen "
             "&mdash; and they have no forms of their own."),
            ("h3", "Why nothing else is needed"),
            ("p",
             "A clause shows its tense once. In <em>she could go</em>, the "
             "tense is in <em>could</em>. Add an ending to <em>go</em> and "
             "the tense is shown twice. That is the mistake in <em>she can "
             "goes</em>: the speaker has put the third person ending on a "
             "verb that follows a word which has already taken it."),
            ("h3", "Counting it"),
            ("p",
             "The lab finds every modal in Chapter XXVI and reads what "
             "follows. There are 76. A bare verb follows 65 times, which is "
             "85.5%. Of those 65, 20 have <em>not</em> or an adverb between "
             "the modal and the verb: <em>you could not do better</em>, "
             "<em>we shall often meet</em>. The bare form holds through "
             "the gap."),
            ("p",
             "The test of the rule is a row that would break it: a modal "
             "followed by a verb with <em>-s</em>, <em>-ed</em> or "
             "<em>-ing</em>. The lab has a box for that, and in the chapter "
             "it holds 0."),
            ("h3", "The eleven others"),
            ("p",
             "Four rows have a <dfn>pronoun</dfn> right after the modal. Two "
             "are questions, <em>will you come</em> and <em>how can I "
             "promise</em>: the bare verb comes after the subject, so the "
             "rule holds, but the scan reads one word and files it apart. "
             "Two are not. In <em>he should not. I see</em> the modal ends "
             "its sentence and the scan read on past the full stop; in "
             "<em>will, I am sure, be</em> a remark stands between the modal "
             "and its verb. Seven rows are filed as "
             "<em>something else</em>. Look at them: two have a bare verb "
             "the word list does not know, one has a bare verb behind "
             "<em>but</em>, one has the verb left out, and three put "
             "<em>no longer</em> or <em>at present</em> in the way. None "
             "of them has an ending on the verb."),
            ("h3", "What a whole novel says"),
            ("p",
             "Counted once over the whole novel, which no page can carry, "
             "and quoted here, there are 2,738 modals. A bare verb comes "
             "directly after 58.5% of them. <em>Not</em> comes between in "
             "14.9%, and an adverb in 9.5%. A pronoun comes next, a "
             "question, in 5.2%. A verb with an ending follows 3 of the "
             "2,738, which is 0.1%, and the three are worth naming: <em>as "
             "soon as he could, provided he chose</em>; <em>as well as she "
             "could, said that</em>; <em>as soon as we can, said Jane</em>. "
             "In each the modal ends its clause, and the verb after the "
             "comma belongs to the next one. The rule has no true exception "
             "in 2,738 rows, and that is a rule worth stating simply."),
            ("p",
             "The two modern documents give 16 of 17 rows, 94.1%, and "
             "again no verb with an ending. The one row that is not a hit is "
             "the month <em>May</em> in <em>changes in May</em>, which the scan "
             "reads as the word <em>may</em>."),
        ],
    },
    {
        "slug": "have-is-two-words",
        "module": "Two words each",
        "title": "Have Is Two Words",
        "one_line": "Sometimes it helps another verb, and sometimes it is the verb.",
        "standard": (
            "Finish when you can tell whether a given have is helping "
            "another verb or is the verb itself.",
            "You should be able to say what comes after have in each case, "
            "sort a list of rows into the helping verb, the main verb and have to, "
            "and read the three shares off a printed chapter.",
        ),
        "summary": (
            "<em>Have</em> is two words that look the same. In <em>she has "
            "seen</em> it helps the verb after it. In <em>she has a "
            "sister</em> it is the verb. The test is the word that comes "
            "next. The scan files 17 of the chapter's 37 forms of "
            "<em>have</em> as helping verbs and 10 as main verbs, and ten it "
            "reads as questions or cannot place; read by hand, 24 of the 37 "
            "are helping verbs, and the rows show where the scan went "
            "wrong."
        ),
        "key_label": "One chapter, 37 forms of have",
        "key": [
            "have + participle       had been, has seen",
            "have + noun phrase      had the fortune",
            "have to + verb          has to go",
            "",
            "the scan: 17 of 37 helping verb, 10 main",
            "read by hand: 24 of 37 helping verb",
        ],
        "concepts_intro": "Three ideas. The first is the whole lesson in a line.",
        "concepts": (
            (
                "What follows tells you which have it is",
                "A <dfn>participle</dfn> after it makes it a helping verb: "
                "<em>had been</em>, <em>has written</em>, <em>have "
                "met</em>. A noun phrase after it &mdash; a word such as "
                "<em>a</em>, <em>the</em>, <em>no</em>, <em>much</em> &mdash; "
                "makes it the main verb, and it means own or hold or "
                "experience: <em>had the fortune</em>, <em>had no "
                "pleasure</em>.",
            ),
            (
                "Have to is a third thing",
                "<em>Have to</em> followed by a verb says that something is "
                "needed: <em>I have to go</em>. It is not the helping verb "
                "and not quite the main verb. The lab counts it apart, "
                "and the chapter has none.",
            ),
            (
                "A one-word scan can give a wrong idea",
                "The scan files 17 of the chapter's 37 forms as helping "
                "verbs, 45.9%. Read the rows and 24 are: three have a "
                "participle the word list lacks, and four have a word or a "
                "phrase between <em>have</em> and its participle, <em>had by "
                "some accident been lost</em>. Counted by the same scan over "
                "the whole novel, 59.5% are helping verbs. This lesson reads "
                "the 37 and quotes the 2,339.",
            ),
        ),
        "steps_title": "Sorting a have in front of you",
        "steps_intro": "Look one word to the right, then two.",
        "steps": (
            (
                "Skip not and short adverb words",
                "<em>Had not</em>, <em>has already</em>: look past them to "
                "the next word. A subject can move in front too, <em>had I "
                "known</em>, <em>had fortune permitted</em>; look past that "
                "as well.",
            ),
            (
                "Is the next word a participle?",
                "<em>Been</em>, <em>seen</em>, <em>written</em>, "
                "<em>met</em>. Then <em>have</em> is a helping verb.",
            ),
            (
                "Is the next word a, the, no, my, some, or a noun?",
                "Then <em>have</em> is the main verb, and it is about "
                "having something.",
            ),
            (
                "Is the next word to?",
                "Then it is <em>have to</em>. Read the verb after it, and "
                "ask whether the sentence is about need.",
            ),
        ),
        "lab": ("english", {
            "mode": "auxchain",
            "rule": "have",
            "panel_title": "Sort every have in the chapter",
            "panel_intro": (
                "The table prints a few words around every form of "
                "<em>have</em> in Chapter XXVI of <em>Pride and "
                "Prejudice</em>, with the sort it was given. The first box "
                "counts the forms. The next boxes count those followed by a "
                "participle, by a noun phrase and by <em>to</em>; "
                "<em>having</em> counts as a form. A word such as <em>he</em> next would be a "
                "question. The scan reads the word list's participle forms and "
                "nouns and no more, so some rows are filed as <em>something "
                "else</em>; read them. The chapter is 1813 prose, and the "
                "two modern documents are in the menu."
            ),
        }),
        "read_title": "The seven the scan filed wrong",
        "read_intro": (
            "Five rows filed as something else, one filed as a question "
            "and one filed as the main verb are helping verbs: seven in "
            "all."
        ),
        "worked": {
            "title": "Helping verb against main verb, row by row",
            "intro": [
                "These rows are from the chapter. The first column is "
                "what the lab files them as.",
            ],
            "lines": [
                "helping verb  had been quitted       has been so",
                "helping verb  had already written    she had seen",
                "main verb     you have sense         he had the fortune",
                "main verb     she had no pleasure    I have nothing to",
                "unknown word  might have foreseen    has proved you right",
                "word between  had I really experienced  had at all cared",
            ],
            "after": [
                "In the first two rows a participle follows, so the helping verb is "
                "doing a job for another verb. In the next two the word "
                "after <em>have</em> begins a noun phrase and <em>have</em> "
                "is the verb itself. The fifth row is the three the lab files "
                "as <em>something else</em>: <em>foreseen</em>, "
                "<em>proved</em> and <em>subsided</em> are participle forms, but "
                "the word list the scan uses does not hold them as that. "
                "The last row is two of the other four. In <em>had I really "
                "experienced</em> and <em>had fortune permitted</em> the "
                "subject has moved in between; the lab files the first as a "
                "question, because a pronoun follows <em>had</em>, and the "
                "second as the main verb. In <em>if he had at all "
                "cared</em> and <em>had by some accident been lost</em> a "
                "phrase has, and the lab files both as something else. All "
                "seven are helping verbs, so read by hand the split is 24 helping verbs against "
                "13 others, and the page keeps the lab's own count so you can "
                "see what the scan did.",
            ],
        },
        "note": (
            "Two of the 13 rows that are not helping verbs are not about "
            "owning anything either. <em>We had better not mention it</em> "
            "has <em>had better</em>, a fixed phrase the scan cannot place, "
            "so it is filed as something else. <em>I would have you be on "
            "your guard</em> has <em>have</em> with a person and a bare verb "
            "after it, which means make or let; the scan sees a pronoun "
            "after <em>have</em> and files it as a question. The label says "
            "what the scan read. It does not say what the writer meant."
        ),
        "mistakes": (
            (
                "Have always means to own",
                "In this chapter the scan files 17 of 37 forms of <em>have</em> "
                "as helping verbs with a participle after them, and seven "
                "more are helping verbs it put in the wrong group: 24 of 37, "
                "against 11 that mean own or hold. "
                "Counted once over the whole novel and quoted here, there are "
                "2,339 forms: 59.5% are helping verbs, 32.1% are the main verb "
                "and 1.1% are <em>have to</em>.",
            ),
            (
                "Reading the scan's count as the answer",
                "The page says 45.9% helping verbs for the chapter and the "
                "novel says 59.5%. The gap is not the chapter: by hand it "
                "gives 24 of 37, 64.9%. It is the scan, which reads one word "
                "and misses a participle the list lacks or a subject that has "
                "moved in between. The novel's figure comes from the same "
                "scan, so rows of the same kind sit inside its 32.1% and its "
                "6.8% filed as something else.",
            ),
            (
                "Taking a fixed phrase for its parts",
                "<em>Had better</em> and <em>have to</em> each work as "
                "one unit. The scan reads one word at a time, so "
                "<em>had better</em> is filed as something else. "
                "Know the phrases, and read the row.",
            ),
        ),
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "In which sentence is <em>have</em> the main verb?",
                "a": [
                    "<em>They have seen it.</em>",
                    "<em>She has been ill.</em>",
                    "<em>I have a sister.</em>",
                    "<em>We have finished.</em>",
                ],
                "c": 2,
                "why": (
                    "<em>A sister</em> is a noun phrase, so <em>have</em> is "
                    "the verb. In the others a participle follows, and "
                    "<em>have</em> is the helping verb."
                ),
            },
            {
                "q": "What does the word after <em>had</em> tell you in "
                     "<em>she had already written</em>?",
                "a": [
                    "<em>Had</em> is the helping verb, because a participle follows "
                    "the adverb.",
                    "<em>Had</em> is the main verb, because <em>already</em> "
                    "follows.",
                    "<em>Had</em> is one of the nine words such as <em>can</em>.",
                    "<em>Had</em> means to own.",
                ],
                "c": 0,
                "why": (
                    "The scan steps over <em>already</em> and finds "
                    "<em>written</em>, a participle."
                ),
            },
            {
                "q": "The scan files 17 of the chapter's 37 forms of "
                     "<em>have</em> as helping verbs, 45.9%. Read by hand "
                     "there are 24. Where does the gap come from?",
                "a": [
                    "The chapter is a small sample.",
                    "Seven rows where a participle the list lacks, or a word "
                    "between <em>have</em> and its participle, hid the "
                    "helping verb from the scan.",
                    "The novel was counted by a different rule.",
                    "1813 English used <em>have</em> less as a helping verb.",
                ],
                "c": 1,
                "why": (
                    "Three participles the word list lacks and four rows with "
                    "a subject or a phrase between <em>have</em> and its "
                    "participle. The sample is small, but this gap is the "
                    "scan's, and the rows show it."
                ),
            },
        ],
        "body": [
            ("p",
             "<em>She has seen the letter.</em> <em>She has a letter.</em> "
             "The same word, the same spelling, and two different jobs. In "
             "the first, <em>has</em> is a helping verb: it "
             "stands in front of <em>seen</em> and carries the <dfn>tense</dfn>. In the "
             "second it is the verb, and it means that she holds the "
             "letter."),
            ("p",
             "The word after it decides which. If a <dfn>participle</dfn> "
             "follows &mdash; <em>seen</em>, <em>been</em>, "
             "<em>written</em> &mdash; <em>have</em> is a helping verb. If a "
             "noun phrase follows &mdash; <em>a letter</em>, <em>no "
             "pleasure</em>, <em>much to say</em> &mdash; it is the main "
             "verb."),
            ("h3", "The lab sorts all 37"),
            ("p",
             "Chapter XXVI has 37 forms of <em>have</em>: <em>have</em>, "
             "<em>has</em>, <em>had</em> and <em>having</em>. The lab "
             "steps over <em>not</em> and short <dfn>adverb</dfn> words and reads the next "
             "word. It finds 17 helping verbs, which is 45.9%, and 10 main "
             "verbs. Zero are <em>have to</em>. Three are filed as questions, "
             "because a pronoun follows <em>have</em>, and seven as something "
             "else."),
            ("h3", "The seven the scan missed"),
            ("p",
             "Look at the three: <em>she might have foreseen</em>, "
             "<em>the event has proved you right</em>, <em>apparent "
             "partiality had subsided</em>. Each has a participle after "
             "the helping verb. The scan's word list does not have "
             "<em>foreseen</em>, <em>proved</em> or <em>subsided</em> as "
             "participle forms, so it could not place them. Now read the other "
             "rows. Four more are helping verbs too. <em>Had by some accident "
             "been lost</em> and <em>if he had at all cared</em> have a "
             "phrase between <em>have</em> and its participle, and the scan "
             "files them as something else. <em>Had fortune permitted "
             "it</em> and <em>for had I really experienced</em> are the old "
             "way of saying <em>if</em>, with the subject moved in behind "
             "<em>had</em>; the scan files the first as the main verb and the "
             "second as a question. Add the seven "
             "and the split is 24 helping verbs against 13 others, 64.9%. The "
             "number the page prints is the scan's, and the rows tell you the "
             "rest."),
            ("h3", "A small count and a large one"),
            ("p",
             "37 forms is a small count. Counted once over the whole novel "
             "and quoted here, <em>have</em> appears 2,339 times, and 59.5% "
             "of them are helping verbs, 32.1% main verbs and 1.1% "
             "<em>have to</em>. The page's lower share for the chapter is the "
             "scan's reading, not the chapter's: by hand the chapter gives "
             "64.9%, and the novel's count comes from the same one-word scan, "
             "with 6.8% filed as something else. In the play <em>The "
             "Importance of Being Earnest</em>, quoted the same way, the split "
             "is 50.1% helping verbs, 42.0% main verbs and 2.9% <em>have "
             "to</em>. In the two modern documents the lab counts 16 helping "
             "verbs in 23 forms, 69.6%, 3 main verbs, one <em>have to</em>, "
             "<em>had to do</em>, and three filed as something else, <em>had "
             "violated</em>, <em>has diminished</em>, <em>has morphed</em>, "
             "all helping verbs with a participle the list lacks."),
            ("h3", "Two phrases the scan reads as their parts"),
            ("p",
             "<em>We had better not mention it.</em> The scan reads "
             "<em>better</em> as no word it knows, so it files <em>had</em> as "
             "something else. The phrase <em>had better</em> is one unit, and it "
             "gives advice. <em>I would have you be on your guard</em> is a "
             "third use of the word: <em>have</em> with a person and a bare "
             "verb after it means make or let, and the scan, which sees a "
             "pronoun after <em>have</em>, files it as a question. Rows like "
             "these are in the lab's counts, and they are the reason to read "
             "the rows."),
        ],
    },
]
