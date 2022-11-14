import http.server
import os
import logging
import http.server as server
import socket
 
import socketserver
 
import webbrowser
 
import pyqrcode
from pyqrcode import QRCode
import json

import png
# assigning the appropriate port value
PORT = 8000
# this finds the name of the computer user
os.environ['USERPROFILE']
desktop = os.path.abspath(os.getcwd())
os.chdir(desktop)

hostname = socket.gethostname()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(PORT)

link = IP
url = pyqrcode.create(link)
url.svg("myqr.svg", scale=8)


class HTTPRequestHandler(server.SimpleHTTPRequestHandler):

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin','*')
        server.SimpleHTTPRequestHandler.end_headers(self)

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        data=[]
        with open(self.path[2:],"r") as f:
            lines=f.readlines()
            for line in lines:
                data.append(int(line.rstrip()))

        self.wfile.write(bytes(json.dumps(data),'utf-8'))


    def do_PUT(self):
        """Save a file following a HTTP PUT request"""
        filename = os.path.basename(self.path)


        file_length = int(self.headers['Content-Length'])
        data=[]
        with open(filename,'r') as f:
            data=f.readlines()
            if (len(data)>=100):
                data=data[20:]
        
        # data+=[self.rfile.read(file_length)]
        with open(filename,"w") as f:
            for i in data:
                f.write(i)
        with open(filename, 'ab') as output_file:
            output_file.write(self.rfile.read(file_length))

        self.send_response(201, 'Created')
        self.end_headers()
        reply_body = 'Saved "%s"\n' % filename
        self.wfile.write(reply_body.encode('utf-8'))

    

with socketserver.TCPServer(("", PORT), HTTPRequestHandler) as httpd:
    print("serving at port", PORT)
    print("Type this in your Browser", IP)
    print("or Use the QRCode")
    httpd.serve_forever()