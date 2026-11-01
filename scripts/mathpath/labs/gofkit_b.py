"""gofkit_b -- family B of the Design Patterns kit: requests, notifications, history, states, sharing.

Specified in docs/design-patterns/PLAN.md section D (family B); the seam with
family A (gofkit.py: the entry point and modes classes, tree, expr) is
docs/design-patterns/kit-contract.md; the report an author configures a lesson
from is the "Family B" section of docs/design-patterns/kit-report.md. Six
modes:

  route    (grt)  chain, wrap, template   Chain of Responsibility, Decorator, Template Method
  notify   (gno)  observer                Observer (and MVC in Chapter 1)
  history  (ghi)  undo                    Command, Memento (and Lexi's user operations)
  machine  (gsm)  states                  State
  share    (gsh)  flyweight               Flyweight
  proxy    (gpx)  access                  Proxy, Singleton

Each mode has one base block <PREFIX>_JS defining the pure function
<prefix>Compute(view, inst, opts), which scripts/mathcheck.js calls (section
"gofkit (Design Patterns), family B"), and one block per view. A page ships
RATIONAL_JS, EA_CORE_JS, DDD_CORE_JS, GOF_CORE_JS, the mode's base block and
its own view's block only.

THE DESIGNS ARE THE LESSON'S. No handler, subject, command, state or object is
a constant here: every one arrives in a preset. Nothing typed is evaluated as
script. Nothing here judges a design: every tile is a count over the design
the lesson states, and every status line says so (gofStatus).

IDS. Every JS function and variable and every element id begins with its
mode's prefix (grt, gno, ghi, gsm, gsh, gpx). Grepped as identifier starts
against scripts/mathpath/labs/*.py and scripts/*.js on 2026-11-01: none is
used by another kit. Names beginning gof / GOF_ are family A's; none is
defined here. Every lookup table keyed by a typed name is made with
Object.create(null), so a name such as constructor or __proto__ is only a name.

SAMPLES at the end holds one worked cfg per view, its presets pinned with
expect; every pinned string was counted by hand and read off a rendered page.
"""

import re
from fractions import Fraction

from . import eakit_core as ea
from .gofkit import mode_lab, vrec

# ---------------------------------------------------------------------------
# route (grt): requests in motion -- a chain, a stack of wrappers, a template
# ---------------------------------------------------------------------------

GRT_JS = r"""
  var GRT_VIEW = {};
  function grtCompute(view, inst, opts) { return eaRun(GRT_VIEW[view], inst, opts); }
  function grtMap() { return Object.create(null); }
"""

GRT_VIEW_JS = {}

GRT_VIEW_JS["chain"] = r"""
  /* A handler's topics: names, or all (takes every request), or - (takes none). */
  GRT_VIEW.chain = function (inst) {
    var H = inst.handlers, Q = inst.requests, n = H.length, takes = [], per = [], rows = [], hops = 0, handled = 0, un = [];
    H.forEach(function (h, i) {
      var set = grtMap(), w = 'Handlers, record ' + (i + 1) + ': ' + h.handler;
      h.rest.forEach(function (t) {
        if ((t === '-' || t === 'all') && h.rest.length > 1) eaRefuse(w + ' gives ' + t + ' with other topics; ' + t + ' stands alone');
        if (set[t]) eaRefuse(w + ' takes ' + t + ' twice');
        set[t] = true;
      });
      takes.push({ all: h.rest[0] === 'all', none: h.rest[0] === '-', set: set });
      per.push(0);
    });
    Q.forEach(function (q, i) {
      if (q === '-' || q === 'all') eaRefuse('Requests, entry ' + (i + 1) + ': ' + q + ' is not a topic (all and - mark what a handler takes)');
    });
    Q.forEach(function (q, i) {
      var at = -1, path = [];
      for (var k = 0; k < n; k += 1) {
        path.push(H[k].handler);
        if (!takes[k].none && (takes[k].all || takes[k].set[q])) { at = k; break; }
      }
      if (at >= 0) { handled += 1; per[at] += 1; hops += at; }
      else { hops += n - 1; un.push(q + ' (' + (i + 1) + ')'); }
      rows.push([String(i + 1), q, path.join(' → ') + (at < 0 ? ' → off the end' : ''), at >= 0 ? H[at].handler : 'no one', String(at >= 0 ? at : n - 1)]);
    });
    var best = -1;
    per.forEach(function (c, k) { if (c > 0 && (best < 0 || c > per[best])) best = k; });
    var tied = best < 0 ? [] : H.filter(function (h, k) { return per[k] === per[best] && k !== best; }).map(function (h) { return h.handler; });
    return {
      tiles: { grtRequests: eaInt(Q.length), grtHandled: eaInt(handled) + ' of ' + eaInt(Q.length), grtHops: eaInt(hops),
        grtUnhandled: dddListed(un.length, un), grtPer: H.map(function (h, k) { return h.handler + ' ' + eaInt(per[k]); }).join(', '),
        grtBusiest: best < 0 ? 'none' : H[best].handler + ', ' + eaPlural(per[best], 'request', 'requests') },
      status: gofStatus('Of ' + eaPlural(Q.length, 'request', 'requests') + ' sent to the head of a chain of ' + eaPlural(n, 'handler', 'handlers')
        + ', ' + eaInt(handled) + (handled === 1 ? ' is' : ' are') + ' handled and ' + eaInt(un.length) + (un.length === 1 ? ' falls' : ' fall')
        + ' off the end; requests are passed on ' + eaPlural(hops, 'time', 'times') + ' in all.'
        + (tied.length ? ' ' + tied.join(', ') + (tied.length === 1 ? ' ties' : ' tie') + ' for the busiest; the tile shows the first in the chain.' : '')),
      table: { caption: 'Each request, the handlers it reaches in order, and who takes it', head: ['request', 'topic', 'path', 'taken by', 'passed on'], rows: rows }
    };
  };
"""

GRT_VIEW_JS["wrap"] = r"""
  function grtValue(text, what) { try { return dddValue(text, what); } catch (e) { eaRefuse(e.message); } }
  /* An exact decimal, as typed: every value here is a sum or product of decimals, so it terminates. */
  function grtDec(r) {
    var neg = r.n < 0n, n = neg ? -r.n : r.n, whole = n / r.d, rem = n % r.d, frac = '', i;
    for (i = 0; i < 80 && rem !== 0n; i += 1) { rem *= 10n; frac += String(rem / r.d); rem %= r.d; }
    return (neg ? EA_MINUS : '') + String(whole) + (frac ? '.' + frac : '');
  }
  GRT_VIEW.wrap = function (inst) {
    var c = inst.core[0], L = inst.layers, n = L.length, base = grtValue(c.value, 'The component’s value'), text = base.kind === 'word', ops = [], at = grtMap();
    L.forEach(function (l, i) {
      var w = 'Decorators, record ' + (i + 1) + ': ' + l.decorator;
      if (l.decorator === c.component) eaRefuse(w + ' has the component’s name');
      if (text && l.op !== 'then') eaRefuse(w + ' uses ' + l.op + ', and the component’s value ' + c.value + ' is a word, which takes only then');
      if (!text && l.op === 'then') eaRefuse(w + ' uses then, and the component’s value ' + c.value + ' is a number, which takes add or times');
      var v = null;
      if (!text) {
        v = grtValue(l.amount, w + ': amount');
        if (v.kind !== 'num') eaRefuse(w + ': amount ' + l.amount + ' should be a number for ' + l.op);
      }
      ops.push({ name: l.decorator, op: l.op, r: v ? v.r : null, w: l.amount });
      at[l.decorator] = ops.length - 1;
    });
    var other;
    if (inst.order.length) {
      inst.order.forEach(function (d, i) { if (at[d] === undefined) eaRefuse('The other order, entry ' + (i + 1) + ': ' + d + ' is not one of the decorators'); });
      if (inst.order.length !== n) eaRefuse('The other order names ' + eaInt(inst.order.length) + ' of the ' + eaPlural(n, 'decorator', 'decorators') + '; give each once, innermost first');
      other = inst.order.map(function (d) { return ops[at[d]]; });
    } else other = ops.slice().reverse();
    /* The result returns from the core outward: the innermost decorator applies first. */
    function run(list) {
      var v = text ? base.w : base.r;
      list.forEach(function (o) { v = text ? v + ' ' + o.w : (o.op === 'add' ? Radd(v, o.r) : Rmul(v, o.r)); });
      return text ? v : grtDec(v);
    }
    var res = run(ops), alt = run(other), names = ops.map(function (o) { return o.name; }), out = names.slice().reverse();
    var sub = 1n << BigInt(n);
    return {
      tiles: { grtLayers: eaInt(n), grtCalls: 'in: ' + out.join(', ') + '; core: ' + c.component + '; out: ' + names.join(', '),
        grtResult: res, grtOther: alt, grtMatters: res === alt ? 'no' : 'yes',
        grtSubclass: eaInt(sub) + ' (the component + ' + eaInt(sub - 1n) + ' combinations)',
        grtDecorator: eaInt(n + 3) + ' (interface, component, abstract decorator + ' + eaInt(n) + ')',
        grtAddOne: 'subclassing +' + eaInt(sub) + ', Decorator +1' },
      status: gofStatus('A call enters ' + eaPlural(n, 'decorator', 'decorators') + ' outermost first, reaches ' + c.component
        + ' and returns through them innermost first, so ' + names[0] + ' applies first: the result is ' + res + '. '
        + (inst.order.length ? 'In the other order given' : 'In the reverse order') + ' it is ' + alt + '.'),
      table: { caption: 'Each decorator, innermost first, and the value as the call returns through it',
        head: ['position', 'decorator', 'does', 'value after'],
        rows: ops.map(function (o, i) { return [String(i + 1), o.name, o.op + ' ' + o.w, run(ops.slice(0, i + 1))]; }) }
    };
  };
"""

