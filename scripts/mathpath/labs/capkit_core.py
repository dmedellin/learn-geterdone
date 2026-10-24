"""capkit_core -- what both halves of the Capital kit share.

Specified in docs/capital/PLAN.md section D.0 (which adopts
docs/philosophy/PLAN.md section D.0). capkit.py (value, form, money, circuit,
surplus, workday, machine, wages, accumulate) and capkit_b.py (turnover,
schemes, profit, prices, tendency, interest, rent, revenue) both import from
here. THE NAMES BELOW ARE STABLE: the other half is written against them.

JavaScript (CAP_CORE_JS, shipped on every capkit page after RATIONAL_JS):

  capNumText(r)         exact figure, minus sign U+2212, digit runs of 4+
                        grouped by commas: 12000 -> "12,000", 9/5 -> "9/5"
  capMoney(r, unit)     unit "hours": "9/5 h"; "£": "£422", "−£10";
                        "s": shillings and pence as Marx prints them --
                        "3s", "3d", "1s 6d", "1½d", "¾d", "30s"; a fraction
                        of a penny other than ½ ¼ ¾ prints "1/3 d", "2 1/3 d";
                        zero is "0s"
  capHours(r)           "9/5 h" whatever the money unit (labour-time)
  capQty(r, unit)       "16 lb"; "16" when the unit is empty
  capPct(r)             "1 = 100%", "2/3 = 66.67%", "11/50 = 22%",
                        "10 = 1,000%" (the exact figure, then the percentage
                        to at most two decimals)
  capSigned(r, fmt)     "+1 h", "0 h", "−1 h" with fmt = capHours
  capEsc, capSet, capBlank, capRefuse, capTable(caption, head, rows)
  capRead(spec, raw)    parse every input of a view; THROWS a sentence for
                        the reader, which the wiring paints red

  The field kinds capRead understands (Python: FIELD KINDS below):
    num (any), pos (> 0), nn (>= 0), share (0 to 1), count (whole >= 1),
    nncount (whole >= 0), opt (empty or >= 0), optcount (empty or whole >= 1),
    yesno, name, word (one of f.words),
    rec (records "a, 1, 2; b, 3, 4" with f.sub = [[key, kind], ...] and
         f.lo..f.hi records; sub kinds also 'label' = text that may be empty),
    nums (numbers "1, 1, 1", each of kind f.each, f.lo..f.hi of them)

Python:

  q(where, value, what)            (Fraction, text) for 3, "3/4", Fraction
  units(cfg, kit, allowed, default) (money_unit, qty_unit), validated
  pick_view(cfg, kit, views)       cfg["view"] or the first; raises on unknown
  choice(cfg, kit, key, options)   a redraw-only select's shipped value
  periods(cfg, kit, default)       cfg["periods"], 1..10, refused above 10
  field_text(where, key, kind, v)  a preset value -> the text the box holds
  presets(cfg, kit, fields, redraw_keys=(), check=None)
                                   (table, menu, expect, chosen)
  mode_lab(cfg, ...)               the whole Lab for one mode and view: preset
                                   menu, text inputs, redraw-only selects, the
                                   periods range, tiles, table, banner, the
                                   optional bar; see its docstring

A mode supplies one pure JS function  fn(view, inst, U, opts)  returning
{tiles: {id: text}, status: text, table: {caption, head, rows} | null,
svg: string | undefined} or {refuse: sentence}. U is {money, qty}; opts maps
each redraw-only key (and 'periods') to its current value. Being pure, it is
what scripts/mathcheck.js calls.
"""

import html
import json
import re
from fractions import Fraction

from .algebra_core import RATIONAL_JS
from .common import Lab, cfg_literal

MONEY_UNITS = ("hours", "s", "£")

# ---------------------------------------------------------------------------
# JavaScript shared by every capkit page
# ---------------------------------------------------------------------------

