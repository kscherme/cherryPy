# reset.py 
# Katie Schermerhorn

import cherrypy
import re,json

class ResetController(object, mdb = None):

	def PUT():

		output = {'result':'success'}
		try:
			mdb.load_movies('ml-1m/movies.dat')
			mdb.load_users('ml-1m/users.dat')
       		mdb.load_ratings('ml-1m/ratings.dat')
       	except KeyError as ex:
       		output['result'] = 'error'

       	return json.dumps(output)

	