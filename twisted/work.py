from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor
from twisted.internet.defer import DeferredQueue

class MyServiceConnection(Protocol):

	def __init__(self, data_conn):
		self.data_conn = data_conn

	def connectionMade(self):
		print "Service Connection Made!"
		self.data_conn.startForwarding(self)

	def dataReceived(self, data):
		print "Got data over service connection: ", data
		self.data_conn.transport.write(data)


class MyCommandConnection(Protocol):

	def connectionMade(self):
		print "Command Connection Made!"

	def dataReceived(self, data):
		print "Got data over command connection: ", data

		# Start data connection if home tells you to
		if data == "startdataconnection":
			reactor.connectTCP("ash.campus.nd.edu", 42100, MyDataConnectionFactory())

class MyDataConnection(Protocol):

	def __init__(self):
		self.queue = DeferredQueue()
		self.service_conn = None

	def connectionMade(self):
		print "Data Connection Made!"
		# Create service connection
		reactor.connectTCP("student00.cse.nd.edu", 22, MyServiceConnectionFactory(self))

	def dataReceived(self, data):
		print "Got data over data connection: ", data
		self.queue.put(data)

	def startForwarding(self, service_conn):
		self.service_conn = service_conn
		self.queue.get().addCallback(self.forwardData)

	def forwardData(self, data):
		self.service_conn.transport.write(data)
		self.queue.get().addCallback(self.forwardData)


class MyServiceConnectionFactory(ClientFactory):

	def __init__(self, data_conn):
		self.myservconn = MyServiceConnection(data_conn)

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
