"""Strings and Pattern Matching -- seven modes over one text and one pattern.

WHAT THIS KIT PROVES, and what it only measures. Every figure on these pages is
a CHARACTER COMPARISON actually made, produced by running the matcher in the
reader's browser over the text in the box. That is a measurement of one input.
The bound beside it -- m(n - m + 1) for naive matching, 2n for Knuth-Morris-
Pratt, 2m for the failure function's inner loop, exactly n transitions for the
automaton -- is a statement about every input, and this Subject's whole hazard
is the step from the first to the second. So every mode prints both, and the
two presets that matter most on each page are the one where they nearly meet
and the one where they are far apart.

THE THREE THINGS THE COURSE TURNS ON, and where each is made visible:

  naive matching is quadratic and usually is not, and the two tables on
    `naive` are careful about which is which. The first repeats the reader's
    text 1 to 6 times with the PATTERN UNCHANGED, so n grows and m does not;
    both the count and the bound are then linear in n and the only thing that
    separates one text from another is the constant, which is why that table's
    column is comparisons per character. The quadratic needs m to grow WITH n,
    and the second table is the family that does it -- text a^(2m), pattern
    a^(m-1)b -- where the count equals the bound in every row and the
    per-character column rises without limit while KMP's stays flat. Saying
    "quadratic" about the first table would have been false, and it was, until
    the numbers were printed.
  the failure function is built, not quoted. `kmp` builds fail[] one character
    at a time and, in the same table, computes the longest proper border of
    every prefix by TRYING EVERY LENGTH and comparing the two strings. The
    amortised claim is checked as a count: the inner loop's total iterations
    against 2m.
  a rolling hash collides. `rabin` opens on a modulus at which the reader's own
    text produces spurious hits -- windows whose hash equals the pattern's and
    whose characters do not -- and lists them, so the reader can read the
    colliding window off the page and check it by eye. It then runs the same
    text at every prime modulus under 200 and prints how many of the 46
    collide. On the opening preset 18 of them do, and the largest is 137 while
    11 is clean, so the sweep also says the thing a threshold story would hide:
    collisions do not switch off above some size. Nothing on that page says
    collisions are rare; it says how many there were, and at which moduli.

WHAT IS COMPUTED AND WHAT IS CHECKED AGAINST SOMETHING ELSE. `algo_core`'s
STRINGS_JS holds the algorithms and nothing here reimplements one. What this
kit adds is the CHECKING, and the oracle is the same on every page: the
definition of a match.

  skBrute(t, p)       every offset from 0 to n - m, compared as whole strings
                      with ===. Six routines on these pages report match
                      positions -- naiveRun, kmpRun, horspoolRun, rollingHash,
                      ahoRun and dfaRun -- and every one of them is checked
                      against this on every redraw, on the reader's own text.
                      A matcher that skips too far returns a SHORTER list of
                      positions, which is exactly the failure that looks like
                      a correct answer.
  skBorderBrute(p)    the longest proper border of every prefix, found by
                      trying all lengths and comparing the prefix with the
                      suffix. `failureFn` computes the same array in linear
                      time; the page prints both columns.
  skSuffixBrute(s)    the suffix array by sorting the suffixes as strings, and
                      the LCP array by comparing characters one at a time,
                      against prefix doubling and Kasai.
  skPrefixBrute(w, q) the words with a given prefix, by filtering the list,
                      against walking the trie.
  skHashOf(s, b, m)   one window's hash computed from scratch in BigInt,
                      against the value the rolling update carried forward.
                      The rolling update is the only place on these pages
                      where an answer is derived from a previous answer
                      instead of from the input, so it is the only place that
                      can drift silently.

The hashes are BigInt, which matters more than it looks: a lesson whose subject
is that two windows collide cannot have the collision depend on the reader's
machine. Every hash on the page is the same number everywhere.

THE MODES, and the figure each one is for:

  naive      comparisons per alignment, measured, against sigma/(sigma - 1) for
             a uniform alphabet and against m(n - m + 1); then the same count
             at six text lengths with m held fixed, which is linear whatever
             the text; then the family with m growing, which is not
  kmp        the failure function built character by character beside the
             longest border found by trying every length; inner-loop
             iterations against 2m; the match run against naive on the same text
  horspool   the shift table, the characters skipped, the alignments examined,
             and the input where every shift is 1 and the skipping stops
  rabin      every window's hash, the windows that collided, the characters
             spent verifying them, and how many of the 46 primes under 200
             collide on this same text
  trie       nodes against the array slots a dense implementation would take,
             prefix queries against filtering the list, and one Aho-Corasick
             pass against k separate KMP runs
  suffix     the prefix-doubling rounds, the suffix array against sorting the
             suffixes, the LCP array against comparing characters, the longest
             repeat and the exact number of distinct substrings
  automaton  the transition table's (m + 1) * sigma cells against a run of
             exactly n steps with no back-up at all, and KMP's comparisons
             beside it

BLOCKS PER MODE, because the measured ceiling is 62 KB gzipped. COUNT_JS,
STRINGS_JS and this kit's own block are on every page here. The rest is added
only where it is called:

    RATIONAL_JS  naive, horspool, automaton -- every ratio on these pages is a
                 fraction of two integers and is printed as one, with the
                 decimal beside it rather than instead of it.
                 `expectedPerAlignment` in STRINGS_JS returns a rational and
                 `naive` calls it. The other four modes print no ratio at all
                 and do not carry the block: `rabin` and `suffix` did until
                 the modes were audited for what they actually call, which is
                 about 2 KB gzipped each.
    TREEDRAW_JS  trie -- the trie is drawn as a tree, through `trieKids`.

Measured, on a lesson page rendered by scripts/mathpath/render.py -- gzipped,
against the repository's 62 KB ceiling. Re-derive rather than trusting these:

    suffix 31.0   kmp 31.4   rabin 31.9   trie 32.7   automaton 33.3
    horspool 33.6   naive 34.2

The spread is the block table above and the size of each mode's own markup,
and nothing else: the three lightest are the three that print no ratio and
therefore carry no rationals, and `naive` is the heaviest because it builds
two growth tables rather than one.
"""

from .algebra_core import RATIONAL_JS
from .algo_core import COUNT_JS, STRINGS_JS, TREEDRAW_JS
from .common import Lab

# ---------------------------------------------------------------------------
# The kit's own arithmetic. Top-level functions, nothing closed over a DOM
# element, so scripts/mathcheck.js executes exactly the source that ships.
# ---------------------------------------------------------------------------

SKIT_JS = r"""
  /* ------------------------------------------------------ what a reader types

     Text and pattern are taken as typed, including spaces, and are capped so
     that a paste of a novel does not freeze the tab. Nothing is lower-cased
     and nothing is stripped: a matcher is case-sensitive and a page that
     quietly normalised its input would be answering about a different string
     from the one on screen. */
  function skEsc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;')
                    .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }
  function skPlural(n, one, many) { return n === 1 ? one : many; }
  function skStep(v, lo, hi) { return v < lo ? lo : (v > hi ? hi : v); }
  function skParse(text, pattern, capT, capP) {
    var t = String(text === undefined || text === null ? '' : text);
    var p = String(pattern === undefined || pattern === null ? '' : pattern);
    if (!p.length) return { bad: 'the pattern is empty, and every offset matches an empty pattern' };
    if (!t.length) return { bad: 'the text is empty' };
    if (capT && t.length > capT) return { bad: 'the text is ' + t.length + ' characters and this mode stops at ' + capT };
    if (capP && p.length > capP) return { bad: 'the pattern is ' + p.length + ' characters and this mode stops at ' + capP };
    if (p.length > t.length) return { bad: 'the pattern is longer than the text, so there is no alignment to try' };
    return { t: t, p: p };
  }
  /* THE ORACLE, and it is the definition rather than a faster way to reach the
     same answer: try every offset and compare the whole substring. Every
     matcher on these pages is checked against this on the reader's own text,
     because a matcher that shifts too far returns a shorter list of positions
     and a shorter list looks exactly like a correct answer. */
  function skBrute(t, p) {
    var out = [], i;
    for (i = 0; i + p.length <= t.length; i += 1) {
      if (t.slice(i, i + p.length) === p) out.push(i);
    }
    return out;
  }
  function skSame(a, b) { return a.join(',') === b.join(','); }
  function skAlphabet(s) {
    var seen = {}, out = [], i;
    for (i = 0; i < s.length; i += 1) if (!seen[s[i]]) { seen[s[i]] = true; out.push(s[i]); }
    return out.sort();
  }
  /* The proved worst case for naive matching: every alignment can cost m. */
  function skNaiveBound(n, m) { return m * Math.max(0, n - m + 1); }
  function skRepeat(s, k) {
    var out = '', i;
    for (i = 0; i < k; i += 1) out += s;
    return out;
  }
  /* The longest proper border of every prefix, by TRYING EVERY LENGTH. O(m^3)
     and obviously right, which is the point: `failureFn` is O(m) and is not
     obviously right, and the page prints the two columns beside each other. */
  function skBorderBrute(p) {
    var out = [0], i, k;
    for (i = 1; i <= p.length; i += 1) {
      var best = 0;
      for (k = i - 1; k >= 1; k -= 1) {
        if (p.slice(0, k) === p.slice(i - k, i)) { best = k; break; }
      }
      out.push(best);
    }
    return out;
  }
  /* The suffix array by sorting the suffixes as strings, and the LCP array by
     comparing characters. Both are the definition and both are quadratic. */
  function skSuffixBrute(s) {
    var idx = [], i;
    for (i = 0; i < s.length; i += 1) idx.push(i);
    idx.sort(function (a, b) {
      var x = s.slice(a), y = s.slice(b);
      return x < y ? -1 : (x > y ? 1 : 0);
    });
    var lcp = [0];
    for (i = 1; i < idx.length; i += 1) {
      var a = s.slice(idx[i - 1]), b = s.slice(idx[i]), k = 0;
      while (k < a.length && k < b.length && a[k] === b[k]) k += 1;
      lcp.push(k);
    }
    return { sa: idx, lcp: lcp };
  }
  function skPrefixBrute(words, prefix) {
    return words.filter(function (w) { return w.slice(0, prefix.length) === prefix; }).sort();
  }
  /* One window's hash from scratch, to check the rolling update against. */
  function skHashOf(s, b, mod) {
    var B = BigInt(b), M = BigInt(mod), h = 0n, i;
    for (i = 0; i < s.length; i += 1) h = (h * B + BigInt(s.charCodeAt(i))) % M;
    return h;
  }
  /* Sweep the modulus and report where the collisions stop. This is what turns
     "collisions are rare" into a number: the count of moduli in the range at
     which THIS text produces a spurious hit, and the smallest that does not. */
  function skModulusSweep(t, p, b, lo, hi) {
    var rows = [], m, collided = 0, clean = null, lastBad = null, worst = 0;
    for (m = lo; m <= hi; m += 1) {
      if (!skIsPrime(m)) continue;
      var r = rollingHash(t, p, b, m).result;
      if (r.spurious > 0) {
        collided += 1; lastBad = m;
        if (r.spurious > worst) worst = r.spurious;
      } else if (clean === null) clean = m;
      rows.push({ mod: m, spurious: r.spurious, verifications: r.verifications,
                  hits: r.hits.length });
    }
    return { rows: rows, collided: collided, clean: clean, lastBad: lastBad,
             worst: worst, tested: rows.length };
  }
  function skIsPrime(n) {
    if (n < 2) return false;
    for (var d = 2; d * d <= n; d += 1) if (n % d === 0) return false;
    return true;
  }
  /* The comparisons an algorithm made per alignment, as a bar chart with the
     bound drawn across it. The bar is the measurement and the line is the
     proof, and the picture is the gap between them. */
  function skBars(values, opts) {
    opts = opts || {};
    var w = opts.width === undefined ? 660 : opts.width;
    var h = opts.height === undefined ? 150 : opts.height;
    var n = Math.max(1, values.length);
    var top = Math.max(opts.bound || 0, 1);
    values.forEach(function (v) { if (v > top) top = v; });
    var cell = (w - 36) / n, s = '', i;
    for (i = 0; i < values.length; i += 1) {
      var bh = (values[i] / top) * (h - 34);
      var x = 30 + i * cell;
      s += '<rect x="' + x.toFixed(1) + '" y="' + (h - 20 - bh).toFixed(1) + '" width="'
        + Math.max(1, cell - 1).toFixed(1) + '" height="' + Math.max(0.6, bh).toFixed(1)
        + '" fill="var(--' + ((opts.mark !== undefined && opts.mark === i) ? 'amber' : 'cyan')
        + ')" opacity="' + ((opts.mark !== undefined && opts.mark === i) ? '1' : '0.72') + '" />';
    }
    if (opts.bound) {
      var by = h - 20 - (opts.bound / top) * (h - 34);
      s += '<line x1="30" y1="' + by.toFixed(1) + '" x2="' + (w - 6) + '" y2="' + by.toFixed(1)
        + '" stroke="var(--red)" stroke-width="1.4" stroke-dasharray="5 4" />';
      s += '<text x="32" y="' + (by - 4).toFixed(1) + '" font-size="9" font-weight="700" '
        + 'fill="var(--red)">' + (opts.boundLabel || ('bound ' + opts.bound)) + '</text>';
    }
    s += '<text x="4" y="' + (h - 20) + '" font-size="9" fill="var(--muted)">0</text>';
    s += '<text x="4" y="14" font-size="9" fill="var(--muted)">' + top + '</text>';
    return s;
  }
  /* The text with every match marked, as escaped markup. Long texts are
     windowed rather than truncated, so the marks stay where they are. */
  function skMarkup(t, hits, m, from, span) {
    var start = from || 0, end = Math.min(t.length, start + (span || t.length));
    var inHit = new Array(t.length).fill(false), i, j;
    hits.forEach(function (at) {
      for (j = at; j < at + m && j < t.length; j += 1) inHit[j] = true;
    });
    var out = '', open = false;
    for (i = start; i < end; i += 1) {
      if (inHit[i] && !open) { out += '<span class="tone-cyan"><strong>'; open = true; }
      if (!inHit[i] && open) { out += '</strong></span>'; open = false; }
      out += skEsc(t[i] === ' ' ? '\u00b7' : t[i]);
    }
    if (open) out += '</strong></span>';
    return out;
  }
"""


