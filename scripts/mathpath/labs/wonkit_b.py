"""wonkit_b -- family B of wonkit, the lab kit of The Wealth of Nations, Read Along: Books II to V.

Specified in docs/wealth-of-nations/PLAN.md section D.2; the seam with family A
(wonkit.py: the entry point `wonkit_lab` and the Book I modes) is wonkit_core.py;
the report an author configures a lesson from is
docs/wealth-of-nations/kit-report-b.md. Seven modes:

  stock   (wst)  division, revenue, accumulate, turnover, spend   Book II, III.4
  bank    (wbk)  paper, redraw                                    II.2
  trade   (wtr)  make, balance, bounty, drawback                  Book IV
  tax     (wtx)  incidence, arithmetic, land                      III.3, V.2
  debt    (wdb)  sinking, debase                                  V.3
  public  (wpb)  soldiers, fees, tolls                            V.1
  system  (wsy)  classes                                          IV.9

Each mode has one base block <PREFIX>_JS defining the pure function
<prefix>Compute(view, inst, opts), and one block per view; a page ships
WNB_SHARED_JS (family B's printers, with %p% replaced by the mode's prefix),
its mode's base block and its own view's block only. scripts/mathcheck.js
(section "wonkit (Wealth of Nations), family B") calls every view.

THE FIGURES ARE THE LESSON'S. No quantity is a constant here: every one
arrives in a preset and stands in a box the reader can see. Nothing typed is
evaluated as script. No view grades a policy or claims a historical fact;
every status line ends with wonkit's caution (wnkStatus).

EXACTNESS. Every figure is an exact BigInt rational or a count. Compounding is
exact, by repeated multiplication over whole years or whole draws; a long
rational is printed to 2 places by an exact rounding (half away from zero on
the exact value) and marked with an approximately sign. No float is printed.

MONEY. Amounts are typed as decimals (at most 6 places) or fractions p/q, in
the one money unit the lesson's cfg names (`money_unit`, default the pound
sign), and printed in it: a symbol (pound, dollar, euro sign) in front, any
other unit after with a space ("5 s", "12 oz silver").

IDS. Every JS function and variable and every element id begins with its
mode's prefix (wst, wbk, wtr, wtx, wdb, wpb, wsy); nothing here begins
wnk/WNK_ or akt/AKT_.
"""

import re
from fractions import Fraction

from .wonkit_core import alist, arec, ea, mode_lab, rat  # noqa: F401  (alist kept for authors' extensions)

_N = ea.NAME
_MINUS = "−"
_BIG = 10 ** 10          # amounts and populations: Smith's national figures run to hundreds of millions
_RECS = 12               # PLAN D.0: at most 12 records per list

# ---------------------------------------------------------------------------
# Family B's printers. One template, shipped once per page under the mode's
# prefix (%p% -> wst, wbk, ...). Python mirrors are below (_money, _plain).
# ---------------------------------------------------------------------------

WNB_SHARED_JS = r"""
  /* wonkit family B's printers (wonkit_b.py), under this mode's prefix. */
  function %p%Unit(text, neg, o) {
    var u = o.unit;
    return (neg ? EA_MINUS : '') + (u === '£' || u === '$' || u === '€' ? u + text : text + ' ' + u);
  }
  function %p%Plain(r) {
    if (eaBig(r)) return eaSci(r);
    for (var p = 0; p <= 6; p += 1) if (eaExactAt(r, p)) return eaFixed(r, p);
    return eaFrac(r) + ' ≈ ' + eaFixed(r, 2);
  }
  function %p%Two(r) {
    for (var p = 0; p <= 2; p += 1) if (eaExactAt(r, p)) return eaFixed(r, p);
    return '≈ ' + eaFixed(r, 2);
  }
  function %p%Money(r, o) {
    var a = Rabs(r), neg = r.n < 0n, p;
    if (eaBig(a)) return '≈ ' + %p%Unit(eaSci(a).slice(2), neg, o);
    for (p = 0; p <= 6; p += 1) if (eaExactAt(a, p)) return %p%Unit(eaFixed(a, p), neg, o);
    return %p%Unit(eaFrac(a), neg, o) + ' ≈ ' + %p%Unit(eaFixed(a, 2), neg, o);
  }
  function %p%Money2(r, o) {
    var a = Rabs(r), p, t;
    for (p = 0; p <= 2; p += 1) if (eaExactAt(a, p)) return %p%Unit(eaFixed(a, p), r.n < 0n, o);
    t = eaFixed(a, 2);
    return '≈ ' + %p%Unit(t, r.n < 0n && t !== '0.00', o);
  }
  function %p%Plus(r, t) { return r.n > 0n ? (t.indexOf('≈ ') === 0 ? '≈ +' + t.slice(2) : '+' + t) : t; }
  function %p%Signed(r, o) { return %p%Plus(r, %p%Money(r, o)); }
  function %p%Pc(r) {
    var p = Rmul(r, R(100n)), k;
    for (k = 0; k <= 2; k += 1) if (eaExactAt(p, k)) return eaFixed(p, k) + '%';
    return '≈ ' + eaFixed(p, 2) + '%';
  }
  function %p%Pts(r) {
    var p = Rmul(r, R(100n)), k, t;
    for (k = 0; k <= 2; k += 1) if (eaExactAt(p, k)) { t = eaFixed(p, k); return %p%Plus(p, t) + (t === '1' || t === EA_MINUS + '1' ? ' point' : ' points'); }
    t = eaFixed(p, 2);
    return '≈ ' + (t === '0.00' ? t : %p%Plus(p, t)) + ' points';
  }
  function %p%Of(pct) { return Rdiv(pct, R(100n)); }
  function %p%One(word) { return word.replace(/s$/, ''); }
  function %p%Qty(r, word) { return %p%Plain(r) + ' ' + (Requ(Rabs(r), R1) ? %p%One(word) : word); }
"""


def _shared(prefix):
    return WNB_SHARED_JS.replace("%p%", prefix)


