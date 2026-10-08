# -*- coding: utf-8 -*-
"""Course four, lesson two: how a listener finds where one word ends."""

LESSONS = [
    {
        "slug": "where-a-word-begins",
        "module": "Nobody leaves gaps between words. Something else marks them",
        "title": "Where a Word Begins",
        "one_line": "Four content words out of five start on their strong part, and that is the clue.",
        "standard": (
            "Finish when you can say why a strong part is a good guess at the "
            "start of a word, and how often that guess is right.",
            "You should be able to mark the strong part of a written word, say "
            "what share of words carry it at the front, explain why that makes it "
            "useful for finding word boundaries in speech, and name the kinds of "
            "word where the guess fails.",
        ),
        "summary": (
            "Speech has no spaces in it. A listener has to work out where one "
            "word stops and the next starts, and English gives them a strong "
            "clue: most words that carry meaning begin with their strong part. "
            "On the page in the lab that is true of 399 of 485 words, which is "
            "82.3%. So a strong part is a good guess at a new word, and this "
            "lesson counts how good."
        ),
        "key_label": "Counted on the same page as the last lesson",
        "key": [
            "485 words that are not squashed",
            "399 of them start strong    82.3%",
            "",
            "S = said hardest   . = said lightly",
            "",
            "FAther  ANswer  CARriage",
            "beLIEVE  aGAIN  reTURN",
        ],
        "concepts_intro": "Three ideas, and the first is the one nobody tells you.",
        "concepts": [
            (
                "Speech has no spaces",
                "Writing puts a gap between every word. Speech does not. The "
                "sound arrives as one run with no breaks, and a listener has to cut it "
                "up. Every learner is doing this work and almost nobody is told "
                "they are doing it.",
            ),
            (
                "A strong part is a good guess at a new word",
                "Most English words that carry meaning are said with their first "
                "part hardest. So when a listener hears a strong part, the "
                "likeliest explanation is that a new word has started. It is a "
                "guess, and on the page in the lab it is right 82.3% of the time.",
            ),
            (
                "The two lessons work together",
                "The last lesson said about half of what you hear is squashed. "
                "This one says most of the other half announces itself with a "
                "strong part. Those two facts between them are how the run of "
                "sound gets cut into words.",
            ),
        ],
        "steps_title": "Using it on something you are listening to",
        "steps_intro": "Four steps.",
        "steps": [
            (
                "Stop trying to catch every word",
                "Half of them are squashed and you will not catch those first. "
                "Let them go past.",
            ),
            (
                "Listen for the strong parts",
                "They are louder, longer and clearer than what surrounds them. "
                "Each one is probably the front of a word that matters.",
            ),
            (
                "Take the meaning from those",
                "The words carrying the message are the ones being said strongly. "
                "If you get those you usually have the sentence.",
            ),
            (
                "Fill the gaps afterwards",
                "What sat between the strong parts was almost certainly from the "
                "list of fifty in the last lesson, and you can often work out "
                "which without having heard it clearly at all.",
            ),
        ],
        "lab": ("english", {
            "mode": "listening",
            "panel_title": "Mark the strong part of every word",
            "panel_intro": (
                "Choose the second setting. Every word that is not squashed is "
                "marked with where it is said hardest: <em>S</em> for the strong "
                "part and a dot for a light one. The count at the top is how many "
                "of those words start on their strong part."
            ),
        }),
        "read_title": "Where the guess fails",
        "read_intro": (
            "Not every word starts strong. The ones that do not fall into a few "
            "groups, and they are worth knowing."
        ),
        "worked": {
            "title": "The words that start light",
            "intro": [
                "A dot is a light part and S is the strong one.",
            ],
            "lines": [
                "start strong     start light",
                "",
                "FAther  S.       beLIEVE   .S",
                "ANswer  S.       aGAIN     .S",
                "MARket   S.      reTURN    .S",
                "HAPpiness S..    aNOTHer   .S.",
                "",
                "399 of 485 start strong    82.3%",
            ],
            "after": [
                "Most of the words that start light begin with a small piece "
                "added to the front &mdash; <em>be-</em>, <em>a-</em>, "
                "<em>re-</em>, <em>in-</em>, <em>de-</em>. Those pieces are "
                "almost never said strongly.",
                "So the guess fails in a group you can learn rather than at "
                "random, which is what makes it useful. A listener who knows the "
                "front pieces knows when to expect the strong part to arrive "
                "second.",
            ],
        },
        "note": (
            "The 82.3% here is for written prose from 1813. Work on conversation "
            "puts the figure closer to nine in ten, which is quoted from Cutler "
            "and Carter rather than counted on this page."
        ),
        "mistakes": [
            (
                "Trying to hear every word equally",
                "Half of them are squashed and will not reward the effort. "
                "Listening for the strong parts first is not cutting corners; it "
                "is what a native listener does.",
            ),
            (
                "Reading the strong part off the spelling",
                "The spelling does not say where the strong part falls. "
                "<em>Record</em> is two different words depending on it. You have "
                "to learn it with the word, which is why the lab prints it.",
            ),
            (
                "Taking 82.3% as a rule rather than a guess",
                "Nearly one word in five starts light. The figure is useful "
                "because it is high, not because it is certain, and the lesson "
                "names the group where it fails.",
            ),
        ],
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "Why does a listener need help to find where words begin?",
                "a": [
                    "Speech has no gaps between words",
                    "People speak too quickly",
                    "Words change their spelling",
                    "English has too many words",
                ],
                "c": 0,
                "why": (
                    "Writing puts spaces in. Speech does not, so the run of sound "
                    "has to be cut up by the listener."
                ),
            },
            {
                "q": "On the page in the lab, how many of the unsquashed words start on their strong part?",
                "a": ["About four in five", "About half", "About one in five", "Nearly all of them"],
                "c": 0,
                "why": "399 of 485, which is 82.3%.",
            },
            {
                "q": "What do most of the words that start light have in common?",
                "a": [
                    "A small piece added to the front, like <em>be-</em> or <em>re-</em>",
                    "They are all very short",
                    "They are all irregular verbs",
                    "They all come from French",
                ],
                "c": 0,
                "why": (
                    "<em>Believe</em>, <em>return</em>, <em>again</em>. Those "
                    "front pieces are almost never said strongly, so the failures "
                    "are a group you can learn."
                ),
            },
        ],
        "body": [
            ("p",
             "Write a sentence down and it comes with spaces in it. Say the same "
             "sentence and the spaces are gone. The sound arrives as one run, and the "
             "person listening has to decide where each word stops."),
            ("p",
             "You do this in your own language without noticing. In a new "
             "language it is most of the difficulty, and almost nobody mentions "
             "it."),
            ("h3", "The help English gives"),
            ("p",
             "English words that carry meaning are usually said with their first "
             "part hardest. <em>Father</em>, <em>answer</em>, <em>carriage</em>, "
             "<em>happiness</em> all lead with their strong part."),
            ("p",
             "So a strong part is a reasonable guess that a new word has just "
             "started. On the page in the lab, 399 of the 485 unsquashed words "
             "start that way: 82.3%."),
            ("h3", "Why that is enough to work with"),
            ("p",
             "Four times in five is not sure, and it does not need to be. A "
             "listener is not deciding one boundary on its own; they are using "
             "this help many times a second alongside everything else they know, "
             "and a guess that is right four times in five is very strong help."),
            ("p",
             "It also fits with the last lesson. About half of what you hear is "
             "squashed and carries little meaning. Most of the rest announces "
             "itself by being said strongly at the front. Between them, the run "
             "of sound has a shape."),
            ("h3", "Where it fails"),
            ("p",
             "Nearly one word in five starts on a light part instead: "
             "<em>believe</em>, <em>again</em>, <em>return</em>, "
             "<em>another</em>. Look at those and a pattern appears. They begin "
             "with a small piece stuck on the front, and those pieces are almost "
             "never the strong part."),
            ("p",
             "That makes the failures easy to learn. You are not facing one word in "
             "five at random; you are facing a short set of front pieces, and "
             "once you know them you know when to expect the strong part to come "
             "second."),
            ("h3", "What to do with this"),
            ("p",
             "Stop trying to catch everything. Listen for the strong parts, take "
             "the meaning from the words carrying them, and let the squashed ones "
             "go by. Most of what sat between the strong parts came from the list "
             "of fifty in the last lesson, and you can often work it out "
             "afterwards without having heard it clearly at all."),
            ("p",
             "That is not a trick for people starting out. It is what a listener who grew "
             "up with the language is already doing."),
        ],
    },
]
