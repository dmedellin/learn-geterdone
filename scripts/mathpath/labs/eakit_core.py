"""eakit_core -- what every mode of the Enterprise Patterns kit shares.

Specified in docs/enterprise-patterns/PLAN.md section D (D.0 conventions, D.1
the eight modes, D.2 what the kit must never do, D.3 the build-time checks).
The report an author configures a lesson from is
docs/enterprise-patterns/kit-report.md.

JavaScript:

  EA_CORE_JS   shipped on every eakit page after RATIONAL_JS:
    eaInt(n)            "2,692,537", "−1" (thousands grouped, U+2212)
    eaNum(r)            "7/2 = 3.50", "51,033/500 ≈ 102.07", "−29/15 ≈ −1.93",
                        "4,000": two places, half away from zero on the exact
                        value, "=" only when those places are exact, both parts
                        of the fraction grouped; past 30 digits "≈ 1.80 × 10^40"
    eaPct(r)            "9/10 = 90%", "2/3 ≈ 66.7%", "1 = 100%", "0 = 0%"
    eaTimes(r)          "10×", "125/37 ≈ 3.4×" (one place, D.0)
    eaSigned(n)         "+1", "−1", "0"
    eaNames, eaCount    "a, b" / "none";  "2: david, martin" / "0: none"
    eaRead(spec, raw)   parse every input of a view; THROWS a sentence
    eaTableHtml(t)      the table under the tiles
  EA_WIRE_JS   the page wiring (preset menu, inputs, redraw)

Python:

  parse(where, f, text)       the build-time mirror of eaRead for one field
  to_text(where, f, value)    a preset value -> the exact text its box holds
  build_lab(cfg, ...)         the whole Lab for one mode and view

A mode supplies one pure JS function <xx>Compute(view, inst, opts) returning
{tiles: {id: text}, status: text, table: {caption, head, rows} | null} or
{refuse: sentence}. It is what scripts/mathcheck.js calls. A view's Python
`check(where, inst, fixed)` mirrors every refusal its JS makes beyond the field
parser (D.3), so a preset the page would refuse fails the build instead.
"""

import html
import re
from fractions import Fraction

from .algebra_core import RATIONAL_JS
from .common import Lab, cfg_literal

LIMIT = 10 ** 7          # D.0: a whole-number field is at most 10,000,000
MAX_RECORDS = 60         # D.0: at most 60 records per input
DECIMALS = 6             # the most decimal places a number may carry

# ---------------------------------------------------------------------------
# JavaScript shared by every eakit page
# ---------------------------------------------------------------------------

