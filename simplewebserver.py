from http.server import HTTPServer, BaseHTTPRequestHandler 
content = """ 
<!DOCTYPE html> 
<html> 
<head> 
<title>Simple Web Server</title> 
</head> 
<body> 
<h1 align="center">19AI414-Fundamentals of Web Application Development</h1> 
<h2>Execrise 1: Simple Web Server</h2> 
<pre>Status: Completed Successfully!!!!</pre> 
</body> 
</html> 
""" 
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleWebServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        content = "<html><body><h1>Hello, World!</h1></body></html>"
        self.wfile.write(content.encode('utf-8'))

server_address = ('', 8080)
httpd = HTTPServer(server_address, SimpleWebServer)
print("my webserver is running at http://localhost:8080")
httpd.serve_forever()