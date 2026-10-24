"""capkit -- the Capital kit, Volume I modes, and the kit's entry point.

Specified in docs/capital/PLAN.md section D (D.0 conventions, D.1 modes),
which adopts docs/philosophy/PLAN.md section D.0. Nine modes live here:

  value       socially necessary labour-time, a lot's value, a ledger of
              hours, the market value of groups producing under different
              conditions
  form        the elementary, expanded, general and money forms of one set
              of labour-values; the count of ratios barter needs
  money       prices in gold and the money needed in circulation, payments
              netted, the drain abroad, a fixed money rent, the Bank Act cap
  circuit     C-M-C against M-C-M', mark-ups that add nothing to the sum of
              values, the daily value of labour-power, the stages of the
              circuit, the home market, costs of circulation, realisation
  surplus     the spinning mill, value transferred, s/v, the product in parts,
              Senior's last hour, the mass of s, s/(v + s)
  workday     necessary and surplus labour on one day, with a bar drawing it
  machine     co-operation, detail labour, adopting a machine, displacement
  wages       the price of labour, time-wages, piece-wages, national
              differences, a statutory maximum
  accumulate  simple reproduction, accumulation period by period, demand for
              labour and the reserve army, centralisation, the colony, thrift

The other eight (turnover, schemes, profit, prices, tendency, interest, rent,
revenue) are capkit_b.py's; capkit_lab() dispatches to it, importing it only
when one of those modes is asked for.

Shared machinery -- the money formatter, the percentage formatter, parsing,
the preset menu, the wiring -- is capkit_core.py. Each mode here is a table
of fields, a table of views (which fields and tiles a view shows) and one
pure JS function  <xx>Compute(view, inst, U, opts)  that scripts/mathcheck.js
calls directly (section "capkit (Volume I modes)").

VIEW IS NOT A CONTROL. cfg["view"] fixes which inputs and tiles the page
shows; an unknown view raises. Redraw-only selects ship from cfg["stage"]
(form/stage), cfg["hold"] (workday/three) and cfg["test"] (machine/adopt).

IDS. Every tile id below is unique within the kit. Grepped against
scripts/mathpath/labs/*.py on 2026-10-24: no module-level JS name of any kit
collides with a capkit function or tile. The element ids acRatio (estimate),
vaPreset/vaStatus/vaTable (argkit, queue), foPreset/foStatus/foTable
(algebra_functions, latency), suPreset/suStatus (strings), maPreset/maStatus
(algebra_systems, markov), waPreset/waStatus (scale), acPreset/acStatus/
acTable (estimate) are element ids on other kits' pages; one page carries one
lab, so they never meet.

EXACT. Every printed figure is a rational over BigInt (RATIONAL_JS). The one
non-exact figure is the percentage printed beside its exact fraction
("19/23 = 82.61%"). The workday bar's pixel widths are BigInt divisions.
"""

import re
from fractions import Fraction

from . import capkit_core as cc

KIT = "capkit"

# ---------------------------------------------------------------------------
# value
# ---------------------------------------------------------------------------

VALUE_JS = r"""
  /* value: socially necessary labour-time as the average over all producers
     (this lab's model of "normal conditions"), and a lot valued at it. */
  function vaTotalOf(p, basis) { return basis === 'per-unit' ? Rmul(p.hours, p.output) : p.hours; }
  function vaSnltOf(producers, basis) {
    var T = R0, O = R0;
    producers.forEach(function (p) { T = Radd(T, vaTotalOf(p, basis)); O = Radd(O, p.output); });
    return { hours: T, output: O, snlt: Rdiv(T, O) };
  }
  function vaMarketValueOf(groups) {
    var T = R0, N = R0;
    groups.forEach(function (g) { T = Radd(T, Rmul(g.units, g.hours)); N = Radd(N, g.units); });
    return Rdiv(T, N);
  }
  function vaCompute(view, inst, U) {
    var unit = 'unit';
    if (view === 'snlt' || view === 'skill') {
      var s = vaSnltOf(inst.producers, inst.basis);
      var skill = view === 'skill' ? inst.skill : R1, per = Rmul(s.snlt, skill), lot = Rmul(inst.lot, per);
      var rows = inst.producers.map(function (p) {
        var total = vaTotalOf(p, inst.basis), own = Rdiv(total, p.output);
        return [p.name, capQty(p.output, U.qty), capHours(total), capHours(own), capSigned(Rsub(own, s.snlt), capHours)];
      });
      var tiles = { vaSnlt: capHours(s.snlt), vaLotValue: capHours(lot), vaPerUnit: capHours(per) };
      var n = inst.producers.length;
      var said = (n === 1 ? 'One producer makes ' : n + ' producers make ') + capQty(s.output, U.qty) + ' with '
        + capHours(s.hours) + ' of labour in all, so the socially necessary labour-time is '
        + capNumText(s.hours) + ' / ' + capNumText(s.output) + ' = ' + capHours(s.snlt) + ' per ' + unit
        + ' (this lab takes the average over every producer as its model of normal conditions).';
      if (view === 'skill') {
        said += ' Counted as ' + capNumText(skill) + ' times simple labour, a unit is worth '
          + capHours(per) + ' of simple labour.';
      }
      said += ' A lot of ' + capQty(inst.lot, U.qty) + ' is worth ' + capHours(lot)
        + ', whoever made it and however long they took.';
      return { tiles: tiles, status: said, table: { caption: 'Each producer against the social average',
        head: ['producer', 'output', 'hours in all', 'own hours per ' + unit, 'own minus social'], rows: rows } };
    }
    if (view === 'ledger') {
      var total = capSum(inst.items.map(function (i) { return i.hours; }));
      var first = inst.items[0], firstPer = Rdiv(first.hours, first.output);
      var per = inst.items.map(function (i) { return Rdiv(i.hours, i.output); });
      return {
        tiles: { vaTotalHours: capHours(total),
                 vaPerUnit: inst.items.map(function (i, k) { return i.name + ' ' + capHours(per[k]); }).join(', ') },
        status: 'The ledger spends ' + capHours(total) + ' in all. Each product carries the hours spent on it '
          + 'divided by the units made, and those hours fix how much of one product equals one unit of '
          + first.name + '.',
        table: { caption: 'Hours behind each product', head: ['product', 'hours', 'units', 'hours per unit',
          'units of ' + first.name + ' it equals'],
          rows: inst.items.map(function (i, k) {
            return [i.name, capHours(i.hours), capNumText(i.output), capHours(per[k]), capNumText(Rdiv(per[k], firstPer))];
          }) }
      };
    }
    /* market */
    var mv = vaMarketValueOf(inst.groups);
    return {
      tiles: { vaMarketValue: capHours(mv),
               vaSurplus: inst.groups.map(function (g) { return capSigned(Rsub(mv, g.hours), capHours); }).join(', ') },
      status: 'The market value is the average over every unit sold, ' + capHours(mv) + ' per ' + unit
        + '. A group whose own value is below it gains the difference on each unit; one above it loses it.',
      table: { caption: 'Each group against the market value', head: ['group', 'units', 'own hours per ' + unit,
        'market value', 'gain per ' + unit],
        rows: inst.groups.map(function (g, k) {
          return [String(k + 1), capQty(g.units, U.qty), capHours(g.hours), capHours(mv), capSigned(Rsub(mv, g.hours), capHours)];
        }) }
    };
  }
"""

VALUE_FIELDS = {
    "producers": ("Producers: name, hours, output; one per entry, separated by ;",
                  ("rec", [("name", "name"), ("hours", "pos"), ("output", "pos")], 1, 8, True), None),
    "basis": ("Their hours are (per-unit or total)", ("word", ["per-unit", "total"]), "per-unit"),
    "skill": ("Skill: one hour counts as this many hours of simple labour", "pos", 1),
    "lot": ("Units in the lot valued", "pos", None),
    "items": ("Ledger: product, hours spent, units made; separated by ;",
              ("rec", [("name", "name"), ("hours", "pos"), ("output", "pos")], 1, 12, True), None),
    "groups": ("Groups: units sold, own hours per unit; separated by ;",
               ("rec", [("units", "pos"), ("hours", "pos")], 1, 8, False), None),
}

VALUE_VIEWS = {
    "snlt": dict(fields=["producers", "basis", "lot"],
                 tiles=[("Socially necessary hours per unit", "vaSnlt"), ("Value of the lot", "vaLotValue")]),
    "skill": dict(fields=["producers", "basis", "skill", "lot"],
                  tiles=[("Socially necessary hours per unit", "vaSnlt"), ("Value per unit", "vaPerUnit"),
                         ("Value of the lot", "vaLotValue")]),
    "ledger": dict(fields=["items"],
                   tiles=[("Hours in all", "vaTotalHours"), ("Hours per unit", "vaPerUnit")]),
    "market": dict(fields=["groups"],
                   tiles=[("Market value per unit", "vaMarketValue"), ("Gain per unit, by group", "vaSurplus")]),
}

# ---------------------------------------------------------------------------
# form
# ---------------------------------------------------------------------------

