# main.py
# Katie Schermerhorn

from _movie_database import _movie_database
import cherrypy
from reset import ResetController
from movies import MovieController
from users import UserController
from ratings import RatingController
from recommendations import RecommendationController
from options import OptionController

def CORS():
	cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
	cherrypy.response.headers["Access-Control-Allow-Credentials"] = "true"	
	cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE, OPTIONS"

def start_service(mdb):

	# create resource objects
	resetController = ResetController(mdb)
	movieController = MovieController(mdb)
	userController = UserController(mdb)
	ratingController = RatingController(mdb)
	recommendationController = RecommendationController(mdb)
	optionController = OptionController

	dispatcher = cherrypy.dispatch.RoutesDispatcher()

	# connections
	# reset connections
	dispatcher.connect('reset_index', '/reset/', controller=resetController, action = 'PUT_INDEX', conditions=dict(method=['PUT']))
	dispatcher.connect('reset_index_option', '/reset/', controller=optionController, action = 'OPTION', conditions=dict(method=['OPTION']))
	dispatcher.connect('reset', '/reset/:mid', controller=resetController, action = 'PUT', conditions=dict(method=['PUT']))
	dispatcher.connect('reset_option', '/reset/:mid', controller=optionController, action = 'OPTION', conditions=dict(method=['OPTION']))

	# movie connections
	dispatcher.connect('movie_get_index', '/movies/', controller=movieController, action = 'GET_INDEX', conditions=dict(method=['GET']))
	dispatcher.connect('movie_get', '/movies/:mid', controller=movieController, action = 'GET', conditions=dict(method=['GET']))
	dispatcher.connect('movie_post_index', '/movies/', controller=movieController, action = 'POST', conditions=dict(method=['POST']))
	dispatcher.connect('movie_put', '/movies/:mid', controller=movieController, action = 'PUT', conditions=dict(method=['PUT']))
	dispatcher.connect('movie_delete_index', '/movies/', controller=movieController, action = 'DELETE_INDEX', conditions=dict(method=['DELETE']))
	dispatcher.connect('movie_delete', '/movies/:mid', controller=movieController, action = 'DELETE', conditions=dict(method=['DELETE']))
	dispatcher.connect('movie_index_option', '/movies/', controller=optionController, action = 'OPTION', conditions=dict(method=['OPTION']))
	dispatcher.connect('movie_option', '/movies/:mid', controller=optionController, action = 'OPTION', conditions=dict(method=['OPTION']))

	# user connections
	dispatcher.connect('user_get_index', '/users/', controller=userController, action = 'GET_INDEX', conditions=dict(method=['GET']))
	dispatcher.connect('user_get', '/users/:uid', controller=userController, action = 'GET', conditions=dict(method=['GET']))
	dispatcher.connect('user_post_index', '/users/', controller=userController, action = 'POST', conditions=dict(method=['POST']))
	dispatcher.connect('user_put', '/users/:uid', controller=userController, action = 'PUT', conditions=dict(method=['PUT']))
	dispatcher.connect('user_delete_index', '/users/', controller=userController, action = 'DELETE_INDEX', conditions=dict(method=['DELETE']))
	dispatcher.connect('user_delete', '/users/:uid', controller=userController, action = 'DELETE', conditions=dict(method=['DELETE']))
	dispatcher.connect('user_index_option', '/users/', controller=optionController, action = 'OPTION', conditions=dict(method=['OPTION']))
	dispatcher.connect('user_option', '/users/:uid', controller=optionController, action = 'OPTION', conditions=dict(method=['OPTION']))

	# rating connections
	dispatcher.connect('rating_get', '/ratings/:mid', controller=ratingController, action = 'GET', conditions=dict(method=['GET']))
	dispatcher.connect('rating_option', '/ratings/:mid', controller=optionController, action = 'OPTION', conditions=dict(method=['OPTION']))

	# recommendation connections
	dispatcher.connect('recommendation_delete_index', '/recommendations/', controller=recommendationController, action = 'DELETE_INDEX', conditions=dict(method=['DELETE']))
	dispatcher.connect('recommendation_get', '/recommendations/:uid', controller=recommendationController, action = 'GET', conditions=dict(method=['GET']))
	dispatcher.connect('recommendation_put', '/recommendations/:uid', controller=recommendationController, action = 'PUT', conditions=dict(method=['PUT']))
	dispatcher.connect('recommendation_index_option', '/recommendations/', controller=optionController, action = 'OPTION', conditions=dict(method=['OPTION']))
	dispatcher.connect('recommendation_option', '/recommendations/:uid', controller=optionController, action = 'OPTION', conditions=dict(method=['OPTION']))

	conf = { 'global' 	: {'server.socket_host': 'ash.campus.nd.edu',
							'server.socket_port': 40100,},
			 '/'		: {'request.dispatch': dispatcher,
			 				'tools.CORS.on': True} }

	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config=conf)
	cherrypy.quickstart(app)

#create movieDBobject
if __name__ == "__main__":
	cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
	mdb = _movie_database()
	start_service(mdb)
