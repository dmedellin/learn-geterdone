'use strict';
const assert=require('node:assert/strict'),protocol=require('./mutation_protocol');
const {lex,accesses,descriptors}=require('../scripts/canvas_sources'),{deriveNumericSource}=require('./canvas_state_sources');
const {normalizeScript}=require('../scripts/canvas_normalize');
try{
 const tokens=lex('`ignored fillText ${first} / ${second > 5 ? `nested ${third}` : "no"}`');
 assert.equal(tokens.filter(t=>t.kind==='template-expression-start').length,3,'executable template interpolation has boundaries');
 assert.equal(tokens.filter(t=>t.kind==='template-expression-end').length,3,'every interpolation closes');
 assert.equal(accesses('`ignored fillText ${(()=>{const method="fill"+"Text";return context[method]})()}`').length,1,'computed native access inside interpolation remains executable');
 assert.equal(accesses('context[`${"fill"}${"Text"}`]("Bypass",0,0)').length,1,'constant interpolated native property is covered');
 const expression='`${left,right}`',definition={id:'fixture.template',role:'annotation',minimumContrast:4.5,region:'annotation',collision:'separate',formatter:expression,family:'fixture',mode:'draw',dependencies:['frame.width','frame.height','theme','parameter.left','parameter.right']};
 const parsed=descriptors('function draw(left,right){CanvasText.text(ctx,CanvasText.site('+JSON.stringify(definition)+'),'+expression+',30,60)}');
 assert.deepEqual(parsed.errors,[],'template expression comma is not an outer call delimiter');
 const source='function active(){let fresh=3;const MAX_AGE=5;const draw=()=>`${fresh<=MAX_AGE?"fresh":"old"}`;bindRange("age",v=>{fresh=v;draw()})}';
 const derived=deriveNumericSource(source,'active');assert.deepEqual(derived.unresolved,[],'template start is a real expression boundary');assert.deepEqual(derived.comparisons.map(c=>c.threshold),[5]);
 const raw='function canvasContext(){const canvas=$("#chart");return {ctx:canvas.getContext("2d")}} function draw(ctx,left,right){ctx.fillText('+expression+',30,60)}';
 const migrated=normalizeScript(raw,'fixture');assert.deepEqual(descriptors(migrated).errors,[],'migration keeps complete template formatter');assert.equal(normalizeScript(migrated,'fixture'),migrated,'template migration remains idempotent');
 console.log('9/9 executable interpolation fixtures passed');
}catch(e){if(e.code==='ERR_ASSERTION')protocol.semantic(e.message.split('\n')[0]);else protocol.setup(e);process.exitCode=1;}
