"""dddkit_b -- family B of the Domain-Driven Design kit: dependencies, contexts, effort and money.

Specified in docs/domain-driven-design/PLAN.md section D (family B); the seam
with family A (dddkit.py: the entry point and modes lang, assoc, identity,
aggregate, spec) is docs/domain-driven-design/kit-contract.md; the report an
author configures a lesson from is the "Family B" section of
docs/domain-driven-design/kit-report.md. Four modes:

  modules  (dmo)  cohesion, change, layers    Chapters 3, 4, 5, 10, 15, 16
  context  (dcx)  map, protocol               Chapters 14, 16
  distill  (dds)  effort                      Chapters 15, 17
  ledger   (dle)  balance, post               Chapter 11

Each mode has one base block <PREFIX>_JS defining the pure function
<prefix>Compute(view, inst, opts), which scripts/mathcheck.js calls (section
"dddkit (Domain-Driven Design), family B"), and one block per view. A page
ships the base block and its own view's block only.

THE MODELS ARE THE LESSON'S. No element, context, part or account is a
constant here: every one arrives in a preset. Nothing typed is evaluated as
script. Nothing here scores a design: every tile is a count over the model the
lesson states, and every status line says so.

IDS. Every JS function and variable and every element id begins with its
mode's prefix (dmo, dcx, dds, dle). Grepped against scripts/mathpath/labs/*.py
and scripts/*.js on 2026-11-01: none is used by another kit.
"""

import re
from fractions import Fraction

from . import eakit_core as ea
from .dddkit import mode_lab, vrec

# ---------------------------------------------------------------------------
# modules (dmo): packaging, change and layering, Chapters 3-5, 10, 15, 16
# ---------------------------------------------------------------------------

DMO_JS = r"""
  var DMO_VIEW = {};
  function dmoCompute(view, inst, opts) { return eaRun(DMO_VIEW[view], inst, opts); }
  /* One or two packagings, read from the records' shape: a module2 column
     makes a second. Modules are listed alphabetically. */
  function dmoPackagings(elements, opts) {
    var keys = elements.length && elements[0].module2 !== undefined ? ['module', 'module2'] : ['module'];
    var names = (opts && opts.names) || ['first packaging', 'second packaging'];
    return keys.map(function (k, i) {
      var of = {}, mods = [];
      elements.forEach(function (e) { of[e.element] = e[k]; if (mods.indexOf(e[k]) < 0) mods.push(e[k]); });
      return { key: k, sfx: i ? '2' : '', name: names[i], of: of, mods: eaSort(mods) };
    });
  }
  function dmoUnknown(what, i, name) { eaRefuse(what + ', record ' + (i + 1) + ': ' + name + ' is not one of the elements'); }
  /* Every dependency joins two different elements, once. */
  function dmoDeps(deps, of) {
    var seen = {};
    deps.forEach(function (d, i) {
      if (of[d.from] === undefined) dmoUnknown('Dependencies', i, d.from);
      if (of[d.to] === undefined) dmoUnknown('Dependencies', i, d.to);
      if (d.from === d.to) eaRefuse('Dependencies, record ' + (i + 1) + ': ' + d.from + ' depends on itself');
      var k = d.from + ' ' + d.to;
      if (seen[k]) eaRefuse('Dependencies, record ' + (i + 1) + ': ' + d.from + ', ' + d.to + ' is given twice');
      seen[k] = true;
    });
  }
  function dmoPairCmp(a, b) { return a[0] < b[0] ? -1 : a[0] > b[0] ? 1 : (a[1] < b[1] ? -1 : a[1] > b[1] ? 1 : 0); }
"""

DMO_VIEW_JS = {}

DMO_VIEW_JS["cohesion"] = r"""
  /* Groups of two or more modules that reach each other along across-module
     dependencies (strongly connected components), each sorted, ordered by
     their first module. */
  function dmoCycles(mods, adj) {
    var reach = {};
    mods.forEach(function (m) {
      var seen = {}, stack = [m];
      while (stack.length) {
        var x = stack.pop();
        Object.keys(adj[x]).forEach(function (y) { if (!seen[y]) { seen[y] = true; stack.push(y); } });
      }
      reach[m] = seen;
    });
    var done = {}, groups = [];
    mods.forEach(function (m) {
      if (done[m]) return;
      var g = mods.filter(function (o) { return o === m || (reach[m][o] && reach[o][m]); });
      g.forEach(function (o) { done[o] = true; });
      if (g.length > 1) groups.push(g);
    });
    return groups;
  }
  DMO_VIEW.cohesion = function (inst, opts) {
    var pks = dmoPackagings(inst.elements, opts), deps = inst.deps, tiles = {}, notes = [], rows = [];
    dmoDeps(deps, pks[0].of);
    pks.forEach(function (pk) {
      var inside = 0, across = 0, adj = {}, per = {}, pairs = {}, list = [];
      pk.mods.forEach(function (m) { adj[m] = {}; per[m] = { els: 0, inside: 0, out: 0, inn: 0 }; });
      inst.elements.forEach(function (e) { per[pk.of[e.element]].els += 1; });
      deps.forEach(function (d) {
        var a = pk.of[d.from], b = pk.of[d.to];
        if (a === b) { inside += 1; per[a].inside += 1; return; }
        across += 1; per[a].out += 1; per[b].inn += 1; adj[a][b] = true;
        var p = eaSort([a, b]), k = p.join(' ');
        if (!pairs[k]) { pairs[k] = { p: p, n: 0 }; list.push(pairs[k]); }
        pairs[k].n += 1;
      });
      list.sort(function (x, y) { return dmoPairCmp(x.p, y.p); });
      var best = null;
      list.forEach(function (x) { if (best === null || x.n > best.n) best = x; });
      var tied = best ? list.filter(function (x) { return x.n === best.n; }) : [];
      var groups = dmoCycles(pk.mods, adj);
      tiles['dmoModules' + pk.sfx] = eaInt(pk.mods.length);
      tiles['dmoInside' + pk.sfx] = eaInt(inside);
      tiles['dmoAcross' + pk.sfx] = eaInt(across);
      tiles['dmoShare' + pk.sfx] = eaPct(R(BigInt(inside), BigInt(deps.length)));
      tiles['dmoCycles' + pk.sfx] = groups.length + ': ' + (groups.length ? groups.map(function (g) { return '(' + g.join(', ') + ')'; }).join(', ') : 'none');
      tiles['dmoPair' + pk.sfx] = best ? best.p[0] + ' and ' + best.p[1] + ': ' + eaInt(best.n) : 'none';
      notes.push((pks.length > 1 ? pk.name + ': ' : '') + eaInt(inside) + ' of ' + eaPlural(deps.length, 'dependency', 'dependencies')
        + (inside === 1 ? ' stays' : ' stay') + ' inside a module and ' + eaInt(across) + (across === 1 ? ' crosses' : ' cross')
        + ' between ' + eaPlural(pk.mods.length, 'module', 'modules') + '.'
        + (tied.length > 1 ? ' The most coupled pairs, ' + eaInt(best.n) + ' each, are ' + tied.map(function (x) { return x.p.join(' and '); }).join('; ')
          + '; the tile shows the alphabetically first.' : ''));
      pk.mods.forEach(function (m) {
        var r = [m, eaInt(per[m].els), eaInt(per[m].inside), eaInt(per[m].out), eaInt(per[m].inn)];
        if (pks.length > 1) r.unshift(pk.name);
        rows.push(r);
      });
    });
    var head = ['module', 'elements', 'inside', 'out to others', 'in from others'];
    if (pks.length > 1) head.unshift('packaging');
    return { tiles: tiles, status: dddStatus(notes.join(' ')),
      table: { caption: 'Each module: its elements and the dependencies inside it, out of it and into it', head: head, rows: rows } };
  };
"""

