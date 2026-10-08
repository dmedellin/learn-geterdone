#!/usr/bin/env node
/*
 * Run every published lab, headlessly, and fail if one throws.
 *
 * WHY THIS EXISTS. `node --check` proves a script parses. It does not prove the
 * lab draws anything, and a lab that throws on its first redraw ships a blank
 * panel that looks like a styling problem and passes every markup test in the
 * suite. Nothing else in this repository executes the JavaScript it publishes.
 *
 * WHAT IT IS NOT. This is a minimal DOM: enough of getElementById, createElement,
 * appendChild, textContent/innerHTML, classList, dataset and addEventListener for
 * the labs to initialise and redraw. It is not a browser, it lays nothing out,
 * and it renders nothing. A lab that runs here can still look wrong; a lab that
 * fails here is broken for every reader.
 *
 * SCOPE. --generated runs the pages listed in scripts/generated-pages.txt, which
 * scripts/build_discrete_math.py writes as it builds them. That is deliberate
 * and it is not a way of avoiding awkward results: the trading path's widgets
 * use DOM features this shim does not implement -- querySelector, namespaced
 * SVG nodes, listeners on elements it returns null for -- so running them here
 * produces failures that are facts about the harness rather than about those
 * pages, which shipped working. Extending the shim to cover them is worth
 * doing; reporting its gaps as their defects is not.
 *
 * --all still runs everything, for anyone extending the shim.
 *
 * EXPECTATIONS. A preset's <option> text says which instance it is. What the
 * page then PRINTS is a separate claim, and until now nothing compared the two:
 * fifteen kits shipped 57 false preset strings and every check in the repository
 * passed. scripts/build_paths.py writes scripts/generated-expectations.json --
 * page -> select id -> option value -> {kpi element id: exact text} -- and this
 * file selects each option, dispatches the control's own change handler, reads
 * getElementById(kpi).textContent out of the shipped page, and compares. It is
 * the page's own output that is checked, never the source that produced it.
 *
 * Usage:  node scripts/labcheck.js site/<course>/<lesson>/index.html ...
 *         node scripts/labcheck.js --generated    (the generated path)
 *         node scripts/labcheck.js --all          (every page under site/)
 *         node scripts/labcheck.js --expect <manifest.json>   (that manifest's
 *             pages, with its expectations; for a path not yet in
 *             GENERATED_PATHS, rendered anywhere, keys relative to the
 *             manifest's parent directory)
 *         node scripts/labcheck.js --observe <page.html>
 *             print every <select> option's KPI tiles as the page prints them,
 *             as JSON. This is how an author reads the figures an expectation
 *             pins: by running the kit, never by reading its source.
 */

const fs = require('fs');
const path = require('path');
const vm = require('vm');

// ---------------------------------------------------------------- the DOM

class ClassList {
  constructor(el) { this.el = el; }
  _list() { return (this.el.className || '').split(/\s+/).filter(Boolean); }
  add(...names) { const s = new Set(this._list()); names.forEach((n) => s.add(n)); this.el.className = [...s].join(' '); }
  remove(...names) { const s = new Set(this._list()); names.forEach((n) => s.delete(n)); this.el.className = [...s].join(' '); }
  contains(name) { return this._list().includes(name); }
  toggle(name) { this.contains(name) ? this.remove(name) : this.add(name); }
}

class Element {
  constructor(tag, doc) {
    this.tagName = (tag || 'div').toUpperCase();
    this._doc = doc;
    this.children = [];
    this.parentElement = null;
    this.attributes = {};
    this.dataset = {};
    this.style = new Proxy({}, { set: (t, k, v) => { t[k] = v; return true; } });
    this.className = '';
    this.classList = new ClassList(this);
    this._text = '';
    this._html = '';
    this._value = '';
    this.hidden = false;
    this.checked = false;
    this.listeners = {};
  }
  get textContent() { return this._text; }
  set textContent(v) { this._text = String(v); if (v === '') this.children = []; }
  get innerHTML() { return this._html; }
  set innerHTML(v) { this._html = String(v); }
  get value() { return this._value; }
  set value(v) { this._value = String(v); }
  appendChild(child) { child.parentElement = this; this.children.push(child); return child; }
  removeChild(child) { this.children = this.children.filter((c) => c !== child); return child; }
  setAttribute(name, value) { this.attributes[name] = String(value); }
  getAttribute(name) { return name in this.attributes ? this.attributes[name] : null; }
  addEventListener(type, fn) { (this.listeners[type] = this.listeners[type] || []).push(fn); }
  removeEventListener() {}
  dispatch(type, event) { (this.listeners[type] || []).forEach((fn) => fn.call(this, event || { target: this })); }
  closest() { return null; }
  querySelector() { return null; }
  querySelectorAll() { return []; }
  focus() {}
  get firstChild() { return this.children[0] || null; }
}