# ---------------------------------------------------------------------------
# One core per mode, not one for the kit -- the largest single lever there is
# on page weight. `kmp` prints no ratio and must not carry the rationals;
# `trie` is the only mode that draws a tree.
# ---------------------------------------------------------------------------

_BASE_JS = COUNT_JS + STRINGS_JS + SKIT_JS
_RATIO_JS = COUNT_JS + RATIONAL_JS + STRINGS_JS + SKIT_JS
_TREE_JS = COUNT_JS + STRINGS_JS + TREEDRAW_JS + SKIT_JS


# ---------------------------------------------------------------------------
# Control furniture, the same shapes every kit on this path uses.
# ---------------------------------------------------------------------------


def _attr(text):
    return (str(text).replace("&", "&amp;").replace('"', "&quot;")
            .replace("<", "&lt;").replace(">", "&gt;"))


def _range(cid, label, lo, hi, value, step=1):
    return (
        "        <div>\n"
        '          <div class="range-row"><label class="small-copy" for="%s">%s</label>'
        '<span class="range-value" id="%sOut">%s</span></div>\n'
        '          <input id="%s" type="range" min="%s" max="%s" step="%s" value="%s" />\n'
        "        </div>\n" % (cid, label, cid, value, cid, lo, hi, step, value)
    )


def _select(cid, label, options, chosen):
    opts = "".join(
        '<option value="%s"%s>%s</option>'
        % (_attr(v), " selected" if str(v) == str(chosen) else "", t)
        for v, t in options
    )
    return (
        '        <div class="field">\n          <label for="%s">%s</label>\n'
        '          <select id="%s">%s</select>\n        </div>\n' % (cid, label, cid, opts)
    )


def _text(cid, label, placeholder):
    """A text box that starts EMPTY and is filled by the script at startup.

    graphkit.py met this first and the reason is the same here: a default
    carried in the markup has to survive scripts/labcheck.js's tag scan as well
    as a browser's entity decoding, and the two disagree. The value goes in
    from the script before the first redraw.
    """
    return (
        '        <div class="field">\n          <label for="%s">%s</label>\n'
        '          <input id="%s" type="text" value="" inputmode="text" autocomplete="off"'
        ' spellcheck="false" placeholder="%s">\n'
        "        </div>\n" % (cid, label, cid, _attr(placeholder))
    )


def _kpis(items):
    cells = "".join(
        '          <div class="kpi"><span>%s</span><strong id="%s">&mdash;</strong></div>\n'
        % (label, cid) for label, cid in items
    )
    return '        <div class="kpi-grid">\n%s        </div>\n' % cells


def _hint(cid, text):
    return '        <p class="small-copy" id="%s" style="margin:0;">%s</p>' % (cid, text)


def _toolbar(name, subtitle, legend):
    swatches = "".join(
        '<span class="tone-%s"><i class="legend-swatch"></i>%s</span>' % (tone, text)
        for tone, text in legend
    )
    return (
        '      <div class="lab-toolbar">\n'
        '        <div class="lab-title"><strong>%s</strong><span>%s</span></div>\n'
        '        <div class="inline-legend">%s</div>\n'
        "      </div>\n" % (name, subtitle, swatches)
    )


def _stage(inner):
    return '      <div class="lab-stage">%s</div>\n' % inner


def _svg(cid, box, alt):
    return '<svg id="%s" viewBox="%s" role="img" aria-label="%s"></svg>' % (cid, box, alt)


def _strip(cid):
    return ('      <p class="tt" id="%s" style="margin:8px 0 0;word-break:break-all;'
            'line-height:1.7;"></p>\n' % cid)


def _table(cid, top=12):
    return ('      <div class="table-wrap" style="margin-top:%dpx;">'
            '<table class="tt" id="%s"></table></div>\n' % (top, cid))


def _banner(cid):
    return '      <div class="status-banner" id="%s" style="margin-top:12px;"></div>' % cid


def _js(text):
    """A JavaScript single-quoted string literal for a preset's own text."""
    return "'" + str(text).replace("\\", "\\\\").replace("'", "\\'").replace("\n", "\\n") + "'"


def _presets_js(name, presets, keys):
    """The preset table as data the script reads, not as branches."""
    rows = []
    for p in presets:
        body = ", ".join("%s: %s" % (k, _js(p[k])) for k in keys)
        rows.append("    '%s': { %s }" % (p["id"], body))
    return "  var %s = {\n%s\n  };\n" % (name, ",\n".join(rows))


def _options(presets):
    return [(p["id"], p["label"]) for p in presets]


def _chosen(presets, cfg):
    want = str(cfg.get("preset", presets[0]["id"]))
    for p in presets:
        if p["id"] == want:
            return p
    raise ValueError(
        "strings: no preset %r; this mode has %s"
        % (want, ", ".join(p["id"] for p in presets))
    )


# The sentence every mode carries in some form. This Subject's hazard is that a
# count on one input is not a bound, and on this course it has a second edge:
# the input that makes an algorithm look good is chosen as carefully as the one
# that makes it look bad. Spelled once so no mode can quietly drop it.
_ONE_TEXT = (
    "  /* Every count below was produced by running the matcher on the text in\n"
    "     the box. That is one text. The bound printed beside it is a statement\n"
    "     about every text there is, and the two presets that matter on this\n"
    "     page are the one where they nearly meet and the one where they do\n"
    "     not. Neither of them is the algorithm's cost. */\n"
)


# ---------------------------------------------------------------------------
# naive -- the same algorithm, linear on one text and quadratic on another
# ---------------------------------------------------------------------------

_NA_PRESETS = [
    {
        "id": "prose",
        "label": "ordinary prose, a pattern that occurs",
        "text": "the rain in spain stays mainly in the plain",
        "pattern": "ain",
        "note": "most alignments die on the first character, so the count is barely above n",
    },
    {
        "id": "absent",
        "label": "a pattern that is not there, where naive wins",
        "text": "the rain in spain stays mainly in the plain",
        "pattern": "zebra",
        "note": "one comparison per alignment and no match to verify: fewer than KMP makes",
    },
    {
        "id": "adversarial",
        "label": "the text built to reach the bound",
        "text": "aaaaaaaaaaaaaaaaaaaaaaaa",
        "pattern": "aaaab",
        "note": "every alignment matches m − 1 characters and then fails: the bound, exactly",
    },
    {
        "id": "dna",
        "label": "four letters, so mismatches come later",
        "text": "GATTACAGATTACCAGATTACAGGATTACAGATTAC",
        "pattern": "GATTACA",
        "note": "a smaller alphabet means a longer run before the first mismatch",
    },
    {
        "id": "binary",
        "label": "two letters, the smallest useful alphabet",
        "text": "101100101101001011010010110100101101",
        "pattern": "10110",
        "note": "sigma = 2 puts the expected comparisons per alignment at 2",
    },
    {
        "id": "periodic",
        "label": "a periodic text, without a single long run",
        "text": "abababababababababababab",
        "pattern": "abababb",
        "note": "four comparisons per alignment out of a possible seven, and no match at all",
    },
]


