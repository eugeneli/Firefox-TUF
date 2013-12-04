from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

import time



class MyHandler(BaseHTTPRequestHandler):


    def do_GET(self):
#        try:
            entire_url = "http://mirror1.poly.edu" + self.path

            print entire_url

            if self.path.endswith(".xml") or self.path.endswith(".xml?force=1"):
                self.send_response(200)
                self.send_header('Content-type',  'text/xml')
                self.end_headers()
                crap ="jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj"
                for i in range(0,10):
                  crap = crap + crap
                  
                while 1:
                   self.wfile.write(crap)
                return

            if self.path.endswith(".mar"):
                f_mar = open("complete.mar", "r+b")
                print "opened complete"
                chunk = f_mar.read()
                final_chunk = chunk + chunk + chunk + chunk + chunk + chunk+ chunk + chunk + chunk + chunk
                print "read chunk"
                f_mar.close()

#                import pdb; pdb.set_trace()
                self.send_response(200)
                self.send_header('Content-Type',  'application/octet-stream')
                self.send_header('Accept-Ranges', 'bytes')
                self.send_header('Content-Length', len(final_chunk))
                self.end_headers()

#                print len(chunk)
#               n = 100
#                while n:
                print "at chunk write"
                self.wfile.write(final_chunk)
                print " chunk written "
 #                  time.sleep(1)                   
#                self.wfile.close()
#                  n = n-1

                return



#        except IOError:
#            print "at error"
#            self.send_error( 404 )


def main():
     try:
        server = HTTPServer(('', 8080), MyHandler)
        print 'started httpserver.....\n'
        server.serve_forever()

     except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()


if __name__ == '__main__':
    main()      