class Doc {
  constructor(ids) {
    this.byId = new Map();
    this.documentElement = new Element('html', this);
    this.body = new Element('body', this);
    for (const [id, tag] of ids) {
      const el = new Element(tag, this);
      el.id = id;
      // A control's initial value is what the markup gave it; the labs set the
      // ones they care about explicitly, and an empty string is a fine default
      // for the rest because every lab reads through a parse or a lookup.
      this.byId.set(id, el);
    }
  }
  getElementById(id) { return this.byId.get(id) || null; }
  createElement(tag) { return new Element(tag, this); }
  createElementNS(_ns, tag) { return new Element(tag, this); }
  querySelector() { return null; }
  querySelectorAll() { return []; }
  addEventListener() {}
}

// -------------------------------------------------------- page inspection

/* Element ids present in the document, with the tag that declares each, so a
   <select> behaves like a select and a <div> like a div. Parsed rather than
   guessed: a lab that reads an id the page does not declare must fail here. */
function idsOf(markup) {
  const body = markup.replace(/<script[\s\S]*?<\/script>/gi, ' ');
  const ids = [];
  const tagRe = /<([a-zA-Z][\w-]*)\b([^>]*)>/g;
  let m;
  while ((m = tagRe.exec(body))) {
    const attrs = m[2];
    const idm = /\bid="([^"]+)"/.exec(attrs);
    if (idm) ids.push([idm[1], m[1].toLowerCase()]);
  }
  return ids;
}

/* Every <select> on the page, with the values of its options in document
   order. One parser, used by the control sweep, by the expectation pass and by
   the gate that says an option without an expectation is a page failure. */
function selectsOf(markup) {
  const out = new Map();
  const selectRe = /<select\b([^>]*)>([\s\S]*?)<\/select>/gi;
  let m;
  while ((m = selectRe.exec(markup))) {
    const idm = /\bid="([^"]+)"/.exec(m[1]);
    if (!idm) continue;
    // A quoted attribute may hold a '>' (the truth-table kit ships formulas
    // such as p -> ~p as option values), so the tag ends at the first '>'
    // outside quotes, not at the first '>'.
    out.set(idm[1], [...m[2].matchAll(/<option\b((?:[^>"']|"[^"]*"|'[^']*')*)>/g)]
      .map((o) => { const v = /\bvalue="([^"]*)"/.exec(o[1]); return v ? v[1] : ''; }));
  }
  return out;
}

/* Every KPI tile: [element id, the label printed beside it]. This is the shape
   _kpis() emits in every kit on every generated path, and it is what --observe
   reports so an author writing an expectation sees the tile's own wording next
   to the figure. */
function kpisOf(markup) {
  return [...markup.matchAll(
    /<div class="kpi"><span>([\s\S]*?)<\/span><strong id="([^"]+)"/g)]
    .map((m) => [m[2], m[1]]);
}

/* Initial value of a <select> (its selected option, else its first) and of an
   <input> (its value attribute), so a lab that reads a control before writing
   it sees what a browser would see. */
function initialValues(markup) {
  const out = new Map();
  const selectRe = /<select\b([^>]*)>([\s\S]*?)<\/select>/gi;
  let m;
  while ((m = selectRe.exec(markup))) {
    const idm = /\bid="([^"]+)"/.exec(m[1]);
    if (!idm) continue;
    const options = [...m[2].matchAll(/<option\b([^>]*)>/g)].map((o) => o[1]);
    let chosen = options.find((a) => /\bselected\b/.test(a)) || options[0];
    if (chosen === undefined) continue;
    const v = /\bvalue="([^"]*)"/.exec(chosen);
    out.set(idm[1], v ? v[1] : '');
  }
  const inputRe = /<input\b([^>]*)>/gi;
  while ((m = inputRe.exec(markup))) {
    const idm = /\bid="([^"]+)"/.exec(m[1]);
    const vm2 = /\bvalue="([^"]*)"/.exec(m[1]);
    if (idm) out.set(idm[1], vm2 ? vm2[1] : '');
  }
  return out;
}

