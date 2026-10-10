"""The English Subject's kit: one rule per mode, each scored on printed text.

WHAT THIS KIT PROVES. Nothing here is a table of answers. Every cell the reader
sees is produced in their browser by the rules the lesson states, applied to the
verb they typed, and `vbRuleTrace` names the rule that fired. A learner who is
handed a filled table learns twelve strings; a learner who watches the rules
fill it learns five rules and can fill the thirteenth themselves.

WHAT IT MEASURES, and why the residue is printed rather than counted away. The
forming rules are scored on the page against the recorded forms of the verb
list the page carries (`table` mode's second menu), and the figures are pinned
in that menu's presets. The words they miss are the lesson -- bus, format,
panic -- because a rule without its exceptions is the thing textbooks give.

THE LIST IS CLEANED, AND SAYS HOW. The NGSL's lemma lists were generated, and
scored raw they counted invented forms (comed, offerring) as right answers.
scripts/wordlists/clean_verbs.py removes them by one stated test and records
every row it drops; the page prints those rows with their reasons.

THE REFUTED RULE. The scoring menu runs the -s rule against the variant that
adds f -> ves, which sounds right and scores WORSE (brief, golf, proof and roof
are verbs that take -s). The reader sees the comparison, not a claim about it.

MARKUP. Tiles are `.kpi` with a `<span>` label and a `<strong>` value, as in
every other kit; theme.py styles exactly that pair.
"""

import json
import pathlib

from .common import Lab, cfg_literal
from .english_core import (AN_JS, AUX_JS, ENDINGS_JS, ENGLISH_VERB_JS, QUESTION_JS, SCAN_JS,
                           SUPER_JS, TIME_JS, WORDRULE_JS)

MODES = ("table", "doubling", "svo", "adverbs", "questions",
         "irregular", "classes", "irrshare", "listening",
         "endings", "wordrule", "an", "the_super", "auxchain", "time_preps")

_REPO = pathlib.Path(__file__).resolve().parents[3]


def _data(name):
    """Read a printed dataset from content/english/data/.

    The data lives beside the content it belongs to rather than inside this
    module: it is the text the page prints, not code, and a reviewer should be
    able to read it without opening a lab kit.
    """
    return json.loads((_REPO / "content" / "english" / "data" / name).read_text())


def _wordlist(name):
    """Read a cleaned word list from scripts/wordlists/ (clean_verbs.py writes them)."""
    return json.loads((_REPO / "scripts" / "wordlists" / name).read_text())


def _kpis(items):
    """[(label, element id, starting text)] -> the kpi grid every kit uses."""
    return ('<div class="kpi-grid">'
            + "".join('<div class="kpi"><span>%s</span><strong id="%s">%s</strong></div>'
                      % (label, kid, start) for label, kid, start in items)
            + '</div>')


def _options(select_id, presets):
    return ('<select id="%s">' % select_id
            + "".join('<option value="%s">%s</option>' % (p["id"], p["label"])
                      for p in presets)
            + "</select>")


def _menu(select_id, items, chosen=None):
    """A <select> of (value, label) pairs with `chosen` marked selected: the
    value a lesson ships with. labcheck reads the selected option as the
    control's starting value."""
    return ('<select id="%s">' % select_id
            + "".join('<option value="%s"%s>%s</option>'
                      % (v, ' selected' if v == chosen else '', label) for v, label in items)
            + "</select>")


def _expect(presets):
    return {p["id"]: p["expect"] for p in presets}


# ---------------------------------------------------------------------------
# table -- type a verb, watch the rules fill the twelve cells; then score the
# rules on the whole printed list
# ---------------------------------------------------------------------------

_TABLE_PRESETS = [
    {"id": "walk", "label": "walk — nothing special happens",
     "verb": "walk",
     "expect": {"tbThird": "walks", "tbIng": "walking", "tbEd": "walked",
                "tbRule": "nothing special: just add the ending"}},
    {"id": "stop", "label": "stop — the last letter doubles",
     "verb": "stop",
     "expect": {"tbThird": "stops", "tbIng": "stopping", "tbEd": "stopped",
                "tbRule": "ends consonant-vowel-consonant, stressed: double it"}},
    {"id": "carry", "label": "carry — -y becomes -ies",
     "verb": "carry",
     "expect": {"tbThird": "carries", "tbIng": "carrying", "tbEd": "carried",
                "tbRule": "consonant then -y: -y becomes -ies"}},
    {"id": "hope", "label": "hope — the silent -e goes",
     "verb": "hope",
     "expect": {"tbThird": "hopes", "tbIng": "hoping", "tbEd": "hoped",
                "tbRule": "silent -e: drop it before -ing"}},
    {"id": "listen", "label": "listen — CVC, but the stress is early, so no doubling",
     "verb": "listen",
     "expect": {"tbThird": "listens", "tbIng": "listening", "tbEd": "listened",
                "tbRule": "nothing special: just add the ending"}},
    {"id": "go", "label": "go — irregular: looked up, not formed",
     "verb": "go",
     "expect": {"tbThird": "goes", "tbIng": "going", "tbEd": "went",
                "tbRule": "irregular: looked up, not formed"}},
]

# Scored on the printed list. Figures were read off the built page with
# `labcheck.js --observe` and agree with scripts/wordlists/verbrules_check.js.
_SCORE_PRESETS = [
    {"id": "s", "label": "the -s rule (he / she / it)",
     "expect": {"tbsHit": "1209 of 1210", "tbsPct": "99.92%", "tbsMiss": "1",
                "tbsFirst": "stomach"}},
    {"id": "oes", "label": "the -s rule before the -o fix (every -o takes -es)",
     "expect": {"tbsHit": "1207 of 1210", "tbsPct": "99.75%", "tbsMiss": "3",
                "tbsFirst": "radio, stomach, video"}},
    {"id": "ves", "label": "the -s rule with f becoming -ves added",
     "expect": {"tbsHit": "1205 of 1210", "tbsPct": "99.59%", "tbsMiss": "5",
                "tbsFirst": "brief, golf, proof, roof, stomach"}},
    {"id": "ing", "label": "the -ing rule",
     "expect": {"tbsHit": "1202 of 1210", "tbsPct": "99.34%", "tbsMiss": "8",
                "tbsFirst": "bus, format, initial, input, output, panic, traffic, up"}},
    {"id": "ed", "label": "the past (-ed) rule",
     "expect": {"tbsHit": "1201 of 1210", "tbsPct": "99.26%", "tbsMiss": "9",
                "tbsFirst": "bus, counsel, format, initial, input, output, panic, traffic, up"}},
]


def _verb_list_text(verbs):
    """The cleaned list as the one string `vbDecodeList` reads.

    Rows split by '|', fields by ' ', spellings by '/', and a leading '~'
    standing for the base: 'stop L ~s ~ping ~ped'. The stress mark is a letter,
    L when the last part is stressed and F otherwise, not a digit: 'course 1'
    in the page's text reads to the copy guards as a numbered course. The
    encoding only shortens the text; every recorded spelling is on the page.
    """
    slots = {slot: dict(verbs["cases"][slot]) for slot in ("s", "ing", "ed")}

    def rel(base, form):
        return "~" + form[len(base):] if form.startswith(base) else form

    rows = []
    for base, last in verbs["stress"].items():
        rows.append(" ".join(
            [base, "L" if last else "F"]
            + ["/".join(rel(base, f) for f in slots[slot][base]) for slot in ("s", "ing", "ed")]))
    return "|".join(rows)


def _table(cfg):
    verbs = _wordlist("verbrules_cases.json")
    focus = cfg.get("focus", "build")
    if focus not in ("build", "score"):
        raise ValueError("english_lab table: focus is build or score, not %r" % focus)
    build = (
        _kpis([("he / she / it", "tbThird", "walks"), ("-ing form", "tbIng", "walking"),
               ("past form", "tbEd", "walked"), ("rule that fired", "tbRule", "nothing special")])
        + '<div class="table-wrap"><table id="tbGrid"><thead><tr>'
        '<th>time</th><th>simple</th><th>progressive</th>'
        '<th>perfect</th><th>perfect progressive</th>'
        '</tr></thead><tbody id="tbBody"></tbody></table></div>'
    )
    scoring = (
        '<p class="small-copy" id="tbsHead">The rules scored on every regular verb in the '
        'printed list below.</p>'
        + _kpis([("rule", "tbsRule", "&mdash;"), ("right", "tbsHit", "&mdash;"),
                 ("share right", "tbsPct", "&mdash;"), ("missed", "tbsMiss", "&mdash;"),
                 ("the words it missed", "tbsFirst", "&mdash;")])
        + '<div class="table-wrap" style="max-height:18rem;overflow-y:auto;">'
        '<table id="tbsTable"><thead><tr id="tbsCols"></tr></thead>'
        '<tbody id="tbsBody"></tbody></table></div>'
    )
    # focus: score puts the scoring half above the twelve cells; nothing else
    # changes, so the two lessons that share this lab pin the same figures.
    markup = scoring + build if focus == "score" else build + scoring
    show = cfg.get("show", "residue")
    controls = (
        '<label for="tbVerb">A verb</label> '
        '<input id="tbVerb" type="text" value="walk" size="14" /> '
        '<label for="tbPreset">or one that shows a rule</label> '
        + _options("tbPreset", _TABLE_PRESETS)
        + ' <label for="tbScore">Score a rule on the list</label> '
        + _options("tbScore", _SCORE_PRESETS)
        + ' <label for="tbShow">List</label> '
        + _menu("tbShow", [("residue", "the words the rule misses"),
                           ("all", "every verb in the list"),
                           ("excluded", "the words left out of the list, and why")], show)
    )
    script = (
        ENGLISH_VERB_JS
        + cfg_literal("TB_PRESETS", _TABLE_PRESETS)
        + cfg_literal("VB_LIST_TEXT", _verb_list_text(verbs))
        + cfg_literal("VB_EXCLUDED", verbs["excluded"])
        + r"""
(function () {
  var el = function (id) { return document.getElementById(id); };
  /* The irregular verbs the page knows, printed in the lesson beside the lab. */
  VB_IRREG = {
    go:   { third: 'goes',  ing: 'going',  past: 'went',  pp: 'gone' },
    be:   { third: 'is',    ing: 'being',  past: 'was',   pp: 'been' },
    have: { third: 'has',   ing: 'having', past: 'had',   pp: 'had' },
    make: { third: 'makes', ing: 'making', past: 'made',  pp: 'made' },
    take: { third: 'takes', ing: 'taking', past: 'took',  pp: 'taken' },
    see:  { third: 'sees',  ing: 'seeing', past: 'saw',   pp: 'seen' }
  };
  VB_FINAL_STRESS = { listen: false, open: false, happen: false, offer: false,
                      visit: false, enter: false, answer: false, travel: false };
  /* The printed list carries a stress mark for every verb in it, so a verb
     typed from the list doubles (or not) by its own stress, not by a guess. */
  var VB_ROWS = vbDecodeList(VB_LIST_TEXT), r;
  for (r = 0; r < VB_ROWS.length; r++) VB_FINAL_STRESS[VB_ROWS[r].base] = VB_ROWS[r].last;

  var draw = function (typed) {
    var verb = (typed || '').replace(/^\s+|\s+$/g, '').toLowerCase();
    /* Refused, visibly: a rule for words cannot be run on a number or on two
       words, and silently cleaning the input would show a verb nobody typed. */
    if (!/^[a-z]+$/.test(verb)) {
      el('tbThird').textContent = '—';
      el('tbIng').textContent = '—';
      el('tbEd').textContent = '—';
      el('tbRule').textContent = verb
        ? 'not one word: type a single verb in letters, such as walk'
        : 'type a verb, such as walk';
      el('tbBody').innerHTML = '';
      return;
    }
    el('tbThird').textContent = vbThird(verb);
    el('tbIng').textContent = vbIng(verb);
    el('tbEd').textContent = vbEd(verb);
    el('tbRule').textContent = vbRuleTrace(verb);
    var cells = vbTable(verb, true), rows = {}, i, t;
    for (i = 0; i < cells.length; i++) {
      (rows[cells[i].time] = rows[cells[i].time] || {})[cells[i].aspect] = cells[i].form;
    }
    var html = '', times = ['present', 'past', 'future'],
        asp = ['simple', 'progressive', 'perfect', 'perfect progressive'];
    for (i = 0; i < times.length; i++) {
      html += '<tr><th scope=row>' + times[i] + '</th>';
      for (t = 0; t < asp.length; t++) {
        html += '<td>' + (rows[times[i]][asp[t]] || '') + '</td>';
      }
      html += '</tr>';
    }
    el('tbBody').innerHTML = html;
  };

  /* The scoring view. Each rule is run on every verb in the printed list and
     counted right when its form is a spelling the list records. */
  var RULES = {
    s:   ['s', vbThird, '-s, -es, -ies'],
    oes: ['s', vbThirdBeforeFix, '-s, with -es after every -o'],
    ves: ['s', vbThirdWithVes, '-s, with f becoming -ves'],
    ing: ['ing', vbIng, '-ing'],
    ed:  ['ed', vbEd, '-ed']
  };
  var scoreId = 's', show = el('tbShow').value;
  var score = function () {
    var rule = RULES[scoreId] || RULES.s, res = vbScoreSlot(VB_ROWS, rule[0], rule[1]);
    var names = [], i, html = '', said, row;
    for (i = 0; i < res.miss.length; i++) names.push(res.miss[i].base);
    el('tbsRule').textContent = rule[2];
    el('tbsHit').textContent = res.hit + ' of ' + res.total;
    el('tbsPct').textContent = vbPct2(res.hit, res.total);
    el('tbsMiss').textContent = String(res.miss.length);
    el('tbsFirst').textContent = names.length ? names.join(', ') : 'none';
    if (show === 'excluded') {
      el('tbsCols').innerHTML = '<th>word</th><th>why it is not scored</th>';
      var keys = Object.keys(VB_EXCLUDED);
      for (i = 0; i < keys.length; i++) {
        html += '<tr><td>' + keys[i] + '</td><td>' + VB_EXCLUDED[keys[i]] + '</td></tr>';
      }
    } else {
      el('tbsCols').innerHTML = '<th>verb</th><th>the rule says</th>'
        + '<th>the list records</th><th></th>';
      var list = show === 'all' ? VB_ROWS : res.miss;
      for (i = 0; i < list.length; i++) {
        row = list[i];
        said = show === 'all' ? rule[1](row.base) : row.said;
        var recorded = show === 'all' ? row[rule[0]] : row.list;
        html += '<tr><td>' + row.base + '</td><td>' + said + '</td><td>'
              + recorded.join(' / ') + '</td><td>'
              + (recorded.indexOf(said) >= 0 ? '' : 'missed') + '</td></tr>';
      }
    }
    el('tbsBody').innerHTML = html;
  };

  /* labcheck calls this after setting a control, and refuses the page without
     it: a lab whose figures cannot be re-driven from outside cannot be pinned. */
  window.redrawLab = function () { draw(el('tbVerb').value); score(); };

  el('tbVerb').addEventListener('input', function () { draw(this.value); });
  el('tbPreset').addEventListener('change', function () {
    var i;
    for (i = 0; i < TB_PRESETS.length; i++) {
      if (TB_PRESETS[i].id === this.value) {
        el('tbVerb').value = TB_PRESETS[i].verb;
        draw(TB_PRESETS[i].verb);
        return;
      }
    }
  });
  el('tbScore').addEventListener('change', function () { scoreId = this.value; score(); });
  el('tbShow').addEventListener('change', function () { show = this.value; score(); });
  draw(el('tbVerb').value);
  score();
}());
"""
    )
    return Lab(
        title="Twelve cells, five rules, and the verb you typed",
        subtitle="Every cell is formed on the page by the rule named beside it",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type any verb and watch the table fill"),
        panel_intro=cfg.get(
            "panel_intro",
            "Nothing here is looked up except the verbs marked irregular. The "
            "three forms at the top are made by the rules this lesson states, "
            "and the box beside them names the rule that fired, so you can "
            "check the answer against the reason for it.",
        ),
        script=script,
        expect={"tbPreset": _expect(_TABLE_PRESETS), "tbScore": _expect(_SCORE_PRESETS)},
    )


