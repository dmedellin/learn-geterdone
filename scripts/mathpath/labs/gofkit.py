"""gofkit -- the lab kit of Design Patterns, Read Along.

Specified in docs/design-patterns/PLAN.md sections 0 and D; the report an
author configures a lesson from is docs/design-patterns/kit-report.md, and the
seam between this module and gofkit_b.py is docs/design-patterns/kit-contract.md.
Built the way dddkit was, on eakit_core (imported as `ea`, unchanged), and on
dddkit itself: its two field kinds (`vrec`, `expr`), its preset reader, its
`dddRead` wiring and DDD_CORE_JS are reused by import, not copied. Only the
lab builder is a thin copy of dddkit's, because dddkit's puts dddkit's own
first sentence on every panel intro.

Family A (this module), classes and structures:

  classes  (gcl)  explosion, factory
  tree     (gtr)  compose, traverse, visit
  expr     (gex)  interpret

Family B (gofkit_b.py): route, notify, history, machine, share, proxy.
`gofkit_lab` dispatches them through `gofkit_b.MODES`.

THE BUILDER SIGNATURE (both families). A mode is built by
`builder(cfg) -> common.Lab`; every builder is
`lambda cfg: mode_lab(cfg, <mode>, <SPEC>)`, and `mode_lab` takes dddkit's
spec dict (kit-contract.md section 2). The first view is the default. A page
ships RATIONAL_JS, EA_CORE_JS, DDD_CORE_JS, GOF_CORE_JS, its mode's base block
and its own view's block -- never the other views or modes.

IDS. PLAN section D's prefixes, all free (grepped against
scripts/mathpath/labs/*.py and scripts/*.js on 2026-11-01). Shared helpers
begin gof / GOF_ and are defined only here.

EXACTNESS. Every figure is a count, a list, or an exact BigInt rational;
nothing typed is evaluated as script. The expr mode's expressions are read by
this kit's own lexer and parser, mirrored in Python so a preset the page would
refuse fails the build.
"""

import re
from fractions import Fraction

from . import eakit_core as ea
from . import dddkit
from .algebra_core import RATIONAL_JS
from .common import Lab, cfg_literal
from .dddkit import DDD_CORE_JS, vrec, expr

KIT = "gofkit"
CAUTION = "the count is of the design stated"
FAMILY_SENTENCE = "A count over the small design the lesson states."

# ---------------------------------------------------------------------------
# GOF_CORE_JS: gofkit's shared helpers (kit-contract.md section 3)
# ---------------------------------------------------------------------------

GOF_CORE_JS = r"""
  /* gofkit's shared helpers (docs/design-patterns/kit-contract.md). */
  var GOF_CAUTION = 'the count is of the design stated';
  function gofStatus(s) { return String(s).replace(/[.\s]+$/, '') + '; ' + GOF_CAUTION + '.'; }
  function gofCount(n, one, many) { return eaPlural(n, one, many); }
  /* A rational with a finite decimal of at most 6 places, grouped: 1,234.5; else eaNum. */
  function gofDec(r) {
    for (var p = 0; p <= 6; p += 1) if (eaExactAt(r, p)) return eaFixed(r, p);
    return eaNum(r);
  }
  /* An exact value: 12; 7/2 = 3.5; 1/8 = 0.125; 2/3 ≈ 0.67; very long ones ≈ 1.23 × 10^40. */
  function gofNum(r) {
    if (eaBig(r)) return eaSci(r);
    if (Rint(r)) return eaInt(r.n);
    for (var p = 1; p <= 6; p += 1) if (eaExactAt(r, p)) return eaFrac(r) + ' = ' + eaFixed(r, p);
    return eaNum(r);
  }
  function gofHas(o, k) { return Object.prototype.hasOwnProperty.call(o, k); }
"""

# ---------------------------------------------------------------------------
# classes (gcl): explosion, factory
# ---------------------------------------------------------------------------

GCL_JS = r"""
  var GCL_VIEW = {};
  function gclCompute(view, inst, opts) { return eaRun(GCL_VIEW[view], inst, opts); }
"""

GCL_VIEW_JS = {}

GCL_VIEW_JS["explosion"] = r"""
  GCL_VIEW.explosion = function (inst) {
    var as = inst.aspects, seen = {}, names = [], counts = [];
    as.forEach(function (a) {
      [a.aspect].concat(a.rest).forEach(function (nm) {
        if (gofHas(seen, nm)) eaRefuse('Aspects: ' + nm + ' is named twice; every aspect and every variant is a class, and each needs a name of its own');
        seen[nm] = true;
      });
      names.push(a.aspect); counts.push(a.rest.length);
    });
    var added = inst.added, at = added === '-' ? -1 : names.indexOf(added);
    if (added !== '-' && at < 0) eaRefuse('The aspect that gains a variant, ' + added + ', is not one of the aspects (' + names.join(', ') + ')');
    var P = 1, S = 0;
    counts.forEach(function (c) { P *= c; S += c; });
    var A = as.length, sub = P + 1, comp = S + A, rows = [];
    as.forEach(function (a, i) {
      rows.push([a.aspect, eaCount(a.rest), '× ' + counts[i], counts[i] + ' + 1 = ' + (counts[i] + 1)]);
    });
    rows.push(['the abstract base', '', '+ 1', '']);
    rows.push(['in all', eaPlural(S, 'variant', 'variants'), eaInt(P) + ' + 1 = ' + eaInt(sub), eaInt(comp)]);
    var addI = 'no aspect gains a variant', addC = 'no aspect gains a variant';
    if (at >= 0) {
      var others = counts.filter(function (c, i) { return i !== at; }), q = 1;
      others.forEach(function (c) { q *= c; });
      addI = (others.length > 1 ? others.join(' × ') + ' = ' : '') + eaInt(q) + ' (' + eaInt(sub) + ' → ' + eaInt(sub + q) + ')';
      addC = '1 (' + eaInt(comp) + ' → ' + eaInt(comp + 1) + ')';
    }
    return {
      tiles: { gclCombos: counts.join(' × ') + ' = ' + eaInt(P), gclSubclass: eaInt(P) + ' + 1 = ' + eaInt(sub),
               gclCompose: counts.map(function (c) { return '(' + c + ' + 1)'; }).join(' + ') + ' = ' + eaInt(comp),
               gclRatio: eaTimes(R(BigInt(sub), BigInt(comp))), gclRefs: eaCount(names.slice(1)),
               gclAddSubclass: addI, gclAddCompose: addC },
      status: gofStatus(eaPlural(A, 'aspect', 'aspects') + ' with ' + eaPlural(S, 'variant', 'variants') + ': '
        + eaPlural(sub, 'class', 'classes') + ' as one subclass per combination, ' + eaInt(comp) + ' as one hierarchy per aspect'),
      table: { caption: 'Each aspect and the classes it brings', head: ['aspect', 'variants', 'one subclass per combination', 'one hierarchy per aspect'], rows: rows }
    };
  };
"""