FORM_JS = r"""
  /* form: each good's lot carries its hours; a lot of a exchanges for
     b.qty * a.hours / b.hours of b, so every equation printed balances. */
  function foFetch(a, b) { return Rdiv(Rmul(b.qty, a.hours), b.hours); }
  /* More than one of a thing is plural: 2 coats, 2 quarters corn. The unit
     takes the plural when there is one (the name is then a mass noun: 20
     yards linen), else the name does. A word already ending in s, an
     abbreviation (lb, cwt) and a unit ending in "of" (head of cattle) stay as
     they are; "pair of boots" becomes "pairs of boots". A fraction up to 1 is
     singular: 1/2 ton iron. */
  var FO_ABBREV = ['lb', 'lbs', 'oz', 'cwt', 'qr', 'qrs', 'yd', 'yds', 'ft', 'kg', 'cm', 'mm', 'km', 'g', 'm'];
  function foPluralWord(w) {
    if (!w || /s$/i.test(w) || FO_ABBREV.indexOf(w.toLowerCase()) >= 0 || !/^[A-Za-z]+$/.test(w)) return w;
    if (/(ch|sh|x|z)$/i.test(w)) return w + 'es';
    if (/[^aeiou]y$/i.test(w)) return w.slice(0, -1) + 'ies';
    return w + 's';
  }
  function foPlural(phrase) {
    var words = phrase.split(' '), at = words.indexOf('of');
    if (at === words.length - 1) return phrase;
    var k = at > 0 ? at - 1 : words.length - 1;
    words[k] = foPluralWord(words[k]);
    return words.join(' ');
  }
  function foLotOf(g, q) {
    var many = Rcmp(q, R(1n)) > 0;
    return capNumText(q) + ' ' + (g.unit ? (many ? foPlural(g.unit) : g.unit) + ' ' + g.name
                                         : (many ? foPlural(g.name) : g.name));
  }
  function foFind(goods, name) {
    for (var i = 0; i < goods.length; i += 1) if (goods[i].name === name) return goods[i];
    return null;
  }
  function foEquations(goods, stage, e) {
    var a = goods[0];
    function eq(x, y) { return foLotOf(x, x.qty) + ' = ' + foLotOf(y, foFetch(x, y)); }
    if (stage === 'elementary') return [eq(a, goods[1])];
    if (stage === 'expanded') return goods.slice(1).map(function (b) { return eq(a, b); });
    return goods.filter(function (g) { return g !== e; }).map(function (g) { return eq(g, e); });
  }
  function foCompute(view, inst, U, opts) {
    var goods = inst.goods, n = BigInt(goods.length), e = foFind(goods, inst.equivalent);
    if (!e) return { refuse: 'The equivalent "' + inst.equivalent + '" is not one of the goods' };
    if (view === 'count') {
      var pairs = R(n * (n - 1n) / 2n), single = R(n - 1n);
      return { tiles: { foPairs: capNumText(pairs), foWithEquivalent: capNumText(single) },
        status: goods.length + ' owners trading each with each need ' + capNumText(pairs)
          + ' exchange ratios, one for every pair; once ' + e.name + ' is everyone\'s equivalent, '
          + capNumText(single) + ' ratios, one for each other commodity, say the same.', table: null };
    }
    var stage = opts.stage, eqs = foEquations(goods, stage, e), general = stage === 'general' || stage === 'money';
    var said = {
      elementary: 'The elementary form: ' + goods[0].name + ' is in the relative form, ' + goods[1].name
        + ' is the equivalent in which its value is expressed.',
      expanded: 'The expanded form: ' + goods[0].name + ' expresses its value in every other commodity in turn.',
      general: 'The general form: every other commodity expresses its value in ' + e.name + ', the general equivalent.',
      money: 'The money form: the same equations as the general form, with ' + e.name
        + ' in the equivalent\'s place as money.'
    }[stage];
    return {
      tiles: { foEquation: eqs.join('; '), foGeneral: general ? e.name + (stage === 'money' ? ' (as money)' : '') : 'none',
               foRelative: foLotOf(goods[1], foFetch(goods[0], goods[1])) },
      status: said + ' Each quantity is computed from the hours in each lot, so every equation balances in hours.',
      table: { caption: 'The hours in each lot', head: ['commodity', 'lot', 'hours in the lot', 'hours per unit'],
        rows: goods.map(function (g) {
          return [g.name, foLotOf(g, g.qty), capHours(g.hours), capHours(Rdiv(g.hours, g.qty))];
        }) }
    };
  }
"""

FORM_FIELDS = {
    "goods": ("Commodities: name, quantity, unit (may be empty), hours in that quantity; separated by ;",
              ("rec", [("name", "name"), ("qty", "pos"), ("unit", "label"), ("hours", "pos")], 2, 7, True), None),
    "equivalent": ("The general equivalent (one of the commodities)", "name", None),
}

FO_STAGES = [("elementary", "elementary form"), ("expanded", "expanded form"),
             ("general", "general form"), ("money", "money form")]

FORM_VIEWS = {
    "stage": dict(fields=["goods", "equivalent"],
                  tiles=[("The equations", "foEquation"), ("General equivalent", "foGeneral"),
                         ("The first lot fetches", "foRelative")],
                  redraw=[("stage", "foStage", "Form of value", FO_STAGES)]),
    "count": dict(fields=["goods", "equivalent"],
                  tiles=[("Ratios needed by barter", "foPairs"), ("Ratios with one equivalent", "foWithEquivalent")]),
}

_MARX_EQ = re.compile(r"^\s*([0-9./]+)\s+(.+?)\s*=\s*([0-9./]+)\s+(.+?)\s*$")


def _form_check(where, p):
    """Every equation in a preset's `marx` list must balance in hours."""
    if p.get("equivalent") not in [g.get("name") for g in p.get("goods") or []]:
        raise ValueError("%s: equivalent %r is not one of the goods" % (where, p.get("equivalent")))
    goods = {g["name"]: g for g in p["goods"]}
    for text in p.get("marx") or []:
        m = _MARX_EQ.match(str(text))
        if not m or m.group(2) not in goods or m.group(4) not in goods:
            raise ValueError("%s: marx equation %r should read '<qty> <good> = <qty> <good>' with goods "
                             "named in the preset" % (where, text))
        sides = []
        for qty, name in ((m.group(1), m.group(2)), (m.group(3), m.group(4))):
            g = goods[name]
            sides.append(cc.q(where, qty)[0] * cc.q(where, g["hours"])[0] / cc.q(where, g["qty"])[0])
        if sides[0] != sides[1]:
            raise ValueError("%s: marx equation %r does not balance in hours (%s against %s); the preset's "
                             "quantities are wrong" % (where, text, sides[0], sides[1]))


_form_check.extra = ("marx",)

# ---------------------------------------------------------------------------
# money
# ---------------------------------------------------------------------------

MONEY_JS = r"""
  /* money. moNeededOf is this kit's formalisation of Volume I, ch. 3,
     sections 2(b) and 3(b): (sum of prices - credit sales + payments due -
     payments that cancel) / velocity. */
  function moPricesOf(goods, goldHours) { return goods.map(function (g) { return Rdiv(g.value_hours, goldHours); }); }
  function moNeededOf(priceSum, credit, due, cancel, velocity) {
    return Rdiv(Radd(Rsub(priceSum, credit), Rsub(due, cancel)), velocity);
  }
  /* Net each party's bills (skipping the defaulted one); the cash needed is
     the sum of the positive balances. */
  function moNetOf(bills, skip) {
    var net = {}, order = [], gross = R0;
    function add(who, x) { if (!(who in net)) { net[who] = R0; order.push(who); } net[who] = Radd(net[who], x); }
    bills.forEach(function (b, i) {
      if (i === skip) return;
      gross = Radd(gross, b.amount); add(b.to, b.amount); add(b.from, Rneg(b.amount));
    });
    var cash = R0;
    order.forEach(function (w) { if (Rsign(net[w]) > 0) cash = Radd(cash, net[w]); });
    return { net: net, order: order, gross: gross, cash: cash };
  }
  function moDrainText(d, M) {
    if (Rsign(d) > 0) return M(d) + ' out';
    if (Rsign(d) < 0) return M(R0) + ' (' + M(Rneg(d)) + ' in)';
    return M(R0);
  }
  function moCompute(view, inst, U) {
    var M = function (x) { return capMoney(x, U.money); };
    var goodsTable = function (prices) {
      return { caption: 'Prices: value in hours over the hours in one unit of money', head: ['commodity', 'value', 'price'],
        rows: inst.goods.map(function (g, i) { return [g.name, capHours(g.value_hours), M(prices[i])]; }) };
    };
    if (view === 'circulate' || view === 'payments' || view === 'bank-act') {
      var prices = moPricesOf(inst.goods, inst.gold_hours_per_unit), sum = capSum(prices);
      var credit = view === 'payments' ? inst.credit_sales : R0, due = view === 'payments' ? inst.payments_due : R0;
      var cancel = view === 'payments' ? inst.cancelling : R0;
      var top = Radd(Rsub(sum, credit), Rsub(due, cancel));
      if (Rsign(top) < 0) {
        return { refuse: 'Credit sales and cancelling payments come to more than the prices and payments due, so the money needed would be negative' };
      }
      var needed = moNeededOf(sum, credit, due, cancel, inst.velocity);
      var tiles = { moPriceSum: M(sum), moNeeded: M(needed) };
      var said = 'The prices sum to ' + M(sum)
        + (view === 'payments' ? ', less ' + M(credit) + ' sold on credit, plus ' + M(due) + ' of payments due, less '
          + M(cancel) + ' of payments that cancel,' : '')
        + ' and each piece of money serves ' + capNumText(inst.velocity) + ' times, so '
        + M(needed) + ' is needed in circulation. This is the lab\'s formalisation of Marx\'s sentence, which speaks of '
        + 'subtracting the circuits a coin makes.';
      if (view === 'payments') {
        var skip = inst['default'] === null ? -1 : Number(inst['default'].n) - 1;
        if (skip >= inst.bills.length) {
          return { refuse: 'There is no bill number ' + (skip + 1) + '; there ' + (inst.bills.length === 1 ? 'is 1 bill' : 'are ' + inst.bills.length + ' bills') };
        }
        var nets = moNetOf(inst.bills, skip), unbacked = R0;
        inst.bills.forEach(function (b) { if (!b.backed) unbacked = Radd(unbacked, b.amount); });
        tiles.moNetted = M(nets.cash);
        tiles.moUnbacked = M(unbacked);
        said += ' The bills paid come to ' + M(nets.gross) + '; set against one another they need ' + M(nets.cash)
          + ' in cash' + (skip >= 0 ? ', with bill ' + (skip + 1) + ' (' + inst.bills[skip].from + ' to ' + inst.bills[skip].to + ') unpaid' : '') + '.';
        return { tiles: tiles, status: said, table: { caption: 'Each party\'s balance once the bills are set off',
          head: ['party', 'net'], rows: nets.order.map(function (w) { return [w, capSigned(nets.net[w], M)]; }) } };
      }
      if (view === 'bank-act') {
        var returned = capMax(R0, Rsub(inst.issue, needed)), cap = Radd(inst.fiduciary, inst.reserve);
        var gap = capMax(R0, Rsub(inst.demand, cap));
        tiles.moReturned = M(returned); tiles.moCap = M(cap); tiles.moGap = M(gap);
        said += ' Of ' + M(inst.issue) + ' issued, ' + M(returned) + ' is more than circulation absorbs and flows back. '
          + 'The Act caps notes at the fiduciary issue plus the gold reserve, ' + M(cap) + ', so a demand for '
          + M(inst.demand) + ' leaves ' + M(gap) + ' unmet.';
      }
      return { tiles: tiles, status: said, table: goodsTable(prices) };
    }
    if (view === 'world') {
      var d = Rsub(Rsub(inst.imports, inst.exports), inst.other_receipts);
      return { tiles: { moDrain: moDrainText(d, M) },
        status: 'Imports of ' + M(inst.imports) + ' against exports of ' + M(inst.exports) + ' and other receipts of '
          + M(inst.other_receipts) + ' leave ' + (Rsign(d) > 0 ? M(d) + ' to be shipped abroad in bullion'
          : (Rsign(d) < 0 ? M(Rneg(d)) + ' owed to this country, so bullion flows in, not out' : 'nothing to ship')) + '.',
        table: null };
    }
    /* fixed-rent */
    var real = Rdiv(inst.rent, inst.price_index);
    var gain = Rsub(Rsub(Rmul(inst.product, inst.price_index), Rmul(inst.wages, inst.wage_index)), inst.rent);
    return { tiles: { moRealRent: M(real), moFarmerGain: M(gain) },
      status: 'Prices are ' + capNumText(inst.price_index) + ' times what they were and money wages '
        + capNumText(inst.wage_index) + ' times. A rent fixed at ' + M(inst.rent) + ' is worth ' + M(real)
        + ' at the old prices; the farmer keeps the product at the new prices, less wages and the rent, ' + M(gain) + '.',
      table: { caption: 'The farmer\'s account at the new prices', head: ['item', 'at old prices', 'at new prices'],
        rows: [['product', M(inst.product), M(Rmul(inst.product, inst.price_index))],
               ['wages', M(inst.wages), M(Rmul(inst.wages, inst.wage_index))],
               ['rent', M(inst.rent), M(inst.rent)]] } };
  }
"""

