"""Turn the content data into the published pages.

Three page kinds, one renderer each. Every convention the library pins lives in
chrome.py or theme.py, so a page produced here cannot ship a variant of the
pager, the palette or the theme toggle even if a lesson wanted one.
"""

import contextvars
import functools
import html
import json
import re

from . import chrome, feedback, labs, progress, readout, speech, theme
from .chrome import esc

ORIGIN = chrome.CANONICAL_ORIGIN

# Authoring shorthand. In any prose field, `x` becomes a monospace math run.
# Notation is dense in this subject -- a paragraph can carry six short
# expressions -- and writing the span by hand six times makes the source
# unreadable, which is how content drifts. This is the ONLY markup the content
# files may use; everything structural is a block kind below.
_MATH_RE = re.compile(r"`([^`]+)`")


# What a voice says for each math run, for Listen (readout.py). Computed here,
# at build time, so the page needs no speech rules of its own.
_SPOKEN = speech.all_overrides()


# The read-out dialect of the page being rendered: None reads every run as
# mathematics (speech.say), "code" as program text (speech.say_code). It is the
# PATH dict's "speech" field, set for the length of one page by _dialect below,
# so the dozens of inline() calls a page makes need not each be handed it.
_DIALECT = contextvars.ContextVar("speech_dialect", default=None)


def _dialect(page):
    """Render `page(..., path=...)` with its Subject's read-out dialect."""
    @functools.wraps(page)
    def rendered(*args, **kwargs):
        path = kwargs["path"] if "path" in kwargs else args[0]
        token = _DIALECT.set(speech.dialect_of(path))
        try:
            return page(*args, **kwargs)
        finally:
            _DIALECT.reset(token)
    return rendered


def _say(run):
    return _say_in(run, _DIALECT.get())


@functools.lru_cache(maxsize=None)
def _say_in(run, dialect):
    if dialect == speech.CODE_DIALECT:
        return speech.say_code(run, override=_SPOKEN.get(run))
    return speech.say(run, override=_SPOKEN.get(run))


_BARE_MARKUP = re.compile(r"&(?!#?\w+;)|[<>]")


def _code_run(part):
    """A backtick run on a code-dialect Subject is program text: `List<String>`
    and `a && b` must show as written, not open a tag. A character reference
    the author wrote (`&lt;`, or one esc_inline already made) is kept as it is."""
    if _DIALECT.get() != speech.CODE_DIALECT:
        return part
    return _BARE_MARKUP.sub(lambda m: {"&": "&amp;", "<": "&lt;", ">": "&gt;"}[m.group()], part)


def _prose(segment):
    """Prose outside the `x` runs, with any math written into it unmarked
    (`compare |r| with 1`) given a spoken form; the visible text is unchanged."""
    out = []
    for piece in re.split(r"(<[^>]+>)", segment):
        if piece.startswith("<"):
            out.append(piece)
            continue
        at = 0
        for start, end in speech.islands(piece):
            out.append(piece[at:start])
            out.append('<span data-say="%s">%s</span>' % (esc(_say(piece[start:end])), piece[start:end]))
            at = end
        out.append(piece[at:])
    return "".join(out)


def inline(text):
    parts = _MATH_RE.split(text)
    return "".join(
        '<span class="math" data-say="%s">%s</span>' % (esc(_say(part)), _code_run(part)) if odd
        else _prose(part)
        for odd, part in ((i % 2, part) for i, part in enumerate(parts)))


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
    # ("math", "one line") iterates its characters: the block renders and
    # reads one character per line, and every check passes. Three Capital
    # lessons shipped that way before this guard.
    if isinstance(lines, str) or not all(isinstance(line, str) for line in lines):
        raise TypeError("a math block takes a list of lines, not %r" % (lines,))
    sayer = speech.say_code if _DIALECT.get() == speech.CODE_DIALECT else speech.say
    spoken = ". ".join(speech.say_block(lines, _SPOKEN, sayer=sayer))
    return '<div class="mathblock" data-say="%s">%s</div>' % (
        esc(spoken), "\n".join(esc(line) for line in lines))


