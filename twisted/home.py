from twisted.internet.protocol import Factory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor

class MyConnection(Protocol):

	def connectionMade(self):
		print "New Connection Made!"
		self.transport.write("GET /movies/32 HTTP/1.0\r\n\r\n")
		# Start listening on client port
		reactor.listenTCP(41100, MyConnectionFactory())

	def dataReceived(self, data):
		print "Got data: ", data

class MyConnectionFactory(Factory):

	def __init__(self):
		self.myconn = MyConnection()

	def buildProtocol(self, addr):
		return self.myconn

# Start listening on command port
reactor.listenTCP(40100, MyConnectionFactory())

# Start listen on client port
reactor.listenTCP(41100, MyConnectionFactory())

reactor.run()