MONEY_FIELDS = {
    "goods": ("Commodities: name, value in hours; separated by ;",
              ("rec", [("name", "name"), ("value_hours", "pos")], 1, 6, True), None),
    "gold_hours_per_unit": ("Hours of labour in one unit of money (gold)", "pos", None),
    "velocity": ("Velocity: times each piece of money changes hands", "pos", None),
    "credit_sales": ("Sold on credit, not yet paid", "nn", 0),
    "payments_due": ("Payments falling due", "nn", 0),
    "cancelling": ("Payments that cancel one another", "nn", 0),
    "bills": ("Bills: from, to, amount, backed by a sale (yes or no); separated by ;",
              ("rec", [("from", "name"), ("to", "name"), ("amount", "pos"), ("backed", "yesno")], 0, 12, False), []),
    "default": ("The number of a bill that is not paid (empty for none)", "optcount", None),
    "imports": ("Imports", "nn", None),
    "exports": ("Exports", "nn", None),
    "other_receipts": ("Other receipts from abroad (negative for payments owed abroad)", "num", 0),
    "rent": ("Money rent fixed by the lease", "nn", None),
    "price_index": ("Prices now, as a multiple of then", "pos", None),
    "wage_index": ("Money wages now, as a multiple of then", "pos", None),
    "product": ("The farmer's product, at the old prices", "nn", None),
    "wages": ("The farmer's wage bill, at the old wages", "nn", None),
    "issue": ("Notes issued", "nn", None),
    "reserve": ("Gold reserve", "nn", None),
    "fiduciary": ("Fiduciary issue (notes without gold behind them)", "nn", None),
    "demand": ("Demand for notes", "nn", None),
}

MONEY_VIEWS = {
    "circulate": dict(fields=["goods", "gold_hours_per_unit", "velocity"],
                      tiles=[("Sum of prices", "moPriceSum"), ("Money needed", "moNeeded")]),
    "payments": dict(fields=["goods", "gold_hours_per_unit", "velocity", "credit_sales", "payments_due",
                             "cancelling", "bills", "default"],
                     tiles=[("Sum of prices", "moPriceSum"), ("Money needed", "moNeeded"),
                            ("Cash to settle the bills", "moNetted"), ("Bills with no sale behind them", "moUnbacked")]),
    "world": dict(fields=["imports", "exports", "other_receipts"],
                  tiles=[("Bullion shipped", "moDrain")]),
    "fixed-rent": dict(fields=["rent", "price_index", "wage_index", "product", "wages"],
                       tiles=[("The rent at the old prices", "moRealRent"), ("The farmer keeps", "moFarmerGain")]),
    "bank-act": dict(fields=["goods", "gold_hours_per_unit", "velocity", "issue", "reserve", "fiduciary", "demand"],
                     tiles=[("Money needed", "moNeeded"), ("Notes that flow back", "moReturned"),
                            ("The Act's cap on notes", "moCap"), ("Demand left unmet", "moGap")]),
}


def _money_check(where, p):
    bills = p.get("bills") or []
    d = p.get("default")
    if d not in (None, "") and not (isinstance(d, int) and 1 <= d <= len(bills)):
        raise ValueError("%s: default %r is not the number of one of the %d bills" % (where, d, len(bills)))

# ---------------------------------------------------------------------------
# circuit
# ---------------------------------------------------------------------------

CIRCUIT_JS = r"""
  function ciLpOf(subsistence) {
    return capSum(subsistence.map(function (s) { return Rdiv(s.hours, s.every_days); }));
  }
  /* Sellers in a ring: each sells its goods to the next at value * (1 +
     markup). What each holds after is the goods received plus money net. */
  function ciRingOf(sellers) {
    var n = sellers.length, price = sellers.map(function (s) { return Rmul(s.value, Radd(R1, s.markup)); });
    return sellers.map(function (s, i) {
      var prev = (i + n - 1) % n;
      var after = Radd(sellers[prev].value, Rsub(price[i], price[prev]));
      return { name: s.name, before: s.value, price: price[i], after: after };
    });
  }
  function ciCompute(view, inst, U) {
    var M = function (x) { return capMoney(x, U.money); };
    if (view === 'formula') {
      var money = inst.start === 'money', delta = Rsub(inst.product, inst.M);
      return { tiles: { ciForm: money ? 'M–C–M′' : 'C–M–C', ciDelta: capSigned(delta, M) },
        status: (money ? 'The circuit starts and ends with money: ' + M(inst.M) + ' buys a commodity that sells for '
          + M(inst.product) + '. Money at the end differs from money at the start only by its amount, ' + capSigned(delta, M) + '.'
          : 'The circuit starts and ends with a commodity: one sold for ' + M(inst.product) + ', another bought for '
          + M(inst.M) + '. Money only mediates; the difference in money is ' + capSigned(delta, M) + '.'), table: null };
    }
    if (view === 'markup') {
      if (inst.sellers.some(function (s) { return Rcmp(s.markup, R(-1n)) < 0; })) {
        return { refuse: 'A mark-up below −1 would be a negative price' };
      }
      var ring = ciRingOf(inst.sellers), before = capSum(ring.map(function (r) { return r.before; }));
      var after = capSum(ring.map(function (r) { return r.after; }));
      return { tiles: { ciTotalBefore: M(before), ciTotalAfter: M(after) },
        status: 'Each seller sells to the next in the list, the last to the first, at its mark-up. What one gains as a '
          + 'seller another loses as a buyer: the values held come to ' + M(before) + ' before and ' + M(after) + ' after.',
        table: { caption: 'Each party before and after', head: ['party', 'holds before', 'sells at', 'holds after', 'gain'],
          rows: ring.map(function (r) { return [r.name, M(r.before), M(r.price), M(r.after), capSigned(Rsub(r.after, r.before), M)]; }) } };
    }
    if (view === 'labour-power' || view === 'market') {
      var lp = ciLpOf(inst.subsistence);
      var rows = inst.subsistence.map(function (s) {
        return [s.item, M(s.hours), capNumText(s.every_days), M(Rdiv(s.hours, s.every_days))];
      });
      var table = { caption: 'The means of subsistence, per day', head: ['item', 'value', 'renewed every (days)', 'per day'], rows: rows };
      if (view === 'labour-power') {
        return { tiles: { ciLpValue: M(lp) }, table: table,
          status: 'Each item\'s value is spread over the days it lasts; together they make the daily value of '
            + 'labour-power, ' + M(lp) + '.' };
      }
      if (Rcmp(inst.self_supplied_value, lp) > 0) {
        return { refuse: 'A household cannot supply itself with more than its whole subsistence, ' + M(lp) + ' a day' };
      }
      var bought = Rsub(lp, inst.self_supplied_value), market = Rmul(inst.households, bought);
      return { tiles: { ciLpValue: M(lp), ciMarket: M(market) }, table: table,
        status: capNumText(inst.households) + ' households each need ' + M(lp) + ' a day and still make '
          + M(inst.self_supplied_value) + ' of it themselves, so they buy ' + M(bought) + ' each: a market of '
          + M(market) + ' a day.' };
    }
    if (view === 'stages') {
      if (!Requ(Radd(inst.mp, inst.lp), inst.M)) {
        return { refuse: 'M buys the means of production and labour-power, so M must equal mp + lp, and '
          + M(inst.mp) + ' + ' + M(inst.lp) + ' is not ' + M(inst.M) };
      }
      var mprime = Rmul(inst.product, inst.sold_share), s = Rsub(mprime, inst.M);
      return { tiles: { ciMprime: M(mprime), ciS: M(s) },
        status: 'M–C: ' + M(inst.M) + ' buys ' + M(inst.mp) + ' of means of production and ' + M(inst.lp)
          + ' of labour-power. …P…: production makes a product worth ' + M(inst.product) + '. C′–M′: '
          + capNumText(inst.sold_share) + ' of it sells, for ' + M(mprime) + ', so M′ − M = ' + M(s) + '.',
        table: { caption: 'The stages of the circuit', head: ['stage', 'value'],
          rows: [['M', M(inst.M)], ['C = mp + lp', M(inst.M)], ['C′ (the product)', M(inst.product)], ['M′ (sold)', M(mprime)]] } };
    }
    if (view === 'costs') {
      var s0 = Rsub(inst.product, inst.M), net = Rsub(s0, inst.pure_costs);
      return { tiles: { ciS: M(s0), ciSNet: M(net) },
        status: 'Costs that add value (transport, storage) are advanced and come back in the product\'s value: '
          + M(inst.value_adding_costs) + ' in and ' + M(inst.value_adding_costs) + ' out, leaving s at ' + M(s0)
          + '. Pure costs of circulation add nothing and are paid out of s: ' + M(s0) + ' − ' + M(inst.pure_costs) + ' = ' + M(net) + '.',
        table: { caption: 'Capital advanced and the product', head: ['', 'advanced', 'in the product'],
          rows: [['production', M(inst.M), M(inst.product)], ['value-adding costs', M(inst.value_adding_costs), M(inst.value_adding_costs)],
                 ['pure costs', M(inst.pure_costs), M(R0)]] } };
    }
    /* realise */
    var thrown = Radd(inst.M, inst.consumption_advance), returned = capMin(inst.product, thrown);
    var sr = Rsub(returned, inst.M);
    return { tiles: { ciReturned: M(returned), ciS: M(sr) },
      status: 'The capitalist class throws ' + M(inst.M) + ' into circulation as capital and ' + M(inst.consumption_advance)
        + ' as money for its own consumption. That is all the money there is to buy a product worth ' + M(inst.product)
        + ', so ' + M(returned) + ' returns and ' + M(sr) + ' of surplus value is realised in money.', table: null };
  }
"""

