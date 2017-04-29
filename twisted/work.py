from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor

class MyServiceConnection(Protocol):

	def connectionMade(self):
		print "Service Connection Made!"

	def dataReceived(self, data):
		print "Got data over service connection: ", data


class MyCommandConnection(Protocol):

	def connectionMade(self):
		print "Command Connection Made!"

	def dataReceived(self, data):
		print "Got data over command connection: ", data

		# Start data connection if home tells you to
		if data == "startdataconnection":
			reactor.connectTCP("ash.campus.nd.edu", 42100, MyDataConnectionFactory())

class MyDataConnection(Protocol):

	def connectionMade(self):
		print "Data Connection Made!"
		# Create service connection
		reactor.connectTCP("student00.cse.nd.edu", 22, MyServiceConnectionFactory())

	def dataReceived(self, data):
		print "Got data over data connection: ", data

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

# Create command connection
reactor.connectTCP("ash.campus.nd.edu", 40100, MyCommandConnectionFactory())

reactor.run()
