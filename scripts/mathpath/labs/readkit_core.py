"""readkit_core -- what every mode of the Reading Faster kit shares.

Specified in docs/reading/PLAN.md section D.0. readkit.py (drill, eye, flash,
scan) and readkit_b.py (triage, text, recall, log) both import from here; the
entry point readkit_lab(cfg) is readkit.py's.

JavaScript, shipped in this order on a readkit page (only what the mode needs):

  RATIONAL_JS    algebra_core's exact rationals over BigInt (reused, not copied)
  RD_CORE_JS     printing and parsing. Every printed figure goes through
                 rdFig / rdUnit / rdShare / rdSigned (section D.0's number
                 format, as implemented: see docs/reading/kit-report.md);
                 rdRead(spec, raw) parses a view's text boxes and THROWS a
                 sentence for the reader, which the wiring paints red.
  RD_TEXT_JS     the passage rules: a word, a sentence, a syllable "by the
                 rule", the first sentence of a paragraph, the phrases of a
                 phrase-marked passage. Pure; scripts/mathcheck.js runs it.
  RD_LOG_JS      the one localStorage key, "learn-reading-log", read and
                 appended inside try/catch.
  <mode>_JS      the mode's pure <xx>Compute(view, inst, opts) -> {tiles,
                 status, table?, svg?, html?} or {refuse}; scripts/mathcheck.js
                 calls it directly.
  RD_DRILL_JS    the drill engine (Start, Done, displays, questions, Score).
                 Browser only: it does nothing until a button is clicked.
  RD_WIRE_JS     the preset menu and the redraw; window.redrawLab.

NOTHING STARTS ON ITS OWN. No timer, animation or flash is created at load or
by a change/input event: every setTimeout in this kit is reached only from a
button's click handler (PLAN D.0, D.2).

Python: check_passage (the section P shape, validated at build time),
passage_counts (the same rules as RD_TEXT_JS, for bank authors), presets()
and the markup helpers, and build_lab(), which assembles one Lab.
"""

import html
import json
import re
from fractions import Fraction

from .algebra_core import RATIONAL_JS
from .capkit_core import attr, field_text as _cc_field_text, kpis_html, select_html, text_html
from .common import Lab, cfg_literal

LOG_KEY = "learn-reading-log"

# ---------------------------------------------------------------------------
# JavaScript: printing and parsing
# ---------------------------------------------------------------------------

RD_CORE_JS = r"""
  /* readkit's printing (PLAN D.0 as implemented). A figure whose exact value
     is whole prints whole, grouped by commas ("1,825,000"); one that is exact
     in at most two decimals prints exactly ("230.4", "12.75"); anything else
     prints "≈" and one decimal, rounded half away from zero ON THE RATIONAL,
     never on a float ("≈ 266.7"). */
  var RD_DASH = '—', RD_MINUS = '−';
  function rdEsc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }
  function rdClean(t) { return String(t === null || t === undefined ? '' : t).replace(/−/g, '-').trim(); }
  function rdGroup(digits) { return digits.length < 4 ? digits : digits.replace(/\B(?=(\d{3})+$)/g, ','); }
  /* |r| to exactly `places` decimals, half away from zero, integer part grouped. */
  function rdFixed(r, places) {
    var num = r.n < 0n ? -r.n : r.n, scale = 10n ** BigInt(places);
    var q = (num * scale * 2n / r.d + 1n) / 2n, s = q.toString();
    while (s.length <= places) s = '0' + s;
    var whole = rdGroup(s.slice(0, s.length - places));
    return places ? whole + '.' + s.slice(s.length - places) : whole;
  }
  function rdFig(r) {
    var neg = Rsign(r) < 0, a = Rabs(r), s, approx = false;
    if (Rint(a)) s = rdGroup(String(a.n));
    else if (Rint(Rmul(a, R(100n)))) s = rdFixed(a, 2).replace(/0$/, '');
    else { approx = true; s = rdFixed(a, 1); }
    return (approx ? '≈ ' : '') + (neg ? RD_MINUS : '') + s;
  }
  function rdUnit(r, unit) { return rdFig(r) + (unit ? ' ' + unit : ''); }
  function rdSigned(r, unit) {
    var t = rdUnit(r, unit);
    if (Rsign(r) <= 0) return t;
    return t.indexOf('≈ ') === 0 ? '≈ +' + t.slice(2) : '+' + t;
  }
  /* A share: the reduced fraction and its percentage, "4/5 = 80%",
     "7/12 ≈ 58.3%", "1 = 100%". The fraction is left out when its numerator
     or denominator runs past four digits (a measured time in ms makes them
     long): "≈ 58.3%". */
  function rdShare(r) {
    var p = Rmul(r, R(100n)), pct = rdFig(p), exact = pct.indexOf('≈') !== 0;
    var a = Rabs(r), short = String(a.n).length <= 4 && String(a.d).length <= 4;
    if (!short) return pct + '%';
    return (Rsign(r) < 0 ? RD_MINUS : '') + Rtext(a) + (exact ? ' = ' : ' ') + pct + '%';
  }
  function rdSum(v) { var s = R0; v.forEach(function (x) { s = Radd(s, x); }); return s; }
  /* The median of a list of rationals: the middle one, or the mean of the two middle ones. */
  function rdMedian(v) {
    var s = v.slice().sort(Rcmp), m = s.length >> 1;
    return s.length % 2 ? s[m] : Rdiv(Radd(s[m - 1], s[m]), R(2n));
  }
  /* words x 60 / seconds */
  function rdRate(words, seconds) { return Rdiv(Rmul(words, R(60n)), seconds); }
  /* A figure as a box holds it: a plain decimal, at most two places, no
     grouping ("251.07"), never a long fraction. rdWhole rounds to a whole number. */
  function rdDec(r) { return rdFixed(r, 2).replace(/,/g, '').replace(/\.?0+$/, ''); }
  function rdWhole(r) { return rdFixed(r, 0).replace(/,/g, ''); }
  /* The verdict on one reading above a range of n readings: with nothing
     changed, a new reading is the highest of n + 1 one time in n + 1. */
  var RD_NW = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve'];
  var RD_ORD = ['', '', '', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'];
  function rdOnce(n) {
    var m = n + 1;
    return 'above the baseline range once — ' + (m < 13 ? 'a ' + RD_ORD[m] + ' reading does this about one time in ' + RD_NW[m]
      : 'a reading after ' + n + ' baselines does this about one time in ' + m);
  }
  /* The Subject's rule needs three baselines before a range judges anything. */
  function rdNeedBase(n) { var k = 3 - n; return 'needs ' + RD_NW[k] + ' more baseline reading' + (k === 1 ? '' : 's'); }

  function rdNum(text, what) {
    var s = rdClean(text), r = s === '' ? null : Rparse(s);
    if (r === null) throw new Error(what + ' should be a number such as 3, 1/2 or 0.25, and "' + s + '" is not one');
    return r;
  }
  var RD_BAD_NAME = /[,;<>&"=\/]/;
  function rdScalar(kind, text, what, words) {
    var s = rdClean(text), r;
    if (kind === 'label' || kind === 'name') {
      if (kind === 'name' && s === '') throw new Error(what + ' is missing');
      if (RD_BAD_NAME.test(s)) throw new Error(what + ' "' + s + '" may not contain , ; / = < > & or quotes');
      return s;
    }
    if (kind === 'word') {
      if (words.indexOf(s) < 0) throw new Error(what + ' should be one of ' + words.join(', ') + ', not "' + s + '"');
      return s;
    }
    if (kind === 'opt' && s === '') return null;
    r = rdNum(s, what);
    if (kind === 'pos' && Rsign(r) <= 0) throw new Error(what + ' must be more than 0, and it is ' + rdFig(r));
    if ((kind === 'nn' || kind === 'opt') && Rsign(r) < 0) throw new Error(what + ' cannot be negative, and it is ' + rdFig(r));
    if (kind === 'share' && (Rsign(r) < 0 || Rcmp(r, R1) > 0)) throw new Error(what + ' is a share from 0 to 1, and it is ' + rdFig(r));
    if (kind === 'count' && (!Rint(r) || Rsign(r) <= 0)) throw new Error(what + ' must be a whole number of at least 1, not ' + rdFig(r));
    if (kind === 'nncount' && (!Rint(r) || Rsign(r) < 0)) throw new Error(what + ' must be a whole number, 0 or more, not ' + rdFig(r));
    return r;
  }
  function rdField(f, text) {
    if (f.kind === 'rec') return rdRecords(text, f);
    if (f.kind === 'nums') return rdNumbers(text, f);
    if (f.kind === 'entries') return rdEntries(text, f);
    if (f.kind === 'strings') return rdStrings(text, f);
    return rdScalar(f.kind, text, f.what, f.words);
  }
  function rdRead(spec, raw) {
    var out = {};
    spec.forEach(function (f) { out[f.key] = rdField(f, raw[f.key]); });
    return out;
  }
  function rdSet(id, text) { var el = document.getElementById(id); if (el) el.textContent = text; }
  function rdRefuse(statusEl, ids, why) {
    ids.forEach(function (id) { rdSet(id, RD_DASH); });
    statusEl.innerHTML = '<span class="tone-red">' + rdEsc(String(why).replace(/\.$/, '')) + '.</span>';
  }
  function rdTable(caption, head, rows) {
    var h = '<caption>' + rdEsc(caption) + '</caption><thead><tr>'
      + head.map(function (x) { return '<th>' + rdEsc(x) + '</th>'; }).join('') + '</tr></thead><tbody>';
    rows.forEach(function (row) { h += '<tr>' + row.map(function (c) { return '<td>' + rdEsc(c) + '</td>'; }).join('') + '</tr>'; });
    return h + '</tbody>';
  }
"""

