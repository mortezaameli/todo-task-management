from django.urls import path
from .views import *


urlpatterns = [
    path('projects/', ProjectListView.as_view()),
    path('project/', ProjectCreateView.as_view()),
    path('project/invite/', ProjectInviteView.as_view()),
    path('project/invite/answer/', ProjectInviteAnswerView.as_view()),
    # path('project/<int:pk>/', ProjectRetrieveView.as_view()),
    path('project/<int:pk>/members/', ProjectMembersView.as_view()),
    path('task/', TaskCreateView.as_view()),

]