CAP_CORE_JS = r"""
  /* capkit's shared printing and parsing. Every parse THROWS an Error whose
     message is a sentence for the reader; the wiring catches it, paints the
     banner red and blanks the tiles. Nothing after the parse is inside that
     catch. */
  var CAP_DASH = '—', CAP_MINUS = '−';
  function capEsc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }
  function capClean(text) {
    return String(text === null || text === undefined ? '' : text).replace(/−/g, '-').trim();
  }
  /* Digit runs of four or more get thousands commas, as Marx's tables do. */
  function capGroup(s) {
    return String(s).replace(/\d{4,}/g, function (run) { return run.replace(/\B(?=(\d{3})+$)/g, ','); });
  }
  function capNumText(r) {
    return (Rsign(r) < 0 ? CAP_MINUS : '') + capGroup(Rtext(Rabs(r)));
  }
  function capHours(r) { return capNumText(r) + ' h'; }
  function capQty(r, unit) { return capNumText(r) + (unit ? ' ' + unit : ''); }
  /* Pence: whole pence and a named half or quarter, "1½d", "¾d"; any other
     fraction of a penny as "n/m d", after the whole pence: "1/3 d", "2 1/3 d"
     (the same strings capkit_b's kbShillings prints). */
  function capPence(p) {
    var whole = p.n / p.d, frac = Rsub(p, R(whole)), name;
    if (Rzero(frac)) return capGroup(String(whole)) + 'd';
    if (Requ(frac, R(1n, 2n))) name = '½';
    else if (Requ(frac, R(1n, 4n))) name = '¼';
    else if (Requ(frac, R(3n, 4n))) name = '¾';
    else return (whole > 0n ? capGroup(String(whole)) + ' ' : '') + Rtext(frac) + ' d';
    return (whole > 0n ? capGroup(String(whole)) : '') + name + 'd';
  }
  /* Shillings and pence, 12d to the shilling. Never converted to pounds: a
     tile never converts between units silently. */
  function capShillings(r) {
    var neg = Rsign(r) < 0, a = Rabs(r), whole = a.n / a.d;
    var pence = Rmul(Rsub(a, R(whole)), R(12n)), parts = [];
    if (whole > 0n) parts.push(capGroup(String(whole)) + 's');
    if (!Rzero(pence)) parts.push(capPence(pence));
    if (!parts.length) return '0s';
    return (neg ? CAP_MINUS : '') + parts.join(' ');
  }
  function capMoney(r, unit) {
    if (unit === 's') return capShillings(r);
    if (unit === '£') return (Rsign(r) < 0 ? CAP_MINUS : '') + '£' + capGroup(Rtext(Rabs(r)));
    return capHours(r);
  }
  /* A rate: the exact fraction and its percentage, to at most two decimals,
     whole part grouped: "2/3 = 66.67%", "10 = 1,000%". */
  function capPct(r) {
    var pct = Rdec(Rmul(r, R(100n)), 2), dot = pct.indexOf('.');
    pct = dot < 0 ? capGroup(pct) : capGroup(pct.slice(0, dot)) + pct.slice(dot);
    return capNumText(r) + ' = ' + pct.replace('-', CAP_MINUS) + '%';
  }
  function capSigned(r, fmt) {
    if (Rsign(r) > 0) return '+' + fmt(r);
    return fmt(r);
  }
  function capSum(v) { var s = R0; v.forEach(function (x) { s = Radd(s, x); }); return s; }
  function capMin(a, b) { return Rcmp(a, b) <= 0 ? a : b; }
  function capMax(a, b) { return Rcmp(a, b) >= 0 ? a : b; }
  function capCount(n, one, many) { return capNumText(n) + ' ' + (Requ(n, R1) ? one : many); }

  function capNum(text, what) {
    var s = capClean(text), r = s === '' ? null : Rparse(s);
    if (r === null) {
      throw new Error(what + ' should be a number such as 3, 1/2 or 0.25, and "' + s + '" is not one');
    }
    return r;
  }
  var CAP_BAD_NAME = /[,;<>&"=]/;
  function capScalar(kind, text, what, words) {
    var s = capClean(text), r;
    if (kind === 'label') {
      if (CAP_BAD_NAME.test(s)) throw new Error(what + ' "' + s + '" may not contain , ; = < > & or quotes');
      return s;
    }
    if (kind === 'name') {
      if (s === '') throw new Error(what + ' is missing');
      if (CAP_BAD_NAME.test(s)) throw new Error(what + ' "' + s + '" may not contain , ; = < > & or quotes');
      return s;
    }
    if (kind === 'yesno') {
      if (/^(yes|y|true)$/i.test(s)) return true;
      if (/^(no|n|false)$/i.test(s)) return false;
      throw new Error(what + ' should be yes or no, not "' + s + '"');
    }
    if (kind === 'word') {
      if (words.indexOf(s) < 0) throw new Error(what + ' should be one of ' + words.join(', ') + ', not "' + s + '"');
      return s;
    }
    if ((kind === 'opt' || kind === 'optcount') && s === '') return null;
    r = capNum(s, what);
    if (kind === 'pos' && Rsign(r) <= 0) throw new Error(what + ' must be more than 0, and it is ' + capNumText(r));
    if ((kind === 'nn' || kind === 'opt') && Rsign(r) < 0) {
      throw new Error(what + ' cannot be negative, and it is ' + capNumText(r));
    }
    if (kind === 'share' && (Rsign(r) < 0 || Rcmp(r, R1) > 0)) {
      throw new Error(what + ' is a share from 0 to 1, and it is ' + capNumText(r));
    }
    if (kind === 'count' || kind === 'optcount') {
      if (!Rint(r) || Rsign(r) <= 0) throw new Error(what + ' must be a whole number of at least 1, not ' + capNumText(r));
    }
    if (kind === 'nncount' && (!Rint(r) || Rsign(r) < 0)) {
      throw new Error(what + ' must be a whole number, 0 or more, not ' + capNumText(r));
    }
    return r;
  }
  function capLimit(n, f) {
    if (n < f.lo) {
      throw new Error(f.what + (n === 0 ? ' is empty' : ': this lab needs at least ' + f.lo + ', and there '
        + (n === 1 ? 'is 1' : 'are ' + n)));
    }
    if (n > f.hi) throw new Error(f.what + ': this lab takes at most ' + f.hi + ', and there are ' + n);
  }
  function capRecords(text, f) {
    var s = capClean(text), rows = s === '' ? [] : s.split(';').map(function (r) { return r.trim(); });
    if (rows.length && rows[rows.length - 1] === '') rows.pop();
    capLimit(rows.length, f);
    var seen = {};
    return rows.map(function (row, i) {
      var cells = row.split(',').map(function (c) { return c.trim(); });
      if (cells.length !== f.sub.length) {
        throw new Error('Entry ' + (i + 1) + ' of ' + f.what + ' has ' + cells.length + ' part'
          + (cells.length === 1 ? '' : 's') + '; each needs ' + f.sub.length + ': '
          + f.sub.map(function (k) { return k[0]; }).join(', '));
      }
      var rec = {};
      f.sub.forEach(function (k, j) {
        rec[k[0]] = capScalar(k[1], cells[j], 'The ' + k[0].replace(/_/g, ' ') + ' in entry ' + (i + 1) + ' of ' + f.what, k[2]);
      });
      if (f.unique) {
        var key = rec[f.sub[0][0]];
        if (seen[key]) throw new Error(f.what + ' name "' + key + '" twice');
        seen[key] = true;
      }
      return rec;
    });
  }
  function capNumbers(text, f) {
    var s = capClean(text), parts = s === '' ? [] : s.split(/[\s,]+/).filter(function (t) { return t.length; });
    capLimit(parts.length, f);
    return parts.map(function (t, i) { return capScalar(f.each, t, 'Entry ' + (i + 1) + ' of ' + f.what); });
  }
  function capField(f, text) {
    if (f.kind === 'rec') return capRecords(text, f);
    if (f.kind === 'nums') return capNumbers(text, f);
    return capScalar(f.kind, text, f.what, f.words);
  }
  function capRead(spec, raw) {
    var out = {};
    spec.forEach(function (f) { out[f.key] = capField(f, raw[f.key]); });
    return out;
  }

  function capSet(id, text) { document.getElementById(id).textContent = text; }
  function capBlank(ids) { ids.forEach(function (id) { capSet(id, CAP_DASH); }); }
  function capRefuse(statusEl, ids, why) {
    capBlank(ids);
    statusEl.innerHTML = '<span class="tone-red">' + capEsc(String(why).replace(/\.$/, '')) + '.</span>';
  }
  /* head: header texts; rows: rows of cells, each text or {t: text, c: class}. */
  function capTable(caption, head, rows) {
    var h = '<caption>' + capEsc(caption) + '</caption><thead><tr>'
      + head.map(function (x) { return '<th>' + capEsc(x) + '</th>'; }).join('') + '</tr></thead><tbody>';
    rows.forEach(function (row) {
      h += '<tr>' + row.map(function (cell) {
        var t = (cell && cell.t !== undefined) ? cell.t : cell, c = (cell && cell.c) ? cell.c : '';
        return '<td' + (c ? ' class="' + c + '"' : '') + '>' + capEsc(t) + '</td>';
      }).join('') + '</tr>';
    });
    return h + '</tbody>';
  }
"""