RD_LIST_JS = r"""
  /* The list-valued inputs (records, numbers, sessions, letter strings):
     shipped only on a page with such an input. */
  function rdLimit(n, f) {
    if (n < f.lo) throw new Error(f.what + (n === 0 ? ' is empty' : ': this lab needs at least ' + f.lo + ', and there ' + (n === 1 ? 'is 1' : 'are ' + n)));
    if (n > f.hi) throw new Error(f.what + ': this lab takes at most ' + f.hi + ', and there are ' + n);
  }
  function rdSplit(s, sep) {
    var rows = s === '' ? [] : s.split(sep).map(function (x) { return x.trim(); });
    if (rows.length && rows[rows.length - 1] === '') rows.pop();
    return rows;
  }
  /* "a, 1, 2; b, 3, 4" with f.sub = [[key, kind, words?], ...] */
  function rdRecords(text, f) {
    var rows = rdSplit(rdClean(text), ';');
    rdLimit(rows.length, f);
    return rows.map(function (row, i) {
      var cells = row.split(',').map(function (c) { return c.trim(); });
      if (cells.length !== f.sub.length) {
        throw new Error('Entry ' + (i + 1) + ' of ' + f.what + ' has ' + cells.length + ' part' + (cells.length === 1 ? '' : 's')
          + '; each needs ' + f.sub.length + ': ' + f.sub.map(function (k) { return k[0]; }).join(', '));
      }
      var rec = {};
      f.sub.forEach(function (k, j) { rec[k[0]] = rdScalar(k[1], cells[j], 'The ' + k[0] + ' in entry ' + (i + 1) + ' of ' + f.what, k[2]); });
      return rec;
    });
  }
  /* "238, 251, 245": numbers of kind f.each */
  function rdNumbers(text, f) {
    var parts = rdSplit(rdClean(text), /[\s,;]+/);
    rdLimit(parts.length, f);
    return parts.map(function (t, i) { return rdScalar(f.each, t, 'Entry ' + (i + 1) + ' of ' + f.what); });
  }
  /* "240/5/5, 238/4/5": a log's sessions as rate/correct/total */
  function rdEntries(text, f) {
    var parts = rdSplit(rdClean(text), /[\s,;]+/);
    rdLimit(parts.length, f);
    return parts.map(function (t, i) {
      /* Split from the right: an older log wrote the rate as a fraction
         ("1964000/7823/5/6"), and the rate is everything before the last two parts. */
      var c = t.split('/'), where = 'Session ' + (i + 1) + ' of ' + f.what;
      if (c.length < 3 || c.length > 4) throw new Error(where + ' should be rate/correct/total, such as 240/4/5, not "' + t + '"');
      var e = { wpm: rdScalar('pos', c.slice(0, -2).join('/'), where + ': the rate'), correct: rdScalar('nncount', c[c.length - 2], where + ': correct'),
                total: rdScalar('count', c[c.length - 1], where + ': questions') };
      if (Rcmp(e.correct, e.total) > 0) throw new Error(where + ' has more right (' + rdFig(e.correct) + ') than asked (' + rdFig(e.total) + ')');
      return e;
    });
  }
  /* "ABCDEFGHI; KLMNOPQRS": strings of letters; f.blank allows - ? _ for a letter not seen */
  function rdStrings(text, f) {
    var parts = rdSplit(rdClean(text), ';'), ok = f.blank ? /^[A-Za-z?_.\-]*$/ : /^[A-Za-z]+$/;
    rdLimit(parts.length, f);
    return parts.map(function (t, i) {
      if (!ok.test(t)) throw new Error('Entry ' + (i + 1) + ' of ' + f.what + ' should be letters only' + (f.blank ? ' (- for a letter asked and not seen, . for a position not asked)' : '') + ', not "' + t + '"');
      return t.toUpperCase();
    });
  }
"""