EA_CORE_JS = r"""
  /* eakit's printing and parsing (docs/enterprise-patterns/PLAN.md D.0). A
     parse THROWS an Error whose message is a sentence for the reader; the
     wiring paints it red and blanks the tiles. Every figure is exact: a
     rational over BigInt, a count or a list. Nothing typed is evaluated. */
  var EA_DASH = '—', EA_MINUS = '−';
  function eaEsc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }
  function eaClean(text) { return String(text === null || text === undefined ? '' : text).replace(/−/g, '-').trim(); }
  function eaGroup(digits) { return digits.replace(/\B(?=(\d{3})+$)/g, ','); }
  function eaInt(n) { n = BigInt(n); return (n < 0n ? EA_MINUS : '') + eaGroup(String(n < 0n ? -n : n)); }
  function eaFrac(r) { return eaInt(r.n) + '/' + eaInt(r.d); }
  /* Exactly `places` decimals, half away from zero, on the exact value. */
  function eaFixed(r, places) {
    var neg = r.n < 0n, num = neg ? -r.n : r.n, scale = 10n ** BigInt(places);
    var q = (num * scale * 2n / r.d + 1n) / 2n, s = q.toString();
    while (s.length <= places) s = '0' + s;
    return (neg && q !== 0n ? EA_MINUS : '') + eaGroup(s.slice(0, s.length - places))
      + (places > 0 ? '.' + s.slice(s.length - places) : '');
  }
  function eaExactAt(r, places) { return (r.n * 10n ** BigInt(places)) % r.d === 0n; }
  function eaDigits(n) { return String(n < 0n ? -n : n).length; }
  function eaBig(r) { return eaDigits(r.n) > 30 || eaDigits(r.d) > 30; }
  /* A figure too long to print: three significant figures and a power of ten. */
  function eaSci(r) {
    var a = Rabs(r), e = eaDigits(a.n) - eaDigits(a.d);
    var ten = function (k) { return k >= 0 ? R(10n ** BigInt(k)) : R(1n, 10n ** BigInt(-k)); };
    if (Rcmp(a, ten(e)) < 0) e -= 1;
    var t = eaFixed(Rdiv(a, ten(e)), 2);
    if (t === '10.00') { t = '1.00'; e += 1; }
    return '≈ ' + (r.n < 0n ? EA_MINUS : '') + t + ' × 10^' + (e < 0 ? EA_MINUS + (-e) : e);
  }
  function eaNum(r) {
    if (eaBig(r)) return eaSci(r);
    if (Rint(r)) return eaInt(r.n);
    return eaFrac(r) + (eaExactAt(r, 2) ? ' = ' : ' ≈ ') + eaFixed(r, 2);
  }
  function eaPct(r) {
    var p = Rmul(r, R(100n)), exact = Rint(p) || eaExactAt(p, 1);
    var d = (Rint(p) ? eaInt(p.n) : eaFixed(p, 1)) + '%';
    if (eaBig(r)) return (exact ? '= ' : '≈ ') + d;
    return (Rint(r) ? eaInt(r.n) : eaFrac(r)) + (exact ? ' = ' : ' ≈ ') + d;
  }
  /* A ratio: whole as "10×", else the fraction and one place, always "≈" (D.0). */
  function eaTimes(r) {
    if (eaBig(r)) return eaSci(r) + '×';
    return Rint(r) ? eaInt(r.n) + '×' : eaFrac(r) + ' ≈ ' + eaFixed(r, 1) + '×';
  }
  function eaSigned(n) { n = BigInt(n); return (n > 0n ? '+' : '') + eaInt(n); }
  function eaNames(list) { return list.length ? list.join(', ') : 'none'; }
  function eaCount(list) { return list.length + ': ' + eaNames(list); }
  function eaPlural(n, one, many) { return eaInt(n) + ' ' + (BigInt(n) === 1n ? one : many); }
  function eaSum(v) { var s = R0; v.forEach(function (x) { s = Radd(s, x); }); return s; }
  /* floor and ceiling of a rational, as BigInt */
  function eaFloor(r) { var q = r.n / r.d; return (r.n < 0n && q * r.d !== r.n) ? q - 1n : q; }
  function eaCeil(r) { return -eaFloor(Rneg(r)); }
  /* A refusal raised inside a view: <xx>Compute turns it into {refuse}. Any
     other error is a bug and is not swallowed. */
  function eaRefuse(why) { var e = new Error(why); e.eaRefuse = true; throw e; }
  function eaRun(fn, inst, opts) {
    try { return fn(inst, opts || {}); } catch (e) { if (e && e.eaRefuse) return { refuse: e.message }; throw e; }
  }
  function eaWhole(r) { return Number(r.n); }
  function eaSort(list) { return list.slice().sort(function (a, b) { return a < b ? -1 : (a > b ? 1 : 0); }); }

  /* --- reading the inputs (D.0) ------------------------------------------ */
  var EA_NAME = /^[A-Za-z0-9._-]+$/, EA_NUMBER = /^-?(?:\d+(?:\.(\d+))?|\.(\d+))$/;
  function eaQuote(s) { s = String(s); return '"' + (s.length > 40 ? s.slice(0, 40) + '…' : s) + '"'; }
  function eaBound(f, key) { return f[key] === undefined ? undefined : Rparse(f[key]); }
  function eaScalar(f, text, what) {
    var s = eaClean(text), m, r, lo, hi;
    switch (f.kind) {
      case 'name':
      case 'parent':
        if (s === '') throw new Error(what + ' is empty');
        if (s === '-') {
          if (f.kind === 'parent') return s;
          throw new Error(what + ' cannot be "-", which marks none');
        }
        if (!EA_NAME.test(s)) throw new Error(what + ' ' + eaQuote(s) + ' should be letters, digits, dots, hyphens or underscores');
        return s;
      case 'word':
        if (f.words.indexOf(s) < 0) throw new Error(what + ' should be one of ' + f.words.join(', ') + ', not ' + eaQuote(s));
        return s;
      case 'whole':
        if (s === '') throw new Error(what + ' is empty');
        if (!/^-?\d+$/.test(s)) throw new Error(what + ' should be a whole number, and ' + eaQuote(s) + ' is not one');
        r = R(BigInt(s));
        lo = eaBound(f, 'min'); hi = eaBound(f, 'max');
        if (Rcmp(r, lo) < 0 || Rcmp(r, hi) > 0) {
          throw new Error(what + ' is a whole number from ' + eaNum(lo) + ' to ' + eaNum(hi) + ', and it is ' + eaNum(r));
        }
        return r;
      case 'num':
        if (s === '') throw new Error(what + ' is empty');
        m = EA_NUMBER.exec(s);
        if (!m) throw new Error(what + ' should be a number such as 3 or 0.25 (no fractions or exponents), and ' + eaQuote(s) + ' is not one');
        if ((m[1] || m[2] || '').length > 6) throw new Error(what + ' has more than 6 decimal places');
        r = Rparse(s);
        m = s.replace('-', EA_MINUS);
        if (f.gt !== undefined && Rcmp(r, Rparse(f.gt)) <= 0) throw new Error(what + ' must be more than ' + eaNum(Rparse(f.gt)) + ', and it is ' + m);
        if (f.min !== undefined && Rcmp(r, Rparse(f.min)) < 0) throw new Error(what + ' cannot be less than ' + eaNum(Rparse(f.min)) + ', and it is ' + m);
        if (Rcmp(r, Rparse(f.max)) > 0) throw new Error(what + ' is at most ' + eaNum(Rparse(f.max)) + ', and it is ' + m);
        return r;
    }
    throw new Error(what + ': no such kind of field');
  }
  function eaSized(n, f, what, things) {
    if (n < f.lo) throw new Error(what + (n === 0 ? ' is empty' : ': this lab needs at least ' + f.lo + ' ' + things + ', and there ' + (n === 1 ? 'is 1' : 'are ' + n)));
    if (n > f.hi) throw new Error(what + ': this lab takes at most ' + f.hi + ' ' + things + ', and there are ' + n);
  }
  function eaRecords(text, f, what) {
    var s = eaClean(text), rows = s === '' ? [] : s.split(';').map(function (r) { return r.trim(); });
    if (rows.length && rows[rows.length - 1] === '') rows.pop();
    eaSized(rows.length, f, what, 'records');
    var seen = {};
    return rows.map(function (row, i) {
      var cells = row.split(',').map(function (c) { return c.trim(); });
      if (cells.length !== f.sub.length) {
        throw new Error(what + ': record ' + (i + 1) + ' has ' + cells.length + ' field' + (cells.length === 1 ? '' : 's')
          + '; this list needs ' + f.sub.length + ' (' + f.sub.map(function (k) { return k[0]; }).join(', ') + ')');
      }
      var rec = {};
      f.sub.forEach(function (k, j) { rec[k[0]] = eaScalar(k[1], cells[j], what + ', record ' + (i + 1) + ': ' + k[0]); });
      if (f.unique) {
        if (Object.prototype.hasOwnProperty.call(seen, cells[0])) throw new Error(what + ' names ' + eaQuote(cells[0]) + ' twice');
        seen[cells[0]] = true;
      }
      return rec;
    });
  }
  /* "class=node; class=node": optional, '' is none. */
  function eaPairs(text, f, what) {
    var s = eaClean(text), out = [], parts = s === '' ? [] : s.split(';');
    parts.forEach(function (part, i) {
      part = part.trim();
      if (part === '' && i === parts.length - 1) return;
      var m = /^([^=\s]+)\s*=\s*([^=\s]+)$/.exec(part);
      if (!m || !EA_NAME.test(m[1]) || !EA_NAME.test(m[2]) || m[1] === '-' || m[2] === '-') {
        throw new Error(what + ': ' + eaQuote(part) + ' should be ' + f.shape + ', two names joined by =');
      }
      if (out.some(function (o) { return o.a === m[1]; })) throw new Error(what + ' names ' + eaQuote(m[1]) + ' twice');
      out.push({ a: m[1], b: m[2] });
    });
    if (out.length > f.hi) throw new Error(what + ': this lab takes at most ' + f.hi + ', and there are ' + out.length);
    return out;
  }
  /* Names or wholes separated by spaces (or commas). */
  function eaList(text, f, what) {
    var s = eaClean(text), toks = s === '' ? [] : s.split(/[\s,]+/).filter(function (t) { return t !== ''; });
    eaSized(toks.length, f, what, f.things);
    var vals = toks.map(function (t, i) { return eaScalar(f.each, t, what + ', entry ' + (i + 1)); });
    if (f.each.kind === 'name') {
      toks.forEach(function (t, i) { if (toks.indexOf(t) !== i) throw new Error(what + ' names ' + eaQuote(t) + ' twice'); });
    }
    return vals;
  }
  function eaField(f, text) {
    if (f.kind === 'rec') return eaRecords(text, f, f.what);
    if (f.kind === 'pairs') return eaPairs(text, f, f.what);
    if (f.kind === 'list') return eaList(text, f, f.what);
    return eaScalar(f, text, f.what);
  }
  function eaRead(spec, raw) {
    var out = {};
    spec.forEach(function (f) { out[f.key] = eaField(f, raw[f.key]); });
    return out;
  }

  /* head: header texts; rows: rows of cells, each text. */
  function eaTableHtml(t) {
    var h = '<caption>' + eaEsc(t.caption) + '</caption><thead><tr>'
      + t.head.map(function (x) { return '<th scope="col">' + eaEsc(x) + '</th>'; }).join('') + '</tr></thead><tbody>';
    t.rows.forEach(function (row) {
      h += '<tr>' + row.map(function (cell) { return '<td>' + eaEsc(cell) + '</td>'; }).join('') + '</tr>';
    });
    return h + '</tbody>';
  }
"""

