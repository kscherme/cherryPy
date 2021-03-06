# recommendations.py
# Katie Schermerhorn

import cherrypy
import re, json

class RecommendationController(object):

	def __init__(self, mdb = None):
		self.mdb = mdb

	def DELETE_INDEX(self):
		output = {'result':'success'}
		try:
			self.mdb.delete_all_ratings()
		except KeyError as ex:
			output['result'] = 'error'

		return json.dumps(output)

	def GET(self, uid):
		output = {'result':'success'}
		try:
			uid = int(uid)
			uids = self.mdb.get_users()
			if uid in uids:
				mid = self.mdb.get_highest_rated_unvoted_movie(uid)
				output['movie_id'] = mid
			else:
				output['result'] = 'error'
		except KeyError as ex:
			output['result'] = 'error'

		return json.dumps(output)

	def PUT(self, uid):
		output = {'result':'success'}
		try:
			uid = int(uid)
			input_body = cherrypy.request.body.read().decode()
			input_body = json.loads(input_body)
			mid = input_body['movie_id']
			rating = input_body['rating']
			mid = int(mid)
			rating = int(rating)
			print(self.mdb.get_rating(mid))
			self.mdb.set_user_movie_rating(uid, mid, rating)
			print(self.mdb.get_rating(mid))
		except KeyError as ex:
			output['result'] = 'error'

		return json.dumps(output)


