from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response
from . import serializers, models
import rest_framework.status as HTTP_status
from rest_framework import status
from rest_framework import permissions
from django.db.models import F

# -----------------------------------------------------------------------------

class ProjectListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        memberships = models.Membership.objects.filter(user=self.request.user)
        serializer = serializers.MembershipSerializers(memberships, many=True)
        return Response(data=serializer.data)

# -----------------------------------------------------------------------------

class ProjectView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''
        get project info
        '''
        project_id = self.kwargs['pk']
        membership = models.Membership.objects.get(project__id=project_id, user=self.request.user)
        serializer = serializers.MembershipSerializers(membership)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        '''
        create a project Model,
        then add this project along with user creator data to Membership Model
        '''
        serializer = serializers.ProjectSerializers(data=request.data)
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
    
    def delete(self, request, *args, **kwargs):
        '''
        delete project with id number
        '''
        project_id = self.kwargs['pk']

        # check project is exists
        try:
            project_obj = models.Project.objects.get(pk=project_id)
        except models.Project.DoesNotExist:
            return Response(data={'err': 'Project does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # check user is member of this project
        try:
            membership = models.Membership.objects.get(project=project_obj, user=self.request.user)
        except models.Membership.DoesNotExist:
            return Response(data={'err': 'You are not a member of this project'}, status=status.HTTP_403_FORBIDDEN)

        # check user is admin of project
        if membership.user_role != models.Membership.ADMIN_ROLE:
            return Response(data={'err': 'Only the admin of project can delete it'}, status=status.HTTP_403_FORBIDDEN)

        project_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        '''
        update project name
        '''
        project_id = self.kwargs['pk']

        serializer = serializers.ProjectSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        new_project_name = serializer.data.get('name')

        # check project is exists
        try:
            project_obj = models.Project.objects.get(pk=project_id)
        except models.Project.DoesNotExist:
            return Response(data={'err': 'Project does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # check user is member of this project
        try:
            membership = models.Membership.objects.get(project=project_obj, user=self.request.user)
        except models.Membership.DoesNotExist:
            return Response(data={'err': 'You are not a member of this project'}, status=status.HTTP_403_FORBIDDEN)

        # check user is admin of project
        if membership.user_role != models.Membership.ADMIN_ROLE:
            return Response(data={'err': 'Only the admin of project can update it'}, status=status.HTTP_403_FORBIDDEN)

        # check new project name is equal with previous name
        if project_obj.name == new_project_name:
            return Response(status=status.HTTP_204_NO_CONTENT)

        project_obj.name = new_project_name
        project_obj.save()
        return Response(data={'id': project_obj.id}, status=status.HTTP_200_OK)

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

        return Response(data={'username': invited_user.username}, status=status.HTTP_200_OK)

# -----------------------------------------------------------------------------

class ProjectMemberListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        project_id = self.kwargs['pk']
        memberships = models.Membership.objects.filter(project__id=project_id)
        
        # check user is a member of project
        if not memberships.filter(user=self.request.user).exists():
            return Response(data={'err': 'You are not a member of this project'}, status=status.HTTP_403_FORBIDDEN)

        serializer = serializers.ProjectMemberSerializer(memberships, many=True)
        return Response(data=serializer.data)

# -----------------------------------------------------------------------------

class ProjectMemberView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        serializer = serializers.ProjectMemberSerializer(data=self.request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        deleted_user_email = serializer.data.get('email', self.request.user.email)
        project_id = self.kwargs['pk']

        # check the requesting user is a member of the project
        try:
            membership = models.Membership.objects.get(project__id=project_id, user=self.request.user)
        except models.Membership.DoesNotExist:
            return Response(data={'err': 'You are not a member of this project'}, status=status.HTTP_403_FORBIDDEN) 

        # The non-admin user leaves the project by herself
        if membership.user_role == models.Membership.USER_ROLE:
            if self.request.user.email != deleted_user_email:
                return Response(data={'err': 'Only the project admin can delete other user'}, status=status.HTTP_403_FORBIDDEN) 
            membership.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        # check project admin requests to delete yourself!
        if membership.user.email == deleted_user_email:
            return Response(data={'err': 'You are admin, then you can not remove yourself from the project'}, status=status.HTTP_403_FORBIDDEN)

        # check the requested user to delete is member of the project
        try:
            membership = models.Membership.objects.get(project__id=project_id, user__email=deleted_user_email)
        except models.Membership.DoesNotExist:
            return Response(data={'err': 'The selected user to delete is not a member of this project'}, status=status.HTTP_404_NOT_FOUND) 

        membership.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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

class TaskListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        project_id = self.kwargs['pk']
        tasks = models.Task.objects.filter(project__id=project_id)
        serializer = serializers.TaskSerializers(tasks, many=True)
        return Response(data=serializer.data)

# -----------------------------------------------------------------------------

class TaskView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        '''
        create a Task in Project
        '''
        project_id = self.kwargs['pk']

        serializer= serializers.TaskSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # check this user has a membership of project
        try:
            membership = models.Membership.objects.get(project__id=project_id, user=self.request.user)
        except models.Membership.DoesNotExist:
            return Response(data={'err': 'You are not a member of this project'}, status=status.HTTP_403_FORBIDDEN)

        # create new Task object
        task = models.Task()
        task.project      = membership.project
        task.phase        = models.Task.PHASE_TODO
        task.row_position = models.Task.objects.filter(project=task.project, phase=models.Task.PHASE_TODO).count()
        task.creator      = self.request.user
        task.title        = serializer.data.get('title')
        task.save()
        
        data = {
            'id': task.pk,
            'phase': task.phase,
            'row_position': task.row_position,
        }
        return Response(data=data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        task_id = self.kwargs['pk']

        serializer= serializers.TaskUpdateSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            task = models.Task.objects.get(pk=task_id)
        except models.Task.DoesNotExist:
            return Response(data={'err': 'Task does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # check this user has a membership of project
        try:
            membership = models.Membership.objects.get(project=task.project, user=self.request.user)
        except models.Membership.DoesNotExist:
            return Response(data={'err': 'You are not a member of this project'}, status=status.HTTP_403_FORBIDDEN)

        if not 'phase' in serializer.data:
            for k in serializer.data:
                setattr(task, k, serializer.data[k])
            task.save()
        else:
            before_phase = task.phase
            before_row_position = task.row_position
            new_phase        = serializer.data.get('phase')
            new_row_position = serializer.data.get('row_position')
            if before_phase != new_phase:
                models.Task.objects.filter(project=task.project, phase=new_phase, row_position__gte=new_row_position).update(row_position=F('row_position')+1)
                task.phase = new_phase
                task.row_position = new_row_position
                task.save()
                models.Task.objects.filter(project=task.project, phase=before_phase, row_position__gt=before_row_position).update(row_position=F('row_position')-1)
            else:
                if new_row_position > before_row_position:
                    models.Task.objects.filter(project=task.project, phase=before_phase, row_position__gt=before_row_position, row_position__lte=new_row_position).update(row_position=F('row_position')-1)
                    task.row_position = new_row_position
                    task.save()
                elif new_row_position < before_row_position:
                    models.Task.objects.filter(project=task.project, phase=before_phase, row_position__lt=before_row_position, row_position__gte=new_row_position).update(row_position=F('row_position')+1)
                    task.row_position = new_row_position
                    task.save()

        serializer = serializers.TaskSerializers(task)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        
# -----------------------------------------------------------------------------
