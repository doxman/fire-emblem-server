from http.server import BaseHTTPRequestHandler

class PlayerRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
    
    def do_POST(self):
        print(self.path)
