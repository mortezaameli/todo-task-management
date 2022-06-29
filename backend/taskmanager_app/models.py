from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=80, unique=True, blank=False, null=False)
    members = models.ManyToManyField(
            User,
            through='Membership',
            through_fields=('project', 'user'),
    )

    def __str__(self) -> str:
        return self.name


class Membership(models.Model):
    ADMIN_ROLE = 'Admin'
    USER_ROLE = 'User'
    USER_ROLE_CHOICES = [
        (ADMIN_ROLE, 'Admin'),
        (USER_ROLE, 'User'),
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    inviter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="membership_invites",
        default=None,
        blank=True,
        null=True
    )
    user_role = models.CharField(max_length=5, choices=USER_ROLE_CHOICES, default=USER_ROLE)
    confirmed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('project', 'user',)


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=256, blank=False, null=False)
    description = models.TextField(default='', blank=True, null=True)

    def __str__(self) -> str:
        return self.title
