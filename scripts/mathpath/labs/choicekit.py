"""choicekit -- the Philosophy kit for decisions, games and collective choice.

Specified in docs/philosophy/PLAN.md section D.2; the conventions every mode
obeys are D.0. Ten modes, one lesson family each:

  decide     an act x state payoff table under eight decision rules, the value
             of perfect information and the probability at which the top two
             acts by expected utility tie
  update     exact Bayesian updating over a finite set of hypotheses: posterior,
             Bayes factor, confirmation verdict, predictive probability, the
             best act after updating
  credence   a belief threshold over a finite space, a lottery or n independent
             claims; whether the accepted set is consistent; a Dutch book
  series     exact partial sums: geometric, harmonic, St Petersburg, the lamp
  game       a bimatrix game up to 4 x 4: pure and mixed equilibria, dominance,
             iterated elimination, Pareto verdicts
  iterated   the repeated prisoner's dilemma: one match, a round robin of seven
             strategies, the discount thresholds for cooperation
  commons    the n-player symmetric binary-choice game: dominance, equilibria,
             the social optimum, universalisation, replicator steps
  vote       ranking profiles under six rules (Condorcet cycles, IIA,
             manipulation), judgment aggregation, the jury theorem
  aggregate  two welfare vectors under six aggregation rules, Gini, n*
  simpson    rates within two groups against the pooled rate

THE LESSON SUPPLIES THE INSTANCES. Every mode takes cfg["presets"], a list of
{"id", "label", ...instance fields..., "expect": {tile id: text}}, and
cfg["preset"] (default the first). The instance fields are validated here --
a malformed instance raises ValueError naming the preset id -- then turned into
the exact text the reader's own input boxes take, and written into a JS table
with cfg_literal. So a preset and a reader's edit go through ONE parser on the
page, and the figures a preset pins are the figures that parser produces.

A preset menu rewrites the instance inputs. It never touches a redraw-only
<select> (the rule, the view, the weighting, the removed candidate, the series
kind, the hypothesis reported), whose shipped value comes from a lesson-level
cfg key -- except where D.2 puts the field in the preset itself: credence and
vote carry `kind` per preset ("set by the preset"), and iterated carries `a`
and `b` per preset. A preset that carries a redraw-only key its mode ships from
the lesson cfg raises, rather than being silently ignored.

EXACT. Every printed figure is a rational over BigInt (algebra_core's
RATIONAL_JS). Nothing is a float. Where an exact figure would be absurdly long
(a replicator share after 40 generations has billions of digits) the page
refuses that figure and says so instead of rounding it.

THE PAGE SHIPS ONE MODE: RATIONAL_JS, the shared block CK_COMMON_JS and that
mode's block only. Each <MODE>_JS block is pure (no DOM): module-level named
functions that scripts/mathcheck.js can extract with blockFrom(). The DOM
wiring lives in the mode's builder.
"""

import html
import re
from fractions import Fraction

from .algebra_core import RATIONAL_JS
from .common import Lab, cfg_literal

# ---------------------------------------------------------------------------
# Shared JavaScript: reading what a reader typed, and printing tiles
# ---------------------------------------------------------------------------

CK_COMMON_JS = r"""
  /* Every parse below THROWS an Error whose message is a sentence for the
     reader; the mode's redraw catches it, paints the banner red and blanks
     every tile. Nothing after the parse is inside that catch. */
  var CK_DASH = '—', CK_MINUS = '−';
  function ckEsc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }
  function ckClean(text) {
    return String(text === null || text === undefined ? '' : text).replace(/−/g, '-').trim();
  }
  function ckNum(text, what) {
    var s = ckClean(text), r = s === '' ? null : Rparse(s);
    if (r === null) {
      throw new Error(what + ' should be a number such as 3, -2 or 3/4, and "' + s + '" is not one');
    }
    return r;
  }
  function ckTokens(text, sep) {
    return ckClean(text).split(sep).map(function (t) { return t.trim(); })
      .filter(function (t) { return t.length > 0; });
  }
  function ckVec(text, what) {
    var parts = ckTokens(text, /[\s,]+/);
    if (!parts.length) throw new Error(what + ' is empty');
    return parts.map(function (t) { return ckNum(t, 'Each entry of ' + what); });
  }
  function ckRows(text, what) {
    var rows = ckClean(text).split(';').map(function (r) { return r.trim(); });
    if (rows.length === 1 && rows[0] === '') throw new Error(what + ' is empty');
    return rows.map(function (r, i) {
      if (r === '') throw new Error('Row ' + (i + 1) + ' of ' + what + ' is empty');
      return ckVec(r, 'row ' + (i + 1) + ' of ' + what);
    });
  }
  function ckNames(text, what, limit) {
    var names = ckTokens(text, ','), seen = {};
    if (!names.length) throw new Error(what + ' are missing');
    if (limit && names.length > limit) {
      throw new Error(what + ': this lab takes at most ' + limit + ', and there are ' + names.length);
    }
    names.forEach(function (n) {
      if (seen[n]) throw new Error(what + ' name "' + n + '" twice');
      seen[n] = true;
    });
    return names;
  }
  function ckCount(n, one, many) { return n + ' ' + (n === 1 ? one : many); }
  function ckSum(v) { var s = R0; v.forEach(function (x) { s = Radd(s, x); }); return s; }
  /* Probabilities: none negative, and they sum to exactly 1. Not rescaled: a
     distribution that does not sum to one is a typo, and rescaling it would
     answer a question nobody asked. */
  function ckDist(v, what) {
    v.forEach(function (x) {
      if (Rsign(x) < 0) throw new Error(what + ' has a negative entry, ' + Rtext(x));
    });
    var s = ckSum(v);
    if (!Requ(s, R1)) throw new Error(what + ' sums to ' + Rtext(s) + ', not to 1');
    return v;
  }
  function ckUnit(x, what) {
    if (Rsign(x) < 0 || Rcmp(x, R1) > 0) throw new Error(what + ' is ' + Rtext(x) + ', outside 0 to 1');
    return x;
  }
  /* A signed figure: +7, the minus sign for -20, and 0 unsigned. */
  function ckSigned(r) {
    if (Rzero(r)) return '0';
    return Rsign(r) > 0 ? '+' + Rtext(r) : CK_MINUS + Rtext(Rneg(r));
  }
  /* The reader's form of a figure that may be negative, with the minus sign. */
  function ckFig(r) { return Rsign(r) < 0 ? CK_MINUS + Rtext(Rneg(r)) : Rtext(r); }
  /* Indices of the best scores, in index order; sign 1 = largest, -1 = smallest.
     A null score is an option the rule leaves out. */
  function ckBest(scores, sign) {
    var best = null, out = [];
    scores.forEach(function (s, i) {
      if (s === null) return;
      var c = best === null ? 1 : Rcmp(s, best) * sign;
      if (c > 0) { best = s; out = [i]; } else if (c === 0) out.push(i);
    });
    return out;
  }
  function ckPick(names, idx) { return idx.map(function (i) { return names[i]; }).join(', '); }
  function ckSet(id, text) { document.getElementById(id).textContent = text; }
  function ckBlank(ids) { ids.forEach(function (id) { ckSet(id, CK_DASH); }); }
  function ckRefuse(statusEl, ids, why) {
    ckBlank(ids);
    statusEl.innerHTML = '<span class="tone-red">' + ckEsc(why) + '.</span>';
  }
  function ckDigits(r) { return String(r.n < 0n ? -r.n : r.n).length + String(r.d).length; }
  /* A table: head is a list of header texts, rows a list of rows, each cell
     either text or {t: text, c: class}. Every text is escaped here. */
  function ckTable(caption, head, rows) {
    var h = '<caption>' + ckEsc(caption) + '</caption><thead><tr>'
      + head.map(function (x) { return '<th>' + ckEsc(x) + '</th>'; }).join('') + '</tr></thead><tbody>';
    rows.forEach(function (row) {
      h += '<tr>' + row.map(function (cell) {
        var t = (cell && cell.t !== undefined) ? cell.t : cell, c = (cell && cell.c) ? cell.c : '';
        return '<td' + (c ? ' class="' + c + '"' : '') + '>' + ckEsc(t) + '</td>';
      }).join('') + '</tr>';
    });
    return h + '</tbody>';
  }
  function ckOptions(sel, pairs, keep) {
    sel.innerHTML = pairs.map(function (p) {
      return '<option value="' + ckEsc(p[0]) + '">' + ckEsc(p[1]) + '</option>';
    }).join('');
    sel.value = keep;
  }
"""

# ---------------------------------------------------------------------------
# decide
# ---------------------------------------------------------------------------

DECIDE_JS = r"""
  /* a dominates b: at least as good in every state and better in some. */
  function deDominates(a, b) {
    var some = false;
    for (var s = 0; s < a.length; s += 1) {
      var c = Rcmp(a[s], b[s]);
      if (c < 0) return false;
      if (c > 0) some = true;
    }
    return some;
  }
  function deEu(row, probs) {
    var t = R0;
    for (var s = 0; s < row.length; s += 1) t = Radd(t, Rmul(row[s], probs[s]));
    return t;
  }
  function deRead(v) {
    var acts = ckNames(v.acts, 'The acts', 5), states = ckNames(v.states, 'The states', 5);
    var pay = ckRows(v.matrix, 'the payoff table');
    if (pay.length !== acts.length) {
      throw new Error('The payoff table has ' + pay.length + ' rows and there are ' + acts.length
        + ' acts; it needs one row per act');
    }
    pay.forEach(function (row, i) {
      if (row.length !== states.length) {
        throw new Error('The table is ragged: the row for ' + acts[i] + ' has ' + ckCount(row.length, 'entry', 'entries')
          + ' and there are ' + ckCount(states.length, 'state', 'states'));
      }
    });
    var probs = null;
    if (ckClean(v.probs) !== '') {
      probs = ckVec(v.probs, 'the probabilities');
      if (probs.length !== states.length) {
        throw new Error('There are ' + probs.length + ' probabilities for ' + states.length + ' states');
      }
      ckDist(probs, 'The probability row');
    }
    var cond = null;
    if (ckClean(v.cond) !== '') {
      cond = acts.map(function () { return null; });
      ckTokens(v.cond, ';').forEach(function (part) {
        var at = part.indexOf(':');
        if (at < 0) throw new Error('Each conditional row reads "act: p1 p2", and "' + part + '" has no colon');
        var name = part.slice(0, at).trim(), k = acts.indexOf(name);
        if (k < 0) throw new Error('"' + name + '" in the conditional rows is not one of the acts');
        if (cond[k]) throw new Error('The conditional rows give ' + name + ' twice');
        var row = ckVec(part.slice(at + 1), 'the conditional row for ' + name);
        if (row.length !== states.length) {
          throw new Error('The conditional row for ' + name + ' has ' + row.length + ' entries for '
            + states.length + ' states');
        }
        cond[k] = ckDist(row, 'The conditional row for ' + name);
      });
    }
    var forbid = acts.map(function () { return false; });
    ckTokens(v.forbid, ',').forEach(function (name) {
      var k = acts.indexOf(name);
      if (k < 0) throw new Error('"' + name + '" in the forbidden acts is not one of the acts');
      forbid[k] = true;
    });
    return { acts: acts, states: states, pay: pay, probs: probs, cond: cond, forbid: forbid };
  }
  /* The score each rule gives each act (null for an act it leaves out), and
     whether the rule wants the largest (1) or the smallest (-1). */
  function deScore(inst, rule) {
    var pay = inst.pay, out = [], i, s, m = inst.states.length;
    if (rule === 'maximin' || rule === 'maximax') {
      for (i = 0; i < pay.length; i += 1) {
        var v = pay[i][0];
        for (s = 1; s < m; s += 1) {
          var c = Rcmp(pay[i][s], v);
          if (rule === 'maximin' ? c < 0 : c > 0) v = pay[i][s];
        }
        out.push(v);
      }
      return { scores: out, sign: 1 };
    }
    if (rule === 'regret') {
      var top = [];
      for (s = 0; s < m; s += 1) {
        var t = pay[0][s];
        for (i = 1; i < pay.length; i += 1) if (Rcmp(pay[i][s], t) > 0) t = pay[i][s];
        top.push(t);
      }
      for (i = 0; i < pay.length; i += 1) {
        var worst = R0;
        for (s = 0; s < m; s += 1) {
          var r = Rsub(top[s], pay[i][s]);
          if (Rcmp(r, worst) > 0) worst = r;
        }
        out.push(worst);
      }
      return { scores: out, sign: -1 };
    }
    if (rule === 'laplace') {
      for (i = 0; i < pay.length; i += 1) out.push(Rdiv(ckSum(pay[i]), R(m)));
      return { scores: out, sign: 1 };
    }
    if (rule === 'eu' || rule === 'constrained') {
      if (!inst.probs) {
        return { need: (rule === 'eu' ? 'Expected utility' : 'The constrained rule')
          + ' needs a probability for each state, and the probabilities box is empty' };
      }
      for (i = 0; i < pay.length; i += 1) {
        out.push(rule === 'constrained' && inst.forbid[i] ? null : deEu(pay[i], inst.probs));
      }
      return { scores: out, sign: 1 };
    }
    if (rule === 'evidential') {
      for (i = 0; i < pay.length; i += 1) {
        if (!inst.cond || !inst.cond[i]) {
          return { need: 'Evidential expected utility needs a conditional row for every act, and '
            + inst.acts[i] + ' has none' };
        }
        out.push(deEu(pay[i], inst.cond[i]));
      }
      return { scores: out, sign: 1 };
    }
    return { need: 'There is no rule called ' + rule };
  }
  function deDecide(inst, rule) {
    var n = inst.pay.length, i, j;
    if (rule === 'dominance') {
      var undominated = [], top = -1;
      for (i = 0; i < n; i += 1) {
        var beaten = false, beatsAll = true;
        for (j = 0; j < n; j += 1) {
          if (j === i) continue;
          if (deDominates(inst.pay[j], inst.pay[i])) beaten = true;
          if (!deDominates(inst.pay[i], inst.pay[j])) beatsAll = false;
        }
        if (!beaten) undominated.push(i);
        if (beatsAll && n > 1) top = i;
      }
      return { choice: top < 0 ? [] : [top], value: null, undominated: undominated, scores: null };
    }
    var sc = deScore(inst, rule);
    if (sc.need) return { need: sc.need };
    var best = ckBest(sc.scores, sc.sign);
    return { choice: best, value: best.length ? sc.scores[best[0]] : null, scores: sc.scores };
  }
  /* The acts a rule chooses among: all of them, except under the constrained rule. */
  function deConsidered(inst, rule) {
    var out = [];
    for (var i = 0; i < inst.acts.length; i += 1) {
      if (!(rule === 'constrained' && inst.forbid[i])) out.push(i);
    }
    return out;
  }
  /* Value of perfect information: the sum over states of p(s) times the best
     payoff in s, minus the best expected utility. */
  function deVpi(inst, acts) {
    if (!inst.probs || !acts.length) return null;
    var withInfo = R0, without = null;
    for (var s = 0; s < inst.states.length; s += 1) {
      var best = null;
      acts.forEach(function (a) { if (best === null || Rcmp(inst.pay[a][s], best) > 0) best = inst.pay[a][s]; });
      withInfo = Radd(withInfo, Rmul(inst.probs[s], best));
    }
    acts.forEach(function (a) {
      var e = deEu(inst.pay[a], inst.probs);
      if (without === null || Rcmp(e, without) > 0) without = e;
    });
    return Rsub(withInfo, without);
  }
  /* Two states: the p(state 1) at which the top two acts by expected utility
     tie. null = not applicable, 'none' = they never tie inside [0, 1]. */
  function deFlip(inst, acts) {
    if (!inst.probs || inst.states.length !== 2) return null;
    if (acts.length < 2) return 'none';
    var eu = {};
    acts.forEach(function (a) { eu[a] = deEu(inst.pay[a], inst.probs); });
    var order = acts.slice().sort(function (x, y) { var c = Rcmp(eu[y], eu[x]); return c !== 0 ? c : x - y; });
    var a = inst.pay[order[0]], b = inst.pay[order[1]];
    var den = Radd(Rsub(a[0], a[1]), Rsub(b[1], b[0]));
    if (Rzero(den)) return 'none';
    var p = Rdiv(Rsub(b[1], a[1]), den);
    if (Rsign(p) < 0 || Rcmp(p, R1) > 0) return 'none';
    return { p: p, a: order[0], b: order[1] };
  }
"""

# ---------------------------------------------------------------------------
# update
# ---------------------------------------------------------------------------

