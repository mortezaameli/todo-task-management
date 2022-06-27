from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=80, unique=True, blank=False, null=False)
    description = models.TextField(default='', blank=True, null=True)


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, blank=False, null=False)
    description = models.TextField(default='', blank=True, null=True)
