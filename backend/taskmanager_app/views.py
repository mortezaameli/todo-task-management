from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response
from . import serializers, models
import rest_framework.status as HTTP_status
from rest_framework import status

# -----------------------------------------------------------------------------

class ProjectListView(generics.ListAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializers

# -----------------------------------------------------------------------------

class ProjectRetrieveView(generics.RetrieveAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializers

# -----------------------------------------------------------------------------