// Every value each control can take, which is what AGENTS.md §1a has always
// said this file checks and what it did not do until now: it ran the page once
// and called redrawLab() once, never setting a control or dispatching an event.
// The third clause of that sentence was false for every lab in the repository.
//
// Three authors noticed the gap independently and each wrote a private sweep in
// a scratchpad, ran it over their own kit, and threw it away. This is that
// sweep, kept.
//
// A range is swept at min, max and a middle step rather than every step: the
// failures this finds are at the ends and at a value the arithmetic divides by,
// and a hundred-step slider costs a hundred redraws to learn nothing more. Text
// boxes get the inputs that have actually broken labs here -- empty, a word, a
// bare operator -- because a parser that returns undefined on "banana" and a
// panel that then formats it is the shape of the bug.
function controlValues(markup) {
  const out = [];
  let m;
  for (const [id, values] of selectsOf(markup)) {
    if (values.length) out.push([id, values]);
  }
  const inputRe = /<input\b([^>]*)>/gi;
  while ((m = inputRe.exec(markup))) {
    const attrs = m[1];
    const idm = /\bid="([^"]+)"/.exec(attrs);
    if (!idm) continue;
    const type = (/\btype="([^"]*)"/.exec(attrs) || [, 'text'])[1];
    if (type === 'range') {
      const num = (name, fallback) => {
        const hit = new RegExp('\\b' + name + '="([^"]*)"').exec(attrs);
        const v = hit ? Number(hit[1]) : NaN;
        return Number.isFinite(v) ? v : fallback;
      };
      const lo = num('min', 0), hi = num('max', 100), step = num('step', 1) || 1;
      const mid = lo + Math.floor(((hi - lo) / step) / 2) * step;
      out.push([idm[1], [...new Set([lo, mid, hi])].map(String)]);
    } else if (type === 'checkbox' || type === 'radio') {
      out.push([idm[1], ['', 'on']]);
    } else {
      out.push([idm[1], ['', 'banana', '0', '-1', '1/0', 'A>B']]);
    }
  }
  return out;
}

function scriptsOf(markup) {
  return [...markup.matchAll(/<script>([\s\S]*?)<\/script>/g)].map((m) => m[1]);
}

// ------------------------------------------------------------------- run

/* One evaluation of one page: its scripts run, its first redraw done. Returned
   rather than consumed here, because the expectation pass needs a page whose
   controls are still at the values the markup shipped -- the sweep below leaves
   text boxes holding "banana" on its way past, and an expectation must be read
   from the page a reader actually opens. */
function loadPage(file) {
  const markup = fs.readFileSync(file, 'utf8');
  const doc = new Doc(idsOf(markup));
  for (const [id, value] of initialValues(markup)) {
    const el = doc.getElementById(id);
    if (el) el.value = value;
  }

  const sandbox = {
    document: doc,
    console: { log() {}, warn() {}, error() {} },
    localStorage: {
      _s: new Map(),
      getItem(k) { return this._s.has(k) ? this._s.get(k) : null; },
      setItem(k, v) { this._s.set(k, String(v)); },
      removeItem(k) { this._s.delete(k); },
    },
    performance: { now: () => 0 },
    setTimeout: (fn) => { fn(); return 0; },
    clearTimeout() {},
    requestAnimationFrame: (fn) => { fn(0); return 0; },
  };
  sandbox.window = sandbox;
  sandbox.globalThis = sandbox;
  sandbox.window.matchMedia = () => ({ matches: false, addEventListener() {}, removeEventListener() {} });

  const context = vm.createContext(sandbox);
  const problems = [];
  scriptsOf(markup).forEach((src, i) => {
    try {
      vm.runInContext(src, context, { filename: `${path.basename(path.dirname(file))}#script${i}`, timeout: 10000 });
    } catch (err) {
      problems.push(`script ${i}: ${err && err.message}`);
    }
  });

  // A lab that initialised must be able to redraw again -- that is the code
  // path every control change takes, and the one a first-paint-only test misses.
  if (typeof sandbox.redrawLab === 'function') {
    try { sandbox.redrawLab(); } catch (err) { problems.push(`redrawLab(): ${err && err.message}`); }
  } else if (/window\.redrawLab/.test(markup)) {
    problems.push('the page assigns window.redrawLab but it is not callable after load');
  }

  return { markup, doc, sandbox, problems };
}