UPDATE_JS = r"""
  function upNames(given, count, stem) {
    if (given && given.length === count) return given.slice();
    var out = [];
    for (var i = 0; i < count; i += 1) out.push(stem + (i + 1));
    return out;
  }
  function upRead(v, hypNames, outNames) {
    var lik = ckRows(v.lik, 'the likelihood table');
    if (lik.length > 10) throw new Error('The likelihood table has ' + lik.length + ' rows; this lab takes at most 10 hypotheses');
    var nOut = lik[0].length;
    if (nOut > 10) throw new Error('This lab takes at most 10 outcomes, and the likelihood rows have ' + nOut);
    var hyps = upNames(hypNames, lik.length, 'H'), outs = upNames(outNames, nOut, 'o');
    lik.forEach(function (row, i) {
      if (row.length !== nOut) {
        throw new Error('The likelihood table is ragged: the row for ' + hyps[i] + ' has ' + ckCount(row.length, 'entry', 'entries')
          + ' and the first row has ' + nOut);
      }
      ckDist(row, 'The likelihood row for ' + hyps[i]);
    });
    var prior = ckVec(v.prior, 'the prior');
    if (prior.length !== lik.length) {
      throw new Error('The prior has ' + prior.length + ' entries and there are ' + lik.length + ' hypotheses');
    }
    ckDist(prior, 'The prior');
    var counts = outs.map(function () { return 0; }), total = 0;
    ckTokens(v.data, /\s+/).forEach(function (tok) {
      var m = /^(.+)\*(\d+)$/.exec(tok), name = m ? m[1] : tok, times = m ? parseInt(m[2], 10) : 1;
      var k = outs.indexOf(name);
      if (k < 0) throw new Error('"' + name + '" in the data is not one of the outcomes (' + outs.join(', ') + ')');
      counts[k] += times; total += times;
      if (total > 1000) throw new Error('This lab takes at most 1000 observations');
    });
    var pay = null;
    if (ckClean(v.pay) !== '') {
      pay = [];
      ckTokens(v.pay, ';').forEach(function (part) {
        var at = part.indexOf(':');
        if (at < 0) throw new Error('Each payoff row reads "act: one payoff per hypothesis", and "' + part + '" has no colon');
        var name = part.slice(0, at).trim();
        if (!name) throw new Error('A payoff row has no act name');
        var vals = ckVec(part.slice(at + 1), 'the payoffs of ' + name);
        if (vals.length !== hyps.length) {
          throw new Error('The act ' + name + ' has ' + vals.length + ' payoffs and there are ' + hyps.length + ' hypotheses');
        }
        pay.push({ name: name, vals: vals });
      });
    }
    return { hyps: hyps, outs: outs, prior: prior, lik: lik, counts: counts, n: total, pay: pay };
  }
  /* P(data | each hypothesis): observations independent given the hypothesis,
     so a product of powers of the likelihoods. */
  function upLikelihood(inst) {
    return inst.lik.map(function (row) {
      var l = R1;
      for (var o = 0; o < row.length; o += 1) if (inst.counts[o]) l = Rmul(l, Rpow(row[o], inst.counts[o]));
      return l;
    });
  }
  function upSolve(inst, h) {
    var like = upLikelihood(inst), joint = [], total = R0, i;
    for (i = 0; i < like.length; i += 1) { joint.push(Rmul(inst.prior[i], like[i])); total = Radd(total, joint[i]); }
    if (Rzero(total)) {
      return { refuse: 'These data have probability 0 under every hypothesis the prior allows, so there is nothing to update to' };
    }
    var post = joint.map(function (j) { return Rdiv(j, total); });
    var rest = Rsub(R1, inst.prior[h]), bf = null;
    if (!Rzero(rest)) {
      var pNot = Rdiv(Rsub(total, joint[h]), rest);
      bf = Rzero(pNot) ? 'infinite' : Rdiv(like[h], pNot);
    }
    var move = Rcmp(post[h], inst.prior[h]);
    var conf = Rzero(post[h]) ? 'Refutes' : (Requ(post[h], R1) ? 'Proves'
      : (move > 0 ? 'Confirms' : (move < 0 ? 'Disconfirms' : 'Neutral')));
    var pred = R0;
    for (i = 0; i < post.length; i += 1) pred = Radd(pred, Rmul(post[i], inst.lik[i][0]));
    var best = null;
    if (inst.pay) {
      var eus = inst.pay.map(function (act) {
        var e = R0;
        for (var k = 0; k < post.length; k += 1) e = Radd(e, Rmul(post[k], act.vals[k]));
        return e;
      });
      var idx = ckBest(eus, 1);
      best = { names: idx.map(function (k) { return inst.pay[k].name; }), value: eus[idx[0]], eus: eus };
    }
    return { like: like, post: post, total: total, bf: bf, conf: conf, pred: pred, best: best };
  }
"""

# ---------------------------------------------------------------------------
# credence
# ---------------------------------------------------------------------------

CREDENCE_JS = r"""
  function crSpace(outsText, probsText) {
    var outs = ckTokens(outsText, /\s+/), probs = ckVec(probsText, 'the outcome probabilities');
    if (outs.length !== probs.length) throw new Error('The space has ' + outs.length + ' outcomes and ' + probs.length + ' probabilities');
    ckDist(probs, 'The outcome distribution');
    return { outs: outs, probs: probs };
  }
  function crReadEvents(text, space) {
    var events = [], seen = {};
    ckTokens(text, ';').forEach(function (part) {
      var at = part.indexOf(':');
      if (at < 0) throw new Error('Each event reads "name: outcome outcome", and "' + part + '" has no colon');
      var name = part.slice(0, at).trim();
      if (!name) throw new Error('An event has no name');
      if (seen[name]) throw new Error('The event "' + name + '" is defined twice');
      seen[name] = true;
      var set = space.outs.map(function () { return false; });
      ckTokens(part.slice(at + 1), /\s+/).forEach(function (o) {
        var k = space.outs.indexOf(o);
        if (k < 0) throw new Error('"' + o + '" in the event ' + name + ' is not an outcome (' + space.outs.join(', ') + ')');
        set[k] = true;
      });
      events.push({ name: name, set: set });
    });
    if (!events.length) throw new Error('There are no events to believe');
    if (events.length > 12) throw new Error('This lab takes at most 12 events');
    return events;
  }
  function crReadTyped(text, events) {
    var s = ckClean(text), out = [], re = /([^=]+?)\s*=\s*([^\s=]+)/g, m, used = '';
    while ((m = re.exec(s)) !== null) {
      var name = m[1].trim(), k = -1;
      for (var i = 0; i < events.length; i += 1) if (events[i].name === name) k = i;
      if (k < 0) throw new Error('"' + name + '" in the typed credences is not one of the events');
      out.push({ k: k, c: ckNum(m[2], 'The credence in ' + name) });
      used += m[0];
    }
    if (used.replace(/\s+/g, '') !== s.replace(/\s+/g, '')) {
      throw new Error('Typed credences read "event=3/5 other=2/5", and "' + s + '" does not');
    }
    return out;
  }
  function crProb(space, set) {
    var p = R0;
    for (var i = 0; i < set.length; i += 1) if (set[i]) p = Radd(p, space.probs[i]);
    return p;
  }
  /* Accept each event whose probability reaches the threshold; the accepted
     set is consistent iff the intersection of its events is nonempty. */
  function crSpaceVerdict(space, events, threshold) {
    var accepted = 0, meet = space.outs.map(function () { return true; });
    events.forEach(function (e) {
      if (Rcmp(crProb(space, e.set), threshold) >= 0) {
        accepted += 1;
        meet = meet.map(function (b, k) { return b && e.set[k]; });
      }
    });
    return { accepted: accepted, of: events.length, pAll: crProb(space, meet), consistent: meet.indexOf(true) >= 0 };
  }
  /* n tickets, one wins; the claims are "ticket i loses", each (n-1)/n. */
  function crLottery(n, threshold) {
    var each = R(n - 1, n), all = Rcmp(each, threshold) >= 0;
    return { accepted: all ? n : 0, of: n, each: each, pAll: all ? R0 : R1, consistent: !all };
  }
  /* n independent claims, each p: their conjunction has probability p^n. */
  function crIndependent(n, p, threshold) {
    var all = Rcmp(p, threshold) >= 0;
    return { accepted: all ? n : 0, of: n, each: p, pAll: all ? Rpow(p, n) : R1, consistent: true };
  }
  function crSame(a, b) { for (var i = 0; i < a.length; i += 1) if (a[i] !== b[i]) return false; return true; }
  /* A Dutch book from typed credences: three checks, the first found wins. */
  function crBook(events, typed) {
    var i, j, k;
    for (i = 0; i < typed.length; i += 1) {
      var c = typed[i].c, nm = events[typed[i].k].name;
      if (Rcmp(c, R1) > 0) return { loss: Rsub(c, R1), why: 'c(' + nm + ') = ' + Rtext(c) + ' is above 1, so you pay that for a bet that returns at most 1' };
      if (Rsign(c) < 0) return { loss: Rneg(c), why: 'c(' + nm + ') = ' + ckFig(c) + ' is below 0, so you pay to give away a bet that cannot cost you' };
    }
    for (i = 0; i < typed.length; i += 1) {
      for (j = i + 1; j < typed.length; j += 1) {
        var A = events[typed[i].k].set, B = events[typed[j].k].set, comp = true;
        for (k = 0; k < A.length; k += 1) if (A[k] === B[k]) comp = false;
        if (!comp) continue;
        var s = Radd(typed[i].c, typed[j].c);
        if (!Requ(s, R1)) {
          return { loss: Rabs(Rsub(R1, s)), why: 'c(' + events[typed[i].k].name + ') + c(' + events[typed[j].k].name
            + ') = ' + Rtext(s) + ' for a complementary pair, and exactly one of the two happens' };
        }
      }
    }
    for (i = 0; i < typed.length; i += 1) {
      for (j = i + 1; j < typed.length; j += 1) {
        var X = events[typed[i].k].set, Y = events[typed[j].k].set, disjoint = true, union = [];
        for (k = 0; k < X.length; k += 1) { if (X[k] && Y[k]) disjoint = false; union.push(X[k] || Y[k]); }
        if (!disjoint) continue;
        for (k = 0; k < typed.length; k += 1) {
          if (k === i || k === j || !crSame(events[typed[k].k].set, union)) continue;
          var sum = Radd(typed[i].c, typed[j].c), d = Rsub(typed[k].c, sum);
          if (!Rzero(d)) {
            return { loss: Rabs(d), why: 'c(' + events[typed[k].k].name + ') = ' + Rtext(typed[k].c) + ' but c('
              + events[typed[i].k].name + ') + c(' + events[typed[j].k].name + ') = ' + Rtext(sum) + ' for disjoint events' };
          }
        }
      }
    }
    return null;
  }
"""

# ---------------------------------------------------------------------------
# series
# ---------------------------------------------------------------------------

SERIES_JS = r"""
  function srTwo(k) { var p = 1n; for (var i = 0; i < k; i += 1) p *= 2n; return p; }
  /* Each series as its exact terms 1..n, with its limit (null = none). */
  function srGeometric(a, r, n) {
    var terms = [], t = a;
    for (var k = 1; k <= n; k += 1) { terms.push(t); t = Rmul(t, r); }
    var limit = null;
    if (Rzero(a)) limit = R0;
    else if (Rcmp(Rabs(r), R1) < 0) limit = Rdiv(a, Rsub(R1, r));
    return { terms: terms, limit: limit };
  }
  function srHarmonic(n) {
    var terms = [];
    for (var k = 1; k <= n; k += 1) terms.push(R(1, k));
    return { terms: terms, limit: null };
  }
  /* Round k pays 2^k with probability 1/2^k, capped at the bankroll: the
     k-th term of the expectation is min(2^k, cap)/2^k. */
  function srPetersburg(n, cap) {
    var terms = [];
    for (var k = 1; k <= n; k += 1) {
      var pow = srTwo(k);
      terms.push(cap === null ? R1 : R(pow < cap ? pow : cap, pow));
    }
    var limit = null;
    if (cap !== null) {
      var K = 0;
      while (srTwo(K + 1) <= cap) K += 1;
      limit = Radd(R(K), R(cap, srTwo(K)));
    }
    return { terms: terms, limit: limit };
  }
  /* The lamp: switch k happens 1/2^k of a minute after switch k - 1. */
  function srLamp(n) {
    var terms = [];
    for (var k = 1; k <= n; k += 1) terms.push(R(1n, srTwo(k)));
    return { terms: terms, limit: R1 };
  }
  function srSummary(series) {
    var sums = [], s = R0;
    series.terms.forEach(function (t) { s = Radd(s, t); sums.push(s); });
    return { sums: sums, sum: s, limit: series.limit, remain: series.limit === null ? null : Rsub(series.limit, s) };
  }
"""

# ---------------------------------------------------------------------------
# game
# ---------------------------------------------------------------------------

GAME_JS = r"""
  function gaRead(v) {
    var rows = ckNames(v.rows, 'The row strategies', 4), cols = ckNames(v.cols, 'The column strategies', 4);
    if (rows.length < 2 || cols.length < 2) throw new Error('Each player needs at least two strategies');
    var lines = ckClean(v.matrix).split(';').map(function (r) { return r.trim(); });
    if (lines.length !== rows.length) throw new Error('The matrix has ' + ckCount(lines.length, 'row', 'rows') + ' and there are ' + rows.length + ' row strategies');
    var pay = lines.map(function (line, i) {
      var cells = ckTokens(line, /\s+/);
      if (cells.length !== cols.length) {
        throw new Error('The matrix is ragged: row ' + rows[i] + ' has ' + ckCount(cells.length, 'cell', 'cells') + ' and there are ' + cols.length + ' columns');
      }
      return cells.map(function (cell) {
        var p = cell.split(',');
        if (p.length !== 2) throw new Error('Each cell reads "row payoff,column payoff", and "' + cell + '" does not');
        return [ckNum(p[0], 'A row payoff'), ckNum(p[1], 'A column payoff')];
      });
    });
    return { rows: rows, cols: cols, pay: pay };
  }
  function gaBest(g) {
    var n = g.rows.length, m = g.cols.length, rb = [], cb = [], i, j;
    for (i = 0; i < n; i += 1) { rb.push([]); cb.push([]); }
    for (j = 0; j < m; j += 1) {
      var top = null;
      for (i = 0; i < n; i += 1) if (top === null || Rcmp(g.pay[i][j][0], top) > 0) top = g.pay[i][j][0];
      for (i = 0; i < n; i += 1) rb[i][j] = Requ(g.pay[i][j][0], top);
    }
    for (i = 0; i < n; i += 1) {
      var best = null;
      for (j = 0; j < m; j += 1) if (best === null || Rcmp(g.pay[i][j][1], best) > 0) best = g.pay[i][j][1];
      for (j = 0; j < m; j += 1) cb[i][j] = Requ(g.pay[i][j][1], best);
    }
    return { row: rb, col: cb };
  }
  function gaPure(g) {
    var b = gaBest(g), out = [];
    for (var i = 0; i < g.rows.length; i += 1) {
      for (var j = 0; j < g.cols.length; j += 1) if (b.row[i][j] && b.col[i][j]) out.push([i, j]);
    }
    return out;
  }
  /* Payoff to player p (0 row, 1 column) playing s against t. */
  function gaPay(g, p, s, t) { return p === 0 ? g.pay[s][t][0] : g.pay[t][s][1]; }
  /* s beats s2 for player p against every strategy in the given list:
     strict = > everywhere; weak = >= everywhere and > somewhere. */
  function gaBeats(g, p, s, s2, against, strict) {
    var some = false;
    for (var k = 0; k < against.length; k += 1) {
      var c = Rcmp(gaPay(g, p, s, against[k]), gaPay(g, p, s2, against[k]));
      if (c < 0 || (strict && c === 0)) return false;
      if (c > 0) some = true;
    }
    return some;
  }
  function gaRange(n) { var out = []; for (var i = 0; i < n; i += 1) out.push(i); return out; }
  /* The strategy of player p that beats every other one of theirs, or -1. */
  function gaDominant(g, p, strict) {
    var mine = gaRange(p === 0 ? g.rows.length : g.cols.length), theirs = gaRange(p === 0 ? g.cols.length : g.rows.length);
    for (var s = 0; s < mine.length; s += 1) {
      var all = true;
      for (var t = 0; t < mine.length; t += 1) if (t !== s && !gaBeats(g, p, s, t, theirs, strict)) all = false;
      if (all) return s;
    }
    return -1;
  }
  /* Iterated elimination of strictly dominated pure strategies. */
  function gaIesds(g) {
    var live = [gaRange(g.rows.length), gaRange(g.cols.length)], changed = true;
    while (changed) {
      changed = false;
      for (var p = 0; p < 2; p += 1) {
        var mine = live[p], theirs = live[1 - p], gone = -1;
        for (var a = 0; a < mine.length && gone < 0; a += 1) {
          for (var b = 0; b < mine.length; b += 1) {
            if (a !== b && gaBeats(g, p, mine[b], mine[a], theirs, true)) { gone = a; break; }
          }
        }
        if (gone >= 0) { mine.splice(gone, 1); changed = true; }
      }
    }
    return { rows: live[0], cols: live[1] };
  }
  function gaDomText(g) {
    var rd = gaDominant(g, 0, true), cd = gaDominant(g, 1, true);
    if (rd >= 0 && cd >= 0) {
      return g.rows[rd] === g.cols[cd] ? g.rows[rd] + ' dominates for both'
        : g.rows[rd] + ' dominates for row, ' + g.cols[cd] + ' for column';
    }
    if (rd >= 0) return g.rows[rd] + ' dominates for row';
    if (cd >= 0) return g.cols[cd] + ' dominates for column';
    var left = gaIesds(g);
    if (left.rows.length === g.rows.length && left.cols.length === g.cols.length) return 'none';
    if (left.rows.length === 1 && left.cols.length === 1) {
      return 'iterated elimination leaves (' + g.rows[left.rows[0]] + ', ' + g.cols[left.cols[0]] + ')';
    }
    return 'iterated elimination leaves rows ' + ckPick(g.rows, left.rows) + '; columns ' + ckPick(g.cols, left.cols);
  }
  /* The completely mixed equilibrium of a 2 x 2 game: p = P(row 1) makes the
     column player indifferent, q = P(column 1) makes the row player
     indifferent. null for a larger game, 'none' unless both lie in (0, 1). */
  function gaMixed(g) {
    if (g.rows.length !== 2 || g.cols.length !== 2) return null;
    var P = g.pay;
    var dp = Radd(Rsub(P[0][0][1], P[1][0][1]), Rsub(P[1][1][1], P[0][1][1]));
    var dq = Radd(Rsub(P[0][0][0], P[0][1][0]), Rsub(P[1][1][0], P[1][0][0]));
    if (Rzero(dp) || Rzero(dq)) return 'none';
    var p = Rdiv(Rsub(P[1][1][1], P[1][0][1]), dp), q = Rdiv(Rsub(P[1][1][0], P[0][1][0]), dq);
    if (Rsign(p) <= 0 || Rcmp(p, R1) >= 0 || Rsign(q) <= 0 || Rcmp(q, R1) >= 0) return 'none';
    return { p: p, q: q };
  }
  function gaParetoBeats(x, y) {
    var a = Rcmp(x[0], y[0]), b = Rcmp(x[1], y[1]);
    return a >= 0 && b >= 0 && (a > 0 || b > 0);
  }
  function gaEfficient(g) {
    var out = [], cells = [], i, j;
    for (i = 0; i < g.rows.length; i += 1) for (j = 0; j < g.cols.length; j += 1) cells.push(g.pay[i][j]);
    for (i = 0; i < g.rows.length; i += 1) {
      out.push([]);
      for (j = 0; j < g.cols.length; j += 1) {
        var me = g.pay[i][j];
        out[i][j] = !cells.some(function (c) { return gaParetoBeats(c, me); });
      }
    }
    return out;
  }
  function gaCell(g, c) { return '(' + g.rows[c[0]] + ', ' + g.cols[c[1]] + ')'; }
  /* Each Pareto-dominated pure equilibrium, with the first efficient cell
     (row-major) that dominates it. */
  function gaParetoText(g, eqs) {
    if (!eqs.length) return null;
    var eff = gaEfficient(g), out = [];
    eqs.forEach(function (e) {
      if (eff[e[0]][e[1]]) return;
      for (var i = 0; i < g.rows.length; i += 1) {
        for (var j = 0; j < g.cols.length; j += 1) {
          if (eff[i][j] && gaParetoBeats(g.pay[i][j], g.pay[e[0]][e[1]])) {
            out.push(gaCell(g, e) + ' is dominated by ' + gaCell(g, [i, j]));
            return;
          }
        }
      }
    });
    return out.length ? out.join('; ') : 'every equilibrium is efficient';
  }
"""

