from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response
from . import serializers, models
import rest_framework.status as HTTP_status
from rest_framework import status
from rest_framework import permissions

# -----------------------------------------------------------------------------

class ProjectListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        memberships = models.Membership.objects.filter(user=self.request.user)
        serializer = serializers.MembershipSerializers(memberships, many=True)
        return Response(data=serializer.data)

# -----------------------------------------------------------------------------

class ProjectRetrieveView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        project_id = self.kwargs['pk']
        membership = models.Membership.objects.get(project__id=project_id, user=self.request.user)
        serializer = serializers.MembershipSerializers(membership)
        return Response(data=serializer.data)

# -----------------------------------------------------------------------------

class ProjectCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        '''
        create a project Model,
        then add this project along with user creator data to Membership Model
        '''
        serializer= serializers.ProjectSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # create new Project object 
        project = models.Project(**serializer.validated_data)
        project.save()

        try:
            # create a new membership object
            membership = self.create_membership(project)
            membership.save()

        # if the membership object faild to save, must be deleted problematic project
        except:
            project.delete()
            return Response(data={'err': 'Failed to create project'}, status=HTTP_status.HTTP_400_BAD_REQUEST)
        
        return Response(data={'id': project.pk}, status=status.HTTP_201_CREATED)
    
    def create_membership(self, project):
        '''
        create a membership object base on new project created by logined in user
        '''
        membership = models.Membership()
        membership.project = project
        membership.user = self.request.user
        membership.inviter = None
        membership.user_role = models.Membership.ADMIN_ROLE
        membership.confirmed = True
        return membership

# -----------------------------------------------------------------------------

class ProjectInviteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        '''
        create a Membershipthat invite a user to the project,
        '''
        serializer= serializers.ProjectInviteSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        project_id = serializer.data.get('project_id')
        user_email = serializer.data.get('user_email')

        try:
            project_obj = models.Project.objects.get(pk=project_id)
        except models.Project.DoesNotExist:
            return Response(data={'err': 'Project does not exist'}, status=status.HTTP_404_NOT_FOUND)

        try:
            invited_user = models.User.objects.get(email=user_email)
        except models.User.DoesNotExist:
            return Response(data={'err': 'Invited user does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # check the user invited herself
        if invited_user == self.request.user:
            return Response(data={'err': 'You cannot invite yourself to the project'}, status=status.HTTP_400_BAD_REQUEST)

        # check for invited user is already a member of the project
        if models.Membership.objects.filter(project__id=project_id,user=invited_user).exists():
            return Response(data={'err': 'Invited user is already a member of the project'}, status=status.HTTP_409_CONFLICT)

        # create Membership for invited user to the project
        membership = models.Membership()
        membership.project = project_obj
        membership.user = invited_user
        membership.inviter = self.request.user
        membership.user_role = models.Membership.USER_ROLE
        membership.confirmed = False
        membership.save()

        return Response(data={'msg': 'The request for cooperation in the project was sent to the user'}, status=status.HTTP_200_OK)

# -----------------------------------------------------------------------------

class ProjectInviteAnswerView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        '''
        Answer to project invitation
        '''
        serializer= serializers.ProjectInviteAnswerSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        project_id = serializer.data.get('project_id')
        confirmed = serializer.data.get('confirmed')
        user = self.request.user

        # check this user has a membership of project
        try:
            membership = models.Membership.objects.get(project__id=project_id, user=user)
        except models.Membership.DoesNotExist:
            return Response(data={'err': 'You are not a member of this project'}, status=status.HTTP_404_NOT_FOUND)

        # check for user has already approved the membership request
        if membership.confirmed:
            print()
            print(membership.__dict__)
            print()
            return Response(data={'err': 'You have already approved the membership invitation'}, status=status.HTTP_409_CONFLICT)

        if confirmed:
            membership.confirmed = True
            membership.save()
            return Response(data={'msg': 'You have been added to the project'}, status=status.HTTP_200_OK)
        else:
            membership.delete()
            return Response(data={'msg': 'Your membership was rejected'}, status=status.HTTP_200_OK)

# -----------------------------------------------------------------------------

class TaskCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        '''
        create a Task in Project,
        '''
        serializer= serializers.TaskCreateSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # check this user has a membership of project
        project_id = serializer.data.get('project_id')
        try:
            membership = models.Membership.objects.get(project__id=project_id, user=self.request.user)
        except models.Membership.DoesNotExist:
            return Response(data={'err': 'You are not a member of this project'}, status=status.HTTP_404_NOT_FOUND)

        # check user Admin of the project to which the task is to be added
        if membership.user_role != models.Membership.ADMIN_ROLE:
            return Response(data={'err': 'Only the project admin can add task'}, status=status.HTTP_403_FORBIDDEN)

        # create new Task object
        task = models.Task()
        task.project = membership.project
        task.owner = self.request.user
        task.title = serializer.data.get('title')
        task.save()
        
        return Response(data={'id': task.pk}, status=status.HTTP_201_CREATED)

# -----------------------------------------------------------------------------
