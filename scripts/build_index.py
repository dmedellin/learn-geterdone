#!/usr/bin/env python3
"""Render the Subject cards and the course search inventory on the site index.

    python3 scripts/build_index.py            # rewrite both regions
    python3 scripts/build_index.py --check    # fail if either would change

site/index.html is hand-authored -- its hero, styles and search script are
written there -- but two regions of it are a LIST OF THE LIBRARY, and a list
kept by hand drifts. Before this script the twelve Subject cards sat in the
order they were wired, and 12 of the 113 search descriptions matched neither
field a course declares. Both regions are now written from data:

    the Subjects section   from scripts/catalog.py (groups, order, card text)
                           and the PATH dicts (counts, level)
    var COURSES = [...]    from the same order, one entry per course, with the
                           description: the course `summary` as plain text for
                           a generated Subject (see describe() for the few that
                           cannot use it), the course card's text for Trading

Everything between the BEGIN and END markers is overwritten. Edit the catalog,
the content, or this file; never the region.

The search array builds TEXT NODES, so its strings are plain characters, never
entities: an entity written into it reaches the reader as its own characters.
"""

import argparse
import html
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "content"))
sys.dont_write_bytecode = True

import add_progress_marks  # noqa: E402
import build_paths  # noqa: E402
import catalog  # noqa: E402
from mathpath.render import plain  # noqa: E402

INDEX = REPO_ROOT / "site" / "index.html"
TRADING_PAGE = REPO_ROOT / "site" / "paths" / "trading" / "index.html"

BEGIN = ("<!-- BEGIN subjects: written by scripts/build_index.py from "
         "scripts/catalog.py. Do not edit by hand. -->")
END = "<!-- END subjects -->"
COURSES_RE = re.compile(r"(      var COURSES = )\[[\s\S]*?\n      \];")

# The Trading notices, moved from the foot of the page into the Markets group
# so they sit beside the one Subject they are about. The text is pinned by
# tests/content_preservation.json; change it there too or not at all.
TRADING_NOTICES = """
          <p class="edu-note">
          <strong>About the Trading courses: educational use only.</strong>
          Nothing in that material is trading, investment, or financial advice.
          Every chart, price, quote, trade, fill, and performance figure in those
          courses is a synthetic example generated to illustrate a concept: no
          lesson describes a real instrument or a real market session, and
          nothing there is a recommendation, a signal, or a forecast. Trading
          carries the risk of losing money, and real outcomes can differ from any
          illustration because of spread, slippage, commissions, gaps, taxes,
          liquidity, assignment, exercise, implied volatility, time decay, and
          other factors. Options in particular involve risk and are not suitable
          for every investor.
          </p>
          <p class="edu-note">
          <strong>The one exception, and it is dated.</strong>
          A single worked example published under Trading is not course
          material and is not synthetic: it analyses real market data for a real
          listed security over a fixed window that ended on August 14, 2026, and
          it is written as of August 16, 2026. It is a point-in-time snapshot,
          not a live or current view, and not a forecast. It is educational
          analysis, not personalized investment advice, not a trade signal, and
          not a guarantee of any outcome, and it carries a notice of its own
          saying exactly that.
          </p>"""


# The wording the library's search copy may not use, as tests/test_course_ui.py
# states it: "the path", "this path", "course 3".
CURRICULAR = re.compile(r"\b(?:the|this|learning|Trading|Algebra|Discrete Mathematics) path\b"
                        r"|\bcourse\s+\d", re.I)


def describe(course):
    """The search description: the course's summary, which is also its course
    home's meta description; the blurb if the summary is curricular; the
    catalog's own text if both are."""
    if course["slug"] in catalog.SEARCH_DESCRIPTIONS:
        return catalog.SEARCH_DESCRIPTIONS[course["slug"]]
    for field in ("summary", "blurb"):
        text = plain(course[field]).strip()
        if not CURRICULAR.search(text):
            return text
    raise SystemExit("%s: blurb and summary both say \"path\" or \"course N\"; add a "
                     "SEARCH_DESCRIPTIONS entry to scripts/catalog.py" % course["slug"])


def trading_courses():
    """Trading's courses with the text its Subject page shows on each card."""
    text = TRADING_PAGE.read_text(encoding="utf-8")
    blurbs = {}
    for card in re.finditer(r'<article class="course-card"[^>]*>(.*?)</article>', text, re.S):
        link = re.search(r'<h3><a href="\.\./\.\./([a-z0-9-]+)/">', card.group(1))
        body = re.search(r"</h3>\s*<p>(.*?)</p>", card.group(1), re.S)
        if link and body:
            blurbs[link.group(1)] = plain(body.group(1)).strip()
    courses = []
    for course in add_progress_marks.trading_inventory():
        courses.append({"slug": course["slug"], "title": course["title"],
                        "lessons": len(course["lessons"]),
                        "description": blurbs[course["slug"]]})
    return courses


