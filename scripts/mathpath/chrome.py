"""The shared frame: <head>, masthead, breadcrumb, pager, footer.

Everything the library pins across course boundaries is written HERE, once:
the two light paths, the pre-paint theme read, the theme toggle markup, the
lesson pager markup, and the footer identity line. A page cannot drift from a
convention it does not spell out itself.
"""

import html

from .theme import stylesheet

CANONICAL_ORIGIN = "https://learn.geterdone.io"

# The educational-use line every course page of this path carries.
#
# The trading path pins "charts are synthetic examples, not trade signals",
# which is the claim a reader of THAT material relies on. It would be a
# meaningless sentence here -- there are no charts of anything and nothing to
# signal -- and a disclaimer that does not apply is worse than none, because it
# is the sentence a reader trusts.
#
# What a reader of THIS material needs told is different and is two claims,
# both true and both checkable:
#
#   * every figure on the page is computed in the browser from the stated
#     definition, so nothing here is a number someone typed in and hoped was
#     right (the labs enumerate, count and verify; none of them ships a
#     precomputed answer);
#   * a worked example is not a proof. That is the actual intellectual hazard
#     of learning discrete mathematics from interactive examples: a widget that
#     checks a claim for n = 1..40 has demonstrated nothing about n = 41, and
#     the whole point of course 3 is why.
# The clause after the licence names the INTELLECTUAL HAZARD of the subject,
# and every subject has its own. Hard-coding discrete mathematics' hazard here
# was correct while it was the only generated path; the moment a second one
# arrived, that sentence became false on its pages -- and a disclaimer that is
# false is worse than none, because it is the sentence a reader trusts. So each
# path states its own, and the site invariants assert that a path never carries
# another path's.
LICENCE_HEAD = (
    "&copy; 2026 dmedellin &middot; Released under the MIT License &middot; "
    "Educational use only &mdash; "
)


def licence(material):
    return LICENCE_HEAD + material

# The theme toggle, verbatim from the library's pinned form. The label is
# STATIC and direction-neutral so it is accurate in both states.
THEME_TOGGLE = (
    '<button class="icon-btn" id="themeToggle" type="button" '
    'aria-label="Toggle light and dark theme" title="Toggle theme">&#9790;</button>'
)

# The sign-in control, in the masthead of every page.
#
# It exists because the only door into /progress/ used to be one sentence of
# body copy under a lesson's completion button, reading "Carry it to another
# device" -- which names a benefit, not an action, and does not read as a
# sign-in to anyone looking for one. A reader who wants to sign in has to be
# able to SEE that they can, from anywhere, without already knowing the feature
# is there.
#
# The label is "Sign in" with no script and stays "Sign in" until a session is
# actually found, so the no-JS rendering is the honest one rather than a
# degraded one. The title is not decoration: this library locks nothing, and a
# masthead sign-in on a site that grants no access is a promise that has to be
# corrected the moment it is made.
SIGNIN_TITLE = (
    "Optional. Signing in carries your completion ticks to your other "
    "devices; it unlocks nothing, because nothing here is locked."
)


def signin_control(href, *, current=False):
    if href is None:
        return ""
    return (
        '<a class="signin-btn" id="signinLink" href="%s" title="%s"%s>'
        '<span class="signin-mark" aria-hidden="true">&#9679;</span>'
        '<span class="signin-label" id="signinLabel">Sign in</span></a>'
        % (esc(href), esc(SIGNIN_TITLE), ' aria-current="page"' if current else "")
    )


# Reads the session the two auth pages write and, if one is there, puts the
# account's own name in the masthead. Same-origin sessionStorage only -- this
# sends nothing and asks nothing, so it holds on every page in the library
# without touching the self-containment rule. Failure is silent and leaves the
# static "Sign in" in place: a masthead is not worth a thrown exception.
SIGNIN_SCRIPT = """
    (function () {
      var a = document.getElementById('signinLink');
      if (!a) return;
      var s = null;
      try { s = JSON.parse(sessionStorage.getItem('learn-auth') || 'null'); }
      catch (e) { return; }
      if (!s || !s.access_token) return;
      var label = document.getElementById('signinLabel');
      var name = null;
      /* Same read the progress page does: the ID token names the account, for
         display only. Nothing here trusts it for authorisation, because there
         is nothing to authorise. */
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
    }());
"""

