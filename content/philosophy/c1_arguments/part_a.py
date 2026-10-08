"""Course 1, lessons 01-06 -- what an argument is, and propositional logic."""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "premises-conclusions-and-standard-form",
        "title": "Premises, Conclusions and Standard Form",
        "module": "What an argument is",
        "one_line": "Find the claim a passage defends, and lay out what is offered for it.",
        "summary": (
            "An argument is a set of sentences, one of which the others are offered "
            "in support of. Rewrite a passage as numbered premises and a single "
            "conclusion, strike the sentences that do no work, and see in a table of "
            "cases what it would take for the support to fail."
        ),
        "key": [
            "argument = premises + one conclusion",
            "the conclusion is what the rest support",
            "indicators: since, because, therefore",
            "a case: true or false for each sentence",
            "two sentences, four cases; three, eight",
        ],
        "key_label": "Standard form in five lines",
        "concepts_intro": (
            "Philosophy is mostly argument, and an argument cannot be tested until it "
            "has been taken apart. Standard form is the taking apart."
        ),
        "concepts": [
            ("Premise and conclusion are roles",
             "No sentence is a premise or a conclusion in itself. The same sentence is "
             "a conclusion in one passage and a premise in the next. The role is fixed "
             "by what the author is trying to get you to accept, and by what is offered "
             "for it."),
            ("Position is not a guide",
             "The conclusion may come first, last or in the middle. Words such as "
             "&ldquo;therefore&rdquo; and &ldquo;hence&rdquo; flag a conclusion; "
             "&ldquo;since&rdquo; and &ldquo;because&rdquo; flag a premise. They are "
             "clues to the author's intention, not a rule."),
            ("A case is a row",
             "To ask whether the support could fail, we need the ways the world might "
             "be, so far as the sentences are concerned. With two simple sentences "
             "there are four: both true, only the first, only the second, neither. "
             "Each is a row of a table."),
        ],
        "read_title": "From a passage to standard form",
        "read_intro": (
            "Standard form is a layout, not a theory: premises numbered, a line, one "
            "conclusion. What matters is what the layout makes visible."
        ),
        "body": [
            ("def", ("Argument",
                     "An <strong>argument</strong> is a set of sentences in which one, "
                     "the <strong>conclusion</strong>, is offered as supported by the "
                     "others, the <strong>premises</strong>. A passage that states "
                     "claims and offers no support for any of them is a description, "
                     "not an argument.")),
            ("p", "Everyday passages do not come in that layout. They begin with the "
                  "conclusion, trail off into asides, repeat themselves and leave out the "
                  "step that everyone is assumed to grant. Writing the passage in "
                  "standard form means deciding, sentence by sentence, which job it is "
                  "doing."),
            ("example", ("A passage in standard form",
                         "&ldquo;The streets are wet. Streets here are only wet after "
                         "rain. So it rained.&rdquo; The last sentence is flagged by "
                         "&ldquo;so&rdquo;. Set out, it reads: P1, the streets are wet; "
                         "P2, streets here are wet only after rain; C, it rained.")),
            ("p", "Three kinds of sentence turn up in a passage, and only the first "
                  "two belong in the standard form. Premises give the support. The "
                  "conclusion is what the support is for. Everything else &mdash; a "
                  "digression, a repetition, a flourish &mdash; does no work, and the "
                  "test is whether deleting the sentence changes what the passage gives "
                  "you reason to accept."),
            ("p", "The conclusion is the sentence the others are offered in support of. "
                  "Find it by asking what the passage wants you to believe or do, not by "
                  "looking at the end. &ldquo;The bus will be late, since the road is "
                  "closed&rdquo; puts the conclusion first and the premise last."),
            ("p", "A table of cases makes the idea of support exact. Let `p` stand for "
                  "&ldquo;the streets are wet&rdquo; and `q` for &ldquo;it rained&rdquo;. "
                  "With two sentences there are two possibilities each, so four cases."),
            ("math", [
                "case    p   q",
                "-------------",
                "1       T   T",
                "2       T   F",
                "3       F   T",
                "4       F   F",
            ]),
            ("p", "The lab below takes premises and a conclusion and lists these cases. "
                  "It marks any case in which every premise is true and the conclusion "
                  "false, because that is the case in which the support has failed. Later "
                  "in this course the same table decides validity; here it is used only "
                  "to show why one premise `p` does not support a different sentence "
                  "`q`, and why adding a premise that is not used changes nothing."),
            ("p", "One limit, stated once. The lab works with simple sentences named by "
                  "single letters. Whether &ldquo;it rained&rdquo; is the right way to "
                  "put the author's claim is a judgement you make while writing the "
                  "standard form, and no lab checks it."),
        ],
        "lab": ("argkit", {
            "mode": "validity",
            "preset": "bare",
            "show": "all",
            "presets": [
                {"id": "bare", "label": "p and q, so p",
                 "premises": ["p", "q"], "conclusion": "p", "expect": {"vaVerdict": "Valid", "vaCounter": "0"}},
                {"id": "leap", "label": "p, so q",
                 "premises": ["p"], "conclusion": "q", "expect": {"vaVerdict": "Invalid", "vaCounter": "1"}},
                {"id": "padding", "label": "p, q and r, so p",
                 "premises": ["p", "q", "r"], "conclusion": "p", "expect": {"vaVerdict": "Valid", "vaCounter": "0"}},
            ],
            "panel_title": "Which cases would break the support",
            "panel_intro": (
                "Each row is a case: a true or false for every simple sentence. A row "
                "is highlighted when every premise is true and the conclusion false. "
                "Choose the leap preset first and find the one highlighted row, then "
                "choose the padding preset and compare how many rows there are with "
                "how many are highlighted."
            ),
        }),
        "steps_title": "Setting out a passage",
        "steps_intro": "Four moves, in this order. The third is the one people skip.",
        "steps": [
            ("Find what is being defended",
             "Ask what the passage wants you to accept. That sentence is the "
             "conclusion, wherever it stands. If you cannot find one, the passage "
             "may be a description, and there is nothing to set out."),
            ("Mark the indicator words",
             "&ldquo;Therefore&rdquo;, &ldquo;so&rdquo; and &ldquo;hence&rdquo; point "
             "to a conclusion; &ldquo;since&rdquo; and &ldquo;because&rdquo; point to "
             "a premise. Treat each as a clue and check it against the first move."),
            ("Strike the sentences that do no work",
             "Delete a sentence in your head. If the support for the conclusion is "
             "unchanged, it was padding: an aside, a repetition, a rhetorical "
             "flourish. Leave it out of the standard form."),
            ("Write it out",
             "Number the premises, draw a line, write the conclusion once. Put each "
             "claim as a complete sentence, and add a missing premise only when the "
             "passage plainly depends on it, saying so."),
        ],
        "worked": {
            "title": "The wet streets",
            "intro": [
                "The passage: &ldquo;The streets are wet. Streets here are only wet "
                "after rain. So it rained.&rdquo; Let `p` be &ldquo;the streets are "
                "wet&rdquo; and `q` be &ldquo;it rained&rdquo;.",
            ],
            "lines": [
                "P1.  The streets are wet.",
                "P2.  Streets here are wet only after rain.",
                "-----------------------------------------",
                "C.   It rained.",
            ],
            "after": [
                "The lab cannot take P2 yet, because P2 is a conditional and the "
                "connectives come in the next lessons. What it can take is P1 alone. "
                "In the leap preset, `p` is the only premise and `q` the conclusion, and "
                "the lab finds one row where the support fails: `p` true and `q` false, "
                "the streets wet and no rain. P2 is exactly the sentence that rules "
                "that row out, which is why the passage needed it, and why an author "
                "who leaves it unstated is still relying on it.",
            ],
        },
        "quiz_title": "Find the conclusion",
        "quiz": [
            {"q": "&ldquo;Since the lease forbids pets, and Ana keeps a cat, Ana is in "
                  "breach. Incidentally, the cat is orange.&rdquo; Which sentence is the "
                  "conclusion?",
             "a": ["The lease forbids pets", "Ana keeps a cat",
                   "Ana is in breach", "The cat is orange"],
             "c": 2,
             "why": "The two sentences after &ldquo;since&rdquo; are offered in support "
                    "of Ana's being in breach. The orange cat supports nothing, so it "
                    "is padding, and the first two are premises."},
            {"q": "In the lab, the padding preset has premises `p`, `q` and `r` and "
                  "conclusion `p`. What does the table show?",
             "a": ["Four rows, none highlighted", "Eight rows, none highlighted",
                   "Eight rows, one highlighted", "Six rows, none highlighted"],
             "c": 1,
             "why": "Three simple sentences give `2 · 2 · 2 = 8` rows. No row has "
                    "`p` true and `p` false, so none is highlighted, and the extra "
                    "premises `q` and `r` do no work."},
            {"q": "&ldquo;We should leave now. The last train is at eleven, and it is "
                  "already half past ten.&rdquo; Which sentence is the conclusion?",
             "a": ["It is already half past ten",
                   "The last train is at eleven",
                   "We should leave now",
                   "There is no conclusion; the passage is a description"],
             "c": 2,
             "why": "The passage wants you to accept that you should leave, and offers "
                    "the train time and the clock as its reasons. The conclusion comes "
                    "first and carries no indicator word at all, which is why asking "
                    "what is being defended beats looking at the end."},
            {"q": "In the leap preset the premise is `p` and the conclusion is `q`. "
                  "Which row is highlighted?",
             "a": ["`p` false, `q` true", "`p` false, `q` false",
                   "`p` true, `q` true", "`p` true, `q` false"],
             "c": 3,
             "why": "A row is highlighted when the premise is true and the conclusion "
                    "false. Only `p` true with `q` false does both."},
        ],
        "mistakes": [
            ("Taking the conclusion to be whatever comes last",
             "Authors often state the conclusion first and give reasons after it: "
             "&ldquo;The bus will be late, since the road is closed.&rdquo; The "
             "conclusion is the sentence the others are offered in support of, and you "
             "find it by asking what the passage wants you to accept."),
            ("Treating every sentence as a premise",
             "A passage carries asides and repetitions that support nothing. Delete a "
             "sentence; if the support for the conclusion is unchanged, it was padding "
             "and does not go into the standard form. The padding preset shows the "
             "same thing in the table: two extra premises, four extra rows, and not "
             "one more highlighted."),
            ("Reading &ldquo;because&rdquo; as the mark of an argument",
             "&ldquo;The streets are wet because it rained&rdquo; may explain a fact "
             "that nobody doubts, rather than argue for a claim somebody does. An "
             "argument tries to give you a reason to accept something. An explanation "
             "assumes you accept it and says why it is so."),
        ],
        "standard": (
            "Finish when you can set out a passage and defend each choice.",
            "Given a short passage, write numbered premises and one conclusion, name "
            "the sentences you left out and say why each does no work, and say which "
            "sentence the others are offered in support of. A layout without those "
            "reasons is a guess."
        ),
        "note": (
            "The lab is here for its rows, not its verdicts. The word valid is defined "
            "in the next lesson; for now, read a highlighted row as a case in which "
            "the support has failed."
        ),
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "validity-and-soundness",
        "title": "Validity and Soundness",
        "module": "What an argument is",
        "one_line": "Two questions kept apart: could the premises be true with the conclusion false, and are the premises in fact true?",
        "summary": (
            "Validity asks whether any case has true premises and a false conclusion. "
            "Soundness asks, in addition, whether the premises are in fact true. The "
            "first can be settled by looking at cases; the second needs the world. "
            "Keeping them apart is the first discipline of the whole subject."
        ),
        "key": [
            "valid: no case with premises T, conclusion F",
            "sound: valid, and the premises are true",
            "a lab can check valid, not sound",
            "valid arguments can have false conclusions",
        ],
        "key_label": "Two words, two questions",
        "concepts_intro": (
            "In everyday speech a valid point is a good point. In logic, validity is "
            "a narrow property of the link between premises and conclusion."
        ),
        "concepts": [
            ("Validity is about the link",
             "An argument is valid when it is impossible, in the sense of there being "
             "no describable case, for every premise to be true and the conclusion "
             "false. It says nothing about whether any premise is true."),
            ("Soundness adds the world",
             "A sound argument is valid and has only true premises. Soundness is "
             "the property you want when you are trying to establish the conclusion, "
             "and the only part of it a table can check is the first half."),
            ("A bad conclusion is a reason to doubt a premise",
             "If a valid argument leads to a conclusion you reject, you are not "
             "entitled to say the argument is invalid. You are committed to rejecting "
             "at least one premise. This is the move most philosophical argument "
             "turns on."),
        ],
        "read_title": "Valid, invalid, sound, unsound",
        "read_intro": (
            "Four combinations of two properties, and the one combination that is "
            "ruled out."
        ),
        "body": [
            ("def", ("Validity",
                     "An argument is <strong>valid</strong> when there is no case in "
                     "which every premise is true and the conclusion is false. "
                     "Otherwise it is <strong>invalid</strong>, and any one such case "
                     "shows it.")),
            ("def", ("Soundness",
                     "An argument is <strong>sound</strong> when it is valid and every "
                     "premise is true. Otherwise it is <strong>unsound</strong>: either "
                     "invalid, or valid with at least one false premise.")),
            ("p", "The definition is a ban on one combination: true premises with a "
                  "false conclusion. Every other combination of true and false can "
                  "occur in a valid argument. In particular a valid argument can have "
                  "false premises and a false conclusion, and false premises and a "
                  "true conclusion."),
            ("example", ("Valid and unsound",
                         "&ldquo;All whales are fish. All fish fly. So all whales "
                         "fly.&rdquo; Suppose the premises were true; then whales would "
                         "be among the fish and the fish among the fliers, so whales "
                         "would fly. No case has the premises true and the conclusion "
                         "false, so the argument is valid. Both premises are false, so "
                         "it is unsound.")),
            ("example", ("Invalid with true parts",
                         "&ldquo;Paris is in France. So Rome is in Italy.&rdquo; Every "
                         "sentence is true. The argument is invalid, because it is easy "
                         "to describe a case in which the premise is true and the "
                         "conclusion false: the two sentences are about different "
                         "things, and nothing ties one to the other.")),
            ("p", "So the lab, which looks at cases, can settle validity. Take the "
                  "preset `same`, with premise `p` and conclusion `p`. There are two "
                  "cases, `p` true and `p` false, and in neither is the premise true "
                  "while the conclusion is false. The lab calls it valid whatever `p` "
                  "says. If `p` is &ldquo;whales fly&rdquo;, the argument is valid and "
                  "unsound; the lab has no way to know that, and no claim about whales "
                  "enters the check."),
            ("p", "The preset `other` has premise `q` and conclusion `p`. Four cases, "
                  "and in one of them `q` is true and `p` false. That single case is "
                  "all the invalidity there is. The preset `both`, with premises `p` "
                  "and `q` and conclusion `q`, has the same four cases and no such "
                  "one: wherever both premises hold, `q` holds, because `q` is one of "
                  "them."),
            ("thm", ("Using a valid argument",
                     "If an argument is valid, then accepting all its premises commits "
                     "you to its conclusion, and rejecting its conclusion commits you "
                     "to rejecting at least one premise. Which of the two to do is a "
                     "question about the premises, and the table does not answer it.")),
            ("p", "The last point is where the lessons ahead begin. A skeptic offers a "
                  "valid argument whose conclusion is that you know nothing; you may "
                  "accept the conclusion or reject a premise, and what each costs is "
                  "the argument. Validity guarantees that you have to choose."),
        ],
        "lab": ("argkit", {
            "mode": "validity",
            "preset": "same",
            "show": "all",
            "presets": [
                {"id": "same", "label": "p, so p",
                 "premises": ["p"], "conclusion": "p", "expect": {"vaVerdict": "Valid", "vaRows": "2"}},
                {"id": "other", "label": "q, so p",
                 "premises": ["q"], "conclusion": "p", "expect": {"vaVerdict": "Invalid", "vaRows": "4"}},
                {"id": "both", "label": "p and q, so q",
                 "premises": ["p", "q"], "conclusion": "q", "expect": {"vaVerdict": "Valid", "vaRows": "4"}},
            ],
            "panel_title": "Valid, or not, from the cases alone",
            "panel_intro": (
                "The lab never asks whether a sentence is true; it asks only whether "
                "some case makes every premise true and the conclusion false. Read the "
                "verdict and the number of rows for each preset, then retype a premise "
                "or the conclusion and watch the verdict move."
            ),
        }),
        "steps_title": "Classifying an argument",
        "steps_intro": "Two questions, asked separately and in this order.",
        "steps": [
            ("Set out the argument",
             "Write the premises and the conclusion in standard form, as in the "
             "previous lesson. Classify nothing until you know what is being "
             "classified."),
            ("Look for a case",
             "Describe a case in which every premise is true and the conclusion "
             "false. Do not ask whether the case actually holds; ask whether it can "
             "be described. If one can, the argument is invalid and you are done."),
            ("If there is no such case, call it valid",
             "Validity is a verdict on the absence of a case, so it needs every case "
             "checked. Here the lab does what a person does slowly."),
            ("Then, and only then, ask about the premises",
             "A valid argument is sound if every premise is true. That is a question "
             "about the world, and an unsound argument has not been refuted so much "
             "as turned into a question about which premise to doubt."),
        ],
        "worked": {
            "title": "Whales and fish",
            "intro": [
                "The argument: all whales are fish; all fish fly; so all whales fly.",
            ],
            "lines": [
                "Valid?  Describe a case: premises true, conclusion false.",
                "        If whales are fish and fish fly, whales fly.",
                "        No such case.  The argument is valid.",
                "Sound?  Is every premise true?",
                "        Whales are mammals.  P1 is false.",
                "        The argument is unsound.",
            ],
            "after": [
                "The lab can do the first half of this. It cannot do the second, "
                "because &ldquo;whales are fish&rdquo; is a claim about the world and "
                "the lab was never told about whales. That division of labour is the "
                "reason to separate the two words.",
            ],
        },
        "quiz_title": "Valid and sound",
        "quiz": [
            {"q": "Which combination is impossible in a valid argument?",
             "a": ["True premises and a true conclusion",
                   "A false premise and a true conclusion",
                   "True premises and a false conclusion",
                   "False premises and a false conclusion"],
             "c": 2,
             "why": "That is exactly the combination validity rules out. Each of the "
                    "other three can occur in a valid argument."},
            {"q": "An argument has a true conclusion. What follows about it?",
             "a": ["It is valid", "It is sound",
                   "Its premises are all true",
                   "Nothing about its validity or soundness"],
             "c": 3,
             "why": "A true conclusion can come at the end of an invalid argument "
                    "(&ldquo;Paris is in France, so Rome is in Italy&rdquo;) or of a "
                    "valid argument with a false premise. Neither property follows."},
            {"q": "The lab calls `q`, so `p` invalid. What did it find?",
             "a": ["A row with `q` true and `p` false",
                   "A row with `q` and `p` both false",
                   "That `q` is false in the world",
                   "That `p` is false in the world"],
             "c": 0,
             "why": "Invalidity is established by one case with true premises and a "
                    "false conclusion. The lab does not look at the world, so the "
                    "last two choices describe something it cannot do."},
            {"q": "You are sure an argument is valid and sure its conclusion is false. "
                  "What follows?",
             "a": ["The argument must be invalid",
                   "At least one premise is false",
                   "The conclusion must be true after all",
                   "The argument is sound"],
             "c": 1,
             "why": "Validity bans true premises with a false conclusion. With a false "
                    "conclusion the premises cannot all be true. The first and third "
                    "choices deny what you were told, and a sound argument has a true "
                    "conclusion."},
        ],
        "mistakes": [
            ("Thinking a valid argument has a true conclusion",
             "Validity is conditional: if the premises are true, so is the conclusion. "
             "&ldquo;All whales are fish; all fish fly; so all whales fly&rdquo; is "
             "valid, and its conclusion is false; validity allows that only because "
             "a premise is false too. A table cannot tell you that the conclusion is "
             "true; only that it cannot be false while every premise is true."),
            ("Using &ldquo;valid&rdquo; to mean &ldquo;reasonable&rdquo;",
             "&ldquo;That is a valid point&rdquo; praises a claim. In logic the word "
             "applies to arguments, never to sentences, and an argument with absurd "
             "premises can be perfectly valid. A sentence is true or false; an "
             "argument is valid or invalid."),
            ("Rejecting a valid argument's conclusion by calling it invalid",
             "If the argument is valid and you do not like the conclusion, the "
             "argument stands and one of the premises must go. Showing that you can "
             "find the premise to reject is the work; saying &ldquo;it cannot be "
             "valid&rdquo; is only a refusal to do it."),
        ],
        "standard": (
            "Finish when you can classify an argument twice, with a reason each time.",
            "Given an argument, say whether it is valid by looking for a case with true "
            "premises and a false conclusion, and then whether it is sound by checking "
            "the premises against what you know. Explain why the lab answers only "
            "the first question."
        ),
        "note": (
            "The argument &ldquo;`p`, so `p`&rdquo; looks trivial, and it is meant to. "
            "It is the smallest valid argument, and it shows that validity depends on "
            "the form alone: whatever `p` says, the verdict is the same."
        ),
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "truth-values-and-the-connectives",
        "title": "Truth Values and the Connectives",
        "module": "Propositional logic",
        "one_line": "Build the table of a compound sentence and find the row where the two kinds of or part.",
        "summary": (
            "Not, and and or are defined by the truth value they give, whatever the "
            "English words suggest. The one that surprises people is or, which logic "
            "reads as true when both parts are true; the exclusive reading is a "
            "separate connective, and the tables differ in exactly one row."
        ),
        "key": [
            "¬p     true when p is false",
            "p ∧ q  true when both are true",
            "p ∨ q  true when at least one is true",
            "p ⊕ q  true when exactly one is true",
            "or in logic includes both",
        ],
        "key_label": "Three connectives and the exclusive or",
        "concepts_intro": (
            "A connective builds a bigger sentence from smaller ones, and in this "
            "course the bigger sentence's truth value depends on nothing but the "
            "smaller ones' truth values."
        ),
        "concepts": [
            ("A connective is a table",
             "`¬`, `∧` and `∨` are each defined by what they do to truth values, "
             "row by row. English words such as &ldquo;and&rdquo; and &ldquo;or&rdquo; "
             "are used to read them, and where the words carry more than the table, "
             "the table wins."),
            ("Or includes both",
             "`p ∨ q` is true when `p` is true, when `q` is true, and when both are. "
             "It is false only when both are false. The exclusive reading, true when "
             "exactly one is true, is written `p ⊕ q`."),
            ("Compound sentences nest",
             "`¬p ∧ ¬q` negates each part and then joins them. A table for it has "
             "a column for each smaller piece, so that each column is read from "
             "the ones before it."),
        ],
        "read_title": "The tables",
        "read_intro": (
            "Four tables for two sentences, side by side, and the English each one "
            "usually carries."
        ),
        "body": [
            ("def", ("Negation",
                     "`¬p` is true when `p` is false and false when `p` is true. "
                     "&ldquo;It is not the case that&rdquo; is the safe English for "
                     "it.")),
            ("def", ("Conjunction",
                     "`p ∧ q` is true exactly when both `p` and `q` are true. "
                     "&ldquo;And&rdquo; is the usual word, and so, for truth value, "
                     "are &ldquo;but&rdquo; and &ldquo;although&rdquo;: they add a "
                     "contrast that the table does not record.")),
            ("def", ("Disjunction",
                     "`p ∨ q` is false exactly when both are false. It is "
                     "<strong>inclusive</strong>: true also when both are true.")),
            ("math", [
                "p   q  |  ¬p   p ∧ q   p ∨ q   p ⊕ q",
                "---------------------------------------",
                "T   T  |  F      T       T       F",
                "T   F  |  F      F       T       T",
                "F   T  |  T      F       T       T",
                "F   F  |  T      F       F       F",
            ]),
            ("p", "The two right-hand columns agree except in the first row. That row "
                  "is where English leaves a gap and logic closes it. &ldquo;You may "
                  "have soup or salad&rdquo; on a menu usually means one of them, so "
                  "the exclusive reading; &ldquo;you will be fined if you are late or "
                  "absent&rdquo; does not mean you escape the fine by being both, so "
                  "the inclusive reading. Logic picks the inclusive one and writes "
                  "the exclusive one separately."),
            ("p", "A compound formula is built up, and its table is built the same way. "
                  "For `¬p ∧ ¬q`, first fill the column for `¬p`, then the one for "
                  "`¬q`, then combine them. Only one row of the four makes it true: "
                  "`p` false and `q` false. This is the sentence &ldquo;neither `p` "
                  "nor `q`&rdquo;."),
            ("p", "In the lab, choose a formula for Formula A and read the table. The "
                  "lab spells the connectives with a tilde for not, an ampersand for "
                  "and, a vertical bar for or and a caret for exclusive or; the rows "
                  "and the verdicts are the same. Switch the menu to compare two "
                  "formulas, and the lab shows the rows where their columns differ."),
            ("example", ("Menu logic",
                         "A diner asks for soup and salad both and is told the menu "
                         "says soup or salad. If the menu's &ldquo;or&rdquo; is the "
                         "logician's, the diner has complied with it. If it is the "
                         "exclusive one, the diner has not. The sentence does not "
                         "say which, which is why contracts and laws that use "
                         "&ldquo;or&rdquo; often add &ldquo;or both&rdquo; or "
                         "&ldquo;but not both&rdquo;.")),
        ],
        "lab": ("truth_table", {
            "formulas": ["p & q", "p | q", "~p", "p ^ q", "~p & ~q"],
            "compare_with": "p ^ q",
            "mode": "one",
            "panel_title": "Inclusive or against exclusive or",
            "panel_intro": (
                "Pick the formula with the vertical bar and read its column. Then "
                "switch the menu to compare two formulas, set A to the vertical bar "
                "and B to the caret, and find the one row where they differ."
            ),
        }),
        "steps_title": "Building a table by hand",
        "steps_intro": "The same four steps for any compound sentence over two letters.",
        "steps": [
            ("List the cases",
             "Write the four rows for `p` and `q`: both true, `p` only, `q` only, "
             "neither. Always in the same order, so that columns can be compared."),
            ("Add a column for each smaller piece",
             "Work from the inside out. For `¬p ∧ ¬q`, the pieces are `¬p` and "
             "`¬q`, and only then the whole."),
            ("Fill each column from the ones it depends on",
             "A cell is decided by the definition of its connective and by the cells "
             "to its left. Never by what the English sounds like."),
            ("Read the answer in the last column",
             "The rows with T are the cases in which the whole sentence is true. Count "
             "them, and compare with another formula by comparing columns."),
        ],
        "worked": {
            "title": "Soup or salad",
            "intro": [
                "Let `p` be &ldquo;you have soup&rdquo; and `q` be &ldquo;you have "
                "salad&rdquo;. The menu says p or q.",
            ],
            "lines": [
                "soup  salad  |  inclusive (∨)   exclusive (⊕)",
                "T     T      |  T               F",
                "T     F      |  T               T",
                "F     T      |  T               T",
                "F     F      |  F               F",
            ],
            "after": [
                "Four rows, and the columns agree in three. The first row is the "
                "only place the menu's meaning matters: both soup and salad. On the "
                "inclusive reading it is allowed, and on the exclusive reading it is "
                "not. Everything else about the menu is settled by either reading.",
            ],
        },
        "quiz_title": "Reading the tables",
        "quiz": [
            {"q": "In how many of the four rows is `p ∨ q` true?",
             "a": ["One", "Two", "Three", "Four"],
             "c": 2,
             "why": "It is false only when both parts are false, so it is true in "
                    "the other three rows."},
            {"q": "A sign says &ldquo;staff or members only&rdquo;. Ana is both. "
                  "On the logician's reading of or, is she admitted?",
             "a": ["No, because or means one but not both",
                   "Yes, because `p ∨ q` is true when both parts are true",
                   "Only if she shows two cards",
                   "It cannot be decided from the table"],
             "c": 1,
             "why": "The table gives T in the row where both are true. Whether the "
                    "sign's author meant the exclusive reading is another matter, and "
                    "is why careful writers add &ldquo;but not both&rdquo;."},
            {"q": "For which assignment do `p ∨ q` and `p ⊕ q` have different values?",
             "a": ["`p` false, `q` false", "`p` true, `q` false",
                   "`p` false, `q` true", "`p` true, `q` true"],
             "c": 3,
             "why": "They agree in the two rows where exactly one part is true, and "
                    "in the row where both are false. Only when both are true does the "
                    "inclusive one say T and the exclusive one F."},
            {"q": "In which rows is `¬p ∧ ¬q` true?",
             "a": ["Only when `p` and `q` are both false",
                   "Whenever `p` is false",
                   "Whenever `p` and `q` differ",
                   "Whenever at least one of them is false"],
             "c": 0,
             "why": "A conjunction needs both parts true, so both `¬p` and `¬q`, so "
                    "both `p` and `q` false. When `p` is false and `q` true, `¬q` is "
                    "false and the whole is false."},
        ],
        "mistakes": [
            ("Reading &ldquo;or&rdquo; as exclusive",
             "In logic `p ∨ q` is true when both parts are true: the first row of "
             "the table says T. An exclusive reading belongs to a different "
             "connective, `p ⊕ q`, and the two columns differ in that one row. "
             "Reading `∨` as &ldquo;one or the other but not both&rdquo; will make a "
             "valid argument look invalid later in this course."),
            ("Treating &ldquo;but&rdquo; as something other than a conjunction",
             "&ldquo;She is clever but lazy&rdquo; carries a contrast, and the table "
             "for `p ∧ q` does not record it. For truth value, the sentence is true "
             "exactly when she is clever and she is lazy. Whatever else it suggests "
             "is not part of what the connective computes."),
            ("Reading a compound sentence in the wrong order",
             "`¬p ∧ q` negates `p` alone; `¬(p ∧ q)` negates the conjunction. The "
             "two have different tables, and the second is the subject of a lesson "
             "ahead. Parentheses decide the order, and a table is built one piece at "
             "a time to keep it visible."),
        ],
        "standard": (
            "Finish when you can build a table and say what each row means.",
            "Given a formula in `¬`, `∧` and `∨`, build its table row by row, state "
            "how many rows make it true, and point to the row where the inclusive and "
            "exclusive readings of or part."
        ),
        "note": (
            "Every connective in this lesson is truth-functional: the truth of the "
            "whole is fixed by the truth of the parts. Not every English connective "
            "is. Whether &ldquo;`p` because `q`&rdquo; is true depends on more than "
            "the truth of `p` and of `q`, so no table can be drawn for it, and this "
            "course treats &ldquo;because&rdquo; as a signpost in an argument rather "
            "than as a connective inside one."
        ),
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "the-conditional",
        "title": "The Conditional",
        "module": "Propositional logic",
        "one_line": "Fill the four rows of if-then and translate only if, unless, necessary and sufficient.",
        "summary": (
            "A conditional is false in exactly one row: the antecedent true and the "
            "consequent false. The other three rows are true, including both where "
            "the antecedent is false, and that is what a promise requires. The "
            "converse, which swaps the parts, is a different sentence."
        ),
        "key": [
            "p → q is false in one row only",
            "p true, q false: the promise is broken",
            "p → q  ≡  ¬p ∨ q",
            "p only if q:  p → q",
            "p if q:  q → p",
            "p unless q:  ¬q → p",
        ],
        "key_label": "The conditional, and what to do with it",
        "concepts_intro": (
            "If-then is the connective arguments are built from, and the one that "
            "feels wrong in the table. The feeling is worth examining."
        ),
        "concepts": [
            ("A promise is broken in one way",
             "&ldquo;If it rains, the match is off&rdquo; is broken when it rains "
             "and the match goes ahead. If it does not rain, nothing has been "
             "violated whether the match goes ahead or not. So the conditional is "
             "true in those rows."),
            ("The antecedent is the condition",
             "In `p → q`, `p` is the antecedent and `q` the consequent. The "
             "conditional says nothing about what happens when the antecedent is "
             "false, and a sentence that says nothing there cannot be false there."),
            ("The direction matters",
             "`p → q` and `q → p` are different sentences. The second is the "
             "converse, and the two disagree in the two rows where `p` and `q` "
             "have different values."),
        ],
        "read_title": "The table, and the words that point to it",
        "read_intro": (
            "One table, then the English phrases that translate into it and the ones "
            "that translate into its converse."
        ),
        "body": [
            ("def", ("The conditional",
                     "`p → q` (&ldquo;if `p` then `q`&rdquo;) is false exactly when "
                     "`p` is true and `q` is false, and true in the other three rows. "
                     "It is equivalent to `¬p ∨ q`.")),
            ("math", [
                "p   q  |  p → q   q → p   ¬p ∨ q",
                "-----------------------------------",
                "T   T  |    T       T        T",
                "T   F  |    F       T        F",
                "F   T  |    T       F        T",
                "F   F  |    T       T        T",
            ]),
            ("p", "The last column shows why the third and fourth rows, where `p` is "
                  "false, are T. `¬p ∨ q` is false only when `p` is true and `q` is "
                  "false, and the conditional was introduced to say exactly that: it "
                  "is ruled out that `p` holds without `q`. A sentence that rules out "
                  "one case and is silent about the rest is true in the rest."),
            ("p", "An independent check on the two rows where `p` is false: take the "
                  "claim that every number divisible by four is even. As a "
                  "conditional about a number `n`, it reads: if `n` is divisible by "
                  "four, then `n` is even. For `n = 6` the antecedent is false and "
                  "the consequent true; for `n = 3` both are false. The claim is "
                  "plainly true of all numbers, so it cannot be false at 6 or 3. If "
                  "the conditional were false, or had no value, whenever its "
                  "antecedent is false, every such claim would fail."),
            ("p", "Translation is mostly a matter of which part is which. These "
                  "phrases all say `p → q`:"),
            ("ul", [
                "if `p`, then `q`; `q` if `p`",
                "`p` only if `q`",
                "`p` is sufficient for `q`",
                "`q` is necessary for `p`",
            ]),
            ("p", "&ldquo;If&rdquo; and &ldquo;only if&rdquo; run opposite ways. "
                  "&ldquo;You may vote only if you are registered&rdquo; says that "
                  "voting requires registration, so `v → r`. &ldquo;You may vote if "
                  "you are registered&rdquo; says that registration is enough, so "
                  "`r → v`. &ldquo;`p` unless `q`&rdquo; says that if `q` fails then "
                  "`p`, so `¬q → p`."),
            ("p", "In the lab the first formula is the conditional, compared with "
                  "its form using or. The columns agree. Change B to the converse "
                  "and the lab marks the two rows that differ: `p` true with `q` "
                  "false, and `p` false with `q` true. A conditional and its converse "
                  "disagree in two rows, not one. The menu's last two formulas, which "
                  "negate both parts, are taken up in &ldquo;Equivalence, De Morgan "
                  "and Contraposition&rdquo;; for now, only count the rows in which "
                  "each differs from A."),
        ],
        "lab": ("truth_table", {
            "formulas": ["p -> q", "q -> p", "~p | q", "~q -> ~p", "~p -> ~q"],
            "compare_with": "~p | q",
            "mode": "two",
            "panel_title": "The conditional and its relatives",
            "panel_intro": (
                "Formula A starts as the conditional and Formula B as its form with "
                "or. They agree in every row. Now set B to the converse and then to "
                "the other two, and count the rows in which each differs from A."
            ),
        }),
        "steps_title": "Translating an if-then sentence",
        "steps_intro": "Decide which part is the condition before you decide the word.",
        "steps": [
            ("Name the two parts",
             "Give each simple sentence a letter: `p` for the part that would have "
             "to hold, `q` for the part that is promised."),
            ("Find the part that is required",
             "Ask which part the sentence says cannot fail while the other holds. "
             "That part is the consequent; the other part is the antecedent."),
            ("Choose the form from the word",
             "&ldquo;If&rdquo; introduces the antecedent. &ldquo;Only if&rdquo; "
             "introduces the consequent. &ldquo;Sufficient&rdquo; goes with the "
             "antecedent, &ldquo;necessary&rdquo; with the consequent."),
            ("Check the one false row",
             "A conditional is false only when the antecedent holds and the "
             "consequent fails. Describe that case in English and see whether it "
             "is the case the sentence forbids."),
        ],
        "worked": {
            "title": "The match is off",
            "intro": [
                "Let `r` be &ldquo;it rains&rdquo; and `m` be &ldquo;the match is "
                "off&rdquo;. The promise: if it rains, the match is off.",
            ],
            "lines": [
                "rain  off  |  r → m   what happened",
                "T     T    |  T       rain, match off: kept",
                "T     F    |  F       rain, match on: broken",
                "F     T    |  T       no rain, match off: kept",
                "F     F    |  T       no rain, match on: kept",
            ],
            "after": [
                "The third row is the one that looks odd. It did not rain and the "
                "match was called off anyway, perhaps because a ground was flooded. "
                "The promise was about what follows rain; it did not say the match "
                "would be on whenever it was dry. It was kept, so the sentence is "
                "true there.",
            ],
        },
        "quiz_title": "Rows and translations",
        "quiz": [
            {"q": "Which row makes `p → q` false?",
             "a": ["`p` false, `q` true", "`p` false, `q` false",
                   "`p` true, `q` false", "`p` true, `q` true"],
             "c": 2,
             "why": "A conditional is false only when its antecedent is true and its "
                    "consequent false. In the other three rows it is true."},
            {"q": "&ldquo;You may enter only if you have a ticket.&rdquo; Let `e` be "
                  "entering and `t` be having a ticket. Which formula is it?",
             "a": ["`t → e`", "`e → t`", "`e ∧ t`", "`e ↔ t`"],
             "c": 1,
             "why": "Entering requires a ticket, so a person who enters without one "
                    "breaks the rule: `e` true and `t` false falsifies `e → t`. The "
                    "first is the converse, and the last would also forbid a "
                    "ticket-holder who stays outside."},
            {"q": "&ldquo;If 2 + 2 = 5, then the moon is made of cheese.&rdquo; What "
                  "is its truth value?",
             "a": ["True, because its antecedent is false",
                   "False, because the two parts are unrelated",
                   "False, because the moon is not made of cheese",
                   "It has no truth value"],
             "c": 0,
             "why": "The antecedent is false, so the one falsifying row is not in "
                    "play. Relevance between the parts is not part of the table, "
                    "and a false consequent does not falsify a conditional whose "
                    "antecedent is false."},
            {"q": "In how many rows do `p → q` and its converse `q → p` differ?",
             "a": ["None", "One", "All four", "Two"],
             "c": 3,
             "why": "They differ where `p` and `q` have different values: `p` true "
                    "with `q` false, and `p` false with `q` true. In the other two "
                    "rows both are true."},
        ],
        "mistakes": [
            ("Thinking a conditional with a false antecedent is false, or has no value",
             "The table says T in both rows where the antecedent is false. Check it "
             "against a promise: if it does not rain, &ldquo;if it rains the match "
             "is off&rdquo; has not been broken, whatever happens to the match. "
             "And a general claim such as &ldquo;if a number is divisible by four it "
             "is even&rdquo; stays true at the numbers 3 and 6, where its "
             "antecedent is false."),
            ("Reversing &ldquo;only if&rdquo;",
             "&ldquo;`p` only if `q`&rdquo; is `p → q`, not `q → p`. &ldquo;Only "
             "if&rdquo; names the requirement. Voting only if registered makes "
             "registration necessary, and does not make it enough."),
            ("Taking the converse to say the same thing",
             "If a shape is a square it has four sides; if it has four sides it is "
             "a square. The first is true and the second false. The lab shows two "
             "rows where the two conditionals disagree, and in each of them one is "
             "true and the other false."),
        ],
        "standard": (
            "Finish when you can fill the table and translate without guessing.",
            "Fill in the four rows of `p → q` from memory, translate a sentence "
            "using only if, unless, necessary or sufficient, and give the row where "
            "a conditional and its converse have different values."
        ),
        "note": (
            "This is the conditional of logic. Ordinary if-then sometimes means more "
            "(a causal link, a counterfactual), and Science, Induction and Causation "
            "returns to that. Nothing in this course needs more than the table."
        ),
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "validity-by-truth-table",
        "title": "Validity by Truth Table",
        "module": "Propositional logic",
        "one_line": "Lay premises and conclusion in one table, and find or rule out the counterexample row.",
        "summary": (
            "An argument is valid when no row of its table makes every premise true "
            "and the conclusion false. The lab finds such rows, and names four forms "
            "on sight: two valid, modus ponens and modus tollens, and two invalid, "
            "affirming the consequent and denying the antecedent."
        ),
        "key": [
            "invalid: a row with premises T, conclusion F",
            "p → q, p ∴ q    modus ponens: valid",
            "p → q, ¬q ∴ ¬p  modus tollens: valid",
            "p → q, q ∴ p    affirming the consequent",
            "p → q, ¬p ∴ ¬q  denying the antecedent",
        ],
        "key_label": "One test, four familiar forms",
        "concepts_intro": (
            "The test is the same for every argument over a few simple sentences: "
            "write every row, and look at the rows where all premises hold."
        ),
        "concepts": [
            ("Only some rows count",
             "A row can refute an argument only if every premise is true in it. "
             "Rows in which a premise is false tell you nothing about the argument, "
             "because the argument promises nothing there."),
            ("One row is enough",
             "A single counterexample row makes the argument invalid. Validity needs "
             "every row examined; invalidity needs one."),
            ("Validity belongs to the form",
             "Replace `p` and `q` with any sentences you like and the verdict does "
             "not change. That is why the four forms have names."),
        ],
        "read_title": "The counterexample row",
        "read_intro": (
            "A definition from the last two lessons, put to work on four arguments."
        ),
        "body": [
            ("p", "A counterexample is a row, and only a row. It is an assignment of "
                  "truth values to the simple sentences under which every premise "
                  "comes out true and the conclusion comes out false; nothing about "
                  "the world is being claimed, only that such a case is describable. "
                  "So an argument is valid when no such row exists, and invalid when "
                  "one does, and the second verdict needs exactly one row to "
                  "establish it. For `p → q, q ∴ p` the lab finds the row `p = F, "
                  "q = T`: the premises hold, the conclusion fails, and no argument "
                  "about the other three rows can rescue the form &mdash; which is "
                  "why &ldquo;if God exists life has meaning; life has meaning; so "
                  "God exists&rdquo; is settled by a table and not by theology."),
            ("math", [
                "p   q  |  p → q   p   q",
                "--------------------------",
                "T   T  |    T     T   T      premises T, conclusion T",
                "T   F  |    F     T   F      a premise is F",
                "F   T  |    T     F   T      a premise is F",
                "F   F  |    T     F   F      a premise is F",
            ]),
            ("p", "That is modus ponens: premises `p → q` and `p`, conclusion `q`. "
                  "The columns shown are the two premises and the conclusion. Only "
                  "the first row has every premise true, and there the conclusion is "
                  "true. The other rows have a false premise and are irrelevant. No "
                  "counterexample, so valid."),
            ("math", [
                "p   q  |  p → q   q   p",
                "--------------------------",
                "T   T  |    T     T   T      no counterexample",
                "T   F  |    F     F   T      a premise is F",
                "F   T  |    T     T   F      COUNTEREXAMPLE",
                "F   F  |    T     F   F      a premise is F",
            ]),
            ("p", "That is the same table for affirming the consequent, `p → q` and "
                  "`q`, concluding `p`. Two rows have both premises true, and in the "
                  "second of them the conclusion is false. One row is enough."),
            ("thm", ("The four forms",
                     "Modus ponens (`p → q`, `p`, so `q`) and modus tollens (`p → q`, "
                     "`¬q`, so `¬p`) are valid. Affirming the consequent (`p → q`, "
                     "`q`, so `p`) and denying the antecedent (`p → q`, `¬p`, so "
                     "`¬q`) are invalid, and each is refuted by the row `p = F, "
                     "q = T`.")),
            ("p", "The pair that look alike are the pair that differ. Modus tollens "
                  "denies the consequent and concludes against the antecedent; "
                  "denying the antecedent starts from the wrong end. If you cannot "
                  "tell which you are looking at, build the table."),
            ("p", "In the lab, choose each of the four presets. It lists the rows, "
                  "marks any counterexample row, and names the form from a catalogue. "
                  "The name is looked up from the shape of the formulas, not from "
                  "what the sentences mean, so an argument with the same shape and "
                  "different subject matter is named the same way."),
        ],
        "lab": ("argkit", {
            "mode": "validity",
            "preset": "mp",
            "show": "all",
            "presets": [
                {"id": "mp", "label": "modus ponens: p → q, p, so q",
                 "premises": ["p -> q", "p"], "conclusion": "q", "expect": {"vaVerdict": "Valid", "vaForm": "modus ponens", "vaCounter": "0"}},
                {"id": "mt", "label": "modus tollens: p → q, ¬q, so ¬p",
                 "premises": ["p -> q", "~q"], "conclusion": "~p", "expect": {"vaVerdict": "Valid", "vaForm": "modus tollens", "vaCounter": "0"}},
                {"id": "ac", "label": "affirming the consequent: p → q, q, so p",
                 "premises": ["p -> q", "q"], "conclusion": "p", "expect": {"vaVerdict": "Invalid", "vaForm": "affirming the consequent", "vaCounter": "1"}},
                {"id": "da", "label": "denying the antecedent: p → q, ¬p, so ¬q",
                 "premises": ["p -> q", "~p"], "conclusion": "~q", "expect": {"vaVerdict": "Invalid", "vaForm": "denying the antecedent", "vaCounter": "1"}},
            ],
            "panel_title": "Four forms, four tables",
            "panel_intro": (
                "For each preset, find the rows in which every premise is true, and "
                "read the conclusion in them. Then switch the display to counterexample "
                "rows only and see what is left."
            ),
        }),
        "steps_title": "Testing an argument by table",
        "steps_intro": "Five steps; the fourth is the one that does the work.",
        "steps": [
            ("Translate the argument",
             "Give each simple sentence a letter, write each premise and the "
             "conclusion as a formula, and keep the same letters throughout."),
            ("List every row",
             "`n` letters give `2ⁿ` rows. List them in a fixed order, and add a "
             "column for each premise and for the conclusion."),
            ("Fill the columns",
             "Evaluate each premise and the conclusion in every row, from the "
             "connective definitions."),
            ("Look only at rows where every premise is true",
             "In each such row, read the conclusion. A row where it is false is "
             "a counterexample; the argument is invalid and you can stop."),
            ("If no row survives, the argument is valid",
             "Every row where the premises hold has a true conclusion, or no row "
             "has the premises all true. Both count as valid."),
        ],
        "worked": {
            "title": "Life has meaning",
            "intro": [
                "Let `p` be &ldquo;God exists&rdquo; and `q` be &ldquo;life has "
                "meaning&rdquo;. If God exists, life has meaning; life has meaning; "
                "so God exists.",
            ],
            "lines": [
                "premises:   p → q ,  q          conclusion:  p",
                "row  p  q  |  p → q  q  |  p",
                "1    T  T  |    T     T  |  T",
                "2    T  F  |    F     F  |  T",
                "3    F  T  |    T     T  |  F    counterexample",
                "4    F  F  |    T     F  |  F",
            ],
            "after": [
                "Row 3 makes both premises true and the conclusion false: there is no "
                "God, and life has meaning anyway. The argument is invalid, "
                "affirming the consequent. This does not show that God does not "
                "exist, or that the premises are false; it shows that these "
                "premises do not settle the conclusion.",
            ],
        },
        "quiz_title": "Counterexample rows",
        "quiz": [
            {"q": "For `p → q, q ∴ p`, which row is the counterexample?",
             "a": ["`p` true, `q` true", "`p` true, `q` false",
                   "`p` false, `q` true", "`p` false, `q` false"],
             "c": 2,
             "why": "Both premises, `p → q` and `q`, are true when `p` is false and "
                    "`q` true, and the conclusion `p` is false. In the row `p` "
                    "false, `q` false the premise `q` is false."},
            {"q": "Which argument is modus tollens?",
             "a": ["If it rains the street is wet; it rained; so the street is wet",
                   "If it rains the street is wet; the street is not wet; so it did "
                   "not rain",
                   "If it rains the street is wet; the street is wet; so it rained",
                   "If it rains the street is wet; it did not rain; so the street is "
                   "not wet"],
             "c": 1,
             "why": "Modus tollens denies the consequent and concludes the denial of "
                    "the antecedent. The first is modus ponens, the third affirms "
                    "the consequent and the fourth denies the antecedent."},
            {"q": "A row of an argument's table has a false premise and a true "
                  "conclusion. What does it show?",
             "a": ["That the argument is invalid",
                   "That the conclusion is true in the world",
                   "That the argument is valid",
                   "Nothing either way, since only rows with every premise true can "
                   "refute"],
             "c": 3,
             "why": "The row cannot be a counterexample, which needs every premise "
                    "true. It cannot show validity either, since validity needs all "
                    "rows checked."},
            {"q": "&ldquo;If the butler did it he had a key; he had a key; so the "
                  "butler did it.&rdquo; What is the verdict?",
             "a": ["Invalid: he may have had a key without doing it, and then both "
                   "premises hold and the conclusion fails",
                   "Valid: it is modus ponens",
                   "Valid: both premises are plausible",
                   "Valid: denying the conclusion contradicts a premise"],
             "c": 0,
             "why": "It affirms the consequent. The row where he had a key and did "
                    "not do it is a counterexample. The other choices all call a "
                    "form valid that has a counterexample row."},
        ],
        "mistakes": [
            ("Counting a row with false premises and a false conclusion as a counterexample",
             "A counterexample needs every premise true and the conclusion false. In "
             "the table for affirming the consequent the row `p` false, `q` false "
             "has a false conclusion, but its second premise `q` is false too, so "
             "the argument promises nothing there. Only the row `p` false, `q` true "
             "refutes it."),
            ("Treating the lab's name for a form as the verdict",
             "The name is looked up from the shape of the formulas. The verdict is "
             "computed from the rows. They agree, and if they ever seemed not to, "
             "trust the rows: the table is the definition."),
            ("Concluding the conclusion is false because the argument is invalid",
             "A counterexample row shows that the premises do not guarantee the "
             "conclusion. The conclusion may be true anyway. &ldquo;God exists&rdquo; "
             "is not refuted by a bad argument for it, any more than it is "
             "established by a good one."),
        ],
        "standard": (
            "Finish when you can produce the row, not just the verdict.",
            "Given an argument over two or three letters, write its table, mark the "
            "rows where every premise is true, name the counterexample row if there is "
            "one, and name the form if it is one of the four."
        ),
        "note": (
            "A table has `2ⁿ` rows, so this method is practical for a handful of "
            "sentences and hopeless for a hundred. Later lessons keep the number of "
            "letters small, and the lab refuses more than six."
        ),
    },
    # ---------------------------------------------------------------- 06
    {
        "slug": "equivalence-de-morgan-and-contraposition",
        "title": "Equivalence, De Morgan and Contraposition",
        "module": "Propositional logic",
        "one_line": "Decide whether two sentences say the same thing by comparing their columns.",
        "summary": (
            "Two sentences are equivalent when their columns agree in every row. "
            "De Morgan's laws turn &ldquo;not both&rdquo; into &ldquo;at least one "
            "not&rdquo; and &ldquo;neither&rdquo; into &ldquo;both not&rdquo;. The "
            "contrapositive of a conditional is equivalent to it; the converse and "
            "the inverse are not."
        ),
        "key": [
            "equivalent: the columns agree in every row",
            "¬(p ∧ q)  ≡  ¬p ∨ ¬q    not both",
            "¬(p ∨ q)  ≡  ¬p ∧ ¬q    neither",
            "p → q  ≡  ¬q → ¬p       contrapositive",
            "not equivalent: q → p, ¬p → ¬q",
        ],
        "key_label": "Three equivalences, two impostors",
        "concepts_intro": (
            "Two sentences that agree in every row can be swapped in any argument "
            "without changing its verdict. That makes equivalence worth checking."
        ),
        "concepts": [
            ("Equivalence is agreement in every row",
             "Write the two columns side by side. If any row has a T in one and "
             "an F in the other, the sentences are not equivalent, and that row is "
             "the proof."),
            ("Negation flips the connective",
             "To negate a conjunction, negate the parts and switch to or; to "
             "negate a disjunction, negate the parts and switch to and. Negating "
             "the parts alone gets the connective wrong."),
            ("A conditional has one equivalent turn",
             "From `p → q` there are three rewritings. Only the contrapositive "
             "`¬q → ¬p` keeps the table. The converse `q → p` and the inverse "
             "`¬p → ¬q` change it."),
        ],
        "read_title": "Same columns, same sentence",
        "read_intro": (
            "Three equivalences to know, each checked by a table, and the near "
            "misses that look like them."
        ),
        "body": [
            ("def", ("Equivalence",
                     "Two formulas are <strong>equivalent</strong>, written `A ≡ B`, "
                     "when they have the same truth value in every row. One row "
                     "with different values shows they are not.")),
            ("thm", ("De Morgan",
                     "`¬(p ∧ q) ≡ ¬p ∨ ¬q` and `¬(p ∨ q) ≡ ¬p ∧ ¬q`. In words: "
                     "&ldquo;not both&rdquo; is &ldquo;at least one is not&rdquo;, "
                     "and &ldquo;neither&rdquo; is &ldquo;both are not&rdquo;.")),
            ("math", [
                "p   q  |  ¬(p ∧ q)   ¬p ∨ ¬q   ¬p ∧ ¬q   ¬(p ∨ q)",
                "-----------------------------------------------------",
                "T   T  |     F          F          F          F",
                "T   F  |     T          T          F          F",
                "F   T  |     T          T          F          F",
                "F   F  |     T          T          T          T",
            ]),
            ("p", "Compare the columns. The first two agree in all four rows, which "
                  "is the first law. The last two agree in all four, which is the "
                  "second. The first and third do not agree: they differ in the "
                  "second and third rows, which is why &ldquo;not both&rdquo; and "
                  "&ldquo;neither&rdquo; are different claims. Not both is satisfied "
                  "when exactly one holds; neither is not."),
            ("p", "The contrapositive is a second, separate equivalence. For a "
                  "conditional `p → q`, the contrapositive is `¬q → ¬p`: swap the "
                  "parts and negate each. The converse swaps only (`q → p`) and the "
                  "inverse negates only (`¬p → ¬q`). The lab sets the conditional "
                  "against all three."),
            ("math", [
                "p   q  |  p → q   ¬q → ¬p   q → p   ¬p → ¬q",
                "---------------------------------------------",
                "T   T  |    T         T         T         T",
                "T   F  |    F         F         T         T",
                "F   T  |    T         T         F         F",
                "F   F  |    T         T         T         T",
            ]),
            ("p", "The contrapositive column is the conditional's column. The converse "
                  "and inverse columns are the same as each other, and differ from "
                  "the conditional in the second and third rows. So a conditional "
                  "and its contrapositive stand or fall together, which is why a "
                  "proof of one is a proof of the other, and why modus tollens is "
                  "valid."),
            ("example", ("A sentence and its contrapositive",
                         "&ldquo;If a shape is a square, it has four sides&rdquo; and "
                         "&ldquo;if a shape does not have four sides, it is not a "
                         "square&rdquo; say the same thing. The converse, &ldquo;if "
                         "it has four sides it is a square&rdquo;, is false of a "
                         "rectangle that is not a square.")),
        ],
        "lab": ("truth_table", {
            "formulas": ["~(p & q)", "~p | ~q", "~p & ~q", "~(p | q)",
                         "p -> q", "~q -> ~p", "q -> p"],
            "compare_with": "~p | ~q",
            "mode": "two",
            "panel_title": "Equivalent, or separated by a row",
            "panel_intro": (
                "Formula A starts as not both and Formula B as at least one not; they "
                "agree everywhere. Change B to the sentence that negates each part "
                "but keeps and, and read the rows that separate them. Then compare "
                "the conditional with each of its three rewritings."
            ),
        }),
        "steps_title": "Deciding whether two sentences are equivalent",
        "steps_intro": "The test is the same every time; only the formulas change.",
        "steps": [
            ("Put both formulas in the same table",
             "Use the same letters in the same order, so that every row means the "
             "same case for both."),
            ("Compare the last columns row by row",
             "Look for any row where one says T and the other F. You are looking for "
             "one disagreement, and need no more."),
            ("If you find one, the sentences are not equivalent",
             "Report the row. It is an assignment under which one sentence is true "
             "and the other false, and it is the whole proof."),
            ("If you find none, they are equivalent",
             "All rows agree. Either can replace the other in any argument."),
        ],
        "worked": {
            "title": "Rich and famous",
            "intro": [
                "&ldquo;It is not the case that she is both rich and famous.&rdquo; "
                "Let `r` be &ldquo;she is rich&rdquo; and `f` be &ldquo;she is "
                "famous&rdquo;.",
            ],
            "lines": [
                "r  f  |  ¬(r ∧ f)   ¬r ∨ ¬f   ¬r ∧ ¬f",
                "T  T  |     F          F          F",
                "T  F  |     T          T          F",
                "F  T  |     T          T          F",
                "F  F  |     T          T          T",
            ],
            "after": [
                "The first two columns agree in all four rows, so &ldquo;not both "
                "rich and famous&rdquo; is &ldquo;not rich or not famous&rdquo;. The "
                "third column does not: in the second row she is rich but not famous, "
                "the sentence is true, and &ldquo;she is neither&rdquo; is false.",
            ],
        },
        "quiz_title": "Equivalent or not",
        "quiz": [
            {"q": "Which sentence is equivalent to &ldquo;it is not the case that she "
                  "is both rich and famous&rdquo;?",
             "a": ["She is not rich and she is not famous",
                   "She is not rich or she is not famous",
                   "She is rich or she is famous",
                   "She is not rich"],
             "c": 1,
             "why": "By De Morgan, `¬(r ∧ f)` is `¬r ∨ ¬f`. The first choice is "
                    "&ldquo;neither&rdquo;, which is false if she is rich and not "
                    "famous."},
            {"q": "What is the contrapositive of &ldquo;if a shape is a square, it "
                  "has four sides&rdquo;?",
             "a": ["If a shape has four sides, it is a square",
                   "If a shape is not a square, it does not have four sides",
                   "A shape is a square and does not have four sides",
                   "If a shape does not have four sides, it is not a square"],
             "c": 3,
             "why": "Swap the parts and negate each. The first is the converse, "
                    "the second the inverse, and the third is the negation of the "
                    "conditional, not a rewriting of it."},
            {"q": "Two formulas agree in three rows and differ in one. What follows?",
             "a": ["They are not equivalent; one row is enough",
                   "They are equivalent most of the time, so equivalent",
                   "They are equivalent, since the differing row may be an exception",
                   "Nothing, until a fifth row is added"],
             "c": 0,
             "why": "Equivalence means agreement in every row, so one disagreement "
                    "decides it. There are no exceptions to carve out."},
            {"q": "Which formula is equivalent to &ldquo;neither `p` nor `q`&rdquo;?",
             "a": ["`¬p ∨ ¬q`", "`¬(p ∧ q)`", "`¬(p ∨ q)`", "`¬p ∨ q`"],
             "c": 2,
             "why": "Neither is the negation of the or. It is true in one row, "
                    "both false. The first two are &ldquo;not both&rdquo;, true in "
                    "three rows, and the last is a different sentence again."},
        ],
        "mistakes": [
            ("Writing ¬(p ∧ q) as ¬p ∧ ¬q",
             "Negating the parts is not enough: the connective flips. In the row "
             "where `p` is true and `q` false, `¬(p ∧ q)` is true and `¬p ∧ ¬q` is "
             "false. The correct partner of &ldquo;not both&rdquo; is `¬p ∨ ¬q`, "
             "whose column the lab shows agreeing in all four rows."),
            ("Offering the converse or inverse as the contrapositive",
             "Of the three rewritings of `p → q`, only `¬q → ¬p` has the same "
             "table. The converse and inverse each differ from it in two rows. "
             "&ldquo;If it is a square it has four sides&rdquo; is true and its "
             "converse is not."),
            ("Treating &ldquo;not both&rdquo; and &ldquo;neither&rdquo; as one claim",
             "`¬(p ∧ q)` is true in three rows and `¬(p ∨ q)` in one. They differ "
             "when exactly one of `p`, `q` is true. A claim that she is not both "
             "rich and famous is made true by her being rich only."),
        ],
        "standard": (
            "Finish when you can negate and rewrite with a reason.",
            "Given two formulas, decide whether they are equivalent by comparing "
            "columns and name a separating row if not; negate a conjunction or a "
            "disjunction by De Morgan; and write a conditional's contrapositive "
            "without producing its converse or its inverse."
        ),
        "note": (
            "Equivalent sentences are interchangeable inside an argument without "
            "changing its verdict. That is how a long sentence is replaced by a short "
            "one in the lessons ahead, and how an invalid-looking argument is "
            "recognised as modus tollens."
        ),
    },
]
