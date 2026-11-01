"""dddkit -- the lab kit of Domain-Driven Design, Read Along.

Specified in docs/domain-driven-design/PLAN.md sections 0 and D; the report an
author configures a lesson from is docs/domain-driven-design/kit-report.md,
and the seam between this module and dddkit_b.py is
docs/domain-driven-design/kit-contract.md. Built on eakit_core (imported as
`ea`, unchanged): its field parser, printers, markup and wiring, with two
field kinds of this kit's own (records with a variable tail, and a
specification box) read by `dddRead` before eakit's `eaField`.

Family A (this module), words, objects and rules:

  lang       (dln)  glossary, cognates
  assoc      (das)  simplify
  identity   (did)  equality, sharing
  aggregate  (dgr)  boundary, lock
  spec       (dsp)  validate, select, subsume

Family B (dddkit_b.py): modules, context, distill, ledger. `dddkit_lab`
dispatches them through `dddkit_b.MODES`.

THE BUILDER SIGNATURE (both families). A mode is built by
`builder(cfg) -> common.Lab`, where cfg is the lesson's lab cfg as written
(cfg["mode"] names the mode). Every builder in this kit is
`lambda cfg: mode_lab(cfg, <mode>, <SPEC>)`, and `mode_lab` takes itakit's
spec dict (kit-contract.md section 2). The first view is the default. A page
ships RATIONAL_JS, EA_CORE_JS, DDD_CORE_JS, its mode's base block and its
own view's block -- never the other views or modes (page weight).

IDS. PLAN section D's prefixes, except `dag`, which other kits use
(dagRelax, dagSchedule), so the aggregate mode is `dgr`. Shared helpers begin
ddd / DDD_. Grepped against scripts/mathpath/labs/*.py and scripts/*.js on
2026-11-01.

EXACTNESS. Every figure is a count, a list, or an exact BigInt rational;
nothing typed is evaluated as script. The spec mode's expressions are read by
this kit's own lexer and parser, mirrored in Python so a preset the page
would refuse fails the build.
"""

import re
from fractions import Fraction

from . import eakit_core as ea
from .algebra_core import RATIONAL_JS
from .common import Lab, cfg_literal

KIT = "dddkit"
CAUTION = "the count is of the model stated"
FAMILY_SENTENCE = "A count over the small model the lesson states."

# ---------------------------------------------------------------------------
# Shared JavaScript, on every dddkit page (both families)
# ---------------------------------------------------------------------------

DDD_CORE_JS = r"""
  /* dddkit's shared helpers (docs/domain-driven-design/kit-contract.md). */
  var DDD_CAUTION = 'the count is of the model stated';
  var DDD_WORD = /^[A-Za-z][A-Za-z0-9._-]*$/;
  function dddStatus(s) { return String(s).replace(/[.\s]+$/, '') + '; ' + DDD_CAUTION + '.'; }
  function dddKey(s) { return String(s).toLowerCase(); }
  function dddQ(r) { return Rint(r) ? eaInt(r.n) : eaInt(r.n) + '/' + eaInt(r.d); }
  /* A rational that has a finite decimal, as typed: 3, 0.25, −1.5 (no grouping). */
  function dddDec(r) {
    var neg = r.n < 0n, n = neg ? -r.n : r.n, whole = n / r.d, rem = n % r.d, frac = '', i;
    for (i = 0; i < 12 && rem !== 0n; i += 1) { rem *= 10n; frac += String(rem / r.d); rem %= r.d; }
    return (neg ? EA_MINUS : '') + String(whole) + (frac ? '.' + frac : '') + (rem !== 0n ? '…' : '');
  }
  /* An attribute value: {kind: 'num', r} for a decimal, {kind: 'word', w} for a
     word beginning with a letter. THROWS a sentence otherwise. */
  function dddValue(text, what) {
    var s = eaClean(text), m = EA_NUMBER.exec(s), r;
    if (s === '') throw new Error(what + ' is empty');
    if (m) {
      if ((m[1] || m[2] || '').length > 6) throw new Error(what + ' has more than 6 decimal places');
      r = Rparse(s);
      if (Rcmp(Rabs(r), R(10000000n)) > 0) throw new Error(what + ' is at most 10,000,000 in size, and it is ' + s.replace('-', EA_MINUS));
      return { kind: 'num', r: r };
    }
    if (DDD_WORD.test(s)) return { kind: 'word', w: s };
    throw new Error(what + ' ' + eaQuote(s) + ' should be a number such as 3 or 0.25, or a word that begins with a letter (letters, digits, dots, hyphens, underscores)');
  }
  function dddValText(v) { return v.kind === 'num' ? dddDec(v.r) : v.w; }
  function dddValEq(a, b) { return a.kind === b.kind && (a.kind === 'num' ? Requ(a.r, b.r) : a.w === b.w); }
  /* Records whose first cells follow f.sub and whose remaining cells (f.loRest
     to f.hiRest of them) each follow f.rest, or are key=value pairs. */
  function dddVrec(text, f, what) {
    var s = eaClean(text), rows = s === '' ? [] : s.split(';').map(function (r) { return r.trim(); });
    if (rows.length && rows[rows.length - 1] === '') rows.pop();
    eaSized(rows.length, f, what, 'records');
    var seen = {}, n = f.sub.length;
    return rows.map(function (row, i) {
      var cells = row.split(',').map(function (c) { return c.trim(); }), k = cells.length - n, w = what + ', record ' + (i + 1);
      if (k < f.loRest || k > f.hiRest) {
        var need = f.loRest === f.hiRest ? String(n + f.loRest) : (n + f.loRest) + ' to ' + (n + f.hiRest);
        throw new Error(w + ' has ' + cells.length + ' field' + (cells.length === 1 ? '' : 's') + '; this list needs ' + need
          + ' (' + f.sub.map(function (kk) { return kk[0]; }).join(', ') + ', then ' + f.restWhat + ')');
      }
      var rec = {}, keys = {};
      f.sub.forEach(function (kk, j) { rec[kk[0]] = eaScalar(kk[1], cells[j], w + ': ' + kk[0]); });
      rec.rest = cells.slice(n).map(function (c, j) {
        var ww = w + ': ' + f.restWhat + ' ' + (j + 1);
        if (f.rest.kind !== 'kv') return eaScalar(f.rest, c, ww);
        var m = /^([^=\s]+)\s*=\s*([^=\s]+)$/.exec(c);
        if (!m || !DDD_WORD.test(m[1])) throw new Error(ww + ': ' + eaQuote(c) + ' should be name=value, such as pages=320 or genre=crime, the name beginning with a letter');
        if (Object.prototype.hasOwnProperty.call(keys, m[1])) throw new Error(w + ' gives ' + m[1] + ' twice');
        keys[m[1]] = true;
        return { k: m[1], v: dddValue(m[2], ww + ' (' + m[1] + ')') };
      });
      if (f.unique) {
        if (Object.prototype.hasOwnProperty.call(seen, cells[0])) throw new Error(what + ' names ' + eaQuote(cells[0]) + ' twice');
        seen[cells[0]] = true;
      }
      return rec;
    });
  }
  function dddExpr(text, what) {
    var s = eaClean(text).replace(/\s+/g, ' ');
    if (s === '') throw new Error(what + ' is empty');
    if (s.length > 300) throw new Error(what + ' has ' + s.length + ' characters; this lab reads at most 300');
    return s;
  }
  function dddRead(spec, raw) {
    var out = {};
    spec.forEach(function (f) {
      if (f.kind === 'vrec') out[f.key] = dddVrec(raw[f.key], f, f.what);
      else if (f.kind === 'expr') out[f.key] = dddExpr(raw[f.key], f.what);
      else out[f.key] = eaField(f, raw[f.key]);
    });
    return out;
  }
  /* "n: a; b" with "0: none". */
  function dddListed(n, parts, sep) { return n === 0 ? '0: none' : eaInt(n) + ': ' + parts.join(sep || ', '); }
"""

# ---------------------------------------------------------------------------
# lang (dln): a glossary across audiences, and terms across contexts
# ---------------------------------------------------------------------------

DLN_JS = r"""
  var DLN_VIEW = {};
  function dlnCompute(view, inst, opts) { return eaRun(DLN_VIEW[view], inst, opts); }
"""

DLN_VIEW_JS = {}

DLN_VIEW_JS["glossary"] = r"""
  DLN_VIEW.glossary = function (inst) {
    var aud = inst.audiences, k = aud.length, terms = inst.terms;
    terms.forEach(function (t, i) {
      if (t.rest.length !== k) eaRefuse('Terms, record ' + (i + 1) + ' (' + t.concept + ') gives ' + eaPlural(t.rest.length, 'name', 'names')
        + '; there are ' + k + ' audiences (' + aud.join(', ') + '), so each record needs ' + k + ' names, - where an audience has none');
    });
    var alike = [], trans = 0, missing = 0, missParts = [], used = aud.map(function () { return { order: [], by: {} }; }), rows = [];
    var missBy = aud.map(function () { return []; });
    terms.forEach(function (t) {
      var names = t.rest, diff = [], gap = false;
      names.forEach(function (nm, a) {
        if (nm === '-') { gap = true; missing += 1; missBy[a].push(t.concept); return; }
        var key = dddKey(nm), u = used[a];
        if (!u.by[key]) { u.by[key] = { name: nm, list: [] }; u.order.push(key); }
        u.by[key].list.push(t.concept);
      });
      for (var a = 0; a < k; a += 1) {
        for (var b = a + 1; b < k; b += 1) {
          if (names[a] !== '-' && names[b] !== '-' && dddKey(names[a]) !== dddKey(names[b])) { diff.push(aud[a] + '↔' + aud[b]); trans += 1; }
        }
      }
      if (!gap && diff.length === 0) alike.push(t.concept);
      rows.push([t.concept].concat(names.map(function (nm) { return nm === '-' ? EA_DASH : nm; }),
        [diff.length ? diff.join(', ') : (gap ? 'none named by both' : 'none')]));
    });
    missBy.forEach(function (list, a) { if (list.length) missParts.push(list.join(', ') + ' (' + aud[a] + ')'); });
    var amb = [];
    used.forEach(function (u, a) {
      u.order.forEach(function (key) { var e = u.by[key]; if (e.list.length > 1) amb.push(e.name + ' (' + aud[a] + ': ' + e.list.join(', ') + ')'); });
    });
    return {
      tiles: {
        dlnConcepts: eaInt(terms.length), dlnAlike: eaCount(alike), dlnTranslations: eaInt(trans),
        dlnMissing: dddListed(missing, missParts, '; '), dlnAmbiguous: dddListed(amb.length, amb, '; ')
      },
      status: dddStatus(eaPlural(terms.length, 'concept', 'concepts') + ' across ' + k + ' audiences: a conversation that touches each concept once needs '
        + eaPlural(trans, 'translation', 'translations') + ', ' + eaPlural(missing, 'name is', 'names are') + ' missing and '
        + eaPlural(amb.length, 'name stands', 'names stand') + ' for more than one concept'),
      table: { caption: 'Each concept as each audience names it; the last column lists the pairs of audiences whose names differ (letter case ignored)',
               head: ['concept'].concat(aud, ['names differ']), rows: rows }
    };
  };
"""

