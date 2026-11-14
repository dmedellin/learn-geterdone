"""levkit_b -- family B of the Leviathan kit: assemblies, succession, taxes, law, scripture.

Specified in docs/leviathan/PLAN.md section D.1 (family B); the seam with
family A (levkit.py: the entry point and modes reckon, deliberate, worth,
equality, covenant) is docs/leviathan/kit-contract.md; the report an author
configures a lesson from is the "Family B" section of
docs/leviathan/kit-report.md. Five modes:

  assembly    (las)  voices, ties        Chapters 16, 19, 22, 25
  succession  (lsu)  heir                Chapter 19
  tax         (ltx)  impose, shares      Chapters 24, 30
  law         (llw)  silence, deter      Chapters 21, 27, 28
  canon       (lcn)  date, benefit       Chapters 33, 47

Each mode has one base block <PREFIX>_JS defining the pure function
<prefix>Compute(view, inst, opts), which scripts/mathcheck.js calls (section
"levkit (Leviathan), family B"), and one block per view. A page ships the
base block and its own view's block only.

THE INSTANCES ARE THE LESSON'S. No member, person, law, book or doctrine is
a constant here: every one arrives in a preset. Nothing typed is evaluated
as script. Nothing here decides whether Hobbes is right: every status line
ends with the kit's caution (lvkStatus).

EXACTNESS. Every figure is a count, a list or an exact BigInt rational. The
chance of an even split is C(n, n/2) / 2^n with both parts BigInt; a share is
printed as its exact fraction, never rounded.

IDS. Every JS function and variable and every element id begins with its
mode's prefix (las, lsu, ltx, llw, lcn); no name here begins lvk/LVK_, and
none begins LAST.
"""

from fractions import Fraction

from . import eakit_core as ea
from .levkit import mode_lab, lrec, llist, rat, NAMES, NAMES_DASH

_N = ea.NAME

# ---------------------------------------------------------------------------
# assembly (las): an assembly's voices, and how often it is mute
# ---------------------------------------------------------------------------

LAS_JS = r"""
  var LAS_VIEW = {};
  function lasCompute(view, inst, opts) { return eaRun(LAS_VIEW[view], inst, opts); }
  /* C(n, k) exactly, as a BigInt. */
  function lasChoose(n, k) {
    var r = 1n, i;
    if (k < 0 || k > n) return 0n;
    for (i = 1; i <= k; i += 1) r = r * BigInt(n - k + i) / BigInt(i);
    return r;
  }
  /* The chance an assembly of n splits evenly, each member as likely to say
     yes as no, independently: C(n, n/2) / 2^n, and 0 for an odd n. */
  function lasEven(n) { return n % 2 ? R0 : R(lasChoose(n, n / 2), 2n ** BigInt(n)); }
"""

LAS_VIEW_JS = {}

LAS_VIEW_JS["voices"] = r"""
  LAS_VIEW.voices = function (inst) {
    var M = inst.members, n = M.length, rule = inst.rule, yes = [], no = [], ab = [];
    M.forEach(function (m) { (m.voice === 'yes' ? yes : m.voice === 'no' ? no : ab).push(m.member); });
    var y = yes.length, x = no.length, dec, need, verdict;
    if (y === x) {
      verdict = 'mute';
      dec = y === 0 ? 'mute: no voice is given (every member abstains)' : 'mute: ' + y + ' to ' + x + ', an even split of the voices';
    } else if (rule === 'greater') {
      verdict = y > x ? 'passes' : 'fails';
      dec = verdict + ': ' + y + ' to ' + x + ' by the greater number of voices given';
    } else {
      verdict = 2 * y > n ? 'passes' : 'fails';
      dec = verdict + ': ' + y + ' of ' + eaPlural(n, 'member', 'members') + ' say yes, ' + (verdict === 'passes' ? 'more than half' : 'not more than half');
    }
    need = rule === 'greater' ? eaPlural(x + 1, 'yes voice', 'yes voices') + ' (more than the ' + x + ' no)'
      : eaPlural(Math.floor(n / 2) + 1, 'yes voice', 'yes voices') + ' (more than half of ' + eaPlural(n, 'member', 'members') + ')';
    var liable, excused, liableOn = inst.liable === 'yes';
    if (!liableOn) { liable = 'not shown (liable is no)'; excused = 'not shown (liable is no)'; }
    else if (verdict === 'passes') { liable = eaCount(yes); excused = eaCount(M.filter(function (m) { return m.voice !== 'yes'; }).map(function (m) { return m.member; })); }
    else { liable = 'none: no decree was made'; excused = 'everyone: no decree was made'; }
    var rows = M.map(function (m) {
      var row = [m.member, m.voice];
      if (liableOn) row.push(verdict !== 'passes' ? 'no decree' : m.voice === 'yes' ? 'answerable' : 'excused');
      return row;
    });
    var ruleText = rule === 'greater' ? 'the greater number of the voices given' : 'more than half of all the members';
    return {
      tiles: { lasYes: eaInt(y), lasNo: eaInt(x), lasAbstain: eaInt(ab.length), lasDecision: dec,
        lasMargin: eaSigned(y - x), lasNeeded: need, lasLiable: liable, lasExcused: excused },
      status: lvkStatus((verdict === 'mute' ? 'The assembly is mute: nothing is decreed' : 'The motion ' + verdict)
        + ' on the rule of ' + ruleText + (liableOn && verdict === 'passes' ? '; only those who voted for the decree are answerable for it' : '')),
      table: { caption: 'Each member\'s voice', head: liableOn ? ['member', 'voice', 'for the decree'] : ['member', 'voice'], rows: rows }
    };
  };
"""

