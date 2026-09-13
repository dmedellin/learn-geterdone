#!/usr/bin/env node
/* Real preflight, one real mutation, success and in-loop failure cleanup. */
'use strict';
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),{spawnSync}=require('node:child_process');
const ROOT=path.resolve(__dirname,'..'),OUT=process.env.BROWSER_EVIDENCE;
assert(OUT&&!path.resolve(OUT).startsWith(ROOT+'/'),'external evidence required');fs.mkdirSync(OUT,{recursive:true});
const hook=path.join(OUT,'failure.cjs');
fs.writeFileSync(hook,"const fs=require('node:fs'),path=require('node:path');const write=fs.writeFileSync;fs.writeFileSync=function(p,...args){const result=write.call(this,p,...args);if(path.basename(String(p))==='summary.json'&&path.dirname(String(p))===process.env.LIFECYCLE_CASE_DIR)throw Error('INJECTED after mutation case');return result};\n");
const rows=[];
for(const failure of [true,false]){
 const out=path.join(OUT,failure?'in-loop':'success');assert(!fs.existsSync(out),'fresh lifecycle evidence');
 const command=[path.join(ROOT,'tests/mutate_browser_ui.js'),'--case=runtime-named-process'];
 const started=Date.now();
 const run=spawnSync(process.execPath,command,{env:{...process.env,TMPDIR:'/tmp',SOURCE_ROOT:ROOT,BROWSER_EVIDENCE:out,...(failure?{NODE_OPTIONS:'--require='+hook,LIFECYCLE_CASE_DIR:out}:{})},encoding:'utf8',maxBuffer:256*1024*1024});
 fs.writeFileSync(path.join(OUT,(failure?'in-loop':'success')+'.log'),run.stdout+run.stderr);
 assert.equal(run.status,failure?1:0,'intended lifecycle exit');
 assert((run.stdout+run.stderr).includes(failure?'INJECTED after mutation case':'1/1 browser mutations caught'),'intended lifecycle reason');
 assert(fs.existsSync(path.join(out,'runtime-named-process','command.log')),'case diagnostic log retained');
 assert(!fs.existsSync(path.join(out,'disposable-export')),'no disposable residue');
 rows.push({failure,command,durationSeconds:(Date.now()-started)/1000,exit:run.status,residue:false,diagnosticsRetained:true});
 console.log('PASS '+(failure?'in-loop failure':'success')+' cleanup');
}
fs.writeFileSync(path.join(OUT,'summary.json'),JSON.stringify(rows,null,2)+'\n');
