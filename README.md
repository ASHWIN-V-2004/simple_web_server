# EX01 Developing a Simple Webserver

# Date:15-10-2025
# AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

# DESIGN STEPS:
## Step 1:
HTML content creation.

## Step 2:
Design of webserver workflow.

## Step 3:
Implementation using Python code.

## Step 4:
Serving the HTML pages.

## Step 5:
Testing the webserver.

# PROGRAM:
```
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
```

# OUTPUT:
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/21765f84-01ad-41e5-9bf8-85cd3a196e27" />


# RESULT:
The program for implementing simple webserver is executed successfully.