LAS_VIEW_JS["ties"] = r"""
  LAS_VIEW.ties = function (inst) {
    var S = inst.sizes.map(function (r) { return Number(r.n); }), seen = {};
    S.forEach(function (n) { if (seen[n]) eaRefuse('Sizes: ' + n + ' is given twice'); seen[n] = true; });
    var ch = S.map(function (n) { return lasEven(n); });
    var even = S.filter(function (n) { return n % 2 === 0; }), odd = S.filter(function (n) { return n % 2 === 1; });
    function pick(better) {
      if (!even.length) return 'none: every size given is odd';
      var best = even[0];
      even.forEach(function (n) { if (better(Rcmp(lasEven(n), lasEven(best)))) best = n; });
      return best + ' members: ' + lvkPct(lasEven(best));
    }
    return {
      tiles: { lasChances: S.map(function (n, i) { return n + ': ' + lvkPct(ch[i]); }).join('; '),
        lasOdd: eaCount(odd.map(String)), lasMost: pick(function (c) { return c > 0; }), lasLeast: pick(function (c) { return c < 0; }) },
      status: lvkStatus('On the stated model (each member says yes or no with equal chance, independently: a model, not Hobbes\'s), '
        + 'an odd assembly is never mute; an even one is mute whenever the voices split evenly, and that grows rarer, but never impossible, as it grows. '
        + 'Hobbes\'s point is about the even ones'),
      table: { caption: 'Even splits among all the ways an assembly can vote',
        head: ['members', 'even splits C(n, n/2)', 'ways to vote 2^n', 'chance of a mute assembly'],
        rows: S.map(function (n, i) { return [String(n), n % 2 ? '0' : eaInt(lasChoose(n, n / 2)), eaInt(2n ** BigInt(n)), lvkPct(ch[i])]; }) }
    };
  };
"""

# ---------------------------------------------------------------------------
# succession (lsu): who succeeds a monarch
# ---------------------------------------------------------------------------

LSU_JS = r"""
  var LSU_VIEW = {};
  function lsuCompute(view, inst, opts) { return eaRun(LSU_VIEW[view], inst, opts); }
  /* The family as a tree: refuses an unknown or own parent, a loop, a birth
     order shared, a child born before its parent. */
  function lsuTree(P) {
    var by = {}, kids = {}, born = {};
    P.forEach(function (p) { by[p.person] = p; kids[p.person] = []; });
    P.forEach(function (p, i) {
      if (p.parent === '-') return;
      if (p.parent === p.person) eaRefuse('People, record ' + (i + 1) + ' (' + p.person + ') is named as their own parent');
      if (!by[p.parent]) eaRefuse('People, record ' + (i + 1) + ' (' + p.person + '): the parent ' + p.parent + ' is not one of the people');
      kids[p.parent].push(p.person);
    });
    P.forEach(function (p) {
      var walk = [], at = {}, x = p.person;
      while (x !== '-') {
        if (at[x] !== undefined) eaRefuse('People: ' + walk.slice(at[x]).join(', ') + ' are one another\'s ancestors in a loop');
        at[x] = walk.length; walk.push(x); x = by[x].parent;
      }
    });
    P.forEach(function (p, i) {
      var b = String(p.born.n);
      if (born[b] !== undefined) eaRefuse('People, record ' + (i + 1) + ' (' + p.person + ') is born ' + b + ', as ' + born[b] + ' is: born gives the order of birth, so no two people share it');
      born[b] = p.person;
    });
    P.forEach(function (p, i) {
      if (p.parent !== '-' && Rcmp(p.born, by[p.parent].born) <= 0) eaRefuse('People, record ' + (i + 1) + ' (' + p.person + ') is born ' + p.born.n + ', not after the parent ' + p.parent + ' (born ' + by[p.parent].born.n + ')');
    });
    return { by: by, kids: kids };
  }
  /* Male before female, then elder (smaller born) before younger. */
  function lsuCmp(a, b) {
    if (a.sex !== b.sex) return a.sex === 'm' ? -1 : 1;
    return Rcmp(a.born, b.born);
  }
"""

LSU_VIEW_JS = {}

LSU_VIEW_JS["heir"] = r"""
  LSU_VIEW.heir = function (inst) {
    var P = inst.people, T = lsuTree(P), by = T.by, kids = T.kids, mon = inst.monarch, named = inst.named;
    if (!by[mon]) eaRefuse('The monarch, ' + mon + ', is not one of the people');
    if (named !== '-') {
      if (!by[named]) eaRefuse('The successor named, ' + named + ', is not one of the people');
      if (named === mon) eaRefuse('The successor named, ' + named + ', is the monarch');
      if (by[named].alive !== 'yes') eaRefuse('The successor named, ' + named + ', is dead (alive is no), and the dead cannot succeed');
    }
    var info = {}, issue = [], desc = {};
    /* the monarch's issue, in order: each child (male before female, elder
       before younger) and then that child's own issue, a dead child's issue
       standing in its place before the next child */
    function down(x, g) {
      kids[x].map(function (c) { return by[c]; }).sort(lsuCmp).forEach(function (c) {
        desc[c.person] = true;
        info[c.person] = { issue: true, gen: g, lca: mon, steps: g };
        if (c.alive === 'yes') issue.push(c.person);
        down(c.person, g + 1);
      });
    }
    down(mon, 1);
    var up = [mon], upAt = {};
    while (by[up[up.length - 1]].parent !== '-') up.push(by[up[up.length - 1]].parent);
    up.forEach(function (x, k) { upAt[x] = k; });
    var others = [];
    P.forEach(function (p) {
      if (p.person === mon || desc[p.person]) return;
      var x = p.person, s = 0;
      while (x !== '-' && upAt[x] === undefined) { x = by[x].parent; s += 1; }
      if (x === '-') { info[p.person] = { blood: false }; return; }
      info[p.person] = { issue: false, lca: x, steps: s + upAt[x], down: s };
      if (p.alive === 'yes') others.push(p);
    });
    others.sort(function (a, b) { var d = info[a.person].steps - info[b.person].steps; return d !== 0 ? d : lsuCmp(a, b); });
    var presume = issue.concat(others.map(function (p) { return p.person; }));
    /* male-line custom: a male, every person between him and the common
       ancestor male, the common ancestor male (unless the monarch), and every
       person between the monarch and the common ancestor male */
    function between(from, to) { var out = [], x = by[from].parent; while (x !== to) { out.push(x); x = by[x].parent; } return out; }
    function maleLine(name) {
      var f = info[name], chain = [];
      if (by[name].sex !== 'm') return 'female';
      if (f.issue) chain = between(name, mon);
      else {
        if (f.lca !== name) chain = between(name, f.lca).concat([f.lca]);
        chain = chain.concat(between(mon, f.lca));
      }
      var fem = chain.filter(function (x) { return by[x].sex !== 'm'; });
      return fem.length ? 'through a female (' + fem[0] + ')' : '';
    }
    var custom = inst.custom === 'male-line', base = custom ? presume.filter(function (x) { return maleLine(x) === ''; }) : presume;
    var line = named !== '-' ? [named].concat(base.filter(function (x) { return x !== named; })) : base;
    var who = line.length ? line[0] : null, rule;
    function near(name) {
      var f = info[name];
      if (!f || f.blood === false) return 'not of the blood';
      if (f.issue) return 'issue, ' + eaPlural(f.gen, 'generation', 'generations') + ' down';
      if (f.lca === name) return eaPlural(f.steps, 'step', 'steps') + ' up (an ancestor)';
      return eaPlural(f.steps, 'step', 'steps') + ' through ' + f.lca;
    }
    if (named !== '-') rule = 'testament: named by express words';
    else if (!who) rule = 'none: no living person of the blood qualifies';
    else if (custom) rule = 'custom (male-line): the first male of the blood through males';
    else if (info[who].issue) rule = 'presumption: the monarch\'s own issue';
    else rule = 'presumption: no living issue, so the nearest in blood';
    var shown = line.slice(0, 6).map(function (x, i) { return (i + 1) + ' ' + x; }).join('; ');
    if (line.length > 6) shown += '; and ' + (line.length - 6) + ' more (the table lists all)';
    var rows = line.map(function (x, i) { var p = by[x]; return [String(i + 1), x, p.sex, String(p.born.n), near(x), x === named ? 'named by testament' : '']; });
    P.forEach(function (p) {
      if (p.person === mon || line.indexOf(p.person) >= 0) return;
      var why = p.alive !== 'yes' ? 'dead' : info[p.person].blood === false ? 'not of the blood' : 'not of the male line: ' + maleLine(p.person);
      rows.push(['', p.person, p.sex, String(p.born.n), near(p.person), why]);
    });
    var without = base.length ? base[0] : 'none';
    return {
      tiles: { lsuSuccessor: who || 'none', lsuRule: rule, lsuLine: line.length ? shown : 'none',
        lsuWithout: named === '-' ? without + ' (there is no testament)' : without,
        lsuPresumption: presume.length ? presume[0] : 'none', lsuIssue: eaCount(issue), lsuNear: who ? who + ': ' + near(who) : 'none' },
      status: lvkStatus((who ? who + ' succeeds ' + mon + ' by ' + rule.split(':')[0] : 'No one succeeds ' + mon + ': no living person of the blood qualifies')
        + (named !== '-' ? '; without the testament it would be ' + without : '')
        + '. The order among the issue (male before female, elder before younger, a dead child\'s issue in its place) is the kit\'s reading of Chapter 19, not Hobbes\'s words'),
      table: { caption: 'The line of succession, then everyone passed over', head: ['place', 'person', 'sex', 'born', 'nearness', 'note'], rows: rows }
    };
  };
"""

