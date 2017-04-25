from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor

class MyConnection(Protocol):

	def connectionMade(self):
		print "New Connection Made!"
		self.transport.write("GET /movies/32 HTTP/1.0\r\n\r\n")

	def dataReceived(self, data):
		print "Got data: ", data

class MyConnectionFactory(ClientFactory):

	def __init__(self):
		self.myconn = MyConnection()

	def buildProtocol(self, addr):
		return self.myconn

reactor.connectTCP("ash.campus.nd.edu", 40001, MyConnectionFactory())

reactor.run()