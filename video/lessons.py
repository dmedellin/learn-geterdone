"""Find a generated lesson by "<course>/<lesson>" and pull out what a video can show.

Stdlib only, so tests/test_video.py can use it without the video venv. The
lessons are the ones scripts/build_paths.py renders (GENERATED_PATHS); the
hand-written Trading pages are not covered yet.
"""

import html
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
    """Yield (path, course, lesson) for every generated lesson, in site order."""
    import build_paths  # noqa: E402  (imports every content package)
    for path in build_paths.GENERATED_PATHS:
        for course in path["courses"]:
            for lesson in course["lessons"]:
                yield path, course, lesson


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
            lines = body if isinstance(body, list) else str(body).split("\n")
            out[str(n)] = "\n".join(plain(x) for x in lines).strip("\n")
    return out


def plain(text):
    """Lesson markup (HTML entities, <code>, `ticks`, **bold**) as plain text."""
    text = re.sub(r"</?[a-zA-Z][^<>]*>", "", str(text))  # tags only; a bare < or <= is mathematics
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.replace("`", "").replace("**", "")
    # *emphasis* only: a star after a letter (y*, the equilibrium) is mathematics
    text = re.sub(r"(?<![\w*])\*(?!\s)([^*]+?)(?<!\s)\*(?![\w*])", r"\1", text)
    return html.unescape(text)


def outline(lesson):
    """A plain-text digest of the lesson, for whoever writes the scripts."""
    out = ["# %s" % plain(lesson["title"]), plain(lesson["one_line"]), "", plain(lesson["summary"]), ""]
    for kind, body in lesson.get("body", []):
        if kind in ("p", "def", "thm", "example", "proof"):
            out.append(plain(body if isinstance(body, str) else " ".join(map(str, body))))
        elif kind == "h3":
            out.append("## " + plain(body))
        elif kind in ("ul", "ol"):
            out += ["- " + plain(x) for x in body]
        elif kind in ("code", "math"):
            lines = body if isinstance(body, list) else [body]
            out += ["    " + plain(x) for x in lines]
        out.append("")
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