CIRCUIT_FIELDS = {
    "start": ("The circuit starts with (money or commodity)", ("word", ["money", "commodity"]), None),
    "M": ("M: money laid out", "nn", None),
    "mp": ("mp: means of production bought", "nn", None),
    "lp": ("lp: labour-power bought", "nn", None),
    "product": ("Money received / value of the product", "nn", None),
    "sold_share": ("Share of the product sold", "share", 1),
    "sellers": ("Sellers: name, value of goods, mark-up (1/10 is 10%); separated by ;",
                ("rec", [("name", "name"), ("value", "pos"), ("markup", "num")], 2, 8, True), None),
    "subsistence": ("Subsistence: item, value, renewed every so many days; separated by ;",
                    ("rec", [("item", "name"), ("hours", "nn"), ("every_days", "pos")], 1, 12, True), None),
    "households": ("Households", "count", None),
    "self_supplied_value": ("Subsistence each household still makes itself, per day", "nn", 0),
    "pure_costs": ("Pure costs of circulation", "nn", 0),
    "value_adding_costs": ("Costs that add value (transport, storage)", "nn", 0),
    "consumption_advance": ("Money the capitalists spend on their own consumption", "nn", 0),
}

CIRCUIT_VIEWS = {
    "formula": dict(fields=["start", "M", "product"],
                    tiles=[("The circuit", "ciForm"), ("Money at the end less money at the start", "ciDelta")]),
    "markup": dict(fields=["sellers"],
                   tiles=[("Values held before", "ciTotalBefore"), ("Values held after", "ciTotalAfter")]),
    "labour-power": dict(fields=["subsistence"], tiles=[("Value of labour-power, per day", "ciLpValue")]),
    "stages": dict(fields=["M", "mp", "lp", "product", "sold_share"],
                   tiles=[("M′", "ciMprime"), ("Surplus value realised", "ciS")]),
    "market": dict(fields=["households", "subsistence", "self_supplied_value"],
                   tiles=[("Subsistence per household, per day", "ciLpValue"), ("The market created, per day", "ciMarket")]),
    "costs": dict(fields=["M", "product", "pure_costs", "value_adding_costs"],
                  tiles=[("Surplus value", "ciS"), ("Surplus value after pure costs", "ciSNet")]),
    "realise": dict(fields=["M", "product", "consumption_advance"],
                    tiles=[("Money returned", "ciReturned"), ("Surplus value realised", "ciS")]),
}

# ---------------------------------------------------------------------------
# surplus
# ---------------------------------------------------------------------------

SURPLUS_JS = r"""
  /* surplus. The value one hour adds is the wage over the necessary hours:
     a day's labour-power at 3s is the value of 6 hours, so an hour adds 1/2 s. */
  function suNewValue(hours, wage, necessary) { return Rdiv(Rmul(hours, wage), necessary); }
  function suPartsOf(c, v, s, output, unit) {
    var total = Radd(Radd(c, v), s);
    return [['c', c], ['v', v], ['s', s]].map(function (p) {
      return p[0] + ': ' + capQty(Rdiv(Rmul(output, p[1]), total), unit);
    }).join(', ');
  }
  function suCompute(view, inst, U) {
    var M = function (x) { return capMoney(x, U.money); };
    var day = inst.hours, nec = inst.necessary_hours;
    if (day !== undefined && Rcmp(day, R(24n)) > 0) return { refuse: 'A day has 24 hours, and this one has ' + capHours(day) };
    if (view === 'mill' || view === 'transfer') {
      var nv = suNewValue(inst.hours, inst.wage, nec);
      if (view === 'mill') {
        if (Rcmp(inst.waste, inst.materials) > 0) return { refuse: 'The waste cannot exceed the materials used' };
        var carried = Radd(Rsub(inst.materials, inst.waste), inst.wear), product = Radd(carried, nv);
        var advanced = Radd(Radd(inst.materials, inst.wear), inst.wage), s = Rsub(product, advanced);
        return { tiles: { suProduct: M(product), suS: M(s) },
          status: 'Advanced: ' + M(inst.materials) + ' of materials, ' + M(inst.wear) + ' of wear, ' + M(inst.wage)
            + ' for a day\'s labour-power, ' + M(advanced) + ' in all. ' + capHours(inst.hours) + ' of labour add '
            + M(nv) + ' and the means of production pass over ' + M(carried)
            + (Rsign(inst.waste) > 0 ? ' (the ' + M(inst.waste) + ' of waste beyond the socially necessary passes over nothing)' : '')
            + ', so the product is worth ' + M(product) + ' against ' + M(advanced) + ' advanced: '
            + (Rsign(s) < 0 ? M(Rneg(s)) + ' less.' : M(s) + ' more.'),
          table: { caption: 'The value of the product', head: ['part', 'value'],
            rows: [['materials carried over', M(Rsub(inst.materials, inst.waste))], ['wear carried over', M(inst.wear)],
                   ['new value added', M(nv)], ['product', M(product)], ['capital advanced', M(advanced)]] } };
      }
      var perDay = Rdiv(inst.machine_value, inst.machine_days), transfer = Radd(perDay, inst.materials);
      var prod = Radd(transfer, nv);
      return { tiles: { suTransfer: M(transfer), suProduct: M(prod) },
        status: 'A machine worth ' + M(inst.machine_value) + ' lasting ' + capNumText(inst.machine_days) + ' days passes '
          + M(perDay) + ' a day into the product; the materials pass over their present value, ' + M(inst.materials)
          + '. Constant capital transfers ' + M(transfer) + ' and adds nothing; labour adds ' + M(nv) + '.',
        table: null };
    }
    if (view === 'rate' || view === 'parts') {
      var total = Radd(Radd(inst.c, inst.v), inst.s), rate = Rdiv(inst.s, inst.v);
      var parts = suPartsOf(inst.c, inst.v, inst.s, inst.output, U.qty);
      return { tiles: { suRate: capPct(rate), suParts: parts, suProduct: M(total) },
        status: 'c + v + s = ' + M(inst.c) + ' + ' + M(inst.v) + ' + ' + M(inst.s) + ' = ' + M(total) + '. The rate of '
          + 'surplus value is s over v alone, ' + capPct(rate) + '; s over the whole capital would be '
          + capPct(Rdiv(inst.s, Radd(inst.c, inst.v))) + ', a different quantity. In ' + capQty(inst.output, U.qty)
          + ' of product the parts are ' + parts + '.', table: null };
    }
    if (Rcmp(nec, day) > 0) {
      return { refuse: 'The day, ' + capHours(day) + ', is shorter than the necessary labour-time, ' + capHours(nec) };
    }
    var sur = Rsub(day, nec), r = Rdiv(sur, nec);
    if (view === 'senior') {
      var cut = Rsub(day, R1);
      if (Rcmp(cut, nec) < 0) return { refuse: 'Cutting an hour would leave a day shorter than the necessary labour-time' };
      var after = Rdiv(Rsub(cut, nec), nec);
      return { tiles: { suRate: capPct(r), suLastHour: capPct(after) + ' (Senior: 0)' },
        status: capHours(sur) + ' of surplus labour on ' + capHours(nec) + ' necessary is ' + capPct(r)
          + '. Cut the day by one hour and ' + capHours(Rsub(cut, nec)) + ' on ' + capHours(nec) + ' is ' + capPct(after)
          + '; Senior predicted that the net profit would vanish.', table: null };
    }
    if (view === 'mass') {
      var mass = Rmul(Rmul(r, inst.wage), inst.workers);
      return { tiles: { suMass: M(mass), suRate: capPct(r) },
        status: capNumText(inst.workers) + ' workers at ' + M(inst.wage) + ' a day each, at a rate of ' + capPct(r)
          + ' (' + capHours(day) + ' worked, ' + capHours(nec) + ' necessary), give a mass of surplus value of '
          + M(mass) + ' a day.', table: null };
    }
    /* formulae */
    var falseRate = Rdiv(sur, day);
    return { tiles: { suRate: capPct(r), suFalse: capPct(falseRate) },
      status: 'Surplus labour over necessary labour is ' + capPct(r) + '; surplus labour over the whole day is '
        + capPct(falseRate) + ', which can approach 100% but never reach it.', table: null };
  }
"""

SURPLUS_FIELDS = {
    "materials": ("Materials used up (their value)", "nn", None),
    "wear": ("Wear of instruments", "nn", 0),
    "wage": ("Value of a day's labour-power (the wage)", "pos", None),
    "hours": ("Hours worked in the day", "nn", None),
    "necessary_hours": ("Necessary hours (labour that reproduces the wage)", "pos", None),
    "waste": ("Materials wasted beyond the socially necessary", "nn", 0),
    "machine_value": ("Value of the machine", "nn", None),
    "machine_days": ("Life of the machine, in days", "pos", None),
    "c": ("c, constant capital", "nn", None),
    "v": ("v, variable capital", "pos", None),
    "s": ("s, surplus value", "nn", None),
    "output": ("Units of product", "pos", None),
    "workers": ("Workers", "nncount", None),
}

SURPLUS_VIEWS = {
    "mill": dict(fields=["materials", "wear", "wage", "hours", "necessary_hours", "waste"],
                 tiles=[("Value of the product", "suProduct"), ("Product less capital advanced", "suS")]),
    "transfer": dict(fields=["machine_value", "machine_days", "materials", "wage", "hours", "necessary_hours"],
                     tiles=[("Value transferred, per day", "suTransfer"), ("Value of the day's product", "suProduct")]),
    "rate": dict(fields=["c", "v", "s", "output"],
                 tiles=[("Rate of surplus value, s/v", "suRate"), ("The product in parts", "suParts")]),
    "parts": dict(fields=["c", "v", "s", "output"],
                  tiles=[("Value of the product", "suProduct"), ("The product in parts", "suParts")]),
    "senior": dict(fields=["hours", "necessary_hours"],
                   tiles=[("Rate of surplus value, s/v", "suRate"), ("After cutting one hour", "suLastHour")]),
    "mass": dict(fields=["wage", "workers", "hours", "necessary_hours"],
                 tiles=[("Mass of surplus value, per day", "suMass"), ("Rate of surplus value, s/v", "suRate")]),
    "formulae": dict(fields=["hours", "necessary_hours"],
                     tiles=[("s/v", "suRate"), ("s/(v + s)", "suFalse")]),
}

