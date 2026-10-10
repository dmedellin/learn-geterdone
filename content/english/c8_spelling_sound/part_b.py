# -*- coding: utf-8 -*-
"""Course seven, lessons four and five: letters you do not say, and four endings.

Every figure is read off the `letters` lab with `labcheck.js --observe`:
gh 42 of 42, the six one-letter groups 19 of 19, h 77 of 80, ough 5 sounds in
10 words; tion 123 of 127, sion 24 of 25, ture 19 of 20, cial 12 of 12.
The groups named in the prose (35 silent and 7 said as f; the six groups of
silent letters) are counted from the lab's own tables.
"""

LESSONS = [
    {
        "slug": "letters-you-do-not-say",
        "module": "Letters you do not say",
        "title": "Letters You Do Not Say",
        "one_line": "English spells letters it does not say, and three of four groups follow a rule you can count.",
        "standard": (
            "Finish when you can look at a word with a silent letter in it, say which letter is not said, and tell the groups that follow a rule from the one that does not.",
            "You should be able to apply each of three silent-letter rules, "
            "read its score off the table, name the three words where "
            "<em>h</em> is not said, and say how many different sounds "
            "<code>ough</code> has in ten common words.",
        ),
        "summary": (
            "Some letters are written and not said: the <em>k</em> in "
            "<em>know</em>, the <em>b</em> in <em>climb</em>, the <code>gh</code> "
            "in <em>night</em>. A student can take these as a long list of "
            "surprises. Counted on the 2,800 words, most of them follow "
            "rules with no misses, and one group, <code>ough</code>, has no rule "
            "at all."
        ),
        "key_label": "Counted on the 2,800 words",
        "key": [
            "gh after a vowel never says g   42 of 42",
            "knee, write, climb, autumn, walk, calm",
            "one letter silent in each      19 of 19",
            "h is said in                   77 of 80",
            "ough has 5 sounds in 10 words",
        ],
        "concepts_intro": "Three ideas.",
        "concepts": [
            (
                "Silent letters sit in a few fixed places",
                "The silent letter is not anywhere in the word. It is the "
                "<em>k</em> at the start of <code>kn</code>, the <em>w</em> at "
                "the start of <code>wr</code>, the <em>b</em> at the end of "
                "<code>mb</code>, the <em>n</em> at the end of <code>mn</code>, and "
                "the <em>l</em> in <code>alk</code>, <code>olk</code>, <code>alm</code> "
                "and <code>alf</code>. Learn six places and you can find them.",
            ),
            (
                "A loose rule can be right every time",
                "The rule for <code>gh</code> is that, after a vowel letter, it "
                "is never said as <em>g</em>. That is right on all 42 words. "
                "But the rule allows two answers: silent, as in "
                "<em>night</em>, or <em>f</em>, as in <em>enough</em>. A "
                "score of 42 of 42 tells you what <code>gh</code> is not. It "
                "does not tell you which of two sounds it is.",
            ),
            (
                "Some groups have no rule to score",
                "Ten common words have <code>ough</code> in them, and they are said "
                "five ways. No rule can be right about all of them. When a "
                "spelling has no rule, the honest thing is to count the "
                "sounds and learn the words.",
            ),
        ],
        "steps_title": "Reading a word with a letter you may not say",
        "steps_intro": "Four steps.",
        "steps": [
            (
                "Look for the fixed places",
                "Is there a <code>kn</code> or <code>wr</code> at the start, an "
                "<code>mb</code> or <code>mn</code> at the end, or an <em>l</em> after "
                "<em>a</em> or <em>o</em> and before <em>k</em> or "
                "<em>m</em>?",
            ),
            (
                "Drop the letter that sits in a silent place",
                "<em>Knee</em> is said <code>nee</code>. <em>Write</em> begins "
                "with <em>r</em>. <em>Climb</em> ends in <em>m</em>.",
            ),
            (
                "Choose between silent and f",
                "After <em>i</em> it is silent. After <code>ou</code> or "
                "<code>au</code> check the word: it is <em>f</em> in "
                "<em>enough</em>, <em>laugh</em> and <em>tough</em>.",
            ),
            (
                "Say the h unless the word is hour, honest or honor",
                "These three are the only words in the table where an "
                "<em>h</em> at the start is silent.",
            ),
        ],
        "lab": ("english", {
            "mode": "letters",
            "rules": ["gh", "kn_wr_mb", "h", "ough"],
            "panel_title": "Score three silent-letter rules and count ough",
            "panel_intro": (
                "Choose a rule. For the first three, the page checks each "
                "word against the dictionary and prints the score and the "
                "misses. The fourth, <code>ough</code>, has no rule, so the page "
                "counts the different sounds instead. The list spells words "
                "the American way, so <em>honor</em> and <em>neighbor</em> "
                "appear without the <em>u</em>."
            ),
        }),
        "read_title": "Where the rules are exact, and where they are not",
        "read_intro": (
            "Two rules have no misses. One has three. One is a count, not a "
            "rule."
        ),
        "worked": {
            "title": "Twenty-two words and the letter each one drops",
            "intro": [
                "Each line shows a group and its words. The first letter or "
                "pair of letters is the one that is not said.",
            ],
            "lines": [
                "kn   knee, know, knife, knock, knowledge",
                "wr   wrap, write, writer, wrong",
                "mb   bomb, climb       mn   autumn, column, damn",
                "lk   walk, talk, folk  lm   calm, half",
                "h    hour, honest, honor",
            ],
            "after": [
                "These are the 19 words of the second rule, and in every one "
                "the dictionary gives no sound for the letter. The last "
                "line is the three words where the <em>h</em> is not said, "
                "set against 77 words where it is, such as <em>have</em>, "
                "<em>hair</em>, <em>hand</em> and <em>happy</em>.",
            ],
        },
        "note": (
            "Three of these rules have a score of 100.0% or close to it, and "
            "that is because each has a clear place to look. The loose rule, "
            "for <code>gh</code>, and the rule with no score, for <code>ough</code>, "
            "are the two where you must still learn words, and the <em>h</em> "
            "rule leaves you three."
        ),
        "mistakes": [
            (
                "Believing English has no rules for silent letters",
                "On the list, <code>gh</code> after a vowel is never said as "
                "<em>g</em>, in 42 of 42 words. The letters <code>kn</code>, "
                "<code>wr</code>, <code>mb</code>, <code>mn</code>, <code>lk</code> and "
                "<code>lm</code> each drop one letter in all 19 of theirs.",
            ),
            (
                "Reading a perfect score as a full rule",
                "The <code>gh</code> rule is right 42 times in 42, but it does "
                "not say whether to say <em>f</em> or nothing. Seven words "
                "say <em>f</em>: <em>cough</em>, <em>enough</em>, "
                "<em>laugh</em>, <em>laughter</em>, <em>rough</em>, "
                "<em>roughly</em> and <em>tough</em>. The other 35 are "
                "silent.",
            ),
            (
                "Saying the last group one way",
                "The ten words in the list with <code>ough</code> in them are said "
                "five ways. <em>Though</em> and <em>although</em> end in "
                "<code>oh</code>, <em>through</em> and <em>throughout</em> in "
                "<code>oo</code>, and <em>cough</em> and <em>ought</em> are two "
                "more sounds again.",
            ),
        ],
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "Which letter is not said in <em>climb</em>?",
                "a": ["c", "l", "m", "b"],
                "c": 3,
                "why": (
                    "The <em>b</em> after <em>m</em> at the end of a word is "
                    "not said. <em>Bomb</em> is the same. Both words are in "
                    "the group of 19 where one letter is dropped."
                ),
            },
            {
                "q": "The <code>gh</code> rule is right on 42 of 42 words. What "
                     "does it tell you about <em>enough</em>?",
                "a": [
                    "<code>gh</code> is silent in it",
                    "<code>gh</code> is not said as <em>g</em> in it, and nothing "
                    "more",
                    "<code>gh</code> is said as <em>f</em> in it",
                    "It is an exception to the rule",
                ],
                "c": 1,
                "why": (
                    "The rule says only that <code>gh</code> is never <em>g</em>. "
                    "<em>Enough</em> follows it, since it is said with "
                    "<em>f</em>, but the rule does not say so. It is not an "
                    "exception."
                ),
            },
            {
                "q": "Which of these words has an <em>h</em> that is not said?",
                "a": ["hour", "have", "hand", "happy"],
                "c": 0,
                "why": (
                    "<em>Hour</em> is one of three: <em>hour</em>, "
                    "<em>honest</em> and <em>honor</em>. In the other 77 words "
                    "of the table the <em>h</em> is said."
                ),
            },
            {
                "q": "How many different sounds do the ten <code>ough</code> words "
                     "have?",
                "a": ["Two", "Three", "Five", "Seven"],
                "c": 2,
                "why": (
                    "The table finds five: the ends of <em>though</em>, "
                    "<em>cough</em>, <em>tough</em>, <em>ought</em> and "
                    "<em>through</em>. With no rule that covers them, you "
                    "learn them as a list."
                ),
            },
        ],
        "body": [
            ("p",
             "Say <em>knee</em>. You do not say the <em>k</em>. Say "
             "<em>write</em>, and you do not say the <em>w</em>. English is "
             "known for letters of this kind, and a student often takes them "
             "as one more thing to remember word by word."),
            ("p",
             "The table asks a plainer question. For each group of silent "
             "letters, how many of the words in the list follow the rule?"),
            ("h3", "Never g: 42 words"),
            ("p",
             "Take every word with a <dfn>vowel</dfn> letter followed by "
             "<code>gh</code>. There are 42 of them. The rule is that <code>gh</code> "
             "is not said as <em>g</em>, and the rule is right on all 42, "
             "which is 100.0%."),
            ("p",
             "Read the rows and two groups appear. In 35 words <code>gh</code> "
             "is silent: <em>night</em>, <em>right</em>, <em>high</em>, "
             "<em>daughter</em>, <em>eight</em>, <em>through</em>. In seven it "
             "is said as <em>f</em>: <em>cough</em>, <em>enough</em>, "
             "<em>laugh</em>, <em>laughter</em>, <em>rough</em>, "
             "<em>roughly</em> and <em>tough</em>. Every word with "
             "<code>igh</code> in it is in the first group."),
            ("p",
             "So a perfect score hides a choice. The rule keeps you from "
             "saying <em>g</em> and does not help you choose between nothing "
             "and <em>f</em>. All seven <em>f</em> words have <code>ough</code> "
             "or <code>augh</code>, but so do <em>though</em>, <em>through</em> "
             "and <em>daughter</em>, where the <code>gh</code> is silent, so the "
             "letters alone do not decide."),
            ("h3", "One letter drops out of six groups"),
            ("p",
             "The second rule covers six places. <em>Kn</em> at the start of "
             "a word is said as <em>n</em>, with five words: <em>knee</em>, "
             "<em>know</em>, <em>knife</em>, <em>knock</em> and "
             "<em>knowledge</em>. <em>Wr</em> is said as <em>r</em>, with "
             "four: <em>wrap</em>, <em>write</em>, <em>writer</em> and "
             "<em>wrong</em>. At the end of a word, <code>mb</code> drops the "
             "<em>b</em> in <em>bomb</em> and <em>climb</em>, and <code>mn</code> "
             "drops the <em>n</em> in <em>autumn</em>, <em>column</em> and "
             "<em>damn</em>. The <em>l</em> is silent in <em>folk</em>, "
             "<em>talk</em> and <em>walk</em>, and in <em>calm</em> and "
             "<em>half</em>."),
            ("p",
             "That is 19 words, and the rule is right on all 19. Most of these "
             "letters were said once, long ago, and the spelling kept them "
             "after the speech lost them. You do not need the history. You "
             "need the six places."),
            ("h3", "The letter h: said, except in three words"),
            ("p",
             "The third rule is that an <em>h</em> at the start of a word, "
             "before a vowel letter, is said. On 80 words it is right 77 "
             "times, which is 96.3%. The three misses are <em>honest</em>, "
             "<em>honor</em> and <em>hour</em>. They are three words to "
             "learn, and the other 77 need no note. Outside the list, "
             "<em>heir</em> drops its <em>h</em> in the same way, and in "
             "American speech so does <em>herb</em>."),
            ("h3", "Ten words, five sounds"),
            ("p",
             "The last group has no rule to score. Ten words in the list "
             "contain <code>ough</code>, and the <dfn>dictionary</dfn>, a book that records how words are said, gives five different "
             "sounds. <em>Though</em> and <em>although</em> end with "
             "<code>oh</code>. <em>Through</em> and <em>throughout</em> end with "
             "<code>oo</code>. <em>Enough</em>, <em>rough</em>, <em>roughly</em> "
             "and <em>tough</em> share one sound. <em>Cough</em> has its own, "
             "and so does <em>ought</em>."),
            ("p",
             "A fair score here would be low, and no rule would help. The "
             "table counts the sounds and prints each word beside its sound "
             "instead. That is the honest form of the answer."),
        ],
    },
    {
        "slug": "tion-sion-and-ture",
        "module": "Endings said one way",
        "title": "-tion, -sion and -ture",
        "one_line": "Three endings said one way in nearly every word, and one said two ways by the letter before it. Six words break a rule.",
        "standard": (
            "Finish when you can say a word that ends in one of four common endings from its spelling, and name the words that break the rule.",
            "You should be able to say each ending, choose between the two "
            "sounds of <code>sion</code> by the letter before it, read the score "
            "of each rule off the table, and name the misses.",
        ),
        "summary": (
            "A word that ends in <code>tion</code> is said with <code>shun</code>, "
            "a word that ends in <code>ture</code> is said with <code>chur</code>, "
            "and a word that ends in <code>cial</code> or <code>tial</code> is said "
            "with <code>shul</code>. <em>Sion</em> has two sounds, and the "
            "letter before it chooses. Each rule is right on 95% or more "
            "of the words it can be tried on, and the misses are few "
            "enough to name."
        ),
        "key_label": "Counted on the 2,800 words",
        "key": [
            "tion says shun           123 of 127",
            "sion says zhun or shun    24 of 25",
            "ture says chur            19 of 20",
            "cial and tial say shul    12 of 12",
            "",
            "nation, vision, picture, special",
        ],
        "concepts_intro": "Three ideas.",
        "concepts": [
            (
                "The letters of the ending are not the sounds",
                "The ending <code>tion</code> has four letters and is said as "
                "<code>sh</code> followed by a weak <code>un</code>. No "
                "<em>t</em> is said. A student who reads the letters one by "
                "one will say <em>nation</em> in the wrong way. A student who "
                "learns the ending as a whole will say it in the right way.",
            ),
            (
                "Sion has two sounds, and the letter before it chooses",
                "After a <dfn>vowel</dfn> letter, <code>sion</code> is said "
                "<code>zhun</code>, as in <em>vision</em>. After a "
                "<dfn>consonant</dfn> it is said <code>shun</code>, as in "
                "<em>tension</em>. The rule is a single glance at the letter "
                "before the ending.",
            ),
            (
                "Few misses is not the same as no misses",
                "The rules here are right 95.0% to 100.0% of the time. The "
                "misses are real words you will say, and each one has a "
                "reason that fits in a sentence. Learn the reasons and the "
                "rules are close to complete.",
            ),
        ],
        "steps_title": "Saying a word with one of these endings",
        "steps_intro": "Four steps.",
        "steps": [
            (
                "Find the ending",
                "Look at the last four or five letters: <code>tion</code>, "
                "<code>sion</code>, <code>ture</code>, <code>cial</code> or "
                "<code>tial</code>.",
            ),
            (
                "Use the fixed sound for three of the endings",
                "<em>Tion</em> is <code>shun</code>, <code>ture</code> is "
                "<code>chur</code>, and <code>cial</code> and <code>tial</code> are "
                "<code>shul</code>.",
            ),
            (
                "For the fourth ending, look at the letter before it",
                "A vowel letter gives <code>zhun</code>. A consonant gives "
                "<code>shun</code>.",
            ),
            (
                "Then check the short list of words that break a rule",
                "<em>Question</em>, <em>suggestion</em>, <em>equation</em>, "
                "<em>intention</em>, <em>version</em> and <em>mature</em> "
                "are the six.",
            ),
        ],
        "lab": ("english", {
            "mode": "letters",
            "rules": ["tion", "sion", "ture", "cial"],
            "panel_title": "Score four endings",
            "panel_intro": (
                "Choose an ending. The page runs the rule on every word of "
                "the list that has the ending and checks it against the "
                "first way the dictionary says the word. The dictionary is "
                "American. The setting called <em>every word scored</em> "
                "prints the words the rule gets right as well as the ones "
                "it gets wrong."
            ),
        }),
        "read_title": "The six words that break a rule",
        "read_intro": (
            "There are four misses for <code>tion</code>, one for "
            "<code>sion</code>, one for <code>ture</code> and none for the last "
            "rule."
        ),
        "worked": {
            "title": "Nine words, four endings",
            "intro": [
                "Read each word out loud, then check the ending against the "
                "rule.",
            ],
            "lines": [
                "nation, station        tion: shun",
                "decision, vision       sion after a vowel: zhun",
                "tension                sion after a consonant: shun",
                "nature, picture        ture: chur",
                "social, special        cial: shul",
            ],
            "after": [
                "Every word here follows its rule. The misses are in the "
                "table: <em>question</em> and <em>suggestion</em> are said "
                "with the sound at the start of <em>church</em>, and "
                "<em>equation</em> with <code>zhun</code>. <em>Version</em> is "
                "said with <code>zhun</code> where the rule expects <code>shun</code>, "
                "and <em>mature</em> ends in a different sound from "
                "<code>chur</code>.",
            ],
        },
        "note": (
            "Two of the four misses for <code>tion</code>, <em>question</em> and "
            "<em>suggestion</em>, have an <em>s</em> in front of the ending. "
            "After <em>s</em>, <code>tion</code> is said <code>chun</code>, and "
            "<em>digestion</em>, outside the list, does the same. "
            "That is the lesson of the earlier pages again: sort the misses, "
            "and a reason appears."
        ),
        "mistakes": [
            (
                "Saying the longest ending as it is spelt",
                "The ending is not <em>t</em>, <em>i</em>, <em>on</em>. It "
                "is <code>shun</code>, in 123 of 127 words. Of the four others, "
                "<em>question</em>, <em>suggestion</em> and "
                "<em>intention</em> are given with the sound at the start of "
                "<em>church</em> by the dictionary, and <em>equation</em> "
                "with <code>zhun</code>.",
            ),
            (
                "Using one sound for the fourth ending",
                "<em>Vision</em> and <em>tension</em> look the same and end "
                "differently. The letter before <code>sion</code> chooses, and "
                "the rule is right on 24 of 25 words.",
            ),
            (
                "Thinking a miss means the rule is wrong",
                "<em>Version</em> and <em>mature</em> are one miss each, "
                "in lists of 25 and 20. A rule that is right 96.0% or 95.0% "
                "of the time is worth keeping, with the word beside it.",
            ),
        ],
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "How is the ending of <em>nation</em> said?",
                "a": [
                    "With <em>t</em>, then <code>ee</code>, then <em>on</em>",
                    "With <code>zhun</code>",
                    "With <code>shun</code>",
                    "With <em>chun</em>",
                ],
                "c": 2,
                "why": (
                    "<em>Tion</em> is said <code>shun</code> in 123 of 127 words. "
                    "No <em>t</em> is said. <em>Zhun</em> belongs to a "
                    "different ending, and <em>chun</em> to a few misses."
                ),
            },
            {
                "q": "Why is <em>vision</em> said with <code>zhun</code> and "
                     "<em>tension</em> with <code>shun</code>?",
                "a": [
                    "The letter before <code>sion</code> is a vowel in "
                    "<em>vision</em> and a consonant in <em>tension</em>",
                    "<em>Vision</em> is a noun and <em>tension</em> is not",
                    "<em>Tension</em> is from another language",
                    "The first has the stronger part earlier in the word",
                ],
                "c": 0,
                "why": (
                    "The letter before <code>sion</code> chooses: <em>i</em> in "
                    "<em>vision</em>, <em>n</em> in <em>tension</em>. Both "
                    "words are nouns, so the second answer fails."
                ),
            },
            {
                "q": "Which word ends in a sound that the <code>ture</code> rule "
                     "does not predict?",
                "a": ["picture", "nature", "future", "mature"],
                "c": 3,
                "why": (
                    "<em>Mature</em> is the one miss in 20 words. The "
                    "dictionary gives it a different ending from the "
                    "<code>chur</code> in <em>picture</em>, <em>nature</em> and "
                    "<em>future</em>."
                ),
            },
            {
                "q": "The <code>cial</code> and <code>tial</code> rule is right on "
                     "12 of 12 words. What can you say?",
                "a": [
                    "The rule is true of English words in general",
                    "The rule is right on every one of these 12 words",
                    "The rule needs a list of misses",
                    "The rule has been tested on all English words",
                ],
                "c": 1,
                "why": (
                    "The count covers 12 words from a list of 2,800. It says "
                    "the rule held on every one of them, and nothing about "
                    "words outside the list."
                ),
            },
        ],
        "body": [
            ("p",
             "Many words in English end in the same few groups of letters, "
             "and each group is said one way. A student who knows the four "
             "in this lesson can say hundreds of words."),
            ("p",
             "The table scores each ending on the words in the list that "
             "have it, and prints the words it gets wrong."),
            ("h3", "The longest group: 127 words"),
            ("p",
             "There are 127 words in the list that end in <code>tion</code>. "
             "The rule says <code>shun</code>, and it is right on 123 of them, "
             "which is 96.9%. <em>Nation</em>, <em>station</em>, "
             "<em>action</em> and <em>attention</em> are among them."),
            ("p",
             "The four that do not follow it are <em>equation</em>, "
             "<em>intention</em>, <em>question</em> and <em>suggestion</em>. "
             "<em>Question</em> and <em>suggestion</em> have an <em>s</em> "
             "before the <em>t</em>, and the <dfn>dictionary</dfn>, a book that records how words are said, gives them the sound "
             "at the start of <em>church</em>. <em>Equation</em> has "
             "<code>zhun</code>. For <em>intention</em> the dictionary's first "
             "entry has the same <em>church</em> sound, and you may say it "
             "another way. Trust your ear for that one: the table reports "
             "what the dictionary says."),
            ("h3", "Two sounds in 25 words"),
            ("p",
             "The 25 words ending in <code>sion</code> split in two. After a "
             "vowel letter the ending is <code>zhun</code>: <em>conclusion</em>, "
             "<em>confusion</em>, <em>decision</em>, <em>division</em>, "
             "<em>occasion</em>, <em>provision</em>, <em>television</em> "
             "and <em>vision</em>. After a consonant it is <code>shun</code>, as "
             "in <em>tension</em>, <em>mission</em>, <em>session</em> and "
             "<em>permission</em>."),
            ("p",
             "That rule is right on 24 of 25, which is 96.0%. The one miss "
             "is <em>version</em>, which has an <em>r</em> before the "
             "ending and is said with <code>zhun</code>. American speech does "
             "the same after <em>r</em> in <em>conversion</em>, outside the "
             "list, and British speech says <code>shun</code> in both. The rule is one glance "
             "at the letter before the ending, and you learn one word."),
            ("h3", "Twenty words, one miss"),
            ("p",
             "The 20 words that end in <code>ture</code> are said with "
             "<code>chur</code>, apart from one. That gives 19 of 20, which is "
             "95.0%. <em>Nature</em>, <em>picture</em>, <em>future</em>, "
             "<em>culture</em> and <em>temperature</em> follow it. "
             "<em>Mature</em> does not. Its last part is the strong one, said "
             "harder than the rest, so its vowel keeps a full sound and the "
             "table prints the ending as <code>choor</code>. In the other 19 "
             "the ending is weak. The next course, Word Stress, is about "
             "which part is strong."),
            ("h3", "Twelve words, no misses"),
            ("p",
             "Twelve words end in <code>cial</code> or <code>tial</code>, among them "
             "<em>social</em>, <em>special</em>, <em>official</em>, "
             "<em>essential</em> and <em>potential</em>. All twelve are said "
             "with <code>shul</code>, so the score is 12 of 12, or 100.0%. "
             "Three of the eight words set aside in the first lesson, "
             "<em>financial</em>, <em>official</em> and <em>racial</em>, "
             "are in this list, and the <em>c</em> in each is said as "
             "<code>sh</code>."),
            ("h3", "What the four rules share"),
            ("p",
             "None of these endings is said the way its letters read. Each "
             "is said as a unit, and the unit is the same in every word. That "
             "is a smaller problem than it looks: you learn four sounds, "
             "name six words that break a rule, and you can say a long list "
             "of words you have never heard."),
        ],
    },
]
