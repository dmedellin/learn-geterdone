"""phenkit_core -- what every mode of the Phenomenology of Perception kit shares.

Specified in docs/phenomenology/PLAN.md section D.0, which adopts
docs/philosophy/PLAN.md section D.0 and the capkit conventions as implemented
(docs/capital/kit-a-report.md). The kit's report, with every field, tile and
format an author configures, is docs/phenomenology/kit-report.md.

JavaScript (PH_CORE_JS, shipped on every phenkit page after RATIONAL_JS):

  phNum(r)              exact figure, reduced, minus sign U+2212: "85/2", "−2"
  phQty(r, unit)        "2 cm", "85/2 cm"; the bare figure when unit is ""
  phDeg(r)              "45°", "45/2°", "−45°"
  phFixed(r, places)    a decimal to exactly `places` places, half away from
                        zero, computed on the exact value: "0.0090"
  phApprox(r, places, suffix)
                        the exact figure and its decimal: "1737/192200 ≈
                        0.0090 rad"; "=" in place of "≈" when the decimal is
                        exact ("13/100 = 0.1300 rad"); a whole number alone
                        ("0 rad")
  phPct(r)              "47/51 ≈ 92.2%", "1 = 100%", "0 = 0%" (one decimal)
  phAngleText(a)        a Pythagorean angle: "3-4-5: cos 4/5, ≈ 36.87°"
  phNames(list)         "a, b, c", or "none" for an empty list
  phEsc, phSet, phBlank, phRefuse, phTable(caption, head, rows), phSvg
  phRead(spec, raw)     parse every input of a view; THROWS a sentence for the
                        reader, which the wiring paints red

  Field kinds phRead understands (the same dicts drive the Python check):
    num, pos (> 0), nn (>= 0), share (0..1), count (whole >= 1),
    nncount (whole >= 0), l10 (whole 0..10), optpos (empty or > 0),
    deg (a rational in [-180, 180]; -180 is read as 180),
    numnone (a number or "none"), name, label (may be empty), yesno,
    word (one of f.words), cell (y, n or -), tokens (space-separated words,
    may be empty), pattern (letters and _), wordtag (word or word:tag),
    tag (empty or a word), dir (a view direction, D.0), angle (a Pythagorean
    angle or a compass point, D.0), reach ("70" or "left 70, right 0"),
    solid ("cube" or "box W D H"), necker ("wire cube", "solid box W D H", ...),
    list (f.each, f.sep "ws" | "comma", f.lo..f.hi, f.unique),
    rec  (records "a, 1, 2; b, 3, 4": f.sub = [[key, kind], ...], the last
          f.opt parts optional, f.lo..f.hi records, f.unique on the first part)

Python:

  parse(where, spec, text)          the build-time mirror of phRead for one
                                    field: raises ValueError naming the preset
  to_text(where, spec, value)       a preset value -> the text its box holds
  presets(cfg, kit, fields, ...)    (table, menu, expect, chosen)
  mode_lab(cfg, ...)                the whole Lab for one mode and view

A mode supplies one pure JS function  <xx>Compute(view, inst, opts)  returning
{tiles: {id: text}, status: text, table: {caption, head, rows} | null,
svg: string | undefined} or {refuse: sentence}. opts carries the lesson's
fixed cfg values (unit, model, accounts, ...) and the current value of each
redraw-only control. Being pure, it is what scripts/mathcheck.js calls.
"""

import html
import json
import math
import re
from fractions import Fraction

from .algebra_core import RATIONAL_JS
from .common import Lab, cfg_literal

UNITS = ["mm", "cm", "m", "km"]

# The Pythagorean angles of D.0: name -> (cos, sin, approximate degrees as
# printed). The degree strings are D.0's own; no trigonometry computes them.
ANGLES = {
    "0": ((1, 1), (0, 1), "0"), "3-4-5": ((4, 5), (3, 5), "≈ 36.87"), "4-3-5": ((3, 5), (4, 5), "≈ 53.13"),
    "5-12-13": ((12, 13), (5, 13), "≈ 22.62"), "12-5-13": ((5, 13), (12, 13), "≈ 67.38"),
    "8-15-17": ((15, 17), (8, 17), "≈ 28.07"), "15-8-17": ((8, 17), (15, 17), "≈ 61.93"),
    "90": ((0, 1), (1, 1), "90"), "180": ((-1, 1), (0, 1), "180"), "270": ((0, 1), (-1, 1), "270"),
}
COMPASS = {"east": "0", "north": "90", "west": "180", "south": "270"}
DIRS = {"front": (0, 0, 1), "back": (0, 0, -1), "right": (1, 0, 0), "left": (-1, 0, 0),
        "above": (0, 1, 0), "below": (0, -1, 0)}

# ---------------------------------------------------------------------------
# JavaScript shared by every phenkit page
# ---------------------------------------------------------------------------

