/* Browser assertions use rendered geometry, native label associations and live
 * text bounds. No CSS-token assertions or URL-specific acceptance exceptions. */
'use strict';

function activeContent(e) {
  if(!e||e.closest('[hidden],.skip-link,script,style,noscript,template'))return false;
  for(let p=e;p;p=p.parentElement)if(getComputedStyle(p).display==='none')return false;
  return true;
}
function semanticSvgText(e) {
  return activeContent(e)&&e.textContent.trim()&&(/[\p{L}\p{N}]/u.test(e.textContent)||!e.closest('[aria-hidden="true"]'));
}
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
async function svgGeometry(scope=document) {
  const rows=[],failures=[],capabilities=[],entries=[],documentSvgs=[...document.querySelectorAll('svg')];
  const svgs=Array.isArray(scope)?scope:scope instanceof SVGElement?[scope]:[...scope.querySelectorAll('svg')];
  for(const svg of svgs){
    const svgIndex=documentSvgs.indexOf(svg);
    if(svgIndex<0)throw Error('raster setup failure: SVG measurement scope is outside the document');
    if(!activeContent(svg))continue;
    const labels=[...svg.querySelectorAll('text')].filter(e=>semanticSvgText(e)&&e.ownerSVGElement===svg);
    if(!labels.length)continue; // text-free and non-semantic decoration
    const readable=labels.filter(visible);
    capabilities.push({svg:svg.id,svgIndex,semantic:labels.length,readable:readable.length});
    if(!readable.length)failures.push({reason:'no readable semantic SVG labels',svg:svg.id,semantic:labels.length});
    for(const e of labels){
      if(!visible(e)){failures.push({reason:'hidden semantic SVG label',svg:svg.id,text:e.textContent});continue;}
      const row={text:e.textContent,svg:svg.id,svgIndex,rect:e.getBoundingClientRect().toJSON(),clipped:false,offscale:false,entity:/&(?:#\d+|#x[\da-f]+|[a-z]+);/i.test(e.textContent)};
      if(row.entity)failures.push(row);
      entries.push({element:e,nodeIndex:rows.length});rows.push(row);
    }
  }
  for(const paint of await measureTextPaint(entries,'geometry')){
    const row=rows[paint.nodeIndex];row.paint=paint;
    row.clipped=paint.missingPixels>0;row.offscale=!paint.sampleCount;
    if(paint.error)failures.push({reason:paint.error,text:row.text,svg:row.svg,...paint});
  }
  for(const item of capabilities){
    const measured=rows.filter(r=>r.svgIndex===item.svgIndex&&!r.clipped&&!r.offscale&&!r.paint?.error);
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
function namedHorizontalScroller(e) {
  const s=getComputedStyle(e);
  const name=e.getAttribute('aria-label')||e.getAttribute('aria-labelledby')?.split(/\s+/).map(id=>document.getElementById(id)?.textContent||'').join('').trim();
  return ['auto','scroll'].includes(s.overflowX)&&e.tabIndex>=0&&!!name;
}
function rootLayout() {
  const failures=[],rows=[];
  for(const e of [document.documentElement,document.body]) {
    const c=getComputedStyle(e);
    if(['hidden','clip'].includes(c.overflowX)||['hidden','clip'].includes(c.overflowY))failures.push({reason:'root masking',tag:e.tagName});
    if(e.scrollWidth>document.documentElement.clientWidth)failures.push({reason:'root overflow',tag:e.tagName,width:e.scrollWidth});
  }
  for(const e of document.querySelectorAll('main,main *,article,section,[role="main"],[role="main"] *,[data-ui],.content,.main-content')) {
    if(!visible(e))continue;
    const s=getComputedStyle(e),row={tag:e.tagName,id:e.id,class:e.className,width:e.clientWidth,scrollWidth:e.scrollWidth,height:e.clientHeight,scrollHeight:e.scrollHeight};
    rows.push(row);
    const clipX=['hidden','clip'].includes(s.overflowX),clipY=['hidden','clip'].includes(s.overflowY);
    if(clipX||clipY) {
      const b=e.getBoundingClientRect(),walker=document.createTreeWalker(e,NodeFilter.SHOW_TEXT),bounds=[];
      while(walker.nextNode()){
        const node=walker.currentNode;if(!node.textContent.trim()||!visible(node.parentElement)||node.parentElement.closest('script,style'))continue;
        let scroller=null;for(let p=node.parentElement;p&&p!==e;p=p.parentElement)if(namedHorizontalScroller(p)){scroller=p;break;}
        const range=document.createRange();range.selectNode(node);
        bounds.push(...(scroller?[scroller.getBoundingClientRect()]:range.getClientRects()));
      }
      for(const item of e.querySelectorAll('canvas,svg,input,select,textarea,button'))if(visible(item)){
        let mediaScroller=null;
        for(let p=item.parentElement;p&&p!==e;p=p.parentElement)if(namedHorizontalScroller(p)){mediaScroller=p;break;}
        bounds.push((mediaScroller||item).getBoundingClientRect());
      }
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
    if(!namedHorizontalScroller(e))failures.push({reason:'unnamed or unfocusable horizontal scroller',tag:e.tagName,id:e.id,class:e.getAttribute('class')});
  }
  if(!rows.length)failures.push({reason:'no visible content owners'});
  return {rows,failures};
}

/* The two diagnostic rasters locate glyph interiors only. Acceptance always
 * compares the unmodified screenshot with the same page minus that text's ink.
 * Removing clips/opacity for a diagnostic can expose a missing glyph, but can
 * never supply its accepted foreground. Chromium owns transforms, masks,
 * gradients, patterns, group compositing and later paint in these captures. */
async function measureTextPaint(entries, mode='contrast', captureScope='target', includeCoreEvidence=false) {
  if(typeof includeCoreEvidence!=='boolean')throw Error('raster setup failure: invalid core evidence request');
  if(!['target','viewport'].includes(captureScope))throw Error('raster setup failure: invalid capture scope');
  if(typeof window.learnCaptureRaster!=='function')throw Error('raster setup failure: capture bridge unavailable');
  const results=[],scroll=[...document.querySelectorAll('*')].map(e=>[e,e.scrollLeft,e.scrollTop]);
  const originalStyles=[...document.querySelectorAll('*')].map(e=>[e,e.getAttribute('style')]);
  const originalVisibility=originalStyles.map(([e])=>[e,getComputedStyle(e).visibility]);
  let cameraScrollOwners=[];
  const restore=()=>{originalStyles.forEach(([e,s])=>{e.setAttribute('style',s||'');e.getAttribute('style');if(s===null)e.removeAttribute('style');});for(const e of cameraScrollOwners)e.style.setProperty('overflow-anchor','none','important');};
  const settleRestoredFrame=async()=>{
    window.learnRasterRestoreSettles=(window.learnRasterRestoreSettles||0)+1;
    const mismatches=()=>{
      const found=[];
      for(let i=0;i<originalStyles.length&&found.length<12;i++){
        const [e,style]=originalStyles[i],visibility=originalVisibility[i][1];
        if(!e.isConnected||e.getAttribute('style')!==style||getComputedStyle(e).visibility!==visibility)
          found.push({kind:'style',tag:e.tagName,id:e.id,connected:e.isConnected,style:e.getAttribute('style'),expectedStyle:style,visibility:getComputedStyle(e).visibility,expectedVisibility:visibility});
      }
      for(let i=0;i<scroll.length&&found.length<12;i++){
        const [e,left,top]=scroll[i];
        if(Math.abs(e.scrollLeft-left)>.5||Math.abs(e.scrollTop-top)>.5)
          found.push({kind:'scroll',tag:e.tagName,id:e.id,left:e.scrollLeft,top:e.scrollTop,expectedLeft:left,expectedTop:top});
      }
      return found;
    };
    let previousClean=false,last=[];
    for(let frame=1;frame<=60;frame++){
      await new Promise(r=>requestAnimationFrame(r));last=mismatches();
      if(!last.length&&previousClean){window.learnRasterRestoreFrames=(window.learnRasterRestoreFrames||0)+frame;return;}
      previousClean=!last.length;
    }
    throw Error('raster setup failure: restored frame did not settle '+JSON.stringify({frames:60,mismatches:last}));
  };
  const set=(e,k,v)=>e.style.setProperty(k,v,'important');
  let currentEntry,frame=null,captureIndex=0,captureNames=[],tileIndex=0,capturePhase='',capturePhases=[],captureFrame=null;
  function metricsNow(){
    const owners=[];
    for(let p=currentEntry.element;p;p=p.parentElement)owners.push({tag:p.tagName,id:p.id,scrollLeft:p.scrollLeft,scrollTop:p.scrollTop,clientWidth:p.clientWidth,clientHeight:p.clientHeight,scrollWidth:p.scrollWidth,scrollHeight:p.scrollHeight,bounds:p.getBoundingClientRect().toJSON()});
    return {innerWidth,innerHeight,devicePixelRatio,scrollX,scrollY,clientWidth:document.documentElement.clientWidth,clientHeight:document.documentElement.clientHeight,visual:visualViewport&&{width:visualViewport.width,height:visualViewport.height,offsetLeft:visualViewport.offsetLeft,offsetTop:visualViewport.offsetTop,pageLeft:visualViewport.pageLeft,pageTop:visualViewport.pageTop},owners};
  }
  function verifyFrame(metrics,metadata){
    if((mode==='contrast'||currentEntry.element instanceof SVGElement)&&frame&&JSON.stringify(metrics)!==JSON.stringify(frame))throw Error('raster setup failure: capture metrics changed '+JSON.stringify(metadata));
    if(!frame)frame=metrics;
  }
  async function capture(){
    await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));
    const metrics=metricsNow();
    const metadata={nodeIndex:currentEntry.nodeIndex,site:currentEntry.element.id||currentEntry.element.tagName,text:(currentEntry.node||currentEntry.element).textContent.slice(0,160),mode,tile:tileIndex,phase:capturePhase,metrics,captureFrame};
    captureIndex++;capturePhases.push(capturePhase);
    verifyFrame(metrics,metadata);
    const img=new Image();img.src='data:image/png;base64,'+await window.learnCaptureRaster(metadata);await img.decode();
    const decodedMetrics=metricsNow();
    verifyFrame(decodedMetrics,{...metadata,phase:metadata.phase+':decoded',metrics:decodedMetrics,decoded:{width:img.width,height:img.height}});
    const canvas=document.createElement('canvas');canvas.width=img.width;canvas.height=img.height;
    const ctx=canvas.getContext('2d',{willReadFrequently:true});if(!ctx)throw Error('raster setup failure: no pixel context');
    ctx.drawImage(img,0,0);return {data:ctx.getImageData(0,0,img.width,img.height).data,width:img.width,height:img.height};
  }
  function sameRaster(a,b){
    if(a.width!==b.width||a.height!==b.height||a.data.length!==b.data.length)return false;
    for(let i=0;i<a.data.length;i++)if(a.data[i]!==b.data[i])return false;
    return true;
  }
  try{
    for(const entry of entries){
      currentEntry=entry;frame=null;captureIndex=0;
      const e=entry.element,node=entry.node,svg=e instanceof SVGElement;
      const lineage=[];for(let p=e;p&&p!==document.documentElement;p=p.parentElement)lineage.push(p);
      restore();
      // Center only the document camera. Element.scrollIntoView() is not used:
      // it can silently move unnamed or unfocusable nested scroll owners before
      // the explicit, audited tile plan decides which owners may move.
      const nested=lineage.filter(p=>p!==document.body&&p!==document.scrollingElement).map(p=>[p,p.scrollLeft,p.scrollTop]);
      const viewTarget=e.ownerSVGElement||e,viewBox=viewTarget.getBoundingClientRect();
      window.scrollBy({left:viewBox.left+viewBox.width/2-innerWidth/2,top:viewBox.top+viewBox.height/2-innerHeight/2,behavior:'instant'});
      for(const [p,left,top] of nested)p.scrollTo({left,top,behavior:'instant'});
      const range=document.createRange();if(node)range.selectNode(node);
      const copyRect=r=>({left:r.left,top:r.top,right:r.right,bottom:r.bottom,width:r.width,height:r.height});
      const nativeScroll=!node&&e.matches('input,textarea');
      function currentRects(){
        if(node)return [...range.getClientRects()].filter(r=>r.width&&r.height).map(copyRect);
        const r=e.getBoundingClientRect();
        if(!nativeScroll&&!e.matches('select'))return [copyRect(r)];
        // Native text is painted inside the control's border. A select's
        // border is not a missing segment of its selected option's text.
        const {scaleX,scaleY}=cssScale(e);
        const left=r.left+(e.clientLeft-(nativeScroll?e.scrollLeft:0))*scaleX,top=r.top+(e.clientTop-(nativeScroll?e.scrollTop:0))*scaleY;
        const width=(nativeScroll?e.scrollWidth:e.clientWidth)*scaleX,height=(nativeScroll?e.scrollHeight:e.clientHeight)*scaleY;
        return [{left,top,right:left+width,bottom:top+height,width,height}];
      }
      const sourceRects=currentRects();
      if(!sourceRects.length)throw Error('raster setup failure: empty target rectangles');
      function translation(){
        const now=currentRects(),dx=now[0].left-sourceRects[0].left,dy=now[0].top-sourceRects[0].top;
        if(now.length!==sourceRects.length||now.some((r,i)=>['left','right'].some(k=>Math.abs(r[k]-sourceRects[i][k]-dx)>.001)||['top','bottom'].some(k=>Math.abs(r[k]-sourceRects[i][k]-dy)>.001)))throw Error('raster setup failure: target geometry changed between tiles');
        return {dx,dy};
      }
      const intersect=(a,b)=>({left:Math.max(a.left,b.left),top:Math.max(a.top,b.top),right:Math.min(a.right,b.right),bottom:Math.min(a.bottom,b.bottom)});
      const positive=r=>r.right>r.left&&r.bottom>r.top;
      const scrollOwnerName=p=>p.getAttribute('aria-label')||p.getAttribute('aria-labelledby')?.split(/\s+/).map(id=>document.getElementById(id)?.textContent||'').join('').trim();
      const approvedScrollOwner=p=>p.tabIndex>=0&&!!scrollOwnerName(p);
      function cssScale(p){
        let matrix=new DOMMatrix();
        for(let a=p;a;a=a.parentElement){const st=getComputedStyle(a),t=new DOMMatrix(st.transform==='none'?undefined:st.transform),zoom=st.zoom.endsWith('%')?parseFloat(st.zoom)/100:Number(st.zoom)||1;matrix=t.scale(zoom).multiply(matrix);}
        if(!matrix.is2D||Math.abs(matrix.b)>1e-8||Math.abs(matrix.c)>1e-8||matrix.a<=0||matrix.d<=0)throw Error('raster setup failure: unsupported scroll-owner transform');
        return {scaleX:matrix.a,scaleY:matrix.d};
      }
      function clipRect(){
        let clip={left:0,top:0,right:innerWidth,bottom:innerHeight};
        for(const p of lineage){
          const st=getComputedStyle(p);
          if(p===document.body||!['hidden','clip','auto','scroll'].includes(st.overflowX)&&!['hidden','clip','auto','scroll'].includes(st.overflowY))continue;
          // SVG clipping bounds stay in the coverage plan. Named, focusable
          // scroll ports can move tile by tile; other ports cannot become a
          // measurement camera. Non-SVG geometry retains its established
          // unclipped diagnostic behavior.
          if(mode==='geometry'&&!svg)continue;
          const clipping=mode==='geometry'?['auto','scroll']:['hidden','clip','auto','scroll'];
          const r=p.getBoundingClientRect(),{scaleX,scaleY}=cssScale(p);
          const box={left:r.left+p.clientLeft*scaleX,top:r.top+p.clientTop*scaleY,right:r.left+(p.clientLeft+p.clientWidth)*scaleX,bottom:r.top+(p.clientTop+p.clientHeight)*scaleY};
          if(clipping.includes(st.overflowX))clip=intersect(clip,{...clip,left:box.left,right:box.right});
          if(clipping.includes(st.overflowY))clip=intersect(clip,{...clip,top:box.top,bottom:box.bottom});
        }
        return clip;
      }
      function subtract(rect,cover){
        const i=intersect(rect,cover);if(!positive(i))return [rect];
        return [{...rect,bottom:i.top},{...rect,top:i.bottom},{left:rect.left,right:i.left,top:i.top,bottom:i.bottom},{left:i.right,right:rect.right,top:i.top,bottom:i.bottom}].filter(positive);
      }
      const uncovered=(r,covers)=>covers.reduce((parts,c)=>parts.flatMap(p=>subtract(p,c)),[r]);
      const scrollers=lineage.filter(p=>{
        const st=getComputedStyle(p),scrollable=((nativeScroll&&p===e||['auto','scroll'].includes(st.overflowX))&&p.scrollWidth>p.clientWidth)||((nativeScroll&&p===e||['auto','scroll'].includes(st.overflowY))&&p.scrollHeight>p.clientHeight);
        return scrollable&&(!svg||mode!=='geometry'||approvedScrollOwner(p));
      });
      // Glyph suppression must not initiate browser scroll anchoring. This
      // changes no paint or clipping; deliberate tiles remain metric-guarded.
      cameraScrollOwners=[...lineage,document.documentElement];for(const p of cameraScrollOwners)set(p,'overflow-anchor','none');
      const captureStates=[],plannedCoverage=[];
      const state=()=>[...scrollers,document.scrollingElement].map(p=>[p,p.scrollLeft,p.scrollTop]);
      function addTile(){
        const {dx,dy}=translation(),clip=clipRect();
        const coverage=sourceRects.map(r=>intersect(r,{left:clip.left-dx,right:clip.right-dx,top:clip.top-dy,bottom:clip.bottom-dy})).filter(positive);
        if(!coverage.some(r=>uncovered(r,plannedCoverage).length))return;
        captureStates.push({scroll:state(),coverage});plannedCoverage.push(...coverage);
      }
      addTile();
      const fixedClip=mode==='contrast'&&lineage.some(p=>{
        if(p===document.body||nativeScroll&&p===e)return false;
        const st=getComputedStyle(p);if(!['hidden','clip'].includes(st.overflowX)&&!['hidden','clip'].includes(st.overflowY))return false;
        const box=p.getBoundingClientRect(),{scaleX,scaleY}=cssScale(p);
        return sourceRects.some(r=>['hidden','clip'].includes(st.overflowX)&&(r.left<box.left+p.clientLeft*scaleX||r.right>box.left+(p.clientLeft+p.clientWidth)*scaleX)||['hidden','clip'].includes(st.overflowY)&&(r.top<box.top+p.clientTop*scaleY||r.bottom>box.top+(p.clientTop+p.clientHeight)*scaleY));
      });
      // A fixed outer clip can contain a legitimate inner scroll camera. Plan
      // every finite camera position while clipRect() keeps all authored
      // clipping in force. A truly clipped target still retains coverage gaps
      // and fails; an inner named/focusable port can now expose its full text.
      if((mode==='contrast'||svg)&&(!fixedClip||scrollers.length)&&sourceRects.some(r=>uncovered(r,plannedCoverage).length)){
        let cellWidth=innerWidth,cellHeight=innerHeight;
        for(const p of lineage){const st=getComputedStyle(p);if(['auto','scroll','hidden','clip'].includes(st.overflowX))cellWidth=Math.min(cellWidth,p.clientWidth);if(['auto','scroll','hidden','clip'].includes(st.overflowY))cellHeight=Math.min(cellHeight,p.clientHeight);}
        cellWidth=Math.max(1,cellWidth-8);cellHeight=Math.max(1,cellHeight-8);
        let candidates=0;
        for(const r of sourceRects){
          const nx=Math.ceil((r.right-r.left)/cellWidth),ny=Math.ceil((r.bottom-r.top)/cellHeight);
          if((candidates+=nx*ny)>4096)throw Error('raster setup failure: finite tile limit exceeded');
          for(let yi=0;yi<ny;yi++)for(let xi=0;xi<nx;xi++){
            const cell={left:r.left+(r.right-r.left)*xi/nx,right:r.left+(r.right-r.left)*(xi+1)/nx,top:r.top+(r.bottom-r.top)*yi/ny,bottom:r.top+(r.bottom-r.top)*(yi+1)/ny};
            if(!uncovered(cell,plannedCoverage).length)continue;
            const cx=(cell.left+cell.right)/2,cy=(cell.top+cell.bottom)/2;
            for(const p of scrollers){
              const st=getComputedStyle(p),box=p.getBoundingClientRect(),{dx,dy}=translation();
              const {scaleX,scaleY}=cssScale(p);
              if(!scaleX||!scaleY)throw Error('raster setup failure: unmeasurable scroll transform');
              const left=p.scrollLeft+(nativeScroll&&p===e||['auto','scroll'].includes(st.overflowX)?(cx+dx-box.left)/scaleX-p.clientLeft-p.clientWidth/2:0);
              const top=p.scrollTop+(nativeScroll&&p===e||['auto','scroll'].includes(st.overflowY)?(cy+dy-box.top)/scaleY-p.clientTop-p.clientHeight/2:0);
              // Offset assignment honors authored smooth scrolling. A tile
              // needs its deliberate camera movement to finish immediately.
              p.scrollTo({left,top,behavior:'instant'});
            }
            const {dx,dy}=translation();window.scrollBy({left:cx+dx-innerWidth/2,top:cy+dy-innerHeight/2,behavior:'instant'});addTile();
          }
        }
      }
      if(!captureStates.length)captureStates.push({scroll:state(),coverage:[]});
      let samples=0,missing=0,worst=null,expected=0;
      const visited=new Set(),tiles=[],capturedCoverage=[],coreEvidence=[];
      for(tileIndex=0;tileIndex<captureStates.length;tileIndex++){
      const tile=captureStates[tileIndex];for(const [p,left,top] of tile.scroll)p.scrollTo({left,top,behavior:'instant'});
      frame=null;captureIndex=0;capturePhases=[];
      const tileSamplesBefore=samples,tileExpectedBefore=expected,tileMissingBefore=missing;
      const delta=translation(),clip=clipRect();
      const rects=mode==='geometry'&&!svg?currentRects():currentRects().map(r=>intersect(r,clip)).filter(positive);
      const s=getComputedStyle(e),hasStroke=(svg?s.stroke!=='none'&&parseFloat(s.strokeWidth)>0:parseFloat(s.webkitTextStrokeWidth)>0)||s.textShadow!=='none';
      const strokeOnly=svg&&s.fill==='none';
      captureFrame=null;
      if((mode==='contrast'||svg)&&captureScope==='target'){
        const padding=Math.ceil(parseFloat(s.fontSize)/4)+2;
        const left=Math.max(0,Math.floor(Math.min(...rects.map(r=>r.left))-padding)),top=Math.max(0,Math.floor(Math.min(...rects.map(r=>r.top))-padding));
        const right=Math.min(innerWidth,Math.ceil(Math.max(...rects.map(r=>r.right))+padding)),bottom=Math.min(innerHeight,Math.ceil(Math.max(...rects.map(r=>r.bottom))+padding));
        captureFrame=rects.length?{left,top,width:Math.max(1,right-left),height:Math.max(1,bottom-top)}:{left:0,top:0,width:1,height:1};
      }

      const targets=[e,...e.querySelectorAll('*')];
      captureNames=hasStroke&&!strokeOnly?['original','halo','backdrop','black','white']:['original','backdrop','black','white'];
      // A document-camera move can reach its final metrics before an offscreen
      // SVG's glyph layer is present in a CDP screenshot. Require two
      // consecutive untouched rasters to agree. Earlier frames are never
      // accepted as foreground evidence, and perpetual drift fails setup.
      capturePhase='settle';
      let settleCapture=await capture(),acceptedOriginal=null,untouchedCaptures=1;
      while(untouchedCaptures<6){
        capturePhases=[];captureIndex=0;capturePhase='original';
        const original=await capture();untouchedCaptures++;
        if(original.width!==settleCapture.width||original.height!==settleCapture.height)throw Error('raster setup failure: dimensions changed '+JSON.stringify({nodeIndex:entry.nodeIndex,mode,tile:tileIndex,captureFrame,untouchedCaptures,captures:[settleCapture,original].map(p=>({width:p.width,height:p.height}))}));
        if(sameRaster(settleCapture,original)){acceptedOriginal=original;break;}
        settleCapture=original;
      }
      if(!acceptedOriginal)throw Error('raster setup failure: untouched frame did not settle '+JSON.stringify({nodeIndex:entry.nodeIndex,mode,tile:tileIndex,captureFrame,untouchedCaptures,metrics:frame}));
      const original=acceptedOriginal;
      for(const t of targets){set(t,'-webkit-text-fill-color','transparent');set(t,'fill','transparent');if(getComputedStyle(t).backgroundClip==='text')set(t,'background-image','none');}
      capturePhase='halo';
      const halo=hasStroke&&!strokeOnly?await capture():null;
      for(const t of targets){set(t,'stroke','transparent');set(t,'-webkit-text-stroke-color','transparent');set(t,'text-shadow','none');}
      capturePhase='backdrop';
      const backdrop=await capture();
      restore();
      const diagnosticTargets=targets;
      // Hide every other paint owner while keeping the live target at its
      // exact compositor position. Geometry mode deliberately removes clips
      // and masks to obtain full ink; the unchanged capture-frame guard makes
      // any resulting viewport or layout drift a setup failure. Contrast mode
      // retains authored clipping and overflow.
      for(const [t] of originalStyles)set(t,'visibility','hidden');
      for(let t=e;t;t=t.parentElement){
        set(t,'opacity','1');set(t,'filter','none');
        if(mode==='geometry'){
          set(t,'clip-path','none');set(t,'mask','none');
          // SVG scroll ports are camera boundaries and remain tileable. Their
          // overflow must not be opened merely to make a diagnostic mask;
          // doing so can change root metrics. Non-SVG geometry retains the
          // established unclip behavior.
          if(!svg){set(t,'overflow','visible');set(t,'clip','auto');}
        }
      }
      for(const t of targets){
        set(t,'visibility','visible');set(t,'opacity','1');set(t,'fill-opacity','1');set(t,'stroke-opacity','1');set(t,'filter','none');set(t,'text-shadow','none');set(t,'caret-color','transparent');
        if(mode==='geometry'){set(t,'clip-path','none');set(t,'mask','none');}
        if(getComputedStyle(t).backgroundClip==='text')set(t,'background-image','none');
        if(!strokeOnly){set(t,'stroke','transparent');set(t,'-webkit-text-stroke-color','transparent');}
      }
      const diagnostic=async ink=>{
        for(const t of diagnosticTargets){set(t,'fill',strokeOnly?'none':ink);set(t,'-webkit-text-fill-color',ink);if(strokeOnly)set(t,'stroke',ink);}
        capturePhase=ink==='#000'?'black':'white';return capture();
      };
      const black=await diagnostic('#000'),white=await diagnostic('#fff');
      restore();
      const requestedRaster=mode==='contrast'||svg?{width:Math.round((captureFrame?.width??innerWidth)*2*devicePixelRatio),height:Math.round((captureFrame?.height??innerHeight)*2*devicePixelRatio)}:null;
      /* raster-dimensions:begin */
      if([settleCapture,backdrop,halo,black,white].filter(Boolean).some(p=>p.width!==original.width||p.height!==original.height)||requestedRaster&&[settleCapture,original,backdrop,halo,black,white].filter(Boolean).some(p=>p.width!==requestedRaster.width||p.height!==requestedRaster.height))throw Error('raster setup failure: dimensions changed '+JSON.stringify({nodeIndex:entry.nodeIndex,mode,requestedRaster,captures:[settleCapture,original,halo,backdrop,black,white].filter(Boolean).map(p=>({width:p.width,height:p.height}))}));
      /* raster-dimensions:end */
      const origin=captureFrame||{left:0,top:0,width:innerWidth,height:innerHeight};
      const sx=original.width/origin.width,sy=original.height/origin.height;
      for(const r of rects){
        for(let y=Math.max(0,Math.floor((r.top-origin.top)*sy));y<Math.min(original.height,Math.ceil((r.bottom-origin.top)*sy));y++){
          for(let x=Math.max(0,Math.floor((r.left-origin.left)*sx));x<Math.min(original.width,Math.ceil((r.right-origin.left)*sx));x++){
            const i=(y*original.width+x)*4,key=(x+(origin.left-delta.dx)*sx).toFixed(4)+','+(y+(origin.top-delta.dy)*sy).toFixed(4);if(visited.has(key))continue;
            const coverage=Math.min(...[0,1,2].map(k=>Math.abs(white.data[i+k]-black.data[i+k])))/255;
            // A meaningful glyph core is fully covered in both diagnostic
            // colors. Partly covered edge pixels can move by one raster cell
            // when Chromium composites the isolated SVG copy at a fractional
            // screen origin; treating those fringes as cores creates false
            // clipping without proving any final ink was lost. Tiny text with
            // no full-coverage pixel still fails through the empty-sample
            // guard, while real clipping, masks and later paint continue to
            // remove full cores and fail below.
            if(coverage!==1)continue;
            visited.add(key);expected++;
            const rgb=p=>[p.data[i],p.data[i+1],p.data[i+2]];
            const foreground=rgb(original),background=rgb(backdrop);
            const actualDelta=Math.max(...foreground.map((v,k)=>Math.abs(v-background[k])));

            let sample={ratio:contrastRatio(foreground,background),foreground,background,x:x/sx+origin.left,y:y/sy+origin.top};
            if(halo){
              const local=rgb(halo),ratio=contrastRatio(foreground,local);if(ratio>sample.ratio)sample={...sample,ratio,background:local};
              const adequate=mode==='geometry'?1.000001:(entry.threshold||4.5);
              const radius=Math.ceil(parseFloat(s.fontSize)*Math.max(sx,sy)/4);
              // A halo surrounds a glyph; it need not extend underneath the
              // middle of a thick stem. Use only nearby stroke pixels present
              // in the unmodified image and attributable to this text.
              search: for(let dy=-radius;sample.ratio<adequate&&dy<=radius;dy++)for(let dx=-radius;dx<=radius;dx++){
                const xx=x+dx,yy=y+dy;if(xx<0||yy<0||xx>=original.width||yy>=original.height||dx*dx+dy*dy>radius*radius)continue;
                const j=(yy*original.width+xx)*4;
                if(![0,1,2].some(k=>Math.abs(halo.data[j+k]-backdrop.data[j+k])>=1))continue;
                if([0,1,2].some(k=>Math.abs(halo.data[j+k]-original.data[j+k])>1))continue;
                const local=[original.data[j],original.data[j+1],original.data[j+2]],ratio=contrastRatio(foreground,local);
                if(ratio>sample.ratio)sample={...sample,ratio,background:local};
                if(sample.ratio>=adequate)break search;
              }
            }
            if(actualDelta<1&&(!halo||sample.ratio<=1))missing++;
            if(includeCoreEvidence)coreEvidence.push([x/sx+origin.left-delta.dx,y/sy+origin.top-delta.dy,...foreground,...background,...sample.background]);
            samples++;if(!worst||sample.ratio<worst.ratio)worst=sample;
          }
        }
      }
      const actualCoverage=sourceRects.map(r=>intersect(r,{left:clip.left-delta.dx,right:clip.right-delta.dx,top:clip.top-delta.dy,bottom:clip.bottom-delta.dy})).filter(positive);
      const exclusiveCoverage=[];for(const r of actualCoverage){const fresh=uncovered(r,capturedCoverage);exclusiveCoverage.push(...fresh);capturedCoverage.push(...fresh);}
      tiles.push({index:tileIndex,frame,captureFrame:origin,decoded:{width:original.width,height:original.height},coverage:exclusiveCoverage,viewportCoverage:actualCoverage,sourceTranslation:delta,settleCaptures:untouchedCaptures-1,untouchedCaptures,untouchedFramesEqual:true,captures:capturePhases.slice(),completeFrame:true,sampleCount:samples-tileSamplesBefore,expectedPixels:expected-tileExpectedBefore,missingPixels:missing-tileMissingBefore});
      }
      const gaps=sourceRects.flatMap(r=>uncovered(r,capturedCoverage));
      const measurement={nodeIndex:entry.nodeIndex,measurement:'actual ink and backdrop raster',sampleCount:samples,expectedPixels:expected,missingPixels:missing,...worst,...(includeCoreEvidence?{coreEvidence}:{}),tiling:{sourceRects,plannedTiles:captureStates.length,capturedTiles:tiles.length,tiles,gaps,complete:!gaps.length}};
      if(!samples)measurement.error='no rendered glyph interior samples';
      else if(gaps.length)measurement.error='unmeasured semantic text outside viewport';
      else if(mode==='geometry'&&missing)measurement.error='semantic SVG glyph pixels absent, clipped, masked or occluded';
      results.push(measurement);
    }
  }finally{cameraScrollOwners=[];restore();for(const [e,left,top] of scroll)e.scrollTo({left,top,behavior:'instant'});await settleRestoredFrame();}
  return results;
}

function contrastRatio(foreground,background) {
  const lum=c=>c.slice(0,3).map(x=>x/255).map(x=>x<=.04045?x/12.92:((x+.055)/1.055)**2.4).reduce((n,x,i)=>n+x*[.2126,.7152,.0722][i],0);
  const a=lum(foreground),b=lum(background);
  return (Math.max(a,b)+.05)/(Math.min(a,b)+.05);
}

function accessibleControlName(e) {
  if(e instanceof SVGElement)return false;
  const s=getComputedStyle(e),owner=e.closest('a[href],button,label');
  const clipped=s.clip!=='auto'&&s.clip!=='none'||/inset\(50%\)/.test(s.clipPath);
  return !!owner&&visible(owner.tagName==='LABEL'?owner.control:owner)&&s.position==='absolute'&&parseFloat(s.width)<=1&&parseFloat(s.height)<=1&&clipped;
}
function nativeText(control) {
  if(control instanceof HTMLSelectElement)return [...control.selectedOptions].map(o=>o.textContent).join(' ');
  if(control.type==='file')return [...control.files].map(f=>f.name).join(' ');
  return control.value||control.getAttribute('placeholder')||'';
}
function screenFontSize(e, size) {
  let matrix=new DOMMatrix();
  for(let p=e;p;p=p.parentElement){
    if(p instanceof SVGElement){const screen=p.getScreenCTM();if(!screen)return 0;matrix=new DOMMatrix([screen.a,screen.b,screen.c,screen.d,screen.e,screen.f]).multiply(matrix);break;}
    const s=getComputedStyle(p),transform=new DOMMatrix(s.transform==='none'?undefined:s.transform);
    if(!transform.is2D)return 0; // a 3D font size cannot justify the large-text exception
    const zoom=s.zoom.endsWith('%')?parseFloat(s.zoom)/100:Number(s.zoom)||1;
    matrix=transform.scale(zoom).multiply(matrix);
  }
  return size*Math.hypot(matrix.c,matrix.d);
}
function renderedContrast(scope=document) {
  const rows=[],failures=[],exclusions=[];
  const canvas=document.createElement('canvas'),ctx=canvas.getContext('2d',{willReadFrequently:true});canvas.width=canvas.height=1;
  const cache=new Map();
  function color(value){
    if(cache.has(value))return cache.get(value);
    if(!CSS.supports('color',value))throw Error('unresolved color: '+value);
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
  for(const control of scope.querySelectorAll('input,textarea,select')){
    if(control.matches('input')&&['range','color','checkbox','radio','hidden','image'].includes(control.type))continue;
    if(nativeText(control).trim())nodes.push(control);
  }
  window.learnContrastNodes=nodes;
  window.learnContrastOpacityGroups={};
  for(const [nodeIndex,node] of nodes.entries()){
    const native=node instanceof Element;
    const e=native?node:node.parentElement,text=(native?nativeText(node):node.textContent).trim();
    if(!e||e.closest('script,style,noscript,template,option')||(!native&&e.closest('textarea,select'))||!activeContent(e))continue;
    if(accessibleControlName(e)){exclusions.push({text,reason:'accessible-only name of a visible control'});continue;}
    // A hidden tick or separator with no linguistic content is decoration.
    // aria-hidden alone does not exempt words, numbers or meaningful labels.
    if(!/[\p{L}\p{N}]/u.test(text)&&e.closest('[aria-hidden="true"]')){exclusions.push({text,reason:'decorative glyph'});continue;}
    const s=getComputedStyle(e),row={nodeIndex,tag:e.tagName,id:e.id,class:e.getAttribute('class'),text:text.slice(0,120),fontSize:parseFloat(s.fontSize),fontWeight:s.fontWeight};
    row.renderedFontSize=screenFontSize(e,row.fontSize);
    row.threshold=row.renderedFontSize>=24||(row.renderedFontSize>=18.6667&&parseFloat(row.fontWeight)>=700)?3:4.5;
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
      }else if(e instanceof SVGElement&&/^url\(/.test(s.fill)){inks=[];row.pendingRaster=true;}
      else inks=[color(e instanceof SVGElement?s.fill:s.webkitTextFillColor)];
      let opacity=1;const opacityGroups=[];
      for(let p=e;p;p=p.parentElement){const value=Number(getComputedStyle(p).opacity);opacity*=value;if(value!==1)opacityGroups.unshift([p,value]);}
      window.learnContrastOpacityGroups[nodeIndex]=opacityGroups;
      row.inks=inks;
      row.requiresRaster=true;
      row.rasterGroup=e instanceof SVGElement?'svg:'+Array.from(document.querySelectorAll('svg')).indexOf(e.ownerSVGElement):'node:'+nodeIndex;
      const ratios=inks.flatMap(ink=>bg.colors.map(background=>({ratio:contrastRatio(over([...ink.slice(0,3),ink[3]*opacity],background),background),foreground:over([...ink.slice(0,3),ink[3]*opacity],background),background})));
      const worst=ratios.length?ratios.reduce((a,b)=>a.ratio<b.ratio?a:b):{};
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
module.exports={screenFontSize,accessibleControlName,nativeText,namedHorizontalScroller,activeContent,semanticSvgText,measureTextPaint,visible,targets,svgGeometry,capstone,rootLayout,contrastRatio,renderedContrast,themeState};
