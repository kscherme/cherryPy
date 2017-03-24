# movies.py
# Katie Schermerhorn

import cherrypy
import re, json

class MovieController(object):

	def __init__(self, mdb = None):
		self.mdb = mdb

	def GET_INDEX(self):
		output = {'result':'success'}
		try:
			output['movies'] = []
			movies = mdb.get_movies()
			for movie in movies.items():
				smallDict = {'genres':genres, 'title':title}
				output['movies'].append(smallDict)
		except KeyError as ex:
			output['result'] = 'error'

		return json.dumps(output)


	