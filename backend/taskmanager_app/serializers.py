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

class TaskSerializers(serializers.ModelSerializer):
    creator = UserInlineSerializer(read_only=True)
    
    class Meta:
        model  = Task
        fields = (
            'id',
            'project',
            'phase',
            'row_position',
            'title',
            'description',
            'start_date',
            'due_date',
            'percentage',
            'created_at',
            'creator',
        )
        extra_kwargs = {
            'project': {'required': False},
            'title': {'required': True},
        }

# -----------------------------------------------------------------------------

class MembershipSerializers(serializers.Serializer):
    id          = serializers.CharField(source='project.id', read_only=True)
    name        = serializers.CharField(source='project.name', read_only=True)
    user        = UserInlineSerializer(read_only=True)
    inviter     = UserInlineSerializer(read_only=True)
    user_role   = serializers.CharField(required=True)
    confirmed   = serializers.BooleanField()
    tasks       = TaskSerializers(source='project.tasks', many=True)

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

class TaskUpdateSerializers(serializers.Serializer):
    phase        = serializers.CharField(required=False)
    row_position = serializers.IntegerField(required=False, min_value=0)
    title        = serializers.CharField(required=False, max_length=256)
    description  = serializers.CharField(required=False, allow_blank=True)
    start_date   = serializers.DateTimeField(required=False, input_formats=['%Y-%m-%dT%H:%M:%SZ'], allow_null=True)
    due_date     = serializers.DateTimeField(required=False, input_formats=['%Y-%m-%dT%H:%M:%SZ'], allow_null=True)
    percentage   = serializers.IntegerField(required=False, min_value=0, max_value=100)

    def validate(self, attrs):
        if len(attrs) > 2:
            raise serializers.ValidationError({'fields_err': 'The number of fields exceeds the limit(2 or 1)'})
        phase_exist        = 'phase' in attrs
        row_position_exist = 'row_position' in attrs
        if phase_exist != row_position_exist:
            raise serializers.ValidationError({'fields_err': '(phase, row_position) are used only together'})
        if len(attrs) == 0:
            raise serializers.ValidationError({'fields_err': 'A field is required'})
        return attrs
    
    def validate_phase(self, value):
        if not value in (p for p,_ in Task.PHASE_CHOICES):
            raise serializers.ValidationError({"phase": "Must be one of these values: ['TODO', 'DOING', 'DONE']"})
        return value

# -----------------------------------------------------------------------------
