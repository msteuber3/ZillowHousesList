import time
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import requests

HOST = "10.184.187.249"
PORT = 8000
username = 'myusername'
password = 'mypassword'

response = requests.get("https://realpython.com", headers={username: password})
print(response.status_code)


class HTTP(BaseHTTPRequestHandler):
    def do_GET(self):

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>Get fucked</h1></body></html>", "utf-8"))
        url = "https://zillow-working-api.p.rapidapi.com/client/byaddress"

        querystring = {"propertyaddress": "10945 MCVINE AVE LOS ANGELES CA 91040"}

        headers = {
            "X-RapidAPI-Key": "a21e225447mshf488525040b1036p1a40ffjsnb99943c1a50a",
            "X-RapidAPI-Host": "zillow-working-api.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        self.wfile.write(bytes(json.dumps(response.json()), "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes('{"time:" "' + date + '"}', "utf-8"))


server = HTTPServer((HOST, PORT), HTTP)
print("Server running")
server.serve_forever()
server.server_close()
print("Server stopped")