RD_TEXT_JS = r"""
  /* The passage rules (PLAN section P and D.1 text). A WORD is a
     whitespace-separated token containing a letter or a digit; "|" (a phrase
     mark) and "## " (a heading mark) are markup, never text. A SENTENCE ends
     at . ! or ? (a run of them), optionally followed by closing quotes or
     brackets, then whitespace or the end of the paragraph. SYLLABLES "by the
     rule": vowel groups (a e i o u y) in the word's letters, minus one for a
     final e that is not "le", at least 1 per word. */
  function rdHeading(p) { return /^## /.test(p); }
  function rdPlain(p) { return String(p).replace(/^## /, '').replace(/\|/g, ' ').replace(/\s+/g, ' ').trim(); }
  function rdTokens(p) { var s = rdPlain(p); return s === '' ? [] : s.split(' '); }
  function rdIsWord(t) { return /[A-Za-z0-9À-ɏ]/.test(t); }
  function rdWordCount(p) { return rdTokens(p).filter(rdIsWord).length; }
  function rdSentenceCount(p) { return (rdPlain(p).match(/[.!?]+["'”’)\]]*(?=\s|$)/g) || []).length; }
  function rdSyllables(word) {
    var w = String(word).toLowerCase().replace(/[^a-z]/g, '');
    if (w === '') return 1;
    var n = (w.match(/[aeiouy]+/g) || []).length;
    if (/e$/.test(w) && !/le$/.test(w)) n -= 1;
    return n < 1 ? 1 : n;
  }
  /* Every paragraph, headings included. */
  function rdPassageWords(P) { var n = 0; P.paragraphs.forEach(function (p) { n += rdWordCount(p); }); return n; }
  /* Characters: the passage's text with its markup removed and every run of
     whitespace, paragraph breaks included, counted as one space. */
  function rdPassageChars(P) { return Array.from(P.paragraphs.map(rdPlain).join(' ')).length; }
  /* The readability counts: body paragraphs only (headings are not prose). */
  function rdCounts(P) {
    var words = 0, sentences = 0, syllables = 0;
    P.paragraphs.forEach(function (p) {
      if (rdHeading(p)) return;
      var w = rdTokens(p).filter(rdIsWord);
      words += w.length; sentences += rdSentenceCount(p);
      w.forEach(function (t) { syllables += rdSyllables(t); });
    });
    return { words: words, sentences: sentences, syllables: syllables };
  }
  /* The first sentence of a paragraph (the whole paragraph if it has no end). */
  function rdFirstSentence(p) {
    var s = rdPlain(p), m = /[.!?]+["'”’)\]]*(?=\s|$)/.exec(s);
    return m ? s.slice(0, m.index + m[0].length) : s;
  }
  /* What the gist display shows: headings and the first sentence of each body paragraph. */
  function rdGistParas(P) {
    return P.paragraphs.map(function (p) { return rdHeading(p) ? p : rdFirstSentence(p); });
  }
  /* What the preview shows: headings, the first and the last body paragraph. */
  function rdPreviewParas(P) {
    var body = [], out = [];
    P.paragraphs.forEach(function (p, i) { if (!rdHeading(p)) body.push(i); });
    P.paragraphs.forEach(function (p, i) {
      if (rdHeading(p) || i === body[0] || i === body[body.length - 1]) out.push(p);
    });
    return out;
  }
  /* A phrase-marked passage's phrases: "|" and paragraph ends are boundaries. */
  function rdPhrases(P) {
    var out = [];
    P.paragraphs.forEach(function (p) {
      String(p).replace(/^## /, '').split('|').forEach(function (ph) {
        var t = ph.replace(/\s+/g, ' ').trim();
        if (t !== '' && rdWordCount(t) > 0) out.push(t);
      });
    });
    return out;
  }
  function rdWordsIn(paras) { var n = 0; paras.forEach(function (p) { n += rdWordCount(p); }); return n; }
"""

RD_LOG_JS = r"""
  /* The log: ONE localStorage key shared by every lesson of the Subject.
     Nothing leaves the browser. Storage that is blocked or full is said once,
     and every drill still runs. */
  var RD_LOG_KEY = 'learn-reading-log', rdLogWarned = false;
  function rdLogRead() {
    try {
      var raw = window.localStorage.getItem(RD_LOG_KEY), v = raw ? JSON.parse(raw) : [];
      return Array.isArray(v) ? v.filter(function (e) { return e && typeof e === 'object'; }) : [];
    } catch (err) { return []; }
  }
  function rdLogWrite(list) {
    try { window.localStorage.setItem(RD_LOG_KEY, JSON.stringify(list)); return true; } catch (err) { return false; }
  }
  /* Append one entry; false (and a single notice) when storage is unavailable. */
  function rdLogAppend(entry, noticeEl) {
    var list = rdLogRead();
    entry.v = 1;
    entry.at = new Date().toISOString();
    if (!entry.lesson) entry.lesson = LESSON || String((window.location && window.location.pathname) || '').split('/').filter(Boolean).pop() || '';
    list.push(entry);
    if (rdLogWrite(list)) return true;
    if (!rdLogWarned && noticeEl) {
      rdLogWarned = true;
      noticeEl.textContent = 'This browser is not keeping data for this page, so your results will not be kept. Every drill still runs.';
    }
    return false;
  }
  /* Readings the verdicts may use: timed readings of a passage (a drill or a
     warm-up), not a skim. rate = words x 60,000 / ms, exact; eff: x right / asked. */
  function rdIsReading(e) { return (e.mode === 'drill' || e.mode === 'warmup') && e.display !== 'gist' && e.words > 0 && e.ms > 0; }
  /* Baselines and tests compare only on standard text: an entry logged with a
     passage band counts only when the band is "standard"; one without a band
     (a log from before bands were recorded, or your own pasted text) counts. */
  function rdStdBand(b) { return !b || b === 'standard'; }
  function rdStandard(e) { return rdStdBand(e.band); }
  function rdEntryRate(e, eff) {
    var r = R(BigInt(Math.round(e.words)) * 60000n, BigInt(Math.round(e.ms)));
    return eff ? Rmul(r, R(BigInt(e.correct), BigInt(e.total))) : r;
  }
  /* The rates of every reading of one kind on standard text, in log order (eff: with questions, effective). */
  function rdKindRates(kind, eff, list) {
    return (list || rdLogRead()).filter(function (e) { return e.kind === kind && rdIsReading(e) && rdStandard(e) && (!eff || e.total > 0); })
      .map(function (e) { return rdEntryRate(e, eff); });
  }
  /* A delayed test that has fallen due is offered on EVERY readkit page: a
     link to the lesson that set it (its path, as logged). Reading the log at
     load starts nothing; it only fills this line. */
  function rdDueEntries(list) {
    var now = Date.now();
    return list.filter(function (e) {
      return e.due && Date.parse(e.due) <= now && !list.some(function (x) {
        return x.view === 'delayed-test' && x.lesson === e.lesson && x.at > e.at;
      });
    });
  }
  function rdDueBanner() {
    var el = document.getElementById('rdDue');
    if (!el) return;
    var here = String((window.location && window.location.pathname) || ''), seen = {}, links = [];
    rdDueEntries(rdLogRead()).forEach(function (e) {
      var u = String(e.url || '');
      if (!/^\/[a-z0-9\-\/]*$/.test(u) || u === here || seen[u]) return;
      seen[u] = true;
      links.push('<a href="' + rdEsc(u) + '">' + (e.title ? 'the test on “' + rdEsc(e.title) + '”' : rdEsc(e.lesson || u)) + '</a>');
    });
    if (links.length) {
      el.innerHTML = 'A delayed test is due: open ' + links.join(', ') + ' to take it.';
      el.style.display = '';
    }
    return links.length;
  }
"""