def _fixed(fr, places):
    """eaFixed: exactly `places` decimals, half away from zero, grouped, U+2212."""
    fr = Fraction(fr)
    num, den = abs(fr.numerator), fr.denominator
    q = (num * 10 ** places * 2 // den + 1) // 2
    s = str(q).rjust(places + 1, "0")
    whole, frac = s[:len(s) - places], s[len(s) - places:]
    return (_MINUS if fr < 0 and q else "") + "{:,}".format(int(whole)) + ("." + frac if places else "")


def _exact_at(fr, places):
    return (Fraction(fr) * 10 ** places).denominator == 1


def _plain(fr):
    """<p>Plain (for figures under 30 digits, which is every figure a refusal quotes)."""
    fr = Fraction(fr)
    for p in range(7):
        if _exact_at(fr, p):
            return _fixed(fr, p)
    return "%s/%s ≈ %s" % (ea.grp(fr.numerator), ea.grp(fr.denominator), _fixed(fr, 2))


def _unit(text, neg, unit):
    return (_MINUS if neg else "") + (unit + text if unit in ("£", "$", "€") else text + " " + unit)


def _money(fr, fixed):
    """<p>Money."""
    fr = Fraction(fr)
    a, neg, unit = abs(fr), fr < 0, fixed["unit"]
    for p in range(7):
        if _exact_at(a, p):
            return _unit(_fixed(a, p), neg, unit)
    return "%s ≈ %s" % (_unit("%s/%s" % (ea.grp(a.numerator), ea.grp(a.denominator)), neg, unit),
                        _unit(_fixed(a, 2), neg, unit))


def _qty(fr, word):
    return _plain(fr) + " " + (re.sub(r"s$", "", word) if abs(Fraction(fr)) == 1 else word)


# ---------------------------------------------------------------------------
# Lesson-level words: money_unit, qty_unit, silver_unit, pupil_word
# ---------------------------------------------------------------------------

_WORD = re.compile(r"[A-Za-z£$€](?:[A-Za-z£$€ .-]{0,22}[A-Za-z£$€.])?")
_WORDS = {  # cfg key -> (name in FIXED, default, placeholder in field and tile labels)
    "money_unit": ("unit", "£", "%u"),
    "qty_unit": ("qty", "units", "%q"),
    "silver_unit": ("silver", "oz", "%s"),
    "pupil_word": ("pupils", "pupils", "%w"),
}


def _cfg_word(cfg, kit, key):
    _name, default, _ph = _WORDS[key]
    v = cfg.get(key, default)
    if not isinstance(v, str) or not _WORD.fullmatch(v):
        raise ValueError("%s: cfg[%r] is a short plain word or symbol (letters, spaces, dots, hyphens or £ $ €, at "
                         "most 24 characters, such as \"£\", \"s\" or \"oz silver\"), not %r" % (kit, key, v))
    return v


def _label(text, words):
    for ph, value in words.items():
        text = text.replace(ph, value)
    return text


def _words_of(cfg, keys):
    """The label placeholders a view uses, from the cfg (defaults when a value is bad: options() refuses it)."""
    out = {}
    for key in keys:
        _name, default, ph = _WORDS[key]
        v = cfg.get(key, default)
        out[ph] = v if isinstance(v, str) and _WORD.fullmatch(v) else default
    return out


def _options(*keys):
    """options(cfg, kit, tiles) for a view taking money_unit and the other words named."""
    keys = ("money_unit",) + keys

    def options(cfg, kit, tiles):
        fixed = {_WORDS[k][0]: _cfg_word(cfg, kit, k) for k in keys}
        words = {_WORDS[k][2]: fixed[_WORDS[k][0]] for k in keys}
        return fixed, list(keys), [(_label(lab, words), cid) for lab, cid in tiles]
    options.words = keys
    return options


def _rows_of(where, key, f, value):
    """A record field given as a list of dicts ({"year": 1, "rent": 1000}) -> a list of cell lists, in the
    field's cell order. Any other value is returned as it is (acckit's to_text reads strings and lists)."""
    if f["kind"] != "arec" or not isinstance(value, (list, tuple)) or not any(isinstance(r, dict) for r in value):
        return value
    cells = [c for c, _s in f["sub"]]
    out = []
    for i, r in enumerate(value):
        if not isinstance(r, dict):
            raise ValueError("%s: %s, record %d: write every record as a dict or none of them" % (where, key, i + 1))
        if sorted(r) != sorted(cells):
            raise ValueError("%s: %s, record %d has the keys %s; a record takes exactly %s"
                             % (where, key, i + 1, ", ".join(sorted(r)) or "none", ", ".join(cells)))
        out.append([r[c] for c in cells])
    return out


def _with_rows(cfg, kit, fields):
    """cfg with every dict-row record value (cfg-level or in a preset) turned into cell lists."""
    arecs = {key: f for key, f, _d in fields if f["kind"] == "arec"}
    if not arecs:
        return cfg
    cfg = dict(cfg)
    for key, f in arecs.items():
        if key in cfg:
            cfg[key] = _rows_of(kit, key, f, cfg[key])
    if isinstance(cfg.get("presets"), list):
        cfg["presets"] = [dict(p, **{k: _rows_of("%s preset %r" % (kit, p.get("id")), k, arecs[k], p[k])
                                     for k in arecs if k in p}) if isinstance(p, dict) else p
                          for p in cfg["presets"]]
    return cfg


def _builder(mode, spec):
    """mode_lab(cfg, mode, spec), with %u %q %s %w in the chosen view's field labels set from the cfg, and record
    values written as lists of dicts accepted."""
    def build(cfg):
        cfg = cfg or {}
        views = spec["views"]
        view = cfg.get("view", next(iter(views)))
        if view not in views:
            return mode_lab(cfg, mode, spec)
        v = views[view]
        cfg = _with_rows(cfg, "wonkit/%s/%s" % (mode, view), v["fields"])
        words = _words_of(cfg, getattr(v.get("options"), "words", ()))
        fields = [(key, dict(f, what=_label(f["what"], words)), d) for key, f, d in v["fields"]]
        return mode_lab(cfg, mode, dict(spec, views=dict(views, **{view: dict(v, fields=fields)})))
    return build


_MONEY_RULE = ("Amounts are in the lesson's money unit, typed as decimals (at most 6 places) or fractions such as "
               "5/2, and computed exactly; one without a finite decimal is printed as its fraction and its value to "
               "2 places after ≈. ")
_PCT_RULE = ("A percentage is exact when it has at most 2 decimal places and is otherwise rounded to 2 places on the "
             "exact value and marked ≈. ")


# ---------------------------------------------------------------------------
# stock (wst): Book II, and the great proprietor of III.4
# ---------------------------------------------------------------------------

WST_JS = r"""
  var WST_VIEW = {};
  function wstCompute(view, inst, opts) { return eaRun(WST_VIEW[view], inst, opts); }
"""

WST_VIEW_JS = {}

WST_VIEW_JS["division"] = r"""
  WST_VIEW.division = function (inst, o) {
    var kinds = ['consumption', 'fixed', 'circulating'], tot = {}, top = {};
    kinds.forEach(function (k) { tot[k] = R0; top[k] = null; });
    inst.parts.forEach(function (p) {
      tot[p.kind] = Radd(tot[p.kind], p.amount);
      if (top[p.kind] === null || Rcmp(p.amount, top[p.kind].amount) > 0) top[p.kind] = p;
    });
    var all = Radd(Radd(tot.consumption, tot.fixed), tot.circulating);
    if (Rzero(all)) eaRefuse('The parts add to nothing, so there is no stock to divide');
    var cap = Radd(tot.fixed, tot.circulating);
    var part = function (k) { return wstMoney(tot[k], o) + ' (' + wstPc(Rdiv(tot[k], all)) + ')'; };
    return {
      tiles: { wstWhole: wstMoney(all, o), wstConsumption: part('consumption'), wstFixed: part('fixed'),
        wstCirculating: part('circulating'),
        wstCapital: wstMoney(cap, o) + ' of ' + wstMoney(all, o) + ' (' + wstPc(Rdiv(cap, all)) + ')',
        wstLargest: kinds.map(function (k) { return k + ' ' + (top[k] === null ? 'none' : top[k].part + ' ' + wstMoney(top[k].amount, o)); }).join('; ') },
      status: wnkStatus('Of a stock of ' + wstMoney(all, o) + ', ' + wstPc(Rdiv(cap, all)) + ' is capital, fixed and circulating, from which a revenue is expected, and '
        + wstPc(Rdiv(tot.consumption, all)) + ' is reserved for immediate consumption, which yields none'),
      table: { caption: 'Each part of the stock, its kind and its share of the whole', head: ['part', 'kind', 'amount', 'share'],
        rows: inst.parts.map(function (p) { return [p.part, p.kind, wstMoney(p.amount, o), wstPc(Rdiv(p.amount, all))]; }) }
    };
  };
"""

WST_VIEW_JS["revenue"] = r"""
  WST_VIEW.revenue = function (inst, o) {
    var g = inst.gross, keep = Radd(inst.fixed, inst.money), s = inst.saving;
    if (Rcmp(keep, g) > 0) eaRefuse('The maintenance of the fixed capital and of the money, ' + wstMoney(keep, o) + ', is more than the gross revenue, ' + wstMoney(g, o));
    if (s !== '-' && Rcmp(s, inst.money) > 0) eaRefuse('The saving, ' + wstMoney(s, o) + ', is more than the maintenance of the money, ' + wstMoney(inst.money, o));
    var net = Rsub(g, keep), none = 'no saving given', net2 = s === '-' ? null : Radd(net, s);
    var rows = [['gross revenue', wstMoney(g, o), '100%'], ['maintaining the fixed capital', wstMoney(inst.fixed, o), wstPc(Rdiv(inst.fixed, g))],
      ['maintaining the money', wstMoney(inst.money, o), wstPc(Rdiv(inst.money, g))], ['net revenue', wstMoney(net, o), wstPc(Rdiv(net, g))]];
    if (net2) rows.push(['saving on the money', wstMoney(s, o), wstPc(Rdiv(s, g))], ['net revenue with the saving', wstMoney(net2, o), wstPc(Rdiv(net2, g))]);
    return {
      tiles: { wstKeep: wstMoney(keep, o) + ' (' + wstPc(Rdiv(keep, g)) + ' of the gross)', wstNet: wstMoney(net, o),
        wstNetShare: wstPc(Rdiv(net, g)),
        wstNew: net2 ? wstMoney(net2, o) + ' (' + wstPc(Rdiv(net2, g)) + ' of the gross)' : none,
        wstGain: net2 ? wstSigned(s, o) + (Rzero(net) ? '' : ' (' + wstPlus(s, wstPc(Rdiv(s, net))) + ' on the net revenue)') : none },
      status: wnkStatus('The net revenue is ' + wstMoney(net, o) + ', ' + wstPc(Rdiv(net, g)) + ' of the gross: what is left after maintaining the fixed capital and the money'
        + (net2 ? '; the saving on the money raises it to ' + wstMoney(net2, o) : '')),
      table: { caption: 'The gross revenue and what comes off it', head: ['', 'amount', 'share of the gross'], rows: rows }
    };
  };
"""

WST_VIEW_JS["accumulate"] = r"""
  WST_VIEW.accumulate = function (inst, o) {
    var c0 = inst.capital, ret = wstOf(inst['return']), n = Number(inst.years.n), w = inst.wage;
    var grow = function (sv) {
      var f = Radd(R1, Rmul(ret, wstOf(sv))), c = c0, cs = [c0], i;
      for (i = 1; i <= n; i += 1) { c = Rmul(c, f); cs.push(c); }
      return { rate: Rsub(f, R1), cs: cs };
    };
    var a = grow(inst.saved), b = inst.saved2 === '-' ? null : grow(inst.saved2), last = a.cs[n];
    var rev = Rmul(c0, ret), add = Rmul(rev, wstOf(inst.saved)), spent = Rsub(rev, add);
    var yrs = eaPlural(n, 'year', 'years'), lab = function (c) { return wstTwo(Rdiv(c, w)); };
    var head = ['year', 'capital'], rows = [], i;
    if (b) head.push('capital at ' + wstPlain(inst.saved2) + '% saved');
    if (w !== '-') head.push('workers maintained');
    for (i = 0; i <= n; i += 1) {
      var row = [String(i), wstMoney2(a.cs[i], o)];
      if (b) row.push(wstMoney2(b.cs[i], o));
      if (w !== '-') row.push(lab(a.cs[i]));
      rows.push(row);
    }
    var first = 'revenue ' + wstMoney(rev, o) + ': ' + (add.n < 0n
      ? wstMoney(spent, o) + ' spent, ' + wstMoney(Rneg(add), o) + ' of it taken from the capital'
      : wstMoney(add, o) + ' added to the capital, ' + wstMoney(spent, o) + ' spent');
    var way = a.rate.n > 0n ? 'grows' : (a.rate.n < 0n ? 'shrinks' : 'stays');
    return {
      tiles: { wstFirst: first, wstRate: wstPlus(a.rate, wstPc(a.rate)) + ' a year',
        wstAfter: wstMoney2(last, o) + ' after ' + yrs,
        wstChange: n === 0 ? 'no years' : wstPlus(Rsub(last, c0), wstPc(Rdiv(Rsub(last, c0), c0))),
        wstLabour: w === '-' ? 'no wage given' : lab(c0) + ' → ' + lab(last) + ' workers',
        wstSecond: b ? wstMoney2(b.cs[n], o) + ' at ' + wstPlain(inst.saved2) + '% saved (' + wstPlus(Rsub(b.cs[n], last), wstMoney2(Rsub(b.cs[n], last), o)) + ' against the first)' : 'no second saving given' },
      status: wnkStatus('A capital of ' + wstMoney(c0, o) + ' whose revenue is ' + wstPlain(inst['return']) + '% of it a year, ' + wstPlain(inst.saved) + '% of that revenue added to it, '
        + way + (way === 'stays' ? ' at ' + wstMoney(c0, o) : ' by ' + wstPc(Rabs(a.rate)) + ' a year, to ' + wstMoney2(last, o) + ' after ' + yrs)),
      table: { caption: 'The capital at the end of each year' + (b ? ', at both savings' : ''), head: head, rows: rows }
    };
  };
"""

WST_VIEW_JS["turnover"] = r"""
  WST_VIEW.turnover = function (inst, o) {
    var T = inst.trades.map(function (t) { return { name: t.trade, cap: t.capital, ret: t.returns, work: Rmul(t.capital, t.returns) }; });
    var order = T.slice().sort(function (a, b) { return Rcmp(b.work, a.work); }), hi = order[0], lo = order[order.length - 1], w = inst.wage;
    var total = eaSum(T.map(function (t) { return t.work; }));
    return {
      tiles: { wstWork: T.map(function (t) { return t.name + ' ' + wstMoney(t.work, o); }).join('; '), wstTotal: wstMoney(total, o),
        wstLabour: w === '-' ? 'no wage given' : T.map(function (t) { return t.name + ' ' + wstTwo(Rdiv(t.work, w)); }).join('; '),
        wstOrder: order.map(function (t) { return t.name; }).join(', '),
        wstRatio: T.length === 1 ? 'one trade only' : aktTimes(Rdiv(hi.work, lo.work)) + ' (' + hi.name + ' against ' + lo.name + ')' },
      status: wnkStatus('Over a year ' + hi.name + ' puts the most stock to work, ' + wstMoney(hi.work, o)
        + (T.length === 1 ? '' : ', and ' + lo.name + ' the least, ' + wstMoney(lo.work, o)) + ': a capital that returns n times a year replaces n times over the stock that maintains labour'),
      table: { caption: 'Each trade: its capital, its returns a year and the stock it puts to work over a year', head: ['trade', 'capital', 'returns a year', 'at work over a year'].concat(w === '-' ? [] : ['workers maintained']),
        rows: T.map(function (t) { return [t.name, wstMoney(t.cap, o), wstPlain(t.ret), wstMoney(t.work, o)].concat(w === '-' ? [] : [wstTwo(Rdiv(t.work, w))]); }) }
    };
  };
"""

WST_VIEW_JS["spend"] = r"""
  WST_VIEW.spend = function (inst, o) {
    var rev = inst.revenue, m = inst.maintenance, P = inst.purchases;
    var spent = eaSum(P.map(function (p) { return p.amount; }));
    if (Rcmp(spent, rev) > 0) eaRefuse('The purchases add to ' + wstMoney(spent, o) + ', more than the revenue, ' + wstMoney(rev, o));
    var kept = Rdiv(rev, m), people = eaSum(P.map(function (p) { return p.makers; }));
    var share = function (p) { return Rdiv(Rdiv(p.amount, p.makers), m); };
    var whole = P.filter(function (p) { return Rcmp(share(p), R1) >= 0; }).map(function (p) { return p.trade; });
    var big = P.slice().sort(function (a, b) { return Rcmp(share(b), share(a)); })[0];
    return {
      tiles: { wstRetainers: wstPlain(kept) + (Requ(kept, R1) ? ' person' : ' people') + (Rint(kept) ? '' : ' (' + eaInt(eaFloor(kept)) + ' wholly)'),
        wstSpent: wstMoney(spent, o) + ' of ' + wstMoney(rev, o) + ' (' + wstPc(Rdiv(spent, rev)) + ')',
        wstShares: P.map(function (p) { return p.trade + ' ' + wstPc(share(p)); }).join('; '),
        wstPeople: eaPlural(people.n, 'person', 'people'),
        wstDependent: whole.length ? aktListed(whole.length, whole) + ' (each maker wholly maintained by the purchase)' : 'no one: every maker’s share is under one maintenance' },
      status: wnkStatus('Spent on retainers, the revenue maintains ' + wstPlain(kept) + ' people, each wholly dependent on the one who spends it; spent on the purchases, '
        + wstMoney(spent, o) + ' pays part of the maintenance of ' + eaPlural(people.n, 'person', 'people') + ', the largest part ' + wstPc(share(big)) + ' (' + big.trade + ')'),
      table: { caption: 'Each purchase: what it pays each maker, as a share of one maintenance', head: ['trade', 'spent', 'makers', 'each maker', 'share of a maintenance'],
        rows: P.map(function (p) { return [p.trade, wstMoney(p.amount, o), eaInt(p.makers.n), wstMoney(Rdiv(p.amount, p.makers), o), wstPc(share(p))]; }) }
    };
  };
"""


def _check_division(inst, fixed):
    if sum((p["amount"] for p in inst["parts"]), Fraction(0)) == 0:
        raise ValueError("The parts add to nothing, so there is no stock to divide")


def _check_revenue(inst, fixed):
    keep = inst["fixed"] + inst["money"]
    if keep > inst["gross"]:
        raise ValueError("The maintenance of the fixed capital and of the money, %s, is more than the gross revenue, %s"
                         % (_money(keep, fixed), _money(inst["gross"], fixed)))
    if inst["saving"] != "-" and inst["saving"] > inst["money"]:
        raise ValueError("The saving, %s, is more than the maintenance of the money, %s"
                         % (_money(inst["saving"], fixed), _money(inst["money"], fixed)))


def _check_spend(inst, fixed):
    spent = sum((p["amount"] for p in inst["purchases"]), Fraction(0))
    if spent > inst["revenue"]:
        raise ValueError("The purchases add to %s, more than the revenue, %s"
                         % (_money(spent, fixed), _money(inst["revenue"], fixed)))


_M = rat(lo=0, hi=_BIG)       # an amount, 0 allowed
_MP = rat(gt=0, hi=_BIG)      # an amount above 0
_MD = rat(gt=0, hi=_BIG, dash=True)
_PCT = rat(lo=0, hi=100)      # a percentage, 0 to 100


def _recs(what, sub, lo=1, unique=True, rows=4):
    return arec(what, sub, unique=unique, rows=rows, lo=lo, hi=_RECS)


STOCK = {
    "prefix": "wst", "fn": "wstCompute", "title": "Stock and its employments", "js": _shared("wst") + WST_JS,
    "views": {
        "division": {
            "fields": [("parts", _recs("Parts of the stock (part, amount in %u, kind: consumption, fixed or circulating)",
                                       [("part", _N), ("amount", _M),
                                        ("kind", ea.word("consumption", "fixed", "circulating"))]), None)],
            "tiles": [("Whole stock", "wstWhole"), ("Reserved for immediate consumption", "wstConsumption"),
                      ("Fixed capital", "wstFixed"), ("Circulating capital", "wstCirculating"),
                      ("Capital (fixed and circulating) of the whole", "wstCapital"),
                      ("Largest part of each kind", "wstLargest")],
            "check": _check_division, "options": _options(),
            "subtitle": "a stock divided into the part kept for consumption, fixed capital and circulating capital",
            "rules": "Each part is put by the lesson into one of Smith's three portions of a stock (Book II, chapter "
                     "1): the part reserved for immediate consumption, which affords no revenue; fixed capital, "
                     "which yields a revenue without changing masters; circulating capital, which yields one by "
                     "parting with it. The lab sums each kind; a share is its sum over the whole stock. Capital is "
                     "fixed plus circulating. The largest part of each kind is the first one given when two are "
                     "equal (the lab's rule). Which kind a part belongs to is the lesson's assignment, not the "
                     "lab's. " + _MONEY_RULE + _PCT_RULE,
            "js": WST_VIEW_JS["division"],
        },
        "revenue": {
            "fields": [("gross", ea.field("Gross revenue: the whole annual produce, in %u", _MP), None),
                       ("fixed", ea.field("Maintaining the fixed capital, a year, in %u", _M), None),
                       ("money", ea.field("Maintaining the money in circulation, a year, in %u", _M), None),
                       ("saving", ea.field("A saving on the money's maintenance, in %u (- for none)",
                                           rat(lo=0, hi=_BIG, dash=True)), "-")],
            "tiles": [("Fixed capital and money maintained", "wstKeep"), ("Net revenue", "wstNet"),
                      ("Net revenue, share of the gross", "wstNetShare"), ("Net revenue with the saving", "wstNew"),
                      ("Gain from the saving", "wstGain")],
            "check": _check_revenue, "options": _options(),
            "subtitle": "gross and net revenue, and what a cheaper money adds to the net",
            "rules": "Net revenue = gross revenue − the maintenance of the fixed capital − the maintenance of the "
                     "money, Smith's rule in Book II, chapter 2: neither the fixed capital's upkeep nor the money, "
                     "\"the great wheel of circulation\", is part of the net revenue. A saving on the money (paper "
                     "for gold, say) is added to the net revenue whole; the lab adds no other effect of it. A "
                     "maintenance above the gross, or a saving above the money's maintenance, is refused. "
                     + _MONEY_RULE + _PCT_RULE,
            "js": WST_VIEW_JS["revenue"],
        },
        "accumulate": {
            "fields": [("capital", ea.field("Capital at the start, in %u", _MP), None),
                       ("return", ea.field("Revenue the capital yields above replacing itself, % of the capital a "
                                           "year", _PCT), None),
                       ("saved", ea.field("Share of that revenue added to the capital, % (negative: capital spent "
                                          "as well)", rat(lo=-100, hi=100)), None),
                       ("years", ea.field("Years (0 to 50)", ea.whole(0, 50)), None),
                       ("wage", ea.field("A year's maintenance of one productive worker, in %u (- for none)", _MD),
                        "-"),
                       ("saved2", ea.field("A second share saved, to compare, % (- for none)",
                                           rat(lo=-100, hi=100, dash=True)), "-")],
            "tiles": [("First year's revenue", "wstFirst"), ("Change in the capital a year", "wstRate"),
                      ("Capital after the years", "wstAfter"), ("Change over the years", "wstChange"),
                      ("Productive workers maintained, first and last", "wstLabour"),
                      ("At the second share saved", "wstSecond")],
            "check": None, "options": _options(),
            "subtitle": "a capital increased by parsimony or diminished by prodigality, year by year",
            "rules": "Each year the capital yields its revenue, the return % of the capital; the share saved of it "
                     "is added to the capital and the rest is spent. A negative share saved spends the whole "
                     "revenue and takes that share of it from the capital as well, Smith's prodigal who encroaches "
                     "on his capital. So the capital is multiplied each year by 1 + return × saved (both as "
                     "shares), exactly, over whole years (at most 50); the bounds keep it from falling below 0. "
                     "Workers maintained = capital ÷ a worker's yearly maintenance. That what is saved maintains "
                     "productive hands and what is spent idle ones is Smith's rule (Book II, chapter 3); the "
                     "constant return is the lab's. Long figures are shown to 2 places by an exact rounding, marked "
                     "≈. " + _MONEY_RULE + _PCT_RULE,
            "js": WST_VIEW_JS["accumulate"],
        },
        "turnover": {
            "fields": [("trades", _recs("Trades (trade, capital in %u, returns a year such as 4 or 1/2)",
                                        [("trade", _N), ("capital", _MP), ("returns", rat(gt=0, hi=365))]), None),
                       ("wage", ea.field("A year's maintenance of one productive worker, in %u (- for none)", _MD),
                        "-")],
            "tiles": [("Stock put to work over a year", "wstWork"), ("All the trades together", "wstTotal"),
                      ("Productive workers it maintains", "wstLabour"), ("Most to least", "wstOrder"),
                      ("Most against least", "wstRatio")],
            "check": None, "options": _options(),
            "subtitle": "how much labour a capital maintains by how often it returns",
            "rules": "Stock put to work over a year = capital × returns a year (a capital that comes back four "
                     "times a year is laid out four times; one that comes back once in two years, 1/2, half once). "
                     "That the labour a capital maintains goes with its returns is Smith's (Book II, chapter 5); "
                     "workers maintained = stock at work ÷ a worker's yearly maintenance, shown to 2 places. Trades "
                     "are ordered from most to least, ties in the order given; the ratio is the most over the least, "
                     "to 2 places. Smith's further ranking of agriculture above the other trades is not computed. "
                     + _MONEY_RULE,
            "js": WST_VIEW_JS["turnover"],
        },
        "spend": {
            "fields": [("revenue", ea.field("The revenue spent, a year, in %u", _MP), None),
                       ("maintenance", ea.field("One person's maintenance, a year, in %u", _MP), None),
                       ("purchases", _recs("Purchases (trade, amount spent in %u, makers whose produce it buys)",
                                           [("trade", _N), ("amount", _MP), ("makers", ea.whole(1, ea.LIMIT))]),
                        None)],
            "tiles": [("Retainers the revenue could maintain", "wstRetainers"), ("Spent on the purchases", "wstSpent"),
                      ("Each maker's share of a maintenance", "wstShares"), ("People partly maintained", "wstPeople"),
                      ("Makers wholly dependent on the buyer", "wstDependent")],
            "check": _check_spend, "options": _options(),
            "subtitle": "a revenue spent on retainers against the same spent on goods",
            "rules": "Retainers = revenue ÷ one person's maintenance: spent on hospitality, every one of them "
                     "depends wholly on the spender. A purchase pays each of its makers amount ÷ makers, which as a "
                     "share of one maintenance is amount ÷ makers ÷ maintenance (the lab spreads it evenly, its own "
                     "rule). People partly maintained = the makers of all the purchases added, a maker named in two "
                     "purchases counted twice. A maker whose share is 1 or more is wholly maintained by that "
                     "purchase. Smith's argument (Book III, chapter 4) is that a buyer of goods contributes \"a very "
                     "small proportion\" to the maintenance of each maker, so no one depends on him. Purchases "
                     "above the revenue are refused. " + _MONEY_RULE + _PCT_RULE,
            "js": WST_VIEW_JS["spend"],
        },
    },
}

# ---------------------------------------------------------------------------
# bank (wbk): Book II, chapter 2
# ---------------------------------------------------------------------------

WBK_JS = r"""
  var WBK_VIEW = {};
  function wbkCompute(view, inst, opts) { return eaRun(WBK_VIEW[view], inst, opts); }
"""

WBK_VIEW_JS = {}

WBK_VIEW_JS["paper"] = r"""
  WBK_VIEW.paper = function (inst, o) {
    var C = inst.circulation, N = inst.notes, r = wbkOf(inst.reserve), kept = Rmul(N, r);
    if (Rcmp(kept, C) > 0) eaRefuse('The reserve, ' + wbkMoney(kept, o) + ', is more than all the gold and silver in circulation, ' + wbkMoney(C, o) + ', so the banks could not gather it');
    var over = Rcmp(N, C) > 0, held = over ? C : N, excess = over ? Rsub(N, C) : R0, need = Radd(Rmul(held, r), excess);
    var before = Radd(N, Rsub(C, kept)), abroad = Rsub(N, kept);
    return {
      tiles: { wbkKept: wbkMoney(kept, o),
        wbkBefore: wbkMoney(before, o) + ' (' + wbkMoney(N, o) + ' of notes, ' + wbkMoney(Rsub(C, kept), o) + ' of coin)',
        wbkAbroad: over ? 'not determined: the notes exceed the circulation' : wbkMoney(abroad, o),
        wbkCoin: over ? 'none' : wbkMoney(Rsub(C, N), o),
        wbkExcess: over ? wbkMoney(excess, o) : 'none: the notes do not exceed the circulation',
        wbkNeeded: wbkMoney(need, o) + (over ? ' (' + wbkMoney(Rsub(need, kept), o) + ' more than the reserve kept)' : ' (the reserve kept)') },
      status: wnkStatus(over
        ? 'Notes of ' + wbkMoney(N, o) + ' exceed the circulation of ' + wbkMoney(C, o) + ' by ' + wbkMoney(excess, o) + ', which returns on the banks for coin, so they need ' + wbkMoney(need, o) + ' in coin, not the ' + wbkMoney(kept, o) + ' kept'
        : 'Notes of ' + wbkMoney(N, o) + ' put ' + wbkMoney(before, o) + ' of paper and coin into a channel that holds ' + wbkMoney(C, o) + '; the ' + wbkMoney(abroad, o) + ' of gold and silver that overflows is free to go abroad'),
      table: { caption: 'The channel of circulation before and after the notes', head: ['', 'amount'],
        rows: [['gold and silver needed to circulate the produce', wbkMoney(C, o)], ['notes issued', wbkMoney(N, o)], ['coin kept by the banks', wbkMoney(kept, o)],
          ['paper and coin poured in', wbkMoney(before, o)], ['overflow: coin free to go abroad', over ? 'not determined' : wbkMoney(abroad, o)],
          ['notes beyond the circulation', wbkMoney(excess, o)], ['coin the banks need', wbkMoney(need, o)]] }
    };
  };
"""

WBK_VIEW_JS["redraw"] = r"""
  WBK_VIEW.redraw = function (inst, o) {
    var m = Number(inst.months.n);
    if (12 % m !== 0) eaRefuse('A bill of ' + m + ' months does not go a whole number of times into a year; the lab takes bills of 1, 2, 3, 4, 6 or 12 months');
    var k = 12 / m, y = Number(inst.years.n), S = inst.sum, i = wbkOf(inst.interest), c = wbkOf(inst.commission);
    var simple = Radd(i, Rmul(c, R(BigInt(k)))), f = Radd(R1, Radd(Rdiv(Rmul(i, R(BigInt(m))), R(12n)), c));
    var g1 = R1, g = R1, rows = [], t, d;
    for (d = 0; d < k; d += 1) g1 = Rmul(g1, f);
    var comp = Rsub(g1, R1);
    for (t = 1; t <= y; t += 1) {
      g = Rmul(g, g1);
      rows.push([String(t), wbkMoney(Rmul(S, Rmul(simple, R(BigInt(t)))), o), wbkMoney2(Rmul(S, Rsub(g, R1)), o)]);
    }
    var yrs = eaPlural(y, 'year', 'years');
    return {
      tiles: { wbkDraws: eaPlural(k, 'draw', 'draws') + ' a year',
        wbkSimple: wbkPc(simple) + ' a year, ' + wbkMoney(Rmul(S, simple), o),
        wbkCompound: wbkPc(comp) + ' a year, ' + wbkMoney2(Rmul(S, comp), o),
        wbkTotal: 'simple ' + wbkMoney(Rmul(S, Rmul(simple, R(BigInt(y)))), o) + ', compound ' + wbkMoney2(Rmul(S, Rsub(g, R1)), o) + ' over ' + yrs,
        wbkExcess: 'simple ' + wbkPts(Rsub(simple, i)) + ', compound ' + wbkPts(Rsub(comp, i)) },
      status: wnkStatus('Raised by drawing and redrawing ' + eaPlural(k, 'time', 'times') + ' a year, the money costs ' + wbkPc(comp) + ' a year, against the '
        + wbkPc(i) + ' stated as interest'),
      table: { caption: 'Cost of the sum raised, to the end of each year', head: ['year', 'simple', 'compound'], rows: rows }
    };
  };
"""


def _check_paper(inst, fixed):
    kept = inst["notes"] * inst["reserve"] / 100
    if kept > inst["circulation"]:
        raise ValueError("The reserve, %s, is more than all the gold and silver in circulation, %s, so the banks could "
                         "not gather it" % (_money(kept, fixed), _money(inst["circulation"], fixed)))


def _check_redraw(inst, fixed):
    m = int(inst["months"])
    if 12 % m:
        raise ValueError("A bill of %d months does not go a whole number of times into a year; the lab takes bills of "
                         "1, 2, 3, 4, 6 or 12 months" % m)


BANK = {
    "prefix": "wbk", "fn": "wbkCompute", "title": "Banks and paper money", "js": _shared("wbk") + WBK_JS,
    "views": {
        "paper": {
            "fields": [("circulation", ea.field("Gold and silver needed to circulate the annual produce, in %u", _MP),
                        None),
                       ("notes", ea.field("Bank notes issued, in %u", _M), None),
                       ("reserve", ea.field("Reserve kept in coin, % of the notes", _PCT), None)],
            "tiles": [("Coin kept by the banks", "wbkKept"), ("Paper and coin poured into the channel", "wbkBefore"),
                      ("Gold and silver free to go abroad", "wbkAbroad"), ("Coin still circulating", "wbkCoin"),
                      ("Notes beyond the circulation, returned on the banks", "wbkExcess"),
                      ("Coin the banks need", "wbkNeeded")],
            "check": _check_paper, "options": _options(),
            "subtitle": "the gold and silver a paper money sends abroad, and the reserve it needs",
            "rules": "Smith's channel (Book II, chapter 2): the produce needs a fixed sum to circulate it. The banks "
                     "keep the reserve % of their notes in coin, drawn from the circulation, so paper and coin "
                     "poured in = notes + (circulation − coin kept). While the notes do not exceed the "
                     "circulation, what the channel cannot hold overflows: notes − coin kept, sent abroad as gold "
                     "and silver; coin still circulating = circulation − notes. Notes beyond the circulation return "
                     "on the banks for coin; then the lab says what goes abroad is not determined, and the coin the "
                     "banks need = the reserve on the notes the channel holds + every note beyond it (the lab's "
                     "rule). A reserve larger than all the coin in circulation is refused. " + _MONEY_RULE,
            "js": WBK_VIEW_JS["paper"],
        },
        "redraw": {
            "fields": [("sum", ea.field("The sum raised, in %u", _MP), None),
                       ("interest", ea.field("Interest, % a year", _PCT), None),
                       ("commission", ea.field("Commission, % of the sum on each draw", _PCT), None),
                       ("months", ea.field("Each bill's term, in months (1, 2, 3, 4, 6 or 12)", ea.whole(1, 12)),
                        None),
                       ("years", ea.field("Years (1 to 50)", ea.whole(1, 50)), None)],
            "tiles": [("Draws a year", "wbkDraws"), ("Cost a year, simple", "wbkSimple"),
                      ("Cost a year, compound", "wbkCompound"), ("Cost over the years", "wbkTotal"),
                      ("Above the interest stated", "wbkExcess")],
            "check": _check_redraw, "options": _options(),
            "subtitle": "what money raised by circular bills costs, interest and commission each round",
            "rules": "A bill of m months is drawn 12 ÷ m times a year (the lab takes only terms that go a whole "
                     "number of times into a year). Simple: interest + commission × draws, the way Smith adds them "
                     "(Book II, chapter 2). Compound: each draw must repay the last bill with its interest for m "
                     "months and the commission, so the sum owed is multiplied by 1 + interest × m ÷ 12 + "
                     "commission at every draw, exactly; the cost is that growth less 1. Over the years the simple "
                     "cost is the year's times the years and the compound cost the growth over every draw. "
                     + _MONEY_RULE + _PCT_RULE + "Percentage points are printed the same way.",
            "js": WBK_VIEW_JS["redraw"],
        },
    },
}

# ---------------------------------------------------------------------------
# trade (wtr): Book IV
# ---------------------------------------------------------------------------

WTR_JS = r"""
  var WTR_VIEW = {};
  function wtrCompute(view, inst, opts) { return eaRun(WTR_VIEW[view], inst, opts); }
"""

WTR_VIEW_JS = {}

WTR_VIEW_JS["make"] = r"""
  WTR_VIEW.make = function (inst, o) {
    var G = inst.goods.map(function (g) {
      var abroad = Radd(g.foreign, g.duty), buy = Rcmp(abroad, g.home) < 0;
      var free = Rcmp(g.foreign, g.home) < 0 ? g.foreign : g.home, paid = buy ? abroad : g.home;
      return { name: g.good, q: g.quantity, home: g.home, foreign: g.foreign, duty: g.duty, abroad: abroad, buy: buy,
        prohibit: Rcmp(g.home, g.foreign) > 0 ? Rmul(g.quantity, Rsub(g.home, g.foreign)) : R0,
        revenue: buy ? Rmul(g.quantity, g.duty) : R0, extra: Rmul(g.quantity, Rsub(paid, free)) };
    });
    var sum = function (k) { return eaSum(G.map(function (g) { return g[k]; })); };
    var prohibit = sum('prohibit'), revenue = sum('revenue'), extra = sum('extra');
    var where = function (g) { var c = Rcmp(g.home, g.abroad); return c < 0 ? 'home' : (c > 0 ? 'abroad' : 'either (the same)'); };
    return {
      tiles: { wtrAbroad: G.map(function (g) { return g.name + ' ' + wtrMoney(g.abroad, o); }).join('; '),
        wtrCheaper: G.map(function (g) { return g.name + ' ' + where(g); }).join('; '),
        wtrProhibit: wtrMoney(prohibit, o) + ' a year',
        wtrDuty: wtrMoney(revenue, o) + ' a year',
        wtrBuyers: wtrMoney(extra, o) + ' a year',
        wtrLoss: wtrMoney(Rsub(extra, revenue), o) + ' a year' },
      status: wnkStatus('Making at home every good bought cheaper abroad costs the country ' + wtrMoney(prohibit, o) + ' a year; with the duties, buyers pay '
        + wtrMoney(extra, o) + ' more than at the cheaper price, of which ' + wtrMoney(revenue, o) + ' is duty paid to the treasury'),
      table: { caption: 'Each good: its cost made at home, bought abroad with the duty, and where it is bought', head: ['good', 'quantity', 'home', 'foreign', 'with the duty', 'bought', 'duty paid', 'buyers pay more'],
        rows: G.map(function (g) { return [g.name, wtrQty(g.q, o.qty), wtrMoney(g.home, o), wtrMoney(g.foreign, o), wtrMoney(g.abroad, o), g.buy ? 'abroad' : 'at home', wtrMoney(g.revenue, o), wtrMoney(g.extra, o)]; }) }
    };
  };
"""

WTR_VIEW_JS["balance"] = r"""
  WTR_VIEW.balance = function (inst, o) {
    var C = inst.countries, bal = function (c) { return Rsub(c.exports, c.imports); };
    var total = eaSum(C.map(bal)), two = eaSum(C.map(function (c) { return Radd(c.exports, c.imports); }));
    var bad = C.filter(function (c) { return bal(c).n < 0n; }).map(function (c) { return c.country; });
    return {
      tiles: { wtrBalances: C.map(function (c) { return c.country + ' ' + wtrSigned(bal(c), o); }).join('; '),
        wtrTotal: wtrSigned(total, o), wtrUnfavourable: aktListed(bad.length, bad), wtrTwoWay: wtrMoney(two, o) },
      status: wnkStatus('Exports less imports come to ' + wtrSigned(total, o) + ' over ' + eaPlural(C.length, 'country', 'countries') + ', ' + eaInt(bad.length)
        + ' of them with more imports than exports; the balance is the mercantile system’s measure, which Smith rejects, and the two-way trade is ' + wtrMoney(two, o)),
      table: { caption: 'Each country: exports, imports and the balance', head: ['country', 'exports', 'imports', 'balance'],
        rows: C.map(function (c) { return [c.country, wtrMoney(c.exports, o), wtrMoney(c.imports, o), wtrSigned(bal(c), o)]; }) }
    };
  };
"""

WTR_VIEW_JS["bounty"] = r"""
  WTR_VIEW.bounty = function (inst, o) {
    var treasury = Rmul(inst.exported, inst.bounty), buyers = Rmul(inst.home, inst.rise), total = Radd(treasury, buyers);
    var one = wtrOne(o.qty);
    return {
      tiles: { wtrTreasury: wtrMoney(treasury, o), wtrConsumers: wtrMoney(buyers, o), wtrTotal: wtrMoney(total, o),
        wtrPerUnit: Rzero(inst.exported) ? 'nothing is exported' : wtrMoney(Rdiv(total, inst.exported), o) + ' a ' + one + ' exported',
        wtrRatio: Rzero(treasury) ? 'no bounty is paid' : wtrPlain(Rdiv(buyers, treasury)) + ' paid by home buyers for each 1 paid to the bounty' },
      status: wnkStatus('The bounty costs the treasury ' + wtrMoney(treasury, o) + ' and home buyers ' + wtrMoney(buyers, o) + ' in the higher price, '
        + wtrMoney(total, o) + ' together; the rise in the home price is the lesson’s supposition, as it is Smith’s'),
      table: { caption: 'The two taxes a bounty lays on the people', head: ['', 'quantity', 'a ' + one, 'cost'],
        rows: [['the bounty on exports', wtrQty(inst.exported, o.qty), wtrMoney(inst.bounty, o), wtrMoney(treasury, o)],
          ['the higher price at home', wtrQty(inst.home, o.qty), wtrMoney(inst.rise, o), wtrMoney(buyers, o)]] }
    };
  };
"""

WTR_VIEW_JS["drawback"] = r"""
  WTR_VIEW.drawback = function (inst, o) {
    var q = inst.quantity, e = inst.exported;
    if (Rcmp(e, q) > 0) eaRefuse('The quantity re-exported, ' + wtrQty(e, o.qty) + ', is more than the quantity imported, ' + wtrQty(q, o.qty));
    var paid = Rmul(q, inst.duty), drawn = Rmul(Rmul(e, inst.duty), wtrOf(inst.share)), net = Rsub(paid, drawn), home = Rsub(q, e);
    return {
      tiles: { wtrPaid: wtrMoney(paid, o), wtrDrawn: wtrMoney(drawn, o), wtrNet: wtrMoney(net, o),
        wtrKept: Rzero(home) ? 'nothing is kept at home' : wtrMoney(Rdiv(net, home), o) + ' a ' + wtrOne(o.qty) + ' on ' + wtrQty(home, o.qty) },
      status: wnkStatus('Of ' + wtrMoney(paid, o) + ' paid in duty, ' + wtrMoney(drawn, o) + ' is drawn back on what is re-exported, leaving ' + wtrMoney(net, o)
        + ' on the goods consumed at home'),
      table: { caption: 'The duty paid, drawn back and kept', head: ['', 'quantity', 'duty'],
        rows: [['imported', wtrQty(q, o.qty), wtrMoney(paid, o)], ['re-exported', wtrQty(e, o.qty), wtrMoney(Rneg(drawn), o)], ['kept at home', wtrQty(home, o.qty), wtrMoney(net, o)]] }
    };
  };
"""


def _check_drawback(inst, fixed):
    if inst["exported"] > inst["quantity"]:
        raise ValueError("The quantity re-exported, %s, is more than the quantity imported, %s"
                         % (_qty(inst["exported"], fixed["qty"]), _qty(inst["quantity"], fixed["qty"])))


TRADE = {
    "prefix": "wtr", "fn": "wtrCompute", "title": "Trade and its restraints", "js": _shared("wtr") + WTR_JS,
    "views": {
        "make": {
            "fields": [("goods", _recs("Goods (good, %q a year, cost a unit made at home, price a unit abroad "
                                       "delivered, duty a unit if bought abroad; all in %u)",
                                       [("good", _N), ("quantity", _MP), ("home", _MP), ("foreign", _M),
                                        ("duty", _M)]), None)],
            "tiles": [("Cost a unit bought abroad, with the duty", "wtrAbroad"), ("Cheaper", "wtrCheaper"),
                      ("Cost to the country of making all at home", "wtrProhibit"), ("Duty collected", "wtrDuty"),
                      ("Buyers pay more than at the cheaper price", "wtrBuyers"),
                      ("Paid by buyers and not collected as duty", "wtrLoss")],
            "check": None, "options": _options("qty_unit"),
            "subtitle": "the cost of making at home what could be bought cheaper abroad",
            "rules": "Bought abroad a unit costs the foreign price + the duty. Buyers buy abroad only when that is "
                     "less than the home cost, and at home when the two are equal (the lab's rule). A prohibition "
                     "makes every good at home: its cost to the country is quantity × (home cost − foreign price) "
                     "on each good dearer at home, nothing on the others, the comparison Smith makes in Book IV, "
                     "chapter 2 (the duty is a payment within the country and not part of it). With the duties as "
                     "given, buyers pay quantity × (the price they pay − the cheaper of the home cost and the "
                     "foreign price); the duty collected is quantity × duty on the goods bought abroad; what buyers "
                     "pay and the treasury does not collect is the difference. " + _MONEY_RULE,
            "js": WTR_VIEW_JS["make"],
        },
        "balance": {
            "fields": [("countries", _recs("Countries (country, exports to it, imports from it; in %u)",
                                           [("country", _N), ("exports", _M), ("imports", _M)]), None)],
            "tiles": [("Balance with each country", "wtrBalances"), ("Balance with all", "wtrTotal"),
                      ("Countries with an unfavourable balance", "wtrUnfavourable"), ("Two-way trade", "wtrTwoWay")],
            "check": None, "options": _options(),
            "subtitle": "the balance of trade, country by country: the mercantile measure, computed for reading",
            "rules": "Balance = exports − imports, signed: + is what the mercantile writers call favourable, − "
                     "unfavourable. The total adds the balances; two-way trade adds exports and imports. Countries "
                     "go in the order given. The balance of trade is the mercantile system's measure, which Smith "
                     "rejects (Book IV, chapters 1 and 3): the lab computes it so that it can be read, not because "
                     "it measures a gain. " + _MONEY_RULE,
            "js": WTR_VIEW_JS["balance"],
        },
        "bounty": {
            "fields": [("exported", ea.field("Quantity exported, %q", _M), None),
                       ("bounty", ea.field("Bounty a unit exported, in %u", _M), None),
                       ("home", ea.field("Quantity bought at home, %q", _M), None),
                       ("rise", ea.field("Rise in the home price a unit, in %u, that the lesson supposes the bounty "
                                         "causes", _M), None)],
            "tiles": [("Cost to the treasury", "wtrTreasury"), ("Cost to home buyers", "wtrConsumers"),
                      ("Together", "wtrTotal"), ("Together, a unit exported", "wtrPerUnit"),
                      ("Home buyers' part against the bounty's", "wtrRatio")],
            "check": None, "options": _options("qty_unit"),
            "subtitle": "the two taxes a bounty on exportation lays on the people",
            "rules": "Cost to the treasury = quantity exported × the bounty; cost to home buyers = quantity bought "
                     "at home × the rise in the home price; together, and together over the quantity exported. "
                     "These are Smith's two taxes (Book IV, chapter 5). The rise in the price is the lesson's "
                     "supposition, as it is Smith's: the lab does not derive it from the bounty. A prohibition's "
                     "cost to consumers is the same sum with no bounty (bounty 0). " + _MONEY_RULE,
            "js": WTR_VIEW_JS["bounty"],
        },
        "drawback": {
            "fields": [("quantity", ea.field("Quantity imported, %q, all paying the duty", _MP), None),
                       ("duty", ea.field("Duty a unit, in %u", _M), None),
                       ("exported", ea.field("Quantity re-exported, %q", _M), None),
                       ("share", ea.field("Share of the duty drawn back on re-exportation, %", _PCT), "100")],
            "tiles": [("Duty paid", "wtrPaid"), ("Drawn back", "wtrDrawn"), ("Net duty", "wtrNet"),
                      ("Net duty a unit kept at home", "wtrKept")],
            "check": _check_drawback, "options": _options("qty_unit"),
            "subtitle": "a duty repaid on the goods that are exported again",
            "rules": "Duty paid = quantity imported × duty; drawn back = quantity re-exported × duty × the share "
                     "drawn back; net = paid − drawn back, over the quantity kept at home (imported − re-exported). "
                     "Smith's point (Book IV, chapter 4) is that a whole drawback leaves the duty on home "
                     "consumption only. Re-exporting more than was imported is refused. " + _MONEY_RULE,
            "js": WTR_VIEW_JS["drawback"],
        },
    },
}

# ---------------------------------------------------------------------------
# tax (wtx): Book V, chapter 2 (and the town's farm of III.3)
# ---------------------------------------------------------------------------

WTX_JS = r"""
  var WTX_VIEW = {};
  function wtxCompute(view, inst, opts) { return eaRun(WTX_VIEW[view], inst, opts); }
"""

WTX_VIEW_JS = {}

WTX_VIEW_JS["incidence"] = r"""
  WTX_VIEW.incidence = function (inst, o) {
    var w = inst.wage, t = wtxOf(inst.rate);
    if (Requ(t, R1)) eaRefuse('A tax of 100% of the wage takes all of it, and no wage could leave the worker anything');
    var w2 = Rdiv(w, Rsub(R1, t)), rise = Rsub(Rdiv(w2, w), R1), tax = Rmul(w2, t);
    return {
      tiles: { wtxWage: wtxMoney(w2, o), wtxRise: wtxPc(rise) + ' (' + wtxSigned(Rsub(w2, w), o) + ')', wtxTax: wtxMoney(tax, o),
        wtxOver: 'the rise exceeds the rate by ' + wtxPts(Rsub(rise, t)).replace(/^(≈ )?\+/, '$1'),
        wtxAdvances: 'the employer, in the higher wage' },
      status: wnkStatus('To leave the worker ' + wtxMoney(w, o) + ' after a tax of ' + wtxPc(t) + ', the wage must rise to ' + wtxMoney(w2, o) + ', by '
        + wtxPc(rise) + ', more than the rate, while the demand for labour and the price of provisions stay as they were'),
      table: { caption: 'The wage before and after the tax', head: ['', 'wage', 'tax', 'left to the worker'],
        rows: [['before the tax', wtxMoney(w, o), wtxMoney(R0, o), wtxMoney(w, o)], ['after the tax', wtxMoney(w2, o), wtxMoney(tax, o), wtxMoney(Rsub(w2, tax), o)]] }
    };
  };
"""

WTX_VIEW_JS["arithmetic"] = r"""
  WTX_VIEW.arithmetic = function (inst, o) {
    var Rw = inst.rows, i;
    for (i = 1; i < Rw.length; i += 1) {
      if (Rcmp(Rw[i].duty, Rw[i - 1].duty) <= 0) eaRefuse('Rows, record ' + (i + 1) + ': the duty ' + wtxMoney(Rw[i].duty, o) + ' is not above the one before it, ' + wtxMoney(Rw[i - 1].duty, o) + '; list the duties from lowest to highest');
    }
    var rev = Rw.map(function (r) { return Rmul(r.duty, r.quantity); }), best = 0, falls = [];
    rev.forEach(function (v, j) {
      if (Rcmp(v, rev[best]) > 0) best = j;
      if (j > 0 && Rcmp(v, rev[j - 1]) < 0) falls.push(wtxMoney(Rw[j].duty, o) + ' yields ' + wtxMoney(v, o) + ', less than the ' + wtxMoney(rev[j - 1], o) + ' at ' + wtxMoney(Rw[j - 1].duty, o));
    });
    var ties = rev.map(function (v, j) { return j; }).filter(function (j) { return j !== best && Requ(rev[j], rev[best]); });
    var last = rev.length - 1;
    return {
      tiles: { wtxRevenues: Rw.map(function (r, j) { return wtxMoney(r.duty, o) + ': ' + wtxMoney(rev[j], o); }).join('; '),
        wtxBest: wtxMoney(Rw[best].duty, o) + ', yielding ' + wtxMoney(rev[best], o) + (ties.length ? ' (as much at ' + ties.map(function (j) { return wtxMoney(Rw[j].duty, o); }).join(', ') + ')' : ''),
        wtxFalls: aktListed(falls.length, falls, '; '),
        wtxEnds: Rzero(Rw[0].duty) ? 'the lowest duty is nothing: revenue from ' + wtxMoney(rev[0], o) + ' to ' + wtxMoney(rev[last], o)
          : 'duty ' + wtxPlain(Rdiv(Rw[last].duty, Rw[0].duty)) + '× the lowest, revenue ' + (Rzero(rev[0]) ? 'from nothing to ' + wtxMoney(rev[last], o) : wtxPlain(Rdiv(rev[last], rev[0])) + '× the lowest’s') },
      status: wnkStatus('Of the duties listed, ' + wtxMoney(Rw[best].duty, o) + ' yields the most, ' + wtxMoney(rev[best], o) + '; '
        + (falls.length ? eaPlural(falls.length, 'higher duty yields', 'higher duties yield') + ' less than the duty below, Swift’s two and two making one' : 'no higher duty yields less than the one below')
        + '; the quantities at each duty are the lesson’s'),
      table: { caption: 'Each duty, the quantity that pays it and the revenue', head: ['duty', 'quantity', 'revenue'],
        rows: Rw.map(function (r, j) { return [wtxMoney(r.duty, o), wtxQty(r.quantity, o.qty), wtxMoney(rev[j], o)]; }) }
    };
  };
"""

WTX_VIEW_JS["land"] = r"""
  WTX_VIEW.land = function (inst, o) {
    var Y = inst.rents, t = wtxOf(inst.rate), i;
    for (i = 1; i < Y.length; i += 1) {
      if (Rcmp(Y[i].year, Y[i - 1].year) <= 0) eaRefuse('Rents, record ' + (i + 1) + ': the year ' + String(Y[i].year.n) + ' is not after the one before it, ' + String(Y[i - 1].year.n));
    }
    var fixedTax = Rmul(inst.valuation, t), follow = Y.map(function (y) { return Rmul(y.rent, t); });
    var n = R(BigInt(Y.length)), totFixed = Rmul(fixedTax, n), totFollow = eaSum(follow), diff = Rsub(totFollow, totFixed);
    var yr = function (y) { return String(y.year.n); };
    return {
      tiles: { wtxTax: wtxMoney(fixedTax, o) + ' every year',
        wtxShares: Y.map(function (y) { return yr(y) + ' ' + wtxPc(Rdiv(fixedTax, y.rent)); }).join('; '),
        wtxFollow: Y.map(function (y, j) { return yr(y) + ' ' + wtxMoney(follow[j], o); }).join('; '),
        wtxTotals: 'fixed ' + wtxMoney(totFixed, o) + ', on the actual rent ' + wtxMoney(totFollow, o) + ', over ' + eaPlural(Y.length, 'year', 'years'),
        wtxDifference: Rzero(diff) ? 'none: the two raise the same' : wtxSigned(diff, o) + (diff.n > 0n ? ': the tax on the actual rent raises more' : ': the tax on the actual rent raises less') },
      status: wnkStatus('A tax of ' + wtxPc(t) + ' on a fixed valuation of ' + wtxMoney(inst.valuation, o) + ' takes ' + wtxPc(Rdiv(fixedTax, Y[0].rent)) + ' of the rent in '
        + yr(Y[0]) + ' and ' + wtxPc(Rdiv(fixedTax, Y[Y.length - 1].rent)) + ' in ' + yr(Y[Y.length - 1]) + '; the same rate on the actual rent would take ' + wtxPc(t) + ' in every year'),
      table: { caption: 'Each year: the rent, the tax on the valuation and the tax on the rent', head: ['year', 'rent', 'tax on the valuation', 'share of the rent', 'tax on the rent'],
        rows: Y.map(function (y, j) { return [yr(y), wtxMoney(y.rent, o), wtxMoney(fixedTax, o), wtxPc(Rdiv(fixedTax, y.rent)), wtxMoney(follow[j], o)]; }) }
    };
  };
"""


def _check_incidence(inst, fixed):
    if inst["rate"] == 100:
        raise ValueError("A tax of 100% of the wage takes all of it, and no wage could leave the worker anything")


def _check_arithmetic(inst, fixed):
    rows = inst["rows"]
    for i in range(1, len(rows)):
        if rows[i]["duty"] <= rows[i - 1]["duty"]:
            raise ValueError("Rows, record %d: the duty %s is not above the one before it, %s; list the duties from "
                             "lowest to highest" % (i + 1, _money(rows[i]["duty"], fixed),
                                                    _money(rows[i - 1]["duty"], fixed)))


def _check_land(inst, fixed):
    ys = inst["rents"]
    for i in range(1, len(ys)):
        if ys[i]["year"] <= ys[i - 1]["year"]:
            raise ValueError("Rents, record %d: the year %s is not after the one before it, %s"
                             % (i + 1, int(ys[i]["year"]), int(ys[i - 1]["year"])))


TAX = {
    "prefix": "wtx", "fn": "wtxCompute", "title": "Taxes", "js": _shared("wtx") + WTX_JS,
    "views": {
        "incidence": {
            "fields": [("wage", ea.field("The wage before the tax, in %u", _MP), None),
                       ("rate", ea.field("The tax, % of the wage (20 for one fifth)", rat(gt=0, hi=100)), None)],
            "tiles": [("Wage that leaves the same subsistence", "wtxWage"), ("Rise in the wage", "wtxRise"),
                      ("Tax paid", "wtxTax"), ("The rise against the rate", "wtxOver"),
                      ("Who advances the tax", "wtxAdvances")],
            "check": _check_incidence, "options": _options(),
            "subtitle": "a direct tax on wages, which raises them by more than the tax",
            "rules": "Smith's rule (Book V, chapter 2, article III): while the demand for labour and the price of "
                     "provisions stay the same, the worker must keep the same wage after the tax, so the wage "
                     "becomes wage ÷ (1 − rate); the rise is rate ÷ (1 − rate), more than the rate (a fifth raises "
                     "it a fourth, a tenth an eighth). The tax paid is the rate of the new wage, and it is advanced "
                     "by the employer; who finally pays is not computed. A tax of 100% is refused. " + _MONEY_RULE
                     + _PCT_RULE,
            "js": WTX_VIEW_JS["incidence"],
        },
        "arithmetic": {
            "fields": [("rows", _recs("Duties, lowest first (duty a unit in %u, %q that pay it at that duty)",
                                      [("duty", _M), ("quantity", _M)], lo=2, unique=False), None)],
            "tiles": [("Revenue at each duty", "wtxRevenues"), ("The duty that yields most", "wtxBest"),
                      ("Higher duties that yield less", "wtxFalls"), ("Highest duty against lowest", "wtxEnds")],
            "check": _check_arithmetic, "options": _options("qty_unit"),
            "subtitle": "revenue against the rate of a duty: when two and two make one",
            "rules": "Revenue = duty × the quantity that pays it, each row. The quantity at each duty is the "
                     "lesson's, written for it: the lab does not derive it. The duty that yields most is the "
                     "lowest such duty when two yield the same (the lab's rule), and the others are named. A row "
                     "yields less when its revenue is below the row before. The last tile gives the highest duty "
                     "and its revenue as multiples of the lowest's. Duties must be listed from lowest to highest. "
                     + _MONEY_RULE,
            "js": WTX_VIEW_JS["arithmetic"],
        },
        "land": {
            "fields": [("valuation", ea.field("The fixed valuation (assessed rent), in %u", _MP), None),
                       ("rate", ea.field("The tax, % of the valuation", rat(gt=0, hi=100)), None),
                       ("rents", _recs("Actual rents (year, rent in %u), earliest first",
                                       [("year", ea.whole(0, 9999)), ("rent", _MP)], unique=False), None)],
            "tiles": [("Tax on the valuation", "wtxTax"), ("As a share of the actual rent", "wtxShares"),
                      ("The same rate on the actual rent", "wtxFollow"), ("Totals over the years", "wtxTotals"),
                      ("On the rent against on the valuation", "wtxDifference")],
            "check": _check_land, "options": _options(),
            "subtitle": "a land tax on a fixed valuation against one that follows the rent",
            "rules": "Tax on the valuation = valuation × rate, the same every year, as England's land tax on its "
                     "fixed valuation (Book V, chapter 2); as a share of each year's actual rent it is that tax ÷ "
                     "the rent. A tax at the same rate on the actual rent is rent × rate. The totals add the years "
                     "listed, and the difference is the tax on the rent less the tax on the valuation. Years must "
                     "be listed earliest first; the lab does not fill in years between them. " + _MONEY_RULE
                     + _PCT_RULE,
            "js": WTX_VIEW_JS["land"],
        },
    },
}

# ---------------------------------------------------------------------------
# debt (wdb): Book V, chapter 3
# ---------------------------------------------------------------------------

WDB_JS = r"""
  var WDB_VIEW = {};
  function wdbCompute(view, inst, opts) { return eaRun(WDB_VIEW[view], inst, opts); }
"""

WDB_VIEW_JS = {}

WDB_VIEW_JS["sinking"] = r"""
  WDB_VIEW.sinking = function (inst, o) {
    var n = Number(inst.years.n), i = wdbOf(inst.interest), P = inst.payment, B = {}, seen = {};
    inst.borrow.forEach(function (b, j) {
      var y = Number(b.year.n);
      if (y > n) eaRefuse('Borrow, record ' + (j + 1) + ': year ' + y + ' is beyond the ' + eaPlural(n, 'year', 'years') + ' computed');
      if (seen[y]) eaRefuse('Borrow names year ' + y + ' twice');
      seen[y] = true; B[y] = b.amount;
    });
    var first = Rmul(inst.debt, i);
    if (Rcmp(P, first) < 0) eaRefuse('A payment of ' + wdbMoney(P, o) + ' a year is less than the interest of the first year, ' + wdbMoney(first, o) + ', so the debt grows every year');
    var D = inst.debt, intTot = R0, paidTot = R0, borTot = R0, off = null, rows = [], t;
    for (t = 1; t <= n; t += 1) {
      var start = D, I = Rmul(D, i), pay;
      if (Rzero(D)) { I = R0; pay = R0; }
      else if (Rcmp(P, Radd(D, I)) >= 0) { pay = Radd(D, I); D = R0; }
      else { pay = P; D = Rsub(Radd(D, I), P); }
      var bor = B[t] || R0;
      D = Radd(D, bor);
      intTot = Radd(intTot, I); paidTot = Radd(paidTot, pay); borTot = Radd(borTot, bor);
      if (Rzero(D)) { if (off === null) off = t; } else off = null;
      rows.push([String(t), wdbMoney2(start, o), wdbMoney2(I, o), wdbMoney2(pay, o), Rzero(bor) ? '' : wdbMoney(bor, o), wdbMoney2(D, o)]);
    }
    var yrs = eaPlural(n, 'year', 'years');
    return {
      tiles: { wdbFirst: wdbMoney(first, o),
        wdbOff: n === 0 ? 'no years computed' : (off === null ? 'not paid off within ' + yrs : 'in year ' + off),
        wdbEnd: wdbMoney2(D, o) + ' after ' + yrs, wdbInterest: wdbMoney2(intTot, o), wdbPaid: wdbMoney2(paidTot, o),
        wdbBorrowed: wdbMoney(borTot, o) },
      status: wnkStatus('A debt of ' + wdbMoney(inst.debt, o) + ' at ' + wdbPc(i) + ', paid ' + wdbMoney(P, o) + ' a year'
        + (Rzero(borTot) ? '' : ' with ' + wdbMoney(borTot, o) + ' borrowed again') + ', is '
        + (n === 0 ? 'not followed over any years' : (off === null ? 'not paid off within ' + yrs + ': ' + wdbMoney2(D, o) + ' is left' : 'paid off in year ' + off + ', after ' + wdbMoney2(intTot, o) + ' of interest'))),
      table: { caption: 'Each year: the debt, its interest, the payment, new loans and the debt at the end', head: ['year', 'debt at the start', 'interest', 'paid', 'borrowed', 'debt at the end'], rows: rows }
    };
  };
"""

WDB_VIEW_JS["debase"] = r"""
  WDB_VIEW.debase = function (inst, o) {
    var d = inst.debt, a = inst.old, b = inst['new'];
    if (Rcmp(b, a) > 0) eaRefuse('The coin after holds more silver, ' + wdbQty(b, o.silver) + ', than before, ' + wdbQty(a, o.silver) + '; raising the denomination lowers the silver in a unit');
    var owed = Rmul(d, a), paid = Rmul(d, b), lost = Rsub(owed, paid), worth = Rdiv(Rmul(d, b), a);
    return {
      tiles: { wdbOwed: wdbQty(owed, o.silver), wdbSilver: wdbQty(paid, o.silver),
        wdbLoss: wdbPc(Rdiv(lost, owed)) + ' (' + wdbQty(lost, o.silver) + ')',
        wdbPretended: wdbMoney(d, o) + ' paid in name, worth ' + wdbMoney(worth, o) + ' in the old coin' },
      status: wnkStatus('Paid in the new coin, a debt of ' + wdbMoney(d, o) + ' returns ' + wdbQty(paid, o.silver) + ' of the ' + wdbQty(owed, o.silver) + ' owed: the creditor loses '
        + wdbPc(Rdiv(lost, owed)) + ' under the name of a full payment'),
      table: { caption: 'The debt in coin and in silver', head: ['', 'silver in a unit of coin', 'silver'],
        rows: [['owed (the old coin)', wdbQty(a, o.silver), wdbQty(owed, o.silver)], ['paid (the new coin)', wdbQty(b, o.silver), wdbQty(paid, o.silver)], ['lost by the creditor', '', wdbQty(lost, o.silver)]] }
    };
  };
"""


def _check_sinking(inst, fixed):
    n, seen = int(inst["years"]), set()
    for j, b in enumerate(inst["borrow"]):
        y = int(b["year"])
        if y > n:
            raise ValueError("Borrow, record %d: year %d is beyond the %s computed"
                             % (j + 1, y, "%s %s" % (ea.grp(n), "year" if n == 1 else "years")))
        if y in seen:
            raise ValueError("Borrow names year %d twice" % y)
        seen.add(y)
    first = inst["debt"] * inst["interest"] / 100
    if inst["payment"] < first:
        raise ValueError("A payment of %s a year is less than the interest of the first year, %s, so the debt grows "
                         "every year" % (_money(inst["payment"], fixed), _money(first, fixed)))


def _check_debase(inst, fixed):
    if inst["new"] > inst["old"]:
        raise ValueError("The coin after holds more silver, %s, than before, %s; raising the denomination lowers the "
                         "silver in a unit" % (_qty(inst["new"], fixed["silver"]), _qty(inst["old"], fixed["silver"])))


DEBT = {
    "prefix": "wdb", "fn": "wdbCompute", "title": "Public debts", "js": _shared("wdb") + WDB_JS,
    "views": {
        "sinking": {
            "fields": [("debt", ea.field("The debt, in %u", _MP), None),
                       ("interest", ea.field("Interest, % a year", _PCT), None),
                       ("payment", ea.field("Paid each year, interest first, in %u", _M), None),
                       ("years", ea.field("Years (0 to 200)", ea.whole(0, 200)), None),
                       ("borrow", _recs("New loans (year, amount in %u); empty for none",
                                        [("year", ea.whole(1, 200)), ("amount", _MP)], lo=0, unique=False, rows=2),
                        "")],
            "tiles": [("Interest of the first year", "wdbFirst"), ("Paid off", "wdbOff"),
                      ("Debt at the end", "wdbEnd"), ("Interest paid", "wdbInterest"), ("Paid in all", "wdbPaid"),
                      ("Borrowed again", "wdbBorrowed")],
            "check": _check_sinking, "options": _options(),
            "subtitle": "a public debt with interest and a yearly payment, year by year",
            "rules": "Each year the debt bears interest at the rate; the payment goes to the interest first and the "
                     "rest to the debt. When the payment covers the debt and its interest, only that much is paid "
                     "and the debt is 0; a year with no debt bears no interest and takes no payment (the lab's "
                     "rules). A new loan is added at the end of its year. Paid off is the first year from which the "
                     "debt stays at 0 to the end of the years computed. Every figure is exact; long ones are shown "
                     "to 2 places by an exact rounding, marked ≈. A payment below the first year's interest is "
                     "refused (the debt would grow every year), and so is a loan outside the years or two in one "
                     "year. " + _MONEY_RULE,
            "js": WDB_VIEW_JS["sinking"],
        },
        "debase": {
            "fields": [("debt", ea.field("The debt, in %u (its name, in units of coin)", _MP), None),
                       ("old", ea.field("Silver in a unit of coin before, %s", rat(gt=0, hi=_BIG)), None),
                       ("new", ea.field("Silver in a unit of coin after the denomination is raised, %s",
                                        rat(gt=0, hi=_BIG)), None)],
            "tiles": [("Silver owed", "wdbOwed"), ("Silver paid", "wdbSilver"), ("Lost by the creditor", "wdbLoss"),
                      ("The pretended payment", "wdbPretended")],
            "check": _check_debase, "options": _options("silver_unit"),
            "subtitle": "a debt repaid in a coin whose denomination has been raised",
            "rules": "The debt is owed in coin of the old standard and paid, unit for unit, in the new. Silver owed "
                     "= debt × silver in the old unit; silver paid = debt × silver in the new; the creditor loses "
                     "the difference, as a share of what was owed 1 − new ÷ old. In the old coin the payment is "
                     "worth debt × new ÷ old. Smith calls it a pretended payment (Book V, chapter 3). A new coin "
                     "with more silver than the old is refused. " + _MONEY_RULE + _PCT_RULE,
            "js": WDB_VIEW_JS["debase"],
        },
    },
}

# ---------------------------------------------------------------------------
# public (wpb): Book V, chapter 1
# ---------------------------------------------------------------------------

WPB_JS = r"""
  var WPB_VIEW = {};
  function wpbCompute(view, inst, opts) { return eaRun(WPB_VIEW[view], inst, opts); }
"""

WPB_VIEW_JS = {}

WPB_VIEW_JS["soldiers"] = r"""
  WPB_VIEW.soldiers = function (inst, o) {
    var pop = inst.population, s = inst.share, men = Rmul(pop, s), c = inst.cost, others = Rdiv(Rsub(R1, s), s);
    var cost = c === '-' ? null : Rmul(men, c);
    return {
      tiles: { wpbSoldiers: wpbPlain(men) + (Rint(men) ? '' : ' (' + eaInt(eaFloor(men)) + ' whole soldiers)'),
        wpbOthers: wpbPlain(others),
        wpbCost: cost ? wpbMoney(cost, o) + ' a year' : 'no cost given',
        wpbPerHead: cost ? wpbMoney(Rdiv(cost, pop), o) + ' a head a year' : 'no cost given' },
      status: wnkStatus('With ' + (Rint(s) ? eaInt(s.n) : eaFrac(s)) + ' of ' + eaInt(pop.n) + ' people under arms, ' + wpbPlain(men) + ' are soldiers and each is maintained by the labour of '
        + wpbPlain(others) + ' others' + (cost ? ', at ' + wpbMoney(cost, o) + ' a year' : '')),
      table: null
    };
  };
"""

WPB_VIEW_JS["fees"] = r"""
  WPB_VIEW.fees = function (inst, o) {
    var P = inst.people.map(function (p) {
      var fees = Rmul(p.pupils, p.fee), all = Radd(p.salary, fees);
      return { name: p.person, salary: p.salary, n: p.pupils, fee: p.fee, fees: fees, all: all, share: Rzero(all) ? null : Rdiv(fees, all) };
    });
    var has = P.filter(function (p) { return p.share !== null; }), top = null;
    has.forEach(function (p) { if (top === null || Rcmp(p.share, top) > 0) top = p.share; });
    var most = top === null ? [] : has.filter(function (p) { return Requ(p.share, top); }).map(function (p) { return p.name; });
    var one = wpbOne(o.pupils);
    return {
      tiles: { wpbFees: P.map(function (p) { return p.name + ' ' + wpbMoney(p.fees, o); }).join('; '),
        wpbIncome: P.map(function (p) { return p.name + ' ' + wpbMoney(p.all, o); }).join('; '),
        wpbShare: P.map(function (p) { return p.name + ' ' + (p.share === null ? 'no income' : wpbPc(p.share)); }).join('; '),
        wpbMore: P.map(function (p) { return p.name + ' ' + wpbSigned(p.fee, o); }).join('; '),
        wpbMost: top === null ? 'no one has an income' : most.join(', ') + ' (' + wpbPc(top) + ' from fees)' },
      status: wnkStatus(top === null ? 'No one listed has an income, from fees or salary'
        : most.join(', ') + ' ' + (most.length === 1 ? 'takes' : 'take') + ' the largest share of income from fees, ' + wpbPc(top) + ', and so depends most on the ' + o.pupils + ' it draws; a salary is paid whatever the diligence'),
      table: { caption: 'Each person: salary, ' + o.pupils + ', fees and the share of income from fees', head: ['person', 'salary', o.pupils, 'fee from each', 'fees', 'income', 'from fees'],
        rows: P.map(function (p) { return [p.name, wpbMoney(p.salary, o), eaInt(p.n.n), wpbMoney(p.fee, o), wpbMoney(p.fees, o), wpbMoney(p.all, o), p.share === null ? 'no income' : wpbPc(p.share)]; }) }
    };
  };
"""

WPB_VIEW_JS["tolls"] = r"""
  WPB_VIEW.tolls = function (inst, o) {
    var C = inst.carriages.map(function (c) { var tons = Rmul(c.weight, c.trips); return { name: c.carriage, w: c.weight, trips: c.trips, tons: tons, toll: Rmul(tons, inst.toll) }; });
    var total = eaSum(C.map(function (c) { return c.toll; })), tons = eaSum(C.map(function (c) { return c.tons; })), heavy = C[0];
    C.forEach(function (c) { if (Rcmp(c.w, heavy.w) > 0) heavy = c; });
    return {
      tiles: { wpbTolls: C.map(function (c) { return c.name + ' ' + wpbMoney(c.toll, o); }).join('; '), wpbTotal: wpbMoney(total, o) + ' a year',
        wpbHeaviest: heavy.name + ' ' + wpbMoney(heavy.toll, o) + (Rzero(total) ? ', and no toll is paid' : ' (' + wpbPc(Rdiv(heavy.toll, total)) + ' of the total)'),
        wpbTons: wpbQty(tons, 'tons'),
        wpbPerTon: Rzero(tons) ? 'nothing is carried' : wpbMoney(Rdiv(total, tons), o) + ' a ton' },
      status: wnkStatus('A toll of ' + wpbMoney(inst.toll, o) + ' a ton a trip raises ' + wpbMoney(total, o) + ' a year, each carriage paying in proportion to the weight it carries and the trips it makes'),
      table: { caption: 'Each carriage: weight, trips, tons carried and toll', head: ['carriage', 'tons', 'trips a year', 'tons carried', 'toll'],
        rows: C.map(function (c) { return [c.name, wpbPlain(c.w), eaInt(c.trips.n), wpbPlain(c.tons), wpbMoney(c.toll, o)]; }) }
    };
  };
"""

PUBLIC = {
    "prefix": "wpb", "fn": "wpbCompute", "title": "The expenses of the sovereign", "js": _shared("wpb") + WPB_JS,
    "views": {
        "soldiers": {
            "fields": [("population", ea.field("Population", ea.whole(1, _BIG)), None),
                       ("share", ea.field("Share under arms, a fraction such as 1/100", rat(gt=0, hi=1)), None),
                       ("cost", ea.field("A soldier's cost a year, in %u (- for none)", _MD), "-")],
            "tiles": [("Soldiers", "wpbSoldiers"), ("Others at work for each soldier", "wpbOthers"),
                      ("Cost a year", "wpbCost"), ("Cost per head of the population", "wpbPerHead")],
            "check": None, "options": _options(),
            "subtitle": "the soldiers a population can support",
            "rules": "Soldiers = population × the share under arms, exact (a fraction of a person is printed as it "
                     "is, with the whole soldiers in it); others at work for each soldier = (1 − share) ÷ share. "
                     "Cost a year = soldiers × a soldier's cost, and per head of the population = that ÷ the "
                     "population. The share is the lesson's: Smith's estimate is that \"not more than the one "
                     "hundredth part of the inhabitants\" of a civilized country can be soldiers (Book V, chapter "
                     "1). " + _MONEY_RULE,
            "js": WPB_VIEW_JS["soldiers"],
        },
        "fees": {
            "fields": [("people", _recs("People (person, salary a year in %u, %w a year, fee from each in %u)",
                                        [("person", _N), ("salary", _M), ("pupils", ea.whole(0, ea.LIMIT)),
                                         ("fee", _M)]), None)],
            "tiles": [("Income from fees", "wpbFees"), ("Income in all", "wpbIncome"),
                      ("Share of income from fees", "wpbShare"), ("Added by one more of the %w", "wpbMore"),
                      ("Depends most on diligence", "wpbMost")],
            "check": None, "options": _options("pupil_word"),
            "subtitle": "a teacher's or a judge's income by fees and by salary",
            "rules": "Fees = the number who pay × the fee from each; income = salary + fees; the share from fees = "
                     "fees ÷ income (\"no income\" when it is 0). One more who pays adds the fee. The person who "
                     "depends most on diligence is the one with the largest share from fees, all of them when "
                     "several are equal: that a share from fees measures the spur to diligence is Smith's argument "
                     "(Book V, chapter 1, parts II and III), not a measurement. " + _MONEY_RULE + _PCT_RULE,
            "js": WPB_VIEW_JS["fees"],
        },
        "tolls": {
            "fields": [("carriages", _recs("Carriages (carriage, tons it carries, trips a year)",
                                           [("carriage", _N), ("weight", _MP), ("trips", ea.whole(0, ea.LIMIT))]),
                        None),
                       ("toll", ea.field("Toll a ton a trip, in %u", _M), None)],
            "tiles": [("Toll each pays a year", "wpbTolls"), ("All the tolls", "wpbTotal"),
                      ("The heaviest carriage", "wpbHeaviest"), ("Tons carried a year", "wpbTons"),
                      ("Toll a ton carried", "wpbPerTon")],
            "check": None, "options": _options(),
            "subtitle": "tolls by weight, paid by those who use the road",
            "rules": "Each carriage pays tons × trips × the toll a ton; the total adds them, and the toll a ton "
                     "carried is the total ÷ the tons carried. The heaviest is the carriage carrying most tons on a "
                     "trip, the first given when two are equal (the lab's rule). That a toll by weight makes those "
                     "who wear the road most pay most is Smith's (Book V, chapter 1, part III). " + _MONEY_RULE
                     + _PCT_RULE,
            "js": WPB_VIEW_JS["tolls"],
        },
    },
}

# ---------------------------------------------------------------------------
# system (wsy): Book IV, chapter 9
# ---------------------------------------------------------------------------

WSY_JS = r"""
  var WSY_VIEW = {};
  function wsyCompute(view, inst, opts) { return eaRun(WSY_VIEW[view], inst, opts); }
"""

WSY_VIEW_JS = {}

WSY_VIEW_JS["classes"] = r"""
  WSY_VIEW.classes = function (inst, o) {
    var C = inst.classes.map(function (c) { return { name: c['class'], p: c.produce, c: c.consumption, a: c.advances, net: Rsub(c.produce, Radd(c.consumption, c.advances)) }; });
    var pick = function (s) { return C.filter(function (c) { return Rsign(c.net) === s; }).map(function (c) { return c.name; }); };
    var plus = pick(1), zero = pick(0), minus = pick(-1), total = eaSum(C.map(function (c) { return c.net; }));
    return {
      tiles: { wsyNet: C.map(function (c) { return c.name + ' ' + wsySigned(c.net, o); }).join('; '),
        wsyProductive: aktListed(plus.length, plus), wsyBarren: aktListed(zero.length, zero),
        wsyShort: aktListed(minus.length, minus), wsyTotal: wsySigned(total, o) },
      status: wnkStatus('Under the figures stated, ' + (plus.length ? plus.join(', ') + ' ' + (plus.length === 1 ? 'shows' : 'show') + ' a net product' : 'no class shows a net product')
        + (zero.length ? ', and ' + zero.join(', ') + ' ' + (zero.length === 1 ? 'produces' : 'produce') + ' just what ' + (zero.length === 1 ? 'it consumes and advances, what the table calls barren' : 'they consume and advance, what the table calls barren') : '')
        + '; the figures are the table’s assumption, not a measurement'),
      table: { caption: 'Each class: produce, consumption, advances and net product', head: ['class', 'produce', 'consumption', 'advances', 'net product'],
        rows: C.map(function (c) { return [c.name, wsyMoney(c.p, o), wsyMoney(c.c, o), wsyMoney(c.a, o), wsySigned(c.net, o)]; }) }
    };
  };
"""

SYSTEM = {
    "prefix": "wsy", "fn": "wsyCompute", "title": "The agricultural system", "js": _shared("wsy") + WSY_JS,
    "views": {
        "classes": {
            "fields": [("classes", _recs("Classes (class, produce, consumption, advances; in %u)",
                                         [("class", _N), ("produce", _M), ("consumption", _M), ("advances", _M)],
                                         lo=2), None)],
            "tiles": [("Net product of each class", "wsyNet"), ("Classes with a net product", "wsyProductive"),
                      ("Classes with none (barren under these figures)", "wsyBarren"),
                      ("Classes producing less than they use", "wsyShort"), ("Net product of the whole table", "wsyTotal")],
            "check": None, "options": _options(),
            "subtitle": "which class, in a stated table, shows a produce beyond its consumption and advances",
            "rules": "Net product = produce − consumption − advances, for each class; the classes are sorted into "
                     "those with a net product (above 0), those with none (exactly 0, what the économistes call "
                     "barren) and those below 0, each in the order given. The figures are the table's assumption, "
                     "the lesson's, not a measurement: Smith's objection (Book IV, chapter 9) is that the table's "
                     "artificers and merchants are not barren because they replace what they consume. "
                     + _MONEY_RULE,
            "js": WSY_VIEW_JS["classes"],
        },
    },
}

SPECS = {"stock": STOCK, "bank": BANK, "trade": TRADE, "tax": TAX, "debt": DEBT, "public": PUBLIC, "system": SYSTEM}

MODES = {"stock": _builder("stock", STOCK),
         "bank": _builder("bank", BANK),
         "trade": _builder("trade", TRADE),
         "tax": _builder("tax", TAX),
         "debt": _builder("debt", DEBT),
         "public": _builder("public", PUBLIC),
         "system": _builder("system", SYSTEM)}

__all__ = ["MODES", "SPECS", "WNB_SHARED_JS"]
