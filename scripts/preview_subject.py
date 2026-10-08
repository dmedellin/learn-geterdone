"""Render and check a Subject that is not yet in GENERATED_PATHS.

Wiring a Subject touches two dozen declaration sites (AGENTS.md section 0), so
it happens once, at the end. Until then an author still needs every check that
does not depend on the wiring, on their own course, in seconds:

  - the lesson shape the renderer and TestLessonDataMatchesTheRenderer enforce;
  - quiz answerability, plain titles, hero key lines that fit the key box;
  - the page actually renders -- which builds the lab, so an unknown mode or a
    bad preset fails here rather than in CI;
  - labcheck.js executes every rendered lab and compares every pinned tile;
  - read-out: no math symbol without a spoken form, and the list of runs the
    rules can only guess at (they need content/spoken/<subject>.py entries).

    python3 scripts/preview_subject.py philosophy                    # the whole Subject
    python3 scripts/preview_subject.py philosophy --course SLUG ...  # some courses
    python3 scripts/preview_subject.py philosophy --no-labcheck      # skip the node run

Writes the pages under --out (default: a fresh directory under /tmp) and exits
non-zero on any failure.
"""

import argparse
import importlib
import json
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "content"))

from build_paths import KITS_WITH_EXPECTATIONS  # noqa: E402
from mathpath import render, speech  # noqa: E402

EXACT = {"concepts": 3, "mistakes": 3}
RANGES = {"steps": (4, 5), "quiz": (3, 4), "key": (3, 8), "body": (7, 18)}
KEY_WIDTH = 46  # the hero key box holds 46 characters at desktop width


def width(line):
    """Rendered width: combining marks take no column."""
    return sum(1 for ch in line if not unicodedata.combining(ch))


def check_lesson(where, lesson, fail):
    for field, want in EXACT.items():
        if len(lesson[field]) != want:
            fail("%s: %d %s, the layout draws exactly %d" % (where, len(lesson[field]), field, want))
    for field, (lo, hi) in RANGES.items():
        if not lo <= len(lesson[field]) <= hi:
            fail("%s: %d %s, outside %d-%d" % (where, len(lesson[field]), field, lo, hi))
    for i, q in enumerate(lesson["quiz"]):
        if len(q["a"]) != 4 or not 0 <= q["c"] < 4 or not q["why"].strip() or len(set(q["a"])) != 4:
            fail("%s: quiz %d needs four distinct choices, a valid index and an explanation" % (where, i))
    for field in ("title",):
        if "`" in lesson[field] or "<" in lesson[field] or "&" in lesson[field]:
            fail("%s: %s reaches <title> and og:title; keep it plain text" % (where, field))
    for line in lesson["key"]:
        if width(line) > KEY_WIDTH:
            fail("%s: key line is %d characters, the box holds %d: %r" % (where, width(line), KEY_WIDTH, line))


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("package", help="content package, e.g. philosophy")
    parser.add_argument("--course", action="append", help="limit to these course slugs")
    parser.add_argument("--out", help="output directory (default: a new temp dir)")
    parser.add_argument("--no-labcheck", action="store_true")
    args = parser.parse_args()

    path = importlib.import_module(args.package).PATH
    out = Path(args.out or tempfile.mkdtemp(prefix="preview-%s-" % args.package))
    failures = []
    fail = failures.append
    courses = [c for c in path["courses"] if not args.course or c["slug"] in args.course]
    if args.course and len(courses) != len(args.course):
        fail("unknown course slug among %s" % args.course)

    for line in path["key"]:
        if width(line) > KEY_WIDTH:
            fail("PATH key line is %d characters: %r" % (width(line), line))

    pages, expectations = [], {}
    if not args.course:
        pages.append(("paths/%s/index.html" % path["slug"], render.path_page(path)))
    all_courses = path["courses"]
    overrides = speech.all_overrides()
    guessed = []
    for course in courses:
        index = all_courses.index(course)
        for line in course["key"]:
            if width(line) > KEY_WIDTH:
                fail("%s: course key line is %d characters: %r" % (course["slug"], width(line), line))
        try:
            pages.append(("%s/index.html" % course["slug"],
                          render.course_home(course=course, index=index, courses=all_courses, path=path)))
        except Exception as exc:  # noqa: BLE001 -- report and keep going
            fail("%s: course home does not render: %r" % (course["slug"], exc))
        lessons = course["lessons"]
        for i, lesson in enumerate(lessons):
            where = "%s/%s" % (course["slug"], lesson["slug"])
            try:
                check_lesson(where, lesson, fail)
                markup, lab = render.lesson_page_with_lab(
                    path=path, course=course, lesson=lesson, index=i,
                    prev_lesson=lessons[i - 1] if i else None,
                    next_lesson=lessons[i + 1] if i + 1 < len(lessons) else None)
            except Exception as exc:  # noqa: BLE001
                fail("%s: does not render: %r" % (where, exc))
                continue
            relative = "%s/%s/index.html" % (course["slug"], lesson["slug"])
            pages.append((relative, markup))
            kit = lesson["lab"][0]
            if kit in KITS_WITH_EXPECTATIONS or lab.expect:
                expectations["site/" + relative] = {"kit": kit, "selects": lab.expect}
            # read-out coverage for this lesson's math
            for run, _, _ in _runs(lesson):
                if speech.unspoken(overrides.get(run) or speech.say(run)):
                    fail("%s: math with no spoken form: %r" % (where, run))
                elif run not in overrides and speech.ambiguous(run):
                    guessed.append((where, run))

    for relative, markup in pages:
        target = out / "site" / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(markup, encoding="utf-8")
    manifest = out / "scripts" / "expectations.json"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text(json.dumps({"pages": expectations}, indent=1, sort_keys=True), encoding="utf-8")
    (out / "scripts" / "pages.txt").write_text(
        "\n".join(str(out / "site" / r) for r, _ in pages) + "\n", encoding="utf-8")

    print("%d page(s) rendered to %s/site" % (len(pages), out))
    if guessed:
        print("%d math run(s) the read-out rules guess at -- give each a spoken form in "
              "content/spoken/%s.py, or rewrite it to the convention in content/AGENTS.md:"
              % (len(guessed), args.package))
        for where, run in guessed:
            print("   %s: %r" % (where, run))

    if not args.no_labcheck and pages:
        lesson_files = [str(out / "site" / r) for r, _ in pages if r.count("/") == 2]
        runs = [("every lab executes", lesson_files)]
        if expectations:
            runs.append(("pinned figures match", ["--expect", str(manifest)]))
        for name, argv in runs:
            result = subprocess.run(["node", str(REPO_ROOT / "scripts" / "labcheck.js")] + argv,
                                    capture_output=True, text=True)
            tail = (result.stdout + result.stderr).strip().splitlines()[-12:]
            print("labcheck, %s:" % name)
            print("\n".join("   " + line for line in tail))
            if result.returncode != 0:
                fail("labcheck failed: " + name)

    if failures:
        print("\n%d FAILURE(S):" % len(failures))
        for f in failures:
            print("  - " + f)
        sys.exit(1)
    print("OK")


def _runs(lesson):
    """The math runs a lesson page speaks, as speechcheck.runs finds them."""
    from speechcheck import runs
    return runs({"courses": [{"lessons": [lesson]}]})


if __name__ == "__main__":
    main()
