from django.urls import path
from .views import *


urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('project/', ProjectView.as_view(), name='project_create'),
    path('project/invite/', ProjectInviteView.as_view(), name='user_invite_to_project'),
    path('project/invite/answer/', ProjectInviteAnswerView.as_view(), name='user_answer_to_invitation'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_views'),
    path('project/<int:pk>/members/', ProjectMemberListView.as_view(), name='project_members_list'),
    path('project/<int:pk>/member/', ProjectMemberView.as_view(), name='project_member_delete'),
    path('project/<int:pk>/tasks/', TaskListView.as_view(), name='task_list'),
    path('project/<int:pk>/task/', TaskView.as_view(), name='task_create'),
    path('project/task/<int:pk>/', TaskView.as_view(), name='task_update_delete'),

]