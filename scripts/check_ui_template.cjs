/* Development-only browser checks. No network assets or native OrcaSlicer IPC. */
const fs = require('fs');
const path = require('path');
const os = require('os');
const { spawn } = require('child_process');
const { chromium } = require(process.env.ORCA_PLAYWRIGHT_MODULE || 'playwright');
const root = path.resolve(__dirname, '..');
const output = process.env.ORCA_UI_OUTPUT || fs.mkdtempSync(path.join(os.tmpdir(), 'orca-ui-evidence-'));
fs.mkdirSync(output, { recursive: true });
const fixture = JSON.parse(fs.readFileSync(path.join(root, 'tests/fixtures/vase_template_metrics.json'), 'utf8'));
const selectors = {header:'.studio-header',workspace:'.studio-workspace',left:'.col-left',right:'.col-right',brand:'.brand-logo',title:'.brand-title',card:'.studio-card',gallery:'.presets-grid',preset:'.preset-card',number:'.ctrl-num',slider:'.orca-slider',toggle:'.toggle-switch',hero:'.col-right .btn-hero',footer:'.col-right .action-footer',view:'.viewport-col',cameraBar:'.vp-cam-bar',cutBar:'.vp-cut-bar'};
function startServer() {
  const child=spawn(process.env.ORCA_TEST_PYTHON || 'python',['-B',path.join(__dirname,'ui_test_server.py')],{cwd:root,stdio:['ignore','pipe','pipe']});
  let logs='';child.stderr.on('data',chunk=>{logs+=chunk.toString();});
  const ready=new Promise((resolve,reject)=>{
    const timer=setTimeout(()=>reject(Error('UI server startup timed out: '+logs)),30000);
    let buffered='';child.stdout.on('data',chunk=>{
      buffered+=chunk.toString();const lines=buffered.split(/\r?\n/);buffered=lines.pop();
      for(const line of lines){try{const value=JSON.parse(line);if(value.url){clearTimeout(timer);resolve(value);}}catch{}}
    });
    child.on('error',error=>{clearTimeout(timer);reject(error);});
    child.on('exit',code=>{clearTimeout(timer);reject(Error('UI server exited '+code+': '+logs));});
  });
  return {child,ready,logs:()=>logs};
}
async function measure(page,reference) {
  return page.evaluate(({selectors,reference})=>{
    const html=getComputedStyle(document.documentElement),body=getComputedStyle(document.body),actual={tokens:{},body:{},components:{},rects:{}};
    for(const key of Object.keys(reference.tokens))actual.tokens[key]=html.getPropertyValue(key).trim();
    for(const key of Object.keys(reference.body))actual.body[key]=body[key];
    for(const [name,selector] of Object.entries(selectors)){
      const el=document.querySelector(selector);if(!el){actual.components[name]=null;continue;}
      const style=getComputedStyle(el),r=el.getBoundingClientRect();
      actual.components[name]=Object.fromEntries(Object.keys(reference.components[name]||{}).map(key=>[key,style[key]]));
      actual.rects[name]={x:r.x,y:r.y,width:r.width,height:r.height,display:style.display};
    }
    actual.overflow=document.documentElement.scrollWidth>innerWidth;
    actual.occludedCameraButtons=[...document.querySelectorAll('.vp-cam-bar button')].filter(button=>{
      const r=button.getBoundingClientRect();return r.width>0&&r.height>0&&!button.contains(document.elementFromPoint(r.x+r.width/2,r.y+r.height/2));
    }).map(button=>button.textContent.trim());
    return actual;
  },{selectors,reference});
}
function compare(actual,expected) {
  const issues=[];
  for(const group of ['tokens','body'])for(const [key,value] of Object.entries(expected[group]))if(actual[group][key]!==value)issues.push(`${group}.${key}: ${actual[group][key]} != ${value}`);
  for(const [component,props] of Object.entries(expected.components)){
    if(!props||!Object.keys(props).length)continue;
    if(!actual.components[component]){issues.push(`missing ${component}`);continue;}
    for(const [key,value] of Object.entries(props))if(actual.components[component][key]!==value)issues.push(`${component}.${key}: ${actual.components[component][key]} != ${value}`);
  }
  if(!expected.dock){
    for(const name of ['header','workspace','left','right'])for(const key of ['x','y','width','height'])if(Math.abs((actual.rects[name]?.[key]??Infinity)-expected.rects[name][key])>1)issues.push(`${name}.${key} differs by more than 1px`);
    const camera=actual.rects.cameraBar,cut=actual.rects.cutBar;
    if(camera&&cut&&camera.display!=='none'&&camera.y+camera.height>cut.y+0.5)issues.push('camera controls overlap the section toolbar');
  }else if(Math.abs((actual.rects.view?.height??0)-245)>1)issues.push('dock preview height differs from 245px');
  if(actual.overflow)issues.push('horizontal document overflow');
  if(!expected.dock&&actual.occludedCameraButtons.length)issues.push('camera buttons occluded: '+actual.occludedCameraButtons.join(', '));
  return issues;
}
const geometryCount=page=>page.evaluate(()=>window.__hostMessages.filter(m=>['geometry','preview_result'].includes(m.type)&&m.meshes>0).length);
async function waitGeometry(page,before=0,expected={}) {
  await page.waitForFunction(({before,expected})=>window.__browserErrors?.length||window.__hostMessages.filter(m=>['geometry','preview_result'].includes(m.type)&&m.meshes>0).slice(before).some(m=>Object.entries(expected).every(([key,value])=>m.params?.[key]===value)),{before,expected},{timeout:180000});
  const failures=await page.evaluate(()=>window.__browserErrors||[]);if(failures.length)throw Error(failures.join('\n'));
}
async function clickAction(page,name) {
  const actions={send:'send_to_plater',stl:'export_stl',three:'export_3mf','3mf':'export_3mf',folder:'open_exports'};
  const buttons=page.locator(`[data-action="${actions[name]||name}"]`);const n=await buttons.count();
  for(let i=0;i<n;i++)if(await buttons.nth(i).isVisible()){await buttons.nth(i).click();return;}
  const aliases={send:'#send',stl:'#stl',three:'#three, #mf','3mf':'#three, #mf',folder:'#folder'};
  await page.locator(aliases[name]||'#'+name).first().click();
}
async function smoke(page,slug,url,passed) {
  await page.goto(url+'/?theme=dark');await waitGeometry(page);passed.push('Python mesh preview');
  let n=await geometryCount(page);await page.locator('#language').selectOption('en');
  await page.waitForFunction(()=>document.documentElement.lang==='en');passed.push('PT/EN');
  if(slug==='thread'&&(await geometryCount(page))!==n)throw Error('Language change regenerated mesh');
  n=await geometryCount(page);await page.locator('#theme, #btn-theme').first().click();
  await page.waitForFunction(()=>document.documentElement.dataset.theme==='light');passed.push('Light/dark');
  if(slug==='thread')await waitGeometry(page,n,{theme:'light'});
  const key=slug==='box'?'width_x':'height';
  const dimension=slug==='box'?page.locator('input[type="number"][data-p="width_x"], input[type="number"][data-key="width_x"]').first():page.locator('input[type="number"][data-key="height"]').first();
  const original=Number(await dimension.inputValue()),before=await geometryCount(page);
  await dimension.fill(String(original+2));await dimension.press('Tab');await waitGeometry(page,before,{[key]:original+2});passed.push('Dimension change');
  n=await geometryCount(page);await page.locator('#undo, #btn-undo').first().click();await waitGeometry(page,n,{[key]:original});
  if(Number(await dimension.inputValue())!==original)throw Error('Undo did not restore dimension');passed.push('Undo');
  n=await geometryCount(page);await page.locator('#redo, #btn-redo').first().click();await waitGeometry(page,n,{[key]:original+2});
  if(Number(await dimension.inputValue())!==original+2)throw Error('Redo did not restore edited dimension');passed.push('Redo');
  if(slug==='thread'){
    n=await geometryCount(page);await dimension.fill(String(original+4));await dimension.press('Tab');await page.locator('#undo, #btn-undo').first().click();
    await waitGeometry(page,n,{[key]:original+2});
    if(Number(await dimension.inputValue())!==original+2)throw Error('Undo lost the pending numeric edit');passed.push('Undo preserves a pending debounced edit');
  }
  const actionBefore=await page.evaluate(()=>window.__hostMessages.length);
  await clickAction(page,'3mf');
  await page.waitForFunction(before=>window.__hostMessages.slice(before).some(m=>m.type==='action_result'&&m.ok===true),actionBefore,{timeout:180000});passed.push('Real isolated 3MF export');
  const sentBefore=await page.evaluate(()=>window.__hostMessages.length);
  await clickAction(page,'send');
  await page.waitForFunction(before=>window.__hostMessages.slice(before).some(m=>m.type==='action_result'&&m.ok===false&&m.detail?.includes('native transport disabled')),sentBefore,{timeout:180000});passed.push('No false success when native transport fails');
  n=await geometryCount(page);await page.locator('#randomize, #btn-randomize').first().click();await waitGeometry(page,n);passed.push('Validated Surprise');
  await page.goto(url+'/?theme=dark&dock');await waitGeometry(page);
  for(const tab of ['shape','textures','print','presets']){
    const button=page.locator(`.dock-tab-btn[data-tab="${tab}"]`);await button.click();
    const footer=page.locator('.dock-global-footer');if(!(await footer.isVisible()))throw Error('Dock footer hidden on '+tab);
    if(!(await page.locator('#gl-canvas').isVisible()))throw Error('Dock preview hidden on '+tab);
  }
  passed.push('All dock sections keep preview and export visible');
  const dockBefore=await page.evaluate(()=>window.__hostMessages.length);
  await clickAction(page,'3mf');
  await page.waitForFunction(before=>window.__hostMessages.slice(before).some(m=>m.type==='action_result'&&m.ok===true),dockBefore,{timeout:180000});passed.push('Dock 3MF export binding');
  return passed;
}
async function featureChecks(page,slug,url,passed){
  await page.goto(url+'/?theme=light');await waitGeometry(page);
  if(slug==='thread'){
    let n=await geometryCount(page);await page.locator('.preset-card[data-preset-id="m12"]').click();await waitGeometry(page,n,{module:'bolt_nut_knob',nominal_dia:12});
    await page.locator('[data-cam="fit"]').click();
    await page.screenshot({path:path.join(output,'thread-m12-fit.png')});passed.push('M12 preset and complete camera fit');
    n=await geometryCount(page);await page.locator('select[data-key="starts"]').selectOption('3');await waitGeometry(page,n,{starts:3,lead:5.25});passed.push('Three-start lead');
    n=await geometryCount(page);await page.locator('select[data-key="hand"]').selectOption('left');await waitGeometry(page,n,{hand:'left'});passed.push('Left-hand thread');
    n=await geometryCount(page);await page.locator('#target').selectOption('calibration');await waitGeometry(page,n,{export_target:'calibration'});
    const rings=await page.evaluate(()=>window.__hostMessages.filter(m=>m.type==='geometry').at(-1).meshes);if(rings!==3)throw Error('Expected three calibration rings');passed.push('Three-ring calibration preview');
    await page.screenshot({path:path.join(output,'thread-calibration-fit.png')});
    const before=await page.evaluate(()=>window.__hostMessages.length);
    await page.locator('.preset-card[data-preset-id="mason86"]').click();
    await page.waitForFunction(before=>window.__hostMessages.slice(before).some(m=>m.type==='geometry'&&m.params?.standard==='mason_86'&&m.meshes===0&&m.warning),before,{timeout:30000});
    const beforeRandom=await page.evaluate(()=>window.__hostMessages.length);await page.locator('#randomize, #btn-randomize').first().click();
    await page.waitForFunction(before=>window.__hostMessages.slice(before).some(m=>m.type==='geometry'&&m.params?.standard==='mason_86'&&m.params?.measurements_confirmed===false&&m.meshes===0),beforeRandom,{timeout:30000});passed.push('Experimental Mason 86 stays blocked after Surprise');
  }else{
    let n=await geometryCount(page);await page.locator('.preset-card').filter({hasText:'Mini'}).click();await waitGeometry(page,n,{width_x:45,depth_y:35});passed.push('Preset gallery changes real box geometry');
    n=await geometryCount(page);await page.locator('#target').selectOption('fit_test_kit');await waitGeometry(page,n,{export_target:'fit_test_kit'});
    const parts=await page.evaluate(()=>window.__hostMessages.filter(m=>m.type==='preview_result').at(-1).meshes);if(parts!==3)throw Error('Expected the three-part Box fit kit preview');passed.push('Box fit-kit preview reflects export target');
    await page.screenshot({path:path.join(output,'box-calibration-fit.png')});
  }
}
async function nativeStyleChecks(page,slug,url,passed){
  for(const theme of ['light','dark']){
    await page.goto(url+'/?theme='+theme);await waitGeometry(page);
    const toggle=page.locator('#theme, #btn-theme').first();
    // Establish a manual preference before testing a conflicting host theme.
    await toggle.click();await toggle.click();
    await page.waitForFunction(theme=>document.documentElement.dataset.theme===theme,theme);
    await page.addStyleTag({content:':root{--orca-bg:#f0f0f0;--orca-fg:#333;--orca-border:#ddd;--orca-accent:#e00000;--orca-accent-fg:#fff;--orca-font:"Segoe UI",sans-serif;}html,body{background:var(--orca-bg);color:var(--orca-fg);font-family:var(--orca-font);font-size:13px;line-height:normal;}button{font:inherit;color:var(--orca-accent-fg);background:var(--orca-accent);border:1px solid var(--orca-accent);padding:5px 14px;}input,select,textarea{font:inherit;color:var(--orca-fg);background:var(--orca-bg);border:1px solid var(--orca-border);padding:4px 8px;}'});
    await page.evaluate(()=>new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve))));
    const state=await page.evaluate(()=>{
      const body=getComputedStyle(document.body),title=getComputedStyle(document.querySelector('.brand-title')),slider=getComputedStyle(document.querySelector('.orca-slider'));
      return {theme:document.documentElement.dataset.theme,color:body.color,title:title.color,font:body.fontSize,line:body.lineHeight,accent:getComputedStyle(document.documentElement).getPropertyValue('--orca-accent').trim(),border:slider.borderTopWidth,padding:slider.padding,height:slider.height};
    });
    const color=theme==='light'?'rgb(28, 34, 43)':'rgb(238, 242, 246)',accent=theme==='light'?'#00897b':'#00a896';
    if(state.theme!==theme||state.color!==color||state.title!==color||state.font!=='12.5px'||state.line!=='17.5px'||state.accent!==accent||state.border!=='0px'||state.padding!=='0px'||state.height!=='5px')throw Error('Late native host CSS changed studio '+JSON.stringify(state));
    await page.screenshot({path:path.join(output,`${slug}-native-host-${theme}.png`)});
    passed.push('Late native host defaults preserve '+theme+' template');
  }
}
(async()=>{
  const server=startServer();let browser;const results=[],errors=[];
  try{
    const {url,slug}=await server.ready;
    const options={headless:true,args:['--use-angle=swiftshader','--enable-webgl','--ignore-gpu-blocklist','--enable-unsafe-swiftshader']};
    if(process.env.ORCA_CHROMIUM_PATH)options.executablePath=process.env.ORCA_CHROMIUM_PATH;
    browser=await chromium.launch(options);
    for(const sample of (process.argv.includes('--smoke-only')?[]:fixture.samples)){
      const page=await browser.newPage({viewport:{width:sample.width,height:sample.height},deviceScaleFactor:sample.scale});
      await page.addInitScript(()=>{window.__browserErrors=[];window.addEventListener('error',event=>window.__browserErrors.push(event.error?.stack||event.message));});
      const pageErrors=[];page.on('pageerror',error=>pageErrors.push(String(error)));
      page.on('console',message=>{if(message.type()==='error')pageErrors.push(message.text());});
      await page.route('**/*',route=>new URL(route.request().url()).origin===url?route.continue():route.abort());
      await page.goto(`${url}/?theme=${sample.theme}${sample.dock?'&dock':''}`);
      try{await waitGeometry(page);}catch(error){
        await page.screenshot({path:path.join(output,'layout-failure.png')});
        fs.writeFileSync(path.join(output,'layout-failure.json'),JSON.stringify({sample:sample.name,theme:sample.theme,error:String(error),pageErrors,messages:await page.evaluate(()=>window.__hostMessages),body:await page.locator('body').innerText()},null,2));
        throw error;
      }
      await page.evaluate(()=>document.fonts.ready);
      const glState=await page.evaluate(()=>{const gl=document.querySelector('#gl-canvas')?.getContext('webgl2');if(!gl||gl.isContextLost())return false;const program=gl.getParameter(gl.CURRENT_PROGRAM);return !!program&&gl.getProgramParameter(program,gl.LINK_STATUS);});
      if(!glState)pageErrors.push('WebGL2 context/program unavailable or lost');
      const actual=await measure(page,sample),issues=compare(actual,sample);
      await page.screenshot({path:path.join(output,`${slug}-${sample.name}-${sample.theme}.png`),animations:'disabled'});
      results.push({name:sample.name,theme:sample.theme,actual,issues,pageErrors});
      console.log(`${sample.name}/${sample.theme}: ${issues.length+pageErrors.length} issues`);
      await page.close();
    }
    const page=await browser.newPage({viewport:{width:1580,height:1090}});page.on('pageerror',e=>errors.push(String(e)));
    await page.addInitScript(()=>{window.__browserErrors=[];window.addEventListener('error',event=>window.__browserErrors.push(event.error?.stack||event.message));});
    const interactions=[];
    try{await smoke(page,slug,url,interactions);await nativeStyleChecks(page,slug,url,interactions);await featureChecks(page,slug,url,interactions);}catch(error){errors.push(String(error));await page.screenshot({path:path.join(output,'interaction-failure.png')});}
    await page.close();
    const report={reference:fixture.reference,slug,results,interactions,errors,nativeApplicationTest:false};
    fs.writeFileSync(path.join(output,process.argv.includes('--smoke-only')?'interaction-report.json':'report.json'),JSON.stringify(report,null,2)+'\n');
    console.log(JSON.stringify({output,interactions,errors,layoutIssues:results.reduce((n,r)=>n+r.issues.length+r.pageErrors.length,0)},null,2));
    if(errors.length||results.some(r=>r.issues.length||r.pageErrors.length))process.exitCode=1;
  }finally{if(browser)await browser.close();server.child.kill();}
})().catch(error=>{console.error(error);process.exitCode=1;});