# ---------------------------------------------------------------------------
# doubling -- the rule that needs the sound, and what it costs without it
# ---------------------------------------------------------------------------

# Every verb of the NGSL that ENDS consonant-vowel-consonant, the only verbs
# the doubling rule can touch, built by scripts/wordlists/clean_verbs.py. Each
# row: base, 1 if the stress falls on the last part, 1 if the list records a
# doubled -ing spelling, every recorded -ing spelling, and the recorded
# spellings removed as misspellings. The raw NGSL carried offerring and
# sufferring (and offerred), which made offer and suffer look like exceptions
# to a rule they obey, and gave council -- not a verb -- a councilling. Rows
# with no correct -ing spelling, or that are not verbs, are left out; the page
# prints them and why. Printed in full, because a hit rate the reader cannot
# recount is a hit rate they have to take on trust.
DOUBLING = _wordlist("doubling_verbs.json")

_DB_PRESETS = [
    {"id": "stress", "label": "double when the last part is the strong part",
     "rule": "stress",
     "expect": {"dbScore": "199 of 217", "dbPct": "91.7%", "dbWrong": "18"}},
    {"id": "always", "label": "double every one of them",
     "rule": "always",
     "expect": {"dbScore": "107 of 217", "dbPct": "49.3%", "dbWrong": "110"}},
    {"id": "never", "label": "never double",
     "rule": "never",
     "expect": {"dbScore": "110 of 217", "dbPct": "50.7%", "dbWrong": "107"}},
]


def _doubling(cfg):
    markup = (
        _kpis([("right", "dbScore", "&mdash;"), ("share", "dbPct", "&mdash;"),
               ("wrong", "dbWrong", "&mdash;"), ("of those, ending in -l", "dbEl", "&mdash;")])
        + '<div class="table-wrap" style="max-height:24rem;overflow-y:auto;">'
        '<table id="dbTable"><thead><tr id="dbCols"></tr></thead>'
        '<tbody id="dbBody"></tbody></table></div>'
    )
    controls = (
        '<label for="dbPreset">The rule to score</label> '
        + _options("dbPreset", _DB_PRESETS)
        + ' <label for="dbShow">Show</label> '
        '<select id="dbShow">'
        '<option value="wrong">only the ones it gets wrong</option>'
        '<option value="all">every verb</option>'
        '<option value="excluded">the words left out, and why</option>'
        '</select>'
    )
    script = (
        cfg_literal("DB_VERBS", DOUBLING["verbs"])
        + cfg_literal("DB_EXCLUDED", DOUBLING["excluded"])
        + cfg_literal("DB_PRESETS", _DB_PRESETS)
        + r"""
(function () {
  var el = function (id) { return document.getElementById(id); };
  var rule = 'stress', show = 'wrong';

  var predicts = function (row) {
    if (rule === 'always') return 1;
    if (rule === 'never') return 0;
    return row[1];                       /* the stress flag */
  };

  var draw = function () {
    var right = 0, wrong = [], i, row;
    for (i = 0; i < DB_VERBS.length; i++) {
      row = DB_VERBS[i];
      if (predicts(row) === row[2]) right++; else wrong.push(row);
    }
    var n = DB_VERBS.length;
    el('dbScore').textContent = right + ' of ' + n;
    /* One decimal place, worked in whole numbers so the printed figure is
       exactly what the division gives and not a floating-point artefact. */
    var tenths = Math.round(right * 1000 / n);
    el('dbPct').textContent = Math.floor(tenths / 10) + '.' + (tenths % 10) + '%';
    el('dbWrong').textContent = String(wrong.length);
    var el_count = 0;
    for (i = 0; i < wrong.length; i++) if (/l$/.test(wrong[i][0])) el_count++;
    el('dbEl').textContent = String(el_count);

    var html = '';
    if (show === 'excluded') {
      el('dbCols').innerHTML = '<th>word</th><th>why it is left out</th>';
      var keys = Object.keys(DB_EXCLUDED);
      for (i = 0; i < keys.length; i++) {
        html += '<tr><td>' + keys[i] + '</td><td>' + DB_EXCLUDED[keys[i]] + '</td></tr>';
      }
    } else {
      el('dbCols').innerHTML = '<th>verb</th><th>strong part last?</th><th>rule says</th>'
        + '<th>word list says</th><th></th>';
      var rowsToShow = show === 'all' ? DB_VERBS : wrong;
      for (i = 0; i < rowsToShow.length; i++) {
        row = rowsToShow[i];
        var says = predicts(row) ? row[0] + row[0].charAt(row[0].length - 1) + 'ing'
                                 : row[0] + 'ing';
        html += '<tr><td>' + row[0] + '</td><td>' + (row[1] ? 'yes' : 'no')
              + '</td><td>' + says + '</td><td>' + row[3].split('/').join(' / ')
              + (row[4] ? ' (the raw list also has ' + row[4].split('/').join(', ')
                          + ', a misspelling, removed)' : '')
              + '</td><td>' + (predicts(row) === row[2] ? '' : 'wrong') + '</td></tr>';
      }
    }
    el('dbBody').innerHTML = html;
  };

  window.redrawLab = draw;
  el('dbPreset').addEventListener('change', function () { rule = this.value; draw(); });
  el('dbShow').addEventListener('change', function () { show = this.value; draw(); });
  draw();
}());
"""
    )
    return Lab(
        title="The doubling rule, scored three ways on the same verbs",
        subtitle="Switch the stress condition off and watch the rule fall to a coin toss",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Score the rule yourself"),
        panel_intro=cfg.get(
            "panel_intro",
            "These are every verb in the word list that ends consonant, vowel, "
            "consonant -- the only verbs the doubling rule can touch. The table "
            "is scored in your browser against the forms the word list records, "
            "and you can read every row.",
        ),
        script=script,
        expect={"dbPreset": _expect(_DB_PRESETS)},
    )


# ---------------------------------------------------------------------------
# The word-order modes. One scanner, three rules, three printed datasets.
#
# Every figure these labs show is computed in the browser over text printed on
# the same page, scored against a lexicon printed with it. A dataset is never
# scored against another page's word list -- an early version scored a
# whole-novel concordance against a 141-word passage lexicon and reported 45%
# of its rows as "outside the lexicon", which measured the lexicon, not English.
# ---------------------------------------------------------------------------

WORDORDER_DATA = _data("wordorder_passage.json")
ADVERB_DATA = _data("adverb_concordance.json")
QUESTION_DATA = _data("question_concordance.json")


def _modern_text(name):
    """The article text of a modern document, without its provenance header."""
    raw = (_REPO / "content" / "english" / "data" / name).read_text(encoding="utf-8")
    return raw.split("\n---\n", 1)[1].strip()


# The two modern public-domain documents the word-order lessons compare with
# Austen. Printed on the page with their citations, and counted there: the
# provenance of each (and why it is public domain) is in the data file header.
MODERN_DATA = {
    "docs": [
        {"name": "Stanley v. City of Sanford, Florida, 606 U.S. 46 (2025), opinion "
                 "of the Court, Parts I and II.A (excerpt)",
         "text": _modern_text("scotus_stanley.txt")},
        {"name": "\u201cU.S. Population Aging as Nation Turns 250\u201d, Luke T. Rogers "
                 "and George M. Hayward, U.S. Census Bureau, April 9, 2026",
         "text": _modern_text("census_aging.txt")},
    ],
}

# What prints the modern documents under a lab: a closed <details>, so the
# figures beside it can be checked word by word without the text taking the
# page over.
_MODERN_MARKUP = (
    '<details><summary>The two modern documents, printed in full</summary>'
    '<div class="mathblock" id="%sModern" style="font-size:0.8rem;"></div></details>'
)

MODERN_JS = r"""
/* The two modern documents as one list of words, and the printed text. */
var modernWords = function () {
  var all = [], i;
  for (i = 0; i < MODERN.docs.length; i++) all = all.concat(wordsOf(MODERN.docs[i].text));
  return all;
};
var modernPrint = function (id) {
  var node = document.getElementById(id), i, out = [];
  if (!node) return;
  for (i = 0; i < MODERN.docs.length; i++) {
    out.push(MODERN.docs[i].name + '\n\n' + MODERN.docs[i].text);
  }
  node.style.whiteSpace = 'pre-wrap';
  node.textContent = out.join('\n\n\n');
};
/* Occurrences per thousand words, to one decimal, in whole numbers. */
var perThousand = function (hits, words) {
  if (!words) return '0.0';
  var t = Math.round(hits * 10000 / words);
  return Math.floor(t / 10) + '.' + (t % 10);
};
"""

# SCAN_JS (wordsOf, tokensOf, lower, setOf, share1, commas) lives in english_core.py
# with every other rule function, and is imported above.


_SVO_PRESETS = [
    {"id": "subject", "label": "subject pronouns: I, he, she, we, they",
     "kind": "subject",
     # Verified against an independent count, not copied from what the page
     # printed: 72 of 80 hold, one is the quotation-tag inversion, five have a
     # modifier between. Pinning whatever the lab says would make this vacuous.
     "expect": {"soHit": "72 of 80", "soPct": "90.0%", "soBroken": "1", "soTimes": "6.1"}},
    {"id": "object", "label": "object pronouns: me, him, us, them",
     "kind": "object",
     "expect": {"soHit": "15 of 17", "soPct": "88.2%", "soBroken": "0", "soTimes": "10.4"}},
]


