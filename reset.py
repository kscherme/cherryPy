# reset.py 
# Katie Schermerhorn

import cherrypy
import re,json

class ResetController(object):

	def __init__(self, mdb = None):
		self.mdb = mdb


	def PUT(self):

		output = {'result':'success'}
		try:
			self.mdb.load_movies('ml-1m/movies.dat')
			self.mdb.load_users('ml-1m/users.dat')
			self.mdb.load_ratings('ml-1m/ratings.dat')
		except KeyError as ex:
			output['result'] = 'error'

		return json.dumps(output)

	