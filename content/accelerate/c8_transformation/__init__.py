"""Course 8 -- Transformation: Chapter 16, the Conclusion and Appendices A and B.

Five lessons in one part_a. Chapter 16, High-Performance Leadership and
Management, is by Steve Bell and Karen Whitley Bell, guests in Part III, and
the lessons credit it to them; the Conclusion and the two appendices are the
book's own authors'. References are to Nicole Forsgren, Jez Humble and Gene
Kim, Accelerate: The Science of Lean Software and DevOps (IT Revolution,
2018), by chapter and section; PDF pages of the operator's copy appear only in
source comments. The design is docs/accelerate/PLAN.md, section C, Course 8.
"""

from . import part_a

COURSE = {
    "slug": "accelerate-transformation",
    "title": "Transformation",
    "level": "Introductory",
    "summary": (
        "Part III and the end matter of the book: Chapter 16, High-Performance "
        "Leadership and Management, which Steve Bell and Karen Whitley Bell "
        "wrote about their visits to ING Netherlands; the Conclusion; and "
        "Appendices A and B, the list of 24 capabilities and the book's "
        "statistical findings by category. Each lesson sets out what the "
        "section says, whose account it is, and where the book itself marks its "
        "limits, and then computes one figure on a small sample written for the "
        "lesson: the lead time of a squad's board with and without a limit on "
        "work in process, a team's current condition and targets on the four "
        "delivery measures, the capabilities a team added in a quarter, what "
        "&lsquo;twice as likely&rsquo; compares, and a category profile of "
        "six teams."
    ),
    "blurb": (
        "Read the book's last chapter and its end matter. Compute what a limit "
        "does to a board's lead time, state a team's condition and see which "
        "targets the next fortnight met, count the capabilities a team added in "
        "a quarter, compare two groups the way the book's &lsquo;twice as "
        "likely&rsquo; does, and find the thinnest category across an "
        "organization&rsquo;s teams."
    ),
    "key": [
        "a framework links strategy to action",
        "problems travel; learning travels back",
        "you cannot implement a culture",
        "you cannot buy or copy high performance",
        "24 capabilities, five categories",
        "a figure belongs to its year and sample",
    ],
    "assumes_short": "Accelerate and Measuring Performance",
    "assumes_long": (
        "Accelerate and Measuring Performance, for the four delivery measures "
        "that Chapter 2 introduces and that the second lesson uses; Security, "
        "Lean Management and Product Development helps with the practices "
        "Chapter 16 shows in use, and Measuring and Changing Culture with the "
        "generative culture it hopes to grow"
    ),
    "outcomes_intro": (
        "By the end you can make, on a small sample written down in front of you, "
        "the computations these sections lean on, and say in the authors' terms "
        "what each shows and what it leaves to judgement."
    ),
    "outcomes": [
        ("Read a board",
         "Compute a squad's average work in process, throughput and lead time from "
         "a log of items, and say what is assumed when a limit is set."),
        ("State a condition and a target",
         "Give a team's deployments, median lead time, change fail rate and "
         "median time to restore for a period, and say from the next period's "
         "log which targets were met."),
        ("Profile a team by capability",
         "Count a team's capabilities in the five categories on two dates, and "
         "say what the count does not show about routines or culture."),
        ("Compare two groups",
         "Compute shares, their ratio, the gap and the odds ratio for two groups, "
         "and say what &lsquo;twice as likely&rsquo; does not claim."),
        ("Use the appendices",
         "Find a capability's chapter in Appendix A, read an Appendix B line by "
         "its verb, and profile an organization&rsquo;s teams by category."),
    ],
    "syllabus_intro": (
        "Five lessons in the book's order. The first three read Chapter 16: the "
        "management framework, the stand-up and catchball rhythm, and the "
        "transformation of leaders&rsquo; and teams&rsquo; practices. The fourth "
        "reads the Conclusion, and the fifth Appendices A and B."
    ),
    "how_to": [
        "Read the section before the lesson. This is a read-along of Nicole "
        "Forsgren, Jez Humble and Gene Kim, <em>Accelerate: The Science of Lean "
        "Software and DevOps</em> (IT Revolution, 2018), with samples and data "
        "written for these lessons. Chapter 16 is by Steve Bell and Karen "
        "Whitley Bell, and its lessons say so. Each lesson names its chapter and "
        "sections, opens with at most one short quotation, and sets out the "
        "argument in its own words.",
        "Read Chapter 16 as a case. It is the Bells&rsquo; account of what they "
        "saw at ING Netherlands, told by coaches and not reported as survey "
        "research; the Conclusion and the appendices are the research&rsquo;s "
        "summary. A lesson says which it is reading, and where the book marks "
        "its own limits it says so too.",
        "Treat each figure as a reason to look. The labs compute one number on "
        "the small sample a lesson states: a lead time, a fail rate, a count of "
        "capabilities, a ratio of shares. It shows what one measure says about "
        "that sample. The book&rsquo;s findings are its survey&rsquo;s, of its "
        "sample, in its years, and a figure here is never a finding about a "
        "team or an organization.",
        "Bring your own log. Every lesson ends by sending you to a board, a "
        "log, a team or a pair of groups you know, and the labs take whatever "
        "records you type. Nothing you type leaves your browser.",
    ],
    "not_covered": [
        "The Bells&rsquo; figures and tables: the leadership Obeya, ING&rsquo;s "
        "organizational model, the stand-up and catchball rhythm and the table of "
        "behaviors and practices. They are better read in the book, and the "
        "lessons describe them in prose only.",
        "The book&rsquo;s own tables and figures in the appendices, such as the "
        "manual-work percentages and the firmographics, and the wording of the "
        "capabilities. The lab names the 24 capabilities with short labels of its "
        "own.",
        "Appendix C, the statistical methods, which is read in Surveys, Data and "
        "Statistical Methods.",
        "Whether any of it works in your organization. The labs compute on "
        "invented samples and cannot test a practice; the exercises send you to "
        "your own log for that.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the small "
        "sample a lesson states: lead time from the days items started and "
        "finished, the four delivery measures from a log of changes and "
        "incidents, capabilities from the lists a team gives, and shares and "
        "ratios from the counts of each group. The samples are written for these "
        "lessons, and none is taken from the book or from ING. A figure shows "
        "what one measure says about that sample; it is not a finding about any "
        "team or organization, and a correlation in it is not a cause."
    ),
    "lessons": part_a.LESSONS,
}