DMO_VIEW_JS["change"] = r"""
  DMO_VIEW.change = function (inst, opts) {
    var pks = dmoPackagings(inst.elements, opts), order = [], els = {}, seen = {}, tiles = {}, notes = [];
    inst.changes.forEach(function (c, i) {
      if (pks[0].of[c.element] === undefined) dmoUnknown('Changes', i, c.element);
      var k = c.change + ' ' + c.element;
      if (seen[k]) eaRefuse('Changes, record ' + (i + 1) + ': ' + c.change + ' already touches ' + c.element);
      seen[k] = true;
      if (!els[c.change]) { els[c.change] = []; order.push(c.change); }
      els[c.change].push(c.element);
    });
    tiles.dmoChanges = eaInt(order.length);
    var touched = pks.map(function (pk) {
      var t = {}, total = 0, confined = [], best = null;
      order.forEach(function (c) {
        var ms = [];
        els[c].forEach(function (e) { if (ms.indexOf(pk.of[e]) < 0) ms.push(pk.of[e]); });
        t[c] = eaSort(ms);
        total += ms.length;
        if (ms.length === 1) confined.push(c);
        if (best === null || ms.length > t[best].length) best = c;
      });
      var tied = order.filter(function (c) { return t[c].length === t[best].length; });
      tiles['dmoPer' + pk.sfx] = order.map(function (c) { return c + ' ' + t[c].length; }).join(', ');
      tiles['dmoTotal' + pk.sfx] = eaInt(total);
      tiles['dmoConfined' + pk.sfx] = confined.length + ' of ' + order.length + (confined.length ? ': ' + confined.join(', ') : '');
      tiles['dmoLargest' + pk.sfx] = best + ', ' + eaPlural(t[best].length, 'module', 'modules');
      notes.push((pks.length > 1 ? pk.name + ': the ' : 'The ') + eaPlural(order.length, 'change touches', 'changes touch') + ' '
        + eaPlural(total, 'module', 'modules') + ' in all, counting a module once per change.'
        + (tied.length > 1 ? ' ' + tied.join(', ') + ' tie for the largest, at ' + eaPlural(t[best].length, 'module', 'modules')
          + '; the tile shows the first given.' : ''));
      return t;
    });
    var head = ['change', 'elements'].concat(pks.map(function (pk) { return pks.length > 1 ? 'modules, ' + pk.name : 'modules'; }));
    var rows = order.map(function (c) {
      return [c, els[c].join(', ')].concat(touched.map(function (t) { return t[c].length + ': ' + t[c].join(', '); }));
    });
    return { tiles: tiles, status: dddStatus(notes.join(' ')),
      table: { caption: 'Each change, the elements it touches and the modules they sit in', head: head, rows: rows } };
  };
"""

DMO_VIEW_JS["layers"] = r"""
  DMO_VIEW.layers = function (inst) {
    var L = inst.layers, at = {}, of = {}, used = {}, down = 0, within = 0, skip = 0, up = [], rows = [];
    L.forEach(function (l, i) { at[l] = i; });
    inst.elements.forEach(function (e, i) {
      if (at[e.layer] === undefined) eaRefuse('Elements, record ' + (i + 1) + ': ' + e.layer + ' is not one of the layers');
      of[e.element] = e.layer; used[e.layer] = true;
    });
    dmoDeps(inst.deps, of);
    inst.deps.forEach(function (d) {
      var a = of[d.from], b = of[d.to], gap = at[b] - at[a], what;
      if (gap === 0) { within += 1; what = 'within ' + a; }
      else if (gap > 0) {
        down += 1;
        if (gap > 1) { skip += 1; what = 'down, skipping ' + eaPlural(gap - 1, 'layer', 'layers'); } else what = 'down';
      } else { up.push(d.from + ' → ' + d.to); what = 'UP, ' + eaPlural(-gap, 'layer', 'layers') + ' (a violation)'; }
      rows.push([d.from + ' (' + a + ')', d.to + ' (' + b + ')', what]);
    });
    var empty = L.filter(function (l) { return !used[l]; });
    return {
      tiles: { dmoDeps: eaInt(inst.deps.length), dmoDown: eaInt(down), dmoWithin: eaInt(within), dmoUp: eaCount(up),
        dmoSkip: eaInt(skip), dmoEmpty: eaCount(empty) },
      status: dddStatus('Of ' + eaPlural(inst.deps.length, 'dependency', 'dependencies') + ' across ' + eaPlural(L.length, 'layer', 'layers')
        + ', ' + eaInt(down) + (down === 1 ? ' runs' : ' run') + ' down (' + eaInt(skip) + ' of them skipping a layer), ' + eaInt(within)
        + (within === 1 ? ' stays' : ' stay') + ' within a layer and ' + eaInt(up.length) + (up.length === 1 ? ' runs' : ' run') + ' up.'),
      table: { caption: 'Each dependency, from the layer it starts in to the layer it reaches', head: ['from', 'to', 'direction'], rows: rows }
    };
  };
"""