PH_CORE_JS = r"""
  /* phenkit's shared printing and parsing. Every parse THROWS an Error whose
     message is a sentence for the reader; the wiring catches it, paints the
     banner red and blanks the tiles. Nothing after the parse is inside that
     catch. Every printed figure is exact; a decimal beside it is marked. */
  var PH_DASH = '—', PH_MINUS = '−';
  function phEsc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }
  function phClean(text) {
    return String(text === null || text === undefined ? '' : text).replace(/−/g, '-').trim();
  }
  function phNum(r) { return (Rsign(r) < 0 ? PH_MINUS : '') + Rtext(Rabs(r)); }
  function phQty(r, unit) { return phNum(r) + (unit ? ' ' + unit : ''); }
  function phDeg(r) { return phNum(r) + '°'; }
  /* Exactly `places` decimals, half away from zero, on the exact value. */
  function phFixed(r, places) {
    var neg = r.n < 0n, num = neg ? -r.n : r.n, scale = 10n ** BigInt(places);
    var q = (num * scale * 2n / r.d + 1n) / 2n, s = q.toString();
    while (s.length <= places) s = '0' + s;
    var out = places > 0 ? s.slice(0, s.length - places) + '.' + s.slice(s.length - places) : s;
    return (neg && q !== 0n ? PH_MINUS : '') + out;
  }
  /* Is r * 10^places a whole number? Then its decimal is exact. */
  function phExactAt(r, places) { return Rint(Rmul(r, R(10n ** BigInt(places)))); }
  function phApprox(r, places, suffix) {
    var tail = suffix ? ' ' + suffix : '';
    if (Rint(r)) return phNum(r) + tail;
    return phNum(r) + (phExactAt(r, places) ? ' = ' : ' ≈ ') + phFixed(r, places) + tail;
  }
  function phPct(r) {
    var p = Rmul(r, R(100n)), exact = phExactAt(p, 1);
    var d = exact ? Rdec(p, 1) : phFixed(p, 1);
    return phNum(r) + (exact ? ' = ' : ' ≈ ') + d.replace('-', PH_MINUS) + '%';
  }
  function phNames(list) { return list.length ? list.join(', ') : 'none'; }
  function phSum(v) { var s = R0; v.forEach(function (x) { s = Radd(s, x); }); return s; }

  /* The Pythagorean angles of D.0. a-b-c means cos b/c, sin a/c. The degree
     figures are D.0's printed approximations, not computed. */
  var PH_ANGLES = {
    '0': [R(1n), R(0n), '0°'], '3-4-5': [R(4n, 5n), R(3n, 5n), '≈ 36.87°'], '4-3-5': [R(3n, 5n), R(4n, 5n), '≈ 53.13°'],
    '5-12-13': [R(12n, 13n), R(5n, 13n), '≈ 22.62°'], '12-5-13': [R(5n, 13n), R(12n, 13n), '≈ 67.38°'],
    '8-15-17': [R(15n, 17n), R(8n, 17n), '≈ 28.07°'], '15-8-17': [R(8n, 17n), R(15n, 17n), '≈ 61.93°'],
    '90': [R(0n), R(1n), '90°'], '180': [R(-1n), R(0n), '180°'], '270': [R(0n), R(-1n), '270°']
  };
  /* Listed in this order (an object's integer-like keys would sort first). */
  var PH_ANGLE_ORDER = ['0', '3-4-5', '4-3-5', '5-12-13', '12-5-13', '8-15-17', '15-8-17', '90', '180', '270'];
  var PH_COMPASS = { east: '0', north: '90', west: '180', south: '270' };
  function phAngle(text, what) {
    var s = phClean(text).toLowerCase(), name = PH_COMPASS[s] !== undefined ? PH_COMPASS[s] : s;
    var a = PH_ANGLES[name];
    if (!a) {
      throw new Error(what + ' "' + phClean(text) + '" is not one of the angles this lab can turn by exactly: '
        + PH_ANGLE_ORDER.join(', ') + ' (or east, north, west, south)');
    }
    return { name: name, word: s !== name ? s : '', cos: a[0], sin: a[1], deg: a[2] };
  }
  function phAngleText(a) { return (a.word ? a.word + ' (' + a.name + ')' : a.name) + ': cos ' + phNum(a.cos) + ', ' + a.deg; }

  /* View directions, D.0: a named face direction or a whole-number triple of
     whole-number length, each component at most 20 in size. */
  var PH_DIRS = { front: [0, 0, 1], back: [0, 0, -1], right: [1, 0, 0], left: [-1, 0, 0], above: [0, 1, 0], below: [0, -1, 0] };
  var PH_FACES = ['front', 'back', 'right', 'left', 'above', 'below'];
  function phIsqrt(n) { if (n < 2n) return n; var x = n, y = (x + 1n) / 2n; while (y < x) { x = y; y = (x + n / x) / 2n; } return x; }
  function phDir(text, what) {
    var s = phClean(text).toLowerCase(), v;
    if (PH_DIRS[s]) return { text: s, v: PH_DIRS[s].map(function (c) { return BigInt(c); }), len: 1n };
    var m = /^(-?\d+)\s+(-?\d+)\s+(-?\d+)$/.exec(s);
    var why = ' A view is front, back, right, left, above or below, or three whole numbers of whole-number length, '
      + 'such as 3 0 4, 1 2 2, 2 3 6, 1 4 8 or 4 4 7, with any signs and in any order';
    if (!m) throw new Error(what + ' "' + phClean(text) + '" is not a view direction.' + why);
    v = [BigInt(m[1]), BigInt(m[2]), BigInt(m[3])];
    if (v.some(function (c) { return c > 20n || c < -20n; })) throw new Error(what + ' "' + s + '" has a component past 20.' + why);
    var sq = v[0] * v[0] + v[1] * v[1] + v[2] * v[2], len = phIsqrt(sq);
    if (sq === 0n) throw new Error(what + ' is 0 0 0, which points nowhere.' + why);
    if (len * len !== sq) throw new Error(what + ' "' + s + '" has length √' + sq + ', not a whole number.' + why);
    return { text: v.join(' '), v: v, len: len };
  }

  function phNumber(text, what) {
    var s = phClean(text), r = s === '' ? null : Rparse(s);
    if (r === null) throw new Error(what + ' should be a number such as 3, 1/2 or 0.25, and "' + s + '" is not one');
    return r;
  }
  var PH_BAD_NAME = /[,;:<>&"=]/;
  var PH_WORD = /^[^\W\d_]+$/;
  var PH_TOKEN = /^[^\s,;:<>&"=]+$/;
  function phLetters(s, what) {
    if (!PH_WORD.test(s)) throw new Error(what + ' "' + s + '" should be a word of letters only');
    return s.toLowerCase();
  }
  function phSized(n, f, what) {
    if (n < f.lo) throw new Error(what + (n === 0 ? ' is empty' : ': this lab needs at least ' + f.lo + ', and there ' + (n === 1 ? 'is 1' : 'are ' + n)));
    if (n > f.hi) throw new Error(what + ': this lab takes at most ' + f.hi + ', and there are ' + n);
  }
  function phScalar(f, text, what) {
    var s = phClean(text), r, m;
    switch (f.kind) {
      case 'label':
        if (PH_BAD_NAME.test(s)) throw new Error(what + ' "' + s + '" may not contain , ; : = < > & or quotes');
        return s;
      case 'name':
        if (s === '') throw new Error(what + ' is missing');
        if (PH_BAD_NAME.test(s)) throw new Error(what + ' "' + s + '" may not contain , ; : = < > & or quotes');
        return s;
      case 'yesno':
        if (/^(yes|y)$/i.test(s)) return true;
        if (/^(no|n)$/i.test(s)) return false;
        throw new Error(what + ' should be yes or no, not "' + s + '"');
      case 'word':
        if (f.words.indexOf(s.toLowerCase()) < 0) throw new Error(what + ' should be one of ' + f.words.join(', ') + ', not "' + s + '"');
        return s.toLowerCase();
      case 'cell':
        if (s !== 'y' && s !== 'n' && s !== '-') throw new Error(what + ' should be y (consistent), n (inconsistent) or - (silent), not "' + s + '"');
        return s;
      case 'tokens':
        if (s === '') return [];
        var toks = s.split(/\s+/);
        toks.forEach(function (t) { if (!PH_TOKEN.test(t)) throw new Error(what + ': "' + t + '" may not contain , ; : = < > & or quotes'); });
        return toks.filter(function (t, i) { return toks.indexOf(t) === i; });
      case 'pattern':
        if (!/^[^\W\d]+$/.test(s)) throw new Error(what + ' "' + s + '" should be letters, with _ for each letter not seen');
        return s.toLowerCase();
      case 'wordtag':
        m = /^([^:]*)(?::(.*))?$/.exec(s);
        return { word: phLetters(m[1], what), tag: m[2] === undefined ? null : phLetters(m[2], what + "'s tag") };
      case 'tag':
        return s === '' ? null : phLetters(s, what);
      case 'dir': return phDir(s, what);
      case 'angle': return phAngle(s, what);
      case 'numnone':
        if (/^none$/i.test(s)) return null;
        return phNumber(s, what + ' (a number, or none)');
      case 'reach':
        if (Rparse(s) !== null) { r = phScalar({ kind: 'nn' }, s, what); return { left: r, right: r }; }
        m = /^(left|right)\s+(\S+)\s*,\s*(left|right)\s+(\S+)$/i.exec(s);
        if (!m || m[1].toLowerCase() === m[3].toLowerCase()) {
          throw new Error(what + ' should be one figure for both sides, such as 70, or both sides, such as left 70, right 0; not "' + s + '"');
        }
        var out = {};
        out[m[1].toLowerCase()] = phScalar({ kind: 'nn' }, m[2], what);
        out[m[3].toLowerCase()] = phScalar({ kind: 'nn' }, m[4], what);
        return out;
      case 'solid':
      case 'necker':
        var parts = s.toLowerCase().split(/\s+/), wire = null;
        if (f.kind === 'necker') {
          wire = parts[0] === 'wire' ? true : (parts[0] === 'solid' ? false : null);
          if (wire === null) throw new Error(what + ' should be wire cube, wire box W D H, solid cube or solid box W D H; not "' + s + '"');
          parts = parts.slice(1);
        }
        if (parts.length === 1 && parts[0] === 'cube') return { wire: wire, w: R1, d: R1, h: R1, box: false };
        if (parts.length === 4 && parts[0] === 'box') {
          var dims = parts.slice(1).map(function (t) { return phScalar({ kind: 'pos' }, t, what + "'s dimension"); });
          if (dims.some(function (x) { return Rcmp(x, R(20n)) > 0; })) throw new Error(what + ': each dimension is at most 20');
          return { wire: wire, w: dims[0], d: dims[1], h: dims[2], box: true };
        }
        throw new Error(what + ' should be ' + (f.kind === 'necker' ? 'wire or solid, then ' : '') + 'cube, or box and three dimensions (width, depth, height); not "' + s + '"');
    }
    if (f.kind === 'optpos' && s === '') return null;
    r = phNumber(s, what);
    if ((f.kind === 'pos' || f.kind === 'optpos') && Rsign(r) <= 0) throw new Error(what + ' must be more than 0, and it is ' + phNum(r));
    if (f.kind === 'nn' && Rsign(r) < 0) throw new Error(what + ' cannot be negative, and it is ' + phNum(r));
    if (f.kind === 'share' && (Rsign(r) < 0 || Rcmp(r, R1) > 0)) throw new Error(what + ' is a share from 0 to 1, and it is ' + phNum(r));
    if (f.kind === 'count' && (!Rint(r) || Rsign(r) <= 0)) throw new Error(what + ' must be a whole number of at least 1, not ' + phNum(r));
    if (f.kind === 'nncount' && (!Rint(r) || Rsign(r) < 0)) throw new Error(what + ' must be a whole number, 0 or more, not ' + phNum(r));
    if (f.kind === 'l10' && (!Rint(r) || Rsign(r) < 0 || Rcmp(r, R(10n)) > 0)) throw new Error(what + ' must be a whole number from 0 to 10, not ' + phNum(r));
    if (f.kind === 'deg') {
      if (Rcmp(r, R(-180n)) < 0 || Rcmp(r, R(180n)) > 0) throw new Error(what + ' is an angle from −180° to 180°, and it is ' + phDeg(r));
      if (Requ(r, R(-180n))) r = R(180n);
    }
    return r;
  }
  function phList(text, f, what) {
    var s = phClean(text);
    var parts = s === '' ? [] : (f.sep === 'comma' ? s.split(',') : s.split(/[\s,]+/)).map(function (t) { return t.trim(); });
    if (f.sep === 'comma' && parts.length && parts[parts.length - 1] === '') parts.pop();
    parts = parts.filter(function (t, i) { return t !== '' || f.sep === 'comma'; });
    phSized(parts.length, f, what);
    var seen = {};
    return parts.map(function (t, i) {
      var v = phScalar(f.each, t, 'Entry ' + (i + 1) + ' of ' + what);
      if (f.unique) {
        var key = typeof v === 'object' && v && v.word ? v.word : String(v && v.n !== undefined ? Rtext(v) : v);
        if (seen[key]) throw new Error(what + ' names "' + key + '" twice');
        seen[key] = true;
      }
      return v;
    });
  }
  function phRecords(text, f, what) {
    var s = phClean(text), rows = s === '' ? [] : s.split(';').map(function (r) { return r.trim(); });
    if (rows.length && rows[rows.length - 1] === '') rows.pop();
    phSized(rows.length, f, what);
    var seen = {}, need = f.sub.length - (f.opt || 0);
    return rows.map(function (row, i) {
      var cells = row.split(',').map(function (c) { return c.trim(); });
      if (cells.length < need || cells.length > f.sub.length) {
        throw new Error('Entry ' + (i + 1) + ' of ' + what + ' has ' + cells.length + ' part' + (cells.length === 1 ? '' : 's')
          + '; each needs ' + (need === f.sub.length ? need : need + ' to ' + f.sub.length) + ': '
          + f.sub.map(function (k) { return k[0]; }).join(', '));
      }
      var rec = {};
      f.sub.forEach(function (k, j) {
        rec[k[0]] = j < cells.length ? phScalar(k[1], cells[j], 'The ' + k[0].replace(/_/g, ' ') + ' in entry ' + (i + 1) + ' of ' + what) : null;
      });
      if (f.unique) {
        var key = String(cells[0]).toLowerCase();
        if (seen[key]) throw new Error(what + ' names "' + cells[0] + '" twice');
        seen[key] = true;
      }
      return rec;
    });
  }
  function phField(f, text) {
    if (f.kind === 'rec') return phRecords(text, f, f.what);
    if (f.kind === 'list') return phList(text, f, f.what);
    return phScalar(f, text, f.what);
  }
  function phRead(spec, raw) {
    var out = {};
    spec.forEach(function (f) { out[f.key] = phField(f, raw[f.key]); });
    return out;
  }

  function phSet(id, text) { document.getElementById(id).textContent = text; }
  function phBlank(ids) { ids.forEach(function (id) { phSet(id, PH_DASH); }); }
  function phRefuse(statusEl, ids, why) {
    phBlank(ids);
    statusEl.innerHTML = '<span class="tone-red">' + phEsc(String(why).replace(/\.$/, '')) + '.</span>';
  }
  /* head: header texts; rows: rows of cells, each text or {t: text, c: class}. */
  function phTable(caption, head, rows) {
    var h = '<caption>' + phEsc(caption) + '</caption><thead><tr>'
      + head.map(function (x) { return '<th>' + phEsc(x) + '</th>'; }).join('') + '</tr></thead><tbody>';
    rows.forEach(function (row) {
      h += '<tr>' + row.map(function (cell) {
        var t = (cell && cell.t !== undefined) ? cell.t : cell, c = (cell && cell.c) ? cell.c : '';
        return '<td' + (c ? ' class="' + c + '"' : '') + '>' + phEsc(t) + '</td>';
      }).join('') + '</tr>';
    });
    return h + '</tbody>';
  }
  /* A drawing. Pixel positions may be floats (D.0); no tile reads them. */
  function phSvg(w, h, label, inner) {
    return '<svg viewBox="0 0 ' + w + ' ' + h + '" role="img" style="width:100%;height:auto;display:block" aria-label="'
      + phEsc(label) + '">' + inner + '</svg>';
  }
  function phPx(x) { return String(Math.round(x * 10) / 10); }
  function phLine(x1, y1, x2, y2, stroke, extra) {
    return '<line x1="' + phPx(x1) + '" y1="' + phPx(y1) + '" x2="' + phPx(x2) + '" y2="' + phPx(y2)
      + '" stroke="' + stroke + '" stroke-width="2"' + (extra || '') + '></line>';
  }
  function phText(x, y, text, anchor) {
    return '<text x="' + phPx(x) + '" y="' + phPx(y) + '" fill="var(--text)" font-size="13"'
      + (anchor ? ' text-anchor="' + anchor + '"' : '') + '>' + phEsc(text) + '</text>';
  }
"""

