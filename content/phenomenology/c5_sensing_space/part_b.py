"""Sensing and Space, lessons 5-8 -- Part Two, Chapter 2, Space, one lesson per section.

Every quotation is copied from Colin Smith's translation, Routledge Classics
pagination (Chapter 2, pp. 283-347); the comment beside each lesson gives its
pages. Smith prints no headings inside the chapter. The four sections are
separated by blank lines in the text and begin on p. 283 (the chapter's
opening; up and down from p. 284), p. 297 ("Traditional ideas of perception
are at one in denying that depth is visible"), p. 311 ("Movement is a
displacement or change of position") and p. 327 ("We have so far considered
... only the perception of space"). Smith's ligatures are printed as plain
letters, a word split by a line-break hyphen is joined, and footnote numerals
are left out. Nothing else is changed.
"""

LESSONS = [
    # ---------------------------------------------------------------- 05
    # Smith p. 289 (opening passage: "If we so contrive it that a subject
    # sees the room ... 'slantwise'." and "After a few minutes a sudden
    # change occurs ... become vertical."; Wertheimer's mirror, from his
    # Experimentelle Studien); pp. 283-284 (Kant; space as the means whereby
    # the position of things becomes possible; spatialized and spatializing
    # space; "top" and "bottom"); pp. 284-285 (Stratton's two experiments;
    # footnote 4: "This is, at least implicitly, Stratton's interpretation");
    # pp. 285-287 (the associationist interpretation); p. 287 ("But this
    # interpretation is unintelligible."; "'Inverted' or 'upright', in
    # themselves, obviously have no meaning."); p. 288 (intellectualism);
    # p. 289 (a third spatiality; the spatial level); p. 290 (anchoring
    # points; Nagel's stick); p. 291 ("My body is wherever there is something
    # to be done."; "a certain gearing of my body to the world"); p. 292
    # (systematic yet piecemeal; the tune sung in another key; footnote 16,
    # the pseudophone); p. 293 ("space always precedes itself"); pp. 294-295
    # (the inverted face; "To invert an object is to deprive it of its
    # significance."); pp. 295-296 (the first level; giddiness and nausea).
    {
        "slug": "up-and-down",
        "title": "Up and Down",
        "module": "Part Two · 2 · Space · Up and Down",
        "one_line": "Up and down are not given by the retinal image or fixed by thought; the chapter argues that they come from a spatial level, the body's hold on a spectacle it can live in, which can tilt as a whole.",
        "summary": (
            "The chapter on space begins with up and down, and with two experiments: "
            "Stratton's spectacles, which turned the visual world upside down for a week, and "
            "Wertheimer's mirror, in which a tilted room suddenly rights itself. Compute "
            "perceived tilt as image tilt minus a spatial level, period by period, under a "
            "sudden and under a gradual re-anchoring, in the lesson's own model, and say what "
            "the chapter means by a level."
        ),
        "key": [
            "no content is upright in itself",
            "perceived tilt = image tilt − level",
            "Wertheimer: the level jumps at once",
            "Stratton: systematic but piecemeal",
            "the body: where something is to be done",
            "space always precedes itself",
        ],
        "key_label": "Up and down in six lines",
        "concepts_intro": (
            "The section asks what it means for something to look the right way up. Three "
            "ideas carry its answer."
        ),
        "concepts": [
            ("Spatialized and spatializing space",
             "Kant's alternative, as the chapter states it: either I live among things and "
             "take space vaguely as their setting, or I reflect and find space as the act of "
             "a subject who traces all its relations. The section looks for a third kind of "
             "spatiality, neither of things nor of a thinking subject."),
            ("The spatial level",
             "The orientation in relation to which a spectacle is upright or tilted. It is "
             "not given by the image and not chosen by thought; it is set when the body's "
             "possible actions and the spectacle come into gear, and it can tilt to a new "
             "position as a whole."),
            ("Anchoring points",
             "Wertheimer's term for the things in a spectacle, walls, doors, a person "
             "walking, that take it upon themselves to give the vertical when a new level "
             "forms."),
        ],
        "read_title": "The passage first, then the section line by line",
        "read_intro": (
            "The passage is Wertheimer's mirror, as the chapter reports it. The lesson goes "
            "back to the chapter's first page, follows Stratton's experiment and the two "
            "interpretations the chapter rejects, returns to the mirror and the spatial "
            "level, and ends with the inverted face and the first level."
        ),
        "body": [
            ("p", "<strong>Space, p. 289.</strong> &ldquo;If we so contrive it that a subject "
                  "sees the room in which he is, only through a mirror which reflects it at an "
                  "angle at 45° to the vertical, the subject at first sees the room "
                  "&lsquo;slantwise&rsquo;. &hellip; After a few minutes a sudden change "
                  "occurs: the walls, the man walking about the room, and the line in which the "
                  "cardboard falls become vertical.&rdquo; The sentences are on page 289 of "
                  "Smith's translation. Smith prints no section headings in this chapter; the "
                  "section on up and down runs from the chapter's first page, 283, to the end "
                  "of the paragraph on giddiness and nausea on page 296. Read those pages in "
                  "your own copy before going on."),
            ("p", "The experiment is Max Wertheimer's, from his 1912 study of seen movement, the "
                  "paper usually taken as the start of Gestalt psychology. In the mirror the "
                  "man walking about the room seems to lean as he goes, and a piece of "
                  "cardboard falling down the door-frame seems to fall obliquely; the whole "
                  "effect is odd. Then, after a few minutes, everything is vertical again. The "
                  "chapter values the experiment for one feature: the righting is sudden and "
                  "needs no exploration by movement. The bearings are taken, it says, by a "
                  "global act of the perceiving subject."),
            ("p", "Now back to the chapter's first page. Kant drew a strict line between space as "
                  "the form of outer experience and the things given in it. Space is not a "
                  "container, since that relation holds only between things, nor a class to "
                  "which things belong, since it comes before its parts: on Kant's view, as the "
                  "chapter states it, space is the means by which the position of things "
                  "becomes possible. So either I do not reflect, and live among things taking "
                  "space vaguely as their setting, or I reflect and pass from spatialized to "
                  "spatializing space, finding a single power to trace out all directions. "
                  "The chapter's question is whether that alternative is forced, and its "
                  "method is to look at an experience of space, up and down, in a case where "
                  "it comes apart and forms again."),
            ("def", ("Spatialized and spatializing space",
                     "Space as the setting in which things already lie, with its regions of up "
                     "and down, near and far; and space as the act of a subject who traces "
                     "and sustains all spatial relations, homogeneous and the same in every "
                     "direction.")),
            ("p", "The case is George Stratton's. Stratton, an American psychologist, wore "
                  "spectacles that inverted the image on the retina, which the eye's lens "
                  "normally inverts already. In a first short experiment the landscape looked "
                  "unreal and upside down, and on the second day normal perception began to "
                  "return while his body felt upside down. In a second, lasting a week, "
                  "things looked inverted at first; from the second day the landscape was no "
                  "longer inverted but the body felt wrongly placed; from the third day to the "
                  "seventh the body gradually righted itself, above all when he was active. "
                  "Actions found their target from the fifth day. Sounds were placed correctly "
                  "only when their source was also seen. When the spectacles came off, things "
                  "looked not inverted but queer, and he reached with the wrong hand."),
            ("p", "The first interpretation the chapter gives in another's voice: at least "
                  "implicitly, a footnote says, Stratton's own. The visual world is given "
                  "turned through 180°, like the pictures in a book someone has turned round, "
                  "while the world of touch stays the right way; the two conflict until "
                  "movement guided by sight builds stable associations between the old "
                  "directions and the new, and the name top is transferred to where the head "
                  "appears. &ldquo;But this interpretation is unintelligible.&rdquo; Head and "
                  "feet in the image could give the field a direction only if they had one "
                  "themselves, and &ldquo;&lsquo;Inverted&rsquo; or &lsquo;upright&rsquo;, in "
                  "themselves, obviously have no meaning.&rdquo; Intellectualism fares no "
                  "better. If up and down are relations to axes a mind chooses, each axis is "
                  "placed only by another and the task of taking bearings is postponed for "
                  "ever; and since a constituting mind sees from nowhere and every objective "
                  "relation survives the spectacles, it cannot even grant that the world "
                  "looked upside down."),
            ("p", "Hence the spatial level. Before the experiment perception recognizes a "
                  "certain level, in relation to which the mirrored room looks tilted; during "
                  "it the spectacle induces another level, in relation to which the whole "
                  "field is upright again. Certain objects act as anchoring points and draw "
                  "the vertical to themselves. The level is not the body's own orientation: a "
                  "subject who tilts his head holds a stick tilted when asked to hold it "
                  "upright, but the vertical follows the head only when the field is empty, in "
                  "the dark. What counts is the body as a system of possible actions. "
                  "&ldquo;My body is wherever there is something to be done.&rdquo; In "
                  "Wertheimer's mirror the subject at first does not inhabit the room; after a "
                  "few minutes the reflected room calls up a subject who could live in it, and "
                  "he feels he has the arms and legs he would need to walk and act there. The "
                  "level is &ldquo;a certain gearing of my body to the world&rdquo;."),
            ("p", "The lab computes a model the lesson builds to illustrate this, and no theory "
                  "says it: perceived tilt is image tilt minus spatial level, period by "
                  "period. The <code>wertheimer</code> preset has an image tilted 45° and a "
                  "level of 0° that jumps to 45° at period 3; the series tile prints 45°, 45°, "
                  "0°, 0°, 0°. The period is illustrative; the suddenness is the book's. The "
                  "perceived-tilt and level tiles show the period the slider is set to, 45° "
                  "and 0° at period 1. The <code>stratton</code> preset has an image turned "
                  "180° and a level that moves half the remaining way each period, so the "
                  "series is 180°, 90°, 45°, 45/2°, 45/4°; the halving is the lesson's "
                  "illustration, not Stratton's figures. The <code>none</code> preset has "
                  "nothing tilted, and the series is 0° throughout."),
            ("p", "The two rules stand for the chapter's two readings. For Wertheimer it is the "
                  "jump that matters: the level is re-anchored as a whole, not corrected point "
                  "by point. For Stratton it is that the change was systematic and yet "
                  "piecemeal and progressive. Association could not make it systematic, whole "
                  "regions falling into line together; a change of coordinates by thought "
                  "could not explain why hearing and the unseen body lagged behind. So I go "
                  "from one system of positions to the other without the key to either, the "
                  "chapter says, as someone with no knowledge of music sings in another key a "
                  "tune he has heard. Notice what Stratton reported and the model does not: no "
                  "single moment at which the world turned back over. The chapter takes his "
                  "descriptions and sets aside his interpretation, and how far the reports "
                  "support its reading of them is something later readers still argue about."),
            ("p", "The section ends by turning the question round. For a thinking subject a face "
                  "the right way up and the same face upside down are indistinguishable; for "
                  "the perceiving subject the inverted face is unrecognizable. Look for long "
                  "enough at someone lying on a bed from the head of the bed, and the face "
                  "becomes terrifying, eyelashes and eyebrows taking on a strange materiality. "
                  "&ldquo;To invert an object is to deprive it of its significance.&rdquo; The "
                  "French word <em>sens</em>, the translator notes, means both sense and "
                  "direction. And a level always presupposes an earlier one: &ldquo;space "
                  "always precedes itself&rdquo;. The first level can be anchored nowhere, so "
                  "my first hold on the world must be the resumption of a pre-personal "
                  "tradition: another subject beneath me, my body as a system of anonymous "
                  "functions, for whom a world exists before I am here. When levels give way, "
                  "the result is not only disorder but giddiness and nausea, the felt "
                  "awareness of that contingency."),
            ("p", "The level gives up and down. Depth is harder, because it seems to belong to the "
                  "perceiver and not to the things at all. The next lesson, “Depth”, reads the "
                  "section in which the chapter takes on Berkeley and the geometry of the "
                  "eyes."),
        ],
        "lab": ("phenkit", {
            "mode": "level",
            "view": "tilt",
            "model": "the lesson's model: perceived tilt as image tilt minus the spatial level",
            "preset": "wertheimer",
            "presets": [
                {"id": "wertheimer",
                 "label": "Wertheimer's mirror: image 45°, level re-anchored at period 3 (period illustrative)",
                 "image": 45, "level": 0, "rule": "switch", "at": 3,
                 "expect": {"lePerceived": "45°", "leLevel": "0°", "leSeries": "45°, 45°, 0°, 0°, 0°"}},
                {"id": "stratton",
                 "label": "Stratton's spectacles: image 180°, level halving the gap each period (illustrative)",
                 "image": 180, "level": 0, "rule": "share", "share": "1/2",
                 "expect": {"leSeries": "180°, 90°, 45°, 45/2°, 45/4°"}},
                {"id": "none",
                 "label": "Nothing tilted: image 0°, level 0°",
                 "image": 0, "level": 0, "rule": "switch",
                 "expect": {"leSeries": "0°, 0°, 0°, 0°, 0°"}},
            ],
            "panel_title": "Perceived tilt against a spatial level",
            "panel_intro": (
                "This lab computes the lesson's model, which no theory states: perceived tilt "
                "is the image's tilt minus the spatial level, with the level re-anchored "
                "suddenly or a share of the way each period. Move the period slider to see "
                "each period; the series tile shows the first five."
            ),
        }),
        "steps_title": "Computing tilt against a level, period by period",
        "steps_intro": "Five steps; the model is the lesson's, and the last step says so.",
        "steps": [
            ("Fix the image tilt",
             "Take the tilt of the image in degrees: 45° for Wertheimer's mirror, 180° for "
             "Stratton's spectacles."),
            ("Set the starting level",
             "Take the level the subject brings, 0° at period 1."),
            ("Apply the rule",
             "Under a switch the level jumps to the image's tilt at the given period; under a "
             "share it moves that fraction of the remaining difference each period."),
            ("Subtract",
             "Perceived tilt in the model is image tilt minus level, period by period."),
            ("Say what the model is",
             "State that the subtraction is the lesson's illustration, that the suddenness is "
             "Wertheimer's report and the halving is not Stratton's, and that the chapter's "
             "level is the body's gearing to the spectacle, not a quantity."),
        ],
        "worked": {
            "title": "The mirror, period by period",
            "intro": [
                "Take the wertheimer preset: an image tilted 45°, a level of 0° that jumps to "
                "45° at period 3. You want the model's perceived tilt at each period.",
            ],
            "lines": [
                "period 1:  45 − 0 = 45°",
                "period 2:  45 − 0 = 45°",
                "period 3:  the level jumps to 45°",
                "period 3:  45 − 45 = 0°",
                "periods 4 and 5:  0°",
            ],
            "after": [
                "The model's figure changes all at once because the level does, and that is the "
                "one feature taken from the report: the room righted itself suddenly, without "
                "the subject moving about. Nothing in the report says when, and the chapter's "
                "level is not a number subtracted from another; it is the body's hold on a room "
                "it could live in.",
            ],
        },
        "quiz_title": "Levels",
        "quiz": [
            {"q": "In the wertheimer preset the level jumps from 0° to 45° at period 3. What "
                  "does the model give at periods 2 and 4?",
             "a": ["45° and 0°", "45° and 45°", "0° and 0°", "45/2° and 0°"],
             "c": 0,
             "why": "At period 2 the level is still 0°, so `45 − 0 = 45`. From period 3 it is "
                    "45°, so period 4 gives `45 − 45 = 0`. Half of 45 would be the share rule, "
                    "not the switch."},
            {"q": "In the stratton preset the image is turned 180° and the level moves half the "
                  "remaining way each period. What does the model give at period 4?",
             "a": ["45/2°", "45°", "90°", "0°"],
             "c": 0,
             "why": "The series halves: 180, 90, 45, then `45/2`. Forty-five is period 3, ninety "
                    "period 2, and under a share the model never reaches 0°."},
            {"q": "Why does the chapter call the associationist interpretation of Stratton "
                  "unintelligible?",
             "a": ["Head and feet in the image would need a direction of their own to give "
                   "one to the field",
                   "Stratton's subject never adapted at all",
                   "Associations take longer than a week to form",
                   "The spectacles did not really invert the image"],
             "c": 0,
             "why": "The interpretation makes up and down follow the apparent position of head "
                    "and feet, and the chapter replies that no content is upright or inverted "
                    "in itself. Stratton's subject did adapt, the chapter makes nothing of how "
                    "long associations take, and it does not dispute that the image was "
                    "inverted."},
            {"q": "What does Wertheimer's mirror show that Stratton's spectacles do not?",
             "a": ["Up and down redistributed at once, without any exploration by movement",
                   "That the body's own orientation fixes the vertical",
                   "That the spatial level never changes",
                   "That up is wherever the top of the retinal image is"],
             "c": 0,
             "why": "The chapter says the experiment's advantage is an instantaneous "
                    "redistribution of high and low without motor exploration. It shows the "
                    "visual field imposing an orientation that is not the body's, the level does "
                    "change, and the mirror leaves the retinal image tilted throughout."},
        ],
        "mistakes": [
            ("Thinking up is where the top of the retinal image is",
             "At its strongest this is the realist's view: the image carries its orientation, "
             "and perception reads it off. Stratton's spectacles invert the image, and after "
             "days the subject's world is upright with the image still inverted; Wertheimer's "
             "mirror tilts the image 45° and after a few minutes the room is vertical with the "
             "image unchanged. In the lesson's model the series goes 45°, 45°, 0° while the "
             "image stays at 45°. The chapter's conclusion is that the orientation registered "
             "on the retina does not govern up and down, and that the level is re-anchored as a "
             "whole, not corrected bit by bit."),
            ("Thinking the spatial level is the body's own orientation",
             "The chapter says the level is not to be confused with the orientation of one's "
             "own body. A tilted head drags the vertical with it only in an empty field or in "
             "the dark, and in the mirror the room comes upright while the subject's body is "
             "as it was. What sets the level is the body as a system of possible actions, a "
             "virtual body with a place defined by its task."),
            ("Taking the model's subtraction for the chapter's theory",
             "Nothing in the chapter says perceived tilt is image tilt minus a level. The "
             "subtraction is the lesson's way of putting a number on the one feature the "
             "reports give, sudden or gradual. The chapter's level is a gearing of the body to "
             "the world, and the figure leaves out what makes it one: a room the subject could "
             "walk about in and act."),
        ],
        "standard": (
            "Finish when you can compute tilt against a level under both rules and say what the chapter means by a level.",
            "Given an image tilt, a starting level and a rule, compute the lesson's model of "
            "perceived tilt period by period, say which feature of Wertheimer's or Stratton's "
            "reports each rule illustrates, and state why the chapter rejects both the "
            "associationist and the intellectualist account of up and down."
        ),
        "note": (
            "The model is the lesson's. No theory says that perceived tilt is image tilt minus "
            "a level, the period of Wertheimer's switch is illustrative, and the halving is not "
            "in Stratton's reports, which describe a piecemeal change with hearing and the "
            "unseen body lagging. The lab cannot compute what makes a level a level on the "
            "chapter's account, the body's possible actions in a room it can live in."
        ),
    },
    # ---------------------------------------------------------------- 06
    # Smith p. 297 (opening passage: "Traditional ideas of perception are at
    # one in denying that depth is visible." ... "In both cases depth is
    # tacitly equated with breadth seen from the side, and this is what
    # makes it invisible."; Berkeley; the spectator from the side); p. 298
    # ("For God, who is everywhere, breadth is immediately equivalent to
    # depth."; depth the most existential dimension); p. 299 (apparent size;
    # "The distance is the height of a triangle with its base and base
    # angles given to me", in the traditional view's voice, footnote
    # Malebranche; the blind man's two sticks); p. 300 (natural geometry;
    # Gestalt: conditions or causes); p. 301 ("Convergence and apparent size
    # are neither signs nor causes of depth"; motive); p. 302 (the journey;
    # the horizon moon); pp. 303-304 (the ash-tray; the road; "he is anterior
    # to equality and inequality; he is the same man seen from farther
    # away"); p. 305 ("there is disparity only for a subject who tries to
    # fuse monocular phenomena"); pp. 306-308 (the reversible cube, Koffka;
    # depth as envelopment); pp. 308-310 (depth as temporal; field of
    # presence); pp. 310-311 (primordial depth; a level of distances).
    {
        "slug": "depth",
        "title": "Depth",
        "module": "Part Two · 2 · Space · Depth",
        "one_line": "The classical theories make depth invisible by treating it as breadth seen from the side and then rebuild it from signs; the chapter argues that convergence and apparent size are motives of a depth already seen, not signs or causes of it.",
        "summary": (
            "The section on depth begins with what Berkeley and the intellectualists agree on: "
            "that depth is not visible. Compute the convergence of the eyes and the binocular "
            "disparity for two distances, as the classical theory of depth from signs computes "
            "them, and state what that theory says the mind does with them and why the chapter "
            "says nobody does it."
        ),
        "key": [
            "depth: not breadth seen from the side",
            "convergence = eye separation / distance",
            "disparity = difference of convergences",
            "signs presuppose the space they give",
            "neither signs nor causes: motives",
        ],
        "key_label": "Depth in five lines",
        "concepts_intro": (
            "The section runs for fifteen pages and covers the whole classical theory of "
            "depth. Three ideas carry it."
        ),
        "concepts": [
            ("Depth as breadth seen from the side",
             "What the chapter says both classical theories assume: that depth is a row of "
             "points like breadth, which I happen to see end-on, and which a spectator off to "
             "the side would see spread out."),
            ("Signs of depth",
             "In the classical theory, the facts from which distance is worked out: the angle "
             "at which the two eyes converge, and an object's apparent size against its known "
             "size."),
            ("Motive",
             "The chapter's alternative to sign and cause: an antecedent that acts only through "
             "its significance, as a death motivates a journey, and whose force is given by "
             "the decision it motivates."),
        ],
        "read_title": "The passage first, then the section line by line",
        "read_intro": (
            "The passage is the section's first paragraph, compressed. The lesson follows the "
            "section in order: Berkeley and analytical reflection, the signs of depth, the "
            "psychologists' causes, the chapter's motives, apparent size, and depth as a "
            "temporal dimension."
        ),
        "body": [
            ("p", "<strong>Space, p. 297.</strong> &ldquo;Traditional ideas of perception are at "
                  "one in denying that depth is visible. &hellip; In both cases depth is "
                  "tacitly equated with breadth seen from the side, and this is what makes it "
                  "invisible.&rdquo; The sentences are on page 297 of Smith's translation, "
                  "which prints no heading for the section; it begins with the first of them "
                  "and ends on page 311, before the paragraph that begins with movement. Read "
                  "pages 297 to 311 in your own copy before going on."),
            ("p", "George Berkeley, the Irish philosopher and later bishop, argued in his 1709 "
                  "<em>New Theory of Vision</em> that distance is not seen. The chapter gives "
                  "his argument two forms. The retina receives only a flat projection of the "
                  "spectacle, so depth has no means of being recorded; and if one objects that "
                  "after the criticism of the constancy hypothesis, the assumption that each "
                  "point of the stimulus gives one fixed sensation, we cannot judge what we see "
                  "by the retinal image, Berkeley would reply that depth still cannot be seen, "
                  "because it is not spread out before the eyes but appears to them only "
                  "foreshortened. Analytical reflection reaches the same verdict for "
                  "theoretical reasons: even a recorded depth would be a multiplicity that "
                  "has to be run over and held together, so that distance exists only for a "
                  "subject who synthesizes it. The two doctrines are opposed, the chapter "
                  "says, and make the same assumption."),
            ("p", "Made explicit, the assumption is this. What I call depth is really a row of "
                  "points like breadth, and I am badly placed to see it; a spectator looking "
                  "on from the side would take in at a glance the objects that, for me, hide "
                  "one another. What makes depth invisible to me is what makes it visible to "
                  "him as breadth. So the depth declared invisible is already a depth "
                  "identified with breadth. To treat it so, the subject must leave his place and "
                  "think himself into a kind of ubiquity: &ldquo;For God, who is everywhere, "
                  "breadth is immediately equivalent to depth.&rdquo; Yet the chapter grants "
                  "Berkeley one thing outright: depth is not imprinted on the object but plainly "
                  "belongs to the perspective, which makes it the most existential of the "
                  "dimensions."),
            ("p", "Then the classical theory itself, stated in its own voice. My table is near, "
                  "the piano farther, the car drives off. These words, it is maintained, mean "
                  "intervals I cannot see from where I am, revealed by the apparent size of "
                  "things against their real size and by the eyes, which converge as an object "
                  "approaches. &ldquo;The distance is the height of a triangle with its base "
                  "and base angles given to me&rdquo;: the base is the distance between the "
                  "eyes and the base angles are given by their convergence. The footnote cites "
                  "Malebranche, Descartes's follower, and the picture goes back to Descartes's "
                  "<em>Optics</em> of 1637, where the eyes are like a blind man's two sticks "
                  "that run together as the object comes near. The Cartesians called the "
                  "calculation a natural geometry. Berkeley denied that anyone performs a "
                  "geometry and put in its place signs learned by experience: a feeling of the "
                  "eyes turning that custom has joined to distance."),
            ("p", "The chapter's reply is that the signs presuppose what they are meant to "
                  "give. I can go back from apparent size to distance only if I already know "
                  "there is a world of undistortable objects and that my body stands before "
                  "it like a mirror. I can read convergence as a sign of distance only if I "
                  "picture my gaze as the blind man's two sticks, which puts my eyes, my body "
                  "and the world in one objective space. Natural geometry and natural "
                  "judgement, it concludes, are myths in Plato's sense: stories that stand for "
                  "a significance enveloped in the signs, before either signs or significance "
                  "is posited."),
            ("p", "The lab computes the classical theory, in the small-angle form in which an "
                  "angle is a length over a distance. With the eyes 6.5 cm apart, the "
                  "<code>near</code> preset puts two points at 50 cm and 60 cm. The convergence "
                  "tile gives `6.5 / 50 = 13/100` rad for the first and `6.5 / 60 = 13/120` rad "
                  "for the second, and the disparity tile, the difference between them, "
                  "`13/600`, about `0.0217` rad. The <code>far</code> preset moves both points "
                  "ten times farther, to 500 cm and 600 cm, and the disparity falls to `13/6000`, "
                  "a tenth. The <code>interval</code> preset keeps the same 10 cm interval as "
                  "<code>near</code> but five metres off, 500 cm and 510 cm, and gives "
                  "`13/51000`, one eighty-fifth of the near figure. The <code>equal</code> "
                  "preset puts both at 50 cm, and the disparity is 0."),
            ("p", "These are the figures the theory says the mind uses, and the chapter's first "
                  "objection is that nobody has them. I am not expressly aware of my eyes' "
                  "convergence or of an apparent size when I see something far off. The "
                  "second is that the disparity the theory starts from is not there to start "
                  "from: &ldquo;there is disparity only for a subject who tries to fuse "
                  "monocular phenomena&rdquo;, two images that are disparate only for a gaze "
                  "already tending towards one thing. The figures are exact, and they are the "
                  "model's; the lesson's comparisons between presets are the model's too."),
            ("p", "The Gestalt psychologists, Kurt Koffka and Paul Guillaume among them, had "
                  "already seen that convergence and apparent size are not explicitly known "
                  "in perception, and concluded that they are not signs but conditions or "
                  "causes of depth, a law to be recorded like a law of physics. The chapter "
                  "says the psychologist here begins a pure description and then interrupts "
                  "it to put himself back in the world. Its own conclusion: &ldquo;Convergence "
                  "and apparent size are neither signs nor causes of depth&rdquo;. They are "
                  "present in the experience of depth as a motive is present in a decision. "
                  "A death motivates my journey because it is a situation that calls for my "
                  "presence, and in deciding to go I make the motive valid; the relation runs "
                  "both ways."),
            ("def", ("Motive",
                     "An antecedent that acts only through its significance, not by any "
                     "physical power, and whose force is confirmed by what it motivates: a "
                     "death and the journey to the funeral.")),
            ("p", "Apparent size gets the same treatment. Asked what diameter I see an ash-tray "
                  "as having, I cannot answer with both eyes open; I shut one, hold a pencil "
                  "at arm's length and mark it, and by isolating the ash-tray I make size "
                  "appear where it had no place. The sides of a road running to the horizon are "
                  "neither given as converging nor as parallel: they are parallel in depth. And "
                  "is not a man smaller at two hundred yards than at five? Only if I isolate "
                  "him and measure. Otherwise &ldquo;he is anterior to equality and inequality; "
                  "he is the same man seen from farther away&rdquo;, a figure that offers my "
                  "gaze less to hold."),
            ("p", "The section ends by making depth temporal. To see an object at a distance is "
                  "already to hold it, or still to hold it, as I still have in hand the moment "
                  "just past without any recollection in between; the chapter borrows "
                  "Husserl's field of presence, which spreads in two dimensions, here and "
                  "there, past and future. Beneath depth between things lies a primordial "
                  "depth, the thickness of a medium with no thing in it: one patient, writing, "
                  "has to push his pen through a certain thickness of whiteness before reaching "
                  "the paper. And like up and down, far and near come to things from a level of "
                  "distances and sizes, the scope of our gestures. Depth, in the chapter's "
                  "account of the reversible cube, is the dimension in which things envelop "
                  "one another, as breadth and height are those in which they lie side by "
                  "side."),
            ("p", "Space so far has been still. The next lesson, “Movement”, reads the section in "
                  "which a line of light moves without passing through the space between, and "
                  "Zeno's old argument comes back."),
        ],
        "lab": ("phenkit", {
            "mode": "depth",
            "view": "binocular",
            "model": "the classical theory of depth from signs",
            "unit": "cm",
            "preset": "near",
            "presets": [
                {"id": "near", "label": "Eyes 6.5 cm apart; points at 50 cm and 60 cm",
                 "iod": "6.5", "near": 50, "far": 60,
                 "expect": {"deConvergence": "50 cm: 13/100 = 0.1300 rad; 60 cm: 13/120 ≈ 0.1083 rad",
                            "deDisparity": "13/600 ≈ 0.0217 rad"}},
                {"id": "far", "label": "The same eyes; points at 500 cm and 600 cm",
                 "iod": "6.5", "near": 500, "far": 600,
                 "expect": {"deDisparity": "13/6000 ≈ 0.0022 rad"}},
                {"id": "interval", "label": "The near preset's 10 cm interval, five metres off: 500 cm and 510 cm",
                 "iod": "6.5", "near": 500, "far": 510,
                 "expect": {"deDisparity": "13/51000 ≈ 0.0003 rad"}},
                {"id": "equal", "label": "Both points at 50 cm",
                 "iod": "6.5", "near": 50, "far": 50,
                 "expect": {"deDisparity": "0 rad"}},
            ],
            "panel_title": "Convergence and disparity, as the classical theory computes them",
            "panel_intro": (
                "This lab computes the classical theory of depth from signs, in its small-angle "
                "form: each point's convergence is the eyes' separation over its distance, in "
                "radians, and the disparity is the difference. The chapter's claim is that no "
                "perceiver performs this calculation."
            ),
        }),
        "steps_title": "Computing convergence and disparity",
        "steps_intro": "Four steps, and a fifth that is the chapter's.",
        "steps": [
            ("Put everything in one unit",
             "Write the separation of the eyes and the two distances in centimetres."),
            ("Compute each convergence",
             "Divide the separation by each distance: the angle in radians, in the small-angle "
             "form the theory uses. At 6.5 cm and 50 cm that is 13/100."),
            ("Take the difference",
             "The disparity is the nearer point's convergence minus the farther's."),
            ("Compare presets",
             "Ten times the distances gives a tenth of the disparity; the same interval farther "
             "off gives much less."),
            ("Say whose calculation it is",
             "State that the figures are the classical theory's, and that the chapter denies "
             "both that anyone has them in seeing depth and that they cause it."),
        ],
        "worked": {
            "title": "Two points near the eyes",
            "intro": [
                "Take the near preset: eyes 6.5 cm apart, points at 50 cm and 60 cm. You want "
                "each point's convergence and the disparity, as the classical theory computes "
                "them.",
            ],
            "lines": [
                "50 cm:  6.5 / 50 = 13/100 = 0.1300 rad",
                "60 cm:  6.5 / 60 = 13/120 ≈ 0.1083 rad",
                "disparity:  13/100 − 13/120 = 13/600",
                "in decimals:  ≈ 0.0217 rad",
                "at 500 and 600 cm:  13/6000, a tenth",
            ],
            "after": [
                "On the classical theory these are the data from which the mind works out that "
                "one point is behind the other. The chapter's reply is not that the arithmetic "
                "is wrong but that no one who sees the two points has it: the disparity exists "
                "only for a gaze already trying to see one thing.",
            ],
        },
        "quiz_title": "Signs, causes and motives",
        "quiz": [
            {"q": "With the eyes 6.5 cm apart, what convergence does the classical theory give "
                  "for a point 65 cm away?",
             "a": ["1/10 rad", "10 rad", "13/100 rad", "1/65 rad"],
             "c": 0,
             "why": "`6.5 / 65 = 1/10`. Ten radians is the ratio upside down, `13/100` is the "
                    "figure for 50 cm, and `1/65` forgets the separation."},
            {"q": "With the eyes 6.5 cm apart, what disparity does the classical theory give for "
                  "points at 50 cm and 100 cm?",
             "a": ["13/200 rad", "13/100 rad", "13/300 rad", "0 rad"],
             "c": 0,
             "why": "The convergences are `13/100` and `13/200`, and the difference is `13/200`. "
                    "`13/100` is the nearer convergence alone, `13/300` uses the sum of the "
                    "distances, and 0 needs both points at one distance."},
            {"q": "On the chapter's reading, what do Berkeley and analytical reflection share "
                  "about depth?",
             "a": ["Both tacitly equate depth with breadth seen from the side",
                   "Both hold that depth is directly visible",
                   "Both derive depth from the physiology of the brain",
                   "Both treat convergence as a motive"],
             "c": 0,
             "why": "That is the passage's second sentence. Both deny that depth is visible, the "
                    "brain is the Gestalt psychologists' resort, and the motive is the chapter's "
                    "own alternative."},
            {"q": "How, on the chapter's account, are convergence and apparent size present in "
                  "the experience of depth?",
             "a": ["As a motive is present in a decision",
                   "As signs from which the distance is worked out",
                   "As causes, recorded like a law of physics",
                   "Not at all"],
             "c": 0,
             "why": "The chapter says they are neither signs nor causes, and compares them to a "
                    "motive in a decision. Signs are the classical theory, causes the Gestalt "
                    "psychologists', and the chapter grants that they do enter into the "
                    "perception of distance, as the stereoscope shows."},
        ],
        "mistakes": [
            ("Thinking we see depth by calculating from convergence",
             "This is the natural geometry of Descartes's <em>Optics</em> and of Malebranche, "
             "whom the chapter cites, and, with the geometry replaced by signs learned by "
             "association, Berkeley's <em>New Theory of Vision</em>. At its strongest it says "
             "the eyes supply exact data, `13/100` and `13/120` rad for points at 50 and 60 cm, "
             "a disparity of `13/600`, and the mind does the rest. The chapter states it and "
             "rejects it: nobody is aware of these figures, the disparity exists only for a gaze "
             "trying to fuse two images, and the signs could give space only to someone who "
             "already had it. The lab computes the calculation the chapter says nobody "
             "performs."),
            ("Taking convergence for a cause of depth",
             "That is the Gestalt psychologists' correction of the sign theory, and the chapter "
             "rejects it too. A cause would make experience a by-product recorded after the "
             "fact; the chapter's choice is that either experience is nothing or it must be "
             "total. Convergence is present in seeing depth as a motive in a decision, acting "
             "through its significance."),
            ("Thinking the far man is seen smaller and then corrected",
             "The constancy theories say the man two hundred yards off is a smaller image "
             "enlarged by the mind, or a compromise between his near and his projected size. "
             "The chapter says he is smaller only if isolated and measured; seen in his "
             "context he is neither smaller nor equal, but the same man seen from farther away, "
             "offering the gaze less to hold."),
        ],
        "standard": (
            "Finish when you can compute convergence and disparity and say what the chapter puts in place of signs and causes.",
            "Given the eyes' separation and two distances, compute each convergence and the "
            "disparity as the classical theory does, compare presets, state the assumption the "
            "chapter finds in both classical theories, and explain why it calls convergence a "
            "motive and not a sign or a cause."
        ),
        "note": (
            "The lab computes the classical theory in its small-angle form, which treats an "
            "angle as a length over a distance; the exact angles differ in the fourth decimal "
            "place, and the comparisons between presets are the lesson's. What the lab cannot "
            "compute is the chapter's claim, that these figures are not had by anyone who sees "
            "depth."
        ),
    },
    # ---------------------------------------------------------------- 07
    # Smith pp. 313-314 (opening passage: "If we present to a subject
    # alternately two lines of light A and B ... ceaselessly moving back and
    # forth."); p. 312 (the stone thrown across the garden; the stone
    # decomposed); p. 313 ("Zeno's arguments become valid once more"); p. 314
    # (two simultaneous or two successive lines; the rod C; "We have not a
    # 'passage of the line', but a pure 'passage'."; the workmen; the pencil);
    # p. 315 (the Haunted House; the psychologist's reply); pp. 315-316 (the
    # logician, Linke: the watch, the fakir, the circle; Smith prints
    # Wertheimer's phenomenon as "phenomenon ø"); pp. 317-318 (both
    # vindicated; "is not identical beneath the phases of movement, it is
    # identical in them"); p. 319 ("the mobile entity has only a style");
    # p. 320 ("merely a greyish power of flight"); pp. 321-322 (Bergson, note
    # 47); pp. 322-325 (the stone, the ship, the steeple, the eye); pp. 325-
    # 326 ("Like top and bottom, motion is a phenomenon of levels"); p. 326
    # (the train, Koffka).
    {
        "slug": "movement",
        "title": "Movement",
        "module": "Part Two · 2 · Space · Movement",
        "one_line": "Movement is not one identical thing passing through every position, nor a passing with nothing that passes; the chapter argues that what moves is identical in its moving, given only as moving.",
        "summary": (
            "The section on movement sets a logician, for whom movement must be the movement "
            "of one identical thing, against Wertheimer's stroboscopic movement, in which a "
            "line moves without crossing the space between. Compute the speed two alternating "
            "lights imply and whether an interval falls in the band in which motion is "
            "reported, and say what the chapter makes of the thing that moves."
        ),
        "key": [
            "an identical moving body: Zeno returns",
            "stroboscopic: a passing, not a path",
            "speed = separation / interval",
            "motion seen: lights alternate in the band",
            "identical in its phases, not beneath",
            "motion is a phenomenon of levels",
        ],
        "key_label": "Movement in six lines",
        "concepts_intro": (
            "The section is a debate between a logician and a psychologist, and the chapter "
            "says both are right. Three ideas carry it."
        ),
        "concepts": [
            ("Stroboscopic movement",
             "The movement seen between two lights flashed in alternation with nothing between "
             "them, which Wertheimer studied in 1912. At one speed of alternation one line is "
             "seen moving back and forth; faster or slower, two lines."),
            ("The mobile entity",
             "The chapter's name for what moves, as distinct from an object defined by its "
             "properties: something that is identical in the phases of its movement, given only "
             "as beginning, pursuing or completing it."),
            ("Anchorage",
             "The background that movement needs, given not by fixed objects posited in "
             "advance but by where the gaze is lodged: the one we look at moves."),
        ],
        "read_title": "The passage first, then the section line by line",
        "read_intro": (
            "The passage is the chapter's report of Wertheimer's experiment. The lesson goes "
            "back to the stone that opens the section and to Zeno, reads the experiment, the "
            "logician's objection and the chapter's verdict on both, and ends with movement "
            "as a phenomenon of levels."
        ),
        "body": [
            ("p", "<strong>Space, pp. 313&ndash;14.</strong> &ldquo;If we present to a subject "
                  "alternately two lines of light A and B, the subject sees a continuous "
                  "movement from A to B, then from B to A, then again from A to B and so on, "
                  "even though no intermediate position or indeed the extreme positions be "
                  "given for themselves; we have one single line ceaselessly moving back and "
                  "forth.&rdquo; The sentence runs from page 313 to page 314 of Smith's "
                  "translation. The section has no printed heading; it begins on page 311 with "
                  "a paragraph on movement as a change of position and ends on page 327. Read "
                  "pages 311 to 327 in your own copy before going on."),
            ("p", "Throw a stone across a garden. For a moment it becomes an indistinct, "
                  "meteor-like streak, then a stone again where it lands. Now think about it "
                  "clearly, the section says, and it comes apart. The stone itself is not "
                  "changed by moving: it is the same stone I held and the same I find on the "
                  "ground, so it was the same stone in the air. Movement is an accidental "
                  "attribute of it, a change in its relations to its surroundings. If the stone "
                  "were abolished at one point and another identical stone arose at the next, "
                  "there would be two movements, not one; so there is no movement without one "
                  "moving body carrying it from start to finish, no movement without a "
                  "landmark, and no absolute movement. That is the objective idea of "
                  "movement, at its strongest."),
            ("p", "And yet, the chapter says, this idea is a negation of movement. If the stone "
                  "in motion is not in some way different from the stone at rest, it is never "
                  "in motion. Zeno of Elea, in the fifth century BC, argued that a flying arrow "
                  "at each instant occupies a space equal to itself and so is at rest at every "
                  "instant; the chapter's point is that as soon as we bring in a moving body "
                  "identical throughout, &ldquo;Zeno’s arguments become valid once more&rdquo;. "
                  "Infinitely small instants and points do not help: whatever two positions "
                  "we take, the act of passing from one to the other cannot be conceived in "
                  "one identical body. Thinking clearly about movement, I do not understand how "
                  "it ever begins for me."),
            ("p", "Now the passage. Max Wertheimer flashed two lines of light in alternation and "
                  "his subjects saw one line moving back and forth, though nothing lit the "
                  "space between. Quicken or slow the alternation and the line is first held "
                  "at A and then jumps to B; go further, and there are two lines at once or "
                  "two in succession. The perception of positions, the chapter concludes, "
                  "varies inversely as that of movement. With a short rod C placed between A "
                  "and B, the rod is never completed by the movement passing over it: "
                  "&ldquo;We have not a &lsquo;passage of the line&rsquo;, but a pure "
                  "&lsquo;passage&rsquo;.&rdquo; Real movements are the same. Watching workmen "
                  "throw bricks, I see the arm at the start and at the end, never between, and "
                  "have a vivid perception of movement; slow a moving pencil down until you can "
                  "keep it in view, and the impression of movement disappears."),
            ("def", ("Stroboscopic movement",
                     "Movement seen between two stationary lights flashed one after the other, "
                     "with nothing shown in between. Wertheimer called the pure case, in "
                     "which movement is seen and no moving thing, the phi phenomenon.")),
            ("p", "The lab computes Wertheimer's bands as later textbooks report them; the "
                  "thresholds are not in Merleau-Ponty. Below an interval of about 30 ms the "
                  "two lights are seen together, above about 200 ms one after the other, and "
                  "between them motion is reported. The bands also shift with distance and "
                  "intensity, as Adolf Korte's laws of 1915 describe, and the lab keeps them "
                  "fixed. In the <code>simultaneous</code> preset the lights are 5 cm apart "
                  "with 20 ms between them: the speed tile prints `5 / 20 = 1/4` cm per ms, and "
                  "the band tile prints seen together. In the <code>optimal</code> preset the "
                  "interval is 60 ms, `1/12` cm per ms, and the band is motion. In the "
                  "<code>succession</code> preset it is 250 ms, `1/50` cm per ms, and the band "
                  "is seen in succession."),
            ("p", "Notice what the speed tile is a figure of. It is the speed a body would need "
                  "to cross the gap in the interval, which is the objective idea of movement "
                  "turned into arithmetic: one thing, every position, a time. In the "
                  "experiment nothing crosses the gap, and the space between is never lit. The "
                  "figure is the model's, and what the band tile names is what the textbooks "
                  "report subjects saying, not anything the lab sees."),
            ("p", "Then the logician answers the psychologist. The chapter's logician is Paul "
                  "Linke, a German philosopher of Husserl's school who wrote on phenomenology "
                  "and the experiments on seen movement. All movement must be movement of something: if "
                  "my watch vanished from the table and reappeared a few seconds later in the "
                  "next room, nobody would say it had moved. When a fakir changes an egg into a "
                  "handkerchief there must be one something presented in two forms. To speak "
                  "of a movement with no moving thing is mere verbiage unless we say how what "
                  "is given is conveyed as movement. The psychologist replies that movement is "
                  "a dynamic phenomenon, whose passing effect is its flesh and blood and cannot "
                  "be built from ordinary visual contents."),
            ("p", "The chapter's verdict is that both are right. The logician is right to demand "
                  "something that moves and wrong to make its identity an express identity. "
                  "The psychologist is right to describe the phenomenon faithfully, and his "
                  "description already has a moving something in it, conceived concretely. "
                  "What Wertheimer means, the chapter says, is that the moving thing is not "
                  "perceived here, then there, and identified afterwards. The mobile entity "
                  "&ldquo;is not identical beneath the phases of movement, it is identical in "
                  "them&rdquo;. I do not believe the stone was one stone in flight because I find "
                  "it on the ground; I go to pick it up because I saw it one in its flight. As "
                  "the circle before Euclid had no diameters, though it could not have unequal "
                  "ones, so &ldquo;the mobile entity has only a style&rdquo;: the bird crossing "
                  "the garden is, while it moves, &ldquo;merely a greyish power of "
                  "flight&rdquo;."),
            ("p", "A long note sets this against Henri Bergson, the French philosopher of "
                  "duration, who tried to rescue movement by dissolving positions in a "
                  "consciousness of fusion. If the phases of movement merge into one another, "
                  "the chapter replies, nothing is anywhere in motion. Then the section turns "
                  "to relativity. I cannot make myself see the stone at rest and the garden and "
                  "myself in motion; and yet movement is given in a field. On a ship along the "
                  "coast, as Leibniz said, either the coast flows by or the ship glides; of a "
                  "cloud over a steeple, the one we look at moves. Playing cards in a train, the "
                  "chapter quotes the Gestalt psychologist Kurt Koffka, I see the next train move off even when it is mine "
                  "that starts. &ldquo;Like top and bottom, motion is a phenomenon of "
                  "levels&rdquo;, every movement presupposing an anchorage that can change."),
            ("p", "So far the chapter has treated space as a disinterested subject might know it. "
                  "The next lesson, “Lived Space”, reads the section in which night, dreams, myth "
                  "and the experience of patients show a spatiality underneath that one."),
        ],
        "lab": ("phenkit", {
            "mode": "motion",
            "view": "phi",
            "model": "Wertheimer's bands, as later textbooks report Wertheimer (1912); not in Merleau-Ponty",
            "unit": "cm",
            "preset": "optimal",
            "presets": [
                {"id": "simultaneous", "label": "Lights 5 cm apart, 20 ms between them",
                 "separation": 5, "interval": 20,
                 "expect": {"moSpeed": "1/4 cm per ms", "moBand": "seen together"}},
                {"id": "optimal", "label": "Lights 5 cm apart, 60 ms between them",
                 "separation": 5, "interval": 60,
                 "expect": {"moSpeed": "1/12 cm per ms", "moBand": "motion"}},
                {"id": "succession", "label": "Lights 5 cm apart, 250 ms between them",
                 "separation": 5, "interval": 250,
                 "expect": {"moSpeed": "1/50 cm per ms", "moBand": "seen in succession"}},
            ],
            "panel_title": "Two lights in alternation",
            "panel_intro": (
                "This lab computes Wertheimer's bands as later textbooks report them, with "
                "thresholds of 30 ms and 200 ms that are not in Merleau-Ponty: the speed a body "
                "would need to cross the gap, and the band an interval falls in. Nothing in the "
                "experiment crosses the gap."
            ),
        }),
        "steps_title": "Computing an implied speed and a band",
        "steps_intro": "Four steps; the thresholds are the textbooks', not the book's.",
        "steps": [
            ("Take the separation and the interval",
             "Write the distance between the lights in centimetres and the time between the "
             "flashes in milliseconds."),
            ("Divide",
             "The implied speed is separation over interval: 5 cm in 60 ms is 1/12 cm per ms."),
            ("Place the interval in a band",
             "Below the simultaneity threshold, about 30 ms, the lights are reported together; "
             "above the succession threshold, about 200 ms, one after the other; between, as "
             "motion."),
            ("Say what the speed is a speed of",
             "State that the speed is that of a body crossing the gap, the objective idea of "
             "movement, and that in the experiment nothing crosses it."),
        ],
        "worked": {
            "title": "Two lights at three intervals",
            "intro": [
                "Take the three presets: lights 5 cm apart at 20, 60 and 250 ms. You want the "
                "implied speed and the band each time.",
            ],
            "lines": [
                "20 ms:  5 / 20 = 1/4 cm per ms; below 30",
                "band:  seen together",
                "60 ms:  5 / 60 = 1/12 cm per ms; in the band",
                "band:  motion",
                "250 ms:  5 / 250 = 1/50 cm per ms; above 200",
                "band:  seen in succession",
            ],
            "after": [
                "Only the middle interval gives motion, and at that interval the speed tile "
                "describes a journey nobody sees: the space between the lights is never lit. "
                "What is reported is a line moving, and the chapter's question is what that "
                "line is, if it is not an object passing through every point.",
            ],
        },
        "quiz_title": "What moves",
        "quiz": [
            {"q": "Two lights 6 cm apart flash 120 ms apart, with the lab's thresholds of 30 ms "
                  "and 200 ms. What are the implied speed and the band?",
             "a": ["1/20 cm per ms; motion", "20 cm per ms; motion",
                   "1/20 cm per ms; seen in succession", "1/20 cm per ms; seen together"],
             "c": 0,
             "why": "`6 / 120 = 1/20` cm per ms, and 120 ms lies between 30 and 200, so the band "
                    "is motion. Twenty is the ratio upside down; succession needs more than "
                    "200 ms and simultaneity less than 30."},
            {"q": "Which observation does the chapter report to show that movement is not the "
                  "successive occupation of every position between two extremes?",
             "a": ["A short rod placed between A and B is never completed by the passing "
                   "movement",
                   "A watch that vanishes and reappears in the next room",
                   "A stone found again on the ground where it fell",
                   "Two lights flashed at the same moment"],
             "c": 0,
             "why": "The rod is the chapter's case: the movement passes and the rod is not "
                    "filled in. The watch is the logician's example of no movement at all, the "
                    "stone found on the ground is the objective idea's evidence for one "
                    "identical stone, and lights flashed together give no movement."},
            {"q": "What does the chapter conclude about the thing that moves?",
             "a": ["It is not identical beneath the phases of movement, but identical in them",
                   "There is none: a pure passing with nothing that passes",
                   "It is an object posited apart from its movement",
                   "It is inferred by a judgement linking two positions"],
             "c": 0,
             "why": "That is the chapter's sentence on page 318. A passing with nothing that "
                    "passes is the reading of Wertheimer the chapter declines; an object posited "
                    "apart and a judgement linking positions are the logician's and the "
                    "intellectualist's accounts, which it rejects."},
            {"q": "Playing cards in a train, in the passage the chapter quotes from Koffka, "
                  "which train do I see move off?",
             "a": ["The neighbouring train, even if it is really mine that is starting",
                   "Always my own train",
                   "Whichever train is actually moving",
                   "Neither train"],
             "c": 0,
             "why": "Absorbed in the compartment, I take it as at rest, so the other train seems "
                    "to leave. When I look at the other train to pick out someone, my own is set "
                    "in motion; which one moves depends on where I am anchored, not on which is "
                    "actually moving."},
        ],
        "mistakes": [
            ("Thinking motion is a succession of positions of one identical thing",
             "This is the assumption Zeno's argument trades on and the classical theory keeps: "
             "one stone, the same at every point, passing through every position in turn. The "
             "lab turns it into a speed, `1/12` cm per ms for 5 cm in 60 ms, the speed of a "
             "body nobody sees, since in Wertheimer's experiment the space between is never "
             "lit. But the chapter does not answer it with a motion of nothing. What moves is "
             "there, indeterminate and given only in its moving: identical in the phases of "
             "the movement, not beneath them, with a style rather than properties."),
            ("Reading the chapter as siding with the psychologist against the logician",
             "The chapter says both must be considered vindicated. The logician is right that "
             "there is no movement without something that moves, which the bare phi "
             "phenomenon seems to deny; he is wrong to demand that its identity be an express "
             "identity. The psychologist describes better, but his description already puts a "
             "moving something into the movement."),
            ("Concluding that movement is relative, since the anchorage can change",
             "The coast flows by or the ship glides, depending on where I look, and that sounds "
             "like the logician's relativity. The chapter says the opposite: to call motion a "
             "structural phenomenon is not to call it relative. Once I am lodged in a setting, "
             "motion appears before me as an absolute; what is relative is only my power to "
             "change the setting."),
        ],
        "standard": (
            "Finish when you can compute an implied speed and a band and say what moves on the chapter's account.",
            "Given the separation and interval of two alternating lights, compute the implied "
            "speed and the band with the stated thresholds, say what the speed is a speed of, "
            "and state the chapter's verdict on the logician and the psychologist and its "
            "account of the mobile entity."
        ),
        "note": (
            "The thresholds are those later textbooks report for Wertheimer's 1912 experiments, "
            "not figures in Merleau-Ponty, and the real bands move with the distance and "
            "brightness of the lights. The lab computes a speed and a band; it cannot compute "
            "the movement subjects report, and nothing in it decides whether what moves is "
            "an object or a mobile entity."
        ),
    },
    # ---------------------------------------------------------------- 08
    # Smith p. 330 (opening passage: "Night is not an object before me; it
    # enwraps me ... personal identity." ... "it is pure depth without
    # foreground or background, without surfaces and without any distance
    # separating it from me."; footnote: Minkowski, Le Temps vécu); p. 327
    # (the perception of space, a disinterested subject); pp. 327-328
    # (Paris); pp. 328-330 (mescalin; the bird and the twittering, Fischer);
    # pp. 331-332 (dreams of rising and falling; the bird shot down); p. 332
    # (Binswanger, a direction of significance); pp. 332-333 (myth; the
    # augur; the holiday village; lived distance, Minkowski); pp. 334-335
    # (the patient in the mountains, Fischer; 'the landscape space', Straus);
    # pp. 335-336 (the objection: these spaces presuppose geometrical
    # space); p. 337 (analytical reflection knows the dreamer better than he
    # does); p. 339 (the brush, Binswanger: "he has no quarrel with explicit
    # perception"; what protects the sane man is the structure of his
    # space); p. 340 (psychologism?); p. 341 ("understanding myth is not
    # believing in it"); p. 342 (the Tuileries stone; "We have said that
    # space is existential; we might just as well have said that existence
    # is spatial"; "Human spaces present themselves as built on the basis of
    # natural space"); p. 343 (natural space is not geometrical space);
    # pp. 343-347 (illusion and truth).
    {
        "slug": "lived-space",
        "title": "Lived Space",
        "module": "Part Two · 2 · Space · Lived Space",
        "one_line": "Beneath the space a disinterested subject knows lie the spaces of night, dreams, myth and illness, and the chapter argues that they are not distortions of geometrical space but modes of an existence that is spatial through and through.",
        "summary": (
            "The chapter's last section widens the inquiry from the perception of space to the "
            "spatiality of existence: night, the dream, myth, and the spaces of patients that "
            "Minkowski, Binswanger and Fischer describe. Code three of the chapter's cases "
            "against empiricism and intellectualism, compute each account's record, and name "
            "the observation both fail."
        ),
        "key": [
            "night: pure depth, no things in it",
            "dreams rise and fall with existence",
            "a lived distance beside the geometric",
            "human space rests on natural space",
            "existence is spatial",
        ],
        "key_label": "Lived space in five lines",
        "concepts_intro": (
            "The section moves from cases to an objection and back. Three ideas carry it."
        ),
        "concepts": [
            ("Lived space",
             "The space of an existence: the directions and distances things have for someone "
             "by what they mean to him, which the chapter finds in night, dreams, myth and "
             "illness, and beneath the clear space of everyday perception too."),
            ("Lived distance",
             "Minkowski's term: besides the physical distance between me and things, a "
             "distance that binds me to what counts for me, sometimes leaving room for "
             "freedom, sometimes too small and too great at once."),
            ("Natural space",
             "The space the body projects us into first, which human spaces are built on and "
             "which is not geometrical space; geometrical space is objective thought's "
             "explicit version of it."),
        ],
        "read_title": "The passage first, then the section line by line",
        "read_intro": (
            "The passage is the chapter's description of night. The lesson reads the "
            "section's widening of the question, the cases in order, the objection that "
            "these are not genuine spaces, and the chapter's reply."
        ),
        "body": [
            ("p", "<strong>Space, p. 330.</strong> &ldquo;Night is not an object before me; it "
                  "enwraps me and infiltrates through all my senses, stifling my recollections "
                  "and almost destroying my personal identity. &hellip; it is pure depth "
                  "without foreground or background, without surfaces and without any distance "
                  "separating it from me.&rdquo; The sentences are on page 330 of Smith's "
                  "translation. The section has no printed heading; it begins on page 327, "
                  "where the chapter says it has so far considered only the perception of "
                  "space, and ends with the chapter on page 347. Read those pages in your own "
                  "copy before going on."),
            ("p", "So far, the section says, the chapter has dealt with the perception of space, "
                  "what a disinterested subject might know of the relations between objects, "
                  "and even there it found the subject's inherence in a world as the "
                  "condition. In the natural attitude, the everyday stance in which the world is "
                  "taken for granted, I do not have perceptions; Paris for me "
                  "is not a collection of views or the law that unites them but a style, like "
                  "the one a person shows in gesture, gait and voice. The cases that follow show "
                  "what lies beneath. Under mescalin, approaching objects seem to grow smaller "
                  "and the walls of a room seem 150 yards apart. One of the schizophrenic "
                  "patients the psychiatrist Fischer reported hears a bird and its twittering and cannot put them "
                  "together. These disturbances, the chapter notes, leave perception as "
                  "knowledge intact: the patient still takes food with his hand. The cases are "
                  "the book's sources' reports; the lab below codes the reports, not the "
                  "patients."),
            ("p", "Then night, and the passage. Eugène Minkowski, a French psychiatrist whose "
                  "<em>Le Temps vécu</em> of 1933 described the lived time and space of his "
                  "patients, is the chapter's source. When the world of clear objects is "
                  "abolished, our perceptual being evolves a spatiality without things. Night "
                  "is not before me as an object is; it has no outlines and is in contact with "
                  "me, and a shout or a distant light peoples it only vaguely. All space for the "
                  "reflecting mind is held together by a thinking that relates its parts, but "
                  "here the thinking starts from nowhere: it is from the heart of the night that "
                  "I am united with it. The distress some feel at night, the chapter adds, is "
                  "that it brings home our contingency."),
            ("p", "Dreams go further. Rising and falling are common themes in dreams, as in myth "
                  "and poetry, and it is well known that they can be related to breathing or "
                  "to sexual drives. These explanations do not get us very far, the chapter "
                  "says, because dreamed rising and falling are not in visible space, as the "
                  "waking perceptions associated with breathing and desire are. The dreamer's "
                  "great bird hovering, hit by a shot, falling and becoming a small heap of "
                  "charred paper does not rise and fall in physical space; it rises and falls "
                  "with the tide of his existence. When I say I am downcast I am not stretching a "
                  "physical relation to the mind: Ludwig Binswanger, a Swiss psychiatrist who "
                  "read his patients through Heidegger, speaks of a direction of significance "
                  "that runs through every region, spatial, auditory, mental."),
            ("def", ("Lived distance",
                     "The distance that binds me to things by what they mean to me, measuring the "
                     "scope of my life at a moment, as against the physical distance between "
                     "my body and them.")),
            ("p", "Myth, waking life and illness follow. For people who live in a world of myth, "
                  "the tribal encampment is not located by a landmark; it is the landmark of all "
                  "landmarks, as for the augur right and left are the lawful and the "
                  "forbidden. I arrive in a village for my holidays and it becomes the centre of "
                  "my life, until a friend brings news from Paris and I feel an exile there. The "
                  "lived distance, Minkowski's term, can leave me room, or be too small and too "
                  "great at once, so that the nearest events obsess me and enshroud me like "
                  "night. One of Fischer's patients, stopping before a mountain landscape, feels "
                  "a threat hanging over him, and then a second sky, black and boundless, "
                  "penetrates the blue sky of evening; he no longer reaches geographical space "
                  "and dwells, in a phrase the chapter takes from Erwin Straus, in &ldquo;the "
                  "landscape space&rdquo;."),
            ("p", "The objection comes in objective thought's voice, at strength. Have these "
                  "descriptions any philosophical value, or do they give only contents of "
                  "experience? The left is a direction only if I can relate it to the right; the "
                  "dreamer must wake to know what he dreamed, and then the anxiety is again "
                  "what it always was, a respiratory obstruction at a point in the chest; ask "
                  "the schizophrenic where his second space is, and in trying to locate it he "
                  "will conjure it away. The phantoms are fragments of the clear world and "
                  "borrow their standing from it. So, the objector concludes, the lived spaces "
                  "are confused appearances of the one true, objective space."),
            ("p", "The chapter's reply begins with a patient of Binswanger's. He feels that a "
                  "brush placed near his window is coming nearer and entering his head, and "
                  "never ceases to be aware that the brush is over there; when he looks at the "
                  "window, he still sees it. No appeal to explicit perception can rouse him, "
                  "because &ldquo;he has no quarrel with explicit perception&rdquo; and holds "
                  "only that it proves nothing against what he experiences. Analytical "
                  "reflection believes it knows what the dreamer or the schizophrenic "
                  "experiences better than they do. Either the one who experiences something "
                  "knows what he experiences, and the dreamer and the patient must be taken at "
                  "their word, or he does not, and then the philosopher's own self-evidence may "
                  "be an illusion. What protects the sane, the chapter concludes, is not their "
                  "critical powers but the structure of their space."),
            ("p", "The lab sets three of these cases against the Introduction's two accounts, as "
                  "the lesson codes them. For empiricism a lived spatial meaning is a feeling "
                  "associated with a geometric percept; for intellectualism there is one space, "
                  "constituted by thought, and the lived spaces are confused thoughts of it. The "
                  "night has no things in it to associate a feeling with, and its thinking starts "
                  "from nowhere, so both fail it. The brush can be a feeling of approach joined "
                  "to an unchanged percept, so empiricism absorbs it, but the correction "
                  "intellectualism predicts never comes, so it fails. The dream's rising and "
                  "falling are not in visible space, so association fails, while "
                  "intellectualism absorbs them by placing them, on waking, in the chest. In the "
                  "<code>all</code> preset each account absorbs 1 of 3 and fails 2, the "
                  "survivors tile prints <code>none</code>, and the split tile names the brush "
                  "and the dream. The <code>night</code> preset keeps the night alone, and still "
                  "nothing survives; the <code>brush-and-dream</code> preset keeps the other two, "
                  "nothing survives, and both are in the split. The coding is the lesson's; the "
                  "chapter's own account is not a column."),
            ("p", "Is this psychologism, each person shut in a private space? The chapter says "
                  "not. Mythical consciousness opens on a horizon of possible objectifications; "
                  "the dream uses all the articulations of waking space; even madness gravitates "
                  "round the world. And &ldquo;understanding myth is not believing in it&rdquo;. "
                  "Crossing the Place de la Concorde, I can rest my eyes on one stone of the "
                  "Tuileries wall until the square disappears and there is only light on a gritty "
                  "surface: beneath human space there is always a natural, non-human one. "
                  "&ldquo;We have said that space is existential; we might just as well have said "
                  "that existence is spatial&rdquo;, and &ldquo;Human spaces present themselves "
                  "as built on the basis of natural space&rdquo;, which is not geometrical space. "
                  "The section's last pages turn to illusion: a flat stone on a sunken path that "
                  "turns out to be a patch of sunlight, a large shadow that is a fly near the "
                  "eye, and perceiving as a faith placed at a stroke in a whole world."),
            ("p", "The course ends where Part Two's next chapter begins, with the thing that keeps "
                  "its size and colour as the light and the distance change. The next course, "
                  "Things, the World and Others, reads that chapter and the one on other people."),
        ],
        "lab": ("phenkit", {
            "mode": "cases",
            "view": "table",
            "accounts": ["empiricism", "intellectualism"],
            "preset": "all",
            "presets": [
                {"id": "all", "label": "All three cases",
                 "observations": ("night envelops me with no things in it, n, n; "
                                  "the brush is in his head and at the window, y, n; "
                                  "the dream rises and falls with desire, n, y"),
                 "expect": {"caRecord": "empiricism: absorbs 1 of 3, fails 2, silent 0; "
                                        "intellectualism: absorbs 1 of 3, fails 2, silent 0",
                            "caSurvivors": "none",
                            "caSplit": "the brush is in his head and at the window, the dream rises and falls with desire"}},
                {"id": "night", "label": "Night alone (Minkowski)",
                 "observations": "night envelops me with no things in it, n, n",
                 "expect": {"caSurvivors": "none", "caSplit": "none"}},
                {"id": "brush-and-dream", "label": "Binswanger's patient and the dream",
                 "observations": ("the brush is in his head and at the window, y, n; "
                                  "the dream rises and falls with desire, n, y"),
                 "expect": {"caSurvivors": "none",
                            "caSplit": "the brush is in his head and at the window, the dream rises and falls with desire"}},
            ],
            "panel_title": "Lived space: two accounts against three cases",
            "panel_intro": (
                "This lab counts the lesson's coding of the chapter: for each case, whether "
                "empiricism and intellectualism absorb it (y), fail it (n) or say nothing (-). "
                "The count is exact; the coding is the lesson's reading of the reports, and "
                "Merleau-Ponty's own account is not a column."
            ),
        }),
        "steps_title": "Counting two accounts against the cases of lived space",
        "steps_intro": "Four steps, as for any table of this kind.",
        "steps": [
            ("State each account at strength",
             "Empiricism: a lived spatial meaning is a feeling associated with a geometric "
             "percept. Intellectualism: there is one space, constituted by thought, and the "
             "lived spaces are confused thoughts of it."),
            ("Code each case with its reason",
             "Mark y, n or - for each account, and give the sentence of the chapter that "
             "decides the mark."),
            ("Compute the records and survivors",
             "Count each account's absorbed, failed and silent cases, and find any account "
             "that fails none, on the table and on each subset."),
            ("Find the split and the common failure",
             "List the cases on which the accounts part, name the case both fail, and state "
             "the chapter's own account of it in prose."),
        ],
        "worked": {
            "title": "Night, the brush and the dream",
            "intro": [
                "Take the all preset, with the lesson's coding. You want each account's record, "
                "the survivors, the split and the case both fail.",
            ],
            "lines": [
                "night envelops me:  n, n",
                "the brush, in his head and at the window:  y, n",
                "the dream rises and falls with desire:  n, y",
                "empiricism:  absorbs 1 of 3, fails 2",
                "intellectualism:  absorbs 1 of 3, fails 2",
                "split:  the brush and the dream",
            ],
            "after": [
                "Neither account survives, and the night defeats both: there is nothing in it to "
                "associate a feeling with, and no part of it for thought to relate to another. "
                "The chapter's own account, that night is a spatiality without things in which "
                "my existence is still situated, is stated in prose and not scored.",
            ],
        },
        "quiz_title": "Spaces of an existence",
        "quiz": [
            {"q": "Four cases are coded, empiricism then intellectualism: A n, n; B y, n; C n, "
                  "y; D y, y. What do the survivors and split tiles print?",
             "a": ["survivors none; split B, C", "survivors none; split A, D",
                   "survivors empiricism; split B", "survivors none; split none"],
             "c": 0,
             "why": "Both accounts fail A, so neither survives. The split lists the cases with y "
                    "against n, which are B and C; A is n against n and D is y against y, so "
                    "neither is in it. Empiricism fails A and C."},
            {"q": "What, on the chapter's account, protects the sane against delirium and "
                  "hallucination?",
             "a": ["Not their critical powers but the structure of their space",
                   "Their critical powers",
                   "Their knowledge of geometrical space",
                   "The testimony of other people"],
             "c": 0,
             "why": "That is the chapter's sentence on page 339: objects stay before the sane "
                    "man, keeping their distance. Critical powers are what it denies, and "
                    "Binswanger's patient shows why: he has no quarrel with explicit perception, "
                    "so neither geometry nor others' testimony would move him."},
            {"q": "Why, on the chapter's reading, do the dream's rising and falling escape the "
                  "explanation by breathing and desire?",
             "a": ["Dreamed rising and falling are not in visible space, as the waking "
                   "perceptions associated with breathing and desire are",
                   "Dreams have nothing to do with breathing or desire",
                   "The explanation is physiologically false",
                   "Dreamers never remember falling"],
             "c": 0,
             "why": "The chapter grants that the themes can be related to breathing and sexual "
                    "drives and calls that a first step; what the explanation misses is that the "
                    "dreamed fall is not in physical space. It does not call the physiology "
                    "false, and memory is not the issue."},
            {"q": "How does the chapter answer the charge that it shuts each kind of experience "
                  "in a private space?",
             "a": ["Mythical, dreaming and mad consciousness are not sealed off; each opens on "
                   "a horizon of possible objectification",
                   "It accepts that each experience is a closed world",
                   "It says only geometrical space is real",
                   "It says the philosopher must believe the myths"],
             "c": 0,
             "why": "The text says these are not small islands of experience with no escape: the "
                    "myth forms a world, the dream uses waking space, madness gravitates round "
                    "the world. It refuses to make geometrical space immanent in mythical space, "
                    "and says understanding myth is not believing in it."},
        ],
        "mistakes": [
            ("Thinking lived space is a subjective distortion of real space",
             "This is objective thought's reading, and the chapter states it at strength: the "
             "dreamer must wake, the patient's second space vanishes when he tries to locate "
             "it, the phantoms borrow their standing from clear space. On the lesson's table "
             "intellectualism absorbs the dream on exactly that ground, and fails the night and "
             "Binswanger's patient, who keeps the brush at the window and in his head at once. "
             "The chapter's reply is that the disturbances leave perception as knowledge "
             "intact and show a deeper life beneath it, that human spaces are built on a "
             "natural space which is not geometrical, and that objective thought itself draws "
             "on the unreflective experience it treats as a distortion."),
            ("Thinking the chapter believes the patient's second space, or the myth",
             "The chapter takes the patient at his word about what he experiences, and still "
             "says the myth opens on possible objectification and the dream uses waking "
             "space. &ldquo;Understanding myth is not believing in it&rdquo;: the claim is that "
             "these spaces are genuine modes of an existence, not that the brush is in the "
             "patient's head."),
            ("Thinking these cases say nothing about normal perception",
             "The chapter says clear space is not only surrounded but permeated by the other "
             "spatiality that illness throws into relief, and finds it in the holiday village "
             "and the stone of the Tuileries wall. The cases are extreme so that a structure "
             "present everywhere can be seen."),
        ],
        "standard": (
            "Finish when you can count two accounts against the cases of lived space and state the chapter's reply to objective thought.",
            "Given the lesson's coding of the night, the brush and the dream, compute each "
            "account's record, the survivors, the split and the case both fail, state the "
            "objection that lived spaces are confused appearances of geometrical space, and "
            "give the chapter's reply."
        ),
        "note": (
            "The cases are the reports of Minkowski, Binswanger and Fischer as the chapter gives "
            "them, and the cells are the lesson's reading; the empiricist cell for the brush "
            "in particular is the lesson's, since the chapter argues there against objective "
            "thought in general. The lab counts the cells and cannot check them, and "
            "Merleau-Ponty's own account is never scored."
        ),
    },
]
