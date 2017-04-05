# ratings.py
# Katie Schermerhorn

import cherrypy
import re, json

class RatingController(object):

	def __init__(self, mdb = None):
		self.mdb = mdb

	def GET(self, mid):
		output = {'result':'success'}
		try:
			mid = int(mid)
			movie_ids = self.mdb.get_movies()
			if mid not in movie_ids:
				raise KeyError()
			rating = self.mdb.get_rating(mid)
			output['rating'] = rating
			output['movie_id'] = mid
		except KeyError as ex:
			output['result'] = 'error'

		return json.dumps(output)