# A code block's limits. 80 characters is the widest line that still scrolls
# only a little inside the block on a phone; 30 lines is a listing a reader can
# hold while reading the paragraph about it. A tab has no fixed width, so the
# listing would not look as it was written. tests/test_site_invariants.py
# (TestLessonDataMatchesTheRenderer) checks every Subject's data against these.
CODE_MAX_LINES = 30
CODE_MAX_WIDTH = 80
# The references an author writing HTML reaches for. Not any `&name;`: Java's
# `x = a&b;` is a bitwise and.
_ENTITY = re.compile(r"&(?:lt|gt|amp|quot|apos|nbsp|ndash|mdash|middot|hellip|minus|times"
                     r"|[lr][sd]quo|#\d+|#x[0-9A-Fa-f]+);")


def code_lines(payload):
    """The lines of a code block's payload: ["line", ...] or {"lines": [...], ...}.
    The snippet test (docs/code-complete/PLAN.md section H.3) compares a lab
    preset's code with "\\n".join(code_lines(payload))."""
    return payload["lines"] if isinstance(payload, dict) else payload


def code_marked(payload):
    """The flagged line numbers (from 1) of a code block's payload."""
    return frozenset(payload.get("marked", ())) if isinstance(payload, dict) else frozenset()


def code_block_problems(payload):
    """Why a ("code", payload) block cannot be drawn, or [] when it can.

    The payload is a list of lines, or {"lines": [...], "marked": [n, ...]}
    when some lines are flagged (drawn with a gutter mark and the hidden word
    "flagged", and announced as flagged by the read-out)."""
    if isinstance(payload, dict):
        extra = sorted(set(payload) - {"lines", "marked"})
        if extra or "lines" not in payload:
            return ["a code block's dict takes \"lines\" and optionally \"marked\", not %r"
                    % (sorted(payload),)]
        marked = payload.get("marked", [])
        lines = payload["lines"]
        if isinstance(marked, (str, dict)) or not all(
                isinstance(n, int) and not isinstance(n, bool) for n in marked):
            return ["a code block's \"marked\" is a list of line numbers, not %r" % (marked,)]
        if isinstance(lines, (list, tuple)):
            outside = sorted(n for n in marked if not 1 <= n <= len(lines))
            if outside:
                return ["marked line(s) %s are not lines of this block (1-%d)"
                        % (outside, len(lines))]
    else:
        lines = payload
    if isinstance(lines, str) or not isinstance(lines, (list, tuple)) \
            or not all(isinstance(line, str) for line in lines):
        return ["a code block takes a list of lines, not %r" % (lines,)]
    problems = []
    if not lines:
        problems.append("a code block has no lines")
    if len(lines) > CODE_MAX_LINES:
        problems.append("%d lines; a code block holds at most %d" % (len(lines), CODE_MAX_LINES))
    for number, line in enumerate(lines, 1):
        if len(line) > CODE_MAX_WIDTH:
            problems.append("line %d is %d characters; at most %d" % (number, len(line), CODE_MAX_WIDTH))
        if "\t" in line:
            problems.append("line %d holds a tab; indent with spaces" % number)
        if "\n" in line or "\r" in line:
            problems.append("line %d holds a line break; give each line its own string" % number)
        if _ENTITY.search(line):
            problems.append("line %d holds %r; a code line is shown exactly as written, so write "
                            "the character itself" % (number, _ENTITY.search(line).group()))
    return problems


