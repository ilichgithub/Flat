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
		url = reverse("branch")
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		data = response.json()
		print(data)
		self.assertFalse( "branchActive" in data )
		
	def test_get_branches(self):
		url = reverse("branch")
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		data = response.json()
		print(data)