# ---------------------------------------------------------------------------
# context (dcx): the context map and integration protocols, Chapters 14, 16
# ---------------------------------------------------------------------------

DCX_JS = r"""
  var DCX_VIEW = {};
  function dcxCompute(view, inst, opts) { return eaRun(DCX_VIEW[view], inst, opts); }
"""

DCX_VIEW_JS = {}

DCX_VIEW_JS["map"] = r"""
  var DCX_KIND = { 'shared-kernel': 'shared kernel', 'customer-supplier': 'customer/supplier', conformist: 'conformist',
    acl: 'anticorruption layer', ohs: 'open host service', 'published-language': 'published language', 'separate-ways': 'separate ways' };
  DCX_VIEW.map = function (inst) {
    var C = inst.contexts, rels = inst.rels, ch = inst.changed, pair = {}, i;
    if (C.indexOf(ch) < 0) eaRefuse('The changed context, ' + ch + ', is not one of the contexts');
    rels.forEach(function (r, i) {
      [r.upstream, r.downstream].forEach(function (c) {
        if (C.indexOf(c) < 0) eaRefuse('Relationships, record ' + (i + 1) + ': ' + c + ' is not one of the contexts');
      });
      if (r.upstream === r.downstream) eaRefuse('Relationships, record ' + (i + 1) + ': ' + r.upstream + ' is related to itself');
      var k = eaSort([r.upstream, r.downstream]).join(' ');
      if (pair[k]) eaRefuse('Relationships, record ' + (i + 1) + ': ' + r.upstream + ' and ' + r.downstream + ' already have a relationship (record ' + pair[k] + ')');
      pair[k] = i + 1;
    });
    /* Models that change: from the changed one, across a shared kernel either
       way and down a conformist or customer/supplier edge, and on from every
       model so changed. A translator stops it. */
    var changed = {}, queue = [ch];
    changed[ch] = true;
    while (queue.length) {
      var x = queue.shift();
      rels.forEach(function (r) {
        var other = null;
        if (r.kind === 'shared-kernel') other = r.upstream === x ? r.downstream : (r.downstream === x ? r.upstream : null);
        else if ((r.kind === 'conformist' || r.kind === 'customer-supplier') && r.upstream === x) other = r.downstream;
        if (other !== null && !changed[other]) { changed[other] = true; queue.push(other); }
      });
    }
    var trans = [], tseen = {}, aclOwner = {}, rows = [];
    rels.forEach(function (r) {
      var up = r.upstream, dn = r.downstream, k = r.kind, eff;
      if (k === 'separate-ways') eff = 'no integration: nothing to change';
      else if (k === 'shared-kernel') eff = (changed[up] ? 'both models change (the kernel is shared)' : 'not reached');
      else if (!changed[up]) eff = changed[dn] ? 'not reached: a change does not travel upstream' : 'not reached';
      else if (k === 'conformist' || k === 'customer-supplier') eff = dn + '’s model changes';
      else if (k === 'acl') {
        eff = dn + '’s anticorruption layer is updated; ' + dn + '’s model ' + (changed[dn] ? 'changes by another route' : 'is unchanged');
        trans.push(dn + '’s ACL from ' + up); aclOwner[dn] = true;
      } else {
        eff = up + '’s protocol is updated; ' + dn + (changed[dn] ? '’s model changes by another route' : ' is unchanged');
        if (!tseen[up]) { tseen[up] = true; trans.push(up + '’s protocol'); }
      }
      rows.push([up, dn, DCX_KIND[k], eff]);
    });
    var models = C.filter(function (c) { return c !== ch && changed[c]; });
    var reached = C.filter(function (c) { return c !== ch && (changed[c] || aclOwner[c]); });
    var untouched = C.filter(function (c) { return c !== ch && reached.indexOf(c) < 0; });
    return {
      tiles: { dcxRels: eaInt(rels.length), dcxModels: eaCount(models), dcxTranslators: eaCount(trans),
        dcxReached: eaCount(reached), dcxUntouched: eaCount(untouched) },
      status: dddStatus('A change to ' + ch + '’s model changes ' + eaPlural(models.length, 'other model', 'other models') + ' and '
        + eaPlural(trans.length, 'translator', 'translators') + '; ' + eaPlural(untouched.length, 'context is', 'contexts are')
        + ' untouched.'),
      table: { caption: 'Each relationship and what the change to ' + ch + ' does there', head: ['upstream', 'downstream', 'kind', 'the change'], rows: rows }
    };
  };
"""