GCL_VIEW_JS["factory"] = r"""
  /* Roles in display order: [key, label, one of them, formula]. */
  var GCL_ROLES = [
    ['af', 'abstract factory', 'abstract factory', '1'], ['cf', 'concrete factories', 'concrete factory', 'families'],
    ['ac', 'abstract creator', 'abstract creator', '1'], ['cs', 'concrete creators', 'concrete creator', 'families'],
    ['pm', 'prototype manager', 'prototype manager', '1'],
    ['ap', 'abstract products', 'abstract product', 'kinds'], ['cp', 'concrete products', 'concrete product', 'families × kinds']];
  function gclDesign(scheme, F, K) {
    var d = { ap: K, cp: F * K };
    if (scheme === 'abstract-factory') { d.af = 1; d.cf = F; }
    else if (scheme === 'factory-method') { d.ac = 1; d.cs = F; }
    else { d.pm = 1; }
    return d;
  }
  function gclSum(d) { var s = 0; GCL_ROLES.forEach(function (r) { if (gofHas(d, r[0])) s += d[r[0]]; }); return s; }
  GCL_VIEW.factory = function (inst) {
    var F = inst.families.length, K = inst.kinds.length, sc = inst.scheme, ch = inst.change;
    var d = gclDesign(sc, F, K), n = gclSum(d), proto = sc === 'prototype';
    var after = ch === 'family' ? gclDesign(sc, F + 1, K) : (ch === 'kind' ? gclDesign(sc, F, K + 1) : d);
    var parts = [], rows = [], addedParts = [];
    GCL_ROLES.forEach(function (r) {
      if (!gofHas(d, r[0])) return;
      parts.push(eaInt(d[r[0]]));
      var plus = after[r[0]] - d[r[0]];
      if (plus) addedParts.push(plus + ' ' + (plus === 1 ? r[2] : r[1]));
      var row = [r[1], r[3], eaInt(d[r[0]])];
      if (ch !== 'none') row.push(eaInt(after[r[0]]) + (plus ? ' (+' + plus + ')' : ''));
      rows.push(row);
    });
    var nAfter = gclSum(after), changed = 0, changedText = '0';
    if (ch === 'kind' && sc === 'abstract-factory') {
      changed = 1 + F;
      changedText = eaInt(changed) + ': the abstract factory and ' + eaPlural(F, 'concrete factory', 'concrete factories') + ', each given an operation to make the new kind';
    } else if (ch === 'kind' && sc === 'factory-method') {
      changed = 1 + F;
      changedText = eaInt(changed) + ': the abstract creator and ' + eaPlural(F, 'concrete creator', 'concrete creators') + ', each given a factory method for the new kind';
    }
    rows.push(['in all', '', eaInt(n)].concat(ch === 'none' ? [] : [eaInt(nAfter) + ' (+' + (nAfter - n) + ')']));
    var factories = sc === 'abstract-factory' ? '1 + ' + F + ' = ' + (1 + F) : (sc === 'factory-method' ? '1 + ' + F + ' = ' + (1 + F) : '1');
    var cfg = proto ? eaPlural(F, 'configuration', 'configurations') + ' of ' + eaPlural(K, 'prototype', 'prototypes') + ' (' + eaInt(F * K) + ' instances)'
      : 'none: the factory classes themselves fix what is made';
    var cfgChange = 'no change chosen';
    if (ch !== 'none') {
      if (!proto) cfgChange = 'none: this scheme configures no prototypes';
      else if (ch === 'family') cfgChange = '1 added, registering ' + eaPlural(K, 'prototype', 'prototypes');
      else cfgChange = eaInt(F) + ' changed, each registering 1 more prototype';
    }
    var what = ch === 'family' ? 'a new family' : 'a new kind of product';
    return {
      tiles: { gclProducts: F + ' × ' + K + ' = ' + eaInt(F * K), gclClasses: parts.join(' + ') + ' = ' + eaInt(n),
               gclFactories: factories, gclConfigs: cfg,
               gclAdded: ch === 'none' ? 'no change chosen' : eaInt(nAfter - n) + ' (' + eaInt(n) + ' → ' + eaInt(nAfter) + '): ' + addedParts.join(', '),
               gclChanged: ch === 'none' ? 'no change chosen' : changedText, gclConfigChange: cfgChange },
      status: gofStatus(sc + ': ' + F + ' × ' + K + ' products in ' + eaPlural(n, 'class', 'classes')
        + (ch === 'none' ? '' : '; ' + what + ' adds ' + eaInt(nAfter - n) + ' and edits ' + eaInt(changed))),
      table: { caption: 'The classes of the design under ' + sc + (ch === 'none' ? '' : ', before and after ' + what),
               head: ['classes', 'how many', 'now'].concat(ch === 'none' ? [] : ['after ' + what]), rows: rows }
    };
  };
"""


def _check_explosion(inst, fixed):
    seen, names = set(), []
    for a in inst["aspects"]:
        for nm in [a["aspect"]] + list(a["rest"]):
            if nm in seen:
                raise ValueError("Aspects: %s is named twice; every aspect and every variant is a class, and each "
                                 "needs a name of its own" % nm)
            seen.add(nm)
        names.append(a["aspect"])
    if inst["added"] != "-" and inst["added"] not in names:
        raise ValueError("The aspect that gains a variant, %s, is not one of the aspects (%s)"
                         % (inst["added"], ", ".join(names)))


# ---------------------------------------------------------------------------
# tree (gtr): compose, traverse, visit
# ---------------------------------------------------------------------------

GTR_JS = r"""
  var GTR_VIEW = {};
  function gtrCompute(view, inst, opts) { return eaRun(GTR_VIEW[view], inst, opts); }
  var GTR_NUM = { kind: 'num', min: '-10000000', max: '10000000' };
  /* The tree: {order, by, kids, root, depth, leaf} or a refusal. */
  function gtrTree(nodes) {
    var by = {}, kids = {}, roots = [], order = [];
    nodes.forEach(function (n) { by[n.node] = n; kids[n.node] = []; order.push(n.node); });
    nodes.forEach(function (n, i) {
      var w = 'Nodes, record ' + (i + 1) + ' (' + n.node + ')';
      if (n.parent === '-') { roots.push(n.node); return; }
      if (n.parent === n.node) eaRefuse(w + ' is its own parent');
      if (!gofHas(by, n.parent)) eaRefuse(w + ': its parent ' + n.parent + ' is not one of the nodes');
      kids[n.parent].push(n.node);
    });
    if (roots.length === 0) eaRefuse('No node has the parent -; a tree has exactly one root');
    if (roots.length > 1) eaRefuse('The tree has ' + roots.length + ' roots (' + roots.join(', ') + '); a tree has exactly one, the only node whose parent is -');
    var root = roots[0], depth = {}, queue = [root], k;
    depth[root] = 0;
    for (k = 0; k < queue.length; k += 1) {
      kids[queue[k]].forEach(function (c) { depth[c] = depth[queue[k]] + 1; queue.push(c); });
    }
    if (queue.length < order.length) {
      var lost = order.filter(function (x) { return !gofHas(depth, x); });
      eaRefuse('Nodes ' + lost.join(', ') + ' cannot be reached from the root ' + root + '; their parents form a cycle');
    }
    var leaf = {}, value = {}, role = {};
    nodes.forEach(function (n, i) {
      var w = 'Nodes, record ' + (i + 1) + ' (' + n.node + ')';
      if (n.value === '-') { leaf[n.node] = false; }
      else {
        try { value[n.node] = eaScalar(GTR_NUM, n.value, w + ': value'); } catch (e) { eaRefuse(e.message); }
        leaf[n.node] = true;
        if (kids[n.node].length) eaRefuse(w + ' has a value, so it is a leaf, and a leaf has no children, but it has ' + kids[n.node].length + ' (' + kids[n.node].join(', ') + '); a composite has the value -');
      }
      var r = leaf[n.node] ? 'leaf' : 'composite';
      if (gofHas(role, n.kind) && role[n.kind].r !== r) {
        eaRefuse('The kind ' + n.kind + ' is a ' + role[n.kind].r + ' class for ' + role[n.kind].at + ' and a ' + r + ' class for ' + n.node + '; a class is one or the other');
      }
      if (!gofHas(role, n.kind)) role[n.kind] = { r: r, at: n.node };
    });
    var maxD = 0;
    order.forEach(function (x) { if (depth[x] > maxD) maxD = depth[x]; });
    return { order: order, by: by, kids: kids, root: root, depth: depth, maxDepth: maxD, leaf: leaf, value: value, bfs: queue };
  }
  function gtrMember(t, name, what) { if (!gofHas(t.by, name)) eaRefuse(what + ': ' + name + ' is not one of the nodes'); }
"""