def _svo(cfg):
    markup = (
        _kpis([("rule holds", "soHit", "&mdash;"), ("share", "soPct", "&mdash;"),
               ("word order broken", "soBroken", "&mdash;"),
               ("a modifier comes between", "soMod", "&mdash;")])
        + _kpis([("per 1,000 words, the passage", "soHereK", "&mdash;"),
                 ("per 1,000 words, the modern documents", "soModK", "&mdash;"),
                 ("the passage has, times as many", "soTimes", "&mdash;")])
        + '<div class="table-wrap"><table id="soTable"><thead><tr>'
        '<th>pronoun</th><th>next word</th><th>what the rule says</th>'
        '</tr></thead><tbody id="soBody"></tbody></table></div>'
        '<div class="mathblock" id="soPassage" style="font-size:0.8rem;"></div>'
        + _MODERN_MARKUP % "so"
    )
    controls = (
        '<label for="soPreset">Which pronouns</label> '
        '<select id="soPreset">'
        + "".join('<option value="%s">%s</option>' % (p["id"], p["label"])
                  for p in _SVO_PRESETS)
        + '</select> '
        '<label for="soShow">Show</label> '
        '<select id="soShow">'
        '<option value="residue">only the ones the rule does not cover</option>'
        '<option value="all">every one</option>'
        '</select>'
    )
    script = (SCAN_JS + cfg_literal("SO_DATA", WORDORDER_DATA) + cfg_literal("MODERN", MODERN_DATA)
              + MODERN_JS + cfg_literal("SO_PRESETS", _SVO_PRESETS)) + r"""
(function () {
  var el = function (id) { return document.getElementById(id); };
  var verbs = setOf(SO_DATA.verbs), aux = setOf(SO_DATA.aux);
  var SUBJ = setOf(['i', 'he', 'she', 'we', 'they']);
  var OBJ = setOf(['me', 'him', 'us', 'them']);
  var PREP = setOf(['of','to','in','for','on','with','at','by','from','about','into','over',
                    'after','under','between','through','against','before','without','upon']);
  var MOD = setOf(['all','both','who','that','first','as','when','also','which','never',
                   'always','only','then','still','soon','too','indeed','certainly','really',
                   'quite','almost','hardly','scarcely']);
  var REPORT = setOf(['said','cried','replied','returned','added','observed','asked',
                      'answered','exclaimed','thought','repeated','rejoined']);
  var kind = 'subject', show = 'residue';

  var scan = function () {
    var w = wordsOf(SO_DATA.passage), lw = lower(w), rows = [], i;
    var hit = 0, broken = 0, mod = 0;
    for (i = 0; i < lw.length; i++) {
      var isTarget = kind === 'subject' ? inSet(SUBJ, lw[i]) : inSet(OBJ, lw[i]);
      if (!isTarget) continue;
      var verdict, nxt = i + 1 < lw.length ? lw[i + 1] : '';
      var prev = i ? lw[i - 1] : '';
      if (kind === 'subject') {
        if (inSet(verbs, nxt) || inSet(aux, nxt)) { verdict = 'holds'; hit++; }
        else if (inSet(REPORT, prev)) { verdict = 'inverted, a quotation tag'; broken++; }
        else if (inSet(MOD, nxt)) { verdict = 'a modifier comes between'; mod++; }
        else verdict = 'next word not in the printed list';
      } else {
        if (inSet(verbs, prev) || inSet(aux, prev) || inSet(PREP, prev)) { verdict = 'holds'; hit++; }
        else if (inSet(MOD, prev)) { verdict = 'a modifier comes between'; mod++; }
        else verdict = 'word before it not in the printed list';
      }
      rows.push([w[i], kind === 'subject' ? (nxt || '—') : (prev || '—'), verdict]);
    }
    el('soHit').textContent = hit + ' of ' + rows.length;
    el('soPct').textContent = share1(hit, rows.length);
    el('soBroken').textContent = String(broken);
    el('soMod').textContent = String(mod);
    var html = '', shown = 0;
    for (i = 0; i < rows.length; i++) {
      if (show === 'residue' && rows[i][2] === 'holds') continue;
      if (shown++ > 120) break;
      html += '<tr><td>' + rows[i][0] + '</td><td>' + rows[i][1]
            + '</td><td>' + rows[i][2] + '</td></tr>';
    }
    el('soBody').innerHTML = html;
    el('soPassage').textContent = SO_DATA.passage;

    /* The same pronouns, counted per thousand words in the passage and in the
       two modern documents printed below it. */
    var target = kind === 'subject' ? SUBJ : OBJ, mw = lower(modernWords()), here = 0, there = 0;
    for (i = 0; i < lw.length; i++) if (inSet(target, lw[i])) here++;
    for (i = 0; i < mw.length; i++) if (inSet(target, mw[i])) there++;
    el('soHereK').textContent = perThousand(here, lw.length) + ' (' + here + ' in ' + commas(lw.length) + ')';
    el('soModK').textContent = perThousand(there, mw.length) + ' (' + there + ' in ' + commas(mw.length) + ')';
    if (!there) el('soTimes').textContent = 'the modern documents have none';
    else {
      var t = Math.round(here * mw.length * 10 / (lw.length * there));
      el('soTimes').textContent = Math.floor(t / 10) + '.' + (t % 10);
    }
  };
  modernPrint('soModern');
  window.redrawLab = scan;
  el('soPreset').addEventListener('change', function () { kind = this.value === 'object' ? 'object' : 'subject'; scan(); });
  el('soShow').addEventListener('change', function () { show = this.value; scan(); });
  scan();
}());
"""
    return Lab(
        title="The rule scored on a page you can read",
        subtitle="Every pronoun in the passage below, and the word that follows it",
        markup=markup, controls=controls,
        panel_title=cfg.get("panel_title", "Score the rule on printed text"),
        panel_intro=cfg.get("panel_intro",
            "The passage is printed under the table and the list of verb forms it "
            "contains is printed with it. The scan runs in your browser over that "
            "text, so you can check any row by eye."),
        script=script,
        expect={"soPreset": _expect(_SVO_PRESETS)},
    )


_ADV_PRESETS = [
    {"id": "mid", "label": "the adverb sits in the middle",
     "expect": {"avHit": "85 of 120", "avPct": "70.8%", "avModN": "2 in 1,723 words"}},
]


# The menu offers only adverbs the concordance has lines for: an adverb with
# none (rarely) would score 0 of 0, a tile that says nothing. The modern-text
# count still searches the whole list, rarely included.
_ADV_MENU = [a for a in ADVERB_DATA["adverbs"]
             if any(row[0] == a for row in ADVERB_DATA["rows"])]


def _adverbs(cfg):
    markup = (
        _kpis([("rule holds", "avHit", "&mdash;"), ("share", "avPct", "&mdash;"),
               ("a preposition follows", "avPrep", "&mdash;"),
               ("something else between", "avOther", "&mdash;")])
        + _kpis([("in the modern documents", "avModN", "&mdash;"),
                 ("per 1,000 words there", "avModK", "&mdash;")])
        + '<div class="table-wrap"><table id="avTable"><thead><tr>'
        '<th>adverb</th><th>the line it came from</th><th>verdict</th>'
        '</tr></thead><tbody id="avBody"></tbody></table></div>'
        + _MODERN_MARKUP % "av"
    )
    controls = (
        '<label for="avWord">Which adverb</label> '
        '<select id="avWord"><option value="">all of them</option>'
        + "".join('<option value="%s">%s</option>' % (a, a) for a in _ADV_MENU)
        + '</select> '
        '<label for="avPreset">Rule</label> '
        '<select id="avPreset">'
        + "".join('<option value="%s">%s</option>' % (p["id"], p["label"]) for p in _ADV_PRESETS)
        + '</select>'
    )
    script = (SCAN_JS + cfg_literal("AV_DATA", ADVERB_DATA) + cfg_literal("MODERN", MODERN_DATA)
              + MODERN_JS + cfg_literal("AV_PRESETS", _ADV_PRESETS)) + r"""
(function () {
  var el = function (id) { return document.getElementById(id); };
  var verbs = setOf(AV_DATA.verbs), aux = setOf(AV_DATA.aux);
  var BE = setOf(['is', 'are', 'was', 'were', 'am', 'be', 'been']);
  var PREP = setOf(['in', 'at', 'on', 'of', 'to', 'for', 'with']);
  var only = '';

  var scan = function () {
    var hit = 0, prep = 0, other = 0, rows = [], i;
    for (i = 0; i < AV_DATA.rows.length; i++) {
      var adv = AV_DATA.rows[i][0], ctx = AV_DATA.rows[i][1];
      if (only && adv !== only) continue;
      var lw = lower(wordsOf(ctx)), at = lw.indexOf(adv), verdict;
      var prev = at > 0 ? lw[at - 1] : '', nxt = at >= 0 && at + 1 < lw.length ? lw[at + 1] : '';
      if (at < 0) verdict = 'not found';
      else if (inSet(aux, prev) || inSet(BE, prev) || inSet(verbs, nxt) || inSet(aux, nxt)) {
        verdict = 'in the middle'; hit++;
      } else if (inSet(PREP, nxt)) { verdict = 'a preposition follows'; prep++; }
      else { verdict = 'something else between'; other++; }
      rows.push([adv, ctx, verdict]);
    }
    el('avHit').textContent = hit + ' of ' + rows.length;
    el('avPct').textContent = share1(hit, rows.length);
    el('avPrep').textContent = String(prep);
    el('avOther').textContent = String(other);
    var html = '';
    for (i = 0; i < rows.length && i < 130; i++) {
      html += '<tr><td>' + rows[i][0] + '</td><td>' + rows[i][1]
            + '</td><td>' + rows[i][2] + '</td></tr>';
    }
    el('avBody').innerHTML = html;

    /* The same adverbs (or the one chosen), counted in the modern documents. */
    var mw = lower(modernWords()), want = only ? setOf([only]) : setOf(AV_DATA.adverbs), m = 0;
    for (i = 0; i < mw.length; i++) if (inSet(want, mw[i])) m++;
    el('avModN').textContent = m + ' in ' + commas(mw.length) + ' words';
    el('avModK').textContent = perThousand(m, mw.length);
  };
  modernPrint('avModern');
  window.redrawLab = scan;
  el('avWord').addEventListener('change', function () { only = this.value; scan(); });
  el('avPreset').addEventListener('change', function () { scan(); });
  scan();
}());
"""
    return Lab(
        title="One hundred and twenty lines, and where the adverb sits in each",
        subtitle="Every line the figure is computed from is printed in the table",
        markup=markup, controls=controls,
        panel_title=cfg.get("panel_title", "Where the adverb goes, counted"),
        panel_intro=cfg.get("panel_intro",
            "Each row is a line taken from the book around one adverb. The rule is "
            "scored in your browser against the verb forms printed with the lines, "
            "and you can read every row and disagree with any of them."),
        script=script,
        expect={"avPreset": _expect(_ADV_PRESETS)},
    )


# The question rule on two sets of printed questions. `source` picks the set:
# austen, the 90 questions from the novel (re-cut at sentence boundaries by
# scripts/wordlists/concordance.py; the first cut started sixteen of its
# misses mid-sentence), or wilde, every question of two words or more in the
# play. The rule's misses are sorted five ways, each with its own tile.
WILDE_QUESTIONS = _data("wilde_questions.json")

_Q_SOURCES = {
    "austen": {k: QUESTION_DATA[k] for k in ("source", "questions", "verbs")},
    "wilde": {k: WILDE_QUESTIONS[k] for k in ("questions", "verbs", "cast")},
}

_Q_PRESETS = {
    "austen": [
        {"id": "aux", "label": "a question starts with a helping verb, or a wh-word then one",
         "expect": {"quHit": "52 of 90", "quPct": "57.8%", "quConnPct": "16 of 38, 42.1%"}},
    ],
    "wilde": [
        {"id": "aux", "label": "a question starts with a helping verb, or a wh-word then one",
         "expect": {"quHit": "89 of 256", "quPct": "34.8%", "quFrag": "14"}},
    ],
}