DLN_VIEW_JS["cognates"] = r"""
  DLN_VIEW.cognates = function (inst) {
    var recs = inst.contexts, ctx = [], terms = {}, torder = [], means = {}, morder = [], seen = {};
    recs.forEach(function (r, i) {
      var tk = dddKey(r.term), pair = r.context + '\u0000' + tk;
      if (seen[pair]) eaRefuse('Terms by context, record ' + (i + 1) + ': ' + r.context + ' gives the term ' + r.term
        + ' twice; give each term one meaning in each context');
      seen[pair] = true;
      if (ctx.indexOf(r.context) < 0) ctx.push(r.context);
      if (!terms[tk]) { terms[tk] = { name: r.term, ctx: [], by: {} }; torder.push(tk); }
      terms[tk].ctx.push(r.context); terms[tk].by[r.context] = r.meaning;
      var mk = dddKey(r.meaning);
      if (!means[mk]) { means[mk] = { name: r.meaning, terms: [], by: {} }; morder.push(mk); }
      if (!means[mk].by[tk]) { means[mk].by[tk] = { name: r.term, ctx: [] }; means[mk].terms.push(tk); }
      means[mk].by[tk].ctx.push(r.context);
    });
    if (ctx.length < 2) eaRefuse('Every record is in the context ' + ctx[0] + '; cognates are counted across two or more contexts');
    var shared = [], falses = [], safe = [], dups = [], rows = [];
    torder.forEach(function (tk) {
      var t = terms[tk], verdict = 'in one context';
      if (t.ctx.length > 1) {
        shared.push(t.name);
        var ms = [];
        t.ctx.forEach(function (c) { var m = dddKey(t.by[c]); if (ms.indexOf(m) < 0) ms.push(m); });
        if (ms.length > 1) {
          falses.push(t.name + ' (' + t.ctx.map(function (c) { return c + ': ' + t.by[c]; }).join(', ') + ')');
          verdict = 'false cognate';
        } else { safe.push(t.name); verdict = 'safe to share'; }
      }
      rows.push([t.name].concat(ctx.map(function (c) { return t.by[c] === undefined ? EA_DASH : t.by[c]; }), [verdict]));
    });
    morder.forEach(function (mk) {
      var m = means[mk];
      if (m.terms.length > 1) dups.push(m.name + ': ' + m.terms.map(function (tk) { var e = m.by[tk]; return e.name + ' (' + e.ctx.join(', ') + ')'; }).join(', '));
    });
    return {
      tiles: {
        dlnContexts: eaCount(ctx), dlnTerms: eaInt(torder.length), dlnShared: eaCount(shared),
        dlnFalse: dddListed(falses.length, falses, '; '), dlnDuplicate: dddListed(dups.length, dups, '; '), dlnSafe: eaCount(safe)
      },
      status: dddStatus(eaPlural(torder.length, 'term', 'terms') + ' in ' + ctx.length + ' contexts: ' + shared.length + ' shared, of which '
        + eaPlural(falses.length, 'is a false cognate', 'are false cognates') + ' and ' + safe.length + ' safe to share; '
        + eaPlural(dups.length, 'concept carries', 'concepts carry') + ' more than one term'),
      table: { caption: 'Each term and what it means in each context (letter case ignored)',
               head: ['term'].concat(ctx, ['verdict']), rows: rows }
    };
  };
"""


def _fold(s):
    return str(s).lower()


def _check_glossary(inst, fixed):
    k = len(inst["audiences"])
    for i, t in enumerate(inst["terms"]):
        if len(t["rest"]) != k:
            raise ValueError("Terms, record %d (%s) gives %s; there are %d audiences (%s), so each record needs %d "
                             "names, - where an audience has none"
                             % (i + 1, t["concept"], _plural(len(t["rest"]), "name", "names"), k,
                                ", ".join(inst["audiences"]), k))


def _check_cognates(inst, fixed):
    seen, ctx = set(), []
    for i, r in enumerate(inst["contexts"]):
        pair = (r["context"], _fold(r["term"]))
        if pair in seen:
            raise ValueError("Terms by context, record %d: %s gives the term %s twice; give each term one meaning in "
                             "each context" % (i + 1, r["context"], r["term"]))
        seen.add(pair)
        if r["context"] not in ctx:
            ctx.append(r["context"])
    if len(ctx) < 2:
        raise ValueError("Every record is in the context %s; cognates are counted across two or more contexts" % ctx[0])


# ---------------------------------------------------------------------------
# assoc (das): simplifying associations
# ---------------------------------------------------------------------------

DAS_JS = r"""
  var DAS_VIEW = {};
  function dasCompute(view, inst, opts) { return eaRun(DAS_VIEW[view], inst, opts); }
  /* One association after its qualifier: the ends ['1'|'n', '1'|'n'] and the
     counts. THROWS (refuses) a qualifier on an end that is already one. */
  function dasOne(r, list, i) {
    var e = r.ends.split('-'), q = '', at;
    if (r.qualified === 'yes') {
      at = r.direction === 'a-b' ? 1 : (r.direction === 'b-a' ? 0 : (e[1] === 'n' ? 1 : 0));
      if (e[at] !== 'n') {
        eaRefuse(list + ', record ' + (i + 1) + ' (' + r.a + '–' + r.b + '): a qualifier reduces the many end it navigates to, and the '
          + (at === 1 ? r.b : r.a) + ' end of ' + r.ends + ' ' + r.direction + ' is already one');
      }
      e[at] = '1'; q = 'yes (' + (at === 1 ? r.b : r.a) + ' end to one)';
    }
    var both = r.direction === 'both';
    return { ends: e.join('-'), dirs: both ? 2 : 1, two: both ? 1 : 0, nn: e[0] === 'n' && e[1] === 'n' ? 1 : 0,
             many: (e[0] === 'n' ? 1 : 0) + (e[1] === 'n' ? 1 : 0), q: q || 'no',
             nav: both ? r.a + '↔' + r.b : (r.direction === 'a-b' ? r.a + '→' + r.b : r.b + '→' + r.a) };
  }
  function dasCount(list, what, rows) {
    var c = { n: list.length, dirs: 0, two: 0, nn: 0, many: 0 };
    list.forEach(function (r, i) {
      var o = dasOne(r, what, i);
      c.dirs += o.dirs; c.two += o.two; c.nn += o.nn; c.many += o.many;
      rows.push([what, r.a + '–' + r.b, r.ends, o.q, o.ends, o.nav, String(o.dirs), String(o.many)]);
    });
    return c;
  }
"""

DAS_VIEW_JS = {}

DAS_VIEW_JS["simplify"] = r"""
  DAS_VIEW.simplify = function (inst) {
    var rows = [], b = dasCount(inst.assocs, 'before', rows), has = inst.after.length > 0;
    var a = has ? dasCount(inst.after, 'after', rows) : null;
    var t = function (key) { return has ? eaInt(b[key]) + ' → ' + eaInt(a[key]) : eaInt(b[key]); };
    var change = has ? [['n', 'associations'], ['dirs', 'navigable directions'], ['two', 'two-way'], ['nn', 'many-to-many'], ['many', 'many ends']]
      .map(function (p) { return eaSigned(a[p[0]] - b[p[0]]) + ' ' + p[1]; }).join(', ') : 'no after list given';
    return {
      tiles: { dasAssocs: t('n'), dasDirections: t('dirs'), dasTwoWay: t('two'), dasManyMany: t('nn'), dasManyEnds: t('many'), dasChange: change },
      status: dddStatus(has ? 'Before: ' + eaPlural(b.dirs, 'navigable direction', 'navigable directions') + ' and ' + eaPlural(b.two, 'association', 'associations')
        + ' to keep in step both ways; after: ' + eaInt(a.dirs) + ' and ' + eaInt(a.two)
        : eaPlural(b.n, 'association', 'associations') + ': ' + eaPlural(b.dirs, 'navigable direction', 'navigable directions') + ', '
          + eaInt(b.two) + ' kept in step both ways, ' + eaInt(b.nn) + ' many-to-many'),
      table: { caption: 'Each association, as written and after its qualifier', head: ['list', 'association', 'ends', 'qualified', 'ends after', 'navigable', 'directions', 'many ends'], rows: rows }
    };
  };
"""


def _check_assoc_list(lst, what):
    for i, r in enumerate(lst):
        if r["qualified"] != "yes":
            continue
        e = r["ends"].split("-")
        at = 1 if r["direction"] == "a-b" else 0 if r["direction"] == "b-a" else (1 if e[1] == "n" else 0)
        if e[at] != "n":
            raise ValueError("%s, record %d (%s–%s): a qualifier reduces the many end it navigates to, and the %s end of "
                             "%s %s is already one" % (what, i + 1, r["a"], r["b"], r["b"] if at == 1 else r["a"],
                                                      r["ends"], r["direction"]))


def _check_simplify(inst, fixed):
    _check_assoc_list(inst["assocs"], "before")
    _check_assoc_list(inst["after"], "after")


# ---------------------------------------------------------------------------
# identity (did): equality, and sharing a value
# ---------------------------------------------------------------------------