GTR_VIEW_JS = {}

GTR_VIEW_JS["compose"] = r"""
  GTR_VIEW.compose = function (inst) {
    var t = gtrTree(inst.nodes), leaves = [], comps = [], sub = {}, size = {}, under = {};
    inst.asks.forEach(function (a) { gtrMember(t, a, 'Asked to add a child'); });
    t.order.forEach(function (x) { (t.leaf[x] ? leaves : comps).push(x); });
    for (var i = t.bfs.length - 1; i >= 0; i -= 1) {
      var x = t.bfs[i];
      sub[x] = t.leaf[x] ? t.value[x] : R0; size[x] = 1; under[x] = t.leaf[x] ? 1 : 0;
      t.kids[x].forEach(function (c) { sub[x] = Radd(sub[x], sub[c]); size[x] += size[c]; under[x] += under[c]; });
    }
    var N = t.order.length, safe = inst.declare === 'safe';
    var askedLeaves = inst.asks.filter(function (a) { return t.leaf[a]; }), taken = inst.asks.filter(function (a) { return !t.leaf[a]; });
    var rows = comps.map(function (x) {
      return [x, t.by[x].kind, eaInt(t.kids[x].length), eaInt(under[x]), gofDec(sub[x]), eaInt(size[x])];
    });
    var leafText = eaCount(askedLeaves);
    if (askedLeaves.length) leafText += safe ? ' (refused by the compiler: add is declared only on composites)'
      : ' (accepted by the interface: each ignores it or fails at run time)';
    return {
      tiles: { gtrNodes: eaInt(N), gtrLeaves: eaInt(leaves.length), gtrComposites: eaInt(comps.length), gtrDepth: eaInt(t.maxDepth),
               gtrCalls: eaInt(N) + ': 1 from the client + ' + eaInt(N - 1) + ' forwarded by composites', gtrTotal: gofDec(sub[t.root]),
               gtrAskLeaves: leafText, gtrAskTaken: eaCount(taken) },
      status: gofStatus('One operation on ' + t.root + ' makes ' + eaPlural(N, 'call', 'calls') + ' and totals ' + gofDec(sub[t.root])),
      table: { caption: 'Each composite: its children, the leaves below it, its subtotal and the calls in its subtree',
               head: ['composite', 'kind', 'children', 'leaves below', 'subtotal', 'calls'], rows: rows }
    };
  };
"""

GTR_VIEW_JS["traverse"] = r"""
  GTR_VIEW.traverse = function (inst) {
    var t = gtrTree(inst.nodes), pre = [], post = [];
    if (inst.find !== '-') gtrMember(t, inst.find, 'The node to find');
    (function walk(x) { pre.push(x); t.kids[x].forEach(walk); post.push(x); })(t.root);
    var lvl = t.bfs, N = t.order.length, pos = function (list, x) { return list.indexOf(x) + 1; };
    var found = inst.find === '-' ? 'no node to find'
      : 'pre-order ' + pos(pre, inst.find) + ', post-order ' + pos(post, inst.find) + ', level-order ' + pos(lvl, inst.find) + ' (of ' + N + ')';
    var rows = t.order.map(function (x) { return [x, t.by[x].parent, eaInt(t.depth[x]), String(pos(pre, x)), String(pos(post, x)), String(pos(lvl, x))]; });
    return {
      tiles: { gtrNodes: eaInt(N), gtrPre: pre.join(', '), gtrPost: post.join(', '), gtrLevel: lvl.join(', '), gtrFind: found },
      status: gofStatus('Three orders over ' + eaPlural(N, 'node', 'nodes') + ': pre-order starts at ' + pre[0] + ', post-order at ' + post[0]),
      table: { caption: 'Each node and its place in each order', head: ['node', 'parent', 'depth', 'pre-order', 'post-order', 'level-order'], rows: rows }
    };
  };
"""

GTR_VIEW_JS["visit"] = r"""
  GTR_VIEW.visit = function (inst) {
    var t = gtrTree(inst.nodes), vs = inst.visitors, V = vs.length, N = t.order.length, kinds = [], per = {};
    t.order.forEach(function (x) { var k = t.by[x].kind; if (!gofHas(per, k)) { per[k] = 0; kinds.push(k); } per[k] += 1; });
    var K = kinds.length, ad = inst.adding;
    var rows = kinds.map(function (k) { return [k, eaInt(per[k])].concat(vs.map(function () { return eaInt(per[k]); })); });
    rows.push(['in all', eaInt(N)].concat(vs.map(function () { return eaInt(N); })));
    var withV = 'no addition chosen', without = 'no addition chosen';
    if (ad === 'operation') {
      withV = '1 added (the new visitor), 0 changed';
      without = '0 added, ' + eaInt(K + 1) + ' changed (the abstract element and ' + eaPlural(K, 'element class', 'element classes') + ')';
    } else if (ad === 'kind') {
      withV = '1 added (the new element class), ' + eaInt(V + 1) + ' changed (the abstract visitor and ' + eaPlural(V, 'visitor', 'visitors') + ')';
      without = '1 added (the new element class), 0 changed';
    }
    return {
      tiles: { gtrAccepts: eaInt(N * V) + ': ' + eaPlural(N, 'node', 'nodes') + ' × ' + eaPlural(V, 'visitor', 'visitors'),
               gtrVisits: eaInt(N * V), gtrElements: '1 + ' + K + ' = ' + (K + 1) + ' (the abstract element; ' + kinds.join(', ') + ')',
               gtrVisitorClasses: '1 + ' + V + ' = ' + (V + 1) + ' (the abstract visitor; ' + vs.join(', ') + ')',
               gtrMethods: K + ' × ' + V + ' + ' + K + ' = ' + eaInt(K * V + K), gtrMethodsPlain: K + ' × ' + V + ' = ' + eaInt(K * V),
               gtrAddVisitor: withV, gtrAddPlain: without },
      status: gofStatus(eaPlural(V, 'visitor', 'visitors') + ' over ' + eaPlural(N, 'node', 'nodes') + ' of ' + eaPlural(K, 'kind', 'kinds')
        + ': ' + eaPlural(N * V, 'accept call', 'accept calls') + ' and as many visit calls'),
      table: { caption: 'Visit calls by kind (rows) and visitor (columns)', head: ['kind', 'nodes'].concat(vs), rows: rows }
    };
  };
"""

_GTR_NUM = ea.num(lo=-ea.LIMIT)


def _tree(nodes):
    """Mirror of gtrTree's refusals; returns (by, kids, leaf)."""
    by = {n["node"]: n for n in nodes}
    kids = {n["node"]: [] for n in nodes}
    roots = []
    for i, n in enumerate(nodes):
        w = "Nodes, record %d (%s)" % (i + 1, n["node"])
        if n["parent"] == "-":
            roots.append(n["node"])
            continue
        if n["parent"] == n["node"]:
            raise ValueError("%s is its own parent" % w)
        if n["parent"] not in by:
            raise ValueError("%s: its parent %s is not one of the nodes" % (w, n["parent"]))
        kids[n["parent"]].append(n["node"])
    if not roots:
        raise ValueError("No node has the parent -; a tree has exactly one root")
    if len(roots) > 1:
        raise ValueError("The tree has %d roots (%s); a tree has exactly one, the only node whose parent is -"
                         % (len(roots), ", ".join(roots)))
    reached, queue = {roots[0]}, [roots[0]]
    for x in queue:
        for c in kids[x]:
            reached.add(c)
            queue.append(c)
    if len(queue) < len(nodes):
        lost = [n["node"] for n in nodes if n["node"] not in reached]
        raise ValueError("Nodes %s cannot be reached from the root %s; their parents form a cycle"
                         % (", ".join(lost), roots[0]))
    leaf, role = {}, {}
    for i, n in enumerate(nodes):
        w = "Nodes, record %d (%s)" % (i + 1, n["node"])
        if n["value"] == "-":
            leaf[n["node"]] = False
        else:
            ea.parse_scalar(_GTR_NUM, n["value"], w + ": value")
            leaf[n["node"]] = True
            if kids[n["node"]]:
                raise ValueError("%s has a value, so it is a leaf, and a leaf has no children, but it has %d (%s); "
                                 "a composite has the value -" % (w, len(kids[n["node"]]), ", ".join(kids[n["node"]])))
        r = "leaf" if leaf[n["node"]] else "composite"
        if n["kind"] in role and role[n["kind"]][0] != r:
            raise ValueError("The kind %s is a %s class for %s and a %s class for %s; a class is one or the other"
                             % (n["kind"], role[n["kind"]][0], role[n["kind"]][1], r, n["node"]))
        role.setdefault(n["kind"], (r, n["node"]))
    return by, kids, leaf


