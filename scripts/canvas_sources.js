'use strict';
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
function lex(source){
 const tokens=[];let i=0;const byteAt=new Uint32Array(source.length+1);for(let k=0;k<source.length;k++){const cp=source.codePointAt(k),n=cp>65535?2:1,b=cp<128?1:cp<2048?2:cp<65536?3:4;byteAt[k+1]=byteAt[k]+b;if(n===2){byteAt[k+2]=byteAt[k+1];k++}}
 const add=(kind,value,start)=>tokens.push({kind,value,charOffset:start,offset:byteAt[start],end:byteAt[i],charEnd:i});
 function escaped(){
  const e=source[i++];let hex;
  if(e==='x'){hex=source.slice(i,i+2);i+=2;if(!/^[\da-f]{2}$/i.test(hex))throw Error('invalid hex escape');return String.fromCharCode(parseInt(hex,16));}
  if(e==='u'){
   if(source[i]==='{'){const end=source.indexOf('}',++i);if(end<0)throw Error('unterminated unicode escape');hex=source.slice(i,end);i=end+1;if(!/^[\da-f]+$/i.test(hex))throw Error('invalid unicode escape');}
   else{hex=source.slice(i,i+4);i+=4;if(!/^[\da-f]{4}$/i.test(hex))throw Error('invalid unicode escape');}
   return String.fromCodePoint(parseInt(hex,16));
  }
  if(e==='\r'&&source[i]==='\n')i++;
  return ({n:'\n',r:'\r',t:'\t',b:'\b',f:'\f',v:'\v','\n':'','\r':''}[e]??e);
 }
 function quoted(quote){const start=i++;let value='';while(i<source.length){const c=source[i++];if(c===quote){add('string',value,start);return}value+=c==='\\'?escaped():c}throw Error('unterminated string at '+start)}
 function template(){
  const start=i++,index=tokens.length,parts=[];let literal='',constant=true;add('template-start','`',start);
  while(i<source.length){
   const c=source[i++];if(c==='\\'){literal+=escaped();continue;}
   if(c==='`'){parts.push({literal});add('template-end','`',i-1);tokens[index].literal=constant?literal:null;tokens[index].parts=parts;tokens[index].templateEnd=tokens.length-1;return;}
   if(c==='$'&&source[i]==='{'){
    i++;constant=false;parts.push({literal});literal='';add('template-expression-start','${',i-2);const first=tokens.length;
    scan(true);const end=tokens.length;parts.push({start:first,end});add('template-expression-end','}',i-1);
   }else literal+=c;
  }
  throw Error('unterminated template at '+start);
 }
 function scan(interpolation=false){let braces=0,regexAllowed=true;const parens=[];while(i<source.length){const c=source[i],start=i;
  if(/\s/.test(c)){i++;continue}
  if(c==='/'&&source[i+1]==='/'){i+=2;while(i<source.length&&!/[\r\n]/.test(source[i]))i++;continue}
  if(c==='/'&&source[i+1]==='*'){const end=source.indexOf('*/',i+2);if(end<0)throw Error('unterminated comment');i=end+2;continue}
  if(c==='"'||c==="'"){quoted(c);regexAllowed=false;continue}
  if(c==='`'){template();regexAllowed=false;continue}
  if(c==='/'&&regexAllowed){i++;let cls=false,closed=false;while(i<source.length){const r=source[i++];if(r==='\\'){i++;continue}if(r==='[')cls=true;else if(r===']')cls=false;else if(r==='/'&&!cls){closed=true;break}}if(!closed)throw Error('unterminated regexp at '+start);while(/[a-z]/i.test(source[i]||'')&&i<source.length)i++;add('regexp','/…/',start);regexAllowed=false;continue}
  if(/[a-zA-Z_$\u0080-\uffff]/.test(c)||c==='\\'&&source[i+1]==='u'){
   let v='';while(i<source.length){
    if(source[i]==='\\'&&source[i+1]==='u'){
     i+=2;let hex;
     if(source[i]==='{'){const end=source.indexOf('}',++i);if(end<0)throw Error('unterminated identifier escape');hex=source.slice(i,end);i=end+1;}
     else{hex=source.slice(i,i+4);i+=4;}
     if(!/^[a-fA-F0-9]+$/.test(hex))throw Error('invalid identifier escape');v+=String.fromCodePoint(parseInt(hex,16));
    }else if(/[\w$\u0080-\uffff]/.test(source[i]))v+=source[i++];else break;
   }
add('identifier',v,start);regexAllowed=['return','throw','case','delete','void','typeof','new','in','of','yield','await','else','instanceof'].includes(v);continue}
  if(/[0-9]/.test(c)){i++;while(i<source.length&&/[\w.]/.test(source[i]))i++;add('number',source.slice(start,i),start);regexAllowed=false;continue}
  if(c==='}'&&interpolation&&braces===0){i++;return}
  const previous=tokens.at(-1)?.value;
  if(c==='{')braces++;if(c==='}')braces--;
  if(c==='(')parens.push(['if','while','for','with','switch','catch'].includes(previous));
  const controlClose=c===')'?parens.pop():false;
  const pair=source.slice(i,i+2),v=['?.','=>','++','--','==','!=','>=','<=','&&','||','??','**'].includes(pair)?pair:c;i+=v.length;add('punctuation',v,start);
  regexAllowed=controlClose||![')',']','}','++','--','.','?.'].includes(v);
 }
 if(interpolation)throw Error('unterminated interpolation')}
 scan();return tokens;
}
function accesses(source){
 const t=lex(source),out=[],native=new Set(['fillText','strokeText']),constants=new Map();
 // A small closed constant-string evaluator. Unsupported computed accesses on
 // canvas context bindings are rejected instead of assumed harmless.
 const constant=(start,end)=>{
  let values=new Set(['']),expect=true;
  for(let i=start;i<end;i++){
   if(expect){
    let part=t[i].kind==='string'?new Set([t[i].value]):t[i].kind==='identifier'?constants.get(t[i].value):null;
    if(t[i].kind==='template-start'&&t[i].templateEnd<end){
     part=new Set(['']);
     for(const chunk of t[i].parts){
      const next=Object.hasOwn(chunk,'literal')?new Set([chunk.literal]):constant(chunk.start,chunk.end);
      if(!next){part=null;break;}
      const combined=new Set();for(const a of part)for(const b of next)combined.add(a+b);
      if(combined.size>256)throw Error('unprovable interpolated property domain');part=combined;
     }
     i=t[i].templateEnd;
    }
    if(t[i].kind==='punctuation'&&t[i].value==='('){const close=matching(t,i);if(close>=end)return null;part=constant(i+1,close);i=close;}
    if(!part)return null;
    const combined=new Set();for(const a of values)for(const b of part)combined.add(a+b);
    if(combined.size>256)throw Error('unprovable constant property domain');values=combined;
   }
   else if(t[i].value!=='+')return null;
   expect=!expect;
  }
  return !expect?values:null;
 };
 for(let pass=0;pass<t.length;pass++){
  let changed=false;
  for(let i=0;i<t.length-2;i++)if(t[i].kind==='identifier'&&t[i+1].value==='='&&!['.','?.'].includes(t[i-1]?.value)){
   let end=i+2;while(end<t.length&&![';',',',')','}'].includes(t[end].value)){if(t[end].kind==='punctuation'&&['(','[','{'].includes(t[end].value))end=matching(t,end);end++;}
   if(t.slice(i+2,end).some(token=>token.kind==='identifier'&&token.value===t[i].value))continue;
   const value=constant(i+2,end);if(value!==null){const previous=constants.get(t[i].value)||new Set();for(const item of value)if(!previous.has(item)){previous.add(item);changed=true;}if(previous.size>256)throw Error('unprovable reassigned property domain');constants.set(t[i].value,previous);}
  }
  if(!changed)break;
 }
 for(let i=0;i<t.length;i++){
  let method=null,form;
  if(native.has(t[i].value)&&t[i].kind==='identifier'){method=t[i].value;form='member-or-alias';}
  if(t[i].kind==='punctuation'&&t[i].value==='['&&t[i-1]&&['identifier','punctuation'].includes(t[i-1].kind)){
   const end=matching(t,i),value=constant(i+1,end);
   if(value&&[...value].some(v=>native.has(v))){method=[...value].find(v=>native.has(v));form='computed-member';}
  }
  // Any acquisition of Reflect.get outside the canonical helper is outside
  // this generation's closed canvas access grammar. Aliasing the acquired
  // function cannot turn that acquisition into an approved native text call.
  if(t[i].value==='Reflect'&&((t[i+1]?.value==='.'&&t[i+2]?.value==='get')||(t[i+1]?.value==='['&&constant(i+2,matching(t,i+1))?.has('get')))){method='reflective-access';form='reflection';}
  if(method)out.push({method,form,offset:t[i].offset,end:t[i].end,line:source.slice(0,t[i].charOffset).split('\n').length});
 }
 return out;
}

