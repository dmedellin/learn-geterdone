"""The Expressive Body, lessons 1-4 -- Part One, Chapters 4-6.

Every quotation is copied from Colin Smith's translation, Routledge Classics
pagination (Part One, Chapters 4-6, pp. 171-232); the comment beside each
lesson gives its pages. Smith's ligatures are printed as plain letters, a word
split by a line-break hyphen is joined, and footnote numerals are left out.
Nothing else is changed. The cases are the book's reports of its sources'
patients, and each lab codes the report, not the patient.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # Smith pp. 174-175 (opening passage: "The body is to be compared ... a
    # work of art." and "It is in this sense ... covariant terms."); p. 171
    # (partes extra partes; not primarily in space: it is of it; the
    # anosognosic's arm 'like a snake'); p. 172 (the telephone; available in
    # virtue of their common meaning; children look at the object); p. 173
    # (photograph, silhouette, walk; the cube's law; I am not in front of my
    # body; Leibniz's 'effective law'); p. 174 (style; Cezanne; poem and cry);
    # p. 175 (the expression indistinguishable from the thing expressed; the
    # arm seen and touched; every habit motor and perceptual); p. 176 (the
    # stick: an instrument with which he perceives; Auffassung-Inhalt);
    # p. 177 (Koffka's child, blue and red; the gaze as an instrument).
    # The telephone preset is the chapter's own example; the signature is the
    # lesson's illustration and the chapter does not use it.
    {
        "slug": "the-body-as-a-work-of-art",
        "title": "The Body as a Work of Art",
        "module": "Part One · 4 · The Synthesis of One's Own Body",
        "one_line": "The body's parts and senses hang together neither as a machine's parts nor as the appearances of an object under a law, but as the colours of a picture carry its meaning.",
        "summary": (
            "Chapter 4 asks what kind of unity one's own body has, and answers with a "
            "comparison: the body is like a work of art, in which the meaning cannot be had "
            "apart from what carries it. Compute what stays when one movement is made in "
            "different ways, find that no muscle is in the core, and say why the chapter "
            "would still not call the core the body's unity."
        ),
        "key": [
            "the body is of space, not merely in it",
            "movements share a meaning, not muscles",
            "I am not in front of my body; I am it",
            "a nexus of meanings, not a law",
            "core = what every variant keeps",
            "the stick: something to perceive with",
        ],
        "key_label": "The chapter in six lines",
        "concepts_intro": (
            "Chapter 4 is the shortest in the book, seven pages. It generalises what the last "
            "chapter found about bodily space, rejects two accounts of the body's unity, and "
            "offers a comparison in their place."
        ),
        "concepts": [
            ("Partes extra partes",
             "Latin for parts outside parts: the way a physical thing exists, each piece beside "
             "the next and related to it only from outside. The Cartesian tradition makes this "
             "the only way of existing in itself, and the chapter denies that one's own body "
             "exists like that."),
            ("Unity under a law",
             "The intellectualist's account of an object's unity: a cube is one thing because "
             "an idea of it prescribes in advance how its faces will appear from every side. "
             "The chapter asks whether the body is one in that way, and answers no."),
            ("A nexus of living meanings",
             "The chapter's phrase for the body's unity. A touch on the upper arm means "
             "something for the forearm, the shoulder and the arm as seen, because they all "
             "take part in one action, as the colours of a painting take part in its meaning."),
        ],
        "read_title": "The passage first, then the chapter line by line",
        "read_intro": (
            "The passage is the comparison the chapter is named for. The lesson then goes back "
            "to the chapter's first page and follows it through the telephone, the cube, the "
            "work of art and the blind man's stick."
        ),
        "body": [
            ("p", "<strong>Part One, Chapter 4, pp. 174&ndash;175.</strong> &ldquo;The body is "
                  "to be compared, not to a physical object, but rather to a work of art. "
                  "&hellip; It is in this sense that our body is comparable to a work of art. It "
                  "is a nexus of living meanings, not the law for a certain number of covariant "
                  "terms.&rdquo; The sentences are from pages 174 and 175 of Colin Smith's "
                  "translation. Read the whole chapter, pages 171 to 177, in your own copy "
                  "before going on; it is short, and the lesson goes back through it a phrase at "
                  "a time."),
            ("p", "The chapter opens by generalising. The analysis of bodily space in Chapter 3 "
                  "has shown, for one's own body, something true of every perceived thing: the "
                  "spatiality of a thing and its being a thing are not two problems. The "
                  "Cartesian and Kantian tradition already knew this, Merleau-Ponty says, but "
                  "read it one way round. It made the object's spatial limits its essence, so "
                  "that to exist in itself is to exist <em>partes extra partes</em>, part "
                  "outside part, and it explained perceiving a thing by perceiving space. The "
                  "experience of one's own body teaches the reverse, to embed space in "
                  "existence: &ldquo;our body is not primarily in space: it is of it&rdquo;. The "
                  "evidence is two kinds of patient. Patients with anosognosia, an unawareness "
                  "of their own illness, describe their arm as like a snake, long and "
                  "cold, and still know where it is, since that is where they look for it. The "
                  "phantom arm is felt where no arm is. So the felt presence of a limb is not "
                  "settled by its objective place: anosognosia shows that the place is not "
                  "enough, the phantom that it is not even needed."),
            ("p", "Then a scene from the book. You are sitting at a table and want to reach the "
                  "telephone. The movement of the hand, the straightening of the upper body and "
                  "the tautening of the leg muscles are, the chapter says, enveloped in each "
                  "other: you want a result, and the work is shared out among the parts of the "
                  "body without your arranging it. The possible ways are given in advance as "
                  "equivalent. You can stay leaning back and stretch the arm further, lean "
                  "forward, or half stand up. &ldquo;All these movements are available to us in "
                  "virtue of their common meaning.&rdquo; That is why, the chapter adds, children "
                  "making their first attempts to grasp look at the object and not at their "
                  "hand: the parts of the body are known by what they are for, and their "
                  "co-ordination, the chapter says flatly, is not learnt."),
            ("p", "The lab codes the scene. The <code>telephone</code> preset lists the three "
                  "ways the chapter names, each with the parts it engages, and marks every one "
                  "as a way of reaching the telephone. The lab prints the core, what every "
                  "variant of the kind has, as <code>hand-at-the-telephone</code>; the list of "
                  "what varies holds every posture of arm, trunk and legs; and since no variant "
                  "is marked as not of the kind, the third tile says so. The coding is the "
                  "lesson's: it decided which parts to name and that each way counts. The count "
                  "over it is exact, and it says that what the three ways share is their result, "
                  "not any part of the body."),
            ("p", "The chapter turns next to how the parts and the senses are joined. You "
                  "cannot see your foot inside your shoe, and yet, the chapter says, as you "
                  "contract it you can see it. Experiments the book reports found that people do "
                  "not recognise their own hand in a photograph, and are unsure of their own "
                  "handwriting among others, and yet recognise their own silhouette or their own "
                  "walk when it is filmed: what they have often seen they miss, and what they "
                  "have never seen they know at once. So the links between the parts of the "
                  "body, and between its look and its feel, are not forged gradually by "
                  "association. I do not translate the data of touch into the language of sight "
                  "one item at a time; that translation, the chapter says, is my body itself."),
            ("p", "Here the chapter states the second account at its strongest. If the parts "
                  "are not added up, perhaps the body is perceived through its law of "
                  "construction, as you know in advance every possible face of a cube from its "
                  "geometry. This is the answer an intellectualist, one of Kant's heirs, gives for "
                  "any object: a thing is one because an idea of it prescribes how its "
                  "appearances vary. The chapter grants that an external object may be defined "
                  "this way, at least as a first approximation, because it stands in front of "
                  "me and shows me its variations. The body does not. &ldquo;I am not in front "
                  "of my body, I am in it, or rather I am it.&rdquo; Neither its variations nor "
                  "the constant that would govern them can be set before me as objects; I am the "
                  "one who sees and touches the arms and legs, the one who unifies them. In "
                  "Leibniz's term, which the chapter borrows, the body is the effective law of "
                  "its own changes, and if it interprets anything, it interprets itself."),
            ("def", ("The body's unity (the chapter's account)",
                     "Neither the joining of parts that lie outside one another nor the "
                     "subsumption of appearances under a law, but the unity of an action: the "
                     "arm seen and the arm touched, like the segments of the arm, perform one "
                     "and the same action, and so each signifies the others.")),
            ("p", "Now the comparison. In a picture or a piece of music the idea cannot be "
                  "conveyed except by showing the colours and the sounds. Paul Cézanne, the "
                  "painter who in the 1880s and 1890s rebuilt the still life and the landscape "
                  "out of patches of colour and is a touchstone for Merleau-Ponty, is the "
                  "example: an analysis of his work, if you have not seen the pictures, leaves "
                  "you choosing among several possible Cézannes, and only the pictures give you "
                  "the one there is. A poem has a surface meaning that prose could carry, and "
                  "a further life that makes it a poem; unlike a cry, it lasts, and it would be "
                  "lost if its text were not kept to the last detail. Change the order of a "
                  "novel's narrative and you change its meaning. These works are individuals, "
                  "beings in which &ldquo;the expression is indistinguishable from the thing "
                  "expressed&rdquo;."),
            ("p", "Go back to the passage. The body is comparable to a work of art in exactly "
                  "that sense, and the next sentence says what it rules out: a nexus of living "
                  "meanings, not a law for covariant terms, a set of quantities that change "
                  "together by rule. The chapter's own example follows. A touch felt in the "
                  "upper arm signifies a touch in the forearm and the shoulder and a certain "
                  "look of the arm, not because all of these are facets of one intelligible "
                  "arm, as the faces of a cube belong to the idea of a cube, but because they "
                  "take part in one action. A page earlier the chapter calls what "
                  "joins the touch and the sight of the hand a certain style of its gestures."),
            ("p", "The lab's second instance is the lesson's own, not the book's. Write your "
                  "signature small on paper with the fingers, large on a blackboard with the "
                  "whole arm, with the left hand, or with a foot in sand. The "
                  "<code>signature</code> preset codes the four, each with the limb it uses and "
                  "with the letter shapes, the order of the strokes and their rhythm. The core "
                  "is <code>letter-shapes, stroke-order, rhythm</code>, and what varies is "
                  "<code>fingers, arm, left-hand, leg</code>: no muscle is in every variant. "
                  "The <code>muscles</code> preset codes the same four by their limbs alone, and "
                  "the core is <code>none</code>. Coded by its parts, the movement has nothing "
                  "in common with itself. The <code>tracing</code> preset adds a slow tracing of "
                  "the signature by someone else, marked as not a signature, and the third tile "
                  "prints <code>tracing lacks rhythm</code>: it has every shape and every stroke "
                  "in order."),
            ("p", "Notice what the lab has done, though. It found an invariant across a set of "
                  "variants, and an invariant of variations is very nearly what the passage "
                  "says the body is not: the law for a certain number of covariant terms. The "
                  "core is a list drawn up by someone looking at four signatures from outside, "
                  "the position the chapter says I am never in towards my own body. What the "
                  "count does show is negative and exact: whatever holds the four together is "
                  "not a part. What it is, on the chapter's account, is not something the hand "
                  "consults before it writes."),
            ("p", "The chapter ends by extending this from movement to perception. Every habit, "
                  "it says, is both motor and perceptual, and the blind man's stick from Chapter "
                  "3 is the example. One is tempted, the chapter says, giving the view it is "
                  "about to reject, to think that the blind man builds up the stick and its "
                  "positions from pressures on his hand, reads the pressures as signs of the "
                  "stick and the stick as a sign of the object, ever faster and from ever fainter "
                  "signals. Its reply is that habit relieves him of any such reading. The "
                  "pressures are no longer given; the stick is no longer something he perceives "
                  "but &ldquo;an instrument with which he perceives&rdquo;, and the perspectives "
                  "it gives on the kerb are aspects of the kerb, not signs of it. A footnote "
                  "notes that Husserl long described consciousness this way, as a content taken "
                  "up as the appearance of an object, and credits him with a decisive step "
                  "beyond it in his lectures on time."),
            ("p", "Last, the child. Kurt Koffka, one of the founders of Gestalt psychology, "
                  "reported that a child who learns to tell blue from red finds the other "
                  "colours easier too. Has the child grasped the category <em>colour</em> through "
                  "the pair? The chapter answers that a category could recognise itself in the "
                  "data only if it were already rooted in them. The gaze is a natural instrument "
                  "like the blind man's stick, and to learn to see colours is to acquire a style "
                  "of seeing, a new use of one's own body, enriching and recasting the body "
                  "schema (Smith's word is body image). The body, the chapter concludes, is not "
                  "an object for an <em>I think</em> but a grouping of lived-through meanings "
                  "that moves towards its own equilibrium."),
            ("p", "If the body's unity is the unity of a meaning, the next question is where "
                  "else in bodily life meaning is found. The next lesson, “The Body as a Sexed "
                  "Being”, reads Chapter 5, which looks for it in the area of experience that "
                  "has significance only for us, affective life, and asks how something comes "
                  "to exist for us through desire or love."),
        ],
        "lab": ("phenkit", {
            "mode": "variation",
            "view": "core",
            "preset": "telephone",
            "presets": [
                {"id": "telephone",
                 "label": "Reaching the telephone from a chair, three ways (the chapter's example, p. 172)",
                 "variants": "lean back and stretch further, yes, arm-at-full-stretch trunk-back hand-at-the-telephone; "
                             "lean forward, yes, arm-half-bent trunk-forward hand-at-the-telephone; "
                             "half stand up, yes, arm-half-bent trunk-raised legs-tautened hand-at-the-telephone",
                 "expect": {"vrCore": "hand-at-the-telephone", "vrVary": "arm-at-full-stretch, trunk-back, arm-half-bent, trunk-forward, trunk-raised, legs-tautened", "vrBreak": "no variant is marked no"}},
                {"id": "signature",
                 "label": "One signature written four ways (the lesson's illustration)",
                 "variants": "small on paper, yes, fingers letter-shapes stroke-order rhythm; "
                             "large on a blackboard, yes, arm letter-shapes stroke-order rhythm; "
                             "with the left hand, yes, left-hand letter-shapes stroke-order rhythm; "
                             "with a foot in sand, yes, leg letter-shapes stroke-order rhythm",
                 "expect": {"vrCore": "letter-shapes, stroke-order, rhythm", "vrVary": "fingers, arm, left-hand, leg"}},
                {"id": "muscles",
                 "label": "The same four, coded only by the limb that writes (the lesson's illustration)",
                 "variants": "small on paper, yes, fingers; large on a blackboard, yes, arm; "
                             "with the left hand, yes, left-hand; with a foot in sand, yes, leg",
                 "expect": {"vrCore": "none", "vrVary": "fingers, arm, left-hand, leg"}},
                {"id": "tracing",
                 "label": "Two signatures and a slow tracing by someone else (the lesson's illustration)",
                 "variants": "small on paper, yes, fingers letter-shapes stroke-order rhythm; "
                             "large on a blackboard, yes, arm letter-shapes stroke-order rhythm; "
                             "tracing, no, fingers letter-shapes stroke-order",
                 "expect": {"vrCore": "letter-shapes, stroke-order, rhythm", "vrBreak": "tracing lacks rhythm"}},
            ],
            "panel_title": "What stays when one movement is made in different ways",
            "panel_intro": (
                "This lab counts the lesson's coding: which parts of the body each variant "
                "engages, and whether it is still the same movement, are the lesson's choices. "
                "The lab prints what every variant of the kind keeps, what varies, and what the "
                "others lack. Compare the signature and muscles presets."
            ),
        }),
        "steps_title": "Finding what one movement keeps",
        "steps_intro": "Five steps; the last is the chapter's caution.",
        "steps": [
            ("Code each variant",
             "List the parts of the body each way of making the movement engages, and what it "
             "produces, as separate words, and mark whether it is still the same movement. "
             "These are decisions about the example."),
            ("Intersect the variants of the kind",
             "Keep the properties every variant marked yes has. That set is the core."),
            ("List what varies",
             "Every property some variant of the kind has and another lacks varies. If every "
             "limb is on this list, no part of the body is what the movements share."),
            ("Check the variants marked no",
             "For each, name the core properties it lacks. A tracing that keeps every shape "
             "and loses the rhythm shows that the rhythm was part of what made the movement "
             "the same."),
            ("Say what the core is not",
             "The core is a list drawn up from outside. On the chapter's account the body's "
             "unity is not a law its movements are checked against, so do not read the core as "
             "that unity."),
        ],
        "worked": {
            "title": "One signature, four ways",
            "intro": [
                "Take the signature preset: the signature small on paper, large on a "
                "blackboard, with the left hand and with a foot in sand, each coded by its limb "
                "and by its letter shapes, stroke order and rhythm. You want the core and what "
                "varies.",
            ],
            "lines": [
                "limbs:  fingers, arm, left hand, leg, one each",
                "a limb in all four?  no, so every limb varies",
                "letter shapes:  in all four, so in the core",
                "stroke order:  in all four, so in the core",
                "rhythm:  in all four, so in the core",
            ],
            "after": [
                "The muscles vary in every variant and the shapes, the order and the rhythm "
                "stay, so the core holds no part of the body. Coded by limb alone, the same four "
                "have an empty core. Both figures are exact counts of the lesson's coding, and "
                "neither is the body's unity, which the chapter says is lived rather than "
                "listed.",
            ],
        },
        "quiz_title": "The body's unity",
        "quiz": [
            {"q": "Three ways of opening a door are coded as opening the door: with the right "
                  "hand (right-hand turn-handle door-opens), with an elbow while carrying "
                  "shopping (elbow push-bar door-opens) and with a hip (hip push-bar "
                  "door-opens). What is the core?",
             "a": ["door-opens", "push-bar, door-opens", "right-hand, door-opens", "none"],
             "c": 0,
             "why": "Only door-opens is in all three. The push bar is missing from the first "
                    "way and the right hand from the other two, so each varies; the core is not "
                    "empty, because the result is shared."},
            {"q": "The chapter compares the body's unity to that of what?",
             "a": ["A cube, whose faces are all known in advance from its geometrical law",
                   "A work of art, whose meaning cannot be had apart from its colours or sounds",
                   "A machine, whose parts lie side by side and act on one another",
                   "A sum of sensations, joined one by one by association"],
             "c": 1,
             "why": "The passage says the body is to be compared not to a physical object but to "
                    "a work of art. The cube known by its law is the intellectualist account the "
                    "chapter rejects on p. 173, the machine is the partes extra partes it rejects "
                    "on p. 171, and the chapter denies that the parts are joined gradually and "
                    "cumulatively."},
            {"q": "Once the blind man's stick has become a habit, what is it, on the chapter's "
                  "account?",
             "a": ["An object whose pressures he reads as signs, ever faster and more faintly",
                   "An object built up from the pressures on the hand, through which the "
                   "thing is reached as a second-order object",
                   "An instrument with which he perceives, no longer an object he perceives",
                   "A tool he must still attend to before each step"],
             "c": 2,
             "why": "The text says the stick is no longer an object perceived by the blind man "
                    "but an instrument with which he perceives. Reading pressures as signs ever "
                    "faster, and building up the stick from the pressures so that it mediates "
                    "the thing as a second-order object, are the view the chapter says one is "
                    "tempted by and then rejects: habit relieves him of that reading."},
            {"q": "In the signature preset no muscle is in the core. Why does the chapter "
                  "still not let you call the core the body's unity?",
             "a": ["Because the core would have to contain at least one muscle",
                   "Because the signature is learnt separately for each limb",
                   "Because the body has no unity, only parts",
                   "Because I am not in front of my body, so its variations and their constant "
                   "cannot be set before me as a law"],
             "c": 3,
             "why": "The chapter says that neither the body's variations nor their constant can "
                    "be expressly posited, since I am in my body and not in front of it, and it "
                    "calls the body a nexus of meanings, not a law for covariant terms. It denies "
                    "that the unity is in the parts, that co-ordination is learnt, "
                    "and that the body lacks unity."},
        ],
        "mistakes": [
            ("Thinking the body is one as a machine is, or as any object is",
             "The Cartesian picture holds the body together as a machine's parts are held, each "
             "outside the next; the intellectualist holds it together as the mind unifies any "
             "object, under a law that prescribes its appearances. The chapter rejects both. "
             "The parts are not added up, since what we have never seen of ourselves we "
             "recognise at once, and the body is not set before me to be unified, since I am "
             "it. Its unity is like a painting's or a poem's, in which the meaning cannot be "
             "had apart from what carries it. The telephone preset makes the first point in the "
             "lab's terms: the core is <code>hand-at-the-telephone</code>, and every posture "
             "varies."),
            ("Taking the lab's core for the body's unity",
             "An invariant of a set of variants is close to what the passage calls the law for a "
             "certain number of covariant terms, the thing the body is not. The core is a "
             "spectator's summary of four signatures. It shows exactly that no part is shared, "
             "and the chapter's account of what is shared, a style lived in the gestures, is "
             "not a further entry on the list."),
            ("Hearing the comparison with art as a claim that the body is beautiful or designed",
             "The comparison is about one feature of a work of art: its meaning is accessible "
             "only through the work itself and cannot be detached from it, as a novel's meaning "
             "changes if its order changes. It says nothing about beauty, and nothing about an "
             "artist who made the body to a plan."),
        ],
        "standard": (
            "Finish when you can compute what a set of movements keeps and say what the "
            "chapter will not let the figure mean.",
            "Given a coded set of ways of making one movement, compute the core, list what "
            "varies and name what each excluded variant lacks; then state the two accounts of "
            "the body's unity the chapter rejects and the comparison it puts in their place."
        ),
        "note": (
            "The telephone is the chapter's own example; the signature, the blackboard and the "
            "sand are the lesson's illustration, and the chapter does not use them. Every cell "
            "is the lesson's coding. The lab finds an invariant, which is a spectator's way of "
            "describing a movement, and the chapter's claim is that the body's unity is not "
            "available to a spectator in that way; the lab cannot test that claim, only show "
            "that the invariant contains no part of the body."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Smith p. 196 (opening passage: "Taken in this way ... co-extensive with
    # life." and "There is interfusion ... 'non-sexual'."); p. 178 (desire or
    # love; affective life); p. 179 (the mosaic of affective states; any
    # sexual incapacity ought to amount ...; Schneider's sexual life, after
    # Steinfeld, footnote 1); p. 180 (visual and tactile representation; the
    # occipital wound would free automatic responses; "Pathology brings to
    # light ... a vital zone"; the sexual schema; physically they are all the
    # same); p. 181 (erotic perception is not a cogitatio ...); p. 182 (the
    # intentional arc; psychoanalysis; whatever Freud's declarations);
    # p. 183 (Stekel; 'has a meaning'; the sexual is not the genital);
    # p. 184 (all existence sexual or every sexual phenomenon existential;
    # Casanova); p. 185 (the girl, Binswanger; footnote 6 misprints
    # 'Rinswanger'); p. 186 (co-existence; swallowing; stripes and a house
    # number); p. 187 (to have lost one's voice ...; treated and left free to
    # see the man she loves; pithiatism; loses her voice as one loses a
    # memory); p. 188 (will presupposes a field of possibilities); p. 189
    # (sleep; a touch of the hand); p. 191 (a conversion of the whole body);
    # p. 193 (walk 'on its head'); p. 195 (two mistakes; an atmosphere);
    # p. 196 (indeterminacy; no God could determine ...); p. 198 (no one is
    # saved ...); pp. 198-201, footnote 18 (historical materialism).
    {
        "slug": "the-body-as-a-sexed-being",
        "title": "The Body as a Sexed Being",
        "module": "Part One · 5 · The Body in its Sexual Being",
        "one_line": "Sexuality is neither a reflex apparatus nor a set of representations, but a way of being towards the world and other people, interfused with the rest of existence.",
        "summary": (
            "Chapter 5 looks for meaning in the one area of experience that matters only for "
            "us, affective and sexual life, through two of its sources' patients: Schneider, "
            "and Binswanger's patient who lost her voice. Compute two classical accounts' "
            "records over the lesson's coding of the reports, find the observations on which "
            "they part and the one both fail, and state the chapter's own account, which is "
            "never a column."
        ),
        "key": [
            "affectivity is not a mosaic of states",
            "Schneider: no freed automatism",
            "a vital zone between reflex and idea",
            "loss of voice: not paralysis, not a pretence",
            "an account survives if no case refutes it",
            "sexuality and existence are interfused",
        ],
        "key_label": "The chapter in six lines",
        "concepts_intro": (
            "The chapter states two classical accounts of affective life and tests them on "
            "Schneider; in Binswanger's patient it meets the same pair under other names, "
            "paralysis and simulation. Its own account is stated in prose."
        ),
        "concepts": [
            ("Automatism and representation",
             "The two accounts the chapter sets aside. On the first, sexuality is a reflex "
             "apparatus set off by stimuli; on the second, a consciousness of pleasures and "
             "ideas sets the apparatus going. The chapter places what it finds in a zone "
             "between them."),
            ("Co-existence",
             "The chapter's word for living with others, of which speech is the bodily "
             "function most closely bound up with it. The girl's loss of voice is read as a "
             "refusal of co-existence."),
            ("Interfusion",
             "The chapter's term for the relation of sexuality to the rest of existence: each "
             "permeates the other, so that neither explains the other and no act can be "
             "labelled purely sexual or purely not."),
        ],
        "read_title": "The passage first, then the chapter's two patients",
        "read_intro": (
            "The passage is the chapter's conclusion about sexuality. The lesson goes back to "
            "the opening, follows the chapter through Schneider, Freud and the girl who lost "
            "her voice, and returns to the passage at the end."
        ),
        "body": [
            ("p", "<strong>Part One, Chapter 5, p. 196.</strong> &ldquo;Taken in this way, as "
                  "an ambiguous atmosphere, sexuality is co-extensive with life. &hellip; There "
                  "is interfusion between sexuality and existence, which means that existence "
                  "permeates sexuality and vice versa, so that it is impossible to determine, in "
                  "a given decision or action, the proportion of sexual to other motivations, "
                  "impossible to label a decision or act &lsquo;sexual&rsquo; or "
                  "&lsquo;non-sexual&rsquo;.&rdquo; The sentences are from page 196 of Smith's "
                  "translation. Read the whole chapter, pages 178 to 201, the long footnote at "
                  "its end included, in your own copy before going on."),
            ("p", "The chapter begins by saying why it turns to desire. Space and perceived "
                  "things tempt us to think of the subject as a knower facing an object, because "
                  "nature seems to exist whether or not it is perceived. To see how a thing or a "
                  "being begins to exist for us, Merleau-Ponty says, we should look at the area "
                  "of experience that has significance only for us, affective life, and ask how "
                  "something comes to exist through desire or love. Then he states the usual "
                  "view. Affectivity is a mosaic of pleasures and pains, each sealed in itself "
                  "and explained by the bodily system; where intelligence enters, it is because "
                  "representations take the place of the natural stimuli, by association or the "
                  "conditioned reflex. On that view, the chapter says, any sexual incapacity "
                  "ought to be either a loss of certain representations or a weakening of the "
                  "capacity for pleasure."),
            ("p", "The test is Schneider, the soldier wounded in 1915 by splinters to the back of "
                  "the head whom The Lived Body met in Gelb and Goldstein's reports; his sexual life "
                  "was analysed by a third author, Steinfeld, whom the chapter cites. The book's "
                  "argument concerns the case as those reports give it, and the reports were "
                  "later questioned by neurologists who re-examined him. As reported, Schneider "
                  "no longer seeks intercourse of his own accord. Pictures, talk of sex and the "
                  "sight of a body do not arouse desire in him; his reactions are strictly local "
                  "and begin only with contact; and at every stage, the report says, it is as if "
                  "he did not know what is to be done."),
            ("p", "Can either account absorb this? The representation account is tried first, as "
                  "Chapter 3 had tried to explain his loss of initiative in movement by a loss of "
                  "visual representations. But touch has lost its sexual significance too, and it is "
                  "hard to say he has no tactile representations; and the weakness of his "
                  "representations looks like an effect of the change, not its cause. The reflex "
                  "account fares no better. His wound was small and in the occipital region; if "
                  "sexuality were an autonomous reflex apparatus, an injury to the brain should "
                  "have freed the automatic responses and made his sexual behaviour more marked, "
                  "not less. &ldquo;Pathology brings to light, somewhere between automatic "
                  "response and representation, a vital zone&rdquo; where his sexual "
                  "possibilities, like his motor and perceptual ones, are worked out."),
            ("p", "What has changed, the chapter says, is the structure of perception itself. "
                  "For a normal subject a body is not perceived merely as an object: beneath the "
                  "visible body is a sexual schema, individual to each person. For Schneider, a "
                  "woman's body has no particular essence; it is character, he says, that makes "
                  "a woman attractive, since physically they are all the same. What he has lost "
                  "is the power to project a sexual world before him and to put himself in an "
                  "erotic situation. &ldquo;Erotic perception is not a cogitatio which aims at a "
                  "cogitatum&rdquo;, an act of thought aimed at its object, in the Latin of Descartes and Husserl; "
                  "through one body it aims at another, in the world and not in a "
                  "consciousness."),
            ("p", "The lab counts that argument. Its accounts are fixed for the lesson: <em>a "
                  "bodily mechanism</em>, the reflex apparatus, and <em>a representing "
                  "consciousness</em>, the account by representations. Each observation is the "
                  "lesson's one-line summary of what the chapter reports, and each cell is the lesson's reading of what the "
                  "chapter says the account can absorb (y), cannot (n), or is silent on (-). The "
                  "<code>schneider</code> preset has one observation, coded n and n. The first "
                  "tile prints each account's record, how many observations it absorbs, fails "
                  "and is silent on; the second, the accounts that fail nothing, is "
                  "<code>none</code>; the third, the observations on which the two part, one y "
                  "and the other n, is <code>none</code> too, because both fail at the same "
                  "place."),
            ("p", "Sexuality, then, is not an autonomous cycle; it is bound up with the whole of "
                  "a person's active and knowing life, and in Schneider the intentional arc that "
                  "The Lived Body described gives way in all three at once. Here the chapter turns to "
                  "Sigmund Freud, the Viennese neurologist who founded psychoanalysis, and reads "
                  "him in a way of its own. Whatever Freud's theoretical declarations, it says, "
                  "psychoanalytic research in fact explains people not by a sexual substructure "
                  "but by finding in sexuality relations and attitudes once thought to belong to "
                  "consciousness; every human action, as Freud put it, has a meaning. For Freud "
                  "himself, the chapter says, the sexual is not the genital, and the libido is "
                  "not an instinct aimed at fixed ends but the power of taking root in different "
                  "settings. Freud's own theory spoke of drives and energies, and whether this is "
                  "Freud or a reading of him is disputed."),
            ("p", "The chapter then sees a difficulty in its own reading. If sexuality is "
                  "widened into a whole manner of being in the world, does that mean all "
                  "existence has a sexual significance, or every sexual phenomenon an "
                  "existential one? The first makes the claim a tautology, since sexuality no "
                  "longer names anything in particular. The second makes sexual life a mere "
                  "reflection of existence, and it is not one: a life effective in politics can "
                  "go with an impaired sexuality, and the sexual life of Casanova, the "
                  "eighteenth-century Venetian whose memoirs made his name a byword for "
                  "seduction, could be technically perfect "
                  "without any particular vigour of being in the world. If words are to mean "
                  "anything, sexual life is a sector of life with a special relation to sex. The "
                  "chapter takes up a second case to say what that relation is."),
            ("p", "Ludwig Binswanger was a Swiss psychiatrist, a friend and correspondent of "
                  "Freud's, who directed a sanatorium at Kreuzlingen and was then turning "
                  "Heidegger's analysis of existence into a psychiatry. He reports a girl whose "
                  "mother has forbidden her to see again the young man she loves. She cannot "
                  "sleep, loses her appetite and finally loses the use of speech; the loss had "
                  "happened once before, in her childhood after an earthquake, and again after a "
                  "severe fright. A strictly Freudian reading would refer it to the oral phase. "
                  "The chapter says that what is fixed on the mouth is not only sexual "
                  "existence but relations with others that have speech as their vehicle. Of all "
                  "bodily functions speech is the most closely bound up with co-existence, so "
                  "the loss of speech stands for a refusal of co-existence, and her inability to "
                  "swallow for the prohibition she cannot, literally, swallow."),
            ("p", "Two readings of the symptom are ready to hand, and the chapter refuses both. "
                  "It is not a paralysis: treated by psychological means and left free by her "
                  "family to see the man she loves, she speaks again. And it is not a deliberate "
                  "silence. &ldquo;To have lost one's voice is not to keep silence: one keeps "
                  "silence only when one can speak.&rdquo; She does not stop speaking; &ldquo;she "
                  "&lsquo;loses&rsquo; her voice as one loses a memory&rdquo;, and the chapter "
                  "explains that with the psychoanalysts' forgetting, an act that keeps a whole "
                  "region of life at arm's length without setting any one memory before the mind "
                  "to be refused. Will supposes a field of possibilities to choose among; what "
                  "collapses when she loses her voice is the field itself. The notion of "
                  "pithiatism, hysterical symptoms that suggestion can bring on or remove, had "
                  "already carried the theory of hysteria beyond the choice between paralysis "
                  "and simulation."),
            ("p", "The lab's other presets code that page. On it the chapter's pair is paralysis "
                  "and simulation, not the two accounts of p. 179; the lesson reads paralysis as "
                  "what a bodily mechanism would make of the symptom and a deliberate silence as "
                  "what a representing consciousness would, the dilemma p. 180 already named "
                  "between automatic response and representation. The mapping is the lesson's. "
                  "The <code>aphonia</code> preset, aphonia being the clinical word for loss "
                  "of voice, has "
                  "two observations. That she speaks again when left free to see him is coded n "
                  "for the mechanism, since a paralysis would not lift with a change in her "
                  "situation, and y for the representing consciousness, since a silence kept on "
                  "purpose would end once the prohibition was lifted. The chapter concedes that "
                  "the recovery rules out paralysis, though on p. 189 it adds that treatment does "
                  "not work by making the patient know the origin of the illness. That she cannot speak even when she wants "
                  "to is coded y for the mechanism and n for the representing consciousness, "
                  "since no decision of hers holds the voice back. The third tile prints both: "
                  "the two accounts part on each. The <code>all</code> preset adds Schneider, and "
                  "the records read one absorbed and two failed for each account, with no "
                  "survivor. Each account fails Schneider, and each fails one of the girl's two "
                  "observations."),
            ("p", "The chapter's own account is not a column, because a column the lesson "
                  "coded for it would come out clean by construction. In prose: the body does "
                  "not express existence as stripes indicate rank or a number a house; the sign "
                  "is filled with what it signifies. The body transforms ideas into things, as "
                  "imitating the sleeper's posture and breathing turns, at some moment, into "
                  "sleep. Her symptom is the refusal of co-existence made into a situation, and "
                  "it is undone not by an intellectual effort or a decree of the will but, the "
                  "chapter says, by a conversion of the whole body, as a forgotten name comes "
                  "back on the tip of the tongue. The reports themselves are Binswanger's; the "
                  "lab codes the reports, not the patient."),
            ("p", "Now the passage. The reason that keeps existence from being reduced to "
                  "sexuality also keeps sexuality from being reduced to existence, and the "
                  "chapter says there is no question of making human existence walk on its "
                  "head, a phrase that recalls Marx turning Hegel the right way up. Two mistakes "
                  "are to be avoided: the philosophies of consciousness, which find in life only "
                  "its obvious content, laid out as distinct representations, and the "
                  "psychologies of the unconscious, which double it with a hidden content also "
                  "made of representations. Sexuality is present as an atmosphere, co-extensive "
                  "with life, and their interfusion is why no act can be labelled. The "
                  "indeterminacy is not a gap in our knowledge: no God, the chapter says, could "
                  "sound our hearts and determine what we owe to nature and what to freedom."),
            ("p", "A long footnote at the chapter's end, pages 198 to 201, makes the same point "
                  "about historical materialism. It cannot be dismissed, the footnote says, by "
                  "rejecting its causal formulations, because it consists as much in making "
                  "economics historical as in making history economic; widening economics as "
                  "Freud widened sexuality raises the same dilemma, and the notion of existence "
                  "lets one leave the dilemma behind. Whether our own time is pre-eminently "
                  "economic is a question it hands to politics, not philosophy. The chapter's "
                  "last line in the main text is a sentence on the human condition: &ldquo;No "
                  "one is saved and no one is totally lost.&rdquo;"),
            ("p", "The chapter has twice compared the body's expressions with a word's: the "
                  "sign filled with its meaning, the body expressing existence as a word "
                  "expresses thought. The next lesson, “Speech as Gesture”, reads Chapter 6, "
                  "where that comparison is examined in speech itself."),
        ],
        "lab": ("phenkit", {
            "mode": "cases",
            "view": "table",
            "accounts": ["a bodily mechanism", "a representing consciousness"],
            "preset": "all",
            "presets": [
                {"id": "schneider",
                 "label": "Schneider as Steinfeld reports him (pp. 179-180)",
                 "observations": "for Schneider after a small occipital wound sight and touch have lost much of their sexual significance, n, n",
                 "expect": {"caRecord": "a bodily mechanism: absorbs 0 of 1, fails 1, silent 0; a representing consciousness: absorbs 0 of 1, fails 1, silent 0", "caSurvivors": "none", "caSplit": "none"}},
                {"id": "aphonia",
                 "label": "Binswanger's patient who lost her voice (pp. 185-189)",
                 "observations": "she speaks again when left free to see him, n, y; "
                                 "she cannot speak even when she wants to, y, n",
                 "expect": {"caSurvivors": "none", "caSplit": "she speaks again when left free to see him, she cannot speak even when she wants to"}},
                {"id": "all",
                 "label": "Both patients, three observations",
                 "observations": "for Schneider after a small occipital wound sight and touch have lost much of their sexual significance, n, n; "
                                 "she speaks again when left free to see him, n, y; "
                                 "she cannot speak even when she wants to, y, n",
                 "expect": {"caRecord": "a bodily mechanism: absorbs 1 of 3, fails 2, silent 0; a representing consciousness: absorbs 1 of 3, fails 2, silent 0", "caSurvivors": "none", "caSplit": "she speaks again when left free to see him, she cannot speak even when she wants to"}},
            ],
            "panel_title": "Two accounts against the chapter's cases",
            "panel_intro": (
                "This lab counts the lesson's coding of the chapter's two patients, as their "
                "doctors reported them, against two classical accounts: a bodily mechanism and a "
                "representing consciousness. Each cell is the lesson's reading of the text; the "
                "chapter's own account is in the prose and is never scored. Compare the "
                "schneider and aphonia presets."
            ),
        }),
        "steps_title": "Counting accounts against cases",
        "steps_intro": "Four steps, the same for any table of this kind.",
        "steps": [
            ("Fix the accounts",
             "Name the accounts the chapter tests, in their own terms, before looking at any "
             "case. Here they are the bodily mechanism and the representing consciousness."),
            ("Code each observation from the text",
             "For each reported observation, mark each account y if the chapter says it can "
             "absorb it, n if the chapter says it cannot, and - if the chapter is silent. Cite "
             "the page for every n."),
            ("Count and compare",
             "An account's record is its count of y, n and -. An account that fails no "
             "observation survives. The two part on an observation that one absorbs and the "
             "other fails."),
            ("State the third account in prose",
             "What the chapter offers instead is said in words, after the table, and never "
             "added as a column: a column coded for it would be clean because it was coded so."),
        ],
        "worked": {
            "title": "Both patients, three observations",
            "intro": [
                "Take the all preset: Schneider coded n and n, the girl speaking again coded n "
                "and y, the girl unable to speak at will coded y and n. You want each record, the "
                "survivors and the split.",
            ],
            "lines": [
                "mechanism:  y on 1, n on 2, so absorbs 1 of 3, fails 2",
                "representation:  y on 1, n on 2, absorbs 1 of 3, fails 2",
                "survivors:  each fails something, so none",
                "Schneider:  n against n, so not in the split",
                "the girl's two:  y against n each time, so both split",
            ],
            "after": [
                "Neither account survives, and each fails Schneider: the occipital wound freed "
                "no automatism, and his loss is not a weakness of representations. The two part "
                "on both of the girl's observations, each absorbing the one the other fails. "
                "The count is exact; the coding is the lesson's reading of the reports.",
            ],
        },
        "quiz_title": "Sexuality and existence",
        "quiz": [
            {"q": "A fourth observation is added to the all preset and coded y for the bodily "
                  "mechanism and y for the representing consciousness. What do the records and "
                  "survivors now show?",
             "a": ["Both accounts now survive",
                   "Each absorbs 2 of 4 and fails 2; still no survivor",
                   "Each absorbs 2 of 4 and fails 1; still no survivor",
                   "The new observation joins the split"],
             "c": 1,
             "why": "A y adds to each account's absorbed count and leaves its failures at 2, so "
                    "neither survives. Nothing removes a failure. The split holds only "
                    "observations coded y against n, and this one is y against y."},
            {"q": "Why, according to the chapter, does Schneider's case tell against the view "
                  "that sexuality is an autonomous reflex apparatus?",
             "a": ["His reflex apparatus was destroyed by the wound",
                   "He has lost every representation, visual and tactile",
                   "A small occipital wound should then have freed the automatic responses and "
                   "made his sexual behaviour more marked, not less",
                   "He recovered once the cause was explained to him"],
             "c": 2,
             "why": "The text says that if sexuality were an autonomous reflex apparatus, the "
                    "cerebral injury would have freed the automatic responses and accentuated his "
                    "sexual behaviour. The apparatus is not said to be destroyed, the chapter "
                    "doubts that he lacks tactile representations, and no recovery of his is "
                    "reported."},
            {"q": "What, in the chapter, shows that the girl's loss of voice is not a paralysis?",
             "a": ["She cannot speak even when she wants to",
                   "The loss had happened before, after an earthquake",
                   "Her throat and mouth may have been particularly sensitive",
                   "Treated by psychological means and left free to see the man she loves, she "
                   "speaks again"],
             "c": 3,
             "why": "The text says loss of voice is not paralysis, and that this is proved by her "
                    "recovering her speech when treated and left free to see him. Being unable to "
                    "speak at will is what shows it is not a deliberate silence, which would fit a "
                    "paralysis. The earlier episodes and the sensitivity are part of the chapter's "
                    "account of why the emotion took this form."},
            {"q": "Which of these is the chapter's own conclusion about sexuality and existence?",
             "a": ["Each permeates the other, so no decision can be labelled sexual or "
                   "non-sexual",
                   "All existence is at bottom sexual, as the psychoanalysts showed",
                   "Sexuality is only a symptom of an existential drama",
                   "Sexuality is a separate function located in its organs"],
             "c": 0,
             "why": "The passage calls the relation interfusion and draws exactly that "
                    "consequence. The chapter says that reducing existence to sexuality makes the "
                    "claim a tautology, that the sexual drama is not merely a symptom of an "
                    "existential one, and that sexual life is not a separate function defined by "
                    "its organs."},
        ],
        "mistakes": [
            ("Thinking Merleau-Ponty reduces sexuality to existence, or existence to sexuality",
             "Read quickly, the chapter seems to dissolve sexuality into a manner of being in "
             "the world, or, read the other way, to find sex everywhere. It says neither. The "
             "same reason that forbids reducing existence to sexuality forbids reducing "
             "sexuality to existence; the relation is interfusion, in which each permeates the "
             "other. The footnote on historical materialism makes the same point about "
             "economics and history: neither is reduced to the other, though every cultural "
             "fact has an economic significance among others. In the lab, neither classical "
             "account survives the three observations, and the chapter's account is stated in "
             "prose rather than scored."),
            ("Reading the loss of voice as a message she means to send",
             "That is the representing consciousness's reading: an inner state, decided on and "
             "made public. The chapter compares it to a head of state's gesture or a friend who "
             "stops speaking to you, and rejects it: one keeps silence only when one can speak, "
             "and she cannot. The cell coding that observation n for the representing "
             "consciousness is this reading."),
            ("Taking the chapter's Freud for Freud's own self-understanding",
             "The chapter reads psychoanalytic practice against Freud's theoretical "
             "declarations, and says so: whatever Freud's declarations may have been. Freud's "
             "theory spoke of drives and their energies, and whether the chapter's Freud, for "
             "whom every action has a meaning and the sexual is not the genital, is Freud or a "
             "reading of him is disputed."),
        ],
        "standard": (
            "Finish when you can count two accounts against the chapter's cases and state the "
            "account the chapter gives instead.",
            "Given the lesson's coding of Schneider and of Binswanger's patient, compute each "
            "account's record, the survivors and the split; give the page on which the chapter "
            "rejects each account at each case; and state, in prose, the chapter's account of "
            "sexuality as interfused with existence."
        ),
        "note": (
            "Every cell is the lesson's reading of the chapter, and the observations are the "
            "chapter's report of its sources' reports, Steinfeld's on Schneider and "
            "Binswanger's on the girl; the lab codes the reports, not the patients, and "
            "Schneider's reports were later questioned. The lab can show that each classical "
            "account fails somewhere. It cannot show that sexuality is an atmosphere "
            "co-extensive with life, which is the chapter's claim and is argued in prose."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Smith pp. 206-207 (opening passage: "Thus we refute ... has a meaning."
    # p. 206, and "Thus speech, in the speaker ... accomplishes it." p. 207);
    # p. 203 (verbal images; no speaking subject; the electric lamp;
    # anarthria; automatic and intentional language); p. 204 ('no'; amnesia
    # for colour names; the sorting test; the pale blue ribbon; the eidos
    # blue; the categorial and the concrete attitude, in the voice of the
    # intellectualist theory of aphasia, Gelb and Goldstein footnote 2);
    # p. 205 (the kinship of empiricism and intellectualism; nobody to speak,
    # a thinking subject); p. 206 (writers who begin a book; 'It is a brush';
    # "The denomination ... itself recognition."); p. 207 (the listener);
    # p. 208 (gestural meaning; a foreign country); p. 209 (the orator; words
    # behind me); p. 210 (one means of representing a word: uttering it);
    # p. 221 (an existential theory of aphasia, whether its authors are aware
    # of it or not); p. 222 (the normal subject's heap of samples; viscosity;
    # passive perception; "We were wrong to say ..."); p. 223 ("in reality he
    # never adopts any"; productive imagination; Gelb and Goldstein's
    # sentence "Categorial behaviour ... behaviour.", footnote 26); p. 224
    # (patients who sort by naming; the emptied word); p. 225 (gestural or
    # existential significance).
    {
        "slug": "speech-as-gesture",
        "title": "Speech as Gesture",
        "module": "Part One · 6 · Expression and Speech",
        "one_line": "The word is neither a trace set off by a stimulus nor an empty sign of a thought that could do without it: it has a meaning, and speech accomplishes thought rather than translating it.",
        "summary": (
            "Chapter 6 begins by asking what it is to have language, and finds the empiricist "
            "and the intellectualist agreeing that the word has no meaning of its own. Its test "
            "case is Gelb and Goldstein's patients who could neither name colours nor sort them. "
            "Compute a sort by colour category and a chain of concrete resemblances, name the "
            "sample where they part, and say how the chapter reads the case against its own "
            "authors' first interpretation."
        ),
        "key": [
            "empiricism: nobody speaks",
            "intellectualism: only a thinker",
            "the word has a meaning",
            "naming is itself recognition",
            "speech accomplishes thought",
            "the sort and the chain part at one sample",
        ],
        "key_label": "The first half of the chapter in six lines",
        "concepts_intro": (
            "The first half of Chapter 6 states two theories of language, finds them agreeing "
            "on one point, and denies that point. A clinical test case runs through it."
        ),
        "concepts": [
            ("The verbal image",
             "The empiricist's account of having a word: a trace left in the brain or the mind "
             "by words heard or spoken, which a stimulus or an association calls up. On this "
             "account, the chapter says, there is no one who speaks."),
            ("The categorial attitude",
             "Gelb and Goldstein's term for the ability to take a thing as a representative of "
             "a kind, this red as a case of red. Its loss, they first argued, explains why some "
             "patients can neither name colours nor sort them."),
            ("Gestural meaning",
             "The chapter's term for the meaning a word carries in its use, its style and tone, "
             "before any concept is drawn from it; the conceptual meaning, it says, is formed "
             "from this."),
        ],
        "read_title": "The passage first, then the chapter's first half and its return to the case",
        "read_intro": (
            "The passage is the chapter's answer to both theories. The lesson goes back to the "
            "chapter's opening, follows it through the colour test to the passage, and then to "
            "the pages where the chapter returns to the same patients."
        ),
        "body": [
            ("p", "<strong>Part One, Chapter 6, pp. 206&ndash;207.</strong> &ldquo;Thus we "
                  "refute both intellectualism and empiricism by simply saying that the word has "
                  "a meaning.&rdquo; And on the next page: &ldquo;Thus speech, in the speaker, "
                  "does not translate ready-made thought, but accomplishes it.&rdquo; Read the "
                  "chapter from its first page, 202, to the end of the paragraph on page 214, and "
                  "then pages 221 to 225, where it comes back to the same patients, in your own "
                  "copy before going on."),
            ("p", "The chapter starts from the first account of language, the one it calls "
                  "empiricist or mechanistic. To possess language is to possess verbal images, "
                  "traces left by words heard or spoken, whether in the nerves or in an "
                  "unconscious mind. A stimulus, or an associated state of mind, calls up the "
                  "right image, and the word is pronounced. On this picture, the chapter says, "
                  "speech happens in a circuit of third-person events: there is a flow of words "
                  "and no one who means them, and a person can speak as an electric lamp can "
                  "glow. The account had evidence. Aphasia, the loss or disturbance of language "
                  "after an injury to the brain, can strike spoken language and spare written "
                  "language, or the reverse, and language can break into fragments; so it "
                  "seemed to be built of independent pieces."),
            ("p", "Then the theory changed, and the chapter tells the story. Neurologists came "
                  "to separate anarthria, the loss of the power to articulate, from aphasia "
                  "proper, and automatic language from intentional language. A patient could "
                  "find the word <em>no</em> in answer to the doctor's questions, when he meant "
                  "to deny something in his present experience, and could not say it as an "
                  "exercise. What the patient had lost was not a stock of words but "
                  "a way of using them. Adhémar Gelb, a psychologist, and Kurt Goldstein, a "
                  "neurologist, who studied brain-injured soldiers together in Frankfurt during "
                  "and after the First World War, examined patients with amnesia for the names of colours, "
                  "and found that the same patients could not sort colours either."),
            ("p", "The test was to sort a heap of coloured samples by basic colour. The "
                  "patients worked more slowly than normal subjects, put the samples side by "
                  "side to compare them, and did not see at a glance which went together. Then, "
                  "having correctly collected several blue ribbons, they made what the chapter "
                  "calls unaccountable mistakes: &ldquo;if for example the last blue ribbon was "
                  "of a pale shade, they carry on by adding to the collection of &lsquo;blues&rsquo; "
                  "a pale green or pale pink&rdquo;. The lab's <code>ribbons</code> preset sets "
                  "that up with lightness figures of the lesson's own, on a scale from 0 for the "
                  "darkest to 10. The first tile is the sort by hue name, <code>blue: dark blue, "
                  "mid blue, pale blue; green: pale green; pink: pale pink</code>. The second is "
                  "the chain, <code>dark blue → mid blue → pale blue → pale green → pale "
                  "pink</code>, and the third names <code>pale green</code> as the sample where "
                  "the chain first leaves blue."),
            ("p", "The chain follows the lesson's rule, printed in the lab's banner: from the "
                  "starting sample, take each time the unsorted sample nearest the last one "
                  "taken, counting the difference in lightness and adding 1 when the hue "
                  "differs, ties going to the sample listed first. No theory in the book states "
                  "this rule; it is the lesson's model of a sort by concrete resemblance, built "
                  "so that you can see where such a sort and a sort by category come apart. "
                  "From pale blue at 8, pale green at 8 costs 0 plus 1 for the change of hue, and "
                  "nothing else is as near."),
            ("p", "The interpretation came with the test, and the chapter first states it as if "
                  "it were its own, answering it only later. To name a thing is to tear oneself away from its individual "
                  "characteristics and see it as representing a category; the patients have not "
                  "lost the verbal images of the words <em>red</em> and <em>blue</em> but the "
                  "general ability to subsume a sensory given under a category, and have fallen "
                  "back from the categorial to the concrete attitude. Even when they sort "
                  "correctly, it is an immediate resemblance that guides them, not the samples' "
                  "fitting an idea. At its strength the account is economical: one deficit "
                  "explains both the lost names and the failed sort, and it makes language "
                  "depend on thought, the opposite of the theory of the verbal image."),
            ("def", ("The categorial and the concrete attitude (Gelb and Goldstein)",
                     "In the categorial attitude a sample is taken as a case of a kind, and the "
                     "kind holds the sort together from start to finish; in the concrete "
                     "attitude each sample is met in its individual look, and only the felt "
                     "resemblance of one to the next can join them.")),
            ("p", "The lab's other presets mark out what the two sorts do. The "
                  "<code>samples</code> preset has seven: pale, mid and dark red at 9, 6 and 3, "
                  "pale and mid green at 8 and 5, brown at 2 and dark brown at 1, starting from "
                  "pale red. The categorical sort gives three groups. The chain runs <code>pale "
                  "red → pale green → mid red → mid green → dark red → brown → dark brown</code>, "
                  "leaving red at <code>pale green</code> on its first step, because pale green "
                  "at 8 is nearer pale red at 9 than mid red at 6 is. The "
                  "<code>lightness</code> preset keeps only the three reds, and the chain and the "
                  "sort agree: the third tile prints <code>none</code>. The <code>close</code> "
                  "preset starts from a dark red at 2 beside a brown at 2, and the chain goes to "
                  "the brown before the other reds."),
            ("p", "Merleau-Ponty's first reply is that the new theory and the old one are "
                  "kin. Both hold that the word has no significance of its own. For the "
                  "empiricist the word is a physical or psychic event thrown up by causes. For "
                  "the intellectualist it is the outward sign of an inner recognition that "
                  "could happen without it, an empty container whose meaning belongs to "
                  "thought. &ldquo;In the first there is nobody to speak; in the second, there "
                  "is certainly a subject, but a thinking one, not a speaking one.&rdquo; And "
                  "once the categorial act is done, the intellectualist still needs a mechanism "
                  "to produce the word. So the chapter refutes both, as the passage says, by "
                  "saying that the word has a meaning."),
            ("p", "Why believe that? If speech presupposed thought, the chapter asks, why would "
                  "thought tend towards expression as towards its completion, why would the most "
                  "familiar thing seem indeterminate until we recall its name, and why would so "
                  "many writers begin a book without knowing exactly what they will put in it? "
                  "When you look at something in the half-light and say <em>it's a brush</em>, "
                  "there is no concept of a brush in your mind under which you first subsume "
                  "it. &ldquo;The denomination of objects does not follow upon recognition; it "
                  "is itself recognition.&rdquo; That is the passage's second sentence: speech "
                  "accomplishes thought. The listener, likewise, receives thought from speech, "
                  "as you learn a word in a foreign country from its place in what people are "
                  "doing. The conceptual meaning of words is formed, the chapter says, from a "
                  "gestural meaning immanent in speech."),
            ("p", "The orator does not think before speaking, nor even while speaking: his "
                  "speech is his thought. The words you know are not verbal images you consult. "
                  "They are behind you, the chapter says, like things behind your back or the "
                  "city's horizon round your house; you rely on them without picturing them, "
                  "and you have only one way of representing a word, which is to say it. The "
                  "chapter's earlier reply to the representation of movement, that you need not "
                  "picture your body to move it, is repeated here for the word."),
            ("p", "Later, on page 221, the chapter comes back to the patients, and to its own "
                  "first description of them. Whether the theory's authors, Goldstein among "
                  "them, knew it or not, it says, they were moving towards an existential theory of aphasia, one that "
                  "treats thought and language as two forms of a single way of being directed "
                  "towards a world. For a normal subject the task organises the heap: the colours "
                  "of the model's category stand out from the rest. For the patient each sample "
                  "stays shut in its own existence, and the heap resists grouping with a kind of "
                  "viscosity. And the chapter corrects itself: it was wrong to say that the "
                  "patient cannot keep to a principle of classification and goes from one to "
                  "another, since he never adopts one at all. What is disturbed, in Kant's "
                  "terms, is not so much the understanding as the productive imagination, the "
                  "power that lays out experience to be judged."),
            ("p", "The chapter's evidence here is Gelb and Goldstein's own, and so is its "
                  "summary sentence, which it quotes from them: &ldquo;Categorial behaviour and "
                  "the possession of meaningful language express one and the same fundamental "
                  "form of behaviour.&rdquo; Neither is cause or effect of the other. Some "
                  "patients sort by naming the model's colour and collecting what the name fits, "
                  "without looking back at the model; the chapter calls that an abnormal "
                  "procedure, language and thought both cut off from their living significance. "
                  "Other patients can repeat the colour names and still not sort. The patient "
                  "who is given a name repeats it as if he expected something to come of it, "
                  "and it tells him nothing. The word has not lost a concept behind it; it has "
                  "been emptied, and the chapter's conclusion is that the meaning inhabits the "
                  "word."),
            ("p", "So the lab's two sorts are both outsiders' constructions. The categorical "
                  "sort is what a normal subject's task produces; the chain is the lesson's "
                  "rule for a sort by resemblance, and the chapter's corrected description of "
                  "the patients is that they adopt no principle of classification at all. What "
                  "the lab shows exactly is where the "
                  "two come apart. The next lesson, “The Spoken Word and Thought”, follows the "
                  "chapter from the word to the gesture, and asks whether the gesture's meaning "
                  "is natural and the word's conventional."),
        ],
        "lab": ("phenkit", {
            "mode": "sorting",
            "view": "sort",
            "model": "the lesson's model of a sort by concrete resemblance",
            "preset": "ribbons",
            "presets": [
                {"id": "ribbons",
                 "label": "Blue ribbons ending in a pale one, then a pale green and a pale pink (after p. 204; lightness figures illustrative)",
                 "samples": "dark blue, blue, 2; mid blue, blue, 5; pale blue, blue, 8; pale green, green, 8; pale pink, pink, 9",
                 "start": "dark blue",
                 "expect": {"soCategorical": "blue: dark blue, mid blue, pale blue; green: pale green; pink: pale pink", "soChain": "dark blue → mid blue → pale blue → pale green → pale pink", "soPart": "pale green"}},
                {"id": "samples",
                 "label": "Seven samples in three hues, from pale red (illustrative)",
                 "samples": "pale red, red, 9; mid red, red, 6; dark red, red, 3; pale green, green, 8; "
                            "mid green, green, 5; brown, brown, 2; dark brown, brown, 1",
                 "start": "pale red",
                 "expect": {"soCategorical": "red: pale red, mid red, dark red; green: pale green, mid green; brown: brown, dark brown", "soChain": "pale red → pale green → mid red → mid green → dark red → brown → dark brown", "soPart": "pale green"}},
                {"id": "lightness",
                 "label": "Three reds only (illustrative)",
                 "samples": "pale red, red, 9; mid red, red, 6; dark red, red, 3",
                 "start": "pale red",
                 "expect": {"soChain": "pale red → mid red → dark red", "soPart": "none"}},
                {"id": "close",
                 "label": "A dark red beside a brown of the same lightness (illustrative)",
                 "samples": "dark red, red, 2; pale red, red, 9; light red, red, 8; brown, brown, 2",
                 "start": "dark red",
                 "expect": {"soChain": "dark red → brown → light red → pale red", "soPart": "brown"}},
            ],
            "panel_title": "A sort by category and a chain of resemblances",
            "panel_intro": (
                "This lab computes the lesson's model, not the book's and not Gelb and "
                "Goldstein's: a sort by hue name beside a chain that always takes the sample "
                "nearest the last, by a rule printed in the banner. Lightness figures are the "
                "lesson's. Compare the ribbons and lightness presets."
            ),
        }),
        "steps_title": "Setting a sort by category beside a chain",
        "steps_intro": "Four steps, the last of which is the chapter's.",
        "steps": [
            ("Sort by category",
             "Group the samples by hue name, keeping the order they were listed in. That is "
             "the sort the task asks for."),
            ("Build the chain",
             "From the starting sample, take the unsorted sample nearest the last one taken: "
             "the difference in lightness, plus 1 if the hue differs. On a tie, take the one "
             "listed first."),
            ("Find where they part",
             "The first sample in the chain whose hue differs from the start's is where the "
             "chain leaves the category. If there is none, the two sorts agree."),
            ("Say whose sort each is",
             "The categorical sort is what the task asks of a normal subject; the chain is the "
             "lesson's rule. The chapter's last description of the patients is that they "
             "adopt no principle at all."),
        ],
        "worked": {
            "title": "Seven samples, from pale red",
            "intro": [
                "Take the samples preset: reds at 9, 6 and 3, greens at 8 and 5, browns at 2 "
                "and 1, starting from pale red. You want the categorical sort, the chain and "
                "the sample where they part.",
            ],
            "lines": [
                "by hue:  three reds, two greens, two browns",
                "from pale red 9:  pale green costs 1 + 1, mid red 3",
                "from pale green 8:  mid red and mid green both 3",
                "tie:  mid red is listed first, so it comes next",
                "then:  mid green, dark red, brown, dark brown",
                "leaves red at:  pale green, the first step",
            ],
            "after": [
                "The categorical sort keeps the reds together; the chain leaves red at its "
                "first step, because pale green is nearer pale red in lightness than any other "
                "red. It has the shape of the report's pale green after a pale blue, which the "
                "ribbons preset codes directly. Neither sort is the patient's experience, and "
                "the chapter's corrected description is that the patient adopts no principle "
                "of classification at all.",
            ],
        },
        "quiz_title": "The word and the category",
        "quiz": [
            {"q": "The samples are dark green (green, 2), pale green (green, 9) and dark blue "
                  "(blue, 3), and the chain starts from dark green. Where does the chain first "
                  "leave green?",
             "a": ["pale green", "none: it never leaves green", "dark blue", "dark green"],
             "c": 2,
             "why": "From dark green at 2, dark blue costs 1 for lightness plus 1 for the hue, "
                    "which is 2, and pale green costs 7. So dark blue comes second and is the "
                    "first sample of another hue. Pale green is green, the chain does leave "
                    "green, and dark green is the start."},
            {"q": "How did Gelb and Goldstein first explain why the patients could neither name "
                  "colours nor sort them, as the chapter reports it?",
             "a": ["They had lost the verbal images of the colour words",
                   "They could no longer see differences of colour",
                   "They sorted at random, by no resemblance at all",
                   "They had lost the general ability to subsume a sensory given under a "
                   "category"],
             "c": 3,
             "why": "The chapter reports the interpretation that the patients had lost not the "
                    "verbal images but the ability to subsume, and had fallen back to the "
                    "concrete attitude. The lost verbal image is the older theory this one "
                    "replaced, the patients do see the samples, and they are said to be guided "
                    "by immediate resemblance."},
            {"q": "On what, according to the chapter, do empiricism and intellectualism agree "
                  "about language?",
             "a": ["That the word has no significance of its own",
                   "That speech is a purely motor phenomenon",
                   "That thought is an effect of language",
                   "That the patients have lost the verbal images"],
             "c": 0,
             "why": "The text says both conceptions are at one in holding that the word has no "
                    "significance: for one it is an event set off by causes, for the other an "
                    "empty sign of thought. Intellectualism makes language depend on thought, "
                    "not the reverse, and only the empiricist speaks of verbal images."},
            {"q": "When the chapter returns to the patients on pp. 222 and 223, how does it "
                  "correct its first description of them?",
             "a": ["They sort correctly, only more slowly than normal subjects",
                   "They do not switch between principles of classification; they never adopt "
                   "one",
                   "They have lost the names and nothing else",
                   "They keep consistently to a principle of lightness instead of hue"],
             "c": 1,
             "why": "The text says it was wrong to say that the patient cannot abide by a given "
                    "principle and goes from one to another: in reality he never adopts any. "
                    "Slowness is part of the first description, the chapter says the disorder "
                    "touches the experience of colours and not only the names, and keeping to "
                    "lightness would be adopting a principle."},
        ],
        "mistakes": [
            ("Accepting Gelb and Goldstein's first reading as the chapter's",
             "Stated at strength, the reading is: the patient has lost the categorial "
             "attitude; his words are intact, but he can no longer subsume a sample under a "
             "category, so he sorts by concrete resemblance. The chapter sets it out on pp. 204 "
             "and 205 without marking it as another's, with Gelb and Goldstein in the "
             "footnote, and then answers it. The word and the category are not "
             "two things, one of which could be lost behind the other; the disturbance is in "
             "the way the colours group themselves for the patient; and the word the patient "
             "keeps has been emptied, not cut off from a concept. Its authors, the chapter "
             "says, were moving towards that conclusion themselves."),
            ("Treating words as labels on categories that are still there",
             "The naive view: the patient still has the category red and has only lost the "
             "label. Then giving him the label should restore the sort. The chapter reports "
             "that patients can repeat the colour names and still not sort, and that a name "
             "given to the patient tells him nothing. Some patients do sort by naming the "
             "model's colour and collecting what the name fits, as the <code>samples</code> "
             "preset's categorical sort uses the hue names as its rule; the chapter calls that "
             "an abnormal procedure, in which language and thought are both cut off from their "
             "living significance."),
            ("Taking the chain's rule for what the patient does",
             "The lab's chain follows a rule: the nearest sample to the last, by lightness "
             "plus 1 for a change of hue. It is the lesson's model, and it matches the report "
             "that a pale blue was followed by a pale green. But the chapter's corrected "
             "description is that the patient adopts no principle of classification at all, "
             "so no principle, this rule included, is what the patient adopts."),
        ],
        "standard": (
            "Finish when you can set a sort by category beside a chain of resemblances and "
            "state how the chapter reads the case.",
            "Given colour samples with hue names and lightness figures, compute the "
            "categorical sort, the chain from a given start and the sample where they part; "
            "state Gelb and Goldstein's first reading at strength, and the chapter's reply that "
            "the word has a meaning."
        ),
        "note": (
            "The chain's rule and every lightness figure are the lesson's, built to show where "
            "two kinds of sort part; the book gives no figures and no rule, and its corrected "
            "description says the patient follows none. The case is Gelb and Goldstein's "
            "report, as the chapter reads it. The lab cannot show that the word has a meaning "
            "of its own, which is the chapter's claim, and it cannot show what grouping the "
            "patient saw."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Smith p. 214 (opening passage: "The spoken word ... a world."); p. 219
    # (opening passage: "The angry Japanese ... his words."); p. 214 (Scheler;
    # "The gesture does not make me think of anger, it is anger itself.";
    # the carpet; the dog and the praying mantis); p. 215 (recaptured by an
    # act; as if the other person's intention inhabited my body; the
    # fireplace); p. 216 (blind recognition; the caress, Sartre); pp. 216-217
    # (the objection: the gesture's world is given, the word's is not; the
    # keyboard of acquired meanings; the smile that has joy in it, stated in
    # setting up the objection; natural signs and conventions, "what is
    # commonly expressed"); p. 217 (conventions a late form; the verbal form
    # appears arbitrary; 'singing' the world; not onomatopoeia); p. 218
    # (nuit and lumiere; never translatable; T. E. Lawrence); p. 219 ("in man
    # there is no natural sign"; anatomical organization; the difference in
    # the emotions themselves); p. 220 ("It is no more natural ... 'a
    # table'."; "Feelings and passional conduct are invented like words.";
    # paternity; both manufactured and natural); pp. 220-221 (speech alone
    # sediments; speak about speech, not paint about painting; Reason);
    # p. 225 (Darwin and the knitted brows); p. 226 (wholly motility and
    # wholly intelligence); p. 228 (Schneider's language, after Benary);
    # p. 229 (a speaking word and a spoken word; "Speech is the surplus ...");
    # p. 230 ("It is the body which points out, and which speaks"; Cezanne);
    # pp. 230-232 (two senses of 'exist'; Descartes to Elizabeth, 1643).
    {
        "slug": "the-spoken-word-and-thought",
        "title": "The Spoken Word and Thought",
        "module": "Part One · 6 · Expression and Speech",
        "one_line": "A gesture is no more a natural sign than a word is a mere convention: anger is read in the gesture, the gesture differs from culture to culture, and speech is the one expression that settles into an acquisition.",
        "summary": (
            "The second half of Chapter 6 reads the word as a gesture and asks whether that "
            "makes speech natural. The chapter answers that there is no natural sign in man: "
            "the angry Japanese smiles, and the Westerner goes red or pale. Compute what bodily "
            "sign, if any, every expression of anger shares, find that none does, and state "
            "what the chapter makes of the speaking and the spoken word."
        ),
        "key": [
            "the gesture is anger itself",
            "in man there is no natural sign",
            "anger: no bodily sign in every culture",
            "feelings are invented like words",
            "speaking word: meaning coming to be",
            "spoken word: meanings already acquired",
        ],
        "key_label": "The second half of the chapter in six lines",
        "concepts_intro": (
            "The second half of Chapter 6 takes the gesture as the model of the word, meets "
            "the classical objection that the gesture is natural and the word conventional, "
            "and answers it."
        ),
        "concepts": [
            ("Natural sign and conventional sign",
             "The classical division the chapter takes up: a natural sign, like a blush or a "
             "smile, would mean what it means because of how the body is built; a "
             "conventional sign, like the word <em>table</em>, means what it means by "
             "agreement, and could have been otherwise."),
            ("The speaking word",
             "Smith's phrase for speech in which a meaning is coming into being for the first "
             "time: the child's first words, the writer's or philosopher's new thought."),
            ("The spoken word",
             "Language as an acquired store of available meanings, the vocabulary and syntax "
             "a speaker uses as one might use a fortune already made, and on which new "
             "speaking draws."),
        ],
        "read_title": "The passage first, then the second half of the chapter line by line",
        "read_intro": (
            "The passage is two sentences five pages apart: the chapter's claim about speech "
            "and the case that tests it. The lesson reads the gesture first, then the "
            "objection, then the reply, and ends where Part One ends."
        ),
        "body": [
            ("p", "<strong>Part One, Chapter 6, pp. 214 and 219.</strong> &ldquo;The spoken "
                  "word is a gesture, and its meaning, a world.&rdquo; Five pages later: "
                  "&ldquo;The angry Japanese smiles, the westerner goes red and stamps his foot "
                  "or else goes pale and hisses his words.&rdquo; Read from page 214, where the "
                  "paragraph on gestures begins, to the end of the chapter on page 232, in your "
                  "own copy before going on; "
                  "pages 221 to 225, on aphasia, were read in the last lesson."),
            ("p", "Across a café you see two people at a table you cannot hear. One leans "
                  "forward, the jaw set, a hand flat on the table, and you know before any "
                  "word reaches you that this is anger. How do you know? The obvious answer is "
                  "that you recall your own feelings when you made that gesture, and reason "
                  "by analogy. The chapter reports modern psychology, Max Scheler's among it, "
                  "against that answer; Scheler was a German philosopher who in the 1910s and "
                  "1920s wrote on sympathy and on how we know other minds. You know very little "
                  "from inside of what your own face does in anger, so the analogy has nothing "
                  "to work with, and you do not see anger as a fact hidden behind the gesture. "
                  "&ldquo;The gesture does not make me think of anger, it is anger itself.&rdquo;"),
            ("p", "But the meaning of a gesture is not seen as the colour of the carpet is. If it "
                  "were, the chapter says, it would be hard to see why we understand mostly "
                  "human gestures, and not the sexual pantomime of a dog or a praying mantis, or "
                  "even the emotions of people in circles very unlike our own. The sense of a "
                  "gesture is not given but understood: taken up by an act of the spectator's. "
                  "It is as if the other person's intention inhabited my body and mine his; the "
                  "gesture outlines an object and invites me to join in, and communication "
                  "happens when my conduct finds the same path. The chapter compares this to "
                  "perceiving a fireplace, which I take as a whole at once and not as the sum of "
                  "views I have checked against each other, and it calls the recognition blind: "
                  "it comes before any intellectual working out, as people performed the caress "
                  "for generations before a philosopher, Sartre in the footnote, gave its "
                  "intellectual meaning."),
            ("p", "The linguistic gesture, the chapter says, likewise outlines its own meaning, "
                  "and then it states the objection at length. A gesture points to a "
                  "relationship between a person and the perceptible world, and that world is "
                  "given to the spectator along with the gesture; a word aims at a mental "
                  "setting that is not given to everyone. The first reply is that what nature "
                  "does not supply, culture does. Earlier acts of expression leave available "
                  "meanings that make a common world between speakers, and new speech plays on "
                  "this keyboard of acquired meanings as a gesture plays on the perceived world. "
                  "But then where did the acquired meanings come from? The objection presses. "
                  "In emotional expression one can see what the gesture and its meaning have in "
                  "common: the smile and the relaxed face have in them the rhythm of joy. The "
                  "word's link with its meaning looks accidental, as the existence of many "
                  "languages shows. This, the chapter says, is what is commonly expressed by "
                  "calling gesture a natural sign and the word a convention."),
            ("def", ("The classical division of signs",
                     "Emotional gesture is a natural sign, the same in every body because the "
                     "body is built the same; the word is a conventional sign, which means what "
                     "it does by agreement. So, on this division, speech cannot be gesture.")),
            ("p", "The chapter replies twice. First, conventions are a late form of relationship "
                  "between people; they presuppose an earlier way of communicating, and "
                  "language has to be put back into it. The chapter grants that, if you consider "
                  "only a word's conceptual meaning, the verbal form, endings apart, looks "
                  "arbitrary. Taken with its gestural sense, which is everything in poetry, it "
                  "does not. Words and phonemes, the sounds a language is built from, are so "
                  "many ways of singing the world, not "
                  "because they imitate things, as the naive theory of onomatopoeia held, but "
                  "because they draw out their emotional essence. If the accidents of phonetics "
                  "and borrowing could be set aside, the chapter suggests, with a probably, a "
                  "language's original form would show a system not wholly arbitrary, in which "
                  "calling night <em>nuit</em> makes it fitting to call light <em>lumière</em>. That is why "
                  "the full meaning of one language never passes into another, and why one of "
                  "the languages we speak is always the one we live in."),
            ("p", "Second, and here the passage's case comes in, the chapter will not grant the "
                  "other half of the division either. It does not reduce language to emotional "
                  "expression, because &ldquo;in man there is no natural sign&rdquo;. A natural "
                  "sign would need the body's anatomy to tie a given gesture to a given state of "
                  "mind, and it does not. The angry Japanese smiles; the Westerner goes red and "
                  "stamps, or goes pale and hisses. Having the same organs and nerves is not "
                  "enough for the same emotion to produce the same signs, and the chapter goes "
                  "further: the difference of behaviour corresponds to a difference in the "
                  "emotions themselves. What matters is how a person uses the body."),
            ("p", "The lab looks for the natural sign. The <code>anger</code> preset codes the "
                  "passage's three expressions with the signs the sentence names: the Japanese "
                  "smile, the Westerner's flush and stamp, the Westerner's pallor and hiss, each "
                  "marked as anger. The core, the sign every expression of anger has, is "
                  "<code>none</code>, and every sign is on the list of what varies. The "
                  "<code>west</code> preset keeps only the two Western expressions, and the core "
                  "is still <code>none</code>: the sentence's <em>or else</em> already gives one "
                  "culture two ways. The third tile, in both, says no variant is marked as not "
                  "anger."),
            ("p", "The <code>smile</code> preset asks the question the other way round. It "
                  "codes the angry Japanese's smile as anger and adds a smile of pleasure, the "
                  "lesson's addition, marked as not anger. With one expression of anger the core "
                  "is its one sign, <code>smile</code>, nothing varies, and the third tile prints <code>smile in "
                  "pleasure lacks none of the core</code>. Everything the coding found in the "
                  "angry smile is in the pleased one, so the sign alone does not decide which "
                  "emotion it is. The objection's smile that has joy in it is not denied; what the "
                  "chapter denies is that anatomy makes it joy's sign, since a natural sign "
                  "would need the body's organisation to tie a gesture to a state of mind."),
            ("p", "Then the sentence the section turns on: &ldquo;It is no more natural, and no "
                  "less conventional, to shout in anger or to kiss in love than to call a table "
                  "&lsquo;a table&rsquo;.&rdquo; A footnote observes that the kiss is not one of "
                  "the traditional customs of Japan. &ldquo;Feelings and passional conduct are "
                  "invented like words.&rdquo; Even paternity, the chapter says, is an "
                  "institution. This is not the claim that emotions are arbitrary. Everything in "
                  "man is both manufactured and natural: no word and no form of behaviour owes "
                  "nothing to biological being, and none fails to slip away from the simplicity "
                  "of animal life. Speech is one case of a power to create meanings that cannot "
                  "be inventoried."),
            ("p", "What sets speech apart, the chapter says, is that alone of all expressive "
                  "processes it settles into a sediment and becomes an acquisition. Writing is "
                  "not the reason, since music can be written down too. The difference is that "
                  "each writer knows he is aiming at the same world others have written about, "
                  "that one can speak about speech and cannot paint about painting, and that "
                  "every philosopher has dreamed of a discourse to supersede all others, as no "
                  "painter dreams of exhausting painting. This is what gives Reason its "
                  "privileged position and the ideal of a thought without words. To understand it, "
                  "the chapter says, thought has to be put back among the phenomena of "
                  "expression."),
            ("p", "At the end of the pages on aphasia and just after them, the chapter shows "
                  "the same power in its beginnings and in its failure. Charles Darwin, the naturalist who wrote on the "
                  "expression of the emotions, thought the knitting of the brows began as a way "
                  "of shielding the eye from the sun; it becomes part of the human act of "
                  "thinking hard and shows it to anyone watching. Speech is in this sense wholly "
                  "motility and wholly intelligence. And Schneider, studied this time by Benary, "
                  "has his vocabulary and syntax intact but never feels the need to speak, never "
                  "speaks of what is merely possible, and finds a sentence like <em>the sky is "
                  "black</em> meaningless: his meanings, the chapter says, are ossified. As with "
                  "the earlier lessons, the argument concerns the case as reported."),
            ("p", "Then the distinction the lesson is named for. The chapter first restates a "
                  "celebrated distinction it does not name, between languages, the constituted "
                  "systems of vocabulary and syntax, and the acts of speech they are the residue "
                  "of. Or again, it says, one might draw &ldquo;a distinction between a "
                  "speaking word and a spoken word&rdquo;. In the speaking word a significant "
                  "intention is coming into being, aiming at something no natural object "
                  "defines: &ldquo;Speech is the surplus of our existence over natural "
                  "being.&rdquo; But the act of expression builds a linguistic and cultural world "
                  "and lets what was reaching beyond fall back into being; hence the spoken word, "
                  "which enjoys available meanings as one enjoys a fortune already made, and "
                  "from which the writer's and the philosopher's new acts of expression become "
                  "possible."),
            ("p", "Part One ends here. The body, the chapter says, is not where it is nor what "
                  "it is: it secretes a meaning that comes from nowhere and projects it on its "
                  "surroundings. &ldquo;It is the body which points out, and which speaks&rdquo;, "
                  "and Cézanne's remark that the little blue and brown touches make a sitter "
                  "gaze as he gazes is its example. The Cartesian tradition allows two senses of "
                  "existing, as a thing or as a consciousness; the experience of one's own body "
                  "is a third, ambiguous one. Descartes himself, in a letter of 1643 to Princess "
                  "Elisabeth of Bohemia, distinguished the body known through living from the "
                  "body known by the understanding, and kept the first subordinate to the "
                  "second, the chapter says, because God stood behind our situation as its "
                  "rational author."),
            ("p", "The chapter's last sentence says the obscurity spreads to the whole perceived "
                  "world. That is where the book goes next. The next course, Sensing and Space, "
                  "begins Part Two, The World as Perceived, with its introduction, The Theory of "
                  "the Body is already a Theory of Perception."),
        ],
        "lab": ("phenkit", {
            "mode": "variation",
            "view": "core",
            "preset": "anger",
            "presets": [
                {"id": "anger",
                 "label": "Three expressions of anger, coded with the signs p. 219 names",
                 "variants": "the angry Japanese, yes, smiles; "
                             "the Westerner who goes red, yes, goes-red stamps; "
                             "the Westerner who goes pale, yes, goes-pale hisses",
                 "expect": {"vrCore": "none", "vrVary": "smiles, goes-red, stamps, goes-pale, hisses", "vrBreak": "no variant is marked no"}},
                {"id": "west",
                 "label": "The two Western expressions only (p. 219)",
                 "variants": "the Westerner who goes red, yes, goes-red stamps; "
                             "the Westerner who goes pale, yes, goes-pale hisses",
                 "expect": {"vrCore": "none", "vrVary": "goes-red, stamps, goes-pale, hisses"}},
                {"id": "smile",
                 "label": "A smile in anger, and a smile in pleasure (the lesson's addition) marked not anger",
                 "variants": "smile in anger, yes, smile; smile in pleasure, no, smile",
                 "expect": {"vrCore": "smile", "vrVary": "none", "vrBreak": "smile in pleasure lacks none of the core"}},
            ],
            "panel_title": "Looking for the natural sign of anger",
            "panel_intro": (
                "This lab counts the lesson's coding: each expression's bodily signs, and "
                "whether it is anger, are the lesson's reading of one sentence. The lab prints "
                "the sign every expression of anger has, if any, what varies, and what an "
                "expression marked not anger lacks. Compare the anger and smile presets."
            ),
        }),
        "steps_title": "Looking for a natural sign",
        "steps_intro": "Four steps; the last says what an empty core means.",
        "steps": [
            ("Code each expression",
             "List the bodily signs each expression of the emotion shows, as the text names "
             "them, and mark whether it is an expression of that emotion."),
            ("Intersect",
             "Keep the signs every expression marked yes shows. If the classical division were "
             "right, the natural sign of the emotion would be here."),
            ("Check the expressions marked no",
             "For each, name the core signs it lacks. If it lacks none, the signs do not by "
             "themselves decide the emotion."),
            ("Read the result, and no further",
             "An empty core says no bodily sign is shared across the coded expressions. It "
             "does not say the gestures are meaningless: the chapter holds that anger is read "
             "in each of them."),
        ],
        "worked": {
            "title": "Three expressions of anger",
            "intro": [
                "Take the anger preset: the angry Japanese who smiles, the Westerner who goes "
                "red and stamps, and the Westerner who goes pale and hisses, each marked as "
                "anger. You want the sign all three share.",
            ],
            "lines": [
                "smiles:  only the Japanese, so it varies",
                "goes red, stamps:  only the first Westerner",
                "goes pale, hisses:  only the second Westerner",
                "a sign in all three?  none",
                "core:  empty",
            ],
            "after": [
                "No bodily sign is in all three, so on this coding anger has no natural sign. "
                "That is what the chapter's sentence says, and what it adds goes beyond the "
                "count: the difference of behaviour is a difference in the emotions themselves.",
            ],
        },
        "quiz_title": "Gesture, sign and speech",
        "quiz": [
            {"q": "Three expressions of grief are coded as grief: tears and a bowed head, tears "
                  "and silence, tears and wailing. What is the core?",
             "a": ["tears, bowed-head", "none", "bowed-head, silence, wailing", "tears"],
             "c": 3,
             "why": "Tears are in all three. The bowed head, the silence and the wailing are each "
                    "in one only, so they vary, and the core is not empty because one sign is "
                    "shared. A shared sign in three coded variants would still not show that it "
                    "is grief's natural sign."},
            {"q": "Which statement is the chapter's own?",
             "a": ["It is no more natural, and no less conventional, to shout in anger than to "
                   "call a table a table",
                   "Gestures are natural signs and words are conventional signs",
                   "Words imitate the things they name, as onomatopoeia shows",
                   "All signs are arbitrary conventions that could be changed by agreement"],
             "c": 0,
             "why": "The chapter writes that sentence on p. 220. The division into natural and "
                    "conventional signs is the view it says is commonly held and rejects; it "
                    "calls the onomatopoeic theory naive; and it says conventions are a late form "
                    "that presupposes an earlier communication, and that everything in man is "
                    "natural as well as made."},
            {"q": "What distinguishes the speaking word from the spoken word?",
             "a": ["The speaking word is said aloud; the spoken word is written down",
                   "In the speaking word a meaning is coming into being; the spoken word uses "
                   "meanings already acquired",
                   "The speaking word is the speaker's; the spoken word is the listener's",
                   "The speaking word is the thought before it is put into words"],
             "c": 1,
             "why": "The chapter defines the speaking word as the one in which the significant "
                    "intention is coming into being, and the spoken word as enjoying available "
                    "significances like an acquired fortune. Neither is defined by voice or "
                    "writing, or by speaker and listener, and the chapter denies there is a "
                    "thought before its expression."},
            {"q": "What, according to the chapter, sets speech apart from the other ways of "
                  "expressing?",
             "a": ["It alone can be written down",
                   "It alone is conventional, while gestures are natural",
                   "It alone settles into a sediment and an acquisition, and can be about "
                   "itself",
                   "It alone has a meaning"],
             "c": 2,
             "why": "The text says that alone of all expressive processes speech settles into a "
                    "sediment and constitutes an acquisition, and that one can speak about speech "
                    "but not paint about painting. It says music can be written down too, it "
                    "denies the natural-conventional division, and it holds that gestures have "
                    "meaning as well."},
        ],
        "mistakes": [
            ("Dividing signs into natural gestures and conventional words",
             "The classical division: emotional gestures are natural signs, the same in every "
             "body, and words are conventional; so speech cannot be gesture. The chapter "
             "grants that a word's conceptual meaning looks arbitrary, and places that "
             "arbitrariness: it belongs to the meaning taken apart from the word's gestural "
             "sense. And it denies the other half, since in man there is no natural sign. The "
             "<code>anger</code> preset's empty core is the passage's case in the lab's "
             "terms: no bodily sign is shared by the three expressions of anger it names."),
            ("Hearing invented like words as arbitrary at will",
             "Feelings and passional conduct are invented like words, the chapter says, but "
             "it does not say anyone could change them by deciding to. Everything in man is "
             "both manufactured and natural: every word and every form of behaviour owes "
             "something to biological being, and none reduces to it. The language one lives "
             "in cannot simply be exchanged for another either."),
            ("Taking the empty core to show that gestures have no meaning",
             "The empty core shows only that no single bodily sign is common to the coded "
             "expressions. The chapter's claim is the reverse of meaninglessness: anger is "
             "read in the gesture, which is anger itself, and the difference between the "
             "Japanese smile and the Western flush is a difference in the angers, not in the "
             "signs of one anger."),
        ],
        "standard": (
            "Finish when you can look for a natural sign in a set of expressions and say what "
            "the chapter makes of the result.",
            "Given a coded set of expressions of one emotion, compute the common sign, if any, "
            "and what an expression marked not of the emotion lacks; state the classical "
            "division of natural and conventional signs and the chapter's reply to each half; "
            "and distinguish the speaking word from the spoken word."
        ),
        "note": (
            "The anger and west presets code one sentence of the book, and the pleased smile is "
            "the lesson's addition. An empty core is a fact about the lesson's coding of three "
            "expressions, not a survey of how people express anger, and a shared sign would not "
            "by itself make it natural. The lab cannot reach the chapter's further claim, that "
            "the difference of behaviour is a difference in the emotions themselves."
        ),
    },
]