/* Set one <select> to one value the way a reader does. DISPATCH, do not just
   redraw: several labs rebuild dependent controls in the change handler, and
   every preset menu in scripts/mathpath/labs rewrites the text boxes there --
   skip it and the figures read belong to the previous preset. */
function choose(page, el, value) {
  el.value = value;
  if (el.checked !== undefined) el.checked = value === 'on';
  if (el.listeners && (el.listeners.change || el.listeners.input)) {
    el.dispatch('change');
    el.dispatch('input');
  } else {
    page.sandbox.redrawLab();
  }
}

/* Which <select>s on this page are PRESET menus, decided by BEHAVIOUR rather
   than by name: a preset menu is one whose own change handler rewrites another
   control's value. Nothing here reads an id, a label or a line of source, so a
   second preset menu added under any name still has to be declared -- which is
   the hole a declaration-only gate leaves open. A menu that merely redraws (the
   greedy rule, the cache policy) rewrites nothing and is not one. */
function presetSelects(file, markup) {
  const found = [];
  for (const [selectId, values] of selectsOf(markup)) {
    if (values.length < 2) continue;
    const page = loadPage(file);
    if (page.problems.length || typeof page.sandbox.redrawLab !== 'function') continue;
    const el = page.doc.getElementById(selectId);
    if (!el) continue;
    const others = [...page.doc.byId.values()].filter(
      (e) => e !== el && (e.tagName === 'INPUT' || e.tagName === 'SELECT'));
    const before = others.map((e) => e.value);
    for (const value of values) {
      if (value === el.value) continue;
      try { choose(page, el, value); } catch (err) { break; }
      if (others.some((e, i) => e.value !== before[i])) { found.push(selectId); break; }
    }
  }
  return found;
}

// ------------------------------------------------------- the expectation pass
//
// A preset carries two claims. Its <option> text -- "density greedy at a
// fiftieth of the optimum" -- says which instance it is; no check can read it.
// Its expectations say what the page PRINTS once it is selected, and that is
// checked here, against the shipped page, by reading the element.
//
// THE GATE. Every option of every declared select must carry at least one
// expectation. Without it the mechanism decays into whichever presets an author
// felt like filling in, which is the state that let 57 false strings ship.
function checkExpectations(file, entry, markup) {
  const problems = [];
  const selects = entry && entry.selects ? entry.selects : {};
  const kit = (entry && entry.kit) || '(unnamed kit)';
  if (!Object.keys(selects).length) {
    problems.push(`${kit}: this kit is listed in build_paths.KITS_WITH_EXPECTATIONS `
      + 'but the page declares no preset expectations at all');
    return problems;
  }

  const onPage = selectsOf(markup);
  for (const selectId of presetSelects(file, markup)) {
    if (!(selectId in selects)) {
      problems.push(`${kit}: #${selectId} rewrites other controls when it changes, so it is a `
        + 'preset menu, and it declares no expectations');
    }
  }
  for (const [selectId, byOption] of Object.entries(selects)) {
    const options = onPage.get(selectId);
    if (!options) {
      problems.push(`${kit}: expectations name #${selectId}, which is not a <select> on this page`);
      continue;
    }
    for (const value of options) {
      const want = byOption[value];
      if (!want || !Object.keys(want).length) {
        problems.push(`${kit}: preset "${value}" of #${selectId} carries no expectation -- `
          + 'every option a reader can choose must pin at least one KPI it prints');
      }
    }
    for (const value of Object.keys(byOption)) {
      if (!options.includes(value)) {
        problems.push(`${kit}: an expectation names preset "${value}" of #${selectId}, `
          + 'which the page does not offer');
      }
    }
  }

  for (const [selectId, byOption] of Object.entries(selects)) {
    if (!onPage.has(selectId)) continue;
    // A fresh page per select: every other control at the value the markup
    // shipped, which is the state the expectation is a statement about.
    const page = loadPage(file);
    // A page that cannot load already fails above, and reporting the same
    // breakage twice buries it.
    if (page.problems.length) continue;
    if (typeof page.sandbox.redrawLab !== 'function') {
      problems.push(`${kit}: #${selectId} cannot be exercised -- the page has no redrawLab`);
      continue;
    }
    const el = page.doc.getElementById(selectId);
    if (!el) {
      problems.push(`${kit}: #${selectId} is in the markup but the harness has no element for it`);
      continue;
    }
    for (const value of onPage.get(selectId)) {
      const want = byOption[value];
      // An option with nothing pinned is already a failure above; there is
      // nothing here to read it against.
      if (!want || !Object.keys(want).length) continue;
      try {
        choose(page, el, value);
      } catch (err) {
        problems.push(`${kit}: #${selectId} = ${JSON.stringify(value)} threw before its `
          + `figures could be read: ${err && err.message}`);
        continue;
      }
      for (const [kpi, expected] of Object.entries(want)) {
        const tile = page.doc.getElementById(kpi);
        if (!tile) {
          problems.push(`${kit}: #${selectId} = ${JSON.stringify(value)} expects #${kpi}, `
            + 'which is not an element on this page');
          continue;
        }
        const found = tile.textContent;
        if (found !== expected) {
          problems.push(`${kit}: #${selectId} = ${JSON.stringify(value)}: #${kpi} should read `
            + `${JSON.stringify(expected)}, the page printed ${JSON.stringify(found)}`);
        }
      }
    }
  }
  return problems;
}