# The wiring every capkit page shares. %(fn)s is the mode's pure function.
CAP_WIRE_JS = r"""
  var presetS = document.getElementById('%(p)sPreset');
  var statusEl = document.getElementById('%(p)sStatus');
  var tableEl = document.getElementById('%(p)sTable');
  var barEl = document.getElementById('%(p)sBar');
  function field(id) { return document.getElementById(id); }
  function capOpts() {
    var o = {};
    Object.keys(REDRAW).forEach(function (k) { o[k] = field(REDRAW[k]).value; });
    if (PERIODS) {
      o.periods = +field(PERIODS).value;
      var out = field(PERIODS + 'Out');
      if (out) out.textContent = field(PERIODS).value;
    }
    return o;
  }
  function capClear() { tableEl.innerHTML = ''; if (barEl) barEl.innerHTML = ''; }
  function redraw() {
    var raw = {}, inst;
    SPEC.forEach(function (f) { raw[f.key] = field(f.id).value; });
    try { inst = capRead(SPEC, raw); } catch (err) { capClear(); capRefuse(statusEl, TILES, err.message); return; }
    var opts = capOpts();
    if (PERIODS && !(opts.periods >= 1 && opts.periods <= 10)) {
      capClear(); capRefuse(statusEl, TILES, 'This lab runs 1 to 10 periods'); return;
    }
    var out = %(fn)s(VIEW, inst, U, opts);
    if (out.refuse) { capClear(); capRefuse(statusEl, TILES, out.refuse); return; }
    TILES.forEach(function (id) { capSet(id, out.tiles[id] === undefined ? CAP_DASH : out.tiles[id]); });
    tableEl.innerHTML = out.table ? capTable(out.table.caption, out.table.head, out.table.rows) : '';
    if (barEl) barEl.innerHTML = out.svg || '';
    statusEl.innerHTML = capEsc(out.status);
  }
  presetS.addEventListener('change', function () {
    var inst = PRESETS[presetS.value];
    if (!inst) return;
    SPEC.forEach(function (f) { if (inst[f.key] !== undefined) field(f.id).value = inst[f.key]; });
    redraw();
  });
  SPEC.forEach(function (f) { field(f.id).addEventListener('input', redraw); });
  Object.keys(REDRAW).forEach(function (k) { field(REDRAW[k]).addEventListener('change', redraw); });
  if (PERIODS) { field(PERIODS).addEventListener('input', redraw); field(PERIODS).addEventListener('change', redraw); }
  redraw();
  window.redrawLab = redraw;
"""

