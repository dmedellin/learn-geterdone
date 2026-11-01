"""acckit -- the lab kit of Accelerate, Read Along.

Specified in docs/accelerate/PLAN.md sections 0 and D; the report an author
configures a lesson from is docs/accelerate/kit-report.md, and the seam
between this module and acckit_b.py is docs/accelerate/kit-contract.md.
Built on eakit_core (imported as `ea`, unchanged): its field parser, printers,
markup and wiring, with field kinds of this kit's own (a time cell, a
rational cell, records with a variable tail, lists of either) read by
`aktRead` before eakit's `eaField`.

Family A (this module), delivery, flow and practice:

  delivery  (ade)  metrics, cluster
  flow      (afl)  utilization, batch, wip
  branches  (atb)  trunk
  release   (arl)  independent, scaling
  change    (acm)  approval
  work      (awk)  split

Family B (acckit_b.py): likert, stats, validity, groups, sample, capability.
`acckit_lab` dispatches them through `acckit_b.MODES`, imported lazily so this
module imports before acckit_b.py exists.

THE BUILDER SIGNATURE (both families). A mode is built by
`builder(cfg) -> common.Lab`, where cfg is the lesson's lab cfg as written
(cfg["mode"] names the mode). Every builder in this kit is
`lambda cfg: mode_lab(cfg, <mode>, <SPEC>)`. The first view is the default.
A page ships RATIONAL_JS, EA_CORE_JS, AKT_CORE_JS, its mode's base block and
its own view's block -- never the other views or modes (page weight).

IDS. PLAN section D's prefixes, unchanged (grepped against
scripts/mathpath/labs/*.py and scripts/*.js on 2026-11-01). Shared helpers
begin akt / AKT_.

EXACTNESS. Every figure is a count, a list, or an exact BigInt rational; a
square root is printed to stated places from the exact rational under it by
an integer square root (aktSqrtFixed). Nothing typed is evaluated as script.
"""

import math
import re
from fractions import Fraction

from . import eakit_core as ea
from .algebra_core import RATIONAL_JS
from .common import Lab, cfg_literal

KIT = "acckit"
CAUTION = "the figure is of the sample stated"
FAMILY_SENTENCE = "A figure computed from the small sample the lesson states."

# ---------------------------------------------------------------------------
# Shared JavaScript, on every acckit page (both families)
# ---------------------------------------------------------------------------

AKT_CORE_JS = r"""
  /* acckit's shared helpers (docs/accelerate/kit-contract.md section 3a). */
  var AKT_CAUTION = 'the figure is of the sample stated';
  var AKT_TIME = /^(\d{1,3})\.(\d{1,2}):(\d{2})$/;
  function aktStatus(s) { return String(s).replace(/[.\s]+$/, '') + '; ' + AKT_CAUTION + '.'; }
  function aktListed(n, parts, sep) { return n === 0 ? '0: none' : eaInt(n) + ': ' + parts.join(sep || ', '); }
  /* A rational that has a finite decimal, as typed: 3, 0.25, −1.5 (no grouping). */
  function aktDec(r) {
    var neg = r.n < 0n, n = neg ? -r.n : r.n, whole = n / r.d, rem = n % r.d, frac = '', i;
    for (i = 0; i < 12 && rem !== 0n; i += 1) { rem *= 10n; frac += String(rem / r.d); rem %= r.d; }
    return (neg ? EA_MINUS : '') + String(whole) + (frac ? '.' + frac : '') + (rem !== 0n ? '…' : '');
  }
  /* floor(sqrt(n)) for a BigInt n >= 0, exactly. */
  function aktIsqrt(n) {
    if (n < 0n) throw new Error('aktIsqrt of a negative number');
    if (n < 2n) return n;
    var x = n, y = (x + 1n) / 2n;
    while (y < x) { x = y; y = (x + n / x) / 2n; }
    return x;
  }
  /* sqrt(r), r >= 0, to exactly `places` decimals, half up on the exact value:
     m = floor((isqrt(floor(4 r 10^(2p))) + 1) / 2) is round(sqrt(r) 10^p). */
  function aktSqrtFixed(r, places) {
    if (r.n < 0n) throw new Error('aktSqrtFixed of a negative number');
    var p = BigInt(places), s = aktIsqrt(4n * r.n * 10n ** (2n * p) / r.d), m = (s + 1n) / 2n, t = m.toString();
    while (t.length <= places) t = '0' + t;
    return eaGroup(t.slice(0, t.length - places)) + (places > 0 ? '.' + t.slice(t.length - places) : '');
  }
  function aktRootSigned(sign, sq, places) {
    var t = aktSqrtFixed(sq, places);
    return (sign < 0 && /[1-9]/.test(t) ? EA_MINUS : '') + t;
  }
  function aktSqrtExact(r) {
    if (r.n < 0n) return null;
    var a = aktIsqrt(r.n), b = aktIsqrt(r.d);
    return a * a === r.n && b * b === r.d ? R(a, b) : null;
  }
  function aktParseDec(text, what) {
    var s = eaClean(text), m = EA_NUMBER.exec(s);
    if (s === '') throw new Error(what + ' is empty');
    if (!m) throw new Error(what + ' should be a number such as 3 or 0.25 (no fractions or exponents), and ' + eaQuote(s) + ' is not one');
    if ((m[1] || m[2] || '').length > 6) throw new Error(what + ' has more than 6 decimal places');
    return Rparse(s);
  }
  function aktParseRat(text, what) {
    var s = eaClean(text), m = /^(-?\d+)\/(\d+)$/.exec(s);
    if (s === '') throw new Error(what + ' is empty');
    if (m) {
      if (/^0+$/.test(m[2])) throw new Error(what + ' ' + eaQuote(s) + ' divides by zero');
      if (m[1].replace('-', '').length > 8 || m[2].length > 8) throw new Error(what + ' ' + eaQuote(s) + ' has more than 8 digits above or below the line');
      return R(BigInt(m[1]), BigInt(m[2]));
    }
    m = EA_NUMBER.exec(s);
    if (!m) throw new Error(what + ' should be a number such as 3, 0.25 or 1/2, and ' + eaQuote(s) + ' is not one');
    if ((m[1] || m[2] || '').length > 6) throw new Error(what + ' has more than 6 decimal places');
    return Rparse(s);
  }
  function aktTime(text, what) {
    var s = eaClean(text), m = AKT_TIME.exec(s), r;
    if (s === '') throw new Error(what + ' is empty');
    if (m) {
      var d = BigInt(m[1]), h = BigInt(m[2]), mi = BigInt(m[3]);
      if (d < 1n || d > 366n) throw new Error(what + ' ' + eaQuote(s) + ': the day is from 1 to 366');
      if (h > 23n) throw new Error(what + ' ' + eaQuote(s) + ': the hour is from 00 to 23');
      if (mi > 59n) throw new Error(what + ' ' + eaQuote(s) + ': the minutes are from 00 to 59');
      return R((d - 1n) * 1440n + h * 60n + mi, 60n);
    }
    m = EA_NUMBER.exec(s);
    if (m && s.charAt(0) !== '-') {
      if ((m[1] || m[2] || '').length > 6) throw new Error(what + ' has more than 6 decimal places');
      r = Rparse(s);
      if (Rcmp(r, R(8784n)) > 0) throw new Error(what + ' is at most 8,784 hours (366 days), and it is ' + s);
      return r;
    }
    throw new Error(what + ' ' + eaQuote(s) + ' should be a time: day.hh:mm (1.09:30 is day 1 at 09:30) or hours from the start (37.5)');
  }
  function aktTimeText(h) {
    var m = Rmul(h, R(60n));
    if (!Rint(m)) return aktDec(h) + ' h';
    var t = m.n, d = t / 1440n + 1n, hh = (t % 1440n) / 60n, mm = t % 60n;
    return String(d) + '.' + (hh < 10n ? '0' : '') + hh + ':' + (mm < 10n ? '0' : '') + mm;
  }
  function aktDur(h) {
    var s = Rmul(h, R(3600n));
    if (!Rint(s) || s.n < 0n) return eaNum(h) + ' h';
    var t = s.n, d = t / 86400n, hh = (t % 86400n) / 3600n, mi = (t % 3600n) / 60n, se = t % 60n, out = [];
    if (d) out.push(eaInt(d) + ' d');
    if (hh) out.push(String(hh) + ' h');
    if (mi) out.push(String(mi) + ' min');
    if (se) out.push(String(se) + ' s');
    return out.length ? out.join(' ') : '0 min';
  }
  function aktSorted(list) { return list.slice().sort(function (a, b) { return Rcmp(a, b); }); }
  function aktMedian(list) {
    var s = aktSorted(list), n = s.length;
    if (n === 0) throw new Error('aktMedian of an empty list');
    return n % 2 ? s[(n - 1) / 2] : Rdiv(Radd(s[n / 2 - 1], s[n / 2]), R(2n));
  }
  function aktMean(list) {
    if (list.length === 0) throw new Error('aktMean of an empty list');
    return Rdiv(eaSum(list), R(BigInt(list.length)));
  }
  /* A difference of two shares in signed percentage points, one place. */
  function aktPp(r) {
    var p = Rmul(r, R(100n)), sign = p.n > 0n ? '+' : '';
    if (Rint(p)) return sign + eaInt(p.n) + (p.n === 1n || p.n === -1n ? ' point' : ' points');
    return (eaExactAt(p, 1) ? '' : '≈ ') + sign + eaFixed(p, 1) + ' points';
  }
  /* A figure and its unit, the unit singular when the figure is exactly 1 ("1 day", "3/2 = 1.50 days"). */
  function aktUnit(r, word) { return eaNum(r) + ' ' + (Requ(Rabs(r), R1) ? word.replace(/s$/, '') : word); }
  /* Two places always: "2.00", "1.50", "≈ 3.14" (≈ when two places are not exact). */
  function aktTwo(r) { return (eaExactAt(r, 2) ? '' : '≈ ') + eaFixed(r, 2); }
  /* A ratio "times": "2.00×", "≈ 3.14×". */
  function aktTimes(r) { return aktTwo(r) + '×'; }
  /* --- acckit's field kinds (kit-contract.md section 4) ------------------- */
  function aktBound(r, f, what, s) {
    if (f.gt !== undefined && Rcmp(r, Rparse(f.gt)) <= 0) throw new Error(what + ' must be more than ' + eaNum(Rparse(f.gt)) + ', and it is ' + s);
    if (f.min !== undefined && Rcmp(r, Rparse(f.min)) < 0) throw new Error(what + ' cannot be less than ' + eaNum(Rparse(f.min)) + ', and it is ' + s);
    if (f.max !== undefined && Rcmp(r, Rparse(f.max)) > 0) throw new Error(what + ' is at most ' + eaNum(Rparse(f.max)) + ', and it is ' + s);
    return r;
  }
  function aktScalar(f, text, what) {
    var s = eaClean(text);
    if ((f.kind === 'rat' || f.kind === 'time') && f.dash && s === '-') return '-';
    if (f.kind === 'rat') return aktBound(aktParseRat(s, what), f, what, s.replace('-', EA_MINUS));
    if (f.kind === 'time' && f.clock && s !== '' && !AKT_TIME.test(s)) throw new Error(what + ' ' + eaQuote(s) + ' should be a time day.hh:mm, such as 3.14:30; this view takes no bare numbers, because a day number alone cannot tell a lifetime of an hour from one of a day and a half');
    if (f.kind === 'time') return aktTime(s, what);
    return eaScalar(f, s, what);
  }
  function aktRecords(text, f, what) {
    var s = eaClean(text), rows = s === '' ? [] : s.split(';').map(function (r) { return r.trim(); });
    if (rows.length && rows[rows.length - 1] === '') rows.pop();
    eaSized(rows.length, f, what, 'records');
    var seen = {}, n = f.sub.length, lr = f.loRest || 0, hr = f.hiRest || 0;
    return rows.map(function (row, i) {
      var cells = row.split(',').map(function (c) { return c.trim(); }), k = cells.length - n, w = what + ', record ' + (i + 1);
      if (k < lr || k > hr) {
        var need = lr === hr ? String(n + lr) : (n + lr) + ' to ' + (n + hr);
        throw new Error(w + ' has ' + cells.length + ' field' + (cells.length === 1 ? '' : 's') + '; this list needs ' + need
          + ' (' + f.sub.map(function (kk) { return kk[0]; }).join(', ') + (hr ? ', then ' + f.restWhat : '') + ')');
      }
      var rec = {};
      f.sub.forEach(function (kk, j) { rec[kk[0]] = aktScalar(kk[1], cells[j], w + ': ' + kk[0]); });
      rec.rest = cells.slice(n).map(function (c, j) { return aktScalar(f.rest, c, w + ': ' + f.restWhat + ' ' + (j + 1)); });
      if (f.unique) {
        if (Object.prototype.hasOwnProperty.call(seen, cells[0])) throw new Error(what + ' names ' + eaQuote(cells[0]) + ' twice');
        seen[cells[0]] = true;
      }
      return rec;
    });
  }
  function aktList(text, f, what) {
    var s = eaClean(text), toks = s === '' ? [] : s.split(/[\s,]+/).filter(function (t) { return t !== ''; });
    eaSized(toks.length, f, what, f.things);
    var vals = toks.map(function (t, i) { return aktScalar(f.each, t, what + ', entry ' + (i + 1)); });
    if (f.each.kind === 'name') {
      toks.forEach(function (t, i) { if (toks.indexOf(t) !== i) throw new Error(what + ' names ' + eaQuote(t) + ' twice'); });
    }
    return vals;
  }
  function aktRead(spec, raw) {
    var out = {};
    spec.forEach(function (f) {
      if (f.kind === 'arec') out[f.key] = aktRecords(raw[f.key], f, f.what);
      else if (f.kind === 'alist') out[f.key] = aktList(raw[f.key], f, f.what);
      else if (f.kind === 'rat' || f.kind === 'time') out[f.key] = aktScalar(f, raw[f.key], f.what);
      else out[f.key] = eaField(f, raw[f.key]);
    });
    return out;
  }
"""

