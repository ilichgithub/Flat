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
		self.assertTrue( "result" in data )
		self.assertTrue("message" in data )
		self.assertTrue("master" in data["result"] )
		self.assertFalse( "HEAD" in data["result"] )

	def test_get_commits(self):
		response = self.client.get('/api/v1/branches/master/commits')
		data = response.json()
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertTrue(len(data["result"])>0)
		self.assertTrue("message" in data )