# ---------------------------------------------------------------------------
# workday
# ---------------------------------------------------------------------------

WORKDAY_JS = r"""
  /* The day as one bar cut at the necessary time. Pixel widths are BigInt
     divisions of the exact figures: nothing on this page is a float. */
  function wdBar(total, cut, fmt) {
    var w = 620n, xc = 10n;
    if (Rsign(total) > 0) {
      var c = capMin(capMax(cut, R0), total);
      xc = 10n + (w * c.n * total.d) / (c.d * total.n);
    }
    var sur = Rsub(total, cut);
    return '<svg viewBox="0 0 640 74" role="img" style="width:100%;height:auto;display:block" aria-label="'
      + capEsc('necessary ' + fmt(cut) + ', surplus ' + fmt(sur)) + '">'
      + '<rect x="10" y="8" width="' + (xc - 10n) + '" height="30" fill="var(--cyan)" opacity="0.35"></rect>'
      + '<rect x="' + xc + '" y="8" width="' + (630n - xc) + '" height="30" fill="var(--amber)" opacity="0.45"></rect>'
      + '<rect x="10" y="8" width="620" height="30" fill="none" stroke="var(--line-strong)"></rect>'
      + '<line x1="' + xc + '" y1="4" x2="' + xc + '" y2="42" stroke="var(--text)" stroke-width="2"></line>'
      + '<text x="10" y="62" fill="var(--text)" font-size="14">necessary ' + capEsc(fmt(cut)) + '</text>'
      + '<text x="630" y="62" text-anchor="end" fill="var(--text)" font-size="14">surplus ' + capEsc(fmt(sur)) + '</text></svg>';
  }
  function wdKindOf(day, nec, newDay, newNec) {
    var a = !Requ(day, newDay), r = !Requ(nec, newNec);
    return a && r ? 'both' : (a ? 'absolute' : (r ? 'relative' : 'none'));
  }
  function wdCompute(view, inst, U, opts) {
    var H = capHours;
    if (view === 'corvee') {
      var all = Radd(inst.lord_days, inst.own_days), days = function (x) { return capNumText(x) + (Requ(x, R1) ? ' day' : ' days'); };
      var rc = Rdiv(inst.lord_days, inst.own_days);
      return { tiles: { wdSurplus: days(inst.lord_days), wdRate: capPct(rc) },
        status: 'Of ' + days(all) + ', ' + days(inst.own_days) + ' are worked on the producer\'s own field and '
          + days(inst.lord_days) + ' on the lord\'s: surplus labour stands visibly beside necessary labour, at ' + capPct(rc) + '.',
        table: null, svg: wdBar(all, inst.own_days, days) };
    }
    if (Rcmp(inst.day, R(24n)) > 0) return { refuse: 'A day has 24 hours, and this one has ' + H(inst.day) };
    var day = inst.day, nec = inst.necessary, made = day, said = '', tiles = {};
    if (view === 'limit') {
      made = capMin(day, inst.limit);
      said = 'The law limits the day to ' + H(inst.limit) + '; ' + H(made) + ' are worked. ';
    } else if (view === 'relative') {
      nec = Rdiv(nec, inst.productivity);
      var extra = Rmul(day, Rsub(inst.pioneer_productivity, R1));
      tiles.wdExtra = capSigned(extra, H);
      said = (Requ(inst.productivity, R1) ? 'Productivity in the wage-goods industries is unchanged. '
        : 'Productivity in the wage-goods industries is ' + capNumText(inst.productivity) + ' times what it was, so the '
          + 'necessary time goes from ' + H(inst.necessary) + ' to ' + H(nec) + '. ')
        + (Requ(inst.pioneer_productivity, R1) ? '' : 'A pioneer ' + capNumText(inst.pioneer_productivity)
          + ' times as productive as the average, selling at the social value, gains ' + capSigned(extra, H)
          + ' a day of extra surplus value. ');
    } else if (view === 'intensity') {
      made = Rmul(day, inst.intensity);
      tiles.wdLabour = H(made);
      said = 'A ' + H(day) + ' day at ' + capNumText(inst.intensity) + ' times the normal intensity spends ' + H(made) + ' of normal labour. ';
    } else if (view === 'classify') {
      if (Rcmp(inst.new_day, R(24n)) > 0) return { refuse: 'A day has 24 hours, and the new one has ' + H(inst.new_day) };
      tiles.wdKind = wdKindOf(day, nec, inst.new_day, inst.new_necessary);
      var r0 = Rcmp(nec, day) <= 0 ? capPct(Rdiv(Rsub(day, nec), nec)) : null;
      said = 'Before: a ' + H(day) + ' day with ' + H(nec) + ' necessary' + (r0 ? ', ' + r0 : '') + '. After: a '
        + H(inst.new_day) + ' day with ' + H(inst.new_necessary) + ' necessary. A longer day is absolute surplus value; '
        + 'a shorter necessary time is relative. ';
      made = inst.new_day; nec = inst.new_necessary;
    } else if (view === 'three') {
      var hold = opts.hold, p = (hold === 'productivity' || hold === 'combined') ? inst.productivity : R1;
      var it = (hold === 'intensity' || hold === 'combined') ? inst.intensity : R1;
      var d = (hold === 'length' || hold === 'combined') ? inst.new_day : day;
      if (Rcmp(d, R(24n)) > 0) return { refuse: 'A day has 24 hours, and the new one has ' + H(d) };
      nec = Rdiv(inst.necessary, p); made = Rmul(d, it);
      tiles.wdLpValue = H(nec);
      said = {
        productivity: 'Productivity varies, the length and intensity of the day held: ',
        intensity: 'Intensity varies, the length of the day and productivity held: ',
        length: 'The length of the day varies, productivity and intensity held: ',
        combined: 'All three vary at once: '
      }[hold] + 'a ' + H(d) + ' day at intensity ' + capNumText(it) + ' produces ' + H(made) + ' of value, of which '
        + 'labour-power, at productivity ' + capNumText(p) + ', is worth ' + H(nec) + '. ';
    } else if (view === 'separate') {
      if (inst.own_land) {
        tiles.wdSurplus = H(R0);
        tiles.wdRate = capPct(R0);
        return { tiles: tiles, svg: wdBar(day, day, H), table: null,
          status: 'On one\'s own land every one of the ' + H(day) + ' is worked for the household; no part of the day is '
            + 'surplus labour for anyone else, for ' + (inst.count.n === 1n ? 'one household' : capNumText(inst.count) + ' households') + '.' };
      }
    }
    if (Rcmp(nec, made) > 0) {
      return { refuse: said + 'That is less than the necessary labour-time, ' + H(nec) + ', so there is no surplus labour' };
    }
    var sur = Rsub(made, nec), rate = Rdiv(sur, nec);
    var count = view === 'separate' ? inst.count : R1;
    tiles.wdSurplus = H(Rmul(sur, count));
    tiles.wdRate = capPct(rate);
    said += H(nec) + ' necessary and ' + H(sur) + ' surplus: s/v = ' + capPct(rate)
      + (view === 'separate' ? '. Separated from the land, ' + (count.n === 1n ? 'one household works' : capNumText(count) + ' households work')
        + ' ' + H(Rmul(sur, count)) + ' of surplus labour a day for an employer' : '') + '.';
    return { tiles: tiles, status: said, table: null, svg: wdBar(made, nec, H) };
  }
"""

WORKDAY_FIELDS = {
    "day": ("Length of the working day, hours", "pos", None),
    "necessary": ("Necessary labour-time, hours", "pos", None),
    "limit": ("The legal limit, hours", "pos", None),
    "productivity": ("Productivity in the wage-goods industries (2 is twice as productive)", "pos", 1),
    "pioneer_productivity": ("The pioneer's productivity against the average", "pos", 1),
    "intensity": ("Intensity of labour (4/3 is a third more labour per hour)", "pos", 1),
    "new_day": ("The new length of the day, hours", "pos", None),
    "new_necessary": ("The new necessary labour-time, hours", "pos", None),
    "own_land": ("Working one's own land (yes or no)", "yesno", None),
    "count": ("Households", "count", 1),
    "lord_days": ("Days worked for the lord", "nn", None),
    "own_days": ("Days worked on one's own field", "pos", None),
}

WD_HOLD = [("productivity", "productivity varies"), ("intensity", "intensity varies"),
           ("length", "the length of the day varies"), ("combined", "all three vary")]

_WD_SR = [("Surplus labour", "wdSurplus"), ("Rate of surplus value", "wdRate")]

WORKDAY_VIEWS = {
    "absolute": dict(fields=["day", "necessary"], tiles=_WD_SR),
    "limit": dict(fields=["day", "necessary", "limit"], tiles=_WD_SR),
    "relative": dict(fields=["day", "necessary", "productivity", "pioneer_productivity"],
                     tiles=_WD_SR + [("The pioneer's extra surplus value, per day", "wdExtra")]),
    "intensity": dict(fields=["day", "necessary", "intensity"],
                      tiles=[("Labour spent, in normal hours", "wdLabour")] + _WD_SR),
    "classify": dict(fields=["day", "necessary", "new_day", "new_necessary"],
                     tiles=[("The change is", "wdKind")] + _WD_SR),
    "three": dict(fields=["day", "necessary", "productivity", "intensity", "new_day"],
                  tiles=[("Value of labour-power, per day", "wdLpValue"), ("Rate of surplus value", "wdRate")],
                  redraw=[("hold", "wdHold", "Which factor varies", WD_HOLD)]),
    "separate": dict(fields=["day", "necessary", "own_land", "count"], tiles=_WD_SR),
    "corvee": dict(fields=["lord_days", "own_days"], tiles=_WD_SR),
}

# ---------------------------------------------------------------------------
# machine
# ---------------------------------------------------------------------------

