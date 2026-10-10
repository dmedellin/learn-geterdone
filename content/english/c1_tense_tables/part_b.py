# -*- coding: utf-8 -*-
"""Lesson three: the doubling rule, and the part of it most books leave out.

Every figure here is read off the doubling lab's `The rule to score` menu
with `labcheck.js --observe`: 199 / 107 / 110 of 217, 18 wrong, 11 of them
ending in -l. The eighteen are named from the lab's own `wrong` table, and
the three words the raw NGSL made look like exceptions (offer, suffer,
council) are named as what they were: misspellings and a non-verb.
"""

LESSONS = [
    {
        "slug": "when-the-last-letter-doubles",
        "module": "The rule that needs the sound",
        "title": "When the Last Letter Doubles",
        "one_line": "Most books give you half this rule, and half of it is only a guess.",
        "standard": (
            "Finish when you can say, before writing it, whether a verb doubles "
            "its last letter, and why.",
            "You should be able to pick out the verbs the rule can touch at all, "
            "apply the strong-part question to each, score the rule against a printed "
            "list, name the group of words it still gets wrong and what they "
            "have in common, and tell a spelling the list has both ways from a "
            "true exception.",
        ),
        "summary": (
            "You have probably been told that a verb ending consonant, vowel, "
            "consonant doubles its last letter: <em>stop</em> becomes "
            "<em>stopping</em>. On the 217 verbs where that rule can apply, it is "
            "right about half the time. The missing half of the rule is where the "
            "strong part of the word falls, and adding it takes the same rule from "
            "about 50% to about 92%."
        ),
        "key_label": "The same 217 verbs, three rules",
        "key": [
            "double every one            107 / 217   49.3%",
            "double none of them         110 / 217   50.7%",
            "double if last part strong  199 / 217   91.7%",
            "",
            "of the 18 still wrong, 11 end in -l",
        ],
        "concepts_intro": "Three ideas, and the third is the one worth keeping.",
        "concepts": [
            (
                "The rule can only touch some verbs",
                "Doubling is only ever a question for a verb ending consonant, "
                "vowel, consonant &mdash; <em>stop</em>, <em>admit</em>, "
                "<em>travel</em>. There are 217 of those in the word list, and "
                "no other verb is affected. The last lesson scored the "
                "<em>-ing</em> rule, doubling and all, on 1,210 regular verbs and "
                "it was right 99.34% of the time. That number hides how often the "
                "doubling part fails, because most verbs never ask the question.",
            ),
            (
                "Half a rule is only a guess",
                "Of those 217, 107 double and 110 do not. So “double them "
                "all” is right 49.3% of the time and “double none” "
                "is right 50.7%. A rule that does no better than guessing is not "
                "a rule, and this is the form most books print.",
            ),
            (
                "The missing half is where the strong part falls",
                "<em>Stop</em> has one part, so the last part is the strong one, "
                "and it doubles. <em>Travel</em> has two and the strong one is the "
                "first, so it does not. Adding that test takes the same rule to "
                "199 of 217, which is 91.7%.",
            ),
        ],
        "steps_title": "Deciding, for a verb in front of you",
        "steps_intro": "Four questions, in this order.",
        "steps": [
            (
                "Does it end consonant, vowel, consonant?",
                "If not, stop: the rule has nothing to say, and you simply add the "
                "ending. A last letter of <em>w</em>, <em>x</em> or <em>y</em> "
                "counts as a no.",
            ),
            (
                "Say the word out loud",
                "Listen for which part you say harder. In <em>admit</em> it is the "
                "second; in <em>travel</em> it is the first.",
            ),
            (
                "If the strong part is the last one, double the letter",
                "<em>admit</em> becomes <em>admitting</em>. If it is not, leave it "
                "alone: <em>travelling</em> is British and <em>traveling</em> is "
                "American, and the rule here gives you the second.",
            ),
            (
                "Check the short list of words that break it",
                "There are 18, and 11 of them end in <em>-l</em>. Learn that one "
                "group and the rule is almost perfect.",
            ),
        ],
        "lab": ("english", {
            "mode": "doubling",
            "panel_title": "Score the rule yourself, three ways",
            "panel_intro": (
                "These are every verb in the word list ending consonant, vowel, "
                "consonant &mdash; the only verbs the doubling rule can touch. "
                "The table is scored in your browser against the forms the word "
                "list records, and you can read every row. Each row shows every "
                "spelling the list has for the verb, and says where a wrong "
                "spelling was removed from it. Switch the rule and watch the "
                "number move."
            ),
        }),
        "read_title": "The words that still break it",
        "read_intro": (
            "18 verbs are still wrong after the strong-part test. They are not a "
            "random 18, and most of them are not wrong at all."
        ),
        "worked": {
            "title": "Eleven of the eighteen end in the same letter",
            "intro": [
                "Here are the verbs the rule still gets wrong, split by how they "
                "end. They are the rows the lab shows under <em>only the ones it "
                "gets wrong</em>.",
            ],
            "lines": [
                "ending in -l   cancel, channel, counsel,",
                "               label, level, model, panel,",
                "               rival, signal, total, travel",
                "",
                "everything else   benefit, bus, focus, format,",
                "                  input, output, program",
            ],
            "after": [
                "The first group is not an exception at all. It is a second rule: "
                "British writers double a final <em>-l</em> whatever the strong "
                "part is, and American writers do not. <em>Travelling</em> and "
                "<em>traveling</em> are both correct, in different places, and the "
                "word list records both. This lab asks a strict question of each "
                "verb: does the list ever record a doubled spelling? For these "
                "eleven it does, the British one, so the rule is marked wrong even "
                "though the form it writes is also in the list. The last lesson "
                "counted the same verbs right, because there the test was whether "
                "the rule's form is one the list records.",
                "The second group is seven words. <em>Benefit</em>, <em>focus</em> "
                "and <em>program</em> are the same story again, with both "
                "spellings in the list. <em>Format</em>, <em>input</em> and "
                "<em>output</em> double though the strong part comes first; the "
                "last two are made from <em>put</em>, which doubles, and keep its "
                "spelling. <em>Bus</em> is the one verb the rule doubles and the "
                "list does not: <em>busing</em>. Four true exceptions, and you can "
                "learn them in a minute.",
            ],
        },
        "note": (
            "This is why a hit rate needs its list of misses printed beside it. "
            "91.7% sounds like a rule with 18 holes in it. Reading the 18 shows "
            "that eleven are a different country's spelling, three more are words "
            "the list spells both ways, and the rest are four words you can learn "
            "in a minute."
        ),
        "mistakes": [
            (
                "Using the short rule you were taught",
                "“Consonant, vowel, consonant, so double it” is right "
                "half the time on the words it can touch. It is not a useful "
                "rule, and the lab lets you watch it fail.",
            ),
            (
                "Scoring a rule on words it cannot touch",
                "Run the <em>-ing</em> rule over all 1,210 regular verbs and it "
                "looks almost perfect, 99.34%, because most verbs never end "
                "consonant, vowel, consonant. The honest score for doubling is on "
                "the 217 where the question comes up at all.",
            ),
            (
                "Treating a spelling difference as a mistake",
                "<em>Travelling</em> is not wrong. It is British. A rule that "
                "produces the American form is marked wrong here because the list "
                "also records the British one, and that is the rule being right "
                "about one country rather than wrong about English.",
            ),
        ],
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "Over the 217 verbs the rule can touch, how often is "
                     "“double every one” right?",
                "a": ["Almost always", "About half the time",
                      "About nine times in ten", "Almost never"],
                "c": 1,
                "why": (
                    "107 of 217, which is 49.3%. Half a rule does no better than "
                    "guessing, and that is the form most books print."
                ),
            },
            {
                "q": "Why does <em>admit</em> double but <em>visit</em> not?",
                "a": [
                    "<em>admit</em> is irregular",
                    "<em>visit</em> ends in <em>-t</em>",
                    "<em>visit</em> has two parts",
                    "The strong part of <em>admit</em> is the last one",
                ],
                "c": 3,
                "why": (
                    "Both end consonant, vowel, consonant, both end in "
                    "<em>-t</em>, and both have two parts. In <em>admit</em> the "
                    "strong part is the last; in <em>visit</em> it is the first. "
                    "That one difference is the whole rule."
                ),
            },
            {
                "q": "11 of the 18 remaining failures end in <em>-l</em>. What does that tell you?",
                "a": [
                    "The word list is wrong",
                    "The strong-part test does not work",
                    "They follow a different rule, not no rule",
                    "<em>-l</em> verbs cannot be learned",
                ],
                "c": 2,
                "why": (
                    "British writers double a final <em>-l</em> whatever the "
                    "strong part is. That is a second rule, and knowing it turns "
                    "eleven exceptions into one thing to remember."
                ),
            },
        ],
        "body": [
            ("p",
             "Here is a rule you have met. A verb that ends with a "
             "<dfn>consonant</dfn>, a <dfn>vowel</dfn> and then another consonant "
             "doubles its last letter before <em>-ing</em> or "
             "<em>-ed</em>. <em>Stop</em> becomes <em>stopping</em>. "
             "<em>Plan</em> becomes <em>planned</em>."),
            ("p",
             "Now test it. In the word list this course uses there are 217 verbs "
             "that end that way. If you double all of them you are right 107 "
             "times. If you double none of them you are right 110 times."),
            ("h3", "A rule that does no better than guessing"),
            ("p",
             "49.3% against 50.7%. Those two numbers are the same number for any "
             "use you could put them to. The rule as it is usually given tells "
             "you nothing at all about the word in front of you."),
            ("p",
             "That is worth sitting with, because the rule is not wrong. It is "
             "half of something that works, and the missing half is never printed "
             "beside it."),
            ("h3", "The part that is missing"),
            ("p",
             "Say <em>admit</em> out loud, then say <em>travel</em>. In the first "
             "you push harder on the second part of the word. In the second you "
             "push harder on the first. English spelling cares about that "
             "difference here, and only here."),
            ("p",
             "The full rule is: double the last letter when the word ends "
             "consonant, vowel, consonant <em>and</em> the last part is the part "
             "you say harder. Score that on the same 217 verbs and it is right "
             "199 times, which is 91.7%."),
            ("p",
             "The same letters, the same verbs, the same table. One extra "
             "question, and the rule goes from a guess to something you can "
             "use."),
            ("h3", "Why this rule and no other"),
            ("p",
             "Every other rule in this course so far worked on letters alone. You "
             "could apply them with the sound turned off. This one cannot be done "
             "that way, and that is the reason it is the rule learners get wrong "
             "most often: it is the only place where you have to know how the "
             "word is said before you can write it. Where the strong part falls "
             "in other words is the work of the course called Word Stress, in "
             "the lesson &ldquo;Nouns at the Front, Verbs at the Back&rdquo;."),
            ("h3", "What is left over"),
            ("p",
             "18 verbs are still wrong, and they are not spread about at random. "
             "Eleven of them end in <em>-l</em>: <em>cancel</em>, "
             "<em>travel</em>, <em>model</em>, <em>signal</em> and the rest. "
             "Those are not broken words. British writers double a final "
             "<em>-l</em> whatever the strong part is, and American writers do "
             "not. <em>Travelling</em> and <em>traveling</em> are both right, and "
             "the list records both. The lab asks whether the list ever records "
             "a doubled spelling, so the rule, which writes the American form, is "
             "marked wrong on eleven words where nothing is actually wrong."),
            ("p",
             "That leaves seven: <em>benefit</em>, <em>bus</em>, <em>focus</em>, "
             "<em>format</em>, <em>input</em>, <em>output</em>, "
             "<em>program</em>. Three of them, <em>benefit</em>, <em>focus</em> "
             "and <em>program</em>, are the same story again, with both spellings "
             "in the list. <em>Format</em>, <em>input</em> and <em>output</em> "
             "double against the rule; <em>bus</em> does not double when the rule "
             "says it should. Four words is a minute of your time, and then the "
             "rule is as good as a rule about English spelling ever gets."),
            ("h3", "Three exceptions that were never there"),
            ("p",
             "Before the word list was cleaned, three more words sat in this "
             "group: <em>offer</em>, <em>suffer</em> and <em>council</em>. None "
             "of them belongs here. The list, made by a machine, recorded "
             "<em>offerring</em> and <em>sufferring</em>, spellings nobody "
             "writes, and it gave <em>council</em>, which is not a verb, the form "
             "<em>councilling</em>. Scored against those, a right rule looked "
             "wrong three times. The list has since been cleaned by one test: a "
             "spelling stays only if a <dfn>dictionary</dfn>, a book that records "
             "the real spellings of a language, has it, or if it is the British "
             "spelling of one the dictionary has. Every spelling removed is named "
             "in the lab's table beside the verb it came from. <em>Offer</em> and "
             "<em>suffer</em> now count as right, which they always were, and "
             "<em>council</em> is in the list of words left out, with the reason."),
            ("p",
             "That is the lesson under the lesson. A hit rate is only as good as "
             "the list it is scored on, and a list can be wrong in a way that "
             "makes a right rule look wrong. Read the misses, every time."),
        ],
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "how-ed-and-s-are-said",
        "module": "The rule that needs the sound",
        "title": "How -ed and -s Are Said",
        "one_line": "Two endings, three sounds each, and the last sound of the verb picks the one.",
        "standard": (
            "Finish when you can say, from the last sound of a verb, how its "
            "-ed and its -s are said.",
            "You should be able to say whether the <em>-ed</em> of a verb is said "
            "<em>t</em> or <em>d</em> or a part of its own, and whether its <em>-s</em> "
            "is said <em>s</em> or <em>z</em> or with a part of its own, read "
            "the score of each rule off the printed list, and explain the few "
            "verbs the rules miss.",
        ),
        "summary": (
            "<em>Walked</em>, <em>played</em> and <em>wanted</em> all end in "
            "<em>-ed</em>, and the ending is said three different ways. The last "
            "sound of the verb picks the way, and the rule that does it is right "
            "for 1111 of the 1118 verbs it can be checked on. The seven it "
            "misses are the lesson."
        ),
        "key_label": "How the two endings are said",
        "key": [
            "-ed   after t or d         id   wanted",
            "      after voiceless      t    walked",
            "      after anything else  d    played",
            "-s    after a hiss         iz   passes",
            "      after voiceless      s    walks",
            "      after anything else  z    plays",
            "",
            "the last SOUND picks it, not the last letter",
        ],
        "concepts_intro": "Three ideas, and the second is a test you can do with one finger.",
        "concepts": [
            (
                "One spelling, three sounds",
                "The ending <em>-ed</em> is written the same in <em>walked</em>, "
                "<em>played</em> and <em>wanted</em>, and said three ways. The "
                "ending <em>-s</em> is the same: <em>walks</em>, <em>plays</em> "
                "and <em>passes</em>. The page reads a sound and not a spelling, "
                "so you can hear what the spelling hides.",
            ),
            (
                "The last sound of the verb picks the ending",
                "You do not learn the sound of each verb. You listen to how the "
                "verb ends. After <em>t</em> or <em>d</em>, the past ending is "
                "a part of its own, <dfn>id</dfn>. After a <dfn>hiss</dfn>, the "
                "<em>-s</em> ending is a part of its own, <dfn>iz</dfn>. Everywhere "
                "else the ending joins the last part, and one question picks it: "
                "is the last sound voiced or voiceless?",
            ),
            (
                "A rule about sounds is scored the same way as a rule about "
                "letters",
                "The lab runs each rule over every verb in the printed list and "
                "checks the answer against a <dfn>dictionary</dfn>, a book that records "
                "how words are said. The share "
                "right is printed, and so is every verb the rule gets wrong. The "
                "rule is not a feeling about how English sounds. It is a count.",
            ),
        ],
        "steps_title": "Saying an ending",
        "steps_intro": "To say the ending of a verb you have not heard, do this.",
        "steps": [
            (
                "Say the verb and listen to its last sound",
                "Not the last letter. <em>Love</em> ends in <em>e</em> and "
                "sounds like it ends in <em>v</em>; <em>laugh</em> ends in "
                "<em>-gh</em> and sounds like it ends in <em>f</em>.",
            ),
            (
                "Ask if it is the sound the ending needs a part for",
                "For <em>-ed</em>, that is <em>t</em> or <em>d</em>. For "
                "<em>-s</em>, it is a hiss: the sound that ends <em>pass</em>, "
                "<em>wish</em> or <em>watch</em>. If so, add a part: "
                "<em>id</em> or <em>iz</em>.",
            ),
            (
                "If not, decide if the last sound is voiced",
                "Say the sound with a finger on your throat. A shake means "
                "voiced, and the ending is <em>d</em> or <em>z</em>. No shake "
                "means voiceless, and the ending is <em>t</em> or <em>s</em>.",
            ),
            (
                "Check the short list of verbs that break it",
                "A few verbs do not end the way the dictionary's first "
                "reading says. The lab prints them, and each one has a reason.",
            ),
        ],
        "lab": ("english", {
            "mode": "endings",
            "rule": "ed",
            "show": "misses",
            "panel_title": "Score the two endings on the printed list",
            "panel_intro": (
                "Each verb in the list of the 2,800 most common words has its "
                "last sound looked up in a dictionary of sounds. The rule "
                "says how the ending should be said; the dictionary says how it "
                "is said. The table prints both for every word, and the words "
                "where they differ. Choose <em>the same -s rule on the plurals "
                "of nouns</em> to run the second rule on nouns. Type a verb "
                "under <em>A word from the list</em> and the page says its last "
                "sound, what the rule says and what the dictionary says, so you "
                "can test your own answer before you read the table. The sounds "
                "are American, from the dictionary's first reading of each word."
            ),
        }),
        "read_title": "The verbs that break it",
        "read_intro": (
            "The rule for <em>-ed</em> misses seven verbs of 1118, and the "
            "rule for <em>-s</em> misses two of 1189. Every miss is the rule "
            "being given a sound the form does not have: either the "
            "dictionary's first reading is another word, or the last sound "
            "itself turns voiced before the ending."
        ),
        "worked": {
            "title": "Three verbs, three sounds",
            "intro": [
                "Read the last sound of each verb. The rule picks the ending "
                "from it, and the dictionary agrees.",
            ],
            "lines": [
                "walk    last sound k, voiceless       walked   said t",
                "play    last sound a vowel, voiced    played   said d",
                "want    last sound t                  wanted   said id",
                "",
                "1111 of 1118 verbs follow the -ed rule",
            ],
            "after": [
                "<em>Walk</em> ends in a voiceless sound, so the ending is "
                "<em>t</em>. "
                "<em>Play</em> ends in a vowel, and every vowel is voiced, so "
                "the ending is <em>d</em>. <em>Want</em> ends in <em>t</em>, "
                "and <em>t</em> and <em>d</em> are the sounds that cannot "
                "take a joined ending, so <em>wanted</em> has a part of its "
                "own, <em>id</em>.",
                "The dictionary agrees for 1111 of the 1118 verbs it can check. "
                "That is the whole rule, and you can use it on a verb you have "
                "never heard.",
            ],
        },
        "note": (
            "The same sounds appear in the spelling. A hiss at the end of a "
            "verb is the <em>-es</em> of &ldquo;Five Forms Make Twelve&rdquo;: "
            "<em>passes</em>, <em>wishes</em>, <em>watches</em>. The spelling "
            "rule and the sound rule are two views of one fact."
        ),
        "mistakes": [
            (
                "Saying -ed as a part of its own every time",
                "<em>Walked</em> has one part, not two. The ending is a part "
                "of its own only after <em>t</em> or <em>d</em>, as in "
                "<em>wanted</em> and <em>needed</em>. After <em>walk</em> it is "
                "<em>t</em>, and after <em>play</em> it is <em>d</em>.",
            ),
            (
                "Reading the last letter instead of the last sound",
                "<em>Laugh</em> ends in the letters <em>-gh</em> and the sound "
                "<em>f</em>, so <em>laughed</em> ends in <em>t</em>. "
                "<em>Love</em> ends in the letter <em>e</em> but its last sound "
                "is <em>v</em>, so <em>loved</em> ends in <em>d</em>. The "
                "rule reads sounds.",
            ),
            (
                "Saying the -s ending as s every time",
                "<em>Plays</em>, <em>needs</em> and <em>loves</em> end in "
                "<em>z</em>, not <em>s</em>. The <em>s</em> you see is a "
                "<em>z</em> you hear after a voiced sound.",
            ),
        ],
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "Which of these verbs has an extra part when <em>-ed</em> is added?",
                "a": ["<em>walk</em>", "<em>play</em>", "<em>want</em>", "<em>hope</em>"],
                "c": 2,
                "why": (
                    "<em>Want</em> ends in <em>t</em>, so <em>wanted</em> has a "
                    "part of its own, <em>id</em>. <em>Hoped</em> is one part "
                    "with a <em>t</em> at the end."
                ),
            },
            {
                "q": "Why is <em>played</em> said with <em>d</em> and <em>walked</em> with <em>t</em>?",
                "a": [
                    "<em>Play</em> ends in a voiced sound and <em>walk</em> in a voiceless one",
                    "<em>Play</em> is an irregular verb",
                    "<em>Walked</em> is an older word",
                    "<em>Walk</em> ends in a consonant letter",
                ],
                "c": 0,
                "why": (
                    "After a voiced sound the ending is <em>d</em>; after a "
                    "voiceless one it is <em>t</em>. <em>Play</em> ends in a "
                    "vowel, which is voiced, and <em>walk</em> in <em>k</em>, "
                    "which is not."
                ),
            },
            {
                "q": "What does the rule read to say how an ending is said?",
                "a": [
                    "The first letter of the verb",
                    "The number of parts in the verb",
                    "The last letter of the verb",
                    "The last sound of the verb",
                ],
                "c": 3,
                "why": (
                    "The last sound. <em>Love</em> ends in the letter <em>e</em> "
                    "and the sound <em>v</em>, and it is the sound that decides."
                ),
            },
            {
                "q": "The rule misses <em>used</em>, <em>closed</em> and <em>housed</em>. What do they have in common?",
                "a": [
                    "They are all very rare verbs",
                    "The dictionary's first reading of the base is a noun or an adjective, which ends in a different sound",
                    "They are all irregular",
                    "They all begin with a vowel",
                ],
                "c": 1,
                "why": (
                    "The noun <em>house</em> ends in <em>s</em>, but the verb "
                    "ends in <em>z</em>. Give the rule the verb's sound and it "
                    "is right: <em>housed</em> ends in <em>d</em>."
                ),
            },
        ],
        "body": [
            ("p",
             "<em>Walked</em>, <em>played</em> and <em>wanted</em> all end in "
             "<em>-ed</em>. Say them and the endings are not the same. "
             "<em>Walked</em> ends in a <em>t</em> sound, <em>played</em> in "
             "a <em>d</em> sound, and <em>wanted</em> has an extra part. The "
             "ending <em>-s</em> does the same thing in <em>walks</em>, "
             "<em>plays</em> and <em>passes</em>."),
            ("p",
             "You do not have to learn which sound each verb takes. The last "
             "sound of the verb decides, and there is a rule for it."),
            ("h3", "Voiced and voiceless"),
            ("p",
             "A sound is <dfn>voiceless</dfn> when it is said without the "
             "throat shaking, and <dfn>voiced</dfn> when the throat shakes. "
             "Put a finger on your throat and say <em>s</em>, then <em>z</em>. "
             "The first has no shake and the second does. Every <dfn>vowel</dfn> is voiced. "
             "So are <em>b</em>, <em>d</em>, <em>g</em>, <em>l</em>, "
             "<em>m</em>, <em>n</em>, <em>r</em>, <em>v</em> and <em>z</em>, "
             "among others. "
             "The voiceless ones are <em>p</em>, <em>k</em>, <em>f</em>, "
             "<em>s</em>, <em>t</em>, the sound at the start of <em>think</em>, "
             "the sound at the start of <em>ship</em> and the sound at the "
             "start of <em>church</em>."),
            ("h3", "The rule for -ed"),
            ("ul", [
                "After <em>t</em> or <em>d</em>, the ending is a part of its "
                "own, <em>id</em>: <em>wanted</em>, <em>needed</em>.",
                "After any other voiceless sound, the ending is <em>t</em>: "
                "<em>walked</em>, <em>hoped</em>, <em>laughed</em>.",
                "After any other sound, a vowel included, the ending is "
                "<em>d</em>: <em>played</em>, <em>loved</em>, "
                "<em>opened</em>.",
            ]),
            ("h3", "The rule for -s"),
            ("ul", [
                "After a hiss, the ending is a part of its own, "
                "<em>iz</em>: <em>passes</em>, <em>wishes</em>, "
                "<em>watches</em>.",
                "After any other voiceless sound, the ending is <em>s</em>: "
                "<em>walks</em>, <em>hopes</em>.",
                "After any other sound, a vowel included, the ending is "
                "<em>z</em>: <em>plays</em>, <em>needs</em>, <em>loves</em>.",
            ]),
            ("p",
             "The spelling does not always show the hiss. <em>Judges</em> and "
             "<em>faces</em> end in a silent <em>e</em>, so the spelling adds "
             "only <em>-s</em>, and they still take the extra part."),
            ("h3", "How often the rule is right"),
            ("p",
             "The lab looks up the last sound of each verb in a dictionary "
             "of sounds and applies the rule. The dictionary also says how the "
             "form with the ending is said, so each answer is checked. "
             "Counted on this page, the <em>-ed</em> rule is right for 1111 of "
             "1118 verbs, 99.4%. The <em>-s</em> rule is right for 1187 of "
             "1189, 99.8%. The dictionary does not carry 92 of the past forms "
             "and 21 of the <em>-s</em> forms, such as <em>blogged</em>; the "
             "lab lists them and does not count them."),
            ("h3", "The seven words the -ed rule misses"),
            ("p",
             "Not one of the seven is a verb that breaks the rule. In every one "
             "the dictionary answered about a different word, so the rule was "
             "given a sound the verb does not have."),
            ("ul", [
                "<strong>The dictionary gives the noun or the adjective "
                "first</strong>: <em>abused</em>, <em>closed</em>, "
                "<em>excused</em>, <em>housed</em> and <em>used</em>. The noun "
                "<em>house</em>, the noun <em>use</em> and the adjective "
                "<em>close</em> end in <em>s</em>, but the verbs end in "
                "<em>z</em>, so the ending is <em>d</em>. Give the rule the "
                "verb's sound and it is right.",
                "<strong>A voiceless sound that turns voiced</strong>: "
                "<em>mouthed</em>. The noun <em>mouth</em> ends in the sound at "
                "the start of <em>think</em>. The verb ends in the sound at the "
                "start of <em>then</em>, which is voiced, so the ending is "
                "<em>d</em>, and the rule is right about the verb.",
                "<strong>A form with two readings</strong>: <em>legged</em>. As "
                "a verb, <em>he legged it</em>, the ending is <em>d</em>, as the "
                "rule says. The dictionary's first reading is the adjective, as "
                "in <em>four-legged</em>, which is said with <em>id</em> after "
                "the <em>g</em>. The rule was right; the dictionary was asked "
                "about another word.",
            ]),
            ("p",
             "The <em>-s</em> rule misses <em>knives</em> and <em>mouths</em>, "
             "and both are one turn: a voiceless last sound turns voiced, and "
             "the ending turns to <em>z</em> with it. <em>Knife</em> ends in "
             "<em>f</em>, and the <em>f</em> becomes <em>v</em> in "
             "<em>knives</em>, as it does in <em>wives</em>; the list also "
             "records <em>knifes</em>, which follows the rule, but the "
             "dictionary does not carry it. <em>Mouths</em> is the verb "
             "<em>mouth</em> again, said with the sound at the start of "
             "<em>then</em>, where the dictionary's first reading is the noun."),
            ("h3", "The same rule on nouns"),
            ("p",
             "The <em>-s</em> rule is the same rule on a noun that means more "
             "than one. "
             "Run on 1823 nouns, it is right for 1820, 99.8%, and the three "
             "misses are <em>mouths</em>, <em>paths</em> and <em>youths</em>. "
             "All three end in the sound at the start of <em>think</em>, and in "
             "all three it turns into the sound at the start of <em>then</em> "
             "when the noun means more than one, so the ending is <em>z</em> "
             "and not <em>s</em>. The course called Nouns and Articles returns "
             "to this rule and the words that break it."),
            ("p",
             "Two limits. The sounds are American, from the dictionary's first "
             "reading of each word, so a British speaker may say a word a "
             "little differently. And the rule says how an ending is said, not "
             "when to use it."),
        ],
    },
]