DCX_VIEW_JS["protocol"] = r"""
  DCX_VIEW.protocol = function (inst, opts) {
    var c = inst.contexts, n, dir = opts.directed === 'yes';
    if (c.length === 1 && /^\d+$/.test(c[0])) {
      n = BigInt(c[0]);
      if (n < 2n || n > 60n) eaRefuse('The number of contexts is a whole number from 2 to 60, and it is ' + eaInt(n));
    } else if (c.length < 2) {
      eaRefuse('Contexts: give at least two names, or one whole number from 2 to 60');
    } else n = BigInt(c.length);
    var pb = dir ? n * (n - 1n) : n * (n - 1n) / 2n, pc = dir ? 2n * (n - 1n) : n - 1n, qb = dir ? 2n * n : n, qc = dir ? 2n : 1n;
    var pw = inst.scheme === 'pairwise', unit = dir ? 'one-way translators' : 'two-way translators';
    return {
      tiles: { dcxN: eaInt(n), dcxBuild: eaInt(pw ? pb : qb), dcxChange: eaInt(pw ? pc : qc),
        dcxOther: (pw ? 'published: ' + eaInt(qb) + ' to build, ' + eaInt(qc) : 'pairwise: ' + eaInt(pb) + ' to build, ' + eaInt(pc)) + ' to change',
        dcxBuildRatio: eaTimes(R(pb, qb)), dcxChangeRatio: eaTimes(R(pc, qc)) },
      status: dddStatus(eaInt(n) + ' contexts, counted in ' + unit + ': pairwise integration builds ' + eaInt(pb) + ' and a published language '
        + eaInt(qb) + '; when one model changes, ' + eaInt(pc) + ' and ' + eaInt(qc) + ' of them change.'),
      table: { caption: 'Both schemes for ' + eaInt(n) + ' contexts (' + unit + ')', head: ['scheme', 'to build', 'to change when one model changes'],
        rows: [['pairwise', eaInt(pb), eaInt(pc)], ['published language', eaInt(qb), eaInt(qc)]] }
    };
  };
"""

# ---------------------------------------------------------------------------
# distill (dds): effort on the core and the generic subdomains, Chapter 15
# ---------------------------------------------------------------------------

DDS_JS = r"""
  var DDS_VIEW = {};
  function ddsCompute(view, inst, opts) { return eaRun(DDS_VIEW[view], inst, opts); }
"""

DDS_VIEW_JS = {}

DDS_VIEW_JS["effort"] = r"""
  /* The optional last cell: build, buy, published or outsource; none is build. */
  function ddsOption(p) { return p.rest && p.rest.length ? p.rest[0] : 'build'; }
  DDS_VIEW.effort = function (inst) {
    var weeks = { core: 0n, supporting: 0n, generic: 0n }, total = 0n, strong = 0n, strongCore = 0n, built = [], free = 0n, unbuilt = 0n, rows = [];
    inst.parts.forEach(function (p, i) {
      var opt = ddsOption(p), w = p.weeks.n, s = p.strong.n;
      if (opt !== 'build' && p.kind !== 'generic') eaRefuse('Parts, record ' + (i + 1) + ': ' + p.part + ' is ' + p.kind + ', and only a generic part can be bought, published or outsourced');
      if (opt !== 'build' && s > 0n) eaRefuse('Parts, record ' + (i + 1) + ': ' + p.part + ' is not built in house, so none of the team’s strongest developers work on it');
      if (opt === 'build') {
        weeks[p.kind] += w; total += w; strong += s;
        if (p.kind === 'core') strongCore += s;
        if (p.kind === 'generic') { built.push(p.part); free += w; }
      } else unbuilt += w;
      rows.push([p.part, p.kind, opt, opt === 'build' ? eaInt(w) : '0 (' + eaInt(w) + ' not counted)', eaInt(s)]);
    });
    if (total === 0n) eaRefuse('No part is built in house with any weeks, so there is no effort to share');
    rows.forEach(function (r, i) { r.splice(4, 0, ddsOption(inst.parts[i]) === 'build' ? eaPct(R(inst.parts[i].weeks.n, total)) : '—'); });
    var share = function (k) { return eaPct(R(weeks[k], total)); };
    return {
      tiles: { ddsWeeks: eaInt(total), ddsCore: share('core'), ddsSupporting: share('supporting'), ddsGeneric: share('generic'),
        ddsStrong: eaInt(strongCore) + ' of ' + eaInt(strong) + (strong > 0n ? ', ' + eaPct(R(strongCore, strong)) : ''),
        ddsBuilt: eaCount(built), ddsFree: eaInt(free) },
      status: dddStatus(eaPlural(total, 'developer-week', 'developer-weeks') + ' are built in house, ' + eaInt(weeks.core) + ' of them on the core'
        + (unbuilt > 0n ? '; ' + eaInt(unbuilt) + ' more are bought, published or outsourced and not counted' : '') + '.'),
      table: { caption: 'Each part: its kind, how it is obtained, the weeks counted and their share, and the strongest developers on it',
        head: ['part', 'kind', 'option', 'weeks counted', 'share', 'strongest'], rows: rows }
    };
  };
"""

# ---------------------------------------------------------------------------
# ledger (dle): accounts, entries and posting rules, Chapter 11 (Fowler)
# ---------------------------------------------------------------------------

DLE_JS = r"""
  var DLE_VIEW = {};
  function dleCompute(view, inst, opts) { return eaRun(DLE_VIEW[view], inst, opts); }
  /* Money to the cent: 1,234.50, −0.75 (U+2212). */
  function dleMoney(r) { return eaFixed(r, 2); }
  function dleSigned(r) { return (r.n > 0n ? '+' : '') + eaFixed(r, 2); }
  /* An exact terminating decimal, at least 2 places and as many as it needs. */
  function dleExact(r) { for (var p = 2; p <= 12; p += 1) if (eaExactAt(r, p)) return (r.n > 0n ? '+' : '') + eaFixed(r, p); return eaNum(r); }
  function dleCents(entries) {
    entries.forEach(function (e, i) {
      if (!Rint(Rmul(e.amount, R(100n)))) eaRefuse('Entries, record ' + (i + 1) + ': ' + dleExact(e.amount).replace(/^\+/, '') + ' is not a whole number of cents; give at most 2 decimal places');
    });
  }
  /* Balances by account, in order of first appearance. */
  function dleBalances(list) {
    var bal = {}, order = [];
    list.forEach(function (e) {
      if (bal[e.account] === undefined) { bal[e.account] = R0; order.push(e.account); }
      bal[e.account] = Radd(bal[e.account], e.amount);
    });
    return { bal: bal, order: order, text: order.map(function (a) { return a + ' ' + dleMoney(bal[a]); }).join(', ') };
  }
"""