function closedSurface(source){
 const t=lex(source),errors=[],aliases=new Set(['CanvasText']);
 const forbidden=new Set(['getContext','CanvasRenderingContext2D','OffscreenCanvasRenderingContext2D','OffscreenCanvas','Function','eval']);
 const methods=new Set(['begin','frame','text','site','plotWidth']);
 const oracle=new Set(['__learnCanvasNative','learnCaptureRaster','__learnCanvasRasterEvidence']);
 for(let pass=0;pass<t.length;pass++){
  let changed=false;
  for(let i=0;i<t.length-2;i++)if(t[i].kind==='identifier'&&t[i+1].value==='='&&t[i+2].kind==='identifier'&&aliases.has(t[i+2].value)&&[';',',',')','}'].includes(t[i+3]?.value)&&!aliases.has(t[i].value)){aliases.add(t[i].value);changed=true;}
  if(!changed)break;
 }
 for(let i=0;i<t.length;i++){
  const token=t[i];
  const property=token.kind==='string'&&t[i-1]?.value==='['&&t[i+1]?.value===']';
  if((token.kind==='identifier'||property)&&oracle.has(token.value))errors.push({assertion:'diagnostic canvas oracle API in product source',offset:token.offset,name:token.value});
  if((token.kind==='identifier'||property)&&forbidden.has(token.value))errors.push({assertion:'uncontracted canvas context or executable-code acquisition',offset:token.offset,name:token.value});
  if(token.kind==='identifier'&&aliases.has(token.value)){
   if(t[i+1]?.value==='[')errors.push({assertion:'noncanonical canvas API access',offset:token.offset});
   if(['.','?.'].includes(t[i+1]?.value)&&!methods.has(t[i+2]?.value))errors.push({assertion:'diagnostic or unknown canvas API in product source',offset:token.offset,name:t[i+2]?.value});
  }
  if(token.kind==='identifier'&&['setTimeout','setInterval'].includes(token.value)&&t[i+1]?.value==='('&&['string','template-start'].includes(t[i+2]?.kind))errors.push({assertion:'uncontracted scheduled executable source',offset:token.offset});
 }
 return errors;
}


