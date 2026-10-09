# -*- coding: utf-8 -*-
"""Lesson one of the tense course.

The prose here is written inside the NGSL 2,809, because the Subject tells its
reader that 98% coverage is what reading needs and a page that teaches that at
90% has failed its own lesson. `scripts/bandcheck.py` is the check; this file is
the first thing it was ever pointed at. One glossary term, `dictionary`, is
defined where the list-cleaning is explained.

Every figure in this file is one the page computes: the hit rates and the
missed words are read off the `Score a rule on the list` menu of the table lab
with `labcheck.js --observe`, and the quiz and body quote nothing else.
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
            "right on 1,210 real verbs, and shows you every word they get wrong."
        ),
        "key_label": "The five forms, and what fills the table",
        "key": [
            "base            walk",
            "he, she, it     walks",
            "-ing form       walking",
            "past            walked",
            "after have      walked",
            "",
            "two boxes are a form on its own",
            "ten are a form with have, be or will in front",
        ],
        "concepts_intro": "Three ideas carry the whole lesson.",
        "concepts": [
            (
                "Twelve boxes, but not twelve things to learn",
                "The table has three times down the side and four shapes across "
                "the top. That makes twelve boxes. But you never learn twelve forms "
                "of a verb, because ten of the boxes are the same few forms with "
                "<em>have</em>, <em>be</em> or <em>will</em> placed in front of "
                "them, and the other two are a form on its own. Learn five forms "
                "and you can write any box.",
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
                "often it is right. Here the rules are run, in your browser, over "
                "1,210 verbs, and the share they get right is printed next to them "
                "with every word they miss. A rule you can trust 99 times in 100 is "
                "worth more than a page of advice.",
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
        "lab": ("english", {
            "mode": "table",
            "panel_title": "Type any verb and watch the table fill",
            "panel_intro": (
                "Nothing here is looked up except the six verbs marked as broken "
                "ones. The three forms at the top are made by the rules this "
                "lesson states, and the box beside them names the rule that "
                "fired, so you can check the answer against the reason for it. "
                "Type a verb that is not in the list and the same rules run, with "
                "one gap: the page cannot hear a word it does not carry, so for a "
                "new verb it treats the last part as the strong part. Then choose "
                "a rule under <em>Score a rule on the list</em> to run it over "
                "every verb printed below and read the words it misses."
            ),
        }),
        "read_title": "What the rules got wrong",
        "read_intro": (
            "The rules are run over every regular verb in a list of the 2,800 "
            "most common words, and checked against the forms that list itself "
            "records. The list had to be cleaned first, and the lab prints what "
            "was left out and why. Here is how the rules did, and what they "
            "missed."
        ),
        "worked": {
            "title": "Three rules, 1,210 verbs, and the words that beat them",
            "intro": [
                "The lab runs these same rules on the page. Choose a rule under "
                "<em>Score a rule on the list</em> and the count below appears, "
                "with every missed word in the table under it.",
            ],
            "lines": [
                "-s      1209 of 1210 right     99.92%",
                "        missed: stomach",
                "",
                "-ing    1202 of 1210 right     99.34%",
                "        missed: bus, format, initial, input,",
                "                output, panic, traffic, up",
                "",
                "-ed     1201 of 1210 right     99.26%",
                "        missed: bus, counsel, format, initial,",
                "                input, output, panic, traffic, up",
            ],
            "after": [
                "The misses are not random, and not all of them are mistakes. "
                "<em>Initial</em>, and <em>counsel</em> in the past, are written "
                "one way in British English and another in American English; the "
                "list records only the British <em>-ll-</em>, so the rule's "
                "American form is marked wrong where nothing is wrong. "
                "<em>Panic</em> and <em>traffic</em> take a <em>-k</em> before "
                "the ending, <em>panicking</em>, which no rule above knows. "
                "<em>Format</em>, <em>input</em> and <em>output</em> double their "
                "last letter though the strong part comes first. <em>Bus</em> is "
                "<em>busing</em> in the list where the rule writes "
                "<em>bussing</em>, and writers use both. <em>Stomach</em> ends in "
                "<em>-ch</em> but does not hiss, so <em>stomachs</em>: the rule "
                "reads letters and cannot hear. And <em>up</em> has no consonant "
                "before its vowel, so the rule never doubles it.",
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
                "a": ["Twelve", "Three", "Five", "Ten"],
                "c": 2,
                "why": (
                    "Five. The other boxes are those forms with <em>have</em>, "
                    "<em>be</em> or <em>will</em> placed in front. Ten is the "
                    "number of boxes that take a small word, not the number of "
                    "forms."
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
                    "<em>listen</em> the stress is on the first part. Verbs with "
                    "two parts double too when the second is strong: "
                    "<em>admit</em>, <em>admitting</em>."
                ),
            },
            {
                "q": "The past rule is right about 99.3% of the time. What does the rest tell you?",
                "a": [
                    "That the rule is wrong",
                    "That English has no rules",
                    "Nothing useful",
                    "Which words to learn one by one",
                ],
                "c": 3,
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
             "on it. Three times: now, before, later. Four shapes for each. "
             "Every box has a name, and the book asks you to learn the names and "
             "the forms that go in them."),
            ("p",
             "You do not have to do that, and this lesson is about why."),
            ("h3", "The five forms"),
            ("p",
             "A verb in English has five forms. For <em>walk</em> they are "
             "<em>walk</em>, <em>walks</em>, <em>walking</em>, <em>walked</em>, "
             "and the form used after <em>have</em>, which for this verb is also "
             "<em>walked</em>. One verb has more: <em>be</em> has eight "
             "(<em>am</em>, <em>is</em>, <em>are</em>, <em>was</em>, "
             "<em>were</em>, <em>be</em>, <em>being</em>, <em>been</em>), and "
             "the second course sets it apart from every other verb. The small "
             "helping words, <em>will</em> among them, have fewer, and they only "
             "ever stand in front."),
            ("p",
             "Those five fill all twelve boxes. Two of the boxes, <em>walk</em> "
             "and <em>walked</em>, are a form on its own. The other ten are simply "
             "one of these forms with a small word in front of it. <em>Have</em> gives you "
             "the shape that looks back from now. <em>Be</em> with the "
             "<em>-ing</em> form gives you the shape that is still going on. "
             "<em>Will</em> moves the whole thing later. That is the entire table."),
            ("h3", "The rules that make four of the five"),
            ("p",
             "You learn the base form when you learn the word. The other four come "
             "from rules, and here they are, exactly as the lab runs them."),
            ("ul", [
                "For <em>he</em>, <em>she</em> or <em>it</em>, add <em>-s</em>. "
                "After a hissing sound, add <em>-es</em>: <em>passes</em>, "
                "<em>wishes</em>, <em>watches</em>. After a consonant and "
                "<em>-y</em>, the <em>-y</em> becomes <em>-ies</em>: "
                "<em>carries</em>. After a consonant and <em>-o</em>, add "
                "<em>-es</em> as well: <em>goes</em>.",
                "For the <em>-ing</em> form, add <em>-ing</em>, dropping a silent "
                "<em>-e</em> first: <em>hope</em>, <em>hoping</em>.",
                "For the past, add <em>-ed</em>. After a silent <em>-e</em> only "
                "<em>-d</em> is needed, <em>hope</em>, <em>hoped</em>, and the "
                "<em>-y</em> change is the same: <em>carry</em>, <em>carried</em>.",
                "If the word ends consonant, vowel, consonant, the last letter is "
                "not <em>w</em>, <em>x</em> or <em>y</em>, and the last part is "
                "the strong part, double that last letter before <em>-ing</em> "
                "and <em>-ed</em>: <em>stop</em>, <em>stopping</em>, "
                "<em>stopped</em>. Nothing ever doubles before <em>-s</em>.",
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
             "above are run, on this page, over the 1,210 regular verbs in a list "
             "of the 2,800 most common English words, and their answers are "
             "checked against the forms that list already records."),
            ("p",
             "They are right 99.92% of the time for <em>-s</em>, 99.34% for "
             "<em>-ing</em>, and 99.26% for the past. The words they miss are "
             "listed in the lab and again in the worked example further down, and "
             "there are not many. Each is there for a reason you can name: a "
             "British spelling the list records and an American one it does not, "
             "a <em>-k</em> the rule does not know about, or a word that doubles "
             "when the strong part says it should not."),
            ("h3", "The list had to be cleaned first"),
            ("p",
             "The word list was made by a machine, and a machine can record a "
             "spelling nobody writes. The raw list had <em>offerring</em>, "
             "<em>commiting</em> and <em>councilling</em>; it gave verb forms to "
             "words that are not verbs, such as <em>able</em> and <em>son</em>; "
             "and it recorded <em>comed</em> and <em>maked</em>, so the past rule "
             "was being marked right for forms nobody writes. Scored against that "
             "list, a right rule looks wrong and a wrong rule looks right. So the "
             "list was cleaned by one test, applied to every spelling the same "
             "way: a spelling stays if a <dfn>dictionary</dfn>, a book that "
             "records the real spellings of a language, has it, or if it is the "
             "British spelling of one the dictionary has. The 90 verbs the second "
             "course calls irregular were taken out, because their past is not "
             "made by any rule. In all, 146 words were left out, each with its "
             "reason, and the lab prints them all under <em>List</em>."),
            ("h3", "A rule that sounded right and was not"),
            ("p",
             "When the <em>-s</em> rule first ran, every <em>-o</em> took "
             "<em>-es</em>, and it turned <em>radio</em> and <em>video</em> into "
             "forms nobody writes. Choose <em>the -s rule before the -o fix</em> "
             "in the lab and you can watch it: 1207 of 1210, 99.75%, with "
             "<em>radio</em> and <em>video</em> among the misses. The fix was "
             "easy: <em>-o</em> takes <em>-es</em> only after a consonant, as in "
             "<em>goes</em>, and plain <em>-s</em> after a vowel."),
            ("p",
             "At the same time a second rule was added, because it also looked "
             "right: <em>-f</em> becomes <em>-ves</em>. For nouns that is often "
             "true: one <em>leaf</em>, two <em>leaves</em>. Choose it in the lab "
             "and the count falls to 1205 of 1210, 99.59%, because "
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
