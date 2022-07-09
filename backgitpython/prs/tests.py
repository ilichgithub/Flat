from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class PRsAPIViewTest(APITestCase):
	def setUp(self):
		pass
		
	def tearDown(self):
		pass
		
	def test_get_pullrequests(self):
		response = self.client.get('/api/v1/prs/')
		data = response.json()
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	