def _codeblock(payload):
    """("code", ["line", ...]) -> a numbered listing, spoken as program text.

    Each line is escaped and wrapped in a span whose number the stylesheet
    draws with a CSS counter (theme.CODE_CSS), so selecting and copying the
    listing copies the code and no numbers. Read-out speaks the block line by
    line in the code dialect on every Subject: a code block is program text
    wherever it appears, each line announced by its number.

    A flagged line (payload {"lines": [...], "marked": [n]}) gets a gutter
    glyph and the hidden word "flagged" (theme.CODE_CSS): never colour alone.
    Both are generated content, so a copy of the listing is the code alone.
    (A visually hidden <span> would be text in the page that nobody sees,
    which tests/browser_contrast.js rightly fails.)
    """
    problems = code_block_problems(payload)
    if problems:
        if isinstance(payload, str) or problems[0].startswith(("a code block takes", "a code block's")):
            raise TypeError(problems[0])
        raise ValueError("code block: " + "; ".join(problems))
    lines, marked = code_lines(payload), code_marked(payload)
    spoken = ". ".join(speech.say_code_block(lines, _SPOKEN, marked))
    return '<pre class="codeblock" data-say="%s"><code>%s</code></pre>' % (
        esc(spoken), "\n".join(
            '<span class="cl flag">%s</span>' % esc(line) if number in marked else '<span class="cl">%s</span>' % esc(line)
            for number, line in enumerate(lines, 1)))


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
    if kind == "code":
        return _codeblock(payload)
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


_LAB_WORD = re.compile(r"\blabs?\b", re.I)


def lab_position(body):
    """Where the lab goes in a lesson's body: how many reading blocks precede it.

    docs/LESSON-LAYOUT-BACKLOG.md L-10, L-14. An author who wants the lab at a
    particular place writes the marker block ("lab", None) there; at most one.
    Otherwise the lab sits right after the first paragraph or list that
    mentions it, which is where the text starts to use it, and a lesson whose
    text never mentions the lab gets it after the reading. The count is of the
    blocks that are drawn, so the marker itself is not one of them.
    """
    markers = [i for i, (kind, _payload) in enumerate(body) if kind == "lab"]
    if len(markers) > 1:
        raise ValueError("a lesson places its lab once; found %d (\"lab\", None) blocks" % len(markers))
    if markers:
        return markers[0]
    for i, (kind, payload) in enumerate(body):
        if kind in ("p", "ul", "ol") and _LAB_WORD.search(
                payload if isinstance(payload, str) else " ".join(payload)):
            return i + 1
    return len(body)


def lesson_page(*, path, course, lesson, index, prev_lesson, next_lesson):
    """One lesson: /<course-slug>/<lesson-slug>/ ."""
    return lesson_page_with_lab(
        path=path, course=course, lesson=lesson, index=index,
        prev_lesson=prev_lesson, next_lesson=next_lesson)[0]


