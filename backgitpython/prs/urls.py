from django.urls import path
from .views import *

app_name = 'prs'

urlpatterns = [
    path('', PullRequestAPIView.as_view()),
    path('update-partial/<int:pk>/', PullRequestUpdatePartialAPIView.as_view()),
    path('merge/<int:pk>/', PullRequestMergeUpdatePartialAPIView.as_view()),
]