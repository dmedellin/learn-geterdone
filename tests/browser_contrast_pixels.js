/* Refine conservative paint bounds using the actual browser raster. This also
 * accounts for SVG sibling shapes behind text. Only test-time ink is hidden;
 * layout, component backgrounds and all product bytes remain unchanged. */
'use strict';
const assert=require('node:assert/strict');
const {contrastRatio}=require('./browser_contracts');
async function refine(c,result){
 const failed=new Set(result.failures.filter(f=>f.reason==='text contrast below threshold').map(f=>f.nodeIndex));
 const candidates=result.rows.filter(r=>r.inks&&(r.requiresRaster||failed.has(r.nodeIndex)));
 const groups=new Map();for(const row of candidates){const key=row.rasterGroup||'node:'+row.nodeIndex;if(!groups.has(key))groups.set(key,[]);groups.get(key).push(row);}
 if(!candidates.length)return result;
 const saved=await c.evaluate(`(()=>{
  const elements=[...new Set(window.learnContrastNodes.map(n=>n.parentElement).filter(Boolean))];
  window.learnContrastScroll=[...document.querySelectorAll('*')].filter(e=>e.scrollTop||e.scrollLeft).map(e=>[e,e.scrollTop,e.scrollLeft]);
  window.learnContrastRestore=elements.map(e=>[e,e.getAttribute('style')]);
  for(const e of elements){const s=getComputedStyle(e);if(s.backgroundClip==='text')e.style.setProperty('background-image','none','important');
   e.style.setProperty('-webkit-text-fill-color','transparent','important');
   if(e instanceof SVGElement&&(e.tagName==='text'||e.closest('text')))e.style.setProperty('fill','transparent','important');}
  return elements.length;
 })()`);assert(saved>0,'nonempty raster measurement nodes');
 try{
  for(const group of groups.values()){
   const geometry=await c.evaluate(`(()=>{
    const indices=${JSON.stringify(group.map(r=>r.nodeIndex))};
    const first=window.learnContrastNodes[indices[0]].parentElement;
    (first.ownerSVGElement||first).scrollIntoView({block:'center',inline:'center',behavior:'instant'});
    const nodes=indices.map(nodeIndex=>{
     const node=window.learnContrastNodes[nodeIndex],range=document.createRange();range.selectNode(node);
     const rects=[...range.getClientRects()].map(r=>({left:Math.max(0,r.left),right:Math.min(innerWidth,r.right),top:Math.max(0,r.top),bottom:Math.min(innerHeight,r.bottom)})).filter(r=>r.right>r.left&&r.bottom>r.top);
     const points=rects.flatMap(r=>[.15,.5,.85].flatMap(x=>[.25,.5,.75].map(y=>({x:Math.floor(r.left+(r.right-r.left)*x),y:Math.floor(r.top+(r.bottom-r.top)*y)}))));
     return {nodeIndex,points};
    });return {nodes,width:innerWidth,height:innerHeight};
   })()`);
   for(const item of geometry.nodes)assert(item.points.length,'no rendered background samples for node '+item.nodeIndex);
   const shot=await c.send('Page.captureScreenshot',{format:'png',captureBeyondViewport:false});
   const measured=await c.evaluate(`(async()=>{
    const img=new Image();img.src=${JSON.stringify('data:image/png;base64,'+shot.data)};await img.decode();
    const canvas=document.createElement('canvas');canvas.width=img.width;canvas.height=img.height;
    const ctx=canvas.getContext('2d',{willReadFrequently:true});ctx.drawImage(img,0,0);
    return ${JSON.stringify(geometry.nodes)}.map(item=>({...item,colors:item.points.map(p=>[...ctx.getImageData(Math.floor(p.x*img.width/${geometry.width}),Math.floor(p.y*img.height/${geometry.height}),1,1).data].slice(0,3))}));
   })()`);
   for(const item of measured){
    const row=group.find(r=>r.nodeIndex===item.nodeIndex);
    const opacities=await c.evaluate(`window.learnContrastOpacityGroups[${item.nodeIndex}].map(x=>x[1])`),outside=[];
    for(let i=0;i<opacities.length;i++){
     await c.evaluate(`(()=>{const e=window.learnContrastOpacityGroups[${item.nodeIndex}][${i}][0];window.learnOpacityRestore=[e,e.getAttribute('style')];e.style.setProperty('visibility','hidden','important')})()`);
     try{
      const background=await c.send('Page.captureScreenshot',{format:'png',captureBeyondViewport:false});
      outside.push(await c.evaluate(`(async()=>{const img=new Image();img.src=${JSON.stringify('data:image/png;base64,'+background.data)};await img.decode();const canvas=document.createElement('canvas');canvas.width=img.width;canvas.height=img.height;const ctx=canvas.getContext('2d',{willReadFrequently:true});ctx.drawImage(img,0,0);return ${JSON.stringify(item.points)}.map(p=>[...ctx.getImageData(Math.floor(p.x*img.width/${geometry.width}),Math.floor(p.y*img.height/${geometry.height}),1,1).data].slice(0,3))})()`));
     }finally{await c.evaluate("(()=>{const [e,s]=window.learnOpacityRestore;s===null?e.removeAttribute('style'):e.setAttribute('style',s);delete window.learnOpacityRestore})()");}
    }
    const samples=item.colors.flatMap((background,pixel)=>row.inks.map(ink=>{
     // Group opacity blends the completed group with its exterior backdrop.
     // Undo outer groups to recover each local backdrop, then composite the
     // opaque ink from inside out. Text alpha blends that result with the
     // actual background raster, which includes the group's own background.
     const localOutside=[];
     for(let i=0;i<outside.length;i++){
      let local=outside[i][pixel];
      for(let j=0;j<i;j++)local=local.map((x,k)=>(x-localOutside[j][k]*(1-opacities[j]))/opacities[j]);
      localOutside.push(local);
     }
     let opaque=ink.slice(0,3);
     for(let i=opacities.length-1;i>=0;i--)opaque=opaque.map((x,k)=>x*opacities[i]+localOutside[i][k]*(1-opacities[i]));
     if(row.halo){background=row.halo.slice(0,3);for(let i=opacities.length-1;i>=0;i--)background=background.map((x,k)=>x*opacities[i]+localOutside[i][k]*(1-opacities[i]));}
     const foreground=opaque.map((x,i)=>Math.max(0,Math.min(255,x*ink[3]+background[i]*(1-ink[3]))));
     return {ratio:contrastRatio(foreground,background),foreground,background};
    }));
    const worst=samples.reduce((a,b)=>a.ratio<b.ratio?a:b);
    Object.assign(row,{conservativeRatio:row.ratio,...worst,measurement:'rendered background raster',sampleCount:samples.length,samplePoints:item.points});
   }
  }
  result.failures=result.failures.filter(f=>f.reason!=='text contrast below threshold').concat(result.rows.filter(r=>r.ratio+1e-6<r.threshold).map(r=>({reason:'text contrast below threshold',...r})));
 }finally{
  await c.evaluate("window.learnContrastRestore.forEach(([e,style])=>style===null?e.removeAttribute('style'):e.setAttribute('style',style));document.querySelectorAll('*').forEach(e=>{if(e.scrollTop||e.scrollLeft){e.scrollTop=0;e.scrollLeft=0}});window.learnContrastScroll.forEach(([e,top,left])=>{e.scrollTop=top;e.scrollLeft=left});delete window.learnContrastScroll;delete window.learnContrastRestore");
 }
 return result;
}
module.exports={refine};