MACHINE_JS = r"""
  /* Detail workers per step so every step's hourly output is equal, in the
     smallest whole numbers: w_i proportional to 1/rate_i. */
  function maBalance(rates) {
    var inv = rates.map(function (r) { return Rinv(r); }), L = 1n, g = 0n;
    inv.forEach(function (x) { L = L / bgcd(L, x.d) * x.d; });
    var w = inv.map(function (x) { return x.n * (L / x.d); });
    w.forEach(function (v) { g = bgcd(g, v); });
    return w.map(function (v) { return v / g; });
  }
  function maVerdictOf(test, inst) {
    var cost = inst.machine_value, against = test === 'society' ? inst.labour_saved_value : inst.wages_displaced;
    return (Rcmp(cost, against) < 0 ? 'adopted' : 'not adopted') + (test === 'society' ? ' (society’s test)' : ' (the capitalist’s test)');
  }
  function maCompute(view, inst, U, opts) {
    var M = function (x) { return capMoney(x, U.money); };
    if (view === 'cooperate') {
      var out = Rmul(inst.workers, inst.output_each), alone = Rdiv(inst.c_each_if_alone, inst.output_each);
      var together = Rdiv(inst.shared_c, out), combined = Rmul(inst.workers, inst.hours);
      return { tiles: { maOutput: capQty(out, U.qty), maCPerUnit: 'alone ' + M(alone) + ', together ' + M(together),
                        maCombinedDay: capHours(combined) },
        status: 'Working alone, each worker\'s means of production, ' + M(inst.c_each_if_alone) + ', go into '
          + capQty(inst.output_each, U.qty) + ': ' + M(alone) + ' a unit. Used in common, ' + M(inst.shared_c) + ' go into '
          + capQty(out, U.qty) + ': ' + M(together) + ' a unit. ' + capNumText(inst.workers) + ' workers deliver '
          + capHours(combined) + ' of labour in one day. No wage is paid for the difference.', table: null };
    }
    if (view === 'detail') {
      var w = maBalance(inst.steps.map(function (s) { return s.rate; }));
      var total = w.reduce(function (a, b) { return a + b; }, 0n), perHour = Rmul(inst.steps[0].rate, R(w[0]));
      return { tiles: { maWorkers: inst.steps.map(function (s, i) { return s.name + ' ' + capGroup(String(w[i])); }).join(', '),
                        maMinimum: capGroup(String(total)) },
        status: 'Each step must turn out as many pieces an hour as the others, so its workers stand in inverse proportion '
          + 'to its rate. The smallest shop that keeps everyone busy has ' + capGroup(String(total)) + ' workers and turns out '
          + capQty(perHour, U.qty) + ' an hour at every step.',
        table: { caption: 'Workers per step', head: ['step', 'pieces an hour each', 'workers', 'pieces an hour'],
          rows: inst.steps.map(function (s, i) {
            return [s.name, capNumText(s.rate), capGroup(String(w[i])), capNumText(Rmul(s.rate, R(w[i])))];
          }) } };
    }
    if (view === 'adopt') {
      var per = Rdiv(inst.machine_value, inst.machine_life_units);
      return { tiles: { maPerUnit: M(per), maVerdict: maVerdictOf(opts.test, inst) },
        status: 'The machine, worth ' + M(inst.machine_value) + ' over ' + capQty(inst.machine_life_units, U.qty || 'units')
          + ' of product'
          + ', passes ' + M(per) + ' into each unit. The capitalist compares its cost with the wages it displaces, '
          + M(inst.wages_displaced) + '; society would compare it with the labour it saves, ' + M(inst.labour_saved_value) + '.',
        table: null };
    }
    /* displace */
    var saved = Rmul(inst.discharged, inst.wage_each);
    if (Rcmp(saved, inst.variable) > 0) return { refuse: 'More wages are discharged than the variable capital pays' };
    var freed = capMax(R0, Rsub(saved, inst.machine_spend)), byFreed = Rdiv(freed, inst.wage_each);
    var byBuilding = Rdiv(Rdiv(inst.machine_spend, Radd(R1, inst.mb_composition)), inst.wage_each);
    var all = Radd(byFreed, byBuilding);
    return { tiles: { maDisplaced: capNumText(inst.discharged),
                      maReemployed: capNumText(all) + ' = ' + capNumText(byFreed) + ' set free + ' + capNumText(byBuilding) + ' in machine-building' },
      status: capNumText(inst.discharged) + ' workers at ' + M(inst.wage_each) + ' are discharged: ' + M(saved) + ' of wages. '
        + M(inst.machine_spend) + ' of it is spent on machinery, so ' + M(freed) + ' is set free to employ anyone. Of the machinery\'s '
        + 'price, machine-building at c/v = ' + capNumText(inst.mb_composition) + ' pays ' + M(Rmul(byBuilding, inst.wage_each))
        + ' in wages, at the same wage.',
      table: { caption: 'The variable capital before and after', head: ['', 'variable capital', 'workers'],
        rows: [['before', M(inst.variable), capNumText(Rdiv(inst.variable, inst.wage_each))],
               ['after', M(Rsub(inst.variable, saved)), capNumText(Rdiv(Rsub(inst.variable, saved), inst.wage_each))]] } };
  }
"""

MACHINE_FIELDS = {
    "workers": ("Workers", "count", None),
    "output_each": ("Output of one worker in a day", "pos", None),
    "shared_c": ("Means of production used in common", "nn", None),
    "c_each_if_alone": ("Means of production one worker needs alone", "nn", None),
    "hours": ("Hours in the working day", "pos", None),
    "steps": ("Steps: name, pieces an hour per worker; separated by ;",
              ("rec", [("name", "name"), ("rate", "pos")], 1, 8, True), None),
    "machine_value": ("Value of the machine", "pos", None),
    "machine_life_units": ("Units the machine makes in its life", "pos", None),
    "wages_displaced": ("Wages of the workers it displaces", "nn", None),
    "labour_saved_value": ("Value of the labour it saves", "nn", None),
    "variable": ("Variable capital before the machine", "pos", None),
    "wage_each": ("Wage of one worker", "pos", None),
    "discharged": ("Workers discharged", "nncount", None),
    "machine_spend": ("Spent on the machinery", "nn", None),
    "mb_composition": ("c/v in machine-building", "nn", None),
}

MA_TEST = [("capitalist", "the capitalist's: cost against wages displaced"),
           ("society", "society's: cost against labour saved")]

MACHINE_VIEWS = {
    "cooperate": dict(fields=["workers", "output_each", "shared_c", "c_each_if_alone", "hours"],
                      tiles=[("Output in a day", "maOutput"), ("Constant capital per unit", "maCPerUnit"),
                             ("The combined working day", "maCombinedDay")]),
    "detail": dict(fields=["steps"], tiles=[("Workers per step", "maWorkers"), ("The smallest shop", "maMinimum")]),
    "adopt": dict(fields=["machine_value", "machine_life_units", "wages_displaced", "labour_saved_value"],
                  tiles=[("Value transferred per unit", "maPerUnit"), ("The machine is", "maVerdict")],
                  redraw=[("test", "maTest", "The test", MA_TEST)]),
    "displace": dict(fields=["variable", "wage_each", "discharged", "machine_spend", "mb_composition"],
                     tiles=[("Workers displaced", "maDisplaced"), ("Workers re-employed", "maReemployed")]),
}

# ---------------------------------------------------------------------------
# wages
# ---------------------------------------------------------------------------

WAGES_JS = r"""
  function waCompute(view, inst, U) {
    var M = function (x) { return capMoney(x, U.money); };
    if (view === 'form' || view === 'time') {
      var price = Rdiv(inst.lp_value, inst.normal_hours);
      if (view === 'form') {
        var made = Rmul(inst.value_per_hour, inst.normal_hours);
        return { tiles: { waHourPrice: M(price), waValueCreated: M(made) + ' in ' + capHours(inst.normal_hours)
          + ' (' + M(inst.value_per_hour) + ' an hour)' },
          status: 'A wage of ' + M(inst.lp_value) + ' for ' + capHours(inst.normal_hours) + ' looks like ' + M(price)
            + ' paid for each hour. It is the value of a day\'s labour-power divided by the hours; the hours themselves create '
            + M(made) + '.', table: null };
      }
      var daily = Rmul(price, inst.hours_worked);
      return { tiles: { waHourPrice: M(price), waDaily: M(daily) },
        status: M(inst.lp_value) + ' for a normal day of ' + capHours(inst.normal_hours) + ' is ' + M(price) + ' an hour. '
          + capHours(inst.hours_worked) + ' at that price pays ' + M(daily) + ', against a daily value of labour-power of '
          + M(inst.lp_value) + '.', table: null };
    }
    if (view === 'piece') {
      var rate = Rdiv(inst.lp_value, inst.pieces_normal), inForce = inst.rate_cut_to === null ? rate : inst.rate_cut_to;
      var day = Rmul(inForce, inst.pieces_actual);
      return { tiles: { waPieceRate: M(inForce), waDaily: M(day) },
        status: M(inst.lp_value) + ' for the ' + capQty(inst.pieces_normal, U.qty) + ' of a normal day of '
          + capHours(inst.normal_hours) + ' is ' + M(rate) + ' a piece'
          + (inst.rate_cut_to === null ? '' : ', cut to ' + M(inForce)) + '. ' + capQty(inst.pieces_actual, U.qty)
          + ' at ' + M(inForce) + ' pay ' + M(day) + '.', table: null };
    }
    if (view === 'national') {
      var a = inst.countries[0], b = inst.countries[1];
      var rel = Rdiv(Rdiv(a.wage, a.output_per_hour), Rdiv(b.wage, b.output_per_hour));
      var rates = inst.countries.map(function (c) {
        return Rdiv(Rsub(Rmul(c.output_per_hour, inst.unit_value), c.wage), c.wage);
      });
      if (rates.some(function (r) { return Rsign(r) < 0; })) {
        return { refuse: 'In one country an hour creates less value than the hourly wage, so there is no surplus value to compare' };
      }
      return { tiles: { waRelative: Rtext(rel),
                        waRate: inst.countries.map(function (c, i) { return c.name + ' ' + capPct(rates[i]); }).join(', ') },
        status: a.name + ' pays ' + capNumText(Rdiv(a.wage, b.wage)) + ' times ' + b.name + '\'s hourly wage for '
          + capNumText(Rdiv(a.output_per_hour, b.output_per_hour)) + ' times the output, so its wage per unit of output is '
          + Rtext(rel) + ' of ' + b.name + '\'s. With a unit worth ' + M(inst.unit_value) + ' on the world market, the rates of '
          + 'surplus value are ' + inst.countries.map(function (c, i) { return c.name + ' ' + capPct(rates[i]); }).join(' and ') + '.',
        table: { caption: 'Two countries, one hour', head: ['country', 'wage an hour', 'output an hour', 'wage per unit'],
          rows: inst.countries.map(function (c) {
            return [c.name, M(c.wage), capQty(c.output_per_hour, U.qty), M(Rdiv(c.wage, c.output_per_hour))];
          }) } };
    }
    /* statute */
    if (Rcmp(inst.day, R(24n)) > 0) return { refuse: 'A day has 24 hours, and this one has ' + capHours(inst.day) };
    var made2 = Rdiv(Rmul(inst.day, inst.lp_value), inst.necessary), gap = Rsub(inst.lp_value, inst.statutory_wage);
    var r = Rdiv(Rsub(made2, inst.statutory_wage), inst.statutory_wage);
    if (Rsign(r) < 0) return { refuse: 'The day creates less value than the statutory wage' };
    var gapText = Rsign(gap) > 0 ? M(gap) + ' below the value' : (Rsign(gap) < 0 ? M(Rneg(gap)) + ' above the value' : 'at the value');
    return { tiles: { waGap: gapText, waRate: capPct(r) },
      status: 'Labour-power is worth ' + M(inst.lp_value) + ' a day, the value of ' + capHours(inst.necessary) + '. A day of '
        + capHours(inst.day) + ' creates ' + M(made2) + '. Paid the statutory ' + M(inst.statutory_wage)
        + ', the worker yields a rate of surplus value of ' + capPct(r) + '.', table: null };
  }
"""

