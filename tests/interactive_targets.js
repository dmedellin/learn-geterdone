/* Reusable by the independent browser harness after every rendered interaction.
 * Return controls AND their possible labeled hit-area owners. The harness must
 * measure each visible owner and exercise the associated control; this inventory
 * makes no claim about 44px geometry. Disabled/hidden reasons remain auditable.
 */
(function(root) {
  const SELECTOR = 'a[href],button,input:not([type="hidden"]),select,textarea,summary,[role="button"],[role="checkbox"],[role="radio"],[role="slider"],[role="switch"],[role="tab"],[role="link"],[role="textbox"],[role="combobox"],[tabindex],[contenteditable="true"]';
  const LABEL_OWNER_TYPES = new Set(['checkbox', 'radio']);
  function inventory(scope = document) {
    return Array.from(scope.querySelectorAll(SELECTOR), control => {
      const labels = Array.from(control.labels || []);
      const owners = LABEL_OWNER_TYPES.has(control.type) && labels.length ? [control, ...labels] : [control];
      return {control, kind: control.type || control.getAttribute('role') || control.tagName.toLowerCase(),
        owners: [...new Set(owners)], labels, disabled: Boolean(control.disabled),
        ownerPolicy: owners.length > 1 ? 'native control or associated label' : 'control'};
    });
  }
  const api = {SELECTOR, inventory};
  if (typeof module !== 'undefined') module.exports = api;
  root.learnInteractiveTargets = api;
  if (typeof process !== 'undefined' && process.argv.includes('--test')) {
    const assert = require('node:assert/strict');
    // Assert selector categories independently, including types absent from the
    // current site (radio). Runtime-generated cells are covered by role/button.
    for (const selector of ['a[href]', 'button', 'input:not([type="hidden"])', 'select', 'textarea', 'summary', '[role="button"]', '[tabindex]', '[contenteditable="true"]'])
      assert.ok(SELECTOR.split(',').includes(selector), 'missing interactive category: '+selector);
    const label = {tagName:'LABEL'}, wrapped = {tagName:'LABEL'};
    const kinds = ['range','number','text','checkbox','radio','search','file','date'];
    const controls = kinds.map(type => ({tagName:'INPUT', type, labels: type === 'checkbox' ? [wrapped] : [label], getAttribute:() => null}));
    controls.push({tagName:'TD', labels:[], getAttribute:name => name === 'role' ? 'button' : null});
    const results = inventory({querySelectorAll: selector => { assert.equal(selector, SELECTOR); return controls; }});
    assert.equal(results.length, controls.length);
    for (const item of results) {
      assert.equal(item.control, controls[results.indexOf(item)]);
      assert.ok(item.owners.includes(item.control));
      if (['checkbox','radio'].includes(item.kind)) {
        assert.ok(item.owners.includes(item.labels[0]), 'associated label must own a possible hit area');
        assert.equal(item.ownerPolicy, 'native control or associated label');
      } else assert.deepEqual(item.owners, [item.control]);
    }
    console.log('9 inventory ownership fixtures passed; browser geometry remains external');
  }
})(globalThis);
