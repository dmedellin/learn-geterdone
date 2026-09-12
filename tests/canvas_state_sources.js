'use strict';
const {lex,matching,functions,htmlParts}=require('../scripts/canvas_sources');
const crypto=require('node:crypto');
const fail=assertion=>{throw Object.assign(Error(assertion),{code:'LEARN_CANVAS_SEMANTIC',assertion})};
function argumentsAt(tokens,open){
 const close=matching(tokens,open),args=[];let start=open+1;
 for(let i=start;i<close;i++){
  if(tokens[i].kind==='template-start'){i=tokens[i].templateEnd;continue;}
  if(tokens[i].kind==='punctuation'&&['(','[','{'].includes(tokens[i].value)){i=matching(tokens,i);continue;}
  if(tokens[i].value===','){args.push(tokens.slice(start,i));start=i+1;}
 }
 if(start<close)args.push(tokens.slice(start,close));return {args,close};
}
// Closed affine arithmetic: state = a * DOM value + b. No evaluation of
// executable source, inferred truth from a default, or guessed branch limits.
function affine(tokens,constants=new Map(),variable=null){
 let i=0;
 const expression=minimum=>{
  let value;const token=tokens[i++];if(!token)throw Error('missing numeric expression');
  if(token.value==='('){value=expression(0);if(tokens[i++]?.value!==')')throw Error('unclosed numeric expression');}
  else if(['+','-'].includes(token.value)){value=expression(30);if(token.value==='-')value={a:-value.a,b:-value.b};}
  else if(token.kind==='number'&&Number.isFinite(Number(token.value)))value={a:0,b:Number(token.value)};
  else if(token.value==='.'&&tokens[i]?.kind==='number'){value={a:0,b:Number('.'+tokens[i++].value)};}
  else if(token.kind==='identifier'&&token.value===variable)value={a:1,b:0};
  else if(token.kind==='identifier'&&constants.has(token.value))value={a:0,b:constants.get(token.value)};
  else throw Error('unresolved numeric expression '+token.value);
  for(;;){const op=tokens[i]?.value,priority=({'+':10,'-':10,'*':20,'/':20})[op];if(!priority||priority<minimum)break;i++;const rhs=expression(priority+1);
   if(op==='+')value={a:value.a+rhs.a,b:value.b+rhs.b};
   if(op==='-')value={a:value.a-rhs.a,b:value.b-rhs.b};
   if(op==='*'){if(value.a&&rhs.a)throw Error('joint numeric expression');value={a:value.a*rhs.b+rhs.a*value.b,b:value.b*rhs.b};}
   if(op==='/'){if(rhs.a||!rhs.b)throw Error('non-affine numeric divisor');value={a:value.a/rhs.b,b:value.b/rhs.b};}
  }
  if(![value.a,value.b].every(Number.isFinite))throw Error('nonfinite numeric expression');return value;
 };
 const result=expression(0);if(i!==tokens.length)throw Error('unsupported numeric expression');return result;
}
function deriveNumericSource(source,ownerName){
 const tokens=lex(source),constants=new Map(),declarations=[],bindings=[],comparisons=[],unresolved=[];
 for(let i=0;i<tokens.length;i++)if(tokens[i].kind==='identifier'&&tokens[i].value==='const'){
  let cursor=i+1;
  for(;;){
   if(tokens[cursor]?.kind!=='identifier'||tokens[cursor+1]?.value!=='=')break;
   const name=tokens[cursor].value,start=cursor+2;let end=start;
   for(;end<tokens.length&&![';',','].includes(tokens[end].value);end++)if(tokens[end].kind==='punctuation'&&['(','[','{'].includes(tokens[end].value))end=matching(tokens,end);
   declarations.push({name,tokens:tokens.slice(start,end)});if(tokens[end]?.value!==',')break;cursor=end+1;
  }
 }
 for(let pass=0;pass<declarations.length;pass++){let changed=false;for(const d of declarations){if(constants.has(d.name))continue;try{const v=affine(d.tokens,constants);if(!v.a){constants.set(d.name,v.b);changed=true;}}catch{}}if(!changed)break;}
 for(let i=0;i<tokens.length;i++)if(tokens[i].kind==='identifier'&&tokens[i].value==='bindRange'&&tokens[i+1]?.value==='('&&tokens[i-1]?.value!=='function'){
  const {args}=argumentsAt(tokens,i+1),id=args[0]?.length===1&&args[0][0].kind==='string'?args[0][0].value:null,callback=args[1];
  if(!id||!callback){unresolved.push({assertion:'unresolved numeric control binding',offset:tokens[i].offset});continue;}
  let arrow=callback.findIndex(t=>t.value==='=>'),parameter=callback.slice(0,arrow).filter(t=>t.kind==='identifier');
  if(arrow<0||parameter.length!==1){unresolved.push({id,assertion:'unresolved numeric control callback'});continue;}
  const body=callback.slice(arrow+1),assignments=[];
  for(let j=0;j<body.length-2;j++)if(body[j].kind==='identifier'&&body[j+1].value==='='&&!['.','?.'].includes(body[j-1]?.value)){
   let end=j+2;for(;end<body.length&&![';',',','}'].includes(body[end].value);end++)if(body[end].kind==='punctuation'&&['(','[','{'].includes(body[end].value))end=matching(body,end);
   try{const mapping=affine(body.slice(j+2,end),constants,parameter[0].value);if(mapping.a)assignments.push({variable:body[j].value,...mapping});}catch(e){unresolved.push({id,assertion:'non-affine numeric control binding',expression:body.slice(j+2,end).map(t=>t.value).join(' '),detail:e.message});}
  }
  if(assignments.length!==1){unresolved.push({id,assertion:'numeric control needs exactly one source state binding',assignments});continue;}
  bindings.push({id,...assignments[0],offset:tokens[i].offset,owner:ownerName});
 }
 for(const binding of bindings){
  for(let i=0;i<tokens.length;i++)if(tokens[i].kind==='identifier'&&tokens[i].value===binding.variable){
   const after=tokens[i+1]?.value,before=tokens[i-1]?.value,operators=['<','<=','>','>=','==','!='];let other=null,operator=null,reverse=false;
   const startBoundary=value=>value===undefined||['(','${',':','?',',',';','{','&&','||','return','=>','='].includes(value);
   const endBoundary=value=>value===undefined||[')',']','}',':','?',',',';','&&','||'].includes(value);
   if(operators.includes(after)){
    operator=after;let start=i+2;if(tokens[start]?.value==='=')start++;let end=start;
    for(;end<tokens.length&&!endBoundary(tokens[end].value);end++)if(tokens[end].kind==='punctuation'&&tokens[end].value==='(')end=matching(tokens,end);
    if(!startBoundary(before)){unresolved.push({id:binding.id,assertion:'joint numeric comparison operand',offset:tokens[i].offset});continue;}
    other=tokens.slice(start,end);
   }
   else if(operators.includes(before)||before==='='&&operators.includes(tokens[i-2]?.value)){
    const at=before==='='?i-2:i-1;operator=tokens[at].value;reverse=true;
    let start=at-1;while(start>0&&!startBoundary(tokens[start-1].value))start--;
    if(!endBoundary(after)){unresolved.push({id:binding.id,assertion:'joint numeric comparison operand',offset:tokens[i].offset});continue;}
    other=tokens.slice(start,at);
   }
   if(!other)continue;
   try{const value=affine(other,constants);if(value.a)throw Error('joint branch threshold');const threshold=(value.b-binding.b)/binding.a;
    comparisons.push({id:binding.id,variable:binding.variable,operator,reverse,stateThreshold:value.b,threshold,offset:tokens[i].offset,reason:'source comparison mapped through exact affine control assignment'});
   }catch(e){unresolved.push({id:binding.id,assertion:'unresolved numeric branch threshold',offset:tokens[i].offset,detail:e.message});}
  }
 }
 return {owner:ownerName,sha256:crypto.createHash('sha256').update(source).digest('hex'),bindings,comparisons,unresolved,scope:'Direct affine control assignments and scalar comparisons only. Joint expressions, formatter domains, dependency products and action state remain separate required proofs.'};
}
function activeNumericSource(html,redraw){
 if(typeof redraw!=='string'||!redraw.trim())fail('missing active canvas implementation');
 const matches=[];
 for(const script of htmlParts(html).scripts.filter(s=>s.executable&&!s.attributes['data-canvas-text'])){
  let at=script.source.indexOf(redraw);
  while(at>=0){const owners=functions(script.source).filter(f=>f.start<=at&&f.end>=at+redraw.length).sort((a,b)=>(a.end-a.start)-(b.end-b.start));if(owners.length){const owner=owners[0];matches.push({script:script.ordinal,offset:Buffer.byteLength(script.source.slice(0,owner.start)),...deriveNumericSource(script.source.slice(owner.start,owner.end),owner.name)});}at=script.source.indexOf(redraw,at+1);}
 }
 if(matches.length!==1)fail('active canvas implementation source is ambiguous');return matches[0];
}
module.exports={argumentsAt,affine,deriveNumericSource,activeNumericSource};
