from django.urls import path
from .views import *


urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('project/', ProjectView.as_view(), name='project_create'),
    path('project/invite/', ProjectInviteView.as_view(), name='user_invite_to_project'),
    path('project/invite/answer/', ProjectInviteAnswerView.as_view(), name='user_answer_to_invitation'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_views'),
    path('project/<int:pk>/members/', ProjectMembersView.as_view(), name='project_members_list'),
    # path('task/', TaskCreateView.as_view()),

]