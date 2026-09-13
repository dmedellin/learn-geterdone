"""Turn the content data into the published pages.

Three page kinds, one renderer each. Every convention the library pins lives in
chrome.py or theme.py, so a page produced here cannot ship a variant of the
pager, the palette or the theme toggle even if a lesson wanted one.
"""

import html
import json
import re

from . import chrome, feedback, labs, progress
from .chrome import esc

ORIGIN = chrome.CANONICAL_ORIGIN

# Authoring shorthand. In any prose field, `x` becomes a monospace math run.
# Notation is dense in this subject -- a paragraph can carry six short
# expressions -- and writing the span by hand six times makes the source
# unreadable, which is how content drifts. This is the ONLY markup the content
# files may use; everything structural is a block kind below.
_MATH_RE = re.compile(r"`([^`]+)`")


def inline(text):
    return _MATH_RE.sub(lambda m: '<span class="math">%s</span>' % m.group(1), text)


_TAG_RE = re.compile(r"<[^>]+>")


def plain(text):
    """Authored prose as PLAIN TEXT, for metadata.

    A <meta description> is not markup: whatever goes in is shown verbatim by a
    search engine or a link preview. The prose fields are written for the page,
    so they carry `x` math runs and HTML entities, and handing them straight to
    an attribute that is then escaped shipped descriptions reading
    "which is inclusive &mdash; and the one English does not have a word for",
    backticks and all. Tags come out, entities are resolved to the characters
    they name, and the shorthand marks are dropped.
    """
    return html.unescape(_TAG_RE.sub("", text)).replace("`", "")


def esc_inline(text):
    """Escape the text, THEN apply the backtick shorthand.

    Headings are not prose: they must not carry arbitrary HTML, so they are
    escaped. But an author writing a heading about a symbol reaches for the same
    `x` shorthand they use everywhere else, and escaping alone printed the
    backticks -- "Reading `or` as exclusive" shipped with the marks visible on
    roughly a hundred and ninety headings across the mathematics path.

    Escaping first is what makes this safe rather than a hole: `a > b` becomes
    `a &gt; b` and only then is wrapped in the math span, so a heading still
    cannot introduce a tag. Fields that also feed metadata -- a lesson's title
    reaches <title> and og:title -- keep plain esc(), because a span in a
    <title> element is not markup, it is six visible characters.
    """
    return inline(esc(text))


def _mathblock(lines):
    return '<div class="mathblock">%s</div>' % "\n".join(esc(line) for line in lines)


def _block(kind, payload):
    """One authored body block -> markup.

    The kinds are deliberately few. A lesson that needs a fifth kind of box is
    usually a lesson that should be two lessons.
    """
    if kind == "p":
        return "<p>%s</p>" % inline(payload)
    if kind == "h3":
        return "<h3>%s</h3>" % esc_inline(payload)
    if kind == "math":
        return _mathblock(payload)
    if kind == "ul":
        return "<ul>%s</ul>" % "".join("<li>%s</li>" % inline(item) for item in payload)
    if kind == "ol":
        return "<ol>%s</ol>" % "".join("<li>%s</li>" % inline(item) for item in payload)
    if kind in ("def", "thm", "example"):
        label = {"def": "Definition", "thm": "Theorem", "example": "Example"}[kind]
        css = {"def": "defbox", "thm": "thm", "example": "example"}[kind]
        title, paragraphs = payload[0], payload[1:]
        body = "".join("<p>%s</p>" % inline(p) for p in paragraphs)
        return '<div class="%s"><span class="label">%s &middot; %s</span>%s</div>' % (
            css, label, esc_inline(title), body,
        )
    if kind == "proof":
        body = "".join("<p>%s</p>" % inline(p) for p in payload)
        return '<div class="proof">%s<p><span class="qed">&#9633;</span></p></div>' % body
    raise KeyError("unknown body block %r" % kind)


