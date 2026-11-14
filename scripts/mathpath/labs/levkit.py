"""levkit -- the lab kit of Leviathan, Read Along.

Specified in docs/leviathan/PLAN.md sections 0 and D; the report an author
configures a lesson from is docs/leviathan/kit-report.md, and the seam
between this module and levkit_b.py is docs/leviathan/kit-contract.md.
Built on eakit_core (imported as `ea`, unchanged) exactly as acckit is: its
field parser, printers, markup and wiring, with field kinds of this kit's own
(a rational cell, a cell of names, records with a variable tail, lists of
either) read by `lvkRead` before eakit's `eaField`.

Family A (this module), names, deliberation, worth, equality, covenants:

  reckon      (lrk)  names
  deliberate  (lde)  will
  worth       (lwo)  price
  equality    (leq)  coalition
  covenant    (lcv)  perform, fool

Family B (levkit_b.py): assembly, succession, tax, law, canon.
`levkit_lab` dispatches them through `levkit_b.MODES`, imported lazily so this
module imports before levkit_b.py exists.

THE BUILDER SIGNATURE (both families). A mode is built by
`builder(cfg) -> common.Lab`, where cfg is the lesson's lab cfg as written
(cfg["mode"] names the mode). Every builder in this kit is
`lambda cfg: mode_lab(cfg, <mode>, <SPEC>)`. The first view is the default.
A page ships RATIONAL_JS, EA_CORE_JS, LVK_CORE_JS, its mode's base block and
its own view's block -- never the other views or modes (page weight).

IDS. PLAN section D's prefixes, unchanged (grepped against
scripts/mathpath/labs/*.py and scripts/*.js on 2026-11-14). Shared helpers
begin lvk / LVK_.

EXACTNESS. Every figure is a count, a list of names, or an exact BigInt
rational. Nothing typed is evaluated as script.
"""

import re
from fractions import Fraction

from . import eakit_core as ea
from .algebra_core import RATIONAL_JS
from .common import Lab, cfg_literal

KIT = "levkit"
CAUTION = "the figure follows from what the lesson states, on Hobbes’s definitions as stated"
FAMILY_SENTENCE = "A figure computed from what the lesson states."

# ---------------------------------------------------------------------------
# Shared JavaScript, on every levkit page (both families)
# ---------------------------------------------------------------------------

LVK_CORE_JS = r"""
  /* levkit's shared helpers (docs/leviathan/kit-contract.md section 3a). */
  var LVK_CAUTION = 'the figure follows from what the lesson states, on Hobbes’s definitions as stated';
  function lvkStatus(s) { return String(s).replace(/[.\s]+$/, '') + '; ' + LVK_CAUTION + '.'; }
  function lvkListed(n, parts, sep) { return n === 0 ? '0: none' : eaInt(n) + ': ' + parts.join(sep || ', '); }
  /* A rational that has a finite decimal, as typed: 3, 0.25, −1.5 (no grouping). */
  function lvkDec(r) {
    var neg = r.n < 0n, n = neg ? -r.n : r.n, whole = n / r.d, rem = n % r.d, frac = '', i;
    for (i = 0; i < 12 && rem !== 0n; i += 1) { rem *= 10n; frac += String(rem / r.d); rem %= r.d; }
    return (neg ? EA_MINUS : '') + String(whole) + (frac ? '.' + frac : '') + (rem !== 0n ? '…' : '');
  }
  /* A chance or share: "1/4 = 25%", "1/8 = 12.5%", "1/3 ≈ 33.33%" (at most two places). */
  function lvkPct(r) {
    var p = Rmul(r, R(100n)), t = eaFixed(p, 2);
    if (t.indexOf('.') >= 0) t = t.replace(/0+$/, '').replace(/\.$/, '');
    return (Rint(r) ? eaInt(r.n) : eaFrac(r)) + (eaExactAt(p, 2) ? ' = ' : ' ≈ ') + t + '%';
  }
  function lvkParseRat(text, what) {
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
  /* --- levkit's field kinds (kit-contract.md section 4) ------------------- */
  /* A cell of names separated by spaces; "-" alone for none when f.dash. */
  function lvkNameSeq(text, f, what) {
    var s = eaClean(text);
    if (s === '') throw new Error(what + ' is empty');
    if (s === '-') {
      if (f.dash) return [];
      throw new Error(what + ' cannot be "-", which marks none');
    }
    var toks = s.split(/\s+/);
    if (toks.length > 40) throw new Error(what + ' holds at most 40 names, and there are ' + toks.length);
    toks.forEach(function (t, i) {
      if (t === '-') throw new Error(what + ' puts "-" among other names; "-" alone marks none');
      if (!EA_NAME.test(t)) throw new Error(what + ' ' + eaQuote(t) + ' should be letters, digits, dots, hyphens or underscores (a name of several words takes hyphens: round-quadrangle)');
      if (toks.indexOf(t) !== i) throw new Error(what + ' names ' + eaQuote(t) + ' twice');
    });
    return toks;
  }
  function lvkBound(r, f, what, s) {
    if (f.gt !== undefined && Rcmp(r, Rparse(f.gt)) <= 0) throw new Error(what + ' must be more than ' + eaNum(Rparse(f.gt)) + ', and it is ' + s);
    if (f.min !== undefined && Rcmp(r, Rparse(f.min)) < 0) throw new Error(what + ' cannot be less than ' + eaNum(Rparse(f.min)) + ', and it is ' + s);
    if (f.max !== undefined && Rcmp(r, Rparse(f.max)) > 0) throw new Error(what + ' is at most ' + eaNum(Rparse(f.max)) + ', and it is ' + s);
    return r;
  }
  function lvkScalar(f, text, what) {
    var s = eaClean(text);
    if (f.kind === 'rat' && f.dash && s === '-') return '-';
    if (f.kind === 'rat') return lvkBound(lvkParseRat(s, what), f, what, s.replace('-', EA_MINUS));
    if (f.kind === 'names') return lvkNameSeq(s, f, what);
    return eaScalar(f, s, what);
  }
  function lvkRecords(text, f, what) {
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
      f.sub.forEach(function (kk, j) { rec[kk[0]] = lvkScalar(kk[1], cells[j], w + ': ' + kk[0]); });
      rec.rest = cells.slice(n).map(function (c, j) { return lvkScalar(f.rest, c, w + ': ' + f.restWhat + ' ' + (j + 1)); });
      if (f.unique) {
        if (Object.prototype.hasOwnProperty.call(seen, cells[0])) throw new Error(what + ' names ' + eaQuote(cells[0]) + ' twice');
        seen[cells[0]] = true;
      }
      return rec;
    });
  }
  function lvkList(text, f, what) {
    var s = eaClean(text), toks = s === '' ? [] : s.split(/[\s,]+/).filter(function (t) { return t !== ''; });
    eaSized(toks.length, f, what, f.things);
    var vals = toks.map(function (t, i) { return lvkScalar(f.each, t, what + ', entry ' + (i + 1)); });
    if (f.each.kind === 'name') {
      toks.forEach(function (t, i) { if (toks.indexOf(t) !== i) throw new Error(what + ' names ' + eaQuote(t) + ' twice'); });
    }
    return vals;
  }
  function lvkRead(spec, raw) {
    var out = {};
    spec.forEach(function (f) {
      if (f.kind === 'lrec') out[f.key] = lvkRecords(raw[f.key], f, f.what);
      else if (f.kind === 'llist') out[f.key] = lvkList(raw[f.key], f, f.what);
      else if (f.kind === 'rat' || f.kind === 'names') out[f.key] = lvkScalar(f, raw[f.key], f.what);
      else out[f.key] = eaField(f, raw[f.key]);
    });
    return out;
  }
"""

