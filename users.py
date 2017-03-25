# users.py
# Katie Schermerhorn

import cherrypy
import re, json

class UserController(object):

	def __init__(self, mdb = None):
		self.mdb = mdb

	def GET_INDEX(self):
		output = {'result':'success'}
		try:
			output['users'] = []
			user_ids = self.mdb.get_users()
			for uid in user_ids:
				user_info = self.mdb.get_user(uid)
				smallDict = {'id':uid, 'zipcode':user_info[4], 'age':user_info[2], 'gender':user_info[1], 'occupation':user_info[3]}
				output['users'].append(smallDict)
		except KeyError as ex:
			output['result'] = 'error'

		return json.dumps(output)

	def GET(self, uid):
		output = {'result':'success'}
		try:
			uid = int(uid)
			user_ids = self.mdb.get_users()
			if uid not in user_ids:
				raise KeyError()
			user_info = self.mdb.get_user(uid)
			output['id'] = uid
			output['zipcode'] = user_info[3]
			output['age'] = user_info[1]
			output['gender'] = user_info[0]
			output['occupation'] = user_info[2]
		except KeyError as ex:
			output['result'] = 'error'

		return json.dumps(output)

	def POST(self):
		output = {'result':'success'}
		try:
			user_ids = self.mdb.get_movies()
			if len(user_ids) == 0:
				uid = 1
			else:
				uid = max(user_ids) + 1
			input_body = cherrypy.request.body.read().decode()
			input_body = json.loads(input_body)
			zipcode = input_body['zipcode']
			age = input_body['age']
			gender = input_body['gender']
			occupation = input_body['occupation']
			ulist = [gender, age, occupation, zipcode]
			self.mdb.set_user(uid, ulist)
			output['id'] = uid
		except KeyError as ex:
			output['result'] = 'error'

		return json.dumps(output)

	def PUT(self, uid):
		output = {'result':'success'}
		try:
			uid = int(uid)
			input_body = cherrypy.request.body.read().decode()
			input_body = json.loads(input_body)
			zipcode = input_body['zipcode']
			age = input_body['age']
			gender = input_body['gender']
			occupation = input_body['occupation']
			ulist = [gender, age, occupation, zipcode]
			self.mdb.set_user(uid, ulist)
		except KeyError as ex:
			output['result'] = 'error'

		return json.dumps(output)

	def DELETE_INDEX(self):
		output = {'result':'success'}
		try:
			self.mdb.users.clear()
		except KeyError as ex:
			output['result'] = 'error'

		return json.dumps(output)

	def DELETE(self, uid):
		output = {'result':'success'}
		try:
			uid = int(uid)
			self.mdb.delete_user(uid)
		except KeyError as ex:
			output['result'] = 'error'

		return json.dumps(output)