# ---------------------------------------------------------------------------
# Python: validating lesson data and turning it into what the boxes hold
# ---------------------------------------------------------------------------

_NUM_RE = re.compile(r"[+-]?\d+/\d+|[+-]?\d+|[+-]?\d*\.\d+")
_BAD_NAME = re.compile(r'[,;<>&"=]')

SCALAR_KINDS = ("num", "pos", "nn", "share", "count", "nncount", "opt", "optcount", "yesno", "name", "label")


def q(where, value, what="a number"):
    """(Fraction, the text the page parses) for an int, a Fraction or "3/4"."""
    if isinstance(value, bool):
        raise ValueError("%s: %s should be a number, not %r" % (where, what, value))
    if isinstance(value, int):
        return Fraction(value), str(value)
    if isinstance(value, Fraction):
        text = str(value.numerator) if value.denominator == 1 else "%d/%d" % (value.numerator, value.denominator)
        return value, text
    if isinstance(value, str):
        s = value.strip().replace("−", "-").replace(" ", "")
        if _NUM_RE.fullmatch(s):
            try:
                return Fraction(s), s
            except ZeroDivisionError:
                pass
    raise ValueError("%s: %s should be a number such as 3 or \"3/4\", not %r" % (where, what, value))


def _scalar(where, kind, value, what, words=None):
    if kind in ("label", "name"):
        s = "" if value is None else str(value).strip() if isinstance(value, (str, int)) and not isinstance(value, bool) else None
        if s is None or _BAD_NAME.search(s) or (kind == "name" and not s):
            raise ValueError("%s: %s %r is not usable (no , ; = < > & or quotes%s)"
                             % (where, what, value, "" if kind == "label" else ", not empty"))
        return s
    if kind == "yesno":
        if not isinstance(value, bool):
            raise ValueError("%s: %s should be true or false, not %r" % (where, what, value))
        return "yes" if value else "no"
    if kind == "word":
        if value not in words:
            raise ValueError("%s: %s should be one of %s, not %r" % (where, what, ", ".join(words), value))
        return value
    if kind in ("opt", "optcount") and (value is None or value == ""):
        return ""
    f, text = q(where, value, what)
    bad = ((kind == "pos" and f <= 0) or (kind in ("nn", "opt") and f < 0)
           or (kind == "share" and not 0 <= f <= 1)
           or (kind in ("count", "optcount") and (f.denominator != 1 or f < 1))
           or (kind == "nncount" and (f.denominator != 1 or f < 0)))
    if bad:
        raise ValueError("%s: %s is %s, which a %s field refuses" % (where, what, text, kind))
    if kind not in ("num", "pos", "nn", "share", "count", "nncount", "opt", "optcount"):
        raise ValueError("%s: unknown field kind %r" % (where, kind))
    return text