def lesson_page(*, path, course, lesson, index, prev_lesson, next_lesson):
    """One lesson: /<course-slug>/<lesson-slug>/ ."""
    number = "%02d" % (index + 1)
    total = len(course["lessons"])
    url = "/%s/%s/" % (course["slug"], lesson["slug"])

    lab = labs.build(lesson["lab"][0], lesson["lab"][1])

    parts = [
        chrome.head(
            title="%s | Lesson | %s | %s | Learn · geterdone.io" % (lesson["title"], course["title"], path["title"]),
            description=plain(lesson["summary"]),
            canonical_path=url,
            favicon=chrome.FAVICON_LESSON, page_kind="lesson",
        ),
        chrome.topbar(up="../../"),
        chrome.crumbs([
            ("Learn library", "../../"),
            (path["title"], "../../paths/%s/" % path["slug"]),
            (course["title"], "../"),
            (lesson["title"], None),
        ]),
        chrome.noscript(
            "<strong>JavaScript is required for the interactive lesson.</strong> "
            "The %s is computed in your browser, so it stays blank while scripting "
            "is off. Everything written &mdash; the definitions, the worked example, "
            "the common mistakes and the understanding check &mdash; reads normally."
            % lab.title.lower()
        ),
        '\n    <main id="main">\n',
    ]

    # -- hero ---------------------------------------------------------------
    parts.append(
        '    <section class="hero" data-ui="hero">\n'
        "      <div>\n"
        '        <span class="eyebrow"><span class="pulse" aria-hidden="true"></span>'
        '<span data-ui="page-kind">Lesson</span> &middot; %s &middot; %s</span>\n'
        "        <h1>%s</h1>\n"
        "        <p>%s</p>\n"
        '        <div class="hero-actions" data-ui="primary-actions">'
        '<a class="btn primary" href="#lab">Open the interactive lesson</a>'
        '<a class="btn ghost" href="#practice">Practice</a></div>\n'
        "      </div>\n"
        '      <div class="hero-visual">\n'
        "        %s\n"
        '        <div class="float-label" style="right:16px;bottom:16px;">%s</div>\n'
        "      </div>\n"
        "    </section>\n"
        % (
            esc(course["title"]), esc(lesson["module"]),
            esc(lesson["title"]), inline(lesson["summary"]),
            _mathblock(lesson["key"]),
            esc_inline(lesson.get("key_label", "The statement in symbols")),
        )
    )

    # -- concepts -----------------------------------------------------------
    cards = "".join(
        '<article class="card concept-card"><div class="icon">%d</div><h3>%s</h3><p>%s</p></article>'
        % (i + 1, esc_inline(t), inline(body))
        for i, (t, body) in enumerate(lesson["concepts"])
    )
    parts.append(
        '    <section class="section">\n'
        '      <div class="section-head"><div><p class="kicker">Core ideas</p>'
        "<h2>What this lesson establishes</h2></div><p>%s</p></div>\n"
        '      <div class="grid-3">%s</div>\n'
        "    </section>\n" % (inline(lesson.get("concepts_intro", "Three ideas carry the rest.")), cards)
    )

    # -- the written material ----------------------------------------------
    body_markup = "".join(_block(kind, payload) for kind, payload in lesson["body"])
    parts.append(
        '    <section class="section" id="read">\n'
        '      <div class="section-head"><div><p class="kicker">The material</p>'
        "<h2>%s</h2></div><p>%s</p></div>\n"
        '      <article class="card card-pad prose">%s</article>\n'
        "    </section>\n"
        % (
            esc_inline(lesson.get("read_title", lesson["title"])),
            inline(lesson.get("read_intro", "Definitions first, then what follows from them.")),
            body_markup,
        )
    )

    # -- the lab ------------------------------------------------------------
    legend = ""
    parts.append(
        '    <section class="section" id="lab">\n'
        '      <div class="section-head"><div><p class="kicker">Interactive</p>'
        "<h2>%s</h2></div><p>%s</p></div>\n"
        '      <div class="lab-layout">\n'
        '        <article class="card lab-main">\n%s\n        </article>\n'
        '        <aside class="card side-panel" aria-live="polite">\n'
        "          <h3>%s</h3>\n          <p>%s</p>\n%s\n        </aside>\n"
        "      </div>\n"
        "    </section>\n"
        % (
            esc(lab.title),
            esc(lab.subtitle),
            lab.markup,
            esc_inline(lab.panel_title),
            inline(lab.panel_intro),
            lab.controls,
        )
    )

    # -- how to use it ------------------------------------------------------
    steps = "".join(
        '<article class="card concept-card"><div class="icon">%d</div><h3>%s</h3><p>%s</p></article>'
        % (i + 1, esc_inline(t), inline(body))
        for i, (t, body) in enumerate(lesson["steps"])
    )
    parts.append(
        '    <section class="section" id="process">\n'
        '      <div class="section-head"><div><p class="kicker">Method</p>'
        "<h2>%s</h2></div><p>%s</p></div>\n"
        '      <div class="grid-4">%s</div>\n'
        "    </section>\n"
        % (
            esc_inline(lesson.get("steps_title", "How to work with this")),
            inline(lesson.get("steps_intro", "The order matters more than the speed.")),
            steps,
        )
    )

    # -- practice + worked example -----------------------------------------
    worked = lesson["worked"]
    parts.append(
        '    <section class="section" id="practice">\n'
        '      <div class="grid-2">\n%s\n'
        '      <article class="card card-pad prose"><h3>%s</h3>%s%s</article>\n'
        "      </div>\n"
        "    </section>\n"
        % (
            labs.QUIZ_MARKUP.format(title=esc_inline(lesson.get("quiz_title", "Check yourself"))),
            esc_inline(worked["title"]),
            "".join("<p>%s</p>" % inline(p) for p in worked.get("intro", [])),
            _mathblock(worked["lines"])
            + "".join("<p>%s</p>" % inline(p) for p in worked.get("after", [])),
        )
    )

    # -- mistakes + completion ---------------------------------------------
    mistakes = "".join(
        '<div class="lesson-row"><div class="num">%d</div><div><strong>%s</strong><span>%s</span></div></div>'
        % (i + 1, esc_inline(t), inline(body))
        for i, (t, body) in enumerate(lesson["mistakes"])
    )
    standard_head, standard_body = lesson["standard"]
    parts.append(
        '    <section class="section">\n'
        '      <div class="grid-2">\n'
        '        <article class="card card-pad"><h3 style="margin-top:0;">Common mistakes</h3>'
        '<div class="lesson-list">%s</div></article>\n'
        '        <article class="card card-pad"><h3 style="margin-top:0;">Check your understanding</h3>'
        '<div class="callout"><div class="mark">&#10003;</div><div><strong>%s</strong><p>%s</p></div></div>'
        '<div class="note" style="margin-top:12px;"><strong>Note:</strong> %s</div></article>\n'
        "      </div>\n"
        "    </section>\n"
        % (mistakes, esc_inline(standard_head), inline(standard_body), inline(lesson["note"]))
    )

    parts.append("    </main>\n")

    # -- the pager, in the library's pinned form ----------------------------
    prev = None
    if prev_lesson is not None:
        prev = (
            "../%s/" % prev_lesson["slug"],
            esc(prev_lesson["title"]),
        )
    if next_lesson is not None:
        nxt = (
            "../%s/" % next_lesson["slug"],
            esc(next_lesson["title"]),
            False,
        )
    else:
        nxt = ("../", esc(course["title"]), True)
    # The completion mark sits between the material and the pager: the moment a
    # reader has finished. localStorage only, no request, never a gate.
    lesson_id = "%s/%s" % (course["slug"], lesson["slug"])
    parts.append(progress.LESSON_MARKUP % "../..")
    parts.append(chrome.pager(prev=prev, next=nxt))
    # Recommendations for this lesson: what should CHANGE about it, as opposed
    # to the completion mark above, which says the reader has finished it.
    parts.append(feedback.MARKUP % {
        "id": esc(lesson_id),
        "lesson": esc(plain(lesson["title"])),
        "course": esc(plain(course["title"])),
    })

    parts.append(
        chrome.footer(
            "<strong>%s.</strong> %s"
            % (esc(course["title"]), inline(course["footer_lead"])),
            path["material"],
        )
    )
    quiz = [
        {
            "q": inline(item["q"]),
            "a": [inline(choice) for choice in item["a"]],
            "c": item["c"],
            "why": inline(item["why"]),
        }
        for item in lesson["quiz"]
    ]
    parts.append(chrome.close(labs.cfg_literal("QUIZ", quiz)
                             + "\n  (function () {\n" + lab.script + "  })();\n"
                             + labs.QUIZ_SCRIPT
                             + progress.PROGRESS_JS
                             + progress.LESSON_JS % json.dumps(lesson_id)
                             + feedback.STORE_JS
                             + feedback.LESSON_JS))
    return chrome.name_horizontal_scrollers("".join(parts))