EA_WIRE_JS = r"""
  function eaEl(id) { return document.getElementById(id); }
  var eaPresetS = eaEl('%P%Preset'), eaStatusEl = eaEl('%P%Status'), eaTableEl = eaEl('%P%Table');
  function eaRed(why) {
    TILES.forEach(function (id) { eaEl(id).textContent = EA_DASH; });
    eaTableEl.innerHTML = '';
    eaStatusEl.innerHTML = '<span class="tone-red">' + eaEsc(String(why).replace(/\.$/, '')) + '.</span>';
  }
  function eaRedraw() {
    var raw = {}, inst, out;
    SPEC.forEach(function (f) { raw[f.key] = eaEl(f.id).value; });
    try { inst = eaRead(SPEC, raw); } catch (err) { eaRed(err.message); return; }
    out = %FN%(VIEW, inst, FIXED);
    if (out.refuse) { eaRed(out.refuse); return; }
    TILES.forEach(function (id) { eaEl(id).textContent = out.tiles[id] === undefined ? EA_DASH : out.tiles[id]; });
    eaTableEl.innerHTML = out.table ? eaTableHtml(out.table) : '';
    eaStatusEl.textContent = out.status;
  }
  function eaFill(id) {
    var inst = PRESETS[id];
    if (!inst) return false;
    SPEC.forEach(function (f) { if (inst[f.key] !== undefined) eaEl(f.id).value = inst[f.key]; });
    return true;
  }
  eaPresetS.addEventListener('change', function () { if (eaFill(eaPresetS.value)) eaRedraw(); });
  SPEC.forEach(function (f) {
    eaEl(f.id).addEventListener(f.control === 'select' ? 'change' : 'input', eaRedraw);
  });
  eaFill(eaPresetS.value);
  eaRedraw();
  window.redrawLab = eaRedraw;
"""

