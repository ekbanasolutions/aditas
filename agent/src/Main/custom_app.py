import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# HTTPRequestHandler class
from socketserver import ThreadingMixIn

from custom_requests import request
from get_urls import all
from bigdata_logs.logger import getLoggingInstance
log = getLoggingInstance()

server_address = ''
final_urls = {}

class HTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        try:
            r = request()
            custom_headers = {
                'API-KEY': self.headers['API-KEY'],
            }
            r.set_headers(custom_headers)

            path = self.path
            if not path.endswith("/"):
                path = path + '/'

            if path in final_urls:
                callable_module = final_urls[path]
                result = callable_module()

                self.send_response(code=200)
                self.end_headers()
                self.wfile.write(bytes(result, 'utf-8'))
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(bytes("404 page not found\n", "utf-8"))
                return
        except Exception as e:
            log.error(e)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        r = request()
        custom_headers = {
            'API-KEY': self.headers['API-KEY'],
        }
        r.set_headers(custom_headers)
        r.set_data(post_data)

        path = self.path
        if not path.endswith("/"):
            path = path + '/'

        if path in final_urls:
            callable_module = final_urls[path]
            result = callable_module()

            self.send_response(code=200)
            self.end_headers()
            self.wfile.write(bytes(result, 'utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes("404 page not found\n", "utf-8"))
            return


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """ This class allows to handle requests in separated threads.
        No further content needed, don't touch this. """


def run(host, port):
    httpd = None
    try:
        global final_urls
        final_urls = all()
        server_address = (host, port)
        httpd = ThreadedHTTPServer(server_address, HTTPServer_RequestHandler)
        # httpd = HTTPServer(server_address, HTTPServer_RequestHandler)
        # print('Running on http://%s:%s/ (Press CTRL+C to quit)\n' % (host, port))
        log.info('Running on http://%s:%s/ \n' % (host, port))
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.socket.close()

