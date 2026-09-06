#!/usr/bin/env python3
"""Give the trading path the completion marks the generated paths already have.

WHY THIS IS A PATCHER AND NOT A RENDERER. The two mathematics paths are
generated from data by build_paths.py, so their lesson pages get the completion
toggle for free. The eight trading courses predate that machinery: their 129
pages are hand-written and there is no generator to re-run. Rewriting them as
data would be a different and much larger change, and would risk the material.
So this edits them in place, and is written to be run again safely.

IDEMPOTENCE IS THE WHOLE DESIGN. A previous in-place patcher in this repo
(register_labs.py) matched only the first line of the statement it was editing
and mangled the file on its second run. Every insertion here is therefore
delimited by an explicit marker and REPLACED rather than appended:

    CSS     /* progress-marks:begin */ ... /* progress-marks:end */
    script  <script data-progress-marks> ... </script>
    markup  identified by id="progressToggle", class="topbar-actions",
            data-lesson= and data-course=

Running it twice must produce a file identical to running it once, and the test
suite checks exactly that.

WHERE THE INVENTORY COMES FROM. The published pages themselves: the path page
lists the courses in order, and each course home lists its lessons in order.
Nothing is re-declared here, so there is no second copy to drift -- a lesson is
in the inventory precisely because a course home links to it.
"""

import pathlib
import re
import sys
from html import unescape
from html.parser import HTMLParser

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from mathpath import chrome, feedback, progress
from mathpath.theme import UI_CSS  # noqa: E402

SITE = pathlib.Path(__file__).resolve().parent.parent / "site"
PATH_PAGE = "paths/trading/index.html"

CSS_BEGIN = "/* progress-marks:begin */"
CSS_END = "/* progress-marks:end */"
SCRIPT_OPEN = "<script data-progress-marks>"
SCRIPT_CLOSE = "</script>"

SIGNIN_TITLE = ("Optional. Signing in carries your completion ticks to your other "
                "devices; it unlocks nothing, because nothing here is locked.")


# --- the styles these pages do not have ------------------------------------
# Values are copied from mathpath/theme.py so a trading lesson's control is the
# same control a mathematics lesson has, not a lookalike. The custom properties
# used here are shared with the generated chrome. ensure_css bridges the
# older panel2/line2 palette names and supplies accent ink for both themes.
CSS = feedback.CSS + """
    .progress-bar {
      display: flex;
      flex-direction: column;
      gap: 7px;
      margin-top: 22px;
      padding: 15px 17px;
      border: 1px solid var(--line);
      border-radius: 12px;
      background: var(--panel-2);
    }
    .progress-toggle {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      align-self: flex-start;
      padding: 10px 16px;
      border: 1px solid var(--line-strong);
      border-radius: 10px;
      background: var(--panel);
      color: var(--text);
      font: inherit;
      font-weight: 700;
      cursor: pointer;
    }
    .progress-toggle:hover { border-color: var(--cyan); }
    .progress-toggle .progress-tick {
      display: grid;
      place-items: center;
      width: 20px;
      height: 20px;
      border-radius: 6px;
      border: 1px solid var(--line-strong);
      background: var(--panel-2);
      color: transparent;
      font-size: 0.8rem;
      font-weight: 900;
    }
    .progress-toggle.is-done { border-color: var(--green); color: var(--green); }
    .progress-toggle.is-done .progress-tick {
      border-color: var(--green);
      background: var(--green);
      color: var(--on-accent);
    }
    .progress-note { margin: 0; color: var(--muted); font-size: 0.82rem; }
    .progress-note a { color: var(--cyan); }

    .course-progress {
      margin: 0 0 13px;
      color: var(--muted);
      font-size: 0.82rem;
      font-weight: 700;
      letter-spacing: 0.04em;
      text-transform: uppercase;
    }

    /* A finished lesson on a course home, and a finished course on the path
       page. Both are a tick and a border -- never a change of size, because a
       card that grows when marked makes the page jump under the reader. */
    .lesson-card.is-done { border-color: var(--green); }
    .lesson-card.is-done .lesson-ord::after {
      content: " \\2713";
      color: var(--green);
      font-weight: 900;
    }
    .course-card.is-complete { border-color: var(--green); }
    .course-progress-note {
      display: block;
      margin-top: 9px;
      color: var(--green);
      font-size: 0.82rem;
      font-weight: 750;
    }
    .course-progress-note:empty { display: none; }

    .topbar-actions { display: flex; align-items: center; gap: 8px; flex: none; }
    .signin-btn {
      display: inline-flex;
      align-items: center;
      gap: 7px;
      flex: none;
      padding: 0 12px;
      height: 38px;
      border: 1px solid var(--line);
      border-radius: 11px;
      background: var(--panel-2);
      color: var(--muted);
      text-decoration: none;
      font-size: 0.84rem;
      font-weight: 650;
      white-space: nowrap;
    }
    .signin-btn:hover { color: var(--text); border-color: var(--line-strong); }
    .signin-mark { font-size: 0.6rem; line-height: 1; color: var(--line-strong); }
    .signin-btn.is-in .signin-mark { color: var(--green); }
    @media (max-width: 560px) {
      .signin-label { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); clip-path: inset(50%); white-space: nowrap; }
      .signin-btn { padding: 0; width: 38px; justify-content: center; }
    }
"""