# ---------------------------------------------------------------------------
# Python mirrors of the shared helpers (kit-contract.md section 3b)
# ---------------------------------------------------------------------------

_NUMBER = re.compile(r"^-?(?:\d+(?:\.(\d+))?|\.(\d+))$")
_RAT = re.compile(r"^(-?\d+)/(\d+)$")
_NAME = re.compile(r"^[A-Za-z0-9._-]+$")
MINUS = "−"


def _clean(text):
    return str("" if text is None else text).replace(MINUS, "-").strip()


def quote(s):
    """eaQuote."""
    s = str(s)
    return '"%s"' % (s[:40] + "…" if len(s) > 40 else s)


def plural(n, one, many):
    """eaPlural."""
    return "%s %s" % (ea.grp(n), one if n == 1 else many)


def dec_text(fr):
    """lvkDec: a finite decimal as typed, ungrouped; cut at 12 places with … otherwise."""
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


def _fixed(fr, places):
    """eaFixed: exactly `places` decimals, half away from zero, grouped."""
    fr = Fraction(fr)
    q = (abs(fr.numerator) * 10 ** places * 2 // fr.denominator + 1) // 2
    t = str(q).rjust(places + 1, "0")
    whole = "{:,}".format(int(t[:len(t) - places]))
    return (MINUS if fr < 0 and q else "") + whole + ("." + t[len(t) - places:] if places else "")


def _frac(fr):
    return "%s/%s" % (ea.grp(fr.numerator), ea.grp(fr.denominator))


def num_text(fr):
    """eaNum, for figures below 30 digits: "4", "3/2 = 1.50", "2/7 ≈ 0.29"."""
    fr = Fraction(fr)
    if fr.denominator == 1:
        return ea.grp(fr.numerator)
    exact = (fr * 100).denominator == 1
    return "%s%s%s" % (_frac(fr), " = " if exact else " ≈ ", _fixed(fr, 2))


def pct_text(fr):
    """lvkPct: the fraction and its percentage to at most two places."""
    fr = Fraction(fr)
    p = fr * 100
    t = _fixed(p, 2)
    if "." in t:
        t = t.rstrip("0").rstrip(".")
    head = ea.grp(fr.numerator) if fr.denominator == 1 else _frac(fr)
    return head + (" = " if (p * 100).denominator == 1 else " ≈ ") + t + "%"


def parse_rat(text, what):
    """lvkParseRat."""
    s = _clean(text)
    if s == "":
        raise ValueError("%s is empty" % what)
    m = _RAT.match(s)
    if m:
        if re.fullmatch(r"0+", m.group(2)):
            raise ValueError("%s %s divides by zero" % (what, quote(s)))
        if len(m.group(1).replace("-", "")) > 8 or len(m.group(2)) > 8:
            raise ValueError("%s %s has more than 8 digits above or below the line" % (what, quote(s)))
        return Fraction(int(m.group(1)), int(m.group(2)))
    m = _NUMBER.match(s)
    if not m:
        raise ValueError("%s should be a number such as 3, 0.25 or 1/2, and %s is not one" % (what, quote(s)))
    if len(m.group(1) or m.group(2) or "") > 6:
        raise ValueError("%s has more than 6 decimal places" % what)
    return Fraction(s)


def parse_names(f, text, what):
    """lvkNameSeq."""
    s = _clean(text)
    if s == "":
        raise ValueError("%s is empty" % what)
    if s == "-":
        if f.get("dash"):
            return []
        raise ValueError('%s cannot be "-", which marks none' % what)
    toks = s.split()
    if len(toks) > 40:
        raise ValueError("%s holds at most 40 names, and there are %d" % (what, len(toks)))
    for i, t in enumerate(toks):
        if t == "-":
            raise ValueError('%s puts "-" among other names; "-" alone marks none' % what)
        if not _NAME.match(t):
            raise ValueError("%s %s should be letters, digits, dots, hyphens or underscores (a name of several "
                             "words takes hyphens: round-quadrangle)" % (what, quote(t)))
        if toks.index(t) != i:
            raise ValueError("%s names %s twice" % (what, quote(t)))
    return toks


# ---------------------------------------------------------------------------
# levkit's field kinds, mirrored (kit-contract.md section 4)
# ---------------------------------------------------------------------------

NAMES = {"kind": "names"}
NAMES_DASH = {"kind": "names", "dash": True}


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


def lrec(what, sub, rest=None, rest_what="value", lo_rest=0, hi_rest=0, unique=False, rows=3, lo=1,
         hi=ea.MAX_RECORDS):
    """Records: the cells in `sub` (any scalar kind), then lo_rest to hi_rest cells each read by `rest`."""
    return {"kind": "lrec", "what": what, "control": "area", "rows": rows, "sub": [list(s) for s in sub],
            "rest": dict(rest or ea.NAME), "restWhat": rest_what, "loRest": lo_rest, "hiRest": hi_rest,
            "lo": lo, "hi": hi, "unique": unique}


def llist(what, each, lo=1, hi=ea.MAX_RECORDS, things="values", control="text"):
    """A list separated by spaces or commas; entries follow any scalar kind."""
    return {"kind": "llist", "what": what, "control": control, "rows": 2, "each": dict(each), "lo": lo, "hi": hi,
            "things": things}


def _bound(r, f, what, s):
    if "gt" in f and r <= Fraction(f["gt"]):
        raise ValueError("%s must be more than %s, and it is %s" % (what, num_text(Fraction(f["gt"])), s))
    if "min" in f and r < Fraction(f["min"]):
        raise ValueError("%s cannot be less than %s, and it is %s" % (what, num_text(Fraction(f["min"])), s))
    if "max" in f and r > Fraction(f["max"]):
        raise ValueError("%s is at most %s, and it is %s" % (what, num_text(Fraction(f["max"])), s))
    return r


def parse_scalar(f, text, what):
    s = _clean(text)
    if f["kind"] == "rat" and f.get("dash") and s == "-":
        return "-"
    if f["kind"] == "rat":
        return _bound(parse_rat(s, what), f, what, s.replace("-", MINUS))
    if f["kind"] == "names":
        return parse_names(f, s, what)
    return ea.parse_scalar(f, s, what)


def _parse_lrec(f, text):
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
                raise ValueError("%s names %s twice" % (what, quote(cells[0])))
            seen.add(cells[0])
        out.append(rec)
    return out


def _parse_llist(f, text):
    what = f["what"]
    s = _clean(text)
    toks = [t for t in re.split(r"[\s,]+", s) if t] if s else []
    ea._sized(len(toks), f, what, f["things"])
    vals = [parse_scalar(f["each"], t, "%s, entry %d" % (what, i + 1)) for i, t in enumerate(toks)]
    if f["each"]["kind"] == "name":
        for i, t in enumerate(toks):
            if toks.index(t) != i:
                raise ValueError("%s names %s twice" % (what, quote(t)))
    return vals


_OWN = ("lrec", "llist", "rat", "names")


def parse_field(where, f, text):
    """Mirror of lvkRead for one field."""
    if f["kind"] not in _OWN:
        return ea.parse(where, f, text)
    try:
        if f["kind"] == "lrec":
            return _parse_lrec(f, text)
        if f["kind"] == "llist":
            return _parse_llist(f, text)
        return parse_scalar(f, text, f["what"])
    except ValueError as exc:
        raise ValueError("%s: %s" % (where, exc)) from None


def _cell(p):
    if isinstance(p, (list, tuple)):
        return " ".join(str(x).strip() for x in p)
    if isinstance(p, bool):
        return "yes" if p else "no"
    return str(p).strip()


def to_text(where, f, value):
    """A preset's value -> the exact text its box holds (eakit's to_text for eakit's kinds).

    A record field takes a string or a list of records, each a string or a list
    of cells; a cell that is itself a list (a NAMES cell) is joined by spaces.
    """
    if f["kind"] not in _OWN:
        return ea.to_text(where, f, value)
    what = f["what"]
    if isinstance(value, str):
        text = value.strip()
    elif f["kind"] == "lrec" and isinstance(value, (list, tuple)):
        text = "; ".join(r.strip() if isinstance(r, str) else ", ".join(_cell(p) for p in r) for r in value)
    elif f["kind"] in ("llist", "names") and isinstance(value, (list, tuple)):
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
    """eakit_core.presets, reading levkit's kinds as well."""
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
_WIRE_JS = ea.EA_WIRE_JS.replace(_READ_CALL, "lvkRead(SPEC, raw)")
assert ea.EA_WIRE_JS.count(_READ_CALL) == 1, "eakit's wiring no longer reads its inputs with one eaRead(SPEC, raw) call"
_COMMENT_LINES = re.compile(r"^[ \t]*/\*(?:(?!\*/).)*\*/[ \t]*\n", re.S | re.M)


def _build_lab(cfg, *, kit, prefix, view, fields, tiles, fn, js, fixed, title, subtitle, intro, rules, extra_keys=(),
               check=None):
    """eakit_core.build_lab, with levkit's kinds and lvkRead (kit-contract.md section 2)."""
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
    return (FAMILY_SENTENCE + " It shows what follows on Hobbes’s definitions as written here; whether they "
            "describe men and commonwealths is what the book argues.")


def _no_options(cfg, kit, tiles):
    return {}, [], tiles


def mode_lab(cfg, mode, spec):
    """One levkit mode as a Lab, from its spec dict (kit-contract.md section 2)."""
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
                      fn=spec["fn"], js=LVK_CORE_JS + spec["js"] + v["js"], fixed=fixed, title=spec["title"],
                      subtitle=v["subtitle"], intro=family_intro(), rules=v["rules"], extra_keys=keys,
                      check=v["check"])


