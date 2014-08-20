from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from redisserver import app

http_server = HTTPServer(WSGIContainer(app))
http_server.bind(6223)
http_server.start(0)
IOLoop.instance().start()