# --- the scripts -----------------------------------------------------------
# Byte-for-byte the same behaviour as mathpath/progress.py: the same storage
# key, the same date format, the same shape of stored value. A tick made on a
# trading lesson and a tick made on an algebra lesson have to be the same kind
# of thing, because /progress/ counts them together.
COURSE_JS = """
  (function () {
    if (!window.learnProgress) return;
    var out = document.getElementById('courseProgress');
    var items = [].slice.call(document.querySelectorAll('[data-lesson]'));
    if (!items.length) return;
    function paint() {
      var n = 0;
      items.forEach(function (item) {
        var on = window.learnProgress.done(item.getAttribute('data-lesson'));
        item.classList.toggle('is-done', on);
        var state = item.querySelector('.lesson-state');
        if (state) state.textContent = on ? 'Marked complete' : 'Not marked';
        if (on) n += 1;
      });
      if (out) {
        out.textContent = n === 0
          ? 'None of the ' + items.length + ' lessons marked complete'
          : n + ' of ' + items.length + ' lessons marked complete';
      }
    }
    paint();
    window.addEventListener('storage', paint);
  })();
"""

PATH_JS = """
  (function () {
    if (!window.learnProgress) return;
    var marks = window.learnProgress.read();
    [].slice.call(document.querySelectorAll('[data-course]')).forEach(function (item) {
      var slug = item.getAttribute('data-course');
      var total = parseInt(item.getAttribute('data-lessons'), 10) || 0;
      var n = Object.keys(marks).filter(function (k) { return k.indexOf(slug + '/') === 0; }).length;
      var out = item.querySelector('.course-progress-note');
      if (!out || !total) return;
      out.textContent = n ? n + ' of ' + total + ' lessons marked complete' : '';
      item.classList.toggle('is-complete', n >= total);
    });
  })();
"""

SIGNIN_JS = """
  (function () {
    var a = document.getElementById('signinLink');
    if (!a) return;
    var s = null;
    try { s = JSON.parse(sessionStorage.getItem('learn-auth') || 'null'); }
    catch (e) { return; }
    if (!s || !s.access_token) return;
    var label = document.getElementById('signinLabel');
    var name = null;
    try {
      if (s.id_token) {
        var c = JSON.parse(atob(s.id_token.split('.')[1].replace(/-/g, '+').replace(/_/g, '/')));
        name = c.name || c.preferred_username || null;
      }
    } catch (e) { name = null; }
    if (label) label.textContent = name ? String(name).split(' ')[0] : 'Signed in';
    a.setAttribute('title', (name ? 'Signed in as ' + name : 'Signed in')
      + '. Your completion ticks can follow you to another device.');
    a.classList.add('is-in');
  })();
"""


def esc(text):
    return (text.replace("&", "&amp;").replace("<", "&lt;")
                .replace(">", "&gt;").replace('"', "&quot;"))


def up_to_root(relative):
    """The relative prefix that reaches site/ from a page's own directory."""
    depth = len(pathlib.PurePosixPath(relative).parent.parts)
    return "../" * depth


# --- inventory, read out of the published pages ----------------------------
def strip_tags(fragment):
    return unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", fragment)).strip())


def trading_inventory():
    text = (SITE / PATH_PAGE).read_text(encoding="utf-8")
    courses = []
    for card in re.finditer(r'<article class="course-card"[^>]*>(.*?)</article>', text, re.S):
        link = re.search(r'<h3><a href="\.\./\.\./([a-z0-9-]+)/">(.*?)</a></h3>', card.group(1), re.S)
        if not link:
            continue
        slug = link.group(1)
        courses.append({
            "slug": slug,
            "title": strip_tags(link.group(2)),
            "lessons": course_lessons(slug),
        })
    return courses


def course_lessons(slug):
    text = (SITE / slug / "index.html").read_text(encoding="utf-8")
    lessons = []
    for card in re.finditer(r'<article class="lesson-card"[^>]*>(.*?)</article>', text, re.S):
        link = re.search(r'<a class="lesson-link" href="\./([a-z0-9-]+)/">(.*?)</a>',
                         card.group(1), re.S)
        if not link:
            continue
        label = re.sub(r'<span class="lesson-ord">.*?</span>', "", link.group(2), flags=re.S)
        lessons.append({"slug": link.group(1), "title": strip_tags(label)})
    return lessons


# --- the four edits, each replacing its own marked region ------------------
def ensure_css(text):
    # An existing block is REMOVED and re-inserted, never edited where it sits.
    # Editing in place cannot fix a block that is in the wrong place, and the
    # first version of this patcher put it in one -- so a rerun would have kept
    # the whole feature inside <noscript> forever. Removal restores the file to
    # its unpatched text, which is what keeps this idempotent.
    text = re.sub(r"[ \t]*" + re.escape(CSS_BEGIN) + r".*?" + re.escape(CSS_END) + r"\n?",
                  lambda _m: "", text, flags=re.S)
    aliases = []
    for canonical, legacy in (("--panel-2", "--panel2"), ("--line-strong", "--line2")):
        if not re.search(re.escape(canonical) + r"\s*:", text):
            if not re.search(re.escape(legacy) + r"\s*:", text):
                legacy = "--panel" if canonical == "--panel-2" else "--line"
            aliases.append(canonical + ": var(" + legacy + ");")
    palette = ":root { " + " ".join(aliases) + " }\n" if aliases else ""
    if not re.search(r"--on-accent\s*:", text):
        # The page background already follows both light-theme paths. Reusing
        # its ink keeps the legacy palette coherent without adding a second
        # light declaration or overriding an authored palette value.
        palette += ':root { --on-accent: var(--bg); }\n'
    block = "%s\n%s%s    %s" % (CSS_BEGIN, palette, CSS + UI_CSS, CSS_END)
    # The FIRST style block -- the page's own stylesheet. NOT the last: every
    # one of these pages ends with a <noscript><style> that hides the theme
    # toggle, and rules put there apply only when scripting is OFF. The first
    # version of this patcher used rfind and buried the whole feature in that
    # block, so the toggle and the feedback panel rendered unstyled for every
    # reader who had JavaScript on -- which is everyone who can use them.
    marker = text.find("</style>")
    if marker == -1:
        raise SystemExit("no <style> block to extend")
    # Insert as WHOLE LINES before the closing tag's own line, so the </style>
    # line keeps the indentation it came with. Inserting at the tag itself made
    # the block's column depend on that indentation, while removal above eats
    # it -- so the first rerun moved the block by two spaces and only then
    # settled. Idempotent from the first run is the requirement, not eventually.
    line_start = text.rfind("\n", 0, marker) + 1
    return text[:line_start] + "    " + block + "\n" + text[line_start:]