# The wiring every phenkit page shares. %(fn)s is the mode's pure function.
PH_WIRE_JS = r"""
  var presetS = document.getElementById('%(p)sPreset');
  var statusEl = document.getElementById('%(p)sStatus');
  var tableEl = document.getElementById('%(p)sTable');
  var figEl = document.getElementById('%(p)sFigure');
  function field(id) { return document.getElementById(id); }
  function phOpts() {
    var o = {};
    Object.keys(FIXED).forEach(function (k) { o[k] = FIXED[k]; });
    REDRAW.forEach(function (r) {
      var el = field(r.id);
      if (r.lo !== undefined) {
        o[r.key] = Number(el.value);
        var out = field(r.id + 'Out');
        if (out) out.textContent = el.value;
      } else {
        o[r.key] = el.value;
      }
    });
    return o;
  }
  function phClear() { tableEl.innerHTML = ''; if (figEl) figEl.innerHTML = ''; }
  function redraw() {
    var raw = {}, inst;
    SPEC.forEach(function (f) { raw[f.key] = field(f.id).value; });
    try { inst = phRead(SPEC, raw); } catch (err) { phClear(); phRefuse(statusEl, TILES, err.message); return; }
    var opts = phOpts(), bad = null;
    REDRAW.forEach(function (r) {
      var v = opts[r.key];
      if (r.lo !== undefined && !(Number.isInteger(v) && v >= r.lo && v <= r.hi)) bad = r.label + ' runs from ' + r.lo + ' to ' + r.hi;
      if (r.values && r.values.indexOf(v) < 0) bad = r.label + ' should be one of ' + r.values.join(', ');
    });
    if (bad) { phClear(); phRefuse(statusEl, TILES, bad); return; }
    var out = %(fn)s(VIEW, inst, opts);
    if (out.refuse) { phClear(); phRefuse(statusEl, TILES, out.refuse); return; }
    TILES.forEach(function (id) { phSet(id, out.tiles[id] === undefined ? PH_DASH : out.tiles[id]); });
    tableEl.innerHTML = out.table ? phTable(out.table.caption, out.table.head, out.table.rows) : '';
    if (figEl) figEl.innerHTML = out.svg || '';
    statusEl.innerHTML = phEsc(out.status);
  }
  presetS.addEventListener('change', function () {
    var inst = PRESETS[presetS.value];
    if (!inst) return;
    /* Only the instance's text boxes. A redraw-only control is never touched
       here (D.0), so what a preset prints never depends on the one before. */
    SPEC.forEach(function (f) { if (inst[f.key] !== undefined) field(f.id).value = inst[f.key]; });
    redraw();
  });
  SPEC.forEach(function (f) { field(f.id).addEventListener('input', redraw); });
  REDRAW.forEach(function (r) { field(r.id).addEventListener(r.lo !== undefined ? 'input' : 'change', redraw);
    if (r.lo !== undefined) field(r.id).addEventListener('change', redraw); });
  redraw();
  window.redrawLab = redraw;
"""