def _check_compose(inst, fixed):
    by, _kids, _leaf = _tree(inst["nodes"])
    for a in inst["asks"]:
        if a not in by:
            raise ValueError("Asked to add a child: %s is not one of the nodes" % a)


def _check_traverse(inst, fixed):
    by, _kids, _leaf = _tree(inst["nodes"])
    if inst["find"] != "-" and inst["find"] not in by:
        raise ValueError("The node to find: %s is not one of the nodes" % inst["find"])


def _check_visit(inst, fixed):
    _tree(inst["nodes"])


# ---------------------------------------------------------------------------
# expr (gex): interpret
# ---------------------------------------------------------------------------

GEX_JS = r"""
  var GEX_VIEW = {};
  function gexCompute(view, inst, opts) { return eaRun(GEX_VIEW[view], inst, opts); }
  var GEX_CLASSES = ['Number', 'Variable', 'Add', 'Subtract', 'Multiply', 'Divide', 'Negate'];
  var GEX_NAME = /^[A-Za-z][A-Za-z0-9_]*$/;
  function gexLex(s) {
    var toks = [], i = 0, m, rest;
    while (i < s.length) {
      var c = s.charAt(i);
      if (c === ' ') { i += 1; continue; }
      if ('+-*/()'.indexOf(c) >= 0) { toks.push({ t: c, at: i, end: i + 1 }); i += 1; continue; }
      rest = s.slice(i);
      m = /^\d+(?:\.(\d+))?/.exec(rest);
      if (m) {
        if ((m[1] || '').length > 6) eaRefuse('The expression: the number ' + m[0] + ' has more than 6 decimal places');
        if (Rcmp(Rparse(m[0]), R(10000000n)) > 0) eaRefuse('The expression: the number ' + m[0] + ' is more than 10,000,000');
        toks.push({ t: 'num', v: m[0], at: i, end: i + m[0].length }); i += m[0].length; continue;
      }
      m = /^[A-Za-z][A-Za-z0-9_]*/.exec(rest);
      if (m) { toks.push({ t: 'name', v: m[0], at: i, end: i + m[0].length }); i += m[0].length; continue; }
      eaRefuse('The expression has ' + eaQuote(c) + ' at character ' + (i + 1) + '; it reads numbers, names, + - * / and parentheses');
    }
    return toks;
  }
  function gexShow(tok) { return tok.t === 'num' || tok.t === 'name' ? tok.v : tok.t; }
  /* Recursive descent: + - over * / over unary minus over numbers, names and ( ). Left-associative. */
  function gexParse(s) {
    var toks = gexLex(s), p = 0;
    function mk(cls, kids, at, end, v) { return { cls: cls, kids: kids, at: at, end: end, oat: at, oend: end, v: v }; }
    function primary() {
      var tk = toks[p];
      if (!tk) eaRefuse('The expression ends where a number, a name, - or ( should be');
      if (tk.t === 'num') { p += 1; return mk('Number', [], tk.at, tk.end, tk.v); }
      if (tk.t === 'name') { p += 1; return mk('Variable', [], tk.at, tk.end, tk.v); }
      if (tk.t === '(') {
        p += 1;
        var e = sum(), cl = toks[p];
        if (!cl || cl.t !== ')') eaRefuse('The expression opens a parenthesis at character ' + (tk.at + 1) + ' and does not close it');
        p += 1; e.oat = tk.at; e.oend = cl.end;
        return e;
      }
      eaRefuse('The expression has ' + gexShow(tk) + ' at character ' + (tk.at + 1) + ', where a number, a name, - or ( should be');
    }
    function unary() {
      var tk = toks[p];
      if (tk && tk.t === '-') { p += 1; var k = unary(); return mk('Negate', [k], tk.at, k.oend); }
      return primary();
    }
    function chain(next, ops, names) {
      return function () {
        var left = next();
        while (toks[p] && ops.indexOf(toks[p].t) >= 0) {
          var op = toks[p].t; p += 1;
          var right = next();
          left = mk(names[ops.indexOf(op)], [left, right], left.oat, right.oend);
        }
        return left;
      };
    }
    var product = chain(unary, ['*', '/'], ['Multiply', 'Divide']), sum = chain(product, ['+', '-'], ['Add', 'Subtract']);
    if (!toks.length) eaRefuse('The expression is empty');
    var tree = sum();
    if (p < toks.length) {
      var tk = toks[p];
      if (tk.t === ')') eaRefuse('The expression has ) at character ' + (tk.at + 1) + ' with no ( to close');
      eaRefuse('The expression has ' + gexShow(tk) + ' at character ' + (tk.at + 1) + ', where an operator or the end should be');
    }
    return tree;
  }
"""

GEX_VIEW_JS = {}

GEX_VIEW_JS["interpret"] = r"""
  GEX_VIEW.interpret = function (inst) {
    var s = inst.expr, ctx = {}, names = [];
    inst.context.forEach(function (c, i) {
      if (!GEX_NAME.test(c.name)) eaRefuse('Context, record ' + (i + 1) + ': ' + c.name + ' cannot be named in an expression; a variable is a letter followed by letters, digits or underscores');
      ctx[c.name] = c.value; names.push(c.name);
    });
    var tree = gexParse(s), post = [], used = [], seen = {}, maxD = 0;
    (function walk(n, d) {
      if (d > maxD) maxD = d;
      n.kids.forEach(function (k) { walk(k, d + 1); });
      post.push(n);
      if (n.cls === 'Variable' && !gofHas(seen, n.v)) { seen[n.v] = true; used.push(n.v); }
    })(tree, 0);
    var unbound = used.filter(function (v) { return !gofHas(ctx, v); });
    if (unbound.length) eaRefuse('The context gives no value for ' + unbound.join(', ') + '; add a record name, value for each');
    var text = function (n) { return s.slice(n.at, n.end); }, val = function (n) { return n.val; };
    post.forEach(function (n) {
      var a = n.kids[0], b = n.kids[1];
      if (n.cls === 'Number') n.val = Rparse(n.v);
      else if (n.cls === 'Variable') n.val = ctx[n.v];
      else if (n.cls === 'Negate') n.val = Rneg(val(a));
      else if (n.cls === 'Add') n.val = Radd(val(a), val(b));
      else if (n.cls === 'Subtract') n.val = Rsub(val(a), val(b));
      else if (n.cls === 'Multiply') n.val = Rmul(val(a), val(b));
      else {
        if (b.val.n === 0n) eaRefuse('Division by zero: the divisor ' + text(b) + ' is 0 in ' + text(n));
        n.val = Rdiv(val(a), val(b));
      }
    });
    var count = {};
    post.forEach(function (n) { count[n.cls] = (count[n.cls] || 0) + 1; });
    var present = GEX_CLASSES.filter(function (c) { return count[c]; });
    var N = post.length;
    return {
      tiles: { gexValue: gofNum(tree.val), gexNodes: eaInt(N),
               gexByClass: present.map(function (c) { return c + ' ' + count[c]; }).join(', '),
               gexClasses: present.length + ' of the 7', gexCalls: eaInt(N) + ': 1 from the client + ' + eaInt(N - 1) + ' from nodes to their operands',
               gexDepth: eaInt(maxD), gexVars: eaCount(used), gexUnused: eaCount(names.filter(function (v) { return !gofHas(seen, v); })) },
      status: gofStatus('The expression interprets to ' + gofNum(tree.val) + ' in ' + eaPlural(N, 'interpret call', 'interpret calls')),
      table: { caption: 'Each node in post-order, the order its value is known', head: ['step', 'class', 'subexpression', 'value'],
               rows: post.map(function (n, i) { return [String(i + 1), n.cls, text(n), gofNum(n.val)]; }) }
    };
  };
"""