GRT_VIEW_JS["template"] = r"""
  GRT_VIEW.template = function (inst) {
    var S = inst.steps, kind = grtMap(), cnt = { fixed: 0, primitive: 0, hook: 0 }, rows = [], own = [], hooks = [], abs = [], over = 0;
    S.forEach(function (s) { kind[s.step] = s.kind; cnt[s.kind] += 1; });
    inst.subclasses.forEach(function (c, i) {
      var mine = grtMap(), w = 'Subclasses, record ' + (i + 1) + ': ' + c.subclass;
      c.rest.forEach(function (s) {
        if (s === '-') { if (c.rest.length > 1) eaRefuse(w + ' gives - with steps; - stands alone'); return; }
        if (kind[s] === undefined) eaRefuse(w + ' overrides ' + s + ', which is not one of the steps');
        if (kind[s] === 'fixed') eaRefuse(w + ' overrides ' + s + ', a fixed step; only primitive operations and hooks are overridden');
        if (mine[s]) eaRefuse(w + ' overrides ' + s + ' twice');
        mine[s] = true;
      });
      var o = 0, h = 0, lacks = [], seq = S.map(function (s) {
        if (s.kind === 'fixed') return s.step + ' base';
        if (mine[s.step]) { o += 1; if (s.kind === 'hook') h += 1; return s.step + ' own'; }
        if (s.kind === 'hook') return s.step + ' base default';
        lacks.push(s.step); return s.step + ' MISSING';
      });
      over += o;
      own.push(c.subclass + ' ' + eaInt(o)); hooks.push(c.subclass + ' ' + eaInt(h));
      if (lacks.length) abs.push(c.subclass + ' (lacks ' + lacks.join(', ') + ')');
      rows.push([c.subclass, seq.join(', '), eaInt(cnt.primitive - lacks.length) + ' of ' + eaInt(cnt.primitive), eaInt(h) + ' of ' + eaInt(cnt.hook)]);
    });
    var k = inst.subclasses.length, inBase = cnt.fixed + cnt.hook;
    return {
      tiles: { grtSteps: eaInt(S.length) + ': ' + eaInt(cnt.fixed) + ' fixed, ' + eaInt(cnt.primitive) + ' primitive, ' + eaPlural(cnt.hook, 'hook', 'hooks'),
        grtOwn: own.join(', '), grtAbstract: dddListed(abs.length, abs, '; '), grtHooks: hooks.join(', '), grtBase: eaInt(inBase),
        grtWhole: eaInt(S.length * k), grtWith: eaInt(inBase + over) },
      status: gofStatus('Each of ' + eaPlural(k, 'subclass', 'subclasses') + ' runs the same ' + eaPlural(S.length, 'step', 'steps')
        + ' in the base class’s order. Written whole in every subclass that is ' + eaPlural(S.length * k, 'step body', 'step bodies')
        + '; with the template it is ' + eaInt(inBase + over) + '.'
        + (abs.length ? ' ' + eaPlural(abs.length, 'subclass is', 'subclasses are') + ' left abstract, lacking a primitive operation.' : '')),
      table: { caption: 'Each subclass: the steps it runs, whose code runs at each, the primitive operations it supplies and the hooks it overrides',
        head: ['subclass', 'runs', 'primitives supplied', 'hooks overridden'], rows: rows }
    };
  };
"""

# ---------------------------------------------------------------------------
# notify (gno): Observer, directly and through a change manager
# ---------------------------------------------------------------------------

GNO_JS = r"""
  var GNO_VIEW = {};
  function gnoCompute(view, inst, opts) { return eaRun(GNO_VIEW[view], inst, opts); }
"""

GNO_VIEW_JS = {}

GNO_VIEW_JS["observer"] = r"""
  GNO_VIEW.observer = function (inst) {
    var subj = Object.create(null), O = inst.observers, P = inst.operations, managed = inst.scheme === 'managed';
    inst.subjects.forEach(function (s) { subj[s] = []; });
    O.forEach(function (o, i) {
      var seen = Object.create(null), w = 'Observers, record ' + (i + 1) + ': ' + o.observer;
      o.rest.forEach(function (s) {
        if (subj[s] === undefined) eaRefuse(w + ' observes ' + s + ', which is not one of the subjects');
        if (seen[s]) eaRefuse(w + ' observes ' + s + ' twice');
        seen[s] = true; subj[s].push(i);
      });
    });
    P.forEach(function (p, i) {
      p.rest.forEach(function (s) { if (subj[s] === undefined) eaRefuse('Operations, record ' + (i + 1) + ': ' + p.operation + ' changes ' + s + ', which is not one of the subjects'); });
    });
    var changes = 0, sentD = 0, sentM = 0, totD = O.map(function () { return 0; }), totM = totD.slice(), rows = [];
    P.forEach(function (p) {
      var d = O.map(function () { return 0; });
      p.rest.forEach(function (s) { changes += 1; subj[s].forEach(function (k) { d[k] += 1; }); });
      var cells = d.map(function (x, k) {
        var m = x > 0 ? 1 : 0;
        sentD += x; sentM += m; totD[k] += x; totM[k] += m;
        return managed ? (x > 1 ? m + ' (of ' + x + ')' : String(m)) : String(x);
      });
      rows.push([p.operation, eaInt(p.rest.length)].concat(cells));
    });
    var tot = managed ? totM : totD, sent = managed ? sentM : sentD;
    var never = O.filter(function (o, k) { return totD[k] === 0; }).map(function (o) { return o.observer; });
    var lone = inst.subjects.filter(function (s) { return subj[s].length === 0; });
    return {
      tiles: { gnoChanges: eaInt(changes), gnoSent: eaInt(sent), gnoOther: (managed ? 'direct: ' + eaInt(sentD) : 'managed: ' + eaInt(sentM)),
        gnoRedundant: eaInt(sentD - sentM), gnoPer: O.map(function (o, k) { return o.observer + ' ' + eaInt(tot[k]); }).join(', '),
        gnoNever: dddListed(never.length, never), gnoUnobserved: dddListed(lone.length, lone) },
      status: gofStatus(eaPlural(P.length, 'operation makes', 'operations make') + ' ' + eaPlural(changes, 'change', 'changes') + '. Sent directly, each change notifies every observer of its subject: '
        + eaPlural(sentD, 'update', 'updates') + '. Through a change manager, each observer is updated once per operation that changed what it observes: '
        + eaInt(sentM) + ', so ' + eaInt(sentD - sentM) + ' direct ' + (sentD - sentM === 1 ? 'update is' : 'updates are') + ' redundant.'),
      table: { caption: 'Updates each operation sends to each observer, ' + (managed ? 'through a change manager (direct in brackets where it sends more)' : 'sent directly'),
        head: ['operation', 'changes'].concat(O.map(function (o) { return o.observer; })), rows: rows }
    };
  };
"""