# ---------------------------------------------------------------------------
# Python: the build-time mirror of phRead, and lesson data -> box text
# ---------------------------------------------------------------------------

_BAD_NAME = re.compile(r'[,;:<>&"=]')
_TOKEN = re.compile(r'^[^\s,;:<>&"=]+$')
_WORD = re.compile(r"^[^\W\d_]+$")


def rparse(text):
    """Rparse: "3", "-7/4", "0.25" -> Fraction; anything else (1/0 too) -> None."""
    s = str(text).strip().replace("−", "-")
    m = re.fullmatch(r"([+-]?\d+)\s*/\s*(\d+)", s)
    if m:
        return None if int(m.group(2)) == 0 else Fraction(int(m.group(1)), int(m.group(2)))
    if re.fullmatch(r"[+-]?\d+", s):
        return Fraction(int(s))
    if re.fullmatch(r"[+-]?\d*\.\d+", s):
        return Fraction(s)
    return None


def ftext(f):
    """A Fraction as the box holds it: "3", "85/2", "-1"."""
    f = Fraction(f)
    return str(f.numerator) if f.denominator == 1 else "%d/%d" % (f.numerator, f.denominator)


def _num(where, s, what):
    r = None if s == "" else rparse(s)
    if r is None:
        raise ValueError("%s: %s should be a number, not %r" % (where, what, s))
    return r


