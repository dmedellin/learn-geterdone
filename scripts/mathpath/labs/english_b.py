"""english kit, second half: the new modes of docs/english-v2/PLAN.md section D
that english.py does not build itself (compare, phrasal, letters, stress,
contractions, linking, coverage). english.english_lab dispatches here, so two
engineers can build the thirteen new modes without sharing a file.
Each entry maps a mode name to a function cfg -> Lab.

WHAT EVERY MODE HERE DOES. It states a rule, runs it in the reader's browser on
printed text or a printed word list, prints the score, and prints every row it
counted with the verdict beside it -- the misses first, because the residue is
the lesson. What the page compares the rule WITH is a fact read off a source
the page names: a word's sounds from CMUdict, the form a writer actually used
from the printed lines. The rule's own answer is never in the data.

THE DATA, and where each file comes from:
  scripts/wordlists/b_letters.json, b_stress.json, b_passage_sounds.json
      written by scripts/wordlists/b_sounds.py from CMUdict (BSD-2: the notice
      is scripts/wordlists/b_CMUDICT_LICENSE and is printed under every lab
      that uses one of these files) and, at build time only, Moby
      Part-of-Speech (public domain; no page carries a Moby tag);
  content/english/data/b_compare_concordance.json, b_phrasal_concordance.json,
  b_wilde_excerpt.json
      written by scripts/wordlists/b_concordance.py from the novel (1813) and
      the play (1895), both public domain.

THE PINS. A preset's expectations are what the built page printed under
`node scripts/labcheck.js --observe`, read on fixture pages and checked
against the counts the two data scripts print. They live in the _PINS tables
below, keyed by every state a lesson can ship (a source and a rule, say), so a
lesson that ships a different redraw-only choice still pins what its page
prints.

THE SCRIPT CONTRACT (tests/test_english_b_kit.py enforces it). The emitted
JavaScript is ES5 and holds no double-quote character: it shares one inline
<script> with the rest of the page, and the trading pages' copy lexer pairs
double quotes across scripts. Data is therefore written by `_lit`, which emits
single-quoted literals, never by json.dumps.
"""

import json
import pathlib

from .common import Lab
from .english import MODERN_DATA, MODERN_JS, SCAN_JS

_REPO = pathlib.Path(__file__).resolve().parents[3]


def _data(name):
    return json.loads((_REPO / "content" / "english" / "data" / name).read_text(encoding="utf-8"))


def _wordlist(name):
    return json.loads((_REPO / "scripts" / "wordlists" / name).read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# emitting data as JavaScript without a double quote
# ---------------------------------------------------------------------------

_ESC = {"\\": "\\\\", "'": "\\'", '"': "\\x22", "\n": "\\n", "\r": "\\r", "\t": "\\t",
        "<": "\\x3c", ">": "\\x3e", " ": "\\u2028", " ": "\\u2029"}


def _js(value):
    """A JavaScript literal for plain data: single-quoted, ES5, no double quote."""
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, (int, float)):
        return repr(value)
    if isinstance(value, str):
        return "'" + "".join(_ESC.get(ch, ch) for ch in value) + "'"
    if isinstance(value, (list, tuple)):
        return "[" + ",".join(_js(v) for v in value) + "]"
    if isinstance(value, dict):
        return "{" + ",".join(_js(str(k)) + ":" + _js(v) for k, v in value.items()) + "}"
    raise TypeError("cannot emit %r" % (value,))


def _lit(name, value):
    """One data line, in the shape tests/test_english_kit.py strips before its ES5 scan."""
    return "  var %s = %s;\n" % (name, _js(value))


# ---------------------------------------------------------------------------
# markup (the same shapes english.py emits; kept here so the files change apart)
# ---------------------------------------------------------------------------

def _kpis(items):
    return ('<div class="kpi-grid">'
            + "".join('<div class="kpi"><span>%s</span><strong id="%s">%s</strong></div>'
                      % (label, kid, start) for label, kid, start in items)
            + '</div>')


def _select(select_id, options, chosen):
    """options: [(value, label)]; the lesson's shipped choice is marked selected."""
    return ('<select id="%s">' % select_id
            + "".join('<option value="%s"%s>%s</option>'
                      % (v, ' selected="selected"' if v == chosen else "", label)
                      for v, label in options)
            + "</select>")


def _table(prefix, rem=20):
    return ('<div class="table-wrap" style="max-height:%drem;overflow-y:auto;">'
            '<table id="%sTable"><thead><tr id="%sCols"></tr></thead>'
            '<tbody id="%sBody"></tbody></table></div>' % (rem, prefix, prefix, prefix))


def _limit(prefix):
    return '<p class="small-copy" id="%sLimit"></p>' % prefix


def _text_block(prefix):
    return '<div class="mathblock" id="%sText" style="font-size:0.84rem;line-height:1.9;"></div>' % prefix


def _pick(cfg, key, allowed, default):
    value = cfg.get(key, default)
    if value not in allowed:
        raise ValueError("english %s: %s must be one of %s, not %r"
                         % (cfg.get("mode"), key, ", ".join(allowed), value))
    return value


def _sub(tiles, keys):
    return {k: tiles[k] for k in keys if k in tiles}


def _cmu_notice():
    text = (_REPO / "scripts" / "wordlists" / "b_CMUDICT_LICENSE").read_text(encoding="utf-8")
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").strip()
    return ('<details><summary>Where the sounds come from</summary>'
            '<p class="small-copy">Every sound, part count and strong part here is read from '
            'the first pronunciation in CMUdict, the Carnegie Mellon University Pronouncing '
            'Dictionary, which records American speech. Its licence asks that this notice '
            'travel with anything made from it:</p>'
            '<pre class="small-copy" style="white-space:pre-wrap;">%s</pre></details>' % text)


# Helpers every mode below shares. bNorm turns the typographic apostrophe into
# the plain one before a word is matched, so I don't is scanned as don't and
# not as don (PLAN D.0).
B_JS = r"""
var bNorm = function (s) { return String(s).replace(/[‘’]/g, '\x27'); };
var bWords = function (s) { return wordsOf(bNorm(s)); };
var bEsc = function (s) {
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
};
var bRow = function (cells) {
  var html = '<tr>', i;
  for (i = 0; i < cells.length; i++) html += '<td>' + bEsc(cells[i]) + '</td>';
  return html + '</tr>';
};
var bHead = function (cells) {
  var html = '', i;
  for (i = 0; i < cells.length; i++) html += '<th>' + bEsc(cells[i]) + '</th>';
  return html;
};
/* Distinct items with how often each came, ranked by count, ties by spelling. */
var bTally = function () {
  var counts = {}, order = [];
  return {
    add: function (k, n) {
      if (!Object.prototype.hasOwnProperty.call(counts, k)) { counts[k] = 0; order.push(k); }
      counts[k] += n || 1;
    },
    ranked: function () {
      var out = order.slice();
      out.sort(function (a, b) { return counts[b] - counts[a] || (a < b ? -1 : a > b ? 1 : 0); });
      return out;
    },
    count: function (k) { return counts[k] || 0; },
    size: function () { return order.length; }
  };
};
var bCounted = function (tally, limit) {
  var r = tally.ranked(), out = [], i;
  for (i = 0; i < r.length && (!limit || i < limit); i++) out.push(r[i] + ' (' + tally.count(r[i]) + ')');
  return out.length ? out.join(', ') : 'none';
};
var bOrd = function (n) {
  return ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh'][n - 1] || String(n);
};
var bFromEnd = function (n) { return n === 1 ? 'the last part' : 'the ' + bOrd(n) + ' part from the end'; };
var bSetText = function (id, text) {
  var node = document.getElementById(id);
  if (!node) return;
  node.style.whiteSpace = 'pre-wrap';
  node.textContent = text;
};
"""


# ---------------------------------------------------------------------------
# compare -- -er/-est against more/most by the adjective's parts
# ---------------------------------------------------------------------------

_CP_SOURCES = [("austen", "the novel (1813)"), ("wilde", "the play (1895)"),
               ("modern", "the two modern documents")]
_CP_RULES = [("A", "A: one part, or two ending -y, takes -er and -est"),
             ("B", "B: as A, and two parts ending -ow, -le or -er too")]
_CP_SHOWS = [("misses", "the forms the rule gets wrong"), ("all", "every form counted"),
             ("aside", "what was set aside, and why")]
# Read off fixture pages with labcheck --observe; see the module docstring.
_CP_PINS = {('austen', 'A'): {'cpN': '367',
                   'cpHit': '337 of 367',
                   'cpPct': '91.8%',
                   'cpMiss': '30',
                   'cpFirst': 'handsomest (4), pleasanter (4), handsomer (3), oftener (3), '
                              'pleasantest (2), commonest (1), gentlest (1), minutest (1), more '
                              'angry (1), more likely (1), more strange (1), most likely (1), most '
                              'sure (1), narrowest (1), nobler (1), noblest (1), quieter (1), '
                              'severest (1), stupider (1)'},
 ('wilde', 'A'): {'cpN': '49',
                  'cpHit': '44 of 49',
                  'cpPct': '89.8%',
                  'cpMiss': '5',
                  'cpFirst': 'remotest (2), noblest (1), oftener (1), pleasanter (1)'},
 ('modern', 'A'): {'cpN': '32',
                   'cpHit': '32 of 32',
                   'cpPct': '100.0%',
                   'cpMiss': '0',
                   'cpFirst': 'none'},
 ('austen', 'B'): {'cpN': '367',
                   'cpHit': '341 of 367',
                   'cpPct': '92.9%',
                   'cpMiss': '26',
                   'cpFirst': 'handsomest (4), pleasanter (4), handsomer (3), oftener (3), '
                              'pleasantest (2), commonest (1), minutest (1), more angry (1), more '
                              'likely (1), more strange (1), most likely (1), most sure (1), '
                              'quieter (1), severest (1), stupider (1)'},
 ('wilde', 'B'): {'cpN': '49',
                  'cpHit': '45 of 49',
                  'cpPct': '91.8%',
                  'cpMiss': '4',
                  'cpFirst': 'remotest (2), oftener (1), pleasanter (1)'},
 ('modern', 'B'): {'cpN': '32',
                   'cpHit': '32 of 32',
                   'cpPct': '100.0%',
                   'cpMiss': '0',
                   'cpFirst': 'none'}}


