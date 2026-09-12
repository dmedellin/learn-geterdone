'use strict';
const {normalizeHtml}=require('../scripts/canvas_normalize'),protocol=require('./mutation_protocol');
const fail=assertion=>{throw Object.assign(Error(assertion),{assertion,code:'LEARN_CANVAS_SEMANTIC'})};
const base='<html><head><script>window.initLab=()=>{};</script></head><body><canvas id="chart"></canvas><button onclick="window.initLab()">Run</button></body></html>';
const cases=[
 ['native event',base.replace('<body>','<body onclick="ctx.fillText(\'Raw\',1,2)">'),'uncontracted native canvas text source'],
 ['native URL',base.replace('<body>','<body><a href="javascript:ctx.strokeText(\'Raw\',1,2)">Run</a>'),'uncontracted native canvas text source'],
 ['encoded native',base.replace('<body>','<body onclick="ctx.&#102;illText(\'Raw\',1,2)">'),'uncontracted native canvas text source'],
 ['no static canvas',base.replace('<canvas id="chart"></canvas>','').replace('<body>','<body onclick="ctx.fillText(\'Raw\',1,2)">'),'uncontracted native canvas text source'],
 ['unknown script owner',base.replace('<script>','<script type="application/unknown">'),'unsupported script classification in canvas source boundary'],
 ['nested source owner',base.replace('<body>','<body><iframe srcdoc="text"></iframe>'),'unsupported nested executable HTML owner']
];
try{const normal=normalizeHtml(base,'fixture/index.html');if(normalizeHtml(normal,'fixture/index.html')!==normal)fail('HTML maintenance boundary: idempotent authored handler');for(const [name,source,expected]of cases){let observed=null;try{normalizeHtml(source,'fixture/index.html')}catch(e){if(e.code!=='LEARN_CANVAS_SEMANTIC')throw e;observed=e.assertion}if(observed!==expected)fail('HTML maintenance boundary: '+name);}console.log('7/7 HTML canvas maintenance fixtures passed');}catch(e){if(e.code==='LEARN_CANVAS_SEMANTIC')protocol.semantic(e.assertion);else protocol.setup(e);process.exitCode=1}
