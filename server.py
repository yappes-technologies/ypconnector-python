from http.server import BaseHTTPRequestHandler, HTTPServer

PORT_NUMBER = 8080

getResponseObj = {"name": "getUser", "id": "1025", "age": "22"}
addResponseObj = {"name": "addUser", "id": "1026", "age": "10"}
updateResponseObj = {"name": "updateUser", "id": "1025", "age": "22"}
deleteResponseObj={"name": "deleteUser", "id": "1025", "age": "22"}
patchResponseObj={"name": "patchUser", "id": "1025", "age": "22"}
class httpRequests(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/getdata":
            print(getResponseObj)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(str(getResponseObj).encode("utf-8"))

    def do_POST(self):
        if self.path == "/postdata":
            print(addResponseObj)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(str(addResponseObj).encode("utf-8"))

    def do_PUT(self):
        if self.path == "/putdata":
            print(updateResponseObj)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(str(updateResponseObj).encode("utf-8"))

    def do_DELETE(self):
        if self.path == "/deletedata":
            print(updateResponseObj)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(str(deleteResponseObj).encode("utf-8"))
    
    def do_PATCH(self):
        if self.path == "/patchdata":
            print(updateResponseObj)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(str(patchResponseObj).encode("utf-8"))

        
try:
    server = HTTPServer(("", PORT_NUMBER), httpRequests)
    print("Listening to port ", PORT_NUMBER)

    server.serve_forever()

except KeyboardInterrupt:
    print("^C received, shutting down the web server")
    server.socket.close()