# %(p)s: the mode's prefix; %(fn)s: its pure function.
RD_WIRE_JS = r"""
  var presetS = document.getElementById('%(p)sPreset');
  var statusEl = document.getElementById('%(p)sStatus');
  var tableEl = document.getElementById('%(p)sTable');
  var extraEl = document.getElementById('%(p)sExtra');
  function field(id) { return document.getElementById(id); }
  function rdClear() { tableEl.innerHTML = ''; if (extraEl) extraEl.innerHTML = ''; }
  function redraw() {
    var raw = {}, inst;
    SPEC.forEach(function (f) { raw[f.key] = field(f.id).value; });
    try { inst = rdRead(SPEC, raw); } catch (err) { rdClear(); rdRefuse(statusEl, TILES, err.message); return; }
    var out = %(fn)s(VIEW, inst, OPTS);
    if (out.refuse) { rdClear(); rdRefuse(statusEl, TILES, out.refuse); return; }
    TILES.forEach(function (id) { rdSet(id, out.tiles[id] === undefined ? RD_DASH : out.tiles[id]); });
    tableEl.innerHTML = out.table ? rdTable(out.table.caption, out.table.head, out.table.rows) : '';
    if (extraEl) extraEl.innerHTML = (out.svg || '') + (out.html || '');
    statusEl.innerHTML = rdEsc(out.status);
  }
  /* Write a set of values into the text boxes (a preset, or a drill's
     measurement) and redraw: one computation for both sources. */
  function rdWrite(values) {
    SPEC.forEach(function (f) { if (values[f.key] !== undefined) field(f.id).value = String(values[f.key]); });
    redraw();
  }
  presetS.addEventListener('change', function () {
    var inst = PRESETS[presetS.value];
    if (!inst) return;
    if (typeof rdFill === 'function') inst = rdFill(inst);
    rdWrite(inst);
  });
  SPEC.forEach(function (f) { field(f.id).addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
  /* A due delayed test takes the warm-up's place. */
  if (rdDueBanner()) { var rdWarmBox = document.getElementById('rdBoxW'); if (rdWarmBox) rdWarmBox.style.display = 'none'; }
"""

# ---------------------------------------------------------------------------
# Python: the passage rules, mirrored for bank authors and build-time checks
# ---------------------------------------------------------------------------

_WORDCHAR = re.compile(r"[A-Za-z0-9À-ɏ]")
_SENT_END = re.compile(r"[.!?]+[\"'”’)\]]*(?=\s|$)")


def plain(p):
    return re.sub(r"\s+", " ", re.sub(r"^## ", "", p).replace("|", " ")).strip()


def tokens(p):
    s = plain(p)
    return s.split(" ") if s else []


def word_count(p):
    return sum(1 for t in tokens(p) if _WORDCHAR.search(t))


def syllables(word):
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 1
    n = len(re.findall(r"[aeiouy]+", w))
    if w.endswith("e") and not w.endswith("le"):
        n -= 1
    return max(1, n)


def passage_counts(p):
    """The figures the kit computes for a passage, by the same rules as RD_TEXT_JS.

    {words (every paragraph), chars, body_words, sentences, syllables, fre,
    grade} -- fre and grade are Fractions. For bank authors checking a band.
    """
    words = sum(word_count(x) for x in p["paragraphs"])
    chars = len(" ".join(plain(x) for x in p["paragraphs"]))
    bw = bs = by = 0
    for x in p["paragraphs"]:
        if x.startswith("## "):
            continue
        ws = [t for t in tokens(x) if _WORDCHAR.search(t)]
        bw += len(ws)
        bs += len(_SENT_END.findall(plain(x)))
        by += sum(syllables(t) for t in ws)
    out = {"words": words, "chars": chars, "body_words": bw, "sentences": bs, "syllables": by}
    if bw and bs:
        out["fre"] = Fraction("206.835") - Fraction("1.015") * Fraction(bw, bs) - Fraction("84.6") * Fraction(by, bw)
        out["grade"] = Fraction("0.39") * Fraction(bw, bs) + Fraction("11.8") * Fraction(by, bw) - Fraction("15.59")
    return out


def word_count_passage(p):
    return sum(word_count(x) for x in p["paragraphs"])


def first_sentence(p):
    s = plain(p)
    m = _SENT_END.search(s)
    return s[:m.end()] if m else s


def gist_words(p):
    """Words the gist display shows: headings and each body paragraph's first sentence."""
    return sum(word_count(x if x.startswith("## ") else first_sentence(x)) for x in p["paragraphs"])


def phrase_count(p):
    n = 0
    for x in p["paragraphs"]:
        for ph in re.sub(r"^## ", "", x).split("|"):
            if word_count(ph):
                n += 1
    return n


