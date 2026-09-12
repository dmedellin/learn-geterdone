'use strict';
const assert=require('node:assert/strict'),{spawnSync}=require('node:child_process'),path=require('node:path');
const R=path.resolve(process.env.SOURCE_ROOT||path.join(__dirname,'..')),p=require('./mutation_protocol');
function run(rows){return spawnSync(process.execPath,['-e',"const {reportFailures}=require('./tests/browser_contrast_pixels'),p=require('./tests/mutation_protocol');try{const rows=JSON.parse(process.argv[1]);reportFailures(rows);if(rows.length)process.exitCode=1}catch(e){p.setup(e);process.exitCode=1}",JSON.stringify(rows)],{cwd:R,encoding:'utf8'});}
const green=run([]);assert.equal(green.status,0);assert.equal(green.stdout,'');assert.equal(green.stderr,'');
const red=run([{reason:'text contrast below threshold',text:'First label',class:'active',nodeIndex:4,ratio:2,threshold:4.5},{reason:'text contrast below threshold',text:'Another label',id:'different',nodeIndex:8,ratio:1,threshold:4.5}]);
assert.equal(red.status,1);assert.equal(p.records(red.stdout).length,1,'exactly one contrast semantic record');
assert(p.diagnose(red,{expected:'text contrast below threshold'}).caught,'exact contrast assertion is a semantic catch');
const invalid=run([{text:'Label lacking a reason'}]);assert.equal(invalid.status,1);assert.equal(p.records(invalid.stdout).length,0);assert.equal(p.records(invalid.stderr).filter(x=>x.schema==='learn-setup-v1').length,1);
console.log('3 contrast reporter fixtures passed');
