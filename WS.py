from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title> Device specification</title>
    </head>
    <body> 
        <h1 align="center"> DEVICE SPECIFICATIONS 25017673 </h1>
        <table border="1" cellspacing="2" cellpadding="10">
            <tr>
                <th>S.NO. </th>
                <th>Device specification</th>
                <th> Description</th>
            </tr>
            <tr>
                <td>1</td>
                <td>Storage</td>
                <td>954GB</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Graphics card</td>
                <td>128GB</td>
            </tr>
            <tr>
                <td>3</td>
                <td>Installed RAM</td>
                <td>16.0GB</td>
            </tr>
            <tr>
                <td>4</td>
                <td>Processor</td>
                <td>Intel(R) Core(TM) Ultra 5 125H (1.20 GHz)</td>
            </tr>
            <tr>
                <td>5</td>
                <td>Product ID</td>
                <td>00342-42784-45915-AAOEM</td>
            </tr>
        </table>
    </body>
            

</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()