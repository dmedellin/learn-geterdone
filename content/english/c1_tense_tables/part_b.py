# -*- coding: utf-8 -*-
"""Lesson two: the doubling rule, and the part of it most books leave out."""

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
            "list, and name the group of words it still gets wrong and what they "
            "have in common.",
        ),
        "summary": (
            "You have probably been told that a verb ending consonant, vowel, "
            "consonant doubles its last letter: <em>stop</em> becomes "
            "<em>stopping</em>. On the 232 verbs where that rule can apply, it is "
            "right about half the time. The missing half of the rule is where the "
            "strong part of the word falls, and adding it takes the same rule from "
            "50% to 90%."
        ),
        "key_label": "The same 232 verbs, three rules",
        "key": [
            "double every one      117 / 232   50.4%",
            "double none of them   115 / 232   49.6%",
            "double when the last",
            "part is the strong",
            "part                  210 / 232   90.5%",
            "",
            "of the 22 still wrong, 13 end in -l",
        ],
        "concepts_intro": "Three ideas, and the third is the one worth keeping.",
        "concepts": [
            (
                "The rule can only touch some verbs",
                "Doubling is only ever a question for a verb ending consonant, "
                "vowel, consonant &mdash; <em>stop</em>, <em>admit</em>, "
                "<em>travel</em>. There are 232 of those in the word list, and "
                "no other verb is affected. Scoring the rule on all 1,356 "
                "verbs would hide how often it fails, because most verbs never "
                "ask the question.",
            ),
            (
                "Half a rule is only a guess",
                "Of those 232, 117 double and 115 do not. So “double them "
                "all” is right 50.4% of the time and “double none” "
                "is right 49.6%. A rule that does no better than guessing is not "
                "a rule, and this is the form most books print.",
            ),
            (
                "The missing half is where the strong part falls",
                "<em>Stop</em> has one part, so the last part is the strong one, "
                "and it doubles. <em>Travel</em> has two and the strong one is the "
                "first, so it does not. Adding that test takes the same rule to "
                "210 of 232, which is 90.5%.",
            ),
        ],
        "steps_title": "Deciding, for a verb in front of you",
        "steps_intro": "Four questions, in this order.",
        "steps": [
            (
                "Does it end consonant, vowel, consonant?",
                "If not, stop: the rule has nothing to say, and you simply add the "
                "ending.",
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
                "There are 22, and 13 of them end in <em>-l</em>. Learn that one "
                "group and the rule is almost perfect.",
            ),
        ],
        "lab": ("tense", {
            "mode": "doubling",
            "panel_title": "Score the rule yourself, three ways",
            "panel_intro": (
                "These are every verb in the word list ending consonant, vowel, "
                "consonant &mdash; the only verbs the doubling rule can touch. "
                "The table is scored in your browser against the forms the word "
                "list records, and you can read every row. Switch the rule and "
                "watch the number move."
            ),
        }),
        "read_title": "The words that still break it",
        "read_intro": (
            "22 verbs are still wrong after the strong-part test. They are not a "
            "random 22."
        ),
        "worked": {
            "title": "Thirteen of the twenty-two end in the same letter",
            "intro": [
                "Here are the verbs the rule still gets wrong, split by how they "
                "end.",
            ],
            "lines": [
                "ending in -l   cancel, channel, council,",
                "               counsel, label, level,",
                "               metal, model, panel, rival,",
                "               signal, total, travel",
                "",
                "everything else   benefit, bus, focus,",
                "                  format, input, offer,",
                "                  output, program, suffer",
            ],
            "after": [
                "The first group is not an exception at all. It is a second rule: "
                "British writers double a final <em>-l</em> whatever the strong "
                "part is, and American writers do not. <em>Travelling</em> and "
                "<em>traveling</em> are both correct, in different places. The "
                "word list records one of them, so the rule is marked wrong on "
                "thirteen words where nothing is wrong.",
                "The second group is small enough to learn directly, and several "
                "of them are words that came into English recently enough that "
                "writers have not settled: <em>formatting</em> and "
                "<em>inputting</em> double, <em>focusing</em> usually does not.",
            ],
        },
        "note": (
            "This is why a hit rate needs its list of misses printed beside it. "
            "90.5% sounds like a rule with 22 holes in it. Reading the 22 shows "
            "that more than half are a different country's spelling, and the rest "
            "are a few words you can learn in a minute."
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
                "Run the doubling rule over all 1,356 verbs and it looks almost "
                "perfect, because most verbs never end consonant, vowel, "
                "consonant. The honest score is on the 232 where the question "
                "comes up at all.",
            ),
            (
                "Treating a spelling difference as a mistake",
                "<em>Travelling</em> is not wrong. It is British. A rule that "
                "produces the American form will be marked wrong against a "
                "British word list, and that is the rule being right about one "
                "country rather than wrong about English.",
            ),
        ],
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "Over the 232 verbs the rule can touch, how often is "
                     "“double every one” right?",
                "a": ["About half the time", "Almost always", "Almost never",
                      "About nine times in ten"],
                "c": 0,
                "why": (
                    "117 of 232, which is 50.4%. Half a rule does no better than "
                    "guessing, and that is the form most books print."
                ),
            },
            {
                "q": "Why does <em>admit</em> double but <em>benefit</em> not?",
                "a": [
                    "The strong part of <em>admit</em> is the last one",
                    "<em>benefit</em> is longer",
                    "<em>admit</em> is irregular",
                    "<em>benefit</em> ends in <em>-t</em>",
                ],
                "c": 0,
                "why": (
                    "Both end consonant, vowel, consonant. In <em>admit</em> the "
                    "strong part is the last; in <em>benefit</em> it is the first. "
                    "<em>Benefit</em> is one of the 22 the rule still gets wrong."
                ),
            },
            {
                "q": "13 of the 22 remaining failures end in <em>-l</em>. What does that tell you?",
                "a": [
                    "They follow a different rule, not no rule",
                    "The word list is wrong",
                    "<em>-l</em> verbs cannot be learned",
                    "The strong-part test does not work",
                ],
                "c": 0,
                "why": (
                    "British writers double a final <em>-l</em> whatever the "
                    "strong part is. That is a second rule, and knowing it turns "
                    "thirteen exceptions into one thing to remember."
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
             "Now test it. In the word list this course uses there are 232 verbs "
             "that end that way. If you double all of them you are right 117 "
             "times. If you double none of them you are right 115 times."),
            ("h3", "A rule that does no better than guessing"),
            ("p",
             "50.4% against 49.6%. Those two numbers are the same number for any "
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
             "you say harder. Score that on the same 232 verbs and it is right "
             "210 times, which is 90.5%."),
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
             "22 verbs are still wrong, and they are not spread about at random. Thirteen of "
             "them end in <em>-l</em>: <em>cancel</em>, <em>travel</em>, "
             "<em>model</em>, <em>signal</em> and the rest."),
            ("p",
             "Those are not broken words. British writers double a final "
             "<em>-l</em> whatever the strong part is, and American writers do "
             "not. <em>Travelling</em> and <em>traveling</em> are both right. The "
             "rule here gives the American form, so it is marked wrong on thirteen "
             "words where nothing is actually wrong."),
            ("p",
             "That leaves nine: <em>benefit</em>, <em>bus</em>, <em>focus</em>, "
             "<em>format</em>, <em>input</em>, <em>offer</em>, <em>output</em>, "
             "<em>program</em>, <em>suffer</em>. Nine words is a minute of your "
             "time, and then the rule is as good as a rule about English spelling "
             "ever gets."),
        ],
    },
]
