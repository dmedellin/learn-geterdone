'use strict';
const assert=require('node:assert/strict');
const {implementationClosures}=require('../scripts/canvas_sources');
const program=`const prefix='$';
const alias=format;
function format(value){return prefix+value;}
function draw(value){return alias(value);}
function unrelated(){return 'outside';}`;
const closure=source=>implementationClosures(source).get('draw');
const normal=closure(program);
assert.deepEqual(normal.members.map(m=>m.name),['alias','draw','format','prefix']);
assert.equal(closure(program.replace("'outside'","'changed unrelated data'")).sha256,normal.sha256,'unreferenced implementation cannot change shared closure identity');
assert.notEqual(closure(program.replace("prefix='$'","prefix='EUR '")).sha256,normal.sha256,'indirect formatter data changes invalidate a borrowed witness');
assert.notEqual(closure(program.replace('return prefix+value','return prefix+Math.abs(value)')).sha256,normal.sha256,'aliased implementation changes invalidate a borrowed witness');
assert.notEqual(closure(program.replace('return alias(value)','if(value>0)return alias(value);return null')).sha256,normal.sha256,'a new conditional implementation requires its own witness');
assert.equal(closure('// a line before the executable implementation\n'+program).sha256,normal.sha256,'line numbers do not identify the implementation');
console.log('6/6 canvas source closure fixtures passed');
