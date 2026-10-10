// Print every figure the second-instalment English labs pin, by running the
// JavaScript the pages ship on the data they ship, outside a browser.
//
//   node scripts/wordlists/english_check.js            # every mode
//   node scripts/wordlists/english_check.js endings an # some of them
//
// The rule functions are read out of the strings in english_core.py, so this
// checks the code readers run, not a copy of it. Every line it prints is a
// tile id and the exact text the page's tile shows for that preset; the
// lesson figures are read off the built page with labcheck.js --observe and
// must agree with these. A rule broken on purpose in english_core.py must
// make a line here change, or this harness is not testing anything.
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const root = path.resolve(__dirname, '..', '..');
const core = fs.readFileSync(path.join(root, 'scripts/mathpath/labs/english_core.py'), 'utf8');
const block = (name) => core.split('\n' + name + ' = r"""')[1].split('"""')[0];
const ctx = {};
vm.createContext(ctx);
for (const name of ['SCAN_JS', 'ENDINGS_JS', 'WORDRULE_JS', 'AN_JS', 'SUPER_JS', 'TIME_JS',
                    'QUESTION_JS', 'AUX_JS']) {
  vm.runInContext(block(name), ctx);
}
const words = (f) => JSON.parse(fs.readFileSync(path.join(__dirname, f), 'utf8'));
const data = (f) => JSON.parse(fs.readFileSync(path.join(root, 'content/english/data', f), 'utf8'));
const modern = () => ['scotus_stanley.txt', 'census_aging.txt'].map((f) =>
  fs.readFileSync(path.join(root, 'content/english/data', f), 'utf8').split('\n---\n')[1].trim());

const show = (title, tiles) => {
  console.log(title);
  for (const [k, v] of Object.entries(tiles)) console.log('  ' + k.padEnd(10) + ' ' + v);
};

const MODES = {
  endings() {
    const d = words('verb_sounds.json');
    for (const r of ['ed', 's', 'plural']) show('endings ' + r, ctx.enTiles(d, r));
  },
  wordrule() {
    const pl = words('plural_nouns.json');
    for (const r of ['r0', 'r1', 'r2', 'r3']) show('wordrule plurals ' + r, ctx.wrTiles(pl, r));
    const ly = words('ly_adjectives.json');
    for (const r of ['plain', 'changes']) show('wordrule ly ' + r, ctx.wrTiles(ly, r));
  },
  an() {
    const c = data('an_concordance.json'), s = words('an_sounds.json').first;
    for (const src of ['all', 'wilde', 'modern', 'passage']) {
      for (const r of ['letter', 'sound']) show('an ' + r + ' / ' + src, ctx.anTiles(c.rows, s, r, src));
    }
  },
  the_super() {
    const c = data('superlative_concordance.json');
    for (const k of ['est', 'same', 'next', 'most']) show('the_super ' + k, ctx.tsTiles(c.rows, k));
  },
  time_preps() {
    const c = data('time_concordance.json');
    for (const s of ['all', 'austen', 'wilde', 'modern']) show('time_preps ' + s, ctx.tpTiles(c.rows, s));
  },
  questions() {
    show('questions austen', ctx.quTiles(data('question_concordance.json')));
    show('questions wilde', ctx.quTiles(data('wilde_questions.json')));
  },
  auxchain() {
    const d = data('long_passage.json'), m = modern().join('\n\n');
    for (const r of ['agree', 'modal', 'have', 'be', 'not', 'boxes']) {
      show('auxchain ' + r + ' / chapter', ctx.axRun(r, d.passage, d).tiles);
      show('auxchain ' + r + ' / modern', ctx.axRun(r, m, d).tiles);
    }
  },
};

const want = process.argv.slice(2);
for (const [name, run] of Object.entries(MODES)) if (!want.length || want.includes(name)) run();
