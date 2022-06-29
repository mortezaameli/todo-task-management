from rest_framework import serializers
from .models import Project, Task, Membership
from django.contrib.auth.models import User


class MembershipSerializers(serializers.Serializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    inviter = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    user_role = serializers.CharField(required=True)
    confirmed = serializers.BooleanField()

    # def create(self, validated_data):
    #     return Membership.objects.create(**validated_data)


class ProjectSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        return Project.objects.create(**validated_data)