# The pre-paint read. Same key as every other page in the library, and it runs
# in <head> so the chosen theme is applied before the first paint rather than
# flashing the other one. The allowlist matters: a corrupt stored value written
# straight onto data-theme matches no CSS while still counting as an explicit
# choice, which pins the page to dark.
PREPAINT = """  <script>
    (function () {
      try {
        var t = localStorage.getItem('learn-theme');
        if (t === 'light' || t === 'dark') document.documentElement.dataset.theme = t;
      } catch (e) { /* Storage can be unavailable (private mode, file://). */ }
    })();
  </script>"""

THEME_SCRIPT = """
    /* Theme toggle. Same control, same key ('learn-theme'), same static label
       as every other page in the library. The button's accessible name is never
       rewritten from script: a label that describes state has to choose between
       naming the current theme and the next one, and courses chose differently. */
    (function () {
      var root = document.documentElement;
      var toggle = document.getElementById('themeToggle');
      var KEY = 'learn-theme';
      var mql = window.matchMedia('(prefers-color-scheme: light)');
      function stored() {
        try { return localStorage.getItem(KEY); } catch (e) { return null; }
      }
      function resolved() {
        var t = root.dataset.theme;
        if (t === 'light' || t === 'dark') return t;
        return mql.matches ? 'light' : 'dark';
      }
      function paintIcon() { toggle.textContent = resolved() === 'light' ? '\\u2600' : '\\u263E'; }
      toggle.addEventListener('click', function () {
        var next = resolved() === 'light' ? 'dark' : 'light';
        root.dataset.theme = next;
        try { localStorage.setItem(KEY, next); } catch (e) { /* Storage can be unavailable. */ }
        paintIcon();
      });
      if (typeof mql.addEventListener === 'function') {
        mql.addEventListener('change', function () { if (!stored()) paintIcon(); });
      }
      paintIcon();
    })();
"""

# Favicons: inline data-URI SVG, no external asset. One mark family (cyan
# gradient tile, dark ink) with a per-level motif, so the three levels of the
# site stay distinguishable in a tab strip.
_TILE = (
    "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
    "%3Cdefs%3E%3ClinearGradient id='g' x1='0' y1='0' x2='1' y2='1'%3E"
    "%3Cstop offset='0' stop-color='%238ff3ff'/%3E"
    "%3Cstop offset='1' stop-color='%2336d6e7'/%3E%3C/linearGradient%3E%3C/defs%3E"
    "%3Crect width='64' height='64' rx='15' fill='url(%23g)'/%3E{ink}%3C/svg%3E"
)

# Path level: a small graph -- four nodes, three edges. The discrete object the
# path spends a whole course on, and the one picture that says "not continuous".
FAVICON_PATH = _TILE.format(
    ink="%3Cg stroke='%23041116' stroke-width='4' stroke-linecap='round'%3E"
    "%3Cpath d='M17 20L46 20'/%3E%3Cpath d='M17 20L17 45'/%3E%3Cpath d='M17 45L46 20'/%3E%3C/g%3E"
    "%3Cg fill='%23041116'%3E%3Ccircle cx='17' cy='20' r='6.5'/%3E"
    "%3Ccircle cx='46' cy='20' r='6.5'/%3E%3Ccircle cx='17' cy='45' r='6.5'/%3E"
    "%3Ccircle cx='46' cy='47' r='6.5'/%3E%3C/g%3E"
)
# Course level: the "for all" quantifier, upside-down A.
FAVICON_COURSE = _TILE.format(
    ink="%3Cg fill='none' stroke='%23041116' stroke-width='6' stroke-linecap='round'"
    " stroke-linejoin='round'%3E%3Cpath d='M20 17L32 47L44 17'/%3E"
    "%3Cpath d='M25 32L39 32'/%3E%3C/g%3E"
)
# Lesson level: "therefore", the three dots that open the last line of a proof.
FAVICON_LESSON = _TILE.format(
    ink="%3Cg fill='%23041116'%3E%3Ccircle cx='32' cy='20' r='6'/%3E"
    "%3Ccircle cx='20' cy='43' r='6'/%3E%3Ccircle cx='44' cy='43' r='6'/%3E%3C/g%3E"
)