# ---------------------------------------------------------------------------
# tax (ltx): an equal imposition on riches or on consumption; shares
# ---------------------------------------------------------------------------

LTX_JS = r"""
  var LTX_VIEW = {};
  function ltxCompute(view, inst, opts) { return eaRun(LTX_VIEW[view], inst, opts); }
  function ltxSigned(r) { return (r.n > 0n ? '+' : '') + eaNum(r); }
  /* A share, never rounded: a whole number, or the exact fraction and, when it
     ends within 6 places, its exact decimal. */
  function ltxExact(r) {
    if (Rint(r)) return eaInt(r.n);
    for (var p = 1; p <= 6; p += 1) if (eaExactAt(r, p)) return eaFrac(r) + ' = ' + eaFixed(r, p);
    return eaFrac(r);
  }
"""

LTX_VIEW_JS = {}

LTX_VIEW_JS["impose"] = r"""
  LTX_VIEW.impose = function (inst) {
    var P = inst.persons, rev = inst.revenue;
    var TR = eaSum(P.map(function (p) { return p.riches; })), TC = eaSum(P.map(function (p) { return p.consumption; }));
    if (Rzero(TR)) eaRefuse('Persons: every person\'s riches are 0, so no rate on riches can raise the revenue');
    if (Rzero(TC)) eaRefuse('Persons: every person\'s consumption is 0, so no rate on consumption can raise the revenue');
    var rr = Rdiv(rev, TR), rc = Rdiv(rev, TC), more = [];
    var t = P.map(function (p) {
      var a = Rmul(rr, p.riches), b = Rmul(rc, p.consumption);
      if (Rcmp(b, a) > 0) more.push(p.person);
      return { a: a, b: b, d: Rsub(b, a), sa: Rzero(p.consumption) ? null : Rdiv(a, p.consumption), sb: Rzero(p.consumption) ? null : Rdiv(b, p.consumption) };
    });
    function each(f) { return P.map(function (p, i) { return p.person + ' ' + f(t[i]); }).join('; '); }
    function share(r) { return r === null ? 'no consumption' : lvkPct(r); }
    return {
      tiles: { ltxRateRiches: lvkPct(rr), ltxRateConsumption: lvkPct(rc),
        ltxOnRiches: each(function (x) { return eaNum(x.a); }), ltxOnConsumption: each(function (x) { return eaNum(x.b); }),
        ltxDifference: each(function (x) { return ltxSigned(x.d); }), ltxMore: eaCount(more),
        ltxBurdenRiches: each(function (x) { return share(x.sa); }), ltxBurdenConsumption: each(function (x) { return share(x.sb); }) },
      status: lvkStatus('Both impositions raise ' + eaNum(rev) + ': on riches at ' + lvkPct(rr) + ' of ' + eaNum(TR) + ', on consumption at ' + lvkPct(rc) + ' of ' + eaNum(TC)
        + '. On consumption every person pays the same share of what they consume; on riches the share of what they consume differs'),
      table: { caption: 'Each person\'s tax under each imposition', head: ['person', 'riches', 'consumption', 'tax on riches', 'tax on consumption', 'difference', 'on riches, of consumption', 'on consumption, of consumption'],
        rows: P.map(function (p, i) { var x = t[i]; return [p.person, eaNum(p.riches), eaNum(p.consumption), eaNum(x.a), eaNum(x.b), ltxSigned(x.d), share(x.sa), share(x.sb)]; }) }
    };
  };
"""