# ---------------------------------------------------------------------------
# history (ghi): Command and Memento -- undo, redo, and what the history holds
# ---------------------------------------------------------------------------

GHI_JS = r"""
  var GHI_VIEW = {};
  function ghiCompute(view, inst, opts) { return eaRun(GHI_VIEW[view], inst, opts); }
"""

GHI_VIEW_JS = {}

GHI_VIEW_JS["undo"] = r"""
  GHI_VIEW.undo = function (inst) {
    var st = Object.create(null), cells = [], cmd = Object.create(null), snap = inst.scheme === 'snapshot';
    inst.state.forEach(function (c) { st[c.cell] = c.value.n; cells.push(c.cell); });
    inst.commands.forEach(function (c, i) {
      var w = 'Commands, record ' + (i + 1) + ': ' + c.command;
      if (c.command === 'undo' || c.command === 'redo') eaRefuse(w + ' is a word the script reserves; name the command otherwise');
      if (st[c.cell] === undefined) eaRefuse(w + ' acts on ' + c.cell + ', which is not one of the cells');
      cmd[c.command] = c;
    });
    inst.script.forEach(function (s, i) {
      if (s !== 'undo' && s !== 'redo' && cmd[s] === undefined) eaRefuse('Script, entry ' + (i + 1) + ': ' + s + ' is not undo, redo or one of the commands');
    });
    var U = [], Rd = [], refU = 0, refR = 0, gone = 0, rows = [];
    function apply(c) { var old = st[c.cell]; st[c.cell] = c.op === 'set' ? c.amount.n : old + c.amount.n; return old; }
    function show() { return cells.map(function (k) { return k + ' ' + eaInt(st[k]); }).join(', '); }
    function names(a) { return dddListed(a.length, a.map(function (e) { return e.c.command; })); }
    inst.script.forEach(function (s, i) {
      var did;
      if (s === 'undo') {
        if (!U.length) { refU += 1; did = 'nothing to undo'; }
        else { var e = U.pop(); st[e.c.cell] = e.c.op === 'set' ? e.old : st[e.c.cell] - e.c.amount.n; Rd.push(e); did = 'undid ' + e.c.command; }
      } else if (s === 'redo') {
        if (!Rd.length) { refR += 1; did = 'nothing to redo'; }
        else { var f = Rd.pop(); f.old = apply(f.c); U.push(f); did = 'redid ' + f.c.command; }
      } else {
        var c = cmd[s];
        U.push({ c: c, old: apply(c) });
        did = 'ran ' + s + (Rd.length ? ', discarding ' + eaPlural(Rd.length, 'redo', 'redos') : '');
        gone += Rd.length; Rd = [];
      }
      rows.push([String(i + 1), s, did, show(), names(U), names(Rd)]);
    });
    var held = U.concat(Rd), inv = held.filter(function (e) { return e.c.op === 'set'; }).length, shot = held.length * cells.length;
    return {
      tiles: { ghiFinal: show(), ghiUndo: names(U), ghiRedo: names(Rd), ghiRefused: 'undo ' + eaInt(refU) + ', redo ' + eaInt(refR),
        ghiDiscarded: eaInt(gone), ghiStored: eaInt(snap ? shot : inv), ghiOther: (snap ? 'inverse: ' + eaInt(inv) : 'snapshot: ' + eaInt(shot)) },
      status: gofStatus(eaPlural(inst.script.length, 'step', 'steps') + ' leave ' + eaPlural(U.length, 'command', 'commands') + ' to undo and '
        + eaInt(Rd.length) + ' to redo. The history holds ' + eaPlural(held.length, 'entry', 'entries') + ': as inverse operations that is '
        + eaPlural(inv, 'stored value', 'stored values') + ' (one old value per set), as snapshots ' + eaInt(shot) + ' (every cell per entry); the states are the same either way.'),
      table: { caption: 'Each step of the script: what it did, the state after, and the two stacks (bottom to top)',
        head: ['step', 'script', 'did', 'state after', 'undo stack', 'redo stack'], rows: rows }
    };
  };
"""

# ---------------------------------------------------------------------------
# machine (gsm): State -- a trace, and one conditional against state classes
# ---------------------------------------------------------------------------

GSM_JS = r"""
  var GSM_VIEW = {};
  function gsmCompute(view, inst, opts) { return eaRun(GSM_VIEW[view], inst, opts); }
"""

GSM_VIEW_JS = {}

GSM_VIEW_JS["states"] = r"""
  GSM_VIEW.states = function (inst) {
    var S = inst.states, E = inst.events, isS = Object.create(null), isE = Object.create(null), next = Object.create(null), out = Object.create(null);
    S.forEach(function (s) { isS[s] = true; out[s] = 0; });
    E.forEach(function (e) { isE[e] = true; });
    inst.transitions.forEach(function (t, i) {
      var w = 'Transitions, record ' + (i + 1) + ': ';
      [t.state, t.next].forEach(function (s) { if (!isS[s]) eaRefuse(w + s + ' is not one of the states'); });
      if (!isE[t.event]) eaRefuse(w + t.event + ' is not one of the events');
      var k = t.state + ' ' + t.event;
      if (next[k] !== undefined) eaRefuse(w + t.state + ' already has a transition on ' + t.event + ' (record ' + next[k].at + ')');
      next[k] = { to: t.next, at: i + 1 };
      out[t.state] += 1;
    });
    inst.input.forEach(function (e, i) { if (!isE[e]) eaRefuse('Input, entry ' + (i + 1) + ': ' + e + ' is not one of the events'); });
    var cur = S[0], seen = Object.create(null), ign = [], rows = [];
    seen[cur] = true;
    inst.input.forEach(function (e, i) {
      var t = next[cur + ' ' + e];
      if (t === undefined) { ign.push(e + ' at ' + cur + ' (' + (i + 1) + ')'); rows.push([String(i + 1), cur, e, 'ignored: stays ' + cur]); return; }
      rows.push([String(i + 1), cur, e, t.to]);
      cur = t.to; seen[cur] = true;
    });
    var T = inst.transitions.length, best = S[0];
    S.forEach(function (s) { if (out[s] > out[best]) best = s; });
    var never = S.filter(function (s) { return !seen[s]; });
    return {
      tiles: { gsmFinal: cur, gsmIgnored: dddListed(ign.length, ign), gsmDefined: eaInt(T), gsmBranches: eaInt(T + S.length),
        gsmClasses: eaInt(S.length + 2), gsmLargest: best + ', ' + eaPlural(out[best], 'transition', 'transitions'), gsmNever: dddListed(never.length, never) },
      status: gofStatus('From ' + S[0] + ', ' + eaPlural(inst.input.length, 'event', 'events') + ' end in ' + cur + ', with ' + eaInt(ign.length)
        + ' ignored. One conditional on the state and the event needs ' + eaPlural(T + S.length, 'branch', 'branches')
        + ' in one method; State needs ' + eaPlural(S.length + 2, 'class', 'classes') + ', the largest handling ' + eaPlural(out[best], 'event', 'events') + '.'),
      table: { caption: 'The trace: each event, the state it meets and the state it leaves', head: ['step', 'state', 'event', 'next'], rows: rows }
    };
  };
"""