def esc(text):
    """HTML-escape a plain string for text content or an attribute value."""
    return html.escape(str(text), quote=True)


def head(*, title, description, canonical_path, favicon, og_description=None,
         extra_css="", page_kind="auth"):
    """The <head> of any page on this path.

    canonical_path is the published directory URL ("/paths/discrete-math/").
    The canonical, og:url and twitter:url tags are the only absolute URLs a
    page carries; they describe the document rather than load anything.
    """
    url = CANONICAL_ORIGIN + canonical_path
    social = og_description or description
    return """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <link rel="canonical" href="{url}" />
  <meta name="author" content="dmedellin" />

  <!-- Favicon: inline data-URI SVG, no external asset. -->
  <link rel="icon" href="data:image/svg+xml,{favicon}" />

  <meta name="theme-color" content="#071019" media="(prefers-color-scheme: dark)" />
  <meta name="theme-color" content="#edf4f8" media="(prefers-color-scheme: light)" />

  <!-- og:image is deliberately OMITTED: a share card needs an absolute hosted
       image URL and this page is self-contained. -->
  <meta property="og:type" content="article" />
  <meta property="og:site_name" content="Learn &middot; geterdone.io" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{social}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:locale" content="en_US" />
  <meta name="twitter:card" content="summary" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{social}" />
  <meta name="twitter:url" content="{url}" />

  <style>{css}{extra_css}  </style>

{prepaint}
</head>
<body data-page-kind="{page_kind}">
  <a class="skip-link" href="#main">Skip to content</a>
""".format(
        title=esc(title),
        description=esc(description),
        social=esc(social),
        url=url,
        favicon=favicon,
        css=stylesheet(),
        extra_css=extra_css,
        prepaint=PREPAINT,
        page_kind=esc(page_kind),
    )


def masthead(up, *, current=False):
    """Global navigation. Page identity belongs in the breadcrumb and hero."""
    return """    <header class="topbar" data-ui="masthead">
      <a class="brand" href="{up}" aria-label="Learn library">
        <span class="brand-mark" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" focusable="false"><path d="M3 5h7l2 2 2-2h7v15h-7l-2 1-2-1H3z" /><path d="M12 7v14" /></svg></span>
        <span class="brand-copy"><strong>Learn</strong></span>
      </a>
      <nav class="topnav" aria-label="Primary">
        <a href="{up}#paths">Subjects</a>
        <a href="{up}#courses">Courses</a>
        <a href="{up}progress/"{current}>Progress</a>
      </nav>
      <div class="topbar-actions">{signin}{toggle}</div>
    </header>
""".format(up=esc(up), current=' aria-current="page"' if current else "",
           signin=signin_control(up + "progress/", current=current), toggle=THEME_TOGGLE)


def topbar(*, up, current=False):
    """Open the shared shell and its global masthead."""
    return '  <div class="shell">\n' + masthead(up, current=current)


def crumbs(trail):
    """Breadcrumb. trail is [(label, href or None)]; None marks the current page."""
    parts = []
    for label, href in trail:
        if parts:
            parts.append('<span class="crumb-sep" aria-hidden="true">/</span>')
        if href is None:
            parts.append(
                '<span class="crumb-current" aria-current="page">%s</span>' % esc(label)
            )
        else:
            parts.append('<a href="%s">%s</a>' % (esc(href), esc(label)))
    return (
        '    <nav class="crumbs" data-ui="breadcrumbs" aria-label="Breadcrumb">\n      '
        + "\n      ".join(parts)
        + "\n    </nav>\n"
    )


def noscript(message):
    return (
        '\n    <noscript>\n      <div class="noscript-note">%s</div>\n    </noscript>\n'
        % message
    )