def _naive(cfg):
    chosen = _chosen(_NA_PRESETS, cfg)
    markup = (
        _toolbar(
            "Naive matching, measured and bounded",
            "comparisons per alignment, and the same count at six sizes",
            [("cyan", "comparisons at this alignment"), ("amber", "the alignment shown"),
             ("red", "m, the most one alignment can cost")],
        )
        + _stage(_svg("naBars", "0 0 660 150",
                      "One bar per alignment, its height the number of characters compared "
                      "there, with m drawn across as the per-alignment bound."))
        + _strip("naStrip")
        + _table("naGrowth")
        + _table("naFamily")
        + _banner("naStatus")
    )
    controls = (
        _select("naPreset", "Worked example", _options(_NA_PRESETS), chosen["id"])
        + _text("naText", "The text", "the rain in spain stays mainly in the plain")
        + _text("naPattern", "The pattern", "ain")
        + _range("naAt", "Show the alignment at", 1, 60, 1)
        + _kpis([("Alignments tried", "naAlign"), ("Characters compared", "naComp"),
                 ("Per alignment, measured", "naPer"),
                 ("Per alignment, uniform alphabet", "naExp"),
                 ("The proved bound m(n − m + 1)", "naBound"),
                 ("Matches, and matches by definition", "naHits"),
                 ("KMP on the same text", "naKmp"),
                 ("Horspool on the same text", "naHors")])
        + _hint(
            "naHint",
            "Type any text and any pattern. The bar chart is one bar per alignment and its "
            "height is the characters compared there, so a text of mostly first-character "
            "mismatches is a flat chart and the adversarial text is a solid block at the line. "
            "The first table repeats your text 1 to 6 times with the pattern unchanged, which "
            "grows n and holds m: the count then has to be linear in n, and the column that "
            "matters is comparisons per character. The second table grows m as well, and that "
            "is where the quadratic lives.",
        )
    )
    script = _RATIO_JS + _ONE_TEXT + _presets_js("NAP", _NA_PRESETS, ["text", "pattern", "note"]) + r"""
  var presetIn = document.getElementById('naPreset'), textIn = document.getElementById('naText');
  var patIn = document.getElementById('naPattern');
  var atIn = document.getElementById('naAt'), atOut = document.getElementById('naAtOut');
  var bars = document.getElementById('naBars'), strip = document.getElementById('naStrip');
  var growth = document.getElementById('naGrowth'), family = document.getElementById('naFamily');
  var status = document.getElementById('naStatus');
  var KPIS = ['naAlign', 'naComp', 'naPer', 'naExp', 'naBound', 'naHits', 'naKmp', 'naHors'];

  function blank(why) {
    bars.innerHTML = ''; strip.innerHTML = ''; growth.innerHTML = ''; family.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> Type a text and a pattern '
      + 'shorter than it.';
  }

  function redraw() {
    var parsed = skParse(textIn.value, patIn.value, 240, 40);
    if (parsed.bad) { blank(parsed.bad); return; }
    var t = parsed.t, p = parsed.p, n = t.length, m = p.length;

    var run = naiveRun(t, p), res = run.result;
    var truth = skBrute(t, p);
    var right = skSame(res.hits, truth);
    var kmp = kmpRun(t, p), hors = horspoolRun(t, p);
    var kmpRight = skSame(kmp.result.hits, truth);
    var horsRight = skSame(hors.result.hits, truth);

    atIn.max = res.alignments;
    var at = skStep(parseInt(atIn.value, 10), 1, res.alignments);
    atOut.textContent = at + ' of ' + res.alignments;
    var step = run.trace[at - 1];

    var compares = run.counts.compares || 0;
    var bound = skNaiveBound(n, m);
    var sigma = skAlphabet(t + p).length;
    var per = R(BigInt(compares), BigInt(Math.max(1, res.alignments)));

    bars.innerHTML = skBars(run.trace.map(function (s) { return s.compares; }),
                            { bound: m, boundLabel: 'm = ' + m, mark: at - 1, width: 660 });
    strip.innerHTML = '<span class="tone-muted">text, matches marked:</span> '
      + skMarkup(t, res.hits, m, 0, 200)
      + (t.length > 200 ? ' <span class="tone-muted">…</span>' : '')
      + '<br><span class="tone-muted">alignment ' + at + ' starts at ' + step.at
      + ' and compared ' + step.compares + ' character'
      + skPlural(step.compares, '', 's') + ', matching ' + step.matched + '.</span>';

    /* n grows, m does not. Both the count and the bound are then linear in n,
       and the whole difference between the two texts is the CONSTANT -- which
       is why the per-character column is the one to read. */
    var rows = '';
    for (var k = 1; k <= 6; k += 1) {
      var tk = skRepeat(t, k);
      if (tk.length > 1440) break;
      var rk = naiveRun(tk, p), kk = kmpRun(tk, p), hk = horspoolRun(tk, p);
      var ck = rk.counts.compares || 0;
      var pc = R(BigInt(ck), BigInt(tk.length));
      rows += '<tr' + (k === 1 ? ' class="tone-cyan"' : '') + '><th class="rowhead">' + k
        + '</th><td>' + tk.length + '</td><td>' + ck + '</td><td>' + Rtext(pc) + ' = '
        + Rnum(pc).toFixed(2) + '</td><td>' + (kk.counts.compares || 0) + '</td><td>'
        + (hk.counts.compares || 0) + '</td><td>' + skNaiveBound(tk.length, m) + '</td></tr>';
    }
    growth.innerHTML = '<caption>Your text repeated 1 to 6 times, with the pattern unchanged. '
      + 'Holding m fixed makes both the count and the bound linear in n, so the column that '
      + 'separates one text from another is comparisons per character</caption><thead><tr>'
      + '<th>copies</th><th>n</th><th>naive</th><th>per character</th><th>KMP</th>'
      + '<th>Horspool</th><th>m(n − m + 1)</th></tr></thead><tbody>' + rows + '</tbody>';

    /* m grows WITH n. This is the family the quadratic claim is about, and it
       is fixed rather than read from the boxes, because a text that reaches
       the bound has to be built and cannot be typed by accident. */
    var frows = '';
    for (var q = 2; q <= 10; q += 1) {
      var wp = naiveWorstPair(q + 1, 2 * q);
      var fn = naiveRun(wp.text, wp.pattern), fk = kmpRun(wp.text, wp.pattern);
      var fh = horspoolRun(wp.text, wp.pattern);
      var fc = fn.counts.compares || 0, fb = skNaiveBound(wp.text.length, wp.pattern.length);
      var fpc = R(BigInt(fc), BigInt(wp.text.length));
      frows += '<tr' + (fc === fb ? '' : ' class="tone-red"') + '><th class="rowhead">'
        + wp.pattern.length + '</th><td>' + wp.text.length + '</td><td>' + fc + '</td><td>'
        + fb + '</td><td>' + Rtext(fpc) + ' = ' + Rnum(fpc).toFixed(2) + '</td><td>'
        + (fk.counts.compares || 0) + '</td><td>' + (fh.counts.compares || 0) + '</td></tr>';
    }
    family.innerHTML = '<caption>The family the quadratic is about: the text is a run of a’s '
      + 'of length 2m and the pattern is m − 1 of them followed by a b, so m grows WITH n. '
      + 'The count equals the bound in every row, the per-character column rises without '
      + 'limit, and KMP’s stays flat</caption><thead><tr><th>m</th><th>n = 2(m − 1)</th>'
      + '<th>naive</th><th>m(n − m + 1)</th><th>per character</th><th>KMP</th>'
      + '<th>Horspool</th></tr></thead><tbody>' + frows + '</tbody>';

    document.getElementById('naAlign').textContent = res.alignments;
    document.getElementById('naComp').textContent = compares;
    document.getElementById('naPer').textContent = Rtext(per) + ' = ' + Rnum(per).toFixed(3);
    document.getElementById('naExp').textContent = sigma > 1
      ? (Rtext(expectedPerAlignment(sigma)) + ' at sigma = ' + sigma)
      : 'one letter only';
    document.getElementById('naBound').textContent = bound;
    document.getElementById('naHits').textContent = res.hits.length + ' and ' + truth.length
      + (right ? '' : ' — DISAGREE');
    document.getElementById('naKmp').textContent = (kmp.counts.compares || 0)
      + (kmpRight ? '' : ' — WRONG MATCHES');
    document.getElementById('naHors').textContent = (hors.counts.compares || 0)
      + (horsRight ? '' : ' — WRONG MATCHES');

    var tight = compares === bound;
    var kc = kmp.counts.compares || 0;
    status.innerHTML = '<strong>' + compares + ' comparison' + skPlural(compares, '', 's')
      + ' over ' + res.alignments + ' alignment' + skPlural(res.alignments, '', 's')
      + ', against a bound of ' + bound + '.</strong> '
      + (tight
          ? '<span class="tone-red">The measured count IS the bound.</span> Every alignment '
            + 'matched m − 1 characters before failing, which is what the bound describes and '
            + 'what a text has to be built to achieve. '
          : 'That is ' + Rtext(per) + ' per alignment against a worst case of ' + m
            + ', so this text costs ' + Rtext(R(BigInt(bound), BigInt(Math.max(1, compares))))
            + ' = ' + Rnum(R(BigInt(bound), BigInt(Math.max(1, compares)))).toFixed(1)
            + ' times less than the bound allows. ')
      + 'Over a uniform alphabet of the ' + sigma + ' letter' + skPlural(sigma, '', 's')
      + ' this input uses, the expected comparisons per alignment is exactly sigma/(sigma − 1) = '
      + (sigma > 1 ? Rtext(expectedPerAlignment(sigma)) : 'undefined') + ', which is under 2 for '
      + 'every alphabet with two or more letters and never depends on m at all. '
      + '<span class="tone-cyan">KMP took ' + kc + '</span> and '
      + '<span class="tone-cyan">Horspool took ' + (hors.counts.compares || 0) + '</span> on '
      + 'this same text, '
      + (compares < kc
          ? 'so naive matching is ahead of KMP here by ' + (kc - compares) + ' comparison'
            + skPlural(kc - compares, '', 's') + ' — which happens whenever the pattern is '
            + 'rare or absent, because naive stops after one comparison at most alignments '
            + 'while KMP still reads every character of the text once. '
          : 'so KMP is ahead here by ' + (compares - kc) + ' and the gap is a constant rather '
            + 'than an order: both are linear in n while m is held fixed. ')
      + 'The lower table is the only place on this page where the quadratic appears, and it '
      + 'has to grow m to get it: at m = 11 the same algorithm makes 110 comparisons on a text '
      + 'of 20 characters. '
      + (right && kmpRight && horsRight
          ? 'All three matchers found the same ' + truth.length + ' match'
            + skPlural(truth.length, '', 'es') + ' as a scan over every offset.'
          : '<span class="tone-red">At least one of the three disagrees with a scan over every '
            + 'offset, which means it is not finding the matches at all.</span>');
  }

  function apply() {
    var pre = NAP[presetIn.value];
    if (!pre) return;
    textIn.value = pre.text; patIn.value = pre.pattern; atIn.value = 1;
    redraw();
  }
  var START = NAP[presetIn.value];
  if (START && !textIn.value) { textIn.value = START.text; patIn.value = START.pattern; }
  presetIn.addEventListener('change', apply);
  textIn.addEventListener('input', redraw);
  patIn.addEventListener('input', redraw);
  atIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Naive matching, and the two texts that answer differently",
        subtitle="Comparisons measured per alignment, against m and against m(n − m + 1)",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type a text and a pattern, and count the work"),
        panel_intro=cfg.get(
            "panel_intro",
            "The matcher runs in your browser and the bar chart is what it did. The match "
            "positions are checked against a scan over every offset on every keystroke, because "
            "an algorithm that shifts too far returns fewer matches and a shorter list is not "
            "obviously wrong.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# kmp -- the failure function, built, and checked against every border
# ---------------------------------------------------------------------------

_KM_PRESETS = [
    {
        "id": "ababaca",
        "label": "the standard example",
        "pattern": "ababaca",
        "text": "abababacaba ababacaab ababaca",
        "note": "borders of lengths 0, 0, 1, 2, 3, 0, 1: the classic shape",
    },
    {
        "id": "aaaa",
        "label": "every prefix is a border of the next",
        "pattern": "aaaaa",
        "text": "aaaaaaaaaaaaaaaaaaaa",
        "note": "fail[k] = k − 1 throughout, and the border chain has every length on it",
    },
    {
        "id": "abcabcabd",
        "label": "a long border that then collapses",
        "pattern": "abcabcabd",
        "text": "abcabcabcabcabdabcabcabd",
        "note": "the border reaches 5 and the final d takes it to 0 in one step",
    },
    {
        "id": "aabaaab",
        "label": "where the inner loop actually iterates",
        "pattern": "aabaaab",
        "text": "aabaaabaaabaabaaab",
        "note": "the only preset here where the fallback chain is followed more than once",
    },
    {
        "id": "abcdefg",
        "label": "no two characters alike: no borders at all",
        "pattern": "abcdefg",
        "text": "abcdefgabcdefh abcdefg",
        "note": "fail[] is all zeros, and KMP degenerates into naive matching exactly",
    },
]


def _kmp(cfg):
    chosen = _chosen(_KM_PRESETS, cfg)
    markup = (
        _toolbar(
            "The failure function, one character at a time",
            "built in linear time, checked against every border length",
            [("cyan", "the prefix being extended"), ("purple", "its longest proper border"),
             ("amber", "the fallback chain from the full pattern")],
        )
        + _stage(_svg("kmBars", "0 0 660 150",
                      "One bar per prefix, its height the length of that prefix's longest "
                      "proper border."))
        + _table("kmFail")
        + _strip("kmChain")
        + _banner("kmStatus")
    )
    controls = (
        _select("kmPreset", "Worked example", _options(_KM_PRESETS), chosen["id"])
        + _text("kmPattern", "The pattern", "ababaca")
        + _text("kmText", "The text to search", "abababacaba ababacaab ababaca")
        + _range("kmAt", "Build up to character", 1, 40, 1)
        + _kpis([("Pattern length m", "kmM"), ("Inner-loop iterations", "kmInner"),
                 ("The bound 2m", "kmBound"), ("Longest border of the whole pattern", "kmTop"),
                 ("Comparisons, KMP on the text", "kmComp"),
                 ("Comparisons, naive on the text", "kmNaive"),
                 ("The bound 2n", "kmNBound"),
                 ("Matches, and matches by definition", "kmHits")])
        + _hint(
            "kmHint",
            "A BORDER of a string is a proper prefix that is also a suffix. fail[k] is the "
            "length of the longest border of the first k characters, and it is the whole of "
            "KMP: on a mismatch after k matched characters the pattern slides so that those "
            "fail[k] characters line up again, and the text pointer never moves back. The third "
            "column is that length found by trying every one of the k − 1 possible lengths and "
            "comparing two substrings, which is how you check a linear-time construction.",
        )
    )
    script = _BASE_JS + _ONE_TEXT + _presets_js("KMP2", _KM_PRESETS, ["pattern", "text", "note"]) + r"""
  var presetIn = document.getElementById('kmPreset'), patIn = document.getElementById('kmPattern');
  var textIn = document.getElementById('kmText');
  var atIn = document.getElementById('kmAt'), atOut = document.getElementById('kmAtOut');
  var bars = document.getElementById('kmBars'), table = document.getElementById('kmFail');
  var chain = document.getElementById('kmChain'), status = document.getElementById('kmStatus');
  var KPIS = ['kmM', 'kmInner', 'kmBound', 'kmTop', 'kmComp', 'kmNaive', 'kmNBound', 'kmHits'];

  function blank(why) {
    bars.innerHTML = ''; table.innerHTML = ''; chain.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> Type a pattern and a text.';
  }

  function redraw() {
    var parsed = skParse(textIn.value, patIn.value, 240, 30);
    if (parsed.bad) { blank(parsed.bad); return; }
    var t = parsed.t, p = parsed.p, m = p.length;

    var f = failureFn(p), fail = f.result.fail;
    var brute = skBorderBrute(p);
    var run = kmpRun(t, p), truth = skBrute(t, p);
    var right = skSame(run.result.hits, truth);
    var naive = naiveRun(t, p);

    atIn.max = m;
    var at = skStep(parseInt(atIn.value, 10), 1, m);
    atOut.textContent = at + ' of ' + m;

    bars.innerHTML = skBars(brute.slice(1), { bound: m - 1, boundLabel: 'm − 1', mark: at - 1,
                                              width: 660, height: 150 });

    var rows = '', mismatched = 0;
    for (var k = 1; k <= m; k += 1) {
      var mine = fail[k] > 0 ? fail[k] : 0, theirs = brute[k];
      if (mine !== theirs) mismatched += 1;
      rows += '<tr' + (k === at ? ' class="tone-cyan"' : (mine === theirs ? '' : ' class="tone-red"'))
        + '><th class="rowhead">' + k + '</th><td class="tt">' + skEsc(p.slice(0, k))
        + '</td><td>' + mine + '</td><td>' + theirs + '</td><td class="tt">'
        + (theirs ? skEsc(p.slice(0, theirs)) : '<span class="tone-muted">none</span>')
        + '</td><td>' + (k <= at ? 'built' : '') + '</td></tr>';
    }
    table.innerHTML = '<caption>One row per prefix. The third column is the linear-time '
      + 'construction and the fourth is the longest border found by trying every length and '
      + 'comparing the two substrings</caption><thead><tr><th>k</th><th>prefix</th>'
      + '<th>fail[k]</th><th>longest border, by definition</th><th>the border</th>'
      + '<th></th></tr></thead><tbody>' + rows + '</tbody>';

    var top = fail[m] > 0 ? fail[m] : 0;
    chain.innerHTML = '<span class="tone-muted">the fallback chain from the whole pattern:</span> '
      + f.result.borders.map(function (b) { return '<span class="tone-amber">' + b + '</span>'; })
        .join(' → ') + ' → 0. '
      + '<span class="tone-muted">Each step is the longest border of the one before, so the '
      + 'chain is every length at which the pattern can still be aligned after a mismatch at '
      + 'the end.</span>';

    document.getElementById('kmM').textContent = m;
    document.getElementById('kmInner').textContent = f.result.inner;
    document.getElementById('kmBound').textContent = f.result.bound;
    document.getElementById('kmTop').textContent = top
      + (top ? ' — ' + skEsc(p.slice(0, top)) : ' — the pattern has no border');
    document.getElementById('kmComp').textContent = run.counts.compares || 0;
    document.getElementById('kmNaive').textContent = naive.counts.compares || 0;
    document.getElementById('kmNBound').textContent = run.result.bound;
    document.getElementById('kmHits').textContent = run.result.hits.length + ' and ' + truth.length
      + (right ? '' : ' — DISAGREE');

    var kc = run.counts.compares || 0, nc = naive.counts.compares || 0;
    status.innerHTML = '<strong>' + (mismatched
        ? '<span class="tone-red">' + mismatched + ' row' + skPlural(mismatched, '', 's')
          + ' where the linear construction and the definition disagree.</span>'
        : 'The linear construction agrees with the definition on all ' + m + ' prefixes.')
      + '</strong> Building it took <span class="tone-cyan">' + f.result.inner + '</span> '
      + 'inner-loop iteration' + skPlural(f.result.inner, '', 's') + ' against a bound of 2m = '
      + f.result.bound + '. '
      + (f.result.inner === 0
          ? 'None at all on this pattern, which is the common case and is why the amortised '
            + 'argument is easy to believe and hard to see. '
          : 'The argument for that bound is not about any one step: k rises by at most 1 per '
            + 'character and the inner loop only ever lowers it, so the total fall cannot exceed '
            + 'the total rise. ')
      + 'On the text, KMP made <span class="tone-cyan">' + kc + '</span> comparison'
      + skPlural(kc, '', 's') + ' against a bound of 2n = ' + run.result.bound
      + ', and naive matching made ' + nc + '. '
      + (kc <= nc
          ? 'KMP is ahead here by ' + (nc - kc) + '. '
          : '<span class="tone-amber">Naive matching is ahead here by ' + (kc - nc)
            + '.</span> That is not a bug: KMP compares once per text character plus once per '
            + 'fallback, and naive often stops after one comparison per alignment. KMP buys a '
            + 'guarantee, and on a text that was never going to be the worst case the guarantee '
            + 'is what you pay for and do not use. ')
      + 'The text pointer never moved backwards in either direction'
      + (right
          ? ', and the ' + truth.length + ' match'
            + skPlural(truth.length, '', 'es') + ' agree with a scan over every offset.'
          : ', but <span class="tone-red">the matches do not agree with a scan over every '
            + 'offset</span>.');
  }

  function apply() {
    var pre = KMP2[presetIn.value];
    if (!pre) return;
    patIn.value = pre.pattern; textIn.value = pre.text; atIn.value = 1;
    redraw();
  }
  var START = KMP2[presetIn.value];
  if (START && !patIn.value) { patIn.value = START.pattern; textIn.value = START.text; }
  presetIn.addEventListener('change', apply);
  patIn.addEventListener('input', redraw);
  textIn.addEventListener('input', redraw);
  atIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The failure function, built character by character",
        subtitle="Every border found twice: in linear time, and by trying every length",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type a pattern and watch its borders appear"),
        panel_intro=cfg.get(
            "panel_intro",
            "fail[k] is the length of the longest proper border of the first k characters. The "
            "table computes it twice, once in linear time and once by trying every length, so "
            "the fast construction is checked rather than trusted.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# horspool -- skipping, and the text where nothing is skipped
# ---------------------------------------------------------------------------

_HO_PRESETS = [
    {
        "id": "english",
        "label": "ordinary prose: most of the text is never looked at",
        "text": "the rain in spain stays mainly in the plain and never in the hills",
        "pattern": "mainly",
        "note": "a six-character pattern jumps six at a time over letters it does not contain",
    },
    {
        "id": "dna",
        "label": "four letters, so shifts are shorter",
        "text": "GATTACAGATTACCAGATTACAGGATTACAGATTACAGGATTA",
        "pattern": "GATTACA",
        "note": "every character of the text is in the pattern, so no shift is ever the full m",
    },
    {
        "id": "stuck",
        "label": "the text where every shift is 1",
        "text": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "pattern": "baaaa",
        "note": "the last character always matches, the first never does: m comparisons, shift 1",
    },
    {
        "id": "rare",
        "label": "a pattern ending in a character the text barely holds",
        "text": "abcabcabcabcabcabcabcabcabcabcabcabcabcz",
        "pattern": "cccz",
        "note": "the final z is absent from almost every window, so the shift is the full m",
    },
    {
        "id": "periodic",
        "label": "a periodic text, where the table repeats too",
        "text": "abababababababababababababababab",
        "pattern": "ababb",
        "note": "shifts alternate between 1 and 2, and the skipping saves about half",
    },
]


def _horspool(cfg):
    chosen = _chosen(_HO_PRESETS, cfg)
    markup = (
        _toolbar(
            "Shifting by more than one",
            "characters skipped, against the characters there are",
            [("cyan", "comparisons at this alignment"), ("amber", "the alignment shown"),
             ("red", "m, the most one alignment can cost")],
        )
        + _stage(_svg("hoBars", "0 0 660 150",
                      "One bar per alignment examined, its height the characters compared "
                      "there, right to left."))
        + _strip("hoStrip")
        + _table("hoShift")
        + _table("hoSteps")
        + _banner("hoStatus")
    )
    controls = (
        _select("hoPreset", "Worked example", _options(_HO_PRESETS), chosen["id"])
        + _text("hoText", "The text", "the rain in spain stays mainly in the plain")
        + _text("hoPattern", "The pattern", "mainly")
        + _range("hoAt", "Show the alignment at", 1, 60, 1)
        + _kpis([("Alignments examined", "hoAlign"), ("Alignments naive would try", "hoAll"),
                 ("Characters compared", "hoComp"), ("Characters skipped entirely", "hoSkip"),
                 ("Average shift", "hoAvg"), ("Comparisons, naive", "hoNaive"),
                 ("Comparisons, KMP", "hoKmp"),
                 ("Matches, and matches by definition", "hoHits")])
        + _hint(
            "hoHint",
            "Horspool compares the window right to left and then shifts by the last occurrence "
            "of the text character under the window's last position, looked up in a table built "
            "from the pattern's first m − 1 characters. A character the pattern does not contain "
            "at all shifts the full m. The saving comes from the TEXT as much as from the "
            "pattern: pick the third worked example, where the last character of every window "
            "matches and the shift is always 1.",
        )
    )
    script = _RATIO_JS + _ONE_TEXT + _presets_js("HOP", _HO_PRESETS, ["text", "pattern", "note"]) + r"""
  var presetIn = document.getElementById('hoPreset'), textIn = document.getElementById('hoText');
  var patIn = document.getElementById('hoPattern');
  var atIn = document.getElementById('hoAt'), atOut = document.getElementById('hoAtOut');
  var bars = document.getElementById('hoBars'), strip = document.getElementById('hoStrip');
  var shiftT = document.getElementById('hoShift'), steps = document.getElementById('hoSteps');
  var status = document.getElementById('hoStatus');
  var KPIS = ['hoAlign', 'hoAll', 'hoComp', 'hoSkip', 'hoAvg', 'hoNaive', 'hoKmp', 'hoHits'];

  function blank(why) {
    bars.innerHTML = ''; strip.innerHTML = ''; shiftT.innerHTML = ''; steps.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> Type a text and a pattern.';
  }

  function redraw() {
    var parsed = skParse(textIn.value, patIn.value, 240, 30);
    if (parsed.bad) { blank(parsed.bad); return; }
    var t = parsed.t, p = parsed.p, n = t.length, m = p.length;

    var run = horspoolRun(t, p), res = run.result;
    var truth = skBrute(t, p), right = skSame(res.hits, truth);
    var naive = naiveRun(t, p), kmp = kmpRun(t, p);

    atIn.max = Math.max(1, run.trace.length);
    var at = skStep(parseInt(atIn.value, 10), 1, Math.max(1, run.trace.length));
    atOut.textContent = at + ' of ' + run.trace.length;
    var step = run.trace[at - 1];

    bars.innerHTML = skBars(run.trace.map(function (s) { return s.matchedFromRight + 1; }),
                            { bound: m, boundLabel: 'm = ' + m, mark: at - 1, width: 660 });
    strip.innerHTML = '<span class="tone-muted">text, matches marked:</span> '
      + skMarkup(t, res.hits, m, 0, 200)
      + (t.length > 200 ? ' <span class="tone-muted">…</span>' : '')
      + (step ? '<br><span class="tone-muted">alignment ' + at + ' sits at ' + step.at
          + ', matched ' + step.matchedFromRight + ' character'
          + skPlural(step.matchedFromRight, '', 's') + ' from the right, and shifted '
          + step.shift + '.</span>' : '');

    var alpha = skAlphabet(t + p), srows = '';
    alpha.forEach(function (ch) {
      var s = res.table[ch] === undefined ? m : res.table[ch];
      var inPat = p.indexOf(ch) >= 0;
      srows += '<tr' + (s === m ? ' class="tone-green"' : '') + '><th class="rowhead tt">'
        + skEsc(ch === ' ' ? '· (space)' : ch) + '</th><td>' + s + '</td><td>'
        + (res.table[ch] === undefined
            ? (inPat ? 'only as the last character, which the table leaves out'
                     : 'not in the pattern at all')
            : 'last seen at index ' + (m - 1 - res.table[ch]) + ' of the pattern')
        + '</td></tr>';
    });
    shiftT.innerHTML = '<caption>The shift table, one row per character of this text and '
      + 'pattern. The table is built from the pattern’s first m − 1 characters only, so '
      + 'the pattern’s own last character can still shift the full m</caption><thead><tr>'
      + '<th>character</th><th>shift</th><th>why</th></tr></thead><tbody>' + srows + '</tbody>';

    var trows = '';
    run.trace.slice(0, 24).forEach(function (s, i) {
      trows += '<tr' + (i === at - 1 ? ' class="tone-cyan"' : '') + '><th class="rowhead">'
        + (i + 1) + '</th><td>' + s.at + '</td><td class="tt">'
        + skEsc(t.slice(s.at, s.at + m)) + '</td><td>' + s.matchedFromRight + '</td><td>'
        + s.shift + '</td><td>'
        + (res.hits.indexOf(s.at) >= 0 ? '<span class="tone-cyan">a match</span>' : '')
        + '</td></tr>';
    });
    steps.innerHTML = '<caption>The alignments actually examined'
      + (run.trace.length > 24 ? ' (first 24 of ' + run.trace.length + ')' : '')
      + '. Naive would examine ' + (n - m + 1) + '</caption><thead><tr><th>step</th>'
      + '<th>at</th><th>window</th><th>matched from the right</th><th>shift</th><th></th>'
      + '</tr></thead><tbody>' + trows + '</tbody>';

    var compares = run.counts.compares || 0;
    /* skipped is the sum of (shift - 1), so this is the mean shift exactly. */
    var avg = R(BigInt(res.skipped + run.trace.length), BigInt(Math.max(1, run.trace.length)));
    document.getElementById('hoAlign').textContent = run.trace.length;
    document.getElementById('hoAll').textContent = n - m + 1;
    document.getElementById('hoComp').textContent = compares;
    document.getElementById('hoSkip').textContent = res.skipped;
    document.getElementById('hoAvg').textContent = Rtext(avg) + ' = ' + Rnum(avg).toFixed(2);
    document.getElementById('hoNaive').textContent = naive.counts.compares || 0;
    document.getElementById('hoKmp').textContent = kmp.counts.compares || 0;
    document.getElementById('hoHits').textContent = res.hits.length + ' and ' + truth.length
      + (right ? '' : ' — DISAGREE');

    var nc = naive.counts.compares || 0;
    status.innerHTML = '<strong>' + run.trace.length + ' alignment'
      + skPlural(run.trace.length, '', 's') + ' examined out of ' + (n - m + 1)
      + ', for ' + compares + ' comparison' + skPlural(compares, '', 's') + '.</strong> '
      + (res.skipped > 0
          ? 'The shifts skipped <span class="tone-cyan">' + res.skipped + '</span> alignment'
            + skPlural(res.skipped, '', 's') + ' outright, at an average shift of '
            + Rnum(avg).toFixed(2) + ' against a maximum of ' + m + '. '
          : '<span class="tone-red">Every shift was 1, so nothing was skipped at all.</span> '
            + 'The last character of every window is in the pattern and near its end, which is '
            + 'what makes the table useless here: the algorithm degenerates to naive matching '
            + 'from the wrong end, and this is its worst case. ')
      + 'It made ' + compares + ' comparison' + skPlural(compares, '', 's')
      + ' against naive’s ' + nc + ' and KMP’s ' + (kmp.counts.compares || 0) + '. '
      + (compares < nc
          ? 'The saving is real and it has no bound behind it: Horspool’s worst case is '
            + 'still m(n − m + 1) comparisons, the same as naive’s, and the only reason '
            + 'this text is faster is the characters it happens to contain. '
          : 'On this text Horspool is not ahead, and its worst case is the same m(n − m + 1) '
            + 'that naive matching has. It has no better guarantee, only a better average on '
            + 'texts over large alphabets. ')
      + (right
          ? 'The ' + truth.length + ' match' + skPlural(truth.length, '', 'es')
            + ' agree with a scan over every offset — which is the check that matters for a '
            + 'skipping algorithm, because skipping too far loses matches silently.'
          : '<span class="tone-red">The matches do not agree with a scan over every offset: a '
            + 'shift went too far and stepped over a match.</span>');
  }

  function apply() {
    var pre = HOP[presetIn.value];
    if (!pre) return;
    textIn.value = pre.text; patIn.value = pre.pattern; atIn.value = 1;
    redraw();
  }
  var START = HOP[presetIn.value];
  if (START && !textIn.value) { textIn.value = START.text; patIn.value = START.pattern; }
  presetIn.addEventListener('change', apply);
  textIn.addEventListener('input', redraw);
  patIn.addEventListener('input', redraw);
  atIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Shifting by more than one, and the text that stops it",
        subtitle="Characters skipped and comparisons made, against naive matching and KMP",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type a text and a pattern, and watch the shifts"),
        panel_intro=cfg.get(
            "panel_intro",
            "The shift table is built from the pattern and the shifts are decided by the text. "
            "Match positions are checked against a scan over every offset on every keystroke, "
            "because an algorithm whose whole idea is skipping can skip over an answer.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# rabin -- the collision, produced rather than described
# ---------------------------------------------------------------------------

_RA_PRESETS = [
    {
        "id": "english",
        "label": "prose, base 256, and a modulus that collides",
        "text": "the rain in spain stays mainly in the plain",
        "pattern": "ain",
        "base": "256",
        "mod": "41",
        "note": "four real matches and three windows whose hash matches and whose text does not",
    },
    {
        "id": "dna",
        "label": "four bases, base 4, modulus 13",
        "text": "GATTACAGATTACCAGATTACAGGATTACAGATTAC",
        "pattern": "GATTACA",
        "base": "4",
        "mod": "13",
        "note": "a seven-character pattern and a two-digit modulus: collisions are not rare here",
    },
    {
        "id": "binary",
        "label": "two letters, where collisions are worst",
        "text": "101100101101001011010010110100101101",
        "pattern": "10110",
        "base": "2",
        "mod": "11",
        "note": "five real matches and four spurious ones, on thirty-two windows",
    },
    {
        "id": "abra",
        "label": "a repetitive text with a short pattern",
        "text": "abracadabra abracadabra abracadabra",
        "pattern": "abra",
        "base": "256",
        "mod": "13",
        "note": "six matches, four collisions, and every collision costs a full re-comparison",
    },
    {
        "id": "clean",
        "label": "the same prose at a modulus large enough",
        "text": "the rain in spain stays mainly in the plain",
        "pattern": "ain",
        "base": "256",
        "mod": "1000003",
        "note": "no collision at all, which is a fact about this text and not a guarantee",
    },
]

_RA_BASES = [("2", "2"), ("4", "4"), ("10", "10"), ("31", "31"), ("128", "128"), ("256", "256")]
_RA_MODS = [(m, m) for m in
            ("7", "11", "13", "17", "19", "23", "29", "31", "37", "41", "53", "67",
             "97", "101", "1009", "10007", "1000003")]


def _rabin(cfg):
    chosen = _chosen(_RA_PRESETS, cfg)
    markup = (
        _toolbar(
            "A rolling hash, and the collisions it actually produces",
            "hashes equal, characters not",
            [("cyan", "a real match"), ("red", "a hash collision that is not a match"),
             ("muted", "the hash did not match")],
        )
        + _stage(_svg("raBars", "0 0 660 150",
                      "One bar per window, its height the window's hash, with the pattern's "
                      "hash drawn across."))
        + _strip("raStrip")
        + _table("raWindows")
        + _table("raSweep")
        + _banner("raStatus")
    )
    controls = (
        _select("raPreset", "Worked example", _options(_RA_PRESETS), chosen["id"])
        + _text("raText", "The text", "the rain in spain stays mainly in the plain")
        + _text("raPattern", "The pattern", "ain")
        + _select("raBase", "The base", _RA_BASES, chosen["base"])
        + _select("raMod", "The modulus", _RA_MODS, chosen["mod"])
        + _kpis([("Windows", "raWin"), ("Hashes equal to the pattern's", "raEqual"),
                 ("Real matches", "raHits"), ("Collisions", "raSpur"),
                 ("Characters compared verifying", "raComp"),
                 ("Wasted on collisions", "raWaste"),
                 ("Primes under 200 that collide", "raBad"),
                 ("Largest of them", "raLast")])
        + _hint(
            "raHint",
            "The hash of a window is its characters read as digits in the chosen base, taken "
            "modulo the chosen modulus, and the next window is computed from this one by "
            "removing the leading digit and appending the trailing one. Equal hashes are NOT a "
            "match: the algorithm must compare the characters, and the count of times it had "
            "to is on the page. Lower the modulus until the collisions appear, then raise it "
            "and watch them go — and notice that they do not go monotonically.",
        )
    )
    script = _BASE_JS + _ONE_TEXT + _presets_js(
        "RAP", _RA_PRESETS, ["text", "pattern", "base", "mod", "note"]) + r"""
  var presetIn = document.getElementById('raPreset'), textIn = document.getElementById('raText');
  var patIn = document.getElementById('raPattern'), baseIn = document.getElementById('raBase');
  var modIn = document.getElementById('raMod');
  var bars = document.getElementById('raBars'), strip = document.getElementById('raStrip');
  var wins = document.getElementById('raWindows'), sweepT = document.getElementById('raSweep');
  var status = document.getElementById('raStatus');
  var KPIS = ['raWin', 'raEqual', 'raHits', 'raSpur', 'raComp', 'raWaste', 'raBad', 'raLast'];

  function blank(why) {
    bars.innerHTML = ''; strip.innerHTML = ''; wins.innerHTML = ''; sweepT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> Type a text and a pattern.';
  }

  function redraw() {
    var parsed = skParse(textIn.value, patIn.value, 160, 24);
    if (parsed.bad) { blank(parsed.bad); return; }
    var t = parsed.t, p = parsed.p, m = p.length;
    var b = parseInt(baseIn.value, 10), mod = parseInt(modIn.value, 10);

    var run = rollingHash(t, p, b, mod), res = run.result;
    var truth = skBrute(t, p), right = skSame(res.hits, truth);

    /* The rolling update is the one place a value comes from a previous value
       rather than from the input, so every window's hash is recomputed from
       scratch and the two are required to agree. */
    var drift = 0;
    run.trace.forEach(function (w) {
      if (skHashOf(t.slice(w.at, w.at + m), b, mod) !== w.hash) drift += 1;
    });

    var maxHash = 1;
    run.trace.forEach(function (w) { if (Number(w.hash) > maxHash) maxHash = Number(w.hash); });
    bars.innerHTML = skBars(run.trace.map(function (w) { return Number(w.hash); }),
                            { bound: Number(res.target), boundLabel: 'the pattern hashes to '
                              + res.target, width: 660 });
    strip.innerHTML = '<span class="tone-muted">text, real matches marked:</span> '
      + skMarkup(t, res.hits, m, 0, 200);

    var rows = '';
    run.trace.forEach(function (w) {
      if (!w.equal && rows.split('<tr').length > 18) return;
      if (!w.equal) return;
      rows += '<tr class="' + (w.match ? 'tone-cyan' : 'tone-red') + '"><th class="rowhead">'
        + w.at + '</th><td class="tt">' + skEsc(t.slice(w.at, w.at + m)) + '</td><td>'
        + w.hash + '</td><td>' + res.target + '</td><td>'
        + (w.match ? 'a real match' : 'a collision: same hash, different characters')
        + '</td></tr>';
    });
    if (!rows) rows = '<tr><td colspan="5">No window hashed equal to the pattern at all, so '
      + 'there is nothing to verify and no match either.</td></tr>';
    wins.innerHTML = '<caption>Every window whose hash equals the pattern’s. Each one costs '
      + m + ' character comparison' + skPlural(m, '', 's') + ' to settle, whether or not it '
      + 'turns out to be a match</caption><thead><tr><th>offset</th><th>window</th>'
      + '<th>its hash</th><th>the pattern’s</th><th>verdict</th></tr></thead><tbody>'
      + rows + '</tbody>';

    var sw = skModulusSweep(t, p, b, 2, 200);
    var srows = '';
    sw.rows.forEach(function (r) {
      srows += '<tr' + (r.mod === mod ? ' class="tone-cyan"'
                                      : (r.spurious ? ' class="tone-red"' : ''))
        + '><th class="rowhead">' + r.mod + '</th><td>' + r.verifications + '</td><td>'
        + r.hits + '</td><td>' + r.spurious + '</td></tr>';
    });
    sweepT.innerHTML = '<caption>The same text and pattern at every prime modulus under 200. '
      + 'The collisions do not stop at a threshold and start again below it: which moduli '
      + 'collide is a property of this text</caption><thead><tr><th>modulus</th>'
      + '<th>verifications</th><th>matches</th><th>collisions</th></tr></thead><tbody>'
      + srows + '</tbody>';

    var compares = run.counts.compares || 0;
    document.getElementById('raWin').textContent = run.trace.length;
    document.getElementById('raEqual').textContent = res.verifications;
    document.getElementById('raHits').textContent = res.hits.length + ' and ' + truth.length
      + (right ? '' : ' — DISAGREE');
    document.getElementById('raSpur').textContent = res.spurious;
    document.getElementById('raComp').textContent = compares;
    document.getElementById('raWaste').textContent = res.spurious * m;
    document.getElementById('raBad').textContent = sw.collided + ' of ' + sw.tested;
    document.getElementById('raLast').textContent = sw.lastBad === null ? 'none' : sw.lastBad;

    status.innerHTML = '<strong>' + res.spurious + ' collision'
      + skPlural(res.spurious, '', 's') + ' on ' + run.trace.length + ' window'
      + skPlural(run.trace.length, '', 's') + ' at base ' + b + ', modulus ' + mod
      + '.</strong> '
      + (res.spurious
          ? 'Each one is a window whose hash is <span class="tone-red">' + res.target
            + '</span>, the same as the pattern’s, and whose characters are not the '
            + 'pattern. The table above lists them: type one of them out and check by eye. '
            + 'They cost ' + (res.spurious * m) + ' of the ' + compares + ' character '
            + 'comparison' + skPlural(compares, '', 's') + ' made, and nothing about the '
            + 'algorithm noticed anything was wrong — the verification is not an optimisation '
            + 'that can be skipped, it is the only reason the answer is right. '
          : 'None here. That is a measurement of this text at this modulus and it is not a '
            + 'guarantee: of the ' + sw.tested + ' prime moduli under 200, '
            + '<span class="tone-red">' + sw.collided + '</span> produce a collision on this '
            + 'same text. ')
      + 'Across those ' + sw.tested + ' primes, ' + sw.collided + ' collide'
      + (sw.lastBad === null ? '' : ', the largest of them ' + sw.lastBad)
      + (sw.worst ? ', and the worst produces ' + sw.worst + ' collision'
                    + skPlural(sw.worst, '', 's') : '')
      + '. Collisions do not switch off above a threshold; whether a given modulus collides is '
      + 'a fact about this text, and the bound the lesson proves is an EXPECTATION over a '
      + 'randomly chosen modulus, not a promise about the one you picked. '
      + (drift
          ? '<span class="tone-red">' + drift + ' window’s hash disagrees with the same '
            + 'hash recomputed from scratch, so the rolling update has drifted.</span>'
          : 'Every window’s hash was also recomputed from scratch and the two agree, so '
            + 'the rolling update is carrying the right number forward.')
      + (right ? '' : ' <span class="tone-red">The match positions disagree with a scan over '
            + 'every offset.</span>');
  }

  function apply() {
    var pre = RAP[presetIn.value];
    if (!pre) return;
    textIn.value = pre.text; patIn.value = pre.pattern;
    baseIn.value = pre.base; modIn.value = pre.mod;
    redraw();
  }
  var START = RAP[presetIn.value];
  if (START && !textIn.value) { textIn.value = START.text; patIn.value = START.pattern; }
  presetIn.addEventListener('change', apply);
  textIn.addEventListener('input', redraw);
  patIn.addEventListener('input', redraw);
  baseIn.addEventListener('change', redraw);
  modIn.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="A rolling hash, and a collision you can read off the page",
        subtitle="Equal hashes are not a match, and the verification is not optional",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Pick a base and a modulus, and find the collisions"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every hash here is a BigInt, so the collisions are the same on every machine. "
            "The page lists the windows whose hash matched and whose characters did not, and "
            "sweeps every prime modulus under 200 to show how many of them collide on this "
            "text.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# trie -- one pass for every pattern at once, against k passes for k patterns
# ---------------------------------------------------------------------------

_TR_PRESETS = [
    {
        "id": "classic",
        "label": "the four words every account of this uses",
        "words": "he, she, his, hers",
        "prefix": "h",
        "text": "ushers hers his she he",
        "note": "she ends where he ends, so one position reports two patterns at once",
    },
    {
        "id": "shared",
        "label": "words that share a long prefix",
        "words": "interest, interesting, interior, internal, intern",
        "prefix": "inte",
        "text": "the internal interest in interning is interesting",
        "note": "five words, and the trie holds the shared prefix once rather than five times",
    },
    {
        "id": "disjoint",
        "label": "words with nothing in common",
        "words": "alpha, bravo, charlie, delta",
        "prefix": "b",
        "text": "alpha bravo charlie delta echo alphabravo",
        "note": "no sharing at all, so the trie is four separate chains and saves nothing",
    },
    {
        "id": "nested",
        "label": "one word inside another",
        "words": "a, ab, abc, abcd",
        "prefix": "ab",
        "text": "abcdabcab",
        "note": "every position that ends abcd ends abc, ab and a as well: four reports at once",
    },
]


def _trie(cfg):
    chosen = _chosen(_TR_PRESETS, cfg)
    markup = (
        _toolbar(
            "One structure for a whole dictionary",
            "nodes against slots, and one pass against k passes",
            [("cyan", "a node that ends a word"), ("purple", "the prefix you asked for"),
             ("muted", "every other node")],
        )
        + _stage(_svg("trTree", "0 0 660 260",
                      "The trie, each edge labelled with its character and each word-ending "
                      "node marked."))
        + _table("trWords")
        + _table("trHits")
        + _banner("trStatus")
    )
    controls = (
        _select("trPreset", "Worked example", _options(_TR_PRESETS), chosen["id"])
        + _text("trWordList", "The words, comma separated", "he, she, his, hers")
        + _text("trPrefix", "Look up every word starting with", "h")
        + _text("trText", "The text to scan for all of them at once", "ushers hers his she he")
        + _kpis([("Words", "trN"), ("Trie nodes", "trNodes"),
                 ("Array slots a dense node table would take", "trSlots"),
                 ("Characters in the words", "trChars"),
                 ("Words with that prefix", "trPrefixN"),
                 ("Matches, one pass", "trMatch"),
                 ("Matches, by definition", "trTruth"),
                 ("Comparisons: one pass against k passes", "trComp")])
        + _hint(
            "trHint",
            "Words are separated by commas. A trie stores the shared prefix once, so the node "
            "count is the number of DISTINCT prefixes and not the total number of characters — "
            "the two KPIs above say how much that saved on these words. Aho-Corasick then adds "
            "a failure link to every node, exactly as KMP does to a single pattern, and one "
            "pass over the text reports every occurrence of every word. It is checked against "
            "scanning the text separately for each one.",
        )
    )
    script = _TREE_JS + _ONE_TEXT + _presets_js(
        "TRP", _TR_PRESETS, ["words", "prefix", "text", "note"]) + r"""
  var presetIn = document.getElementById('trPreset');
  var wordsIn = document.getElementById('trWordList');
  var prefixIn = document.getElementById('trPrefix'), textIn = document.getElementById('trText');
  var treeEl = document.getElementById('trTree'), wordsT = document.getElementById('trWords');
  var hitsT = document.getElementById('trHits'), status = document.getElementById('trStatus');
  var KPIS = ['trN', 'trNodes', 'trSlots', 'trChars', 'trPrefixN', 'trMatch', 'trTruth', 'trComp'];

  function blank(why) {
    treeEl.innerHTML = ''; wordsT.innerHTML = ''; hitsT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> Words are comma separated: '
      + '<span class="tt">he, she, his, hers</span>.';
  }

  function redraw() {
    var words = String(wordsIn.value || '').split(',').map(function (w) { return w.trim(); })
                  .filter(function (w) { return w.length; });
    if (!words.length) { blank('no words'); return; }
    if (words.length > 10) { blank('this mode stops at ten words'); return; }
    var tooLong = words.filter(function (w) { return w.length > 14; });
    if (tooLong.length) { blank('a word is longer than fourteen characters'); return; }
    var text = String(textIn.value || '');
    if (!text.length) { blank('the text is empty'); return; }
    if (text.length > 160) { blank('the text is longer than 160 characters'); return; }

    var sigma = skAlphabet(words.join('')).length;
    var trie = trieBuild(words, sigma || 1);
    var prefix = String(prefixIn.value || '');
    var found = triePrefix(trie, prefix).sort();
    var truthPrefix = skPrefixBrute(words, prefix);

    ahoLinks(trie);
    var aho = ahoRun(text, trie);
    var idToWord = {};
    (function walk(n, acc) {
      if (n.end) idToWord[n.id] = acc;
      trieKids(n).forEach(function (k) { walk(k, acc + k.ch); });
    })(trie.root, '');

    var perWord = {}, kmpTotal = 0, truthTotal = 0;
    words.forEach(function (w) {
      var run = kmpRun(text, w);
      var truth = skBrute(text, w);
      perWord[w] = { kmp: run.result.hits, truth: truth, compares: run.counts.compares || 0,
                     agree: skSame(run.result.hits, truth) };
      kmpTotal += run.counts.compares || 0;
      truthTotal += truth.length;
    });

    treeEl.innerHTML = drawTree(null, trie.root, trieKids, function (n) {
      return n.ch === '' ? '·' : n.ch;
    }, { width: 660, height: 260 });

    var rows = '';
    words.forEach(function (w) {
      var d = perWord[w];
      rows += '<tr' + (found.indexOf(w) >= 0 ? ' class="tone-purple"' : '')
        + '><th class="rowhead tt">' + skEsc(w) + '</th><td>' + w.length + '</td><td>'
        + (found.indexOf(w) >= 0 ? 'yes' : 'no') + '</td><td>' + d.truth.length + '</td><td>'
        + d.compares + '</td><td>' + (d.agree ? '' : '<span class="tone-red">KMP disagrees</span>')
        + '</td></tr>';
    });
    wordsT.innerHTML = '<caption>One row per word: its length, whether it starts with the '
      + 'prefix you asked for, how many times it occurs in the text, and what a separate KMP '
      + 'pass for it alone cost</caption><thead><tr><th>word</th><th>length</th>'
      + '<th>has the prefix</th><th>occurrences</th><th>KMP comparisons</th><th></th>'
      + '</tr></thead><tbody>' + rows + '</tbody>';

    var hrows = '', ahoTotal = 0, wrong = 0;
    var byWord = {};
    aho.result.hits.forEach(function (h) {
      var w = idToWord[h.node];
      if (w === undefined) { wrong += 1; return; }
      (byWord[w] = byWord[w] || []).push(h.at - w.length + 1);
      ahoTotal += 1;
    });
    words.forEach(function (w) {
      var mine = (byWord[w] || []).slice().sort(function (a, b) { return a - b; });
      var truth = perWord[w].truth;
      var ok = skSame(mine, truth);
      if (!ok) wrong += 1;
      hrows += '<tr' + (ok ? '' : ' class="tone-red"') + '><th class="rowhead tt">' + skEsc(w)
        + '</th><td>' + (mine.length ? mine.join(', ') : '—') + '</td><td>'
        + (truth.length ? truth.join(', ') : '—') + '</td><td>'
        + (ok ? 'agree' : 'DISAGREE') + '</td></tr>';
    });
    hitsT.innerHTML = '<caption>What one Aho-Corasick pass reported, against scanning the text '
      + 'separately for each word</caption><thead><tr><th>word</th><th>one pass</th>'
      + '<th>by definition</th><th></th></tr></thead><tbody>' + hrows + '</tbody>';

    var chars = words.reduce(function (a, w) { return a + w.length; }, 0);
    document.getElementById('trN').textContent = words.length;
    document.getElementById('trNodes').textContent = trie.count;
    document.getElementById('trSlots').textContent = trie.slots + ' at sigma = ' + (sigma || 1);
    document.getElementById('trChars').textContent = chars;
    document.getElementById('trPrefixN').textContent = found.length + ' and ' + truthPrefix.length
      + (skSame(found, truthPrefix) ? '' : ' — DISAGREE');
    document.getElementById('trMatch').textContent = ahoTotal;
    document.getElementById('trTruth').textContent = truthTotal;
    document.getElementById('trComp').textContent = (aho.counts.compares || 0) + ' against '
      + kmpTotal;

    var shared = chars + 1 - trie.count;
    status.innerHTML = '<strong>' + words.length + ' word'
      + skPlural(words.length, '', 's') + ', ' + chars + ' character'
      + skPlural(chars, '', 's') + ', ' + trie.count + ' node'
      + skPlural(trie.count, '', 's') + '.</strong> '
      + (shared > 0
          ? 'The words share <span class="tone-cyan">' + shared + '</span> character position'
            + skPlural(shared, '', 's') + ', and the trie stores each shared prefix once. '
          : 'These words share no prefix at all, so the trie is ' + words.length
            + ' separate chains and stores nothing twice that it would not have stored anyway. ')
      + 'Held as one array of sigma slots per node it would take <span class="tone-amber">'
      + trie.slots + '</span> cells against ' + trie.count + ' map entries — the space question '
      + 'answered with two numbers rather than with a word. '
      + 'The prefix <span class="tt">' + skEsc(prefix) + '</span> matched ' + found.length
      + ' word' + skPlural(found.length, '', 's')
      + (skSame(found, truthPrefix)
          ? ', the same as filtering the list. '
          : ', and <span class="tone-red">filtering the list gives ' + truthPrefix.length
            + '</span>. ')
      + 'One Aho-Corasick pass over ' + text.length + ' character'
      + skPlural(text.length, '', 's') + ' reported ' + ahoTotal + ' occurrence'
      + skPlural(ahoTotal, '', 's') + ' of all ' + words.length + ' words for '
      + (aho.counts.compares || 0) + ' comparison' + skPlural(aho.counts.compares || 0, '', 's')
      + ', against ' + kmpTotal + ' for ' + words.length + ' separate KMP passes. '
      + (wrong
          ? '<span class="tone-red">' + wrong + ' word' + skPlural(wrong, '', 's')
            + ' where the one pass and the separate scans disagree.</span>'
          : 'Every word’s positions agree with scanning the text for it alone, which is '
            + 'the check that matters: a failure link that points to the wrong node loses '
            + 'occurrences of one word while every other word still reports correctly.');
  }

  function apply() {
    var pre = TRP[presetIn.value];
    if (!pre) return;
    wordsIn.value = pre.words; prefixIn.value = pre.prefix; textIn.value = pre.text;
    redraw();
  }
  var START = TRP[presetIn.value];
  if (START && !wordsIn.value) {
    wordsIn.value = START.words; prefixIn.value = START.prefix; textIn.value = START.text;
  }
  presetIn.addEventListener('change', apply);
  wordsIn.addEventListener('input', redraw);
  prefixIn.addEventListener('input', redraw);
  textIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="A trie, and one pass that finds every word at once",
        subtitle="Nodes against array slots, and one scan against one scan per word",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type a dictionary and a text to scan"),
        panel_intro=cfg.get(
            "panel_intro",
            "The trie is built from the words you type and drawn as a tree. Prefix queries are "
            "checked against filtering the word list, and the single Aho-Corasick pass is "
            "checked word by word against scanning the text separately for each one.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# suffix -- every suffix in order, and what that order then answers
# ---------------------------------------------------------------------------

_SU_PRESETS = [
    {
        "id": "banana",
        "label": "banana",
        "text": "banana",
        "note": "six suffixes, two doubling rounds, and a longest repeat of ana",
    },
    {
        "id": "mississippi",
        "label": "mississippi",
        "text": "mississippi",
        "note": "the standard example: issi repeats, and the LCP array finds it in one pass",
    },
    {
        "id": "abracadabra",
        "label": "abracadabra",
        "text": "abracadabra",
        "note": "abra occurs twice and is the longest repeated substring",
    },
    {
        "id": "distinct",
        "label": "no character repeated at all",
        "text": "abcdefgh",
        "note": "every LCP is 0, so the number of distinct substrings is exactly n(n + 1)/2",
    },
    {
        "id": "uniform",
        "label": "one letter, repeated",
        "text": "aaaaaaaa",
        "note": "the other extreme: only n distinct substrings, and the LCP array is a staircase",
    },
]


def _suffix(cfg):
    chosen = _chosen(_SU_PRESETS, cfg)
    markup = (
        _toolbar(
            "Every suffix, in order",
            "prefix doubling against sorting the suffixes as strings",
            [("cyan", "the suffix at the chosen rank"), ("purple", "its overlap with the one above"),
             ("muted", "the rest of the order")],
        )
        + _stage(_svg("suBars", "0 0 660 150",
                      "One bar per adjacent pair in the sorted order, its height the length "
                      "of their longest common prefix."))
        + _table("suRounds")
        + _table("suArray")
        + _banner("suStatus")
    )
    controls = (
        _select("suPreset", "Worked example", _options(_SU_PRESETS), chosen["id"])
        + _text("suText", "The text", "banana")
        + _range("suAt", "Highlight rank", 1, 24, 1)
        + _kpis([("Length n", "suN"), ("Doubling rounds", "suRoundsN"),
                 ("Comparisons, prefix doubling", "suComp"),
                 ("The suffix array agrees with sorting", "suAgree"),
                 ("The LCP array agrees with comparing", "suLcp"),
                 ("Longest repeated substring", "suRepeat"),
                 ("Distinct substrings", "suDistinct"),
                 ("All substrings, with repeats", "suAll")])
        + _hint(
            "suHint",
            "Prefix doubling sorts the suffixes by their first character, then uses the ranks "
            "from that round to sort by 2, 4, 8 characters at a time — so each round compares "
            "PAIRS OF RANKS rather than strings, and there are log2 n of them. The answer is "
            "checked against sorting the suffixes as whole strings, which is the definition and "
            "is quadratic. The LCP array then makes the sorted order answer questions: the "
            "longest repeated substring is its largest entry, and the number of distinct "
            "substrings is n(n + 1)/2 minus the sum of it.",
        )
    )
    script = _BASE_JS + _ONE_TEXT + _presets_js("SUP", _SU_PRESETS, ["text", "note"]) + r"""
  var presetIn = document.getElementById('suPreset'), textIn = document.getElementById('suText');
  var atIn = document.getElementById('suAt'), atOut = document.getElementById('suAtOut');
  var bars = document.getElementById('suBars'), rounds = document.getElementById('suRounds');
  var arr = document.getElementById('suArray'), status = document.getElementById('suStatus');
  var KPIS = ['suN', 'suRoundsN', 'suComp', 'suAgree', 'suLcp', 'suRepeat', 'suDistinct', 'suAll'];

  function blank(why) {
    bars.innerHTML = ''; rounds.innerHTML = ''; arr.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> Type a text of up to 40 '
      + 'characters.';
  }

  function redraw() {
    var s = String(textIn.value || '');
    if (!s.length) { blank('the text is empty'); return; }
    if (s.length > 40) { blank('this mode stops at 40 characters'); return; }

    var run = suffixArray(s), res = run.result;
    var k = kasai(s, res.sa).result;
    var brute = skSuffixBrute(s);
    var saAgree = skSame(res.sa, brute.sa);
    var lcpAgree = skSame(k.lcp, brute.lcp);

    atIn.max = s.length;
    var at = skStep(parseInt(atIn.value, 10), 1, s.length);
    atOut.textContent = at + ' of ' + s.length;

    bars.innerHTML = skBars(k.lcp, { bound: s.length - 1, boundLabel: 'n − 1',
                                     mark: at - 1, width: 660 });

    var rrows = '';
    res.rounds.forEach(function (r, i) {
      rrows += '<tr><th class="rowhead">' + (i + 1) + '</th><td>' + r.k + '</td><td class="tt">'
        + r.order.join(' ') + '</td><td class="tt">' + r.rank.join(' ') + '</td></tr>';
    });
    rounds.innerHTML = '<caption>One row per doubling round: the number of characters the '
      + 'order is correct to, the order itself, and the rank of each starting position'
      + '</caption><thead><tr><th>round</th><th>correct to</th><th>order of starts</th>'
      + '<th>rank per position</th></tr></thead><tbody>' + rrows + '</tbody>';

    var arows = '';
    res.sa.forEach(function (start, rank) {
      arows += '<tr' + (rank === at - 1 ? ' class="tone-cyan"' : '') + '><th class="rowhead">'
        + (rank + 1) + '</th><td>' + start + '</td><td class="tt">' + skEsc(s.slice(start))
        + '</td><td>' + brute.sa[rank] + '</td><td>' + k.lcp[rank] + '</td><td class="tt">'
        + (k.lcp[rank] ? '<span class="tone-purple">' + skEsc(s.slice(start, start + k.lcp[rank]))
                         + '</span>' : '<span class="tone-muted">nothing</span>')
        + '</td></tr>';
    });
    arr.innerHTML = '<caption>The suffix array. The fourth column is the same array produced by '
      + 'sorting the suffixes as whole strings, and the last two are the overlap with the '
      + 'suffix one rank above</caption><thead><tr><th>rank</th><th>starts at</th>'
      + '<th>suffix</th><th>by sorting</th><th>LCP</th><th>the shared prefix</th></tr></thead>'
      + '<tbody>' + arows + '</tbody>';

    var n = s.length;
    var allSubs = n * (n + 1) / 2;
    document.getElementById('suN').textContent = n;
    document.getElementById('suRoundsN').textContent = res.rounds.length;
    document.getElementById('suComp').textContent = run.counts.compares || 0;
    document.getElementById('suAgree').textContent = saAgree ? 'yes' : 'NO';
    document.getElementById('suLcp').textContent = lcpAgree ? 'yes' : 'NO';
    document.getElementById('suRepeat').textContent = k.longestRepeat
      + (k.longestRepeat ? ' — ' + skEsc(s.slice(k.repeatAt, k.repeatAt + k.longestRepeat))
                         : ' — nothing repeats');
    document.getElementById('suDistinct').textContent = String(k.distinctSubstrings);
    document.getElementById('suAll').textContent = allSubs;

    var lcpSum = k.lcp.reduce(function (a, v) { return a + v; }, 0);
    status.innerHTML = '<strong>' + res.rounds.length + ' doubling round'
      + skPlural(res.rounds.length, '', 's') + ' on ' + n + ' character'
      + skPlural(n, '', 's') + ', ' + (run.counts.compares || 0) + ' comparison'
      + skPlural(run.counts.compares || 0, '', 's') + '.</strong> '
      + (saAgree
          ? 'The order agrees with sorting the suffixes as whole strings. '
          : '<span class="tone-red">The order disagrees with sorting the suffixes as whole '
            + 'strings, so prefix doubling has not converged.</span> ')
      + (lcpAgree
          ? 'Kasai’s one pass agrees with comparing each adjacent pair character by '
            + 'character. '
          : '<span class="tone-red">Kasai’s pass disagrees with comparing each adjacent '
            + 'pair character by character.</span> ')
      + 'There are ' + allSubs + ' substrings counted with repeats and '
      + '<span class="tone-cyan">' + k.distinctSubstrings + '</span> distinct ones: the '
      + 'difference is exactly the sum of the LCP array, ' + lcpSum + ', because each entry '
      + 'counts the prefixes this suffix shares with the one above and therefore contributes '
      + 'no new substring. '
      + (k.longestRepeat
          ? 'The longest repeated substring is <span class="tt">'
            + skEsc(s.slice(k.repeatAt, k.repeatAt + k.longestRepeat)) + '</span> at '
            + k.longestRepeat + ' character' + skPlural(k.longestRepeat, '', 's')
            + ', and it is the largest LCP entry — a repeated substring is a prefix shared by '
            + 'two suffixes, and in sorted order the two are neighbours. '
          : 'No substring repeats, so every LCP entry is zero and the two counts of substrings '
            + 'are the same number. ')
      + 'The round count is log2 n, which is a bound; the comparison count beside it is what '
      + 'this text cost.';
  }

  function apply() {
    var pre = SUP[presetIn.value];
    if (!pre) return;
    textIn.value = pre.text; atIn.value = 1;
    redraw();
  }
  var START = SUP[presetIn.value];
  if (START && !textIn.value) textIn.value = START.text;
  presetIn.addEventListener('change', apply);
  textIn.addEventListener('input', redraw);
  atIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The suffix array, and the questions a sorted order answers",
        subtitle="Prefix doubling against sorting the suffixes, and the LCP array against comparing them",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type a text and sort every suffix of it"),
        panel_intro=cfg.get(
            "panel_intro",
            "Prefix doubling reaches the sorted order in log2 n rounds by sorting pairs of "
            "ranks. The result is checked against sorting the suffixes as whole strings, and "
            "the LCP array against comparing each adjacent pair character by character.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# automaton -- a table that costs (m + 1) * sigma, and a run that costs n
# ---------------------------------------------------------------------------

_AU_PRESETS = [
    {
        "id": "ababc",
        "label": "a pattern with a border, over three letters",
        "pattern": "ababc",
        "text": "abababcababcabababc",
        "note": "state 4 on an a goes to 3, not to 0: the border is in the table",
    },
    {
        "id": "aaab",
        "label": "a run of one letter",
        "pattern": "aaab",
        "text": "aaaaabaaabaaaab",
        "note": "every a climbs one state and saturates at 3, which is the longest border",
    },
    {
        "id": "binary",
        "label": "two letters, so the table is narrow and tall",
        "pattern": "10110",
        "text": "101100101101001011010010110100101101",
        "note": "sigma = 2 makes the table 2(m + 1) cells, the cheapest it can be",
    },
    {
        "id": "distinct",
        "label": "no repeated character: every mismatch goes to 0",
        "pattern": "abcd",
        "text": "abcabcdabdabcd",
        "note": "with no border anywhere, the table is the same as restarting from scratch",
    },
    {
        "id": "wide",
        "label": "a larger alphabet, and the table grows with it",
        "pattern": "the",
        "text": "the theory of the theatre is the thing",
        "note": "the run still takes exactly n steps; only the table got bigger",
    },
]


def _automaton(cfg):
    chosen = _chosen(_AU_PRESETS, cfg)
    markup = (
        _toolbar(
            "The matcher as a machine",
            "a table built once, then exactly one step per character",
            [("cyan", "the accepting state"), ("purple", "the state at the chosen position"),
             ("muted", "every other transition")],
        )
        + _stage(_svg("auBars", "0 0 660 150",
                      "One bar per text position, its height the state the machine is in "
                      "after reading that character."))
        + _strip("auStrip")
        + _table("auTable")
        + _banner("auStatus")
    )
    controls = (
        _select("auPreset", "Worked example", _options(_AU_PRESETS), chosen["id"])
        + _text("auPattern", "The pattern", "ababc")
        + _text("auText", "The text", "abababcababcabababc")
        + _range("auAt", "Show the state after character", 1, 60, 1)
        + _kpis([("States", "auStates"), ("Alphabet size", "auSigma"),
                 ("Table cells", "auCells"), ("Writes to build it", "auBuild"),
                 ("Steps to run it", "auSteps"), ("Comparisons, KMP", "auKmp"),
                 ("Cells per text character", "auRatio"),
                 ("Matches, and matches by definition", "auHits")])
        + _hint(
            "auHint",
            "The automaton has one state per number of pattern characters matched so far, and "
            "a transition for every character of the alphabet, so the table is (m + 1) times "
            "sigma cells. Running it is then exactly one array lookup per text character with "
            "no comparison and no back-up at all — the run is n steps whatever the text is. "
            "That is the trade the lesson is about, and both halves of it are numbers above: "
            "widen the alphabet and the table grows while the run does not move.",
        )
    )
    script = _RATIO_JS + _ONE_TEXT + _presets_js("AUP", _AU_PRESETS, ["pattern", "text", "note"]) + r"""
  var presetIn = document.getElementById('auPreset'), patIn = document.getElementById('auPattern');
  var textIn = document.getElementById('auText');
  var atIn = document.getElementById('auAt'), atOut = document.getElementById('auAtOut');
  var bars = document.getElementById('auBars'), strip = document.getElementById('auStrip');
  var table = document.getElementById('auTable'), status = document.getElementById('auStatus');
  var KPIS = ['auStates', 'auSigma', 'auCells', 'auBuild', 'auSteps', 'auKmp', 'auRatio',
              'auHits'];

  function blank(why) {
    bars.innerHTML = ''; strip.innerHTML = ''; table.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> Type a pattern and a text.';
  }

  function redraw() {
    var parsed = skParse(textIn.value, patIn.value, 120, 12);
    if (parsed.bad) { blank(parsed.bad); return; }
    var t = parsed.t, p = parsed.p, m = p.length;
    var alphabet = skAlphabet(t + p);
    if (alphabet.length > 14) { blank('this mode stops at fourteen distinct characters'); return; }

    var built = dfaTable(p, alphabet);
    var run = dfaRun(t, built.table, m);
    var truth = skBrute(t, p), right = skSame(run.result.hits, truth);
    var kmp = kmpRun(t, p);

    atIn.max = t.length;
    var at = skStep(parseInt(atIn.value, 10), 1, t.length);
    atOut.textContent = at + ' of ' + t.length;
    var here = run.trace[at - 1];

    bars.innerHTML = skBars(run.trace.map(function (s) { return s.state; }),
                            { bound: m, boundLabel: 'state ' + m + ' is a match',
                              mark: at - 1, width: 660 });
    strip.innerHTML = '<span class="tone-muted">text, matches marked:</span> '
      + skMarkup(t, run.result.hits, m, 0, 200)
      + '<br><span class="tone-muted">after character ' + at + ' ('
      + skEsc(t[at - 1] === ' ' ? '·' : t[at - 1]) + ') the machine is in state '
      + here.state + (here.state === m ? ', which accepts' : '') + '.</span>';

    var head = alphabet.map(function (ch) {
      return '<th>' + skEsc(ch === ' ' ? '·' : ch) + '</th>';
    }).join('');
    var rows = '';
    built.table.forEach(function (row, st) {
      var cells = alphabet.map(function (ch) {
        var to = row[ch];
        var cls = to === m ? ' class="tone-cyan"' : (to === 0 ? ' class="tone-muted"' : '');
        return '<td' + cls + '>' + to + '</td>';
      }).join('');
      rows += '<tr' + (st === here.state ? ' class="tone-purple"' : '')
        + '><th class="rowhead">' + st + '</th><td class="tt">'
        + (st ? skEsc(p.slice(0, st)) : '<span class="tone-muted">nothing</span>') + '</td>'
        + cells + '</tr>';
    });
    table.innerHTML = '<caption>The whole transition table: ' + built.states + ' states by '
      + alphabet.length + ' characters. Every entry is the number of pattern characters that '
      + 'would be matched after reading that character in that state</caption><thead><tr>'
      + '<th>state</th><th>matched so far</th>' + head + '</tr></thead><tbody>' + rows
      + '</tbody>';

    var ratio = R(BigInt(built.cells), BigInt(Math.max(1, t.length)));
    document.getElementById('auStates').textContent = built.states;
    document.getElementById('auSigma').textContent = alphabet.length;
    document.getElementById('auCells').textContent = built.cells;
    document.getElementById('auBuild').textContent = built.counts.writes || 0;
    document.getElementById('auSteps').textContent = (run.counts.reads || 0) + ' for n = '
      + t.length;
    document.getElementById('auKmp').textContent = kmp.counts.compares || 0;
    document.getElementById('auRatio').textContent = Rtext(ratio) + ' = '
      + Rnum(ratio).toFixed(2);
    document.getElementById('auHits').textContent = run.result.hits.length + ' and '
      + truth.length + (right ? '' : ' — DISAGREE');

    var steps = run.counts.reads || 0;
    status.innerHTML = '<strong>' + built.cells + ' table cell'
      + skPlural(built.cells, '', 's') + ' built, then ' + steps + ' step'
      + skPlural(steps, '', 's') + ' to read ' + t.length + ' character'
      + skPlural(t.length, '', 's') + '.</strong> '
      + (steps === t.length
          ? 'Exactly one step per character, with no comparison and no back-up anywhere — '
            + 'which is the only matcher on this course whose cost does not depend on the text '
            + 'at all. '
          : '<span class="tone-red">The run took ' + steps + ' steps for ' + t.length
            + ' characters, and it must take exactly one each.</span> ')
      + 'KMP made ' + (kmp.counts.compares || 0) + ' comparison'
      + skPlural(kmp.counts.compares || 0, '', 's') + ' on the same text, so the automaton is '
      + 'ahead on the run and behind on the setup: the table cost '
      + (built.counts.writes || 0) + ' write' + skPlural(built.counts.writes || 0, '', 's')
      + ' and KMP’s failure function costs O(m). '
      + 'The table is ' + Rtext(ratio) + ' cells per text character here, so the automaton pays '
      + 'for itself on a text ' + (Rnum(ratio) > 1 ? 'longer than this one'
          : 'of this length or longer') + ' and not on a short one. '
      + 'Widen the alphabet and the table grows with sigma while the run does not move: that is '
      + 'the whole trade, and it is why KMP — which stores m numbers instead of m times sigma — '
      + 'is what gets used. '
      + (right
          ? 'The ' + truth.length + ' match' + skPlural(truth.length, '', 'es')
            + ' agree with a scan over every offset.'
          : '<span class="tone-red">The matches disagree with a scan over every offset.</span>');
  }

  function apply() {
    var pre = AUP[presetIn.value];
    if (!pre) return;
    patIn.value = pre.pattern; textIn.value = pre.text; atIn.value = 1;
    redraw();
  }
  var START = AUP[presetIn.value];
  if (START && !patIn.value) { patIn.value = START.pattern; textIn.value = START.text; }
  presetIn.addEventListener('change', apply);
  patIn.addEventListener('input', redraw);
  textIn.addEventListener('input', redraw);
  atIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The matcher as a machine, and what the table costs",
        subtitle="(m + 1) times sigma cells built once, then exactly one step per character",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type a pattern and read the whole transition table"),
        panel_intro=cfg.get(
            "panel_intro",
            "The table is built from the pattern by asking, for every state and every "
            "character, how much of the pattern would then be matched. The run that follows "
            "makes no comparison at all, and its cost is the length of the text and nothing "
            "else.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# The dispatch. Unknown raises, and the raise is the contract: a kit that fell
# back to a default would render a finished-looking page carrying another
# lesson's widget, and nothing downstream would notice -- the markup assertions
# pass, labcheck passes, and a reader is shown a suffix array under the heading
# about rolling hashes.
# ---------------------------------------------------------------------------

_MODES = {
    "naive": _naive,
    "kmp": _kmp,
    "horspool": _horspool,
    "rabin": _rabin,
    "trie": _trie,
    "suffix": _suffix,
    "automaton": _automaton,
}

MODES = tuple(sorted(_MODES))


def strings_lab(cfg):
    """The strings course's kit. `cfg["mode"]` chooses the lesson; unknown raises."""
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError(
            "strings_lab: unknown mode %r; the seven modes of the strings course are %s"
            % (mode, ", ".join(MODES))
        )
    return _MODES[mode](cfg or {})


__all__ = ["strings_lab", "SKIT_JS", "MODES"]
