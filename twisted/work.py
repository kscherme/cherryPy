from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor

class MyConnection(Protocol):

	def connectionMade(self):
		print "New Connection Made!"
		#self.transport.write("GET /movies/32 HTTP/1.0\r\n\r\n")

	def dataReceived(self, data):
		print "Got data: ", data

class MyConnectionFactory(ClientFactory):

	def __init__(self):
		self.myconn = MyConnection()

	def buildProtocol(self, addr):
		return self.myconn


# Create service connection
reactor.connectTCP("student00.cse.nd.edu", 22, MyConnectionFactory())

# Create command connection
reactor.connectTCP("ash.campus.nd.edu", 40100, MyConnectionFactory())

reactor.run()
