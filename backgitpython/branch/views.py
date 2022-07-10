import os
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from git import Repo, Git, Commit

def cloneRepository():
    try:
        Repo.clone_from(settings.URL_REPOSITORY_REMOTE, settings.PATH_REPOSITORY_LOCAL)
        return True
    except Exception as ex:
        return False

def getBranches(local_repo):
    branches = local_repo.git.branch('-a').replace(
        "*", "").replace("->", "").replace("remotes/", "").replace(
            "origin/", "").replace("HEAD", "").split()
    return set(branches)

class BranchAPIView(APIView):
        
    def get(self, request, format=None, *args, **kwargs):
        mkdir = os.path.exists(settings.PATH_REPOSITORY_LOCAL)
        clone = False
        if not mkdir:
            clone = cloneRepository()
        if clone or mkdir:
            local_repo = Repo(settings.PATH_REPOSITORY_LOCAL)
            branches = getBranches(local_repo)
            return Response({
                'result': branches,
                "message":"OK"
                })
        else:
            return Response({
                "result":None,
                "message":"Clone repository not found"
                })

class CommitBranchAPIView(APIView):

    def get(self, request, branch, format=None):
        mkdir = os.path.exists(settings.PATH_REPOSITORY_LOCAL)
        clone = False
        if not mkdir:
            clone = cloneRepository()
        if clone or mkdir:
            local_repo = Repo(settings.PATH_REPOSITORY_LOCAL)
            branches = getBranches(local_repo)
            if branch in branches:
                local_repo.git.checkout(branch)
                commits = list(local_repo.iter_commits(
                    branch
                    ))
            else:
                return Response({
                    "result":None,
                    "message":"Branch not found"
                })
            commitsInfo = []
            for c in commits:
                commitsInfo.append({
                    'name': str(c.author), 
                    'email': c.author.email, 
                    'msg': c.message, 
                    'date':c.committed_datetime.strftime('%Y-%m-%d %H:%M:%S'), 
                    'files': c.stats.total['files']    
                })
            return Response({
                "result":commitsInfo,
                "message":"OK"
                })
        else:
            return Response({
                "result":None,
                "message":"Clone repository not found"
                })

class CloneRepoAPIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        Repo.clone_from(settings.URL_REPOSITORY_REMOTE, settings.PATH_REPOSITORY_LOCAL)
        return Response({"result":"clone"})