DID_JS = r"""
  var DID_VIEW = {};
  function didCompute(view, inst, opts) { return eaRun(DID_VIEW[view], inst, opts); }
"""

DID_VIEW_JS = {}

DID_VIEW_JS["equality"] = r"""
  DID_VIEW.equality = function (inst) {
    var objs = inst.objects, by = {}, pairs = [];
    objs.forEach(function (o) { var m = {}; o.rest.forEach(function (kv) { m[kv.k] = kv.v; }); by[o.name] = { id: o.id, attrs: o.rest, map: m }; });
    if (inst.pairs.length === 0) {
      if (objs.length > 12) eaRefuse('With no pairs given every pair is compared, which this lab does for at most 12 objects, and there are ' + objs.length + '; list the pairs to compare');
      for (var i = 0; i < objs.length; i += 1) for (var j = i + 1; j < objs.length; j += 1) pairs.push([objs[i].name, objs[j].name]);
    } else {
      var seenP = {};
      inst.pairs.forEach(function (p, i) {
        [p.x, p.y].forEach(function (nm) { if (!by[nm]) eaRefuse('Pairs, record ' + (i + 1) + ': ' + nm + ' is not one of the objects'); });
        if (p.x === p.y) eaRefuse('Pairs, record ' + (i + 1) + ' compares ' + p.x + ' with itself');
        var key = p.x < p.y ? p.x + '\u0000' + p.y : p.y + '\u0000' + p.x;
        if (seenP[key]) eaRefuse('Pairs, record ' + (i + 1) + ' compares ' + p.x + ' and ' + p.y + ' a second time');
        seenP[key] = true;
        pairs.push([p.x, p.y]);
      });
    }
    var sameId = [], sameAt = [], changed = [], looks = [], rows = [];
    pairs.forEach(function (p) {
      var x = by[p[0]], y = by[p[1]], name = '(' + p[0] + ', ' + p[1] + ')', diff = [];
      x.attrs.forEach(function (kv) { if (!y.map[kv.k] || !dddValEq(kv.v, y.map[kv.k])) diff.push(kv.k); });
      y.attrs.forEach(function (kv) { if (!x.map[kv.k]) diff.push(kv.k); });
      var ids = x.id !== '-' && y.id !== '-', idSame = ids && x.id === y.id, atSame = diff.length === 0, verdict = EA_DASH;
      if (idSame) sameId.push(name);
      if (atSame) sameAt.push(name);
      if (idSame && !atSame) { changed.push(name + ': ' + diff.join(', ')); verdict = 'changed'; }
      if (ids && !idSame && atSame) { looks.push(name); verdict = 'look-alikes'; }
      if (!ids) verdict = atSame ? 'equal values' : 'different values';
      rows.push([name, x.id === '-' ? 'none' : x.id, y.id === '-' ? 'none' : y.id,
        ids ? (idSame ? 'same' : 'different') : 'no identity', atSame ? 'same' : 'differ in ' + diff.join(', '), verdict]);
    });
    return {
      tiles: { didPairs: eaInt(pairs.length), didIdentity: eaCount(sameId), didAttrs: eaCount(sameAt),
               didChanged: dddListed(changed.length, changed, '; '), didLookalike: eaCount(looks) },
      status: dddStatus(eaPlural(pairs.length, 'pair', 'pairs') + ' compared: identity and attributes disagree on '
        + eaInt(changed.length + looks.length) + ' (' + changed.length + ' changed, ' + looks.length + ' look-alike)'),
      table: { caption: 'Each pair, by identity and by attributes', head: ['pair', 'id', 'id', 'by identity', 'by attributes', 'they disagree'], rows: rows }
    };
  };
"""

DID_VIEW_JS["sharing"] = r"""
  DID_VIEW.sharing = function (inst) {
    var hs = inst.holders, v = inst.value, ch = inst.change, of = [], who = null, rows = [];
    hs.forEach(function (h) { if (h.value === v) of.push(h.holder); if (h.holder === ch) who = h; });
    if (!of.length) eaRefuse('No holder holds ' + v + '; the shared value must be one the holders hold');
    if (!who) eaRefuse(ch + ' is not one of the holders; the change is made through a holder');
    if (who.value !== v) eaRefuse(ch + ' holds ' + who.value + ', not ' + v + '; the change must be made through a holder of ' + v);
    var mut = inst.kind === 'mutable', fresh = v + '′';
    var see = mut ? of.slice() : [ch], surprised = mut ? of.filter(function (h) { return h !== ch; }) : [];
    hs.forEach(function (h) {
      var holds = h.value === v, after = !mut && h.holder === ch ? fresh : h.value;
      rows.push([h.holder, h.value, after, holds && see.indexOf(h.holder) >= 0 ? 'yes' : 'no', h.holder === ch ? 'yes' : 'no',
        surprised.indexOf(h.holder) >= 0 ? 'yes' : 'no']);
    });
    return {
      tiles: { didHolders: eaCount(of), didSee: eaCount(see), didSurprised: eaCount(surprised),
               didNew: mut ? '0' : '1: ' + fresh + ', now held by ' + ch },
      status: dddStatus('A change to the ' + inst.kind + ' value ' + v + ' through ' + ch + ' is seen by '
        + eaPlural(see.length, 'holder', 'holders') + ', ' + eaInt(surprised.length) + ' of whom did not make it'),
      table: { caption: 'Each holder before and after the change', head: ['holder', 'holds before', 'holds after', 'sees the change', 'made it', 'surprised'], rows: rows }
    };
  };
"""


def _check_equality(inst, fixed):
    names = [o["name"] for o in inst["objects"]]
    if not inst["pairs"]:
        if len(names) > 12:
            raise ValueError("With no pairs given every pair is compared, which this lab does for at most 12 objects, "
                             "and there are %d; list the pairs to compare" % len(names))
        return
    seen = set()
    for i, p in enumerate(inst["pairs"]):
        for nm in (p["x"], p["y"]):
            if nm not in names:
                raise ValueError("Pairs, record %d: %s is not one of the objects" % (i + 1, nm))
        if p["x"] == p["y"]:
            raise ValueError("Pairs, record %d compares %s with itself" % (i + 1, p["x"]))
        key = tuple(sorted((p["x"], p["y"])))
        if key in seen:
            raise ValueError("Pairs, record %d compares %s and %s a second time" % (i + 1, p["x"], p["y"]))
        seen.add(key)


def _check_sharing(inst, fixed):
    v, ch = inst["value"], inst["change"]
    held = [h for h in inst["holders"] if h["value"] == v]
    who = [h for h in inst["holders"] if h["holder"] == ch]
    if not held:
        raise ValueError("No holder holds %s; the shared value must be one the holders hold" % v)
    if not who:
        raise ValueError("%s is not one of the holders; the change is made through a holder" % ch)
    if who[0]["value"] != v:
        raise ValueError("%s holds %s, not %s; the change must be made through a holder of %s"
                         % (ch, who[0]["value"], v, v))


# ---------------------------------------------------------------------------
# aggregate (dgr): boundaries, and locking
# ---------------------------------------------------------------------------

DGR_JS = r"""
  var DGR_VIEW = {};
  function dgrCompute(view, inst, opts) { return eaRun(DGR_VIEW[view], inst, opts); }
"""

DGR_VIEW_JS = {}

DGR_VIEW_JS["boundary"] = r"""
  DGR_VIEW.boundary = function (inst) {
    var objs = inst.objects, agg = {}, aggs = [], roots = {}, isObj = {};
    objs.forEach(function (o) {
      isObj[o.object] = o;
      if (!agg[o.aggregate]) { agg[o.aggregate] = []; aggs.push(o.aggregate); roots[o.aggregate] = []; }
      agg[o.aggregate].push(o.object);
      if (o.root === 'yes') roots[o.aggregate].push(o.object);
    });
    aggs.forEach(function (g) {
      if (roots[g].length === 0) eaRefuse('The aggregate ' + g + ' has no root; mark exactly one of its objects root yes');
      if (roots[g].length > 1) eaRefuse('The aggregate ' + g + ' has ' + roots[g].length + ' roots (' + roots[g].join(', ') + '); an aggregate has exactly one');
    });
    inst.refs.forEach(function (r, i) {
      if (!isObj[r.to]) eaRefuse('References, record ' + (i + 1) + ': ' + r.to + ' is not one of the objects; a reference points to an object (a name that is not an object may only hold references)');
    });
    var del = inst['delete'];
    if (del !== '-' && !isObj[del]) eaRefuse('The object to delete, ' + del + ', is not one of the objects');
    var crossing = 0, viol = [], removed = [], dangling = [], refused = '', rows = [];
    if (del !== '-') {
      var dg = isObj[del].aggregate;
      if (roots[dg][0] === del) removed = agg[dg].slice();
      else refused = del + ' is not the root of ' + dg + '; delete it through ' + roots[dg][0];
    }
    inst.refs.forEach(function (r) {
      var from = isObj[r.from], to = isObj[r.to], g = to.aggregate, inside = from && from.aggregate === g;
      var toRoot = roots[g][0] === r.to, verdict, after = '';
      if (inside) verdict = 'inside ' + g;
      else {
        crossing += 1;
        if (toRoot) verdict = 'crosses into ' + g + ', to its root';
        else { verdict = 'crosses into ' + g + ', to a non-root: violation'; viol.push(r.from + ' → ' + r.to); }
      }
      if (removed.length) {
        var fromGone = removed.indexOf(r.from) >= 0, toGone = removed.indexOf(r.to) >= 0;
        if (toGone && !fromGone) { after = 'left dangling'; dangling.push(r.from + ' → ' + r.to); }
        else if (fromGone) after = 'removed';
      }
      rows.push([r.from + ' → ' + r.to, from ? from.aggregate : 'outside', g + (toRoot ? ' (root)' : ''), verdict, after]);
    });
    var none = 'no delete given';
    return {
      tiles: {
        dgrAggregates: eaCount(aggs), dgrObjects: eaInt(objs.length), dgrCrossing: eaInt(crossing),
        dgrViolations: dddListed(viol.length, viol),
        dgrRemoves: del === '-' ? none : (refused ? 'refused: ' + refused : eaCount(removed)),
        dgrDangling: del === '-' ? none : (refused ? 'none: the delete is refused' : dddListed(dangling.length, dangling))
      },
      status: dddStatus(eaPlural(inst.refs.length, 'reference', 'references') + ', ' + crossing + ' crossing a boundary, '
        + eaPlural(viol.length, 'of them to a non-root', 'of them to non-roots')
        + (del === '-' ? '' : (refused ? '; the delete of ' + del + ' is refused' : '; deleting ' + del + ' removes '
          + eaPlural(removed.length, 'object', 'objects') + ' and leaves ' + eaInt(dangling.length) + ' dangling'))),
      table: { caption: 'Each reference and the boundary it meets', head: ['reference', 'from', 'into', 'verdict', 'after the delete'], rows: rows }
    };
  };
"""