def course_home(*, course, index, courses, path):
    """One course home: /<course-slug>/ ."""
    total_courses = len(courses)
    url = "/%s/" % course["slug"]
    lessons = course["lessons"]

    syllabus = "".join(
        '<a class="syllabus-item" href="./%s/" data-lesson="%s/%s"><div class="num" aria-hidden="true"></div>'
        '<div><strong>%s</strong><span>%s</span><span class="lesson-state">Not marked</span></div></a>'
        % (lesson["slug"], course["slug"], lesson["slug"],
           esc(lesson["title"]), esc_inline(lesson["one_line"]))
        for i, lesson in enumerate(lessons)
    )
    outcomes = "".join(
        '<article class="card concept-card"><div class="icon">%d</div><h3>%s</h3><p>%s</p></article>'
        % (i + 1, esc_inline(t), inline(body))
        for i, (t, body) in enumerate(course["outcomes"])
    )

    nav = []
    if index > 0:
        before = courses[index - 1]
        nav.append(
            '        <a class="path-move prev" href="../%s/" rel="prev">'
            "<span>Related course</span><strong>%s</strong></a>"
            % (before["slug"], esc(before["title"]))
        )
    if index < total_courses - 1:
        after = courses[index + 1]
        nav.append(
            '        <a class="path-move next" href="../%s/" rel="next">'
            "<span>Related course</span><strong>%s</strong></a>"
            % (after["slug"], esc(after["title"]))
        )
    else:
        nav.append(
            '        <a class="path-move next" href="../paths/%s/">'
            "<strong>All %s courses</strong></a>" % (path["slug"], esc(path["title"]))
        )

    parts = [
        chrome.head(
            title="%s | Course | %s | Learn · geterdone.io" % (course["title"], path["title"]),
            description=plain(course["summary"]),
            canonical_path=url,
            favicon=chrome.FAVICON_COURSE, page_kind="course",
        ),
        chrome.topbar(up="../"),
        chrome.crumbs([
            ("Learn library", "../"),
            (path["title"], "../paths/%s/" % path["slug"]),
            (course["title"], None),
        ]),
        '\n    <main id="main">\n',
        '    <section class="hero" data-ui="hero">\n'
        "      <div>\n"
        '        <span class="eyebrow"><span class="pulse" aria-hidden="true"></span>'
        '<span data-ui="page-kind">Course</span> &middot; %s</span>\n'
        "        <h1>%s</h1>\n"
        "        <p>%s</p>\n"
        '        <div class="hero-actions" data-ui="primary-actions">'
        '<a class="btn primary" href="#syllabus">View lessons</a>'
        '<a class="btn ghost" href="#background">Recommended background</a></div>\n'
        "      </div>\n"
        '      <div class="hero-visual">\n        %s\n'
        '        <div class="float-label" style="right:16px;bottom:16px;">What this course is about</div>\n'
        "      </div>\n"
        "    </section>\n"
        % (
            esc(path["title"]),
            esc(course["title"]), inline(course["blurb"]),
            _mathblock(course["key"]),
        ),
        '    <section class="section" data-ui="metadata">\n'
        '      <dl class="stats">\n'
        "        <div><dt>Subject</dt><dd>%s</dd></div>\n"
        "        <div><dt>Lessons</dt><dd>%d</dd></div>\n"
        "        <div><dt>Format</dt><dd>Interactive</dd></div>\n"
        "      </dl>\n"
        "    </section>\n" % (esc(path["title"]), len(lessons)),
        '    <section class="section" data-ui="overview">\n'
        '      <div class="section-head"><div><p class="kicker">Overview</p>'
        "<h2>What you will be able to do</h2></div><p>%s</p></div>\n"
        '      <div class="grid-4">%s</div>\n'
        "    </section>\n" % (inline(course["outcomes_intro"]), outcomes),
        '    <section class="section" id="syllabus" data-ui="lesson-list">\n'
        '      <div class="section-head"><div><p class="kicker">Lessons</p>'
        '<h2>%d lessons</h2>'
        '<p class="course-progress" id="courseProgress"></p></div><p>%s</p></div>\n'
        '      <div class="syllabus">%s</div>\n'
        "    </section>\n" % (len(lessons), inline(course["syllabus_intro"]), syllabus),
        '    <section class="section" id="background" data-ui="background">'
        '<h2>Recommended background</h2><p>%s.</p></section>\n' % esc(course["assumes_long"].capitalize().rstrip(".")),
        '    <section class="section">\n'
        '      <div class="grid-2">\n'
        '        <article class="card card-pad prose"><h3>Practice suggestions</h3>%s</article>\n'
        '        <article class="card card-pad prose"><h3>What it does not cover</h3>%s</article>\n'
        "      </div>\n"
        "    </section>\n"
        % (
            "".join("<p>%s</p>" % inline(p) for p in course["how_to"]),
            "".join("<p>%s</p>" % inline(p) for p in course["not_covered"]),
        ),
        "    </main>\n",
        '\n    <nav class="path-nav" data-ui="course-navigation" aria-label="Course navigation">\n%s\n      </nav>\n' % "\n".join(nav),
        chrome.footer(
            "<strong>%s.</strong> %s" % (esc(course["title"]), inline(course["footer_lead"])),
            path["material"],
        ),
        chrome.close(progress.PROGRESS_JS + progress.COURSE_JS),
    ]
    return chrome.name_horizontal_scrollers("".join(parts))


