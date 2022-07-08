from django.urls import path
from .views import *

app_name = 'branch'

urlpatterns = [
    path('', BranchAPIView.as_view()),
    path('<slug:branch>/commits', CommitBranchAPIView.as_view()),
    path('clone', CloneRepoAPIView.as_view()),
]