PASSAGE_KEYS = {"id", "title", "band", "kind", "paragraphs", "phrases", "questions", "ideas", "sections", "targets"}
BANDS = ("easy", "standard", "hard", "mixed")
KINDS = ("narrative", "expository", "procedural", "argument", "document")


def check_passage(where, p):
    """Validate one passage dict (PLAN section P plus "id"); raise ValueError naming it."""
    if not isinstance(p, dict):
        raise ValueError("%s: a passage must be a dict from the bank, not %r" % (where, type(p).__name__))
    pid = p.get("id")
    if not isinstance(pid, str) or not re.fullmatch(r"[A-Z][A-Z0-9]{1,5}", pid):
        raise ValueError("%s: a passage needs an \"id\" such as \"P01\" (the bank's key), not %r" % (where, pid))
    where = "%s passage %s" % (where, pid)
    extra = sorted(set(p) - PASSAGE_KEYS)
    if extra:
        raise ValueError("%s: unknown key(s) %s; a passage has only %s" % (where, ", ".join(extra), ", ".join(sorted(PASSAGE_KEYS))))
    if not isinstance(p.get("title"), str) or not p["title"].strip():
        raise ValueError("%s: needs a plain-text \"title\"" % where)
    if "band" in p and p["band"] not in BANDS:
        raise ValueError("%s: band %r is not one of %s" % (where, p["band"], ", ".join(BANDS)))
    if "kind" in p and p["kind"] not in KINDS:
        raise ValueError("%s: kind %r is not one of %s" % (where, p["kind"], ", ".join(KINDS)))
    paras = p.get("paragraphs")
    if not isinstance(paras, list) or not paras or not all(isinstance(x, str) and x.strip() for x in paras):
        raise ValueError("%s: \"paragraphs\" must be a non-empty list of non-empty strings" % where)
    if not any(word_count(x) for x in paras):
        raise ValueError("%s: has no words" % where)
    if any(x.startswith("## ") and "|" in x for x in paras):
        raise ValueError("%s: a heading may not carry phrase marks" % where)
    phr = p.get("phrases", False)
    if not isinstance(phr, bool):
        raise ValueError("%s: \"phrases\" is True or False" % where)
    marked = any("|" in x for x in paras)
    if phr and not marked:
        raise ValueError("%s: \"phrases\" is True but no paragraph carries a | mark" % where)
    if marked and not phr:
        raise ValueError("%s: a paragraph carries a | mark but \"phrases\" is not True, so the mark would be read as text" % where)
    qs = p.get("questions")
    if qs is not None:
        if not isinstance(qs, list) or not 4 <= len(qs) <= 6:
            raise ValueError("%s: \"questions\" must be a list of 4 to 6 (the bank gives six: three gist, three detail)" % where)
        for i, q in enumerate(qs):
            w = "%s question %d" % (where, i + 1)
            if not isinstance(q, dict) or set(q) - {"q", "a", "c", "kind"}:
                raise ValueError("%s: must be {q, a, c, kind}" % w)
            if not isinstance(q.get("q"), str) or not q["q"].strip():
                raise ValueError("%s: needs a question \"q\"" % w)
            a = q.get("a")
            if not isinstance(a, list) or len(a) != 4 or not all(isinstance(x, str) and x.strip() for x in a) or len(set(a)) != 4:
                raise ValueError("%s: \"a\" must be four distinct non-empty options" % w)
            if isinstance(q.get("c"), bool) or q.get("c") not in (0, 1, 2, 3):
                raise ValueError("%s: \"c\" must be the index 0-3 of the right option" % w)
            if q.get("kind") not in ("gist", "detail"):
                raise ValueError("%s: \"kind\" must be \"gist\" or \"detail\"" % w)
    ideas = p.get("ideas")
    if ideas is not None:
        if not isinstance(ideas, list) or not 8 <= len(ideas) <= 14 or not all(isinstance(x, str) and x.strip() for x in ideas):
            raise ValueError("%s: \"ideas\" must be 8 to 14 idea units, each a non-empty string" % where)
    if "sections" in p:
        section_starts(where, p)
    if "targets" in p:
        resolve_targets(where, p, p["targets"])
    return p


def section_starts(where, p):
    """[0, j]: the paragraph indices where the two sections start. Accepts j, [j] or [0, j]."""
    s = p.get("sections")
    if isinstance(s, int) and not isinstance(s, bool):
        s = [0, s]
    elif isinstance(s, list) and len(s) == 1:
        s = [0] + s
    n = len(p["paragraphs"])
    if (not isinstance(s, list) or len(s) != 2 or not all(isinstance(x, int) and not isinstance(x, bool) for x in s)
            or s[0] != 0 or not 0 < s[1] < n):
        raise ValueError("%s: \"sections\" must be [0, j] with 0 < j < %d (the paragraph where section 2 starts)" % (where, n))
    return s


def _norm(t):
    return re.sub(r"^[^\w]+|[^\w]+$", "", t.lower())


def all_tokens(p):
    """Every whitespace token of the passage in order (headings included), as the drill wraps them."""
    out = []
    for x in p["paragraphs"]:
        out.extend(tokens(x))
    return out


def resolve_targets(where, p, targets):
    """Scan targets -> [{q, at: [i, j]}] over all_tokens(p) (0-based, inclusive).

    A target is {q, answer, nth (1-based, default 1)} -- the answer is one or
    more words, matched case- and punctuation-insensitively -- or {q, at: [i, j]}.
    """
    toks = [_norm(t) for t in all_tokens(p)]
    if not isinstance(targets, list) or not 1 <= len(targets) <= 10:
        raise ValueError("%s: scan targets must be a list of 1 to 10" % where)
    out = []
    for k, t in enumerate(targets):
        w = "%s target %d" % (where, k + 1)
        if not isinstance(t, dict) or not isinstance(t.get("q"), str) or not t["q"].strip():
            raise ValueError("%s: needs a prompt \"q\"" % w)
        if set(t) - {"q", "answer", "nth", "at"}:
            raise ValueError("%s: only q, answer, nth or at" % w)
        if "at" in t:
            at = t["at"]
            if (not isinstance(at, list) or len(at) != 2 or not all(isinstance(x, int) for x in at)
                    or not 0 <= at[0] <= at[1] < len(toks)):
                raise ValueError("%s: \"at\" must be [i, j] word-token indices within 0..%d" % (w, len(toks) - 1))
            out.append({"q": t["q"], "at": list(at)})
            continue
        ans = [_norm(x) for x in str(t.get("answer", "")).split()]
        if not ans or not all(ans):
            raise ValueError("%s: needs an \"answer\" (the words to click) or \"at\"" % w)
        nth = t.get("nth", 1)
        hits = [i for i in range(len(toks) - len(ans) + 1) if toks[i:i + len(ans)] == ans]
        if not isinstance(nth, int) or isinstance(nth, bool) or not 1 <= nth <= len(hits):
            raise ValueError("%s: the answer %r occurs %d time(s) in the passage; nth %r is not one of them"
                             % (w, t.get("answer"), len(hits), nth))
        i = hits[nth - 1]
        out.append({"q": t["q"], "at": [i, i + len(ans) - 1]})
    return out


