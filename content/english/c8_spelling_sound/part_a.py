# -*- coding: utf-8 -*-
"""Course seven, lessons one to three: c and g, the silent e, i before e.

Every figure is read off the `letters` lab with `labcheck.js --observe`:
soft c 348 of 348 and soft g 177 of 187; the silent e 131 of 140 and the
r case 1 of 19; i before e 36 of 58 and, where the letters say ee, 14 of 18.
The words named in the prose are the words in the lab's own tables.
"""

LESSONS = [
    {
        "slug": "c-and-g-before-e-i-and-y",
        "module": "A letter and its sound",
        "title": "C and G Before E, I and Y",
        "one_line": "One of these two rules is right every time it can be tried. The other fails on ten common words.",
        "standard": (
            "Finish when you can say, before you look it up, how a word with c or g in it is said, and name the ten words that break the g rule.",
            "You should be able to read the letter after a <em>c</em> or a "
            "<em>g</em>, choose the sound, read the score of each rule off the "
            "table, say which words were left out of the score and why, and "
            "say the ten words where <em>g</em> keeps its hard sound.",
        ),
        "summary": (
            "The letters <em>c</em> and <em>g</em> each have two sounds, and the "
            "letter after them chooses. Before <em>e</em>, <em>i</em> or "
            "<em>y</em>, <em>c</em> is said as <em>s</em> and <em>g</em> as the "
            "sound at the start of <em>judge</em>. Anywhere else, <em>c</em> is "
            "<em>k</em> and <em>g</em> is the hard sound in <em>go</em>. The "
            "table scores both rules. One is perfect and one is not."
        ),
        "key_label": "Counted on the 2,800 words",
        "key": [
            "c before e, i, y says s    348 of 348",
            "g before e, i, y says j    177 of 187",
            "",
            "city, cell, policy     cat, cold, cup",
            "gentle, giant, energy  get, give, girl",
        ],
        "concepts_intro": "Three ideas. The third is the one a student needs most.",
        "concepts": [
            (
                "The next letter chooses the sound",
                "A <em>c</em> or a <em>g</em> followed by <em>e</em>, <em>i</em> "
                "or <em>y</em> takes its soft sound: <em>s</em> for <em>c</em>, "
                "and <em>j</em> for <em>g</em>. Followed by anything else, "
                "including <em>a</em>, <em>o</em>, <em>u</em> and a "
                "<dfn>consonant</dfn>, a letter that is not <em>a</em>, "
                "<em>e</em>, <em>i</em>, <em>o</em> or <em>u</em>, it takes its "
                "hard sound. You read one letter and you have the answer.",
            ),
            (
                "A score counts only the words the rule can be tried on",
                "Many words have a <em>c</em> or a <em>g</em> that is not "
                "a test of this rule. In <em>chair</em> and <em>back</em> the "
                "<em>c</em> is part of a pair of letters. In <em>sign</em> the "
                "<em>g</em> is not said. In <em>science</em> the <em>c</em> "
                "sits beside an <em>s</em> that could be the source of the "
                "sound. The table leaves these out and lists them with the "
                "reason, so the score is about the rule and not about "
                "other things.",
            ),
            (
                "The two rules are not equally good",
                "Soft <em>c</em> is right on all 348 words it can be tried on. "
                "Soft <em>g</em> is right on 177 of 187. The ten misses are "
                "short, common words, and they are the same kind of word every "
                "time, so you can learn them as one list.",
            ),
        ],
        "steps_title": "Saying a word with a c or a g in it",
        "steps_intro": "Four steps, in this order.",
        "steps": [
            (
                "Find the letter after the c or the g",
                "Look only at that one letter. If the <em>c</em> or the "
                "<em>g</em> is the last letter, there is nothing after it and "
                "the hard sound is the answer.",
            ),
            (
                "If it is e, i or y, use the soft sound",
                "<em>City</em> and <em>cell</em> begin with <em>s</em>. "
                "<em>Gentle</em> and <em>giant</em> begin with the sound at the "
                "start of <em>judge</em>.",
            ),
            (
                "If it is anything else, use the hard sound",
                "<em>Cat</em>, <em>cold</em> and <em>cup</em> begin with "
                "<em>k</em>. <em>Go</em> and <em>good</em> begin with the "
                "hard <em>g</em>.",
            ),
            (
                "For g, check the short list of words that break it",
                "<em>Get</em>, <em>give</em>, <em>girl</em> and seven more keep "
                "the hard sound before <em>e</em> or <em>i</em>. There is no "
                "such list for <em>c</em>.",
            ),
        ],
        "lab": ("english", {
            "mode": "letters",
            "rules": ["softc", "softg"],
            "panel_title": "Score both rules, then read the misses",
            "panel_intro": (
                "Choose a rule. The page reads the letter after the <em>c</em> "
                "or the <em>g</em> in each word of the list, says what the rule "
                "predicts, and checks it against the first way a dictionary says "
                "the word. The dictionary is American. The setting called "
                "<em>every word scored</em> shows the right answers too, and "
                "the setting called <em>the words set aside</em> shows what was "
                "left out and why."
            ),
        }),
        "read_title": "The ten words where g keeps its hard sound",
        "read_intro": (
            "The table scored 187 words for the <em>g</em> rule, and ten of "
            "them break it."
        ),
        "worked": {
            "title": "Three groups from one rule",
            "intro": [
                "Each line reads the letter after the <em>c</em> or the "
                "<em>g</em> and gives the sound. The last line is the one "
                "that fails.",
            ],
            "lines": [
                "city, cell        c before i, e: said s",
                "cat, cold, cup    c before a, o, u: said k",
                "gentle, giant     g before e, i: said j",
                "get, give, girl   g before e, i: said g, a miss",
            ],
            "after": [
                "<em>Get</em> is one of the first words a student meets, and "
                "it breaks the rule. So do <em>give</em>, <em>girl</em>, "
                "<em>gift</em>, <em>begin</em>, <em>forget</em>, "
                "<em>gear</em>, <em>target</em>, <em>together</em> and "
                "<em>altogether</em>. In all ten, the <em>g</em> comes before "
                "<em>e</em> or <em>i</em> and is said hard. Nothing goes wrong "
                "the other way: on the 187 words, a <em>g</em> followed by "
                "anything else is never said as <em>j</em>.",
            ],
        },
        "note": (
            "A perfect score and a score of 94.7% look close. They are not the "
            "same kind of rule. With <em>c</em> you apply the rule and stop. "
            "With <em>g</em> you apply the rule and then ask whether the word "
            "is one of ten."
        ),
        "mistakes": [
            (
                "Thinking the two rules are equally good",
                "They look the same, and they are taught together, so a student "
                "expects them to work the same way. Soft <em>c</em> is right 348 times "
                "in 348. Soft <em>g</em> is right 177 times in 187, and the ten "
                "misses include <em>get</em>, <em>give</em> and <em>girl</em>.",
            ),
            (
                "Scoring every word that has a c or a g in it",
                "In <em>back</em> and <em>chair</em> the letter is part of a "
                "pair, and in <em>sign</em> it is not said. Those words do not "
                "test the rule. The table sets 400 words aside for <em>c</em> "
                "and 143 for <em>g</em>, and prints each with its reason.",
            ),
            (
                "Leaving out the y",
                "The rule names three letters, and <em>y</em> counts like "
                "<em>e</em> and <em>i</em>. <em>Cycle</em> begins with "
                "<em>s</em> for that reason; the table does not score it, "
                "since it has two <em>c</em> letters. The words it does score "
                "with a <em>y</em> after the letter, <em>policy</em> and "
                "<em>agency</em> for <em>c</em> and <em>energy</em> and "
                "<em>strategy</em> for <em>g</em>, all follow the rule.",
            ),
        ],
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "How is the <em>c</em> in <em>cell</em> said, and why?",
                "a": [
                    "As <em>k</em>, because it is at the start of the word",
                    "As <em>s</em>, because the next letter is <em>e</em>",
                    "As <em>s</em>, because all words with <em>c</em> start "
                    "with <em>s</em>",
                    "As <em>k</em>, because the next letter is a "
                    "<dfn>vowel</dfn>",
                ],
                "c": 1,
                "why": (
                    "The next letter decides. <em>E</em>, <em>i</em> and "
                    "<em>y</em> give the soft sound, <em>s</em>. A vowel by "
                    "itself is not the test: <em>cat</em> has a vowel after "
                    "the <em>c</em> and is said with <em>k</em>."
                ),
            },
            {
                "q": "Which word breaks the rule for <em>g</em>?",
                "a": ["gentle", "giant", "age", "get"],
                "c": 3,
                "why": (
                    "<em>Get</em> has an <em>e</em> after the <em>g</em>, so "
                    "the rule says <em>j</em>, but it is said with the hard "
                    "<em>g</em>. <em>Gentle</em>, <em>giant</em> and "
                    "<em>age</em> follow the rule."
                ),
            },
            {
                "q": "The <em>c</em> rule is right on 348 of 348 words and the "
                     "<em>g</em> rule on 177 of 187. What follows?",
                "a": [
                    "You can apply the <em>c</em> rule and stop, but for "
                    "<em>g</em> you also check ten words",
                    "The <em>g</em> rule is not worth learning",
                    "Both rules need a list of misses",
                    "Both rules are equally reliable",
                ],
                "c": 0,
                "why": (
                    "A rule with no misses needs no list. A rule that is right "
                    "94.7% of the time is still worth learning, and its ten "
                    "misses are short enough to remember. The third answer is "
                    "wrong because the <em>c</em> rule has no misses at all."
                ),
            },
            {
                "q": "Why does the table leave out <em>back</em> and "
                     "<em>chair</em>?",
                "a": [
                    "They are too easy",
                    "They are not in the dictionary",
                    "Their <em>c</em> belongs to a pair of letters, so they "
                    "do not test the rule",
                    "They break the rule",
                ],
                "c": 2,
                "why": (
                    "In <em>back</em> the <em>c</em> and <em>k</em> work as "
                    "one pair, and in <em>chair</em> the <em>c</em> and "
                    "<em>h</em> do. A score should count only the words that "
                    "can show the rule to be right or wrong."
                ),
            },
        ],
        "body": [
            ("p",
             "Take two letters and ask what sound each makes. For <em>c</em> "
             "the answer is two sounds. It is <em>k</em> in <em>cat</em> and "
             "<em>s</em> in <em>city</em>. For <em>g</em> it is also two: the "
             "hard sound in <em>go</em> and the sound at the start of "
             "<em>gentle</em>."),
            ("p",
             "You have probably been given a rule for this. Before <em>e</em>, "
             "<em>i</em> or <em>y</em>, the letter is soft. Anywhere else it "
             "is hard. The question for this lesson is a plain one: how often "
             "is that right?"),
            ("h3", "What the table counts"),
            ("p",
             "Before the page was built, every word of the 2,800 with a "
             "<em>c</em> or a <em>g</em> in it was picked out, and the way it "
             "is said was read from a <dfn>dictionary</dfn>, a book that records how "
             "the word is said. The page prints those words, runs the rule on "
             "each one, and compares the two. It scores a word only if the <em>c</em> or the <em>g</em> "
             "is the one place the sound could come from. A word with two "
             "<em>c</em> letters is set aside, because one score cannot say "
             "which <em>c</em> made the sound. So is a word where the letter "
             "is part of <code>ch</code>, <code>ck</code>, <code>sc</code>, <code>cc</code>, "
             "<code>cq</code> or <code>qu</code>, and a word where another letter, "
             "<em>s</em>, <em>k</em>, <em>q</em>, <em>x</em> or <em>z</em>, "
             "could make the sound instead."),
            ("p",
             "That leaves 348 words with a <em>c</em> that tests the rule, "
             "and 400 that were set aside. For <em>g</em> it leaves 187 and "
             "sets 143 aside. Open the setting called <em>the words set "
             "aside</em> and every one of them is there with its reason."),
            ("h3", "The c rule is right every time"),
            ("p",
             "On the 348 words, the rule is right 348 times, which is "
             "100.0%. <em>Center</em>, <em>certain</em>, <em>face</em>, "
             "<em>price</em> and <em>century</em> are said with <em>s</em>. "
             "<em>Call</em>, <em>come</em>, <em>cut</em> and <em>cold</em> "
             "are said with <em>k</em>. There is no miss to read, and that is "
             "a result too: for this list, one letter after the c is all "
             "a student needs."),
            ("p",
             "Eight words were set aside because the dictionary gives them "
             "both sounds or neither. They are <em>ancient</em>, "
             "<em>appreciate</em>, <em>efficient</em>, <em>financial</em>, "
             "<em>ocean</em>, <em>official</em>, <em>politician</em> and "
             "<em>racial</em>. In seven of them the <em>c</em> is said as "
             "<code>sh</code>; for <em>ancient</em> the dictionary's first entry "
             "gives the sound at the start of <em>church</em>. That is a "
             "different rule, and the last lesson of this course takes up the "
             "endings several of them share."),
            ("h3", "The g rule fails on ten words"),
            ("p",
             "On the 187 words for <em>g</em>, the rule is right 177 times, "
             "which is 94.7%. <em>Gentle</em>, <em>giant</em>, <em>age</em>, "
             "<em>large</em> and <em>energy</em> follow it. "
             "The ten that do not are <em>altogether</em>, <em>begin</em>, "
             "<em>forget</em>, <em>give</em>, <em>gear</em>, <em>get</em>, "
             "<em>gift</em>, <em>girl</em>, <em>target</em> and "
             "<em>together</em>."),
            ("p",
             "Read them again. In every one, the <em>g</em> sits before "
             "<em>e</em> or <em>i</em> and is said hard. That is why this "
             "list is worth knowing: all ten are common words, and you will "
             "use them every day."),
            ("h3", "What the score does not say"),
            ("p",
             "The dictionary is American and the table reads only its first "
             "entry. A word that has two ways to be said is scored on the "
             "first. Nine words were set aside for <em>g</em> because the "
             "dictionary gives both sounds or neither, <em>sign</em> and "
             "<em>foreign</em> among them. The rule says what the spelling "
             "suggests, and the dictionary says what people say."),
        ],
    },
    {
        "slug": "the-silent-e-and-the-vowels-name",
        "module": "A letter and its sound",
        "title": "The Silent E and the Vowel's Name",
        "one_line": "A word that ends vowel, consonant, e says its vowel as its name. Nine common words do not.",
        "standard": (
            "Finish when you can read a word of one part that ends in a vowel, a consonant and e, say its vowel as the letter's name, and name the nine common words that break the rule.",
            "You should be able to say what the final <em>e</em> does, read "
            "the score of the rule off the table, sort the nine misses into "
            "three groups, and say why the same rule fails before <em>r</em>.",
        ),
        "summary": (
            "Add an <em>e</em> to the end of <em>hop</em> and you have "
            "<em>hope</em>. The <em>e</em> is not said, but it changes the "
            "word before it: the <em>o</em> now says its own name. The rule "
            "is right on 131 of 140 words. The nine that break it are words "
            "you use every day, and they fall into three groups."
        ),
        "key_label": "Counted on the 2,800 words",
        "key": [
            "vowel, consonant, e: the vowel",
            "says its name       131 of 140",
            "",
            "hop  hope     bit  bite     tub  tube",
            "",
            "before r the rule is right  1 of 19",
        ],
        "concepts_intro": "Three ideas, and the second answers a common worry.",
        "concepts": [
            (
                "The last letter changes the vowel before it",
                "<em>Hop</em> has a short <dfn>vowel</dfn>. <em>Hope</em> has "
                "the same letters and an <em>e</em>, and the <em>o</em> now "
                "says what the letter is called. The <em>e</em> itself is not "
                "said. It marks the word as one with a long vowel.",
            ),
            (
                "The words that break it are common",
                "You might expect a rule's misses to be rare words. These are "
                "not. <em>Have</em>, <em>come</em> and <em>some</em> are among "
                "the commonest words in English, and <em>give</em>, "
                "<em>love</em> and <em>move</em> are not far behind. If you "
                "learn the rule and not the list, you will be wrong on words "
                "you meet every day.",
            ),
            (
                "A letter after the vowel can change the rule",
                "Put an <em>r</em> before the final <em>e</em> and the rule "
                "all but stops working. The <em>a</em> in <em>care</em> does "
                "not say its name. The table scores these words apart so that "
                "they do not hide the result for all the others.",
            ),
        ],
        "steps_title": "Reading a word that ends in e",
        "steps_intro": "Four steps.",
        "steps": [
            (
                "Check the shape",
                "The word must have one part, and its end must be a vowel, "
                "a consonant and a final <em>e</em>, as in <em>make</em>. "
                "The consonant is not <em>w</em>, <em>x</em>, <em>y</em> or "
                "<em>r</em>.",
            ),
            (
                "Say the vowel as the letter's name",
                "<em>A</em> says <code>ay</code>, <em>i</em> says the word "
                "<em>eye</em>, <em>o</em> says <code>oh</code> and <em>u</em> says "
                "<code>oo</code> or <em>you</em>. For <em>e</em> it says "
                "<code>ee</code>.",
            ),
            (
                "Do not say the final e",
                "<em>Make</em> has one sound after the <em>m</em> and it is "
                "<code>ay</code> and then <em>k</em>. The last letter is only a "
                "mark.",
            ),
            (
                "Then check the nine",
                "If the word is <em>have</em>, <em>give</em>, <em>come</em>, "
                "<em>some</em>, <em>love</em>, <em>none</em>, <em>lose</em>, "
                "<em>move</em> or <em>prove</em>, the rule does not apply.",
            ),
        ],
        "lab": ("english", {
            "mode": "letters",
            "rules": ["magic", "magic_r"],
            "panel_title": "Score the silent e, with and without r",
            "panel_intro": (
                "Choose a rule. The first setting scores every word of one part "
                "of the list that ends in a vowel, a consonant and an "
                "<em>e</em>. The second scores the words that have an "
                "<em>r</em> before the <em>e</em>, apart from the rest. Each "
                "row says what the rule predicts and what the dictionary "
                "gives. The dictionary is American, and it is read at its "
                "first entry."
            ),
        }),
        "read_title": "The nine words that break it",
        "read_intro": (
            "Of 140 words, nine are said some other way. They are not nine "
            "separate facts."
        ),
        "worked": {
            "title": "Nine misses in three groups",
            "intro": [
                "Here are the nine, sorted by what the vowel does instead.",
            ],
            "lines": [
                "short vowel      have, give",
                "u as in cup      come, some, love, none",
                "oo               lose, move, prove",
            ],
            "after": [
                "The first group has a reason you can use. English spelling "
                "almost never ends a word in <em>v</em>, so the <em>e</em> in "
                "<em>have</em> and <em>give</em> is there because of the "
                "<em>v</em>, and not to change the vowel. The second group "
                "says one sound, the vowel in <em>cup</em>, though the "
                "spelling has an <em>o</em>. The third group has the sound "
                "<code>oo</code>, though <em>o</em> would say <code>oh</code>. "
                "Four words have no simple reason, and that is honest: you "
                "learn <em>come</em>, <em>some</em>, <em>love</em> and "
                "<em>none</em> as a short list.",
            ],
        },
        "note": (
            "Seven of the nine have an <em>o</em> as the vowel. Reading the "
            "misses in groups gives you more than a list: it tells you "
            "where to be careful, and it shows that the rule fails "
            "most often on one letter."
        ),
        "mistakes": [
            (
                "Thinking the exceptions are rare words",
                "They are <em>have</em>, <em>give</em>, <em>come</em>, "
                "<em>some</em>, <em>love</em>, <em>none</em>, <em>lose</em>, "
                "<em>move</em> and <em>prove</em>. A student meets most of "
                "them in the first week.",
            ),
            (
                "Saying the final e",
                "The <em>e</em> at the end of <em>hope</em> is never said. "
                "It is a sign for the vowel before it. A student who says "
                "<em>hope</em> in two parts has read the sign as a sound.",
            ),
            (
                "Using the rule before r",
                "<em>Care</em>, <em>more</em>, <em>sure</em>, <em>there</em> "
                "and <em>where</em> have the same shape and do not follow the "
                "rule. The table scores 19 words of this kind and the rule is "
                "right once.",
            ),
        ],
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "What does the final <em>e</em> in <em>hope</em> do?",
                "a": [
                    "It is said as a short <code>ee</code> at the end",
                    "It makes the <em>o</em> say its own name",
                    "It makes the word a noun",
                    "It does nothing",
                ],
                "c": 1,
                "why": (
                    "The <em>e</em> is not said, but without it the word is "
                    "<em>hop</em>, with a short vowel. It marks a long "
                    "vowel. That is a job, so the last answer is wrong."
                ),
            },
            {
                "q": "Which of these words breaks the rule?",
                "a": ["make", "time", "hope", "move"],
                "c": 3,
                "why": (
                    "<em>Move</em> is said with the sound <code>oo</code>, not "
                    "<code>oh</code>. <em>Make</em>, <em>time</em> and "
                    "<em>hope</em> are said with the name of their vowel."
                ),
            },
            {
                "q": "Why do <em>have</em> and <em>give</em> end in <em>e</em>?",
                "a": [
                    "English spelling almost never ends a word in <em>v</em>",
                    "The <em>e</em> makes the vowel short",
                    "They come from another language",
                    "The dictionary is wrong",
                ],
                "c": 0,
                "why": (
                    "The final <em>e</em> is there for the <em>v</em>, so the "
                    "word does not end in that letter. It does not make the "
                    "vowel long, which is why these two keep a short vowel."
                ),
            },
            {
                "q": "The rule is right on 131 of 140 words. What does the "
                     "table show about the 9 misses?",
                "a": [
                    "They are rare words you can leave out",
                    "They are all words with an <em>r</em>",
                    "They are common words and they fall into groups",
                    "They are all spelling mistakes in the list",
                ],
                "c": 2,
                "why": (
                    "The nine include <em>have</em>, <em>come</em> and "
                    "<em>some</em>. They sort into three groups by what the "
                    "vowel does. Words with <em>r</em> are scored in a "
                    "different table."
                ),
            },
        ],
        "body": [
            ("p",
             "Say <em>hop</em>, then say <em>hope</em>. The second word has "
             "one more letter, and you do not say it. What changed is the "
             "vowel: in <em>hope</em> the <em>o</em> says its own name."),
            ("p",
             "That is the silent <em>e</em> rule. It is about words of one "
             "<dfn>part</dfn>, said in one beat, as <em>hop</em> is and "
             "<em>hoping</em> is not. Such a word, when it "
             "ends in a vowel, a <dfn>consonant</dfn> and an <em>e</em>, is "
             "said with the vowel's name. <em>Bit</em> becomes <em>bite</em>, "
             "<em>tub</em> becomes <em>tube</em>, <em>mat</em> becomes "
             "<em>mate</em>."),
            ("h3", "What was scored"),
            ("p",
             "The lab takes every word of the list with one part that ends "
             "in a vowel, a consonant and an <em>e</em>. It leaves out words "
             "where the consonant is <em>w</em>, <em>x</em>, <em>y</em> or "
             "<em>r</em>. Then it checks the vowel against a <dfn>dictionary</dfn>, a book that records how words are said. "
             "That gives 140 words."),
            ("p",
             "The rule is right on 131 of them, which is 93.6%. Time, make, "
             "hope, tube, huge and wide are among the words it gets right. "
             "In <em>huge</em> the <em>u</em> says <em>you</em>, which the "
             "table counts as the name of <em>u</em>."),
            ("h3", "The nine that break it"),
            ("p",
             "The misses are <em>come</em>, <em>have</em>, <em>give</em>, "
             "<em>lose</em>, <em>love</em>, <em>move</em>, <em>none</em>, "
             "<em>prove</em> and <em>some</em>. Read the list again. These "
             "are not the words a dictionary notes as odd. They are among the "
             "words a student needs first."),
            ("p",
             "Sort them and three groups appear. <em>Have</em> and "
             "<em>give</em> keep a short vowel. <em>Come</em>, <em>some</em>, "
             "<em>love</em> and <em>none</em> are said with the vowel of "
             "<em>cup</em>. <em>Lose</em>, <em>move</em> and <em>prove</em> "
             "are said with <code>oo</code>. Each group is small enough to say "
             "out loud in a few seconds."),
            ("p",
             "There would be a tenth. The dictionary's first entry for "
             "<em>live</em> is the word in <em>live music</em>, said with the "
             "sound of <em>eye</em>, so the table counts it as right. The "
             "verb <em>live</em>, which you use far more often, has the short "
             "vowel of <em>give</em>. The table reads one entry and says so; "
             "your ear can add the tenth word to the first group."),
            ("h3", "Why have and give are different"),
            ("p",
             "English words almost never end in <em>v</em>. When the last "
             "sound of a word is <em>v</em>, an <em>e</em> is written after it. So the "
             "<em>e</em> in <em>have</em> is not a mark for a long vowel. "
             "It is only there so the word does not end in <em>v</em>. "
             "<em>Save</em> and <em>wave</em> have the same <em>e</em> and "
             "do follow the rule, because there the vowel is also long. The "
             "letters tell you the pattern; the dictionary tells you "
             "which of the two jobs the <em>e</em> is doing."),
            ("h3", "The same shape before r"),
            ("p",
             "Take the words that end in a vowel, <em>r</em> and <em>e</em>. "
             "The rule says the <em>a</em> in <em>care</em> should say its "
             "name, as it does in <em>make</em>, and it does not. The table "
             "scores 19 of these words apart. The rule is right once, for "
             "<em>here</em>, which is 5.3%."),
            ("p",
             "The other 18 sort the same way. Nine, among them <em>care</em>, "
             "<em>rare</em>, <em>share</em>, <em>there</em> and "
             "<em>where</em>, are said with the vowel of <em>bed</em>. Six, "
             "<em>bore</em>, <em>core</em>, <em>more</em>, <em>score</em>, "
             "<em>shore</em> and <em>store</em>, are said with the vowel "
             "of <em>or</em>. Two, <em>pure</em> and <em>sure</em>, have the "
             "vowel of <em>book</em>, and <em>mere</em> has the vowel of "
             "<em>sit</em>. An <em>r</em> changes the vowel before it in "
             "every way you can see here, which is why the table keeps these "
             "words apart."),
        ],
    },
    {
        "slug": "i-before-e-and-its-failure-rate",
        "module": "The famous rule",
        "title": "I Before E, and Its Failure Rate",
        "one_line": "The best known rule of English spelling is right on 36 of 58 common words.",
        "standard": (
            "Finish when you can apply the saying about i before e to a word, say how often it is right, and sort the words where it fails into the groups that cause the failures.",
            "You should be able to find every <code>ie</code> and <code>ei</code> in "
            "a word, predict the spelling from the rule, read the score off the "
            "table, name the three kinds of miss, and explain why the same "
            "rule looks better when it is applied only where the letters say "
            "<code>ee</code>.",
        ),
        "summary": (
            "Most students are given a saying: <em>i before e, except after "
            "c</em>. On the 58 places in the 2,800 words where <em>i</em> and "
            "<em>e</em> sit together, it is right 36 times. That is 62.1%. "
            "The 22 misses are not random, and "
            "narrowing the rule to words said with <code>ee</code> lifts it to 14 "
            "of 18."
        ),
        "key_label": "Counted on the 2,800 words",
        "key": [
            "i before e, except after c",
            "right on 36 of 58       62.1%",
            "",
            "only where the letters say ee",
            "right on 14 of 18       77.8%",
        ],
        "concepts_intro": "Three ideas.",
        "concepts": [
            (
                "A rule is a bet, and this one is a poor bet",
                "The rule is right on 36 of 58 words. That is a little over "
                "six in ten. If you guess the order of the letters with this "
                "rule you will spell about four in ten of these words "
                "wrong. A student who knows this will check the dictionary; "
                "a student who does not will trust the saying.",
            ),
            (
                "The failures come in groups",
                "Of the 22 misses, eight have the letters <code>eigh</code>, "
                "as in <em>eight</em> and <em>weight</em>. Nine are the "
                "letters <code>cie</code>, as in <em>science</em> and "
                "<em>efficient</em>. Five are alone: <em>either</em>, "
                "<em>neither</em>, <em>foreign</em>, <em>protein</em> and "
                "<em>weird</em>. Three groups explain 22 words.",
            ),
            (
                "The saying was made for one sound",
                "The rule is about words said with <code>ee</code>, as in "
                "<em>believe</em> and <em>receive</em>. Where the letters say "
                "something else, the rule has no claim. Apply it only where "
                "the letters say <code>ee</code> and it is right on 14 of 18.",
            ),
        ],
        "steps_title": "Using the rule, and knowing when not to",
        "steps_intro": "Four steps.",
        "steps": [
            (
                "Find the pair",
                "Look for <code>ie</code> or <code>ei</code> in the word. The rule has "
                "nothing to say about a word that has neither.",
            ),
            (
                "Say the sound",
                "If the pair says <code>ee</code>, as in <em>believe</em>, the "
                "rule applies. If it says <code>ay</code>, as in <em>weigh</em>, "
                "the letters are <code>eigh</code> and the rule does not apply.",
            ),
            (
                "Look at the letter before the pair",
                "After a <em>c</em>, write <code>ei</code>. After any other "
                "letter, write <code>ie</code>.",
            ),
            (
                "Learn the nine words with c before ie",
                "<em>Science</em>, <em>efficient</em> and <em>sufficient</em> "
                "break the rule and make up the largest group of misses.",
            ),
        ],
        "lab": ("english", {
            "mode": "letters",
            "rules": ["ie", "ie_ee"],
            "panel_title": "Score the famous rule, then narrow it",
            "panel_intro": (
                "Choose a rule. The first setting runs the rule on every "
                "<code>ie</code> and <code>ei</code> in the list. The second runs it "
                "only where the letters line up one to one with the parts of "
                "the word and the dictionary gives <code>ee</code> at that place. "
                "The page lists what was set aside and why. The dictionary is "
                "American and is read at its first entry."
            ),
        }),
        "read_title": "The 22 words that break it",
        "read_intro": (
            "Read the misses in three groups, and the rule starts to make "
            "sense."
        ),
        "worked": {
            "title": "Friend, receive, weight, science",
            "intro": [
                "Four words, one rule, and four different results.",
            ],
            "lines": [
                "friend, believe   ie, no c before it   right",
                "receive           ei after c           right",
                "weight, eight     ei said ay           miss",
                "science           ie after c           miss",
            ],
            "after": [
                "<em>Friend</em> and <em>believe</em> follow the rule. "
                "<em>Receive</em> is the rule working the other way: after "
                "<em>c</em> it says <code>ei</code>, and <em>perceive</em> does "
                "the same. Those two are the only words in the table where "
                "the rule says <code>ei</code> and is right. <em>Weight</em> "
                "and <em>science</em> break it in different ways, and the "
                "difference is the point of the lesson.",
            ],
        },
        "note": (
            "The saying has two halves, and the second half, <em>except after "
            "c</em>, is the weaker. Of 11 words with a <em>c</em> before the "
            "pair, only two follow it. If you keep the first half and look "
            "up words with <code>cie</code>, you do better than with the whole "
            "saying."
        ),
        "mistakes": [
            (
                "Treating a saying as a rule",
                "It is easy to remember, and that is why it has lasted. It "
                "is right 36 times in 58, which is 62.1%. A rule that fails "
                "nearly four times in ten is not one to trust without "
                "checking.",
            ),
            (
                "Thinking the c clause is the safe part",
                "After <em>c</em> the rule says <code>ei</code>. On the list, "
                "the words with a <em>c</em> before the pair are "
                "<em>receive</em> and <em>perceive</em>, which follow it, "
                "and nine words with <code>cie</code>, which do not.",
            ),
            (
                "Applying it to every pair of these letters",
                "The rule was made for words said with <code>ee</code>. In "
                "<em>weight</em> and <em>height</em> the letters say "
                "something else, and the rule was never about them. Count "
                "only the words said with <code>ee</code> and the score is 14 of "
                "18.",
            ),
        ],
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "On the 58 words in the table, how often is <em>i before "
                     "e, except after c</em> right?",
                "a": [
                    "Every time",
                    "Nine times in ten",
                    "About six times in ten",
                    "Less than half the time",
                ],
                "c": 2,
                "why": (
                    "It is right on 36 of 58 words, which is 62.1%. That is "
                    "about six in ten and more than half, so the last answer "
                    "is wrong."
                ),
            },
            {
                "q": "Which word follows the rule?",
                "a": ["weight", "receive", "science", "foreign"],
                "c": 1,
                "why": (
                    "<em>Receive</em> has <code>ei</code> after a <em>c</em>, "
                    "which is what the rule says. <em>Weight</em> and "
                    "<em>foreign</em> have <code>ei</code> without a <em>c</em>, "
                    "and <em>science</em> has <code>ie</code> after one."
                ),
            },
            {
                "q": "What do <em>eight</em>, <em>weight</em>, <em>weigh</em> "
                     "and <em>neighbor</em> have in common?",
                "a": [
                    "The letters <code>eigh</code>, said as <code>ay</code>",
                    "A <em>c</em> before the pair",
                    "The sound <code>ee</code>",
                    "They are all verbs",
                ],
                "c": 0,
                "why": (
                    "All four have <code>eigh</code>, said as <code>ay</code>. The "
                    "rule is about words said with <code>ee</code>, so this "
                    "group is outside what it claims to cover."
                ),
            },
            {
                "q": "Where the letters say <code>ee</code>, the rule is right on "
                     "14 of 18. Which word is among the 4 misses?",
                "a": ["believe", "achieve", "piece", "either"],
                "c": 3,
                "why": (
                    "<em>Either</em> has <code>ei</code> with no <em>c</em> before "
                    "it, so the rule says <code>ie</code>. The other misses are "
                    "<em>neither</em>, <em>protein</em> and <em>species</em>."
                ),
            },
        ],
        "body": [
            ("p",
             "Here is the most quoted spelling rule in English. <em>I before "
             "e, except after c.</em> Most people who have learned English "
             "have heard it, and many repeat it when they are not sure how "
             "to spell <em>believe</em> or <em>receive</em>."),
            ("p",
             "The lab runs it on every <code>ie</code> and <code>ei</code> in the "
             "2,800 words. There are 58. The rule says <code>ie</code> unless the "
             "letter before the pair is <em>c</em>, and then it says "
             "<code>ei</code>."),
            ("h3", "The score"),
            ("p",
             "The rule is right on 36 of the 58, which is 62.1%. Twenty-two "
             "words break it. In a list of the 2,800 commonest words, that "
             "is a saying that is wrong more often than it is worth."),
            ("p",
             "Those 22 are not spread about at random. Sorted, they make three groups."),
            ("h3", "The three kinds of miss"),
            ("p",
             "The first group is <code>eigh</code>: <em>eight</em>, "
             "<em>eighteen</em>, <em>eighty</em>, <em>weigh</em>, "
             "<em>weight</em>, <em>neighbor</em>, <em>neighborhood</em> and "
             "<em>height</em>. That is eight words. In most of them the "
             "letters say <code>ay</code>, so they are not about <code>ee</code> at "
             "all. <em>Height</em> is said with the sound of the word "
             "<em>eye</em>, which is a different case again."),
            ("p",
             "The second group is <code>cie</code>: <em>ancient</em>, "
             "<em>efficiency</em>, <em>efficient</em>, <em>science</em>, "
             "<em>scientific</em>, <em>scientist</em>, <em>society</em>, "
             "<em>species</em> and <em>sufficient</em>. That is nine words. "
             "They are the part of the saying that fails after <em>c</em>: the "
             "rule says <code>ei</code> there, and every one of them has "
             "<code>ie</code>."),
            ("p",
             "The third group is five words that stand alone: "
             "<em>either</em>, <em>neither</em>, <em>foreign</em>, "
             "<em>protein</em> and <em>weird</em>. Each has <code>ei</code> with "
             "no <em>c</em> before it, and each is said its own way."),
            ("h3", "A better question"),
            ("p",
             "The saying was made to help with words said with <code>ee</code>. "
             "So the lab can ask a second question: how often is the rule "
             "right where the letters line up with the <dfn>parts</dfn> of the word, "
             "the beats it is said in, "
             "and the <dfn>dictionary</dfn>, a book that records how words are said, has <code>ee</code> at that place? That leaves "
             "18 words, and the rule is right on 14, which is 77.8%."),
            ("p",
             "Forty words were set aside. Fourteen do not line up, which "
             "means the letters and the parts of the word cannot be matched "
             "one to one, and 26 are said with something other than "
             "<code>ee</code> at that place. The four misses are "
             "<em>either</em>, <em>neither</em>, <em>protein</em> and "
             "<em>species</em>. The first three have <code>ei</code> with no "
             "<em>c</em>, and the last has <code>ie</code> after a <em>c</em>."),
            ("h3", "What to keep"),
            ("p",
             "Keep the first half of the saying for words said with "
             "<code>ee</code>. Learn <em>either</em>, <em>neither</em> and "
             "<em>protein</em> as three words. Learn that after <em>c</em> the "
             "saying is right only where the pair says <code>ee</code>, as in "
             "<em>receive</em>; in the nine <code>cie</code> words the "
             "<em>i</em> and the <em>e</em> are said apart, as in "
             "<em>science</em>, or the <em>c</em> is part of a <code>sh</code> "
             "sound, as in <em>efficient</em>. "
             "Learn that <code>eigh</code> is a group of its own. With those four "
             "facts, you have a better rule than the saying."),
        ],
    },
]