LTX_VIEW_JS["shares"] = r"""
  LTX_VIEW.shares = function (inst) {
    var total = inst.total, P = inst.parties, S = inst.setaside;
    var f = eaSum(S.map(function (s) { return s.fraction; }));
    if (Rcmp(f, R1) > 0) eaRefuse('Set apart: the fractions add to ' + eaFrac(f) + ', more than the whole');
    var rem = Rmul(total, Rsub(R1, f)), W = eaSum(P.map(function (p) { return p.weight; }));
    var aside = S.map(function (s) { return Rmul(total, s.fraction); });
    var sh = P.map(function (p) { return Rdiv(Rmul(rem, p.weight), W); });
    var whole = {}, order = [];
    function add(name, r) { if (!whole[name]) { whole[name] = R0; order.push(name); } whole[name] = Radd(whole[name], r); }
    S.forEach(function (s, i) { add(s.party, aside[i]); });
    P.forEach(function (p, i) { add(p.party, sh[i]); });
    var sum = eaSum(order.map(function (x) { return whole[x]; }));
    var notWhole = P.filter(function (_p, i) { return !Rint(sh[i]); }).map(function (p) { return p.party; });
    return {
      tiles: { ltxSetAside: S.length ? S.map(function (s, i) { return s.party + ' ' + ltxExact(s.fraction) + ' of the total: ' + ltxExact(aside[i]); }).join('; ') : 'none set apart',
        ltxRemainder: ltxExact(rem), ltxWeight: ltxExact(W),
        ltxShares: P.map(function (p, i) { return p.party + ' ' + ltxExact(sh[i]); }).join('; '), ltxNotWhole: eaCount(notWhole),
        ltxSum: ltxExact(sum) + (Requ(sum, total) ? ', the whole total' : ', not the total ' + ltxExact(total)) },
      status: lvkStatus(ltxExact(total) + ' is divided: ' + (S.length ? ltxExact(Rsub(total, rem)) + ' set apart first, then ' : '')
        + 'the remainder ' + ltxExact(rem) + ' by weight, ' + ltxExact(W) + ' in all. Every share is exact; none is rounded'),
      table: { caption: 'Each party\'s portion', head: ['party', 'set apart', 'weight', 'share of the remainder', 'portion'],
        rows: order.map(function (x) {
          var si = -1, pi = -1;
          S.forEach(function (s, i) { if (s.party === x) si = i; });
          P.forEach(function (p, i) { if (p.party === x) pi = i; });
          return [x, si >= 0 ? ltxExact(aside[si]) : '', pi >= 0 ? ltxExact(P[pi].weight) : '', pi >= 0 ? ltxExact(sh[pi]) : '', ltxExact(whole[x])];
        }) }
    };
  };
"""

# ---------------------------------------------------------------------------
# law (llw): the silence of the law; punishment against the benefit of a crime
# ---------------------------------------------------------------------------

LLW_JS = r"""
  var LLW_VIEW = {};
  function llwCompute(view, inst, opts) { return eaRun(LLW_VIEW[view], inst, opts); }
"""

LLW_VIEW_JS = {}

LLW_VIEW_JS["silence"] = r"""
  LLW_VIEW.silence = function (inst) {
    var A = inst.actions, L = inst.laws, I = inst.inalienable, known = {}, cmd = {}, fbd = {}, keep = {};
    A.forEach(function (a) { known[a] = true; cmd[a] = []; fbd[a] = []; });
    L.forEach(function (l, i) {
      l.commands.forEach(function (a) { if (!known[a]) eaRefuse('Laws, record ' + (i + 1) + ' (' + l.law + '): it commands ' + a + ', which is not one of the actions'); cmd[a].push(l.law); });
      l.forbids.forEach(function (a) { if (!known[a]) eaRefuse('Laws, record ' + (i + 1) + ' (' + l.law + '): it forbids ' + a + ', which is not one of the actions'); fbd[a].push(l.law); });
    });
    I.forEach(function (x, i) {
      if (!known[x.action]) eaRefuse('Inalienable, record ' + (i + 1) + ': ' + x.action + ' is not one of the actions');
      keep[x.action] = x.reason.join(' ');
    });
    var C = A.filter(function (a) { return cmd[a].length; }), F = A.filter(function (a) { return fbd[a].length; });
    var both = A.filter(function (a) { return cmd[a].length && fbd[a].length; }), free = A.filter(function (a) { return !cmd[a].length && !fbd[a].length; });
    var refuse = C.filter(function (a) { return keep[a] !== undefined; });
    function state(a) { return cmd[a].length && fbd[a].length ? 'both commanded and forbidden' : cmd[a].length ? 'commanded' : fbd[a].length ? 'forbidden' : 'free'; }
    return {
      tiles: { llwCommanded: eaCount(C), llwForbidden: eaCount(F), llwFree: eaCount(free),
        llwBoth: both.length ? eaCount(both.map(function (a) { return a + ' (commanded by ' + cmd[a].join(' and ') + ', forbidden by ' + fbd[a].join(' and ') + ')'; })) : '0: none',
        llwRefusable: !I.length ? 'no inalienable liberty is stated' : eaCount(refuse.map(function (a) { return a + ' (' + keep[a] + ')'; })),
        llwShareFree: free.length + ' of ' + A.length + ': ' + lvkPct(R(BigInt(free.length), BigInt(A.length))) },
      status: lvkStatus(eaPlural(free.length, 'action is', 'actions are') + ' left free in the silence of the law, of ' + A.length
        + (both.length ? '; ' + eaPlural(both.length, 'action is', 'actions are') + ' both commanded and forbidden, a contradiction in the laws' : '')
        + (refuse.length ? '; ' + eaPlural(refuse.length, 'command', 'commands') + ' a subject may still refuse' : '')),
      table: { caption: 'Each action under the laws', head: ['action', 'commanded by', 'forbidden by', 'so it is', 'liberty kept'],
        rows: A.map(function (a) { return [a, cmd[a].join(', '), fbd[a].join(', '), state(a), keep[a] === undefined ? '' : keep[a]]; }) }
    };
  };
"""