def ensure_script(text, body):
    block = SCRIPT_OPEN + body + "  " + SCRIPT_CLOSE + "\n"
    if SCRIPT_OPEN in text:
        return re.sub(re.escape(SCRIPT_OPEN) + r".*?" + re.escape(SCRIPT_CLOSE),
                      lambda _m: block.rstrip("\n"), text, count=1, flags=re.S)
    marker = text.rfind("</body>")
    if marker == -1:
        raise SystemExit("no </body> to precede")
    return text[:marker] + "  " + block + text[marker:]


def ensure_masthead(text, relative):
    """The sign-in control, beside the theme toggle, inside one grouped child.

    The masthead is justify-content: space-between, so a bare extra child is
    spread into open space rather than sitting next to the toggle.
    """
    href = up_to_root(relative) + "progress/"
    link = ('<a class="signin-btn" id="signinLink" href="%s" title="%s">'
            '<span class="signin-mark" aria-hidden="true">&#9679;</span>'
            '<span class="signin-label" id="signinLabel">Sign in</span></a>'
            % (esc(href), esc(SIGNIN_TITLE)))
    toggle = re.search(r'<button class="icon-btn" id="themeToggle".*?</button>', text, re.S)
    if toggle is None:
        raise SystemExit("no theme toggle in the masthead")
    if 'class="topbar-actions"' in text:
        # Already grouped: only refresh the link, so a moved page gets the right depth.
        return re.sub(r'<a class="signin-btn" id="signinLink".*?</a>',
                      lambda _m: link, text, count=1, flags=re.S)
    group = '<div class="topbar-actions">%s%s</div>' % (link, toggle.group(0))
    return text[:toggle.start()] + group + text[toggle.end():]


class ElementSpans(HTMLParser):
    """Locate whole elements while leaving every untouched source byte alone."""
    VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input",
            "link", "meta", "param", "source", "track", "wbr"}

    def __init__(self, text):
        super().__init__(convert_charrefs=False)
        self.text = text
        self.starts = [0]
        for line in text.splitlines(keepends=True):
            self.starts.append(self.starts[-1] + len(line))
        self.stack, self.elements, self.copy = [], [], []
        self.feed(text)

    def source_offset(self):
        line, column = self.getpos()
        return self.starts[line - 1] + column

    def handle_starttag(self, tag, attrs):
        start = self.source_offset()
        node = dict(tag=tag, attrs=dict(attrs), start=start,
                    open_end=start + len(self.get_starttag_text()))
        if tag in self.VOID:
            node.update(close_start=node["open_end"], end=node["open_end"])
            self.elements.append(node)
        else:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in self.VOID:
            node = self.stack.pop()
            node.update(close_start=node["open_end"], end=node["open_end"])
            self.elements.append(node)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i]["tag"] == tag:
                node = self.stack[i]
                del self.stack[i:]
                node.update(close_start=self.source_offset(), end=self.text.index(">", self.source_offset()) + 1)
                self.elements.append(node)
                break

    def handle_data(self, data):
        if not any(n["tag"] in ("script", "style") for n in self.stack):
            self.copy.append((self.source_offset(), self.source_offset() + len(data), data))


def element(text, tag, *, cls=None, identity=None):
    found = [n for n in ElementSpans(text).elements if n["tag"] == tag
             and (cls is None or cls in n["attrs"].get("class", "").split())
             and (identity is None or identity == n["attrs"].get("id"))]
    if len(found) != 1:
        raise ValueError("expected one %s.%s#%s, found %d" % (tag, cls, identity, len(found)))
    return found[0]


def replace_element(text, node, replacement):
    return text[:node["start"]] + replacement + text[node["end"]:]


def annotate(text, tag, name, *, cls=None, identity=None):
    node = element(text, tag, cls=cls, identity=identity)
    opening = text[node["start"]:node["open_end"]]
    opening = re.sub(r'\sdata-ui="[^"]*"', '', opening)
    return text[:node["start"]] + opening[:-1] + ' data-ui="%s">' % name + text[node["open_end"]:]