# ---------------------------------------------------------------------------
# iterated
# ---------------------------------------------------------------------------

ITERATED_JS = r"""
  var IT_STRATEGIES = ['ALLC', 'ALLD', 'TFT', 'GRIM', 'PAVLOV', 'TF2T', 'STFT'];
  function itRead(text) {
    var v = ckVec(text, 'the payoffs');
    if (v.length !== 4) throw new Error('The payoffs are four numbers, R S T P, and there are ' + v.length);
    var g = { R: v[0], S: v[1], T: v[2], P: v[3] };
    if (!(Rcmp(g.T, g.R) > 0 && Rcmp(g.R, g.P) > 0 && Rcmp(g.P, g.S) > 0)) {
      throw new Error('A prisoner\'s dilemma needs T, R, P, S in that order from largest, and these are R ' + ckFig(g.R)
        + ', S ' + ckFig(g.S) + ', T ' + ckFig(g.T) + ', P ' + ckFig(g.P));
    }
    if (Rcmp(Radd(g.R, g.R), Radd(g.T, g.S)) <= 0) {
      throw new Error('A repeated dilemma needs 2R to exceed T + S, or taking turns to exploit beats cooperating');
    }
    return g;
  }
  function itMove(name, mine, theirs) {
    var t = mine.length;
    if (name === 'ALLC') return 'C';
    if (name === 'ALLD') return 'D';
    if (name === 'TFT') return t === 0 ? 'C' : theirs[t - 1];
    if (name === 'STFT') return t === 0 ? 'D' : theirs[t - 1];
    if (name === 'GRIM') return theirs.indexOf('D') >= 0 ? 'D' : 'C';
    if (name === 'PAVLOV') return t === 0 ? 'C' : (mine[t - 1] === theirs[t - 1] ? 'C' : 'D');
    if (name === 'TF2T') return t >= 2 && theirs[t - 1] === 'D' && theirs[t - 2] === 'D' ? 'D' : 'C';
    throw new Error('no strategy ' + name);
  }
  function itPayoff(g, me, them) {
    if (me === 'C') return them === 'C' ? g.R : g.S;
    return them === 'C' ? g.T : g.P;
  }
  function itPlay(g, a, b, rounds) {
    var ma = [], mb = [], sa = R0, sb = R0;
    for (var k = 0; k < rounds; k += 1) {
      var x = itMove(a, ma, mb), y = itMove(b, mb, ma);
      ma.push(x); mb.push(y);
      sa = Radd(sa, itPayoff(g, x, y)); sb = Radd(sb, itPayoff(g, y, x));
    }
    return { a: ma, b: mb, sa: sa, sb: sb };
  }
  /* Round robin: every strategy meets every strategy, itself included, once;
     a strategy's total is the sum of its own scores. */
  function itTournament(g, rounds) {
    var totals = IT_STRATEGIES.map(function () { return R0; });
    for (var i = 0; i < IT_STRATEGIES.length; i += 1) {
      for (var j = 0; j < IT_STRATEGIES.length; j += 1) {
        totals[i] = Radd(totals[i], itPlay(g, IT_STRATEGIES[i], IT_STRATEGIES[j], rounds).sa);
      }
    }
    return { totals: totals, best: ckBest(totals, 1) };
  }
  function itThresholds(g) {
    var grim = Rdiv(Rsub(g.T, g.R), Rsub(g.T, g.P)), tft2 = Rdiv(Rsub(g.T, g.R), Rsub(g.R, g.S));
    return { grim: grim, tft: Rcmp(tft2, grim) > 0 ? tft2 : grim };
  }
"""

# ---------------------------------------------------------------------------
# commons
# ---------------------------------------------------------------------------

COMMONS_JS = r"""
  /* An exact expression in k and n: numbers, k, n, + - * / ^ (a whole-number
     exponent), brackets, and implicit multiplication (5k, 2(k + 1)).
     Compiled once to a tree; evaluated exactly; an undefined value is null. */
  function cmLex(text) {
    var s = ckClean(text).replace(/[×·]/g, '*'), out = [], i = 0;
    if (!s) throw new Error('A payoff is empty');
    while (i < s.length) {
      var ch = s.charAt(i);
      if (/\s/.test(ch)) { i += 1; continue; }
      var m = /^\d+(\.\d+)?/.exec(s.slice(i));
      if (m) { out.push({ t: 'num', v: Rparse(m[0]) }); i += m[0].length; continue; }
      if (ch === 'k' || ch === 'n') { out.push({ t: 'var', v: ch }); i += 1; continue; }
      if ('+-*/^()'.indexOf(ch) >= 0) { out.push({ t: ch }); i += 1; continue; }
      throw new Error('A payoff may use numbers, k, n, + - * / ^ and brackets, and "' + ch + '" is none of them');
    }
    return out;
  }
  function cmParse(text) {
    var toks = cmLex(text), pos = 0;
    function peek() { return toks[pos] || { t: 'end' }; }
    function expr() {
      var left = term();
      while (peek().t === '+' || peek().t === '-') { var op = peek().t; pos += 1; left = [op, left, term()]; }
      return left;
    }
    function term() {
      var left = unary();
      for (;;) {
        var t = peek().t;
        if (t === '*' || t === '/') { pos += 1; left = [t, left, unary()]; }
        else if (t === 'num' || t === 'var' || t === '(') left = ['*', left, power()];
        else return left;
      }
    }
    function unary() {
      if (peek().t === '-') { pos += 1; return ['neg', unary()]; }
      if (peek().t === '+') { pos += 1; return unary(); }
      return power();
    }
    function power() {
      var base = atom();
      if (peek().t === '^') { pos += 1; return ['^', base, unary()]; }
      return base;
    }
    function atom() {
      var t = peek();
      if (t.t === 'num') { pos += 1; return ['num', t.v]; }
      if (t.t === 'var') { pos += 1; return ['var', t.v]; }
      if (t.t === '(') {
        pos += 1;
        var e = expr();
        if (peek().t !== ')') throw new Error('A payoff has an unclosed bracket');
        pos += 1;
        return e;
      }
      throw new Error('A payoff has a gap where a number, k, n or a bracket should be');
    }
    var tree = expr();
    if (pos !== toks.length) throw new Error('A payoff has something left over after it ends');
    return tree;
  }
  function cmEval(tree, env) {
    var op = tree[0], a, b;
    if (op === 'num') return tree[1];
    if (op === 'var') return env[tree[1]];
    if (op === 'neg') { a = cmEval(tree[1], env); return a === null ? null : Rneg(a); }
    a = cmEval(tree[1], env); b = cmEval(tree[2], env);
    if (a === null || b === null) return null;
    if (op === '+') return Radd(a, b);
    if (op === '-') return Rsub(a, b);
    if (op === '*') return Rmul(a, b);
    if (op === '/') return Rzero(b) ? null : Rdiv(a, b);
    if (!Rint(b) || b.n > 20n || b.n < -20n) return null;
    if (Rzero(a) && b.n < 0n) return null;
    return Rpow(a, Number(b.n));
  }
  /* C(k) and D(k) for k = 0..n-1 others cooperating. */
  function cmTable(pc, pd, n) {
    var C = [], D = [], N = R(n);
    for (var k = 0; k < n; k += 1) {
      var c = cmEval(pc, { k: R(k), n: N }), d = cmEval(pd, { k: R(k), n: N });
      if (c === null || d === null) return { bad: k };
      C.push(c); D.push(d);
    }
    return { C: C, D: D };
  }
  /* Defect dominates when D(k) >= C(k) for every k and > for some. */
  function cmDominance(t) {
    var dWorse = false, cWorse = false;
    for (var k = 0; k < t.C.length; k += 1) {
      var c = Rcmp(t.D[k], t.C[k]);
      if (c < 0) dWorse = true;
      if (c > 0) cWorse = true;
    }
    if (cWorse && !dWorse) return 'Defect dominates';
    if (dWorse && !cWorse) return 'Cooperate dominates';
    return 'neither';
  }
  /* k* cooperators is an equilibrium when no cooperator gains by switching
     (C(k*-1) >= D(k*-1)) and no defector does (D(k*) >= C(k*)). */
  function cmEquilibria(t, n) {
    var out = [];
    for (var k = 0; k <= n; k += 1) {
      var okC = k === 0 || Rcmp(t.C[k - 1], t.D[k - 1]) >= 0;
      var okD = k === n || Rcmp(t.D[k], t.C[k]) >= 0;
      if (okC && okD) out.push(k);
    }
    return out;
  }
  /* The total payoff with k cooperators: k C(k-1) + (n-k) D(k). */
  function cmWelfare(t, n, k) {
    var w = R0;
    if (k > 0) w = Radd(w, Rmul(R(k), t.C[k - 1]));
    if (k < n) w = Radd(w, Rmul(R(n - k), t.D[k]));
    return w;
  }
  function cmOptimum(t, n) {
    var totals = [];
    for (var k = 0; k <= n; k += 1) totals.push(cmWelfare(t, n, k));
    var best = ckBest(totals, 1);
    return { ks: best, total: totals[best[0]], totals: totals };
  }
  function cmUniversal(t, n) {
    return { alone: Rsub(t.D[n - 1], t.C[n - 1]), everyone: Rsub(t.D[0], t.C[n - 1]) };
  }
  /* Replicator steps x' = x fC / (x fC + (1-x) fD), fitness evaluated at the
     rational k = x (n-1). Exact; stops with a reason at a negative fitness, a
     mean fitness that is not positive, or a share past 600 digits. */
  function cmReplicate(pc, pd, n, x0, gens) {
    var x = x0, N = R(n);
    for (var g = 0; g < gens; g += 1) {
      var k = Rmul(x, R(n - 1));
      var fc = cmEval(pc, { k: k, n: N }), fd = cmEval(pd, { k: k, n: N });
      if (fc === null || fd === null) return { stop: g, why: 'a payoff is undefined at k = ' + Rtext(k) };
      if (Rsign(fc) < 0 || Rsign(fd) < 0) return { stop: g, why: 'the replicator needs payoffs of at least 0, and generation ' + g + ' has a negative one' };
      var mean = Radd(Rmul(x, fc), Rmul(Rsub(R1, x), fd));
      if (Rsign(mean) <= 0) return { stop: g, why: 'the mean payoff at generation ' + g + ' is 0, so the next shares are undefined' };
      x = Rdiv(Rmul(x, fc), mean);
      if (ckDigits(x) > 600) return { stop: g + 1, why: 'the exact share after generation ' + (g + 1) + ' has more than 600 digits' };
    }
    return { x: x };
  }
"""

# ---------------------------------------------------------------------------
# vote
# ---------------------------------------------------------------------------