_GEX_NAME = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")


def _gex_lex(s):
    toks, i = [], 0
    while i < len(s):
        c = s[i]
        if c == " ":
            i += 1
            continue
        if c in "+-*/()":
            toks.append((c, None, i, i + 1))
            i += 1
            continue
        m = re.match(r"\d+(?:\.(\d+))?", s[i:])
        if m:
            if len(m.group(1) or "") > 6:
                raise ValueError("The expression: the number %s has more than 6 decimal places" % m.group(0))
            if Fraction(m.group(0)) > ea.LIMIT:
                raise ValueError("The expression: the number %s is more than 10,000,000" % m.group(0))
            toks.append(("num", m.group(0), i, i + len(m.group(0))))
            i += len(m.group(0))
            continue
        m = re.match(r"[A-Za-z][A-Za-z0-9_]*", s[i:])
        if m:
            toks.append(("name", m.group(0), i, i + len(m.group(0))))
            i += len(m.group(0))
            continue
        raise ValueError("The expression has %s at character %d; it reads numbers, names, + - * / and parentheses"
                         % (ea._quote(c), i + 1))
    return toks


def gex_parse(s):
    """Mirror of gexParse: a tree of dicts {cls, kids, at, end, v}, or ValueError with the page's sentence."""
    toks = _gex_lex(s)
    pos = [0]

    def show(tk):
        return tk[1] if tk[0] in ("num", "name") else tk[0]

    def mk(cls, kids, at, end, v=None):
        return {"cls": cls, "kids": kids, "at": at, "end": end, "oat": at, "oend": end, "v": v}

    def primary():
        if pos[0] >= len(toks):
            raise ValueError("The expression ends where a number, a name, - or ( should be")
        tk = toks[pos[0]]
        if tk[0] == "num":
            pos[0] += 1
            return mk("Number", [], tk[2], tk[3], tk[1])
        if tk[0] == "name":
            pos[0] += 1
            return mk("Variable", [], tk[2], tk[3], tk[1])
        if tk[0] == "(":
            pos[0] += 1
            e = add()
            if pos[0] >= len(toks) or toks[pos[0]][0] != ")":
                raise ValueError("The expression opens a parenthesis at character %d and does not close it" % (tk[2] + 1))
            e["oat"], e["oend"] = tk[2], toks[pos[0]][3]
            pos[0] += 1
            return e
        raise ValueError("The expression has %s at character %d, where a number, a name, - or ( should be"
                         % (show(tk), tk[2] + 1))

    def unary():
        if pos[0] < len(toks) and toks[pos[0]][0] == "-":
            at = toks[pos[0]][2]
            pos[0] += 1
            k = unary()
            return mk("Negate", [k], at, k["oend"])
        return primary()

    def chain(nxt, ops):
        def run():
            left = nxt()
            while pos[0] < len(toks) and toks[pos[0]][0] in ops:
                op = toks[pos[0]][0]
                pos[0] += 1
                right = nxt()
                left = mk(ops[op], [left, right], left["oat"], right["oend"])
            return left
        return run

    mul = chain(unary, {"*": "Multiply", "/": "Divide"})
    add = chain(mul, {"+": "Add", "-": "Subtract"})
    if not toks:
        raise ValueError("The expression is empty")
    tree = add()
    if pos[0] < len(toks):
        tk = toks[pos[0]]
        if tk[0] == ")":
            raise ValueError("The expression has ) at character %d with no ( to close" % (tk[2] + 1))
        raise ValueError("The expression has %s at character %d, where an operator or the end should be"
                         % (show(tk), tk[2] + 1))
    return tree


def gex_value(s, context):
    """The exact value of expression s under context {name: Fraction}, mirroring the view's refusals."""
    tree = gex_parse(s)
    post, used = [], []

    def walk(n):
        for k in n["kids"]:
            walk(k)
        post.append(n)
        if n["cls"] == "Variable" and n["v"] not in used:
            used.append(n["v"])
    walk(tree)
    unbound = [v for v in used if v not in context]
    if unbound:
        raise ValueError("The context gives no value for %s; add a record name, value for each" % ", ".join(unbound))
    for n in post:
        k = n["kids"]
        c = n["cls"]
        if c == "Number":
            n["val"] = Fraction(n["v"])
        elif c == "Variable":
            n["val"] = Fraction(context[n["v"]])
        elif c == "Negate":
            n["val"] = -k[0]["val"]
        elif c == "Add":
            n["val"] = k[0]["val"] + k[1]["val"]
        elif c == "Subtract":
            n["val"] = k[0]["val"] - k[1]["val"]
        elif c == "Multiply":
            n["val"] = k[0]["val"] * k[1]["val"]
        else:
            if k[1]["val"] == 0:
                raise ValueError("Division by zero: the divisor %s is 0 in %s"
                                 % (s[k[1]["at"]:k[1]["end"]], s[n["at"]:n["end"]]))
            n["val"] = k[0]["val"] / k[1]["val"]
    return tree["val"]


def _check_interpret(inst, fixed):
    ctx = {}
    for i, c in enumerate(inst["context"]):
        if not _GEX_NAME.match(c["name"]):
            raise ValueError("Context, record %d: %s cannot be named in an expression; a variable is a letter followed "
                             "by letters, digits or underscores" % (i + 1, c["name"]))
        ctx[c["name"]] = c["value"]
    gex_value(inst["expr"], ctx)


# ---------------------------------------------------------------------------
# The mode specs (family A)
# ---------------------------------------------------------------------------

_N = ea.NAME
_NUM = ea.num(lo=-ea.LIMIT)

_EXPLOSION_RULES = (
    "Each record is one aspect that varies, then its variants (2 to 4 aspects, 1 to 8 variants each); every name is "
    "a class and is used once. Combinations = the product of the variant counts. With one subclass per combination "
    "the design has that product + 1 classes (one abstract base). With one hierarchy per aspect, joined by "
    "composition, each aspect has 1 abstract class + 1 concrete class per variant, so the design has the sum of the "
    "variant counts + the number of aspects; the client holds the first aspect's abstract class, and each of its "
    "objects holds one reference per other aspect. The ratio is the first count over the second. One new variant "
    "of the added aspect adds the product of the other aspects' counts under subclassing and 1 class under "
    "composition; neither design edits an existing class for it.")

_FACTORY_RULES = (
    "F families × K kinds of product. Every scheme has K abstract products and F × K concrete product classes, "
    "counted as if each concrete product differs in behaviour. Abstract Factory adds 1 abstract factory and 1 "
    "concrete factory per family: 1 + F + K + F × K. Factory Method has 1 abstract creator declaring one factory "
    "method per kind and 1 concrete creator subclass per family overriding them: 1 + F + K + F × K, the same "
    "count, the difference being that the client subclasses the creator instead of composing with a factory "
    "object. Prototype adds 1 "
    "prototype manager, a registry keyed by kind, and no factory subclasses: 1 + K + F × K; a family is a "
    "configuration of K prototype instances. A new family adds its K products and, under Abstract Factory, 1 "
    "concrete factory, under Factory Method 1 concrete creator, under Prototype 1 configuration; it edits no "
    "existing class. A new kind adds 1 abstract product and F concrete products; under Abstract Factory it "
    "edits the abstract factory and every concrete factory (1 + F classes), each gaining an operation, and under "
    "Factory Method the abstract creator and every concrete creator (1 + F), each gaining a factory method; under Prototype it edits no class, and each of the "
    "F configurations registers one more prototype. The client is not counted.")

