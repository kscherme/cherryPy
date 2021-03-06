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
				image_info = self.mdb.get_image(mid)
				smallDict = {'id':mid, 'genres':movie_info[1], 'title':movie_info[0], 'img':image_info, 'result':'success'}
				output['movies'].append(smallDict)
		except KeyError as ex:
			output['result'] = 'error'

		return json.dumps(output)

	def GET(self, mid):
		output = {'result':'success'}
		try:
			mid = int(mid)
			movie_ids = self.mdb.get_movies()
			if mid not in movie_ids:
				raise KeyError()
			movie_info = self.mdb.get_movie(mid)
			image_info = self.mdb.get_image(mid)
			output['id'] = mid
			output['genres'] = movie_info[1]
			output['title'] = movie_info[0]
			output['img'] = image_info
		except KeyError as ex:
			output['result'] = 'error'

		return json.dumps(output)

	def POST(self):
		output = {'result':'success'}
		try:
			movie_ids = self.mdb.get_movies()
			if len(movie_ids) == 0:
				mid = 1
			else:
				mid = max(movie_ids) + 1
			input_body = cherrypy.request.body.read().decode()
			input_body = json.loads(input_body)
			genres = input_body['genres']
			title = input_body['title']
			mlist = [title, genres]
			self.mdb.set_movie(mid, mlist)
			output['id'] = mid
		except KeyError as ex:
			output['result'] = 'error'

		return json.dumps(output)

	def PUT(self, mid):
		output = {'result':'success'}
		try:
			mid = int(mid)
			input_body = cherrypy.request.body.read().decode()
			input_body = json.loads(input_body)
			genres = input_body['genres']
			title = input_body['title']
			mlist = [title, genres]
			self.mdb.set_movie(mid, mlist)
		except KeyError as ex:
			output['result'] = 'error'

		return json.dumps(output)

	def DELETE_INDEX(self):
		output = {'result':'success'}
		try:
			self.mdb.movies.clear()
			self.mdb.images.clear()
		except KeyError as ex:
			output['result'] = 'error'

		return json.dumps(output)

	def DELETE(self, mid):
		output = {'result':'success'}
		try:
			mid = int(mid)
			self.mdb.delete_movie(mid)
			self.mdb.delete_image(mid)
		except KeyError as ex:
			output['result'] = 'error'

		return json.dumps(output)







	