VOTE_JS = r"""
  /* Ranking profiles: "4: A B C; 3: B C A". Candidates are kept in
     alphabetical order, which is the order every tie and list prints in. */
  function voReadRanking(text) {
    var groups = [], cands = null, voters = 0;
    ckTokens(text, ';').forEach(function (part) {
      var at = part.indexOf(':');
      if (at < 0) throw new Error('Each group reads "count: best ... worst", and "' + part + '" has no colon');
      var cs = part.slice(0, at).trim();
      if (!/^\d+$/.test(cs) || parseInt(cs, 10) < 1) throw new Error('A group count should be a whole number of voters, and "' + cs + '" is not');
      var names = ckTokens(part.slice(at + 1), /\s+/), sorted = names.slice().sort();
      for (var i = 1; i < sorted.length; i += 1) if (sorted[i] === sorted[i - 1]) throw new Error('A ranking lists ' + sorted[i] + ' twice');
      if (cands === null) cands = sorted;
      if (sorted.join(' ') !== cands.join(' ')) throw new Error('Every ranking must rank the same candidates (' + cands.join(', ') + ')');
      groups.push({ count: parseInt(cs, 10), order: names.map(function (n) { return cands.indexOf(n); }) });
      voters += parseInt(cs, 10);
    });
    if (!groups.length) throw new Error('The profile is empty');
    if (cands.length < 2 || cands.length > 5) throw new Error('This lab takes 2 to 5 candidates, and there are ' + cands.length);
    if (voters > 60) throw new Error('This lab takes at most 60 voters, and there are ' + voters);
    return { cands: cands, groups: groups, voters: voters };
  }
  /* The groups with the struck-out candidates removed from every ranking. */
  function voRestrict(groups, live) {
    return groups.map(function (g) {
      return { count: g.count, order: g.order.filter(function (c) { return live[c]; }) };
    });
  }
  /* N[a][b] = voters ranking a above b. */
  function voMargins(groups, m) {
    var N = [], a, b;
    for (a = 0; a < m; a += 1) { N.push([]); for (b = 0; b < m; b += 1) N[a].push(0); }
    groups.forEach(function (g) {
      for (var i = 0; i < g.order.length; i += 1) for (var j = i + 1; j < g.order.length; j += 1) N[g.order[i]][g.order[j]] += g.count;
    });
    return N;
  }
  function voLiveList(live) { var out = []; for (var i = 0; i < live.length; i += 1) if (live[i]) out.push(i); return out; }
  function voFirsts(groups, m) {
    var f = []; for (var i = 0; i < m; i += 1) f.push(0);
    groups.forEach(function (g) { if (g.order.length) f[g.order[0]] += g.count; });
    return f;
  }
  function voMaxSet(list, score) {
    var best = null, out = [];
    list.forEach(function (c) { if (best === null || score[c] > best) { best = score[c]; out = [c]; } else if (score[c] === best) out.push(c); });
    return out;
  }
  function voHead(N, a, b) { return N[a][b] > N[b][a] ? [a] : (N[a][b] < N[b][a] ? [b] : [a, b]); }
  function voUnion(sets) {
    var seen = {}, out = [];
    sets.forEach(function (s) { s.forEach(function (c) { if (!seen[c]) { seen[c] = true; out.push(c); } }); });
    return out.sort(function (x, y) { return x - y; });
  }
  /* Instant runoff. A tie for elimination is followed down every branch and
     the possible winners are reported together, never broken silently. */
  function voIrv(groups, live, voters, memo) {
    var key = live.join(','), list = voLiveList(live);
    if (memo[key]) return memo[key];
    var out;
    if (list.length === 1) out = list;
    else {
      var f = voFirsts(voRestrict(groups, live), live.length), lead = voMaxSet(list, f);
      if (lead.length === 1 && f[lead[0]] * 2 > voters) out = lead;
      else {
        var low = null, losers = [];
        list.forEach(function (c) { if (low === null || f[c] < low) { low = f[c]; losers = [c]; } else if (f[c] === low) losers.push(c); });
        if (losers.length === list.length) out = list;
        else {
          out = voUnion(losers.map(function (c) {
            var next = live.slice(); next[c] = false;
            return voIrv(groups, next, voters, memo);
          }));
        }
      }
    }
    memo[key] = out;
    return out;
  }
  /* Winners of the rule among the live candidates, as sorted indices. A tie is
     every tied candidate; the runoff follows every way of filling a tied
     second place. */
  function voWinners(prof, live, rule) {
    var m = prof.cands.length, list = voLiveList(live), groups = voRestrict(prof.groups, live), score = [], c, d;
    if (list.length === 1) return list;
    var N = voMargins(groups, m);
    if (rule === 'plurality') return voMaxSet(list, voFirsts(groups, m));
    if (rule === 'borda') {
      for (c = 0; c < m; c += 1) score.push(0);
      groups.forEach(function (g) { g.order.forEach(function (x, pos) { score[x] += g.count * (g.order.length - 1 - pos); }); });
      return voMaxSet(list, score);
    }
    if (rule === 'condorcet' || rule === 'copeland') {
      var winners = [];
      for (c = 0; c < m; c += 1) score.push(0);
      list.forEach(function (x) {
        var all = true;
        list.forEach(function (y) {
          if (x === y) return;
          if (N[x][y] > N[y][x]) score[x] += 1;
          else { all = false; if (N[x][y] < N[y][x]) score[x] -= 1; }
        });
        if (all) winners.push(x);
      });
      return rule === 'condorcet' ? winners : voMaxSet(list, score);
    }
    if (rule === 'runoff') {
      var f = voFirsts(groups, m), top = voMaxSet(list, f), pairs = [];
      if (top.length >= 2) {
        for (c = 0; c < top.length; c += 1) for (d = c + 1; d < top.length; d += 1) pairs.push([top[c], top[d]]);
      } else {
        var rest = list.filter(function (x) { return x !== top[0]; });
        voMaxSet(rest, f).forEach(function (x) { pairs.push([top[0], x]); });
      }
      return voUnion(pairs.map(function (p) { return voHead(N, p[0], p[1]); }));
    }
    if (rule === 'irv') return voIrv(prof.groups, live, prof.voters, {});
    throw new Error('no rule ' + rule);
  }
  function voWinnerText(prof, w) {
    if (!w.length) return 'none';
    return w.length === 1 ? prof.cands[w[0]] : ckPick(prof.cands, w) + ' (tie)';
  }
  /* The Condorcet winner; else a majority cycle inside the top cycle (the
     candidates that reach every other through "not beaten by"), longest
     first, starting from the alphabetically first; else none. */
  function voCondorcetText(prof, live) {
    var m = prof.cands.length, list = voLiveList(live), N = voMargins(voRestrict(prof.groups, live), m);
    var cw = voWinners(prof, live, 'condorcet');
    if (cw.length === 1) return prof.cands[cw[0]];
    var reach = {};
    list.forEach(function (x) {
      var seen = {}, stack = [x];
      seen[x] = true;
      while (stack.length) {
        var y = stack.pop();
        list.forEach(function (z) { if (!seen[z] && N[y][z] >= N[z][y]) { seen[z] = true; stack.push(z); } });
      }
      reach[x] = seen;
    });
    var top = list.filter(function (x) { return list.every(function (z) { return reach[x][z]; }); });
    function beats(a, b) { return N[a][b] > N[b][a]; }
    var found = null;
    function walk(path, used, want) {
      if (found) return;
      if (path.length === want) {
        if (beats(path[path.length - 1], path[0])) found = path.slice();
        return;
      }
      top.forEach(function (z) {
        if (found || used[z] || !beats(path[path.length - 1], z)) return;
        used[z] = true; path.push(z); walk(path, used, want); path.pop(); used[z] = false;
      });
    }
    for (var len = top.length; len >= 3 && !found; len -= 1) {
      top.forEach(function (s) { if (!found) { var u = {}; u[s] = true; walk([s], u, len); } });
    }
    if (!found) return 'none';
    return 'cycle: ' + found.concat([found[0]]).map(function (c) { return prof.cands[c]; }).join(' > ');
  }
  function voSame(a, b) { return a.length === b.length && a.every(function (x, i) { return x === b[i]; }); }
  /* IIA: strike out one losing candidate and recompute the winners. The last argument is
     that candidate, or -1 to try every loser in alphabetical order. */
  function voIia(prof, rule, only) {
    var full = prof.cands.map(function () { return true; }), w = voWinners(prof, full, rule);
    var tryList = only >= 0 ? [only] : prof.cands.map(function (c, i) { return i; });
    for (var k = 0; k < tryList.length; k += 1) {
      var x = tryList[k];
      if (w.indexOf(x) >= 0) { if (only >= 0) return { winner: true }; continue; }
      var live = full.slice(); live[x] = false;
      if (!voSame(voWinners(prof, live, rule), w)) return { violated: x };
    }
    return { holds: true };
  }
  function voPermutations(items) {
    if (items.length <= 1) return [items.slice()];
    var out = [];
    items.forEach(function (x, i) {
      var rest = items.slice(0, i).concat(items.slice(i + 1));
      voPermutations(rest).forEach(function (p) { out.push([x].concat(p)); });
    });
    return out;
  }
  /* Manipulation: every voter sharing a ranking switches together to each
     other ranking in turn; the first switch that elects a single candidate
     they rank above every sincere winner is reported. null = no sincere
     winner to improve on. */
  function voManipulate(prof, live, rule) {
    var w = voWinners(prof, live, rule);
    if (!w.length) return null;
    var merged = [], keyOf = {};
    prof.groups.forEach(function (g) {
      var key = g.order.filter(function (c) { return live[c]; }).join(',');
      if (keyOf[key] === undefined) { keyOf[key] = merged.length; merged.push({ count: 0, order: g.order }); }
      merged[keyOf[key]].count += g.count;
    });
    var perms = voPermutations(voLiveList(live));
    function said(o) { return o.filter(function (c) { return live[c]; }).map(function (c) { return prof.cands[c]; }).join(' '); }
    for (var gi = 0; gi < merged.length; gi += 1) {
      var g = merged[gi], pos = {}, sincere = said(g.order);
      g.order.filter(function (c) { return live[c]; }).forEach(function (c, i) { pos[c] = i; });
      for (var pi = 0; pi < perms.length; pi += 1) {
        var perm = perms[pi];
        if (said(perm) === sincere) continue;
        var groups = merged.map(function (h, hi) { return hi === gi ? { count: h.count, order: perm } : h; });
        var w2 = voWinners({ cands: prof.cands, groups: groups, voters: prof.voters }, live, rule);
        if (w2.length === 1 && w.every(function (x) { return pos[w2[0]] < pos[x]; })) {
          return { from: sincere, to: said(perm) };
        }
      }
    }
    return 'none';
  }
  /* Judgment: "p q p∧q: 1 1 1; 1 0 0; 0 1 0" -- premises, then the
     conclusion formula; one row per judge. */
  function voFormula(text, atoms) {
    var s = ckClean(text), toks = [], i = 0;
    while (i < s.length) {
      var ch = s.charAt(i), m = /^[A-Za-z][A-Za-z0-9]*/.exec(s.slice(i));
      if (m) {
        if (atoms.indexOf(m[0]) < 0) throw new Error('The conclusion uses ' + m[0] + ', which is not one of the premises');
        toks.push({ t: 'atom', v: atoms.indexOf(m[0]) }); i += m[0].length; continue;
      }
      if ('&∧'.indexOf(ch) >= 0) toks.push({ t: '&' });
      else if ('|∨'.indexOf(ch) >= 0) toks.push({ t: '|' });
      else if ('!¬'.indexOf(ch) >= 0) toks.push({ t: '!' });
      else if (ch === '→') toks.push({ t: 'imp' });
      else if (ch === '(' || ch === ')') toks.push({ t: ch });
      else throw new Error('The conclusion may use premise names, ∧ ∨ ¬ → and brackets, and "' + ch + '" is none of them');
      i += 1;
    }
    var pos = 0;
    function peek() { return (toks[pos] || { t: 'end' }).t; }
    function imp() { var a = or(); if (peek() === 'imp') { pos += 1; return ['imp', a, imp()]; } return a; }
    function or() { var a = and(); while (peek() === '|') { pos += 1; a = ['|', a, and()]; } return a; }
    function and() { var a = not(); while (peek() === '&') { pos += 1; a = ['&', a, not()]; } return a; }
    function not() { if (peek() === '!') { pos += 1; return ['!', not()]; } return atom(); }
    function atom() {
      var t = toks[pos];
      if (t && t.t === 'atom') { pos += 1; return ['atom', t.v]; }
      if (t && t.t === '(') {
        pos += 1;
        var e = imp();
        if (peek() !== ')') throw new Error('The conclusion has an unclosed bracket');
        pos += 1;
        return e;
      }
      throw new Error('The conclusion has a gap where a premise or a bracket should be');
    }
    var tree = imp();
    if (pos !== toks.length) throw new Error('The conclusion has something left over after it ends');
    return tree;
  }
  function voTruth(tree, vals) {
    var op = tree[0];
    if (op === 'atom') return vals[tree[1]];
    if (op === '!') return !voTruth(tree[1], vals);
    if (op === '&') return voTruth(tree[1], vals) && voTruth(tree[2], vals);
    if (op === '|') return voTruth(tree[1], vals) || voTruth(tree[2], vals);
    return !voTruth(tree[1], vals) || voTruth(tree[2], vals);
  }
  function voReadJudgment(text) {
    var s = ckClean(text), at = s.indexOf(':');
    if (at < 0) throw new Error('A judgment profile reads "p q p∧q: 1 1 1; 1 0 0", and this one has no colon');
    var head = ckTokens(s.slice(0, at), /\s+/);
    if (head.length < 2) throw new Error('Name at least one premise and then the conclusion formula');
    var atoms = head.slice(0, -1);
    atoms.forEach(function (a, i) {
      if (!/^[A-Za-z][A-Za-z0-9]*$/.test(a)) throw new Error('"' + a + '" is not a premise name');
      if (atoms.indexOf(a) !== i) throw new Error('The premise ' + a + ' is named twice');
    });
    if (atoms.length > 6) throw new Error('This lab takes at most 6 premises');
    var formula = voFormula(head[head.length - 1], atoms), rows = [];
    ckTokens(s.slice(at + 1), ';').forEach(function (r, i) {
      var vals = ckTokens(r, /\s+/);
      if (vals.length !== atoms.length && vals.length !== atoms.length + 1) {
        throw new Error('Judge ' + (i + 1) + ' gives ' + vals.length + ' verdicts; each judge gives one per premise, and may add the conclusion');
      }
      var b = vals.map(function (x) {
        if (x !== '0' && x !== '1') throw new Error('Judge ' + (i + 1) + ' has a verdict "' + x + '"; verdicts are 1 or 0');
        return x === '1';
      });
      var concl = voTruth(formula, b.slice(0, atoms.length));
      if (b.length > atoms.length && b[atoms.length] !== concl) {
        throw new Error('Judge ' + (i + 1) + '\'s verdict on the conclusion contradicts their own premises');
      }
      rows.push({ premises: b.slice(0, atoms.length), concl: concl });
    });
    if (!rows.length) throw new Error('There are no judges');
    if (rows.length > 59) throw new Error('This lab takes at most 59 judges');
    if (rows.length % 2 === 0) throw new Error('With ' + rows.length + ' judges a majority can tie; this lab takes an odd number');
    return { atoms: atoms, formula: formula, rows: rows };
  }
  function voJudge(j) {
    var half = j.rows.length / 2, maj = j.atoms.map(function (a, i) {
      return j.rows.filter(function (r) { return r.premises[i]; }).length > half;
    });
    var concl = j.rows.filter(function (r) { return r.concl; }).length > half;
    return { premises: maj, premiseBased: voTruth(j.formula, maj), conclusionBased: concl };
  }
  /* Jury: "n=3 p=3/5". */
  function voReadJury(text) {
    var m = /^n\s*=\s*(\d+)\s+p\s*=\s*(\S+)$/.exec(ckClean(text));
    if (!m) throw new Error('A jury reads "n=3 p=3/5"');
    var n = parseInt(m[1], 10);
    if (n < 1 || n > 101) throw new Error('This lab takes 1 to 101 jurors, and n is ' + n);
    return { n: n, p: ckUnit(ckNum(m[2], 'The competence p'), 'The competence p') };
  }
  function voBinom(n, k) { var r = 1n; for (var i = 1; i <= k; i += 1) r = r * BigInt(n - k + i) / BigInt(i); return r; }
  /* P(a strict majority is right) and, for odd n, P(one vote is decisive). */
  function voJury(n, p) {
    var q = Rsub(R1, p), sum = R0;
    for (var k = Math.floor(n / 2) + 1; k <= n; k += 1) sum = Radd(sum, Rmul(R(voBinom(n, k)), Rmul(Rpow(p, k), Rpow(q, n - k))));
    var pivot = null;
    if (n % 2 === 1) { var h = (n - 1) / 2; pivot = Rmul(R(voBinom(n - 1, h)), Rpow(Rmul(p, q), h)); }
    return { correct: sum, pivot: pivot };
  }
"""

# ---------------------------------------------------------------------------
# aggregate
# ---------------------------------------------------------------------------

AGGREGATE_JS = r"""
  function agTotal(v) { return ckSum(v); }
  /* g(x) = x up to the knee, knee + (x - knee)/2 above it. */
  function agPrior(v, knee) {
    return ckSum(v.map(function (x) { return Rcmp(x, knee) <= 0 ? x : Radd(knee, Rdiv(Rsub(x, knee), R(2))); }));
  }
  function agMin(v) { var m = v[0]; v.forEach(function (x) { if (Rcmp(x, m) < 0) m = x; }); return m; }
  function agSorted(v) { return v.slice().sort(Rcmp); }
  function agOrdinal(i) { return i === 1 ? '2nd' : (i === 2 ? '3rd' : (i + 1) + 'th'); }
  /* Gini = sum over all ordered pairs |xi - xj| / (2 n^2 mean); null when
     the mean is not positive. */
  function agGini(v) {
    var n = v.length, mean = Rdiv(ckSum(v), R(n));
    if (Rsign(mean) <= 0) return null;
    var s = R0;
    for (var i = 0; i < n; i += 1) for (var j = 0; j < n; j += 1) s = Radd(s, Rabs(Rsub(v[i], v[j])));
    return Rdiv(s, Rmul(R(2 * n * n), mean));
  }
  /* The smallest n with n * eps > total(A). */
  function agRepugnant(A, eps) {
    var q = Rdiv(agTotal(A), eps), fl = q.n / q.d;
    if (q.n < 0n && fl * q.d !== q.n) fl -= 1n;
    var n = fl + 1n;
    return n < 1n ? 1n : n;
  }
  /* {verdict: 1 (A better) | -1 | 0, scores: text}, or {need: why}. */
  function agCompare(A, B, rule, par) {
    var a, b;
    if (rule === 'total' || rule === 'average' || rule === 'prioritarian' || rule === 'maximin') {
      if (rule === 'prioritarian' && par.knee === null) return { need: 'The prioritarian rule needs a knee' };
      var score = function (v) {
        return rule === 'total' ? agTotal(v) : (rule === 'average' ? Rdiv(agTotal(v), R(v.length))
          : (rule === 'prioritarian' ? agPrior(v, par.knee) : agMin(v)));
      };
      a = score(A); b = score(B);
      return { verdict: Rcmp(a, b), scores: ckFig(a) + ' vs ' + ckFig(b) };
    }
    if (rule === 'leximin') {
      if (A.length !== B.length) return { need: 'Leximin compares populations of the same size, and these have ' + A.length + ' and ' + B.length };
      var sa = agSorted(A), sb = agSorted(B);
      for (var i = 0; i < sa.length; i += 1) {
        var c = Rcmp(sa[i], sb[i]);
        if (c !== 0) return { verdict: c, scores: (i === 0 ? 'worst ' : agOrdinal(i) + ' worst ') + ckFig(sa[i]) + ' vs ' + ckFig(sb[i]) };
      }
      return { verdict: 0, scores: 'equal at every rank' };
    }
    if (rule === 'sufficientarian') {
      if (par.thresh === null) return { need: 'The sufficientarian rule needs a threshold' };
      var t = par.thresh;
      var below = function (v) { return v.filter(function (x) { return Rcmp(x, t) < 0; }).length; };
      var short = function (v) { return ckSum(v.map(function (x) { return Rcmp(x, t) < 0 ? Rsub(t, x) : R0; })); };
      var ba = below(A), bb = below(B);
      if (ba !== bb) return { verdict: ba < bb ? 1 : -1, scores: 'below ' + ba + ' vs ' + bb };
      var fa = short(A), fb = short(B);
      if (!Requ(fa, fb)) return { verdict: -Rcmp(fa, fb), scores: 'shortfall ' + Rtext(fa) + ' vs ' + Rtext(fb) };
      a = agTotal(A); b = agTotal(B);
      return { verdict: Rcmp(a, b), scores: 'total ' + ckFig(a) + ' vs ' + ckFig(b) };
    }
    return { need: 'There is no rule called ' + rule };
  }
"""

# ---------------------------------------------------------------------------
# simpson
# ---------------------------------------------------------------------------

SIMPSON_JS = r"""
  function siRead(namesText, tableText) {
    var names = ckNames(namesText, 'The two treatments');
    if (names.length !== 2) throw new Error('Name exactly two treatments, and there are ' + names.length);
    var groups = ckTokens(tableText, ';').map(function (part) {
      var at = part.indexOf(':');
      if (at < 0) throw new Error('Each group reads "name: s/t s/t", and "' + part + '" has no colon');
      var name = part.slice(0, at).trim(), cells = ckTokens(part.slice(at + 1), /\s+/);
      if (!name) throw new Error('A group has no name');
      if (cells.length !== 2) throw new Error('The group ' + name + ' needs two cells, successes/trials for each treatment');
      var counts = cells.map(function (c) {
        var m = /^(\d+)\/(\d+)$/.exec(c);
        if (!m) throw new Error('"' + c + '" in ' + name + ' should read successes/trials, such as 81/87');
        var s = BigInt(m[1]), t = BigInt(m[2]);
        if (t === 0n || s > t) throw new Error('"' + c + '" in ' + name + ' needs at least one trial and no more successes than trials');
        return { s: s, t: t };
      });
      return { name: name, a: counts[0], b: counts[1] };
    });
    if (groups.length !== 2) throw new Error('This lab compares exactly two groups, and there are ' + groups.length);
    return { names: names, groups: groups };
  }
  function siRate(c) { return R(c.s, c.t); }
  function siWord(names, c) { return c > 0 ? names[0] + ' higher' : (c < 0 ? names[1] + ' higher' : 'equal'); }
  /* Pooled counts, within-group comparisons, the standardised rates (each
     group weighted by its share of all trials) and whether the pooled
     comparison reverses the groups. */
  function siSolve(inst) {
    var g = inst.groups;
    var pa = { s: g[0].a.s + g[1].a.s, t: g[0].a.t + g[1].a.t }, pb = { s: g[0].b.s + g[1].b.s, t: g[0].b.t + g[1].b.t };
    var all = pa.t + pb.t, sa = R0, sb = R0;
    g.forEach(function (x) {
      var w = R(x.a.t + x.b.t, all);
      sa = Radd(sa, Rmul(w, siRate(x.a))); sb = Radd(sb, Rmul(w, siRate(x.b)));
    });
    var within = g.map(function (x) { return Rcmp(siRate(x.a), siRate(x.b)); });
    var pooled = Rcmp(siRate(pa), siRate(pb));
    var reversal = pooled !== 0 && within[0] !== pooled && within[1] !== pooled
      && (within[0] === -pooled || within[1] === -pooled);
    return { pa: pa, pb: pb, pooled: pooled, within: within, sa: sa, sb: sb, std: Rcmp(sa, sb), reversal: reversal };
  }
"""