/* --observe. Every option of every <select>, and what the KPI tiles then hold.
   The author's instrument: the figures an expectation pins are read off a
   running kit here, never copied out of the code that computes them. */
function observePage(file) {
  const markup = fs.readFileSync(file, 'utf8');
  const kpis = kpisOf(markup);
  const out = { page: file, labels: {}, selects: {} };
  kpis.forEach(([id, label]) => { out.labels[id] = label; });
  for (const [selectId, values] of selectsOf(markup)) {
    if (!values.length) continue;
    const page = loadPage(file);
    if (page.problems.length) { out.selects[selectId] = { error: page.problems }; continue; }
    if (typeof page.sandbox.redrawLab !== 'function') continue;
    const el = page.doc.getElementById(selectId);
    if (!el) continue;
    const seen = {};
    for (const value of values) {
      try { choose(page, el, value); } catch (err) {
        seen[value] = { error: String(err && err.message) };
        continue;
      }
      const row = {};
      kpis.forEach(([id]) => {
        const tile = page.doc.getElementById(id);
        if (tile) row[id] = tile.textContent;
      });
      seen[value] = row;
    }
    out.selects[selectId] = seen;
  }
  return out;
}

function runPage(file, sweep, entry) {
  const page = loadPage(file);
  const { markup, doc, sandbox } = page;
  const problems = page.problems;

  // Now every value of every control, one control at a time, each restored
  // before the next. A page that throws on one slider position is broken for
  // the reader who moves that slider, and nothing else here would say so.
  if (sweep && typeof sandbox.redrawLab === 'function') {
    for (const [id, values] of controlValues(markup)) {
      const el = doc.getElementById(id);
      if (!el) continue;
      const was = el.value;
      // DISPATCH, do not just redraw. A browser fires the control's own change
      // handler, and several labs do real work there -- the probability kit
      // rebuilds its two event menus when the experiment changes, and calls
      // redraw() afterwards. Setting .value and calling redrawLab() skips that
      // rebuild and leaves an event index pointing into the previous
      // experiment's list, which throws. The first version of this sweep did
      // exactly that and reported two "failures" that no reader can reach.
      const listened = (el.listeners && (el.listeners.change || el.listeners.input)) ? true : false;
      for (const value of values) {
        el.value = value;
        if (el.checked !== undefined) el.checked = value === 'on';
        try {
          if (listened) {
            el.dispatch('change');
            el.dispatch('input');
          } else {
            sandbox.redrawLab();
          }
        } catch (err) {
          problems.push(`${id} = ${JSON.stringify(value)}: ${err && err.message}`);
          break;                       // one report per control, not per value
        }
      }
      el.value = was;
      if (listened) { try { el.dispatch('change'); } catch (err) { /* restored below */ } }
    }
    try { sandbox.redrawLab(); } catch (err) {
      problems.push(`redrawLab() after the sweep: ${err && err.message}`);
    }
  }

  // The quiz is data, and every question must be answerable: the correct index
  // has to point at a real choice.
  const quizMatch = /var QUIZ = (\[[\s\S]*?\]);\n/.exec(markup);
  if (quizMatch) {
    try {
      const quiz = JSON.parse(quizMatch[1].replace(/<\\\//g, '</'));
      quiz.forEach((q, i) => {
        if (!Array.isArray(q.a) || q.a.length < 2) problems.push(`quiz ${i}: fewer than two choices`);
        if (!(q.c >= 0 && q.c < q.a.length)) problems.push(`quiz ${i}: correct index ${q.c} is out of range`);
        if (!q.why) problems.push(`quiz ${i}: no explanation`);
      });
    } catch (err) {
      problems.push(`quiz data does not parse: ${err && err.message}`);
    }
  }

  if (entry) problems.push(...checkExpectations(file, entry, markup));
  return problems;
}

function collect(dir) {
  const out = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) out.push(...collect(full));
    else if (entry.name.endsWith('.html')) out.push(full);
  }
  return out;
}