def parse_scalar(where, f, text, what):
    """Mirror of phScalar: the value, or ValueError naming the preset."""
    s = str(text).replace("−", "-").strip()
    k = f["kind"]
    if k in ("label", "name"):
        if (k == "name" and not s) or _BAD_NAME.search(s):
            raise ValueError("%s: %s %r is not usable (no , ; : = < > & or quotes%s)"
                             % (where, what, s, "" if k == "label" else ", not empty"))
        return s
    if k == "yesno":
        if s.lower() not in ("yes", "y", "no", "n"):
            raise ValueError("%s: %s should be yes or no, not %r" % (where, what, s))
        return s.lower() in ("yes", "y")
    if k == "word":
        if s.lower() not in f["words"]:
            raise ValueError("%s: %s should be one of %s, not %r" % (where, what, ", ".join(f["words"]), s))
        return s.lower()
    if k == "cell":
        if s not in ("y", "n", "-"):
            raise ValueError("%s: %s should be y, n or -, not %r" % (where, what, s))
        return s
    if k == "tokens":
        toks = s.split() if s else []
        for t in toks:
            if not _TOKEN.match(t):
                raise ValueError("%s: %s: %r is not a usable word" % (where, what, t))
        return list(dict.fromkeys(toks))
    if k == "pattern":
        if not re.fullmatch(r"[^\W\d]+", s):
            raise ValueError("%s: %s %r should be letters and _" % (where, what, s))
        return s.lower()
    if k == "wordtag":
        word, _, tag = s.partition(":")
        if not _WORD.match(word) or (":" in s and not _WORD.match(tag)):
            raise ValueError("%s: %s %r should be a word, or word:tag, of letters" % (where, what, s))
        return (word.lower(), tag.lower() if ":" in s else None)
    if k == "tag":
        if s and not _WORD.match(s):
            raise ValueError("%s: %s %r should be a word of letters, or empty" % (where, what, s))
        return s.lower() or None
    if k == "dir":
        return parse_dir(where, s, what)
    if k == "angle":
        name = COMPASS.get(s.lower(), s.lower())
        if name not in ANGLES:
            raise ValueError("%s: %s %r is not one of %s (or a compass point)" % (where, what, s, ", ".join(ANGLES)))
        return name
    if k == "numnone":
        return None if s.lower() == "none" else _num(where, s, what)
    if k == "reach":
        if rparse(s) is not None:
            v = parse_scalar(where, {"kind": "nn"}, s, what)
            return {"left": v, "right": v}
        m = re.fullmatch(r"(left|right)\s+(\S+)\s*,\s*(left|right)\s+(\S+)", s, re.I)
        if not m or m.group(1).lower() == m.group(3).lower():
            raise ValueError("%s: %s %r should be 70 or left 70, right 0" % (where, what, s))
        return {m.group(1).lower(): parse_scalar(where, {"kind": "nn"}, m.group(2), what),
                m.group(3).lower(): parse_scalar(where, {"kind": "nn"}, m.group(4), what)}
    if k in ("solid", "necker"):
        parts = s.lower().split()
        if k == "necker":
            if not parts or parts[0] not in ("wire", "solid"):
                raise ValueError("%s: %s %r should start wire or solid" % (where, what, s))
            parts = parts[1:]
        if parts == ["cube"]:
            return (1, 1, 1)
        if len(parts) == 4 and parts[0] == "box":
            dims = [parse_scalar(where, {"kind": "pos"}, t, what) for t in parts[1:]]
            if any(d > 20 for d in dims):
                raise ValueError("%s: %s: each dimension is at most 20" % (where, what))
            return tuple(dims)
        raise ValueError("%s: %s %r should be cube or box W D H" % (where, what, s))
    if k == "optpos" and s == "":
        return None
    r = _num(where, s, what)
    bad = ((k in ("pos", "optpos") and r <= 0) or (k == "nn" and r < 0) or (k == "share" and not 0 <= r <= 1)
           or (k == "count" and (r.denominator != 1 or r < 1)) or (k == "nncount" and (r.denominator != 1 or r < 0))
           or (k == "l10" and (r.denominator != 1 or not 0 <= r <= 10)) or (k == "deg" and not -180 <= r <= 180))
    if bad:
        raise ValueError("%s: %s is %s, which a %s field refuses" % (where, what, s, k))
    if k not in ("num", "pos", "optpos", "nn", "share", "count", "nncount", "l10", "deg"):
        raise ValueError("%s: unknown field kind %r" % (where, k))
    return Fraction(180) if (k == "deg" and r == -180) else r