_N = ea.NAME

# ---------------------------------------------------------------------------
# reckon (lrk): names as sums of names, and affirmations by the definitions
# ---------------------------------------------------------------------------

LRK_JS = r"""
  var LRK_VIEW = {};
  function lrkCompute(view, inst, opts) { return eaRun(LRK_VIEW[view], inst, opts); }
"""

LRK_VIEW_JS = {}

LRK_VIEW_JS["names"] = r"""
  /* The refusals, in this order: a name defined twice; a name both simple and
     defined; an opposed pair that is not two distinct simple names; a circle. */
  function lrkVocabulary(inst) {
    var simple = {}, def = {}, at = {}, order = [];
    inst.simple.forEach(function (s) { simple[s] = true; });
    inst.defs.forEach(function (d, i) {
      if (Object.prototype.hasOwnProperty.call(def, d.name)) eaRefuse('Definitions define ' + d.name + ' twice (records ' + at[d.name] + ' and ' + (i + 1) + '); a name of inconstant signification cannot be reckoned with, so keep one definition');
      def[d.name] = d.parts; at[d.name] = i + 1; order.push(d.name);
    });
    order.forEach(function (n) {
      if (simple[n]) eaRefuse(n + ' is both a simple name and defined (Definitions, record ' + at[n] + '); a name is one or the other');
    });
    inst.opposed.forEach(function (o, i) {
      [o.a, o.b].forEach(function (x) { if (!simple[x]) eaRefuse('Opposed pairs, record ' + (i + 1) + ': ' + x + ' is not one of the simple names'); });
      if (o.a === o.b) eaRefuse('Opposed pairs, record ' + (i + 1) + ' pairs ' + o.a + ' with itself');
    });
    var state = {}, stack = [];
    function visit(n) {
      if (!Object.prototype.hasOwnProperty.call(def, n) || state[n] === 2) return;
      if (state[n] === 1) eaRefuse('The definitions go round in a circle: ' + stack.slice(stack.indexOf(n)).concat([n]).join(' → ') + '; a name cannot be defined through itself');
      state[n] = 1; stack.push(n);
      def[n].forEach(visit);
      stack.pop(); state[n] = 2;
    }
    order.forEach(visit);
    /* Expansions: the simple names a name adds up to; empty is the first name
       reached that stands for nothing (neither simple nor defined). */
    var memo = {};
    function expand(n) {
      if (memo[n]) return memo[n];
      var e;
      if (simple[n]) e = { names: [n], empty: null };
      else if (!Object.prototype.hasOwnProperty.call(def, n)) e = { names: [], empty: n };
      else {
        var set = {}, empty = null;
        def[n].forEach(function (p) {
          var x = expand(p);
          if (empty === null && x.empty !== null) empty = x.empty;
          x.names.forEach(function (s) { set[s] = true; });
        });
        e = { names: eaSort(Object.keys(set)), empty: empty };
      }
      memo[n] = e;
      return e;
    }
    return { simple: simple, def: def, order: order, expand: expand };
  }
  function lrkSum(names) { return names.length ? names.join(' + ') : 'nothing'; }
  LRK_VIEW.names = function (inst) {
    var v = lrkVocabulary(inst), counts = { 'true': [], 'false': [], absurd: [], insignificant: [] };
    var known = function (x) { return v.simple[x] || Object.prototype.hasOwnProperty.call(v.def, x); };
    var union = function (list) {
      var set = {};
      list.forEach(function (x) { v.expand(x).names.forEach(function (s) { set[s] = true; }); });
      return eaSort(Object.keys(set));
    };
    var rows = [], verdicts = [];
    inst.claims.forEach(function (c) {
      var se = union(c.subject), pe = union(c.predicate), verdict = null, why = '';
      c.subject.concat(c.predicate).forEach(function (x) {
        if (verdict) return;
        if (!known(x)) { verdict = 'insignificant'; why = x + ' stands for nothing'; }
        else if (v.expand(x).empty !== null) { verdict = 'insignificant'; why = x + ' is defined through ' + v.expand(x).empty + ', which stands for nothing'; }
      });
      if (!verdict) {
        var places = [[se, 'in the subject'], [pe, 'in the predicate'], [eaSort(se.concat(pe.filter(function (s) { return se.indexOf(s) < 0; }))), 'subject and predicate together']];
        places.forEach(function (pl) {
          if (verdict) return;
          inst.opposed.forEach(function (o) {
            if (verdict) return;
            if (pl[0].indexOf(o.a) >= 0 && pl[0].indexOf(o.b) >= 0) { verdict = 'absurd'; why = o.a + ' and ' + o.b + ' cannot be added (' + pl[1] + ')'; }
          });
        });
      }
      if (!verdict) {
        var missing = pe.filter(function (s) { return se.indexOf(s) < 0; });
        if (missing.length) { verdict = 'false'; why = 'the subject lacks ' + missing.join(', '); }
        else { verdict = 'true'; why = 'every part of the predicate is in the subject'; }
      }
      counts[verdict].push(c.claim);
      verdicts.push(c.claim + ' ' + verdict);
      rows.push([c.claim, c.subject.join(' '), lrkSum(se), c.predicate.join(' '), lrkSum(pe), verdict, why]);
    });
    var expansions = v.order.map(function (n) {
      var e = v.expand(n);
      return n + ' = ' + (e.empty !== null ? 'nothing (' + e.empty + ' stands for nothing)' : lrkSum(e.names));
    });
    var tally = counts['true'].length + ' true, ' + counts['false'].length + ' false, ' + counts.absurd.length + ' absurd, ' + counts.insignificant.length + ' insignificant';
    var listed = function (k) { return lvkListed(counts[k].length, counts[k]); };
    return {
      tiles: {
        lrkNames: inst.simple.length + ' simple, ' + v.order.length + ' defined',
        lrkExpand: expansions.length ? expansions.join('; ') : 'no definitions given',
        lrkVerdicts: verdicts.join('; '),
        lrkCounts: tally,
        lrkTrue: listed('true'), lrkFalse: listed('false'), lrkAbsurd: listed('absurd'), lrkEmpty: listed('insignificant')
      },
      status: lvkStatus(eaPlural(inst.claims.length, 'claim', 'claims') + ': ' + tally
        + '; a claim is true when every simple name of the predicate is in the subject'),
      table: { caption: 'Each claim, subject is predicate, reckoned by the definitions', head: ['claim', 'subject', 'adds up to', 'predicate', 'adds up to', 'verdict', 'why'], rows: rows }
    };
  };
"""