LLW_VIEW_JS["deter"] = r"""
  LLW_VIEW.deter = function (inst) {
    var g = inst.gain, p = inst.penalty, c = inst.certainty, pr = inst.prescribed, inf = inst.inflicted;
    var e = Rmul(c, p), k = Rcmp(e, g), net = Rsub(g, e);
    var deters = k > 0 ? 'yes: ' + eaNum(e) + ' is more than the gain ' + eaNum(g)
      : k === 0 ? 'no: ' + eaNum(e) + ' equals the gain, and does not exceed it' : 'no: ' + eaNum(e) + ' is less than the gain ' + eaNum(g);
    var least = Rzero(c) ? 'none: at certainty 0 the penalty is never inflicted, so no penalty deters' : 'more than ' + eaNum(Rdiv(g, c));
    var host, price;
    if (pr === '-' || inf === '-') host = 'needs both the prescribed and the inflicted penalty';
    else if (Rcmp(inf, pr) > 0) host = 'yes: the excess, ' + eaNum(Rsub(inf, pr)) + ', is not punishment but an act of hostility';
    else host = 'no: the inflicted ' + eaNum(inf) + ' is within the prescribed ' + eaNum(pr);
    if (pr === '-') price = 'no prescribed penalty is given';
    else if (Rcmp(pr, g) < 0) price = 'yes: the prescribed ' + eaNum(pr) + ' is less than the gain ' + eaNum(g) + ', rather the price of the crime than a punishment';
    else price = 'no: the prescribed ' + eaNum(pr) + ' is not less than the gain ' + eaNum(g);
    return {
      tiles: { llwExpected: eaNum(e), llwNet: (net.n > 0n ? '+' : '') + eaNum(net), llwDeters: deters, llwLeast: least, llwHostility: host, llwPrice: price },
      status: lvkStatus('At a certainty of ' + lvkPct(c) + ' a penalty of ' + eaNum(p) + ' is expected to cost ' + eaNum(e) + ' against a gain of ' + eaNum(g)
        + (k > 0 ? ': on this model the crime does not pay' : Rcmp(c, R1) < 0 ? ': on this model the hope of impunity makes the crime pay'
          : ': the penalty is certain but not more than the gain, so it is rather the price of the crime') + ' (deterrence here is a stated model, the expected penalty against the gain)'),
      table: null
    };
  };
"""

# ---------------------------------------------------------------------------
# canon (lcn): when a book was written; who benefits from a doctrine
# ---------------------------------------------------------------------------

LCN_JS = r"""
  var LCN_VIEW = {};
  function lcnCompute(view, inst, opts) { return eaRun(LCN_VIEW[view], inst, opts); }
  function lcnYear(r) { return lvkDec(r); }
"""

LCN_VIEW_JS = {}

LCN_VIEW_JS["date"] = r"""
  LCN_VIEW.date = function (inst) {
    var B = inst.books, M = inst.mentions, of = {};
    B.forEach(function (b) { of[b.book] = []; });
    M.forEach(function (m, i) {
      if (!of[m.book]) eaRefuse('Mentions, record ' + (i + 1) + ': the book ' + m.book + ' is not one of the books');
      of[m.book].push(m);
    });
    var after = [], possible = [], none = [], latest = [], gaps = [], rows = [];
    B.forEach(function (b) {
      var L = of[b.book];
      if (!L.length) {
        none.push(b.book); latest.push(b.book + ': no test'); gaps.push(b.book + ' no test');
        rows.push([b.book, b.author, lcnYear(b.author_death), '', '', 'no test']); return;
      }
      var top = L[0].year;
      L.forEach(function (m) { if (Rcmp(m.year, top) > 0) top = m.year; });
      var ev = L.filter(function (m) { return Requ(m.year, top); }).map(function (m) { return m.event; }).join(' and ');
      var gap = Rsub(top, b.author_death), late = Rcmp(gap, R0) > 0;
      (late ? after : possible).push(b.book);
      latest.push(b.book + ': ' + ev + ' (' + lcnYear(top) + ')');
      gaps.push(b.book + ' ' + (late ? eaPlural(gap.n, 'year', 'years') + ' after' : Rzero(gap) ? 'in the year of' : eaPlural(-gap.n, 'year', 'years') + ' before') + ' ' + b.author + '\'s death');
      rows.push([b.book, b.author, lcnYear(b.author_death), ev, lcnYear(top), late ? 'written after ' + b.author + '\'s death' : 'not ruled out']);
    });
    return {
      tiles: { lcnLatest: latest.join('; '), lcnAfter: eaCount(after), lcnGap: gaps.join('; '), lcnPossible: eaCount(possible), lcnNoTest: eaCount(none) },
      status: lvkStatus(eaPlural(after.length, 'book mentions', 'books mention') + ' something after the death of its traditional author, so it was written after it'
        + '; a book is not shown to be its author\'s by passing this test, only not ruled out'),
      table: { caption: 'Each book, the latest thing it mentions, and its traditional author', head: ['book', 'author', 'author died', 'latest mention', 'year', 'verdict'], rows: rows }
    };
  };
"""

LCN_VIEW_JS["benefit"] = r"""
  LCN_VIEW.benefit = function (inst) {
    var Ps = inst.parties, D = inst.doctrines, known = {}, by = {};
    Ps.forEach(function (p) { known[p] = true; by[p] = []; });
    D.forEach(function (d, i) {
      d.benefits.forEach(function (p) {
        if (!known[p]) eaRefuse('Doctrines, record ' + (i + 1) + ' (' + d.doctrine + '): ' + p + ' is not one of the parties');
        by[p].push(d.doctrine);
      });
    });
    var top = 0;
    Ps.forEach(function (p) { if (by[p].length > top) top = by[p].length; });
    var most = Ps.filter(function (p) { return by[p].length === top; });
    var noOne = D.filter(function (d) { return !d.benefits.length; }).map(function (d) { return d.doctrine; });
    var unserved = Ps.filter(function (p) { return !by[p].length; });
    var mostText = top === 0 ? 'none: no doctrine benefits any party'
      : most.join(' and ') + ', ' + top + ' of ' + eaPlural(D.length, 'doctrine', 'doctrines') + (most.length > 1 ? ' each (a tie)' : '');
    return {
      tiles: { lcnCounts: Ps.map(function (p) { return p + ' ' + by[p].length; }).join('; '), lcnMost: mostText,
        lcnNoOne: eaCount(noOne), lcnUnserved: eaCount(unserved) },
      status: lvkStatus('Of ' + eaPlural(D.length, 'doctrine', 'doctrines') + ', ' + (top === 0 ? 'none benefits any party named' : 'the most, ' + top + ', benefit ' + most.join(' and '))
        + '. Who benefits is counted from the lesson\'s list; whether a doctrine is true is not'),
      table: { caption: 'Each party and the doctrines that benefit it', head: ['party', 'doctrines', 'which'], rows: Ps.map(function (p) { return [p, String(by[p].length), by[p].join(', ')]; }) }
    };
  };
"""