def field_text(where, key, kind, value):
    """A preset's value for one field -> the exact text the input box holds.

    kind is a scalar kind string, ("word", [words]), ("rec", [(sub, kind)...],
    lo, hi, unique) or ("nums", each_kind, lo, hi).
    """
    what = key.replace("_", " ")
    if isinstance(kind, tuple) and kind[0] == "word":
        return _scalar(where, "word", value, what, kind[1])
    if isinstance(kind, tuple) and kind[0] == "rec":
        _, sub, lo, hi, unique = kind
        if not isinstance(value, (list, tuple)):
            raise ValueError("%s: %s should be a list of records" % (where, what))
        if not lo <= len(value) <= hi:
            raise ValueError("%s: %s has %d entries; this lab takes %d to %d" % (where, what, len(value), lo, hi))
        rows, seen = [], set()
        for i, rec in enumerate(value):
            if not isinstance(rec, dict) or set(rec) - {k for k, _ in sub}:
                raise ValueError("%s: entry %d of %s should be {%s}, not %r"
                                 % (where, i + 1, what, ", ".join(k for k, _ in sub), rec))
            cells = []
            for k, kk in sub:
                if k not in rec and kk != "label":
                    raise ValueError("%s: entry %d of %s has no %s" % (where, i + 1, what, k))
                cells.append(_scalar(where, kk[0] if isinstance(kk, tuple) else kk, rec.get(k, ""),
                                     "%s of entry %d of %s" % (k, i + 1, what),
                                     kk[1] if isinstance(kk, tuple) else None))
            if unique:
                if cells[0] in seen:
                    raise ValueError("%s: %s names %r twice" % (where, what, cells[0]))
                seen.add(cells[0])
            rows.append(", ".join(cells))
        return "; ".join(rows)
    if isinstance(kind, tuple) and kind[0] == "nums":
        _, each, lo, hi = kind
        if not isinstance(value, (list, tuple)) or not lo <= len(value) <= hi:
            raise ValueError("%s: %s should be a list of %d to %d numbers" % (where, what, lo, hi))
        return ", ".join(_scalar(where, each, v, "entry %d of %s" % (i + 1, what)) for i, v in enumerate(value))
    if kind not in SCALAR_KINDS:
        raise ValueError("%s: unknown field kind %r" % (where, kind))
    return _scalar(where, kind, value, what)