DLE_VIEW_JS = {}

DLE_VIEW_JS["balance"] = r"""
  DLE_VIEW.balance = function (inst) {
    var E = inst.entries;
    dleCents(E);
    var b = dleBalances(E), net = {}, txns = [], total = R0, n = {};
    E.forEach(function (e) {
      if (net[e.txn] === undefined) { net[e.txn] = R0; txns.push(e.txn); n[e.txn] = 0; }
      net[e.txn] = Radd(net[e.txn], e.amount); n[e.txn] += 1;
      total = Radd(total, e.amount);
    });
    var bad = txns.filter(function (t) { return !Requ(net[t], R0); });
    return {
      tiles: { dleAccounts: eaInt(b.order.length), dleBalances: b.text, dleTxns: eaInt(txns.length),
        dleUnbalanced: bad.length + ': ' + (bad.length ? bad.map(function (t) { return t + ' ' + dleSigned(net[t]); }).join(', ') : 'none'),
        dleTotal: dleMoney(total) },
      status: dddStatus(eaPlural(E.length, 'entry', 'entries') + ' in ' + eaPlural(txns.length, 'transaction', 'transactions') + ' post to '
        + eaPlural(b.order.length, 'account', 'accounts') + '; ' + eaPlural(bad.length, 'transaction does', 'transactions do') + ' not balance.'),
      table: { caption: 'Each transaction: its entries and its net', head: ['transaction', 'entries', 'net', 'balances'],
        rows: txns.map(function (t) { return [t, eaInt(n[t]), dleMoney(net[t]), Requ(net[t], R0) ? 'yes' : 'no']; }) }
    };
  };
"""

DLE_VIEW_JS["post"] = r"""
  var DLE_SHOW = 12;
  DLE_VIEW.post = function (inst) {
    var E = inst.entries, rules = inst.rules, journal = [], fired = [], used = [], left = R0, rows = [];
    dleCents(E);
    rules.forEach(function (r, i) {
      if (r.from === r.to) eaRefuse('Rules, record ' + (i + 1) + ': ' + r.rule + ' posts from ' + r.from + ' back to itself');
    });
    /* Each given entry, then what each rule on its account derives from it,
       rules in the order given. A derived entry fires nothing. */
    E.forEach(function (e) {
      journal.push(e);
      rules.forEach(function (r) {
        if (r.from !== e.account) return;
        var exact = Rmul(r.share, e.amount), a = Rabs(exact);
        var cents = eaFloor(Radd(Rmul(a, R(100n)), R(1n, 2n))), got = R(exact.n < 0n ? -cents : cents, 100n);
        left = Radd(left, Rsub(exact, got));
        journal.push({ txn: e.txn, account: r.to, amount: got });
        journal.push({ txn: e.txn, account: r.from, amount: Rneg(got) });
        if (used.indexOf(r.rule) < 0) used.push(r.rule);
        fired.push(r.rule + ' on ' + e.txn + ': ' + dleMoney(got) + ' to ' + r.to);
        rows.push([e.txn, r.rule, e.account + ' ' + dleMoney(e.amount), eaNum(r.share), dleExact(exact).replace(/^\+/, ''), r.to + ' ' + dleSigned(got) + ', ' + r.from + ' ' + dleSigned(Rneg(got))]);
      });
    });
    var b = dleBalances(journal), shown = fired.slice(0, DLE_SHOW);
    return {
      tiles: { dleGiven: eaInt(E.length), dleDerived: eaInt(2 * fired.length), dleBalances: b.text,
        dleList: fired.length ? shown.join('; ') + (fired.length > DLE_SHOW ? '; and ' + (fired.length - DLE_SHOW) + ' more (the table lists all)' : '') : 'none',
        dleLeft: Requ(left, R0) ? '0' : dleExact(left) },
      status: dddStatus(eaInt(used.length) + ' of ' + eaPlural(rules.length, 'rule', 'rules') + (used.length === 1 ? ' fires, ' : ' fire, ')
        + eaPlural(fired.length, 'time', 'times') + ' in all, on '
        + eaPlural(E.length, 'given entry', 'given entries') + ', deriving '
        + eaPlural(2 * fired.length, 'entry', 'entries') + '; derived entries fire nothing. Rounding to the cent leaves ' + (Requ(left, R0) ? '0' : dleExact(left)) + ' in all.'),
      table: { caption: 'Each firing: the entry, the rule, the exact share and the two entries it derives',
        head: ['transaction', 'rule', 'entry', 'share', 'exact', 'derived'], rows: rows }
    };
  };
"""

# ---------------------------------------------------------------------------
# Python: the checks (each mirrors a JS refusal beyond the field parser)
# ---------------------------------------------------------------------------


def _deps(deps, of):
    seen = set()
    for i, d in enumerate(deps):
        for end in (d["from"], d["to"]):
            if end not in of:
                raise ValueError("Dependencies, record %d: %s is not one of the elements" % (i + 1, end))
        if d["from"] == d["to"]:
            raise ValueError("Dependencies, record %d: %s depends on itself" % (i + 1, d["from"]))
        k = (d["from"], d["to"])
        if k in seen:
            raise ValueError("Dependencies, record %d: %s, %s is given twice" % (i + 1, d["from"], d["to"]))
        seen.add(k)


def _check_cohesion(inst, fixed):
    _deps(inst["deps"], {e["element"] for e in inst["elements"]})


def _check_change(inst, fixed):
    of, seen = {e["element"] for e in inst["elements"]}, set()
    for i, c in enumerate(inst["changes"]):
        if c["element"] not in of:
            raise ValueError("Changes, record %d: %s is not one of the elements" % (i + 1, c["element"]))
        k = (c["change"], c["element"])
        if k in seen:
            raise ValueError("Changes, record %d: %s already touches %s" % (i + 1, c["change"], c["element"]))
        seen.add(k)


