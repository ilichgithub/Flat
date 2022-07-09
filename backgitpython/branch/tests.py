from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class BranchesAPIViewTest(APITestCase):
	def setUp(self):
		pass
		
	def tearDown(self):
		pass
		
	def test_get_branches(self):
		response = self.client.get('/api/v1/branches/')
		data = response.json()
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertFalse( "branchActive" in data )
		self.assertTrue("branches" in data )
		self.assertTrue("master" in data["branches"] )
		self.assertFalse( "HEAD" in data["branches"] )

	def test_get_commits(self):
		response = self.client.get('/api/v1/branches/master/commits')
		data = response.json()
		print(data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertTrue(len(data)>0)
