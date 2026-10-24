"""Classical Prejudices, lessons 1-5 -- the Introduction, Smith pp. 3-74.

Every quotation is copied from Colin Smith's translation, Routledge Classics
pagination; the comment beside each lesson gives its pages. Smith's ligatures
are printed as plain letters, a word split by a line-break hyphen is joined,
footnote numerals are left out, and Smith's single quote marks inside a
quotation are printed as single quotes. Nothing else is changed.

Chapter I is two lessons (pure sensation, pp. 3-7; the constancy hypothesis,
pp. 6-14); Chapters II, III and IV are one lesson each. The ship on the shore
is in Chapter II (p. 20), not III; the lesson on judgement borrows it, and says
so.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # Smith p. 4 (opening passage: "Let us imagine a white patch ... 'shape'"
    # and "The perceptual 'something' ... 'field'"; "Each part arouses ...";
    # "It is the very definition ..."); p. 3 ("undifferentiated, instantaneous,
    # dotlike impact"; the greyness behind closed eyes; the ape and the hen,
    # p. 4); p. 5 (the red patch on the carpet, the woolly red, the experience
    # error, "We make perception out of things perceived"); p. 6 (the two ways
    # of mistaking quality; the retina and the zone of blackness); p. 7 ("We
    # must recognize the indeterminate ..."; attention as an auxiliary
    # hypothesis). Wertheimer's laws: Chapter II, p. 19 and n. 4.
    {
        "slug": "the-idea-of-pure-sensation",
        "title": "The Idea of Pure Sensation",
        "module": "Introduction · I · Sensation",
        "one_line": "The simplest thing perception gives is not a dot of sensation but a figure on a ground, and a sensation with no field around it is something no one has ever perceived.",
        "summary": (
            "The Introduction opens by testing the idea that perception is built from "
            "sensations, and finds that the simplest perceived thing is already a figure on a "
            "background. Compute how the Gestalt proximity rule groups a row of dots, and say "
            "what a pure-sensation account would have to add to get groups that are in no "
            "single dot."
        ),
        "key": [
            "sensation: an impact with no meaning",
            "simplest given: a figure on a ground",
            "perceived: always within a field",
            "experience error: things into mind",
            "gaps: next dot minus this dot",
            "split where gap ≥ ratio × smallest",
        ],
        "key_label": "The first chapter's opening in six lines",
        "concepts_intro": (
            "The chapter tries out two definitions of sensation and finds each borrowed from "
            "the perceived object. Three ideas carry its first five pages."
        ),
        "concepts": [
            ("Pure sensation",
             "The idea of a unit of experience before any meaning: being affected by a state of "
             "oneself, as by the grey that surrounds you when you close your eyes, or by a "
             "point of red that signifies nothing. The chapter takes it as empiricism's starting "
             "point and asks whether anyone has ever had one."),
            ("Figure and ground",
             "The Gestalt psychologists' finding that what perception gives first is a shape "
             "standing out from a background, its edges belonging to the shape and the "
             "background running on beneath it. The chapter makes it the definition of "
             "perception, not one fact about it."),
            ("The experience error",
             "A psychologists' name for a habit of analysis: taking what we know to be in "
             "things as if it were in our consciousness of them, so that the coloured object "
             "becomes a coloured sensation."),
        ],
        "read_title": "The passage first, then the chapter's first five pages line by line",
        "read_intro": (
            "The passage is the chapter's first example, a white patch on a plain background. "
            "The lesson reads it, goes back to the chapter's first page, and follows the "
            "argument to the point where it turns to physiology."
        ),
        "body": [
            ("p", "<strong>Introduction, Chapter 1, p. 4.</strong> &ldquo;Let us imagine a "
                  "white patch on a homogeneous background. All the points in the patch have a "
                  "certain &lsquo;function&rsquo; in common, that of forming themselves into a "
                  "&lsquo;shape&rsquo;. &hellip; The perceptual &lsquo;something&rsquo; is "
                  "always in the middle of something else, it always forms part of a "
                  "&lsquo;field&rsquo;.&rdquo; The sentences are from page 4 of Colin Smith's "
                  "translation, in the chapter Smith titles The &lsquo;Sensation&rsquo; as a "
                  "Unit of Experience. Read from the chapter's first page, 3, to the paragraph "
                  "on page 7 that turns to the physiologist's definition of sensation, in your "
                  "own copy before going on; the lesson goes back through it a phrase at a time."),
            ("p", "The Introduction is where the book clears the ground. Merleau-Ponty names "
                  "two theories of perception he will spend the rest of it answering. "
                  "<em>Empiricism</em>, the tradition that runs from Locke and Hume to the "
                  "laboratory psychology of his own day, holds that perception is built from "
                  "sensations caused by stimuli and joined by association. "
                  "<em>Intellectualism</em>, the tradition of Descartes and Kant and, in his "
                  "France, of the philosophers Lagneau and Alain, holds that perception is a "
                  "judgement the mind makes about such sensations. The first three chapters "
                  "take the two in turn, beginning where both begin: with the sensation."),
            ("p", "The chapter's first sentence finds the notion in ordinary language. I have "
                  "a sensation of redness, of blue, of heat, and nothing seems more obvious. "
                  "Nothing, the chapter says, is in fact more confused. Take sensation first as "
                  "the way I am affected: the grey that surrounds me when I close my eyes, the "
                  "sounds that hum in my head as I fall asleep. Pure sensation would then be "
                  "the experience of an &ldquo;undifferentiated, instantaneous, dotlike "
                  "impact&rdquo;, prior even to red and blue, since two colours told apart "
                  "already form a picture in front of me. The authors agree, Merleau-Ponty "
                  "says, that nothing in experience corresponds to it; even the simplest "
                  "perceptions of an ape or a hen bear on relationships, not on absolute "
                  "terms. His question is why theory still feels entitled to a layer of pure "
                  "impressions underneath."),
            ("p", "That is where the passage comes in. Every point of the white patch shares "
                  "one function, forming a shape. The shape's colour is more intense and as it "
                  "were firmer than the background's; its edges belong to it and not to the "
                  "background they touch; the patch lies on the background without breaking it. "
                  "And each part, in the passage's words, &ldquo;arouses the expectation of more "
                  "than it contains&rdquo;, so the most elementary perception is already charged "
                  "with a meaning. Then "
                  "an objection, in the empiricist's voice: if the shape and the ground are not "
                  "sensed as wholes, they must be sensed point by point. The reply is that each "
                  "point, in its turn, can be perceived only as a figure on a background."),
            ("def", ("Figure and ground",
                     "A figure is what stands out in a field, bounded and owning its edges; the "
                     "ground is what it stands out from, without bounds and continuing beneath "
                     "it. On the chapter's account there is no perceiving below this level.")),
            ("p", "The finding is the Gestalt psychologists'. Max Wertheimer, Wolfgang Köhler "
                  "and Kurt Koffka, working in Germany from the 1910s, argued that perception "
                  "is of organised wholes, <em>Gestalten</em>, which are not sums of their "
                  "parts. Merleau-Ponty takes their result and goes one step further. Gestalt "
                  "theory says that a figure on a background is the simplest thing the senses "
                  "give us; he replies that this is not a contingent fact about perception, "
                  "which would leave an ideal analysis free to posit impressions beneath it, to set them down as there. "
                  "&ldquo;It is the very definition of the phenomenon of perception&rdquo;, "
                  "without which a phenomenon cannot be called perception at all. A field "
                  "offering nothing to perceive cannot be perceived."),
            ("p", "The lab computes the proximity rule, the first of the laws Wertheimer set "
                  "out in 1923, on dots in a row. The <code>pairs</code> preset puts dots at "
                  "0, 1, 4, 5, 8 and 9. The gaps tile lists the distances between neighbours, "
                  "1, 3, 1, 3, 1. The lesson's rule is that a gap at least twice the smallest "
                  "gap separates two groups; the ratio 2 is the lesson's choice, not "
                  "Wertheimer's figure. Here the smallest gap is 1, so every gap of 3 "
                  "separates, and the groups tile prints <code>{0, 1} {4, 5} {8, 9}</code>: "
                  "three pairs, which the count tile gives as 3. Look at what the rule had to "
                  "use. No dot carries the word pair; a pair is a relation between two dots and "
                  "the space on either side of them."),
            ("p", "The other two presets make the point harder to miss. In <code>even</code> "
                  "the dots stand at 0, 2, 4, 6 and 8; every gap is 2, the smallest gap is "
                  "2, nothing reaches 4, and the rule makes one group of five. In "
                  "<code>shift</code> one dot of the pairs row moves, from 5 to 6. The gaps "
                  "become 1, 3, 2, 2, 1, every gap of 2 or more now separates, and the rule "
                  "gives <code>{0, 1} {4} {6} {8, 9}</code>, four groups. The dot at 4 did not "
                  "move, and it has lost its partner. Whatever a dot is, its membership of a "
                  "group is not in it. A pure-sensation account would have to add, to its dots, "
                  "a law of arrangement that no dot contains, and that is the first sign that "
                  "the unit is a construction."),
            ("p", "The chapter's second definition fares no better. Perhaps to sense is simply "
                  "to have qualities, to have seen a red or heard an A. But red and green are not "
                  "sensations; they are the sensed, and quality is a property of the object. "
                  "The red patch on the carpet is red only through the shadow that lies across "
                  "it and the play of light on it; it is a colour at all only over an area of a "
                  "certain size; and it would not be the same red if it were not the woolly red "
                  "of a carpet, a phrase the chapter takes from Jean-Paul Sartre's book on the imagination. A critic may answer that "
                  "this is true of qualities overlaid with knowledge, and that a pure quality "
                  "can still be conceived. The chapter's reply is that a pure quality is what "
                  "pure sensation was, a sensation of nothing, and so no sensation."),
            ("p", "Why, then, does the idea seem obvious? Because we have long been given "
                  "objects that are coloured or that sound, and when we analyse perception we "
                  "move those objects into consciousness. Psychologists call it the experience "
                  "error. &ldquo;We make perception out of things perceived.&rdquo; And because "
                  "the things are reached only through perception, we end by understanding "
                  "neither. There are two ways to go wrong about a quality, the chapter says: to "
                  "make it an element of consciousness when it is an object for consciousness, "
                  "and to think that, at the level of quality, its meaning is already fully "
                  "determinate. Both come from the same prejudice about the world."),
            ("p", "The second error has a test the reader can try. Build, with optics and "
                  "geometry, the part of the world that can throw its image on the retina at "
                  "this moment. On that construction you ought to perceive a sharply bounded "
                  "segment, packed with qualities and surrounded by blackness. Experience offers "
                  "nothing like it. The edge of the visual field is neither black nor grey, and "
                  "what is behind your back is not without some visual presence. The "
                  "psychologists' way out is to say the field is determinate in itself and only "
                  "unnoticed through inattention, which makes attention an auxiliary hypothesis "
                  "evolved to save the objective world. The chapter's answer is one sentence: "
                  "&ldquo;We must recognize the indeterminate as a positive phenomenon.&rdquo;"),
            ("p", "Go back to the dots with that in mind. The lab states the proximity rule as "
                  "a rule over measured positions, gaps in units on a ruler. The next chapter "
                  "warns that this is the psychologist's way of talking, and that read this way "
                  "Wertheimer's laws can smuggle the associationist's objective contiguity back "
                  "in as the cause of the grouping. So the figures show something modest and "
                  "exact: that the groups the rule computes are in no single dot. They do not "
                  "show what anyone sees, and they put the measured dots first, which is the "
                  "order the chapter says perception does not follow."),
            ("p", "The chapter now turns from experience to physiology, to the theory that "
                  "each stimulus produces its own sensation wherever it falls. The next lesson, "
                  "“The Constancy Hypothesis”, reads that theory and the figure of "
                  "two lines with arrowheads that it cannot account for."),
        ],
        "lab": ("phenkit", {
            "mode": "grouping",
            "view": "proximity",
            "model": "the Gestalt proximity rule (Wertheimer, 1923)",
            "preset": "pairs",
            "presets": [
                {"id": "pairs",
                 "label": "Dots at 0, 1, 4, 5, 8, 9 (illustrative)",
                 "points": [0, 1, 4, 5, 8, 9], "ratio": 2,
                 "expect": {"grGaps": "1, 3, 1, 3, 1", "grGroups": "{0, 1} {4, 5} {8, 9}",
                            "grCount": "3"}},
                {"id": "even",
                 "label": "Dots evenly spaced at 0, 2, 4, 6, 8 (illustrative)",
                 "points": [0, 2, 4, 6, 8], "ratio": 2,
                 "expect": {"grGaps": "2, 2, 2, 2", "grGroups": "{0, 2, 4, 6, 8}",
                            "grCount": "1"}},
                {"id": "shift",
                 "label": "The pairs row with the dot at 5 moved to 6 (illustrative)",
                 "points": [0, 1, 4, 6, 8, 9], "ratio": 2,
                 "expect": {"grGaps": "1, 3, 2, 2, 1", "grGroups": "{0, 1} {4} {6} {8, 9}",
                            "grCount": "4"}},
            ],
            "panel_title": "Grouping by proximity",
            "panel_intro": (
                "This lab computes the Gestalt proximity rule, Wertheimer's law of 1923, as the "
                "lesson states it: dots on a line separate into groups wherever a gap is at "
                "least the ratio times the smallest gap. The positions and the ratio are "
                "illustrative. It prints the gaps, the groups and their number, which are "
                "relations among the dots and in no single one of them."
            ),
        }),
        "steps_title": "Computing the groups proximity predicts",
        "steps_intro": "Four steps, the last of which is the lesson's.",
        "steps": [
            ("Order the positions and take the gaps",
             "Write the dots' positions from left to right and subtract each from the next. A "
             "row of six dots has five gaps."),
            ("Set the threshold",
             "Multiply the smallest gap by the ratio. With ratio 2 and a smallest gap of 1, "
             "any gap of 2 or more separates."),
            ("Cut the row",
             "Start a new group after every gap at or above the threshold, and count the "
             "groups. Every dot belongs to exactly one."),
            ("Find what is in no dot",
             "Name what the computation used besides the dots one by one: the gaps between "
             "them and a rule comparing the gaps. That is what a pure-sensation account must "
             "add, and the chapter's point is that it is already there in the simplest "
             "perceived thing."),
        ],
        "worked": {
            "title": "Three pairs, then four groups",
            "intro": [
                "Take the pairs preset, dots at 0, 1, 4, 5, 8 and 9, with ratio 2, then move "
                "the dot at 5 to 6. You want the groups each time, and what changed.",
            ],
            "lines": [
                "gaps:  1, 3, 1, 3, 1",
                "threshold:  2 × 1 = 2, so the gaps of 3 separate",
                "groups:  {0, 1} {4, 5} {8, 9}, three",
                "move 5 to 6; gaps:  1, 3, 2, 2, 1",
                "groups:  {0, 1} {4} {6} {8, 9}, four",
            ],
            "after": [
                "One dot moved and another dot's group changed. The grouping the rule computes "
                "belongs to the row, not to any dot in it. That is the lab's whole claim; the "
                "chapter's is larger, that the figure comes first and the dots are found in it "
                "afterwards.",
            ],
        },
        "quiz_title": "Pure sensation and the figure",
        "quiz": [
            {"q": "Dots stand at 0, 2, 3, 7 and 8. With ratio 2, how does the proximity rule "
                  "group them?",
             "a": ["Three groups: {0} {2, 3} {7, 8}",
                   "Two groups: {0, 2, 3} {7, 8}",
                   "One group of five",
                   "Five groups, one dot each"],
             "c": 0,
             "why": "The gaps are 2, 1, 4, 1, so the smallest is 1 and the threshold is "
                    "`2 × 1 = 2`. The gaps of 2 and 4 both separate, which gives three groups. "
                    "Two groups would need the gap of 2 to fall below the threshold; one group "
                    "ignores the gap of 4; five would need every gap to separate, and the gaps "
                    "of 1 do not."},
            {"q": "In the white-patch passage, what does each part of the patch do, on the "
                  "chapter's description?",
             "a": ["It arouses the expectation of more than it contains",
                   "It delivers one impression, later joined to the others",
                   "It is perceived first as a point and then as part of a shape",
                   "It shows the patch's colour exactly as the stimulus fixes it"],
             "c": 0,
             "why": "That is the passage's own phrase, and it is why the elementary perception "
                    "is already charged with a meaning. Separate impressions joined later is the "
                    "view the chapter rejects. Points perceived first get the order backwards: "
                    "each point is perceived only as a figure on a background. And the colour of "
                    "the shape is described as more intense than the background's, not as fixed "
                    "by the stimulus."},
            {"q": "What do psychologists call the experience error, in the chapter's account?",
             "a": ["Taking what we know to be in things as being in our consciousness of them",
                   "Mistaking an illusion for a genuine perception",
                   "Trusting the senses over measurement",
                   "Failing to attend to the edge of the visual field"],
             "c": 0,
             "why": "The chapter defines it so: we make perception out of things perceived, "
                    "moving the coloured object into consciousness as a coloured sensation. An "
                    "illusion is a different matter, trusting the senses is no error on the "
                    "chapter's view, and inattention is the psychologists' own hypothesis, which "
                    "the chapter rejects."},
            {"q": "Gestalt theory says a figure on a background is the simplest thing the senses "
                  "give. What does the chapter add?",
             "a": ["That this is the definition of perception, not a contingent fact leaving "
                   "room for impressions beneath it",
                   "That figure and background are each built up from sensations",
                   "That Gestalt theory is wrong about figure and background",
                   "That the figure appears only after attention is paid to it"],
             "c": 0,
             "why": "The chapter accepts the finding and denies that an ideal analysis may still "
                    "posit pure impressions under it. Building figure and ground from sensations "
                    "is the view it rejects. It does not reject the Gestalt finding but extends "
                    "it. And attention, the chapter says, is an auxiliary hypothesis supported "
                    "by no evidence of consciousness."},
        ],
        "mistakes": [
            ("Thinking experience is built from units of sensation",
             "A sensation looks like the simplest thing perception gives, so it seems "
             "experience must be built from such units. The chapter's claim is that the unit "
             "is a construction: the simplest thing perceived is already a figure on a ground, "
             "and the pure impression is not only undiscoverable but imperceptible. The lab "
             "shows the smallest version of this. In the shift preset the dot at 4 does not "
             "move, and the rule takes it from the group <code>{4, 5}</code> and leaves it "
             "alone, <code>{4}</code>: its grouping is a relation to the other dots and is in "
             "no dot."),
            ("Reading the lab's groups as what is seen",
             "The groups tile is what the proximity rule computes from measured positions, "
             "with a ratio the lesson chose. It is not a report of anyone's perception, and the "
             "next chapter warns that stating Wertheimer's law over measured stimuli is the "
             "psychologist's hybrid way of talking. The lab shows that a group is in no single "
             "dot; it cannot show the figure arriving before the dots."),
            ("Treating the indeterminate as a failure to perceive",
             "The psychologists say a misty landscape is unclear only for us, and that the "
             "bounded visual field is there but unnoticed. The chapter calls that attention "
             "brought in as an auxiliary hypothesis to save the objective world. The edge of "
             "the field is neither black nor grey, and the chapter asks that the indeterminate "
             "be recognised as a positive phenomenon, not as a gap in a determinate picture."),
        ],
        "standard": (
            "Finish when you can compute proximity groups and say what is in no single dot.",
            "Given positions on a line and a ratio, compute the gaps, the groups and their "
            "number; then state what the computation used besides the dots, and why the "
            "chapter holds that the simplest perceived thing is a figure on a ground."
        ),
        "note": (
            "The dots, the ratio and the rule's form are the lesson's illustration; the "
            "chapter has no figures of this kind, and it names Wertheimer's laws only in the "
            "next chapter, to warn against reading them as objective conditions. The lab "
            "computes a relation among measured positions, which nothing in the chapter "
            "disputes. It cannot show what the chapter claims, that the figure is given before "
            "any dot is singled out of it."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Smith p. 8 (opening passage: "Hence we have in principle ... purely
    # theoretical character"; the receiver-transmitter-recording station; the
    # three conflicting cases; n. 7, Koehler 1913; n. 8, Stumpf); p. 6
    # ("neither of equal nor unequal length ... arises", Fig. 1); p. 9
    # (attention and judgement as additional factors; "substitute a special
    # set-up ..."; n. 13, "It is discredited ..."); p. 10 (touch lesions;
    # "the text of the external world ..."); p. 13 ("one of the lines ceases
    # ... 'different'"; analytic perception; children's constancy, Hering and
    # Jaensch; Scheler's net, p. 14).
    {
        "slug": "the-constancy-hypothesis",
        "title": "The Constancy Hypothesis",
        "module": "Introduction · I · Sensation",
        "one_line": "The theory that each point of stimulus produces its own point of sensation predicts that equal lines look equal, and the chapter's reply is that in the perceived field the lines are not yet the kind of thing that is either.",
        "summary": (
            "The chapter turns to physiology's definition of sensation and names its hidden "
            "premise, the constancy hypothesis: a point-for-point correspondence between "
            "stimulus and elementary perception. Compute the hypothesis's prediction for two "
            "lines and the gap to a reported difference, and say why the chapter will not call "
            "the gap a mistake."
        ),
        "key": [
            "constancy: one stimulus, one sensation",
            "predicted = a − b",
            "reported − predicted gives the gap",
            "Müller-Lyer: neither equal nor unequal",
            "equal or unequal: the objective world's",
            "analysis may substitute a set-up",
        ],
        "key_label": "The constancy hypothesis in six lines",
        "concepts_intro": (
            "The second half of the first chapter is an argument with physiology. Three ideas "
            "carry it."
        ),
        "concepts": [
            ("The constancy hypothesis",
             "The premise that a stimulus and the elementary perception correspond point for "
             "point, so that the same local stimulus always gives the same sensation. The term "
             "is the Gestalt psychologist Wolfgang Köhler's, from a paper of 1913."),
            ("Analytic perception",
             "Looking at a figure part by part, for instance at the two main lines of the "
             "Müller-Lyer figure with the fins ignored. The chapter asks whether it reveals a "
             "normal sensation or replaces the original phenomenon with a special set-up."),
            ("The objective world",
             "The world as measured and fully determinate, where any two lines are either equal "
             "or unequal. The chapter's claim is that this world is a late result of "
             "perception, and that its questions do not all arise in the perceived field."),
        ],
        "read_title": "The passage first, then the chapter's argument with physiology",
        "read_intro": (
            "The passage is the chapter's statement of the hypothesis and the first "
            "objection. The lesson reads it, then follows the chapter from the Müller-Lyer "
            "figure on page 6 to its last paragraph."
        ),
        "body": [
            ("p", "<strong>Introduction, Chapter 1, p. 8.</strong> &ldquo;Hence we have in "
                  "principle a point-by-point correspondence and constant connection between the "
                  "stimulus and the elementary perception.&rdquo; That is physiology's "
                  "premise, as the chapter states it, and the next sentence names it and "
                  "objects: &ldquo;But this &lsquo;constancy hypothesis&rsquo; conflicts with "
                  "the data of consciousness, and the very psychologists who accept it "
                  "recognize its purely theoretical character.&rdquo; Both sentences are on "
                  "page 8 of Smith's translation. Read "
                  "from the Müller-Lyer figure on page 6 to the end of the chapter on page 14, "
                  "in your own copy before going on."),
            ("p", "You have almost certainly seen the two lines with arrowheads, one with the "
                  "fins turned out and one with them turned in, and been told that they are the "
                  "same length. Measure them and they are. The lab does the measurement for "
                  "you: ten centimetres and ten centimetres, so the theory Köhler named the "
                  "constancy hypothesis, that each point of the stimulus produces its own point "
                  "of sensation, the same wherever it occurs, predicts no difference at all. "
                  "Most people report one. The usual way of putting this is that perception has "
                  "made a mistake, and the textbook calls the figure an illusion. "
                  "Merleau-Ponty's reply is different: the mistake is in the question. "
                  "<em>Equal</em> and <em>unequal</em>, he argues, belong to a world where "
                  "lines are laid side by side and measured; in the field you are looking at, "
                  "the two lines are not yet the kind of thing that is either."),
            ("p", "First the hypothesis, at its strength. Physiology, the chapter says, places "
                  "its object in the world like any science, and treats the path from the eye to "
                  "the brain as a line from a receiver through a transmitter to a recording "
                  "station. The objective world sends messages to the sense organs, and they "
                  "are registered and deciphered so as to reproduce the original text in us. "
                  "If that is right, the same message must be decoded the same way wherever it "
                  "arrives, and the passage's first sentence follows. Without it, it is hard to "
                  "see how a stimulus could explain a perception at all. A footnote credits the "
                  "term to Köhler's 1913 paper on unnoticed sensations and errors of judgement, "
                  "and adds that Carl Stumpf, the experimental psychologist under whom Köhler had "
                  "trained, said outright that the hypothesis is theoretical."),
            ("p", "Then the conflicts. The intensity of a sound can lower its pitch; added lines "
                  "make two objectively equal figures unequal; a coloured area looks one colour "
                  "over its whole surface although the retina's thresholds differ from place to "
                  "place. Red and green shown together give grey, and an object's apparent size "
                  "varies with its apparent distance; in these last two cases, the chapter notes, "
                  "the hypothesis's own defenders concede that central processes intervene. The "
                  "chapter puts the choice plainly on "
                  "page 9: keep the law of constancy and explain the deviations by additional "
                  "factors, attention and judgement, or give up the law. Chapter 3 examines those "
                  "two factors; this chapter examines the law."),
            ("p", "The lab computes the hypothesis's prediction. In the <code>muller</code> "
                  "preset the shaft with outward fins and the shaft with inward fins both "
                  "measure 10 cm. The predicted tile is the difference the hypothesis allows, "
                  "10 − 10, printed <code>0 cm</code>. The reported tile holds a difference "
                  "someone reports, here 2 cm, the outward-finned shaft taken as the longer; the "
                  "figure is illustrative, since the size of the effect varies with the length "
                  "and angle of the fins. The gap tile is reported minus predicted, "
                  "<code>2 cm</code>. That gap is what the textbook calls the illusion, and it "
                  "is an illusion only if the measured lines are taken as the standard of what "
                  "should be seen."),
            ("p", "The <code>equal</code> preset removes the fins: two plain shafts of 10 cm, "
                  "a reported difference of 0, and every tile <code>0 cm</code>. Here the "
                  "hypothesis and the report agree, which is why it looks so secure. The "
                  "<code>context</code> preset is the chapter's sharper case. It sets one shaft "
                  "with inward fins against the same shaft drawn alone: the same local stimulus "
                  "twice, 10 cm and 10 cm, and a report, illustrative again, that the finned "
                  "one is 1 cm shorter. The reported tile and the gap both print "
                  "<code>−1 cm</code>; the minus sign says the first-named line was reported "
                  "the shorter. One stimulus, two reports, is exactly what a point-for-point "
                  "correspondence forbids."),
            ("p", "Now the chapter's reading of the figure, which it gives twice. On page 6 the "
                  "two lines are &ldquo;neither of equal nor unequal length; it is only in the "
                  "objective world that this question arises&rdquo;. The visual field, it goes "
                  "on, is a strange zone where contradictory notions jostle, because the lines "
                  "are not assigned to the realm of being in which a comparison could be made; "
                  "each is taken in its own context. On page 13 the same thought is sharper: "
                  "&ldquo;one of the lines ceases to be equal to the other without becoming "
                  "&lsquo;unequal&rsquo;: it becomes &lsquo;different&rsquo;&rdquo;. An "
                  "isolated line and the same line in a figure cease, for perception, to be the "
                  "same line, and only analytic perception, which is not natural, can identify "
                  "them."),
            ("def", ("Different, not unequal",
                     "Unequal is a relation between two measured lengths in one space. "
                     "Different, in the chapter's sense, is what a line becomes in a figure: "
                     "something other than the same line alone, before any measuring "
                     "compares them.")),
            ("p", "The hypothesis has a reply, and the chapter states it. With attention, "
                  "precise instructions, rest or long practice, observers come to report the "
                  "lines as equal, so the normal sensation was there all along. The answer on "
                  "page 9 is that the first appearance had a sensory character just as "
                  "undeniable as the final result, and that attentive, analytic looking may "
                  "&ldquo;substitute a special set-up for the original phenomenon&rdquo; rather "
                  "than uncover it. And a footnote concedes, in fairness, that there is no crucial "
                  "experiment against the hypothesis, as there is none for any theory, and that "
                  "it cannot be completely refuted by induction. &ldquo;It is discredited because it overlooks "
                  "phenomena and does not permit any understanding of them.&rdquo; To judge it, "
                  "the footnote adds, one must first suspend it."),
            ("p", "The physiology itself, the chapter goes on, no longer fits the role of "
                  "transmitter. After a lesion of the apparatus of touch the specific sensations "
                  "return if the stimulus is large enough, the hand making up for the raised "
                  "thresholds by moving more vigorously. When sight is destroyed, wherever the "
                  "injury, colours lose their saturation in the same order, down to grey. So "
                  "normal functioning has to be understood as an integration in which "
                  "&ldquo;the text of the external world is not so much copied, as "
                  "composed&rdquo;. The scientist, too, must learn to criticise the idea of an "
                  "external world in itself, because the facts prompt him to give up the body "
                  "as a transmitter of messages."),
            ("p", "The chapter ends with a reversal you might not expect. Constancy of apparent "
                  "size at different distances, and of colour in different lights, is known to "
                  "be more perfect in children than in adults. So perception is more strictly "
                  "bound to the local stimulus when it is developed than when it is not, and the "
                  "theory of sensation fits the adult better than the child. Perception, in an "
                  "image the chapter takes from the German phenomenologist Max Scheler, is like a "
                  "net whose knots show up more and more clearly. The theory of sensation describes the "
                  "most finished layer of consciousness and takes it for the first."),
            ("p", "Back to the lab, then, with that in view. Its reported tile has to print a "
                  "number of centimetres, and a number of centimetres already treats the two "
                  "lines as comparable in one measured space. The lab can only print the "
                  "objective comparison. It has no tile for different, and the chapter's claim "
                  "is that the perceived figure is different before it is anything a ruler can "
                  "settle."),
            ("p", "If the deviations are not sensations misreported, perhaps memory corrects "
                  "them. The next lesson, “Association and the Projection of "
                  "Memories”, reads the chapter that tests the empiricist's next resource."),
        ],
        "lab": ("phenkit", {
            "mode": "stimulus",
            "view": "illusion",
            "model": "the constancy hypothesis (Köhler's term)",
            "preset": "muller",
            "presets": [
                {"id": "muller",
                 "label": "Müller-Lyer: both shafts 10 cm, the outward-finned one reported 2 cm longer (illustrative)",
                 "a": 10, "b": 10, "unit": "cm", "reported": 2,
                 "expect": {"stPredicted": "0 cm", "stReported": "2 cm", "stGap": "2 cm"}},
                {"id": "equal",
                 "label": "Two plain shafts of 10 cm, no fins, no difference reported",
                 "a": 10, "b": 10, "unit": "cm", "reported": 0,
                 "expect": {"stPredicted": "0 cm", "stReported": "0 cm", "stGap": "0 cm"}},
                {"id": "context",
                 "label": "One 10 cm shaft with inward fins against the same shaft alone, reported 1 cm shorter (illustrative)",
                 "a": 10, "b": 10, "unit": "cm", "reported": -1,
                 "expect": {"stPredicted": "0 cm", "stReported": "−1 cm", "stGap": "−1 cm"}},
            ],
            "panel_title": "What the constancy hypothesis predicts",
            "panel_intro": (
                "This lab computes the constancy hypothesis, Köhler's term for the premise that "
                "each point of stimulus gives its own point of sensation: two lines that measure "
                "the same are predicted to differ by nothing. It prints that prediction, a "
                "reported difference, which is illustrative, and the gap between them."
            ),
        }),
        "steps_title": "Computing the hypothesis's prediction and the gap",
        "steps_intro": "Four steps, the last of which is the lesson's.",
        "steps": [
            ("Measure both lines in one unit",
             "Write the two measured lengths, a and b, in the same unit. On the constancy "
             "hypothesis these lengths fix what is sensed."),
            ("Compute the prediction",
             "The predicted difference is a − b. Equal measured lines are predicted to differ "
             "by 0."),
            ("Compute the gap",
             "Subtract the prediction from the reported difference. A positive gap means the "
             "first line was reported longer than predicted, a negative gap shorter."),
            ("Name what the gap assumes",
             "The gap is an error only if the measured lines are the standard of what should "
             "be seen. State the chapter's alternative: that equal and unequal are questions of "
             "the objective world, and that in the figure a line becomes different."),
        ],
        "worked": {
            "title": "Two equal shafts and a reported difference",
            "intro": [
                "Take the muller preset: both shafts measure 10 cm, and someone reports the "
                "shaft with outward fins as 2 cm longer. You want the prediction, the gap, and "
                "what the gap is a gap between.",
            ],
            "lines": [
                "predicted:  10 − 10 = 0 cm",
                "reported:  2 cm",
                "gap:  2 − 0 = 2 cm",
                "context preset:  10 − 10 = 0; reported −1 cm",
                "context gap:  −1 − 0 = −1 cm",
            ],
            "after": [
                "Every figure is exact, and the 2 cm and the 1 cm are illustrative. The gap "
                "measures the distance between a report and the hypothesis's prediction. Calling "
                "it an illusion takes the measurement as what should have been seen; the "
                "chapter's view is that the comparison belongs to the objective world, and that "
                "the perceived lines are not yet equal or unequal.",
            ],
        },
        "quiz_title": "The constancy hypothesis",
        "quiz": [
            {"q": "Two shafts measure 12 cm each, and the one with outward fins is reported 3 cm "
                  "longer. What do the hypothesis's prediction and the gap come to?",
             "a": ["Predicted 0 cm, gap 3 cm",
                   "Predicted 3 cm, gap 0 cm",
                   "Predicted 0 cm, gap −3 cm",
                   "Predicted 12 cm, gap −9 cm"],
             "c": 0,
             "why": "The prediction is the measured difference, `12 − 12 = 0`, and the gap is "
                    "reported minus predicted, `3 − 0 = 3`. Predicting 3 cm takes the report for "
                    "the prediction; −3 subtracts the wrong way round; 12 cm confuses a length "
                    "with a difference of lengths."},
            {"q": "A shaft of 9 cm and a shaft of 10 cm are reported as differing by 1 cm, the "
                  "first the longer. What are the prediction and the gap?",
             "a": ["Predicted −1 cm, gap 2 cm",
                   "Predicted 1 cm, gap 0 cm",
                   "Predicted −1 cm, gap 0 cm",
                   "Predicted 0 cm, gap 1 cm"],
             "c": 0,
             "why": "The prediction is `9 − 10 = −1`: the first shaft should look 1 cm shorter. "
                    "The report says 1 cm longer, so the gap is `1 − (−1) = 2`. A prediction of "
                    "+1 reverses the subtraction, a gap of 0 compares sizes and ignores signs, "
                    "and a prediction of 0 treats the shafts as equal."},
            {"q": "What does the chapter say of the two lines of the Müller-Lyer figure as they "
                  "are perceived?",
             "a": ["That they are neither equal nor unequal, the question arising only in the "
                   "objective world",
                   "That they look unequal, so perception is mistaken about them",
                   "That they are equal in sensation, the difference being added by a judgement",
                   "That they look equal once enough attention is paid"],
             "c": 0,
             "why": "That is page 6, and page 13 adds that the line becomes different rather "
                    "than unequal. Calling perception mistaken keeps the measured lines as the "
                    "standard. Equal sensations with an added judgement is the intellectualist "
                    "repair of the hypothesis, and attention bringing them into line is the "
                    "reply the chapter answers on page 9."},
            {"q": "According to the chapter's footnote, why is the constancy hypothesis "
                  "discredited?",
             "a": ["It overlooks phenomena and permits no understanding of them",
                   "A crucial experiment has refuted it",
                   "It has been disproved by induction from many cases",
                   "Physiologists found no path from receiver to brain"],
             "c": 0,
             "why": "The footnote says exactly this, and says just as plainly that there is no "
                    "crucial experiment and that the hypothesis cannot be completely refuted by "
                    "induction. The receiver-transmitter path is the chapter's description of "
                    "the theory, not a finding against it."},
        ],
        "mistakes": [
            ("Thinking perception is simply mistaken about the Müller-Lyer lines",
             "The lines measure the same and look different, so it seems perception has made "
             "an error. The chapter's point is not that perception errs but that the question "
             "of equal or unequal belongs to the objective world; in the perceived field the "
             "lines are not yet comparable in that way, and one of them becomes "
             "&ldquo;&lsquo;different&rsquo;&rdquo; rather than unequal. The lab can only "
             "print the objective comparison: predicted <code>0 cm</code>, reported "
             "<code>2 cm</code>, gap <code>2 cm</code>, every figure a measurement or a report "
             "and none of them the figure as seen."),
            ("Taking the reported tile for what is seen",
             "The reported tile holds a difference in centimetres that someone states, and "
             "the lesson's figures for it are illustrative. To state it at all, the observer "
             "has already laid the two lines side by side in one measured space, which is the "
             "analytic attitude the chapter says perception does not begin with."),
            ("Thinking practice reveals the normal sensation",
             "With attention, instruction or practice observers do come to report the lines "
             "as equal, and the hypothesis's defenders read that as the normal sensation "
             "uncovered. The chapter answers that the first appearance was just as sensory as "
             "the last, and that analytic looking may replace the original phenomenon with a "
             "special set-up. It does not claim a refutation; it says the hypothesis "
             "overlooks the phenomena."),
        ],
        "standard": (
            "Finish when you can compute the hypothesis's prediction and say why the gap is not a mistake.",
            "Given two measured lengths and a reported difference, compute the constancy "
            "hypothesis's prediction and the gap, with its sign, and state the chapter's "
            "reason for saying that the perceived lines are neither equal nor unequal."
        ),
        "note": (
            "The reported differences are illustrative, and the lab prints a measured "
            "comparison, which is the one thing the chapter says the perceived figure is not; "
            "it cannot show a line becoming different. One later view bears on the same "
            "phenomenon. Predictive-processing theories in cognitive science also reject the "
            "constancy hypothesis, because on them expectations shape the percept, so the same "
            "stimulus need not give the same perception. They differ from Merleau-Ponty, and "
            "among themselves, on what replaces it: on one reading the brain's prediction is "
            "an unconscious inference, close to the judgement Introduction III argues against; "
            "on enactive and active-inference readings it lies nearer the body's own hold on "
            "the world. The chapter, written in 1945, answers neither; what in it bears on the "
            "dispute is its choice on page 9, between added factors and dropping the law."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Smith p. 23 (opening passage: "How could the evocation of memories ...
    # storehouse of memory?"; "I read 'deduction' ... 'destruction'" -- the
    # projection theory's own example; "nothing but a bad metaphor ...");
    # p. 15 (figure and background); pp. 16-17 (A, B and C; association of
    # ideas; "as evening leads one to expect night"; nominalism, p. 18);
    # p. 18 (things and spaces between things; rabbit and hunter); p. 19
    # (Wertheimer's laws, n. 4); p. 20 (the ship, read in lesson 4); pp. 20-21
    # (Lewin's syllables); p. 21 (Gottschaldt's figures); p. 22 (Bergson,
    # reading; Hering's memory colour, p. 23); p. 24 ("this original text is
    # perception itself"; a tardy correction of empiricism); p. 26 ("To
    # perceive is not to remember."); p. 27 (reflection as closed as
    # insanity); pp. 27-29 (the human world; the hysterical child).
    {
        "slug": "association-and-the-projection-of-memories",
        "title": "Association and the Projection of Memories",
        "module": "Introduction · II · Association and Memory",
        "one_line": "Memories cannot fill in what the senses leave out, because to call up the right memory what is seen must already have the shape memory was supposed to give it.",
        "summary": (
            "The second chapter tests empiricism's two ways of getting meaning out of "
            "sensations, the association of ideas and the projection of memories, and finds "
            "that each presupposes the meaning it was meant to supply. Count the remembered "
            "words that fit a partly seen word, then the ones left once a context arrives, and "
            "say what did the selecting."
        ),
        "key": [
            "association: contiguity, resemblance",
            "memory said to fill the gaps",
            "recall needs a shape already there",
            "count = remembered words fitting",
            "pattern and context select",
            "to perceive is not to remember",
        ],
        "key_label": "The second chapter in six lines",
        "concepts_intro": (
            "The chapter answers two empiricist resources and then says what empiricism "
            "hides. Three ideas carry it."
        ),
        "concepts": [
            ("Association",
             "The empiricist's principle of connection: impressions that have occurred together "
             "(contiguity) or that are alike (resemblance) call one another up. The chapter "
             "argues that it can restore only external links, and that the meaning of what is "
             "perceived is presupposed by any association."),
            ("The projection of memories",
             "The view that perception fills the gaps in the sense data with memories, as when "
             "a reader is said to supply the letters the eye skipped. The chapter calls it a "
             "late and ineffective correction of empiricism, sharing its postulates."),
            ("The horizon of the past",
             "The chapter's alternative: the past is present not as stored pictures projected "
             "onto sensations but as a horizon that gives what is perceived its atmosphere, "
             "and that can be reopened in an act of recollection."),
        ],
        "read_title": "The passage first, then the chapter from its first page",
        "read_intro": (
            "The passage is the chapter's question about the proofreader. The lesson reads "
            "it, goes back to the chapter's opening on association, and follows it to the "
            "end."
        ),
        "body": [
            ("p", "<strong>Introduction, Chapter 2, p. 23.</strong> &ldquo;How could the "
                  "evocation of memories come about unless guided by the look of the strictly "
                  "visible data, and if it is thus guided, what use is it then, since the word "
                  "already has its structure or its features before taking anything from the "
                  "storehouse of memory?&rdquo; The question is on page 23 of Smith's "
                  "translation, in the chapter Smith titles &lsquo;Association&rsquo; and the "
                  "&lsquo;Projection of Memories&rsquo;. Read the whole chapter, pages 15 to 29, "
                  "in your own copy before going on."),
            ("p", "Anyone who has proofread their own writing knows the trouble. You read the "
                  "sentence you meant, and the letter you left out or the word you typed twice "
                  "slides past. The standard explanation is that memory fills in: you know the "
                  "word, so you supply what the page does not show. The chapter's example is "
                  "the proofreader's illusion, as the theory itself describes it: "
                  "&ldquo;I read &lsquo;deduction&rsquo; when the word printed is "
                  "&lsquo;destruction&rsquo;&rdquo;. The d stands where str was printed, it was "
                  "not given to the eye, so it must come from somewhere else, and the theory "
                  "says it comes from memory. The passage is the chapter's question back."),
            ("p", "The chapter begins further back, with what is left once sensation has been "
                  "admitted. A figure on a background means more than its qualities: it has an "
                  "outline, it stands out, the background runs on beneath it. If perception is "
                  "made of sensations, that meaning can come only from further sensations, and "
                  "a shape becomes a sum of limited views. Take three points A, B and C on a "
                  "circle. For empiricism their order is just the position of A plus the "
                  "position of B plus the position of C, and seeing a circle is being reminded "
                  "of other circular paths the eye has travelled."),
            ("def", ("Association by contiguity and by resemblance",
                     "The two classical laws of the association of ideas, a phrase John "
                     "Locke made current and a principle David Hume made central, and the "
                     "engine of the psychology that followed them: impressions that occurred together, or "
                     "that are alike, come to call one another up.")),
            ("p", "Followed through, the chapter says, this makes knowledge a system of "
                  "substitutions, in which one impression announces others without ever "
                  "justifying the announcement, and words lead one to expect sensations "
                  "&ldquo;as evening leads one to expect night&rdquo;. Two paths can never be "
                  "understood as the same; they can only be associated. The philosophy that "
                  "fits is nominalism, the view that general words name nothing but vague "
                  "resemblances, and understanding becomes a fraud. The reply is that "
                  "sensations and images appear only within a horizon of meaning already there. "
                  "Our perceptual field is made of things and spaces between things, and if you "
                  "set yourself to see the intervals as things, the world would change as a "
                  "puzzle picture does when you pick out the rabbit or the hunter: not the same "
                  "elements differently associated, but another world."),
            ("p", "The chapter's evidence against association as a force is an experiment by "
                  "the psychologist Kurt Lewin. Subjects learn two sets of paired syllables: in "
                  "one the second syllable is a softened rhyme of the first, tak and dak; in the "
                  "other it is the first reversed, ged and deg. Asked to find a softened rhyme, "
                  "they are slower for ged than for a neutral syllable. Asked instead to change "
                  "the vowel, they show no delay. If the drilled association were a force, it "
                  "should act in both tasks. It acts only when the task makes reproducing the "
                  "drill an attractive short cut, through what the chapter calls a "
                  "reproduction intention: association works through the meaning a past "
                  "experience has, not as an efficient cause."),
            ("p", "Then the projection of memories, a way of talking found outside empiricism "
                  "too: the French philosopher Léon Brunschvicg speaks of the contributions of "
                  "memory, and Henri Bergson argues that in reading the eye moves too fast to "
                  "take in every letter, so memory fills the gaps. The answer is the passage. To be "
                  "called up, a memory must be guided by what is strictly visible, and once it "
                  "is so guided it has nothing left to do, because the word already has its "
                  "structure. The same holds of the physiologist Ewald Hering's memory colour, the colour we "
                  "are said to see objects in through the spectacles of memory: something in "
                  "what is present must first tell us the object is familiar. The projection of "
                  "memories, the chapter concludes, is &ldquo;nothing but a bad metaphor hiding "
                  "a deeper, ready-made recognition&rdquo;."),
            ("p", "The lab computes the associationist's model on a list of twenty remembered "
                  "words, the same for every preset. In <code>misprint</code> the printed word "
                  "is <em>hoxse</em>. The model counts the misprinted third letter as not seen, "
                  "as the projection theory counts the letters the eye skipped, so the pattern is "
                  "<code>ho_se</code>, the blank standing for that letter. The count "
                  "tile prints <code>2</code> and the candidates tile <code>house, horse</code>, "
                  "in list order: memory, on this model, offers two words and cannot choose. "
                  "The context tile prints a dash, because no context has been given. The "
                  "misprint is the lesson's; the book's is deduction for destruction, where "
                  "three printed letters give way to one, which no pattern of blanks can model."),
            ("p", "The <code>wide</code> preset loosens the pattern to <code>_a_e</code>, a "
                  "four-letter word with a in second place and e in fourth. Eighteen of the "
                  "twenty remembered words fit, and the count tile prints <code>18</code>. In "
                  "<code>context</code> the same pattern meets a sentence about a door. Three "
                  "words in the list carry a context tag, and only gate is tagged door, so the "
                  "count drops to <code>1</code>, the candidates tile prints <code>gate</code> "
                  "and the context tile <code>door</code>. Look at what did the selecting. The "
                  "memories sat in their list throughout; the pattern of letters on the page "
                  "and the sentence around the word chose among them."),
            ("p", "That is the chapter's dilemma in miniature. If memories projected "
                  "themselves onto sensations, nothing in the percept could stem their flood, "
                  "and eighteen candidates is a small flood. If instead consciousness compares "
                  "memories with the present data and keeps only those that fit, then an "
                  "original text has been admitted beside them, and &ldquo;this original text is "
                  "perception itself&rdquo;. The model, notice, takes the second horn, since its "
                  "pattern is a present datum doing the choosing. So the theory is not the "
                  "mental activity opposed to empiricism that it seems; it is a tardy "
                  "correction of empiricism that shares its postulate, building perception from "
                  "states of consciousness as a house is built from bricks, with nobody who "
                  "sees."),
            ("p", "None of this, the chapter says, removes memory from perception; it moves the "
                  "real problem. The past is present as a horizon, an atmosphere that gives what "
                  "is seen its significance, and that can be reopened in recollection or left at "
                  "the fringe. To perceive is to see an immanent significance stand out from a "
                  "cluster of data, and to remember is to go back into that horizon and unfold "
                  "it. The chapter's sentence is short: &ldquo;To perceive is not to "
                  "remember.&rdquo;"),
            ("p", "The chapter is candid about the limits of the argument. On its own footing "
                  "empiricism cannot be refuted, since it rejects the evidence of reflection "
                  "and can always rebuild, from associated impressions, a near equivalent of any "
                  "structure described to it. The new way of looking has to be undertaken by "
                  "each for himself. And Merleau-Ponty allows himself a dry comparison: in this "
                  "sense reflection is a system as closed as insanity, with the difference that "
                  "it understands itself and the madman too, while the madman does not "
                  "understand it."),
            ("p", "What empiricism hides, the chapter ends, is the human world: the anger read "
                  "in a face, the temper of a city in a policeman's bearing or the style of a "
                  "public building, which for empiricism can only be transferred memories, "
                  "meaningful by accident. It hides the natural world too, and the strange "
                  "presence of the things behind our back. The next lesson, “Attention and "
                  "Judgment”, turns to the other opponent, who agrees that sensations "
                  "cannot organise themselves and gives the work to the mind."),
        ],
        "lab": ("phenkit", {
            "mode": "cues",
            "view": "pattern",
            "model": "the associationist account",
            "preset": "misprint",
            "presets": [
                {"id": "misprint",
                 "label": "The printed word hoxse, its misprinted third letter taken as unseen: pattern ho_se (illustrative)",
                 "words": ("house, horse, gate:door, game, gave, have, hate, lake:water, make, "
                           "name, same, take, cake, late, sale, tale, wave, cane, date, page:book"),
                 "pattern": "ho_se", "context": "",
                 "expect": {"cuCount": "2", "cuCandidates": "house, horse", "cuContext": "—"}},
                {"id": "wide",
                 "label": "A four-letter word with a second and e fourth: pattern _a_e",
                 "words": ("house, horse, gate:door, game, gave, have, hate, lake:water, make, "
                           "name, same, take, cake, late, sale, tale, wave, cane, date, page:book"),
                 "pattern": "_a_e", "context": "",
                 "expect": {"cuCount": "18", "cuContext": "—"}},
                {"id": "context",
                 "label": "The same pattern in a sentence about a door",
                 "words": ("house, horse, gate:door, game, gave, have, hate, lake:water, make, "
                           "name, same, take, cake, late, sale, tale, wave, cane, date, page:book"),
                 "pattern": "_a_e", "context": "door",
                 "expect": {"cuCount": "1", "cuCandidates": "gate", "cuContext": "door"}},
            ],
            "panel_title": "Which remembered words fit",
            "panel_intro": (
                "This lab computes the associationist account of reading: a stock of remembered "
                "words, the lesson's twenty, is matched against the letters seen, with a blank "
                "for each letter not seen, and then against a context tag. It counts the "
                "words that fit and lists them, which shows what does the selecting; it cannot "
                "show a word being read."
            ),
        }),
        "steps_title": "Counting the memories that fit",
        "steps_intro": "Four steps, the last of which is the lesson's.",
        "steps": [
            ("Write the pattern",
             "Put each letter seen in its place and a blank for each letter not seen. A "
             "pattern fits only words of its own length."),
            ("Match the remembered words",
             "Keep every word in the list that has the pattern's letters in the pattern's "
             "places. Their number is the count."),
            ("Apply the context",
             "If a context is given, keep only the words tagged with it. With no context the "
             "count stands."),
            ("Say what selected",
             "Name what reduced the candidates: the letters on the page and the sentence "
             "around the word, both present. The memories did not select themselves, which is "
             "the chapter's objection to the projection of memories."),
        ],
        "worked": {
            "title": "Two words, eighteen words, one word",
            "intro": [
                "Take the twenty remembered words and three readings: ho_se, then _a_e alone, "
                "then _a_e in a sentence about a door. You want the count each time, and what "
                "brought it down.",
            ],
            "lines": [
                "ho_se:  house, horse; count 2",
                "_a_e:  18 of the 20 fit; only house and horse do not",
                "_a_e with context door:  gate; count 1",
            ],
            "after": [
                "The letters alone cannot choose between house and horse, or among eighteen "
                "words; the sentence the word sits in can. Both of those are present, not "
                "remembered. On the chapter's account the word already has its structure before "
                "memory adds anything, which is why the memories in the list never have "
                "anything to do.",
            ],
        },
        "quiz_title": "Association and memory",
        "quiz": [
            {"q": "With the lesson's twenty remembered words, the pattern _a_e and the context "
                  "water, what does the lab count?",
             "a": ["1: lake", "18", "2: lake and cake", "0"],
             "c": 0,
             "why": "Eighteen words fit _a_e, and only lake carries the tag water, so one "
                    "remains. Eighteen ignores the context; cake fits the letters but is not "
                    "tagged; and nothing reduces the count to 0, since lake both fits and is "
                    "tagged."},
            {"q": "In Lewin's experiment, why does the delay over ged count against association "
                  "as a force?",
             "a": ["The same drill caused a delay under one task and none under another, so the "
                   "task decided whether it acted",
                   "The subjects had not learnt the syllables well enough to associate them",
                   "Reversed syllables cannot be associated at all",
                   "The delay was too short to measure reliably"],
             "c": 0,
             "why": "A force would act whatever the task; the drilled pairs slowed the rhyming "
                    "task and did not touch the vowel task, so they acted only through a "
                    "reproduction intention the task invited. The chapter does not say the "
                    "learning was weak, or that reversed pairs cannot be associated, and it "
                    "reports a delay, not a doubtful one."},
            {"q": "What is the chapter's objection to saying that perception fills the gaps in "
                  "the sense data with memories?",
             "a": ["A memory could be called up only if what is seen already had the shape the "
                   "memory is supposed to give it",
                   "Memories are too faint to compete with present sensations",
                   "The past plays no part in perception at all",
                   "Proofreaders do not really misread words"],
             "c": 0,
             "why": "That is the passage: the evocation must be guided by the visible, and then "
                    "the word already has its structure. Faintness is no part of the argument. "
                    "The chapter keeps the past in perception, as a horizon, and it takes the "
                    "proofreader's illusion as real."},
            {"q": "How does the chapter place the theory of the projection of memories in "
                  "relation to empiricism?",
             "a": ["As a tardy correction of empiricism that shares its postulates",
                   "As the mental activity that refutes empiricism",
                   "As an intellectualist theory opposed to association",
                   "As the Gestalt psychologists' replacement for sensation"],
             "c": 0,
             "why": "The chapter says the theory seems to bring a mental activity into "
                    "perception against empiricism, and that this is a mistake: it accepts "
                    "empiricism's postulates and shares its difficulties. It is not "
                    "intellectualism, which the next chapter treats, and the Gestalt "
                    "psychologists are the chapter's source of evidence against it."},
        ],
        "mistakes": [
            ("Thinking memory supplies what the senses leave out",
             "The proofreader reads the word that was not printed, so it seems memory must "
             "have supplied it. The chapter's objection is that to call up the right memory the "
             "perceived word must already have the shape that memory is said to give it, and "
             "then memory has nothing left to do. The lab shows the memories do not select "
             "themselves: <code>ho_se</code> leaves two words, <code>_a_e</code> eighteen, and "
             "only the context door brings the count to one, <code>gate</code>. The pattern and "
             "the context, both present, did the choosing."),
            ("Taking the projection of memories for an answer to empiricism",
             "It looks like a mental activity added to raw sensation, and so like a move away "
             "from empiricism. The chapter calls it a tardy and ineffective correction that "
             "keeps empiricism's postulate: the given is first deduced from what the sense "
             "organs can supply, and the rest is then put down to recollection, as bricks are "
             "added to a house."),
            ("Concluding that the past plays no part in perception",
             "The chapter does not deny that former experience shapes what is seen. It "
             "denies that the past arrives as pictures projected onto sensations. The past is "
             "present as a horizon, an atmosphere around what is perceived, which recollection "
             "can reopen and which can equally stay at the fringe of experience."),
        ],
        "standard": (
            "Finish when you can count the memories that fit and say what selected them.",
            "Given a list of remembered words, a pattern of seen letters and a context, count "
            "and list the words that fit, and state the chapter's reason for holding that the "
            "projection of memories presupposes what it was meant to explain."
        ),
        "note": (
            "The word list, the misprint and the context tags are the lesson's; the book's "
            "example, deduction read for destruction, cannot be modelled by blanks. The lab "
            "computes the associationist's matching, which is the model the chapter rejects, "
            "and it can only match letters: it cannot show a word with its structure before "
            "any matching, which is the chapter's claim."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Smith p. 30 (opening passage: "We must now show ... constitutes its
    # object"; attention as searchlight; Malebranche); p. 31 (the wax; the
    # circle in the plate); p. 32 (the moon through a cardboard tube, Alain,
    # n. 2); p. 33 ("we need to be ignorant of what we are looking for";
    # attention creates nothing, for both); pp. 33-35 (Head; infants'
    # colours; attention as the constitution of a new object); p. 36 (the
    # moon again, the reply); pp. 37-38 (judgement; the wax; Descartes's men
    # at the window, n. 16; two eyes, Lagneau); pp. 39-40 (the box, the drawn
    # cube; true and false perception); pp. 40-42 (Zollner; "creates at a
    # stroke"); p. 45 ("We pass from absolute objectivity ..."); pp. 48-52
    # (natural judgement; Sixth Meditation); p. 56 ("There is no reason, but
    # there is a motive."). The ship: Chapter 2, p. 20 ("there will be a
    # moment ..."; "these reasons ... beforehand"; Kant's synopsis).
    {
        "slug": "attention-and-judgment",
        "title": "Attention and Judgment",
        "module": "Introduction · III · Attention and Judgment",
        "one_line": "Intellectualism is not the opposite of empiricism but its counterpart: both start from a finished objective world, and differ only over whether the stimulus or the mind builds the percept.",
        "summary": (
            "The third chapter turns to intellectualism, the view that perception is a "
            "judgement, and shows through the history of attention and the analysis of "
            "judgement that it stands on the same ground as empiricism. Count the "
            "interpretations a judgement-from-signs model keeps as the cues arrive on the walk "
            "towards a stranded ship, and name the step at which the model decides."
        ),
        "key": [
            "attention, empiricist: a searchlight",
            "attention, intellectualist: elucidation",
            "both: attention creates nothing",
            "judgement: what sensation lacks",
            "count = candidates fitting every cue",
            "reasons came after the recasting",
            "no reason, but a motive",
        ],
        "key_label": "The third chapter in seven lines",
        "concepts_intro": (
            "The chapter's argument runs through two notions the theories need, attention and "
            "judgement. Three ideas hold it together."
        ),
        "concepts": [
            ("Attention",
             "For empiricism a searchlight that lights up sensations already there; for "
             "intellectualism the mind coming to itself and finding what it had already put "
             "in the object. On the chapter's account it is neither, but the active "
             "constitution of a new object out of what was an indeterminate horizon."),
            ("Judgement",
             "What intellectualism adds to sensation to make perception: an interpretation of "
             "the signs the senses provide, a conclusion drawn from them. The chapter argues "
             "that this makes seeing and thinking one sees indistinguishable."),
            ("Motive",
             "The chapter's alternative to both cause and reason. One phenomenon releases "
             "another through the meaning it holds out, not as an efficient cause and not as a "
             "premise, as intervening objects mean a greater distance without proving it."),
        ],
        "read_title": "The passage first, then attention, then judgement",
        "read_intro": (
            "The passage is the chapter's opening thesis. The lesson reads it, follows the "
            "history of attention, then the analysis of judgement, and tests a "
            "judgement-from-signs model on the book's walk along the shore."
        ),
        "body": [
            ("p", "<strong>Introduction, Chapter 3, p. 30.</strong> &ldquo;We must now show "
                  "that its intellectualist antithesis is on the same level as empiricism "
                  "itself. Both take the objective world as the object of their analysis, when "
                  "this comes first neither in time nor in virtue of its meaning; and both are "
                  "incapable of expressing the peculiar way in which perceptual consciousness "
                  "constitutes its object.&rdquo; The sentences open the chapter Smith titles "
                  "&lsquo;Attention&rsquo; and &lsquo;Judgement&rsquo;, on page 30. Read the "
                  "whole chapter, pages 30 to 59, in your own copy before going on; it is the "
                  "longest in the Introduction, and the lesson follows its two halves."),
            ("p", "The thesis is surprising, because intellectualism grew up as the answer to "
                  "empiricism. If sensations cannot organise themselves, as the last two "
                  "chapters argued, then something must organise them, and the obvious "
                  "candidate is the mind. Descartes and Kant are the great names behind the "
                  "view; the chapter's nearer targets are the French philosophers who taught it, "
                  "Jules Lagneau and his pupil Émile Chartier, who wrote as Alain. The chapter "
                  "sets out to show that the answer shares the question's premise; its word "
                  "<em>constitutes</em>, in the passage, is the phenomenologists' term for how "
                  "a consciousness brings its object into being for itself. It begins "
                  "with the history of a single concept, attention."),
            ("p", "For empiricism, attention follows from the constancy hypothesis. If what we "
                  "perceive does not match the stimulus, the normal sensations must still be "
                  "there, unperceived, and attention is what reveals them, as a searchlight "
                  "shows up objects already in the dark. It creates nothing; it is the same in "
                  "every act, as the beam is the same whatever it lights, and so it is a power "
                  "that can be turned anywhere and has no purposes of its own. Intellectualism "
                  "starts from the fruitfulness of attention instead. Descartes's wax was a "
                  "piece of extension from the start, and I grasp this clearly or confusedly as "
                  "I attend more or less; if I find a geometrical circle in a round plate, it "
                  "is because I had put it there."),
            ("p", "The intellectualist has a test, and the chapter reports it from Alain. "
                  "The moon on the horizon is not, and is not seen to be, bigger than at the "
                  "zenith: look at it through a cardboard tube or a telescope and its apparent "
                  "diameter stays the same. Inattentive perception contains nothing more than "
                  "the attentive kind. The test is the opponent's, and the reply comes on "
                  "page 36. The tube does not reveal the moon of free vision; it makes a "
                  "different, analytic kind of looking. When you look freely, the parts of the "
                  "field interact and motivate the enormous moon on the horizon, a measureless "
                  "size that is nevertheless a size."),
            ("p", "So the two theories of attention fail in opposite ways and for one reason. "
                  "Empiricism's consciousness is too poor for anything to call on it, "
                  "intellectualism's too rich. Empiricism cannot see that we need to know what "
                  "we are looking for, or we would not look; intellectualism cannot see that "
                  "&ldquo;we need to be ignorant of what we are looking for&rdquo;, or we would "
                  "not search. They agree that attention creates nothing. The chapter's own "
                  "account comes from the clinic and the nursery. The neurologist Henry Head put "
                  "patients' failure to locate a touch on their skin down to a local weakening of "
                  "attention; the chapter, following J. Stein's clinical reports, finds instead a "
                  "sensory field that shifts and shrinks while it is probed, so that attention's first work is "
                  "to make a field that stays still to be surveyed. Infants, for their first "
                  "nine months, tell only the coloured from the colourless, and colours proper "
                  "come later, as a new structure of experience."),
            ("def", ("Attention, on the chapter's account",
                     "Not the lighting of what was already there, and not the mind's return "
                     "to what it already held, but the active constitution of a new object, "
                     "which makes explicit what had been an indeterminate horizon.")),
            ("p", "The second half turns to judgement, introduced as what sensation lacks to "
                  "make a perception. Descartes looks from his window at men in the street and "
                  "asks what he sees: hats and coats, which might cover dummies worked by "
                  "springs. He does not see the men, he judges them to be there. Lagneau adds "
                  "that we have two eyes and so ought to see double, and that the single object "
                  "is constructed from two images. Perception becomes the interpretation of "
                  "signs the senses provide. That is the intellectualist's strongest argument: "
                  "once vision is defined in the empiricist way, as a quality impressed on the "
                  "body by the stimulus, the least "
                  "illusion, which gives the object properties it does not have on the retina, "
                  "proves that perception is a judgement."),
            ("p", "The chapter's objections follow one another fast. A large cardboard box feels "
                  "heavier than a small one of the same cardboard; intellectualism must say the "
                  "weight is judged, not felt, so that there is no sensory knowledge at all. A "
                  "cube drawn on paper changes its look, seen from above or from below, and "
                  "knowing it can be seen both ways does not make it change; knowledge has to "
                  "wait. And if we see what we judge, how could we tell true perception from "
                  "false, or say the man who hallucinates thinks he sees what he does not see? "
                  "The difference must lie in the sensible text the judgement shapes, so to "
                  "perceive is not to judge but to grasp a sense immanent in the sensible before "
                  "judgement begins."),
            ("p", "The lab tests the judgement-from-signs model on a case the book describes in "
                  "the previous chapter, on page 20, against association: a walk along a shore "
                  "towards a ship run aground, whose masts or funnel merge into the forest on "
                  "the dune behind. The model holds two interpretations of the upright forms, "
                  "<em>part of the forest behind</em> and <em>masts and funnel of the "
                  "ship</em>, and each cue removes whatever it does not fit. In the "
                  "<code>ship</code> preset the cues are c1, the upright forms where the ship "
                  "meets the forest, and c2, the same forms nearer with no new detail. Both "
                  "interpretations fit both cues, so at step 1 and step 2 the count tile prints "
                  "<code>2</code>, the candidates tile lists both, and the removed tile prints "
                  "<code>none</code>. The step range runs to 3; this preset has only two cues, "
                  "so the lab shows step 2 and the banner says so."),
            ("p", "The <code>close</code> preset adds c3, the forms seen at close quarters, the "
                  "same colour as the ship and fitting its superstructure. At step 3 the count "
                  "falls to <code>1</code>, the candidates tile prints <em>masts and funnel of "
                  "the ship</em>, and the removed tile names the forest. On the model the ship "
                  "is concluded there, from the sign that excludes the trees. The book's "
                  "description puts it elsewhere: &ldquo;there will be a moment when these "
                  "details suddenly become part of the ship&rdquo;, it says, after a tension "
                  "like a storm in storm clouds, and only afterwards does the walker find the "
                  "colour and the fit as justifications: &ldquo;these reasons for correct "
                  "perception were not given as reasons beforehand&rdquo;. The same page credits "
                  "Kant with seeing that such elements could not be associated until a synopsis, "
                  "a seeing-together, placed them in one object, so the model here is the psychologists' judgement "
                  "from signs, not Kant's synthesis."),
            ("p", "The chapter does not leave intellectualism there; it asks whether it has "
                  "caricatured it. Perhaps Descartes's judgement is a natural judgement, formed, "
                  "as the Sixth Meditation says, before there is time to weigh any reasons, so "
                  "that perception is a judgement unaware of its grounds, and the wax is a "
                  "unity before it is extension. That reading, the chapter grants, would make "
                  "perception an originating knowledge, and it may be the deepest sense of "
                  "Cartesianism. Its question is whether Descartes posited it, set it down as his doctrine, and its answer is "
                  "that he could have done so only by transforming his philosophy radically, "
                  "since the Meditations rest it in the end on a thought that possesses itself "
                  "absolutely."),
            ("p", "The last pages give the chapter's own word for what intellectualism misses. "
                  "Gestalt psychology showed that the supposed signs of distance, the apparent "
                  "size, the objects between, the disparity of the images, are not known as "
                  "signs in seeing distance, and then concluded that they must be causes. "
                  "Neither, the chapter says. Hide the intervening objects behind a screen and the "
                  "distance appears to shrink; yet there is no reason why a steeple should look "
                  "smaller and farther away when you can see the slopes and fields before it in "
                  "more detail. &ldquo;There is no reason, "
                  "but there is a motive.&rdquo;"),
            ("p", "Which brings the passage's thesis home. Intellectualism replaces a world in "
                  "itself acting on the eyes with a consciousness that thinks the world, and "
                  "leaves the world exactly as it was, parts outside parts, now doubled by a "
                  "thought. &ldquo;We pass from absolute objectivity to absolute subjectivity, "
                  "but this second idea is not better than the first and is upheld only "
                  "against it, which means by it.&rdquo; The two theories stand or fall "
                  "together, because they share the prejudice in favour of the objective world. "
                  "The last lesson of the course, “The Phenomenal Field”, reads the "
                  "chapter that names what is left once both have fallen."),
        ],
        "lab": ("phenkit", {
            "mode": "cues",
            "view": "sequence",
            "model": "perception as a judgement from signs",
            "cue_text": {
                "c1": "upright forms where the ship meets the forest",
                "c2": "the same forms, nearer, with no new detail",
                "c3": "the forms at close quarters, the same colour as the ship and fitting its superstructure",
            },
            "step": 3,
            "preset": "ship",
            "presets": [
                {"id": "ship",
                 "label": "The walk along the shore: cues c1 and c2 (the book's case, p. 20; the cues are the lesson's)",
                 "candidates": "part of the forest behind, c1 c2; masts and funnel of the ship, c1 c2 c3",
                 "cues": "c1, c2",
                 "expect": {"cuCount": "2",
                            "cuCandidates": "part of the forest behind, masts and funnel of the ship",
                            "cuRemoved": "none"}},
                {"id": "close",
                 "label": "And then at close quarters: cues c1, c2 and c3",
                 "candidates": "part of the forest behind, c1 c2; masts and funnel of the ship, c1 c2 c3",
                 "cues": "c1, c2, c3",
                 "expect": {"cuCount": "1", "cuCandidates": "masts and funnel of the ship",
                            "cuRemoved": "part of the forest behind"}},
            ],
            "panel_title": "What a judgement from signs can conclude",
            "panel_intro": (
                "This lab computes perception as a judgement from signs, the psychologists' "
                "intellectualism the chapter criticises: each interpretation is kept while it "
                "fits every cue so far, and the step control sets how many cues have arrived. "
                "The case is the book's; the coding of the cues is the lesson's."
            ),
        }),
        "steps_title": "Counting what a judgement from signs keeps",
        "steps_intro": "Four steps, the last of which is the lesson's.",
        "steps": [
            ("List the interpretations and their cues",
             "Write each candidate with the cues it is consistent with. Here the forest fits c1 "
             "and c2, the ship fits c1, c2 and c3."),
            ("Take the cues in order",
             "At each step keep only the candidates consistent with every cue so far, and note "
             "which candidate the latest cue removed."),
            ("Find the deciding step",
             "The model concludes at the first step where one candidate is left. If none is, "
             "it never decides."),
            ("Set the step beside the description",
             "Compare the model's deciding step with the book's account of the walk, in which "
             "the forms suddenly become part of the ship and the reasons are found afterwards. "
             "The model needs the sign first; the description gives the unity first."),
        ],
        "worked": {
            "title": "The walk towards the ship",
            "intro": [
                "Take the two interpretations, part of the forest behind and masts and funnel "
                "of the ship, and the cues c1, c2 and c3 in order. You want the count at each "
                "step and the step at which the model decides.",
            ],
            "lines": [
                "step 1, c1:  both fit; count 2, removed none",
                "step 2, c2:  both fit; count 2, removed none",
                "step 3, c3:  only the ship fits; count 1",
                "removed at step 3:  part of the forest behind",
            ],
            "after": [
                "Without c3 the model never decides, where the walker on page 20 has already "
                "seen the forms become part of the ship. With c3 it decides at the third step, "
                "from exactly the colour and fit that the book says were found as reasons only "
                "afterwards.",
            ],
        },
        "quiz_title": "Attention and judgement",
        "quiz": [
            {"q": "A judgement-from-signs model holds three interpretations: a flat shadow, fitting "
                  "c1; part of the forest behind, fitting c1 and c2; masts and funnel of the ship, "
                  "fitting c1, c2 and c3. After cues c1 and c2, what is the count, and what did c2 "
                  "remove?",
             "a": ["Count 2; c2 removed the flat shadow",
                   "Count 3; c2 removed nothing",
                   "Count 1; c2 removed the shadow and the forest",
                   "Count 2; c2 removed the ship"],
             "c": 0,
             "why": "Every interpretation fits c1. The shadow does not fit c2, so it goes, and the "
                    "forest and the ship remain. A count of 3 ignores c2; removing the forest "
                    "would need c3; and the ship fits every cue."},
            {"q": "On the chapter's account, what do the empiricist and intellectualist theories "
                  "of attention have in common?",
             "a": ["That attention creates nothing",
                   "That attention creates its object",
                   "That attention is a judgement",
                   "That attention is a sensation of effort"],
             "c": 0,
             "why": "The chapter says so in so many words: a world of impressions in itself or a "
                    "universe of determining thought leaves attention nothing to do. That "
                    "attention constitutes a new object is the chapter's own account, which both "
                    "theories miss. Neither theory makes attention a judgement or a sensation of "
                    "effort."},
            {"q": "Descartes, looking from his window, sees hats and coats. What does the "
                  "intellectualist conclude from the case?",
             "a": ["That he does not see the men but judges them to be there",
                   "That the men are associated with the hats by past experience",
                   "That perception gives the men before any judgement",
                   "That the hats and coats may be dummies, so nothing can be known"],
             "c": 0,
             "why": "The case is the intellectualist's showcase: the image of the men cannot be "
                    "on the retina, so they are judged. Association is the empiricist's account. "
                    "Perception before judgement is the chapter's reply, not Descartes's "
                    "conclusion, and Descartes raises the dummies to show that he judges, not to "
                    "deny all knowledge."},
            {"q": "Why, on the chapter's argument, does perception as judgement make it hard to "
                  "tell true perception from false?",
             "a": ["If we see what we judge, seeing and thinking one sees become the same thing",
                   "Judgements are always false, so every perception is an illusion",
                   "The judge cannot compare a perception with the stimulus",
                   "A hallucination is a sensation without any judgement"],
             "c": 0,
             "why": "The chapter asks where the difference between seeing and thinking one sees "
                    "would lie, and finds it only in the sensible text the judgement shapes, "
                    "which is perception before judgement. It does not call all judgements false. "
                    "Comparing with the stimulus is not the argument, and a hallucination, on the "
                    "intellectualist's view, is a judgement, an empty one."},
        ],
        "mistakes": [
            ("Thinking that refuting empiricism confirms intellectualism",
             "Intellectualism grew up as empiricism's opposite, so it seems that refuting one "
             "confirms the other. The chapter's claim is that both start from the same "
             "objective world and differ only in who builds the percept, the stimulus or the "
             "mind: the second idea is &ldquo;upheld only against it, which means by "
             "it&rdquo;. The lab shows the judgement model's half of this. In the "
             "<code>ship</code> preset it keeps <code>2</code> interpretations at every step "
             "and never concludes; in <code>close</code> it concludes at step 3, from a sign "
             "that excludes the trees, where on the book's description the unity arrived "
             "before any such sign."),
            ("Reading the deciding step as the moment of seeing",
             "Step 3 is where the model, holding a list of interpretations, is left with one. "
             "It is not when anyone sees the ship. On page 20 the forms become part of the ship "
             "suddenly, in a recasting that satisfies a vague expectation, and the colour and "
             "fit that the model needs as its third cue are found only afterwards."),
            ("Thinking the chapter dismisses Descartes",
             "The chapter considers the strongest reading of Descartes, the natural judgement "
             "of the Sixth Meditation formed before there is time to weigh reasons, and grants "
             "that it would make perception an originating knowledge. Its objection is that "
             "Descartes could have posited this only by transforming his philosophy, which in "
             "the end rests on a thought that possesses itself absolutely."),
        ],
        "standard": (
            "Finish when you can run the judgement model through its cues and say what it needs that the description does not.",
            "Given interpretations, each with the cues it fits, and an order of cues, compute "
            "the count, the candidates and the removed interpretation at each step and the "
            "step at which the model decides; then state why the chapter holds that empiricism "
            "and intellectualism stand on the same ground."
        ),
        "note": (
            "The walk along the shore is the book's case, from the previous chapter, where it "
            "is aimed at association; the interpretations, the cues and their coding are the "
            "lesson's, and testing the judgement model on it is the lesson's use of the case. "
            "The lab computes that model exactly. It cannot show the recasting the book "
            "describes, which on the chapter's account comes before any of the cues are "
            "available as reasons."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Smith p. 62 (opening passage, first sentence: "So, 'sensation' and
    # 'judgement' ... was maintained"); p. 66 (opening passage, second
    # sentence: "This phenomenal field is not an 'inner world' ... Bergson's
    # sense"; "classical science is a form of perception ..."); pp. 60-61 (le
    # sentir; Herder; the wheel; the candle); pp. 62-65 (faith in perception;
    # the living body as interiorless; the impartial spectator; "collapsing
    # before our eyes", p. 65); p. 67 (the rabbit in the foliage; the
    # immediate as meaning); p. 68 (not an irrational conversion but an
    # intentional analysis); pp. 69-71 (the transcendental field; "The Gestalt
    # of a circle ...", p. 70; the sun at two hundred yards, p. 71); p. 72
    # (Bergson's mistake and the reflective philosophies'); p. 73 ("Experience
    # anticipates a philosophy ..."). Cases coded: pp. 6, 8, 13 and 41 (the
    # illusion figures); p. 23 (the misprint); p. 20 (the ship); p. 33
    # (knowing and not knowing what is sought; attention creates nothing);
    # pp. 32 and 36 (the moon through a tube); p. 40 (the drawn cube).
    {
        "slug": "the-phenomenal-field",
        "title": "The Phenomenal Field",
        "module": "Introduction · IV · The Phenomenal Field",
        "one_line": "Once sensation and judgement have both lost their clearness, what is left is the phenomenal field: not an inner world of appearances, but the world as lived before it is split into inner and outer.",
        "summary": (
            "The Introduction's last chapter gathers the argument: sensation and judgement were "
            "clear only while the prejudice in favour of the world held, and their criticism "
            "opens a phenomenal field that is neither the objective world nor an inner one. "
            "Compute each classical account's record over the Introduction's cases as the "
            "lesson codes them, name the cases on which they part, and state what both "
            "assume."
        ),
        "key": [
            "sensation and judgement: clear together",
            "prejudice: the world taken as finished",
            "phenomenal field: not an inner world",
            "science: perception unaware of itself",
            "record = absorbs, fails, silent",
            "survivors: accounts with no fail",
            "split: one absorbs, the other fails",
        ],
        "key_label": "The Introduction's last chapter in seven lines",
        "concepts_intro": (
            "The chapter looks back over the Introduction and forward to the book. Three ideas "
            "carry it."
        ),
        "concepts": [
            ("The prejudice in favour of the world",
             "The assumption both classical accounts share: that the world is already there, "
             "fully determinate, and that perception is either its effect or a thought of it. "
             "The chapter says sensation and judgement were clear only while it held."),
            ("The phenomenal field",
             "The world as it is lived, before it is divided into an objective world and an "
             "inner one: meanings, structures and the arrangement of parts given together. "
             "The chapter is emphatic that it is not a private world of appearances."),
            ("The transcendental field",
             "What the phenomenal field becomes when reflection asks how every object is "
             "constituted through it. The chapter calls it a field because reflection never "
             "holds the whole world before it and is always partial."),
        ],
        "read_title": "The passage first, then the chapter's look back and forward",
        "read_intro": (
            "The passage joins the chapter's verdict on sensation and judgement to its denial "
            "that the phenomenal field is an inner world. The lesson reads both, then puts the "
            "Introduction's cases in one table."
        ),
        "body": [
            ("p", "<strong>Introduction, Chapter 4, pp. 62 and 66.</strong> &ldquo;So, "
                  "&lsquo;sensation&rsquo; and &lsquo;judgement&rsquo; have together lost "
                  "their apparent clearness: we have observed that they were clear only as long "
                  "as the prejudice in favour of the world was maintained. &hellip; This "
                  "phenomenal field is not an &lsquo;inner world&rsquo;, the "
                  "&lsquo;phenomenon&rsquo; is not a &lsquo;state of consciousness&rsquo;, or a "
                  "&lsquo;mental fact&rsquo;, and the experience of phenomena is not an act of "
                  "introspection or an intuition in Bergson&rsquo;s sense.&rdquo; The first "
                  "sentence is on page 62 of Smith's translation, the second on page 66. Read "
                  "the whole chapter, pages 60 to 74, in your own copy before going on."),
            ("p", "The chapter opens by giving sense experience back its mystery. Smith's "
                  "<em>sense experience</em> translates the French <em>le sentir</em>, the "
                  "feeling or sensing that empiricism had flattened into the possession of a "
                  "quality. Ordinary usage knows better, the chapter says, and so did Romantic "
                  "usage, that of the eighteenth-century German writer Johann Gottfried Herder "
                  "for example. Kurt Koffka supplies the cases: a wooden wheel lying on the ground is not, for sight, the same as "
                  "a wheel bearing a load, and a candle flame changes its look for a child who "
                  "has been burned, from something that draws the hand to something repulsive. "
                  "Vision is already inhabited by a meaning, and quality comes with a value for "
                  "the heavy mass that is our body."),
            ("p", "Now the passage's first sentence. Sensation and judgement lost their "
                  "clearness together, and the order of the chapters showed why: each was clear "
                  "only so long as the world was taken for granted as finished and determinate, "
                  "and the moment either was used to describe perception as it happens, it "
                  "became inconceivable. The criticism of the constancy hypothesis, and more "
                  "generally the setting aside of the idea of the world, opened a phenomenal "
                  "field, and the chapter's task is to say what it is and what it is not."),
            ("p", "First, where the prejudice came from. Science and philosophy, the chapter "
                  "says, have lived for centuries on an unquestioning faith in perception, which "
                  "opens a window on things and seems to promise that every experience can be "
                  "fitted with every other into one unbroken text. Science followed that promise "
                  "to the end, and made the living body a thing without an inside and the "
                  "thinking subject an impartial spectator with no place in the world. It could "
                  "then be held, as Alain and Léon Brunschvicg held, that perception is an "
                  "incipient science. The chapter reverses the formula: "
                  "&ldquo;classical science is a form of perception which loses sight of its "
                  "origins and believes itself complete&rdquo;."),
            ("p", "Second, what the field is not, which is the passage's second sentence. It "
                  "would be easy to hear the return to phenomena as a turn inward, to private "
                  "appearances known by introspection. Henri Bergson, the French philosopher "
                  "who had asked his readers to go back to the immediate data of consciousness, "
                  "is the chapter's example of how that goes wrong: an immediate known only by "
                  "coinciding with it is a lonely, blind and mute life that cannot even be said. "
                  "The phenomenal is understood, as you understand when you find the rabbit in "
                  "the foliage of a puzzle or catch a slight gesture. After the criticism of "
                  "sensation, the immediate is no longer the impression but the meaning, the "
                  "structure, the spontaneous arrangement of parts, and a face or a signature is "
                  "given with its sense."),
            ("def", ("The phenomenal field",
                     "The layer of lived experience through which things and other people are "
                     "first given, prior to the objective world and not inside the mind: what "
                     "the Introduction's criticism of sensation and judgement leaves standing.")),
            ("p", "The chapter then follows psychology one step past itself. Once the psychologist "
                  "takes the Gestalt as the theme, the meaning of what is perceived no longer "
                  "comes from sensations meeting by accident, and the phenomenal field becomes a "
                  "transcendental field, the place where every object is constituted. The "
                  "classical transcendental philosopher would now complete the analysis and "
                  "recognise one true subject, the thinking Ego; that, the chapter adds, is to "
                  "all appearances the programme of Husserl's transcendental phenomenology too, "
                  "as most of his works set it out. The chapter refuses the step. The form "
                  "is not the outcome of a law laid down beforehand: &ldquo;The Gestalt of a "
                  "circle is not its mathematical law but its physiognomy&rdquo;, the look it "
                  "has, as a face has one. Reflection "
                  "cannot stop me seeing the sun two hundred yards away on a misty day, and the "
                  "philosopher's thinking is always situated."),
            ("p", "The two mistakes the Introduction has been tracking turn out to mirror each "
                  "other. Bergson's, the chapter says, is to think the knower can fuse with what "
                  "it knows; the reflective philosophies' is to think the knower can absorb what "
                  "it knows into its thought without remainder. We are never the unreflective "
                  "subject we try to know, and never wholly the consciousness that would know it. "
                  "That is why a philosophy becomes radical by treating its own presumption to "
                  "total knowledge as the fundamental problem."),
            ("p", "The lab puts the Introduction's cases in one table, as the lesson codes them. "
                  "Each row is a case from the Introduction, and each cell says whether, on the "
                  "chapters' arguments, the account absorbs the case (y), fails it (n), or is "
                  "silent (-). Empiricism's column carries the constancy hypothesis, association "
                  "and the projection of memories; intellectualism's, attention as elucidation "
                  "and perception as judgement. The <code>intro</code> preset shows all eight "
                  "rows. The record tile counts each column: empiricism absorbs 1 of 8 and fails "
                  "7, intellectualism absorbs 2, fails 5 and is silent on 1. The survivors tile, "
                  "the accounts with no failure, prints <code>none</code>. The Müller-Lyer row is "
                  "coded n for intellectualism by the argument of page 41, on Zöllner's figure, "
                  "where calling an illusion a mistaken judgement leaves the mistake unexplained."),
            ("p", "The split tile lists the rows where one account absorbs and the other fails: "
                  "<em>the misprinted word</em>, <em>knowing what is sought</em> and <em>not "
                  "knowing what is sought</em>. The misprint is coded y for intellectualism "
                  "because, read as an interpretation of signs, a misreading is a false "
                  "judgement it can describe; the chapter's objection to that, that it then "
                  "cannot tell seeing from thinking one sees, comes on the page of the drawn "
                  "cube and is coded in that row. The two "
                  "attention rows are page 33, where empiricism cannot see that we must know "
                  "what we look for and intellectualism that we must not. The ship is coded "
                  "silent for intellectualism, because page 20 aims it at association and "
                  "credits Kant on the very point. Every other row fails both."),
            ("p", "The other presets take the table apart. <code>sensation</code> keeps the rows "
                  "from Chapters 1 and 2, the Müller-Lyer lines, the misprint and the ship: "
                  "empiricism absorbs none of the three, intellectualism one, and the split is "
                  "the misprinted word alone. <code>attention</code> keeps the three attention "
                  "rows, and the accounts part in opposite directions on two of them and fail "
                  "together on the third, attention making a new object. <code>shared</code> "
                  "keeps the moon through a tube and the drawn cube, where the split is "
                  "<code>none</code>: both fail, and for the same reason."),
            ("p", "Read the record with care. It is not a ranking, and intellectualism's 2 "
                  "against empiricism's 1 says only which cases the lesson chose to code. The "
                  "Introduction's claim is not that one account does better but that both fail "
                  "from one shared prejudice in favour of the objective world, which is the "
                  "reason behind every <code>n</code> and appears in no cell. Merleau-Ponty's own "
                  "account is not a column. Scored by the lesson, it would have a clean sheet "
                  "because the lesson coded it so; it is stated in prose instead: what perception "
                  "first gives is the phenomenal field, the meaning and the arrangement given "
                  "together, and "
                  "the coding of every cell is the lesson's reading of the chapters, not the "
                  "book's."),
            ("p", "The chapter closes on why the book had to begin with psychology. Without the "
                  "psychologist's descriptions the transcendental problem would not be "
                  "understood, and without philosophy the descriptions would not be seen to be "
                  "true; the book could begin neither without psychology nor with psychology "
                  "alone. &ldquo;Experience anticipates a philosophy and philosophy is merely an "
                  "elucidated experience.&rdquo; The next course, The Lived Body, enters the "
                  "phenomenal field by the body, beginning with “Experience and Objective "
                  "Thought”, the introduction to Part One."),
        ],
        "lab": ("phenkit", {
            "mode": "cases",
            "view": "table",
            "accounts": ["empiricism", "intellectualism"],
            "preset": "intro",
            "presets": [
                {"id": "intro",
                 "label": "The Introduction's eight cases, as the lesson codes them",
                 "observations": ("the Müller-Lyer lines, n, n; the misprinted word, n, y; "
                                  "the ship on the shore, n, -; knowing what is sought, n, y; "
                                  "not knowing what is sought, y, n; attention making a new object, n, n; "
                                  "the moon through a tube, n, n; the drawn cube, n, n"),
                 "expect": {"caRecord": "empiricism: absorbs 1 of 8, fails 7, silent 0; "
                                        "intellectualism: absorbs 2 of 8, fails 5, silent 1",
                            "caSurvivors": "none",
                            "caSplit": "the misprinted word, knowing what is sought, not knowing what is sought"}},
                {"id": "sensation",
                 "label": "Chapters 1 and 2: the lines, the misprint and the ship",
                 "observations": ("the Müller-Lyer lines, n, n; the misprinted word, n, y; "
                                  "the ship on the shore, n, -"),
                 "expect": {"caRecord": "empiricism: absorbs 0 of 3, fails 3, silent 0; "
                                        "intellectualism: absorbs 1 of 3, fails 1, silent 1",
                            "caSurvivors": "none", "caSplit": "the misprinted word"}},
                {"id": "attention",
                 "label": "Chapter 3 on attention: three cases",
                 "observations": ("knowing what is sought, n, y; not knowing what is sought, y, n; "
                                  "attention making a new object, n, n"),
                 "expect": {"caRecord": "empiricism: absorbs 1 of 3, fails 2, silent 0; "
                                        "intellectualism: absorbs 1 of 3, fails 2, silent 0",
                            "caSurvivors": "none",
                            "caSplit": "knowing what is sought, not knowing what is sought"}},
                {"id": "shared",
                 "label": "Two cases both accounts fail: the moon and the drawn cube",
                 "observations": "the moon through a tube, n, n; the drawn cube, n, n",
                 "expect": {"caSurvivors": "none", "caSplit": "none"}},
            ],
            "panel_title": "The two accounts across the Introduction",
            "panel_intro": (
                "This lab counts the lesson's coding of the Introduction's cases against the two "
                "classical accounts, empiricism and intellectualism: each cell is y (absorbs), n "
                "(fails) or - (silent). The count is exact and the coding is an interpretation. "
                "Merleau-Ponty's own account is not a column."
            ),
        }),
        "steps_title": "Reading the accounts' record",
        "steps_intro": "Five steps, the last of which is the lesson's.",
        "steps": [
            ("Code each case",
             "For each case and each account, record y if the chapter's argument lets the "
             "account absorb the case, n if it fails it, and - if the chapter says nothing of "
             "that account there."),
            ("Count each column",
             "For each account count the y, n and - cells. That is its record over the cases "
             "shown."),
            ("Find the survivors",
             "An account survives if it has no n. With every account failing somewhere, there "
             "are none."),
            ("Find the split",
             "List the cases where one account has y and the other n. Silent cells do not "
             "split."),
            ("Name what the table does not show",
             "State the reason the chapter gives for the failures, the shared prejudice in "
             "favour of the objective world, which is in no cell, and say that the coding is "
             "the lesson's reading."),
        ],
        "worked": {
            "title": "Eight cases, two accounts",
            "intro": [
                "Take the intro preset's eight rows. You want each account's record, the "
                "survivors and the split.",
            ],
            "lines": [
                "empiricism:  y 1, n 7, silent 0",
                "intellectualism:  y 2, n 5, silent 1",
                "survivors:  none",
                "split:  the misprint, and the two attention rows",
                "both fail:  the lines, attention, the moon, the cube",
            ],
            "after": [
                "Neither account survives, and they part on three rows, in both directions. "
                "Where both fail, the chapters give one reason for both: each assumes the "
                "objective world. The record is not a ranking, and the split is the lesson's "
                "coding, not the book's.",
            ],
        },
        "quiz_title": "The phenomenal field",
        "quiz": [
            {"q": "A table has three cases: the first coded n for empiricism and y for "
                  "intellectualism, the second y and n, the third n and -. What do the survivors "
                  "and split tiles print?",
             "a": ["Survivors none; split the first and second cases",
                   "Survivors intellectualism; split the first case",
                   "Survivors none; split all three cases",
                   "Survivors empiricism; split the second case"],
             "c": 0,
             "why": "Each account has an n, empiricism in the first and third rows and "
                    "intellectualism in the second, so none survives. The first two rows are y "
                    "against n; the third is n against silent, which does not split. Choosing an "
                    "account as survivor overlooks its n."},
            {"q": "What, according to the chapter, made sensation and judgement seem clear?",
             "a": ["The prejudice in favour of the world, while it was maintained",
                   "Careful introspection of one's own states",
                   "The success of physiology in tracing the nerves",
                   "Their agreement with the Gestalt psychologists"],
             "c": 0,
             "why": "That is the passage's first sentence. Introspection is what the chapter "
                    "denies the phenomenal field is reached by. Physiology's picture of the "
                    "transmitter was found wanting in Chapter 1, and the Gestalt psychologists "
                    "are among those whose findings undid both notions."},
            {"q": "Which of these does the chapter say the phenomenal field is not?",
             "a": ["An inner world of states of consciousness known by introspection",
                   "Prior to the objective world",
                   "The layer through which things and other people are first given",
                   "Something consciousness forgets in favour of the things it presents"],
             "c": 0,
             "why": "That is the passage's second sentence. The chapter does place the field "
                    "before the objective world, as the layer through which others and things are "
                    "first given, and it says consciousness forgets its phenomena in favour of "
                    "things, though it can always recall them."},
            {"q": "On the intro preset, intellectualism absorbs 2 cases and empiricism 1. What "
                  "follows, on the lesson's reading?",
             "a": ["Nothing about which account is better: the counts depend on the cases coded, "
                   "and both fail from one shared prejudice",
                   "Intellectualism is the better account of perception",
                   "Merleau-Ponty sides with intellectualism against empiricism",
                   "A third case for empiricism would make the accounts equal and the table "
                   "complete"],
             "c": 0,
             "why": "The Introduction's claim is that both fail symmetrically, from the "
                    "prejudice in favour of the objective world, and the lesson says the record "
                    "is not a ranking. Chapter 3 argues that intellectualism stands on the same "
                    "ground as empiricism, and no number of cases completes a coding that is "
                    "itself an interpretation."},
        ],
        "mistakes": [
            ("Taking the phenomenal field for a private inner world",
             "Returning to phenomena sounds like turning inward, to appearances only I can "
             "inspect. The chapter places the field before the split into inner and outer: it "
             "is the world as it is lived, not a mental picture of it, and it is "
             "&ldquo;not an &lsquo;inner world&rsquo;&rdquo;. In the lab the point shows as "
             "an absence. Every row is a case in the world, a pair of lines, a printed word, a "
             "ship, the moon, and in the <code>intro</code> preset neither account survives, "
             "<code>none</code>, without any row being an inner state."),
            ("Reading the record as a ranking",
             "Intellectualism absorbs 2 of 8 and empiricism 1 of 8, and it is tempting to "
             "conclude that the book prefers the first. The counts depend on which cases the "
             "lesson coded and how; the Introduction's claim is that both fail from one shared "
             "prejudice, and Chapter 3 is written to show that intellectualism is on the same "
             "level as empiricism."),
            ("Expecting Merleau-Ponty's own column",
             "If the table scored his account it would come out clean, because the lesson would "
             "have coded it to. That would be a decoration and an endorsement at once. His "
             "account is stated in prose: the phenomenal field, in which meaning, structure and "
             "the arrangement of parts are given together, before any division into inner and "
             "outer."),
        ],
        "standard": (
            "Finish when you can compute the accounts' record and say what no cell shows.",
            "Given a coded table of cases against two accounts, compute each account's record, "
            "the survivors and the split; then state the prejudice the chapter says both "
            "accounts share, and why the phenomenal field is not an inner world."
        ),
        "note": (
            "Every cell is the lesson's reading of the Introduction, and a reader may code a "
            "case differently: the misprint for intellectualism and the ship are the "
            "arguable ones, and the lesson says why it codes them as it does. The lab counts "
            "the coding exactly. It cannot show the shared prejudice that the chapter says lies "
            "behind every failure, and it does not score Merleau-Ponty's own account."
        ),
    },
]