DGR_VIEW_JS["lock"] = r"""
  DGR_VIEW.lock = function (inst) {
    var items = {}, order = [];
    inst.items.forEach(function (it) { items[it.item] = it.value; order.push(it.item); });
    inst.edits.forEach(function (e, i) {
      if (items[e.item] === undefined) eaRefuse('Edits, record ' + (i + 1) + ': ' + e.item + ' is not one of the items');
    });
    var users = [], U = {};
    inst.edits.forEach(function (e, i) {
      if (!U[e.user]) { U[e.user] = { name: e.user, first: i, commit: 0n, edits: [], pending: {}, porder: [], refused: '', locks: [] }; users.push(U[e.user]); }
      var u = U[e.user];
      if (e.minute.n > u.commit) u.commit = e.minute.n;
      u.edits.push(e);
    });
    var seq = inst.edits.map(function (e, i) { return { e: e, i: i }; });
    seq.sort(function (p, q) { var c = Rcmp(p.e.minute, q.e.minute); return c !== 0 ? c : p.i - q.i; });
    var agg = inst.scheme === 'aggregate', holder = {};
    var release = function (u) { Object.keys(holder).forEach(function (k) { if (holder[k] === u) delete holder[k]; }); };
    seq.forEach(function (p) {
      var e = p.e, u = U[e.user], m = e.minute.n;
      if (u.refused) return;
      users.forEach(function (w) { if (w !== u && !w.refused && w.commit < m) release(w); });
      var need = agg ? '*' : e.item, h = holder[need];
      if (h && h !== u) {
        u.refused = (agg ? 'the aggregate' : e.item) + ' held by ' + h.name + ' at minute ' + eaInt(m);
        u.refusedAt = m;
        release(u);
        return;
      }
      holder[need] = u;
      if (!Object.prototype.hasOwnProperty.call(u.pending, e.item)) u.porder.push(e.item);
      u.pending[e.item] = e.value;
    });
    var done = users.filter(function (u) { return !u.refused; });
    done.sort(function (a, b) { return a.commit < b.commit ? -1 : (a.commit > b.commit ? 1 : a.first - b.first); });
    var vals = {}, by = {}, lost = [];
    order.forEach(function (k) { vals[k] = items[k]; });
    done.forEach(function (u) {
      u.porder.forEach(function (k) {
        if (by[k]) lost.push(k + ' (' + by[k] + '’s)');
        vals[k] = u.pending[k]; by[k] = u.name;
      });
    });
    var sum = eaSum(order.map(function (k) { return vals[k]; })), ok = Rcmp(sum, inst.limit) <= 0;
    var rows = users.map(function (u) {
      var mine = {}; u.edits.forEach(function (e) { mine[e.item] = e.value; });
      var seenSum = eaSum(order.map(function (k) { return mine[k] !== undefined ? mine[k] : items[k]; }));
      return [u.name, u.edits.map(function (e) { return e.item + ' = ' + dddDec(e.value) + ' at ' + eaInt(e.minute.n); }).join(', '),
        dddDec(seenSum), u.refused ? 'refused: ' + u.refused : 'committed at minute ' + eaInt(u.commit)];
    });
    var refused = users.filter(function (u) { return u.refused; }).map(function (u) { return u.name + ' (' + u.refused + ')'; });
    return {
      tiles: {
        dgrCommitted: eaCount(users.filter(function (u) { return !u.refused; }).map(function (u) { return u.name; })), dgrRefused: dddListed(refused.length, refused, '; '),
        dgrFinal: order.map(function (k) { return k + ' = ' + dddDec(vals[k]); }).join(', '), dgrSum: dddDec(sum),
        dgrHolds: (ok ? 'yes: sum ' + dddDec(sum) + ' within limit ' : 'no: sum ' + dddDec(sum) + ' over limit ') + dddDec(inst.limit),
        dgrLost: dddListed(lost.length, lost)
      },
      status: dddStatus('Under ' + (agg ? 'an aggregate lock' : 'object locks') + ', ' + eaPlural(done.length, 'user commits', 'users commit') + ' and '
        + eaInt(refused.length) + ' ' + (refused.length === 1 ? 'is' : 'are') + ' refused; the invariant (sum ≤ ' + dddDec(inst.limit) + ') '
        + (ok ? 'holds' : 'is broken') + ' after the last commit'),
      table: { caption: 'Each user: the edits, the sum as that user saw it (minute 0 plus their own edits), and the outcome',
               head: ['user', 'edits', 'sum they saw', 'outcome'], rows: rows }
    };
  };
"""


def _check_boundary(inst, fixed):
    roots, isobj = {}, {}
    for o in inst["objects"]:
        isobj[o["object"]] = o
        roots.setdefault(o["aggregate"], [])
        if o["root"] == "yes":
            roots[o["aggregate"]].append(o["object"])
    for g, rs in roots.items():
        if not rs:
            raise ValueError("The aggregate %s has no root; mark exactly one of its objects root yes" % g)
        if len(rs) > 1:
            raise ValueError("The aggregate %s has %d roots (%s); an aggregate has exactly one" % (g, len(rs), ", ".join(rs)))
    for i, r in enumerate(inst["refs"]):
        if r["to"] not in isobj:
            raise ValueError("References, record %d: %s is not one of the objects; a reference points to an object (a "
                             "name that is not an object may only hold references)" % (i + 1, r["to"]))
    d = inst["delete"]
    if d != "-" and d not in isobj:
        raise ValueError("The object to delete, %s, is not one of the objects" % d)


def _check_lock(inst, fixed):
    items = {it["item"] for it in inst["items"]}
    for i, e in enumerate(inst["edits"]):
        if e["item"] not in items:
            raise ValueError("Edits, record %d: %s is not one of the items" % (i + 1, e["item"]))


# ---------------------------------------------------------------------------
# spec (dsp): specifications, read by the kit's own parser
# ---------------------------------------------------------------------------