# ---------------------------------------------------------------------------
# Python: the checks (each mirrors a JS refusal beyond the field parser)
# ---------------------------------------------------------------------------


def _check_voices(inst, fixed):
    return None


def _check_ties(inst, fixed):
    seen = set()
    for r in inst["sizes"]:
        n = int(r)
        if n in seen:
            raise ValueError("Sizes: %d is given twice" % n)
        seen.add(n)


def _check_heir(inst, fixed):
    P = inst["people"]
    by = {p["person"]: p for p in P}
    for i, p in enumerate(P):
        if p["parent"] == "-":
            continue
        if p["parent"] == p["person"]:
            raise ValueError("People, record %d (%s) is named as their own parent" % (i + 1, p["person"]))
        if p["parent"] not in by:
            raise ValueError("People, record %d (%s): the parent %s is not one of the people"
                             % (i + 1, p["person"], p["parent"]))
    for p in P:
        walk, at, x = [], {}, p["person"]
        while x != "-":
            if x in at:
                raise ValueError("People: %s are one another's ancestors in a loop" % ", ".join(walk[at[x]:]))
            at[x] = len(walk)
            walk.append(x)
            x = by[x]["parent"]
    born = {}
    for i, p in enumerate(P):
        b = int(p["born"])
        if b in born:
            raise ValueError("People, record %d (%s) is born %d, as %s is: born gives the order of birth, so no two "
                             "people share it" % (i + 1, p["person"], b, born[b]))
        born[b] = p["person"]
    for i, p in enumerate(P):
        if p["parent"] != "-" and p["born"] <= by[p["parent"]]["born"]:
            raise ValueError("People, record %d (%s) is born %d, not after the parent %s (born %d)"
                             % (i + 1, p["person"], int(p["born"]), p["parent"], int(by[p["parent"]]["born"])))
    mon, named = inst["monarch"], inst["named"]
    if mon not in by:
        raise ValueError("The monarch, %s, is not one of the people" % mon)
    if named != "-":
        if named not in by:
            raise ValueError("The successor named, %s, is not one of the people" % named)
        if named == mon:
            raise ValueError("The successor named, %s, is the monarch" % named)
        if by[named]["alive"] != "yes":
            raise ValueError("The successor named, %s, is dead (alive is no), and the dead cannot succeed" % named)


def _check_impose(inst, fixed):
    if sum((p["riches"] for p in inst["persons"]), Fraction(0)) == 0:
        raise ValueError("Persons: every person's riches are 0, so no rate on riches can raise the revenue")
    if sum((p["consumption"] for p in inst["persons"]), Fraction(0)) == 0:
        raise ValueError("Persons: every person's consumption is 0, so no rate on consumption can raise the revenue")


def _check_shares(inst, fixed):
    f = sum((s["fraction"] for s in inst["setaside"]), Fraction(0))
    if f > 1:
        raise ValueError("Set apart: the fractions add to %s/%s, more than the whole"
                         % (ea.grp(f.numerator), ea.grp(f.denominator)))


def _check_silence(inst, fixed):
    known = set(inst["actions"])
    for i, l in enumerate(inst["laws"]):
        for key, verb in (("commands", "commands"), ("forbids", "forbids")):
            for a in l[key]:
                if a not in known:
                    raise ValueError("Laws, record %d (%s): it %s %s, which is not one of the actions"
                                     % (i + 1, l["law"], verb, a))
    for i, x in enumerate(inst["inalienable"]):
        if x["action"] not in known:
            raise ValueError("Inalienable, record %d: %s is not one of the actions" % (i + 1, x["action"]))


def _check_date(inst, fixed):
    books = {b["book"] for b in inst["books"]}
    for i, m in enumerate(inst["mentions"]):
        if m["book"] not in books:
            raise ValueError("Mentions, record %d: the book %s is not one of the books" % (i + 1, m["book"]))


def _check_benefit(inst, fixed):
    known = set(inst["parties"])
    for i, d in enumerate(inst["doctrines"]):
        for p in d["benefits"]:
            if p not in known:
                raise ValueError("Doctrines, record %d (%s): %s is not one of the parties" % (i + 1, d["doctrine"], p))


# ---------------------------------------------------------------------------
# Python: the spec dicts (kit-contract.md section 2)
# ---------------------------------------------------------------------------

_YEAR = ea.whole(-ea.LIMIT, ea.LIMIT)
_AMOUNT = ea.whole(0, ea.LIMIT)

ASSEMBLY = {
    "prefix": "las", "fn": "lasCompute", "title": "An assembly's voices", "js": LAS_JS,
    "views": {
        "voices": {
            "fields": [("members", lrec("Members (member, voice: yes, no or abstain)",
                                        [("member", _N), ("voice", ea.word("yes", "no", "abstain"))],
                                        unique=True, rows=4, lo=1, hi=60), None),
                       ("rule", ea.choice("Rule", "greater", "absolute"), "greater"),
                       ("liable", ea.choice("Show who is answerable for the decree", "no", "yes"), "no")],
            "tiles": [("Yes", "lasYes"), ("No", "lasNo"), ("Abstain", "lasAbstain"), ("The decision", "lasDecision"),
                      ("Margin (yes less no)", "lasMargin"), ("Yes voices needed to pass", "lasNeeded"),
                      ("Answerable for the decree", "lasLiable"), ("Excused", "lasExcused")],
            "check": None,
            "subtitle": "what a representative's voices decide, and when an even assembly is mute",
            "rules": "Each member gives one voice: yes, no or abstain. On the rule greater, the motion passes when the "
                     "yes voices are more than the no voices given; on the rule absolute, when the yes voices are more "
                     "than half of all the members, abstainers counted. On either rule, when the yes and no voices are "
                     "equal (none at all included) the assembly is mute and nothing is decreed (Chapter 16). With "
                     "answerable shown, a decree that passes binds as its authors only the members who voted yes; "
                     "those who voted no or abstained are excused (Chapter 22). Members go in the order given.",
            "js": LAS_VIEW_JS["voices"],
        },
        "ties": {
            "fields": [("sizes", llist("Assembly sizes (1 to 60 members each, up to 8 sizes)", ea.whole(1, 60),
                                       lo=1, hi=8, things="sizes"), None)],
            "tiles": [("Chance of an even split, for each size", "lasChances"), ("Odd sizes: never mute", "lasOdd"),
                      ("The even size most often mute", "lasMost"), ("The even size least often mute", "lasLeast")],
            "check": _check_ties,
            "subtitle": "how often an assembly of n members splits evenly",
            "rules": "The model is stated, not Hobbes's: each member says yes or no with equal chance, independently "
                     "of the others, and no one abstains. Of the 2^n ways n members can vote, C(n, n/2) split evenly, "
                     "so the chance of a mute assembly is C(n, n/2) ÷ 2^n, exact, and 0 for an odd n. Chances print as "
                     "the fraction and its percentage to at most two places. Sizes go in the order given; a size given "
                     "twice is refused.",
            "js": LAS_VIEW_JS["ties"],
        },
    },
}