CLASSES = {
    "prefix": "gcl", "fn": "gclCompute", "title": "Classes", "js": GCL_JS,
    "views": {
        "explosion": {
            "fields": [("aspects", vrec("Aspects (aspect, then its variants)", [("aspect", _N)], _N, "variant", 1, 8,
                                        unique=True, rows=4, lo=2, hi=4), None),
                       ("added", ea.field("The aspect that gains one variant (- for none)", ea.PARENT), "-")],
            "tiles": [("Combinations", "gclCombos"),
                      ("Classes, one subclass per combination", "gclSubclass"),
                      ("Classes, one hierarchy per aspect", "gclCompose"),
                      ("Subclassing against composition", "gclRatio"),
                      ("References each object of the first aspect holds", "gclRefs"),
                      ("A new variant: classes added by subclassing", "gclAddSubclass"),
                      ("A new variant: classes added by composition", "gclAddCompose")],
            "check": _check_explosion, "subtitle": "every combination a subclass, or one hierarchy per aspect",
            "rules": _EXPLOSION_RULES, "js": GCL_VIEW_JS["explosion"],
        },
        "factory": {
            "fields": [("families", {"kind": "list", "what": "Families (1 to 8 names)", "control": "text",
                                     "lo": 1, "hi": 8, "things": "families", "each": _N}, None),
                       ("kinds", {"kind": "list", "what": "Kinds of product (1 to 8 names)", "control": "text",
                                  "lo": 1, "hi": 8, "things": "kinds", "each": _N}, None),
                       ("scheme", ea.choice("The scheme", "abstract-factory", "factory-method", "prototype"),
                        "abstract-factory"),
                       ("change", ea.choice("The change", "none", "family", "kind"), "none")],
            "tiles": [("Concrete products (families × kinds)", "gclProducts"),
                      ("Classes in the design", "gclClasses"),
                      ("Classes that create (factories or creators)", "gclFactories"),
                      ("Prototype configurations", "gclConfigs"),
                      ("Classes the change adds", "gclAdded"),
                      ("Existing classes the change edits", "gclChanged"),
                      ("Configurations the change touches", "gclConfigChange")],
            "check": None, "subtitle": "families and kinds of product, and who makes them",
            "rules": _FACTORY_RULES, "js": GCL_VIEW_JS["factory"],
        },
    },
}

_NODES = ("nodes", ea.rec("Nodes (node, parent, kind, value)",
                          [("node", _N), ("parent", ea.PARENT), ("kind", _N), ("value", ea.PARENT)],
                          unique=True, rows=6), None)

_TREE_RULES = (
    "Each record is one node: its name, its parent (- for the root; exactly one root), its kind (a class name) and "
    "its value, a decimal for a leaf and - for a composite. A leaf has no children; a composite may have none. "
    "Children are taken in record order. A kind is either a leaf class or a composite class, never both. Depth "
    "counts the edges on the longest path down from the root (a root alone is at depth 0). ")

TREE = {
    "prefix": "gtr", "fn": "gtrCompute", "title": "A tree of parts", "js": GTR_JS,
    "views": {
        "compose": {
            "fields": [_NODES,
                       ("asks", {"kind": "list", "what": "Nodes asked to add a child (names; empty for none)",
                                 "control": "text", "lo": 0, "hi": ea.MAX_RECORDS, "things": "nodes", "each": _N}, ""),
                       ("declare", ea.choice("Child operations are declared", "safe", "transparent"), "safe")],
            "tiles": [("Nodes", "gtrNodes"), ("Leaves", "gtrLeaves"), ("Composites", "gtrComposites"),
                      ("Depth", "gtrDepth"), ("Calls one operation on the root makes", "gtrCalls"),
                      ("The total (the sum of the leaves)", "gtrTotal"),
                      ("Leaves asked to add a child", "gtrAskLeaves"),
                      ("Composites asked to add a child (they do)", "gtrAskTaken")],
            "check": _check_compose, "subtitle": "one operation over a whole and its parts",
            "rules": _TREE_RULES + (
                "One operation on the root makes one call per node: the client's call on the root, and one call from "
                "each composite to each of its children. The total is the sum of the leaf values, exactly; a "
                "composite's subtotal is the sum of the leaves below it, and its calls are the nodes in its subtree. "
                "A composite asked to add a child does. A leaf asked to: under the safe declaration (add declared "
                "only on the composite class) the call does not compile; under the transparent one (add declared on "
                "every component) it compiles, and the leaf ignores it or fails at run time."),
            "js": GTR_VIEW_JS["compose"],
        },
        "traverse": {
            "fields": [_NODES, ("find", ea.field("A node to find (- for none)", ea.PARENT), "-")],
            "tiles": [("Nodes", "gtrNodes"), ("Pre-order", "gtrPre"), ("Post-order", "gtrPost"),
                      ("Level-order", "gtrLevel"), ("The node to find, by position", "gtrFind")],
            "check": _check_traverse, "subtitle": "one tree, three orders of visiting it",
            "rules": _TREE_RULES + (
                "Pre-order visits a node, then each child's subtree in order; post-order visits each child's subtree "
                "in order, then the node; level-order visits the root, then every node at depth 1, then depth 2, "
                "each level left to right in record order of the children. Positions count from 1."),
            "js": GTR_VIEW_JS["traverse"],
        },
        "visit": {
            "fields": [_NODES,
                       ("visitors", {"kind": "list", "what": "Visitors, the operations (1 to 4 names)", "control": "text",
                                     "lo": 1, "hi": 4, "things": "visitors", "each": _N}, None),
                       ("adding", ea.choice("The addition", "none", "operation", "kind"), "none")],
            "tiles": [("Accept calls", "gtrAccepts"), ("Visit calls", "gtrVisits"),
                      ("Element classes", "gtrElements"), ("Visitor classes", "gtrVisitorClasses"),
                      ("Methods written, with Visitor", "gtrMethods"),
                      ("Methods written, operations on the elements", "gtrMethodsPlain"),
                      ("The addition, with Visitor", "gtrAddVisitor"),
                      ("The addition, operations on the elements", "gtrAddPlain")],
            "check": _check_visit, "subtitle": "operations as visitors, or as methods of the elements",
            "rules": _TREE_RULES + (
                "The structure asks every node to accept each visitor once, and each accept makes one visit call on "
                "the visitor's method for that node's kind: nodes × visitors of each. Element classes are 1 abstract "
                "element + 1 per kind; visitor classes are 1 abstract visitor + 1 per visitor. Methods written, "
                "counting implementations only: with Visitor, kinds × visitors visit methods + 1 accept per kind; "
                "with each operation a method of the element classes, kinds × visitors. A new operation is 1 new "
                "visitor and changes nothing, against a change to the abstract element and every element class; a "
                "new kind is 1 new element class that changes the abstract visitor and every visitor, against "
                "nothing changed."),
            "js": GTR_VIEW_JS["visit"],
        },
    },
}