@_dialect
def lesson_page_with_lab(*, path, course, lesson, index, prev_lesson, next_lesson):
    """(markup, the Lab it was built from).

    The lab is handed back rather than rebuilt: scripts/build_paths.py needs
    lab.expect to write the expectations manifest, and building the lab twice
    would double the cost of a full render for a dictionary it already has.
    """
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
            # only a page that draws a listing carries its styles, so every
            # other page is byte-for-byte what it was before code blocks existed
            extra_css=theme.CODE_CSS if any(kind == "code" for kind, _ in lesson["body"]) else "",
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

    # -- the lesson bar: where you are, and Listen ---------------------------
    # docs/LESSON-LAYOUT-BACKLOG.md L-8. It stays on screen while the reader
    # scrolls, names the course, marks the part of the lesson in view (the
    # script at the foot of this page sets aria-current) and holds Listen,
    # which readout.py places in .bar-actions.
    parts.append(
        '    <nav class="lesson-bar" id="lessonBar" aria-label="In this lesson">\n'
        '      <a class="bar-course" href="../">%s</a>\n'
        '      <ol class="bar-steps">'
        '<li><a href="#read">Read</a></li><li><a href="#lab">Try</a></li>'
        '<li><a href="#process">Practise</a></li><li><a href="#check">Check</a></li></ol>\n'
        '      <div class="bar-actions"></div>\n'
        "    </nav>\n" % esc(course["title"])
    )

    # -- the head: one sentence, then the text --------------------------------
    # L-1. The kicker carries what the breadcrumb does not (the chapter) and
    # the lede is the lesson's authored one-line description. The long summary,
    # the key ideas and the key block close the lesson in the recap below.
    parts.append(
        '    <section class="lesson-head" data-ui="hero">\n'
        '      <p class="lesson-kind"><span data-ui="page-kind">Lesson</span> &middot; %s</p>\n'
        "      <h1>%s</h1>\n"
        '      <p class="lesson-lede">%s</p>\n'
        "    </section>\n"
        % (esc(lesson["module"]), esc(lesson["title"]), esc_inline(lesson["one_line"]))
    )

    # -- the reading, with the lab where the text first uses it --------------
    lab_markup = (
        '      <section class="lab-block" id="lab">\n'
        '        <div class="section-head"><div><p class="kicker">Try it</p>'
        "<h2>%s</h2></div><p>%s</p></div>\n"
        '        <div class="lab-layout">\n'
        '          <article class="card lab-main">\n%s\n          </article>\n'
        '          <aside class="card side-panel" aria-live="polite">\n'
        "            <h3>%s</h3>\n            <p>%s</p>\n%s\n          </aside>\n"
        "        </div>\n"
        "      </section>\n"
        % (
            esc(lab.title),
            esc(lab.subtitle),
            lab.markup,
            esc_inline(lab.panel_title),
            inline(lab.panel_intro),
            lab.controls,
        )
    )
    split = lab_position(lesson["body"])
    blocks = [(kind, payload) for kind, payload in lesson["body"] if kind != "lab"]
    before = "".join(_block(kind, payload) for kind, payload in blocks[:split])
    after = "".join(_block(kind, payload) for kind, payload in blocks[split:])
    parts.append(
        '    <section class="section lesson-reading" id="read">\n'
        '      <div class="reading-col"><h2>%s</h2>'
        '<div class="prose reading">%s</div></div>\n'
        "%s"
        "%s"
        "    </section>\n"
        % (
            esc_inline(lesson.get("read_title", lesson["title"])), before, lab_markup,
            '      <div class="reading-col"><div class="prose reading">%s</div></div>\n' % after
            if after else "",
        )
    )

    # -- method: the steps as a numbered list in the reading column ----------
    steps = "".join(
        "<li><strong>%s.</strong> %s</li>" % (esc_inline(t).rstrip("."), inline(body))
        for t, body in lesson["steps"]
    )
    parts.append(
        '    <section class="section reading-col" id="process">\n'
        "      <h2>%s</h2>\n"
        '      <p class="lead-in">%s</p>\n'
        '      <ol class="key-ideas method">%s</ol>\n'
        "    </section>\n"
        % (
            esc_inline(lesson.get("steps_title", "How to work with this")),
            inline(lesson.get("steps_intro", "The order matters more than the speed.")),
            steps,
        )
    )

    # -- practice + worked example: the quiz keeps its panel, it is a tool ----
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

    # -- mistakes and the check, as plain sections (L-11) ---------------------
    mistakes = "".join(
        '<div class="lesson-row"><div class="num">%d</div><div><strong>%s</strong><span>%s</span></div></div>'
        % (i + 1, esc_inline(t), inline(body))
        for i, (t, body) in enumerate(lesson["mistakes"])
    )
    standard_head, standard_body = lesson["standard"]
    parts.append(
        '    <section class="section reading-col" id="check">\n'
        '      <h3>Common mistakes</h3><div class="lesson-list">%s</div>\n'
        '      <h3>Check your understanding</h3>'
        '<div class="callout"><div class="mark">&#10003;</div><div><strong>%s</strong><p>%s</p></div></div>'
        '<div class="note"><strong>Note:</strong> %s</div>\n'
        "    </section>\n"
        % (mistakes, esc_inline(standard_head), inline(standard_body), inline(lesson["note"]))
    )

    # -- recap: the key ideas to recall, then the summary (L-9) ---------------
    # Recalling an idea before seeing it again strengthens it more than
    # re-reading it (retrieval practice), so each idea is a disclosure: its
    # name first, its statement on demand.
    recall = "".join(
        '<details class="recall"><summary>%s</summary><p>%s</p></details>'
        % (esc_inline(t), inline(body))
        for t, body in lesson["concepts"]
    )
    parts.append(
        '    <section class="section reading-col lesson-summary" id="recap" aria-labelledby="lessonRecap">\n'
        '      <h2 id="lessonRecap">Before you go</h2>\n'
        # concepts_intro introduced the three ideas when they were cards at
        # the top; it reads as well, or better, as the way into recalling them
        # (LESSON-LAYOUT-BACKLOG L-15). read_intro, the reading's side note,
        # stays unrendered: it was the fourth preview.
        '%s'
        '      <p class="lead-in">Say each idea in your own words, then open it to check.</p>\n'
        '      <div class="recall-list">%s</div>\n'
        "      <h3>Summary</h3>\n"
        "      <p>%s</p>\n"
        '      <figure class="key-figure">%s<figcaption>%s</figcaption></figure>\n'
        "    </section>\n"
        % ('      <p class="lead-in">%s</p>\n' % inline(lesson["concepts_intro"])
           if lesson.get("concepts_intro") else "",
           recall, inline(lesson["summary"]), _mathblock(lesson["key"]),
           esc_inline(lesson.get("key_label", "The statement in symbols")))
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

    # The course lead repeats the licence clause on every lesson; it stays on the
    # course home (docs/LESSON-LAYOUT-BACKLOG.md L-7).
    parts.append(chrome.footer(None, path["material"]))
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
                             + feedback.LESSON_JS
                             + LESSON_BAR_JS
                             + readout.READOUT_JS))
    return chrome.name_horizontal_scrollers("".join(parts)), lab