# ---------------------------------------------------------------------------
# Python side: validation and the furniture every mode shares
# ---------------------------------------------------------------------------

_NUM_RE = re.compile(r"[+-]?\d+/\d+|[+-]?\d+|[+-]?\d*\.\d+")
_BAD_NAME = re.compile(r'[,;:=<>&"*\\]')


def _q(where, value, what="a number"):
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


def _vec(where, values, what, length=None):
    if not isinstance(values, (list, tuple)) or not values:
        raise ValueError("%s: %s should be a non-empty list" % (where, what))
    out = [_q(where, v, what) for v in values]
    if length is not None and len(out) != length:
        raise ValueError("%s: %s has %d entries, it needs %d" % (where, what, len(out), length))
    return out


def _dist(where, values, what, length=None):
    out = _vec(where, values, what, length)
    total = sum(f for f, _ in out)
    if any(f < 0 for f, _ in out) or total != 1:
        raise ValueError("%s: %s must be non-negative and sum to exactly 1 (they sum to %s)" % (where, what, total))
    return out


def _name(where, value, what, spaces=True):
    s = str(value).strip() if isinstance(value, (str, int)) and not isinstance(value, bool) else ""
    if not s or _BAD_NAME.search(s) or (not spaces and re.search(r"\s", s)):
        raise ValueError("%s: %s %r is not a usable name (no , ; : = < > & * or quotes%s)"
                         % (where, what, value, "" if spaces else ", no spaces"))
    return s


def _names(where, values, what, lo, hi, spaces=True):
    if not isinstance(values, (list, tuple)):
        raise ValueError("%s: %s should be a list" % (where, what))
    out = [_name(where, v, what, spaces) for v in values]
    if not lo <= len(out) <= hi:
        raise ValueError("%s: %d %s, this mode takes %d to %d" % (where, len(out), what, lo, hi))
    if len(set(out)) != len(out):
        raise ValueError("%s: %s repeat a name" % (where, what))
    return out


def _txt(pairs):
    return " ".join(t for _, t in pairs)


def _int(where, value, what, lo, hi):
    if isinstance(value, bool) or not isinstance(value, int) or not lo <= value <= hi:
        raise ValueError("%s: %s should be a whole number from %d to %d, not %r" % (where, what, lo, hi, value))
    return value


