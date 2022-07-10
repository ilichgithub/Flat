from django.db import models
from model_utils.models import TimeStampedModel

class PullRequest(TimeStampedModel):
	branch_source 	= models.CharField(max_length=50, null=False, blank=False)
	branch_destiny 	= models.CharField(max_length=50, null=False, blank=False)
	author 			= models.CharField(max_length=50, null=False, blank=False)
	title 			= models.CharField(max_length=50, null=False, blank=False)
	description 	= models.TextField(max_length=500, null=False, blank=False)
	status 			= models.CharField(max_length=50, null=False, blank=False)

	def __str__(self):
		return self.title