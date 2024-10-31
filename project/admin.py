from django.contrib import admin
from .models import Clients
# Register your models here.
#
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description')
#     list_display_links = ('name', 'description')
#     search_fields = ('name', 'description')
# admin.site.register(Project, ProjectAdmin)
admin.site.register(Clients)