DSP_JS = r"""
  var DSP_VIEW = {};
  function dspCompute(view, inst, opts) { return eaRun(DSP_VIEW[view], inst, opts); }
  var DSP_OPS = { '=': 1, '!=': 1, '<': 1, '<=': 1, '>': 1, '>=': 1 };
  var DSP_TOKEN = /^(?:\(|\)|!=|<=|>=|=|<|>|[A-Za-z0-9._-]+)/;
  function dspKw(t) { return t === 'and' || t === 'or' || t === 'not'; }
  /* Read a specification: {tree, clauses}; every clause {attr, cmp, val, text, n}.
     Refuses (never throws) on anything it cannot read. Nothing is evaluated. */
  function dspParse(text, what) {
    var toks = [], i = 0, m;
    while (i < text.length) {
      if (/\s/.test(text[i])) { i += 1; continue; }
      m = DSP_TOKEN.exec(text.slice(i));
      if (!m) eaRefuse(what + ' has ' + eaQuote(text[i]) + ' at character ' + (i + 1) + ', which this lab cannot read (it reads attribute op value, with = != < <= > >=, and, or, not and parentheses)');
      toks.push(m[0]); i += m[0].length;
    }
    var p = 0, clauses = [], depth = 0;
    var peek = function () { return p < toks.length ? toks[p] : null; };
    var orE, andE, notE, atom;
    orE = function () { var n = andE(); while (peek() === 'or') { p += 1; n = { op: 'or', a: n, b: andE() }; } return n; };
    andE = function () { var n = notE(); while (peek() === 'and') { p += 1; n = { op: 'and', a: n, b: notE() }; } return n; };
    notE = function () { if (peek() === 'not') { p += 1; return { op: 'not', a: notE() }; } return atom(); };
    atom = function () {
      var t = peek();
      if (t === null) eaRefuse(what + ' ends where a clause should be');
      if (t === '(') {
        p += 1; depth += 1;
        if (depth > 8) eaRefuse(what + ' nests parentheses more than 8 deep');
        var n = orE();
        if (peek() !== ')') eaRefuse(what + ' opens a parenthesis it never closes');
        p += 1; depth -= 1;
        return n;
      }
      if (t === ')' || DSP_OPS[t] || dspKw(t) || !DDD_WORD.test(t)) eaRefuse(what + ' has ' + eaQuote(t) + ' where an attribute name should be (a word beginning with a letter)');
      p += 1;
      var op = peek();
      if (op === null || !DSP_OPS[op]) eaRefuse(what + ': after ' + t + ' should come one of = != < <= > >=' + (op === null ? '' : ', not ' + eaQuote(op)));
      p += 1;
      var v = peek();
      if (v === null || v === '(' || v === ')' || DSP_OPS[v] || dspKw(v)) eaRefuse(what + ': ' + t + ' ' + op + ' needs a value, a number or a word');
      p += 1;
      var val;
      try { val = dddValue(v, what + ': the value in ' + t + ' ' + op + ' ' + v); } catch (e) { eaRefuse(e.message); }
      if (val.kind === 'word' && op !== '=' && op !== '!=') eaRefuse(what + ': ' + t + ' ' + op + ' ' + v + ' orders a word; a word compares only by = and !=');
      var c = { op: 'clause', attr: t, cmp: op, val: val, text: t + ' ' + op + ' ' + dddValText(val), n: clauses.length };
      clauses.push(c);
      if (clauses.length > 20) eaRefuse(what + ' has more than 20 clauses; this lab reads at most 20');
      return c;
    };
    var tree = orE();
    if (p < toks.length) eaRefuse(what + ' has ' + eaQuote(toks[p]) + ' after the specification ends');
    return { tree: tree, clauses: clauses };
  }
  /* Candidates as {name, attrs: {k: value}, order: [k]}. */
  function dspCands(list) {
    return list.map(function (c) { var a = {}; c.rest.forEach(function (kv) { a[kv.k] = kv.v; }); return { name: c.name, attrs: a }; });
  }
  /* A clause on one candidate: {v: true|false, seen: what the candidate has}. A
     missing attribute makes the clause false, whatever its operator. */
  function dspClause(c, cand) {
    var a = cand.attrs[c.attr];
    if (!a) return { v: false, seen: 'missing' };
    if (c.cmp === '=') return { v: dddValEq(a, c.val), seen: dddValText(a) };
    if (c.cmp === '!=') return { v: !dddValEq(a, c.val), seen: dddValText(a) };
    if (a.kind !== 'num') return { v: false, seen: dddValText(a) + ', not a number' };
    var s = Rcmp(a.r, c.val.r);
    var v = c.cmp === '<' ? s < 0 : (c.cmp === '<=' ? s <= 0 : (c.cmp === '>' ? s > 0 : s >= 0));
    return { v: v, seen: dddValText(a) };
  }
  function dspTree(node, res) {
    if (node.op === 'clause') return res[node.n].v;
    if (node.op === 'not') return !dspTree(node.a, res);
    if (node.op === 'and') return dspTree(node.a, res) && dspTree(node.b, res);
    return dspTree(node.a, res) || dspTree(node.b, res);
  }
  function dspRun(spec, cand) {
    var res = spec.clauses.map(function (c) { return dspClause(c, cand); });
    var first = null;
    res.forEach(function (r, i) { if (!r.v && first === null) first = i; });
    return { ok: dspTree(spec.tree, res), res: res, first: first };
  }
  /* Clause i with what the candidate has: "pages <= 300: pages is 412". */
  function dspDesc(spec, res, i, under) {
    var c = spec.clauses[i], s = res[i].seen;
    return c.text + (under ? ', true under not' : '') + (s === 'missing' ? ': ' + c.attr + ' missing' : ': ' + c.attr + ' is ' + s);
  }
  /* The clause that gives a node its value, walking from the left: a false and
     is blamed on its first false part, a true or on its first true part, a
     not on what makes its operand the opposite. */
  function dspBlame(node, res, val) {
    if (node.op === 'clause') return node.n;
    if (node.op === 'not') return dspBlame(node.a, res, !val);
    var left = dspTree(node.a, res);
    if ((node.op === 'and' && !val) || (node.op === 'or' && val)) return left === val ? dspBlame(node.a, res, val) : dspBlame(node.b, res, val);
    return dspBlame(node.a, res, val);
  }
  function dspWhy(spec, r) { var i = dspBlame(spec.tree, r.res, false); return dspDesc(spec, r.res, i, r.res[i].v); }
  /* --- the exact logical answer for pure conjunctions --------------------- */
  function dspConj(node) {
    if (node.op === 'clause') return [node];
    if (node.op !== 'and') return null;
    var a = dspConj(node.a), b = dspConj(node.b);
    return a && b ? a.concat(b) : null;
  }
  function dspUses(node, op) { return node.op === op || (node.a ? dspUses(node.a, op) : false) || (node.b ? dspUses(node.b, op) : false); }
  /* The values one attribute may take under B's clauses on it: words (all but
     ex, or only the list `only`) and numbers (an interval minus points). */
  function dspSet() { return { wAll: true, wEx: [], wOnly: [], qNone: false, lo: null, loIn: false, hi: null, hiIn: false, qEx: [] }; }
  function dspLo(S, c, incl) { var k = S.lo === null ? 1 : Rcmp(c, S.lo); if (k > 0) { S.lo = c; S.loIn = incl; } else if (k === 0) S.loIn = S.loIn && incl; }
  function dspHi(S, c, incl) { var k = S.hi === null ? -1 : Rcmp(c, S.hi); if (k < 0) { S.hi = c; S.hiIn = incl; } else if (k === 0) S.hiIn = S.hiIn && incl; }
  function dspNoWords(S) { S.wAll = false; S.wOnly = []; }
  function dspApply(S, c) {
    var v = c.val;
    if (v.kind === 'word') {
      if (c.cmp === '=') {
        S.qNone = true;
        if (S.wAll) S.wOnly = S.wEx.indexOf(v.w) >= 0 ? [] : [v.w]; else S.wOnly = S.wOnly.filter(function (x) { return x === v.w; });
        S.wAll = false;
      } else if (S.wAll) S.wEx.push(v.w); else S.wOnly = S.wOnly.filter(function (x) { return x !== v.w; });
      return;
    }
    if (c.cmp === '!=') { S.qEx.push(v.r); return; }
    dspNoWords(S);
    if (c.cmp === '=' || c.cmp === '>' || c.cmp === '>=') dspLo(S, v.r, c.cmp !== '>');
    if (c.cmp === '=' || c.cmp === '<' || c.cmp === '<=') dspHi(S, v.r, c.cmp !== '<');
  }
  function dspIn(list, r) { return list.some(function (x) { return Requ(x, r); }); }
  /* The numeric part with excluded endpoints opened: null when empty. */
  function dspQ(S) {
    if (S.qNone) return null;
    var q = { lo: S.lo, loIn: S.loIn, hi: S.hi, hiIn: S.hiIn };
    if (q.lo !== null && q.hi !== null) {
      var k = Rcmp(q.lo, q.hi);
      if (k > 0) return null;
      if (k === 0) return q.loIn && q.hiIn && !dspIn(S.qEx, q.lo) ? { point: q.lo } : null;
    }
    if (q.loIn && dspIn(S.qEx, q.lo)) q.loIn = false;
    if (q.hiIn && dspIn(S.qEx, q.hi)) q.hiIn = false;
    return q;
  }
  function dspWordsEmpty(S) { return !S.wAll && S.wOnly.length === 0; }
  function dspQHas(S, q, r) {
    if (!q) return false;
    if (q.point) return Requ(q.point, r);
    if (dspIn(S.qEx, r)) return false;
    var a = q.lo === null ? 1 : Rcmp(r, q.lo), b = q.hi === null ? -1 : Rcmp(r, q.hi);
    return (a > 0 || (a === 0 && q.loIn)) && (b < 0 || (b === 0 && q.hiIn));
  }
  /* Is everything S allows inside clause c of A? */
  function dspImplies(S, c) {
    var q = dspQ(S), noW = dspWordsEmpty(S), v = c.val;
    if (v.kind === 'word') {
      if (c.cmp === '=') return !q && (!S.wAll && S.wOnly.every(function (x) { return x === v.w; }));
      return S.wAll ? S.wEx.indexOf(v.w) >= 0 : S.wOnly.indexOf(v.w) < 0;
    }
    if (c.cmp === '!=') return !dspQHas(S, q, v.r);
    if (!noW) return false;
    if (!q) return true;
    if (c.cmp === '=') return !!q.point && Requ(q.point, v.r);
    if (q.point) { var s = Rcmp(q.point, v.r); return c.cmp === '<' ? s < 0 : (c.cmp === '<=' ? s <= 0 : (c.cmp === '>' ? s > 0 : s >= 0)); }
    if (c.cmp === '<' || c.cmp === '<=') {
      if (q.hi === null) return false;
      var h = Rcmp(q.hi, v.r);
      return h < 0 || (h === 0 && (c.cmp === '<=' || !q.hiIn));
    }
    if (q.lo === null) return false;
    var l = Rcmp(q.lo, v.r);
    return l > 0 || (l === 0 && (c.cmp === '>=' || !q.loIn));
  }
  function dspLogical(A, B) {
    var ca = dspConj(A.tree), cb = dspConj(B.tree);
    if (!ca || !cb) {
      var who = !ca ? A : B, nm = !ca ? 'A' : 'B';
      return 'not decidable by the lab: ' + nm + ' uses ' + (dspUses(who.tree, 'or') ? 'or' : 'not') + ', and the lab decides only clauses joined by and';
    }
    var sets = {}, attrs = [];
    cb.forEach(function (c) { if (!sets[c.attr]) { sets[c.attr] = dspSet(); attrs.push(c.attr); } dspApply(sets[c.attr], c); });
    for (var i = 0; i < attrs.length; i += 1) {
      var S = sets[attrs[i]];
      if (!dspQ(S) && dspWordsEmpty(S)) return 'yes, vacuously: B can select nothing (no value of ' + attrs[i] + ' meets all its clauses)';
    }
    for (var j = 0; j < ca.length; j += 1) {
      var c = ca[j];
      if (!sets[c.attr]) return 'no: B says nothing of ' + c.attr + ', so a candidate missing it can satisfy B and fail A’s clause ' + c.text;
      if (!dspImplies(sets[c.attr], c)) return 'no: B allows a value of ' + c.attr + ' that fails A’s clause ' + c.text;
    }
    return 'yes: every clause of A follows from B’s clauses';
  }
"""

DSP_VIEW_JS = {}

DSP_VIEW_JS["validate"] = r"""
  DSP_VIEW.validate = function (inst) {
    var cands = dspCands(inst.candidates), cand = null;
    cands.forEach(function (c) { if (c.name === inst.candidate) cand = c; });
    if (!cand) eaRefuse('The candidate to validate, ' + inst.candidate + ', is not one of the candidates');
    var spec = dspParse(inst.spec, 'The specification'), r = dspRun(spec, cand), falses = [], ntrue = 0;
    var rows = spec.clauses.map(function (c, i) {
      if (r.res[i].v) ntrue += 1; else falses.push(c.text);
      return [String(i + 1), c.text, r.res[i].seen, r.res[i].v ? 'true' : 'false'];
    });
    return {
      tiles: { dspSatisfied: r.ok ? 'yes' : 'no', dspTrue: eaInt(ntrue) + ' of ' + eaInt(spec.clauses.length),
               dspFirstFalse: r.first === null ? 'none: every clause is true' : 'clause ' + (r.first + 1) + ', ' + dspDesc(spec, r.res, r.first, false),
               dspFalse: dddListed(falses.length, falses) },
      status: dddStatus(cand.name + (r.ok ? ' satisfies' : ' does not satisfy') + ' the specification; '
        + eaInt(ntrue) + ' of its ' + eaPlural(spec.clauses.length, 'clause', 'clauses') + (ntrue === 1 ? ' is' : ' are') + ' true'),
      table: { caption: 'Each clause, in the order written, on ' + cand.name, head: ['#', 'clause', cand.name + ' has', 'clause is'], rows: rows }
    };
  };
"""

