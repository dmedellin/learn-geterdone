'use strict';
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),crypto=require('node:crypto');
const ROOT=process.env.SOURCE_ROOT||path.resolve(__dirname,'..'),OUT=process.env.GEN5_EVIDENCE||process.env.BROWSER_EVIDENCE;
const {inventory,htmlParts,lex,matching}=require('../scripts/canvas_sources'),protocol=require('./mutation_protocol');
function removeText(source){
 const changes=[];
 for(const script of htmlParts(source).scripts.filter(s=>s.executable&&!s.attributes['data-canvas-text'])){
  const tokens=lex(script.source);
  for(let i=0;i<tokens.length-3;i++)if(tokens[i].value==='CanvasText'&&tokens[i+1].value==='.'&&tokens[i+2].value==='text'&&tokens[i+3].value==='('){const end=matching(tokens,i+3);changes.push({start:script.contentStart+tokens[i].charOffset,end:script.contentStart+tokens[end].charEnd});i=end;}
 }
 for(const c of changes.sort((a,b)=>b.start-a.start))source=source.slice(0,c.start)+'void 0'+source.slice(c.end);
 return {source,removed:changes.length};
}
function main(){
 if(!OUT||path.resolve(OUT).startsWith(ROOT+'/'))throw Error('external inventory fixture evidence required');fs.mkdirSync(OUT,{recursive:true});
 const baseline=inventory(ROOT);assert.equal(baseline.errors.length,0,'inventory fixture requires unchanged green source');assert.equal(baseline.contractOccurrences,269);
 const copy=fs.mkdtempSync(path.join(OUT,'canvas-empty-')),files=[];let observed=null;
 fs.writeFileSync(path.join(OUT,'empty-inventory-owned-root.json'),JSON.stringify({root:copy,device:fs.statSync(copy).dev,inode:fs.statSync(copy).ino}));
 try{
  fs.cpSync(path.join(ROOT,'site'),path.join(copy,'site'),{recursive:true});fs.mkdirSync(path.join(copy,'scripts'));fs.copyFileSync(path.join(ROOT,'scripts/canvas_contract.js'),path.join(copy,'scripts/canvas_contract.js'));
  let removed=0;
  for(const page of baseline.pages.filter(p=>p.occurrences.length)){
   const target=path.join(copy,'site',path.relative(path.join(ROOT,'site'),page.file)),before=fs.readFileSync(target,'utf8'),result=removeText(before);removed+=result.removed;
   fs.writeFileSync(target,result.source);files.push({route:page.route,removed:result.removed,before:crypto.createHash('sha256').update(before).digest('hex'),after:crypto.createHash('sha256').update(result.source).digest('hex')});
  }
  observed=inventory(copy);fs.writeFileSync(path.join(OUT,'empty-inventory-observation.json'),JSON.stringify({removed,files,result:observed}));
  assert.equal(removed,baseline.contractOccurrences,'every executable semantic call was removed');assert.equal(observed.contractOccurrences,0);assert.equal(observed.nativeProductOccurrences,0);
  assert(observed.errors.some(e=>e.assertion==='canvas semantic site continuity differs'&&e.observed===0),'empty canvas source inventory is rejected');
 }finally{
  const before={exists:fs.existsSync(copy),device:fs.statSync(copy).dev,inode:fs.statSync(copy).ino};fs.rmSync(copy,{recursive:true});fs.writeFileSync(path.join(OUT,'empty-inventory-cleanup.json'),JSON.stringify({root:copy,before,existsAfter:fs.existsSync(copy)}));
 }
 console.log('1/1 empty canvas source inventory fixture passed');
}
module.exports={removeText};if(require.main===module){try{main()}catch(e){if(e.code==='ERR_ASSERTION')protocol.semantic(e.message.split('\n')[0]);else protocol.setup(e);process.exitCode=1}}