def _check_names(inst, fixed):
    simple = set(inst["simple"])
    defs, at, order = {}, {}, []
    for i, d in enumerate(inst["defs"]):
        if d["name"] in defs:
            raise ValueError("Definitions define %s twice (records %d and %d); a name of inconstant signification "
                             "cannot be reckoned with, so keep one definition" % (d["name"], at[d["name"]], i + 1))
        defs[d["name"]], at[d["name"]] = d["parts"], i + 1
        order.append(d["name"])
    for n in order:
        if n in simple:
            raise ValueError("%s is both a simple name and defined (Definitions, record %d); a name is one or the other"
                             % (n, at[n]))
    for i, o in enumerate(inst["opposed"]):
        for x in (o["a"], o["b"]):
            if x not in simple:
                raise ValueError("Opposed pairs, record %d: %s is not one of the simple names" % (i + 1, x))
        if o["a"] == o["b"]:
            raise ValueError("Opposed pairs, record %d pairs %s with itself" % (i + 1, o["a"]))
    state, stack = {}, []

    def visit(n):
        if n not in defs or state.get(n) == 2:
            return
        if state.get(n) == 1:
            path = stack[stack.index(n):] + [n]
            raise ValueError("The definitions go round in a circle: %s; a name cannot be defined through itself"
                             % " → ".join(path))
        state[n] = 1
        stack.append(n)
        for p in defs[n]:
            visit(p)
        stack.pop()
        state[n] = 2

    for n in order:
        visit(n)


RECKON = {
    "prefix": "lrk", "fn": "lrkCompute", "title": "Reckoning with names", "js": LRK_JS,
    "views": {
        "names": {
            "fields": [("simple", llist("Simple names (admitted with no definition)", _N, lo=1, hi=40, things="names",
                                        control="area"), None),
                       ("defs", lrec("Definitions (name, then its parts separated by spaces)",
                                     [("name", _N), ("parts", NAMES)], rows=4, lo=0, hi=40), ""),
                       ("opposed", lrec("Names that cannot be added (two simple names)", [("a", _N), ("b", _N)],
                                        rows=2, lo=0, hi=20), ""),
                       ("claims", lrec("Claims (claim, subject, predicate: subject is predicate)",
                                       [("claim", _N), ("subject", NAMES), ("predicate", NAMES)], unique=True, rows=4,
                                       lo=1, hi=30), None)],
            "tiles": [("Names", "lrkNames"), ("Each defined name, added up", "lrkExpand"),
                      ("Each claim", "lrkVerdicts"), ("Verdicts", "lrkCounts"), ("True", "lrkTrue"),
                      ("False", "lrkFalse"), ("Absurd", "lrkAbsurd"), ("Insignificant", "lrkEmpty")],
            "check": _check_names, "subtitle": "what a name adds up to, and whether an affirmation is true by it",
            "rules": "A defined name is the sum of its parts, and a part may itself be defined; adding up every part "
                     "down to the simple names gives the name's expansion (listed in alphabetical order). A claim "
                     "'subject is predicate' may give several names on either side, read as their sum. Its verdict, "
                     "in this order of precedence: insignificant, when a name in it, or a name it is defined "
                     "through, is neither simple nor defined, so stands for nothing; else absurd, when the subject, "
                     "the predicate, or the two together contain a pair of names that cannot be added; else true, "
                     "when every simple name of the predicate is in the subject's expansion; else false. A name "
                     "defined through itself, directly or through others, is refused, naming the circle.",
            "js": LRK_VIEW_JS["names"],
        },
    },
}

# ---------------------------------------------------------------------------
# deliberate (lde): the will as the last appetite or aversion
# ---------------------------------------------------------------------------

LDE_JS = r"""
  var LDE_VIEW = {};
  function ldeCompute(view, inst, opts) { return eaRun(LDE_VIEW[view], inst, opts); }
"""

LDE_VIEW_JS = {}

LDE_VIEW_JS["will"] = r"""
  /* A step inclines to doing when it is an appetite (or hope) toward doing, or
     an aversion (or fear) toward omitting; otherwise to omitting. */
  function ldeLean(s) {
    var pull = s.motion === 'appetite' || s.motion === 'hope';
    return (pull === (s.toward === 'do')) ? 'do' : 'omit';
  }
  function ldeMotion(s) {
    var as = { hope: ', an appetite', fear: ', an aversion' }[s.motion] || '';
    return s.motion + ' toward ' + (s.toward === 'do' ? 'doing' : 'omitting') + as;
  }
  function ldeEndCheck(inst) {
    var last = inst.steps[inst.steps.length - 1], lean = ldeLean(last);
    if (inst.end === 'done' && lean === 'omit') eaRefuse('The deliberation ends with the action done, but its last motion (' + last.step + ') inclines to omit it; on Hobbes’s definition the will is that last motion, so an action done follows a last appetite to do it');
    if (inst.end === 'omitted' && lean === 'do') eaRefuse('The deliberation ends with the action omitted, but its last motion (' + last.step + ') inclines to do it; on Hobbes’s definition the will is that last motion, so an action omitted follows a last motion toward omitting it');
  }
  LDE_VIEW.will = function (inst) {
    ldeEndCheck(inst);
    var st = inst.steps, n = st.length, leans = st.map(ldeLean), alt = 0, i;
    for (i = 1; i < n; i += 1) if (leans[i] !== leans[i - 1]) alt += 1;
    var will = leans[n - 1], last = st[n - 1];
    var outcome = inst.end === 'impossible' ? 'not done: thought impossible' : (will === 'do' ? 'done' : 'omitted');
    var opp = [];
    for (i = 0; i < n - 1; i += 1) if (leans[i] !== will) opp.push(st[i].step);
    var nDo = leans.filter(function (x) { return x === 'do'; }).length;
    var rows = st.map(function (s, j) { return [s.step, s.motion, s.toward, leans[j], leans[j] === will ? 'the same' : 'the opposite']; });
    return {
      tiles: {
        ldeSteps: eaInt(n),
        ldeAlternations: eaInt(alt),
        ldeLean: nDo + ' toward doing, ' + (n - nDo) + ' toward omitting',
        ldeWill: (will === 'do' ? 'to do' : 'to omit') + ' (' + last.step + ': ' + ldeMotion(last) + ')',
        ldeOutcome: inst.action + ' ' + outcome,
        ldeWills: st.map(function (s, j) { return s.step + ' ' + leans[j]; }).join(', '),
        ldeOpposite: n === 1 ? 'no earlier step' : opp.length + ' of ' + (n - 1) + (opp.length ? ': ' + opp.join(', ') : '')
      },
      status: lvkStatus('The will is the last appetite or aversion, ' + last.step + ', so the will is ' + (will === 'do' ? 'to do' : 'to omit')
        + ' and ' + inst.action + ' is ' + outcome + '; stopped earlier, ' + opp.length + ' of ' + (n - 1) + ' steps would have given the opposite will'),
      table: { caption: 'Each step, and the will had deliberation ended there', head: ['step', 'motion', 'toward', 'inclines to', 'will if it ended here'], rows: rows }
    };
  };
"""