# ---------------------------------------------------------------------------
# share (gsh): Flyweight -- storage without sharing and with
# ---------------------------------------------------------------------------

GSH_JS = r"""
  var GSH_VIEW = {};
  function gshCompute(view, inst, opts) { return eaRun(GSH_VIEW[view], inst, opts); }
"""

GSH_VIEW_JS = {}

GSH_VIEW_JS["flyweight"] = r"""
  GSH_VIEW.flyweight = function (inst) {
    var I = inst.intrinsic.n, X = inst.extrinsic.n, ref = inst.ref.n, kept = inst.stored === 'yes', per = kept ? X + ref : ref;
    var G = inst.objects, N = 0n, F = BigInt(G.length), big = G[0], small = G[0], rows = [];
    G.forEach(function (g) {
      N += g.count.n;
      if (g.count.n > big.count.n) big = g;
      if (g.count.n < small.count.n) small = g;
      rows.push([g.key, eaInt(g.count.n), eaInt(g.count.n * (I + X)), eaInt(I + g.count.n * per)]);
    });
    var without = N * (I + X), withs = F * I + N * per, saved = without - withs;
    return {
      tiles: { gshObjects: eaInt(N), gshFlyweights: eaInt(F), gshWithout: eaInt(without), gshWith: eaInt(withs), gshSaved: eaInt(saved),
        gshShare: eaPct(R(saved, without)), gshLargest: big.key + ', ' + eaPlural(big.count.n, 'object', 'objects'),
        gshSmallest: small.key + ', ' + eaPlural(small.count.n, 'object', 'objects') },
      status: gofStatus(eaPlural(N, 'object shares', 'objects share') + ' ' + eaPlural(F, 'flyweight', 'flyweights') + '. Unshared, every object holds its '
        + eaInt(I) + ' intrinsic and ' + eaInt(X) + ' extrinsic bytes: ' + eaInt(without) + '. Shared, the intrinsic state is held once per flyweight'
        + (kept ? ' and each object keeps its extrinsic state' : ' and the extrinsic state is computed, not stored') + (ref > 0n ? ', with a ' + eaInt(ref) + '-byte reference per object' : '')
        + ': ' + eaInt(withs) + (saved < 0n ? ', which is more' : '') + '.'),
      table: { caption: 'Each intrinsic state: its objects, and the bytes they take without sharing and with one flyweight',
        head: ['intrinsic state', 'objects', 'bytes unshared', 'bytes shared'], rows: rows }
    };
  };
"""

# ---------------------------------------------------------------------------
# proxy (gpx): Proxy and Singleton -- when costly subjects are created
# ---------------------------------------------------------------------------

GPX_JS = r"""
  var GPX_VIEW = {};
  function gpxCompute(view, inst, opts) { return eaRun(GPX_VIEW[view], inst, opts); }
"""

GPX_VIEW_JS = {}

GPX_VIEW_JS["access"] = r"""
  GPX_VIEW.access = function (inst) {
    var cost = Object.create(null), order = [], may = null;
    inst.subjects.forEach(function (s) { cost[s.subject] = s.cost.n; order.push(s.subject); });
    inst.requests.forEach(function (q, i) {
      if (cost[q.subject] === undefined) eaRefuse('Requests, record ' + (i + 1) + ': ' + q.subject + ' is not one of the subjects');
    });
    if (inst.rights.length) {
      may = Object.create(null);
      inst.rights.forEach(function (r, i) {
        var m = Object.create(null), w = 'Rights, record ' + (i + 1) + ': ' + r.client;
        r.rest.forEach(function (s) {
          if (cost[s] === undefined) eaRefuse(w + ' may use ' + s + ', which is not one of the subjects');
          if (m[s]) eaRefuse(w + ' names ' + s + ' twice');
          m[s] = true;
        });
        may[r.client] = m;
      });
    }
    var refused = [], served = [];
    inst.requests.forEach(function (q, i) {
      if (may && !(may[q.client] && may[q.client][q.subject])) refused.push(q.client + ' → ' + q.subject + ' (' + (i + 1) + ')');
      else served.push(i);
    });
    function run(scheme) {
      var made = Object.create(null), r = { creations: 0, start: 0n, total: 0n, first: null, paid: [], did: [] };
      if (scheme === 'eager') order.forEach(function (s) { made[s] = true; r.creations += 1; r.start += cost[s]; });
      r.total = r.start;
      inst.requests.forEach(function (q, i) {
        if (served.indexOf(i) < 0) { r.paid.push(null); r.did.push('refused'); return; }
        var c = 0n, fresh = scheme === 'fresh' || !made[q.subject];
        if (fresh) { c = cost[q.subject]; made[q.subject] = true; r.creations += 1; }
        r.total += c; r.paid.push(c); r.did.push(fresh ? 'created' : 'reused');
        if (r.first === null) r.first = c;
      });
      return r;
    }
    var all = { eager: run('eager'), lazy: run('lazy'), fresh: run('fresh') }, me = all[inst.scheme];
    var asked = Object.create(null);
    served.forEach(function (i) { asked[inst.requests[i].subject] = true; });
    var never = order.filter(function (s) { return !asked[s]; });
    var rows = inst.requests.map(function (q, i) {
      var c = me.paid[i];
      return [String(i + 1), q.client, q.subject, me.did[i], c === null ? '—' : eaInt(c)];
    });
    return {
      tiles: { gpxRequests: eaInt(inst.requests.length), gpxRefused: dddListed(refused.length, refused), gpxCreations: eaInt(me.creations),
        gpxStart: eaInt(me.start), gpxTotal: eaInt(me.total), gpxNever: dddListed(never.length, never), gpxAlive: eaInt(me.creations),
        gpxFirst: me.first === null ? 'none served' : eaInt(me.first),
        gpxCompare: 'eager ' + eaInt(all.eager.total) + ', lazy ' + eaInt(all.lazy.total) + ', fresh ' + eaInt(all.fresh.total) },
      status: gofStatus('Of ' + eaPlural(inst.requests.length, 'request', 'requests') + ', ' + eaInt(refused.length) + (refused.length === 1 ? ' is' : ' are') + ' refused. '
        + (inst.scheme === 'eager' ? 'Every subject is created at the start' : inst.scheme === 'lazy' ? 'Each subject is created on its first request and reused' : 'Every request served creates a new instance')
        + ': ' + eaPlural(me.creations, 'instance', 'instances') + ', costing ' + eaInt(me.total) + ' in all'
        + (inst.scheme === 'eager' && never.length ? ', ' + eaInt(never.length) + ' of them for subjects never requested' : '') + '.'),
      table: { caption: 'Each request, ' + inst.scheme + ': whether it is refused, creates its subject or reuses one, and what it costs',
        head: ['request', 'client', 'subject', 'outcome', 'cost'], rows: rows }
    };
  };
"""

# ---------------------------------------------------------------------------
# Python: the checks (each mirrors a JS refusal beyond the field parser)
# ---------------------------------------------------------------------------

_WORD = re.compile(r"^[A-Za-z][A-Za-z0-9._-]*$")
_NUMBER = re.compile(r"-?(?:\d+(?:\.(\d+))?|\.(\d+))")


def _quote(s):
    s = str(s)
    return '"%s"' % (s[:40] + "…" if len(s) > 40 else s)


def _value(text, what):
    """Mirror of dddValue: ('num', Fraction) or ('word', str)."""
    s = str(text).replace("−", "-").strip()
    if s == "":
        raise ValueError("%s is empty" % what)
    m = _NUMBER.fullmatch(s)
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