def _check_layers(inst, fixed):
    layers = set(inst["layers"])
    for i, e in enumerate(inst["elements"]):
        if e["layer"] not in layers:
            raise ValueError("Elements, record %d: %s is not one of the layers" % (i + 1, e["layer"]))
    _deps(inst["deps"], {e["element"] for e in inst["elements"]})


def _check_map(inst, fixed):
    ctx = inst["contexts"]
    if inst["changed"] not in ctx:
        raise ValueError("The changed context, %s, is not one of the contexts" % inst["changed"])
    pair = {}
    for i, r in enumerate(inst["rels"]):
        for c in (r["upstream"], r["downstream"]):
            if c not in ctx:
                raise ValueError("Relationships, record %d: %s is not one of the contexts" % (i + 1, c))
        if r["upstream"] == r["downstream"]:
            raise ValueError("Relationships, record %d: %s is related to itself" % (i + 1, r["upstream"]))
        k = tuple(sorted((r["upstream"], r["downstream"])))
        if k in pair:
            raise ValueError("Relationships, record %d: %s and %s already have a relationship (record %d)"
                             % (i + 1, r["upstream"], r["downstream"], pair[k]))
        pair[k] = i + 1


def _check_protocol(inst, fixed):
    c = inst["contexts"]
    if len(c) == 1 and re.fullmatch(r"\d+", c[0]):
        if not 2 <= int(c[0]) <= 60:
            raise ValueError("The number of contexts is a whole number from 2 to 60, and it is %s" % ea.grp(int(c[0])))
    elif len(c) < 2:
        raise ValueError("Contexts: give at least two names, or one whole number from 2 to 60")


def _check_effort(inst, fixed):
    total = 0
    for i, p in enumerate(inst["parts"]):
        opt = p["rest"][0] if p.get("rest") else "build"
        if opt != "build" and p["kind"] != "generic":
            raise ValueError("Parts, record %d: %s is %s, and only a generic part can be bought, published or outsourced"
                             % (i + 1, p["part"], p["kind"]))
        if opt != "build" and p["strong"] > 0:
            raise ValueError("Parts, record %d: %s is not built in house, so none of the team’s strongest "
                             "developers work on it" % (i + 1, p["part"]))
        if opt == "build":
            total += p["weeks"]
    if total == 0:
        raise ValueError("No part is built in house with any weeks, so there is no effort to share")


def _money_text(f):
    """dleExact without its plus sign: an exact decimal, at least 2 places (12.505, \u22120.001)."""
    f = Fraction(f)
    p = 2
    while (f * 10 ** p).denominator != 1:
        p += 1
    q = abs(f.numerator) * 10 ** p // f.denominator
    whole, frac = divmod(q, 10 ** p)
    return "%s%s.%0*d" % ("\u2212" if f < 0 else "", "{:,}".format(whole), p, frac)


def _cents(entries):
    for i, e in enumerate(entries):
        if (e["amount"] * 100).denominator != 1:
            raise ValueError("Entries, record %d: %s is not a whole number of cents; give at most 2 decimal places"
                             % (i + 1, _money_text(e["amount"])))


def _check_balance(inst, fixed):
    _cents(inst["entries"])


def _check_post(inst, fixed):
    _cents(inst["entries"])
    for i, r in enumerate(inst["rules"]):
        if r["from"] == r["to"]:
            raise ValueError("Rules, record %d: %s posts from %s back to itself" % (i + 1, r["rule"], r["from"]))


# ---------------------------------------------------------------------------
# Python: the spec dicts (kit-contract.md section 2)
# ---------------------------------------------------------------------------

_N = ea.NAME


def _names(what, lo, hi, things):
    return dict(what=what, control="text", kind="list", lo=lo, hi=hi, things=things, each=dict(_N))


def _elements(two):
    if two:
        return ea.rec("Elements (element, its module in the first packaging, in the second)",
                      [("element", _N), ("module", _N), ("module2", _N)], unique=True, rows=4)
    return ea.rec("Elements (element, module)", [("element", _N), ("module", _N)], unique=True, rows=4)


_DEPS = ("deps", ea.rec("Dependencies (from, to: from depends on to)", [("from", _N), ("to", _N)], rows=3), None)

_MOD_COHESION_TILES = [("Modules", "dmoModules"), ("Dependencies inside a module", "dmoInside"),
                       ("Dependencies across modules", "dmoAcross"), ("Share inside", "dmoShare"),
                       ("Module cycles", "dmoCycles"), ("Most coupled pair", "dmoPair")]
_MOD_CHANGE_TILES = [("Modules touched per change", "dmoPer"), ("Total module touches", "dmoTotal"),
                     ("Changes confined to one module", "dmoConfined"), ("The largest change", "dmoLargest")]

_PACKAGING_RULE = ("Each element sits in one module of each packaging; with a third column (module2) the view counts "
                   "a second packaging of the same elements and prints its tiles second. ")


def _packaging_options(first):
    """cfg packagings (1 or 2) and names (two short labels for the packagings)."""
    def options(cfg, kit, tiles):
        n = cfg.get("packagings", 1)
        if n not in (1, 2):
            raise ValueError("%s: cfg['packagings'] is 1 or 2, not %r" % (kit, n))
        names = cfg.get("names", ["first packaging", "second packaging"])
        if (not isinstance(names, (list, tuple)) or len(names) != 2
                or any(not isinstance(x, str) or not x.strip() or re.search(r"[<>&]", x) or len(x) > 30 for x in names)
                or names[0] == names[1]):
            raise ValueError("%s: cfg['names'] is two different plain names of at most 30 characters, not %r" % (kit, names))
        if "names" in cfg and n != 2:
            raise ValueError("%s: cfg['names'] names two packagings; set packagings to 2" % kit)
        names = [x.strip() for x in names]
        if n == 1:
            return {}, ["packagings", "names"], list(first) + list(tiles)
        out = list(first)
        for label, cid in tiles:
            out.append(("%s, %s" % (label, names[0]), cid))
        for label, cid in tiles:
            out.append(("%s, %s" % (label, names[1]), cid + "2"))
        return {"names": names}, ["packagings", "names"], out
    return options


