import web
import tuf.interposition
from tuf.interposition import urllib2_tuf as urllib2

urls = (
   "http://aus3.mozilla.org/update/3/Firefox/24.0/20130910160258/Linux_x86_64-gcc3/en-US/release/Linux%202.6.32-358.23.2.el6.x86_64%20(GTK%202.18.9)/default/default/update.xml?force=1", "updatexml"
   "http://download.mozilla.org/?product=firefox-25.0-complete&os=linux64&lang=en-US&force=1", "complete"
   "http://download.mozilla.org/?product=firefox-25.0-partial-24.0&os=linux64&lang=en-US&force=1", "partial"
)

app = web.application(urls,globals())

class updatexml:
   def GET(self):
      return urllib2.urlopen("http://redowl.net:8001/targets/update.xml")

class complete:
   def GET(self):
      return urllib2.urlopen("http://redowl.net:8001/targets/firefox-25.0.complete.mar")

class partial:
   def GET(self):
      return urllib2.urlopen("http://redowl.net:8001/targets/firefox-24.0-25.0.partial.mar")

if __name__=="__main__":
   tuf.interposition.configure()
   app.run()
