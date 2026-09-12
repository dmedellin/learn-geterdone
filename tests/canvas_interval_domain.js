'use strict';
const ROOT=require('node:path').resolve(process.env.SOURCE_ROOT||require('node:path').join(__dirname,'..'));
const {lex,matching,htmlParts,functions}=require(ROOT+'/scripts/canvas_sources');
function intervalDomain(html){
 const definitions=[];
 for(const script of htmlParts(html).scripts.filter(s=>s.executable&&!s.attributes['data-canvas-text'])){
  const tokens=lex(script.source);
  for(let i=0;i<tokens.length;i++)if(tokens[i].value==='setInterval'&&tokens[i].kind==='identifier'){
   if(tokens[i+1]?.value!=='(')throw Error('unresolved interval access');const end=matching(tokens,i+1),args=tokens.slice(i+2,end);
   if(args.length!==3||args[0].kind!=='identifier'||args[1].value!==','||args[2].kind!=='identifier')throw Error('unresolved interval arguments');
   const owners=functions(script.source).filter(f=>f.start<tokens[i].charOffset&&f.end>tokens[end].charOffset).sort((a,b)=>(a.end-a.start)-(b.end-b.start));
   if(!owners.length)throw Error('missing interval source owner');const owner=owners[0],candidates=[];
   for(let j=0;j<i;j++)if(tokens[j].charOffset>owner.start&&tokens[j].value==='const'&&tokens[j+1]?.value===args[0].value&&tokens[j+2]?.value==='='){
    const start=j+3;if(tokens[start]?.value!=='('||tokens[start+1]?.value!==')'||tokens[start+2]?.value!=='=>'||tokens[start+3]?.value!=='{')throw Error('unsupported interval closure');const close=matching(tokens,start+3);
    candidates.push({id:owner.name+':'+args[0].value,source:script.source.slice(tokens[start].charOffset,tokens[close].charEnd),owner:owner.name,script:script.ordinal,offset:tokens[i].offset,delayState:args[2].value});
   }
   if(candidates.length!==1)throw Error('ambiguous interval closure');definitions.push(candidates[0]);
  }
 }
 return definitions;
}
module.exports={intervalDomain};
function boundedIntervalDomain(html){
 const definitions=intervalDomain(html),scripts=htmlParts(html).scripts;
 return definitions.map(definition=>{
  const script=scripts.find(s=>s.ordinal===definition.script),all=functions(script.source),owner=all.find(f=>f.name===definition.owner),tokens=lex(script.source.slice(owner.start,owner.end));
  const step=lex(definition.source),v=step.map(t=>t.value),number=x=>/^\d+$/.test(x)&&Number.isSafeInteger(Number(x));
  // Derive names at their lexical positions; accept only this closed bounded
  // transition shape. Other action machines need their own reviewed model.
  const actualCounter=v[4],actualCollection=v[10],actualDraw=v[19],actualStop=v[31];
  const pattern=['(',')','=>','{',actualCounter,'=','Math','.','min','(',actualCollection,'.','length',',',actualCounter,'+',v[16],')',';',actualDraw,'(',')',';','if','(',actualCounter,'>=',actualCollection,'.','length',')',actualStop,'(',')','}'];
  if(JSON.stringify(v)!==JSON.stringify(pattern)||!number(v[16])||Number(v[16])!==1)throw Error('unsupported bounded interval transition');
  const initials=[],factories=[];
  for(let i=0;i<tokens.length-2;i++){
   if(tokens[i].value===actualCounter&&tokens[i+1].value==='='&&tokens[i+2].kind==='number')initials.push(Number(tokens[i+2].value));
   if(tokens[i].value===actualCollection&&tokens[i+1].value==='='&&tokens[i+2].kind==='identifier'&&tokens[i+3]?.value==='(')factories.push(tokens[i+2].value);
  }
  if(!initials.length||initials.some(n=>n!==initials[0])||initials[0]!==1||!factories.length||new Set(factories).size!==1)throw Error('unresolved interval initial state');
  const matches=all.filter(f=>f.name===factories[0]);if(matches.length!==1)throw Error('ambiguous bounded collection factory');const f=matches[0],ft=lex(script.source.slice(f.start,f.end));
  const loops=[];
  for(let i=0;i<ft.length;i++)if(ft[i].value==='for'&&ft[i+1]?.value==='('){const end=matching(ft,i+1);loops.push({start:i,end,header:ft.slice(i+2,end).map(t=>t.value)});}
  if(loops.length!==1)throw Error('unresolved bounded collection loop');const loop=loops[0],h=loop.header;
  if(JSON.stringify(h)!==JSON.stringify(['let',h[1],'=','0',';',h[1],'<',h[7],';',h[1],'++'])||!number(h[7])||Number(h[7])<1)throw Error('unresolved bounded collection length');
  const open=loop.end+1;if(ft[open]?.value!=='{')throw Error('unbraced bounded collection loop');const close=matching(ft,open);
  const returns=ft.flatMap((t,i)=>t.value==='return'?[i]:[]);if(returns.length!==1||returns[0]<=close||ft[returns[0]+1]?.kind!=='identifier')throw Error('unresolved bounded collection return');const array=ft[returns[0]+1].value;
  let pushes=0,initializations=0;
  for(let i=0;i<ft.length;i++)if(ft[i].kind==='identifier'&&ft[i].value===array){
   if(ft[i+1]?.value==='='&&ft[i+2]?.value==='['&&ft[i+3]?.value===']'&&i<loop.start){initializations++;continue;}
   if(ft[i-1]?.value==='return')continue;
   if(ft[i+1]?.value==='.'&&ft[i+2]?.value==='push'&&ft[i+3]?.value==='('&&i>open&&i<close){
    if(![';','{'].includes(ft[i-1]?.value))throw Error('conditional bounded collection insertion');
    for(let k=open+1;k<i;k++)if(ft[k].kind==='punctuation'&&['{','(','['].includes(ft[k].value)){const end=matching(ft,k);if(end>=i)throw Error('nested bounded collection insertion');k=end;}
    pushes++;continue;
   }
   throw Error('unresolved bounded collection mutation');
  }
  if(pushes!==1||initializations!==1||ft.slice(open+1,close).some(t=>t.kind==='identifier'&&['break','continue','return'].includes(t.value)))throw Error('incomplete bounded collection construction');
  const terminal=Number(h[7]);return {...definition,counter:actualCounter,collection:actualCollection,draw:actualDraw,stop:actualStop,factory:factories[0],initial:initials[0],increment:1,terminal,states:Array.from({length:terminal},(_,i)=>i+1),reason:'Exactly one unconditional array insertion per integer loop iteration; original interval closure increments by one and clamps/stops at that array length. Each state is compared with the authored Step control.'};
 });
}
module.exports.boundedIntervalDomain=boundedIntervalDomain;