def _js_kind(key, label, kind):
    spec = {"key": key, "what": label}
    if isinstance(kind, tuple) and kind[0] == "word":
        spec.update(kind="word", words=list(kind[1]))
    elif isinstance(kind, tuple) and kind[0] == "rec":
        _, sub, lo, hi, unique = kind
        spec.update(kind="rec", lo=lo, hi=hi, unique=bool(unique),
                    sub=[[k, kk[0], list(kk[1])] if isinstance(kk, tuple) else [k, kk] for k, kk in sub])
    elif isinstance(kind, tuple) and kind[0] == "nums":
        spec.update(kind="nums", each=kind[1], lo=kind[2], hi=kind[3])
    else:
        spec["kind"] = kind
    return spec


def presets(cfg, kit, fields, redraw_keys=(), check=None):
    """(instance table, menu pairs, expect by preset id, the chosen id).

    fields: [(key, label, kind, default)] -- the instance inputs this view
    shows. A preset lacking a field takes its default; a default of None
    means the field is required. A preset key that is neither a field of this
    view nor id/label/note/expect raises (a typo would otherwise be ignored),
    and so does one naming a redraw-only key. check(where, preset) may raise
    for cross-field rules.
    """
    plist = cfg.get("presets")
    if not isinstance(plist, list) or not plist:
        raise ValueError("%s: cfg['presets'] must be a non-empty list of instances" % kit)
    known = {f[0] for f in fields} | {"id", "label", "note", "expect"}
    table, menu, expect = {}, [], {}
    for p in plist:
        pid = p.get("id") if isinstance(p, dict) else None
        if not isinstance(pid, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", pid):
            raise ValueError("%s: every preset needs an id of lowercase letters, digits and hyphens, not %r"
                             % (kit, pid))
        where = "%s preset %r" % (kit, pid)
        if pid in table:
            raise ValueError("%s: the id is used twice" % where)
        label = p.get("label")
        if not isinstance(label, str) or not label.strip() or "<" in label:
            raise ValueError("%s: needs a plain-text label" % where)
        bad = [k for k in redraw_keys if k in p]
        if bad:
            raise ValueError("%s: sets %s, a redraw-only control; PLAN.md D.0 ships it from the lesson "
                             "cfg and a preset never touches it" % (where, ", ".join(bad)))
        extra = sorted(set(p) - known - (set(check.extra) if check is not None and hasattr(check, "extra") else set()))
        if extra:
            raise ValueError("%s: %s %s not an input of this view (it shows %s)"
                             % (where, ", ".join(extra), "is" if len(extra) == 1 else "are",
                                ", ".join(f[0] for f in fields)))
        inst = {}
        for key, _label, kind, default in fields:
            value = p.get(key, default)
            if value is None and kind not in ("opt", "optcount"):
                raise ValueError("%s: needs %s" % (where, key))
            inst[key] = field_text(where, key, kind, value)
        if check is not None:
            check(where, p)
        table[pid] = inst
        menu.append((pid, label))
        expect[pid] = dict(p.get("expect") or {})
    chosen = cfg.get("preset", plist[0]["id"])
    if chosen not in table:
        raise ValueError("%s: cfg['preset'] %r is not one of the presets (%s)" % (kit, chosen, ", ".join(table)))
    return table, menu, expect, chosen


def units(cfg, kit, allowed=MONEY_UNITS, default="hours", qty_default=""):
    money = cfg.get("money_unit", default)
    if money not in allowed:
        raise ValueError("%s: cfg['money_unit'] is %r; this mode takes %s" % (kit, money, ", ".join(allowed)))
    qty = cfg.get("qty_unit", qty_default)
    if not isinstance(qty, str) or _BAD_NAME.search(qty) or len(qty) > 20:
        raise ValueError("%s: cfg['qty_unit'] %r should be a short unit such as lb or yards" % (kit, qty))
    return money, qty.strip()


def pick_view(cfg, kit, views):
    view = cfg.get("view", views[0])
    if view not in views:
        raise ValueError("%s: unknown view %r; the views are %s" % (kit, view, ", ".join(views)))
    return view


def choice(cfg, kit, key, options):
    value = cfg.get(key, options[0][0])
    if value not in [v for v, _ in options]:
        raise ValueError("%s: cfg[%r] is %r; it must be one of %s"
                         % (kit, key, value, ", ".join(v for v, _ in options)))
    return value


def periods(cfg, kit, default=5):
    n = cfg.get("periods", default)
    if isinstance(n, bool) or not isinstance(n, int) or not 1 <= n <= 10:
        raise ValueError("%s: cfg['periods'] is %r; this kit runs 1 to 10 periods, and more than 10 is refused"
                         % (kit, n))
    return n


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


def markup_html(prefix, name, subtitle, bar=False):
    return ('      <div class="lab-toolbar">\n'
            '        <div class="lab-title"><strong>%s</strong><span>%s</span></div>\n'
            "      </div>\n" % (html.escape(name, quote=False), html.escape(subtitle, quote=False))
            + ('      <div id="%sBar" style="margin-top:12px;"></div>\n' % prefix if bar else "")
            + '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="%sTable"></table></div>\n'
            % prefix
            + '      <div class="status-banner" id="%sStatus" style="margin-top:12px;"></div>\n' % prefix)


def _camel(prefix, key):
    """An input's id: prefix + 'In' + CamelKey ('su', 's' -> 'suInS'), never a tile's id."""
    return prefix + "In" + "".join(part[:1].upper() + part[1:] for part in key.split("_"))


def mode_lab(cfg, *, kit, prefix, view, fields, tiles, mode_js, fn, money, qty,
             title, subtitle, panel_title, panel_intro, redraw=(), n_periods=None,
             bar=False, check=None, extra_js=""):
    """One mode, one view, as a Lab.

    fields: [(key, label, kind, default)] in display order; each becomes a text
            input with id prefix + 'In' + CamelKey (prefix 'ci', key
            'every_days' -> 'ciInEveryDays'), filled from the chosen preset.
    tiles:  [(label, id)].
    redraw: [(cfg key, element id, label, [(value, text)])] -- redraw-only
            selects, shipped from cfg[key], defaulting to the first option.
    n_periods: None, or the shipped number of periods (a 1..10 range, id
            prefix + 'Periods').
    fn:     the name of the mode's pure JS function.
    Returns Lab(expect={prefix + 'Preset': {preset id: {tile: text}}}).
    """
    table, menu, expect, chosen = presets(cfg, kit, fields, tuple(k for k, *_ in redraw) + ("periods",), check)
    here = table[chosen]
    spec = []
    controls = select_html(prefix + "Preset", "Worked example", menu, chosen)
    for key, label, kind, _default in fields:
        cid = _camel(prefix, key)
        js = _js_kind(key, label, kind)
        js["id"] = cid
        spec.append(js)
        controls += text_html(cid, label, here[key])
    redraw_ids = {}
    for key, cid, label, options in redraw:
        controls += select_html(cid, label, options, choice(cfg, kit, key, options))
        redraw_ids[key] = cid
    periods_id = ""
    if n_periods is not None:
        periods_id = prefix + "Periods"
        controls += range_html(periods_id, "Periods", 1, 10, n_periods)
    controls += kpis_html(tiles)
    ids = [s["id"] for s in spec] + list(redraw_ids.values()) + [cid for _l, cid in tiles]
    if len(set(ids)) != len(ids):
        raise ValueError("%s: two controls or tiles share an id: %s" % (kit, sorted(i for i in ids if ids.count(i) > 1)))
    script = (RATIONAL_JS + CAP_CORE_JS + extra_js + mode_js
              + cfg_literal("PRESETS", table) + cfg_literal("SPEC", spec)
              + cfg_literal("TILES", [cid for _label, cid in tiles])
              + cfg_literal("REDRAW", redraw_ids) + cfg_literal("PERIODS", periods_id)
              + cfg_literal("VIEW", view) + cfg_literal("U", {"money": money, "qty": qty})
              + CAP_WIRE_JS % {"p": prefix, "fn": fn})
    return Lab(title=cfg.get("title", title), subtitle=subtitle,
               markup=markup_html(prefix, title, subtitle, bar=bar), controls=controls, script=script,
               panel_title=cfg.get("panel_title", panel_title),
               panel_intro=cfg.get("panel_intro", panel_intro),
               expect={prefix + "Preset": expect})


__all__ = ["CAP_CORE_JS", "CAP_WIRE_JS", "MONEY_UNITS", "q", "field_text", "presets", "units", "pick_view",
           "choice", "periods", "attr", "select_html", "text_html", "range_html", "kpis_html", "markup_html",
           "mode_lab"]