def passages_of(cfg, kit, n=None, need=()):
    """The passage dicts a cfg carries: cfg["passage"] (one) or cfg["passages"] (a list), validated.

    n: the number required (None: any, 0: none allowed). need: keys each must have.
    """
    if "passage" in cfg and "passages" in cfg:
        raise ValueError("%s: give cfg[\"passage\"] or cfg[\"passages\"], not both" % kit)
    if "passage" in cfg:
        plist = [cfg["passage"]]
    elif "passages" in cfg:
        plist = cfg["passages"]
        if not isinstance(plist, list) or not plist:
            raise ValueError("%s: cfg[\"passages\"] must be a non-empty list of passage dicts" % kit)
    else:
        plist = []
    if n is not None and len(plist) != n:
        raise ValueError("%s: this view takes %s, and the cfg gives %d"
                         % (kit, "no passage" if n == 0 else "%d passage%s" % (n, "" if n == 1 else "s"), len(plist)))
    seen = set()
    for p in plist:
        check_passage(kit, p)
        for key in need:
            if not p.get(key):
                raise ValueError("%s passage %s: this view needs its %r" % (kit, p["id"], key))
        if p["id"] in seen:
            raise ValueError("%s: passage %s is given twice" % (kit, p["id"]))
        seen.add(p["id"])
    return plist


def embed(plist, keep=("id", "title", "paragraphs", "questions", "ideas")):
    """The passages as the page ships them: only what a drill shows or scores."""
    return {p["id"]: {k: p[k] for k in keep if k in p} for p in plist}


# ---------------------------------------------------------------------------
# Python: fields, presets, markup
# ---------------------------------------------------------------------------

_LETTERS = re.compile(r"^[A-Za-z]+$")
_TYPED = re.compile(r"[A-Za-z?_.\-]*")


def _unfloat(v):
    """A float in a preset (110.5) is taken as the decimal it prints as ("110.5")."""
    if isinstance(v, float):
        return repr(v)
    if isinstance(v, (list, tuple)):
        return type(v)(_unfloat(x) for x in v)
    if isinstance(v, dict):
        return {k: _unfloat(x) for k, x in v.items()}
    return v


def field_text(where, key, kind, value):
    """A preset's value for one field -> the exact text the box holds. A float
    is read as the decimal it prints as, so seconds may be 110.5 or "110.5"."""
    value = _unfloat(value)
    if isinstance(kind, tuple) and kind[0] == "entries":
        _, lo, hi = kind
        if not isinstance(value, (list, tuple)) or not lo <= len(value) <= hi:
            raise ValueError("%s: %s should be a list of %d to %d (rate, correct, total) triples" % (where, key, lo, hi))
        cells = []
        for i, e in enumerate(value):
            if not isinstance(e, (list, tuple)) or len(e) != 3:
                raise ValueError("%s: session %d of %s should be (rate, correct, total)" % (where, i + 1, key))
            r = _cc_field_text(where, key, "pos", e[0])
            c = _cc_field_text(where, key, "nncount", e[1])
            t = _cc_field_text(where, key, "count", e[2])
            if int(c) > int(t):
                raise ValueError("%s: session %d of %s has more right than asked" % (where, i + 1, key))
            cells.append("%s/%s/%s" % (r, c, t))
        return ", ".join(cells)
    if isinstance(kind, tuple) and kind[0] == "strings":
        _, lo, hi, blank = kind
        if not isinstance(value, (list, tuple)) or not lo <= len(value) <= hi:
            raise ValueError("%s: %s should be a list of %d to %d strings" % (where, key, lo, hi))
        pat = _TYPED if blank else _LETTERS
        for s in value:
            if not isinstance(s, str) or not pat.fullmatch(s):
                raise ValueError("%s: %s entry %r should be letters only%s" % (where, key, s, " (or - and .)" if blank else ""))
        return "; ".join(s.upper() for s in value)
    return _cc_field_text(where, key, kind, value)


def js_kind(key, label, kind):
    spec = {"key": key, "what": label}
    if isinstance(kind, tuple) and kind[0] == "word":
        spec.update(kind="word", words=list(kind[1]))
    elif isinstance(kind, tuple) and kind[0] == "rec":
        _, sub, lo, hi, _unique = kind
        spec.update(kind="rec", lo=lo, hi=hi,
                    sub=[[k, kk[0], list(kk[1])] if isinstance(kk, tuple) else [k, kk] for k, kk in sub])
    elif isinstance(kind, tuple) and kind[0] == "nums":
        spec.update(kind="nums", each=kind[1], lo=kind[2], hi=kind[3])
    elif isinstance(kind, tuple) and kind[0] == "entries":
        spec.update(kind="entries", lo=kind[1], hi=kind[2])
    elif isinstance(kind, tuple) and kind[0] == "strings":
        spec.update(kind="strings", lo=kind[1], hi=kind[2], blank=bool(kind[3]))
    else:
        spec["kind"] = kind
    return spec


