from django.urls import path
from .views import *


urlpatterns = [
    path('projects/', ProjectListView.as_view()),
    path('project/<int:pk>/', ProjectRetrieveView.as_view()),
    path('project/', ProjectCreateView.as_view()),
]