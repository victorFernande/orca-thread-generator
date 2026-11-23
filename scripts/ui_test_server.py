"""Isolated backend for browser checks; never imports models into OrcaSlicer."""
from __future__ import annotations
import importlib
import json
from pathlib import Path
import queue
import sys
import tempfile
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
PACKAGE = next((ROOT / "src").glob("*_studio")).name
SLUG = PACKAGE.split("_", 1)[0]
mod = importlib.import_module(PACKAGE + ".plugin_main")
private = tempfile.TemporaryDirectory(prefix="orca-ui-check-")
mod._resolve_storage_dir = lambda: Path(private.name)
mod._dispatch_files_to_plater = lambda *a, **kw: (False, "Isolated browser test: native transport disabled", None)
mod._open_folder_native = lambda *a, **kw: False
controller = getattr(mod, SLUG.title() + "StudioController")()
outbox = queue.Queue()
outboxes = {}

class Handler(BaseHTTPRequestHandler):
    def reply(self, value, kind="application/json"):
        data = (value if isinstance(value, str) else json.dumps(value)).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", kind + "; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        url = urlparse(self.path)
        query = parse_qs(url.query, keep_blank_values=True)
        if url.path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()
            return
        if url.path == "/messages":
            target = outboxes.get(query.get("client", [""])[0], outbox)
            messages = []
            while True:
                try:
                    messages.append(target.get_nowait())
                except queue.Empty:
                    break
            self.reply(messages)
            return
        mode = "dock" if "dock" in query else "page"
        client = uuid.uuid4().hex
        outboxes[client] = queue.Queue()
        # Let the controller initialize host preferences before applying the
        # explicit synthetic theme/language requested by this browser case.
        controller.build_initial_context(mode)
        params = controller.current_params() if SLUG == "box" else controller.current_params
        params.update(theme=query.get("theme", ["dark"])[0], lang=query.get("lang", [params["lang"]])[0])
        if SLUG == "box":
            controller.set_current_params(params)
        else:
            controller.set_current_params(params, history=False)
        context = controller.build_initial_context(mode)
        context.update(theme=params["theme"], lang=params["lang"])
        html = mod.get_studio_html(mode, context)
        shim = """<script>
window.__hostMessages=[];window.__sentMessages=[];
window.orca={onMessage:callback=>window.__hostCallback=callback,postMessage:payload=>{
window.__sentMessages.push(payload);return fetch('/message?mode=MODE&client=CLIENT',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)});}};
setInterval(async()=>{try{const response=await fetch('/messages?client=CLIENT');for(const m of await response.json()){
window.__hostMessages.push({type:m.type,lang:m.lang,language_request_id:m.language_request_id,warning:m.warning,ok:m.ok,meshes:m.meshes?.length,request_id:m.request_id,message:m.message,detail:m.detail,paths:m.paths,params:m.params});
if(window.__hostCallback)window.__hostCallback(m);else if(window.handleHostMessage)window.handleHostMessage(m);else window.dispatchEvent(new MessageEvent('message',{data:m}));
}}catch(error){console.error(error);}},150);
</script>""".replace("MODE", mode).replace("CLIENT", client)
        self.reply(html.replace("<head>", "<head>" + shim, 1), "text/html")

    def do_POST(self):
        url = urlparse(self.path)
        payload = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        mode = parse_qs(url.query).get("mode", ["page"])[0]
        target = outboxes.get(parse_qs(url.query).get("client", [""])[0], outbox)
        controller.handle_message(payload, target.put, mode)
        self.reply({"accepted": True})

    def log_message(self, *args):
        pass

if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    print(json.dumps({"url": "http://127.0.0.1:" + str(server.server_port), "slug": SLUG}), flush=True)
    try:
        server.serve_forever()
    finally:
        server.server_close()
        private.cleanup()