def _compare(cfg):
    source = _pick(cfg, "source", [s for s, _ in _CP_SOURCES], "austen")
    rule = _pick(cfg, "rule", [r for r, _ in _CP_RULES], "A")
    show = _pick(cfg, "show", [s for s, _ in _CP_SHOWS], "misses")
    data = _data("b_compare_concordance.json")["texts"]
    markup = (
        _kpis([("the rule", "cpSays", "&mdash;"), ("forms counted", "cpN", "&mdash;"),
               ("the rule is right", "cpHit", "&mdash;"), ("share right", "cpPct", "&mdash;"),
               ("wrong", "cpMiss", "&mdash;"), ("the forms it gets wrong", "cpFirst", "&mdash;")])
        + _limit("cp")
        + '<div class="table-wrap"><table id="cpBySyll"><thead><tr>'
          '<th>parts in the adjective</th><th>-er or -est used</th><th>more or most used</th>'
          '</tr></thead><tbody id="cpBySyllBody"></tbody></table></div>'
        + _table("cp", 22)
        + _cmu_notice()
    )
    controls = (
        '<label for="cpPreset">Printed text</label> ' + _select("cpPreset", _CP_SOURCES, source)
        + ' <label for="cpRule">Rule</label> ' + _select("cpRule", _CP_RULES, rule)
        + ' <label for="cpShow">List</label> ' + _select("cpShow", _CP_SHOWS, show)
    )
    script = SCAN_JS + B_JS + _lit("CP_DATA", data) + r"""
(function () {
  var el = function (id) { return document.getElementById(id); };
  var NAMES = { austen: 'the novel, 1813', wilde: 'the play, 1895',
                modern: 'the two modern documents' };
  var SAYS = { A: 'one part, or two ending -y: -er and -est; otherwise more and most',
               B: 'one part, or two ending -y, -ow, -le or -er: -er and -est; otherwise more and most' };
  var PARTS = ['', 'one', 'two', 'three', 'four or more'];
  /* The rule. i stands for -er or -est, m for more or most. */
  var predicts = function (adj, parts, rule) {
    if (parts === 1) return 'i';
    if (parts === 2 && /y$/.test(adj)) return 'i';
    if (parts === 2 && rule === 'B' && /(ow|le|er)$/.test(adj)) return 'i';
    return 'm';
  };
  var formOf = function (row) {
    var w = row[0].split(' ');
    return row[4] === 'm' ? w[row[1]] + ' ' + w[row[1] + 1] : w[row[1]];
  };
  var used = function (k) { return k === 'i' ? '-er or -est' : 'more or most'; };
  var draw = function () {
    var source = el('cpPreset').value, rule = el('cpRule').value, show = el('cpShow').value;
    var d = CP_DATA[source] || CP_DATA.austen, rows = d.rows, hit = 0, i, r, p, k;
    var miss = bTally(), by = {}, html = '';
    if (!SAYS[rule]) rule = 'A';
    for (i = 0; i < rows.length; i++) {
      r = rows[i];
      p = predicts(r[2], r[3], rule);
      if (p === r[4]) hit++; else miss.add(formOf(r).toLowerCase());
      k = r[3] > 3 ? 4 : r[3];
      by[k] = by[k] || { i: 0, m: 0 };
      by[k][r[4]]++;
    }
    el('cpSays').textContent = SAYS[rule];
    el('cpN').textContent = String(rows.length);
    el('cpHit').textContent = hit + ' of ' + rows.length;
    el('cpPct').textContent = share1(hit, rows.length);
    el('cpMiss').textContent = String(rows.length - hit);
    el('cpFirst').textContent = bCounted(miss);
    el('cpLimit').textContent = 'Read from ' + NAMES[source] + ': the forms the writers used, '
      + 'not what they meant. The parts are counted by the dictionary, which records American speech.';
    for (k = 1; k <= 4; k++) {
      if (by[k]) html += bRow([PARTS[k], String(by[k].i), String(by[k].m)]);
    }
    el('cpBySyllBody').innerHTML = html;
    html = '';
    if (show === 'aside') {
      el('cpCols').innerHTML = bHead(['words', 'why they are not counted', 'times']);
      for (i = 0; i < d.aside.length; i++) {
        html += bRow([d.aside[i][0], d.aside[i][1], String(d.aside[i][2])]);
      }
      if (!d.aside.length) html = bRow(['nothing was set aside in this text', '', '']);
    } else {
      el('cpCols').innerHTML = bHead(['the printed words', 'form', 'adjective', 'parts',
                                      'the rule says', 'the writer used', '']);
      for (i = 0; i < rows.length; i++) {
        r = rows[i];
        p = predicts(r[2], r[3], rule);
        if (show === 'misses' && p === r[4]) continue;
        html += bRow([r[0], formOf(r), r[2], String(r[3]), used(p), used(r[4]),
                      p === r[4] ? 'right' : 'wrong']);
      }
    }
    el('cpBody').innerHTML = html;
  };
  window.redrawLab = draw;
  el('cpPreset').addEventListener('change', draw);
  el('cpRule').addEventListener('change', draw);
  el('cpShow').addEventListener('change', draw);
  draw();
}());
"""
    keys = ["cpN", "cpHit", "cpPct", "cpMiss", "cpFirst"]
    return Lab(
        title="-er or more, scored on every comparison in the text",
        subtitle="The adjective's parts decide; the printed lines say how often that is right",
        markup=markup, controls=controls,
        panel_title=cfg.get("panel_title", "Choose a text, then a rule"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every -er, -est, more and most before an adjective is listed under the lab "
            "with the words around it. The rule reads only the adjective's parts and its "
            "last letters and says which form a writer should use; the tiles count how "
            "often the writer did."),
        script=script,
        expect={"cpPreset": {s: _sub(_CP_PINS.get((s, rule), {}), keys) for s, _ in _CP_SOURCES},
                "cpRule": {r: _sub(_CP_PINS.get((source, r), {}), keys) for r, _ in _CP_RULES}},
    )


# ---------------------------------------------------------------------------
# phrasal -- which phrasal verbs a text uses, and where the pronoun goes
# ---------------------------------------------------------------------------

_PH_RULES = [("pronoun", "where the pronoun goes"), ("freq", "the commonest, ranked")]
_PH_SOURCES = [("austen", "the novel (1813)"), ("wilde", "the play (1895)")]
# Read off fixture pages with labcheck --observe; see the module docstring.
_PH_PINS = {'austen': {'phN': '473',
            'phTop': 'go away 32, sit down 29, find out 20, come back 16, give up 12',
            'phBetween': '34',
            'phAfter': '8',
            'phPct': '81.0%',
            'phPrep': '347'},
 'wilde': {'phN': '149',
           'phTop': 'sit down 11, go out 9, break off 8, pick up 7, come up 5',
           'phBetween': '16',
           'phAfter': '5',
           'phPct': '76.2%',
           'phPrep': '93'}}
_PH_KEYS = {"pronoun": ["phN", "phBetween", "phAfter", "phPct", "phPrep"],
            "freq": ["phN", "phTop"]}


def _phrasal(cfg):
    rule = _pick(cfg, "rule", [r for r, _ in _PH_RULES], "pronoun")
    source = _pick(cfg, "source", [s for s, _ in _PH_SOURCES], "austen")
    data = _data("b_phrasal_concordance.json")["texts"]
    markup = (
        _kpis([("verb and particle lines", "phN", "&mdash;"),
               ("the commonest five", "phTop", "&mdash;"),
               ("pronoun between verb and particle", "phBetween", "&mdash;"),
               ("particle, then a pronoun", "phAfter", "&mdash;"),
               ("share with the pronoun between", "phPct", "&mdash;"),
               ("verb, preposition, pronoun", "phPrep", "&mdash;")])
        + _limit("ph")
        + _table("ph", 22)
        + '<p class="small-copy">The contrast: a verb, then a preposition (at, to, for, of, '
          'with), then a pronoun. The pronoun comes after a preposition, never before it.</p>'
        + '<div class="table-wrap" style="max-height:16rem;overflow-y:auto;">'
          '<table id="phPrepTable"><thead><tr><th>the printed words</th><th>verb</th>'
          '<th>preposition</th><th>pronoun</th></tr></thead><tbody id="phPrepBody"></tbody>'
          '</table></div>'
    )
    controls = (
        '<label for="phPreset">What to read</label> ' + _select("phPreset", _PH_RULES, rule)
        + ' <label for="phSource">Printed text</label> ' + _select("phSource", _PH_SOURCES, source)
    )
    script = SCAN_JS + B_JS + _lit("PH_DATA", data) + r"""
(function () {
  var el = function (id) { return document.getElementById(id); };
  var PART = setOf(['up', 'out', 'off', 'down', 'away', 'back', 'over']);
  var OBJ = setOf(['me', 'him', 'us', 'them', 'it', 'you']);
  var NAMES = { austen: 'the novel, 1813', wilde: 'the play, 1895' };
  /* One printed line: the verb, its particle, and a pronoun before or after it. */
  var read = function (row) {
    var w = lower(row[0].split(' ')), v = row[1], out = { verb: row[2], form: row[0].split(' ')[v],
      between: '', after: '', particle: '' };
    if (inSet(PART, w[v + 1])) {
      out.particle = w[v + 1];
      if (inSet(OBJ, w[v + 2] || '')) out.after = w[v + 2];
    } else {
      out.between = w[v + 1];
      out.particle = w[v + 2];
    }
    return out;
  };
  var draw = function () {
    var rule = el('phPreset').value, source = el('phSource').value;
    var d = PH_DATA[source] || PH_DATA.austen, i, r, top = bTally(), between = 0, after = 0;
    var html = '', ranked, x;
    for (i = 0; i < d.rows.length; i++) {
      r = read(d.rows[i]);
      top.add(r.verb + ' ' + r.particle);
      if (r.between) between++;
      if (r.after) after++;
    }
    ranked = top.ranked();
    var five = [];
    for (i = 0; i < ranked.length && i < 5; i++) five.push(ranked[i] + ' ' + top.count(ranked[i]));
    el('phN').textContent = String(d.rows.length);
    el('phTop').textContent = five.join(', ');
    el('phBetween').textContent = String(between);
    el('phAfter').textContent = String(after);
    el('phPct').textContent = between + after ? share1(between, between + after) : '—';
    el('phPrep').textContent = String(d.prep.length);
    el('phLimit').textContent = 'Read from ' + NAMES[source] + ', whole. A line is a verb from the '
      + 'printed verb lists and a particle (up, out, off, down, away, back, over), with at most one '
      + 'pronoun between. Her is never counted: it is also the word in her eyes.';
    if (rule === 'freq') {
      el('phCols').innerHTML = bHead(['verb and particle', 'times']);
      for (i = 0; i < ranked.length; i++) html += bRow([ranked[i], String(top.count(ranked[i]))]);
    } else {
      el('phCols').innerHTML = bHead(['the printed words', 'verb', 'particle', 'where the pronoun is']);
      for (i = 0; i < d.rows.length; i++) {
        r = read(d.rows[i]);
        x = r.between ? 'between: ' + r.between : r.after ? 'after: ' + r.after : 'no pronoun';
        html += bRow([d.rows[i][0], r.verb, r.particle, x]);
      }
    }
    el('phBody').innerHTML = html;
    html = '';
    for (i = 0; i < d.prep.length; i++) {
      x = lower(d.prep[i][0].split(' '));
      html += bRow([d.prep[i][0], d.prep[i][2], x[d.prep[i][1] + 1], x[d.prep[i][1] + 2]]);
    }
    el('phPrepBody').innerHTML = html;
  };
  window.redrawLab = draw;
  el('phPreset').addEventListener('change', draw);
  el('phSource').addEventListener('change', draw);
  draw();
}());
"""
    return Lab(
        title="Where the pronoun goes in a phrasal verb",
        subtitle="Every verb and particle in the text, and every verb, preposition and pronoun",
        markup=markup, controls=controls,
        panel_title=cfg.get("panel_title", "Count the lines, then find the pronoun"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every line where a verb is followed by up, out, off, down, away, back or over is "
            "listed under the lab. A pronoun can stand between the verb and the particle (find "
            "it out); after a preposition it can only follow (look at him)."),
        script=script,
        expect={"phPreset": {r: _sub(_PH_PINS.get(source, {}), _PH_KEYS[r]) for r, _ in _PH_RULES},
                "phSource": {s: _sub(_PH_PINS.get(s, {}), _PH_KEYS[rule]) for s, _ in _PH_SOURCES}},
    )


