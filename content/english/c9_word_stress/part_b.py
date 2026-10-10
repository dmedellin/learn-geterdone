# -*- coding: utf-8 -*-
"""Course eight, lessons three and four: endings that leave the strong part alone, the flat vowel.

Every figure is read off the `stress` lab with `labcheck.js --observe`:
-ly 83 of 87 (95.4%), -ness 6 of 6, -ment 31 of 32 (96.9%), -er 48 of 50 (96.0%),
-ful 7 of 7, -able 10 of 10; 2628 weak parts in 1779 words, the flat vowel 1387
(52.8%), the flat vowel with r 400, the vowel of sit 352, the vowel of see 348.
The remainder (141) and the two shares 15.2% and 13.4% and 13.2% are arithmetic on
those tiles. Every word named in the prose is a word in the lab's own tables,
except airline, which The Flat Vowel names as a word the table does NOT hold
(its second part carries a secondary stress, EH1 R L AY2 N, so it has no part
with no beat and is left out), and the pair fifteen and fifty is not named here.
The schwa rows keep only the parts CMUdict marks "0"; a part marked "2" is
neither strong nor counted, and the prose says so.
The dictionary facts behind the prose (perfect's first reading is the verb
P ER0 F EH1 K T, research's is R IY0 S ER1 CH, engineer is EH1 N JH AH0 N IH1 R,
career is in the -eer rows of lesson two, the false pairs listed in lesson
three are all rows of the er, ly, ment, ness and able rules) were checked against
b_stress.json and cmudict.dict in docs/english-v2/measure/data on 2026-10-10.

Spoken forms for the orchestrator are in content/spoken/english_c9_word_stress.py.
"""

