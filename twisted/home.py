from twisted.internet.protocol import Factory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor

class MyCommandConnection(Protocol):

	def connectionMade(self):
		print "Command Connection Made!"
		# self.transport.write("GET /movies/32 HTTP/1.0\r\n\r\n")
		# Start listening on client port
		# reactor.listenTCP(41100, MyConnectionFactory())

	def dataReceived(self, data):
		print "Got data: ", data

class MyClientConnection(Protocol):
        
        def connectionMade(self):
                print "Client Connection Made!"

        def dataReceived(self, data):
                print "Got data: ", data

class MyCommandConnectionFactory(Factory):

	def __init__(self, ):
		self.mycmdconn = MyCommandConnection()

	def buildProtocol(self, addr):
		return self.mycmdconn

class MyClientConnectionFactory(Factory):

        def __init__(self):
                self.mycliconn = MyClientConnection()

        def buildProtocol(self, addr):
                return self.mycliconn

# Start listening on command port
reactor.listenTCP(40100, MyCommandConnectionFactory(self))

# Start listening on client port
reactor.listenTCP(41100, MyClientConnectionFactory())

reactor.run()
