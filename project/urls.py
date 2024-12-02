from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('projects', show_project, name='projects'),
    path('create', create, name='create'),
    path('manage', manage, name='manage'),
]