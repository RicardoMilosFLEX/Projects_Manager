from django.contrib import admin
from .models import *

# Register your models here.
#
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description')
#     list_display_links = ('name', 'description')
#     search_fields = ('name', 'description')
# admin.site.register(Project, ProjectAdmin)
admin.site.register(Clients)
admin.site.register(ProjectStatuses)
admin.site.register(ProjectTypes)
admin.site.register(Tasks)
admin.site.register(TaskStatuses)
admin.site.register(TaskLists)
admin.site.register(Priorities)
admin.site.register(Projects)