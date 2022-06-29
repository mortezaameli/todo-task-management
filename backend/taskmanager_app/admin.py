from django.contrib import admin
from .models import Project, Task, Membership


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id','name',]


class TaskAmdin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'project']


class MembershipAmdin(admin.ModelAdmin):
    list_display = ['id', 'project', 'user', 'inviter', 'user_role', 'confirmed']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Membership, MembershipAmdin)
admin.site.register(Task, TaskAmdin)
