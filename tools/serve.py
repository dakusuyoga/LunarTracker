import os, sys, http.server, socketserver

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(root)

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):
        sys.stderr.write("%s\n" % (fmt % args))

    def end_headers(self):
        # Dev server: never let the browser cache stale JS/CSS.
        self.send_header("Cache-Control", "no-store, must-revalidate")
        super().end_headers()

port = int(os.environ.get("PORT", "8642"))
with socketserver.TCPServer(("127.0.0.1", port), Handler) as httpd:
    print("serving %s on http://127.0.0.1:%d" % (root, port), flush=True)
    httpd.serve_forever()