def normalize_taxonomy_copy(text, courses, *, lesson=False):
    """Change curriculum references in prose and accessible copy, never code or URLs."""
    parsed = ElementSpans(text)
    shell = [n for n in parsed.elements if n["tag"] in ("header", "footer", "nav", "title", "meta")]

    def rewrite(value, *, in_shell):
        # A numbered curricular reference has an unambiguous replacement even
        # in teaching prose. An execution "trading path" does not.
        value = re.sub(r'\bcourse\s+([1-8]) of the path\b',
                       lambda m: courses[int(m[1])-1]["title"], value, flags=re.I)
        value = re.sub(r'\bcourse\s+\d+\s+of\s+\d+\b', 'Course', value, flags=re.I)
        value = re.sub(r'\b(?:start|begin)(?: with| at)? lesson\s+\d+(?:\s+of\s+\d+)?', 'Open lesson', value, flags=re.I)
        value = re.sub(r'\bStart lesson\b', 'Open lesson', value, flags=re.I)
        value = re.sub(r'\blesson\s+\d+\s+of\s+\d+\b', 'Lesson', value, flags=re.I)
        value = re.sub(r'\bcourse\s+([1-8])\b', lambda m: courses[int(m[1])-1]["title"], value, flags=re.I)
        if in_shell:
            value = re.sub(r'\bnext course\b', 'Related course', value, flags=re.I)
            value = re.sub(r'\blearning path\b', 'Subject', value, flags=re.I)
            value = re.sub(r'\btrading path\b', 'Trading courses', value, flags=re.I)
        return value
    def in_shell(start):
        return not lesson or any(n["start"] <= start < n["end"] for n in shell)

    edits = []
    for start, end, value in parsed.copy:
        new = rewrite(value, in_shell=in_shell(start))
        if new != value:
            edits.append((start, end, new))
    for node in parsed.elements:
        opening = text[node["start"]:node["open_end"]]
        for attr in ("aria-label", "aria-description", "alt", "title", "placeholder", "content"):
            if attr not in node["attrs"]:
                continue
            opening = re.sub(r'\b' + attr + r'="([^"]*)"',
                             lambda m: attr + '="' + rewrite(m[1], in_shell=in_shell(node['start'])) + '"', opening)
        if opening != text[node["start"]:node["open_end"]]:
            edits.append((node["start"], node["open_end"], opening))
    for start, end, value in sorted(edits, reverse=True):
        text = text[:start] + value + text[end:]
    return text


def normalize_lesson_ui(text, relative, course, lesson):
    """Normalize the authored shell, preserving teaching, illustrations and scripts.

    Only the two verified shell shapes are accepted. A new shape fails during
    preflight, before main() writes any page.
    """
    body = element(text, "body")
    text = text[:body["start"]] + '<body data-page-kind="lesson">' + text[body["open_end"]:]
    main = element(text, "main")
    if main["attrs"].get("class") == "shell":
        text = text[:main["close_start"]] + '</div>' + text[main["end"]:]
        text = text[:main["start"]] + '<div class="shell">' + text[main["open_end"]:]
        hero = element(text, "section", cls="hero")
        text = text[:hero["start"]] + '<main id="main">\n' + text[hero["start"]:]
        boundary = element(text, "div", cls="progress-bar")["start"]
        text = text[:boundary] + '</main>\n    ' + text[boundary:]
    elif main["attrs"].get("id") != "main":
        raise ValueError("%s: unrecognized main landmark" % relative)
    if 'class="skip-link"' not in text:
        text = text.replace('<body data-page-kind="lesson">',
                            '<body data-page-kind="lesson">\n  <a class="skip-link" href="#main">Skip to content</a>', 1)
    header = element(text, "header", cls="topbar")
    old_header = text[header["start"]:header["end"]]
    resets = re.findall(r'<button\b[^>]*id="resetBtn"[^>]*>.*?</button>', old_header, re.S)
    text = replace_element(text, header, chrome.masthead(up_to_root(relative)).strip())
    if resets:
        actions = element(text, "div", cls="hero-actions")
        text = text[:actions["close_start"]] + resets[0] + text[actions["close_start"]:]
    crumb = element(text, "nav", cls="crumbs")
    text = replace_element(text, crumb, chrome.crumbs([
        ("Learn library", "../../"), ("Trading", "../../paths/trading/"),
        (course["title"], "../"), (lesson["title"], None)]).strip())
    title = esc(lesson["title"] + " | Lesson | " + course["title"] + " | Trading | Learn · geterdone.io")
    text = replace_element(text, element(text, "title"), '<title>%s</title>' % title)
    for field in ("og:title", "twitter:title"):
        text = re.sub(r'<meta\s+(?:name|property)="' + field + r'"[^>]*>',
                      lambda m: re.sub(r'content="[^"]*"', lambda _m: 'content="%s"' % title, m[0]), text)
    hero = element(text, "section", cls="hero")
    markup = text[hero["start"]:hero["end"]]
    eyebrow = element(markup, "span", cls="eyebrow")
    markup = replace_element(markup, eyebrow,
        '<span class="eyebrow"><span data-ui="page-kind">Lesson</span> &middot; %s</span>' % esc(course["title"]))
    text = replace_element(text, hero, markup)
    text = annotate(text, "section", "hero", cls="hero")
    text = annotate(text, "div", "primary-actions", cls="hero-actions")
    index = next(i for i, item in enumerate(course["lessons"]) if item["slug"] == lesson["slug"])
    def neighbor(i):
        item = course["lessons"][i]
        return ("../%s/" % item["slug"], "%02d &middot; %s" % (i + 1, esc(item["title"])))
    previous = neighbor(index - 1) if index else None
    following = (*neighbor(index + 1), False) if index + 1 < len(course["lessons"]) else ("../", esc(course["title"]), True)
    text = replace_element(text, element(text, "nav", cls="lesson-nav"), chrome.pager(prev=previous, next=following).strip())
    text = annotate(text, "footer", "footer")
    return text


