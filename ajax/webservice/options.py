# options.py
# Katie Schermerhorn

import cherrypy
import re, json

class OptionController(object):

	def OPTIONS(self, *args, **kwargs):
		return ""