EXPR = {
    "prefix": "gex", "fn": "gexCompute", "title": "An interpreter", "js": GEX_JS,
    "views": {
        "interpret": {
            "fields": [("expr", expr("The expression"), None),
                       ("context", ea.rec("Context (name, value; empty for none)", [("name", _N), ("value", _NUM)],
                                          unique=True, rows=3, lo=0), "")],
            "tiles": [("Value", "gexValue"), ("Nodes", "gexNodes"), ("Nodes by class", "gexByClass"),
                      ("Classes used", "gexClasses"), ("Interpret calls", "gexCalls"), ("Depth", "gexDepth"),
                      ("Variables used", "gexVars"), ("Context names not used", "gexUnused")],
            "check": _check_interpret, "subtitle": "a class per rule, an expression as a tree of objects",
            "rules": "The language: numbers (at most 6 decimal places, at most 10,000,000), variables (a letter, then "
                     "letters, digits or underscores; letter case counts), + - * /, a minus in front, and "
                     "parentheses. * and / bind tighter than + and -, a leading minus tighter than either, and each "
                     "operator groups from the left (8 - 3 - 2 takes away the 3 first and then the 2). Each number, variable and operator "
                     "is one node, of the class Number, Variable, Add, Subtract, Multiply, Divide or Negate; "
                     "parentheses make no node, and -3 is a Negate of the Number 3. Interpreting the root makes one "
                     "interpret call per node. Values are exact fractions; a variable takes its value from the "
                     "context, and one the context does not give, or a divisor that is 0, is refused. Depth counts "
                     "the edges on the longest path down from the root.",
            "js": GEX_VIEW_JS["interpret"],
        },
    },
}

SPECS = {"classes": CLASSES, "tree": TREE, "expr": EXPR}
MODES_A = tuple(SPECS)

# Worked cfgs, one per view, every preset pinned (each tile string counted by
# hand and read off a rendered page with labcheck --observe). Authors may copy
# the shape; a lesson uses a design of its own (PLAN section C).
SAMPLES = [{'mode': 'classes',
  'view': 'explosion',
  'presets': [{'id': 'coffee',
               'label': 'A coffee order: size, milk, cup',
               'aspects': 'size, small, medium, large; milk, whole, oat; cup, paper, ceramic',
               'added': 'milk',
               'expect': {'gclCombos': '3 × 2 × 2 = 12',
                          'gclSubclass': '12 + 1 = 13',
                          'gclCompose': '(3 + 1) + (2 + 1) + (2 + 1) = 10',
                          'gclRatio': '13/10 ≈ 1.3×',
                          'gclRefs': '2: milk, cup',
                          'gclAddSubclass': '3 × 2 = 6 (13 → 19)',
                          'gclAddCompose': '1 (10 → 11)'}},
              {'id': 'print-shop',
               'label': 'A print shop: job and finish',
               'aspects': 'job, flyer, poster, banner, card; finish, matte, gloss',
               'added': 'finish',
               'expect': {'gclCombos': '4 × 2 = 8',
                          'gclSubclass': '8 + 1 = 9',
                          'gclCompose': '(4 + 1) + (2 + 1) = 8',
                          'gclRatio': '9/8 ≈ 1.1×',
                          'gclRefs': '1: finish',
                          'gclAddSubclass': '4 (9 → 13)',
                          'gclAddCompose': '1 (8 → 9)'}},
              {'id': 'bike-dock',
               'label': 'A bike-share dock: four aspects',
               'aspects': 'frame, city, cargo; motor, none, assist; lock, key, app; rack, front, rear, bare',
               'expect': {'gclCombos': '2 × 2 × 2 × 3 = 24',
                          'gclSubclass': '24 + 1 = 25',
                          'gclCompose': '(2 + 1) + (2 + 1) + (2 + 1) + (3 + 1) = 13',
                          'gclRatio': '25/13 ≈ 1.9×',
                          'gclRefs': '3: motor, lock, rack',
                          'gclAddSubclass': 'no aspect gains a variant',
                          'gclAddCompose': 'no aspect gains a variant'}}]},
 {'mode': 'classes',
  'view': 'factory',
  'families': 'rustic french vegan',
  'kinds': 'loaf roll',
  'presets': [{'id': 'af-kind',
               'label': 'A bakery under Abstract Factory, a new kind',
               'scheme': 'abstract-factory',
               'change': 'kind',
               'expect': {'gclProducts': '3 × 2 = 6',
                          'gclClasses': '1 + 3 + 2 + 6 = 12',
                          'gclFactories': '1 + 3 = 4',
                          'gclConfigs': 'none: the factory classes themselves fix what is made',
                          'gclAdded': '4 (12 → 16): 1 abstract product, 3 concrete products',
                          'gclChanged': '4: the abstract factory and 3 concrete factories, each given an operation '
                                        'to make the new kind',
                          'gclConfigChange': 'none: this scheme configures no prototypes'}},
              {'id': 'fm-family',
               'label': 'The bakery under Factory Method, a new family',
               'scheme': 'factory-method',
               'change': 'family',
               'expect': {'gclClasses': '1 + 3 + 2 + 6 = 12',
                          'gclFactories': '1 + 3 = 4',
                          'gclAdded': '3 (12 → 15): 1 concrete creator, 2 concrete products',
                          'gclChanged': '0'}},
              {'id': 'proto-kind',
               'label': 'The bakery under Prototype, a new kind',
               'scheme': 'prototype',
               'change': 'kind',
               'expect': {'gclClasses': '1 + 2 + 6 = 9',
                          'gclFactories': '1',
                          'gclConfigs': '3 configurations of 2 prototypes (6 instances)',
                          'gclAdded': '4 (9 → 13): 1 abstract product, 3 concrete products',
                          'gclChanged': '0',
                          'gclConfigChange': '3 changed, each registering 1 more prototype'}}]},
 {'mode': 'tree',
  'view': 'compose',
  'presets': [{'id': 'hamper',
               'label': 'A gift hamper, safe declaration',
               'nodes': 'hamper, -, Box, -; tray, hamper, Box, -; jam, hamper, Item, 4.5; bread, tray, Item, 3.25; '
                        'scone, tray, Item, 1.75; tin, hamper, Box, -; tea, tin, Item, 6',
               'asks': 'jam tin',
               'declare': 'safe',
               'expect': {'gtrNodes': '7',
                          'gtrLeaves': '4',
                          'gtrComposites': '3',
                          'gtrDepth': '2',
                          'gtrCalls': '7: 1 from the client + 6 forwarded by composites',
                          'gtrTotal': '15.5',
                          'gtrAskLeaves': '1: jam (refused by the compiler: add is declared only on composites)',
                          'gtrAskTaken': '1: tin'}},
              {'id': 'playlist',
               'label': 'A playlist in seconds, transparent declaration',
               'nodes': 'set, -, Playlist, -; side1, set, Playlist, -; intro, side1, Track, 95; song1, side1, Track, '
                        '212.5; side2, set, Playlist, -; song2, side2, Track, 180; outro, set, Track, 40',
               'asks': '',
               'declare': 'transparent',
               'expect': {'gtrNodes': '7',
                          'gtrLeaves': '4',
                          'gtrComposites': '3',
                          'gtrDepth': '2',
                          'gtrTotal': '527.5',
                          'gtrAskLeaves': '0: none',
                          'gtrAskTaken': '0: none'}}]},
 {'mode': 'tree',
  'view': 'traverse',
  'presets': [{'id': 'hamper',
               'label': 'The gift hamper, finding the scone',
               'nodes': 'hamper, -, Box, -; tray, hamper, Box, -; jam, hamper, Item, 4.5; bread, tray, Item, 3.25; '
                        'scone, tray, Item, 1.75; tin, hamper, Box, -; tea, tin, Item, 6',
               'find': 'scone',
               'expect': {'gtrNodes': '7',
                          'gtrPre': 'hamper, tray, bread, scone, jam, tin, tea',
                          'gtrPost': 'bread, scone, tray, jam, tea, tin, hamper',
                          'gtrLevel': 'hamper, tray, jam, tin, bread, scone, tea',
                          'gtrFind': 'pre-order 4, post-order 2, level-order 6 (of 7)'}},
              {'id': 'audio-guide',
               'label': 'A museum audio guide',
               'nodes': 'tour, -, Stop, -; hall1, tour, Stop, -; vase, hall1, Exhibit, 2; mask, hall1, Exhibit, 3; '
                        'hall2, tour, Stop, -; coin, hall2, Exhibit, 1; garden, tour, Exhibit, 4',
               'find': '-',
               'expect': {'gtrPre': 'tour, hall1, vase, mask, hall2, coin, garden',
                          'gtrPost': 'vase, mask, hall1, coin, hall2, garden, tour',
                          'gtrLevel': 'tour, hall1, hall2, garden, vase, mask, coin',
                          'gtrFind': 'no node to find'}}]},
 {'mode': 'tree',
  'view': 'visit',
  'presets': [{'id': 'hamper-kind',
               'label': 'The hamper, two visitors, a new kind',
               'nodes': 'hamper, -, Box, -; tray, hamper, Box, -; jam, hamper, Item, 4.5; bread, tray, Item, 3.25; '
                        'scone, tray, Item, 1.75; tin, hamper, Box, -; tea, tin, Item, 6',
               'visitors': 'price weigh',
               'adding': 'kind',
               'expect': {'gtrAccepts': '14: 7 nodes × 2 visitors',
                          'gtrVisits': '14',
                          'gtrElements': '1 + 2 = 3 (the abstract element; Box, Item)',
                          'gtrVisitorClasses': '1 + 2 = 3 (the abstract visitor; price, weigh)',
                          'gtrMethods': '2 × 2 + 2 = 6',
                          'gtrMethodsPlain': '2 × 2 = 4',
                          'gtrAddVisitor': '1 added (the new element class), 3 changed (the abstract visitor and 2 '
                                           'visitors)',
                          'gtrAddPlain': '1 added (the new element class), 0 changed'}},
              {'id': 'guide-operation',
               'label': 'The audio guide, a new operation',
               'nodes': 'tour, -, Stop, -; hall1, tour, Stop, -; vase, hall1, Exhibit, 2; mask, hall1, Exhibit, 3; '
                        'hall2, tour, Stop, -; coin, hall2, Exhibit, 1; garden, tour, Exhibit, 4',
               'visitors': 'narrate time',
               'adding': 'operation',
               'expect': {'gtrAccepts': '14: 7 nodes × 2 visitors',
                          'gtrElements': '1 + 2 = 3 (the abstract element; Stop, Exhibit)',
                          'gtrVisitorClasses': '1 + 2 = 3 (the abstract visitor; narrate, time)',
                          'gtrAddVisitor': '1 added (the new visitor), 0 changed',
                          'gtrAddPlain': '0 added, 3 changed (the abstract element and 2 element classes)'}}]},
 {'mode': 'expr',
  'view': 'interpret',
  'presets': [{'id': 'coffee-price',
               'label': "A coffee's price",
               'expr': 'base + shots * 0.6 - discount',
               'context': 'base, 3.2; shots, 2; discount, 0.5; tip, 1',
               'expect': {'gexValue': '39/10 = 3.9',
                          'gexNodes': '7',
                          'gexByClass': 'Number 1, Variable 3, Add 1, Subtract 1, Multiply 1',
                          'gexClasses': '5 of the 7',
                          'gexCalls': '7: 1 from the client + 6 from nodes to their operands',
                          'gexDepth': '3',
                          'gexVars': '3: base, shots, discount',
                          'gexUnused': '1: tip'}},
              {'id': 'box-office',
               'label': 'A box-office total with a discount',
               'expr': '(adults * 12 + children * 7.5) * (1 - discount)',
               'context': 'adults, 2; children, 3; discount, 0.1',
               'expect': {'gexValue': '837/20 = 41.85',
                          'gexNodes': '11',
                          'gexByClass': 'Number 3, Variable 3, Add 1, Subtract 1, Multiply 3',
                          'gexClasses': '5 of the 7',
                          'gexCalls': '11: 1 from the client + 10 from nodes to their operands',
                          'gexDepth': '3',
                          'gexVars': '3: adults, children, discount',
                          'gexUnused': '0: none'}},
              {'id': 'thermostat',
               'label': "A thermostat's steps to target",
               'expr': '(target - now) / step',
               'context': 'target, 21; now, 18.5; step, 0.5',
               'expect': {'gexValue': '5',
                          'gexNodes': '5',
                          'gexByClass': 'Variable 3, Subtract 1, Divide 1',
                          'gexClasses': '3 of the 7',
                          'gexDepth': '2',
                          'gexVars': '3: target, now, step'}}]}]


