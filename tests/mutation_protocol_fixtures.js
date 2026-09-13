#!/usr/bin/env node
'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const {caught,diagnose}=require('./mutation_protocol');
const expected='fixture-only requires inventory or svg';
const record={schema:'learn-semantic-v1',assertion:expected,observed:'FAIL'};
const semantic=JSON.stringify(record),setup=JSON.stringify({schema:'learn-setup-v1',error:'planted setup failure'});
const cases=[
 ['genuine catch',{},semantic,true],
 ['wrong assertion',{},JSON.stringify({...record,assertion:'other'}),false],
 ['raw phrase',{},expected,false],
 ['nested expected text',{},`AssertionError: '${expected}' not found in 'Error: Chrome launch timeout...'`,false],
 ['JSON embedded in wrapper',{},'AssertionError: not found in '+JSON.stringify(semantic),false],
 ['setup only',{},setup,false],
 ['setup after semantic',{},semantic+'\n'+setup,false],
 ['setup before semantic',{},setup+'\n'+semantic,false],
 ...['SyntaxError: bad token','Error: Cannot find module required.js','ERR_MODULE_NOT_FOUND','ENOENT missing file',
     'CDP timeout Runtime.evaluate','Chrome launch timeout','server launch timeout','Document never completed /',
     'Error [ERR_DLOPEN_FAILED]: bad load','ImportError: bad load','ModuleNotFoundError: missing module','PermissionError: teardown','TypeError: teardown failed','ReferenceError: setup failed','Error: unexpected runtime failure','  Error: indented runtime failure','\x1b[31mError: colored runtime failure\x1b[0m','FAILED (errors=1)']
     .flatMap(error=>[['late '+error,{},semantic+'\n'+error,false],['early '+error,{},error+'\n'+semantic,false]]),
 ['malformed',{},'{"schema":"learn-semantic-v1"',false],
 ['malformed beside valid',{},semantic+'\n{"schema":"learn-semantic-v1"',false],
 ['embedded beside valid',{},semantic+'\nWrapper: '+semantic,false],
 ['malformed JSON beside semantic',{},semantic+'\n{bad JSON',false],
 ['empty',{},'',false],
 ['empty selection',{},JSON.stringify({schema:'learn-selection-v1',phase:'validated'}),false],
 ['duplicate',{},semantic+'\n'+semantic,false],
 ['conflicting',{},semantic+'\n'+JSON.stringify({...record,observed:'PASS'}),false],
 ['nonfailure',{},JSON.stringify({...record,observed:'PASS'}),false],
 ['empty assertion',{},JSON.stringify({...record,assertion:''}),false],
 ['success',{status:0},semantic,false],
 ['signal',{status:null,signal:'SIGINT'},semantic,false],
 ['null status',{status:null},semantic,false],
 ['spawn error',{status:null,error:Object.assign(Error('spawn failed'),{code:'ENOENT',errno:-2,syscall:'spawn missing',path:'missing'})},semantic,false],
 ['spawn error with semantic status',{error:Error('spawn failed')},semantic,false],
];
const results=[];
// Every declared driver group shares this predicate. Both streams are exercised
// independently; registration changes must extend this cross-product via inventory.
const groups=['source','inventory','svg','targets','capstone','theme','contract','contrast'];
for(const group of groups)for(const stream of ['stdout','stderr'])for(const [name,overrides,output,want] of cases){
 const run={status:1,signal:null,error:null,stdout:'',stderr:'',...overrides,[stream]:output};
 const actual=caught(run,{expected}),detail=diagnose(run,{expected});
 assert.equal(actual,want,group+' '+stream+' '+name);
 assert.equal(detail.status,run.status);assert.equal(detail.signal,run.signal);
 if(run.error){assert.equal(detail.error.message,run.error.message);assert.equal(detail.error.code,run.error.code??null);}
 assert.equal(detail.semanticRecords.length,detail.records.filter(r=>r.schema==='learn-semantic-v1').length);
 assert.equal(detail.setupRecords.length,detail.records.filter(r=>r.schema==='learn-setup-v1').length);
 results.push({group,stream,name,caught:actual,expected:want,status:detail.status,signal:detail.signal,error:detail.error});
}
if(process.env.BROWSER_EVIDENCE){fs.mkdirSync(process.env.BROWSER_EVIDENCE,{recursive:true});fs.writeFileSync(path.join(process.env.BROWSER_EVIDENCE,'protocol-fixtures.json'),JSON.stringify({groups,cases:cases.map(c=>c[0]),results},null,2)+'\n');}
console.log(`${results.length} adversarial classifications pass (${cases.length} cases × ${groups.length} groups × 2 streams)`);

const p=require('./mutation_protocol'),{spawnSync}=require('node:child_process');
const child=spawnSync(process.execPath,['-e',`const p=require(${JSON.stringify(path.join(__dirname,'mutation_protocol'))});p.semantic(${JSON.stringify(expected)},{});p.semantic(${JSON.stringify(expected)},{});process.exitCode=1;`],{encoding:'utf8',env:{...process.env,TMPDIR:'/tmp'}});
assert(caught(child,{expected}),'real semantic emission must survive and be unique');
assert.equal(diagnose(child,{expected}).semanticRecords.length,1,'emitter deduplicates repeated measurements');
const inventory=[{name:'fixture',group:'source',driver:'test_browser_source.py',expected}];
p.validateInventory(inventory);
assert.throws(()=>p.validateInventory([]),/nonempty declared mutation inventory/);
assert.throws(()=>p.validateInventory([...inventory,...inventory]),/unique declared mutation names/);
for(const key of ['name','group','driver','expected'])assert.throws(()=>p.validateInventory([{...inventory[0],[key]:''}]),/missing mutation/);
console.log('real emitter and inventory non-vacuity fixtures pass');
