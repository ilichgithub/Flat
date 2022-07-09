from django.urls import path
from .views import *

app_name = 'branch'

urlpatterns = [
    path('', BranchAPIView.as_view(), name="branch"),
    path('<slug:branch>/commits', CommitBranchAPIView.as_view(), name="commits"),
    path('clone', CloneRepoAPIView.as_view(), name="clone"),
]