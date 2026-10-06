#!/usr/bin/env python3
"""Render every generated path into site/.

    python3 scripts/build_paths.py            # write the pages
    python3 scripts/build_paths.py --check    # fail if any page would change

--check is what CI runs. The content is the source and the pages are derived, so
a page edited by hand is a page that will be silently reverted the next time
anyone builds; failing loudly is the only honest alternative.

A new generated path is one import and one entry in GENERATED_PATHS below. It is
deliberately not a discovery scan of content/: the set of published paths is a
decision, and it should be readable in one place rather than inferred from which
directories happen to exist.
"""

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "content"))
sys.dont_write_bytecode = True

from algebra import PATH as ALGEBRA_PATH  # noqa: E402
from algorithms import PATH as ALGORITHMS_PATH  # noqa: E402
from discrete_math import PATH as DISCRETE_MATH_PATH  # noqa: E402
from operations_research import PATH as OPERATIONS_RESEARCH_PATH  # noqa: E402
from system_design import PATH as SYSTEM_DESIGN_PATH  # noqa: E402
from mathpath import render  # noqa: E402

GENERATED_PATHS = (DISCRETE_MATH_PATH, ALGEBRA_PATH, SYSTEM_DESIGN_PATH,
                   ALGORITHMS_PATH, OPERATIONS_RESEARCH_PATH)

SITE = REPO_ROOT / "site"
# The list of pages this build produces, consumed by scripts/labcheck.js.
MANIFEST = REPO_ROOT / "scripts" / "generated-pages.txt"
# What each of those pages must PRINT, also consumed by scripts/labcheck.js.
EXPECTATIONS = REPO_ROOT / "scripts" / "generated-expectations.json"

# THE SWITCH. One lab key per line; a kit is converted by adding it here.
#
# A preset's menu text is prose, and no check in this repository can read it --
# a sweep of fifteen kits found 57 preset strings that were false about the lab
# they described, and every check passed on all of them. What a preset makes the
# page PRINT is checkable, so each preset now carries an `expect` dict and
# labcheck.js reads the tile out of the built page. For a kit listed here the
# check is a GATE: every option of every declared preset <select> must pin at
# least one tile or the page fails, because a mechanism authors can skip is an
# intention rather than a mechanism.
#
# The remaining kits are not listed, so they are not gated, and adding one
# before its presets carry expectations is what makes its pages fail. That is
# the intended order: convert the kit, then add the line.
KITS_WITH_EXPECTATIONS = ("greedy", "random", "hash", "tree", "reduction", "coping",
                          "dpkit", "dpseq", "strings", "geometry",
                          "markov", "schedule", "network", "graphkit", "flowkit",
                          "tense",)


def path_pages(path):
    """[(relative path under site/, markup, expectations or None)] for one path.

    The third item is the page's entry in the expectations manifest, and it is
    None for every page whose kit is not in KITS_WITH_EXPECTATIONS -- a page
    absent from that manifest is a page labcheck.js does not gate.
    """
    out = [("paths/%s/index.html" % path["slug"], render.path_page(path), None)]
    courses = path["courses"]
    for index, course in enumerate(courses):
        out.append((
            "%s/index.html" % course["slug"],
            render.course_home(course=course, index=index, courses=courses, path=path),
            None,
        ))
        lessons = course["lessons"]
        for position, lesson in enumerate(lessons):
            markup, lab = render.lesson_page_with_lab(
                path=path,
                course=course,
                lesson=lesson,
                index=position,
                prev_lesson=lessons[position - 1] if position else None,
                next_lesson=lessons[position + 1] if position + 1 < len(lessons) else None,
            )
            kit = lesson["lab"][0]
            expect = None
            if kit in KITS_WITH_EXPECTATIONS:
                # Emitted even when the lab declared nothing, because an empty
                # entry is what makes labcheck.js fail the page. A kit that is
                # switched on and then quietly emptied must not fall silent.
                expect = {"kit": kit, "selects": lab.expect}
            out.append(("%s/%s/index.html" % (course["slug"], lesson["slug"]), markup, expect))
    return out


def pages():
    """[(relative path under site/, markup, expectations or None)] for every path."""
    out = []
    for path in GENERATED_PATHS:
        out.extend(path_pages(path))
    return out


def expectations_body(built):
    """The manifest text, for the pages in `built` that carry expectations."""
    return json.dumps(
        {"pages": {"site/" + relative: entry
                   for relative, _markup, entry in built if entry is not None}},
        indent=1, sort_keys=True,
    ) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="do not write; exit non-zero if any page differs")
    args = parser.parse_args(argv)

    built = pages()

    # The manifest scripts/labcheck.js consumes. It is derived from the same
    # page list, so the harness can never drift from what was built -- and it is
    # what lets --generated mean "the pages this harness was written for" rather
    # than "every page in the repository". The trading path's widgets use DOM
    # features the harness deliberately does not implement, and reporting them
    # as failures would be reporting a limitation of the harness as a defect in
    # those pages.
    manifest_written = 0
    changed, written = [], 0
    for manifest, body in ((MANIFEST, "\n".join("site/" + relative
                                                for relative, _m, _e in built) + "\n"),
                           (EXPECTATIONS, expectations_body(built))):
        current = manifest.read_text(encoding="utf-8") if manifest.is_file() else None
        if current != body:
            changed.append(str(manifest.relative_to(REPO_ROOT)))
            if not args.check:
                manifest.write_text(body, encoding="utf-8")
                manifest_written += 1
    for relative, markup, _entry in built:
        target = SITE / relative
        current = target.read_text(encoding="utf-8") if target.is_file() else None
        if current == markup:
            continue
        changed.append(relative)
        if not args.check:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(markup, encoding="utf-8")
            written += 1

    for path in GENERATED_PATHS:
        total_lessons = sum(len(c["lessons"]) for c in path["courses"])
        print("%s: %d courses, %d lessons"
              % (path["title"], len(path["courses"]), total_lessons))
    print("%d generated pages in total" % len(built))
    if args.check:
        if changed:
            print("OUT OF DATE (%d page(s)); run scripts/build_paths.py:" % len(changed))
            for relative in changed[:20]:
                print("  %s" % relative)
            if len(changed) > 20:
                print("  ... and %d more" % (len(changed) - 20))
            return 1
        print("every published page matches the content in content/")
        return 0
    # The manifest is counted apart from the pages: folding it in made this line
    # report "-1 already current" on a full rebuild.
    print("wrote %d page(s), %d already current%s"
          % (written, len(built) - written,
             "; %d manifest(s) updated" % manifest_written if manifest_written else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