# ---------------------------------------------------------------------------
# letters -- a spelling-to-sound rule scored on the 2,800 words
# ---------------------------------------------------------------------------

_LT_RULES = [
    ("softc", "c before e, i or y says s"),
    ("softg", "g before e, i or y says j"),
    ("magic", "the silent e: the vowel says its name"),
    ("magic_r", "the silent e before r"),
    ("ie", "i before e, except after c"),
    ("ie_ee", "i before e, where it says ee"),
    ("gh", "gh after a vowel: never a g"),
    ("kn_wr_mb", "kn-, wr-, -mb, -mn, -alk, -alm: one letter silent"),
    ("h", "h at the start is said"),
    ("ough", "ough: how many sounds"),
    ("tion", "-tion says shun"),
    ("sion", "-sion: zhun after a vowel, shun after a consonant"),
    ("ture", "-ture says chur"),
    ("cial", "-cial and -tial say shul"),
]
_LT_SHOWS = [("misses", "the words the rule gets wrong"), ("all", "every word scored"),
             ("aside", "the words set aside, and why")]
# Read off fixture pages with labcheck --observe; see the module docstring.
_LT_PINS = {'softc': {'ltN': '348',
           'ltHit': '348 of 348',
           'ltPct': '100.0%',
           'ltMiss': '0',
           'ltFirst': 'none',
           'ltSounds': '—'},
 'softg': {'ltN': '187',
           'ltHit': '177 of 187',
           'ltPct': '94.7%',
           'ltMiss': '10',
           'ltFirst': 'altogether, begin, forget, give, gear, get, gift, girl, target, together',
           'ltSounds': '—'},
 'magic': {'ltN': '140',
           'ltHit': '131 of 140',
           'ltPct': '93.6%',
           'ltMiss': '9',
           'ltFirst': 'come, have, give, lose, love, move, none, prove, some',
           'ltSounds': '—'},
 'magic_r': {'ltN': '19',
             'ltHit': '1 of 19',
             'ltPct': '5.3%',
             'ltMiss': '18',
             'ltFirst': 'bore, care, core, dare, mere, more, pure, rare, scare, score, share, '
                        'shore, spare, stare, store, sure, there, where',
             'ltSounds': '—'},
 'ie': {'ltN': '58',
        'ltHit': '36 of 58',
        'ltPct': '62.1%',
        'ltMiss': '22',
        'ltFirst': 'ancient, efficiency, efficient, eight, eighteen, eighty, either, foreign, '
                   'height, neighbor, neighborhood, neither, protein, science, scientific, '
                   'scientist, society, species, sufficient, weigh, weight, weird',
        'ltSounds': '—'},
 'ie_ee': {'ltN': '18',
           'ltHit': '14 of 18',
           'ltPct': '77.8%',
           'ltMiss': '4',
           'ltFirst': 'either, neither, protein, species',
           'ltSounds': '—'},
 'gh': {'ltN': '42',
        'ltHit': '42 of 42',
        'ltPct': '100.0%',
        'ltMiss': '0',
        'ltFirst': 'none',
        'ltSounds': '—'},
 'kn_wr_mb': {'ltN': '19',
              'ltHit': '19 of 19',
              'ltPct': '100.0%',
              'ltMiss': '0',
              'ltFirst': 'none',
              'ltSounds': '—'},
 'h': {'ltN': '80',
       'ltHit': '77 of 80',
       'ltPct': '96.3%',
       'ltMiss': '3',
       'ltFirst': 'honest, honor, hour',
       'ltSounds': '—'},
 'ough': {'ltN': '10',
          'ltHit': '—',
          'ltPct': '—',
          'ltMiss': '—',
          'ltFirst': '—',
          'ltSounds': '5 sounds in 10 words'},
 'tion': {'ltN': '127',
          'ltHit': '123 of 127',
          'ltPct': '96.9%',
          'ltMiss': '4',
          'ltFirst': 'equation, intention, question, suggestion',
          'ltSounds': '—'},
 'sion': {'ltN': '25',
          'ltHit': '24 of 25',
          'ltPct': '96.0%',
          'ltMiss': '1',
          'ltFirst': 'version',
          'ltSounds': '—'},
 'ture': {'ltN': '20',
          'ltHit': '19 of 20',
          'ltPct': '95.0%',
          'ltMiss': '1',
          'ltFirst': 'mature',
          'ltSounds': '—'},
 'cial': {'ltN': '12',
          'ltHit': '12 of 12',
          'ltPct': '100.0%',
          'ltMiss': '0',
          'ltFirst': 'none',
          'ltSounds': '—'}}


