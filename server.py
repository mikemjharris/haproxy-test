#!/usr/bin/env python2
from SimpleHTTPServer import SimpleHTTPRequestHandler
from BaseHTTPServer import HTTPServer

class MyRequestHandler(SimpleHTTPRequestHandler):
      protocol_version = "HTTP/1.1" 

server = HTTPServer(("127.0.0.1", 8000), MyRequestHandler)
server.serve_forever()

