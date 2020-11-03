#
# sa https://qiita.com/__init__/items/5c89fa5b37b8c5ed32a4
#

import http.server
import socketserver

HOST = '127.0.0.1'
PORT = 8000

with socketserver.TCPServer((HOST, PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()