# One-time migration copy for legacy catalog shells. Once data-ui regions are
# present, the published catalog remains authoritative for its authored prose.
TRADING_OVERVIEWS = {
    "market-structure": ("Read price structure, ranges, liquidity, multi-timeframe context, entry models, invalidation, participation, and options contract selection.", "No trading background is assumed. The lessons introduce chart terminology."),
    "trade-setup-execution": ("Define trade setups, plan entries and exits, size positions, manage trades, and use records to review decisions.", "Price structure, support and resistance, pullbacks, and invalidation levels."),
    "options-trading": ("Read option contracts and chains, calculate expiration payoffs, interpret volatility and the Greeks, and evaluate options strategies.", "Trade planning, position sizing, and basic risk and reward calculations."),
    "technical-indicators": ("Calculate and interpret trend, momentum, volatility, and volume indicators, and evaluate indicator rules.", "Price charts, trend and range structure, and trade planning."),
    "volume-and-order-flow": ("Interpret volume, participation, liquidity, order flow, profiles, and execution evidence alongside price.", "Price structure, trade planning, and the distinction between a signal and a tested rule."),
    "trading-risk-management": ("Set risk budgets, size positions, evaluate portfolio exposure and drawdowns, and document risk decisions.", "Position sizing, trade records, and basic probability and expectancy."),
    "backtesting-and-trading-systems": ("Specify trading rules, design tests, account for data and execution limits, and evaluate system performance.", "Trading rules, risk budgets, trade records, and performance measures."),
    "algorithmic-and-automated-trading": ("Specify automated trading workflows, data and order handling, deployment controls, monitoring, and operational risk procedures.", "Tested trading rules, risk management, and backtesting concepts. Software examples explain their trading context."),
}


def catalog_frame(text, relative, kind, title, description, trail):
    body = element(text, "body")
    text = text[:body["start"]] + '<body data-page-kind="%s">' % kind + text[body["open_end"]:]
    text = replace_element(text, element(text, "header", cls="topbar"), chrome.masthead(up_to_root(relative)).strip())
    text = replace_element(text, element(text, "nav", cls="crumbs"), chrome.crumbs(trail).strip())
    # Metadata is copy, so give search engines the same literal identity.
    context = kind.capitalize() + (" | Trading" if kind == "course" else "")
    text = replace_element(text, element(text, "title"), '<title>%s | %s | Learn · geterdone.io</title>' % (esc(title), context))
    for field, value in (("description", description), ("og:description", description),
                         ("twitter:description", description), ("og:title", title + " | " + context + " | Learn"),
                         ("twitter:title", title + " | " + context + " | Learn")):
        text = re.sub(r'<meta\s+(?:name|property)="' + re.escape(field) + r'"[^>]*>',
                      lambda m: re.sub(r'content="[^"]*"', 'content="%s"' % esc(value), m[0]), text)
    return annotate(text, "footer", "footer")


def course_navigation(courses, index, up="../"):
    links = []
    for offset, direction in ((-1, "prev"), (1, "next")):
        if 0 <= index + offset < len(courses):
            target = courses[index + offset]
            links.append('<a class="path-move %s" href="%s%s/" rel="%s"><span>Related course</span><strong>%s</strong></a>'
                         % (direction, up, target["slug"], direction, esc(target["title"])))
    if index == len(courses) - 1:
        links.append('<a class="path-move next" href="%spaths/trading/"><strong>All Trading courses</strong></a>' % up)
    return '<nav class="path-nav" data-ui="course-navigation" aria-label="Course navigation">%s</nav>' % ''.join(links)


