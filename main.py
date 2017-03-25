# main.py
# Katie Schermerhorn

from _movie_database import _movie_database
import cherrypy
from reset import ResetController
from movies import MovieController

def start_service(mdb):

	# create resource objects
	resetController = ResetController(mdb)
	movieController = MovieController(mdb)

	dispatcher = cherrypy.dispatch.RoutesDispatcher()

	# connections
	# reset connections
	dispatcher.connect('reset_index', '/reset/', controller=resetController, action = 'PUT_INDEX', conditions=dict(method=['PUT']))
	dispatcher.connect('reset', '/reset/:mid', controller=resetController, action = 'PUT', conditions=dict(method=['PUT']))

	# movie connections
	dispatcher.connect('movie_get_index', '/movies/', controller=movieController, action = 'GET_INDEX', conditions=dict(method=['GET']))
	dispatcher.connect('movie_get', '/movies/:mid', controller=movieController, action = 'GET', conditions=dict(method=['GET']))


	conf = { 'global' 	: {'server.socket_host': 'ash.campus.nd.edu',
							'server.socket_port': 40100,},
			 '/'		: {'request.dispatch': dispatcher,} }

	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config=conf)
	cherrypy.quickstart(app)

#create movieDBobject
if __name__ == "__main__":
       mdb = _movie_database()
       start_service(mdb)
