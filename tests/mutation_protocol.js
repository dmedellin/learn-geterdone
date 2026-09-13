'use strict';
// Only complete JSON lines are protocol records. Prose is retained as diagnostic
// output, never searched for an expected assertion.
function records(output){
 return String(output).split(/\r?\n/).flatMap(line=>{
  try{const value=JSON.parse(line);return value&&typeof value==='object'&&!Array.isArray(value)?[value]:[];}catch{return [];}
 });
}
function errorData(error){
 if(!error)return null;
 return Object.fromEntries([...new Set(['name','message','code','errno','syscall','path','spawnargs','stack',...Object.getOwnPropertyNames(error)])].map(k=>[k,error[k]??null]));
}
function diagnose(run={},mutation={}){
 const stdout=run.stdout||'',stderr=run.stderr||'',output=stdout+'\n'+stderr,items=records(output);
 const semanticRecords=items.filter(r=>r.schema==='learn-semantic-v1'),setupRecords=items.filter(r=>r.schema==='learn-setup-v1');
 const reasons=[];
 if(run.status!==1)reasons.push('required semantic exit status is 1');
 if(run.signal)reasons.push('signal exit');
 if(run.error)reasons.push('spawn error');
 // Includes failures before a driver can load its structured reporter, and
 // unittest errors in setup/teardown after an earlier semantic assertion.
 // Terminal formatting cannot hide a runtime failure. Preserve the original
 // streams and require protocol JSON itself to remain an exact raw line.
 const runtimeOutput=output.replace(/\x1b\[[0-?]*[ -/]*[@-~]/g,'');
 if(/Chrome launch timeout|server launch timeout|CDP timeout|Document never completed|(?:Syntax|Type|Reference|Range|URI|Eval|Aggregate|Runtime|OSError|FileNotFound)Error\b|MODULE_NOT_FOUND|ERR_MODULE_NOT_FOUND|ENOENT|Cannot find module|Cannot find package|^\s*[\w.]*Error(?: \[[^\]]+\])?:|^\s*ERROR:|FAILED \([^\n]*errors=/m.test(runtimeOutput))reasons.push('runtime or loader failure');
 if(setupRecords.length)reasons.push('setup record');
 for(const line of output.split(/\r?\n/)){
  if(line.trimStart().startsWith('{')){try{JSON.parse(line);}catch{reasons.push('malformed JSON output');}}
  // A damaged/embedded protocol record must not be ignored beside a good one.
  if(/learn-(?:semantic|setup)-v1/.test(line)&&!records(line).some(r=>['learn-semantic-v1','learn-setup-v1'].includes(r.schema)))reasons.push('malformed or wrapped protocol record');
 }
 const assertions=new Set();
 for(const record of semanticRecords){
  if(record.observed!=='FAIL'||typeof record.assertion!=='string'||!record.assertion.trim())reasons.push('invalid semantic record');
  if(assertions.has(record.assertion))reasons.push('duplicate or conflicting semantic record');
  assertions.add(record.assertion);
 }
 const matches=semanticRecords.filter(r=>r.observed==='FAIL'&&r.assertion===mutation.expected);
 if(typeof mutation.expected!=='string'||!mutation.expected||matches.length!==1)reasons.push('exact expected assertion missing or repeated');
 return {caught:reasons.length===0,status:run.status??null,signal:run.signal??null,error:errorData(run.error),
  semanticRecords,setupRecords,records:items,reasons,stdout,stderr};
}
function validateInventory(cases){
 if(!Array.isArray(cases)||!cases.length)throw Error('nonempty declared mutation inventory');
 if(new Set(cases.map(c=>c.name)).size!==cases.length)throw Error('unique declared mutation names');
 for(const c of cases)for(const key of ['name','group','driver','expected'])if(typeof c[key]!=='string'||!c[key])throw Error('missing mutation '+key);
}
function caught(run,mutation){return diagnose(run,mutation).caught;}
// A driver may observe the same assertion at many widths/states. Emit its
// first standalone witness once; full measurements remain in command/evidence logs.
const emitted=new Set();
function semantic(assertion,details){
 if(emitted.has(assertion))return;
 emitted.add(assertion);
 console.log(JSON.stringify({schema:'learn-semantic-v1',assertion,observed:'FAIL',details}));
}
function setup(error){
 console.error(JSON.stringify({schema:'learn-setup-v1',error:String(error?.stack||error),errorData:errorData(error instanceof Error?error:null)}));
}
function failures(group,items){
 if(items.length)semantic('FAIL '+group,{count:items.length});
 for(const failure of items){
  if(typeof failure==='string')for(const assertion of failure.split(': '))semantic(assertion,failure);
  else for(const [key,value] of Object.entries(failure)){
   if(!['reason','text','id','class','reachable','entity'].includes(key))continue;
   const detail={group,nodeIndex:failure.nodeIndex,id:failure.id,key};
   if(typeof value==='string'&&value)semantic(value,detail);
   if(['string','boolean'].includes(typeof value))semantic(JSON.stringify(key)+':'+JSON.stringify(value),detail);
  }
 }
}
module.exports={validateInventory,caught,diagnose,errorData,records,semantic,setup,failures};
