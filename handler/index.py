from http.server import BaseHTTPRequestHandler

from .map import fetch_map

class PlayerRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if (self.path.find('map')):
            fetch_map(self)
    
    def do_POST(self):
        print(self.path)