def parse_dir(where, s, what):
    s = s.strip().lower()
    if s in DIRS:
        return DIRS[s]
    m = re.fullmatch(r"(-?\d+)\s+(-?\d+)\s+(-?\d+)", s)
    if not m:
        raise ValueError("%s: %s %r is not a view direction (a face name, or three whole numbers such as 1 2 2)"
                         % (where, what, s))
    v = tuple(int(g) for g in m.groups())
    sq = sum(c * c for c in v)
    if any(abs(c) > 20 for c in v) or sq == 0 or math.isqrt(sq) ** 2 != sq:
        raise ValueError("%s: %s %r is refused: components at most 20, not all zero, whole-number length "
                         "(3 0 4, 1 2 2, 2 3 6, 1 4 8, 4 4 7)" % (where, what, s))
    return v


def _sized(where, n, f, what):
    if not f["lo"] <= n <= f["hi"]:
        raise ValueError("%s: %s has %d entries; this lab takes %d to %d" % (where, what, n, f["lo"], f["hi"]))


def parse(where, f, text):
    """Mirror of phField for one field, at build time."""
    what = f["what"]
    s = str(text).replace("−", "-").strip()
    if f["kind"] == "list":
        if f.get("sep") == "comma":
            parts = [t.strip() for t in s.split(",")] if s else []
            if parts and parts[-1] == "":
                parts.pop()
        else:
            parts = [t for t in re.split(r"[\s,]+", s) if t] if s else []
        _sized(where, len(parts), f, what)
        vals = [parse_scalar(where, f["each"], t, "entry %d of %s" % (i + 1, what)) for i, t in enumerate(parts)]
        if f.get("unique"):
            keys = [v[0] if isinstance(v, tuple) else str(v) for v in vals]
            dup = sorted({x for x in keys if keys.count(x) > 1})
            if dup:
                raise ValueError("%s: %s names %s twice" % (where, what, ", ".join(dup)))
        return vals
    if f["kind"] == "rec":
        rows = [r.strip() for r in s.split(";")] if s else []
        if rows and rows[-1] == "":
            rows.pop()
        _sized(where, len(rows), f, what)
        need = len(f["sub"]) - f.get("opt", 0)
        out, seen = [], set()
        for i, row in enumerate(rows):
            cells = [c.strip() for c in row.split(",")]
            if not need <= len(cells) <= len(f["sub"]):
                raise ValueError("%s: entry %d of %s has %d parts; it needs %s: %s"
                                 % (where, i + 1, what, len(cells), need if need == len(f["sub"])
                                    else "%d to %d" % (need, len(f["sub"])), ", ".join(k for k, _ in f["sub"])))
            rec = {}
            for j, (key, kk) in enumerate(f["sub"]):
                rec[key] = parse_scalar(where, kk, cells[j], "%s of entry %d of %s" % (key, i + 1, what)) \
                    if j < len(cells) else None
            if f.get("unique"):
                if cells[0].lower() in seen:
                    raise ValueError("%s: %s names %r twice" % (where, what, cells[0]))
                seen.add(cells[0].lower())
            out.append(rec)
        return out
    return parse_scalar(where, f, s, what)