def _check_chain(inst, fixed):
    for i, h in enumerate(inst["handlers"]):
        w, seen = "Handlers, record %d: %s" % (i + 1, h["handler"]), set()
        for t in h["rest"]:
            if t in ("-", "all") and len(h["rest"]) > 1:
                raise ValueError("%s gives %s with other topics; %s stands alone" % (w, t, t))
            if t in seen:
                raise ValueError("%s takes %s twice" % (w, t))
            seen.add(t)
    for i, q in enumerate(inst["requests"]):
        if q in ("-", "all"):
            raise ValueError("Requests, entry %d: %s is not a topic (all and - mark what a handler takes)" % (i + 1, q))


def _check_wrap(inst, fixed):
    c = inst["core"][0]
    base = _value(c["value"], "The component’s value")
    text = base[0] == "word"
    names = set()
    for i, l in enumerate(inst["layers"]):
        w = "Decorators, record %d: %s" % (i + 1, l["decorator"])
        if l["decorator"] == c["component"]:
            raise ValueError("%s has the component’s name" % w)
        if text and l["op"] != "then":
            raise ValueError("%s uses %s, and the component’s value %s is a word, which takes only then"
                             % (w, l["op"], c["value"]))
        if not text and l["op"] == "then":
            raise ValueError("%s uses then, and the component’s value %s is a number, which takes add or times"
                             % (w, c["value"]))
        if not text and _value(l["amount"], "%s: amount" % w)[0] != "num":
            raise ValueError("%s: amount %s should be a number for %s" % (w, l["amount"], l["op"]))
        names.add(l["decorator"])
    order = inst["order"]
    if order:
        for i, d in enumerate(order):
            if d not in names:
                raise ValueError("The other order, entry %d: %s is not one of the decorators" % (i + 1, d))
        n = len(inst["layers"])
        if len(order) != n:
            raise ValueError("The other order names %s of the %s %s; give each once, innermost first"
                             % (ea.grp(len(order)), ea.grp(n), "decorator" if n == 1 else "decorators"))


def _check_template(inst, fixed):
    kind = {s["step"]: s["kind"] for s in inst["steps"]}
    for i, c in enumerate(inst["subclasses"]):
        w, mine = "Subclasses, record %d: %s" % (i + 1, c["subclass"]), set()
        for s in c["rest"]:
            if s == "-":
                if len(c["rest"]) > 1:
                    raise ValueError("%s gives - with steps; - stands alone" % w)
                continue
            if s not in kind:
                raise ValueError("%s overrides %s, which is not one of the steps" % (w, s))
            if kind[s] == "fixed":
                raise ValueError("%s overrides %s, a fixed step; only primitive operations and hooks are overridden"
                                 % (w, s))
            if s in mine:
                raise ValueError("%s overrides %s twice" % (w, s))
            mine.add(s)


def _check_observer(inst, fixed):
    subj = set(inst["subjects"])
    for i, o in enumerate(inst["observers"]):
        w, seen = "Observers, record %d: %s" % (i + 1, o["observer"]), set()
        for s in o["rest"]:
            if s not in subj:
                raise ValueError("%s observes %s, which is not one of the subjects" % (w, s))
            if s in seen:
                raise ValueError("%s observes %s twice" % (w, s))
            seen.add(s)
    for i, p in enumerate(inst["operations"]):
        for s in p["rest"]:
            if s not in subj:
                raise ValueError("Operations, record %d: %s changes %s, which is not one of the subjects"
                                 % (i + 1, p["operation"], s))


def _check_undo(inst, fixed):
    cells = {c["cell"] for c in inst["state"]}
    cmds = set()
    for i, c in enumerate(inst["commands"]):
        w = "Commands, record %d: %s" % (i + 1, c["command"])
        if c["command"] in ("undo", "redo"):
            raise ValueError("%s is a word the script reserves; name the command otherwise" % w)
        if c["cell"] not in cells:
            raise ValueError("%s acts on %s, which is not one of the cells" % (w, c["cell"]))
        cmds.add(c["command"])
    for i, s in enumerate(inst["script"]):
        if s not in ("undo", "redo") and s not in cmds:
            raise ValueError("Script, entry %d: %s is not undo, redo or one of the commands" % (i + 1, s))


def _check_states(inst, fixed):
    states, events, seen = set(inst["states"]), set(inst["events"]), {}
    for i, t in enumerate(inst["transitions"]):
        w = "Transitions, record %d: " % (i + 1)
        for s in (t["state"], t["next"]):
            if s not in states:
                raise ValueError(w + "%s is not one of the states" % s)
        if t["event"] not in events:
            raise ValueError(w + "%s is not one of the events" % t["event"])
        k = (t["state"], t["event"])
        if k in seen:
            raise ValueError(w + "%s already has a transition on %s (record %d)" % (t["state"], t["event"], seen[k]))
        seen[k] = i + 1
    for i, e in enumerate(inst["input"]):
        if e not in events:
            raise ValueError("Input, entry %d: %s is not one of the events" % (i + 1, e))


def _check_access(inst, fixed):
    subj = {s["subject"] for s in inst["subjects"]}
    for i, q in enumerate(inst["requests"]):
        if q["subject"] not in subj:
            raise ValueError("Requests, record %d: %s is not one of the subjects" % (i + 1, q["subject"]))
    for i, r in enumerate(inst["rights"]):
        w, seen = "Rights, record %d: %s" % (i + 1, r["client"]), set()
        for s in r["rest"]:
            if s not in subj:
                raise ValueError("%s may use %s, which is not one of the subjects" % (w, s))
            if s in seen:
                raise ValueError("%s names %s twice" % (w, s))
            seen.add(s)


# ---------------------------------------------------------------------------
# Python: the spec dicts (kit-contract.md section 2)
# ---------------------------------------------------------------------------

_N = ea.NAME
_P = ea.PARENT          # a name, or - (none); a list of these may repeat a name
_SIGNED = ea.whole(-ea.LIMIT, ea.LIMIT)


def _names(what, lo, hi, things, each=None):
    """A list box; with each=_P a name may repeat (eakit refuses repeats only in a list of plain names)."""
    return dict(what=what, control="text", kind="list", lo=lo, hi=hi, things=things, each=dict(each or _N))


