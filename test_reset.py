import unittest
import requests
import json

class TestReset(unittest.TestCase):

	SITE_URL = 'http://ash.campus.nd.edu:40100'
	RESET_URL = SITE_URL + '/reset/'

	def test_reset_data(self):
		m = {}
		m['apikey'] = 'AAAAAAAB'
		r = requests.put(self.RESET_URL)

if __name__ == "__main__":
	unittest.main()