# ---------------------------------------------------------------------------
# Python: the build-time mirror of eaRead (D.3)
# ---------------------------------------------------------------------------

_NAME = re.compile(r"^[A-Za-z0-9._-]+$")
_NUMBER = re.compile(r"^-?(?:\d+(?:\.(\d+))?|\.(\d+))$")


def grp(n):
    """eaInt: thousands grouped, U+2212 for a minus."""
    s = "{:,}".format(abs(int(n)))
    return ("−" + s) if n < 0 else s


def ftext(f):
    """eaNum, enough for a refusal sentence: a whole number or a decimal."""
    f = Fraction(f)
    if f.denominator == 1:
        return grp(f.numerator)
    return "%s/%s" % (grp(f.numerator), grp(f.denominator))


def _quote(s):
    s = str(s)
    return '"%s"' % (s[:40] + "…" if len(s) > 40 else s)


def parse_scalar(f, text, what):
    s = str(text).replace("−", "-").strip()
    k = f["kind"]
    if k in ("name", "parent"):
        if s == "":
            raise ValueError("%s is empty" % what)
        if s == "-":
            if k == "parent":
                return s
            raise ValueError('%s cannot be "-", which marks none' % what)
        if not _NAME.match(s):
            raise ValueError("%s %s should be letters, digits, dots, hyphens or underscores" % (what, _quote(s)))
        return s
    if k == "word":
        if s not in f["words"]:
            raise ValueError("%s should be one of %s, not %s" % (what, ", ".join(f["words"]), _quote(s)))
        return s
    if k == "whole":
        if s == "":
            raise ValueError("%s is empty" % what)
        if not re.fullmatch(r"-?\d+", s):
            raise ValueError("%s should be a whole number, and %s is not one" % (what, _quote(s)))
        r = int(s)
        lo, hi = int(f["min"]), int(f["max"])
        if not lo <= r <= hi:
            raise ValueError("%s is a whole number from %s to %s, and it is %s" % (what, grp(lo), grp(hi), grp(r)))
        return Fraction(r)
    if k == "num":
        if s == "":
            raise ValueError("%s is empty" % what)
        m = _NUMBER.match(s)
        if not m:
            raise ValueError("%s should be a number such as 3 or 0.25 (no fractions or exponents), and %s is not one"
                             % (what, _quote(s)))
        if len(m.group(1) or m.group(2) or "") > DECIMALS:
            raise ValueError("%s has more than 6 decimal places" % what)
        r, typed = Fraction(s), s.replace("-", "\u2212")
        if "gt" in f and r <= Fraction(f["gt"]):
            raise ValueError("%s must be more than %s, and it is %s" % (what, ftext(Fraction(f["gt"])), typed))
        if "min" in f and r < Fraction(f["min"]):
            raise ValueError("%s cannot be less than %s, and it is %s" % (what, ftext(Fraction(f["min"])), typed))
        if r > Fraction(f["max"]):
            raise ValueError("%s is at most %s, and it is %s" % (what, ftext(Fraction(f["max"])), typed))
        return r
    raise ValueError("%s: no such kind of field %r" % (what, k))