def _questions(cfg):
    source = cfg.get("source", "austen")
    if source not in _Q_SOURCES:
        raise ValueError("english_lab questions: unknown source %r (austen or wilde)" % source)
    data, presets = _Q_SOURCES[source], _Q_PRESETS[source]
    n = len(data["questions"])
    markup = (
        _kpis([("rule holds", "quHit", "&mdash;"), ("share", "quPct", "&mdash;"),
               ("starts with a joining word", "quConn", "&mdash;"),
               ("joining words, share of the misses", "quConnPct", "&mdash;")])
        + _kpis([("a wh-word, no helping verb after it", "quWh", "&mdash;"),
                 ("a word of address first", "quAddr", "&mdash;"),
                 ("a pronoun first: a statement", "quStmt", "&mdash;"),
                 ("no verb at all", "quFrag", "&mdash;"),
                 ("something else", "quOther", "&mdash;")])
        + _kpis([("questions in the modern documents", "quModQ", "&mdash;"),
                 ("words in them", "quModW", "&mdash;")])
        + '<p class="small-copy" id="quLimit"></p>'
        '<div class="table-wrap" style="max-height:22rem;overflow-y:auto;">'
        '<table id="quTable"><thead><tr>'
        '<th>question</th><th>verdict</th></tr></thead>'
        '<tbody id="quBody"></tbody></table></div>'
        + _MODERN_MARKUP % "qu"
    )
    controls = (
        '<label for="quPreset">Rule</label> '
        '<select id="quPreset">'
        + "".join('<option value="%s">%s</option>' % (p["id"], p["label"]) for p in presets)
        + '</select> '
        '<label for="quShow">Show</label> '
        '<select id="quShow">'
        '<option value="residue">only the ones it fails</option>'
        '<option value="all">every question</option>'
        '</select>'
    )
    limit = ("Words, not meanings: a line is sorted by its first word or two, and no verb at "
             "all means no word of the line is a helping verb or on the printed verb lists. "
             + ("The lines are from a play of 1895." if source == "wilde"
                else "The lines are from a novel of 1813."))
    script = (SCAN_JS + QUESTION_JS + cfg_literal("QU_DATA", data)
              + cfg_literal("MODERN", MODERN_DATA) + MODERN_JS
              + cfg_literal("QU_LIMIT", limit)) + r"""
(function () {
  var el = function (id) { return document.getElementById(id); };
  var show = 'residue';

  var scan = function () {
    var tiles = quTiles(QU_DATA), rows = quScore(QU_DATA).rows, k, i, html = '';
    for (k in tiles) if (inSet(tiles, k)) el(k).textContent = tiles[k];
    /* A question in print ends with a question mark; the modern documents are
       searched for one. */
    var qs = 0, d;
    for (d = 0; d < MODERN.docs.length; d++) qs += MODERN.docs[d].text.split('?').length - 1;
    el('quModQ').textContent = String(qs);
    el('quModW').textContent = commas(modernWords().length);
    el('quLimit').textContent = QU_LIMIT;
    for (i = 0; i < rows.length; i++) {
      if (show === 'residue' && rows[i][1] === QU_HOLDS) continue;
      html += '<tr><td>' + rows[i][0] + '</td><td>' + rows[i][1] + '</td></tr>';
    }
    el('quBody').innerHTML = html;
  };
  modernPrint('quModern');
  window.redrawLab = scan;
  el('quPreset').addEventListener('change', function () { scan(); });
  el('quShow').addEventListener('change', function () { show = this.value; scan(); });
  scan();
}());
"""
    play = source == "wilde"
    return Lab(
        title=("%d questions from a play, and a rule that covers a third" % n if play
               else "Ninety real questions, and a rule that covers just over half"),
        subtitle="The rule is stated, scored, and shown to fail -- which is the lesson",
        markup=markup, controls=controls,
        panel_title=cfg.get("panel_title", "A rule that does not work, and why that is printed"),
        panel_intro=cfg.get("panel_intro",
            ("These are the questions the characters ask in the play, each from where its "
             "sentence starts. The rule is scored against them in your browser, and the "
             "questions it misses are sorted by what they start with.") if play else
            ("These are real questions from the book, each from where its sentence starts. "
             "The rule is scored against them in your browser, and the half it misses is "
             "printed so you can see what questions actually look like.")),
        script=script,
        expect={"quPreset": _expect(presets)},
    )


# ---------------------------------------------------------------------------
# The irregular-verb modes. One printed list, three views of it.
# ---------------------------------------------------------------------------

IRREGULAR_DATA = _data("irregular_verbs.json")

# The sorting questions of six-patterns-not-one-hundred-and-eighty, asked in
# the lesson's order, run on the three printed forms of each verb. The class a
# verb lands in is COMPUTED here; the `class` field in the data file is not
# read by any page, and a test checks the two agree.
IRCLASS_JS = r"""
var IR_CLASSES = [
  { id: 'all_same',       size: 'all three the same',              ex: 'put' },
  { id: 'past_eq_pp',     size: 'past = form after have',          ex: 'bring' },
  { id: 'base_eq_pp',     size: 'base = form after have',          ex: 'come' },
  { id: 'base_eq_past',   size: 'base = past',                     ex: 'beat' },
  { id: 'all_diff_n',     size: 'all differ, last ends in -n',     ex: 'know' },
  { id: 'all_diff_other', size: 'all differ, last does not end in -n', ex: 'sing' }
];
/* A form written with a slash is two words (be: was/were), and a rule about
   equal strings cannot sort it: it stands outside the six. */
var irClassOf = function (v) {
  if (v.past.indexOf('/') >= 0 || v.pp.indexOf('/') >= 0) return 'outside';
  if (v.base === v.past && v.past === v.pp) return 'all_same';
  if (v.past === v.pp) return 'past_eq_pp';
  if (v.base === v.pp) return 'base_eq_pp';
  if (v.base === v.past) return 'base_eq_past';
  return /n$/.test(v.pp) ? 'all_diff_n' : 'all_diff_other';
};
/* The vowel pattern of sing, sang, sung: the first i of the base becomes a
   in the past and u in the form after have, and nothing else changes. */
var irIau = function (v) {
  var k = v.base.indexOf('i');
  if (k < 0) return false;
  return v.past === v.base.slice(0, k) + 'a' + v.base.slice(k + 1)
      && v.pp === v.base.slice(0, k) + 'u' + v.base.slice(k + 1);
};
var irCounts = function () {
  var counts = {}, i;
  for (i = 0; i < IR_DATA.verbs.length; i++) {
    var c = irClassOf(IR_DATA.verbs[i]);
    counts[c] = (counts[c] || 0) + 1;
  }
  return counts;
};
"""

_IR_PRESETS = [
    {"id": "all", "label": "every verb on the list", "cls": "",
     "expect": {"irCount": "133", "irClasses": "6", "irBiggest": "60"}},
    {"id": "past_eq_pp", "label": "past and participle are the same word", "cls": "past_eq_pp",
     "expect": {"irCount": "60", "irClasses": "6", "irBiggest": "60"}},
    {"id": "all_same", "label": "all three forms the same", "cls": "all_same",
     "expect": {"irCount": "21", "irClasses": "6", "irBiggest": "60"}},
    {"id": "all_diff_n", "label": "all three differ, participle ends in -n", "cls": "all_diff_n",
     "expect": {"irCount": "37", "irClasses": "6", "irBiggest": "60"}},
    {"id": "all_diff_other", "label": "all three differ, participle does not end in -n",
     "cls": "all_diff_other",
     "expect": {"irCount": "9", "irClasses": "6", "irBiggest": "60"}},
]


def _irregular(cfg):
    """The whole list, narrowed by class: the lesson that introduces the list."""
    markup = (
        _kpis([("verbs shown", "irCount", "&mdash;"), ("classes", "irClasses", "&mdash;"),
               ("largest class", "irBiggest", "&mdash;"), ("share of the list", "irPct", "&mdash;")])
        + '<div id="irRule" class="mathblock"></div>'
        '<div class="table-wrap"><table id="irTable"><thead><tr>'
        '<th>base</th><th>past</th><th>after <em>have</em></th><th>class</th>'
        '</tr></thead><tbody id="irBody"></tbody></table></div>'
    )
    controls = '<label for="irPreset">Which verbs</label> ' + _options("irPreset", _IR_PRESETS)
    script = (SCAN_JS + cfg_literal("IR_DATA", IRREGULAR_DATA) + IRCLASS_JS
              + cfg_literal("IR_PRESETS", _IR_PRESETS) + r"""
(function () {
  var el = function (id) { return document.getElementById(id); };
  var cls = '';

  var draw = function () {
    var rows = [], i, v, counts = irCounts(), biggest = 0, six = 0, k;
    for (i = 0; i < IR_DATA.verbs.length; i++) {
      v = IR_DATA.verbs[i];
      if (!cls || irClassOf(v) === cls) rows.push(v);
    }
    for (k = 0; k < IR_CLASSES.length; k++) {
      if (counts[IR_CLASSES[k].id]) six++;
      if ((counts[IR_CLASSES[k].id] || 0) > biggest) biggest = counts[IR_CLASSES[k].id];
    }
    el('irCount').textContent = String(rows.length);
    el('irClasses').textContent = String(six);
    el('irBiggest').textContent = String(biggest);
    el('irPct').textContent = share1(rows.length, IR_DATA.verbs.length);
    el('irRule').textContent = cls && IR_DATA.classes[cls]
      ? IR_DATA.classes[cls].rule
      : 'Every verb on the list. ' + (counts.outside || 0)
        + ' of them (be) stands outside the classes.';
    var html = '';
    for (i = 0; i < rows.length; i++) {
      html += '<tr><td>' + rows[i].base + '</td><td>' + rows[i].past
            + '</td><td>' + rows[i].pp + '</td><td>' + irClassOf(rows[i]).replace(/_/g, ' ')
            + '</td></tr>';
    }
    el('irBody').innerHTML = html;
  };
  window.redrawLab = draw;
  el('irPreset').addEventListener('change', function () {
    var i;
    for (i = 0; i < IR_PRESETS.length; i++) {
      if (IR_PRESETS[i].id === this.value) { cls = IR_PRESETS[i].cls; draw(); return; }
    }
  });
  draw();
}());
""")
    return Lab(
        title="Every irregular verb the course covers, with its three forms",
        subtitle="133 verbs, and the class the sorting questions put each one in",
        markup=markup, controls=controls,
        panel_title=cfg.get("panel_title", "The whole list, and how it divides"),
        panel_intro=cfg.get("panel_intro",
            "Every verb here is printed with its three forms. Choose a class and "
            "the list narrows to the verbs that follow it, with the rule that "
            "defines it printed above the table."),
        script=script, expect={"irPreset": _expect(_IR_PRESETS)},
    )


# The six classes, plus the one vowel pattern the lesson names. Each preset
# pins how many verbs the questions put in it and where those verbs land.
_CL_PRESETS = [
    {"id": "past_eq_pp", "label": "past = form after have (bring)",
     "expect": {"clCount": "60", "clWhere": "past = form after have: 60"}},
    {"id": "all_diff_n", "label": "all three differ, last ends in -n (know)",
     "expect": {"clCount": "37", "clWhere": "all differ, last ends in -n: 37"}},
    {"id": "all_same", "label": "all three the same (put)",
     "expect": {"clCount": "21", "clWhere": "all three the same: 21"}},
    {"id": "all_diff_other", "label": "all three differ, last does not end in -n (go, sing)",
     "expect": {"clCount": "9", "clWhere": "all differ, last does not end in -n: 9"}},
    {"id": "base_eq_pp", "label": "base = form after have (come)",
     "expect": {"clCount": "4", "clWhere": "base = form after have: 4"}},
    {"id": "base_eq_past", "label": "base = past (beat)",
     "expect": {"clCount": "1", "clWhere": "base = past: 1"}},
    {"id": "iau", "label": "the vowels i, a, u (sing, sang, sung), whatever the class",
     "expect": {"clCount": "7",
                "clWhere": "all differ, last ends in -n: 1; all differ, last does not end in -n: 6"}},
]


def _classes(cfg):
    """Six string rules, run: a distinct widget from `irregular`'s list.

    The lesson claims six classes of 60, 37, 21, 9, 4 and 1, with be outside,
    and that the class of nine is the i-a-u verbs plus go, do and undergo,
    while begin -- same vowels -- lands in the class of 37. Every one of those
    counts is computed here from the three printed forms.
    """
    markup = (
        _kpis([("verbs in this pattern", "clCount", "&mdash;"),
               ("share of the sorted verbs", "clShare", "&mdash;"),
               ("where the questions put them", "clWhere", "&mdash;"),
               ("outside all six", "clOutside", "&mdash;")])
        + '<div class="table-wrap"><table id="clSummary"><thead><tr>'
        '<th>question</th><th>class</th><th>verbs</th><th>for example</th>'
        '</tr></thead><tbody id="clSumBody"></tbody></table></div>'
        '<div class="table-wrap"><table id="clTable"><thead><tr>'
        '<th>base</th><th>past</th><th>after <em>have</em></th><th>class</th>'
        '</tr></thead><tbody id="clBody"></tbody></table></div>'
    )
    controls = '<label for="clPreset">Which pattern</label> ' + _options("clPreset", _CL_PRESETS)
    script = (SCAN_JS + cfg_literal("IR_DATA", IRREGULAR_DATA) + IRCLASS_JS
              + cfg_literal("CL_PRESETS", _CL_PRESETS) + r"""
(function () {
  var el = function (id) { return document.getElementById(id); };
  var pick = 'past_eq_pp';
  var label = {}, k;
  for (k = 0; k < IR_CLASSES.length; k++) label[IR_CLASSES[k].id] = IR_CLASSES[k].size;

  var draw = function () {
    var counts = irCounts(), sorted = IR_DATA.verbs.length - (counts.outside || 0);
    var rows = [], where = {}, order = [], i, v, c, html = '';
    for (i = 0; i < IR_DATA.verbs.length; i++) {
      v = IR_DATA.verbs[i]; c = irClassOf(v);
      if (pick === 'iau' ? irIau(v) : c === pick) {
        rows.push(v);
        if (!where[c]) { where[c] = 0; order.push(c); }
        where[c]++;
      }
    }
    /* Report the classes in the lesson's order, not the list's. */
    var parts = [];
    for (k = 0; k < IR_CLASSES.length; k++) {
      if (where[IR_CLASSES[k].id]) parts.push(IR_CLASSES[k].size + ': ' + where[IR_CLASSES[k].id]);
    }
    el('clCount').textContent = String(rows.length);
    el('clShare').textContent = share1(rows.length, sorted);
    el('clWhere').textContent = parts.join('; ');
    el('clOutside').textContent = String(counts.outside || 0);

    var q = ['1. all three the same?', '2. past = form after have?', '3. base = one of the others?',
             '3. base = one of the others?', '4. all differ: last letter -n?', '4. all differ: last letter -n?'];
    for (k = 0; k < IR_CLASSES.length; k++) {
      html += '<tr><td>' + q[k] + '</td><td>' + IR_CLASSES[k].size + '</td><td>'
            + (counts[IR_CLASSES[k].id] || 0) + '</td><td>' + IR_CLASSES[k].ex + '</td></tr>';
    }
    el('clSumBody').innerHTML = html;
    html = '';
    for (i = 0; i < rows.length; i++) {
      html += '<tr><td>' + rows[i].base + '</td><td>' + rows[i].past + '</td><td>'
            + rows[i].pp + '</td><td>' + label[irClassOf(rows[i])] + '</td></tr>';
    }
    el('clBody').innerHTML = html;
  };
  window.redrawLab = draw;
  el('clPreset').addEventListener('change', function () { pick = this.value; draw(); });
  draw();
}());
""")
    return Lab(
        title="Six patterns, and the rule that decides each one",
        subtitle="The sorting questions run on every verb's three written forms",
        markup=markup, controls=controls,
        panel_title=cfg.get("panel_title", "Pick a pattern and read its rule"),
        panel_intro=cfg.get("panel_intro",
            "The four questions are asked of every verb's three written forms, in "
            "order, and the table counts where each verb lands. Pick a class to "
            "read its verbs, or the vowel pattern to see it cut across two classes."),
        script=script, expect={"clPreset": _expect(_CL_PRESETS)},
    )


