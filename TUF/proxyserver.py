import web
import tuf.interposition
from tuf.interposition import urllib2_tuf as urllib2

        
urls = (
    '/(.*)', 'tufguy'
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
