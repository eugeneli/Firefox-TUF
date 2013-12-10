#interpose.py

import time
import mimetypes
import tuf.interposition

from libmproxy.flow import Response
from netlib.odict import ODictCaseless
from tuf.interposition import urllib2_tuf

def start(context):
    context.log("start")
    tuf.interposition.configure()
    
# - skip interposition and use a lower level
# - handle errors
# - handle https

def request(context, flow):

    context.log("request")
    url = flow.request.get_url()
    url = "http://mirror1.poly.edu" + url[len("http://127.0.0.1:8080"):]

    if flow.request.path.endswith('.xml?force=1'):
       url = url[:-8]

    content_type, content_encoding = mimetypes.guess_type(url)

    if not content_type:
      if flow.request.path.endswith('.mar'):
        content_type = "application/octet-stream"
      else:
        content_type = "text/html"
    context.log("before")
    context.log(url)
    document = urllib2_tuf.urlopen(url)
    context.log("after")

    content = document.read()
    response = Response(flow.request,

                       [1,1],      # HTTP protocol version 1.1

                       200,        # HTTP response status code

                       "OK",       # HTTP response status message

                       ODictCaseless([["Content-Type", content_type]]),

                       content,    # HTTP response body

                       None)       # certificate

    flow.request.reply(response)