def _letters(cfg):
    ids = [r for r, _ in _LT_RULES]
    rules = list(cfg.get("rules") or ids)
    for r in rules:
        if r not in ids:
            raise ValueError("english letters: unknown rule %r" % r)
    show = _pick(cfg, "show", [s for s, _ in _LT_SHOWS], "misses")
    allrules = _wordlist("b_letters.json")["rules"]
    data = {r: allrules[r] for r in rules}
    markup = (
        _kpis([("the rule", "ltRule", "&mdash;"), ("words scored", "ltN", "&mdash;"),
               ("the rule is right", "ltHit", "&mdash;"), ("share right", "ltPct", "&mdash;"),
               ("wrong", "ltMiss", "&mdash;"), ("the words it gets wrong", "ltFirst", "&mdash;"),
               ("set aside", "ltAside", "&mdash;"), ("different sounds", "ltSounds", "&mdash;")])
        + _limit("lt")
        + _table("lt", 22)
        + _cmu_notice()
    )
    labels = dict(_LT_RULES)
    controls = (
        '<label for="ltPreset">Rule</label> '
        + _select("ltPreset", [(r, labels[r]) for r in rules], rules[0])
        + ' <label for="ltShow">List</label> ' + _select("ltShow", _LT_SHOWS, show)
    )
    script = SCAN_JS + B_JS + _lit("LT_DATA", data) + r"""
(function () {
  var el = function (id) { return document.getElementById(id); };
  var NAME = { a: ['ay'], e: ['ee'], i: ['eye'], o: ['oh'], u: ['oo', 'you'] };
  var GROUP = { kn: 'k in kn-', wr: 'w in wr-', mb: 'b in -mb', mn: 'n in -mn',
                lk: 'l in -alk, -olk', lm: 'l in -alm, -alf' };
  /* Each rule: what it says from the spelling alone, and whether the
     dictionary's fact agrees. The row is [word, ...facts]. */
  var RULES = {
    softc: { says: 'c before e, i or y is said s; otherwise k',
      run: function (r) { var i = r[0].indexOf('c'); return /[eiy]/.test(r[0].charAt(i + 1)) ? 's' : 'k'; } },
    softg: { says: 'g before e, i or y is said j; otherwise g',
      run: function (r) { var i = r[0].indexOf('g'); return /[eiy]/.test(r[0].charAt(i + 1)) ? 'j' : 'g'; } },
    magic: { says: 'in one part ending vowel, consonant, e, the vowel says its name',
      run: function (r) { return NAME[r[0].charAt(r[0].length - 3)].join(' or '); },
      ok: function (r) { return NAME[r[0].charAt(r[0].length - 3)].indexOf(r[1]) >= 0; } },
    magic_r: { says: 'the same rule before r and e: the vowel says its name',
      run: function (r) { return NAME[r[0].charAt(r[0].length - 3)].join(' or '); },
      ok: function (r) { return NAME[r[0].charAt(r[0].length - 3)].indexOf(r[1]) >= 0; } },
    ie: { says: 'i before e, except after c',
      run: function (r) { return r[1] > 0 && r[0].charAt(r[1] - 1) === 'c' ? 'ei' : 'ie'; },
      ok: function (r) { return RULES.ie.run(r) === r[2]; }, fact: function (r) { return r[2]; } },
    ie_ee: { says: 'i before e, except after c, where the letters say ee',
      run: function (r) { return RULES.ie.run(r); },
      ok: function (r) { return RULES.ie.run(r) === r[2]; }, fact: function (r) { return r[2]; } },
    gh: { says: 'gh after a vowel is silent or f, never g',
      run: function () { return 'silent or f'; }, ok: function (r) { return r[1] !== 'g'; } },
    kn_wr_mb: { says: 'one letter of kn-, wr-, -mb, -mn, -alk, -alm and -alf is not said',
      run: function (r) { return GROUP[r[1]] + ': silent'; },
      ok: function (r) { return r[2] === 'silent'; }, fact: function (r) { return r[2]; } },
    h: { says: 'an h before a vowel at the start is said',
      run: function () { return 'said'; } },
    ough: { says: 'no rule: count the sounds', run: null },
    tion: { says: '-tion is said shun', run: function () { return 'shun'; } },
    sion: { says: '-sion is zhun after a vowel letter, shun after a consonant',
      run: function (r) { return /[aeiou]/.test(r[0].charAt(r[0].length - 5)) ? 'zhun' : 'shun'; } },
    ture: { says: '-ture is said chur', run: function () { return 'chur'; } },
    cial: { says: '-cial and -tial are said shul', run: function () { return 'shul'; } }
  };
  var factOf = function (id, r) { return RULES[id].fact ? RULES[id].fact(r) : r[1]; };
  var okOf = function (id, r) { return RULES[id].ok ? RULES[id].ok(r) : RULES[id].run(r) === r[1]; };
  var draw = function () {
    var id = el('ltPreset').value, show = el('ltShow').value;
    if (!LT_DATA[id]) return;
    var d = LT_DATA[id], rule = RULES[id], rows = d.rows, hit = 0, miss = [], i, r, ok;
    var html = '', reasons = Object.keys(d.aside), aside = 0, sounds = bTally();
    for (i = 0; i < reasons.length; i++) aside += d.aside[reasons[i]].length;
    el('ltRule').textContent = rule.says;
    el('ltN').textContent = String(rows.length);
    el('ltAside').textContent = String(aside);
    if (!rule.run) {
      for (i = 0; i < rows.length; i++) sounds.add(rows[i][1]);
      el('ltHit').textContent = '—';
      el('ltPct').textContent = '—';
      el('ltMiss').textContent = '—';
      el('ltFirst').textContent = '—';
      el('ltSounds').textContent = sounds.size() + ' sounds in ' + rows.length + ' words';
    } else {
      for (i = 0; i < rows.length; i++) {
        if (okOf(id, rows[i])) hit++; else miss.push(rows[i][0]);
      }
      el('ltHit').textContent = hit + ' of ' + rows.length;
      el('ltPct').textContent = share1(hit, rows.length);
      el('ltMiss').textContent = String(miss.length);
      el('ltFirst').textContent = miss.length ? miss.join(', ') : 'none';
      el('ltSounds').textContent = '—';
    }
    el('ltLimit').textContent = 'Read from the first pronunciation the dictionary gives, which '
      + 'is American. A word whose sound could come from another letter is set aside, not scored.';
    if (show === 'aside') {
      el('ltCols').innerHTML = bHead(['why it is set aside', 'words', 'how many']);
      for (i = 0; i < reasons.length; i++) {
        html += bRow([reasons[i], d.aside[reasons[i]].join(', '), String(d.aside[reasons[i]].length)]);
      }
      if (!reasons.length) html = bRow(['nothing is set aside for this rule', '', '']);
    } else if (!rule.run) {
      el('ltCols').innerHTML = bHead(['word', 'ough is said']);
      for (i = 0; i < rows.length; i++) html += bRow([rows[i][0], rows[i][1]]);
    } else {
      el('ltCols').innerHTML = bHead(['word', 'the rule says', 'the dictionary says', '']);
      for (i = 0; i < rows.length; i++) {
        r = rows[i];
        ok = okOf(id, r);
        if (show === 'misses' && ok) continue;
        html += bRow([r[0], rule.run(r), factOf(id, r), ok ? 'right' : 'wrong']);
      }
    }
    el('ltBody').innerHTML = html;
  };
  window.redrawLab = draw;
  el('ltPreset').addEventListener('change', draw);
  el('ltShow').addEventListener('change', draw);
  draw();
}());
"""
    keys = ["ltN", "ltHit", "ltPct", "ltMiss", "ltFirst", "ltSounds"]
    return Lab(
        title="A spelling rule against the dictionary",
        subtitle="Each rule reads only the letters; the dictionary says what is actually said",
        markup=markup, controls=controls,
        panel_title=cfg.get("panel_title", "Choose a rule and read its score"),
        panel_intro=cfg.get(
            "panel_intro",
            "The rule is run on the 2,800 words in the page's list and checked against the "
            "first pronunciation in a pronouncing dictionary. The words it gets wrong are "
            "listed first, and the words it was not tried on are listed with the reason."),
        script=script,
        expect={"ltPreset": {r: _sub(_LT_PINS.get(r, {}), keys) for r in rules}},
    )


# ---------------------------------------------------------------------------
# stress -- where the strong part falls, by class and by ending
# ---------------------------------------------------------------------------

_ST_RULES = [
    ("nouns2", "two-part nouns: strong at the front"),
    ("verbs2", "two-part verbs: strong at the back"),
    ("adj2", "two-part adjectives: strong at the front"),
    ("pairs", "words that are both, said both ways"),
    ("tion", "-tion and -sion"), ("ic", "-ic"), ("ical", "-ical"), ("ity", "-ity"),
    ("ate", "-ate verbs"), ("ize", "-ize and -ise"), ("ee", "-ee, -eer, -ese, -ette"),
    ("ly", "adding -ly"), ("ness", "adding -ness"), ("ment", "adding -ment"),
    ("er", "adding -er"), ("ful", "adding -ful"), ("able", "adding -able"),
    ("schwa", "the weak parts: the flat vowel"),
]
_ST_SHOWS = [("misses", "the words the rule gets wrong"), ("all", "every word scored"),
             ("aside", "the words set aside, and why")]
# Read off fixture pages with labcheck --observe; see the module docstring.
_ST_PINS = {'nouns2': {'stN': '231',
            'stHit': '207 of 231',
            'stPct': '89.6%',
            'stMiss': '24',
            'stFirst': 'advice, affair, belief, complaint, constraint, decade, defense, device, '
                       'disease, eighteen, estate, event, exam, extent, fifteen, guitar, hello, '
                       'hotel, july, offense, relief, response, success, technique',
            'stCount': '—',
            'stSchwa': '—',
            'stEr': '—',
            'stIh': '—',
            'stIy': '—'},
 'verbs2': {'stN': '150',
            'stHit': '134 of 150',
            'stPct': '89.3%',
            'stMiss': '16',
            'stFirst': 'alter, argue, differ, enter, frighten, govern, injure, license, listen, '
                       'locate, marry, premise, reckon, strengthen, suffer, threaten',
            'stCount': '—',
            'stSchwa': '—',
            'stEr': '—',
            'stIh': '—',
            'stIy': '—'},
 'adj2': {'stN': '47',
          'stHit': '35 of 47',
          'stPct': '74.5%',
          'stMiss': '12',
          'stFirst': 'afraid, alive, ashamed, aware, distinct, intense, precise, remote, severe, '
                     'toward, unclear, unlike',
          'stCount': '—',
          'stSchwa': '—',
          'stEr': '—',
          'stIh': '—',
          'stIy': '—'},
 'pairs': {'stN': '49',
           'stHit': '—',
           'stPct': '—',
           'stMiss': '—',
           'stFirst': '—',
           'stCount': '49',
           'stSchwa': '—',
           'stEr': '—',
           'stIh': '—',
           'stIy': '—'},
 'tion': {'stN': '152',
          'stHit': '151 of 152',
          'stPct': '99.3%',
          'stMiss': '1',
          'stFirst': 'television',
          'stCount': '—',
          'stSchwa': '—',
          'stEr': '—',
          'stIh': '—',
          'stIy': '—'},
 'ic': {'stN': '28',
        'stHit': '28 of 28',
        'stPct': '100.0%',
        'stMiss': '0',
        'stFirst': 'none',
        'stCount': '—',
        'stSchwa': '—',
        'stEr': '—',
        'stIh': '—',
        'stIy': '—'},
 'ical': {'stN': '16',
          'stHit': '16 of 16',
          'stPct': '100.0%',
          'stMiss': '0',
          'stFirst': 'none',
          'stCount': '—',
          'stSchwa': '—',
          'stEr': '—',
          'stIh': '—',
          'stIy': '—'},
 'ity': {'stN': '27',
         'stHit': '27 of 27',
         'stPct': '100.0%',
         'stMiss': '0',
         'stFirst': 'none',
         'stCount': '—',
         'stSchwa': '—',
         'stEr': '—',
         'stIh': '—',
         'stIy': '—'},
 'ate': {'stN': '36',
         'stHit': '36 of 36',
         'stPct': '100.0%',
         'stMiss': '0',
         'stFirst': 'none',
         'stCount': '—',
         'stSchwa': '—',
         'stEr': '—',
         'stIh': '—',
         'stIy': '—'},
 'ize': {'stN': '14',
         'stHit': '13 of 14',
         'stPct': '92.9%',
         'stMiss': '1',
         'stFirst': 'characterize',
         'stCount': '—',
         'stSchwa': '—',
         'stEr': '—',
         'stIh': '—',
         'stIy': '—'},
 'ee': {'stN': '12',
        'stHit': '8 of 12',
        'stPct': '66.7%',
        'stMiss': '4',
        'stFirst': 'coffee, committee, employee, refugee',
        'stCount': '—',
        'stSchwa': '—',
        'stEr': '—',
        'stIh': '—',
        'stIy': '—'},
 'ly': {'stN': '87',
        'stHit': '83 of 87',
        'stPct': '95.4%',
        'stMiss': '4',
        'stFirst': 'absolutely, necessarily, perfectly, primarily',
        'stCount': '—',
        'stSchwa': '—',
        'stEr': '—',
        'stIh': '—',
        'stIy': '—'},
 'ness': {'stN': '6',
          'stHit': '6 of 6',
          'stPct': '100.0%',
          'stMiss': '0',
          'stFirst': 'none',
          'stCount': '—',
          'stSchwa': '—',
          'stEr': '—',
          'stIh': '—',
          'stIy': '—'},
 'ment': {'stN': '32',
          'stHit': '31 of 32',
          'stPct': '96.9%',
          'stMiss': '1',
          'stFirst': 'advertisement',
          'stCount': '—',
          'stSchwa': '—',
          'stEr': '—',
          'stIh': '—',
          'stIy': '—'},
 'er': {'stN': '50',
        'stHit': '48 of 50',
        'stPct': '96.0%',
        'stMiss': '2',
        'stFirst': 'career, researcher',
        'stCount': '—',
        'stSchwa': '—',
        'stEr': '—',
        'stIh': '—',
        'stIy': '—'},
 'ful': {'stN': '7',
         'stHit': '7 of 7',
         'stPct': '100.0%',
         'stMiss': '0',
         'stFirst': 'none',
         'stCount': '—',
         'stSchwa': '—',
         'stEr': '—',
         'stIh': '—',
         'stIy': '—'},
 'able': {'stN': '10',
          'stHit': '10 of 10',
          'stPct': '100.0%',
          'stMiss': '0',
          'stFirst': 'none',
          'stCount': '—',
          'stSchwa': '—',
          'stEr': '—',
          'stIh': '—',
          'stIy': '—'},
 'schwa': {'stN': '2628 weak parts in 1779 words',
           'stHit': '1387 of 2628',
           'stPct': '52.8%',
           'stMiss': '—',
           'stFirst': '—',
           'stCount': '—',
           'stSchwa': '1387 of 2628',
           'stEr': '400 of 2628',
           'stIh': '352 of 2628',
           'stIy': '348 of 2628'}}


