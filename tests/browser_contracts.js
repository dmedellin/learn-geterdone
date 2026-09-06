/* Browser assertions use rendered geometry, native label associations and live
 * text bounds. No CSS-token assertions or URL-specific acceptance exceptions. */
'use strict';

function visible(e) {
  if (!e || !e.checkVisibility({checkOpacity:true, checkVisibilityCSS:true})) return false;
  const s=getComputedStyle(e), b=e.getBoundingClientRect();
  return b.width>0 && b.height>0 && !e.closest('[hidden],.skip-link') &&
    (!s.clip || s.clip==='auto') && !/inset\(50%\)/.test(s.clipPath);
}
function targets() {
  const rows=[], failures=[], exclusions=[];
  for (const item of learnInteractiveTargets.inventory()) {
    const owners=item.owners.filter(visible);
    if (!owners.length) {exclusions.push({id:item.control.id,kind:item.kind,reason:'no visible target owner'});continue;}
    const sized=owners.filter(e=>{const b=e.getBoundingClientRect();return b.width>=44&&b.height>=44;});
    const owner=sized[0]||owners[0];
    owner.scrollIntoView({block:'center',inline:'center',behavior:'instant'});
    const b=owner.getBoundingClientRect(), hit=document.elementFromPoint(b.x+b.width/2,b.y+b.height/2);
    const row={kind:item.kind,id:item.control.id,tag:item.control.tagName,owner:owner.tagName,
      class:owner.getAttribute('class'),text:(owner.innerText||owner.textContent||'').trim().slice(0,90),
      width:b.width,height:b.height,disabled:item.disabled,
      small:b.width<44||b.height<44,reachable:owners.some(e=>e===hit||e.contains(hit))};
    rows.push(row);
    if(!item.disabled && ((matchMedia('(pointer:coarse)').matches&&row.small)||!row.reachable)) failures.push(row);
  }
  window.scrollTo({top:0,left:0,behavior:'instant'});
  for(const e of document.querySelectorAll('.slide,.table-wrap,.lab-stage')) {e.scrollTop=0;e.scrollLeft=0;}
  if(!rows.length) failures.push({reason:'no visible target owners'});
  if(innerWidth<=390&&!matchMedia('(pointer:coarse)').matches) failures.push({reason:'phone pointer emulation is not coarse'});
  return {rows,exclusions,failures};
}
function svgGeometry(scope=document) {
  const rows=[],failures=[],capabilities=[],svgs=[...scope.querySelectorAll('svg')];
  for(const svg of scope.querySelectorAll('svg')) {
    if(!visible(svg))continue; // inactive slides are not visible capabilities
    const labels=[...svg.querySelectorAll('text')].filter(e=>e.textContent.trim());
    if(!labels.length)continue; // a genuinely text-free illustration
    const readable=labels.filter(visible);
    capabilities.push({svg:svg.id,svgIndex:svgs.indexOf(svg),semantic:labels.length,readable:readable.length});
    if(!readable.length)failures.push({reason:'no readable semantic SVG labels',svg:svg.id,semantic:labels.length});
  }
  for(const e of scope.querySelectorAll('svg text')) {
    if(!visible(e)||!e.textContent.trim()) continue;
    const b=e.getBoundingClientRect(), clips=[e.ownerSVGElement.getBoundingClientRect()];
    for(let p=e.parentElement;p&&p!==document.body;p=p.parentElement) {
      const s=getComputedStyle(p),pb=p.getBoundingClientRect();
      const ref=(p.getAttribute('clip-path')||s.clipPath||'').match(/#([^\)"']+)/);
      if(ref&&p.ownerSVGElement) {
        const c=p.ownerSVGElement.querySelector('[id="'+ref[1]+'"] rect');
        if(c){const m=p.getScreenCTM(),a=new DOMPoint(+c.getAttribute('x'),+c.getAttribute('y')).matrixTransform(m),
          z=new DOMPoint(+c.getAttribute('x')+ +c.getAttribute('width'),+c.getAttribute('y')+ +c.getAttribute('height')).matrixTransform(m);
          clips.push({left:a.x,top:a.y,right:z.x,bottom:z.y});}
      }
      if(['hidden','clip'].includes(s.overflowX)||['hidden','clip'].includes(s.overflowY))
        clips.push({left:['hidden','clip'].includes(s.overflowX)?pb.left:-Infinity,
          right:['hidden','clip'].includes(s.overflowX)?pb.right:Infinity,
          top:['hidden','clip'].includes(s.overflowY)?pb.top:-Infinity,
          bottom:['hidden','clip'].includes(s.overflowY)?pb.bottom:Infinity});
    }
    const row={text:e.textContent,svg:e.ownerSVGElement.id,svgIndex:svgs.indexOf(e.ownerSVGElement),rect:b.toJSON(),clipped:false,offscale:false,entity:/&(?:#\d+|#x[\da-f]+|[a-z]+);/i.test(e.textContent)};
    const c={left:Math.max(...clips.map(c=>c.left)),top:Math.max(...clips.map(c=>c.top)),
      right:Math.min(...clips.map(c=>c.right)),bottom:Math.min(...clips.map(c=>c.bottom))};
    row.offscale=b.right<=c.left||b.left>=c.right||b.bottom<=c.top||b.top>=c.bottom;
    row.clipped=!row.offscale&&(b.left<c.left-.1||b.right>c.right+.1||b.top<c.top-.1||b.bottom>c.bottom+.1);
    // Offscale labels should be intentionally absent, not clipped DOM text.
    if(row.clipped||row.offscale||row.entity) failures.push(row);
    rows.push(row);
  }
  for(const item of capabilities) {
    const measured=rows.filter(r=>r.svgIndex===item.svgIndex&&!r.clipped&&!r.offscale);
    if(item.readable&&!measured.length)failures.push({reason:'no readable semantic SVG labels',...item});
  }
  return {rows,capabilities,failures};
}
function capstone() {
  const failures=[],slides=[...document.querySelectorAll('.slide')],isDeck=slides.length>0;
  const print=matchMedia('print').matches;
  if(print&&isDeck) {
    for(const [i,s] of slides.entries()) {const c=getComputedStyle(s),b=s.getBoundingClientRect();
      if(c.display==='none'||c.position!=='relative'||c.breakAfter!=='page'||c.overflow!=='hidden'||Math.abs(b.height-720)>.1||Math.abs(b.width-1279.96875)>.1)
        failures.push({reason:'one fixed page per printed slide',i,display:c.display,position:c.position,breakAfter:c.breakAfter,overflow:c.overflow,height:b.height});}
    for(const [i,s] of slides.entries()) {
      const b=s.getBoundingClientRect();
      for(const e of s.querySelectorAll('canvas,p,li,h1,h2,h3,.kpi,.slide-foot,.slide-stamp')) {
        if(!visible(e))continue;const r=e.getBoundingClientRect();
        if(r.left<b.left-.1||r.right>b.right+.1||r.top<b.top-.1||r.bottom>b.bottom+.1)
          failures.push({reason:'printed slide content clipped',slide:i+1,tag:e.tagName,text:e.textContent.slice(0,90),bottom:r.bottom-b.top});
      }
    }
    if(visible(document.querySelector('[data-ui="masthead"]'))) failures.push({reason:'print masthead takes slide space'});
    if(slides.length!==16)failures.push({reason:'preserved sixteen authored slides',count:slides.length});
    for(const e of document.querySelectorAll('.nav,.progress'))if(visible(e))failures.push({reason:'printed deck navigation'});
  } else {
    for(const selector of ['main','h1','[data-ui="masthead"]','[data-ui="breadcrumbs"]','[data-ui="page-kind"]'])
      if(document.querySelectorAll(selector).length!==1) failures.push({reason:'shared anatomy',selector,count:document.querySelectorAll(selector).length});
    const mast=document.querySelector('[data-ui="masthead"]'), brand=mast?.querySelector('a.brand');
    if(!visible(brand)||brand.pathname!=='/'||!brand.innerText.includes('Learn')) failures.push({reason:'Learn masthead identity'});
    const crumbs=document.querySelector('[data-ui="breadcrumbs"]');
    if(!visible(crumbs)||!crumbs.textContent.includes('Learn library')||!crumbs.textContent.includes('Trading')) failures.push({reason:'library and Subject hierarchy'});
    if(document.body.dataset.pageKind!==(isDeck?'slides':'supplemental')) failures.push({reason:'page type',actual:document.body.dataset.pageKind});
    for(const e of [document.documentElement,document.body]) if(['hidden','clip'].includes(getComputedStyle(e).overflowX)||['hidden','clip'].includes(getComputedStyle(e).overflowY)) failures.push({reason:'root masking',tag:e.tagName});
    if(document.documentElement.scrollWidth>innerWidth) failures.push({reason:'root overflow',width:document.documentElement.scrollWidth});
    if(!isDeck)for(const e of document.querySelectorAll('.hero .kpi strong')) {
      if(!/^\$[\d.]+$/.test(e.textContent.trim()))continue;
      const range=document.createRange();range.selectNodeContents(e);
      if(range.getClientRects().length!==1)failures.push({reason:'supplemental price wraps mid-number',text:e.textContent});
    }
  }
  if(isDeck&&slides.length!==16)failures.push({reason:'preserved sixteen authored slides',count:slides.length});
  if(!isDeck&&!document.querySelector('[data-ui="primary-actions"] a[href="slides/"]'))failures.push({reason:'supplemental lab opens its slide deck'});
  return {slides:slides.length,print,failures};
}
function rootLayout() {
  const failures=[],rows=[];
  for(const e of [document.documentElement,document.body]) {
    const c=getComputedStyle(e);
    if(['hidden','clip'].includes(c.overflowX)||['hidden','clip'].includes(c.overflowY))failures.push({reason:'root masking',tag:e.tagName});
    if(e.scrollWidth>document.documentElement.clientWidth)failures.push({reason:'root overflow',tag:e.tagName,width:e.scrollWidth});
  }
  for(const e of document.querySelectorAll('main,article,section,[role="main"],[data-ui],.content,.main-content')) {
    if(!visible(e))continue;
    const s=getComputedStyle(e),row={tag:e.tagName,id:e.id,class:e.className,width:e.clientWidth,scrollWidth:e.scrollWidth,height:e.clientHeight,scrollHeight:e.scrollHeight};
    rows.push(row);
    const clipX=['hidden','clip'].includes(s.overflowX),clipY=['hidden','clip'].includes(s.overflowY);
    if((clipX&&e.scrollWidth>e.clientWidth+1)||(clipY&&e.scrollHeight>e.clientHeight+1)) {
      const b=e.getBoundingClientRect(),walker=document.createTreeWalker(e,NodeFilter.SHOW_TEXT),bounds=[];
      while(walker.nextNode()){
        const node=walker.currentNode;if(!node.textContent.trim()||!visible(node.parentElement)||node.parentElement.closest('script,style'))continue;
        const range=document.createRange();range.selectNode(node);bounds.push(...range.getClientRects());
      }
      for(const item of e.querySelectorAll('canvas,svg,input,select,textarea,button'))if(visible(item))bounds.push(item.getBoundingClientRect());
      // Pseudo-element glows may intentionally extend beyond their card.
      // Only clipped content, not decorative paint, makes an owner fail.
      if(bounds.some(r=>(clipX&&(r.left<b.left-1||r.right>b.right+1))||(clipY&&(r.top<b.top-1||r.bottom>b.bottom+1))))
        failures.push({reason:'clipped content owner',...row});
    }
  }
  // Horizontal overflow must remain reachable and named; hiding it at the
  // document root cannot turn a broken content owner into a valid layout.
  for(const e of document.querySelectorAll('main *')) {
    if(!visible(e)||e.scrollWidth<=e.clientWidth+1)continue;
    const s=getComputedStyle(e);
    if(!['auto','scroll'].includes(s.overflowX))continue;
    const named=e.getAttribute('aria-label')||e.getAttribute('aria-labelledby')?.split(/\s+/).map(id=>document.getElementById(id)?.textContent||'').join('').trim();
    if(e.tabIndex<0||!named)failures.push({reason:'unnamed or unfocusable horizontal scroller',tag:e.tagName,id:e.id,class:e.getAttribute('class')});
  }
  if(!rows.length)failures.push({reason:'no visible content owners'});
  return {rows,failures};
}

function contrastRatio(foreground,background) {
  const lum=c=>c.slice(0,3).map(x=>x/255).map(x=>x<=.04045?x/12.92:((x+.055)/1.055)**2.4).reduce((n,x,i)=>n+x*[.2126,.7152,.0722][i],0);
  const a=lum(foreground),b=lum(background);
  return (Math.max(a,b)+.05)/(Math.min(a,b)+.05);
}

function renderedContrast(scope=document) {
  const rows=[],failures=[],exclusions=[];
  const canvas=document.createElement('canvas'),ctx=canvas.getContext('2d',{willReadFrequently:true});canvas.width=canvas.height=1;
  const cache=new Map();
  function color(value){
    if(cache.has(value))return cache.get(value);
    ctx.clearRect(0,0,1,1);ctx.fillStyle=value;ctx.fillRect(0,0,1,1);
    const p=[...ctx.getImageData(0,0,1,1).data];p[3]/=255;cache.set(value,p);return p;
  }
  const over=(fg,bg)=>{const a=fg[3]+bg[3]*(1-fg[3]);return [...fg.slice(0,3).map((x,i)=>a?(x*fg[3]+bg[i]*bg[3]*(1-fg[3]))/a:0),a];};
  // Resolved gradient stops give a conservative contrast bound. Every stop
  // (including translucent stops) is composited in paint order; interpolation
  // is sampled as well. We report the bound, never an invented point sample.
  function paints(s){
    const image=s.backgroundImage;
    if(image==='none'||s.backgroundClip==='text')return [];
    if(/url\(/.test(image))throw Error('unresolved background image');
    const layers=image.match(/(?:repeating-)?(?:linear|radial|conic)-gradient\((?:[^()]|\([^()]*\))*\)/g);
    if(!layers)throw Error('unresolved background paint: '+image);
    return layers.map(layer=>{
      const stops=(layer.match(/(?:rgba?|color)\([^)]*\)/g)||[]).map(color);
      if(!stops.length)throw Error('gradient has no resolved color stops');
      return stops.flatMap((c,i)=>i?[c,...[.25,.5,.75].map(t=>c.map((x,k)=>x*t+stops[i-1][k]*(1-t)))]:[c]);
    }).reverse();
  }
  function backgrounds(e){
    const lineage=[];for(let p=e;p;p=p.parentElement)lineage.unshift(p);
    let colors=[[255,255,255,1]],gradient=false;
    for(const p of lineage){const s=getComputedStyle(p),solid=color(s.backgroundColor);
      colors=solid[3]===1?[solid]:colors.map(bg=>over(solid,bg));
      for(const layer of paints(s)){gradient=true;colors=colors.flatMap(bg=>layer.map(fg=>over(fg,bg)));}
      // Retain extrema by luminance and hue, bounding a bounded paint stack.
      if(colors.length>512){colors.sort((a,b)=>contrastRatio(a,[0,0,0])-contrastRatio(b,[0,0,0]));colors=colors.filter((_,i)=>i%Math.ceil(colors.length/256)===0||i===colors.length-1);}
    }
    return {colors,gradient};
  }
  const walker=document.createTreeWalker(scope,NodeFilter.SHOW_TEXT),nodes=[];
  while(walker.nextNode())if(walker.currentNode.textContent.trim())nodes.push(walker.currentNode);
  window.learnContrastNodes=nodes;
  window.learnContrastOpacityGroups={};
  for(const [nodeIndex,node] of nodes.entries()){
    const e=node.parentElement,text=node.textContent.trim();
    if(!e||e.closest('script,style,noscript,template')||!visible(e))continue;
    if(e.closest('[disabled]')){exclusions.push({text,reason:'inactive control'});continue;}
    // A hidden tick or separator with no linguistic content is decoration.
    // aria-hidden alone does not exempt words, numbers or meaningful labels.
    if(!/[\p{L}\p{N}]/u.test(text)&&e.closest('[aria-hidden="true"]')){exclusions.push({text,reason:'decorative glyph'});continue;}
    const s=getComputedStyle(e),row={nodeIndex,tag:e.tagName,id:e.id,class:e.getAttribute('class'),text:text.slice(0,120),fontSize:parseFloat(s.fontSize),fontWeight:s.fontWeight};
    row.threshold=row.fontSize>=24||(row.fontSize>=18.6667&&parseFloat(row.fontWeight)>=700)?3:4.5;
    try{
      const bg=backgrounds(e);let inks;
      if(e instanceof SVGElement&&s.paintOrder.split(/\s+/)[0]==='stroke'&&parseFloat(s.strokeWidth)>=2&&s.stroke!=='none'){
        const halo=color(s.stroke);halo[3]*=Number(s.strokeOpacity);
        if(halo[3]===1){row.halo=halo;bg.colors=[halo];bg.gradient=false;}
      }
      if(s.backgroundClip==='text'){
        inks=(s.backgroundImage.match(/(?:rgba?|color)\([^)]*\)/g)||[]).map(color);
        if(!inks.length)throw Error('unresolved text gradient');
        row.gradientInk=true;
      }else inks=[color(e instanceof SVGElement?s.fill:s.color)];
      let opacity=1;const opacityGroups=[];
      for(let p=e;p;p=p.parentElement){const value=Number(getComputedStyle(p).opacity);opacity*=value;if(value!==1)opacityGroups.unshift([p,value]);}
      window.learnContrastOpacityGroups[nodeIndex]=opacityGroups;
      row.inks=inks;
      row.requiresRaster=(e instanceof SVGElement&&!row.halo)||opacity!==1;
      row.rasterGroup=e instanceof SVGElement?'svg:'+Array.from(document.querySelectorAll('svg')).indexOf(e.ownerSVGElement):'node:'+nodeIndex;
      const ratios=inks.flatMap(ink=>bg.colors.map(background=>({ratio:contrastRatio(over([...ink.slice(0,3),ink[3]*opacity],background),background),foreground:over([...ink.slice(0,3),ink[3]*opacity],background),background})));
      const worst=ratios.reduce((a,b)=>a.ratio<b.ratio?a:b);
      Object.assign(row,worst,{bound:bg.gradient||!!row.gradientInk});
      if(row.ratio+1e-6<row.threshold)failures.push({reason:'text contrast below threshold',...row});
    }catch(error){failures.push({reason:'text contrast measurement error',...row,error:error.message});}
    rows.push(row);
  }
  if(!rows.length)failures.push({reason:'no meaningful text contrast samples'});
  return {rows,exclusions,failures};
}
function themeState(expected) {
  const failures=[],explicit=document.documentElement.dataset.theme||null,
    systemLight=matchMedia('(prefers-color-scheme:light)').matches;
  const sample=document.createElement('span');sample.style.cssText='background:var(--bg);color:var(--text)';document.body.append(sample);
  const c=getComputedStyle(sample),actual={explicit,systemLight,background:c.backgroundColor,text:c.color,bodyText:getComputedStyle(document.body).color};sample.remove();
  const light=expected!=='dark';
  if((expected==='system-light'&&(explicit!==null||!systemLight))||
     (expected==='explicit-light'&&explicit!=='light')||(expected==='dark'&&explicit!=='dark'))failures.push({reason:'actual theme policy',expected,actual});
  if(actual.background!==(light?'rgb(237, 244, 248)':'rgb(7, 16, 25)')||
     (light&&(actual.text!=='rgb(16, 36, 51)'||actual.bodyText!=='rgb(16, 36, 51)')))failures.push({reason:'resolved theme colors',expected,actual});
  const rgb=value=>value.match(/[\d.]+/g).map(Number),ratio=contrastRatio(rgb(actual.text),rgb(actual.background));
  if(ratio<4.5)failures.push({reason:'theme text contrast below threshold',ratio,threshold:4.5,actual});
  return {actual,failures};
}
module.exports={visible,targets,svgGeometry,capstone,rootLayout,contrastRatio,renderedContrast,themeState};
