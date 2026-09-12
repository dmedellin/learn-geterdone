'use strict';
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const {lex,htmlParts,matching,functions,accesses,inventory,descriptors,attributeSourceErrors}=require('./canvas_sources.js');
function edits(source,changes){
 changes.sort((a,b)=>b.start-a.start||b.end-a.end);
 let limit=source.length;for(const c of changes){if(c.end>limit||c.start>c.end)throw Error('overlapping source migration');source=source.slice(0,c.start)+c.text+source.slice(c.end);limit=c.start;}return source;
}
function maintainDepthLayout(source){
 const owners=functions(source).filter(f=>f.name==='drawDepth');if(!owners.length)return source;
 if(owners.length!==1)throw Error('ambiguous depth chart layout owner');
 const owner=owners[0],body=source.slice(owner.start,owner.end),before='const {ctx,w,h}=canvasContext(),c=colors();const area=',after='const canvas=$("#chart");canvas.style.minWidth="600px";'+before;
 if(body.includes(after))return source;
 if(body.split(before).length!==2)throw Error('depth chart layout anchor changed');
 return edits(source,[{start:owner.start,end:owner.end,text:body.replace(before,after)}]);
}
function depthDefinition(definition){
 if(definition.family!=='volume-and-order-flow'||definition.mode!=='drawDepth')return definition;
 if(definition.formatter==='fmt(x.p,2)')return {...definition,role:'axis',region:'axis-bottom',collision:'fixed'};
 if(definition.formatter==='"RESTING DEPTH"')return {...definition,role:'status',region:'title-top',collision:'fixed'};
 throw Error('unknown depth text domain');
}
function maintainConstantRange(source,family){
 if(family!=='trading-risk-management')return source;
 // Match executable tokens: comments and string descriptions do not install a
 // coordinate policy, and harmless whitespace does not remove one.
 const spans=(body,pattern)=>{const tokens=lex(body),needle=lex(pattern),result=[];for(let i=0;i<=tokens.length-needle.length;i++)if(needle.every((n,j)=>n.kind===tokens[i+j].kind&&n.value===tokens[i+j].value))result.push({start:tokens[i].charOffset,end:tokens[i+needle.length-1].charEnd});return result};
 const changes=[];
 for(const [name,before,after]of [
  ['line',['sy=v=>area.y+(max-v)/(max-min)*area.h','sy=v=>max===min?area.y+area.h/2:area.y+(max-v)/(max-min)*area.h'],'sy=v=>max===min&&Number.isFinite(max)?area.y+area.h/2:area.y+(max-v)/(max-min)*area.h'],
  ['axes','for(let i=0;i<=4;i++){','for(const i of min===max?[2]:[0,1,2,3,4]){']
 ]){
  const owners=functions(source).filter(f=>f.name===name);if(!owners.length)continue;
  if(owners.length!==1)throw Error('ambiguous constant plot range owner');
  const owner=owners[0],body=source.slice(owner.start,owner.end);
  if(spans(body,after).length===1)continue;
  const variants=(Array.isArray(before)?before:[before]).flatMap(pattern=>spans(body,pattern));
  if(variants.length!==1)throw Error('constant plot range anchor changed');
  changes.push({start:owner.start,end:owner.end,text:body.slice(0,variants[0].start)+after+body.slice(variants[0].end)});
 }
 return edits(source,changes);
}
function normalizeScript(source,family){
 source=maintainConstantRange(maintainDepthLayout(source),family);
 const native=accesses(source);
 if(!native.length){
  const parsed=descriptors(source),changes=[];
  const invalid=parsed.errors.filter(e=>e.assertion!=='canvas captured state dependency missing');
  if(invalid.length)throw Error('canvas descriptor maintenance rejected: '+JSON.stringify(invalid));
  for(const occurrence of parsed.bound){
   if(!Array.isArray(occurrence.value.dependencies))throw Error('descriptor dependencies missing');
   const missing=occurrence.requiredDirectState.filter(d=>!occurrence.value.dependencies.includes(d));
   const definition=depthDefinition({...occurrence.value,dependencies:[...occurrence.value.dependencies,...missing]});
   if(JSON.stringify(definition)!==JSON.stringify(occurrence.value))changes.push({start:occurrence.definitionStart,end:occurrence.definitionEnd,text:JSON.stringify(definition)});
  }
  return edits(source,changes);
 }
 if(source.includes('CanvasText.text('))throw Error('mixed migrated and raw canvas source');
 const t=lex(source),fn=functions(source,t),changes=[],ordinals=new Map();
 const factories=fn.filter(f=>['canvasContext','sizeCanvas'].includes(f.name));
 if(factories.length!==1)throw Error('canvas source needs exactly one recognized context factory');
 const factory=factories[0];
 const factorySource=source.slice(factory.start,factory.end);
 if(factory.name==='canvasContext'){
  if(!factorySource.includes("$('#chart')")&&!factorySource.includes('$("#chart")'))throw Error('unknown chart factory identity');
  changes.push({start:factory.bodyStart+1,end:factory.bodyEnd,text:"const canvas=$('#chart'),rect=canvas.getBoundingClientRect(),dpr=2,w=Math.max(520,rect.width),h=Math.max(310,rect.height);const ctx=CanvasText.begin(canvas,w,h,dpr);return{ctx,w,h}"});
 }else if(family.endsWith('supplemental')){
  if(!factorySource.includes("c.style.height=h+'px'"))throw Error('unknown supplemental canvas height policy');
  changes.push({start:factory.bodyStart+1,end:factory.bodyEnd,text:"const d=2,r=c.getBoundingClientRect(),w=Math.max(520,r.width);c.style.height=h+'px';const x=CanvasText.begin(c,w,h,d);return{x,w,h}"});
 }else if(family.endsWith('slides')){
  if(!factorySource.includes('h=Math.max(300,r.height)'))throw Error('unknown deck canvas height policy');
  changes.push({start:factory.bodyStart+1,end:factory.bodyEnd,text:"const d=2,r=c.getBoundingClientRect(),w=Math.max(520,r.width),h=Math.max(300,r.height);const x=CanvasText.begin(c,w,h,d);return{x,w,h}"});
 }else throw Error('unknown canvas family');
 // Literal plot rectangles retain their authored margins until an axis
 // lane needs more room. This changes geometry only, never data arithmetic.
 if(factory.name==='canvasContext')for(let i=0;i<t.length;i++)if(t[i].value==='{'){
  const end=matching(t,i);let left=null,width=null;
  for(let j=i+1;j<end;j++){
   if(t[j].value==='x'&&t[j+1]?.value===':'&&t[j+2]?.kind==='number'&&[',','}'].includes(t[j+3]?.value))left=Number(t[j+2].value);
   if(t[j].value==='w'&&t[j+1]?.value===':'&&t[j+2]?.value==='w'&&t[j+3]?.value==='-'&&t[j+4]?.kind==='number'&&[',','}'].includes(t[j+5]?.value))width={start:t[j+2].charOffset,end:t[j+4].charEnd,subtract:Number(t[j+4].value)};
   if(['{','[','('].includes(t[j].value))j=matching(t,j);
  }
  if(left!==null&&width){if(width.subtract<left)throw Error('negative authored plot margin');changes.push({start:width.start,end:width.end,text:'CanvasText.plotWidth(ctx,w-'+width.subtract+','+(width.subtract-left)+')'});}
 }
 let migrated=0;
 for(let i=0;i<t.length-3;i++){
  if(t[i].kind!=='identifier'||t[i+1].value!=='.'||t[i+2].value!=='fillText'||t[i+3].value!=='(')continue;
  const close=matching(t,i+3),owner=fn.filter(f=>f.bodyStart<t[i].charOffset&&f.bodyEnd>t[i].charOffset).sort((a,b)=>(a.end-a.start)-(b.end-b.start))[0];
  if(!owner)throw Error('native text lacks implementation owner');
  const ordinal=(ordinals.get(owner.name)||0)+1;ordinals.set(owner.name,ordinal);
  const start=i+4;let argEnd=start;
  for(;argEnd<close;argEnd++){
   if(t[argEnd].value===',')break;
   if(t[argEnd].kind==='template-start'){argEnd=t[argEnd].templateEnd;continue;}
   if(['(','[','{'].includes(t[argEnd].value))argEnd=matching(t,argEnd);
  }
  const expression=source.slice(t[start].charOffset,t[argEnd].charOffset).trim();let role='annotation',region='annotation';
  if(['axes','drawAxes','drawPrice','drawSeries'].includes(owner.name)){role='axis';region='axis-right';}
  else if(['drawCandles','candles'].includes(owner.name)&&factory.name==='sizeCanvas'){
   if(ordinal===1){role='axis';region='axis-left';}else{role='date';region=ordinal===2?'date-bottom-left':'date-bottom-right';}
  }else if(['drawAnalog','analogChart'].includes(owner.name)){role=ordinal===1?'date':'value';region=ordinal===1?'date-left':'value-right';}
  else if(owner.name==='patternChart'){role=ordinal===1?'annotation':'value';region=ordinal===1?'label-left':'value-right';}
  else if(!['label','drawLabel'].includes(owner.name)){role='status';region='status';}
  const mode=owner.name==='initLabSpecific'?crypto.createHash('sha256').update(source.slice(owner.start,owner.end)).digest('hex').slice(0,16):owner.name;
  const definition={id:family+'.'+mode+'.'+ordinal,role,minimumContrast:4.5,region,collision:'separate',formatter:expression,family,mode,dependencies:['frame.width','frame.height','theme',...(() => {const part=lex(source.slice(owner.start,owner.bodyStart));const end=matching(part,2);const names=[];for(let k=3;k<end;k++){if(part[k].kind==='identifier'&&(k===3||part[k-1].value===','))names.push(part[k].value);if(['(','[','{'].includes(part[k].value))k=matching(part,k);}return names.filter(n=>![t[i].value,'c','color'].includes(n)).map(n=>'parameter.'+n);})()]};
  changes.push({start:t[i].charOffset,end:t[i+3].charEnd,text:'CanvasText.text('+t[i].value+',CanvasText.site('+JSON.stringify(definition)+'),'});migrated++;
 }
 if(migrated!==native.length)throw Error('unsupported native canvas access: migration must account for every lexical occurrence');
 // Every drawing callback owns a transaction. Nested chart producers defer
 // finalization to that callback so annotations still queue in the same frame.
 const wraps=[];
 for(let i=0;i<t.length-5;i++)if(t[i].value==='draw'&&t[i+1].value==='='&&t[i+2].value==='('){
  const params=matching(t,i+2);if(t[params+1]?.value==='=>'&&t[params+2]?.value==='{'){
   const end=matching(t,params+2);wraps.push([t[params+2].charOffset,t[end].charEnd]);
  }
 }
 for(const f of fn){
  if(f===factory)continue;
  // Direct producers may also be invoked independently by capstone controls.
  const bodyTokens=t.filter(x=>x.charOffset>f.bodyStart&&x.charOffset<f.bodyEnd);
  const ownCalls=bodyTokens.some((x,i)=>x.value===factory.name&&bodyTokens[i+1]?.value==='('&&!wraps.some(([s,e])=>s<x.charOffset&&e>x.charOffset)&&!fn.some(g=>g!==f&&g.start>f.start&&g.start<x.charOffset&&g.end>x.charOffset));
  if(ownCalls&&!wraps.some(([s,e])=>s<f.bodyStart&&e>f.bodyEnd))wraps.push([f.bodyStart,f.bodyEnd+1]);
 }
 // Nested wrappers are harmless and make each source producer auditable.
 for(const [start,end] of wraps){changes.push({start:start+1,end:start+1,text:'return CanvasText.frame(()=>{'});changes.push({start:end-1,end:end-1,text:'});'});}
 return normalizeScript(edits(source,changes),family);
}
function normalizeHtml(source,relative){
 const parts=htmlParts(source);
 const boundary=[...parts.boundaryErrors,...parts.attributesCode.flatMap(attributeSourceErrors)];
 if(boundary.length)throw Object.assign(Error('canvas maintenance: '+boundary[0].assertion),{code:'LEARN_CANVAS_SEMANTIC',assertion:boundary[0].assertion,detail:boundary[0]});
 if(!parts.canvases.length)return source;
 if(!relative||relative.includes('..'))throw Error('source identity required');
 const family=relative.startsWith('paths/trading/')?'iren-'+(/data-page-kind="slides"/.test(source)?'slides':'supplemental'):relative.split('/')[0];
 const canonical=fs.readFileSync(path.join(__dirname,'canvas_contract.js'),'utf8').trim(),changes=[];
 for(const script of parts.scripts.filter(s=>s.executable)){
  if(script.attributes['data-canvas-text']==='v1'){changes.push({start:script.contentStart,end:script.contentEnd,text:'\n'+canonical+'\n'});continue;}
  const after=normalizeScript(script.source,family);if(after!==script.source)changes.push({start:script.contentStart,end:script.contentEnd,text:after});
 }
 if(!parts.scripts.some(s=>s.attributes['data-canvas-text']==='v1')){
  const target=parts.scripts.find(s=>s.executable);if(!target)throw Error('canvas document has no executable source');
  changes.push({start:target.start,end:target.start,text:'<script data-canvas-text="v1">\n'+canonical+'\n</script>\n'});
 }
 return edits(source,changes);
}
module.exports={normalizeScript,normalizeHtml};
if(require.main===module){const source=fs.readFileSync(0,'utf8');process.stdout.write(normalizeHtml(source,process.argv[2]));}
