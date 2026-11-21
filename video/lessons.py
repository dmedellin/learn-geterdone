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
            out.append(plain(body if isinstance(body, str) else " ".join(map(str, body))))
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