def normalize_course_ui(text, course, courses, index):
    title, slug = course["title"], course["slug"]
    if 'data-ui="overview"' in text:
        # Refresh shared controls without overwriting subsequent authored copy.
        description = next(n["attrs"]["content"] for n in ElementSpans(text).elements
                           if n["tag"] == "meta" and n["attrs"].get("name") == "description")
        text = catalog_frame(text, slug + "/index.html", "course", title, description,
                             [("Learn library", "../"), ("Trading", "../paths/trading/"), (title, None)])
        return replace_element(text, element(text, "nav", cls="path-nav"), course_navigation(courses, index))
    summary, background = TRADING_OVERVIEWS[slug]
    text = catalog_frame(text, slug + "/index.html", "course", title, summary,
                         [("Learn library", "../"), ("Trading", "../paths/trading/"), (title, None)])
    hero = element(text, "section", cls="hero")
    hero_text = text[hero["start"]:hero["end"]]
    left = min((n for n in ElementSpans(hero_text).elements if n["tag"] == "div"), key=lambda n: n["start"])
    hero_text = replace_element(hero_text, left,
        '<div><span class="eyebrow"><span data-ui="page-kind">Course</span> &middot; Trading</span>'
        '<h1 id="hero-title">%s</h1><p>%s</p><div class="hero-actions" data-ui="primary-actions">'
        '<a class="btn primary" href="#lessons">View lessons</a>'
        '<a class="btn ghost" href="#background">Recommended background</a></div></div>' % (esc(title), esc(summary)))
    text = replace_element(text, hero, hero_text)
    text = annotate(text, "section", "hero", cls="hero")
    # Retain old fragment destinations while removing their course-order claims.
    for identity in ("path", "next-course"):
        found = [n for n in ElementSpans(text).elements if n["tag"] == "section" and n["attrs"].get("id") == identity]
        if found:
            text = replace_element(text, found[0], '')
    metadata = ('<section class="section" id="ui-metadata" data-ui="metadata"><dl class="stats">'
                '<div><dt>Subject</dt><dd>Trading</dd></div><div><dt>Lessons</dt><dd>%d</dd></div>'
                '<div><dt>Format</dt><dd>Interactive</dd></div></dl></section>' % len(course["lessons"]))
    if 'id="ui-metadata"' in text:
        text = replace_element(text, element(text, "section", identity="ui-metadata"), metadata)
    else:
        boundary = element(text, "section", cls="hero")["end"]
        text = text[:boundary] + '\n' + metadata + text[boundary:]
    overview = element(text, "section", identity="overview")
    region = text[overview["start"]:overview["end"]]
    heading = element(region, "div", cls="section-head")
    region = replace_element(region, heading,
        '<div class="section-head"><div><h2 id="overview-title">Overview</h2><p>%s</p></div></div>' % esc(summary))
    # Keep the authored topic overview; replace only audience and completion-order advice.
    cards = sorted([n for n in ElementSpans(region).elements if n["tag"] == "article" and 'note-card' in n["attrs"].get('class','').split()], key=lambda n:n['start'])
    for n in reversed(cards[1:]):
        old = region[n['start']:n['end']]
        label = re.search(r'<h3[^>]*>(.*?)</h3>', old, re.S)
        if label and ('Who' in label[1] or 'How' in label[1]):
            body = background if 'Who' in label[1] else 'Use the explanations, examples, interactive controls, and practice questions for the topics you want to study. Completion marks are optional.'
            heading_text = 'Background' if 'Who' in label[1] else 'Using the lessons'
            region = replace_element(region,n,'<article class="note-card"><h3>%s</h3><p>%s</p></article>' % (heading_text,esc(body)))
    text = replace_element(text, overview, region)
    text = annotate(text, "section", "overview", identity="overview")
    lessons = element(text, "section", identity="lessons")
    region = text[lessons['start']:lessons['end']]
    region = replace_element(region,element(region,"div",cls="section-head"),
        '<div class="section-head"><div><h2 id="lessons-title">Lessons</h2><p>Explanations, examples, interactive tools, and practice questions.</p></div><p class="count-chip">%d lessons</p></div>' % len(course["lessons"]))
    text=replace_element(text,lessons,region)
    text=annotate(text,"section","lesson-list",identity="lessons")
    background_markup = ('<section class="section prose" id="background" data-ui="background">'
        '<span id="path"></span><span id="next-course"></span>'
        '<h2 id="path-title">Recommended background</h2><p>%s</p></section>' % esc(background))
    if 'id="background"' in text:
        text=replace_element(text,element(text,"section",identity="background"),background_markup)
    else:
        boundary=element(text,"section",identity="lessons")['end']
        text=text[:boundary]+'\n'+background_markup+text[boundary:]
    text=replace_element(text,element(text,"nav",cls="path-nav"),course_navigation(courses,index))
    # Numbered cross-course references in overview/resource copy use their titles.
    main=element(text,"main"); region=text[main['start']:main['end']]
    region=re.sub(r'\bcourse\s+[1-8]\s+of\s+8\b', 'Course', region, flags=re.I)
    region=re.sub(r'\bcourse\s+([1-8])\b',lambda m: esc(courses[int(m[1])-1]['title']),region,flags=re.I)
    region=re.sub(r'\bStart lesson\s+\d+\s+of\s+\d+\b','Open lesson',region,flags=re.I)
    region=region.replace('PATH ENDS','AUTOMATION')
    region=region.replace('The last lesson of the last course is not a quiz you pass and close.',
                          'The specification lesson documents an automated trading system.')
    region=re.sub(r'\b[Tt]rading path\b','Trading courses',region)
    region=re.sub(r'<span class="level">\s*\d+ of \d+\s*</span>', '', region)
    region=region.replace('Three lessons in strict dependency order, and the order is the point. ', '')
    region=region.replace('The finish, and the two questions left.', 'AI workflows and system specifications.')
    region=region.replace('The last lesson is not a quiz you pass and close.', 'The specification lesson documents a trading system.')
    text=replace_element(text,main,region)
    return text


def normalize_subject_ui(text, courses):
    if 'data-ui="course-list"' in text:
        description = next(n["attrs"]["content"] for n in ElementSpans(text).elements
                           if n["tag"] == "meta" and n["attrs"].get("name") == "description")
        return catalog_frame(text, PATH_PAGE, "subject", "Trading", description,
                             [("Learn library", "../../"), ("Trading", None)])
    description = 'Trading courses on price structure, trade planning, options, indicators, order flow, risk, backtesting, and automation.'
    text=catalog_frame(text,PATH_PAGE,"subject","Trading",description,
                       [("Learn library","../../"),("Trading",None)])
    capstone=element(text,"section",identity="capstone")
    capstone_text=text[capstone['start']:capstone['end']].replace('the way this path teaches it', 'using the methods covered in these courses')
    cards=''.join('<article class="course-card" data-course="%s" data-lessons="%d">'
        '<h3><a href="../../%s/">%s</a></h3><p>%s</p><div class="meta-row"><span class="chip">%d lessons</span></div>'
        '<span class="course-progress-note"></span></article>'
        % (c['slug'],len(c['lessons']),c['slug'],esc(c['title']),esc(TRADING_OVERVIEWS[c['slug']][0]),len(c['lessons'])) for c in courses)
    main='''<main id="main">
      <section class="hero" data-ui="hero"><div><span class="eyebrow"><span data-ui="page-kind">Subject</span> &middot; Learn library</span>
      <h1 id="hero-title">Trading</h1><p>%s</p><div class="hero-actions" data-ui="primary-actions"><a class="btn primary" href="#courses">View courses</a><a class="btn ghost" href="#background">Recommended background</a></div></div></section>
      <section class="section" data-ui="metadata"><dl class="stats"><div><dt>Courses</dt><dd>%d</dd></div><div><dt>Lessons</dt><dd>%d</dd></div><div><dt>Format</dt><dd>Interactive</dd></div></dl></section>
      <section class="section prose" id="outcomes" data-ui="overview"><h2 id="outcomes-title">Overview</h2><p>Study market observations, trade decisions, and the methods used to test and manage them. Course examples and labs use synthetic data.</p></section>
      <section class="section" id="courses" data-ui="course-list"><div class="section-head"><div><h2 id="courses-title">Courses</h2><p>Choose a course by topic. Each course lists recommended background and its lessons.</p></div></div><div class="subject-courses">%s</div></section>
      <section class="section prose" id="background" data-ui="background"><h2>Recommended background</h2><p>Market Structure introduces chart terminology. Other courses identify the chart, planning, risk, or testing concepts useful for their topics.</p></section>
      %s
    </main>''' % (esc(description),len(courses),sum(len(c['lessons']) for c in courses),cards,capstone_text)
    return replace_element(text,element(text,"main"),main)


