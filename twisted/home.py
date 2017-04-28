from twisted.internet.protocol import Factory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor

class MyCommandConnection(Protocol):


	def connectionMade(self):
		print "Command Connection Made!"
		reactor.listenTCP(41100, MyClientConnectionFactory(self))
		#self.transport.write("startdataconnection")
		# Start listening on client port
		# reactor.listenTCP(41100, MyConnectionFactory())

	def dataReceived(self, data):
		print "Got data: ", data

class MyClientConnection(Protocol):

        def __init__(self,cmd_conn):
                self.cmd_conn = cmd_conn
        
        def connectionMade(self):
                print "Client Connection Made!"
                self.cmd_conn.transport.write("startdataconnection")
                reactor.listenTCP(42100, MyDataConnectionFactory(self))

        def dataReceived(self, data):
                print "Got data: ", data

class MyDataConnection(Protocol):

        def __init__(self,cli_conn):
                self.cli_conn = cli_conn
        
        def connectionMade(self):
                print "Data Connection Made!"
                #self.cmd_conn.transport.write("startdataconnection")
                #reactor.listenTCP(42100, MyDataConnectionFactory(self))

        def dataReceived(self, data):
                print "Got data: ", data

class MyCommandConnectionFactory(Factory):

		def __init__(self):
				self.mycmdconn = MyCommandConnection()

		def buildProtocol(self, addr):
				return self.mycmdconn

class MyClientConnectionFactory(Factory):

        def __init__(self, cmd_conn):
                self.mycliconn = MyClientConnection(cmd_conn)

        def buildProtocol(self, addr):
                return self.mycliconn

class MyDataConnectionFactory(Factory):

        def __init__(self, cli_conn):
                self.mydataconn = MyDataConnection(cli_conn)

        def buildProtocol(self, addr):
                return self.mydataconn

# Start listening on command port
reactor.listenTCP(40100, MyCommandConnectionFactory())

# Start listening on client port
#reactor.listenTCP(41100, MyClientConnectionFactory())

reactor.run()
