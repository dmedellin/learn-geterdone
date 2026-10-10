# -*- coding: utf-8 -*-
"""Course eight, lessons one and two: nouns and verbs of two parts, endings that pull the stress.

Every figure is read off the `stress` lab with `labcheck.js --observe`:
two-part nouns 207 of 231 (89.6%), verbs 134 of 150 (89.3%), adjectives 35 of 47
(74.5%), 49 words said both ways; -tion and -sion 151 of 152, -ic 28 of 28,
-ical 16 of 16, -ity 27 of 27, -ate 36 of 36, -ize 13 of 14, -ee 8 of 12.
Every word named in the prose is a word in the lab's own tables (rows or the
words set aside), except the well-known pair photograph and photography and the
pair able and ability, which the Misconception, the Worked example and the note
use as plain facts about English; fifty and examination, named beside the noun
misses fifteen and exam; and the verbs behind the ten nouns made from a verb
(advise ... succeed), which are plain facts about the words, not scores.
The dictionary facts behind the prose (perfect's first reading is the verb,
engineer carries two primary stresses, the four -ee misses carry IY0 on the
ending, television is EH1 first) were checked against cmudict.dict in
docs/english-v2/measure/data on 2026-10-10.

Spoken forms for the orchestrator are in content/spoken/english_c9_word_stress.py.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "nouns-at-the-front-verbs-at-the-back",
        "module": "Where the strong part falls",
        "title": "Nouns at the Front, Verbs at the Back",
        "one_line": "For a word of two parts, the word class picks the strong part, and the rule is right nine times in ten.",
        "standard": (
            "Finish when you can say which part of a word of two parts is strong "
            "from the word class alone, and name the words that break the rule.",
            "You should be able to put the strong part first for a noun "
            "of two parts and second for a verb of two parts, read both rules' scores off "
            "the table, sort the words each rule misses into kinds, and say "
            "<em>record</em> both ways.",
        ),
        "summary": (
            "In a word of two parts, one part is said stronger than the other. "
            "Which one is not luck. A noun of two parts is strong on the first "
            "part, and a verb of two parts is strong on the second. The table "
            "scores both rules: each is right for about nine words in ten. "
            "Forty-nine words are both, and are said both ways."
        ),
        "key_label": "Counted on the 2,800 words",
        "key": [
            "noun of two parts: first    207 of 231",
            "verb of two parts: second   134 of 150",
            "adjective of two parts: first 35 of 47",
            "",
            "money, action      decide, believe",
            "49 words are said both ways",
        ],
        "concepts_intro": "Three ideas. The third one explains the lists of misses.",
        "concepts": [
            (
                "One part of every word is the strong part",
                "Say <em>money</em> slowly. The first part is longer, louder "
                "and higher than the second. That is the strong part. Every "
                "word of two or more parts has one, and the other parts are "
                "weak. A dictionary marks it, so the page can check any rule "
                "about it.",
            ),
            (
                "The word class picks the strong part",
                "A noun of two parts is strong on the first part: "
                "the first part of <em>money</em> or <em>action</em>. A verb of "
                "two parts is strong on the second: the second part of "
                "<em>decide</em> or <em>believe</em>. "
                "You do not learn each word. You ask what kind of word it is.",
            ),
            (
                "A rule is scored on the words it can be tried on",
                "Many common words are a noun and a verb at once, such as "
                "<em>answer</em> and <em>water</em>. For them the rule has "
                "nothing to say, because it needs one class. The table scores "
                "only the words that have one class, and keeps the words that "
                "have both on a list of their own.",
            ),
        ],
        "steps_title": "Putting the strong part in a new word",
        "steps_intro": "Four steps, then a check.",
        "steps": [
            (
                "Count the parts",
                "Say the word slowly and tap once for each beat. "
                "<em>Money</em> has two. If the word has one part, there is "
                "nothing to choose.",
            ),
            (
                "Ask what the word is doing in your sentence",
                "A thing, or an action? <em>I need advice</em> uses a noun. "
                "<em>I will believe it</em> uses a verb.",
            ),
            (
                "Noun: strong part first. Verb: strong part second",
                "<em>Action</em>, <em>brother</em>, <em>country</em>. "
                "<em>Accept</em>, <em>agree</em>, <em>explain</em>.",
            ),
            (
                "If the word is both, say it the way the sentence uses it",
                "<em>Record</em> is strong on the first part as a noun and on "
                "the second part as a verb. The table lists 49 words like it.",
            ),
            (
                "Check the short lists of words that break the rule",
                "Each miss has a reason, and the reasons are below.",
            ),
        ],
        "lab": ("english", {
            "mode": "stress",
            "rules": ["nouns2", "verbs2", "adj2", "pairs"],
            "panel_title": "Score the rule for each kind of word",
            "panel_intro": (
                "Choose a kind of word. The page takes every word of that kind "
                "that has two parts, puts the strong part where the rule says, "
                "and checks it against the strong part a pronouncing dictionary "
                "marks. The setting called <em>the words set aside</em> shows "
                "which words were not scored, and why. The sounds are American, "
                "from the dictionary's first reading of each word."
            ),
        }),
        "read_title": "The words that break the rule",
        "read_intro": (
            "The noun rule misses 24 words of 231, the verb rule 16 of 150 and "
            "the adjective rule 12 of 47. The words sort into a few kinds."
        ),
        "worked": {
            "title": "Three words, three answers",
            "intro": [
                "Name the class, apply the rule, and check the table. The last "
                "word is one of the 24 the noun rule misses.",
            ],
            "lines": [
                "money   a noun    rule: first    said: first",
                "decide  a verb    rule: second   said: second",
                "hotel   a noun    rule: first    said: second",
                "",
                "207 of 231 nouns, 134 of 150 verbs",
            ],
            "after": [
                "<em>Money</em> and <em>decide</em> are the usual case. The "
                "rule says where the strong part is, and the dictionary agrees.",
                "<em>Hotel</em> is a noun, so the rule says first, but it is "
                "said <em>ho</em>-<em>tel</em> with the push on the second "
                "part. It is one of the 11 nouns that sit alone, and the lab "
                "lists it with them. A rule counted on a list is a pattern, "
                "and a pattern has words outside it.",
            ],
        },
        "note": (
            "<em>Record</em> is the clearest case of the rule at work. As a "
            "noun, <em>a record</em> is strong on the first part. As a verb, "
            "<em>to record</em> is strong on the second. The spelling is the "
            "same. The strong part tells the listener which word it is."
        ),
        "mistakes": [
            (
                "Thinking the strong part has no rule",
                "To someone learning it looks like something to memorise one word at "
                "a time. For nouns and verbs of two parts there is a rule, and it "
                "is right 207 times of 231 and 134 times of 150, about nine "
                "times in ten.",
            ),
            (
                "Putting the strong part on the same part in a noun and its verb",
                "<em>I need a permit</em> and <em>they permit it</em> are "
                "different words to the ear. The noun is strong on the first "
                "part and the verb on the second. A listener hears the class "
                "before the sentence is finished.",
            ),
            (
                "Using the rule for every word",
                "It covers words of two parts. A word of three parts such as "
                "<em>family</em> or <em>important</em> has its own patterns, "
                "and the next two lessons give the ones with an ending.",
            ),
        ],
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "Where is the strong part of <em>action</em>, a noun of two parts?",
                "a": [
                    "On the second part",
                    "On the first part",
                    "On both parts equally",
                    "It depends on the sentence",
                ],
                "c": 1,
                "why": (
                    "A noun of two parts is strong on the first part: "
                    "the <em>ac</em> of <em>action</em>. The sentence does not change it, because "
                    "<em>action</em> is only a noun."
                ),
            },
            {
                "q": "Which of these is a verb of two parts with the strong part on the second?",
                "a": ["<em>action</em>", "<em>country</em>", "<em>brother</em>", "<em>believe</em>"],
                "c": 3,
                "why": (
                    "<em>Believe</em> is strong on its second part. The other three "
                    "are nouns, and each is strong on its first part."
                ),
            },
            {
                "q": "<em>Advice</em> is a noun, and the noun rule misses it. What kind of miss is it?",
                "a": [
                    "A noun made from a verb, <em>advise</em>, that keeps the strong part at the back",
                    "A word with only one part",
                    "A word that is both a noun and a verb",
                    "A word that is too rare for the dictionary",
                ],
                "c": 0,
                "why": (
                    "<em>Advice</em> and <em>advise</em> are one word in two "
                    "forms, and the noun keeps the strong part of the verb. "
                    "<em>Belief</em>, <em>relief</em> and <em>device</em> are "
                    "the same kind."
                ),
            },
            {
                "q": "What does it mean that <em>record</em> is on the list of 49 words said both ways?",
                "a": [
                    "The dictionary is not sure how to say it",
                    "It is a very old word",
                    "Its noun and its verb are strong on different parts",
                    "Speakers in two countries say it differently",
                ],
                "c": 2,
                "why": (
                    "The list holds words that are a noun and a verb, with a "
                    "reading strong on the first part and another strong on the "
                    "second. That is the rule showing up inside one spelling."
                ),
            },
        ],
        "body": [
            ("p",
             "Say <em>money</em>. Then say <em>decide</em>. Both have two parts, "
             "and in each one part is stronger. In <em>money</em> it is the "
             "first. In <em>decide</em> it is the second. A listener uses the "
             "strong part to find the word, so a student who puts it in the "
             "wrong place is often not understood, even when every sound in "
             "the word is right."),
            ("h3", "A part, and the strong part"),
            ("p",
             "A <dfn>part</dfn> is one beat of a word. <em>Money</em> has two, "
             "<em>decide</em> has two and <em>tomorrow</em> has three. In every "
             "word of two or more parts, one part is said longer, louder and "
             "higher than the others. This course calls it the strong part. "
             "A pronouncing <dfn>dictionary</dfn>, a book that says how "
             "every word is said, marks it, and the page uses one."),
            ("h3", "The rule"),
            ("ul", [
                "A <strong>noun</strong> of two parts is strong on the "
                "<strong>first</strong> part: <em>action</em>, "
                "<em>brother</em>, <em>country</em>, <em>kitchen</em>.",
                "A <strong>verb</strong> of two parts is strong on the "
                "<strong>second</strong> part: <em>accept</em>, "
                "<em>agree</em>, <em>explain</em>, <em>enjoy</em>.",
                "An <strong><dfn>adjective</dfn></strong> of two parts, a word "
                "that tells a quality, is strong on the "
                "<strong>first</strong> part, as a noun is: <em>angry</em>, "
                "<em>famous</em>, <em>lazy</em>. It is the weakest of the three "
                "rules.",
            ]),
            ("h3", "How often the rule is right"),
            ("p",
             "The lab takes the words of two parts that the build step found "
             "to be only a noun, only a verb or only an adjective, and checks "
             "each against the dictionary. Counted on this page, the noun rule "
             "is right for 207 of 231 words, 89.6%. The verb rule is right for "
             "134 of 150, 89.3%. The adjective rule is right for 35 of 47, "
             "74.5%."),
            ("p",
             "Nine in ten is a good rule for a thing you do in every sentence. "
             "Three in four for adjectives is a weaker one, and the lab says "
             "so. Which words are only a noun, only a verb or only an adjective "
             "was decided once, from a printed word list, and is not on the "
             "page. The words that have more than one class, such as "
             "<em>answer</em>, are not scored, and the setting called <em>the "
             "words set aside</em> shows them."),
            ("h3", "The 24 nouns that break the rule"),
            ("p",
             "The noun rule says first, and these are said with the push "
             "somewhere else. They sort into three kinds."),
            ("ul", [
                "<strong>A noun made from a verb</strong>: <em>advice</em>, "
                "<em>belief</em>, <em>complaint</em>, <em>constraint</em>, "
                "<em>defense</em>, <em>device</em>, <em>offense</em>, "
                "<em>relief</em>, <em>response</em> and <em>success</em>. Each "
                "is the verb's word in a new form: <em>advise</em>, "
                "<em>believe</em>, <em>complain</em>, <em>constrain</em>, "
                "<em>defend</em>, <em>devise</em>, <em>offend</em>, "
                "<em>relieve</em>, <em>respond</em>, <em>succeed</em>. The "
                "verb is strong at the back, and the noun keeps it there. Ten "
                "of the 24.",
                "<strong>A number or a month</strong>: <em>eighteen</em>, "
                "<em>fifteen</em> and <em>July</em>. The numbers that end in "
                "<em>-teen</em> take the push at the end, and that is how a "
                "listener tells <em>fifteen</em> from <em>fifty</em>. Three of "
                "the 24.",
                "<strong>A word that sits alone</strong>: <em>affair</em>, "
                "<em>decade</em>, <em>disease</em>, <em>estate</em>, "
                "<em>event</em>, <em>exam</em>, <em>extent</em>, "
                "<em>guitar</em>, <em>hello</em>, <em>hotel</em> and "
                "<em>technique</em>. Most of these came into English from "
                "French, which puts the push at the end of a word, and they "
                "kept it there. <em>Exam</em> is cut from "
                "<em>examination</em> and keeps that word's beat, and "
                "<em>hello</em> is a call, not a thing. Learn these as a "
                "list. Eleven of the 24.",
            ]),
            ("h3", "The 16 verbs that break the rule"),
            ("p",
             "The verb rule says second. Ten of the 16 are verbs whose second "
             "part is a weak ending: <em>alter</em>, <em>differ</em>, "
             "<em>enter</em>, <em>frighten</em>, <em>govern</em>, "
             "<em>listen</em>, <em>reckon</em>, <em>strengthen</em>, "
             "<em>suffer</em> and <em>threaten</em>. Say them and the second "
             "part is only a flat sound and a consonant, too light to carry the "
             "push, so it stays on the first. The other six are "
             "<em>argue</em>, <em>injure</em>, <em>license</em>, "
             "<em>locate</em>, <em>marry</em> and <em>premise</em>. "
             "<em>Argue</em>, <em>injure</em> and <em>marry</em> also end in "
             "a light second part. <em>License</em> and <em>premise</em> "
             "are nouns first and verbs second, and keep the noun's push. "
             "<em>Locate</em> is said both ways, and the dictionary's first "
             "reading is the American one. The last lesson of this course is "
             "about the flat sound."),
            ("h3", "The 12 adjectives that break the rule"),
            ("p",
             "The adjective rule says first, and every one of its 12 misses "
             "begins with a front piece that takes no push. Six begin with "
             "<em>a-</em> or <em>un-</em>: <em>afraid</em>, <em>alive</em>, "
             "<em>ashamed</em>, <em>aware</em>, <em>unclear</em> and "
             "<em>unlike</em>. The other six begin with a front piece that "
             "came with the word from Latin: <em>distinct</em>, "
             "<em>intense</em>, <em>precise</em>, <em>remote</em>, "
             "<em>severe</em> and <em>toward</em>. When a two-part adjective "
             "starts with a piece like these, the push is on the second part, "
             "and the rule for adjectives is best read as: first, unless the "
             "word begins with a front piece."),
            ("h3", "Words that are both"),
            ("p",
             "The lab also lists 49 words that the build step found to be both "
             "a noun and a verb, and for which the dictionary gives two "
             "readings, strong on different parts. They include "
             "<em>address</em>, <em>contract</em>, <em>increase</em>, "
             "<em>object</em>, <em>permit</em>, <em>present</em>, "
             "<em>produce</em>, <em>project</em>, <em>protest</em>, "
             "<em>record</em>, <em>refuse</em>, <em>subject</em> and "
             "<em>survey</em>. Take <em>present</em>: <em>a present</em> is "
             "strong on the first part, and <em>to present</em> on the "
             "second. Say each one in a sentence, and check yourself by asking "
             "which class you meant."),
            ("p",
             "Two limits. The sounds are American, from the dictionary's first "
             "reading of each word, and a British speaker may put the push "
             "elsewhere in a few of them. And the rule tells you where the "
             "strong part is, not what the word means."),
        ],
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "endings-that-pull-the-stress",
        "module": "Endings",
        "title": "Endings That Pull the Stress",
        "one_line": "Some endings decide where the strong part goes, and each of six is right for nearly every word in the list.",
        "standard": (
            "Finish when you can place the strong part in a word that ends in "
            "-tion, -ic, -ical, -ity, -ate, -ize or -ee without hearing it "
            "first.",
            "You should be able to say, for each of these endings, which part "
            "is strong, read each rule's score off the table, and say why a "
            "word is on its list of misses.",
        ),
        "summary": (
            "An ending can fix where the strong part goes, whatever the word "
            "was before. Before <em>-tion</em> and <em>-ic</em> it is the part "
            "just before the ending. Before <em>-ical</em>, <em>-ity</em>, "
            "<em>-ate</em> and <em>-ize</em> it is the third part from the end. "
            "Counted on the 2,800 words, six of these rules miss no more than "
            "one word each, and the last is right for two words in three."
        ),
        "key_label": "Counted on the 2,800 words",
        "key": [
            "-tion, -sion   part before it  151 of 152",
            "-ic            part before it   28 of 28",
            "-ical, -ity    third from end   16, 27",
            "-ate, -ize     third from end   36, 13",
            "-ee            the ending itself 8 of 12",
        ],
        "concepts_intro": "Three ideas. The first is the surprise.",
        "concepts": [
            (
                "An ending can move the strong part",
                "<em>Educate</em> is strong on its first part. Add "
                "<em>-tion</em> and the push moves to the part before the "
                "ending: <em>education</em>. The word before the ending does "
                "not decide. The ending does.",
            ),
            (
                "Each ending has its place, counted from the end",
                "Before <em>-tion</em>, <em>-sion</em> and <em>-ic</em> the "
                "strong part is the one just before the ending. Before "
                "<em>-ical</em>, <em>-ity</em>, <em>-ate</em> and "
                "<em>-ize</em> it is the third part from the end, with two "
                "parts after it. Counting from the end works because the word "
                "can be any length.",
            ),
            (
                "A rule this good is still a rule, so read the misses",
                "<em>Television</em> is the one miss for <em>-sion</em>, and "
                "<em>characterize</em> the one for <em>-ize</em>. The "
                "<em>-ee</em> rule is weaker, and its four misses show why: "
                "an ending can be spelled the same and not carry the push.",
            ),
        ],
        "steps_title": "Placing the strong part in a word with an ending",
        "steps_intro": "To place it in a word you have not heard, do this.",
        "steps": [
            (
                "Look at the ending, not the front of the word",
                "The ending decides. Do not say the word before the ending "
                "and carry its push forward.",
            ),
            (
                "Find the ending's rule",
                "<em>-tion</em>, <em>-sion</em>, <em>-ic</em>: the part just "
                "before the ending. <em>-ical</em>, <em>-ity</em>, "
                "<em>-ate</em>, <em>-ize</em>: the third part from the end. "
                "<em>-ee</em>: the ending itself.",
            ),
            (
                "Count back from the end",
                "<em>Ability</em> has four parts: a, bil, i, ty. The third "
                "from the end is <em>bil</em>.",
            ),
            (
                "Say it with the push there, and the other parts weak",
                "Then check by saying the word the other way. The wrong one "
                "sounds foreign at once.",
            ),
            (
                "Check the short list of misses",
                "<em>Television</em> and <em>characterize</em> have their "
                "own push, and so do four words in <em>-ee</em>.",
            ),
        ],
        "lab": ("english", {
            "mode": "stress",
            "rules": ["tion", "ic", "ical", "ity", "ate", "ize", "ee"],
            "panel_title": "Score each ending's rule",
            "panel_intro": (
                "Choose an ending. The page finds every word of the list that "
                "has it, counts the parts, puts the strong part where the rule "
                "says and checks it against the strong part a pronouncing "
                "dictionary marks. The ending <em>-ate</em> is scored on verbs "
                "of three or more parts, and the others on words long enough "
                "for the rule. The setting called <em>the words set aside</em> "
                "shows what was left out. The sounds are American."
            ),
        }),
        "read_title": "The words that break the rules",
        "read_intro": (
            "Four of the rules miss no word, two miss one word each, and the "
            "rule for <em>-ee</em> misses four."
        ),
        "worked": {
            "title": "Moving the strong part with an ending",
            "intro": [
                "Each line takes a word, adds an ending, and says where the "
                "strong part goes.",
            ],
            "lines": [
                "educate       3 parts   strong: the first",
                "education     4 parts   strong: the third",
                "able          2 parts   strong: the first",
                "ability       4 parts   strong: the second",
                "celebrate     3 parts   strong: the first",
            ],
            "after": [
                "<em>Education</em> has four parts and the rule for "
                "<em>-tion</em> asks for the part just before the ending, "
                "which is the third. <em>Ability</em> has four parts and the "
                "rule for <em>-ity</em> asks for the third from the end, which "
                "is the second.",
                "<em>Celebrate</em> has three parts, and the third from the "
                "end is the first. The same rule gives a different part in a "
                "word of a different length, which is why the count is from "
                "the end.",
            ],
        },
        "note": (
            "A strong part that moves often leaves the part it left with no "
            "clear vowel. The first part of <em>able</em> has a clear vowel; "
            "in <em>ability</em> it has the flat sound. Not always: the first "
            "part of <em>educate</em> keeps a smaller beat and its clear "
            "vowel in <em>education</em>. The last lesson of this course is "
            "about what a weak part is said as."
        ),
        "mistakes": [
            (
                "Thinking the stress of photograph stays in photography",
                "It does not. <em>Photograph</em> is strong on its first part "
                "and <em>photography</em> on its second. An ending can move "
                "the push, and this lesson has seven endings that do. Each "
                "one is counted.",
            ),
            (
                "Counting from the front of the word",
                "A rule such as <em>the third part</em> gives the wrong part "
                "in a word of four. <em>Education</em> has the push on its "
                "third part, <em>ability</em> on its second. Count from the "
                "end, where the ending is.",
            ),
            (
                "Thinking -ee works like the others",
                "The other six endings leave the push before them. The "
                "<em>-ee</em> rule puts it on the ending, as in "
                "<em>agree</em> and <em>engineer</em>. It is also the weakest "
                "of the seven.",
            ),
        ],
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "Where is the strong part of <em>education</em>?",
                "a": [
                    "On the first part",
                    "On the last part",
                    "On the part just before <em>-tion</em>",
                    "On the part <em>-tion</em> itself",
                ],
                "c": 2,
                "why": (
                    "The ending <em>-tion</em> puts the push on the part before "
                    "it: <em>edu</em>-<em>ca</em>-tion. In <em>education</em> "
                    "that is the third of four parts."
                ),
            },
            {
                "q": "Which word has the strong part on the <em>second</em> part?",
                "a": ["<em>ability</em>", "<em>celebrate</em>", "<em>educate</em>", "<em>chemical</em>"],
                "c": 0,
                "why": (
                    "<em>Ability</em> has four parts, and the rule for "
                    "<em>-ity</em> asks for the third from the end, which is "
                    "the second. The other three are strong on their first "
                    "part."
                ),
            },
            {
                "q": "Why do the rules count from the end of the word?",
                "a": [
                    "Because the front of a word is always weak",
                    "Because dictionaries are written backwards",
                    "Because it is easier to say the end first",
                    "Because the ending carries the rule, and words differ in length",
                ],
                "c": 3,
                "why": (
                    "The rule belongs to the ending, so its place is measured "
                    "from the ending. <em>Chemical</em> has three parts and "
                    "<em>biological</em> has five, and the strong part is the "
                    "third from the end in both."
                ),
            },
            {
                "q": "The rule for <em>-ee</em> is right for 8 of 12 words. What does that say?",
                "a": [
                    "The rule is wrong and should be dropped",
                    "It is much weaker than the other six, so check the list of misses every time",
                    "It is as good as the rule for <em>-ity</em>",
                    "Words in <em>-ee</em> have no strong part",
                ],
                "c": 1,
                "why": (
                    "Two thirds is a pattern, not a rule to rely on. "
                    "<em>Coffee</em>, <em>committee</em>, <em>employee</em> and "
                    "<em>refugee</em> are the four words it misses."
                ),
            },
        ],
        "body": [
            ("p",
             "The first lesson of this course put the strong part by the class "
             "of the word. A word with an ending is different. The ending "
             "itself says where the strong part goes, and it can move the push "
             "away from where it was in the word you started with."),
            ("h3", "The rules"),
            ("ul", [
                "<strong><em>-tion</em> and <em>-sion</em></strong>: the part "
                "just before the ending. <em>Station</em>, <em>education</em>.",
                "<strong><em>-ic</em></strong>: the part just before the "
                "ending. <em>Basic</em>, <em>economic</em>.",
                "<strong><em>-ical</em></strong>: the third part from the end. "
                "<em>Chemical</em>, <em>political</em>.",
                "<strong><em>-ity</em></strong>: the third part from the end. "
                "<em>Ability</em>, <em>community</em>.",
                "<strong><em>-ate</em></strong>, for a verb of three or more "
                "parts: the third part from the end. <em>Celebrate</em>, "
                "<em>operate</em>.",
                "<strong><em>-ize</em></strong>, and the spelling "
                "<em>-ise</em>, for a word of three or more parts: the third "
                "part from the end. <em>Realize</em>, <em>organize</em>.",
                "<strong><em>-ee</em></strong>, and <em>-eer</em>, "
                "<em>-ese</em> and <em>-ette</em>: the ending itself. "
                "<em>Agree</em>, <em>engineer</em>.",
            ]),
            ("h3", "How often each rule is right"),
            ("p",
             "Counted on this page against the dictionary, the rule for "
             "<em>-tion</em> and <em>-sion</em> is right for 151 of 152 words, "
             "99.3%. The rule for <em>-ic</em> is right for 28 of 28, "
             "<em>-ical</em> for 16 of 16, <em>-ity</em> for 27 of 27 and "
             "<em>-ate</em> for 36 of 36. The rule for <em>-ize</em> is right "
             "for 13 of 14, 92.9%. The table reads the spelling, so the 14 "
             "include five words spelled <em>-ise</em>: <em>advertise</em> "
             "and <em>compromise</em>, which are built with the ending, and "
             "<em>exercise</em>, <em>enterprise</em> and <em>otherwise</em>, "
             "which are not. All five follow the pattern anyway."),
            ("p",
             "Each rule applies only where the word is long enough for the "
             "rule to make sense. The table sets aside <em>-ate</em> words "
             "that are not verbs, such as <em>accurate</em> and "
             "<em>candidate</em>, and words of fewer than three parts, such "
             "as <em>create</em>, <em>date</em> and <em>private</em>. It also "
             "sets aside <em>city</em>, the one word in <em>-ity</em> with "
             "only two parts. It says why beside each one."),
            ("h3", "The two misses"),
            ("p",
             "<em>Television</em> has four parts and is strong on the first. "
             "The rule asked for the third, the part before <em>-sion</em>, "
             "and some British speakers do say it there; the American reading "
             "does not. "
             "<em>Characterize</em> has four parts and is strong on the "
             "first, and the rule asked for the second, the third from the "
             "end. The word is built on <em>character</em>, which is strong "
             "on its first part, and the longer word keeps the push of its "
             "base. Both are single words to learn by name."),
            ("h3", "The weaker rule, -ee"),
            ("p",
             "The rule for <em>-ee</em> reads the last strong part the "
             "dictionary marks, and asks for it on the ending. Counted on "
             "this page it is right for 8 of 12 words, 66.7%. Nine short words "
             "are set aside because they have only one part and there is "
             "nothing to choose: <em>see</em>, <em>free</em>, <em>tree</em> "
             "and six more. One of the nine is <em>cheese</em>, the only word "
             "in <em>-ese</em> on the list, so that ending is named in the "
             "rule and never scored."),
            ("p",
             "The four misses are <em>coffee</em>, <em>committee</em>, "
             "<em>employee</em> and <em>refugee</em>. In all four the "
             "dictionary's first reading gives the ending no push at all: the "
             "<em>-ee</em> is said like the <em>-y</em> of <em>happy</em>. "
             "<em>Coffee</em> and <em>refugee</em> are strong on the first "
             "part, <em>committee</em> and <em>employee</em> on the second. "
             "Many speakers do put the push on the ending of "
             "<em>employee</em> and <em>refugee</em>, and for "
             "<em>refugee</em> that is the usual British reading, but the "
             "dictionary's first reading is the one the page scores. So a "
             "spelling in <em>-ee</em> does not always "
             "carry the push; the rule works for <em>agree</em>, "
             "<em>degree</em> and <em>engineer</em> and fails for these "
             "four."),
            ("p",
             "Two limits. The sounds are American, from the dictionary's first "
             "reading of each word. And the rules say where the push goes, not "
             "what an ending adds to the meaning."),
        ],
    },
]
