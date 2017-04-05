# reset.py 
# Katie Schermerhorn

import cherrypy
import re,json
from _movie_database import _movie_database

class ResetController(object):

	def __init__(self, mdb = None):
		self.mdb = mdb
		self.orginal_movies = _movie_database()
		self.orginal_movies.load_movies('ml-1m/movies.dat') 
		self.orginal_images = _movie_database()
		self.orginal_images.load_images('images.dat')


	def PUT_INDEX(self):

		output = {'result':'success'}
		try:
			self.mdb.load_movies('ml-1m/movies.dat')
			self.mdb.load_users('ml-1m/users.dat')
			self.mdb.load_ratings('ml-1m/ratings.dat')
			self.mdb.load_images('images.dat')
		except KeyError as ex:
			output['result'] = 'error'

		return json.dumps(output)

	def PUT(self, mid):

		output = {'reset':'success'}
		try:
			mid = int(mid)
			movie_list = self.orginal_movies.get_movie(mid)
			self.mdb.set_movie(mid, movie_list)
			image_info = self.orginal_images.get_image(mid)
			self.mdb.set_image(mid, image_info)
		except KeyError as ex:
			output['result'] = 'error'

		return json.dumps(output)

	