def ensure_lesson_toggle(text, lesson_id, relative):
    markup = (
        '\n    <div class="progress-bar" data-ui="progress">\n'
        '      <button class="progress-toggle" id="progressToggle" type="button" aria-pressed="false">\n'
        '        <span class="progress-tick" aria-hidden="true">&#10003;</span>'
        '<span id="progressLabel">Mark this lesson complete</span>\n'
        '      </button>\n'
        '      <p class="progress-note">Kept in this browser only, for you. Nothing is sent anywhere '
        'and nothing checks it.\n'
        '        <a href="%sprogress/">Carry it to another device</a>.</p>\n'
        '    </div>\n' % up_to_root(relative)
    )
    if 'id="progressToggle"' in text:
        return re.sub(r'\n    <div class="progress-bar"(?: data-ui="progress")?>.*?\n    </div>\n',
                      lambda _m: markup, text, count=1, flags=re.S)
    anchor = text.find('<nav class="lesson-nav"')
    if anchor == -1:
        raise SystemExit("no lesson pager to precede")
    line_start = text.rfind("\n", 0, anchor) + 1
    return text[:line_start] + markup.lstrip("\n") + "\n" + text[line_start:]


def ensure_feedback_panel(text, lesson_id, lesson_title, course_title):
    """The recommendations panel, at the foot of the lesson.

    Placed after the pager and before the footer, which is where the generated
    lessons put it: past the material and the completion mark, so it reads as
    "now that you have been through this", not as a form to fill in first.
    """
    markup = feedback.MARKUP % {
        "id": esc(lesson_id),
        "lesson": esc(lesson_title),
        "course": esc(course_title),
    }
    if 'id="lessonFeedback"' in text:
        return re.sub(r'\n    <section class="lesson-feedback".*?\n    </section>\n',
                      lambda _m: markup, text, count=1, flags=re.S)
    # Anchored on the pager, not on the footer: the seven market-structure
    # lessons close with a bare <footer> and the rest with <footer class="footer">,
    # so the footer is not a reliable landmark. Every lesson page has the pager --
    # the completion toggle above is placed by finding it.
    nav = text.find('<nav class="lesson-nav"')
    if nav == -1:
        raise SystemExit("no lesson pager to follow")
    close = text.find("</nav>", nav)
    if close == -1:
        raise SystemExit("unterminated lesson pager")
    close += len("</nav>")
    return text[:close] + "\n" + markup + text[close:]


def clean_catalog_spacing(text):
    # Section removal can leave an indentation-only line. Normalize only
    # whitespace text nodes in the catalog main; scripts/styles are excluded.
    main = element(text, "main")
    edits = [(start, end, re.sub(r"(?m)^[ \t]+(?=\n)", "", value))
             for start, end, value in ElementSpans(text).copy
             if main["start"] <= start < main["end"] and not value.strip()]
    for start, end, value in sorted(edits, reverse=True):
        text = text[:start] + value + text[end:]
    return text


def ensure_course_hooks(text, course_slug, lessons):
    """data-lesson on each lesson card, and one line saying how many are done."""
    by_slug = {l["slug"]: l for l in lessons}
    seen = []

    def stamp(match):
        head, body = match.group(1), match.group(2)
        link = re.search(r'<a class="lesson-link" href="\./([a-z0-9-]+)/">', body)
        if not link or link.group(1) not in by_slug:
            return match.group(0)
        slug = link.group(1)
        seen.append(slug)
        head = re.sub(r'\s+data-lesson="[^"]*"', "", head)
        body = re.sub(r'<span class="lesson-state">.*?</span>', '', body, flags=re.S)
        body = re.sub(r"(?m)^[ \t]+$", "", body)
        content = element(body, "div", cls="lesson-body")
        body = body[:content["close_start"]] + '<span class="lesson-state">Not marked</span>' + body[content["close_start"]:]
        return '<article class="lesson-card"%s data-lesson="%s/%s">%s</article>' % (
            head, course_slug, slug, body)

    text = re.sub(r'<article class="lesson-card"([^>]*)>(.*?)</article>', stamp, text, flags=re.S)
    if len(seen) != len(lessons):
        raise SystemExit("%s: stamped %d of %d lesson cards" % (course_slug, len(seen), len(lessons)))

    line = '<p class="course-progress" id="courseProgress">None of the %d lessons marked complete</p>\n\n          ' % len(lessons)
    if 'id="courseProgress"' in text:
        return re.sub(r'<p class="course-progress" id="courseProgress">.*?</p>',
                      lambda _m: line.strip(), text, count=1, flags=re.S)
    anchor = text.find('<ol class="course-track"')
    if anchor == -1:
        raise SystemExit("%s: no course track to precede" % course_slug)
    return text[:anchor] + line + text[anchor:]


