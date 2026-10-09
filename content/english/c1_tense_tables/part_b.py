# -*- coding: utf-8 -*-
"""Lesson two: the doubling rule, and the part of it most books leave out.

Every figure here is read off the doubling lab's `The rule to score` menu
with `labcheck.js --observe`: 199 / 107 / 110 of 217, 18 wrong, 11 of them
ending in -l. The eighteen are named from the lab's own `wrong` table, and
the three words the raw NGSL made look like exceptions (offer, suffer,
council) are named as what they were: misspellings and a non-verb.
"""

LESSONS = [
    {
        "slug": "when-the-last-letter-doubles",
        "module": "The one rule that needs the sound and not only the letters",
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
            "double every one      107 / 217   49.3%",
            "double none of them   110 / 217   50.7%",
            "double when the last",
            "part is the strong",
            "part                  199 / 217   91.7%",
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
             "Every other rule in the last lesson worked on letters alone. You "
             "could apply them with the sound turned off. This one cannot be done "
             "that way, and that is the reason it is the rule learners get wrong "
             "most often: it is the only place where you have to know how the "
             "word is said before you can write it."),
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
]
