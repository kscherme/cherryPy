from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor

class MyServiceConnection(Protocol):

	def connectionMade(self):
		print "Service Connection Made!"
		#self.transport.write("GET /movies/32 HTTP/1.0\r\n\r\n")

	def dataReceived(self, data):
		print "Got data: ", data


class MyCommandConnection(Protocol):

	def connectionMade(self):
		print "Command Connection Made!"
		#self.transport.write("GET /movies/32 HTTP/1.0\r\n\r\n")

	def dataReceived(self, data):
		print "Got data: ", data
		if data == "startdataconnection":
			reactor.connectTCP("ash.campus.nd.edu", 42100, MyDataConnectionFactory())

class MyDataConnection(Protocol):

	def connectionMade(self):
		print "Data Connection Made!"
		#self.transport.write("GET /movies/32 HTTP/1.0\r\n\r\n")

	def dataReceived(self, data):
		print "Got data: ", data

class MyServiceConnectionFactory(ClientFactory):

	def __init__(self):
		self.myservconn = MyServiceConnection()

	def buildProtocol(self, addr):
		return self.myservconn

class MyCommandConnectionFactory(ClientFactory):

	def __init__(self):
		self.mycmdconn = MyCommandConnection()

	def buildProtocol(self, addr):
		return self.mycmdconn

class MyDataConnectionFactory(ClientFactory):

	def __init__(self):
		self.mydataconn = MyDataConnection()

	def buildProtocol(self, addr):
		return self.mydataconn

# Create service connection
reactor.connectTCP("student00.cse.nd.edu", 22, MyServiceConnectionFactory())

# Create command connection
reactor.connectTCP("ash.campus.nd.edu", 40100, MyCommandConnectionFactory())

reactor.run()
