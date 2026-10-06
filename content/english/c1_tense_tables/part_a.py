# -*- coding: utf-8 -*-
"""Lesson one of the tense course.

The prose here is written inside the NGSL 2,809, because the Subject tells its
reader that 98% coverage is what reading needs and a page that teaches that at
90% has failed its own lesson. `scripts/bandcheck.py` is the check; this file is
the first thing it was ever pointed at, and it measures 98.8% with no glossary.
"""

LESSONS = [
    {
        "slug": "five-forms-and-the-whole-table",
        "module": "A table you can build beats a table you remember",
        "title": "Five Forms Make Twelve",
        "one_line": "Learn five forms of a verb and the twelve boxes fill themselves.",
        "standard": (
            "Finish when you can build the full table for a verb you have never "
            "seen, and name the rule that made each form.",
            "You should be able to take any regular verb, write its five forms "
            "by rule, say which of the four rules fired and why, fill all twelve "
            "boxes by placing <em>have</em>, <em>be</em> and <em>will</em> in "
            "front of them, and name the short list of words each rule misses.",
        ),
        "summary": (
            "A tense table has twelve boxes. Books print them and ask you to learn "
            "them. You do not have to. Every box is built from five forms of the "
            "verb, and four of those five follow rules you can state in one line "
            "each. This lesson gives you the rules, counts how often they are "
            "right on 1,356 real verbs, and shows you every word they get wrong."
        ),
        "key_label": "The five forms, and what fills the table",
        "key": [
            "base            walk",
            "he/she/it       walks",
            "-ing form       walking",
            "past            walked",
            "after have      walked",
            "",
            "the other nine boxes are these five",
            "with have, be and will in front",
        ],
        "concepts_intro": "Three ideas carry the whole lesson.",
        "concepts": [
            (
                "Twelve boxes, but not twelve things to learn",
                "The table has three times across the top and four shapes down the "
                "side. That makes twelve boxes. But you never learn twelve forms of "
                "a verb, because nine of the boxes are the same few forms with "
                "<em>have</em>, <em>be</em> or <em>will</em> placed in front of "
                "them. Learn five forms and you can write any box.",
            ),
            (
                "Four of the five follow a rule",
                "Only the base form has to be learned. The other four are made from "
                "it: add <em>-s</em>, add <em>-ing</em>, add <em>-ed</em>. What "
                "makes English feel hard is that each rule has a small change for "
                "certain endings, and those changes are what this lesson states "
                "exactly.",
            ),
            (
                "A rule is only as good as the count beside it",
                "Anyone can give you a rule. The question no book answers is how "
                "often it is right. Here the rules are run over 1,356 verbs and the "
                "share they get right is printed next to them, with every word they "
                "miss listed. A rule you can trust 99 times in 100 is worth more "
                "than a page of advice.",
            ),
        ],
        "steps_title": "Building a box",
        "steps_intro": "To write any box of the table, do this.",
        "steps": [
            (
                "Start from the base form",
                "The form you would find in a word list. This is the one form you "
                "have to learn; the rest are made from it.",
            ),
            (
                "Make the other four forms",
                "Add <em>-s</em>, <em>-ing</em> and <em>-ed</em> by the rules "
                "below, or look the verb up if it is one of the few that break "
                "them. The lab names the rule it used beside each form.",
            ),
            (
                "Choose the time you mean",
                "Now, before, or later. This picks the row of the table.",
            ),
            (
                "Put the small word in front",
                "<em>Have</em> to look back, <em>be</em> with the <em>-ing</em> "
                "form for something still going on, <em>will</em> to move it later. "
                "This picks the column, and the box is written.",
            ),
        ],
        "lab": ("tense", {
            "mode": "table",
            "panel_title": "Type any verb and watch the table fill",
            "panel_intro": (
                "Nothing here is looked up except the six verbs marked as broken "
                "ones. The three forms at the top are made by the rules this "
                "lesson states, and the box beside them names the rule that "
                "fired, so you can check the answer against the reason for it. "
                "Type a verb that is not in the list and the same rules run."
            ),
        }),
        "read_title": "What the rules got wrong",
        "read_intro": (
            "The rules were run over every regular verb in a list of the 2,800 "
            "most common words, and checked against the forms that list itself "
            "records. Here is how they did, and what they missed."
        ),
        "worked": {
            "title": "Three rules, 1,356 verbs, and the words that beat them",
            "intro": [
                "The lab runs these same rules on the page. The counts below are "
                "what they scored against the word list printed with this lesson.",
            ],
            "lines": [
                "-s      1354 of 1356 right     99.85%",
                "        missed: shelf, stomach",
                "",
                "-ing    1342 of 1356 right     98.97%",
                "        missed: busing, counselling,",
                "                formatting, inputting",
                "",
                "-ed     1338 of 1356 right     98.67%",
                "        missed: bred, bused, counselled",
            ],
            "after": [
                "The misses are not random. Several are words written one way in "
                "British English and another way in American English, and both are "
                "right. The rules cannot choose for you, and saying so is more use "
                "than pretending there is one answer.",
            ],
        },
        "note": (
            "The three lists of missed words are short enough to learn directly. "
            "That is the whole saving: a rule plus a short list beats a long list."
        ),
        "mistakes": [
            (
                "Learning the table instead of the rules",
                "Twelve boxes for every verb is a very large number of things to "
                "hold. Five forms and four rules is a small one, and it works on a "
                "verb you have never met.",
            ),
            (
                "Doubling the last letter when the stress is early",
                "<em>Stop</em> becomes <em>stopping</em>, but <em>listen</em> does "
                "not become <em>listenning</em>. The letter only doubles when the "
                "last part of the word is the strong part, which is why the rule "
                "needs the sound and not only the letters.",
            ),
            (
                "Believing a rule because it sounds right",
                "A rule turning <em>-f</em> into <em>-ves</em> looks correct, and "
                "for nouns it often is. Added here it made the results worse, "
                "because <em>brief</em>, <em>golf</em>, <em>proof</em> and "
                "<em>roof</em> are all verbs that simply add <em>-s</em>. The count "
                "caught it; the ear did not.",
            ),
        ],
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "How many forms of a verb do you need to write any of the twelve boxes?",
                "a": ["Five", "Twelve", "Three", "One for each box"],
                "c": 0,
                "why": (
                    "Five. The other boxes are those forms with <em>have</em>, "
                    "<em>be</em> or <em>will</em> placed in front."
                ),
            },
            {
                "q": "Why does <em>stop</em> double its last letter but <em>listen</em> not?",
                "a": [
                    "The strong part of <em>stop</em> is at the end",
                    "<em>listen</em> is irregular",
                    "<em>stop</em> is shorter",
                    "Only verbs with one part ever double",
                ],
                "c": 0,
                "why": (
                    "The letter doubles when the word ends consonant, vowel, "
                    "consonant <em>and</em> the last part carries the stress. In "
                    "<em>listen</em> the stress is on the first part."
                ),
            },
            {
                "q": "The past rule is right about 98.7% of the time. What does the rest tell you?",
                "a": [
                    "Which words to learn one by one",
                    "That the rule is wrong",
                    "That English has no rules",
                    "Nothing useful",
                ],
                "c": 0,
                "why": (
                    "The words a rule misses are a short list you can learn "
                    "directly. That is far less work than treating every verb as a "
                    "special case."
                ),
            },
        ],
        "body": [
            ("p",
             "Open any book for learners and you will find a page with twelve boxes "
             "on it. Three times across the top: now, before, later. Four shapes "
             "down the side. Every box has a name, and the book asks you to learn "
             "the names and the forms that go in them."),
            ("p",
             "You do not have to do that, and this lesson is about why."),
            ("h3", "The five forms"),
            ("p",
             "Every verb in English has five forms, and only five. For "
             "<em>walk</em> they are <em>walk</em>, <em>walks</em>, "
             "<em>walking</em>, <em>walked</em>, and the form used after "
             "<em>have</em>, which for this verb is also <em>walked</em>."),
            ("p",
             "Those five fill all twelve boxes. Nine of the boxes are simply one of "
             "these forms with a small word in front of it. <em>Have</em> gives you "
             "the shape that looks back from now. <em>Be</em> with the "
             "<em>-ing</em> form gives you the shape that is still going on. "
             "<em>Will</em> moves the whole thing later. That is the entire table."),
            ("h3", "The rules that make four of the five"),
            ("p",
             "You learn the base form when you learn the word. The other four come "
             "from rules, and here they are."),
            ("ul", [
                "For <em>he</em>, <em>she</em> or <em>it</em>, add <em>-s</em>. "
                "After a hissing sound, add <em>-es</em>. After a consonant and "
                "<em>-y</em>, the <em>-y</em> becomes <em>-ies</em>.",
                "For the <em>-ing</em> form, add <em>-ing</em>, dropping a silent "
                "<em>-e</em> first.",
                "For the past, add <em>-ed</em>, with the same <em>-y</em> change.",
                "If the word ends consonant, vowel, consonant and the last part is "
                "the strong part, double that last letter before any of the above.",
            ]),
            ("p",
             "That last rule is the only one needing the sound of the word and not "
             "only its letters. <em>Stop</em> is one part, so the last part is the "
             "strong part, and it doubles: <em>stopping</em>. <em>Listen</em> has "
             "two parts and the strong one is the first, so nothing doubles: "
             "<em>listening</em>."),
            ("h3", "How often the rules are right"),
            ("p",
             "A rule with no number beside it is only an opinion. So the rules "
             "above were run over the 1,356 regular verbs in a list of the 2,800 "
             "most common English words, and their answers were checked against "
             "the forms that list already records."),
            ("p",
             "They were right 99.85% of the time for <em>-s</em>, 98.97% for "
             "<em>-ing</em>, and 98.67% for the past. The words they missed are "
             "shown above, and there are not many. Several are words where British "
             "and American writers simply spell the same verb differently, so no "
             "rule could pick one."),
            ("h3", "A rule that sounded right and was not"),
            ("p",
             "When the <em>-s</em> rule first ran it missed <em>radio</em> and "
             "<em>video</em>, turning them into forms nobody writes. The fix was "
             "easy: <em>-o</em> takes <em>-es</em> only after a consonant, as in "
             "<em>potatoes</em>, and plain <em>-s</em> after a vowel."),
            ("p",
             "At the same time a second rule was added, because it also looked "
             "right: <em>-f</em> becomes <em>-ves</em>. For nouns that is often "
             "true. Added here it made the whole thing worse, not better, because "
             "<em>brief</em>, <em>golf</em>, <em>proof</em> and <em>roof</em> are "
             "verbs and they simply take <em>-s</em>."),
            ("p",
             "This is worth more than any single rule in the lesson. A rule can "
             "sound right, come from a real pattern, and still cost you accuracy. "
             "The only way to know is to run it over real words and count. That is "
             "what every lesson on this path does."),
        ],
    },
]