def _stress(cfg):
    ids = [r for r, _ in _ST_RULES]
    rules = list(cfg.get("rules") or ids)
    for r in rules:
        if r not in ids:
            raise ValueError("english stress: unknown rule %r" % r)
    show = _pick(cfg, "show", [s for s, _ in _ST_SHOWS], "misses")
    allrules = _wordlist("b_stress.json")["rules"]
    data = {r: allrules[r] for r in rules}
    markup = (
        _kpis([("the rule", "stRule", "&mdash;"), ("words scored", "stN", "&mdash;"),
               ("the rule is right", "stHit", "&mdash;"), ("share right", "stPct", "&mdash;"),
               ("wrong", "stMiss", "&mdash;"), ("the words it gets wrong", "stFirst", "&mdash;"),
               ("words said both ways", "stCount", "&mdash;")])
        + _kpis([("weak parts with the flat vowel", "stSchwa", "&mdash;"),
                 ("the flat vowel with r", "stEr", "&mdash;"),
                 ("the vowel of sit", "stIh", "&mdash;"),
                 ("the vowel of see", "stIy", "&mdash;")])
        + _limit("st")
        + _table("st", 22)
        + _cmu_notice()
    )
    labels = dict(_ST_RULES)
    controls = (
        '<label for="stPreset">Rule</label> '
        + _select("stPreset", [(r, labels[r]) for r in rules], rules[0])
        + ' <label for="stShow">List</label> ' + _select("stShow", _ST_SHOWS, show)
    )
    script = SCAN_JS + B_JS + _lit("ST_DATA", data) + r"""
(function () {
  var el = function (id) { return document.getElementById(id); };
  var CLASS = { nouns2: [1, 'a two-part noun is strong on its first part'],
                verbs2: [2, 'a two-part verb is strong on its second part'],
                adj2: [1, 'a two-part adjective is strong on its first part'] };
  var END = { tion: [2, 'strong on the part before -tion or -sion'],
              ic: [2, 'strong on the part before -ic'],
              ical: [3, 'strong two parts before -ical'],
              ity: [3, 'strong two parts before -ity'],
              ate: [3, 'a verb in -ate of three or more parts: strong two parts before the ending'],
              ize: [3, 'a word in -ize or -ise of three or more parts: strong two parts before the ending'],
              ee: [1, 'strong on the ending itself: -ee, -eer, -ese, -ette'] };
  var SAME = { ly: '-ly', ness: '-ness', ment: '-ment', er: '-er', ful: '-ful', able: '-able' };
  var WEAK = { u: 'the flat vowel', r: 'the flat vowel with r', i: 'the vowel of sit',
               e: 'the vowel of see', x: 'another vowel' };
  var dash = ['stHit', 'stPct', 'stMiss', 'stFirst', 'stCount', 'stSchwa', 'stEr', 'stIh', 'stIy'];
  /* [the rule says, the dictionary says, right?] for one row of one rule. */
  var judge = function (id, r) {
    var fromEnd;
    if (CLASS[id]) return [bOrd(CLASS[id][0]) + ' part', bOrd(r[1]) + ' part', r[1] === CLASS[id][0]];
    if (END[id]) {
      fromEnd = r[1] - r[2] + 1;
      return [bFromEnd(END[id][0]), bFromEnd(fromEnd) + ', of ' + r[1] + ' parts', fromEnd === END[id][0]];
    }
    if (SAME[id]) {
      return [bOrd(r[3]) + ' part, as in ' + r[1], bOrd(r[2]) + ' part', r[2] === r[3]];
    }
    return null;
  };
  var draw = function () {
    var id = el('stPreset').value, show = el('stShow').value;
    if (!ST_DATA[id]) return;
    var d = ST_DATA[id], rows = d.rows, i, j, r, v, hit = 0, miss = [], html = '';
    var reasons = Object.keys(d.aside), says;
    for (i = 0; i < dash.length; i++) el(dash[i]).textContent = '—';
    el('stN').textContent = String(rows.length);
    el('stLimit').textContent = 'Read from the first pronunciation the dictionary gives, which is '
      + 'American; the ee endings read its last strong part. Which words are nouns, verbs or '
      + 'adjectives was decided once, from a printed word list, and is not on this page.';
    if (id === 'pairs') {
      el('stRule').textContent = 'a noun and a verb with the same spelling, strong on a different part';
      el('stCount').textContent = String(rows.length);
      el('stCols').innerHTML = bHead(['word']);
      for (i = 0; i < rows.length; i++) html += bRow([rows[i][0]]);
      el('stBody').innerHTML = html;
      return;
    }
    if (id === 'schwa') {
      var n = { u: 0, r: 0, i: 0, e: 0, x: 0 }, all = 0;
      el('stRule').textContent = 'the parts the dictionary marks with no beat at all take the flat vowel';
      el('stLimit').textContent += ' A weak part here is one the dictionary marks with no beat at all; '
        + 'a part with a smaller beat is not counted.';
      for (i = 0; i < rows.length; i++) {
        for (j = 0; j < rows[i][1].length; j++) { n[rows[i][1].charAt(j)]++; all++; }
      }
      el('stN').textContent = all + ' weak parts in ' + rows.length + ' words';
      el('stSchwa').textContent = n.u + ' of ' + all;
      el('stEr').textContent = n.r + ' of ' + all;
      el('stIh').textContent = n.i + ' of ' + all;
      el('stIy').textContent = n.e + ' of ' + all;
      el('stPct').textContent = share1(n.u, all);
      el('stHit').textContent = n.u + ' of ' + all;
      el('stCols').innerHTML = bHead(['word', 'its weak parts', '']);
      for (i = 0; i < rows.length; i++) {
        r = rows[i];
        v = [];
        for (j = 0; j < r[1].length; j++) v.push(WEAK[r[1].charAt(j)]);
        says = /^u+$/.test(r[1]);
        if (show === 'misses' && says) continue;
        if (show === 'aside') break;
        html += bRow([r[0], v.join(', '), says ? 'all flat' : 'not all flat']);
      }
      if (show === 'aside') html = bRow(['nothing is set aside: every word of two or more parts is read', '', '']);
      el('stBody').innerHTML = html;
      return;
    }
    el('stRule').textContent = CLASS[id] ? CLASS[id][1] : END[id] ? END[id][1]
      : 'adding ' + SAME[id] + ' leaves the strong part where it was';
    for (i = 0; i < rows.length; i++) {
      if (judge(id, rows[i])[2]) hit++; else miss.push(rows[i][0]);
    }
    el('stHit').textContent = hit + ' of ' + rows.length;
    el('stPct').textContent = share1(hit, rows.length);
    el('stMiss').textContent = String(miss.length);
    el('stFirst').textContent = miss.length ? miss.join(', ') : 'none';
    if (show === 'aside') {
      el('stCols').innerHTML = bHead(['why it is set aside', 'words', 'how many']);
      for (i = 0; i < reasons.length; i++) {
        html += bRow([reasons[i], d.aside[reasons[i]].join(', '), String(d.aside[reasons[i]].length)]);
      }
      if (!reasons.length) html = bRow(['nothing is set aside for this rule', '', '']);
    } else {
      el('stCols').innerHTML = bHead(['word', 'the rule says', 'the dictionary says', '']);
      for (i = 0; i < rows.length; i++) {
        r = judge(id, rows[i]);
        if (show === 'misses' && r[2]) continue;
        html += bRow([rows[i][0], r[0], r[1], r[2] ? 'right' : 'wrong']);
      }
    }
    el('stBody').innerHTML = html;
  };
  window.redrawLab = draw;
  el('stPreset').addEventListener('change', draw);
  el('stShow').addEventListener('change', draw);
  draw();
}());
"""
    keys = ["stN", "stHit", "stPct", "stMiss", "stFirst", "stCount", "stSchwa", "stEr", "stIh", "stIy"]
    return Lab(
        title="Where the strong part falls",
        subtitle="Each rule reads a word's class or ending; the dictionary says which part is strong",
        markup=markup, controls=controls,
        panel_title=cfg.get("panel_title", "Choose a rule and read its score"),
        panel_intro=cfg.get(
            "panel_intro",
            "The rule is run on the 2,800 words in the page's list and checked against the "
            "strong part a pronouncing dictionary marks. The words it gets wrong are listed "
            "first."),
        script=script,
        expect={"stPreset": {r: _sub(_ST_PINS.get(r, {}), keys) for r in rules}},
    )


