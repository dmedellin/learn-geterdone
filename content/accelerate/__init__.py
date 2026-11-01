"""The Accelerate path, as data: a read-along of Nicole Forsgren, Jez Humble
and Gene Kim's Accelerate: The Science of Lean Software and DevOps (IT
Revolution, 2018).

Eight courses that follow the book's three parts, sixteen chapters,
conclusion and appendices, one lesson per section or group of sections. Each
lesson sets out what the research found and how it was measured, and
recomputes one kind of figure the researchers computed on a small sample
written for the lesson. The content lives here and only here; scripts/ turns
it into pages. The design is docs/accelerate/PLAN.md.
"""

from . import (
    c1_measuring_performance,
    c2_culture,
    c3_technical_practices,
    c4_lean_management,
    c5_people,
    c6_the_science,
    c7_surveys_and_data,
    c8_transformation,
)

# A course module still being authored exports COURSE = None. It is filtered
# here rather than left out of the import list, so an unfinished course is
# visible in the source and cannot be forgotten.
COURSES = [c for c in [
    c1_measuring_performance.COURSE,
    c2_culture.COURSE,
    c3_technical_practices.COURSE,
    c4_lean_management.COURSE,
    c5_people.COURSE,
    c6_the_science.COURSE,
    c7_surveys_and_data.COURSE,
    c8_transformation.COURSE,
] if c is not None]

for _index, _course in enumerate(COURSES, start=1):
    _course["number"] = _index

# Course 1's author completes this from docs/accelerate/PLAN.md section A,
# field for field as content/domain_driven_design/__init__.py.
PATH = {
    "slug": "accelerate",
    "title": "Accelerate, Read Along",
    "level": "Introductory",
    "level_note": "you have worked on, with or near a team that builds and runs software",
    # Backtick runs, key lines and worked lines are read by the code dialect
    # (speech.say_code), as on the other software read-alongs.
    "speech": "code",
    "tagline": (
        "Forsgren, Humble and Kim&rsquo;s <em>Accelerate</em>, read chapter by chapter, with each finding recomputed on a small sample: delivery measures from a log, groups of teams by cluster analysis, culture scores and their reliability, a correlation and why it is not a cause. Eight courses and 46 lessons are available."
    ),
    "description": (
        "The Accelerate Subject: a read-along of Nicole Forsgren, Jez Humble and Gene Kim&rsquo;s 2018 book in its own order, from the Preface and the case for capabilities over maturity, through the four measures of software delivery performance and the practices, architecture, management and people that the research links to them, to the second part on the science and the survey method and the third on a transformation. Each lesson sets out what the researchers found and how they measured it, and recomputes one kind of figure on a small sample written for the lesson &mdash; a lead time from a log, the groups a clustering finds, a construct&rsquo;s score and reliability, a correlation &mdash; and ends with a sample to work by hand. All eight courses and 46 lessons are available."
    ),
    "key": [
        "capabilities, not a maturity level",
        "four measures of delivery performance",
        "a survey finding is of its sample",
        "a score is a mean of several items",
        "a correlation is not a cause",
        "a figure shows a sample, not your team",
    ],
    "sequence_intro": (
        "Each course assumes the ones before it and nothing else, and the order is the book&rsquo;s. The first course&rsquo;s four measures of delivery performance are the outcomes every later chapter reports against, and the course on culture gives the scales that the chapters on people and the science of the book use again."
    ),
    "why_order": [
        "The order is the book&rsquo;s, and it runs from the outcome to its drivers. Accelerate and Measuring Performance sets out what the authors measure and why: capabilities rather than maturity, and four measures of delivery that reward a team-level outcome. Measuring and Changing Culture, Technical Practices and Architecture, Security, Lean Management and Product Development, and Sustainable Work, Satisfaction and Leadership are Part I&rsquo;s findings: the capabilities and practices that predict those measures, and the people they affect.",
        "The measures come first because every later finding is stated against them. A practice is said to predict lead time, deployment frequency, time to restore or change fail rate, and a reader who has not met the four, and the groups of high, medium and low performers drawn from them, cannot weigh the claim.",
        "Part II comes after the findings because it explains how they were reached. The Science Behind the Book and Surveys, Data and Statistical Methods read the book&rsquo;s own account of its method, constructs, reliability, sampling and the kinds of analysis, and a reader who has seen a dozen findings is ready to ask how they were established. Transformation, the last course, reads Part III, a chapter by Steve Bell and Karen Whitley Bell on a large organization&rsquo;s change, with the book&rsquo;s conclusion and appendices.",
        "The courses can be read separately once the first is read. The two courses on method assume the first and enough of the second to know what a construct is; the last assumes the first and the third.",
    ],
    "prerequisites": [
        "You have worked on, with or near a team that builds and runs software. Every lesson is about measuring what such a team does, and it lands best on a reader who has shipped a change, waited for a release or been paged.",
        "No programming and no earlier statistics. The arithmetic is counting, sums, shares and, in the later courses, a mean, a correlation and a square root, and the labs do it and show each step.",
        "No other Subject. <em>System Design</em> and <em>Operations Research</em> teach the queueing the book touches in two chapters, and the lessons name the one lesson there where it is taught once.",
        "A copy of the book is strongly recommended. The book is in copyright, so a lesson states each chapter&rsquo;s findings in its own words, points to the chapter and section by name, and quotes at most a sentence or two. The book&rsquo;s tables, figures and survey items are described and never reproduced; the samples in the lessons are written for them.",
        "Some team of your own, or one you know. Every lesson&rsquo;s last step sends you to a team you work with, with a figure to compute.",
    ],
    # Each path names its own hazard. This one's is that a figure computed from
    # a lesson's small sample is not a finding, and a correlation in it is not
    # a cause (PLAN section A).
    "material": (
        "every figure on this path is computed in your browser from the small sample a lesson states &mdash; its log, its answers, its teams &mdash; and shows what one measure says about that sample; it is not a finding about any team or organization, and a correlation in it is not a cause."
    ),
    "footer_lead": (
        "<strong>Educational course material.</strong> Every figure on this path is computed in your browser from what the lesson states: a lead time is a difference between two times in the log it lists, a score is the mean of the answers it gives, a correlation is computed from the pairs it names. The samples are written for this course and none is taken from the book; nothing you type is sent anywhere. What the labs cannot do is show what causes what &mdash; the book argues that from theory and from years of survey data, with limits it states itself, and so must you."
    ),
    "courses": COURSES,
}
