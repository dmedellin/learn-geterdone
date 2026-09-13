'use strict';
function canvasControls(source=null){
 const fail=assertion=>{throw Object.assign(Error(assertion),{assertion,code:'LEARN_CANVAS_SEMANTIC'})};
 if(source&&(!Array.isArray(source.unresolved)||source.unresolved.length))fail('unresolved source numeric boundary');
 if(source&&(!Array.isArray(source.bindings)||!Array.isArray(source.comparisons)||!/^[0-9a-f]{64}$/.test(source.sha256)))fail('missing numeric source identity');
 const roots=[...new Set([...document.querySelectorAll('canvas')].map(c=>c.closest('.lab')||c.closest('section')).filter(Boolean))];
 const nodes=[...new Set(roots.flatMap(r=>[...r.querySelectorAll('input,select,button')]))];
 const controls=[],targets=[];
 const add=(e,control)=>{control.key=e.id||'canvas-control-'+controls.length;targets.push(e);controls.push(control)};
 const seen=new Set();
 for(const e of nodes){
  if(e.tagName==='BUTTON'){
   if(!e.hasAttribute('data-value')&&!e.hasAttribute('data-v')){add(e,{kind:'action',values:['invoke'],default:'idle',label:e.textContent.trim()});continue;}
   if(seen.has(e.parentElement))continue;seen.add(e.parentElement);
   const buttons=[...e.parentElement.children].filter(b=>b.tagName==='BUTTON');
   const attribute=e.hasAttribute('data-value')?'data-value':'data-v';
   if(buttons.some(b=>!b.hasAttribute(attribute)))throw Error('unclassified categorical canvas button');
   const values=buttons.map(b=>b.getAttribute(attribute));if(new Set(values).size!==values.length)throw Error('duplicate canvas control option');
   add(e.parentElement,{kind:'segmented',attribute,values,default:buttons.find(b=>b.classList.contains('active'))?.getAttribute(attribute),labels:buttons.map(b=>b.textContent.trim())});
  }else if(e.tagName==='SELECT')add(e,{kind:'select',values:[...e.options].map(o=>o.value),default:e.value,labels:[...e.options].map(o=>o.textContent.trim())});
  else if(e.type==='checkbox')add(e,{kind:'checkbox',values:[false,true],default:e.checked});
  else if(['range','number'].includes(e.type)){
   const min=Number(e.min),max=Number(e.max),step=e.step?Number(e.step):1,initial=Number(e.value);
   if(!e.min||!e.max){add(e,{kind:'unbounded-number',default:e.value,values:['',e.value,'-1e100','1e100','W'.repeat(512),'交易 Δ🙂'],needsSourceNoninterference:true});continue;}
   if(![min,max,step,initial].every(Number.isFinite)||step<=0||min>initial||initial>max)throw Error('invalid numeric canvas control '+e.id);
   const values=new Set([min,max,initial]);
   const neighbor=v=>{for(const k of [-1,0,1,2]){const q=min+Math.floor((v-min)/step)*step+k*step;if(q>=min&&q<=max)values.add(Number(q.toPrecision(13)))}};
   neighbor(0);for(let power=-8;power<=16;power++){neighbor(10**power);neighbor(-(10**power));}
   const boundaries=source?source.comparisons.filter(c=>c.id===e.id):[];
   if(source&&source.bindings.filter(b=>b.id===e.id).length!==1)fail('numeric control lacks exactly one source boundary binding');
   for(const boundary of boundaries){if(!Number.isFinite(boundary.threshold)||!Number.isInteger(boundary.offset))fail('invalid numeric source boundary');neighbor(boundary.threshold);}
   add(e,{kind:'numeric',min,max,step,default:initial,values:[...values].sort((a,b)=>a-b),sourceBoundaries:boundaries,reason:'DOM min/max/default, zero/sign and decimal magnitude neighbors'+(source?', source scalar comparison neighbors':' (source comparison proof absent)')+'; formatter, joint dependency and action classes require separate reconciliation'});
  }else if(['text','search','email','url'].includes(e.type))add(e,{kind:'text',default:e.value,values:['','W'.repeat(512),'交易 Δ🙂 café'.repeat(32)]});
  else throw Error('unclassified canvas control '+e.tagName+' '+e.type);
 }
 if(source&&source.bindings.some(b=>controls.filter(c=>c.kind==='numeric'&&c.key===b.id).length!==1))fail('orphan numeric source binding');
 Object.defineProperty(window,'__canvasControlTargets',{value:targets,configurable:true});
 return {controls,sourceScalarBoundaries:source?.sha256||null,finiteProofComplete:false,mode:window.LESSON?.lab||document.body.dataset.pageKind,slides:[...document.querySelectorAll('.slide')].map((e,i)=>({index:i,id:e.id,name:e.getAttribute('aria-labelledby')})),roots:roots.map(r=>({tag:r.tagName,id:r.id,class:r.className}))};
}
function applyCanvasControl(index,value){
 const e=window.__canvasControlTargets[index];if(!e||!e.isConnected)throw Error('canvas control identity detached');
 if(e.tagName==='BUTTON'){if(value!=='idle')e.click();}
 else if(e.tagName==='SELECT'){if(![...e.options].some(o=>o.value===String(value)))throw Error('unknown canvas select option');e.value=String(value);e.dispatchEvent(new Event('change',{bubbles:true}));}
 else if(e.tagName==='INPUT'){if(e.type==='checkbox'){e.checked=!!value;e.dispatchEvent(new Event('change',{bubbles:true}));}else{e.value=String(value);e.dispatchEvent(new Event('input',{bubbles:true}));e.dispatchEvent(new Event('change',{bubbles:true}));}}
 else{const b=[...e.children].find(b=>(b.dataset.value??b.dataset.v)===String(value));if(!b)throw Error('unknown canvas segmented option');b.click();}
}
function refreshCanvasControls(expected,source=null){
 const fail=assertion=>{throw Object.assign(Error(assertion),{assertion,code:'LEARN_CANVAS_SEMANTIC'})};
 if(!expected||!Array.isArray(expected.controls)||expected.sourceScalarBoundaries&&(source?.sha256!==expected.sourceScalarBoundaries))fail('missing canvas control source identity');
 const previous=window.__canvasControlTargets||[],current=canvasControls(source);
 const identity=control=>({key:control.key,kind:control.kind,attribute:control.attribute||null,values:['select','segmented','checkbox'].includes(control.kind)?control.values:null,min:control.min??null,max:control.max??null,step:control.step??null});
 if(JSON.stringify(expected.controls.map(identity))!==JSON.stringify(current.controls.map(identity)))fail('canvas control domain changed without witness');
 return {controls:current.controls,targets:window.__canvasControlTargets.map((e,index)=>({key:current.controls[index].key,replaced:e!==previous[index],disabled:!!e.disabled,value:e.tagName==='INPUT'&&e.type==='checkbox'?e.checked:e.value??null,label:e.tagName==='BUTTON'?e.textContent.trim():null}))};
}
module.exports={canvasControls,applyCanvasControl,refreshCanvasControls};
