from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

import tuf
import tuf.interposition
from tuf.interposition import urllib2_tuf



class MyHandler(BaseHTTPRequestHandler):


    def do_GET(self):
        try:
            entire_url = "http://mirror1.poly.edu" + self.path

            print entire_url
            f = urllib2_tuf.urlopen(entire_url)

            if self.path.endswith(".xml") or self.path.endswith(".xml?force=1"):
                self.send_response(200)
                self.send_header('Content-type',  'text/xml')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return

            if self.path.endswith(".mar"):
                chunk = f.read()
#                import pdb; pdb.set_trace()
                self.send_response(200)
                self.send_header('Content-Type',  'application/octet-stream')
                self.send_header('Accept-Ranges', 'bytes')
                self.send_header('Content-Length', len(chunk))
                self.end_headers()

                print len(chunk)
                self.wfile.write(chunk)
#                self.wfile.close()
                f.close()
                return



        except IOError:
            self.send_error( 404 )


def main():
     try:
        server = HTTPServer(('', 8080), MyHandler)
        print 'started httpserver.....\n'
        server.serve_forever()

     except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()


if __name__ == '__main__':
    tuf.interposition.configure()
    main()      