ROUTE = {
    "prefix": "grt", "fn": "grtCompute", "title": "Requests in motion", "js": GRT_JS,
    "views": {
        "chain": {
            "fields": [("handlers", vrec("Handlers in chain order (handler, then the topics it takes; all for every "
                                         "topic, - for none)", [("handler", _N)], _P, "topic", 1, 12, unique=True,
                                         rows=4, hi=12), None),
                       ("requests", _names("Requests, in the order sent (their topics)", 1, 60, "requests", _P),
                        None)],
            "tiles": [("Requests", "grtRequests"), ("Handled", "grtHandled"), ("Times passed on, in all", "grtHops"),
                      ("Unhandled (position)", "grtUnhandled"), ("Requests each handler takes", "grtPer"),
                      ("The busiest handler", "grtBusiest")],
            "check": _check_chain, "subtitle": "which handler takes each request, and how far it travels",
            "rules": "Every request goes to the head of the chain, and each handler in turn either takes it, if its "
                     "topic is one the handler lists (a handler listing all takes every request, one listing - takes "
                     "none), or passes it to the next. A request taken by the k-th handler is passed on k − 1 times; "
                     "one no handler takes is passed along the whole chain, n − 1 times for n handlers, and falls "
                     "off the end. Unhandled requests are listed in the order sent, with their position. The busiest "
                     "handler takes the most requests; a tie goes to the one first in the chain, and the status line "
                     "names the others.",
            "js": GRT_VIEW_JS["chain"],
        },
        "wrap": {
            "fields": [("core", ea.rec("The component (name, base value: a number, or a word)",
                                       [("component", _N), ("value", _N)], rows=1, hi=1), None),
                       ("layers", ea.rec("Decorators, innermost first (decorator, op add, times or then, amount)",
                                         [("decorator", _N), ("op", ea.word("add", "times", "then")),
                                          ("amount", _N)], unique=True, rows=3, hi=8), None),
                       ("order", _names("Another order to compare, innermost first (optional; empty is the reverse)",
                                        0, 8, "decorators"), "")],
            "tiles": [("Decorators", "grtLayers"), ("Call order", "grtCalls"), ("Result", "grtResult"),
                      ("Result in the other order", "grtOther"), ("Does the order change it?", "grtMatters"),
                      ("Classes, one subclass per combination", "grtSubclass"),
                      ("Classes with Decorator", "grtDecorator"), ("Classes one more option adds", "grtAddOne")],
            "check": _check_wrap, "subtitle": "a component in a stack of decorators",
            "rules": "A call enters the outermost decorator first and is passed inward to the component; the value "
                     "comes back out through the decorators innermost first, each applying its op: add adds its "
                     "amount, times multiplies by it (exact), then appends its word. A number takes add and times, a "
                     "word takes only then. The other order is the one given, or else the reverse. Classes are "
                     "counted for n options that may each be on or off: one subclass per combination is the "
                     "component plus one class for every non-empty set of options, 2ⁿ in all; Decorator is the "
                     "component interface, the concrete component, the abstract decorator and one class per "
                     "option, n + 3. One more option doubles the first (+2ⁿ) and adds 1 to the second. The "
                     "combination count ignores order and repetition, which decorators can also vary.",
            "js": GRT_VIEW_JS["wrap"],
        },
        "template": {
            "fields": [("steps", ea.rec("Steps of the template method, in order (step, kind fixed, primitive or "
                                        "hook)", [("step", _N), ("kind", ea.word("fixed", "primitive", "hook"))],
                                        unique=True, rows=3, hi=12), None),
                       ("subclasses", vrec("Subclasses (subclass, then the steps it overrides; - for none)",
                                           [("subclass", _N)], _P, "step", 1, 12, unique=True, rows=3, hi=8), None)],
            "tiles": [("Steps", "grtSteps"), ("Steps each subclass writes", "grtOwn"),
                      ("Subclasses left abstract", "grtAbstract"), ("Hooks each subclass overrides", "grtHooks"),
                      ("Steps written once in the base", "grtBase"),
                      ("Step bodies, the algorithm written whole in each subclass", "grtWhole"),
                      ("Step bodies with the template", "grtWith")],
            "check": _check_template, "subtitle": "the steps a template method runs for each subclass",
            "rules": "The base class's template method runs the steps in order for every subclass. A fixed step is "
                     "the base class's own and is never overridden; a primitive operation is abstract in the base "
                     "and each subclass must supply it, and a subclass that lacks one is left abstract (it cannot be "
                     "made), its missing steps named; a hook has a default in the base that a subclass may override. "
                     "Step bodies count the code written for steps: with every subclass writing the algorithm whole, "
                     "steps × subclasses; with the template, the fixed steps and hook defaults once in the base plus "
                     "each subclass's overrides.",
            "js": GRT_VIEW_JS["template"],
        },
    },
}

NOTIFY = {
    "prefix": "gno", "fn": "gnoCompute", "title": "Observers and their updates", "js": GNO_JS,
    "views": {
        "observer": {
            "fields": [("subjects", _names("Subjects", 1, 12, "subjects"), None),
                       ("observers", vrec("Observers (observer, then the subjects it observes)", [("observer", _N)],
                                          _N, "subject", 1, 12, unique=True, rows=3, hi=20), None),
                       ("operations", vrec("Operations (operation, then the subjects it changes, in order)",
                                           [("operation", _N)], _N, "subject", 1, 12, unique=True, rows=3, hi=20),
                        None),
                       ("scheme", ea.choice("Updates sent", "direct", "managed"), "direct")],
            "tiles": [("Changes", "gnoChanges"), ("Updates sent", "gnoSent"), ("Under the other scheme", "gnoOther"),
                      ("Redundant updates a change manager saves", "gnoRedundant"),
                      ("Updates each observer receives", "gnoPer"), ("Observers never notified", "gnoNever"),
                      ("Subjects no one observes", "gnoUnobserved")],
            "check": _check_observer, "subtitle": "the updates a change sends, directly and through a change manager",
            "rules": "An operation may change several subjects, and the same subject more than once; each is a "
                     "change. Sent directly, each change notifies every observer of its subject, so an observer of "
                     "two subjects that one operation changes is updated twice. Through a change manager, each "
                     "observer is updated once for each operation that changed any subject it observes. Redundant "
                     "updates are direct minus managed, printed under either scheme. Observers and subjects are "
                     "listed in the order given.",
            "js": GNO_VIEW_JS["observer"],
        },
    },
}

HISTORY = {
    "prefix": "ghi", "fn": "ghiCompute", "title": "Commands, undo and redo", "js": GHI_JS,
    "views": {
        "undo": {
            "fields": [("state", ea.rec("The state (cell, whole value)", [("cell", _N), ("value", _SIGNED)],
                                        unique=True, rows=2, hi=12), None),
                       ("commands", ea.rec("Commands (command, op set or add, cell, whole amount)",
                                           [("command", _N), ("op", ea.word("set", "add")), ("cell", _N),
                                            ("amount", _SIGNED)], unique=True, rows=3, hi=20), None),
                       ("script", _names("Script: command names, undo and redo, in order", 1, 60, "steps", _P),
                        None),
                       ("scheme", ea.choice("The history stores", "inverse", "snapshot"), "inverse")],
            "tiles": [("Final state", "ghiFinal"), ("Undo stack, bottom to top", "ghiUndo"),
                      ("Redo stack, bottom to top", "ghiRedo"), ("Refused: nothing to undo or redo", "ghiRefused"),
                      ("Redo entries a new command discarded", "ghiDiscarded"),
                      ("Values the history holds at the end", "ghiStored"), ("Under the other scheme", "ghiOther")],
            "check": _check_undo, "subtitle": "the undo and redo stacks after a sequence of commands",
            "rules": "A command name in the script runs it: set puts its amount in the cell, add adds it. Running a "
                     "command pushes it on the undo stack and empties the redo stack, whose entries are discarded. "
                     "Undo pops the undo stack, restores the state before that command and pushes it on the redo "
                     "stack; redo pops the redo stack, runs the command again and pushes it back. An undo or redo "
                     "with its stack empty does nothing and is counted. Stored values count what the history holds "
                     "at the end, one entry per command on either stack: as inverse operations, one old value per "
                     "set (an add is undone by subtracting its amount, which the command already holds); as "
                     "snapshots, every cell of the state per entry. The states are the same under both.",
            "js": GHI_VIEW_JS["undo"],
        },
    },
}

MACHINE = {
    "prefix": "gsm", "fn": "gsmCompute", "title": "A state machine", "js": GSM_JS,
    "views": {
        "states": {
            "fields": [("states", _names("States (the first is the start)", 1, 12, "states"), None),
                       ("events", _names("Events", 1, 12, "events"), None),
                       ("transitions", ea.rec("Transitions (state, event, next state)",
                                              [("state", _N), ("event", _N), ("next", _N)], rows=4), None),
                       ("input", _names("Input: events in order", 1, 60, "events", _P), None)],
            "tiles": [("Final state", "gsmFinal"), ("Events ignored (position)", "gsmIgnored"),
                      ("Transitions defined", "gsmDefined"), ("Branches in one conditional", "gsmBranches"),
                      ("Classes with State", "gsmClasses"), ("The largest state class", "gsmLargest"),
                      ("States never entered", "gsmNever")],
            "check": _check_states, "subtitle": "a trace over events, and one conditional against the classes of State",
            "rules": "The machine starts in the first state. An event with a transition from the current state moves "
                     "it to the next state; an event with none is ignored and the state stays. A state and an event "
                     "have at most one transition. One conditional on the state and the event needs one branch per "
                     "transition plus one default (ignore) branch per state: transitions + states, all in one "
                     "method. With State it is one class per state, the context and the abstract state: states + 2, "
                     "each state class handling only its own transitions (the abstract state ignores every event by "
                     "default); the largest is the state with the most transitions, a tie going to the first given.",
            "js": GSM_VIEW_JS["states"],
        },
    },
}