_SH_PRESETS = [
    {"id": "with", "label": "count be, have and do as irregular verbs", "big": 1,
     "expect": {"shCount": "149", "shPct": "15.9%", "shBig": "91", "shBigPct": "61.1%",
                "shTop": "95.3%"}},
    {"id": "without", "label": "leave be, have and do out", "big": 0,
     "expect": {"shCount": "58", "shPct": "6.2%", "shBig": "91", "shBigPct": "61.1%",
                "shTop": "93.1%"}},
]


def _irrshare(cfg):
    markup = (
        '<div class="kpi-grid">'
        '<div class="kpi"><span>irregular forms found</span>'
        '<strong id="shCount">&mdash;</strong></div>'
        '<div class="kpi"><span>share of the passage</span>'
        '<strong id="shPct">&mdash;</strong></div>'
        '<div class="kpi"><span>be, have and do alone</span>'
        '<strong id="shBig">&mdash;</strong></div>'
        '<div class="kpi"><span>their share of the irregulars</span>'
        '<strong id="shBigPct">&mdash;</strong></div>'
        '<div class="kpi"><span>the twenty commonest verbs, share of the irregular forms</span>'
        '<strong id="shTop">&mdash;</strong></div>'
        '</div>'
        '<div class="table-wrap"><table id="shTable"><thead><tr>'
        '<th>verb</th><th>times it appears</th></tr></thead>'
        '<tbody id="shBody"></tbody></table></div>'
        '<div class="mathblock" id="shPassage" style="font-size:0.8rem;"></div>'
    )
    controls = (
        '<label for="shPreset">How to count</label> <select id="shPreset">'
        + "".join('<option value="{}">{}</option>'.format(p["id"], p["label"])
                  for p in _SH_PRESETS)
        + "</select>"
    )
    script = (ENGLISH_VERB_JS + SCAN_JS + cfg_literal("SH_IRR", IRREGULAR_DATA)
              + cfg_literal("SH_TEXT", _data("wordorder_passage.json"))
              + cfg_literal("SH_PRESETS", _SH_PRESETS) + r"""
(function () {
  var el = function (id) { return document.getElementById(id); };
  var BIG = setOf(['be', 'have', 'do']);
  var withBig = true;

  /* Every written form of every verb on the printed list, mapped to its base.
     The past and past-participle columns can hold more than one spelling
     ('was/were'), so each is split. The present takes the -s rule and the
     -ing form the spelling rules, both the ones the tense-table lesson
     teaches (vbThird, vbIng: drop a silent e, double a stressed final
     consonant). be and have are the two the rules cannot form, so their
     present is written out here: am, is, are; has. */
  VB_IRREG = { be: { third: 'is', ing: 'being' }, have: { third: 'has' } };
  var SH_ALSO = { be: ['am', 'are'] };
  var form2base = {};
  (function () {
    var i, j, k, v, b, forms;
    for (i = 0; i < SH_IRR.verbs.length; i++) {
      v = SH_IRR.verbs[i]; b = v.base;
      forms = [b, vbThird(b), vbIng(b)].concat(SH_ALSO[b] || []);
      if (v.past) forms = forms.concat(v.past.split('/'));
      if (v.pp) forms = forms.concat(v.pp.split('/'));
      for (j = 0; j < forms.length; j++) {
        k = forms[j];
        if (k) form2base[k] = b;
      }
    }
  }());

  var draw = function () {
    var toks = lower(wordsOf(SH_TEXT.passage)), counts = {}, total = 0, big = 0, i, base;
    for (i = 0; i < toks.length; i++) {
      if (!inSet(form2base, toks[i])) continue;
      base = form2base[toks[i]];
      if (inSet(BIG, base)) { big++; if (!withBig) continue; }
      counts[base] = (counts[base] || 0) + 1;
      total++;
    }
    el('shCount').textContent = String(total);
    el('shPct').textContent = share1(total, toks.length);
    el('shBig').textContent = String(big);
    /* be/have/do as a share of the irregulars WITH them counted, always: the
       point of the tile is what they contribute, so the denominator must not
       move when the menu does. */
    el('shBigPct').textContent = share1(big, withBig ? total : total + big);
    var names = Object.keys(counts);
    /* Commonest first, ties in alphabetical order, so the twenty are always
       the same twenty; the tie at the edge cannot change the sum. */
    names.sort(function (a, b) { return counts[b] - counts[a] || (a < b ? -1 : 1); });
    var top = 0;
    for (i = 0; i < names.length && i < 20; i++) top += counts[names[i]];
    el('shTop').textContent = share1(top, total);
    var html = '';
    for (i = 0; i < names.length; i++) {
      html += '<tr><td>' + names[i] + '</td><td>' + counts[names[i]] + '</td></tr>';
    }
    el('shBody').innerHTML = html;
    el('shPassage').textContent = SH_TEXT.passage;
  };
  window.redrawLab = draw;
  el('shPreset').addEventListener('change', function () {
    withBig = this.value === 'with'; draw();
  });
  draw();
}());
""")
    return Lab(
        title="How much of a real page is an irregular verb",
        subtitle="Counted on the passage below, with and without be, have and do",
        markup=markup, controls=controls,
        panel_title=cfg.get("panel_title", "Count them yourself"),
        panel_intro=cfg.get("panel_intro",
            "The passage is printed under the table. Every word in it is checked "
            "against the printed list of irregular verbs, and the menu decides "
            "whether be, have and do are counted. Watch what happens when they "
            "are not."),
        script=script, expect={"shPreset": _expect(_SH_PRESETS)},
    )




# ---------------------------------------------------------------------------
# listening -- the one thing a page can teach about hearing English
#
# The page reads itself aloud with the browser's voice; what this mode adds
# is knowing what to listen for. A learner who says English is "too fast" is usually
# failing at is not speed but WORD BOUNDARIES, and the two regularities native
# listeners use to find them can both be printed:
#
#   function words reduce, and they are nearly half of every sentence;
#   content words almost always BEGIN with the strong syllable, so a strong
#   syllable is a good guess at where a word starts (Cutler and Carter 1987).
#
# Both are annotation, both are printed, and both are counted on the page.
# ---------------------------------------------------------------------------

LISTENING_DATA = _data("listening.json")

_LS_PRESETS = [
    {"id": "weak", "label": "mark the words that get squashed", "view": "weak",
     "expect": {"lsWeak": "387 of 936", "lsWeakPct": "41.3%", "lsTypes": "43", "lsMixed": "42",
                "lsFinal": "24 of 387"}},
    {"id": "strong", "label": "mark where each other word is said hardest", "view": "strong",
     "expect": {"lsStrong": "390 of 474", "lsStrongPct": "82.3%"}},
]


def _listening(cfg):
    markup = (
        _kpis([("words that can be squashed", "lsWeak", "&mdash;"),
               ("share of the page", "lsWeakPct", "&mdash;"),
               ("different ones used", "lsTypes", "&mdash;"),
               ("of them that, have, has or had", "lsMixed", "&mdash;"),
               ("other words starting strong", "lsStrongPct", "&mdash;"),
               ("squashable words before . , ; : ? or !", "lsFinal", "&mdash;")])
        + _kpis([("of the other words, starting strong", "lsStrong", "&mdash;")])
        + '<div class="mathblock" id="lsText" style="font-size:0.84rem;line-height:2;"></div>'
        '<div class="table-wrap"><table id="lsTable"><thead><tr>'
        '<th>word</th><th>squashed, said as</th><th>times on the page</th>'
        '</tr></thead><tbody id="lsBody"></tbody></table></div>'
    )
    controls = (
        '<label for="lsPreset">What to mark</label> ' + _options("lsPreset", _LS_PRESETS)
    )
    script = (SCAN_JS + cfg_literal("LS_DATA", LISTENING_DATA)
              + cfg_literal("LS_TEXT", _data("wordorder_passage.json"))
              + cfg_literal("LS_PRESETS", _LS_PRESETS) + r"""
(function () {
  var el = function (id) { return document.getElementById(id); };
  var view = 'weak';

  var draw = function () {
    var w = wordsOf(LS_TEXT.passage), lw = lower(w), i, t;
    /* Every token of a word on the list is counted, so the count is of words
       that CAN take a weak form. Demonstrative that (that book) and have as
       a main verb (have tea) keep their full form; the tile below says how
       many of the tokens are those four words, and the table lists every
       word with its count, so the reader can see what was counted. */
    var MIXED = setOf(['that', 'have', 'has', 'had']), mixed = 0;
    var weak = 0, types = {}, strong = 0, annotated = 0, out = [];
    for (i = 0; i < lw.length; i++) {
      t = lw[i];
      if (inSet(LS_DATA.weak, t)) {
        weak++; types[t] = (types[t] || 0) + 1;
        if (inSet(MIXED, t)) mixed++;
        out.push(view === 'weak' ? '[' + w[i] + ']' : w[i]);
      } else if (inSet(LS_DATA.stress, t) || inSet(LS_DATA.stress, t.replace(/'s$/, ''))) {
        /* A possessive is marked as its word: aunt's as aunt. */
        annotated++;
        var pat = LS_DATA.stress[inSet(LS_DATA.stress, t) ? t : t.replace(/'s$/, '')];
        if (pat.charAt(0) === 'S') strong++;
        out.push(view === 'strong' ? w[i] + '(' + pat + ')' : w[i]);
      } else {
        out.push(w[i]);
      }
    }
    /* The listed words that stand last before a punctuation mark, where a
       weak form is said in full: the scan looks at the character after each
       word, past a closing quotation mark. */
    var re = /[A-Za-z][A-Za-z']*/g, txt = normApos(LS_TEXT.passage), m, after, fin = 0;
    while ((m = re.exec(txt)) !== null) {
      if (!inSet(LS_DATA.weak, m[0].replace(/'+$/, '').toLowerCase())) continue;
      after = txt.slice(re.lastIndex).replace(/^['”’]+/, '').charAt(0);
      if ('.,;:?!'.indexOf(after) >= 0 && after !== '') fin++;
    }
    el('lsFinal').textContent = fin + ' of ' + weak;
    el('lsWeak').textContent = weak + ' of ' + lw.length;
    el('lsWeakPct').textContent = share1(weak, lw.length);
    el('lsTypes').textContent = String(Object.keys(types).length);
    el('lsMixed').textContent = String(mixed);
    el('lsStrong').textContent = strong + ' of ' + annotated;
    el('lsStrongPct').textContent = share1(strong, annotated);
    el('lsText').textContent = out.join(' ');

    var names = Object.keys(types).sort(), html = '';
    names.sort(function (a, b) { return types[b] - types[a] || (a < b ? -1 : 1); });
    for (i = 0; i < names.length; i++) {
      html += '<tr><td>' + names[i] + '</td><td>'
            + (LS_DATA.weak[names[i]] || '') + '</td><td>' + types[names[i]] + '</td></tr>';
    }
    el('lsBody').innerHTML = html;
  };
  window.redrawLab = draw;
  el('lsPreset').addEventListener('change', function () {
    var i;
    for (i = 0; i < LS_PRESETS.length; i++) {
      if (LS_PRESETS[i].id === this.value) { view = LS_PRESETS[i].view; draw(); return; }
    }
  });
  draw();
}());
""")
    return Lab(
        title="Why it sounds too fast, marked on the page",
        subtitle="Press Listen above to hear the page; this marks what to listen for",
        markup=markup, controls=controls,
        panel_title=cfg.get("panel_title", "Mark the squashed words, then the strong parts"),
        panel_intro=cfg.get("panel_intro",
            "Press Listen at the top of the page to hear it read. What this marks "
            "is which words get squashed when people speak, and which part of "
            "every other word is said hardest. Both are counted on the passage below, and the "
            "squashed words are listed with how they are actually said."),
        script=script, expect={"lsPreset": _expect(_LS_PRESETS)},
    )


