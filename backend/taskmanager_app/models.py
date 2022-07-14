from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Project(models.Model):
    name       = models.CharField(max_length=80, blank=False, null=False)
    members    = models.ManyToManyField(
                    User,
                    through='Membership',
                    through_fields=('project', 'user'),
                )

    def __str__(self) -> str:
        return self.name


class Membership(models.Model):
    ADMIN_ROLE        = 'Admin'
    USER_ROLE         = 'User'
    USER_ROLE_CHOICES = [(ADMIN_ROLE, 'Admin'), (USER_ROLE, 'User')]

    project     = models.ForeignKey(Project, on_delete=models.CASCADE)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    inviter     = models.ForeignKey(
                    User,
                    on_delete=models.CASCADE,
                    related_name="membership_invites",
                    default=None,
                    blank=True,
                    null=True
                )
    user_role   = models.CharField(max_length=5, choices=USER_ROLE_CHOICES, default=USER_ROLE)
    confirmed   = models.BooleanField(default=False)


class Task(models.Model):
    PHASE_TODO    = 'TODO'
    PHASE_DOING   = 'DOING'
    PHASE_DONE    = 'DONE '
    PHASE_CHOICES = [
        (PHASE_TODO,  'TODO' ),
        (PHASE_DOING, 'DOING'),
        (PHASE_DONE,  'DONE' ),
    ]
    project       = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    phase         = models.CharField(max_length=5, choices=PHASE_CHOICES, default=PHASE_TODO)
    row_position  = models.PositiveSmallIntegerField(default=0)
    creator       = models.ForeignKey(User, on_delete=models.CASCADE)
    title         = models.CharField(max_length=256, blank=False, null=False)
    description   = models.TextField(default='', blank=True, null=True)
    start_date    = models.DateTimeField(blank=True, null=True, default=None)
    due_date      = models.DateTimeField(blank=True, null=True, default=None)
    percentage    = models.PositiveIntegerField(default=0)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
