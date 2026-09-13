'use strict';
const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm'),assert=require('node:assert/strict');
const ROOT=process.env.SOURCE_ROOT||path.resolve(__dirname,'..'),{inventory,htmlParts,functions}=require(ROOT+'/scripts/canvas_sources'),{normalizeScript}=require(ROOT+'/scripts/canvas_normalize'),protocol=require(ROOT+'/tests/mutation_protocol');
let count=0;
try{
 const data=inventory(ROOT);assert.equal(data.errors.length,0,'constant range source inventory is valid');const owners=[];
 for(const page of data.pages.filter(p=>p.canvases.length))for(const script of htmlParts(fs.readFileSync(page.file,'utf8')).scripts.filter(s=>s.executable&&!s.attributes['data-canvas-text'])){
  const fs=functions(script.source),axes=fs.find(f=>f.name==='axes');if(!axes||!script.source.slice(axes.start,axes.end).includes('"family":"trading-risk-management"'))continue;
  const line=fs.find(f=>f.name==='line');assert(line,'constant range line owner exists');owners.push({route:page.route,script:script.source,line:script.source.slice(line.start,line.end),axes:script.source.slice(axes.start,axes.end)});
 }
 assert(owners.length>0,'constant range source inventory is nonempty');count++;
 const hashes=new Set(owners.map(o=>o.line+'\n'+o.axes));assert.equal(hashes.size,1,'repeated constant range implementations agree');count++;
 const owner=owners[0],context={fmt:v=>String(v),CanvasText:{site:d=>d,text:(_ctx,_token,value,x,y)=>context.labels.push({value,x,y})},labels:[]};vm.createContext(context);vm.runInContext(owner.line+'\n'+owner.axes,context);
 const area={x:24,y:22,w:414,h:144},points=[],ctx={save(){},restore(){},beginPath(){},stroke(){},moveTo(x,y){points.push([x,y])},lineTo(x,y){points.push([x,y])}};
 for(const value of [0,250,-250]){
  points.length=0;context.labels=[];context.line(ctx,[value,value,value],area,value,value,'#fff');
  assert(points.length===3&&points.every(p=>p.every(Number.isFinite)),'constant line coordinates are finite');count++;
  assert(points.every(p=>p[1]===area.y+area.h/2),'constant line is centered');count++;
  context.axes(ctx,area,value,value,{muted:'#fff'},v=>String(v));assert.equal(context.labels.length,1,'constant axis has one tick');count++;
  assert.equal(context.labels[0].value,String(value),'constant axis preserves the plotted value');assert.equal(context.labels[0].y,area.y+area.h/2,'constant axis and line are aligned');count++;
 }
 for(const value of [Infinity,-Infinity,NaN]){points.length=0;context.line(ctx,[value,value,value],area,value,value,'#fff');assert(points.some(p=>p.some(v=>!Number.isFinite(v))),'nonfinite constant series stays outside the coordinate contract');count++;}
 points.length=0;context.labels=[];context.line(ctx,[-10,0,10],area,-10,10,'#fff');assert.deepEqual(points,[[24,166],[231,94],[438,22]],'nonconstant line mapping is preserved');count++;
 context.axes(ctx,area,-10,10,{muted:'#fff'},v=>String(v));assert.deepEqual(context.labels.map(l=>l.value),['10','5','0','-5','-10'],'nonconstant axis values are preserved');count++;
 const legacy=owner.script.replace('sy=v=>max===min&&Number.isFinite(max)?area.y+area.h/2:area.y+(max-v)/(max-min)*area.h','sy=v=>area.y+(max-v)/(max-min)*area.h').replace('for(const i of min===max?[2]:[0,1,2,3,4]){','for(let i=0;i<=4;i++){');
 assert.notEqual(legacy,owner.script,'constant range maintenance fixture changes source');count++;
 assert.equal(normalizeScript(legacy,'trading-risk-management'),owner.script,'normalizer restores constant-range coordinate policy');count++;
 assert.equal(normalizeScript(owner.script,'trading-risk-management'),owner.script,'constant range normalizer is idempotent');count++;
 const policy='sy=v=>max===min&&Number.isFinite(max)?area.y+area.h/2:area.y+(max-v)/(max-min)*area.h';
 for(const [name,extra]of [['comment','/* '+policy+' */'],['string','const policyDescription='+JSON.stringify(policy)+';']]){
  const insert=source=>{const f=functions(source).find(f=>f.name==='line');return source.slice(0,f.bodyStart+1)+extra+source.slice(f.bodyStart+1)};
  assert.equal(normalizeScript(insert(legacy),'trading-risk-management'),insert(owner.script),'normalizer ignores '+name+' policy sentinels');count++;
 }
 console.log(count+'/'+count+' constant range source fixtures passed; '+owners.length+' authored implementations');
}catch(e){if(e.code==='ERR_ASSERTION')protocol.semantic(e.message.split('\n')[0]);else protocol.setup(e);process.exitCode=1}