def _sized(n, f, what, things):
    if n < f["lo"]:
        raise ValueError("%s is empty" % what if n == 0 else
                         "%s: this lab needs at least %d %s, and there %s" % (what, f["lo"], things,
                                                                             "is 1" if n == 1 else "are %d" % n))
    if n > f["hi"]:
        raise ValueError("%s: this lab takes at most %d %s, and there are %d" % (what, f["hi"], things, n))


def parse(where, f, text):
    """Mirror of eaField for one field, at build time; raises naming `where`."""
    try:
        return _parse(f, text)
    except ValueError as exc:
        raise ValueError("%s: %s" % (where, exc)) from None


def _parse(f, text):
    what = f["what"]
    s = str(text).replace("−", "-").strip()
    if f["kind"] == "rec":
        rows = [r.strip() for r in s.split(";")] if s else []
        if rows and rows[-1] == "":
            rows.pop()
        _sized(len(rows), f, what, "records")
        out, seen = [], set()
        for i, row in enumerate(rows):
            cells = [c.strip() for c in row.split(",")]
            if len(cells) != len(f["sub"]):
                raise ValueError("%s: record %d has %d field%s; this list needs %d (%s)"
                                 % (what, i + 1, len(cells), "" if len(cells) == 1 else "s", len(f["sub"]),
                                    ", ".join(k for k, _ in f["sub"])))
            rec = {}
            for j, (key, kk) in enumerate(f["sub"]):
                rec[key] = parse_scalar(kk, cells[j], "%s, record %d: %s" % (what, i + 1, key))
            if f.get("unique"):
                if cells[0] in seen:
                    raise ValueError("%s names %s twice" % (what, _quote(cells[0])))
                seen.add(cells[0])
            out.append(rec)
        return out
    if f["kind"] == "pairs":
        out = []
        parts = s.split(";") if s else []
        for i, part in enumerate(parts):
            part = part.strip()
            if part == "" and i == len(parts) - 1:
                continue
            m = re.fullmatch(r"([^=\s]+)\s*=\s*([^=\s]+)", part)
            if not m or not _NAME.match(m.group(1)) or not _NAME.match(m.group(2)) or "-" in (m.group(1), m.group(2)):
                raise ValueError("%s: %s should be %s, two names joined by =" % (what, _quote(part), f["shape"]))
            if any(a == m.group(1) for a, _b in out):
                raise ValueError("%s names %s twice" % (what, _quote(m.group(1))))
            out.append((m.group(1), m.group(2)))
        if len(out) > f["hi"]:
            raise ValueError("%s: this lab takes at most %d, and there are %d" % (what, f["hi"], len(out)))
        return out
    if f["kind"] == "list":
        toks = [t for t in re.split(r"[\s,]+", s) if t] if s else []
        _sized(len(toks), f, what, f["things"])
        vals = [parse_scalar(f["each"], t, "%s, entry %d" % (what, i + 1)) for i, t in enumerate(toks)]
        if f["each"]["kind"] == "name":
            for i, t in enumerate(toks):
                if toks.index(t) != i:
                    raise ValueError("%s names %s twice" % (what, _quote(t)))
        return vals
    return parse_scalar(f, s, what)