# ---------------------------------------------------------------------------
# contractions -- how much of not is n't, and the full form behind each
# ---------------------------------------------------------------------------

_CO_SOURCES = [("wilde", "the play: 1,975 words of Act II (1895)"),
               ("austen", "the novel: the 936-word passage (1813)"),
               ("modern", "the two modern documents")]
# Read off fixture pages with labcheck --observe; see the module docstring.
_CO_PINS = {'wilde': {'coN': '1975',
           'coNt': '22',
           'coNot': '14',
           'coPct': '61.1%',
           'coK': '18.2',
           'coTypes': "'t 22, 's 9, 'll 2, 've 2, 'd 1"},
 'austen': {'coN': '936',
            'coNt': '1',
            'coNot': '12',
            'coPct': '7.7%',
            'coK': '5.3',
            'coTypes': "'s 4, 't 1"},
 'modern': {'coN': '1723',
            'coNt': '0',
            'coNot': '10',
            'coPct': '0.0%',
            'coK': '9.9',
            'coTypes': "'s 17"}}


def _contractions(cfg):
    source = _pick(cfg, "source", [s for s, _ in _CO_SOURCES], "wilde")
    texts = {"wilde": _data("b_wilde_excerpt.json")["text"],
             "austen": _data("wordorder_passage.json")["passage"]}
    markup = (
        _kpis([("words read", "coN", "&mdash;"), ("n't", "coNt", "&mdash;"),
               ("not, cannot included", "coNot", "&mdash;"), ("share of not written n't", "coPct", "&mdash;"),
               ("contractions per 1,000 words", "coK", "&mdash;"),
               ("by ending", "coTypes", "&mdash;")])
        + _limit("co")
        + _table("co", 18)
        + '<details open="open"><summary>The text, printed in full</summary>'
        + _text_block("co") + '</details>'
    )
    controls = '<label for="coPreset">Printed text</label> ' + _select("coPreset", _CO_SOURCES, source)
    script = (SCAN_JS + MODERN_JS + B_JS + _lit("MODERN", MODERN_DATA) + _lit("CO_TEXTS", texts)
              + r"""
(function () {
  var el = function (id) { return document.getElementById(id); };
  var NT = { 'won\x27t': 'will not', 'can\x27t': 'can not', 'shan\x27t': 'shall not' };
  var FULL = { 'll': 'will', 'm': 'am', 're': 'are', 've': 'have', 'd': 'would or had',
               's': 'is, has, or belonging to' };
  var NAMES = { wilde: 'the play, 1895: people talking', austen: 'the novel, 1813',
                modern: 'two documents written in 2025 and 2026' };
  var full = function (w) {
    var m;
    if (/n\x27t$/.test(w)) return NT[w] || w.slice(0, -3) + ' not';
    m = /^(.*)\x27(ll|m|re|ve|d|s)$/.exec(w);
    return m ? m[1] + ' + ' + FULL[m[2]] : '';
  };
  var draw = function () {
    var source = el('coPreset').value, text, scan, w, i, t, nt = 0, nots = 0;
    var types = bTally(), seen = bTally(), html = '', m, all = 0, ty, r;
    /* The modern documents are counted without their titles, as the
       word-order lessons count them, and printed with them. */
    if (source === 'modern') {
      text = '';
      scan = '';
      for (i = 0; i < MODERN.docs.length; i++) {
        text += MODERN.docs[i].name + '\n\n' + MODERN.docs[i].text + '\n\n\n';
        scan += MODERN.docs[i].text + '\n';
      }
    } else {
      text = CO_TEXTS[source] || CO_TEXTS.wilde;
      scan = text;
    }
    w = lower(bWords(scan));
    for (i = 0; i < w.length; i++) {
      t = w[i];
      /* cannot is can and not written as one word: its not is a full form. */
      if (t === 'not' || t === 'cannot') nots++;
      m = /\x27(s|ll|m|re|ve|d|t)$/.exec(t);
      if (!m) continue;
      all++;
      if (/n\x27t$/.test(t)) nt++;
      types.add('\x27' + m[1]);
      seen.add(t);
    }
    el('coN').textContent = String(w.length);
    el('coNt').textContent = String(nt);
    el('coNot').textContent = String(nots);
    el('coPct').textContent = nt + nots ? share1(nt, nt + nots) : '—';
    el('coK').textContent = perThousand(all, w.length);
    ty = types.ranked();
    r = [];
    for (i = 0; i < ty.length; i++) r.push(ty[i] + ' ' + types.count(ty[i]));
    el('coTypes').textContent = r.length ? r.join(', ') : 'none';
    el('coLimit').textContent = 'Read from ' + NAMES[source] + '. Every word ending in an apostrophe and '
      + 's, ll, m, re, ve, d or t is counted, and cannot counts as a not written in full; which s is '
      + 'is, has or belonging the page cannot tell, so the list gives all three and you sort them.';
    el('coCols').innerHTML = bHead(['as printed', 'times', 'the full form']);
    ty = seen.ranked();
    for (i = 0; i < ty.length; i++) html += bRow([ty[i], String(seen.count(ty[i])), full(ty[i])]);
    if (!ty.length) html = bRow(['no contractions in this text', '', '']);
    el('coBody').innerHTML = html;
    bSetText('coText', text);
  };
  window.redrawLab = draw;
  el('coPreset').addEventListener('change', draw);
  draw();
}());
""")
    keys = ["coN", "coNt", "coNot", "coPct", "coK", "coTypes"]
    return Lab(
        title="Where the small words went",
        subtitle="Every contraction in the text, with the full form it stands for",
        markup=markup, controls=controls,
        panel_title=cfg.get("panel_title", "Choose a text and count the contractions"),
        panel_intro=cfg.get(
            "panel_intro",
            "Each text is printed under the lab. The tiles count every not and every n't, "
            "and the table lists every contraction with the full form it stands for. The "
            "play is people talking; the novel and the modern documents are written."),
        script=script,
        expect={"coPreset": {s: _sub(_CO_PINS.get(s, {}), keys) for s, _ in _CO_SOURCES}},
    )


# ---------------------------------------------------------------------------
# linking -- what meets at a word boundary
# ---------------------------------------------------------------------------

_LK_RULES = [("cv", "a consonant meets a vowel"), ("vv", "a vowel meets a vowel"),
             ("same", "the same consonant on both sides")]
# Read off fixture pages with labcheck --observe; see the module docstring.
_LK_PINS = {'cv': {'lkN': '740 of 756 scored', 'lkCount': '124', 'lkPct': '16.8%', 'lkUnknown': '16'},
 'vv': {'lkN': '740 of 756 scored', 'lkCount': '53', 'lkPct': '7.2%', 'lkUnknown': '16'},
 'same': {'lkN': '740 of 756 scored', 'lkCount': '16', 'lkPct': '2.2%', 'lkUnknown': '16'}}


def _linking(cfg):
    rule = _pick(cfg, "rule", [r for r, _ in _LK_RULES], "cv")
    sounds = _wordlist("b_passage_sounds.json")["sounds"]
    passage = _data("wordorder_passage.json")["passage"]
    markup = (
        _kpis([("word boundaries scored", "lkN", "&mdash;"),
               ("boundaries of this kind", "lkCount", "&mdash;"),
               ("share of those scored", "lkPct", "&mdash;"),
               ("boundaries with a word the dictionary lacks", "lkUnknown", "&mdash;")])
        + _limit("lk")
        + _text_block("lk")
        + _table("lk", 18)
        + _cmu_notice()
    )
    controls = '<label for="lkPreset">Mark</label> ' + _select("lkPreset", _LK_RULES, rule)
    script = SCAN_JS + B_JS + _lit("LK_SOUNDS", sounds) + _lit("LK_TEXT", passage) + r"""
(function () {
  var el = function (id) { return document.getElementById(id); };
  var VOWEL = setOf(['AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'ER', 'EY', 'IH', 'IY', 'OW', 'OY', 'UH', 'UW']);
  var SAY = { SH: 'sh', ZH: 'zh', CH: 'ch', JH: 'j', NG: 'ng', TH: 'th', DH: 'th', HH: 'h' };
  var say = function (p) { return inSet(VOWEL, p) ? 'a vowel' : (SAY[p] || p.toLowerCase()); };
  var kindOf = function (a, b) {
    var va = inSet(VOWEL, a), vb = inSet(VOWEL, b);
    if (!va && vb) return 'cv';
    if (va && vb) return 'vv';
    if (va) return 'vc';
    return a === b ? 'same' : 'cc';
  };
  var lookup = function (w) {
    var k = w.toLowerCase().replace(/^\x27+|\x27+$/g, '');
    return inSet(LK_SOUNDS, k) ? LK_SOUNDS[k].split(' ') : null;
  };
  var draw = function () {
    var rule = el('lkPreset').value, text = bNorm(LK_TEXT), re = /[A-Za-z][A-Za-z']*/g, m, toks = [];
    var i, a, b, kind, n = 0, scored = 0, unknown = 0, count = 0, html = '', out = '', last = 0;
    while ((m = re.exec(text))) toks.push({ w: m[0], at: m.index, end: m.index + m[0].length });
    for (i = 0; i + 1 < toks.length; i++) {
      if (!/^ +$/.test(text.slice(toks[i].end, toks[i + 1].at))) continue;
      n++;
      a = lookup(toks[i].w);
      b = lookup(toks[i + 1].w);
      if (!a || !b) { unknown++; continue; }
      scored++;
      kind = kindOf(a[1], b[0]);
      if (kind === rule || (rule === 'same' && kind === 'same')) {
        count++;
        out += text.slice(last, toks[i].end) + '‿';
        last = toks[i + 1].at;
        html += bRow([toks[i].w + ' ' + toks[i + 1].w, say(a[1]) + ', then ' + say(b[0])]);
      }
    }
    out += text.slice(last);
    el('lkN').textContent = scored + ' of ' + n + ' scored';
    el('lkCount').textContent = String(count);
    el('lkPct').textContent = share1(count, scored);
    el('lkUnknown').textContent = String(unknown);
    el('lkLimit').textContent = 'Read from the first pronunciation the dictionary gives, which is '
      + 'American. A boundary counts only where a single space separates the words; a comma or a '
      + 'full stop is a place a speaker may stop.';
    el('lkCols').innerHTML = bHead(['the two words', 'last sound, then first sound']);
    el('lkBody').innerHTML = html;
    bSetText('lkText', out);
  };
  window.redrawLab = draw;
  el('lkPreset').addEventListener('change', draw);
  draw();
}());
"""
    keys = ["lkN", "lkCount", "lkPct", "lkUnknown"]
    return Lab(
        title="Why words run together",
        subtitle="Every place in the passage where one word meets the next with only a space between",
        markup=markup, controls=controls,
        panel_title=cfg.get("panel_title", "Mark the boundaries, then count them"),
        panel_intro=cfg.get(
            "panel_intro",
            "The passage is printed with a mark at every boundary of the kind you choose. "
            "Where a word ends in a consonant and the next begins with a vowel, a speaker "
            "says the consonant as the start of the next word."),
        script=script,
        expect={"lkPreset": {r: _sub(_LK_PINS.get(r, {}), keys) for r, _ in _LK_RULES}},
    )


