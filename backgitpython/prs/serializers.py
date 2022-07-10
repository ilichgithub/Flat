from rest_framework import serializers
from prs.models import PullRequest

class PullRequestSerializers(serializers.ModelSerializer):
    class Meta:
        model = PullRequest  
        exclude = [ 'created', 'modified']