def _decimal(where, what, f):
    """A Fraction as the decimal a box holds; refused when it does not terminate in 6 places."""
    f = Fraction(f)
    scaled = f * 10 ** DECIMALS
    if scaled.denominator != 1:
        raise ValueError("%s: %s %s has no decimal of at most 6 places; give it as a string" % (where, what, f))
    n = abs(scaled.numerator)
    whole, frac = divmod(n, 10 ** DECIMALS)
    text = str(whole) + ("." + ("%06d" % frac).rstrip("0") if frac else "")
    return ("-" if f < 0 else "") + text


def _part(where, what, v):
    if isinstance(v, bool):
        return "yes" if v else "no"
    if isinstance(v, int):
        return str(v)
    if isinstance(v, Fraction):
        return _decimal(where, what, v)
    if isinstance(v, str):
        return v.strip()
    raise ValueError("%s: %s cannot hold %r" % (where, what, v))


def to_text(where, f, value):
    """A preset's value for one field -> the exact text its box holds.

    A string is taken as typed (trimmed). An int prints as it is, a Fraction
    as its decimal. A record field also takes a list of records, each a list
    of parts or a string; a list field a list; a pairs field a dict.
    """
    what = f["what"]
    if isinstance(value, str):
        text = value.strip()
    elif f["kind"] == "rec" and isinstance(value, (list, tuple)):
        text = "; ".join(r.strip() if isinstance(r, str) else ", ".join(_part(where, what, p) for p in r)
                         for r in value)
    elif f["kind"] == "list" and isinstance(value, (list, tuple)):
        text = " ".join(_part(where, what, p) for p in value)
    elif f["kind"] == "pairs" and isinstance(value, dict):
        text = "; ".join("%s=%s" % (a, b) for a, b in value.items())
    elif isinstance(value, (bool, int, Fraction)):
        text = _part(where, what, value)
    else:
        raise ValueError("%s: %s cannot be %r" % (where, what, value))
    if re.search(r'[<>&"]', text):
        raise ValueError("%s: %s %r contains < > & or a quote, which no shipped value may" % (where, what, text))
    parse(where, f, text)
    return text


# ---------------------------------------------------------------------------
# Python: presets, markup and the Lab
# ---------------------------------------------------------------------------