SUCCESSION = {
    "prefix": "lsu", "fn": "lsuCompute", "title": "The right of succession", "js": LSU_JS,
    "views": {
        "heir": {
            "fields": [("people", lrec("People (person, parent or -, sex m or f, born, alive yes or no)",
                                       [("person", _N), ("parent", ea.PARENT), ("sex", ea.word("m", "f")),
                                        ("born", _AMOUNT), ("alive", ea.YESNO)], unique=True, rows=6, lo=2, hi=20),
                        None),
                       ("monarch", ea.field("The monarch", _N), None),
                       ("named", ea.field("Successor named by express words or testament (- for none)", ea.PARENT), "-"),
                       ("custom", ea.choice("Custom", "none", "male-line"), "none")],
            "tiles": [("The successor", "lsuSuccessor"), ("By what right", "lsuRule"),
                      ("The line of succession (first 6)", "lsuLine"), ("Without the testament", "lsuWithout"),
                      ("By presumption alone", "lsuPresumption"), ("The monarch's living issue", "lsuIssue"),
                      ("The successor's nearness in blood", "lsuNear")],
            "check": _check_heir,
            "subtitle": "who succeeds a monarch, by testament, custom or presumption",
            "rules": "A successor named by express words or testament succeeds first; failing that, custom, and "
                     "failing both, the presumption of natural affection (Chapter 19). The kit reads the presumption "
                     "so, which is its reading and not Hobbes's words: the monarch's own issue before all others; among "
                     "the issue each child in turn, male before female and then elder before younger, followed by that "
                     "child's own issue in the same order, so that a dead child's issue stand in its place before the "
                     "next child; with no living issue, the nearer in blood before the remoter, counting the steps up "
                     "from the monarch to the nearest common ancestor and down from it to the person (a parent is 1, "
                     "a brother 2, a nephew 3), and among the equally near, male before female and elder before "
                     "younger. Born is the order of birth: smaller is elder. The dead do not succeed, but their issue "
                     "are counted. Custom male-line admits only males whose descent from the common ancestor, and the "
                     "monarch's, runs through males (the common ancestor male, unless it is the monarch). People with "
                     "no ancestor in common with the monarch are not of the blood. After a testament, the line "
                     "continues by custom or presumption.",
            "js": LSU_VIEW_JS["heir"],
        },
    },
}

TAX = {
    "prefix": "ltx", "fn": "ltxCompute", "title": "Taxes and shares", "js": LTX_JS,
    "views": {
        "impose": {
            "fields": [("persons", lrec("Persons (person, riches, consumption: whole amounts)",
                                        [("person", _N), ("riches", _AMOUNT), ("consumption", _AMOUNT)],
                                        unique=True, rows=5, lo=1, hi=60), None),
                       ("revenue", ea.field("Revenue to raise", rat(gt=0)), None)],
            "tiles": [("Rate on riches", "ltxRateRiches"), ("Rate on consumption", "ltxRateConsumption"),
                      ("Each person's tax on riches", "ltxOnRiches"),
                      ("Each person's tax on consumption", "ltxOnConsumption"),
                      ("Difference (on consumption less on riches)", "ltxDifference"),
                      ("Who pays more on consumption", "ltxMore"),
                      ("Tax on riches, as a share of what each consumes", "ltxBurdenRiches"),
                      ("Tax on consumption, as a share of what each consumes", "ltxBurdenConsumption")],
            "check": _check_impose,
            "subtitle": "an equal imposition on riches against one on consumption",
            "rules": "The rate on riches is the revenue ÷ everyone's riches added up, and on consumption the revenue ÷ "
                     "everyone's consumption; a person's tax is the rate × their riches (or consumption), so both "
                     "raise the whole revenue. Every figure is exact; a rate or share prints as the fraction and its "
                     "percentage to at most two places. A person pays more on consumption when that tax is greater, "
                     "not when equal. A share of consumption is not defined for a person who consumes nothing. "
                     "Persons go in the order given.",
            "js": LTX_VIEW_JS["impose"],
        },
        "shares": {
            "fields": [("total", ea.field("What is divided (the total)", rat(gt=0)), None),
                       ("parties", lrec("Parties (party, weight)", [("party", _N), ("weight", rat(gt=0))],
                                        unique=True, rows=4, lo=1, hi=60), None),
                       ("setaside", lrec("Set apart first (party, fraction of the total); empty for none",
                                         [("party", _N), ("fraction", rat(gt=0, hi=1))], unique=True, rows=2, lo=0,
                                         hi=60), "")],
            "tiles": [("Set apart first", "ltxSetAside"), ("The remainder", "ltxRemainder"),
                      ("Weights in all", "ltxWeight"), ("Each party's share of the remainder", "ltxShares"),
                      ("Shares that are not whole", "ltxNotWhole"), ("Every portion added up", "ltxSum")],
            "check": _check_shares,
            "subtitle": "a distribution by stated shares, with a portion set apart",
            "rules": "Each portion set apart is its fraction × the total, taken first; the fractions may add to at "
                     "most the whole. The remainder is divided by weight: a party's share is the remainder × its "
                     "weight ÷ all the weights. A party may be both set apart a portion and given a share; its "
                     "portion is the two added. Every figure is exact and none is rounded: a share that is not whole "
                     "prints as its fraction, with its decimal only when that ends within six places. Parties go in "
                     "the order given.",
            "js": LTX_VIEW_JS["shares"],
        },
    },
}