WAGES_FIELDS = {
    "lp_value": ("Value of a day's labour-power", "pos", None),
    "normal_hours": ("Hours in the normal day", "pos", None),
    "hours_worked": ("Hours actually worked", "nn", None),
    "value_per_hour": ("Value one hour of labour creates", "nn", None),
    "pieces_normal": ("Pieces in a normal day", "pos", None),
    "pieces_actual": ("Pieces actually made", "nn", None),
    "rate_cut_to": ("Piece-rate cut to (empty for no cut)", "opt", None),
    "countries": ("Two countries: name, wage an hour, output an hour; separated by ;",
                  ("rec", [("name", "name"), ("wage", "pos"), ("output_per_hour", "pos")], 2, 2, True), None),
    "unit_value": ("Value of a unit of output on the world market", "pos", None),
    "statutory_wage": ("The statutory wage", "pos", None),
    "day": ("Length of the working day, hours", "pos", None),
    "necessary": ("Necessary labour-time, hours", "pos", None),
}

WAGES_VIEWS = {
    "form": dict(fields=["lp_value", "normal_hours", "value_per_hour"],
                 tiles=[("The apparent price of an hour", "waHourPrice"), ("Value the hours create", "waValueCreated")]),
    "time": dict(fields=["lp_value", "normal_hours", "hours_worked"],
                 tiles=[("Price of an hour", "waHourPrice"), ("The day's wage", "waDaily")]),
    "piece": dict(fields=["lp_value", "normal_hours", "pieces_normal", "pieces_actual", "rate_cut_to"],
                  tiles=[("Piece-rate", "waPieceRate"), ("The day's wage", "waDaily")]),
    "national": dict(fields=["countries", "unit_value"],
                     tiles=[("Wage per unit of output, first over second", "waRelative"),
                            ("Rate of surplus value", "waRate")]),
    "statute": dict(fields=["statutory_wage", "lp_value", "day", "necessary"],
                    tiles=[("The statute's wage", "waGap"), ("Rate of surplus value under the statute", "waRate")]),
}

# ---------------------------------------------------------------------------
# accumulate
# ---------------------------------------------------------------------------

ACCUMULATE_JS = r"""
  /* Accumulation period by period. Each period the whole capital is laid out
     at that period's c/v; s = s' * v, or, when wages are tracked, the value the
     employed create, (1 + s') * the first period's wage each, less the wages
     paid (which is all of v). Demand for labour is v over the wage; if it
     exceeds the supply, the supply is employed and the wage rises to v over
     the supply. A share of s is added to capital, held as a hoard until the
     hoard reaches the investment threshold. */
  function acRun(o) {
    var K = o.capital, hoard = R0, rows = [];
    for (var t = 1; t <= o.periods; t += 1) {
      var tt = R(BigInt(t - 1)), cv = Radd(o.cv, Rmul(tt, o.rise));
      var v = Rdiv(K, Radd(R1, cv)), row = { t: t, K: K, cv: cv, c: Rsub(K, v), v: v }, s;
      if (o.wage) {
        var w0 = Radd(o.wage, Rmul(tt, o.wageGrowth)), demand = Rdiv(v, w0), paid = w0, employed = demand;
        var supply = Radd(o.supply, Rmul(tt, o.growth));
        if (Rcmp(demand, supply) > 0) { employed = supply; paid = Rdiv(v, supply); }
        s = Rsub(Rmul(employed, Rmul(Radd(R1, o.sRate), o.wage)), v);
        row.employed = employed; row.supply = supply; row.reserve = Rsub(supply, employed); row.wage = paid;
      } else {
        s = Rmul(o.sRate, v);
      }
      var fund = Radd(hoard, Rsign(s) > 0 ? Rmul(o.share, s) : R0), added = R0;
      if (Rcmp(fund, o.threshold) >= 0) { added = fund; hoard = R0; } else { hoard = fund; }
      K = Radd(K, added);
      row.s = s; row.added = added; row.hoard = hoard; row.Kend = K;
      rows.push(row);
    }
    return rows;
  }
  /* Concentration and centralisation: every capital grows by `growth`; then,
     under the merge rule, the largest (first among equals) absorbs the
     smallest of the others (last among equals). */
  function acCentralise(caps, growth, merge, periods) {
    var k = caps.slice(), rows = [];
    for (var t = 1; t <= periods; t += 1) {
      k = k.map(function (x) { return Rmul(x, Radd(R1, growth)); });
      if (merge && k.length > 1) {
        var big = 0, small = -1;
        k.forEach(function (x, i) { if (Rcmp(x, k[big]) > 0) big = i; });
        k.forEach(function (x, i) { if (i !== big && (small < 0 || Rcmp(x, k[small]) <= 0)) small = i; });
        k[big] = Radd(k[big], k[small]);
        k.splice(small, 1);
      }
      var top = k.reduce(function (a, x) { return Rcmp(x, a) > 0 ? x : a; }, k[0]), total = capSum(k);
      rows.push({ t: t, count: k.length, top: top, total: total, share: Rdiv(top, total) });
    }
    return rows;
  }
  function acCompute(view, inst, U, opts) {
    var M = function (x) { return capMoney(x, U.money); }, N = capNumText;
    if (view === 'simple') {
      var y = Rdiv(inst.capital, inst.consumed_per_year);
      return { tiles: { acYears: N(y) + (Requ(y, R1) ? ' year' : ' years') },
        status: 'A capital of ' + M(inst.capital) + ', with ' + M(inst.consumed_per_year) + ' of surplus value consumed each year, '
          + 'has consumed a sum equal to itself after ' + N(y) + ' years; on Marx\'s reckoning what remains is capitalised surplus value.',
        table: null };
    }
    if (view === 'centralise') {
      var rows = acCentralise(inst.capitals, inst.growth, inst.merge_rule === 'largest-absorbs-smallest', opts.periods);
      var last = rows[rows.length - 1];
      return { tiles: { acTopShare: capPct(last.share), acCount: String(last.count) },
        status: 'After ' + opts.periods + ' period' + (opts.periods === 1 ? '' : 's') + ' ' + last.count + ' capital'
          + (last.count === 1 ? '' : 's') + ' remain and the largest holds ' + capPct(last.share) + ' of the total, ' + M(last.total) + '.',
        table: { caption: 'Capitals period by period', head: ['period', 'capitals', 'largest', 'total', 'largest\'s share'],
          rows: rows.map(function (r) { return [String(r.t), String(r.count), M(r.top), M(r.total), capPct(r.share)]; }) } };
    }
    if (view === 'colony') {
      var free = Rzero(inst.land_price_years), never = !free && Rzero(inst.saving_share);
      var years = free || never ? R0 : Rdiv(inst.land_price_years, inst.saving_share), crows = [];
      for (var t = 1; t <= opts.periods; t += 1) {
        var left = never || (!free && Rcmp(R(BigInt(t - 1)), years) < 0) ? inst.colonists : R0;
        crows.push([String(t), N(left)]);
      }
      return { tiles: { acReserve: crows[crows.length - 1][1], acYearsToLand: never ? 'never' : N(years) + (Requ(years, R1) ? ' year' : ' years') },
        status: (free ? 'Land is free, so every one of the ' + N(inst.colonists) + ' colonists can leave wage-labour at once.'
          : (never ? 'No worker can save, so none can ever buy land.'
          : 'Land costs ' + N(inst.land_price_years) + ' years\' wages; saving ' + N(inst.saving_share) + ' of the wage, a worker needs '
            + N(years) + ' years to buy it, and works for wages until then.'))
          + ' A capital of ' + M(inst.capital) + ' finds ' + crows[crows.length - 1][1] + ' workers for hire in period ' + opts.periods + '.',
        table: { caption: 'Workers for hire, period by period', head: ['period', 'workers for hire'], rows: crows } };
    }
    if (view === 'thrift') {
      var perDay = Rmul(inst.wage, inst.saving_share);
      if (Rzero(perDay)) return { tiles: { acDaysToTarget: 'never' }, status: 'Saving nothing, the worker never reaches ' + M(inst.target) + '.', table: null };
      var days = Rdiv(inst.target, perDay);
      return { tiles: { acDaysToTarget: N(days) + ' working days' },
        status: 'Saving ' + N(inst.saving_share) + ' of a wage of ' + M(inst.wage) + ' is ' + M(perDay) + ' a day; '
          + M(inst.target) + ' takes ' + N(days) + ' working days.', table: null };
    }
    var tracked = view !== 'expand';
    var o = { capital: inst.capital, cv: inst.c_v, rise: inst.composition_rise || R0, sRate: inst.s_rate,
              share: inst.accumulate_share, periods: opts.periods, threshold: inst.invest_threshold || R0,
              wage: tracked ? inst.wage_per_worker : null, wageGrowth: inst.wage_growth || R0,
              supply: tracked ? inst.labour_supply : null, growth: inst.supply_growth || R0 };
    var run = acRun(o), end = run[run.length - 1], tiles = { acCapital: M(end.Kend) };
    var head = ['period', 'capital', 'c/v', 'c', 'v', 's', 'added'];
    if (tracked) head = head.concat(['employed', 'supply', 'reserve', 'wage']);
    var trows = run.map(function (r) {
      var row = [String(r.t), M(r.K), N(r.cv), M(r.c), M(r.v), M(r.s), M(r.added)];
      return tracked ? row.concat([N(r.employed), N(r.supply), N(r.reserve), M(r.wage)]) : row;
    });
    var said = 'Starting from ' + M(inst.capital) + ' at c/v = ' + N(inst.c_v) + ' and s/v = ' + N(inst.s_rate) + ', adding a share of '
      + N(inst.accumulate_share) + ' of s to capital, the capital is ' + M(end.Kend) + ' after ' + opts.periods
      + ' period' + (opts.periods === 1 ? '' : 's') + '.';
    if (!tracked) {
      tiles.acShareOriginal = capPct(Rdiv(inst.capital, end.Kend));
      tiles.acHoard = M(end.hoard);
      said += ' The original capital is ' + capPct(Rdiv(inst.capital, end.Kend)) + ' of it; the rest is capitalised surplus value.'
        + (Rsign(end.hoard) > 0 ? ' ' + M(end.hoard) + ' is held as a hoard, below the ' + M(inst.invest_threshold)
          + ' that can be invested at once.' : '');
    } else {
      if (Rzero(end.employed)) return { refuse: 'Nobody is employed in the last period' };
      tiles.acDemand = N(end.employed);
      tiles.acReserve = N(end.reserve);
      tiles.acRatio = capPct(Rdiv(end.reserve, end.employed));
      said += ' In the last period v employs ' + N(end.employed) + ' of ' + N(end.supply) + ' workers available at a wage of '
        + M(end.wage) + ', leaving a reserve of ' + N(end.reserve) + '. When demand exceeds the supply the lab raises the wage to '
        + 'v over the supply, and the extra wages come out of s.';
    }
    return { tiles: tiles, status: said, table: { caption: 'Accumulation period by period', head: head, rows: trows } };
  }
"""