def presets(cfg, kit, fields, tiles, check, fixed):
    """(instance table, menu pairs, expect by preset id, the chosen id).

    fields: [(key, spec, default)]. A cfg key named like a field supplies it to
    every preset that does not set it (D.0). A preset key that is not an input
    of the view raises, naming the inputs; so does an expectation naming a tile
    the view does not show, and so does anything the page itself would refuse
    (the field parser's mirror, then the view's own `check`).
    """
    plist = cfg.get("presets")
    if not isinstance(plist, list) or not plist:
        raise ValueError("%s: cfg['presets'] must be a non-empty list of instances" % kit)
    known = {key for key, _s, _d in fields} | {"id", "label", "expect"}
    tile_ids = [cid for _l, cid in tiles]
    table, menu, expect = {}, [], {}
    for p in plist:
        pid = p.get("id") if isinstance(p, dict) else None
        if not isinstance(pid, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", pid):
            raise ValueError("%s: every preset needs an id of lowercase letters, digits and hyphens, not %r" % (kit, pid))
        where = "%s preset %r" % (kit, pid)
        if pid in table:
            raise ValueError("%s: the id is used twice" % where)
        label = p.get("label")
        if not isinstance(label, str) or not label.strip() or re.search(r"[<>&]", label):
            raise ValueError("%s: needs a plain-text label" % where)
        extra = sorted(set(p) - known)
        if extra:
            raise ValueError("%s: %s %s not an input of this view (its inputs are %s)"
                             % (where, ", ".join(extra), "is" if len(extra) == 1 else "are",
                                ", ".join(k for k, _s, _d in fields)))
        exp = p.get("expect") or {}
        if not isinstance(exp, dict) or any(k not in tile_ids or not isinstance(v, str) for k, v in exp.items()):
            raise ValueError("%s: expect maps this view's tile ids (%s) to the exact text printed"
                             % (where, ", ".join(tile_ids)))
        inst, parsed = {}, {}
        for key, spec, default in fields:
            value = p.get(key, cfg.get(key, default))
            if value is None:
                raise ValueError("%s: needs %s" % (where, key))
            inst[key] = to_text(where, spec, value)
            parsed[key] = parse(where, spec, inst[key])
        if check:
            try:
                check(parsed, fixed)
            except ValueError as exc:
                raise ValueError("%s: %s" % (where, exc)) from None
        table[pid] = inst
        menu.append((pid, label.strip()))
        expect[pid] = dict(exp)
    chosen = cfg.get("preset", plist[0]["id"])
    if chosen not in table:
        raise ValueError("%s: cfg['preset'] %r is not one of the presets (%s)" % (kit, chosen, ", ".join(table)))
    return table, menu, expect, chosen


def plain(cfg, kit, key, default, limit=200):
    """A lesson-level text value: plain, short, no markup."""
    v = cfg.get(key, default)
    if not isinstance(v, str) or re.search(r"[<>&]", v) or len(v) > limit:
        raise ValueError("%s: cfg[%r] should be plain text of at most %d characters, not %r" % (kit, key, limit, v))
    return v


def attr(text):
    return html.escape(str(text), quote=True)


def esc(text):
    return html.escape(str(text), quote=False)


def camel(prefix, key):
    """An input's id: prefix + 'In' + the key with its first letter capitalised ('rr', 'latencyMs' -> 'rrInLatencyMs')."""
    return prefix + "In" + key[:1].upper() + key[1:]


def select_html(cid, label, options, chosen):
    opts = "".join('<option value="%s"%s>%s</option>' % (attr(v), " selected" if v == chosen else "", esc(t))
                   for v, t in options)
    return ('        <div class="field">\n          <label for="%s">%s</label>\n'
            '          <select id="%s">%s</select>\n        </div>\n' % (cid, esc(label), cid, opts))


def text_html(cid, label, value):
    return ('        <div class="field">\n          <label for="%s">%s</label>\n'
            '          <input id="%s" type="text" value="%s" inputmode="text" autocomplete="off" spellcheck="false">\n'
            "        </div>\n" % (cid, esc(label), cid, attr(value)))


def area_html(cid, label, value, rows):
    """A record list: a box that wraps, so a long list reads at phone width."""
    return ('        <div class="field">\n          <label for="%s">%s</label>\n'
            '          <textarea id="%s" rows="%d" spellcheck="false" autocomplete="off" autocapitalize="off" '
            'style="width:100%%;box-sizing:border-box;font-family:var(--mono);font-size:0.85rem;line-height:1.5;">'
            "%s</textarea>\n        </div>\n" % (cid, esc(label), cid, rows, esc(value)))


def kpis_html(items):
    cells = "".join('          <div class="kpi"><span>%s</span><strong id="%s">&mdash;</strong></div>\n'
                    % (esc(label), cid) for label, cid in items)
    return '        <div class="kpi-grid">\n%s        </div>\n' % cells


def markup_html(prefix, name, subtitle, rules):
    return ('      <div class="lab-toolbar">\n'
            '        <div class="lab-title"><strong>%s</strong><span>%s</span></div>\n'
            "      </div>\n" % (esc(name), esc(subtitle))
            + '      <div class="status-banner" id="%sStatus" style="margin-top:12px;" aria-live="polite"></div>\n' % prefix
            + '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="%sTable"></table></div>\n'
            % prefix
            + '      <p class="small-copy" style="margin-top:12px;"><strong>How the lab counts.</strong> %s</p>\n'
            % esc(rules))


FAMILY = {
    1: "A count over the situation the lesson states.",
    2: "The arithmetic of the figures the lesson states (marked with their source).",
}

COMMON_CFG = {"mode", "view", "presets", "preset", "title", "panel_title", "panel_intro"}

_COMMENT_LINES = re.compile(r"^[ \t]*/\*(?:(?!\*/).)*\*/[ \t]*\n", re.S | re.M)


def build_lab(cfg, *, kit, prefix, view, fields, tiles, fn, js, fixed, title, subtitle, family, intro, rules,
              extra_keys=(), check=None):
    """One mode, one view, as a Lab.

    fields: [(key, spec, default)] in display order; spec["what"] is the label
            and spec["control"] one of "text", "area" (a record list) or
            "select" (spec["words"] its options). Every input's id is
            prefix + 'In' + Key.
    tiles:  [(label, id)].
    fixed:  the lesson-level values handed to the compute function as opts.
    rules:  the sentence(s) stating how the view counts, always on the page.
    check:  check(parsed inputs, fixed) raises ValueError on what the page
            would refuse beyond the field parser (D.3).
    """
    allowed = COMMON_CFG | set(extra_keys) | {key for key, _s, _d in fields}
    if family == 2:
        allowed |= {"source"}
    stray = sorted(set(cfg) - allowed)
    if stray:
        raise ValueError("%s: cfg sets %s, which this view does not take (it takes %s)"
                         % (kit, ", ".join(stray), ", ".join(sorted(allowed))))
    table, menu, expect, chosen = presets(cfg, kit, fields, tiles, check, fixed)
    here = table[chosen]
    spec, controls = [], select_html(prefix + "Preset", "Worked example", menu, chosen)
    for key, fspec, _default in fields:
        cid = camel(prefix, key)
        spec.append(dict(fspec, key=key, id=cid))
        if fspec["control"] == "select":
            controls += select_html(cid, fspec["what"], [(w, w) for w in fspec["words"]], here[key])
        elif fspec["control"] == "area":
            controls += area_html(cid, fspec["what"], here[key], fspec.get("rows", 3))
        else:
            controls += text_html(cid, fspec["what"], here[key])
    controls += kpis_html(tiles)
    ids = [s["id"] for s in spec] + [cid for _l, cid in tiles] + [prefix + x for x in ("Preset", "Status", "Table")]
    if len(set(ids)) != len(ids):
        raise ValueError("%s: two controls or tiles share an id: %s" % (kit, sorted({i for i in ids if ids.count(i) > 1})))
    script = (RATIONAL_JS + EA_CORE_JS + js
              + cfg_literal("PRESETS", table) + cfg_literal("SPEC", spec)
              + cfg_literal("TILES", [cid for _label, cid in tiles])
              + cfg_literal("FIXED", fixed) + cfg_literal("VIEW", view)
              + EA_WIRE_JS.replace("%P%", prefix).replace("%FN%", fn))
    script = _COMMENT_LINES.sub("", script)
    panel_intro = plain(cfg, kit, "panel_intro", intro, limit=1200)
    if FAMILY[family] not in panel_intro:
        panel_intro = FAMILY[family] + " " + panel_intro
    if family == 2 and cfg.get("source"):
        panel_intro = panel_intro.rstrip() + " Figures: %s." % plain(cfg, kit, "source", "", limit=300).strip().rstrip(".")
    title = plain(cfg, kit, "title", title)
    return Lab(title=title, subtitle=subtitle,
               markup=markup_html(prefix, title, subtitle, rules), controls=controls, script=script,
               panel_title=plain(cfg, kit, "panel_title", "Change the inputs, or choose a worked example"),
               panel_intro=panel_intro, expect={prefix + "Preset": expect})


# --- field specs every mode builds from ------------------------------------

def whole(lo=0, hi=LIMIT):
    return {"kind": "whole", "min": str(lo), "max": str(hi)}


def num(gt=None, lo=None, hi=LIMIT):
    f = {"kind": "num", "max": str(hi)}
    if gt is not None:
        f["gt"] = str(gt)
    if lo is not None:
        f["min"] = str(lo)
    return f


NAME = {"kind": "name"}
PARENT = {"kind": "parent"}
YESNO = {"kind": "word", "words": ["yes", "no"]}


def word(*words):
    return {"kind": "word", "words": list(words)}


def rec(what, sub, unique=False, rows=3, lo=1, hi=MAX_RECORDS):
    return {"kind": "rec", "what": what, "control": "area", "rows": rows, "sub": [list(s) for s in sub],
            "lo": lo, "hi": hi, "unique": unique}


def field(what, spec):
    return dict(spec, what=what, control="text")


def choice(what, *words):
    return {"kind": "word", "words": list(words), "what": what, "control": "select"}


def pairs(what, shape):
    return {"kind": "pairs", "what": what, "control": "text", "shape": shape, "hi": MAX_RECORDS}


__all__ = ["EA_CORE_JS", "EA_WIRE_JS", "FAMILY", "LIMIT", "MAX_RECORDS", "parse", "parse_scalar", "to_text",
           "presets", "plain", "camel", "build_lab", "esc", "grp", "whole", "num", "NAME", "PARENT", "YESNO",
           "word", "rec", "field", "choice", "pairs"]
