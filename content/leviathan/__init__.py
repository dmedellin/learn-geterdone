"""The Leviathan path, as data: a read-along of Thomas Hobbes's Leviathan (1651).

Nine courses in Hobbes's order, from sense and speech through the natural
condition, the generation and offices of the commonwealth and the Christian
commonwealth to the kingdom of darkness and the Review and Conclusion, one
lesson per chapter or group of chapters. Each lesson quotes its passage from
the 1651 text and works one of its arguments as a problem the reader can check.
The content lives here and only here; scripts/ turns it into pages. The design
is docs/leviathan/PLAN.md.
"""

from . import (
    c1_sense_and_speech,
    c2_reason_and_passions,
    c3_power_and_religion,
    c4_natural_condition,
    c5_commonwealth,
    c6_dominion_and_liberty,
    c7_office_of_sovereign,
    c8_christian_commonwealth,
    c9_kingdom_of_darkness,
)

# A course module still being authored exports COURSE = None. It is filtered
# here rather than left out of the import list, so an unfinished course is
# visible in the source and cannot be forgotten.
COURSES = [c for c in [
    c1_sense_and_speech.COURSE,
    c2_reason_and_passions.COURSE,
    c3_power_and_religion.COURSE,
    c4_natural_condition.COURSE,
    c5_commonwealth.COURSE,
    c6_dominion_and_liberty.COURSE,
    c7_office_of_sovereign.COURSE,
    c8_christian_commonwealth.COURSE,
    c9_kingdom_of_darkness.COURSE,
] if c is not None]

for _index, _course in enumerate(COURSES, start=1):
    _course["number"] = _index

# Course 1's author completes this from docs/leviathan/PLAN.md section A,
# field for field as content/capital/__init__.py.
PATH = {
    "slug": "leviathan",
    "title": "Leviathan, Read Along",
    "level": "Introductory \u2192 Advanced",
    "level_note": "no philosophy or political theory is assumed",
    "tagline": (
        'Thomas Hobbes&rsquo;s <em>Leviathan</em>, read chapter by chapter from sense and speech to the commonwealth and the kingdom of darkness, with each argument worked as a problem you can check: validity, presumption, the meaning of names, what a covenant needs, what an assembly decides. Nine courses and 55 lessons are available.'
    ),
    "description": (
        "The Leviathan Subject: a read-along of all four Parts of Hobbes's book and its Review and Conclusion, in his order, nine courses with a lesson for every chapter or group of chapters. Each lesson reads a passage from the text of 1651 first, then explains it, then works one of its arguments as a problem you can check in your browser: an argument's counterexample row, a presumption updated on what has been seen, the verdict on an affirmation from its definitions, the covenant a man does better to keep, what an assembly's voices decide. All nine courses and 55 lessons are available."
    ),
    "key": ['reasoning = adding and subtracting names', 'A is B: every part of B is in A', 'will = the last appetite before the act', 'power: priced by the buyer, not fixed', 'covenant kept if expected sanction covers cost', 'law silent: the subject is free', 'dated by the latest event it mentions'],
    "sequence_intro": (
        "Each course assumes the ones before it and nothing else. Reason, Science and the Passions uses the reckoning with names of Sense, Imagination and Speech; Power, Manners and Religion uses the passions; The Natural Condition and the Laws of Nature uses power and worth; Persons and the Generation of a Commonwealth uses the covenants of the natural condition; Dominion, Liberty and the Parts of a Commonwealth uses the commonwealth made; the office of the sovereign course uses all of Part II; the two courses on the Christian commonwealth and the kingdom of darkness use the definitions and arguments of Part I and Part II throughout."
    ),
    "why_order": [
        "The order is Hobbes's, and it is the order of his argument. He builds the commonwealth the way a man builds anything, from the materials: first what a man is made of, then how men make a body from themselves, then what that body may do, then what Scripture says of it, and last the doctrines that, in his view, weaken it.",
        "Sense, imagination and speech come first because every later claim is built from them. Reason is a reckoning with names, so names come before reason; the passions are motions that begin in sense, so sense comes before the passions; and the laws of nature are theorems of reason, so reason comes before them.",
        "Part I is split by its own argument: the materials of the mind, then reason and the passions, then the social passions and religion, then the natural condition and its laws. Chapter 16, on persons, opens the course on the generation of a commonwealth because it is the hinge into Part II and Chapter 17 needs it.",
        "Parts III and IV come last because Hobbes means them as the application. A Christian commonwealth is the commonwealth of Part II read with Scripture, and the kingdom of darkness is what he calls the error that would unmake it; the Review and Conclusion then says what the whole book was for.",
    ],
    "prerequisites": [
        "No philosophy and no political theory. Hobbes defines his terms as he goes, and the Subject introduces the people and quarrels of his time, the Civil War, the exile in Paris, the schools, Bramhall, when his argument meets them.",
        "A willingness to read slowly. Hobbes writes long sentences, and the lessons read each passage once whole and then a phrase at a time. Each lab asks you to say what a figure is a figure of, and none needs more than counting and fractions.",
        "A copy of the book is welcome but not required. Every lesson quotes the passage it reads from the text of 1651, quoted from the operator&rsquo;s copy of Richard Tuck&rsquo;s revised student edition (Cambridge, 1996), which keeps Hobbes&rsquo;s spelling. Quotations are in that spelling, and the explanations around them are in modern spelling. The editor&rsquo;s introduction and notes are not used.",
        "Patience with a book that argues from definitions. Where a lesson computes what follows from a definition, it says so, and it says where Hobbes&rsquo;s critics would deny the definition.",
    ],
    "material": (
        "every figure on this path is computed in your browser from the names, payoffs and numbers a lesson states, and shows what follows from them on Hobbes&rsquo;s definitions; whether men are as Hobbes describes them, and whether his conclusions follow for any commonwealth, is what the book argues and the lab cannot settle."
    ),
    "footer_lead": (
        "<strong>Educational course material.</strong> Every figure on this path is computed in your browser from what the lesson states: a verdict on an affirmation is read from the definitions given, a presumption is updated on the observations listed, a covenant is kept or broken by its payoffs. Quotations are from Hobbes&rsquo;s text of 1651, in its original spelling. What the labs cannot do is tell you whether Hobbes&rsquo;s definitions are the right ones &mdash; and that is what the book is arguing about."
    ),
    "courses": COURSES,
}
