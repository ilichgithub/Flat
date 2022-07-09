import os
from rest_framework.views import APIView
from rest_framework.response import Response
from git import Repo, Git, Commit

def cloneRepository():
    try:
        Repo.clone_from("https://github.com/FlatDigital/fullstack-interview-test.git", "/repository/clone")
        return True
    except Exception as ex:
        return False

class BranchAPIView(APIView):
        
    def get(self, request, format=None, *args, **kwargs):
        mkdir = os.path.exists('/repository/clone')
        clone = False
        if not mkdir:
            clone = cloneRepository()
        if clone or mkdir:
            local_repo = Repo("/repository/clone")
            print(local_repo.git.status())
            branches = local_repo.git.branch('-a').replace(
                "*", "").replace("->", "").replace("remotes/", "").replace(
                    "origin/", "").replace("HEAD", "").split()
            branches = set(branches)
            return Response({
                'branches': branches
                })
        else:
            return Response({
                "mensaje":"Error al tratar de clonar el repositorio"
                })

class CommitBranchAPIView(APIView):

    def get(self, request, branch, format=None):
        local_repo = Repo("/repository/clone")
        try:
            commits = list(local_repo.iter_commits(
                branch
                ))
        except Exception as ex:
            local_repo.git.checkout(branch)
            commits = list(local_repo.iter_commits(
                branch
                ))

        commitsInfo = []
        for c in commits:
            commitsInfo.append({
                'name': str(c.author), 
                'email': c.author.email, 
                'msg': c.message, 
                'date':c.committed_datetime.strftime('%Y-%m-%d %H:%M:%S'), 
                'files': c.stats.total['files']    
            })
        return Response(commitsInfo)

class CloneRepoAPIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        Repo.clone_from("https://github.com/FlatDigital/fullstack-interview-test.git", "/repository/clone")
        return Response({"result":"clone"})