/* The expectations manifest. Keys are page paths relative to the manifest's
   parent directory, exactly as scripts/generated-pages.txt spells them, so the
   two manifests are read the same way and a page is the same string in both. */
function readExpectations(manifestFile) {
  const root = path.resolve(path.dirname(manifestFile), '..');
  const raw = JSON.parse(fs.readFileSync(manifestFile, 'utf8'));
  const byFile = new Map();
  for (const [relative, entry] of Object.entries(raw.pages || {})) {
    byFile.set(path.resolve(root, relative), entry);
  }
  return byFile;
}

function main(argv) {
  const args = argv.slice(2);
  // The sweep is the default, because the claim in AGENTS.md is the default.
  const sweep = !args.includes('--no-sweep');
  let files = args.filter((a) => a !== '--no-sweep');

  const observeAt = files.indexOf('--observe');
  if (observeAt !== -1) {
    const targets = files.slice(observeAt + 1);
    if (!targets.length) {
      console.error('usage: node scripts/labcheck.js --observe <page.html> ...');
      return 2;
    }
    console.log(JSON.stringify(targets.map((f) => observePage(path.resolve(f))), null, 1));
    return 0;
  }

  // Where the expectations come from: --expect names a manifest anywhere, which
  // is how a path not yet in GENERATED_PATHS gets checked; otherwise
  // --generated picks up the one build_paths.py writes beside the page list.
  let expectFile = null;
  const expectAt = files.indexOf('--expect');
  if (expectAt !== -1) {
    expectFile = path.resolve(files[expectAt + 1] || '');
    if (!expectFile || !fs.existsSync(expectFile)) {
      console.error('no expectations manifest at ' + expectFile);
      return 2;
    }
    files.splice(expectAt, 2);
  }

  if (files[0] === '--all') {
    files = collect(path.join(__dirname, '..', 'site'));
  } else if (files[0] === '--generated') {
    const manifest = path.join(__dirname, 'generated-pages.txt');
    if (!fs.existsSync(manifest)) {
      console.error('no manifest at ' + manifest + '; run scripts/build_paths.py');
      return 2;
    }
    files = fs.readFileSync(manifest, 'utf8')
      .split('\n')
      .map((line) => line.trim())
      .filter(Boolean)
      .map((rel) => path.join(__dirname, '..', rel));
    if (!expectFile) {
      const generated = path.join(__dirname, 'generated-expectations.json');
      if (fs.existsSync(generated)) expectFile = generated;
    }
  }

  let expectations = new Map();
  if (expectFile) {
    try {
      expectations = readExpectations(expectFile);
    } catch (err) {
      console.error('the expectations manifest does not parse: ' + (err && err.message));
      return 2;
    }
    // A manifest on its own is a page list too: the pages it names are exactly
    // the ones whose figures are pinned.
    if (!files.length) files = [...expectations.keys()];
  }

  if (!files.length) {
    console.error('usage: node scripts/labcheck.js <page.html> ... '
      + '| --generated | --all | --expect <manifest.json> | --observe <page.html>');
    return 2;
  }
  let failed = 0;
  let pinned = 0;
  for (const file of files) {
    const entry = expectations.get(path.resolve(file)) || null;
    if (entry) pinned += 1;
    // A manifest naming a page that was never built is a stale manifest, and
    // saying so beats an ENOENT stack trace from the middle of the sweep.
    if (!fs.existsSync(file)) {
      failed += 1;
      console.log(`FAIL ${path.relative(process.cwd(), file)}`);
      console.log('      no such page; the manifest is stale, run scripts/build_paths.py');
      continue;
    }
    const problems = runPage(file, sweep, entry);
    if (problems.length) {
      failed += 1;
      console.log(`FAIL ${path.relative(process.cwd(), file)}`);
      problems.forEach((p) => console.log(`      ${p}`));
    }
  }
  console.log(`${files.length} page(s) executed${sweep ? ' and swept' : ''}`
    + `, ${pinned} with pinned figures, ${failed} failing`);
  return failed ? 1 : 0;
}

process.exit(main(process.argv));