# ---------------------------------------------------------------------------
# The second instalment (docs/english-v2/PLAN.md section D). Each mode ships
# SCAN_JS, the rule block from english_core.py, the data it reads, and the
# block below that writes the tiles the rule block returns. The figures in
# the presets were read off rendered pages with labcheck.js --observe and
# agree with scripts/wordlists/english_check.js, which runs the same blocks.
# ---------------------------------------------------------------------------

def _shipped(presets, cfg, key, default):
    """The preset a lesson ships selected: cfg[key], which must be one of them."""
    chosen = cfg.get(key, default)
    if chosen not in [p["id"] for p in presets]:
        raise ValueError("english_lab: %s %r is not one of %s"
                         % (key, chosen, ", ".join(p["id"] for p in presets)))
    return chosen


def _restrict(presets, cfg):
    """cfg['rules'] restricts a menu to the presets a lesson shows, in its order."""
    if not cfg.get("rules"):
        return presets
    by_id = {p["id"]: p for p in presets}
    missing = [r for r in cfg["rules"] if r not in by_id]
    if missing:
        raise ValueError("english_lab: unknown rules %s" % ", ".join(missing))
    return [by_id[r] for r in cfg["rules"]]


def _preset_menu(select_id, presets, chosen):
    return _menu(select_id, [(p["id"], p["label"]) for p in presets], chosen)


def _payload(data, *keys):
    """Only the fields a page reads: the notes and sha256 pins stay in the
    committed file, where a reviewer reads them, and off the wire."""
    return {k: data[k] for k in keys if k in data}


def _scroll_table(table_id, cols_id, body_id, rem=20):
    return ('<div class="table-wrap" style="max-height:%drem;overflow-y:auto;">'
            '<table id="%s"><thead><tr id="%s"></tr></thead><tbody id="%s"></tbody></table></div>'
            % (rem, table_id, cols_id, body_id))


# Every page that reads a CMUdict-derived file says where it came from.
_CMUDICT_CREDIT = ("Sounds are from CMUdict (Carnegie Mellon University, BSD licence; the "
                   "notice is in scripts/wordlists/CMUDICT_LICENSE).")

# A shared tile writer: every rule block returns {tile id: text}.
_WRITE_TILES = r"""
var writeTiles = function (tiles) {
  var k, node;
  for (k in tiles) {
    if (!inSet(tiles, k)) continue;
    node = document.getElementById(k);
    if (node) node.textContent = tiles[k];
  }
};
"""


# ---------------------------------------------------------------- endings

VERB_SOUNDS = _wordlist("verb_sounds.json")

_EN_PRESETS = [
    {"id": "ed", "label": "the past ending, -ed",
     "expect": {"enHit": "1111 of 1118", "enPct": "99.4%",
                "enFirst": "abused, closed, excused, housed, legged, mouthed, used"}},
    {"id": "s", "label": "the he, she and it ending, -s",
     "expect": {"enHit": "1187 of 1189", "enPct": "99.8%", "enFirst": "knives, mouths"}},
    {"id": "plural", "label": "the same -s rule on the plurals of nouns",
     "expect": {"enHit": "1820 of 1823", "enPct": "99.8%", "enFirst": "mouths, paths, youths"}},
]


def _endings(cfg):
    rule = _shipped(_EN_PRESETS, cfg, "rule", "ed")
    show = cfg.get("show", "misses")
    markup = (
        _kpis([("the rule", "enRule", "&mdash;"), ("the rule is right", "enHit", "&mdash;"),
               ("share", "enPct", "&mdash;"), ("it misses", "enMiss", "&mdash;"),
               ("the words it misses", "enFirst", "&mdash;"),
               ("not in the dictionary, not counted", "enSkipped", "&mdash;")])
        + _kpis([("the word you typed", "enWordSays", "&mdash;")])
        + '<p class="small-copy" id="enLimit"></p>'
        + _scroll_table("enTable", "enCols", "enBody")
    )
    controls = (
        '<label for="enPreset">The ending</label> ' + _preset_menu("enPreset", _EN_PRESETS, rule)
        + ' <label for="enShow">List</label> '
        + _menu("enShow", [("misses", "the words the rule misses"), ("all", "every word"),
                           ("skipped", "the words the dictionary does not carry")], show)
        + ' <label for="enWord">A word from the list</label> '
        '<input id="enWord" type="text" value="walk" size="14" />'
    )
    script = (SCAN_JS + ENDINGS_JS + _WRITE_TILES + cfg_literal("EN_DATA", _payload(VERB_SOUNDS, "ed", "s", "plural", "skipped"))
              + cfg_literal("EN_LIMIT", "The sounds are the dictionary's first pronunciation of "
                            "each word, which is American; a word it does not carry is listed, "
                            "not counted. " + _CMUDICT_CREDIT)) + r"""
(function () {
  var el = function (id) { return document.getElementById(id); };
  var rule = el('enPreset').value, show = el('enShow').value;
  var draw = function () {
    var res = enScore(EN_DATA, rule), html = '', rows, i, r, keys;
    writeTiles(enTiles(EN_DATA, rule));
    el('enWordSays').textContent = enWordSays(EN_DATA, rule, el('enWord').value);
    el('enLimit').textContent = EN_LIMIT;
    if (show === 'skipped') {
      el('enCols').innerHTML = '<th>word</th><th>why it is not counted</th>';
      keys = Object.keys(EN_DATA.skipped[EN_RULES[rule][1]]);
      for (i = 0; i < keys.length; i++) {
        html += '<tr><td>' + keys[i] + '</td><td>' + EN_DATA.skipped[EN_RULES[rule][1]][keys[i]] + '</td></tr>';
      }
    } else {
      el('enCols').innerHTML = '<th>word</th><th>form</th><th>last sound</th><th>which is</th>'
        + '<th>the rule says</th><th>the dictionary says</th><th></th>';
      rows = show === 'all' ? res.all : res.miss;
      for (i = 0; i < rows.length; i++) {
        r = rows[i];
        html += '<tr><td>' + r.word + '</td><td>' + r.form + '</td><td>' + r.last + '</td><td>'
              + r.cls + '</td><td>' + r.rule + '</td><td>' + r.dict + '</td><td>'
              + (r.ok ? '' : 'missed') + '</td></tr>';
      }
    }
    el('enBody').innerHTML = html;
  };
  window.redrawLab = draw;
  el('enPreset').addEventListener('change', function () { rule = this.value; draw(); });
  el('enShow').addEventListener('change', function () { show = this.value; draw(); });
  el('enWord').addEventListener('input', function () {
    el('enWordSays').textContent = enWordSays(EN_DATA, rule, this.value);
  });
  draw();
}());
"""
    return Lab(
        title="How -ed and -s are said, from the last sound of the word",
        subtitle="Two rules run on every verb in the printed list, and scored against the dictionary",
        markup=markup, controls=controls,
        panel_title=cfg.get("panel_title", "Score the two rules on the printed list"),
        panel_intro=cfg.get("panel_intro",
            "Each verb's last sound is looked up in a pronunciation dictionary. The rule says "
            "what the ending should sound like; the dictionary says what it does. The table "
            "prints both for every word, and the words where they differ."),
        script=script, expect={"enPreset": _expect(_EN_PRESETS)},
    )


# ---------------------------------------------------------------- wordrule

PLURAL_NOUNS = _wordlist("plural_nouns.json")
LY_ADJECTIVES = _wordlist("ly_adjectives.json")

_WR_PRESETS = {
    "plurals": [
        {"id": "r0", "label": "-s, -es after a hiss, -y to -ies",
         "expect": {"wrHit": "1866 of 1887", "wrPct": "98.9%",
                    "wrFirst": "analysis, chairman, child, crisis, die, emphasis, foot, gentleman, "
                               "half, hypothesis, life, man, mouse, phenomenon, potato, self, shelf, "
                               "stomach, tooth, wife, woman",
                    "wrNone": "75", "wrNoneOf": "75 of 683"}},
        {"id": "r1", "label": "the same, and a consonant then -o takes -es",
         "expect": {"wrHit": "1864 of 1887", "wrPct": "98.8%",
                    "wrFirst": "analysis, chairman, child, crisis, die, emphasis, foot, gentleman, "
                               "half, hypothesis, life, man, mouse, phenomenon, photo, piano, pro, "
                               "self, shelf, stomach, tooth, wife, woman"}},
        {"id": "r2", "label": "the same, and f or fe becomes -ves",
         "expect": {"wrHit": "1861 of 1887", "wrPct": "98.6%",
                    "wrFirst": "analysis, belief, brief, chairman, chief, child, crisis, die, "
                               "emphasis, foot, gentleman, golf, hypothesis, man, mouse, phenomenon, "
                               "photo, piano, pro, proof, relief, roof, safe, stomach, tooth, woman"}},
        {"id": "r3", "label": "the same, with -ves only after -lf, -ife, -eaf, -olf",
         "expect": {"wrHit": "1868 of 1887", "wrPct": "99.0%",
                    "wrFirst": "analysis, chairman, child, crisis, die, emphasis, foot, gentleman, "
                               "golf, hypothesis, man, mouse, phenomenon, photo, piano, pro, "
                               "stomach, tooth, woman"}},
    ],
    "ly": [
        {"id": "plain", "label": "add -ly to the adjective",
         "expect": {"wrHit": "98 of 126", "wrPct": "77.8%", "wrNone": "27",
                    "wrFirst": "acceptable, angry, capable, comfortable, considerable, crazy, "
                               "democratic, dramatic, economic, electronic, ethnic, extraordinary, "
                               "flexible, genetic, guilty, healthy, historic, horrible, impossible, "
                               "lazy, necessary, reasonable, reliable, remarkable, scientific, "
                               "suitable, tall, terrible"}},
        {"id": "changes", "label": "add -ly, with the spelling changes",
         "expect": {"wrHit": "126 of 126", "wrPct": "100.0%", "wrNone": "27", "wrFirst": "none"}},
    ],
}


def _wordrule(cfg):
    lst = cfg.get("list", "plurals")
    if lst not in _WR_PRESETS:
        raise ValueError("english_lab wordrule: list is plurals or ly, not %r" % lst)
    presets = _WR_PRESETS[lst]
    rule = _shipped(presets, cfg, "rule", presets[0]["id"])
    plurals = lst == "plurals"
    data = PLURAL_NOUNS if plurals else LY_ADJECTIVES
    none_value = "noplural" if plurals else "none"
    shows = [("misses", "the words the rule misses"), ("all", "every word")]
    shows.append((none_value, "nouns the dictionary gives no plural" if plurals
                  else "adjectives with no -ly adverb in the dictionary"))
    if plurals:
        shows.append(("excluded", "the words set aside, and why"))
    show = cfg.get("show", "misses")
    if show not in [v for v, _l in shows]:
        raise ValueError("english_lab wordrule: show %r is not offered for %s" % (show, lst))
    markup = (
        _kpis([("the rule", "wrRule", "&mdash;"), ("the rule is right", "wrHit", "&mdash;"),
               ("share", "wrPct", "&mdash;"), ("it misses", "wrMiss", "&mdash;"),
               ("the words it misses", "wrFirst", "&mdash;")])
        + _kpis([("nouns with no plural" if plurals else "adjectives with no -ly adverb",
                  "wrNone", "&mdash;"),
                 ("of the nouns that are only nouns" if plurals else "of the adjectives",
                  "wrNoneOf", "&mdash;")])
        + '<p class="small-copy" id="wrLimit"></p>'
        + _scroll_table("wrTable", "wrCols", "wrBody")
    )
    controls = (
        '<label for="wrPreset">The rule</label> ' + _preset_menu("wrPreset", presets, rule)
        + ' <label for="wrShow">List</label> ' + _menu("wrShow", shows, show)
    )
    limit = ("Spellings, not meanings: the dictionary says a word exists, not that it is the "
             + ("plural of this noun. Which words are nouns comes from the Moby list, checked "
                "against the dictionary; the list is not printed."
                if plurals else
                "adverb of this adjective (hardly is a word, and does not mean hard)."))
    script = (SCAN_JS + WORDRULE_JS + _WRITE_TILES + cfg_literal("WR_DATA", _payload(data, "rows", "noun_only", "noplural", "none", "excluded"))
              + cfg_literal("WR_LIMIT", limit)) + r"""
(function () {
  var el = function (id) { return document.getElementById(id); };
  var rule = el('wrPreset').value, show = el('wrShow').value;
  var draw = function () {
    var res = wrScore(WR_DATA, rule), html = '', rows, i, keys, none;
    writeTiles(wrTiles(WR_DATA, rule));
    el('wrLimit').textContent = WR_LIMIT;
    if (show === 'noplural' || show === 'none') {
      el('wrCols').innerHTML = '<th>word</th>';
      none = wrNoneList(WR_DATA);
      for (i = 0; i < none.length; i++) html += '<tr><td>' + none[i] + '</td></tr>';
    } else if (show === 'excluded') {
      el('wrCols').innerHTML = '<th>word</th><th>why it is set aside</th>';
      keys = Object.keys(WR_DATA.excluded || {});
      for (i = 0; i < keys.length; i++) {
        html += '<tr><td>' + keys[i] + '</td><td>' + WR_DATA.excluded[keys[i]] + '</td></tr>';
      }
    } else {
      el('wrCols').innerHTML = '<th>word</th><th>the rule says</th><th>the dictionary has</th><th></th>';
      rows = show === 'all' ? res.all : res.miss;
      for (i = 0; i < rows.length; i++) {
        html += '<tr><td>' + rows[i].word + '</td><td>' + rows[i].said + '</td><td>'
              + rows[i].list.join(' / ') + '</td><td>' + (rows[i].ok ? '' : 'missed') + '</td></tr>';
      }
    }
    el('wrBody').innerHTML = html;
  };
  window.redrawLab = draw;
  el('wrPreset').addEventListener('change', function () { rule = this.value; draw(); });
  el('wrShow').addEventListener('change', function () { show = this.value; draw(); });
  draw();
}());
"""
    return Lab(
        title=("The plural rule, scored on every noun in the list" if plurals
               else "The -ly rule, scored on every adjective in the list"),
        subtitle="Each word's form is made by the rule on the page and checked against a dictionary",
        markup=markup, controls=controls,
        panel_title=cfg.get("panel_title", "Score the rule on the printed list"),
        panel_intro=cfg.get("panel_intro",
            "The rule makes each word's form in your browser. A form counts as right when it "
            "is one the dictionary has for that word, and every word the rule gets wrong is "
            "printed with what the dictionary has instead."),
        script=script, expect={"wrPreset": _expect(presets)},
    )


