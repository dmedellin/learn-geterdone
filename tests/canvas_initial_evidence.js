'use strict';
function reconcileInitialStates(plan,rows){
 const fail=assertion=>{throw Object.assign(Error(assertion),{assertion,code:'LEARN_CANVAS_SEMANTIC'})};
 if(!Array.isArray(plan)||!plan.length||!Array.isArray(rows)||!rows.length)fail('empty canvas initial-state evidence');
 const expected=new Map(),actual=new Set();
 for(const [index,state]of plan.entries()){
  if(!state.page||!state.page.route||!/^[0-9a-f]{64}$/.test(state.page.sha256)||!Array.isArray(state.page.canvases)||!state.page.canvases.length||!Number.isInteger(state.width)||state.width<1||!Number.isInteger(state.height)||state.height<1||!['dark','system-light','explicit-light'].includes(state.theme))fail('invalid canvas initial-state plan');
  for(const canvas of state.page.canvases){const key=index+':'+canvas.id;if(!canvas.id||expected.has(key))fail('duplicate canvas initial-state plan');expected.set(key,{index,route:state.page.route,sourceHash:state.page.sha256,width:state.width,height:state.height,theme:state.theme,canvas:canvas.id,state:'initial'});}
 }
 for(const row of rows){
  const key=row.index+':'+row.canvas,match=expected.get(key);if(!match||actual.has(key))fail('missing or duplicate canvas initial-state identity');actual.add(key);
  if(Object.keys(match).some(k=>row[k]!==match[k]))fail('wrong canvas initial-state identity');
  if(typeof row.inactive!=='boolean'||!row.events||!['exceptions','blocked','responses'].every(k=>Array.isArray(row.events[k]))||row.events.exceptions.length||row.events.blocked.length||row.events.responses.some(r=>r.status>=400))fail('invalid canvas initial-state result');
  if(row.inactive){if(row.proof!==null||row.artifactProof!==null)fail('inactive canvas received a raster passing claim');}
  else if(!row.proof||!row.artifactProof||!['labels','tiles','samples'].every(k=>Number.isInteger(row.proof[k])&&row.proof[k]>0)||row.artifactProof.independentPNG!==true||!Number.isInteger(row.artifactProof.artifacts)||row.artifactProof.artifacts<1||['canvas','labels','tiles','samples'].some(k=>row.proof[k]!==row.artifactProof[k])||row.proof.canvas!==row.canvas)fail('missing canvas initial-state final pixels');
 }
 if(actual.size!==expected.size)fail('incomplete canvas initial-state coverage');
 const active=rows.filter(r=>!r.inactive);if(!active.length)fail('empty active canvas initial-state coverage');
 return {phase:'initial',finiteProofComplete:false,routes:new Set(plan.map(s=>s.page.route)).size,states:plan.length,canvases:rows.length,expectedCanvases:expected.size,active:active.length,inactive:rows.length-active.length,labels:active.reduce((n,r)=>n+r.proof.labels,0),samples:active.reduce((n,r)=>n+r.proof.samples,0),failures:0};
}
module.exports={reconcileInitialStates};
