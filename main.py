# main.py
# Katie Schermerhorn

import _movie_database.py
import cherrypy
from reset import ResetController

def start_service(mdb):

	resetController = ResetController(mdb)

	dispatcher = cherrypy.dispatch.RoutesDispatcher()

	dispatcher.connect('reset', '/reset/', controller=resetController, action = 'PUT', conditions=dict(method=['PUT']))

	conf = { 'global' 	: {'server.socket_host': 'ash.campus.nd.edu',
							'server.socket_port': 40001,},
			 '/'		: {'request.dispatch': dispatcher,} }

	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config=conf)
	cherrypy.quickstart(app)

#create movieDBobject
if __name__ == "__main__":
       mdb = _movie_database()
       start_service(mdb)