def _part_text(v):
    if isinstance(v, bool):
        return "yes" if v else "no"
    if isinstance(v, (int, Fraction)):
        return ftext(v)
    if isinstance(v, (list, tuple)):
        return " ".join(_part_text(x) for x in v)
    return str(v)


def to_text(where, f, value):
    """A preset's value for one field -> the exact text its box holds.

    A string is taken as typed. A number or Fraction prints reduced. A list
    field takes a list of items; a record field takes a list of records, each
    a list/tuple of parts (a part that is itself a list is joined by spaces:
    a direction (1, 2, 2) or a list of properties) or a string.
    """
    if isinstance(value, str):
        text = value.strip()
    elif f["kind"] == "list" and isinstance(value, (list, tuple)):
        text = ", ".join(_part_text(v) for v in value)
    elif f["kind"] == "rec" and isinstance(value, (list, tuple)):
        rows = []
        for rec in value:
            if isinstance(rec, str):
                rows.append(rec.strip())
            elif isinstance(rec, (list, tuple)):
                rows.append(", ".join(_part_text(p) for p in rec).rstrip(", ").rstrip())
            else:
                raise ValueError("%s: %s: each record is a list of parts or a string, not %r" % (where, f["what"], rec))
        text = "; ".join(rows)
    elif isinstance(value, (bool, int, Fraction)) or (isinstance(value, (list, tuple)) and f["kind"] in ("dir",)):
        text = _part_text(value)
    else:
        raise ValueError("%s: %s cannot be %r" % (where, f["what"], value))
    if ">" in text or "<" in text:
        raise ValueError("%s: %s %r contains < or >, which no shipped value may" % (where, f["what"], text))
    parse(where, f, text)
    return text