# ---------------------------------------------------------------- an

AN_DATA = _data("an_concordance.json")
AN_SOUNDS = _wordlist("an_sounds.json")["first"]

_AN_PRESETS = [
    {"id": "letter", "label": "an before a vowel letter",
     "expect": {"anHit": "486 of 493", "anPct": "98.6%",
                "anFirst": "a University, an hour (5), a utilitarian"}},
    {"id": "sound", "label": "an before a vowel sound",
     "expect": {"anHit": "493 of 493", "anPct": "100.0%", "anFirst": "none"}},
]

# What each rule prints when a lesson ships another text chosen in anSource.
_AN_BY_SOURCE = {
    "wilde": {"letter": {"anHit": "448 of 455", "anPct": "98.5%",
                         "anFirst": "a University, an hour (5), a utilitarian"},
              "sound": {"anHit": "455 of 455", "anPct": "100.0%", "anFirst": "none"}},
    "modern": {"letter": {"anHit": "29 of 29", "anPct": "100.0%", "anFirst": "none"},
               "sound": {"anHit": "29 of 29", "anPct": "100.0%", "anFirst": "none"}},
    "passage": {"letter": {"anHit": "9 of 9", "anPct": "100.0%", "anFirst": "none"},
                "sound": {"anHit": "9 of 9", "anPct": "100.0%", "anFirst": "none"}},
}

_AN_SOURCES = [("all", "all three texts"), ("wilde", "the play"),
               ("modern", "the modern documents"), ("passage", "the passage from the novel")]
_AN_CODES = {"w": "the play", "m": "the modern documents", "p": "the passage"}


def _an(cfg):
    rule = _shipped(_AN_PRESETS, cfg, "rule", "letter")
    source = cfg.get("source", "all")
    if source not in dict(_AN_SOURCES):
        raise ValueError("english_lab an: unknown source %r" % source)
    markup = (
        _kpis([("the rule", "anRule", "&mdash;"), ("lines scored", "anN", "&mdash;"),
               ("the rule is right", "anHit", "&mdash;"), ("share", "anPct", "&mdash;"),
               ("it misses", "anMiss", "&mdash;"), ("the lines it misses", "anFirst", "&mdash;")])
        + _kpis([("next word not in the dictionary, not scored", "anUnknown", "&mdash;")])
        + '<p class="small-copy" id="anLimit"></p>'
        + _scroll_table("anTable", "anCols", "anBody", 22)
        + '<details><summary>Words that look like a but are not</summary>'
        '<div class="table-wrap"><table><tbody id="anMarkers"></tbody></table></div></details>'
    )
    controls = (
        '<label for="anPreset">The rule</label> ' + _preset_menu("anPreset", _AN_PRESETS, rule)
        + ' <label for="anSource">Lines from</label> ' + _menu("anSource", _AN_SOURCES, source)
    )
    script = (SCAN_JS + AN_JS + _WRITE_TILES + cfg_literal("AN_ROWS", AN_DATA["rows"])
              + cfg_literal("AN_MARKERS", AN_DATA["markers"]) + cfg_literal("AN_FIRST", AN_SOUNDS)
              + cfg_literal("AN_CODES", _AN_CODES)
              + cfg_literal("AN_LIMIT", "The sound is the dictionary's first pronunciation of the "
                            "next word, which is American; a word it does not carry is listed and "
                            "not scored. The play is English of 1895. " + _CMUDICT_CREDIT)) + r"""
(function () {
  var el = function (id) { return document.getElementById(id); };
  var rule = el('anPreset').value, source = el('anSource').value;
  var draw = function () {
    var res = anScore(AN_ROWS, AN_FIRST, rule, source), html = '', i, a, verdict;
    writeTiles(anTiles(AN_ROWS, AN_FIRST, rule, source));
    el('anLimit').textContent = AN_LIMIT;
    el('anCols').innerHTML = '<th>from</th><th>the line</th><th>the rule says</th><th></th>';
    for (i = 0; i < res.all.length; i++) {
      a = res.all[i];
      verdict = a.says === null ? 'not in the dictionary' : (a.ok ? '' : 'missed');
      html += '<tr><td>' + AN_CODES[a.line[0]] + '</td><td>' + a.line[1] + ' <strong>' + a.line[2]
            + ' ' + a.line[3] + '</strong> ' + a.line[4] + '</td><td>' + (a.says || '') + '</td><td>'
            + verdict + '</td></tr>';
    }
    el('anBody').innerHTML = html;
    html = '';
    for (i = 0; i < AN_MARKERS.length; i++) {
      html += '<tr><td>' + AN_MARKERS[i][1] + '</td><td>' + AN_MARKERS[i][2] + '</td></tr>';
    }
    el('anMarkers').innerHTML = html;
  };
  window.redrawLab = draw;
  el('anPreset').addEventListener('change', function () { rule = this.value; draw(); });
  el('anSource').addEventListener('change', function () { source = this.value; draw(); });
  draw();
}());
"""
    return Lab(
        title="A or an, scored by the next letter and by the next sound",
        subtitle="Every a and an in three printed texts, with the word after it",
        markup=markup, controls=controls,
        panel_title=cfg.get("panel_title", "Score both rules on the same lines"),
        panel_intro=cfg.get("panel_intro",
            "Each line is an a or an from the play, the modern documents or the passage, with "
            "the word that follows it. The two rules are run on the same lines in your browser; "
            "only the question changes."),
        script=script,
        expect={"anPreset": _expect(_AN_PRESETS) if source == "all" else _AN_BY_SOURCE[source]},
    )


# ---------------------------------------------------------------- the_super

SUPERLATIVE_DATA = _data("superlative_concordance.json")

_TS_PRESETS = [
    {"id": "est", "label": "an -est adjective (eldest, greatest)",
     "expect": {"tsHit": "127 of 142", "tsPct": "89.4%", "tsOther": "15"}},
    {"id": "same", "label": "same",
     "expect": {"tsHit": "69 of 69", "tsPct": "100.0%", "tsOther": "0"}},
    {"id": "next", "label": "next",
     "expect": {"tsHit": "49 of 72", "tsPct": "68.1%", "tsOther": "23"}},
    {"id": "most", "label": "most and an adjective",
     "expect": {"tsHit": "40 of 122", "tsPct": "32.8%", "tsOther": "37", "tsA": "45"}},
]


def _the_super(cfg):
    rule = _shipped(_TS_PRESETS, cfg, "rule", "est")
    markup = (
        _kpis([("lines", "tsN", "&mdash;"), ("the or a possessive before it", "tsHit", "&mdash;"),
               ("share", "tsPct", "&mdash;"), ("the", "tsThe", "&mdash;"),
               ("a possessive", "tsPoss", "&mdash;"), ("a or an", "tsA", "&mdash;"),
               ("something else", "tsOther", "&mdash;")])
        + '<p class="small-copy" id="tsLimit"></p>'
        + _scroll_table("tsTable", "tsCols", "tsBody", 22)
    )
    controls = '<label for="tsPreset">The word</label> ' + _preset_menu("tsPreset", _TS_PRESETS, rule)
    script = (SCAN_JS + SUPER_JS + _WRITE_TILES + cfg_literal("TS_ROWS", SUPERLATIVE_DATA["rows"])
              + cfg_literal("TS_LIMIT", "The word directly before is all the scan reads: it cannot "
                            "tell a most that means very from one that means the most, except by "
                            "the a in front of it. The lines are from a novel of 1813.")) + r"""
(function () {
  var el = function (id) { return document.getElementById(id); };
  var rule = el('tsPreset').value;
  var draw = function () {
    var res = tsScore(TS_ROWS, rule), html = '', i, a;
    writeTiles(tsTiles(TS_ROWS, rule));
    el('tsLimit').textContent = TS_LIMIT;
    el('tsCols').innerHTML = '<th>the line</th><th>the word before</th><th></th>';
    for (i = 0; i < res.all.length; i++) {
      a = res.all[i];
      html += '<tr><td>' + a.row[1] + ' <strong>' + a.row[2] + '</strong> ' + a.row[3] + '</td><td>'
            + TS_LABELS[a.cls] + '</td><td>' + (a.ok ? '' : 'not the rule') + '</td></tr>';
    }
    el('tsBody').innerHTML = html;
  };
  window.redrawLab = draw;
  el('tsPreset').addEventListener('change', function () { rule = this.value; draw(); });
  draw();
}());
"""
    return Lab(
        title="What stands in front of the only one",
        subtitle="Every superlative, same, next and most in the novel, and the word before it",
        markup=markup, controls=controls,
        panel_title=cfg.get("panel_title", "Read the word before each one"),
        panel_intro=cfg.get("panel_intro",
            "Each line is taken from the novel around one word. The scan reads the word "
            "directly before it, and the rule holds when that word is the or a possessive "
            "such as her or Darcy's."),
        script=script, expect={"tsPreset": _expect(_TS_PRESETS)},
    )


# ---------------------------------------------------------------- time_preps

TIME_DATA = _data("time_concordance.json")

_TP_PRESETS = [
    {"id": "all", "label": "all three texts",
     "expect": {"tpN": "109", "tpHit": "103 of 109", "tpPct": "94.5%"}},
    {"id": "austen", "label": "the novel (1813)",
     "expect": {"tpN": "79", "tpHit": "77 of 79", "tpPct": "97.5%"}},
    {"id": "wilde", "label": "the play (1895)",
     "expect": {"tpN": "13", "tpHit": "9 of 13", "tpPct": "69.2%"}},
    {"id": "modern", "label": "the modern documents",
     "expect": {"tpN": "17", "tpHit": "17 of 17", "tpPct": "100.0%"}},
]
_TP_CODES = {"a": "the novel", "w": "the play", "m": "the modern documents"}