SHARE = {
    "prefix": "gsh", "fn": "gshCompute", "title": "Flyweights and storage", "js": GSH_JS,
    "views": {
        "flyweight": {
            "fields": [("objects", ea.rec("Objects by intrinsic state (state, how many objects have it)",
                                          [("key", _N), ("count", ea.whole(1, 1000000))], unique=True, rows=3),
                        None),
                       ("intrinsic", ea.field("Intrinsic bytes per object", ea.whole(1, 1000000)), None),
                       ("extrinsic", ea.field("Extrinsic bytes per object", ea.whole(0, 1000000)), None),
                       ("stored", ea.choice("Extrinsic state stored with each object", "yes", "no"), "yes"),
                       ("ref", ea.field("Bytes for a reference to a flyweight (0 to leave out)", ea.whole(0, 64)), 0)],
            "tiles": [("Objects", "gshObjects"), ("Flyweights", "gshFlyweights"),
                      ("Bytes without sharing", "gshWithout"), ("Bytes with flyweights", "gshWith"),
                      ("Bytes saved", "gshSaved"), ("Share saved", "gshShare"),
                      ("Most objects on one flyweight", "gshLargest"), ("Fewest objects on one flyweight", "gshSmallest")],
            "check": None, "subtitle": "storage without sharing and with one flyweight per intrinsic state",
            "rules": "Objects with the same intrinsic state share one flyweight. Without sharing every object holds "
                     "its intrinsic and its extrinsic state: objects × (intrinsic + extrinsic). With sharing the "
                     "intrinsic state is held once per flyweight, flyweights × intrinsic, plus, for every object, its "
                     "extrinsic state if it is stored (none if it is computed) and the reference to its flyweight "
                     "(0 unless given). Saved is the difference, negative when sharing costs more, and the share "
                     "saved is saved over unshared, exact. Most and fewest go to the first given on a tie.",
            "js": GSH_VIEW_JS["flyweight"],
        },
    },
}

PROXY = {
    "prefix": "gpx", "fn": "gpxCompute", "title": "Creating costly subjects", "js": GPX_JS,
    "views": {
        "access": {
            "fields": [("subjects", ea.rec("Subjects (subject, whole cost to create)",
                                           [("subject", _N), ("cost", ea.whole(0, ea.LIMIT))], unique=True, rows=2,
                                           hi=20), None),
                       ("requests", ea.rec("Requests in order (client, subject)", [("client", _N), ("subject", _N)],
                                           rows=3), None),
                       ("scheme", ea.choice("Creation", "eager", "lazy", "fresh"), "lazy"),
                       ("rights", vrec("Rights (client, then the subjects it may use; empty for no protection)",
                                       [("client", _N)], _N, "subject", 1, 20, unique=True, rows=2, lo=0, hi=20), "")],
            "tiles": [("Requests", "gpxRequests"), ("Refused by the protection proxy", "gpxRefused"),
                      ("Instances created", "gpxCreations"), ("Cost at the start", "gpxStart"),
                      ("Cost in all", "gpxTotal"), ("Subjects never requested", "gpxNever"),
                      ("Instances alive at the end", "gpxAlive"), ("The first request's cost", "gpxFirst"),
                      ("Cost in all, each scheme", "gpxCompare")],
            "check": _check_access, "subtitle": "objects created and cost spent, eagerly, lazily behind a proxy, or afresh",
            "rules": "Eager creates every subject at the start; lazy (a virtual proxy, or a singleton made on first "
                     "use) creates a subject on its first request and reuses it; fresh creates a new instance on "
                     "every request. Each creation costs the subject's cost. With rights given, a protection proxy "
                     "refuses any request whose client is not listed or whose subject is not among the client's; a "
                     "refused request creates nothing and costs nothing, and its subject does not count as "
                     "requested. Nothing is freed, so every instance created is alive at the end. The first "
                     "request's cost is what the first request served pays (0 under eager, whose cost is paid at "
                     "the start).",
            "js": GPX_VIEW_JS["access"],
        },
    },
}

SPECS = {"route": ROUTE, "notify": NOTIFY, "history": HISTORY, "machine": MACHINE, "share": SHARE, "proxy": PROXY}

MODES = {
    "route": lambda cfg: mode_lab(cfg, "route", ROUTE),
    "notify": lambda cfg: mode_lab(cfg, "notify", NOTIFY),
    "history": lambda cfg: mode_lab(cfg, "history", HISTORY),
    "machine": lambda cfg: mode_lab(cfg, "machine", MACHINE),
    "share": lambda cfg: mode_lab(cfg, "share", SHARE),
    "proxy": lambda cfg: mode_lab(cfg, "proxy", PROXY),
}

__all__ = ["MODES", "SPECS"]

# ---------------------------------------------------------------------------
# Worked cfgs, one per view: every preset's expect was counted by hand and read
# off a rendered page (docs/design-patterns/kit-report.md, Family B). They are
# examples for authors and the build check's fixture; no page ships them.
# ---------------------------------------------------------------------------

