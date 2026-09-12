/* Resolve the provisional style inventory against unmodified Chromium pixels.
 * All meaningful rows are measured, including native values. A missing capture
 * is a setup failure; an absent glyph/empty inventory is a semantic failure. */
'use strict';
const {measureTextPaint,contrastRatio}=require('./browser_contracts');
const {reconcileTextTiles}=require('./text_tile_contract');
async function refine(c,result){
 if(!result.rows.length)return {...result,failures:result.failures.length?result.failures:[{reason:'no meaningful text contrast samples'}]};
 const measured=[];
 for(let start=0;start<result.rows.length;start+=4){
 const batch=result.rows.slice(start,start+4);
 const samples=await c.evaluate(`(async()=>{
  ${contrastRatio.toString()}
  ${measureTextPaint.toString()}
  const rows=${JSON.stringify(batch)};
  return measureTextPaint(rows.map(row=>{
   const node=window.learnContrastNodes[row.nodeIndex];
   if(!node)throw Error('raster setup failure: missing semantic inventory node');
   return {nodeIndex:row.nodeIndex,threshold:row.threshold,element:node instanceof Element?node:node.parentElement,node:node instanceof Element?null:node};
  }));
 })()`);
 measured.push(...samples);
 }
 if(measured.length!==result.rows.length||new Set(measured.map(r=>r.nodeIndex)).size!==result.rows.length||measured.some(m=>!result.rows.some(r=>r.nodeIndex===m.nodeIndex)||(!m.error&&(!Number.isFinite(m.ratio)||!(m.sampleCount>0)||m.measurement!=='actual ink and backdrop raster'))))throw Error('raster setup failure: incomplete semantic measurements');
 measured.forEach(reconcileTextTiles);
 const rows=result.rows.map(row=>({...row,...measured.find(m=>m.nodeIndex===row.nodeIndex)}));
 const failures=rows.flatMap(row=>row.error?[{reason:'text contrast measurement error',...row}]:row.ratio+1e-6<row.threshold?[{reason:'text contrast below threshold',...row}]:[]);
 return {...result,rows,failures};
}
// A contrast registration has one semantic assertion per reason. Keep label
// identity and raster detail in evidence instead of emitting assertion aliases.
function reportFailures(failures){
 if(!Array.isArray(failures)||failures.some(f=>!f||typeof f.reason!=='string'||!f.reason.trim()))throw Error('contrast report setup failure: semantic reason missing');
 const protocol=require('./mutation_protocol');
 for(const f of failures)protocol.semantic(f.reason,{group:'contrast',nodeIndex:f.nodeIndex,id:f.id||null,ratio:f.ratio??null,threshold:f.threshold??null});
}
module.exports={refine,reportFailures};