ACCUMULATE_FIELDS = {
    "capital": ("Capital", "pos", None),
    "consumed_per_year": ("Surplus value consumed each year", "pos", None),
    "c_v": ("c/v, the composition of capital", "nn", None),
    "s_rate": ("s/v, the rate of surplus value (1 is 100%)", "nn", None),
    "accumulate_share": ("Share of s added to capital", "share", None),
    "invest_threshold": ("Least sum that can be invested (smaller sums are hoarded)", "nn", 0),
    "composition_rise": ("Added to c/v each period", "nn", 0),
    "labour_supply": ("Workers available in the first period", "pos", None),
    "supply_growth": ("Workers added to the supply each period", "nn", 0),
    "wage_per_worker": ("Wage per worker per period", "pos", None),
    "wage_growth": ("Added to the wage each period", "nn", 0),
    "capitals": ("Capitals, separated by commas", ("nums", "pos", 1, 10), None),
    "merge_rule": ("Merging (largest-absorbs-smallest or none)", ("word", ["largest-absorbs-smallest", "none"]), None),
    "growth": ("Growth of every capital each period (1/10 is 10%)", "nn", 0),
    "colonists": ("Colonists brought out as workers", "nncount", None),
    "land_price_years": ("Price of land, in years of wages (0 is free land)", "nn", None),
    "saving_share": ("Share of the wage a worker saves", "share", None),
    "wage": ("Daily wage", "pos", None),
    "target": ("The capital to be saved", "pos", None),
}

_AC_GROW = ["capital", "c_v", "s_rate", "accumulate_share"]

ACCUMULATE_VIEWS = {
    "simple": dict(fields=["capital", "consumed_per_year"], tiles=[("Years to consume a sum equal to the capital", "acYears")]),
    "expand": dict(fields=_AC_GROW + ["invest_threshold"], periods=True,
                   tiles=[("Capital at the end", "acCapital"), ("The original capital's share", "acShareOriginal"),
                          ("Held as a hoard", "acHoard")]),
    "labour": dict(fields=_AC_GROW + ["labour_supply", "supply_growth", "wage_per_worker"], periods=True,
                   tiles=[("Workers employed, last period", "acDemand"), ("Reserve, last period", "acReserve"),
                          ("Capital at the end", "acCapital")]),
    "composition": dict(fields=_AC_GROW + ["composition_rise", "labour_supply", "supply_growth", "wage_per_worker"],
                        periods=True,
                        tiles=[("Workers employed, last period", "acDemand"), ("Reserve, last period", "acReserve")]),
    "law": dict(fields=_AC_GROW + ["composition_rise", "labour_supply", "supply_growth", "wage_per_worker", "wage_growth"],
                periods=True,
                tiles=[("Reserve over employed, last period", "acRatio"), ("Reserve, last period", "acReserve"),
                       ("Workers employed, last period", "acDemand")]),
    "centralise": dict(fields=["capitals", "merge_rule", "growth"], periods=True,
                       tiles=[("The largest capital's share", "acTopShare"), ("Capitals left", "acCount")]),
    "colony": dict(fields=["capital", "colonists", "land_price_years", "saving_share"], periods=True,
                   tiles=[("Workers for hire, last period", "acReserve"), ("Years of work to buy land", "acYearsToLand")]),
    "thrift": dict(fields=["wage", "saving_share", "target"], tiles=[("Saving it takes", "acDaysToTarget")]),
}

# ---------------------------------------------------------------------------
# The modes
# ---------------------------------------------------------------------------

# mode: (prefix, JS, fn, fields, views, allowed money units, default unit,
#        title, subtitle, panel title, panel intro, check)
_MODES = {
    "value": ("va", VALUE_JS, "vaCompute", VALUE_FIELDS, VALUE_VIEWS, ("hours",), "hours",
              "Value as socially necessary labour-time", "hours per unit, averaged over every producer",
              "Change the producers, their hours or the lot",
              "Every figure is computed from the hours and outputs as typed.", None),
    "form": ("fo", FORM_JS, "foCompute", FORM_FIELDS, FORM_VIEWS, ("hours",), "hours",
             "The form of value", "one set of labour-values, written four ways",
             "Change the commodities, their hours or the equivalent",
             "Each quantity in an equation is computed from the hours in each lot.", _form_check),
    "money": ("mo", MONEY_JS, "moCompute", MONEY_FIELDS, MONEY_VIEWS, cc.MONEY_UNITS, "£",
              "Money and its circulation", "prices from values, and the money a day's sales need",
              "Change the values, the velocity or the payments",
              "Every sum is computed from the figures as typed, in the lesson's unit of money.", _money_check),
    "circuit": ("ci", CIRCUIT_JS, "ciCompute", CIRCUIT_FIELDS, CIRCUIT_VIEWS, cc.MONEY_UNITS, "£",
                "The circuit of capital", "what circulation adds, and what it does not",
                "Change the sums", "Every sum is computed from the figures as typed.", None),
    "surplus": ("su", SURPLUS_JS, "suCompute", SURPLUS_FIELDS, SURPLUS_VIEWS, cc.MONEY_UNITS, "s",
                "Surplus value", "c + v + s, computed from the figures Marx gives",
                "Change the capital, the wage or the hours",
                "Every figure is exact; a rate prints as a fraction and its percentage.", None),
    "workday": ("wd", WORKDAY_JS, "wdCompute", WORKDAY_FIELDS, WORKDAY_VIEWS, ("hours",), "hours",
                "The working day", "one day cut at the necessary labour-time",
                "Change the day, the necessary time or the factors",
                "The bar is drawn from the same exact figures the tiles print.", None),
    "machine": ("ma", MACHINE_JS, "maCompute", MACHINE_FIELDS, MACHINE_VIEWS, cc.MONEY_UNITS, "£",
                "Co-operation, manufacture and machinery", "what shared means, detail labour and machines change",
                "Change the workers, the steps or the machine",
                "No co-operation gain is typed in: the lab computes only what follows from the figures.", None),
    "wages": ("wa", WAGES_JS, "waCompute", WAGES_FIELDS, WAGES_VIEWS, cc.MONEY_UNITS, "s",
              "Wages", "the value of labour-power in the form of a price of labour",
              "Change the wage, the hours or the pieces", "Every sum is exact, in the lesson's unit of money.", None),
    "accumulate": ("ac", ACCUMULATE_JS, "acCompute", ACCUMULATE_FIELDS, ACCUMULATE_VIEWS, cc.MONEY_UNITS, "£",
                   "Accumulation", "capital period by period, and the labour it employs",
                   "Change the capital, the rates or the periods",
                   "Each period is computed from the one before, exactly; at most 10 periods.", None),
}

MODES = tuple(_MODES)
B_MODES = ("turnover", "schemes", "profit", "prices", "tendency", "interest", "rent", "revenue")


def _mode_lab(cfg, mode):
    (prefix, js, fn, fields, views, allowed, default_unit, title, subtitle,
     panel_title, panel_intro, check) = _MODES[mode]
    kit = "%s/%s" % (KIT, mode)
    view = cc.pick_view(cfg, kit, list(views))
    spec = views[view]
    kit = "%s/%s/%s" % (KIT, mode, view)
    money, qty = cc.units(cfg, kit, allowed, default_unit)
    field_rows = [(key,) + fields[key] for key in spec["fields"]]
    n_periods = cc.periods(cfg, kit) if spec.get("periods") else None
    if not spec.get("periods") and "periods" in cfg:
        raise ValueError("%s: this view does not iterate, so cfg['periods'] means nothing here" % kit)
    stray = [k for k in ("stage", "hold", "test") if k in cfg and k not in [r[0] for r in spec.get("redraw", [])]]
    if stray:
        raise ValueError("%s: cfg sets %s, which this view has no control for" % (kit, ", ".join(stray)))
    return cc.mode_lab(cfg, kit=kit, prefix=prefix, view=view, fields=field_rows, tiles=spec["tiles"],
                       mode_js=js, fn=fn, money=money, qty=qty, title=title, subtitle=subtitle,
                       panel_title=panel_title, panel_intro=panel_intro, redraw=spec.get("redraw", []),
                       n_periods=n_periods, bar=(mode == "workday"), check=check)


def capkit_lab(cfg):
    """The Capital kit. `cfg["mode"]` chooses the mode; an unknown mode or view raises.

    Nine modes are built here; the other eight are capkit_b's, imported only
    when asked for, so this half runs whether or not that file exists yet.
    """
    cfg = cfg or {}
    mode = cfg.get("mode")
    if mode in _MODES:
        return _mode_lab(cfg, mode)
    if mode in B_MODES:
        from . import capkit_b
        return capkit_b.capkit_b_lab(cfg)
    raise ValueError("capkit_lab: unknown mode %r; the seventeen modes are %s"
                     % (mode, ", ".join(MODES + B_MODES)))