def subjects():
    """[{slug, title, display, level, courses: [...]}] in catalog order."""
    by_slug = {}
    for path in build_paths.GENERATED_PATHS:
        by_slug[path["slug"]] = {
            "slug": path["slug"], "title": path["title"], "level": path["level"],
            "courses": [{"slug": c["slug"], "title": c["title"],
                         "lessons": len(c["lessons"]),
                         "description": describe(c)}
                        for c in path["courses"]],
        }
    by_slug["trading"] = dict(catalog.TRADING, level=None, courses=trading_courses())

    listed = [entry["slug"] for entry in catalog.SUBJECTS]
    if sorted(listed) != sorted(by_slug):
        raise SystemExit("scripts/catalog.py and the published Subjects disagree: "
                         "only in catalog %s, only published %s"
                         % (sorted(set(listed) - set(by_slug)),
                            sorted(set(by_slug) - set(listed))))
    out = []
    for entry in catalog.SUBJECTS:
        subject = dict(by_slug[entry["slug"]], **entry)
        subject["display"] = entry.get("short_title", subject["title"])
        out.append(subject)
    return out


def _esc(text):
    return html.escape(text, quote=True)


def _card(subject, displays):
    courses = subject["courses"]
    meta = "%d courses &middot; %d lessons" % (len(courses), sum(c["lessons"] for c in courses))
    if subject.get("level"):
        meta += " &middot; " + _esc(subject["level"]).replace("→", "&rarr;")
    parts = ['<article class="subject-card card card-pad">']
    if subject.get("kind"):
        parts.append('<span class="eyebrow">%s</span>' % _esc(subject["kind"]))
    href = "./paths/%s/" % subject["slug"]
    parts.append('<h4><a href="%s">%s</a></h4>' % (href, _esc(subject["display"])))
    parts.append("<p>%s</p>" % subject["card"])
    parts.append('<p class="subject-meta">%s</p>' % meta)
    if subject.get("builds_on"):
        links = ['<a href="./paths/%s/">%s</a>' % (slug, _esc(displays[slug]))
                 for slug in subject["builds_on"]]
        parts.append('<p class="subject-assumes">Builds on %s</p>' % " and ".join(links))
    parts.append('<a class="btn" href="%s">View courses</a>' % href)
    parts.append("</article>")
    return "".join(parts)


def subjects_markup(listed):
    displays = {s["slug"]: s["display"] for s in listed}
    jump = " ".join('<a href="#group-%s">%s</a>' % (g["key"], _esc(g["title"]))
                    for g in catalog.GROUPS)
    out = [
        BEGIN,
        '\n      <section class="section" id="paths" data-ui="subject-list">'
        '<div class="section-head"><div><h2 id="paths-title">Subjects</h2>'
        "<p>Browse courses by topic and use their recommended background to "
        "choose material.</p></div></div>",
        '\n        <p class="group-jump">%s</p>' % jump,
    ]
    for group in catalog.GROUPS:
        members = [s for s in listed if s["group"] == group["key"]]
        if not members:
            raise SystemExit("group %r in scripts/catalog.py has no Subject" % group["key"])
        out.append(
            '\n        <section class="subject-group" id="group-%s" aria-labelledby="group-%s-title">'
            '<div class="group-head"><h3 id="group-%s-title">%s</h3><p>%s</p></div>'
            '\n          <div class="grid-3">%s</div>'
            % (group["key"], group["key"], group["key"], _esc(group["title"]),
               _esc(group["note"]), "".join(_card(s, displays) for s in members)))
        if group["key"] == "markets":
            out.append(TRADING_NOTICES)
        out.append("\n        </section>")
    out.append("\n      </section>\n      " + END)
    return "".join(out)


def courses_markup(listed):
    """The array, in the shape the page has always had. `path` is written as a
    bare key on purpose: the copy sweep reads every quoted string in a script as
    reader-facing text, and a quoted "path" is the word the library's copy may
    not use."""
    def string(text):
        return json.dumps(text, ensure_ascii=False).replace("</", "<\\/")

    entries = []
    for subject in listed:
        for course in subject["courses"]:
            entries.append(
                "        {\n"
                '          "title": %s,\n'
                '          "description": %s,\n'
                "          path: %s,\n"
                '          "lessons": %d,\n'
                '          "href": %s\n'
                "        }" % (string(course["title"]), string(course["description"]),
                              string(subject["title"]), course["lessons"],
                              string("./%s/" % course["slug"])))
    return "[\n" + ",\n".join(entries) + "\n      ];"


def render(text):
    listed = subjects()
    start, stop = text.find(BEGIN), text.find(END)
    if start < 0 or stop < start:
        raise SystemExit("site/index.html has no %s ... %s region" % (BEGIN, END))
    text = text[:start] + subjects_markup(listed) + text[stop + len(END):]
    if not COURSES_RE.search(text):
        raise SystemExit("site/index.html has no `var COURSES = [...]` block")
    return COURSES_RE.sub(lambda m: m.group(1) + courses_markup(listed), text, count=1)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="do not write; exit non-zero if the index would change")
    args = parser.parse_args(argv)
    current = INDEX.read_text(encoding="utf-8")
    rendered = render(current)
    if rendered == current:
        print("site/index.html is current")
        return 0
    if args.check:
        print("OUT OF DATE: site/index.html; run scripts/build_index.py")
        return 1
    INDEX.write_text(rendered, encoding="utf-8")
    print("wrote site/index.html")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
