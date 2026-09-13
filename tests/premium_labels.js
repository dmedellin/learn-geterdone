// UI-only execution fixture: model arithmetic and chart geometry are separate gates.
const assert = require('node:assert/strict');
const vm = require('node:vm');
const data = JSON.parse(require('node:fs').readFileSync(0, 'utf8'));
class Element {
  constructor(n) {
    this.tagName = n.tag; this.attrs = n.attrs; this.initialText = n.text;
    this.children = n.children.map(c => new Element(c));
    this.style = {}; this.value = n.attrs.value || '';
  }
  get textContent() { return this.initialText; }
  set textContent(value) {
    // Every assignment removes descendants, including nonempty assignments.
    this.initialText = String(value); this.children = [];
  }
  set innerHTML(value) { this.textContent = value; }
}
const root = new Element(data.root);
const all = (n = root) => [n, ...n.children.flatMap(c => all(c))];
const match = (n, s) => s.startsWith('#') ? n.attrs.id === s.slice(1)
  : s.startsWith('.') ? (n.attrs.class || '').split(/\s+/).includes(s.slice(1))
  : s === '[aria-label="Premium components"]' && n.attrs['aria-label'] === 'Premium components';
const document = {
  getElementById: id => all().find(n => n.attrs.id === id),
  querySelector: s => all().find(n => match(n, s)),
  querySelectorAll: s => all().filter(n => match(n, s)),
};
const legend = document.querySelector('[aria-label="Premium components"]');
const labels = legend.children.filter(n => (n.attrs.class || '').includes('legend-item'));
const originals = labels.map(n => n.textContent);
let scenario;
const context = {document, Math, premiumType:'call', premiumReading:{intrinsic:'',none:''},
  num:(x,d) => Number(x) || d, pct:x => String(x), money:x => '$'+x.toFixed(2),
  optionModel:() => scenario, optionIntrinsic:() => 0, payoffPoints:() => [], drawPayoffChart:() => {},
  setText:(id,v) => { document.getElementById(id).textContent=v; },
  setHTML:(id,v) => { document.getElementById(id).innerHTML=v; }};
vm.createContext(context); vm.runInContext(data.function,context);
const seen = new Set();
for (scenario of [{price:10,intrinsic:0,extrinsic:10}, {price:10,intrinsic:.001,extrinsic:9.999},
                  {price:10,intrinsic:9.999,extrinsic:.001}, {price:10,intrinsic:10,extrinsic:0}]) {
  context.renderPremium();
  for (let i=0;i<labels.length;i++) {
    assert.ok(all().includes(labels[i]), 'premium labels must stay attached');
    assert.equal(labels[i].textContent,originals[i], 'premium labels must not be overwritten');
  }
  for (const [component,value] of [['Intrinsic',scenario.intrinsic],['Extrinsic',scenario.extrinsic]]) {
    assert.equal(document.getElementById('premium'+component).textContent, '$'+value.toFixed(2), 'separate numeric update');
    assert.equal(document.getElementById('premium'+component+'Bar').style.width, `${value/10*100}%`, 'decorative proportion update');
  }
  seen.add(document.getElementById('premiumIntrinsic').textContent);
}
assert.ok(seen.size > 1, 'numeric update sweep must change values');
console.log('4 premium scenarios passed; labels persist at zero and tiny proportions');