def _directed(cfg, kit, tiles):
    d = cfg.get("directed", "no")
    if d not in ("yes", "no"):
        raise ValueError("%s: cfg['directed'] is \"yes\" or \"no\", not %r" % (kit, d))
    return {"directed": d}, ["directed"], tiles


MODULES = {
    "prefix": "dmo", "fn": "dmoCompute", "title": "Modules and dependencies", "js": DMO_JS,
    "views": {
        "cohesion": {
            "fields": [("elements", _elements(False), None), _DEPS],
            "tiles": _MOD_COHESION_TILES, "check": _check_cohesion, "options": _packaging_options([]),
            "subtitle": "dependencies inside and across modules",
            "rules": _PACKAGING_RULE + "A dependency is inside when both of its elements sit in the same module and "
                     "across otherwise; the share inside is the inside dependencies over all of them, exact. A module "
                     "cycle is a group of two or more modules each of which reaches every other along across-module "
                     "dependencies (a strongly connected component); each group lists its modules alphabetically, and "
                     "groups go in the order of their first module. The most coupled pair is the pair of modules with "
                     "the most dependencies between them in either direction; a tie goes to the alphabetically first "
                     "pair and the status line names the others. An element may depend on another once; a dependency "
                     "on itself is refused.",
            "js": DMO_VIEW_JS["cohesion"],
        },
        "change": {
            "fields": [("elements", _elements(False), None),
                       ("changes", ea.rec("Changes (change, an element it touches; one record per element)",
                                          [("change", _N), ("element", _N)], rows=4), None)],
            "tiles": _MOD_CHANGE_TILES, "check": _check_change,
            "options": _packaging_options([("Changes", "dmoChanges")]),
            "subtitle": "the modules each change reaches",
            "rules": _PACKAGING_RULE + "A change touches every element it lists, and through them every module those "
                     "elements sit in, each module counted once per change however many of its elements the change "
                     "touches. The total adds those counts over the changes. Changes are listed in the order first "
                     "given; the largest is the change touching the most modules, a tie going to the first given (the "
                     "status line names the others).",
            "js": DMO_VIEW_JS["change"],
        },
        "layers": {
            "fields": [("layers", _names("Layers, top to bottom", 2, 12, "layers"), None),
                       ("elements", ea.rec("Elements (element, layer)", [("element", _N), ("layer", _N)], unique=True,
                                           rows=4), None),
                       _DEPS],
            "tiles": [("Dependencies", "dmoDeps"), ("Downward", "dmoDown"), ("Within a layer", "dmoWithin"),
                      ("Upward (violations)", "dmoUp"), ("Downward, skipping a layer", "dmoSkip"),
                      ("Layers with no element", "dmoEmpty")],
            "check": _check_layers,
            "subtitle": "which dependencies run down the layers and which run up",
            "rules": "The layers are listed top to bottom. A dependency from an element in a higher layer to one in a "
                     "lower layer runs downward, one between two elements of the same layer is within it, and one "
                     "from a lower layer to a higher runs upward, which a strict layering forbids; upward ones are "
                     "listed in the order given. Downward counts every downward dependency, and of those, skipping a "
                     "layer counts the ones that pass over at least one layer between (allowed in a relaxed layering, "
                     "counted separately, not as violations). So downward + within + upward = all.",
            "js": DMO_VIEW_JS["layers"],
        },
    },
}

_KINDS = ea.word("shared-kernel", "customer-supplier", "conformist", "acl", "ohs", "published-language",
                 "separate-ways")

CONTEXT = {
    "prefix": "dcx", "fn": "dcxCompute", "title": "Context map", "js": DCX_JS,
    "views": {
        "map": {
            "fields": [("contexts", _names("Bounded contexts", 2, 30, "contexts"), None),
                       ("rels", ea.rec("Relationships (upstream, downstream, kind)",
                                       [("upstream", _N), ("downstream", _N), ("kind", _KINDS)], rows=4), None),
                       ("changed", ea.field("The context whose model changes", _N), None)],
            "tiles": [("Relationships", "dcxRels"), ("Other models that must change", "dcxModels"),
                      ("Translators to update", "dcxTranslators"), ("Contexts reached", "dcxReached"),
                      ("Contexts untouched", "dcxUntouched")],
            "check": _check_map, "subtitle": "how far one model change reaches across the map",
            "rules": "Kinds: shared-kernel, customer-supplier, conformist, acl (anticorruption layer), ohs (open host "
                     "service), published-language, separate-ways; two contexts have at most one relationship. A "
                     "model change crosses a shared kernel in both directions and goes down a conformist or a "
                     "customer-supplier relationship to the downstream model, and it travels on only from a model "
                     "that changed. It never travels upstream. An acl stops it at the downstream context's "
                     "translator, and an ohs or published-language relationship at the upstream's protocol: each is "
                     "a translator to update, the downstream model unchanged (it changes only if another route "
                     "reaches it). The ohs and published-language relationships of one upstream share its one "
                     "protocol, counted once; each acl is its own translator. Separate-ways has no effect. Contexts "
                     "reached are the other models that change and the contexts whose acl is updated; lists go in "
                     "the order the contexts are given, translators in the order of the relationships.",
            "js": DCX_VIEW_JS["map"],
        },
        "protocol": {
            "fields": [("contexts", _names("Contexts: their names, or how many (2 to 60)", 1, 60, "contexts"), None),
                       ("scheme", ea.choice("Scheme", "pairwise", "published"), "pairwise")],
            "tiles": [("Contexts n", "dcxN"), ("Translators to build", "dcxBuild"),
                      ("Translators to change when one model changes", "dcxChange"), ("The other scheme", "dcxOther"),
                      ("Pairwise ÷ published, to build", "dcxBuildRatio"),
                      ("Pairwise ÷ published, to change", "dcxChangeRatio")],
            "check": _check_protocol, "options": _directed,
            "subtitle": "translators for point-to-point integration and for one published language",
            "rules": "Pairwise, every pair of contexts has its own translation: n(n − 1)/2 two-way translators, of "
                     "which the n − 1 touching a context change when its model does. Published, each context "
                     "translates to and from one shared language: n translators, of which 1 changes. When the lesson "
                     "counts one-way translators (directed), each figure doubles: n(n − 1) and 2(n − 1), 2n and 2. "
                     "The ratios are pairwise over published, exact, and the same either way.",
            "js": DCX_VIEW_JS["protocol"],
        },
    },
}