def _lean(s):
    pull = s["motion"] in ("appetite", "hope")
    return "do" if pull == (s["toward"] == "do") else "omit"


def _check_will(inst, fixed):
    last = inst["steps"][-1]
    lean = _lean(last)
    if inst["end"] == "done" and lean == "omit":
        raise ValueError("The deliberation ends with the action done, but its last motion (%s) inclines to omit it; on "
                         "Hobbes’s definition the will is that last motion, so an action done follows a last appetite "
                         "to do it" % last["step"])
    if inst["end"] == "omitted" and lean == "do":
        raise ValueError("The deliberation ends with the action omitted, but its last motion (%s) inclines to do it; "
                         "on Hobbes’s definition the will is that last motion, so an action omitted follows a last "
                         "motion toward omitting it" % last["step"])


DELIBERATE = {
    "prefix": "lde", "fn": "ldeCompute", "title": "Deliberation and the will", "js": LDE_JS,
    "views": {
        "will": {
            "fields": [("action", ea.field("The action deliberated (one name)", _N), None),
                       ("steps", lrec("Steps (step, motion, toward: do or omit)",
                                      [("step", _N), ("motion", ea.word("appetite", "aversion", "hope", "fear")),
                                       ("toward", ea.word("do", "omit"))], unique=True, rows=5, lo=1, hi=30), None),
                       ("end", ea.choice("How the deliberation ends", "as-last", "done", "omitted", "impossible"),
                        "as-last")],
            "tiles": [("Steps", "ldeSteps"), ("Changes of direction", "ldeAlternations"),
                      ("Steps inclining each way", "ldeLean"), ("The will (the last motion)", "ldeWill"),
                      ("Outcome", "ldeOutcome"), ("The will had it ended at each step", "ldeWills"),
                      ("Earlier stops that give the opposite will", "ldeOpposite")],
            "check": _check_will, "subtitle": "the will as the last appetite or aversion before the act",
            "rules": "Each step is an appetite or an aversion toward doing or toward omitting the action; hope counts "
                     "as an appetite and fear as an aversion. A step inclines to doing when it is an appetite toward "
                     "doing or an aversion toward omitting, and otherwise to omitting. The will is the last step, "
                     "whatever the earlier ones were and however many lean the other way; had deliberation ended at "
                     "an earlier step, that step would have been the will. A change of direction is a step that "
                     "inclines the other way from the one before. The end as-last means the action follows the will; "
                     "done or omitted must agree with the last step, or the inputs are refused; impossible means the "
                     "action is not done because it was thought impossible.",
            "js": LDE_VIEW_JS["will"],
        },
    },
}

# ---------------------------------------------------------------------------
# worth (lwo): a person's price, set by the buyer
# ---------------------------------------------------------------------------

LWO_JS = r"""
  var LWO_VIEW = {};
  function lwoCompute(view, inst, opts) { return eaRun(LWO_VIEW[view], inst, opts); }
"""

LWO_VIEW_JS = {}

LWO_VIEW_JS["price"] = r"""
  function lwoCheck(inst) {
    var k = inst.powers.length, names = inst.persons.map(function (p) { return p.person; }), seen = {};
    inst.persons.forEach(function (p, i) {
      if (p.rest.length !== k) eaRefuse('Persons, record ' + (i + 1) + ' (' + p.person + ') gives ' + p.rest.length + ' amounts, and there are ' + k + ' powers');
    });
    inst.buyers.forEach(function (b, i) {
      if (b.rest.length !== k) eaRefuse('Buyers, record ' + (i + 1) + ' (' + b.buyer + ') gives ' + b.rest.length + ' needs, and there are ' + k + ' powers');
    });
    inst.dignity.forEach(function (d, i) {
      if (names.indexOf(d.person) < 0) eaRefuse('Dignity, record ' + (i + 1) + ': ' + d.person + ' is not one of the persons');
      if (seen[d.person]) eaRefuse('Dignity names ' + d.person + ' twice');
      seen[d.person] = true;
    });
    if (inst.dignity.length && inst.dignity.length !== names.length) {
      eaRefuse('Dignity is given for ' + inst.dignity.length + ' of the ' + names.length + ' persons; give it for every person, or for none');
    }
  }
  /* Persons by price, highest first, ties in input order: "a > b = c > d". */
  function lwoRank(persons, price) {
    var idx = persons.map(function (_p, i) { return i; });
    idx.sort(function (a, b) { return Rcmp(price[b], price[a]) || a - b; });
    var out = '';
    idx.forEach(function (i, j) {
      if (j) out += Requ(price[i], price[idx[j - 1]]) ? ' = ' : ' > ';
      out += persons[i].person;
    });
    return out;
  }
  LWO_VIEW.price = function (inst) {
    lwoCheck(inst);
    var P = inst.persons, B = inst.buyers, k = inst.powers.length;
    var price = B.map(function (b) {
      return P.map(function (p) { var s = R0, j; for (j = 0; j < k; j += 1) s = Radd(s, Rmul(b.rest[j], p.rest[j])); return s; });
    });
    var ranks = B.map(function (b, bi) { return b.buyer + ': ' + lwoRank(P, price[bi]); });
    var tops = B.map(function (b, bi) {
      var hi = price[bi].reduce(function (m, x) { return Rcmp(x, m) > 0 ? x : m; }, price[bi][0]);
      var who = P.filter(function (_p, i) { return Requ(price[bi][i], hi); }).map(function (p) { return p.person; });
      return b.buyer + ': ' + who.join(', ') + (who.length > 1 ? ' (tied)' : '');
    });
    var rel = function (bi, i, j) {
      var c = Rcmp(price[bi][i], price[bi][j]);
      return c > 0 ? P[i].person + ' above ' + P[j].person : (c < 0 ? P[j].person + ' above ' + P[i].person : P[i].person + ' equal to ' + P[j].person);
    };
    var same;
    if (B.length === 1) same = 'one buyer only: nothing to compare';
    else {
      var i, j, b, found = null;
      for (i = 0; i < P.length && !found; i += 1) for (j = i + 1; j < P.length && !found; j += 1) for (b = 1; b < B.length && !found; b += 1) {
        if (Rsign(Rsub(price[0][i], price[0][j])) !== Rsign(Rsub(price[b][i], price[b][j]))) found = [i, j, b];
      }
      same = found ? 'no: on ' + P[found[0]].person + ' and ' + P[found[1]].person + ', ' + B[0].buyer + ' ranks ' + rel(0, found[0], found[1])
        + ' and ' + B[found[2]].buyer + ' ranks ' + rel(found[2], found[0], found[1])
        : 'yes: every buyer ranks ' + lwoRank(P, price[0]);
    }
    var dig = {}, hasDig = inst.dignity.length > 0;
    inst.dignity.forEach(function (d) { dig[d.person] = d.value; });
    var none = 'no dignity given', against = none, apart = none;
    if (hasDig) {
      against = P.map(function (p, pi) {
        return p.person + ' ' + eaNum(dig[p.person]) + ': ' + B.map(function (b, bi) {
          var c = Rcmp(dig[p.person], price[bi][pi]);
          return (c > 0 ? 'above ' : (c < 0 ? 'below ' : 'equal to ')) + b.buyer;
        }).join(', ');
      }).join('; ');
      var ap = P.filter(function (p, pi) { return B.every(function (_b, bi) { return !Requ(dig[p.person], price[bi][pi]); }); }).map(function (p) { return p.person; });
      apart = lvkListed(ap.length, ap);
    }
    var rows = P.map(function (p, pi) {
      return [p.person].concat(B.map(function (_b, bi) { return eaNum(price[bi][pi]); })).concat(hasDig ? [eaNum(dig[p.person])] : []);
    });
    return {
      tiles: {
        lwoPrices: B.map(function (b, bi) { return b.buyer + ': ' + P.map(function (p, pi) { return p.person + ' ' + eaNum(price[bi][pi]); }).join(', '); }).join('; '),
        lwoRanks: ranks.join('; '),
        lwoTop: tops.join('; '),
        lwoSame: same,
        lwoDignity: against,
        lwoApart: apart
      },
      status: lvkStatus(eaPlural(P.length, 'person', 'persons') + ' priced by ' + eaPlural(B.length, 'buyer', 'buyers')
        + '; the same ranking for every buyer: ' + same.split(':')[0] + '; a price is what a buyer would give, so it depends on the buyer'),
      table: { caption: 'Each person’s price to each buyer (the sum of need × amount)' + (hasDig ? ', and the dignity set' : ''),
               head: ['person'].concat(B.map(function (b) { return b.buyer; })).concat(hasDig ? ['dignity'] : []), rows: rows }
    };
  };
"""