# ---------------------------------------------------------------------------
# coverage -- how much of a text the 2,800 headwords cover
# ---------------------------------------------------------------------------

_CV_TEXTS = [("passage", "the 936-word passage from the novel (1813)"),
             ("wilde", "1,975 words of the play (1895)"),
             ("modern", "the two modern documents"),
             ("own", "a text of your own")]
_CV_SHOWS = [("bands", "the words not covered"), ("top", "the commonest words, ranked"),
             ("family", "the words a family adds")]
# Read off fixture pages with labcheck --observe; see the module docstring.
_CV_PINS = {'passage': {'cvN': '936',
             'cvB1': '85.0%',
             'cvB2': '89.2%',
             'cvB3': '91.0%',
             'cvNames': '94.3%',
             'cvFam': '95.6%',
             'cvOff': '41',
             'cvDistinct': '361',
             'cvTop10': '25.6%',
             'cvTop50': '54.5%',
             'cvTop100': '67.7%'},
 'wilde': {'cvN': '1972',
           'cvB1': '79.5%',
           'cvB2': '83.9%',
           'cvB3': '85.9%',
           'cvNames': '94.6%',
           'cvFam': '95.4%',
           'cvOff': '91',
           'cvDistinct': '605',
           'cvTop10': '24.9%',
           'cvTop50': '50.5%',
           'cvTop100': '63.3%'},
 'modern': {'cvN': '1685',
            'cvB1': '76.0%',
            'cvB2': '84.7%',
            'cvB3': '87.3%',
            'cvNames': '92.7%',
            'cvFam': '93.7%',
            'cvOff': '106',
            'cvDistinct': '603',
            'cvTop10': '24.7%',
            'cvTop50': '47.3%',
            'cvTop100': '60.6%'},
 'own': {'cvN': '—',
         'cvB1': '—',
         'cvB2': '—',
         'cvB3': '—',
         'cvNames': '—',
         'cvFam': '—',
         'cvOff': '—',
         'cvDistinct': '—',
         'cvTop10': '—',
         'cvTop50': '—',
         'cvTop100': '—'}}

# Plurals no rule forms (PLAN section D.1 names this list); -men compounds are
# handled by the rule below them.
_IRREGULAR_PLURALS = {"men": "man", "women": "woman", "children": "child", "feet": "foot",
                      "teeth": "tooth", "mice": "mouse", "geese": "goose", "oxen": "ox",
                      "lice": "louse", "dice": "die", "pence": "penny", "people": "person"}

# The case forms the NGSL records under its pronoun and demonstrative
# headwords (him under he, these under this): a closed list no ending forms,
# like the irregular verbs, so it is looked up and the page says so.
_PRONOUN_FORMS = {"me": "i", "my": "i", "mine": "i", "us": "we", "our": "we", "ours": "we",
                  "him": "he", "his": "he", "her": "she", "hers": "she", "its": "it",
                  "them": "they", "their": "they", "theirs": "they", "your": "you",
                  "yours": "you", "these": "this", "those": "that", "whom": "who",
                  "whose": "who", "an": "a", "cannot": "can"}

# The rules run backwards: every reduction a word is allowed, in one string so
# a harness can evaluate exactly what the page runs (see the module docstring).
B_COVER_JS = r"""
var cvHeads = {};
var cvIrr = {};
var cvLoad = function (heads, irr) {
  var b, w, i, k;
  for (b = 0; b < heads.length; b++) {
    w = heads[b].split(' ');
    for (i = 0; i < w.length; i++) if (!inSet(cvHeads, w[i])) cvHeads[w[i]] = b + 1;
  }
  for (k in irr) if (Object.prototype.hasOwnProperty.call(irr, k)) cvIrr[k] = irr[k];
};
/* Every headword a word could be a form of, by the Subject's rules undone. */
var cvCands = function (t) {
  var out = [t], n;
  if (inSet(cvIrr, t)) out.push(cvIrr[t]);
  if (/men$/.test(t)) out.push(t.slice(0, -3) + 'man');
  if (/n\x27t$/.test(t)) {
    out.push({ 'won\x27t': 'will', 'can\x27t': 'can', 'shan\x27t': 'shall' }[t] || t.slice(0, -3));
    return out;
  }
  if (/\x27(ll|re|ve|m|d)$/.test(t)) { out.push(t.replace(/\x27(ll|re|ve|m|d)$/, '')); return out; }
  n = t.length;
  if (/ies$/.test(t)) out.push(t.slice(0, -3) + 'y');
  if (/(lves|ives|eaves|olves)$/.test(t)) { out.push(t.slice(0, -3) + 'f'); out.push(t.slice(0, -3) + 'fe'); }
  if (/es$/.test(t)) out.push(t.slice(0, -2));
  if (/s$/.test(t) && !/ss$/.test(t)) out.push(t.slice(0, -1));
  if (/ied$/.test(t)) out.push(t.slice(0, -3) + 'y');
  if (/ed$/.test(t)) { out.push(t.slice(0, -2)); out.push(t.slice(0, -1)); }
  if (/([^aeiou])\1ed$/.test(t)) out.push(t.slice(0, -3));
  if (/ying$/.test(t)) out.push(t.slice(0, -4) + 'ie');
  if (/ing$/.test(t)) { out.push(t.slice(0, -3)); out.push(t.slice(0, -3) + 'e'); }
  if (/([^aeiou])\1ing$/.test(t)) out.push(t.slice(0, -4));
  if (/ier$/.test(t)) out.push(t.slice(0, -3) + 'y');
  if (/er$/.test(t)) { out.push(t.slice(0, -2)); out.push(t.slice(0, -1)); }
  if (/([^aeiou])\1er$/.test(t)) out.push(t.slice(0, -3));
  if (/iest$/.test(t)) out.push(t.slice(0, -4) + 'y');
  if (/est$/.test(t)) { out.push(t.slice(0, -3)); out.push(t.slice(0, -2)); }
  if (/([^aeiou])\1est$/.test(t)) out.push(t.slice(0, -4));
  if (/ily$/.test(t)) out.push(t.slice(0, -3) + 'y');
  if (/ically$/.test(t)) out.push(t.slice(0, -4));
  if (/lly$/.test(t)) out.push(t.slice(0, -1));
  if (/[^aeiou]ly$/.test(t) && n > 3) out.push(t.slice(0, -1) + 'e');
  if (/uly$/.test(t)) out.push(t.slice(0, -2) + 'e');
  if (/ly$/.test(t)) out.push(t.slice(0, -2));
  return out;
};
var cvHead = function (w) { return inSet(cvHeads, w) ? cvHeads[w] : 0; };
/* The lowest band of any headword the word reduces to; 0 when none. A form
   may be two rules from its headword (feelings: feeling, feel), never more. */
var cvBand = function (t, depth) {
  var c = cvCands(t), i, b = 0, h;
  for (i = 0; i < c.length; i++) {
    h = cvHead(c[i]);
    if (!h && inSet(cvIrr, c[i])) h = cvHead(cvIrr[c[i]]);
    if (!h && !depth && c[i] !== t) h = cvBand(c[i], 1);
    if (h && (!b || h < b)) b = h;
  }
  return b;
};
var CV_PRE = ['un', 're', 'dis', 'in', 'im', 'mis', 'non', 'over', 'under', 'pre'];
var CV_SUF = ['ly', 'ness', 'ment', 'tion', 'sion', 'er', 'or', 'ful', 'less', 'able', 'ible',
              'ity', 'ous', 'ive', 'al', 'ish', 'ist', 'ism', 'ance', 'ence', 'ure', 'age'];
/* One derivational affix stripped, and what is left covered: the family.
   The stem with -e is tried first, so a word whose -e fell off before the
   suffix is given back its headword (notable: note, not not). */
var cvFamily = function (t) {
  var i, s, stem, c, j;
  for (i = 0; i < CV_PRE.length; i++) {
    s = CV_PRE[i];
    if (t.length > s.length + 2 && t.slice(0, s.length) === s && cvBand(t.slice(s.length))) {
      return s + '- + ' + t.slice(s.length);
    }
  }
  for (i = 0; i < CV_SUF.length; i++) {
    s = CV_SUF[i];
    if (t.length > s.length + 2 && t.slice(-s.length) === s) {
      stem = t.slice(0, -s.length);
      c = [stem + 'e', stem];
      if (/i$/.test(stem)) c.push(stem.slice(0, -1) + 'y');
      if (/([^aeiou])\1$/.test(stem)) c.push(stem.slice(0, -1));
      for (j = 0; j < c.length; j++) if (cvBand(c[j])) return c[j] + ' + -' + s;
    }
  }
  return '';
};
"""


