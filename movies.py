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
                        movie_ids = self.mdb.get_movies()
                        for mid in movie_ids:
                            movie_info = self.mdb.get_movie(mid)
                            smallDict = {'id':mid, 'genres':movie_info[1], 'title':movie_info[0], 'result':'success'}
                            output['movies'].append(smallDict)
                except KeyError as ex:
                        output['result'] = 'error'
                        
                return json.dumps(output)


	
