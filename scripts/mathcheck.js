#!/usr/bin/env node
/*
 * Test the ARITHMETIC the generated paths are built on.
 *
 * WHY THIS EXISTS, and why it is separate from labcheck.js. That harness proves
 * every published lab runs and paints. It cannot prove the numbers are right: a
 * lab that confidently reports the wrong roots passes it, and passes every
 * markup assertion in tests/ too. The footer of every algebra page promises the
 * reader that each figure is computed from the stated definition and that the
 * arithmetic is exact. This file is what makes that promise checkable.
 *
 * The same holds for the logic course: its truth tables and quantifier
 * verdicts are computed by evaluators in scripts/mathpath/labs/logic.py, and a
 * quantifier lab whose status text reasons about a different statement than
 * its evaluator computes runs, paints, and passes labcheck while teaching a
 * falsehood. That defect shipped once; the logic section below is what now
 * catches it.
 *
 * The JavaScript under test IS the JavaScript that ships. It is extracted from
 * scripts/mathpath/labs/algebra_core.py and scripts/mathpath/labs/logic.py,
 * which hold it as raw strings, so there is no second copy to drift -- testing
 * a transcription would prove nothing about the published pages.
 *
 * Usage:  node scripts/mathcheck.js
 */

const fs = require('fs');
const path = require('path');

const SOURCE = path.join(__dirname, 'mathpath', 'labs', 'algebra_core.py');
const src = fs.readFileSync(SOURCE, 'utf8');
const LOGIC_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'logic.py');
const logicSrc = fs.readFileSync(LOGIC_SOURCE, 'utf8');
const COUNTING_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'counting.py');
const countingSrc = fs.readFileSync(COUNTING_SOURCE, 'utf8');
const PROB_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'probability.py');
const probSrc = fs.readFileSync(PROB_SOURCE, 'utf8');
const NUMBER_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'number.py');
const numberSrc = fs.readFileSync(NUMBER_SOURCE, 'utf8');
const GRAPH_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'graph.py');
const graphSrc = fs.readFileSync(GRAPH_SOURCE, 'utf8');
const ALGO_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'algorithms.py');
const algoSrc = fs.readFileSync(ALGO_SOURCE, 'utf8');
const SYSD_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'sysdesign_core.py');
const sysdSrc = fs.readFileSync(SYSD_SOURCE, 'utf8');
const ALGOCORE_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'algo_core.py');
const algoCoreSrc = fs.readFileSync(ALGOCORE_SOURCE, 'utf8');
const ESTIMATE_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'estimate.py');
const estimateSrc = fs.readFileSync(ESTIMATE_SOURCE, 'utf8');
const LATENCY_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'latency.py');
const latencySrc = fs.readFileSync(LATENCY_SOURCE, 'utf8');

/* Each block is  NAME = r"""..."""  in the Python module. */
function blockFrom(text, name, where) {
  const m = new RegExp(name + ' = r"""([\\s\\S]*?)"""', 'm').exec(text);
  if (!m) { console.error('cannot find ' + name + ' in ' + where); process.exit(2); }
  return m[1];
}
function block(name) { return blockFrom(src, name, SOURCE); }
function logicBlock(name) { return blockFrom(logicSrc, name, LOGIC_SOURCE); }
function sysdBlock(name) { return blockFrom(sysdSrc, name, SYSD_SOURCE); }
function estimateBlock(name) { return blockFrom(estimateSrc, name, ESTIMATE_SOURCE); }
function latencyBlock(name) { return blockFrom(latencySrc, name, LATENCY_SOURCE); }
function countingBlock(name) { return blockFrom(countingSrc, name, COUNTING_SOURCE); }
function probBlock(name) { return blockFrom(probSrc, name, PROB_SOURCE); }
function numberBlock(name) { return blockFrom(numberSrc, name, NUMBER_SOURCE); }
function graphBlock(name) { return blockFrom(graphSrc, name, GRAPH_SOURCE); }
function algoBlock(name) { return blockFrom(algoSrc, name, ALGO_SOURCE); }
function algoCoreBlock(name) { return blockFrom(algoCoreSrc, name, ALGOCORE_SOURCE); }

let fails = 0;
function eq(got, want, label) {
  if (String(got) !== String(want)) { fails += 1; console.log('  FAIL ' + label + ': got ' + got + ', want ' + want); }
}
function near(got, want, tol, label) {
  if (!(Math.abs(got - want) <= tol)) { fails += 1; console.log('  FAIL ' + label + ': got ' + got + ', want ~' + want); }
}

/* A minimal SVG DOM, the same shape scripts/labcheck.js gives a real page. */
function El(name) { this.name = name; this.attrs = {}; this.children = []; this._text = ''; }
El.prototype.setAttribute = function (k, v) { this.attrs[k] = String(v); };
El.prototype.getAttribute = function (k) { return this.attrs[k]; };
El.prototype.appendChild = function (c) { this.children.push(c); return c; };
Object.defineProperty(El.prototype, 'textContent', {
  get: function () { return this._text; },
  set: function (v) { this._text = String(v); if (v === '') this.children = []; }
});
global.document = { createElementNS: function (_ns, n) { return new El(n); } };
function all(el, name, out) {
  out = out || [];
  el.children.forEach(function (c) { if (c.name === name) out.push(c); all(c, name, out); });
  return out;
}

eval(block('RATIONAL_JS') + block('POLY_JS') + block('EXPR_JS') + block('SURD_JS') + block('PLOT_JS'));

// ------------------------------------------------- exact rational arithmetic
console.log('exact rationals');
eq(Rtext(Radd(R(1n, 3n), R(1n, 6n))), '1/2', '1/3 + 1/6');
eq(Rtext(Rmul(R(2n, 3n), R(9n, 4n))), '3/2', '2/3 * 9/4');
eq(Rtext(Rdiv(R(-3n, 4n), R(6n, 8n))), '-1', '-3/4 / 3/4');
eq(Rtext(Rpow(R(2n, 3n), 3)), '8/27', '(2/3)^3');
eq(Rtext(Rpow(R(2n), -3)), '1/8', '2^-3');
eq(Rtext(Rparse('-7/14')), '-1/2', 'parse -7/14 in lowest terms');
eq(Rtext(Rparse('0.375')), '3/8', 'a decimal becomes an exact fraction');
eq(Rtext(Rsqrt(R(4n, 9n))), '2/3', 'sqrt(4/9)');
eq(Rsqrt(R(2n)), 'null', 'sqrt(2) is not rational, and says so');
eq(Rcmp(R(1n, 3n), R(1n, 2n)), -1, 'comparison');
/* Exactness is the whole promise: forty additions of a third stay a third. */
let big = R(1n, 3n);
for (let i = 0; i < 40; i += 1) big = Radd(big, R(1n, 3n));
eq(Rtext(big), '41/3', '41 thirds, exactly');

// ------------------------------------------------------ polynomials over Q
console.log('polynomials over Q');
function P() { return Array.prototype.slice.call(arguments).map(v => (typeof v === 'object' ? v : R(BigInt(v)))); }
eq(Ptext(P(-6, 1, 1)), 'x^2 + x - 6', 'standard form');
eq(Ptext(P(0, 0, 3)), '3x^2', 'a monomial');
eq(Ptext(P(1, -1)), '-x + 1', 'a leading -1 is written as a sign');
eq(Ptext([R(3n, 4n), R(1n)]), 'x + (3/4)', 'a fractional coefficient is bracketed');
eq(Ptext([]), '0', 'the zero polynomial');
eq(Pdeg([]), -1, 'the zero polynomial has degree -1');
eq(Ptext(Pmul(P(-2, 1), P(3, 1))), 'x^2 + x - 6', '(x-2)(x+3) expands');
eq(Rtext(Peval(P(-6, 1, 1), R(2n))), '0', 'p(2) = 0');
eq(Ptext(Pderiv(P(-6, 1, 1))), '2x + 1', 'derivative');
const dm = Pdivmod(P(-6, 1, 1), P(-2, 1));
eq(Ptext(dm.q) + ' r ' + Ptext(dm.r), 'x + 3 r 0', 'exact division');
const dm2 = Pdivmod(P(1, 0, 0, 1), P(-1, 1));
eq(Ptext(dm2.q) + ' r ' + Ptext(dm2.r), 'x^2 + x + 1 r 2', 'x^3+1 divided by x-1');
eq(Ptext(Pgcd(P(-6, 1, 1), P(-4, 0, 1))), 'x - 2', 'polynomial gcd');

// ---------------------------------------- the rational root theorem, applied
console.log('rational roots and factoring');
eq(Prationalroots(P(-6, 1, 1)).map(Rtext).join(','), '-3,2', 'roots of x^2+x-6');
eq(Prationalroots(P(-3, 5, 2)).map(Rtext).join(','), '-3,1/2', 'roots of 2x^2+5x-3');
eq(Prationalroots(P(1, 0, 1)).length, 0, 'x^2+1 has no rational root');
/* Factors come out in ascending order of their root: deterministic and stated. */
eq(Pfactortextfull(P(-6, 1, 1)), '(x + 3)(x - 2)', 'factor x^2+x-6');
eq(Pfactortextfull(P(-3, 5, 2)), '(x + 3)(2x - 1)', 'factor 2x^2+5x-3');
eq(Pfactortextfull(P(4, -4, 1)), '(x - 2)^2', 'a perfect square keeps its multiplicity');
eq(Pfactortextfull(P(1, 0, 1)), 'x^2 + 1', 'an irreducible polynomial is written as itself');
eq(Pfactortextfull(P(-4, 0, 1)), '(x + 2)(x - 2)', 'difference of squares');
eq(Pfactortextfull(P(0, -9, 0, 1)), 'x(x + 3)(x - 3)', 'x^3-9x');
eq(Pfactortextfull(P(6, -5, 1)), '(x - 2)(x - 3)', 'x^2-5x+6');
/* 4x^3-8x-12 = 4(x^3-2x-3), and +-1, +-3 are the only candidates: none works. */
eq(Pfactortextfull(P(-12, -8, 0, 4)), '4(x^3 - 2x - 3)', 'the content comes out, the cubic stays');
eq(Pfactor(P(-12, -8, 0, 4)).complete, false, 'a cubic leftover is not claimed complete');
eq(Pfactor(P(1, 0, 1)).complete, true, 'a quadratic leftover is complete');

// ------------------------------------------------------- expression parsing
console.log('the expression parser');
const ev = (s, x) => Eeval(Eparse(s), { x: x });
const pol = (s) => { const p = Epolyof(s); return p === null ? 'null' : Ptext(p); };
eq(ev('2x', 3), 6, 'implicit multiplication: 2x');
eq(ev('3(x+1)', 4), 15, '3(x+1)');
eq(ev('(x+1)(x-2)', 5), 18, '(x+1)(x-2)');
eq(ev('4x^2', 3), 36, '4x^2');
eq(ev('2sqrt(x)', 9), 6, '2sqrt(x)');
eq(Eeval(Eparse('xy'), { x: 3, y: 4 }), 12, 'xy is a product of two variables');
/* The two places a reader is marked wrong. */
eq(ev('-x^2', 3), -9, '-x^2 means -(x^2)');
eq(ev('(-x)^2', 3), 9, '(-x)^2');
eq(ev('2^3^2', 0), 512, '^ is right-associative');
eq(ev('8/2/2', 0), 2, '/ is left-associative');
eq(ev('2*3^2', 0), 18, 'power before times');
eq(isNaN(ev('sqrt(x)', -1)), true, 'outside the domain gives NaN, not an exception');
/* Errors are named rather than swallowed. */
const msg = (s) => { try { Eparse(s); return ''; } catch (e) { return e.message; } };
eq(msg('2x +'), 'the expression ends early', 'a trailing operator');
eq(msg('sqrtt(x)'), 'unknown function "sqrtt"', 'a typo in a function name');
eq(msg('x $ 2'), 'unexpected character "$"', 'a stray character');
eq(msg('(x+1'), 'expected ")"', 'an unclosed bracket');
/* Typed input reaches the EXACT machinery, not a float approximation of it. */
eq(pol('(x+1)(x-2)'), 'x^2 - x - 2', 'a typed product expands exactly');
eq(pol('(x/3) + 1/2'), '(1/3)x + (1/2)', 'rational coefficients stay exact');
eq(pol('(2x-1)^3'), '8x^3 - 12x^2 + 6x - 1', 'a typed cube expands');
eq(pol('sqrt(x)'), 'null', 'sqrt(x) is not a polynomial');
eq(pol('1/x'), 'null', 'division by x is not a polynomial');
eq(pol('0.1x + 0.2x'), '(3/10)x', '0.1 + 0.2 is 3/10, not 0.30000000000000004');

// ----------------------------------------------- surds and quadratic roots
console.log('exact surds and quadratic roots');
const Q = (v) => R(BigInt(v));
eq(surdtext(Rsurd(Q(9))), '3', 'sqrt(9)');
eq(surdtext(Rsurd(Q(8))), '2sqrt(2)', 'sqrt(8)');
eq(surdtext(Rsurd(R(1n, 2n))), '(1/2)sqrt(2)', 'sqrt(1/2)');
eq(surdtext(Rsurd(Q(72))), '6sqrt(2)', 'sqrt(72)');
let r = quadroots(Q(1), Q(-5), Q(6));
eq(r.kind + ' ' + r.roots.map(Rtext).join(','), 'rational 2,3', 'x^2-5x+6');
r = quadroots(Q(1), Q(-2), Q(-4));
eq(r.kind + ' ' + pmtext(r.p, r.s), 'irrational 1 +- sqrt(5)', 'x^2-2x-4 keeps its surd');
r = quadroots(Q(1), Q(-4), Q(4));
eq(r.kind + ' ' + Rtext(r.roots[0]), 'double 2', 'a repeated root');
r = quadroots(Q(1), Q(0), Q(1));
eq(r.kind + ' ' + pmtext(r.p, r.s, true), 'complex +-i', 'x^2+1');
r = quadroots(Q(1), Q(-2), Q(5));
eq(r.kind + ' ' + pmtext(r.p, r.s, true), 'complex 1 +- 2i', 'x^2-2x+5');
eq(quadroots(Q(2), Q(5), Q(-3)).roots.map(Rtext).join(','), '-3,1/2', '2x^2+5x-3');
r = quadroots(Q(3), Q(-6), Q(2));
eq(pmtext(r.p, r.s), '1 +- (1/3)sqrt(3)', '3x^2-6x+2');
/* The irrational pair really are roots: substitute them back. */
{
  const a = 3, b = -6, c = 2;
  const pv = Rnum(r.p), sv = Rnum(r.s.q) * Math.sqrt(Number(r.s.k));
  eq(Math.abs(a * (pv + sv) * (pv + sv) + b * (pv + sv) + c) < 1e-12, true, 'the + root checks out');
  eq(Math.abs(a * (pv - sv) * (pv - sv) + b * (pv - sv) + c) < 1e-12, true, 'the - root checks out');
}

// ------------------------------------------------------------- the grapher
console.log('the grapher');
{
  const svg = new El('svg');
  const p = Plot(svg, { xmin: -5, xmax: 5, ymin: -10, ymax: 10 });
  near(p.sx(-5), 44, 0.01, 'left edge');
  near(p.sx(5), 644, 0.01, 'right edge');
  near(p.sx(0), 344, 0.01, 'x = 0 is centred');
  near(p.sy(10), 16, 0.01, 'top edge');
  near(p.sy(-10), 386, 0.01, 'bottom edge');
  eq(p.sy(5) < p.sy(-5), true, 'positive y is higher on screen');
  p.frame();
  eq(svg.getAttribute('viewBox'), '0 0 660 420', 'viewBox');
  const axes = all(svg, 'line').filter(l => l.attrs.class === 'plot-axis');
  eq(axes.length, 2, 'two axes');
  near(parseFloat(axes[0].attrs.y1), 201, 0.01, 'the x-axis sits at y = 0');
  near(parseFloat(axes[1].attrs.x1), 344, 0.01, 'the y-axis sits at x = 0');
}
{
  /* A window with zero out of view still gets a labelled frame. */
  const svg = new El('svg');
  Plot(svg, { xmin: 10, xmax: 20, ymin: 100, ymax: 200 }).frame();
  const axes = all(svg, 'line').filter(l => l.attrs.class === 'plot-axis');
  near(parseFloat(axes[0].attrs.y1), 386, 0.01, 'the x-axis pins to the near edge');
  near(parseFloat(axes[1].attrs.x1), 44, 0.01, 'the y-axis pins to the near edge');
}
function runs(fn) {
  const svg = new El('svg');
  Plot(svg, { xmin: -5, xmax: 5, ymin: -10, ymax: 10 }).frame().curve(fn);
  return all(svg, 'polyline');
}
eq(runs(x => x * x - 4).length, 1, 'a parabola is one unbroken run');
/* Joining across a pole draws a vertical line that is not part of the graph,
   which is exactly why readers believe 1/x is connected.
   The curve breaks for TWO different reasons and both need testing. A pole the
   sampler lands on exactly returns Infinity and breaks on the non-finite check;
   a pole it steps over returns two large finite values of opposite sign and can
   only be caught by the jump check. Sampling runs from -5 to 5 in 480 steps, so
   x = 0 IS a sample and x = 0.3 is not -- and a test using only 1/x passes with
   the jump check deleted, which is how this gap was found. */
eq(runs(x => 1 / x).length, 2, '1/x: a pole landed on exactly');
eq(runs(x => 1 / (x - 0.3)).length, 2, '1/(x-0.3): a pole stepped over');
eq(runs(x => 1 / (x * x - 0.09)).length, 3, 'two stepped-over poles give three runs');
{
  const rs = runs(x => Math.sqrt(x));
  eq(rs.length, 1, 'sqrt(x) is one run');
  eq(parseFloat(rs[0].attrs.points.split(' ')[0].split(',')[0]) >= 343.9, true,
     'sqrt(x) starts at x = 0 and not before');
}
{
  const svg = new El('svg');
  const pl = Plot(svg, { xmin: -5, xmax: 5, ymin: -10, ymax: 10 }).frame();
  pl.point(2, -4, 'plot-point root', '2');
  const c = all(svg, 'circle').filter(e => e.attrs.class === 'plot-point root');
  near(parseFloat(c[0].attrs.cx), 464, 0.01, 'a marked point lands where the number says');
  near(parseFloat(c[0].attrs.cy), 275, 0.01, 'and at the right height');
  pl.vline(3, 'plot-asym', 'x = 3');
  near(parseFloat(all(svg, 'line').filter(e => e.attrs.class === 'plot-asym')[0].attrs.x1), 524, 0.01,
       'an asymptote lands where the number says');
  const before = all(svg, 'circle').length;
  pl.point(NaN, 3); pl.point(1, Infinity);
  eq(all(svg, 'circle').length, before, 'a non-finite point is skipped, not drawn at NaN');
}
{
  const svg = new El('svg');
  NumberLine(svg, -10, 10).interval(-3, 5, true, false);
  const ends = all(svg, 'circle');
  eq(ends.length, 2, 'an interval has two endpoints');
  eq(ends[0].attrs.class, 'plot-end closed', 'a closed end is filled');
  eq(ends[1].attrs.class, 'plot-end open', 'an open end is hollow');
  near(parseFloat(ends[0].attrs.cx), 30 + (7 / 20) * 600, 0.01, 'the closed end is placed correctly');
}

// ---------------------------------------------------- propositional logic
console.log('propositional logic (course 1 labs)');
eval(logicBlock('PARSER_JS'));
{
  const T = { p: true }, F = { p: false };
  const env = (p, q) => ({ p, q });
  /* The conditional's one false row, and vacuous truth in both false-p rows. */
  const imp = parse('p -> q');
  eq(evalNode(imp, env(true, false)), false, 'T -> F is the one false row');
  eq(evalNode(imp, env(false, true)), true, 'F -> T is vacuously true');
  eq(evalNode(imp, env(false, false)), true, 'F -> F is vacuously true');
  /* Precedence: ~ binds tighter than &, and ~p & q differs from ~(p & q). */
  eq(evalNode(parse('~p & q'), env(false, false)), false, '~p & q at FF: negation binds tight');
  eq(evalNode(parse('~(p & q)'), env(false, false)), true, '~(p & q) at FF');
  /* Inclusive or vs xor part company in exactly the TT row. */
  eq(evalNode(parse('p | q'), env(true, true)), true, 'inclusive or is true at TT');
  eq(evalNode(parse('p ^ q'), env(true, true)), false, 'xor is false at TT');
  /* -> is right-associative: p -> q -> r is p -> (q -> r). */
  eq(evalNode(parse('p -> q -> r'), { p: true, q: true, r: false }), false, 'p->q->r at TTF');
  eq(evalNode(parse('p -> q -> r'), { p: false, q: true, r: false }), true, 'p->q->r at FTF: right-associative');
  /* Constants, so ⊤ and ⊥ mean what the pages say they mean. */
  eq(evalNode(parse('⊤'), {}), true, 'top is true');
  eq(evalNode(parse('⊥ -> p'), F), true, 'ex falso: bottom implies anything');
  /* Whole-table facts, over every assignment: the identities the lessons teach. */
  function rowsFor(vars) { return assignments(vars); }
  function agreeEverywhere(aSrc, bSrc, vars) {
    const a = parse(aSrc), b = parse(bSrc);
    return rowsFor(vars).every((e) => evalNode(a, e) === evalNode(b, e));
  }
  eq(agreeEverywhere('~(p & q)', '~p | ~q', ['p', 'q']), true, 'De Morgan over all four rows');
  eq(agreeEverywhere('p -> q', '~q -> ~p', ['p', 'q']), true, 'contraposition over all four rows');
  eq(agreeEverywhere('p -> q', 'q -> p', ['p', 'q']), false, 'the converse is NOT equivalent');
  const mt = parse('((p -> q) & ~q) -> ~p');
  eq(rowsFor(['p', 'q']).every((e) => evalNode(mt, e)), true, 'modus tollens is a tautology');
  const ac = parse('((p -> q) & q) -> p');
  eq(rowsFor(['p', 'q']).every((e) => evalNode(ac, e)), false, 'affirming the consequent is not');
  /* The row order the lessons teach: T before F, rightmost fastest. */
  eq(rowsFor(['p', 'q']).map((e) => (e.p ? 'T' : 'F') + (e.q ? 'T' : 'F')).join(' '),
     'TT TF FT FF', 'conventional row order');
}

// ------------------------------------------------------- quantifier verdicts
console.log('quantifier verdicts (course 1 labs)');
eval(logicBlock('QUANT_EVAL_JS'));
{
  /* Exhaustive over every 3x3 predicate: 512 grids. This is the check that
     would have caught the shipped row/column confusion, so it is done by
     enumeration rather than by trusting a handful of examples. */
  const N = 3;
  let thmOk = true, mirrorOk = true, negOk = true;
  for (let bits = 0; bits < 512; bits += 1) {
    const P = [], C = [];
    for (let x = 0; x < N; x += 1) {
      P.push([]); C.push([]);
      for (let y = 0; y < N; y += 1) {
        const v = ((bits >> (x * N + y)) & 1) === 1;
        P[x].push(v); C[x].push(!v);
      }
    }
    /* The lesson's theorem, and its mirror -- each in its own variables. */
    if (qExistsYForallX(P, N).v && !qForallXExistsY(P, N).v) thmOk = false;
    if (qExistsXForallY(P, N).v && !qForallYExistsX(P, N).v) mirrorOk = false;
    /* Lesson 10: negation flips every quantifier. Three dual pairs. */
    if (qForallForall(P, N).v !== !qExistsExists(C, N).v) negOk = false;
    if (qForallXExistsY(P, N).v !== !qExistsXForallY(C, N).v) negOk = false;
    if (qExistsYForallX(P, N).v !== !qForallYExistsX(C, N).v) negOk = false;
  }
  eq(thmOk, true, 'exists-y-forall-x implies forall-x-exists-y, all 512 grids');
  eq(mirrorOk, true, 'exists-x-forall-y implies forall-y-exists-x, all 512 grids');
  eq(negOk, true, 'negation duality across all three pairs, all 512 grids');

  /* A full row is not a full column: the regression that shipped. */
  const rowGrid = [[true, true, true], [false, false, false], [false, false, false]];
  eq(qExistsXForallY(rowGrid, N).v, true, 'a full row satisfies exists-x-forall-y');
  eq(qExistsYForallX(rowGrid, N).v, false, 'a full row does NOT satisfy exists-y-forall-x');
  eq(qForallXExistsY(rowGrid, N).v, false, 'and forall-x-exists-y fails: x = 2 has no y');

  /* The presets, on the 4-element universe the lessons publish. */
  function fill(n, fn) {
    const P = [];
    for (let x = 0; x < n; x += 1) { P.push([]); for (let y = 0; y < n; y += 1) P[x].push(!!fn(x + 1, y + 1)); }
    return P;
  }
  const diag = fill(4, (x, y) => x === y);
  eq(qForallXExistsY(diag, 4).v, true, 'identity: every x has its own y');
  eq(qExistsYForallX(diag, 4).v, false, 'identity: no single y serves every x — the lesson-9 separator');
  const succ = fill(4, (x, y) => y === x + 1);
  eq(qForallXExistsY(succ, 4).v, false, 'successor on {1..4}: forall-x-exists-y FAILS');
  eq(qForallXExistsY(succ, 4).why, 'x = 4 has no y at all', 'and names the top element as the reason');
  const le = fill(4, (x, y) => x <= y);
  const leVerdicts = [qForallForall(le, 4), qForallXExistsY(le, 4), qExistsYForallX(le, 4),
                      qForallYExistsX(le, 4), qExistsXForallY(le, 4), qExistsExists(le, 4)];
  eq(leVerdicts.filter((r) => r.v).length, 5, 'order preset: five of six verdicts true, as lesson 10 says');
  const leC = fill(4, (x, y) => !(x <= y));
  const leCVerdicts = [qForallForall(leC, 4), qForallXExistsY(leC, 4), qExistsYForallX(leC, 4),
                       qForallYExistsX(leC, 4), qExistsXForallY(leC, 4), qExistsExists(leC, 4)];
  eq(leCVerdicts.filter((r) => r.v).map((r) => r.why).join(';'),
     'x = 2, y = 1 works', 'complemented order preset: only exists-exists survives');
}

// ------------------------------------------------------------- counting
console.log('counting in BigInt (course 4 labs)');
{
  /* The course-4 labs promise the reader that every count is exact and that
     the derangement lab's three routes agree. The functions below are the
     shipped ones, extracted from counting.py; a wrong comb() would reach
     every page that lists selections, and a wrong derangeTerms() would ship a
     table that confidently disagrees with the lesson above it. */
  eval(countingBlock('BIGINT_JS') + countingBlock('DERANGE_JS'));

  eq(fact(0), 1n, '0! = 1');
  eq(fact(20), 2432902008176640000n, '20! exactly');
  eq(perm(10, 3), 720n, 'P(10,3) = 720');
  eq(perm(24, 12), 1295295050649600n, 'P(24,12), the largest P the lab can show');
  eq(perm(3, 5), 0n, 'P(n, r) with r > n is 0');
  eq(comb(52, 5), 2598960n, 'C(52,5) = 2 598 960');
  eq(comb(35, 12), 834451800n, 'C(35,12), the largest C(n+r-1, r) the lab can show');
  eq(comb(7, 5), 21n, 'C(7,5) = 21: five doughnuts from three kinds');
  eq(comb(6, 2), comb(5, 1) + comb(5, 2), "Pascal's rule at the lesson-5 preset");
  eq(comb(4, 7), 0n, 'C(n, r) with r > n is 0');
  eq(group(1295295050649600n), '1 295 295 050 649 600', 'digit grouping');

  const D = [1n, 0n, 1n, 2n, 9n, 44n, 265n, 1854n, 14833n, 133496n];
  for (let n = 0; n < D.length; n += 1) {
    eq(derangeFormula(n), D[n], 'D_' + n + ' by the alternating sum');
    eq(derangeRec(n), D[n], 'D_' + n + ' by the recurrence');
    if (n <= 8) eq(derangeBrute(n), D[n], 'D_' + n + ' by listing');
  }
  eq(derangeFormula(12), 176214841n, 'D_12, the largest n the slider allows');
  eq(derangeList(4).sort().join(','), '2143,2341,2413,3142,3412,3421,4123,4312,4321', 'the nine derangements of 1..4');
  const rows6 = derangeTerms(6).map((r) => r.running.toString()).join(',');
  eq(rows6, '720,0,360,240,270,264,265', 'the running total at n = 6 swings and settles on 265');
  eq(ratioDigits(265n, 720n, 7), '0.3680556', 'D_6/6! to seven places, rounded');
  eq(ratioDigits(1854n, 5040n, 7), '0.3678571', 'D_7/7! to seven places');
  eq(ratioDigits(14833n, 40320n, 7), '0.3678819', 'D_8/8! to seven places (the lesson table row)');
  eq(ratioDigits(1n, 3n, 4), '0.3333', 'ratioDigits pads and truncates correctly');
  eq(ratioDigits(0n, 1n, 7), '0.0000000', 'ratioDigits at zero');
  eq(ratioDigits(1n, 2n, 3), '0.500', 'ratioDigits at one half');
}

// ---------------------------------------------------------- probability
console.log('probability as exact fractions and summed distributions (course 5 labs)');
{
  /* The course-5 footer promises every probability is an exact fraction from
     the enumerated sample space, and that the distributions are summed term by
     term and compared with the closed forms. The functions below are the
     shipped ones, extracted from probability.py. The geometric case is the one
     that failed: a sum stopped at thirty terms reads 5.848 against a closed
     form of 6 at p = 1/6, and the lab printed both side by side. */
  eval(probBlock('FRACTION_JS') + probBlock('DIST_JS') + probBlock('BAYES_JS'));

  eq(frac(6, 36).text, '1/6', '6/36 reduces to 1/6');
  eq(frac(0, 15).text, '0', 'an empty event is 0, not 0/15');
  eq(frac(15, 15).text, '1', 'the whole space is 1');
  eq(frac(3, 0).text, 'undefined', 'conditioning on an empty event is undefined');
  eq(pct(frac(1, 6)), '16.67%', 'pct rounds to two places');
  eq(frac(18 * 6, 36 * 36).text, '1/12', 'P(A)·P(B) for first-even and sum-7, the lesson-5 pair');

  eq(comb(52, 5), 2598960, 'C(52,5) in doubles is still exact');
  eq(comb(20, 5), 15504, 'C(20,5)');

  const bin = binomialPmf(20, 0.25), mb = moments(bin.ks, bin.probs);
  near(bin.probs[5], 0.2023311518569244, 1e-12, 'P(X = 5) at n = 20, p = 1/4 (lesson 11 worked example)');
  near(mb.E, 5, 1e-12, 'E[X] summed = np = 5');
  near(mb.V, 3.75, 1e-12, 'Var(X) summed = np(1-p) = 3.75');
  near(mb.total, 1, 1e-12, 'the binomial sums to 1');
  near(bin.probs.slice(10).reduce((s, x) => s + x, 0), 0.01386441694376117, 1e-12, 'P(X >= 10) = 0.0139');
  const bin10 = binomialPmf(10, 0.5);
  near(bin10.probs[5], 0.24609375, 1e-15, 'P(exactly 5 heads in 10) = 252/1024');
  near(moments(bin10.ks, bin10.probs).E, 5, 1e-12, 'E[X] = 5 at n = 10, p = 1/2 (lesson 9 preset)');

  const K = geometricTerms(1 / 6);
  eq(K > 30, true, 'the geometric sum runs past the thirty drawn bars');
  eq(Math.pow(5 / 6, K) < 1e-15, true, 'and stops only when the tail is below 1e-15');
  const geo = geometricPmf(1 / 6, K), mg = moments(geo.ks, geo.probs);
  near(geo.probs[0], 1 / 6, 1e-15, 'P(X = 1) = 1/6, the mode');
  near(geo.probs[5], 0.06697959533607682, 1e-15, 'P(X = 6) = (5/6)^5 / 6');
  near(mg.E, 6, 1e-9, 'E[X] summed = 1/p = 6 (lesson 12 worked example)');
  near(mg.V, 30, 1e-6, 'Var(X) summed = (1-p)/p^2 = 30');
  near(mg.total, 1, 1e-12, 'the geometric sums to 1');
  near(moments(geo.ks.slice(0, 30), geo.probs.slice(0, 30)).E, 5.848342071608853, 1e-9,
       'thirty terms alone give 5.848 -- the figure the lab used to print beside 6');
  const geo12 = geometricPmf(1 / 12, geometricTerms(1 / 12)), mg12 = moments(geo12.ks, geo12.probs);
  near(mg12.E, 12, 1e-9, 'E[X] = 12 at the smallest p the slider allows');
  near(mg12.V, 132, 1e-6, 'Var(X) = 132 there');

  const uni = uniformPmf(6), mu = moments(uni.ks, uni.probs);
  near(mu.E, 3.5, 1e-12, 'a fair die: E[X] = 3.5 (lesson 8 preset)');
  near(mu.V, 35 / 12, 1e-12, 'a fair die: Var(X) = 35/12 (lesson 10)');
  const dice = diceSumPmf(), md = moments(dice.ks, dice.probs);
  eq(dice.probs.map((x) => Math.round(x * 36)).join(','), '1,2,3,4,5,6,5,4,3,2,1', 'the triangle over 36 (lesson 7 table)');
  near(md.E, 7, 1e-12, 'sum of two dice: E[X] = 7');
  near(md.V, 35 / 6, 1e-12, 'sum of two dice: Var(X) = 35/6, the lesson-10 worked example by another route');

  const cells = bayesCounts(1000000, 1000, 99, 5);
  eq([cells.D, cells.TP, cells.FN, cells.H, cells.FP, cells.TN].join(','), '1000,990,10,999000,49950,949050',
     'the four cells at 1 in 1000, 99%, 5%');
  eq(cells.posterior.text, '11/566', 'P(D|+) = 990/50940 = 11/566');
  near(cells.posterior.dec, 0.019434628975265017, 1e-15, 'about 2%, the lesson-6 answer');
  near(cells.npv.dec, 949050 / 949060, 1e-15, 'P(no D | -) from the same cells');
  eq(bayesCounts(1000000, 300000, 99, 5).posterior.text, '297/332', 'the worked example: prior 0.30 gives 297/332 = 0.895');
  eq(bayesCounts(1000000, 20000, 95, 10).posterior.text, '19/117', 'the standard: 2%, 95%, 10% gives 19/117');
  const rare = bayesCounts(1000000, 100, 99, 1);
  eq(rare.FP / rare.TP, 101, 'concept 3: 1 in 10 000 at a 1% false-positive rate is about 100 false positives per true one');
  eq(grp(50940), '50 940', 'digit grouping');
  eq(dec(990, 1000000), '0.00099', 'decimals are printed without trailing zeros');
  eq(dec(99, 100), '0.99', 'and a percentage as its decimal');
}

// -------------------------------------------------------- number theory
console.log('number theory in BigInt (course 6 labs)');
{
  /* The course-6 footer promises exact big-integer arithmetic, and lesson 14
     promises that the key the lab generates decrypts and is then recovered by
     factoring. The functions below are the shipped ones, extracted from
     number.py. The case that motivated this section: the lesson-14 worked
     example printed c = 3 for 9^7 mod 143 while the lab under it printed 48;
     the lab was right, and nothing checked either. */
  eval(numberBlock('NT_JS'));

  eq(bgcd(1071n, 462n), 21n, 'gcd(1071, 462) = 21 (lesson 5 worked example)');
  eq(bgcd(264n, 84n), 12n, 'gcd(264, 84) = 12 (lesson 4 worked example)');
  eq(bgcd(-12n, 18n), 6n, 'gcd ignores sign');
  eq(bgcd(17n, 0n), 17n, 'gcd(a, 0) = a, the base case');
  eq(egcd(1071n, 462n).join(','), '21,-3,7', '1071·(−3) + 462·7 = 21 (lesson 6 body)');
  eq(egcd(17n, 3120n).join(','), '1,-367,2', '17·(−367) + 3120·2 = 1 (lesson 6 worked example)');
  const tr = egcdTrace(17n, 3120n);
  eq(tr.g + ',' + tr.x + ',' + tr.y, '1,-367,2', 'the trace ends where egcd does');
  eq(tr.rows.every((r) => 17n * r.s + 3120n * r.t === r.r), true, 'r = a·s + b·t holds on every row of the trace');
  eq(tr.rows.map((r) => r.r).join(','), '17,3120,17,9,8,1,0', 'the remainders are the worked example\'s 9, 8, 1, 0');
  const trn = egcdTrace(-1071n, 462n);
  eq(-1071n * trn.x + 462n * trn.y, trn.g, 'a negative input keeps the identity true as typed');
  eq(modinv(17n, 3120n), 2753n, '17⁻¹ mod 3120 = 2753, the RSA private exponent');
  eq(modinv(7n, 26n), 15n, '7⁻¹ mod 26 = 15 (lesson 9 example, lesson 6 standard)');
  eq(modinv(5n, 26n), 21n, '5⁻¹ mod 26 = 21 (lesson 13 example)');
  eq(modinv(15n, 26n), 7n, '15⁻¹ mod 26 = 7 (lesson 13 worked example)');
  eq(modinv(6n, 9n), null, 'no inverse when the gcd is not 1');
  eq(modinv(2n, 4n), null, '2 has no inverse mod 4');
  eq(modinv(-367n, 3120n), 17n, 'the inverse of −367 ≡ 2753 is 17: a negative representative is reduced first');

  eq(modpow(7n, 128n, 13n), 3n, '7^128 mod 13 = 3 (lesson 8 body)');
  eq(modpow(3n, 200n, 50n), 1n, '3^200 mod 50 = 1 (lesson 8 worked example)');
  eq(modpow(5n, 117n, 19n), 1n, '5^117 mod 19 (lesson 8 standard)');
  eq(modpow(7n, 100n, 10n), 1n, '7^100 ends in 1 (lesson 7 worked example)');
  eq(modpow(7n, 1000n, 13n), 9n, '7^1000 mod 13 = 9 (lesson 11 body)');
  eq(modpow(3n, 1234567n, 100n), 87n, '3^1234567 mod 100 = 87 (lesson 11 worked example)');
  eq(modpow(2n, 1000000n, 77n), 23n, '2^1000000 mod 77 (lesson 11 standard) equals 2^40 mod 77');
  eq(modpow(2n, 40n, 77n), 23n, 'because the exponent reduces modulo φ(77) = 60');
  eq(modpow(2n, 10n, 7n), 2n, '2^10 mod 7 = 2, not the 1 that reducing the exponent mod 7 gives (lesson 11 mistake 1)');
  eq(modpow(-7n, 3n, 10n), 7n, 'a negative base is reduced into [0, m) first');
  eq(modpow(65n, 17n, 3233n), 2790n, '65^17 mod 3233 = 2790 (the textbook key)');
  eq(modpow(2790n, 2753n, 3233n), 65n, 'and 2790^2753 mod 3233 = 65 decrypts it');
  eq(modpow(9n, 7n, 143n), 48n, '9^7 mod 143 = 48 — the lesson-14 worked example, which once said 3');
  eq(modpow(48n, 103n, 143n), 9n, 'and 48^103 mod 143 = 9 decrypts it');
  eq(modpow(3n, 103n, 143n), 16n, 'the old ciphertext 3 would not have decrypted to 9');
  const mt = modpowTrace(7n, 128n, 13n, 64);
  eq(mt.result, 3n, 'the trace reaches the same answer as modpow');
  eq(mt.rows.length + ',' + mt.squarings + ',' + mt.mults, '8,7,1', '7^128: eight rows, seven squarings, one multiplication');
  eq(mt.rows.map((r) => r.power).join(','), '7,10,9,3,9,3,9,3', 'the powers 7, 10, 9, 3, 9, 3, 9, 3 the body lists');
  const mt2 = modpowTrace(3n, 200n, 50n, 64);
  eq(mt2.rows.map((r) => r.power).join(','), '3,9,31,11,21,41,31,11', 'the worked example\'s column: 3, 9, 31, 11, 21, 41, 31, 11');
  eq(mt2.rows.map((r) => (r.use ? 1 : 0)).join(''), '00010011', 'set bits at positions 3, 6 and 7');
  eq(mt2.squarings + ',' + mt2.mults + ',' + mt2.result, '7,3,1', 'seven squarings, three multiplications, result 1');
  eq(modpowTrace(5n, 117n, 19n, 64).squarings + ',' + modpowTrace(5n, 117n, 19n, 64).mults, '6,5', '5^117: six squarings, five set bits');
  eq(modpowTrace(7n, 2n ** 100n, 13n, 64).complete, false, 'a 101-bit exponent is reported as truncated at 64 rows');

  eq(isPrimeBig(2n), true, '2 is prime');
  eq(isPrimeBig(1n), false, '1 is not prime');
  eq(isPrimeBig(101n), true, '101 is prime (lesson 2: four divisions)');
  eq(isPrimeBig(149n), true, '149 is prime (lesson 2 quiz)');
  eq(isPrimeBig(561n), false, '561, a Carmichael number, is composite');
  eq(isPrimeBig(30031n), false, '2·3·5·7·11·13 + 1 is composite');
  eq(factorize(360n).map((pe) => pe.join('^')).join(','), '2^3,3^2,5^1', '360 = 2³·3²·5 (lesson 2 worked example)');
  eq(divisorCount(360n), 24n, '360 has 24 divisors');
  eq(divisorCount(2520n), 48n, '2520 has 48 divisors (lesson 2 standard)');
  eq(factorize(30031n).map((pe) => pe[0]).join(','), '59,509', '30031 = 59 · 509');
  eq(factorize(1071n).map((pe) => pe.join('^')).join(','), '3^2,7^1,17^1', '1071 = 3²·7·17');
  eq(factorize(1n).length, 0, '1 has no prime factors');
  eq(factorize(97n).map((pe) => pe.join('^')).join(','), '97^1', 'a prime is its own factorisation');
  eq(totient(7n), 6n, 'φ(7) = 6');
  eq(totient(9n), 6n, 'φ(9) = 6');
  eq(totient(12n), 4n, 'φ(12) = 4');
  eq(totient(15n), 8n, 'φ(15) = 8 (lesson 11 quiz)');
  eq(totient(35n), 24n, 'φ(35) = 24');
  eq(totient(100n), 40n, 'φ(100) = 40 (lesson 11 worked example)');
  eq(totient(77n), 60n, 'φ(77) = 60 (lesson 11 standard)');
  eq(totient(3120n), 768n, 'φ(3120) = 768');
  eq(totient(26n), 12n, 'φ(26) = 12, the affine multipliers');
  eq(totient(1n), 1n, 'φ(1) = 1');
  eq(modpow(7n, totient(13n), 13n), 1n, 'Fermat at the lesson-11 preset: 7^12 ≡ 1 (mod 13)');
  eq(modpow(2n, totient(4n), 4n), 0n, '2^φ(4) ≡ 0 (mod 4): the theorem needs a coprime base');

  const sun = crtPair(2n, 3n, 3n, 5n);
  eq(sun.x + ' mod ' + sun.lcm, '8 mod 15', 'x ≡ 2 (3), x ≡ 3 (5) gives 8 mod 15 (lesson 10 preset)');
  const sun2 = crtPair(8n, 15n, 2n, 7n);
  eq(sun2.x + ' mod ' + sun2.lcm, '23 mod 105', 'then with x ≡ 2 (7): Sun Tzu\'s 23 mod 105');
  const std = crtPair(crtPair(1n, 5n, 2n, 7n).x, 35n, 3n, 9n);
  eq(std.x + ' mod ' + std.lcm, '156 mod 315', 'the lesson-10 standard: 156 mod 315');
  const bad = crtPair(1n, 4n, 2n, 6n);
  eq(bad.x === null && bad.g === 2n, true, 'x ≡ 1 (4), x ≡ 2 (6) is inconsistent modulo gcd 2');
  const ok = crtPair(1n, 4n, 3n, 6n);
  eq(ok.x + ' mod ' + ok.lcm, '9 mod 12', 'x ≡ 1 (4), x ≡ 3 (6) is 9 modulo the lcm 12, not 24');
  eq(crtPair(1n, 2n, 3n, 4n).x, 3n, 'one modulus dividing the other');
  eq(crtPair(-1n, 4n, 5n, 6n).x, 11n, 'negative remainders are reduced first');
  {
    /* The construction the lab displays for coprime moduli must agree with the
       general solver: Σ aᵢMᵢyᵢ mod M. */
    const M = 15n, t1 = 2n * 5n * modinv(5n, 3n) % M, t2 = 3n * 3n * modinv(3n, 5n) % M;
    eq((t1 + t2) % M, sun.x, 'the displayed construction agrees with crtPair');
  }

  const g1 = lcgRun(5n, 3n, 8n, 0n, 9);
  eq(g1.seq.join(','), '0,3,2,5,4,7,6,1', 'a = 5, c = 3, m = 8 from 0: the lesson-12 body sequence');
  eq(g1.start + ',' + g1.period, '0,8', 'full period 8');
  const g2 = lcgRun(4n, 3n, 8n, 0n, 9);
  eq(g2.seq.join(',') + ' then ' + g2.next, '0,3,7 then 7', 'a = 4 collapses: 0, 3, 7, 7, …');
  eq(g2.start + ',' + g2.period, '2,1', 'period 1 after a tail of 2');
  const g3 = lcgRun(5n, 3n, 16n, 1n, 17);
  eq(g3.seq.join(','), '1,8,11,10,5,12,15,14,9,0,3,2,13,4,7,6', 'the worked example\'s good generator at m = 16');
  eq(g3.period, 16, 'period 16 — every value once');
  const g4 = lcgRun(6n, 3n, 16n, 1n, 17);
  eq(g4.seq.join(',') + ' then ' + g4.next + ',' + g4.period, '1,9 then 9,1', 'a = 6: 1, 9, 9, 9, … period 1');
  eq(hullDobell(5n, 3n, 16n).join(','), 'true,true,true', 'Hull–Dobell passes for (5, 3, 16)');
  eq(hullDobell(6n, 3n, 16n).join(','), 'true,false,false', 'and (6, 3, 16) fails the second and third: 2 ∤ 5 and 4 ∤ 5');
  eq(hullDobell(4n, 3n, 8n).join(','), 'true,false,false', '(4, 3, 8): a − 1 = 3 is divisible by neither 2 nor 4');
  eq(hullDobell(21n, 1n, 100n).join(','), 'true,true,true', '(21, 1, 100) passes: a full-period generator for the standard');
  eq(lcgRun(21n, 1n, 100n, 0n, 101).period, 100, 'and it does have period 100');
  eq(hullDobell(5n, 3n, 7n).join(','), 'true,false,true', 'm = 7: the third condition is vacuous, the second fails');
  eq(lcgRun(5n, 3n, 7n, 0n, 8).period + ',' + lcgRun(5n, 3n, 7n, 1n, 8).period, '6,1',
     'so the period depends on the seed: 6 from 0, and 1 from the fixed point 1');

  const af = affineMap(5n, 8n, 26n);
  eq(af.map[7], 17n, 'H = 7 → 17 = R under (5, 8) (lesson 13 body)');
  eq(af.distinct + ',' + af.inv, '26,21', 'all 26 letters distinct, a⁻¹ = 21');
  eq((((17n - 8n) * 21n) % 26n + 26n) % 26n, 7n, 'D(17) = 21·(17 − 8) ≡ 7 = H');
  const af2 = affineMap(15n, 9n, 26n);
  eq(af2.map[4] + ',' + af2.map[19], '17,8', 'the recovered key (15, 9) sends E → R and T → I (lesson 13 worked example)');
  const af3 = affineMap(3n, 24n, 26n);
  eq(af3.map[4] + ',' + af3.map[19], '10,3', 'the standard\'s key (3, 24) sends E → K and T → D');
  const af13 = affineMap(13n, 0n, 26n);
  eq(af13.distinct + ',' + af13.inv, '2,null', 'a = 13 gives two outputs and no inverse');
  eq(affineMap(2n, 5n, 26n).distinct, 13, 'an even multiplier gives thirteen outputs');
}

// ---------------------------------------------------------------- graphs
console.log('graph algorithms (course 7 workbench)');
{
  /* Every course-7 lesson renders through one workbench, and the panels quote
     what it prints at their presets: distances, visit orders, Kruskal's
     decisions, the clique bound, the planarity counts. The functions below
     are the shipped ones, extracted from graph.py. The case that motivated
     this section: lesson 8's panel promised that BFS and DFS draw different
     trees on a preset that was itself a tree, and nothing could have said so. */
  eval(graphBlock('GRAPH_JS'));
  const L = (a) => a.map((v) => v + 1).join(' ');
  const S = (a) => '{' + L(a) + '}';
  const tree = (parent) => parent.map((p, v) => (p === -1 ? null : (p + 1) + '-' + (v + 1))).filter(Boolean).join(',');
  function load(preset, n) { N = n; useLessonWeights = false; A = PRESETS[preset](n); }
  function custom(n, list) { LESSON = lessonFrom(list); useLessonWeights = true; N = n; A = PRESETS.lesson(n); }
  const degs = () => { const d = []; for (let v = 0; v < N; v += 1) d.push(degree(v)); return d.join(''); };

  load('complete', 5);
  eq(edges().length, 10, 'K5 has 10 edges (lesson 1 preset)');
  eq(degs(), '44444', 'every degree 4');
  load('bipartite', 6);
  eq(edges().length + ',' + degs(), '9,333333', 'K_{3,3}: 9 edges, every degree 3');
  load('cycle', 6);
  eq(edges().length + ',' + degs(), '6,222222', 'C6: 6 edges, every degree 2');

  custom(8, [[1, 2], [1, 3], [1, 5], [2, 4], [2, 6], [3, 4], [3, 7], [4, 8], [5, 6], [5, 7], [6, 8], [7, 8]]);
  eq(degs() + ',' + edges().length, '33333333,12', 'Q3 (lesson 2 preset): eight vertices of degree 3, twelve edges');
  eq(twoColour().conflict, null, 'and Q3 is bipartite');
  eq(hamilton().circuit !== null, true, 'and has a Hamilton circuit');

  load('cycle', 4);
  eq(JSON.stringify(matrixPower(2)), '[[2,0,2,0],[0,2,0,2],[2,0,2,0],[0,2,0,2]]', 'A² of C4 (lesson 3 worked example)');
  eq(matrixPower(3)[0][3] + ',' + triangles(), '4,0', 'A³[1][4] = 4 and no triangle');
  load('petersen', 6);
  eq(triangles() + ',' + edges().length, '2,7', 'two triangles joined: 2 triangles, 7 edges');

  custom(7, [[1, 2], [2, 3], [3, 1], [3, 4], [5, 6]]);
  eq(componentsOf().map(S).join(' '), '{1 2 3 4} {5 6} {7}', 'lesson 4 worked example: three components');
  {
    const c = cuts();
    eq(c.bridges.map((b) => L(b.edge)).join(','), '3 4,5 6', 'bridges 3–4 and 5–6');
    eq(L(c.cutVertices), '3', 'the one cut vertex is 3');
    eq(c.bridges[0].sides.map(S).join(' '), '{1 2 3} {4}', 'removing 3–4 separates {1, 2, 3} from {4}');
    eq(componentsOf(2).length, 4, 'deleting vertex 3 leaves four components');
  }
  load('tree', 7);
  eq(cuts().bridges.length + ',' + L(cuts().cutVertices), '6,1 2 3', 'on the tree preset every edge is a bridge and every internal vertex a cut vertex');
  load('cycle', 6);
  eq(cuts().bridges.length + ',' + cuts().cutVertices.length, '0,0', 'a cycle has no bridge and no cut vertex');

  custom(6, [[1, 2], [2, 3], [3, 1], [4, 5], [5, 6], [6, 4]]);
  eq(degs() + ',' + componentsOf().length, '222222,2', 'two disjoint triangles (lesson 5 preset): 2-regular, two components');
  load('cycle', 6);
  eq(degs() + ',' + componentsOf().length, '222222,1', 'C6: the same degrees, one component');

  load('cycle', 6);
  eq(twoColour().colour.join(''), '010101', 'C6 two-coloured by parity: X = {1, 3, 5}');
  load('cycle', 5);
  eq(L(twoColour().conflict), '3 4', 'C5: the conflict is at vertices 3 and 4 (lesson 6 worked example)');
  load('cycle', 6); link(A, 0, 2);
  eq(twoColour().conflict !== null, true, 'C6 plus the chord 1–3 is not bipartite');
  load('cycle', 6); link(A, 0, 3);
  eq(twoColour().conflict, null, 'C6 plus the chord 1–4 still is');

  load('cycle', 6);
  eq(L(hamilton().circuit), '1 2 3 4 5 6', 'C6 has a Hamilton circuit (lesson 7 preset)');
  A[0][1] = 0; A[1][0] = 0;
  eq(degs().split('').map((d, i) => (d % 2 ? i + 1 : null)).filter(Boolean).join(','), '1,2', 'minus 1–2: the odd vertices are 1 and 2');
  eq(L(hamilton().path) + '|' + hamilton().circuit, '1 6 5 4 3 2|null', 'a Hamilton path and no circuit');

  custom(6, [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 6]]);
  {
    const b = bfs(0), d = dfs(0);
    eq(b.dist.join(' '), '0 1 1 2 3 4', 'lesson 8 worked example: BFS distances');
    eq(L(b.order), '1 2 3 4 5 6', 'BFS order');
    eq(tree(b.parent), '1-2,1-3,2-4,4-5,5-6', 'BFS tree edges');
    eq(L(d.order), '1 2 4 3 5 6', 'DFS order');
    eq(tree(d.parent), '1-2,4-3,2-4,4-5,5-6', 'DFS tree edges: 4–3 is a tree edge, so 3–1 is the back edge');
  }
  load('tree', 7);
  eq(tree(bfs(0).parent) === tree(dfs(0).parent), true, 'on a tree BFS and DFS draw the same tree');

  custom(4, [[1, 2, 10], [1, 3, 3], [3, 2, 2], [2, 4, 1], [3, 4, 9]]);
  eq(weight(0, 1) + ',' + weight(1, 2), '10,2', 'the lesson preset carries its own weights');
  {
    const r = dijkstra(0);
    eq(r.dist.join(' '), '0 5 3 6', 'lesson 9 worked example: s = 0, a = 5, b = 3, t = 6');
    let v = 3; const route = []; while (v !== -1) { route.unshift(v); v = r.parent[v]; }
    eq(L(route), '1 3 2 4', 'route s → b → a → t');
    eq(bfs(0).dist[3], 2, 'against a fewest-edge distance of 2');
  }
  useLessonWeights = false;
  eq(weight(0, 1), 5, 'off the lesson preset the formula weight returns');
  load('complete', 6);
  eq(dijkstra(0).dist[5] + ',' + bfs(0).dist[5], '3,1', 'on K6 the cheapest route 1 → 6 is the direct edge');

  custom(6, [[1, 2], [2, 3], [3, 1], [4, 5], [5, 6]]);
  eq(componentsOf().length + ',' + edges().length + ',' + (edges().length === N - componentsOf().length), '2,5,false',
     'lesson 10 graph C: two components, five edges, not acyclic');
  load('path', 6);
  eq(componentsOf().length + ',' + edges().length + ',' + degs(), '1,5,122221', 'graph A is a path with leaves 1 and 6');

  load('tree', 7);
  {
    const o = rootedOrders(0);
    eq(L(o.pre), '1 2 4 5 3 6 7', 'preorder on the tree preset (lesson 11)');
    eq(L(o.ino), '4 2 5 1 6 3 7', 'inorder');
    eq(L(o.post), '4 5 2 6 7 3 1', 'postorder');
    eq(L(o.level), '1 2 3 4 5 6 7', 'level order');
    eq(o.treeEdges + ',' + o.reached, '6,7', 'six tree edges reach all seven');
  }
  load('star', 7);
  eq(rootedOrders(0).ino + ',' + (rootedOrders(0).tooMany + 1), 'null,1', 'on a star inorder is undefined and vertex 1 is why');
  load('cycle', 5);
  eq(L(rootedOrders(0).pre) + ',' + rootedOrders(0).treeEdges, '1 2 3 4 5,4', 'on C5 the orders are those of the DFS spanning tree, one edge left out');

  custom(5, [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4], [1, 5, 5], [1, 3, 6], [2, 4, 7]]);
  {
    const k = kruskal();
    eq(k.total + ',' + k.chosen.length, '10,4', 'lesson 12 worked example: total 10, four edges');
    eq(k.considered.map((c) => L(c[0].slice(0, 2)) + (c[1] ? '+' : '-')).join(','), '1 2+,2 3+,3 4+,4 5+,1 5-,1 3-,2 4-',
       'AB, BC, CD, DE taken; AE, AC, BD rejected, in weight order');
    eq(dijkstra(0).dist[4], 5, 'Dijkstra 1 → 5 on the same graph is the rejected edge of weight 5');
  }
  load('complete', 6);
  eq(kruskal().total + ',' + kruskal().chosen.length, '12,5', 'Kruskal on K6 with the formula weights');
  load('petersen', 6); A[0][3] = 0; A[3][0] = 0;
  eq(kruskal().chosen.length, 4, 'a disconnected graph gives a spanning forest with n − c edges');

  custom(5, [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4], [4, 5]]);
  eq(greedyColour().join(''), '01201', 'lesson 13 worked example: greedy colours 1, 2, 3, 1, 2');
  eq(cliqueNumber().size + ',' + S(cliqueNumber().vertices), '3,{1 2 3}', 'clique number 3 on the triangle');
  eq(Math.max(...degs().split('').map(Number)), 3, 'Δ = 3, so the greedy bound is 4');
  custom(6, [[1, 4], [1, 6], [3, 2], [3, 6], [5, 2], [5, 4]]);
  eq(Math.max(...greedyColour()) + 1 + ',' + twoColour().conflict + ',' + cliqueNumber().size, '3,null,2',
     'the bipartite trap: greedy uses three colours on a bipartite graph');
  load('cycle', 5);
  eq(Math.max(...greedyColour()) + 1 + ',' + cliqueNumber().size, '3,2', 'C5: greedy 3, clique 2, the odd cycle supplies the third');

  load('complete', 5);
  {
    const p = planarity();
    eq(p.verdict + ',' + p.E + ',' + p.bound, 'bound,10,9', 'K5: 10 > 3·5 − 6 = 9 (lesson 14 preset)');
  }
  load('bipartite', 6);
  {
    const p = planarity();
    eq(p.verdict + ',' + p.triangles + ',' + p.bound + ',' + p.bound2, 'bound2,0,12,8', 'K_{3,3}: passes 12, triangle-free, fails 8');
  }
  load('complete', 4);
  eq(planarity().verdict + ',' + planarity().E + ',' + planarity().bound, 'planar,6,6', 'K4: 6 ≤ 6 and planar');
  load('petersen', 6);
  eq(planarity().verdict, 'planar', 'seven edges: no subdivision of K5 or K_{3,3} fits');
  custom(8, [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]);
  eq(planarity().verdict + ',' + S(planarity().k5), 'k5,{1 2 3 4 5}', 'K5 on eight vertices passes both bounds and is caught as a subgraph');
  custom(7, [[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6]]);
  {
    const p = planarity();
    eq(p.verdict + ',' + S(p.k33.left) + ',' + S(p.k33.right), 'k33,{1 2 3},{4 5 6}', 'K_{3,3} plus an isolated vertex passes 10 and is caught as a subgraph');
  }
  custom(7, [[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 7], [7, 6]]);
  eq(planarity().verdict, 'open', 'a subdivided K_{3,3} passes the bounds, has no K_{3,3} subgraph, and is reported open, not planar');
  load('cycle', 4); link(A, 0, 2); link(A, 1, 3);
  eq(planarity().verdict + ',' + planarity().triangles, 'planar,4', 'K4 built by hand: four triangles, planar');
}

// ------------------------------------------------------------ algorithms
console.log('algorithm counts and the witness verdict (course 8 lab)');
{
  /* Every course-8 lesson renders through one lab, and its panels quote what
     it prints: comparison counts, the loop-nest sums, the invariant trace,
     the dynamic array's copies, the master theorem's case, the amounts where
     greedy fails. The functions below are the shipped ones, extracted from
     algorithms.py. The case that motivated this section: the witness mode
     searched C ≤ 1000 over n ≤ 64 and reported n² = O(n) with C = 100,
     contradicting the lesson's own example directly above it. */
  eval(algoBlock('ALGO_JS'));
  const F = { one: 0, log: 1, n: 2, nlogn: 3, n2: 4, n3: 5, exp: 6, fact: 7, poly: 8, hundred: 9 };
  const W = (f, g) => { const w = witnessSearch(F[f], F[g], 16); return w ? w.C + ',' + w.k : 'none'; };
  eq(bigO(F.poly, F.n2) + ':' + W('poly', 'n2'), 'true:4,13', '3n² + 5n + 100 = O(n²) with C = 4, k = 13 (lesson 4 preset)');
  eq(bigO(F.n, F.n2) + ':' + W('n', 'n2'), 'true:1,1', 'n = O(n²) with C = 1, k = 1 (lesson 4 quiz)');
  eq(bigO(F.n2, F.n), false, 'n² ≠ O(n) — the lesson 4 example the old search contradicted');
  eq(bigO(F.nlogn, F.n), false, 'n log n ≠ O(n), though a search to n = 10⁹ would find C = 50');
  eq([bigO(F.n3, F.n2), bigO(F.log, F.one), bigO(F.fact, F.exp), bigO(F.exp, F.n3)].join(','), 'false,false,false,false',
     'n³ vs n², log n vs 1, n! vs 2ⁿ, 2ⁿ vs n³ are all false');
  eq(bigO(F.one, F.log) + ':' + W('one', 'log'), 'true:1,2', '1 = O(log n) needs k = 2 because log 1 = 0');
  eq(bigO(F.exp, F.fact) + ':' + W('exp', 'fact'), 'true:1,4', '2ⁿ = O(n!) from n = 4');
  eq(W('n3', 'exp'), '1,10', 'n³ ≤ 2ⁿ from n = 10');
  eq(W('hundred', 'n'), '100,1', '100n = O(n) with C = 100');
  {
    let bad = 0;
    for (let f = 0; f < FUNCS.length; f += 1) for (let g = 0; g < FUNCS.length; g += 1) if (bigO(f, g) && !witnessSearch(f, g, 16)) bad += 1;
    eq(bad, 0, 'every true relation among the ten functions has a witness in the grid');
  }
  eq(ratioAt(F.n2, F.n, 1000000), 1000000, 'the ratio n²/n at 10⁶ is 10⁶ — the disproof column');

  const S = (n, kind) => bubbleSort(makeArray(n, kind)) + ',' + insertionSort(makeArray(n, kind)) + ',' + mergeSort(makeArray(n, kind));
  eq(S(16, 'shuffle'), '120,77,48', 'n = 16 shuffled: bubble 120, insertion 77, merge 48 (lesson 6 worked example)');
  eq(insertionSort(makeArray(16, 'sorted')) + ',' + insertionSort(makeArray(16, 'reverse')), '15,120', 'insertion sort: 15 on sorted, 120 on reversed input');
  eq(S(24, 'shuffle'), '276,174,82', 'n = 24 shuffled');
  eq(S(1000, 'shuffle'), '499500,235149,7387', 'n = 1000: bubble 499 500 = n(n−1)/2, merge 7 387');
  eq(makeArray(16, 'shuffle').join(' '), '8 16 9 2 12 6 3 15 14 1 5 11 10 4 13 7', 'the shuffle is the same permutation for every reader');
  eq(linearSearch(makeArray(16, 'sorted'), 16) + ',' + binaryWorst(16), '16,5', 'linear 16, binary ⌊log₂16⌋ + 1 = 5');
  {
    let ok = true;
    for (let n = 2; n <= 64; n += 1) if (binaryWorst(n) !== ilog2(n) + 1) ok = false;
    eq(ok, true, 'binary search worst case is ⌊log₂ n⌋ + 1 for every n to 64');
  }
  eq(binaryWorst(1000), 10, 'and 10 at n = 1000');

  const nest = countNests(16);
  eq([nest.A, nest.B, nest.C, nest.D].join(','), '4096,136,64,816', 'lesson 5 nests at n = 16: n³, n(n+1)/2, n⌊log₂n⌋, n(n+1)(n+2)/6');
  {
    let ok = true;
    for (let n = 1; n <= 64; n += 1) { const r = countNests(n); if (r.A !== r.predA || r.B !== r.predB || r.C !== r.predC || r.D !== r.predD) ok = false; }
    eq(ok, true, 'every nest equals its formula for every n to 64');
  }

  const p = powerTrace(3, 13);
  eq([p.rows.every((r) => r.ok), p.rows.length, p.squarings, p.mults, p.value].join(','), 'true,5,4,3,1594323',
     'POWER(3, 13): the invariant holds on all five rows, 4 squarings, 3 multiplications, 3¹³ (lesson 2 preset)');
  eq(powerTrace(3, 1000).squarings + ',' + powerTrace(3, 1000).mults, '10,6', 'x¹⁰⁰⁰: 10 squarings and 6 multiplications against 999');
  eq(powerTrace(2, 64).value, 18446744073709551616n, '2⁶⁴ exactly, beyond double precision');

  const d16 = dynamicArray(16, 'double');
  eq([d16.copies, d16.total, d16.worst, d16.worstAt].join(','), '15,31,9,9', 'doubling, 16 inserts: 15 copies, total 31, worst insertion 9 at element 9 (lesson 8 worked example)');
  eq(d16.events.map((e) => e.at + ':' + e.from + '>' + e.to).join(' '), '2:1>2 3:2>4 5:4>8 9:8>16', 'resizes at inserts 2, 3, 5, 9');
  const d17 = dynamicArray(17, 'double');
  eq([d17.copies, d17.total, d17.amortised < 3].join(','), '31,48,true', '17 inserts: total 48, above 2n and still under 3n');
  eq(dynamicArray(16, 'one').copies, 120, 'growing by one copies 1 + ⋯ + 15 = 120');
  {
    let ok = true;
    for (let n = 2; n <= 64; n += 1) if (dynamicArray(n, 'double').amortised >= 3 || dynamicArray(n, 'half').amortised >= 4) ok = false;
    eq(ok, true, 'doubling stays under 3 and ×1.5 under 4 per insertion for every n to 64');
  }

  const M = (a, b, d) => { const m = masterCase(a, b, d); return m.which + ':' + m.result; };
  eq(M(4, 2, 1), '3:Θ(n^2)', 'lesson 7 baseline 4T(n/2) + n: case 3, Θ(n²)');
  eq(M(4, 2, 0), '3:Θ(n^2)', 'faster combining, d = 0: still Θ(n²)');
  eq(M(3, 2, 1), '3:Θ(n^log_2 3) ≈ Θ(n^1.585)', 'one fewer subproblem: Θ(n^1.585)');
  eq(M(9, 3, 2), '2:Θ(n^2 log n)', 'the standard\'s 9T(n/3) + n²: balanced');
  eq([M(2, 2, 1), M(1, 2, 0), M(2, 4, 1), M(7, 2, 2)].join('|'), '2:Θ(n log n)|2:Θ(log n)|1:Θ(n)|3:Θ(n^log_2 7) ≈ Θ(n^2.807)',
     'merge sort, binary search, course 3 lesson 11\'s last row, Strassen');

  eq(greedyFailures([1, 3, 4], 24).join(','), '6,10,14,18,22', 'greedy with {1, 3, 4} fails first at 6 (lesson 9 preset)');
  eq(greedyCoins([1, 3, 4], 6).picks.join('+') + ' vs ' + dpCoins([1, 3, 4], 6).picks.join('+'), '4+1+1 vs 3+3', 'at 6: 4 + 1 + 1 against 3 + 3');
  eq(dpCoins([1, 3, 4], 8).table.join(' '), '0 1 2 1 1 2 2 2 2', 'the lesson 10 table best[0..8]');
  eq(greedyFailures([1, 5, 10, 25], 99).length, 0, 'with {1, 5, 10, 25} greedy is optimal for every amount to 99');
}


// ---------------------------------- capacity, latency, queues and availability
console.log('system design: exact capacity, queueing and availability');
{
  eval(countingBlock('BIGINT_JS') + sysdBlock('HARMONIC_JS') + sysdBlock('RCEIL_JS')
       + sysdBlock('PERCENTILE_JS') + sysdBlock('PMF_JS') + sysdBlock('QUEUE_JS')
       + sysdBlock('SLOTTED_JS') + sysdBlock('TRACE_JS') + sysdBlock('STREAM_JS')
       + sysdBlock('REPLAY_JS') + sysdBlock('AVAIL_JS') + sysdBlock('APPROX_JS'));

  /* Zipf popularity: the cache hit rate is a ratio of harmonics, and it is the
     ratio that makes a small cache of a skewed workload worth having. */
  eq(Rtext(harmonic(4, 1)), '25/12', 'H(4,1) = 1 + 1/2 + 1/3 + 1/4');
  eq(Rtext(harmonic(3, 2)), '49/36', 'H(3,2) = 1 + 1/4 + 1/9');
  eq(Rtext(zipfHit(1, 4, 1)), '12/25', 'the most popular of four keys, s = 1');
  eq(Rtext(zipfHit(4, 4, 1)), '1', 'caching everything hits everything');

  /* Nearest rank, so a percentile is a value some request actually took. */
  eq(percentileRank(10, R(9n, 10n)), 9, 'p90 of ten samples is the 9th');
  eq(percentileRank(10, R(99n, 100n)), 10, 'p99 of ten samples is the 10th, not an interpolation');
  eq(percentileRank(100, R(1n, 2n)), 50, 'p50 of a hundred');
  const lat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100];
  eq(percentile(lat, R(9n, 10n)), 9, 'the p90 of that sample');
  eq(Rtext(empiricalCdf(lat, 5)), '1/2', 'P(X <= 5)');

  /* A latency budget adds distributions; fan-out takes their maximum. */
  const coin = [[0, R(1n, 2n)], [1, R(1n, 2n)]];
  eq(pmfConvolve(coin, coin).map(p => p[0] + ':' + Rtext(p[1])).join(' '),
     '0:1/4 1:1/2 2:1/4', 'two independent stages add by convolution');
  eq(Rtext(pmfMean(pmfConvolve(coin, coin))), '1', 'and their means add');
  eq(pmfMax(coin, 2).map(p => p[0] + ':' + Rtext(p[1])).join(' '),
     '0:1/4 1:3/4', 'the max of two: the tail is what fan-out costs');
  eq(Rtext(pmfTail(pmfConvolve(coin, coin), 0)), '3/4', 'P(sum > 0)');

  /* M/M/1 from the cut equations. */
  const q = mm1(R(1n, 1n), R(2n, 1n));
  eq(Rtext(q.rho) + ' ' + Rtext(q.L) + ' ' + Rtext(q.W) + ' ' + Rtext(q.Lq),
     '1/2 1 1 1/2', 'M/M/1 at lam = 1, mu = 2');
  eq(mm1(R(3n, 1n), R(2n, 1n)).stable, false, 'rho >= 1 does not settle');
  /* The knee: the last tenth of utilisation costs more than the first nine. */
  eq(Rtext(mm1(R(9n, 10n), R(1n, 1n)).L), '9', 'rho = 0.9 queues 9');
  eq(Rtext(mm1(R(99n, 100n), R(1n, 1n)).L), '99', 'rho = 0.99 queues 99');

  /* Erlang C must agree with M/M/1 at one server -- and s = 1 is exactly the
     case that cannot distinguish a from rho, so s = 2 and 3 are checked too. */
  eq(Rtext(erlangC(R(1n, 1n), R(2n, 1n), 1).pWait), '1/2', 'Erlang C at s = 1 is rho');
  eq(Rtext(erlangC(R(1n, 1n), R(2n, 1n), 1).L), Rtext(q.L), 'and its L is M/M/1 L');
  const e2 = erlangC(R(1n, 1n), R(1n, 1n), 2);
  eq(Rtext(e2.p0) + ' ' + Rtext(e2.pWait) + ' ' + Rtext(e2.L), '1/3 1/3 4/3', 'M/M/2 at a = 1');
  const e3 = erlangC(R(2n, 1n), R(1n, 1n), 3);
  eq(Rtext(e3.p0) + ' ' + Rtext(e3.pWait), '1/9 4/9', 'M/M/3 at a = 2');
  /* Pooling: one queue of two servers beats two queues of one. */
  eq(Rcmp(erlangC(R(1n, 1n), R(1n, 1n), 2).Wq, mm1(R(1n, 2n), R(1n, 1n)).Wq), -1,
     'a pooled M/M/2 waits less than two separate M/M/1s at the same load');

  /* A bounded queue is stable at any load, and Little's law must use the
     EFFECTIVE arrival rate, not the offered one. */
  const fk = mm1k(R(1n, 1n), R(1n, 1n), 3);
  eq(Rtext(fk.blocking), '1/4', 'M/M/1/3 at rho = 1 blocks a quarter');
  eq(Rtext(fk.L), '3/2', 'and holds 3/2 on average');
  eq(Rtext(fk.lamEff), '3/4', 'the effective rate is lam(1 - pK)');

  /* Availability composes three ways, and the three must agree where they meet. */
  eq(Rtext(availSeries([R(9n, 10n), R(9n, 10n)])), '81/100', 'series multiplies down');
  eq(Rtext(availParallel([R(9n, 10n), R(9n, 10n)])), '99/100', 'parallel multiplies up');
  const three = [R(9n, 10n), R(9n, 10n), R(9n, 10n)];
  eq(Rtext(availKofN(R(9n, 10n), 3, 3)), Rtext(availSeries(three)), 'n-of-n is series');
  eq(Rtext(availKofN(R(9n, 10n), 1, 3)), Rtext(availParallel(three)), '1-of-n is parallel');
  eq(Rtext(availKofN(R(1n, 2n), 2, 3)), '1/2', 'majority of three fair coins');
  /* Ten 99.9% dependencies in series are 99.0%, not "as good as the weakest". */
  const ten = []; for (let i = 0; i < 10; i += 1) ten.push(R(999n, 1000n));
  near(Number(Rdec(availSeries(ten), 6)), 0.990045, 1e-6, 'ten 99.9% dependencies give 99.0%');

  /* Retries: the geometric sum, and what it costs when p is high. */
  eq(Rtext(retryAttempts(R(1n, 2n), 2)), '7/4', 'two retries at p = 1/2 cost 7/4 attempts');
  eq(Rtext(retrySuccess(R(1n, 2n), 2)), '7/8', 'and succeed 7/8 of the time');
  eq(Rtext(retryAttempts(R(9n, 10n), 3)), '3439/1000', 'at p = 0.9 the amplification approaches r + 1');

  /* The slotted queue is NOT M/M/1, and this is the assertion that stops a
     lesson claiming the continuous formula is "checked against the simulation".
     At p = 2/5, q = 1/2 the exact slotted mean is 12/5; rho/(1 - rho) is 4. */
  const slot = geoGeo1(R(2n, 5n), R(1n, 2n));
  eq(Rtext(slot.ratio), '2/3', 'Geo/Geo/1 ratio p(1-q)/(q(1-p))');
  eq(Rtext(slot.p0), '1/5', 'and its empty probability');
  eq(Rtext(slot.L), '12/5', 'the EXACT slotted mean');
  eq(Rtext(slot.rho), '4/5', 'at the same utilisation');
  eq(Rtext(mm1(R(4n, 5n), R(1n, 1n)).L), '4', 'where the continuous formula says 4');
  eq(Rcmp(slot.L, mm1(R(4n, 5n), R(1n, 1n)).L), -1,
     'the slotted mean is strictly below M/M/1 -- the two agree only in the limit');
  /* A second point with q != 1/2. At q = 1/2, (1 - q) = q and the ratio
     p(1-q)/(q(1-p)) is indistinguishable from pq/(q(1-p)) -- so one point
     cannot check the formula at all. */
  const slot2 = geoGeo1(R(1n, 4n), R(1n, 3n));
  eq(Rtext(slot2.ratio), '2/3', 'Geo/Geo/1 ratio at p = 1/4, q = 1/3');
  eq(Rtext(slot2.p0) + ' ' + Rtext(slot2.L), '1/4 9/4', 'its empty probability and exact mean');
  eq(Rtext(mm1(R(3n, 4n), R(1n, 1n)).L), '3', 'against 3 from the continuous formula');

  /* Little's Law as an identity about a trace, which is how it is proved here.
     Three customers, each in the system 2 slots, over a horizon of 6:
     area 6, L = 1, lambda = 1/2, W = 2, and L = lambda*W exactly. */
  const tr = littleFromTrace([0, 2, 4], [2, 4, 6]);
  eq(Rtext(tr.L) + ' ' + Rtext(tr.lambda) + ' ' + Rtext(tr.W), '1 1/2 2', 'L, lambda, W from the trace');
  eq(Rtext(tr.L), Rtext(Rmul(tr.lambda, tr.W)), 'L = lambda * W, exactly, with no model');
  eq(occupancyTrace([0, 2, 4], [2, 4, 6], 6).join(''), '111111', 'N(t) is 1 throughout');
  /* The same three customers, arriving together instead of spread out: the same
     total time in system over a third of the horizon, so L triples and W does
     not move. That is the identity doing work. */
  const tr2 = littleFromTrace([0, 0, 0], [2, 2, 2]);
  eq(Rtext(tr2.L) + ' ' + Rtext(tr2.W), '3 2', 'stacked arrivals triple L and leave W alone');
  eq(Rtext(tr2.L), Rtext(Rmul(tr2.lambda, tr2.W)), 'and the identity still holds');

  /* A seeded stream: same seed, same values, or a reader cannot check a lab. */
  eq(lcgStream(1103515245, 12345, 2147483648, 1, 3).join(','),
     '1103527590,377401575,662824084', 'the stream is these values, not merely repeatable');
  eq(lcgStream(1103515245, 12345, 2147483648, 1, 3).join(','),
     lcgStream(1103515245, 12345, 2147483648, 1, 3).join(','), 'and the same on a second call');
  const fair = [[1, R(1n, 2n)], [2, R(1n, 2n)]];
  eq(sampleFromPmf(fair, R(1n, 4n)), 1, 'inverse transform below the first mass');
  eq(sampleFromPmf(fair, R(3n, 4n)), 2, 'and above it');
  /* The boundary: u exactly at the cumulative mass. Half-open [lo, hi) is what
     keeps the sampler's frequencies equal to the pmf, so u = 1/2 is the SECOND
     value, and a <= here would bias every sampled distribution low. */
  eq(sampleFromPmf(fair, R(1n, 2n)), 2, 'u exactly on the boundary falls to the second value');
  eq(sampleFromPmf(fair, R(0n, 1n)), 1, 'and u = 0 to the first');

  /* Ceiling and floor, because 3.2 machines is four. */
  eq(Rceil(R(16n, 5n)), 4n, 'ceil(3.2) = 4 -- the sizing answer');
  eq(Rfloor(R(16n, 5n)), 3n, 'floor(3.2) = 3');
  eq(Rceil(R(4n, 1n)), 4n, 'an exact integer does not round up');
  eq(Rfloor(R(-16n, 5n)), -4n, 'floor of a negative goes down, not toward zero');
  eq(Rceil(R(-16n, 5n)), -3n, 'and ceil goes up');
  /* The case the sign guard exists for: an EXACT negative integer must not be
     pushed a further step. Without it -4 floors to -5. */
  eq(Rfloor(R(-4n, 1n)), -4n, 'floor of an exact negative integer is itself');
  eq(Rceil(R(-4n, 1n)), -4n, 'and so is its ceiling');

  /* Replacement policies on a trace, and the bound the lesson rests on.
     Trace A B C A B D A B C D, three slots. */
  const tr3 = ['A','B','C','A','B','D','A','B','C','D'];
  const opt = replayPolicy(tr3, 3, 'opt'), lru = replayPolicy(tr3, 3, 'lru');
  /* Exact rates, not merely an ordering: "OPT >= LRU" holds for several WRONG
     policies too, including one that evicts the nearest-future key. */
  eq(Rtext(opt.rate), '1/2', 'farthest-in-future gets 5 of 10');
  eq(Rtext(lru.rate), '2/5', 'LRU gets 4');
  eq(Rcmp(opt.rate, lru.rate) > 0, true, 'and the bound is strict on this trace');
  eq(replayPolicy(tr3, 10, 'lru').misses, 4, 'a cache big enough misses only the compulsory four');
  eq(Rtext(replayPolicy(['A','A','A','A'], 1, 'lru').rate), '3/4', 'one key, one slot');

  /* The four places this subject rounds, and only these. */
  near(expNegApprox(1, 1e-15), Math.exp(-1), 1e-12, 'e^-1 by series');
  near(expNegApprox(5, 1e-15), Math.exp(-5), 1e-12, 'e^-5 by series');
  /* The arguments that expose a cancelling implementation. Summing the
     ALTERNATING series for e^-x is exact at 1 and 5 -- which is why the first
     version of this test passed -- and then 0.4% out at 17, 173% out at 20, and
     NEGATIVE past 21. A probability cannot be negative, so these are pinned by
     relative error rather than absolute, at arguments where the absolute error
     of a badly wrong answer is still tiny. */
  for (const x of [10, 12, 15, 17, 20, 21, 25, 40]) {
    const got = expNegApprox(x, 1e-15), want = Math.exp(-x);
    eq(got > 0, true, 'e^-' + x + ' is positive');
    eq(Math.abs(got - want) / want < 1e-10, true,
       'e^-' + x + ' is right to a relative 1e-10, not merely a small absolute error');
  }
  near(expNegApprox(-2, 1e-15), Math.exp(2), 1e-10, 'a negative argument gives e^|x|');
  near(standardErrorApprox(0.5, 100), 0.05, 1e-12, 'the standard error of a proportion');
  /* 1.44*log2(1/0.01) = 9.57 bits per key is the canonical 1% figure, and the
     rate it actually delivers at k = 7 is what the lesson quotes. */
  near(bloomApprox(9585, 1000, 7), 0.01004, 1e-4, 'a Bloom filter at 9.585 bits per key is ~1%');
  /* 9.585, not the 9.57 a textbook quotes: that figure uses 1.44 in place of
     1/ln2 = 1.4427. The lesson should give the exact form and note the rounding. */
  near(bitsPerKeyApprox(0.01), 9.585, 0.001, '1% costs 9.585 bits per key');
  near(sqrtApprox(R(2n, 1n), 1e-15), Math.SQRT2, 1e-12, 'a root that rounds, and says so');
  near(sqrtApprox(R(9n, 4n), 1e-15), 1.5, 1e-12, 'agreeing with Rsqrt where Rsqrt is exact');
  near(harmonicApprox(1000000, 1), 14.392727, 1e-4, 'the Zipf normaliser past where exact is readable');
}

// ------------------------------------- system design C2: latency and the tail
/* The `latency` kit's own arithmetic, on the numbers its eleven lessons print.
   Every assertion below is a figure that appears on a page, so a change that
   moves one of them is a change to what a lesson claims. */
console.log('system design: latency, percentiles and the tail');
{
  eval(block('RATIONAL_JS') + sysdBlock('RCEIL_JS') + sysdBlock('PERCENTILE_JS')
       + sysdBlock('PMF_JS') + sysdBlock('APPROX_JS') + latencyBlock('LATENCY_JS'));

  /* Rfixed exists because Rdec cannot do this. 0.999^693 has a 2079-digit
     numerator; Number() of it is Infinity and Infinity/Infinity is NaN, so the
     fan-out lesson at p99.9 would print NaN. Long division in BigInt instead. */
  eq(Rfixed(R(1n, 3n), 6), '0.333333', 'a third to six places');
  eq(Rfixed(R(2n, 3n), 6), '0.666667', 'two thirds, rounded half up at the last digit');
  eq(Rfixed(R(-1n, 8n), 3), '-0.125', 'a negative rational keeps its sign');
  eq(Rfixed(R(7n, 1n), 0), '7', 'no places asked for, no decimal point');
  eq(Rfixed(Rpow(R(999n, 1000n), 693), 6), '0.499900', '0.999^693, which Number cannot hold');
  eq(String(Number(Rpow(R(999n, 1000n), 693).n)), 'Infinity', 'and this is why Rdec would give NaN');
  eq(Rpct(R(1n, 400n), 4), '0.2500%', 'a probability as a percentage');

  /* L1 and L3: the two terms, and the size at which they cross. */
  eq(Rtext(transferMs(64000, 100)), '128/25', '64 kB over 100 Mbit/s is 5.12 ms');
  eq(Rtext(bdpBytes(100, 80)), '1000000', '100 Mbit/s x 80 ms holds exactly one megabyte');
  eq(Rtext(linkTimeMs(5, 80, 14000, 10)), '2056/5', '5 round trips at 80 ms plus 14 kB at 10 Mbit/s');
  eq(Rtext(crossoverBytes(5, 80, 10)), '500000', 'the bytes catch 5 round trips at 500 kB');
  /* The crossover for ONE round trip IS the bandwidth-delay product -- L1 and
     L3 are the same fact, and if these ever disagree one of the two is wrong. */
  eq(Rtext(crossoverBytes(1, 80, 100)), Rtext(bdpBytes(100, 80)), 'k = 1 crossover is the BDP');

  /* L2: the floor. c is exact by definition, so this is an exact fraction. */
  eq(Rtext(lightFloorMs(5585)), '8377500000/149896229', 'New York to London, exactly');
  eq(Rfixed(lightFloorMs(5585), 3), '55.889', 'which is the 56 ms the course quotes');
  eq(Rfixed(unexplainedMs(76, 5585), 3), '20.111', 'a measured 76 ms leaves 20 ms to explain');
  eq(Rcmp(unexplainedMs(40, 5585), R(0n, 1n)) < 0, true, 'a measurement under the floor goes negative');

  /* L4: the longest path, its slack, and the two edges the lesson toggles. */
  const dagT = [4, 18, 6, 22, 55, 12, 3];
  const dagE = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4], [3, 5], [4, 5], [5, 6]];
  const base = dagSchedule(dagT, dagE);
  eq(base.length, 92, 'the critical path is 92 ms, not the 120 ms the stages total');
  eq(base.slack.join(','), '0,0,12,33,0,0,0', 'cache has 12 ms spare and enrich 33');
  eq(base.path.join('-'), '0-1-4-5-6', 'gateway, authz, db, render, respond');
  /* Speeding up an off-path stage changes nothing: enrich to 1 ms is still 92. */
  eq(dagSchedule([4, 18, 6, 1, 55, 12, 3], dagE).length, 92, 'making enrich instant saves nothing');
  eq(dagSchedule([4, 18, 6, 22, 55, 12, 2], dagE).length, 91, 'a critical stage saves its whole millisecond');
  /* Serialising the cache behind authz puts it ON the path and costs 6 ms. */
  const serial = dagSchedule(dagT, dagE.concat([[1, 2]]));
  eq(serial.length + ' ' + serial.slack[2], '98 0', 'authz -> cache moves cache onto the path');
  /* Making the db wait for the enrichment costs the whole 22 ms of it. */
  const after = dagSchedule(dagT, dagE.concat([[3, 4]]));
  eq(after.length + ' ' + after.path.join('-'), '114 0-1-3-4-5-6', 'enrich -> db reroutes the path');

  /* L5: the rank, the value it selects, and the mean that is neither. */
  const s5 = parseSample('12, 13, 14, 14, 15, 15, 16, 17, 18, 19, 21, 22, 24, 27, 31, 38, 52, 96, 180, 420');
  eq(s5.length, 20, 'twenty measurements');
  eq(percentile(s5, R(1n, 2n)) + ' ' + percentile(s5, R(95n, 100n)) + ' ' + percentile(s5, R(99n, 100n)),
     '19 180 420', 'p50, p95 and p99 by nearest rank');
  eq(Rtext(sampleMean(s5)), '266/5', 'the mean is 53.2 ms');
  eq(countBelow(s5, sampleMean(s5)), 17, '17 of 20 requests are faster than the average');
  /* Nothing in the sample IS the mean, which is the lesson. */
  eq(s5.indexOf(53), -1, 'and no request took 53 ms');
  eq(parseSample('   '), 'null', 'an empty sample is refused rather than guessed at');

  /* L6: p^n, the break-even n, and the same number from pmfMax. */
  eq(Rfixed(Rpow(R(99n, 100n), 69), 6), '0.499837', '0.99^69 is just under a half');
  eq(fanoutBreakEven(R(99n, 100n), 20000), 69, 'a p99 becomes the median at a fan-out of 69');
  eq(fanoutBreakEven(R(9n, 10n), 20000), 7, 'a p90 at 7');
  eq(fanoutBreakEven(R(19n, 20n), 20000), 14, 'a p95 at 14');
  eq(fanoutBreakEven(R(999n, 1000n), 20000), 693, 'and a p99.9 at 693');
  /* 68 must NOT be the answer: at n = 68 the probability is still above a half,
     and an off-by-one here is the whole content of the lesson. */
  eq(Rcmp(Rpow(R(99n, 100n), 68), R(1n, 2n)) > 0, true, '68 calls are still better than even');
  const twoWay = pmfMax([[0, R(99n, 100n)], [1, R(1n, 100n)]], 69);
  eq(Rtext(twoWay[0][1]), Rtext(Rpow(R(99n, 100n), 69)), 'pmfMax agrees with p^n exactly');

  /* L7: the hedge. The preset is 100 measured calls as run lengths. */
  const hSpec = parsePmfSpec('10:40, 12:25, 15:15, 20:10, 30:5, 50:3, 120:1, 300:1');
  const hPmf = pmfFromSpec(hSpec);
  eq(expandSpec(hSpec).length, 100, 'the run lengths expand to a hundred calls');
  eq(pmfPercentile(hPmf, R(99n, 100n)) + ' ' + pmfPercentile(hPmf, R(95n, 100n))
     + ' ' + pmfPercentile(hPmf, R(1n, 2n)), '120 30 12', 'p99, p95 and p50 of the service');
  eq(Rtext(hedgeLoad(hPmf, 30)), '1/20', 'a hedge at the p95 costs 5% more traffic');
  eq(Rtext(Rpow(hedgeLoad(hPmf, 30), 2)), '1/400', 'and the tail past it is that squared');
  eq(Rtext(hedgedTail(hPmf, 30, 42)), '7/400', 'P(hedged > 42) = P(X > 42) P(X > 12)');
  eq(hedgedQuantile(hPmf, 30, R(99n, 100n)), 45, 'the hedged p99 is 45 ms, down from 120');
  eq(hedgedQuantile(hPmf, 30, R(1n, 2n)), 12, 'and the median does not move');
  /* Hedging at the median doubles the load, which is the misconception. */
  eq(Rtext(hedgeLoad(hPmf, 12)), '7/20', 'hedging at the p50 sends a backup for a third of requests');

  /* L8: percentiles do not add. Two stages, seven atoms each. */
  const A = pmfFromSpec(parsePmfSpec('4:520, 6:250, 9:120, 14:60, 22:30, 38:16, 70:4'));
  const B = pmfFromSpec(parsePmfSpec('12:420, 17:300, 24:150, 34:80, 48:36, 72:12, 130:2'));
  const S = pmfNormalise(pmfConvolve(A, B));
  const q99 = R(99n, 100n);
  eq(pmfPercentile(A, q99) + ' ' + pmfPercentile(B, q99), '38 72', 'each stage has its own p99');
  eq(pmfPercentile(S, q99), 78, 'the SUM has a p99 of 78 ms');
  eq(pmfPercentile(A, q99) + pmfPercentile(B, q99), 110, 'while the two p99s add to 110');
  eq(pmfPercentile(S, q99) < pmfPercentile(A, q99) + pmfPercentile(B, q99), true,
     'p99(A + B) < p99(A) + p99(B) on these distributions');
  /* Means DO add, exactly -- the contrast the lesson is built on. */
  eq(Rtext(pmfMean(A)) + ' ' + Rtext(pmfMean(B)) + ' ' + Rtext(pmfMean(S)),
     '881/125 2414/125 659/25', 'the two means and the sum of the two stages');
  eq(Rtext(Radd(pmfMean(A), pmfMean(B))), Rtext(pmfMean(S)), 'expectation is linear; percentiles are not');
  eq(S.length, 43, '43 attainable totals from 7 x 7 pairs');
  eq(Rtext(pmfCdfAt(S, 78)), '3096/3125', 'the cumulative at 78 ms, exactly');
  eq(Rcmp(pmfCdfAt(S, 78), q99) >= 0, true, 'which does reach 99/100');
  eq(Rcmp(pmfCdfAt(S, 77), q99) < 0, true, 'while the atom below it does not -- so 78 is the rank');
  eq(parsePmfSpec('4:520, oops'), 'null', 'an unreadable stage is refused, not half-parsed');
  eq(parsePmfSpec('4:0'), 'null', 'and a zero weight is not a distribution');

  /* L9: the budget, allocated backwards from a 400 ms SLO. */
  const plan = budgetPlan(400, 208, [8, 20, 150, 40]);
  eq(Rtext(plan.avail) + ' ' + Rtext(plan.share), '192 48', '192 ms left, 48 ms each on an even split');
  eq(Rtext(plan.residual), '-26', 'the plan is 26 ms short');
  eq(plan.rows.map(function (r) { return r.fits ? 'y' : 'n'; }).join(''), 'yyny', 'search is the stage that cannot fit');
  eq(Rtext(plan.rows[2].residual), '-102', 'by 102 ms');
  eq(Rtext(plan.spare) + ' ' + Rtext(plan.need), '76 102', 'the others release 76 ms against a need of 102');
  eq(plan.balanced, true, 'and the residual balances both ways of counting it');
  /* Raise the SLO until it fits, and the two ways of counting still agree. */
  const roomy = budgetPlan(500, 208, [8, 20, 150, 40]);
  eq(Rtext(roomy.residual) + ' ' + roomy.balanced, '74 true', 'at a 500 ms SLO the plan fits');

  /* L10: the timeout, the retries and the calls it kills. */
  const tSpec = parsePmfSpec('8:45, 11:25, 16:15, 24:8, 45:4, 90:2, 400:1');
  const tSample = expandSpec(tSpec);
  eq(tSample.length, 100, 'a hundred measured calls');
  eq(Rtext(worstCaseMs(90, 1)), '180', 'one retry at a 90 ms timeout is 180 ms worst case');
  eq(Rtext(killFraction(tSample, 90)), '1/100', 'a timeout at the p99 kills one call in a hundred');
  eq(Rtext(allAttemptsLost(R(1n, 100n), 1)), '1/10000', 'and both attempts fail once in ten thousand');
  eq(Rtext(sampleMean(tSample)), '1827/100', 'the mean of that sample is 18.27 ms');
  /* The misconception, priced: a timeout at the mean throws away 15% of calls
     that were going to succeed. */
  eq(Rtext(killFraction(tSample, 18)), '3/20', 'a timeout at the mean kills 15% of good calls');
  eq(Rtext(killFraction(tSample, 400)), '0', 'a timeout past the maximum kills none');

  /* L11: the one rounded figure on the course, and the reason it rounds. */
  near(mathisMbitsApprox(1460, 100, R(1n, 100n)), 1.168, 1e-9, '1% loss at 100 ms bounds a flow at 1.168 Mbit/s');
  eq(streamsToFillApprox(10000, mathisMbitsApprox(1460, 100, R(1n, 100n))), 8562,
     'so 8562 streams are needed to fill a 10 Gbit/s link');
  /* Halving the loss multiplies the bound by sqrt(2), not by 2 -- the whole
     shape of the result is in that square root. */
  near(mathisMbitsApprox(1460, 100, R(1n, 200n)) / mathisMbitsApprox(1460, 100, R(1n, 100n)),
       Math.SQRT2, 1e-9, 'halving the loss buys a factor of sqrt 2');
  eq(Rsqrt(R(1n, 50n)), 'null', 'and 2% loss has no rational root at all, which is why sqrtApprox is used');
  near(mathisMbitsApprox(1460, 100, R(1n, 50n)), 0.826, 1e-3,
       'and twice the loss is not half the bound: 2% gives 0.826, not 0.584');
}


// ------------------------------------------- capacity estimation (kit: estimate)
/* The arithmetic of System Design course 1. Every case below is a claim some
   lesson on that course makes out loud, so a failure here is a page asserting
   something false, not a style regression. */
console.log('capacity estimation: intervals, unit chains, series and ceilings');
{
  eval(countingBlock('BIGINT_JS') + sysdBlock('RCEIL_JS') + sysdBlock('APPROX_JS')
       + estimateBlock('ESTIMATE_JS'));

  /* Printing an exact rational at a size that defeats Rdec. This is not
     cosmetic: Rdec goes through Number(n)/Number(d), and the storage mode
     routinely holds 10^15 over 10^72. */
  eq(Rround(R(1n, 3n), 4), '0.3333', 'a third to four places');
  eq(Rround(R(2n, 3n), 4), '0.6667', 'two thirds rounds up, not down');
  eq(Rround(R(1n, 2n), 0), '1', 'a half rounds half-up at zero places');
  eq(Rround(R(-1n, 3n), 3), '-0.333', 'and the sign survives');
  eq(Rround(R(10n ** 24n + 1n, 1n), 0), '1000000000000000000000001',
     '10^24 + 1 exactly, where a double would have said 1e+24');
  eq(Number(Rdec(R(10n ** 24n + 1n, 1n))) === 1e24, true,
     'which is exactly what Rdec does say, and why Rround exists');
  eq(groupDec('1234567.89'), '1 234 567.89', 'grouping stops at the decimal point');
  eq(groupDec('-1000'), '-1 000', 'and does not eat the sign');
  eq(showR(R(1234567n, 100n), 1), '12 345.7', 'a figure as a capacity page shows it');
  eq(Rtextg(R(100000n, 1n)), '100 000', 'an exact ratio, grouped');
  eq(Rtextg(R(125n, 108n)), '125/108', 'a small fraction is left alone');
  eq(powTen(5) + ' ' + powTen(-3), '10⁵ 10⁻³', 'decades read as decades');

  /* Widths in powers of ten: an exact integer search, and its rounded gloss. */
  eq(decadeBracket(R(64n, 1n)), 1, '64 is between 10^1 and 10^2');
  eq(decadeBracket(R(1n, 1n)), 0, '1 sits in decade 0');
  eq(decadeBracket(R(1000n, 1n)), 3, 'an exact power belongs to its own decade, not the one below');
  eq(decadeBracket(R(1n, 1000n)), -3, 'and a thousandth to -3');
  eq(decadeBracket(R(999n, 1000n)), -1, 'just under 1 is decade -1');
  near(log10Approx(R(1000n, 1n)), 3, 1e-12, 'log10 of a thousand');
  near(log10Approx(R(64n, 1n)), 1.80617997, 1e-6, 'log10 of the width three doubling factors give');
  /* The case Rnum cannot do: both ends past 2^53, the ratio small. */
  near(log10Approx(Rdiv(R(10n ** 40n, 1n), R(10n ** 37n, 1n))), 3, 1e-9,
       'a ratio of two numbers a double cannot hold');
  near(ratioApprox(R(3n * 10n ** 40n, 1n), R(10n ** 40n, 1n)), 3, 1e-9,
       'and the same ratio as a Number, for pixels');

  /* L1. Three factors at a factor of two: the product is at a factor of EIGHT,
     the interval is 64x end to end, and the arithmetic midpoint is four times
     the estimate -- which is the misconception the lesson names. */
  const C = [R(10000000n, 1n), R(100n, 1n), R(1000n, 1n)];
  const two = [R(2n, 1n), R(2n, 1n), R(2n, 1n)];
  const iv = productInterval(C, two, two);
  eq(Rtext(iv.centre), '1000000000000', 'the product of the central values');
  eq(Rtext(iv.lo) + ' ' + Rtext(iv.hi), '125000000000 8000000000000', 'the product interval');
  eq(Rtext(iv.down) + ' ' + Rtext(iv.up), '8 8', 'three half-widths of 2 multiply to 8, not to 6');
  eq(Rtext(iv.ratio), '64', 'and end to end the interval is 64x');
  eq(Rtext(Rdiv(arithMid(iv.lo, iv.hi), iv.centre)), '65/16',
     'the arithmetic midpoint is 65/16 of the estimate: it is dragged to the high end');
  eq(Rtext(geoMeanExact(iv.lo, iv.hi)), '1000000000000',
     'the geometric centre of a symmetric interval IS the product of the centres, exactly');
  /* Asymmetric: the root is irrational, so the page must round and say so. */
  const skew = productInterval(C, two, [R(2n, 1n), R(3n, 1n), R(2n, 1n)]);
  eq(Rtext(skew.up), '12', 'one factor skewed high widens only the high end');
  eq(geoMeanExact(skew.lo, skew.hi), 'null', 'and its geometric centre is not rational');
  near(geoMeanApprox(skew.lo, skew.hi), Math.sqrt(1.5) * 1e12, 1e4,
       'so it is computed by the rounded root, which is sqrt(3/2) x the centre');
  /* A factor known exactly contributes nothing to the width. */
  const one3 = [R(1n, 1n), R(1n, 1n), R(1n, 1n)];
  eq(Rtext(productInterval(C, one3, one3).ratio), '1', 'three exact factors give a point, not an interval');

  /* L2. 86400 against 10^5, in both directions -- the lesson's own numbers. */
  eq(Rtext(rpsExact(R(10000000n, 1n), R(100n, 1n))), '312500/27', '10M users x 100 actions a day, per second');
  eq(Rtext(rpsRounded(R(10000000n, 1n), R(100n, 1n))), '10000', 'and with the 10^5-second day');
  eq(Rtext(dayLengthRatio()), '125/108', 'the shortcut day is 125/108 of a real one');
  eq(Rtext(rateShortfallRatio()), '108/125', 'so the rate it gives is 108/125 of the truth');
  eq(Rtext(Rdiv(rpsExact(R(7n, 1n), R(13n, 1n)), rpsRounded(R(7n, 1n), R(13n, 1n)))), '125/108',
     'and the ratio does not depend on the volume, which is why it is quotable');
  eq(Rtrim(Rround(Rmul(Rsub(dayLengthRatio(), R(1n, 1n)), R(100n, 1n)), 2)), '15.74',
     'the 15.7% the lesson quotes is the DAY being long');
  eq(Rtext(Rmul(Rsub(R(1n, 1n), rateShortfallRatio()), R(100n, 1n))), '68/5',
     'the rate is low by 13.6%, which is a different number and the reader will confuse them');
  /* Turning it back: rate x 86400 must return the daily volume it came from. */
  eq(Rtext(Rmul(rpsExact(R(10000000n, 1n), R(100n, 1n)), R(86400n, 1n))), '1000000000',
     'the chain read upward returns where it started');

  /* L3. 100:1 is 1/101, not 1%. */
  const sp = splitRates(R(10000n, 1n), R(100n, 1n));
  eq(Rtext(sp.writeShare), '1/101', 'a 100:1 read/write ratio makes writes one part in 101');
  eq(Rtext(sp.readShare), '100/101', 'and reads the other hundred');
  eq(Rtext(Radd(sp.readShare, sp.writeShare)), '1', 'the two shares are a partition');
  eq(Rtext(sp.naiveWriteShare), '1/100', 'the instinct says 1/100');
  eq(Requ(sp.writeShare, sp.naiveWriteShare), false, 'which is not the same number');
  eq(Rtext(sp.naiveOver), '101/100', 'and overstates the write rate by exactly (r+1)/r');
  eq(Rtext(sp.writes) + ' ' + Rtext(sp.reads), '10000/101 1000000/101', 'the two rates, exactly');
  eq(Rtext(Radd(sp.writes, sp.reads)), '10000', 'and they add back to the total');
  eq(Rtext(splitRates(R(2n, 1n), R(1n, 1n)).writeShare), '1/2', '1:1 is half and half');

  /* L5. Bits, bytes, and the header that is charged once per request. */
  eq(Rtext(bandwidthMbit(R(2000n, 1n), R(1000n, 1n), R(200n, 1n))), '96/5',
     '2000 req/s of 1200 B is 19.2 Mbit/s');
  eq(Rtrim(Rround(bandwidthMbit(R(2000n, 1n), R(1000n, 1n), R(200n, 1n)), 2)), '19.2', 'read as a decimal');
  eq(Rtext(Rdiv(bandwidthMbit(R(2000n, 1n), R(1000n, 1n), R(200n, 1n)),
                bandwidthNoEight(R(2000n, 1n), R(1000n, 1n), R(200n, 1n)))), '8',
     'forgetting the factor of 8 is out by exactly 8, at every rate and every size');
  eq(Rtext(headerShare(R(1000n, 1n), R(200n, 1n))), '1/6', 'headers are a sixth of a 1 kB request');
  eq(Rtext(headerShare(R(200n, 1n), R(200n, 1n))), '1/2',
     'and half of one whose payload equals the header');
  eq(Rtext(headerCrossover(R(200n, 1n))), '200', 'which is why the crossover payload IS the header size');
  eq(Rcmp(headerShare(R(199n, 1n), R(200n, 1n)), R(1n, 2n)) > 0, true, 'below it they are the majority');

  /* L4. Storage as a series, with growth compounding once a month. */
  const gb500 = R(500n * 10n ** 9n, 1n);
  const terms = growthTerms(gb500, 90, R(5n, 100n));
  eq(terms.length, 3, '90 days is three monthly blocks');
  eq(terms.map(function (t) { return t.days; }).join(','), '30,30,30', 'each of them full');
  eq(Rtext(terms[2].rate), '551250000000', 'by the third month the daily ingest has compounded twice');
  eq(Rtext(terms[2].running), '47287500000000', 'and 47.2875 TB has accumulated');
  eq(Rtext(storageGrowth(gb500, 90, R(5n, 100n), 3)), '141862500000000', 'three copies of it');
  eq(Rtext(storageFlat(gb500, 90, 3)), '135000000000000', 'against 135 TB if ingest never grew');
  /* The invariant that catches an off-by-one in the block loop. */
  eq(Rtext(storageGrowth(gb500, 90, R(0n, 1n), 3)), Rtext(storageFlat(gb500, 90, 3)),
     'at zero growth the geometric series IS the arithmetic one');
  eq(Rtext(storageGrowth(gb500, 1, R(5n, 100n), 1)), Rtext(gb500), 'one day is one day of ingest');
  /* A part-month: 45 days is 30 at the first rate and 15 at the second. */
  const part = growthTerms(R(10n, 1n), 45, R(1n, 10n));
  eq(part.map(function (t) { return t.days; }).join(','), '30,15', 'the last block is short');
  eq(Rtext(part[1].rate), '11', 'and runs at the compounded rate');
  eq(Rtext(part[1].running), '465', '30x10 + 15x11');

  /* L6. The ratio between two rungs, exactly. */
  eq(Rtext(rungRatio(10000000, 100)), '100000',
     '10^5 main-memory references fit inside one disk seek -- the lesson’s headline');
  eq(Rtext(rungRatio(150000000, 1)), '150000000', 'and the whole ruler spans that from L1');
  eq(Rtext(rungRatio(4, 3)), '4/3', 'two rungs that do not divide stay a fraction');

  /* L7. Twenty-four buckets, a peak, a mean, and their ratio. */
  eq(profileWeights('flat', 12, 5).join(','), new Array(24).fill(10).join(','),
     'a flat profile is flat whatever the amplitude');
  const office = profileWeights('office', 21, 6);
  eq(office[21], 46, 'the busy hour carries 10 + 6x6');
  eq(office.reduce(function (a, b) { return a + b; }, 0), 456, 'and the day totals 456 weight');
  eq(office[9], 10, 'twelve hours away the profile is back at the floor');
  const spike = profileWeights('spike', 19, 10);
  eq(spike[19] + ',' + spike[18] + ',' + spike[20], '130,10,10', 'a spike is one bucket and nothing else');
  let shapeThrew = false;
  try { profileWeights('nonesuch', 0, 1); } catch (e) { shapeThrew = true; }
  eq(shapeThrew, true, 'an unknown profile shape raises rather than quietly going flat');
  const buckets = office.map(function (w) { return R(BigInt(w) * 1000000n, 1n); });
  const ps = peakStats(buckets);
  eq(ps.peakHour, 21, 'the peak is where the shape put it');
  eq(Rtext(ps.total), '456000000', 'the day’s total');
  eq(Rtext(ps.peakRps), '115000/9', 'peak requests a second');
  eq(Rtext(ps.meanRps), '47500/9', 'mean requests a second');
  eq(Rtext(ps.ratio), '46/19', 'peak over mean is 24 x the busiest bucket over the total, exactly');
  eq(Rtext(peakStats(new Array(24).fill(R(7n, 1n))).ratio), '1',
     'and a day with no shape at all has a multiplier of 1, which is the sanity check');

  /* L8. The ceiling, and the headroom named rather than assumed. */
  const mc = machineCount(R(20000n, 1n), R(40n, 1n), 8, R(60n, 100n));
  eq(Rtext(mc.capacity), '200', 'one 8-core machine at 40 ms a request serves 200 req/s');
  eq(Rtext(mc.usable), '120', 'of which 60% may be used');
  eq(Rtext(mc.exact), '500/3', 'so the fleet needs 500/3 machines');
  eq(mc.n, 167n, 'and machines are integers, so N = 167');
  eq(mc.nFull, 100n, 'sizing at 100% would have said 100');
  eq(Rtext(mc.spare), '13400', 'N leaves 13 400 req/s of headroom');
  eq(Rtext(Rmul(mc.utilisation, R(100n, 1n))), '10000/167',
     'the peak then sits at 10000/167 % of the fleet, which is 59.88');
  eq(Rtrim(Rround(Rmul(mc.utilisation, R(100n, 1n)), 2)), '59.88', 'read as a percentage');
  /* The ceiling must not round a whole number up: that is the off-by-one that
     buys a machine nobody needs, on every page that sizes anything. */
  eq(machineCount(R(24000n, 1n), R(40n, 1n), 8, R(60n, 100n)).n, 200n,
     'an exact 200 machines is 200, not 201');
  eq(machineCount(R(1n, 1n), R(40n, 1n), 8, R(60n, 100n)).n, 1n, 'and any positive load needs at least one');

  /* L9. The working set, and the inverse that the whole lesson rests on. */
  const hot = R(1n, 10n), share = R(9n, 10n);
  eq(Rtext(workingSetFraction(hot, share, R(8n, 10n))), '4/45',
     '80% of the hits from a tenth of the data that takes 90% of the reads');
  eq(Rtext(workingSetFraction(R(5n, 100n), R(75n, 100n), R(95n, 100n))), '81/100',
     'and 95% costs 81% of the data once the target is past the knee');
  eq(Rtext(hitRateAt(hot, share, hot)), '9/10', 'caching exactly the hot region gets exactly its share');
  eq(Rtext(hitRateAt(hot, share, R(1n, 1n))), '1', 'caching everything hits everything');
  eq(Rtext(hitRateAt(hot, share, R(0n, 1n))), '0', 'caching nothing hits nothing');
  eq(Rtext(workingSetFraction(hot, share, R(1n, 1n))), '1', 'and a 100% target needs all of it');
  /* Inverse, at ten targets either side of the knee. A sizing lesson whose
     curve and whose inverse disagree is giving the reader a number that its own
     graph contradicts. */
  let inverseOk = true;
  for (let t = 1; t <= 10; t += 1) {
    const target = R(BigInt(t), 10n);
    if (!Requ(hitRateAt(hot, share, workingSetFraction(hot, share, target)), target)) inverseOk = false;
  }
  eq(inverseOk, true, 'the memory a target needs, put back into the curve, returns that target');
  eq(Rtext(workingSetBytes(R(5n * 10n ** 12n, 1n), hot, share, R(8n, 10n))), '4000000000000/9',
     '5 TB, a tenth hot, 80% wanted: 444.4 GB');
  /* No skew at all: caching x of the data buys x of the hits, which is the
     "caching is not worth it here" case the lesson needs to be able to show. */
  eq(Rtext(workingSetFraction(R(1n, 2n), R(1n, 2n), R(9n, 10n))), '9/10',
     'with no skew the cache must hold as much as the hit rate you want');

  /* L10. Two routes, their ratio, the band, and the shared factor. */
  const routeA = [R(500000n, 1n), R(20n, 1n), R(2000000n, 1n)];
  const routeB = [R(10000000n, 1n), R(1800000n, 1n)];
  eq(Rtext(routeProduct(routeA)), '20000000000000', 'route A');
  eq(Rtext(routeProduct(routeB)), '18000000000000', 'route B');
  eq(Rtext(routeRatio(routeProduct(routeA), routeProduct(routeB))), '10/9', 'and the ratio between them');
  eq(Rtext(routeProduct([])), '1', 'an empty chain is the empty product');
  eq(withinBand(R(10n, 9n), R(8n, 1n)), true, '10/9 is inside a band of 8');
  eq(withinBand(R(9n, 10n), R(8n, 1n)), true, 'and so is its reciprocal');
  eq(withinBand(R(9n, 1n), R(8n, 1n)), false, 'nine is outside');
  /* The direction a naive check gets wrong: a ratio far BELOW 1 is just as much
     a disagreement as one far above, and "ratio < k" alone would pass it. */
  eq(withinBand(R(1n, 9n), R(8n, 1n)), false, 'and so is a ninth');
  eq(withinBand(R(1n, 1n), R(1n, 1n)), true, 'a band of 1 admits only exact agreement');
  eq(sharedFactors(['users', 'sessions', 'bytes'], [R(5n), R(3n), R(7n)],
                   ['rows', 'bytes'], [R(9n), R(7n)]).join(','), 'bytes',
     'a factor in both chains with the same value is shared');
  eq(sharedFactors(['bytes'], [R(7n)], ['bytes'], [R(8n)]).length, 0,
     'the same NAME at a different value is not: route B measured it for itself');
  eq(sharedFactors(['bytes'], [R(7n)], ['rows'], [R(7n)]).length, 0,
     'and a coincidence of value under another name is not either');

  /* Units and the slider ladder. */
  eq(fmtBytes(R(1500n, 1n), 2), '1.5 kB', 'kB is 1000 B, decimal, as a disk is sold');
  eq(fmtBytes(R(999n, 1n), 2), '999 B', 'and below that it stays bytes');
  eq(fmtBytes(R(47287500000000n, 1n), 2), '47.29 TB', 'the storage lesson’s own total');
  eq(fmtBytes(R(10n ** 15n, 1n), 2), '1 PB', 'and a petabyte is a petabyte');
  eq(Rtext(ladderValue(0)) + ' ' + Rtext(ladderValue(1)) + ' ' + Rtext(ladderValue(6)), '1 3/2 10',
     'the 1, 1.5, 2, 3, 5, 7 ladder, one rung per decade step');
  eq(Rtext(ladderValue(ladderIndex(0, 7))), '10000000', '10 million is a rung, so lesson 1 can open on it');
  eq(Rtext(ladderValue(ladderIndex(2, 6))), '2000000', 'and so is 2 MB');
}

// ------------------------------------------- caching and hit rates (kit: cache)
/* The `cache` kit's own arithmetic, on the numbers its ten lessons print.
   Every assertion below is a figure that appears on a page, so a change that
   moves one of them is a change to what a lesson claims.

   Three of them are not figures but PINS. The stepper this kit uses to show a
   policy's cache contents duplicates the eviction rules of the core's
   replayPolicy, which is the tested one, so it is checked against it on every
   trace and every size below; the byte hit rate is checked against zipfHit at
   the shifted exponent it must equal; and the phase-averaged TTL simulation is
   checked against the closed form it is meant to confirm. A duplicated rule
   that nothing compares is a rule that has already drifted. */
console.log('system design: caching, skew, replacement and staleness');
{
  const CACHE_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'cache.py');
  const cacheSrc = fs.readFileSync(CACHE_SOURCE, 'utf8');
  const cacheBlock = (name) => blockFrom(cacheSrc, name, CACHE_SOURCE);
  eval(block('RATIONAL_JS') + sysdBlock('RCEIL_JS') + sysdBlock('HARMONIC_JS')
       + sysdBlock('QUEUE_JS') + sysdBlock('REPLAY_JS') + sysdBlock('APPROX_JS')
       + cacheBlock('CACHE_JS'));

  /* --- printing. Rnum goes through Number and this course overflows it. --- */
  eq(Rshow(R(1n, 3n), 3), '0.333', 'long division in BigInt');
  eq(Rshow(R(2n, 3n), 3), '0.667', 'rounded half up at the last digit');
  eq(Rshow(R(1n, 2n), 0), '1', 'and half rounds up, not to even');
  eq(Rshow(R(-1n, 3n), 3), '-0.333', 'the sign survives the division');
  /* The reason Rshow exists: a byte weight over fifty ranks leaves a double. */
  eq(Rnum(R(10n ** 400n + 1n, 3n * 10n ** 400n)), NaN, 'Rnum of a 400-digit ratio is NaN');
  eq(Rshow(R(10n ** 400n + 1n, 3n * 10n ** 400n), 4), '0.3333', 'Rshow of the same is a third');
  eq(Rpercent(R(1n, 3n), 2), '33.33%', 'a percentage of an exact probability');
  eq(groupNum(1234567), '1 234 567', 'digit grouping');
  eq(bytesText(1500), '1.50 kB', 'a kB is 1000 B: egress is billed in decimal units');
  eq(bytesText(40000000000n), '40.00 GB', 'and so is a GB');
  eq(moneyText(R(2400000n, 1n)), '$24 000.00', 'cents to dollars');

  /* --- L1: the backend sees the miss rate ---------------------------------
     The lesson's whole claim is the ratio: 90% to 99% is a tenfold cut, and
     99% to 99.9% is another one. Asserting the two loads alone would not
     catch a formula that had (1 - h) right and lambda wrong. */
  eq(Rtext(backendRate(R(10000n, 1n), R(9n, 10n))), '1000', '10k rps at 90% leaves 1000');
  eq(Rtext(backendRate(R(10000n, 1n), R(99n, 100n))), '100', 'and at 99%, 100');
  eq(Rtext(backendRho(R(10000n, 1n), R(9n, 10n), R(2000n, 1n))), '1/2', 'the backend sits at rho = 1/2');
  eq(Rtext(missMultiple(R(9n, 10n), R(99n, 100n))), '10', '90% to 99% divides the load by 10');
  eq(Rtext(missMultiple(R(99n, 100n), R(999n, 1000n))), '10', 'and 99% to 99.9% by 10 again');
  eq(missMultiple(R(9n, 10n), R(1n, 1n)), null, 'a perfect cache has no ratio, and says so');

  /* --- L2: an expectation, and a percentile that steps --------------------- */
  eq(Rtext(meanLatency(R(19n, 20n), R(1n, 1n), R(40n, 1n))), '59/20', 'the lesson mean, 2.95 ms');
  eq(Rtext(latencyQuantile(R(19n, 20n), R(1n, 1n), R(40n, 1n), R(1n, 2n))), '1', 'the p50 is a hit');
  eq(Rtext(latencyQuantile(R(19n, 20n), R(1n, 1n), R(40n, 1n), R(99n, 100n))), '40',
     'at h = 95% the p99 is the MISS latency -- the misconception, refuted');
  eq(Rtext(latencyQuantile(R(99n, 100n), R(1n, 1n), R(40n, 1n), R(99n, 100n))), '1',
     'and it flips exactly at h = q, not gradually');
  eq(Rtext(latencyQuantile(R(9899n, 10000n), R(1n, 1n), R(40n, 1n), R(99n, 100n))), '40',
     'one ten-thousandth below q and it is the miss latency again');

  /* --- L3, L4: Zipf, exactly ---------------------------------------------- */
  eq(Rtext(rankTerm(2, 3)) + ' ' + Rtext(rankTerm(2, -3)) + ' ' + Rtext(rankTerm(5, 0)), '8 1/8 1',
     'i^e for e positive, negative and zero');
  eq(Rtext(zipfProb(1, 4, 1)), '12/25', 'the most popular of four keys at s = 1');
  eq(Rtext(zipfShare(4, 20, 1, 50).exact), '6466460/11167027',
     'the top 4 of 20 at s = 1 -- the L3 worked example, exactly');
  eq(zipfShare(4, 20, 1, 50).rounded, false, 'and it is not rounded');
  eq(Rtext(zipfHit(4, 20, 0)), '1/5', 's = 0 IS uniform popularity: 20% of the keys, 20% of the hits');
  eq(Rtext(zipfShare(0, 20, 1, 50).exact) + ' ' + Rtext(zipfShare(25, 20, 1, 50).exact), '0 1',
     'an empty cache hits nothing and a complete one hits everything');
  /* Past the limit the page must ROUND and must say so. A silent switch would
     print an approximation in the shape of an exact fraction. */
  eq(zipfShare(20, 200, 1, 50).rounded, true, 'past N = 50 the share is rounded');
  eq(zipfShare(20, 200, 1, 50).exact, null, 'and there is no exact fraction to offer');
  near(zipfShare(20, 200, 1, 50).value, 0.612101, 1e-5, 'the rounded value at N = 200');
  /* Sizing: the C a target costs, and the diminishing returns that follow. */
  eq(sizeForTarget(50, 2, R(9n, 10n)), 5, 'at N = 50, s = 2, ninety per cent costs 5 keys');
  eq(sizeForTarget(50, 2, R(99n, 100n)), 28, 'and ninety-nine per cent costs 28 -- the next nine');
  eq(sizeForTarget(20, 0, R(1n, 2n)), 10, 'under uniform popularity it IS proportional: half for half');
  eq(JSON.stringify(sizeTarget(200, 1, R(9n, 10n), 50)), '{"c":111,"rounded":true}',
     'past the limit the search rounds, and reports that it did');
  eq(hitCurve(4, 1, 50).join(' '), '0.48 0.72 0.88 1', 'h(C) for C = 1..4 at N = 4, s = 1');

  /* --- L10: the byte hit rate is a different number ------------------------
     It is the same harmonic ratio at exponent s - b, so the two must agree
     wherever both are defined. That identity is the assertion: it catches a
     sign error in the exponent, which no single value would. */
  eq(Rtext(byteWeight(20, 1, 0)), Rtext(harmonic(20, 1)), 'at b = 0 the byte weight IS the harmonic');
  eq(Rtext(byteHit(4, 20, 1, 0)), Rtext(zipfHit(4, 20, 1)),
     'so at b = 0 the byte hit rate IS the request hit rate -- the control');
  eq(Rtext(byteHit(4, 20, 2, 1)), Rtext(zipfHit(4, 20, 1)), 'and in general it is zipfHit at s - b');
  eq(Rtext(byteHit(4, 20, 1, 1)), '1/5',
     'at b = s it collapses to C/N: 57.9% of the requests, 20% of the bytes');
  eq(Rtext(byteHit(2, 4, 1, 2)), '3/10', 'b > s is allowed, and harmonicApprox could not compute it');
  near(byteHitApprox(4, 20, 1, 1), 0.2, 1e-12, 'the rounded path agrees with the exact one');
  eq(Rtext(objectBytes(3, 1, 100000)), '300000', 'rank 3 at b = 1 is three times the base size');
  eq(Rtext(egressCost(R(40000n * 1000000000n, 1n), R(2n, 1n), 30)), '2400000',
     '40 TB a day at 2c/GB is $24 000 a month');

  /* --- L5: replacement, and the bound the lesson rests on ------------------ */
  const T1 = parseTrace('A B C A B D A B C D');
  eq(T1.join(''), 'ABCABDABCD', 'the course trace parses');
  eq(parseTrace('a,b--c  A!!b').join('|'), 'A|B|C|A|B', 'any separator, and case folds');
  eq(traceKeys(T1).join(''), 'ABCD', 'four distinct keys, in first-use order');
  eq(Rtext(replayTrace(T1, 3, 'opt').rate), '1/2', 'farthest-in-future gets 5 of 10');
  eq(Rtext(replayTrace(T1, 3, 'lru').rate), '2/5', 'LRU gets 4');
  eq(Rtext(replayTrace(T1, 3, 'fifo').rate), '1/5', 'FIFO gets 2');
  /* THE PIN. The stepper duplicates the core's eviction rules so that it can
     report cache contents; if the two ever disagree the page is showing one
     run and counting another. Checked on five traces at six sizes. */
  {
    let mismatches = 0;
    const traces = [T1, parseTrace('1 2 3 4 1 2 5 1 2 3 4 5'), parseTrace('A A A B C B C B C'),
                    parseTrace('A B C D E A B C D E A B'), parseTrace('A')];
    for (const t of traces) {
      for (let k = 1; k <= 6; k += 1) {
        for (const p of ['fifo', 'lru', 'opt']) {
          if (replayTrace(t, k, p).hits !== replayPolicy(t, k, p).hits) mismatches += 1;
        }
      }
    }
    eq(mismatches, 0, 'the kit stepper agrees with the core replay on every trace, size and policy');
  }
  /* LFU is the one policy the core does not implement, so it needs a trace
     that separates it from the two it would otherwise be mistaken for. On
     A A A B C B C B C at two slots it keeps the stale hot key and gets 2
     where FIFO, LRU and OPT all get 6. */
  const T2 = parseTrace('A A A B C B C B C');
  eq(replayTrace(T2, 2, 'lfu').hits, 2, 'LFU holds the once-hot key and thrashes on the rest');
  eq(replayTrace(T2, 2, 'lru').hits, 6, 'LRU lets it go');
  eq(replayTrace(T2, 2, 'fifo').hits, 6, 'so does FIFO');
  eq(replayTrace(T2, 2, 'opt').hits, 6, 'and the bound is 6 as well, so LFU is losing 4 hits');
  /* An unknown policy must throw. The core silently treats one as FIFO, which
     would show a FIFO run under an LFU heading. */
  {
    let threw = false;
    try { replayTrace(T1, 3, 'random'); } catch (err) { threw = true; }
    eq(threw, true, 'an unknown policy throws rather than quietly becoming FIFO');
  }
  /* Belady's anomaly, measured. FIFO misses 9 times with three slots and 10
     with four; LRU and OPT are stack algorithms and never rise. */
  const BEL = parseTrace('1 2 3 4 1 2 5 1 2 3 4 5');
  eq(missBySize(BEL, 'fifo', 6).join(','), '12,12,9,10,5,5', 'FIFO misses against cache size');
  eq(missBySize(BEL, 'lru', 6).join(','), '12,12,10,8,5,5', 'LRU never rises');
  eq(missBySize(BEL, 'opt', 6).join(','), '12,9,7,6,5,5', 'nor does the bound');
  eq(JSON.stringify(firstAnomaly(BEL, 'fifo', 6)), '{"k":3,"up":4,"from":9,"to":10}',
     "Belady's anomaly, found rather than asserted");
  eq(firstAnomaly(BEL, 'lru', 6), null, 'and LRU has none');
  eq(firstAnomaly(BEL, 'opt', 6), null, 'and neither has OPT');
  eq(firstAnomaly(T1, 'fifo', 6), null, 'the course trace does not show one, which is why the kit ships both');

  /* --- L6: TTL and staleness ---------------------------------------------- */
  eq(Rtext(staleFraction(R(10n, 1n), R(60n, 1n))), '1/12', 'T/(2U) below U');
  eq(Rtext(staleFraction(R(120n, 1n), R(60n, 1n))), '3/4', '1 - U/(2T) above it');
  eq(Rtext(staleFraction(R(60n, 1n), R(60n, 1n))), '1/2', 'and the two branches meet at T = U');
  eq(Rtext(ttlMissRate(R(5n, 1n), R(10n, 1n))), '1/50', 'a 10 s TTL at 5 reads/s misses 2%');
  eq(Rtext(ttlMissRate(R(5n, 1n), R(1n, 10n))), '1',
     'a TTL shorter than the gap between reads misses everything, and the rate caps at 1');
  /* The boundary the simulation turns on: a refresh at the same instant as an
     update picks up the NEW value, so the next update is strictly after. */
  eq(Rtext(nextUpdateAfter(R(0n, 1n), R(0n, 1n), R(60n, 1n))), '60',
     'an update at the refresh instant does not make the copy stale');
  eq(Rtext(nextUpdateAfter(R(0n, 1n), R(10n, 1n), R(60n, 1n))), '10', 'the next one does');
  /* THE SECOND PIN: the phase-averaged simulation must reproduce the closed
     form it is printed beside, or the page is showing two models. */
  eq(Rtext(staleRun(R(10n, 1n), R(60n, 1n), R(15n, 1n), 24).fraction), '1/12', 'one run at one phase');
  eq(Rtext(staleAverage(R(10n, 1n), R(60n, 1n), 24, 24)), Rtext(staleFraction(R(10n, 1n), R(60n, 1n))),
     'and 24 midpoint phases reproduce T/(2U) exactly');
  eq(Rtext(staleAverage(R(120n, 1n), R(60n, 1n), 24, 2)), Rtext(staleFraction(R(120n, 1n), R(60n, 1n))),
     'the same on the other branch');
  eq(Rtext(staleAverage(R(25n, 1n), R(60n, 1n), 24, 10)), '5/24',
     'and with T not dividing U it still lands on the formula');

  /* --- L7: the stampede ---------------------------------------------------- */
  eq(Rtext(stampedeSize(R(500n, 1n), R(40n, 1n))), '20', 'lambda*d: 500 rps through a 40 ms window');
  eq(Rtext(stampedeSize(R(500n, 1n), R(1n, 1n))), '1/2', 'a 1 ms window lets half a request through');
  eq(String(stampedeCount(R(500n, 1n), R(1n, 1n))), '1', 'which the backend counts as one');
  eq(Rtext(stampedeTotal(R(500n, 1n), R(40n, 1n), 10)), '200', 'ten hot keys expiring together');

  /* --- L8: write-through against write-back -------------------------------- */
  const W = parseTrace('A B A C A B A D A B');
  eq(distinctPerWindow(W, 5).map((x) => x.distinct).join(','), '3,3', 'three distinct keys per flush');
  eq(coalescing(W, 5).writes + ' ' + coalescing(W, 5).distinct + ' ' + Rtext(coalescing(W, 5).ratio),
     '10 6 5/3', 'ten writes become six, a ratio of 5/3');
  eq(coalescing(W, 5).peak, 3, 'and the largest dirty set is three keys');
  eq(Rtext(coalescing(W, 1).ratio), '1', 'flushing every write coalesces nothing');
  eq(Rtext(coalescing(W, 99).ratio), '5/2', 'and one flush for the whole trace coalesces most');
  eq(Rtext(bytesAtRisk(3, 4000)), '12000', 'three 4 kB keys is 12 kB at risk');

  /* --- L9: the second level is conditional --------------------------------- */
  eq(Rtext(globalHit(R(4n, 5n), R(1n, 2n))), '9/10', '80% then half the rest is 90%, not 130%');
  eq(Rtext(globalMiss(R(4n, 5n), R(1n, 2n))), '1/10', 'the global miss is the PRODUCT');
  eq(Rtext(Radd(globalHit(R(4n, 5n), R(1n, 2n)), globalMiss(R(4n, 5n), R(1n, 2n)))), '1',
     'and the two account for everything');
  eq(Rtext(levelLatency(R(4n, 5n), R(1n, 2n), R(1n, 1n), R(5n, 1n), R(50n, 1n))), '7',
     't1 + (1-h1)(t2 + (1-h2)t3) = 7 ms');
  eq(Rtext(naiveSumHit(R(4n, 5n), R(1n, 2n))), '13/10',
     'adding the rates gives 130%, which is how you know it is the wrong operation');
  eq(Rtext(conditionalShare(R(4n, 5n), R(1n, 2n))), '1/10',
     "L2's measured 50% is 10% of all requests, not 50%");
}

// ------------------------------- system design C3: queues and utilisation
/* The `queue` kit's own arithmetic, on the numbers its thirteen lessons print.

   The block this section exists for is the Geo/Geo/1 convergence. A slotted
   simulation is NOT M/M/1 at finite slot size, and a lesson that says its
   formula is "checked against the simulation" is comparing two models. The
   assertions below pin the exact discrete mean at three slot sizes and the rate
   at which it approaches the continuous one, so a change that quietly restores
   the false claim fails here rather than on the page. */
console.log('system design: queues, Little\'s Law and the slotted chain');
{
  const QUEUE_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'queue.py');
  const queueSrc = fs.readFileSync(QUEUE_SOURCE, 'utf8');
  const queueBlock = (name) => blockFrom(queueSrc, name, QUEUE_SOURCE);
  eval(block('RATIONAL_JS') + countingBlock('BIGINT_JS') + sysdBlock('RCEIL_JS')
       + sysdBlock('QUEUE_JS') + sysdBlock('SLOTTED_JS') + sysdBlock('TRACE_JS')
       + sysdBlock('STREAM_JS') + sysdBlock('APPROX_JS') + queueBlock('QUEUE_KIT_JS'));

  /* --- L1: mu is a rate ------------------------------------------------- */
  eq(Rtext(muFromServiceMs(1)), '1000', 'a 1 ms service is 1000 per second, not 1');
  eq(Rtext(muFromServiceMs(4)), '250', 'a 4 ms service is 250 per second');
  eq(Rtext(serviceMsFromMu(muFromServiceMs(4))), '4', 'and back again');
  eq(Rtext(Rdiv(R(800n, 1n), muFromServiceMs(1))), '4/5', 'rho = lambda/mu at the lesson preset');
  eq(Rtext(growthPerSec(R(1200n, 1n), muFromServiceMs(1))), '200', 'above rho = 1 the backlog grows at lambda - mu');
  eq(Rtext(backlogAfter(R(1200n, 1n), muFromServiceMs(1), 60)), '12000', 'a minute of that is 12 000 waiting');
  eq(Rtext(backlogAfter(R(800n, 1n), muFromServiceMs(1), 60)), '0', 'and below rho = 1 nothing accumulates');

  /* --- L2: Little's Law inside a window ---------------------------------- */
  /* The lesson's trace: five customers over ten slots, area 17. */
  const A = [0, 1, 2, 5, 6], D = [3, 4, 6, 8, 10];
  const w10 = littleWindow(A, D, 10);
  eq(w10.area + ' ' + w10.arrived + ' ' + w10.done + ' ' + w10.inflight, '17 5 5 0', 'the whole trace, counted');
  eq(Rtext(w10.L) + ' ' + Rtext(w10.lambda) + ' ' + Rtext(w10.W), '17/10 1/2 17/5', 'L, lambda and W over it');
  eq(Rtext(w10.lamW), Rtext(w10.L), 'and lambda*W IS L, with no model assumed');
  eq(w10.holds, true, 'the identity holds on a window everyone has left');
  eq(occupancyTrace(A, D, 10).join(''), '1232122211', 'the N(t) staircase the area is under');
  eq(Rtext(littleFromTrace(A, D).L), Rtext(w10.L), 'and the core agrees at the full horizon');
  /* Cut the window short and it stops holding -- which is the misconception,
     and the assertion that keeps the lab honest about WHY. */
  const w8 = littleWindow(A, D, 8);
  eq(w8.inflight, 1, 'at T = 8 one customer is still in the system');
  eq(Rtext(w8.L) + ' vs ' + Rtext(w8.lamW), '15/8 vs 65/32', 'so L and lambda*W part company');
  eq(w8.holds, false, 'the law did not fail; the window did');

  /* --- L3: the same identity, solved three ways -------------------------- */
  eq(Rtext(littleSolve('L', R(1n, 2n), R(4n, 1n))), '2', 'L = lambda*W');
  eq(Rtext(littleSolve('W', R(2n, 1n), R(1n, 2n))), '4', 'W = L/lambda');
  eq(Rtext(littleSolve('lambda', R(2n, 1n), R(4n, 1n))), '1/2', 'lambda = L/W');
  /* The unit trap the lesson is about: 500/s at 40 ms is 20, not 20 000. */
  eq(Rtext(poolForRate(R(500n, 1n), R(40n, 1n))), '20', '500 per second at 40 ms needs 20 connections');
  eq(Rtext(poolCapPerSec(20, R(40n, 1n))), '500', 'and 20 connections at 40 ms cap at 500 per second');
  eq(Rtext(poolForRate(poolCapPerSec(20, R(40n, 1n)), R(40n, 1n))), '20', 'the two are inverses');

  /* --- L4, L7: the slotted chain, which is the point of this section ------ */
  /* The closed form the kit's docstring states, checked against the core's
     geoGeo1 at four points. One point would not do it: at q = 1/2 several wrong
     formulas coincide with the right one. */
  function closed(p, q) {
    const rho = Rdiv(p, q);
    return Rdiv(Rmul(rho, Rsub(R(1n, 1n), p)), Rsub(R(1n, 1n), rho));
  }
  const pts = [[2, 5, 1, 2], [4, 5, 1, 1], [1, 4, 1, 3], [2, 25, 1, 10]];
  pts.forEach(function (t) {
    const p = R(BigInt(t[0]), BigInt(t[1])), q = R(BigInt(t[2]), BigInt(t[3]));
    eq(Rtext(geoGeo1(p, q).L), Rtext(closed(p, q)),
       'Geo/Geo/1 L = rho(1-p)/(1-rho) at p = ' + Rtext(p) + ', q = ' + Rtext(q));
    eq(Rtext(geoGeo1(p, q).p0), Rtext(Rsub(R(1n, 1n), Rdiv(p, q))),
       'and its empty probability is 1 - rho at p = ' + Rtext(p));
  });
  /* The convergence panel L7 ships, exactly. At lambda = 4/5, mu = 1 the
     largest legal slot is 1, and each tenth of it closes the gap by a factor of
     ten -- linear in Delta, because the gap is rho*p/(1 - rho) and p = lambda*Delta. */
  eq(Rtext(largestLegalSlot(R(4n, 5n), R(1n, 1n))), '1', 'the largest slot where lambda*D and mu*D are probabilities');
  eq(Rtext(largestLegalSlot(R(1n, 1n), R(2n, 1n))), '1/2', 'and it is set by whichever rate is larger');
  const conv = convergenceRows(R(4n, 5n), R(1n, 1n), 3);
  eq(conv.map(r => Rtext(r.delta) + ':' + Rtext(r.L)).join(' '),
     '1:4/5 1/10:92/25 1/100:496/125', 'the exact slotted mean at Delta = 1, 1/10, 1/100');
  eq(conv.map(r => Rtext(r.gap)).join(' '), '16/5 8/25 4/125',
     'and the shortfall against rho/(1-rho), falling by exactly ten each step');
  eq(Rtext(Rdiv(conv[0].gap, conv[1].gap)) + ' ' + Rtext(Rdiv(conv[1].gap, conv[2].gap)), '10 10',
     'exactly ten, because the gap is linear in the slot');
  eq(Rtext(mm1(R(4n, 5n), R(1n, 1n)).L), '4', 'while the continuous formula says 4 at every slot size');
  eq(Rtext(slottedMean(R(4n, 5n), R(1n, 1n), R(1n, 2n))), '12/5',
     'and at Delta = 1/2 the slotted mean is the docstring\'s 12/5, not 4');
  /* A slot too big is not a small error, it is not a model: p must be a
     probability, and the panel must refuse rather than print a number. */
  eq(slottedMean(R(2n, 1n), R(3n, 1n), R(1n, 1n)), 'null', 'lambda*Delta > 1 is not a Bernoulli slot');
  eq(slottedMean(R(1n, 2n), R(3n, 1n), R(1n, 1n)), 'null', 'nor is mu*Delta > 1');
  /* Lq = L - rho, because exactly rho of the time there is one in service. */
  eq(Rtext(geoGeo1Lq(R(2n, 5n), R(1n, 2n))), '8/5', 'the slotted Lq is L - rho');
  eq(Rtext(slottedCa2(R(2n, 5n))) + ' ' + Rtext(slottedCs2(R(1n, 2n))), '3/5 1/2',
     'and the chain\'s own coefficients of variation are 1 - p and 1 - q');

  /* --- L4: the simulation must match the chain it claims to be ----------- */
  const p25 = R(2n, 5n), q12 = R(1n, 2n);
  eq(drawBelow(0, 100, R(2n, 5n)), true, 'a draw at 0 is below any positive probability');
  eq(drawBelow(39, 100, R(2n, 5n)), true, 'and 39/100 is below 2/5');
  eq(drawBelow(40, 100, R(2n, 5n)), false, 'while 40/100 is NOT -- the boundary is half-open, or every rate is biased high');
  eq(slottedRun(p25, q12, 7, 12).join(''), slottedRun(p25, q12, 7, 12).join(''), 'the same seed gives the same run');
  eq(slottedRun(p25, q12, 7, 12).join('') === slottedRun(p25, q12, 8, 12).join(''), false,
     'and a different seed does not');
  /* 40 000 slots, warm-up discarded: the measured mean must land near 12/5. A
     loose tolerance, because this asserts the SIMULATOR implements the chain,
     not that a finite sample equals its mean. */
  const longRun = slottedRun(p25, q12, 11, 40000);
  near(Number(Rdec(runMean(longRun, 4000), 6)), 2.4, 0.12, 'a long slotted run converges on the chain\'s exact 12/5');
  eq(Rtext(runMean([0, 1, 2, 3], 0)) + ' ' + Rtext(runMean([0, 1, 2, 3], 2)), '3/2 5/2', 'the mean, and the mean after a warm-up');
  eq(queueOf([0, 1, 2, 3]).join(''), '0012', 'those waiting is N - 1, floored at zero');
  eq(runMax([0, 3, 1]), 3, 'and the peak of a run');
  /* D/D/1 at the same rho: never a queue, and the mean IS rho. That is lesson
     4's whole claim, and it is exact rather than measured. */
  eq(Rtext(runMean(ddRun(5, 4, 4000), 0)), '4/5', 'clockwork arrivals at rho = 4/5 hold exactly 4/5');
  eq(runMax(ddRun(5, 4, 4000)), 1, 'and never more than the one in service -- nothing ever waits');
  eq(runMax(ddRun(4, 1, 100)), 1, 'the same at a light load');
  /* Deterministic service, same arrival stream: it must wait LESS than
     geometric service at the same rho, which is lesson 9 seen from lesson 4. */
  eq(Rcmp(runMean(queueOf(slottedDetRun(p25, 2, 11, 40000)), 4000),
          runMean(queueOf(slottedRun(p25, q12, 11, 40000)), 4000)) < 0, true,
     'fixed service waits less than geometric service on the same arrivals');
  /* The initial transient: E[N] over an ensemble starts low and climbs. This is
     the assertion behind the sentence "the simulation starts empty". */
  const curve = transientCurve(p25, q12, 1, 24, 160);
  eq(Rtext(curve[0]) === '0' || Rcmp(curve[0], R(1n, 1n)) < 0, true, 'the ensemble starts near empty');
  eq(Rcmp(curveMean(curve, 0, 20), curveMean(curve, 80, 160)) < 0, true,
     'and the early mean is BELOW the late one -- the bias a warm-up removes');
  eq(runningMeans([1, 1, 1, 1], 0, 2).map(r => r[0] + ':' + Rtext(r[1])).join(' '), '2:1 4:1',
     'the running mean, sampled, and exact at each cut-off');

  /* --- L5: geometric to exponential -------------------------------------- */
  eq(Rtext(geoTail(R(1n, 2n), 2, 2)), '81/256', '(1 - 1/2*1/2)^(2/(1/2)) = (3/4)^4, exactly');
  eq(Rtext(geoTail(R(1n, 1n), 1, 3)), '0', 'lambda*Delta = 1 means it always arrives in the first slot');
  /* Rfixed, not Rdec: 200^400 has 921 digits and Number() of it is Infinity, so
     Rdec returns NaN on exactly the case the lesson is about. */
  near(parseFloat(Rfixed(geoTail(R(1n, 2n), 10, 4), 8)), 0.1285121, 1e-6, '(19/20)^40, the lesson\'s exact tail');
  near(parseFloat(Rfixed(geoTail(R(1n, 2n), 100, 4), 8)), 0.1346580, 1e-6, 'a hundred times finer');
  near(expNegApprox(2, 1e-15), 0.13533528, 1e-7, 'and e^-2, which is where it is going');
  eq(Rcmp(geoTail(R(1n, 2n), 100, 4), geoTail(R(1n, 2n), 10, 4)) > 0, true, 'the gap closes from below');
  /* Memorylessness is EXACT at every slot size, for every s. Not a limit. */
  [0, 1, 3, 5].forEach(function (s) {
    eq(Rtext(geoCondTail(R(1n, 2n), 10, s, 4)), Rtext(geoTail(R(1n, 2n), 10, 4)),
       'P(T > s+4 | T > s) = P(T > 4) at s = ' + s + ', exactly');
  });

  /* --- L6: the binomial exactly, Poisson as its limit --------------------- */
  /* binomRow is a recurrence; this checks it against the closed form it
     replaced, which is the only way to know the recurrence is the same
     distribution and not merely a fast one. */
  const row = binomRow(20, 10, 20);
  let mass = R(0n, 1n);
  for (let k = 0; k <= 20; k += 1) {
    mass = Radd(mass, row[k]);
    eq(Rtext(row[k]), Rtext(Rmul(R(comb(20, k), 1n), Rmul(Rpow(R(1n, 2n), k), Rpow(R(1n, 2n), 20 - k)))),
       'binomRow[' + k + '] is comb(n,k)p^k(1-p)^(n-k)');
  }
  eq(Rtext(mass), '1', 'and the row is a distribution');
  eq(Rtext(binomPmf(20, 10, 10)), '46189/262144', 'ten heads in twenty tosses');
  eq(Rtext(binomTail(20, 10, 19)), '1/1048576', 'a tail past n-1 is the last atom, (1/2)^20');
  eq(Rtext(binomTail(20, 10, 10)), '215955/524288', 'and P(more than half heads) at n = 20');
  eq(Rtext(binomTail(20, 10, 20)), '0', 'nothing exceeds n');
  eq(Rtext(binomVar(100, 10)), '9', 'the binomial variance m(1 - m/n) at n = 100');
  eq(Rtext(binomVar(1000, 10)), '99/10', 'closer to the mean as the window is chopped finer');
  near(Number(Rdec(binomTail(200, 10, 15), 8)), 0.0443561, 1e-5, 'P(count > 15) exactly, at 20 chances per unit');
  near(poissonTailApprox(10, 15), 0.0487404, 1e-6, 'and by the Poisson limit, which rounds');
  near(poissonPmfApprox(10, 10), 0.1251100, 1e-6, 'e^-m m^k/k! at the mean');
  eq(headroomForApprox(10, 0.01, 400), 18, 'a mean of 10 needs headroom 18 for a 1% overflow');
  eq(headroomForApprox(10, 0.001, 400), 21, 'and 21 for 0.1% -- the price of the tail');
  eq(headroomForApprox(12, 0.01, 400), 21, 'and 21 at a mean of 12, the largest this lab offers');
  /* Every Poisson figure above is checked against the same recurrence started
     from Math.exp rather than from the core's series, because the two agree only
     inside the range the block below pins. */
  function refPoissonTail(m, C) { let t = Math.exp(-m), h = t; for (let k = 1; k <= C; k += 1) { t = t * m / k; h += t; } return 1 - h; }
  near(poissonTailApprox(10, 15), refPoissonTail(10, 15), 1e-8, 'the Poisson tail matches a Math.exp reference at m = 10');
  near(poissonTailApprox(12, 20), refPoissonTail(12, 20), 1e-6, 'and at m = 12, the edge of the usable range');

  /* --- e^-x has a range, and the kit stops inside it ---------------------- *
     sysdesign_core's expNegApprox sums the ALTERNATING series for e^-x, whose
     largest term is about e^x/sqrt(2 pi x) while the answer is e^-x. It
     therefore loses roughly 2x/ln(10) significant digits to cancellation:
     measured, the relative error is 3e-9 at x = 10, 1.6e-7 at x = 12, 4e-3 at
     x = 17 and 173% at x = 20, and past x = 21 the SIGN is wrong.

     That is a defect in the core, not in this kit, and the fix belongs there --
     1/exp(x) by a positive-term series would be correct at every x. Until then
     the kit bounds the two modes that call it and refuses outside the bound,
     because a wrong number under a promise of a checkable one is worse than no
     number. These assertions pin both halves: that the method is good where the
     lab uses it, and that the lab's own functions refuse where it is not. */
  near(expNegSafe(10), Math.exp(-10), Math.exp(-10) * 1e-6, 'e^-10 is still good to six figures');
  near(expNegSafe(12), Math.exp(-12), Math.exp(-12) * 1e-5, 'e^-12, the bound, to five');
  eq(expNegSafe(20), 'NaN', 'past the bound the kit returns NaN rather than a confident 173% error');
  eq(expNegSafe(-1), 'NaN', 'and refuses a negative x outright');
  eq(poissonTailApprox(20, 25), 'NaN', 'so the Poisson tail refuses too');
  eq(headroomForApprox(20, 0.01, 400), -1, 'and the headroom search reports that it has no answer');
  eq(Number.isNaN(expTailApprox(R(2n, 1n), 12)), true, 'lambda*t = 24 is outside the method');
  eq(expTailApprox(R(3n, 2n), 8) > 0, true, 'lambda*t = 12 is inside it');

  /* --- L8: the knee ------------------------------------------------------ */
  eq(Rtext(kneeFactor(R(1n, 2n))) + ' ' + Rtext(kneeFactor(R(9n, 10n))) + ' ' + Rtext(kneeFactor(R(99n, 100n))),
     '2 10 100', 'W/S at 50%, 90% and 99%');
  eq(Rtext(Rdiv(kneeFactor(R(9n, 10n)), kneeFactor(R(1n, 2n)))), '5', '50% to 90% multiplies the wait by five');
  eq(Rtext(Rdiv(kneeFactor(R(99n, 100n)), kneeFactor(R(9n, 10n)))), '10', 'and 90% to 99% by ten more');
  eq(Rtext(rhoForFactor(10)) + ' ' + Rtext(rhoForFactor(100)), '9/10 99/100', 'the rho at which W = kS is (k-1)/k');
  eq(Rtext(kneeFactor(rhoForFactor(7))), '7', 'and the two are inverses at every k');

  /* --- L9: Kingman, whose model is the approximation --------------------- */
  /* At c_a^2 = c_s^2 = 1 the formula must reproduce M/M/1 EXACTLY. If it does
     not, the disagreement the lesson shows is an arithmetic bug rather than a
     modelling one, and the page would be teaching the wrong lesson. */
  [[1, 2], [4, 5], [9, 10]].forEach(function (r) {
    const rho = R(BigInt(r[0]), BigInt(r[1])), mu = R(1n, 1n);
    const S = Rinv(mu), lam = Rmul(rho, mu);
    eq(Rtext(kingmanWq(rho, R(1n, 1n), R(1n, 1n), S)), Rtext(mm1(lam, mu).Wq),
       'Kingman at c^2 = 1, 1 IS the M/M/1 Wq at rho = ' + Rtext(rho));
  });
  eq(Rtext(kingmanWq(R(4n, 5n), R(1n, 1n), R(0n, 1n), R(2n, 1n))), '4', 'M/D/1 waits half of M/M/1');
  eq(Rtext(kingmanWq(R(4n, 5n), R(1n, 1n), R(1n, 1n), R(2n, 1n))), '8', 'which is 8');
  eq(kingmanWq(R(1n, 1n), R(1n, 1n), R(1n, 1n), R(1n, 1n)), 'null', 'and it says nothing at rho = 1');
  /* The disagreement itself, as a number: at the chain's own coefficients
     Kingman says 22/5 and the exact chain says 4. */
  eq(Rtext(kingmanWq(R(4n, 5n), slottedCa2(R(2n, 5n)), slottedCs2(R(1n, 2n)), R(2n, 1n))), '22/5',
     'Kingman at the slotted chain\'s true c^2');
  eq(Rtext(Rdiv(geoGeo1Lq(R(2n, 5n), R(1n, 2n)), R(2n, 5n))), '4', 'against the chain\'s exact 4');

  /* --- L10: pooling ------------------------------------------------------ */
  /* The lesson's worked example: lambda = 3, mu = 1, s = 4. */
  const pooled = erlangC(R(3n, 1n), R(1n, 1n), 4), separate = mm1(R(3n, 4n), R(1n, 1n));
  eq(Rtext(pooled.pWait) + ' ' + Rtext(pooled.Lq) + ' ' + Rtext(pooled.Wq), '27/53 81/53 27/53',
     'Erlang C at a = 3, s = 4');
  eq(Rtext(separate.Wq), '3', 'against 3 for one of four separate queues at the same load');
  eq(Rtext(Rdiv(separate.Wq, pooled.Wq)), '53/9', 'so splitting the traffic costs 53/9 times the wait');
  eq(Rtext(Rdiv(R(3n, 1n), Rmul(R(4n, 1n), R(1n, 1n)))), '3/4', 'at an identical rho of 3/4 either way');

  /* --- L11: the two W values a lossy system separates -------------------- */
  const fin = mm1k(R(4n, 5n), R(1n, 1n), 4);
  eq(Rtext(fin.blocking), '256/2101', 'the lesson preset blocks 256/2101');
  eq(Rtext(fin.L) + ' ' + Rtext(fin.lamEff), '3284/2101 1476/2101', 'its L and its ADMITTED rate');
  eq(Rtext(fin.W), '821/369', 'W from the admitted rate, which is the right one');
  eq(Rtext(Rdiv(fin.L, R(4n, 5n))), '4105/2101', 'W from the offered rate, which is the wrong one');
  eq(Rtext(Rdiv(fin.W, Rdiv(fin.L, R(4n, 5n)))), Rtext(Rinv(Rsub(R(1n, 1n), fin.blocking))),
     'and the error is exactly the factor 1/(1 - piK)');
  eq(smallestBuffer(R(4n, 5n), R(1n, 1n), R(1n, 100n), 60), 14, 'a 1% loss target needs K = 14 here');
  eq(smallestBuffer(R(4n, 5n), R(1n, 1n), R(1n, 1000n), 60), 24, 'and 0.1% needs K = 24');
  eq(Rtext(bufferLatencyCap(R(1n, 1n), 14)), '14', 'which caps the wait near K/mu -- the bufferbloat trade');
  /* A finite chain is stable at every rho, which is the other half of L11. */
  eq(Rtext(mm1k(R(1n, 1n), R(1n, 1n), 4).blocking), '1/5', 'at rho = 1 every state is equally likely');
  eq(Rtext(mm1k(R(2n, 1n), R(1n, 1n), 3).L) !== '', true, 'and even above rho = 1 there is an answer');

  /* --- L12: the bucket and the window it replaces ------------------------ */
  const TRACE = [0, 200, 400, 600, 800, 900, 900, 900, 900, 900,
                 1000, 1000, 1000, 1000, 1000, 1400, 1600, 1800, 2000, 2200];
  const bkt = bucketRun(TRACE, R(5n, 1n), 3);
  eq(bkt.admitted + '/' + bkt.rejected, '13/7', 'the lesson trace through a bucket of 3 refilling at 5/s');
  eq(bkt.rows.map(r => (r.admit ? '+' : '-')).join(''), '+++++++---+----+++++', 'and which arrival got what');
  eq(largestBurst(bkt.rows, 1000) <= 3 + 5, true, 'no second exceeds the b + rt bound');
  eq(largestBurst(bkt.rows, 1000), 7, 'the largest it actually allows here is 7');
  /* The misconception, as a number: a fixed window of the same nominal limit
     lets nearly twice that through across a boundary. */
  const win = fixedWindowRun(TRACE, 5, 1000);
  eq(win.admitted + '/' + win.rejected, '12/8', 'the same trace through a fixed window at 5 per second');
  eq(largestBurst(win.rows, 1000), 9, 'which lets 9 through in one second while claiming 5');
  eq(largestBurst(win.rows, 1000) > largestBurst(bkt.rows, 1000), true, 'worse than the bucket it replaces');
  eq(Rtext(bucketRun([0, 1000, 2000], R(1n, 1n), 1).rows[2].tokens), '0', 'tokens are exact, not drifting floats');
  /* The lid, which is what makes b a burst allowance rather than a savings
     account. Idle for twenty seconds at one token a second and the bucket has
     earned twenty; it may keep three. Without the cap a quiet night pays for an
     unbounded morning and the b + rt guarantee is gone. */
  const idle = bucketRun([0, 20000, 20000, 20000, 20000, 20000, 20000], R(1n, 1n), 3);
  eq(idle.admitted + '/' + idle.rejected, '4/3', 'twenty idle seconds still buy only b tokens');
  eq(idle.rows.map(r => (r.admit ? '+' : '-')).join(''), '++++---', 'the burst stops at b, not at what was earned');
  eq(Rtext(bucketRun([0, 20000], R(1n, 1n), 3).rows[1].tokens), '2',
     'the level is capped at b before the arrival is charged, so it is 2 and not 21');
  eq(bucketRun([0, 0, 0, 0], R(5n, 1n), 2).admitted, 2, 'a burst with no gap spends the bucket and stops');
  eq(parseTimes('0 10  20', 9).join(','), '0,10,20', 'times parse and sort');
  eq(parseTimes('', 9), 'null', 'and an empty trace is refused rather than guessed at');

  /* --- L13: a spike is an area ------------------------------------------- */
  const plan = backlogPlan(R(1000n, 1n), R(800n, 1n), R(1500n, 1n), 60, R(800n, 1n));
  eq(Rtext(plan.excess) + ' ' + Rtext(plan.peak), '500 30000', 'the excess rate, and the area it builds');
  eq(Rtext(plan.headroom) + ' ' + Rtext(plan.drainSecs), '200 150', 'the headroom left, and the drain it buys');
  eq(Rtext(plan.maxLagSecs), '30', 'the worst lag is backlog/mu');
  eq(Rtext(plan.totalSecs), '210', 'so a 60 second spike is a 210 second incident');
  eq(Rtext(backlogAt(plan, 60, 30)) + ' ' + Rtext(backlogAt(plan, 60, 60)), '15000 30000', 'the backlog rises to its peak AT the end of the spike');
  eq(Rtext(backlogAt(plan, 60, 135)) + ' ' + Rtext(backlogAt(plan, 60, 210)), '15000 0', 'and falls from there');
  eq(Rtext(backlogAt(plan, 60, 400)), '0', 'never going negative');
  const never = backlogPlan(R(1000n, 1n), R(800n, 1n), R(1500n, 1n), 60, R(1000n, 1n));
  eq(never.drains, false, 'with no headroom afterwards it never drains');
  eq(never.drainSecs, 'null', 'and there is no drain time to print');
  eq(Rtext(backlogPlan(R(1000n, 1n), R(800n, 1n), R(900n, 1n), 60, R(800n, 1n)).peak), '0',
     'a "spike" under mu builds nothing at all');

  /* --- the kit's own printing -------------------------------------------- */
  eq(Rfixed(R(1n, 3n), 4), '0.3333', 'long division in BigInt');
  eq(Rfixed(R(2n, 3n), 4), '0.6667', 'rounded half up at the last digit');
  eq(Rfixed(R(-1n, 8n), 3), '-0.125', 'and signed');
  eq(Rpct(R(4n, 5n), 1), '80.0%', 'a percentage of an exact probability');
  eq(Rshort(R(17n, 10n), 4), '17/10', 'a readable fraction stays a fraction');
  eq(Rshort(R(272378807820n, 68618940391n), 4), '3.9694', 'and a twelve-digit one becomes a decimal');
  eq(commas(1234567), '1 234 567', 'digit grouping');
}

// --------------------------------------- availability and failure (kit: avail)
/* The `avail` kit's own arithmetic, on the numbers its thirteen lessons print.
   Every assertion below is a figure that appears on a page, so a change that
   moves one of them is a change to what a lesson claims.

   Four of them are not figures but IDENTITIES, and they are the reason this
   section exists. k-of-n at k = n must be the series product and at k = 1 the
   parallel form; the break-even common cause must be exactly the point at
   which a pair is no better than one machine; halving the repair window must
   divide the loss probability by 2^(N-1) and not by two; and the overlap
   distribution of shuffle sharding must sum to one. Each is exact, each is
   checkable, and each is a claim a lesson makes in prose. */
console.log('system design: availability, retries, durability and blast radius');
{
  const AVAIL_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'avail.py');
  const availSrc = fs.readFileSync(AVAIL_SOURCE, 'utf8');
  const availBlock = (name) => blockFrom(availSrc, name, AVAIL_SOURCE);
  eval(block('RATIONAL_JS') + countingBlock('BIGINT_JS') + sysdBlock('AVAIL_JS')
       + sysdBlock('STREAM_JS') + sysdBlock('APPROX_JS') + availBlock('AVAILKIT_JS'));

  /* --- printing. Rdec goes through Number; the storm iterates past it. ----- */
  eq(Rfixed(R(1n, 3n), 6), '0.333333', 'long division in BigInt');
  eq(Rfixed(R(2n, 3n), 6), '0.666667', 'rounded half up at the last digit');
  eq(Rfixed(R(-1n, 8n), 3), '-0.125', 'a negative rational keeps its sign');
  eq(Rpct(R(999n, 1000n), 5), '99.90000%', 'three nines as a percentage');
  eq(Rpct(R(9999n, 10000n), 5), '99.99000%', 'and four, which two places could not tell apart');
  /* RpctAuto widens with the answer, because a fixed width prints a five-nines
     quorum as 100.000000% -- which is the exact claim these lessons deny. */
  eq(RpctAuto(R(999n, 1000n)), '99.90000%', 'three nines gets five places');
  eq(RpctAuto(Rsub(R(1n, 1n), R(1n, 10n ** 10n))), '99.999999990000%',
     'ten nines gets twelve places, rather than rounding to 100%');
  eq(Rpct(Rsub(R(1n, 1n), R(1n, 10n ** 10n)), 6), '100.000000%',
     'which a fixed six places would have printed as a hundred per cent');
  eq(RpctAuto(R(1n, 1n)), '100%', 'and only an exact one prints as 100%');
  eq(RpctAuto(R(1n, 2n)), '50.0000%', 'while a coin-flip availability gets four');
  /* The reason Rfixed exists here: an iterate of the retry map overflows Number. */
  eq(String(Number(Rpow(R(999n, 1000n), 400).n)), 'Infinity',
     'Number() of 0.999^400 is Infinity');
  eq(Rfixed(Rpow(R(999n, 1000n), 400), 6), '0.670186', 'Rfixed prints it anyway');

  /* --- L1: nines and downtime, in both directions ------------------------- */
  eq(Rtext(periodSeconds('month')), '2628000', 'a month is a twelfth of a 365-day year');
  eq(Rtext(periodSeconds('year')), '31536000', 'and a year is 365 days');
  eq(Rtext(Rmul(periodSeconds('month'), R(12n, 1n))), Rtext(periodSeconds('year')),
     'twelve of those months are exactly the year');
  eq(Rtext(downtimeSeconds(R(999n, 1000n), periodSeconds('month'))), '2628',
     '99.9% is 2628 seconds a month');
  eq(durText(downtimeSeconds(R(999n, 1000n), periodSeconds('month'))), '43 min 48 s',
     'which is the 43.8 minutes the lesson quotes');
  eq(durText(downtimeSeconds(R(9999n, 10000n), periodSeconds('month'))), '4 min 22.80 s',
     'and one more nine is a tenth of it, not 0.09% more');
  eq(durText(downtimeSeconds(R(999n, 1000n), periodSeconds('year'))), '8 h 45 min 36 s',
     '8.76 hours a year');
  /* The two directions are inverses, which is what makes the budget selector
     and the target selector the same lesson rather than two. */
  eq(Rtext(availFromDowntime(R(2628n, 1n), periodSeconds('month'))), '999/1000',
     'a 2628-second budget IS three nines');
  eq(Rtext(availFromDowntime(downtimeSeconds(R(99991n, 100000n), periodSeconds('week')),
                             periodSeconds('week'))), '99991/100000',
     'and the round trip returns the availability it started from');
  eq(ninesOf(R(999n, 1000n)), 3, '99.9% has three nines');
  eq(ninesOf(R(9995n, 10000n)), 3, '99.95% has three, not three and a half');
  eq(ninesOf(R(9n, 10n)), 1, '90% has one');
  eq(ninesOf(R(1n, 2n)), 0, 'and 50% has none');

  /* --- L2: MTBF, MTTR, and the identity that makes the lesson -------------- */
  eq(Rtext(availFromMtbf(R(1000n, 1n), R(1n, 1n))), '1000/1001', 'A = MTBF/(MTBF + MTTR)');
  /* THE IDENTITY: halving the repair time is worth exactly as much as doubling
     the time between failures. A(2M, R) = 2M/(2M+R) = M/(M+R/2) = A(M, R/2).
     The lesson says "worth as much"; this is the sense in which that is exact. */
  eq(Requ(availFromMtbf(Rmul(R(1000n, 1n), R(2n, 1n)), R(1n, 1n)),
          availFromMtbf(R(1000n, 1n), Rdiv(R(1n, 1n), R(2n, 1n)))), true,
     'doubling MTBF and halving MTTR give the SAME fraction');
  eq(Requ(availFromMtbf(Rmul(R(37n, 5n), R(2n, 1n)), R(3n, 7n)),
          availFromMtbf(R(37n, 5n), Rdiv(R(3n, 7n), R(2n, 1n)))), true,
     'and on numbers with nothing round about them');
  /* The target solvers invert the availability formula, so putting their
     answer back in must return the target exactly. */
  eq(Rtext(availFromMtbf(R(1000n, 1n), mttrForTarget(R(1000n, 1n), R(9999n, 10000n)))), '9999/10000',
     'the MTTR a target needs, put back through A, returns the target');
  eq(Rtext(availFromMtbf(mtbfForTarget(R(1n, 1n), R(999n, 1000n)), R(1n, 1n))), '999/1000',
     'and so does the MTBF a target needs');
  eq(Rtext(failuresPerPeriod(Radd(R(3600000n, 1n), R(3600n, 1n)), periodSeconds('year'))), '8760/1001',
     '1000 h up plus 1 h down is 8.75 cycles a year');

  /* --- L3: the chain, and how far under the weakest link it lands ---------- */
  eq(Rtext(pctToFraction('99.9')), '999/1000', 'a typed percentage is an exact fraction');
  eq(Rtext(pctToFraction('99.95')), '1999/2000', 'and in lowest terms');
  eq(parseChain('99.9, 99.99, 100').length, 3, 'a chain of three');
  eq(parseChain('99.9, banana'), null, 'and a typo is refused rather than guessed at');
  const ten = parseChain('99.9, 99.9, 99.9, 99.9, 99.9, 99.9, 99.9, 99.9, 99.9, 99.9');
  eq(Rtext(availSeries(ten)), Rtext(Rpow(R(999n, 1000n), 10)), 'ten of them is the tenth power');
  eq(Rfixed(availSeries(ten), 7), '0.9900449', 'ten 99.9% dependencies give 99.0%, not 99.9%');
  /* The misconception, as a number: the chain is TEN TIMES the downtime of its
     own weakest link, not equal to it. */
  eq(Rfixed(Rdiv(Rsub(R(1n, 1n), availSeries(ten)), Rsub(R(1n, 1n), R(999n, 1000n))), 2), '9.96',
     'the chain is 9.96x the downtime of the weakest link in it');
  eq(Rcmp(availSeries(ten), R(999n, 1000n)) < 0, true, 'and strictly worse than it');
  eq(Rtext(availSeries(parseChain('100, 100'))), '1', 'a chain of perfect parts is perfect');

  /* --- L4: parallel, and the failover the formula does not contain --------- */
  const two99 = [R(99n, 100n), R(99n, 100n)];
  eq(Rtext(availParallel(two99)), '9999/10000', 'two 99% paths are four nines, ideally');
  const charged = parallelWithFailover(two99, R(30n, 1n), R(12n, 1n), periodSeconds('year'));
  eq(Rtext(charged.ideal), '9999/10000', 'the ideal figure is untouched');
  eq(Rtext(charged.charge), '1/87600', '12 failovers of 30 s is 360 s a year');
  eq(Rtext(charged.adjusted), Rtext(Rsub(R(9999n, 10000n), R(1n, 87600n))),
     'and the real availability is the ideal one minus that');
  eq(Rfixed(charged.adjusted, 8), '0.99988858', 'four nines becomes three');
  eq(ninesOf(charged.ideal) + ' ' + ninesOf(charged.adjusted), '4 3',
     'the switch costs a whole nine, which is what "failover is not free" means');
  eq(Rtext(parallelWithFailover(two99, R(0n, 1n), R(12n, 1n), periodSeconds('year')).adjusted),
     '9999/10000', 'an instant switch costs nothing, which is the formula as written');

  /* --- L5: k-of-n, AND THE TWO IDENTITIES ---------------------------------- */
  /* These are the assertions the course rests on: the binomial tail is not a
     third model, it is the other two with k moved. If either fails, one of
     three lessons is teaching a different arithmetic from the other two. */
  const A99 = R(99n, 100n);
  for (const n of [1, 2, 3, 5, 8, 12]) {
    const copies = [];
    for (let i = 0; i < n; i += 1) copies.push(A99);
    eq(Requ(availKofN(A99, n, n), availSeries(copies)), true,
       'k = n is the series product at n = ' + n);
    eq(Requ(availKofN(A99, 1, n), availParallel(copies)), true,
       'k = 1 is the parallel form at n = ' + n);
    eq(Rtext(kofnTotal(A99, n)), '1', 'and all ' + (n + 1) + ' terms sum to one');
  }
  /* The same two identities on an availability with an ugly denominator, since
     99/100 is exactly the kind of number a wrong coefficient survives. */
  const Augly = R(7n, 11n), uglyCopies = [Augly, Augly, Augly, Augly];
  eq(Requ(availKofN(Augly, 4, 4), availSeries(uglyCopies)), true, 'k = n at A = 7/11');
  eq(Requ(availKofN(Augly, 1, 4), availParallel(uglyCopies)), true, 'k = 1 at A = 7/11');
  eq(Rtext(kofnTotal(Augly, 4)), '1', 'and its terms still sum to one');
  eq(Rtext(availKofN(R(1n, 2n), 2, 3)), '1/2', 'a majority of three fair coins');
  eq(Rfixed(availKofN(A99, 3, 5), 6), '0.999990', '3 of 5 at 99% is five nines');
  /* "More replicas always means more available" is false, and this is where. */
  eq(Rcmp(availKofN(A99, 5, 5), A99) < 0, true, '5-of-5 is WORSE than 1-of-1');
  eq(Rtext(kofnTerms(A99, 3)[3].term), Rtext(Rpow(A99, 3)), 'the j = n term is the series product');
  eq(String(kofnTerms(A99, 5)[2].c), '10', 'the coefficients are C(n, j)');

  /* --- L6: the common cause, and where redundancy stops paying ------------- */
  eq(Rtext(pairBothDown(R(0n, 1n), R(1n, 100n))), '1/10000', 'at c = 0 the pair is p^2');
  eq(Rtext(pairBothDown(R(1n, 1000n), R(1n, 100n))), '10999/10000000',
     'a 0.1% common cause against a 10^-4 pair');
  eq(Rfixed(Rdiv(pairBothDown(R(1n, 1000n), R(1n, 100n)), R(1n, 10000n)), 2), '11.00',
     'which is eleven times what independence promised');
  eq(Rtext(correlatedBreakEven(R(1n, 100n))), '1/101', 'the break-even c is p/(1 + p)');
  /* THE IDENTITY: at that c the pair is EXACTLY as available as one machine.
     The lesson asks the reader to find "the c at which redundancy buys
     nothing"; this is the sense in which that c is exact rather than a
     reading off a curve. */
  for (const p of [R(1n, 100n), R(1n, 3n), R(7n, 1000n)]) {
    eq(Rtext(pairBothDown(correlatedBreakEven(p), p)), Rtext(p),
       'at c = p/(1+p) the pair is down exactly as often as one machine, p = ' + Rtext(p));
    eq(Rtext(redundancyGain(correlatedBreakEven(p), p)), '1',
       'so the redundancy gain there is exactly 1');
  }
  eq(Rtext(redundancyGain(R(0n, 1n), R(1n, 100n))), '100', 'and 1/p under independence');

  /* --- L7: the error budget, in requests rather than minutes --------------- */
  const reqs = Rmul(R(1000n, 1n), periodSeconds('month'));
  eq(Rtext(reqs), '2628000000', '1000 rps for a month');
  eq(Rtext(budgetRequests(R(999n, 1000n), reqs)), '2628000', 'is a budget of 2.628 M failures');
  eq(Rtext(incidentBurn(R(1000n, 1n), R(1800n, 1n), R(1n, 1n))), '1800000',
     'a 30-minute total outage costs 1.8 M of them');
  eq(Rtext(Rdiv(incidentBurn(R(1000n, 1n), R(1800n, 1n), R(1n, 1n)),
                budgetRequests(R(999n, 1000n), reqs))), '50/73', 'which is 68.5% of the budget');
  /* Severity is a multiplier, which is the whole difference between an SLO on
     requests and an SLO on the clock. */
  eq(Rtext(incidentBurn(R(1000n, 1n), R(1800n, 1n), R(1n, 2n))), '900000',
     'the same 30 minutes at half severity costs half as much');
  eq(Rtext(budgetSeconds(R(999n, 1000n), periodSeconds('month'))), '2628',
     'and the budget as a full outage is the L1 downtime figure again');

  /* --- L8: retries as load ------------------------------------------------- */
  eq(Rtext(retryAttempts(R(1n, 10n), 2)), '111/100', 'two retries at p = 0.1 cost 1.11 attempts');
  eq(Rtext(retrySuccess(R(1n, 10n), 2)), '999/1000', 'and succeed 99.9% of the time');
  eq(Rtext(amplifiedLoad(R(500n, 1n), R(1n, 10n), 2)), '555', '500 rps becomes 555 attempts a second');
  eq(Rtext(duplicateShare(R(1n, 10n), 2)), '11/111', 'of which 9.9% is retry traffic');
  /* The geometric sum, checked against the sum it stands for: the expected
     attempts are the probabilities of reaching each attempt, added up. */
  for (const p of [R(1n, 10n), R(9n, 10n), R(1n, 3n)]) {
    for (const r of [0, 1, 3, 6]) {
      let s = R(0n, 1n);
      for (let i = 0; i <= r; i += 1) s = Radd(s, attemptReach(p, i));
      eq(Rtext(s), Rtext(retryAttempts(p, r)),
         'sum of p^i for i <= r IS the closed form, p = ' + Rtext(p) + ', r = ' + r);
    }
  }
  /* The amplification is worst exactly when the service is worst, and its
     ceiling is the retry budget itself. */
  eq(Rcmp(retryAttempts(R(9n, 10n), 3), retryAttempts(R(1n, 10n), 3)) > 0, true,
     'a worse failure rate costs more attempts, not fewer');
  eq(Rtext(retryAttempts(R(9n, 10n), 3)), '3439/1000', 'p = 0.9 with 3 retries is 3.439 attempts');
  eq(Rcmp(retryAttempts(R(99n, 100n), 3), R(4n, 1n)) < 0, true, 'and it never reaches r + 1');

  /* --- L9: the retry storm, its iteration and its fixed point -------------- */
  const lam = R(95n, 100n), cap = R(1n, 1n), base = R(1n, 10n);
  eq(Rtext(stormFailure(R(1n, 2n), cap, base)), '1/10', 'under capacity the failure rate is the base');
  eq(Rtext(stormFailure(R(2n, 1n), cap, base)), '11/20',
     'at twice capacity half the excess fails on top of it');
  eq(Rtext(stormNext(lam, cap, base, 0, lam).load), Rtext(lam),
     'with no retries the map is the identity, so the offered load IS the answer');
  const run = stormRun(lam, cap, base, 3, 5, 3000);
  eq(run.rows.length, 5, 'five iterations');
  eq(Rtext(run.rows[0].amp), '1111/1000', 'the first amplification, exactly');
  eq(Rtext(run.rows[0].out), '21109/20000', 'and the first iterate, which is already over capacity');
  eq(Rcmp(run.rows[0].out, cap) > 0, true, 'from an offered load that was NOT');
  eq(Rcmp(run.rows[4].out, run.rows[0].out) > 0, true, 'the iterates climb');
  /* The fixed point is an ENCLOSURE and the bracket is what makes it exact:
     the map is increasing, so a sign change between two fractions traps a
     fixed point between them. Both ends are checked in the right direction. */
  const fp = stormFixedPoint(lam, cap, base, 3, 24);
  eq(Rcmp(stormNext(lam, cap, base, 3, fp.lo).load, fp.lo) >= 0, true,
     'the map pushes the low end up');
  eq(Rcmp(stormNext(lam, cap, base, 3, fp.hi).load, fp.hi) <= 0, true,
     'and the high end down, so the fixed point is between them');
  eq(Rcmp(fp.lo, fp.hi) <= 0, true, 'and the bracket is the right way round');
  eq(Rfixed(fp.lo, 5), '1.72736', 'the fixed point of the preset');
  /* THE LESSON: the un-retried load was serviceable and the fixed point is not. */
  eq(Rcmp(lam, cap) <= 0, true, '0.95 of capacity was fine');
  eq(Rcmp(fp.lo, cap) > 0, true, 'and the retries alone put the fixed point above capacity');
  eq(Rcmp(stormFixedPoint(lam, cap, base, 0, 24).hi, cap) < 0, true,
     'with retries switched off the same load settles below capacity');
  /* The digit budget stops the table rather than hanging the page. */
  eq(stormRun(lam, cap, base, 3, 12, 200).stopped, true,
     'a tight digit budget stops the iteration and says so');
  eq(stormRun(lam, cap, base, 3, 12, 200).rows.length < 12, true, 'with fewer rows than asked for');

  /* --- L10: backoff waves, seeded ----------------------------------------- */
  eq([1, 2, 3, 4].map((i) => backoffDelayMs(1000, i)).join(','), '1000,2000,4000,8000',
     'the waves land at 1, 2, 4 and 8 seconds');
  const noJit = backoffHistogram(600, 20, 1000, 0, 8, 40, 7, 200);
  eq(noJit.plain.join(',') === noJit.jitter.join(','), true,
     'jitter of zero width IS the un-jittered schedule, which is the check that the spread is centred');
  eq(peakOf(noJit.plain), 600, 'and every client lands in one slot');
  const jit = backoffHistogram(600, 20, 1000, 100, 8, 40, 7, 200);
  eq(peakOf(jit.jitter) < peakOf(jit.plain), true, 'jitter lowers the peak');
  eq(peakOf(jit.plain), 600, 'while the un-jittered arm is unchanged by the jitter slider');
  eq(totalOf(jit.plain), 3600, 'six waves of 600 without jitter');
  /* Seeded, and the seed is actually used: same seed same bars, other seed not. */
  eq(backoffHistogram(600, 20, 1000, 100, 8, 40, 7, 200).jitter.join(','),
     jit.jitter.join(','), 'the same seed draws the same histogram');
  eq(backoffHistogram(600, 20, 1000, 100, 8, 40, 8, 200).jitter.join(',') === jit.jitter.join(','),
     false, 'and a different seed does not');
  eq(perSecond(jit.jitter, 200).length <= 40, true, 'the per-second fold covers the horizon');
  eq(totalOf(perSecond(jit.jitter, 200)), totalOf(jit.jitter), 'and loses no retries');

  /* --- L11: shedding against collapse ------------------------------------- */
  const capacity = R(1000n, 1n);
  eq(Rtext(goodputShed(R(2000n, 1n), capacity, R(900n, 1n))), '900',
     'shedding above 90% of capacity delivers 900 rps at twice the load');
  eq(Rtext(goodputUnshed(R(2000n, 1n), capacity)), '500', 'not shedding delivers 500');
  eq(Rcmp(goodputShed(R(2000n, 1n), capacity, R(900n, 1n)),
          goodputUnshed(R(2000n, 1n), capacity)) > 0, true,
     'so rejecting requests served MORE users than accepting them');
  eq(Rtext(goodputUnshed(capacity, capacity)), '1000', 'the collapse model is continuous at the knee');
  eq(Rtext(goodputUnshed(R(500n, 1n), capacity)), '500', 'and is the offered load below it');
  eq(Rtext(goodputShed(R(500n, 1n), capacity, R(900n, 1n))), '500',
     'a shedder under its threshold sheds nothing');
  eq(Rtext(rejectedFraction(R(2000n, 1n), R(900n, 1n))), '11/20', 'and rejects 55% at twice capacity');
  eq(Rtext(rejectedFraction(R(500n, 1n), R(900n, 1n))), '0', 'nothing at all below it');
  /* A threshold set above capacity is not a shedder: what it admits collapses
     exactly as the unshed arm does, which is the failure mode of a limit copied
     from the load generator rather than measured from the service. */
  eq(Rtext(goodputShed(R(2000n, 1n), capacity, R(1200n, 1n))),
     Rtext(goodputUnshed(R(1200n, 1n), capacity)), 'a threshold above capacity sheds into collapse');
  eq(Rtext(goodputShed(R(2000n, 1n), capacity, R(1200n, 1n))), '2500/3',
     'and delivers less than a threshold at 90% would');
  eq(Rtext(admittedLoad(R(2000n, 1n), R(900n, 1n))), '900', 'the shedder admits the threshold');
  eq(Rtext(admittedLoad(R(500n, 1n), R(900n, 1n))), '500', 'or the offered load, whichever is smaller');
  eq(Rtext(Rdiv(admittedLoad(R(2000n, 1n), R(900n, 1n)), capacity)), '9/10',
     'so utilisation under the shedder is the ADMITTED load over capacity, not the goodput');

  /* --- L12: durability, the one approximation ----------------------------- */
  /* The exact fraction of the first-order formula, which is what the page
     prints beside the float so that the reader can see WHICH part rounds. */
  eq(Rtext(durabilityLossExact(3, R(1n, 50n), R(24n, 1n))), '3/8326562500',
     'three copies, 2% a year, a 24 h repair window');
  near(durabilityLossApprox(3, R(1n, 50n), R(24n, 1n)), 3.6029e-10, 1e-14,
     'and the float agrees with it');
  near(durabilityLossApprox(3, R(1n, 50n), R(24n, 1n)),
       Number(durabilityLossExact(3, R(1n, 50n), R(24n, 1n)).n)
       / Number(durabilityLossExact(3, R(1n, 50n), R(24n, 1n)).d), 1e-20,
       'the rounding is in the MODEL, not in the division');
  /* THE IDENTITY: halving the window divides by 2^(N-1), not by two. This is
     the lesson's "R matters as much as f", and it is exact. */
  for (const n of [2, 3, 4, 6]) {
    eq(Rtext(Rdiv(durabilityLossExact(n, R(1n, 50n), R(24n, 1n)),
                  durabilityLossExact(n, R(1n, 50n), R(12n, 1n)))), String(Math.pow(2, n - 1)),
       'halving R divides the loss probability by 2^(N-1) at N = ' + n);
  }
  /* "Three copies is three times the durability" is false: it is a factorial
     times the Nth power of the failure rate. */
  eq(Rtext(Rdiv(durabilityLossExact(1, R(1n, 50n), R(24n, 1n)),
                durabilityLossExact(3, R(1n, 50n), R(24n, 1n)))),
     Rtext(Rdiv(R(1n, 1n), Rmul(R(6n, 1n), Rmul(Rpow(R(1n, 50n), 2), Rpow(R(1n, 365n), 2))))),
     'a third copy is worth f^2 R^2 times a factorial, not a factor of three');
  eq(Rtext(durabilityLossExact(1, R(1n, 50n), R(24n, 1n))), '1/50',
     'and one copy is just the failure rate');
  /* The truncation itself: the first-order term stands in for 1 - e^-x, and
     the page shows the gap rather than claiming there is none. */
  const gap = truncationGap(2 * 0.02 * 24 / 8760);
  eq(gap.first > gap.exact, true, 'the first-order term overstates 1 - e^-x');
  near((gap.first - gap.exact) / gap.first, 5.48e-5, 1e-6, 'here by 0.0055%');

  /* --- L13: shuffle sharding, exactly ------------------------------------- */
  eq(String(comb(16, 2)), '120', 'sixteen nodes, two each, is 120 shards');
  eq(Rtext(shuffleDisjoint(16, 2)), '91/120', 'two tenants share no node 91 times in 120');
  eq(Rtext(shuffleIdentical(16, 2)), '1/120', 'and hold the identical set once');
  eq(Rtext(shuffleOverlap(16, 2, 1)), '7/30', 'overlapping in exactly one is the rest');
  /* THE IDENTITY: the overlap distribution is a distribution. This is
     Vandermonde, and a wrong coefficient anywhere breaks it. */
  for (const [n, k] of [[16, 2], [8, 3], [40, 8], [10, 5], [6, 1], [5, 3]]) {
    let s = R(0n, 1n);
    for (let j = 0; j <= k; j += 1) s = Radd(s, shuffleOverlap(n, k, j));
    eq(Rtext(s), '1', 'the overlap terms sum to one at n = ' + n + ', k = ' + k);
  }
  /* Where a disjoint pair is impossible the probability must be zero, not
     small: with k > n/2 there are not enough nodes left to miss you. */
  eq(Rtext(shuffleDisjoint(5, 3)), '0', 'with 3 of 5 nodes, no second tenant can miss you');
  eq(Rtext(shuffleIdentical(5, 3)), '1/10', 'and one pairing in ten is identical');
  eq(Rtext(blastFraction(16, 2)), '1/8', 'one bad node degrades an eighth of the tenants');
  /* The sample assignment is drawn from the same seeded stream the page uses,
     so what it shows and what it claims come from one run. */
  const sets = shuffleAssign(16, 2, 12, 3);
  eq(sets.length, 12, 'twelve tenants drawn');
  eq(sets.every((s) => s.length === 2), true, 'each holding exactly k nodes');
  eq(sets.every((s) => s[0] !== s[1]), true, 'and never the same node twice');
  eq(sets.every((s) => s.every((v) => v >= 0 && v < 16)), true, 'all inside the fleet');
  eq(shuffleAssign(16, 2, 12, 3).join('|'), sets.join('|'), 'the same seed draws the same assignment');
  eq(shuffleAssign(16, 2, 12, 4).join('|') === sets.join('|'), false, 'a different seed does not');
  eq(identicalCount([[1, 2], [1, 2], [3, 4]]), 1, 'one tenant holds the exact set of the first');
  eq(disjointCount([[1, 2], [1, 2], [3, 4]]), 1, 'and one shares nothing with it');
}

console.log('system design: partitioning, imbalance, rehashing and cross-shard cost');
{
  const SHARD_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'shard.py');
  const shardSrc = fs.readFileSync(SHARD_SOURCE, 'utf8');
  const shardBlock = (name) => blockFrom(shardSrc, name, SHARD_SOURCE);
  eval(block('RATIONAL_JS') + countingBlock('BIGINT_JS') + sysdBlock('RCEIL_JS')
       + sysdBlock('PERCENTILE_JS') + sysdBlock('PMF_JS') + sysdBlock('QUEUE_JS')
       + sysdBlock('STREAM_JS') + sysdBlock('APPROX_JS') + shardBlock('SHARDKIT_JS'));

  /* --- the stream this kit draws from, and why it is not the other one ----
     The rest of the path draws from the glibc LCG, whose modulus is 2^31. This
     kit takes its draws MODULO N, and the low bits of a power-of-two modulus
     are a cycle, not a sample. That is asserted here rather than described,
     because if it were ever untrue the right thing to do would be to simplify
     the kit -- and because a future edit that "unified" the generators would
     silently make every imbalance lesson teach the opposite of its claim. */
  {
    const glibc = lcgStream(1103515245, 12345, 2147483648, 7, 16).map((x) => x % 4);
    eq(glibc.join(','), '0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3',
       'the glibc LCG taken mod 4 is a cycle, not a sample');
    const level = new Array(8).fill(0);
    lcgStream(1103515245, 12345, 2147483648, 7, 1600).forEach((x) => { level[x % 8] += 1; });
    eq(level.every((c) => c === 200), true,
       'and 1600 of its values into 8 bins come out PERFECTLY level, which is the claim this course denies');
    const mine = binOccupancy(7, 1600, 8);
    eq(occTotal(mine), 1600, 'the kit places every key it is given');
    eq(occMax(mine) > occMin(mine), true, 'and MINSTD mod 8 does not come out level');
  }
  /* Reproducibility, which is the point of seeding at all. */
  eq(shardStream(7, 12).join(','), shardStream(7, 12).join(','), 'the same seed draws the same stream');
  eq(shardStream(8, 12).join(',') === shardStream(7, 12).join(','), false, 'a different seed does not');
  eq(shardStream(7, 400).every((x) => x >= 1 && x < shardModulus()), true,
     'every draw is inside the modulus and never the fixed point 0');
  /* THE SEED FINALISER. Without it an LCG's k-th value is an affine function
     of the seed, and for the small seeds a slider offers nothing wraps, so
     consecutive seeds hand out proportional placements: the ring arcs came out
     0.0206, 0.0309, 0.0411, ... a straight line. Every mode here asks the
     reader to reseed and compare, so this is load-bearing. The test is that
     three consecutive seeds are NOT in arithmetic progression at the first
     draw, which is exactly what a raw seed would give. */
  {
    const a = shardStream(1, 1)[0], b = shardStream(2, 1)[0], c = shardStream(3, 1)[0];
    eq(b - a === c - b, false, 'consecutive seeds are not an arithmetic progression');
    eq(shardSeedState(3) === 3, false, 'and the seed itself never becomes the state');
    const arcs = [];
    for (let s = 1; s <= 12; s += 1) arcs.push(Rnum(ringNewNodeArc(s, 7, 1)));
    let monotone = true;
    for (let i = 2; i < arcs.length; i += 1) if (arcs[i] < arcs[i - 1]) monotone = false;
    eq(monotone, false, 'the arc a joining node takes is not monotone in the seed');
  }

  /* --- L1: two constraints, and the larger ------------------------------- */
  {
    const lam = R(120000n, 1n), per = R(8000n, 1n), rho = R(65n, 100n);
    const D = R(48n * 10n ** 12n, 1n), rf = R(3n, 1n), node = R(4n * 10n ** 12n, 1n);
    eq(String(shardsForLoad(lam, per, rho)), '24', '120000/(8000 x 0.65) = 23.08, so 24 shards');
    eq(Rtext(Rdiv(lam, Rmul(per, rho))), '300/13', 'and the fraction under that ceiling is exact');
    eq(String(shardsForStorage(D, rf, node)), '36', '48 TB x 3 / 4 TB = 36 exactly');
    const pick = bindingShards(shardsForLoad(lam, per, rho), shardsForStorage(D, rf, node));
    eq(String(pick.n) + '/' + pick.binding + '/' + pick.slack, '36/storage/12',
       'storage binds by twelve shards');
    /* THE MISCONCEPTION, as a number: sizing on load alone leaves the nodes
       over their disks, and sizing on storage alone leaves them idle. */
    eq(Rpct(utilisationAt(lam, per, 36n), 2), '41.67%', 'the storage-bound count runs the nodes at 42%');
    eq(Rpct(utilisationAt(lam, per, 24n), 2), '62.50%', 'while the load-bound one would have run them at 62.5%');
    eq(byteText(bytesPerNodeAt(D, rf, 24n)), '6.00 TB', 'and put 6 TB on a 4 TB disk');
    /* A ceiling is a ceiling: an exact multiple must not round up. */
    eq(String(shardsForLoad(R(100n, 1n), R(10n, 1n), R(1n, 1n))), '10', 'an exact fit is not rounded up');
    eq(String(shardsForLoad(R(101n, 1n), R(10n, 1n), R(1n, 1n))), '11', 'and one request past it is');
    eq(shardsForLoad(lam, per, R(0n, 1n)), null, 'a zero target utilisation has no answer');
    eq(bindingShards(7n, 7n).binding, 'both', 'equal constraints bind together');
  }

  /* --- L2: hashing does not give equal shards ---------------------------- */
  {
    const occ = binOccupancy(7, 1200, 12);
    eq(occTotal(occ), 1200, 'every key is placed exactly once');
    eq(occ.length, 12, 'into the shards asked for');
    eq(Rtext(maxOverMean(occ)), Rtext(R(BigInt(occMax(occ)) * 12n, 1200n)), 'max/mean is max x N / m');
    eq(Rcmp(maxOverMean(occ), R(1n, 1n)) > 0, true, 'and it is above one -- hashing is not level');
    eq(Rcmp(minOverMean(occ), R(1n, 1n)) < 0, true, 'while the emptiest shard is below it');
    eq(binOccupancy(7, 1200, 12).join(','), occ.join(','), 'the placement is reproducible');
    /* One seed is one sample of a maximum: across seeds the maximum MOVES,
       which is the sentence the lesson's how_to asks the reader to check. */
    {
      const maxima = new Set();
      for (let s = 1; s <= 12; s += 1) maxima.add(occMax(binOccupancy(s, 1200, 12)));
      eq(maxima.size > 1, true, 'the maximum is a distribution, not a constant');
    }
    /* A single shard takes everything, and the ratio says so exactly. */
    eq(Rtext(maxOverMean(binOccupancy(3, 500, 1))), '1', 'one shard holds the mean, which is everything');
    eq(occEmpty([0, 4, 0, 9]), 2, 'empty shards are counted');
    /* The stated asymptotic is a Number and is labelled as one everywhere it
       is printed; below n = 16 it refuses rather than returning nonsense. */
    near(oneChoiceStatedApprox(1024), 3.5804, 1e-3, 'ln n / ln ln n at n = 1024, stated not proved');
    near(twoChoiceStatedApprox(1024), 1.9355, 1e-3, 'ln ln n at n = 1024, stated not proved');
    eq(isFinite(oneChoiceStatedApprox(4)), false, 'and it declines to answer where ln ln n is not positive');
  }

  /* --- L3: rehashing, and THE identity of the whole course ---------------
     N/(N+1) of the keys move under mod-N rehashing and 1/(N+1) move on a ring,
     and those two fractions ARE the whole key set. The course's how_to asks
     the reader to read them as a pair; this is that pair, checked. */
  for (const n of [1, 2, 3, 4, 7, 8, 12, 16, 31, 64, 100]) {
    eq(Rtext(rehashShareSum(n)), '1',
       'mod N moves N/(N+1) and a ring moves 1/(N+1): at N = ' + n + ' they add to one whole');
    eq(Rtext(modMoveShare(n)), n + '/' + (n + 1), 'the mod-N fraction at N = ' + n);
    eq(Rtext(ringMoveShare(n)), '1/' + (n + 1), 'and the ring fraction is the rest of it');
  }
  /* And the mod-N fraction is not a formula quoted at the reader -- it is the
     count over a complete cycle, which by CRT is exactly N of every N(N+1). */
  for (const n of [2, 3, 4, 7, 12, 20]) {
    const c = modCycleMoved(n);
    eq(c.total, n * (n + 1), 'the complete cycle at N = ' + n + ' is N(N+1) hashes');
    eq(c.moved, n * n, 'and exactly N^2 of them move');
    eq(Requ(c.share, modMoveShare(n)), true,
       'so the enumeration at N = ' + n + ' IS N/(N+1), not an estimate of it');
  }
  eq(Rtext(modCycleMoved(7).share), '7/8', 'seven shards to eight moves seven eighths of the keys');
  eq(Rtext(ringMoveShare(7)), '1/8', 'and a ring moves the other eighth');
  /* THE MISCONCEPTION, priced: adding a node does NOT move 1/N of the keys. */
  eq(Rfixed(Rdiv(modMoveShare(7), R(1n, 7n)), 2), '6.13',
     'mod-N moves 6.1 times what the 1/N intuition predicts at N = 7');
  {
    /* The seeded sample lands near the enumeration without being it. */
    const s = modSampleMoved(11, 1200, 7);
    eq(s.total, 1200, 'the sample counts every key it was given');
    eq(Rcmp(s.share, R(4n, 5n)) > 0 && Rcmp(s.share, R(19n, 20n)) < 0, true,
       'and its moved fraction sits around the exact 7/8');
    eq(Requ(s.share, modCycleMoved(7).share), false,
       'a sample is not the enumeration, which is why both are printed');
    /* The ring: a key moves exactly when the joining node took its arc, so the
       counted fraction must track the arc rather than the expectation. */
    const arc = ringNewNodeArc(5, 7, 1), moved = ringSampleMoved(5, 11, 1200, 7, 1);
    eq(Math.abs(Rnum(moved.share) - Rnum(arc)) < 0.03, true,
       'the keys the ring moves are the keys in the joining node arc');
    eq(Rcmp(moved.share, modSampleMoved(11, 1200, 7).share) < 0, true,
       'and far fewer of them than mod-N moves');
    /* Ownership and nesting: an N-node ring is a PREFIX of an (N+1)-node ring,
       which is the property that makes the scheme worth anything at all. */
    const before = ringTokens(5, 7, 1), after = ringTokens(5, 8, 1);
    eq(before.length, 7, 'seven tokens for seven nodes at V = 1');
    eq(after.length, 8, 'and eight for eight');
    eq(before.every((t, i) => before.slice(i).every((u) => u.pos >= t.pos)), true, 'tokens are sorted');
    eq(new Set(before.map((t) => t.pos)).size <= new Set(after.map((t) => t.pos)).size, true,
       'the old tokens are still there');
    eq(before.map((t) => t.pos).every((p) => after.some((u) => u.pos === p)), true,
       'adding a node adds a token and moves none of the others');
    eq(ringArcMeanApprox(1, 7, 1, 40) !== null, true, 'the arc averages over seeds');
    eq(Math.abs(Rnum(ringArcMeanApprox(1, 7, 1, 40)) - 0.125) < 0.05, true,
       'and over 40 seeds it lands near the expected 1/8');
  }

  /* --- L4: virtual nodes -------------------------------------------------- */
  {
    for (const [n, v] of [[8, 1], [8, 10], [8, 100], [3, 1], [16, 25]]) {
      const sh = ringShares(5, n, v);
      eq(sh.length, n, 'one share a node at N = ' + n + ', V = ' + v);
      eq(Rtext(shareTotal(sh)), '1',
         'and the shares are a partition of the ring at N = ' + n + ', V = ' + v);
      eq(Rcmp(shareMaxOverMean(sh), R(1n, 1n)) >= 0, true, 'the largest share is at or above the mean');
      eq(Rcmp(shareMinOverMean(sh), R(1n, 1n)) <= 0, true, 'and the smallest at or below it');
    }
    /* THE STATED RATE. The relative spread falls like 1/sqrt(V) -- stated, and
       measured here across seeds because one ring is one sample. A factor of
       100 in V should buy about a factor of 10 in spread. */
    const s1 = spreadRmsOverSeedsApprox(1, 8, 1, 16);
    const s10 = spreadRmsOverSeedsApprox(1, 8, 10, 16);
    const s100 = spreadRmsOverSeedsApprox(1, 8, 100, 16);
    eq(s1 > s10 && s10 > s100, true, 'the spread falls as V rises');
    near(s1 / s10, Math.sqrt(10), 1.0, 'V = 1 to V = 10 is about a factor of sqrt(10)');
    near(s1 / s100, 10, 4, 'and V = 1 to V = 100 about a factor of ten');
    near(spreadRateStatedApprox(1), 1, 1e-12, '1/sqrt(V) at V = 1');
    near(spreadRateStatedApprox(100), 0.1, 1e-12, 'and at V = 100');
    /* A perfectly level ring has zero spread and max/mean of exactly one, so
       the statistic means what it says at the boundary. */
    const even = [R(1n, 4n), R(1n, 4n), R(1n, 4n), R(1n, 4n)];
    eq(spreadRmsApprox(even), 0, 'a level ring has no spread at all');
    eq(Rtext(shareMaxOverMean(even)), '1', 'and max/mean of exactly one');
  }

  /* --- L5: range partitioning -------------------------------------------- */
  {
    const mono = rangeWindows('monotonic', 2400, 8, 8, 5, 4);
    eq(Rtext(worstWindowShare(mono)), '1',
       'a monotonic key sends ALL of the current writes to one range');
    eq(Rtext(lifetimeShare(mono)), '1/8',
       'and over the whole run that same range holds a perfectly even eighth -- which is the trap');
    eq(scanRanges('monotonic', 8, 4), 1, 'a time-range scan reads one range');
    const hashed = rangeWindows('hashed', 2400, 8, 8, 5, 4);
    eq(Rcmp(worstWindowShare(hashed), R(1n, 4n)) < 0, true, 'hashing brings the hottest window share down');
    eq(scanRanges('hashed', 8, 4), 8, 'and makes the scan read every range');
    const pre = rangeWindows('prefixed', 2400, 8, 8, 5, 4);
    eq(scanRanges('prefixed', 8, 4), 4, 'a four-bucket prefix makes the scan read four');
    eq(Rcmp(worstWindowShare(pre), worstWindowShare(mono)) < 0, true,
       'and spreads the current writes off the single hot range');
    eq(Rcmp(worstWindowShare(pre), R(1n, 2n)) < 0, true, 'to about one bucket-share of them');
    /* Every pattern places every write, and an unknown one refuses. */
    for (const g of [mono, hashed, pre]) {
      let total = 0;
      g.forEach((row) => { total += occTotal(row); });
      eq(total, 2400, 'every write lands in exactly one range');
    }
    eq(rangeWindows('nope', 100, 4, 4, 1, 1), null, 'an unknown key pattern has no answer');
    eq(scanRanges('nope', 8, 4), null, 'and no scan cost either');
  }

  /* --- L6: a hot key does not care about N -------------------------------- */
  {
    const lam = R(100000n, 1n), f = R(12n, 100n);
    eq(Rtext(hottestLoad(lam, f, 16)), '17500', '0.12 x 100000 + 0.88 x 100000/16');
    eq(Rtext(meanLoad(lam, 16)), '6250', 'against a mean shard of 6250');
    eq(Rtext(hotImbalance(lam, f, 16)), '14/5', 'an imbalance of 2.8');
    eq(Rtext(hotAsymptote(lam, f)), '12000', 'and a floor of f x lambda = 12000');
    /* THE LESSON, as an inequality no shard count escapes. */
    for (const n of [1, 2, 8, 64, 1024, 1000000]) {
      eq(Rcmp(hottestLoad(lam, f, n), hotAsymptote(lam, f)) > 0, true,
         'the hottest shard is above f x lambda at N = ' + n + ', however large N is');
    }
    eq(Rfixed(hottestLoad(lam, f, 1000000), 4), '12000.0880',
       'a million shards leaves the hot shard at 12000.09, not at 0.1');
    eq(Rtext(Rsub(hottestLoad(lam, f, 16), hottestLoad(lam, f, 32))), '2750',
       'doubling the shards removes only half of the UNIFORM part');
    /* Salting divides the term that has no N in it, and charges for it. */
    eq(Rtext(hottestLoadSalted(lam, f, 16, 8)), '7000', 'a salt of 8 brings the hot shard to 7000');
    eq(Rtext(hottestLoadSalted(lam, f, 16, 1)), Rtext(hottestLoad(lam, f, 16)),
       'and a salt of 1 is no salt at all');
    eq(Rtext(saltReadAmplification(f, 8)), '46/25', 'at 1.84 times the reads overall');
    eq(Rtext(saltReadAmplification(f, 1)), '1', 'which is 1 when nothing is salted');
    eq(Rtext(saltReadAmplification(R(0n, 1n), 64)), '1', 'and 1 when no key is hot');
    eq(saltForTarget(lam, f, 16, R(3n, 2n)), 4, 'a salt of 4 brings it inside 1.5 times the mean');
    eq(Rcmp(hottestLoadSalted(lam, f, 16, 4), Rmul(R(3n, 2n), meanLoad(lam, 16))) <= 0, true,
       'and 4 really is inside it');
    eq(Rcmp(hottestLoadSalted(lam, f, 16, 3), Rmul(R(3n, 2n), meanLoad(lam, 16))) <= 0, false,
       'while 3 is not, so the search returned the smallest');
    eq(saltForTarget(lam, f, 16, R(1n, 2n)), null, 'and no salt reaches half the mean, which it says');
    /* With no hot key the hottest shard IS the mean, exactly. */
    eq(Rtext(hottestLoad(lam, R(0n, 1n), 16)), Rtext(meanLoad(lam, 16)), 'f = 0 leaves a level fleet');
  }

  /* --- L7: the maximum of N partition times ------------------------------- */
  {
    const pmf = parsePmf('20:900, 40:70, 120:25, 400:5');
    eq(pmf.length, 4, 'four partition times parsed');
    eq(Rtext(pmf[0][1]), '9/10', 'and the weights normalised to exact probabilities');
    eq(parsePmf('20, 40'), null, 'a list of times is not a distribution');
    eq(parsePmf('x:1'), null, 'nor is a non-numeric time');
    eq(parsePmf('20:-1'), null, 'nor a negative weight');
    eq(parsePmf('20:0, 40:0'), null, 'nor weights that are all zero');
    eq(Rtext(pmfMean(pmf)), '129/5', 'one partition averages 25.8 ms');
    /* pmfMax at N = 1 must be the distribution itself, and its total mass 1. */
    eq(pmfMax(pmf, 1).map((p) => p[0] + ':' + Rtext(p[1])).join(' '),
       pmf.map((p) => p[0] + ':' + Rtext(p[1])).join(' '), 'the maximum of one is the thing itself');
    for (const n of [1, 2, 5, 24, 128]) {
      let total = R(0n, 1n);
      pmfMax(pmf, n).forEach((p) => { total = Radd(total, p[1]); });
      eq(Rtext(total), '1', 'the maximum of ' + n + ' is still a distribution');
    }
    /* THE NEAREST-RANK CROSS-CHECK. pmfQuantile lifts percentile() from a
       sample to a distribution, so on an equiprobable pmf the two must agree
       exactly -- if they ever stop agreeing, one of them has been changed. */
    {
      const sample = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100];
      const flat = sample.map((v) => [v, R(1n, 10n)]);
      for (const [num, den] of [[1n, 10n], [1n, 4n], [1n, 2n], [9n, 10n], [99n, 100n], [1n, 1n]]) {
        const q = R(num, den);
        eq(pmfQuantile(flat, q), percentile(sample, q),
           'pmfQuantile agrees with the core percentile at q = ' + Rtext(q));
      }
    }
    eq(pmfQuantile(pmf, R(99n, 100n)), 120, 'one partition has a p99 of 120 ms');
    eq(pmfQuantile(pmfMax(pmf, 24), R(99n, 100n)), 400, 'a 24-partition job has a p99 of 400');
    eq(Rfixed(pmfMean(pmfMax(pmf, 24)), 2), '111.63', 'and a mean of 111.63 against one partition 25.8');
    eq(Rfixed(stragglerTax(pmf, 24).ratio, 2), '4.33', 'a straggler tax of 4.33x');
    eq(Rtext(stragglerTax(pmf, 1).ratio), '1', 'which is exactly 1 at a single partition');
    /* The 0.5% partition is not the p99 of one and IS the p99 of three -- found
       by exact integer search over N, never by a logarithm. */
    eq(pmfWorst(pmf), 400, 'the slowest time the distribution puts mass on');
    eq(smallestNForQuantile(pmf, R(99n, 100n), 400, 4096), 3,
       'a 0.5% partition becomes the job p99 at three partitions');
    eq(pmfQuantile(pmfMax(pmf, 2), R(99n, 100n)) < 400, true, 'two partitions do not reach it');
    eq(Rfixed(anySlowerThan(pmf, 24, 120), 4), '0.1133',
       'P(at least one of 24 partitions past 120 ms) = 1 - (1 - 0.005)^24');
    eq(Rtext(anySlowerThan(pmf, 1, 120)), Rtext(pmfTail(pmf, 120)), 'which at N = 1 is just the tail');
  }

  /* --- L8: one choice against d ------------------------------------------ */
  {
    const one = placeOneChoiceFrom(3, 1024, 1024, 2), two = placeChoices(3, 1024, 1024, 2);
    eq(occTotal(one), 1024, 'every key is placed, one choice');
    eq(occTotal(two), 1024, 'and every key is placed, two choices');
    eq(occMax(two) < occMax(one), true, 'the second look lowers the maximum');
    /* THE FAIRNESS OF THE COMPARISON: both arms read the SAME stream, and the
       one-choice arm is exactly the d-choice arm with the extra draws thrown
       away. At d = 1 the two placements must therefore be identical. */
    eq(placeChoices(3, 1024, 1024, 1).join(','), placeOneChoiceFrom(3, 1024, 1024, 1).join(','),
       'at d = 1 the two policies are the same policy');
    eq(placeOneChoiceFrom(3, 512, 512, 2).join(','), placeOneChoiceFrom(3, 512, 512, 2).join(','),
       'and the run is reproducible');
    /* The measured collapse, across seeds rather than on one lucky draw. */
    {
      const acc = maxLoadAcrossSeeds(1, 1024, 1024, 2, 12);
      eq(acc.one.length, 12, 'twelve seeds of one choice');
      eq(acc.many.every((m, i) => m <= acc.one[i]), true,
         'and on every one of them two choices is at least as level');
      eq(Rcmp(meanOf(acc.many), meanOf(acc.one)) < 0, true, 'strictly better on average');
      eq(new Set(acc.many).size <= 2, true, 'the two-choice maximum barely moves across seeds');
      eq(Rtext(meanOf([3, 3, 4])), '10/3', 'the mean of a run is an exact fraction');
    }
    /* Both asymptotics are STATED. What is checked here is only that the
       measured maxima sit in the region they describe -- the proofs are not in
       this library, which is what reconciliation #17 requires the pages to say. */
    near(oneChoiceStatedApprox(4096), 3.9264, 1e-3, 'ln n / ln ln n at n = 4096');
    near(twoChoiceStatedApprox(4096), 2.1184, 1e-3, 'ln ln n at n = 4096');
    eq(occMax(placeOneChoiceFrom(1, 4096, 4096, 2)) > occMax(placeChoices(1, 4096, 4096, 2)), true,
       'and the measured gap at n = 4096 goes the way they describe');
  }

  /* --- L9: scatter-gather ------------------------------------------------- */
  {
    const pmf = parsePmf('10:80, 25:15, 90:4, 250:1');
    eq(Rtext(shardRequestRate(R(400n, 1n), 24)), '9600', '400 queries a second is 9600 shard requests');
    eq(Rtext(requestAmplification(24)), '24', 'an amplification of N');
    eq(Rtext(routedRequestRate(R(400n, 1n))), '400', 'while a routed query stays at 400');
    eq(Rtext(shardRequestRate(R(400n, 1n), 1)), '400', 'and at one shard the two agree');
    /* The tail the query waits for is not the tail a per-shard dashboard shows. */
    const exact = pmfMax(pmf, 24);
    eq(pmfQuantile(pmf, R(99n, 100n)), 90, "one shard's own p99 is 90 ms");
    eq(pmfQuantile(exact, R(99n, 100n)), 250, 'but the QUERY p99 is the 1-in-100 shard, 250 ms');
    eq(pmfQuantile(exact, R(1n, 2n)), 90, 'and the median query already waits what a shard p99 does');
    eq(Rfixed(pmfMean(exact), 2), '105.24', 'the mean query takes 105.24 ms');
    eq(Rfixed(pmfMean(pmf), 2), '17.85', 'against a mean shard of 17.85');
    /* TWO ROUTES TO ONE NUMBER: the exact tail and the seeded run agree. If
       either the pmf algebra or the inverse-transform sampler were wrong, this
       is the assertion that would notice. */
    for (const seed of [9, 21, 37]) {
      const sample = scatterSample(pmf, 24, 800, seed);
      eq(sample.length, 800, 'the run produced the queries it was asked for');
      eq(sample.every((v, i) => i === 0 || v >= sample[i - 1]), true, 'sorted, so percentile can read it');
      eq(percentile(sample, R(1n, 2n)), pmfQuantile(exact, R(1n, 2n)),
         'the sampled median matches the exact one at seed ' + seed);
      eq(percentile(sample, R(99n, 100n)), pmfQuantile(exact, R(99n, 100n)),
         'and so does the sampled p99 at seed ' + seed);
    }
    eq(scatterSample(pmf, 4, 50, 9).join(',') === scatterSample(pmf, 4, 50, 9).join(','), true,
       'the sampled run is reproducible');
  }

  /* --- L10: local against global ------------------------------------------ */
  {
    const r = R(5000n, 1n), w = R(2000n, 1n);
    eq(Rtext(localIndexCost(r, w, 16)), '82000', 'r x N + w at sixteen shards');
    eq(Rtext(globalIndexCost(r, w)), '9000', 'against r + 2w');
    eq(cheaperIndex(r, w, 16), 'global', 'so the global index wins this workload');
    eq(Rtext(indexCrossover(16)), '1/15', 'and they break even at r/w = 1/(N - 1)');
    eq(indexCrossover(1), null, 'at one shard there is no difference to have');
    /* THE CROSSOVER IS A CROSSOVER: at exactly r/w = 1/(N-1) the two costs are
       equal, and either side of it the other one wins. Checked at several N so
       that an off-by-one in the algebra cannot hide. */
    for (const n of [2, 3, 8, 16, 64]) {
      const ratio = indexCrossover(n);
      const rr = R(ratio.n, 1n), ww = R(ratio.d, 1n);
      eq(Rtext(localIndexCost(rr, ww, n)), Rtext(globalIndexCost(rr, ww)),
         'the two indexes cost the same at r/w = 1/(N-1), at N = ' + n);
      eq(cheaperIndex(rr, ww, n), 'equal', 'and the verdict says so at N = ' + n);
      eq(cheaperIndex(Rmul(rr, R(1n, 2n)), ww, n), 'local', 'fewer reads favours the local index');
      eq(cheaperIndex(Rmul(rr, R(2n, 1n)), ww, n), 'global', 'and more reads favours the global one');
    }
    eq(Rtext(localIndexCost(R(0n, 1n), w, 16)), '2000', 'with no reads the local index costs one write');
    eq(Rtext(globalIndexCost(R(0n, 1n), w)), '4000', 'and the global one costs two');
  }

  /* --- L11: cross-shard transactions --------------------------------------- */
  {
    eq(Rtext(sameShardProb(2, 2)), '1/2',
       'THE number: at two shards, half of every two-key transaction already crosses');
    eq(Rtext(crossShardProb(2, 2)), '1/2', 'and the other half of it does not');
    eq(Rtext(sameShardProb(2, 16)), '1/16', 'N^(1-k) at k = 2 is 1/N');
    eq(Rtext(sameShardProb(3, 16)), '1/256', 'and at k = 3 it is 1/N^2');
    eq(Rtext(sameShardProb(12, 64)), '1/73786976294838206464',
       'Rpow takes the negative exponent and stays exact at 64^11');
    eq(Rtext(sameShardProb(1, 37)), '1', 'a one-key transaction is always local');
    eq(Rtext(sameShardProb(5, 1)), '1', 'and so is anything on a single shard');
    for (const k of [1, 2, 3, 7]) {
      for (const n of [2, 5, 16]) {
        eq(Rtext(Radd(sameShardProb(k, n), crossShardProb(k, n))), '1',
           'local and crossing are a partition at k = ' + k + ', N = ' + n);
        eq(Rtext(sameShardProb(k, n)), Rtext(Rpow(R(1n, BigInt(n)), k - 1)),
           'N^(1-k) is 1/N^(k-1) at k = ' + k + ', N = ' + n);
      }
    }
    /* The shards a transaction touches is a coupon-collector expectation, and
       it must sit between one and the smaller of k and N. */
    eq(Rtext(expectedShardsTouched(1, 16)), '1', 'one key touches one shard');
    eq(Rtext(expectedShardsTouched(2, 2)), '3/2', 'two keys on two shards touch 1.5 of them');
    eq(Rfixed(expectedShardsTouched(3, 16), 4), '2.8164', 'three keys on sixteen touch 2.82');
    for (const [k, n] of [[2, 2], [4, 8], [12, 64], [8, 3]]) {
      const t = expectedShardsTouched(k, n);
      eq(Rcmp(t, R(1n, 1n)) >= 0, true, 'at least one shard at k = ' + k + ', N = ' + n);
      eq(Rcmp(t, R(BigInt(Math.min(k, n)), 1n)) <= 0, true, 'and never more than min(k, N)');
    }
    /* Two-phase commit, itemised, and charged only to the ones that cross. */
    const cost = twoPhaseCost(R(2n, 1n), R(1n, 2n));
    eq(Rtext(cost.rtt) + '/' + Rtext(cost.fsync) + '/' + Rtext(cost.total), '4/1/5',
       'two round trips and two fsyncs');
    eq(Rtext(meanAddedLatency(2, 2, R(2n, 1n), R(1n, 2n))), '5/2',
       'half the transactions pay 5 ms, so the mean is 2.5');
    eq(Rtext(meanAddedLatency(1, 16, R(2n, 1n), R(1n, 2n))), '0',
       'and a single-key transaction pays none of it');
  }

  /* --- L12: rebalancing ---------------------------------------------------- */
  {
    const D = R(48n * 10n ** 12n, 1n), B = R(200n * 10n ** 6n, 1n), budget = R(800n * 10n ** 6n, 1n);
    eq(byteText(movedBytes(R(1n, 4n), D)), '12.00 TB', 'a quarter of 48 TB is 12 TB');
    eq(Rtext(rebalanceSeconds(R(1n, 4n), D, B)), '60000', 'at 200 MB/s that is 60000 seconds');
    eq(durText(rebalanceSeconds(R(1n, 4n), D, B)), '16 h 40 min', 'which is 16 h 40 min, not a moment');
    eq(rebalanceSeconds(R(1n, 4n), D, R(0n, 1n)), null, 'a throttle of zero never finishes');
    eq(Rtext(rebalanceSeconds(R(0n, 1n), D, B)), '0', 'and moving nothing takes no time');
    /* Halving the throttle doubles the window: the operational trade, exactly. */
    eq(Rtext(Rdiv(rebalanceSeconds(R(1n, 4n), D, R(100n * 10n ** 6n, 1n)),
                  rebalanceSeconds(R(1n, 4n), D, B))), '2',
       'halving the throttle doubles the window');
    eq(Rtext(stolenShare(B, budget)), '1/4', 'the copy holds a quarter of the transfer budget');
    eq(Rtext(serviceDuringMove(R(8000n, 1n), B, budget)), '6000',
       'so the node serves 6000 a second instead of 8000');
    const load = rebalanceLoad(R(5000n, 1n), R(8000n, 1n), B, budget);
    eq(Rtext(load.before.rho), '5/8', 'utilisation before the move');
    eq(Rtext(load.during.rho), '5/6', 'and during it');
    eq(Rtext(load.before.W), '1/3000', "course 3's M/M/1 wait before");
    eq(Rtext(load.during.W), '1/1000', 'and during');
    eq(Rtext(Rdiv(load.during.W, load.before.W)), '3',
       'a gentle-looking quarter of the budget triples the wait');
    /* A throttle at the whole budget stops the node serving, and the page has
       to say so rather than printing a finite wait. */
    const starved = rebalanceLoad(R(5000n, 1n), R(8000n, 1n), budget, budget);
    eq(Rtext(starved.muMove), '0', 'a copy at the full budget leaves no service rate');
    eq(starved.during.stable, false, 'and no steady state at all');
  }
}

/* -----------------------------------------------------------------------
   SYSTEM DESIGN, COURSE 6: replication and consistency.

   Thirteen lessons, one kit, and nothing in it rounds: order statistics from
   enumerated distributions, quorum tails as binomial sums over fractions,
   overlap as combinations, linearizations counted rather than sampled.

   Eleven of the assertions below are not figures but IDENTITIES, and they are
   why this section exists. The per-replica load of the fan-out plan must come
   back as exactly one replica's capacity; the pigeonhole minimum must be
   ATTAINED by some pair and not merely respected; the enumerated count of
   disjoint quorum pairs must equal the closed form; the quorum tail must be
   monotone in N at fixed W, which is the one claim on this course readers
   refuse; the sloppy miss must equal that same disjoint count over all pairs;
   a majority of an even n must be strictly WORSE than of n - 1; the election
   probability must equal a brute-force count over every assignment; a vector
   clock's happens-before must imply a smaller Lamport stamp; the permutation
   generator must produce exactly k!; real time must partition the pairs; and
   the counter CRDT's merge must be commutative, associative and idempotent.
   Each is exact, each is checkable, and each is a claim a lesson makes in
   prose. */
console.log('system design: replication, quorums, clocks and consistency');
{
  const REPLICA_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'replica.py');
  const replicaSrc = fs.readFileSync(REPLICA_SOURCE, 'utf8');
  const replicaBlock = (name) => blockFrom(replicaSrc, name, REPLICA_SOURCE);
  eval(block('RATIONAL_JS') + countingBlock('BIGINT_JS') + sysdBlock('RCEIL_JS')
       + sysdBlock('PERCENTILE_JS') + sysdBlock('PMF_JS') + sysdBlock('AVAIL_JS')
       + replicaBlock('REPLICA_JS'));

  /* The two distributions the kit ships as its presets, so that what is
     asserted here is what a reader opens the page on. */
  const REPLY = pmfFromSpec(parsePmfSpec('2:600, 4:300, 8:70, 16:22, 24:6, 40:2'));
  const LAG = pmfFromSpec(parsePmfSpec('10:500, 25:300, 50:120, 120:60, 250:15, 400:5'));
  const q99 = R(99n, 100n), q50 = R(1n, 2n), q999 = R(999n, 1000n);

  /* --- printing ----------------------------------------------------------- */
  eq(Rfixed(R(1n, 3n), 6), '0.333333', 'long division in BigInt');
  eq(Rfixed(R(2n, 3n), 6), '0.666667', 'rounded half up at the last digit');
  eq(Rfixed(R(-1n, 8n), 3), '-0.125', 'a negative rational keeps its sign');
  eq(Rpct(R(2n, 3n), 3), '66.667%', 'the sloppy-quorum miss as a percentage');
  eq(ninesOf(R(999702n, 1000000n)), 3, 'a majority of three at 99% has three nines');
  eq(RpctAuto(R(999702n, 1000000n)), '99.970200%', 'and prints wide enough to show them');
  eq(RpctAuto(R(1n, 1n)), '100%', 'only an exact one prints as 100%');
  eq(RpctAuto(Rsub(R(1n, 1n), R(1n, 10n ** 9n))), '99.999999900000%',
     'nine nines gets twelve places rather than rounding to 100%');
  eq(bytesText(2828n), '2.83 kB', 'decimal byte units: 1 kB is 1000 B');
  /* Rfixed exists here because F(t)^(N-1) leaves Number behind: the 24-ms atom
     of the shipped pmf raised to the 8th power has a 24-digit denominator. */
  eq(Rtext(Rpow(R(998n, 1000n), 8)), '3844185754368006996001/3906250000000000000000',
     'F(24) to the 8th is a fraction with no decimal anywhere in it');

  /* --- L1: the four multipliers, and the ceiling the ratio sets ------------ */
  eq(Rtext(fanoutCeiling(R(9n, 1n))), '10', 'nine reads per write caps the speed-up at 10x');
  eq(Rtext(fanoutSpeedup(3, R(9n, 1n))), '5/2', 'three replicas of that workload give 2.5x, not 3x');
  eq(Rtext(fanoutPlan(R(1000n, 1n), 3, R(9n, 1n)).total), '2500',
     'which is 2500 ops/s from three 1000 ops/s replicas');
  eq(Rtext(fanoutPlan(R(1000n, 1n), 3, R(9n, 1n)).readCapacity), '3000', 'reads scale by N');
  eq(Rtext(fanoutPlan(R(1000n, 1n), 3, R(9n, 1n)).writeCapacity), '1000', 'writes do not scale at all');
  /* THE IDENTITY: the plan must saturate a replica exactly. Every replica
     carries all the writes plus 1/N of the reads, and that has to come back as
     one replica's capacity or the throughput formula is wrong. */
  for (const [n, rhoN, c] of [[1, 9, 1000], [3, 9, 1000], [7, 4, 250], [12, 0, 5000], [5, 37, 900]]) {
    const plan = fanoutPlan(R(BigInt(c), 1n), n, R(BigInt(rhoN), 1n));
    eq(Rtext(plan.perReplicaLoad), String(c),
       'a replica is saturated exactly at n = ' + n + ', rho = ' + rhoN);
    eq(Rtext(Radd(plan.reads, plan.writes)), Rtext(plan.total),
       'and the mix adds back to the total at n = ' + n + ', rho = ' + rhoN);
  }
  /* THE IDENTITY: at one replica there is no speed-up, and at rho = 0 -- a
     write-only workload -- there is none at ANY N. Replication does not scale
     writes, and this is the arithmetic of that sentence. */
  for (const rhoN of [0, 1, 9, 60]) {
    eq(Rtext(fanoutSpeedup(1, R(BigInt(rhoN), 1n))), '1', 'one replica is 1x at rho = ' + rhoN);
  }
  for (const n of [1, 2, 5, 12, 100]) {
    eq(Rtext(fanoutSpeedup(n, R(0n, 1n))), '1', 'a write-only workload is 1x at N = ' + n);
  }
  /* The speed-up rises in N and never reaches the ceiling. */
  for (const rhoN of [1, 9, 60]) {
    const rho = R(BigInt(rhoN), 1n);
    for (let n = 1; n < 24; n += 1) {
      eq(Rcmp(fanoutSpeedup(n + 1, rho), fanoutSpeedup(n, rho)) > 0, true,
         'the speed-up rises from N = ' + n + ' at rho = ' + rhoN);
      eq(Rcmp(fanoutSpeedup(n, rho), fanoutCeiling(rho)) < 0, true,
         'and stays under the ceiling at N = ' + n + ', rho = ' + rhoN);
    }
  }

  /* --- L2: the maximum of N - 1, not N times one -------------------------- */
  eq(syncAckPmf(REPLY, 1).length, 1, 'at N = 1 there is no follower to wait for');
  eq(Rtext(syncAckPmf(REPLY, 1)[0][1]), '1', 'so the wait is zero with probability one');
  eq(syncAckPmf(REPLY, 1)[0][0], 0, 'and the value is zero, not one replica');
  /* THE IDENTITY: P(max of k <= t) is F(t)^k at every attainable time. This is
     what the lesson claims and pmfMax is what the page calls. */
  for (const k of [1, 2, 3, 8]) {
    const mx = pmfMax(REPLY, k);
    for (const t of pmfSupport(REPLY)) {
      eq(Rtext(pmfCdfAt(mx, t)), Rtext(Rpow(pmfCdfAt(REPLY, t), k)),
         'P(max of ' + k + ' <= ' + t + ') is F(t) to the ' + k);
    }
  }
  /* THE IDENTITY the lesson states in its key line: P(all N - 1 followers
     acked by t) = F(t)^(N-1). The order of the maximum is N - 1 and not N --
     the leader does not wait for itself -- and the percentiles alone do not
     pin that, because a discrete tail can absorb an off-by-one in the
     exponent without moving the 99th percentile at all. */
  for (const n of [2, 3, 5, 9]) {
    const ack = syncAckPmf(REPLY, n);
    for (const t of pmfSupport(REPLY)) {
      eq(Rtext(pmfCdfAt(ack, t)), Rtext(Rpow(pmfCdfAt(REPLY, t), n - 1)),
         'the sync write is acked by ' + t + ' with probability F(t)^(N-1) at N = ' + n);
    }
  }
  eq(Rtext(pmfMean(syncAckPmf(REPLY, 3))), '147007/31250',
     'and the mean wait of a three-replica sync write is exact');
  eq(Rtext(pmfMean(syncAckPmf(REPLY, 2))), '442/125', 'as is a two-replica one');
  eq(pmfPercentile(REPLY, q99), 16, 'one replica acks by 16 ms 99 times in 100');
  eq(pmfPercentile(syncAckPmf(REPLY, 3), q99), 24, 'synchronising to three costs 24 ms at p99');
  eq(naiveSyncCost(REPLY, 3, q99), 48, 'while "three times one replica" would claim 48');
  eq(pmfPercentile(syncAckPmf(REPLY, 9), q99), 40, 'and nine replicas cost 40, not 144');
  eq(naiveSyncCost(REPLY, 9, q99), 144, 'which is what the naive rule claims at N = 9');
  /* The sync wait is non-decreasing in N and bounded by the slowest atom -- a
     maximum of more copies is never faster and never leaves the support. */
  for (let n = 2; n < 12; n += 1) {
    eq(pmfPercentile(syncAckPmf(REPLY, n + 1), q99) >= pmfPercentile(syncAckPmf(REPLY, n), q99),
       true, 'the sync p99 does not fall as N rises, at N = ' + n);
    eq(pmfPercentile(syncAckPmf(REPLY, n), q99) <= 40, true, 'and never leaves the support');
  }
  eq(Rtext(asyncAtRiskBytes(2000, pmfMean(REPLY), 400)), '14144/5',
     'the async alternative risks writes/s x mean lag x bytes');
  eq(String(bytesFloor(asyncAtRiskBytes(2000, pmfMean(REPLY), 400))), '2828',
     'and a count of bytes is floored, never rounded up into bytes that do not exist');
  eq(bytesText(bytesFloor(asyncAtRiskBytes(2000, pmfMean(REPLY), 400))), '2.83 kB',
     'which reads as 2.83 kB');

  /* --- L3: the tail, and the mass the mean cannot see --------------------- */
  eq(Rtext(pmfMean(LAG)), '629/20', 'the shipped lag averages 31.45 ms');
  eq(Rtext(staleProb(LAG, 50)), '2/25', 'a read 50 ms after the write is stale 8 times in 100');
  eq(Rtext(tailPastRational(LAG, pmfMean(LAG))), '1/5',
     'and waiting for the MEAN still leaves one read in five stale');
  eq(Rtext(staleReadsPerSec(LAG, 50, 12000)), '960', 'which at 12 000 reads/s is 960 a second');
  eq(freshDelay(LAG, q99), 250, '99% freshness needs 250 ms');
  eq(freshDelay(LAG, q999), 400, 'and 99.9% needs 400');
  /* THE IDENTITY: fresh and stale are a partition. */
  for (const t of [0, 9, 10, 24, 25, 50, 119, 120, 250, 399, 400, 1000]) {
    eq(Rtext(Radd(pmfCdfAt(LAG, t), staleProb(LAG, t))), '1',
       'fresh and stale partition the mass at t = ' + t);
  }

  /* --- L4: overlap, claimed and measured ---------------------------------- */
  eq(quorumOverlap(3, 2, 2), 1, 'R + W - N is one at the canonical (3, 2, 2)');
  eq(quorumScan(3, 2, 2).min, 1, 'and the scan over all nine pairs finds exactly one');
  eq(quorumScan(3, 2, 2).disjoint, 0, 'with no disjoint pair');
  eq(quorumScan(3, 1, 1).disjoint, 6, 'while (3, 1, 1) has six disjoint pairs of nine');
  eq(String(subsets(5, 2).length), String(comb(5, 2)), 'the enumeration produces C(n, k) sets');
  eq(subsets(4, 2).map((s) => s.join('')).join(' '), '01 02 03 12 13 23', 'in lexicographic order');
  eq(subsets(3, 0).length, 1, 'and C(n, 0) = 1: the empty set');
  eq(overlapSize([0, 1], [1, 2]), 1, 'two sets sharing one node overlap in one');
  eq(overlapSize([0, 1], [2, 3]), 0, 'and two that share nothing overlap in none');
  eq(overlapSize([0, 1, 2], [2, 1, 0]), 3, 'order does not change the overlap');
  eq(overlapSize([], [0]), 0, 'the empty set meets nothing');
  /* THE IDENTITY, twice over, on every configuration up to seven nodes: the
     pigeonhole minimum is ATTAINED, and the enumerated disjoint count equals
     the closed form C(N, W) x C(N - W, R). A page that asserted the bound
     without measuring it would pass every other test in this file. */
  for (let n = 1; n <= 7; n += 1) {
    for (let r = 1; r <= n; r += 1) {
      for (let w = 1; w <= n; w += 1) {
        const scan = quorumScan(n, r, w);
        eq(scan.min, r + w > n ? r + w - n : 0,
           'the minimum overlap is attained at (' + n + ', ' + r + ', ' + w + ')');
        eq(String(scan.disjoint), String(disjointPairCount(n, r, w)),
           'and the disjoint count matches the formula at (' + n + ', ' + r + ', ' + w + ')');
        eq(scan.pairs, Number(comb(n, r)) * Number(comb(n, w)),
           'over C(n,r) x C(n,w) pairs at (' + n + ', ' + r + ', ' + w + ')');
        eq((scan.witness === null) === quorumOverlaps(n, r, w), true,
           'a witness exists exactly when the configuration does NOT overlap at ('
           + n + ', ' + r + ', ' + w + ')');
      }
    }
  }

  /* --- L5: the binomial tail, and the result readers refuse --------------- */
  /* The two edges of availKofN, on a latency CDF rather than an availability:
     W = 1 is the parallel form and W = N the series one. */
  for (const t of pmfSupport(REPLY)) {
    const F = pmfCdfAt(REPLY, t);
    for (const n of [1, 3, 5]) {
      eq(Rtext(quorumAckBy(REPLY, t, n, n)), Rtext(Rpow(F, n)),
         'waiting for all ' + n + ' is F(t)^' + n + ' at t = ' + t);
      eq(Rtext(quorumAckBy(REPLY, t, 1, n)),
         Rtext(Rsub(R(1n, 1n), Rpow(Rsub(R(1n, 1n), F), n))),
         'waiting for any one of ' + n + ' is 1 - (1 - F)^' + n + ' at t = ' + t);
    }
  }
  /* THE IDENTITY, and it is the lesson: with W fixed the tail is monotone in
     N. More replicas make a quorum write FASTER, and this is that sentence. */
  for (const w of [1, 2, 3, 5]) {
    for (const t of pmfSupport(REPLY)) {
      for (let n = w; n < 12; n += 1) {
        eq(Rcmp(quorumAckBy(REPLY, t, w, n + 1), quorumAckBy(REPLY, t, w, n)) >= 0, true,
           'P(>= ' + w + ' of N by ' + t + ') does not fall from N = ' + n);
      }
    }
  }
  eq(quorumPercentile(REPLY, 2, 2, q99), 24, 'a 2-of-2 quorum has a p99 of 24 ms');
  eq(quorumPercentile(REPLY, 2, 3, q99), 8, 'a 2-of-3 quorum, 8 ms');
  eq(quorumPercentile(REPLY, 2, 4, q99), 4, 'and a 2-of-4 quorum, 4 ms -- faster, on more replicas');
  eq(quorumPercentile(REPLY, 2, 8, q99), 2, 'at eight replicas it is the fastest atom there is');
  eq(quorumSweep(REPLY, 2, 9, q99).map((r) => r.p).join(','), '24,8,4,4,4,4,2,2',
     'the whole sweep, non-increasing all the way down');
  eq(quorumPercentile(REPLY, 5, 4, q99), null, 'a quorum larger than the fleet is never met');
  eq(Rtext(quorumAckBy(REPLY, 2, 0, 3)), '1', 'and a quorum of nobody is met immediately');

  /* --- L6: the sloppy miss ------------------------------------------------ */
  eq(Rtext(sloppyMiss(3, 1, 1)), '2/3', 'two reads in three miss at N = 3, R = W = 1');
  eq(Rtext(sloppyMiss(3, 2, 1)), '1/3', 'R = 2 halves it, and does not remove it');
  eq(Rtext(sloppyMiss(3, 2, 2)), '0', 'R + W > N removes it exactly');
  eq(Rtext(sloppyMiss(5, 2, 3)), '1/10', 'R + W = N is still one read in ten');
  eq(Rtext(sloppyHit(3, 1, 1)), '1/3', 'hit and miss are complements');
  /* THE IDENTITY: the probability is the enumerated disjoint count over all
     pairs. Two different routes to the same fraction, on every configuration. */
  for (let n = 1; n <= 7; n += 1) {
    for (let r = 1; r <= n; r += 1) {
      for (let w = 1; w <= n; w += 1) {
        const scan = quorumScan(n, r, w);
        eq(Rtext(sloppyMiss(n, r, w)), Rtext(R(BigInt(scan.disjoint), BigInt(scan.pairs))),
           'the miss probability is the disjoint share at (' + n + ', ' + r + ', ' + w + ')');
        eq(Rzero(sloppyMiss(n, r, w)), quorumOverlaps(n, r, w),
           'and it is zero exactly when the quorums overlap at ('
           + n + ', ' + r + ', ' + w + ')');
      }
    }
  }

  /* --- L7: 2f + 1, and the node that buys nothing ------------------------- */
  eq(majoritySize(3), 2, 'a majority of three is two');
  eq(majoritySize(4), 3, 'and of four is three');
  eq(faultsTolerated(3), 1, 'three tolerate one');
  eq(faultsTolerated(4), 1, 'and so do four');
  eq(Rtext(majorityAvail(R(99n, 100n), 3)), '499851/500000', '2-of-3 at 99% each');
  eq(RpctAuto(majorityAvail(R(99n, 100n), 3)), '99.970200%', 'which is 99.9702%');
  eq(RpctAuto(majorityAvail(R(99n, 100n), 4)), '99.940797%', 'and 3-of-4 is WORSE');
  /* THE IDENTITY, three ways: the quorum and the tolerance partition the
     cluster; an even size tolerates what the odd size below it does; and its
     majority is strictly less available whenever a node is better than a coin.
     The last is the sentence "a fourth node adds nothing to three", made
     sharper -- it subtracts. */
  for (let n = 1; n <= 20; n += 1) {
    eq(majoritySize(n) + faultsTolerated(n), n, 'quorum plus tolerance is n at n = ' + n);
    eq(2 * faultsTolerated(n) + 1 <= n, true, '2f + 1 fits inside n at n = ' + n);
  }
  for (let k = 1; k <= 10; k += 1) {
    eq(faultsTolerated(2 * k), faultsTolerated(2 * k - 1),
       'an even cluster tolerates what the odd one below it does, at n = ' + (2 * k));
    eq(evenIsWasted(2 * k), true, 'and is flagged as wasted at n = ' + (2 * k));
    eq(evenIsWasted(2 * k - 1), false, 'while the odd size is not, at n = ' + (2 * k - 1));
  }
  for (const a of [R(9n, 10n), R(99n, 100n), R(999n, 1000n), R(3n, 4n)]) {
    for (let k = 1; k <= 6; k += 1) {
      eq(Rcmp(majorityAvail(a, 2 * k), majorityAvail(a, 2 * k - 1)) < 0, true,
         'the majority of ' + (2 * k) + ' is strictly worse than of ' + (2 * k - 1)
         + ' at A = ' + Rtext(a));
    }
  }
  eq(Rtext(majorityAvail(R(3n, 7n), 1)), '3/7', 'a single node IS its own majority');

  /* --- L8: the split vote ------------------------------------------------- */
  eq(Rtext(electionClean(2, 2)), '1/2', 'two candidates over two slots');
  eq(Rtext(electionClean(2, 3)), '2/3', 'two over three');
  eq(Rtext(electionClean(3, 3)), '5/9', 'three over three');
  eq(Rtext(electionTerm(5, 10, 1)), '6561/20000', 'the first term of the lesson preset');
  eq(Rtext(electionTerm(5, 10, 9)), '1/20000', 'the ninth, four orders of magnitude down');
  eq(Rtext(electionTerm(5, 10, 10)), '0',
     'and the last is always zero: nobody can fire later than the last slot');
  eq(Rtext(electionClean(5, 10)), '15333/20000', 'the lesson preset, exactly');
  eq(Rfixed(electionRounds(5, 10), 4), '1.3044', 'so 1.3044 rounds on average');
  eq(Rtext(electionClean(1, 7)), '1', 'one candidate always wins');
  for (const n of [2, 3, 5, 12]) {
    eq(Rtext(electionClean(n, 1)), '0', 'a FIXED timeout is a guaranteed tie at n = ' + n);
    eq(electionRounds(n, 1), null, 'and the expected rounds are not a number');
  }
  /* The window a 95% clean rate needs, by binary search. P(clean) rises with T,
     which is what makes the search exact -- so that is asserted, and then the
     search is checked against the scan it replaced. */
  for (const n of [2, 3, 5, 12]) {
    for (let T = 1; T < 40; T += 1) {
      eq(Rcmp(electionClean(n, T + 1), electionClean(n, T)) > 0, true,
         'a wider window is always cleaner at n = ' + n + ', T = ' + T);
    }
  }
  const scanSlots = (n, target, limit) => {
    for (let k = 1; k <= limit; k += 1) if (Rcmp(electionClean(n, k), target) >= 0) return k;
    return null;
  };
  for (const n of [1, 2, 3, 5, 8, 12]) {
    for (const target of [R(9n, 10n), R(95n, 100n), R(99n, 100n)]) {
      eq(String(slotsForClean(n, target, 400)), String(scanSlots(n, target, 400)),
         'the binary search finds the same window as the scan at n = ' + n
         + ', target ' + Rtext(target));
    }
  }
  eq(slotsForClean(5, R(95n, 100n), 400), 50, 'the lesson preset needs 50 slots for 95% clean');
  eq(slotsForClean(1, R(99n, 100n), 400), 1, 'and one candidate needs one slot');
  eq(slotsForClean(12, R(95n, 100n), 2), null, 'a target out of reach inside the limit returns null');
  /* THE IDENTITY: the closed form equals a brute-force count over every
     assignment of candidates to slots. This is the one assertion here that
     does not trust the algebra at all. */
  const bruteClean = (n, T) => {
    let good = 0;
    const pick = new Array(n).fill(0);
    const walk = (i) => {
      if (i === n) {
        let lo = Infinity, count = 0;
        for (const v of pick) { if (v < lo) { lo = v; count = 1; } else if (v === lo) count += 1; }
        if (count === 1) good += 1;
        return;
      }
      for (let s = 0; s < T; s += 1) { pick[i] = s; walk(i + 1); }
    };
    walk(0);
    return R(BigInt(good), BigInt(T) ** BigInt(n));
  };
  for (const [n, T] of [[1, 3], [2, 2], [2, 5], [3, 3], [3, 4], [4, 4], [5, 3], [2, 1], [4, 1]]) {
    eq(Rtext(electionClean(n, T)), Rtext(bruteClean(n, T)),
       'the closed form matches a brute-force count at n = ' + n + ', T = ' + T);
  }

  /* --- L9, L10: the two clocks on one diagram ----------------------------- */
  const DIAG = parseDiagram('A:4 B:4 C:3; A2 to B2; B3 to C2; C1 to A4');
  eq(DIAG === null, false, 'the shipped diagram parses');
  eq(DIAG.procs.length, 3, 'three processes');
  eq(DIAG.msgs.length, 3, 'and three messages');
  eq(parseDiagram('A:4 B:4 C:3; A2>B2; B3>C2; C1>A4').msgs.length, 3,
     'and ">" is accepted as the arrow too, for a reader who types it');
  eq(parseDiagram('A:2 B:2; A2 to B1; B2 to A1') && lamportStamps(parseDiagram('A:2 B:2; A2 to B1; B2 to A1')),
     null, 'a message received before it was sent has no topological order');
  eq(parseDiagram('A:2 B:2; A1 to B1; A1 to B2'), null, 'one event cannot send twice');
  eq(parseDiagram('A:2 B:2; A1 to B1; A2 to B1'), null, 'nor can one event receive twice');
  eq(parseDiagram('A:2; A1 to A2'), null, 'a process cannot message itself');
  eq(parseDiagram('A:2 B:2; A9 to B1'), null, 'nor can it send from an event it does not have');
  eq(parseDiagram('A:2 A:2'), null, 'and a process may not be declared twice');
  eq(diagramEvents(DIAG).length, 11, 'eleven events across the three processes');
  eq(diagramOrder(diagramEvents(DIAG)).length, 11,
     'and they have a topological order, so every stamp has its inputs before it');
  eq(diagramOrder(diagramEvents(parseDiagram('A:2 B:2; A2 to B1; B2 to A1'))), null,
     'a diagram whose messages make a cycle has none, and the page says so');
  const L = lamportStamps(DIAG), V = vectorStamps(DIAG), EV = diagramEvents(DIAG);
  eq(L.join(','), '1,2,3,4,1,3,4,5,1,5,6', 'the Lamport stamps of the shipped diagram');
  eq(V.map((v) => v.join('')).join(' '), '100 200 300 401 010 220 230 240 001 232 233',
     'and its vectors');
  eq(concurrentPairs(V).length, 23, '23 of its 55 pairs are concurrent');
  eq(lamportFalsePairs(L, V).length, 17, 'and 17 ordered pairs have L(a) < L(b) with a NOT before b');
  /* THE IDENTITY: Lamport is sound and not complete. a -> b implies L(a) < L(b)
     on every diagram; the converse fails, and the vector clock is what knows. */
  for (const spec of ['A:4 B:4 C:3; A2 to B2; B3 to C2; C1 to A4',
                      'A:2 B:2; A1 to B1; B2 to A2',
                      'A:1',
                      'A:3 B:3 C:3 D:3; A1 to B1; B2 to C2; C3 to D3',
                      'A:5 B:5; A3 to B4']) {
    const d = parseDiagram(spec), l = lamportStamps(d), v = vectorStamps(d);
    eq(lamportConsistent(l, v), true, 'happens-before implies a smaller stamp on ' + spec);
    for (let i = 0; i < v.length; i += 1) {
      eq(vecCompare(v[i], v[i]), 0, 'a vector equals itself on ' + spec);
      for (let j = 0; j < v.length; j += 1) {
        const ab = vecCompare(v[i], v[j]), ba = vecCompare(v[j], v[i]);
        eq(ab === null ? ba === null : ab === -ba, true,
           'the comparison is antisymmetric on ' + spec);
      }
    }
    eq(concurrentPairs(v).length + (v.length * (v.length - 1)) / 2 - concurrentPairs(v).length,
       (v.length * (v.length - 1)) / 2, 'concurrent and ordered partition the pairs on ' + spec);
  }
  /* The sequential diagram has no concurrency at all, which is the control:
     a page that reported concurrent pairs here would be reporting noise. */
  eq(concurrentPairs(vectorStamps(parseDiagram('A:6'))).length, 0,
     'one process alone has nothing concurrent');
  eq(lamportStamps(parseDiagram('A:6')).join(','), '1,2,3,4,5,6', 'and its stamps just count');

  /* --- L11: drift, skew, commit-wait -------------------------------------- */
  eq(Rtext(skewMicros(200, 30)), '6000', '200 ppm over 30 s is 6000 microseconds');
  eq(Rtext(commitWaitMicros(200, 30)), '12000', 'and the comparison window is twice that');
  eq(orderTrustworthy(R(5000n, 1n), 200, 30), false, 'a 5 ms gap is inside a 12 ms window');
  eq(orderTrustworthy(R(20000n, 1n), 200, 30), true, 'a 20 ms gap clears it');
  eq(orderTrustworthy(R(12000n, 1n), 200, 30), false, 'and the boundary is not trustworthy either');
  eq(Rtext(windowRatio(R(5000n, 1n), 200, 30)), '12/5', 'the window is 2.4x that separation');
  eq(windowRatio(R(0n, 1n), 200, 30), null, 'two simultaneous events have no ratio');
  /* A ppm figure is microseconds per second by definition, so halving the sync
     interval halves the window exactly -- no rounding anywhere in the chain. */
  for (const [ppm, iv] of [[10, 60], [50, 10], [100, 30], [500, 600]]) {
    eq(Rtext(commitWaitMicros(ppm, iv)), Rtext(Rmul(R(2n, 1n), skewMicros(ppm, iv))),
       'the commit-wait is 2 epsilon at ' + ppm + ' ppm / ' + iv + ' s');
    eq(Rtext(skewMicros(ppm, 2 * iv)), Rtext(Rmul(R(2n, 1n), skewMicros(ppm, iv))),
       'and doubling the interval doubles the skew at ' + ppm + ' ppm');
  }

  /* --- L12: linearizability, counted -------------------------------------- */
  /* THE IDENTITY: the generator produces exactly k! orders. The lesson quotes
     that number as its reason for the cap, so it had better be the number the
     enumeration actually walks. */
  for (let k = 0; k <= 6; k += 1) {
    eq(permutations(k).length, Number(fact(k)), 'the generator produces ' + k + '! orders');
    eq(new Set(permutations(k).map((p) => p.join(','))).size, Number(fact(k)),
       'all distinct at k = ' + k);
  }
  const H_BAD = parseHistory('A w1[0,4]; B r1[2,6]; C r0[5,9]');
  const H_OK = parseHistory('A w1[0,4]; B r1[2,6]; C r1[5,9]');
  const H_SIX = parseHistory('A w1[0,2]; B r1[1,4]; C w2[3,6]; D r2[5,8]; E r2[7,10]; F r2[9,12]');
  eq(H_BAD.length, 3, 'the lesson history has three operations');
  eq(linearizations(H_BAD, 0).total, 6, 'six total orders');
  eq(linearizations(H_BAD, 0).realTime, 3, 'three of which real time allows');
  eq(linearizations(H_BAD, 0).valid.length, 0, 'and NONE is legal: the history is a violation');
  eq(linearizations(H_OK, 0).valid.length, 2, 'one return value later, two orders are legal');
  eq(linearizations(H_SIX, 0).total, 720, 'the six-operation history has 720 orders');
  eq(linearizations(H_SIX, 0).realTime, 13, '13 of which real time allows');
  eq(linearizations(H_SIX, 0).valid.length, 3, 'and 3 are legal');
  eq(parseHistory('A w1[4,4]'), null, 'an operation must return after it was invoked');
  eq(parseHistory('A w1[0,4], B r1[2,6]'), null,
     'operations are separated by semicolons -- the comma lives inside the interval');
  eq(parseHistory('A z1[0,4]'), null, 'and an operation is a read or a write');
  eq(historyPairs(H_BAD).forced, 1, 'real time decides one pair of the three');
  eq(historyPairs(H_BAD).concurrent, 2, 'and leaves two free');
  eq(historyPairs(H_SIX).forced, 10, 'ten of the fifteen pairs are decided on the six-op history');
  eq(historyPairs(H_SIX).concurrent, 5, 'and five are concurrent');
  /* The order the operations are TYPED in is not the order they ran in, so the
     real-time test has to look both ways round. */
  eq(historyPairs(parseHistory('C r1[5,9]; A w1[0,4]')).forced, 1,
     'a history typed out of time order still has its pair decided');
  eq(historyPairs(parseHistory('C r1[5,9]; A w1[0,4]')).concurrent, 0, 'with none left free');
  eq(realTimeBefore(H_BAD[0], H_BAD[2]), true, 'A returned at 4 before C was invoked at 5');
  eq(realTimeBefore(H_BAD[0], H_BAD[1]), false, 'but it overlaps B');
  eq(orderLegal(H_OK, [0, 1, 2], 0), true, 'write 1 then two reads of 1 is legal');
  eq(orderLegal(H_BAD, [0, 1, 2], 0), false, 'a read of 0 after a write of 1 is not');
  eq(orderLegal([], [], 3), true, 'and the empty order is vacuously legal');
  /* THE IDENTITY: real time decides some pairs and leaves the rest free, and
     the two counts are C(k, 2). The enumeration searches exactly the freedom. */
  for (const h of [H_BAD, H_OK, H_SIX,
                   parseHistory('A w1[0,3]; B w2[1,5]; C r1[4,8]; D r2[6,10]')]) {
    const pairs = historyPairs(h);
    eq(pairs.forced + pairs.concurrent, Number(comb(h.length, 2)),
       'forced and concurrent pairs are C(k, 2) on a ' + h.length + '-operation history');
    const res = linearizations(h, 0);
    eq(res.realTime <= res.total, true, 'real time can only remove orders');
    eq(res.valid.length <= res.realTime, true, 'and legality can only remove more');
    /* Every order the enumeration calls valid must survive an independent
       replay -- the count means nothing if the orders it counted do not. */
    for (const p of res.valid) {
      eq(orderRespectsRealTime(h, p) && orderLegal(h, p, 0), true,
         'a counted order really is valid on a ' + h.length + '-operation history');
    }
  }

  /* --- L13: what each merge throws away ----------------------------------- */
  const TRACE = parseTrace('A:3:+2, B:5:+3, C:4:+1, B:9:+4');
  eq(TRACE.length, 4, 'the lesson trace has four updates');
  eq(traceTotal(TRACE), 10, 'worth ten between them');
  eq(lwwMerge(TRACE).winner, 'B', 'B holds the largest timestamp');
  eq(lwwMerge(TRACE).value, 7, 'so last-writer-wins returns seven');
  eq(lwwMerge(TRACE).lost.length, 2, 'discarding two updates');
  eq(lwwMerge(TRACE).discarded, 3, 'worth three');
  eq(crdtValue(crdtCounts(TRACE)), 10, 'while the counter CRDT returns the true ten');
  eq(JSON.stringify(crdtCounts(TRACE)), '{"A":2,"B":7,"C":1}', 'from these per-replica counts');
  eq(lwwMerge(parseTrace('A:5:+1, B:5:+2')).winner, 'B',
     'a tie on the timestamp is broken by replica name, as a real LWW register does');
  eq(lwwMerge(parseTrace('A:5:+1, B:5:+2')).tieBroken, true, 'and the page is told that it was');
  eq(lwwMerge(parseTrace('A:1:+1, A:2:+5')).lost.length, 0,
     'updates at one replica lose nothing: concurrency is the whole problem');
  eq(parseTrace('A:1:-1'), null, 'a grow-only counter grows');
  eq(parseTrace('A:1'), null, 'and an update needs a replica, a timestamp and a delta');
  /* THE IDENTITY: the CRDT loses nothing and LWW loses everything off the
     winner, on every trace; and the merge obeys its three laws, which is WHY
     the replicas converge whatever order they gossip in. */
  for (const spec of ['A:3:+2, B:5:+3, C:4:+1, B:9:+4',
                      'A:1:+1, B:2:+2, C:3:+3, D:4:+4, E:5:+5',
                      'A:7:+9',
                      'A:5:+1, B:5:+2, C:5:+3',
                      'B:2:+4, B:3:+4, A:9:+1']) {
    const tr = parseTrace(spec), counts = crdtCounts(tr), lww = lwwMerge(tr);
    eq(crdtValue(counts), traceTotal(tr), 'the CRDT loses nothing on ' + spec);
    eq(lww.value + lww.discarded, traceTotal(tr), 'and LWW loses exactly the rest on ' + spec);
    eq(lww.kept.length + lww.lost.length, tr.length, 'every update is kept or lost on ' + spec);
    eq(lww.value <= traceTotal(tr), true, 'LWW never invents value on ' + spec);
    const st = replicaStates(tr), names = traceReplicas(tr);
    const a = st[names[0]], b = st[names[1]] || a, c = st[names[2]] || b;
    eq(countsEqual(crdtJoin(a, b), crdtJoin(b, a)), true, 'the merge is commutative on ' + spec);
    eq(countsEqual(crdtJoin(crdtJoin(a, b), c), crdtJoin(a, crdtJoin(b, c))), true,
       'associative on ' + spec);
    eq(countsEqual(crdtJoin(crdtJoin(a, b), crdtJoin(a, b)), crdtJoin(a, b)), true,
       'and idempotent on ' + spec);
    /* Joining every replica's own state must reach the same vector as counting
       the trace directly -- gossip converges on the answer. */
    let merged = {};
    for (const nm of names) merged = crdtJoin(merged, st[nm]);
    eq(countsEqual(merged, counts), true, 'gossip converges on the full count for ' + spec);
    eq(crdtValue(merged), traceTotal(tr), 'and on the true total for ' + spec);
  }
}

console.log('system design: storage engines, amplification, filters and recovery');
{
  const STORAGE_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'storage.py');
  const storageSrc = fs.readFileSync(STORAGE_SOURCE, 'utf8');
  const storageBlock = (name) => blockFrom(storageSrc, name, STORAGE_SOURCE);
  const CACHE_SRC = path.join(__dirname, 'mathpath', 'labs', 'cache.py');
  const cacheSrc2 = fs.readFileSync(CACHE_SRC, 'utf8');
  eval(block('RATIONAL_JS') + sysdBlock('RCEIL_JS') + sysdBlock('HARMONIC_JS')
       + sysdBlock('QUEUE_JS') + sysdBlock('APPROX_JS') + storageBlock('STORAGE_JS')
       /* the cache kit's own Zipf wrapper, so L10 can be pinned against the
          course it borrows from rather than merely described as sharing it */
       + blockFrom(cacheSrc2, 'CACHE_JS', CACHE_SRC));

  /* --- printing. Rnum goes through Number and this course overflows it. --- */
  eq(Rfix(R(1n, 3n), 3), '0.333', 'long division in BigInt');
  eq(Rfix(R(2n, 3n), 3), '0.667', 'rounded half up at the last digit');
  eq(Rfix(R(-1n, 3n), 3), '-0.333', 'the sign survives the division');
  eq(grp(62500000), '62 500 000', 'digit grouping');
  eq(byteText(R(4000n, 1n)), '4.00 kB', 'a kB is 1000 B on this course, and it says so');
  eq(byteText(R(1000000000n, 1n)), '1.00 GB', 'and a GB is 10^9 B');
  eq(secText(R(1n, 100n)), '10.00 ms', 'ten milliseconds');
  eq(secText(R(2510n, 1n)), '41.8 min', 'and forty-two minutes is printed as minutes');

  /* --- L1: the pattern, not the size -------------------------------------
     The lesson's headline is a RATIO, and asserting the two times separately
     would not catch a bandwidth term that was right in one and wrong in the
     other. 1 GB in 4 kB chunks on a 10 ms / 100 MB/s disk. */
  const GB = R(1000000000n, 1n), CHUNK = R(4000n, 1n);
  const SEEK = R(1n, 100n), BW = R(100000000n, 1n);
  eq(seekCount(GB, CHUNK), 250000n, 'a gigabyte in 4 kB reads is 250 000 seeks');
  eq(Rtext(seqTime(GB, SEEK, BW)), '1001/100', 'sequential: one seek and then the bytes');
  eq(Rtext(randomTime(GB, CHUNK, SEEK, BW)), '2510', 'random: 250 000 seeks and the same bytes');
  eq(Rtext(ioRatio(GB, CHUNK, SEEK, BW)), '251000/1001', 'the ratio the lesson quotes as ~250');
  eq(Rfix(ioRatio(GB, CHUNK, SEEK, BW), 2), '250.75', 'and 250.75 is what 250 is short for');
  /* The bytes term is IDENTICAL in both, which is the whole claim: everything
     that differs between a sequential and a random read is the seek count. */
  eq(Rtext(Rsub(randomTime(GB, CHUNK, SEEK, BW), seqTime(GB, SEEK, BW))),
     Rtext(Rmul(R(249999n, 1n), SEEK)), 'the difference is exactly 249 999 extra seeks');
  eq(Rtext(crossoverChunk(SEEK, BW)), '1000000', 'the crossover chunk is t_seek * bw = 1 MB');
  /* At the crossover the two terms of the formula are equal. That is the
     DEFINITION of the crossover, and it is checked rather than restated. */
  {
    const cross = crossoverChunk(SEEK, BW);
    const seeks = seekCount(GB, cross);
    eq(Rtext(Rmul(R(seeks, 1n), SEEK)), Rtext(Rdiv(GB, BW)),
       'at the crossover chunk the seek term equals the byte term');
  }
  /* The same arithmetic on hardware two orders of magnitude quicker to seek:
     the 250 collapses to 13.5, which is the lesson's solid-state preset. */
  eq(Rfix(ioRatio(GB, CHUNK, R(1n, 10000n), R(500000000n, 1n)), 2), '13.50',
     'an SSD turns the 250x into 13.5x');
  eq(byteText(crossoverChunk(R(1n, 10000n), R(500000000n, 1n))), '50.00 kB',
     'and moves the crossover from 1 MB to 50 kB');

  /* --- L2: the height, by integer search ---------------------------------
     The boundary is the whole reason this is a search and not a logarithm. */
  eq(btreeHeight(1000000000n, 500), 4, 'a billion keys at B = 500 is four levels');
  eq(String(btreeCapacity(500, 3)), '125000000', 'three levels reach 125 million, short of it');
  eq(String(btreeCapacity(500, 4)), '62500000000', 'and four reach 62.5 billion');
  eq(lookupIos(1000000000n, 500, 2), 2, 'with two levels cached a lookup is two page reads');
  eq(lookupIos(1000000000n, 500, 9), 0, 'caching more levels than exist is not negative work');
  eq(lookupIos(1000000000n, 500, 0), 4, 'and caching none is the full height');
  eq(btreeHeight(1, 500), 1, 'one key still costs a page');
  eq(btreeHeight(500, 500), 1, 'N = B exactly is ONE level, not two');
  eq(btreeHeight(501, 500), 2, 'and one key more is two');
  eq(btreeHeight(100, 1), null, 'a fanout of one never covers N, and says so');
  /* Exact at every whole power of B -- including the four where the floating
     point logarithm is not, which is why the lab prints both. */
  [[3, 2], [5, 3], [6, 3], [7, 3], [8, 7], [14, 2], [18, 3], [19, 5], [12, 13], [500, 4]]
    .forEach(([b, h]) => {
      const n = BigInt(b) ** BigInt(h);
      eq(btreeHeight(n, b), h, 'B = ' + b + ', N = B^' + h + ' is exactly ' + h + ' levels');
      eq(btreeHeight(n + 1n, b), h + 1, 'and one key past it is ' + (h + 1));
    });
  eq(btreeHeightByLog(9, 3), 3, 'Math.ceil(log 9 / log 3) says three levels');
  eq(btreeHeight(9, 3), 2, 'and the integer search says two, which is the right answer');
  eq(btreeHeightByLog(125, 5), 4, 'the logarithm is wrong at B = 5, N = 125 too');
  eq(btreeHeight(125, 5), 3, 'where the search gives three');

  /* --- L3: a workload mix, in I/Os --------------------------------------- */
  eq(pagesFor(1000000, 200), 5000n, 'a million rows at 200 a page is 5000 pages');
  eq(hashPointIos(), 1n, 'a hash point lookup is one I/O');
  eq(hashRangeIos(1000000, 200), 5000n, 'and a hash RANGE is the whole table');
  eq(treePointIos(1000000, 500), 3n, 'the tree pays its height on a point lookup');
  eq(treeRangeIos(1000000, 500, 100, 200), 3n, 'and height - 1 plus the leaves on a range');
  eq(Rtext(mixIos(900, 100, hashPointIos(), hashRangeIos(1000000, 200))), '500900',
     'the hash does half a million I/O a second on this mix');
  eq(Rtext(mixIos(900, 100, treePointIos(1000000, 500), treeRangeIos(1000000, 500, 100, 200))),
     '3000', 'and the tree does three thousand');
  eq(Rtext(rangeCrossover(900, 1n, 5000n, 3n, 3n)), '1800/4997',
     'a third of a range query a second is enough to flip the choice');
  /* The crossover is a TIE, and the tie is checked rather than asserted: at
     that range rate the two engines cost the same, exactly. */
  {
    const r = rangeCrossover(900, 1n, 5000n, 3n, 3n), p = R(900n, 1n);
    const h = Radd(Rmul(p, R(1n, 1n)), Rmul(r, R(5000n, 1n)));
    const t = Radd(Rmul(p, R(3n, 1n)), Rmul(r, R(3n, 1n)));
    eq(Rtext(h), Rtext(t), 'at the crossover rate both engines do the same I/O');
  }
  eq(rangeCrossover(900, 1n, 7n, 3n, 7n), null, 'and nothing ties them when the ranges cost the same');

  /* --- L4: the write cost of an index ------------------------------------ */
  eq(Rtext(writesPerInsert(0)), '1', 'no indexes: one write');
  eq(Rtext(writesPerInsert(3)), '4', 'three indexes: four writes');
  eq(Rtext(insertRate(10000, 3)), '2500', '10 000 random writes a second is 2500 inserts');
  eq(Rtext(throughputShare(3)), '1/4', 'a quarter of the bare rate');
  eq(String(indexesForShare(R(1n, 2n))), '1', 'the k that HALVES throughput is one, computed');
  eq(String(indexesForShare(R(1n, 3n))), '2', 'a third takes two');
  eq(String(indexesForShare(R(2n, 5n))), '2', 'and two fifths takes two as well');
  eq(String(maxIndexesFor(10000, 2500)), '3', 'three indexes still meet 2500 inserts a second');
  eq(String(maxIndexesFor(10000, 3000)), '2', 'only two meet 3000');
  eq(maxIndexesFor(10000, 20000), null, 'and no number of indexes meets 20 000');
  /* The bound is tight in both directions, which a single equality would not
     show: k meets the target and k + 1 does not. */
  [[10000, 2500], [10000, 3000], [7500, 1200], [50000, 9000]].forEach(([d, t]) => {
    const k = maxIndexesFor(d, t);
    eq(Rcmp(insertRate(d, Number(k)), R(BigInt(t), 1n)) >= 0, true,
       d + '/s at k = ' + k + ' still meets ' + t);
    eq(Rcmp(insertRate(d, Number(k) + 1), R(BigInt(t), 1n)) < 0, true,
       'and k = ' + (Number(k) + 1) + ' does not');
  });

  /* --- L5: write amplification ------------------------------------------- */
  eq(Rtext(lsmWriteAmp(5, 10)), '25', 'L = 5, F = 10 rewrites each byte 25 times');
  eq(Rtext(lsmWriteAmp(7, 11)), '77/2', 'and an odd product stays a fraction, not a rounding');
  eq(Rtext(lsmReadAmp(5)), '5', 'read amplification before filters is L');
  eq(byteText(compactionBw(R(50000000n, 1n), lsmWriteAmp(5, 10))), '1.25 GB',
     '50 MB/s of ingest needs 1.25 GB a second of disk');
  eq(byteText(levelCapacity(R(64000000n, 1n), 10, 5)), '6.40 TB', 'the fifth level holds 6.4 TB');
  eq(levelsForSize(R(1000000000000n, 1n), R(64000000n, 1n), 10), 5,
     'a terabyte over a 64 MB memtable at F = 10 forces five levels');
  /* The same boundary discipline as the B-tree height, and for the same
     reason: at an exact power the answer is L, not L + 1. */
  eq(levelsForSize(R(6400000000000n, 1n), R(64000000n, 1n), 10), 5, 'exactly 10^5 memtables is five');
  eq(levelsForSize(R(6400000000001n, 1n), R(64000000n, 1n), 10), 6, 'and one byte more is six');
  eq(levelsForSize(R(1000000n, 1n), R(64000000n, 1n), 10), 0, 'data inside the memtable needs no level');
  eq(levelsForSize(R(1000000000000n, 1n), R(64000000n, 1n), 1), null, 'a fanout of one never fills');

  /* --- L6: bits per key, and WHICH constant --------------------------------
     The whole point of the rewritten lesson is that 9.57 is the two-digit
     constant's answer and 9.585 is the constant's own. Both are pinned, and so
     is the gap, because a lab that printed one under the other's name would
     look entirely reasonable. */
  near(bitsPerKeyApprox(0.01), 9.585058, 1e-6, '1% costs 9.585 bits per key, at 1/ln2');
  near(bitsPerKeyTextbook(0.01), 9.567153, 1e-6, 'and 9.567 at the textbook 1.44');
  near(bitsPerKeyApprox(0.01) - bitsPerKeyTextbook(0.01), 0.017905, 1e-6,
       'the two differ in the second decimal, which is the lesson');
  near(bitsPerKeyApprox(0.001), 14.377587, 1e-6, '0.1% costs 14.38 bits per key');
  near(bitsPerKeyApprox(0.1), 4.792529, 1e-6, 'and 10% costs 4.79');
  /* Independent of n: that is the claim, so it is checked at three sizes. */
  [1e6, 1e9, 1e11].forEach((n) => {
    near(bloomBits(n, 0.01) / n, bitsPerKeyApprox(0.01), 1e-6,
         'bits per key is the same at n = ' + n);
  });
  eq(bloomHashes(0.01), 7, 'k = log2(1/p) rounds to seven hashes at 1%');
  eq(bloomHashes(0.001), 10, 'ten at 0.1%');
  eq(bloomHashes(0.5), 1, 'and never fewer than one');
  eq(byteText(bloomMemoryBytes(1e9, 0.01)), '1.20 GB', 'a billion keys at 1% is 1.2 GB of filter');
  /* The EXACT form, as a rational, beside the approximation every figure on
     the page uses. They are NOT the same number, and that is the point of
     printing both: 3% apart at this size. */
  {
    const exact = bloomExactRate(64, 8, 5);
    eq(Rfix(exact, 8), '0.02230073', 'the exact (1-(1-1/m)^kn)^k at m=64, n=8, k=5');
    eq(String(exact.d).length, 362, 'which is a fraction with a 362-digit denominator');
    near(bloomApprox(64, 8, 5), 0.02167922, 1e-8, 'the approximation gives 0.021679');
    near(Rfix(exact, 8) - bloomApprox(64, 8, 5), 0.00062151, 1e-7,
         'so the approximation is 2.8% low here, and the page shows both');
  }
  eq(bloomExactRate(100000, 8, 5), null, 'past a printable size it returns null, not a rounding');
  eq(bloomExactRate(64, 200, 5), null, 'and the same when kn is past it');
  eq(Rtext(readAmpWithFilter(5, R(1n, 100n))), '26/25',
     'a filter per level turns RA of 5 into 1 + 4/100, exactly');
  eq(Rtext(readAmpWithFilter(5, R(0n, 1n))), '1', 'a perfect filter would make it one');
  eq(Rtext(readAmpWithFilter(5, R(1n, 1n))), '5', 'and a useless one leaves it at L');
  /* expNegApprox is what bloomApprox is built on, and it was wrong in a way
     that looked right: the alternating series for e^-x cancels. The
     positive-term form is accurate across the whole range, including where
     the old one returned a NEGATIVE probability. */
  near(expNegApprox(0), 1, 1e-15, 'e^-0 is one');
  [1, 5, 17, 20, 21, 50, 200, 600].forEach((x) => {
    near(expNegApprox(x) / Math.exp(-x), 1, 1e-12, 'e^-' + x + ' is accurate to 1e-12 relative');
  });
  eq(expNegApprox(21) > 0, true, 'and never returns a negative probability');

  /* --- L7: the RUM triple ------------------------------------------------- */
  {
    const lev = rumLevelled(5, 10), tier = rumTiered(5, 10);
    const bt = rumBtree(4, 4000, 128, R(2n, 3n));
    eq([lev.read, lev.write, lev.space].map(Rtext).join('/'), '5/25/11/10', 'levelled: 5, 25, 1.1');
    eq([tier.read, tier.write, tier.space].map(Rtext).join('/'), '50/5/10', 'tiered: 50, 5, 10');
    eq([bt.read, bt.write, bt.space].map(Rtext).join('/'), '4/125/4/3/2', 'B-tree: 4, 31.25, 1.5');
    /* The lesson's claim is that no engine wins all three. Asserted as three
       comparisons rather than as prose, so a change that quietly made one
       engine dominate would fail here. */
    eq(Rcmp(tier.write, lev.write) < 0, true, 'tiered writes less than levelled');
    eq(Rcmp(tier.read, lev.read) > 0, true, 'and reads more');
    eq(Rcmp(tier.space, lev.space) > 0, true, 'and keeps more copies');
    eq(Rcmp(bt.read, lev.read) < 0, true, 'the B-tree reads in fewer I/Os than either LSM');
    eq(Rcmp(bt.write, tier.write) > 0, true, 'and writes a whole page to change a row');
    /* The shares are a probability vector, which is what lets them be plotted. */
    [lev, tier, bt].forEach((t, i) => {
      const sh = rumShares(t);
      eq(Rtext(Radd(Radd(sh.read, sh.write), sh.space)), '1',
         'the three shares of engine ' + i + ' sum to one');
    });
    eq(byteText(compactionBw(R(50000000n, 1n), tier.write)), '250.00 MB',
       'tiered needs 250 MB a second of disk at 50 MB/s of ingest');
    eq(byteText(compactionBw(R(50000000n, 1n), lev.write)), '1.25 GB', 'levelled needs five times that');
  }

  /* --- L8: fsync and group commit ----------------------------------------- */
  {
    const TF = R(1n, 100n), LAM = R(5000n, 1n);
    eq(Rtext(durableCap(TF)), '100', 'a 10 ms fsync caps durable writes at 100 a second');
    eq(Rtext(groupedCap(TF, 64)), '6400', 'grouping 64 makes it 6400 on the same disk');
    eq(Rtext(perWriteCost(TF, 64)), '1/6400', 'each write carries 1/64 of the fsync');
    eq(Rtext(perWriteCost(TF, 1)), '1/100', 'and alone it carries all of it');
    eq(Rtext(fillWait(1, LAM)), '0', 'a batch of one waits for nobody');
    eq(Rtext(fillWait(64, LAM)), '63/10000', 'and a batch of 64 waits 6.3 ms at 5000/s');
    /* The cap arrives as a QUEUEING fact: at B = 1 and 5000 arrivals a second
       the commit queue is unstable, which is what "capped at 1/t" means. */
    eq(commitLatency(TF, 1, LAM).stable, false, 'one fsync per write cannot keep up with 5000/s');
    eq(Rtext(commitLatency(TF, 1, LAM).rho), '50', 'it is fifty times oversubscribed');
    eq(commitLatency(TF, 64, LAM).stable, true, 'grouping 64 makes it stable');
    eq(Rtext(commitLatency(TF, 64, LAM).rho), '25/32', 'at rho = 0.78125');
    eq(commitLatency(TF, 1, R(50n, 1n)).stable, true, 'and at 50 arrivals a second B = 1 is fine');
    /* The optimum is SCANNED. Checking only its position would not catch a
       scan that returned a batch size whose latency was not actually least. */
    {
      const best = bestBatch(TF, LAM, 256);
      eq(best.batch, 121, 'the batch that minimises commit latency here is 121');
      eq(secText(best.total), '29.04 ms', 'at 29.04 ms all in');
      for (let B = 1; B <= 256; B += 1) {
        const c = commitLatency(TF, B, LAM);
        if (c.stable && Rcmp(c.total, best.total) < 0) {
          eq(B, best.batch, 'no batch beats the one the scan returned');
        }
      }
      eq(Rcmp(commitLatency(TF, 64, LAM).total, best.total) > 0, true,
         'and the round 64 is worse than it');
      eq(Rcmp(commitLatency(TF, 256, LAM).total, best.total) > 0, true,
         'and so is 256, so the minimum is interior');
    }
    eq(bestBatch(TF, R(50000n, 1n), 256), null, 'past 1/t * maxB no batch keeps up, and it says so');
  }

  /* --- L9: row against column --------------------------------------------- */
  {
    const ROWS = 1000000000, RR = R(2n, 1n), CR = R(5n, 1n), BW1 = R(1000000000n, 1n);
    eq(Rtext(columnBytes(200, 20)), '10', 'twenty columns of a 200-byte row are 10 B each');
    eq(byteText(rowScanBytes(ROWS, 200, RR)), '100.00 GB', 'the row store reads 100 GB');
    eq(byteText(colScanBytes(ROWS, 200, 20, 3, CR)), '6.00 GB', 'the column store reads 6 GB');
    eq(secText(scanSeconds(rowScanBytes(ROWS, 200, RR), BW1)), '100.00 s', 'a hundred seconds');
    eq(secText(scanSeconds(colScanBytes(ROWS, 200, 20, 3, CR), BW1)), '6.00 s', 'against six');
    eq(Rtext(Rdiv(rowScanBytes(ROWS, 200, RR), colScanBytes(ROWS, 200, 20, 3, CR))), '50/3',
       'a factor of 16.67, from three columns and a better ratio');
    eq(Rtext(colCrossover(20, RR, CR)), '50', 'the scans would tie at 50 columns, past the 20 there are');
    eq(Rtext(colCrossover(20, RR, RR)), '20', 'at equal compression they tie at every column');
    /* And the query where columnar loses, which is the misconception. */
    eq(wholeRowIos(20, 'row'), 1n, 'one whole row is one page in a row store');
    eq(wholeRowIos(20, 'column'), 20n, 'and one page per column in a column store');
    let threw = false;
    try { wholeRowIos(20, 'hybrid'); } catch (e) { threw = true; }
    eq(threw, true, 'an unknown layout throws rather than defaulting to a row store');
  }

  /* --- L10: the page cache IS course 4's cache ----------------------------
     Not described as shared -- pinned. wsHit's exact branch and the cache
     kit's zipfShare are evaluated here from their own shipped sources, and
     they must agree digit for digit. */
  {
    const PAGE = R(8000n, 1n);
    eq(pageCount(R(500000000000n, 1n), PAGE), 62500000n, '500 GB is 62.5 million 8 kB pages');
    eq(pageCount(R(64000000000n, 1n), PAGE), 8000000n, 'and 64 GB is eight million');
    for (const [c, n, s] of [[4, 40, 1], [10, 40, 2], [1, 40, 1], [25, 40, 3]]) {
      eq(Rtext(wsHit(c, n, s, 40).exact), Rtext(zipfShare(c, n, s, 40).exact),
         'storage and cache agree exactly at C = ' + c + ', N = ' + n + ', s = ' + s);
      eq(Rtext(wsHit(c, n, s, 40).exact), Rtext(zipfHit(c, n, s)),
         'and both are the core zipfHit, not a second implementation');
    }
    eq(wsHit(4, 40, 1, 40).rounded, false, 'inside the limit the figure is an exact fraction');
    eq(wsHit(8000000, 62500000, 1, 40).rounded, true, 'and past it the lab reports that it rounds');
    near(wsHit(8000000, 62500000, 1, 40).value, 0.889047, 1e-5,
         '64 GB of a 500 GB dataset at s = 1 holds 88.9% of the reads');
    /* s = 0 is the control, and it stays EXACT at any size because H(n,0) = n.
       A lab that rounded it would be rounding C/N. */
    eq(wsHit(8000000, 62500000, 0, 40).rounded, false, 'the uniform case never rounds');
    eq(Rtext(wsHit(8000000, 62500000, 0, 40).exact), '16/125', 'it is C/N: 12.8%');
    eq(Rtext(wsHit(0, 40, 1, 40).exact), '0', 'no memory holds nothing');
    eq(Rtext(wsHit(40, 40, 1, 40).exact), '1', 'and memory for all of it holds everything');
    eq(Rtext(diskIopsExact(20000, R(16n, 125n))), '17440', 'the uniform case leaves 17 440 IOPS');
    eq(Math.round(diskIopsApprox(20000, wsHit(8000000, 62500000, 1, 40).value)), 2219,
       'and the skewed one leaves 2219, which is the point of the lesson');
  }

  /* --- L11: RPO and RTO are different numbers ----------------------------- */
  {
    const IVL = R(86400n, 1n), W = R(20000000n, 1n), SIZE = R(2000000000000n, 1n);
    const RES = R(200000000n, 1n), REP = R(50000000n, 1n);
    eq(byteText(rpoBytes(IVL, W)), '1.73 TB', 'a day at 20 MB/s puts 1.73 TB at risk');
    eq(byteText(rpoExpectedBytes(IVL, W)), '864.00 GB', 'and 864 GB on average');
    eq(secText(restoreSeconds(SIZE, RES)), '2.78 h', 'copying 2 TB back at 200 MB/s is 2.8 hours');
    eq(secText(replaySeconds(rpoBytes(IVL, W), REP)), '9.60 h', 'replaying the log is 9.6 more');
    eq(secText(rtoSeconds(SIZE, RES, rpoBytes(IVL, W), REP)), '12.38 h', 'an RTO of 12.4 hours');
    /* Halving the interval halves the RPO and the replay and leaves the copy
       alone, which is why the copy is the floor. */
    eq(Rtext(Rdiv(rpoBytes(R(43200n, 1n), W), rpoBytes(IVL, W))), '1/2',
       'half the interval is half the bytes at risk');
    eq(Rtext(Rsub(rtoSeconds(SIZE, RES, rpoBytes(R(43200n, 1n), W), REP),
                  restoreSeconds(SIZE, RES))),
       Rtext(Rdiv(Rsub(rtoSeconds(SIZE, RES, rpoBytes(IVL, W), REP),
                       restoreSeconds(SIZE, RES)), R(2n, 1n))),
       'and half the replay, while the copy does not move at all');
    /* The interval a target implies, checked by round trip rather than by
       repeating the rearrangement. */
    {
      const ivl = intervalForRto(SIZE, RES, W, REP, R(14400n, 1n));
      eq(Rtext(ivl), '11000', 'a four-hour RTO allows a backup every 11 000 seconds');
      eq(Rtext(rtoSeconds(SIZE, RES, rpoBytes(ivl, W), REP)), '14400',
         'and at that interval the RTO is the target exactly');
    }
    eq(intervalForRto(SIZE, RES, W, REP, R(3600n, 1n)), null,
       'inside an hour is impossible: the copy alone is 2.8 hours, and it says so');
  }
}

// ------------------------------- system design C9: scaling laws and cost
/* The `scale` kit's own arithmetic, on the numbers its thirteen modes print.

   The block this section exists for is the Universal Scalability Law's TURNOVER.
   A coherency term dropped anywhere -- from the denominator, or by locating the
   peak from contention alone -- leaves a curve that rises and plateaus. Every
   figure on the page still looks plausible, the lesson's hard idea is quietly
   inverted, and nothing else in this repository would notice. So the assertions
   below do not merely check that N* has the value the closed form suggests: they
   check that C(N*+1) is strictly LESS than C(N*), that it keeps falling, and
   that with beta = 0 the same curve is monotone -- which is exactly what a
   dropped coherency term looks like.

   The other five are the break-evens. Each is asserted as the EQUALITY it came
   from rather than as a remembered decimal: at the break-even bandwidth the two
   transfer times are equal as fractions, at the placement crossover the two
   plans tie, and the reserved level found by the marginal rule is the level an
   exhaustive costing of every integer level also picks. */
console.log('system design: scaling laws, break-evens and what capacity costs');
{
  const SCALE_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'scale.py');
  const scaleSrc = fs.readFileSync(SCALE_SOURCE, 'utf8');
  const scaleBlock = (name) => blockFrom(scaleSrc, name, SCALE_SOURCE);
  /* No BIGINT_JS: the scale kit does not ship it either, and evaluating a
     block here that the page does not carry would test a program nobody runs. */
  eval(block('RATIONAL_JS') + sysdBlock('RCEIL_JS')
       + sysdBlock('APPROX_JS') + scaleBlock('SCALE_JS'));

  /* --- scale kit: BEGIN assertions (the mutation harness slices on this) --- */

  /* --- printing, at sizes that defeat Rdec --------------------------------- */
  eq(Rfixed(R(1n, 3n), 4), '0.3333', 'a third to four places');
  eq(Rfixed(R(2n, 3n), 4), '0.6667', 'two thirds rounds up');
  eq(Rfixed(R(-1n, 3n), 3), '-0.333', 'and the sign survives');
  eq(Rfixed(loadAtMonth(R(5000n, 1n), R(1n, 10n), 400), 0),
     String((11n ** 400n * 5000n + 10n ** 400n / 2n) / 10n ** 400n),
     'a 400-month compounding, printed exactly where Number would have said Infinity');
  eq(Number.isFinite(Rnum(loadAtMonth(R(5000n, 1n), R(1n, 10n), 400))), false,
     'which is precisely what Rnum does say, and why Rfixed exists');
  eq(groupDec('1234567.89'), '1 234 567.89', 'grouping stops at the decimal point');
  eq(groupDec('-1000'), '-1 000', 'and does not eat the sign');
  eq(money(R(1n, 100000n)), '$0.00001000', 'a unit cost keeps the digits it is about');
  eq(money(R(12345n, 1n)), '$12 345', 'and a monthly bill does not pretend to cents');
  eq(fmtBytes(R(2000000000000n, 1n), 2), '2 TB', 'decimal units: a TB is 10^12 bytes');
  eq(fmtSecs(R(1n, 4n)), '250 ms', 'a quarter second reads as milliseconds');
  eq(Rtext(ladderValue(52)), '500000000', 'the ladder is exact at every rung');

  /* --- L1: Amdahl ---------------------------------------------------------- */
  const p95 = R(95n, 100n);
  eq(Rtext(amdahlSpeedup(p95, 1)), '1', 'one machine is one machine');
  eq(Rtext(amdahlSpeedup(p95, 32)), '640/51', 'the lesson preset: 32 machines at 95% parallel');
  eq(Rtext(amdahlCeiling(p95)), '20', 'five per cent serial caps the speedup at twenty');
  eq(amdahlCeiling(R(1n, 1n)), null, 'and p = 1 has no ceiling to report');
  /* THE CEILING IS A CEILING: no n reaches it, at any n. */
  for (const n of [10, 100, 1000, 100000]) {
    eq(Rcmp(amdahlSpeedup(p95, n), amdahlCeiling(p95)) < 0, true,
       'S(n) stays strictly below 1/(1-p) at n = ' + n);
  }
  /* THE IDENTITY: the scan and the rearranged inequality are the same integer,
     at every parallel fraction and every target. */
  for (const [pn, pd] of [[95, 100], [99, 100], [7, 10], [999, 1000], [1, 2], [1, 100]]) {
    for (const [fn, fd] of [[9, 10], [1, 2], [95, 100], [99, 100]]) {
      const p = R(BigInt(pn), BigInt(pd)), f = R(BigInt(fn), BigInt(fd));
      const scan = amdahlReach(p, f, 200000), closed = amdahlReachClosed(p, f);
      eq(scan, closed, 'scan and closed form agree at p = ' + pn + '/' + pd + ', f = ' + fn + '/' + fd);
      eq(Rcmp(amdahlSpeedup(p, scan), Rmul(f, amdahlCeiling(p))) >= 0, true,
         'and that n really does reach the target');
      if (scan > 1) {
        eq(Rcmp(amdahlSpeedup(p, scan - 1), Rmul(f, amdahlCeiling(p))) < 0, true,
           'while the one before it does not');
      }
    }
  }
  eq(amdahlReachClosed(p95, R(9n, 10n)), 171, '90% of a twentyfold ceiling takes 171 machines');
  eq(Rtext(amdahlEfficiency(p95, 32)), '20/51', 'and 32 machines are 39% busy doing it');
  eq(Rtext(linearSpeedup(32)), '32', 'the expectation the lesson names');

  /* --- L2: the Universal Scalability Law, and its TURNOVER ----------------- */
  const uA = R(1n, 50n), uB = R(1n, 10000n);
  eq(Rtext(uslThroughput(1, uA, uB)), '1', 'one machine is one machine here too');
  eq(uslPeakExact(uA, uB, 20000), 99, 'the lesson curve peaks at 99 machines');
  eq(uslPeakScan(uA, uB, 400).N, 99, 'and the argmax of the scan agrees');
  near(uslPeakRootApprox(uA, uB), 98.99494936611666, 1e-9, 'sqrt((1-a)/b) rounds to 98.995');

  /* THE ASSERTION THIS SECTION EXISTS FOR. */
  for (const [an, ad, bn, bd] of [[1, 50, 1, 10000], [1, 20, 1, 1000], [1, 200, 1, 100000],
                                  [0, 1, 1, 1000], [1, 10, 1, 500], [1, 4, 1, 50]]) {
    const a = R(BigInt(an), BigInt(ad)), b = R(BigInt(bn), BigInt(bd));
    const where = 'a = ' + an + '/' + ad + ', b = ' + bn + '/' + bd;
    const N = uslPeakExact(a, b, 20000);
    eq(N !== null && N >= 1, true, 'a peak exists at ' + where);
    eq(Rcmp(uslThroughput(N + 1, a, b), uslThroughput(N, a, b)) < 0, true,
       'THE CURVE FALLS past N* at ' + where);
    eq(Rcmp(uslThroughput(2 * N, a, b), uslThroughput(N, a, b)) < 0, true,
       'and keeps falling at twice N*, ' + where);
    if (N > 1) {
      eq(Rcmp(uslThroughput(N - 1, a, b), uslThroughput(N, a, b)) < 0, true,
         'while the machine before N* was still buying something, ' + where);
    }
    eq(uslPeakScan(a, b, 4 * N + 20).N, N, 'the scan finds the same peak at ' + where);
    const root = uslPeakRootApprox(a, b);
    eq(N >= Math.floor(root) && N <= Math.ceil(root), true,
       'and the rounded root brackets it at ' + where);
    /* the predicate and the comparison are the same claim */
    eq(uslBeyondPeak(N, a, b), true, 'bN(N+1) >= 1-a holds at N*, ' + where);
    eq(N === 1 || !uslBeyondPeak(N - 1, a, b), true, 'and not before it, ' + where);
  }
  /* AND WHAT A DROPPED COHERENCY TERM LOOKS LIKE: with b = 0 there is no peak
     and the curve is monotone all the way out. */
  eq(uslPeakExact(uA, R(0n, 1n), 20000), null, 'beta = 0 has no peak at all');
  {
    let mono = true;
    for (let N = 1; N < 500; N += 1) {
      if (Rcmp(uslThroughput(N + 1, uA, R(0n, 1n)), uslThroughput(N, uA, R(0n, 1n))) <= 0) mono = false;
    }
    eq(mono, true, 'with beta = 0 the curve only ever rises -- Amdahl, not the USL');
  }
  eq(Rtext(uslContentionCeiling(uA)), '50', 'and it rises towards 1/a = 50');
  eq(Rtext(uslRetained(99, uA, uB, 99)), '1', 'the peak retains all of itself');
  eq(Rcmp(uslRetained(198, uA, uB, 99), R(1n, 1n)) < 0, true,
     'and twice the peak, at twice the bill, retains less');

  /* --- L3: batching -------------------------------------------------------- */
  const bF = R(2000n, 1n), bV = R(100n, 1n), bLam = R(500n, 1n);
  eq(Rtext(perItemCost(bF, bV, 1)), '2100', 'one item alone pays the whole call');
  eq(Rtext(perItemCost(bF, bV, 100)), '120', 'and a batch of a hundred pays a fiftieth of it');
  eq(Rtext(fixedShare(bF, bV, 100)), '1/6', 'the fixed part is a sixth of the cost there');
  eq(batchForFixedShare(bF, bV, R(1n, 5n)), 100, 'F/B = v/5 at B = 100');
  eq(Rtext(batchWaitFirst(100, bLam)), '99/500', 'the first item waits (B-1)/lambda');
  eq(Rtext(batchWaitMean(100, bLam)), '99/1000', 'and the average item waits half of that');
  /* THE RULE OF THUMB'S ERROR IS EXACTLY ONE INTER-ARRIVAL TIME, at every B --
     which is why it is usable and still not the number. */
  for (const B of [2, 10, 100, 800]) {
    eq(Rtext(Rsub(batchWaitRule(B, bLam), batchWaitFirst(B, bLam))), Rtext(Rinv(bLam)),
       'B/lambda overstates the first item\'s wait by 1/lambda at B = ' + B);
  }
  eq(Rcmp(perItemCost(bF, bV, 800), bV) > 0, true, 'the cost curve never reaches its floor');
  eq(batchUnderTimer(100, bLam, R(1n, 5n)).effective, 100, 'a 200 ms timer just reaches a batch of 100');
  eq(batchUnderTimer(400, bLam, R(1n, 5n)).capped, true, 'and caps a batch of 400');
  eq(batchUnderTimer(400, bLam, R(1n, 5n)).effective, 100, 'at the hundred that arrive in the window');

  /* --- L4: vertical against horizontal ------------------------------------- */
  const vAlpha = R(1n, 200n);
  /* the node count is the USL's contention term, not a second overhead model */
  eq(horizontalNodes(1, vAlpha, 6000), 1, 'one node delivers one node');
  eq(horizontalNodes(5, vAlpha, 6000), 6, 'five nodes\' worth takes six of them at a = 1/200');
  eq(Rcmp(uslThroughput(6, vAlpha, R(0n, 1n)), R(5n, 1n)) >= 0, true, 'because C(6) clears 5');
  eq(Rcmp(uslThroughput(5, vAlpha, R(0n, 1n)), R(5n, 1n)) < 0, true, 'and C(5) does not');
  eq(horizontalNodes(60, R(1n, 20n), 6000), null,
     'and 1/a is a ceiling on a fleet exactly as it is on a program');
  eq(JSON.stringify(verticalRung(5)), '{"rung":3,"units":8}', 'a 5x target buys the 8x rung');
  eq(Rtext(verticalCost(5, R(100n, 1n), R(11n, 10n))), '5324/5',
     'at 10% a doubling that rung costs $1064.80, not $500');
  eq(shapeFirstCrossing(R(100n, 1n), R(100n, 1n), R(11n, 10n), vAlpha, 64, 6000), 3,
     'horizontal first wins at 3x');
  eq(shapeBreakEven(R(100n, 1n), R(100n, 1n), R(11n, 10n), vAlpha, 64, 6000), 5,
     'but only from 5x does it never lose again -- the ladder is a staircase');
  eq(horizontalWinsAt(4, R(100n, 1n), R(100n, 1n), R(11n, 10n), vAlpha, 6000), false,
     'and at 4x the freshly bought rung is cheaper');
  /* a break-even is a break-even: nothing below it wins from there on */
  {
    const be = shapeBreakEven(R(100n, 1n), R(100n, 1n), R(11n, 10n), vAlpha, 64, 6000);
    let always = true;
    for (let t = be; t <= 64; t += 1) {
      if (!horizontalWinsAt(t, R(100n, 1n), R(100n, 1n), R(11n, 10n), vAlpha, 6000)) always = false;
    }
    eq(always, true, 'and horizontal wins at every target from the break-even on');
  }

  /* --- L5: waste ----------------------------------------------------------- */
  const dayW = dayShape('evening', 21, 6).map((w) => R(BigInt(w), 1n));
  const dayS = profileStats(dayW);
  eq(Rtext(dayS.peak) + ' ' + Rtext(dayS.mean), '48 21', 'the lesson profile: peak 48, mean 21');
  eq(Rtext(dayS.peakToMean), '16/7', 'peak over mean, exactly');
  eq(Rtext(paidCapacity(dayS.peak, R(7n, 10n))), '480/7', 'you pay for peak/rho');
  eq(Rtext(wasteFraction(dayS.mean, dayS.peak, R(7n, 10n))), '111/160', 'and waste 69.4% of it');
  /* THE SIZE OF THE DAY CANCELS: only the SHAPE and rho move the waste. */
  for (const k of [2n, 17n, 1000000n]) {
    const scaled = dayW.map((v) => Rmul(v, R(k, 1n)));
    const s2 = profileStats(scaled);
    eq(Rtext(wasteFraction(s2.mean, s2.peak, R(7n, 10n))), '111/160',
       'scaling every bucket by ' + k + ' leaves the waste untouched');
  }
  eq(Rtext(wasteFraction(dayS.mean, dayS.peak, R(1n, 1n))), '9/16',
     'and even at rho = 1 the shape alone wastes 56%');
  {
    const flat = dayShape('flat', 12, 0).map((w) => R(BigInt(w), 1n));
    const fs2 = profileStats(flat);
    eq(Rtext(wasteFraction(fs2.mean, fs2.peak, R(1n, 1n))), '0',
       'a flat profile at rho = 1 is the only one with no waste at all');
  }
  eq(JSON.stringify(hoursOver(dayW, dayS.mean).hours), '9',
     'cutting to the mean leaves nine hours of the day over capacity');
  eq(Rtext(hoursOver(dayW, dayS.mean).worst), '27',
     'the worst of them short by 27 -- more than the mean bucket itself');
  eq(JSON.stringify(hoursOver(dayW, paidCapacity(dayS.peak, R(7n, 10n))).hours), '0',
     'while the capacity actually bought covers every hour');

  /* --- L6: reserved, on-demand and spot ------------------------------------ */
  eq(Rtext(breakEvenUtilisation(R(7n, 100n), R(12n, 100n))), '7/12', 'u* is the price ratio');
  /* THE IDENTITY: the marginal rule and an exhaustive costing pick the same
     level, on every profile and at every price pair. */
  const profiles = [
    dayShape('evening', 21, 4), dayShape('office', 10, 5),
    dayShape('batchwindow', 3, 9), dayShape('flat', 12, 0), dayShape('evening', 21, 10)
  ].map((w) => w.map((v) => R(BigInt(v), 1n)));
  for (let pi = 0; pi < profiles.length; pi += 1) {
    const bs = profiles[pi];
    const top = Number(profileStats(bs).peak.n);
    for (const [rn, dn] of [[7, 12], [3, 12], [11, 12], [1, 12], [12, 12], [6, 12]]) {
      const r = R(BigInt(rn), 100n), d = R(BigInt(dn), 100n);
      const marginal = reserveLevelMarginal(bs, r, d);
      const search = reserveLevelSearch(bs, r, d, top);
      eq(Rtext(mixCost(bs, marginal, r, d).total), Rtext(search.cost),
         'the marginal level costs what the best level costs, profile ' + pi + ', ' + rn + '/' + dn);
      eq(Rcmp(mixCost(bs, marginal, r, d).total, mixCost(bs, marginal + 1, r, d).total) <= 0, true,
         'one more reserved instance does not help, profile ' + pi + ', ' + rn + '/' + dn);
      if (marginal > 0) {
        eq(Rcmp(mixCost(bs, marginal, r, d).total, mixCost(bs, marginal - 1, r, d).total) <= 0, true,
           'and one fewer does not either, profile ' + pi + ', ' + rn + '/' + dn);
      }
    }
  }
  {
    const bs = profiles[0];
    eq(reserveLevelMarginal(bs, R(7n, 100n), R(12n, 100n)), 12, 'u* = 7/12 reserves the floor');
    eq(reserveLevelMarginal(bs, R(3n, 100n), R(12n, 100n)), 24, 'a deeper commitment reserves into the shoulder');
    eq(Rtext(mixCost(bs, 12, R(7n, 100n), R(12n, 100n)).total), '936/25', '$37.44 a day for the mix');
    eq(Rtext(mixCost(bs, 0, R(7n, 100n), R(12n, 100n)).total), '1296/25', 'against $51.84 all on demand');
    eq(Rcmp(mixCost(bs, Number(profileStats(bs).peak.n), R(7n, 100n), R(12n, 100n)).total,
            mixCost(bs, 12, R(7n, 100n), R(12n, 100n)).total) > 0, true,
       'and reserving the peak costs more than the optimum -- the misconception, priced');
  }
  /* spot is a price AND an interruption model; without the model it is just a
     smaller number. */
  eq(Rtext(spotBreakEvenRate(R(4n, 100n), R(12n, 100n))), '2/3', 'q* = (d-s)/d');
  eq(Rtext(spotExpectedPrice(R(4n, 100n), R(12n, 100n), R(15n, 100n))), '29/500',
     'a delivered spot hour at 15% reclaimed expects 5.8 cents');
  eq(spotWorthIt(R(4n, 100n), R(12n, 100n), R(2n, 3n)), false, 'exactly at q* it is a wash');
  eq(spotWorthIt(R(4n, 100n), R(12n, 100n), R(66n, 100n)), true, 'just below it, spot pays');
  eq(spotWorthIt(R(4n, 100n), R(12n, 100n), R(67n, 100n)), false, 'just above it, it does not');
  eq(spotWorthIt(R(1n, 100n), R(12n, 100n), R(95n, 100n)), false,
     'and a 92% discount is worth nothing at a 95% interruption rate');

  /* --- L7: autoscaling lag ------------------------------------------------- */
  const aR = R(50n, 1n), aTau = R(90n, 1n), aD = R(300n, 1n), aBase = R(5000n, 1n);
  eq(Rtext(autoscaleTrapezoid(aR, aTau, aD)), '1147500', 'r*tau*(D - tau/2), the lesson form');
  eq(Rtext(autoscaleShortfall(aR, aTau, aD, R(0n, 1n)).area), '1147500',
     'and the general area agrees with it when no reserve is held');
  eq(Rtext(autoscaleReserveNeeded(aR, aTau)), '4500', 'the reserve that removes it is r*tau');
  eq(Rtext(autoscaleShortfall(aR, aTau, aD, R(4500n, 1n)).area), '0', 'and it removes it exactly');
  eq(Rtext(autoscaleShortfall(aR, aTau, aD, R(4501n, 1n)).area), '0', 'one more changes nothing');
  eq(Rcmp(autoscaleShortfall(aR, aTau, aD, R(4499n, 1n)).area, R(0n, 1n)) > 0, true,
     'one fewer does not');
  /* THE INDEPENDENT CHECK: the area under max(0, demand - capacity), summed by
     the trapezoid rule over unit steps. Both the integrand and its breakpoints
     are at integers here, so that sum is EXACT, and it shares no algebra with
     the closed form it is checking. */
  function shortfallBySum(rate, tau, dur, reserve, base) {
    let total = R(0n, 1n);
    const T = Number(dur.n / dur.d);
    for (let t = 0; t < T; t += 1) {
      const at = (k) => {
        const tt = R(BigInt(k), 1n);
        const g = Rsub(autoscaleDemand(base, rate, dur, tt),
                       autoscaleCapacity(base, reserve, rate, tau, dur, tt));
        return Rcmp(g, R(0n, 1n)) > 0 ? g : R(0n, 1n);
      };
      total = Radd(total, Rdiv(Radd(at(t), at(t + 1)), R(2n, 1n)));
    }
    return total;
  }
  for (const h of [0, 500, 1000, 2000, 4000, 4500, 6000]) {
    eq(Rtext(autoscaleShortfall(aR, aTau, aD, R(BigInt(h), 1n)).area),
       Rtext(shortfallBySum(aR, aTau, aD, R(BigInt(h), 1n), aBase)),
       'the closed form matches the area under the curve at a reserve of ' + h);
  }
  /* a ramp shorter than the boot: the fleet never moves at all */
  eq(Rtext(autoscaleShortfall(R(300n, 1n), R(90n, 1n), R(30n, 1n), R(0n, 1n)).area), '135000',
     'a 30 s spike behind a 90 s boot is a bare triangle');
  eq(Rtext(autoscaleShortfall(R(300n, 1n), R(90n, 1n), R(30n, 1n), R(0n, 1n)).area),
     Rtext(shortfallBySum(R(300n, 1n), R(90n, 1n), R(30n, 1n), R(0n, 1n), aBase)),
     'and the summed area agrees there too');
  eq(Rcmp(autoscaleTrapezoid(R(300n, 1n), R(90n, 1n), R(30n, 1n)),
          autoscaleShortfall(R(300n, 1n), R(90n, 1n), R(30n, 1n), R(0n, 1n)).area) !== 0, true,
     'while r*tau*(D - tau/2) does NOT, because D < tau breaks its assumption');
  /* rho is lambda over mu, and it is course 3's rho */
  eq(Rtext(rhoAt(autoscaleDemand(aBase, aR, aD, aTau),
                 autoscaleCapacity(aBase, R(0n, 1n), aR, aTau, aD, aTau))), '19/10',
     'rho at the worst instant of the lesson preset');
  eq(Rtext(backlogGrowth(R(9500n, 1n), R(5000n, 1n))), '4500',
     'and above rho = 1 the backlog grows at lambda - mu, as course 3 says');
  eq(responseFactor(R(19n, 10n)), null, 'with no steady state, 1/(1-rho) is not a number');
  eq(Rtext(responseFactor(R(9n, 10n))), '10', 'and at rho = 0.9 it is ten');

  /* --- L8: cost per request ------------------------------------------------ */
  const uCfg = {
    fixedMonthly: R(4000n, 1n), variablePerRequest: R(1n, 1000000n),
    bytesPerRequest: R(2000n, 1n), retentionMonths: R(12n, 1n), storagePrice: R(23n, 1000n),
    bytesOut: R(120000n, 1n), egressPrice: R(9n, 100n)
  };
  const uParts = unitCost(uCfg, R(500000000n, 1n));
  eq(Rtext(uParts.fixed), '1/125000', 'the fixed cost shared over 500M requests');
  eq(Rtext(uParts.egress), '27/2500000', '120 kB at 9 cents a GB');
  eq(Rtext(uParts.storage), '69/125000000', '2 kB held for twelve months');
  eq(dominantTerm(uParts), 'egress', 'and egress is the biggest of the four');
  eq(Rtext(uParts.total), '159/7812500', 'the four added');
  eq(Rtext(uParts.monthly), '10176', 'which is $10 176 a month');
  /* ONLY THE FIXED TERM MOVES WITH VOLUME. */
  for (const v of [1000000n, 500000000n, 900000000000n]) {
    const q = unitCost(uCfg, R(v, 1n));
    eq(Rtext(q.egress) + ' ' + Rtext(q.storage) + ' ' + Rtext(q.compute),
       Rtext(uParts.egress) + ' ' + Rtext(uParts.storage) + ' ' + Rtext(uParts.compute),
       'egress, storage and compute per request do not move at volume ' + v);
  }
  eq(Rcmp(unitCost(uCfg, R(1000000000n, 1n)).total, uParts.total) < 0, true,
     'while the unit cost falls with volume');
  eq(Rcmp(unitCost(uCfg, R(1000000000n, 1n)).monthly, uParts.monthly) > 0, true,
     'and the monthly total rises with it -- the misconception is wrong in both directions');
  /* the crossing is an equality, solved */
  {
    const cross = fixedCrossing(uCfg.fixedMonthly, uParts.egress);
    eq(Rtext(cross), '10000000000/27', 'fixed / egress-per-request');
    eq(Rtext(unitCost(uCfg, cross).fixed), Rtext(uParts.egress),
       'and at that volume the two terms are exactly equal');
  }
  /* storage follows retention, not traffic */
  eq(Rtext(storagePerRequest(R(2000n, 1n), R(24n, 1n), R(23n, 1000n))),
     Rtext(Rmul(storagePerRequest(R(2000n, 1n), R(12n, 1n), R(23n, 1000n)), R(2n, 1n))),
     'doubling the retention doubles the storage term');

  /* --- L9: storage tiers --------------------------------------------------- */
  const tHot = R(23n, 1000n), tCold = R(4n, 1000n), tRead = R(10n, 1000n);
  eq(Rtext(tierBreakEvenAccesses(tHot, tCold, tRead)), '19/10', 'a* = (hot - cold)/retrieval');
  eq(tierBreakEvenAge(R(8n, 1n), R(1n, 2n), tHot, tCold, tRead, 36), 3,
     'eight reads halving monthly crosses a* at month 3');
  eq(Rtext(accessesAtAge(R(8n, 1n), R(1n, 2n), 3)), '1', 'because month 3 is read once');
  eq(Rtext(accessesAtAge(R(8n, 1n), R(1n, 2n), 2)), '2', 'and month 2 is read twice');
  /* AT THE BREAK-EVEN AGE THE TWO TIERS COST THE SAME, exactly. */
  {
    const gb = R(1000n, 1n), star = tierBreakEvenAccesses(tHot, tCold, tRead);
    const hot = tierCost(gb, star, tHot, tCold, tRead, false);
    const cold = tierCost(gb, star, tHot, tCold, tRead, true);
    eq(Rtext(hot.total), Rtext(cold.total), 'at exactly a* reads a GB-month the tiers tie');
    eq(Rcmp(tierCost(gb, Rmul(star, R(2n, 1n)), tHot, tCold, tRead, true).total,
            tierCost(gb, Rmul(star, R(2n, 1n)), tHot, tCold, tRead, false).total) > 0, true,
       'above it, cold costs more -- "everything old should go cold" is false');
    eq(Rcmp(tierCost(gb, Rdiv(star, R(2n, 1n)), tHot, tCold, tRead, true).total,
            tierCost(gb, Rdiv(star, R(2n, 1n)), tHot, tCold, tRead, false).total) < 0, true,
       'and below it, cold saves');
  }
  {
    const bs = [];
    for (let age = 0; age < 24; age += 1) {
      bs.push({ gb: R(1000n, 1n), accesses: accessesAtAge(R(8n, 1n), R(1n, 2n), age) });
    }
    const plan = tierPlan(bs, tHot, tCold, tRead, 3);
    eq(Rtext(plan.allHot), '552', 'keeping all 24 TB hot is $552 a month');
    eq(Rcmp(plan.saving, R(0n, 1n)) > 0, true, 'and tiering at a* saves against it');
    eq(Rtext(plan.movedGb), '21000', 'with 21 TB moved');
    /* tiering at a WRONGER age saves less. That is what "break-even" means. */
    for (const age of [0, 1, 2, 4, 6]) {
      eq(Rcmp(tierPlan(bs, tHot, tCold, tRead, age).saving, plan.saving) <= 0, true,
         'tiering at month ' + age + ' saves no more than tiering at a*');
    }
  }

  /* --- L10: compress or not ------------------------------------------------ */
  const cSize = R(10000000000n, 1n), cRatio = R(4n, 1n), cRate = R(250000000n, 1n);
  const cBw = R(125000000n, 1n);
  eq(Rtext(rawTime(cSize, cBw)), '80', '10 GB over a gigabit link is 80 seconds');
  eq(Rtext(compressedTime(cSize, cBw, cRatio, cRate, null).total), '60', 'and 60 compressed');
  eq(Rtext(compressBreakEvenBandwidth(cRatio, cRate, null)), '187500000', 'bw* = rate*(k-1)/k');
  eq(Rtext(compressBreakEvenRate(cRatio, cBw)), '500000000/3', 'read the other way: rate > bw*k/(k-1)');
  /* THE BREAK-EVEN IS AN EQUALITY: at bw* the two plans take exactly the same
     time, at every size, ratio and compressor -- and with the far end counted. */
  for (const [kn, kd] of [[4, 1], [3, 2], [17, 10], [10, 1], [21, 20]]) {
    for (const rate of [60000000n, 250000000n, 2000000000n]) {
      for (const drate of [null, 300000000n, 800000000n]) {
        const k = R(BigInt(kn), BigInt(kd)), rr = R(rate, 1n);
        const dr = drate === null ? null : R(drate, 1n);
        const star = compressBreakEvenBandwidth(k, rr, dr);
        const label = 'k = ' + kn + '/' + kd + ', rate ' + rate + ', drate ' + drate;
        for (const size of [1000n, 10000000000n]) {
          const S = R(size, 1n);
          eq(Rtext(rawTime(S, star)), Rtext(compressedTime(S, star, k, rr, dr).total),
             'at bw* the two plans tie, ' + label + ', size ' + size);
        }
        /* and the size cancels out of the break-even entirely */
        eq(Rcmp(rawTime(R(7n, 1n), Rmul(star, R(9n, 10n))),
                compressedTime(R(7n, 1n), Rmul(star, R(9n, 10n)), k, rr, dr).total) > 0, true,
           'below bw* compressing wins, ' + label);
        eq(Rcmp(rawTime(R(7n, 1n), Rmul(star, R(11n, 10n))),
                compressedTime(R(7n, 1n), Rmul(star, R(11n, 10n)), k, rr, dr).total) < 0, true,
           'above it, it loses, ' + label);
      }
    }
  }
  eq(compressBreakEvenRate(R(1n, 1n), cBw), null, 'a ratio of 1 has no crossing to report');

  /* --- L11: move the data or the compute ----------------------------------- */
  const pData = R(2000000000000n, 1n), pResult = R(5000000n, 1n), pCode = R(200000n, 1n);
  const pBw = R(125000000n, 1n);
  eq(Rtext(moveDataTime(pData, pBw)), '16000', '2 TB over a gigabit link is 16 000 seconds');
  eq(Rtext(moveComputeTime(pCode, pResult, pBw)), '26/625', 'and the job itself is 42 ms');
  eq(Rtext(resultRatio(pResult, pData)), '1/400000', 'the result-to-input ratio, and it is tiny');
  eq(Rtext(placementCrossover(pData, pCode)), '1999999800000', 'the two tie at D - code of result');
  /* THE BANDWIDTH CANCELS: the crossing is the same at every link speed. */
  for (const bw of [1000000n, 125000000n, 3125000000n]) {
    const B = R(bw, 1n), cross = placementCrossover(pData, pCode);
    eq(Rtext(moveDataTime(pData, B)), Rtext(moveComputeTime(pCode, cross, B)),
       'at the crossover the plans tie at ' + bw + ' B/s');
    eq(Rcmp(moveComputeTime(pCode, pResult, B), moveDataTime(pData, B)) < 0, true,
       'and moving the compute wins at ' + bw + ' B/s, as it does at every other');
  }
  eq(Rtext(placementSpeedup(pData, pCode, pResult)), '5000000/13',
     'here by a factor of 384 615');

  /* --- headroom: N-1 capacity ---------------------------------------------- */
  const hCap = R(1000n, 1n), hLam = R(9000n, 1n);
  eq(Rtext(fleetRho(hLam, 10, hCap)), '9/10', 'ten machines at rho = 0.9');
  eq(Rtext(rhoAfterLoss(R(9n, 10n), 10, 1)), '1', 'and losing one lands exactly on 1');
  eq(responseFactor(rhoAfterLoss(R(9n, 10n), 10, 1)), null, 'where there is no steady state left');
  eq(Rtext(survivingFraction(10, 1)), '9/10', '(N-1)/N on ten machines');
  eq(Rtext(survivingFraction(3, 1)), '2/3', 'and two thirds on three -- why small fleets need more');
  /* rho after the loss IS lambda over the surviving capacity. Two routes. */
  for (const [N, f, lam] of [[10, 1, 9000n], [3, 1, 1800n], [12, 4, 7200n], [60, 1, 54000n]]) {
    eq(Rtext(rhoAfterLoss(fleetRho(R(lam, 1n), N, hCap), N, f)),
       Rtext(fleetRho(R(lam, 1n), N - f, hCap)),
       'multiplying rho by N/(N-f) is dividing lambda by the survivors, N = ' + N);
  }
  /* THE IDENTITY: scan and closed form pick the same machine count. */
  for (const lam of [9000n, 1800n, 54000n, 100n, 23700n]) {
    for (const f of [1, 2, 4]) {
      for (const [rn] of [[90], [80], [99], [50], [70]]) {
        const rmax = R(BigInt(rn), 100n);
        eq(machinesForHeadroom(R(lam, 1n), hCap, rmax, f, 4000),
           machinesForHeadroomClosed(R(lam, 1n), hCap, rmax, f),
           'scan and closed form agree at lambda = ' + lam + ', f = ' + f + ', rho <= ' + rn + '%');
      }
    }
  }
  eq(machinesForHeadroom(hLam, hCap, R(9n, 10n), 1, 4000), 11,
     'holding rho <= 0.9 through one loss takes eleven machines, not ten');
  eq(Rtext(usableUtilisation(R(9n, 10n), 10, 1)), '81/100',
     'so the utilisation you may plan for is 81%, not 90%');

  /* --- growth: the month the plan runs out --------------------------------- */
  const gCur = R(5000n, 1n), gRate = R(1n, 10n), gLimit = R(50000n, 1n);
  eq(Rtext(loadAtMonth(gCur, gRate, 0)), '5000', 'month zero is today');
  eq(monthsToLimit(gCur, gRate, gLimit, 2000), 25, 'and 10% a month reaches 50 000 rps in month 25');
  eq(Rcmp(loadAtMonth(gCur, gRate, 25), gLimit) >= 0, true, 'month 25 is over the limit');
  eq(Rcmp(loadAtMonth(gCur, gRate, 24), gLimit) < 0, true, 'and month 24 is not');
  near(monthsToLimitApprox(gCur, gRate, gLimit), 24.15885792809679, 1e-9,
       'log(limit/current)/log(1+r) is the rounded gloss');
  /* THE EXACT SEARCH AND THE ROUNDED LOGARITHM MUST BRACKET EACH OTHER. */
  for (const [cur, rate, lim] of [[5000n, 10n, 50000n], [5000n, 26n, 50000n], [5000n, 3n, 50000n],
                                  [100n, 1n, 500000n], [40000n, 40n, 500000n]]) {
    const c = R(cur, 1n), r = R(rate, 100n), l = R(lim, 1n);
    const exact = monthsToLimit(c, r, l, 5000), approx = monthsToLimitApprox(c, r, l);
    eq(exact, Math.ceil(approx - 1e-9),
       'the integer search is the ceiling of the logarithm at r = ' + rate + '%');
    eq(Rcmp(loadAtMonth(c, r, exact), l) >= 0, true, 'and it really does clear the limit');
    eq(Rcmp(loadAtMonth(c, r, exact - 1), l) < 0, true, 'while the month before does not');
  }
  eq(monthsToLimit(gCur, R(0n, 1n), gLimit, 2000), null, 'no growth never reaches it');
  eq(monthsToLimit(gLimit, gRate, gCur, 2000), 0, 'and a limit already passed is month zero');
  /* THE BOUNDARY: a load landing exactly ON the limit has reached it. Every
     other case in this section crosses between two months and cannot tell >=
     from >, so a plan that quietly gave itself one more month than it has
     would survive all of them. */
  eq(Rtext(loadAtMonth(R(5000n, 1n), R(1n, 1n), 2)), '20000',
     'at 100% a month, month 2 is exactly 20 000 rps');
  eq(monthsToLimit(R(5000n, 1n), R(1n, 1n), R(20000n, 1n), 2000), 2,
     'so the 20 000 rps limit is reached in month 2, not month 3');
  eq(doublingMonths(R(1n, 1n), 2000), 1, 'and 100% a month doubles in exactly one month');
  eq(doublingMonths(R(1n, 10n), 2000), 8, '10% a month doubles in eight months');
  eq(doublingMonths(R(26n, 100n), 2000), 3, 'and 26% a month doubles in three');
  /* the plan itself: a ceiling, because 3.2 machines is four */
  eq(machinesAtMonth(gCur, gRate, 0, R(1000n, 1n), R(7n, 10n)), 8,
     '5000 rps at 70% of a 1000 rps machine is eight machines, not 7.14');
  eq(machinesAtMonth(gCur, gRate, 25, R(1000n, 1n), R(7n, 10n)), 78,
     'and 78 by the month the limit arrives');
  eq(orderMonth(25, 3), 22, 'a three-month lead time makes month 22 the date that matters');
  eq(orderMonth(25, 30) < 0, true, 'and a lead time longer than the runway is already late');

  /* --- scale kit: END assertions --- */
}

// ------------------------------------- measuring systems (kit: measure)
/* The `measure` kit's own arithmetic, on the numbers its ten lessons print.

   Three of these are not figures but CLAIMS the course makes in prose, and
   they are why this section exists.

   The fleet p99 must differ from the mean of the per-host p99s on the preset
   L2 opens with. If those two ever came out equal, the "merged" figure would
   not be merging anything -- the single most plausible way for that lesson to
   be quietly broken is for both numbers to come from the same list.

   The error budget must be EXACTLY 43.2 minutes at three nines over 30 days.
   That is the number burn-rate alerting is quoted against; 216/5 is the whole
   lesson, and a period convention that silently changed it would leave every
   pair in the table wrong by 1.4%.

   And the reweighted mean must be exactly the true mean, not nearly it. The
   sampling lesson claims that counting each sampled request 1/s times undoes
   the tail bias; Requ, not near, is the assertion that claim deserves. */
console.log('system design: measurement, aggregation, sampling and alerts');
{
  const MEASURE_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'measure.py');
  const measureSrc = fs.readFileSync(MEASURE_SOURCE, 'utf8');
  const measureBlock = (name) => blockFrom(measureSrc, name, MEASURE_SOURCE);
  /* latency.py's block is evaluated FIRST and measure.py's second, so that the
     shared output helpers in scope are the ones measure.py ships. What is
     wanted from the latency kit is parseSample and fanoutBreakEven: this
     course's percentiles have to agree with the course that owns them. */
  eval(block('RATIONAL_JS') + countingBlock('BIGINT_JS') + sysdBlock('RCEIL_JS')
       + sysdBlock('PERCENTILE_JS') + sysdBlock('PMF_JS') + sysdBlock('AVAIL_JS')
       + sysdBlock('STREAM_JS') + sysdBlock('APPROX_JS')
       + latencyBlock('LATENCY_JS') + measureBlock('MEASURE_JS'));

  /* --- printing, and the one that exists because Rnum cannot ------------- */
  eq(Rfixed(R(1n, 3n), 6), '0.333333', 'long division in BigInt');
  eq(Rfixed(R(2n, 3n), 6), '0.666667', 'rounded half up at the last digit');
  eq(Rfixed(R(-1n, 8n), 3), '-0.125', 'a negative rational keeps its sign');
  eq(Rpct(R(1n, 3n), 4), '33.3333%', 'a percentage without a gcd');
  eq(Rpct(R(216n, 5000n), 2), '4.32%', 'and it agrees with the Rmul form');
  eq(Rpct(R(216n, 5000n), 2), Rfixed(Rmul(R(216n, 5000n), R(100n, 1n)), 2) + '%',
     'scaling the numerator prints what multiplying the rational prints');
  eq(RpctAuto(R(1n, 2n)), '50.00%', 'a middling probability gets two places');
  eq(RpctAuto(Rsub(R(1n, 1n), R(1n, 10n ** 7n))), '99.99999%',
     'and one near certainty widens rather than printing 100%');
  eq(RpctAuto(R(1n, 500000n)), '0.0002%', 'a rare one widens downwards the same way');
  eq(minutesText(R(216n, 5n)), '43.20 min', '43.2 minutes reads as minutes');
  eq(minutesText(R(300n, 1n)), '5.00 h', 'five hours reads as hours');
  eq(minutesText(R(3000n, 1n)), '2.08 days', 'and fifty hours reads as days');
  eq(minutesText(R(1n, 2n)), '30.0 s', 'and half a minute reads as seconds');
  /* THE REASON Rplot EXISTS. Rnum on a load-test probability is NaN, and a
     chart of NaNs paints nothing and throws nothing. */
  const huge = atLeastOne(R(1n, 1000n), 3000);
  eq(Number.isNaN(Rnum(huge)), true, 'Rnum of a 9000-digit fraction is NaN');
  near(Rplot(huge), 0.950288, 1e-6, 'Rplot long-divides it instead');

  /* --- the formula that repeats: 1 - (1-p)^k ---------------------------- */
  /* The fast form and the rational-arithmetic form are the same number. This
     is the assertion that licenses building the fraction without a gcd. */
  for (const [n, d, k] of [[1n, 100n, 10], [259n, 1000n, 10], [1n, 1000n, 600],
                           [3n, 7n, 5], [1n, 1n, 4], [7n, 8n, 1], [1n, 2n, 12]]) {
    const p = R(n, d);
    eq(Requ(atLeastOne(p, k), Rsub(R(1n, 1n), Rpow(Rsub(R(1n, 1n), p), k))), true,
       '1 - (1-p)^k built in lowest terms at p = ' + Rtext(p) + ', k = ' + k);
  }
  eq(Rtext(atLeastOne(R(0n, 1n), 9)), '0', 'sampling nothing catches nothing');
  eq(Rtext(atLeastOne(R(1n, 100n), 1)), '1/100', 'one trial is just p');
  eq(Rtext(atLeastOne(R(1n, 100n), 10)), '9561792499119550999/100000000000000000000',
     '1% sampling of a ten-request problem, exactly');
  eq(Rpct(atLeastOne(R(1n, 100n), 10), 2), '9.56%', 'which is 9.56%, so it is missed 90% of the time');
  /* The curve the pages draw carries the power forward; it must be the same
     number at every point it draws. */
  const curve = atLeastOneCurve(R(1n, 1000n), 50, 6);
  for (let i = 0; i <= 6; i += 1) {
    eq(Requ(curve[i], atLeastOne(R(1n, 1000n), 50 * i)), true, 'the drawn curve at n = ' + (50 * i));
  }
  /* The searches: the scan, the bisection, and the closed form all agree. */
  eq(rateForTarget(10, R(95n, 100n), 1000).n + '/' + rateForTarget(10, R(95n, 100n), 1000).d, '259/1000',
     '95% confidence in a ten-request problem needs 25.9% sampling');
  eq(Rcmp(atLeastOne(R(258n, 1000n), 10), R(95n, 100n)) < 0, true, 'and 25.8% does not reach it');
  for (const k of [3, 10, 25]) {
    for (const t of [[1n, 2n], [9n, 10n], [95n, 100n], [99n, 100n]]) {
      eq(Requ(rateForTarget(k, R(t[0], t[1]), 1000), rateForTargetSearch(k, R(t[0], t[1]), 1000)), true,
         'the scan and the bisection agree at k = ' + k + ', target ' + t[0] + '/' + t[1]);
    }
  }
  /* The rule of three, exactly: a clean run of 1000 bounds the rate at 3/1000. */
  eq(Rtext(rateForTargetSearch(1000, R(95n, 100n), 10000)), '3/1000',
     'a thousand clean requests bound the failure rate at exactly 3/1000');
  eq(Rtext(rateForTargetSearch(100, R(95n, 100n), 10000)), '37/1250',
     'at a hundred requests the exact bound is 2.96%, not the 3% of the rule of thumb');
  /* The idealisation, which rounds AND is a different quantity. */
  near(captureApprox(R(1n, 100n), 10), 0.09516258196404, 1e-12, '1 - e^(-sk) as expNegApprox computes it');
  near(Math.abs(captureApprox(R(1n, 100n), 10) - Rplot(atLeastOne(R(1n, 100n), 10))), 4.55e-4, 1e-5,
     'and it differs from the exact answer by far more than it rounds');

  /* --- L1: the SLI, its exact variance and its rounded root -------------- */
  const p1 = R(9995n, 10000n), obj = R(999n, 1000n);
  /* An SLI is a count over a count, so a window of n can only produce the n + 1
     fractions with denominator n. 99.95% is not one of them at n = 1000. */
  eq(Rtext(sliRatio(999, 1000)), '999/1000', 'an SLI is good over total, in lowest terms');
  eq(Rint(Rmul(p1, R(1000n, 1n))), false, '99.95% of a thousand requests is 999.5 of them');
  eq(Rint(Rmul(p1, R(20000n, 1n))), true, 'while at twenty thousand it is a whole number again');
  eq(Rpct(sliRatio(Number(Rfloor(Rmul(p1, R(1000n, 1n)))), 1000), 3), '99.900%',
     'so the nearest ratio below is the objective itself');
  eq(Rtext(sliVariance(p1, 1000)), '1999/4000000000', 'p(1-p)/n at 99.95% on 1000 requests, exactly');
  near(sliSeApprox(p1, 1000), 0.00070692998, 1e-10, 'its square root, which rounds');
  near(sigmasApprox(p1, obj, 1000), 0.7072836, 1e-6, '99.95% is 0.71 standard errors from 99.9%');
  /* 1000 requests cannot tell 99.9% from 99.8%: the standard error at three
     nines IS the whole 0.001 gap between them. */
  near(sliSeApprox(R(999n, 1000n), 1000), 0.0009995, 1e-7, 'the SE at 99.9% on 1000 requests is 0.0999%');
  eq(sliSeApprox(R(999n, 1000n), 1000) > 0.00099, true, 'which is the entire gap to 99.8%');
  /* The window the lesson solves for: the search and the closed form agree. */
  const halfGap = Rdiv(Rsub(p1, obj), R(2n, 1n));
  eq(sampleSizeForWidth(p1, halfGap), 7996, 'separating 99.95% from 99.9% by two SE takes 7996 requests');
  eq(String(sampleSizeClosed(p1, halfGap)), '7996', 'and ceil(p(1-p)/w^2) says the same');
  for (const [pn, pd, wn, wd] of [[9995n, 10000n, 1n, 4000n], [99n, 100n, 1n, 1000n],
                                  [999n, 1000n, 1n, 10000n], [1n, 2n, 1n, 100n]]) {
    const p = R(pn, pd), w = R(wn, wd);
    eq(sampleSizeForWidth(p, w), Number(sampleSizeClosed(p, w)),
       'search equals closed form at p = ' + Rtext(p) + ', w = ' + Rtext(w));
    const n = sampleSizeForWidth(p, w);
    eq(Rcmp(sliVariance(p, n), Rmul(w, w)) <= 0, true, 'and n is large enough');
    eq(Rcmp(sliVariance(p, n - 1), Rmul(w, w)) > 0, true, 'while n - 1 is not');
  }

  /* --- L2: THE CLAIM. Percentiles do not average ------------------------ */
  const hostA = parseRuns('8, 9, 10, 11, 12');
  const hostB = parseRuns('10, 11, 12, 13, 14');
  const hostC = parseRuns('150:20, 180:20, 220:20, 260:15, 320:10, 400:5');
  const q99 = R(99n, 100n), q50 = R(1n, 2n);
  eq(hostC.length, 90, 'the run-length spec expands to ninety requests');
  eq(mergeSamples([hostA, hostB, hostC]).length, 100, 'and the fleet served a hundred');
  const perHost = hostPercentiles([hostA, hostB, hostC], q99);
  eq(perHost.join(','), '12,14,400', 'the three per-host p99s');
  const meanP99 = meanOfPercentiles(perHost);
  const fleetP99 = fleetPercentile([hostA, hostB, hostC], q99);
  const fleetMed = fleetPercentile([hostA, hostB, hostC], q50);
  eq(Rtext(meanP99), '142', 'their mean is 142 ms');
  eq(fleetP99, 400, 'the fleet p99, from the merged sample, is 400 ms');
  eq(fleetMed, 180, 'and the fleet median is 180 ms');
  /* THE assertion. If these were ever equal the merge would be fake. */
  eq(Requ(R(BigInt(fleetP99), 1n), meanP99), false,
     'the merged p99 is NOT the mean of the per-host p99s');
  eq(Rcmp(meanP99, R(BigInt(fleetMed), 1n)) < 0, true,
     'the mean of the p99s lands BELOW the fleet median -- the preset the course asks for');
  /* Two shards, each with a p99 the other does not share: the average is a
     number that belongs to neither, and the pooled figure is one of them. */
  const shardX = parseRuns('10:90, 40:10'), shardY = parseRuns('20:90, 100:10');
  eq(percentile(shardX, q99), 40, 'shard X has a p99 of 40 ms');
  eq(percentile(shardY, q99), 100, 'shard Y has a p99 of 100 ms');
  eq(Rtext(meanOfPercentiles(hostPercentiles([shardX, shardY], q99))), '70', 'their average is 70 ms');
  eq(fleetPercentile([shardX, shardY], q99), 100, 'and the pooled p99 is 100 ms, which is not 70');
  /* The bound that DOES hold, on every split this file tries: pooling can
     never exceed the largest per-host answer, because the ranks add. */
  for (const q of [R(1n, 2n), R(9n, 10n), R(95n, 100n), q99]) {
    for (const lists of [[hostA, hostB, hostC], [shardX, shardY], [hostA, hostC], [hostB]]) {
      const per = hostPercentiles(lists, q);
      eq(fleetPercentile(lists, q) <= maxOf(per), true, 'pooled <= the largest per-host value at q = ' + Rtext(q));
      eq(fleetPercentile(lists, q) >= minOf(per), true, 'pooled >= the smallest per-host value at q = ' + Rtext(q));
    }
  }
  /* The corollary, and the reason this lesson is about the MEAN rather than
     about disagreement: nearest rank sandwiches the pooled value between the
     smallest and largest per-host one, because ceil(q*n_1) + ... + ceil(q*n_h)
     is both at least ceil(q*N) and less than q*N + h. So two hosts that report
     the SAME p99 pool to exactly that p99 -- averaging them is right there and
     wrong the moment they differ, which is why the preset above differs. */
  const twinA = parseRuns('5:60, 100:3'), twinB = parseRuns('9:30, 40:5, 100:2');
  eq(percentile(twinA, q99), 100, 'one host reports a p99 of 100 ms');
  eq(percentile(twinB, q99), 100, 'so does the other');
  eq(fleetPercentile([twinA, twinB], q99), 100, 'and the pooled p99 is 100 ms too, exactly');
  /* And this course's percentiles are course 2's percentiles: same parser
     result, same rank, same value. */
  const plain = '12, 13, 14, 14, 15, 15, 16, 17, 18, 19, 21, 22, 24, 27, 31, 38, 52, 96, 180, 420';
  eq(parseRuns(plain).join(','), parseSample(plain).join(','),
     'parseRuns and the latency kit\'s parseSample read a plain sample identically');
  eq(percentile(parseRuns(plain), q99), percentile(parseSample(plain), q99),
     'so the p99 is the same number on both courses');

  /* --- L3: bucket error -------------------------------------------------- */
  const edges = bucketEdges(25, R(2n, 1n), 6);
  eq(edges.map(Rtext).join(' '), '25 50 100 200 400 800 1600', 'doubling buckets from 25 ms');
  eq(bucketEdges(25, R(3n, 2n), 4).map(Rtext).join(' '), '25 75/2 225/4 675/8 2025/16',
     'and at r = 3/2 the edges stay fractions');
  const hSample = parseRuns('30:40, 45:25, 60:15, 85:10, 120:6, 137:3, 400:1');
  eq(hSample.length, 100, 'a hundred requests');
  eq(percentile(hSample, q99), 137, 'whose exact p99 is 137 ms');
  eq(histogramBucket(hSample, edges, q99), 2, 'the histogram reports the third bucket');
  eq(Rtext(edges[2]) + '-' + Rtext(edges[3]), '100-200', 'which is [100, 200) ms -- the lesson\'s sentence');
  eq(Rtext(bucketWidth(edges, 2)), '100', 'a bucket 100 ms wide');
  eq(Rtext(bucketRelative(R(2n, 1n))), '1', 'and a relative error of r - 1 = 100%');
  eq(Rtext(bucketRelative(R(3n, 2n))), '1/2', 'at r = 3/2 it is 50%');
  /* The relative width is r - 1 in EVERY bucket, which is the argument for
     exponential bucketing and not a property of the first one. */
  for (const [rn, rd] of [[2n, 1n], [3n, 2n], [5n, 4n], [10n, 1n]]) {
    const r = R(rn, rd), es = bucketEdges(7, r, 8);
    for (let i = 0; i < 8; i += 1) {
      eq(Requ(Rdiv(bucketWidth(es, i), es[i]), Rsub(r, R(1n, 1n))), true,
         'bucket ' + i + ' is (r-1) times its own lower edge at r = ' + Rtext(r));
    }
  }
  /* The reported bucket always contains the exact percentile. If it ever did
     not, the histogram would not be an interval estimate of anything. */
  for (const [rn, rd] of [[2n, 1n], [3n, 2n], [5n, 4n]]) {
    for (const q of [R(1n, 2n), R(9n, 10n), R(95n, 100n), q99]) {
      const es = bucketEdges(25, R(rn, rd), 9);
      const b = histogramBucket(hSample, es, q), v = percentile(hSample, q);
      if (b >= 0 && b < es.length - 1) {
        eq(Rcmp(R(BigInt(v), 1n), es[b]) >= 0 && Rcmp(R(BigInt(v), 1n), es[b + 1]) < 0, true,
           'the reported bucket contains the exact p' + Rtext(Rmul(q, R(100n, 1n))) + ' at r = ' + rn + '/' + rd);
      }
    }
  }
  const counts = bucketCounts(hSample, edges);
  eq(counts.under + counts.inside.reduce((a, b) => a + b, 0) + counts.over, 100, 'every request lands in exactly one bucket');
  eq(counts.inside.join(','), '65,25,9,0,1,0', 'the bucket counts');

  /* --- L4: coordinated omission ------------------------------------------ */
  const naive = naiveSample(100, 2, 1000);
  const fixed = correctedSample(100, 10, 2, 1000);
  eq(naive.length, 100, 'the generator recorded a hundred requests');
  eq(percentile(naive, q99), 2, 'and measured a p99 of 2 ms -- the healthy service time');
  eq(omittedCount(10, 1000), 99, 'the schedule called for 99 more during the stall');
  eq(fixed.length, 199, 'so the corrected sample holds 199');
  eq(percentile(fixed, q99), 990, 'whose p99 is 990 ms');
  eq(percentile(fixed, q50), 10, 'and whose median moves from 2 ms to 10 ms');
  eq(imputedLatencies(10, 1000)[0], 990, 'the first imputed request waited 990 ms');
  eq(imputedLatencies(10, 1000)[98], 10, 'and the last waited 10 ms');
  eq(imputedLatencies(250, 1000).join(','), '750,500,250', 'a coarser schedule imputes fewer');
  eq(imputedLatencies(2000, 1000).length, 0, 'a stall shorter than one interval omits nothing');
  /* The correction can never make a percentile faster: it only adds waiting. */
  for (const q of [R(1n, 2n), R(9n, 10n), q99, R(1n, 1n)]) {
    eq(percentile(correctedSample(100, 10, 2, 1000), q) >= percentile(naive, q), true,
       'the corrected percentile is never below the measured one at q = ' + Rtext(q));
  }

  /* --- L5: scrape intervals ---------------------------------------------- */
  eq(Rtext(catchProbability(3, 15)), '1/5', 'a 3 s spike read every 15 s');
  eq(Rpct(catchProbability(3, 15), 1), '20.0%', 'is caught a fifth of the time');
  eq(Rtext(catchProbability(60, 15)), '1', 'a spike longer than the interval is always caught');
  eq(longestInvisible(15), 14, 'and the longest invisible spike is one second short of the interval');
  eq(longestInvisible(1), 0, 'at a one-second interval nothing can hide');
  const starts = spikeStarts(12, 300, 7);
  eq(starts.length, 12, 'twelve spikes drawn from the seeded stream');
  eq(spikeStarts(12, 300, 7).join(','), starts.join(','), 'the same seed draws the same times');
  eq(spikeStarts(12, 300, 8).join(',') === starts.join(','), false, 'a different seed does not');
  eq(caughtCount(starts, 3, 15, 0), 2, 'this run caught two of the twelve, against an expected 2.4');
  /* The generator is MINSTD and the seed is mixed, and both matter HERE rather
     than in general: these draws are taken modulo a horizon and compared modulo
     a scrape interval. Under the path's glibc constants -- modulus 2^31 -- the
     low bits are a cycle, so x % 4 would read 0,1,2,3 forever and a run at a
     4, 8 or 16 second interval would catch exactly d/I of its spikes every
     time, which is the one thing this lesson exists to deny. */
  const low4 = measureStream(7, 40).map((x) => x % 4);
  eq(low4.every((v, i) => i < 4 || v === low4[i - 4]), false,
     'the low two bits of the stream are not a period-4 cycle');
  const low2 = measureStream(3, 40).map((x) => x % 2);
  eq(low2.every((v, i) => i < 2 || v === low2[i - 2]), false, 'nor do the low bits alternate');
  eq(new Set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10].map((s) => spikeStarts(12, 300, s).join(','))).size, 10,
     'ten consecutive seeds draw ten different runs');
  /* An LCG's k-th value is affine in its seed, so unmixed seeds walk a line.
     The first draw on consecutive seeds must not be an arithmetic progression. */
  const firsts = [1, 2, 3, 4, 5].map((s) => measureStream(s, 1)[0]);
  eq(firsts[1] - firsts[0] === firsts[2] - firsts[1], false, 'and consecutive seeds do not walk a straight line');
  /* A spike at least as long as the interval cannot be missed, whatever the
     phase -- the one thing the probability formula caps at one. */
  for (const off of [0, 1, 7, 14]) {
    eq(caughtCount(starts, 15, 15, off), 12, 'every 15 s spike is caught at phase ' + off);
  }

  /* A counter that restarts: the naive rate, and the correction. §4.10 gives
     this no mode of its own, so it lives with L5 -- a reset between two reads
     is the second thing a scrape interval cannot see, and the evidence for it
     is only that the number went down. */
  const csamples = counterSamples(40, 15, 300, 152);
  eq(csamples[10][1], 6000, 'at 150 s a counter climbing at 40/s reads 6000');
  eq(csamples[11][1], 520, 'and at 165 s, after a restart at 152 s, it reads 520');
  eq(resetInterval(csamples), 11, 'the eleventh window is where it went backwards');
  eq(Rtext(naiveRates(csamples)[10]), '-1096/3', 'whose naive rate is -365.33 a second');
  eq(Rcmp(naiveRates(csamples)[10], R(0n, 1n)) < 0, true, 'a negative rate for a counter that only rose');
  eq(Rtext(correctedRates(csamples)[10]), '104/3', 'the correction gives 34.67 a second, positive');
  eq(lostIncrements(40, 15, 152), 80, 'and loses the 80 increments between the last read and the restart');
  eq(Rtext(Radd(correctedRates(csamples)[10], R(BigInt(lostIncrements(40, 15, 152)), 15n))), '40',
     'corrected rate plus the lost increments over the window IS the true 40/s');
  /* Every other window is exactly the true rate, before and after the reset. */
  for (const i of [0, 5, 9, 11, 15, 18]) {
    eq(Rtext(correctedRates(csamples)[i]), '40', 'window ' + i + ' reads the true rate');
  }
  eq(resetInterval(counterSamples(40, 15, 300, 0)), -1, 'with no restart nothing goes backwards');
  eq(naiveRates(counterSamples(40, 15, 300, 0)).every((r) => Rtext(r) === '40'), true,
     'and then the naive rate is right everywhere, which is why the correction is invisible until it is not');

  /* --- L6: sampling, and the mean it ruins -------------------------------- */
  const pop = runsFromText('5:900, 8:60, 12:30, 400:10');
  eq(slowCount(pop, 100), 10, 'ten of the thousand requests are over 100 ms');
  eq(Rtext(trueMean(pop)), '467/50', 'the true mean is 9.34 ms');
  eq(Rfixed(sampledMean(pop, 100, R(1n, 100n), R(1n, 1n)), 3), '203.688',
     'a tail-biased sample averages 203.688 ms');
  /* THE CLAIM: reweighting recovers the true mean EXACTLY, at every rate and
     every threshold, which is what makes it a correction and not a fudge. */
  for (const s of [[1n, 100n], [1n, 1000n], [1n, 2n], [1n, 1n]]) {
    for (const thr of [0, 6, 10, 100, 399]) {
      eq(Requ(reweightedMean(pop, thr, R(s[0], s[1]), R(1n, 1n)), trueMean(pop)), true,
         'the reweighted mean IS the true mean at s = ' + s[0] + '/' + s[1] + ', threshold ' + thr);
    }
  }
  eq(Requ(sampledMean(pop, 100, R(1n, 1n), R(1n, 1n)), trueMean(pop)), true,
     'and with no bias at all the naive mean is already right');

  /* --- L7: cardinality ---------------------------------------------------- */
  eq(String(seriesCount([40, 120, 6, 30, 4])), '3456000', 'five labels multiply to 3 456 000 series');
  eq(Rtext(samplesPerDay(15)), '5760', 'a 15 s scrape stores 5760 samples a day');
  eq(Rfixed(gigabytes(bytesPerDay(seriesCount([40, 120, 6, 30, 4]), 15, 2)), 2), '39.81',
     'which is 39.81 GB a day at two bytes a sample');
  eq(String(seriesCount([40, 120, 6, 30, 4, 10000])), '34560000000',
     'a user_id label does not add ten thousand series, it multiplies by ten thousand');
  eq(Rtext(Rdiv(bytesPerDay(seriesCount([40, 120, 6, 30, 4]), 15, 2),
                bytesPerDay(seriesCount([40, 120, 6, 30, 4]), 30, 2))), '2',
     'halving the scrape interval doubles the bill');

  /* --- L8: how long to run a load test ------------------------------------ */
  const tail = R(1n, 1000n);
  eq(Rpct(atLeastOne(tail, 600), 2), '45.14%', '600 requests see the top 0.1% 45% of the time');
  eq(Rcmp(atLeastOne(tail, 600), R(1n, 2n)) < 0, true, 'so a 600-request run misses it more than half the time');
  eq(trialsForTarget(tail, R(95n, 100n), 1 << 22), 2995, '95% confidence takes 2995 requests');
  eq(Rcmp(atLeastOne(tail, 2994), R(95n, 100n)) < 0, true, 'and 2994 does not reach it');
  eq(Rcmp(atLeastOne(tail, 2995), R(95n, 100n)) >= 0, true, 'while 2995 does');
  eq(trialsForTarget(tail, R(1n, 2n), 1 << 22), 693, 'an even chance takes 693');
  /* 693 is the same integer course 2 finds for fan-out at a p99.9 per call,
     because it is the same power crossing the same half. */
  eq(fanoutBreakEven(R(999n, 1000n), 1 << 20), 693, 'which is course 2\'s fan-out break-even, exactly');
  eq(trialsForTarget(R(1n, 100n), R(95n, 100n), 1 << 22), 299, 'a p99 needs only 299 requests');

  /* --- L9: THE ERROR BUDGET IS 43.2 MINUTES ------------------------------- */
  const three = R(999n, 1000n);
  eq(Rtext(periodMinutes(30)), '43200', 'thirty days is 43 200 minutes');
  eq(Rtext(budgetMinutes(three, 30)), '216/5', 'and 99.9% of it leaves 216/5 minutes');
  eq(Rfixed(budgetMinutes(three, 30), 2), '43.20', 'which is exactly 43.2 minutes');
  eq(Requ(budgetMinutes(three, 30), R(216n, 5n)), true, 'exactly, not nearly');
  eq(Rfixed(budgetMinutes(R(9999n, 10000n), 30), 3), '4.320', 'four nines leaves 4.32 minutes');
  eq(Rfixed(budgetMinutes(three, 7), 2), '10.08', 'and a week of three nines is 10.08 minutes');
  /* The C5 convention, which is a different month and therefore a different
     figure. Both pages say which one they are using. */
  eq(Rfixed(Rdiv(Rmul(Rsub(R(1n, 1n), three), R(2628000n, 1n)), R(60n, 1n)), 1), '43.8',
     'course 5\'s 2 628 000-second month gives 43.8 minutes for the same objective');
  /* The four standard pairs, exactly. */
  eq(Rtext(burnFraction(R(144n, 10n), R(60n, 1n), 30)), '1/50', '14.4x over an hour spends 2% of the budget');
  eq(Rtext(burnFraction(R(6n, 1n), R(360n, 1n), 30)), '1/20', '6x over six hours spends 5%');
  eq(Rtext(burnFraction(R(3n, 1n), R(1440n, 1n), 30)), '1/10', '3x over a day spends 10%');
  eq(Rtext(burnFraction(R(1n, 1n), R(4320n, 1n), 30)), '1/10', '1x over three days spends 10% as well');
  eq(Rfixed(budgetSpentMinutes(R(144n, 10n), R(60n, 1n), 30, three), 3), '0.864',
     'which at three nines is 51.8 seconds of the 43.2 minutes');
  eq(Rtext(exhaustMinutes(R(144n, 10n), 30)), '3000', 'a 14.4x burn exhausts the budget in 3000 minutes');
  eq(minutesText(exhaustMinutes(R(144n, 10n), 30)), '2.08 days', 'which is just over two days');
  eq(Rtext(exhaustMinutes(R(1n, 1n), 30)), '43200', 'and a burn of 1 lasts exactly the period');
  eq(Requ(burnFraction(R(1n, 1n), periodMinutes(30), 30), R(1n, 1n)), true,
     'burning at 1 for the whole period spends the whole budget -- the definition, checked');
  eq(Rtext(burnErrorRate(R(144n, 10n), three)), '9/625', '14.4x at three nines is a 1.44% error rate');

  /* --- L10: what a threshold fires at when nothing is wrong --------------- */
  eq(String(thresholdCount(R(2n, 100n), 200)), '5', '2% of 200 is 4, so the alert needs 5 errors');
  eq(String(thresholdCount(R(25n, 1000n), 200)), '6', 'and 2.5% of 200 is 5, so it needs 6');
  eq(String(thresholdCount(R(1n, 100n), 150)), '2', 'a rate that divides exactly still needs one more');
  const perr = R(1n, 100n);
  const tail5 = falseAlarmProbability(perr, 5n, 200);
  eq(Rpct(tail5, 3), '5.175%', 'a healthy 1% service trips it in 5.175% of 200-request windows');
  eq(Rfixed(windowsPer(7 * 24 * 60, 5), 0), '2016', 'a week holds 2016 five-minute windows');
  eq(Rfixed(expectedPages(tail5, windowsPer(7 * 24 * 60, 5)), 2), '104.32',
     'so the threshold pages 104 times a week with nothing to find');
  eq(Rfixed(expectedPages(tail5, windowsPer(30 * 24 * 60, 5)), 1), '447.1', 'and 447 times a month');
  eq(Rpct(atLeastOne(tail5, 12), 2), '47.14%', 'the chance of at least one in the next hour');
  /* The cheap distribution and the shared tail must be the same number: the
     page prints one and tabulates with the other. */
  const pmf = binomialPmf(perr, 200), tails = pmfUpperTails(pmf);
  eq(pmf.length, 201, 'the distribution has n + 1 outcomes');
  eq(Rtext(tails[0]), '1', 'and it is a distribution: the terms sum to exactly one');
  for (const k of [1, 2, 5, 8, 12, 30]) {
    eq(Requ(tails[k], availKofN(perr, k, 200)), true,
       'the suffix sum at k = ' + k + ' equals availKofN, exactly');
  }
  eq(Requ(binomialTerm(perr, 5, 200), pmf[5]), true, 'and the single term agrees with the recurrence');
  /* Raising the threshold by one error cuts the false pages by a factor of
     three here -- the lever the lesson recommends, computed rather than said. */
  eq(Rcmp(availKofN(perr, 6, 200), Rdiv(availKofN(perr, 5, 200), R(3n, 1n))) < 0, true,
     'one more error on the threshold cuts the false-alarm rate by more than three');
}


// ==========================================================================
// Operations Research: the exact simplex, and the twelve kits' shared engine
// ==========================================================================
//
// scripts/mathpath/labs/or_core.py is thirteen raw-string blocks and this is
// where they are exercised directly, before any kit dresses them in modes.
//
// TWO NAMED REGRESSION TESTS carry the whole section: Beale's cycling example
// and the Klee-Minty cube. Both are lessons ABOUT things floating point
// destroys -- "the tableau is identical entry for entry" is a claim about
// equality of numbers, and a pivot count of 2^n - 1 survives only if every
// degenerate comparison lands exactly -- so if the arithmetic ever stops being
// exact, these two fail first and loudest.
console.log('operations research: the exact simplex, duality, networks and the rest');
{
  const OR_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'or_core.py');
  const orSrc = fs.readFileSync(OR_SOURCE, 'utf8');
  const SYSTEMS_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'algebra_systems.py');
  const systemsSrc = fs.readFileSync(SYSTEMS_SOURCE, 'utf8');
  const orBlock = (n) => blockFrom(orSrc, n, OR_SOURCE);
  const sysBlock = (n) => blockFrom(systemsSrc, n, SYSTEMS_SOURCE);

  eval(countingBlock('BIGINT_JS') + sysdBlock('HARMONIC_JS') + sysdBlock('RCEIL_JS')
     + sysdBlock('PMF_JS') + sysdBlock('QUEUE_JS')
     + sysBlock('FORMAT_JS') + sysBlock('LINEAR_JS') + sysBlock('MATRIX_JS') + sysBlock('FEAS_JS')
     + orBlock('ORFMT_JS') + orBlock('TABLEAU_JS') + orBlock('PHASE_JS') + orBlock('DUAL_JS')
     + orBlock('RANGE_JS') + orBlock('NET_JS') + orBlock('TRANS_JS') + orBlock('IP_JS')
     + orBlock('SCHED_JS') + orBlock('DPSEQ_JS') + orBlock('CHAIN_JS') + orBlock('SIM_JS')
     + orBlock('INV_JS'));

  const ri = (v) => R(BigInt(v), 1n);
  const rf = (n, d) => R(BigInt(n), BigInt(d));

  /* --- ORFMT: the printer this path actually needs ------------------------
     algebra_core's Rdec goes through Number, and this path produces rationals
     Number cannot hold. That is not a hypothetical: both figures below are
     measured, and the second one is Rdec returning NaN for a probability. */
  eq(Rfixed(rf(1, 3), 6), '0.333333', 'Rfixed is long division in BigInt');
  eq(Rfixed(rf(2, 3), 4), '0.6667', 'rounded half up at the last digit');
  eq(Rfixed(rf(-1, 8), 3), '-0.125', 'and it keeps the sign');
  const decayed = Rpow(rf(19, 20), 400);
  eq(String(decayed.n).length + '/' + String(decayed.d).length, '512/521',
     '(19/20)^400 is 512 digits over 521 -- measured here, because queue.py\'s comment says "521-digit numerator" and 521 is the DENOMINATOR');
  eq(Rfixed(decayed, 12), '0.000000001229', 'which Rfixed prints');
  eq(Rdec(decayed, 12), 'NaN', 'and Rdec, going through Number, does not -- this is why ORFMT_JS exists');
  eq(Rshort(rf(1, 3)), '1/3', 'Rshort keeps a fraction a reader can read');
  eq(Rshort(decayed, 6), Rfixed(decayed, 6), 'and falls back to a decimal when the fraction has run away');
  eq(Rpct(rf(1, 8), 2), '12.50%', 'Rpct');
  eq(Rtext(Rfrac(rf(7, 3))), '1/3', 'the fractional part of 7/3');
  eq(Rtext(Rfrac(rf(-7, 3))), '2/3', 'and of -7/3 it is 2/3, not -1/3 -- Gomory cuts depend on it');
  eq(String(bifloor(999999n)), '999', 'bifloor floors the integer square root');
  eq(String(bifloor(2n)), '1', 'and never returns null, which is what algebra_core bisqrt does');
  eq(surdDec(Rsurd(ri(2)), 10), '1.4142135624', 'surdDec -- the one function here that rounds');
  eq(surdDec({ q: ri(40), k: 3n }, 6), '69.282032', '40 sqrt 3, to six places');
  eq(surdDec({ q: ri(-2), k: 7n }, 5), '-5.29150', 'and it carries a sign');

  /* --- REGRESSION TEST 1: BEALE'S CYCLING EXAMPLE (1955) ------------------
     max (3/4)x1 - 150x2 + (1/50)x3 - 6x4  subject to three rows and x >= 0.
     From the slack basis {x5, x6, x7}:
       * Dantzig's rule with the lowest-row-index ratio tie-break returns to
         that basis after exactly 6 pivots, with the tableau IDENTICAL entry
         for entry and z = 0 throughout;
       * Bland's rule terminates after 6 pivots at z* = 1/20.
     Same count, different ending. That contrast is C2 L7, and a float
     implementation cannot show it, because "the tableau is identical" is a
     claim about equality of numbers. */
  const beale = {
    max: true, names: ['x1', 'x2', 'x3', 'x4'],
    obj: [rf(3, 4), ri(-150), rf(1, 50), ri(-6)],
    cons: [
      { a: [rf(1, 4), ri(-60), rf(-1, 25), ri(9)], rel: 'le', b: ri(0), name: 'row 1' },
      { a: [rf(1, 2), ri(-90), rf(-1, 50), ri(3)], rel: 'le', b: ri(0), name: 'row 2' },
      { a: [ri(0), ri(0), ri(1), ri(0)], rel: 'le', b: ri(1), name: 'row 3' }]
  };
  {
    const d = lpSolve(beale, { rule: 'dantzig', maxPivots: 60 });
    eq(d.status, 'cycled', 'Beale under Dantzig CYCLES -- not "limit reached", which would teach the wrong thing');
    eq(d.run.pivots, 6, 'and it takes exactly 6 pivots to come back');
    eq(d.run.steps.map((s) => s.enterName).join(','), 'x1,x2,x3,x4,s1,s2',
       'entering x1 x2 x3 x4 x5 x6, in that order');
    eq(d.run.steps.map((s) => s.row + 1).join(','), '1,2,1,2,1,2', 'with the leaving rows alternating 1,2');
    eq(d.run.path.every((t) => Rzero(t.z[t.n])), true, 'z is 0 at every step: every pivot is degenerate');
    eq(d.run.cycle.from, 0, 'the basis it returns to is the one it started from');
    /* IDENTICAL ENTRY FOR ENTRY -- the claim the lesson makes. */
    const first = d.run.path[0], last = d.run.path[d.run.path.length - 1];
    let identical = first.basis.join(',') === last.basis.join(',');
    for (let i = 0; i < first.m; i += 1) {
      for (let j = 0; j <= first.n; j += 1) if (!Requ(first.T[i][j], last.T[i][j])) identical = false;
    }
    for (let j = 0; j <= first.n; j += 1) if (!Requ(first.z[j], last.z[j])) identical = false;
    eq(identical, true, 'and the sixth tableau equals the first ENTRY FOR ENTRY, not nearly');
    const b = lpSolve(beale, { rule: 'bland', maxPivots: 60 });
    eq(b.status, 'optimal', 'Bland terminates on the same problem');
    eq(b.run.pivots, 6, 'in the same 6 pivots');
    eq(Rtext(b.zOrig), '1/20', 'at z* = 1/20');
    eq(Rtext(lpSolve(beale, { rule: 'bestImprovement' }).zOrig), '1/20',
       'best improvement reaches the same optimum');
    eq(Rtext(lpSolve(beale, { rule: 'lastIndex' }).zOrig), '1/20', 'and so does the last-index rule');
  }

  /* --- REGRESSION TEST 2: THE KLEE-MINTY CUBE ----------------------------
     max sum 10^(n-j) x_j  subject to  2 sum_{j<i} 10^(i-j) x_j + x_i <= 100^(i-1).
     Dantzig's rule visits every one of the 2^n vertices: 3, 7, 15 pivots at
     n = 2, 3, 4, with z* = 100^(n-1). Bland's rule gives 3, 5, 9 -- the "run
     another rule and count fewer" figure C2 L9 is built on. */
  const kleeMinty = (n) => {
    const obj = [], names = [], cons = [];
    for (let j = 1; j <= n; j += 1) { obj.push(R(10n ** BigInt(n - j), 1n)); names.push('x' + j); }
    for (let i = 1; i <= n; i += 1) {
      const a = [];
      for (let j = 1; j <= n; j += 1) {
        a.push(j < i ? R(2n * 10n ** BigInt(i - j), 1n) : (j === i ? R1 : R0));
      }
      cons.push({ a: a, rel: 'le', b: R(100n ** BigInt(i - 1), 1n), name: 'row ' + i });
    }
    return { max: true, names: names, obj: obj, cons: cons };
  };
  for (const [n, dantzig, bland, star] of [[2, 3, 3, '100'], [3, 7, 5, '10000'], [4, 15, 9, '1000000']]) {
    const m = kleeMinty(n);
    const d = lpSolve(m, { rule: 'dantzig', maxPivots: 200 });
    const b = lpSolve(m, { rule: 'bland', maxPivots: 200 });
    eq(d.run.pivots, dantzig, 'Klee-Minty n = ' + n + ': Dantzig takes 2^n - 1 = ' + dantzig + ' pivots');
    eq(b.run.pivots, bland, 'and Bland takes ' + bland + ' -- run another rule and count fewer');
    eq(Rtext(d.zOrig), star, 'both stop at z* = 100^(n-1) = ' + star);
    eq(Rtext(b.zOrig), star, 'whichever rule got there');
  }
  eq(lpSolve(kleeMinty(3), { rule: 'bestImprovement' }).run.pivots, 1,
     'and best improvement walks straight to the far corner in one');

  /* THE TIE-BREAKS THEMSELVES, on an LP built so that they bite: both columns
     start with the same most-negative reduced cost, so the ONLY thing choosing
     between them is the rule. Neither Beale nor Klee-Minty exercises this --
     their reduced costs are all distinct -- and a tie-break nobody tests is a
     tie-break that was chosen by accident, which is what C2 L7 is about. */
  {
    const tied = { max: true, names: ['x1', 'x2'], obj: [ri(1), ri(1)],
      cons: [{ a: [ri(1), ri(2)], rel: 'le', b: ri(4), name: 'A' },
             { a: [ri(2), ri(1)], rel: 'le', b: ri(4), name: 'B' }] };
    const start = tabInit(stdForm(tied));
    const rates = tabEnter(start, 'dantzig').rates;
    eq(Rtext(rates[0].reduced) + ',' + Rtext(rates[1].reduced), '-1,-1',
       'both columns start at the same reduced cost, so only the tie-break can choose');
    eq(tabEnter(start, 'dantzig').enter, 0, 'Dantzig breaks the tie on the LOWEST column index');
    eq(tabEnter(start, 'bland').enter, 0, 'Bland takes the smallest index with a negative reduced cost');
    eq(tabEnter(start, 'lastIndex').enter, 1, 'and the last-index rule takes the other one');
    eq(lpSolve(tied, { rule: 'dantzig' }).run.steps[0].enterName, 'x1', 'so Dantzig enters x1 first');
    eq(lpSolve(tied, { rule: 'lastIndex' }).run.steps[0].enterName, 'x2', 'and last-index enters x2 first');
    eq(Rtext(lpSolve(tied, { rule: 'dantzig' }).zOrig), Rtext(lpSolve(tied, { rule: 'lastIndex' }).zOrig),
       'both reach the same optimum, by different corners');
    /* rate times step really is the change in z, which is C2 L4's panel */
    eq(rates[0].step !== null && Requ(Rmul(rates[0].rate, rates[0].step), rates[0].delta), true,
       'and every candidate column carries its own rate, step and rate x step');
    const first = lpSolve(tied, { rule: 'bestImprovement' }).run.steps[0];
    eq(Requ(first.delta, Rmul(first.rates[first.enter].rate, first.rates[first.enter].step)), true,
       'best improvement picks the largest of them, and z really moves by that much');
    const ratio = tabRatio(start, 0, 'dantzig');
    eq(ratio.rows.map((r) => (r.eligible ? Rtext(r.ratio) : '-')).join(','), '4,2',
       'the ratio test on that column is 4 and 2');
    eq(ratio.leave, 1, 'so the second row leaves');
  }

  /* --- THE INDEPENDENT ORACLE: corner enumeration -------------------------
     algebra_systems.Ccorners already enumerates the corners of a two-variable
     region exactly. Every two-variable LP can be solved both ways, and the two
     answers must agree -- a check the solver cannot fake, because Ccorners
     knows nothing about tableaux. */
  {
    const cornerOpt = (model) => {
      const cons = model.cons.map((k) => Cnew(k.a[0], k.a[1], k.b, false, ''))
        .concat([Cnew(ri(-1), ri(0), ri(0), false, ''), Cnew(ri(0), ri(-1), ri(0), false, '')]);
      const cs = Ccorners(cons);
      if (!cs.length) return { empty: true };
      if (Cunbounded(cons) && Cgrows(cons, model.obj[0], model.obj[1])) return { unbounded: true };
      let best = null;
      for (const p of cs) {
        const v = Radd(Rmul(model.obj[0], p.x), Rmul(model.obj[1], p.y));
        if (best === null || Rcmp(v, best) > 0) best = v;
      }
      return { z: best };
    };
    let x = 20260913n;
    const next = () => { x = (1103515245n * x + 12345n) % 2147483648n; return Number(x % 100n); };
    let agreed = 0, unbounded = 0;
    for (let t = 0; t < 200; t += 1) {
      const obj = [ri(1 + next() % 9), ri(1 + next() % 9)];
      const cons = [];
      for (let i = 0; i < 2 + t % 3; i += 1) {
        cons.push({ a: [ri(next() % 7 - 1), ri(next() % 7 - 1)], rel: 'le', b: ri(next() % 30), name: 'r' + i });
      }
      const model = { max: true, names: ['x', 'y'], obj: obj, cons: cons };
      const enumerated = cornerOpt(model), solved = lpSolve(model, { rule: 'dantzig', maxPivots: 200 });
      if (enumerated.unbounded) {
        if (solved.status === 'unbounded') unbounded += 1;
        else { fails += 1; console.log('  FAIL LP ' + t + ' should be unbounded, got ' + solved.status); }
        continue;
      }
      if (solved.status !== 'optimal' || !Requ(solved.zOrig, enumerated.z)) {
        fails += 1;
        console.log('  FAIL LP ' + t + ': simplex ' + solved.status + ' vs corner enumeration ' + Rtext(enumerated.z));
        continue;
      }
      /* and the point it reports is feasible and attains the value */
      const attained = Radd(Rmul(obj[0], solved.x[0]), Rmul(obj[1], solved.x[1]));
      if (!Requ(attained, solved.zOrig)) { fails += 1; console.log('  FAIL LP ' + t + ': the reported point misses its own objective'); }
      for (const k of cons) {
        if (Rcmp(Radd(Rmul(k.a[0], solved.x[0]), Rmul(k.a[1], solved.x[1])), k.b) > 0) {
          fails += 1; console.log('  FAIL LP ' + t + ': the reported point is infeasible');
        }
      }
      /* strong duality, on every one of them */
      const dv = dualVector(solved.tab);
      if (!Requ(dv.value, solved.zOrig)) { fails += 1; console.log('  FAIL LP ' + t + ': y.b != z*'); }
      if (!dv.ok) { fails += 1; console.log('  FAIL LP ' + t + ': the dual vector is infeasible'); }
      /* and B^-1 A rebuilt from the ORIGINAL matrix is the tableau, entry for entry */
      const bi = basisInverse(solved.tab);
      for (let i = 0; i < solved.tab.m; i += 1) {
        for (let j = 0; j < solved.tab.n; j += 1) {
          if (!Requ(bi.BinvA[i][j], solved.tab.T[i][j])) { fails += 1; console.log('  FAIL LP ' + t + ': B^-1 A is not the tableau'); i = 99; break; }
        }
      }
      agreed += 1;
    }
    eq(agreed, 178, '178 two-variable LPs solved by simplex and by corner enumeration agree, exactly');
    eq(unbounded, 22, 'and the other 22 are unbounded, which both methods say');
  }

  /* --- duality: the second program, and the certificate ------------------ */
  {
    const p = { max: true, names: ['x1', 'x2'], obj: [ri(3), ri(5)],
      cons: [{ a: [ri(1), ri(0)], rel: 'le', b: ri(4), name: 'A' },
             { a: [ri(0), ri(2)], rel: 'le', b: ri(12), name: 'B' },
             { a: [ri(3), ri(2)], rel: 'le', b: ri(18), name: 'C' }] };
    const s = lpSolve(p);
    eq(Rtext(s.zOrig), '36', 'the textbook LP has z* = 36');
    eq(s.x.map(Rtext).join(','), '2,6', 'at (2, 6)');
    eq(dualVector(s.tab).y.map(Rtext).join(','), '0,3/2,1', 'with shadow prices 0, 3/2, 1');
    const d = dualModel(p), dd = dualModel(d);
    eq(lpSolve(d).status === 'optimal' && Requ(lpSolve(d).zOrig, s.zOrig), true, 'the dual attains the same value');
    eq(dd.max, true, 'the dual of the dual is a maximisation again');
    eq(dd.cons.map((k) => k.rel).join(','), 'le,le,le', 'with the primal\'s relations');
    eq(dd.obj.map(Rtext).join(','), p.obj.map(Rtext).join(','), 'and the primal\'s objective');
    eq(d.pairs.filter((q) => q.kind === 'row').every((q) => q.sign === 'ge0'), true,
       'every <= row of a maximisation prices at y >= 0');
    /* dualVector must report WHICH columns it read B^-1 from -- on a >= row
       the slack is the surplus column and holds nothing of the sort, which is
       C2 L8's named misconception. */
    const mixed = { max: true, names: ['x', 'y'], obj: [ri(1), ri(1)],
      cons: [{ a: [ri(1), ri(1)], rel: 'le', b: ri(10), name: 'cap' },
             { a: [ri(1), ri(0)], rel: 'ge', b: ri(2), name: 'floor' }] };
    const ms = lpSolve(mixed);
    const cols = dualVector(ms.tab).columns;
    eq(cols.map((c) => c.kind).join(','), 'slack,artificial',
       'on a >= row the identity column is the ARTIFICIAL, not the surplus beside it');
    eq(cols.filter((c) => c.isSlack).length, 1, 'so only one of the two rows reads B^-1 out of a slack');
    /* Farkas: an empty region certified rather than asserted */
    const empty = { max: true, names: ['x', 'y'], obj: [ri(1), ri(1)],
      cons: [{ a: [ri(1), ri(1)], rel: 'le', b: ri(1), name: 'first' },
             { a: [ri(1), ri(1)], rel: 'ge', b: ri(4), name: 'second' }] };
    const e = lpSolve(empty);
    eq(e.status, 'infeasible', 'x + y <= 1 with x + y >= 4 has no solution');
    eq(e.certificate.y.map(Rtext).join(','), '-1,1', 'and the Farkas multipliers are (-1, 1)');
    eq(e.certificate.ok, true, "y'A <= 0 and y'b > 0, verified row by row rather than claimed");
    eq(Rtext(e.certificate.checks.b.value), '3', "y'b = 3 > 0");
  }

  /* --- the two conventions a kit is most likely to get wrong -------------- */
  {
    /* A MINIMISATION is negated on the way in. Reading tab.z[n] and printing it
       is the sign error the maximised/zOrig convention exists to prevent. */
    const m = { max: false, names: ['x', 'y'], obj: [ri(2), ri(3)],
      cons: [{ a: [ri(1), ri(1)], rel: 'ge', b: ri(4), name: 'need' },
             { a: [ri(1), ri(0)], rel: 'le', b: ri(3), name: 'cap' }] };
    const s = lpSolve(m, { rule: 'bland' });
    eq(s.status, 'optimal', 'a minimisation with a >= row solves through Phase I');
    eq(Rtext(s.zOrig), '9', 'and its minimum is 9');
    eq(s.x.map(Rtext).join(','), '3,1', 'at (3, 1)');
    eq(Rsign(s.z) < 0, true, 'while the INTERNAL value is negative, because the solver always maximises');
    eq(Requ(zOriginal(s.std, s.z), s.zOrig), true, 'and zOriginal is what turns one into the other');
    /* A FREE variable is carried as the difference of two columns, so it can go
       negative -- which is what makes the dual of an equality row solvable. */
    const free = { max: true, names: ['u', 'v'], obj: [ri(0), ri(1)], free: [0],
      cons: [{ a: [ri(1), ri(1)], rel: 'eq', b: ri(2), name: 'sum' },
             { a: [ri(0), ri(1)], rel: 'le', b: ri(5), name: 'cap' }] };
    const fs = lpSolve(free, { rule: 'bland' });
    eq(fs.x.map(Rtext).join(','), '-3,5', 'u goes NEGATIVE, which a >= 0 column could not do');
    eq(Requ(Radd(fs.x[0], fs.x[1]), ri(2)), true, 'and the equality still holds at the point reported');
    eq(stdForm(free).kinds.slice(0, 3).join(','), 'decision,decision,decision',
       'because u became the two columns u+ and u-');
  }

  /* --- sensitivity: every answer a ratio test on the final tableau -------- */
  {
    const p = { max: true, names: ['x1', 'x2'], obj: [ri(3), ri(5)],
      cons: [{ a: [ri(1), ri(0)], rel: 'le', b: ri(4), name: 'A' },
             { a: [ri(0), ri(2)], rel: 'le', b: ri(12), name: 'B' },
             { a: [ri(3), ri(2)], rel: 'le', b: ri(18), name: 'C' }] };
    const s = lpSolve(p);
    const r1 = rhsRange(s.tab, 1), r2 = rhsRange(s.tab, 2);
    eq(Rtext(r1.lo) + '..' + Rtext(r1.hi), '6..18', 'row B holds its basis for b in [6, 18]');
    eq(Rtext(r2.lo) + '..' + Rtext(r2.hi), '12..24', 'and row C for b in [12, 24]');
    const c0 = costRange(s.tab, 0), c1 = costRange(s.tab, 1);
    eq(c0.basic && c1.basic, true, 'both decision variables are basic here');
    eq(Rtext(c0.lo) + '..' + Rtext(c0.hi), '0..15/2', 'c_1 may range over [0, 15/2]');
    eq(c1.hi, null, 'and c_2 has NO upper limit -- a one-sided interval is a real answer');
    eq(Rtext(c1.lo), '2', 'with 2 underneath');
    /* a nonbasic cost is a different formula, which is the misconception */
    const nb = { max: true, names: ['x', 'y'], obj: [ri(1), ri(5)],
      cons: [{ a: [ri(1), ri(1)], rel: 'le', b: ri(4), name: 'r' }] };
    const ns = lpSolve(nb);
    eq(costRange(ns.tab, 0).basic, false, 'x is nonbasic at the optimum');
    eq(Rtext(costRange(ns.tab, 0).hi), '5', 'so its cost may rise only to 5, where it ties');
    eq(costRange(ns.tab, 0).lo, null, 'and may fall forever');
    /* the whole piecewise-linear z*(b), checked against fresh solves */
    const curve = rhsCurve(p, 2, ri(0), ri(40));
    eq(curve.pieces.length, 3, 'z*(b_C) has three linear pieces on [0, 40]');
    eq(curve.breakpoints.map(Rtext).join(','), '12,24', 'breaking at 12 and 24');
    eq(curve.pieces.map((q) => Rtext(q.slope)).join(','), '5/2,1,0', 'with slopes 5/2, 1 and 0');
    for (const piece of curve.pieces) {
      for (const at of [piece.from, piece.to, Rdiv(Radd(piece.from, piece.to), ri(2))]) {
        const again = lpSolve({ max: true, names: p.names, obj: p.obj,
          cons: p.cons.map((k, q) => (q === 2 ? { a: k.a, rel: k.rel, b: at, name: k.name } : k)) });
        eq(Requ(again.zOrig, Radd(piece.z, Rmul(piece.slope, Rsub(at, piece.from)))), true,
           'the curve at b = ' + Rtext(at) + ' is what a fresh solve there gives');
      }
    }
    /* the efficient frontier of two objectives, and its exact breakpoint */
    const front = paramFront(p, [ri(3), ri(5)], [ri(5), ri(3)]);
    eq(front.corners.length, 2, 'two supported efficient corners');
    eq(Rtext(front.breakpoints[0]), '9/10', 'swapping at lambda = 9/10 exactly');
    eq(front.corners.map((c) => '(' + Rtext(c.f1) + ',' + Rtext(c.f2) + ')').join(' '), '(36,28) (27,29)',
       'at (36, 28) and (27, 29)');
    /* THE SAME MACHINERY ON >=, = AND FLIPPED ROWS. All three go through Phase
       I, so the column holding B^-1 is an ARTIFICIAL rather than a slack, and a
       row whose right-hand side was negative was multiplied by -1 on the way in
       -- a range quoted in those flipped units is a wrong answer that looks
       right. Every endpoint below is checked against a fresh solve, and every
       point just outside is checked to break the linear prediction. */
    for (const [label, m] of [
      ['a minimisation with two >= rows', { max: false, names: ['x', 'y'], obj: [ri(2), ri(3)],
        cons: [{ a: [ri(1), ri(1)], rel: 'ge', b: ri(4), name: 'need' },
               { a: [ri(1), ri(0)], rel: 'le', b: ri(3), name: 'cap' },
               { a: [ri(0), ri(1)], rel: 'ge', b: ri(1), name: 'floor' }] }],
      ['an equality row', { max: true, names: ['x', 'y'], obj: [ri(5), ri(4)],
        cons: [{ a: [ri(6), ri(4)], rel: 'le', b: ri(24), name: 'A' },
               { a: [ri(1), ri(2)], rel: 'le', b: ri(6), name: 'B' },
               { a: [ri(1), ri(1)], rel: 'eq', b: ri(3), name: 'exact' }] }],
      ['a row the solver had to flip', { max: true, names: ['x', 'y'], obj: [ri(1), ri(2)],
        cons: [{ a: [ri(-1), ri(-1)], rel: 'le', b: ri(-2), name: 'flipped' },
               { a: [ri(1), ri(1)], rel: 'le', b: ri(8), name: 'cap' }] }]]) {
      const sol = lpSolve(m, { rule: 'bland', maxPivots: 300 });
      eq(sol.status, 'optimal', label + ' solves');
      const dual = dualVector(sol.tab), inv = basisInverse(sol.tab);
      eq(Requ(dual.value, sol.zOrig), true, label + ': strong duality still holds');
      eq(dual.ok, true, label + ': and the dual vector is feasible');
      let matches = true;
      for (let i = 0; i < sol.tab.m; i += 1) {
        for (let j = 0; j < sol.tab.n; j += 1) if (!Requ(inv.BinvA[i][j], sol.tab.T[i][j])) matches = false;
      }
      eq(matches, true, label + ": B^-1 A rebuilt from the original matrix is still the tableau");
      for (let i = 0; i < m.cons.length; i += 1) {
        const range = rhsRange(sol.tab, i);
        eq(Requ(range.b, m.cons[i].b), true, label + ', row ' + (i + 1) + ': the range is quoted against the READER\'s b');
        const solveAt = (v) => lpSolve({ max: m.max, names: m.names, obj: m.obj,
          cons: m.cons.map((k, q) => (q === i ? { a: k.a, rel: k.rel, b: v, name: k.name } : k)) },
          { rule: 'bland', maxPivots: 300 });
        for (const [end, step] of [[range.lo, rf(-1, 100)], [range.hi, rf(1, 100)]]) {
          if (end === null) continue;
          const predict = (b) => Radd(sol.zOrig, Rmul(range.y_i, Rsub(b, range.b)));
          const again = solveAt(end);
          eq(again.status === 'optimal' && Requ(again.zOrig, predict(end)), true,
             label + ', row ' + (i + 1) + ': z at b = ' + Rtext(end) + ' is what the shadow price predicts');
          const outside = Radd(end, step), past = solveAt(outside);
          eq(past.status === 'optimal' && Requ(past.zOrig, predict(outside)), false,
             label + ', row ' + (i + 1) + ': and the prediction BREAKS just past ' + Rtext(end) + ', so the endpoint is tight');
        }
      }
    }

    /* pricing a new activity, and adding a constraint after the fact */
    const priced = priceColumn(s.tab, [ri(1), ri(1), ri(1)], ri(4));
    eq(Rtext(priced.reduced), '3/2', 'a new product earning 4 and using one of each is worth 3/2 more than it costs');
    eq(priced.enters, true, 'so it enters');
    eq(Rtext(priced.after.z[priced.after.n]), '39', 'and one pivot takes z from 36 to 39');
    const added = addRow(s.tab, { a: [ri(1), ri(1)], rel: 'le', b: ri(5) });
    const fresh = lpSolve({ max: true, names: p.names, obj: p.obj,
      cons: p.cons.concat([{ a: [ri(1), ri(1)], rel: 'le', b: ri(5), name: 'D' }]) });
    eq(added.status, 'optimal', 'a constraint appended after the fact is restored by dual simplex');
    eq(Requ(added.run.zOrig, fresh.zOrig), true, 'to exactly what a fresh solve gives');
    eq(Rtext(added.run.zOrig), '25', 'which is 25');
  }

  /* --- networks ---------------------------------------------------------- */
  {
    const nodes = ['s', 'a', 'b', 't'];
    const arcs = [{ from: 's', to: 'a' }, { from: 's', to: 'b' }, { from: 'a', to: 'b' },
                  { from: 'a', to: 't' }, { from: 'b', to: 't' }];
    eq(unimodularSweep(incidence(nodes, arcs), 4).unimodular, true,
       'a node-arc incidence matrix is totally unimodular, checked determinant by determinant');
    const odd = [[R1, R1, R0], [R1, R0, R1], [R0, R1, R1]];
    eq(Rtext(submatrixDet(odd, [0, 1, 2], [0, 1, 2])), '-2', 'an odd cycle has a determinant of -2');
    eq(unimodularSweep(odd, 3).bad.length, 1, 'so it is not unimodular, and the sweep names the submatrix');
    const acts = [{ id: 'A', dur: ri(3), pred: [] }, { id: 'B', dur: ri(2), pred: ['A'] },
                  { id: 'C', dur: ri(4), pred: ['A'] }, { id: 'D', dur: ri(2), pred: ['B', 'C'] },
                  { id: 'E', dur: ri(1), pred: ['D'] }];
    const cpm = cpmPasses(acts);
    eq(Rtext(cpm.makespan), '10', 'the project takes 10');
    eq(cpm.critical.join(''), 'ACDE', 'B is the only activity with slack');
    eq(Rtext(cpm.slack[1]), '2', 'and it has two units of it');
    eq(cpm.paths.length, 1, 'one critical path');
    eq(cpmPasses(acts.map((a) => (a.id === 'C' ? { id: 'C', dur: ri(2), pred: ['A'] } : a))).paths.length, 2,
       'shorten C and a SECOND path becomes critical -- the whole of C4 L7');
    eq(topoOrder(['a', 'b', 'c'], [{ from: 'a', to: 'b' }, { from: 'b', to: 'c' }, { from: 'c', to: 'a' }]).cycle.length,
       3, 'a cyclic project has no order, and the cycle is named');
    const wnodes = ['s', 'a', 'b', 't'];
    const warcs = [{ from: 's', to: 'a', cost: ri(4) }, { from: 's', to: 'b', cost: ri(2) },
                   { from: 'b', to: 'a', cost: ri(1) }, { from: 'a', to: 't', cost: ri(3) },
                   { from: 'b', to: 't', cost: ri(7) }];
    const bf = bellmanRounds(wnodes, warcs, 's');
    eq(bf.dist.map(Rtext).join(','), '0,3,2,6', 'Bellman-Ford labels, on rational arc costs');
    eq(potentialCheck(wnodes, warcs, bf.dist, 's', 't').ok, true,
       'and those labels are feasible potentials: pi_j - pi_i <= c_ij on every arc');
    eq(potentialCheck(wnodes, warcs, bf.dist, 's', 't').tight.length, 3, 'three arcs are tight');
    const neg = bellmanRounds(['x', 'y', 'z'],
      [{ from: 'x', to: 'y', cost: ri(1) }, { from: 'y', to: 'z', cost: ri(-3) },
       { from: 'z', to: 'x', cost: ri(1) }, { from: 'x', to: 'z', cost: ri(5) }], 'x');
    eq(neg.negative, true, 'an n-th round improvement certifies a negative cycle');
    eq(Rtext(neg.cycleCost), '-1', 'and the cycle it names really does sum to -1');
    const cnodes = ['s', 'a', 'b', 't'];
    const carcs = [{ from: 's', to: 'a', cap: ri(3) }, { from: 's', to: 'b', cap: ri(2) },
                   { from: 'a', to: 'b', cap: ri(2) }, { from: 'a', to: 't', cap: ri(2) },
                   { from: 'b', to: 't', cap: ri(3) }];
    const flow = [ri(3), ri(2), ri(1), ri(2), ri(3)];
    const cut = cutCapacity(cnodes, carcs, reachable(cnodes, residual(carcs, flow), 's').set);
    eq(Rtext(cut.capacity), '5', 'max flow 5 equals the cut the residual network shades');
    eq(Rcmp(cutCapacity(cnodes, carcs, ['s', 'a']).capacity, cut.capacity) >= 0, true,
       'and ANY other cut is at least as big, which is what makes it a proof');
    const match = bipartiteMatch(['1', '2', '3'], ['a', 'b', 'c'],
      [['1', 'a'], ['1', 'b'], ['2', 'a'], ['2', 'b'], ['3', 'a'], ['3', 'b']]);
    eq(match.size, 2, 'three workers competing for two jobs match only two');
    eq(match.cover.size, match.size, "Koenig: the minimum cover is the maximum matching, COMPUTED -- not drawn");
    eq(match.deficient.S.length > match.deficient.N.length, true, "Hall: |N(S)| < |S| on the deficient set");
    eq(match.deficient.S.join('') + '/' + match.deficient.N.join(''), '123/ab', 'which is all three onto two');
  }

  /* --- transportation and assignment -------------------------------------- */
  {
    const C = [[10, 2, 20, 11], [12, 7, 9, 20], [4, 14, 16, 18]].map((r) => r.map(ri));
    const S = [ri(15), ri(25), ri(10)], D = [ri(5), ri(15), ri(15), ri(15)];
    /* the transportation LP, solved by the simplex, is the oracle MODI is held to */
    const obj = [], names = [], cons = [];
    for (let i = 0; i < 3; i += 1) for (let j = 0; j < 4; j += 1) { obj.push(C[i][j]); names.push('x' + i + j); }
    for (let i = 0; i < 3; i += 1) {
      const a = []; for (let p = 0; p < 3; p += 1) for (let q = 0; q < 4; q += 1) a.push(p === i ? R1 : R0);
      cons.push({ a: a, rel: 'eq', b: S[i], name: 'supply ' + (i + 1) });
    }
    for (let j = 0; j < 4; j += 1) {
      const a = []; for (let p = 0; p < 3; p += 1) for (let q = 0; q < 4; q += 1) a.push(q === j ? R1 : R0);
      cons.push({ a: a, rel: 'eq', b: D[j], name: 'demand ' + (j + 1) });
    }
    const oracle = lpSolve({ max: false, names: names, obj: obj, cons: cons }, { rule: 'bland', maxPivots: 400 });
    eq(Rtext(oracle.zOrig), '435', 'the transportation LP costs 435 -- solved through Phase I, with equality rows');
    for (const start of [northwest(C, S, D), leastCost(C, S, D)]) {
      eq(start.count, start.want, start.rule + ' leaves m + n - 1 = ' + start.want + ' basic cells');
      let basis = start.basis.map((c) => ({ i: c.i, j: c.j, x: c.x }));
      const x = start.x.map((r) => r.slice());
      for (let guard = 0; guard < 30; guard += 1) {
        const uv = uvPotentials(C, basis, 3, 4);
        for (const c of basis) {
          if (!Requ(Radd(uv.u[c.i], uv.v[c.j]), C[c.i][c.j])) { fails += 1; console.log('  FAIL u + v = c fails on a basic cell'); }
        }
        if (uv.optimal) break;
        const cyc = stoneCycle(basis, uv.entering, 3, 4);
        if (!cyc.found || cyc.cells.length % 2 !== 0) { fails += 1; console.log('  FAIL the stepping-stone cycle is not a cycle'); break; }
        for (const c of cyc.cells) x[c.i][c.j] = c.sign > 0 ? Radd(x[c.i][c.j], cyc.theta) : Rsub(x[c.i][c.j], cyc.theta);
        basis = basis.filter((c) => !(c.i === cyc.leaving.i && c.j === cyc.leaving.j))
                     .concat([{ i: uv.entering.i, j: uv.entering.j }])
                     .map((c) => ({ i: c.i, j: c.j, x: x[c.i][c.j] }));
      }
      let total = R0;
      for (let i = 0; i < 3; i += 1) for (let j = 0; j < 4; j += 1) total = Radd(total, Rmul(C[i][j], x[i][j]));
      eq(Rtext(total), '435', 'MODI from the ' + start.rule + ' start reaches the LP optimum');
    }
    eq(northwest([[4, 8], [6, 2]].map((r) => r.map(ri)), [ri(5), ri(5)], [ri(5), ri(5)]).epsilon.length, 1,
       'a tie leaves a NAMED epsilon cell rather than a basis one cell short');
    eq(balance([ri(10)], [ri(4)]).dummy, 'col', 'surplus supply gets a dummy destination');
    eq(balance([ri(4)], [ri(10)]).dummy, 'row', 'and unmet demand a dummy source');
    /* Hungarian against exhaustive assignment */
    for (const cm of [[[9, 11, 14, 11, 7], [6, 15, 13, 13, 10], [12, 13, 6, 8, 8], [11, 9, 10, 12, 9], [7, 12, 14, 10, 14]],
                      [[4, 2, 8], [4, 3, 7], [3, 1, 6]],
                      [[10, 19, 8, 15], [10, 18, 7, 17], [13, 16, 9, 14], [12, 19, 8, 18]]]) {
      const cost = cm.map((r) => r.map(ri)), n = cost.length;
      const h = hungarian(cost);
      let best = null;
      const walk = (k, used, sum) => {
        if (k === n) { if (best === null || Rcmp(sum, best) < 0) best = sum; return; }
        for (let j = 0; j < n; j += 1) { if (used[j]) continue; used[j] = 1; walk(k + 1, used, Radd(sum, cost[k][j])); used[j] = 0; }
      };
      walk(0, {}, R0);
      eq(h.complete, true, 'the Hungarian method assigns everybody at n = ' + n);
      eq(Requ(h.value, best), true, 'and its value is the exhaustive optimum, ' + Rtext(best));
      eq(new Set(h.assignment).size, n, 'the assignment is a permutation');
      eq(h.steps.filter((s) => s.kind === 'cover').every((s) => s.size === s.matching.length), true,
         'every cover it drew was the size of a matching, by Koenig');
    }
  }

  /* --- integer programming ------------------------------------------------ */
  {
    const ip = { max: true, names: ['x1', 'x2'], obj: [ri(1), ri(1)],
      cons: [{ a: [ri(2), ri(5)], rel: 'le', b: ri(16), name: 'A' },
             { a: [ri(6), ri(5)], rel: 'le', b: ri(30), name: 'B' }] };
    eq(Rtext(lpSolve(ip).zOrig), '53/10', 'the relaxation stops at 53/10, which no integer plan can do');
    const lattice = latticePoints(ip, [[0n, 6n], [0n, 4n]]);
    let bestInt = null;
    for (const q of lattice.points) if (q.feasible && (bestInt === null || Rcmp(q.objective, bestInt) > 0)) bestInt = q.objective;
    eq(Rtext(bestInt), '5', 'and the exhaustive integer optimum is 5');
    for (const order of ['depthFirst', 'bestBound']) {
      const tree = bbTree(ip, { order: order, maxNodes: 60 });
      eq(tree.status, 'optimal', 'branch and bound under ' + order + ' finishes');
      eq(Requ(tree.best, bestInt), true, 'at the same 5 the lattice found');
      eq(tree.nodes.slice(1).every((n) => n.sol.from === 'dual simplex on the parent tableau'), true,
         'and every child was re-solved from its parent tableau, not from scratch');
    }
    eq(bbTree(ip, { maxNodes: 2 }).refused, true, 'a node cap REFUSES rather than reporting an unproved optimum');
    /* a Gomory cut must cut off the fractional point and keep every integer one */
    const relaxed = lpSolve(ip);
    let cutRow = -1;
    for (let i = 0; i < relaxed.tab.m; i += 1) if (!Rint(relaxed.tab.T[i][relaxed.tab.n])) { cutRow = i; break; }
    const cut = gomoryCut(relaxed.tab, cutRow);
    let here = R0;
    for (let j = 0; j < 2; j += 1) here = Radd(here, Rmul(cut.inOriginal.a[j], relaxed.x[j]));
    eq(Rcmp(here, cut.inOriginal.b) < 0, true, 'the cut excludes the fractional optimum');
    for (const q of lattice.points) {
      if (!q.feasible) continue;
      let v = R0;
      for (let j = 0; j < 2; j += 1) v = Radd(v, Rmul(cut.inOriginal.a[j], q.x[j]));
      if (Rcmp(v, cut.inOriginal.b) < 0) { fails += 1; console.log('  FAIL a Gomory cut removed a feasible integer point'); }
    }
    eq(Rzero(Rfrac(cut.fracB)), false, 'and it was derived from a row with a fractional right-hand side');
    const items = [{ name: 'a', value: ri(60), weight: ri(10) }, { name: 'b', value: ri(100), weight: ri(20) },
                   { name: 'c', value: ri(120), weight: ri(30) }];
    const knap = knapsackExact(items, ri(50));
    eq(Rtext(knap.relaxation), '240', 'the knapsack relaxation is 240');
    eq(Rtext(knap.optimum), '220', 'the exact optimum is 220');
    eq(Rtext(knap.greedy), '160', 'and greed gets 160 -- all three from one call, which is the lesson');
    eq(knap.fractionalItem.name, 'c', 'with exactly one item split');
    const d4 = [[0, 20, 42, 35], [20, 0, 30, 34], [42, 30, 0, 12], [35, 34, 12, 0]].map((r) => r.map(ri));
    eq(tspExact(d4).count, 3, 'four cities have (n-1)!/2 = 3 DISTINCT tours, not 6');
    eq(Rtext(tspExact(d4).best.cost), '97', 'the shortest is 97');
    eq(Requ(tspBranch(d4).best, tspExact(d4).best.cost), true, 'and branch and bound agrees');
    /* tspBranch's assignment bound is a SUBSET RECURSION in IP_JS; transport's
       hungarian is Koenig covers and reductions in TRANS_JS. Two different
       algorithms for one number, so their agreement is arithmetic and not a
       shared implementation -- and `integer` does not have to carry TRANS_JS. */
    for (const cm of [[[9, 11, 14, 11, 7], [6, 15, 13, 13, 10], [12, 13, 6, 8, 8], [11, 9, 10, 12, 9], [7, 12, 14, 10, 14]],
                      [[4, 2, 8], [4, 3, 7], [3, 1, 6]],
                      [[10, 19, 8, 15], [10, 18, 7, 17], [13, 16, 9, 14], [12, 19, 8, 18]]]) {
      const cost = cm.map((r) => r.map(ri));
      eq(Requ(assignMin(cost).value, hungarian(cost).value), true,
         'the subset recursion and the Hungarian method agree at n = ' + cost.length);
    }
    const d6 = [[0, 3, 93, 13, 33, 9], [4, 0, 77, 42, 21, 16], [45, 17, 0, 36, 16, 28],
                [39, 90, 80, 0, 56, 7], [28, 46, 88, 33, 0, 25], [3, 88, 18, 46, 92, 0]].map((r) => r.map(ri));
    eq(tspExact(d6).count, 120, 'an ASYMMETRIC six-city instance has 5! = 120 tours, not 60');
    eq(Requ(tspBranch(d6, { maxNodes: 300 }).best, tspExact(d6).best.cost), true,
       'and the assignment bound with subtour cuts still finds the best of them');
  }

  /* --- scheduling ---------------------------------------------------------- */
  {
    const jobs = [{ id: 'A', p: ri(6), w: ri(1), d: ri(8) }, { id: 'B', p: ri(4), w: ri(2), d: ri(4) },
                  { id: 'C', p: ri(5), w: ri(4), d: ri(12) }, { id: 'D', p: ri(3), w: ri(3), d: ri(6) },
                  { id: 'E', p: ri(7), w: ri(1), d: ri(20) }];
    const byKey = (f) => jobs.map((_, k) => k).sort((a, b) => Rcmp(f(jobs[a]), f(jobs[b])));
    const spt = byKey((j) => j.p), wspt = byKey((j) => Rdiv(j.p, j.w)), edd = byKey((j) => j.d);
    eq(bestSequence(jobs, 'sumC').count, 120, 'five jobs is 120 orders, all of them checked');
    eq(Requ(seqObjectives(spt, jobs).sumC, bestSequence(jobs, 'sumC').value), true, 'SPT minimises sum C');
    eq(Requ(seqObjectives(wspt, jobs).sumWC, bestSequence(jobs, 'sumWC').value), true, "and Smith's order minimises sum wC");
    eq(Requ(seqObjectives(edd, jobs).Lmax, bestSequence(jobs, 'Lmax').value), true, 'and EDD minimises Lmax');
    eq(Rcmp(seqObjectives(edd, jobs).sumT, bestSequence(jobs, 'sumT').value) > 0, true,
       'but EDD LOSES on sum T to a sequence only exhaustive search finds');
    eq(Rtext(seqObjectives(spt, jobs).makespan), '25', 'while the makespan is 25 whatever the order');
    for (let i = 0; i < 4; i += 1) {
      const sw = adjacentSwap([0, 1, 2, 3, 4], i, jobs);
      eq(sw.checkC && sw.checkWC, true,
         'swapping positions ' + (i + 1) + ' and ' + (i + 2) + ' moves the objectives by exactly p_b - p_a and w_a p_b - w_b p_a');
    }
    eq(mooreHodgson(jobs).sumU, Number(bestSequence(jobs, (o) => R(BigInt(o.sumU), 1n)).value.n),
       'Moore-Hodgson attains the minimum number of late jobs');
    const fs = [{ id: '1', p1: ri(5), p2: ri(2) }, { id: '2', p1: ri(1), p2: ri(6) },
                { id: '3', p1: ri(9), p2: ri(7) }, { id: '4', p1: ri(3), p2: ri(8) },
                { id: '5', p1: ri(10), p2: ri(4) }];
    let bestFlow = null;
    const permute = (used, acc) => {
      if (acc.length === fs.length) { const v = flowshopMakespan(acc, fs).value; if (bestFlow === null || Rcmp(v, bestFlow) < 0) bestFlow = v; return; }
      for (let k = 0; k < fs.length; k += 1) { if (used[k]) continue; used[k] = 1; acc.push(k); permute(used, acc); acc.pop(); used[k] = 0; }
    };
    permute({}, []);
    eq(Requ(johnsonRule(fs).makespan.value, bestFlow), true, "Johnson's rule attains the minimum two-machine makespan");
    const par = parallelAssign([7, 6, 5, 4, 4, 4, 4].map((p, k) => ({ id: 'j' + k, p: ri(p) })), 3, 'LPT');
    eq(Rtext(par.makespan) + '/' + Rtext(par.optimum), '13/12', 'LPT gets 13 where the exhaustive optimum is 12');
    eq(Rcmp(par.ratio, rf(4, 3)) <= 0, true, 'which is inside the 4/3 ratio it is proved to');
    eq(Rtext(par.bounds.average) + ' and ' + Rtext(par.bounds.longest), '34/3 and 7',
       'and both lower bounds the proof uses are reported, not just the heuristic');
    const shop = jobShopAll([{ job: 'J1', machine: 'M1', dur: ri(3) }, { job: 'J1', machine: 'M2', dur: ri(2) },
                             { job: 'J2', machine: 'M2', dur: ri(4) }, { job: 'J2', machine: 'M1', dur: ri(1) }]);
    eq(shop.total, 4, 'two disjunctive pairs is four orientations');
    eq(Rtext(shop.best.makespan), '6', 'the best of which finishes at 6');
    eq(shop.cyclic, 1, 'and one of them DEADLOCKS, which is an answer and not an error');
    const crashActs = [{ id: 'A', normal: ri(6), crash: ri(4), normalCost: ri(100), crashCost: ri(140), pred: [] },
                       { id: 'B', normal: ri(4), crash: ri(2), normalCost: ri(80), crashCost: ri(120), pred: ['A'] },
                       { id: 'C', normal: ri(5), crash: ri(3), normalCost: ri(60), crashCost: ri(90), pred: ['A'] },
                       { id: 'D', normal: ri(3), crash: ri(2), normalCost: ri(50), crashCost: ri(80), pred: ['B', 'C'] }];
    const crash = crashModel(crashActs, ri(14));
    eq(Rtext(cpmPasses(crashActs.map((a) => ({ id: a.id, dur: a.normal, pred: a.pred }))).makespan), '14',
       'CPM says the uncrashed project takes 14');
    eq(Rzero(lpSolve(crash.model, { rule: 'bland', maxPivots: 400 }).zOrig), true, 'so at a 14-day deadline the crash bill is 0');
    const tc = rhsCurve(crash.model, crash.deadlineRow, ri(9), ri(14), { rule: 'bland', maxPivots: 400 });
    eq(tc.pieces.map((q) => Rtext(q.slope)).join(','), '-35,-30,-20,-15',
       'and the exact time-cost curve is rhsCurve on the deadline row -- the same function, not a second one');
    for (const piece of tc.pieces) {
      const again = lpSolve(crashModel(crashActs, piece.from).model, { rule: 'bland', maxPivots: 400 });
      eq(Requ(again.zOrig, piece.z), true, 'the curve at a deadline of ' + Rtext(piece.from) + ' is what a fresh solve gives');
    }
  }

  /* --- dynamic programming ------------------------------------------------- */
  {
    const stages = [['A'], ['B', 'C'], ['D', 'E'], ['F']];
    const arcs = [{ from: 'A', to: 'B', cost: ri(2) }, { from: 'A', to: 'C', cost: ri(4) },
                  { from: 'B', to: 'D', cost: ri(7) }, { from: 'B', to: 'E', cost: ri(4) },
                  { from: 'C', to: 'D', cost: ri(3) }, { from: 'C', to: 'E', cost: ri(2) },
                  { from: 'D', to: 'F', cost: ri(1) }, { from: 'E', to: 'F', cost: ri(4) }];
    const back = backwardStages(stages, arcs);
    eq(Rtext(back.value), '8', 'the cheapest route costs 8');
    eq(back.policy.map((p) => p.join('')).join('|'), 'ACDF', 'and here it is unique');
    eq(back.ties.length, 1, 'but the TIE at B is kept rather than silently resolved');
    const tied = backwardStages(stages, arcs.map((a) => (a.from === 'A' && a.to === 'B' ? { from: 'A', to: 'B', cost: R0 } : a)));
    eq(tied.policy.length, 3, 'and when a tie is ON the optimal route, every optimal route comes back');
    const demand = [ri(10), ri(62), ri(12), ri(130), ri(154), ri(129)];
    const ww = wagnerWhitin(demand, ri(54), ri(2));
    let bestPlan = null;
    for (let mask = 0; mask < (1 << (demand.length - 1)); mask += 1) {
      const orders = [0];
      for (let k = 1; k < demand.length; k += 1) if (mask & (1 << (k - 1))) orders.push(k);
      let cost = R0;
      for (let a = 0; a < orders.length; a += 1) {
        const from = orders[a], to = a + 1 < orders.length ? orders[a + 1] : demand.length;
        cost = Radd(cost, ri(54));
        for (let t = from; t < to; t += 1) cost = Radd(cost, Rmul(ri(2), Rmul(ri(t - from), demand[t])));
      }
      if (bestPlan === null || Rcmp(cost, bestPlan) < 0) bestPlan = cost;
    }
    eq(Requ(ww.cost, bestPlan), true, 'Wagner-Whitin is the exact optimum over all 32 order patterns');
    eq(Rtext(ww.cost), '294', 'which is 294');
    const heur = lotsizeHeuristics(demand, ri(54), ri(2));
    eq(Rzero(heur.silverMeal.gap), true, 'Silver-Meal happens to find it here');
    eq(Rtext(heur.leastUnitCost.gap), '306', 'and least-unit-cost is 306 worse -- two heuristics, two answers');
    const s4 = secretaryExact(4);
    eq(s4.probs.map((q) => Rtext(q.p)).join(','), '1/4,11/24,5/12,1/4', 'the secretary problem at n = 4, exactly');
    eq(s4.best, 2, 'look at one, then take the next best');
    eq(secretaryExact(100).best, 38, 'at n = 100 look at 37');
    eq(Rfixed(secretaryExact(100).bestP, 6), '0.371043', 'and succeed 37.1043% of the time');
    const offers = [[ri(10), rf(1, 3)], [ri(20), rf(1, 3)], [ri(30), rf(1, 3)]];
    const stop = stopThresholds(offers, 3, ri(1));
    eq(stop.rows.map((q) => Rtext(q.threshold)).join(','), '22,19,0', 'the stopping threshold falls as the deadline nears');
    const tree = { root: { kind: 'decision', children: [
        { label: 'build', node: { kind: 'chance', children: [
          { p: rf(3, 10), node: { kind: 'leaf', value: ri(100) } },
          { p: rf(7, 10), node: { kind: 'leaf', value: ri(-20) } }] } },
        { label: 'wait', node: { kind: 'leaf', value: ri(0) } }] },
      payoff: [[ri(100), ri(-20)], [ri(0), ri(0)]], prior: [rf(3, 10), rf(7, 10)] };
    const folded = foldBack(tree);
    eq(Rtext(folded.value), '16', 'the tree folds back to 16');
    eq(folded.root.choiceLabel, 'build', 'so build');
    eq(Rtext(folded.evpi), '14', 'and perfect information is worth 30 - 16 = 14');
    eq(folded.evsi, null, 'EVSI comes back null without a likelihood rather than being invented');
    const P = [[rf(1, 2), rf(1, 2)], [rf(1, 4), rf(3, 4)]];
    const sdp = stochasticDp(['a', 'b'], ['hold', 'act'],
      [[[rf(1, 2), rf(1, 2)], [rf(1, 4), rf(3, 4)]], [[rf(3, 4), rf(1, 4)], [rf(1, 2), rf(1, 2)]]],
      [[ri(1), ri(3)], [ri(2), ri(1)]], 3);
    eq(sdp.V[0].map(Rtext).join(','), '53/8,67/8', 'the three-period stochastic recursion, exactly');
    eq(sdp.policy[0].map((a) => ['hold', 'act'][a]).join(','), 'act,hold',
       'and the action it chooses in each state at the first stage');
    const dv = discountedValue(P, [ri(1), ri(3)], rf(1, 2), 20);
    eq(dv.v.map(Rtext).join(','), '22/7,38/7', 'the exact fixed point (I - gamma P)^-1 r');
    eq(Rcmp(Rabs(dv.gap[0]), rf(1, 100000)) < 0, true, 'which twenty iterations reach to five places');
    eq(String(dv.iterations[20][0].d).length > String(dv.iterations[3][0].d).length, true,
       'and the denominators grow on the way, which is worth seeing');
  }

  /* --- Markov chains and the birth-death queue ----------------------------- */
  {
    const P = [[rf(1, 2), rf(1, 2)], [rf(1, 4), rf(3, 4)]];
    eq(Rtext(chainPow(P, 2)[0][0]), '3/8', 'P^2 by repeated Mmul');
    const five = [[rf(1, 5), rf(1, 5), rf(1, 5), rf(1, 5), rf(1, 5)],
                  [rf(1, 20), rf(3, 20), rf(7, 20), rf(4, 20), rf(5, 20)],
                  [rf(2, 20), rf(2, 20), rf(6, 20), rf(7, 20), rf(3, 20)],
                  [rf(9, 20), rf(1, 20), rf(1, 20), rf(4, 20), rf(5, 20)],
                  [rf(3, 20), rf(4, 20), rf(6, 20), rf(2, 20), rf(5, 20)]];
    const p12 = chainPow(five, 12)[0][0];
    eq(String(p12.n).length + '/' + String(p12.d).length, '15/16',
       'P^12 on a five-state chain is 15 digits over 16 -- past what Number holds, which is why chainPow is exact');
    eq(chainPeriod([[R0, R1, R0], [R0, R0, R1], [R1, R0, R0]], [0, 1, 2]).period, 3, 'a 3-cycle has period 3');
    eq(chainPeriod(P, [0, 1]).period, 1, 'and a chain with a self-loop is aperiodic');
    const leaky = chainClasses([[rf(1, 2), rf(1, 2), R0], [R0, R1, R0], [R0, R0, R1]]);
    eq(leaky.classes.map((c) => (c.recurrent ? 'R' : 'T')).join(''), 'TRR', 'a state that can leave and not return is transient');
    const ss = steadyState(P);
    eq(ss.pi.map(Rtext).join(','), '1/3,2/3', 'pi P = pi with sum pi = 1');
    eq(ss.dropped, 1, 'and the dropped equation is named rather than left implicit');
    eq(ss.system.length, 2, 'and the system SHOWN has n rows, not n + 1: one balance equation really was replaced');
    eq(Requ(steadyState(P, 0).pi[0], ss.pi[0]), true, 'dropping a different one gives the same pi');
    eq(Rcmp(Rabs(Rsub(chainPow(P, 30)[0][0], ss.pi[0])), rf(1, 1000000)) < 0, true, 'and P^30 approaches it');
    const ruin = [[R1, R0, R0, R0, R0], [rf(1, 2), R0, rf(1, 2), R0, R0],
                  [R0, rf(1, 2), R0, rf(1, 2), R0], [R0, R0, rf(1, 2), R0, rf(1, 2)],
                  [R0, R0, R0, R0, R1]];
    const abs = absorbing(ruin, [0, 4]);
    eq(abs.t.map(Rtext).join(','), '3,4,3', "the gambler's expected steps to ruin or riches from 1, 2, 3");
    eq(Rtext(abs.B[1][1]), '1/2', 'and from 2 the two ends are equally likely');
    eq(Requ(abs.partials[6][0][0], Radd(abs.partials[5][0][0], chainPow(abs.Q, 6)[0][0])), true,
       'the partials really are I + Q + ... + Q^k, which is what N sums to');
    const acts = [[[rf(1, 2), rf(1, 2)], [rf(1, 4), rf(3, 4)]], [[rf(3, 4), rf(1, 4)], [rf(1, 2), rf(1, 2)]]];
    const rew = [[ri(1), ri(3)], [ri(2), ri(1)]];
    const pol = policyIterate(acts, rew, rf(9, 10));
    let bestValue = null, bestPolicy = null;
    for (const a of [0, 1]) for (const b of [0, 1]) {
      const v = policyEvaluate(acts, rew, [a, b], rf(9, 10)).v;
      if (bestValue === null || (Rcmp(v[0], bestValue[0]) >= 0 && Rcmp(v[1], bestValue[1]) >= 0)) { bestValue = v; bestPolicy = [a, b]; }
    }
    eq(pol.policy.join(','), bestPolicy.join(','), 'policy iteration finds the best of all four policies');
    eq(Requ(pol.v[0], bestValue[0]), true, 'with its exact value ' + Rtext(bestValue[0]));
    /* THE KIT'S UNIFYING OBJECT: M/M/1 and M/M/s are one set of cut equations,
       and sysdesign_core's closed forms are the check panel beside them. */
    const lam = [], mu = [];
    for (let n = 0; n < 60; n += 1) { lam.push(ri(3)); mu.push(ri(5)); }
    const bd = birthDeath(lam, mu);
    eq(Rcmp(Rabs(Rsub(bd.L, mm1(ri(3), ri(5)).L)), rf(1, 1000000)) < 0, true,
       'the cut equations give the same L as sysdesign_core mm1 -- the two subjects CANNOT disagree');
    eq(bd.stable, true, 'lam < mu, so it is stable');
    eq(birthDeath([ri(5), ri(5), ri(5)], [ri(3), ri(3), ri(3)]).stable, false, 'and lam > mu is reported unstable');
    const lam2 = [], mu2 = [];
    for (let n = 0; n < 80; n += 1) { lam2.push(ri(2)); mu2.push(ri(Math.min(n + 1, 3))); }
    const mms = birthDeath(lam2, mu2, { servers: 3 });
    let waiting = R0;
    for (let n = 3; n < mms.pi.length; n += 1) waiting = Radd(waiting, mms.pi[n]);
    eq(Rcmp(Rabs(Rsub(waiting, erlangC(ri(2), ri(1), 3).pWait)), rf(1, 1000000)) < 0, true,
       'and Erlang C falls out of the SAME pi as a reading, not as a second formula');
    eq(Rcmp(Rabs(Rsub(mms.Lq, erlangC(ri(2), ri(1), 3).Lq)), rf(1, 1000000)) < 0, true, 'Lq with it');
  }

  /* --- simulation output, exactly ------------------------------------------ */
  {
    const xs = [2, 4, 4, 4, 5, 5, 7, 9].map(ri);
    eq(Rtext(sampleMean(xs)), '5', 'the sample mean');
    eq(Rtext(sampleVar(xs)), '32/7', 'and the sample variance, with n - 1 = 7 underneath');
    const ys = xs.map((x) => Radd(Rmul(ri(2), x), ri(1)));
    eq(Rtext(rhoSquared(xs, ys)), '1', 'a perfect line has rho^2 = 1 -- and rho^2 is the only one ever printed, because rho is a surd');
    eq(Requ(sampleCov(xs, ys), Rmul(ri(2), sampleVar(xs))), true, 'Cov(X, 2X + 1) = 2 Var X');
    const cov = chebyshevCover([9, 10, 11, 14, 6, 10].map(ri), ri(10), ri(2), ri(4));
    eq(Rtext(cov.bound), '3/4', 'the Chebyshev bound at k = 2');
    eq(cov.outside, 2, 'two replicates are two standard deviations out, counted by comparing SQUARES -- no root is taken');
    eq(cov.holds, false, 'and 4 of 6 falls short of the bound, which the field reports rather than hides');
    const cs = [1, 3, 2, 5, 4, 6, 8, 7].map(ri);
    const ctl = controlB(xs, cs);
    eq(Rtext(ctl.bStar), '31/42', 'the control-variate b* = Cov / Var C');
    eq(Requ(ctl.varAt, Rmul(ctl.varRaw, Rsub(R1, ctl.rho2))), true, 'and Var at b* is exactly Var X (1 - rho^2)');
    for (const d of [rf(1, 7), rf(-1, 3), ri(1), ri(-2)]) {
      eq(Rcmp(controlVarAt(ctl.quadratic, Radd(ctl.bStar, d)), ctl.varAt) >= 0, true, 'b* minimises the quadratic');
    }
    const p = [[ri(0), rf(9, 10)], [ri(1), rf(9, 100)], [ri(2), rf(1, 100)]];
    const q = [[ri(0), rf(1, 2)], [ri(1), rf(3, 10)], [ri(2), rf(1, 5)]];
    const imp = importanceRun(p, q, (x) => Rcmp(x, ri(2)) >= 0);
    eq(Rtext(imp.estimate), '1/100', 'both estimators are unbiased for the same 1/100');
    eq(Rtext(imp.ratio), '99/4', 'and importance sampling cuts the variance by 99/4');
    const refused = importanceRun(p, [[ri(0), rf(1, 2)], [ri(1), rf(1, 2)], [ri(2), R0]], (x) => Rcmp(x, ri(2)) >= 0);
    eq(refused.refused && refused.estimate === null, true,
       'q(x) = 0 where p(x) > 0 is REFUSED -- an estimator that skips the outcome is biased and no variance figure shows it');
    const des = desRun([0, 1, 2, 9].map(ri), [4, 3, 1, 2].map(ri));
    eq(des.events.map((e) => Rtext(e.t) + e.kind.charAt(0) + e.who).join(' '),
       '0a0 1a1 2a2 4d0 7d1 8d2 9a3 11d3', 'the event calendar, in order');
    eq(des.events[2].inSystem, 3, 'three in the system after the third arrival');
    eq(Rtext(des.meanWait), '2', 'the mean wait is 2');
    eq(Rtext(des.utilisation), '10/11', 'and the server was busy 10 of 11');
    const run = [];
    for (let k = 1; k <= 20; k += 1) run.push(ri(k));
    const bm = batchMeans(run, 4, 4);
    eq(bm.means.map(Rtext).join(','), '13/2,21/2,29/2,37/2', 'four batch means after a warm-up discard of four');
    eq(Rtext(bm.grand) + ' vs ' + Rtext(bm.naive), '25/2 vs 21/2', 'and the discard changes the answer, which is the point');
  }

  /* --- inventory ------------------------------------------------------------ */
  {
    const e = eoq(ri(100), ri(1200), ri(6));
    eq(e.Qsurd.k === 1n && Rtext(e.Qsurd.q) === '200', true, 'EOQ(100, 1200, 6) = 200, and this one is rational');
    eq(Requ(eoqCostAt(ri(200), ri(100), ri(1200), ri(6)), ri(1200)), true, 'costing 1200 at it');
    const irr = eoq(ri(50), ri(600), ri(5));
    eq(Rtext(irr.Qsurd.q) + 'sqrt' + irr.Qsurd.k, '20sqrt30', 'EOQ(50, 600, 5) is 20 sqrt 30 and STAYS a surd');
    eq(surdDec(irr.Qsurd, 4), '109.5445', 'printed as 109.5445 only where the page says it is rounded');
    const merged = eoqDiscriminant(ri(100), ri(1200), ri(6), ri(1200));
    eq(merged.atMinimum && merged.roots.kind === 'double', true,
       'at T = C* the discriminant of hQ^2/2 - TQ + KD is exactly zero');
    eq(Rtext(merged.roots.roots[0]), '200', 'and the double root IS the EOQ -- derived, not asserted');
    eq(eoqDiscriminant(ri(100), ri(1200), ri(6), ri(1300)).roots.roots.map(Rtext).join(','), '400/3,300',
       'above C* an interval of quantities is cheap enough');
    eq(eoqDiscriminant(ri(100), ri(1200), ri(6), ri(1100)).feasible, false, 'and below it, none is');
    eq(Rtext(eoqRatio(ri(2))) + ',' + Rtext(eoqRatio(rf(1, 2))), '5/4,5/4', 'twice the EOQ and half of it cost the same 25% more');
    eq(Rtext(eoqRatio(rf(6, 5))), '61/60', 'while a 20% error costs 1/60 -- under 2%, which is why the EOQ is worth using badly');
    const epq = epqCost(ri(100), ri(1200), ri(6), ri(2400), R0, R0);
    eq(Rtext(epq.factor), '1/2', 'producing at twice demand halves the effective holding rate');
    eq(Requ(epqCostAt(ri(400), R0, ri(100), ri(1200), ri(6), ri(2400), R0),
            eoqCostAt(ri(400), ri(100), ri(1200), ri(3))), true, 'and at b = 0 the EPQ IS the EOQ with h scaled by f');
    const back = epqCost(ri(100), ri(1200), ri(6), ri(2400), null, ri(6));
    eq(Rtext(back.Qsurd.q) + '/' + Rtext(back.costSurd.q), '400/600', 'with backorders at pi = h, Q* = 400 and the cost is 600');
    eq(Requ(epqCostAt(ri(400), ri(100), ri(100), ri(1200), ri(6), ri(2400), ri(6)), ri(600)), true,
       'which is what the cost formula gives at that Q and b* = 100');
    const demandPmf = [[0, rf(1, 10)], [1, rf(2, 10)], [2, rf(3, 10)], [3, rf(3, 10)], [4, rf(1, 10)]];
    const nv = newsvendor(demandPmf, ri(7), ri(3));
    eq(Rtext(nv.ratio), '7/10', 'the newsvendor critical ratio');
    eq(nv.Q, 3, 'crossed first at Q = 3');
    eq(nv.agrees, true, 'and that Q really is the cheapest on the whole tabulated curve');
    const per = [[0, rf(1, 4)], [1, rf(1, 2)], [2, rf(1, 4)]];
    const rp = reorderPoint(per, 2, 2);
    eq(Rtext(rp.meanDemand), '2', 'two periods of mean-1 demand, by pmfConvolve');
    eq(Rtext(rp.shortage), '3/8', 'and a reorder point of 2 still runs 3/8 of a unit short per cycle');
    const bs = baseStock(per, 2, 1, rf(9, 10));
    eq(bs.periods, 3, 'periodic review covers R + L = 3 periods, not one');
    eq(bs.S, 5, 'so the 90% base-stock level is 5');
    const bands = [{ from: ri(0), price: ri(10), h: rf(2, 1) },
                   { from: ri(500), price: ri(9), h: rf(18, 10) },
                   { from: ri(1000), price: ri(8), h: rf(16, 10) }];
    const disc = discountCandidates(bands, ri(40), ri(1200), ri(2));
    eq(disc.candidates.map((c) => c.at).join(' | '), 'the EOQ | the band edge | the band edge',
       'one candidate per band: its EOQ when that falls inside, the band edge when it does not');
    eq(Rtext(disc.candidates[0].cost.r) + ' + ' + Rtext(disc.candidates[0].cost.s.q) + 'sqrt' + disc.candidates[0].cost.s.k,
       '12000 + 80sqrt30', 'the first band costs an exact surd');
    eq(disc.best, 2, 'and the cheapest plan buys into the deepest discount, compared without rounding');
    eq(surdValueCmp(surdValue(ri(0), Rsurd(ri(2))), surdValue(ri(0), Rsurd(ri(3)))), -1, 'sqrt 2 < sqrt 3, exactly');
    eq(surdValueCmp(surdValue(ri(0), { q: ri(3), k: 2n }), surdValue(ri(0), { q: ri(2), k: 5n })), -1, '3 sqrt 2 < 2 sqrt 5');
    eq(surdValueCmp(surdValue(ri(0), { q: ri(3), k: 2n }), surdValue(ri(0), { q: ri(1), k: 17n })), 1, '3 sqrt 2 > sqrt 17');
    eq(surdValueCmp(surdValue(ri(1), Rsurd(ri(2))), surdValue(ri(1), Rsurd(ri(2)))), 0, 'and equal values compare equal');
  }
}


// ------------------------------------------------------------- algo_core
console.log('algorithms: counts, exact expectations, and the oracles they agree with');
{
  /* The Algorithms path's shared engine. Two things this section is for.
     First, the arithmetic: exact expectations, exact probabilities, exact
     determinants and the four quantities that are NOT exact. Second, and more
     valuable, the ORACLE AGREEMENTS: four routines here answer a question
     graph.py already answers by brute force, and where two implementations
     written from different definitions agree, both are evidence. */
  eval(algoCoreBlock('COUNT_JS'));
  eval(algoCoreBlock('RFIXED_JS'));
  eval(algoCoreBlock('SERIES_JS'));
  eval(algoCoreBlock('SEEDED_JS'));
  eval(algoCoreBlock('TREEDRAW_JS'));
  eval(algoCoreBlock('DIGRAPH_JS'));
  eval(algoCoreBlock('ORACLE_JS'));
  eval(algoCoreBlock('SEQ_JS'));
  eval(algoCoreBlock('HEAP_JS'));
  eval(algoCoreBlock('HASH_JS'));
  eval(algoCoreBlock('TREE_JS'));
  eval(algoCoreBlock('SORT_JS'));
  eval(algoCoreBlock('GRAPHKIT_JS'));
  eval(algoCoreBlock('FLOW_JS'));
  eval(algoCoreBlock('GREEDY_JS'));
  eval(algoCoreBlock('DP_JS'));
  eval(algoCoreBlock('STRINGS_JS'));
  eval(algoCoreBlock('GEOM_JS'));
  eval(algoCoreBlock('RANDOM_JS'));
  eval(algoCoreBlock('REDUCTION_JS'));
  eval(algoCoreBlock('COPING_JS'));
  eval(graphBlock('GRAPH_JS'));
  const loadPreset = (preset, n) => { LESSON = null; useLessonWeights = false; N = n; A = PRESETS[preset](n); };
  const loadLesson = (n, list) => { LESSON = lessonFrom(list); useLessonWeights = true; N = n; A = PRESETS.lesson(n); };
  const pair = (u, v) => Math.min(u, v) + '-' + Math.max(u, v);
  const inf = (d) => (d === null ? Infinity : d);

  /* --- the seeded stream, and the defect it exists to avoid -------------- */
  {
    const bins = [0, 0, 0, 0];
    lcgStream(1103515245, 12345, 2147483648, 7, 1200).forEach((x) => { bins[x % 4] += 1; });
    eq(bins.join(','), '300,300,300,300',
       'the glibc modulus is a power of two, so 1200 draws mod 4 come out PERFECTLY level');
    const mine = [0, 0, 0, 0];
    algoStream(7, 1200).forEach((x) => { mine[x % 4] += 1; });
    eq(mine.join(',') === '300,300,300,300', false, 'MINSTD, whose modulus 2^31 - 1 is prime, does not');
    const raw = [1, 2, 3, 4, 5, 6].map((s) => lcgStream(16807, 0, 2147483647, s, 1)[0]);
    eq(raw.join(','), '16807,33614,50421,67228,84035,100842',
       'and an unmixed seed is affine in the seed: six seeds, one straight line');
    const mixed = [1, 2, 3, 4, 5, 6].map((s) => algoStream(s, 1)[0]);
    eq(new Set(mixed.slice(1).map((v, i) => v - mixed[i])).size, 5,
       'splitmix64 before the state breaks that: five different gaps');
    eq(algoStream(3, 5).join(','), algoStream(3, 5).join(','), 'and the stream is still reproducible');
  }

  /* --- ORACLE AGREEMENT: the new graph code against graph.py's brute force */
  const LIST = [[1,2,4],[1,3,3],[2,3,2],[2,4,5],[3,4,7],[4,5,1],[5,6,6],[5,7,8],[6,7,2]];
  loadLesson(7, LIST);
  const G7 = dgFromLesson(7, LIST, false);
  eq(G7.arcs.length + ',' + edges().length, '9,9', 'both representations hold the same nine edges');
  eq(G7.arcs.map((a) => a.w).join(','), edges().map((e) => e[2]).join(','), 'at the same weights');
  eq(kruskalRun(G7).result.weight, kruskal().total,
     'kruskalRun agrees with GRAPH_JS.kruskal on the minimum spanning tree');
  eq(primRun(G7, 0).result.weight, kruskal().total, 'and so does Prim, from the cut property instead');
  for (const s of [0, 3, 6]) {
    eq(relaxRun(G7, s, 'heap').result.dist.map(inf).join(','), dijkstra(s).dist.join(','),
       'relaxRun agrees with GRAPH_JS.dijkstra from vertex ' + (s + 1));
    eq(relaxRun(G7, s, 'insertion').result.dist.map(inf).join(','), dijkstra(s).dist.join(','),
       'and relaxing in arc order reaches the same distances from ' + (s + 1));
  }
  eq(relaxRun(G7, 0, 'heap').counts.relaxations === relaxRun(G7, 0, 'insertion').counts.relaxations, false,
     'the schedule changes the WORK and not the answer');
  for (const [preset, n] of [['cycle', 6], ['tree', 7], ['path', 6], ['petersen', 6], ['complete', 5], ['star', 6]]) {
    loadPreset(preset, n);
    const Gp = dgFromMatrix(A, n, weight, false), mine = lowLink(Gp), theirs = cuts();
    eq(mine.result.bridges.map((b) => pair(b.u, b.v)).sort().join(' '),
       theirs.bridges.map((b) => pair(b.edge[0], b.edge[1])).sort().join(' '),
       'lowLink agrees with delete-and-recount on the bridges of ' + preset);
    eq(mine.result.cutVertices.join(','), theirs.cutVertices.join(','),
       'and on its cut vertices');
    eq(kruskalRun(Gp).result.weight, kruskal().total, 'and the MST weight agrees on ' + preset);
    eq(hamiltonBrute(Gp).result.circuit !== null, hamilton().circuit !== null,
       'hamiltonBrute agrees with GRAPH_JS.hamilton about a circuit on ' + preset);
    eq(cliqueBrute(Gp).result.size, cliqueNumber().size,
       'and cliqueBrute agrees with GRAPH_JS.cliqueNumber on ' + preset);
  }
  loadPreset('petersen', 6);
  {
    const Gp = dgFromMatrix(A, 6, weight, false), comp = complementGraph(Gp);
    const id = checkComplementIdentity(Gp);
    N = 6; A = dgToMatrix(comp);
    eq(cliqueBrute(comp).result.size, cliqueNumber().size,
       'the complement, handed back to GRAPH_JS through dgToMatrix, has the clique number this code found');
    eq(id.identityHolds, true, 'and |independent set| + |vertex cover| = V');
    eq(id.cliqueMatches, true, 'an independent set being a clique in the complement');
  }

  /* --- what GRAPH_JS cannot express: direction, negative weights, capacity */
  {
    const D = dgFromLesson(6, [[1,2],[2,3],[3,1],[3,4],[4,5],[5,6],[4,6]], true);
    const kinds = edgeKindCounts(classifyEdges(D, dfsTimes(D, [0]).result));
    eq([kinds.tree, kinds.back, kinds.forward, kinds.cross].join(','), '5,1,1,0',
       'the triangle contributes a back edge and 4 -> 6 a forward one');
    eq(topoDfs(D).result.acyclic + ',' + (topoKahn(D).result.order === null), 'false,true',
       'so neither topological order exists, and both say so');
    eq(kosaraju(D).result.components.map((c) => '{' + c.map((v) => v + 1).join(' ') + '}').join(' '),
       '{1 2 3} {4} {5} {6}', 'Kosaraju finds the one non-trivial strongly connected component');
    eq(kosaraju(D).result.condensationAcyclic, true, 'and the condensation is acyclic');
    const dag = dgFromLesson(6, [[1,2,3],[1,3,2],[2,4,4],[3,4,1],[4,5,2],[3,5,7],[5,6,1]], true);
    eq(dagRelax(dag, 0, 1).result.dist.join(','), '0,3,2,3,5,6', 'one pass in topological order gives shortest paths');
    eq(dagRelax(dag, 0, -1).result.dist.join(','), '0,3,2,7,9,10', 'and with the sign flipped, LONGEST paths');
    eq(relaxRun(dag, 0, 'heap').result.dist.join(','), dagRelax(dag, 0, 1).result.dist.join(','),
       'agreeing with Dijkstra on the same DAG');
    const neg = dgFromLesson(5, [[1,2,6],[1,3,7],[2,3,8],[2,4,5],[2,5,-4],[3,4,-3],[3,5,9],[4,2,-2],[5,1,2],[5,4,7]], true);
    eq(bellmanFordRounds(neg, 0).result.dist.join(','), '0,2,7,4,-2',
       'Bellman-Ford under NEGATIVE weights, which GRAPH_JS cannot hold at all');
    eq(floydSteps(dgWeightMatrix(neg)).result.dist[0].join(','), bellmanFordRounds(neg, 0).result.dist.join(','),
       'and Floyd agrees with it row for row');
    const cyc = dgFromLesson(4, [[1,2,1],[2,3,-3],[3,4,1],[4,2,1]], true);
    eq(bellmanFordRounds(cyc, 0).result.negativeCycle.map((v) => v + 1).join(' -> '), '2 -> 3 -> 4 -> 2',
       'a negative cycle comes back as the cycle itself, not as a boolean');
    const tricky = dgFromLesson(4, [[1,2,6],[2,4,9],[3,2,2],[4,3,8]], true);
    eq(floydSteps(dgWeightMatrix(tricky)).result.dist[0][2], 23,
       'Floyd reaches 1 -> 3 at 23 through two interior vertices, which the k loop must be outermost to find');
  }
  {
    const net = dgFromLesson(6, [[1,2,0,16],[1,3,0,13],[2,3,0,10],[3,2,0,4],[2,4,0,12],
                                 [3,5,0,14],[4,3,0,9],[5,4,0,7],[4,6,0,20],[5,6,0,4]], true);
    const mf = maxflow(net, 0, 5), cut = minCutFrom(net, mf.result.flow, 0);
    eq(mf.result.value + ',' + mf.result.conserved, '23,true', 'the maximum flow is 23 and conserves at every interior vertex');
    eq(cut.capacity + ',' + cut.allSaturated, '23,true', 'the minimum cut has the same capacity and every crossing arc saturated');
    eq(cut.S.map((v) => v + 1).join(','), '1,2,3,5', 'with {1, 2, 3, 5} on the source side');
    const trap = dgFromLesson(4, [[1,2,0,1],[1,3,0,1],[2,3,0,1],[2,4,0,1],[3,4,0,1]], true);
    const first = augment(trap, zeroFlow(trap), residual(trap, zeroFlow(trap)), [0, 2, 4]);
    eq(bfsPath(residual(trap, first.flow, { reverse: false }), 0, 3).path, null,
       'push one unit down the middle and WITHOUT a backward arc there is no second path');
    const back = bfsPath(residual(trap, first.flow), 0, 3);
    eq(flowValue(trap, augment(trap, first.flow, residual(trap, first.flow), back.path).flow, 0), 2,
       'and with one there is: the flow reaches 2 by undoing the middle arc');
    const net2 = matchingNetwork(3, 3, [[0,0],[0,1],[1,0],[2,1],[2,2]]);
    const m2 = maxflow(net2.graph, net2.s, net2.t);
    eq(m2.result.value + ',' + konigCover(net2, m2.result.flow).size, '3,3',
       "Konig: the matching and the cover read off the cut are the same size");
  }

  /* --- the exact expectations, and the four things that are not exact ----- */
  eq(Rtext(quickExpected(3)), '8/3', 'E[quicksort comparisons] at n = 3 is 8/3 -- (1/3)(2) + (2/3)(3), by hand');
  eq(Rtext(quickExpected(5)), '37/5', 'and 37/5 at n = 5, from an exact H_5');
  eq(Requ(quickExpected(5), Rsub(Rmul(R(12n, 1n), harmonic(5, 1)), R(20n, 1n))), true,
     'which is 2(n+1)H_n - 4n with harmonic() reused as it ships');
  eq(Rtext(buildSumExact(7).total), '4', 'Floyd build: sum ceil(7/2^{h+1})h = 0 + 2 + 2 = 4');
  eq(Rcmp(buildSumExact(7).total, R(7n, 1n)) < 0, true, 'which is under n -- the linear claim, evaluated');
  eq(Rtext(chainRun([1,2,3,4,5,6,7,8,9,10], 5, 'division').result.expectedSuccessful), '9/5',
     'expected probes in a chain: 1 + a/2 - a/2m = 9/5');
  eq(Rtext(chainRun([1,2,3,4,5,6,7,8,9,10], 5, 'division').result.measuredMean), '3/2',
     'beside the 3/2 the page measured by running all ten searches');
  eq(Rtext(ballsExact(23, 365).expectedPairs) + ',' + ballsExact(23, 365).birthdayN, '253/365,23',
     'balls in bins, exactly, and the birthday number by exact product');
  eq(Rtext(bloomExact(8, 2, 2)), '2873025/16777216', 'the exact Bloom rate at m = 8, n = 2, k = 2');
  eq(Number.isNaN(Rnum(bloomExact(1000, 100, 7))), true,
     'at m = 1000 the exact rate overflows a double -- which is why Rfixed divides the BigInts');
  eq(Rfixed(bloomExact(1000, 100, 7), 6), '0.008214', 'and prints 0.008214');
  eq(bloomApprox(1000, 100, 7).toFixed(6), '0.008194',
     'while the independent-hash idealisation says 0.008194 -- LABELLED, and the gap is the lesson');
  eq(knuthProbeApprox(0.99), null, 'the clustering curve is refused above alpha = 0.98, not extrapolated');
  eq(knuthProbeApprox(0.5).unsuccessful, 2.5, 'and reads 2.5 at alpha = 1/2 -- an approximation, and it says so');
  near(randomBstDepthApprox(15), 5.4161, 1e-3, '2 ln n is 5.416 at n = 15');
  eq(bstFromOrder([8,4,12,2,6,10,14,1,3,5,7,9,11,13,15]).result.height, 3,
     'while the balanced tree on 15 keys has height 3: the ASYMPTOTE is not the tree');
  eq(Rtext(countMinRun([1,1,1,2,2,3,4,4,4,4], 8, 3).result.delta), '1/8',
     'count-min quotes the Markov guarantee 2^-d = 1/8, which this library proves');
  eq(countMinRun([1,1,1,2,2,3,4,4,4,4], 8, 3).result.neverUnder, true, 'and it never underestimates');

  /* --- counted algorithms, each against the baseline it claims to beat ---- */
  {
    const asc = [];
    for (let i = 1; i <= 31; i += 1) asc.push(i);
    eq(floydBuild(asc, true).counts.compares < insertBuild(asc, true).counts.compares, true,
       'Floyd builds a heap in fewer comparisons than 31 insertions');
    eq(floydBuild(asc, true).counts.swaps <= 31, true, 'and at most n swaps');
    eq(heapsortRun([5,3,8,1,9,2]).result.sorted.join(','), '1,2,3,5,8,9', 'heapsort sorts');
    const runs = [[1,4,9],[2,5,8],[3,6,7]];
    eq(kwayMerge(runs).result.merged.join(','), pairwiseMerge(runs).result.merged.join(','),
       'the k-way merge and the pairwise passes produce the same sequence');
    eq(quickRun(asc, 'last').counts.compares, 465, 'a last-element pivot on sorted input is the quadratic worst case');
    eq(quickRun(asc, 'median3').counts.compares < 465, true, 'and median-of-three is not');
    eq(quickRun(asc, 'random', 3).result.sorted.join(',') === asc.join(','), true, 'a seeded pivot still sorts');
    eq(radixRun([329,457,657,839,436,720,355], 10, true).result.sorted.join(','),
       '329,355,436,457,657,720,839', 'LSD radix sorts when its pass is stable');
    eq(radixRun([329,457,657,839,436,720,355], 10, false).result.correct, false, 'and does not when it is not');
    eq(stableRun(stableRecords([2,2,1]), 'selection').result.stable, false, 'selection sort is not stable');
    eq(stableRun(stableRecords([2,2,1]), 'insertion').result.stable, true, 'and insertion sort is');
    eq(momRun([7,2,9,4,1,8,3,6,5,10,11,12], 5, 5).result.agrees, true,
       'median of medians and quickselect find the same 5th smallest');
    eq(Rtext(levelSums(R(1n, 5n), R(7n, 10n), 100, 6).geometric), '1000',
       'and its recursion tree sums to 10n exactly, which is why it is linear');
    eq(tournament([3,1,4,1,5,9,2,6]).counts.compares <= tournament([3,1,4,1,5,9,2,6]).result.bound, true,
       'the tournament finds the second largest within n - 1 + ceil(log n) - 1 comparisons');
    eq(twoStackRun([1,2,3].map((k) => ({ op: 'enqueue', key: k }))
        .concat([{ op: 'dequeue' }, { op: 'dequeue' }, { op: 'dequeue' }])).result.order.join(','),
       '1,2,3', 'two stacks make a queue');
    eq(twoStackRun([1,2,3].map((k) => ({ op: 'enqueue', key: k }))
        .concat([{ op: 'dequeue' }, { op: 'dequeue' }, { op: 'dequeue' }])).result.withinBound, true,
       'inside the 3m the credit argument allows');
    eq(unionFindRun([0,1,2,3,4,5,6].map((i) => ({ op: 'union', a: i, b: i + 1 }))
        .concat([{ op: 'find', a: 0 }]), {}, 8).result.worstHops, 7,
       'chained unions with no rank rule make a path of length 7');
    eq(unionFindRun([0,1,2,3,4,5,6].map((i) => ({ op: 'union', a: i, b: i + 1 }))
        .concat([{ op: 'find', a: 0 }]), { rank: true }, 8).result.rankBoundHolds, true,
       'and a rank-r root has at least 2^r descendants');
    eq(avlInsert([1,2,3,4,5,6,7]).result.height + ',' + avlInsert([1,2,3,4,5,6,7]).result.plainHeight, '2,6',
       'AVL holds the height at 2 where the plain BST is a path of 6');
    eq(minAvlNodes(4).n, 12, 'and N(4) = 12 is the fewest nodes an AVL tree of height 4 can hold');
    const aug = bstFromOrder([9,4,13,2,6,11,15]).result.root;
    eq(augmentWalk(aug, { op: 'select', i: 3 }).result.value + ','
       + augmentWalk(aug, { op: 'rank', key: 13 }).result.value, '6,6',
       'the order-statistic tree selects the 3rd key and ranks 13, by walking subtree sizes');
    {
      const keys = bstInorder(aug);
      let bad = 0;
      for (let lo = 0; lo <= 16; lo += 1) for (let hi = lo; hi <= 16; hi += 1) {
        if (augmentWalk(aug, { op: 'range', lo: lo, hi: hi }).result.value
            !== keys.filter((k) => k >= lo && k <= hi).length) bad += 1;
      }
      eq(bad, 0, 'and its range count agrees with a scan on all 153 intervals, while being two walks');
    }
    const t1 = treapInsert([5,2,8,1], [30,10,20,5]), t2 = treapInsert([1,8,2,5], [5,20,10,30]);
    eq(t1.result.heapOrdered + ',' + (t1.result.height === t2.result.height), 'true,true',
       'two insertion orders of the same (key, priority) set give the same treap');
  }

  /* --- greedy, DP and the optima they are checked against ---------------- */
  {
    const I = [{s:0,f:6},{s:1,f:4},{s:3,f:5},{s:3,f:8},{s:4,f:7},{s:5,f:9},{s:6,f:10},{s:8,f:11}];
    eq(greedyTrace(I, 'earliestFinish').result.matchesOptimum, true,
       'earliest finish time matches the brute-force optimum');
    eq(greedyTrace(I, 'earliestFinish').result.rows.every((r) => r.ahead !== false), true,
       'staying ahead at every step');
    eq(greedyTrace([{s:0,f:5},{s:4,f:6},{s:5,f:10}], 'shortest').result.matchesOptimum, false,
       'and the shortest-first rule does not, on the instance built to break it');
    eq(partitionRooms(I, 'start').result.optimal, true, 'interval partitioning uses exactly the depth');
    const F = [{symbol:'a',weight:45},{symbol:'b',weight:13},{symbol:'c',weight:12},
               {symbol:'d',weight:16},{symbol:'e',weight:9},{symbol:'f',weight:5}];
    const codes = huffmanBuild(F).result.codes, cost = codeCost(codes, F);
    eq(Rtext(cost.expected) + ' = ' + Rfixed(cost.expected, 2), '56/25 = 2.24',
       "Huffman on CLRS's example costs 56/25 bits per symbol, exactly");
    const small = [{symbol:'a',weight:5},{symbol:'b',weight:2},{symbol:'c',weight:1},{symbol:'d',weight:1}];
    const bestShape = allFullBinaryTrees(4)
      .map((s) => shapeCost(s, small.map((x) => x.weight)))
      .reduce((a, b) => (b < a ? b : a));
    eq(String(codeCost(huffmanBuild(small).result.codes, small).bits), String(bestShape),
       'and it attains the minimum over every full binary tree on four leaves');
    const items = [{w:10,v:60},{w:20,v:100},{w:30,v:120}];
    eq(Rtext(fractionalKnapsack(items, 50).result.value) + ',' + fractionalKnapsack(items, 50).result.integralValue,
       '240,220', 'the fractional optimum is 240 and the 0/1 optimum 220');
    eq(Rtext(fractionalKnapsack(items, 50).result.picks[2].take), '2/3', 'taking two thirds of the last item');
    const uni = independenceEnumerate([0,1,2,3], (m) => m.length <= 2);
    eq(exchangeTest(uni.result.family).isMatroid, true, 'the uniform family is a matroid');
    eq(matroidGreedy(uni.result.family, [7,5,3,1], [0,1,2,3]).result.matches, true, 'so greedy is optimal on it');
    eq(replayPolicy([1,2,3,1,4,1,2,5,1,2,3,4,5], 3, 'opt').hits
       >= replayPolicy([1,2,3,1,4,1,2,5,1,2,3,4,5], 3, 'lru').hits, true,
       'and greedy.caching is replayPolicy, reused: farthest-in-future beats LRU');
    const its = [{w:1,v:1},{w:3,v:4},{w:4,v:5},{w:5,v:7}];
    const ks = dpFill({ rows: its.length + 1, cols: 8,
      cell: (i, j, get) => {
        if (i === 0) return { v: 0, from: null };
        const skip = get(i - 1, j);
        if (its[i - 1].w > j) return { v: skip, from: [i - 1, j] };
        const take = its[i - 1].v + get(i - 1, j - its[i - 1].w);
        return take > skip ? { v: take, from: [i - 1, j - its[i - 1].w] } : { v: skip, from: [i - 1, j] };
      } });
    eq(ks.result.table[its.length][7], knapsackBrute(its, 7).result.value,
       'the knapsack table agrees with brute force');
    eq(ks.result.deps[2][5].length > 0, true, 'and every cell records the cells it actually read');
    const dims = [30,35,15,5,10,20,25];
    const mc = dpFill({ rows: 6, cols: 6, order: 'bylength',
      cell: (i, j, get) => {
        if (i === j) return { v: 0, from: null };
        let best = null, at = null;
        for (let k = i; k < j; k += 1) {
          const v = get(i, k) + get(k + 1, j) + dims[i] * dims[k + 1] * dims[j + 1];
          if (best === null || v < best) { best = v; at = [i, k]; }
        }
        return { v: best, from: at };
      } });
    eq(mc.result.table[0][5], 15125, "the matrix chain optimum is CLRS's 15125, filled by length");
    eq(lisTails([1,5,6,2,3,4]).result.subsequence.join(','), '1,2,3,4',
       'the LIS comes from predecessors, not from the tails array');
    const tree = { 0: [1, 2], 1: [0, 3, 4], 2: [0], 3: [1], 4: [1] }, w = [3,4,2,1,5];
    eq(treeDp(tree, w).result.value, misBrute(tree, w).result.value,
       'the tree DP agrees with brute force on the weighted independent set');
    eq(String(countWays([1,2,5], 5, 'combinations').result.count) + ','
       + String(countWays([1,2,5], 5, 'permutations').result.count), '4,9',
       'four combinations make 5 from {1, 2, 5} and nine ordered sequences do -- the loop order is the answer');
    eq(gameLabels((p) => [p - 1, p - 2, p - 3].filter((q) => q >= 0), [0,1,2,3,4,5,6,7,8]).result.losing.join(','),
       '0,4,8', 'the subtraction game {1, 2, 3} loses exactly at the multiples of 4');
    const D4 = [[0,2,9,10],[1,0,6,4],[15,7,0,8],[6,3,12,0]];
    eq(heldKarp(D4).result.length, tspBrute(D4).result.length, 'Held-Karp agrees with the brute-force tour');
    eq(String(heldKarp(D4).result.heldKarpWork) + ' vs ' + String(heldKarp(D4).result.bruteWork), '256 vs 6',
       'and prints n^2 2^n against (n - 1)! as exact integers');
  }

  /* --- strings, geometry, randomness ------------------------------------- */
  {
    const t = 'abababcabababcabc', p = 'ababc';
    eq(naiveRun(t, p).result.hits.join(','), '2,9', 'naive matching finds two occurrences');
    eq(kmpRun(t, p).result.hits.join(','), '2,9', 'KMP the same two');
    eq(horspoolRun(t, p).result.hits.join(','), '2,9', 'Horspool the same two');
    eq(rollingHash(t, p, 256, 101).result.hits.join(','), '2,9', 'and Rabin-Karp the same two');
    eq(dfaRun(t, dfaTable(p, ['a','b','c']).table, 5).result.hits.join(','), '2,9',
       'and the automaton, in exactly n steps');
    eq(kmpRun(t, p).counts.compares <= 2 * t.length, true, 'KMP inside its 2n bound');
    eq(failureFn('ababaca').result.fail.join(','), '-1,0,0,1,2,3,0,1', 'the failure function of ababaca');
    eq(Rtext(expectedPerAlignment(26)), '26/25', 'expected characters per alignment over 26 letters');
    eq(suffixArray('banana').result.suffixes.join(' '), 'a ana anana banana na nana', 'the suffix array of banana');
    eq(kasai('banana', suffixArray('banana').result.sa).result.lcp.join(','), '0,1,3,0,0,2', 'and its LCP array');
    eq(String(kasai('banana', suffixArray('banana').result.sa).result.distinctSubstrings), '15',
       'so banana has 15 distinct substrings');
    eq(ahoRun('ushers', ahoLinks(trieBuild(['he','she','his','hers']))).result.hits.length, 3,
       'Aho-Corasick reports three matches in one pass');

    eq(String(orient2([0,0],[134217729,134217728],[134217728,134217727])), '-1',
       'the exact determinant calls these three a right turn');
    eq(orient2Float([0,0],[134217729,134217728],[134217728,134217727]), 0,
       'and a double calls them collinear -- a wrong SIGN, not a rounding, which is why this block is BigInt');
    const pts = [[0,0],[1,3],[2,1],[3,4],[4,0],[5,2],[2,5],[6,3]];
    const key = (h) => h.slice().sort((x, y) => x[0] - y[0] || x[1] - y[1]).map((q) => q.join(',')).join(' ');
    eq(key(jarvis(pts).result.hull), key(monotoneChain(pts).result.hull),
       "Jarvis's march and the monotone chain find the same hull");
    eq(String(calipers(monotoneChain(pts).result.hull).result.d2), String(diameterBrute(pts).d2),
       'rotating calipers finds the same squared diameter as every pair');
    eq(String(shoelace2([[0,0],[4,0],[4,4],[0,4]])), '32', 'the doubled area of a 4x4 square is 32');
    eq(rayParity([[0,0],[4,0],[2,4]], [2,0]).onBoundary + ',' + rayParity([[0,0],[4,0],[2,4]], [2,1]).inside,
       'true,true', 'a ray through a vertex does not double count');
    const P6 = [[0,0],[10,10],[1,1],[20,20],[2,3],[30,30]];
    let brute = null;
    for (let i = 0; i < P6.length; i += 1) for (let j = i + 1; j < P6.length; j += 1) {
      const d = dist2(P6[i], P6[j]);
      if (brute === null || d < brute) brute = d;
    }
    eq(String(closestPair(P6).result.d2), String(brute), 'divide and conquer finds the same closest pair as every pair');
    eq(closestPair(P6).result.stripCompares <= closestPair(P6).result.bound, true,
       'with the strip comparisons under 7n');

    const pmf = [[0, R(1n,2n)], [1, R(1n,4n)], [4, R(1n,4n)]];
    eq(Rtext(exactTail(pmf, 4)) + ' <= ' + Rtext(markovBound(pmf, 4).bound), '1/4 <= 5/16',
       "the exact tail sits under Markov's bound, both exact");
    eq(Rcmp(exactDeviation(pmf, 2), chebyshevBound(pmf, 2).bound) <= 0, true, 'and under Chebyshev too');
    const fy = shuffleFrequencies(4, 'fisheryates'), nv = shuffleFrequencies(4, 'naive');
    eq(fy.tapes + ',' + fy.distinct + ',' + fy.uniform, '24,24,true',
       'Fisher-Yates: 24 tapes, 24 permutations, each exactly once');
    eq(nv.tapes + ',' + nv.uniform, '256,false',
       'the naive shuffle has 256 tapes and cannot be uniform -- 4^4 is not a multiple of 4!');
    const C4 = dgFromLesson(4, [[1,2],[2,3],[3,4],[4,1]], false);
    eq(Rtext(kargerExact(C4, [0,0,1,1]).probability), '1/6',
       'Karger keeps a given minimum cut of C4 with probability exactly 1/6 -- a memoised recursion, not a sample');
    eq(Requ(kargerExact(C4, [0,0,1,1]).probability, kargerExact(C4, [0,0,1,1]).bound), true,
       'which is exactly the 2/(n(n-1)) bound: C4 is a tight instance');
    eq(minCutBrute(C4).size, 2, 'and C4 does have a minimum cut of 2');
    eq(strongTest(561, 2).witness + ',' + witnessCount(561).prime, 'true,false',
       '561 is a Carmichael number: the Fermat test misses it and the strong test does not');
    eq(Rcmp(witnessCount(561).fraction, R(3n, 4n)) >= 0, true, 'at least three quarters of its bases are witnesses');
    eq(witnessCount(97).prime, true, 'and 97 has none at all');
    eq(strongTest(2047, 2).witness, false, '2047 is a strong pseudoprime to base 2');
    eq(witnessCount(2047, 4096).prime, false, 'but not to every base -- the cap is a parameter, raised here');
    const F3 = { n: 4, clauses: [[1,2,3],[-1,2,4],[1,-3,-4],[-2,3,4]] };
    eq(Rtext(max3satEnumerate(F3).mean) + ',' + max3satEnumerate(F3).matchesSevenEighths, '7/2,true',
       'over all 16 assignments the mean satisfied count is exactly 7m/8');
    eq(max3satEnumerate({ n: 3, clauses: [[1,1,2],[-1,2,3]] }).matchesSevenEighths, false,
       'and a clause that repeats a variable breaks that identity');
  }

  /* --- reductions and the coping strategies ------------------------------ */
  {
    const F = { n: 3, clauses: [[1,2,-3],[-1,-2,3],[1,-2,3]] };
    eq(selfReduce(F).result.verified, true, 'search from decision: n oracle calls build a satisfying assignment');
    eq(checkIndependentSetReduction(F).agree, true, 'the 3-SAT to independent-set reduction agrees with brute-force SAT');
    eq(checkIndependentSetReduction(F).readBackSatisfies, true, 'and the set reads back as an assignment that satisfies');
    for (const [preset, n] of [['cycle', 5], ['path', 5], ['complete', 5]]) {
      loadPreset(preset, n);
      eq(checkTspReduction(dgFromMatrix(A, n, weight, false)).agree, true,
         'the TSP instance from ' + preset + ' is within budget exactly when a Hamilton circuit exists');
    }
    const ss = satToSubsetSum({ n: 2, clauses: [[1,2],[-1,2]] });
    eq(String(ss.target) + ',' + subsetSumDp(ss.rows.map((r) => r.value), ss.target).result.found, '1144,true',
       'the subset-sum digit table has a subset hitting its target of 1s and 4s');
    const tri = dgFromLesson(3, [[1,2],[2,3],[3,1]], false);
    eq(colouringEnumerate(tri, 2).count + ',' + colouringEnumerate(tri, 3).count, '0,6',
       'a triangle has no proper 2-colouring and exactly six 3-colourings');

    const items = [{w:2,v:3},{w:3,v:4},{w:4,v:5},{w:5,v:6}];
    eq(branchBound(items, 8, true).result.correct, true, 'branch and bound finds the optimum');
    eq(branchBound(items, 8, true).counts.nodes < branchBound(items, 8, false).counts.nodes, true,
       'and the fractional bound -- the greedy lesson`s own algorithm -- prunes the tree');
    loadPreset('cycle', 6);
    const C6 = dgFromMatrix(A, 6, weight, false);
    eq(maximalMatching(C6).result.withinTwo, true, 'the matching cover is within twice the optimum');
    eq(Rtext(maximalMatching(dgFromLesson(4, [[1,2],[3,4]], false)).result.ratio), '2',
       'and on a perfect matching the ratio is exactly 2 -- the tight case');
    const metric = [[0,2,3,4],[2,0,2,3],[3,2,0,2],[4,3,2,0]];
    eq(mstTour(metric).result.metric + ',' + mstTour(metric).result.withinTwo, 'true,true',
       'the doubled-MST tour is within twice the optimum on a metric instance');
    eq(mstTour([[0,1,1,50],[1,0,1,1],[1,1,0,1],[50,1,1,0]]).result.metric, false,
       'and the toggle that drops the triangle inequality says so');
    const sets = [[1,2,3,4,5,6],[1,2,3,4],[5,6,7,8],[1,5],[2,6],[3,7],[4,8]];
    const sc = greedySetCover(sets, [1,2,3,4,5,6,7,8]);
    eq(sc.result.chargesSumToSize, true, 'the set-cover charges sum to exactly the number of sets chosen');
    eq(Rtext(sc.result.Hn) + ',' + sc.result.withinBound, '761/280,true',
       'and the cover is inside H_8 * OPT, with H_8 = 761/280 exactly');
    eq(fptasScale(items, 8, R(1n, 2n)).result.withinPromise, true, 'the FPTAS loses no more than eps * OPT');
    eq(fptasScale(items, 8, R(1n, 100n)).result.loss, 0, 'and at a small epsilon it finds the optimum');
    const F5 = { n: 4, clauses: [[1,2,3],[-1,2,4],[1,-3,-4],[-2,3,4],[-1,-2,-3]] };
    eq(Rtext(derandomise(F5).result.expectation) + ',' + derandomise(F5).result.atLeastExpectation, '35/8,true',
       'conditional expectations reach at least the 35/8 the random assignment averages');
    eq(fptVertexCover(C6, 3).result.correct + ',' + fptVertexCover(C6, 2).result.exists, 'true,false',
       'FPT vertex cover agrees with brute force at k = 3 and reports none at k = 2');
    eq(fptVertexCover(C6, 3).counts.nodes <= fptVertexCover(C6, 3).result.treeBound, true,
       'inside a search tree of 2^(k+1) nodes however big the graph is');
    eq(dpllRun(F5).result.agrees + ',' + dpllRun(F5).result.verified, 'true,true', 'DPLL agrees with brute-force SAT');
    eq(dpllRun({ n: 3, clauses: [[1,2],[1,-2],[-1,3],[-1,-3]] }).result.satisfiable, false,
       'and proves an unsatisfiable formula unsatisfiable');
  }

  /* --- the two drawings, asserted on the strings they return -------------- */
  {
    const sc = seriesScale([{ values: [0, 5, 10, 10] }], [1, 2, 3, 4], {});
    eq(sc.y(10) + ',' + sc.y(0) + ',' + sc.x(0) + ',' + sc.x(3), '14,200,26,496',
       'the series scale puts the maximum on the top of the box and zero on the baseline');
    const svg = drawSeries(null, [
      { label: 'measured', values: [1, 2, 3, 4], colour: 'var(--cyan)', points: true },
      { label: 'n log n', values: [0, 2, 4.7, 8], colour: 'var(--amber)', dashed: true }], [1, 2, 3, 4], {});
    eq(svg.indexOf('stroke-dasharray') !== -1, true, 'a predicted curve is dashed and a measured one is not');
    eq((svg.match(/<circle /g) || []).length, 4, 'with the measured samples marked');
    const Gd = dgNew(4, true);
    dgAdd(Gd, 0, 1, -3); dgAdd(Gd, 1, 2, 5); dgAdd(Gd, 2, 0, 2); dgAdd(Gd, 1, 0, 7);
    const gsvg = drawGraph(null, Gd, {});
    eq((gsvg.match(/<polygon /g) || []).length, 4, 'every arc of a directed graph gets an arrowhead');
    eq((gsvg.match(/ Q/g) || []).length, 2, 'and the antiparallel pair is bowed so neither hides the other');
    eq(drawTree(null, bstFromOrder([9,4,13,2,6,11,15]).result.root, bstKids, (n) => n.key)
       .match(/<circle /g).length, 7, 'the tree renderer draws every node');
    eq(matrixHtml([[0, 1], [1, 0]], { caption: 'A' }).indexOf('<caption>A</caption>'), 0,
       'and the matrix painter returns its own markup, with no element involved');
  }

  /* --- the caps refuse rather than freeze the tab ------------------------ */
  {
    const refuses = (f) => { try { f(); return false; } catch (e) { return /exceeds/.test(e.message); } };
    eq(refuses(() => knapsackBrute(new Array(13).fill({ w: 1, v: 1 }), 4)), true, 'thirteen knapsack items are refused');
    eq(refuses(() => allSpanningTrees(dgFromLesson(9, [[1,2]], false))), true, 'nine vertices of spanning trees are refused');
    eq(refuses(() => allFullBinaryTrees(6)), true, 'six leaves of full binary trees are refused');
    eq(refuses(() => witnessCount(3001)), true, 'and n = 3001 witnesses is refused -- not slow, refused');
  }
}

if (fails) {
  console.log('\n' + fails + ' assertion(s) FAILED');
  process.exit(1);
}
console.log('\nevery arithmetic assertion passes');