def _time_preps(cfg):
    source = _shipped(_TP_PRESETS, cfg, "source", "all")
    show = cfg.get("show", "lines")
    markup = (
        _kpis([("lines scored", "tpN", "&mdash;"), ("the rule is right", "tpHit", "&mdash;"),
               ("share", "tpPct", "&mdash;"), ("it misses", "tpMiss", "&mdash;"),
               ("the lines it misses", "tpFirst", "&mdash;")])
        + '<p class="small-copy" id="tpLimit"></p>'
        '<div class="table-wrap"><table id="tpKinds"><thead><tr><th>kind of time word</th>'
        '<th>the rule says</th><th>lines</th><th>right</th></tr></thead>'
        '<tbody id="tpKindBody"></tbody></table></div>'
        + _scroll_table("tpTable", "tpCols", "tpBody", 20)
    )
    controls = (
        '<label for="tpPreset">Lines from</label> ' + _preset_menu("tpPreset", _TP_PRESETS, source)
        + ' <label for="tpShow">List</label> '
        + _menu("tpShow", [("lines", "every line"), ("misses", "the lines the rule misses"),
                           ("bare", "time words with no in, on or at, not scored")], show)
    )
    script = (SCAN_JS + TIME_JS + _WRITE_TILES + cfg_literal("TP_ROWS", TIME_DATA["rows"])
              + cfg_literal("TP_BARE", TIME_DATA["bare"]) + cfg_literal("TP_CODES", _TP_CODES)
              + cfg_literal("TP_LIMIT", "Words, not meanings: a line is read only when in, on or "
                            "at comes before the time word with nothing between but words such "
                            "as the, next or a day name. May is left out, because it is also a "
                            "helping verb.")) + r"""
(function () {
  var el = function (id) { return document.getElementById(id); };
  var source = el('tpPreset').value, show = el('tpShow').value;
  var SAYS = { 'day': 'on', 'month': 'in', 'year': 'in', 'season': 'in',
               'part of the day': 'in, or on a named day', 'night, noon or midnight': 'at',
               'festival': 'at', 'clock time': 'at' };
  var draw = function () {
    var res = tpScore(TP_ROWS, source), html = '', i, a, k, want = setOf(TP_SOURCES[source]);
    writeTiles(tpTiles(TP_ROWS, source));
    el('tpLimit').textContent = TP_LIMIT;
    for (i = 0; i < TP_KINDS.length; i++) {
      k = res.byKind[TP_KINDS[i]];
      if (!k.n) continue;
      html += '<tr><td>' + TP_KINDS[i] + '</td><td>' + SAYS[TP_KINDS[i]] + '</td><td>' + k.n
            + '</td><td>' + k.hit + '</td></tr>';
    }
    el('tpKindBody').innerHTML = html;
    html = '';
    if (show === 'bare') {
      el('tpCols').innerHTML = '<th>from</th><th>the time words</th><th>times</th>';
      for (i = 0; i < TP_BARE.length; i++) {
        if (!inSet(want, TP_BARE[i][0])) continue;
        html += '<tr><td>' + TP_CODES[TP_BARE[i][0]] + '</td><td>' + TP_BARE[i][1] + '</td><td>'
              + TP_BARE[i][2] + '</td></tr>';
      }
    } else {
      el('tpCols').innerHTML = '<th>from</th><th>the line</th><th>kind</th><th>the rule says</th><th></th>';
      for (i = 0; i < res.all.length; i++) {
        a = res.all[i];
        if (show === 'misses' && a.ok) continue;
        html += '<tr><td>' + TP_CODES[a.row[0]] + '</td><td>' + a.row[4] + ' <strong>' + a.row[1]
              + (a.row[2] ? ' ' + a.row[2] : '') + ' ' + a.row[3] + '</strong> ' + a.row[5]
              + '</td><td>' + a.kind + '</td><td>' + a.says + '</td><td>' + (a.ok ? '' : 'missed')
              + '</td></tr>';
      }
    }
    el('tpBody').innerHTML = html;
  };
  window.redrawLab = draw;
  el('tpPreset').addEventListener('change', function () { source = this.value; draw(); });
  el('tpShow').addEventListener('change', function () { show = this.value; draw(); });
  draw();
}());
"""
    return Lab(
        title="In, on or at, scored on every time word in three texts",
        subtitle="The rule picks the word from the kind of time; the page checks it line by line",
        markup=markup, controls=controls,
        panel_title=cfg.get("panel_title", "Score the rule on the printed lines"),
        panel_intro=cfg.get("panel_intro",
            "Each line has in, on or at before a time word. The rule is run on the kind of "
            "time word, and the table prints every line with what the rule says and what "
            "the writer wrote."),
        script=script, expect={"tpPreset": _expect(_TP_PRESETS)},
    )


# ---------------------------------------------------------------- auxchain

LONG_PASSAGE = _data("long_passage.json")

# What each rule prints on the two modern documents, for a lesson that ships
# with the modern documents chosen; the chapter's figures are in _AX_PRESETS.
_AX_MODERN = {
    "agree": {"axHit": "14 of 14", "axPct": "100.0%", "axBroken": "0"},
    "modal": {"axHit": "16 of 17", "axPct": "94.1%", "axFormed": "0"},
    "have": {"axPerf": "16 of 23", "axPct": "69.6%", "axMain": "3 of 23"},
    "be": {"axIng": "2 of 36", "axIngPct": "5.6%", "axPP": "5 of 36"},
    "not": {"axHit": "8 of 10", "axPct": "80.0%", "axOld": "1"},
    "boxes": {"axSimple": "14 of 34, 41.2%", "axProg": "0 of 34, 0.0%", "axPerf": "3 of 34, 8.8%"},
}

_AX_PRESETS = [
    {"id": "agree", "label": "the -s belongs to he, she and it",
     "expect": {"axHit": "74 of 75", "axPct": "98.7%", "axBroken": "1"}},
    {"id": "modal", "label": "after a modal, the verb is bare",
     "expect": {"axHit": "65 of 76", "axPct": "85.5%", "axFormed": "0"}},
    {"id": "have", "label": "have: the helping verb or the main verb",
     "expect": {"axPerf": "17 of 37", "axPct": "45.9%", "axMain": "10 of 37"}},
    {"id": "be", "label": "be: what follows it",
     "expect": {"axIng": "6 of 137", "axIngPct": "4.4%", "axPP": "13 of 137"}},
    {"id": "not", "label": "not goes after the first helping verb",
     "expect": {"axHit": "29 of 39", "axPct": "74.4%", "axOld": "5"}},
    {"id": "boxes", "label": "which of the twelve boxes get used",
     "expect": {"axSimple": "55 of 216, 25.5%", "axProg": "3 of 216, 1.4%",
                "axPerf": "4 of 216, 1.9%"}},
]

# Which tiles each rule writes; the others are hidden while it is chosen.
_AX_TILES = [
    ("axN", "how many it looks at", None),
    ("axHit", "the rule holds", ("agree", "modal", "not")),
    ("axPct", "share", ("agree", "modal", "have", "not")),
    ("axPairs", "pairs the rule covers", ("agree",)),
    ("axBroken", "against the rule", ("agree",)),
    ("axBetween", "not or an adverb between", ("modal",)),
    ("axFormed", "a verb with an ending next", ("modal",)),
    ("axPerf", "perfect: have and a participle", ("have", "boxes")),
    ("axMain", "a noun phrase next: the main verb", ("have",)),
    ("axTo", "have to", ("have",)),
    ("axIng", "an -ing form next", ("be",)),
    ("axIngPct", "share", ("be",)),
    ("axPP", "a participle next", ("be",)),
    ("axAdj", "an adjective next", ("be",)),
    ("axNP", "a noun phrase next", ("be",)),
    ("axPrep", "a preposition or place word next", ("be",)),
    ("axOld", "after a main verb: the old order", ("not",)),
    ("axJoin", "after a joining word", ("not",)),
    ("axNt", "n't", ("not",)),
    ("axQ", "a pronoun next: a question", ("modal", "have", "be", "not")),
    ("axOther", "something else", ("modal", "have", "be", "not")),
    ("axSimple", "simple, present and past", ("boxes",)),
    ("axProg", "progressive, any time", ("boxes",)),
    ("axModal", "with a modal", ("boxes",)),
    ("axPassive", "be and a participle", ("boxes",)),
    ("axNone", "no verb found", ("boxes",)),
]

_AX_LIMITS = {
    "agree": "Only the word right after the pronoun is read, so it in to use it your father is read as a subject; every row is printed.",
    "modal": "The adverbs the scan steps over are a fixed list and the words the Moby list calls adverbs.",
    "have": "A noun phrase is a word such as the, a, his, or a word the Moby list calls a noun, leaving out the small words (I, by, as, all, well, better) it also lists as nouns.",
    "be": "The scan cannot tell a passive from an adjective (was pleased), and counts both as a participle.",
    "not": "The word right before not is read; the chapter is 1813 prose, which put not after a main verb.",
    "boxes": "Every pronoun is read as a subject, and the boxes are sorted from the words after it; no verb found is printed row by row.",
}


def _auxchain(cfg):
    presets = _restrict(_AX_PRESETS, cfg)
    rule = _shipped(presets, cfg, "rule", presets[0]["id"])
    source = cfg.get("source", "chapter")
    if source not in ("chapter", "modern"):
        raise ValueError("english_lab auxchain: source is chapter or modern, not %r" % source)
    show = cfg.get("show", "residue")
    shown = {p["id"] for p in presets}
    tiles = []
    for tid, label, rules in _AX_TILES:
        if rules is None or set(rules) & shown:
            tiles.append((label, tid, "&mdash;"))
    markup = (
        '<div class="kpi-grid">'
        + "".join('<div id="axK_%s" style="display:contents;"><div class="kpi"><span>%s</span>'
                  '<strong id="%s">%s</strong></div></div>'
                  % (kid, label, kid, start) for label, kid, start in tiles)
        + '</div>'
        '<p class="small-copy" id="axLimit"></p>'
        '<div class="table-wrap" id="axBoxWrap"><table><thead><tr><th>box</th><th>pronoun subjects</th>'
        '<th>share</th></tr></thead><tbody id="axBoxBody"></tbody></table></div>'
        + _scroll_table("axTable", "axCols", "axBody", 22)
        + '<details><summary>The text the figures come from</summary>'
        '<div class="mathblock" id="axText" style="font-size:0.8rem;white-space:pre-wrap;"></div></details>'
    )
    controls = (
        '<label for="axPreset">The rule</label> ' + _preset_menu("axPreset", presets, rule)
        + ' <label for="axSource">Text</label> '
        + _menu("axSource", [("chapter", "Chapter XXVI of the novel (1813)"),
                             ("modern", "the two modern documents")], source)
        + ' <label for="axShow">Show</label> '
        + _menu("axShow", [("residue", "only the rows the rule does not cover"),
                           ("all", "every row")], show)
    )
    uses = {tid: list(rules) if rules else None for tid, _l, rules in _AX_TILES}
    script = (SCAN_JS + AUX_JS + _WRITE_TILES
              + cfg_literal("AX_DATA", _payload(LONG_PASSAGE, "passage", "classes")) + cfg_literal("MODERN", MODERN_DATA)
              + cfg_literal("AX_USES", uses) + cfg_literal("AX_LIMITS", _AX_LIMITS)) + r"""
(function () {
  var el = function (id) { return document.getElementById(id); };
  var rule = el('axPreset').value, source = el('axSource').value, show = el('axShow').value;
  var text = function () {
    var out = [], d;
    if (source === 'chapter') return AX_DATA.passage;
    for (d = 0; d < MODERN.docs.length; d++) out.push(MODERN.docs[d].text);
    return out.join('\n\n');
  };
  var draw = function () {
    var t = text(), res = axRun(rule, t, AX_DATA), k, node, html = '', i, keys;
    for (k in AX_USES) {
      if (!inSet(AX_USES, k)) continue;
      node = el('axK_' + k);
      if (!node) continue;
      /* A wrapper with display: contents leaves the tile in the grid. */
      node.style.display = AX_USES[k] === null || AX_USES[k].indexOf(rule) >= 0 ? 'contents' : 'none';
      el(k).textContent = '—';
    }
    writeTiles(res.tiles);
    el('axLimit').textContent = AX_LIMITS[rule];
    el('axBoxWrap').style.display = rule === 'boxes' ? '' : 'none';
    if (res.boxes) {
      keys = Object.keys(res.boxes);
      keys.sort(function (a, b) { return res.boxes[b] - res.boxes[a] || (a < b ? -1 : 1); });
      for (i = 0; i < keys.length; i++) {
        html += '<tr><td>' + keys[i] + '</td><td>' + res.boxes[keys[i]] + '</td><td>'
              + share1(res.boxes[keys[i]], res.rows.length) + '</td></tr>';
      }
    }
    el('axBoxBody').innerHTML = html;
    html = '';
    el('axCols').innerHTML = '<th>the words</th><th>what the scan reads</th>';
    for (i = 0; i < res.rows.length; i++) {
      if (show === 'residue' && res.rows[i].hit) continue;
      html += '<tr><td>' + res.rows[i].text + '</td><td>' + res.rows[i].verdict + '</td></tr>';
    }
    el('axBody').innerHTML = html;
    el('axText').textContent = t;
  };
  window.redrawLab = draw;
  el('axPreset').addEventListener('change', function () { rule = this.value; draw(); });
  el('axSource').addEventListener('change', function () { source = this.value; draw(); });
  el('axShow').addEventListener('change', function () { show = this.value; draw(); });
  draw();
}());
"""
    return Lab(
        title="Helping verbs, counted on one chapter of a novel",
        subtitle="Every pronoun, modal, have, be and not in the chapter, and what comes next",
        markup=markup, controls=controls,
        panel_title=cfg.get("panel_title", "Score the rule on the printed chapter"),
        panel_intro=cfg.get("panel_intro",
            "The chapter is printed under the table, and the word lists the scan uses are "
            "built for its words. Choose a rule and the scan runs in your browser; switch to "
            "the modern documents to see the same rule on writing from 2025 and 2026."),
        script=script,
        expect={"axPreset": {p["id"]: dict(_AX_MODERN[p["id"]] if source == "modern" else p["expect"])
                             for p in presets}},
    )


_MODES = {"table": _table, "doubling": _doubling,
          "svo": _svo, "adverbs": _adverbs, "questions": _questions,
          "irregular": _irregular, "classes": _classes, "irrshare": _irrshare,
          "listening": _listening, "endings": _endings, "wordrule": _wordrule, "an": _an,
          "the_super": _the_super, "auxchain": _auxchain, "time_preps": _time_preps}


def english_lab(cfg):
    """The tense course's kit. `cfg["mode"]` chooses the lesson; unknown raises."""
    from . import english_b  # the second half of the kit; see its docstring

    mode = (cfg or {}).get("mode")
    build = _MODES.get(mode) or english_b.MODES.get(mode)
    if build is None:
        raise ValueError(
            "english_lab: unknown mode %r; this kit serves %s"
            % (mode, ", ".join(sorted(set(_MODES) | set(english_b.MODES))))
        )
    return build(cfg or {})


__all__ = ["english_lab", "MODES"]