def ensure_path_hooks(text, courses):
    """data-course/data-lessons on each course card, and a line for its count."""
    counts = {c["slug"]: len(c["lessons"]) for c in courses}
    seen = []

    def stamp(match):
        head, body = match.group(1), match.group(2)
        link = re.search(r'<h3><a href="\.\./\.\./([a-z0-9-]+)/">', body)
        if not link or link.group(1) not in counts:
            return match.group(0)
        slug = link.group(1)
        seen.append(slug)
        head = re.sub(r'\s+data-(course|lessons)="[^"]*"', "", head)
        if 'class="course-progress-note"' not in body:
            body = body.rstrip() + '\n              <span class="course-progress-note"></span>\n            '
        return '<article class="course-card"%s data-course="%s" data-lessons="%d">%s</article>' % (
            head, slug, counts[slug], body)

    text = re.sub(r'<article class="course-card"([^>]*)>(.*?)</article>', stamp, text, flags=re.S)
    if len(seen) != len(courses):
        raise SystemExit("path page: stamped %d of %d course cards" % (len(seen), len(courses)))
    return text


def prepare_lesson(before, relative, course, lesson, courses):
    lesson_id = '"%s/%s"' % (course["slug"], lesson["slug"])
    text = ensure_css(before)
    text = ensure_lesson_toggle(text, lesson_id, relative)
    text = normalize_lesson_ui(text, relative, course, lesson)
    text = annotate(text, "div", "progress", cls="progress-bar")
    text = ensure_feedback_panel(text, "%s/%s" % (course["slug"], lesson["slug"]),
                                 lesson["title"], course["title"])
    text = ensure_script(text, progress.PROGRESS_JS + (progress.LESSON_JS % lesson_id)
                         + feedback.STORE_JS + feedback.LESSON_JS + SIGNIN_JS)
    # Remove the curricular prefix from the footer before resolving references,
    # so "Course 8 · <title>" retains exactly one course identity.
    footer = element(text, "footer")
    copy = text[footer["start"]:footer["end"]]
    copy = re.sub(r'Course [1-8] (?:·|&middot;|&#183;) ', '', copy)
    text = replace_element(text, footer, copy)
    return normalize_taxonomy_copy(text, courses, lesson=True)


def main():
    courses = trading_inventory()
    identities = [c["slug"] + "/" + lesson["slug"] for c in courses for lesson in c["lessons"]]
    # Frozen published scope for this migration. New curriculum requires updating
    # the URL declarations as well as this preflight, not silently shrinking it.
    if (len(courses), len(identities), len(set(identities))) != (8, 118, 118):
        raise ValueError("incomplete or duplicate Trading inventory; expected 8 courses and 118 distinct lessons")
    changed = 0
    touched = 0
    pending = []

    def save(relative, text, before):
        nonlocal changed, touched
        touched += 1
        if text != before:
            pending.append((SITE / relative, text))
            changed += 1

    # Lessons: the toggle, the masthead control, the styles and the scripts.
    for course_index, course in enumerate(courses):
        for lesson in course["lessons"]:
            relative = "%s/%s/index.html" % (course["slug"], lesson["slug"])
            before = (SITE / relative).read_text(encoding="utf-8")
            text = prepare_lesson(before, relative, course, lesson, courses)
            save(relative, text, before)

        # Course home: a tick against each lesson it lists, and a count.
        relative = "%s/index.html" % course["slug"]
        before = (SITE / relative).read_text(encoding="utf-8")
        text = ensure_css(before)
        text = normalize_course_ui(text, course, courses, course_index)
        text = ensure_course_hooks(text, course["slug"], course["lessons"])
        text = ensure_script(text, progress.PROGRESS_JS + COURSE_JS + SIGNIN_JS)
        text = normalize_taxonomy_copy(text, courses)
        text = clean_catalog_spacing(text)
        save(relative, text, before)

    # The path page: the same count, per course, on its spine.
    before = (SITE / PATH_PAGE).read_text(encoding="utf-8")
    text = ensure_css(before)
    text = normalize_subject_ui(text, courses)
    text = ensure_path_hooks(text, courses)
    text = ensure_script(text, progress.PROGRESS_JS + PATH_JS + SIGNIN_JS)
    text = normalize_taxonomy_copy(text, courses)
    save(PATH_PAGE, text, before)

    before = (SITE / "index.html").read_text(encoding="utf-8")
    text = ensure_css(before)
    text = annotate(text, "footer", "footer")
    save("index.html", text, before)

    # The capstone pages are not lessons -- they belong to no course's list and
    # so are not tickable and not in any denominator. They still get the way in
    # to /progress/, because every other page a reader can land on has one.
    for relative in ("paths/trading/iren-analysis-2026-08-16/index.html",
                     "paths/trading/iren-analysis-2026-08-16/slides/index.html"):
        if not (SITE / relative).exists():
            continue
        before = (SITE / relative).read_text(encoding="utf-8")
        text = ensure_css(before)
        text = ensure_masthead(text, relative)
        text = ensure_script(text, SIGNIN_JS)
        save(relative, text, before)

    # Structural errors anywhere above must leave the complete source tree alone.
    for target, text in pending:
        target.write_text(text, encoding="utf-8")
    lessons = sum(len(c["lessons"]) for c in courses)
    print("Trading path: %d courses, %d lessons now tickable." % (len(courses), lessons))
    print("%d page(s) visited, %d rewritten." % (touched, changed))


if __name__ == "__main__":
    main()
