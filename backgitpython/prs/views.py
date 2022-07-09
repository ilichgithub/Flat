from django.shortcuts import render
from rest_framework import status, generics 
from .serializers import PullRequestSerializers
from .models import PullRequest
from rest_framework.response import Response 
from git import Repo, Git, Commit

class PullRequestAPIView(generics.ListCreateAPIView):
    queryset = PullRequest.objects.all()
    serializer_class = PullRequestSerializers
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PullRequestUpdatePartialAPIView(generics.UpdateAPIView):
    queryset = PullRequest.objects.all()
    serializer_class = PullRequestSerializers
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "pull request updated successfully"
                })
        else:
            return Response({
                "message": "failed", 
                "details": serializer.errors
                })

class PullRequestMergeUpdatePartialAPIView(generics.UpdateAPIView):
    queryset = PullRequest.objects.all()
    serializer_class = PullRequestSerializers
    lookup_field = 'pk'
    
    def update(self, request, format=None, *args, **kwargs):
        info = request.data
        local_repo = Repo("/repository/clone")
        branch_source = info['branch_source']
        branch_destiny = info['branch_destiny']
        local_repo.git.checkout(branch_destiny)

        try:
            obj = local_repo.git.merge(branch_source)
        except Exception as ex:
            obj = str(ex).replace("\n", " ")

        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "pull rquest updated successfully",
                "result":obj
                })
        else:
            return Response({
                "message": "failed", 
                "details": serializer.errors, 
                "result":obj
                })