# The lesson pager, in the library's pinned form. Class names are exactly
# lesson-nav / lesson-link prev / lesson-link next; each anchor carries only
# class, href and rel; the body is <span>kind</span><strong>literal title</strong>.
# The FIRST lesson omits the prev anchor entirely rather than shipping a
# disabled one, and the LAST lesson's forward link points at the course home
# and carries NO rel, because the course home is not the next document.
def pager(*, prev=None, next=None):
    rows = []
    if prev:
        href, label = prev
        rows.append(
            '      <a class="lesson-link prev" href="%s" rel="prev">'
            "<span>Lesson</span><strong>%s</strong></a>" % (esc(href), label)
        )
    if next:
        href, label, is_terminal = next
        rel = "" if is_terminal else ' rel="next"'
        direction = "Course" if is_terminal else "Lesson"
        rows.append(
            '      <a class="lesson-link next" href="%s"%s>'
            "<span>%s</span><strong>%s</strong></a>" % (esc(href), rel, direction, label)
        )
    return (
        '\n    <nav class="lesson-nav" data-ui="lesson-navigation" aria-label="Course and lesson links">\n'
        + "\n".join(rows)
        + "\n    </nav>\n"
    )


def footer(lead_html, material):
    """The footer. Every page names this library at its own host.

    geterdone.io is a separate live site this project does not control, so a
    footer link there would walk the reader off the library from every page at
    once; the only host any footer names is learn.geterdone.io.

    `material` is the owning path's hazard clause; it is required rather than
    defaulted, so a new path cannot inherit another subject's disclaimer by
    forgetting to state its own.
    """
    return """
    <footer class="footer" data-ui="footer">
      <p>{lead}</p>
      <p>{licence}</p>
      <p><a href="{origin}">learn.geterdone.io</a></p>
    </footer>
  </div>
""".format(lead=lead_html, licence=licence(material), origin=CANONICAL_ORIGIN)


def close(scripts):
    return "  <script>%s%s%s  </script>\n</body>\n</html>\n" % (
        THEME_SCRIPT, SIGNIN_SCRIPT, scripts)


def name_horizontal_scrollers(text):
    """Give authored table/notation/SVG overflow owners a keyboard stop and name.

    Parse actual tags so JavaScript strings and instructional examples stay
    untouched. A lab stage is included only when its actual markup owns an SVG.
    Existing names and native keyboard semantics take precedence.
    """
    from html.parser import HTMLParser

    offsets = [0]
    for line in text.splitlines(keepends=True):
        offsets.append(offsets[-1] + len(line))
    edits = {}

    class Scrollers(HTMLParser):
        VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
                'link', 'meta', 'param', 'source', 'track', 'wbr'}

        def __init__(self):
            super().__init__()
            self.stack = []

        def add(self, tag, attrs, label, at):
            if at in edits:
                return
            extra = ''
            if 'tabindex' not in attrs:
                extra += ' tabindex="0"'
            if not any(k in attrs for k in ('aria-label', 'aria-labelledby')):
                extra += (' role="region"' if tag != 'table' else '') + ' aria-label="%s"' % label
            if extra:
                edits[at] = edits.get(at, '') + extra

        def handle_starttag(self, tag, attrs):
            attrs = dict(attrs)
            classes = attrs.get('class', '').split()
            label = next((name for cls, name in (
                ('mathblock', 'Mathematical notation'), ('table-wrap', 'Data table'),
                ('data-table', 'Data table'), ('heatmap-wrap', 'Sensitivity grid'),
                ('calc-table', 'Calculation table'), ('schema-output', 'Exported plan data'),
                ('footprint', 'Bid and ask volume by price'),
                ('market-chart-scroll', 'Interactive chart; scroll horizontally for complete chart labels')
            ) if cls in classes), None)
            line, column = self.getpos()
            at = offsets[line - 1] + column + len(self.get_starttag_text()) - 1
            if label:
                self.add(tag, attrs, label, at)
            if tag == 'svg':
                owner = next((row for row in reversed(self.stack)
                              if 'lab-stage' in row[1]), None)
                if owner:
                    self.add(owner[0], owner[2],
                             'Interactive diagram; scroll horizontally for complete labels',
                             owner[3])
            if tag not in self.VOID:
                self.stack.append((tag, classes, attrs, at))

        def handle_endtag(self, tag):
            for index in range(len(self.stack) - 1, -1, -1):
                if self.stack[index][0] == tag:
                    self.stack = self.stack[:index]
                    return

    Scrollers().feed(text)
    for at, extra in sorted(edits.items(), reverse=True):
        text = text[:at] + extra + text[at:]
    return text