def presets(cfg, kit, fields, redraw_keys=(), fixed_keys=()):
    """(instance table, menu pairs, expect by preset id, the chosen id).

    fields: [(key, spec, default)] -- the instance inputs this view shows. A
    preset lacking a field takes its default; a default of None means the
    field is required. A preset key that is not an input of this view raises
    (a typo would otherwise be ignored), and so does a redraw-only key or a
    lesson-level cfg key such as `accounts` (a preset never changes those).
    """
    plist = cfg.get("presets")
    if not isinstance(plist, list) or not plist:
        raise ValueError("%s: cfg['presets'] must be a non-empty list of instances" % kit)
    known = {key for key, _s, _d in fields} | {"id", "label", "note", "expect"}
    table, menu, expect = {}, [], {}
    for p in plist:
        pid = p.get("id") if isinstance(p, dict) else None
        if not isinstance(pid, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", pid):
            raise ValueError("%s: every preset needs an id of lowercase letters, digits and hyphens, not %r" % (kit, pid))
        where = "%s preset %r" % (kit, pid)
        if pid in table:
            raise ValueError("%s: the id is used twice" % where)
        label = p.get("label")
        if not isinstance(label, str) or not label.strip() or "<" in label or ">" in label:
            raise ValueError("%s: needs a plain-text label" % where)
        locked = sorted({k for k in tuple(redraw_keys) + tuple(fixed_keys) if k in p})
        if locked:
            raise ValueError("%s: sets %s, which the lesson's cfg fixes (a redraw-only control or a lesson-level "
                             "value); a preset never touches it (PLAN.md D.0)" % (where, ", ".join(locked)))
        extra = sorted(set(p) - known)
        if extra:
            raise ValueError("%s: %s %s not an input of this view (it shows %s)"
                             % (where, ", ".join(extra), "is" if len(extra) == 1 else "are",
                                ", ".join(k for k, _s, _d in fields)))
        inst = {}
        for key, spec, default in fields:
            value = p.get(key, default)
            if value is None:
                raise ValueError("%s: needs %s" % (where, key))
            inst[key] = to_text(where, spec, value)
        table[pid] = inst
        menu.append((pid, label))
        expect[pid] = dict(p.get("expect") or {})
    chosen = cfg.get("preset", plist[0]["id"])
    if chosen not in table:
        raise ValueError("%s: cfg['preset'] %r is not one of the presets (%s)" % (kit, chosen, ", ".join(table)))
    return table, menu, expect, chosen


def pick_view(cfg, kit, views):
    view = cfg.get("view", views[0])
    if view not in views:
        raise ValueError("%s: unknown view %r; the views are %s" % (kit, view, ", ".join(views)))
    return view


def plain(cfg, kit, key, default, limit=200):
    """A lesson-level text value (model name, unit): plain, short, no markup."""
    v = cfg.get(key, default)
    if not isinstance(v, str) or "<" in v or ">" in v or "&" in v or len(v) > limit:
        raise ValueError("%s: cfg[%r] should be plain text of at most %d characters, not %r" % (kit, key, limit, v))
    return v


# ---------------------------------------------------------------------------
# Markup
# ---------------------------------------------------------------------------


def attr(text):
    return html.escape(str(text), quote=True)


def select_html(cid, label, options, chosen):
    opts = "".join('<option value="%s"%s>%s</option>' % (attr(v), " selected" if str(v) == str(chosen) else "",
                                                          html.escape(t, quote=False)) for v, t in options)
    return ('        <div class="field">\n          <label for="%s">%s</label>\n'
            '          <select id="%s">%s</select>\n        </div>\n' % (cid, html.escape(label, quote=False), cid, opts))


def text_html(cid, label, value):
    return ('        <div class="field">\n          <label for="%s">%s</label>\n'
            '          <input id="%s" type="text" value="%s" inputmode="text" autocomplete="off">\n'
            "        </div>\n" % (cid, html.escape(label, quote=False), cid, attr(value)))


def range_html(cid, label, lo, hi, value):
    return ("        <div>\n"
            '          <div class="range-row"><label class="small-copy" for="%s">%s</label>'
            '<span class="range-value" id="%sOut">%s</span></div>\n'
            '          <input id="%s" type="range" min="%s" max="%s" step="1" value="%s" />\n'
            "        </div>\n" % (cid, html.escape(label, quote=False), cid, value, cid, lo, hi, value))


def kpis_html(items):
    cells = "".join('          <div class="kpi"><span>%s</span><strong id="%s">&mdash;</strong></div>\n'
                    % (html.escape(label, quote=False), cid) for label, cid in items)
    return '        <div class="kpi-grid">\n%s        </div>\n' % cells


def markup_html(prefix, name, subtitle, figure=False):
    return ('      <div class="lab-toolbar">\n'
            '        <div class="lab-title"><strong>%s</strong><span>%s</span></div>\n'
            "      </div>\n" % (html.escape(name, quote=False), html.escape(subtitle, quote=False))
            + ('      <div id="%sFigure" style="margin-top:12px;"></div>\n' % prefix if figure else "")
            + '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="%sTable"></table></div>\n'
            % prefix
            + '      <div class="status-banner" id="%sStatus" style="margin-top:12px;"></div>\n' % prefix)


def camel(prefix, key):
    """An input's id: prefix + 'In' + CamelKey ('sz', 'standard_distance' -> 'szInStandardDistance')."""
    return prefix + "In" + "".join(part[:1].upper() + part[1:] for part in key.split("_"))


def mode_lab(cfg, *, kit, prefix, view, fields, tiles, mode_js, fn, fixed, title, subtitle,
             panel_title, panel_intro, redraw=(), figure=False, fixed_keys=()):
    """One mode, one view, as a Lab.

    fields: [(key, spec, default)] in display order; spec["what"] is the label.
            Each becomes a text input with id prefix + 'In' + CamelKey, filled
            from the chosen preset.
    tiles:  [(label, id)].
    redraw: [dict(key, id, label, options=[(v, text)] | lo, hi, value)] --
            redraw-only controls: a select, or a range whose bounds the cfg
            fixes. Their shipped value is the cfg's; a preset never sets one.
    fixed:  the lesson-level values handed to the compute function as opts.
    Returns Lab(expect={prefix + 'Preset': {preset id: {tile: text}}}).
    """
    table, menu, expect, chosen = presets(cfg, kit, fields, tuple(r["key"] for r in redraw), fixed_keys)
    here = table[chosen]
    spec = []
    controls = select_html(prefix + "Preset", "Worked example", menu, chosen)
    for key, fspec, _default in fields:
        cid = camel(prefix, key)
        js = dict(fspec, key=key, id=cid)
        spec.append(js)
        controls += text_html(cid, fspec["what"], here[key])
    redraw_js = []
    for r in redraw:
        if "options" in r:
            controls += select_html(r["id"], r["label"], r["options"], r["value"])
            redraw_js.append({"key": r["key"], "id": r["id"], "label": r["label"],
                              "values": [v for v, _t in r["options"]]})
        else:
            controls += range_html(r["id"], r["label"], r["lo"], r["hi"], r["value"])
            redraw_js.append({"key": r["key"], "id": r["id"], "label": r["label"], "lo": r["lo"], "hi": r["hi"]})
    controls += kpis_html(tiles)
    ids = [s["id"] for s in spec] + [r["id"] for r in redraw] + [cid for _l, cid in tiles]
    if len(set(ids)) != len(ids):
        raise ValueError("%s: two controls or tiles share an id: %s" % (kit, sorted(i for i in ids if ids.count(i) > 1)))
    script = (RATIONAL_JS + PH_CORE_JS + mode_js
              + cfg_literal("PRESETS", table) + cfg_literal("SPEC", spec)
              + cfg_literal("TILES", [cid for _label, cid in tiles])
              + cfg_literal("REDRAW", redraw_js) + cfg_literal("FIXED", fixed)
              + cfg_literal("VIEW", view)
              + PH_WIRE_JS % {"p": prefix, "fn": fn})
    return Lab(title=plain(cfg, kit, "title", title), subtitle=subtitle,
               markup=markup_html(prefix, title, subtitle, figure=figure), controls=controls, script=script,
               panel_title=plain(cfg, kit, "panel_title", panel_title),
               panel_intro=plain(cfg, kit, "panel_intro", panel_intro, limit=1200),
               expect={prefix + "Preset": expect})


__all__ = ["PH_CORE_JS", "PH_WIRE_JS", "UNITS", "ANGLES", "COMPASS", "DIRS", "rparse", "ftext", "parse",
           "parse_scalar", "parse_dir", "to_text", "presets", "pick_view", "plain", "attr", "select_html",
           "text_html", "range_html", "kpis_html", "markup_html", "camel", "mode_lab"]
