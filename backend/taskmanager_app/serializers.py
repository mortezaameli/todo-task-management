from rest_framework import serializers
from .models import Project, Task, Membership
from django.contrib.auth import get_user_model


User = get_user_model()

# -----------------------------------------------------------------------------

class ProjectSerializers(serializers.Serializer):
    id      = serializers.IntegerField(read_only=True)
    name    = serializers.CharField(required=True)

# -----------------------------------------------------------------------------

class UserInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model   = User
        fields  = ['email', 'username']

# -----------------------------------------------------------------------------

class MembershipSerializers(serializers.Serializer):
    id          = serializers.CharField(source='project.id', read_only=True)
    name        = serializers.CharField(source='project.name', read_only=True)
    user        = UserInlineSerializer(read_only=True)
    inviter     = UserInlineSerializer(read_only=True)
    user_role   = serializers.CharField(required=True)
    confirmed   = serializers.BooleanField()

# -----------------------------------------------------------------------------

class ProjectInviteSerializer(serializers.Serializer):
    project_id    = serializers.IntegerField(required=True)
    user_email    = serializers.EmailField(required=True)

# -----------------------------------------------------------------------------

class ProjectInviteAnswerSerializer(serializers.Serializer):
    project_id    = serializers.IntegerField(required=True)
    confirmed     = serializers.BooleanField(required=True)

# -----------------------------------------------------------------------------

class ProjectMemberSerializer(serializers.Serializer):
    username  = serializers.CharField(read_only=True, source='user.username')
    email     = serializers.EmailField(source='user.email', required=False)
    user_role = serializers.CharField(read_only=True)
    confirmed = serializers.BooleanField(read_only=True)

# -----------------------------------------------------------------------------

class TaskCreateSerializers(serializers.Serializer):
    project_id  = serializers.IntegerField(source='project.id', required=True)
    title       = serializers.CharField(required=True)

# -----------------------------------------------------------------------------
