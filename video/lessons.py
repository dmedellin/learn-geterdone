"""Find a generated lesson by "<course>/<lesson>" and pull out what a video can show.

Stdlib only, so tests/test_video.py can use it without the video venv. The
lessons are the ones scripts/build_paths.py renders (GENERATED_PATHS), then the
hand-written Trading lessons, whose page is their source: trading_lesson()
reads each page's <main> into the same lesson shape (title, one_line, body).
"""

import html
import html.parser
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
for _p in (ROOT / "scripts", ROOT / "content"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))
sys.dont_write_bytecode = True

_INDEX = None


def all_lessons():
    """Yield (path, course, lesson) for every lesson with a script: generated, then Trading."""
    import build_paths  # noqa: E402  (imports every content package)
    for path in build_paths.GENERATED_PATHS:
        for course in path["courses"]:
            for lesson in course["lessons"]:
                yield path, course, lesson
    yield from trading_lessons()


TRADING_PATH = {"slug": "trading", "title": "Trading"}


def trading_lessons():
    """(path, course, lesson) for each hand-written Trading lesson, in course order."""
    import add_progress_marks as apm  # noqa: E402  (reads the course list out of the pages)
    for c in apm.trading_inventory():
        course = {"slug": c["slug"], "title": c["title"], "lessons": []}
        for item in c["lessons"]:
            course["lessons"].append(trading_lesson(c["slug"], item["slug"], item["title"]))
        for lesson in course["lessons"]:
            yield TRADING_PATH, course, lesson


class _Main(html.parser.HTMLParser):
    """Block text of a Trading page's <main>, as (kind, text) in reading order."""
    SKIP = {"script", "style", "svg", "select", "option", "input", "textarea", "canvas", "noscript"}
    BLOCKS = {"h1": "h1", "h2": "h3", "h3": "h4", "h4": "h4", "p": "p", "li": "li", "pre": "code",
              "td": "cell", "th": "cell", "figcaption": "p", "blockquote": "p", "label": "li", "dt": "p", "dd": "p"}
    ROWS = ("lesson-row", "callout", "note", "reading", "feedback")

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip, self.stack, self.buf, self.kind = [], 0, [], [], None
        self.choice = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class") or ""
        if tag in self.SKIP or (tag == "section" and a.get("id") == "feedback") or "visually-hidden" in cls:
            self.skip += 1
            self.stack.append(("skip", tag))
            return
        if tag == "article" and a.get("data-correct", "").isdigit():
            self.correct, self.qi = int(a["data-correct"]), 0
        if "choice-grid" in cls or cls.split() == ["choices"]:
            self.choice += 1
            self.stack.append(("choice", tag))
            return
        self.stack.append(("tag", tag))
        if self.skip:
            return
        row = tag == "div" and any(k in cls.split() for k in self.ROWS)
        formula = tag == "div" and "rule-output" in cls.split()  # pre-formatted formula block
        if tag in self.BLOCKS or (tag == "button" and self.choice) or row or formula:
            self.flush()
            self.kind = ("li" if tag == "button" else "math" if formula else "p" if row
                         else self.BLOCKS[tag])
            if tag == "button" and getattr(self, "correct", None) is not None:
                # a quiz choice: the page's data-correct marks the right one
                self.buf.append("(correct) " if self.qi == self.correct else "(wrong) ")
                self.qi += 1
                if a.get("data-why"):
                    self.why = a["data-why"]
            self.depth = len(self.stack)
        elif tag == "br" and self.kind in ("code", "math"):
            self.buf.append("\n")
        elif self.kind and self.kind not in ("code", "math"):
            self.buf.append(" ")

    def handle_endtag(self, tag):
        if tag == "article":
            self.correct = None
        while self.stack:
            what, t = self.stack.pop()
            if what == "skip":
                self.skip -= 1
            elif what == "choice":
                self.choice -= 1
            if t == tag:
                break
        if not self.skip and (tag in self.BLOCKS or tag == "button" or len(self.stack) < getattr(self, "depth", -1)):
            self.flush()
        elif self.kind and self.kind not in ("code", "math"):
            self.buf.append(" ")

    def handle_data(self, data):
        if not self.skip and self.kind:
            self.buf.append(data)

    def flush(self):
        if self.kind and self.buf:
            text = "".join(self.buf)
            text = text.strip("\n") if self.kind in ("code", "math") else re.sub(r"\s+", " ", text).strip()
            if getattr(self, "why", None):
                text += " [why it is wrong: %s]" % self.why
                self.why = None
            if text:
                self.out.append((self.kind, text))
        self.kind, self.buf, self.depth = None, [], -1


def trading_lesson(course_slug, slug, title):
    """A Trading lesson page read into the generated lesson shape."""
    page = ROOT / "site" / course_slug / slug / "index.html"
    text = page.read_text(encoding="utf-8")
    main = re.search(r'<main id="main">(.*?)</main>', text, re.S)
    parser = _Main()
    parser.feed(main.group(1) if main else "")
    parser.flush()
    desc = re.search(r'<meta name="description" content="([^"]*)"', text)
    body, cells = [], []
    for kind, value in parser.out:
        if kind != "cell" and cells:
            body.append(("p", " | ".join(cells)))
            cells = []
        if kind == "h1":
            continue
        if kind == "cell":
            cells.append(value)
        elif kind in ("h3", "h4"):
            body.append(("h3", value))
        elif kind == "li":
            body.append(("ul", [value]))
        elif kind in ("code", "math"):
            body.append((kind, value.split("\n")))
        else:
            body.append(("p", value))
    if cells:
        body.append(("p", " | ".join(cells)))
    return {"slug": slug, "title": title, "one_line": html.unescape(desc.group(1)) if desc else "",
            "summary": "", "body": body, "trading": True}