LAW = {
    "prefix": "llw", "fn": "llwCompute", "title": "The law and its silence", "js": LLW_JS,
    "views": {
        "silence": {
            "fields": [("actions", llist("Actions (up to 12 names)", _N, lo=1, hi=12, things="actions"), None),
                       ("laws", lrec("Laws (law, actions it commands, actions it forbids: names separated by spaces, "
                                     "- for none)", [("law", _N), ("commands", NAMES_DASH), ("forbids", NAMES_DASH)],
                                     unique=True, rows=3, lo=1, hi=60), None),
                       ("inalienable", lrec("Liberties a subject keeps whatever is commanded (action, reason in "
                                            "words); empty for none", [("action", _N), ("reason", NAMES)],
                                            unique=True, rows=2, lo=0, hi=12), "")],
            "tiles": [("Commanded", "llwCommanded"), ("Forbidden", "llwForbidden"),
                      ("Free, in the silence of the law", "llwFree"),
                      ("Both commanded and forbidden (a contradiction)", "llwBoth"),
                      ("Commands a subject may still refuse", "llwRefusable"), ("Share of actions left free", "llwShareFree")],
            "check": _check_silence,
            "subtitle": "what the laws command, forbid, and leave free",
            "rules": "An action is commanded when some law commands it, forbidden when some law forbids it, and free "
                     "when no law does either: the liberty of subjects lies in the silence of the law (Chapter 21). "
                     "An action both commanded and forbidden is listed as a contradiction in the laws, with the laws "
                     "that do each. A liberty a subject keeps whatever is commanded (Chapter 21's true liberties) "
                     "makes any command of that action one the subject may still refuse; the reason is the lesson's. "
                     "The share free is the free actions over all of them, exact. Actions go in the order given.",
            "js": LLW_VIEW_JS["silence"],
        },
        "deter": {
            "fields": [("gain", ea.field("The benefit of the crime to the offender", rat(lo=0)), None),
                       ("penalty", ea.field("The penalty", rat(lo=0)), None),
                       ("certainty", ea.field("Chance the penalty is inflicted (0 to 1)", rat(lo=0, hi=1)), None),
                       ("prescribed", ea.field("Penalty the law prescribed beforehand (- for none)", rat(lo=0, dash=True)), "-"),
                       ("inflicted", ea.field("Penalty inflicted (- for none)", rat(lo=0, dash=True)), "-")],
            "tiles": [("Expected penalty", "llwExpected"), ("Gain less expected penalty", "llwNet"),
                      ("Does the expected penalty exceed the gain?", "llwDeters"),
                      ("Penalty it must exceed to deter at this certainty", "llwLeast"),
                      ("Inflicted beyond the prescribed: hostility?", "llwHostility"),
                      ("Prescribed below the gain: a price, not a punishment?", "llwPrice")],
            "check": None,
            "subtitle": "a penalty against the benefit of the crime",
            "rules": "The model is stated: the expected penalty is the chance it is inflicted × the penalty, exact, and "
                     "it deters when it is more than the gain (equal does not). To deter at this certainty a penalty "
                     "must exceed the gain ÷ the certainty; at certainty 0 none does. With a prescribed and an "
                     "inflicted penalty: an inflicted penalty greater than the prescribed is, in its excess, not "
                     "punishment but an act of hostility (Chapter 28); a prescribed penalty less than the gain is, on "
                     "Hobbes's definition, rather the price of the crime than its punishment (equal is not less).",
            "js": LLW_VIEW_JS["deter"],
        },
    },
}

CANON = {
    "prefix": "lcn", "fn": "lcnCompute", "title": "Scripture and its uses", "js": LCN_JS,
    "views": {
        "date": {
            "fields": [("books", lrec("Books (book, traditional author, the author's death: a whole year on the stated "
                                      "scale, negative allowed)",
                                      [("book", _N), ("author", _N), ("author_death", _YEAR)], unique=True, rows=4,
                                      lo=1, hi=30), None),
                       ("mentions", lrec("Mentions (book, event, year on the same scale)",
                                         [("book", _N), ("event", _N), ("year", _YEAR)], rows=5, lo=0, hi=60), None)],
            "tiles": [("The latest thing each book mentions", "lcnLatest"),
                      ("Written after the author's death", "lcnAfter"), ("Latest mention against the author's death", "lcnGap"),
                      ("Not ruled out by this test", "lcnPossible"), ("No mention, no test", "lcnNoTest")],
            "check": _check_date,
            "subtitle": "when a book was written, by the latest thing it mentions",
            "rules": "A book was written no earlier than the latest event it mentions (ties are named together). When "
                     "that year is after the year its traditional author died, the book was written after the "
                     "author's death and cannot be wholly the author's (Chapter 33); in the year of the death or "
                     "before, the test does not rule the author out, which is not to show the author wrote it. Years "
                     "are whole numbers on the scale the lesson states and may be negative. A book with no mention "
                     "has no test. Books go in the order given.",
            "js": LCN_VIEW_JS["date"],
        },
        "benefit": {
            "fields": [("parties", llist("Parties (names)", _N, lo=1, hi=20, things="parties"), None),
                       ("doctrines", lrec("Doctrines (doctrine, the parties it benefits, separated by spaces, - for "
                                          "none)", [("doctrine", _N), ("benefits", NAMES_DASH)], unique=True, rows=5,
                                          lo=1, hi=60), None)],
            "tiles": [("Doctrines benefiting each party", "lcnCounts"), ("The party served by the most", "lcnMost"),
                      ("Doctrines that benefit no one named", "lcnNoOne"), ("Parties served by none", "lcnUnserved")],
            "check": _check_benefit,
            "subtitle": "cui bono: who benefits from a set of doctrines",
            "rules": "Each doctrine lists the parties the lesson says it benefits. A party's count is the number of "
                     "doctrines that benefit it; the party served by the most is the one with the greatest count, "
                     "every party tied at it named together, in the order given. Doctrines benefiting no party (-) "
                     "are listed. The count says who gains by a doctrine (Chapter 47), not whether it is true.",
            "js": LCN_VIEW_JS["benefit"],
        },
    },
}

SPECS = {"assembly": ASSEMBLY, "succession": SUCCESSION, "tax": TAX, "law": LAW, "canon": CANON}

MODES = {"assembly": lambda cfg: mode_lab(cfg, "assembly", ASSEMBLY),
         "succession": lambda cfg: mode_lab(cfg, "succession", SUCCESSION),
         "tax": lambda cfg: mode_lab(cfg, "tax", TAX),
         "law": lambda cfg: mode_lab(cfg, "law", LAW),
         "canon": lambda cfg: mode_lab(cfg, "canon", CANON)}

__all__ = ["MODES", "SPECS"]