_PART_SUB = [("part", _N), ("kind", ea.word("core", "supporting", "generic")), ("weeks", ea.whole(0, 100000)),
             ("strong", ea.whole(0, 1000))]

_PARTS = vrec("Parts (part, kind, developer-weeks, strongest developers, and for a generic part an option)", _PART_SUB,
              ea.word("build", "buy", "published", "outsource"), "option", 0, 1, unique=True, rows=4)


DISTILL = {
    "prefix": "dds", "fn": "ddsCompute", "title": "Distillation: where the effort goes", "js": DDS_JS,
    "views": {
        "effort": {
            "fields": [("parts", _PARTS, None)],
            "tiles": [("Developer-weeks built in house", "ddsWeeks"), ("Share on the core", "ddsCore"),
                      ("Share on supporting parts", "ddsSupporting"), ("Share on generic parts", "ddsGeneric"),
                      ("Strongest developers on the core", "ddsStrong"), ("Generic parts built in house", "ddsBuilt"),
                      ("Weeks buying or publishing would free", "ddsFree")],
            "check": _check_effort,
            "subtitle": "the share of effort and of the strongest developers on the core domain",
            "rules": "Each part is core, supporting or generic, with its developer-weeks and the number of the team's "
                     "strongest developers on it. A part may end with an option: build (the same as none), buy, "
                     "published (a published model adopted) or outsource; only a generic part may take one other than "
                     "build, and a part not built has no strongest developers on it. Only built parts count their "
                     "weeks. The shares are each kind's built "
                     "weeks over all built weeks, exact. The strongest on the core are counted against the strongest "
                     "on every built part. The weeks buying or publishing would free are those of the generic parts "
                     "still built in house.",
            "js": DDS_VIEW_JS["effort"],
        },
    },
}

_ENTRIES = ("entries", ea.rec("Entries (transaction, account, amount)",
                              [("txn", _N), ("account", _N), ("amount", ea.num(lo=-ea.LIMIT))], rows=4), None)

LEDGER = {
    "prefix": "dle", "fn": "dleCompute", "title": "Accounts and entries", "js": DLE_JS,
    "views": {
        "balance": {
            "fields": [_ENTRIES],
            "tiles": [("Accounts", "dleAccounts"), ("Balances", "dleBalances"), ("Transactions", "dleTxns"),
                      ("Unbalanced transactions (net)", "dleUnbalanced"), ("Total of all entries", "dleTotal")],
            "check": _check_balance,
            "subtitle": "balances from entries, and transactions that do not balance",
            "rules": "Amounts are signed and exact to the cent (at most 2 decimal places). An account's balance is the "
                     "sum of its entries; accounts are listed in the order they first appear. A transaction balances "
                     "when its entries sum to 0; the others are listed, in the order first given, with their net.",
            "js": DLE_VIEW_JS["balance"],
        },
        "post": {
            "fields": [_ENTRIES,
                       ("rules", ea.rec("Posting rules (rule, from account, to account, share 0 to 1)",
                                        [("rule", _N), ("from", _N), ("to", _N), ("share", ea.num(lo=0, hi=1))],
                                        unique=True, rows=2, hi=20), None)],
            "tiles": [("Entries given", "dleGiven"), ("Entries derived", "dleDerived"),
                      ("Balances after", "dleBalances"), ("Derived postings", "dleList"),
                      ("Rounding left (exact − rounded, summed)", "dleLeft")],
            "check": _check_post,
            "subtitle": "posting rules that derive entries",
            "rules": "Amounts are exact to the cent. When a given entry posts to a rule's from account, the rule posts "
                     "share × the amount to its to account and the same amount negated back to the from account, in "
                     "the entry's transaction: two derived entries, rounded to the cent half away from zero, even when "
                     "they round to 0.00. Every rule fires once on every given entry to its account, rules in the order "
                     "given; a derived entry fires no rule. Balances after list accounts in the order they first "
                     "appear in the journal, each given entry followed by what it derives. The rounding left sums the "
                     "exact share less the rounded one over every firing.",
            "js": DLE_VIEW_JS["post"],
        },
    },
}

SPECS = {"modules": MODULES, "context": CONTEXT, "distill": DISTILL, "ledger": LEDGER}


def _with_fields(spec, view, fields):
    views = dict(spec["views"])
    views[view] = dict(views[view], fields=fields)
    return dict(spec, views=views)


def modules_lab(cfg):
    spec = MODULES
    view = cfg.get("view", "cohesion")
    if view in ("cohesion", "change") and cfg.get("packagings", 1) == 2:
        fields = list(spec["views"][view]["fields"])
        fields[0] = ("elements", _elements(True), None)
        spec = _with_fields(spec, view, fields)
    return mode_lab(cfg, "modules", spec)


def context_lab(cfg):
    return mode_lab(cfg, "context", CONTEXT)


def distill_lab(cfg):
    return mode_lab(cfg, "distill", DISTILL)


def ledger_lab(cfg):
    return mode_lab(cfg, "ledger", LEDGER)


MODES = {"modules": modules_lab, "context": context_lab, "distill": distill_lab, "ledger": ledger_lab}

__all__ = ["MODES", "SPECS"]