// The published generation has no character references in executable attributes.
// Recognize ASCII grammar references; reject every other reference in a potential
// executable owner. This is a closed grammar, not a general HTML entity decoder.
const EXECUTABLE_ENTITIES={"AMP;":"&","amp;":"&","apos;":"'","ast;":"*","bsol;":"\\","colon;":":","comma;":",","commat;":"@","DiacriticalGrave;":"`","dollar;":"$","equals;":"=","excl;":"!","fjlig;":"fj","grave;":"`","GT;":">","gt;":">","Hat;":"^","lbrace;":"{","lbrack;":"[","lcub;":"{","lowbar;":"_","lpar;":"(","lsqb;":"[","LT;":"<","lt;":"<","midast;":"*","NewLine;":"\n","num;":"#","percnt;":"%","period;":".","plus;":"+","quest;":"?","QUOT;":"\"","quot;":"\"","rbrace;":"}","rbrack;":"]","rcub;":"}","rpar;":")","rsqb;":"]","semi;":";","sol;":"/","Tab;":"\t","UnderBar;":"_","verbar;":"|","vert;":"|","VerticalLine;":"|"};
const SCRIPT_TYPES=new Set(['application/ecmascript','application/javascript','application/x-ecmascript','application/x-javascript','text/ecmascript','text/javascript','text/javascript1.0','text/javascript1.1','text/javascript1.2','text/javascript1.3','text/javascript1.4','text/javascript1.5','text/jscript','text/livescript','text/x-ecmascript','text/x-javascript']);
function executableAttribute(value){
 return value.replace(/&(?:#[xX][0-9a-fA-F]+;?|#[0-9]+;?|[a-zA-Z][a-zA-Z0-9]*;?)/g,reference=>{
  if(reference[1]==='#'){
   const digits=reference.slice(2).replace(/;$/,''),number=/^[xX]/.test(digits)?parseInt(digits.slice(1),16):Number(digits);
   if(number===0||number>0x10ffff||number>=0xd800&&number<=0xdfff||number>=0x80&&number<=0x9f)throw Error('unsupported numeric reference '+reference);
   return String.fromCodePoint(number);
  }
  const decoded=EXECUTABLE_ENTITIES[reference.slice(1)];if(decoded===undefined)throw Error('unsupported named reference '+reference);return decoded;
 });
}
function attributeSourceErrors(part){
 const errors=[...closedSurface(part.source),...accesses(part.source).map(a=>({...a,assertion:'uncontracted native canvas text source'}))];
 if(lex(part.source).some(t=>t.kind==='identifier'&&t.value==='CanvasText'))errors.push({assertion:'canvas descriptor requires an owned script implementation'});
 return errors.map(error=>({...error,ownerKind:part.kind,tag:part.tag,attribute:part.attribute,ownerOffset:part.offset}));
}
function htmlParts(source){
 const scripts=[],canvases=[],attributesCode=[],boundaryErrors=[];let i=0,ordinal=0;
 const entities=s=>s.replace(/&(?:quot|apos|amp|lt|gt|#(\d+)|#x([\da-f]+));/gi,(all,decimal,hex)=>decimal?String.fromCodePoint(+decimal):hex?String.fromCodePoint(parseInt(hex,16)):({'&quot;':'"','&apos;':"'",'&amp;':'&','&lt;':'<','&gt;':'>'}[all.toLowerCase()]));
 while(i<source.length){
  const start=source.indexOf('<',i);if(start<0)break;
  if(source.startsWith('<!--',start)){const end=source.indexOf('-->',start+4);if(end<0)throw Error('unclosed HTML comment');i=end+3;continue;}
  const name=/^<\/?([a-zA-Z][\w:-]*)\b/.exec(source.slice(start));if(!name){i=start+1;continue;}
  let end=start+name[0].length,quote=null;
  for(;end<source.length;end++){const c=source[end];if(quote){if(c===quote)quote=null;}else if(c==='"'||c==="'")quote=c;else if(c==='>')break;}
  if(end===source.length)throw Error('unclosed HTML tag');
  i=end+1;if(source[start+1]==='/')continue;
  const tag=name[1].toLowerCase(),attributes={};
  const raw=source.slice(start+name[0].length,end);
  for(const a of raw.matchAll(/([^\s=/>]+)(?:\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s>]+)))?/g)){
   const key=a[1].toLowerCase(),value=a[2]??a[3]??a[4]??'';
   if(Object.hasOwn(attributes,key)){boundaryErrors.push({assertion:'duplicate HTML attribute in canvas source boundary',tag,attribute:key});continue;}
   attributes[key]=entities(value);
   const event=key.startsWith('on'),url=['href','xlink:href','src','action','formaction'].includes(key);
   if(event||url){
    let decoded;try{decoded=executableAttribute(value);}catch(error){boundaryErrors.push({assertion:'unsupported executable HTML character reference',tag,attribute:key,message:error.message});continue;}
    const normalized=decoded.replace(/[\t\r\n]/g,'').replace(/^[\x00-\x20]+/,'');
    if(event||/^javascript:/i.test(normalized))attributesCode.push({kind:event?'event-handler':'javascript-url',tag,attribute:key,offset:Buffer.byteLength(source.slice(0,start+name[0].length+a.index)),source:event?decoded:normalized.slice(normalized.indexOf(':')+1)});
   }
  }
  if(['iframe','object','embed','xmp','plaintext','noembed','noframes'].includes(tag)||Object.hasOwn(attributes,'srcdoc'))boundaryErrors.push({assertion:'unsupported nested executable HTML owner',tag});
  if(tag==='canvas')canvases.push({id:attributes.id||null,attributes,offset:Buffer.byteLength(source.slice(0,start)),start,end:i});
  if(['script','style','textarea','title','noscript'].includes(tag)){
   const re=new RegExp('</'+tag+'\\s*>','ig');re.lastIndex=i;const close=re.exec(source);if(!close)throw Error('unclosed raw HTML element '+tag);
   if(tag==='script'){
    const type=(attributes.type||'').trim().toLowerCase(),language=(attributes.language||'').trim().toLowerCase();
    const executable=(!type&&!language)||(!type&&SCRIPT_TYPES.has('text/'+language))||SCRIPT_TYPES.has(type)||type==='module';
    if(Object.hasOwn(attributes,'src'))boundaryErrors.push({assertion:'external script in canvas source boundary'});
    if(!executable&&!['application/json','application/ld+json','importmap','speculationrules'].includes(type))boundaryErrors.push({assertion:'unsupported script classification in canvas source boundary',type,language});
    scripts.push({ordinal:ordinal++,attributes,start,contentStart:i,contentEnd:close.index,end:re.lastIndex,source:source.slice(i,close.index),executable});
   }
   i=re.lastIndex;
  }
 }
 return {scripts,canvases,attributesCode,boundaryErrors};
}
function matching(tokens,start,open=tokens[start].value,close=({'(':')','{':'}','[':']'})[open]){
 let depth=0;for(let i=start;i<tokens.length;i++){if(tokens[i].kind!=='punctuation')continue;if(tokens[i].value===open)depth++;if(tokens[i].value===close&&!--depth)return i;}
 throw Error('unbalanced executable source at '+tokens[start].offset);
}
function functions(source,t=lex(source)){
 const out=[];
 for(let i=0;i<t.length-3;i++)if(t[i].kind==='identifier'&&t[i].value==='function'&&t[i+1].kind==='identifier'&&t[i+2].value==='('){
  const params=matching(t,i+2);if(t[params+1]?.value!=='{')throw Error('function body missing');const end=matching(t,params+1);
  out.push({name:t[i+1].value,start:t[i].charOffset,bodyStart:t[params+1].charOffset,bodyEnd:t[end].charOffset,end:t[end].charEnd});
 }
 return out;
}
// This check closes direct reads of mutable bindings in named enclosing producers.
// It deliberately does not claim transitive data-flow or finite state closure.
function directCapturedState(source,callCharOffset,argumentTokens,t=lex(source)){
 const owners=functions(source,t).filter(f=>f.bodyStart<callCharOffset&&f.bodyEnd>callCharOffset).sort((a,b)=>(a.end-a.start)-(b.end-b.start));
 const bindings=new Map();
 for(const owner of owners){
  const start=t.findIndex(x=>x.charOffset===owner.bodyStart),end=matching(t,start),fn=t.findIndex(x=>x.charOffset===owner.start),parameters=fn+2;
  // Resolve the nearest named producer before its enclosing producers. A
  // parameter or constant shadows an outer mutable binding with the same name.
  for(let i=parameters+1;i<start-1;i++)if(t[i].kind==='identifier'&&[',','('].includes(t[i-1]?.value)&&[')',',','='].includes(t[i+1]?.value)&&!bindings.has(t[i].value))bindings.set(t[i].value,'parameter');
  for(let i=start+1;i<end;i++){
   if(t[i].kind==='template-start'){i=t[i].templateEnd;continue;}
   if(t[i].kind==='punctuation'&&['(','[','{'].includes(t[i].value)){i=matching(t,i);continue;}
   if(t[i].kind!=='identifier'||!['let','var','const'].includes(t[i].value))continue;
   const kind=t[i].value;let cursor=i+1;
   for(;;){
    if(t[cursor]?.kind!=='identifier')break;if(!bindings.has(t[cursor].value))bindings.set(t[cursor].value,kind);cursor++;
    for(;cursor<end&&![';',','].includes(t[cursor].value);cursor++){
     if(t[cursor].kind==='template-start'){cursor=t[cursor].templateEnd;continue;}
     if(t[cursor].kind==='punctuation'&&['(','[','{'].includes(t[cursor].value))cursor=matching(t,cursor);
    }
    if(t[cursor]?.value!==',')break;cursor++;
   }
   i=cursor;
  }
 }
 return [...new Set(argumentTokens.filter((x,i)=>x.kind==='identifier'&&['let','var'].includes(bindings.get(x.value))&&!['.','?.'].includes(argumentTokens[i-1]?.value)).map(x=>'state.'+x.value))].sort();
}
function validDescriptor(value){
 const fields=['id','role','minimumContrast','region','collision','formatter','family','mode','dependencies'];
 return !(!value||Object.keys(value).sort().join()!==fields.sort().join()||typeof value.id!=='string'||!/^[a-zA-Z0-9_.:-]+$/.test(value.id)||!['axis','annotation','value','status','date'].includes(value.role)||value.minimumContrast!==4.5||!['axis-right','axis-left','axis-bottom','title-top','annotation','date-left','date-bottom-left','date-bottom-right','label-left','value-right','status'].includes(value.region)||!['fixed','separate'].includes(value.collision)||['formatter','family','mode'].some(k=>typeof value[k]!=='string'||!value[k])||!Array.isArray(value.dependencies)||value.dependencies.some(x=>typeof x!=='string'||!x)||new Set(value.dependencies).size!==value.dependencies.length||['frame.width','frame.height','theme'].some(d=>!value.dependencies.includes(d)));
}
function descriptors(source){
 const t=lex(source),definitions=[],calls=[];
 for(let i=0;i<t.length-4;i++){
  if(t[i].kind!=='identifier'||t[i].value!=='CanvasText'||t[i+1].value!=='.')continue;
  if(t[i+2].value==='text'&&t[i+3].value==='(')calls.push({index:i,token:t[i],end:matching(t,i+3)});
  if(t[i+2].value!=='site'||t[i+3].value!=='(')continue;
  const begin=i+4;
  if(t[begin].value!=='{')throw Error('descriptor must be a source-co-located JSON literal');
  const end=matching(t,begin);if(t[end+1]?.value!==')')throw Error('descriptor has extra arguments');
  const value=JSON.parse(source.slice(t[begin].charOffset,t[end].charEnd));
  definitions.push({value,index:i,end:end+1,offset:t[i].offset,source:source.slice(t[begin].charOffset,t[end].charEnd)});
 }
 const errors=[],bound=[];
 for(const definition of definitions)if(!validDescriptor(definition.value))errors.push({assertion:'invalid canvas semantic descriptor',id:definition.value.id,offset:definition.offset});
 for(const call of calls){
  const owned=definitions.filter(d=>d.index===call.index+6&&t[call.index+4]?.kind==='identifier'&&t[call.index+5]?.value===','&&d.end<call.end&&t[d.end+1]?.value===',');
  if(owned.length!==1){errors.push({assertion:'canvas text call lacks exactly one co-located descriptor',offset:call.token.offset});continue;}
  const d=owned[0];let argEnd=d.end+2;const argStart=argEnd;for(;argEnd<call.end;argEnd++){if(t[argEnd].value===',')break;if(t[argEnd].kind==='template-start'){argEnd=t[argEnd].templateEnd;continue;}if(t[argEnd].kind==='punctuation'&&['(','[','{'].includes(t[argEnd].value))argEnd=matching(t,argEnd);}
  const formatter=source.slice(t[argStart].charOffset,t[argEnd].charOffset).trim();
  if(d.value.formatter!==formatter)errors.push({assertion:'canvas formatter identity differs from executable source',id:d.value.id});
  const requiredDirectState=directCapturedState(source,call.token.charOffset,t.slice(argStart,call.end),t);
  for(const dependency of requiredDirectState)if(!Array.isArray(d.value.dependencies)||!d.value.dependencies.includes(dependency))errors.push({assertion:'canvas captured state dependency missing',id:d.value.id,dependency});
  bound.push({...d,callOffset:call.token.offset,callCharOffset:call.token.charOffset,definitionStart:t[d.index+4].charOffset,definitionEnd:t[d.end-1].charEnd,requiredDirectState});
 }
 for(const d of definitions)if(!bound.includes(d)&&!bound.some(b=>b.index===d.index))errors.push({assertion:'orphan canvas descriptor',offset:d.offset,id:d.value.id});
 return {definitions,bound,errors};
}
// A shared site's witness belongs to its executable closure, not merely its
// spelling. Conservatively include referenced source bindings, even a binding
// whose name also occurs as a property. Extra dependencies may require an
// additional witness; omitted dependencies would permit unsound sharing.
function implementationClosures(source, declared=functions(source)){
 const t=lex(source),bindings=new Map(declared.map(f=>[f.name,{start:f.start,end:f.end}]));
 for(let i=0;i<t.length;i++){
  if(t[i].kind!=='identifier'||!['const','let','var'].includes(t[i].value)||declared.some(f=>f.start<t[i].charOffset&&f.end>t[i].charOffset))continue;
  const start=i,names=[];let end=i+1;
  for(;end<t.length&&t[end].value!==';';end++){
   if(t[end].kind==='identifier'&&(end===start+1||t[end-1].value===','))names.push(t[end].value);
   if(t[end].kind==='punctuation'&&['(','[','{'].includes(t[end].value))end=matching(t,end);
  }
  if(end>=t.length)throw Error('unterminated canvas source binding');
  for(const name of names)bindings.set(name,{start:t[start].charOffset,end:t[end].charEnd});i=end;
 }
 const results=new Map();
 for(const f of declared){
  const pending=[f.name],seen=new Set(),members=[];
  while(pending.length){
   const name=pending.pop();if(seen.has(name))continue;seen.add(name);
   const b=bindings.get(name);if(!b)throw Error('missing canvas implementation binding '+name);
   const body=source.slice(b.start,b.end);members.push({name,sha256:crypto.createHash('sha256').update(body).digest('hex')});
   for(const token of lex(body))if(token.kind==='identifier'&&bindings.has(token.value)&&!seen.has(token.value))pending.push(token.value);
  }
  members.sort((a,b)=>a.name.localeCompare(b.name));results.set(f.name,{members,sha256:crypto.createHash('sha256').update(JSON.stringify(members)).digest('hex')});
 }
 return results;
}
function inventory(root){
 const siteRoot=path.join(root,'site'),files=[];
 const walk=dir=>{for(const e of fs.readdirSync(dir,{withFileTypes:true}).sort((a,b)=>a.name.localeCompare(b.name))){const p=path.join(dir,e.name);if(e.isDirectory())walk(p);else if(e.name.endsWith('.html'))files.push(p)}};walk(siteRoot);
 const canonical=fs.existsSync(path.join(root,'scripts/canvas_contract.js'))?fs.readFileSync(path.join(root,'scripts/canvas_contract.js'),'utf8').trim():null;
 const pages=[],errors=[],definitions=new Map();let native=0,unbound=0,bound=0;
 for(const file of files){
  const raw=fs.readFileSync(file),source=raw.toString(),route='/'+path.relative(siteRoot,file).replace(/index\.html$/,''),html=htmlParts(source),occurrences=[],helper=[];
  errors.push(...html.boundaryErrors.map(error=>({route,...error})));
  for(const part of html.attributesCode){
   const found=accesses(part.source);native+=found.length;unbound+=found.length;
   errors.push(...attributeSourceErrors(part).map(error=>({route,...error})));
  }
  const local=new Set();
  for(const script of html.scripts.filter(s=>s.executable)){
   const accessesFound=accesses(script.source),isHelper=script.attributes['data-canvas-text']==='v1';
   if(isHelper){helper.push(script.ordinal);if(!canonical||script.source.trim()!==canonical)errors.push({route,assertion:'canvas helper differs from authoritative source'});continue;}
   errors.push(...closedSurface(script.source).map(error=>({route,script:script.ordinal,...error})));
   native+=accessesFound.length;unbound+=accessesFound.length;
   for(const a of accessesFound)errors.push({route,script:script.ordinal,...a,assertion:'uncontracted native canvas text source'});
   const d=descriptors(script.source),owners=d.bound.length?functions(script.source):[],closures=d.bound.length?implementationClosures(script.source,owners):new Map();errors.push(...d.errors.map(e=>({route,script:script.ordinal,...e})));
   for(const occurrence of d.bound){
    bound++;const value=occurrence.value,key=JSON.stringify(value),prior=definitions.get(value.id);


    if(prior&&prior!==key)errors.push({route,id:value.id,assertion:'conflicting canvas descriptor'});definitions.set(value.id,key);
    if(local.has(value.id))errors.push({route,id:value.id,assertion:'duplicate canvas site occurrence'});local.add(value.id);
    const owner=owners.filter(f=>f.bodyStart<occurrence.callCharOffset&&f.bodyEnd>occurrence.callCharOffset).sort((a,b)=>(a.end-a.start)-(b.end-b.start))[0];
    if(!owner)errors.push({route,id:value.id,assertion:'canvas semantic implementation owner missing'});
    const implementationHash=owner?crypto.createHash('sha256').update(script.source.slice(owner.start,owner.end)).digest('hex'):null;
    occurrences.push({route,script:script.ordinal,offset:occurrence.callOffset,siteID:value.id,descriptor:value,implementationOwner:owner?.name||null,implementationHash,closure:owner?closures.get(owner.name):null});
   }
  }
  if(html.canvases.length&&helper.length===1&&helper[0]!==html.scripts.find(s=>s.executable)?.ordinal)errors.push({route,assertion:'canvas helper must execute before authored scripts'});
  if(html.canvases.length&&helper.length!==1)errors.push({route,assertion:'canvas document needs exactly one canonical helper',helpers:helper.length});
  if(!html.canvases.length&&helper.length)errors.push({route,assertion:'orphan canvas helper'});
  if(new Set(html.canvases.map(c=>c.id)).size!==html.canvases.length||html.canvases.some(c=>!c.id))errors.push({route,assertion:'canvas identities must be nonempty and unique'});
  pages.push({route,file,sha256:crypto.createHash('sha256').update(raw).digest('hex'),canvases:html.canvases.map(({id,offset})=>({id,offset})),helpers:helper,occurrences});
 }
 if(pages.length!==369)errors.push({assertion:'canvas published route inventory differs',observed:pages.length});
 if(pages.filter(p=>p.canvases.length).length!==66||pages.reduce((n,p)=>n+p.canvases.length,0)!==71)errors.push({assertion:'canvas element continuity differs'});
 if(bound!==269)errors.push({assertion:'canvas semantic site continuity differs',observed:bound});
 return {htmlRoutes:pages.length,canvasRoutes:pages.filter(p=>p.canvases.length).length,canvases:pages.reduce((n,p)=>n+p.canvases.length,0),nativeProductOccurrences:native,contractOccurrences:bound,unbound,errors,pages};
}
module.exports={validDescriptor,executableAttribute,attributeSourceErrors,SCRIPT_TYPES,lex,accesses,closedSurface,htmlParts,matching,functions,descriptors,implementationClosures,inventory};
if(require.main===module){const result=inventory(process.argv[2]||process.cwd());if(process.argv[3])fs.writeFileSync(process.argv[3],JSON.stringify(result,null,2));console.log(JSON.stringify({...result,pages:undefined,errors:result.errors.slice(0,5)}));process.exitCode=result.errors.length?1:0;}
