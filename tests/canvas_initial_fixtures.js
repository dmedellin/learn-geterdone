'use strict';
const assert=require('node:assert/strict'),{reconcileInitialStates}=require('./canvas_initial_evidence'),protocol=require('./mutation_protocol');
const page={route:'/fixture/',sha256:'a'.repeat(64),canvases:[{id:'chart'}]},plan=[320,390].map(width=>({page,width,height:844,theme:'dark'}));
const rows=plan.map((s,index)=>({index,route:page.route,sourceHash:page.sha256,width:s.width,height:s.height,theme:s.theme,canvas:'chart',state:'initial',inactive:false,events:{exceptions:[],blocked:[],responses:[]},proof:{canvas:'chart',labels:1,tiles:1,samples:8},artifactProof:{canvas:'chart',labels:1,tiles:1,samples:8,artifacts:7,independentPNG:true}}));
const cases=[
 ['positive',()=>{},null],
 ['empty-plan',(p,r)=>p.length=0,'empty canvas initial-state evidence'],
 ['empty-results',(p,r)=>r.length=0,'empty canvas initial-state evidence'],
 ['missing-state',(p,r)=>r.pop(),'incomplete canvas initial-state coverage'],
 ['duplicate-state',(p,r)=>r[1]=structuredClone(r[0]),'missing or duplicate canvas initial-state identity'],
 ['wrong-route',(p,r)=>r[0].route='/other/','wrong canvas initial-state identity'],
 ['wrong-source',(p,r)=>r[0].sourceHash='b'.repeat(64),'wrong canvas initial-state identity'],
 ['wrong-theme',(p,r)=>r[0].theme='explicit-light','wrong canvas initial-state identity'],
 ['wrong-width',(p,r)=>r[0].width=319,'wrong canvas initial-state identity'],
 ['missing-events',(p,r)=>delete r[0].events.responses,'invalid canvas initial-state result'],
 ['runtime',(p,r)=>r[0].events.exceptions.push({error:'runtime'}),'invalid canvas initial-state result'],
 ['network',(p,r)=>r[0].events.responses.push({status:404}),'invalid canvas initial-state result'],
 ['missing-raster',(p,r)=>r[0].proof=null,'missing canvas initial-state final pixels'],
 ['missing-png',(p,r)=>r[0].artifactProof.independentPNG=false,'missing canvas initial-state final pixels'],
 ['empty-samples',(p,r)=>r[0].proof.samples=r[0].artifactProof.samples=0,'missing canvas initial-state final pixels'],
 ['nonfinite-samples',(p,r)=>r[0].proof.samples=r[0].artifactProof.samples=Infinity,'missing canvas initial-state final pixels'],
 ['artifact-mismatch',(p,r)=>r[0].artifactProof.samples++,'missing canvas initial-state final pixels'],
 ['inactive-passing-claim',(p,r)=>r[0].inactive=true,'inactive canvas received a raster passing claim'],
 ['no-active-canvases',(p,r)=>r.forEach(row=>{row.inactive=true;row.proof=row.artifactProof=null}),'empty active canvas initial-state coverage']
];
try{for(const [name,change,expected]of cases){const p=structuredClone(plan),r=structuredClone(rows);change(p,r);let observed=null,result;try{result=reconcileInitialStates(p,r)}catch(e){if(e.code!=='LEARN_CANVAS_SEMANTIC')throw e;observed=e.assertion}assert.equal(observed,expected,'canvas initial-state evidence: '+name);if(result){assert.equal(result.states,2);assert.equal(result.labels,2);assert.equal(result.samples,16);assert.equal(result.finiteProofComplete,false)}}console.log(cases.length+'/'+cases.length+' canvas initial-state evidence fixtures passed');}
catch(e){if(e.code==='ERR_ASSERTION'||e.code==='LEARN_CANVAS_SEMANTIC')protocol.semantic(e.assertion||e.message.split('\n')[0]);else protocol.setup(e);process.exitCode=1}
