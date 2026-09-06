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
  const rows=[],failures=[];
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
    const row={text:e.textContent,svg:e.ownerSVGElement.id,rect:b.toJSON(),clipped:false,offscale:false,entity:/&(?:#\d+|#x[\da-f]+|[a-z]+);/i.test(e.textContent)};
    const c={left:Math.max(...clips.map(c=>c.left)),top:Math.max(...clips.map(c=>c.top)),
      right:Math.min(...clips.map(c=>c.right)),bottom:Math.min(...clips.map(c=>c.bottom))};
    row.offscale=b.right<=c.left||b.left>=c.right||b.bottom<=c.top||b.top>=c.bottom;
    row.clipped=!row.offscale&&(b.left<c.left-.1||b.right>c.right+.1||b.top<c.top-.1||b.bottom>c.bottom+.1);
    // Offscale labels should be intentionally absent, not clipped DOM text.
    if(row.clipped||row.offscale||row.entity) failures.push(row);
    rows.push(row);
  }
  return {rows,failures};
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
  const failures=[];
  for(const e of [document.documentElement,document.body]) {
    const c=getComputedStyle(e);
    if(['hidden','clip'].includes(c.overflowX))failures.push({reason:'root masking',tag:e.tagName});
    if(e.scrollWidth>document.documentElement.clientWidth)failures.push({reason:'root overflow',tag:e.tagName,width:e.scrollWidth});
  }
  return {failures};
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
  return {actual,failures};
}
module.exports={visible,targets,svgGeometry,capstone,rootLayout,themeState};