# ---------------------------------------------------------------------------
# Python mirrors of the shared helpers (kit-contract.md section 3b)
# ---------------------------------------------------------------------------

_NUMBER = re.compile(r"^-?(?:\d+(?:\.(\d+))?|\.(\d+))$")
_TIME = re.compile(r"^(\d{1,3})\.(\d{1,2}):(\d{2})$")
_RAT = re.compile(r"^(-?\d+)/(\d+)$")
MINUS = "−"


def _clean(text):
    return str("" if text is None else text).replace(MINUS, "-").strip()


def _quote(s):
    s = str(s)
    return '"%s"' % (s[:40] + "…" if len(s) > 40 else s)


def plural(n, one, many):
    return "%s %s" % (ea.grp(n), one if n == 1 else many)


def dec_text(fr):
    """aktDec: a finite decimal as typed, ungrouped; cut at 12 places with … otherwise."""
    fr = Fraction(fr)
    neg, n, d = fr < 0, abs(fr.numerator), fr.denominator
    whole, rem, frac = n // d, n % d, ""
    for _ in range(12):
        if rem == 0:
            break
        rem *= 10
        frac += str(rem // d)
        rem %= d
    return (MINUS if neg else "") + str(whole) + ("." + frac if frac else "") + ("…" if rem else "")


def sqrt_fixed(fr, places):
    """aktSqrtFixed: sqrt(fr), fr >= 0, to exactly `places` decimals, half up on the exact value."""
    fr = Fraction(fr)
    if fr < 0:
        raise ValueError("sqrt_fixed of a negative number")
    s = math.isqrt(4 * fr.numerator * 10 ** (2 * places) // fr.denominator)
    t = str((s + 1) // 2).rjust(places + 1, "0")
    whole = "{:,}".format(int(t[:len(t) - places]))
    return whole + ("." + t[len(t) - places:] if places > 0 else "")


def root_signed(sign, sq, places):
    t = sqrt_fixed(sq, places)
    return (MINUS if sign < 0 and re.search(r"[1-9]", t) else "") + t


def sqrt_exact(fr):
    fr = Fraction(fr)
    if fr < 0:
        return None
    a, b = math.isqrt(fr.numerator), math.isqrt(fr.denominator)
    return Fraction(a, b) if a * a == fr.numerator and b * b == fr.denominator else None


def parse_dec(text, what):
    s = _clean(text)
    if s == "":
        raise ValueError("%s is empty" % what)
    m = _NUMBER.match(s)
    if not m:
        raise ValueError("%s should be a number such as 3 or 0.25 (no fractions or exponents), and %s is not one"
                         % (what, _quote(s)))
    if len(m.group(1) or m.group(2) or "") > 6:
        raise ValueError("%s has more than 6 decimal places" % what)
    return Fraction(s)


def parse_rat(text, what):
    s = _clean(text)
    if s == "":
        raise ValueError("%s is empty" % what)
    m = _RAT.match(s)
    if m:
        if re.fullmatch(r"0+", m.group(2)):
            raise ValueError("%s %s divides by zero" % (what, _quote(s)))
        if len(m.group(1).replace("-", "")) > 8 or len(m.group(2)) > 8:
            raise ValueError("%s %s has more than 8 digits above or below the line" % (what, _quote(s)))
        return Fraction(int(m.group(1)), int(m.group(2)))
    m = _NUMBER.match(s)
    if not m:
        raise ValueError("%s should be a number such as 3, 0.25 or 1/2, and %s is not one" % (what, _quote(s)))
    if len(m.group(1) or m.group(2) or "") > 6:
        raise ValueError("%s has more than 6 decimal places" % what)
    return Fraction(s)


def parse_time(text, what):
    s = _clean(text)
    if s == "":
        raise ValueError("%s is empty" % what)
    m = _TIME.match(s)
    if m:
        d, h, mi = int(m.group(1)), int(m.group(2)), int(m.group(3))
        if not 1 <= d <= 366:
            raise ValueError("%s %s: the day is from 1 to 366" % (what, _quote(s)))
        if h > 23:
            raise ValueError("%s %s: the hour is from 00 to 23" % (what, _quote(s)))
        if mi > 59:
            raise ValueError("%s %s: the minutes are from 00 to 59" % (what, _quote(s)))
        return Fraction((d - 1) * 1440 + h * 60 + mi, 60)
    m = _NUMBER.match(s)
    if m and not s.startswith("-"):
        if len(m.group(1) or m.group(2) or "") > 6:
            raise ValueError("%s has more than 6 decimal places" % what)
        r = Fraction(s)
        if r > 8784:
            raise ValueError("%s is at most 8,784 hours (366 days), and it is %s" % (what, s))
        return r
    raise ValueError("%s %s should be a time: day.hh:mm (1.09:30 is day 1 at 09:30) or hours from the start (37.5)"
                     % (what, _quote(s)))


def time_text(h):
    """aktTimeText."""
    m = Fraction(h) * 60
    if m.denominator != 1:
        return dec_text(h) + " h"
    t = m.numerator
    return "%d.%02d:%02d" % (t // 1440 + 1, (t % 1440) // 60, t % 60)


def median(values):
    s = sorted(Fraction(v) for v in values)
    n = len(s)
    if n == 0:
        raise ValueError("median of an empty list")
    return s[(n - 1) // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2


def _fixed(fr, places):
    """eaFixed: exactly `places` decimals, half away from zero, grouped."""
    fr = Fraction(fr)
    q = (abs(fr.numerator) * 10 ** places * 2 // fr.denominator + 1) // 2
    t = str(q).rjust(places + 1, "0")
    whole = "{:,}".format(int(t[:len(t) - places]))
    return (MINUS if fr < 0 and q else "") + whole + ("." + t[len(t) - places:] if places else "")


def num_text(fr):
    """eaNum, for figures below 30 digits: "4", "3/2 = 1.50", "2/7 ≈ 0.29"."""
    fr = Fraction(fr)
    if fr.denominator == 1:
        return ea.grp(fr.numerator)
    exact = (fr * 100).denominator == 1
    return "%s/%s%s%s" % (ea.grp(fr.numerator), ea.grp(fr.denominator), " = " if exact else " ≈ ", _fixed(fr, 2))


def unit_text(fr, word):
    """aktUnit: the figure and its unit, singular when the figure is exactly 1 or −1."""
    return num_text(fr) + " " + (word[:-1] if abs(Fraction(fr)) == 1 and word.endswith("s") else word)


def pp_text(fr):
    """aktPp: signed percentage points, one place."""
    p = Fraction(fr) * 100
    sign = "+" if p > 0 else ""
    if p.denominator == 1:
        return sign + ea.grp(p.numerator) + (" point" if abs(p.numerator) == 1 else " points")
    exact = (p * 10).denominator == 1
    q = (abs(p.numerator) * 10 * 2 // p.denominator + 1) // 2
    t = "%s%d.%d" % (MINUS if p < 0 and q else "", q // 10, q % 10)
    return ("" if exact else "≈ ") + sign + t + " points"


# ---------------------------------------------------------------------------
# acckit's field kinds, mirrored (kit-contract.md section 4)
# ---------------------------------------------------------------------------

TIME = {"kind": "time"}
CLOCK = {"kind": "time", "clock": True}   # day.hh:mm only


def rat(gt=None, lo=None, hi=ea.LIMIT, dash=False):
    """A rational cell: a decimal (at most 6 places) or a fraction p/q; '-' when dash."""
    f = {"kind": "rat"}
    if gt is not None:
        f["gt"] = str(gt)
    if lo is not None:
        f["min"] = str(lo)
    if hi is not None:
        f["max"] = str(hi)
    if dash:
        f["dash"] = True
    return f


def arec(what, sub, rest=None, rest_what="value", lo_rest=0, hi_rest=0, unique=False, rows=3, lo=1,
         hi=ea.MAX_RECORDS):
    """Records: the cells in `sub` (any scalar kind), then lo_rest to hi_rest cells each read by `rest`."""
    return {"kind": "arec", "what": what, "control": "area", "rows": rows, "sub": [list(s) for s in sub],
            "rest": dict(rest or ea.NAME), "restWhat": rest_what, "loRest": lo_rest, "hiRest": hi_rest,
            "lo": lo, "hi": hi, "unique": unique}


def alist(what, each, lo=1, hi=ea.MAX_RECORDS, things="values", control="text"):
    """A list separated by spaces or commas; entries follow any scalar kind."""
    return {"kind": "alist", "what": what, "control": control, "rows": 2, "each": dict(each), "lo": lo, "hi": hi,
            "things": things}


def _bound(r, f, what, s):
    if "gt" in f and r <= Fraction(f["gt"]):
        raise ValueError("%s must be more than %s, and it is %s" % (what, ea.ftext(Fraction(f["gt"])), s))
    if "min" in f and r < Fraction(f["min"]):
        raise ValueError("%s cannot be less than %s, and it is %s" % (what, ea.ftext(Fraction(f["min"])), s))
    if "max" in f and r > Fraction(f["max"]):
        raise ValueError("%s is at most %s, and it is %s" % (what, ea.ftext(Fraction(f["max"])), s))
    return r


def parse_scalar(f, text, what):
    s = _clean(text)
    if f["kind"] in ("rat", "time") and f.get("dash") and s == "-":
        return "-"
    if f["kind"] == "rat":
        return _bound(parse_rat(s, what), f, what, s.replace("-", MINUS))
    if f["kind"] == "time" and f.get("clock") and s != "" and not _TIME.match(s):
        raise ValueError("%s %s should be a time day.hh:mm, such as 3.14:30; this view takes no bare numbers, because a day number alone cannot tell a lifetime of an hour from one of a day and a half" % (what, _quote(s)))
    if f["kind"] == "time":
        return parse_time(s, what)
    return ea.parse_scalar(f, s, what)


def _parse_arec(f, text):
    what = f["what"]
    s = _clean(text)
    rows = [r.strip() for r in s.split(";")] if s else []
    if rows and rows[-1] == "":
        rows.pop()
    ea._sized(len(rows), f, what, "records")
    out, seen, n, lr, hr = [], set(), len(f["sub"]), f.get("loRest", 0), f.get("hiRest", 0)
    for i, row in enumerate(rows):
        cells = [c.strip() for c in row.split(",")]
        k, w = len(cells) - n, "%s, record %d" % (what, i + 1)
        if k < lr or k > hr:
            need = str(n + lr) if lr == hr else "%d to %d" % (n + lr, n + hr)
            raise ValueError("%s has %d field%s; this list needs %s (%s%s)"
                             % (w, len(cells), "" if len(cells) == 1 else "s", need,
                                ", ".join(key for key, _ in f["sub"]), ", then " + f["restWhat"] if hr else ""))
        rec = {}
        for j, (key, kk) in enumerate(f["sub"]):
            rec[key] = parse_scalar(kk, cells[j], "%s: %s" % (w, key))
        rec["rest"] = [parse_scalar(f["rest"], c, "%s: %s %d" % (w, f["restWhat"], j + 1))
                       for j, c in enumerate(cells[n:])]
        if f["unique"]:
            if cells[0] in seen:
                raise ValueError("%s names %s twice" % (what, _quote(cells[0])))
            seen.add(cells[0])
        out.append(rec)
    return out


def _parse_alist(f, text):
    what = f["what"]
    s = _clean(text)
    toks = [t for t in re.split(r"[\s,]+", s) if t] if s else []
    ea._sized(len(toks), f, what, f["things"])
    vals = [parse_scalar(f["each"], t, "%s, entry %d" % (what, i + 1)) for i, t in enumerate(toks)]
    if f["each"]["kind"] == "name":
        for i, t in enumerate(toks):
            if toks.index(t) != i:
                raise ValueError("%s names %s twice" % (what, _quote(t)))
    return vals


_OWN = ("arec", "alist", "rat", "time")


def parse_field(where, f, text):
    """Mirror of aktRead for one field."""
    if f["kind"] not in _OWN:
        return ea.parse(where, f, text)
    try:
        if f["kind"] == "arec":
            return _parse_arec(f, text)
        if f["kind"] == "alist":
            return _parse_alist(f, text)
        return parse_scalar(f, text, f["what"])
    except ValueError as exc:
        raise ValueError("%s: %s" % (where, exc)) from None


def to_text(where, f, value):
    """A preset's value -> the exact text its box holds (eakit's to_text for eakit's kinds)."""
    if f["kind"] not in _OWN:
        return ea.to_text(where, f, value)
    what = f["what"]
    if isinstance(value, str):
        text = value.strip()
    elif f["kind"] == "arec" and isinstance(value, (list, tuple)):
        text = "; ".join(r.strip() if isinstance(r, str) else ", ".join(str(p).strip() for p in r) for r in value)
    elif f["kind"] == "alist" and isinstance(value, (list, tuple)):
        text = " ".join(str(p).strip() for p in value)
    elif isinstance(value, (int, Fraction)) and not isinstance(value, bool):
        text = str(value)
    else:
        raise ValueError("%s: %s cannot be %r" % (where, what, value))
    if re.search(r'[<>&"]', text):
        raise ValueError("%s: %s %r contains < > & or a quote, which no shipped value may" % (where, what, text))
    parse_field(where, f, text)
    return text


# ---------------------------------------------------------------------------
# Building a lab (both families)
# ---------------------------------------------------------------------------

def _presets(cfg, kit, fields, tiles, check, fixed):
    """eakit_core.presets, reading acckit's kinds as well."""
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
            parsed[key] = parse_field(where, spec, inst[key])
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


_READ_CALL = "eaRead(SPEC, raw)"
_WIRE_JS = ea.EA_WIRE_JS.replace(_READ_CALL, "aktRead(SPEC, raw)")
assert ea.EA_WIRE_JS.count(_READ_CALL) == 1, "eakit's wiring no longer reads its inputs with one eaRead(SPEC, raw) call"
_COMMENT_LINES = re.compile(r"^[ \t]*/\*(?:(?!\*/).)*\*/[ \t]*\n", re.S | re.M)


def _build_lab(cfg, *, kit, prefix, view, fields, tiles, fn, js, fixed, title, subtitle, intro, rules, extra_keys=(),
               check=None):
    """eakit_core.build_lab, with acckit's kinds and aktRead (kit-contract.md section 2)."""
    allowed = ea.COMMON_CFG | set(extra_keys) | {key for key, _s, _d in fields}
    stray = sorted(set(cfg) - allowed)
    if stray:
        raise ValueError("%s: cfg sets %s, which this view does not take (it takes %s)"
                         % (kit, ", ".join(stray), ", ".join(sorted(allowed))))
    table, menu, expect, chosen = _presets(cfg, kit, fields, tiles, check, fixed)
    here = table[chosen]
    spec, controls = [], ea.select_html(prefix + "Preset", "Worked example", menu, chosen)
    for key, fspec, _default in fields:
        cid = ea.camel(prefix, key)
        spec.append(dict(fspec, key=key, id=cid))
        if fspec["control"] == "select":
            controls += ea.select_html(cid, fspec["what"], [(w, w) for w in fspec["words"]], here[key])
        elif fspec["control"] == "area":
            controls += ea.area_html(cid, fspec["what"], here[key], fspec.get("rows", 3))
        else:
            controls += ea.text_html(cid, fspec["what"], here[key])
    controls += ea.kpis_html(tiles)
    ids = [s["id"] for s in spec] + [cid for _l, cid in tiles] + [prefix + x for x in ("Preset", "Status", "Table")]
    if len(set(ids)) != len(ids):
        raise ValueError("%s: two controls or tiles share an id: %s" % (kit, sorted({i for i in ids if ids.count(i) > 1})))
    script = (RATIONAL_JS + ea.EA_CORE_JS + js
              + cfg_literal("PRESETS", table) + cfg_literal("SPEC", spec)
              + cfg_literal("TILES", [cid for _label, cid in tiles])
              + cfg_literal("FIXED", fixed) + cfg_literal("VIEW", view)
              + _WIRE_JS.replace("%P%", prefix).replace("%FN%", fn))
    script = _COMMENT_LINES.sub("", script)
    panel_intro = ea.plain(cfg, kit, "panel_intro", intro, limit=1200)
    if FAMILY_SENTENCE not in panel_intro:
        panel_intro = FAMILY_SENTENCE + " " + panel_intro
    title = ea.plain(cfg, kit, "title", title)
    return Lab(title=title, subtitle=subtitle,
               markup=ea.markup_html(prefix, title, subtitle, rules), controls=controls, script=script,
               panel_title=ea.plain(cfg, kit, "panel_title", "Change the inputs, or choose a worked example"),
               panel_intro=panel_intro, expect={prefix + "Preset": expect})


def family_intro():
    return (FAMILY_SENTENCE + " It shows what one measure says about that sample; the book's findings are its "
            "survey's, and a correlation is not a cause.")


def _no_options(cfg, kit, tiles):
    return {}, [], tiles


def mode_lab(cfg, mode, spec):
    """One acckit mode as a Lab, from its spec dict (kit-contract.md section 2)."""
    views = spec["views"]
    order = tuple(views)
    view = cfg.get("view", order[0])
    if view not in views:
        raise ValueError("%s/%s: unknown view %r; the views are %s" % (KIT, mode, view, ", ".join(order)))
    kit = "%s/%s/%s" % (KIT, mode, view)
    v = views[view]
    fixed, keys, tiles = v.get("options", _no_options)(cfg, kit, v["tiles"])
    for _label, cid in tiles:
        if not cid.startswith(spec["prefix"]):
            raise ValueError("%s: tile id %r does not begin with the prefix %r" % (kit, cid, spec["prefix"]))
    return _build_lab(cfg, kit=kit, prefix=spec["prefix"], view=view, fields=v["fields"], tiles=tiles,
                      fn=spec["fn"], js=AKT_CORE_JS + spec["js"] + v["js"], fixed=fixed, title=spec["title"],
                      subtitle=v["subtitle"], intro=family_intro(), rules=v["rules"], extra_keys=keys,
                      check=v["check"])

# ---------------------------------------------------------------------------
# delivery (ade): the four measures from a log, and classes of performer
# ---------------------------------------------------------------------------

ADE_JS = r"""
  var ADE_VIEW = {};
  function adeCompute(view, inst, opts) { return eaRun(ADE_VIEW[view], inst, opts); }
  /* The book's six answer options (Chapter 2), best first. */
  var ADE_LEAD = ['less than one hour', 'less than one day', 'between one day and one week',
    'between one week and one month', 'between one month and six months', 'more than six months'];
  var ADE_FREQ = ['on demand (multiple deploys per day)', 'between once per hour and once per day',
    'between once per day and once per week', 'between once per week and once per month',
    'between once per month and once every six months', 'fewer than once every six months'];
  var ADE_FAIL = ['0–15%', '16–30%', '31–45%', '46–60%', '61–75%', '76–100%'];
  /* A duration in hours: the first option whose bound it is under (1 h, 1 d, 7 d, 30 d, 180 d). */
  function adeLeadOpt(h) {
    var up = [1n, 24n, 168n, 720n, 4320n], i;
    for (i = 0; i < up.length; i += 1) if (Rcmp(h, R(up[i])) < 0) return i;
    return 5;
  }
  /* Deploys per day: the first option whose floor it reaches (2, 1, 1/7, 1/30, 1/180 a day). */
  function adeFreqOpt(f) {
    var lo = [R(2n), R(1n), R(1n, 7n), R(1n, 30n), R(1n, 180n)], i;
    for (i = 0; i < lo.length; i += 1) if (Rcmp(f, lo[i]) >= 0) return i;
    return 5;
  }
  /* A failure share: the first band whose top it does not pass (15, 30, 45, 60, 75, 100 percent). */
  function adeFailOpt(r) {
    var up = [15n, 30n, 45n, 60n, 75n], p = Rmul(r, R(100n)), i;
    for (i = 0; i < up.length; i += 1) if (Rcmp(p, R(up[i])) <= 0) return i;
    return 5;
  }
"""

ADE_VIEW_JS = {}

ADE_VIEW_JS["metrics"] = r"""
  function adePeriod(days, changes, incidents, cw, iw) {
    var end = Rmul(R(days.n), R(24n)), dTxt = eaInt(days.n);
    var late = function (w, what, t) { if (Rcmp(t, end) > 0) eaRefuse(w + ': ' + what + ' ' + aktTimeText(t) + ' is after the end of the ' + dTxt + '-day period'); };
    var deployedAt = [], leads = [], failed = 0, rows = [], restores = [];
    changes.forEach(function (c, i) {
      var w = cw + ', record ' + (i + 1) + ' (' + c.change + ')';
      late(w, 'committed', c.committed);
      if (c.deployed === '-') {
        if (c.failed === 'yes') eaRefuse(w + ': failed is yes, but the change was never deployed (deployed -)');
        rows.push(['change ' + c.change, aktTimeText(c.committed), 'not deployed', '—', c.failed]);
        return;
      }
      late(w, 'deployed', c.deployed);
      if (Rcmp(c.deployed, c.committed) < 0) eaRefuse(w + ': deployed ' + aktTimeText(c.deployed) + ' is before committed ' + aktTimeText(c.committed));
      if (!deployedAt.some(function (t) { return Requ(t, c.deployed); })) deployedAt.push(c.deployed);
      var lt = Rsub(c.deployed, c.committed);
      leads.push(lt);
      if (c.failed === 'yes') failed += 1;
      rows.push(['change ' + c.change, aktTimeText(c.committed), aktTimeText(c.deployed), aktDur(lt), c.failed]);
    });
    incidents.forEach(function (x, i) {
      var w = iw + ', record ' + (i + 1) + ' (' + x.incident + ')';
      late(w, 'start', x.start);
      late(w, 'restored', x.restored);
      if (Rcmp(x.restored, x.start) < 0) eaRefuse(w + ': restored ' + aktTimeText(x.restored) + ' is before start ' + aktTimeText(x.start));
      var rt = Rsub(x.restored, x.start);
      restores.push(rt);
      rows.push(['incident ' + x.incident, aktTimeText(x.start), aktTimeText(x.restored), aktDur(rt), '']);
    });
    var n = deployedAt.length, perDay = R(BigInt(n), days.n), P = { rows: rows, deployed: leads.length, failed: failed };
    P.deploys = eaInt(n);
    P.changes = eaInt(leads.length) + ' of ' + eaInt(changes.length);
    P.perDay = eaNum(perDay);
    P.perWeek = eaNum(Rmul(perDay, R(7n)));
    P.freq = n === 0 ? 'none: no deployment in the period' : ADE_FREQ[adeFreqOpt(perDay)];
    P.lead = leads.length ? aktDur(aktMedian(leads)) : 'no change deployed';
    P.leadOpt = leads.length ? ADE_LEAD[adeLeadOpt(aktMedian(leads))] : 'no change deployed';
    P.fail = leads.length ? eaPct(R(BigInt(failed), BigInt(leads.length))) : 'no change deployed';
    P.failBand = leads.length ? ADE_FAIL[adeFailOpt(R(BigInt(failed), BigInt(leads.length)))] : 'no change deployed';
    P.restore = restores.length ? aktDur(aktMedian(restores)) : 'no incident in the period';
    P.restoreOpt = restores.length ? ADE_LEAD[adeLeadOpt(aktMedian(restores))] : 'no incident in the period';
    P.say = eaPlural(n, 'deployment', 'deployments') + ' (' + P.perDay + ' a day), median lead time ' + P.lead
      + ', change fail rate ' + P.fail + ', median time to restore ' + P.restore;
    return P;
  }
  ADE_VIEW.metrics = function (inst) {
    var p1 = adePeriod(inst.days, inst.changes, inst.incidents, 'Changes', 'Incidents');
    var two = inst.changes2.length > 0 || inst.incidents2.length > 0;
    var p2 = two ? adePeriod(inst.days, inst.changes2, inst.incidents2, 'Changes, period 2', 'Incidents, period 2') : null;
    var keys = ['deploys', 'changes', 'perDay', 'perWeek', 'freq', 'lead', 'leadOpt', 'fail', 'failBand', 'restore', 'restoreOpt'];
    var ids = ['adeDeploys', 'adeChanges', 'adePerDay', 'adePerWeek', 'adeFreq', 'adeLead', 'adeLeadOpt', 'adeFail', 'adeFailBand', 'adeRestore', 'adeRestoreOpt'];
    var tiles = {};
    keys.forEach(function (k, i) { tiles[ids[i]] = two ? p1[k] + ' → ' + p2[k] : p1[k]; });
    var rows = two ? p1.rows.map(function (r) { return ['1'].concat(r); }).concat(p2.rows.map(function (r) { return ['2'].concat(r); })) : p1.rows;
    var head = ['record', 'start', 'end', 'lead time or time to restore', 'failed'];
    return {
      tiles: tiles,
      status: aktStatus(two ? 'Period 1: ' + p1.say + '. Period 2: ' + p2.say
                            : 'Over ' + eaPlural(inst.days.n, 'day', 'days') + ': ' + p1.say),
      table: { caption: 'Each change (commit to deploy) and each incident (start to restore)', head: two ? ['period'].concat(head) : head, rows: rows }
    };
  };
"""

ADE_VIEW_JS["cluster"] = r"""
  var ADE_MEASURES = [['deploy', ADE_FREQ], ['lead', ADE_LEAD], ['restore', ADE_LEAD], ['fail', ADE_FAIL]];
  function adeDecode(code, words, better) { return words[better === '1' ? code - 1 : 6 - code]; }
  function adeMedText(m, words, better) {
    if (Rint(m)) return aktDec(m) + ', ' + adeDecode(Number(m.n), words, better);
    var lo = Number(m.n / m.d);
    return aktDec(m) + ', ' + adeDecode(lo, words, better) + ' / ' + adeDecode(lo + 1, words, better);
  }
  ADE_VIEW.cluster = function (inst) {
    var teams = inst.teams, n = teams.length, k = Number(inst.k.n), dims = ['deploy', 'lead', 'restore', 'fail'];
    if (k >= n) eaRefuse('k is ' + k + ', and there are ' + n + ' teams; k must be fewer than the teams');
    var cl = teams.map(function (t, i) {
      return { m: [i], s: dims.map(function (d) { return t[d].n; }) };
    });
    var name = function (c) { return '{' + c.m.map(function (i) { return teams[i].team; }).join(', ') + '}'; };
    var merges = [], total = R0, groupsAtK = null, rows = [];
    while (cl.length > 1) {
      var best = null, bi = -1, bj = -1, i, j;
      for (i = 0; i < cl.length; i += 1) {
        for (j = i + 1; j < cl.length; j += 1) {
          var a = cl[i], b = cl[j], na = BigInt(a.m.length), nb = BigInt(b.m.length), num = 0n;
          dims.forEach(function (d, x) { var t = a.s[x] * nb - b.s[x] * na; num += t * t; });
          var cost = R(num, na * nb * (na + nb));
          if (best === null || Rcmp(cost, best) < 0) { best = cost; bi = i; bj = j; }
        }
      }
      var A = cl[bi], B = cl[bj], merged = { m: A.m.concat(B.m).sort(function (p, q) { return p - q; }), s: A.s.map(function (v, x) { return v + B.s[x]; }) };
      total = Radd(total, best);
      var what = name(A) + ' + ' + name(B);
      cl.splice(bj, 1); cl.splice(bi, 1, merged);
      cl.sort(function (p, q) { return p.m[0] - q.m[0]; });
      merges.push({ what: what, cost: best, left: cl.length, total: total });
      rows.push([String(merges.length), what, eaNum(best), String(cl.length) + (cl.length === k ? ' (k)' : ''), eaNum(total)]);
      if (cl.length === k) groupsAtK = cl.map(function (c) { return { m: c.m.slice() }; });
    }
    var made = merges[n - k - 1], next = merges[n - k];
    var tiles = {
      adeTeams: eaInt(n),
      adeGroups: groupsAtK.map(function (g, x) { return 'G' + (x + 1) + ': ' + g.m.map(function (i) { return teams[i].team; }).join(', '); }).join('; '),
      adeWithin: eaNum(made.total),
      adeLastCoef: eaNum(made.cost) + ' (' + made.what + ')',
      adeNextCoef: eaNum(next.cost) + ' (' + next.what + ')'
    };
    ADE_MEASURES.forEach(function (mw) {
      tiles['adeMed' + mw[0].charAt(0).toUpperCase() + mw[0].slice(1)] = groupsAtK.map(function (g, x) {
        var m = aktMedian(g.m.map(function (i) { return teams[i][mw[0]]; }));
        return 'G' + (x + 1) + ': ' + adeMedText(m, mw[1], inst.better);
      }).join('; ');
    });
    return {
      tiles: tiles,
      status: aktStatus(eaPlural(n, 'team', 'teams') + ' in ' + k + ' groups by Ward’s method; the last merge made added '
        + eaNum(made.cost) + ' to the within-group sum of squares, and the next, to ' + (k - 1) + ' group' + (k - 1 === 1 ? '' : 's') + ', would add ' + eaNum(next.cost)),
      table: { caption: 'Each merge in order, with its fusion coefficient (the increase in the total within-group sum of squares)',
               head: ['merge', 'groups joined', 'fusion coefficient', 'groups left', 'total within-group sum of squares'], rows: rows }
    };
  };
"""


def _check_metrics_period(days, changes, incidents, cw, iw):
    end = Fraction(days) * 24
    dtxt = ea.grp(int(days))

    def late(w, what, t):
        if t > end:
            raise ValueError("%s: %s %s is after the end of the %s-day period" % (w, what, time_text(t), dtxt))
    for i, c in enumerate(changes):
        w = "%s, record %d (%s)" % (cw, i + 1, c["change"])
        late(w, "committed", c["committed"])
        if c["deployed"] == "-":
            if c["failed"] == "yes":
                raise ValueError("%s: failed is yes, but the change was never deployed (deployed -)" % w)
            continue
        late(w, "deployed", c["deployed"])
        if c["deployed"] < c["committed"]:
            raise ValueError("%s: deployed %s is before committed %s" % (w, time_text(c["deployed"]),
                                                                          time_text(c["committed"])))
    for i, x in enumerate(incidents):
        w = "%s, record %d (%s)" % (iw, i + 1, x["incident"])
        late(w, "start", x["start"])
        late(w, "restored", x["restored"])
        if x["restored"] < x["start"]:
            raise ValueError("%s: restored %s is before start %s" % (w, time_text(x["restored"]), time_text(x["start"])))


def _check_metrics(inst, fixed):
    _check_metrics_period(inst["days"], inst["changes"], inst["incidents"], "Changes", "Incidents")
    if inst["changes2"] or inst["incidents2"]:
        _check_metrics_period(inst["days"], inst["changes2"], inst["incidents2"], "Changes, period 2",
                              "Incidents, period 2")


def _check_cluster(inst, fixed):
    n, k = len(inst["teams"]), int(inst["k"])
    if k >= n:
        raise ValueError("k is %d, and there are %d teams; k must be fewer than the teams" % (k, n))


_N = ea.NAME
_CODE = ea.whole(1, 6)
_DEPLOYED = dict(TIME, dash=True)
_CHANGES_SUB = [("change", _N), ("committed", TIME), ("deployed", _DEPLOYED), ("failed", ea.YESNO)]
_INCIDENT_SUB = [("incident", _N), ("start", TIME), ("restored", TIME)]
_TIME_RULE = ("A time is day.hh:mm from the period's start (1.09:30 is day 1 at 09:30; day 1 begins at hour 0) or "
              "decimal hours from the start (33.5). ")

DELIVERY = {
    "prefix": "ade", "fn": "adeCompute", "title": "Delivery performance", "js": ADE_JS,
    "views": {
        "metrics": {
            "fields": [("days", ea.field("Days in the period", ea.whole(1, 366)), "14"),
                       ("changes", arec("Changes (change, committed, deployed or -, failed yes or no)", _CHANGES_SUB,
                                        unique=True, rows=5, lo=0), None),
                       ("incidents", arec("Incidents (incident, start, restored)", _INCIDENT_SUB, unique=True,
                                          rows=2, lo=0), ""),
                       ("changes2", arec("Period 2 changes, to compare (empty for none)", _CHANGES_SUB,
                                         unique=True, rows=3, lo=0), ""),
                       ("incidents2", arec("Period 2 incidents (empty for none)", _INCIDENT_SUB, unique=True,
                                           rows=2, lo=0), "")],
            "tiles": [("Deployments", "adeDeploys"), ("Changes deployed", "adeChanges"),
                      ("Deployments per day", "adePerDay"), ("Deployments per week", "adePerWeek"),
                      ("Deployment frequency, as the book's answer option", "adeFreq"),
                      ("Median lead time (commit to deploy)", "adeLead"), ("Lead time, as the book's answer option", "adeLeadOpt"),
                      ("Change fail rate (failed / deployed)", "adeFail"), ("Change fail rate band", "adeFailBand"),
                      ("Median time to restore service", "adeRestore"),
                      ("Time to restore, as the book's answer option", "adeRestoreOpt")],
            "check": _check_metrics, "subtitle": "the four measures from a log of changes and incidents",
            "rules": _TIME_RULE + "Every time falls within the period. A deployment is one deploy time: changes "
                     "deployed at the same moment are one deployment. Lead time is deployed minus committed, for each "
                     "change deployed; time to restore is restored minus start. A median is the middle value, or the "
                     "mean of the two middle values. Change fail rate is the failed changes over the changes "
                     "deployed. Each measure is placed on the book's six answer options: lead time and time to "
                     "restore under less than one hour, less than one day, between one day and one week, between "
                     "one week and one month (30 days), between one month and six months (180 days), more than six "
                     "months, a value exactly on a boundary going to the longer option (one hour exactly is less "
                     "than one day); deployment frequency by deployments per day over the period, where the book's "
                     "first two options overlap, so two or more a day is on demand (multiple deploys per day), at "
                     "least one but fewer than two is between once per hour and once per day, at least one a week "
                     "between once per day and once per week, at least one in 30 days between once per week and "
                     "once per month, at least one in 180 days between once per month and once every six months, "
                     "a rate exactly on a boundary going to the more frequent option. The fail rate's bands are "
                     "0–15%, 16–30%, 31–45%, 46–60% (the book's) and the lab's 61–75%, 76–100%, a rate in the "
                     "first band whose top it does not pass (15.5% is 16–30%). With period 2 given, each tile "
                     "reads period 1 → period 2, over the same number of days.",
            "js": ADE_VIEW_JS["metrics"],
        },
        "cluster": {
            "fields": [("teams", ea.rec("Teams, coded 1 to 6 (team, deploy, lead, restore, fail)",
                                        [("team", _N), ("deploy", _CODE), ("lead", _CODE), ("restore", _CODE),
                                         ("fail", _CODE)], unique=True, rows=6, lo=3, hi=30), None),
                       ("k", ea.field("Groups to stop at (k, 2 to 5)", ea.whole(2, 5)), "3"),
                       ("better", ea.choice("The book's first option (on demand, less than one hour, 0–15%) is coded",
                                            "1", "6"), "1")],
            "tiles": [("Teams", "adeTeams"), ("The k groups", "adeGroups"),
                      ("Median deployment frequency per group", "adeMedDeploy"),
                      ("Median lead time per group", "adeMedLead"),
                      ("Median time to restore per group", "adeMedRestore"),
                      ("Median change fail rate per group", "adeMedFail"),
                      ("Total within-group sum of squares at k", "adeWithin"),
                      ("Fusion coefficient of the last merge made", "adeLastCoef"),
                      ("Fusion coefficient of the next merge (to k − 1)", "adeNextCoef")],
            "check": _check_cluster, "subtitle": "Ward's hierarchical clustering of coded answers",
            "rules": "Each team is a point of four codes, 1 to 6, one per measure. Ward's method starts with every "
                     "team alone and merges, at each step, the two groups whose merge adds least to the total "
                     "within-group sum of squares (squared Euclidean distance of each team from its group's mean, "
                     "summed); that increase, nA·nB/(nA + nB) times the squared distance between the two means, is "
                     "the merge's fusion coefficient, an exact fraction. The clustering does not know which end of "
                     "a scale is better; it groups by distance alone. Groups are kept in the order of their earliest "
                     "team in the input, and a tie between merges goes to the pair whose first group comes earliest, "
                     "then whose second does. Groups are named G1, G2, … in that order at k. A group's median on a "
                     "measure is the middle code, or the mean of the two middle codes, decoded to the book's option "
                     "(a half code shows both neighbours). The table runs every merge down to one group.",
            "js": ADE_VIEW_JS["cluster"],
        },
    },
}

# ---------------------------------------------------------------------------
# flow (afl): utilization and queueing, batch size, work in process
# ---------------------------------------------------------------------------

AFL_JS = r"""
  var AFL_VIEW = {};
  function aflCompute(view, inst, opts) { return eaRun(AFL_VIEW[view], inst, opts); }
  function aflPct(r) { return aktDec(r) + '%'; }
"""

AFL_VIEW_JS = {}

AFL_VIEW_JS["utilization"] = r"""
  AFL_VIEW.utilization = function (inst) {
    var unit = inst.unit, rows = [], mult = [], leads = [], hi = null, lo = null;
    inst.levels.forEach(function (l, i) {
      if (Rcmp(l, R(100n)) >= 0) eaRefuse('Utilization levels, entry ' + (i + 1) + ' is 100%: there u/(1 − u) divides by zero, because work arrives as fast as it can be done, so in this model the queue and the wait grow without bound and no lead time exists');
    });
    inst.levels.forEach(function (l) {
      var u = Rdiv(l, R(100n)), idle = Rsub(R1, u), q = Rdiv(u, idle), lead = Rdiv(inst.service, idle);
      mult.push(aflPct(l) + ': ' + eaNum(q));
      leads.push(aflPct(l) + ': ' + aktUnit(lead, unit));
      rows.push([aflPct(l), eaNum(q), aktUnit(lead, unit), aktTimes(Rinv(idle))]);
      if (hi === null || Rcmp(l, hi.l) > 0) hi = { l: l, lead: lead, x: Rinv(idle) };
      if (lo === null || Rcmp(l, lo.l) < 0) lo = { l: l, lead: lead };
    });
    return {
      tiles: {
        aflLevels: eaCount(inst.levels.map(aflPct)), aflMultiples: mult.join('; '), aflLeads: leads.join('; '),
        aflHigh: aflPct(hi.l) + ': ' + aktTimes(hi.x) + ' the service time',
        aflRatio: Requ(hi.l, lo.l) ? 'one level only' : aktTimes(Rdiv(hi.lead, lo.lead)) + ' (' + aflPct(lo.l) + ' to ' + aflPct(hi.l) + ')'
      },
      status: aktStatus('With a service time of ' + aktUnit(inst.service, unit) + ', the lead time at ' + aflPct(hi.l)
        + ' utilization is ' + aktUnit(hi.lead, unit) + ', ' + aktTimes(hi.x) + ' the service time, in the simple queueing model'),
      table: { caption: 'Each utilization level: the queueing multiple u/(1 − u) and the lead time service/(1 − u)',
               head: ['utilization', 'u/(1 − u)', 'lead time', 'lead ÷ service'], rows: rows }
    };
  };
"""

AFL_VIEW_JS["batch"] = r"""
  function aflRun(work, b, p, c) {
    var nb = (work + b - 1n) / b, out = { nb: nb, rel: [], wait: R0 }, done = 0n, i;
    for (i = 1n; i <= nb; i += 1n) {
      var size = i < nb ? b : work - b * (nb - 1n);
      done += size;
      var t = Radd(Rmul(R(done), p), Rmul(R(i), c));
      out.rel.push({ size: size, t: t });
      out.wait = Radd(out.wait, Rmul(R(size), t));
    }
    out.wait = Rdiv(out.wait, R(work));
    out.first = out.rel[0].t; out.last = out.rel[out.rel.length - 1].t; out.over = Rmul(R(nb), c);
    var last = out.rel[out.rel.length - 1].size;
    out.batches = last === b ? eaInt(nb) + ' of ' + eaInt(b) : eaInt(nb) + ': ' + (nb > 1n ? eaInt(nb - 1n) + ' of ' + eaInt(b) + ', ' : '') + 'the last of ' + eaInt(last);
    return out;
  }
  AFL_VIEW.batch = function (inst) {
    var work = inst.work.n, u = inst.unit;
    inst.batch.forEach(function (b, i) {
      if (b.n > work) eaRefuse('Batch sizes, entry ' + (i + 1) + ' is ' + eaInt(b.n) + ', more than the work (' + eaPlural(work, 'item', 'items') + ')');
    });
    var runs = inst.batch.map(function (b) { return aflRun(work, b.n, inst.per_item, inst.release_cost); });
    var two = runs.length === 2, both = function (f) { return runs.map(f).join(' → '); };
    var tm = function (r) { return aktUnit(r, u); };
    var rows = [], most = runs.reduce(function (m, r) { return r.rel.length > m ? r.rel.length : m; }, 0), i;
    for (i = 0; i < Math.min(most, 40); i += 1) {
      var row = [String(i + 1)];
      runs.forEach(function (r) { row.push(i < r.rel.length ? eaInt(r.rel[i].size) : ''); row.push(i < r.rel.length ? tm(r.rel[i].t) : ''); });
      rows.push(row);
    }
    var head = ['batch'];
    inst.batch.forEach(function (b) { head.push('items (batch of ' + eaInt(b.n) + ')'); head.push('released at'); });
    return {
      tiles: {
        aflBatches: both(function (r) { return r.batches; }),
        aflFirst: both(function (r) { return tm(r.first); }),
        aflLast: both(function (r) { return tm(r.last); }),
        aflWait: both(function (r) { return tm(r.wait); }),
        aflOverhead: both(function (r) { return tm(r.over); }),
        aflRatio: two ? aktTimes(Rdiv(runs[0].first, runs[1].first)) : 'one batch size only'
      },
      status: aktStatus(eaPlural(work, 'item', 'items') + ' at ' + tm(inst.per_item) + ' each, '
        + tm(inst.release_cost) + ' per release: the first feedback comes at ' + both(function (r) { return tm(r.first); })
        + (two ? ' as the batch goes from ' + eaInt(inst.batch[0].n) + ' to ' + eaPlural(inst.batch[1].n, 'item', 'items') : '')),
      table: { caption: 'Each batch, when it is released' + (most > 40 ? ' (the first 40 of ' + most + ')' : ''), head: head, rows: rows }
    };
  };
"""

AFL_VIEW_JS["wip"] = r"""
  AFL_VIEW.wip = function (inst) {
    var log = inst.items, D = inst.days, end = R(D.n), dTxt = eaInt(D.n), rows = [], thru, tiles = {}, say;
    if (log.length === 0 && inst.throughput === '-') eaRefuse('Give a throughput, or a board log to measure it from');
    if (log.length === 0 && inst.wip.length === 0) eaRefuse('Give one or two work-in-process values, or a board log');
    if (log.length > 0 && inst.throughput !== '-') eaRefuse('Give a throughput or a board log, not both: with a log the throughput is measured from it (set the throughput to -)');
    log.forEach(function (x, i) {
      var w = 'Items, record ' + (i + 1) + ' (' + x.item + ')';
      if (Rcmp(x.start, end) > 0) eaRefuse(w + ': start ' + aktDec(x.start) + ' is after the end of the ' + dTxt + '-day window');
      if (x.done !== '-') {
        if (Rcmp(x.done, x.start) < 0) eaRefuse(w + ': done ' + aktDec(x.done) + ' is before start ' + aktDec(x.start));
        if (Rcmp(x.done, end) > 0) eaRefuse(w + ': done ' + aktDec(x.done) + ' is after the end of the ' + dTxt + '-day window');
      }
    });
    if (log.length) {
      var inProc = R0, leadSum = R0, done = 0, open = [];
      log.forEach(function (x) {
        var stop = x.done === '-' ? end : x.done, t = Rsub(stop, x.start);
        inProc = Radd(inProc, t);
        if (x.done === '-') { open.push(x.item); rows.push([x.item, aktDec(x.start), 'open', eaNum(t), '—']); }
        else { done += 1; leadSum = Radd(leadSum, t); rows.push([x.item, aktDec(x.start), aktDec(x.done), eaNum(t), eaNum(t)]); }
      });
      var L = Rdiv(inProc, end), lw = Rdiv(leadSum, end);
      thru = R(BigInt(done), D.n);
      tiles.aflAvgWip = aktUnit(L, 'items');
      tiles.aflAvgLead = done ? aktUnit(Rdiv(leadSum, R(BigInt(done))), 'days') : 'no item done';
      tiles.aflLittle = done === 0 ? 'no item done, so no lead time to check' : (Requ(L, lw)
        ? 'holds: average WIP ' + eaNum(L) + ' = throughput × average lead time'
        : 'differs: average WIP ' + eaNum(L) + ', throughput × average lead time ' + eaNum(lw) + ', because '
          + eaPlural(open.length, 'item is', 'items are') + ' still open at the end (' + open.join(', ') + ')');
      say = 'The board log over ' + eaPlural(D.n, 'day', 'days') + ': ' + eaPlural(done, 'item', 'items') + ' done, average work in process ' + eaNum(L);
    } else {
      thru = inst.throughput;
      tiles.aflAvgWip = 'no board log'; tiles.aflAvgLead = 'no board log'; tiles.aflLittle = 'no board log';
      say = 'At a throughput of ' + aktUnit(thru, 'items') + ' a day';
    }
    tiles.aflThru = aktUnit(thru, 'items') + ' a day';
    if (inst.wip.length && thru.n === 0n) eaRefuse('No item is done in the window, so the throughput is 0 and Little’s law gives no lead time for a work in process');
    var leads = inst.wip.map(function (w) { return Rdiv(w, thru); });
    tiles.aflLeadAt = inst.wip.length ? inst.wip.map(function (w, i) { return 'WIP ' + aktDec(w) + ': ' + aktUnit(leads[i], 'days'); }).join('; ') : 'no work in process given';
    tiles.aflChange = inst.wip.length === 2 ? aktTimes(Rdiv(leads[1], leads[0])) + ' the lead time (' + eaNum(leads[0]) + ' → ' + aktUnit(leads[1], 'days') + ')' : 'one value only';
    if (inst.wip.length) say += '; lead time = WIP / throughput is ' + leads.map(function (l) { return eaNum(l); }).join(' → ') + (leads.length === 1 && Requ(leads[0], R1) ? ' day' : ' days');
    if (!log.length) rows = inst.wip.map(function (w, i) { return [aktDec(w), eaNum(thru), eaNum(leads[i])]; });
    return {
      tiles: tiles, status: aktStatus(say),
      table: log.length ? { caption: 'Each item on the board, in days from the window start', head: ['item', 'start', 'done', 'days in process in the window', 'lead time'], rows: rows }
                        : { caption: 'Little’s law: lead time = work in process / throughput', head: ['work in process', 'throughput (a day)', 'lead time (days)'], rows: rows }
    };
  };
"""


def _check_utilization(inst, fixed):
    for i, lv in enumerate(inst["levels"]):
        if lv >= 100:
            raise ValueError("Utilization levels, entry %d is 100%%: there u/(1 − u) divides by zero, because work "
                             "arrives as fast as it can be done, so in this model the queue and the wait grow without "
                             "bound and no lead time exists" % (i + 1))


def _check_batch(inst, fixed):
    work = int(inst["work"])
    for i, b in enumerate(inst["batch"]):
        if int(b) > work:
            raise ValueError("Batch sizes, entry %d is %s, more than the work (%s items)" % (i + 1, ea.grp(int(b)), ea.grp(work)))


def _check_wip(inst, fixed):
    log, end, dtxt = inst["items"], Fraction(inst["days"]), ea.grp(int(inst["days"]))
    if not log and inst["throughput"] == "-":
        raise ValueError("Give a throughput, or a board log to measure it from")
    if not log and not inst["wip"]:
        raise ValueError("Give one or two work-in-process values, or a board log")
    if log and inst["throughput"] != "-":
        raise ValueError("Give a throughput or a board log, not both: with a log the throughput is measured from it "
                         "(set the throughput to -)")
    for i, x in enumerate(log):
        w = "Items, record %d (%s)" % (i + 1, x["item"])
        if x["start"] > end:
            raise ValueError("%s: start %s is after the end of the %s-day window" % (w, dec_text(x["start"]), dtxt))
        if x["done"] != "-":
            if x["done"] < x["start"]:
                raise ValueError("%s: done %s is before start %s" % (w, dec_text(x["done"]), dec_text(x["start"])))
            if x["done"] > end:
                raise ValueError("%s: done %s is after the end of the %s-day window" % (w, dec_text(x["done"]), dtxt))
    if log and inst["wip"] and not any(x["done"] != "-" for x in log):
        raise ValueError("No item is done in the window, so the throughput is 0 and Little’s law gives no lead time "
                         "for a work in process")


FLOW = {
    "prefix": "afl", "fn": "aflCompute", "title": "Flow", "js": AFL_JS,
    "views": {
        "utilization": {
            "fields": [("levels", alist("Utilization levels, percent (below 100)", ea.num(lo=0, hi=100), lo=1, hi=12,
                                        things="levels"), None),
                       ("service", ea.field("Service time of one job", rat(gt=0)), "1"),
                       ("unit", ea.field("Unit of time", _N), "hours")],
            "tiles": [("Levels", "aflLevels"), ("Queueing multiple u/(1 − u) at each level", "aflMultiples"),
                      ("Lead time at each level", "aflLeads"), ("Lead time at the highest level", "aflHigh"),
                      ("Highest level's lead time over the lowest's", "aflRatio")],
            "check": _check_utilization, "subtitle": "how lead time grows as utilization nears 100 percent",
            "rules": "The model is the simplest queue, a single server with random arrivals and random service "
                     "times (M/M/1), a simplification of any real team: at utilization u (the share of time busy) a "
                     "job waits u/(1 − u) service times in the queue on average, so its lead time is service × "
                     "(1 + u/(1 − u)) = service/(1 − u). Every figure is exact. At 100% the multiple divides by zero "
                     "and the lab refuses. Levels are shown in the order given; the highest and lowest are by value.",
            "js": AFL_VIEW_JS["utilization"],
        },
        "batch": {
            "fields": [("work", ea.field("Work items", ea.whole(1, 1000)), None),
                       ("batch", alist("Batch sizes (one, or two to compare)", ea.whole(1, 1000), lo=1, hi=2,
                                       things="batch sizes"), None),
                       ("per_item", ea.field("Time to do one item", rat(gt=0)), "1"),
                       ("release_cost", ea.field("Fixed time per release", rat(lo=0)), "0"),
                       ("unit", ea.field("Unit of time", _N), "days")],
            "tiles": [("Batches", "aflBatches"), ("Time to first feedback (first batch released)", "aflFirst"),
                      ("Time to last release", "aflLast"), ("Average wait per item (start to release)", "aflWait"),
                      ("Total release overhead", "aflOverhead"), ("First feedback, first size over second", "aflRatio")],
            "check": _check_batch, "subtitle": "what a smaller batch does to the wait for feedback",
            "rules": "One worker does the items one after another; a batch is released when its last item is done, "
                     "taking the fixed release time, and the next batch starts after the release. Batch i is released "
                     "at (items done through batch i) × time per item + i × release time; the last batch holds what "
                     "is left when the work does not divide evenly. Feedback on an item arrives when its batch is "
                     "released. The average wait is the mean, over items, of the time from the start to the item's "
                     "release. With two sizes each tile reads first → second.",
            "js": AFL_VIEW_JS["batch"],
        },
        "wip": {
            "fields": [("throughput", ea.field("Throughput, items a day (- to measure it from the log)", rat(gt=0, dash=True)), "-"),
                       ("wip", alist("Work in process (one value, or two: without and with a limit)", rat(gt=0),
                                     lo=0, hi=2, things="values"), ""),
                       ("days", ea.field("Days in the window (for a board log)", ea.whole(1, 366)), "10"),
                       ("items", arec("Board log (item, start day, done day or -)",
                                      [("item", _N), ("start", rat(lo=0, hi=366)), ("done", rat(lo=0, hi=366, dash=True))],
                                      unique=True, rows=4, lo=0), "")],
            "tiles": [("Throughput", "aflThru"), ("Average work in process (from the log)", "aflAvgWip"),
                      ("Average lead time of items done (from the log)", "aflAvgLead"),
                      ("Little's law on the log", "aflLittle"), ("Lead time at each work in process", "aflLeadAt"),
                      ("Second lead time over the first", "aflChange")],
            "check": _check_wip, "subtitle": "Little's law: work in process, throughput and lead time",
            "rules": "Little's law: average lead time = average work in process / throughput, for a stable system. "
                     "Give a throughput and one or two work-in-process values, or a board log of items with start "
                     "and done days (decimal days from the window's start, 0 to the window's length; - for an item "
                     "still open at the end) and the throughput is measured from it. From a log: average work in "
                     "process is the item-days in process inside the window over its days; throughput is the items "
                     "done over the days; average lead time is the mean of done − start for the items done. On a log "
                     "the law holds exactly when no item is open at the end; an open item adds to the work in process "
                     "but has no lead time yet, and the lab says so. Every figure is exact.",
            "js": AFL_VIEW_JS["wip"],
        },
    },
}

# ---------------------------------------------------------------------------
# branches (atb): trunk-based development from a month of branches
# ---------------------------------------------------------------------------

ATB_JS = r"""
  var ATB_VIEW = {};
  function atbCompute(view, inst, opts) { return eaRun(ATB_VIEW[view], inst, opts); }
"""

ATB_VIEW_JS = {}

ATB_VIEW_JS["trunk"] = r"""
  ATB_VIEW.trunk = function (inst) {
    var days = Number(inst.days.n), end = R(BigInt(days) * 24n), dTxt = eaInt(days), br = inst.branches;
    br.forEach(function (b, i) {
      var w = 'Branches, record ' + (i + 1) + ' (' + b.branch + ')';
      if (Rcmp(b.created, end) > 0) eaRefuse(w + ': created ' + aktTimeText(b.created) + ' is after the end of the ' + dTxt + '-day period');
      if (b.merged !== '-') {
        if (Rcmp(b.merged, end) > 0) eaRefuse(w + ': merged ' + aktTimeText(b.merged) + ' is after the end of the ' + dTxt + '-day period');
        if (Rcmp(b.merged, b.created) < 0) eaRefuse(w + ': merged ' + aktTimeText(b.merged) + ' is before created ' + aktTimeText(b.created));
      }
    });
    var seen = {};
    inst.freezes.forEach(function (d, i) {
      var k = String(d.n);
      if (d.n > BigInt(days)) eaRefuse('Freeze days, entry ' + (i + 1) + ' is day ' + k + ', after the ' + dTxt + '-day period');
      if (seen[k]) eaRefuse('Freeze days names day ' + k + ' twice');
      seen[k] = true;
    });
    /* the most branches open at one moment: a merge at t ends before a branch created at t begins */
    var ev = [];
    br.forEach(function (b) {
      ev.push({ t: b.created, d: 1 });
      if (b.merged !== '-') ev.push({ t: b.merged, d: -1 });
    });
    ev.sort(function (p, q) { var c = Rcmp(p.t, q.t); return c !== 0 ? c : p.d - q.d; });
    var cur = 0, max = 0, at = null;
    ev.forEach(function (e) { cur += e.d; if (cur > max) { max = cur; at = e.t; } });
    var lim = inst.life_hours, lives = [], over = [], young = [], open = [], rows = [];
    br.forEach(function (b) {
      if (b.merged === '-') {
        var age = Rsub(end, b.created);
        open.push(b.branch);
        if (Rcmp(age, lim) >= 0) over.push(b.branch + ' (open, at least ' + aktDur(age) + ')');
        else young.push(b.branch);
      } else {
        var life = Rsub(b.merged, b.created);
        lives.push(life);
        if (Rcmp(life, lim) >= 0) over.push(b.branch + ' (' + aktDur(life) + ')');
      }
    });
    var d;
    for (d = 1; d <= days; d += 1) {
      var lo = R(BigInt(d - 1) * 24n), hi = R(BigInt(d) * 24n), on = br.filter(function (b) {
        return Rcmp(b.created, hi) < 0 && (b.merged === '-' || Rcmp(b.merged, lo) >= 0);
      }).map(function (b) { return b.branch; });
      rows.push([String(d), String(on.length), eaNames(on), seen[String(d)] ? 'freeze' : '']);
    }
    var most = Number(inst.max_active.n), fz = inst.freezes.length, fzMax = Number(inst.freeze_max.n);
    var limTxt = aktDur(lim);
    var lifeMet = over.length ? 'no: ' + eaPlural(over.length, 'branch lived', 'branches lived') + ' ' + limTxt + ' or longer'
      : (young.length ? 'not yet determined: ' + eaPlural(young.length, 'branch is', 'branches are') + ' open and younger than ' + limTxt
        : 'yes: every branch merged in less than ' + limTxt);
    return {
      tiles: {
        atbBranches: eaInt(br.length),
        atbMaxActive: max === 0 ? '0' : eaInt(max) + ', first at ' + aktTimeText(at),
        atbMeanLife: lives.length ? aktDur(aktMean(lives)) : 'no branch merged',
        atbOver: aktListed(over.length, over, '; '),
        atbOpen: aktListed(open.length, open),
        atbFreeze: aktListed(fz, inst.freezes.map(function (x) { return 'day ' + String(x.n); })),
        atbMetActive: (max <= most ? 'yes: at most ' : 'no: ') + eaInt(max) + ' at once, and the threshold is at most ' + eaInt(most) + (most === 2 ? ' (fewer than three)' : ''),
        atbMetLife: lifeMet,
        atbMetFreeze: (fz <= fzMax ? 'yes: ' : 'no: ') + eaPlural(fz, 'freeze day', 'freeze days') + ', and the threshold is at most ' + eaInt(fzMax)
      },
      status: aktStatus(eaPlural(br.length, 'branch', 'branches') + ' over ' + eaPlural(days, 'day', 'days') + ': at most '
        + eaInt(max) + ' open at once, ' + eaInt(over.length) + ' living ' + limTxt + ' or longer, '
        + eaInt(open.length) + ' open at the end, ' + eaPlural(fz, 'freeze day', 'freeze days')),
      table: { caption: 'Each day: the branches that exist at some moment of it', head: ['day', 'branches', 'which', 'freeze'], rows: rows }
    };
  };
"""


def _check_trunk(inst, fixed):
    days = int(inst["days"])
    end, dtxt = Fraction(days * 24), ea.grp(days)
    for i, b in enumerate(inst["branches"]):
        w = "Branches, record %d (%s)" % (i + 1, b["branch"])
        if b["created"] > end:
            raise ValueError("%s: created %s is after the end of the %s-day period" % (w, time_text(b["created"]), dtxt))
        if b["merged"] != "-":
            if b["merged"] > end:
                raise ValueError("%s: merged %s is after the end of the %s-day period" % (w, time_text(b["merged"]), dtxt))
            if b["merged"] < b["created"]:
                raise ValueError("%s: merged %s is before created %s" % (w, time_text(b["merged"]),
                                                                         time_text(b["created"])))
    seen = set()
    for i, d in enumerate(inst["freezes"]):
        d = int(d)
        if d > days:
            raise ValueError("Freeze days, entry %d is day %d, after the %s-day period" % (i + 1, d, dtxt))
        if d in seen:
            raise ValueError("Freeze days names day %d twice" % d)
        seen.add(d)


BRANCHES = {
    "prefix": "atb", "fn": "atbCompute", "title": "Trunk-based development", "js": ATB_JS,
    "views": {
        "trunk": {
            "fields": [("days", ea.field("Days in the period", ea.whole(1, 92)), "30"),
                       ("branches", arec("Branches (branch, created, merged or - if still open; day.hh:mm)",
                                         [("branch", _N), ("created", CLOCK), ("merged", dict(CLOCK, dash=True))],
                                         unique=True, rows=5), None),
                       ("freezes", alist("Code-freeze days (day numbers; empty for none)", ea.whole(1, 366), lo=0,
                                         hi=92, things="days"), ""),
                       ("max_active", ea.field("Threshold: active branches at most", ea.whole(0, 60)), "2"),
                       ("life_hours", ea.field("Threshold: branch lifetime less than (hours)", rat(gt=0)), "24"),
                       ("freeze_max", ea.field("Threshold: freeze days at most", ea.whole(0, 92)), "0")],
            "tiles": [("Branches", "atbBranches"), ("Most branches open at once", "atbMaxActive"),
                      ("Mean lifetime of merged branches", "atbMeanLife"),
                      ("Branches living the limit or longer", "atbOver"), ("Open at the end", "atbOpen"),
                      ("Freeze days", "atbFreeze"), ("Active branches threshold met", "atbMetActive"),
                      ("Lifetime threshold met", "atbMetLife"), ("Freeze threshold met", "atbMetFreeze")],
            "check": _check_trunk, "subtitle": "active branches, lifetimes and freezes against the thresholds",
            "rules": "A time is day.hh:mm (1.09:30 is day 1 at 09:30; day 1 begins at hour 0); a bare day number is "
                     "refused, since it cannot tell whether a branch lived less than a day. A branch is open from its creation until its merge (a merge at the same moment as "
                     "another branch's creation ends first); - means it is still open at the period's end. Its "
                     "lifetime is merged − created. The thresholds default to the book's (Chapter 4): fewer than "
                     "three active branches at any time (at most 2), lifetimes of less than a day, no code freezes; a lesson may "
                     "state others. A branch living the limit or longer fails the lifetime threshold; an open branch "
                     "fails it once its age at the period's end reaches the limit, and while it is younger its "
                     "lifetime is not yet known. The table counts a branch on a day when it exists at some moment "
                     "of it: created before the day ends and not merged before the day begins.",
            "js": ATB_VIEW_JS["trunk"],
        },
    },
}

# ---------------------------------------------------------------------------
# release (arl): release groups from ties, and deploys per developer at scale
# ---------------------------------------------------------------------------

ARL_JS = r"""
  var ARL_VIEW = {};
  function arlCompute(view, inst, opts) { return eaRun(ARL_VIEW[view], inst, opts); }
  function arlRate(r) { return Rint(r) ? eaInt(r.n) : eaFrac(r) + (eaExactAt(r, 3) ? ' = ' : ' ≈ ') + eaFixed(r, 3); }
"""

ARL_VIEW_JS = {}

ARL_VIEW_JS["independent"] = r"""
  function arlGroupsOf(names, ties) {
    var parent = {};
    names.forEach(function (c) { parent[c] = c; });
    var find = function (x) { while (parent[x] !== x) x = parent[x]; return x; };
    ties.forEach(function (t) { var a = find(t.a), b = find(t.b); if (a !== b) { if (names.indexOf(a) < names.indexOf(b)) parent[b] = a; else parent[a] = b; } });
    var by = {}, out = [];
    names.forEach(function (c) { var r = find(c); if (!by[r]) { by[r] = []; out.push(by[r]); } by[r].push(c); });
    return out;
  }
  ARL_VIEW.independent = function (inst) {
    var names = inst.components, team = {}, withTeam = inst.teams.length > 0;
    inst.teams.forEach(function (t, i) {
      if (names.indexOf(t.component) < 0) eaRefuse('Teams, record ' + (i + 1) + ': ' + t.component + ' is not one of the components');
      team[t.component] = t.team;
    });
    if (withTeam) names.forEach(function (c) { if (team[c] === undefined) eaRefuse('Give a team for every component or for none; ' + c + ' has none'); });
    var key = function (t) { return t.a < t.b ? t.a + '\u0000' + t.b : t.b + '\u0000' + t.a; }, keys = {};
    inst.ties.forEach(function (t, i) {
      [t.a, t.b].forEach(function (x) { if (names.indexOf(x) < 0) eaRefuse('Ties, record ' + (i + 1) + ': ' + x + ' is not one of the components'); });
      if (t.a === t.b) eaRefuse('Ties, record ' + (i + 1) + ': ' + t.a + ' is tied to itself');
      if (keys[key(t)]) eaRefuse('Ties, record ' + (i + 1) + ': the tie ' + t.a + '–' + t.b + ' is given twice');
      keys[key(t)] = true;
    });
    var rm = inst.remove.length ? inst.remove[0] : null;
    if (rm && !keys[key(rm)]) eaRefuse('The tie to remove, ' + rm.a + '–' + rm.b + ', is not one of the ties');
    var show = function (g) { return '{' + g.join(', ') + '}'; };
    var sum = function (groups) {
      var big = groups.reduce(function (m, g) { return g.length > m.length ? g : m; }, []);
      var alone = groups.filter(function (g) { return g.length === 1; }).map(function (g) { return g[0]; });
      var coord = [];
      if (withTeam) groups.forEach(function (g) {
        var ts = [];
        g.forEach(function (c) { if (ts.indexOf(team[c]) < 0) ts.push(team[c]); });
        if (ts.length > 1) coord.push(ts.join(' + ') + ' for ' + show(g));
      });
      return { groups: aktListed(groups.length, groups.map(show)), big: eaInt(big.length) + ': ' + big.join(', '), alone: eaCount(alone),
               coord: !withTeam ? 'no teams given' : (coord.length === 0 ? 'none: every release group belongs to one team' : eaInt(coord.length) + (coord.length === 1 ? ' group spans' : ' groups span') + ' more than one team: ' + coord.join('; ')), n: groups.length };
    };
    var g0 = arlGroupsOf(names, inst.ties), s0 = sum(g0), s1 = null, change = 'no tie removed';
    if (rm) {
      var kept = inst.ties.filter(function (t) { return key(t) !== key(rm); }), g1 = arlGroupsOf(names, kept);
      s1 = sum(g1);
      change = g1.length > g0.length ? 'removing ' + rm.a + '–' + rm.b + ' splits a group: ' + eaInt(g0.length) + ' → ' + eaInt(g1.length) + ' release groups'
        : 'removing ' + rm.a + '–' + rm.b + ' changes no group: ' + rm.a + ' and ' + rm.b + ' are still tied through others';
    }
    var none = 'no tie removed', rows = g0.map(function (g, i) {
      return [String(i + 1), g.join(', '), String(g.length), withTeam ? g.map(function (c) { return team[c]; }).filter(function (t, j, a) { return a.indexOf(t) === j; }).join(', ') : '—'];
    });
    return {
      tiles: {
        arlGroups: s0.groups, arlLargest: s0.big, arlAlone: s0.alone, arlCoord: s0.coord, arlRemoved: change,
        arlAfterGroups: s1 ? s1.groups : none, arlAfterAlone: s1 ? s1.alone : none, arlAfterCoord: s1 ? s1.coord : none
      },
      status: aktStatus(eaPlural(names.length, 'component', 'components') + ' and ' + eaPlural(inst.ties.length, 'tie', 'ties')
        + ' make ' + eaPlural(s0.n, 'release group', 'release groups') + (s1 ? '; without ' + rm.a + '–' + rm.b + ', ' + eaInt(s1.n) : '')),
      table: { caption: 'Each release group (components that must be released together)', head: ['group', 'components', 'size', 'teams'], rows: rows }
    };
  };
"""

ARL_VIEW_JS["scaling"] = r"""
  ARL_VIEW.scaling = function (inst) {
    var orgs = inst.orgs, days = inst.days;
    orgs.forEach(function (o, i) {
      orgs.forEach(function (p, j) {
        if (j < i && Requ(o.developers, p.developers)) eaRefuse('Organizations, record ' + (i + 1) + ' (' + o.org + ') has as many developers as ' + p.org + ' (' + eaInt(o.developers.n) + '); this view orders by size, so each needs a different number');
      });
    });
    var s = orgs.map(function (o) { return { o: o, r: Rdiv(o.deploys, Rmul(o.developers, days)) }; });
    s.sort(function (a, b) { return Rcmp(a.o.developers, b.o.developers); });
    var up = 0, down = 0, flat = 0, rows = [];
    s.forEach(function (x, i) {
      var c = i ? Rcmp(x.r, s[i - 1].r) : null;
      if (c === 1) up += 1; else if (c === -1) down += 1; else if (c === 0) flat += 1;
      rows.push([x.o.org, eaInt(x.o.developers.n), eaInt(x.o.deploys.n), arlRate(x.r), c === null ? '' : (c > 0 ? 'rises' : (c < 0 ? 'falls' : 'holds'))]);
    });
    var steps = s.length - 1, trend;
    if (flat === steps) trend = 'holds: the same at every size';
    else if (up === steps) trend = 'rises at every step';
    else if (down === steps) trend = 'falls at every step';
    else if (down === 0) trend = 'rises or holds, never falls';
    else if (up === 0) trend = 'falls or holds, never rises';
    else trend = 'rises and falls: no single direction';
    var first = s[0], last = s[s.length - 1];
    var who = function (x) { return x.o.org + ' (' + eaPlural(x.o.developers.n, 'developer', 'developers') + '): ' + arlRate(x.r); };
    return {
      tiles: {
        arlOrgs: eaInt(orgs.length), arlRates: s.map(who).join('; '), arlSmall: who(first), arlBig: who(last),
        arlTrend: 'from ' + first.o.org + ' to ' + last.o.org + ', the rate ' + trend
      },
      status: aktStatus('Deploys per developer per day over ' + eaPlural(days.n, 'day', 'days') + ', smallest to largest: ' + trend + ', in these rows'),
      table: { caption: 'Each organization by size: deploys per developer per day', head: ['organization', 'developers', 'deploys', 'per developer per day', 'from the one before'], rows: rows }
    };
  };
"""


def _check_independent(inst, fixed):
    names, teams = inst["components"], {}
    for i, t in enumerate(inst["teams"]):
        if t["component"] not in names:
            raise ValueError("Teams, record %d: %s is not one of the components" % (i + 1, t["component"]))
        teams[t["component"]] = t["team"]
    if inst["teams"]:
        for c in names:
            if c not in teams:
                raise ValueError("Give a team for every component or for none; %s has none" % c)
    keys = set()
    for i, t in enumerate(inst["ties"]):
        for x in (t["a"], t["b"]):
            if x not in names:
                raise ValueError("Ties, record %d: %s is not one of the components" % (i + 1, x))
        if t["a"] == t["b"]:
            raise ValueError("Ties, record %d: %s is tied to itself" % (i + 1, t["a"]))
        k = frozenset((t["a"], t["b"]))
        if k in keys:
            raise ValueError("Ties, record %d: the tie %s–%s is given twice" % (i + 1, t["a"], t["b"]))
        keys.add(k)
    if inst["remove"]:
        rm = inst["remove"][0]
        if frozenset((rm["a"], rm["b"])) not in keys:
            raise ValueError("The tie to remove, %s–%s, is not one of the ties" % (rm["a"], rm["b"]))


def _check_scaling(inst, fixed):
    orgs = inst["orgs"]
    for i, o in enumerate(orgs):
        for j, p in enumerate(orgs[:i]):
            if o["developers"] == p["developers"]:
                raise ValueError("Organizations, record %d (%s) has as many developers as %s (%s); this view orders "
                                 "by size, so each needs a different number"
                                 % (i + 1, o["org"], p["org"], ea.grp(int(o["developers"]))))


_TIE = [("a", _N), ("b", _N)]

RELEASE = {
    "prefix": "arl", "fn": "arlCompute", "title": "Release independence", "js": ARL_JS,
    "views": {
        "independent": {
            "fields": [("components", alist("Components (names)", _N, lo=1, hi=60, things="components", control="area"), None),
                       ("teams", ea.rec("Teams (component, team; empty for none)", [("component", _N), ("team", _N)],
                                        unique=True, rows=3, lo=0), ""),
                       ("ties", ea.rec("Must release together (a, b)", _TIE, rows=4, lo=0), ""),
                       ("remove", ea.rec("Remove this tie (a, b; empty for none)", _TIE, rows=1, lo=0, hi=1), "")],
            "tiles": [("Release groups", "arlGroups"), ("Largest group", "arlLargest"),
                      ("Deployable alone", "arlAlone"), ("Teams that must coordinate a release", "arlCoord"),
                      ("The tie removed", "arlRemoved"), ("Release groups after", "arlAfterGroups"),
                      ("Deployable alone after", "arlAfterAlone"), ("Teams that must coordinate after", "arlAfterCoord")],
            "check": _check_independent, "subtitle": "which components can be released on their own",
            "rules": "A tie a, b says the two components must be released together, in either direction; ties chain, "
                     "so a release group is every component reachable from another through ties (a connected "
                     "component). A component in a group of one is deployable alone. When components carry teams, "
                     "a group holding more than one team's components makes those teams coordinate its release. "
                     "Groups are listed in the order of their first component in the input, and the largest group "
                     "is the first of the largest size. With a tie to remove, the after tiles are the same counts "
                     "without it.",
            "js": ARL_VIEW_JS["independent"],
        },
        "scaling": {
            "fields": [("orgs", ea.rec("Organizations (org, developers, deploys in the period)",
                                       [("org", _N), ("developers", ea.whole(1, ea.LIMIT)), ("deploys", ea.whole(0, ea.LIMIT))],
                                       unique=True, rows=4, lo=2, hi=30), None),
                       ("days", ea.field("Days in the period", ea.whole(1, 366)), "30")],
            "tiles": [("Organizations", "arlOrgs"), ("Deploys per developer per day, by size", "arlRates"),
                      ("Smallest", "arlSmall"), ("Largest", "arlBig"), ("As size grows", "arlTrend")],
            "check": _check_scaling, "subtitle": "deploys per developer per day as an organization grows",
            "rules": "Deploys per developer per day = deploys / (developers × days), an exact fraction, shown to three "
                     "places. Organizations are ordered by developers, smallest first; two with the same number are "
                     "refused. Each step to the next larger organization rises, holds or falls; the trend says "
                     "whether every step rises, holds or falls, or which mix, as of these rows only.",
            "js": ARL_VIEW_JS["scaling"],
        },
    },
}

# ---------------------------------------------------------------------------
# change (acm): lead time and change fail rate by approval route
# ---------------------------------------------------------------------------

ACM_JS = r"""
  var ACM_VIEW = {};
  function acmCompute(view, inst, opts) { return eaRun(ACM_VIEW[view], inst, opts); }
"""

ACM_VIEW_JS = {}

ACM_VIEW_JS["approval"] = r"""
  ACM_VIEW.approval = function (inst) {
    var ch = inst.changes, routes = [], by = {};
    ch.forEach(function (c) {
      if (!by[c.route]) { by[c.route] = { waits: [], failed: 0 }; routes.push(c.route); }
      by[c.route].waits.push(c.wait);
      if (c.failed === 'yes') by[c.route].failed += 1;
    });
    if (inst.compare.length === 1) eaRefuse('Name two routes to compare, or none (the first two routes met are compared)');
    inst.compare.forEach(function (r) { if (!by[r]) eaRefuse('The route ' + r + ' is not used by any change'); });
    var rate = function (r) { return R(BigInt(by[r].failed), BigInt(by[r].waits.length)); };
    var rows = routes.map(function (r) {
      var b = by[r];
      return [r, eaInt(b.waits.length), aktDur(aktMean(b.waits)), aktDur(aktMedian(b.waits)), eaInt(b.failed), eaPct(rate(r))];
    });
    var failed = ch.filter(function (c) { return c.failed === 'yes'; }).length;
    var pair = inst.compare.length === 2 ? inst.compare : routes.slice(0, 2), diff;
    if (pair.length < 2) diff = 'one route only';
    else diff = pair[0] + ' ' + eaPct(rate(pair[0])) + ' against ' + pair[1] + ' ' + eaPct(rate(pair[1])) + ': ' + aktPp(Rsub(rate(pair[0]), rate(pair[1])));
    var list = function (f) { return routes.map(function (r) { return r + ' ' + f(r); }).join('; '); };
    return {
      tiles: {
        acmChanges: eaInt(ch.length),
        acmRoutes: aktListed(routes.length, routes.map(function (r) { return r + ' (' + by[r].waits.length + ')'; })),
        acmMeanWait: list(function (r) { return aktDur(aktMean(by[r].waits)); }),
        acmMedianWait: list(function (r) { return aktDur(aktMedian(by[r].waits)); }),
        acmFail: list(function (r) { return eaPct(rate(r)); }),
        acmOverall: eaPct(R(BigInt(failed), BigInt(ch.length))),
        acmDiff: diff
      },
      status: aktStatus(eaPlural(ch.length, 'change', 'changes') + ' by ' + eaPlural(routes.length, 'route', 'routes')
        + (pair.length === 2 ? '; the fail rate of ' + pair[0] + ' minus ' + pair[1] + ' is ' + aktPp(Rsub(rate(pair[0]), rate(pair[1]))) : '')
        + '; a difference between routes in a sample says nothing of what causes it'),
      table: { caption: 'Each approval route: the wait it adds and its change fail rate', head: ['route', 'changes', 'mean wait', 'median wait', 'failed', 'change fail rate'], rows: rows }
    };
  };
"""


def _check_approval(inst, fixed):
    routes = {c["route"] for c in inst["changes"]}
    if len(inst["compare"]) == 1:
        raise ValueError("Name two routes to compare, or none (the first two routes met are compared)")
    for r in inst["compare"]:
        if r not in routes:
            raise ValueError("The route %s is not used by any change" % r)


CHANGE = {
    "prefix": "acm", "fn": "acmCompute", "title": "Change approval", "js": ACM_JS,
    "views": {
        "approval": {
            "fields": [("changes", arec("Changes (change, route, wait in hours, failed yes or no)",
                                          [("change", _N), ("route", _N), ("wait", rat(lo=0)), ("failed", ea.YESNO)],
                                          unique=True, rows=5), None),
                       ("compare", alist("Two routes to compare (empty: the first two met)", _N, lo=0, hi=2,
                                         things="routes"), "")],
            "tiles": [("Changes", "acmChanges"), ("Changes by route", "acmRoutes"),
                      ("Mean wait each route adds", "acmMeanWait"), ("Median wait each route adds", "acmMedianWait"),
                      ("Change fail rate by route", "acmFail"), ("Change fail rate overall", "acmOverall"),
                      ("Difference in fail rate between two routes", "acmDiff")],
            "check": _check_approval, "subtitle": "what each approval route adds to lead time, and its fail rate",
            "rules": "Each change went through one approval route (a name: none, peer, cab, …) and waited the hours "
                     "given for it. Per route: the mean wait, the median wait (the middle value, or the mean of the "
                     "two middle ones), and the change fail rate, failed over changes, exact. The difference is the "
                     "first route's rate minus the second's, in percentage points, for the two routes named or else "
                     "the first two met. Routes are listed in the order first met. A difference in this sample "
                     "describes the sample; it is not evidence of what an approval step causes.",
            "js": ACM_VIEW_JS["approval"],
        },
    },
}

# ---------------------------------------------------------------------------
# work (awk): hours by kind of work, and what a scaling frees
# ---------------------------------------------------------------------------

AWK_JS = r"""
  var AWK_VIEW = {};
  function awkCompute(view, inst, opts) { return eaRun(AWK_VIEW[view], inst, opts); }
"""

AWK_VIEW_JS = {}

AWK_VIEW_JS["split"] = r"""
  AWK_VIEW.split = function (inst) {
    var kinds = inst.kinds, h = {}, nw = inst['new'], st = {}, stages = [];
    if (kinds.indexOf(nw) < 0) eaRefuse('The new-work kind ' + nw + ' is not one of the kinds (' + kinds.join(', ') + ')');
    kinds.forEach(function (k) { h[k] = R0; });
    inst.entries.forEach(function (e, i) {
      if (kinds.indexOf(e.kind) < 0) eaRefuse('Entries, record ' + (i + 1) + ': ' + e.kind + ' is not one of the kinds (' + kinds.join(', ') + ')');
      h[e.kind] = Radd(h[e.kind], e.hours);
      if (e.rest.length) {
        if (!st[e.rest[0]]) { st[e.rest[0]] = R0; stages.push(e.rest[0]); }
        st[e.rest[0]] = Radd(st[e.rest[0]], e.hours);
      }
    });
    var total = eaSum(kinds.map(function (k) { return h[k]; })), sc = inst.scale.length ? inst.scale[0] : null, move = inst.move === 'yes';
    var after = {}, freed = R0;
    kinds.forEach(function (k) { after[k] = h[k]; });
    if (sc) {
      if (kinds.indexOf(sc.kind) < 0) eaRefuse('The scaling names ' + sc.kind + ', which is not one of the kinds (' + kinds.join(', ') + ')');
      if (move && sc.kind === nw) eaRefuse('Scaling the new work itself frees nothing for it; scale another kind, or set freed hours to go to new work to no');
      after[sc.kind] = Rmul(h[sc.kind], sc.factor);
      freed = Rsub(h[sc.kind], after[sc.kind]);
      if (move) {
        after[nw] = Radd(after[nw], freed);
        if (Rsign(after[nw]) < 0) eaRefuse('Scaling ' + sc.kind + ' by ' + aktDec(sc.factor) + ' adds ' + aktUnit(Rneg(freed), 'hours') + ', more than the new work’s ' + aktUnit(h[nw], 'hours'));
      }
    }
    var total2 = move ? total : Rsub(total, freed);
    var share = function (x, t) { return Rzero(t) ? R0 : Rdiv(x, t); };
    var rows = kinds.map(function (k) {
      return [k, eaNum(h[k]), eaPct(share(h[k], total))].concat(sc ? [eaNum(after[k]), eaPct(share(after[k], total2))] : []);
    });
    var list = function (f) { return kinds.map(function (k) { return k + ' ' + f(k); }).join('; '); };
    var none = 'no scaling given';
    return {
      tiles: {
        awkStages: stages.length ? stages.map(function (x) { return x + ' ' + eaNum(st[x]); }).join('; ') : 'no stages given',
        awkTotal: aktUnit(total, 'hours'), awkHours: list(function (k) { return eaNum(h[k]); }),
        awkShares: list(function (k) { return eaPct(share(h[k], total)); }), awkNew: eaPct(share(h[nw], total)),
        awkFreed: sc ? aktUnit(freed, 'hours') + ' (' + sc.kind + ' ' + eaNum(h[sc.kind]) + ' → ' + eaNum(after[sc.kind]) + ')' + (move ? ', to ' + nw : ', total ' + eaNum(total2)) : none,
        awkAfter: sc ? list(function (k) { return eaPct(share(after[k], total2)); }) : none,
        awkNewAfter: sc ? eaPct(share(after[nw], total2)) : none
      },
      status: aktStatus(aktUnit(total, 'hours') + ', ' + eaPct(share(h[nw], total)) + ' of them ' + nw
        + (sc ? '; with ' + sc.kind + ' × ' + aktDec(sc.factor) + ', ' + nw + ' is ' + eaPct(share(after[nw], total2)) : '')),
      table: { caption: 'Hours and share by kind of work' + (sc ? ', before and after the scaling' : ''),
               head: ['kind', 'hours', 'share'].concat(sc ? ['hours after', 'share after'] : []), rows: rows }
    };
  };
"""


def _check_split(inst, fixed):
    kinds, nw = inst["kinds"], inst["new"]
    ks = ", ".join(kinds)
    if nw not in kinds:
        raise ValueError("The new-work kind %s is not one of the kinds (%s)" % (nw, ks))
    h = {k: Fraction(0) for k in kinds}
    for i, e in enumerate(inst["entries"]):
        if e["kind"] not in kinds:
            raise ValueError("Entries, record %d: %s is not one of the kinds (%s)" % (i + 1, e["kind"], ks))
        h[e["kind"]] += e["hours"]
    if inst["scale"]:
        sc, move = inst["scale"][0], inst["move"] == "yes"
        if sc["kind"] not in kinds:
            raise ValueError("The scaling names %s, which is not one of the kinds (%s)" % (sc["kind"], ks))
        if move and sc["kind"] == nw:
            raise ValueError("Scaling the new work itself frees nothing for it; scale another kind, or set freed hours "
                             "to go to new work to no")
        freed = h[sc["kind"]] - h[sc["kind"]] * sc["factor"]
        if move and h[nw] + freed < 0:
            raise ValueError("Scaling %s by %s adds %s, more than the new work’s %s"
                             % (sc["kind"], dec_text(sc["factor"]), unit_text(-freed, "hours"), unit_text(h[nw], "hours")))


WORK = {
    "prefix": "awk", "fn": "awkCompute", "title": "Where the time goes", "js": AWK_JS,
    "views": {
        "split": {
            "fields": [("kinds", alist("Kinds of work (2 to 10 names, in order)", _N, lo=2, hi=10, things="kinds"),
                        "new unplanned rework"),
                       ("new", ea.field("The kind that is new work", _N), "new"),
                       ("entries", arec("Entries (kind, hours, then a stage if any)", [("kind", _N), ("hours", rat(gt=0))], _N,
                                        "stage", 0, 1, rows=4), None),
                       ("scale", arec("Scale one kind (kind, factor; empty for none)",
                                      [("kind", _N), ("factor", rat(lo=0, hi=10))], rows=1, lo=0, hi=1), ""),
                       ("move", ea.choice("Freed hours go to new work", "yes", "no"), "yes")],
            "tiles": [("Total", "awkTotal"), ("Hours by kind", "awkHours"), ("Share by kind", "awkShares"),
                      ("New work's share", "awkNew"), ("Hours by stage (entries that give one)", "awkStages"), ("Hours freed by the scaling", "awkFreed"),
                      ("Shares after the scaling", "awkAfter"), ("New work's share after", "awkNewAfter")],
            "check": _check_split, "subtitle": "hours by kind of work, and what less rework frees",
            "rules": "Entries are summed by kind; a kind may appear in several entries, and a kind with none has 0 "
                     "hours. An entry may name a stage (where the work was found or done); hours by stage sum the "
                     "entries that give one, in the order first met. A share is the kind's hours over the total, exact. A scaling multiplies one kind's hours "
                     "by the factor (1/2 halves it); the hours freed are the difference. When freed hours go to new "
                     "work, they are added to the new-work kind and the total stays the same; otherwise the total "
                     "falls by them. Kinds are listed in the order given.",
            "js": AWK_VIEW_JS["split"],
        },
    },
}

SPECS = {"delivery": DELIVERY, "flow": FLOW, "branches": BRANCHES, "release": RELEASE, "change": CHANGE, "work": WORK}
MODES_A = tuple(SPECS)


def _family_b():
    """acckit_b.MODES, imported on first use; {} while acckit_b.py does not exist."""
    try:
        from . import acckit_b
    except ModuleNotFoundError as exc:
        if exc.name and exc.name.endswith("acckit_b"):
            return {}
        raise
    return acckit_b.MODES


def acckit_lab(cfg):
    """The Accelerate kit: cfg["mode"] chooses the mode, cfg["view"] the view."""
    cfg = cfg or {}
    mode = cfg.get("mode")
    if mode in SPECS:
        return mode_lab(cfg, mode, SPECS[mode])
    family_b = _family_b()
    if mode in family_b:
        return family_b[mode](cfg)
    raise ValueError("acckit_lab: unknown mode %r; the modes are %s"
                     % (mode, ", ".join(MODES_A + tuple(m for m in family_b if m not in SPECS))))


__all__ = ["acckit_lab", "mode_lab", "family_intro", "AKT_CORE_JS", "SPECS", "MODES_A", "KIT", "CAUTION",
           "FAMILY_SENTENCE", "arec", "alist", "rat", "TIME", "CLOCK", "parse_field", "to_text", "sqrt_fixed", "root_signed",
           "sqrt_exact", "parse_dec", "parse_rat", "parse_time", "dec_text", "time_text", "median", "pp_text"]