def _check_price(inst, fixed):
    k = len(inst["powers"])
    names = [p["person"] for p in inst["persons"]]
    for i, p in enumerate(inst["persons"]):
        if len(p["rest"]) != k:
            raise ValueError("Persons, record %d (%s) gives %d amounts, and there are %d powers"
                             % (i + 1, p["person"], len(p["rest"]), k))
    for i, b in enumerate(inst["buyers"]):
        if len(b["rest"]) != k:
            raise ValueError("Buyers, record %d (%s) gives %d needs, and there are %d powers"
                             % (i + 1, b["buyer"], len(b["rest"]), k))
    seen = set()
    for i, d in enumerate(inst["dignity"]):
        if d["person"] not in names:
            raise ValueError("Dignity, record %d: %s is not one of the persons" % (i + 1, d["person"]))
        if d["person"] in seen:
            raise ValueError("Dignity names %s twice" % d["person"])
        seen.add(d["person"])
    if inst["dignity"] and len(inst["dignity"]) != len(names):
        raise ValueError("Dignity is given for %d of the %d persons; give it for every person, or for none"
                         % (len(inst["dignity"]), len(names)))


WORTH = {
    "prefix": "lwo", "fn": "lwoCompute", "title": "Worth as price", "js": LWO_JS,
    "views": {
        "price": {
            "fields": [("powers", llist("Powers (2 to 6 names, in order)", _N, lo=2, hi=6, things="powers"), None),
                       ("persons", lrec("Persons (person, then an amount of each power)", [("person", _N)],
                                        ea.whole(0, ea.LIMIT), "amount", 2, 6, unique=True, rows=4, lo=2, hi=12),
                        None),
                       ("buyers", lrec("Buyers (buyer, then a need for each power)", [("buyer", _N)],
                                       rat(lo=0, hi=1000), "need", 2, 6, unique=True, rows=3, lo=1, hi=6), None),
                       ("dignity", lrec("Dignity set by the commonwealth (person, value; empty for none)",
                                        [("person", _N), ("value", rat(lo=0))], rows=3, lo=0, hi=12), "")],
            "tiles": [("Each person’s price to each buyer", "lwoPrices"), ("Each buyer’s ranking", "lwoRanks"),
                      ("The person each buyer would pay most for", "lwoTop"),
                      ("Does every buyer rank them the same?", "lwoSame"),
                      ("Dignity against each buyer’s price", "lwoDignity"),
                      ("Dignity apart from every buyer’s price", "lwoApart")],
            "check": _check_price, "subtitle": "what each buyer would give for each person's powers",
            "rules": "A person's price to a buyer is the sum, over the powers, of the buyer's need for that power "
                     "times the person's amount of it, exact. Each buyer ranks the persons by price, highest first; "
                     "equal prices share a place (written =) and are listed in input order. The rankings agree when, "
                     "for every pair of persons, every buyer puts them in the same order or ties them alike; "
                     "otherwise the first pair in input order on which a buyer differs from the first buyer is "
                     "named. A dignity is the public worth the commonwealth sets, compared with each buyer's price "
                     "as above, equal to or below it; it is given for every person or for none.",
            "js": LWO_VIEW_JS["price"],
        },
    },
}

# ---------------------------------------------------------------------------
# equality (leq): whether the weak, alone or together, can overcome the strong
# ---------------------------------------------------------------------------

LEQ_JS = r"""
  var LEQ_VIEW = {};
  function leqCompute(view, inst, opts) { return eaRun(LEQ_VIEW[view], inst, opts); }
"""

LEQ_VIEW_JS = {}

