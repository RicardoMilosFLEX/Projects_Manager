from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('projects', show_project, name='projects'),
    path('create_project', create_project, name='create_project'),
    path('manage', manage, name='manage'),
    path('managers_info', show_all_managers, name='managers_info' ),
    path('create_task', create_task, name='create_task'),
]