# The lesson bar's "you are here": the part whose top has passed a line a third
# of the way down the screen is current, except that the lab, which sits inside
# the reading, is current only while it is on that line.
LESSON_BAR_JS = """
  (function () {
    var bar = document.getElementById('lessonBar');
    if (!bar || typeof bar.querySelectorAll !== 'function'
        || typeof window.addEventListener !== 'function') return;
    var raf = window.requestAnimationFrame || function (f) { return setTimeout(f, 16); };
    var links = Array.prototype.slice.call(bar.querySelectorAll('.bar-steps a'));
    var parts = links.map(function (a) { return document.querySelector(a.getAttribute('href')); });
    var lab = document.getElementById('lab');
    function paint() {
      var line = window.innerHeight / 3, current = -1;
      parts.forEach(function (el, i) {
        if (el && el !== lab && el.getBoundingClientRect().top <= line) current = i;
      });
      if (lab) {
        var r = lab.getBoundingClientRect();
        if (r.top <= line && r.bottom > line) current = parts.indexOf(lab);
      }
      links.forEach(function (a, i) {
        if (i === current) a.setAttribute('aria-current', 'location');
        else a.removeAttribute('aria-current');
      });
    }
    var queued = false;
    window.addEventListener('scroll', function () {
      if (queued) return;
      queued = true;
      raf(function () { queued = false; paint(); });
    }, { passive: true });
    paint();
  })();
"""


def _first_upper(text):
    return text[:1].upper() + text[1:]