SAMPLES = {
    ("route", "chain"): {"mode": "route", "view": "chain", "presets": [
        {"id": "bike-share", "label": "Bike-share support: a logger, a bot, an agent, a supervisor",
         "handlers": "logger, -; bot, unlock, balance; agent, unlock, refund, damage; supervisor, refund, ban",
         "requests": "unlock balance refund ban theft unlock damage theft",
         "expect": {"grtRequests": "8", "grtHandled": "6 of 8", "grtHops": "16",
                    "grtUnhandled": "2: theft (5), theft (8)", "grtPer": "logger 0, bot 3, agent 2, supervisor 1",
                    "grtBusiest": "bot, 3 requests"}},
        {"id": "box-office", "label": "A theatre box office whose manager takes everything",
         "handlers": "kiosk, collect; clerk, collect, exchange, refund; manager, all",
         "requests": "refund collect comp exchange collect",
         "expect": {"grtHandled": "5 of 5", "grtHops": "4", "grtUnhandled": "0: none",
                    "grtPer": "kiosk 2, clerk 2, manager 1", "grtBusiest": "kiosk, 2 requests"}}]},
    ("route", "wrap"): {"mode": "route", "view": "wrap", "presets": [
        {"id": "coffee", "label": "A coffee order: milk, a double shot, syrup",
         "core": "flatwhite, 2.50", "layers": "milk, add, 0.40; double, times, 2; syrup, add, 0.35",
         "expect": {"grtLayers": "3", "grtCalls": "in: syrup, double, milk; core: flatwhite; out: milk, double, syrup",
                    "grtResult": "6.15", "grtOther": "6.1", "grtMatters": "yes",
                    "grtSubclass": "8 (the component + 7 combinations)",
                    "grtDecorator": "6 (interface, component, abstract decorator + 3)",
                    "grtAddOne": "subclassing +8, Decorator +1"}},
        {"id": "ticket", "label": "A ticket's printed line, in another order",
         "core": "ticket, Row-F", "layers": "date, then, Sat-14; seat, then, F12; vip, then, VIP",
         "order": "vip date seat",
         "expect": {"grtResult": "Row-F Sat-14 F12 VIP", "grtOther": "Row-F VIP Sat-14 F12", "grtMatters": "yes"}},
        {"id": "parcel", "label": "A parcel's price, where order does not matter",
         "core": "parcel, 4", "layers": "insured, add, 1.5; tracked, add, 0.75",
         "expect": {"grtResult": "6.25", "grtOther": "6.25", "grtMatters": "no",
                    "grtSubclass": "4 (the component + 3 combinations)",
                    "grtDecorator": "5 (interface, component, abstract decorator + 2)",
                    "grtAddOne": "subclassing +4, Decorator +1"}}]},
    ("route", "template"): {"mode": "route", "view": "template", "presets": [
        {"id": "bakery", "label": "A bakery's loaf, three breads",
         "steps": "weigh, fixed; mix, primitive; proof, hook; bake, primitive; cool, fixed; glaze, hook",
         "subclasses": "Sourdough, mix, bake, proof; Brioche, mix, bake, glaze; Flatbread, mix, proof",
         "expect": {"grtSteps": "6: 2 fixed, 2 primitive, 2 hooks", "grtOwn": "Sourdough 3, Brioche 3, Flatbread 2",
                    "grtAbstract": "1: Flatbread (lacks bake)", "grtHooks": "Sourdough 1, Brioche 1, Flatbread 1",
                    "grtBase": "4", "grtWhole": "18", "grtWith": "12"}},
        {"id": "quiz", "label": "A quiz app's round, two modes",
         "steps": "load, fixed; ask, primitive; score, primitive; report, fixed; badge, hook",
         "subclasses": "Timed, ask, score; Practice, ask, score, badge",
         "expect": {"grtSteps": "5: 2 fixed, 2 primitive, 1 hook", "grtOwn": "Timed 2, Practice 3",
                    "grtAbstract": "0: none", "grtHooks": "Timed 0, Practice 1", "grtBase": "3",
                    "grtWhole": "10", "grtWith": "8"}}]},
    ("notify", "observer"): {"mode": "notify", "view": "observer", "presets": [
        {"id": "thermostat", "label": "A thermostat: three readings, four observers",
         "subjects": "temp humidity mode",
         "observers": "display, temp, humidity, mode; logger, temp, humidity; fan, temp; app, mode",
         "operations": "reading, temp, humidity; storm, temp, humidity, temp; switch, mode; calibrate, humidity",
         "expect": {"gnoChanges": "7", "gnoSent": "17", "gnoOther": "managed: 10", "gnoRedundant": "7",
                    "gnoPer": "display 7, logger 6, fan 3, app 1", "gnoNever": "0: none", "gnoUnobserved": "0: none"}},
        {"id": "audio-guide", "label": "A museum audio guide, through a change manager",
         "subjects": "hall gallery cafe garden",
         "observers": "guide, hall, gallery; map, hall, gallery; ticket, cafe",
         "operations": "open, hall, gallery; tour, gallery, gallery; close, hall; rain, garden", "scheme": "managed",
         "expect": {"gnoChanges": "6", "gnoSent": "6", "gnoOther": "direct: 10", "gnoRedundant": "4",
                    "gnoPer": "guide 3, map 3, ticket 0", "gnoNever": "1: ticket", "gnoUnobserved": "1: garden"}}]},
    ("history", "undo"): {"mode": "history", "view": "undo", "presets": [
        {"id": "dock", "label": "A bike-share dock: rentals, a price, undo and redo",
         "state": "bikes, 10; fee, 2",
         "commands": "rent, add, bikes, -1; ret, add, bikes, 1; price, set, fee, 3; free, set, fee, 0",
         "script": "rent rent price undo undo redo free undo undo undo undo",
         "expect": {"ghiFinal": "bikes 10, fee 2", "ghiUndo": "0: none", "ghiRedo": "3: free, rent, rent",
                    "ghiRefused": "undo 1, redo 0", "ghiDiscarded": "1", "ghiStored": "1", "ghiOther": "snapshot: 6"}},
        {"id": "recipe", "label": "A recipe being scaled, kept as snapshots",
         "state": "flour, 500; sugar, 100; eggs, 2",
         "commands": "double, set, flour, 1000; sweet, add, sugar, 50; egg, add, eggs, 1; plain, set, sugar, 0",
         "script": "double sweet egg undo plain redo undo", "scheme": "snapshot",
         "expect": {"ghiFinal": "flour 1,000, sugar 150, eggs 2", "ghiUndo": "2: double, sweet",
                    "ghiRedo": "1: plain", "ghiRefused": "undo 0, redo 1", "ghiDiscarded": "1", "ghiStored": "9",
                    "ghiOther": "inverse: 2"}}]},
    ("machine", "states"): {"mode": "machine", "view": "states", "presets": [
        {"id": "locker", "label": "A parcel locker over eight events",
         "states": "idle reserved loaded emptied jammed", "events": "reserve load collect cancel timeout jam",
         "transitions": "idle, reserve, reserved; reserved, load, loaded; reserved, cancel, idle; "
                        "loaded, collect, emptied; loaded, timeout, reserved; emptied, reserve, reserved; "
                        "loaded, jam, jammed; jammed, cancel, idle",
         "input": "load reserve load timeout load collect cancel reserve",
         "expect": {"gsmFinal": "reserved", "gsmIgnored": "2: load at idle (1), cancel at emptied (7)",
                    "gsmDefined": "8", "gsmBranches": "13", "gsmClasses": "7", "gsmLargest": "loaded, 3 transitions",
                    "gsmNever": "1: jammed"}},
        {"id": "vending", "label": "A vending machine with two states",
         "states": "ready paid", "events": "coin push refund",
         "transitions": "ready, coin, paid; paid, push, ready; paid, refund, ready; paid, coin, paid",
         "input": "push coin coin push",
         "expect": {"gsmFinal": "ready", "gsmIgnored": "1: push at ready (1)", "gsmDefined": "4",
                    "gsmBranches": "6", "gsmClasses": "4", "gsmLargest": "paid, 3 transitions", "gsmNever": "0: none"}}]},
    ("share", "flyweight"): {"mode": "share", "view": "flyweight", "presets": [
        {"id": "map-tiles", "label": "A map tile viewer: 8,000 tiles, four bitmaps",
         "objects": "grass, 4000; water, 2500; road, 600; forest, 900", "intrinsic": 4096, "extrinsic": 8,
         "expect": {"gshObjects": "8,000", "gshFlyweights": "4", "gshWithout": "32,832,000", "gshWith": "80,384",
                    "gshSaved": "32,751,616", "gshShare": "63,968/64,125 ≈ 99.8%",
                    "gshLargest": "grass, 4,000 objects", "gshSmallest": "road, 600 objects"}},
        {"id": "seats", "label": "Theatre seats whose position is computed, with references",
         "objects": "standard, 40; premium, 12; box, 4", "intrinsic": 64, "extrinsic": 6, "stored": "no", "ref": 2,
         "expect": {"gshObjects": "56", "gshFlyweights": "3", "gshWithout": "3,920", "gshWith": "304",
                    "gshSaved": "3,616", "gshShare": "226/245 ≈ 92.2%", "gshLargest": "standard, 40 objects",
                    "gshSmallest": "box, 4 objects"}}]},
    ("proxy", "access"): {"mode": "proxy", "view": "access", "presets": [
        {"id": "audio-tracks", "label": "Audio-guide tracks loaded lazily, behind a protection proxy",
         "subjects": "intro, 40; egypt, 120; rome, 90; vault, 200",
         "requests": "ana, intro; ben, egypt; ana, egypt; guest, vault; ben, intro; cara, egypt",
         "rights": "ana, intro, egypt, rome; ben, intro, egypt; cara, egypt",
         "expect": {"gpxRequests": "6", "gpxRefused": "1: guest → vault (4)", "gpxCreations": "2", "gpxStart": "0",
                    "gpxTotal": "160", "gpxNever": "2: rome, vault", "gpxAlive": "2", "gpxFirst": "40",
                    "gpxCompare": "eager 450, lazy 160, fresh 440"}},
        {"id": "catalogue", "label": "A library catalogue connection made afresh on every request",
         "subjects": "catalogue, 30", "requests": "desk, catalogue; kiosk, catalogue; app, catalogue; desk, catalogue",
         "scheme": "fresh",
         "expect": {"gpxRefused": "0: none", "gpxCreations": "4", "gpxStart": "0", "gpxTotal": "120",
                    "gpxNever": "0: none", "gpxAlive": "4", "gpxFirst": "30",
                    "gpxCompare": "eager 30, lazy 30, fresh 120"}}]},
}
