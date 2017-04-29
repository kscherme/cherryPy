from twisted.internet.protocol import Factory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor

class MyCommandConnection(Protocol):


		def connectionMade(self):
				print "Command Connection Made!"

				# Listen on the Client Connection
				reactor.listenTCP(41100, MyClientConnectionFactory(self))

		def dataReceived(self, data):
				print "Got data over command connection: ", data

class MyClientConnection(Protocol):

        def __init__(self,cmd_conn):
                self.cmd_conn = cmd_conn
        
        def connectionMade(self):
                print "Client Connection Made!"

                # Through command connection tell work to start data connection
                self.cmd_conn.transport.write("startdataconnection")
                reactor.listenTCP(42100, MyDataConnectionFactory(self))

        def dataReceived(self, data):
                print "Got data over client connection: ", data

class MyDataConnection(Protocol):

        def __init__(self,cli_conn):
                self.cli_conn = cli_conn
        
        def connectionMade(self):
                print "Data Connection Made!"

        def dataReceived(self, data):
                print "Got data over data connection: ", data

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

reactor.run()
