'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),{descriptors}=require('../scripts/canvas_sources'),{normalizeScript}=require('../scripts/canvas_normalize'),protocol=require('./mutation_protocol');
const make=(shell,expression='score',x='30')=>shell.replace('CALL','CanvasText.text(ctx,CanvasText.site('+JSON.stringify({id:'fixture.draw.1',role:'value',minimumContrast:4.5,region:'status',collision:'separate',formatter:expression,family:'fixture',mode:'draw',dependencies:['frame.width','frame.height','theme']})+'),'+expression+','+x+',80)');
const cases=[
 ['outer formatter','function init(){let score=7;function draw(){const ctx={};CALL}}','score','30',['state.score']],
 ['outer coordinate','function init(){let anchor=7;function draw(){const ctx={};CALL}}','"Value"','anchor',['state.anchor']],
 ['two enclosing producers','function init(){let score=7;function middle(){function draw(){const ctx={};CALL}}}','score','30',['state.score']],
 ['var binding','function init(){var score=7;function draw(){const ctx={};CALL}}','score','30',['state.score']],
 ['nearest mutable binding','function init(){let score=7;function draw(){let score=8;const ctx={};CALL}}','score','30',['state.score']],
 ['constant shadow','function init(){let score=7;function draw(){const score=8,ctx={};CALL}}','score','30',[]],
 ['parameter shadow','function init(){let score=7;function draw(score){const ctx={};CALL}}','score','30',[]],
 ['default parameter shadow','function init(){let score=7;function draw(score=8){const ctx={};CALL}}','score','30',[]],
 ['property name is not state','function init(){let score=7;function draw(obj){const ctx={};CALL}}','obj.score','30',[]],
 ['inert string is not state','function init(){let score=7;function draw(){const ctx={};CALL}}','"score"','30',[]],
 ['unicode and line movement','const title="交易 🙂";\nfunction init(){let score=7;\nfunction draw(){const ctx={};CALL}}','score','30',['state.score']]
];
const rows=[];
try{for(const [name,shell,expression,x,expected]of cases){const source=make(shell,expression,x),before=descriptors(source),actual=before.errors.filter(e=>e.assertion==='canvas captured state dependency missing').map(e=>e.dependency).sort();assert.deepEqual(actual,expected,'enclosing canvas dependency: '+name);const normalized=normalizeScript(source,'fixture'),after=descriptors(normalized);assert.deepEqual(after.errors,[],'enclosing canvas maintenance: '+name);assert.equal(normalizeScript(normalized,'fixture'),normalized,'enclosing canvas maintenance is idempotent: '+name);assert.equal(after.bound[0].value.id,'fixture.draw.1','enclosing state retains semantic identity');rows.push({name,source,expected,normalized,definition:after.bound[0].value});}if(process.env.BROWSER_EVIDENCE){fs.mkdirSync(process.env.BROWSER_EVIDENCE,{recursive:true});fs.writeFileSync(process.env.BROWSER_EVIDENCE+'/scope-fixtures.json',JSON.stringify(rows,null,2))}console.log(cases.length+'/'+cases.length+' named enclosing-state fixtures passed');}
catch(e){if(e.code==='ERR_ASSERTION'||e.code==='LEARN_CANVAS_SEMANTIC')protocol.semantic(e.assertion||e.message.split('\n')[0]);else protocol.setup(e);process.exitCode=1}