def presets(cfg, kit, fields, extra_keys=(), check=None):
    """(instance table, menu, expect by id, chosen id).

    fields: [(key, label, kind, default)]. A preset key that is neither a field
    of this view nor id/label/note/expect (nor one of extra_keys) raises.
    """
    plist = cfg.get("presets")
    if not isinstance(plist, list) or not plist:
        raise ValueError("%s: cfg['presets'] must be a non-empty list of instances" % kit)
    known = {f[0] for f in fields} | {"id", "label", "note", "expect"} | set(extra_keys)
    table, menu, expect = {}, [], {}
    for p in plist:
        pid = p.get("id") if isinstance(p, dict) else None
        if not isinstance(pid, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", pid):
            raise ValueError("%s: every preset needs an id of lowercase letters, digits and hyphens, not %r" % (kit, pid))
        where = "%s preset %r" % (kit, pid)
        if pid in table:
            raise ValueError("%s: the id is used twice" % where)
        label = p.get("label")
        if not isinstance(label, str) or not label.strip() or "<" in label:
            raise ValueError("%s: needs a plain-text label" % where)
        extra = sorted(set(p) - known)
        if extra:
            raise ValueError("%s: %s %s not an input of this view (it shows %s)"
                             % (where, ", ".join(extra), "is" if len(extra) == 1 else "are",
                                ", ".join(f[0] for f in fields)))
        if not isinstance(p.get("expect", {}), dict):
            raise ValueError("%s: expect must be {tile id: text}" % where)
        inst = {}
        for key, _label, kind, default in fields:
            value = p.get(key, default)
            if value is None:
                raise ValueError("%s: needs %s" % (where, key))
            inst[key] = field_text(where, key, kind, value)
        for key in extra_keys:
            if key in p:
                inst["__" + key] = p[key]
        if check is not None:
            check(where, p, inst)
        table[pid] = inst
        menu.append((pid, label))
        expect[pid] = dict(p.get("expect") or {})
    chosen = cfg.get("preset", plist[0]["id"])
    if chosen not in table:
        raise ValueError("%s: cfg['preset'] %r is not one of the presets (%s)" % (kit, chosen, ", ".join(table)))
    return table, menu, expect, chosen


def camel(prefix, key):
    """An input's id: prefix + 'In' + Key ('dr', 'wordsA' -> 'drInWordsA')."""
    return prefix + "In" + "".join(part[:1].upper() + part[1:] for part in key.split("_"))


def esc(text):
    return html.escape(str(text), quote=False)


def btn(cid, text, primary=False, hidden=False):
    return ('<button class="btn small%s" type="button" id="%s"%s>%s</button>'
            % (" primary" if primary else "", cid, ' style="display:none"' if hidden else "", esc(text)))


PHOTO_NOTE = ("Flashed and streamed displays are not suitable for readers with photosensitive conditions; "
              "skip this drill if that applies to you, and the rest of the lesson stands without it.")


def slot_html(key, heading, intro, extra_buttons=""):
    """One drill's controls and stage. Ids end in the slot key ('' 'A' 'B' '1'...)."""
    k = key
    return (
        '      <div class="card card-pad" id="rdBox%s" style="margin-top:12px;">\n'
        '        <h4 style="margin:0 0 4px;">%s</h4>\n'
        '        <p class="small-copy" id="rdMsg%s" style="margin:0 0 8px;" aria-live="polite">%s</p>\n'
        '        <div style="display:flex;flex-wrap:wrap;gap:8px;">%s %s %s %s</div>\n'
        '        <div id="rdText%s" class="prose" style="display:none;margin-top:12px;overflow-wrap:anywhere;"></div>\n'
        '        <div id="rdWork%s" style="display:none;margin-top:12px;"></div>\n'
        '        <div id="rdOut%s" class="small-copy" style="margin-top:8px;"></div>\n'
        '      </div>\n'
        % (k, esc(heading), k, esc(intro), btn("rdStart" + k, "Start", primary=True),
           btn("rdDone" + k, "Done", hidden=True), extra_buttons, btn("rdReset" + k, "Reset"), k, k, k))


def build_lab(cfg, *, kit, prefix, view, fields, tiles, fn, js, opts, title, subtitle,
              panel_title, panel_intro, main_html="", passages=None, slots=None, ui_js="",
              extra_keys=(), check=None, needs_log=False, needs_text=False, table=True, intro_tail="", lists=False):
    """Assemble one Lab: the preset menu, the text inputs, the tiles, the
    status banner, the drill slots (if any), and the script.

    js: the mode's pure block(s); ui_js: browser-only code that runs after the
    wiring (it may use redraw, rdWrite, field). slots: {key: slot config} for
    RD_DRILL_JS; when given, the drill engine and the log ship. intro_tail: a
    sentence the panel intro always ends with, even when the cfg gives its own
    intro (unless that intro already carries it).
    """
    tbl, menu, expect, chosen = presets(cfg, kit, fields, extra_keys, check)
    here = tbl[chosen]
    spec = []
    controls = select_html(prefix + "Preset", "Worked example", menu, chosen)
    for key, label, kind, _default in fields:
        cid = camel(prefix, key)
        s = js_kind(key, label, kind)
        s["id"] = cid
        spec.append(s)
        controls += text_html(cid, label, here.get(key, ""))
    controls += kpis_html(tiles)
    ids = [s["id"] for s in spec] + [cid for _l, cid in tiles]
    if len(set(ids)) != len(ids):
        raise ValueError("%s: two controls or tiles share an id: %s" % (kit, sorted(i for i in ids if ids.count(i) > 1)))
    passages = list(passages or [])
    slots = dict(slots or {})
    if "warmup" in cfg:
        wl = cfg["warmup"] if isinstance(cfg["warmup"], list) else [cfg["warmup"]]
        if not wl:
            raise ValueError("%s: cfg[\"warmup\"] is a passage dict or a non-empty list of them" % kit)
        wk = cfg.get("warmup_kind")
        wks = wk if isinstance(wk, list) else [wk] * len(wl)
        if len(wks) != len(wl):
            raise ValueError("%s: cfg[\"warmup_kind\"] is one kind or one per warm-up passage" % kit)
        wks = [log_kind(kit + " warm-up", k, "practice") for k in wks]
        wkind = wks[0]
        for wp in wl:
            check_passage(kit + " warm-up", wp)
            if not wp.get("questions"):
                raise ValueError("%s: the warm-up passage %s has no questions" % (kit, wp["id"]))
            if any(p["id"] == wp["id"] for p in passages):
                raise ValueError("%s: the warm-up passage %s is also this view's passage" % (kit, wp["id"]))
        if len({wp["id"] for wp in wl}) != len(wl):
            raise ValueError("%s: a warm-up passage is listed twice" % kit)
        passages += wl
        said = wkind if len(set(wks)) == 1 else ", then ".join("%s (%s)" % (k, wp["title"]) for k, wp in zip(wks, wl))
        slots["W"] = slot("W", wl[0], intro="A warm-up: a timed reading at your usual pace, then its questions. It is "
                          "logged as %s and fills none of the boxes below." % said,
                          kind=wkind, mode="warmup", view="warmup", pool=[wp["id"] for wp in wl])
        if len(set(wks)) > 1:
            slots["W"]["kinds"] = {wp["id"]: k for k, wp in zip(wks, wl)}
        main_html = slot_html("W", "Warm-up reading" + (": " + wl[0]["title"] if len(wl) == 1 else ""),
                              slots["W"]["intro"]) + main_html
    for key in cfg:
        if key not in opts.get("_cfg_keys", ()) and key not in COMMON_CFG:
            raise ValueError("%s: cfg key %r means nothing to this view (it takes %s)"
                             % (kit, key, ", ".join(sorted(set(opts.get("_cfg_keys", ())) | COMMON_CFG))))
    opts = {k: v for k, v in opts.items() if not k.startswith("_")}
    from .readkit_drill import RD_DRILL_JS, RD_FIND_JS, RD_RECALL_JS, RD_TIMED_JS
    # Idea units ship only where a free-recall drill ticks them.
    keep = ("id", "title", "band", "paragraphs", "questions") + (("ideas",) if any(sl["flow"] == "recall" for sl in slots.values()) else ())
    script = RATIONAL_JS + RD_CORE_JS
    if any(s["kind"] in ("rec", "nums", "entries", "strings") for s in spec) or lists:
        script += RD_LIST_JS
    if needs_text or slots:
        script += RD_TEXT_JS
    script += RD_LOG_JS
    script += js
    script += (cfg_literal("PRESETS", tbl) + cfg_literal("SPEC", spec)
               + cfg_literal("TILES", [cid for _label, cid in tiles]) + cfg_literal("VIEW", view)
               + cfg_literal("OPTS", opts) + cfg_literal("LESSON", str(cfg.get("lesson", "")))
               + cfg_literal("PASSAGES", embed(passages or [], keep)))
    if slots:
        script += cfg_literal("SLOTS", slots) + RD_DRILL_JS
        if any(sl["display"] in ("pacer", "mask", "rsvp", "phrases") or sl["flow"] == "practice" for sl in slots.values()):
            script += RD_TIMED_JS
        if any(sl["flow"] in ("reread", "recall") for sl in slots.values()):
            script += RD_RECALL_JS
        if any(sl["flow"] in ("find", "coverage") for sl in slots.values()):
            script += RD_FIND_JS
    script += RD_WIRE_JS % {"p": prefix, "fn": fn}
    if slots:
        script += "  rdDrillInit();\n"
    script += ui_js
    script = _COMMENT_LINES.sub("", script)
    markup = ('      <div class="lab-toolbar">\n'
              '        <div class="lab-title"><strong>%s</strong><span>%s</span></div>\n'
              "      </div>\n" % (esc(title), esc(subtitle))
              + '      <div class="status-banner" id="rdDue" style="display:none;margin-top:12px;"></div>\n'
              + main_html
              + '      <div id="%sExtra" style="margin-top:12px;"></div>\n' % prefix
              + ('      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="%sTable"></table></div>\n'
                 % prefix)
              + '      <div class="status-banner" id="%sStatus" style="margin-top:12px;"></div>\n' % prefix)
    intro = cfg.get("panel_intro", panel_intro)
    if intro_tail and intro_tail.lower().rstrip(".") not in intro.lower() and "a one-question difference is not a result" not in intro.lower():
        intro = intro.rstrip() + " " + intro_tail
    return Lab(title=cfg.get("title", title), subtitle=subtitle, markup=markup, controls=controls, script=script,
               panel_title=cfg.get("panel_title", panel_title), panel_intro=intro,
               expect={prefix + "Preset": expect})


# Whole-line /* ... */ comments are for the source and for scripts/mathcheck.js,
# which reads the blocks from this file; a page ships the code without them.
_COMMENT_LINES = re.compile(r"^[ \t]*/\*(?:(?!\*/).)*\*/[ \t]*\n", re.S | re.M)

COMMON_CFG = {"mode", "view", "presets", "preset", "title", "panel_title", "panel_intro", "lesson", "warmup", "warmup_kind"}
LOG_KINDS = ("baseline", "test", "practice", "condition", "other")


def log_kind(kit, value, default):
    v = default if value is None else value
    if v not in LOG_KINDS:
        raise ValueError("%s: log kind %r is not one of %s" % (kit, v, ", ".join(LOG_KINDS)))
    return v


def slot(key, passage, *, intro, kind, mode, view, display="normal", questions=True, qkinds="all", flow="read",
         write=None, target=None, target_key=None, chunk=1, limit=None, split=None, targets=None, suppress=False,
         days=None, summary=False, pool=None, tick=None, published=None, order=None, say=None):
    """One drill's configuration as RD_DRILL_JS reads it.

    pool: passage ids; Start serves the first one not yet in the log. tick: {label, key}, a box
    ticked after Done and stored in the entry's extra. published: the figure (wpm) that the
    aloud fallback writes in place of a reading. order: the compare order this side runs in.
    """
    if suppress and tick is None:
        tick = {"label": "I kept counting the whole way", "key": "kept"}
    return {"passage": passage["id"] if passage else None, "intro": intro, "kind": kind, "mode": mode, "view": view,
            "display": display, "questions": bool(questions), "qkinds": qkinds, "flow": flow, "write": write or {},
            "target": target, "targetKey": target_key, "chunk": chunk, "limit": limit, "split": split,
            "targets": targets, "suppress": bool(suppress), "days": days, "summary": bool(summary),
            "pool": pool, "tick": tick, "published": published, "order": order, "say": say}


def num(kit, cfg, key, default, lo=None, hi=None, whole=False):
    """A numeric cfg value (int, Fraction or "a/b"), range-checked; returned as text the JS parses."""
    v = _unfloat(cfg.get(key, default))
    if v is None:
        return None
    if isinstance(v, bool) or not isinstance(v, (int, str, Fraction)):
        raise ValueError("%s: cfg[%r] should be a number, not %r" % (kit, key, v))
    try:
        f = Fraction(str(v).replace(" ", ""))
    except (ValueError, ZeroDivisionError):
        raise ValueError("%s: cfg[%r] should be a number, not %r" % (kit, key, v))
    if (lo is not None and f < lo) or (hi is not None and f > hi) or (whole and f.denominator != 1):
        raise ValueError("%s: cfg[%r] is %s; it must be %s%s%s" % (
            kit, key, v, "a whole number " if whole else "", "" if lo is None else "at least %s " % lo,
            "" if hi is None else "at most %s" % hi))
    return f


def ftext(f):
    return str(f.numerator) if f.denominator == 1 else "%d/%d" % (f.numerator, f.denominator)


__all__ = ["RD_CORE_JS", "RD_LIST_JS", "RD_TEXT_JS", "RD_LOG_JS", "RD_WIRE_JS", "LOG_KEY", "check_passage", "passage_counts",
           "passages_of", "resolve_targets", "section_starts", "all_tokens", "embed", "field_text", "presets",
           "camel", "build_lab", "slot_html", "btn", "esc", "attr", "num", "ftext", "PHOTO_NOTE", "word_count"]