def _coverage_irregulars():
    irr = {}
    for v in _data("irregular_verbs.json")["verbs"]:
        for slot in ("past", "pp"):
            for form in v[slot].split("/"):
                irr.setdefault(form, v["base"])
    for form in ("am", "is", "are"):
        irr[form] = "be"
    irr["has"] = "have"
    irr.update(_IRREGULAR_PLURALS)
    irr.update({"better": "good", "best": "good", "worse": "bad", "worst": "bad"})
    irr.update(_PRONOUN_FORMS)
    return irr


def _headwords():
    bands = {1: [], 2: [], 3: []}
    seen = set()
    for line in (_REPO / "scripts" / "wordlists" / "ngsl.tsv").read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        _form, head, band = line.split("\t")
        if head not in seen:
            seen.add(head)
            bands[int(band)].append(head)
    return [" ".join(bands[b]) for b in (1, 2, 3)]


def _coverage(cfg):
    text = _pick(cfg, "text", [t for t, _ in _CV_TEXTS], "passage")
    show = _pick(cfg, "show", [s for s, _ in _CV_SHOWS], "bands")
    texts = {"passage": _data("wordorder_passage.json")["passage"],
             "wilde": _data("b_wilde_excerpt.json")["text"]}
    markup = (
        _kpis([("words read", "cvN", "&mdash;"), ("first band, 1,050 headwords", "cvB1", "&mdash;"),
               ("first two bands, 2,050", "cvB2", "&mdash;"), ("all three, 2,859", "cvB3", "&mdash;"),
               ("and names", "cvNames", "&mdash;"), ("and families", "cvFam", "&mdash;"),
               ("words not covered", "cvOff", "&mdash;"), ("different words", "cvDistinct", "&mdash;")])
        + _kpis([("the commonest ten", "cvTop10", "&mdash;"), ("fifty", "cvTop50", "&mdash;"),
                 ("a hundred", "cvTop100", "&mdash;")])
        + _limit("cv")
        + _table("cv", 20)
        + '<details><summary>The text, printed in full</summary>' + _text_block("cv") + '</details>'
    )
    controls = (
        '<label for="cvPreset">Text</label> ' + _select("cvPreset", _CV_TEXTS, text)
        + ' <label for="cvShow">List</label> ' + _select("cvShow", _CV_SHOWS, show)
        + '<div id="cvOwnBox"><label for="cvOwn">Paste a text of fifty words or more</label>'
          '<textarea id="cvOwn" rows="6" style="width:100%;"></textarea></div>'
    )
    script = (SCAN_JS + B_JS + B_COVER_JS + _lit("MODERN", MODERN_DATA)
              + _lit("CV_HEADS", _headwords()) + _lit("CV_IRR", _coverage_irregulars())
              + _lit("CV_TEXTS", texts) + r"""
(function () {
  var el = function (id) { return document.getElementById(id); };
  var TILES = ['cvN', 'cvB1', 'cvB2', 'cvB3', 'cvNames', 'cvFam', 'cvOff', 'cvDistinct',
               'cvTop10', 'cvTop50', 'cvTop100'];
  var NAMES = { passage: 'the passage from the novel, 1813', wilde: 'the play, 1895',
                modern: 'the two modern documents', own: 'your text' };
  cvLoad(CV_HEADS, CV_IRR);
  var modernText = function () {
    var s = '', k;
    for (k = 0; k < MODERN.docs.length; k++) s += MODERN.docs[k].text + '\n\n';
    return s;
  };
  /* A word starts a sentence when only spaces, quotation marks or brackets
     stand between it and a full stop, a question mark, an exclamation mark,
     a blank line or the start of the text -- and the full stop is not the one
     after Mr, Mrs, Dr or St, which ends no sentence. */
  var startsSentence = function (text, at) {
    var i = at - 1, c, lines = 0;
    while (i >= 0) {
      c = text.charAt(i);
      if (c === '\n') lines++;
      else if (!/[\s\x22“”\x27(\[_]/.test(c)) break;
      i--;
    }
    if (i < 0 || lines > 1) return true;
    if (c === '.' && /(^|[^A-Za-z])(Mr|Mrs|Ms|Dr|St)$/.test(text.slice(Math.max(0, i - 4), i))) return false;
    return /[.!?]/.test(c);
  };
  var draw = function () {
    var which = el('cvPreset').value, show = el('cvShow').value, text, re = /[A-Za-z][A-Za-z']*/g;
    var m, i, t, w, b, toks = [], n = 0, b1 = 0, b2 = 0, b3 = 0, names = 0, fam = 0;
    var off = bTally(), nameT = bTally(), famT = bTally(), rank = bTally(), html = '', f, r, cum;
    el('cvOwnBox').style.display = which === 'own' ? '' : 'none';
    text = which === 'own' ? el('cvOwn').value : which === 'modern' ? modernText()
      : (CV_TEXTS[which] || CV_TEXTS.passage);
    text = bNorm(text || '');
    /* A letter run glued to a digit (the nd of 22nd) is part of a number, not a word. */
    while ((m = re.exec(text))) if (!/[0-9]/.test(text.charAt(m.index - 1))) toks.push({ w: m[0], at: m.index });
    /* A capitalised word that also stands capitalised inside a sentence is a
       name wherever it stands, so Elizabeth at the start of a sentence is
       still a name; a capital that only ever opens a sentence is not. */
    var midCaps = {};
    for (i = 0; i < toks.length; i++) {
      if (/^[A-Z]/.test(toks[i].w) && !startsSentence(text, toks[i].at)) {
        midCaps[toks[i].w.replace(/\x27s$/, '')] = true;
      }
    }
    if (which === 'own' && toks.length < 50) {
      for (i = 0; i < TILES.length; i++) el(TILES[i]).textContent = '—';
      el('cvLimit').textContent = 'Type at least fifty words: a share of a shorter text says '
        + 'more about the text than about the list.';
      el('cvCols').innerHTML = '';
      el('cvBody').innerHTML = '';
      bSetText('cvText', '');
      return;
    }
    for (i = 0; i < toks.length; i++) {
      w = toks[i].w;
      t = w.toLowerCase().replace(/\x27s$/, '').replace(/\x27+$/, '');
      if (t.length === 1 && t !== 'a' && t !== 'i') continue;
      n++;
      rank.add(t);
      b = cvBand(t);
      if (b) {
        b3++;
        if (b <= 2) b2++;
        if (b === 1) b1++;
      } else if (/^[A-Z]{2,}$/.test(w) || inSet(midCaps, w.replace(/\x27s$/, ''))) {
        names++;
        nameT.add(w.replace(/\x27s$/, ''));
      } else if ((f = cvFamily(t))) {
        fam++;
        famT.add(t + ' (' + f + ')');
      } else {
        off.add(t);
      }
    }
    var top = rank.ranked(), sum = [0, 0, 0], k;
    for (i = 0; i < top.length && i < 100; i++) {
      k = rank.count(top[i]);
      if (i < 10) sum[0] += k;
      if (i < 50) sum[1] += k;
      sum[2] += k;
    }
    el('cvN').textContent = String(n);
    el('cvB1').textContent = share1(b1, n);
    el('cvB2').textContent = share1(b2, n);
    el('cvB3').textContent = share1(b3, n);
    el('cvNames').textContent = share1(b3 + names, n);
    el('cvFam').textContent = share1(b3 + names + fam, n);
    el('cvOff').textContent = String(n - b3 - names - fam);
    el('cvDistinct').textContent = String(top.length);
    el('cvTop10').textContent = share1(sum[0], n);
    el('cvTop50').textContent = share1(sum[1], n);
    el('cvTop100').textContent = share1(sum[2], n);
    el('cvLimit').textContent = 'Read from ' + NAMES[which] + '. A word counts when it is a headword '
      + 'or becomes one when the endings this Subject teaches are taken off; a name is a word with a '
      + 'capital letter that does not start a sentence. Spellings only: the page cannot tell which '
      + 'meaning of a word is meant.';
    if (show === 'top') {
      el('cvCols').innerHTML = bHead(['rank', 'word', 'times', 'share of the text so far']);
      cum = 0;
      for (i = 0; i < top.length && i < 100; i++) {
        cum += rank.count(top[i]);
        html += bRow([String(i + 1), top[i], String(rank.count(top[i])), share1(cum, n)]);
      }
    } else if (show === 'family') {
      el('cvCols').innerHTML = bHead(['word, and what it is made of', 'times']);
      r = famT.ranked();
      for (i = 0; i < r.length; i++) html += bRow([r[i], String(famT.count(r[i]))]);
      if (!r.length) html = bRow(['no word here needs its family', '']);
    } else {
      el('cvCols').innerHTML = bHead(['word', 'times', 'what it is']);
      r = off.ranked();
      for (i = 0; i < r.length; i++) html += bRow([r[i], String(off.count(r[i])), 'not covered']);
      r = nameT.ranked();
      for (i = 0; i < r.length; i++) html += bRow([r[i], String(nameT.count(r[i])), 'a name']);
    }
    el('cvBody').innerHTML = html;
    bSetText('cvText', which === 'own' ? '' : text);
  };
  window.redrawLab = draw;
  el('cvPreset').addEventListener('change', draw);
  el('cvShow').addEventListener('change', draw);
  el('cvOwn').addEventListener('input', draw);
  draw();
}());
""")
    keys = ["cvN", "cvB1", "cvB2", "cvB3", "cvNames", "cvFam", "cvOff", "cvDistinct",
            "cvTop10", "cvTop50", "cvTop100"]
    return Lab(
        title="How much of a page the 2,800 words cover",
        subtitle="Every word of the text checked against the list, by the rules of the nine courses before",
        markup=markup, controls=controls,
        panel_title=cfg.get("panel_title", "Choose a text, or paste your own"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every word is checked against the 2,800 headwords. A form such as walked or "
            "happier counts when the rules this Subject teaches turn it back into a headword. "
            "The words not covered are listed: they are the ones to learn next."),
        script=script,
        expect={"cvPreset": {t: _sub(_CV_PINS.get(t, {}), keys) for t, _ in _CV_TEXTS}},
    )


MODES = {"compare": _compare, "phrasal": _phrasal, "letters": _letters, "stress": _stress,
         "contractions": _contractions, "linking": _linking, "coverage": _coverage}