DSP_VIEW_JS["select"] = r"""
  DSP_VIEW.select = function (inst) {
    var cands = dspCands(inst.candidates), spec = dspParse(inst.spec, 'The specification'), yes = [], no = [];
    var rows = cands.map(function (c) {
      var r = dspRun(spec, c), nt = r.res.filter(function (x) { return x.v; }).length;
      if (r.ok) yes.push(c.name); else no.push(c.name + ' (' + dspWhy(spec, r) + ')');
      return [c.name, r.ok ? 'yes' : 'no', eaInt(nt) + ' of ' + eaInt(spec.clauses.length), r.ok ? '' : dspWhy(spec, r)];
    });
    return {
      tiles: { dspCandidates: eaInt(cands.length), dspSatisfying: eaCount(yes), dspFailing: dddListed(no.length, no, '; ') },
      status: dddStatus('The specification selects ' + eaInt(yes.length) + ' of ' + eaPlural(cands.length, 'candidate', 'candidates')),
      table: { caption: 'Each candidate and, when it fails, the clause that rejects it', head: ['candidate', 'satisfies', 'clauses true', 'rejected by'], rows: rows }
    };
  };
"""

DSP_VIEW_JS["subsume"] = r"""
  DSP_VIEW.subsume = function (inst) {
    var cands = dspCands(inst.candidates), A = dspParse(inst.spec, 'Specification A'), B = dspParse(inst.other, 'Specification B');
    var sa = [], sb = [], counter = [];
    var rows = cands.map(function (c) {
      var a = dspRun(A, c).ok, b = dspRun(B, c).ok;
      if (a) sa.push(c.name);
      if (b) sb.push(c.name);
      if (b && !a) counter.push(c.name);
      return [c.name, b ? 'yes' : 'no', a ? 'yes' : 'no', b && !a ? 'counter-example' : ''];
    });
    var on = sb.length === 0 ? 'yes, vacuously: no candidate satisfies B'
      : (counter.length === 0 ? (sb.length === 1 ? 'yes: the one candidate that satisfies B satisfies A' : 'yes: all ' + eaInt(sb.length) + ' that satisfy B satisfy A')
        : 'no: ' + eaInt(counter.length) + ' of the ' + eaInt(sb.length) + ' that satisfy B ' + (counter.length === 1 ? 'fails' : 'fail') + ' A');
    var logic = dspLogical(A, B);
    return {
      tiles: { dspSatB: eaCount(sb), dspSatA: eaCount(sa), dspOnCands: on, dspCounter: eaCount(counter), dspLogical: logic },
      status: dddStatus('On these ' + eaPlural(cands.length, 'candidate', 'candidates') + ', '
        + (counter.length ? 'A rejects ' + eaInt(counter.length) + ' that B accepts' : 'every one B accepts, A accepts too')
        + '; for every possible candidate, ' + logic.split(':')[0]),
      table: { caption: 'Each candidate under B and under A', head: ['candidate', 'satisfies B', 'satisfies A', ''], rows: rows }
    };
  };
"""

# --- the spec parser, mirrored (refusals only) ------------------------------

_TOKEN = re.compile(r"\(|\)|!=|<=|>=|=|<|>|[A-Za-z0-9._-]+")
_WORD = re.compile(r"^[A-Za-z][A-Za-z0-9._-]*$")
_OPS = ("=", "!=", "<", "<=", ">", ">=")
_KW = ("and", "or", "not")


def _quote(s):
    s = str(s)
    return '"%s"' % (s[:40] + "…" if len(s) > 40 else s)


def _plural(n, one, many):
    return "%s %s" % (ea.grp(n), one if n == 1 else many)


def _value(text, what):
    """Mirror of dddValue: ('num', Fraction) or ('word', str)."""
    s = str(text).replace("−", "-").strip()
    if s == "":
        raise ValueError("%s is empty" % what)
    m = re.fullmatch(r"-?(?:\d+(?:\.(\d+))?|\.(\d+))", s)
    if m:
        if len(m.group(1) or m.group(2) or "") > ea.DECIMALS:
            raise ValueError("%s has more than 6 decimal places" % what)
        r = Fraction(s)
        if abs(r) > 10 ** 7:
            raise ValueError("%s is at most 10,000,000 in size, and it is %s" % (what, s.replace("-", "−", 1)))
        return ("num", r)
    if _WORD.match(s):
        return ("word", s)
    raise ValueError("%s %s should be a number such as 3 or 0.25, or a word that begins with a letter (letters, "
                     "digits, dots, hyphens, underscores)" % (what, _quote(s)))