# ---------------------------------------------------------------------------
# Building a lab (both families) and the entry point
# ---------------------------------------------------------------------------

def _build_lab(cfg, *, kit, prefix, view, fields, tiles, fn, js, fixed, title, subtitle, intro, rules, extra_keys=(),
               check=None):
    """dddkit._build_lab with gofkit's first sentence (dddkit's own would be prepended otherwise)."""
    allowed = ea.COMMON_CFG | set(extra_keys) | {key for key, _s, _d in fields}
    stray = sorted(set(cfg) - allowed)
    if stray:
        raise ValueError("%s: cfg sets %s, which this view does not take (it takes %s)"
                         % (kit, ", ".join(stray), ", ".join(sorted(allowed))))
    table, menu, expect, chosen = dddkit._presets(cfg, kit, fields, tiles, check, fixed)
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
              + dddkit._WIRE_JS.replace("%P%", prefix).replace("%FN%", fn))
    script = dddkit._COMMENT_LINES.sub("", script)
    panel_intro = ea.plain(cfg, kit, "panel_intro", intro, limit=1200)
    if FAMILY_SENTENCE not in panel_intro:
        panel_intro = FAMILY_SENTENCE + " " + panel_intro
    title = ea.plain(cfg, kit, "title", title)
    return Lab(title=title, subtitle=subtitle,
               markup=ea.markup_html(prefix, title, subtitle, rules), controls=controls, script=script,
               panel_title=ea.plain(cfg, kit, "panel_title", "Change the inputs, or choose a worked example"),
               panel_intro=panel_intro, expect={prefix + "Preset": expect})


def family_intro():
    return (FAMILY_SENTENCE + " The lab counts one consequence of applying a pattern or not; whether the pattern "
            "fits is weighed in the book, against what in the design is expected to vary.")


def _no_options(cfg, kit, tiles):
    return {}, [], tiles


def mode_lab(cfg, mode, spec):
    """One gofkit mode as a Lab, from its spec dict (kit-contract.md section 2)."""
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
                      fn=spec["fn"], js=DDD_CORE_JS + GOF_CORE_JS + spec["js"] + v["js"], fixed=fixed,
                      title=spec["title"], subtitle=v["subtitle"], intro=family_intro(), rules=v["rules"],
                      extra_keys=keys, check=v["check"])


def gofkit_lab(cfg):
    """The Design Patterns kit: cfg["mode"] chooses the mode, cfg["view"] the view."""
    cfg = cfg or {}
    mode = cfg.get("mode")
    if mode in SPECS:
        return mode_lab(cfg, mode, SPECS[mode])
    family_b = gofkit_b.MODES
    if mode in family_b:
        return family_b[mode](cfg)
    raise ValueError("gofkit_lab: unknown mode %r; the modes are %s"
                     % (mode, ", ".join(MODES_A + tuple(m for m in family_b if m not in SPECS))))


# Family B. Imported last, after mode_lab exists, so that gofkit_b may import
# from this module at its top whichever module loads first.
from . import gofkit_b  # noqa: E402

__all__ = ["gofkit_lab", "mode_lab", "family_intro", "GOF_CORE_JS", "SPECS", "MODES_A", "KIT", "CAUTION",
           "vrec", "expr", "gex_parse", "gex_value", "SAMPLES"]
