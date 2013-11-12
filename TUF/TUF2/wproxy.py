import web
import tuf.interposition
from tuf.interposition import urllib2_tuf as urllib2

urls = (
   "http://aux3.mozilla.org/(.*)/update.xml?force=1", "updatexml"
   "http://download.mozilla.org/(.*)/firefox-25.0-partial-24.0(.*)force=1", "marfile"
)

app = web.application(urls,globals())

class updatexml:
   def GET(self):
      return urllib2.urlopen("http://redowl.net:8001/targets/update.xml")

class marfile:
   def GET(self):
      return urllib2.urlopen("http://redowl.net:8001/targets/firefox-24.0-25.0.partial.mar")

if __name__=="__main__":
   tuf.interposition.configure()
   app.run()