def _dec(r):
    """Mirror of dddDec for a value that has a finite decimal."""
    r = Fraction(r)
    neg, n = r < 0, abs(r)
    whole, rem = divmod(n.numerator, n.denominator)
    frac = ""
    for _ in range(12):
        if not rem:
            break
        rem *= 10
        frac += str(rem // n.denominator)
        rem %= n.denominator
    return ("−" if neg else "") + str(whole) + ("." + frac if frac else "") + ("…" if rem else "")


def parse_spec(text, what):
    """Mirror of dspParse's refusals; returns the number of clauses."""
    toks, i = [], 0
    while i < len(text):
        if text[i].isspace():
            i += 1
            continue
        m = _TOKEN.match(text, i)
        if not m:
            raise ValueError("%s has %s at character %d, which this lab cannot read (it reads attribute op value, with "
                             "= != < <= > >=, and, or, not and parentheses)" % (what, _quote(text[i]), i + 1))
        toks.append(m.group(0))
        i = m.end()
    st = {"p": 0, "n": 0, "depth": 0}

    def peek():
        return toks[st["p"]] if st["p"] < len(toks) else None

    def or_e():
        and_e()
        while peek() == "or":
            st["p"] += 1
            and_e()

    def and_e():
        not_e()
        while peek() == "and":
            st["p"] += 1
            not_e()

    def not_e():
        if peek() == "not":
            st["p"] += 1
            not_e()
            return
        atom()

    def atom():
        t = peek()
        if t is None:
            raise ValueError("%s ends where a clause should be" % what)
        if t == "(":
            st["p"] += 1
            st["depth"] += 1
            if st["depth"] > 8:
                raise ValueError("%s nests parentheses more than 8 deep" % what)
            or_e()
            if peek() != ")":
                raise ValueError("%s opens a parenthesis it never closes" % what)
            st["p"] += 1
            st["depth"] -= 1
            return
        if t == ")" or t in _OPS or t in _KW or not _WORD.match(t):
            raise ValueError("%s has %s where an attribute name should be (a word beginning with a letter)"
                             % (what, _quote(t)))
        st["p"] += 1
        op = peek()
        if op is None or op not in _OPS:
            raise ValueError("%s: after %s should come one of = != < <= > >=%s"
                             % (what, t, "" if op is None else ", not " + _quote(op)))
        st["p"] += 1
        v = peek()
        if v is None or v in ("(", ")") or v in _OPS or v in _KW:
            raise ValueError("%s: %s %s needs a value, a number or a word" % (what, t, op))
        st["p"] += 1
        kind, _val = _value(v, "%s: the value in %s %s %s" % (what, t, op, v))
        if kind == "word" and op not in ("=", "!="):
            raise ValueError("%s: %s %s %s orders a word; a word compares only by = and !=" % (what, t, op, v))
        st["n"] += 1
        if st["n"] > 20:
            raise ValueError("%s has more than 20 clauses; this lab reads at most 20" % what)

    or_e()
    if st["p"] < len(toks):
        raise ValueError("%s has %s after the specification ends" % (what, _quote(toks[st["p"]])))
    return st["n"]


def _check_validate(inst, fixed):
    if inst["candidate"] not in [c["name"] for c in inst["candidates"]]:
        raise ValueError("The candidate to validate, %s, is not one of the candidates" % inst["candidate"])
    parse_spec(inst["spec"], "The specification")


def _check_select(inst, fixed):
    parse_spec(inst["spec"], "The specification")


def _check_subsume(inst, fixed):
    parse_spec(inst["spec"], "Specification A")
    parse_spec(inst["other"], "Specification B")


# ---------------------------------------------------------------------------
# dddkit's two field kinds, mirrored (kit-contract.md section 4)
# ---------------------------------------------------------------------------

KV = {"kind": "kv"}


def vrec(what, sub, rest, rest_what, lo_rest, hi_rest, unique=False, rows=3, lo=1, hi=ea.MAX_RECORDS):
    """Records: the cells in `sub`, then lo_rest to hi_rest cells each read by `rest` (a scalar spec, or KV)."""
    return {"kind": "vrec", "what": what, "control": "area", "rows": rows, "sub": [list(s) for s in sub],
            "rest": dict(rest), "restWhat": rest_what, "loRest": lo_rest, "hiRest": hi_rest,
            "lo": lo, "hi": hi, "unique": unique}


def expr(what, rows=2):
    """A specification box: one expression, at most 300 characters; empty in the markup, filled by script."""
    return {"kind": "expr", "what": what, "control": "expr", "rows": rows}


def _parse_vrec(f, text):
    what = f["what"]
    s = str(text).replace("−", "-").strip()
    rows = [r.strip() for r in s.split(";")] if s else []
    if rows and rows[-1] == "":
        rows.pop()
    ea._sized(len(rows), f, what, "records")
    out, seen, n = [], set(), len(f["sub"])
    for i, row in enumerate(rows):
        cells = [c.strip() for c in row.split(",")]
        k, w = len(cells) - n, "%s, record %d" % (what, i + 1)
        if k < f["loRest"] or k > f["hiRest"]:
            need = (str(n + f["loRest"]) if f["loRest"] == f["hiRest"]
                    else "%d to %d" % (n + f["loRest"], n + f["hiRest"]))
            raise ValueError("%s has %d field%s; this list needs %s (%s, then %s)"
                             % (w, len(cells), "" if len(cells) == 1 else "s", need,
                                ", ".join(key for key, _ in f["sub"]), f["restWhat"]))
        rec = {}
        for j, (key, kk) in enumerate(f["sub"]):
            rec[key] = ea.parse_scalar(kk, cells[j], "%s: %s" % (w, key))
        rest, keys = [], set()
        for j, c in enumerate(cells[n:]):
            ww = "%s: %s %d" % (w, f["restWhat"], j + 1)
            if f["rest"]["kind"] != "kv":
                rest.append(ea.parse_scalar(f["rest"], c, ww))
                continue
            m = re.fullmatch(r"([^=\s]+)\s*=\s*([^=\s]+)", c)
            if not m or not _WORD.match(m.group(1)):
                raise ValueError("%s: %s should be name=value, such as pages=320 or genre=crime, the name beginning "
                                 "with a letter" % (ww, _quote(c)))
            if m.group(1) in keys:
                raise ValueError("%s gives %s twice" % (w, m.group(1)))
            keys.add(m.group(1))
            rest.append({"k": m.group(1), "v": _value(m.group(2), "%s (%s)" % (ww, m.group(1)))})
        rec["rest"] = rest
        if f["unique"]:
            if cells[0] in seen:
                raise ValueError("%s names %s twice" % (what, _quote(cells[0])))
            seen.add(cells[0])
        out.append(rec)
    return out


def _parse_expr(f, text):
    s = re.sub(r"\s+", " ", str(text).replace("−", "-").strip())
    if s == "":
        raise ValueError("%s is empty" % f["what"])
    if len(s) > 300:
        raise ValueError("%s has %d characters; this lab reads at most 300" % (f["what"], len(s)))
    return s


def parse_field(where, f, text):
    """Mirror of dddRead for one field."""
    if f["kind"] not in ("vrec", "expr"):
        return ea.parse(where, f, text)
    try:
        return _parse_vrec(f, text) if f["kind"] == "vrec" else _parse_expr(f, text)
    except ValueError as exc:
        raise ValueError("%s: %s" % (where, exc)) from None


def to_text(where, f, value):
    """A preset's value -> the exact text its box holds (eakit's to_text for eakit's kinds)."""
    if f["kind"] not in ("vrec", "expr"):
        return ea.to_text(where, f, value)
    what = f["what"]
    if isinstance(value, str):
        text = value.strip()
    elif f["kind"] == "vrec" and isinstance(value, (list, tuple)):
        text = "; ".join(r.strip() if isinstance(r, str) else ", ".join(str(p).strip() for p in r) for r in value)
    else:
        raise ValueError("%s: %s cannot be %r" % (where, what, value))
    bad = r'[&"]' if f["kind"] == "expr" else r'[<>&"]'
    if re.search(bad, text):
        raise ValueError("%s: %s %r contains %s, which no shipped value may"
                         % (where, what, text, "& or a quote" if f["kind"] == "expr" else "< > & or a quote"))
    parse_field(where, f, text)
    return text


def _presets(cfg, kit, fields, tiles, check, fixed):
    """eakit_core.presets, reading dddkit's two kinds as well."""
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
_WIRE_JS = ea.EA_WIRE_JS.replace(_READ_CALL, "dddRead(SPEC, raw)")
assert ea.EA_WIRE_JS.count(_READ_CALL) == 1, "eakit's wiring no longer reads its inputs with one eaRead(SPEC, raw) call"
_COMMENT_LINES = re.compile(r"^[ \t]*/\*(?:(?!\*/).)*\*/[ \t]*\n", re.S | re.M)


def _build_lab(cfg, *, kit, prefix, view, fields, tiles, fn, js, fixed, title, subtitle, intro, rules, extra_keys=(),
               check=None):
    """eakit_core.build_lab, with dddkit's two kinds and dddRead (kit-contract.md section 2)."""
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
        elif fspec["control"] == "expr":
            controls += ea.area_html(cid, fspec["what"], "", fspec.get("rows", 2))
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


# ---------------------------------------------------------------------------
# The mode specs (family A)
# ---------------------------------------------------------------------------

_N = ea.NAME
_NUM = ea.num(lo=-ea.LIMIT)

LANG = {
    "prefix": "dln", "fn": "dlnCompute", "title": "The language", "js": DLN_JS,
    "views": {
        "glossary": {
            "fields": [("audiences", {"kind": "list", "what": "Audiences (2 to 4 names, in order)", "control": "text",
                                      "lo": 2, "hi": 4, "things": "audiences", "each": _N}, "experts developers code"),
                       ("terms", vrec("Terms (concept, then one name per audience; - for none)", [("concept", _N)],
                                      ea.PARENT, "name", 1, 4, unique=True, rows=4), None)],
            "tiles": [("Concepts", "dlnConcepts"), ("Named alike by every audience", "dlnAlike"),
                      ("Translations a conversation needs", "dlnTranslations"),
                      ("Names missing (concept, audience)", "dlnMissing"),
                      ("Ambiguous names (one name, two or more concepts)", "dlnAmbiguous")],
            "check": _check_glossary, "subtitle": "one concept, several audiences, how many names",
            "rules": "Each record names one concept and then gives one name for it per audience, in the order of the "
                     "audiences; - means that audience has no name for it. Names compare ignoring letter case and "
                     "nothing else (Loan = loan; loan_record ≠ loan). A translation is one pair of audiences whose "
                     "names for one concept differ, counted once per pair and per concept; a pair where either name "
                     "is missing is not a translation but a name missing. A concept is named alike when every "
                     "audience names it and all the names agree. A name is ambiguous when one audience uses it for "
                     "two or more concepts. Lists follow the order of the records and of the audiences.",
            "js": DLN_VIEW_JS["glossary"],
        },
        "cognates": {
            "fields": [("contexts", ea.rec("Terms by context (context, term, meaning)",
                                           [("context", _N), ("term", _N), ("meaning", _N)], rows=5, lo=2), None)],
            "tiles": [("Contexts", "dlnContexts"), ("Terms", "dlnTerms"), ("Shared terms (in two or more contexts)", "dlnShared"),
                      ("False cognates (one term, different meanings)", "dlnFalse"),
                      ("Duplicate concepts (one meaning, different terms)", "dlnDuplicate"),
                      ("Terms safe to share", "dlnSafe")],
            "check": _check_cognates, "subtitle": "the same word in different bounded contexts",
            "rules": "Each record says what one term means in one context, the meaning a short name of the concept. "
                     "Terms and meanings compare ignoring letter case. A shared term appears in two or more "
                     "contexts; it is a false cognate when its meanings there are not all the same, and safe to "
                     "share when they are (a term in one context is neither). A duplicate concept is one meaning "
                     "carried by two or more different terms, in any contexts. A context may give a term once. "
                     "Lists follow the order in which contexts, terms and meanings first appear.",
            "js": DLN_VIEW_JS["cognates"],
        },
    },
}

_ASSOC_SUB = [("a", _N), ("b", _N), ("ends", ea.word("1-1", "1-n", "n-1", "n-n")),
              ("direction", ea.word("both", "a-b", "b-a")), ("qualified", ea.YESNO)]

ASSOC = {
    "prefix": "das", "fn": "dasCompute", "title": "Associations", "js": DAS_JS,
    "views": {
        "simplify": {
            "fields": [("assocs", ea.rec("Associations before (a, b, ends, direction, qualified)", _ASSOC_SUB, rows=4), None),
                       ("after", ea.rec("Associations after (same shape; empty for none)", _ASSOC_SUB, rows=4, lo=0), "")],
            "tiles": [("Associations", "dasAssocs"), ("Navigable directions", "dasDirections"),
                      ("Two-way (two references to keep in step per link)", "dasTwoWay"),
                      ("Many-to-many", "dasManyMany"), ("Many ends", "dasManyEnds"),
                      ("The change, after − before", "dasChange")],
            "check": _check_simplify, "subtitle": "a direction, a qualifier, a dropped association",
            "rules": "Each record is one association between classes a and b: ends 1-n means one a to many b; "
                     "direction both, a-b (only a navigates to b) or b-a. A two-way association gives 2 navigable "
                     "directions and 2 references to keep in step whenever one link changes; a one-way association "
                     "gives 1 of each. A qualifier (qualified yes) reduces one many end to one: the end navigated to "
                     "(b for a-b, a for b-a; for both, b if it is many, else a); a qualifier on an end that is "
                     "already one is refused. Every count is after qualifiers. The after list, when given, is "
                     "counted the same way, each tile reads before → after, and the change is after − before.",
            "js": DAS_VIEW_JS["simplify"],
        },
    },
}

IDENTITY = {
    "prefix": "did", "fn": "didCompute", "title": "Identity and value", "js": DID_JS,
    "views": {
        "equality": {
            "fields": [("objects", vrec("Objects (name, id or -, then attribute=value cells)",
                                        [("name", _N), ("id", ea.PARENT)], KV, "attribute", 0, 12, unique=True,
                                        rows=4), None),
                       ("pairs", ea.rec("Pairs to compare (x, y; empty for every pair)", [("x", _N), ("y", _N)],
                                        rows=2, lo=0), "")],
            "tiles": [("Pairs compared", "didPairs"), ("Same by identity", "didIdentity"),
                      ("Same by attributes", "didAttrs"), ("Same thing, attributes changed", "didChanged"),
                      ("Different things, same attributes (look-alikes)", "didLookalike")],
            "check": _check_equality, "subtitle": "the same by identity, or the same by value",
            "rules": "Two objects are the same by identity when both carry an id and the ids are equal (ids compare "
                     "exactly; - means the object has no identity, a value object, and is never the same by "
                     "identity). They are the same by attributes when they have the same attribute names and every "
                     "value is equal (numbers exactly, so 2 = 2.0; words exactly, letter case counted). A changed "
                     "pair is the same thing with different attributes; a look-alike pair is two things, both with "
                     "ids and the ids different, with the same attributes. With no pairs given, every pair is "
                     "compared in record order (at most 12 objects).",
            "js": DID_VIEW_JS["equality"],
        },
        "sharing": {
            "fields": [("holders", ea.rec("Holders (holder, the value it refers to)", [("holder", _N), ("value", _N)],
                                          unique=True, rows=3), None),
                       ("value", ea.field("The shared value", _N), None),
                       ("change", ea.field("The holder that makes the change", _N), None),
                       ("kind", ea.choice("The value is", "mutable", "immutable"), None)],
            "tiles": [("Holders of the value", "didHolders"), ("Holders that see the change", "didSee"),
                      ("Holders surprised (saw a change they did not make)", "didSurprised"),
                      ("New values created", "didNew")],
            "check": _check_sharing, "subtitle": "a change through one holder of a shared value",
            "rules": "Each record says which value a holder refers to; several holders may share one. A change is "
                     "made through one holder. If the value is mutable it changes in place, so every holder of it "
                     "sees the change; if it is immutable the changing holder gets a new value (named with ′) and "
                     "every other holder keeps the old one. A holder is surprised when it sees a change it did not "
                     "make. Lists follow the record order.",
            "js": DID_VIEW_JS["sharing"],
        },
    },
}

AGGREGATE = {
    "prefix": "dgr", "fn": "dgrCompute", "title": "Aggregates", "js": DGR_JS,
    "views": {
        "boundary": {
            "fields": [("objects", ea.rec("Objects (object, aggregate, root yes or no)",
                                          [("object", _N), ("aggregate", _N), ("root", ea.YESNO)], unique=True,
                                          rows=4), None),
                       ("refs", ea.rec("References (from, to; from may be an outside holder)", [("from", _N), ("to", _N)],
                                       rows=3, lo=0), ""),
                       ("delete", ea.field("Delete this object (- for none)", ea.PARENT), "-")],
            "tiles": [("Aggregates", "dgrAggregates"), ("Objects", "dgrObjects"),
                      ("References crossing a boundary", "dgrCrossing"),
                      ("Of those, to a non-root (violations)", "dgrViolations"),
                      ("Objects the delete removes", "dgrRemoves"), ("References left dangling", "dgrDangling")],
            "check": _check_boundary, "subtitle": "who may hold a reference into an aggregate",
            "rules": "Each object belongs to one aggregate, and each aggregate has exactly one root. A reference "
                     "crosses a boundary when it comes from outside the aggregate it points into: from another "
                     "aggregate's object, or from a name that is not an object (an outside holder). A crossing "
                     "reference may hold only the root; one to any other object is a violation. Deleting a root "
                     "removes its whole aggregate; deleting a non-root is refused, naming the root to go through. A "
                     "reference left dangling runs from a surviving object or outside holder to a removed object. "
                     "Lists follow the order of the records.",
            "js": DGR_VIEW_JS["boundary"],
        },
        "lock": {
            "fields": [("items", ea.rec("Items of one aggregate (item, value)", [("item", _N), ("value", _NUM)],
                                        unique=True, rows=2, hi=20), None),
                       ("limit", ea.field("The invariant: sum of the values at most", _NUM), None),
                       ("edits", ea.rec("Edits (minute, user, item, new value)",
                                        [("minute", ea.whole(1, 1440)), ("user", _N), ("item", _N), ("value", _NUM)],
                                        rows=4), None),
                       ("scheme", ea.choice("Locking scheme", "object", "aggregate"), "object")],
            "tiles": [("Users who commit", "dgrCommitted"), ("Users refused", "dgrRefused"),
                      ("Final values", "dgrFinal"), ("Final sum", "dgrSum"), ("Invariant holds", "dgrHolds"),
                      ("Edits lost (overwritten by a later commit)", "dgrLost")],
            "check": _check_lock, "subtitle": "concurrent edits, an invariant that spans objects",
            "rules": "Every user reads the aggregate at minute 0, edits items at the minutes given (an edit sets the "
                     "item's new value) and commits at their last edit's minute. Locks are pessimistic, taken at an "
                     "edit and held to the end of the user's commit minute. Object scheme: an edit locks only its "
                     "item, so two users conflict only on the same item. Aggregate scheme: an edit locks the whole "
                     "aggregate. An edit of what another user holds refuses its user outright: all their edits are "
                     "discarded and their locks released. Edits are taken in minute order, ties in record order; "
                     "commits apply in commit-minute order, ties in order of first appearance. An edit lost is a "
                     "committed value overwritten by a later commit. The invariant is that the sum of the values "
                     "is at most the limit.",
            "js": DGR_VIEW_JS["lock"],
        },
    },
}

_CANDS = ("candidates", vrec("Candidates (name, then attribute=value cells)", [("name", _N)], KV, "attribute", 1, 12,
                             unique=True, rows=4, hi=40), None)
_SPEC_RULES = ("A specification is clauses attribute op value, with op one of = != < <= > >=, joined by and, or, not "
               "and parentheses (not binds tightest, then and, then or); a value is a number or a word beginning "
               "with a letter. Numbers compare exactly; a word compares only by = and != (an ordering op on a word "
               "is refused), and words compare exactly, letter case counted. A clause on an attribute the "
               "candidate lacks is false whatever its op, so not of it is true; an ordering clause on a word value "
               "is false. ")

SPEC = {
    "prefix": "dsp", "fn": "dspCompute", "title": "Specifications", "js": DSP_JS,
    "views": {
        "validate": {
            "fields": [_CANDS, ("candidate", ea.field("The candidate to validate", _N), None),
                       ("spec", expr("The specification"), None)],
            "tiles": [("Satisfied", "dspSatisfied"), ("Clauses true", "dspTrue"),
                      ("The first false clause, in the order written", "dspFirstFalse"),
                      ("Every false clause", "dspFalse")],
            "check": _check_validate, "subtitle": "one candidate against one rule",
            "rules": _SPEC_RULES + "Clauses are numbered in the order written; the first false clause is the "
                     "first in that order, whether or not the whole is satisfied.",
            "js": DSP_VIEW_JS["validate"],
        },
        "select": {
            "fields": [_CANDS, ("spec", expr("The specification"), None)],
            "tiles": [("Candidates", "dspCandidates"), ("Satisfying", "dspSatisfying"),
                      ("Failing, each with the clause that rejects it", "dspFailing")],
            "check": _check_select, "subtitle": "a rule as a query over candidates",
            "rules": _SPEC_RULES + "Candidates are listed in record order. A failing candidate is shown with the "
                     "clause that rejects it, found from the left: a false and is blamed on its first false part, a "
                     "true or on its first true part, and under a not a clause rejects by being true (for clauses "
                     "joined only by and, this is the first false clause in the order written).",
            "js": DSP_VIEW_JS["select"],
        },
        "subsume": {
            "fields": [_CANDS, ("spec", expr("Specification A"), None),
                       ("other", expr("Specification B"), None)],
            "tiles": [("Satisfying B", "dspSatB"), ("Satisfying A", "dspSatA"),
                      ("On these candidates: every one B accepts, A accepts too", "dspOnCands"),
                      ("Counter-examples (B accepts, A rejects)", "dspCounter"),
                      ("For every possible candidate: every one B accepts, A accepts too", "dspLogical")],
            "check": _check_subsume, "subtitle": "does every candidate one rule accepts pass the other",
            "rules": _SPEC_RULES + "The question is one relation, in plain words: does A accept every candidate "
                     "B accepts? The word subsumes is used both ways round: in the logicians' sense the looser "
                     "rule, A, subsumes B; in Evans's sense (Chapter 10) the stricter rule, B, subsumes A. The "
                     "tiles avoid the word. On the candidates the relation is checked one by one. For every "
                     "possible candidate the answer is exact when both are clauses joined only by and: B's clauses "
                     "on each attribute give the values it allows (an interval of numbers less excluded points, and "
                     "words), and A accepts all B accepts when B allows nothing or every clause of A holds for "
                     "everything B allows, an attribute B never mentions being allowed missing. With or or not in "
                     "either, the lab says it cannot decide.",
            "js": DSP_VIEW_JS["subsume"],
        },
    },
}

SPECS = {"lang": LANG, "assoc": ASSOC, "identity": IDENTITY, "aggregate": AGGREGATE, "spec": SPEC}
MODES_A = tuple(SPECS)


# ---------------------------------------------------------------------------
# Building a lab (both families) and the entry point
# ---------------------------------------------------------------------------

def family_intro():
    return (FAMILY_SENTENCE + " The lab counts one consequence of one modelling choice; the choice itself is weighed "
            "in the book, against the domain, the team and the project.")


def _no_options(cfg, kit, tiles):
    return {}, [], tiles


def mode_lab(cfg, mode, spec):
    """One dddkit mode as a Lab, from its spec dict (kit-contract.md section 2)."""
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
                      fn=spec["fn"], js=DDD_CORE_JS + spec["js"] + v["js"], fixed=fixed, title=spec["title"],
                      subtitle=v["subtitle"], intro=family_intro(), rules=v["rules"], extra_keys=keys,
                      check=v["check"])


def dddkit_lab(cfg):
    """The Domain-Driven Design kit: cfg["mode"] chooses the mode, cfg["view"] the view."""
    cfg = cfg or {}
    mode = cfg.get("mode")
    if mode in SPECS:
        return mode_lab(cfg, mode, SPECS[mode])
    family_b = dddkit_b.MODES
    if mode in family_b:
        return family_b[mode](cfg)
    raise ValueError("dddkit_lab: unknown mode %r; the modes are %s"
                     % (mode, ", ".join(MODES_A + tuple(m for m in family_b if m not in SPECS))))


# Family B. Imported last, after mode_lab exists, so that dddkit_b may import
# from this module at its top whichever module loads first.
from . import dddkit_b  # noqa: E402

__all__ = ["dddkit_lab", "mode_lab", "family_intro", "DDD_CORE_JS", "SPECS", "MODES_A", "KIT", "CAUTION",
           "vrec", "expr", "KV", "parse_field", "to_text", "parse_spec"]
