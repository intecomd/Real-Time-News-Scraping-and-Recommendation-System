import pyjsonrpc
import json
import os
import sys

from bson.json_util import dumps

sys.path.append(os.path.join(os.path.dirname(__file__),'./','utils'))

import mongodb_client


SERVER_HOST = 'localhost'
SERVER_PORT = 4040

class RequestHandler(pyjsonrpc.HttpRequestHandler): 
   """ Test Method """
   @pyjsonrpc.rpcmethod
   def add(self, a , b):
    print "add is called with %d and %d" %(a,b)
    return a + b


   @pyjsonrpc.rpcmethod
   def getNews(self):
    db = mongodb_client.get_db()
    news = list(db['test'].find())
    return json.loads(dumps(news))

http_server = pyjsonrpc.ThreadingHttpServer(
   server_address = (SERVER_HOST, SERVER_PORT),
   RequestHandlerClass = RequestHandler
)

print "start Http server on %s:%d" % (SERVER_HOST, SERVER_PORT)
http_server.serve_forever()