def path_page(path):
    """Subject catalog at the stable /paths/<slug>/ URL."""
    courses = path["courses"]
    total_lessons = sum(len(c["lessons"]) for c in courses)
    cards = "".join(
        '<a class="spine-item" href="../../%s/" data-course="%s" data-lessons="%d">'
        '<div class="spine-body"><strong>%s</strong><p>%s</p>'
        '<div class="spine-meta"><span>%d lessons</span><span>%s</span>'
        '<span class="spine-progress"></span></div></div></a>'
        % (c["slug"], c["slug"], len(c["lessons"]), esc(c["title"]),
           inline(c["blurb"]), len(c["lessons"]), esc(c["level"])) for c in courses)
    return chrome.name_horizontal_scrollers("".join([
        chrome.head(title="%s | Subject | Learn · geterdone.io" % path["title"],
                    description=plain(path["description"]),
                    canonical_path="/paths/%s/" % path["slug"], favicon=chrome.FAVICON_PATH, page_kind="subject"),
        chrome.topbar(up="../../"),
        chrome.crumbs([("Learn library", "../../"), (path["title"], None)]),
        '<main id="main">\n',
        '<section class="hero" data-ui="hero"><div>'
        '<span class="eyebrow"><span data-ui="page-kind">Subject</span> &middot; Learn library</span>'
        '<h1>%s</h1><p>%s</p>'
        '<div class="hero-actions" data-ui="primary-actions">'
        '<a class="btn primary" href="#courses">View courses</a>'
        '<a class="btn ghost" href="#background">Recommended background</a></div></div>'
        '<div class="hero-visual">%s</div></section>\n'
        % (esc(path["title"]), inline(path["tagline"]), _mathblock(path["key"])),
        '<section class="section" data-ui="metadata"><dl class="stats">'
        '<div><dt>Courses</dt><dd>%d</dd></div><div><dt>Lessons</dt><dd>%d</dd></div>'
        '<div><dt>Level</dt><dd>%s</dd></div></dl></section>\n'
        % (len(courses), total_lessons, esc(path["level"])),
        '<section class="section prose" data-ui="overview"><h2>Overview</h2>%s</section>\n'
        % "".join('<p>%s</p>' % inline(p) for p in path["why_order"]),
        '<section class="section" id="courses" data-ui="course-list">'
        '<div class="section-head"><div><h2>Courses</h2></div><p>%s</p></div>'
        '<div class="spine">%s</div></section>\n' % (inline(path["sequence_intro"]), cards),
        '<section class="section prose" id="background" data-ui="background">'
        '<h2>Recommended background</h2>%s</section>\n'
        % "".join('<p>%s</p>' % inline(p) for p in path["prerequisites"]),
        '</main>\n',
        chrome.footer(inline(path["footer_lead"]), path["material"]),
        chrome.close(progress.PROGRESS_JS + progress.PATH_JS),
    ]))
