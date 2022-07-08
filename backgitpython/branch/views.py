from rest_framework.views import APIView
from rest_framework.response import Response
from git import Repo, Git, Commit

class BranchAPIView(APIView):
        
    def get(self, request, format=None, *args, **kwargs):
        print("BranchesAPIView.get")
        local_repo = Repo("/tmp/git/ilich")
        for remote in local_repo.remotes:
            remote.fetch()
        remote_repo = local_repo.remote()
        local_branch = local_repo.active_branch.name
        remote_branches = []
        for this_branch in remote_repo.refs:
            remote_branches.append(this_branch.remote_head)
        return Response({
            'branch_active': local_branch,
            'branches': remote_branches
            })

class CommitBranchAPIView(APIView):

    def get(self, request, branch, format=None):
        print("CommitsBranchAPIView.get")
        local_repo = Repo("/tmp/git/ilich")
        local_repo.git.checkout(branch)
        o = local_repo.remotes.origin
        o.pull()
        commits = list(local_repo.iter_commits(
            local_repo.active_branch.name, max_count=100
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