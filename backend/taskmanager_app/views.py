from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response
from . import serializers, models
import rest_framework.status as HTTP_status
from rest_framework import status

# -----------------------------------------------------------------------------

class ProjectListView(APIView):

    def get(self, request, *args, **kwargs):
        memberships = models.Membership.objects.filter(user=self.request.user)
        serializer = serializers.MembershipSerializers(memberships, many=True)
        return Response(data=serializer.data)

# -----------------------------------------------------------------------------

class ProjectRetrieveView(APIView):

    def get(self, request, *args, **kwargs):
        project_id = self.kwargs['pk']
        membership = models.Membership.objects.get(project__id=project_id, user=self.request.user)
        serializer = serializers.MembershipSerializers(membership)
        return Response(data=serializer.data)

# -----------------------------------------------------------------------------

class ProjectCreateView(APIView):

    def post(self, request, format=None):
        '''
        create a project Model,
        then add this project along with user creator data to Membership Model
        '''
        serializer= serializers.ProjectSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # create new project object 
        project = models.Project(**serializer.validated_data)
        project.save()

        try:
            # create a new membership object
            member = self.create_membership(project)

            # if user have same project name already 
            if member.is_exists():
                project.delete()
                return Response(data={'err': 'A project with the same name already exists'}, status=HTTP_status.HTTP_400_BAD_REQUEST )
            
            member.save()

        # if the membership object faild to save, must be deleted problematic project
        except:
            project.delete()
            return Response(data={'err': 'Failed to create project'}, status=HTTP_status.HTTP_400_BAD_REQUEST)
        return Response(data={'id': project.pk})
    
    def create_membership(self, project):
        '''
        create a membership object base on new project created by logined in user
        '''
        member = models.Membership()
        member.project = project
        member.user = self.request.user
        member.inviter = None
        member.user_role = models.Membership.ADMIN_ROLE
        member.confirmed = True
        return member

# -----------------------------------------------------------------------------
