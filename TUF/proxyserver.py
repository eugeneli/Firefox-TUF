import web
import tuf.interposition
from tuf.interposition import urllib2_tuf as urllib2

        
urls = (
   "http://aus3.mozilla.org/update/3/Firefox/24.0/20130910160258/Linux_x86_64-gcc3/en-US/release/Linux%202.6.32-358.23.2.el6.x86_64%20(GTK%202.18.9)/default/default/update.xml?force=1", "tufguy"
)
app = web.application(urls, globals())

class tufguy:        
    def GET(self, target):
	#Serve Firefox the update.xml
	return urllib2.urlopen("http://127.0.0.1:8080/repository/metadata/update.xml")
	#return "target is: {0}".format(target)
        #if not target: 
        #    return Http404Error()
        #else:
        #   return urllib2.urlopen(target)

if __name__ == "__main__":
    tuf.interposition.configure()
    app.run()