def _presets(cfg, mode, convert, redraw_keys=()):
    """(instance table, menu pairs, expect by preset id, the chosen id)."""
    presets = cfg.get("presets")
    if not isinstance(presets, list) or not presets:
        raise ValueError("choicekit/%s: cfg['presets'] must be a non-empty list of instances" % mode)
    table, menu, expect = {}, [], {}
    for p in presets:
        pid = p.get("id") if isinstance(p, dict) else None
        if not isinstance(pid, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", pid):
            raise ValueError("choicekit/%s: every preset needs an id of lowercase letters, digits and "
                             "hyphens, not %r" % (mode, pid))
        where = "choicekit/%s preset %r" % (mode, pid)
        if pid in table:
            raise ValueError("%s: the id is used twice" % where)
        label = p.get("label")
        if not isinstance(label, str) or not label.strip() or "<" in label:
            raise ValueError("%s: needs a plain-text label" % where)
        bad = [k for k in redraw_keys if k in p]
        if bad:
            raise ValueError("%s: sets %s, a redraw-only control; PLAN.md D.0 ships it from the lesson "
                             "cfg and a preset never touches it" % (where, ", ".join(bad)))
        table[pid] = convert(where, p)
        menu.append((pid, label))
        expect[pid] = dict(p.get("expect") or {})
    chosen = cfg.get("preset", presets[0]["id"])
    if chosen not in table:
        raise ValueError("choicekit/%s: cfg['preset'] %r is not one of the presets (%s)"
                         % (mode, chosen, ", ".join(table)))
    return table, menu, expect, chosen


def _choice(cfg, mode, key, options, default=None):
    value = cfg.get(key, default if default is not None else options[0][0])
    if value not in [v for v, _ in options]:
        raise ValueError("choicekit/%s: cfg[%r] is %r; it must be one of %s"
                         % (mode, key, value, ", ".join(v for v, _ in options)))
    return value


def _attr(text):
    return html.escape(str(text), quote=True)


def _select(cid, label, options, chosen):
    opts = "".join('<option value="%s"%s>%s</option>' % (_attr(v), " selected" if str(v) == str(chosen) else "", t)
                   for v, t in options)
    return ('        <div class="field">\n          <label for="%s">%s</label>\n'
            '          <select id="%s">%s</select>\n        </div>\n' % (cid, label, cid, opts))


def _text(cid, label, value):
    return ('        <div class="field">\n          <label for="%s">%s</label>\n'
            '          <input id="%s" type="text" value="%s" inputmode="text" autocomplete="off">\n'
            "        </div>\n" % (cid, label, cid, _attr(value)))


def _range(cid, label, lo, hi, value):
    return ("        <div>\n"
            '          <div class="range-row"><label class="small-copy" for="%s">%s</label>'
            '<span class="range-value" id="%sOut">%s</span></div>\n'
            '          <input id="%s" type="range" min="%s" max="%s" step="1" value="%s" />\n'
            "        </div>\n" % (cid, label, cid, value, cid, lo, hi, value))


def _kpis(items):
    cells = "".join('          <div class="kpi"><span>%s</span><strong id="%s">&mdash;</strong></div>\n'
                    % (label, cid) for label, cid in items)
    return '        <div class="kpi-grid">\n%s        </div>\n' % cells


def _markup(prefix, name, subtitle):
    return ('      <div class="lab-toolbar">\n'
            '        <div class="lab-title"><strong>%s</strong><span>%s</span></div>\n'
            "      </div>\n" % (name, subtitle)
            + '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="%sTable"></table></div>\n'
            % prefix
            + '      <div class="status-banner" id="%sStatus" style="margin-top:12px;"></div>\n' % prefix)


# The wiring every mode shares. HEAD declares the preset menu, the banner and
# the table before the mode's body runs; TAIL attaches the listeners: the
# preset menu fills the controls named in FIELDS from its instance and
# redraws, a text box or range redraws on input, and each REDRAW_ONLY select
# redraws on change and is never written by anything but the reader.
_HEAD = r"""
  var presetS = document.getElementById('%(p)sPreset');
  var statusEl = document.getElementById('%(p)sStatus');
  var tableEl = document.getElementById('%(p)sTable');
  function field(id) { return document.getElementById(id); }
  function showRange(id) { var out = field(id + 'Out'); if (out) out.textContent = field(id).value; }
"""

_TAIL = r"""
  presetS.addEventListener('change', function () {
    var inst = PRESETS[presetS.value];
    if (!inst) return;
    Object.keys(FIELDS).forEach(function (k) { if (inst[k] !== undefined) field(FIELDS[k]).value = inst[k]; });
    redraw();
  });
  Object.keys(FIELDS).forEach(function (k) {
    var el = field(FIELDS[k]);
    if (el.tagName === 'SELECT') return;
    el.addEventListener('input', redraw);
    if (el.type === 'range') el.addEventListener('change', redraw);
  });
  REDRAW_ONLY.forEach(function (id) { field(id).addEventListener('change', redraw); });
  redraw();
  window.redrawLab = redraw;
"""


def _script(prefix, mode_js, table, body):
    return (RATIONAL_JS + CK_COMMON_JS + mode_js + cfg_literal("PRESETS", table)
            + _HEAD % {"p": prefix} + body + _TAIL)


def _lab(cfg, *, title, subtitle, markup, controls, script, panel_title, panel_intro, select, expect):
    return Lab(title=title, subtitle=subtitle, markup=markup, controls=controls, script=script,
               panel_title=cfg.get("panel_title", panel_title),
               panel_intro=cfg.get("panel_intro", panel_intro),
               expect={select: expect})


# ---------------------------------------------------------------------------
# decide
# ---------------------------------------------------------------------------

DE_RULES = [("dominance", "dominance"), ("maximin", "maximin"), ("maximax", "maximax"),
            ("regret", "minimax regret"), ("laplace", "Laplace (equal weights)"),
            ("eu", "expected utility"), ("evidential", "evidential expected utility"),
            ("constrained", "expected utility, forbidden acts removed")]


def _decide_convert(where, p):
    acts = _names(where, p.get("acts"), "acts", 1, 5)
    states = _names(where, p.get("states"), "states", 1, 5)
    pay = p.get("payoffs")
    if not isinstance(pay, list) or len(pay) != len(acts):
        raise ValueError("%s: payoffs need one row per act (%d)" % (where, len(acts)))
    rows = [_vec(where, row, "the payoff row for %s" % a, len(states)) for row, a in zip(pay, acts)]
    probs = p.get("probs")
    probs_t = _txt(_dist(where, probs, "probs", len(states))) if probs else ""
    cond = p.get("conditional") or {}
    if not isinstance(cond, dict):
        raise ValueError("%s: conditional should be {act: [probabilities]}" % where)
    cond_t = []
    for act, row in cond.items():
        if act not in acts:
            raise ValueError("%s: conditional names %r, which is not an act" % (where, act))
        cond_t.append("%s: %s" % (act, _txt(_dist(where, row, "the conditional row for %s" % act, len(states)))))
    forbidden = p.get("forbidden") or []
    for act in forbidden:
        if act not in acts:
            raise ValueError("%s: forbidden names %r, which is not an act" % (where, act))
    return {"acts": ", ".join(acts), "states": ", ".join(states),
            "matrix": "; ".join(_txt(r) for r in rows), "probs": probs_t,
            "cond": "; ".join(cond_t), "forbid": ", ".join(forbidden)}


def _decide(cfg):
    table, menu, expect, chosen = _presets(cfg, "decide", _decide_convert, ("rule",))
    rule = _choice(cfg, "decide", "rule", DE_RULES)
    here = table[chosen]
    controls = (
        _select("dePreset", "Worked example", menu, chosen)
        + _text("deActs", "Acts, separated by commas", here["acts"])
        + _text("deStates", "States, separated by commas", here["states"])
        + _text("deMatrix", "Payoffs: one row per act, rows separated by &ldquo;;&rdquo;", here["matrix"])
        + _text("deProbs", "State probabilities (empty for ignorance)", here["probs"])
        + _text("deCond", "Probabilities given each act, &ldquo;act: p1 p2; &hellip;&rdquo;", here["cond"])
        + _text("deForbid", "Forbidden acts", here["forbid"])
        + _select("deRule", "Decision rule", DE_RULES, rule)
        + _kpis([("Choice", "deChoice"), ("The rule&rsquo;s score", "deValue"),
                 ("Value of perfect information", "deVpi"), ("Expected utilities tie at", "deFlip")])
    )
    body = r"""
  var FIELDS = { acts: 'deActs', states: 'deStates', matrix: 'deMatrix', probs: 'deProbs', cond: 'deCond', forbid: 'deForbid' };
  var REDRAW_ONLY = ['deRule'];
  var TILES = ['deChoice', 'deValue', 'deVpi', 'deFlip'];
  var RULE_SAYS = {
    maximin: 'Maximin scores each act by its worst payoff and takes the best of those',
    maximax: 'Maximax scores each act by its best payoff and takes the best of those',
    regret: 'Minimax regret scores each act by its largest regret, the column best minus its payoff, and takes the smallest',
    laplace: 'Laplace weights every state equally and takes the best average',
    eu: 'Expected utility weights each payoff by its state probability and takes the best sum',
    evidential: 'Evidential expected utility weights each act\'s payoffs by the state probabilities given that act',
    constrained: 'The constrained rule removes the forbidden acts and takes the best expected utility of the rest'
  };
  function redraw() {
    var inst;
    try {
      inst = deRead({ acts: field('deActs').value, states: field('deStates').value, matrix: field('deMatrix').value,
                      probs: field('deProbs').value, cond: field('deCond').value, forbid: field('deForbid').value });
    } catch (err) { tableEl.innerHTML = ''; ckRefuse(statusEl, TILES, err.message); return; }
    var rule = field('deRule').value, out = deDecide(inst, rule), acts = deConsidered(inst, rule);
    var vpi = deVpi(inst, acts), flip = deFlip(inst, acts);
    tableEl.innerHTML = ckTable('The payoff table' + (out.scores ? ', with each act\'s score under the rule' : ''),
      ['act'].concat(inst.states).concat(out.scores ? ['score'] : []),
      inst.acts.map(function (a, i) {
        var cls = out.choice && out.choice.indexOf(i) >= 0 ? 'tone-cyan' : (acts.indexOf(i) < 0 ? 'tone-muted' : '');
        var row = [{ t: a, c: cls }].concat(inst.pay[i].map(function (x) { return { t: ckFig(x), c: cls }; }));
        if (out.scores) row.push({ t: out.scores[i] === null ? 'forbidden' : ckFig(out.scores[i]), c: cls });
        return row;
      }));
    ckSet('deVpi', vpi === null ? CK_DASH : ckFig(vpi));
    ckSet('deFlip', flip === null ? CK_DASH : (flip === 'none' ? 'none' : 'p(' + inst.states[0] + ') = ' + Rtext(flip.p)));
    if (out.need) {
      ckSet('deChoice', CK_DASH); ckSet('deValue', CK_DASH);
      statusEl.innerHTML = '<span class="tone-red">' + ckEsc(out.need) + '.</span>';
      return;
    }
    ckSet('deChoice', out.choice.length ? ckPick(inst.acts, out.choice) : 'none');
    ckSet('deValue', out.value === null ? CK_DASH : ckFig(out.value));
    var said;
    if (rule === 'dominance') {
      said = 'Dominance compares acts state by state. No act dominates ' + ckPick(inst.acts, out.undominated)
        + (out.choice.length ? ', and ' + inst.acts[out.choice[0]] + ' dominates every other act, so dominance picks it.'
          : ', and no single act dominates all the others, so dominance picks none.');
    } else {
      said = RULE_SAYS[rule] + ': ' + inst.acts.map(function (a, i) {
        return a + ' ' + (out.scores[i] === null ? 'forbidden' : ckFig(out.scores[i]));
      }).join(', ') + '. It picks ' + (out.choice.length ? ckPick(inst.acts, out.choice) : 'nothing') + '.';
    }
    if (vpi !== null) said += ' Knowing the state before acting is worth ' + ckFig(vpi) + '.';
    if (flip && flip !== 'none') said += ' ' + inst.acts[flip.a] + ' and ' + inst.acts[flip.b] + ' tie when p(' + inst.states[0] + ') = ' + Rtext(flip.p) + '.';
    statusEl.innerHTML = ckEsc(said);
  }
"""
    return _lab(
        cfg, title="A decision table under every rule",
        subtitle="the same payoffs, eight ways of choosing, each computed exactly",
        markup=_markup("de", "Acts by states", "a row per act, a column per state; the rule decides"),
        controls=controls, script=_script("de", DECIDE_JS, table, body),
        panel_title="Change the payoffs, the probabilities or the rule",
        panel_intro="Every score is computed from the table as typed. A rule that needs probabilities "
                    "says so rather than inventing them.",
        select="dePreset", expect=expect)


# ---------------------------------------------------------------------------
# update
# ---------------------------------------------------------------------------


def _update_convert(where, p):
    hyps = _names(where, p.get("hyps"), "hypotheses", 1, 10)
    outs = _names(where, p.get("outcomes"), "outcomes", 1, 10, spaces=False)
    prior = _dist(where, p.get("prior"), "prior", len(hyps))
    lik = p.get("lik")
    if not isinstance(lik, list) or len(lik) != len(hyps):
        raise ValueError("%s: lik needs one row per hypothesis (%d)" % (where, len(hyps)))
    rows = [_dist(where, row, "the likelihood row for %s" % h, len(outs)) for row, h in zip(lik, hyps)]
    data = p.get("data") or []
    if isinstance(data, str):
        data = data.split()
    if not isinstance(data, list) or any(d not in outs for d in data) or len(data) > 1000:
        raise ValueError("%s: data must be a list of at most 1000 outcomes from %s" % (where, outs))
    runs, i = [], 0
    while i < len(data):
        j = i
        while j < len(data) and data[j] == data[i]:
            j += 1
        runs.append("%s*%d" % (data[i], j - i) if j - i >= 4 else " ".join(data[i:j]))
        i = j
    pay = p.get("payoffs") or {}
    if not isinstance(pay, dict):
        raise ValueError("%s: payoffs should be {act: [one payoff per hypothesis]}" % where)
    pay_t = ["%s: %s" % (_name(where, a, "act"), _txt(_vec(where, v, "the payoffs of %s" % a, len(hyps))))
             for a, v in pay.items()]
    return {"hyps": hyps, "outs": outs, "prior": _txt(prior), "lik": "; ".join(_txt(r) for r in rows),
            "data": " ".join(runs), "pay": "; ".join(pay_t)}


def _update(cfg):
    table, menu, expect, chosen = _presets(cfg, "update", _update_convert)
    here = table[chosen]
    controls = (
        _select("upPreset", "Worked example", menu, chosen)
        + _text("upPrior", "Prior, one per hypothesis", here["prior"])
        + _text("upLik", "Likelihoods: a row per hypothesis, a column per outcome, rows separated by &ldquo;;&rdquo;",
                here["lik"])
        + _text("upData", "Data: outcome names separated by spaces (red*10 is ten reds)", here["data"])
        + _text("upPay", "Payoffs, &ldquo;act: one per hypothesis; &hellip;&rdquo; (empty for none)", here["pay"])
        + _select("upHyp", "The hypothesis the tiles report", [(str(i), h) for i, h in enumerate(here["hyps"])], "0")
        + _kpis([("Posterior", "upPost"), ("Bayes factor", "upBF"), ("The data", "upConf"),
                 ("Next outcome is the first", "upPred"), ("Best act now", "upBest")])
    )
    body = r"""
  var FIELDS = { prior: 'upPrior', lik: 'upLik', data: 'upData', pay: 'upPay' };
  var REDRAW_ONLY = ['upHyp'];
  var TILES = ['upPost', 'upBF', 'upConf', 'upPred', 'upBest'];
  var shownHyps = (PRESETS[presetS.value] || { hyps: [] }).hyps.join('\n');
  /* The hypothesis menu follows the hypotheses; its value (an index) is kept. */
  function syncHyps(hyps) {
    if (hyps.join('\n') === shownHyps) return;
    var sel = field('upHyp'), keep = +sel.value < hyps.length ? sel.value : '0';
    ckOptions(sel, hyps.map(function (h, i) { return [String(i), h]; }), keep);
    shownHyps = hyps.join('\n');
  }
  function redraw() {
    var preset = PRESETS[presetS.value] || {}, inst;
    try {
      inst = upRead({ prior: field('upPrior').value, lik: field('upLik').value, data: field('upData').value,
                      pay: field('upPay').value }, preset.hyps, preset.outs);
    } catch (err) { tableEl.innerHTML = ''; ckRefuse(statusEl, TILES, err.message); return; }
    syncHyps(inst.hyps);
    var h = +field('upHyp').value;
    if (!(h >= 0 && h < inst.hyps.length)) h = 0;
    var out = upSolve(inst, h);
    if (out.refuse) { tableEl.innerHTML = ''; ckRefuse(statusEl, TILES, out.refuse); return; }
    tableEl.innerHTML = ckTable('Prior times the likelihood of the data, then normalised',
      ['hypothesis', 'prior', 'P(data | H)', 'posterior'],
      inst.hyps.map(function (name, i) {
        var c = i === h ? 'tone-cyan' : '';
        return [{ t: name, c: c }, { t: Rtext(inst.prior[i]), c: c }, { t: Rtext(out.like[i]), c: c }, { t: Rtext(out.post[i]), c: c }];
      }));
    ckSet('upPost', Rtext(out.post[h]));
    ckSet('upBF', out.bf === null ? CK_DASH : (out.bf === 'infinite' ? 'infinite' : Rtext(out.bf)));
    ckSet('upConf', out.conf);
    ckSet('upPred', Rtext(out.pred));
    ckSet('upBest', out.best ? out.best.names.join(', ') + ': ' + ckFig(out.best.value) : CK_DASH);
    statusEl.innerHTML = ckEsc('After ' + inst.n + ' observation' + (inst.n === 1 ? '' : 's') + ', ' + inst.hyps[h]
      + ' moves from ' + Rtext(inst.prior[h]) + ' to ' + Rtext(out.post[h]) + '. '
      + (out.bf === null ? 'Its prior is 1, so there is no alternative to weigh it against.'
        : (out.bf === 'infinite' ? 'The data are impossible on every alternative.'
          : (Requ(out.bf, R1) ? 'The data are exactly as probable on it as on the alternatives taken together.'
            : 'The data are ' + Rtext(out.bf) + ' times as probable on it as on the alternatives taken together.')))
      + ' The next observation is ' + inst.outs[0] + ' with probability ' + Rtext(out.pred) + '.');
  }
"""
    return _lab(
        cfg, title="Exact Bayesian updating",
        subtitle="prior times likelihood, normalised; the Bayes factor is the weight of the data",
        markup=_markup("up", "Hypotheses, data, posterior", "every figure is an exact fraction"),
        controls=controls, script=_script("up", UPDATE_JS, table, body),
        panel_title="Change the prior, the likelihoods or the data",
        panel_intro="A prior or a likelihood row that does not sum to 1 is refused, not rescaled.",
        select="upPreset", expect=expect)


# ---------------------------------------------------------------------------
# credence
# ---------------------------------------------------------------------------

CR_KINDS = [("space", "a finite outcome space"), ("lottery", "a fair lottery"), ("independent", "independent claims")]


def _credence_convert(where, p):
    kind = p.get("kind", "space")
    if kind not in [k for k, _ in CR_KINDS]:
        raise ValueError("%s: kind %r is not space, lottery or independent" % (where, kind))
    _, thr = _q(where, p.get("threshold", 1), "threshold")
    out = {"kind": kind, "threshold": thr, "n": str(_int(where, p.get("n", 100), "n", 2, 1000)),
           "outs": "", "probs": "", "events": "", "typed": "", "p": ""}
    if kind == "space":
        outs = _names(where, p.get("outcomes"), "outcomes", 1, 12, spaces=False)
        out["outs"] = " ".join(outs)
        out["probs"] = _txt(_dist(where, p.get("probs"), "probs", len(outs)))
        events, seen = [], set()
        for e in p.get("events") or []:
            name = _name(where, e.get("name"), "event")
            if name in seen:
                raise ValueError("%s: the event %r is defined twice" % (where, name))
            seen.add(name)
            members = e.get("set") or []
            if any(m not in outs for m in members):
                raise ValueError("%s: the event %r names an outcome not in %s" % (where, name, outs))
            events.append("%s: %s" % (name, " ".join(members)))
        if not events or len(events) > 12:
            raise ValueError("%s: a space needs 1 to 12 events" % where)
        out["events"] = "; ".join(events)
        typed = p.get("typed") or {}
        for ev in typed:
            if ev not in seen:
                raise ValueError("%s: a typed credence names %r, which is not an event" % (where, ev))
        out["typed"] = " ".join("%s=%s" % (ev, _q(where, c, "credence")[1]) for ev, c in typed.items())
    else:
        f, t = _q(where, p.get("p", "1/2"), "p")
        if not 0 <= f <= 1:
            raise ValueError("%s: p must lie in [0, 1]" % where)
        out["p"] = t
    return out


def _credence(cfg):
    table, menu, expect, chosen = _presets(cfg, "credence", _credence_convert)
    here = table[chosen]
    controls = (
        _select("crPreset", "Worked example", menu, chosen)
        + _select("crKind", "Kind", CR_KINDS, here["kind"])
        + _range("crN", "Number of tickets or claims", 2, 1000, here["n"])
        + _text("crP", "Probability of each claim (independent kind)", here["p"])
        + _text("crThreshold", "Belief threshold", here["threshold"])
        + _text("crEvents", "Events, &ldquo;name: outcomes; &hellip;&rdquo; (space kind)", here["events"])
        + _text("crTyped", "Typed credences, &ldquo;event=3/5 &hellip;&rdquo;", here["typed"])
        + _kpis([("Accepted", "crAccepted"), ("P(all accepted)", "crPAll"),
                 ("The accepted set", "crConsistent"), ("Dutch book", "crBook")])
    )
    body = r"""
  var FIELDS = { kind: 'crKind', n: 'crN', p: 'crP', threshold: 'crThreshold', events: 'crEvents', typed: 'crTyped' };
  var REDRAW_ONLY = ['crKind'];
  var TILES = ['crAccepted', 'crPAll', 'crConsistent', 'crBook'];
  function redraw() {
    showRange('crN');
    var kind = field('crKind').value, preset = PRESETS[presetS.value] || {}, threshold, space = null, events = null, typed = null, p = null;
    var n = Math.max(2, Math.min(1000, parseInt(field('crN').value, 10) || 2));
    try {
      threshold = ckNum(field('crThreshold').value, 'The threshold');
      if (kind === 'space') {
        if (!preset.outs) throw new Error('This worked example has no outcome space; choose the lottery or independent kind');
        space = crSpace(preset.outs, preset.probs);
        events = crReadEvents(field('crEvents').value, space);
        typed = crReadTyped(field('crTyped').value, events);
      } else if (kind === 'independent') {
        p = ckUnit(ckNum(field('crP').value, 'The probability of each claim'), 'The probability of each claim');
      }
    } catch (err) { tableEl.innerHTML = ''; ckRefuse(statusEl, TILES, err.message); return; }
    var v, said, book = null;
    if (kind === 'space') {
      v = crSpaceVerdict(space, events, threshold);
      book = crBook(events, typed);
      tableEl.innerHTML = ckTable('Each event, its probability, and whether the threshold accepts it', ['event', 'P', 'accepted'],
        events.map(function (e) {
          var pe = crProb(space, e.set), ok = Rcmp(pe, threshold) >= 0;
          return [{ t: e.name, c: ok ? 'tone-cyan' : '' }, Rtext(pe), ok ? 'yes' : 'no'];
        }));
      said = 'Over ' + space.outs.length + ' outcomes the threshold ' + Rtext(threshold) + ' accepts ' + v.accepted + ' of '
        + v.of + ' events, which together have probability ' + Rtext(v.pAll) + '. '
        + (book ? 'The typed credences can be booked: ' + book.why + '.' : 'No Dutch book against the typed credences was found.');
    } else {
      v = kind === 'lottery' ? crLottery(n, threshold) : crIndependent(n, p, threshold);
      tableEl.innerHTML = ckTable('One claim and all of them', ['claims', 'P(each)', 'threshold', 'P(all accepted)'],
        [[String(n), Rtext(v.each), Rtext(threshold), Rtext(v.pAll)]]);
      said = (kind === 'lottery' ? 'Each of the ' + n + ' claims that a given ticket loses has probability '
        : 'Each of the ' + n + ' independent claims has probability ')
        + Rtext(v.each) + ', so the threshold ' + Rtext(threshold) + ' accepts ' + v.accepted + ' of ' + n
        + ', and the probability that every accepted claim is true is ' + Rtext(v.pAll) + '.';
    }
    ckSet('crAccepted', v.accepted + ' of ' + v.of);
    ckSet('crPAll', Rtext(v.pAll));
    ckSet('crConsistent', v.consistent ? 'Consistent' : 'Inconsistent');
    ckSet('crBook', kind !== 'space' ? CK_DASH : (book ? 'loss ' + Rtext(book.loss) + ' per unit' : 'none found'));
    statusEl.innerHTML = ckEsc(said);
  }
"""
    return _lab(
        cfg, title="A threshold for belief, and a book",
        subtitle="what a threshold accepts, whether it can all be true, and what incoherence costs",
        markup=_markup("cr", "Accepting by threshold", "each claim on its own probability; the conjunction on the product"),
        controls=controls, script=_script("cr", CREDENCE_JS, table, body),
        panel_title="Move the threshold, the number of claims or the credences",
        panel_intro="Probabilities are exact fractions; a conjunction of a hundred claims at 99/100 is "
                    "printed as the fraction it is.",
        select="crPreset", expect=expect)


# ---------------------------------------------------------------------------
# series
# ---------------------------------------------------------------------------

SR_KINDS = [("geometric", "geometric"), ("harmonic", "harmonic"), ("petersburg", "St Petersburg"), ("lamp", "the lamp")]


def _series(cfg):
    presets = cfg.get("presets")
    first = presets[0] if isinstance(presets, list) and presets and isinstance(presets[0], dict) else {}
    kind = _choice(cfg, "series", "kind", SR_KINDS, first.get("kind", "geometric"))

    def convert(where, p):
        if p.get("kind", kind) != kind:
            raise ValueError("%s: kind %r differs from the lesson's kind %r; the series kind is a redraw-only "
                             "control the preset never touches (PLAN.md D.0)" % (where, p.get("kind"), kind))
        out = {"n": str(_int(where, p.get("n", 10), "n", 1, 60)), "a": "1", "r": "1/2", "cap": ""}
        if "a" in p:
            out["a"] = _q(where, p["a"], "a")[1]
        if "r" in p:
            out["r"] = _q(where, p["r"], "r")[1]
        if p.get("cap") is not None:
            out["cap"] = str(_int(where, p["cap"], "cap", 1, 10 ** 18 - 1))
        return out

    table, menu, expect, chosen = _presets(cfg, "series", convert)
    here = table[chosen]
    controls = (
        _select("srPreset", "Worked example", menu, chosen)
        + _select("srKind", "Series", SR_KINDS, kind)
        + _text("srA", "First term a (geometric)", here["a"])
        + _text("srR", "Ratio r (geometric)", here["r"])
        + _range("srN", "Terms n", 1, 60, here["n"])
        + _text("srCap", "Bankroll cap (St Petersburg; empty for none)", here["cap"])
        + _kpis([("Term n", "srTerm"), ("Sum of n terms", "srSum"), ("Limit", "srLimit"), ("Remainder", "srRemain")])
    )
    body = r"""
  var FIELDS = { n: 'srN', a: 'srA', r: 'srR', cap: 'srCap' };
  var REDRAW_ONLY = ['srKind'];
  var TILES = ['srTerm', 'srSum', 'srLimit', 'srRemain'];
  var NAMES = { geometric: 'geometric series', harmonic: 'harmonic series', petersburg: 'St Petersburg expectation',
                lamp: 'lamp\'s switching times' };
  function redraw() {
    showRange('srN');
    var kind = field('srKind').value, n = Math.max(1, Math.min(60, parseInt(field('srN').value, 10) || 1)), series;
    try {
      if (kind === 'geometric') {
        series = srGeometric(ckNum(field('srA').value, 'The first term a'), ckNum(field('srR').value, 'The ratio r'), n);
      } else if (kind === 'harmonic') {
        series = srHarmonic(n);
      } else if (kind === 'petersburg') {
        var c = ckClean(field('srCap').value), cap = null;
        if (c !== '') {
          if (!/^\d{1,18}$/.test(c) || BigInt(c) < 1n) throw new Error('The cap should be a whole number of at least 1, or empty for none');
          cap = BigInt(c);
        }
        series = srPetersburg(n, cap);
      } else {
        series = srLamp(n);
      }
    } catch (err) { tableEl.innerHTML = ''; ckRefuse(statusEl, TILES, err.message); return; }
    var s = srSummary(series), rows = [];
    for (var k = 1; k <= n; k += 1) {
      if (n > 12 && k > 6 && k <= n - 4) { if (k === 7) rows.push(['…', '', '']); continue; }
      rows.push([String(k), ckFig(series.terms[k - 1]), ckFig(s.sums[k - 1])]);
    }
    tableEl.innerHTML = ckTable('Term by term, with the running sum', ['k', 'term', 'sum so far'], rows);
    ckSet('srTerm', kind === 'lamp' ? (n % 2 === 1 ? '+1 (on)' : CK_MINUS + '1 (off)') : ckFig(series.terms[n - 1]));
    ckSet('srSum', ckFig(s.sum));
    ckSet('srLimit', s.limit === null ? 'none' : ckFig(s.limit));
    ckSet('srRemain', s.remain === null ? CK_DASH : ckFig(s.remain));
    statusEl.innerHTML = ckEsc('The first ' + n + ' terms of the ' + NAMES[kind] + ' sum to ' + ckFig(s.sum) + '. '
      + (s.limit === null ? 'The partial sums have no finite limit.'
        : 'They approach ' + ckFig(s.limit) + ', and ' + ckFig(s.remain) + ' is still to come.')
      + (kind === 'lamp' ? ' After ' + n + ' switches the lamp is ' + (n % 2 === 1 ? 'on' : 'off')
        + '; the times add up to a minute, and nothing in the series says what the lamp is at the minute.' : ''));
  }
"""
    return _lab(
        cfg, title="Exact partial sums",
        subtitle="n terms added as fractions, against the limit when there is one",
        markup=_markup("sr", "Adding up infinitely many steps", "the sum of n terms, and what remains"),
        controls=controls, script=_script("sr", SERIES_JS, table, body),
        panel_title="Change the terms, the count or the cap",
        panel_intro="Every sum is an exact fraction, so a remainder of 1/1024 prints as 1/1024.",
        select="srPreset", expect=expect)


# ---------------------------------------------------------------------------
# game
# ---------------------------------------------------------------------------

GA_VIEWS = [("best", "best responses"), ("dominance", "dominance"), ("pareto", "Pareto efficiency")]


def _game_convert(where, p):
    rows = _names(where, p.get("rows"), "row strategies", 2, 4)
    cols = _names(where, p.get("cols"), "column strategies", 2, 4)
    pay = p.get("payoffs")
    if not isinstance(pay, list) or len(pay) != len(rows):
        raise ValueError("%s: payoffs need one row per row strategy (%d)" % (where, len(rows)))
    lines = []
    for row, name in zip(pay, rows):
        if not isinstance(row, list) or len(row) != len(cols):
            raise ValueError("%s: the payoff row for %s is ragged" % (where, name))
        cells = []
        for cell in row:
            if not isinstance(cell, (list, tuple)) or len(cell) != 2:
                raise ValueError("%s: each cell is [row payoff, column payoff]" % where)
            cells.append("%s,%s" % (_q(where, cell[0])[1], _q(where, cell[1])[1]))
        lines.append(" ".join(cells))
    return {"rows": ", ".join(rows), "cols": ", ".join(cols), "matrix": "; ".join(lines)}


def _game(cfg):
    table, menu, expect, chosen = _presets(cfg, "game", _game_convert, ("view",))
    view = _choice(cfg, "game", "view", GA_VIEWS)
    here = table[chosen]
    controls = (
        _select("gaPreset", "Worked example", menu, chosen)
        + _text("gaRows", "Row player&rsquo;s strategies", here["rows"])
        + _text("gaCols", "Column player&rsquo;s strategies", here["cols"])
        + _text("gaMatrix", "Payoffs &ldquo;row,column&rdquo;, rows separated by &ldquo;;&rdquo;", here["matrix"])
        + _select("gaView", "Show", GA_VIEWS, view)
        + _kpis([("Pure equilibria", "gaPure"), ("Mixed equilibrium", "gaMixed"),
                 ("Dominance", "gaDom"), ("Pareto", "gaPareto")])
    )
    body = r"""
  var FIELDS = { rows: 'gaRows', cols: 'gaCols', matrix: 'gaMatrix' };
  var REDRAW_ONLY = ['gaView'];
  var TILES = ['gaPure', 'gaMixed', 'gaDom', 'gaPareto'];
  function redraw() {
    var g;
    try { g = gaRead({ rows: field('gaRows').value, cols: field('gaCols').value, matrix: field('gaMatrix').value }); }
    catch (err) { tableEl.innerHTML = ''; ckRefuse(statusEl, TILES, err.message); return; }
    var view = field('gaView').value, best = gaBest(g), eqs = gaPure(g), mixed = gaMixed(g), eff = gaEfficient(g), left = gaIesds(g);
    function isEq(i, j) { return eqs.some(function (e) { return e[0] === i && e[1] === j; }); }
    tableEl.innerHTML = ckTable(view === 'best' ? 'Best responses marked *, equilibria in colour'
      : (view === 'dominance' ? 'Strategies iterated elimination removes are greyed' : 'Pareto-efficient cells in green, inefficient equilibria in amber'),
      ['row \\ column'].concat(g.cols), g.rows.map(function (r, i) {
        return [r].concat(g.cols.map(function (c, j) {
          var x = g.pay[i][j], t, cls = '';
          if (view === 'best') {
            t = ckFig(x[0]) + (best.row[i][j] ? '*' : '') + ', ' + ckFig(x[1]) + (best.col[i][j] ? '*' : '');
            if (isEq(i, j)) cls = 'tone-cyan';
          } else {
            t = ckFig(x[0]) + ', ' + ckFig(x[1]);
            if (view === 'dominance') cls = (left.rows.indexOf(i) < 0 || left.cols.indexOf(j) < 0) ? 'tone-muted' : 'tone-cyan';
            else cls = eff[i][j] ? 'tone-green' : (isEq(i, j) ? 'tone-amber' : '');
          }
          return { t: t, c: cls };
        }));
      }));
    var pure = eqs.length ? eqs.map(function (e) { return gaCell(g, e); }).join('; ') : 'none';
    var par = gaParetoText(g, eqs), dom = gaDomText(g);
    ckSet('gaPure', pure);
    ckSet('gaMixed', mixed === null ? CK_DASH : (mixed === 'none' ? 'none'
      : 'row ' + g.rows[0] + ': ' + Rtext(mixed.p) + ', col ' + g.cols[0] + ': ' + Rtext(mixed.q)));
    ckSet('gaDom', dom);
    ckSet('gaPareto', par === null ? CK_DASH : par);
    var wr = gaDominant(g, 0, false), wc = gaDominant(g, 1, false);
    statusEl.innerHTML = ckEsc('In this ' + g.rows.length + ' by ' + g.cols.length + ' game the pure equilibria are '
      + pure + '. '
      + (mixed && mixed !== 'none' ? 'In the completely mixed equilibrium the row player plays ' + g.rows[0] + ' with probability '
        + Rtext(mixed.p) + ' and the column player plays ' + g.cols[0] + ' with probability ' + Rtext(mixed.q) + '. ' : '')
      + 'Strict dominance: ' + dom + '.'
      + (wr >= 0 && gaDominant(g, 0, true) < 0 ? ' ' + g.rows[wr] + ' weakly dominates for row.' : '')
      + (wc >= 0 && gaDominant(g, 1, true) < 0 ? ' ' + g.cols[wc] + ' weakly dominates for column.' : ''));
  }
"""
    return _lab(
        cfg, title="A game in a table",
        subtitle="best responses, equilibria, dominance and efficiency, computed from the payoffs",
        markup=_markup("ga", "Two players, payoffs row first", "an equilibrium is a cell where both are best-responding"),
        controls=controls, script=_script("ga", GAME_JS, table, body),
        panel_title="Change the payoffs or the view",
        panel_intro="The mixed equilibrium of a 2 by 2 game is solved exactly from the two indifference conditions.",
        select="gaPreset", expect=expect)


# ---------------------------------------------------------------------------
# iterated
# ---------------------------------------------------------------------------

IT_STRATEGIES = ("ALLC", "ALLD", "TFT", "GRIM", "PAVLOV", "TF2T", "STFT")


def _iterated(cfg):
    defaults = {"a": cfg.get("a", "TFT"), "b": cfg.get("b", "ALLD"),
                "rounds": cfg.get("rounds", 10), "delta": cfg.get("delta", "9/10")}

    def convert(where, p):
        vals = [_q(where, p.get(k), k) for k in ("R", "S", "T", "P")]
        r_, s_, t_, p_ = [f for f, _ in vals]
        if not (t_ > r_ > p_ > s_ and 2 * r_ > t_ + s_):
            raise ValueError("%s: a repeated prisoner's dilemma needs T > R > P > S and 2R > T + S" % where)
        a, b = p.get("a", defaults["a"]), p.get("b", defaults["b"])
        for s in (a, b):
            if s not in IT_STRATEGIES:
                raise ValueError("%s: unknown strategy %r; the strategies are %s" % (where, s, ", ".join(IT_STRATEGIES)))
        d, dt = _q(where, p.get("delta", defaults["delta"]), "delta")
        if not 0 <= d <= 1:
            raise ValueError("%s: delta must lie in [0, 1]" % where)
        return {"pay": _txt(vals), "a": a, "b": b,
                "rounds": str(_int(where, p.get("rounds", defaults["rounds"]), "rounds", 1, 50)), "delta": dt}

    table, menu, expect, chosen = _presets(cfg, "iterated", convert)
    here = table[chosen]
    opts = [(s, s) for s in IT_STRATEGIES]
    controls = (
        _select("itPreset", "Worked example", menu, chosen)
        + _text("itPay", "Payoffs R S T P", here["pay"])
        + _select("itA", "Player A", opts, here["a"])
        + _select("itB", "Player B", opts, here["b"])
        + _range("itRounds", "Rounds", 1, 50, here["rounds"])
        + _text("itDelta", "Continuation probability &delta;", here["delta"])
        + _kpis([("A&rsquo;s total", "itScoreA"), ("B&rsquo;s total", "itScoreB"),
                 ("Round-robin winner", "itWinner"), ("Cooperation needs", "itThresh")])
    )
    body = r"""
  var FIELDS = { pay: 'itPay', a: 'itA', b: 'itB', rounds: 'itRounds', delta: 'itDelta' };
  var REDRAW_ONLY = ['itA', 'itB'];
  var TILES = ['itScoreA', 'itScoreB', 'itWinner', 'itThresh'];
  function redraw() {
    showRange('itRounds');
    var g, delta, rounds = Math.max(1, Math.min(50, parseInt(field('itRounds').value, 10) || 1));
    try {
      g = itRead(field('itPay').value);
      delta = ckUnit(ckNum(field('itDelta').value, 'The continuation probability'), 'The continuation probability');
    } catch (err) { tableEl.innerHTML = ''; ckRefuse(statusEl, TILES, err.message); return; }
    var a = field('itA').value, b = field('itB').value;
    if (IT_STRATEGIES.indexOf(a) < 0) a = 'TFT';
    if (IT_STRATEGIES.indexOf(b) < 0) b = 'ALLD';
    var m = itPlay(g, a, b, rounds), tour = itTournament(g, rounds), th = itThresholds(g), shown = Math.min(rounds, 12);
    tableEl.innerHTML = ckTable('The match' + (rounds > shown ? ' (first ' + shown + ' of ' + rounds + ' rounds shown)' : '')
      + ', then each strategy\'s round-robin total', ['', 'moves', 'total'],
      [[a, m.a.slice(0, shown).join(' '), ckFig(m.sa)], [b, m.b.slice(0, shown).join(' '), ckFig(m.sb)]]
        .concat(IT_STRATEGIES.map(function (s, i) {
          return [{ t: s, c: tour.best.indexOf(i) >= 0 ? 'tone-cyan' : '' }, 'round robin', ckFig(tour.totals[i])];
        })));
    ckSet('itScoreA', ckFig(m.sa));
    ckSet('itScoreB', ckFig(m.sb));
    ckSet('itWinner', ckPick(IT_STRATEGIES, tour.best) + ': ' + ckFig(tour.totals[tour.best[0]]));
    var verdict = Rcmp(delta, th.tft) >= 0 ? 'sustains' : (Rcmp(delta, th.grim) >= 0 ? 'sustains GRIM only' : 'does not');
    ckSet('itThresh', 'GRIM ' + Rtext(th.grim) + ', TFT ' + Rtext(th.tft) + ': δ = ' + Rtext(delta) + ' ' + verdict);
    statusEl.innerHTML = ckEsc(a + ' against ' + b + ' over ' + rounds + ' round' + (rounds === 1 ? '' : 's') + ' scores '
      + ckFig(m.sa) + ' to ' + ckFig(m.sb) + '. In a round robin of all seven strategies, each also meeting itself, '
      + ckPick(IT_STRATEGIES, tour.best) + ' scores most. Cooperation is an equilibrium against GRIM when δ is at least '
      + Rtext(th.grim) + ', and against TFT when it is at least ' + Rtext(th.tft) + '.');
  }
"""
    return _lab(
        cfg, title="The repeated prisoner's dilemma",
        subtitle="one match, a tournament of seven strategies, and the discount that sustains cooperation",
        markup=_markup("it", "Playing the dilemma again", "C cooperates, D defects; payoffs R S T P"),
        controls=controls, script=_script("it", ITERATED_JS, table, body),
        panel_title="Change the payoffs, the strategies or the rounds",
        panel_intro="Payoffs that are not a repeated prisoner&rsquo;s dilemma (T &gt; R &gt; P &gt; S and "
                    "2R &gt; T + S) are refused.",
        select="itPreset", expect=expect)


# ---------------------------------------------------------------------------
# commons
# ---------------------------------------------------------------------------

_POLY_RE = re.compile(r"[0-9kn+\-*/^().\s−×·]+")


def _commons(cfg):
    lesson_gens = _int("choicekit/commons", cfg.get("gens", 0), "cfg['gens']", 0, 40)

    def convert(where, p):
        n = _int(where, p.get("n"), "n", 2, 50)
        for key in ("payC", "payD"):
            if not isinstance(p.get(key), str) or not p[key].strip() or not _POLY_RE.fullmatch(p[key]):
                raise ValueError("%s: %s must be an expression in k and n, such as \"3k + 1\"" % (where, key))
        x0, xt = _q(where, p.get("x0", "1/2"), "x0")
        if not 0 <= x0 <= 1:
            raise ValueError("%s: x0 must lie in [0, 1]" % where)
        return {"n": str(n), "payC": p["payC"].strip(), "payD": p["payD"].strip(), "x0": xt,
                "gens": str(_int(where, p.get("gens", lesson_gens), "gens", 0, 40))}

    table, menu, expect, chosen = _presets(cfg, "commons", convert)
    here = table[chosen]
    controls = (
        _select("cmPreset", "Worked example", menu, chosen)
        + _range("cmN", "Players n", 2, 50, here["n"])
        + _text("cmPC", "Cooperator&rsquo;s payoff C(k), with k of the others cooperating", here["payC"])
        + _text("cmPD", "Defector&rsquo;s payoff D(k)", here["payD"])
        + _text("cmX0", "Starting share of cooperators", here["x0"])
        + _range("cmGens", "Generations", 0, 40, here["gens"])
        + _kpis([("Dominance", "cmDom"), ("Equilibria", "cmEq"), ("Social optimum", "cmOpt"),
                 ("Defecting gains", "cmUniv"), ("Cooperators after the generations", "cmShare")])
    )
    body = r"""
  var FIELDS = { n: 'cmN', payC: 'cmPC', payD: 'cmPD', x0: 'cmX0', gens: 'cmGens' };
  var REDRAW_ONLY = [];
  var TILES = ['cmDom', 'cmEq', 'cmOpt', 'cmUniv', 'cmShare'];
  function redraw() {
    showRange('cmN'); showRange('cmGens');
    var n = Math.max(2, Math.min(50, parseInt(field('cmN').value, 10) || 2));
    var gens = Math.max(0, Math.min(40, parseInt(field('cmGens').value, 10) || 0)), pc, pd, x0;
    try {
      pc = cmParse(field('cmPC').value); pd = cmParse(field('cmPD').value);
      x0 = ckUnit(ckNum(field('cmX0').value, 'The starting share'), 'The starting share');
    } catch (err) { tableEl.innerHTML = ''; ckRefuse(statusEl, TILES, err.message); return; }
    var t = cmTable(pc, pd, n);
    if (t.C === undefined) {
      tableEl.innerHTML = '';
      ckRefuse(statusEl, TILES, 'A payoff is undefined at k = ' + t.bad + ' (a division by zero, or a power this lab cannot take)');
      return;
    }
    var eq = cmEquilibria(t, n), opt = cmOptimum(t, n), uni = cmUniversal(t, n), rep = cmReplicate(pc, pd, n, x0, gens), rows = [];
    for (var k = 0; k < n; k += 1) {
      if (n > 14 && k > 6 && k < n - 4) { if (k === 7) rows.push(['…', '', '']); continue; }
      rows.push([String(k), ckFig(t.C[k]), ckFig(t.D[k])]);
    }
    tableEl.innerHTML = ckTable('What one player gets with k of the others cooperating', ['k', 'cooperate C(k)', 'defect D(k)'], rows);
    var ks = opt.ks, dom = cmDominance(t);
    var optText = ks.length === 1 ? (ks[0] === n ? 'all ' + n + ' cooperate' : (ks[0] === 0 ? 'none cooperate' : ks[0] + ' cooperate'))
      : ks.join(' or ') + ' cooperate';
    ckSet('cmDom', dom);
    ckSet('cmEq', eq.length ? 'k* = ' + eq.join(', ') : 'none');
    ckSet('cmOpt', optText + ': total ' + ckFig(opt.total));
    ckSet('cmUniv', 'alone ' + ckSigned(uni.alone) + ', everyone ' + ckSigned(uni.everyone));
    ckSet('cmShare', rep.x === undefined ? CK_DASH : Rtext(rep.x));
    statusEl.innerHTML = ckEsc('With ' + n + ' players: ' + (dom === 'neither' ? 'neither choice dominates' : dom.toLowerCase())
      + '; the symmetric equilibria have ' + (eq.length ? eq.join(' or ') : 'no number of') + ' cooperators; and the total is largest when '
      + optText + '. One defector among cooperators changes their own payoff by ' + ckSigned(uni.alone)
      + ', and everyone defecting rather than cooperating changes each payoff by ' + ckSigned(uni.everyone) + '. '
      + (rep.x === undefined ? 'The replicator stops at generation ' + rep.stop + ': ' + rep.why + '.'
        : 'After ' + gens + ' generation' + (gens === 1 ? '' : 's') + ' of replicator dynamics the cooperating share is ' + Rtext(rep.x) + '.'));
  }
"""
    return _lab(
        cfg, title="The many-player dilemma",
        subtitle="payoffs as exact expressions in k, and what follows from them",
        markup=_markup("cm", "One choice, n players", "C(k) and D(k): a player's payoff when k of the others cooperate"),
        controls=controls, script=_script("cm", COMMONS_JS, table, body),
        panel_title="Change the payoffs, the number of players or the starting share",
        panel_intro="Payoffs are expressions in k and n, such as 3k/(n - 1) + 1, evaluated as fractions.",
        select="cmPreset", expect=expect)


# ---------------------------------------------------------------------------
# vote
# ---------------------------------------------------------------------------

VO_KINDS = [("ranking", "rankings"), ("judgment", "judgments"), ("jury", "a jury")]
VO_RULES = [("plurality", "plurality"), ("runoff", "two-round runoff"), ("irv", "instant runoff"),
            ("borda", "Borda count"), ("condorcet", "Condorcet"), ("copeland", "Copeland")]
_FORMULA_RE = re.compile(r"[A-Za-z0-9()&|!∧∨¬→]+")


def _vote_convert(where, p):
    kind = p.get("kind", "ranking")
    if kind == "ranking":
        prof = p.get("profile")
        if not isinstance(prof, list) or not prof:
            raise ValueError("%s: a ranking profile is a list of {count, rank}" % where)
        cands, voters, parts = None, 0, []
        for g in prof:
            count = _int(where, g.get("count"), "a group count", 1, 60)
            rank = g.get("rank")
            if isinstance(rank, str):
                rank = rank.split()
            rank = _names(where, rank, "ranked candidates", 2, 5, spaces=False)
            if cands is None:
                cands = sorted(rank)
            if sorted(rank) != cands:
                raise ValueError("%s: every ranking must rank the same candidates %s" % (where, cands))
            voters += count
            parts.append("%d: %s" % (count, " ".join(rank)))
        if voters > 60:
            raise ValueError("%s: %d voters, this mode takes at most 60" % (where, voters))
        if p.get("cands") is not None and sorted(p["cands"]) != cands:
            raise ValueError("%s: cands %s are not the candidates the profile ranks" % (where, p["cands"]))
        return {"kind": kind, "profile": "; ".join(parts), "cands": cands}
    if kind == "judgment":
        atoms = _names(where, p.get("atoms"), "premises", 1, 6, spaces=False)
        formula = p.get("formula")
        if not isinstance(formula, str) or not _FORMULA_RE.fullmatch(formula.replace(" ", "")):
            raise ValueError("%s: formula must use the premises, & | ! (or ∧ ∨ ¬), → and "
                             "brackets, such as \"p&q\"" % where)
        # Shipped with the logical symbols: a value attribute holding & is an
        # entity the reader never typed.
        formula = formula.replace(" ", "").replace("&", "∧").replace("|", "∨").replace("!", "¬")
        voters = p.get("voters")
        if not isinstance(voters, list) or not voters or len(voters) % 2 == 0 or len(voters) > 59:
            raise ValueError("%s: voters must be an odd number (at most 59) of 0/1 rows" % where)
        rows = []
        for row in voters:
            if (not isinstance(row, list) or len(row) not in (len(atoms), len(atoms) + 1)
                    or any(v not in (0, 1) or isinstance(v, bool) for v in row)):
                raise ValueError("%s: each judge is a row of 0/1, one per premise and optionally the conclusion" % where)
            rows.append(" ".join(str(v) for v in row))
        return {"kind": kind, "profile": "%s %s: %s" % (" ".join(atoms), formula, "; ".join(rows)), "cands": []}
    if kind == "jury":
        n = _int(where, p.get("n"), "n", 1, 101)
        f, t = _q(where, p.get("p"), "p")
        if not 0 <= f <= 1:
            raise ValueError("%s: p must lie in [0, 1]" % where)
        return {"kind": kind, "profile": "n=%d p=%s" % (n, t), "cands": []}
    raise ValueError("%s: kind %r is not ranking, judgment or jury" % (where, kind))


def _vote(cfg):
    table, menu, expect, chosen = _presets(cfg, "vote", _vote_convert, ("rule", "remove"))
    rule = _choice(cfg, "vote", "rule", VO_RULES)
    here = table[chosen]
    remove_opts = [("nobody", "nobody")] + [(c, c) for c in here["cands"]]
    remove = _choice(cfg, "vote", "remove", remove_opts, "nobody")
    controls = (
        _select("voPreset", "Worked example", menu, chosen)
        + _select("voKind", "Kind", VO_KINDS, here["kind"])
        + _text("voProfile", "Profile: &ldquo;4: A B C; 3: B C A&rdquo;, &ldquo;p q p&and;q: 1 1 1; &hellip;&rdquo; "
                "or &ldquo;n=3 p=3/5&rdquo;", here["profile"])
        + _select("voRule", "Rule", VO_RULES, rule)
        + _select("voRemove", "Remove a candidate", remove_opts, remove)
        + _kpis([("Winner", "voWinner"), ("Majority relation", "voCondorcet"), ("Independence (IIA)", "voIIA"),
                 ("Manipulation", "voManip"), ("Majority correct", "voJury"), ("One vote decisive", "voPivot")])
    )
    body = r"""
  var FIELDS = { kind: 'voKind', profile: 'voProfile' };
  var REDRAW_ONLY = ['voKind', 'voRule', 'voRemove'];
  var TILES = ['voWinner', 'voCondorcet', 'voIIA', 'voManip', 'voJury', 'voPivot'];
  var RULE_NAMES = { plurality: 'plurality', runoff: 'the two-round runoff', irv: 'instant runoff', borda: 'the Borda count',
                     condorcet: 'the Condorcet rule', copeland: 'Copeland' };
  var shownCands = (PRESETS[presetS.value] || { cands: [] }).cands.join(' ');
  /* The removal menu follows the candidates; a removed candidate who is
     still standing stays selected. */
  function syncRemove(cands) {
    if (cands.join(' ') === shownCands) return;
    var sel = field('voRemove'), keep = cands.indexOf(sel.value) >= 0 ? sel.value : 'nobody';
    ckOptions(sel, [['nobody', 'nobody']].concat(cands.map(function (c) { return [c, c]; })), keep);
    shownCands = cands.join(' ');
  }
  function tf(b) { return b ? 'T' : 'F'; }
  function redraw() {
    var kind = field('voKind').value, text = field('voProfile').value, prof, judg, jury;
    try {
      if (kind === 'ranking') prof = voReadRanking(text);
      else if (kind === 'judgment') judg = voReadJudgment(text);
      else jury = voReadJury(text);
    } catch (err) { tableEl.innerHTML = ''; ckRefuse(statusEl, TILES, err.message); return; }
    if (kind === 'jury') {
      var j = voJury(jury.n, jury.p);
      ckBlank(['voWinner', 'voCondorcet', 'voIIA', 'voManip']);
      ckSet('voJury', Rtext(j.correct));
      ckSet('voPivot', j.pivot === null ? CK_DASH : Rtext(j.pivot));
      tableEl.innerHTML = ckTable('The jury', ['jurors', 'each right with', 'majority right with'],
        [[String(jury.n), Rtext(jury.p), Rtext(j.correct)]]);
      statusEl.innerHTML = ckEsc(jury.n + ' independent jurors, each right with probability ' + Rtext(jury.p)
        + ', reach a correct majority with probability ' + Rtext(j.correct) + '.'
        + (j.pivot === null ? ' With an even jury a tie is possible, so the decisive-vote tile is left blank.'
          : ' One juror\'s vote decides the outcome with probability ' + Rtext(j.pivot) + '.'));
      return;
    }
    if (kind === 'judgment') {
      var v = voJudge(judg);
      ckBlank(['voIIA', 'voManip', 'voJury', 'voPivot']);
      ckSet('voWinner', 'premise-based: ' + tf(v.premiseBased) + '; conclusion-based: ' + tf(v.conclusionBased));
      ckSet('voCondorcet', 'premises ' + v.premises.map(tf).join(', ') + '; conclusion ' + tf(v.conclusionBased));
      tableEl.innerHTML = ckTable('Each judge, then the majority in each column', judg.atoms.concat(['conclusion']),
        judg.rows.map(function (r) { return r.premises.map(tf).concat([tf(r.concl)]); })
          .concat([v.premises.map(function (b) { return { t: tf(b), c: 'tone-cyan' }; }).concat([{ t: tf(v.conclusionBased), c: 'tone-cyan' }])]));
      statusEl.innerHTML = ckEsc('Majorities accept the premises ' + v.premises.map(tf).join(', ') + ', which make the conclusion '
        + tf(v.premiseBased) + '; a majority vote on the conclusion itself gives ' + tf(v.conclusionBased) + '. '
        + (v.premiseBased === v.conclusionBased ? 'Here the two procedures agree.'
          : 'The two procedures disagree, though every judge is consistent.'));
      return;
    }
    syncRemove(prof.cands);
    var rule = field('voRule').value, rm = prof.cands.indexOf(field('voRemove').value);
    var live = prof.cands.map(function (c, i) { return i !== rm; });
    var w = voWinners(prof, live, rule), iia = voIia(prof, rule, rm), manip = voManipulate(prof, live, rule);
    var N = voMargins(voRestrict(prof.groups, live), prof.cands.length), list = voLiveList(live), cond = voCondorcetText(prof, live);
    ckSet('voWinner', voWinnerText(prof, w));
    ckSet('voCondorcet', cond);
    ckSet('voIIA', iia.winner ? CK_DASH : (iia.holds ? 'holds' : 'violated (remove ' + prof.cands[iia.violated] + ')'));
    ckSet('voManip', manip === null ? CK_DASH : (manip === 'none' ? 'none found' : 'voters ranking ' + manip.from + ' gain by ' + manip.to));
    ckBlank(['voJury', 'voPivot']);
    tableEl.innerHTML = ckTable('Voters preferring the row candidate to the column candidate',
      [''].concat(list.map(function (c) { return prof.cands[c]; })),
      list.map(function (a) {
        return [{ t: prof.cands[a], c: w.indexOf(a) >= 0 ? 'tone-cyan' : '' }].concat(list.map(function (b) {
          return a === b ? '' : { t: String(N[a][b]), c: N[a][b] > N[b][a] ? 'tone-green' : '' };
        }));
      }));
    statusEl.innerHTML = ckEsc(prof.voters + ' voters rank ' + list.length + ' candidates' + (rm >= 0 ? ' (' + prof.cands[rm] + ' removed)' : '')
      + '. Under ' + RULE_NAMES[rule] + ' the winner is ' + voWinnerText(prof, w) + '; the majority relation gives ' + cond + '.'
      + (iia.winner ? ' ' + prof.cands[rm] + ' is a winner with everyone standing, so removing it is not a test of independence.' : ''));
  }
"""
    return _lab(
        cfg, title="Collective choice",
        subtitle="six voting rules, the majority relation, judgment aggregation and the jury theorem",
        markup=_markup("vo", "From individual verdicts to a group's", "every winner recomputed from the profile as typed"),
        controls=controls, script=_script("vo", VOTE_JS, table, body),
        panel_title="Change the profile, the rule or the candidate removed",
        panel_intro="A profile reads count: best to worst, groups separated by semicolons. Ties are reported, "
                    "never broken silently.",
        select="voPreset", expect=expect)


# ---------------------------------------------------------------------------
# aggregate
# ---------------------------------------------------------------------------

AG_RULES = [("total", "total"), ("average", "average"), ("prioritarian", "prioritarian"),
            ("maximin", "maximin"), ("leximin", "leximin"), ("sufficientarian", "sufficientarian")]


def _aggregate_convert(where, p):
    a = _vec(where, p.get("A"), "A")
    b = _vec(where, p.get("B"), "B")
    if len(a) > 12 or len(b) > 12:
        raise ValueError("%s: a distribution has at most 12 entries" % where)
    out = {"A": _txt(a), "B": _txt(b), "knee": "", "threshold": "", "eps": ""}
    for key in ("knee", "threshold", "eps"):
        if p.get(key) is not None:
            out[key] = _q(where, p[key], key)[1]
    return out


def _aggregate(cfg):
    table, menu, expect, chosen = _presets(cfg, "aggregate", _aggregate_convert, ("rule",))
    rule = _choice(cfg, "aggregate", "rule", AG_RULES)
    here = table[chosen]
    controls = (
        _select("agPreset", "Worked example", menu, chosen)
        + _text("agA", "Distribution A, one welfare level per person", here["A"])
        + _text("agB", "Distribution B", here["B"])
        + _select("agRule", "Rule", AG_RULES, rule)
        + _text("agKnee", "Prioritarian knee", here["knee"])
        + _text("agThresh", "Sufficiency threshold", here["threshold"])
        + _text("agEps", "A life barely worth living, &epsilon;", here["eps"])
        + _kpis([("Verdict", "agVerdict"), ("Scores", "agScores"), ("Gini", "agGini"),
                 ("Population at &epsilon; to beat A", "agRepug")])
    )
    body = r"""
  var FIELDS = { A: 'agA', B: 'agB', knee: 'agKnee', threshold: 'agThresh', eps: 'agEps' };
  var REDRAW_ONLY = ['agRule'];
  var TILES = ['agVerdict', 'agScores', 'agGini', 'agRepug'];
  function optional(id, what) { var s = ckClean(field(id).value); return s === '' ? null : ckNum(s, what); }
  function redraw() {
    var A, B, par;
    try {
      A = ckVec(field('agA').value, 'distribution A'); B = ckVec(field('agB').value, 'distribution B');
      if (A.length > 12 || B.length > 12) throw new Error('A distribution has at most 12 people here');
      par = { knee: optional('agKnee', 'The knee'), thresh: optional('agThresh', 'The threshold'), eps: optional('agEps', 'Epsilon') };
    } catch (err) { tableEl.innerHTML = ''; ckRefuse(statusEl, TILES, err.message); return; }
    var rule = field('agRule').value, c = agCompare(A, B, rule, par), ga = agGini(A), gb = agGini(B);
    tableEl.innerHTML = ckTable('The two distributions, worst off first', ['', 'people', 'sorted', 'total'],
      [['A', String(A.length), agSorted(A).map(ckFig).join(' '), ckFig(agTotal(A))],
       ['B', String(B.length), agSorted(B).map(ckFig).join(' '), ckFig(agTotal(B))]]);
    ckSet('agGini', (ga === null ? CK_DASH : Rtext(ga)) + ' vs ' + (gb === null ? CK_DASH : Rtext(gb)));
    var repug = par.eps !== null && Rsign(par.eps) > 0 ? agRepugnant(A, par.eps) : null;
    ckSet('agRepug', repug === null ? CK_DASH : 'n* = ' + String(repug));
    if (c.need) {
      ckSet('agVerdict', CK_DASH); ckSet('agScores', CK_DASH);
      statusEl.innerHTML = '<span class="tone-red">' + ckEsc(c.need) + '.</span>';
      return;
    }
    ckSet('agVerdict', c.verdict > 0 ? 'A ≻ B' : (c.verdict < 0 ? 'B ≻ A' : 'A ~ B'));
    ckSet('agScores', c.scores);
    statusEl.innerHTML = ckEsc('The ' + rule + ' rule compares A and B on ' + c.scores + ', so it ranks '
      + (c.verdict > 0 ? 'A above B' : (c.verdict < 0 ? 'B above A' : 'them equal')) + '.'
      + (repug === null ? '' : ' ' + String(repug) + ' lives at ' + Rtext(par.eps) + ' each would have a larger total than A.'));
  }
"""
    return _lab(
        cfg, title="Two distributions, six rules",
        subtitle="the same people ranked by total, average, priority, the worst off, and sufficiency",
        markup=_markup("ag", "Comparing distributions of welfare", "each rule is a different answer to whose gain counts"),
        controls=controls, script=_script("ag", AGGREGATE_JS, table, body),
        panel_title="Change the distributions or the rule",
        panel_intro="Every score is exact; the Gini coefficient is the mean absolute difference over twice the mean.",
        select="agPreset", expect=expect)


# ---------------------------------------------------------------------------
# simpson
# ---------------------------------------------------------------------------

SI_WEIGHTS = [("pooled", "pooled (each treatment&rsquo;s own mix)"),
              ("standardised", "standardised (common group weights)")]


def _simpson_convert(where, p):
    names = _names(where, p.get("names"), "names", 2, 2)
    groups = p.get("groups")
    if not isinstance(groups, list) or len(groups) != 2:
        raise ValueError("%s: groups must list exactly two groups" % where)
    parts = []
    for g in groups:
        gname = _name(where, g.get("name"), "group")
        cells = []
        for key in ("a", "b"):
            cell = g.get(key)
            if (not isinstance(cell, (list, tuple)) or len(cell) != 2
                    or not all(isinstance(x, int) and not isinstance(x, bool) for x in cell)
                    or not 0 <= cell[0] <= cell[1] or cell[1] < 1):
                raise ValueError("%s: group %r cell %s must be [successes, trials] with 0 <= s <= t and t >= 1"
                                 % (where, gname, key))
            cells.append("%d/%d" % tuple(cell))
        parts.append("%s: %s" % (gname, " ".join(cells)))
    return {"names": ", ".join(names), "table": "; ".join(parts)}


def _simpson(cfg):
    table, menu, expect, chosen = _presets(cfg, "simpson", _simpson_convert, ("weight",))
    weight = _choice(cfg, "simpson", "weight", SI_WEIGHTS)
    here = table[chosen]
    controls = (
        _select("siPreset", "Worked example", menu, chosen)
        + _text("siNames", "The two treatments", here["names"])
        + _text("siCounts", "Groups, &ldquo;name: successes/trials for each; &hellip;&rdquo;", here["table"])
        + _select("siWeight", "Adjusted rate weights", SI_WEIGHTS, weight)
        + _kpis([("Pooled", "siPooled"), ("Group 1", "siGroup1"), ("Group 2", "siGroup2"),
                 ("Adjusted", "siAdjusted"), ("Verdict", "siVerdict")])
    )
    body = r"""
  var FIELDS = { names: 'siNames', table: 'siCounts' };
  var REDRAW_ONLY = ['siWeight'];
  var TILES = ['siPooled', 'siGroup1', 'siGroup2', 'siAdjusted', 'siVerdict'];
  function redraw() {
    var inst;
    try { inst = siRead(field('siNames').value, field('siCounts').value); }
    catch (err) { tableEl.innerHTML = ''; ckRefuse(statusEl, TILES, err.message); return; }
    var o = siSolve(inst), nm = inst.names, g = inst.groups;
    var pooled = nm[0] + ' ' + o.pa.s + '/' + o.pa.t + ' vs ' + nm[1] + ' ' + o.pb.s + '/' + o.pb.t + ': ' + siWord(nm, o.pooled);
    var adjusted = field('siWeight').value === 'standardised'
      ? nm[0] + ' ' + Rtext(o.sa) + ' vs ' + nm[1] + ' ' + Rtext(o.sb) + ': ' + siWord(nm, o.std) : pooled;
    tableEl.innerHTML = ckTable('Successes over trials, and each rate as a fraction', ['group', nm[0], nm[1], 'higher'],
      g.map(function (x, i) {
        return [x.name, x.a.s + '/' + x.a.t + ' = ' + Rtext(siRate(x.a)), x.b.s + '/' + x.b.t + ' = ' + Rtext(siRate(x.b)), siWord(nm, o.within[i])];
      }).concat([[{ t: 'pooled', c: 'tone-cyan' }, o.pa.s + '/' + o.pa.t + ' = ' + Rtext(siRate(o.pa)),
                  o.pb.s + '/' + o.pb.t + ' = ' + Rtext(siRate(o.pb)), siWord(nm, o.pooled)]]));
    ckSet('siPooled', pooled);
    ckSet('siGroup1', siWord(nm, o.within[0]));
    ckSet('siGroup2', siWord(nm, o.within[1]));
    ckSet('siAdjusted', adjusted);
    ckSet('siVerdict', o.reversal ? 'Reversal' : 'No reversal');
    statusEl.innerHTML = ckEsc('Within ' + g[0].name + ': ' + siWord(nm, o.within[0]) + '; within ' + g[1].name + ': '
      + siWord(nm, o.within[1]) + '; pooled: ' + siWord(nm, o.pooled) + '. '
      + (o.reversal ? 'The pooled comparison reverses both groups, because the two treatments were given to different mixes of groups.'
        : 'The pooled comparison does not reverse the groups.')
      + ' Weighting both treatments by the same group shares gives ' + nm[0] + ' ' + Rtext(o.sa) + ' against ' + nm[1] + ' ' + Rtext(o.sb) + '.');
  }
"""
    return _lab(
        cfg, title="Rates within groups and pooled",
        subtitle="the same counts, compared group by group and all together",
        markup=_markup("si", "Two treatments, two groups", "a rate is successes over trials, kept as a fraction"),
        controls=controls, script=_script("si", SIMPSON_JS, table, body),
        panel_title="Change the counts or the weighting",
        panel_intro="Counts read successes/trials. The pooled rate adds the counts; the standardised rate "
                    "weights each group by its share of all trials.",
        select="siPreset", expect=expect)


_MODES = {
    "decide": _decide,
    "update": _update,
    "credence": _credence,
    "series": _series,
    "game": _game,
    "iterated": _iterated,
    "commons": _commons,
    "vote": _vote,
    "aggregate": _aggregate,
    "simpson": _simpson,
}

MODES = tuple(_MODES)


def choicekit_lab(cfg):
    """The Philosophy choice kit. `cfg["mode"]` chooses the lesson; an unknown one raises.

    The raise is the contract, as in markov_lab: a kit that fell back to a
    default would render another lesson's widget under the right title.
    """
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError("choicekit_lab: unknown mode %r; the ten modes are %s" % (mode, ", ".join(MODES)))
    return _MODES[mode](cfg or {})