@_dialect
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
        '<div class="outcome"><h3>%s</h3><p>%s</p></div>' % (esc_inline(t), inline(body))
        for t, body in course["outcomes"]
    )

    # The pager is labelled by dependency, which is what the Subject's course
    # order means: "Builds on" the course this one assumes, "Leads to" the one
    # that assumes it. Both once read "Related course", which hid the direction.
    nav = []
    if index > 0:
        before = courses[index - 1]
        nav.append(
            '        <a class="path-move prev" href="../%s/" rel="prev">'
            "<span>Builds on</span><strong>%s</strong></a>"
            % (before["slug"], esc(before["title"]))
        )
    if index < total_courses - 1:
        after = courses[index + 1]
        nav.append(
            '        <a class="path-move next" href="../%s/" rel="next">'
            "<span>Leads to</span><strong>%s</strong></a>"
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
        # docs/LESSON-LAYOUT-BACKLOG.md C-1: the lessons, which are why a
        # reader opened this page, come right after a short head. The key card
        # and the three stat tiles are gone ("Format: Interactive" was true of
        # every course); the facts are one line inside the head, and the
        # objectives and background are one tap away below the list.
        '    <section class="page-head" data-ui="hero">\n'
        '      <p class="lesson-kind"><span data-ui="page-kind">Course</span> &middot; %s</p>\n'
        "      <h1>%s</h1>\n"
        '      <p class="lesson-lede">%s</p>\n'
        '      <dl class="meta-line" data-ui="metadata">'
        "<div><dt>Subject</dt><dd>%s</dd></div>"
        "<div><dt>Lessons</dt><dd>%d</dd></div>"
        "<div><dt>Level</dt><dd>%s</dd></div></dl>\n"
        '      <div class="hero-actions" data-ui="primary-actions">'
        '<a class="btn primary" href="./%s/">Start with %s</a></div>\n'
        "    </section>\n"
        % (
            esc(path["title"]), esc(course["title"]), inline(course["blurb"]),
            esc(path["title"]), len(lessons), esc(course["level"]),
            lessons[0]["slug"], esc(lessons[0]["title"]),
        ),
        '    <section class="section" id="syllabus" data-ui="lesson-list">\n'
        '      <div class="list-head"><h2>%d lessons</h2>'
        '<p class="course-progress" id="courseProgress"></p><p>%s</p></div>\n'
        '      <div class="syllabus">%s</div>\n'
        "    </section>\n" % (len(lessons), inline(course["syllabus_intro"]), syllabus),
        # Headings keep their levels and the outcomes their h3/p shape: the
        # copy fixtures in tests/content_preservation.json pin (tag, text).
        '    <details class="section more" id="about">\n'
        '      <summary class="more-summary">More about this course</summary>\n',
        '    <section class="more-part" data-ui="overview">\n'
        "      <h2>What you will be able to do</h2><p>%s</p>\n"
        '      <div class="outcomes">%s</div>\n'
        "    </section>\n" % (inline(course["outcomes_intro"]), outcomes),
        '    <section class="more-part" id="background" data-ui="background">'
        # First character up, and NOTHING else touched. str.capitalize()
        # lowercases the rest of the string, so every proper noun in this field
        # was destroyed: "Discrete Mathematics" shipped as "discrete
        # mathematics" and a course named by title as "queues and utilisation".
        # The two live paths never noticed because they wrote the field entirely
        # in lower case; the first course to name a sibling by title, which is
        # what the no-ordinals rule asks for, hit it immediately.
        # escaped, then the `x` shorthand: a background that names `y′ = k·y`
        # shipped its backticks on six Differential Equations course homes
        '<h2>Recommended background</h2><p>%s.</p></section>\n'
        % esc_inline(_first_upper(course["assumes_long"]).rstrip(".")),
        '    <section class="more-part">\n'
        '      <h3>Practice suggestions</h3>%s\n'
        '      <h3>What it does not cover</h3>%s\n'
        '      <h3>What this course is about</h3><figure class="key-figure">%s</figure>\n'
        "    </section>\n"
        "    </details>\n"
        % (
            "".join("<p>%s</p>" % inline(p) for p in course["how_to"]),
            "".join("<p>%s</p>" % inline(p) for p in course["not_covered"]),
            _mathblock(course["key"]),
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


@_dialect
def path_page(path):
    """Subject catalog at the stable /paths/<slug>/ URL."""
    courses = path["courses"]
    total_lessons = sum(len(c["lessons"]) for c in courses)
    cards = "".join(
        '<a class="spine-item" href="../../%s/" data-course="%s" data-lessons="%d">'
        '<div class="spine-body"><strong>%s</strong><p>%s</p>'
        '<div class="spine-meta"><span>%d lessons</span><span>%s</span>'
        '<span class="spine-progress" hidden></span></div></div></a>'
        % (c["slug"], c["slug"], len(c["lessons"]), esc(c["title"]),
           inline(c["blurb"]), len(c["lessons"]), esc(c["level"])) for c in courses)
    return chrome.name_horizontal_scrollers("".join([
        chrome.head(title="%s | Subject | Learn · geterdone.io" % path["title"],
                    description=plain(path["description"]),
                    canonical_path="/paths/%s/" % path["slug"], favicon=chrome.FAVICON_PATH, page_kind="subject"),
        chrome.topbar(up="../../"),
        chrome.crumbs([("Learn library", "../../"), (path["title"], None)]),
        '<main id="main">\n',
        # docs/LESSON-LAYOUT-BACKLOG.md S-1: the courses come right after a
        # short head, in one column so their order reads top to bottom (the
        # two-column grid read row by row). The four facts are one line in
        # the head; the overview and the background are one tap below.
        #
        # `level_note` was declared in every PATH dict and rendered nowhere. It
        # is the one thing a reader browsing Subjects most wants next to a
        # level -- every value is a statement about what is assumed ("no
        # calculus required", "assumes Discrete Mathematics in full") -- so it
        # is its own fact rather than a parenthetical inside Level.
        '<section class="page-head" data-ui="hero">'
        '<p class="lesson-kind"><span data-ui="page-kind">Subject</span> &middot; Learn library</p>'
        '<h1>%s</h1><p class="lesson-lede">%s</p>'
        '<dl class="meta-line" data-ui="metadata">'
        '<div><dt>Courses</dt><dd>%d</dd></div><div><dt>Lessons</dt><dd>%d</dd></div>'
        '<div><dt>Level</dt><dd>%s</dd></div>'
        '<div><dt>Assumes</dt><dd>%s</dd></div></dl>'
        '<div class="hero-actions" data-ui="primary-actions">'
        '<a class="btn primary" href="../../%s/">Start with %s</a></div></section>\n'
        % (esc(path["title"]), inline(path["tagline"]), len(courses), total_lessons,
           esc(path["level"]), esc(path["level_note"]),
           courses[0]["slug"], esc(courses[0]["title"])),
        '<section class="section" id="courses" data-ui="course-list">'
        '<div class="list-head"><h2>Courses</h2><p>%s</p></div>'
        '<div class="spine">%s</div></section>\n' % (inline(path["sequence_intro"]), cards),
        '<details class="section more" id="about"><summary class="more-summary">More about this Subject</summary>\n',
        '<section class="more-part prose" data-ui="overview"><h2>Overview</h2>%s</section>\n'
        % "".join('<p>%s</p>' % inline(p) for p in path["why_order"]),
        '<section class="more-part prose" id="background" data-ui="background">'
        '<h2>Recommended background</h2>%s</section>\n'
        % "".join('<p>%s</p>' % inline(p) for p in path["prerequisites"]),
        '<section class="more-part"><h3>In symbols</h3><figure class="key-figure">%s</figure></section>\n'
        % _mathblock(path["key"]),
        '</details>\n',
        '</main>\n',
        chrome.footer(inline(path["footer_lead"]), path["material"]),
        chrome.close(progress.PROGRESS_JS + progress.PATH_JS),
    ]))