def key(course, lesson):
    return "%s/%s" % (course["slug"], lesson["slug"])


def find(lesson_key):
    """(path, course, lesson) for "<course-slug>/<lesson-slug>"."""
    global _INDEX
    if _INDEX is None:
        _INDEX = {key(c, l): (p, c, l) for p, c, l in all_lessons()}
    try:
        return _INDEX[lesson_key]
    except KeyError:
        raise KeyError("no generated lesson %r (use <course-slug>/<lesson-slug>)" % lesson_key)


def url_path(course, lesson):
    return "/%s/%s/" % (course["slug"], lesson["slug"])


def code_sources(lesson):
    """The lesson's ("code", lines) blocks in order, keyed "1", "2", ... as strings."""
    out, n = {}, 0
    for kind, body in lesson.get("body", []):
        if kind == "code":
            n += 1
            # a code line is shown exactly as written (scripts/mathpath/render.py
            # code_block_problems), so it is not run through plain(): <T>, ** and *p are code
            lines = body["lines"] if isinstance(body, dict) else body
            lines = lines if isinstance(lines, (list, tuple)) else str(lines).split("\n")
            out[str(n)] = "\n".join(lines).strip("\n")
    return out


def plain(text):
    """Lesson markup (HTML entities, <code>, `ticks`, **bold**) as plain text."""
    text = re.sub(r"</?[a-zA-Z][^<>]*>", "", str(text))  # tags only; a bare < or <= is mathematics
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.replace("`", "").replace("**", "")
    # *emphasis* only: a star after a letter (y*, the equilibrium) is mathematics
    text = re.sub(r"(?<![\w*])\*(?!\s)([^*]+?)(?<!\s)\*(?![\w*])", r"\1", text)
    return html.unescape(text)


def _as_list(x):
    return [] if x is None else ([x] if isinstance(x, str) else list(x))


def outline(lesson):
    """A plain-text digest of the lesson, for whoever writes the scripts."""
    out = ["# %s" % plain(lesson["title"]), plain(lesson["one_line"]), "", plain(lesson["summary"]), ""]
    for kind, body in lesson.get("body", []):
        if kind in ("p", "def", "thm", "example", "proof"):
            if isinstance(body, str):
                out.append(plain(body))
            elif isinstance(body, tuple) and len(body) > 1:  # (heading, text, ...): keep the heading apart
                out.append("%s %s: %s" % (kind.capitalize(), plain(body[0]), " ".join(plain(x) for x in body[1:])))
            else:
                out.append(plain(" ".join(map(str, body))))
        elif kind == "h3":
            out.append("## " + plain(body))
        elif kind in ("ul", "ol"):
            out += ["- " + plain(x) for x in body]
        elif kind in ("code", "math"):
            lines = body if isinstance(body, list) else [body]
            out += ["    " + plain(x) for x in lines]
        out.append("")
    lab = lesson.get("lab")
    if isinstance(lab, (list, tuple)) and len(lab) > 1 and isinstance(lab[1], dict):
        cfg = lab[1]
        out.append("## Lab: %s" % plain(cfg.get("panel_title", lab[0])))
        if cfg.get("panel_intro"):
            out.append(plain(cfg["panel_intro"]))
        out.append("")
    if lesson.get("steps"):
        out.append("## Steps")
        if lesson.get("steps_intro"):
            out.append(plain(lesson["steps_intro"]))
        out += ["%d. %s: %s" % (n, plain(t), plain(b)) for n, (t, b) in enumerate(lesson["steps"], 1)]
        out.append("")
    worked = lesson.get("worked")
    if isinstance(worked, dict):
        out.append("## Worked example: %s" % plain(worked.get("title", "")))
        out += [plain(x) for x in _as_list(worked.get("intro"))]
        out += ["    " + plain(x) for x in _as_list(worked.get("lines"))]
        out += [plain(x) for x in _as_list(worked.get("after"))]
        out.append("")
    if lesson.get("quiz"):
        out.append("## Quiz (answers marked *)")
        for item in lesson["quiz"]:
            out.append("- Q: " + plain(item["q"]))
            out += ["    %s %s" % ("*" if i == item.get("c") else "-", plain(a)) for i, a in enumerate(item["a"])]
            if item.get("why"):
                out.append("    Why: " + plain(item["why"]))
        out.append("")
    if lesson.get("note"):
        out += ["## Note", plain(lesson["note"]), ""]
    out.append("## Key")
    out += ["- " + plain(k) for k in lesson.get("key", [])]
    out.append("## Concepts")
    out += ["- %s: %s" % (plain(t), plain(b)) for t, b in lesson.get("concepts", [])]
    out.append("## Mistakes")
    out += ["- %s: %s" % (plain(t), plain(b)) for t, b in lesson.get("mistakes", [])]
    return "\n".join(out)


_TRAILING_COMMENT = re.compile(r"\s{2,}(#|//).*$")


def display_lines(code, strip_comments=False):
    """The listing as a video shows it; `strip_comments` drops trailing comments."""
    lines = code.split("\n")
    return [_TRAILING_COMMENT.sub("", x) for x in lines] if strip_comments else lines
