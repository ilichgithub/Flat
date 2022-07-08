from rest_framework.views import APIView
from rest_framework.response import Response
from git import Repo, Git, Commit

class BranchAPIView(APIView):
        
    def get(self, request, format=None, *args, **kwargs):
        local_repo = Repo("/code/backgitpython/repository")
        branches = local_repo.git.branch('-a').replace(
            "*", "").replace("->", "").replace("remotes/", "").replace(
                "origin/", "").replace("HEAD", "").split()
        branches = set(branches)
        return Response({
            'branches': branches
            })

class CommitBranchAPIView(APIView):

    def get(self, request, branch, format=None):
        local_repo = Repo("/code/backgitpython/repository")
        try:
            commits = list(local_repo.iter_commits(
                branch, max_count=100
                ))
        except Exception as ex:
            local_repo.git.checkout(branch)
            commits = list(local_repo.iter_commits(
                branch, max_count=100
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
        Repo.clone_from("git@github.com:ilichgithub/git.git", "/tmp/git/ilich")
        return Response({"result":"clone"})