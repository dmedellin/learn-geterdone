'use strict';
const assert=require('node:assert/strict'),protocol=require('./mutation_protocol');
const {descriptors}=require('../scripts/canvas_sources'),{normalizeScript}=require('../scripts/canvas_normalize');
const definition={id:'fixture.initCMF.1',role:'status',minimumContrast:4.5,region:'status',collision:'separate',formatter:'`CMF (${period})`',family:'fixture',mode:'initCMF',dependencies:['frame.width','frame.height','theme']};
const program='function initCMF(){let mode="accumulation",period=14;const draw=()=>{const ctx={},panel={x:6,y:48};CanvasText.text(ctx,CanvasText.site('+JSON.stringify(definition)+'),`CMF (${period})`,panel.x,panel.y)}}';
try{
 assert(descriptors(program).errors.some(e=>e.assertion==='canvas captured state dependency missing'&&e.dependency==='state.period'),'captured formatter state must be declared');
 const repaired=normalizeScript(program,'fixture'),bound=descriptors(repaired);
 assert.deepEqual(bound.errors,[]);assert(bound.bound[0].value.dependencies.includes('state.period'));assert(!bound.bound[0].value.dependencies.includes('state.mode'),'unused mode is not a direct formatter dependency');
 assert.equal(normalizeScript(repaired,'fixture'),repaired,'captured-state maintenance is idempotent');
 const removed=repaired.replace(',"state.period"','');assert(descriptors(removed).errors.some(e=>e.dependency==='state.period'),'removing a captured dependency remains a rejection');
 assert.equal(descriptors('// line added\n'+repaired).bound[0].value.id,definition.id,'source movement retains semantic identity');
 console.log('7/7 direct captured-state descriptor fixtures passed');
}catch(e){if(e.code==='ERR_ASSERTION')protocol.semantic(e.message.split('\n')[0]);else protocol.setup(e);process.exitCode=1;}