LEQ_VIEW_JS["coalition"] = r"""
  function leqBeats(force, strength, rule) { var c = Rcmp(force, strength); return rule === 'match' ? c >= 0 : c > 0; }
  /* The fewest others whose summed strength times the factor overcomes the
     target: take the others from the strongest down, ties in input order. */
  function leqFewest(P, t, f, rule) {
    var others = P.map(function (_p, i) { return i; }).filter(function (i) { return i !== t; });
    others.sort(function (a, b) { return Rcmp(P[b].strength, P[a].strength) || a - b; });
    var sum = R0, k;
    for (k = 0; k < others.length; k += 1) {
      sum = Radd(sum, P[others[k]].strength);
      if (leqBeats(Rmul(sum, f), P[t].strength, rule)) return { k: k + 1, who: others.slice(0, k + 1), sum: sum };
    }
    return null;
  }
  LEQ_VIEW.coalition = function (inst) {
    var P = inst.persons, f = inst.machination, rule = inst.rule, n = P.length;
    var hi = P.reduce(function (m, p) { return Rcmp(p.strength, m) > 0 ? p.strength : m; }, P[0].strength);
    var lo = P.reduce(function (m, p) { return Rcmp(p.strength, m) < 0 ? p.strength : m; }, P[0].strength);
    var strong = P.map(function (_p, i) { return i; }).filter(function (i) { return Requ(P[i].strength, hi); })[0];
    var weak = P.map(function (_p, i) { return i; }).filter(function (i) { return Requ(P[i].strength, lo) && i !== strong; })[0];
    var ties = function (v) { return P.filter(function (p) { return Requ(p.strength, v); }).map(function (p) { return p.person; }).join(', ') + ' (' + eaNum(v) + ')'; };
    var force = function (sum) { return Requ(f, R(1n)) ? eaNum(sum) : eaNum(sum) + ' × ' + (Rint(f) ? eaInt(f.n) : eaFrac(f)) + ' = ' + eaNum(Rmul(sum, f)); };
    var res = P.map(function (_p, i) { return leqFewest(P, i, f, rule); });
    var beyond = P.filter(function (_p, i) { return res[i] === null; }).map(function (p) { return p.person; });
    var byTwo = res.filter(function (r) { return r !== null && r.k <= 2; }).length;
    var win = rule === 'match' ? 'matches or exceeds' : 'exceeds', lose = rule === 'match' ? 'falls short of' : 'does not exceed';
    var wf = Rmul(P[weak].strength, f), alone = leqBeats(wf, P[strong].strength, rule);
    var aloneText = (alone ? 'yes: ' : 'no: ') + P[weak].person + ', ' + force(P[weak].strength) + ', ' + (alone ? win : lose) + ' ' + P[strong].person + ', ' + eaNum(P[strong].strength);
    var fewest = P.map(function (p, i) {
      var r = res[i];
      return p.person + ': ' + (r ? r.k + ' (' + r.who.map(function (j) { return P[j].person; }).join(' + ') + ')' : 'no coalition');
    }).join('; ');
    var rows = P.map(function (p, i) {
      var r = res[i];
      return [p.person, eaNum(p.strength), r ? eaInt(r.k) : 'none', r ? r.who.map(function (j) { return P[j].person; }).join(' + ') : 'all the others are not enough', r ? force(r.sum) : '—'];
    });
    var rs = res[strong];
    return {
      tiles: {
        leqStrongest: ties(hi), leqWeakest: ties(lo), leqFewest: fewest,
        leqBeyond: lvkListed(beyond.length, beyond),
        leqWeakAlone: aloneText,
        leqByTwo: byTwo + ' of ' + n
      },
      status: lvkStatus('The strongest, ' + P[strong].person + ', ' + (rs ? 'can be overcome by ' + eaPlural(rs.k, 'other', 'others') + ' (' + rs.who.map(function (j) { return P[j].person; }).join(' + ') + ')' : 'is beyond every coalition')
        + '; ' + byTwo + ' of ' + n + ' can be overcome by two or fewer; the weakest alone ' + (alone ? win : lose) + ' the strongest'),
      table: { caption: 'Each person, and the fewest others who overcome him (' + (rule === 'match' ? 'matching or exceeding' : 'exceeding') + ' his strength)', head: ['person', 'strength', 'fewest others', 'coalition', 'their force'], rows: rows }
    };
  };
"""

EQUALITY = {
    "prefix": "leq", "fn": "leqCompute", "title": "Equality of ability", "js": LEQ_JS,
    "views": {
        "coalition": {
            "fields": [("persons", lrec("Persons (person, strength: a whole number from 1)",
                                        [("person", _N), ("strength", ea.whole(1, ea.LIMIT))], unique=True, rows=4,
                                        lo=2, hi=10), None),
                       ("machination", ea.field("Factor for secret machination (1 for none)", rat(lo=1, hi=1000)), "1"),
                       ("rule", ea.choice("To overcome is to", "exceed", "match"), "exceed")],
            "tiles": [("The strongest", "leqStrongest"), ("The weakest", "leqWeakest"),
                      ("Fewest others who overcome each", "leqFewest"), ("Beyond every coalition", "leqBeyond"),
                      ("The weakest alone against the strongest", "leqWeakAlone"),
                      ("Overcome by two or fewer", "leqByTwo")],
            "check": None, "subtitle": "who can be overcome, and by how few",
            "rules": "A coalition's force is the sum of its members' strengths times the factor (secret machination, "
                     "or the victim asleep; 1 for none). It overcomes a person when its force exceeds his strength "
                     "(rule exceed) or at least equals it (rule match). For each person, the others are taken from "
                     "the strongest down, ties in input order, until their force overcomes him; that is the fewest "
                     "who can, and the coalition shown. A person whom all the others together cannot overcome is "
                     "beyond every coalition. The strongest is the first of the greatest strength in input order, "
                     "the weakest the first of the least strength other than him; the weakest alone has the factor "
                     "too.",
            "js": LEQ_VIEW_JS["coalition"],
        },
    },
}

# ---------------------------------------------------------------------------
# covenant (lcv): when keeping pays, with and without the sword; the Fool
# ---------------------------------------------------------------------------

LCV_JS = r"""
  var LCV_VIEW = {};
  function lcvCompute(view, inst, opts) { return eaRun(LCV_VIEW[view], inst, opts); }
"""

LCV_VIEW_JS = {}

LCV_VIEW_JS["perform"] = r"""
  LCV_VIEW.perform = function (inst) {
    var a = inst.first, b = inst.second;
    if (a === b) eaRefuse('The two parties are both named ' + a + '; name them apart');
    var keep = Rsub(inst.gain2, inst.cost2), exp = Rmul(inst.certainty, inst.sanction), brk = Rsub(inst.gain2, exp);
    var c = Rcmp(keep, brk), keeps = c > 0 || (c === 0 && inst.tie === 'keep');
    var choice = b + (keeps ? ' keeps: ' : ' breaks: ') + eaNum(keeps ? keep : brk) + ' against ' + eaNum(keeps ? brk : keep)
      + (c === 0 ? ' (equal; the tie rule ' + inst.tie + 's)' : '');
    var first = keeps ? Rsub(inst.gain1, inst.cost1) : Rneg(inst.cost1);
    var fc = Rsign(first);
    var reasonable = (fc > 0 ? 'yes: ' : (fc < 0 ? 'no: ' : 'no better: ')) + eaNum(first) + ' against 0 for not performing';
    var least;
    if (Rzero(inst.cost2)) least = '0: keeping costs ' + b + ' nothing';
    else if (Rzero(inst.certainty)) least = 'none: at certainty 0 no sanction is ever applied';
    else least = eaNum(Rdiv(inst.cost2, inst.certainty)) + ' (cost2 ÷ certainty)';
    var nature = Rzero(inst.sanction) || Rzero(inst.certainty);
    var cond = Rzero(inst.sanction) ? 'mere nature: no sanction' : (Rzero(inst.certainty) ? 'a sanction never applied (certainty 0)' : 'a common power: sanction ' + eaNum(inst.sanction) + ' at certainty ' + lvkPct(inst.certainty));
    var rows = [
      [b, 'keeps', eaNum(keep), keeps ? 'chosen' : ''],
      [b, 'breaks', eaNum(brk), keeps ? '' : 'chosen'],
      [a, 'performs first, ' + b + ' keeps', eaNum(Rsub(inst.gain1, inst.cost1)), keeps ? 'what follows' : ''],
      [a, 'performs first, ' + b + ' breaks', eaNum(Rneg(inst.cost1)), keeps ? '' : 'what follows'],
      [a, 'does not perform', '0', '']
    ];
    return {
      tiles: {
        lcvCondition: cond,
        lcvKeep: eaNum(keep), lcvBreak: eaNum(brk), lcvExpected: eaNum(exp),
        lcvChoice: choice,
        lcvFirst: eaNum(first) + (keeps ? ', since ' + b + ' keeps' : ', since ' + b + ' breaks'),
        lcvReasonable: reasonable,
        lcvLeast: least
      },
      status: lvkStatus((Rzero(inst.sanction) ? 'In the condition of mere nature (no sanction), ' : (nature ? 'With a sanction never applied, ' : 'Under a sanction of ' + eaNum(inst.sanction) + ' applied with certainty ' + lvkPct(inst.certainty) + ', '))
        + b + ' does better to ' + (keeps ? 'keep' : 'break') + ', so ' + a + ' performing first gets ' + eaNum(first)
        + '; performing first is ' + (fc > 0 ? 'reasonable' : (fc < 0 ? 'not reasonable' : 'no better than not performing'))),
      table: { caption: 'What each party gets', head: ['who', 'does', 'payoff', 'note'], rows: rows }
    };
  };
"""