LESSONS = [
    # ---------------------------------------------------------------- 03
    {
        "slug": "endings-that-leave-it-alone",
        "module": "Endings",
        "title": "Endings That Leave It Alone",
        "one_line": "Six common endings add a part and keep the strong part of the word where it was, in nearly every pair.",
        "standard": (
            "Finish when you can add -ly, -ness, -ment, -er, -ful or -able to "
            "a word without moving its strong part.",
            "You should be able to say where the strong part of the longer word "
            "is, read each ending's score off the table, and explain why the "
            "words that miss the rule miss it.",
        ),
        "summary": (
            "The last lesson was about endings that move the strong part. These "
            "six do not. Add <em>-ness</em> to <em>happy</em> and the strong "
            "part stays on the first part. Counted on word pairs from the 2,800, "
            "the strong part stays put in 185 of the 192 pairs, and the "
            "seven that move are mostly easy to explain."
        ),
        "key_label": "Counted on pairs from the 2,800 words",
        "key": [
            "-ly      83 of 87      -ment   31 of 32",
            "-ness     6 of 6       -ful     7 of 7",
            "-er      48 of 50      -able   10 of 10",
            "",
            "the word keeps the strong part it had",
        ],
        "concepts_intro": "Three ideas. The second one matters most when you speak.",
        "concepts": [
            (
                "Some endings add a part and change nothing else",
                "<em>Happy</em> is strong on its first part. <em>Happiness</em> "
                "has one more part, and it is strong on the first part too. The "
                "ending is weak. It sits at the end and does not take the push.",
            ),
            (
                "A student's mistake is to move it",
                "A student who has just met <em>-tion</em> and <em>-ity</em> "
                "may move the push in every long word. That puts the push "
                "on the end of <em>teacher</em>, which is wrong. The word you "
                "started with is the guide for these six endings.",
            ),
            (
                "A pair is two words from the list that differ by the ending",
                "The table forms a pair only where both the short word and the "
                "longer word are in the 2,800 and in the dictionary. It puts "
                "back a dropped <em>-e</em> or changed <em>-y</em> first, so "
                "<em>argue</em> and <em>argument</em> are a pair and so are "
                "<em>happy</em> and <em>happiness</em>.",
            ),
        ],
        "steps_title": "Adding an ending without moving the strong part",
        "steps_intro": "Four steps, then one check.",
        "steps": [
            (
                "Say the short word and find its strong part",
                "<em>Agree</em> is strong on its second part. <em>Care</em> "
                "has one part, and it is the strong one.",
            ),
            (
                "Check the ending is one of the six",
                "<em>-ly</em>, <em>-ness</em>, <em>-ment</em>, <em>-er</em>, "
                "<em>-ful</em> or <em>-able</em>. If it is one of the seven in "
                "the last lesson, use that rule instead.",
            ),
            (
                "Say the longer word with the push where it was",
                "<em>Agreement</em> is strong on its second part. "
                "<em>Careful</em> is strong on its first.",
            ),
            (
                "Keep the new part weak",
                "The ending is quiet. Do not give <em>-ful</em> or "
                "<em>-ness</em> the vowel of the word they come from.",
            ),
            (
                "Check the short list of misses",
                "<em>Advertisement</em> is one. The reasons for the others "
                "are below.",
            ),
        ],
        "lab": ("english", {
            "mode": "stress",
            "rules": ["ly", "ness", "ment", "er", "ful", "able"],
            "panel_title": "Score each ending",
            "panel_intro": (
                "Choose an ending. The page finds the pairs in the list, a short "
                "word and the same word with the ending, and checks whether the "
                "strong part is on the same part in both. It reads the "
                "dictionary's first reading of each word, which is American. "
                "The setting called <em>every word scored</em> shows the pairs "
                "that are right too."
            ),
        }),
        "read_title": "The pairs that move",
        "read_intro": (
            "Seven pairs of 192 have the strong part on a different part in "
            "the longer word. A few kinds explain them."
        ),
        "worked": {
            "title": "Four pairs and one that moves",
            "intro": [
                "The first four keep the strong part. The last is the one "
                "<em>-ment</em> pair that does not.",
            ],
            "lines": [
                "happy      strong: first      happiness     first",
                "agree      strong: second     agreement     second",
                "care       strong: first      careful       first",
                "teach      strong: first      teacher       first",
                "advertise  strong: first      advertisement second",
            ],
            "after": [
                "In the first four the longer word is the short word with a "
                "weak part added. In <em>advertisement</em> the dictionary puts "
                "the strong part on the second part, <em>ver</em>, while "
                "<em>advertise</em> has it on the first. It is the only one of "
                "the 32 <em>-ment</em> pairs where the push moves.",
            ],
        },
        "note": (
            "These six endings and the seven of the last lesson are the "
            "whole of this course's rules for endings. If an ending is in "
            "the last lesson, count from the end. If it is one of these six, "
            "leave the push where it was."
        ),
        "mistakes": [
            (
                "Thinking every ending moves the stress",
                "After <em>-tion</em> and <em>-ity</em> it is natural to guess "
                "that every ending does. These six do not. The strong part of "
                "<em>happiness</em> stays on the first part, as in "
                "<em>happy</em>, and the rule is right for 185 of 192 pairs.",
            ),
            (
                "Giving the ending a strong vowel",
                "The ending <em>-ful</em> in <em>careful</em> is weak. Say it "
                "short, not as the word <em>full</em>. The same goes for "
                "<em>-ment</em>, <em>-ness</em> and <em>-able</em>.",
            ),
            (
                "Trusting a pair because the spelling matches",
                "The table pairs words by spelling. <em>Beer</em> is paired "
                "with <em>be</em>, <em>bother</em> with <em>both</em> and "
                "<em>shoulder</em> with <em>should</em>. These are false pairs, "
                "not words built with <em>-er</em>, and they are counted all "
                "the same.",
            ),
        ],
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "Where is the strong part of <em>happiness</em>?",
                "a": [
                    "On the first part, where it is in <em>happy</em>",
                    "On the part just before <em>-ness</em>",
                    "On <em>-ness</em> itself",
                    "On the third part from the end",
                ],
                "c": 0,
                "why": (
                    "<em>-ness</em> leaves the push alone, so <em>happiness</em> "
                    "is strong on its first part. The second part, "
                    "<em>pi</em>, is the one an ending that pulls the stress "
                    "would choose."
                ),
            },
            {
                "q": "Which pair moves the strong part?",
                "a": [
                    "<em>agree</em> and <em>agreement</em>",
                    "<em>teach</em> and <em>teacher</em>",
                    "<em>advertise</em> and <em>advertisement</em>",
                    "<em>care</em> and <em>careful</em>",
                ],
                "c": 2,
                "why": (
                    "<em>Advertise</em> is strong on its first part and "
                    "<em>advertisement</em> on its second. It is the one "
                    "<em>-ment</em> pair out of 32 that moves."
                ),
            },
            {
                "q": "<em>Career</em> is paired with <em>care</em> and counted as a miss for <em>-er</em>. What does that show?",
                "a": [
                    "The rule moves the push in short words",
                    "The table pairs by spelling, and <em>career</em> is not <em>care</em> with an ending",
                    "<em>Career</em> is a verb",
                    "The dictionary does not know the word",
                ],
                "c": 1,
                "why": (
                    "A pair found by spelling can be a false pair. "
                    "<em>Career</em> is a word of its own, and the rule was "
                    "tried on it by accident. The table prints it so you can "
                    "strike it out."
                ),
            },
            {
                "q": "Which statement about the six endings in this lesson is true?",
                "a": [
                    "Each moves the strong part to the part just before it",
                    "Each puts the strong part on the ending",
                    "Each moves it to the third part from the end",
                    "Each leaves the strong part where it was in the shorter word",
                ],
                "c": 3,
                "why": (
                    "Counted on 192 pairs, the longer word keeps the strong "
                    "part of the shorter one in 185. The first three "
                    "statements describe the endings of the last lesson."
                ),
            },
        ],
        "body": [
            ("p",
             "The last lesson gave seven endings that decide where the strong "
             "part goes. Most endings are not like that. When you add "
             "<em>-ness</em> to <em>happy</em> or <em>-er</em> to "
             "<em>teach</em>, you make a longer word that is strong on the "
             "same part as the word you began with. Each part is built "
             "around a <dfn>vowel</dfn>, a sound made with the mouth open, "
             "as in <em>see</em>, and the ending adds one more."),
            ("h3", "The rule"),
            ("p",
             "Add the ending, and leave the strong part where it was. The six "
             "endings the lab tests are these:"),
            ("ul", [
                "<strong><em>-ly</em></strong>: <em>quick</em>, "
                "<em>quickly</em>. <strong><em>-ness</em></strong>: "
                "<em>dark</em>, <em>darkness</em>.",
                "<strong><em>-ment</em></strong>: <em>agree</em>, "
                "<em>agreement</em>. <strong><em>-er</em></strong>: "
                "<em>teach</em>, <em>teacher</em>.",
                "<strong><em>-ful</em></strong>: <em>care</em>, "
                "<em>careful</em>. <strong><em>-able</em></strong>: "
                "<em>accept</em>, <em>acceptable</em>.",
            ]),
            ("h3", "How often the rule is right"),
            ("p",
             "Counted on this page, the strong part stays where it was in 83 "
             "of 87 pairs with <em>-ly</em>, 95.4%. It stays in 6 of 6 with "
             "<em>-ness</em>, 31 of 32 with <em>-ment</em>, 96.9%, 48 of 50 "
             "with <em>-er</em>, 96.0%, 7 of 7 with <em>-ful</em> and 10 of "
             "10 with <em>-able</em>."),
            ("p",
             "The table forms a pair only when the short word and the longer "
             "word are both in the 2,800 and in the pronouncing <dfn>dictionary</dfn>, "
             "after putting back a dropped <em>-e</em> or a changed "
             "<em>-y</em>. That is why <em>-ness</em> has only six: the list "
             "holds few words in <em>-ness</em> whose short word it holds too. "
             "One of the six, <em>business</em> and <em>bus</em>, is a pair by "
             "spelling only, and the table counts it all the same."),
            ("h3", "The four misses for -ly"),
            ("p",
             "Three of the four are long words where the dictionary marks a "
             "strong beat early and a smaller one later. With the ending the "
             "main beat moves later: <em>absolute</em> to "
             "<em>absolutely</em>, <em>necessary</em> to <em>necessarily</em> "
             "and <em>primary</em> to <em>primarily</em>. The fourth, "
             "<em>perfectly</em>, is a mistake of reading. The "
             "dictionary's first reading of <em>perfect</em> is the verb, as "
             "in <em>to perfect a skill</em>, which is strong on the second "
             "part. <em>Perfectly</em> goes with the <dfn>adjective</dfn>, a word "
             "for a quality, which is "
             "strong on the first."),
            ("h3", "The one miss for -ment, and the two for -er"),
            ("p",
             "<em>Advertisement</em> is the miss for <em>-ment</em>, shown in "
             "the worked example. The two for <em>-er</em> are "
             "<em>career</em> and <em>researcher</em>. <em>Career</em> is a "
             "false pair: it is not <em>care</em> with an ending but a word "
             "in <em>-eer</em>, and the last lesson's rule for <em>-eer</em> "
             "gets it right. "
             "<em>Researcher</em> is paired with <em>research</em>, and "
             "<em>research</em> is one of the 49 words of the first lesson "
             "that are said two ways, so the pair was tried against the wrong "
             "reading."),
            ("p",
             "The table pairs by spelling and cannot tell a real ending from "
             "an accident, so it holds more false pairs than <em>career</em>, "
             "and nearly all of them land on the rule's side. <em>Beer</em> "
             "and <em>be</em>, <em>bother</em> and <em>both</em>, "
             "<em>shoulder</em> and <em>should</em>, <em>offer</em> and "
             "<em>off</em>, <em>flower</em> and <em>flow</em>, <em>only</em> "
             "and <em>on</em>, <em>early</em> and <em>ear</em>, "
             "<em>comment</em> and <em>come</em> and <em>capable</em> and "
             "<em>cap</em> are all counted right, because both words in each "
             "pair happen to be strong on the first part. So the false pairs "
             "help the rule a little, and <em>career</em> is the one that "
             "costs it. Strike them out by hand if you like. The table prints "
             "every pair."),
            ("p",
             "Two words are scored in both lessons about endings. "
             "<em>Career</em> is one. The other is <em>engineer</em>, paired "
             "here with "
             "<em>engine</em> by spelling. The dictionary marks it with two "
             "strong beats, one early and one on <em>-eer</em>. The last "
             "lesson reads the last, and this lesson reads the first, and "
             "both are right for the beat they read."),
            ("p",
             "Two limits. The sounds are American, from the dictionary's first "
             "reading of each word. And the table says where the push is, not "
             "which words an ending can join."),
        ],
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "the-flat-vowel",
        "module": "The weak part",
        "title": "The Flat Vowel",
        "one_line": "A part that is not strong usually takes one short sound, whatever vowel letter it is spelled with.",
        "standard": (
            "Finish when you can say a weak part of a word as the flat vowel "
            "instead of reading the letter, and name the endings that do not "
            "use it.",
            "You should be able to pick out the weak parts of a word, say each "
            "as the flat vowel, read the share of weak parts that take it off "
            "the table, and name the two kinds that take another vowel.",
        ),
        "summary": (
            "The strong part of a word keeps its vowel. The parts that are not "
            "strong are said with one short, plain sound, the flat vowel, "
            "whether they are spelled <em>a</em>, <em>e</em>, <em>o</em> or "
            "<em>u</em>. Counted on every word of two or more parts in the "
            "2,800, it is more than half of all the weak parts, and the two "
            "kinds that are not flat are easy to name."
        ),
        "key_label": "Counted on the 2,800 words",
        "key": [
            "weak parts counted        2628",
            "the flat vowel            1387  52.8%",
            "the flat vowel with r      400",
            "the vowel of sit           352",
            "the vowel of see           348",
        ],
        "concepts_intro": "Three ideas. The first two connect this lesson to the last three.",
        "concepts": [
            (
                "The weak part is every part that is not strong",
                "The first three lessons found the strong part. The rest of "
                "the word is weak, apart from a part that carries a smaller "
                "beat, as the first part of <em>education</em> does. The "
                "strong part keeps a clear vowel; a weak part gives up its "
                "vowel.",
            ),
            (
                "The vowel letter does not tell you the sound",
                "<em>About</em>, <em>today</em>, <em>listen</em> and "
                "<em>minute</em> have a weak part spelled with <em>a</em>, "
                "<em>o</em>, <em>e</em> and <em>u</em>. In all four it is said "
                "the same, with a short, plain sound that a mouth makes when "
                "it does not try. This is the flat vowel.",
            ),
            (
                "Two kinds of weak part are not flat",
                "The <em>y</em> at the end of <em>happy</em> is said as the "
                "vowel of <em>see</em>. The ending of <em>active</em> and "
                "<em>basic</em> takes the vowel of <em>sit</em>. A weak part "
                "is not always flat, but it is never as clear as a strong one.",
            ),
        ],
        "steps_title": "Saying the weak parts of a word",
        "steps_intro": "Four steps, in this order.",
        "steps": [
            (
                "Find the strong part",
                "Use the rules of the last three lessons, or the dictionary. "
                "In <em>about</em> it is <em>bout</em>.",
            ),
            (
                "Mark every other part as weak",
                "The first part of <em>about</em>, the second of "
                "<em>listen</em> and the last of <em>minute</em>.",
            ),
            (
                "Say each weak part with the flat vowel, not the letter",
                "Short, quiet, and the same sound for every vowel letter.",
            ),
            (
                "Check the end of the word",
                "A <em>y</em> at the end says the vowel of <em>see</em>. "
                "<em>-ive</em>, <em>-ic</em> and <em>-ing</em> say the vowel "
                "of <em>sit</em>. A part ending in <em>r</em> is the flat "
                "vowel with an <em>r</em>.",
            ),
        ],
        "lab": ("english", {
            "mode": "stress",
            "rules": ["schwa"],
            "show": "all",
            "panel_title": "Count the vowels of the weak parts",
            "panel_intro": (
                "The page takes every word of two or more parts in the list, "
                "finds the parts the dictionary marks with no beat at all, and "
                "reads each one's vowel from it. A part with a smaller beat is "
                "not counted. The four counts below "
                "the first tile are the four kinds of vowel it found. The "
                "table shows each word with the kind of each weak part. The "
                "sounds are American, from the dictionary's first reading of "
                "each word."
            ),
        }),
        "read_title": "What the weak parts say",
        "read_intro": (
            "Out of 2628 weak parts in 1779 words, four kinds of vowel "
            "account for nearly all."
        ),
        "worked": {
            "title": "Four spellings, one sound",
            "intro": [
                "Find the weak part of each word and say it. The letter is "
                "different each time and the sound is not.",
            ],
            "lines": [
                "about    weak part: a      said: the flat vowel",
                "today    weak part: to     said: the flat vowel",
                "listen   weak part: ten    said: the flat vowel",
                "minute   weak part: ute    said: the flat vowel",
            ],
            "after": [
                "The letters are <em>a</em>, <em>o</em>, <em>e</em> and "
                "<em>u</em>. A reader who says each as its letter says four "
                "different sounds, and none is the sound in the word.",
                "The next course, Listening, shows the same thing in the "
                "small words. &ldquo;Why It Sounds Too Fast&rdquo; counts how many "
                "of the words of a passage are small words said weak.",
            ],
        },
        "note": (
            "The flat vowel is the commonest vowel among the weak parts "
            "counted here. A student who says it well sounds clearer than one who "
            "says every vowel clearly, because the strong parts stand out."
        ),
        "mistakes": [
            (
                "Reading every vowel letter as itself",
                "A reader who says <em>a</em> in <em>about</em>, <em>o</em> "
                "in <em>today</em> and <em>e</em> in <em>listen</em> as those "
                "letters gives every part the same weight. In a weak part the "
                "letter mostly collapses to one sound, 1387 times in 2628, and "
                "400 more times with an <em>r</em> after it.",
            ),
            (
                "Thinking the flat vowel is a careless way to speak",
                "It is the standard way. The dictionary marks it for more than "
                "half of all the weak parts in the 2,800 words. A speaker "
                "who leaves it out is the one who sounds odd.",
            ),
            (
                "Thinking every weak part is flat",
                "The end of <em>happy</em> is the vowel of <em>see</em> and "
                "the end of <em>active</em> is the vowel of <em>sit</em>. "
                "These two kinds are 700 of the 2628, and the table lists "
                "them word by word.",
            ),
        ],
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "What vowel is in the weak part of <em>about</em>, <em>today</em>, <em>listen</em> and <em>minute</em>?",
                "a": [
                    "Four different vowels, one for each letter",
                    "The vowel of <em>see</em>",
                    "The vowel of <em>sit</em>",
                    "The same flat vowel, whatever the letter",
                ],
                "c": 3,
                "why": (
                    "The letters are <em>a</em>, <em>o</em>, <em>e</em> and "
                    "<em>u</em>, and the sound is one. The vowel of "
                    "<em>see</em> is what the end of <em>happy</em> says."
                ),
            },
            {
                "q": "The flat vowel is 1387 of 2628 weak parts. What is the best reading?",
                "a": [
                    "Almost every weak part takes it",
                    "About half of the weak parts take it, and with an <em>r</em> about two in three",
                    "Fewer than one in five takes it",
                    "Only parts spelled with <em>a</em> take it",
                ],
                "c": 1,
                "why": (
                    "1387 is a little over half of 2628. Add the 400 with an "
                    "<em>r</em> and it is 1787, a little over two in three."
                ),
            },
            {
                "q": "Which of these is <em>not</em> said with the flat vowel?",
                "a": [
                    "The <em>y</em> at the end of <em>happy</em>",
                    "The <em>a</em> at the start of <em>about</em>",
                    "The <em>man</em> of <em>woman</em>",
                    "The <em>ten</em> of <em>listen</em>",
                ],
                "c": 0,
                "why": (
                    "The end of <em>happy</em> says the vowel of <em>see</em>. "
                    "The other three are weak parts said with the flat vowel."
                ),
            },
            {
                "q": "Why does saying each vowel letter as itself make a word hard to follow?",
                "a": [
                    "Vowel letters are never said in English",
                    "The strong part is always the last one",
                    "In the weak parts, <em>a</em>, <em>e</em>, <em>o</em> and <em>u</em> mostly collapse to one sound, so the strong part stands out",
                    "Vowel letters are said as themselves only in verbs",
                ],
                "c": 2,
                "why": (
                    "The strong part stands out because the parts around it are "
                    "quiet. Give every part a clear vowel and the strong part "
                    "is lost."
                ),
            },
        ],
        "body": [
            ("p",
             "Say <em>about</em> slowly: a-bout. Now say it as you would in a "
             "sentence. The first part is so short that you hardly hear a "
             "vowel in it. The second carries the word. The first lesson of "
             "this course found where the strong part goes. This one is about "
             "the parts around it."),
            ("h3", "Weak parts"),
            ("p",
             "Every part of a word that is not the strong part is weak. A "
             "weak part is said shorter and quieter, and its vowel loses its "
             "clear shape. The sound it falls to most often has a name in this "
             "course: <dfn>the flat vowel</dfn>. It is the short, plain sound "
             "at the start of <em>about</em>, said with no effort, and it is "
             "the commonest vowel among the weak parts counted here."),
            ("h3", "What was counted"),
            ("p",
             "The lab takes every word of two or more parts in the 2,800 and "
             "keeps the parts the dictionary marks with no beat at all. A part "
             "with a smaller beat, such as the first part of "
             "<em>education</em>, keeps a clear vowel and is not counted, and "
             "a word whose other parts all carry one, such as "
             "<em>airline</em>, is not in the table. That leaves 1779 words "
             "and 2628 weak parts. For each "
             "weak part the lab reads the vowel from the pronouncing "
             "dictionary."),
            ("ul", [
                "<strong>The flat vowel</strong>: 1387 of 2628, 52.8%. "
                "<em>About</em>, <em>today</em>, <em>listen</em>.",
                "<strong>The flat vowel with <em>r</em></strong>: 400, 15.2%. "
                "The ending of <em>another</em> and <em>number</em>.",
                "<strong>The vowel of <em>sit</em></strong>: 352, 13.4%. "
                "<em>Active</em>, <em>basic</em>, <em>morning</em>.",
                "<strong>The vowel of <em>see</em></strong>: 348, 13.2%. "
                "<em>Happy</em>, <em>city</em>, <em>money</em>.",
                "<strong>Another vowel</strong>: the other 141, 5.4%. A part "
                "with no beat that keeps a clear vowel all the same, as the "
                "first part of <em>accept</em> and <em>employ</em> does.",
            ]),
            ("h3", "Why the spelling hides it"),
            ("p",
             "The flat vowel has no letter of its own. It is written with "
             "whichever vowel letter the word had when it was written down. "
             "In the lab, find <em>about</em>, <em>today</em>, "
             "<em>listen</em> and <em>minute</em> in the table, and read the "
             "kind of their weak parts. They are all the same kind, and the "
             "four spellings are the four letters in the worked example."),
            ("h3", "The two kinds that are not flat"),
            ("p",
             "Most of the 348 parts that say the vowel of <em>see</em> are the "
             "<em>-y</em> at the end of a word such as <em>happy</em>, "
             "<em>city</em> or <em>money</em>. It is weak, and it is not flat. "
             "The rest are mostly an <em>i</em> or <em>e</em> said before "
             "another vowel, as in <em>radio</em>, <em>area</em> and "
             "<em>create</em>, or the front piece <em>re-</em> of "
             "<em>remind</em> and <em>report</em>. "
             "The vowel of <em>sit</em> belongs to endings such as "
             "<em>-ive</em> in <em>active</em>, <em>-ic</em> in "
             "<em>basic</em> and <em>-ing</em> in <em>morning</em>, "
             "<em>evening</em> and <em>nothing</em>. The list holds few words "
             "that end in <em>-ing</em>, since it holds base forms, but the "
             "ones it holds follow the rule."),
            ("p",
             "Both are still weak. Say the <em>y</em> of <em>happy</em> quickly "
             "and lightly, and give the push to the first part."),
            ("h3", "What this does to the lessons before it"),
            ("p",
             "The rules of the last three lessons say where the strong part "
             "is. This lesson says what the rest sounds like. A word said "
             "with a clear strong part and flat, quiet parts around it is a "
             "word a listener hears at once, even if one sound is wrong."),
            ("p",
             "Two limits. The sounds are American, from the dictionary's first "
             "reading of each word, and a British speaker may use a different "
             "vowel in some weak parts. And the table counts the vowel of a "
             "part, not how long or how loud the part is."),
        ],
    },
]