LCV_VIEW_JS["fool"] = r"""
  LCV_VIEW.fool = function (inst) {
    var t = Rdiv(inst.gain, inst.loss), breaks = [], keeps = [], vals = [], rows = [];
    inst.chances.forEach(function (c) {
      var ev = Rsub(inst.gain, Rmul(c, inst.loss)), s = Rsign(ev), say = s > 0 ? 'breaking' : (s < 0 ? 'keeping' : 'neither (equal)');
      if (s > 0) breaks.push(lvkPct(c));
      if (s < 0) keeps.push(lvkPct(c));
      vals.push(lvkPct(c) + ': ' + eaNum(ev));
      rows.push([lvkPct(c), eaNum(ev), '0', say]);
    });
    var tt = lvkPct(t) + (Rcmp(t, R(1n)) > 0 ? ', above certainty: breaking pays at every chance' : '');
    return {
      tiles: {
        lcvThreshold: tt,
        lcvValues: vals.join('; '),
        lcvBreakAt: lvkListed(breaks.length, breaks, '; '),
        lcvKeepAt: lvkListed(keeps.length, keeps, '; ')
      },
      status: lvkStatus('Breaking pays the Fool when the chance of being cast out is below gain ÷ loss = ' + lvkPct(t) + '; it does at '
        + breaks.length + ' of the ' + inst.chances.length + ' chances given; Hobbes’s reply is that no one can reasonably count on the errors of others, which this calculation assumes'),
      table: { caption: 'Each chance of being found out and cast out', head: ['chance', 'expected value of breaking', 'keeping', 'the calculation favours'], rows: rows }
    };
  };
"""


def _check_perform(inst, fixed):
    if inst["first"] == inst["second"]:
        raise ValueError("The two parties are both named %s; name them apart" % inst["first"])


_AMT = rat(lo=0)
_CHANCE = rat(lo=0, hi=1)

COVENANT = {
    "prefix": "lcv", "fn": "lcvCompute", "title": "Covenants", "js": LCV_JS,
    "views": {
        "perform": {
            "fields": [("first", ea.field("The party who performs first", _N), "first"),
                       ("second", ea.field("The party trusted to perform after", _N), "second"),
                       ("cost1", ea.field("cost1: what the first gives up by performing", _AMT), None),
                       ("gain1", ea.field("gain1: what the first gets when the second performs", _AMT), None),
                       ("cost2", ea.field("cost2: what the second gives up by performing", _AMT), None),
                       ("gain2", ea.field("gain2: what the second gets from the first", _AMT), None),
                       ("sanction", ea.field("Sanction on the second's breach (0 for none)", _AMT), "0"),
                       ("certainty", ea.field("Certainty the sanction is applied (0 to 1)", _CHANCE), "1"),
                       ("tie", ea.choice("When keeping and breaking pay the same, the second", "keep", "break"),
                        "keep")],
            "tiles": [("Condition", "lcvCondition"), ("Second's payoff if it keeps", "lcvKeep"),
                      ("Second's payoff if it breaks", "lcvBreak"), ("Expected sanction", "lcvExpected"),
                      ("What the second does", "lcvChoice"), ("First's payoff from performing first", "lcvFirst"),
                      ("Is performing first reasonable?", "lcvReasonable"),
                      ("Least sanction that makes keeping at least as good", "lcvLeast")],
            "check": _check_perform, "subtitle": "whether the second does better to keep, and whether to trust first",
            "rules": "The first performs first. The second then keeps, getting gain2 − cost2, or breaks, getting "
                     "gain2 − certainty × sanction (the expected sanction). The second keeps when keeping pays more, "
                     "and when the two are equal it does as the tie rule says (keep by default). The first gets "
                     "gain1 − cost1 if the second keeps and −cost1 if it breaks; not performing gets 0, and "
                     "performing first is reasonable only when it gets more than 0. The least sanction that makes "
                     "keeping at least as good is cost2 ÷ certainty; there is none at certainty 0 (unless keeping "
                     "costs nothing). With no sanction this is the condition of mere nature.",
            "js": LCV_VIEW_JS["perform"],
        },
        "fool": {
            "fields": [("gain", ea.field("What breaking now gains", _AMT), None),
                       ("loss", ea.field("What being cast out of the confederacy costs", rat(gt=0)), None),
                       ("chances", llist("Chances of being found out and cast out (0 to 1, up to 8)", _CHANCE, lo=1,
                                         hi=8, things="chances"), None)],
            "tiles": [("Threshold chance (gain ÷ loss)", "lcvThreshold"),
                      ("Expected value of breaking at each chance", "lcvValues"),
                      ("Chances at which breaking pays", "lcvBreakAt"),
                      ("Chances at which keeping pays", "lcvKeepAt")],
            "check": None, "subtitle": "the Fool's calculation, and where it turns",
            "rules": "Breaking gains the gain now and, with the chance given, costs the loss of being cast out: its "
                     "expected value is gain − chance × loss, exact, against 0 for keeping. The threshold chance "
                     "gain ÷ loss is where the two are equal; below it the calculation favours breaking, above it "
                     "keeping, and at it neither. Chances are listed in the order given. The calculation is the "
                     "Fool's; Hobbes's reply is that no one can reasonably count on the errors of others.",
            "js": LCV_VIEW_JS["fool"],
        },
    },
}

SPECS = {"reckon": RECKON, "deliberate": DELIBERATE, "worth": WORTH, "equality": EQUALITY, "covenant": COVENANT}
MODES_A = tuple(SPECS)


def _family_b():
    """levkit_b.MODES, imported on first use; {} while levkit_b.py does not exist."""
    try:
        from . import levkit_b
    except ModuleNotFoundError as exc:
        if exc.name and exc.name.endswith("levkit_b"):
            return {}
        raise
    return levkit_b.MODES


def levkit_lab(cfg):
    """The Leviathan kit: cfg["mode"] chooses the mode, cfg["view"] the view."""
    cfg = cfg or {}
    mode = cfg.get("mode")
    if mode in SPECS:
        return mode_lab(cfg, mode, SPECS[mode])
    family_b = _family_b()
    if mode in family_b:
        return family_b[mode](cfg)
    raise ValueError("levkit_lab: unknown mode %r; the modes are %s"
                     % (mode, ", ".join(MODES_A + tuple(m for m in family_b if m not in SPECS))))


__all__ = ["levkit_lab", "mode_lab", "family_intro", "LVK_CORE_JS", "SPECS", "MODES_A", "KIT", "CAUTION",
           "FAMILY_SENTENCE", "lrec", "llist", "rat", "NAMES", "NAMES_DASH", "parse_field", "to_text", "parse_rat",
           "dec_text", "num_text", "pct_text", "plural", "quote", "MINUS"]
